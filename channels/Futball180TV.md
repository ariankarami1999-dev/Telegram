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
<img src="https://cdn5.telesco.pe/file/E8_LYLo-hCQryOrexXvw3KDvoPxcmP3YV9muPtyQ3U0fJywo3m848TXcePVBZUoZa3GSQeF9NbqOxV79NawiaoFphVQ26FdmVky-SrhnMi5-29KgDtf_rv3Okqk5qclU0sk67pc-5QQl-9mEVEHgweL91BFcqx-vDsEdHCTISe7LbYRfhUDjv0aUuCoFzdRDo3U0vxz6UIfqFfEXdhsbaiEvum07yVhpza0HARGh_JA3iCxutFjMw8_umTT3DvizO69MuHvyCKRg4UL9BO3MuhU3Gq7QUlJ-aCOxhPaRCHSutPoqyQfeGQFNn-qXwB9T222Yz71ohE8DtvGCsMunrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 518K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 00:35:05</div>
<hr>

<div class="tg-post" id="msg-102197">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔵
▶️
ویدیو باشگاه استقلال به مناسب سالگرد دومین قهرمانی آبی‌پوشان در رقابت‌های آسیایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/102197" target="_blank">📅 00:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102196">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtQSvjKzxUm-MaTMTOsy3JnfzKKC2EPTKdrtN-CoDB5Go4fO427w9gpWyg_1hjU933m3AqJPQEJNI6vmxsShWu3ti_YuCfmyjuz1WJsYZoHwIB6ghv42qi8kWWViuX_WeYeMZ-IOJtso3G0gntyFKi2H-tZn77GMzhKr8YQ3iuAG7CIIiy0CyiA8GHvAhm7FMz5TyczWZGtDWDkBSLhrplfJsnjE7wyl-Ftilm-XtL4vQEv49Yx4w0kawwJNwOS1H3RfOD-q58KQ-aN0v5sL1H78QpaSLTmUwPisXkJYtLNpR3mXbBD0hegewf6zJYYDlF_0O6XkUWjqcPjLJebvfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
#فوووووری؛ اینفانتینو تصمیم گرفته که حق برگزاری مسابقات جام‌جهانی رو به سرمایه‌گذاران خصوصی با بالاترین رقم بفروشه. کوشنر داماد دونالد ترامپ از خریداران مطرح طرح اینفانتینو به شمار میره
❌
از طرفی یوفا به فیفا هشدار داده که اینکار نقض آشکار روح برگزاری…</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/Futball180TV/102196" target="_blank">📅 23:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102195">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NX3QnPgBXY0Lc8ilBAIF0H3f4tJfv-gfDBNcuj-LmZbjx_jayzh7TcgZwkWFxjcVQEHJyeJCvFwO7ZKASvtER6h7acxRnJOHsYGrF3eQd81AQXYWELjSnkd78JIJG_6MCZs-DHi9vQtLDoP8FoAKdQIRsM1IL_IOdu-vNOvTAVOYrd5qIVkMwtsbuwcqJXHkZIOvt23o4z7qIam1iaV4WA3BYVM-K2U_jg69PBNJezk-13G76mO-dx8j1Kv9JQ9mo-UxaPVkUfsuHT5xjmY6HlCt9VWGYnDp4q1WKknUfnthV1Ck11-c91Q6PplAn4VkXPID3UvE1XWcanxYIyyQ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیلد:
نویر پایان فصل از فوتبال خداحافظی میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/102195" target="_blank">📅 23:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102194">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIqenKWIzIkAU1pzF6fI_oVenasn314IN7-5vgoOJ9Y7uAwpHBo72iFloVZuXX02qgGnGi8JQ8JzPHLRbQRmSIN1KXRUtJEX-xSUSV9-klupcxbN29Qwle43OFUYRvZANGdhk5eufK-Wd-9t_b_fAyO53QRpMECjr0gxugAR5nK-A8wvSLQQKoAi_ZZgefFjDkwUp6QM3B0rfMYIO53iDnk3Jhny_F-rna3M-JP5oUIjCaND_Ihm5YUhJfcpUdkdF-Sf_cqZZMnD4f3S06mz6Ce6OZZ9EtsbXYaUj9-wTDRKH8qzHrRaJf2Ffc3Dl5O-TxyknSJs4mFJNyTH4Eh7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناموسا یکی جلوی گذر زمانو بگیره
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/102194" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102192">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af48b4918a.mp4?token=Pz7ZO2jenldDJRqtZr7I8N8uMAR8m5vw2jSxlcJbAGBy5bUX_mEdaSYg9RvghLlRErhvozXipDgGiGX_hnoqyjbvJZco-CfYFcfthqzs706Jh39BZt-u2SQE2Wlupm-4yRLWI0esCLskdr9zIlU9rc9_AGXZfPL24JozlVZ5jHXKQNjZ-mBS0WXj_FJMa0Qg2rTNdlCp6t4ai1AEjtvWsvarUm4hkf4vd6hKAx193U48ixrHS4MkoP-5bVMBpVmkd3xtqsz-z2bvsAvURLd6qvlTZKrKXApwGD9YJveqoE8Pglm7nStKs1r4cw4muu-5_0lgFgUjkCMUuPa45R3fRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af48b4918a.mp4?token=Pz7ZO2jenldDJRqtZr7I8N8uMAR8m5vw2jSxlcJbAGBy5bUX_mEdaSYg9RvghLlRErhvozXipDgGiGX_hnoqyjbvJZco-CfYFcfthqzs706Jh39BZt-u2SQE2Wlupm-4yRLWI0esCLskdr9zIlU9rc9_AGXZfPL24JozlVZ5jHXKQNjZ-mBS0WXj_FJMa0Qg2rTNdlCp6t4ai1AEjtvWsvarUm4hkf4vd6hKAx193U48ixrHS4MkoP-5bVMBpVmkd3xtqsz-z2bvsAvURLd6qvlTZKrKXApwGD9YJveqoE8Pglm7nStKs1r4cw4muu-5_0lgFgUjkCMUuPa45R3fRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
کافو: وقتی پاتو اومد هیچکس نمی‌تونست تو تمرینات اونو بگیره؛ کالادزه، مالدینی، نستا، هیچکس نمی‌خواست اونو مهار کنه، دیگه ببینید چه سگی بود که می‌تونست به راست بره، به چپ، سر بزنه، با هر دو پا شوت بزنه، سرعتش به طور دیوانه‌واری تغییر میکرد، به سرژینیو گفتم یکی از بزرگ‌ترین مهاجمان تمام دوران‌ها به میلان اومده اما یهو همه چیز عوض شد...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/102192" target="_blank">📅 22:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102191">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6KfjnL6fczr1z8OutQ7Fcyem4UvuzuLpBR9Dqk7ziEamUadjkTuj8APgJyLISLKiRdTSa5wuFQ_kZgUKacTw8C1s6uWis06F6V1Vzvw5DhrGm_4DszucwHhfDTXKdcGDhd-ZlwEyfbXytanEl0P5okLhi2-XmJjDeIrxiGGurYlsFCgkFO3TlIzzScyvtawa_Q06ftw-xgjvLRCdaR7_Ov85L-HRNqnPvYKEKyz0IFkN3VEHAAGWdbcyTaq6JeI4AVJ4Y66RrlSiEtB_GF1zcIFc7LJ2Y-OWDK5I7YgpdsPvBjxEuRtj8metTZth-thLPmT0Unhbv_Lsjyggcv9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کریستیان دریسن، مدیرعامل باشگاه بایرن مونیخ، درباره اولیسه:
هیچگونه ارتباطی از سوی باشگاه رئال مادرید وجود نداشته است، نه تماس تلفنی، نه نامه، نه فکس و نه ایمیل. بسیار شگفت‌انگیز است که چه چیزهایی منتشر می‌شود، در حالی که خودتان حقیقت را می‌دانید. این واقعاً حیرت‌انگیز است. او هنوز سه سال از قراردادش باقی مانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/102191" target="_blank">📅 22:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102190">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b8f5f5029.mp4?token=p1K4_-zabxe1nJDTmyKo_Nl2IBhlz_V8dWyayjO59LR1hmMBJ8OD6f2op4AYl3eXFHSYTi_kY2aHjX-GDwAmxTUIcC-9s4uzu9xM9qSXJ4rCmS4h-stW3ATE90lPrSvO-5t31pVKjg4VfFUfCqbukRtusoGkkHFYF2dQsIu3dQ9IqQUA7a9ojFYny1R2pYYR16C-ou0BXP88KocdsS-2aF2M0tOIdscYqKY5WZ1Z8ZLIaYHsWdR2CisyGWuS5rkhCz6MRwVupecS0CrLm9Ug63nZk2bKW_hyTpdhv8GA4Sehn84I6X1Hv0mc9SzYOZuJ6ctZaR-JZR_7M6a7qgWSki0qddCwJdVUMJhl9Hw29J5J8zvFL5OGyN0tQHb_rd2Mn_xLuecp_B1oZShaw7-mRGp_M0yMNhvqQoiRPiccAkAXghDOK_A8xuC_jg1Qsj7ob-9gjs87L124PpKoxve6h6q-9W0l4pUNhhW0feB3KPQANL2IbcmjOVKTzzaK88nGWaAlLawC68UYV-F7TcA5gK2RZvaXhnFqvZnZbgNb2Vy0t-0H2WkLTYaaAGRRAQBHBXqB_IPZ-wmzOWIKf9Vc0dqjeYkQ427o3gBd-RoQBq19YiWn3wDLKeBhPEoZ1ByW_lSe5hcDUaPDMA_LSewtjr41mJw5etAjM3mFebYcf30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b8f5f5029.mp4?token=p1K4_-zabxe1nJDTmyKo_Nl2IBhlz_V8dWyayjO59LR1hmMBJ8OD6f2op4AYl3eXFHSYTi_kY2aHjX-GDwAmxTUIcC-9s4uzu9xM9qSXJ4rCmS4h-stW3ATE90lPrSvO-5t31pVKjg4VfFUfCqbukRtusoGkkHFYF2dQsIu3dQ9IqQUA7a9ojFYny1R2pYYR16C-ou0BXP88KocdsS-2aF2M0tOIdscYqKY5WZ1Z8ZLIaYHsWdR2CisyGWuS5rkhCz6MRwVupecS0CrLm9Ug63nZk2bKW_hyTpdhv8GA4Sehn84I6X1Hv0mc9SzYOZuJ6ctZaR-JZR_7M6a7qgWSki0qddCwJdVUMJhl9Hw29J5J8zvFL5OGyN0tQHb_rd2Mn_xLuecp_B1oZShaw7-mRGp_M0yMNhvqQoiRPiccAkAXghDOK_A8xuC_jg1Qsj7ob-9gjs87L124PpKoxve6h6q-9W0l4pUNhhW0feB3KPQANL2IbcmjOVKTzzaK88nGWaAlLawC68UYV-F7TcA5gK2RZvaXhnFqvZnZbgNb2Vy0t-0H2WkLTYaaAGRRAQBHBXqB_IPZ-wmzOWIKf9Vc0dqjeYkQ427o3gBd-RoQBq19YiWn3wDLKeBhPEoZ1ByW_lSe5hcDUaPDMA_LSewtjr41mJw5etAjM3mFebYcf30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇪🇸
یادی‌کنیم از هافبک‌خلاق دهه گذشته بارسلونا ایوان راکیتیچ کروات که زیر سایه مودریچ دیده نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102190" target="_blank">📅 22:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102189">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQ-xIvGh_0ZCc1aYujaqANm3bUXHfuj2sPMTDLF26dQZVaefwZj3TCKJf_h9xThxbZCPJq9muVvZB3KgBy0lJ9kaDf3t8-kSD0gPc9jbRpXYOhQ59HUhkT9EYeWsE_2eaqghFfu3qJ_d6Mn2iuw0O_ggpN046n9EEju33KOTIlYlWx6LjFM2LOqr1EohxELVnDN0086qhpmFNEQnVZWOfx7TVn0xZjI-i4T-GJUihmKh8ZihEaWivn_6WRLR67q0Nzdm6KPr8qo11xNHWaGPaEqcd5Q4-gqGC2ufV1UQtFTGoBTK2XM19dcA9098N3cWswX0QpHb1vwu-WqOF7bjDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تیم‌ملی آلمان قصد داره درخواست میزبانی جام‌جهانی ۲۰۳۸ یا ۲۰۴۲ رو به فیفا ارائه بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/102189" target="_blank">📅 22:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102188">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laOVYyDqNxCvrA_FRMWCeQW55KubQQ_Ty6fb2TIrcygAVoC7IRPd0EhaGFyinLBObq_rUuDCWt2uxcDnCFzGGgC1u1WaNsZs7Ju04uOvzOKfN6C5WjdYqgm9Oh_p5WQIGR0p77gm3cR3noYq6UfpOUmVh3kQbD7wEKgjoGqvVyFAKmSn6lazim-gsqOC1qIK50ogj0h0OR3Vkw8DTrSgHBjh0HyZvNydPm8l08jHzaWJHHfDHqEKeMH-CFDlPAj29AexhzqEk9swBvE-s-a7rE3TxUcUxbT0AH2ZnhZPvhgkawL5-wI4jAa4inA5_fS_VkbGjWo4jkks349Vl5_Eag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
از برند‌های محبوبت،با تخفیف و ۴ قسطه خرید کن!
😍
🤔
می‌دونستی می‌تونی از فروشگاه‌های فعال در شبکه‌های اجتماعی مثل اینستاگرام و تلگرام و سایر شبکه‌های اجتماعی، با تخفیف خرید کنی و هزینه‌شو در ۴ قسط با اسنپ‌پی پرداخت کنی؟!
🤩
🤩
کد تخفیف ۳۰۰ هزار تومنی: PAY3SCP
⬅️
از طریق لینک زیر لیست فروشگاه‌های طرف قرارداد با اسنپ‌پی رو ببین:
👇🏻
https://l.snpy.ir/v06dj
https://l.snpy.ir/v06dj</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/102188" target="_blank">📅 22:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102187">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzNhb7DqR_VgR_xxMysTMk3xsEKYJq_kKb4x51kGY20IiB0hq7FJruu6CFodKaAPkqjgXMwEqWFI--p_B7W4L2Ky6vBWk2G7Dfh9Y3jffev9uEjK6ZwFlX2DMAL5UGsmVt8Wri5dXOHVxOVnZwh1et_JkCicIXSNaaZF32CLxMii42-mnN4dFGq-0jLtZw-rJzKit5q_Aj-TnbaA3Zb3g5WzRVNh0oTSUmiBKHY_RTQM--8Nl7zvANTrve-W0qjczvypi163AXBIP_r4iih_ld7IQDB8t4ecdYxsk9fx6FNeHYoYfJAavdyCCmGa1aBk9rgEs00d4G7thojQYfXKVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏆
زیدان و بازدید از افتخارات تیم ملی فرانسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/102187" target="_blank">📅 22:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102186">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gz3UNkk3rz3N7CX950Q8bMXqxAR4pG_gzCFE-VxvD6_hSCE0YH5wT8YAReyMxRL07E8Ww87JX5mwfLFxak5ZIM-XgEwNCaRBx5oS9GkHcEghX_lchZdwYHLi3UPOYsIjwslHrGuLxlhdJrWJHVWt5DB8Rh5EwoPiTy_y4xTD4O26SfBApuRhbaFWYHYRvfauMkEYTfgftb3XqzQwCXXAprfdR2qTlE6_z1e_h-KVxQMHv1MGw46rViFcPlor_Te1JyysFcfA-dzxuCiXCtCtmmbk3DUS_oKlRM44cBDC0Ei_9nEDgTIEw0KbEWwJ0fWt0aOLi-Y1RM-QsvZwwq5ZZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔺
در سال 2020، بارسلونا تصمیم گرفت که دیگر به لوئیس سوارز نیازی ندارد و او را تنها با 6.5 میلیون به اتلتیکو مادرید فروختند.
🎙
سوارز : «تماس کومان برای گفتن اینکه روی من حساب نمی‌کند، 40 ثانیه طول کشید. این روش خداحافظی با یک اسطوره نیست. اول گفت در برنامه‌هایش نیستم، بعد گفت اگر قراردادم را حل نکنم، مقابل ویارئال بازی خواهم کرد. شخصیت کافی نداشت که واضح بگوید خودش مرا نمی‌خواهد یا تصمیم باشگاه است.
🔺
سوارز رفت،21 گل زد و اتلتیکو رو بعد از 7 سال قهرمان لالیگا کرد.
🔺
و وقتی مقابل بارسلونا گل زد، اون تماس 40 ثانیه‌ای رو فراموش نکرد. نه جشن گرفت، نه ذوق کرد. فقط نگاهش رو کرد به جایگاه مدیران باشگاه و با دست گوشی رو گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/102186" target="_blank">📅 21:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102185">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpUkYef_MGxgaW0vmYUzYAe12hmhvL7Eq_8fyUGZOPTxsjTOMSU02bBk0EBrD0YF8fD0Y_YILrlKbFQY9XbULVYMF3jqRgbysgFHuEj-vSYNBHZ_CCli2Jh0lAO7OD-VpeDeCcqv0r_wSdqFdrFpn7merKtRfcNnWfcOTe9-8_R7S7HpVy9j0I_bb5bvTXcvCnW2kreKH4DhXME1Sejka2qdW__OWEeB_dc5pQZvap06M15OMDRcVohaVmV8BAYHEmGKzRYojB_z4JwyLRJ_2yKO2Zc5wclle633OoEYC0g9HUQGHcr-fUSLS2jc1kgYb96jSkO1pUiWxg02izk1rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مادرید در اولین بازی تحت هدایت مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/102185" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102184">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vV6Z9umMzgfyuqDN4cBvHkMNNRt01EegHzbI_uQVioQTjPzA9IJA9AXmmPobZtWKHV2_ml3sdCgmJeMVnEU_inAD6xyPAPUgaybQnV3E6dBtd_VfyniPYN7PtD5Z73A7t0KcDNjcRg71MGIXK91JSVTfOh2hkxwTmQ6iYr8zDDu6-BAwysgibHiUtYMg8G4zcg2gY42-_2dy2s9Xn1bcFvlmrND8BtSs2DeZmi8pX8uBeMvLVqkxBAfgcHPSep3Bar3SSfZJ4_rTvt5EyX8QSG9TbZ38KuMUmRqEct1Q0aXo_psFN8iKV9xb0ztCwUBhIb97DuXDzYv4aFnE381GAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#رسمیییییی
؛ کسری‌طاهری هم پس از مذاکرات ناموفق با پرسپولیس راهی نساجی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102184" target="_blank">📅 21:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102183">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aItq0w75KW08n0o3wFN25_1ka7ok2gxEEjYJOODNZQimCaiClK0upD4vTqiPYiuwB1aFI65qVvnD_LUyizwY71GRIQpu-iTWqFqrk8Jcrf_d0vEWGjDHDWsOIMPAdKLPdMl3dw1ZjtnKLY4yQ4OK0_MbATZvtkzeaYyiFNsD9hbSW5GIC2giqRpcBsPAuTHsvudlbGWGIB2trKH70qXjQELwRQNYVaBFmM6BIAF8Qpxu74_-UO0_XshIhNvX1KiK7Bzw7GbyE0vnh5mwg19s6vnIuLCgUKbzYrU1vNTnvO3qXGykW6t_S3QdRmrpm0ZSWfMhiLF0IgQlWzZKTwfIpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست منچسترسیتی برای تور آسیایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102183" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102182">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b71e2610e.mp4?token=PD3ZQEMpVenL4UsDHdxIC98sbahZCiAMHoDzavtkluxpNej9NLs7q0DlTpq7TPAgW1vBufwjdYnZ5cEW-oqv5nXdiMU0UeglmoYuyvc0-nvmu2uF6hZd7359p17ejRwkUzQQ9T4Cs1nPfxcxJGR79qAGKCJENEPzdyYs19zs4ZncTizOc56BQ7S3J_G2_2AQqVVMimMXqFkbZ1avsghQMK3OAHaKksVGGbzAY0OpYYINfP1tmS540x5IJ9DCEwXxI7kP_b4zMZxPawJTfGUVKE3j2jfBbQ8--aDgpL1RRBO38Jp95KcXQmbT7ohNk1BBN_kL8AVVJz_tlCIii85tOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b71e2610e.mp4?token=PD3ZQEMpVenL4UsDHdxIC98sbahZCiAMHoDzavtkluxpNej9NLs7q0DlTpq7TPAgW1vBufwjdYnZ5cEW-oqv5nXdiMU0UeglmoYuyvc0-nvmu2uF6hZd7359p17ejRwkUzQQ9T4Cs1nPfxcxJGR79qAGKCJENEPzdyYs19zs4ZncTizOc56BQ7S3J_G2_2AQqVVMimMXqFkbZ1avsghQMK3OAHaKksVGGbzAY0OpYYINfP1tmS540x5IJ9DCEwXxI7kP_b4zMZxPawJTfGUVKE3j2jfBbQ8--aDgpL1RRBO38Jp95KcXQmbT7ohNk1BBN_kL8AVVJz_tlCIii85tOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
وضعیت صداوسیما رو؛ چهره شرکت کننده در برنامه عشق ابدی، مهمان برنامه صداوسیما شده و به ژیلا صادقی میگه شما همیشه با معلومات صحبت می‌کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102182" target="_blank">📅 20:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102181">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcRobxhuJr7Icc_Z5uXZM1Oi2JZZppFGG3PhP3Au0VmKGNUYA9fhalR_p27pg6RU7GlF3s4yB9Ix_1fV1zjW3QjuounzVCd0cOZS-emrwlPkIyzaMRAu7dn9NuRU6bhYON2rQ-SlCflDzAo6oddNJTEfOTsV-Vlq_udVbCH_F6vQ_MT1JWzVHw4b3zVXsvEFAFw6xY4cgCstutUNVGObE7hY_merN195ovqqrJ2QWWfL4a7DuxrfqVuucP8vhdx1j8W_T49Ad1jip7VWRxVkiUvo6TzxknWitEMlDJJrivqceTHk84t_Az2LVoK6Hbgyz_dKhn9xHTzASrvmFqOshw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوری
🚨
🚨
🚨
🔴
🔻
باشگاه لیورپول در حال آماده‌سازی پیشنهادی به ارزش 94 میلیون پوند + 35 میلیون اضافات برای جذب بردلی بارکولا است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102181" target="_blank">📅 20:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102180">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be1bfab961.mp4?token=CyXEJLafMMr5SP1Wbf7d-rR-eiQrVIKTzXtA6KDazNLj1zywfOV4e0ZqSD4xMGX2uqtolrN_6gI7n8mTFfDdkmpIVHy9SJaE1X5ItCySbh5yOczIKpmbEyNFbixEDm6HrUIW2XhvlVcz-0FesoMq3YON2U_ItEl1GyPRYcOz72AlnLqn1Biw7-kc8GAMbKsZZKutZYrmMC6fWvsEy-1GsilPrhrhr4nByv16DHSurCdM5B2cYqhQ2qzkDJTMXeW7g_79d9lc1ammMqBnTt1VhBoua-hbUjXk1GfMQChfq7oYbiA31FJZ8UIpdOM3l8IpUjBElHLcMN2IqaHFGoEx3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be1bfab961.mp4?token=CyXEJLafMMr5SP1Wbf7d-rR-eiQrVIKTzXtA6KDazNLj1zywfOV4e0ZqSD4xMGX2uqtolrN_6gI7n8mTFfDdkmpIVHy9SJaE1X5ItCySbh5yOczIKpmbEyNFbixEDm6HrUIW2XhvlVcz-0FesoMq3YON2U_ItEl1GyPRYcOz72AlnLqn1Biw7-kc8GAMbKsZZKutZYrmMC6fWvsEy-1GsilPrhrhr4nByv16DHSurCdM5B2cYqhQ2qzkDJTMXeW7g_79d9lc1ammMqBnTt1VhBoua-hbUjXk1GfMQChfq7oYbiA31FJZ8UIpdOM3l8IpUjBElHLcMN2IqaHFGoEx3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای انگلیس با هر پاس گلی که آرنولد بده قطعا یه فحش حواله توخل میکنن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102180" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102179">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a5b1e0f9.mp4?token=HnF2FKnQc6SKV_dFZbhLNJbeGmgsmBQfMFerp06SH5b7t-JSgllCK2sNsT5rAbeK_jPpmRCrMRmbjPGyXuYUNRcXDOUgajg-RgS5s2NY3Ygc-hwDacMu0N27NHB1DoJUy7tIUERT8fXjw2WHISvmI46n2zLI6bjn4F9a-3oeFK2iR920eRiQ2uHU1t2RX0rA8PAOEaaijCs51nYg3pBtGTNEfZGRK891A_fZZOzUGo5tqZ_yROnGH1aG8Dtg94DjbJjKAZp4cXoc4axScnm1EK_I3JFD8UhRMDN7q3JtckwBKEwnGmg7lZUDiwhxR1HoyFMHraOb0NjF2zVur8Xb0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a5b1e0f9.mp4?token=HnF2FKnQc6SKV_dFZbhLNJbeGmgsmBQfMFerp06SH5b7t-JSgllCK2sNsT5rAbeK_jPpmRCrMRmbjPGyXuYUNRcXDOUgajg-RgS5s2NY3Ygc-hwDacMu0N27NHB1DoJUy7tIUERT8fXjw2WHISvmI46n2zLI6bjn4F9a-3oeFK2iR920eRiQ2uHU1t2RX0rA8PAOEaaijCs51nYg3pBtGTNEfZGRK891A_fZZOzUGo5tqZ_yROnGH1aG8Dtg94DjbJjKAZp4cXoc4axScnm1EK_I3JFD8UhRMDN7q3JtckwBKEwnGmg7lZUDiwhxR1HoyFMHraOb0NjF2zVur8Xb0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
کصنمک‌بازی مجری تلویزیون با تاریخ ۰۵/۰۵/۰۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102179" target="_blank">📅 20:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102177">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9rrKcRZvlMATc9gx3uXanPggC8oPdY46-1Qr0KfNpvmEgGrLgKtAe6IPuSV9BoS3ezqkUk4S0ffpXX6WDhljwl9UTz4-GGLaz4h_VoRoPynEZn1R4u1GhSs_wqFZcO59LCGr2_w-hvD6UyoS0f193ZqzK_jrUQtQjYidgYwxjeNTwtFSxDHCsb-BweQ5r4GNOkWdkAAd-QJ6Nfny8oZ5JkoAXOg2LZYvOLgRHIIUdvOew-iOzT6wFEzCZYGk6FO576NGRm9u_RBRsk9f7m_vHKBlw2morLNUDgKW-GfRMjuyVhuG6NDKxy1Irj5q4yDqH5Y_kh3hQ0Esp6VXqq1zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsk-WUsHWM7uLk0Naao3XQ5hUPDUmdwlEAjwc-zsgCZlaa5j1ieXRa4L0EbQwpU3txcbK7zBIE53-BrJIOr4WYDmAynkA1VYGKkLpKrpxHVCq_8nasLziWmjB1q2Irzuce_Q32Sh7Wivo39KwZI-TZibt9LEEdwyiHjZMnxaOrdkHTI2ioA5Jr6LygN12jXzftZ3igpk74h1kVTiHLgfKUl_-N_FTDBgEpxd0Un1v3KVgrL-h5Fzl9xEJDqt4k2VXL9S825OBWMrdWRI98-1ztxQmI4BqgbxGUaQOAtKcf8xaEsvtIx2yB5iKng5A2VqQQ2WDwKjUnS990TJFSGZxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🇪🇸
فکت جالب: چلسی برای قهرمانی در جام جهانی باشگاه‌ها پول بیشتری از اسپانیا برای قهرمانی در جام جهانی گرفت!
💰
🏆
قهرمانی جام جهانی باشگاه‌ها: ۱۲۰ میلیون دلار
🏆
قهرمانی جام جهانی: ۵۰ میلیون دلار
یعنی قهرمانی چلسی در یک تورنمنت باشگاهی، بیش از دو برابر قهرمانی یک تیم ملی در بزرگ‌ترین تورنمنت فوتبال پاداش داشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102177" target="_blank">📅 20:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102176">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Of6oXoNr81IHWMPOOk7-70LS-eI4LNQX2Q9muAsMbxFQ_aChvp9_WKgJDM4zzhzyhD2ZH_bGI8iVI50SQ1OFnBOwoVD285kP1q4-PDqd1wCEX0JS_xtqXB-dTEBaC2ax7f2ypSWb6O0y3lAz83ghRbNbvlrp7UdO45-UoasISwg4ZbNochJ3IouSIZFxihGNGH5LlKOc81BuA4t5HfmX-bBH-AsP2HSDFbqfDPnsjKaBAtqYq0EXqs0V_O0O0ynxmuDekJ0xyxZsqKJV0Sd-HtU7flkFC7wxPoh-GYLZXG_f4kI4001FBvP_Y5r6vKOJsF9HWJf_swh2o8SqJKENhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#رسمیییییی
؛ با اعلام باشگاه نساجی، دانیال ایری، مدافع سابق ذوب‌آهن و ملوان به جمع شاگردان مجتبی حسینی اضافه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102176" target="_blank">📅 19:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102175">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMGBECrsWuYesRGX3JKZh_Ky2M60XGhCl9KBP4U3Lmdml-UHKxe4azKG704Afwr0bHMQ8gQUOHvkoIbIkZqLnhEGWOrBC_5DfNMSot0KH87oSo2b2ZQ9bzRRf6fZuA9YF8C_SgQJqYdtW1fr5H2aWp42jNrYbgrIpBLCwgDbuncYrIjiu58WMwGYOBrRJ4Gm-n-TuLcKvIR7aL_28h5Y5P0wU4SJISmFwRZdbdSUgCucaL9VE5uPRVFCiIk6ux6D0bb4KyH9rNY3ppqQDMF0tjce5IWh006WyfjRUgT63t-ThdEMl87sI0LIRzsiBtS_qj-ZCFzpgJFgsMTNa7zUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
#فوووووری
؛ اینفانتینو تصمیم گرفته که حق برگزاری مسابقات جام‌جهانی رو به سرمایه‌گذاران خصوصی با بالاترین رقم بفروشه. کوشنر داماد دونالد ترامپ از خریداران مطرح طرح اینفانتینو به شمار میره
❌
از طرفی یوفا به فیفا هشدار داده که اینکار نقض آشکار روح برگزاری فوتبال هست و باید به صورت جدی با عوامل این تصمیم برخورد بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102175" target="_blank">📅 19:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102174">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kl4Xejz0tKUkZ1XxAHcL_so9UL94fECmrr-irsJBzmLU_tFFJTgDEsXhDyxyScs86QqWhkZNvQ9dmLjyNc2QkgZtMLkkq3ujsxVKD0O_B0aaqQAp2YsWXGdTsb2AgUGFWRBv1kIsTQnjgVOW-0t-a3QrsnLWZxnSNhpnSY7LQbzgcmiry1qAAAN9YSVO9GyQzoqAH07n_FpXWDJXy8v0VQgyUzOVE1WmtD2Of5TnSzHgP7gne4NFqiJFViEeSCqXcAXGXDgiqgQbNEmC2MPlQSBB60rZ-jBQet3DJxLhYw4XLNhDkXHWqoSP3U6Tnu8J3nUb-oPPcTQ1549dYkEmPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
اسکای‌اسپورت: رئال‌مادرید به پیشنهاد آرسنال برای جذب وینیسیوس جواب رد میده و هرگز اجازه خروج ستاره برزیلی تیمش رو‌ نمیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102174" target="_blank">📅 19:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102173">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cb3c3fae0.mp4?token=kg_VaQp-YO6BbSys14rqrkN3LlYmXH7fqR8IC4QwhLHifiusWUWpBSSfzD0IjJ1qY09IdHzHC_1DBvPk-Rvcf6yi7A8yuihLHM_GTXhrC6yoHvw0NG-138Lv5fpOiIvT6xzEKXM4iMxixnyrabsgGb-skdn2KO5pU7uZThti61E1sMn4K3ao1o0wr00KBDwodOkuH6K0PgOa5zJsZbDXyHut3v63_r3oO7hJfzfGX9wtdoOuD333_J7wY5_shIOb83u88BQe7VxX7BmEyb9aZg-3KFe7HRNudqyyCcQiKa16CQdDVyodrJSz2QhdHdorYRmVt1QyoGfZp9OICCzDHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cb3c3fae0.mp4?token=kg_VaQp-YO6BbSys14rqrkN3LlYmXH7fqR8IC4QwhLHifiusWUWpBSSfzD0IjJ1qY09IdHzHC_1DBvPk-Rvcf6yi7A8yuihLHM_GTXhrC6yoHvw0NG-138Lv5fpOiIvT6xzEKXM4iMxixnyrabsgGb-skdn2KO5pU7uZThti61E1sMn4K3ao1o0wr00KBDwodOkuH6K0PgOa5zJsZbDXyHut3v63_r3oO7hJfzfGX9wtdoOuD333_J7wY5_shIOb83u88BQe7VxX7BmEyb9aZg-3KFe7HRNudqyyCcQiKa16CQdDVyodrJSz2QhdHdorYRmVt1QyoGfZp9OICCzDHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
😆
تتو دلافوئنته روی بدن کوکوریا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102173" target="_blank">📅 19:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102172">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QitpTL6fOT5Hf_RaRhedpE8Mpu66Z6xFBS834CXbwW7YrZwzJu5Kijt_kiZ3Ndp3RJqHiJyzFSHmyjYXGx6M-dOySpyfxxBQB_U470YUgrjK5Bnc_auptC9RoFov25Ok_TiUFbxkvSRVPHSw7i-ZugtDCsFl1H7vjK3xbqncpq3TDn1TQ9AagW78hEFOaTsCmdqRGtqEfdZvTXZKorGIjyVAsPvwayoZguULvOKFqc0yAFHdQml6w9KuR9ys4NYcEXswGWWp3WJbw6g4mhlwIkJ1WAPYjvgBjMMAUm3e3DpZJiS_1gBlXE-yOFYiprIZhDD-HNLorWD2xmI7vJJ46Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مادرید در اولین بازی تحت هدایت مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102172" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102171">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/164942a925.mp4?token=DPsAwkIYQP0L3sMg6jlVim1IfxUuzrSNX_nD6I3GjY90kbNI1iXWYPIgpphwvXcbeym_lxJTQJX9HzAvcZacf4GxWnn6iTH8HUQam0zp2_gxXGiTLp2hMgPc0KKFYUkU8X-7zCB5TJ6HtJYhsWK5Sj1HWhIYmGZZJnw86lZLFqHGLZq-jbU37a_VNqU0fRqjtnh7OYtImAUi_SFCo9hbjM_6nEnvgrMMCDzukbqnFr1RkaAXe12vdWm0TwlhSyQj_sbJGTmPG6kJLItcsGJ95Z2eLcbncXMIioBlRVB-9-iry4wZ-jKXvYve6nfDCoH6goQVUMnQlgIAxgd9GodkijiHYzKFAesmAR5xX7yiSVkpv1PUtRWCEEeOgNikVaoRdQueaS4m-83JBH5CeloguGTzo1qPyswwiWIg1iWk6UQLh6KpFm986CiDtkQnIFPGqwDCYiHMps3lNUZNYhOmt36u0afDLtlM5G8u_75zOWMmfwWz-whoYuPcHvxUezPNmLnqyVulgscLH6z4RsyuP4ir4aLLXU5lnVtxBq6W924Q8BNGqX2ADOrFoGS2lZiq4sgf1EYLtT4gygLqJTjAGa-RtkJn27-mSe4J138Uz2L_br46aWAgzvCXeA-yqoCRDr074xISvRxBGFKla7sAbB67h-CEjw1GeS6B5OzNQ7E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/164942a925.mp4?token=DPsAwkIYQP0L3sMg6jlVim1IfxUuzrSNX_nD6I3GjY90kbNI1iXWYPIgpphwvXcbeym_lxJTQJX9HzAvcZacf4GxWnn6iTH8HUQam0zp2_gxXGiTLp2hMgPc0KKFYUkU8X-7zCB5TJ6HtJYhsWK5Sj1HWhIYmGZZJnw86lZLFqHGLZq-jbU37a_VNqU0fRqjtnh7OYtImAUi_SFCo9hbjM_6nEnvgrMMCDzukbqnFr1RkaAXe12vdWm0TwlhSyQj_sbJGTmPG6kJLItcsGJ95Z2eLcbncXMIioBlRVB-9-iry4wZ-jKXvYve6nfDCoH6goQVUMnQlgIAxgd9GodkijiHYzKFAesmAR5xX7yiSVkpv1PUtRWCEEeOgNikVaoRdQueaS4m-83JBH5CeloguGTzo1qPyswwiWIg1iWk6UQLh6KpFm986CiDtkQnIFPGqwDCYiHMps3lNUZNYhOmt36u0afDLtlM5G8u_75zOWMmfwWz-whoYuPcHvxUezPNmLnqyVulgscLH6z4RsyuP4ir4aLLXU5lnVtxBq6W924Q8BNGqX2ADOrFoGS2lZiq4sgf1EYLtT4gygLqJTjAGa-RtkJn27-mSe4J138Uz2L_br46aWAgzvCXeA-yqoCRDr074xISvRxBGFKla7sAbB67h-CEjw1GeS6B5OzNQ7E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
👀
برخی از سوپرگل‌های بیرون‌پا رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102171" target="_blank">📅 19:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102170">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfZzYJf5x2laBRqpRtHT1-2rSmbi9_F2BGE4dIVSYrCAu81F5EBuyahKfmdMbWhfJXsBwvvJeiA4BSgDuou0DfgeAr7rRc7bKbH8Tjz4y9FngItf621tET9jFzm_AISqGv6TuvG0LB5sjGcioOmIvGKLgQVq8KR40bvqYJwU1JqXfQUhitARSmmBt_hHkmMJFGmXzyEea0-hqPF4Y9snw35EWVriOeV7bnziA4eko6EbMiQdCpkkHqpbrC3Tl0mtzSU3WBMlypb85OAklamCYzDke3Nh6XoS0PBpx_cUKrzPEN8rJamtPPm4hnfcWgSruaByJjCCqkq5_YW_2dNnlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
‼️
منتخب بازیکنانی که در پایان‌فصل‌آینده بازیکن آزاد می‌شوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102170" target="_blank">📅 18:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102169">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjb6-pnzDmprmuJk3LPiBPFtcL2cPuZU9SV5FkcUCfUfkMdOZ4zwgO5mL4fCkg67G3evqQdiCaCS9c7MEGzSOoHq5M8k5g2R8jCgMX-XHOG5ELhbkM2oj-wfBwntKToZIGkMPkaMeLFS9DwybAowiSBOu02CW86Fi8UvDQPK1fZcawtQOr7YwAjWSkuZFzIzeC9hx1hqXapSJeVJUY6tcw0Xop_h84JpWn6Oh4OQjbgdYC9ZW_85trPMt95sRb8-afWRYnxHAtYSBGZnpGu2lsbavCxB6PqWflzlWk1bLhu8MkwkrPKFtT20yTrQfm_Aln3gdQT-9WJ6Bwt7OMqhWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔎
🔵
ژابی آلونسو بعد از دو هفته حضور در چلسی سریع متوجه شده که تیمش برای قهرمانی خیلی جوان و کم‌تجربه‌ست.
‼️
اون گفته به بازیکن‌هایی نیاز داره که تجربه و شخصیت برنده داشته باشن.
🔺
جردن هندرسون — ۳۶ ساله
✅
۴۶۳ بازی در لیگ برتر
🔺
دنی ولبک — ۳۵ ساله
✅
۴۰۰ بازی در لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102169" target="_blank">📅 18:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102168">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYoBhxsxdKHAONZ3jtq_svla7rdRx1cSitgfTM4bXNxgaAX4LRw8A4VKYqAvIbH-HDcMrYUUmP_Qqh8LN5ZwPqO286BlyNgHOqj95M09AOG7lhP9JOnsvB5GPa62vN_fltwWJ-pFM1gnRxaggija6Ob0G-Ph9dIe5_ukw9fp-MaCTNyTAPczOy-rbCMW0qs-9gapCc7nWCeztL5spSudHxYm_8M4mTnKxSA0IC9m0LzNZ1HuEcVpYyfWdMjYoweNHm9ZjCPYeqbDzIY5HFaGyCDyx7twAeO592RKxwDFtFhL4IM6taQJ5fS4Ve4BSuuX5-tFVezVJ79StsF1hriFTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗞
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: ساوینیو به منچسترسیتی گفته که میخواد تابستون از این تیم جدا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102168" target="_blank">📅 18:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102167">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVNKw5JVl66Szvb2AkjuukNI7zu_4_qDBxj6SEPkFRl-ecUQKSqIA09x7kh0t_5m0CUbTqWT8moSgjREbKKlGRdr3uqZwATffMISpJXunUjaNSGC1aQTjZuHgb_qZlP3kL5Isfn7bMytT0AaR8g4JWIlvalyrtq1znXVgeNnjVcYm8phHU2y75gdrsk7wHsqwp2U_gb5jfh4L6qjOX93Qsb6FpfvqL-UMLoVtES4e9JIKx2hfNV6z-AsbMXVZ3B97jamQBDGicJgXGnsWnMjTe0E2r4P0b--QGXd143fD0dJzO-gC-oAer_x_O8NapB6NbhefS_lF0yv2S69ZgVYTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نیمار جونیور درباره لیونل مسی:
من کنار مسی بازی کردم، مقابلش بازی کردم و باهاش تمرین کردم. باور کنید تلویزیون همه‌چیز رو نشون نمیده. سخت‌ترین بخشِ مهار مسی این نیست که جلوشو بگیری؛ سخت‌ترین بخش اینه که قبول کنی بعضی وقت‌ها واقعا هیچ کاری از دستت برنمیاد. از زمین بیرون میای و فکر میکنی خوب دفاع کردی، اما وقتی صحنه‌ها رو دوباره می‌بینی، متوجه میشی که اون کل بازی رو کنترل کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102167" target="_blank">📅 18:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102165">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vq0iXaaicdVpXAmuSld-PH3gH3h0pTysAdTFHR49jFwKC12aMFqcTRiw4QRx-CZqfvaA4e_1yVK9YJTnTbwujJyWWmMTxDS163rPcbFUvMWksQ2NQiWnjPlWQ1rD6ew2G3wpGuOdyHeBLdeDgAwdIJFeN8sMnRVGWrdzvybHN8MQaCdSJLhZ2cQMumeavPjg-97LI3nEtp7u04LsFZSD_U8Tb240-6ERuLUX3eWjr1AJ0WybnPHJ5gvVOxb9yh1ExdJeNN4YHMQZmIwd0twoRqlw1PhLIdrVyqhCcUMiF-R0gDQxVj0qTfnnrAe3Pyg2aLveumUsfOa4ki8I1Otjzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LD5ka-4F9pbmf4NfyxziuDhsldzHyeHdzv4vuzChAInisz0dTBMIwJ5ehhtSk8uIxVj48f8XhjlCO8GGTIONfADkmbWeYq2Jbc4goxc7uHdAQ3SnJozbPQTb3pX6UkqQGNacKYDPzhRYO2rKHvZKEzTz0nAE9uy7V3y0M-2Udd1nmUJ99aaPd8IUZzX27GoiSGE-pafIZcaE14CctrFJ1bVtq1vC1-8mXx9gnsA_Ih9Q9DF9ih6DZFa6TqAKP7z-621HHEfYhj2cR5aN7EGMNZyopzsrFomoOGmKalw7g95r6O5Ydn0jrcsjOoTTEE-iolNRfsyiaS3t_k4EI-ZpGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
🇦🇷
رودریگو دی‌پائول درباره اینکه کریستیانو رونالدو خودش رو بهترین بازیکن تاریخ میدونه:
این نظر خودشه! برای من، لئو مسی هنره. کریستیانو رونالدو یه ماشین گلزنی فوق‌العاده‌ست. اما شماره ۱۰، هنره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102165" target="_blank">📅 17:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102164">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WagISHqPqPD3xBhl3TjGbm53-h9acJ32rLFhXFHNSa328c3whBqZ2GnSaq7Rnzcne7Sa8vkl9ZgCeuokY7OWXxZj5Z1EwtU-ldNhQCxrJ_v_XvCfetbVntQfSyG4i6Xzo4b5Ut5N0PeXPU3FcMwmGuIABHSpAavpU0O6phUfk5g1Ro4iOIuSsWE-Wx80GZF94U3cR1U2tf4tIeZ30ktJMuuzDsnR1HkknEfcd3oydi7pKTEeHyWLbVaRLEy4onMa_pgpvCy4M1fV-MSw7hXjqxtQrDZ0-EHGlXW0uQVPJgFKPCovxsO3OaQegsAvamVOpBHza8FLG1SF_aVFLRIv1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🤩
محمدمهدی‌محبی بازیکن فصل‌گذشته سپاهان به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102164" target="_blank">📅 17:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102163">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">برنامه کامل فصل جدید لیگ برتر.pdf</div>
  <div class="tg-doc-extra">34.2 KB</div>
</div>
<a href="https://t.me/Futball180TV/102163" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
✔️
🏆
برنامه کامل فصل جدید لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102163" target="_blank">📅 17:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102162">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🔵
برنامه بازی‌های استقلال در نیم‌فصل اول:
🟠
🏘
هفته اول: مس شهر بابک
🤩
✈️
هفته دوم: نساجی
🟡
🏘
هفته سوم: سپاهان
🟠
✈️
هفته چهارم: فولاد
🔴
🏘
هفته پنجم: پرسپولیس
🟢
✈️
هفته ششم: آلومینیوم
🟢
🏘
هفته هفتم: پیکان
🔴
✈️
هفته هشتم: تراکتور
🔵
🏘
هفته نهم: گل گهر
🔵
✈️
هفته دهم: چادرملو
🟢
🏘
هفته یازدهم: شمس آذر
🔵
✈️
هفته دوازدهم: استقلال خوزستان
🟢
✈️
هفته سیزدهم: خیبر
🔴
🏘
هفته چهاردهم: صنعت نفت
🟢
✈️
هفته پانزدهم: ذوب آهن
🟡
🏘
هفته شانزدهم: فجر
⚪️
✈️
هفته هفدهم: ملوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102162" target="_blank">📅 17:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102161">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🔴
📊
حریفان پرسپولیس در نیم فصل اول:
🟣
هفته اول: شمس‌آذر
🔵
هفته دوم: اس‌خوزستان
🔴
هفته سوم: تراکتور
⚪️
هفته چهارم: ملوان
🔵
هفته پنجم: استقلال
🟢
هفته ششم: ذوب‌آهن
🟢
هفته هفتم: خیبر
🔴
هفته هشتم: صنعت نفت
🟠
هفته نهم: مس شهر بابک
🟠
هفته دهم: فولاد
🔴
هفته یازدهم: نساجی
🟡
هفته دوازدهم: فجر
🔴
هفته سیزدهم: پیکان
🔴
هفته چهاردهم: آلومینیوم
🔴
هفته پانزدهم: سپاهان
🔴
هفته شانزدهم: گلگهر
🤩
هفته هفدهم: چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102161" target="_blank">📅 17:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102160">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jh8Lpa7oqDcbDrBHgqnV7YMplTp5pAOR8R18k_GEIIU9hofSC7Km9fwO84c8qiaRFffBroXC38Nci9u9gXB_VGeOvhkvgNKEbR1HngON9JPkdDgu0C2kDTCpMaJwTzYxpsCqmnh-K7O3AvJQdUfDICiLHTkVAxGQYUqQJ0rooZquUzaTXqjOaygrGKU-iKsETIWPGumQNsPC3D3Zn_vwo08wtbZkdiFHhQZG3RZsYmEGT9wET4XP72ZwuCQHuTmxWrrZ9MUHYAwl5XGfBPLCpAJzI7dkpIz0T-L3cBRKqAq2ap-uPC8TivgYYHMk20qw65zLd_7xJqzdOUpgAydSWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
روبرتو مانچینی رسما به عنوان سرمربی تیم ملی ایتالیا انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102160" target="_blank">📅 17:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102159">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHsLAxrHn5An38Oe4DaOZVDrDjmBhPa_2_9wTtQwi4dvSHxQYjiRaZyJB0WRFb8aDTOZ82ayLKxd0lsqU3-E5izDYXo6gXhEQgHc1PVGjOz5lp6EWWqTMFbNZbA2dhkcP6_fgvMLX_f_jNGH8RGphL8MlJf7H487Biwotyjc0qr0ouZ5ZJ83dze2tDyD6pIK9vxkpti7HTit7DC3njIxmYAZmcQa5emHuzZ4MUq5r4x4URKbIy0Lg0-Ju_SOMWhQ8w4aBUrSQjSGGgTSSjpjVxBLkQydGCdCK2FzXk0v_NxfxaidGC9vPHi9k5mahPxLR_HYnVM-PuwaVCs9bkOMgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗓
برنامه هفته‌اول لیگ‌برتر فوتبال ایران
🔵
استقلال - مس‌شهربابک
🔴
پرسپولیس - شمس‌آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102159" target="_blank">📅 17:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102157">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpC2eyjADYddrM7ryjTL_td8U-X2R3McUhiQXIBqwcdjaz1H_P7mvQCnaBKG3n8vzixOOl2jqKrPMnOhtqcrLoGyS0mVn8-BIMBqAYYVHUDQLVkYsiBqgEQeVKUXXN09lU6tmCC3SpfvtqtvLki56qrXXJAgTjsjMr1iamLOtbbULVp2vQvxcyDMw9SXge5Hj2sl1rQeRUv8zm5i5iXrjRR65dg_7EKOLZpr48HqjJZmE3h57vrfTuBdolb1jCbaXQEje8D_dbgfPN7AivMJrgikNtp6dXfn7CTQPosJSXqNnlH9UpQ2nu7jSjC6KmmRolHI2K7VPwaHEhLZ7irdmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c787f96db6.mp4?token=b-OGPmdXa6EiC0afWLDWDW9Og1dCmfXH_drXImH728wTuDmI3QjMpT_JidIX9lOqMVz4-WAdq06Sc3gKqHrqJ1CEwbOsN0ZmQXUIxiRkOdTtv-KmxO_6K_Ydtm5v5OlgWvRVXdKhvkeOa6NR6zhOhqv4jKqyszu8xykKx5bucy99NUf96-lrOzo2nFlRBFzK3mN8NzYoww6M43LWAU3yPOK6GttiHOeNw6UcBPat7Z-mtax7DSHQPfwH_Ejjee8bKQrpiNfp1ddJUIkW0S8ILJSi0KcgCG-9G-TDGBpm3rV7qbGo8c731lkmZoBgLfZkO4TGFP-HF_ifHl5cCKko_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c787f96db6.mp4?token=b-OGPmdXa6EiC0afWLDWDW9Og1dCmfXH_drXImH728wTuDmI3QjMpT_JidIX9lOqMVz4-WAdq06Sc3gKqHrqJ1CEwbOsN0ZmQXUIxiRkOdTtv-KmxO_6K_Ydtm5v5OlgWvRVXdKhvkeOa6NR6zhOhqv4jKqyszu8xykKx5bucy99NUf96-lrOzo2nFlRBFzK3mN8NzYoww6M43LWAU3yPOK6GttiHOeNw6UcBPat7Z-mtax7DSHQPfwH_Ejjee8bKQrpiNfp1ddJUIkW0S8ILJSi0KcgCG-9G-TDGBpm3rV7qbGo8c731lkmZoBgLfZkO4TGFP-HF_ifHl5cCKko_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نیکی نیکول درباره جدایی از لامین یامال گفت:
من قبل از لامین هم توی کار خودم موفق بودم. این لامین بود که اول بهم پیام داد و با وجود اختلاف سنی ازم خواست وارد رابطه بشیم. حتی گفت ازم حمایت مالی میکنه و هفته‌ای ۲۰ هزار دلار بهم میده. همه‌چیز خوب پیش رفت، اما بعد از مدتی دیگه پیام نداد و منو بلاک کرد. الان با مدارکی که دارم، میخوام این موضوع رو از راه قانونی پیگیری کنم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102157" target="_blank">📅 17:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102156">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
⭕️
🔵
🔴
دربی پایتخت در هفته پنجم لیگ‌برتر برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102156" target="_blank">📅 16:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102155">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AziLRxXX4KvVsR734XYAH-JbncdCmmSUGkOSNZ0oWxUJQpAc4hHvwd11oI4nLoXf9W7A3QUUW3K6GDy6ZhB9WrKyu-KkQe2wG2YZrafeD0rDc9zu4bDyNNQ4Mu6npP2esrLOz2xSiXS8LxF99l6-65KIgPO4DcTg7m_v4HsK6HT-L-I3tcWVHeaGhbBNhfPKRSPSIzbwyoizX2jGIZ7ULhcFtdOVBXhjQL3hHWXgU5lh7yN0dR9yaWjynQnfbuVTonNN9w3yYUpBXRPfVswljEK6DCglnOVvoMO4-PaF4ZqsOeYsDHzXAFFo7TuG3UHwidZf7AsOiQLG3ztk1gqM2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از نشریه لکیپ فرانسه: لیورپول با بردلی‌بارکولا به توافق اولیه رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102155" target="_blank">📅 16:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102154">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAnzOx7sjM9kNWj4KZ_1xt79CLYHK-LmqSsi1QxGGTlFObzMdspJ0gUfIshjS923f9qHDdeBXqDoximDMV6swGJ8n3I_Eo9xBd67M7wOmqvb9S4JHumSg8GPvmRA768sGWUagawXTI6HoQYaQQVzpJYZ4XvoWTdST1bBWaoml3631MYYDEsnVyccPH4_Zedw-o7Uve_TtgGm_NAYN29ppRJ2wxRN4iLuieI_r29WAyS5cfTZ0QmXa3xJB1mlGjg_4hRoXDQuCx71Q9ksyFCXh9gBvV9GBiOqT7rwaFkzI2Qh5B96hd6QQlb-5Og-0Vy4wriOXuCgLF6B95fy82sdfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🔵
🔴
دربی پایتخت در هفته پنجم لیگ‌برتر برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102154" target="_blank">📅 16:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102153">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMMOKljzEXnu1Cd30Yy5i49dnQLUbc-ap4IVLxkeeQOjy69emKJGAhCIknQNwGVIMusbwodUKIUtkNvupqnjRYEY7LTnjsWi8VYLN1XbLbKiwalS6FMvWfgRoPS4UTxRcYvJPm8qqcyXzffIzVdrihEMjVdoFLqkFlbTtKUeKKINudvhf44PzAXEzxPIuVwuou6VbNp3tA5DnrfZROOGmxqAHMrBgCDhVYPLFgePGjePuELeZ8H-QfhycuFA9MdIPFhSLGWpJ1NoB3CrVBmPQ_fuk20nJ5qVWa48UM5MnUVSOfusE3ZFnnx8O7jsL3CirshJ3SQjWUx927412oO4FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🤩
محمدمهدی‌محبی بازیکن فصل‌گذشته سپاهان به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102153" target="_blank">📅 16:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102152">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCz0CyVTwFPee909gQZxMlYAY0Ww6yrPsSttsn-EA8H-ceqO22GBqUT5NTjs4Vw-M4Od_mSbpffYBfiBcgyp8XnA4PIfIy89qb1reyAfc4emBkhLU8kZu88Bg34lf_skI3BPz0dfj_tKlUMc2V1NrSTqcWOeuomFGWUcoI-HlbzORRMB7qOOu6cKephgiNtAdIDED64wJb2WQ_tytvv4om5U-gIWoueXG1GiOPejUpdKIIzvgH03uMQFfdQLaslwpkW_NhpdIkVmmOUEkaGy-WK5I9oA9ewM2qk89xH6gh_5cJiYagPmElkXQdBYX4BKxCi1S6XALgnY8XNJ4ZVXCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
#فورییییییییی از رومانو: مانچینی سرمربی تیم ملی ایتالیا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102152" target="_blank">📅 16:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102151">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hqo3g-Kf3QIgQzR0f6ka4ajPZsg69MjoHwvfVQvoANxAftvagmT7vtE-jFJ81aVCf88GbnXiOSf_ppWjLZdAeCBafFkF0bDLA2CbO3F0ZUjh8nKuL7cbh1lE7zw1xKsKSAOxXuhsyphiCbnSMC6uUgupDDAUxi9aA1S7iSrEcF92NwQvBfhFj_cDcnlozxy8-eY6_wtARpZP374zNUi9tpFNXbV9ipDgH59HTHqtTXBVFdi3B2qS7WfafA5PlVBCmqZYL6nDYNH5aHfkwOu4n_wP4TNaQO_FfywxUrjJ4b_0aggLY4DWQQfEE4S5XwbLgAPqCXZWYwDqD4hQx6Fi2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینترنت سیم‌کارتتون زود تموم‌ میشه؟
چون ایرانسل و همراه اول اومدن روی اینترنت بین الملل ضریب 4 اعمال کردن! یعنی شما 1 گیگ استفاده کنی 4 گیگ از حجمت میره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102151" target="_blank">📅 16:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102150">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/881c68dbcf.mp4?token=LKHX-fRFYSW70BOAeeh_BMDseqByE7mcTXHGjDttdlmlX5HeE9pymuMpQLP-6J9abla2U7Vfs4XpJeLnhpWb2ZlNvcEQ9UZV0qpY0cC4vdc47bCKHmqGUOolDbHhxb0fqYcJhCXGi2gHyjXJx_-_dGBNb106g0dMIPLO1aAUSv1KFbvTsbDWJjLIJ2B42PDTftxk7tCe_DICAFlWW8Fhn9H6mL7xeGJOlW40h0uCcpi4FalXX1o5voIKe7VjBz2rTF9yQpTK1uWFEnP6I1VqMvSqXT9j8y7G9l8oefQzMFmRvHpht7ACm_wrwXkZcQnP0-I-KP3AEjno1j_b7Gdv7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/881c68dbcf.mp4?token=LKHX-fRFYSW70BOAeeh_BMDseqByE7mcTXHGjDttdlmlX5HeE9pymuMpQLP-6J9abla2U7Vfs4XpJeLnhpWb2ZlNvcEQ9UZV0qpY0cC4vdc47bCKHmqGUOolDbHhxb0fqYcJhCXGi2gHyjXJx_-_dGBNb106g0dMIPLO1aAUSv1KFbvTsbDWJjLIJ2B42PDTftxk7tCe_DICAFlWW8Fhn9H6mL7xeGJOlW40h0uCcpi4FalXX1o5voIKe7VjBz2rTF9yQpTK1uWFEnP6I1VqMvSqXT9j8y7G9l8oefQzMFmRvHpht7ACm_wrwXkZcQnP0-I-KP3AEjno1j_b7Gdv7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
من بعد از اینکه توی مستر لیگ PES برای دهمین فصل پیاپی بدون باخت قهرمان چمپیونزلیگ شدم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102150" target="_blank">📅 16:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102149">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EM-SCdzbjuyo0vpR-xSUee8xHvm8395l0oRzxYa7_M6vtK1KnS6fe1rxc5vTZieb55MEEITEAvuACEqCYAcOf55_XiegJlt3KpJ_1b501uSAKC_fI3xOq_3GqYAIkfSeQEGCYrceYVHoO-tT5gEl8IhvsE-fWY8kpqCZFx3ORktNAntipKSUHcgUd57vXQrOGTLFLvpbQO5i__OAfnUuPYMxYMLq_oIwIEpqN6TVprQCV5cDRiNZM8TJIWKq83Ose8hx-gsU9aoi1e-obKub-msb0av0WwB2CuZ7xXWGiwTKXGieqgbMkoX9nZBM_NSqlXF-vevr8JdFlBZC_TT8zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🙂
✅
کوکوریا به قول خودش عمل کرد و بالاخره عکس دلافوئنته رو رو بدنش تتو زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102149" target="_blank">📅 15:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102148">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwtPERmXVeu3xSXLDs5RdV7w4Sy9-yhQdWlGESN_MsX4ez3Nv3O2km6PC_PYrMRtfQXwIECYr-2bv4UX9Rq9MVmKzGQx8I_gb1rDTqvLmx1MscsaATlznUNd8XYgdNBjGS4S6yRQNDnATUFBoFsknoJkBX8iwogicyB7avFupVPbu9OjEX4nuCD3mWNFJEZQg0_y__ktBjT40N7GSCcJt44OLyuBXVnsiKzlMR1iEhwNPw3g9h6mAAZwOcqrKcMbJnQvRDUn8yJKed7yYA5yiyv94VUtFo0YSleaAUTEufkZwJbDlyhe_OlCTU6UZf83WcxgSXxi_72tqnLFt1TRpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🔵
رسمی؛ قرارداد یوشکو گواردیول با منچسترسیتی تا 2031 تمدید شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102148" target="_blank">📅 15:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102147">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f242c0afa.mp4?token=AWeFCeq-L8k6QhemPh3YWyWMyOTVwmQRZZYNPvr62jCeSDIiCH7YTy1z0fEQFJAnj9UTmLHc6XrQJmXtqPtg_AWuWcCRdbZ5wyj9PW3Sp8g3BZ5Hq2LFzm5lH_Gff05zKctRt48Z7aiM-SU_XUhZ3dcDr513iBhmmyBbidoJkKM61rYDnTaQZbt8lZtUmTRmim74zlyrIhpx0xkQS7hgQTFINB6pjgDIKM_urXAG3c0LmXfn_0xD9j4q27tPkwSd8rS1AK6fXe3XudKNk4u0x9QTyl_55vSfIvb5V29nHS8ZPC7DsuIdcUxwTe-k-djgJVSHwtnep327JNQL6Vhalg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f242c0afa.mp4?token=AWeFCeq-L8k6QhemPh3YWyWMyOTVwmQRZZYNPvr62jCeSDIiCH7YTy1z0fEQFJAnj9UTmLHc6XrQJmXtqPtg_AWuWcCRdbZ5wyj9PW3Sp8g3BZ5Hq2LFzm5lH_Gff05zKctRt48Z7aiM-SU_XUhZ3dcDr513iBhmmyBbidoJkKM61rYDnTaQZbt8lZtUmTRmim74zlyrIhpx0xkQS7hgQTFINB6pjgDIKM_urXAG3c0LmXfn_0xD9j4q27tPkwSd8rS1AK6fXe3XudKNk4u0x9QTyl_55vSfIvb5V29nHS8ZPC7DsuIdcUxwTe-k-djgJVSHwtnep327JNQL6Vhalg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال به دنبال جذب وینی.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102147" target="_blank">📅 15:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102146">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea2f2fd87.mp4?token=qsCWXk6PcFioTIJYiefRogf_whJBy3YkB-G4SyqN4nujLWGTTIxTPhciJ7fyVUspb3YyWXU6hXPYUPMh4ymcLv8WRWLLO7YAfLu7N1j3T3xf4t-Ox5WOTuMSpe23haLYhS3WPxrwuOG3mvqnr2MTp7lZ3TGRxe5yXYiGOnnUzg0p7vhF8pN1t_9J4n_6JRT_h71qdnWECXLHNMTliKeaTci6VT2fdykz9oKbBmkCdU2uP1FZOgaxC9l_bq35l1Zs-3-bUeS05iCqlQ3_a-K6WiikFBQlxnWFrfvMvuwvu9V7KbowtDS-ZITKkmizTi26Faf7WvdZvrF-4vJqEAgs2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea2f2fd87.mp4?token=qsCWXk6PcFioTIJYiefRogf_whJBy3YkB-G4SyqN4nujLWGTTIxTPhciJ7fyVUspb3YyWXU6hXPYUPMh4ymcLv8WRWLLO7YAfLu7N1j3T3xf4t-Ox5WOTuMSpe23haLYhS3WPxrwuOG3mvqnr2MTp7lZ3TGRxe5yXYiGOnnUzg0p7vhF8pN1t_9J4n_6JRT_h71qdnWECXLHNMTliKeaTci6VT2fdykz9oKbBmkCdU2uP1FZOgaxC9l_bq35l1Zs-3-bUeS05iCqlQ3_a-K6WiikFBQlxnWFrfvMvuwvu9V7KbowtDS-ZITKkmizTi26Faf7WvdZvrF-4vJqEAgs2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇹
اولین‌بازی روبن‌آموریم با آث‌میلان:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102146" target="_blank">📅 15:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102145">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRBOxHdf2oVI1wdV0Sux-spB-lSrbcimWJgQ0OzI3K8Cr2_QbBRGqGg8YROHs_ANEmS5Ub0Puz-AP59YiD_78YCrt-1Eb0MiGgXn648d03mS_zK9Y0R9w0yM6ShIrBL5aKZP48XkjR9jZAFdy6FSETQVIIE_xm7KJPYkMdTd3FtjDIREJOy-4D-xXXCpzSwWCnV-nTcjtD9XiTA4wqXD9OvfBNV0zObFp7C0Cm5jK0ehG3xFtqew01p3kHj6xL5gHi_IU86KgvB2dfmUs_r0-pJOKO-vCAIcngt9dTnGJWHbuGY3o2QHttM5EXfQyNp1cCa5sJk4mGmYmYHpEOjvCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی دوستانه|ترکیب تیم‌فوتبال چلسی مقابل وسترن‌سیدنی استرالیا؛ ساعت ۱۳:۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102145" target="_blank">📅 15:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102143">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MDGliQOG1ll57VVRnR_xd2xh45_4ypliV0DkskJvwdmfl80zHLx89FBHkoTFPm65nlQBLRmJz74QuEqkKvNVXmXJXQHJ_dTLAbfn9rpu2d-Kb8sEf5sthmjFSVqP_R7r16N85rz7eAPQlEN-BNqxEDH2z31AcKXWuLW4qKwfhQzNlwSkXyYfwhGpJlZ4G4AmLDfwV-tYl_X-pFNPlqxVnsMjVDwMGM-1uTJoitNHCBXwJSuN6SmukAMuzeD6M73LOXB3sI2wVZDAbD1JhxlCuiKPq1muZiP5nueF9twpC_UyH3Jn27B8S0NfCPXT2aTHujjANDNjE1voFSgquA1j3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWpKygj19cFcJMbBywwMKNnjxvZGqXQLSISceXFdFtDUCiGwwh8XDAVElALyO-_chGTebOv6wWURBzoqa7jeOlViE0RV84tMRwohvUxqAvlVdKr8SB3P1-lB6jUtoUZovp6FS1YDdeb8Z0xEt9G_D7-ISGU0Qq73zs9bT2vddutNGE0ffzv7p9Oz3FgfD1Ht9fA4tZ5jshxF4mptfZdPu8klLCNyuL6ejTNmjT_423w8w6r5e-jK7Tnjgo7IC3OkQR1rXBcdq4MjeMmsTudVmjTLCwRhXyZhT2lN1qBQ-Hs4JimVvWFwxkHrcyoLDiKOHVcg8B50mWn_uy557Ngaeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
مائورو ایکاردی گفت همسر سابقش در جریان طلاق درخواست کرده بود:
💰
۲۵۰ هزار یورو در ماه برای خودش
💰
۶۵ هزار یورو در ماه برای فرزندانش
💰
۱۰۰ هزار یورو هم به‌عنوان غرامت طلاق
اما قاضی این درخواست‌ها را رد کرد و سیستم قضایی ایتالیا هم درخواست تجدیدنظر را نپذیرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102143" target="_blank">📅 15:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102142">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtJPZFs8aJB6QhF5EG-KcIEsWUzY2dFRFRqBM3npQVlaVWJ3P0E46gm9W4FIWTBtjgwGGff_GZyx7Y1OUGxcOalYJtTFclH8k7t01dMSgPpZD3IMCXnYZRmXfRPwwxEUxsDVDHqTfG7lZegxR_Yybaz9kjoYuMbu-chhMD43ly41Bw_HhowbWbaU0YLtdKAoRGMrHUx5Ax2D-F1-SaFYRGgLkR_wRoasAt7BgDUVAy1t1NlILfeEvpePAkT32evGRmTW8tBGnFKPph919mrz9x_jcQ_NYGkyhY5fmJjzhk3sCgKJDP7hLxE8hNDliFL_FirU0iNTq6qQOrvtLeb5Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
نیکولو شیرا
🚨
🚨
🚨
توافق حاصل شد: کلودیو رانیری، مدیر فنی جدید تیم ملی ایتالیا خواهد بود.
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102142" target="_blank">📅 14:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102141">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5520qZra63r8AkbBFJuaduaPEFsXTof41v8LKRGa55jd3PpRFk_9JR7GKwQsdR_bTGRSk881-2hY4BMWjU0erb2q8c2Q8wcqQ5UDwKCq40DJh4ImRBoasH_fbzut6ksFEcvQ_l_33JvEhtxvM9RytxWaUGjczoU3XOxGgeDBzwUbJ9h6B7QuODzi8PwsonsmRVfIzp_7tyBbASgii0tfBh1aJC9jcYLocofZVEGqBKkD7H-4DjWiRz2N6WqJTop6qlPmlt4bwtK2EPWo6Y7LgGbawiVoSASw-rQSHnCL-aThcEvUpVS47oovldWQ02gyjlHhpwavTsVFVEAVThl0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
#فورییییییییی
از رومانو: مانچینی سرمربی تیم ملی ایتالیا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102141" target="_blank">📅 14:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102140">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922dff29be.mp4?token=FhEdlXu4AYC0wZZk4Loh8wVxU9SrIFSA9ft883A2cf3AvD9_dMc5X7xZ2lwQ2l_qke1kTEV9OCJPrYk3G2vx_gpujpRPfB1_v8q_o1PMopstaGIWddUXwRYEKaB24wgyXHuBYcGCH3votUYicz8wnFlcPjY_8vNH4_kagtslv7eXZ1OXkgFVnq3yUYLWD6NEU-X5F-Hnm6n-74uLAnxMbig4YxoknBtGnNJXjL3rEs-Fh4l6zTzj1AoX2KJ-Oc_jizfc7UZ8Zxn3c9Fb8vZ86ZHDBJ_Fzxe7nuYgY-IL0d0R_TnkpqNT4ifnUNg_fbb-bAUhpS5u63bm1pN3WWDy3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922dff29be.mp4?token=FhEdlXu4AYC0wZZk4Loh8wVxU9SrIFSA9ft883A2cf3AvD9_dMc5X7xZ2lwQ2l_qke1kTEV9OCJPrYk3G2vx_gpujpRPfB1_v8q_o1PMopstaGIWddUXwRYEKaB24wgyXHuBYcGCH3votUYicz8wnFlcPjY_8vNH4_kagtslv7eXZ1OXkgFVnq3yUYLWD6NEU-X5F-Hnm6n-74uLAnxMbig4YxoknBtGnNJXjL3rEs-Fh4l6zTzj1AoX2KJ-Oc_jizfc7UZ8Zxn3c9Fb8vZ86ZHDBJ_Fzxe7nuYgY-IL0d0R_TnkpqNT4ifnUNg_fbb-bAUhpS5u63bm1pN3WWDy3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⭐️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برخی از سوپر‌گل‌های معرکه استیون‌جرارد اسطوره فوتبال انگلیس و لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102140" target="_blank">📅 14:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102139">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👀
▶️
💥
هایلایتی‌از تقابل تماشایی سه‌فصل پیش نیوکاسل و پاری‌سن‌ژرمن در لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102139" target="_blank">📅 14:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102138">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f94a2bbd.mp4?token=VOYNy7E5K0hdK0IOniUBelU-IC7FuXw_LO3IHBnIpFsigkxpr9qc9icf4h6lZvAdJ5hT36AERZZg1z2YU3WxfeVgKoZ-ge6rRcIDGTSfd5nfA0L9pqh4bD8Q4puXXnp9779Ks1nT69trWVSFzRRTePpoC8KYqK4L0fzdM_hO47squYLyAJo8eWjSuVfgay3_v1k73HErYXXqeT9r72SKdY6BHB9UJ8-UsaK-O4vUj1x65aTJYaDIgWxikLj94D_Da5UH7JXkbqopsDghO9AqSZ1uodEUmNCvMj8hBzy-hU9O7YvC2vK6owWRxH9-hvUMj_U95wW4wCJhozQkfCxXuoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f94a2bbd.mp4?token=VOYNy7E5K0hdK0IOniUBelU-IC7FuXw_LO3IHBnIpFsigkxpr9qc9icf4h6lZvAdJ5hT36AERZZg1z2YU3WxfeVgKoZ-ge6rRcIDGTSfd5nfA0L9pqh4bD8Q4puXXnp9779Ks1nT69trWVSFzRRTePpoC8KYqK4L0fzdM_hO47squYLyAJo8eWjSuVfgay3_v1k73HErYXXqeT9r72SKdY6BHB9UJ8-UsaK-O4vUj1x65aTJYaDIgWxikLj94D_Da5UH7JXkbqopsDghO9AqSZ1uodEUmNCvMj8hBzy-hU9O7YvC2vK6owWRxH9-hvUMj_U95wW4wCJhozQkfCxXuoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
امیرحسین صادقی: از وزیر انتقاد کردم، به دادسرا احضار شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102138" target="_blank">📅 14:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102137">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FJH6nCvZTxmQQX2GF2WsP7SCLBQ4_RCuW4q5WQs0ZXqC8kHJOMej7gq4Ht-Iv1Lyu2r3RQxbt6DFYxledbiblXDOIPUdeBVG9negfVH4WQCw32ZZ5RBJN1Hck_Ljb1FD7PBKd3rAQlo2DqviHFKMZeohm6AMnJgTpIHAxaV0NyL7lqC8owSAAJa9WQK-mhHSFCiQ43Y01PDoXu4Ll0T_VEnfiTg9cUg7JNALXs9VjknvNrV2vRdZSoOjJiVrjDADjA3XIQKEtj4_xeOmJX68q-b0nZD6WAwmYKa-Bs__j-5sg6-maF4vX_S2fc5h-ayAUkhLpzg-I7vRnVas1IcKxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از دیوید اورنشتین: وولتماده مهاجم نیوکاسل مورد توجه بارسا قرار گرفته و به صورت قرضی در دسترس کاتالان‌هاست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102137" target="_blank">📅 13:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102136">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔥
کنترل‌‌توپ‌های ستارگان که منجر به گلزنی میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102136" target="_blank">📅 13:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102135">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P96FqHhslYwE3vYDP1o022b6vWWxxBh-ICACfysOSLqI2KhQsyBEQAai1iFFGuqhOOR90rQL0wzzwIDWvWYh9JKJg-_rDG_8A3yzREz1lhSOjo327P57-slYvEfyam9EoQUf2FrRc40Cu612mwOGvWx2ZYah95fm0Hte8AWBuSTqVC9vNeaCRnPRCQfNXbwv7S46wlFhO_oik5icECbnfTyhd26UC8Ot0omrFMdYXQbsz-1k5b6oSkifDsY9K0JOzYag59f9mLMiBgCLlYAsaf6dWhxCakmRNf8hdxMw2uzdM8arL9zs_kLTolN5NO7CraP5T0THD8sCGhTuFmplQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
باشگاه بورنموث علاقه‌ای به فورش جونیور کروپی به بارسلونا ندارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102135" target="_blank">📅 13:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102134">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/792acb1bf3.mp4?token=HU5xeRkFhQJYTScjssOMLWveWDXYSXY6iFQUgXBhlmi-i3Jn_0NaaEys_EOBknkCcyDD7HqbMg_K4QNLei_V6p5D0pCABEMyCL78BC_NOhRj1SokEX1JQSyBXpSX-FU_8DbKU_lLXo1VsHri2A4dfubtVw1yobjA4QbUjEafUkjRRJsfzLUV6l7455bQOUn6pu2zJUMnsXUkS1uAbb64n6WPqxqU3Kl8Dr79TvZsyl84mlj0CLWBhrkWCTIj2zlwffBvbhoJRwu7t8vCCvk-rTSH8CbXkkwq_zG1RBVxoF6ZKNzDSnHyDOk0BAdIOfKVx4T-mCsqkSqL47bdJ9b_eoSmeKgsA32CkB0lYLIFUR5rUGqRqrI6avV06bwBvEL3LlKRTov-rjwDMkNgn8v-l9sakxiULxFsjW_FbojVE5KCdshsroGqNzv1BzPJyqdROcvJj5X25anvooF_uPQP2eKVIWU2IrhDHG3-nJUwwEMeb4hzaIb5IGhabtXGOCmyIXXOe-NP470lEVfbd_a5WjhrUZkRSKqLyziHL_J4yYzK9qmdUXCG_ODE0Mdd5RCrEPv8tU87wLVxlG-9h6C0pOocUR-JjFhsXd6VUou1KGd8NnqprGfHg_CrE5YTxD7ybsOXQK0jCqu-2eE0tSBqIF1sbnxIt59eEwAVNF1gXeE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/792acb1bf3.mp4?token=HU5xeRkFhQJYTScjssOMLWveWDXYSXY6iFQUgXBhlmi-i3Jn_0NaaEys_EOBknkCcyDD7HqbMg_K4QNLei_V6p5D0pCABEMyCL78BC_NOhRj1SokEX1JQSyBXpSX-FU_8DbKU_lLXo1VsHri2A4dfubtVw1yobjA4QbUjEafUkjRRJsfzLUV6l7455bQOUn6pu2zJUMnsXUkS1uAbb64n6WPqxqU3Kl8Dr79TvZsyl84mlj0CLWBhrkWCTIj2zlwffBvbhoJRwu7t8vCCvk-rTSH8CbXkkwq_zG1RBVxoF6ZKNzDSnHyDOk0BAdIOfKVx4T-mCsqkSqL47bdJ9b_eoSmeKgsA32CkB0lYLIFUR5rUGqRqrI6avV06bwBvEL3LlKRTov-rjwDMkNgn8v-l9sakxiULxFsjW_FbojVE5KCdshsroGqNzv1BzPJyqdROcvJj5X25anvooF_uPQP2eKVIWU2IrhDHG3-nJUwwEMeb4hzaIb5IGhabtXGOCmyIXXOe-NP470lEVfbd_a5WjhrUZkRSKqLyziHL_J4yYzK9qmdUXCG_ODE0Mdd5RCrEPv8tU87wLVxlG-9h6C0pOocUR-JjFhsXd6VUou1KGd8NnqprGfHg_CrE5YTxD7ybsOXQK0jCqu-2eE0tSBqIF1sbnxIt59eEwAVNF1gXeE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیر حسین صادقی: قلعه‌نویی هم مثل علی دایی جر زن است؛ کاش آن حرف را نمی زد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102134" target="_blank">📅 13:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102133">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9afeb8a4ca.mp4?token=gVvObf_HppcT2NG2bakVAf78TwpWkytTTRcUzYZxPO055xnSHJ9T_tZq1qhV4XqjelwMxFTtilGDiLdVib3_3khI8BJpkXMNpyl663t8lanz9uKxG9WFnkNbFAtkyu30WCr22Hy0bYJ4y7IMJk4nB7OmleIOBIo0VEpoq_RL8oBnkKxl6r241PGRQfRzQrXZRQtgxJahXdyXsO1pH1wFDzUp2tBAuypjSQNeKWCpSWfuFEAPXPgKPG5FHbGc4BhzHHxU6JCUlIMQ84PjgnxzdMRsQleVciNY3uBmsj5pzWVzTtcmeNUvqWYDUfXczgcjntiTSjr4MxZV4S-qjCROsrUH6YYQUQq1tho04elp8IzOt5EYF7FQj9sPdrwNXttx2ZZIDSDKk-T71YJhCNX7cg0mOeJ5UAu1AQFoDqRlf5Teq-7ELHv24ax31JzOntqTmCPSb568qo2unNpcnraGSdJhMWeBBYSqDtHecVI3rH9iU_TCiWEJ2CgsuFwK1xcsczoNkxteV4kYK24ksuT-NPGiVlP2TvY5IjfmYSiSHrsKcfuaX9Od-zzIk0DmfUewiaY1iCn-GENRRqEKFZhDFc0C0No4a9ER-KtK-fDI1J-9Peaq8-ZmD-qX_jBl97hYApconvPd1DK6UwTPMJuzNMdCeGo8O5NYV5d5soVC5Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9afeb8a4ca.mp4?token=gVvObf_HppcT2NG2bakVAf78TwpWkytTTRcUzYZxPO055xnSHJ9T_tZq1qhV4XqjelwMxFTtilGDiLdVib3_3khI8BJpkXMNpyl663t8lanz9uKxG9WFnkNbFAtkyu30WCr22Hy0bYJ4y7IMJk4nB7OmleIOBIo0VEpoq_RL8oBnkKxl6r241PGRQfRzQrXZRQtgxJahXdyXsO1pH1wFDzUp2tBAuypjSQNeKWCpSWfuFEAPXPgKPG5FHbGc4BhzHHxU6JCUlIMQ84PjgnxzdMRsQleVciNY3uBmsj5pzWVzTtcmeNUvqWYDUfXczgcjntiTSjr4MxZV4S-qjCROsrUH6YYQUQq1tho04elp8IzOt5EYF7FQj9sPdrwNXttx2ZZIDSDKk-T71YJhCNX7cg0mOeJ5UAu1AQFoDqRlf5Teq-7ELHv24ax31JzOntqTmCPSb568qo2unNpcnraGSdJhMWeBBYSqDtHecVI3rH9iU_TCiWEJ2CgsuFwK1xcsczoNkxteV4kYK24ksuT-NPGiVlP2TvY5IjfmYSiSHrsKcfuaX9Od-zzIk0DmfUewiaY1iCn-GENRRqEKFZhDFc0C0No4a9ER-KtK-fDI1J-9Peaq8-ZmD-qX_jBl97hYApconvPd1DK6UwTPMJuzNMdCeGo8O5NYV5d5soVC5Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🔥
چند ضربه کاشته تمرین‌شده و تماشایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102133" target="_blank">📅 13:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102132">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQ3fC46uQWvuNMu8b4NCxbpX7uVzQMN-wfgT9nfBbwy4BKRF6Ho665z_DNQeL1T1rZyfuVdp2hX5m53LpMLIbML0J_2a0BsnZIyQTFuor_bSpWBHi0ZCAWROU1ehyva2R_66cCCKsm8QdeeF5IG93H4HTt6J0ANCKMl7MIt4YVoIQ5K28bHc621UGLR1z-zv43Evw5D8ksDZlvBOpYmPaYeDl262YJzQqTZBugI_-nxZoa-ZmMFaWD4cxvE5glUtkYedMJu3-wx-up7C-p8mZhPJC0_qNjGosDqnnjeNA48MV1E6eclkrytHl7PiJb_KKdFDL2GA7uv82DDestWaBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دنی ولبک خرید احتمالی چلسی در فصل گذشته پرمیر لیگ بیشتر از خریدهای جنجالی تیمای بزرگ گل زده!
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دنی ولبک: 13 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بنجامین ششکو: 11 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هوگو اکیتیکه: 11 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برایان امبوئمو: 11 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتئوس کونیا: 10 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102132" target="_blank">📅 12:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102131">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
✔️
#رسمیییییی؛ زین‌الدین زیدان تا سال ۲۰۳۰ سرمربی تیم‌ملی فرانسه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102131" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102130">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsfHTy0B7qu8EUyZGGvWF5WukWIvMzk4DAmGoSpjK4mgw7PzBKnTNSmphOZqllPXK8YCIn3L90XFNf1S9g2BxYYdq5u9dYOjDAqvXWe7KqrpdFwPRC9uKOxbm9qMB_mB7LCKpeKDd4pjnWaXTJ8wJ4hmUNNhi-ygH8u0l64eR5b_GSazeYVBs6nUIRwRa0b_GQ6tG7w-vXgezLtnV9evNtboMvA6dmZRPq7fWGJ61s8qfY5lMWAoxvUDsXahYEWBIR5qs2EmSrGZCnQlwQ0P8dqVY3n1-brq9TtSf_tCbnKwQ9Sfo9tGN5tSMQkBYKKHy6ebV3uqzDVvRjVyiqqS0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
#رسمیییییی
؛ زین‌الدین زیدان تا سال ۲۰۳۰ سرمربی تیم‌ملی فرانسه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102130" target="_blank">📅 12:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102129">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/496ccbf92e.mp4?token=k7dS77GuNwl40lFlIVJ2qU3ucHEt_XZUqUc_T5c8BtojU4b_1IIOKP-dHDtFPpeZ9lfeXSems4FB7MuTX2hblybPPR0EQdcgzZ3QVDF9KsMT4wkqTH3BN261yz8_9jc1OuSujgOxEu-CczyFCFi_s644qPLrs5ttEogB14fZWWFbPp7tjSTxIrWW9A-tUKPpWOd7CJB8fPA-BCEOCkHqi3zMgu-R3A-IVUUqSlJtJgL81SVAYtxnk9RS7o2pWqlAo04CQUD9mwyTAhpZ2xBulmrAcwwBRU1VzqlhAWPVc70ZzpwmmIbBjCtokK35GBhWNotk1GoHvHXaAK0-w8J8x4Pwab86OdhCe7lmdH1XDQEb5KXkH-ztAhI8XivBEu3TbQffSMI9I_a7nUJCb44Ixbgg7kns7QhXbjKtw76VHLk3d9KXzGuCAVgHOBzUDSPSBoFyieu_h8mB9kP5Sk3pfRrYTvWmNcr1LkehvVHy3Von-XEhIEtuiMU1OCuFwIggMuB5N07aNeVyWdTR_CMewCY2yp8aziC_SM-1zD9vrnc8Ps4tu1unYMDLNrXyvJ6Vf1jGYJFa_3Df-ti_yZb670lIyzP6omyY4E7gwrUyv3uY7TPmoPGBUaQD6V_mirxy2bzn8VbLULvaQZqoTAuwyUhjJHOmSdxT-BMS1wlBAcI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/496ccbf92e.mp4?token=k7dS77GuNwl40lFlIVJ2qU3ucHEt_XZUqUc_T5c8BtojU4b_1IIOKP-dHDtFPpeZ9lfeXSems4FB7MuTX2hblybPPR0EQdcgzZ3QVDF9KsMT4wkqTH3BN261yz8_9jc1OuSujgOxEu-CczyFCFi_s644qPLrs5ttEogB14fZWWFbPp7tjSTxIrWW9A-tUKPpWOd7CJB8fPA-BCEOCkHqi3zMgu-R3A-IVUUqSlJtJgL81SVAYtxnk9RS7o2pWqlAo04CQUD9mwyTAhpZ2xBulmrAcwwBRU1VzqlhAWPVc70ZzpwmmIbBjCtokK35GBhWNotk1GoHvHXaAK0-w8J8x4Pwab86OdhCe7lmdH1XDQEb5KXkH-ztAhI8XivBEu3TbQffSMI9I_a7nUJCb44Ixbgg7kns7QhXbjKtw76VHLk3d9KXzGuCAVgHOBzUDSPSBoFyieu_h8mB9kP5Sk3pfRrYTvWmNcr1LkehvVHy3Von-XEhIEtuiMU1OCuFwIggMuB5N07aNeVyWdTR_CMewCY2yp8aziC_SM-1zD9vrnc8Ps4tu1unYMDLNrXyvJ6Vf1jGYJFa_3Df-ti_yZb670lIyzP6omyY4E7gwrUyv3uY7TPmoPGBUaQD6V_mirxy2bzn8VbLULvaQZqoTAuwyUhjJHOmSdxT-BMS1wlBAcI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🎙
رئیس مرکز ورزش و تربیت بدنی دانشگاه ازاد: علیرضا بیرانوند سال پیش فارغ‌التحصیل شده و الان دانشجوی دکتری نیست
+سربازی در کمین است؟
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102129" target="_blank">📅 12:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102128">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpkHL8VJ0WrhHOBthCVmHhJazYuf0uSIykgaLsDw5oKBXN5ntRXiuSsg1JgOs1tzpAUrmzqheFsaOI2UVvhXCcjnpyWVs3sQMDQ36xx2ETg50sQ6Tbrk6rpVnI05CST00pAFvc2wYdOyWb8hojvjE0yxIvuKzSZXI7aKt78sXlll7Ep2Oa_AHnaWcthKD324iFQ-MB5RhQL87yrbiVn8EC5GHQ-wlfgbyXo6OnCcAuxxdILkKTW-JF-MxGtlPp1gTTHgsx35yBoA26PJpt96oTVSkDrDI6GSTXK-R5mMVO23_tySi3YpAmxY0tAqTz3i26ISd0_O4G6qafokP8JsAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی دوستانه|ترکیب تیم‌فوتبال چلسی مقابل وسترن‌سیدنی استرالیا؛ ساعت ۱۳:۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102128" target="_blank">📅 12:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102127">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04499b20cd.mp4?token=IIQ56gPtcri-6BK9-OtI0Vx1klsCJ_MnI1HEpMmrOrDHRSMQxrs9h_ubPdD8iSBlbCv-xqOtq18sfPzZmrVZDveVA4sdKvEXZTzvbSO34Mhhs7ZXtTF3nbwhlGfzjrbI4eqMhHCBHC-DseFPgxnf7VMkXb5kFRtrARcA0RJuC1F6sWayZTji1-bMZQ3g-LH4kQUJikKQC61Tv6ll8t-TG-5-Aa-5xuYsYVlUOSdIrkb2lzR2mCCPGxNVUZwz7F2YEVZEvAywaj_L9ygvTpFw5WD1QYnQRnN5t_EQA0DZ9GCSeFX7phe4BTNb3FWgMRnZD4-H15rwkLY3ycvkYkNWFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04499b20cd.mp4?token=IIQ56gPtcri-6BK9-OtI0Vx1klsCJ_MnI1HEpMmrOrDHRSMQxrs9h_ubPdD8iSBlbCv-xqOtq18sfPzZmrVZDveVA4sdKvEXZTzvbSO34Mhhs7ZXtTF3nbwhlGfzjrbI4eqMhHCBHC-DseFPgxnf7VMkXb5kFRtrARcA0RJuC1F6sWayZTji1-bMZQ3g-LH4kQUJikKQC61Tv6ll8t-TG-5-Aa-5xuYsYVlUOSdIrkb2lzR2mCCPGxNVUZwz7F2YEVZEvAywaj_L9ygvTpFw5WD1QYnQRnN5t_EQA0DZ9GCSeFX7phe4BTNb3FWgMRnZD4-H15rwkLY3ycvkYkNWFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
خلاصه که نگاه کردن زیاد آخر و عاقبت نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102127" target="_blank">📅 12:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102126">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxbepIyl6uiWkE-p1ZhE4uZ5zEesDUOqjT9S1xRinL4RY2m6ntw7-u4_kXURbaTSM0ZSp5Iv7yRldPGPv0TQFEJcHYh3bUBEjESE8u8FZPkDjq1KNXZaAoUbNFFv4ZjVLyWmMR2ZJkG07iGEpVQI9v-I12BrW_XS6u42Kky9kkFVtUokEd8LxCt5TMcuOajU-KPYbv1RnMAX1GwGU_dY8RVvwIAf0Zuv7_CLlEBxoZNKgKGQVG_KAggk91j0pCyf7yOs-2lY7sEUgQLxOR6Opksh_O3tTSCNtWaUnAbxGVKlZGmzG97W_CGiQAc9LN_7SSgn7-VKZFl0-fsxaRLGzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
‼️
آپدیت جدید و عجیب اینستاگرام که شدیدا مخصوص ایرانی‌هاست..
شما میتونین در قسمت «یادبود» اینستاگرام یک نفر رو مشخص کنین که بتونه بعد مرگتون در پیجتون فعالیت کنه، و توی بیوی پیجتون هم میزنه «صفحه یادبود»..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102126" target="_blank">📅 12:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102125">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6VqM3XLeQHyAyYTZ5Vl3QnI7C6tTlyCn1ftrFBbVEwFf4AKwUzCb-_oaVNqefhgfeXoHoaxBqOAULWYadxf76jBnqNch2MoPKJB6ybj7XQSn5CYJqqVlnWRe2hlbHXIA1-4PsC8_hGCLJKUwqYqpK_oGPUZdA_3HdlnDENTUQ7z_tht3u1nDPhyPQh2PJR9LLcjgCwoNfgOOZRVms5UGYHgGZ_KgmXsVFb7rDTwXcO02NfMrcRn75etSyh2e10uUPSq2SGLC0LnomR6PfJNdEALXza6XnvfgGMTf84PFhN3bmAAbifAEEb2msakXxbK7WrMLjXyQmNf9NLuVHBrxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماتون بریزه که یامال تا الان که 19 سالش شده با همه اینا یه دور تو رابطه بوده
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102125" target="_blank">📅 11:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102124">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/07378b8b26.mp4?token=f2ruJYaArl-__EX7-S714yYrbe4U_FDLIAfCyFzcIwAJV_OplN52-aUjel7Y3wgZieAkM-RB0AzjQp4eqWPLQU7M1G6IZLHSw-l9VTHkiOf-h09yYa6vfuPLR4UymEXbemRXW6aN7OWdwMsX86KIorLUnXmojALf8AixZoCn113HnbZmLXXk_2-JjhQFRDZr8IiUxRXfL0XCYufotW8IguY-bMWWactSbUwp2-7V6R-o8pmmY3TSLOrEvHZR10k3IK3GmnQzLJKwiC83a2dayBMtrZOqTHr8tb5IuhtC1QrapUlJR7LDcglF-S1zMRPhqrAEqi3L4-oM7S5us4hxgg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/07378b8b26.mp4?token=f2ruJYaArl-__EX7-S714yYrbe4U_FDLIAfCyFzcIwAJV_OplN52-aUjel7Y3wgZieAkM-RB0AzjQp4eqWPLQU7M1G6IZLHSw-l9VTHkiOf-h09yYa6vfuPLR4UymEXbemRXW6aN7OWdwMsX86KIorLUnXmojALf8AixZoCn113HnbZmLXXk_2-JjhQFRDZr8IiUxRXfL0XCYufotW8IguY-bMWWactSbUwp2-7V6R-o8pmmY3TSLOrEvHZR10k3IK3GmnQzLJKwiC83a2dayBMtrZOqTHr8tb5IuhtC1QrapUlJR7LDcglF-S1zMRPhqrAEqi3L4-oM7S5us4hxgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو با کیلومتر ها اختلاف آندرریتد ترین ویدیو سم تاریخ فوتبال ایرانه
دعوای علیرضا منصوریان و فیروز کریمی در یک قاب ، منصوریان میگه فیروز کریمی داره بهم فحش میده یهو فیروز کریمی از اون طرف داد میزنه :«گه میخوره»
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102124" target="_blank">📅 11:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102123">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeee92fd86.mp4?token=qeyLsPtpswkr_hgcMHkaWF4agUisOwrTOu4TyvkUkGyI7IklICPTmyZy2YdIyYKad6ROTIILxfF6ZOIfCWw9s9w_ArPkxjWVXk-ir1tl68WFIMoOpQjCrgKv0ePVY4WwEzQmUC3pn0BeZ7wko-3FuU06IjKamEJGEL59XOvbQPsjT9ctqBH0vK438pTahBMeMaUGZ6Bgw7GDNKuCaHci_chA99ipb1K9OIvbATQsEVx1e-66EZ5AkFEU2d3Nxh6vDq_Svtt6thQPjSz5lPabOlJo7JzgfvRH3fVAw3gdcwtd7G9ZapmZy1fPMe9r-NMzGsnos4LiJoLj6bVASSeb1Aurmv3yipmmI6f8M8YW2mR5ixlMLtK2TzVcXARQAe0mnK_eDzg42RHtYEBlrkbNF3wje8seXFwQx15v3_xVQlmeZz8FvMtJI9Y61V9vYEpkEHrVuVnOo7sbCOLjm3nUM8hv0r-mXRCMf1wZhs9mSKK0YHzq3MIpENsdNYfUnOhEpOT7g09Fny2k7Hg105X3rCUxt8eowUkZO6JBfST3PGHIEplarRrg7mGPNR66sbGTjjhyk4NE8xZJxxp9zCmLLjBnXZ-cGux3FCU190xReLB22I7pcJCJNCnhu8nrYpPqQky3tVKeC63nh9wMeEZQv2tL1HYMn4tmg8BVOqCisyo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeee92fd86.mp4?token=qeyLsPtpswkr_hgcMHkaWF4agUisOwrTOu4TyvkUkGyI7IklICPTmyZy2YdIyYKad6ROTIILxfF6ZOIfCWw9s9w_ArPkxjWVXk-ir1tl68WFIMoOpQjCrgKv0ePVY4WwEzQmUC3pn0BeZ7wko-3FuU06IjKamEJGEL59XOvbQPsjT9ctqBH0vK438pTahBMeMaUGZ6Bgw7GDNKuCaHci_chA99ipb1K9OIvbATQsEVx1e-66EZ5AkFEU2d3Nxh6vDq_Svtt6thQPjSz5lPabOlJo7JzgfvRH3fVAw3gdcwtd7G9ZapmZy1fPMe9r-NMzGsnos4LiJoLj6bVASSeb1Aurmv3yipmmI6f8M8YW2mR5ixlMLtK2TzVcXARQAe0mnK_eDzg42RHtYEBlrkbNF3wje8seXFwQx15v3_xVQlmeZz8FvMtJI9Y61V9vYEpkEHrVuVnOo7sbCOLjm3nUM8hv0r-mXRCMf1wZhs9mSKK0YHzq3MIpENsdNYfUnOhEpOT7g09Fny2k7Hg105X3rCUxt8eowUkZO6JBfST3PGHIEplarRrg7mGPNR66sbGTjjhyk4NE8xZJxxp9zCmLLjBnXZ-cGux3FCU190xReLB22I7pcJCJNCnhu8nrYpPqQky3tVKeC63nh9wMeEZQv2tL1HYMn4tmg8BVOqCisyo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
نوستالژی خاطره‌انگیز از دربی دلامادونینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102123" target="_blank">📅 11:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102122">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aafdb5637.mp4?token=MiL-SRgYRyaNA8c0w_LdD1y08nOAmRVgXL8T_jXcAq35UE2ddRQCPEBQ7RhmiMBdt69obsFgkDqIXm_C76bQLCcUFuqv2t4iXPUmg1_AXMYfhRDw_QsuRMmMVCOpZQJNfm5VgYfgzE1K7UivZBaVDIuUks55TNaB9EgFwAQG3wgWFbnbcuSvsXShjpDnLfmWn0sUvGjXXLJ6yac4xTYKZL2Xvzr_1f1TQY3Maw3FynFEqFLj8QMXb8S7UX-i-Ympa4AkM8ZN3PoqMY3wR03p7B6j78rRF3Vpu7dCVK0JnyW3aLGjAiUa_Xs8tWI6NiUL6RytvEW2HRDTKrT86rBc6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aafdb5637.mp4?token=MiL-SRgYRyaNA8c0w_LdD1y08nOAmRVgXL8T_jXcAq35UE2ddRQCPEBQ7RhmiMBdt69obsFgkDqIXm_C76bQLCcUFuqv2t4iXPUmg1_AXMYfhRDw_QsuRMmMVCOpZQJNfm5VgYfgzE1K7UivZBaVDIuUks55TNaB9EgFwAQG3wgWFbnbcuSvsXShjpDnLfmWn0sUvGjXXLJ6yac4xTYKZL2Xvzr_1f1TQY3Maw3FynFEqFLj8QMXb8S7UX-i-Ympa4AkM8ZN3PoqMY3wR03p7B6j78rRF3Vpu7dCVK0JnyW3aLGjAiUa_Xs8tWI6NiUL6RytvEW2HRDTKrT86rBc6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
۱۰ گل خوشکل زده شده از مدافعین فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102122" target="_blank">📅 11:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102121">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7bc32139.mp4?token=q1BMDxPEKDVvFjePRXxEcnKuGn1l8FkVAu6aosH2TZhcvd3jgYSS61BqZZFzuXN2ED50bpg6TzdHqA6Af_-tK4xE6woxz0nR-Uuns8qQd_GXvL5e6zib7tN6OUfNFI300MoDEjb1_IP6Qs-qXnzaet48M9xM8KKKK0sn8VX0D8M0dk8RXsu8ki-V5CQ9Hd1mNNE44purxNKE0n1u-w4EnXfa-s_UdgzCehmPf6zrCkInks95h_l-_tebVbeeYNni5p-oeKTzpYfpGxrz8mAbskYipbOLmKol0i8xWW2DLl--m4Fx1RqLW0oA7D-oMNX12Fv8BNxM9p3wa6fv7LKQiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7bc32139.mp4?token=q1BMDxPEKDVvFjePRXxEcnKuGn1l8FkVAu6aosH2TZhcvd3jgYSS61BqZZFzuXN2ED50bpg6TzdHqA6Af_-tK4xE6woxz0nR-Uuns8qQd_GXvL5e6zib7tN6OUfNFI300MoDEjb1_IP6Qs-qXnzaet48M9xM8KKKK0sn8VX0D8M0dk8RXsu8ki-V5CQ9Hd1mNNE44purxNKE0n1u-w4EnXfa-s_UdgzCehmPf6zrCkInks95h_l-_tebVbeeYNni5p-oeKTzpYfpGxrz8mAbskYipbOLmKol0i8xWW2DLl--m4Fx1RqLW0oA7D-oMNX12Fv8BNxM9p3wa6fv7LKQiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
خوشحالی‌گل‌های عجیب در لیگ‌های‌فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102121" target="_blank">📅 10:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102120">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">▶️
رضا نوروزی؛ یک فصل طوفانی، یک عمر سکوت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102120" target="_blank">📅 10:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102119">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQpcWhWvzBTwsdNfZb2sSlkz5Y6twb-C0E3CTbXuM1-iS2hVZSY1jWb-UCwlmftkspLqwW9UNsGebcJXt7fIxy8xkEdwtDv2J5o3tGWv6fYwQG1tPfjqTZpQxW7wr4GJowE8dQRN6EREPr0H0LFt7Dlw2_c4jSZN0yoOFl2fW1KKZTc3ufZtYLHazXhu-2veVu_7kE1BMg2zaa9uFqHQA4HAsiQgkvTjlKcgOesO2YLsxk2On8RP4M4d8l5Z8f9Fjsqh3CEH5Fuj71jmKkqGb0WAjZb5t6zbSbXZeuREt-cnBbQQRWTFeeEEJtu45mgdUF6WomhahN3l59qnzFZ04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
😟
اینتر میلان به توافقی با تاتنهام برای جذب کریستین رومرو به مبلغ تقریبی 40 میلیون یورو رسیده است.
✅
⭕️
🇪🇸
اما این بازیکن منتظر بارسلونا است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102119" target="_blank">📅 10:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102118">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2348e726.mp4?token=ANg9S9zDhez23qI_qzgRQA7qJZbCZEtG1FAlskP_aaAj7ghnNN3nfKIbY0AQ5zN3Lpfan_e1_fX807CoimxSDerWF0QtEIjtx5Rou0DpZlFdHAvWR2VWWKGi-yHPKjacws1h-_HcHEPTI3qRy_jhfXKFV5auwfLQ6hhcOkTg4dbDW02M6kCHPDfAqO9a9UN7hRqEIUE56E8dhOrQjKfs9bRDcC3kb37s_Fs6V0eqSe5yRaq07p7u5j84i0h0y6SzByLRibClQhzv4drYKIY5pGLXmaz5eBDWlxCSvhIfbOixmpaJEzeaRq_G0wKRQGyGai7N9kckUQArvzdj8lUhQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2348e726.mp4?token=ANg9S9zDhez23qI_qzgRQA7qJZbCZEtG1FAlskP_aaAj7ghnNN3nfKIbY0AQ5zN3Lpfan_e1_fX807CoimxSDerWF0QtEIjtx5Rou0DpZlFdHAvWR2VWWKGi-yHPKjacws1h-_HcHEPTI3qRy_jhfXKFV5auwfLQ6hhcOkTg4dbDW02M6kCHPDfAqO9a9UN7hRqEIUE56E8dhOrQjKfs9bRDcC3kb37s_Fs6V0eqSe5yRaq07p7u5j84i0h0y6SzByLRibClQhzv4drYKIY5pGLXmaz5eBDWlxCSvhIfbOixmpaJEzeaRq_G0wKRQGyGai7N9kckUQArvzdj8lUhQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یادی‌کنیم از تقابل نوستالژی نیمار و ریورپلاته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102118" target="_blank">📅 10:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102117">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3115e0e757.mp4?token=PHOE0QZdijs185IylCmcLdF8Kj9WyRrjaoINd30_mFdFZskJfO5OKr8DY4U_ACKxyKLyLHPdlfYx-wn2WD7BFOSz2UX49GAhEnzoDeeGlskAQ6DTw7PA4RKCsB0H3208WZieBdeRVYBnIEzsN9efwECQOV1xiNVX-CBNS7rN5q9INuUJxeFwo0WhpIzmsfr6WIRLg9B8CjFry6AX7s7lRMG8xC8udtHjQKPHuLvg09TlrnofkJt1QSVBEw9cpqDNZzfAdvkgP8gyyUs9OIdqVxqoyfhw1GbdixBJFMHhTzHwGzbrH0n1arKkWawWgblwhthsNrs6r7lRyFAa11VnNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3115e0e757.mp4?token=PHOE0QZdijs185IylCmcLdF8Kj9WyRrjaoINd30_mFdFZskJfO5OKr8DY4U_ACKxyKLyLHPdlfYx-wn2WD7BFOSz2UX49GAhEnzoDeeGlskAQ6DTw7PA4RKCsB0H3208WZieBdeRVYBnIEzsN9efwECQOV1xiNVX-CBNS7rN5q9INuUJxeFwo0WhpIzmsfr6WIRLg9B8CjFry6AX7s7lRMG8xC8udtHjQKPHuLvg09TlrnofkJt1QSVBEw9cpqDNZzfAdvkgP8gyyUs9OIdqVxqoyfhw1GbdixBJFMHhTzHwGzbrH0n1arKkWawWgblwhthsNrs6r7lRyFAa11VnNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
▶️
این فیلم مربوط به سال ۱۸۹۴ هست و رنگی و اصلاح شده. حتما ببینید واقعا جالبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102117" target="_blank">📅 09:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102116">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52dd0bc973.mp4?token=QjyagBubzpyPF3k_9dcNz6xjb0nqVkc__5VHWI91vW51vOkVxCAbAkXYqigmmKLFObk1Rtv0J-cmqoQ8H5rev363nEVYuaxlr6qGGQTkjlPBpKstTrbecxwv9WLBETlV5Y1lMbm_7nzd6yEoqpdb3HPcnV-fsx9ld7lC7ESf_QFTDa3fSFHm2p5aGTUxnlttJzEZ3UBbJ8Bm1mOlOGf4nqrxS50r_qcsFn55ynw8_uJHqL9UJJmOYG-zjnpIQM1eYsqCuWJYPpfvoGPmLO6kReTx0Q5Qpjb40h01WWmL4nbcxHWhHFEk10iwif5nSEQG3hPebNcNmsUQSim_MQbFeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52dd0bc973.mp4?token=QjyagBubzpyPF3k_9dcNz6xjb0nqVkc__5VHWI91vW51vOkVxCAbAkXYqigmmKLFObk1Rtv0J-cmqoQ8H5rev363nEVYuaxlr6qGGQTkjlPBpKstTrbecxwv9WLBETlV5Y1lMbm_7nzd6yEoqpdb3HPcnV-fsx9ld7lC7ESf_QFTDa3fSFHm2p5aGTUxnlttJzEZ3UBbJ8Bm1mOlOGf4nqrxS50r_qcsFn55ynw8_uJHqL9UJJmOYG-zjnpIQM1eYsqCuWJYPpfvoGPmLO6kReTx0Q5Qpjb40h01WWmL4nbcxHWhHFEk10iwif5nSEQG3hPebNcNmsUQSim_MQbFeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ذهنیت برنده بودنه که آدم رو به همه چی میرسونه
🔥
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102116" target="_blank">📅 09:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102115">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffacd8024c.mp4?token=ore31HQVCzg13dFep_Tqintr4gZENxyzOeyFvyrj3O09FmQ-gn_1RKrdgv54wuwIjqViLrSBlW7K7dGzz6d6aPnQ9Cm40Ulz8yWZ6kXnlAM1TbGvdBFWn-bZIe-zAZGc2poCXQhL99n-mrsk8ONsJHtB845P8SD9M1jZ00dcymOZbn80GlYYGcmQK8qBTvCx_x88qOJQKzog4aO5Trh8ZGsVse0pdukILX0aKjIzha7QpR_GHWsm9H6fx7bZX4uXXjZNlzYt7Ac5CgFRlILGt_Sv5Cy6xDOXndstgf7M0KxdexTSt4n3ue9ztOF6tg7hNuKsSOK6MMT2riw_oSOaQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffacd8024c.mp4?token=ore31HQVCzg13dFep_Tqintr4gZENxyzOeyFvyrj3O09FmQ-gn_1RKrdgv54wuwIjqViLrSBlW7K7dGzz6d6aPnQ9Cm40Ulz8yWZ6kXnlAM1TbGvdBFWn-bZIe-zAZGc2poCXQhL99n-mrsk8ONsJHtB845P8SD9M1jZ00dcymOZbn80GlYYGcmQK8qBTvCx_x88qOJQKzog4aO5Trh8ZGsVse0pdukILX0aKjIzha7QpR_GHWsm9H6fx7bZX4uXXjZNlzYt7Ac5CgFRlILGt_Sv5Cy6xDOXndstgf7M0KxdexTSt4n3ue9ztOF6tg7hNuKsSOK6MMT2riw_oSOaQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مایلی کهن و پروین و کفاشیان در خنده‌بازار
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102115" target="_blank">📅 09:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102114">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7e0420a2b.mp4?token=DBaTIvk0ZdqI-qgbeoz_jIS3D5uME7h6Ug6jVw7YFsLmCw-hZFBAIX41j4pq7GbZf7cVjPPolXDO2P0BdhG_GaWbYSbPWkU-iVTAoS5P14t6jIjMVrSQKqoQmbTM57fwy47vCo7Oc5m8Rc5Kti9LCUuICt8B8i25Mts6iFnVirVG8bkaslcellEYEDDUT3laolVWeXgguokJtdSl-OyQefAqHfCgGLGhkdCcdITUPY8Guj145dSb9DebKSHt0KRqJv5a-hdwXdwjmQZhTldhVr2BfP_LtKRpDcmFhouW0dNedAY3maIFx4jeKwEHcXM8cY-pXJg5XqUaNVtkXbGixRRu3ZiMyxD0UZSunXwlkyp-Hd1NsDpH5Bw9Tlh4ymVuyATbB6B2Hucfl369sTL0QOeXpZps-TVeHZuqzg9_PncOgeCIGpHnwklt8ZapFnz-ijQqeeUt4nkGLQZE2JyFA-GkhnuaVMtOPIj8PJGjIzifwvCoujzDLPLzgOPmnfN9sUz1FTpQgm-4Aqgo3DhhQQytX1SCTdY6xkRzbTMc3zAfM1sxFg0Y9US6f-HcdAW6ZSazdqgbqkuAmAIeGDxnwoCBAAdt-L1swFL27f4nAwilxCc8G1SSTfmbpnMnJV8jPde5VITaD2s71pyLnmzk5emh1znReD75z5QY1PijIdU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7e0420a2b.mp4?token=DBaTIvk0ZdqI-qgbeoz_jIS3D5uME7h6Ug6jVw7YFsLmCw-hZFBAIX41j4pq7GbZf7cVjPPolXDO2P0BdhG_GaWbYSbPWkU-iVTAoS5P14t6jIjMVrSQKqoQmbTM57fwy47vCo7Oc5m8Rc5Kti9LCUuICt8B8i25Mts6iFnVirVG8bkaslcellEYEDDUT3laolVWeXgguokJtdSl-OyQefAqHfCgGLGhkdCcdITUPY8Guj145dSb9DebKSHt0KRqJv5a-hdwXdwjmQZhTldhVr2BfP_LtKRpDcmFhouW0dNedAY3maIFx4jeKwEHcXM8cY-pXJg5XqUaNVtkXbGixRRu3ZiMyxD0UZSunXwlkyp-Hd1NsDpH5Bw9Tlh4ymVuyATbB6B2Hucfl369sTL0QOeXpZps-TVeHZuqzg9_PncOgeCIGpHnwklt8ZapFnz-ijQqeeUt4nkGLQZE2JyFA-GkhnuaVMtOPIj8PJGjIzifwvCoujzDLPLzgOPmnfN9sUz1FTpQgm-4Aqgo3DhhQQytX1SCTdY6xkRzbTMc3zAfM1sxFg0Y9US6f-HcdAW6ZSazdqgbqkuAmAIeGDxnwoCBAAdt-L1swFL27f4nAwilxCc8G1SSTfmbpnMnJV8jPde5VITaD2s71pyLnmzk5emh1znReD75z5QY1PijIdU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
ویدئویی که صداوسیما جمهوری اسلامی تحت عنوان مستند شوک از پرونده خیابون علیخانی منتشر کرده که ساعاتی‌پیش به سبب اون سه جوون مملکت اعدام شدن!!
+ اتهام‌هایی که به این جوون‌ها زده شده:
- بستن مامورها با طناب به تابلو
- سنگ زدن به مامورها
- آتیش زدن مامورها با بنزین
- روی زمین کشیدن مامورها
-  تیکه تیکه کردن مامورها با چاقو
- فرستادن فیلم از اون لحظه به رسانه‌های معاند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/102114" target="_blank">📅 08:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102113">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/508992e992.mp4?token=H82GzTrdtGFyt-CnXxb2aSYpAq8giCGC3kHeaF_LHfP6xEoRRJ04_HbkrNe_GrDWuq2GLzzJUZ4rrViagKSHX7keBvW_wIMn6qU6kFMuVMb0DtfF_9iAdXVrklD7JleuKmyJ38I-UTC2b8kDphonmpxanFd_frj92vrUIDRCSNgo_CTt-EgFdSarfb0_nAExeNjmI6GEh5bLtrOSar73DCQ8WLJQwKZf5-LATU52wFMUASwyNWBLxxFkCmIjSwg4EAoCzDDO-d-Vj5tiS9mg1pJSPZdWC0D9EiU8DZoU2dnuFAO8d-RfGxCVX7-nB62eTmPwZN4_N6lk5dpZfbLmLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/508992e992.mp4?token=H82GzTrdtGFyt-CnXxb2aSYpAq8giCGC3kHeaF_LHfP6xEoRRJ04_HbkrNe_GrDWuq2GLzzJUZ4rrViagKSHX7keBvW_wIMn6qU6kFMuVMb0DtfF_9iAdXVrklD7JleuKmyJ38I-UTC2b8kDphonmpxanFd_frj92vrUIDRCSNgo_CTt-EgFdSarfb0_nAExeNjmI6GEh5bLtrOSar73DCQ8WLJQwKZf5-LATU52wFMUASwyNWBLxxFkCmIjSwg4EAoCzDDO-d-Vj5tiS9mg1pJSPZdWC0D9EiU8DZoU2dnuFAO8d-RfGxCVX7-nB62eTmPwZN4_N6lk5dpZfbLmLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپیده دمید، اما روشنی نیاورد؛ گویی خودِ آسمان هم داغدار بود.. صبح آمد، اما هیچ‌کس از آمدنش شاد نشد؛ انگار خودِ سحر هم به سوگ نشسته بود.. ای صبحِ غم، مخند که امشب هزار شمع، در ماتمِ عزیزانِ خود اشکبار شدند...
⚽️
@Futball180TV
| Quf</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/102113" target="_blank">📅 06:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102112">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_MQCC2k1QgGZ8AZTeJFHXL8n5iW-zit5CpAdZTxCaATtCwyo7OeCy28c_8ZXcN2tt4E0yYDf1sW8AkHVGoGRymDzMDfRi7Jmeh4Oai9X1O6Xc570Jt_hTHcpnNBHz6S1YnSNqvZe75Ph4gcFpWunIx7blanh4Dmpw47wxUCfIOppdkCtIVd0jncrGeansVFJjdcmOjuSIJjnjxXnUZy_C2iisDl9cap6G_unLkh5ABs-KV-ldioNO9dvYPRrMbepQBhiEIJyILQSJ4fn_0k1mz9T2f8ccvJDtPXdUi7ZD9vMD2nS_mDu_qVfsNUiHCX8AZzT6TVdjI9KkFiCuvHYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوووووری
از رومانو: پرز مجوز مذاکره و عقد قرارداد با رودری رو تا امروز صادر نکرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/102112" target="_blank">📅 02:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102111">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhfqndiavNFUMmzpon1vpsP_AybxStkcvmVZT0r88uV4ZzYSOmtnoDdW0VKE-kj3qPHbdCCJWxgeIiPDAyvtQI52RUNqJernDqJulxiSF-tp-SXn8QRUotfHruITJAJGHQwrD9Iziu1WpsQcQeeBOvyk53BFXJ2xMY8YF5N_RJaMWuBwGrx4VvZfEVuGv9IHwZoJpNXXrYdS-4fStkSDwDVKP3rjwVX5P_Q_jjmS09gcSkVWBkZNPdE683unYokYl_QAQQfntk21iWPRhVG_kdcAE5cbDDzBZqYtRfw5j8JALadK3GDFBYcanPiHWk8xZmuPS8h0ihn8ZBmg_yy_yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇹
افشاگری پائولو مالدینی از وضعیت وخیم فوتبال ایتالیا و دلایل استعفایش:
یکی از بزرگترین اشتباهاتم این بود که اصلاً این سمت را قبول کردم. سطح فوتبال ایتالیا به این حد سقوط کرده است، و دلیل آن فدراسیون است!
وقتی منصوب شدیم، فهرستی از سه نامزد برای تصدی سمت سرمربی تیم‌ملی تهیه کردیم. پپ گواردیولا بدون شک گزینه اول ما بود، در حالی که آندره‌آ پی‌رلو گزینه سوم ما بود.
ما مذاکرات خوبی با پپ داشتیم و به توافقی با او رسیدیم. با این حال، وقتی به فدراسیون اطلاع دادیم که به توافق رسیده‌ایم، به ما گفتند که نمی‌توانند هزینه دستمزد او را بپردازند و گفتند که باید گزینه‌ای ارزان‌تر پیدا کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/102111" target="_blank">📅 01:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102110">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c83412a5e5.mp4?token=TbiEGjk8QFS-TxklsODqh20hJ8zjdvwmTQ9vgJS8xgJBrOPkIHJjvVgdNEpc-AfeCF3GpiFT6e19SzBKUavGutmL1OKjlxShYjdXyTHb8T9D_w1z6KKA-XwS_9LoyzvQYm_8989iH2gUId1V7HBW5IbzOvXheMuLgIRQ8pSoOuexKoDnlztZCrQfI-KHHtBKPwnZdVI_SYOMzs5OfzKcMyV0GUqfSFGr9IMQVx3JDL5mzuLpOwCmkSHOv_YlnV0xV3R-fKDt2OR0a2uAo6lWeco-tpnX-ExbdN-hhmPzfTJiHnsNwjNKhZ16Z0T0Shm9A6atgy_Dah9F6rgoYf-Xfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c83412a5e5.mp4?token=TbiEGjk8QFS-TxklsODqh20hJ8zjdvwmTQ9vgJS8xgJBrOPkIHJjvVgdNEpc-AfeCF3GpiFT6e19SzBKUavGutmL1OKjlxShYjdXyTHb8T9D_w1z6KKA-XwS_9LoyzvQYm_8989iH2gUId1V7HBW5IbzOvXheMuLgIRQ8pSoOuexKoDnlztZCrQfI-KHHtBKPwnZdVI_SYOMzs5OfzKcMyV0GUqfSFGr9IMQVx3JDL5mzuLpOwCmkSHOv_YlnV0xV3R-fKDt2OR0a2uAo6lWeco-tpnX-ExbdN-hhmPzfTJiHnsNwjNKhZ16Z0T0Shm9A6atgy_Dah9F6rgoYf-Xfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✨
روزی روزگاری ایوان زایتسف بزرگ و افسانه ای در خط سرویس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/102110" target="_blank">📅 01:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102109">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7bsJH68lX5-M6eMMQyDGnjHc8gYx-kwA3G1TxxTN4eIc6coE2z60uzni-HIyaDcHGksNjKxcqrj_hUyagY_prYd1_NyE7KqXsRU2eEgsoIH-WyoOYgOEcBsJ6YaOdGkf9IPtlAC_5DIfcicDKbb6j_nx7TDyvT1_y0-WeFQlFe7F0KKv5hvVAR5-OoPBcOTqWWNrv4_KI7PvNcYFgC49fmFG_Tyc8QVqjFqK6pXBhcgUTeXa4p2nI28BeJ8pGubyIYKMqN8jgKYGqnSRCcIVnTRzM8EnUALkvC8kkkDUJgzuO5wjchRAbpLgTMOmcV_eH2GcpyMJ5sn73VOoinOTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
‼️
لیست گران‌قیمت‌ترین نقل‌وانتقالات تاریخ که ۵ موردش مربوط به امسال هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102109" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102108">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQ41GFfnyhsFzq7sxBJLNg40FPiak8S5wcEnM-6p91wDOtE0shDom5Q5gncGd9pHQcsImdB0d9rJyF58HjM7BMUfOVwYC0fbt-P68ohaij3IKSfRlPXN9fBGrbCCIwZ0P8MzwWDNtEPEAMQt4026wjRYmkV9XHusxhPSrga6Bpps3BwsiI3tZ0WeWETq7nd80gOOOzAJihON4JPjVBUskGTEzDc7EKmnW4T7vhHD7FztTn-JA2Nhe021OwD___0p8Q1R2yhEgLhSzjMKiZPd_1rc8_WV_jFpFO0jM5i8lNDIK4GmNZv-kmaMra-X57HVeoZYNYdHqbTzzcRLtCZP8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پینی زهاوی ایجنت لواندوفسکی:
لوا برای اینکه بتونه برای بارسا بازی کنه قید 200 میلیون یورو رو زد، اون پیشنهاد سالانه 100 میلیون یورویی از عربستان داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102108" target="_blank">📅 01:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102107">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=jNYLN_irRyBnRCWfd-2tqVss3MrfViXT-rry4RDQujFCQYa5ZuS1iOqi7hDCSMJ0cImMhsArF_3AhSVnxgrhxXfVZ54VFp5bhxkA4Xzs7ndfVQou1P77GSPlwQTgt9a27xXN5GVbytDBne_sb5PNQ_htyA9QoPTTAXNaDQDCb3pIxGi7nqjsTj4pAJlH3jqHFBcA0VGbBpB6F6Sdiqv_vDiXUZx2SBIzsZsAkBefwIo96hUhz4NzYGyWzRXK8u78zhinoZy99ulZGuLqFiTyVTaKxTxYdXlNwNBmtkZdBFFx13vciEmD129Fasq7uEgV7iqwIV70IiUIAQPuTHHRjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=jNYLN_irRyBnRCWfd-2tqVss3MrfViXT-rry4RDQujFCQYa5ZuS1iOqi7hDCSMJ0cImMhsArF_3AhSVnxgrhxXfVZ54VFp5bhxkA4Xzs7ndfVQou1P77GSPlwQTgt9a27xXN5GVbytDBne_sb5PNQ_htyA9QoPTTAXNaDQDCb3pIxGi7nqjsTj4pAJlH3jqHFBcA0VGbBpB6F6Sdiqv_vDiXUZx2SBIzsZsAkBefwIo96hUhz4NzYGyWzRXK8u78zhinoZy99ulZGuLqFiTyVTaKxTxYdXlNwNBmtkZdBFFx13vciEmD129Fasq7uEgV7iqwIV70IiUIAQPuTHHRjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آمار تا پیش‌بینی
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102107" target="_blank">📅 01:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102106">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhbiOzuRMv-nIGm8kJ9UPLqam8c01RlAktpWSHYTF9Yc-p8SR4TOm0W1WlchMycGbOGiEiP_On7AQ4xvQGo39zUZbKrNgQ-YdW6yf3wYasS9cmqUOS3-04GKSHw56Ka8Ln9_AmqY_o18Xy8Ct9jR_7fKP3TZhpcQeM8ffvaMj8BAQR7MlsgribW4G7Xmon-PZne_dyd2g2zKPC9Tp9-qHmS1OmrC-DjvDIMhyEfvUs_nIvQDCGGgcoJsr_6Q9wmuySUjlamH0OEs9q5W9ZW57tUUtfAmzqJ_jW0R_eQBf5bqhjzovLhlGGxLt2dGv3He7jab_Ot1YF7WEs6178MkdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🤍
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فلوریان‌پلتنبرگ: رئال‌مادرید از علاقه آرسنال به وینیسیوس مطلع شده و اولین پیشنهاد رسمی خودش برای تمدید قرارداد رو تقدیم ستاره برزیلی خودش کرده. از طرفی آرسنال هم آماده ارائه اولین پیشنهاد خودش به رئال برای جذب وینیسیوس هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102106" target="_blank">📅 00:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102105">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sd1SiE-jzWlzc8tLoZCaAqLr_J0-1uS09gtAIxhsmQKNIYW2xddhNjBdCqKuH_Orqt6pQQZfCCQ6nMSV0F21RL1CQ3XZd7nIUfI6lp9clqdikypEDeYgN9-uIkFFQtqVpCo5HaESm9iljIUNtfSfA3bb5QuHtBN_hjGr1xlh_4Xmh0uM4PV0emEOKzKn7vyU1GdqVOE1rk3cvyS8UZYiRiohnXfORKvMAVnmaSsqT8bJdVHYNkM1Df1ISbhJa0L3y8SGAINqvx48_8l1UlNmXN-x7J0o1OzKveKm9skYyeajJURWVFxAC6L9hlALeNFnIj_qbjMtJgFfMvVPUOoFBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: باشگاه چلسی موفق به توافق شخصی با جردن هندرسون و دنی‌ولبک شده و بزودی باید شاهد عقد قرارداد با این دو بازیکن باتجربه باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102105" target="_blank">📅 00:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102104">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LjTjln2lekEAtEZnroAOHs0vGmPG2gPunyulGQH6TCC-Ot8gMfCl4Vnkj3-DtiUG9vjhp-aA8xT9-XOWJZ3k_yADKEytHQ9XWTezo-_0BtYvcLFs9ZO3nGb6Q9Qgq0dnxnO5grYfnMN3JEsgohaSSWRulqXV0O8U2fck_6WvbxaPFoaHgLhlL9hMOKgUH1BLHoSYdapWpabHGc8spxB0LpLJWwebFso0a-uJxTtuE4iZaZz0YhioVUbUzgTbdwSBoesyb1j1eSCnuHPJiMLC4Lj6F3G9SiOW9QMCtwGCaF1XEmramgiR3Yf1nlnYVDM_kW_Y_ePv0NqZAInjzmBmcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇩🇪
فلوریان پلتنبرگ: هیچ توافقی تا این لحظه بین رئال‌مادرید و لایپزیگ درباره دیومانده صورت نگرفته اما مذاکرات به صورت فشرده از فردا ادامه پیدا میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102104" target="_blank">📅 00:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102103">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYgry2oPDOtmqadWJfiITMF8jllxBNZj6hCypdFDu0vbYiyoeQgTB68iub4_eNjmSuDGn5iYVVcH6eDYTw6Ohzufmnyrn-FKTNqJCxCMKZqRn4lVRVQ0aLAYCJVFLFmUdi0ws3vjMFMQDas1rOLm0YP50j9jzo8faO6MAEgCTRynTf2YkHeVbXoHXz4SJmga-yvHOZTk89bEerWycDnn-5VbJIWj2qqdudWY207icBMVm-H6qBpu7jFA0Qqz77tYN9HQlkdKcvEYM90fnQKLGxmbLFuX2gUXoDEJq2Sztoz1Dkm9CZ2Qd3wY4d5t-It9awcdhzfuPKAKUkUyNgiE6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: مورینیو درحال تلاش برای قانع کردن گونزالو گارسیا برای موندن در رئاله. مورینیو به این بازیکن قول داده که با وجود امباپه،‌ دقایق بازی مناسبی بهش میرسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102103" target="_blank">📅 00:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102102">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_EOTumwkRVXLZpu0MD4n4H89al--onMCOrZfdWPGP6iGpTst985HngjPsFSxyuIkqV-V-wSDJIQdLsZKYUA3obzrwNrFYfGbsIcDxrjc_eRkecboegrV_41y-sjDlXZNQL39PpUHBTRtEczc0t4s-1mmDcEF7uaSAvNVghPhvCFhJKbgoahFgcfjcFFy7otlKqvus3YHM4RO1ZUgXkwCNVW4UAaa-OyC2028uTRiQWvmsmaJJV6qv0C8ejAngvIV_s9977lRm9PBNRfL5pDH53GFiSgflt-3gVNz4DE2eSIcugV0HzwuWHIsXgpW4qRgR6TYSf3BM5O3jrYq6TbAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
لباس سوم فصل‌آینده رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102102" target="_blank">📅 00:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102101">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52dfeed19b.mp4?token=Xj7k3uU24aGglU7WV6L3V4lLRXhrmQMVRGNCnh2gfiFuGltB1BRB06stAiI0xyMrYWWXe3ArMVKts7-mLFe182yGFYgyL1hAN7551DNa-_uH8sKjdLt_T7rsGbOAyJYJJkjTKQg92i2XK4OAV2oEq58EjjBYNDceYn4IrGYQ9ZQKmqFgEyh9k8v4Fyp_uO9j0chNflOILHYNsuSLBDidKL2uRvryx551Omk2IPErHuSURglj1PuxmdyFyIEamWF-qLUilWaOENN_xyeyfJ7hrtKvXqt-5OjnYNzYYtwNcsGwWIguFbhWJ3lUGYPQDXDU99UuH1lFRQuVU0xHrqAi1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52dfeed19b.mp4?token=Xj7k3uU24aGglU7WV6L3V4lLRXhrmQMVRGNCnh2gfiFuGltB1BRB06stAiI0xyMrYWWXe3ArMVKts7-mLFe182yGFYgyL1hAN7551DNa-_uH8sKjdLt_T7rsGbOAyJYJJkjTKQg92i2XK4OAV2oEq58EjjBYNDceYn4IrGYQ9ZQKmqFgEyh9k8v4Fyp_uO9j0chNflOILHYNsuSLBDidKL2uRvryx551Omk2IPErHuSURglj1PuxmdyFyIEamWF-qLUilWaOENN_xyeyfJ7hrtKvXqt-5OjnYNzYYtwNcsGwWIguFbhWJ3lUGYPQDXDU99UuH1lFRQuVU0xHrqAi1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تموم فینال هایی که بود
میرفت تو نسخه (پرایم) خودش
و تو اون نسخه دو تا وینسیوس و یامال رو میخورد.
شاید یکی از دلایل نتیجه نگرفتن آرژانتین مقابل اسپانیا هم نبود آنخل دیماریا بود..
🥃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102101" target="_blank">📅 00:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102100">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f39b79d0a.mp4?token=aRavKYZAmyc1sbEV3G3MHDBrX_94rEqTl4fpcT_OhLBEAxaqMupVgmqeoVLENssxqnASZQM17RgSkysSFIAT49rCmJjsgK1iVUu1qZV-SFAxPqejC3a0xfZ_GbapqK_dMTtcskW4Onqib5wq0tp1ISkdURf0_lqtAR7uGVa_GYxvbPwtc4up9iY28zOusdrweCIYeoI5lxo9W-aD6luTSxuPzsoOTtjb5kLoQQPkyeYNWFZveRe-S31vxUhqsQpNO2wG9wLyxGGwozi164o428TczNTxAi_Y7orYjAqkiMIqz67FuTOKvSYfiyNQCnAu46C9yOsbJwD4a2SHpL5GHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f39b79d0a.mp4?token=aRavKYZAmyc1sbEV3G3MHDBrX_94rEqTl4fpcT_OhLBEAxaqMupVgmqeoVLENssxqnASZQM17RgSkysSFIAT49rCmJjsgK1iVUu1qZV-SFAxPqejC3a0xfZ_GbapqK_dMTtcskW4Onqib5wq0tp1ISkdURf0_lqtAR7uGVa_GYxvbPwtc4up9iY28zOusdrweCIYeoI5lxo9W-aD6luTSxuPzsoOTtjb5kLoQQPkyeYNWFZveRe-S31vxUhqsQpNO2wG9wLyxGGwozi164o428TczNTxAi_Y7orYjAqkiMIqz67FuTOKvSYfiyNQCnAu46C9yOsbJwD4a2SHpL5GHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل سیدنی لوپز به آرژانتین به عنوان بهترین گل جام جهانی انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102100" target="_blank">📅 23:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102099">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUhg9X41jswD5si1bJwxmiJ1jsmVfwMC9kgf8asXxRtDrNaRnSmeIdgQaVzVS-d85EiahH6tmoWXRkHpyEWNPLbTDrga0V5oH39xsiXGUwq66Rk7_pIfNOiAFPzZyase1SuO58aGrfoqYsQGlbQ_nJmbTDuzKS20OLyZKNLDlX3reIKA0jeEyBKQ-ESStTeAtrh4BKG2-e5T1e80SR-JM4Q_aEcdElysSOS4AOVMRyPAfZKySSWXNWnsk2MDC7NOMvr0uDQKVvOrtOFmMxo3apPo4VT1qtoA0JhykHA-xlwVfJHjnKnbxjUEe91lIPtMKTrtKoTqHNAoTbke1R1Zrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو:
جان استونز به اینترمیلان
HERE WE Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102099" target="_blank">📅 23:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102098">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBlebmnbaMOSHykitPbXsCYvQjJwkeue88nNqooMopvulZYDqNJt5t-toeA5m6ZyitIXCighhXIhJTv4WOP3_W2yUHPmwZGzzzxHgu-9nPaGtBlfGuBBPawVDgJ7Okaep5GW5IDd9pq4LusFFGVuNjZdaM14ENjIG24LY-uJ8lT_X3JnUuhJB27QNW6Qp7NSYpjk64W6JyeX392KOj3JkBPEKjIdeS9RDLvt-APSIWGAW9vqKcGuYQPFKjM2rcOc2oFlkH79m5L8zgfK19qqDik1yRbM4hjT9NDKrMz1r-dsYBm7tWeupyl01DNMI07BUMxIhZp0wf3ha6HosWXEbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندریک و خانومی و بچه‌شون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102098" target="_blank">📅 22:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102097">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUHLO4kVVMG_lOCbsFTiTajrBoSaJjoZnUZSLoSuS97p-wX9io-B3jQNFHMwXc0gxj6kjXyQQNl4SZA8ro3ATXw8j1eeXvihGbKQe819O5sk6EUk68jq78PD-bq9X-AiuJ-U7ECvJN09fqAx3NwCjT0h53W-SVq7amDq84naVhhiImm0QlfuTjWTRq_y_m_a4oXSjasDpOumhl5WoddaUseQidjt0Fz-D1_GWsEsZf9znvO4Ca2WrEhv-SXw5KCY8V9grIsrIvRAJBJhlzDvDfbiVPWERZt0-MGM-UhtdzH7m7J9j4lgK0v6Es8Ui8auCvTP0ycl-JY_k1eMLEAlWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو:
جیمز ترافورد از منچسترسیتی به لیدز یونایتد پیوست. جقی 3 بار ادیت زد تا تونست درست بنویسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102097" target="_blank">📅 22:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102096">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxAJ1_PAkMG1pRf3WicibUiVOAVA4Gt865qpa3_N_pcFY_bksY-2Xupcim2n_dMPLHQ43Da8GaR12SssAGUB3vMhQTzIldsibRj0hbkfrIcIqI7iWtS6uLg3bJ7gYVUfof-e0VQYYnVcTukToZI5QwrDLpFOhYAyodpylbb59y10IUtjYdgrKgJewMdnzEeAXYXVbGc9xaLfklbrIi2PYocKcWoxB6m1k7rdxmHjm26X8dBcfKuwmYOtURS7Qxlo62gKc6SbmJhptk6bFL9nN29nMmCOIpuWV9rtnMbwc53utrtMM6jfXUBH4Fxc8Eer35vB0K8kKW666G6-UHS6Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
تیم منتخب بازیکنان آزاد در تابستان 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102096" target="_blank">📅 22:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102095">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🔵
متئو مورتو: جان استونز در آستانه پیوستن به اینترمیلان است. دو باشگاه در حال نهایی کردن جزئیات این انتقال هستند تا آن را به طور رسمی اعلام کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102095" target="_blank">📅 21:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102094">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbNUEg10tLPNaXa57AArF8e23t0v8GHFwUbxUlkVZBm0BagwRzILXgcRf0N7qicPY8Vyd9tM_EXUDyXHFAF1oLtuNszWHub7TDx-0i5Rj542uRloE6PiIDnnUc0r0hc_tXU6KZgOTuqu7hULlArShcoJLLXyhy2VglasJ_vHk4bCtY13QkQdFCDt8i6YqAA6JJqcVxZUn4FI1xP6Oq3vr_MZBPFPGscNFaDUfNvkykj_teWk18XFoI7_MKh3Yw0ff74hA9-4V83DgKAdivnhClF1UbmQW3EzL4M9S0lRdjfMePYuKd187JXOj9K9OTCkYP0TNhjcFlw7sNNSj9K_Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فلوریان پلتنبرگ:
لیورپول گفتگوهایی را با مدیر برنامه‌های برادلی بارکولا و باشگاه پاری سن ژرمن آغاز کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102094" target="_blank">📅 21:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102093">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLJWclt2lW2uGh2btOdHMSasesxj_lzki24Kz5iL5Biz-9MWoEwfnsGcqNEwwixd7et67_mpftn9bDVVDyJNITjfZjHX9e23VokZXoH95akxAQLQvWZBTrYiaIzsAZyXPkeZM54LrsHsZmP4KQBQxdWiLk3xdQm8SHOo6CGBtLi-tMzQ2x3w7fdx8U7KAy5I7PLJFEMsDLPZnnUu-pRHBWBZcNXhr8Ktvig12zveP5UkFqdpidH1NnK20w5PTdhXR8nzXyxgUiyzzFbyw3we1yzBepMh9WSWLyNFCt03wMRnpc6voj8qNLzKDy_ujStb7tpTCHgUEJA7EAs-Pjle2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو: چلسی قصد داره جردن هندرسون 36 ساله رو به صورت آزاد جذب کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102093" target="_blank">📅 20:57 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
