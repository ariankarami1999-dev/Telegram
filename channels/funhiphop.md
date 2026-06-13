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
<img src="https://cdn4.telesco.pe/file/vkhcwemlJbPYmHtMrLqr8bhhac4GPVW7D6W2HLA5JuSceKzNkcC6SbtN1Se8HohsHhlg2YW56ZApC6RDhNqsiS59cLiYmfYi9ZNv0pS4KKIyCnrX-k3dsefdBDkyxRjw2oEpD7CAAyqq0zgGNXx4Ah6GbIhddloSYOEJFJxUzgKyonpb71o6R0V9O6Bn6viP3XsFd2XfgWbiQ_2aX_qBRa6Zia33JNGzHYqcXM9aar_2A8S-jA_9Fmm8FPTcpq__dT-VbhHvNXh-1mSDK-f1ELlKf3z9Zt2mlXd12xV7DHrBKds_XCoHPUXB1xFumCY4-HFNrAEibA-_LT_6PaKLxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 172K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 11:49:06</div>
<hr>

<div class="tg-post" id="msg-77763">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نیمار بازیای گروهی جام جهانی رو از دست داد
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/funhiphop/77763" target="_blank">📅 11:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77762">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCr5IRmrBZVz3jceNAM_9A_2sKdtKz0LMkq3eRpxYmB1St1pJXEEqR8Kc_lO95YLqCyrk6WfE3Y_xqT8Vjc-XJ4ZCh714u6RhC1b0-ShLLrbL3zNq9RV3BqLBBTiV0cI3wFzm6k9H48D60QDi8w5-D_oxbNpKXxCJ5Lx6kEXgdz3u7kwktJgfpjHMssckRNPW1k-AicMi0uLAoL_g0ezybTTvIdvd-ju84oPk3FzslfV1h1BTGrZ8mWMmW8ZYMw0Np8xEkEMNQtH9VYQqnUkA38V2SmIRxa5vxMr3HHhL20G-M1-5lCxu9FaTwiPQSwnXvv9Y7FASKhmmGC_Y25zLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو نگاه اول آدم میگه طرف یه عقب مونده اس که اومده برا دیدن فوتبال، ولی یارو جزو تاپ ۵ بهترین بسکتبالیست های تاریخه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/funhiphop/77762" target="_blank">📅 11:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77761">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آمریکا کی انقد فوتبالش خوب شد</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/funhiphop/77761" target="_blank">📅 10:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77760">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odNEFBJdhVO9bgOm1jYs4U8GiOTMySLerilsZlD-KvCo8tyuQuzmVh6Ixp4qE4KbcutbiN-Y9yR48QIQi2u8vgMrVUuojr5jbykyDJAOK31KdqEaUuNKjw6l7OBcV834fSis8rw_g2Y32BqJmgDMNXMpAIQMLv7ON4mf6znodyU7cBY9KR4pFOyWUzVkTb2SrWo4X43wCRTty1IGk-6Pd-a9MNA5uflCF1hBabqL9d66J5fLHcXhgVZj3MRnpm_X2wrz0uXnfpY_rRJQWsGJKRIzelem4v7EO4xQKzatKP5tDG6pWTUYmNjGqhl4vrqit7p_MMt9RX5Yefa429AIag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقت قهرمان بازیه پسر، شهر به کمک کن نیاز داره.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/funhiphop/77760" target="_blank">📅 10:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77759">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77759" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/funhiphop/77759" target="_blank">📅 10:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77758">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zo8Q-gnsr3OX3k5vn6B3vo7Zo3NGeVAYCDBMrC0_pp4BdZG2_dqLQxxExanNr3m-3dLMRKCmkNbaPfDktCM4oLoKtl4XN0Qxg6Gh8L7GZMC-su2GUhP_ke3TegkA_4RTRdiDLGOHDA4pry_PPP2qzEQKNoDX1F2RUvyjwMDifkEsARVJ5LHK3qgOLOt2NYe7Dvs_s96tZlQdKHHQ5f7uaw14eE7YPaQl0fLcjBc4069HpIQI4RObFe50_8beuBLkPDVW__l8T9fn-B67e82MUVBmbQoQ5d8WXHMGTNyWsv5sf_aNcim8pKKUnApZs1lgkatzALdn5tYzLPDK6CJ2yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r23
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/funhiphop/77758" target="_blank">📅 10:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77757">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">درود دوستان شبتون بخیر
💤
امیدوارم حالتون خوب باشه
❤️
کانفیگ داریم سرعت جت
🚀
(جتی که حرکت نمیکنه) کاربر نامحدود
♾️
اتصال پایدار
✅
قطعی ام نداره
❌
(چون اصن وصل نمیشه که بخواد قطع بشه)  هر گیگ کمتر از 7,500 تومن
🔥
لیست قیمتا توی عکس هست
👆🏼
ایشالا که گول حرفامونو…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/funhiphop/77757" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77756">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رویترز:
ارتش آمریکا امشب چندین پهپاد انتحاری سپاه که قصد حمله به کشتی‌های عبوری از تنگه هرمز داشتند را منهدم کرد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/funhiphop/77756" target="_blank">📅 04:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77755">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiJreJl8gv12rht4c-3HzkQ6FjCQpSWPvwIwnn0508j6hOrPK61APagaScuLJB08X3ffKCxaOAkxrPiws418u9EXgt-74Slq_bZlhONdeaypWoTKsDofMn4P78q-dEvrVMDUwDLy65ppbbgIfrY6TG3UIAXM0yx13t5YN71vHz829_Ew2zdxaj0PygvPgfUXZf3-T44-0u6Lo6nCDSCVXJz6QLEKHSSXwcEbhFc0qXxs4Itsn5XLgCFndAxHNc-ALFy8N5sFMH18fYNnjxkRMFxZZ_-adYmNAUEbf3Kah5BckNOuUf2x1OJ495dZ1F7qK-IvaZiejKFzELfRAqFQmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار باقری هم در اتاق جنگ بود
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77755" target="_blank">📅 02:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77754">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یک سال پیش در چنین روزی جنگ ۱۲ روزه شروع شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77754" target="_blank">📅 02:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77753">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">امارات آزاد کردن پول های بلوکه شده جمهوری اسلامی رو تکذیب کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77753" target="_blank">📅 01:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77752">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">زیر این پست قهرمان جام جهانی رو پیش بینی کنید، هر کی درست حدس بزنه صد تومن میزنه به کارتم.
@FunHipHop
|  محمد رضا ناصری آزاد</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77752" target="_blank">📅 01:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77751">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e3c0e5144.mp4?token=kin3-FC-Nf4nXHcUIhj_eK-tnsC0CHAoDy15DS3YYRDuq7hJc3ncSooEpLxwmV_mbke_Dv01Ag_bVyiRORYEVGXMCbAtPc1bb-CXn4Enit5O34RaRcah8IaXFOnGqucAnBcM4BZjvZ_ySfV0odXoJTBcEenUroNiWdqPMbimbCYo3GSBfOPjl1MajdG7_U605EOJtQ0e3npfeDjIFdzsj0qFvuXlFcES7h6yw_6mCxObZxiJlGuTulB-0SgDowtjIwsGUjdPgDjWScz7e7g5jHkHw0_f36vLpyn5DA3eHeAk3GvU034Gt506JCmxCmbMfd-hCi3YddeeJX7F4PGB0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e3c0e5144.mp4?token=kin3-FC-Nf4nXHcUIhj_eK-tnsC0CHAoDy15DS3YYRDuq7hJc3ncSooEpLxwmV_mbke_Dv01Ag_bVyiRORYEVGXMCbAtPc1bb-CXn4Enit5O34RaRcah8IaXFOnGqucAnBcM4BZjvZ_ySfV0odXoJTBcEenUroNiWdqPMbimbCYo3GSBfOPjl1MajdG7_U605EOJtQ0e3npfeDjIFdzsj0qFvuXlFcES7h6yw_6mCxObZxiJlGuTulB-0SgDowtjIwsGUjdPgDjWScz7e7g5jHkHw0_f36vLpyn5DA3eHeAk3GvU034Gt506JCmxCmbMfd-hCi3YddeeJX7F4PGB0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میساقی تو آنتن زنده خطاب به کسایی که مخالف تیم ملین: آدم مفت بر از خاله کسکش تره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/77751" target="_blank">📅 00:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77750">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سیریک صدای انفجار
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77750" target="_blank">📅 23:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77748">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">عراقچی:
دو تا موضوع مهم هنوز مونده برای توافق نهایی؛ یکی بحث تحریم‌ها، یکی هم مواد غنی‌شده. راه‌حلی که داریم اینه که غنی‌سازی ۶۰ درصد رو رقیق کنیم. در مورد تحریم‌ها هم، ما مشخص می‌کنیم که دقیقاً کدوم تحریم‌ها باید برداشته بشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77748" target="_blank">📅 23:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77747">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">عراقچی:
برای خدمات در تنگه هرمز هزینه دریافت خواهد شد و این خدمات دیگر رایگان نخواهد بود. این موضوع مهم تأیید شده است: پرداخت هزینه‌ها الزامی است.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77747" target="_blank">📅 23:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77746">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">عراقچی:
اگر در ۶۰ روز به توافق نهایی نرسیم اما دو طرف از روند راضی باشند ممکن است تمدید شود.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77746" target="_blank">📅 23:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77745">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">عراقچی:
محاصره دریایی آمریکا اولین چیزی است که در این توافق به آن اشاره و تاکید شده است که باید رفع شود.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77745" target="_blank">📅 23:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77744">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">عراقچی:
به‌زودی ایران و عمان بیانیهٔ مشترکی در مورد ادارهٔ تنگهٔ هرمز منتشر خواهند کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77744" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77743">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عراقچی:
دشمن تعهد میده که دیگه آغازگر جنگ نباشه و از تهدید و زور استفاده نکنه و دوطرف به حاکمیت یکدیگر احترام بذارن و در امور داخلی یک‌دیگر دخالت نکنن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77743" target="_blank">📅 23:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77742">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">عراقچی:
توافق شامل دو مرحله است و موضوع هسته‌ای را به مرحله دوم انتقال دادیم و هر وقت همه چیز قطعی شد به همتون اطلاع میدم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77742" target="_blank">📅 23:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77740">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0oTxD4HGRlF2aoKTAdvg5Y-yIby0nLcWhZv3CfkQnsV6x6x_3_zHNeoVw6I3dFT2uqjJutUlx1lNya85GrKot1FIjjHlHMgPUepxgi9l8ZhC4T1hMYuWQMEQDNn9Zk-keZN8_nN_-ilA0XGaFNiP3j0tf0Bweuie9hDpoQcrtkaTCEN85u73hLd47eV4caYESsuPd57NWwMoWjOl_VqqRE1e7TNAeBW8F9rhcb4cJ32_OJH7SwHTXdvp9Sroehft1bu57jVa0I4hGP5icWusC8KT4_gvMjcP11D5c6dUybR9rWpQAbOgy0-MUjSr5dN1s8XqYKLclQiJ7BhYBS-1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
YËAT
📌
ADL
📌
Lifestyle
📌
2093
📌
AftërLyfe
📌
Lyfë
📌
2 Alivë (Gëëk pack
)
📌
2 Alivë
📌
Up 2 Më
📌
4L
📌
Alivë
📌
Wake Up Call
@DiscographyTship
🇺🇸</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77740" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77739">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_K6SOe1wvCCUaHRUNiGVLTujfEceX1VJMY8ZXsYoIJNudSnolM1BKVsyubgMsKDu6Ou7jJXZpkXnJRojpELZWqjPN3NXEyK5vYOgMN2rUMcvNZetsHM7bS6Pa19Y8iYVBBZ9p8rQm6sR6PzVsI3kEN0xYbO8n6_hmWUUG-dAz9skGLf1I686A0E4TbbzAMfu-biu3ZJppU3QbvurJnGO0m_9KcLi8sZ7r-HpowivyFsS5dJd54SHFx4JW1ha4Z2lRdom9h_lCfDZDkDo-2Vz9ulNMyBNrdL68dEGnF8PP_v2WvmJ2HVyMfvaTjZy53m4lO2fkzo7axE0MIx11o1sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوف خدایا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/77739" target="_blank">📅 22:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77738">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIK_0l96Msbuid1UXezdWdYBjWL23UUZxNNp_4tf_0lJ6ll5YFBm7Nf4P6aErf1cMedB_gy58W7q59IK9vjnwQ4bEo-0i7U2l_0-RzeXSqjX0yhTLokc_TmNGV5ax-rk30ShEqkHgVxF-bU3qHdlHB6zg8NZMT_bkj1kT_qxdNSa4XVdoFbSL9B43QsExn-kW5JSwDrurLJtMdVOCV5FuLRVQa73wKYVfy7PvYScK0WojTbCZIvC5HUZIyPFJnWN2VYQxzNzp2NKFXXV9myRztJBwpJC328oODvSg2OiAHQ6R5wk4fqyYMSWNixR5hr3CXUTTv8ZiIJ0NvoxBVLsXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود دوستان شبتون بخیر
💤
امیدوارم حالتون خوب باشه
❤️
کانفیگ داریم سرعت جت
🚀
(جتی که حرکت نمیکنه)
کاربر نامحدود
♾️
اتصال پایدار
✅
قطعی ام نداره
❌
(چون اصن وصل نمیشه که بخواد قطع بشه)
هر گیگ کمتر از 7,500 تومن
🔥
لیست قیمتا توی عکس هست
👆🏼
ایشالا که گول حرفامونو میخورید و قید پولتونو میزنید
🫶🏼
Channel ID:
@RezoraVPN
Robot ID:
@RezoraVPN_bot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77738" target="_blank">📅 22:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77737">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دوستان عزیز در خدمتتون هستم با یک برنامه دیگه از سیاست با فرید میخوام فلش بک بزنم به حدود ۲ ماه پیش  عباس عراقچی در یک توئیت اعلام کرد که تنگه هرمز باز شده و ترامپ هم در مورد این اتفاق بیانیه داد نتیجه توئیت عراقچی چیشد؟ رفتار خودسرانه یکی از باند های قدرتمند…</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/funhiphop/77737" target="_blank">📅 21:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77736">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pb26cPcqUrojE-dLGU4nzfM3SKXP07oNUKiicN__3jtlSrlzdIfECeKTT6Ze9UtQBIlPXY9g97je-_-azCfUSaShOIeq764Xq89aXlVBTh32UmbmXV59_pAmDrZWP-ogr7nHLGiDyyjG3ipDEfIO2SJqvnjDPKxaBp6KT_IZ9ED_uIARNSbvpt1S1z754MWdI8TCaN8eb7maLz-onMA4g6hZ_n2L8qYJLmfhvK0FzrgOnWxpDy_KdQYzBcQYTVntpDN-dhgEjJPuNFPIOcwurgyZYnE-Si0f7Zo4p-X9ySfk82luuDW25l3zipcjBB3l7L-N30bb4Da1_AL56JrHlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Kendrick Lamar
📌
GNX
📌
Mr.Morale & The Big Steppers
📌
Black Panther The Album Music From And Inspired By
📌
Damn. Collectors Edition
📌
Damn
.
📌
Untitled Unmastered
📌
To Pimp A Butterfly
📌
Good Kid m.A.A.d City (Deluxe
)
📌
Good Kid m.A.A.d City
📌
Section.80
📌
Overly Dedicated
@DiscographyTship
🇺🇸</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77736" target="_blank">📅 21:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77735">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmJzRB0vmZ6cC5Dm-8hDuAzzssiGWgvyvQe8FjMlwbyS4zAvbifhs-T1_1GSDCG_pEhtedV767k6QUnM_YF7B2ffRpe1Bw7o_l4E_MZT_mgVli1w7DlqF3IUHNu-983HKDf0A3X7JRHpkyjoRLOKanWjeHi80ufK_FAV39URUS7t4tTCx2TEzpw715-jXZUOq7l-4ZVc1cTvJfc9bd-PVRBpFqp-1Ts3evns7V4IVY97nw2PG4DZjhKWiIQI4Y5dENod3Gd8b5XiSIivA3hRQsEhR-9oYTZqCYsuiFd4uVUTpK47YbdZja6vtBdfFrIuRpVDJOy9a8JrXy1Z75bgxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیدم مردم افغانستان میخوان قیام کنن، میرم اونجا هم یه سر برینم امیدوارم اشتباه شده باشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77735" target="_blank">📅 20:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77734">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مردم افغانستان برای امشب علیه طالبان فراخوان دادن و قراره به خیابون بیان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77734" target="_blank">📅 20:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77733">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دوستان عزیز در خدمتتون هستم با یک برنامه دیگه از سیاست با فرید
میخوام فلش بک بزنم به حدود ۲ ماه پیش
عباس عراقچی در یک توئیت اعلام کرد که تنگه هرمز باز شده و ترامپ هم در مورد این اتفاق بیانیه داد
نتیجه توئیت عراقچی چیشد؟
رفتار خودسرانه یکی از باند های قدرتمند سپاه و بسته موندن تنگه هرمز، ایجاد جنگ داخلی، حمله خبرگزاری فارس و تسنیم به عباس عراقچی و …
الان هم به احتمال خیلی زیاد توافقی که ترامپ ازش صحبت میکنه با باند قالیباف و عراقچی بدست اومده و این میتونه تنش رو در بین مقامات باقیمانده به حداکثر برسونه
باید کمی صبر کنیم که ببینیم واکنش باند مخالف توافق به این توئیت چیه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77733" target="_blank">📅 19:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77732">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">میشه بگید ژنرال یه عکس دیگه بزاره؟ من نتونستم ساعتشو ببینم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77732" target="_blank">📅 19:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77730">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jV7V1fLCxGofK2XwGYvHhDlTVpnWM5_MS7pnodaWEVJNeKBEZT7bRmPQC5_fNgE_3Rr5QZZeezTrzJW4IIMP46CwFcrYhqxuHst5erJ6qVQ43a6hmoOHmE1xM7pnRUZ6aWxaxJB_WU2zC3elHc6MiQ8cIkiWAvwHfjublQFHwVBzRAccu745-WVpWKJNEMMUDZdNYC9oDAe2mqIstfrw1xDJSxTG-y_sGaYN3TSk2hxpp3ApH-ha-OCbhOpmpPYmhQGqj6AAOut1evJjHvQmfaW73hUzojhf8hIkw8U-1Ux-8FKFQTWBkQ7ldneb2Wvx4-iyiumiYYBwJ7Xd_hSuKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دالگخیز توییت عباسو ریتوییت کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77730" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77729">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rre38sxhiIz5zJSfFrDhDIpgDD28skit617sBn92t2dLFOOu_z4Fadk0u--_5HBDqakCaJ7rbTr-5EkxhsslykpztFeuPTBwKZ9hz2-BUPI-ECqRu6QFLyOG6SPB47jchT6997g9jf264xtFxmiIPMhdkWcfO4pxaDPahD5rvGVLQGJtIKuBu_h-UKnS0rb9ZS9ffNzCk1vDya-6Z_w9SledS9DkDANWId-Dr0Y_n0NG2TiTnprfisLDwoJeS7JAwQMa4v8L6ooQJKDqhPR3y9XpodsGIdkcEubqRETckqk_2zZwsXBUfpLgZtR6HY4fmD7NA85_UGWbWwILzQQgIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سری آخری که عراقچی گفت به توافق خیلی نزدیکیم هفته بعدش آمریکا و اسرائیل حمله کردن پس تا یک هفته دیگه جنگ میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77729" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77727">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">عراقچی:
توافق با آمریکا هیچوقت انقد نزدیک نبوده و مذاکرات به جدی ترین حدش رسیده، بزودی جزئیات رو با مردم به اشتراک میذاریم.
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77727" target="_blank">📅 18:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77726">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">شاهکار ترین عکس روز  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77726" target="_blank">📅 18:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77725">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7H7SMEOjbDbx9Mz1d8YEKsgHf_4LJNBnjp2CjvvjnAabOd1LGL317pNxZ49AxGWZvLup3yXdUaA-aDGjWaPOURHevQzA0QiYTfP417JMGnfByIQF7Rw0XFqO--nJf6BqX62W8e71ML80Y_0IoJQV_u3osn_x4Yce5yx1AuGAkOZri4GqIxe4xqR42B9qxBkJRiCtBhIjQNuijphJNmRxAEeGRWSZi6iuC6XWwJXwh9788sVwHErCRy0n6QcTBZnFckb0kIghhOweCTjn5lAMAN5P4F40d0bXzNr-eZMD4RUrVghBHQOe2JuS3hiucJ_F_W5H2F65lGHgbTmYEaFIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار ترین عکس روز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77725" target="_blank">📅 18:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77724">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtd74wyI180E94XC2kUHPNEtnhqfFXb1_q8dtUXiQRhxMb_RXAbHUb-CS2XR0qIgRmOko7IaLTPa86Jamk5BaHTxDO1Beigl6ovMMPwBuFu92rzjoBpsPOzRcfKiHvocLIKmfcBNIQ8Rw60vnYhXYIqSm-exjJ92KQAxaSE_AhadwtI7L_bppVdmKJH7S53V-HhLX_dDkWNW_xUXLqJBzWTlWVCbKqdVBk-HwntKMBoALXdWKvlzHABrLNqKUIcnE525ZZEpEq63otmv3oJlnecnV5iCyTeKOL0RZedU8tbI_auFLOk9sPehPdW51ocRUqgNNUf5UiDegx9u7SK1xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کره جنوبی هم خوبه ها، حالا در حد تیم ژنرال نه ولی خوبه
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77724" target="_blank">📅 17:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77723">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjJvTeclVyehFnrrR1TTtWh927UWzCtHo3weKwwYlE4-mWTolzi7CYUg2SyPW5URuKHJTnb_kHqxnOgLsnSt8igKz-H3PO48tn-DxIVxwEhPahLuo5jFv61zyoKOqLGokZvtMYkvzKmPWOM-QugS5NyyGUGjV8wNU36GeT2zCvEOTCQQf5j1YvGABy8aXS5mEKoy4GXxUBrdWWOHg3Umjkwqp8qObU_YgKi4mBSzNykKk5Zm-DxtORQZ6RP-3B6fA1xyPSwW_C5kTc-UiWyFF_j9FDgrm_puLn2uIPnNr23uaJPY2I0i9iZIRl4ww2mCk1-9CgMY4kM8cNyBifnrbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو روزی که همه ویژه برنامه جام‌جهانی رو با رامبد و دیبالا و... شروع کردن ابوطالب رفته «علی پروین، مادرقحبهههه برو دیگه» رو دعوت کرده باهاش برنامه ساخته.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77723" target="_blank">📅 17:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77722">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77722" target="_blank">📅 17:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77721">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/va_6v3SzGEh9aOlEyjZKWt3OwlCa64ptX7TzSR0Nu-uL5gZ1TSzOLjn2rfdymKlhhcYH8sIfmKJ4zuu-OrS6jm_2y9GF9Xyr-huxZRJ8cia7xxtHu7okxpLgkQzYIhf99EDO6G-LvxOOpTQ_bLq7pBOJwWZ9uYFLIeSBBqksSBirCTlSlav5PUMslXs_Y3ZpaZdVxaaFlYnFkGNYpbXjFFRWZBZb7OZzbgTyALyprwq8VuqQb8XAdl5Gv5NKeJlVOdUrmPSx3rP6mJp2deMdPQjxvybtqljoOh-bJ2VTFFR0LHe_MvRslM7W5wfTKn-8cKk2R40M_i7TIV_wGWxmQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g22
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77721" target="_blank">📅 17:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77720">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رویترز دیروز: لشکر 82 هوابرد آمریکا خارک را تصرف خواهد کرد.
رویترز امروز: جی‌دی ونس و مم‌باقر قالیباف توافق امضا میکنند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77720" target="_blank">📅 17:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77719">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فاکس نیوز درمورد مفاد توافق احتمالی:
مواد هسته‌ای ایران نابود و خارج خواهد شد، برنامه هسته‌ای آن متلاشی می‌شود و هیچ پولی آزاد نخواهد شد تا زمانی که تعهدات خود را انجام دهد.
یک مقام کاخ سفید گفت که تنگه هرمز به طور کامل باز خواهد شد و ایران موافقت خواهد کرد که از حمایت «گروه‌های تروریستی» دست بردارد. (دقیقا کی موافقت خواهد کرد آخه حرامز
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77719" target="_blank">📅 17:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77718">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c4a7984e.mp4?token=XWacPQYgIJBBwGem_7XIWsaVyxBJwVmSZIClwSbViI6F3AC_DhTojFwTHxdA_R-J098zwhxzt6ymuiyfESX0qYPpqn2kuVh7tsZx45je_dmWm2CZp3aNe3mHOA-Wx0mbs_HndA0epk7ITdVpsotoJV6O1oF4KDLazQ7YEuhWu1fBLizdwKsdRV0fgXmfiPDrutLkCqaSHrlUL0t44gMUF1tOXLOXo3o3tvd-N3QJsLwgnXdPnPr8kY6tt50iMX217km6x0SWRKv2hgMbJmf5FzhH-rZB8NuHj34lGHFnWdnCaGKSaODxSiNF2vj23QEpxTLM1EsA7e-J0RNhFsfH0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c4a7984e.mp4?token=XWacPQYgIJBBwGem_7XIWsaVyxBJwVmSZIClwSbViI6F3AC_DhTojFwTHxdA_R-J098zwhxzt6ymuiyfESX0qYPpqn2kuVh7tsZx45je_dmWm2CZp3aNe3mHOA-Wx0mbs_HndA0epk7ITdVpsotoJV6O1oF4KDLazQ7YEuhWu1fBLizdwKsdRV0fgXmfiPDrutLkCqaSHrlUL0t44gMUF1tOXLOXo3o3tvd-N3QJsLwgnXdPnPr8kY6tt50iMX217km6x0SWRKv2hgMbJmf5FzhH-rZB8NuHj34lGHFnWdnCaGKSaODxSiNF2vj23QEpxTLM1EsA7e-J0RNhFsfH0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77718" target="_blank">📅 17:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77717">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ یهو ریج بیت مودش فعال شد گرفت رو مذاکرات و رسانه‌های ایرانی:
شرایطی که ایران به اخبار جعلی فاش کرده است، هیچ ارتباطی با شرایطی که به صورت کتبی توافق شده بود ندارد.
آنچه گفتند، از جمله بیانیه ضعیف و ناامیدکننده‌شان درباره داشتن یک توافق، هیچ ربطی به حقیقت ندارد.
افرادی بسیار بی‌شرف برای معامله کردن.
با آنها، چیزی به نام معامله با حسن نیت وجود ندارد.
شگفت‌انگیز! همچنین، حمله پهپادی کاملاً دفع شده آنها دیشب علیه کشتی‌های هندی که از تنگه هرمز خارج می‌شدند، کاملاً غیرقابل قبول است.
بهتر است هر چه سریع‌تر خودشان را جمع و جور کنند!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77717" target="_blank">📅 17:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77716">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTyczqVsjQQCEkQG9EzncXibTdPFIC3oC_XyriQPuV4ZnZOLM7FxieCZ6tBQ5zsMnIt7IRkl6oQPfLRVfbCVdxfJPneU7-A1ofS1Jo3GNgn_WS7wNrDQ89MszbPgIlT-EeC2dTfhG__527KhiRIEIKmsYo_pkXbEog6qJjb_qoh9v4BmaLxcM3zgMbtipLHs53IMf_XyXX8HJdmL1iyLcj6a5jRmM_QVVAoRmmtS_pxR_QC28Jip_MZgM7jhALu5meiIOS4wh-4e4cJ5vXZI8eL878bhp2WEHt86t1yFxibI3XisLNoMmoCSA10cZvC512o8xpCQZLwiEeRoomU1MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید ارباب سعی میکنیم درست بشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77716" target="_blank">📅 16:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77714">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انتظار می‌رود امضا اوایل هفته آینده، احتمالاً در ژنو انجام شود.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77714" target="_blank">📅 16:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77713">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">من تازه فهمیدم چرا علیرضا منصوریان کچل بود، خواهراش کنده بودنش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77713" target="_blank">📅 15:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77712">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHALY7sYqHE8jAeif6174UhPHyVvzt0t1B8Qn8B9WrLjoVxPsVAr7COBZ3bx6AMt86DGUlTQA7bWBzY1gAiSV0iqXUT7JtfZvCO42iBF-lgKfBXjEgrvFoExmmmw5j19izif0_kY24LaIdi-xrDcZsQbiMuVsKpg3f3odF61k75Ly7KU6c7c8TsR7EzLu2aVTjaSwLj59NzKvKm19BadsWQlPeGLoCcvtxPS1y-RU2awUiDkYFqxuXpJjwlnptzOyTKdtqFAyW4yOUsPd3DHlHCLM9XlzWjQi9mK18JKl-ycowse_Y5KRNjuSGorQluc5ldX89ncE4a5iMA3OGBDFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
کشتی‌های جنگی و تجهیزات هوایی نیروی دریایی ایالات متحده همچنان به گشت‌زنی در آب‌های منطقه‌ای ادامه می‌دهند و محاصره علیه ایران را اجرا می‌کنند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77712" target="_blank">📅 15:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77711">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1716c7017.mp4?token=Jq4-IErEFU3ni5jztmKbmlmi315WzzBnwA6yhHlEEL9-SQutOgHiB-JNy0u63419tmOkheOIWXCrG-3K-KR57AuMMe4ebBJpMlmp3uVHfaWvQQ_NxHKECdSe86xTBFB51vVoliLpK1exhJ9mFffh-Avw7ozbYn0CK19TCtUMP7ldEfdWMrkp8J9PBtf8aU9VYFy0u8fSnZb9op7QF2GnnaLaurMC0zb1brJ4TYfSpkHmcGI2XiSta7Qyd9BkuzCaW1ahoNCSyOeptIYoFcUumriDB9ExeyXaX96odRoGLYTEfU1ute0IZxApq09eu4Bi3oyqpIM4zR0RQhO1RROGWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1716c7017.mp4?token=Jq4-IErEFU3ni5jztmKbmlmi315WzzBnwA6yhHlEEL9-SQutOgHiB-JNy0u63419tmOkheOIWXCrG-3K-KR57AuMMe4ebBJpMlmp3uVHfaWvQQ_NxHKECdSe86xTBFB51vVoliLpK1exhJ9mFffh-Avw7ozbYn0CK19TCtUMP7ldEfdWMrkp8J9PBtf8aU9VYFy0u8fSnZb9op7QF2GnnaLaurMC0zb1brJ4TYfSpkHmcGI2XiSta7Qyd9BkuzCaW1ahoNCSyOeptIYoFcUumriDB9ExeyXaX96odRoGLYTEfU1ute0IZxApq09eu4Bi3oyqpIM4zR0RQhO1RROGWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
توهین بسیار زشت صهیونیست‌ها به رهبر معظم انقلاب.
🔹
صهیونیست‌های ساکن سرزمین‌های اشغالی که فهمیده‌اند کار جز کودک‌کشی بلد نیستند، اینبار در اقدامی توهین‌آمیز یک مقوا با سیمای زیبای آیت الله سید مجتبی خامنه‌ای به همراه رنگ‌های مختلف را در رژه روز همجنس‌گرایان نمایش دادند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77711" target="_blank">📅 15:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77709">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYeuOFIIxLghg9aCPnIvoAGjqIgkSpvdWxIDEcAHAstBBC2CJp30OJ4KAivEEXZZyfziC-Ui-MOFLkZC5CRsK7eVsX_TJzJYphzU9dSoNBZ5CtAe63pXItaDTY8Qfm1V974f_DXwD1mw8y9_MxcWSWCdeEVQyt2v8eJxBASuS6Wvx9HOc7FsePGMu-taipvWcF54vmXEiJhmBZESs2Zctk3qEXAn3QHW7veL3DMRQ1SKDLOoEjGDtVy7KSsVhM8GVwqDfzpdrVIx8bfgRPrhBt_GuMI0RTGEfz5tonrYi_mW6prpH9V91biepDUYDj1l-_t3WYFJ3xiqpvN4GtVxaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#رشید_مظاهری
را فراموش نکنیم
رشید مظاهری دروازه‌بان سابق استقلال و تیم ملی پس از حمایت از مردم بازداشت شده و ازش هنوز هم خبری نیست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77709" target="_blank">📅 14:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77708">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBW9ijgjTUicSpMQEw95ynPPTJXC8g0cp3cUIjxEAFlPzdfrRSOqkkexjCjEAnLcDjQhNshIk7NO9vkLHywwZrD_ng0oiy2ytfQOHc4ZJFh_cSUfL2iT_SkF-Eui5w7Y1ZgNu3veVYx03OaKTSALw9x2U7j1aC0twscPsND1MdZeBdsX54ovfForvpZwMxBgqkhRjCjqpX1-ZZAKAVukJId7w0oPz_0hHtPA4ZWjad13Veyn_fDfgP6DiKEF5K0Yo9XIcMPkjAowUQf3a_ifhHyG-i0WkC3KiO7wG4xt73CVbZofR7xt3UYab0lwgeP_ikpIt9gUxm-J4oNg3RWlBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیر دیگه کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77708" target="_blank">📅 14:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77707">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojCVAsb8VY-J8aIwG_cqOF_DjZ4zYYyjcytDc6xB9q3ryCZ6cD3BH4PyExqJqkqscZUNDXCPz02YDyK8ppQnjx9w9vSlxoM6Jr76mgSV0zXVXsqGN6VbhHzErjCzxPwmM-wtZXz6OuV43E9Ywx9HCGPw01afTlnXvypk8TeBtQ33BFJ_QQ9wgkL8fQXLlqJA-yF2vQuChLuvtYiQhXpOIsXpgUAdeCL94fzHfIUcHhUbp1xS43mEJzwLp_XzRUFKCoHv26uW8JqXnijAW0Cpdhug6X38p5zZ1y3w1vbPlrsJ2ZEzC0uR0LLXF--oA2YBuIvfwQlrvkymXgexdWJ0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیسو
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77707" target="_blank">📅 14:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77699">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اسرائیل هیوم تقریبا توافق احتمالی رو کامل تشریح کرد: ایران اصولاً موافقت کرده است که اورانیوم غنی‌شده بالای ۳.۷۵٪ را منتقل کند، از غنی‌سازی بلندمدت صرف‌نظر کند و از به‌دست آوردن سلاح هسته‌ای، از جمله از طریق خرید، خودداری نماید، به عنوان بخشی از یادداشت تفاهمی…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77699" target="_blank">📅 13:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77698">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اسرائیل هیوم تقریبا توافق احتمالی رو کامل تشریح کرد:
ایران اصولاً موافقت کرده است که اورانیوم غنی‌شده بالای ۳.۷۵٪ را منتقل کند، از غنی‌سازی بلندمدت صرف‌نظر کند و از به‌دست آوردن سلاح هسته‌ای، از جمله از طریق خرید، خودداری نماید، به عنوان بخشی از یادداشت تفاهمی که منجر به لغو حملات آمریکا به ایران شد.
تنگه هرمز پس از امضا به طور کامل بدون محدودیت یا عوارض باز خواهد شد.
هر دو طرف متعهد می‌شوند که در این ۶۰ روز علیه یکدیگر یا هر کشور منطقه‌ای دیگر اقدام نظامی نکنند.
این پیشرفت در مذاکرات پس از تمایل آمریکا به آزادسازی ۱۲ تا ۱۵ میلیارد دلار تحت نظارت قطر
برای خرید وسایل بشردوستانه
ناشی شده است.
یک مقام ارشد آمریکایی گفت هدف استراتژیک تغییر رژیم «فعلاً» کنار گذاشته نشده است.
انتظار می‌رود امضا اوایل هفته آینده، احتمالاً در ژنو انجام شود.
بند آتش‌بس لبنان همچنان باز است: آمریکا مایل است به اسرائیل اجازه دهد به تهدیدات نوظهور پاسخ دهد، در حالی که ایران خواستار آتش‌بس کامل است.
مذاکرات آینده ظرف دو هفته (مطالبه آمریکا) یا ۶۰ روز (مطالبه ایران) به محدودیت‌های موشکی، حمایت ایران از نیابتی‌ها، خروج آمریکا از خلیج و تضمین‌های بین‌المللی خواهد پرداخت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77698" target="_blank">📅 13:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77697">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فوری
پیت هگست 44 تا پرس سینه رفت و ویدیو شو منتشر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77697" target="_blank">📅 13:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77696">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اسرائیل بمباران جنوب لبنانو از سر گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77696" target="_blank">📅 12:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77695">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agQJwzgy-TRObWkyeONh3_cRP7rzrCmRoVdUoH-KoXByZyzN6J_xjCRJGfK92ziv9wmfyX1hDsg3fQZ0Cb1LjZTopVjAwOzTDi0DwLRTdU3fQzOGmtrop70g6jtkt-uxrdANaYaaZ8OKTDzOzjdyC_VjtDKHatkJAvOATSP3SB3yLe1PCmEpmA0vVzLsk8CWm6WJRyzly7gPfNW4UViWCAeCk_d-VNeNiMW18Zi9V4GVJPHUK5jkDd_R0M6_b_4bPV_tOpmwHw_P0eQz5Af33Sc58HDnQG_W2wQK-m_UbeuJThFSZvLHoZgjXl4hR5sfOgDCajyHQ1fCcVnMz5_GPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوشش اسلامی سال 2026
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/77695" target="_blank">📅 12:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77694">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فقط چرا اون پایین زده ۲۰۲۲  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77694" target="_blank">📅 12:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77693">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTGWWZ2eVn60UUZ8qTrxuf-GNWKRimCs4HWJ2IH-hIWqQMyt-gKY9ac88AU2sDw_rLwkEnrRMBNZ-pyRAhzM7cAoqBKjlw0NaC8DYR8Hssh9G1Ehy6g79N9OT5Gk3a9g2XUXrd5HqWb_wu3xynJzSRnrJh-vBysjtdCK7qnT0CBBHFDa168F36t2lSLyGs4dVNmLxbzySTAhiGXGg1kXlwE_eonAK2OO2KMHK4_9M8eioOwQQp_R5i4vtId4L2U--wUG1mjfNT8DcHbXwGhv1-UCxDAK_8YkImlgsWbuOaw2Dr6ppZr0RDFZDzcRx9l1aHgaUeijgvbfuiUx6CdCqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط چرا اون پایین زده ۲۰۲۲
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77693" target="_blank">📅 12:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77691">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWgO9LXj7jxuXtUj3qAPM2XB-Y1bj0L9idazEctk3Xjc2eOS7jSM8AeFpP8vzNh7FYYzt-1e_Zc0w4Lvhd_S_uyTqnBwaSJZM2y_8RAdFtTeowO4fyY5Zodl4EpRZdu05pxUazTW7AqFAPEnWxRTyEe1EVCO37p-Ub0axdju18RYhma-o18-p8Il7RplrkUDS6NxYxm1ytG2veWmN3DEIs_0aByhF7j8zvh3wYrfjx01lURj2UE6mS4k72RZuKwOel2xh11M200ryLkAml2ppF05DtXlaGwc1u_chhsMID9lzDcLtZc9bIH95zVtcJPg1b82JzkUymOVbgikDon4vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواهران منصوریان ساعت 11:08 صبح رو بهت بخیر میگن.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77691" target="_blank">📅 11:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77690">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7o11J-KCInzYjiDZTCiQSQufyt3qDVx2DoDdnO4pCdOV13oHtWgID__Ql8j5nqOXjNidvPX3bLuuWXIvvGl74oWDtY8iGFeU8sI8Jt7sPOh0HdIS039qJ39Mq-FxlzGdAYBL19Z5REGDVKRDBMJhegzJUjE66CKym1TyRrmw9SDK_KXcNhwhbE4AYxgUxGZ-MrD_G5StPViAoxwbuPOsclGF6JQ9W2-UbZvQxX7DY8dwg7l-RUxFPX9A5t-8PxRha9nNdRMipWDuTM2hA3YKhJxVZoqEos-gyZk3UtmNufq5J9gAmM0mSkB_sggk-aRZXHfx_MaGyLlQiETpFnM8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتتاحیه جام‌جهانی
❌
فیلم سوپر BBC
✅
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77690" target="_blank">📅 11:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77689">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77689" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77689" target="_blank">📅 11:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77688">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpQ4vC6IxCSSkBGPGSvEVW66LdKdP--0z0wFzMDdTjD5vYPY2CKnRdwD77dRG9DjrZH0QAtL31Ivss7XmYDIbdCz-FBqd26s1BA_YdpBGx_1B6Hpg0I8waAEsuc97GVfhJFdhAGrpVgAOzRRlayTxuiI3i5HNp6XzGtJ9tVQjfQX-AovmyYtp9pfXqfbW-KHnd3D-JY9JOf9URAWAJ7M8upEG_fVxveFFIY0yUuxsaC5DJMN-GySKoUBHLcXkbBQXfen7sSruVn79jMWrvWIZ9polgEGwmCR1NG5Y_m70N9bmqP4MlXTIxxGrVOxQTw2ttyy-T6VZVWKh1ffvSwWzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r22
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77688" target="_blank">📅 11:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77687">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">شاهکار جدید جواد خیابانی:
خلیج فارس خاک ماست
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77687" target="_blank">📅 10:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77686">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcee0eb614.mp4?token=iwQEDYMq5txYck9Goy2cBgMFYdXTncKNXulM3_Wu95AmquHPElUsK63KZRw31Tu2PPpCyxX-tk5c1juVwaiG2oywong4S96J2ixCkn7iU56U2mODEfgx9XmAaztHCZF2pCCG7Pxi6FrOtdtKvkdvffemQHA0bUWPN8Uy8vML2Lu_fPXCnb7dYDOREkqgIsBqucItB5ABmYSgx2bh2UFktsUkFJkRhJzRp8CaR6OEdQADygrVTxHVRP92xyS0y-PXmKY_dy0nEyf5a1_Ld-loqaFHfDTxgZpFruVg7H1_pTnoTyEEWASE2bDFsx-0GycWF0TcqlHarFYkxHLf015Jng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcee0eb614.mp4?token=iwQEDYMq5txYck9Goy2cBgMFYdXTncKNXulM3_Wu95AmquHPElUsK63KZRw31Tu2PPpCyxX-tk5c1juVwaiG2oywong4S96J2ixCkn7iU56U2mODEfgx9XmAaztHCZF2pCCG7Pxi6FrOtdtKvkdvffemQHA0bUWPN8Uy8vML2Lu_fPXCnb7dYDOREkqgIsBqucItB5ABmYSgx2bh2UFktsUkFJkRhJzRp8CaR6OEdQADygrVTxHVRP92xyS0y-PXmKY_dy0nEyf5a1_Ld-loqaFHfDTxgZpFruVg7H1_pTnoTyEEWASE2bDFsx-0GycWF0TcqlHarFYkxHLf015Jng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بنده خدایی هم به توافق اوباما که بدون ریختن یک کیلو بمب، حدود ۱۰ هزار کیلوگرم اورانیوم رو از بین برد می‌گه شکست مفتضحانه ولی خیلی جدی معتقده ریختن چند هزار تن بمب و بگا دادن کل اقتصاد جهانی یه پیروزی تمام عیار بود چون بعدش ایران قبول کرده بهش قول بده که…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77686" target="_blank">📅 09:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77685">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b774ac8b5.mp4?token=TtWpDHqNBSSCsKJYsifHEszryhR-9zCTchC_t9rH78Nns6x6J2SSDouLCdicMfVfaDGDgQXtI1ejNSiJ-AM7uf1gWEKqQwaVAJOfxwgUBQxOMwxLxcw22gW-lv0N2fTUmP9U2bpWbgEB6dnGfGQZNC2RuwUALibXL9MxRPTAiseyKu7aUUp-rYufOF-9KNrhAjxBjq_JZ32ei9Qx1gWAykwb_6PGBOu6DL4b3E6QwNXRNIKKnLdf_leygzA3Cl8ao1_yEHqPQR8w186Im9PLbfw3OcmJ2LL4Rig_fguhaQ54iPjV2L32rD0jwdAeSkb8FMZZO-V4-9f7hY3wtsWTsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b774ac8b5.mp4?token=TtWpDHqNBSSCsKJYsifHEszryhR-9zCTchC_t9rH78Nns6x6J2SSDouLCdicMfVfaDGDgQXtI1ejNSiJ-AM7uf1gWEKqQwaVAJOfxwgUBQxOMwxLxcw22gW-lv0N2fTUmP9U2bpWbgEB6dnGfGQZNC2RuwUALibXL9MxRPTAiseyKu7aUUp-rYufOF-9KNrhAjxBjq_JZ32ei9Qx1gWAykwb_6PGBOu6DL4b3E6QwNXRNIKKnLdf_leygzA3Cl8ao1_yEHqPQR8w186Im9PLbfw3OcmJ2LL4Rig_fguhaQ54iPjV2L32rD0jwdAeSkb8FMZZO-V4-9f7hY3wtsWTsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بنده خدایی هم به توافق اوباما که بدون ریختن یک کیلو بمب، حدود ۱۰ هزار کیلوگرم اورانیوم رو از بین برد می‌گه شکست مفتضحانه ولی خیلی جدی معتقده ریختن چند هزار تن بمب و بگا دادن کل اقتصاد جهانی یه پیروزی تمام عیار بود چون بعدش ایران قبول کرده بهش قول بده که سلاح هسته‌ای نداشته باشه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77685" target="_blank">📅 07:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77684">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIuA2HAMRFggN4lb3ucaTbVb0clUTiRYeBEjm6WUvEm4YgkVoIo3ISIRWp6rkHNN6q4lM5Rqf1R8ArGwwXcVV8G9vUrZzYU3KsDna5EvnAWouF-r6JMojZphVUJP9evz4h58RjKCpxQc34guaTWZk2p6CLGW0Yn5BLY53LGa0v7AhRaghhVfb_dXHKTmll0Z3vrge-xK5ovwKmnsJGqwNZSsC7CMBog9-LfwT9xg0U1GHRVgSuGUKzF_SSIE8VeCYqJRtIyJ2iiMa943eVqwVUWfgT8l38dxYHenpV1EQHEbCev8ydRKd6c5cC5_Qz0TY-H0bvCH79jUvBA5VUELdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمنا می‌کنم هر کجای این کشور نابغه پرور که هستید همین الان متوقف شید و سعی کنید یه مدت تحلیل و تفکر و کلا اینجور چیزا رو بذارید کنار ممنون.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/77684" target="_blank">📅 04:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77683">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یه کودن زاده‌ای هم نیم ساعت پیش اینارو گفته بود ولی از شدت کصشعر دلم نیومده بود بذارم:
ما امروز جنگ با ایران را به پایان رساندیم و آنها موافقت کردند که هرگز سلاح هسته‌ای نداشته باشند، چیزی که ما بر آن تأکید داشتیم. این هدف اصلی بود.
این ۹۵٪ از هدف ما بود. و، آنها این کار را به قدرتمندترین شکل ممکن انجام داده‌اند.
ما، آه، با ایران توافق کردیم.
معامله بزرگی انجام دادیم. هیچ سلاح هسته‌ای وجود نخواهد داشت.
اه، نیروهای ما خیلی زود شروع به بازگشت خواهند کرد.
تقریباً، اه، تقریباً کامل شده است.
ما هر چیزی که می‌خواستیم را گرفتیم. نکته بزرگ این است که هیچ سلاح هسته‌ای در ایران وجود نخواهد داشت.
آنها بندی داشتند که توسعه نخواهند داد. من گفتم، «خرید چطور؟» آنها گفتند، «خب، ما آن را پوشش ندادیم.» پس دو روز بعد آنها با آن هم موافقت کردند.
ما هر چیزی که می‌خواستیم را گرفتیم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/77683" target="_blank">📅 03:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77682">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">عرازشه ای که میگید آمریکا نباید فوتبال و سیاست رو باهم قاطی کنه پس میشه بگید دقیقا سردار آزمون چرا دعوت نشد؟
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/77682" target="_blank">📅 02:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77681">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDPgtEPaU_2fQmbtVWRFW7jhFJM3JO5OaOT4lRs7SMHjars4dgxmY2U9s2ObSLoXiG8SGkZWBWEv0YBh2A-4TDbBFr0cNoFaY5lvE3kJhzzkvQ9PYdadQS48HE9LXyzLIufpamm50-dx0H_QMdxCiTPRJhE42KdOY3Ug1uN41RQF9LW1K4s4IUw3FJI7DASyfcykJN5JkJSCbnHUhzKkzzPWk_LvK47K0QYzQ8mLp6mgYGejmSkl2cBFtD4TQ0ZoNMZq6G41utgo9cwCcPfZF2LLetZ0MhgWmr0z6VTl_hHWyngjhnG54OxzA46Zzincm700b6xElbiBUpikMuAXVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست ترور بیکینی باتم اومد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/77681" target="_blank">📅 01:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77680">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">میناب انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/77680" target="_blank">📅 01:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77679">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تسنیم: متن تفاهم تا این لحظه در مراجع ذی‌صلاح  ایران به تایید نهایی نرسیده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/77679" target="_blank">📅 01:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77678">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">چه علاقه‌ای به گوز داری مشتی</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/77678" target="_blank">📅 01:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77677">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بازم گوز  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/77677" target="_blank">📅 01:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77676">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سلام فریب صدای 2تا گوز قوی از سیریک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/77676" target="_blank">📅 01:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77675">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFw2-y5gCf4SIVSmu-Nz1bxY34KCJGqKaaf_mX-kApEAPkCY-D7VFa58p0GVbkY99YFZHcejQMddwyd-K5W6KeLMqzFbsG3-aB56Eoj9Xx8SELsyZtvLb1HzdtCLS9MtFpXGZpwmaVcPWv8zthqu7DZBLBOm6klDVJeAVCMuL1nwmnm0ss7Z4Z-CjvB3yHxTHsQX7u_8j9TtirbzfXn_51gY-CjHrcFa5boaHP9yTL7nrSJclESAnQqdVJq7BfFl5u5oxX2gwQsvync-A_cwYkNNLSODZzk9uJEbWZOIwoMlV3UYkwy7C49BS6fsjjOOqaWQ9wGJkXfiE-BCKPTSsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه اواکس هم داره فعالیت میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/77675" target="_blank">📅 01:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77674">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پرواز سنگین جنگنده های آمریکایی برفراز عراق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77674" target="_blank">📅 00:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77673">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گناوه صدای انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77673" target="_blank">📅 00:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77672">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">درگیری ارتش امریکا و سپاه در خلیج فارس
تایید نشده هنوز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77672" target="_blank">📅 00:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77671">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سلام فریب جان هم اکنون صدای توافق از خونه همسایه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77671" target="_blank">📅 00:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77670">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سلام فریب صدای 2تا گوز قوی از سیریک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77670" target="_blank">📅 00:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77669">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سلام فریب صدای 2تا گوز قوی از سیریک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/77669" target="_blank">📅 00:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77668">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خبرنگار: آیا رژیم ایران عوض شده؟
دالگخیز: بله، نه یک بار بلکه دو بار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/77668" target="_blank">📅 00:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77667">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">3 تا توافق رسان KC-135R هم از اروپا دارن میان خاورمیانه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77667" target="_blank">📅 00:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77666">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رسانه های مختلف خبر توافقو میدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77666" target="_blank">📅 00:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77665">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الان یعنی با قاتل
حضرت سید علی خامنه‌ای
💔
، قاتل خانواده‌ی رهبر جدیدمون
💔
قاتل سردار سلیمانی
💔
، قاتل سید مقاومت حسن نصرالله
💔
، قاتل شهید فقید اسماعیل هنیه
💔
، قاتل دانشمندمون محسن فخری‌زاده
💔
، قاتل سردار حسین سلامی
💔
، قاتل سردار محمد باقری غلامعلی رشید
💔
، قاتل سردار موشکیمون امیرعلی حاجی‌زاده
💔
، قاتل شهید فریدون عباسی
💔
، قاتل شهیپ محمدمهدی طهرانچی
💔
، قاتل سرلشکر شهید احمدرضا ذوالفقاری
💔
، قاتل سید امیرحسین فقهی
💔
، قاتل شهید اکبر مطلبی‌زاده
💔
، قاتل سردار سرافراز عزیزمون علی شمخانی
💔
، قاتل فرمانده بی‌بدیلمون محمد پاکپور
💔
، قاتل سرلشکر عبدالرحیم موسوی
💔
، قاتل سرتیپ عزیز نصیری‌زاده
💔
، قاتل عزیز اطلاعاتیمون اسماعیل خطیب
💔
، قاتل شهیدان غلامرضا سلیمانی
💔
و مجید خادمی
💔
، قاتل سردار سرافرازی که بر بستن تنگه اصرار داشت یعنی شهید علیرضا تنگسیری
💔
، قاتل رئیس جمهور آینده شهید بزرگوار علی لاریجانی
💔
، و قاتل شهیدان دیگر مانند محمد کاظمی
💔
، حسن محقق
💔
، داوود شیخیان
💔
، محمدباقر طاهرپور
💔
، بهنام رضایی
💔
، اسماعیل احمدی
💔
، علی‌محمد نائینی
💔
، مهدی رستمی شمستان
💔
، سعید برجی
💔
و منصور صفارپور
💔
توافق کردن؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77665" target="_blank">📅 00:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77663">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه: بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77663" target="_blank">📅 23:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77662">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">☁️
✨
HappyCloud
✨
☁️
🔥
تخفیف‌های فوق خفن
🔥
فقط برای مدت محدود
💢
+
⚡
قوی • سریع • پایدار
+
🌍
مولتی لوکیشن واقعی در ۴ کشور:
🇩🇪
آلمان
🇳🇱
هلند
🇦🇹
اتریش
🇺🇸
آمریکا
+
🛜
تمامی سرویس‌ها آیپی ثابت هستند.
+
🎛️
پنل کاربری اختصاصی و حرفه‌ای
---
📦
20 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۴۹ تومن
📦
30 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۷۲ تومن
📦
50 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۹۹ تومن
📦
100 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۱۶۹ تومن
📦
150 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۲۳۹ تومن
📦
200 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۲۹۹ تومن
✅
خرید فوری از طریق بات
👇🏻
🤖
@HappySmileVPNBot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77662" target="_blank">📅 23:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77661">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAA6--GJGhI9-v0Mdo3S7835oc8YpxuH6KYrS1gmHo-ZwynX4aAqjfXQxK9-keGLqlL8k_LGgJlkWvZ0gkKY0k6FVYzyOrPaKiBnf3PFfPH4eC4laXED0OA931vZRtctxSgaCXBOriigu1J1pBjNC7w7hLHJrnPKiQew16LnUi2HCxSY3mSxcCEQTzCaNY_AoG9WhWHTssd3XXzSocL4b7koTyRnV8IGSrGkD94F5vApqwtUO1b-P2JARV6zOnpWfXUd3cNQXz1_1qUrFcUx_Pf_JoNfMxaW3IIQ2cNxm5wZgw-eo3w4L39R6P4OUWTHYSNc9UG30behbX1HOxASDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انشالله بازی کشور کوردستان با مکزیک  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77661" target="_blank">📅 23:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77660">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انشالله بازی کشور کوردستان با مکزیک
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77660" target="_blank">📅 23:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77659">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromcина</strong></div>
<div class="tg-text">این برای امشبه؟؟؟؟؟</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77659" target="_blank">📅 22:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77658">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ed6deedd.mp4?token=ZLu85d_Xdkpmkh_gOJn_24C0uJzjsyDDdjrQMbxobReIoQp_lru5X1eYfxD7_opFqSCh_eIGQpYheNlhD3jwvi7KBXP_G7lFFy-6hCksa02U8NxYb6U53-J72tPQk_co7XRpKOuMquLZ4m4Gxp7qdSnK0bD782uIma83dr5-YnkKND6UzPHZRyMI5f6yyRbSnJWG0jszNASwR46YvfKHij8bHAcWuTyK6-dWXMA94ftJH3dWoWnYi6azIHW6dd1aXzhOIztHw-oc_JB6-BmltdaMs89eKMrDPrNeOR8ipG3yUEsqEZey18jqAhOHi9z7GnqEOHjeV3ex2D9OGDdSGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ed6deedd.mp4?token=ZLu85d_Xdkpmkh_gOJn_24C0uJzjsyDDdjrQMbxobReIoQp_lru5X1eYfxD7_opFqSCh_eIGQpYheNlhD3jwvi7KBXP_G7lFFy-6hCksa02U8NxYb6U53-J72tPQk_co7XRpKOuMquLZ4m4Gxp7qdSnK0bD782uIma83dr5-YnkKND6UzPHZRyMI5f6yyRbSnJWG0jszNASwR46YvfKHij8bHAcWuTyK6-dWXMA94ftJH3dWoWnYi6azIHW6dd1aXzhOIztHw-oc_JB6-BmltdaMs89eKMrDPrNeOR8ipG3yUEsqEZey18jqAhOHi9z7GnqEOHjeV3ex2D9OGDdSGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدی مکزیک همیشه تو جام جهانی ها تیم قدری بوده و مدعی ها رو به دردسر انداخته  باید ببینیم این جام جهانی هم همین روند رو ادامه میدن یا نه  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77658" target="_blank">📅 22:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77657">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">جدی مکزیک همیشه تو جام جهانی ها تیم قدری بوده و مدعی ها رو به دردسر انداخته
باید ببینیم این جام جهانی هم همین روند رو ادامه میدن یا نه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77657" target="_blank">📅 22:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77656">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">توووی دروازه
مکزیک گل زد
اولین گل جام جهانی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77656" target="_blank">📅 22:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77655">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">جام جهانی شروع شدددددد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77655" target="_blank">📅 22:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77654">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aG0vIPWjjNz01_cgo_1V8ZBVwAVEEluIyv9YTw1UvwGbRXd0BoeL4oKbLmNm4neDZhfSssumOH3eWpYIcKTpnDMrjTemanrXAkwATkf7FS7pEv89tLGmXi14m_PRgzPhKt99A6hx_R-Tq9T1a1dsxtCRHud_bH4QdL6dpefvmtgy7MUYA6a8eTX5K_zUsQKcBbBvWSMKfT1LG8Klbpl9c9MQaNMv5XE4CCtEJtCt-qwBmCs2t0mM-v3QOI4T_XtRmQ1deaHPzzsflscWzFKI42tNyON8xt9R8eSJeC3nskjoq9hy5CIr5RtTK4bron_cjxJPBz_joTKdswAc6aNa1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه سخنگوی کمیسیون امنیت ملی و سیاست خارجی مجلس هنوز نمی‌دونه توافق نهایی شده:
من از نمایندگانی بودم که خلیج خارگ و نیروهای پشتیبان آن را از نزدیک دیده‌ام؛ پای ناپاک شما به آنجا نخواهد رسید و اگر بیایید، زنده باز نخواهید گشت.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77654" target="_blank">📅 22:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77653">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه: بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77653" target="_blank">📅 22:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77652">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دالگخیز
🔙
عمو ترامپ  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77652" target="_blank">📅 21:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77651">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نیویورک تایمز: امیدها برای یک پیشرفت دیپلماتیک پس از آنکه تیم ملی میانجی‌گری قطر روز چهارشنبه بدون پیشرفت در مذاکرات تهران را ترک کرد، کمرنگ شد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77651" target="_blank">📅 21:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77650">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ به نیویورک پست:
توافق مورد انتظار برای آغاز مذاکرات هسته‌ای با تهران «تقریباً کاملاً نهایی شده است.»
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77650" target="_blank">📅 21:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77649">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دیبالا هم از خودشونه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77649" target="_blank">📅 21:32 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
