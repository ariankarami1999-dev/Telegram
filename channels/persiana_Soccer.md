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
<img src="https://cdn4.telesco.pe/file/YOxq070t0dZpYCmQekig9NwpN2t5iSn8K0puPFdDOuw6kYkM-iX5o93MwX78NngB6NM0MupEDeCkOhrk1WYB4Ep8Rc-yVOaJ6FDhhaT6ueRmlY7orW8ZStiwUUYv7ixUXvhDlc9UMfQE8BtvR-xSGDGBDQjc7jdQoLo9WYeF6AxAaF-z1OMkR4Qqhu2K5Z8nRSM2Dy0L5uelWHHXnhZE5YUo8JYWLqvck9Z8d0rOXCwYU8w6OEMoPChu4YUD9vBRNMVcX9KpEDsQ52S2msuZDz1Px0NMuLaDWn9TJCL8_-QI8rf1wYJhWtQmu2EuEy6RqR3lI3NZkxsXR9gFJ9txaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 565K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 15:28:59</div>
<hr>

<div class="tg-post" id="msg-26412">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JL_ya9qYa9YvZ0_XyivYRp5FluuhwpHAXnhq1oM_fPGwiqZECXnyOtO9IZMkWp6VZmyRDdORw1XPg4JdIpYJaOBex46jPmGoqAiPCJNIqsysolmSDcYu5GBX0AxPeBlkQWs0uBgpWWP6dVTYtMsQ9_7wNg9BgD3w-KuLD8VGcs4oL2C2ZWp6qScg0cDX3mVYOsWVFgG3W6t34zYfWT1-OMKPYJ0cReQbc5D6FNO_5fsixmGJUIQazy-QyfogBJuQ2Ce86G2mD12Dcn57io1e4Uxl0t2DuQl4l11XKfe4JFozTm_vmlRRseBT2jiqDkCAfVPtzYCtIpDpC7DQGgp6jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/persiana_Soccer/26412" target="_blank">📅 15:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26411">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZ8sJekuGaGYaOpZXHcCX621hUSr_OJXK5bG6nfMEzb6WaA2N99fev8QDw4JFvvagPQr-zXez1co1C3cZa-HXVXgqzLw39SvEK5IrRDKT5_xDpOuJxWU9zmK52FgYgtPdkSrJ6xMZFapXPEhP_mWJ3jvCY0wtch4rXMKnQFY1ZgpTyUZ3YwOQm05FjCBfR1zVy6oFmcrColOneV1X1RNoisMnBjrgiblraW2C1yyuIOcnN-4PYmpY7HCAplc_MVj9KV0kPaGXV3pSDdQSU8JoTUejCDZtubVTRfRowrkFgE9R51HCHErRgvaaTX2ZXTZfiKuZAfCGUeuAod2asnXVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ درباره آخرین وضعیت مهدی محبی پیگیری کردیم و مشخص‌شدکه این بازیکن مذاکرات مفصلی‌با تراکتور داشته و حتی توافقات بین طرفین انجام‌شده امافعلامبلغ رضایت نامه محبی به حساب باشگاه اتحاد کلبا واریز نشده. ضمن این که نزدیکان محبی اعلام کردند این بازیکن اگه…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/26411" target="_blank">📅 15:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26409">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9e7HbDU0ZGUwELnN9bHO_YaoF1LgqU-hkM0fqFI0DD6v76PA3mJKI1sB9JIXGA3vkfy1a4j7SyEwn9f2EO8UbYOeB4jPUGVq70ZdyIhDQdFJP-DvneSi5q61dT1Z5SHRyMcXPtEeWAUXhhgnQEmqad9kA9IKqV_1s23Q4zYh2tgDNIieHJGOyMy6AA9ILWCFLl7GbKnFABJnp9KTq9CnhbVlgaA0NJWJSwILgPobooLhDYxqrcoM64-1_KjBxmvtdleK0ijrTbyxQapZTNquMhwCcn-2wpRTbDuWRd_VEudQN8bgf7KHXIlUHY-pecDAP-dbee27eOqV8rDRU4erg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اولین هتریک‌ شش‌فوق‌ستاره فعلی فوتبال جهان درنخستین‌بازی دوران حرفه‌ایشون درمستطیل سبز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/26409" target="_blank">📅 14:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26408">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqLTVJdJxc871cs9QskzPhN_1EeRdLBvPhFhoLU_DVfcMURquK-wSf710Z8npSTkmM1Nvv57WfARGvsIXwRDLzYVCPTpUdxhPzmk-J9D8hDsrqJHsraQ4PiTboZbAJBtmIdTYNcgLmaNVEYLvtJD9a1T1xcHpWQTPtgCfrvc2SK1hLKPM7ljYtvA9zhi-n8_q4Cw66wSaIC9lBeO-9eqPs4dUWmXqAbsM0UvgVlOE50eu2FLefHRbruszUb77PYtkeXM57BfCOW8nAUepX8QhgtWMd33p3kBGlIpc2DSLDg2wxOLBQbTPeMcj-xOJMsznE5AvqRmqSHQRMydulWVeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که هفت روز پیش خبر دادیم؛ باشگاه‌گلگهر بزودی از امیررضا رفیعی دروازه بان جدیدخود رونمایی خواهدکرد. در قبال این انتقال قرارشده پوریا لطیفی فر ستاره جوان سیرجانی ها با قراردادی چهارساله شاگرد تارتار در پرسپولیس شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/26408" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26407">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPP9TiCbyugdzsSr0abAsCvia4LlZmboVacJolh3MvW7z9rRiKgViyYjh5SRUWEkk2zujvIpkIGbwaaoIPmSyFqVMClsQazYcrGQUIUNpoeGySGIyXFafQaSRXxMoVWbOXsmZhNNygnrUkjaOkGp2lrvIDgULmWTW58_SE6r57RonH1i_aBQcL0gXR0eB8mLCiw8CGKsEShVV-12kB9YPCbjgp___cdYWxewQUb1ao3UzHT0jGce1U2rfrGG1X4vguHcG6n7mI_n3EGM2ljePsc3qn8lXKfjY4cI0sA67ptb91S1SaNlS550aAeXPdUTLrLRmnqmTFanK-4pRhns6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/26407" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26406">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mj2KPsec5ukmjxLHlh93UiTR5GEsr5pZeNMvIxxo9BIwPboywY1enhk0Qk-CQkOdq6tMmy6QB4ql8LdwyebtSB5_HwMFCapZ0Isa_RwlQjTz8qIMhLNAj3PHU9usegKXfMg2N9ox7C1OUq5ItkXMQ2QPFUglotQGzz5c2vST-6GL76NLqMlNWeZper2YD6AQv57DHItJRpWgfgJUk0pCwRDd0EyoY2qvzWRu96Sor3M2wsGKcHHKCN6U0yzo8N-9WLjGlwPwsdKIDz0Djo-GLa4po6SLrE2Unl6dVFHEDZ2Ty60fxjxt-dgNuzj9wjDdlQk3HFjIdE9M02_57tJGNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درخصوص محمد مهدی محبی ستاره سابق سپاهانی‌ها زیاد سوال‌پرسیدین‌که وضعیت او به کجا رسید؟ سعی‌میکنیم‌تاپایان امشب‌جزئیات‌دقیق‌وکامل درباره تیم جدید او بگیریم در کانال پوشش بدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/26406" target="_blank">📅 13:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26405">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=ubb0GwnhEtS6eg7AmX5TjFCWUTCpiASctAIvkpNcqxzS062r3TF76XQS6ytRfkp_-SuYitzLLkGei_jC2zATMHARpNOGbUq32IEoUAP-bDdIRIh3j4HxXygKKNCrzWqS5sx8qZod1rrOOCJBGw-Ic1CRJSJrbvXzfbtWkBFB5XnYVwvkKJW6DB-Ik-dLfjTKXIWQW0BcOnURbFP-VE4_lz2Q1Sx4GKaYZHnEzsuNgSuspoUWuO3XEla-D4S9lIl_XFyh4-4msC2fAcv7J5qmK8myMl_qNkW3u3LeSOT2uCD1gywt8flxWHkNgPYA4NFcuEiaiWtxF3VJbTRR7tEeZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=ubb0GwnhEtS6eg7AmX5TjFCWUTCpiASctAIvkpNcqxzS062r3TF76XQS6ytRfkp_-SuYitzLLkGei_jC2zATMHARpNOGbUq32IEoUAP-bDdIRIh3j4HxXygKKNCrzWqS5sx8qZod1rrOOCJBGw-Ic1CRJSJrbvXzfbtWkBFB5XnYVwvkKJW6DB-Ik-dLfjTKXIWQW0BcOnURbFP-VE4_lz2Q1Sx4GKaYZHnEzsuNgSuspoUWuO3XEla-D4S9lIl_XFyh4-4msC2fAcv7J5qmK8myMl_qNkW3u3LeSOT2uCD1gywt8flxWHkNgPYA4NFcuEiaiWtxF3VJbTRR7tEeZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
امیر قلعه نویی:
به‌جای اینکه مارو تو کتاب گینس ثبت کنن، با پاریسن ژرمن مقایسه‌مون کردن! آخه پاریس تیمه که مارو باهاش مقایسه میکنین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/26405" target="_blank">📅 13:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26404">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQbaeAN36II6r40lZ0l2nDa6GHCrK9E7ErZmSW0EOnUpK_DCIASE0MlEqtt67-zXxQYzlkV58_3mp5fgt6EkH0dakZuKhg9pJCV4OlHMwmLIAAH7Y41_A66ZXrbV4jX8QEpAq2f08mzAvme7kRb1krMQW3ISrn8rOEGypazcx0yyBvNLhE3RA-gyXcw85XboqyUePHVjkN0KTL5uE8PRlTYFLLtyUxZXFzl0oIm3KK24F37muMLcqZYuRtDGCXW_2SApHwrFfaSumfwpjMgJJ-DxvRBbny77VBcz94hruFLSyyIyGgX-o43z2FuCB4ICRTDYxt6nCQ5xVW774TC_HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دو سوپرگل دیدنی پوریا لطیفی‌فر ستاره 22 ساله فصل گذشته گل‌گهر به سیدپیام نیازمند در بازی مقابل پرسپولیس؛ این‌بازیکن بزودی با عقد قرار دادی چهار ساله به عضویت باشگاه پرسپولیس در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/26404" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26403">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P86JkuCTS4YODiYG70Xdhcd5o9zIVEevQw-GeSfMmvYwngkWwytxD6UonZ7cIHjJJ_DiR7JKnLaufROncBH612DBgNWIwgs6-1bGB61S1A7KcnKL_ohG2xmXw4soDgVP6lKxGRnSbPlzChR0Fmx4CD5jkVyRWS6G8hCCYOXaihsFzrBMygp-lSAKeiH4w2cMA9ai-cJaSUHzL3Z6tR2SP8IiPMEDCMQvwlOtbbc7DOFfp73-FdNezTbtvYuxZeBz7y0bXv1DjywSJuUb6tLwhV7dgwmTo4qTxUoegpSBfn-A-WjjkWOwnwPL5aGylTl36RcVF_SMgGfyUQNS7wxwoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال بایستی ظرف 40 روز آینده بایستی 350 هزاردلاربه‌موسی‌جنپو و 500 هزار دلار به داکنز نازون بدهد تا پرونده به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/26403" target="_blank">📅 13:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26402">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QV83bXhkByfkTCGFl6-OYn7xpH3ZnBzmLszEqqTKOH_LEfdwY7-ycg1SnY3VtQ1-tmWvJL4l9QDPF89etTAGh5Fjbx1tkkGS8r-YtsYM3feulgcOUNF-KkPHqS1yv3EKLQuBEanW0ce4cNN4iT-edn6drEFR_N0sFFjH3AcTYOdLvc3wUUEpC1JB_juIB5xmkJPsmVox7Rm7i0bUsghwIK_SiNwBBOMj06TQ2VZjax8oze7PRdL2s_TSb8qBcifxOgxWqD0_CEKC0fClCFzTAooTSfnQ5RQFfYZLIACu6gYGpaxfztvfdS2ZrLMEv2PJhyLysck47u-T9iwL_aMipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/26402" target="_blank">📅 12:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26401">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=EOSC76St6nMtLm5r8bk7W1--8qpEblQ7Zuuk9hDWG952_XUnHnFEG34EbqBX7CmC2ZCc95jjg_62MHWrnCGsRJTRPTgQPue0ML-ZktQHGMEspdGCrfQu5kt8wdDnvCHySCrREen3Wmli7SJB4gr1tmBSR7tO78TjfUQWrtbLUTCgCTCzSTqMTvPgbQ-oRe1mLtuINnDYySkQLIjYFMj36H1S3-gMg0SPJVjHMTb__pxhbqhJkMpZbNoVTGRiTreQWbe2QY2bXgBXa8mlE-4KbGRC7wKnn4lISgT0Ge04BwJvMd9PibX7orQsLVaY9ZTmYLbm_LSIlrj6VpZCmOvQ6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=EOSC76St6nMtLm5r8bk7W1--8qpEblQ7Zuuk9hDWG952_XUnHnFEG34EbqBX7CmC2ZCc95jjg_62MHWrnCGsRJTRPTgQPue0ML-ZktQHGMEspdGCrfQu5kt8wdDnvCHySCrREen3Wmli7SJB4gr1tmBSR7tO78TjfUQWrtbLUTCgCTCzSTqMTvPgbQ-oRe1mLtuINnDYySkQLIjYFMj36H1S3-gMg0SPJVjHMTb__pxhbqhJkMpZbNoVTGRiTreQWbe2QY2bXgBXa8mlE-4KbGRC7wKnn4lISgT0Ge04BwJvMd9PibX7orQsLVaY9ZTmYLbm_LSIlrj6VpZCmOvQ6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
باشگاه هامبورگ با انتشار این گل دیدنی مهدی مهدوی کیا باپیراهن این تیم درفصل 2005 تولد 49 سالگی اسطوره باشگاه پرسپولیس رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/26401" target="_blank">📅 12:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26400">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyvyD1_33B0htX8BHvXQR7ABEALKSH-rrzRyGf7MkRkkfmnhLQAS704ojd_A5GXGogyvFC2dusymphFf2cKxof9Zv-Po_E16dTI3arg5wnYd4UA6-COzQDUixVB2Lz77SSVtEtV3rjG7S4zgTg_xuxsoUJsfjOqXCLY1C4BmW3Qv43C34zwfvHoEt_PrEkMSiXNEIw58oEvXMsrFib1km9dItKou9fV2DeFQ0IN0wuW8Rt5JFH_hWL5BPDHaLUOKpdi07p0P3cKZNbPd7I_fHMH0JJUiT2Ndd1GcW15vorFilaHYNCjLkAWkHx2DUC1Uwm4I7YsZH5GbcTNG_u-Nkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/26400" target="_blank">📅 12:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26399">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=mvqAITOQwsSvaOLZ5JWH2j3-zcuEmlndL8MggZB2EWARattgRwFIsH4WF7SS6cUVQoPqF9cp29vA2WbrczGUKl8HrtHrUwlG_MV3tOyO_RAcD0C-to5Qcv3WZo1xnN8VdgTrq-SqDu0-p92gMgSDrABH-SwGV3oBEIlYZi0CH0ZNHin6cYqzkqS-gybEgKHRNzzOBvnCqyJJxixDtTH-lUMlVzuV8AWP_tqCbjSqDeUUDZSAelIUd42d8etYitiASSfp5a3KREkhTGxbjEpImKXWDKs2nRbivh5XdG82apb2k8_kK-mAj5ONJcZRQJzLBI_xYlI-V3rp-Bix6y3neBRsu521zSxN_8an_hFOGlTsLKSSfCQwIjNt8yuckcUpRM9mP9egLmookZDaMsVF1ZD2OiNZ1EvAqt4-GxXV65O4lVclDJU9lBAFavympiKdRVJAJ15sASCDtb2pGfNX3TriXrWbBAt_Opekpob8L-2sYI2QxnU-_BeWDxFLkOOLJYjf-35hXjwQikzbAUOWS58UAfxWkpxrJ9GoocH-3Pifufda0BkPMHU0IPSGuaEMUy4d9aeWT9uJs76s4GtDBmvg1TZKWlxj8aB3IS8b3dJnKFS5B2HUMg6SAICstjc3prd28v9LTZBpD8zUe914jP_z9SRF8hlDgvDuhUM4bDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=mvqAITOQwsSvaOLZ5JWH2j3-zcuEmlndL8MggZB2EWARattgRwFIsH4WF7SS6cUVQoPqF9cp29vA2WbrczGUKl8HrtHrUwlG_MV3tOyO_RAcD0C-to5Qcv3WZo1xnN8VdgTrq-SqDu0-p92gMgSDrABH-SwGV3oBEIlYZi0CH0ZNHin6cYqzkqS-gybEgKHRNzzOBvnCqyJJxixDtTH-lUMlVzuV8AWP_tqCbjSqDeUUDZSAelIUd42d8etYitiASSfp5a3KREkhTGxbjEpImKXWDKs2nRbivh5XdG82apb2k8_kK-mAj5ONJcZRQJzLBI_xYlI-V3rp-Bix6y3neBRsu521zSxN_8an_hFOGlTsLKSSfCQwIjNt8yuckcUpRM9mP9egLmookZDaMsVF1ZD2OiNZ1EvAqt4-GxXV65O4lVclDJU9lBAFavympiKdRVJAJ15sASCDtb2pGfNX3TriXrWbBAt_Opekpob8L-2sYI2QxnU-_BeWDxFLkOOLJYjf-35hXjwQikzbAUOWS58UAfxWkpxrJ9GoocH-3Pifufda0BkPMHU0IPSGuaEMUy4d9aeWT9uJs76s4GtDBmvg1TZKWlxj8aB3IS8b3dJnKFS5B2HUMg6SAICstjc3prd28v9LTZBpD8zUe914jP_z9SRF8hlDgvDuhUM4bDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجینا وقتی‌ کریس‌رونالدو بهش قول داده بود فردای قهرمانی‌توجام‌جهانی مراسم عروسی میگیرند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/26399" target="_blank">📅 12:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26398">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUI-spun1GbdK8_K3EjZNthOtlMV_Ln_cIYaP5C2ZiAWA8Ud7nTyznlBiBqMwmVQBbD-nhdgByHFMT7-qf3Y_QHx8ZgTJE1fCyyGjavCrxtl5T4MdnIHWhQJemKGS9aadVtiURVjKxd6rELxCgJaL9zHe4QH1UWh5voFKzWAlWB63xtqlR9e_MEtyDz7hVA3XRbDnMw7ARSAg5yt9468QpR5yuE95W5qY1SnOrdQYO3aaJyAxuhSpTKmgoXqAqMEi-3YSWe8d6lvNFgTQiEbOZWXZ4YH-zNgNIqZmMn4jDX2COX8YESk4kM8GcPXYQ4O1TDD4jyiqWebDYDEHxqdfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دستاوردهای فوتبال اسپانیا در رقابت‌های ملی و باشگاهی در قرن 21؛ بیشترین قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/26398" target="_blank">📅 11:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26397">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kj8oAPi2EQf0CYUOceZ90DqI4Oh4TB0i-dowcStoCGRLiA9cqyiunK8aAYya4h38XumcYm9SNXdo1_PY9XIy4miWQcXjOF-cubejdeYUSKK3046p25kbaaAR5Ru4cIPNHeY_32gIN1zsHNsS4Pudk-iGoQ_1IJjft8cYn436ZrxcrGoiQ1lY8YAeBHrxkphsE9qwxJao0wwzwLkgTIC-bpZmpDHO-mYB46_KsbGNvx9MSojlU_OKEWW0SXjG6yCKxtWqFayiGjUqQ21zgJOdsne4ob4KFrnc3wB5YDKl1zLgrrOM3pqGBwY2YPQnb91pKcfp-Dai6PoPkJlta7KaXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبری که الان رسانه‌ها منتشر کردند که یاسر آسانی روز شنبه هفته‌آینده وارد تهران خواهد شد رو دیشب اعلام کردیم دیگه. مدیریت باشگاه به خودش و مدیربرنامه‌های اصلی‌اش گفته که شنبه بیا هم پول این فصل رو میدیم بهت هم باهات قرارداد بلند مدت میبندیم. دیگه باشگاه منتظره…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/26397" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26396">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t32oM1m8k6o8TlavrfrB1X1tTukTCUFgrjFJWMaVts8OTV5LLBkWf1B_b_yDziyGSuTKpFD7gwhY6LliuvnflXEjL6eQWQb-gsTSUBVIRBRsq5oud3mphV0eyLaQmbMAF9gez_oulquU6zE3tW3LoV2nHmgs-MAbY1zvZhfhm6OWwRThQHYFgAytYOtHwVo5fk9mkXCkjFi-JD90NVFqrcW_gOHKh88JRZ-EDp_n-_K2FJQ0ARbE4_vlGeSax8qqAPpVgPjvPXS1mNxpLy9ZJt_eYwPVtB5g9D9X7oGghWr8skZR9D-ChhSGTYKbUYLDot-I6gl_AlwtXonL6T-jpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون‌فوتبال آفریقای‌جنوبی در روزهای اخیر با پیتسو موسیمانه سرمربی‌سابق‌تیم استقلال در حال مذاکره است تادرصورت توافق قراردادی چهارساله تا پایان جام جهانی 2030 با این سرمربی امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/26396" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26395">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swoM_8xnreMr8100hBOQH0ZfdzOHMyMO-hj3JJlH5qVpye3Hg3cHxJ_Lfgn6k866QraaqgGKAFl0FdHkhckQ0CtrMkMoDtXn8JT9MMidzsRzXIrAqQdW6_MGLcXLSFW_To5pdZcogqZqVmriF8tfaX86rzKGch2OYGJsD5Z6D3s1dXGoDvGfTeU8eutFUcTqb_S43zywa04SnOtHDw7aPgtJ-WaXDVgGrFVxu_9IKxxMBAGyk1ya6BXoBaBE0Ys0OXHoOdby9Nqdq8PCMqZ6iUpdn4GNKz1hXWEUxEsASThzCiAeGqSUIfcDc8W2mUJmoAj7Hui-MdqDJBWzaib_vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
1️⃣
میلیون تومان واریز كن
3️⃣
میلیون تومان تو وینرو شارژ شو
🔝
🎲
سوپر بونوس
🤩
🤩
🤩
درصدی وینرو
🎲
✅
مخصوص اولین واریز
✔️
🎲
برای اولین بار در ایران
🎰
متنوع‌ترین بونوس‌های را در وینرو تجربه کنید
🔊
با وینرو همیشه راهی برای برد پیدا میکنی
🎁
🚨
اطلاعات تکیملی بونوس
⚡️
✅
✍
️
ثبت نام آسان و سریع کلیک کنید
✅
🤩
🤩
🤩
کش‌بک هفتگی
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده
!
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
r2
📩
@winro_io</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/26395" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26394">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrOLJ_HNg4QorUs_0hze0V7GxUumD4Mk6IRRXN8j4xRYSsSkz5lym47qtFZyt1EumjxJ0JKaHmQqVQQXc40XFXvvLKsMcx8CmQDPcFfJ9zSLSh_WTjVTmcK49O1iA6Q8yBg_FKogWyTyPCXzp1CsFtNPtW_htBHXXGfozXReEPaHOAmp8os9sPSOQTVlpPSOsqpbwd0CJSME1LST3VwkDaunXOWiO56JcvoBQd_iXPei-q7CGyHXQ1W6gh0YL8ze94hHyecWN_qdICdWBsd51H0vcUrzLUcWFfyjt3thFP6dKKIzs7RGjdM6nr8pBcCXRdU5tjcln8vRf6Ris68waw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/26394" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26393">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pmojt7hyWGPFraUZ4q-FWXjsJOgd91WQUxO369ez33Rb6gD2plyMywgScDxDt0bA5ui2cTB4alkcCP0wy38sXSn5RXnlH1ZF8Rmgzxv6h_zJrC48bFG6hmmL_VZrO6H2mCxGMmIeERSFuIVdJd27rT_tjOsqe0DpsqF23Jjtl_1EQhE3PMI11qd9WKioLcOdYdRWv6LUSm0ueBSznhueh05JsIp23zJhepSvMOOgANLM6JQM6XOi-hbEPvAnfw5if1fOqkm9kIx09zPJLFGGBmz0YGpG6RR4xaJB66JAtTlhVrTNzYXJyoR-9VrWgfEuIRejYmDlOOzToLVjbxO3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال صبح‌امروز باارسال‌نامه‌ای به مدیریت تیم سپاهان خواستار جذب محمد امین حزباوی مدافع میانی23ساله‌طلایی‌پوشان زاینده‌رود شد. نویدکیا سرمربی‌سپاهان به مدیریت فولاد مبارکه گفته اگه رقم بالایی دادند مشکلی با فروش حزباوی ندارم.…</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/26393" target="_blank">📅 11:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26392">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdWUVoqjWY-b3rOEy7hbjrDruZjULMBKn5PTyDL-Oaca_wsMlW72DYYCjqyXhfZCYyEzpWINFLW4vJaM9XXR3VJnHNlM40M7McaSzVdalhNlXrrFtP6LG9JSWu33U3FQqNf2T3ZKOsp1N3garWiCsuqnunL6u-Vl6N3YEusbe0VbUMx4xxakNxPNSs54j2pUAYbD8HGjhZGbT_ids6s7frebdWSyF7CXXL6MIwyMqltmndmwLMEhwO_NYlbCL4zdCeRi6hDPoomVvD1RkAFNIpfLG-8-1jPY2fXx9oUz30JS2JXLm-lQpADs7HPrA6v53foStMFWQ74uoCovyZWBYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/26392" target="_blank">📅 11:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26390">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDHQ7N35JbBIhPt3J6T5s89hTBNit8hUrYpHx747j8mkKwHe4DKMq_B_gCP_SVKM1mVSqtLtWAAKd-E5EK2DlbZueL-P8WyVDPSu-lwChAGs2gtSFAuTOXx7eQd8unl1Q5bqXDHUxk_BCAAcar_PJjzke0C_VsI5GBghvMnm4reOSztcPsy-5qXnLNvUILwwc8wsYOrIFmImJlFjlxsSqqsWfSB-hpOQ3hZVGo7J6k_su10j_aOBMvkOpVGZmdNNZREH2uzxbT2DObr8cH0G0fEntmCdyTqjLg6bb_JspT6MWZU4HcKRypmM0AFcuTR12MOSXWtw1PfmHfSOEP1tgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bafI0AUhrdh4oop5OyTbv7ieB_uCy-vra3V3zR80ssxge8RUQFVUQK8CVNi_FUOSTbuoOG_ftvNFt6kKLFm3KIcOJsfeOxlkUfZMHTFbCN_epNp4krIoAp_M6GwX4eRUn0tGdx3M4WrazW7G0Z14qtA0mXCGmrbPDvJPkdPgD4aTnQMLcF5j11WoKhDcVFwJ4NjoAOEe33XAf-NLqcDTpxXlch-hXH-qwRqh9Oxqs1pS1wzCpah9DslGNdJFr751gzkbZyc7rTW1BTdSylJ7I7Nr4re1dDrsQnVOBq1hCJdfUnlpA4sSw9c1xcMgG6slO8jMTJsz27x_UXykWkEBwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی رسمی باشگاه رئال مادرید از کیت دوم کهکشانی‌ها در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/26390" target="_blank">📅 10:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26388">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G-HGK8fXC8_8EyN4JgPJ4c5nh56YK5Imczf7Slekowi1oNOzZMiVVShjKTIdViWYfanMaHQaCdcT_poJpNXy4fX7Z3SqppAANWOIWrQybYLDi3tn164XBJ88LcVFWg42-uNsYm_pWtgpx3B2IrfDkigy7ZwhhythbNOyQ1IAkCOWnU8KG4cAoTZHFzqVo7TorH6Cn_F0N6uLjChAUSX2i4_POx1ZLOZSX1IEU5GadlW27CqBNLzQAIAV8y0j6d7FE7fKoD7cl6vtPA8uE_t2bC6WkR301mtpB6VDnsKDFPvkDJnOFBGU0zTu7EuW6BFrAT42eMLow2gJ9hq1uYdppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTqJ9chgkRZKg5mxehSFvGs_ta3VLcvUrFG2MITsDA2wBGNCZyU6Imum_JUBbeE4fHjCcpflaT2_-uwrC-Af-iOttLnJQ4XlU--eQO1oURBMbsxo09y3QCfFs0JziP1WnlbJl_UBaqVKMr2fF3YXHiakxZoVHR98c3r1mFGUNgZ0nXrr-EwAslHqksYfKhvDxYgDkhGEVIUQnQA6cZMvFxnhtussblLpAHqRGBIlc2DYKVvKBDsQbSv7DV3PKBQZnFB0nNg_49XhbVJTnVYG5Zi5GfMTjoX6tpXzVKPPoLdfGy7pQLcafAlt5-5HpYy9nSQy7l1CSc2WM7Q9a2MycQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ارزشمندترین‌ بازیکنان‌ دنیا بعد جام جهانی
‼️
یامال پس از قهرمانی جام جهانی 2026 در 19 سالگی و ارلینگ‌هالند با درخشش در تیم ملی نروژ در رده‌های اول این فهرست قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/26388" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26387">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjjch_iZCUtYk1oGIuFQyRsGw8X2FPszXJYi7AOrAHbHA1R-du2bFJRZmcAPcD0lnXceURWjdoBmVQM0iGkk8q-WwMJ2UrVfIr6q9g8B6RPOqJrF5XcGHi4vKnGEOXFudi4eZGxK9maAKEJneWT6Lihdg7J_z5-eOwr1HycNndij_CEGaAyJwizjT7Uvpl1gNS_ghCMOhySXctcPvCYoSfAyI5MrNrw9spO41XlIJF-h_qqtJ_bVPxP4L2qWyKEbcKhOYSYiBuv_iXRCV7aaQl6j7e7htg8yx2lf0QNq-AIEi0EVFDog_zbH-e7_vkhiORy7mEx300pVVB2qxq8twg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛ علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/26387" target="_blank">📅 09:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26386">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STCix7UQleNaCEwRbm6zVQdaXo6pJ3mjEtKcnpmW4VL3SLuS6Ts6tGfQpfR0N5335B0mnMelh7hMg27PTZTEKgewp1ahitURFiz3oQ0G0IOXbKLgIybtVmlA_4iS5NinUFglTca8k1qVcFVdNVVKyq_jEopV3QVp-VPmgJbIdz7GRtan6RBoPEv5i_F2cGUEVf6uF_pQImWRJD1nkUct_T1UPGs_W5BxKqcXeoCfhX2drZdDR_9hpQZq2p5z7XNNt4CKFvQOPxvN5WWd-fAV-kN1kuD5gqyX12iOGipsk5YA1UEDa9xz4_C10EmOk01adNF-OXVBlc3jWk7WWghmPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
نشریه‌بیلد: کیلیان‌امباپه به فلورنتینو پرز گفته مایکل‌اولیسه کاملا اماده عقد قرار داد با باشگاه رئال مادریده و این فرصت رو از دست نده و با بایرن مونیخ برای خرید این فوق ستاره جوان توافق کن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/26386" target="_blank">📅 09:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26385">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naeksJRd-hGzgzDlHoemfxwYxIn_zmNSMoaH8R4_OqYa5LlJgjcum9mC-jTGZm70oK_UA198FcxPMp1BQ7AyGzGMxjUIRCuUZz_LIn64U9oC1vpZfbvsT5K3i44Ga3rqXh3_JBTDbgnB8HoT-nQQjNHPfDpDRx31PGsCT6RFOQY4osUiQJ3yoIqsFlvy2py5OInWcS1dJsy8A5XueNbpUOx6UUFmSN1Ya0GfEq7oqodwzSstREvNZ1Veb6-8kdt7UjRwZqovapWxNGw0A-ZnJYIlaLY5dDDBG5EEyymIf7L4T_ogCW5fKY0vFFeGPW46NA-serSGtUkkvJOUcOKIBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛
علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/26385" target="_blank">📅 09:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26384">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJsnymRtjoH_u8sw3vxey5aR3O6Uwhxrgj__sxVKN86Zp2C6T8LPBzga5gzrq8whtttgIxrGmdgOC4BR3kHCAZkxkludBb4yjPA6tJwZHRSAVJeNcc4EvxpjpO9lXd_N25BKqykpYQhoAv4tS0TvAmZPI_l3yF5wGyqMnlciw8mUM8BBsCMtpUYCKrqF-y5hHUTO0wRghzZoTJnNpK-WE2yhfz6KY2xtj-Rc3kZthURt-jAzguCEGWeY6wpXl0FkHeRaSYhuGUopS9XWrpTCDjg9jDtYd6Lia36mi8Avln3Q-3pm02g5diK9mBGOJAEjN06V8G9OOUBEu2y3fvujRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌پرشیانا؛ باشگاه پرسپولیس برای دانیال ایری و کسری طاهری دو خرید جدید خود نیز بلیط ترکیه‌برای‌اضافه‌شدن به اردوی سرخ‌ها نیز تهیه کرده و بلافاصله بعد از رونمایی راهی ترکیه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/26384" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26383">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">📹
مهم‌ترین و معنادار ترین لحظات ویژه برنامه‌های عادل‌درجام‌جهانی2026؛آخرین سنگر سکوت نست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26383" target="_blank">📅 02:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26382">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=WsfILwm1-SVPByO3DQZLygdtKpDIzyzAcQpe3pRUk4JGBDksnicWlocf7W_ApX2Zi_27nV8IZU1ERxMCQ1R0uDZdG0t_Wa9lUo5Tds4IWpfgxSPGUzkyI4GMId6xZfweMNsrU5hFzvwgpJUuc4rR8X6k9WMOoCDqQ6DGjqotXFYBAYQ-NHelEzpX4P39jlKIg7SZkQbJXkNpklgBieTfy3xsSdR8BLab2wrT1iD0f7570UQjdWKJZDt_5lQTtmW5USBgVufwlxaDlJEHXry8bAf7I_gBd_4aN7uH4oz9rF3cdmSMP39nyEifCvm4rnTjPgrbIFUBHAiXWG5Aj-4Eaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=WsfILwm1-SVPByO3DQZLygdtKpDIzyzAcQpe3pRUk4JGBDksnicWlocf7W_ApX2Zi_27nV8IZU1ERxMCQ1R0uDZdG0t_Wa9lUo5Tds4IWpfgxSPGUzkyI4GMId6xZfweMNsrU5hFzvwgpJUuc4rR8X6k9WMOoCDqQ6DGjqotXFYBAYQ-NHelEzpX4P39jlKIg7SZkQbJXkNpklgBieTfy3xsSdR8BLab2wrT1iD0f7570UQjdWKJZDt_5lQTtmW5USBgVufwlxaDlJEHXry8bAf7I_gBd_4aN7uH4oz9rF3cdmSMP39nyEifCvm4rnTjPgrbIFUBHAiXWG5Aj-4Eaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درجریان‌مسابقه‌مردان‌آهنین‌یکی‌ازشرکت‌کنندگان هنگام تلاش برای‌رکوردزنی دچار پارگی شدید عضله پا شد؛ اتفاقی‌که باعث‌شد ورزشکار با شدت به عقب پرتاب شود و فضای مسابقه را در بهت فرو ببرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26382" target="_blank">📅 01:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26381">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTrupWOlelBiIma3QakMOAtmyMSEEfdtti9QFry5jHzC69obdKvtBJMLZf-7Im9XNAg4PLgvI8mZL42RBqigm288WKe_zy8O9Lk5_3RYq9j2Rc_QKpZ5npcuU9w1n-Y99Lsu6wSOlKfsU8zsd0ZPRrgykPoyJg-UiyOUpH-g-midr_mJBMdddljX2S8cLW6Tpu2JJk8qTkBBOnlIjcdYHKCQO1hMsugnG8CsGj8s--DiSpo-htVkSl3noIM9IisHc_1TLimYn93nAAeadsMrfkvo4LlUywxJyJ6gW9WpklBLXMnerE-nl74xZAVf1E73CMszcj2CQUideJ6ayk3eRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26381" target="_blank">📅 01:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26380">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2kd_Ifr9qJt6xJqTn3EcWHvBENs_S_SCh7d7tj4qc7A6NWGEoOL3IDui5GDUHclpZsGakkj-Ra8LcQMItO9X4N_RPd7MKWGpFPwrZa9Mhxa-F7FuSIhS6O72mGrST9NzesSei9IGhXKMO5q4yf19v25ZPyxWv8NBEWTFGWz9NXRllMsw4VcIfbnUEyxdT4MJZnNqdJl4fuqVYZnPuTesDzIHpd70dXC7tbaGgBPfcS1d0D_ae8LXGhTzd8ewTAQLpEmljC78vLfM3DdsU-qmt1E9IXqyYgQHXOKYMeHwYzicDmgO8ShHB6rtpvurvP8Scd6OVX8RdFQGg1pIQvVxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26380" target="_blank">📅 01:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26379">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrP9EAovq5V2h7y9XgBHBRTv2tcfFEwm4l4GwSqLCIv4oxJKltGUtyS4CJg7O9qdHiau_GebKaq1h2Os4ytRENw5yCX4CuJeuN_QJqpFiJ1_vk_Qa8_xZad4N6zYP2-pPPE_fyETtJDSoeV2y4dgnk285DEjq-Rwf2nwGzDa5KF9PtpqX3mhPjDQ8OhGLrUIfCfCJzG9ymlORGdQg5GGR5zo53M9DleP2CFxcs_rr2Lh88ARKZtHjldrwUiQQV19-HTan6Fy55moCpx4jhViFvCKAykZh0d7FF4MdEwuEQ5ACHCSRjveEn4XyfOPY6rtgzJBAplQ7i5g_ibXfF3_TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان ظهر امروز جلسه‌ای دوساعته با نماینده مرتضی پور علی گنجی مدافع 34 ساله‌سابق‌پرسپولیس داشته و مذاکرات بین طرفین نیز مثبت بوده و احتمال اینکه مرتضی پورعلی گنجی بزودی با قرار دادی یک ساله راهی این تیم شود و شاگرد محرم شود…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26379" target="_blank">📅 01:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26377">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nb9HZ5mVZoXGg_IaMNXvgQdVRv_IPnBZpB1e3RiQN986pkzv5sjU1hvzTjxrov63OFyhCsnlhSghL7Z1ii-YMrDVlho-wRp_Aarmh0MPsdFBSf8LsS7xaenjGrrmvDlTE7i2JdLy1wO9gYitH-3wBVtIs0VlLfkBzuGlbSO0SocvRmCDb3cwnSrn48-FWNG5u7xET1xr4B6HJTLNeKJBX5wW_A7b7mxZSWZnFr9rJheD7suYS1Pj84fZgHmGYdROUGLjqA7kg4Wcu2a34aFaxlDnckzZeq-6lsPioK41jkz3kxh2vjWKTRVkfmNFJslyyUyAfi_Iy6uFrCVNV98uGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
لیست 10 بازیکنی که در رقابت های جام جهانی 2026 بیشترین تعداد فالور رو دریافت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26377" target="_blank">📅 00:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26376">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a867be5010.mp4?token=lPtE7_h3swckuiCxhRLVFsj4NDceTwA5fJllxv79inqZ_I3oAGQfMJB9_PPbhs7ob7lilTnbQnznRLPtI_oK40WHtYksaT_2turNJwoOS9CJM1v5pfITCRxm19GGOiD9obXlGSaQuugwMUPWIGC4QZXYf7l7O5ySlYcwfMW-PGB6rA193P2qU4eGeVysgi6tRnVoz-s2iHHqJW1KSsrc2bU04H4ZmOe7ZnhhSuhpd-hcIMDWBPCaxSPea5zu90oJVuv56KPjeFCr9Rf1mPRUVhYhiGlS-2xxwr3c4SZWCS2yl8gw0GaVERFrle0_bvKHzmy398BU9cqxMbFkLccQ7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a867be5010.mp4?token=lPtE7_h3swckuiCxhRLVFsj4NDceTwA5fJllxv79inqZ_I3oAGQfMJB9_PPbhs7ob7lilTnbQnznRLPtI_oK40WHtYksaT_2turNJwoOS9CJM1v5pfITCRxm19GGOiD9obXlGSaQuugwMUPWIGC4QZXYf7l7O5ySlYcwfMW-PGB6rA193P2qU4eGeVysgi6tRnVoz-s2iHHqJW1KSsrc2bU04H4ZmOe7ZnhhSuhpd-hcIMDWBPCaxSPea5zu90oJVuv56KPjeFCr9Rf1mPRUVhYhiGlS-2xxwr3c4SZWCS2yl8gw0GaVERFrle0_bvKHzmy398BU9cqxMbFkLccQ7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26376" target="_blank">📅 00:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26375">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=RcrYCEngIwM_Oa52vZ6w5adFozSB3uQNovg9UbFFDZ9gKhUh0YPE7ViAU58p6WE6EMZoh8p3nShomhQ6e8MhzuitutzsxQCuiQ4te9xxBAtICce58Iv1qGBa63L3TwvbpfmS06VqjX4ihM00VkUVwvlgWXMyM0hYZySaPNutpynBE1D_VqjpBmP-Mup9VCEUaVPsmTtEetjawIF2eDJg_0oEyrLIMJSJvtjpCGoDhzXpHmX0zotxSSV8ZWudV-8qI2VGSQy5mMr2GvfV0fZTwdvrhjNjdSOUeJBuLgoZc1E0JpDj3WRmXfd-yiBWOUFs5_Cw5RmTPZk7rhLBXudspQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=RcrYCEngIwM_Oa52vZ6w5adFozSB3uQNovg9UbFFDZ9gKhUh0YPE7ViAU58p6WE6EMZoh8p3nShomhQ6e8MhzuitutzsxQCuiQ4te9xxBAtICce58Iv1qGBa63L3TwvbpfmS06VqjX4ihM00VkUVwvlgWXMyM0hYZySaPNutpynBE1D_VqjpBmP-Mup9VCEUaVPsmTtEetjawIF2eDJg_0oEyrLIMJSJvtjpCGoDhzXpHmX0zotxSSV8ZWudV-8qI2VGSQy5mMr2GvfV0fZTwdvrhjNjdSOUeJBuLgoZc1E0JpDj3WRmXfd-yiBWOUFs5_Cw5RmTPZk7rhLBXudspQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
عموپورنگ امروزتولدمادرش بوده که هفته پیش به‌رحمت‌خدا رفت. اینجوری براش تولد گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26375" target="_blank">📅 00:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26374">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQBqP45sSz7VTfvdYQoP1BjaeS68xQ6bs0-Yls4s6s6hxQZojnWbaOmhRGRC3yzseYEvQjAfjT5digXmwEiQnK_c1W7yHcwBUapc9RmHQJAsB-EeRjlFYpXS4rEOcxz06fSzugshWUSgsvj2UsmhEnW8AsxPdeqxew6ppuoehV7gp6Xs0fOxIWYMHxL8cPsv7t92a3r0QbJUy43jzA0sB5LxhqNt_xfHb6_lJTh7WAiR7kpLg0Z-QjRCJDLcg74pr9i8zHK6D5lhW5QBMNedrZXK_6qjb-Zuh0S-uegwuqvAlMVAU2YpIt5fOF3Et8LAz_xPQdnOzTh7Tspp0-zsSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26374" target="_blank">📅 23:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26373">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCa388LdQqXaeTBlZKqjR9axx5QtbXb_aTbWRLgXBag7SXsrMmO1r_JP_ZtZAn6KirauxHop-iOk8yx9P5psfWd7eV2ng35NSrbuUfRjwlnjhJlMowljjIqaj7X83k2lW0DrU7ZOcFua4xT4OakmoCdvlzbXEg0qzolLQ4haQFC--d_r9mt4IpubeceLDm8oooCYcZ2eqZDBUMTHiSPiZt8WpjuHAxQy4nHxADRusdfLUZhS8p-t2SwlIPHkqljBa7aBOX1A-KoPpcbLC-DnMOhUb-Sh3ajuV6xdMDLwfDrEt7QWUKmaW_SZ42p2NCI3k3BGMByTWsAjnMA-j2J8Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇷
برونو گیمارش ستاره برزیلی نیوکاسل بزودی با عقد قراردادی چهارساله به آرسنال خواهد پیوست. طبق‌گزارش‌رسانه‌ها توافقات بین طرفین انجام شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26373" target="_blank">📅 23:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26372">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_gSYE4u7ZFOqQz-vFmcEicpwYu_DPEuM97irTjrx5Ba-55kpaUuAh7mY76C6OXrfGdUanNoAZ0NMAh5NFaMZzeU2xHJhv9QbIKwHUUjFAabShjePV1LI5jspr-DUJajygB3esIzHkuk69u4_MCIeH9R-s4mIYJnOba3LZAroe7krYZfI4EerNHkI55v70jCKC4e-wSk-05xTZTmUUli0RazCrziiAaxnFZcFDMTMpsU2oiM0KC6TDpr_9RfNtgF6FpWsBxk16-V2j0qtX1lGLDTDLKL9WeMB5FQyhCP3EcLkmPaDj_a4e-RKb2AeN_aW5hLKbBGue2WzGkrIazAqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خوزه فلیکس دیاز: رودری به سران منچستر سیتی اعلام کرده علاقه‌ای به‌موندن در این تیم نداره و میخواد در این پنجره راهی رئال مادرید بشه. پرز حاضره برای جذب بود 40 میلیون یورو هزینه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26372" target="_blank">📅 23:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26371">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0hZAhj2zeiEqqR8YIbQg_eW2T2EdveqAWA1WIP1ZWls2WzwE7Cp1j72Ay5P94tNDMXDzcIaG8EiOrRLmfMSt8H1d3nUBdRJ15be6g-_907GEQNqtlWWRwLaUFOvB41LihRMKkzEQeEfWz112ROqfp-I679D0U1-1LVtBRWeN5af5ZzZbxEB8PvN-tMVeM9aLyodwiadwTib1WE_6ATRdSPo_eCyWOzV2CrMRFHN6dfJuKu7Fa516uQAvYgrW7fJ72sgepaMIyTJhdWhZPrNZrgAFmsoj6DIUdXU5r_jTTWvZDKEiKJYtN8HDqavJVhL3lxGNqwwr0UPuylIipJy-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26371" target="_blank">📅 22:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26370">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBO30r4qcvh-VitB3Dr3RxscstWnBeWWW_-QDVrNgAtSKN6TzmD2p97XbOSdMveGJr5_ABPFqruRfKeTbX_dI89FiBy_p5TPr-GFmQzLsi5960T3af_bWLhEdfGRYPhAIOnLMftD4H53D95JMYJERZeeIwz0bN07M6wQ1rZiPL2vuurFaxHBmAnMZmOawgF9vOGAHMvnubBwy6-W-sVaxDWJI5JB2y2IGnentzld3_87xqvytVC48irlT6Bslkmgz4MxH0R2HcqxB-KnWMypBEnJbs8kyHcUgJ7ziPOyq7RPFubRu39xG5dhbbmB_i7SveWDGyPEDijqnaGlJV1W3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26370" target="_blank">📅 22:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26369">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u97xztR-Uw3p3iayB6uB-LR0kiAI4OiZznGSKrWkc2MF7hACIfrekquuS9tlPUXhRwgySVzFXHrnVYZ2zkOA1XuxqJ8icJdiome7RC98WSvSV8klnFn1Vip3NEPG53w-tAZtBUWwbAeN-r5VlJFbE2H80R0YeLkqOANYnV8494aienZM8xfUv_EYTVY_YBnqOpKy0C9mav2FGgel10XGFDXMF55dtHalWsEp8kwstH1TYvDwJmJAIlP8ctkEPOHzGWBKlr1ODA7PllZjRdqM8E2LEdqkXJzv8Lmay9hhMbEC7YbB02YBfV3KVrZ7p4qsf3jP8uB-SAMJXfj5FPwwiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
مرتضی پورعلی‌گنجی‌درحال‌انجام‌مذاکرات نهایی با سپاهانه و به احتمال زیاد راهی این تیم میشود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26369" target="_blank">📅 21:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26368">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAoQiC6JipaYFFomd6sszUs7Znqf6LW_T5Hj34bTd5X8bfUPI8gQKIrFairV3Te6tC0u_MZjJh5rOfQuakTpKKOKN2at3x8w6_8RPotu60LSExFqfdfTmL-UNrghIOOUP--62cM0dft99QALKhyzgUwzh7FG-qwolZyFfS5PYKSsNnHphGecdlu4TUT4XmqUeT9kZo6repmVgBKR9Z-FhoUnXFx5-0oSaypeM45sU7K6VNuEpOGisCVU9mUR6rj_9F5pwqEYRZylAQ2SRHil2PVZalMpQJc3gCN89kDx0cot_o7LuLEmO47bNe_2fsErCXmy5Mn1zoUIEtptglclKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26368" target="_blank">📅 21:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26367">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQZTqczw8XbU5SmF_AZTFnrDxvzdDTvK6NobDkJ-Ifta_WaTYNCFF8H8GTMmPrlGK6YAYWcUP3GB4oTZvj8kF0BAvnczEFTmND56GvxxnrJ82c4On7zMmdZR_Vdl9m_Cdy4yPxjEtj7i2_5hJTfPOmHzEbjPiflHgYfFyGOAf2xRYJzEFGFqSEcEpFkPHb15l0Ibz-dOeVMoyff14KkUEO98KaPAeH9myKRbF4dv1B4wlx3sxic_-X10RYL87yjeDY6YqlkGYYD9KJWQAVSIjB1bc9-Snszovtjh6RxrAfY56xwKtJt58mmcf1lREHv48P3folOoN6rNta-Pej36bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب دوستان برگردید گویا کاور کیلیان امباپه فیک بوده و کاور اصلی FC27 این خواهد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26367" target="_blank">📅 21:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26366">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=rSbdWfPt0sgTi6wwsYBnzECIjKBYlWbppy-ZiDwcxjoX8ru9CbotBuk_FKJXATmgA57-sR-RWYY5T8MFRnO-xKSX8qyJJ8ADvhQoWrvpob_NDJz1l_FBYCar4owd_Zhv5wjawb_NWs2FUCdZPDW7JdxszMO81dpDL3B2m478dUkUvtAdslSKDlSfkxgpjlYV1qKzxrQCjiE8DiVd0swcDdGlPV0W2AzRaQzLP6zLOxwYS0J9Tr44SlZqOp6kYHJkdoRkw8Eqsw2Io2MgySKwsOtNoWnqFS1ZAyOPr1GE4fHHt8f2qMO_n2z56rqn_CKSGjw952wAABqNQYajfQyq328NIBa3PoW1wH5PP3F2-QGH9K25-dQa3VLr-unCUYouN0bGOo5MU51WlVWHtco83ac97FC88BQnuUmD0ZJr7ONts4XGDTeLYMSw3Stc8hFpXWzomzbLETN4atColb7FRyvepL4o4nJFTsGMP8uaji_acrYR6jIoV-Hy0b-q6MWeVPNVAvOqbDCtfjVdGrsTrigjZcGlGVrCscEXtr2xOX7RbPjUJF1F1C2Kkocr3Pyl9XrPP7sWhL9PHUH-gcAnfTg14AXuwCURIAVrLwwlmdXI_j8eCkjeGU5NDz2nAwNtklPhB-25OyHbHZ59xFZpjxfrp-ifA9JW8XLm6sG70r4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=rSbdWfPt0sgTi6wwsYBnzECIjKBYlWbppy-ZiDwcxjoX8ru9CbotBuk_FKJXATmgA57-sR-RWYY5T8MFRnO-xKSX8qyJJ8ADvhQoWrvpob_NDJz1l_FBYCar4owd_Zhv5wjawb_NWs2FUCdZPDW7JdxszMO81dpDL3B2m478dUkUvtAdslSKDlSfkxgpjlYV1qKzxrQCjiE8DiVd0swcDdGlPV0W2AzRaQzLP6zLOxwYS0J9Tr44SlZqOp6kYHJkdoRkw8Eqsw2Io2MgySKwsOtNoWnqFS1ZAyOPr1GE4fHHt8f2qMO_n2z56rqn_CKSGjw952wAABqNQYajfQyq328NIBa3PoW1wH5PP3F2-QGH9K25-dQa3VLr-unCUYouN0bGOo5MU51WlVWHtco83ac97FC88BQnuUmD0ZJr7ONts4XGDTeLYMSw3Stc8hFpXWzomzbLETN4atColb7FRyvepL4o4nJFTsGMP8uaji_acrYR6jIoV-Hy0b-q6MWeVPNVAvOqbDCtfjVdGrsTrigjZcGlGVrCscEXtr2xOX7RbPjUJF1F1C2Kkocr3Pyl9XrPP7sWhL9PHUH-gcAnfTg14AXuwCURIAVrLwwlmdXI_j8eCkjeGU5NDz2nAwNtklPhB-25OyHbHZ59xFZpjxfrp-ifA9JW8XLm6sG70r4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26366" target="_blank">📅 20:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26365">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7dcpJuvVs8snq-GKl9lhTWgQhJrpzbKQn8LYFHlY2sf4sx1qTMwV5qurqKqAcYsDfPCILIp9ntnmuz5-rQluOj7QpuOdvMjES9waocq28PBBJkeTuoR2PahJFpITf7QUnzDdNNy2mrqdMknFw6mNAJBgIWUQutCs0MuFiiqS8Fl_ZvpR3l90WIVx6TTe0WcCPUNbiKr3pfu4shnWnY7ueo4CV5qjfO3T-Rem7l6TCgwu2lAaclYnQyiOYpLAO3khhMwfTxLDFfC2_Xa5Pqkeh19mrtT32egHv9oFnUfN7LQyMewaR4WL-9QhdgcnHm59ndzsez8fQfqwxgwh9xVgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌جدیدترین‌اخباردریافتی‌رسانه پرشیانا؛ باشگاه استقلال شب‌گذشته دوباره با وکیل ایتالیایی خود ارتباط گرفته که ایشان اعلام کرده در باز شدن پنجره نقل‌وانتقالات تابستانی آبی‌ها مطمئن هست و بزودی این‌ پنجره‌ باز میشود. چیواله وکیل ایتالیایی حتی به تاجرنیا اعلام‌کرده…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26365" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26364">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrdp40kYESGcSxeKt_1boHoIsS4guBKHF-FW9q-_z7qvOwmPoJOhOAtO_Yjf_aIsiArwvK-OIBx7LnO2ekh63nVec7ZHKjfH0sQ8OypS7_4aVJjUb7A6Gi3bKtJhgJB34WWhGYH6ydSGuPqGWHJrT5puO-vfc5Ug4wElTk-0-feciAgr6F1y8fJ9l6aSIu8SND4g67QUUO-v_p7Lx3lJGGZrClmLrOg76biUsb7u7nbql9ueysgE9gxMG1z2YurjuW0Uat14zg5oWFTNFykBsQdffT0Zve_aeDf8FsQ5qWkC44dt0HXiITwGmgt3MM8TTR9riRgpGHhjkPDdQ9QH5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛
فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26364" target="_blank">📅 20:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26363">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPT9QVOt73HzranE2tqyixxo-451pUyMXtNBU_Daj1oTu9nMeUBb8AbdmSd0q5jIPYFwwe-HoBGw4IX5utRfo2u0yugPguT-P3pYuHfVAaJ8ZPWWgk-3Eckoi5xhFuEUglmCoI3vPPEN-d0kpyBozc09grrzMA0TvfZHaBLLlCYx49gTNBw2oIuZ_EV5zDuHr281wKYEIh-g3eFTXe411piZqEy1kgVt5QxksWYI93RF9eQ9-yBKPQ7jLf115nwOONFAfLQtlP0qfqMvcg6ZmUTCpR0PekURGN_zSRexhZOzPxRUlVnbEFst8NZSQQfS_i3rOtZ1T5khrv-3T6_HPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ برخلاف ادعای رسانه‌ها؛ قرار داد جدید کسری طاهری باباشگاه پرسپولیس قطعی و چهارساله خواهدبود. فردا هم قراره پول رضایت نامه او و ایری به حساب باشگاه نساجی واریز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26363" target="_blank">📅 19:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26362">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🎮
دقایقی‌قبل نخستین تریلر بازی فوق العاده جذاب و پرطرفدار FC2027 به این شکل رسما منتشر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26362" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26361">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTjXq4nvs29iJjDSBfEuZ5cxADbe7a9Axo06n3RF4z0FSAjAKNG23uVARRIjaJOeyOc9lPjYQ5XKU6VTbt5sagK7VtAf1pSgfYpL8z48CUbKLn0k4R2rpkk5zJE-d0t-hqXZZ68Zk4yo5yWAskYPKGGn2ip5-X84rexF243dF_BvbT_2mk4P7_ozE9vG9pqXh12KYZT2MyMA7HJmdF0a7Pc_AXIye-QBE-fvdfoQ4lv1F49haOIsf0UKB3zu-LdXha3-HNGsXYoON6jjnPMR88frl5AksFMBAdsseB3RFGoXPNACs75IwGwcLiE9yP7UwGTQ6iampQeyPf7u02ITcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26361" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26360">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jL8kDqJGo2uuaFhI-LbbIyZAMG0pPXosgUijJ5An9zBkPF2BcT6IFIM8Mqvwp2TBHizsfE_-6Kgw4pr7gYCEoC1tAGHPnmlm-DYRS9sMM8Nh10vF6nFKdEqnDc-pA4khem_2v2Ono6WOpMnA3NjQLFOboeJuaFcxaqkZQ26pXleKadv1b1sfejNPwat9iyoHPrLuy8Zjtml95Vez_G39hu0kOMHdahF6nluHul3So4u03DfQbv5E1pldR71uQxE0L3s6xEa7JNYFuK004RxmLodhmyrG6bWMW8Sk6kPp-j8K4d75DJVEAibDBIhuzN67iv7KLra8hwzNE5dypzO9uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ باشگاه منچسترسیتی با پرداخت 150 میلیون‌یورو به باشگاه ناتینگهام‌ فارست الیوت اندرسون ستاره23ساله این‌تیم رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26360" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26358">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDigEYEZhBxxkFs1kWC-ePz3Q7_nc2T2dq0hnWB9q8gsBNxvd7WwIlQL1WKHTdW8xTvmOD39Hyp_tO5kX2-mQ0ur7XJCFUgMBh_m_P1i2_qmqLcBYru2c429KTTntmfD6eJr9RqFwcZATjHqgdKz39POM3tC5wVaTtfEwtUDC5f380o6-ygr0JtbbXEU0UFhTTRcGuLAaS4xmoYU8LDjdmUQB9Vnlpit1ii_sNANnPKppSRtipsloPfQgJ1I8TMBcW7cdO7Y_eCIl1_mM9oMk1AHdShOSpG8UO_MGZxUV1V4LUdFOwROtw0rOVHce_zw3FYXaUD0Co6eJ_nKCTcTUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26358" target="_blank">📅 19:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26357">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EE19h8nD4kRwCRE35bp0rodiFYlGsE-XPIbGJuWBnJIIk17iBlxMnQC4_xO5DZlZMyC0Q-__c-m-NH9GpKrudicnZJjeEPaZ-xv7QuW_HfKFtndpx-1BTABN9vkxsUEKYXv8KoAC06vdLkcua2rOplOfnMtgQjFk9HpWIOJKJJYXHEP_TxgAJ9ZXczMwRF8e6gCuMn7RvFsyOIeRu7prblznR6GxceMieCLNf3BeJmO8AQeHZg_fF1NuJ8slTTfgVkZJ6SOaMqfmpYk17V_SlvHZWaVmTkNYTLrG9tGAc3e_r5uIo062dYMSIMJk_WeOfc8UCgTQhgEcdacIHoEstA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو تصمیم گرفته بعد از دیدار با ولز در لیگ ملت‌های اروپا در استادیوم خوزه آلوادا جایی که نخستین بار فوتبالش رو استارت زد از بازی های ملی و تیم ملی پرتغال خداحافطی کنه. خورخه ژسوس میخواد رونالدو رو منصرف کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26357" target="_blank">📅 19:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26356">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=NIDrbKrSP-itL9qKc6o-biCaFH8z11m5hDn8vRmrdBkavPVAG5xFpxuYUrF2gownqiKlls2omQ5p9timmu95RW0zmBxVNdNJrtJfY0ZjdZawzb1tSKaoBoA7ygw_3Ww8LKfK8dkHKjHfwZRbqF5uUplXf3MrxWdi4TZBMNRyhBNSxVVHRAV3dIDDPqSOk0j8UYXtCI6o6_z845OnFgMD3s4pg0L-P63nL5edPSUSLedVBZdmCSO21zdaijAu2-NlljYQ8jRsK6uE7Yp-DOu7Yu986hM3nVz14z9TriM91Wwf19N85CLJptHBkdcPuRBfqw0b8m4EcNdmryCmxkfh3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=NIDrbKrSP-itL9qKc6o-biCaFH8z11m5hDn8vRmrdBkavPVAG5xFpxuYUrF2gownqiKlls2omQ5p9timmu95RW0zmBxVNdNJrtJfY0ZjdZawzb1tSKaoBoA7ygw_3Ww8LKfK8dkHKjHfwZRbqF5uUplXf3MrxWdi4TZBMNRyhBNSxVVHRAV3dIDDPqSOk0j8UYXtCI6o6_z845OnFgMD3s4pg0L-P63nL5edPSUSLedVBZdmCSO21zdaijAu2-NlljYQ8jRsK6uE7Yp-DOu7Yu986hM3nVz14z9TriM91Wwf19N85CLJptHBkdcPuRBfqw0b8m4EcNdmryCmxkfh3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
ویدیو باشگاه بارسلونا برای رونمایی از کریم ادیمی فوق‌ستاره جوان آلمانی جدید آبی اناری‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26356" target="_blank">📅 18:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26355">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=aX_vBUwAoYQqtFUt6j5KZHs9BkS70pP-JHC1PMc-pOQXNCxlejMgj0PUPWouUXEtfBUP9zIsLhthRzqY1jVCG7af3LVNQ4llnIjbg5CHcOBXto3ESqertJLWZO6dOCk1O_7TvtkIY7s69xS379Jms8tacQQwnhJDyKp3Sze6ONKCAsmZUET0RYgWvTlPuSWEzQYZcMDCXcl2yYg5vY4WtmvQryH62yuAtM16F5Qqt-z-S0rFa2vZ8aUkgf01SjEeaPNZdlzcazBliVk-6T7Y0FWgGPIx9dJyau01HVLkLeiQnh9H5vMa_WvSdPmlRhYcpqQ_ylHevhvmePS2oiAH-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=aX_vBUwAoYQqtFUt6j5KZHs9BkS70pP-JHC1PMc-pOQXNCxlejMgj0PUPWouUXEtfBUP9zIsLhthRzqY1jVCG7af3LVNQ4llnIjbg5CHcOBXto3ESqertJLWZO6dOCk1O_7TvtkIY7s69xS379Jms8tacQQwnhJDyKp3Sze6ONKCAsmZUET0RYgWvTlPuSWEzQYZcMDCXcl2yYg5vY4WtmvQryH62yuAtM16F5Qqt-z-S0rFa2vZ8aUkgf01SjEeaPNZdlzcazBliVk-6T7Y0FWgGPIx9dJyau01HVLkLeiQnh9H5vMa_WvSdPmlRhYcpqQ_ylHevhvmePS2oiAH-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اسپویل‌از نبردتاریخی جواد
🆚
خداداد در ویژه برنامه‌رقابت‌های‌جام‌جهانی2030؛ جام جهانی بعدی قراره تو پرتغال، اسپانیا و مراکش برگزار بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26355" target="_blank">📅 18:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26354">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saN8B7xYvQlQnw6tzh2_8unFyPiemegx8z3sxagM5SsPFIuxxmPmhxYjjeVm0ne3akWF1mZiMl8eLrD88Q1MvKpT0Vdi5lTrYUhcUQ5KH2AI65QKAC_fjA_X5EcTnzBtpRfwCyHJnMSsI7l_p3c0tDSyx8jUnCA_b6CB4ZjNplsocnimw8_i6gSEqCsv4kwHnQbH-wBlH-XU9lA5cT6ZjaBwpYfljIZwl-Byw_GvgmxLH1w4Jf_GYeFyV1v8I3iJ0iAiLQfJsii7PJ-g6EC0Tr5d1fCZv7NkXYVHRpNdYN9Eulo-wLAi81d2CCy_ot9salrjggkbh5HmHwkDFeZYZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26354" target="_blank">📅 17:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26353">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amjvPpovuGA6Sf8K8cGv-JmR-UHUN1Mb5nH_q3RY0WYiGF0Fb2YRBXINNPBI4R2D3b1sQ4FtnvVDMrYFTVnoldN38QUUPsAkJCbNPZAEwFQ95QGk4DbF_nWugQHcKwRdC2yYd9U5Qu3Oehw9zhC3kAH5JZopqFif3marm3df95XX3i2aekISjMxc3_snTrUWYFsxe_0mJJHIpaB_uvSh1vnv-ummO-j1kDSCKF4ZFy8P6ANKUbweSV0srTzrXrnV81Rw04h7Q8fP6C4UP_I-fsjxKoomRC5QjvKqIfANiIucG8dQm0rzEzsC2bWbJOHjPB5KiLGvEIXKs-l-meo5Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
بعد از انتخاب یورگن کلوپ بعنوان سرمربی تیم ملی آلمان؛ درصورت توافقات‌مالی باید شاهد حضور پپ گواردیولا روی‌نیمکت تیم دوست داشتتی ایتالیا باشیم. چه‌پپ‌گوردیولا چه‌روبرتومانچینی بیان قطعا تو یورو آتزوری باز پرچمش میره اون بالا بالاها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26353" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26352">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDsURAtlsJqurOvBKxxVYhIdC7-VUDHjZrFEC5-GoFepqPaAmDtiVmDzVrOK8poPLMRD0W6cPAw0wiJexsn5IDw6FFtkZrOKYVCEvLj8W5iu_V0de9Tozg7i-OCmIQ5BQk5ngpTkDnKDZTzXfDQvBOV6JvXoKK94oxMGE9gIUa1obAbX-m5wgefDePuGZ7qq88kOHPXG-4gwDiYPPlNNShsMdN1JRObPNFbgcVlPezvLZ5peDMCpQfi6kTZohD-6b3EirOCDi_DjpZAcFlhhuyv1qx3Rv0K9IvzmplrQKugeJpxJWR_xouehdBNgDbLuuCuGVdUNSP3kPbR7bwghkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26352" target="_blank">📅 17:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26351">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTruRprpTRaPRpMVSGh1NJRmY-59jPgIQ-vZddogWOgyPB6Wj3a_SOOIBcPSyEqTJeWnHH3UUVefAnSS9X2YXqB1VrtowL6S2ZOOud_r6iUQjqfv4lO7sAtp6e53zzeWjOGKCmuXe3f8I-Y4RmroVmuWgjIsUHWCbGqYwe1f6BbUQ7gB3OvnrF8Xy65TZu-_qDlHo2NvEEVKkSEAe9Sj6Xfi9JBdrWk4Zsy1u7o-cjpa5T1aYqY09QwRb7STCCeK-I6692li0H9Rid5dddw1qOQFE-ecRHEPgfxj5hc_JkhTg0RnWm9hUUmBUw94PZuxvvR_Bm1PDjMa74pS8wvAOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم دونده چینی‌به‌اسم لی میژن، در هشت کیلومتری پایان مسابقه‌ماراتن پریود میشه و علی‌رغم درد احتمالی و تغییرات ظاهری که داشته، به مسابقه ادامه میده و ماراتن رو به پایان میرسونه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26351" target="_blank">📅 17:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26350">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFsBKpWUXS-NPk2IUgO5BltInSUXCO8ntymnkIOUKJUgk6WQRQREChXSTCRd7i55ksTRD7PDw9CjiXPfyDIxoJn8-12j9w82uVNJYyXAge6Dy6OPTzJp3UyI8XpXmhduHJzuo6hdJfABc7tJfTw4Dkt1ldxSb3uG3t9ij3aPZAiAWzFZHIT7Gb_-yJRvQwVPQlSUMqWNKmYjTpgogZXGlZ3Z49PvsEzZeWt7iqu9qvpe8QiIc_yzKPQdaarH3u8WhLvaKTRvttK_6OgOTxs1UDJqIW-ZlxeqVQ_ZUcaWRqyqQ7DQGbvmgqniZE4wKz-u68fgmZhZLlAUUbPFzuYdMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇬🇧
🇫🇷
#فوری
؛مسئولان بریتانیا و فرانسه در 24 ساعت اخیر سفارت خود در تهران را تخلیه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26350" target="_blank">📅 16:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26349">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lv-3w48mBqmsteXZmhRemanDAywzVHufe8Ks90AUNFRd4sUkkzwV2N44JqdwEnkkopK8rQN-8VzZmGqvZ6FrglOdeUjxege_i90EseS2F8qsXffGoZ1p1Z0X1caFknEA3RvaQiglVIqzDD-AnuyK6Rm3KnzYH_4HKtnzotoqGM2-4uswiq1jgqGi_z6Dc2sold3ysc9e3AQ187nC213VLz1EN3Rxk-HN4nSoY7KlTjwcX79YD-ecYV5dcvflyDJXjyqHQcDz7fsZo_Sn8YaIroOWloNtdCzEbdd6ycaEWa3jTvYdYi884FqPxlYKCEGm50Grg7e9_KsQ8nggOV-m6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26349" target="_blank">📅 14:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26348">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqTGu-QuLwZ-LczHJMHxQsz1Ky_Sgyh2nOfKCjZcx1dapbK5f60MANV-6HhKNszmYa-yD7ffAiZP_QUJYPTovebZAQ6pGquETiOEoGYgAEBH3bAW0ZPr2HcXruf-DZvC5hPhra8Q84zUgPzFehGT8Z6x6odzxc08yQucC_nUl3q6ujS4XNlk1wfG_wa0jwv2lvJGU63i0-mvPhTMsy7zMXaMb1_uUInJrSTOmoiLTWfe-0GAiGdQyTMrh8ySGJ1fC4_14ceEYczT-wYlyIjjgYU5i342yHRaOaVmsoj2Hlo2DHFfRvwUqMjcrY9MlLIUIBAttYrdEpKs9vo1lOGb0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26348" target="_blank">📅 14:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26347">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=Bse137m5pE1PkM3iBTIPYTCsb84Z6xstDAHAofZqJRPyrFbfrAoQfo5UFw4pC7hWdrCXQRFKIBz6iYjJa4mrUUWXtRv2tt5Vd6nFVpz9tXc1OAeNL810OJauHox9w2-qRmtl4O6FsuVUxLqfZxMnH9JN5F20h-JYmx0JPq_YCiSEijh1PRNoaHUaZR7h3gtjVQfTxJ4REOJwgMkEW1ibiriWMCNJKuaSyJj-xm-xn1wODc4OE9ubenM7weVTpia4OrOKI-kW4QuZGYLYRL-vAMzVxcXvi9AVeqJTpCGNQ8wBAZ_Lel-i8S2r2adGpKHFZ3vVfvBjjZYkfTSd4nmExg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=Bse137m5pE1PkM3iBTIPYTCsb84Z6xstDAHAofZqJRPyrFbfrAoQfo5UFw4pC7hWdrCXQRFKIBz6iYjJa4mrUUWXtRv2tt5Vd6nFVpz9tXc1OAeNL810OJauHox9w2-qRmtl4O6FsuVUxLqfZxMnH9JN5F20h-JYmx0JPq_YCiSEijh1PRNoaHUaZR7h3gtjVQfTxJ4REOJwgMkEW1ibiriWMCNJKuaSyJj-xm-xn1wODc4OE9ubenM7weVTpia4OrOKI-kW4QuZGYLYRL-vAMzVxcXvi9AVeqJTpCGNQ8wBAZ_Lel-i8S2r2adGpKHFZ3vVfvBjjZYkfTSd4nmExg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26347" target="_blank">📅 14:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26346">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkF5Qlm5nnFa2okrdRbGvkBJqIV9jBGgJCUpVUl6HNkePx_OrAyGlEMCDZew_eiQCNBlowNL4Rm99bhGT97j03s5jUI4PTw8N76ZJGK1aXfO-H79_vpOVEUkaixTKjnD9RKjTuwA0aWtBalslfo6VAF9tOf5L8I-WHc17wGF8CqBLgVxfMEs_vPprqi-KHyKP98NoT4jygsUnKVig8ru4AKPOvfzhE1KVWybuEhCYsYYnxtgW7gqBUde816ke_zSeUsDhaLkOLvuc0YqUa5sTFaSiAflEHS23ISBOjw-1Ui0YJb06WucLamGs763LkQUhzWW0fqy6lM8K04kPdgwjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26346" target="_blank">📅 14:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26345">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=dd31rkr3fnlqDTewxlSU1rd0E9T8yITraItEUj-cfToI4dahWMcORbjo7szXFFfZpm-feByhyIoHt9Ky8FaUBlnCRo5pUqoAdc8BbXVsNIPhEIAVui2uAQjlkLZJAkq9luUJnPnYKKzErkDvJ587c5jBDUBwDFJ4HLVTQtZUBY8iT15w127VwyFWp1vynlvmB8iGHN0Jl-dRslQGnNthEfKbhlXZVKFpQuLXc611epZhtWIrGA4ZUlEwrl7Fyss1eTX8b19IXtPw1GZxzbGRzzmR93pjjuFb0mWFCiPMc5SVgUenWoXLbrRnM16EM4n7Ctihi4B_sTJsU1ISv-pQPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=dd31rkr3fnlqDTewxlSU1rd0E9T8yITraItEUj-cfToI4dahWMcORbjo7szXFFfZpm-feByhyIoHt9Ky8FaUBlnCRo5pUqoAdc8BbXVsNIPhEIAVui2uAQjlkLZJAkq9luUJnPnYKKzErkDvJ587c5jBDUBwDFJ4HLVTQtZUBY8iT15w127VwyFWp1vynlvmB8iGHN0Jl-dRslQGnNthEfKbhlXZVKFpQuLXc611epZhtWIrGA4ZUlEwrl7Fyss1eTX8b19IXtPw1GZxzbGRzzmR93pjjuFb0mWFCiPMc5SVgUenWoXLbrRnM16EM4n7Ctihi4B_sTJsU1ISv-pQPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه‌ بدونید که‌ چرا مارک‌ کوکوریا مدافع‌ رئال موهاش بلنده؛ پسر بزرگ کوکوریا متاسفانه اوتیسم داره. ماتئو درتشخیص‌چهره‌هامشکل داره و این موی خاص تنها راهی است که پسرش میتونه او را هنگام تماشای بازی از میان ۲۲ بازیکن روی زمین پیدا کنه. کوکوریا بارها تأکید…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26345" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26344">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFhdbSZkmWZ3dUu957iY2tbxU66K8Xk_4aoU6Avxjf-d6UIpUnK4BExDBQv3d_A3TTWVz9uX21fKe9E6UUY2hL_xr_K6sHp2hYOJdr3lk45MBtk5tDEtEbYZqJx0PdgnLtZj8zJgTqReRa9kfXf1BoLoP5PLQTtXhe3WyvN8AxqjI4v19Mp7woAAOlA6RYPH4HcUw1AwqOucjYQLqVe99P2k1u9lhbCDOQxF_u9Iv2EGDm4EQreagb5H6dyKH1O6L4qwXpOkp8ctOiJqr0c2DH-hOquofmokfr2yvHoneHR5o8DebWNxJaCcB3paxyKTox2X1flfJS52jsL7RXRB4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇮🇹
🇦🇷
#نقل‌وانتقالات
|
احتمال پیوستن فرانکو ماسانتوئونو ستاره جوان رئال مادرید به میلان بسیار زیاده. مورینیو از پرز خواسته که قرضی اون رو بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26344" target="_blank">📅 13:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26343">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac2f696a95.mp4?token=VdQZE8C7k69aRQtVUOjByJyy2Hgu2GKquGWGKgkZtGg8QHrFbAmtr4fwGTAHdwA9ODdX8vDL3kuyY5qusBIzGl7LYNUN-NBraBo9U66yedLJyOnnBeBZ40G1JC85rvuNCK9S2drXooyycUAfUml1tAPMugDXjJ0Y4EEvFuHOVbiBGTM0PdCgEnTsuxw2ADz8BLHyo26CZ7x74bWTjhtTFRi6Tg7bZ4bB--qaWMUkVyZobHHWeG9Az5kfflBPqen_QzBWs9jnCN7uR4kZj4F62fgioaYQXqhSZZBOOHq6tsVc_hxDgUE8daGQrn--RHSMmhn7bmmcRI04mq6lwBXxog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac2f696a95.mp4?token=VdQZE8C7k69aRQtVUOjByJyy2Hgu2GKquGWGKgkZtGg8QHrFbAmtr4fwGTAHdwA9ODdX8vDL3kuyY5qusBIzGl7LYNUN-NBraBo9U66yedLJyOnnBeBZ40G1JC85rvuNCK9S2drXooyycUAfUml1tAPMugDXjJ0Y4EEvFuHOVbiBGTM0PdCgEnTsuxw2ADz8BLHyo26CZ7x74bWTjhtTFRi6Tg7bZ4bB--qaWMUkVyZobHHWeG9Az5kfflBPqen_QzBWs9jnCN7uR4kZj4F62fgioaYQXqhSZZBOOHq6tsVc_hxDgUE8daGQrn--RHSMmhn7bmmcRI04mq6lwBXxog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26343" target="_blank">📅 12:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26342">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tw4LsH-4XTatFvYJTDpPUTHlv9O_a2ry2tppkkq7hBygR8xlZZT4RmQHCSJr83s1TPe-gTfNB31iU6AERqoAjYuafTCMczFY3m_3Bhjx8QMkearWs4EuOWq2y6Awkk-Kh062ojxb44XHojd64DrfBez4Ix3JtMcbZC9gDOTBvUmGG0HzMKbGktSloT5ud18gL8Gr1uLOVEIFb52Ks4jpO6sODfCgwP-Y93oFp2IOs3RW6uROoe2gksYA4z22xyAvc5Dyzv0CziZIVGneLxJAXaY0MckRSgGM4Ri3pJTcsX2sIp0sNPQ2vOlGCoqvS3GQy930iOAsW1hsMlvnu_pcKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26342" target="_blank">📅 12:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26341">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMNXg83Iu786l44XV_hSDc75dQboekrzD2yRdaRPowNBYVrTcugcLQssYbbbQCi0EwOd82GmeJ8nrMN0-4E7TJo9uvEWIaJ5uuo3oMKbr7Alvi8EMl_Ayq3hKWzm56QWz5tXtJINEix4cyfarWfNaSaZ7cbDuXPik-gSH0fyME5kM1jjY4bth33O9rX64EuxIR14sldl9F9lOCfDZy75OJQWfwPV708-SdHafE5QX368tJqv6Nob_ei_fQwBKQzx_ioStjpac5mNqHM-sHx1zFwhVQPYpETK6yi2jNAbiNUdblTO7YV_clItFpqSylcfo0pU20-9k6RwuOPRgh2oQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
یکی‌ازمسئولان‌تیم پرسپولیس: با دانیال ایری قرارداد امضا کرده ایم و بزودی از او رونمایی میکنیم‌. علاوه بر ایری چهار پنج خرید دیگر خواهیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26341" target="_blank">📅 12:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26340">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvGn1wxKBqEiyNXZLmu-P3KC7VmBOn68eyew69_r1nErDxdcAKGsCb1lunhF_yGqEll5MFOza7MkDi9TQSLhv62ABDRPzX2yS1-SbdbYPN8j9ap8PCCuMFBouCNHYFsS4w9RgUbTGnJN0cWBDsCmT-pegIgiN_-cb4USL5ybijoh7I5tGIVTMyi5IP6iurpnk5Kymyq4jIIAg7_KqwbkZf5bISE58YyW6Z_jfm8y83CHsj9f9l9axh7f-DJUTnV2XXCqmz6-pUaiUPummwFOSZeEq1qbMnpCBLXw3ksY9Gue0-QznwOAld4RsBvVr_FO1RSbC5T3_cEF9r6EiINuZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26340" target="_blank">📅 11:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26338">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q8olHZOu7LZ67aKFohitny3ffi4mOqv5FLrqm4teyYvX5F7k1YUElEZe2o6td898DylYShwEfL-7bME9i6EDTKFIPfdwnsIonjmFeLVhbTNq9hgA3fTDa_GVLP387nO_dk69Z4fCkxl-tkNvuEtTb0F24uI-BgmsHesbWygUNL4s-BvyefzAfN45WbFP33vuBOfPlUAbs8TdEFwzPcGTwrZwMRmD7ibpgFEs2_375uPayyn7srBDtI5m2OUqS39bEkrPISr0r1sjSLafai3_UoYcD1D4o2H-nb_Sp1wCpPja5TUd00HAQl1a9pU-WXDXtF_Ik8AB60s728KYN6sfbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OAbeqk0PzSjSeq-Mi4cgeCkVKRuhNaGls4SHZmIUhAxOBfp3K1U2TcEFGOnBtcFpOsc4kadB6WbVkjHWnzXMMc16tK_cnWZ1DMf3UHXWBK41B8QEJY4yVeD2Q8z7oDqR5PXCL_pLgNgd755odbbn0Nx8AVkFv8GjBwXqzwCBbbexygfSETPWJIEotp1VikZtTAV9aRtexPde50l1iVCDM-ERD39OASZvptlme7o96khUy0GmG2YVc6aTQ0h-LoJZf8xoHMqR8X09x-73QY-7YnjcQJBHK26uMrjbfRrzfAZ1rC5hyvictkWeeAblvoVrfvIVNz9aOj_d8F0vbDQWdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی‌غیررسمی‌از کیت‌دوم تیم رئال مادرید در فصل جدید رقابت‌ها؛ فکرکنم باب‌میل هوادارانشونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26338" target="_blank">📅 11:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26337">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h28j3urnNHfXx9h0E0IXpz1nzttp7O8reCiseeTwYIhmGU5qA5BW2xkE4ciW7xqyNAg28QOfdTiv1GTN0MwZcIvia8HNaoTC0yXE5qyeNUFJfbZxSUtZfR-igEtXFukYQv5AaFljOm8EIs5oRTIwJ3H9ruipisAx3EUY_CDFivX_kHF3RhKSK9l7mznV-utetdtMajIdLAOxqvplnHQUIfAkrMzgJMCbXizMdEON4u2UOMp37LF6UPQDnxan6ecFTzdCIU4rDZLhZ2yzahbK258f895DAKkhrblXveHDMW1bc-gDeEdJ90Exm8BA5z85wBbOJpZsUSlPwodAncjuJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26337" target="_blank">📅 11:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26336">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=Ga7UVGbfme1_i70FDQopKLM0TjFmE9PYksIuT4F4QlehCVDzQcyDSUCz5KCm4AZ8SkgXtyAG1pVZVhY51hH-kpEk10P2FJNTEl6uL013oF4Lzn35altjgN_22URs0A_ej8k8P8Ig1YzBZXnl7Q6uTZ9xUzecdUwg-2aPYv2o2QPbajyzUUyaxhVGxtpb8dVuZ4LZLfHvOBjy49AbiOvHB6eD4SSb3gGgIoSSRI2fJXRsv9O54HVVrM-qQ-pD0wTzBG4AFwyCP-Uqr-CulcVxlis4PzZCYrFzFHkTPQLWuPQ4y9rjZSNHXYvPQlYYznQ81NWUZgCeNkFiND6VurErvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=Ga7UVGbfme1_i70FDQopKLM0TjFmE9PYksIuT4F4QlehCVDzQcyDSUCz5KCm4AZ8SkgXtyAG1pVZVhY51hH-kpEk10P2FJNTEl6uL013oF4Lzn35altjgN_22URs0A_ej8k8P8Ig1YzBZXnl7Q6uTZ9xUzecdUwg-2aPYv2o2QPbajyzUUyaxhVGxtpb8dVuZ4LZLfHvOBjy49AbiOvHB6eD4SSb3gGgIoSSRI2fJXRsv9O54HVVrM-qQ-pD0wTzBG4AFwyCP-Uqr-CulcVxlis4PzZCYrFzFHkTPQLWuPQ4y9rjZSNHXYvPQlYYznQ81NWUZgCeNkFiND6VurErvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
سوتی برگ ریزون دروازه بان تیم اینترمیامی در بازی بامدای امروز مقابل شیکاگو فایر؛ اینتر میامی این‌دیدار رو با درخشش سواری سه بر دو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26336" target="_blank">📅 11:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26335">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRM4tAUBalTtvryO66RnQASxoo8e2cmtkEdVq3iX2HxAmk8lTuyze5YSqwFGzvx-KcqOd00sr3WuKoka8hVLLSU8nlyMFUXawR-lqdXwtnRF6X40DIe5_PiJvsDtSmsU5JyaPwNuved2GiaiNcTaxZ4fpLxK2Yww-8RANSoG7HXcpdnwTKHhUeZum-rA4OlGNu3BshtT_5ZwxmP3gANIuD0XgkIpv5MJSiqIKgR8E-GUAuzva8q3Rb8-a-mZNMGG-FEIHg3IJyJv2D-WB55dTUM19SeN4G66MYqhWK73Gf7FyaIulpe4KtR_wDcCxsuqMM9XM3rXiCtckyewGd_9LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26335" target="_blank">📅 11:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26334">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D60r6Bg59tnu_G7Pp5eh3ZrjiXhVxkE3DCryaxwsqYHNqY-AwUgtjQM2rdUd51QRiz2q7xkM5Uom-2lbvR1y9SETJ4k18_CT0w93LtqoShAXPS73ZtYgrSd2wY11o6Dq_8iSAQ9xqZMdF5uMFAvqf74DLatjHe48F4YyLxB7MNU9PGzFO-ulT30O1Epkd2kVtwLoWvMMjm6iqDY-vvZX4doUlhVbeqj3IsKtAQCga5Lkuxwek5dnAznL1Qnsz3mfswv7cQ2nSHDfaQ3FP4tYacfb9zcP2iMFCpWhiKlkZ2i2FsFdv6WEKCbgtmRFZnuNW_LIqtZ_he56y9yfWFCd0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پیرو خبری که ظهر امروز گذاشتیم؛ باشگاه پرسپولیس ظرف‌فردا و پس‌فردا و شنبه به تریبت از دانیال ایری، کسری‌ طاهری و محمد رضا اخباری سه خرید جدید خود بشکل رسمی رونمایی خواهد کرد.
🔴
عصرم‌گفتیم‌کسری‌مشکلی‌برای‌رفتن‌به پرسپولیس نداره. ایری هم‌داخلی‌بسته وکار تموم…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26334" target="_blank">📅 11:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26333">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qr0vSw003l1GbMCqFkzYRKStBSDlAhsmFXNGZfuPItqLnmXDMnaPmvHtDBVRKKXO3dYYL4U2PLO4EPsr4pADdTDVKrUl0Ud83wCyFr0CA0rS6rZ716e-9M7lTC7KgiFu0iDc0dLaOIA8Lw5nK9fXOzZ6GIvzSvPeHsydgM6b3ehdvxi87k5_l3_qXMtrf_NDFXBiE-usWaBKh4DZfbzb-UyTKjMWsQ4BZmuzAGqIpGbOTA1M7tlpIXfwXa6ih-CoMYeRW10MdUIpie19iBl2txPLCC1r9uRiTyrO6T9xJ_3B_GcJ6NV55NsWYwZ3z64CqA9bYOxUqKCR-sPKyZq6hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
اسکواد کامل و فوق‌العاده بارسلونا در فصل آینده رقابت‌ها؛ بایستی‌صبرکنیم و دید هانسی فلیک به طلسم 12 ساله قهرمانی در UCL با این اسکواد خاتمه میده یا باز هم ناکام خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26333" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26332">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc429eafa7.mp4?token=NtUvlWO07KVueHbHQHHVmVvZ7YCdG1rZg3xLU9zUCbIF9hM9K8Z5Ybq6eEEW2JPy6tTC5wmH75M95fOprDI5WNYT0LQNtsl3pCzdTlzdeoZxoq4XNxxrRQL1wofeS3-z2WL-3ery7ODTeE4FW-T1Gx70tV8NQPRM2RLAGwN4UqRMeEkFa2AiRtUNne0DGRPlUlgw8Y-sv0bKm87LLl5Td5460WHwvcSyufyWvXiC-mzQkz_OO28UwmVKEZ-EbIYlhZ6RaLE0C774XNgUdGNacQ5Fb26Kwrc2LfA5jHFEz8PXvim7bql658Xu7LLmlKdo1oGckq4Ef_hdRv4jQSk7lqcU_vrKnITHfx74EzcfzJZ2ii5qlPW8CCdgZTi_NSg1z6HCGqvbSHvw8OUCCjm3x2QqiEhbL4NwSwD_N249YZMNmpHR10oqFGg4THy3kmsZSI1P7ccjC0srV97ftLkYME7cxlivnhDxxT2_vVnnj-nloc3-_GEvlHzgzb7IbsT_j-iZQL9S2NnKW1HV7-hOlTPZ_3bcl0DqOuq-T0yz5MroRJrONctytEytWumWlcYLBp2jI099EzEO5wXQqvWxosAMekTtGByr0BimTfY9WAXZdtpp2iphairHlvGJPa9tcutIPiM_u_EPJLBJ14by23wtn6ksn4iVjssWn9GNXyI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc429eafa7.mp4?token=NtUvlWO07KVueHbHQHHVmVvZ7YCdG1rZg3xLU9zUCbIF9hM9K8Z5Ybq6eEEW2JPy6tTC5wmH75M95fOprDI5WNYT0LQNtsl3pCzdTlzdeoZxoq4XNxxrRQL1wofeS3-z2WL-3ery7ODTeE4FW-T1Gx70tV8NQPRM2RLAGwN4UqRMeEkFa2AiRtUNne0DGRPlUlgw8Y-sv0bKm87LLl5Td5460WHwvcSyufyWvXiC-mzQkz_OO28UwmVKEZ-EbIYlhZ6RaLE0C774XNgUdGNacQ5Fb26Kwrc2LfA5jHFEz8PXvim7bql658Xu7LLmlKdo1oGckq4Ef_hdRv4jQSk7lqcU_vrKnITHfx74EzcfzJZ2ii5qlPW8CCdgZTi_NSg1z6HCGqvbSHvw8OUCCjm3x2QqiEhbL4NwSwD_N249YZMNmpHR10oqFGg4THy3kmsZSI1P7ccjC0srV97ftLkYME7cxlivnhDxxT2_vVnnj-nloc3-_GEvlHzgzb7IbsT_j-iZQL9S2NnKW1HV7-hOlTPZ_3bcl0DqOuq-T0yz5MroRJrONctytEytWumWlcYLBp2jI099EzEO5wXQqvWxosAMekTtGByr0BimTfY9WAXZdtpp2iphairHlvGJPa9tcutIPiM_u_EPJLBJ14by23wtn6ksn4iVjssWn9GNXyI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
سوتی برگ ریزون دروازه بان تیم اینترمیامی در بازی بامدای امروز مقابل شیکاگو فایر؛ اینتر میامی این‌دیدار رو با درخشش سواری سه بر دو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26332" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26330">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967d8465e2.mp4?token=SizFw0Grc7f1UEAWbiI98d3DNcjQqRSa4GK3cz96sFo-WZVOdxbQL8SryDToSiMUj6zY4eavf9dCrnQfJL4ozQ8wF7lrYOXliUmgTXYim-gOyMSiKGxMzYp1ySfPhBJfzSGs53KVEPxBoPe8RVjySGE6-be6lkJ_FBvr_KK5pMTjccX8jR-1WZY4MsOsdK5y-Y0w81-MFI83-nHHgjuUg9ru_JAAVEYVQT3AzpX100kLlq5bJP1elv2ybb7iA03JT1we0MH1gksHorvCRxhrgtq_ZGeaClkkPx7FW6FZxUGZ9CaUzNzWjXl3i36MO0cXJmy__MRV0eST6cDdlnOvtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967d8465e2.mp4?token=SizFw0Grc7f1UEAWbiI98d3DNcjQqRSa4GK3cz96sFo-WZVOdxbQL8SryDToSiMUj6zY4eavf9dCrnQfJL4ozQ8wF7lrYOXliUmgTXYim-gOyMSiKGxMzYp1ySfPhBJfzSGs53KVEPxBoPe8RVjySGE6-be6lkJ_FBvr_KK5pMTjccX8jR-1WZY4MsOsdK5y-Y0w81-MFI83-nHHgjuUg9ru_JAAVEYVQT3AzpX100kLlq5bJP1elv2ybb7iA03JT1we0MH1gksHorvCRxhrgtq_ZGeaClkkPx7FW6FZxUGZ9CaUzNzWjXl3i36MO0cXJmy__MRV0eST6cDdlnOvtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌مهدی‌قایدی درسال‌های اول حضورش دراستقلال: رحمتی و حسینی بشدت‌باهام بد رفتاری کردند. تو یه بازی درون تیمی به حسینی گل زد گفت دفعه آخرت باشه این کار رومیکنی‌ها! مهدی رحمتیم گفت این کار رو بامن‌بکنی شلوار رو از پات در میارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26330" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26329">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a30d0e41d.mp4?token=L5GOz8W8xor_JmXxIruFCNMke-Of9BbUiAFIuB4erSHnmbY_1f-05ztBl31R4yJEZ_Vuchb7tn4dxcdySN2alocDqwxtwfNs1Ft3Pj_5TcJnPsVmR1eJNmhWq0_jBjYs_9rEVqvHeBNljsJyBGXJjBvwJ_LL2dvBnZ9T2TnApaUa7WpIZdbTlTMlK1CnXGaYDbpN4dOSyt4pCiJlmD_cectkF1Jpe1pyqu5SnMuEConle8RVhDqriAjZQG4OiGq-k0OVwF-qYGbobuJcmaRBGAaiEVReDtNp-P2d9yiWclmxyAApN6iJp5TT7ZINL9W4v8y6-m-G5qxAedp1WOzZLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a30d0e41d.mp4?token=L5GOz8W8xor_JmXxIruFCNMke-Of9BbUiAFIuB4erSHnmbY_1f-05ztBl31R4yJEZ_Vuchb7tn4dxcdySN2alocDqwxtwfNs1Ft3Pj_5TcJnPsVmR1eJNmhWq0_jBjYs_9rEVqvHeBNljsJyBGXJjBvwJ_LL2dvBnZ9T2TnApaUa7WpIZdbTlTMlK1CnXGaYDbpN4dOSyt4pCiJlmD_cectkF1Jpe1pyqu5SnMuEConle8RVhDqriAjZQG4OiGq-k0OVwF-qYGbobuJcmaRBGAaiEVReDtNp-P2d9yiWclmxyAApN6iJp5TT7ZINL9W4v8y6-m-G5qxAedp1WOzZLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
بدل ایرانی مارک کوکوریا ستاره چپ پا تیم ملی اسپانیا و باشگاه رئال مادرید هم پیدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26329" target="_blank">📅 09:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26328">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88237cb2df.mp4?token=DebWgmg0zD5BOe7vJNtJO725FmHUFznOXKEJfWa3nbbyEoy4FfjZt77UHzmQvrsoz7Jr320paLoN90H9xtjMxJPyXcYUeNx-hCgRU0wKO98cckH4Pw_Ylu6QGi-dhRpHQeII033fOhu08zLlbcqvff88He5FJvi3p0jbwld4QHbvluibcRGKY76NC1AsDA60qCsy0Mb1fBlpQ9AMx8KoG_y5YRz3RFNVnGnGBVZpqWshCGpId4hFWvgsXX1qz8O3jKjZgTeyKR3i1m4X1jTHZSwOSahiJIEnHvsoIS_7k9xFcFwSNcrUQnSfHFkzsdjysy-7jo4oiiHGY9wCphKIVhuf7GGwrOAasvTaY1-SzCfjC9COlXpV0I-0_2RT_f-7jxNIo5OT4RC2TSMrg2M8ttuCqAn5GXb_vd_NZY4NxMzMKRmF4c19jnZDimg0gKk6L_JL4Dx_-Mqt-3AVkcYZTbZ7NDld_l5JeNujlaCLeW4gPyroLhgSB6d3v8Zsa8a-XFp1lgyWZAMQLpjQvQdIpzQqPyVSgpeIFz2jWeUXFsxg48kNfZ1TkTaxMc-_zX7g10TE_uhD8ys3p-10F3H0v3xIJAJAsSmMV9LM58h2mq1wtNnKj_JmEbHrU4zCdbPgBiHMVZEl18BAL1An3fl4rlMmtXh0Qvh7FAnABPa0Iqc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88237cb2df.mp4?token=DebWgmg0zD5BOe7vJNtJO725FmHUFznOXKEJfWa3nbbyEoy4FfjZt77UHzmQvrsoz7Jr320paLoN90H9xtjMxJPyXcYUeNx-hCgRU0wKO98cckH4Pw_Ylu6QGi-dhRpHQeII033fOhu08zLlbcqvff88He5FJvi3p0jbwld4QHbvluibcRGKY76NC1AsDA60qCsy0Mb1fBlpQ9AMx8KoG_y5YRz3RFNVnGnGBVZpqWshCGpId4hFWvgsXX1qz8O3jKjZgTeyKR3i1m4X1jTHZSwOSahiJIEnHvsoIS_7k9xFcFwSNcrUQnSfHFkzsdjysy-7jo4oiiHGY9wCphKIVhuf7GGwrOAasvTaY1-SzCfjC9COlXpV0I-0_2RT_f-7jxNIo5OT4RC2TSMrg2M8ttuCqAn5GXb_vd_NZY4NxMzMKRmF4c19jnZDimg0gKk6L_JL4Dx_-Mqt-3AVkcYZTbZ7NDld_l5JeNujlaCLeW4gPyroLhgSB6d3v8Zsa8a-XFp1lgyWZAMQLpjQvQdIpzQqPyVSgpeIFz2jWeUXFsxg48kNfZ1TkTaxMc-_zX7g10TE_uhD8ys3p-10F3H0v3xIJAJAsSmMV9LM58h2mq1wtNnKj_JmEbHrU4zCdbPgBiHMVZEl18BAL1An3fl4rlMmtXh0Qvh7FAnABPa0Iqc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
واکنش مهدی قائدی به حرکات عجیب و غریب قلعه‌ نویی کنار زمین؛ خودش از خنده رود بر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26328" target="_blank">📅 09:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26327">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=eh30kGVc_TRytYV-yMKZFbvuDleiuNsDM9nAYKkawP9DhfZ0DYT8rBAHG4oNIJUn96xKIsX_BOQzSXRhQIKJxOfOFhnjwMxkJFzMfFM77gAGqTW1h7uCVpq99q6O0HV42MXx0oc_ie-3gBuzGGMh6T_cTD4zoXCUwH8PGudRExMW0GcQQFrXUkLJYjg9ho2oHO0eooWlWZlg7xrMAKkqNr_H_ss4AO3gVIKxlFhZcyi_Ng-52wbTWIKWUmEJ94e760Ryyne8mzEx7IdqnrQiKfo8ZZTT8nNT4R4heGvx_KGEcXvJHFU6WjiNg9RZwNIbzgff7nUuZXoFwEbot5_K8XOD1yTxTMmVHcQ9ZJu_YGIgpJMp45w562TyONlX09R30KcRBszFn9Js6QsAiLDsOiWXAQP67V1a28mF3dpvRQvBlvwEFNmm68vb5Lkfw4Lt93Tfgs4FnXxW7FJ56l4wUwKkPLkh8x9v4h9sMGj8254gtVh053mHnZM_-hgdMq1gyP5plBAic3LlRDkz_R6hOByi7UqpwgvR9O7VgUR99cPEIlWgUp-70hbysDuN8JCaq6Jlp8Woo81Ng2Rv_pZo0pu-eD2ofa-e9g8sniEoTzu8z1mgTrCEa56cjwyEQJ8rXHB_wFqL59zeJUHChifCHaj4yzUHzvbbtlolvZEp3Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=eh30kGVc_TRytYV-yMKZFbvuDleiuNsDM9nAYKkawP9DhfZ0DYT8rBAHG4oNIJUn96xKIsX_BOQzSXRhQIKJxOfOFhnjwMxkJFzMfFM77gAGqTW1h7uCVpq99q6O0HV42MXx0oc_ie-3gBuzGGMh6T_cTD4zoXCUwH8PGudRExMW0GcQQFrXUkLJYjg9ho2oHO0eooWlWZlg7xrMAKkqNr_H_ss4AO3gVIKxlFhZcyi_Ng-52wbTWIKWUmEJ94e760Ryyne8mzEx7IdqnrQiKfo8ZZTT8nNT4R4heGvx_KGEcXvJHFU6WjiNg9RZwNIbzgff7nUuZXoFwEbot5_K8XOD1yTxTMmVHcQ9ZJu_YGIgpJMp45w562TyONlX09R30KcRBszFn9Js6QsAiLDsOiWXAQP67V1a28mF3dpvRQvBlvwEFNmm68vb5Lkfw4Lt93Tfgs4FnXxW7FJ56l4wUwKkPLkh8x9v4h9sMGj8254gtVh053mHnZM_-hgdMq1gyP5plBAic3LlRDkz_R6hOByi7UqpwgvR9O7VgUR99cPEIlWgUp-70hbysDuN8JCaq6Jlp8Woo81Ng2Rv_pZo0pu-eD2ofa-e9g8sniEoTzu8z1mgTrCEa56cjwyEQJ8rXHB_wFqL59zeJUHChifCHaj4yzUHzvbbtlolvZEp3Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این گیف عالی بود؛ امیر قلعه نویی حین بازی با نیوزیلند بدنبال‌ساعت گرونقیمتش بود. مشخص نیس کی ازش دزدیدتش که اینجوری داره از هم میپرسه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26327" target="_blank">📅 09:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26326">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bggMV5ezLwkzCTb9pVPlhe0Pujxy652qiTL1IvjgSDG4ygPSabF1rCV8sFPb09oNpuhEr2mUw970Dwbgp5Q0rBwGyb3N1wU7_pRK-481zKSWk_n8up3qXOIpYPKVn-xg9ffn1jtGOBi-OMze3Y2KHtkOHxM1Ue0A9rbRw1B3d57vqj6qFfuOUhgz9t7QxDLYTZALRwvBWQyVo4Xm9TPWaCPbLtwd4PTreFYjSsYCfM_v-kX_q15SN8eCh6RWGV3Sbo4E-cs84ahi4SwU6IRIFP_P5WGibnj_rI0cSqIZ0ziXNbRSN-QxErFu5MJ6Zl68bZBXohmT9LPugnGYILBTsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26326" target="_blank">📅 08:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26325">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ffe3dc96.mp4?token=B85XcDaxZM2kM_nmrHuDV93toDGegz7GUHJ53HL5mLpClSCrBYW1J0Ub5VEeUlmuFq56HuP_Pw2q2Rs0qD-W7sTZ3JuLFNpfFRkTFo9hOmazajg180-zw27j3CyKBrQ0EmFyjlBjxYit5CoPJarENkhxm9nL454o658b9KF9hSs2_zb0iZAEQjxQ6n3efTdoEZrEmhuwkooBMZvmFCm70oZcDfk8Drlu1oj0AQPKpdXZMyYpwSqVkXTekY7MgiDYD5RElinT0295_1NWYV0qpXqUy_PI6yD1uE7mD4i5GcZtCc_AfgRd2LnYVouKHeYagLx2KMS94hMLQuAs2EQTlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ffe3dc96.mp4?token=B85XcDaxZM2kM_nmrHuDV93toDGegz7GUHJ53HL5mLpClSCrBYW1J0Ub5VEeUlmuFq56HuP_Pw2q2Rs0qD-W7sTZ3JuLFNpfFRkTFo9hOmazajg180-zw27j3CyKBrQ0EmFyjlBjxYit5CoPJarENkhxm9nL454o658b9KF9hSs2_zb0iZAEQjxQ6n3efTdoEZrEmhuwkooBMZvmFCm70oZcDfk8Drlu1oj0AQPKpdXZMyYpwSqVkXTekY7MgiDYD5RElinT0295_1NWYV0qpXqUy_PI6yD1uE7mD4i5GcZtCc_AfgRd2LnYVouKHeYagLx2KMS94hMLQuAs2EQTlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
تیم بارسلونا دربازی چهار آبان‌ماه با رئال مادرید با این کیت جدید به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26325" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26324">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851f45a809.mp4?token=iyQBnbAhiacVuGKfY8PeLDIPI_3HS19uR-VVLj56Qm8tTAgiDPgMjRVsY2CTTRuhWZfnDSWOkB3pNr4DTz8eHuSJ01-OY2TtSfqOkSjr1hLTugNxnZczQGUqwgF9nNImNmnzoOkjq1lvrTpjLAFn0fcEogv-j0mQX-vVCnDVLLfjgNVhwi3i4L8Fr8tlc3iEKcW75ovLlTDZJ5uz_ghRe6C2I-x8c-PfTCCzv8tVL3RwHfr8POczmE9oCtH8oR-a1NLESK4AgMjSPPOYb0ZmNzGy1VTWH63AzwqOvyOLA16tZG4Ua0fst5zccNemfgonmrzWatdJvq7rGgkgB7TWXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851f45a809.mp4?token=iyQBnbAhiacVuGKfY8PeLDIPI_3HS19uR-VVLj56Qm8tTAgiDPgMjRVsY2CTTRuhWZfnDSWOkB3pNr4DTz8eHuSJ01-OY2TtSfqOkSjr1hLTugNxnZczQGUqwgF9nNImNmnzoOkjq1lvrTpjLAFn0fcEogv-j0mQX-vVCnDVLLfjgNVhwi3i4L8Fr8tlc3iEKcW75ovLlTDZJ5uz_ghRe6C2I-x8c-PfTCCzv8tVL3RwHfr8POczmE9oCtH8oR-a1NLESK4AgMjSPPOYb0ZmNzGy1VTWH63AzwqOvyOLA16tZG4Ua0fst5zccNemfgonmrzWatdJvq7rGgkgB7TWXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های‌ابوطالب‌حسینی درقسمت‌آخر ویژه برنامه جام جهانی؛ هرچی تو دلش بود رو گفت:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26324" target="_blank">📅 00:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26323">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtRzxfuyyRKUh8KgiopyrixBloVAONkmxsoOyb2gYtePnpsH1_XGI8o1h1Y-rNv1BDUk1EUto666vrayFGwlj47j2Jf5umokwgNNMcUSbTy2GRvDvwHFI0ENyjvte8cQU6_u2tZCdt24iWKzpzLrszyt7brqz3NTnGrGv-hDx1iqrdbMwcn3MeIyIzdIp9i2Rn8tJfYqIE71wff8j2odV72xlOuxjzq9cfLiACTOfn4keK80IiBGs9rUl3SF_wjt0YY2bYSc8WBiz5Y7zHflzWuYKIjX5iBZWshRPt40FqlLBP3Iv4J0wrvMIhMX3FZebWzy1F4iMAt3HRRtvR2q_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26323" target="_blank">📅 00:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26322">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=dT_yAcnGFKArKsyFlglnn7Mv-IEzHSe77biEw7AstkKiSCy4Nj6lEri5AzrAFIMdvkS7gb0syHPsHDTbzRzA2GNAkhOn2DjyAWIyDpauCc_NT8LyIXryRaqiJjxiw5osUI7VObtoUvAfgDI_61qhH5XCkijBy9KlEUVaLdwz32iYXm6CwiIBo6a0x5SpvYfCB1evssWMHttU7JvoB86NNkxkuv80NoxW9_bMt5tT4kEU-PEXVbPQblrcHLGF75GseVVlO8zZE6kFwTnA0Bz3xg46IE2wLlST1Ow3lPBldv7F36R_WoPj3TbTqTlWZ-K-bpRyrhhlaQ5_vlPID4r5eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=dT_yAcnGFKArKsyFlglnn7Mv-IEzHSe77biEw7AstkKiSCy4Nj6lEri5AzrAFIMdvkS7gb0syHPsHDTbzRzA2GNAkhOn2DjyAWIyDpauCc_NT8LyIXryRaqiJjxiw5osUI7VObtoUvAfgDI_61qhH5XCkijBy9KlEUVaLdwz32iYXm6CwiIBo6a0x5SpvYfCB1evssWMHttU7JvoB86NNkxkuv80NoxW9_bMt5tT4kEU-PEXVbPQblrcHLGF75GseVVlO8zZE6kFwTnA0Bz3xg46IE2wLlST1Ow3lPBldv7F36R_WoPj3TbTqTlWZ-K-bpRyrhhlaQ5_vlPID4r5eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چیزی بهت میگم قول بده به کسی نگی؛ دو ثانیه بعد: چه میم‌هایی از صحنه در اومده. بازی قبل اون حرکت مسی مقابل بلینگهام میم شد تو بازی دیشبم این حرکتش حالا حالا میم ازش میسازند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26322" target="_blank">📅 00:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26321">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی بینید از پاس‌های فوق العاده هری کین ستاره بایرن؛ مهاجم‌نوک‌باچنین‌قابلیتی به یاد ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26321" target="_blank">📅 00:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26320">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yap-68k0PTDRDhIDCzwAFiy0ecITzkqAXQaXVotDSZnYA_utvKOJjf7itPG4xgG_mNHbdEVgu9otq1ZXIa10wBz0D0de5uT6B9tTWtG1HZ_FjJr-8-ChgwswP3TbfKjBQp89fsjxvmrLPFcV6qwtfJI5NNDkozZghwQeiZT-3uPM4nqe9IQ-hZ2kVVtgYcnMKeru-lRXXopy19JEjbrR38EAer3gdscMYO7i_xiSODcgkxkiro_9KHK-nhDkAgL2-M4Z9ETY5D9XvijP6XH1O043gWSswKEgdDFwpqsr6lr5eCTIqT5vFFXu41nQflY4hZed5dSfaUFNXYhfp5lyBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26320" target="_blank">📅 23:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26319">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-8waKmdK5HiL2-NcZFAPR73bYEUNSWpuqm-4bfBJMhAn23l7rIjbe-r46H-OWmoG08Bc6b2iQ_UkwlL-ZmUTfzFfF42kuibceSEFD_6QksKJuv8PcGARRsA7vadr6ZU2suGdZRvqZ4nchkhge2_xYu44FC_5Ub686WCidWCUGFJ73zeC60iLVmucve0Z2z9eoSA1Scii3WM9VYWsxivkarn4R2Ae-LRYMjA1ODzaNaec2LcW8POOjbgFCN2kJZbhX0dFeJ-uQJAQeQvRlspxlY2-VpMvHZS6mpFCBsO_WeCgtYkCXD5CLPyREwR4dXSP3K1AvmeQLYecBV_FFuw3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبر اختصاصی‌پرشیانا تایید شد؛ تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: با مدیر برنامه‌های یاسر آسانی اختلافاتی‌ داشتیم اما درتلاش‌هستیم که او رو به‌‌تیم استقلال برگردونیم. آسانی فسخ قراردادش رو به‌فیفا تحویل‌ نداده و ماهم‌امیدواریم که او رو راضی کنیم برای…</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/persiana_Soccer/26319" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26318">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTSuWXc2iJlVH0zyNM8nScXQR1GlMqSpHc4oA0Dk4KRZBeEhkgxpzxvs2zRtcv3-7RO8b-kRhVsElUKBP_N_3qxG2O0rufN4uNpTUDFllHDSyVOMgz7I8D0cikKArwp-BIeOWU8a5aDHFGQV9qEstPLOEwYS9Bqgdwe64_TxUxIo8wDJDltfQZLZAWBUNp26MXXXyHfv4WcrIPmhw22GyhOdaPxS3dswv50hXxGyCQai-EhIrCiuZJzUBsTi163W0FX_Iwm89EqJBfmCfGrn9V984ElhevQxk_5RuvWmWiq2AFAd73YVJbhk-F_i99Za1Kgo_D-E0VlcMxxZSBv8QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/persiana_Soccer/26318" target="_blank">📅 23:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26317">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HuKQXZ2huetN28mVZEN0teB3wWuB5JU0DYdK-Ar7bbKX5o7BDDmvXbH6BJIWwK57DiyrAk70hAsh1zQ7hPX_q1bx2MZhviZ8YsxTvKjHS-dDeb1gVl-YqmCrusn-4bYa8W2hNTnwKa9hsb4jVs8fJE7Vml1hmRNfF9144NuoCbglTaDOAlxd2M83m9gM-oEbJNBKR5SBp5J2IAlfBrd0wMt3BR0Oyi7W0nQ2Azpu730j8BMMP6v54Kb3-3Gpjp8BDjeqFPvh39vSsX7JnQJ8vrDweUOITZTCF0u9ai7I5kDreI13VpKdo6NJBRcLU0WbfKGS7cr9vHLMFzUfBJ88uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
آخرین وضعیت دو خرید جدید پرسپولیس؛ محمد رضا اخباری صبح امروز به پیمان حدادی قول داده امروزعصر یا فرداصبح برای بستن قرارداد خود راهی ساختمان‌ باشگاه شود. دانیال ایری هم دو شب پیش‌باشگاه پرسپولیس‌باهاش‌قرارداد داخلی بست و به‌محض پرداخت رضایت نامه از او رونمایی…</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/persiana_Soccer/26317" target="_blank">📅 23:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26316">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3gdR2vIrIJ9uWINsgiR4pCNk_i-0mQ551CJQOr-VMQWkq-QZdtTDjDNSPKzBvr3gTbNAp9dBL1AxFsw_BjDPv85apfFG7kUKq-zCF8iK5p6e14XQx_LGs1oslDIEQbtXmeYNTI2Tf0VH6rNcbl4a61OXnUNvKTy2qgh69lwfNIUdX_5YduBz7J91HmQf9beiYMsorbzVxKg56d2i0GXfajxpvX28pCQGFj5h0PPEMJVOgqX544bGxPN6XzYL-6B6rljBNYdNYLai7UAJx9nyOh5qr6WoIKZbUAcPLVRJ5dlyVFbu_t55Z3cCWD8jyx22h3f2MW6aPAo_9i98MGp6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق اطلاعات بدست آمده؛ قراره امشب یا نهایتا فردا سامان قدوس پاسخ نهایی خود را به آفر باشگاه پرسپولیس بدهد. مدیریت سرخ ها پیشنهاد مالی سه ساله بالایی رو به قدوس داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26316" target="_blank">📅 22:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26315">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xv-ziurU8ccXBwRj-zvUbAU7lLrfddLWTchaoYyNGSBJN1m5ay4s1CuHpxrPslCwg_CmIQQqwK9Q0kRCLhRSWk2UJN4lOpJr0QN844KK8hK1lW0-ReXTv8quC6d96hDlLu824tzeweK2SiOt9joe4erdQUN5zpN1Fs4N-ihdiO7xvrXD3GS5iXEuHuGsuYzbHiDcaDG6cMbOSXk_NyjXTYddKAduj5QPWXs_OsCBScLiAmdXVep5S1_mpUJjxwzNHyXP8wS1njizvwwUQto9T2bi-x21XS3ykgD_TrZ3WvydZnHbGyX_WBdYH93rU7_B6-im_WhjZId7XRcSKkK8Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
زین‌الدین‌زیدان‌سرمربی‌جدید تیم‌ملی فرانسه روز به روز بیشتر داره شبیه بهنام تشکر خودمون میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26315" target="_blank">📅 22:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26314">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrCU_I-NcxCEstQ2oomzvpylHCZORVX3KdYwtS9KBlL6RCIer57CENeG8RbR9H10nhd17t_6y_HUMm0iDFrpcAN3syKp5ppi3eWy2tQThxyldVE4wwjKdJpdpd5xiDIXqoR-xVl7LVxgQ1hduvGuEjTO_qtyPu0FqhhBxIb1snFPhnmRhP4Vs1eR-ix3jQIGPbCMLRyShEh_LaDdUSToRdINKwquX77jC1SDAAdXvAMohexNT75umpHz_ozIwSm3HHm548I-laFviSBdP7XAbbiGtzUgk4U_SWDeXAmhODKUY4Y2i5LpIS-4j1X5VOKJ3sCgOcOPCITYCpn3qekKZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: سه هدف اصلی فلورنتینو پرز در این تابستون که قولشو به مورینیو داده: تمدید قرار داد وینیسیوس جونیور، عقد قرارداد با انزو فرناندز و مایکل اولیسه دو فوق ستاره چلسی و بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26314" target="_blank">📅 22:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26313">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3oMGwTGpajZSeQqOEKDWEHtRkwSYQuuRF_-l-Z3Fj9jGfdv5JDDR04yxM-MFPBq75qgICjGxaT3twLGHYR-6ooSss6fJI35g5i53-CVOH23deHrJsJ-PA8haaJe9E4t0eLPRrHBbuxHWr_ZFXLubm3pPdsMw5mc56A5oOS1W9o5gp6x0tuQTc3BBke_cuI2KwWIEyl5GGOdBwEYxb5a065YUraAY_7jbaNN4CxSlFyc7jSl8eKMm9nM4vE9OBLJd9cV-AiwBOGJeTv2vNtj-2vWoGAznVilSN-KuGm_bYFPDkfr8_DyrNVb3iX0s3M6N8tZUvVvZTvtXxZ9Iiix5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26313" target="_blank">📅 22:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26312">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2YJ3Fdxt2cJVFQE5Jv2PRVX4HuvSuaiQf0hmXyAnLDBHQPIDytNdIMXqZ40M891_lrfEnAmt563x6eKroli6SZXxC5ptY-YYInJrVsgAYOjcprEGspG4XuX4ogdxArOd3Pgvcyd7Q0BNrPLZUs69ca1_2pVjqQSp97kthsDZSDEpEpodQ6Zq6QSGl1cqXzb0wh4Yj5hSO8NzyHyrrl5BvK92uxhTleVXJ2sUQkdRYANWEUuaP4RbOFEIxdveyeIx9WWggHfNP5ebKIjA3cYG9SeH-40IrAVHYmIDQWV14TxA41izMf-e9Ncw73hcWvTZUnMMhvBIdUiryD-gt8umQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فابریتزیو رومانو خبر داد:
کریسنسیو سامرویل، مهاجم 24 ساله و هلندی تیم وستهم با قراردادی به ارزش 55+10 میلیون پوند به الهلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26312" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26311">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQTLbQKuWNy7ZekiJoQstcuvpKYe57dowm-VpUhmWD0MZHUIjoa7_Q7zR8pyLy_dRwPfvZET8_DnQQjnV7gQlb9_yikRbQNGe62SsSi1qJcxMlb4UMgtyTtYnDdNf9TJK7-MK13AZlSbyE_e5Qor7nPkORcrRkPxZNZOcHjphxeouGq2TUADqdRedOd0JwR3UmWEWD1hRyShShkLS7ahV-accdaWG5kOqsFdEBNUEGlzxzr8cJHdjyqdUMk1hwew2J9YdRLlMyj8SlViaSqeLxf8eNDsXVGLOCiins3H6ylhU6vSi3AB0Rfh21QLeTS_PQS_l3hTWZOqQMLLil7wIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26311" target="_blank">📅 21:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26310">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBICCKxfCNlzWfn41H1ENSYQawpij5YzscDH-csPWyMe9kS1jw7D2P3bPer0xQB8IIe46KvQ8ZOF1Ivf4P7bn3LEeajjZiOV4ME3UXe56pFDy6DUHBQxnqCtKbGzAU2zC0F_fNsFUnCJnGMLC3EEYc894CQL0b16MM3VbPxLnfnASW7G-Lsnwx8nXYe9xIwXWBRZjH28ZxZlYZ36KC-IaRskU6zfV2htOoVLVXYdJDXebT79NKv4yJFErBC-crvndcCgblGtysldaatl7GIh6k_dAF6Q5ZpvJoKdMW95zItBO8EuVDIEpeTplfv-vvEkPkjy4ZrgD1TuNia2kuBqQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج رقابت‌های لیگ آزادگان در پایان هفته سی‌وسوم؛ صنعت‌نفت بازی پایانی مقابل نیرو زمینی رو ببره‌میره‌پلی‌آف اما اگه تبره و سایپا بتونه پالایش نفت روببره سایپا میره‌پلی‌اف. اون سر بازی پلی آف شاگردان مجتبی جباری در مس رفسنجان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26310" target="_blank">📅 21:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26309">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQC6HIk4iFbURnbInr-5VgKpiGKy6dmuFMpqZ9z-dHDSkxvi8rmczhBsURnrruaOqTalkTBW-d6xJDS62WRi3o1GPRC0TA37Hj_X4dtWI-tFb5WHLHpuAQ96EIWbyrJ2e82CjivMOWHUDFJCtQ_EcL5udburgKADZQLFMWQSSIPg4iFh4sY-1mE-tUeuMMXrffN1xBGm_nfLgoPiA3Fn4mSUCFyqlhgMCmmxHPb6APQvHA8vrm3HsikNtFDDFy8J9KohD58FTOQH5Zm9qD5A2-sLJLYVvP41AZASGY9LO6YmmjYg-KQhOqTmedhYY15U7fQoKL0d69Q5HqQsiyy3QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛درباره کسری طاهری ازمدیریت باشگاه پرسپولیس پرسیدیم که گفتن امشب یا فردا استعلام فیفا به باشگاه ارسال میشه. اگه منعی وجود نداشته باشه طاهری فردا شب با حضور در ساحتمان باشگاه قراردادش رو چهارساله با پرسپولیس امضا میکنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26309" target="_blank">📅 20:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26308">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a142133503.mp4?token=LQgmxWEzM5RxoKJA-kZwnEWxTbjr600gtEsoreBcu0puLZ20Pkq5FPfXtBC_OmKPAnkgOI8VT0i7D6E1w9U7FLiqc3mbM2Ywah8QbgmZulcBuqZKOGOumweBwLaA5eN-dv2LSKV3nhfohAGIkEKUYm7VEYPDoa8kpV4VZIIsF-iJsC4W82xVvNNppt9JMIt1sPH6199tvH0Jd5h3sE-KN9qc_jhq4FTV0uFjPE_RA1jDO5-hQT9UigpeAX4hm1uFFc2xXLEhL3d6-YcaSVV8pAUEfS1j5ALFfzFCm_eGGTWavPLm-zHtugu3Pd_5duUhZMTMxqaVx6bzZWyf_KbrEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a142133503.mp4?token=LQgmxWEzM5RxoKJA-kZwnEWxTbjr600gtEsoreBcu0puLZ20Pkq5FPfXtBC_OmKPAnkgOI8VT0i7D6E1w9U7FLiqc3mbM2Ywah8QbgmZulcBuqZKOGOumweBwLaA5eN-dv2LSKV3nhfohAGIkEKUYm7VEYPDoa8kpV4VZIIsF-iJsC4W82xVvNNppt9JMIt1sPH6199tvH0Jd5h3sE-KN9qc_jhq4FTV0uFjPE_RA1jDO5-hQT9UigpeAX4hm1uFFc2xXLEhL3d6-YcaSVV8pAUEfS1j5ALFfzFCm_eGGTWavPLm-zHtugu3Pd_5duUhZMTMxqaVx6bzZWyf_KbrEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پاسخ متفاوت و معنادار پیمان یوسفی به سوالی درباره گزارش نکردن بازی های جام جهانی این دوره
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26308" target="_blank">📅 20:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26307">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=ttR6M253DcF6JrQgxepRw6GPOs2Yet8wTptTIkxylfTASS5j7OOFXtnbaR3TWub7VsKzKo1gtsL6B1bRy7Pn24OkDxKXv_VTcriFcvL6ZUkYHR-zIdIouee_wEV2igpy2nBtnXrd5dfbbjCf9Ai8-xfSdkfSYXPEWH77qpAwjU6CyJPN51uq1a3Ve4Q-uRZyJ9Xox0GQ7F_f7MbFaX54a0uILYAeCb0WTjNccepp-NGulPbDAOQkgT9Ik_NPuSB9alWar-4RnWf6W6Y-43FiUVm-Z-Jk4LZHXC3gtiILVMaKttK0dAl_3GaSf80elkqr8SHJkpYTygaoAccXA7Kv2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=ttR6M253DcF6JrQgxepRw6GPOs2Yet8wTptTIkxylfTASS5j7OOFXtnbaR3TWub7VsKzKo1gtsL6B1bRy7Pn24OkDxKXv_VTcriFcvL6ZUkYHR-zIdIouee_wEV2igpy2nBtnXrd5dfbbjCf9Ai8-xfSdkfSYXPEWH77qpAwjU6CyJPN51uq1a3Ve4Q-uRZyJ9Xox0GQ7F_f7MbFaX54a0uILYAeCb0WTjNccepp-NGulPbDAOQkgT9Ik_NPuSB9alWar-4RnWf6W6Y-43FiUVm-Z-Jk4LZHXC3gtiILVMaKttK0dAl_3GaSf80elkqr8SHJkpYTygaoAccXA7Kv2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
بادستورمسعود پزشکیان؛ مشکل پلتفرم و سایت عادل فردوسی پور در حال برطرف شدنه و عادل پر قدرت تر از قبل برنامه اش رو ادامه میده. مصاحبه مسعود پزشکیان رو تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26307" target="_blank">📅 20:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26306">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiuLzan2ere7l_9WKsQ7oPPf5JgpWs5wqJvOZVyQbsvAX05gvl4NHW-50a02KLh2ZYKheX5GkGKjcDHkdVuMYGFg_zMfJkqBueUAeygUd4fLE8GooSgXI-gMg0sR-n9v33dvkCrtIIq2Po7UOgGFRzhUItjQ4noA0OyOQ9MHHUpupCf5-eNVQ_quH_64tVqTBkrTt6wLBbEX74I-TbemoLTFbgxiF_8MYFMLzmWq3yTBOP9LviyTGpgW0Gtw7N9m527x0rv9WwWVkiV6LrbLQfjhK6CgYbgnDqS4fee1UdCptSKahrAVPskBRwB4LrFV6SRIuz_TklrLOuoOuIgBzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇧🇷
رسمی شد؛ کاسمیرو ستاره برزیلی سابق دو باشگاه رئال‌مارید و منچستریونایتد با عقد قراردادی دوساله به اینترمیامی پیوست و هم‌تیمی مسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26306" target="_blank">📅 19:59 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
