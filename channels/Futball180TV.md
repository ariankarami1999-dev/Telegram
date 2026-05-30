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
<img src="https://cdn4.telesco.pe/file/fc8MANGoyFNWxknRR5CfwsiizoY7uJ93h8rrzsZ-DfY4Th2vF03rWinw67vXyoQzFa4dgKTY0lb9K_ldPqFXbJ4oXMbbO3KbmU4_0hxLDpftP-YW376m7eW3rDHlaBvY-WwjYTp7DY9jj1lcOsxn8PGZ_rdU4KSMz93c4UQq9OuzEnYt_fta2X41BfGNYROmNsB2x0F4CT2Pmdsy9sJEjpcXMMuBo1QtXvTtiH8z_Y4LbkRqx41BWmUL__BK-tzMJoLN9uBu7OtxBCmgx556uKWRx_mnbFH5JtSii3DMBEu66uYmWGT5Q-qCBJCLjGZY2LYV0PhbFeaPA-hvow_i9g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 126K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 08:36:32</div>
<hr>

<div class="tg-post" id="msg-90437">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZGdwz5PnM1mscdMsEAwK516bfk9X6BD0MCRKQXvEEZkT-5jMRPg1eX3sfA8XDHgzNg8xcx4ScOJkYGlVMawLlUeRG_dfUMiCc2sCbVk1Zs1IDQ25ow9doGHmq0kNFMgcwXOuGno2JxFYXZzk5oNHuAcj6cHPhWkV7ZvdRmiHsZP7m5Jga7d61m0D1rmcl9nm4Tfe0X4eiyIyGE-AHpvb20Er3JXeiZHsazOxqk89vnQ6ybjwUlUDGIGO99Gsxgxe1oLh_3qNPWS5hfdhSbaq3bPrT0BSO3HxbeBDEkBpY0868xGDao66ooUDkTlbBIDTkC1L0dg4ZhkrUgRvxPsJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار و عملکرد رافینیا در دوران فوتبالش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 354 · <a href="https://t.me/Futball180TV/90437" target="_blank">📅 08:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90436">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
😮
تنها سایتی که با عضویت بدون  واریز 500,000 تومان شارژ بی قیدو شرط میده #وینرو هست
💰
👑
#معتبرترین سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال…</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/Futball180TV/90436" target="_blank">📅 00:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90435">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_iSDQaNz0h0DAqU4Tj_rtxMcrOZMXmzL_0Wsz2_CGhF0pkkdctQEeBIGAKykVprcLvWXZHlO6bRoWFnVu3yq0X-YX557n8BUz_XWuQXdOmC7SCjYZCYlsbQr5MKANMLc-isNVTcAKFi2PD1XrkZdgsHLhn-nILje3uZHKuYa8Jbk7kkubVxcmhUQrBYnOqfy2hsd1MjbY7dQuf3aYbNPIUBDeJAxgG_WI590OV3EVDOS7MDAn0dC3yKiYuWdz-SP70dFAyhVgwxKSORJ5gpb_Ik-MmmSqYVzywHoCFkdvUGdSzRwNI-KCcSrZdUTmA8NaDJHDK-V0guyczCUiXUcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
😮
تنها سایتی که با عضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا
a8
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/Futball180TV/90435" target="_blank">📅 00:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90434">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltZDc578FFEZf2ApRAdm1GOzIVJgrrtrV9VzF9Ixc1Bg88LxUK_2hweUVkVHomk2byjamg6Yg4qqtgjOPvnu2ga9UgmG-hbxbBeDUl5_aDPU5_OtDemtpR7U0crSWjIH8AhGYOd7k7WXeNAPkOqgHxGAs2DYWEgKnXLRHn1NW15-K2miUbADfSt9rthGs5zVHgraa3MJEC6PRYaDTmVyjTGpMzJB9lNYRfsevGbdqpIkyIgW8zHuOqHnrip9gLRqQ6jK39lIKRYqGSWrv7hHE5F414iblzA-YDujrL7RPIp45klPqZqOaYvuewQkZSzz3UybfeqeDUxrgD0e7BMWMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساپینتو با پافوس قبرس قهرمان جام حذفی شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/Futball180TV/90434" target="_blank">📅 00:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90433">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مجوز حرفه ای سپاهان صادر شد و فردا اعلام میشود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/Futball180TV/90433" target="_blank">📅 23:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90432">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJ0v2i_izd1AazGWeYsjgyqevLO55GYS2FqDR3hbJYN2ti35bRPXxJXRcZ5TXuomFpJWY3vXjNXtTfKfOcODlsxaXoZMJHbenX1xXPaoshBR6tcN2uBnYBSd2MelJYcTlQ3qvpUwUDNRteh5aOJ_MCKyxhWMblYj3FKs6aGz9BKtkBZarEjrkD_nw6KIknY5GE9siX0ykY5Yy_h0QY0fUEjG8OceeqY67P2e9N-dB4efwbpOFQ-iDFx7mZQaVHkpkEXDhc6uWJAM--7WsLv3oWCN-bH79tWgcze1_U3ccbHgQyYYl2hMc9V1JSMXzWk7IRci72meMyKj20G2XbvfPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوری و رسمی
گوردون با قرادادی تا سال ۲۰۳۱ به بارسلونا پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90432" target="_blank">📅 22:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90431">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvwq_I_DoCkKethVsn2ofHsLuIVAN3j63h31gXGvofs9jf_gQHCix7lfzhU9VcxAXxQeG1Rs29uqf4mm_qnGaFTvNWjPXbQgWAf4fQrWHg7Ak4YFQgQi-8ZRUjCkQLUXH6sKBxTcd8lcAL8gR2IZyBvkfRzZTXcStsFMXxASxCelTHjRl4_wL2EPDJNEyYQGiSfCQ7uNDVoDnUeYoO7fD1loTed6glYljVvEqoOWiTxCQeHK6IBCBmh5Na8Y91n2cyI_7MQuF3Dqhbh99WLRp6uner1wgCyYSj2PKXN1vJnn697Dbkfkahoxm3AaKfjYxAOCvvJmOObnx6E0bsfWUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست دورتمند
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/Futball180TV/90431" target="_blank">📅 22:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90430">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnkizbXhuwzsUYjuQ6UISKXyQd16krr1ok2u4ys9-CI1jjugFYekNqK8vNCVX-iHlO737J5wbfegWZ4cbp79JGsPOKuyM2azwwbpXQRmtia7cXOPa7vU53I2-s1fMviyYlO8dEKGUQ0HmKLwLMXtoMk8RcI0dyk8Oz1m5X75nel_5AICbMZCwOxL0_1OkcEiXakpSKfyMAHQfW86uWNxy8YX_FtPU6cRgekzln-Gw41O-L3VJIXamaXoIWKY3ZHVqi6g5RpqgMbYLzVtVwaUIwvhgS58qW4ln1UYkLCgzeK4Jb7I7qtS9LuNx9C58HF227tOOPhXGfWcTTrFurAZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اتلتیکو مادرید بیانیه ای طولانی را برای روزنامه های اسپانیایی ارسال کرد:
خلاصه این بیانیه این است که اتلتیکو مادرید به دلیل نحوه رسیدگی به پرونده جولیان آلوارز از بارسلونا بسیار عصبانی است و معتقد است که بارسلونا به جای مذاکره رسمی با باشگاه، از رسانه ها، افشاگری ها و فشار از طریق خبرنگاران و عوامل استفاده کرده است. اتلتیکو تأیید می کند که این بازیکن برای فروش نیست مگر اینکه بند آزادسازی کامل را بپردازد: 500 میلیون یورو نقد، و او تا سال 2030 قرارداد دارد و بخشی از برنامه های تیم در فصل آینده خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90430" target="_blank">📅 22:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90429">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎙
لوئیس انریکه:
به آرتتا می‌گویم تو هنوز جوانی، پس بذار این پیرمرد دوباره قهرمان سی‌ال بشه، چون آینده بزرگی در پیش روی توست
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90429" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90428">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYKiqf2QXeXwfkWB8VrCZ4uNu0v_PxwS-BLpd4hg3FwKLLrlqhCyhqyvkrl31W_GDRFfI5S00vhBo75AXXk9ZVmlCsr3CNyVR37WiS3jCBp1SB2rqTasEAOapDT-gvPFQa9v_Q9WCA7ltDS5RrEwrMysS-7rhknzn7mjGUFQwLp_qXt1fjJY1QDyMwpQAe_P4x1OqLNvCff7LtooJATEMHdBqu4hr6PB8mvEsdVyUJ1TatGNUy4uYSah5nNSCzPsFMKQhMw3EagQ1Xun_EJyiKpDuqtMDLUkDQKVbQgMT3kXtkqhNe44Fo_muh0eBCvCYmm9NMez0Wsx_fiO8-v3SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پاری سن ژرمن
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🏆
فینال لیگ قهرمانان اروپا‌
🇪🇺
⏰
شنبه ساعت ۱۹:۳۰
🏟
ورزشگاه پوشکاش آرنا، بوداپست
🎲
با بیش از ۶۵۰ نوع آپشن پیش‌بینی
⚡️
با بالاترین ضرایب پیش‌بینی و بیمه صد درصدی
💯
📊
نگاهی به آمار دو تیم:
✅
پاری سن ژرمن در ۹ بازی اخیر خود در لیگ قهرمانان شکست نخورده است.
✅
آرسنال در ۱۴ بازی اخیر خود در لیگ قهرمانان شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پاری سن ژرمن در لیگ قهرمانان ۲.۹ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر آرسنال در لیگ قهرمانان ۲.۴ گل در هر بازی بوده است.
🧠
وقتی بازی با فکر انجام شود، باختی وجود ندارد.
⏩
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/CH100
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90428" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90427">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d5ed95013.mp4?token=Lbpdq6UQupaDyIciLZ_TRDgXR3U7c1xZDFGT8QJ8eRMueN0JMFx6hHrYlTq13OUOQmMqMfX8sFoRtaFLEvfe5c6zZb0uN711Yq4XANRk7mVqefMgFDDSYfLi1U6_PAhRm2FZb8sLotRNGsBviJyALOAlG-XTXgW5stsQu9ouisPdHnYgWF_UJTzLmRtHGdLz0gds_WSqpeNwcpUu_Q8W4SWc8JOmlVNcRtkS_mrJtSGvZjNo8H9ghP6hvcxwRzxQ1kCe4pMFhKVXEx4-QRvEiu_DVF3t4o6nXAGoZr_MhtxvnKxbSAV0mu0gg7adnx1dpkefqs6YxKqRBmUUNpJ9Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d5ed95013.mp4?token=Lbpdq6UQupaDyIciLZ_TRDgXR3U7c1xZDFGT8QJ8eRMueN0JMFx6hHrYlTq13OUOQmMqMfX8sFoRtaFLEvfe5c6zZb0uN711Yq4XANRk7mVqefMgFDDSYfLi1U6_PAhRm2FZb8sLotRNGsBviJyALOAlG-XTXgW5stsQu9ouisPdHnYgWF_UJTzLmRtHGdLz0gds_WSqpeNwcpUu_Q8W4SWc8JOmlVNcRtkS_mrJtSGvZjNo8H9ghP6hvcxwRzxQ1kCe4pMFhKVXEx4-QRvEiu_DVF3t4o6nXAGoZr_MhtxvnKxbSAV0mu0gg7adnx1dpkefqs6YxKqRBmUUNpJ9Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو جدید اتلتیکومادرید علیه بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90427" target="_blank">📅 21:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90426">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrUPSpUX6niMz85UzvycxAjY-si5d_eWhrZKJnhhxbvBP73y_SsHyH99CSK_fng1QxfbcMDHGNjnfhoxdXlomL2mHLS4rzvbGa1Rw8NCphc8xpecIa0TVA5SnSMVgRyuhe0LYCRbNCNDqi4Y5uQvLjCUyC2fJ1hWUY45Zn8xTE3bheUUycuhD-86iOEXMhumOvl_tUqUV42lEv8YKDvBdP1d8Lx2kafzy9fO4bEX2eSRp8v8zJHY6YyoGhVZnhU7uNPUffGATdW7kEnlbrfYoMPzgte4aniBJVsGPZ3i4e331Ka0bo_BeO94_Ba1ir3e6fUxMid8jxMmHFI5mlv6Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانه جدید اتلتیکو:  برای این پیشنهاد مشکلی داشتیم، چون متوجه شدیم بلیت های کنسرت فردا تمام شده. پس پیشنهاد جدیدمان را با ۶ بلیت برای کنسرت یکشنبه بهبود بخشیدیم
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90426" target="_blank">📅 21:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90425">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تیم ملی ایران موفق شد در یک بازی دوستان ۳_۱ گامبیا رو شکست بده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90425" target="_blank">📅 20:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90424">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34e3caa05f.mp4?token=SRIdOaTqu7fu0WibDFkDaj8N7IQxorhY4b58eN6CUV0JMmijQgxI0DAaIRCuvTAThw16vsiXCIRyjF-zboNs6_8e7h-kiHCSe7VRtYYqVaEr1NRh60SOKbAC3VeFfyZEikmtD7C8nouc-OgNu7PUahAbzUj-GyJ2X1BB_i9ktCki9l6Wo-UKtxSjP5YMXAeYATPPQxJWE7T-1gQl5Y9h2LPQl-i6B8pWOzPdlzNGe61EbPRT3ErzOsh7id1q6_N1DwSEQs6HhcmRPWc5OV9WZBWEQN08VN4Z-X75QQpEkHgQ4oho4Kog8h57HRiSHgskRmsFzTt_-gl-ti9BTc0lYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34e3caa05f.mp4?token=SRIdOaTqu7fu0WibDFkDaj8N7IQxorhY4b58eN6CUV0JMmijQgxI0DAaIRCuvTAThw16vsiXCIRyjF-zboNs6_8e7h-kiHCSe7VRtYYqVaEr1NRh60SOKbAC3VeFfyZEikmtD7C8nouc-OgNu7PUahAbzUj-GyJ2X1BB_i9ktCki9l6Wo-UKtxSjP5YMXAeYATPPQxJWE7T-1gQl5Y9h2LPQl-i6B8pWOzPdlzNGe61EbPRT3ErzOsh7id1q6_N1DwSEQs6HhcmRPWc5OV9WZBWEQN08VN4Z-X75QQpEkHgQ4oho4Kog8h57HRiSHgskRmsFzTt_-gl-ti9BTc0lYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم ایران به گامبیا توسط طارمی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90424" target="_blank">📅 20:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90423">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1fd30abfa.mp4?token=bVpZT36cezftsz9UkR0fJl8zNX3wevuy349wyNKogcRQj33dI_cOwdm1xW-6_8bCpAWAUKdKajI19RXcwkNNyfeb-GLs8Muxcdrf16o_qXONPRtk5iTw191YWPghvBwsgxOA63ep6jD6zAzxwdG6Lj5Y0kH7dswf6Ppn-c0uYUOapVCfEt1Sd9334Je8hkyxuE6T4PMXX-28lyEPuOP0TbHR43ZgAZtkD-2m18GHnoVw6ZfVUrXVT9RzlFVKgx7bM-v9CxuwietHUwotPBvWYh8ZpZOGgPtOwACLxgQEJXc0s2zljjgUNoULMiVVrDEra9gqZeWPX5v8fD1znzlA1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1fd30abfa.mp4?token=bVpZT36cezftsz9UkR0fJl8zNX3wevuy349wyNKogcRQj33dI_cOwdm1xW-6_8bCpAWAUKdKajI19RXcwkNNyfeb-GLs8Muxcdrf16o_qXONPRtk5iTw191YWPghvBwsgxOA63ep6jD6zAzxwdG6Lj5Y0kH7dswf6Ppn-c0uYUOapVCfEt1Sd9334Je8hkyxuE6T4PMXX-28lyEPuOP0TbHR43ZgAZtkD-2m18GHnoVw6ZfVUrXVT9RzlFVKgx7bM-v9CxuwietHUwotPBvWYh8ZpZOGgPtOwACLxgQEJXc0s2zljjgUNoULMiVVrDEra9gqZeWPX5v8fD1znzlA1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم ایران توسط رامین رضاییان در دقیقه 59
ایران 2 - گامبیا 1
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90423" target="_blank">📅 20:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90422">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7455525379.mp4?token=kquPwNNFGONdBcBgQPlsZt78rlmLlq05ShdKviPCmLRVH1emYePiVKQ4YRBkLQJi2XXxMxeJ6cQZwxPu0hRWkxfYF8OYw41zZSL5G85o5Iy7IlP6QHNvROF38IpHnqOfxnHe1YtNK301OIqJUc3prHL3UCXSKGDqLcZIwJeW0T088aYlTO_4WJ2wcMaV4T0d2ATHMlz_-o4Q-BTwC8dvdRIX2Eh56oQzeduShFOIgpTVO1DC9dhFB8Ty8ca9nYRzxxhiicTl9aRpl-KchoDRc8UX8aHphvBBS-Jqkd6GQtmbO_e1YQJZirxjifrbr2LzFZNLQgFMAkTHN8fsXlYZGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7455525379.mp4?token=kquPwNNFGONdBcBgQPlsZt78rlmLlq05ShdKviPCmLRVH1emYePiVKQ4YRBkLQJi2XXxMxeJ6cQZwxPu0hRWkxfYF8OYw41zZSL5G85o5Iy7IlP6QHNvROF38IpHnqOfxnHe1YtNK301OIqJUc3prHL3UCXSKGDqLcZIwJeW0T088aYlTO_4WJ2wcMaV4T0d2ATHMlz_-o4Q-BTwC8dvdRIX2Eh56oQzeduShFOIgpTVO1DC9dhFB8Ty8ca9nYRzxxhiicTl9aRpl-KchoDRc8UX8aHphvBBS-Jqkd6GQtmbO_e1YQJZirxjifrbr2LzFZNLQgFMAkTHN8fsXlYZGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول ایران توسط آریا یوسفی در دقیقه 47
ایران 1 - گامبیا 1
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90422" target="_blank">📅 20:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90421">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ روزنامه آبولا پرتغال مدعی شد که مذاکرات بارسلونا با برناردو سیلوا در مسیر بسیار خوبی قرار دارد و احتمالا بزودی منجر به عقد قراردادی دوساله خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90421" target="_blank">📅 19:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90420">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7061278c4.mp4?token=HipReiACZHoFVo75iOTuJurksAOhzg6ljE48ZDaoXOtr97iucCeR5i1fzNLU0NQMTCxWZ200kNgQSqk8z5xLaGNsJ_-Z9reklJBQnRHXa5e28b7WWTk1dz5CToB9Z7JbUZmSYt69imoK-k6JhYfe2crypDr7f-5pHihIhpNCe41Chj3X8P2MjgX_lVm-ZXTU4WvkLYqStRiMW8_ouZ7XimVxRY3F5cGQhv6imme-W4X38h54VUzesoTIo4xxUrfD93pxIlemwZT2TqmdrTeroNvwzr9z0r2eOEcDYvhLbpWaueW4JsniaPSoW6Afb4x4a0lLl_uwnhCT6SMOwvUxPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7061278c4.mp4?token=HipReiACZHoFVo75iOTuJurksAOhzg6ljE48ZDaoXOtr97iucCeR5i1fzNLU0NQMTCxWZ200kNgQSqk8z5xLaGNsJ_-Z9reklJBQnRHXa5e28b7WWTk1dz5CToB9Z7JbUZmSYt69imoK-k6JhYfe2crypDr7f-5pHihIhpNCe41Chj3X8P2MjgX_lVm-ZXTU4WvkLYqStRiMW8_ouZ7XimVxRY3F5cGQhv6imme-W4X38h54VUzesoTIo4xxUrfD93pxIlemwZT2TqmdrTeroNvwzr9z0r2eOEcDYvhLbpWaueW4JsniaPSoW6Afb4x4a0lLl_uwnhCT6SMOwvUxPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول تیم‌ فلک‌زده گامبیا به تیم فلک‌زده تر قلعه‌نویی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90420" target="_blank">📅 19:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90419">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISWeTIpSZH9vU-QuXKvB_SwtbE1TiDUCUbgrQOYFNtMOaWQwGddEmnnxQUDU3MBA_-WYLPHDXysg682_CmWeu2gfFrCUPKR0r0AAHcsbIS-4ahSXGNqRbxwpxeq0C4qgz24lYIbL_MLsQsx6eCezi-T2T6FJmpP5sr7tjAuwgOlUCMyXedEG64TaH-7rozEyzPdnwrEy6ZqwOt4NQ-nSW4Z2sBmCw8BZKmaP554fYoQWInzMu0GLYZCImPIEmnhaCMHB_0umw8TT0DOKBbgaxosTWRCUDKQPP3QBXzE15_K8JjfjiNAvsiFSnW52536V2OFnkFZ__viCDq44Sj_5tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانه جدید اتلتیکو:
برای این پیشنهاد مشکلی داشتیم، چون متوجه شدیم بلیت های کنسرت فردا تمام شده. پس پیشنهاد جدیدمان را با ۶ بلیت برای کنسرت یکشنبه بهبود بخشیدیم
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90419" target="_blank">📅 19:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90418">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⭕️
رایگان بدون واریز شرط های فوتبالی ببند از همون اول موجودی 500 هزارتومانه
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90418" target="_blank">📅 19:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90417">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoPTU0nditKWTVjm6FkiSnMuPBVV9CLxfGYWV0ouUzyxjWocOp4GnomHXz2xXqFroJqM1dEhxZ7LRYWLROKoBK52H3wyE1N98BlBHtCWIzARgG9H5sIgdP1SwnIlERICsuvFN0dSO0fQZN7wYikoWRy_gM6nW72zmw7sO1kxEfkh4uhXsH8Vvgv6-P68zhMtu7fU69kriBBoSBaUruOrCqY0WVnCOI5FRL0Uy8SEMGYfAMOhmTdA-klvHejV64zO5mjPFuyxbD0vWprqf6Au8wj__YfSQB3mSsXJ4mXNta-5cTxJnVUUaKVTSNUCGZUBSoePbG84Ly8Yfq22bO1lng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رایگان بدون واریز شرط های فوتبالی ببند از همون اول موجودی 500 هزارتومانه
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g8
📱
@winro_io</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90417" target="_blank">📅 19:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90416">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl_oljQWGX71WWhk_W2riclgEvakVJGcOZm082teTxPYnhNyeA19SZ124o34NhdUCj1bWqIDxmaC-epj0NJmfkrm3FeCk9igheeYZhOyptHGA7Ks9XLBMb7S_nYLWJX9OsN70v53k4TXcmnRia9yd_6ZBrY3ym99JtMZnU7Tb7do9eteOJyrAKMYjPalKu4z9eHDCDTrkRNVdSVntzfpfCMZzSDacIdJqmZYNt6xUvUevuOvO5Eu946ni3RSqO_YYqzncI-73ZRlkaBi22MdRdw2sKZlz-s6D0UDHYmwdewjRsmaJdWBqp1zVega8nMavMfz2F858znb-tDgJWSq2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‼️
حساب‌رسمی اتلتیکومادرید دست‌بردار بارسا نیست
😂
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/90416" target="_blank">📅 19:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90415">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tb_lVxWJl_o4JygknDnrVdD7w9LohIBpckXlrCyzKmEFdMFSeJTqbsspgytCpBK_ue7CflNTVAPprU1ut098qG22-Gczsj-NRNKE8Zich67VhhSDQryHVMzFgB1XZi6fMRasNxdcDpNdNrOiQO_L3DLsnOSk7-hNKLUIvoKGvYBjAgHI9j-Rw4asS4-WTGrC03nuJyzolnxcCiiYKipoaX_gtXVEpe89Pnqb3p8IsbwOFCTMgKXYPONcIJ31nOyyJFxOPZeLhNDhl_yEb0HH6X2ml_jlLe6xOthrtQVTF9NCmo99W819Nk-gX1w0BuoNkVYrK7fEi3wA2B1UqBfd9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه اتلتیکو دقایقی دیگر راجب آلوارز بیانه ای صادر میکند!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90415" target="_blank">📅 19:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90414">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krEkBobuxPipiwBmC7mcgPZNqyGNGeCdXv_To7Wub4KRToBoHCeWieA5fJNiXFXPWPkHJxMDzuiFZGtWJ6oipUhRsDXg3PBKJHt6BRPtJ92ksDdXkGsxi13MyEUu0oCvN0gn7TOTHjMyuFvosdNL0NqXcon92b69S_sAnaKeyx9_IX0XzdWLWgC7DRbps7aVRTVll2Hw1BkTeCMGGNoiKgkAPuf2LIqdGMoIvFdTb1g-HHcXpoN3iyyEy1QpwLxBq0vnpFa4HtjKopiNzEsO_2RubmGXbZQL49_zl0jxln4P3EYND5mpP2Df9FNKOTdXVv0dtYzJFNQIOs0QJ3CGQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه اتلتیکو دقایقی دیگر راجب آلوارز بیانه ای صادر میکند!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90414" target="_blank">📅 19:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90413">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🇺🇸
⭕️
⭕️
دونالد ترامپ اعلام کرد که محاصره دریایی ایران از این لحظه به پایان می‌رسد. همچنین اعلام کرد که تا ساعاتی دیگر تصمیم نهایی درباره ایران اتخاذ خواهد شد. به گفته رئیس جمهور ترامپ، مواد هسته‌ای ایران بزودی از مکان مورد نظر خارج یا نابود خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90413" target="_blank">📅 18:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90412">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ایجنت الهیار صیادمنش اعلام کرده در صورت تصمیم این بازیکن مبنی بر بازگشت به لیگ ایران، اولویت او بازی برای باشگاه استقلال خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90412" target="_blank">📅 17:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90411">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDsLOC0yhzu5vP25kCen9Ws75unOemLi3IaN6bzxilu1DQOf-cnDDBZtBxMRxdUYAI-glB9w02lVn-tDspq2YXOlNlyHOuUau67OdD7rzgL2tnnC21N6ol73TLLiJUc89XCMVEy2Fz6VTLwT9fmGXT4TwyhKMYzSqRZa3gWMxROxBXT9M3ejDTMi2c8c_aTMod1zr7_nRBD_mav_DNc28P5v8NgaML5WtdUF3Yt10C3IR6E-zVFPOYvydtxuJ3ZKOzHNSGUVhK4qqG2FcF4TQy524mhtLMOdzEvP5S_72b_E3-nQBG0Tsg27se7AUlPKw1Otbgh6OG4VCvpTNvh3Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت فینال لیگ‌قهرمانان اروپا نگاهی بر آقای‌گل‌های تاریخ ادوار این مسابقات
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90411" target="_blank">📅 17:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90410">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">Barko VPN_v2.2.apk</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90410" target="_blank">📅 17:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90409">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.2.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90409" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
بهترین فیلترشکن حال حاضر ایران
👉
💎
با همه نت ها پرسرعت کار میکنه بدون محدودیت
💎
👌
پیشنهاد ما دانلود این فیلترشکنه
🔧
لینک دانلود داخلی با نت ملی با سرعت بالا
👇
https://uploadb.com/plx39j7b72sy/Barko__v2.2.apk.html</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90409" target="_blank">📅 17:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90408">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97be903d17.mp4?token=JPetItp0ju0cCAm2YGQcdqDIZBeFAzxcqSeQWCv_EEWysKlDO_s4ckd44XE6ncZaFqVKVNcI9j6lvUlmgMEDtyHVWLyzsQw4oc2rB7aQQMFraZti63i5O9wfPmpMHNSTLddwmx_NtCtJ6STF6n-vZ2XVtWZnk0Xaa60TTsNIKbaxKiVaJ9uK24V9UIovn6qAEtabyBz3JkEjTT-xcSaXq-fU4psPOy0bgW0nJUBvQquf3RsFn6kX6kF0FmKFzSZe18zInNSwYgQpHnGTTISEidWHaYIt6RhPaevOO-kIxcjqzQHmMEcUK_1TuVKqdO0vSEKHdW2cqWkS2oQ-QFbmNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97be903d17.mp4?token=JPetItp0ju0cCAm2YGQcdqDIZBeFAzxcqSeQWCv_EEWysKlDO_s4ckd44XE6ncZaFqVKVNcI9j6lvUlmgMEDtyHVWLyzsQw4oc2rB7aQQMFraZti63i5O9wfPmpMHNSTLddwmx_NtCtJ6STF6n-vZ2XVtWZnk0Xaa60TTsNIKbaxKiVaJ9uK24V9UIovn6qAEtabyBz3JkEjTT-xcSaXq-fU4psPOy0bgW0nJUBvQquf3RsFn6kX6kF0FmKFzSZe18zInNSwYgQpHnGTTISEidWHaYIt6RhPaevOO-kIxcjqzQHmMEcUK_1TuVKqdO0vSEKHdW2cqWkS2oQ-QFbmNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💙
گل یاسر آسانی هافبک استقلال به الحسین نامزد بهترین گل مسابقات لیگ قهرمانان آسیا 2 شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90408" target="_blank">📅 16:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90407">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgM1e_A8qpw-kZYOJ68Qk7s0Zfkwi_8mVah51T9HxxZ0MNnobUdT_aO24_0lP691RWA1esPZ7rKCl3F8lRJaYG_jTdsNbTD2R2ii78_1FpAREROPb6ZhXn7tLCWa5iP4psYrL9WII58_04BM5cr4sAqZS-LKFqnattghyKUXJcdy7QV4QZl1N-oFoTW29VifXlzRA_4R5j3XiSN6VF48w5DsYzUuZtBwfTue-J5KycbkDsuCHEaYc7n8TxiOcKsOQ7QmxL5vLvms2Q4GPswclej6c_6q6NDKJ6N4eCUC0ZyFg6uZW-JsLT08dWWE0658LATtU0TFhMBs-9X5il6pkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|تریپیر مدافع فصل‌قبل تیم نیوکاسل با عقد قراردادی به ولورهمپتون پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90407" target="_blank">📅 16:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90406">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZ9vvmeIcOf1mD5N-tki_KtXfZSKaUZ4rkUwb-4TFhoZygjeB0EJmeGBZFnJCcFeVOIku0NNKF3dleIQzhNm7KdgaKpivYhB3hAo3JwAR7NmayJfR53Rnr4zrRbJa6Oupe87L_khpcV_ZbolUYBdwVXb359OqXzsjZ5O_s0hpEfP-2KQClDkC0M_ncVHo1fCw9QBeFKkH50eJFdkhL-oVy1jGzIeq6-uOKEnqyDEPYqyIejMUCM_ND6N72y5sluVpiMmjIZopz2cGzA0PgSwGyJ_gq6mTzJ5peD7FFlQcAmcirabvZs66jOMdv8i0uNvDjFaY6AvfrlWBhup6j3Hpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مثلث‌های هجومی آرژانتین در ۶ دوره اخیر جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90406" target="_blank">📅 16:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90405">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usmMtdsnhEA8K7dh29mDRywEUFTmaR8_uvWGSmbyXiL8Cx9-gcida-J-E8SPrRjdjrbMNtlZvcp7nWW8-j9voBFvHk8Jx2uVgfGgmYBenXk8Ye528K4IKGQGTHHd857ZOjYwZeDfZqoisOfFa6qbKJc8ood2gPMoMMXYrhvumQiyrzGhPefs8ag8zix86KclapSdZnNvfnm9M0xYoiwLFQK8mSiyhPlH4J3ZDucRlfdK6cigtbIbNWVmWYbdIFt0-Bv3h_B7ehl8nZ3NcXNfGyfuEgIyuCnjJ1S2UzBEUArzEmmIswdj9BcXBwABb1kUSvAYNIJVceITL5Wylh0pfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">↪️
🏀
سوفی رین، مدل OnlyFans، ادعا کرد که یک بازیکن بسکتبال NBA مبلغ هنگفتی را در ازای بکارت او پیشنهاد داده است.
🔍
اکنون کاربران در شبکه‌های اجتماعی تلاش می‌کنند هویت فردی که این پیشنهاد را داده پیدا کنند و تصاویر جنجالی این دختر به‌ سرعت در فضای مجازی در حال پخش شدن است.
1️⃣
داغ‌ترین عکس‌های سوفی رین در کانال ما!</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/Futball180TV/90405" target="_blank">📅 16:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90404">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfxgu2NIP9ytYfcFk1lkX-ZpL_o7amC6RHx6pJNNgfiN6Pi8JE_QwFSiYX9P51dxEzMKB0686oXF56uFN2inE9XHYo9r-VVqwre55YihE9QMsZzZ2KIB6OWFPgDnwo5iFQL3mSm3Vhkd_8SJvjG2RtO0Vwt-dOx4xAEX993GttEOJzCq3o5p5u80Ucsc8ezOn2lJcXuvkE24zjpXz4risk-nShI7krYxjqEjX8o4HBFAc2bqya6E4sjai2LARaKPdudV9VGND0j8k7gVYXix96xMQ9mR9jBn_nyVqe094Xfr93ogIBnJRr3SJ-EmhZEuNEoj7rTTBVKR33E4TajBfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شانس‌های اصلی کسب عنوان سوپر توپ‌طلا که قرار است در سال ۲۰۲۹ اهدا شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/Futball180TV/90404" target="_blank">📅 16:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90403">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da3204b2c2.mp4?token=KuY09Sq7D1fqcpK2EcDoF_pYhvZ0xVyf0TjYkwTEWCtNZHitKyG1FCRSv5V6YAb8g37r5PjDuSthf6TljSk7i_qgCk0JDwRSUu5yQgNRk_QmAhyLrVLPMGBDK5YskQwipMFp9-3FCj8k3QSnsi2T19k6nhHwJmSLai5_1gsZhXq0WDSfCeOjzBairrWZLea15tgt5leXhYsvLI2oWs-AZ4kRlYJoyn8KzhThIVzmR03x2oLuk-6I3rNu1tf8Ht9NLgn0p3TkTKfOvl_PPhNb3Er4ZBdafYVyJZT9CWUOOYo63tKVsTuJlZqIGeEnis_5ISeOSOeXOH-0_RksccR-YrLpXyqGpd4qkXwyvLCV7xdtgLZfYJZ-dsesy9Qm-jIru4mwSBncn70P-r2TjpqSuuOUIKUUXBfJZb9Yd2rk7izE6s_ke3Ru7o9gNCxaTH15-5Oy3q-5ZKNUzsa_Kj4VA6bJ5FjR_uC4ieeTWtUsydqgYvZMQlQJjQ3Xe1L_efcnNegdLOQp9l-aOrKl7Zk0FadSnD_iImc4ZkNEAXj0274f8fv9lykFFxgrdTNaoO6fpNu8s-cgnMudKwCzEMVUJ15xC_ZnqgdCrNakwhZzFbBcJpRCSsuIcI1uT5FphxDJ5Z13iVVV6vseHwaPbnjghW_7_s5A3BEhYviwPls3QuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da3204b2c2.mp4?token=KuY09Sq7D1fqcpK2EcDoF_pYhvZ0xVyf0TjYkwTEWCtNZHitKyG1FCRSv5V6YAb8g37r5PjDuSthf6TljSk7i_qgCk0JDwRSUu5yQgNRk_QmAhyLrVLPMGBDK5YskQwipMFp9-3FCj8k3QSnsi2T19k6nhHwJmSLai5_1gsZhXq0WDSfCeOjzBairrWZLea15tgt5leXhYsvLI2oWs-AZ4kRlYJoyn8KzhThIVzmR03x2oLuk-6I3rNu1tf8Ht9NLgn0p3TkTKfOvl_PPhNb3Er4ZBdafYVyJZT9CWUOOYo63tKVsTuJlZqIGeEnis_5ISeOSOeXOH-0_RksccR-YrLpXyqGpd4qkXwyvLCV7xdtgLZfYJZ-dsesy9Qm-jIru4mwSBncn70P-r2TjpqSuuOUIKUUXBfJZb9Yd2rk7izE6s_ke3Ru7o9gNCxaTH15-5Oy3q-5ZKNUzsa_Kj4VA6bJ5FjR_uC4ieeTWtUsydqgYvZMQlQJjQ3Xe1L_efcnNegdLOQp9l-aOrKl7Zk0FadSnD_iImc4ZkNEAXj0274f8fv9lykFFxgrdTNaoO6fpNu8s-cgnMudKwCzEMVUJ15xC_ZnqgdCrNakwhZzFbBcJpRCSsuIcI1uT5FphxDJ5Z13iVVV6vseHwaPbnjghW_7_s5A3BEhYviwPls3QuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
روایتی عجیب از کمپ تیم‌ملی ایران در مکزیک
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90403" target="_blank">📅 16:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90402">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAfNhvIz2uv3jNOvHyqBzPuSWU90rtJIYIjWTwMM8JLgM70P7qLBdwSOfBPsMvx0JrlaHd4uTL2nM05QJbpsJ8R75cqNgPfKVbRAc4-6JN8l68HexapRYdVOFLqEdZ4qku2qjYkTtsIVKLBAYPUkhHuOXeRSdKuI7iYLrqWFQmkDSW1v3-wyZ8fsWNi7Z7QaJ-vvUvlIfmNpEEMFBXSIVrexVClSOfVM_w2D6HErceJgxL-LCtNO32yAqfvCxxc7TMr2Se76t-YG3ldYacmWZWiqpQQepT_0FQpNYCV6HIRq3QTppNU66J6x_9hplxjsAS65sf1DyS_fCB5UifzGrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی با بیشترین پاس‌گل در قرن بیست‌ویک
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90402" target="_blank">📅 15:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90401">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb048df6e1.mp4?token=Gm_HKPNlbQ-kGGitWdsog8yN10XrXEFqyDQSqRmfGQx1cnVQIZKfCzB8nnQn5kbKdrFnOYv5ghAU_EEPEfsafM7w9kbXLDieMutw5GTv7qmNsDIZeMWcLsK8ARhQH9F0BNrty6pocSVGWMcJxDyrD6pEawlElzbUuBLK1HxeWvNQD0AaGe-fz2plj5ICKHM7t1SVDhFqzTkg6TxFko-etnozADFqoMi5tBdc17qNUc45NnFrbMAAWkCAV7EHb-5Y8st9y2qmdgKoDZDGDO3FbfL7ol5R7-7fM3pDVXTdXAEweCqZFSl5ZfV0THPDQ0j2-FQCwi7pTPcZYUkNZT0afA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb048df6e1.mp4?token=Gm_HKPNlbQ-kGGitWdsog8yN10XrXEFqyDQSqRmfGQx1cnVQIZKfCzB8nnQn5kbKdrFnOYv5ghAU_EEPEfsafM7w9kbXLDieMutw5GTv7qmNsDIZeMWcLsK8ARhQH9F0BNrty6pocSVGWMcJxDyrD6pEawlElzbUuBLK1HxeWvNQD0AaGe-fz2plj5ICKHM7t1SVDhFqzTkg6TxFko-etnozADFqoMi5tBdc17qNUc45NnFrbMAAWkCAV7EHb-5Y8st9y2qmdgKoDZDGDO3FbfL7ol5R7-7fM3pDVXTdXAEweCqZFSl5ZfV0THPDQ0j2-FQCwi7pTPcZYUkNZT0afA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت لاپورتا رئیس بارسا در ساعات اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90401" target="_blank">📅 15:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90400">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBbXqgwvtueeo3sCofWVfx0fMrg1YimEDr5_KveaOyzMgW5lBejRYanP0xq5nYeV1TGDiCGzY9wkdAxCA2Jyf648K5OgD5_hIO8qaKF8Rpc-NyQI4Q0I6mUdc6h8w9ELoJRkY817Pc04GPfAbLep7NV9Peo9kJW42MH1Bx4E84g3rP1MdHMCNrtFAjaMD171KyAlDbk6oH-RG2_I5AcB7OMbBAdt6N0ZS0HMu9IAW_rMPttl2-a70cURlOMAQof4o6wa9RS2RcUdfUsDqXnaE34oAiQbXrs776ghOC9wAs29mBovA99vweZ_uwwE2zrqaMOA215PQFPxDT6xRs7M2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
ترکیب احتمالی بارسلونا در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90400" target="_blank">📅 14:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90399">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d70d85d83.mp4?token=HuMmEq_98ZXoclSAkERc4xRyMTIIaz-kjdtwlPEwqqwfa-MGnFR7CMVqTmFC8Pugk7PT5dkFyRpHkBwTiqdWJTNDf1tJbYwgwy6Kvo066_hLfYW8_bpXj4s0UqY1jwEp4N_NRmiFjAjIl3TMewqIa0vguoehIFixItn-XOEeuAOLH7SG-Lso5bpuPVmiVxOimJc0-m95ZsFQlFrnwUfXrdIpa1MXplsG4PCT8hkDzKI0V-qLoXMxgGzvrIeLAUNkmi3dh3-TIkTpQUAPyUhtyR9DIht-iWoOdmTe3NGHQJiMakPlV_s8-Rvuu4giIqHUl3aC5IqfPI7WdHfJgyKQLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d70d85d83.mp4?token=HuMmEq_98ZXoclSAkERc4xRyMTIIaz-kjdtwlPEwqqwfa-MGnFR7CMVqTmFC8Pugk7PT5dkFyRpHkBwTiqdWJTNDf1tJbYwgwy6Kvo066_hLfYW8_bpXj4s0UqY1jwEp4N_NRmiFjAjIl3TMewqIa0vguoehIFixItn-XOEeuAOLH7SG-Lso5bpuPVmiVxOimJc0-m95ZsFQlFrnwUfXrdIpa1MXplsG4PCT8hkDzKI0V-qLoXMxgGzvrIeLAUNkmi3dh3-TIkTpQUAPyUhtyR9DIht-iWoOdmTe3NGHQJiMakPlV_s8-Rvuu4giIqHUl3aC5IqfPI7WdHfJgyKQLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
حضور کریس‌رونالدو با جت‌شخصی خودش در پرتغال برای حضور در تمرینات کشورش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90399" target="_blank">📅 14:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90398">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vC3OUFnDLLUviANm_ImLOsZ6wnRfyj4ylggtCklAZ8V1tv-NqagwY_pyWzJm7u9PjclA26ugxMBa5JTMgdx4TedBUHh4d4IDfyrhssI1MFUNLj9eAFDLGLSLk7rLqWiy7uKG8DCwwEeeBji6_GboLXOOewdPg8xPfSGugdwqah2aMhtfjcL3nWh5dh4ywMCooldB-TR1oPepXvKDIa5dCexsJTbEzzjyv51x3JfOeqoPSBxh-CtBMc4079zaqFd3IWKTg3A4yeXRil5oKXSgRm4jwczEdVUmO2nbsp7JyaqjSZtQwFLhxqod8mDK7781StRTFoSXcxsSLmrLxRcOPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ نیکولا شیرا خبرنگار مشهور ورزشی ایتالیا اعلام کرد که قرارداد احتمالی خولیان آلوارز با بارسلونا تا سال 2031 خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90398" target="_blank">📅 13:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90397">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcXQEHDx2ViB-uQF8SzSrMAfpgO1fh0wfx3WSssr5TcUzekpPF90X2xqS09z8o5ln8lT0xvpMLjMEMiHKzVQjibtEyLa8c4itejMQFCdueMx7A6sAyZStkFZjcBimcc38AP45cvaZm7dNkYOfzYBeCw9iRjCKzXysGj8szipfNvH4s2husx9iPm7mtYVzeYUnkhWu2w9hmX0IavDRB57z8Sz9DMEcf_qMvd0yhBcXVeD-LHAvtvFS4biJKGoF6CZwvHoUspjErx69hTbk5KGitPHrEcB66z5X0r13YMDKBajop50SahxqZbZrABsUiaM5GeeRbq2rtP9vaGHO8ewKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
به نقل از مارکا، ژوزه مورینیو اعلام کرده که با توجه به نقل‌وانتقالات پربار بارسلونا، رئال‌مادرید برای رقابت با تیم هانسی‌فلیک نیاز به جذب حداقل دو ستاره تراز اول جهانی دارد و برنده انتخابات رئال‌مادرید باید در این مسیر اقدامات لازم را انجام دهد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90397" target="_blank">📅 13:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90396">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🇪🇸
#فوری از رومانو: بارسلونا اولین پیشنهاد رسمی خود را به اتلتیکو مادرید برای خولیان آلوارز به ارزش 100 میلیون یورو ارسال کرد. بدون هیچ گونه افزونی و بازیکنی. اتلتیکو، از وضعیت 24 ساعت گذشته راضی نیست، اما خولیان درخواست جدایی داده است.
⚽️
Channel:
⚽️
…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90396" target="_blank">📅 13:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90395">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyuOnaDLAFvvUU-YrKXyLhS4ElmukDcBB4J3Rxi6Enceh99YMVpjhhdiU5z0H4ttYffIzfwqLd4MJ2ELXoR7WQmhHt-3UIdo6fqkpQ02vp_BblpVuX_OQ2XItUsAjS85x8s5UnuvpRe62DgtA14i06QJoSHYBo1UIFYzBXcMW8Fnq7MaDifDaeO7dQpG1V9d0_AsInOUuy342KEv1541UHmOiC6BYl0bILimHzJcq0-IEW9rKE1QqUl960Fo5DdGzvVUEhXzg56Sr-D-qeXP0ZySkrHg3bjznls-pnG5FrAu7ODuR20Py5URKQUtuB0bRSIPd6AKUNizu8JOTJ4OGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه‌استقلال با محمد خلیفه به توافق اولیه و شفاهی رسیده است اما این گلر جوان اعلام کرده که پس از جام‌جهانی و برحسب پیشنهادات دریافتی دیگر خود، تصمیم نهایی را خواهد گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90395" target="_blank">📅 13:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90394">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zp6cYFBJALxtipSx3K-8YEyDv6Ow-HQ9L-M4aLDuaELpsSwo6k8bI6ZPC1YTDs1xrtS1WnjX-zXYNEnmA06egGyUan3uUUUuV90AV9xJdO6QkJWXLmnPm0rdlJIv-RgqPiwOjWxifZXYX6rXLGgSg6uzJWiAV4pnp5i-4mbBxs_7i34xckflNsOK-ecNJ7gzffb9BJHmSPEjNsEHm_c23IklU9jZ7ATGDg6lf_TxSsILh1axHGXVxF7Cd12sklxQbEnE2xY3f4nrXtE5qKP0fnEO_3_eld0HPENocWpAu7Pdeqke-ceuT6lxBmvuWjrXmjhlP6aJ2zPXcN8HnEZflw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات
؛ متئو مورتو خبرنگار اسپانیایی مدعی شد که اتلتیکومادرید به جذب تیجانی ریندرز هافبک سیتیزن‌ها علاقه‌مند است و قصد دارد بزودی با ارائه پیشنهادی این بازیکن را جذب کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90394" target="_blank">📅 13:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90393">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3D2TDM6vryHk-B8a1sWoIKNDD_KOrWaXnTBRgWHHVK06TAroieSKZ2FaH3XdCgq09uwPLrCqdpf26Qm2d8x7Xsy18bpxtdrmak5pQRIbCA7aqLWuIR_ceiqlnXsM1hzqSMeJR_Ln9-Lb0qX1701rQqU3TA6nnS3CsPw_h-aPGewjAsbFJagF7UsWm-zi-JQX2YaYmhggSBx8Ik8L3MMpeiNskDMV_6iDnEhDRqA0sb26rFweljt_dzw3I42Wt5IQ0nlY3sMKyazQTmV6UApH5nFwtRFTFDPa-4AjxgagT6ouMKS8dE-kh9n7FRGvx6MnDWsABp5WMGV_lfYiUwCWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ روزنامه آبولا پرتغال مدعی شد که مذاکرات بارسلونا با برناردو سیلوا در مسیر بسیار خوبی قرار دارد و احتمالا بزودی منجر به عقد قراردادی دوساله خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90393" target="_blank">📅 13:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90392">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEEZxaO-VoP1rXJ2U625byYIyx2ERsxl6FEK_RJ9hnWXpOGCVNEohDtWpynbp_v88u5MXYnY2tiipu8W8eZYwlB-iLxX0pobqkbr0rO0m0NdMqB_0kyN3KdUeKIRibqiD_3Xg2oNiwV02QDuRtNGJ80du5QZgr7eRiMzU1-ipxv3-PY-4YMJp1iKR1XooTHp7h2jfHrtGYavTwparfVjOek-P3tqahdq9jHph-df2qUlf1jy6vPA3dSazBG7_g-RNg2kJGmP5NSUfvHuWN-oVOK-bc34EUvRQ50vV5iL5t7DyyKwqnQsZ8ObzLqxKvEkH2kqXIu7RinBzCOKJV5MKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🇪🇸
#فوری
از رومانو
: بارسلونا اولین پیشنهاد رسمی خود را به اتلتیکو مادرید برای خولیان آلوارز به ارزش 100 میلیون یورو ارسال کرد. بدون هیچ گونه افزونی و بازیکنی. اتلتیکو، از وضعیت 24 ساعت گذشته راضی نیست، اما خولیان درخواست جدایی داده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90392" target="_blank">📅 13:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90391">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lg-WUNJRh_hKeBNM78c3dp9AoQAg6E401lOl9r7FvoRox2Lp9La72LYkyrKImPV7dfwqaHrmhxf7SFoeMo83isoub-3wDW06QDRD94-ZTBqzy07WizZuOZFvK3CSW0Q8FiAy65hfpMJduwjXFrX9fBxvxJM5e-Q9umnv0oE1wsDLW4RJ0r9iLbiVTyT59qNXTJdvXjeSFncrXro1Z1zZkb9JYYC5O7jQxgFFt_PfFGZphCdSBueQzvGUlimP4k3Z_uA4Prk7n5uNWMzxsqEsAO50Ilrg_qnczyoDOWrmY72sPRZ7fXjF6j0QgX-9tkIUSGZOZX02MLH9RgU2mKufTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
عمق‌اسکواد ترکیب آرژانتین در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90391" target="_blank">📅 13:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90390">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766445bcae.mp4?token=YpB8fxlrRir7j_LRvIiUOMco25_v64xCs3_9sHQUk38ACi9WlpDirA36281lmH0BVNQsuGV4BqKk3qNHaCCsDVfYvgc8JgxxuIxoAQ4jul-qKw0g381s7M6iam0wp0gr-qxh-T1L2Zidh03pK4K3VJFA5whxrPRrP6grwJijoJdI_A8iOiWkBfLbjewHswuB-rWX4QF6xSnv5LtU_1mkHrOVeBFdLCtCm9KXmXHwUoGZY0-w0OARVN9IdhnWNBDrAI43ldlZxL64mF9EVBGjPfdwfbERzB3UUnRtgmYW6WKpQzPWZ8AvhYhX9A8DzVewf4LWovtuau2-EM8ods0t5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766445bcae.mp4?token=YpB8fxlrRir7j_LRvIiUOMco25_v64xCs3_9sHQUk38ACi9WlpDirA36281lmH0BVNQsuGV4BqKk3qNHaCCsDVfYvgc8JgxxuIxoAQ4jul-qKw0g381s7M6iam0wp0gr-qxh-T1L2Zidh03pK4K3VJFA5whxrPRrP6grwJijoJdI_A8iOiWkBfLbjewHswuB-rWX4QF6xSnv5LtU_1mkHrOVeBFdLCtCm9KXmXHwUoGZY0-w0OARVN9IdhnWNBDrAI43ldlZxL64mF9EVBGjPfdwfbERzB3UUnRtgmYW6WKpQzPWZ8AvhYhX9A8DzVewf4LWovtuau2-EM8ods0t5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هایجک گوردون توسط بارسلونا به روایت دیگر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90390" target="_blank">📅 12:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90389">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEeItu8uWZmeAyBGoNivUyebK4b1AZxCVujePv3a0yl5Ody-GEnvFwvxLob40GoKVXv6F1DUrUWkVTuXMlx4mtgP05356zktrFlwT7UG534bfvE7FsbkQIjpYjdfK_VcsCsQbWLbPiBGelOnoTFnQNcpIVONaP-ZEFRP0WjGwCe-5iGKJkgBEzgV5vqI2Z0RWMLZkj0BiiIUnboca3UReaBcOv7LwaNdteUdeVirsLWHRizbkIeE4YaCHIIsb_ozXrnGKFQd75UJHtiKfDo522R5k3r18nRJHpk0XOJ7yyALPqPghlAsv5Nj2jGgqDk52vw2E6a1Et5Yq0PbKknnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
؛ باشگاه بارسلونا پس از تکمیل قرارداد با آلوارز، بدنبال جذب یوشکو گواردیول ستاره خط دفاعی باشگاه منچسترسیتی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90389" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90388">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز به واریز
۵۰۰هزارتومان بهت میده
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90388" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90387">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0iAL8u9Z0tj2zpYmpSONqKHCgUGd0BoocHwiR9X0jWUU5V9T3kr5Eq8zZZO-Y01tbXqt74Z7xPrDPe9A-qHlnjgczOf4eFbUZFRvHan-_GzDwHVAjWE2iVeGir59wU0wRrZrNMv8yeIcR4h8Wg1fSxYwSmTovoxIrEbrqzNYAMKyirUGf4XsKm-ymFku4W2E6i5ij6UEPz3aEscK5jLA4h9YzqFDGBnb8PWAHlL7UmVImqHoXarHLXBl219RQJco44OJGAtHgjBROzQmWFw-kOdm5hQZYEDVbEEqd3ttSxKn6t9XIx4fy7tl_dBHnyWe11rj3TO5DrhTdHbFolYJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز به واریز
۵۰۰هزارتومان بهت میده
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r8
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90387" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90385">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-BPfg43c96Sp1mb2OdTX0AOeSd8w-B7Gq8hEPrdoTycfF2GHwdeRqwWOcXmWuCJF5830Aex-HCtwigj7ILTsMInjhjXtSMiJOZamrjDcnzxUnNl6RPLp5oVkfY_Yf8jan8VzwILgS8cl5NlDPJ8bvDC59c6zwucLUfbw3xlVFF4Bw3yhDVu5Q11LKqp6--vwIBP-_NKLlwspUhh_FdC5mnSg1XSCjRcrszI2d3D_EksXJ-Tcv2kSDTlqJbOX8lLNvq9NqXDKefzyByBpyYNU34c6lhQealbeNU2pxsjLHkaz-wBfjGzqubg4I95FlgPtBRrzJxVCOgPhF3ZwRaPGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
؛ رئال‌مادرید با ارائه پیشنهاد نجومی ۱۲۰ میلیون یورویی بدنبال جذب ژائو نوس از پاری‌سن‌ژرمن است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90385" target="_blank">📅 12:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90384">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqCNwoHU8rvENG9HebZOt_MvMYNTbh8-A4kgpPQYCbY2OKRjMBGnMxkidM1-A-D1ndINVSb72lzOiNa_m4TC00I3l9G0H2SrfsLYOgMg0IYRW6jnMv4C2T8fXVEfCglUd1cQnAZ96f-k6VZiMDNfKpNXVHu3_Xchqe4zaUdwwzr3seUtnkQ-rEx-zdhI3UXeQSv3y9pXsQpMNN4TKdHVTa7S73a1PUgANhLvu9m0OE_ksr_8hqXlxGwfYqcFfBY_bc1Jwf5ZjCq4SxrK7ygUHtdIuWZUS9KMc2GQ9wJR1mfgHMoQ6jICPROKhxNikqfuiZ4wUISIn5ZLvLWAjlKE0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
لیست پاری‌سن‌ژرمن برای فینال UCL
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90384" target="_blank">📅 12:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90383">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32bcc3a9e5.mp4?token=fU9DXDDk02hUkkQPcBjet6P3D9g4Z9GCz2cui8DoAvAvoupSD1ShGRDzKrZS6knKOguzDq7IRj9ec3U_nEG7x0yPGirgQjgK54cq70VGyXGnCFzIzLvGrs65aaauXM2S9W7FefpMEcei1H8VlQwuSf5LyEsObsxZuU9O-uZ0lZjDL7p0UMq78-ZE4XQB6aT5pD9qkoGKmHrIUMR6V4YVTp7iFDNLW8GUHgVHyS1wWr2b6qiQKqDH9WSabTj-lQS_28L3dIql_ONVUaKhHfzEFBI1AvbA8KfXfu2pUwM7SC68CFOXXfyiNXgCr1dw2b4pZC1K_l_BYEd1G76u0hiVZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32bcc3a9e5.mp4?token=fU9DXDDk02hUkkQPcBjet6P3D9g4Z9GCz2cui8DoAvAvoupSD1ShGRDzKrZS6knKOguzDq7IRj9ec3U_nEG7x0yPGirgQjgK54cq70VGyXGnCFzIzLvGrs65aaauXM2S9W7FefpMEcei1H8VlQwuSf5LyEsObsxZuU9O-uZ0lZjDL7p0UMq78-ZE4XQB6aT5pD9qkoGKmHrIUMR6V4YVTp7iFDNLW8GUHgVHyS1wWr2b6qiQKqDH9WSabTj-lQS_28L3dIql_ONVUaKhHfzEFBI1AvbA8KfXfu2pUwM7SC68CFOXXfyiNXgCr1dw2b4pZC1K_l_BYEd1G76u0hiVZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره مشترک رهبری‌فرد و شاهرودی برای رفتن به کنسرت ابی: پرده‌ها را گره زدیم و از پنجره...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90383" target="_blank">📅 11:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90382">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M97mePnUH0hpfaIc7MvDXhtPiWdZ6Wry1BEW5PCA41H3uuFE9_0SObY13UrhRlMtHyx7Eiu95gG0hZRRbxMA_JlvQEGkUZdSjnaWx4oYeAqry1vlzpZNtBnxipY8ldktu8zf332sdWEjdcY2_KLcjr7_lqYfPKN7I3vs32eGeVf5f8LhpvcSDiKCKchy8cZMfRb6yjHr5DmBTQLx-y3WHIm2LRtKiEuBykk49llFQqDZKEGUWyTkTyTvBTSNCBcSyR_0NvZocNRtcpfIOK_jwSnJ9NhPXS1bdr4GOwNbZ6J0qyi2AekVK5LO6mKZXZ-dVjY_6MxXToEz2-k7r7YaOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری
؛ اسکای‌اسپورت در خبری اعلام کرد که ابراهیم‌کوناته ستاره فرانسوی لیورپول در آستانه خروج از این باشگاه قرار گرفته است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90382" target="_blank">📅 11:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90381">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JKApjsEHnSMv6NxpEYbdyIpr2ktSvX0VQ9bCpVTzBAClvpWCpTY5PXyQ7I0qd6SfUsbCUyTQ6TLoMFUF5dObLJwFIEoeyVd9q2t2HHEAIFxd1jV7m4-JzdFfzIN37IHmoKQHWTdyNCsTZYc0GHSfpXwXk_zhLYtddXhJdz6dFTarMdA0kOyAmCiKLlDPhbrJ9ogAIAwO4dYUuvE1t8vhle1wiN7RX5ct0vw8jXjSwnUGyEzgPl_suXI2gBAW_9XKxU0Kx4JNcnRgzWDxSKrJKnk7Mk3MVXmYQeGKkI0quecNbb9vhlBX_hbEgaqnZGMxpv7vqr5TPIroBcteZPoKSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#فوری
؛ باشگاه الاتحاد عربستان درحال مذاکرات فشرده با یورگن‌کلوپ است. این سرمربی اعلام کرده که در ۶ بازی اول فصل جدید، دستیارانش هدایت تیم را برعهده خواهند داشت و سپس وی به نیمکت اضافه خواهد شد. درحال‌حاضر منابع عربستانی از بررسی درخواست کلوپ توسط مدیریت الاتحاد خبر می‌دهند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90381" target="_blank">📅 11:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90380">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbjiiV4jWkVlKyd8xJPz1BUdDq9Pvz18xRuDJJwWxceDyLBUSxyBbyoJ8gZaINZgxhBdiglOBH-qz_wGY8hEco1LoMq84eeqopGAxl3WQuDwdWpqBMRqoWD9Bwq9jcaQnviSn7eLxmd7BtkuRBfBup8_WTee0oJ6eLqQ1uaE099_6Bm01X4uDHhC5n_TurlC7KupeLUtk1GBYSZ-Z7yTXMdSXYe8PLXuwOXcU2_48yCYGqwtdMU2FGnx3TIbaP0ZUBgMqm9EyrsbC1ApEqsetC02CYWEDUCd5jNqaauOBJnkOOsZitiNtqBiGotZnhKAqllUNmZVEcd7FZqB15vAWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
استوری ژائو پدرو ستاره برزیلی چلسی؛ شایعاتی پیرامون خط خوردن نیمار از فهرست این کشور و حضور این بازیکن در جام‌جهانی در ساعات اخیر منتشر شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90380" target="_blank">📅 11:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90379">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eq_uU8eiWwl3O7c2FaBsTLIPRM5c_4Oxrcx2i2R1d02LRUgw4Og8_iuOOkuG0buY-B-ZjMLG8CPMrtMwygz9mc5sIqip9U-8muskkuJfOO6byGJbKcVXEexxY24djaV_x6V_pow8apn1QuEessPX_OnRblzXFJGAoVILDPSSUrSknGLO7MpdR7Eh_AqF0-SVaFiZ061WpteAKcioFJzwYWJuD1nISo5jm5Ccn5BX41f3SpgC9bi9yNB4tyOS7y2Qjq-3LdqjrNm9O4lebNvcnam-2nWP1ijNTS-Z_yr8RqkR9Ma1yHcLVPZbuQ-RDexDsltY12eu504HNfF3otEkPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🏆
ترکیب احتمالی پرتغال در جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90379" target="_blank">📅 11:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90378">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20638b4d5d.mp4?token=DmqDfDS79qaonHi6pMbfmzYWl9361xcodlE6QoyAffmdw-huQMmU21gqnlBF2MBia6qVc3IwgzXUB-fQQVg_nKdG_kOo9Z2pS4fSu9AEmHKXpfyoe_YT7fotFKca0pByMqYj6DTroiTtBc3aHPnPRPG0nX-fBiHI7le7jwmq5nBgzHBTeLYONfBEm4nABTYKJxtIdDKXkcSZeCO_0DkuvB5vJAVF5CoN85iXHHdQp2sc6a9vU5HEJDQPjVZ12xgh26tEO433y8Xj23yZ1Luo6fI0-9eNWjb7NKMmKa4UkPeLA5Z653jbFh7KnNXPNbIBBVvhkLjYsstTq6mG6LoMEiiyqbpAPVq1jQC67NTXObvfGa5pDFbJW8FOxxEIbeIoiosf2zf8Yi3zk7Ty1f6At_l_mTeIa8EP7j6SRl6jE7St0XZvc6ogjG50NNx0nJ0D2ozlx_ggo8DmZ8QQ94F4riekaQMaAVuF-P7TaJ5OFqhrs7Gx7Ab5XggbMOxk2Wl_XmEVJ5HzKyShau72J2OrrSYnblhEq2QGSy4-qaDlRpRSjSD5l1RckOnJidLXukj7naRCshLAZ7xv4-mDI2QwkKyiM1nBUTbEw60CrbEGcTELsvEdVHBdJYmepq_FVta1n8DebSzWHlTUfezOhF2sQpJM9PIiDpB9iCxLAH2Gr4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20638b4d5d.mp4?token=DmqDfDS79qaonHi6pMbfmzYWl9361xcodlE6QoyAffmdw-huQMmU21gqnlBF2MBia6qVc3IwgzXUB-fQQVg_nKdG_kOo9Z2pS4fSu9AEmHKXpfyoe_YT7fotFKca0pByMqYj6DTroiTtBc3aHPnPRPG0nX-fBiHI7le7jwmq5nBgzHBTeLYONfBEm4nABTYKJxtIdDKXkcSZeCO_0DkuvB5vJAVF5CoN85iXHHdQp2sc6a9vU5HEJDQPjVZ12xgh26tEO433y8Xj23yZ1Luo6fI0-9eNWjb7NKMmKa4UkPeLA5Z653jbFh7KnNXPNbIBBVvhkLjYsstTq6mG6LoMEiiyqbpAPVq1jQC67NTXObvfGa5pDFbJW8FOxxEIbeIoiosf2zf8Yi3zk7Ty1f6At_l_mTeIa8EP7j6SRl6jE7St0XZvc6ogjG50NNx0nJ0D2ozlx_ggo8DmZ8QQ94F4riekaQMaAVuF-P7TaJ5OFqhrs7Gx7Ab5XggbMOxk2Wl_XmEVJ5HzKyShau72J2OrrSYnblhEq2QGSy4-qaDlRpRSjSD5l1RckOnJidLXukj7naRCshLAZ7xv4-mDI2QwkKyiM1nBUTbEw60CrbEGcTELsvEdVHBdJYmepq_FVta1n8DebSzWHlTUfezOhF2sQpJM9PIiDpB9iCxLAH2Gr4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🏆
هواداران پرتغال در انتظار جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90378" target="_blank">📅 10:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90377">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5359012d10.mp4?token=vXohF7YSpQSRW0qJS4p2CLnChdRdodcj_qqp_DVpQbmdckl_8hnDbg03frCMYjkOS0WhnuftfBWD0U22pPp0kkKrrT0yGwDSWMUj6e8PJv2rvNnjjc_PwNv-82Db_Ghsm0Gk7AfxdaiQl8Krzi_8PZeCI5PaxXqBAln3IKhur-ywgZinUrDNbDoaZcrD8OR_Bswb4TF79JIBZ7uyM-cGzUEKokYo6t6VggAWt6ANRUTTc0Q1QXBoXfvsDy88JCJbvHu2ieFDBSY7J8frPyJ4bdQ0J8i6Hi6TYTs5RzPCLOtn_8A1P03Jtftcz69h4UvFkCKr1GK4UBLyYuU4kvxQLbmcrbGlHViF3mqQ8MZ7y2WazygW0HDk8_KVB7IWb2pzf0N6kLc9Mr5uHfIZvXwejGnsI1MW1fPvsQ8B8T65PwrfKmK3Wn3B9xUQaSMIdFHK7hc6qtby-0DSPlHpRmgEm5WUINeosgfX8vZqFO7Z6ePJeuluxubzBVYtk4e7jqw9Bl8dg7uqUrPtc2gBEnIBIcqXW5EYNJEEi0EV7Z16jjjaYkeK66pRIAh8Tq_o_IdKgcGp3e4VsedsWNJGyZ0ZCyZBKFiUBvirq2XmS78edTWRzbA1rVXgXEdkHEN5l7Kidpg94zG295pcxc88qFk16NPw59cbUz85NYLYrN41yeY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5359012d10.mp4?token=vXohF7YSpQSRW0qJS4p2CLnChdRdodcj_qqp_DVpQbmdckl_8hnDbg03frCMYjkOS0WhnuftfBWD0U22pPp0kkKrrT0yGwDSWMUj6e8PJv2rvNnjjc_PwNv-82Db_Ghsm0Gk7AfxdaiQl8Krzi_8PZeCI5PaxXqBAln3IKhur-ywgZinUrDNbDoaZcrD8OR_Bswb4TF79JIBZ7uyM-cGzUEKokYo6t6VggAWt6ANRUTTc0Q1QXBoXfvsDy88JCJbvHu2ieFDBSY7J8frPyJ4bdQ0J8i6Hi6TYTs5RzPCLOtn_8A1P03Jtftcz69h4UvFkCKr1GK4UBLyYuU4kvxQLbmcrbGlHViF3mqQ8MZ7y2WazygW0HDk8_KVB7IWb2pzf0N6kLc9Mr5uHfIZvXwejGnsI1MW1fPvsQ8B8T65PwrfKmK3Wn3B9xUQaSMIdFHK7hc6qtby-0DSPlHpRmgEm5WUINeosgfX8vZqFO7Z6ePJeuluxubzBVYtk4e7jqw9Bl8dg7uqUrPtc2gBEnIBIcqXW5EYNJEEi0EV7Z16jjjaYkeK66pRIAh8Tq_o_IdKgcGp3e4VsedsWNJGyZ0ZCyZBKFiUBvirq2XmS78edTWRzbA1rVXgXEdkHEN5l7Kidpg94zG295pcxc88qFk16NPw59cbUz85NYLYrN41yeY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پنج‌موزیک رسمی جام‌جهانی دوره‌‌های اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90377" target="_blank">📅 10:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90376">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCDfx7Mnx_LPTybc7JuQkT0WN9410RAdBWAf2Nd_1QeZRVUk7wTSNY1H_Ow78PQSuf_4yg538wvMsn5ABlzJ2C8ARy0IcaJG4E7vNMvXgCO79i5aF_zEjTln5mTJpK-6xOkTfS82gacHdjpknEw946y7CjMJJEgTLfpIyWRc_Lf-ZPLC9GYoxty_e3WGXwVBt-zxIQIjXmqh-qS4mI10MhPDDgn-cVmOtUNpVp33QFD8Txl_9TzJuWXxNtOYzTmC276DC2pBdNldbNZorf6W2cCGxw6u4pYPHwVjKc02wxNCsdICTOPS6vVmNenOWS5WPMjtoNZUF1-ALTB3yKsARg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
تصویر جدید یوفا از جانمایی ۴۳ دوربین پوشش دهنده فینال لیگ‌قهرمانان اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90376" target="_blank">📅 10:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90375">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RF8gH-O0jELj5lhtPRg_7Xy21umwevve0oj_3TLTW7MLSxNOvCg4s8I1GeXw3E8a_Wz2kJqfPx4G0BRlDErziJro31K-xdSSNOzFfDJUsY3v-GQwkLahjFMZfRqpGfeXcgAqCAVCNJt8YEhVA9r1OJKPTyCpg6rMZVUC3xQZOcJiQMZj6r2Mz-3QZj5SStE-JJGCDxn1ZpTRUfT8Q2w4L_2go7dKsQp8ghreMPsx_HE4I2caezXraJ0x-F1UoaSGPk13dcE9EZ1JX5kiVsmBAbTGnCpwalPK75cCmL8Oyo0L1BgAA17EjJoOR7dOXquNI_xDizxLyoHodsqfzgTZzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
ترکیب رویایی رئال‌مادرید که البته بیش از حد رویایی هست و احتمالا محقق نمیشه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90375" target="_blank">📅 09:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90374">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🏆
کار گرافیکی فوق‌العاده زیبا از قهرمانان جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90374" target="_blank">📅 09:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90373">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac09312735.mp4?token=pdBDxUm3C-RYwCBjNbpK7OsJJce8UeZWUmcI8z52WmrSTBlc5W_J0DZwpa22zj7KiOMoYqnLLzcD245dvsQkRrzh6QjRB2VMevFBCY3IjFJ2KdkD45VOfmfH7ZT6ibz02abiKS_7c4Jb4mcw6ioXtlH9_pjgWUSKQT6QCKr-TGVyzgHXbufcmPiNczrgp1uvweUjcd8iSLUjzTXXyM1fvyyTGHNVLGvAKjOtHCMOop4CRG1aguIEAZMLFgicaeFs9xKWEtSHWasRJa7iFFcKcbLgnGTpWyjh27FuEW-OLdAi1GPTWhxc0MF5___xzCgIEGdGHYcEhEmra7AcsnQ4JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac09312735.mp4?token=pdBDxUm3C-RYwCBjNbpK7OsJJce8UeZWUmcI8z52WmrSTBlc5W_J0DZwpa22zj7KiOMoYqnLLzcD245dvsQkRrzh6QjRB2VMevFBCY3IjFJ2KdkD45VOfmfH7ZT6ibz02abiKS_7c4Jb4mcw6ioXtlH9_pjgWUSKQT6QCKr-TGVyzgHXbufcmPiNczrgp1uvweUjcd8iSLUjzTXXyM1fvyyTGHNVLGvAKjOtHCMOop4CRG1aguIEAZMLFgicaeFs9xKWEtSHWasRJa7iFFcKcbLgnGTpWyjh27FuEW-OLdAi1GPTWhxc0MF5___xzCgIEGdGHYcEhEmra7AcsnQ4JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سانسور نام علی دایی در سریال صداوسیما
صدا می‌گوید «مهدی طارمی» لب‌خوانی می‌گوید: «علی‌ دایی»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90373" target="_blank">📅 08:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90372">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjX16MqAfhdFJkrVWQSlCYReecUdcaeI65mbUHy21k4EofPufI0-4HFqSKVX5ZZzuBfEFKhGF_vQGVO6vm0Dskl-7Uy-5dPem4tXIcPXJ9LfNtSnZK4A2wbOS791DDPmfPGfgbK6u4Ttyv3mjCs3kTLDM4XJyFMz4KHxcGjgKkV7XIqWAcrldXzXIlXG1KrsedWE1g8zrtadXgzz2UrMsKmUJB2mxL5Vjcdw1hyCnS1FzMyRx3R8Iqep7eNtDmQdENqi6EKDusB1mFmexBa8KDpjXacgKWHsPM2tGtm9vTTC2eXmqngfONd3OdCDLmrubXAwSbsjFVatibEpK2lG1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
لیست آرژانتین برای جام جهانی.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90372" target="_blank">📅 08:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90371">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
اگر همین الان توی سایت #وینرو عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر،…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90371" target="_blank">📅 00:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90370">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rS7lrn_YUEoSPj4zt6nfFKceWTtW4BRl7FFqSRcbLqzCEhxTJwR2MjARJxWulHJbL-CK31C2yIAPlkhpAd39i1XCcuGGyT_J3PauAW_nkknedK-4f8IjuceBarl-KlxCK-Moqp8CCTB8lY_4TfIezmwUZkf3cwBEjWahFghDKZcxFJPzlAZjz7X76e2fE5mI4NbvyG9BdbXtLLBaTArptK-q0sfijwm0CzyfULG_R_z1zl74epRrIcopLITKmvuFmNvxk0DPloYTAU9tUE_52E1LQpKeFVubHJLVl7b-ESZ-ax-gPKZfHnyce6N2cympyCfhoqxvH9RrowffjrFRow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگر همین الان توی سایت
#وینرو
عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
🔴
این فرصت محدود رو از دست ندید:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a7
📱
@winro_io</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90370" target="_blank">📅 00:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90369">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eThbwmvEyDPvPDAjhmGMrxx_0OLxPt1vkWHV4_I3quVQLV7ZiKS2XM-K01Z12nsuq6trBgitr3P01FN6MUFPmPFilQnylm2isUm7PO1IkgI9A7smDlO4kkmGUamEGZM4j0TRCV67fRnc405-wqTIb3xVpZsh9gwq7UYFHkXb_p8MVNRATSP-Y1glosJT4js9QkZlUH4hI5aR1hR861LczhUHrfTMFzGxCwRAqPvobZeHsG05dxUE-iBT2LFz-fr8dOrqT_gHwqoD843rkMqscXLCyF7c4jcPhExRbBRm1Qnp385tGYHCZIgIdGOmIoDZl-u2IQfqECBDHUMwEHp-pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل بعد بارسا:
😳
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90369" target="_blank">📅 00:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90368">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f5c4c6ab5.mp4?token=cjknst62RAp4hBWUlrJOthVmV-oz7m4Kux2Y1yq_CTkWYfGfFBLzDthnfkvs0b5vHjOEdG00_kfvsB8qBRxmeFvOLimRBddBBCpPwcw2BRDvsfHxht2mXfx2pGU8CMb7Qh8apgJlL5cIOCLtGnLI6iNS77Q6LiKMB3-_xC6QX4PhoDQRY8hhiieGjx_Mkw042gtuEFr4CEzMSMtQL3XLgafa48dFaPEatFqopN85Kn-RjEzS-fJhr-7t6GBWRnOohykcxXBbQtECr7FKuziQS7bW7DuZIAY26k_Pd7YEIwfINCe85Kyx-j7qaRWWvySWzD3KmvKUUxDm3xledQts4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f5c4c6ab5.mp4?token=cjknst62RAp4hBWUlrJOthVmV-oz7m4Kux2Y1yq_CTkWYfGfFBLzDthnfkvs0b5vHjOEdG00_kfvsB8qBRxmeFvOLimRBddBBCpPwcw2BRDvsfHxht2mXfx2pGU8CMb7Qh8apgJlL5cIOCLtGnLI6iNS77Q6LiKMB3-_xC6QX4PhoDQRY8hhiieGjx_Mkw042gtuEFr4CEzMSMtQL3XLgafa48dFaPEatFqopN85Kn-RjEzS-fJhr-7t6GBWRnOohykcxXBbQtECr7FKuziQS7bW7DuZIAY26k_Pd7YEIwfINCe85Kyx-j7qaRWWvySWzD3KmvKUUxDm3xledQts4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙️
سفیر فرانسه در ایران:
علاقه‌مند هستم همکاری‌ها و تعاملات ورزشی گسترده‌ای با باشگاه استقلال شکل بگیرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/90368" target="_blank">📅 23:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90367">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ff0dd9d2.mp4?token=DXfIfvq_FfSVI2NHKV7XUqN_wmw8rytFOe-fnMyLx5V27On39nU_nNug-9qaWqgasazIgnYHls4sXg-an5KxRZhYA55tKYIb3AgfdScLmmsoP54Ddq7YIaBLqojbUBG1ofOjYXRGDdQhUXGKHwVrU0lseohenGT-_f0kSHwNVkCkyBF0rooTJQdhYaxKrEZhHGdcj7tGMQv9XDZs2fzG6Z_yrypnJgfqh5X-CONE5fmd0EnDWNttpPoAlVAwkvNSh1ZzQjF_hV2rW1-9C6IcFsTjcXZNx9di0nVcRGXbRn2Z1PN4FakvvGSPs8mc4YTyV7l0CkIav8RT6s2F37dxjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ff0dd9d2.mp4?token=DXfIfvq_FfSVI2NHKV7XUqN_wmw8rytFOe-fnMyLx5V27On39nU_nNug-9qaWqgasazIgnYHls4sXg-an5KxRZhYA55tKYIb3AgfdScLmmsoP54Ddq7YIaBLqojbUBG1ofOjYXRGDdQhUXGKHwVrU0lseohenGT-_f0kSHwNVkCkyBF0rooTJQdhYaxKrEZhHGdcj7tGMQv9XDZs2fzG6Z_yrypnJgfqh5X-CONE5fmd0EnDWNttpPoAlVAwkvNSh1ZzQjF_hV2rW1-9C6IcFsTjcXZNx9di0nVcRGXbRn2Z1PN4FakvvGSPs8mc4YTyV7l0CkIav8RT6s2F37dxjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
رسمی؛ با اعلام باشگاه النصر ژرژ ژسوس از این تیم جدا شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/90367" target="_blank">📅 23:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90366">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پاسخ اتلتیکو مادرید به بارسلونا در مورد جولیان آلوارز:
خولیان آلوارز فروشی نیست و باشگاه هیچ پیشنهادی برای این بازیکن دریافت نکرد و جلسه ای برگزار نشد و از ماه های طولانی دروغ، نیمه حقیقت و داستان های ساختگی مانند خرید خانه ادعایی در بارسلونا خسته شده ایم. این رفتار یک تیم کوچک است!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90366" target="_blank">📅 22:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90365">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxy_IxcGN4zDjZswWwu1xiUYDy-j4CCOtbCNV5JtqPLWG6JBBgUWhLutcRZbBsx-D8mnNiKP1OtEcdS-4IL9ncmv2YDj02lExJ1CNg-u0euVxs8W0nbEST86ykFKnknhNtwqWGJzxjYSvIp7AlJtIU9l7P8qYp7OVMa5w1aiFaK37m9upTvX_nEV5hNKib_q8ug8QyC3_Iyn3PArgMrVT95MgUNThtB4evYMgissqbCeIFK6RsU_T5kzo2AWQz0_dRjkCIEYCpzqF_DRzihb61TMLTK4-FOnaWz5AzgkT4lf-HYusvgVwvq_9nKLEIO1_2h6zUbkrkbdpd5Ay1qa_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوورییی از سیمون جونز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
:
•
💬
بارسلونا در حال بررسی احتمال به خدمت گرفتن پیرو هینکاپیه مدافع آرسنال است!!
•
💬
اما روند کار دشواری است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/90365" target="_blank">📅 21:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90364">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqF0wcV1L-n8MbF20slXpoWiECo1PbBXsA3EnN74zKF5tRBrvlIh2YOLXdE3r78UCnkU6Vy_q77Pfsf6Nl4xicu485NHhaC_uqdE2GJ-o9eZrVRhWvRi1sHdLc-tS_Oxph6RkO7kjhKYeisiJAm9m9R90ti4wMDddI_eoA-QCqkEH2JU5c84oD37Z37Wxk882AdtqS0O5c5SvK7CY2dDplVBD378MOx_ztjuQoEGvRl8qa8bTl02ZFMnRWAeRzcVG5F_hno2Z-C8oUUv-Qib4RBV-bSnq8EaiMCDTjLDjFgvWO9ThtUu-T1CLPLRq_D_KCjoh8qXduUvfiveTYedQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
گردونه شگفت‌انگیز جام جهانی
🏆
⏩
با پیش‌بینی رقابت‌های ورزشی و بازی‌های کازینویی، مراحل هفتگی «گردونه شگفت‌انگیز» ویژه جام جهانی را تکمیل کرده و هر هفته تا دو چرخش دریافت کنید.
اطلاعات بیش‌تر و قوانین:
🔗
bfrd.link/WCW
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90364" target="_blank">📅 21:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90363">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OK0hSmzRHAVu-MSvPwetAvznmiwH2w7QTOhyzH__HXZjC2c5xzNXb29_LS5ymR8P6RQxg7OpT4DBvq0xpr5IzOQ0UAAhQkt8yQ1bLbAM-aMj-xxGSqFlq7_8ebBzWhRQ3SzeMDw7Qd-T0qc9JMfPMK9XMOVEfQKjzbFM_pYnFdOowjjqNti5DdoFWRIeTAnhm2VypgK0-h1nYP3SIsbm7xD5UDPhkoe_AtQWlfE4hksTA_7BF8Y8uu-YHahOEUAlPIEmu19VZ2xlNp4iZXTrjNvWKcak4Wz3x0bT0TQdhxMDYTHPGXuxmwyo9zZfki3bQLkAql6yNOaVD4VaQ1cM1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیکولو شیرا :
قرارداد برناردو سیلوا با بارسلونا تا سال ۲۰۲۸ خواهد بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90363" target="_blank">📅 21:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90362">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozp_8iYtohvno6Ctk0u8CLaG2gQFGcvYrYOxcmMJdtn9QMtyUkdTi9Y8xud7kKphBml41voKkSDw6J81qENJ9ueR0gnWZkEfKvk4UNdRhjRolEU4v47znvg0pBAtKGfuOhS-g3ISt1TY0pXKZeNM-46pMiHafoi-PoyddyB97glI_QdWjH05k6snGAAODEVofN3b8tM4jpS_a-B_grhPcPkcO3CfDUnjvNYNB1GRJcGombw9Mx5wWrvYsrNVFKMsyfSpWpHzFOUPnBSIQrQ3DkKxS9JGlnqmjwJ-MoPH23c12iQA_ACgHU-AQMkbCXF1NAFGbTLSItxlbW34c-Au5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم بسکتبال استقلال در بازی برگشت فینال انتخابی آسیا موفق شد در یک بازی جذاب پالایش نفت رو شکست بده و به عنوان تیم اول این تورنمنت شناخته و راهی آسیا شود.
استقلال 93-78 پالایش نفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90362" target="_blank">📅 20:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90361">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl-kpgBBk-JHCw0Wr7l8R5DXMoTl8tFSbDjuD-aVdiPbruoDd4NOTi7PHy6etTzSGvBkeRsiQJ2AAV_8go1-BHkk63MZ_md8qSkDrtD0SecYy6EgUBSXdH8J-8dZc7uuYrF_nbit5S4pAQyTqR1mTv-lgaCM7Ffm8GlLpAXsQEOfcg93_6MxSET--ed1ve4Ak0yST1wC4CNwuzzmc7vircQiScytvALn1tCsOTtDQrILzggI5V4-vZBZ9Fo_76gWDrfXvyIxlUYATV6bNRyha7t6QAtumy_fHAzM5PtjJr9_SgjJrGKfOmWc09FCwkRV3Nikl6Fq4896l9pjvYCNCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو : آلگری به ناپولی
HERE WE GO
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90361" target="_blank">📅 20:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90360">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">معاون وزیر ارتباطات و مدیرعامل شرکت ارتباطات زیرساخت:
بهبود کیفیت سرویس‌ها و بازگشت ترافیک بین‌الملل به دلیل طولانی شدن قطعی‌ها چند روزی زمان‌ می برد، در شکل روند افزایشی ترافیک بین‌الملل قابل مشاهده است، کمی صبور باشید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90360" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90359">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qciZb21VeJ9LitxMqweINlQ71LH8fDri5KJlR2-0NGxPOAYYcJ3W-mauE1zvABvxFz0E5MecHM4-0srCkWIgk7T8W3v3Fk8B7n0zhtFMLnpkKBT4IUJJ1aV6WyYRJlrKQIqPk1nMvavuMIB-0UTNp0gXprdzkYPw2NGFscl9AhZeBr5vKC3xC3MYuhAID8ug9ePBMCHprc2CVP7Xod3t49j8kpn_vzfyFArFJTjE7-vJO-FaSMTHXHC_N2syUQIHiYhfJj_b9btO8LpZiTPimQP3FzTvCW-N9je2a1uJIC0DtbXmulnFPm__aqAYqyjeNzwC9f0p8mwgZjhXT8atCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فابریتزیو رومانو:
تا این لحظه وضعیت مارکوس رشفورد هنوز مشخص نیست؛ خودش هم دقیق نمی‌دونه تکلیفش چیه و منتظر تصمیم بارسلونا تو روزهای آینده می‌مونه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90359" target="_blank">📅 19:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90358">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">💯
اگر هنوز ۵۰۰ هزارتومان رو  نگرفتی همین الان عضو شو‌ و جایزتو بگیر
نیازی هم به واریز نیست
👍
تنها سایت مورد
#تایید
ما  با بونوس های واقعی
🌐
Winro.io</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90358" target="_blank">📅 19:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90357">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtZyhIWYzgThLj__nEkxCxwvppbDf5kb_ExjQ-QmGF5thCS-dYBvklhk3mogPyn1j8fr56y9iIVVXU1d8gVTYf6158P3V46muY1Y9PxfKNK44vh4YE_jTg5KjippGBxAGi5EmhUcDyRWxvQXRifFc2hLLr8QpirYcYmJzAS1xv2SA9v_RHYLUIwfbJ2ovsQgX0WYfXkyoiEwnPbg1vAbdRRwXiKQT1XDVUTvH1mp94aTlKL2WYwRu4IyVjFuUWkCti80Zb15jH_V3bx1yzD2WGz7z9dKorJab4W3imf9FcPQwlh5gnP6Y9_nZaE7MzCeWBI3Lh2SOHgMfzB3F0xrcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g7
📱
@winro_io</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90357" target="_blank">📅 19:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90356">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwcJN-G8EgVl7I2z-fszm6BE4nlVWK4ADRAgELd-JcmSoHhNdE0tMFZnvN9Uv8aHKGfJuONS0Dn3HneIhqydQHKhtJCMefLnsnGT3hzc1p-7px--S0CwdHVxj4IGtJA0sM36JztW7QbE0lgGXtoZ1cEbwMJzMRMWdvI_r1NaW-F6jk23rKwDjgXFIvgXX0gtrNEUCGhXV1kfIZOT7ZDnB_i-c_Hk4doZdlaj5b6z0CrSfV9Rj7lfNjoi2xirTBSH7_Z3GILDIBAVV3dk1sbxrZVcSLMPIKSgPHAXtZVGQU9jDZ-D9yozUVaSUi1E7VaZ-R__OAE3F7xwcyZTsckfig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
کیت‌های ایران و هم‌گروه‌هایش در جام‌جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90356" target="_blank">📅 18:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90353">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lhcyoh2LM53Ov2awhwjkJofDREnG88x4rLC7GZvxW5fCih46Npe-_oryo5RiWqs39rdPVI0WjOfKV0nZg0SVtDiwR6LGFSUcz_z27N1YkxLx2y2bFWlGJ2SJvsEbHzGCIRTN25HOPMKypHxBohZXK_aImsUhHCsYSYpbH5jOKZyVtPxgffvgVbWotlJojuzec7sLgGohuFSvyt1HGkI0QSt0b8qgOtwloBZLv4qkwYUjF7QUJke0lMGfwEwYQfr1mK6ZPA55McfwvfjIO22AbFppnf6JsIZbOZXYL1tOMGrgNuRDjpd-CQ1HVHLYKsk825xWQ1Gf11JElKTImq4z7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فابریتزیو رومانو :
تعجب نمی‌کنم اگر بارسلونا بعد از جولیان آلوارز و آنتونی گوردون هم باز در بازار نقل‌وانتقالات فعال باشد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90353" target="_blank">📅 18:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90352">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نیمار سه هفته به دلیل مصدویت غایب خواهد بود
!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90352" target="_blank">📅 17:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90351">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQp9InKieruJSmaTe6dz0Tnp-blxFrWqsecPuMCq2JRpGFUXoRo5L70KnH0LncwLylmRxmYDMOlrjOqFTB30vtnF_KkFinXuxxyxJEokngvIhI1fnJKhhFCm5aRkXE8aFOuDhAx9CcNHhb5NR468RpnkIDTNgbZAtKHZmqd0Vlc01obB7MLEJOnoe2nMpJVox90W20zyav5ta1LVdyIHLnwGB82pbRGst_1CPXFycHR0814A-FlYFjBnWDzU95j-yugOOuN-RxZL1Q1f18C6WTjF5d-wpVxprtPHfJTBUViOqcyxpA_bDBGJt-iZvYZIcAaZZx2nis1B3442jIWccQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اتلتیکومادرید به بارسلونا اعلام کرده که هیچ رقمی کمتر از ۱۵۰ میلیون یورو برای فروش آلوارز قبول نخواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90351" target="_blank">📅 17:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90350">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCT4qND3IgAR24h5iIXFg2zE6YlheKL9JktWBbIcQ9G4ZVEeyzBpB2jTIpDKmnKFdyalysW70Ij_xYVMDm8odYg-84HPQ831c3vfRw23x2uunr4TzCYDZGFH2e9XBoc7HdUPNgr-RrmanITvh-gScR_H0_vMUqp-z4LS278MZFeYwxZxFdRYOLbb7DzMLiWA_-m0fAI4e1LcrIQdZJBdJOIMgZLBLEp7PSd1mg5WAe0sxhOlQHdqUt25Mb49QQKcE_CPzgPzCWYx-lOZKYXXZZdDPsa0_12hVkTzZDub6U6aWXa6-t8-mAu_Zqw3cc9HVyOZMFk4Rq655mrZXuDoCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور گوردون ستاره جدید بارسلونا برای عقد قرارداد و انجام تست‌های پزشکی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90350" target="_blank">📅 17:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90349">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAK-_O42gnhpyyKmGhsHlyIDwwBKp60RYHYjHWHFz3m5weiPKeouOZTytcfrI6WKHrDZ3ra2OBLDcz3M3xc51tnquPlJHgTklTJoBEUxWNnb-ZoEyl9l9LwVGVmhu9TCb0j6j8raTCT1xITAUy6I9HGcSfrcxCpBGg5Y_HzB8crfPDuJa9ewSpwXzCSB5C_pqCZV3dKDzTFLPnbAUQqgzoMAyv8icUN8XyuvzR49TnYa0YmyJ3ouvNch8Kyu3Lv3-neD03vL5nJgTarGYmKNj37dUNZ470aLt81fDATV4wb8m3fws0kEPV96EDsrHjZkfp-QrDA2ck6SDMVhnDf9Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
مراسم اهدای توپ‌طلا ۲۰۲۶ روز ۲۶ اکتبر یا به عبارتی ۴ آبان‌ماه در شهر لندن برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90349" target="_blank">📅 16:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90348">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1FXFFXpM_Chb30OxW_VhS61Z9DCyvtT8wVxfJzF5AFjtn5o8cMSJp21rA8JMi-7vAw7tcUFRsdJRQnjRcBkcIJ-Vd8_ac57UpkmCWAA5np03EmfiQd2tow4QJ0xRlVQMrJWi8UHa-8PjJV7-3i2k9q5mQeWRkAUJzbee1Mgb48kpXs-yIWmdz10MG2O-F2otzE1Q0Lcg0CufYLPLXYj0F6QLPBo46Jt0chQeDX7fZ4TiVabW5XinZimY2RMlFzA0OKpln7r35mBnz-WQC-CmU5NdrtlwhVnt2KUCkZlS-39bLmWer0tFv2Yr__wpG_Rn5Iegw1marvFatzd0qFkoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مارکا: اتلتیکومادرید می‌خواد خولیان آلوارز را با قیمت ۱۵۰ میلیون یورو به بارسلونا بفروشه
💸
‼️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90348" target="_blank">📅 16:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90347">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cf1gDsMuLg_QmIo5TUMwIXS0q4SSk3ZCJfXboroWF6NN8gkqdtmXb4Zmqn8g6dDy2vPn1hJ44onQvDxSzFtG7g_d_2C8XKH_r878M7xwVYTbZLvA8RxDCYYATyzaogekk5aEX7k-IBQimbHXre06a-_FZ5sDb94mtNMH-yQw6u3nsYw91imW1lpt5n8XGGuTd6k3Mdz3sa-2S5LOQMQcqj0XjkxgoXprMlx0Re7Go7_zg4mcrIftvrQai-FJ9GmjZCbAYEcacBkNy43LQ2TdIAHSHCZSni4O2MpKn-9hBRiXwzQzweF_SXrp4-ZL1d9U6ksE_oNT5bJOtLiG4cw-9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه عملکرد دیگو مارادونا و لیونل‌مسی در دو دوره جام‌جهانی که قهرمان رقابت‌ها شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90347" target="_blank">📅 15:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90346">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb77f6f337.mp4?token=vX-onrmIX0xUg2AocwbRGIi9FqDAWpVtvoKnd0WOW44UsGxAFwP0ldc0oJ9EIm8rTEeNWIfCQHTGQy7vUrC9VU6tDD3ZvgRENv2Uq_xL2cn0a_JL_mk0hyxByqx7nRn-BmDszh2-fjYCIZi4WderOVtHhKP-NG_frGr5c97IQG5ayTEZi03DH8Trj7WOO3PbtC3Xh1kT9TTxrTVC6PL02uxksCr0dWUs-_Wg1cMt4aMYAIrSVLjt-qACpV8eAzMloTv07XHLb-wTGM3-4LUy2tVjKqguRbDLuYXprRV4kVAXCdAx5Z2gxT9lxqowEziqvK_Mhf3HNQvKY1IT7b5lEQtGNShSSSjClrTr9yfbX7FQMlP4fWpsL20Hoahth94k_4TijDHvzW9Ur8Q1fPFgxWYb-MpOtZyxBl7a0yodb4pV1X_1-QEDPFEzYZfdDZSeHR9NEMD1ZqLs1TlftiVhpjvTJScSX02gO70y6htlqAjz8wOXjCZ05hscbev_V2mrFQS1eub_OBgpNLAN6RIVqzH7aISGsDe71S3x7q0ChFw2fnpTA5sSk7Mi_MYM8MVS3zFX4whsM4xhLWougSSO_oz3u-TSAmyqldUN8367e351UraAQrTs6dZfVaTa-s18kyb-Z-z8a-GlsjZkqBFoXKrpIj3bduJzfgkt4in1U9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb77f6f337.mp4?token=vX-onrmIX0xUg2AocwbRGIi9FqDAWpVtvoKnd0WOW44UsGxAFwP0ldc0oJ9EIm8rTEeNWIfCQHTGQy7vUrC9VU6tDD3ZvgRENv2Uq_xL2cn0a_JL_mk0hyxByqx7nRn-BmDszh2-fjYCIZi4WderOVtHhKP-NG_frGr5c97IQG5ayTEZi03DH8Trj7WOO3PbtC3Xh1kT9TTxrTVC6PL02uxksCr0dWUs-_Wg1cMt4aMYAIrSVLjt-qACpV8eAzMloTv07XHLb-wTGM3-4LUy2tVjKqguRbDLuYXprRV4kVAXCdAx5Z2gxT9lxqowEziqvK_Mhf3HNQvKY1IT7b5lEQtGNShSSSjClrTr9yfbX7FQMlP4fWpsL20Hoahth94k_4TijDHvzW9Ur8Q1fPFgxWYb-MpOtZyxBl7a0yodb4pV1X_1-QEDPFEzYZfdDZSeHR9NEMD1ZqLs1TlftiVhpjvTJScSX02gO70y6htlqAjz8wOXjCZ05hscbev_V2mrFQS1eub_OBgpNLAN6RIVqzH7aISGsDe71S3x7q0ChFw2fnpTA5sSk7Mi_MYM8MVS3zFX4whsM4xhLWougSSO_oz3u-TSAmyqldUN8367e351UraAQrTs6dZfVaTa-s18kyb-Z-z8a-GlsjZkqBFoXKrpIj3bduJzfgkt4in1U9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواداران جذاب الجزایر آماده جام‌جهانی فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90346" target="_blank">📅 15:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90345">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spZNVrTJHOv-q0GWI2aKTMXDGMM-AUzkscwK4yexcJoxzfLbnvVv3WkbQbRT0YQxZ6UytkNdcsKO_DoEqO86Nd_FIZo8-VnyFRduR5h-_A_515sedpGKIdGoBIgw6Okx8yitKaoSCScPgFV0DT_GfTSnQ8cTOfeUF3Wg45U_l-EwLv7UJ5AoVmt2CtHeTHVX9ukAi_VqoqKYa531qhS5z3QPTdUyXvmxosQuLdYbjfqP1X8snSMKCFC0hqTmQJOr396rNDlZK7xN_OuFu4FT86lHIadXloDvIwbDPEQlylsjPkI7Gr4A_gfR0OrSPt5btkaUmq7htDmSIIfKGiKEKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
🎤
امروز دور جدیدی از رأی‌گیری برای عنوان جذاب‌ترین مجری فوتبال را آغاز می‌کنیم.
❤️
عکس‌های جذاب ۸ دختر از دنیای رسانه‌های فوتبالی را تماشا کنید.
1️⃣
و هر چه سریع‌تر در کانال ما به گزینه موردعلاقه‌تان در نخستین تقابل رأی دهید</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90345" target="_blank">📅 15:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90344">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFLBcSuIzlydGrz518Cpt4Wur3sA9s6v7TqAscS3V2D-8HwAqEZdoEU-XQY3SbYXqVIYj-36FaC35gkaPbZHT4de-aAmDK1q1aDEr96qUzVgsIE_P8YOdjXyCYVZ3A3kllH-GKbYj0C5p-spePcFw_9T96MQ_sermCJKxp4AjutnSWyvzmYrApDo9rCxO4lsm6aCUaMJZYwfAI_LZnbczYBwNPARijXF78S9IMuw8dzg5VqoA6ce5lapmDHN9i4oeq84Pl83Ee6Bp50Q1K2sToY7Qzn87bAmmg3XsEbt62DHFrJiaEBa2UWL4uLtGXg5CdfmjZldCPZ73eb4sdInzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه جالب نیمار و لیونل‌مسی در بازی‌های ملی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90344" target="_blank">📅 15:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90342">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEjRUJUzXkmPPO-cRg-7xQxfuom8Y_RGmc3FU5CPQX4qDSLjthuLSLfPAhdCFDsKNlLivGfDmNPKjuwGZmEB56OsN6tXnMQVySyD2K9FOrWx2PfHcm-P3oLhtIhURX4lORMIsDmOJkgLyf9HAKTU8zL8dX3lrxkqHrRfMifO4Uzl8i0ynYv_r7qR0MLpxe8CrupXOAcAkfKii8mlWPzoAV5Yg_pbx3IAGtm8ECAQQBs4itMwnVtf6HTwp7PpIsn5jGB4Y846lOVcAZ-AWAVzh7yuewExon4I_8B0liQgRmEiWKDFcfX74208kI4evaKkaipNNpGqeDoCBX18owJ7nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین ترکیب آکادمی تاریخ بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90342" target="_blank">📅 15:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90341">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdadf29b0c.mp4?token=drmocuM3u4b0nBdplz0WfMds5eoaCsOiBljkZpO1MFROXuvM0Xi80dBCQ2VGURijVDLnhjevROJMlcI2VyvFZgsEbc8bZ6MimDnqibz1NHy1CuDyB6G2BIkSGALW49YIZG7PbSc9nCG8CSg5lvPiDflzFemHs3te7ZGbN1jUUUuvCyflVUdkPHqKmYpK29XV5LJvXbldAuKOVCNqSGSAxWilbtTOoOlIdhGGXELJsV4rOIb6hVqXoEhUW4dmiVX_rgS3hyDqxl00OF0bXBGarJ8IAJD1QqyWvwhBK64TmOSBd8ppSWQ9tEt5DB-M4yhwVf9NPFyRHKbd-TqPJ_IR6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdadf29b0c.mp4?token=drmocuM3u4b0nBdplz0WfMds5eoaCsOiBljkZpO1MFROXuvM0Xi80dBCQ2VGURijVDLnhjevROJMlcI2VyvFZgsEbc8bZ6MimDnqibz1NHy1CuDyB6G2BIkSGALW49YIZG7PbSc9nCG8CSg5lvPiDflzFemHs3te7ZGbN1jUUUuvCyflVUdkPHqKmYpK29XV5LJvXbldAuKOVCNqSGSAxWilbtTOoOlIdhGGXELJsV4rOIb6hVqXoEhUW4dmiVX_rgS3hyDqxl00OF0bXBGarJ8IAJD1QqyWvwhBK64TmOSBd8ppSWQ9tEt5DB-M4yhwVf9NPFyRHKbd-TqPJ_IR6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم‌ و صمیمی از نیمار در اردوی برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90341" target="_blank">📅 14:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90340">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9f0d340d.mp4?token=hEctQGkXfaA2nIOsUykWc87ISW4RvPEmuxc6IZroMbxdKZ6PA2bjq1b_1_lgvgf6Iu4fZBMPr7bNU71aVhR2cEf2rwLQYFGc1UekEXUZMxGWwhb6-ZoqvjHjEzXtx7UssGp6vsLf0ylWoFHMt_sqEJE7LHCNKx7caEmsac6OXurXnK3F_MaM89IB8OoTpd91rrx7bCQnOkisWsJVSUFyglDgkHlPjcrhMwKUqwFtLxg_Qvqv7Cl1_Hy0yRWd3h0qMs4GVY9dvLhAUiIqXWI0weuRZECsbqWOsOFkN1VqhcvUDEbSOX0sgNJ6TTw-qWV1Z1viFIwGse1pEhrwhm1jjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9f0d340d.mp4?token=hEctQGkXfaA2nIOsUykWc87ISW4RvPEmuxc6IZroMbxdKZ6PA2bjq1b_1_lgvgf6Iu4fZBMPr7bNU71aVhR2cEf2rwLQYFGc1UekEXUZMxGWwhb6-ZoqvjHjEzXtx7UssGp6vsLf0ylWoFHMt_sqEJE7LHCNKx7caEmsac6OXurXnK3F_MaM89IB8OoTpd91rrx7bCQnOkisWsJVSUFyglDgkHlPjcrhMwKUqwFtLxg_Qvqv7Cl1_Hy0yRWd3h0qMs4GVY9dvLhAUiIqXWI0weuRZECsbqWOsOFkN1VqhcvUDEbSOX0sgNJ6TTw-qWV1Z1viFIwGse1pEhrwhm1jjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد جالب و شنیدنی هیوا یوسفی از وزیر ورزش و جوانان که هیچ نظری درباره قطعی اینترنت در ایام اخیر نداشت...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90340" target="_blank">📅 14:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90339">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18e2b0b1c0.mp4?token=fTyppUzWBJ0PKeRtoHlRkjrabkukhRzxzlLj_ED-YUl_D8-JkXvuqjA1XAZlU4c2XhXnatI-nZXdtEt4THsOuLB_AzNzpVyl3EUIhXKe75-tkqPSU2dzyO6Eh3kZyq-f_e_7y-0ruNH-gBlGK8rST1Ezv4GeoKTXsRijfKIXtH19hhahsNbSLeT8T73rLZ8-2awfRjs5AG9SU_JETiCiNHlbXMDarBG45qWkMMrF2ZqeUYaWeUWW7gNfRyKHakf2NhSseD1MFUUxXrIMFdM0kakOPYR0nlK15_8Zn0wPtBGCGfsF1G7VqoRrVNK34SQUTmmSwwTdbKzGt2r1FOqJog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18e2b0b1c0.mp4?token=fTyppUzWBJ0PKeRtoHlRkjrabkukhRzxzlLj_ED-YUl_D8-JkXvuqjA1XAZlU4c2XhXnatI-nZXdtEt4THsOuLB_AzNzpVyl3EUIhXKe75-tkqPSU2dzyO6Eh3kZyq-f_e_7y-0ruNH-gBlGK8rST1Ezv4GeoKTXsRijfKIXtH19hhahsNbSLeT8T73rLZ8-2awfRjs5AG9SU_JETiCiNHlbXMDarBG45qWkMMrF2ZqeUYaWeUWW7gNfRyKHakf2NhSseD1MFUUxXrIMFdM0kakOPYR0nlK15_8Zn0wPtBGCGfsF1G7VqoRrVNK34SQUTmmSwwTdbKzGt2r1FOqJog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پيش بينى فرزاد آشوبى از عملكرد تيم ملى ايران
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90339" target="_blank">📅 13:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90338">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EI57OpYkp3O6noOuAGiOoSwmq5An-sTywWHFc5ZEogdj9K6bIb3lospObZZq835C__o4f_EeiB-L7FkfShOyBunZAXi35kjkjx_BJcnbGOvBvUSXVyiTTrmIHUrwYPr4tLU0TGLyP6MX-phV2N2iGQ9UPft4blsTx7xRIW5u3DcwCb3v9qNdXI0_VtUGuGW4yf3AVnSRZMfB8vAI0ieo8pIFsLpphV6VChFB46NTqH8-E5LTqRdC0073hQhgc1OUq2rW8SAALmubS-kDf926LHEa6EVzhvy2yjx-ckxKOgcOij0XaNFb1kfIY704ME9Bm7ZoZpfULZ5YC49NcAbIMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ۱۱ ژوئیه، ممکن است شاهد پرتماشاگرترین بازی در تاریخ جهانی باشیم.
🌍
اگر هر دو تیم آرژانتین و پرتغال صدرنشین گروه‌های خود شوند و تا مراحل پایانی ادامه دهند، طرفداران شاهد رویارویی نهایی بین کریستیانو رونالدو و لیونل مسی در مرحله یک‌چهارم نهایی جام جهانی خواهند بود.
🤯
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90338" target="_blank">📅 13:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90337">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k18YyizcJnvFO91BYyRwwit15LZlmMxswQRBQd7NPLj8ikkhE63nO8H9uq1ujm1UOUUDei6IhP7gRTCsl6mlcsF5PlUDc85l6y_mAh8cr02FbL9IkAG21W5TvUahd9CTS8yWkPQmCUwiFONf57BsOeJXDp0Y8SceRip-VLQ19_c7FnsmjoJAT3HyVL9kzKFmbTMk6PC-6TqhDyHOQWyja52aElqZWx7YRUXfBDVJsxAgGUjzOkAJNjegqWB3mTVHxFcEiY0K60mpEFyRDEHCB8T5zMKKsmCVacRSu1jU7HwGUEFOeDadd_zdgpODq7YqEa53mHZjgAIgK8Cjn3gp9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماره ده‌های تاریخ تیم‌ملی برزیل در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90337" target="_blank">📅 13:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90336">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31f588b63d.mp4?token=jreqQj77b8x9nFfo3qsouSyawaVyuMijFKx7ZNpnL0Wd1gi3qjlXh3dNXkPRCLC5nAcbuklINks4282H6lTXT3o7mb4dw_dG0u5m98tQdKS7Zuu9HuHIE9wjKVdFxqvv_Tub4iiYIh0kZ63WcvGu-azbs1hStCHoTiY9hQqK6Ly-Si6pLiHX5k2TY-Tmrmv0hweY6areqqcd-pNbBwA1hU9njLQkJAsNZ3H0d4AYrDrXsb6_ivmxoFJdy-Pz6v-NBWJKeJwQkRs2vnPqvF_AnteUDiGp9hJ2oFkCq3xaR3pghGv2niXbYb89DDBd79CcRxshVarbDtIqdGhQaNKkKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31f588b63d.mp4?token=jreqQj77b8x9nFfo3qsouSyawaVyuMijFKx7ZNpnL0Wd1gi3qjlXh3dNXkPRCLC5nAcbuklINks4282H6lTXT3o7mb4dw_dG0u5m98tQdKS7Zuu9HuHIE9wjKVdFxqvv_Tub4iiYIh0kZ63WcvGu-azbs1hStCHoTiY9hQqK6Ly-Si6pLiHX5k2TY-Tmrmv0hweY6areqqcd-pNbBwA1hU9njLQkJAsNZ3H0d4AYrDrXsb6_ivmxoFJdy-Pz6v-NBWJKeJwQkRs2vnPqvF_AnteUDiGp9hJ2oFkCq3xaR3pghGv2niXbYb89DDBd79CcRxshVarbDtIqdGhQaNKkKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیب منتخب سهراب برای حضور در جام جهانی
👀
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90336" target="_blank">📅 13:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90334">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اولین پیشنهاد بارسلونا برای جذب آلوارز رقم ۹۰ میلیون یورو به علاوه آپشن‌ها خواهد بود. لاپورتا قصد داره قبل جام‌جهانی این بازیکن رو جذب کنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90334" target="_blank">📅 13:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90333">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوری از فابریزیو رومانو :  بارسلونا در حال آماده‌سازی اولین پیشنهاد رسمی برای خولیان آلوارز است که به زودی ارسال خواهد شد؛ هیچ بازیکنی در آن گنجانده نشده است.  خولیان پس از رد قرارداد جدید ماه‌ها پیش، به اتلتیکو اطلاع داد که تمایل به ترک این تیم دارد.…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90333" target="_blank">📅 13:00 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
