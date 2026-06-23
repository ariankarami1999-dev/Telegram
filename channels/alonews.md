<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/CJyCIUPhVO5NWmVKZlnon13tPJ7RRghp6_B3Y-RgkDd97qtf5WAhrqiTXEwZ-SXvTuER-i7vHjpIZrYuJRoy5SaPRStAgpnWCEOBGp_j9qnrT-A5lvQjiGnIWPNHZL7nSDm6_FdEKSYsxy_q2doVHVBU-HlKx0auFB27iW-yUzAfUROc7v_WJ_E5BNWPTna_rYgS8RGIK9baCXki0TEbHNz2EAM-0RQWkauGAwVLq7hvtXoULdIc8jLv8XbTslUIwXuymHj-dr0od_04C157iyi2ri08Vdk3IjJYGKgV8zR6INwPH95CmoKAysIgeoZy0Cvq_Dx8uaq0QtKdRzhOug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 949K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 11:54:03</div>
<hr>

<div class="tg-post" id="msg-129831">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58a20450c.mp4?token=lgvigIb0XsxNprgTyldhGV2O_VlkUXMMtvwXT_os04ZckZUNpfJaCd4cPdzD7Ko5y4t296dOZK19suMV12RRjaHu4ZmoGdabcTzN47-0nd5Q2G7Fv2KAHKQksgLekTK_7BVhzo5rSU6S_SbVVpbK2ARe0jfxJ7WQWITGZrGF3yzhBZHnLFZK_Ra_LtC89PjJ4k9aIb2FN5KfCfcmMbLZJSmZczn0JtT8-6XrdtYzPSvRkfQ-WB4W8vcFtTX0Gbhr-xdqFKkolpTjUOpOrC_qNIG_31Ag_EtthquDBOWWRFty4hmnfI6MTCgZnm0iDv_4WSk2ZbmpC3mzdl-pl-9DxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58a20450c.mp4?token=lgvigIb0XsxNprgTyldhGV2O_VlkUXMMtvwXT_os04ZckZUNpfJaCd4cPdzD7Ko5y4t296dOZK19suMV12RRjaHu4ZmoGdabcTzN47-0nd5Q2G7Fv2KAHKQksgLekTK_7BVhzo5rSU6S_SbVVpbK2ARe0jfxJ7WQWITGZrGF3yzhBZHnLFZK_Ra_LtC89PjJ4k9aIb2FN5KfCfcmMbLZJSmZczn0JtT8-6XrdtYzPSvRkfQ-WB4W8vcFtTX0Gbhr-xdqFKkolpTjUOpOrC_qNIG_31Ag_EtthquDBOWWRFty4hmnfI6MTCgZnm0iDv_4WSk2ZbmpC3mzdl-pl-9DxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی : قالیباف به چین میرود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/alonews/129831" target="_blank">📅 11:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129830">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fec08cc90a.mp4?token=U4BgPv7I36fJe_0vEmjIAiVp3YnWXezHSXvLmmSUWAAH8mKL7mVC_0U37UjwRGf7XyJjIanpdiKdxtnXo3aHIc29MRW1Cmi-_U5ku78dw-ybbXKEiKhq9Kuifr_-SnGpYGEM0I4YaOnz35J5IO8DT1KcsRz3HZq-zclC5xeG4scHfZ8WzSMncjVoeqSnzdFxmBdQ8s3jl_44DVQ69T9czPgb7tiz0TLy-1dNQdoGiCMfe8lW1-eqpwIqXffZVx62NG-lx95VOY8BGf3t854JvTYAC6ZlncMS87CIouk2ZzuKSvBYqLxkXhk6BlPomcpXxrJ5xDGaWps8APgebXJuow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fec08cc90a.mp4?token=U4BgPv7I36fJe_0vEmjIAiVp3YnWXezHSXvLmmSUWAAH8mKL7mVC_0U37UjwRGf7XyJjIanpdiKdxtnXo3aHIc29MRW1Cmi-_U5ku78dw-ybbXKEiKhq9Kuifr_-SnGpYGEM0I4YaOnz35J5IO8DT1KcsRz3HZq-zclC5xeG4scHfZ8WzSMncjVoeqSnzdFxmBdQ8s3jl_44DVQ69T9czPgb7tiz0TLy-1dNQdoGiCMfe8lW1-eqpwIqXffZVx62NG-lx95VOY8BGf3t854JvTYAC6ZlncMS87CIouk2ZzuKSvBYqLxkXhk6BlPomcpXxrJ5xDGaWps8APgebXJuow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مجوز فروش نفت و محصولات پتروشیمی دیروز صادر شد و از همان زمان قابلیت اجرا دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/alonews/129830" target="_blank">📅 11:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129829">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9061886b7c.mp4?token=tl0zx4hFvlTFR_SP5q5UTSaab3M6YGQy4Ej2zCd4AsZTNp5DdOGsVCdFLdkFSWwK1CaaWkVjwal_gDD_BeBUevw9sa179C6qsag5FFx7wrJ63EMg7a0Qs3xvNq0ymvTbXCAo_i44Pg4cSrR_YV0IeTnmm30gF2fB6P4Q_7N2OOYgv7eFr-jRyeCaPU2TEEayKRbW-nfiLa_G9KtYkwQQr_u4sngetnyMZSO5EWZ1BoyzQXMJ5On9TJ78qyRBLUzJl0MXd99ZiAAJX3f9ct5ISoIydHoCD9F6XaaqzCcZwIG2NZ7SC6u8vhau0f_BZDckL8g4lU0ASKZ6_G5F7XgIKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9061886b7c.mp4?token=tl0zx4hFvlTFR_SP5q5UTSaab3M6YGQy4Ej2zCd4AsZTNp5DdOGsVCdFLdkFSWwK1CaaWkVjwal_gDD_BeBUevw9sa179C6qsag5FFx7wrJ63EMg7a0Qs3xvNq0ymvTbXCAo_i44Pg4cSrR_YV0IeTnmm30gF2fB6P4Q_7N2OOYgv7eFr-jRyeCaPU2TEEayKRbW-nfiLa_G9KtYkwQQr_u4sngetnyMZSO5EWZ1BoyzQXMJ5On9TJ78qyRBLUzJl0MXd99ZiAAJX3f9ct5ISoIydHoCD9F6XaaqzCcZwIG2NZ7SC6u8vhau0f_BZDckL8g4lU0ASKZ6_G5F7XgIKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: طرف ما بر اساس یادداشت تفاهم ۲۸ خرداد دولت آمریکا است/ تعهد ما مبتنی بر تعهد طرف مقابل است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/alonews/129829" target="_blank">📅 11:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129828">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5565eeff1.mp4?token=JHnqE-bNyn9vvIOJzIXMuAQJE_7CkHky-lt1r0I4iiVQlWDakinF14Q__fpvwgf80-Nao5nlHbe-hoW_4DREBB52sz49jBLUcc4A4wi2QBGHT9tUMQU8qEY35rYt3mv57_dys7EnVIvvVitOjfazncuAKwSUkAcpSu3lso9pPSSonBewM_fj7BkJORvfwFxzEOmBu3Dy5nswQ2bCgZOmG1YmmZhR7wyaq8W-ZK_Gw4bIdzMgO9gWMYf2s7cOeukg6uIJwPmED2R6UmjYork99_FMp1rPI6Uz8Az3IfPDpZVs6UJoeCC4tKv4rFOaXTR4fsZH072Jvt5JsuZleCh0Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5565eeff1.mp4?token=JHnqE-bNyn9vvIOJzIXMuAQJE_7CkHky-lt1r0I4iiVQlWDakinF14Q__fpvwgf80-Nao5nlHbe-hoW_4DREBB52sz49jBLUcc4A4wi2QBGHT9tUMQU8qEY35rYt3mv57_dys7EnVIvvVitOjfazncuAKwSUkAcpSu3lso9pPSSonBewM_fj7BkJORvfwFxzEOmBu3Dy5nswQ2bCgZOmG1YmmZhR7wyaq8W-ZK_Gw4bIdzMgO9gWMYf2s7cOeukg6uIJwPmED2R6UmjYork99_FMp1rPI6Uz8Az3IfPDpZVs6UJoeCC4tKv4rFOaXTR4fsZH072Jvt5JsuZleCh0Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توضیحات بقایی درباره خروج خبرنگاران از سالن اجلاس چهارجانبه: ما برای کار رسانه‌ای و تبلیغاتی به سوئیس نرفته بودیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/alonews/129828" target="_blank">📅 11:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129827">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
مایک والتز، سفیر آمریکا در سازمان ملل:
جمهوری اسلامی با بازگشت بازرسان هسته‌ای به ایران موافقت کرده و این اولین گام برای توافقی گسترده‌تره.
🔴
برخلاف برجام، این بار بازرسی‌ها باید در هر زمان و هر مکان ممکن باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/alonews/129827" target="_blank">📅 11:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129826">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60eb3a2c96.mp4?token=X0KdLSdztyh2AwKnL6VDSI01kNHEurRb5zxC_Of4leUot36BLMci0AOy3ukz-99oaS-hXMPvSTf61YHJAnmd3MPdzmAwNk38FwVtKW8GxwymTYxC2nKEAjvsV6ApgugBvgO-srs1Dh1KEL24Wpuy-UAGuhJqWeeZhJ5KTiB8SBRlaB59SvwYPFLOTxGDiHldW9I6zCFZ-VW6kvXaWR8pIsXlYcP0qwll2xiRp23itg7xaotRZS9PJUVSGef7GPgeFzt5o8X90JceZ07YvxZp0CqI6Yu0CRbJmu7TTpH9OU3-eFleeGy8fRhSzKnsW1ldVcEG4UdUH5J1LIX8ZlPmgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60eb3a2c96.mp4?token=X0KdLSdztyh2AwKnL6VDSI01kNHEurRb5zxC_Of4leUot36BLMci0AOy3ukz-99oaS-hXMPvSTf61YHJAnmd3MPdzmAwNk38FwVtKW8GxwymTYxC2nKEAjvsV6ApgugBvgO-srs1Dh1KEL24Wpuy-UAGuhJqWeeZhJ5KTiB8SBRlaB59SvwYPFLOTxGDiHldW9I6zCFZ-VW6kvXaWR8pIsXlYcP0qwll2xiRp23itg7xaotRZS9PJUVSGef7GPgeFzt5o8X90JceZ07YvxZp0CqI6Yu0CRbJmu7TTpH9OU3-eFleeGy8fRhSzKnsW1ldVcEG4UdUH5J1LIX8ZlPmgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: توانمندی دفاعی و موشکی ایران هیچگاه موضوع مذاکره با هیچ طرفی نخواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/alonews/129826" target="_blank">📅 11:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129825">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27922d07c6.mp4?token=W99GhJYuFDL67cudiZ43pRaGZEZrXiq4RlQEI7156lWyBNotNth0_2ShE50zWTm1FuGdDRqlLOLO3CkU3yOP0nzUd6xj0beTFEii_fXrxtww7bz7nfcfFaREGDUNWCub_q0yTEetf851vJYYpEIdraL6bbW05rxvIRtPB6zlZlxmcGkFWP5PNJLMviWwhSdgew_aWdqqczJyRxID_g_yQzxVSHvNSJpYCYteekcmFxU7DaejjM1XF1qrTeCRfMb6s9Mx_PiCfirPX4otm7Jz8Rz868cJOisUMb7qU1YDYhp4F-F9yJOvxsneBpVStq1vnAfZ66J1jCXvPjf9Dy1sJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27922d07c6.mp4?token=W99GhJYuFDL67cudiZ43pRaGZEZrXiq4RlQEI7156lWyBNotNth0_2ShE50zWTm1FuGdDRqlLOLO3CkU3yOP0nzUd6xj0beTFEii_fXrxtww7bz7nfcfFaREGDUNWCub_q0yTEetf851vJYYpEIdraL6bbW05rxvIRtPB6zlZlxmcGkFWP5PNJLMviWwhSdgew_aWdqqczJyRxID_g_yQzxVSHvNSJpYCYteekcmFxU7DaejjM1XF1qrTeCRfMb6s9Mx_PiCfirPX4otm7Jz8Rz868cJOisUMb7qU1YDYhp4F-F9yJOvxsneBpVStq1vnAfZ66J1jCXvPjf9Dy1sJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: مجوز فروش نفت و محصولات پتروشیمی دیروز صادر شد و از همان زمان قابلیت اجرا دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/alonews/129825" target="_blank">📅 11:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129824">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: برای ما جالب است که فلسفه و هدف جنگ، که قبلاً اعلام کرده بودند از بین بردن تمدن و فروپاشی ایران است، تقلیل پیدا کرده به ثروتمندتر کردن کشاورزان آمریکایی.
🔴
ما در رابطه با اموال آزادشده ایران، هر طور که به صرفه و صلاح کشور باشد، تصمیم می‌گیریم. در رابطه با خرید کالا، وزارت کشاورزی ما و سایر بخش‌هایی که متولی امر هستند، هر آن‌طور که تشخیص بدهند، هم بر اساس قیمت و هم بر اساس کیفیت، تصمیم می‌گیرند. لذا هیچ محدودیتی در این رابطه وجود ندارد.
🔴
مجوزهایی که در رابطه با بحث فروش نفت صادر شد، از دیروز اجرایی شده است. سایر موارد هم مشخصاً در رابطه با هزینه‌کرد از دارایی‌های محدودشده یا مسدودشده ایران به همین ترتیب است.
🔴
آقای همتی دیروز توضیحات مفصلی در این رابطه داد. مهم این است که اموال مسدودشده ایران در دسترس است و برای استفاده آزادانه ایران، هر طور که تشخیص بدهد، برای تأمین کالاهایی که مدنظر کشور است، قابل استفاده خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/129824" target="_blank">📅 11:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129823">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
بر اساس مصوبه امروز شورای شهر تهران، مترو و اتوبوس‌های بی‌آرتی تا ۱۹ تیر رايگان می‌ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/129823" target="_blank">📅 11:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129822">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
الجزیره: «تغییری بزرگ» در سیاست آمریکا؛ ایران اکنون می‌تواند نفت خود را با قیمت کامل بفروشد
🔴
این اقدام صد‌ها میلیون دلار درآمد اضافی برای اقتصاد ایران به همراه خواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/129822" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129821">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d72b824858.mp4?token=f-CjY6gqBkMAnv6QQA0r0hvdlX1HiT_ZdpMAcD1RSiCtcHfv673clIRc0-sySI9YD1oVawIl4HZ25a8toCF4ApF6nHZ0Fjd06B5e5sj6W0T16K2-Hx5Ofa2YHvz47xr7_-P85fA7a9quCbwzE9Q1W6gTbWfBjaIb_cBFLgUx6II5w8GwaVfO4rIz67R-j3CytubCIi7Xqqa21Yh3edULMXExrABrKvofD_pg3Bk4LU7iVZXtJTNaSOE6ZwLvXkT8pmP_ekB-QC_d3v3-l8rmABpbnZLid587zZfaKzU2lcnzDkGQPK52e31njIwNrw3xZVZmSvVgrOiep588Dnk_Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d72b824858.mp4?token=f-CjY6gqBkMAnv6QQA0r0hvdlX1HiT_ZdpMAcD1RSiCtcHfv673clIRc0-sySI9YD1oVawIl4HZ25a8toCF4ApF6nHZ0Fjd06B5e5sj6W0T16K2-Hx5Ofa2YHvz47xr7_-P85fA7a9quCbwzE9Q1W6gTbWfBjaIb_cBFLgUx6II5w8GwaVfO4rIz67R-j3CytubCIi7Xqqa21Yh3edULMXExrABrKvofD_pg3Bk4LU7iVZXtJTNaSOE6ZwLvXkT8pmP_ekB-QC_d3v3-l8rmABpbnZLid587zZfaKzU2lcnzDkGQPK52e31njIwNrw3xZVZmSvVgrOiep588Dnk_Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی تکذیب کرد: نه دیداری با گروسی داشتیم و نه برنامه‌ای برای بازرسی آژانس از تاسیسات هسته‌ای آسیب‌دیده ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/129821" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129820">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9MBclp_xAb_kk5FtAjzv5JDOLThg45QbB4xu-eT2o8G51yEJ1nizxtq2iyWsl11A5URKaPW_ZaMf2hBJqZW3QW4kuou82FenVWKpEq5u4-yXZJReY5TR1VSAyZXC1WLmkT0N9sl9PX2DayXbNltJhoSHZhr938fXQEya4X7O2gvOkogfV_OYLmYIR65Nm1dY-sP2yNiaLbh1SilNdzsuHOED0sFRms1hjszJPTarCALzrETTXHC-FhfJAgKdTiCyZEDMKr-U2FLYbZGYdLLYf2Jlw8m91h6FmvRXRNXQK6bhaFRrA6ZgJaEb7X_bsYB3wyALf3t9A7_9Cone7NC3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز:  روبیو با وظیفه سختی برای متقاعد کردن متحدان محتاط خلیج فارس در مورد بازگرداندن روابط با ایران روبرو است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/129820" target="_blank">📅 11:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129819">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سازمان ملل: برای نخستین بار از مارس هیچ حمله هوایی در لبنان ثبت نشد
🔴
استفان دوجاریک، سخنگوی سازمان ملل، اعلام کرد که روز یکشنبه نخستین روز از زمان آغاز درگیری‌ها در دوم مارس بود که نیروهای حافظ صلح سازمان ملل در جنوب لبنان هیچ پرتابه یا رهگیری هوایی ثبت نکردند. او افزود که این وضعیت تا صبح دوشنبه نیز ادامه داشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/129819" target="_blank">📅 11:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129818">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXPP5_ab-ts5lUhpnDggMZZ6vORrceY8Q3PH9OJ6I_BuUxwux8KPOWrKsPllAlfiTTyCL6XSr0pOuriOL06Gd8sZs3edNwdzYrHqteYsIqTlDFdPVONSntHJRGAay87Sl3ncmisaeS2nZX2ZKQxoSoI3Rg84BHBWp7AegPx-opcimwjd2GiinFUtCLs09_RQeJBgl9lVdsZmv2PB9hGtsQ_kgevexYZmZ-rtmh6sVdY7_R8_xR02RnDCcFZhCtlDcarmooZ8G1OUrJM9xqLBgFg9-FjGReWoFAca1512nz8puvDfvhK0AcZ9aT6-QERGYRiCBELJGe01o6fPqIrF8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سلیمی، نماینده تهران: با توجه به تغییر شرایط، آن دلیل ابتدایی که موجب می‌شد صحن تعطیل باشد، دیگر منتفی شده و ان‌شاءالله به زودی شاهد بازگشایی صحن خواهیم بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/129818" target="_blank">📅 11:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129817">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpiqPZcp4KsQDYX4iI13ZQB99j9LIs2ktJJWNU8tV5SnPQIR6y2lSE8Gy9ocVGu4Ad_IPzN4tCVIFBj-OQqk7meO3OoGOO3nsJE0HfiAmjJkGc1zzRuv8H-2Q5TLegfoAe1wn_aZuIGp3-_pad6hJnfFtLK4LMkGNXTAWTUPK_YRPOKJmSHKszhhn1DatrlHuvapl1Y52ME5JcylCPWHnkwVyr3B6fCOcVa5H4xHshajVykHnyh3sC4opmxvS0CFCPszrXqvkIVVt1KspYMPT0VOnzv_192I4UZeKB17EWFSFmkId5e_KT6HGOte5mEwPNqp7Wrxkq90JnSnN3EbyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: اونا مردمشون رو گشنه نگه داشتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/129817" target="_blank">📅 10:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129816">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزیر دفاع پاکستان: حصول توافق میان ایران و آمریکا ممکن است به پایانِ حیات سیاسی نتانیاهو و حتی بازداشت او منجر شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/alonews/129816" target="_blank">📅 10:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129815">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
پزشکیان عازم پاکستان شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/129815" target="_blank">📅 10:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129814">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EB9RRw9IVQEFFQsduGOCNlP3FxcS9QcKxL2cScXmXuEbp5Iyw9_h6dpo0gCZTUsDJeR9T59LuNXTspyxaV0k35Eo4oQWRTa_N21ZJMYXWRAjHjjCbF7SR_v8TXlLkCNhknq0kGc4srL90sruyBG0u0s9oucbdCViEiJEDN3D-CIDJRYo0CBA0RTc0uUTybgZ4jDMbnQrZ6DF05rq4oKnFhwwswjSE_Ief77Xno97meLzgwGltV3iI63O7j7uEI9IuHCmygG8xYRcOGkkxiuMx1OkaFgtW4DikKNWJAmy7lcrFP3FMqFzvfW2FUZ3wnrx1kzDK3o7EDU5SkQiBeIZYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زنگنه، نماینده مجلس:
یکشنبه آتی، صحن مجلس، کار خود را آغاز می کند/ احتمالا با موضوع بررسی روند اجرای تفاهم نامه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/129814" target="_blank">📅 10:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129813">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16290e355b.mp4?token=G5m_tu-BlhIs3C3FixoszW81IdejwxufeXT-mTWN77aKUv8VA35Y9JW2MiExl4MsG0Bv4UNtCs2-5Zi_z-0fyxep99kjADqC7N9hrWEOn2dJcLbdDy2lAXjRwI1eXRtYxknlswbyijQDh3IwrwGzNwGFhufGyYLN-AoY8CJP4WoT8OxRgtGq3zVEx9DDCZEL82Pr3mlHB9ip3p30Tr4fZWJOwrf1b3d0oJEpA3tt1nvxJ9sch7nQYH2xKgS6SjXpwicNvJVhgX-sLL_WOse3__AqcqM03YW6UkgmGHCVok459jR9aEiWJrnhH7cwZIh9YIu_Ms53_NJ10r4uQH2W6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16290e355b.mp4?token=G5m_tu-BlhIs3C3FixoszW81IdejwxufeXT-mTWN77aKUv8VA35Y9JW2MiExl4MsG0Bv4UNtCs2-5Zi_z-0fyxep99kjADqC7N9hrWEOn2dJcLbdDy2lAXjRwI1eXRtYxknlswbyijQDh3IwrwGzNwGFhufGyYLN-AoY8CJP4WoT8OxRgtGq3zVEx9DDCZEL82Pr3mlHB9ip3p30Tr4fZWJOwrf1b3d0oJEpA3tt1nvxJ9sch7nQYH2xKgS6SjXpwicNvJVhgX-sLL_WOse3__AqcqM03YW6UkgmGHCVok459jR9aEiWJrnhH7cwZIh9YIu_Ms53_NJ10r4uQH2W6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقوع یک آتش‌سوزی در شهر هیوستون ایالت تگزاس آمریکا موجب برخاستن ستون‌های عظیم دود بر فراز این شهر شد
🔴
تا این لحظه جزئیات دقیقی درباره دلیل آغاز آتش‌سوزی، میزان خسارات احتمالی یا تلفات انسانی منتشر نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/129813" target="_blank">📅 10:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129812">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R681S-JmZv48xhBR_j6AMw_usULnuPv8yfJxwPrzGnyl9XNRVcFdQDJ4Yx3aPPo5834dAvo-GGy-cMolgCxCt-2XgnnChYyBdrsJkMs4tXdTU363-lCVknxQGHLZA-e4UkQchM-AWQ-5UNJNRErVXbV-nV7CMx9x3FC-50bF5teKvSHYeWhibUnuHmZPORcKLgXh3ayjY-xHi_5TxQeogjyr4IcPpdxvnhTUFYmsGNjH4ERIfIBszS9ySEiQ7-hBxvi0jhJpFs81NRDP0dXILss5G8cUXJDbhe2maXgQesfSEdEz19UwMy9iKoW8AAph_69TgkglffYnkIDd0t27tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقامات بهداشتی کشور کنگو اعلام کردند با تشدید شیوع ویروس ابولا، شمار مرگ‌ومیر ناشی از این بیماری به 267 نفر افزایش یافته است.
🔴
تا کنون 1048 مورد ابتلای قطعی به این ویروس مرگبار در این کشور به ثبت رسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/129812" target="_blank">📅 10:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129811">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
روانشناس اسرائیلی ، اوری گلر روانشناس مطرح جهان به کانال 14 اسرائیل: ایران از سلاح الکترو مغناطیسی با فرکانس پایین برای شستشوی مغزی و تحت تأثیر قرار دادن ترامپ برای پذیرش تفاهم‌ نامه استفاده میکند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/129811" target="_blank">📅 10:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129810">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
کاخ سفید : به هئیت مذاکره کننده اعتماد کنید
🔴
آنها به مذاکرات ادامه خواهند داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/129810" target="_blank">📅 10:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129809">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
داده‌های کشتیرانی: طی 24 ساعت گذشته، دست‌کم 20 کشتی از تنگه هرمز عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/alonews/129809" target="_blank">📅 09:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129808">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش :بر این اساس، امتحانات نهایی پایه یازدهم از ۲۰ تیر ۱۴۰۵ و پایه دوازدهم از ۲۱ تیر ۱۴۰۵ طبق برنامه اعلام‌شده برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/alonews/129808" target="_blank">📅 09:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129807">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نتانیاهو و وزیر دفاع، کاتس :
ارتش قراره همین‌طور ادامه بده تهدیدها رو خنثی کنه و تو منطقه امنیتی جنوب لُبنان بمونه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/alonews/129807" target="_blank">📅 09:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129805">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ترامپ: خودروسازان آمریکایی تولید سلاح را آغاز خواهند کرد
🔴
رئیس جمهور آمریکا در کاخ سفید به خبرنگاران گفت: «آنها برنامه‌هایی برای تغییر کاربری کارخانه‌ها دارند. ما قصد داریم سلاح‌هایی از جمله موشک‌های پاتریوت، موشک‌های تاماهاک و موارد دیگر تولید کنیم.»
🔴
طبق گزارش‌های متعدد رسانه‌ای، درگیری با ایران زرادخانه‌های ایالات متحده را به طور قابل توجهی تخلیه کرده و خطر جنگ‌های جدید را ایجاد کرده است.
🔴
در ماه آوریل، کانال‌های تلویزیونی ایالات متحده ادعا کردند که تنها در هفت هفته، ایالات متحده تقریبا نیمی از ذخایر موشک‌های پاتریوت و حدود ۳۰ درصد از موشک‌های تاماهاک خود را استفاده کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/alonews/129805" target="_blank">📅 09:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129804">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d480841643.mp4?token=QTmrMC9ECJYGyHn7H2PELgsqIovO3sst-dDOFwaiXl0T9b39yuE449NKti8BczFI7BJzo1QDkibDFlGk3df0GLd6wqNNFOX1vAHwoyIT1CCk78g6tNZEz96y-yHDKTL5ofMgxjFy_x3xKVTNExqIwvdeYAV3WafSvy3TOYyBQCd0Jas5pbnnWlq1J2uoP3e1UnH0UAiWwSE0Qg4xmUrjEwNGqcs4Kf21bIIHInbvNc3F8d89CG31AXiCKNLyeocYDtcXziF8HnKdxml1ZBhrn1egq1oSQoaq-kXAeYgJpfy0QIm1XtkLF5aZdLlzOTkehZCObPq0KQon3-FaCUOUuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d480841643.mp4?token=QTmrMC9ECJYGyHn7H2PELgsqIovO3sst-dDOFwaiXl0T9b39yuE449NKti8BczFI7BJzo1QDkibDFlGk3df0GLd6wqNNFOX1vAHwoyIT1CCk78g6tNZEz96y-yHDKTL5ofMgxjFy_x3xKVTNExqIwvdeYAV3WafSvy3TOYyBQCd0Jas5pbnnWlq1J2uoP3e1UnH0UAiWwSE0Qg4xmUrjEwNGqcs4Kf21bIIHInbvNc3F8d89CG31AXiCKNLyeocYDtcXziF8HnKdxml1ZBhrn1egq1oSQoaq-kXAeYgJpfy0QIm1XtkLF5aZdLlzOTkehZCObPq0KQon3-FaCUOUuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک روحانی: اسم بچه‌هاتون رو امیر نزارید، ریشه این اسم بهایی هست
🔴
امیرها همه آدمای مشکل دار و ناجوری هستن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/129804" target="_blank">📅 08:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129803">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdrRjSedcVzS_soy8IcsKxllOJ7wqGb_Abe-s8UydGWJDek-l9CkKFXVuLgyu0SlUqDYZrU78AEGBML2bWD7siCcSgom98Jc2RRHmUN2oYeQIwoTDl3SV5hbL4KS06LerUZ27CFTNAxtVNd6crYO7FyKL2GHkCOVRTwQhuA3pmc-YVUyM_plPga2X0wLq1tatO8rerkI1oO7ix-KDRk_Lx9rNFFL6Ytv-tpgmHj0_97GaB70a6uril6SJR14pUGGCtAx7KBZdWzhKixPq4vtCsVVaMV5VPF7NkQE5lTNwaJLm1OD1UfQQLt4RiRh0dt-4pMlV7SG-ezF-tFrotKM0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غضنفروف نماینده مجلس: جمعی از نمایندگان یکشنبه به مجلس خواهند رفت؛ اگر در بسته بود همانجا تحصن می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/129803" target="_blank">📅 07:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129802">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Du5afVZmbcSX9Rgs1ktf9dV77vjLDZRk1-1m2UKExr6HFqNa8m-vbNk_7Nq-CA8eVJLGdTQTnuu9D5-lJoP3COQC_TM5zLQuftcU7LPHN_0IS_58gxlW18TI_gIIDxH0dsaiApg2QMMjBVgecZ_411BOj8Npmxkym3LxEbXEEgb6qWd6_0f2JuEDtpXFFBpCMbOHNFfR7T2fuw-yiYJGi9LioRGF44_vfyGD-PQlItjwjQMWlf_1iRLfp640-YbOHQMGBMHIvuSwZUFb_jZtEpRAUmkstvL8HfNvKzqYGYL_8nB0-XxIfKRKjmfAbaW9_BNmeCTB8vLeyQZL_VAbew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: مفتی مفتی تنگه رو دادیم رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/129802" target="_blank">📅 07:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129801">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبارفوری مذاکره | مذاکرات ایران امریکا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdMPO5m14LRUHCVhF-DPxDD5IV9CUjwgVWRW5VcZdsG6J3Q1VbF7bfqkMLPRuxmVK6Bb4zjGtr_i0DWpBfvpIbBP2Y85bugPzSY0SddhY_0faEByJqMebUooWIQFZnyZpDIds-Qt1HACjnEvp7EAfiQQlRaWc1wJ175YcHRviUQh82PRGspkBYP9fYj60_4EJCGGRL5ni6K2U0pkhMYp03mUcy8pK3pXdAcvGQ1SOpHzlyNbItZfsbBN7BxBKSyMBy-fRkbhgpQa3RtY8925Papy7om7kKK8XJTL-l6cPjgVrBo_pqIx9udcjKZskKmFJ6-MOcK2jUD90pyVCCxHVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/129801" target="_blank">📅 01:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129800">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxU-TmEIw4VRdBgu5_UidhYnZA2vl_YXKqgfwwHcLEy_jquGacUGpAFS54aLuY_yIhJ7bTvQ7i3PLLNTBTW-MXxw4hM5VQH839z17C5RRg-ILrni37Ne2hbx3_9PzkLIrL3hraZStYwcOtJTh9w3liJklaqhecgnrhPOk4M_ZLJhAuUlotBzQGTqZc6Zt9dsj3imbleCFMYCsalJGNiLwmYQweqBQhLf4BOfNX2W34qIYX84hUclI1sMh3yfTG4pKBkxUHWd3KZWFANC59fYqYOXfRyzHWGY8ElYnd8noCYY2ifHQ8thDJ4aM-iN16LKXNR2r3gnYH4R0COuBtIqqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عماد الدین باقی: طبق بند 2 توافق ایران و آمریکا، از این به بعد شعار مرگ بر آمریکا یا سوزاندن پرچم این کشور و لگد کردنش تو مراسم‌ها و اجتماعات رسمی (مثل نماز جمعه) ممنوعه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/129800" target="_blank">📅 01:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129799">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وزیر خارجه عمان: به قانون بین‌المللی و تضمین عبور امن و بدون اخذ عوارض از تنگه هرمز  پایبندیم. به مذاکره‌کنندگان ایرانی بر تعهد خود به قانون بین‌المللی در ارتباط با تنگه هرمز، تاکید کردیم. مذاکرات سازنده‌ای با قالیباف و عراقچی درباره یادداشت تفاهم انجام دادیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/129799" target="_blank">📅 01:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129798">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAZixioSL5fSCXY_YrNBDJSPdgWq2CUCO83iVTDRSRwJN38wS09u_toRkOjK0Ilazm6KkZgH7V1HQm5W4YLCoj0UQMhoV_BRSkVuSAPbxp91On9NhKYGDvRNRc-j5ACrHF6Tm5Vlhs4nul6DVewwJ3SB0HT3BENZCT3RxBSNtfwCRlH7fa6J0xKBOgXDV2fXUQpqOfeVSduUP4trWWLQj-TOPoKeXBCTt9F5SAUEL7uUBHBirVtW_TiLJye1ANzUZJwjtG_20Cdby_XS5NrGeV_IcUEmpGOwAX3702E5TepPE0mnyL8wmDuC_jlReh_muB8zR642CXh9g-m47Owo_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چند روز دیگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/129798" target="_blank">📅 01:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129796">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
گویا علاوه بر سویا و گندم، قرار است سیب زمینی دشت مغان هم از آمریکا خریداری بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/129796" target="_blank">📅 00:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129794">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3WswkqEYdpVeE9YDg_lxzSgdscLWtdCXB2ItpEaBYR53BwCv1LA3qcODtOsPLliB05BsT4rPPtju5pUfQTYbkDvZ0i3O7fZ97C5TJXF_p23mx7teaairAjxPOL069OHOPQvWEtZgPy130m_xMvRWZq-k0NeQNJQvtMnNPv1zN2Y5pvVy12G6Q7mwbDl7u6E06lAJ8gL-O-SA1zasZJLIqQEja7LLdWxwwGNr5EC9u4Fma_0YOO6NkV4TeB55KJgwbMB6ptcKdxLIxNC1mQBl6BmDfiAPbQncbNlo0NlHqzIF2xwfkk0CJaJK9REIyr4VPOzYz1JQouoabhIg7H58Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vlAXTTexYnqmyPV6Vb6zcVVl8hQlaWlc5AB6w5f57Ackayh3WE5W0eN7sC6QJCxXaeJbw9mj8p0HTtNViKQyMBWzBqA6w0FOMNW30dHLO56fOOs8a0Lo0MoAZeudOg-vSrGSDqfpZ16aDiOFTep1YKbFhcpDeLJlaA2zy3-w0_o4wi_Pvt62bXNm7Z7g58YICxO6RHEYU9lgNXryMkC1KVojtMfbKzvNrdNJt8mxX6-LkwhUPc5OCQV4nYFbNxlcrfWBMjkMnnEC8o2nsUt2B3lXPaeCZ0c5qvnZGZ6c_EPzKDZNHAEbzqTL4yhuT1shMyCz36NdsZZinEdez4503A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایران صاحب پیرترین ترکیب تاریخ جام جهانی شد
!
تیم ملی ایران در دیدار مقابل بلژیک با میانگین سنی ۳۲.۵ سال، پیرترین ترکیب اصلی تاریخ جام‌های جهانی را به میدان فرستاد و رکوردی تاریخی را به نام خود ثبت کرد.
@AloSport</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/129794" target="_blank">📅 00:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129793">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
یکی نفت رو میگیره بجاش سنگ پا و سوزن نخ کن میده یکی هم پولا نمیده و بجاش سویا میده
🔴
دیس ایز ایسلامیک ریپابلیک آو ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/129793" target="_blank">📅 00:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129792">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e0b59223.mp4?token=ewA3AM7OO_HdZJztuOqU3hAtfsTCsvi03vkxl6CBA7pxq4I_FxBo1PoJ0TXWUEzaNHoy38t6aQHn9d_DkupE-UTE0MUVbBkpcMrT3NIsrCrj1B7E-QeznFD4-MiLOHqwPL5i4ssdW8XJoXrIfpJOB1HhHVdvrj5--yP6sh9cmBAks959GD-2yDMT0Nav9VWPx8drMciHRSdLVjOCBRmh6nGO5zObWN_jK3yTCit8brL2CDp43gsItBDn8QjgHkhjBhSKPh26Sb91hneK-II7gOM6uamrcdYeMdsF4_EGABZ_kPhylypspqYfsJW_EewJZkjXzRhN06CmqtPW5eiisg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e0b59223.mp4?token=ewA3AM7OO_HdZJztuOqU3hAtfsTCsvi03vkxl6CBA7pxq4I_FxBo1PoJ0TXWUEzaNHoy38t6aQHn9d_DkupE-UTE0MUVbBkpcMrT3NIsrCrj1B7E-QeznFD4-MiLOHqwPL5i4ssdW8XJoXrIfpJOB1HhHVdvrj5--yP6sh9cmBAks959GD-2yDMT0Nav9VWPx8drMciHRSdLVjOCBRmh6nGO5zObWN_jK3yTCit8brL2CDp43gsItBDn8QjgHkhjBhSKPh26Sb91hneK-II7gOM6uamrcdYeMdsF4_EGABZ_kPhylypspqYfsJW_EewJZkjXzRhN06CmqtPW5eiisg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف و تیم مذاکره‌کننده وقتی ۱۲میلیارد دلار رو میدن تا از آمریکایی‌ها سویا و گندم بخرن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/129792" target="_blank">📅 00:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129791">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommorteza</strong></div>
<div class="tg-text">داداش حساب کردم پشمات میریزه .نفری ۷۰ کیلو غلات میرسه بهمون</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/129791" target="_blank">📅 00:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129790">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiLzPbwgzvcLKJge2sV3cnImQsFzMF9yuVloKrTguMkAQuCLb6GOaWjkBlDdEYJbkGcydehglT066Ti1eHsdMm2P1oBJ_YW-i6iqCbOscGH1EhOel9oRb5K_D_6aVEjl-apj7OFanKqLiqfK0y3Zaa82gbfoYcjKAgTu9mb6A0P2FBCUAKDzLFD3hHA26XMhMrvV1glHE_iamr2lrIGKFOHivgzFo-Fdem2RaKJ6cd2DMkVrI1e68UJNxq1QczYccWep7Z9zmTjmPHHQylMG61ZqolBRgvvrgX4b9JzsBobjXFbXGIOKea3fpU3gpqmehd3GPlNRJXsp3XPVct7Guw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همتی: اگه آمریکایی‌ها قیمت سویا و نهاده‌ها رو خوب بگن ازشون میخریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/129790" target="_blank">📅 00:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129789">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oroXI2XkcOMktPzp2i5SKH_Fq6OPKzWeNpyV_DN9tIK2vtCRvvxtwrwLqSj3GsNlkul2nPCms3a9kyOIYtI6Vv3T20NhHm5-AwwhDNmpjrQTgkMAuESniTEKcfaxoT_H3mW_wAZ50XotnjP_uV-j7gDh53am0X5vMZV4FJwRPG3OeqW2UDCgXons5YrNXUFG_Y44_8NfxLASTH1gI2rFLjR48ISSbj9TpyGTenRLTu3Qy8sNmjTbDf5UFfjwC0-jLJsgKFAhGEzSd49M83cc3Iy2KR6uv17yp9WdULriJQnpFGkxVaPAFxATFuaSRBbiS_2D-XtIpdh8aihLuod7rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم:
هر پولی بیاد ما موشک میسازیم تا اسرائیل رو نابود کنیم و به آرزومون برسیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/129789" target="_blank">📅 00:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129788">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sG2d5pNA8TmMkXW77gOhx1iw3LMTkfFQpTYMfnTBn2AveOoKQNNEFOImDibk6fmJVoJIK4eKtFkCcAFzi72ndWI6K-weHSeamzIVBz5aOD4994LtJNmjVd_Fy_pkg8DoMC1vX2xZQGc2KtSJgTU-R-2dy0uXripOOev6r5CNsvz_DIID13rhyyUeeq7VwkGDzSaDtPtEpmz2d7MNL0arlT1E2o_lRRm9zCAbEJtjQvQ_MSO_54emrOiXycN5IO54dMFPGQA2VIazbSG8qrmMZ0L43L7v_osT8burDgh6nUJKFwoPBWoRouzE7gG9O-W86IXh4ccY5QpGAj-xn87yoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: با آمریکایی‌ها عکس نمیگیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/129788" target="_blank">📅 00:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129787">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
خبرنگار : سالگرد عملیات جکش نیمه شب هست، اگه برگردید عقب، چیزی رو عوض می‌کنید؟
🔴
ترامپ : نه، هیچ چیز
این موفق‌ترین حمله‌ای بود که کسی تا حالا با بمب‌افکن دیده؛ کاملاً توان هسته‌ای‌شون رو از بین برد
🔴
اگه اون کار رو نمی‌کردیم، الان اسرائیل وجود نداشت و بخش زیادی از خاورمیانه هم از بین رفته بود
🔴
اونا فقط دو هفته با ساخت سلاح هسته‌ای فاصله داشتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/129787" target="_blank">📅 00:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129786">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ درباره ناتو و ایران:
ایتالیا خیلی بد بود. آلمان خیلی بد بود. ناتو برای ما نبود.
ما سالانه صدها میلیون دلار برای دفاع از آن‌ها در برابر روسیه هزینه می‌کنیم، و سپس آن‌ها به ما می‌گویند، «ما ترجیح می‌دهیم کمک نکنیم.» حرف احمقانه‌ای است.
چون ما می‌توانیم این حرف را به آن‌ها بزنیم اگر بخواهیم، و ممکن است این کار را بکنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/129786" target="_blank">📅 00:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129785">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ درباره ناتو و ایران:
من حتی به کمک آن‌ها نیاز نداشتم. بیشتر از هر چیز کنجکاو بودم.
از آن‌ها خواستیم بیایند، اما برای ما نبودند. احمقانه بود که نبودند.
استارمر آنجا نبود و مردم بریتانیا از نبود او خوششان نیامد.
استارمر به ما گفت: «به محض اینکه شما پیروز شوید، ما آنجا خواهیم بود.» من گفتم: «وقتی ما پیروز شویم، به شما نیاز نداریم.» این وینستون چرچیل نبود که با او طرف بودیم؛ این را می‌توانم به شما بگویم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/129785" target="_blank">📅 00:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129784">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ: اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من آنچه باید انجام دهم را انجام خواهم داد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/129784" target="_blank">📅 23:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129783">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ: اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من آنچه باید انجام دهم را انجام خواهم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/129783" target="_blank">📅 23:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129782">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb4f50edba.mp4?token=HVuoTKP8a1AdISmKqSJcVN65zDLOKfg2QlNGCQBASIlgtK1DLkWZUGL8EqfbcXU4LVYhwZifQs4Ww78mjhHi29dGyMlNTeMKGrv8RrWfIlO36CPOIUWBSttKDlvmhDVdZYtaC7J5FCKMLF4k0SiJQnFM3aYxIGwTTAUd597ZgSZq2gNDBEgbfKIoNxVsIAjXu64hqeRsj-EzcP2dwg63B2eGoISz-hMFsUPnfEa6Q-GyYkSc-FtjAK1GbHI1i2UCVrFLUr973XSaabqWwZnlgJnQBN3veViBhY4kN76bcwr73Y_6xqTvjK_0WlAv5g3vLeM_LfanoBIckq5tOzr5qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb4f50edba.mp4?token=HVuoTKP8a1AdISmKqSJcVN65zDLOKfg2QlNGCQBASIlgtK1DLkWZUGL8EqfbcXU4LVYhwZifQs4Ww78mjhHi29dGyMlNTeMKGrv8RrWfIlO36CPOIUWBSttKDlvmhDVdZYtaC7J5FCKMLF4k0SiJQnFM3aYxIGwTTAUd597ZgSZq2gNDBEgbfKIoNxVsIAjXu64hqeRsj-EzcP2dwg63B2eGoISz-hMFsUPnfEa6Q-GyYkSc-FtjAK1GbHI1i2UCVrFLUr973XSaabqWwZnlgJnQBN3veViBhY4kN76bcwr73Y_6xqTvjK_0WlAv5g3vLeM_LfanoBIckq5tOzr5qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: اگر به سوئیس نمی‌رفتیم، هر لحظه خون بیشتری از مسلمانان و شیعیان لبنان ریخته می‌شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/129782" target="_blank">📅 23:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129781">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/054f327a6d.mp4?token=H_0PgpCfJtQdmv11OU1XojWfcHD23b0iKmahjGrHRJKMwaV0l5TaCbBza7X2lNi1F9hp6mRJNl3JBxyaADjD-Ju7pyYTDimp9j2wwjYBZ7r74BLX0AxpExaYG8-VUmKSfhDRNfS6FDoCw3QNZwsc4aoofwXAzb7ZqoLSE7ow7rzxVFuC1GXEfB1r0m0B6daaHM-pi-iQQOX5iaTk7wCQHh3Wio1MN3s_tiktE7-gKaCmf_J-O80QEWEWdXFzcp-8qZIVK5oM8sjkNSSz-mx_ePd-FOE1ozrYUgE_dd3-rjVjPj1fyrFSXhLxoQb-XFEvcwuiX9rqPptdJodJx1aCPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/054f327a6d.mp4?token=H_0PgpCfJtQdmv11OU1XojWfcHD23b0iKmahjGrHRJKMwaV0l5TaCbBza7X2lNi1F9hp6mRJNl3JBxyaADjD-Ju7pyYTDimp9j2wwjYBZ7r74BLX0AxpExaYG8-VUmKSfhDRNfS6FDoCw3QNZwsc4aoofwXAzb7ZqoLSE7ow7rzxVFuC1GXEfB1r0m0B6daaHM-pi-iQQOX5iaTk7wCQHh3Wio1MN3s_tiktE7-gKaCmf_J-O80QEWEWdXFzcp-8qZIVK5oM8sjkNSSz-mx_ePd-FOE1ozrYUgE_dd3-rjVjPj1fyrFSXhLxoQb-XFEvcwuiX9rqPptdJodJx1aCPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: نتانیاهو می‌گوید نیروهایش لبنان را ترک نمی‌کنند
ترامپ:
🔴
ما قرار است به این موضوع نگاهی بیندازیم. من یک حل‌کننده مشکل هستم؛ می‌توانم مشکلات را سریع حل کنم، از جمله با بیبی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/129781" target="_blank">📅 23:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129780">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc43c98ca.mp4?token=LLfMXJklF6jDFdQJsnufSP-dPPd42hHoU2QCOJh1neQyYrA0am9D45d2AEz51t82U9r-GK-FPbwMG_cmivNWePsi0mQvSohhWmTFBYuecaF3MSbTo-xpYx2g4gwa7JFKjx6fgDgozH6YpOc1UQH3KlMO-nvIcWOSLQ-V95pcUw7X1Ef6s-nNHX0-K_T_5tbHchQC0S442OTPVJLYTLQIm00eU6jcHfqVW5J8xKmAtaV4GM3MUP1dVMPT19h81MvG9qDLlTpC0IurNWGUARVHg8yu17sc9aeJeBBSro_E9RN1MWH5H-320Manc8BurK9EoY4W2mg8olTj3bpZr7Jm-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc43c98ca.mp4?token=LLfMXJklF6jDFdQJsnufSP-dPPd42hHoU2QCOJh1neQyYrA0am9D45d2AEz51t82U9r-GK-FPbwMG_cmivNWePsi0mQvSohhWmTFBYuecaF3MSbTo-xpYx2g4gwa7JFKjx6fgDgozH6YpOc1UQH3KlMO-nvIcWOSLQ-V95pcUw7X1Ef6s-nNHX0-K_T_5tbHchQC0S442OTPVJLYTLQIm00eU6jcHfqVW5J8xKmAtaV4GM3MUP1dVMPT19h81MvG9qDLlTpC0IurNWGUARVHg8yu17sc9aeJeBBSro_E9RN1MWH5H-320Manc8BurK9EoY4W2mg8olTj3bpZr7Jm-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ درباره ایران:
باید مکالمات آن‌ها را بشنوید: «چه کسی می‌خواهد رئیس‌جمهور شود؟» «من نمی‌خواهم.»
هیچ‌کس نمی‌خواهد رئیس‌جمهور شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/129780" target="_blank">📅 23:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129779">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15fe6d2c2d.mp4?token=no5-QAYRpMFeEUKVWC5aN5gct0deNsGL9WiCGZSNLpVL_ybzK2cWcnqAaOz0s5a6xjzAc_Uoy25d9GZcX5ZzoZ_yeRZdOaTRMDEGU7wOWLr5Yu2KnZwM5AocgCaeIPJXJ2lfNQLquKjhRPu3_S91J9qs2FfTzm0jsFmmdOA3BG-BFBRkRUFLzK8VSBky_uz99_1AqG3fkI5Cvbud6GCf62Wvgtck2Eco9AqvlbxTrZWvHJ_XyxRPoeGLG_mOC69j3M7xPEWl1ebtyZxup1OXDnCODUyvhdjNwXx2qXPL4uuTSaesB0wxqkxby0KSPAOYrrjopeuqASkbOcJkVADTJBSxyxzToJAqpoBAQB_QhtsU-6SwyVH4lPdGPERh-qMeVa_mV0UqSQ8BwUOTP5F-Kc_6E6YrV8g-9XwV6OUUKeYXxS3jY8sQnfIpBvf_J6Ii38r3TVXnELNXmpNYVNWbQm0EVB7o5NBVLYlz6BnT-XMiSdJyVhIqbiDiZXRIlFp472bE8Q-WvOylPe_uDlguGDenyTlEyhptNNqDex6JhkWwS4B37YL8F0j5k_F47iTNN6ccqzK11XLKxKZ1qRQX1gRehv4M3Hx7etvcwbveGGDxgYiKwdSBykq3piA1eplEgf5nYwaQFtb5aetGydtoaPEjQd-chxlfWQ9xsyLOruM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15fe6d2c2d.mp4?token=no5-QAYRpMFeEUKVWC5aN5gct0deNsGL9WiCGZSNLpVL_ybzK2cWcnqAaOz0s5a6xjzAc_Uoy25d9GZcX5ZzoZ_yeRZdOaTRMDEGU7wOWLr5Yu2KnZwM5AocgCaeIPJXJ2lfNQLquKjhRPu3_S91J9qs2FfTzm0jsFmmdOA3BG-BFBRkRUFLzK8VSBky_uz99_1AqG3fkI5Cvbud6GCf62Wvgtck2Eco9AqvlbxTrZWvHJ_XyxRPoeGLG_mOC69j3M7xPEWl1ebtyZxup1OXDnCODUyvhdjNwXx2qXPL4uuTSaesB0wxqkxby0KSPAOYrrjopeuqASkbOcJkVADTJBSxyxzToJAqpoBAQB_QhtsU-6SwyVH4lPdGPERh-qMeVa_mV0UqSQ8BwUOTP5F-Kc_6E6YrV8g-9XwV6OUUKeYXxS3jY8sQnfIpBvf_J6Ii38r3TVXnELNXmpNYVNWbQm0EVB7o5NBVLYlz6BnT-XMiSdJyVhIqbiDiZXRIlFp472bE8Q-WvOylPe_uDlguGDenyTlEyhptNNqDex6JhkWwS4B37YL8F0j5k_F47iTNN6ccqzK11XLKxKZ1qRQX1gRehv4M3Hx7etvcwbveGGDxgYiKwdSBykq3piA1eplEgf5nYwaQFtb5aetGydtoaPEjQd-chxlfWQ9xsyLOruM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ درباره ایران:
ایران چهار ماه پیش نیروی دریایی و هوایی قدرتمندی داشت. بیشتر موشک‌ها، پرتابگرها و تأسیسات تولیدی آن‌ها از بین رفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129779" target="_blank">📅 23:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129778">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75e37a8b38.mp4?token=jfpYha17_b2ug7oCu-kkqV1U7KEMXSPHgi4s23XhmfmUlkcI3LV9GAXVsPGeqIxlBZ0VO1fUTqKDbe_TndvfZTWE382-NXlWKGRGXugzMa7IhpF2T4Y6fhwE308AE_96YzAK3u-iidDSijkGsmSaVPDp80G92DQXI7djU67Gl6b7brgGHq97-riDlKAgTcqko_V1qL7RY_XaCUNnO4-hKbAQMLhsppx37LT-iMeQx4XxWlTtkTh8PYy5xodRrhwzuMZ9EARuYoi4EtQFHwPKIOrK3Tc0cjb_PDe1fPKZ5SaXc-2VWA0Md7LyhpRPQY_r1vQhaPHe-3rQR2UTl6KI5ayS8RGqqFFRQmbeA2xIhsNT2QqglPLBjF6RRXFhs0_61_aOPHN7zEAZiu3s4JwD1LExt2uEJ0iIKEDxlEFFIYzCLWaRy5bcRKfT2cWGVAVjWee3bo6hGgKCdeBvi1wBKTGMwpqVdEeetUednnvF2oY1SHh5KweImh4OrQ2C8IppkOpp95FDAskHTqB5B0N-iNZnYnoRIdokjdcCnzzWiF5SQfCEhhC9rFyyy08R6uubnMWtxbZMu8nt_tATuby3dz-tYbgO-qHUQ_w0-h-DvMdnN1mTAlcunL8A_OOUhhnR5-BgaTgNv7wvf00UBr1zaEhlguF4cahc_btcimwamWk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75e37a8b38.mp4?token=jfpYha17_b2ug7oCu-kkqV1U7KEMXSPHgi4s23XhmfmUlkcI3LV9GAXVsPGeqIxlBZ0VO1fUTqKDbe_TndvfZTWE382-NXlWKGRGXugzMa7IhpF2T4Y6fhwE308AE_96YzAK3u-iidDSijkGsmSaVPDp80G92DQXI7djU67Gl6b7brgGHq97-riDlKAgTcqko_V1qL7RY_XaCUNnO4-hKbAQMLhsppx37LT-iMeQx4XxWlTtkTh8PYy5xodRrhwzuMZ9EARuYoi4EtQFHwPKIOrK3Tc0cjb_PDe1fPKZ5SaXc-2VWA0Md7LyhpRPQY_r1vQhaPHe-3rQR2UTl6KI5ayS8RGqqFFRQmbeA2xIhsNT2QqglPLBjF6RRXFhs0_61_aOPHN7zEAZiu3s4JwD1LExt2uEJ0iIKEDxlEFFIYzCLWaRy5bcRKfT2cWGVAVjWee3bo6hGgKCdeBvi1wBKTGMwpqVdEeetUednnvF2oY1SHh5KweImh4OrQ2C8IppkOpp95FDAskHTqB5B0N-iNZnYnoRIdokjdcCnzzWiF5SQfCEhhC9rFyyy08R6uubnMWtxbZMu8nt_tATuby3dz-tYbgO-qHUQ_w0-h-DvMdnN1mTAlcunL8A_OOUhhnR5-BgaTgNv7wvf00UBr1zaEhlguF4cahc_btcimwamWk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار:
آیا می‌توانید تضمین کنید که ایرانی‌ها از سود فروش نفت برای بازسازی ارتش خود استفاده نکنند و فقط برای دولت بعدی آماده شوند؟
🔴
ترامپ:
خب، آن‌ها قرار نیست این کار را بکنند، قربان. خواهیم دید، اما قرار است پول را برای خرید غذا برای مردمشان استفاده کنند، چون در حال حاضر مردمشان خیلی گرسنه هستند و آن را فقط از ما می‌خرند — ذرت، سویا.
باید پول زیادی باشد. امیدوارم پول زیادی باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/129778" target="_blank">📅 23:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129777">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbc98d2cf2.mp4?token=bjtc1P2OfW2DoLd8zVJG3ZRJ1vkAAEr-nz4VgOdAFc3xYYbGV7IkXAK-1-65xYd80NgxYvMig7W6DqmejzKPef1c97AlnFFyFJ2jCU0iNJRdv6mm1NrxpiriaLIGwHaTP7z0t-QHXFqwnNNr3CCH1r9Rq41f3OZJKFrg7RpJN9LNzVRGwrO2uPTyABsZvtVNhQDRbZs-Y-xQWfHdYus2AA2VRiF2oGpawfr4e0c0NmxtSIwzcEHNvgxwNDv6KRUe6_1TTpFwXugHA0XFwdIcKph0K1275XpLrxkhcXcjuX649_cDHiis9Ng_PnHRtvg-vFoXL9-nhj2ZDXbK2zQSTXfLvwUc6WXvoQhumcSXCd7n9uD1AggU_WG2KsFlGcKJ8vwKhCgBoJ-UY1kLLj-2yHqdqzVlH7jknxMaeyt_MGX0xQCSOnl78ANyi-NrpWD-ELvrd5UzxifBK5OpxRxJBG2enmVbacrca9jPG8GBMI3gglS1PXcEG1r-NpwX9kpzDBIRX_uCnZytGg1UqOTehwQ5G2GGfKtBdSHbUFJsndCHFFQU4XEJGZGBZrkMeDHCOl1VwqqktLB-sWdPTG6S3tEKw3t1_sODPRXmUG7dSUb50aolOQq2nhPNAGQlUKaKVdGHrdGBwEht-2kf-fYuMXI0GR29011HbDv006L026g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbc98d2cf2.mp4?token=bjtc1P2OfW2DoLd8zVJG3ZRJ1vkAAEr-nz4VgOdAFc3xYYbGV7IkXAK-1-65xYd80NgxYvMig7W6DqmejzKPef1c97AlnFFyFJ2jCU0iNJRdv6mm1NrxpiriaLIGwHaTP7z0t-QHXFqwnNNr3CCH1r9Rq41f3OZJKFrg7RpJN9LNzVRGwrO2uPTyABsZvtVNhQDRbZs-Y-xQWfHdYus2AA2VRiF2oGpawfr4e0c0NmxtSIwzcEHNvgxwNDv6KRUe6_1TTpFwXugHA0XFwdIcKph0K1275XpLrxkhcXcjuX649_cDHiis9Ng_PnHRtvg-vFoXL9-nhj2ZDXbK2zQSTXfLvwUc6WXvoQhumcSXCd7n9uD1AggU_WG2KsFlGcKJ8vwKhCgBoJ-UY1kLLj-2yHqdqzVlH7jknxMaeyt_MGX0xQCSOnl78ANyi-NrpWD-ELvrd5UzxifBK5OpxRxJBG2enmVbacrca9jPG8GBMI3gglS1PXcEG1r-NpwX9kpzDBIRX_uCnZytGg1UqOTehwQ5G2GGfKtBdSHbUFJsndCHFFQU4XEJGZGBZrkMeDHCOl1VwqqktLB-sWdPTG6S3tEKw3t1_sODPRXmUG7dSUb50aolOQq2nhPNAGQlUKaKVdGHrdGBwEht-2kf-fYuMXI0GR29011HbDv006L026g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار:
خزانه‌داری تحریم‌های نفتی ایران را برداشت.
🔴
ترامپ:
من باید دقیقاً وضعیت را بفهمم، اما اگر تحریم‌ها برداشته شوند، پول به این کشور وارد خواهد شد. تمام آن پول بازمی‌گردد. آنها ۹۱ میلیون نفر جمعیت دارند؛ نمی‌توانند آنها را تغذیه کنند. پول عمدتاً به کشاورزان ما خواهد رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/129777" target="_blank">📅 23:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129776">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNLctDdQBEbtKzWrzec7z-TFBN0qPVdY6opiH0QAHUTxeKrk4xgYv7J7jUMb2N-K-eYeBDHn7pidz-_FXBJmaNRO4HKsQAb1xB3W86wL7xcxJ5fAjk5wAta3WW4wheFV8ee1IhTWAqc1ONLO2Cr4yrlQKLjt30ERhr0lGrYTelMABLyVSlKtjfMAv0kV3fgXe1k77xDpxONyXBQ9WjQ1mwsDeLu4O9o2GYIeC9ryNfEebV0LZd9vNJnO07qGvfkxlgSqeOKHtLhl8pPtcEQh6crcsQlE4YuTvS52oU37wfxjaMYVtWv1R_R7r7tLKgjf4lrmbBc0ijNKH7iF2Hncwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: ۱۲میلیارد دلار رو آزاد کردیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/129776" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129775">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5pwotO0pPUgRWO6XWRZyDfXNpeHv1hfoTq3u1Y3yBRNf5dyLHAhMYb42yvT-8P6O9KWArXpC925fwwR_ENWN9Ep-Ece72TBFeRyHKlA2MQvw8xf8wcIeahv32O68GQUOvGd4o3glTGZnHWmUegipKvEfdejd94w97nbSq9wxFNTLIvHMasdmDgW8nXNzMEjtSiw-_lJ3n0O8R3fCvh-RmLjOVH-fXEdp6u3U6Zbsrhyxfet_YAPTTH7Y2RgRNOoLLcqTcrZ195A7G2HDQVMBAvCJgnQx_Wkp4vNfmd11SNbWJVuLy0ByNL5V0zWk5VUgsZBaAOeT14yhqDOaAabpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: ۱۲میلیارد دلار رو آزاد کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/129775" target="_blank">📅 23:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129774">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd99c1a494.mp4?token=iALgJyEIqRqggLDdeJ02bRJeF_Ouj99Ptp8icahQkya7vcUY6W8HbDhHV5JGAnZLW5rPJtXzmFj1ikLZXTtV5cvzaiA5R3GF1RYKo6yNnmFRkQdJwcAUY4OYFsKvq2Z8BQkKvjFrswLsaFwrpjEUkoVpdinTWMFaPMi_3Rwm--Z5rjFPJEUNruBqqaqnCZlRUQ_wCpaSRIKfmAYdQ_spMYiXDS-AFlulAcoBKzkKwR1Rpde7x4uWihK2jGiGJUj930knZ2jO0t3UDfcTs6qdoAvJG8VhVhjzI4Ye7bKetg1Yxc4W-b_UlbSlUsjNQTEYR6Y-aRgQczs3aiAXzOBUJYjuLxZfCHk0XFzDuB4U5W4SAsx3jYNWXqLTYRZ2ZNMhwCnFq6Vyi6iuuO0YB4JpHPLLcIKJb3HG3oT28D_BEHaj6-lW3msIObiZMVTHZZz7RxF4awDShR9pPtAmTdD2tqgcpmcqMmqhy_syQjoVeXWjivKLT5CgwcZ0DtedjKtQtUmBQO5PNpW1b1nRR4GafXfWvw_TxouupRq4KqdKQQr0W_CESfvNmEhwL9JNUcN64NZoJ7JP62Dgcse9trC-553fT14bRsr5l_LBi3zCEaANyCXOAU_RR_KwpTItgi2cqDw3VWzLE5l4gKv9avmiAJl30YbrgJE167F5z8DO-Dc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd99c1a494.mp4?token=iALgJyEIqRqggLDdeJ02bRJeF_Ouj99Ptp8icahQkya7vcUY6W8HbDhHV5JGAnZLW5rPJtXzmFj1ikLZXTtV5cvzaiA5R3GF1RYKo6yNnmFRkQdJwcAUY4OYFsKvq2Z8BQkKvjFrswLsaFwrpjEUkoVpdinTWMFaPMi_3Rwm--Z5rjFPJEUNruBqqaqnCZlRUQ_wCpaSRIKfmAYdQ_spMYiXDS-AFlulAcoBKzkKwR1Rpde7x4uWihK2jGiGJUj930knZ2jO0t3UDfcTs6qdoAvJG8VhVhjzI4Ye7bKetg1Yxc4W-b_UlbSlUsjNQTEYR6Y-aRgQczs3aiAXzOBUJYjuLxZfCHk0XFzDuB4U5W4SAsx3jYNWXqLTYRZ2ZNMhwCnFq6Vyi6iuuO0YB4JpHPLLcIKJb3HG3oT28D_BEHaj6-lW3msIObiZMVTHZZz7RxF4awDShR9pPtAmTdD2tqgcpmcqMmqhy_syQjoVeXWjivKLT5CgwcZ0DtedjKtQtUmBQO5PNpW1b1nRR4GafXfWvw_TxouupRq4KqdKQQr0W_CESfvNmEhwL9JNUcN64NZoJ7JP62Dgcse9trC-553fT14bRsr5l_LBi3zCEaANyCXOAU_RR_KwpTItgi2cqDw3VWzLE5l4gKv9avmiAJl30YbrgJE167F5z8DO-Dc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ درباره ایران:
ما در مورد تنگه هرمز بسیار خوب عمل می‌کنیم.
دیروز نفت بیشتری نسبت به هر زمان دیگری که از این تنگه عبور کرده، دریافت کردیم. تنگه کاملاً باز است.
ما دو چیز داریم: یک تنگه باز و کشوری که هرگز سلاح هسته‌ای نخواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/129774" target="_blank">📅 23:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129773">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa7c9b7e2.mp4?token=nMz0locl-Arj4WyMZsKx6vR5zjg3UPtHXVCRMbfPJFBjhQaOPENRQchty-S44bpVv6rKsCOaFR1ofCly6UIhL_DLNKEjMv6scwzziHpCRGAk-KSW1MXaoWH2T3KkepNY2ouHEpBX76bnbAuIeU5pEXWxntOz4qmNNZ0Y7DKrx_0I8uG-c7V89S5HePbNberNIPWC_p-HRgBNOn-O2pjOeHJtnSrjjD_A7FACbpGTllWAp5ktkXoD-LdOVOrxa_Rkr0daLof53GgXDbgqD49j8CGuoOwe71ab1bbKFjZFTlUt86MUQ8anQ6ZLVM7cq5CIwo8sqknrCIYOmFy6wEyV4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa7c9b7e2.mp4?token=nMz0locl-Arj4WyMZsKx6vR5zjg3UPtHXVCRMbfPJFBjhQaOPENRQchty-S44bpVv6rKsCOaFR1ofCly6UIhL_DLNKEjMv6scwzziHpCRGAk-KSW1MXaoWH2T3KkepNY2ouHEpBX76bnbAuIeU5pEXWxntOz4qmNNZ0Y7DKrx_0I8uG-c7V89S5HePbNberNIPWC_p-HRgBNOn-O2pjOeHJtnSrjjD_A7FACbpGTllWAp5ktkXoD-LdOVOrxa_Rkr0daLof53GgXDbgqD49j8CGuoOwe71ab1bbKFjZFTlUt86MUQ8anQ6ZLVM7cq5CIwo8sqknrCIYOmFy6wEyV4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
پول‌هایی که در حال آزاد شدن هستند، برای خرید مواد غذایی استفاده خواهند شد و این مواد غذایی به‌طور انحصاری از ایالات متحده و از کشاورزان آمریکایی خریداری می‌شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/129773" target="_blank">📅 23:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129772">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
وزیر دفاع پاکستان:
اسرائیل تنها تهدید توافق ایران و آمریکا است
🔴
اسرائیل به هر دری خواهد زد تا در مسیر توافق خرابکاری کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/129772" target="_blank">📅 23:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129771">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0a8a9b37f2.mp4?token=AIaqlqzWmczNal_5YKpDm-hSnUsgKwkesfnBeu0YEKPO1cgaCpBl0dJ9levUf-x-tJujP9-XjLJfnYMmWLboMfGpLgFxBbs01v3DdJTVnc--bltlDm05so0-T_S86bEUqX4JMRvb6VXFnJRIU4QY53crLf4zfrwyIKr6HSGEf8fUw6ZQKrApkX1u_pUwjoHQKxfLxTeMCO-dDH1pSHpRIS1eif21_4qik7-ebddSD_MloAV-jvdLw2Jiw0tRsL6RN97TfBGbl4KdTuzz9shEp1RD4x9TDrwgF_mYLDxLiqzgkXXJ7UY1OKMaBgyYlTVffSgIlxM2nlsap8Zcn4R0IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0a8a9b37f2.mp4?token=AIaqlqzWmczNal_5YKpDm-hSnUsgKwkesfnBeu0YEKPO1cgaCpBl0dJ9levUf-x-tJujP9-XjLJfnYMmWLboMfGpLgFxBbs01v3DdJTVnc--bltlDm05so0-T_S86bEUqX4JMRvb6VXFnJRIU4QY53crLf4zfrwyIKr6HSGEf8fUw6ZQKrApkX1u_pUwjoHQKxfLxTeMCO-dDH1pSHpRIS1eif21_4qik7-ebddSD_MloAV-jvdLw2Jiw0tRsL6RN97TfBGbl4KdTuzz9shEp1RD4x9TDrwgF_mYLDxLiqzgkXXJ7UY1OKMaBgyYlTVffSgIlxM2nlsap8Zcn4R0IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
تو یکی از تعزیه های اصفهان، جیگر امام حسین رو در آوردن
😐
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/129771" target="_blank">📅 23:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129770">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2DkrgU3hHbLz8d-JO8gqTTCJpyxLvnKevpvryTSOmMVVxOYSGWhBm1T5RRLfYmneLAiUiNsts9nmFq2b5qr56dKWGYTog1A-nSDBeNW4zeW_CY6-tt4Owo1PPOm_Cq4IznEweH5acO8O9Xm3DDQMuyaGU8mPAd8--YfPFTi46m8uW1qScqytc1-oLxmfFAelRMdt_oehlTE6TUj7EMeqxsUF-XyhhwNShSA62vadI8wXxfVVrjygVo3Wws05-LqC35WszenEzcdYq6VrgFZPT0sz9C8bMlqk5fdex0D7IZGMsKheKOgcVjtCahA7YL1wu9xRwmGy3wvAm_QKybgpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: میخوایم جلسه مجلس رو وسط خیابون برگزار کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/129770" target="_blank">📅 23:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129769">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوری / مختارنامه شروع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/129769" target="_blank">📅 23:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129768">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وزارت خارجه فرانسه: بدون موافقت اروپایی امکان ندارد تحریم‌ها از ایران رفع شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/129768" target="_blank">📅 23:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129767">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
وزارت خارجه فرانسه: احتمالا در مذاکرات فنی بین ‌آمریکا و ایران در سوئیس شرکت کنیم
🔴
بدون موافقت اروپایی امکان ندارد تحریم‌ها از ایران رفع شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/129767" target="_blank">📅 22:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129766">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d033d127d.mp4?token=WFbcTRJ5oxx_CTJLBoh0_Dyppd4jCW3ZBl_XY8Yh0zxmBvwdLqJn0XeU1it4eDo0hAcu0HjA-nBG52YouCDvkgcKG1u41mcj5sQIRDTEo_QbtiAG1ow1kdBs2Sgf2G2p3ZAzpaK_es8AL3yRz9i1CPXRBuuDGekEDTs2IFpSPn-v2J1pfQIXtNl_ztXFFanppA3W1lBn8bqJttbytlAPVz3WP99viI6um3WtMfpYxfp5EJGKtvjzx3JHfpI2dx_yKxkGoqMS9EEsdrW7NeBUUK5eeFkodF9ZpjLA7cKcxXf5Yj9ySXEIMI2FK7XI1ndJP1XL1ceNxQf4KSzirbLYWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d033d127d.mp4?token=WFbcTRJ5oxx_CTJLBoh0_Dyppd4jCW3ZBl_XY8Yh0zxmBvwdLqJn0XeU1it4eDo0hAcu0HjA-nBG52YouCDvkgcKG1u41mcj5sQIRDTEo_QbtiAG1ow1kdBs2Sgf2G2p3ZAzpaK_es8AL3yRz9i1CPXRBuuDGekEDTs2IFpSPn-v2J1pfQIXtNl_ztXFFanppA3W1lBn8bqJttbytlAPVz3WP99viI6um3WtMfpYxfp5EJGKtvjzx3JHfpI2dx_yKxkGoqMS9EEsdrW7NeBUUK5eeFkodF9ZpjLA7cKcxXf5Yj9ySXEIMI2FK7XI1ndJP1XL1ceNxQf4KSzirbLYWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه 14 اسرائیل:
به نظر ما ایران داره با یه سلاح الکترومغناطیسی روی مغز ترامپ اثر می‌ذاره
🔴
رفتار و تصمیم‌های ترامپ نسبت به قبل فرق کرده و این اتفاق عادی نیست.
🔴
این فناوری شبیه تله‌پاتیه، با این تفاوت که از امواج الکترومغناطیسی استفاده می‌کنه.
روسیه و چین این تکنولوژی رو دارن و الان هم ایران هم بهش دست پیدا کرده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/129766" target="_blank">📅 22:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129765">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812edc498b.mp4?token=LJ-JjZkwAV4VXlLrzD6jhGgvS_J0B-CtIEILDHSGyT9nEFmIcSJp5unxmvhjRBnRYWnnjPe6F54Ce5fxZ6iqD9rRSLMukm8cSsw8aAc-Xvbm4sYp7LYM8XJCM7E02nnrCGUhP79azq6DL0gsKmYlTkHGz8eRTNRRg13X2BK8uxeaUF34yJ94WiKqGGavYb6B_xBT0fvyH9rQ0fTUGCHJfAcflWFrnGJ86ts_h7Q3tp2renJk_yvcr_oEjYz9lL-jQXsHPwWj_ByDnFg4Suc5AAHt4Bpa2vkNCDfx2-mgkDPKp_O72OJKOk0h-gZ4Ips86zwwWWkEA6hm3g5tT0vNxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812edc498b.mp4?token=LJ-JjZkwAV4VXlLrzD6jhGgvS_J0B-CtIEILDHSGyT9nEFmIcSJp5unxmvhjRBnRYWnnjPe6F54Ce5fxZ6iqD9rRSLMukm8cSsw8aAc-Xvbm4sYp7LYM8XJCM7E02nnrCGUhP79azq6DL0gsKmYlTkHGz8eRTNRRg13X2BK8uxeaUF34yJ94WiKqGGavYb6B_xBT0fvyH9rQ0fTUGCHJfAcflWFrnGJ86ts_h7Q3tp2renJk_yvcr_oEjYz9lL-jQXsHPwWj_ByDnFg4Suc5AAHt4Bpa2vkNCDfx2-mgkDPKp_O72OJKOk0h-gZ4Ips86zwwWWkEA6hm3g5tT0vNxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این کلیپ علیه قالیباف توسط علی الاصول‌ها درحال وایرال شدن هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/129765" target="_blank">📅 22:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129764">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ قراره چهارشنبه بره کاخ سفید تا با مقام‌های ارشد پنتاگون و شرکت‌های بزرگ اسلحه‌سازی جلسه بذاره تا درباره نگرانی از کمبود ذخایر مهمات و تسلیحات صحبت کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/129764" target="_blank">📅 22:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129763">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqyyf8XhzyfJGi3J9ylQu_mqvR3ivLDdTot4xBMj82J1MkoX_7JUjjQQh7xiOKZs0R_4Y87XMLdO1z5bV7uB1BpZnnZpOhYDpMot4g-ZKUM4rSbDmV933cbeJ1fcU1KysQ87NopjmITVAuWDzy6HJN_X7eqldiiiLQxx5h1XDMWpHvmazg86abPgGW-Z-QLi9aFCsjjphlSGrGZkQhiRzj6cj4iHl01q5nNtCo0SB8IVm29pa1CaUakapM6qsepDD7m6qc-UDMph7XuyBn-7yY4wgwoB3JAo8l-sWm2Ihuwx1eQd0HmLjKtsF04c4RQ0tfoDlhC-XdYDe4iNG7V0Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرستاده ویژه ترامپ به گرینلند جف لندری از طریق ایکس دیروز: روز ملی مبارک به همه مردم در سراسر جزیره شگفت‌انگیز گرینلند.
🔴
امیدواریم امروز یادآور فرهنگ غنی، سنت‌ها و ارزش‌هایی باشد که میراث شما را تعریف می‌کند.
🔴
همزمان با نزدیک شدن آمریکا به ۲۵۰مین سالگرد استقلال خود، ما در جشن آزادی و فرصت‌ها شریک می‌شویم.
🔴
شاید تولد ۲۵۱ام آمریکا با اضافه شدن ایالت ۵۱ام آن جشن گرفته شود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/129763" target="_blank">📅 22:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129762">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff2ab234.mp4?token=T77-Gi-FjzB-us-hQ92wWJNv-WceRmULn0VoP0sWNxb8EzoKKVE_vc1zFCf0r4wdx4M_SL5OqncHiuGDwPCm0q6gCEsNUSD0D8jO888rIiOH02dHhHmGeD60k-KbiZGnssxTg8AhxuuXYmmLYc3WzgUwpq9NmgqGFQVy6aGVbU1AdoxSmcvgS8sYRNN54rJuRXhXWHJjdx4Y88R-VFuREyFV5rMXh31L7eDY2uyN8BDolqmWWMrNy5uBbmvp1_9gI1phPi_50mp8y_fZiOkntYaGbrIzwryKOohy-nIn0hj8XdqwwwhRbhHuknqVpxTtA4esYoxBeWXU6dGuV95Kig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff2ab234.mp4?token=T77-Gi-FjzB-us-hQ92wWJNv-WceRmULn0VoP0sWNxb8EzoKKVE_vc1zFCf0r4wdx4M_SL5OqncHiuGDwPCm0q6gCEsNUSD0D8jO888rIiOH02dHhHmGeD60k-KbiZGnssxTg8AhxuuXYmmLYc3WzgUwpq9NmgqGFQVy6aGVbU1AdoxSmcvgS8sYRNN54rJuRXhXWHJjdx4Y88R-VFuREyFV5rMXh31L7eDY2uyN8BDolqmWWMrNy5uBbmvp1_9gI1phPi_50mp8y_fZiOkntYaGbrIzwryKOohy-nIn0hj8XdqwwwhRbhHuknqVpxTtA4esYoxBeWXU6dGuV95Kig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس:
چیزی که برای من خنده‌دار بود این بود که بعد از آن جلسه اولیه، نوعی طوفان رسانه‌ای در شبکه‌های اجتماعی به پا شد که همه می‌گفتند ایرانی‌ها قرار است بروند، و بعد ما حدود ۹ ساعت با آنها صحبت کردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/129762" target="_blank">📅 22:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129760">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/bSdKaNpJSJyV5mjPh07UKNfhXWpHQVn5f26Ti6IbGoqcr6WhlwMgoSL6el48Ct6E2eOAKdP2XdP-kDfNOPlNy5F3UaY0e0slsm2JNi2PNkJ8dMfwwjxM6DUwOOYpZlXJx5StPGt15B9AN7nFEvCmNOwQQIDYY-9CsgUd_XT6MKcZp_PAH9VVPua3qXw3st7rAoAMWLS3PXJADu5brcSIV9AoqNCy_TMPG3bZHeHAUb_YoRaR6yKFU4NA0cQ0PBWQByXIXXI_XQ4Q2m33OqbzqvrUj1Lm88CLbzS3pEaF1xbZHYpgMFQbLpNHuocviFow3SEKhTM6a57ErLWfRPJPng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/0336eb3457.mp4?token=NXebh1vhxATw2tEDbjHAgH9FAMHuGUDRSxns52Fd98ue3X5QfhKM9jxUtBzKEBqjObc4dtiNphBFnULdkIIt4rpKxQDIC1sDq6OxVRFwZen-8KH19KSlp9Y83q9Oom3YDaNNvMoA0hMcWzDEdtgvELhRS5BUN1wBkRlvOg_TG8sae8kusqvC4_qXnMtuO4bUI7GMvyC9sjlazV8_FGE1E_u5ORB03XF-Q56VM_OGxXIw2dkDXDNSqB-KDwosZjcub8bfBV8pnEmyUO0kJXRwjTPPrl3XjzG-DAX87c5TTkZ9hyPnEvFfoPjPKE96X-u06ZyKStOE4zvc6-svBHxwjA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/0336eb3457.mp4?token=NXebh1vhxATw2tEDbjHAgH9FAMHuGUDRSxns52Fd98ue3X5QfhKM9jxUtBzKEBqjObc4dtiNphBFnULdkIIt4rpKxQDIC1sDq6OxVRFwZen-8KH19KSlp9Y83q9Oom3YDaNNvMoA0hMcWzDEdtgvELhRS5BUN1wBkRlvOg_TG8sae8kusqvC4_qXnMtuO4bUI7GMvyC9sjlazV8_FGE1E_u5ORB03XF-Q56VM_OGxXIw2dkDXDNSqB-KDwosZjcub8bfBV8pnEmyUO0kJXRwjTPPrl3XjzG-DAX87c5TTkZ9hyPnEvFfoPjPKE96X-u06ZyKStOE4zvc6-svBHxwjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب دوباره صداوسیما دستش در رفت و دوتا از هوادارای آرژانتینی وسط صداسیما لبارو درگیر کردن
😂
@AloSport</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/129760" target="_blank">📅 22:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129758">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وزیر دفاع پاکستان: توافق ایران و آمریکا، به معنای پایان سیاسی نتانیاهو است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/129758" target="_blank">📅 22:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129757">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/460ce843c3.mp4?token=RGlUCMkseOLFHTqbJujVisgo7GuyofbfseBDxPs-7E61FWUzFJCKggeaJQyJt8ymo-4VmJxREIv1GV3L5E_wlks5uqJkQhxduqSQ28OfM5pYnAtC-XJv16BiEVkrMCD-XAHSvhO5bEpIh47CdVRxbvgX06Ddq_AMyuG0lSfx1krLYN-t3RhlcmUcuwesaRjyJpqANWqx8BPZM1DD0uEqNHs03CsZoCXe-hIymQS_C9ilOHabmr1opqtwIHrWBwSmDppC7t00e2MzyqHSm7NRkxb7haWcC8TnKRYIeVTddoVJKNB3oXz6pdPxB7Jl6qNdqlHa8Cd1pBurJapT3heYow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/460ce843c3.mp4?token=RGlUCMkseOLFHTqbJujVisgo7GuyofbfseBDxPs-7E61FWUzFJCKggeaJQyJt8ymo-4VmJxREIv1GV3L5E_wlks5uqJkQhxduqSQ28OfM5pYnAtC-XJv16BiEVkrMCD-XAHSvhO5bEpIh47CdVRxbvgX06Ddq_AMyuG0lSfx1krLYN-t3RhlcmUcuwesaRjyJpqANWqx8BPZM1DD0uEqNHs03CsZoCXe-hIymQS_C9ilOHabmr1opqtwIHrWBwSmDppC7t00e2MzyqHSm7NRkxb7haWcC8TnKRYIeVTddoVJKNB3oXz6pdPxB7Jl6qNdqlHa8Cd1pBurJapT3heYow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل در ۱.۵ کیلومتری شهر نبطیه!
🔴
حضور تانک های اسرائیلی در روستای کفر رمان در فاصله ۱.۵ کیلومتری نبطیه در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/129757" target="_blank">📅 21:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129756">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ونس: دارایی‌های مسدود شده ایران آزاد نخواهد شد مگر اینکه در مذاکرات پیشرفتی حاصل شود؛
🔴
ایران برای اولین بار پس از مدت‌ها به بازرسان آژانس بین‌المللی انرژی اتمی اجازه ورود خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/129756" target="_blank">📅 21:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129755">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ قراره چهارشنبه بره کاخ سفید
🔴
با مقام‌های ارشد پنتاگون و شرکت‌های بزرگ اسلحه‌سازی جلسه بذاره تا درباره نگرانی از کمبود ذخایر مهمات و تسلیحات صحبت کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/129755" target="_blank">📅 21:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129754">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ونس لحظاتی پیش سوئیس را به مقصد آمریکا ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/129754" target="_blank">📅 21:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129753">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
قالیباف: حاکمیت ملی لبنان بر تمامیت سرزمین خودش انشالا در این گفتگوها به نتیجه نهایی میرسه و تا به نتیجه نرسه، رهاشون نخواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/129753" target="_blank">📅 21:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129752">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
قالیباف: بدون دیپلماسی زحمت عرصهٔ میدان به ثمر نخواهد نشست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/129752" target="_blank">📅 21:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129751">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
قالیباف: مذاکره، یک روش مبارزه است و ادامه آن است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/129751" target="_blank">📅 21:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129750">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpVel4yYo5bS3zTR7t7Q6cIyM73HOcdrxxkLxqPduROsIf52EB50HHVY8GXckGk9WdZOPOTTJGQjNBVOSdp2FIe5H2YUT-8dwUxZFl2Zm8EjW3fF8FWAt9xw1VfgCxl80Uyglt5uEKFknwMl7Vmz9NADqTraXr2bcB5NEVxrjwUppPax6li5EheuIuDlHM2HDBhmMR0wFA2V03Z0aLa4cIhD8Znrlrn5XsCW8ddf6Y75jihn1BkNKINiYaO-zAWpOK3FKEOIq1iIclfL2_JK-jfa1kmxLwzNcPNdUyBKe2K21A5H_nA1wm7vi7RxW4CbfK_6t8pYAg22bS0gdNLYgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عضو تیم مذاکره‌کننده ایران در اسلام‌آباد: احتمالا اموال بلوکه شده ایران صرف خرید مستقیم از آمریکا شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/129750" target="_blank">📅 21:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129749">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed2b1eb31f.mp4?token=Fcb7wJgkllCD6NvUC_PDrQe9h7DQdKZ6Kxno0Ar1wkdex9q9TYb1SBMP0DFfiXNAtWINhEx85zfl85HJwhaO7-BMPv-zCefc4zpXieMu-egH25fVJXgSVEP3K1VswN7F_4A0hwnbLJ7eGx6T3K7IqctBA8PBZqXAIaZnmf9ceaKRGoXJo62aZkqYs1g_z_ppb9DIVNKsmt7oVYYFTbiYeBRYXErLz-QRaDqoofzQUtKkUrfrfdAOJXcLKv-JnsyeKBkXIM1xpLyhIp3lGMtfcpenNC3_je5zZBLoMKbxbdv671-Hb_BS1l6YnKLaskBOgmqRvaKH8Fd2xwlKlmu60Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed2b1eb31f.mp4?token=Fcb7wJgkllCD6NvUC_PDrQe9h7DQdKZ6Kxno0Ar1wkdex9q9TYb1SBMP0DFfiXNAtWINhEx85zfl85HJwhaO7-BMPv-zCefc4zpXieMu-egH25fVJXgSVEP3K1VswN7F_4A0hwnbLJ7eGx6T3K7IqctBA8PBZqXAIaZnmf9ceaKRGoXJo62aZkqYs1g_z_ppb9DIVNKsmt7oVYYFTbiYeBRYXErLz-QRaDqoofzQUtKkUrfrfdAOJXcLKv-JnsyeKBkXIM1xpLyhIp3lGMtfcpenNC3_je5zZBLoMKbxbdv671-Hb_BS1l6YnKLaskBOgmqRvaKH8Fd2xwlKlmu60Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو نخست وزیر اسرائیل با ژلیکا کوییانوویچ، رئیس دفتر ریاست جمهوری بوسنی و هرزگوین در اورشلیم دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/129749" target="_blank">📅 21:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129748">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
شبکه اسرائیلی i24: هیئت «اسرائیل» فردا راهی واشنگتن می‌شود؛ دور جدیدی از مذاکرات میان اسرائیل و لبنان از فردا سه‌شنبه در آمریکا آغاز خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/129748" target="_blank">📅 20:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129747">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEXNUrnX0NswGWt5Js0nAthCoJUQ-s6Q2w91U9RzBk1XzwGJrrMpjgoyO6D6wVlyEw7_FpsINPcAMpdJp9IRojGIICQkvspMPIxNsDqCsCMNLLzKa_VbVTdzziXgDxbj-NEqXxcyo2pl-wWOlHTWB013_WiezEwwHE2-UyjVB_AkakaeePMDQNj5QVsQ9oPFXXZpvYNLE4QF27pHVzyprnio7z7EBtrILGjF5HHU-CMASpOsBdpWghH3OWpBDWo4-nWV0vT5EIXd7unzgXsohOF0rRFgjhUhmpoFCxe7sginA0ncA9eJcy7emDCPzhs5nWyWps9IP5A_lbFmBFJEeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز ۶ سوخت‌رسان آمریکایی بر فراز خلیج فارس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/129747" target="_blank">📅 20:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129746">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bC5Vi4uYqWkK10g7bXM-2508ulk9LCfT-fkSymF2keq67rb98z0qU6LmABc0K19dy6KhKThiFgo5mHv-uqW0eLYmzfcEIGmhkSAqGGgCL9NrWRhOzgTq0lhbTp-dE6vfb7TiDG_XAhGTwpocba6w0YSM53NMpw0aBjCFfOKIjsCw5Eg0G6vsy8KgrzSPfewcuQBnXx0OqwkqiUkTnATCmNOsdeP19hYEdyO9G3FCW_nn3XkJoi8Zzk7Cgi2lO3yrRIOhNde8VVellN_SGkaEnnLdn7upuzZ9BKZWjIYh35BGUptk7lFcup8cpCQ89aONbcOpIlryoUm0cArhrc37aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:  همه به خوبی می‌دانند که ایران برای تضمین «صداقت هسته‌ای» در سال‌های آینده، با بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد. رئیس‌جمهور دونالد ج. ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/129746" target="_blank">📅 20:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129745">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
در پی رفع تحریم نفتی ایران، قیمت خودروها از دقایقی قبل در بازار معاملات خودرو کاهشی شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/129745" target="_blank">📅 20:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129744">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، کاتس : امنیت مردم و نیروهای اسرائیل اولویته
🔴
ارتش با حمایت کامل دولت اختیار کامل داره با هر تهدیدی تو غزه، لبنان و هر جا لازم باشه برخورد کنه
🔴
نیروها شبانه‌روز در حال عملیاتن و اسرائیل تو منطقه امنیتی لُبنان می‌مونه تا تهدیدها و زیرساخت‌های نظامی رو از بین ببره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/129744" target="_blank">📅 20:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129743">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
رویترز: ذخایر نفت خام آمریکا به پایین‌ترین سطح خود از سال ۱۹۸۳ رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/129743" target="_blank">📅 20:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129742">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHHxAsRMYW7cRjriCiU5tDherX_fNHJ1RemK3IT9qe6_cG0DuBLjvvFZr8DSgIUXV-Eb9AU62PEVeXtSQhtQ7r0CNrLDJ8u1_qgCtPTfWwygsVWQSEnt77aurgLntDIfcLRMsEAY3n13kY2qubitBpWlKov4wqdMhXhM0SjtoseNCHhMgXcBiJvwCkduaGzSDQIYGxNijFQm5gob3xLFEMyqZLQvn6dvetIsfe3BI-_k4EW-HZNdJgVNdlveHUx3Y9zeLLq5Hj5ZMccqhOSM1kLlqRt5c8EtWqyEODxBXb37GwPgzl8C5RrCQup42nISFrhey5VkBhp3nTHWakUu7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا ادعا کرده، این معافیت تحریمی در ازای اجازه تهران برای بازرسی آژانس از تأسیسات هسته‌ای ایرانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/129742" target="_blank">📅 20:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129741">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZXOJO4tQPT6X49J8pw87nL7u3Ev5YHZSGdp3ZOJ8c1nObkBRE7LmgaYeGt7u-78EF8DE4Nhwhs7wOf_UMe2ewov_6GqA--YBpjPXDKbMUfSvWeQUHffm_-Emjtvx_UtMAKgWP42d-t3fdz_YLEcv3ZhVcFfRxkrt4ABqYUATyYKcLW_0rrfosFZxvQAQ8QDlJLRCF1P1SqhuNDsXcH_47j8dKX3QGBxACGIuZ8defOGoWTQBNYDi36Yrhda3vephEBYDqVItwUO_YlcTg_jykxurmlff4N6y0fXdfDNCcZASfBDjzRaXSNdDQ_jyj3WC9p5TVtygiYoMS9cCbYEIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / وزارت خزانه‌داری آمریکا رسماْ معافیت تحریم‌های نفتی ایران رو برای ۲ماه صادر کرد ( تا ۳۰ مرداد )
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/129741" target="_blank">📅 20:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129740">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UO4YK12C2ctNfhkzLKYN-TWqwU0NAjGeFnu_49OxAB6-9uNWQI7S2nevS9zuHJs2ECf6F0jytAFovHBjNfDy3u8xnTZq7roUPPV4pkAbDXmChIKbQVjzTBpJPxq8kyTKnNc0eChx31ExntdUlauHQwJK0PdkVf0MmlfFhs-yy3i_B2p4LmEYC2k6k3G_RTIv0EUrA3TpNsqFo_QBJqa57M1p7cCE5ZL8nKcT7hGqM5z9irKLPR4IePEGXO_cxYydufP_R7c3qmbN9hQLumdX5toXdUMO24ePWjC7Nl4XALwyJlYY-IvUOAHotRAAWFrUzpZ_CoF2d4X1oKRyrAj1Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی: ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/129740" target="_blank">📅 20:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129739">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21803dc203.mp4?token=UCtFN8uHpCs7qBQPsTAr0eh_inArgE3jZblpkc0qB6sbIqo5qFosiO_K4GZ8ZFUy8ytCZwkErFOq_BWX5yPQyLnYoDE5pR8YSTtfS62D7_klEia3v6NdY7NpjlSK4fH5XJ40Pz5D-tO4zkxCRXAntG21y35aa5ZCOV975Y-xTvFdJcufYkQEHi2DOXp0tOcIC1U4nx9TBdGcYmIHvYatHXIDNv5hQ_UkxizVlxIC_FHPhFgYSQs3pzpmqka8aUdiTfT6TcYRVp02gu3TtXzRcBoBAU-3Yj4GQH0HaXPe5NkJ0i5xRyKjIrTANAluzxTbNvbKy4VXWqvxdY7X_aa4kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21803dc203.mp4?token=UCtFN8uHpCs7qBQPsTAr0eh_inArgE3jZblpkc0qB6sbIqo5qFosiO_K4GZ8ZFUy8ytCZwkErFOq_BWX5yPQyLnYoDE5pR8YSTtfS62D7_klEia3v6NdY7NpjlSK4fH5XJ40Pz5D-tO4zkxCRXAntG21y35aa5ZCOV975Y-xTvFdJcufYkQEHi2DOXp0tOcIC1U4nx9TBdGcYmIHvYatHXIDNv5hQ_UkxizVlxIC_FHPhFgYSQs3pzpmqka8aUdiTfT6TcYRVp02gu3TtXzRcBoBAU-3Yj4GQH0HaXPe5NkJ0i5xRyKjIrTANAluzxTbNvbKy4VXWqvxdY7X_aa4kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اردوغان: به امید خدا، شهرت بین‌المللی آنکارا امسال بیش از هر زمان دیگری افزایش خواهد یافت
🔴
پایتخت ما نامی برای خود به عنوان مرکز دیپلماسی جهانی خواهد ساخت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/129739" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129738">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزیر خارجه قطر: مذاکرات فنی میان ایران و آمریکا ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/129738" target="_blank">📅 19:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129737">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
فارس: ادعای معاون رئیس‌جمهور آمریکا دربارۀ بازگشت بازرسان آژانس به ایران کذب است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/129737" target="_blank">📅 19:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129736">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
قطر: ایران و کشورهای عرب خلیج فارس نشست امنیتی برگزار می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/129736" target="_blank">📅 19:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129735">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
به گزارش نیویورک تایمز با استناد به دو مقام اسرائیلی، سربازان اسرائیلی روز شنبه دستورالعمل‌های جدیدی دریافت کردند که عملیات آن‌ها در جنوب لبنان را به «اقدامات دفاعی» محدود می‌کند.
🔴
طبق دستورات به‌روزرسانی شده، نیروها تنها در صورت وجود تهدید فوری مجاز به شلیک هستند، مگر اینکه مجوزی از سوی رئیس ستاد ارتش دریافت کنند.
🔴
این دستورالعمل‌ها همچنین شلیک هشدار به غیرنظامیان بازگشته به جنوب لبنان را ممنوع می‌کند، مگر اینکه آن‌ها «بیش از حد نزدیک» به مواضع نظامی شوند. علاوه بر این، نیروها دیگر بدون تأیید فرماندهان ارشد مجاز به تخریب خانه‌ها یا سایر زیرساخت‌ها در منطقه امنیتی نیستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/129735" target="_blank">📅 19:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129734">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
فارس: ادعای معاون رئیس‌جمهور آمریکا دربارۀ بازگشت بازرسان آژانس به ایران کذب است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/129734" target="_blank">📅 19:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129733">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nluK9CD0bJL2R-fRjdNyjZP-rhOe0phUg8qIkNy4GRcaIrD8RFytiaIn2Xfa5uTy18kxLBNENvhFDjkc69DiTPXSJDO3aHkgJJUGrMb_W323vtVarmOTIp0yK8CiTI2H08COUj85OJXrkbfTVhuVqs8jel7xYTM44-K5uxdkxoWhgbrmFc-5ghBH1Y4h5XVg-BaQ3fGgCdb2vWBlnZmSHN_2m4uftvE3-8ahyJg51NGHadRgzXMaF3Vv-wbyCSyi6g4uHfd1OhglTb1Qw_m4JKcSf-tC1LnPEcBlg8Y39BGDOwaFv7PnrcmVphdJqDzjS4y3c3U03KeyGSUgcG9DJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف در سفر به عمان با  "هیثم بن طارق" سلطان عمان دیدار و در خصوص تشریک مساعی برای تثبیت ترتیبات ایرانی اداره تنگه هرمز گفت‌وگو خواهد کرد.
🔴
در این سفر عراقچی، رئیس هیئت مذاکره‌کننده ایران را همراهی می کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/129733" target="_blank">📅 19:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129732">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
قالیباف رئیس هیئت مذاکره‌کننده کشورمان دقایقی پیش تهران را به مقصد مسقط ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/129732" target="_blank">📅 19:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129731">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMAAXNUiF2X2u7BK7PA3BV4rPZJaCppdYOxO43w7iRYY27LcOP7OsjS8ULfv_by2gyBV_O29C0NQDmM2daiRlvRBuRwOFc7RpNCJsTRB5kjk1spsFgldIyxt5qZ8n0UqY8Ghmi3LEYukaI_vLZxvj3LMzswRxXlUZJI82B_ea3tv9a-auTByuUTM40H7KxSrSLfZ9ouRiWRk-gzzWNHhHtUWX_X0-gxwWbZe73M8ovQBDdOiI6hH72PlgfGdIJ01In4InNy3HXWOWG5UB0FA0TmmAjoWp75ShlPePMBj_esruaE6yU1VjSZaMY4AsGg9uc81nDnwITtvPdDEMsdNpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید خبرنگار آکسیوس:
🔴
وزارت امور خارجه تأیید کرد:  روبیو از ۲۳ تا ۲۵ ژوئن به امارات متحده عربی، کویت و بحرین سفر خواهد کرد. وزیر امور خارجه در مورد طیف وسیعی از اولویت‌های منطقه‌ای از جمله یادداشت تفاهم با ایران، تلاش‌ها برای تأمین ترانزیت کامل و آزاد و ایمن از طریق تنگه هرمز و اهمیت صلح و ثبات در منطقه گفتگو خواهد کرد.
🔴
وزیر امور خارجه در بحرین همچنین با شورای همکاری خلیج فارس دیدار خواهد کرد تا در مورد اولویت‌های مشترک در سراسر منطقه گفتگو کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/129731" target="_blank">📅 19:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129730">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
جی دی ونس:
اگه پول های بلوکه شده ایران رو هم آزاد کنیم؛ فقط باید باهاش از خودمون ذرت؛ گندم و غلات آمریکایی بخرن. تا هم کشاورزهای ما پولدار شن هم به نفع ایران بشه.
🔴
تیم ایرانی رفته اورانیوم ۶۰ درصد رو داده جاش ذرت و سویا گرفته‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/129730" target="_blank">📅 19:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129729">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
اسماعیل بقایی، سخنگوی وزارت امور خارجه:
تعامل ایران با آژانس بین‌المللی انرژی اتمی طبق روال جاری و بر اساس مصوبات مجلس شورای اسلامی و تصمیمات شورای عالی امنیت ملی ادامه خواهد یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/129729" target="_blank">📅 19:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129728">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/129728" target="_blank">📅 19:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129727">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d4e5db99c.mp4?token=CtFF7vL4yZMf8V63E5ClXSPzVW_0G9uD5acGiJXM8xyC5peRH-H4y0Z2MXcDT4UuWUroP8Pj4_VoEmbfr-ajD7iWbklEOzs3DVMgszGlRKHC1GXJPlrBUorMSXzF1D9LOIMvMpTMMaywYrXEUgiu5g9gZLLf-QGfOfFeWH243tMYflm1uyoCcQRRuEb0Gof1m-CmvpCf1kBRGTKKAoJQ2MmWUrkagcb7lulgyrdKCvphyAJ5siOD7juotTUStOPZf9rwmMuOr9goND3HlXMSWnbs80G3r83SPBkuijEwDmpAKCF0QSctcq6qEwYcuFEv4pjUvE-tRii7xFKftA9cBEAuDAml0vllLTFHnkfOon68FMhdCpwTP639nZ_Yz4oZwEDxWhIHiFnE2nRS6hXqP31rl5aFCG4YSrRDpBjN42-MNKX7aOdv4nCGI5a5qT2mEvWxODNF48VRUgVeOjDYT05UO-QljUf7IE0z5yEJ8PfzDeoaYYWP0nPoiiTkxkdxpXDnhhb6SNVsly_dIqxBQTdwlKRNuxi5y5JrSivwTN1aYAQrvHAAloRVIGAmtCeylylirmEMsGQbCj8mgf2V7TOXeuej9INjyHKcWP3Kl40Yd50jFc1xwOY5UuhiqDuKUSbW6D9MkVSLg4iYh-2RtdWvIp3WZDVcg9NXTY29Jf4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d4e5db99c.mp4?token=CtFF7vL4yZMf8V63E5ClXSPzVW_0G9uD5acGiJXM8xyC5peRH-H4y0Z2MXcDT4UuWUroP8Pj4_VoEmbfr-ajD7iWbklEOzs3DVMgszGlRKHC1GXJPlrBUorMSXzF1D9LOIMvMpTMMaywYrXEUgiu5g9gZLLf-QGfOfFeWH243tMYflm1uyoCcQRRuEb0Gof1m-CmvpCf1kBRGTKKAoJQ2MmWUrkagcb7lulgyrdKCvphyAJ5siOD7juotTUStOPZf9rwmMuOr9goND3HlXMSWnbs80G3r83SPBkuijEwDmpAKCF0QSctcq6qEwYcuFEv4pjUvE-tRii7xFKftA9cBEAuDAml0vllLTFHnkfOon68FMhdCpwTP639nZ_Yz4oZwEDxWhIHiFnE2nRS6hXqP31rl5aFCG4YSrRDpBjN42-MNKX7aOdv4nCGI5a5qT2mEvWxODNF48VRUgVeOjDYT05UO-QljUf7IE0z5yEJ8PfzDeoaYYWP0nPoiiTkxkdxpXDnhhb6SNVsly_dIqxBQTdwlKRNuxi5y5JrSivwTN1aYAQrvHAAloRVIGAmtCeylylirmEMsGQbCj8mgf2V7TOXeuej9INjyHKcWP3Kl40Yd50jFc1xwOY5UuhiqDuKUSbW6D9MkVSLg4iYh-2RtdWvIp3WZDVcg9NXTY29Jf4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوش‌چشم، کارشناس صداوسیما:
خوش چشم
:
آمریکا ۱۰۰ آب‌نبات جلوی تیم مذاکره کننده ایرانی انداخته است تا مروارید ایران که تنگه هرمز است را از آن‌ها بگیرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/129727" target="_blank">📅 18:50 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
