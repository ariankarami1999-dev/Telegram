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
<img src="https://cdn4.telesco.pe/file/UtH2I92lfk5ugLHHd0UGRuJHNly02HUwNOlICNEIazy0WmodVyW1N0ZVPKzL5IiRh6T-85wQzjZ3_GmE78mU8hLn-ZRn_lF9OIpM2l6p2gCjiiEzsWmyBtP5_nlYH4ZtbknYMkt82dhCIXDpYVUZKSdOogMJyJt8tctnkRbESVdqdRx4LxT3NcT2afzZk4nSnpABycr20ZQrE6ZXYFd6MZDK5YgwCsOaEIf1wPe-sajipBzk2EE9ZB29nf4LBeekBG_n77ZzZksHzmrOoDb5TAGaY16qV28Y3XXae3V9pNNdUDzmYqDc8fjPPB3m-NZLAtDbIzwBtaaA0Go6yfzMng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 09:45:22</div>
<hr>

<div class="tg-post" id="msg-140781">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🗞
لیست بازیکنانی که قلعه‌نویی ازشون ناراضیه و شاید دیگه دعوت نکنه:
❌
محمدمهدی محبی
❌
صالح حردانی
❌
سامان فلاح
❌
احسان حاج‌صفی
❌
حسین حسینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 519 · <a href="https://t.me/SorkhTimes/140781" target="_blank">📅 09:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140780">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
خط خوردگان بزرگ لیست
😀
محمدحسین کنعانی‌زاگان
😀
روزبه چشمی
😀
شهریار مغانلو
😀
هادی حبیبی‌نژاد
😀
علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 581 · <a href="https://t.me/SorkhTimes/140780" target="_blank">📅 09:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140779">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
پیگیری‌ها از مسئولان باشگاه پرسپولیس نشان می‌دهد که هیچ پیشنهاد رسمی از سوی باشگاه‌های خارجی، چه از قطر و چه از سایر کشورها، برای جذب محمد عمری به باشگاه پرسپولیس ارائه نشده است و بحث جدایی این بازیکن صحت ندارد. / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 915 · <a href="https://t.me/SorkhTimes/140779" target="_blank">📅 09:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140778">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
یازده سال گذشت
❌
روحت شاد؛ هادی جان 24 ابدی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/140778" target="_blank">📅 09:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140777">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
❌
❌
دراگان اسکوچیچ از طریق واسطه‌های نزدیک به فدراسیون فوتبال، برای بازگشت به نیمکت تیم ملی و هدایت مجدد ملی‌پوشان اعلام آمادگی کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/140777" target="_blank">📅 09:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140776">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
یه سری شایعات از بازگشت اسکوچیچ به تیم ملی در حال انتشاره که نه تایید می‌کنیم و نه رد می‌کنیم./فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/140776" target="_blank">📅 09:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140775">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRSptN5ckDuU_RGiR2BEBdnUhybcjH1Rgy5pGKK9ZElN0wS0dw3VNCN2CC3XNRhwhOyjG70UaVxRg7JVD1BzKebSzGN4zrbb8ej5JIgBPMCW-XCm_cuF9YYzkt4nnRGx7XVfUjN8iWxA4DMf49wUNQN63rxjNV86UDQPg261RpMaKlML1GxjrQV888IoCHBDbdDmpic33D1UU7y92Gl0QJOwgjrbIUm67oopmVKjCuv0Nw4Yr58r8LF4702AyA6pSmU4LU0UPZwNWBZOml4zF0PlTB1DNL-BOsekfc_bDE9Kvzh7ll8HGGF3Puhp1SZDyDJ3xCsKN_S_IYLcZ-cwxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/140775" target="_blank">📅 08:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140774">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FE-7JsGXAmQIgM3sFQAOMHZ38M-VmYttHJjgcHGzwgbtUR0-C5TpveqJ4q47WM1pJK-jHM8vSEAa4jO0sp9kjnuaiegW0q_3FZqA-PzQ01oNEFnL4IM52PpQcrV6c_xfrGFQV-yRPXW2x5HDYpQaIFb0ztruPmajgRozmgNbOru8X0qVfdJ4bM6xiDfYd0REXX0lZIBMVubTmlX4wNDxAWcaiVPeEdF52tpC5J5LE49eHFZkocfE6crG2KPQo3sEuKS6fQIeCVBYqk6OAWu2NntAVqgJ7ZUW_4OorPoWJEgb6_Cd_ehgN2msRIsz2AqM_lzuNknmrMr2VScuAhQwXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شبِ سنگین فوتبال؛ چند تقابل با پتانسیل غافلگیری
🔥
⚡️
⚽️
ژاپن و اکوادور شروع‌کننده بازی‌های فردا؛ کنداکتور فرداشب پر از تضادِ ضریب و احتماله؛ جایی که بعضی انتخاب‌ها از همان ابتدا جهت مشخصی دارند و بعضی‌ها تا دقیقه آخر قابل پیش‌بینی نیستند. آلمان و نروژ روی کاغذ دست بالاتر را دارند؛ پرتغال، هلند و اتریش اما وارد بازی‌هایی می‌شوند که یک اتفاق می‌تواند همه‌چیز را جابه‌جا کند. فرداشب، عددها حرف می‌زنند؛ زمین تصمیم می‌گیرد.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و با اولین شارژ خود و دریافت ۱۰٪ بونوس ویژه این دیدار‌هارو رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SorkhTimes/140774" target="_blank">📅 01:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140773">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
🚨
فوری/ ترامپ : به زودی اتفاقات مهمی درمورد ایران خواهد افتاد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SorkhTimes/140773" target="_blank">📅 01:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140772">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✔️
✔️
فرهیختگان : دقیقه ۲۷ قلعه‌نویی خواسته حاج صفی بیاد تو بازی تا رکورددار تیم ملی بشه و به محبی گفته یجوری بیوفت زمین که انگار مصدوم شدی وگرنه مصدوم نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/140772" target="_blank">📅 00:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140771">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
تعویض زودهنگام محبی، به دلیل مصدومیت که احسان حاج صفی جای او را می‌گیرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/140771" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140770">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIeEhF_g__myiahiSsrK3YFasijyTqz_R4iRnpCCf8dKpX6R3Mvnz3iOvehkm9hV4UYx3SdS4yhCTGoHfCKuZnMNye8ZeHOifEj-t2w86k0u4nzbja_ZXVQjjg0sB6vxOYoP0u-FBQ6ie3k8eoyJXWJ8kEeWGCqVEinzhkut6h0LuMWvJAv9daLMIwOPSABlCOCiaEm9-ZdCwiEmORD4xPhE-HtpGg0223EPkkjgCim9t0ReHZltC6VHDx7Jo6dRYRYI3v2qXhRHmdV9UA_AE8XA02NdZ5KklnyspjPDZFkxMB12nn8mGOTeCkspRPx9ou0bCz29z1a8v_Y7S1BeMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
عالیشاه در خانه
❌
دیدار تدارکاتی روز جمعه میان پرسپولیس و گل‌گهر در ورزشگاه شهید کاظمی فرصت خوبی برای قدردانی از کاپیتان سابق پرسپولیس است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/140770" target="_blank">📅 23:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140769">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
لحظه گل ثانیه پایانی جوانان پرسپولیس مقابل پارسیان توسط محمدامین قرنجیک
👍
👍
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/140769" target="_blank">📅 23:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140768">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c458bfa09b.mp4?token=Dfhn6HEbKaMP_z9e-Dg1l2JvhToE7PtG2K2xyVKq1N8c2ZQ6zfygOzP0iRUn5JcAGckNcFIvdjiXA1c80qNk04SdZe6yWTFs9ZmN5ncsfA9KyEWYqNDj9GmQwuMoqzbD5za4TQ4AX9CZzQQtn9o_I49W6YyOMDKOlSbW3JsqbeQcmJuyOfJkewK19TgP_1tBUQkzNAnse3SdRDIvggOe9yqV4C8Tka_nzx-hHscPGgbP7dfbm8DY6lC8O225LwqJPkdDPp2Sht43hFupExwSYdUlnBpsBp2qrkVx2DlMNQbqwqVdUgoKdc0PsrGhtA4lH9BwC1VvFbniIlA-xovqRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c458bfa09b.mp4?token=Dfhn6HEbKaMP_z9e-Dg1l2JvhToE7PtG2K2xyVKq1N8c2ZQ6zfygOzP0iRUn5JcAGckNcFIvdjiXA1c80qNk04SdZe6yWTFs9ZmN5ncsfA9KyEWYqNDj9GmQwuMoqzbD5za4TQ4AX9CZzQQtn9o_I49W6YyOMDKOlSbW3JsqbeQcmJuyOfJkewK19TgP_1tBUQkzNAnse3SdRDIvggOe9yqV4C8Tka_nzx-hHscPGgbP7dfbm8DY6lC8O225LwqJPkdDPp2Sht43hFupExwSYdUlnBpsBp2qrkVx2DlMNQbqwqVdUgoKdc0PsrGhtA4lH9BwC1VvFbniIlA-xovqRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بالاخره گداوند رو‌ بردن سربازی
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/140768" target="_blank">📅 23:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140767">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ca8ba9d21.mp4?token=IUYu6nUqaJWrzF9Ulntt1ynej6_yCghFD8h46yAINVpIb8a3Thz5KYTp2A71XPzAe8LRB_sIvkqDyGZCcjQ3flNM10z_OYsTn_W8X0N4bFuXAuuErv1GSyx_i2JcBpUR6CVwfYcAfu25fDfeN3WMFWI0E9-62xcOWchHAo5uuXcUueEg6NiwnaKW8TTfL36t-jWamsV2zxiLG3IciPWOrQB1E3aVBV6ZHKp7iBjgziVJuq5q6JqFX7EnG6eSHeEQPPB725ApqE0wH4hhCHDs3nZDRO7qBOV0WjF9F0l_pogIyVLHUUF_vASk9aEzQJxj2zmz1pf6X7jVQdSKVT-sNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ca8ba9d21.mp4?token=IUYu6nUqaJWrzF9Ulntt1ynej6_yCghFD8h46yAINVpIb8a3Thz5KYTp2A71XPzAe8LRB_sIvkqDyGZCcjQ3flNM10z_OYsTn_W8X0N4bFuXAuuErv1GSyx_i2JcBpUR6CVwfYcAfu25fDfeN3WMFWI0E9-62xcOWchHAo5uuXcUueEg6NiwnaKW8TTfL36t-jWamsV2zxiLG3IciPWOrQB1E3aVBV6ZHKp7iBjgziVJuq5q6JqFX7EnG6eSHeEQPPB725ApqE0wH4hhCHDs3nZDRO7qBOV0WjF9F0l_pogIyVLHUUF_vASk9aEzQJxj2zmz1pf6X7jVQdSKVT-sNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دلداری خیابانی به بیرانوند قبل خدمت رفتن
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/140767" target="_blank">📅 23:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140766">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxwxnHnlI1rtgGfcngK62FRwv5m2QU61Y619popQq1hzsCwhij6nRbpenXKjSJSzTXKJq3Rc-RvY9Nx00NWXrLohtdvDqPhynKxqbz3-mW_zK0vr7tuW8OG26k3B549qEKRpMpZi5Z4YI0LIkkLKtmXiC6xLG_NaSwpFc3TUSreD3bIblsmKc5XMYg5Gbz-_5EpNxOIew0Ts9QDjGYLPPcPQavUV3nJOwpDX30UPNskvtQLfflXuG0iOaxpX8djWiGc9kYYF9G464QzPbUazhvEpGLuktlOvEJcsafZLtokwOvPksogG6z5qxvZgcoABxCP4ddYAhAuDa3cJJsOqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🤍
قلعه‌نویی: اشتباهات و نتایج اخیر رو می‌پذیرم و مسئولیت فنی تیم با من است. برنامه تیم رو دوباره بررسی می‌کنیم و در انتخاب بازیکنان، تاکتیک و آماده‌‌‌سازی تغییراتی میدیم.
⚪
می‌خواهم تیم ملی رو حتی بهتر از قبل بسازم و از مردم می‌خواهم فرصت بدن انتقادها رو می‌پذیرم اما تسلیم نمیشم!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/140766" target="_blank">📅 23:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140765">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hE2yGyySFIU9yw1O-HD5_8cHl8w0YSMWtghMt8n0-C4Do-le-am0w9UVQ7YhSh2zse7H0sK3n7nklw8en898EB9N-5LDIgM3WdQzrYjqJ6dcgMeWuXAQgv-4cISDd586qQy_ocNBX6OXTNN-XDw3Fcs5BO_3cHdFRL5hwzd7iEIXkMC79EK-T3S_FG7MH9UZifpy8uV3uaX8RZ-YNPchUfzkv156UKX7mNufC_6rIaXhPGmRfklMgDW8_s9IFFTvkW4ZCGWXKWibNXpWht1SWgh5tmnA72H5atWN0hc7m0orQAXpHDcdnjdTaGOpSu8CF_7L1oVKyFfA053szYXrzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
یازده سال گذشت
❌
روحت شاد؛ هادی جان 24 ابدی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/140765" target="_blank">📅 23:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140764">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
کریستیانو رونالدو امروز برای سومین روز متوالی در تمرین تیم ملی پرتغال حاضر نشد و طبق گزارش رسانه‌های پرتغالی و اسپانیایی، اردوی تیم را ترک کرده است. این اتفاق پس از اظهارات ژسوس درباره غیبت رونالدو مقابل دانمارک رخ داده و برخی رسانه‌ها احتمال بازگشت او…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/140764" target="_blank">📅 22:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140763">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
🚨
فوری/ ترامپ : به زودی اتفاقات مهمی درمورد ایران خواهد افتاد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/140763" target="_blank">📅 21:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140762">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامپ: جمهوری اسلامی‌ هیچ پولی براش نمونده؛ برای همین فشار آورده که توافق کنه و رفع محاصره بشه. وگرنه چه نیازی به توافق دارن که پیشنهاد میفرستن؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/140762" target="_blank">📅 21:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140761">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
🇵🇹
👤
رونالدو اردوی پرتغال را ترک کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/140761" target="_blank">📅 21:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140760">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rg6B_NEmIXvxMW7LaXp5Y5ST5xlxPZFxym55emo1N3FOCXduRdfeyVQ2cdb6i640fXpXxQ37zOJpxuy96BD0nhOijPaWwoCDWIB383EsYJNXIb7WtaXUvjHv8D0yw_U95ne4nTyg0OkLHkK28qrShEmu-BJanQv1qZXSR-mLDyM3ONyBjLGF8ECbxl8bopzjScAOwrg8cvFD24yQUytq20Bre9u8Cfn7kTeScbznD_lacIevQWMi9GdazxbiHFL1gG4niScpP8kYLiFe-B5_4KmGu8ZbtkoVRdMnkdNJrgTNsUDmVDG96dS6_dHwsAQFGpDfN_ey_w9TyrG6yV-p8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇵🇹
👤
رونالدو اردوی پرتغال را ترک کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTime
s</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/140760" target="_blank">📅 21:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140759">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtI9AJZNuSgO1ddjwpYfbC1q1DHf0Slc5JnYOiehKtxJQJE1w0T2NyC_3JGJioG0S_v1I0JfK5Y5lC3iUyFF5igIP2AlmAzrA6wxnoYL5k6gx6dt5xMO3l9GKluCur9xchsffurKCTCsHMRkZiZxs7FMHo0CX4G-zZJa4kd5vVDz2g_7ZvW5ehm7bsw18cR1vJtWiVYdhKVz8miE-oumPQl47y392zV6Q2HMS45USUwKqKIQXAdvRtQ-XBoCXEZIQuWinDZzor6PzZ9pRP-S_mVONbKIo1ICfPHF8E9-f5ZwmIrzMgAJBf6ZL8wQ2N4g_kv70GAtKkPnAgnGa3-02Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نزول فوتبال ایران به رده ۲۳ جهان
▫️
تیم ملی فوتبال ایران با شکست مقابل ازبکستان و روسیه، در جدیدترین رده‌بندی فیفا یک پله سقوط کرد و به رتبه بیست‌وسوم جهان رسید؛ جایگاهی که در سه سال اخیر بی‌سابقه بوده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/140759" target="_blank">📅 21:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140758">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3fYT7epKkjJNgeiWMac8J2DWMlSvNWwk0GOvss4ias3-6bXL2Vb7BD6B6NBd8yrhtnKcaJkauGhlAE5mpeehJdJfw3nRgniPY8GWaNKqTNzCrUYL3GBaQ3-6e6d8fK3K9l69SrvAVttVR_BGFQanZX-3winLVjmozbDcMD70cSFXixZcu6ZFfkd6jOmKvTwFQhxO8cQgn24tnXJh8LwHREJeSfq2wxLaO1QnH5sCC5RSHSJyn_1q7AqaJ4adh7w09H9LF2k9WouQZC3AEYIPDP0kcx3gezk2jV5iLzT-aCB6tSBn9gxQGKOWXlUBYNLBlreIvAOVubu1FZcPBbBqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🩸
لیست مصدومان باشگاه
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/140758" target="_blank">📅 21:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140757">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
❌
مذاکرات مدیران باشگاه پرسپولیس برای جذب فرهان جعفری ستاره ملوان ادامه دارد و اتفاق خاصی رخ ندهد این ستاره به زودی راهی پرسپولیس خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/140757" target="_blank">📅 21:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140756">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4n336jjmlnGNStiLRwvj5wmSI6VtFowWqNbhdH1iKhG9OPqfCFwdZqjSQ1xwlmZYKTcAO2gDryIXIrjimTU-YjhthboddtjZdsLbHt5d1GnFWXZmjXCiqu2_h8sh_7_Y9UNeNdJxKBKa9Hs21-be_mNqLmlilz-lddAa7zmTi4rYjI-umKhuQNN9NMJN6tfT3_Izeb_I75afA_OuKZRNJR6p6TpEH1e_yrUu_xXF9fSeN7Jps9AoIWHCQTtkbiaCghOrYOXp9i-ClkERFQC-0icHieKSPAHOqKONlH8fETboLxRbeAV1sgchiE5K39J7K7pQ2XNYI1q-A7Xpr0WPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
وقتشه پوکرو حرفه‌ای بازی کنی!
🎰
اگر به دنبال تجربه‌ای متفاوت و پر از هیجان هستید، بخش کازینوی وینکوبت بهترین انتخاب برای شماست. از بازی‌های کلاسیک مانند بلک‌جک، رولت و باکارات گرفته تا صدها اسلات جذاب با جوایز بزرگ، همه چیز برای یک سرگرمی حرفه‌ای فراهم شده است.
🕹
همین حالا وارد دنیای کازینوی وینکوبت شوید و هیجان واقعی را تجربه کنید. شاید برنده بزرگ بعدی شما باشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/140756" target="_blank">📅 20:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140755">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEJYSLfE6iv1L2wxFx3jhcCV86s527y9aOHz_WyFd-fuf0HddZbDkMALzr-1EGv_wheIDt4vQ6jhBA33pzReXv3ucwHNuIyOQbCk1BwAqdHmhXGre9auEXq9JRWa9xvW0z5NiAeaUn1hYDN0rY6upka3wtvTcW9anw5VOc6lHFsW30pvrtcHAl1cwe98LY0tuwIhh4-0PmaGlKP7y--7BwxFfnYcOkEEPieNUHogm5janbNnA5CCUkaeqDpXCCh5TVrhy3KXew07y5hZrDw5DM6BgoL-Kh3v2-21vMSQi0OClX4MyxD1FCK8GbgQbZC6qA-r8XOafvHXg4lrVX7sXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
والیبال به میرزایی رسید!
🔴
با حکم احد میرزایی؛ رضا صفایی سرمربی تیم والیبال پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140755" target="_blank">📅 19:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140754">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
تیمداری مجدد پرسپولیس در والیبال پس از سال ها
❌
❌
تیم والیبال پرسپولیس تهران در گروه چهارم رقابت های دسته یک کشور با تیم‌های طلایی‌پوشان ورامین، نیروی زمینی تهران، بوعلی قم، مقاومت شهرداری تبریز، سروقامتان ارومیه، بنیس شبستر تبریز و روژمیوه زریبار مریوان…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/140754" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140753">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔄
🔄
هوشنگ نصیرزاده: پرسپولیس با شکایت از آسانی به CAS وقت خود را تلف می‌کند هیچ سندی علیه آسانی وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140753" target="_blank">📅 16:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140752">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⭕️
⭕️
⭕️
خبرورزشی: مرغ حدادی یه پا داره بردن شکایت آسانی به Cas همین و تمام
⭕️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140752" target="_blank">📅 16:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140751">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
تعویض زودهنگام محبی، به دلیل مصدومیت که احسان حاج صفی جای او را می‌گیرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140751" target="_blank">📅 16:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140750">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
❌
هفته هشتم لیگ برتر در آستانه تعویق!
✔️
✔️
در صورت قطعی شدن برگزاری سومین دیدار دوستانه تیم ملی در فیفادی پیش‌رو و انجام این بازی در ترکیه، احتمال تعویق برخی مسابقات هفته هشتم لیگ برتر وجود دارد.
✔️
✔️
در این صورت، دیدار حساس استقلال و تراکتور نیز ممکن است…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/140750" target="_blank">📅 16:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140749">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⚽️
گل های بازی بانوان پرسپولیس چهار - صفر ملوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/140749" target="_blank">📅 16:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140748">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d02c1a357e.mp4?token=Jt24mCeikniJtAWD6c3ZhkAI3Yc6SJRqxSgCbomMK0SQ4AeKPOKRY0lQQdvgDrFONFBhO0e_oTxwuoBs40KKSqb94CaJxLHjhXzNNBNnvOOjlD2PM82y2sJNOqfMJQOQJQHawPEgAnV5kOAE7Zm5sprSpVHeuiGvt8VdF679oYVeLe04opTRWkI0M8ow5NOk_pUooOilyZWE5GRJfciZt1QmhikzZSN35SVHZ7pFmqFwW1CPAEuglgupCvspFwCrPd3u-kS-XKs-gmL1sHxAN436sRvJpvYI5TtJDpJiPrBPOUBdTDPbLTHyqrlwKzJaH_ACv0vvCV8o6JKBzI0mDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d02c1a357e.mp4?token=Jt24mCeikniJtAWD6c3ZhkAI3Yc6SJRqxSgCbomMK0SQ4AeKPOKRY0lQQdvgDrFONFBhO0e_oTxwuoBs40KKSqb94CaJxLHjhXzNNBNnvOOjlD2PM82y2sJNOqfMJQOQJQHawPEgAnV5kOAE7Zm5sprSpVHeuiGvt8VdF679oYVeLe04opTRWkI0M8ow5NOk_pUooOilyZWE5GRJfciZt1QmhikzZSN35SVHZ7pFmqFwW1CPAEuglgupCvspFwCrPd3u-kS-XKs-gmL1sHxAN436sRvJpvYI5TtJDpJiPrBPOUBdTDPbLTHyqrlwKzJaH_ACv0vvCV8o6JKBzI0mDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ملی‌پوشان فوتبال ایران پس از برگزاری دیدار تدارکاتی برابر روسیه وارد ایران شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/140748" target="_blank">📅 16:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140747">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/140747" target="_blank">📅 15:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140746">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rG4ETJ4a4Q9U1ANAsCSe9jsoFn0Bdf2g8Lla0ADFrVGKh0_g_x81rDi4C12pFXmfP3AGH8N8tq_m3QkEKbBWiYBIqIBuLC9f2fK4NvqrkAska4jbI0iNBbtKxP4zIfe7lBWaf7YoesuAAv0MgVSSwEElG9NJD0IUx0dSfXGUDgOkphTBnJSP4Bqib9-gjLtWsIVNCHAnD-3G6hu6VjDYhPM6pKHnlmxlFdNKqJCvItcjLnopw7Vk9EeYCrUFY58k_wE7xUe1ffNAR6CpG9hmRusmgJuNcSi9rPr2bwt-RkYIX4y1g2VbvKojZm4yg2dEgKenNisGtjEQJNIkid6w6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
اگه درآینده جنگ رخ بده و بیش از 90 روز طول بکشه بازیکن میتونه یه اخطاره 30 روزه به مدیریت باشگاه‌بده و بعدش‌هم توافقی قراردادش رو فسخ کنه اما اگه جنگ کمتر از 90 روز باشه بازیکنان خارجی باشگاه‌ها حق هییییچگونه فسخی ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/140746" target="_blank">📅 14:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140745">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/140745" target="_blank">📅 14:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140744">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⭕️
⭕️
ابوالفضل رزاق پور مدافع چپ تیم فولاد: از پرسپولیس آفر دریافت‌کرده‌ام‌اگه دو باشگاه به توافق کامل برسن درنیم‌فصل راهی این باشگاه خواهم شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/140744" target="_blank">📅 14:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140743">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔄
🔄
عملکرد یاسین سلمانی در دیدار های تدارکاتی  امسال پرسپولیس: ۸ بازی - ۴ گل - ۵ پاس‌گل :  پ.ن تارتار به شدت راضیه از یاسین   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/140743" target="_blank">📅 14:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140742">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
بازگشت دنیل گرا به تمرینات پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140742" target="_blank">📅 14:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140741">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKn4ZFi_wsCZD7yjYpSV9W0W-m6Bs9OlP6R9KvhY-G_oOIh7MPy2MnqfKz1_z6iFzQgtu19m9Gg2QUQKI-sVE9HnvXeUSuCVGaYApumW6E08pH3tzfyBgIT8IH9xyL_XyXR0_pDSEZg59F3FUJmcUAcBLSgJc4qkhfNiGrhlUJOg8DL-lEeXUgAMrGT-6PZcYIASqVHqL2dXjrFx9jz_f_FrdOWawhrDjRuwvWGEtQrENWBhHmsxSoFGZHbVV59XFYdZr4VtzFh9ymqeFSzqJ6sQHEhRrw39NGTh3hPWWqNBc8glknOmT46A99QmSKefSJfcfUoKDGnxGgYNYnV-Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎲
هیجان واقعی همراه با کازینو
اسپورت نود
🔵
کازینو آنلاین
اسپورت‌نود
، هیجان واقعی با بردهای بزرگ همراه با انواع
بازی‌های کازینویی،
🎮
انفجار،
💣
رولت، بلک‌جک،
🃏
اسلات و بازی‌های زنده
همراه با پشتیبانی ۲۴ ساعته همین حالا شانس خودت رو امتحان کن!
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/140741" target="_blank">📅 13:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140740">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‼️
آخرین وضعیت پرونده جادوگر فوتبال؛ تمام اموال نامشروع مصادره شد
🔄
🔄
رئیس کل دادگستری استان البرز:
❌
❌
در پی دستگیری و محاکمه شخصی که در محافل ورزشی به نام «جادوگر فوتبال» معروف بوده است؛ وی به اتهام «فعالیت تبلیغی انحرافی مغایر یا مخل به شرع از طریق ادعای واهی و کذب» به تحمل ۵ سال حبس و ضبط اموال نامشروع حاصل از جرم محکوم شد.
❌
❌
حدود ۶۶۰۰ دلار، بیش از ۲ هزار یورو، ۸۰ سکه تمام بهار آزادی، ۳ شمش طلا و مقادیری طلا و ۲ دستگاه خودرو تویوتا لندکروز و مرسدس بنز از متهم کشف شد.
✔️
✔️
متهم هم اکنون در حال تحمل پنج سال محکومیت حبس صادره است و کلیه آلات و ادوات مختلف مربوط به سحر و جادو که از متهم کشف شده بود هم معدوم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/140740" target="_blank">📅 13:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140739">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
🏟
بازسازی زیرساخت‌های پرسپولیس
✔️
✔️
رختکن‌ها، چمن، نیمکت‌ها و سکوهای ورزشگاه شهید کاظمی بازسازی و بهسازی شدن. بازسازی کامل استخر درفشی‌فر هم تقریباً تمومه و قراره نیمه دوم مهرماه به بهره‌برداری برسه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/140739" target="_blank">📅 13:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140738">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🤩
⚽
شاهکار پیمان حدادی در پرسپولیس؛ درآمدزایی ۱۳۶۵ میلیارد تومانی از پیراهن سرخ‌ها
❌
پیمان حدادی، مدیرعامل پرسپولیس، پس از پشت سر گذاشتن نقل‌وانتقالاتی موفق و پیروزی در پرونده‌های حقوقی باشگاه، حالا با یک دستاورد اقتصادی قابل‌توجه مورد توجه قرار گرفته است. بر…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140738" target="_blank">📅 11:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140737">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fl9XNwfUbVGKChhpSG4hYZbIdSkhB5UyeQEL9jx0bFKgT8H1hrSpmeKlRhGFNY-yIEd7W74pX-q5foQD582mOL5zIud6F1Yx_Aq6iHscrnTwMMxdIym4CjBfy12mJ0QhlAfZeJBOUqzWNOut8bSf-ZJs_OCl5BRFMMx9lxWYObmYH8V8DGo4of_yhtFnLXuF-DphUbU_2hvQTLMX16gYYUm_lI_EahnKE9FnONk-6GQumRJxMB3GhBZF4J1e10IGauxHzCEtPJLlXOB6AoA5m6JD0GBRQuhHqTtDckTJC_DtNMYGMN6pTdm1299RCkb8aLNGQmuc7ay7QFcA4lGg4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140737" target="_blank">📅 11:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140736">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3297ba87bf.mp4?token=vOJiL6Sj83l-DelTNZ4CSWu5MASfYvfq3ruC_UPFKWj5WKuPB1oRCz_N17Aqk_EHBtoF30pDZaTYA6TrenN4IV1R6-rLdOvw14y07zT_yiE1oWjOhBJnolKtUo7ns4s7e0hQnPtcs17xpKcOwmmKxGLYgVsE86oCqnf-KCUOP3k2_ZK4cxsu1TARhzupgKADHanaBBXdnPhIcqBE1udATnHqpdjEDOEoRWCFOpupavcwIgQEaZVtaYJLvHD0VitzSgYdsnVK7WGmFyOVxh31SEI3BMtXkKCPNPAc5QMrLBiuNsv0rrlEqiw_Do__5ruyZe5wyILSFi1cssU6up7-ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3297ba87bf.mp4?token=vOJiL6Sj83l-DelTNZ4CSWu5MASfYvfq3ruC_UPFKWj5WKuPB1oRCz_N17Aqk_EHBtoF30pDZaTYA6TrenN4IV1R6-rLdOvw14y07zT_yiE1oWjOhBJnolKtUo7ns4s7e0hQnPtcs17xpKcOwmmKxGLYgVsE86oCqnf-KCUOP3k2_ZK4cxsu1TARhzupgKADHanaBBXdnPhIcqBE1udATnHqpdjEDOEoRWCFOpupavcwIgQEaZVtaYJLvHD0VitzSgYdsnVK7WGmFyOVxh31SEI3BMtXkKCPNPAc5QMrLBiuNsv0rrlEqiw_Do__5ruyZe5wyILSFi1cssU6up7-ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
۶ سال گذشت...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140736" target="_blank">📅 10:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140735">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✔️
✔️
مصدومیت دانیال ایری از ناحیه کشاله ران پا بوده و مداوا روش شروع شده تا بزودی به تمرینات برگرده؛ اما بعیده به بازی صنعت نفت برسه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140735" target="_blank">📅 10:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140734">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
🏥
دانیال ایری در بازی آخر تیم امید مصدوم شد؛ MRI کشیدگی عضلات لگن و بالای کشاله ران رو نشون داد. کادر پزشکی پرسپولیس هم درمان و فیزیوتراپی رو شروع کرده تا هرچه زودتر برگرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140734" target="_blank">📅 10:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140733">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
❌
گروهبان قندلی: از بازیکنانی که به آنها فضا دادیم اما نتونستن چیزی که مدنظر ما هست رو انجام بدن در اردوهای بعدی استفاده نخواهیم کرد
😁
✔️
✔️
این بازی ما رو یاد جام جهانی انداخت و سطحش در حد این رقابت‌ها بود. برای ما بسیار مفید بود هرچند از نتیجه ناراحت هستیم…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140733" target="_blank">📅 10:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140732">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
❌
گروهبان قندلی: از بازیکنانی که به آنها فضا دادیم اما نتونستن چیزی که مدنظر ما هست رو انجام بدن در اردوهای بعدی استفاده نخواهیم کرد
😁
✔️
✔️
این بازی ما رو یاد جام جهانی انداخت و سطحش در حد این رقابت‌ها بود. برای ما بسیار مفید بود هرچند از نتیجه ناراحت هستیم…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/140732" target="_blank">📅 10:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140731">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLByMyoARZW4Vd72o5-gfqWozJV1P5yQjFaIzQKZvDopwpM66Dy-QjFbErBQDgBg3gQxv-B24DYR2h6lfiqXW1RGzl7TILSoBf_wls2MttoH1YgrT5yOzcPRzT9D7vL3Fh0y_i8Zz2hZwZTzgo0CGZYtZ6ttDYsvtuUUR2DSn9jAmCbpYGWYQwcxOMG3FDjZ9UO8dRuGCMYy456k66shMsdFTT7SVVGgFqOEZkqU2icqnh_RJFBDDgxejRPlnT8u3C9EO9z8MCy_--fMZgtCIIkWrfuF3tBrZEnoVfqZ98OSXcXrm1S7haOTpaTTJ_kexA1WIC771i8llPYBoj4iXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
حمله تند روزنامه‌های ورزشی به قلعه‌‌نویی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140731" target="_blank">📅 09:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140730">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXId1JR2rYnRgjevPcFfHuIxnu9XRZ6x070__aCxjuURHHr_Zi82Dm1NQKx2B3j1eaL5T4gc8XkgiuWJWh8Kg0PQLHcVEU3FEH7Si4bnZ41iIh2NWVJLsCxU1ZUrg1JujIS-PNMkHpPKf5sfpxtrEZ4fM-fSEBRhTU5w3pDYk04Qn5wsNzKESxVcw3U-LBI_tyWvfA4t5MCrXc5UA-76Am_WGITnd-VcPHysdyRcVEhwI3MsljwVhAI_hFEBtAN7EMwX6WTQUhyO1hGknek44baJNifSipYjsvzFPhA8-U79tAJjya2D0ngY0_UJRfHZAi7IuamqszK9bTT6JFjKnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140730" target="_blank">📅 09:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140729">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmhMi5x6CoFnihnOW1mPlMmFc_W1mH0wdCn3VU2UrzyVvy6RxA-aA8m7tV7auN3pRJTeU-Y-6kN_83-a3jW1RRUVf2m1q_MobRwWLPfndk7PTMYMYYet96ulDtvf6n4zOKwDiEOArnj_ddJEopuyqO75brN9sAyFKOkVPvAVNKVCDB1LI0kFd4T8huuMhoalHW2b6MQLR-9bAqT8Ec53wAXP8PtxkWyg8rJtDRADwoTNYnwqnwoHblk1PG1tt2vaHh2vafG6fDL7vEHI6VEXXLO-IoCl2EB0OkoCJcahiGB7jBV9jiS26RTQd5NVxIV4Y0x4Ni9MqxbmzOnzdVBAEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140729" target="_blank">📅 01:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140728">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyxsOkh9KMJo0xB63twwUwaJpzsAmeZHpshDGgkc_c2L6lxR6kuIvTg8pjUo36fAgkezB401zbCMr-Z5RjbhSXYQfRuoHC5yE8uu6NLF15KZGCWiy3NODCLYcYJaZAtMHx7shI5VemKemrzAlxLly_BsNVaWvVgpy0VeVaUIh2BH6jhLmj7qHV-_fdq-drCESH0pXIVY7WB5n5kOnJmsSLIofjFhl_0iBq9kOsXhWDAfhQamZSf1MYQdRD8gbQUs43f1hLSPC64U1K_9OxJTsAHWivOwN4Jrcp_jYIpLoyFNaMD3DK4QQrlNCIetAywrl0siuaTNVCLmfmrYo06a9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
در تاریخ بنوسید تو فوتبال‌‌فاسد ایران قرار بوده استقلال جام رو بگیره بجاش ٧۵٠ هزاردلار طلبش از مهدی‌تاج رو بلاعوض کنن‌‌. پشت‌پرده درحال انجام بوده اما مخالفت شدید باشگاه‌ها این معامله کثیف پول با جام بهم میخوره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140728" target="_blank">📅 00:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140727">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
#فوووووری
🖍
دانیال ایری به دلیل مصدومیت در تمرین امروز  سرخپوشان غایب بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140727" target="_blank">📅 00:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140726">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🏆
🏆
نتایج بازی های امشب:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140726" target="_blank">📅 00:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140725">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBJ1OQhGtJmcjdiIWqIfuMjOvTNc_dD7Ct9iaUWQk4lA2dsj4wsX5vHSQMugzr_31hZU07No8eTBW4dHfG9O7new5NEvJFpyCB0xlS4oUP5MrWTx8JeX1C-hH5Pvi-go-ghGTAbHdIs7Y2I-nsTYH3_pt87QuEvYsiO45oGfBBbmfijAjIHIRmHyXHACxXrSixEeQLzFSym08Fb3XyKq61ZE-B0sg6SB1O5JtuIGwJTmX8o3cszX0GohfAwSSpMsOvBg62dtLovrWkIFW8cqWPGG6tZW4DvNMDMpfFaGuEY0OdNrzc5S3UZVqPXcBGsRy53uPduEqo6e4UeXmoISbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏆
نتایج بازی های امشب:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140725" target="_blank">📅 00:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140724">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♨️
🤩
🤩
افشاگری باورنکردنی میثاقی از یک ایجنت، عارف آقاسی، پرسپولیس و پیش قرارداد برای یاسر آسانی!
🔄
🔄
محمدحسین‌میثاقی: پرسپولیس به یک ایجنت ۱۰۰ هزار دلار پول داده بود که عارف آقاسی را به پرسپولیس ببرد ولی این بازیکن را به استقلال برد و الان باشگاه از این ایجنت…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140724" target="_blank">📅 00:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140723">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNSbctMoWxrv9mr8-C6R-pMqWaLgCPdqzcdpRL3qrZzvqDAw2IlfKQWhXe5F2oiJ-P2kHJL3Os6UWqXcwcjSRL8N1lEKsvB9zprZJbEXcSfV6z7UyaPa-8jsD_EDryv4rZ-dsO88jqEUdmR8WmpAHBKewuXGJgOUTK4yfhvUtNCYEHuUDgnt7Rlhwtwn8m62LknW92g1dJCGeFrKW8k2vAStU-Q1fiuGuDsSdv8zXLyy4FCLTJ4bPEx9y6axt56ssfhx_EG6CRoqocE50MI1PoT4ipiV90wRolr3DZoYaF8irXcGaGGuSURn-YuwPHuErZJ4u-eYEdvZoezwTTRA5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🔻
مدت قرارداد احتمالی جدید نیازمند با پرسپولیس مشخص شد
⚪️
⚪️
پیام نیازمند گلر پرسپولیس که اخیرا مذاکراتش را با این باشگاه برای تمدید قرارداد آغاز کرده طبق شنیده ها به توافقات نسبی دست یافته. طبق شنیده‌ها قرارداد جدید نیازمند با پرسپولیس 2 ساله خواهد بود و گلر فعلی سرخپوشان قرار است دو فصل دیگر نیز در جمع پرسپولیسی‌ها باقی بماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140723" target="_blank">📅 23:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140722">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">📘
📘
در 14 بازی آخر تیم ملی با هدایت امیرخان فقط سه برد داشته که اونم مقابل گامبیا، تانزانیا و کره‌شمالی بوده
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140722" target="_blank">📅 23:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140721">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpnBD7H6LS9rG0aNW4jqXODM0NO-2DsQpopVr0YmCQH9TL_KkkqUBUV3XHnzD5oap75qS6gGTiNOGO3R8bZYyPE18sqUZVdPIxzdol81BnsR38AbFr04I6n-YN3bzvcJxynXlVV1IZfjVoQXwgMRA1gnIRJTyyZsfso9iiqQsMR5kFDQhxFMGyRpkqGOpge0xaeQtD96LkTO2qy9NPa1ujzrIXyzW7avNf11vbn40z0SL5nd55L1yPkbNDZsJYezEJkQ9Gn4O2jIGB5ovycrRD4_z7-v7DNaNGKXY0x_81uOP_cCUSq8incCRCUQpz0aIegaKpsMGGRG5z5gEegdHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
قرارداد ۱۳۶۵ میلیاردی پرسپولیس برای تبلیغات البسه
✔️
✔️
باشگاه پرسپولیس قراردادی به مبلغ ۱۳۶۵ میلیارد تومان برای تبلیغات بر روی البسه تیم‌های خود شامل بزرگسالان، رده‌های پایه و بانوان منعقد کرد.
✔️
✔️
این قرارداد برای فصل جاری جهت اطلاع عموم بر روی سایت کدال…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140721" target="_blank">📅 22:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140720">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bid4jAS4tX4dNjLN_XF8bJrXBJLUyexVCBxxaXE-kvki7pSdSgoWEa14BeVIsQzGJE_VqYbf5e66cAMs3JUhzPliOz9qerE4QwWxtSRkTbEw8S879-zaEdsC_mS3R6rkZUXP2YciWedY8wg3dZliGJmpvx1b-icZCZ0VP_Pv-YuSp-aCzmdKLbM7IP-_Pbz66IF3DP04EdjAB5uR2ArpTJxQI1ogbM26elMpRmPvKx92yzP0HuF8j4qMRYu9iIr9-DI-ovzF-Ha3QCOxX22FdhQj0HQPMjPc-8s__JkUPiQZB9Mo65JQW6DEeQUMf5qDbct5OSLqTNXrTzi0h-6BVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب اگه پیام نیازمند نبود، فاجعه بازی انگلیس تکرار میشد؛ تفاوت دروازبان درجه یک با دروازبان معمولی اینجور جاها معلوم میشه
❤️
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140720" target="_blank">📅 22:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140719">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
لباس پرسپولیس عوض می‌شود
⚡️
⚡️
باشگاه پرسپولیس برای فصل جدید رقابت‌های فوتبال، در آستانه تغییر برند تولیدکننده البسه خود قرار دارد.
⚡️
⚡️
⚡️
برند «یوسف جامه» در فرایند مربوط به انتخاب تولیدکننده البسه باشگاه پرسپولیس، توانسته نظر کمیسیون معاملات باشگاه را جلب…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140719" target="_blank">📅 22:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140718">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1880075a0d.mp4?token=Uskd9767iUa_2-sAF32-54Idhw5skVDDKolScG1AkioHqPxuejYh_Al-D3dKb-SU2r8XXAAq8T8NzLjEWA_gLchlIrTFz3GUhYcHxlH0Hy31vwJcu6uQ0JsGsFEoDmISgefrgAMCKRxu29l-klvabnE7UTmsIv935lb0I4C07DSuNSaRHK8NpnBlBk6W1crh6g5_zAzsHkytTPSTFYMlrzx_SA0xlXmdBP8nY_rnncLTUXXMVsN6xEYtRWtBry0HYya2uNM7EmaRsw6kZTQ8Yw0gt0vHlvarCdMXqsjw5FEP_KzToEyRy1FCipxGXNHT2uk2e5k7KpGFSsL2iyQZ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1880075a0d.mp4?token=Uskd9767iUa_2-sAF32-54Idhw5skVDDKolScG1AkioHqPxuejYh_Al-D3dKb-SU2r8XXAAq8T8NzLjEWA_gLchlIrTFz3GUhYcHxlH0Hy31vwJcu6uQ0JsGsFEoDmISgefrgAMCKRxu29l-klvabnE7UTmsIv935lb0I4C07DSuNSaRHK8NpnBlBk6W1crh6g5_zAzsHkytTPSTFYMlrzx_SA0xlXmdBP8nY_rnncLTUXXMVsN6xEYtRWtBry0HYya2uNM7EmaRsw6kZTQ8Yw0gt0vHlvarCdMXqsjw5FEP_KzToEyRy1FCipxGXNHT2uk2e5k7KpGFSsL2iyQZ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
درگیری شدید در بازی رده نوجوانان لیگ تهران میان تیم‌های کیسه و شاهین!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140718" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140717">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✔️
پرسپولیس هنوز هیچ توافق یا مذاکره‌ای با اندونگ انجام نداده/طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140717" target="_blank">📅 22:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140716">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
پایان  بازی روسیه 2 _ 0 ایران
✔️
✔️
یک نمایش ناامید کننده دیگر از تیم ملی/ با «مدل بازی متفاوت» هم باختیم!
❌
❌
در حالی که امیر قلعه‌نویی وعده داده بود تیم ملی با مدلی متفاوت برابر روسیه به میدان می‌رود اما نمایش تیم ملی همان همیشگی بود؛ نگران کننده و ناامید…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140716" target="_blank">📅 21:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140715">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66e4f7259.mp4?token=fi511Hy-gamme3VI0-LodSnVlJ8yaSk5dSi9Ch6nyv8kMweMxGxWzQlZf7_iN7jPUYhYp0Ah69xI05_vj0x5VW2EuLCFbchXOThcx5jzUBEAspcJlE9har1YzQDGs9hnrd5kHY1JrELhZ1nKYckeBC8xdmjskPniv4FsyrJvIzpth6mKePS4SuNV0suPcY5iJ1nDTgbwL8bhQws1X0OqaoADX_S9AskpvJGeK9SXP6nXWbxdjqmNGCx2GTqF8DCDsstiL7yGsJ9O1hW-YNUwrd7K1nQBEmfqa_GZzqZWnhfKm9-rT7aZPLq-ITZTtvW_lq6-I2YOU3v8ZE4BQ8sXvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66e4f7259.mp4?token=fi511Hy-gamme3VI0-LodSnVlJ8yaSk5dSi9Ch6nyv8kMweMxGxWzQlZf7_iN7jPUYhYp0Ah69xI05_vj0x5VW2EuLCFbchXOThcx5jzUBEAspcJlE9har1YzQDGs9hnrd5kHY1JrELhZ1nKYckeBC8xdmjskPniv4FsyrJvIzpth6mKePS4SuNV0suPcY5iJ1nDTgbwL8bhQws1X0OqaoADX_S9AskpvJGeK9SXP6nXWbxdjqmNGCx2GTqF8DCDsstiL7yGsJ9O1hW-YNUwrd7K1nQBEmfqa_GZzqZWnhfKm9-rT7aZPLq-ITZTtvW_lq6-I2YOU3v8ZE4BQ8sXvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📘
📘
در 14 بازی آخر تیم ملی با هدایت امیرخان فقط سه برد داشته که اونم مقابل گامبیا، تانزانیا و کره‌شمالی بوده
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140715" target="_blank">📅 21:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140714">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
✅
سومین سوپر سیو از پیام !!!
⬇
دمت گرم واقعا پیام جون
🔄
یه تنه جلوی آبروریزی رو گرفتی سلطان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/140714" target="_blank">📅 21:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140713">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYrPMKCecvHDKcYi7QEDDM91XeJ8uvXrZsJ3pjdRxyPS0wCGPLxpKy6qNMOvdZIcrwq0dirE8TNeNzGXhzuW2m5UR2drmgNhomF1PzdHmgjeSK65vtsDqH54gtcj3yhRVpflCf9qwtW2VRsmZVPRWw-ubLjftYZD8YVblyMaDjCXBUpdQkeukeH1Y-TbApMS46_alRgxgOhuISu8_blWOYZG_bC3HoTtajnfHukypYlbWoquzyT50yp5aIlGHunvb2PVbq8WpJvmm6PYtgUYCAo8mIa_MdZdWDRD66sOSqavEcqKed56_R4cYNDSWnGSHZ-rbSgnddj5OXoS_mCqHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
🔄
تصاویری از تمرین امروز تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140713" target="_blank">📅 21:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140712">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
✅
آقای قلعه نوعی با ی خداحافظی کل ایران و خوشحال کن .....سومین گل هم از ازبکستان خوردیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140712" target="_blank">📅 21:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140711">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
❌
با دعوت احسان حاج‌صفی به اردوی تیم ملی این بازیکن در صورتی که مقابل ازبکستان و روسیه حتی یک دقیقه بازی کنه رکورددار بازی با پیراهن ایران خواهد بود و از علی دایی و جواد نکونام عبور خواهد کرد
✔️
جواد نکونام ـ 149 بازی ملی
✔️
علی دایی - 148 بازی ملی
✔️
احسان…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140711" target="_blank">📅 20:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140710">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⭕️
⭕️
⭕️
خبرورزشی: مرغ حدادی یه پا داره بردن شکایت آسانی به Cas همین و تمام
⭕️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140710" target="_blank">📅 20:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140709">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
کنعانی و علیپور به دیدار مقابل صنعت نفت نخواهند رسید/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140709" target="_blank">📅 20:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140708">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
✅
آقای قلعه نوعی با ی خداحافظی کل ایران و خوشحال کن .....سومین گل هم از ازبکستان خوردیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140708" target="_blank">📅 20:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140707">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41fa93705.mp4?token=bJwuQChS4S_WU0-2sL84-K4O3xCcLi0qoaCauDeBve93rOY3JgH_4F44I4xkKOUf7RDnzM0i1ASiDUZB5wliOm30sfWONn5Q0lU6IFIJZTY8suPP5l6DDcnbV_oFmHovTgEqxKV9fhd22a1gWMU4VGaSGYSyMtXGMlb9j94nDu_hBW_YNzyUxPPK2yKtMPo4tS-KsKnyvYiBUP7NmQleReitbbNoQcuGeb9WEAu3S0jXop9o3a2nSW7lAp9Aprr1HfyEXGBQTmmmrksD1ER0bbHCfbVBnXU3QSeYy7nWkU3wxHxOd2y81XEs_pDBPWZpDBO5ymmHg4NNHZwqNA0N_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41fa93705.mp4?token=bJwuQChS4S_WU0-2sL84-K4O3xCcLi0qoaCauDeBve93rOY3JgH_4F44I4xkKOUf7RDnzM0i1ASiDUZB5wliOm30sfWONn5Q0lU6IFIJZTY8suPP5l6DDcnbV_oFmHovTgEqxKV9fhd22a1gWMU4VGaSGYSyMtXGMlb9j94nDu_hBW_YNzyUxPPK2yKtMPo4tS-KsKnyvYiBUP7NmQleReitbbNoQcuGeb9WEAu3S0jXop9o3a2nSW7lAp9Aprr1HfyEXGBQTmmmrksD1ER0bbHCfbVBnXU3QSeYy7nWkU3wxHxOd2y81XEs_pDBPWZpDBO5ymmHg4NNHZwqNA0N_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇷🇺
گل دوم روسیه به ایران توسط گلوین در دقیقه ۳۵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140707" target="_blank">📅 20:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140706">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQVgZ--uc0CxKnN7k_ZVFAF6H7jrnwdwhHU2vD35neqOyRDVFKm76WaYhM9Fi7O1T1Z4S7gAxHIMK3UBcXof6zAXtsmhrmnoLBj2jilGpJZCY4-YdVtsq8NXcwGqMcV3fS5eUsORARW3hbPcwLoCUeBf1GrndShG05JXKrTURekGyyd0dOVgN8tCF6bWLP4LVEICNi_aVAD1HJnAIfrEFgdzKdmxrNDV5R3WqQrQPDwSwS3k9t0VSqEPGV78A0E0WyoYpVcLdLd2JbFGP00YIMwto3sDojpcDfYnfuMMBp4KWduDqEL2OIRr7MBef46SnOrk5ZmIfuUoIFFwtLKlPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد ماتادورها و شطرنجی‌ها امشب در یک دوئل تماشایی!
🔥
⚡️
[
اسپانیا
🇪🇸
🆚
🇭🇷
کرواسی
]
⚽️
اسپانیا بعد از برد ۳-۲ مقابل انگلیس با ۵ برد متوالی وارد این بازی شده و در ۶ تقابل اخیرش با کرواسی ۴ برد داشته است. کرواسی هم در بازی اول ۲-۱ چک را برده، اما مقابل مالکیت و پرس اسپانیا احتمالاً بیشتر به انتقال سریع و ضدحمله تکیه می‌کند. باتوجه به روند دو تیم، سناریوی بازی نزدیک اما پرموقعیت محتمل است؛ اسپانیا از نظر خلق موقعیت دست بالاتر را دارد و یامال می‌تواند مهره کلیدی باشد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140706" target="_blank">📅 20:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140705">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
تعویض زودهنگام محبی، به دلیل مصدومیت که احسان حاج صفی جای او را می‌گیرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140705" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140704">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be44fa519.mp4?token=Wl4dGaWRqOoAgTVEzTWvWMzdUejsrKRc836VoaC0s-RTQR2yIAPJrk0BVnQy5eL2tK5cDKpvdlgJmEoa2f-dGtw_51qiUp2w2iy_3cecvP13LK4WzG_NgJRvSnBKGcRXMpGH93dLM-swQUM7XBlxf4hjO1A5HwIlaC8v4lcrpNMKvKkzUhk67bzlkEnVd33_7AVuKN5X7xKd1irmWYvstH-x0ghRk1MOu9szuBLdErB5r7bCyVzo4ascmLCt52KEnCcuc9tS8g-DSLwEQwVC_3X2omOQtBFi0yGlJmiP_RaiSbACntawcQZhJWnauq82wIUDkXrPaDZ1f6GRZPmrkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be44fa519.mp4?token=Wl4dGaWRqOoAgTVEzTWvWMzdUejsrKRc836VoaC0s-RTQR2yIAPJrk0BVnQy5eL2tK5cDKpvdlgJmEoa2f-dGtw_51qiUp2w2iy_3cecvP13LK4WzG_NgJRvSnBKGcRXMpGH93dLM-swQUM7XBlxf4hjO1A5HwIlaC8v4lcrpNMKvKkzUhk67bzlkEnVd33_7AVuKN5X7xKd1irmWYvstH-x0ghRk1MOu9szuBLdErB5r7bCyVzo4ascmLCt52KEnCcuc9tS8g-DSLwEQwVC_3X2omOQtBFi0yGlJmiP_RaiSbACntawcQZhJWnauq82wIUDkXrPaDZ1f6GRZPmrkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تعویض زودهنگام محبی، به دلیل مصدومیت که احسان حاج صفی جای او را می‌گیرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140704" target="_blank">📅 20:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140703">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
تیم قلعه‌نویی گل اول از روسیه هم خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140703" target="_blank">📅 20:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140702">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a7b7886c.mp4?token=L2-eHCTjmMgaKd4wv_Wyj0bn9JsYduJnXDlN1uwhye3fn5AJ6m-gNF0S_7puZxMtcpAd6NTthlECA-edHwKoDLiUtiL2JO15yjgsZFG_eMbtcLdsXikU4cLJxJ-y4CySO40jVscsyf9mKV_xz4gtSgptAWZbJcCoA0Bv9r9igAxdqJ4zyQ6oafWZ-GVxV0U-G_vnGsBGTiUNlfAGbdXZqysQLHnV7S4YJWzFnrD5BfHUX_pfDUGrhrpU7uFudJjN2guoFD5DULIM1G1X_WxLqLR3SSftCQO9At6E4S-sRMCj0pHl44AG9Bue8tFyjXwIzZgNVNHzcn5f8iGFHkKwbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a7b7886c.mp4?token=L2-eHCTjmMgaKd4wv_Wyj0bn9JsYduJnXDlN1uwhye3fn5AJ6m-gNF0S_7puZxMtcpAd6NTthlECA-edHwKoDLiUtiL2JO15yjgsZFG_eMbtcLdsXikU4cLJxJ-y4CySO40jVscsyf9mKV_xz4gtSgptAWZbJcCoA0Bv9r9igAxdqJ4zyQ6oafWZ-GVxV0U-G_vnGsBGTiUNlfAGbdXZqysQLHnV7S4YJWzFnrD5BfHUX_pfDUGrhrpU7uFudJjN2guoFD5DULIM1G1X_WxLqLR3SSftCQO9At6E4S-sRMCj0pHl44AG9Bue8tFyjXwIzZgNVNHzcn5f8iGFHkKwbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تیم قلعه‌نویی گل اول از روسیه هم خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140702" target="_blank">📅 20:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140701">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
✔️
غایبان پرسپولیس در دیدار دوستانه امروز
⏺
حسین کنعانی، علیپور، عمری، ابوالفضل جلالی و حسین ابرقویی، باکیچ، ارونوف، نیازمند، زارع، محبی، محمودی، ایری، لطیفی فر و شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140701" target="_blank">📅 19:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140700">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
همه هواداران پرسپولیس از مدیران باشگاه عاجزانه تقاضا دارن تا ماجرای یاسر آسانی رو تا ته تهش پیش برن.
🔺
آخرش اینه که یه پولی میخواییم بدیم و رای هم صادر نشه به نفعمون، این همه پرونده بوده که هزینه کردیم و باختیم، اینم روش
🔺
دقیقا از روزی که فهمیدن…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140700" target="_blank">📅 19:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140699">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01dc83e8df.mp4?token=vnKR3ZPw4BeSbfsyT5Dui2jbEExkVEwaxGD_ag6i1ha0Pk6mi9JDE3WL_P1EIM0SRTGLzgqce5KN51RDmoRyP02GJPDZlVvEk7TzZ6wm1_EGx6Lf-C-W-2B65vx1hk2FgpvJQRxaG1VU72JTSKeJRfZ1PvG0WRXhJs3mlDTpONI_XbGlSOetL7G90qdTxEwO2BFoPwMcTo_KLuLKl0r_XQBFFkeWfFHmhNrRlIAFzz2AXR-vI1lD58k6tKfqP_PDTKEWrg0pYEBzAzF1R7dKm0JhQkjMahI6zixiQGRD-YmPVgqo_SW9kAX-0jG2qYM1EJ6GAvphVgcJmtcAzNSgHSVnBQm-bvX6Gvmyl8fOVuvET5MVr93qsRcE7DwzrYKqf2e7yc4eK4UyqTAj7ZeckFVLuHbojNScUcoehkh_jyraPBnU2Z2LPJaXiMd_zchtsHVg6LY-z859gWEBOZUtSzpF8dPWTlzBcvNKLAX1KIiFfI3GmHIQbgrpjz4sQYPdCvxQlGLRk3O2N9F23l5LRK8RhrF9mp3imra-siwYFtyfOYzMbU7Jyqee3TZVxNV2Q4GRimhXbR-0jGyI0G_xlxL-jwBV1h5WW5yBVnbb4DEd4CE3eKver36IEelwPRBXBKKRrZ9Ol7UO0KQnKjMnpD2XmClr1g0hBju4BA5gq98" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01dc83e8df.mp4?token=vnKR3ZPw4BeSbfsyT5Dui2jbEExkVEwaxGD_ag6i1ha0Pk6mi9JDE3WL_P1EIM0SRTGLzgqce5KN51RDmoRyP02GJPDZlVvEk7TzZ6wm1_EGx6Lf-C-W-2B65vx1hk2FgpvJQRxaG1VU72JTSKeJRfZ1PvG0WRXhJs3mlDTpONI_XbGlSOetL7G90qdTxEwO2BFoPwMcTo_KLuLKl0r_XQBFFkeWfFHmhNrRlIAFzz2AXR-vI1lD58k6tKfqP_PDTKEWrg0pYEBzAzF1R7dKm0JhQkjMahI6zixiQGRD-YmPVgqo_SW9kAX-0jG2qYM1EJ6GAvphVgcJmtcAzNSgHSVnBQm-bvX6Gvmyl8fOVuvET5MVr93qsRcE7DwzrYKqf2e7yc4eK4UyqTAj7ZeckFVLuHbojNScUcoehkh_jyraPBnU2Z2LPJaXiMd_zchtsHVg6LY-z859gWEBOZUtSzpF8dPWTlzBcvNKLAX1KIiFfI3GmHIQbgrpjz4sQYPdCvxQlGLRk3O2N9F23l5LRK8RhrF9mp3imra-siwYFtyfOYzMbU7Jyqee3TZVxNV2Q4GRimhXbR-0jGyI0G_xlxL-jwBV1h5WW5yBVnbb4DEd4CE3eKver36IEelwPRBXBKKRrZ9Ol7UO0KQnKjMnpD2XmClr1g0hBju4BA5gq98" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◀️
🔴
حضور پیمان حدادی مدیرعامل باشگاه پرسپولیس در ایستگاه 88 خیابان پارک وی به مناسبت روز آتش نشان
🔴
مسئولان پرسپولیس در این دیدار ضمن خدا قوت به پرسنل این ایستگاه آتش نشانی با اهدای گل و یک پیراهن پرسپولیس از این قشر زحمت کش تقدیر کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140699" target="_blank">📅 18:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140698">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
ساعت بازی ایران و روسیه تغییر کرد
❌
❌
فدراسیون فوتبال روسیه از تغییر زمان آغاز دیدار دوستانه تیم ملی این کشور برابر ایران خبر داد.
❌
❌
تیم ملی فوتبال روسیه به هدایت والری کارپین، روز ۲۹ سپتامبر (۷ مهر) در شهر کازان به مصاف ایران خواهد رفت. سوت آغاز این مسابقه…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140698" target="_blank">📅 18:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140697">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
🔴
🔴
رسمی/ صنعت‌نفت برابر مس پیروز اعلام شد
🔄
🔄
کمیته انضباطی فدراسیون فوتبال در پی عدم حضور تیم مس رفسنجان در دیدار پلی‌آف مقابل صنعت نفت آبادان، نتیجه بازی را ۳ بر صفر به سود صنعت نفت اعلام کرد. با این حکم، صنعت نفت به لیگ برتر صعود و مس رفسنجان به دسته پایین‌تر…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140697" target="_blank">📅 16:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140696">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‼️
😳
⚽️
بیرانوند: سربازی من نهایت ۵ماه است!
❌
فجرسپاسی؟ شاید اصلا به تیم نظامی نروم/ کل سربازی من با کسری‌ها 5 ماه است؛ در همان تبریز به پادگان می‌روم و با تراکتور هم تمرین می‌کنم!
🚫
❗️
۲۱ ماه خدمت چطوری و با چه کسری‌هایی یهویی شد ۵ ماه؟ بجز تاهل و ۲ فرزند و راه…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140696" target="_blank">📅 15:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140695">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_G8ttphmS3rZLh7x6yTOQNe5DCp5ixDZtW1wiuns3bjMsPAFlv_CNLyLZTV-hnVYiF3w-TRd3LsmT-hAcPdm98W0qb52bt1w4_S7-DAUNbBCwEobDTO0DXeckfmBti3YcNOwBVC0BNMpySlPCegxc8pp8ZNq2kZZ3pCbgQa-xGkQsrh3RAfZ-wRJH62eIYMn62RpPiKAr3mYQlbhqvnGgH_jSs4HBaHbVoRgUovK8aR4SVYBs1BzQQHyZwriTUClCDFRLmx_PitYM6iR-rEoZ-Yrhj4DHrEC9eh7PDUontIfG9SNt4DHRbhGYPlHQyJjGQqiW2BXf1zHO-QQy2H6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری | رسما شرعا جام قهرمانی به کیسه اهدا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140695" target="_blank">📅 15:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140694">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
افشین قطبی، رسول خطیبی و پیروز قربانی به عنوان سه گزینه نهایی سرمربیگری تیم ملی امید انتخاب شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140694" target="_blank">📅 14:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140693">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
❌
علوی سخنگوی فدراسیون: تراکتور، سپاهان و پرسپولیس پیشنهاد دادن جام قهرمانی فصل گذشته به شهدای میناب اهدا بشه‌ و فردا تصمیم فدراسیون در این مورد مشخص میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140693" target="_blank">📅 14:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140692">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🟥
دانیال اسماعیلی فر از تعویض ناراحت شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140692" target="_blank">📅 12:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140691">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
تیکدری بازیکن پرسپولیس: مهدی تارتار یک مربی بی نظیر است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140691" target="_blank">📅 12:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140690">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
❌
تیم ملی والیبال کشورمان با شکست ۳ بر صفر مقابل ژاپن نایب قهرمان آسیا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140690" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140689">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZ6HNvFJZX4IkXgmlyDpq-0TpbDuZsM-tMFdLufwAINTGAkYm9NE2GbhFHawwaD0W2IoDYXdXyTBen79EKKg-wj8brCuKoI7GWK0sAPNlwi-RBVfp750ZrxOAjEcb1fDzzphWrDeG9MMn6qNQNEuH617sDthtbDl_I3OuFwPAL0pjL-tWQNBhDX5LSpvC8FP4u2FMrsWSgXQP_FriZzoKoCBscUAosN3PMLiDeByjZjWrjebrNZFz-UNhDx6HlUAzOt8RU1yLuLjNua2VN6UOzvP1VQYAQE4uP6_bS2YG2Uz7ihcOgfJQqrROLWyfxZmL0HoWLzxdtpy3IdNSGFrgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
Spain -
❤️
Croatia
⏰
Tonight 22:15
🏟
Ramón Sánchez Pizjuán
⚽️
اسپانیا با ۵ برد متوالی و بدون شکست در ۳۹ بازی اخیر وارد این مسابقه خواهد شد؛ کرواسی هم در بازی نخست ۲ - ۱ چک را برده است. در ۱۱ تقابل قبلی، اسپانیا ۷ برد، ۱ مساوی و ۳ شکست داشته و آخرین بازی دو تیم را هم ۳ - ۰ برده است. مدل آماری پیش‌بینی، شانس برد اسپانیا را ۶۱.۷٪ و کرواسی را ۱۸.۶٪ برآورد کرده و احتمال زیر ۲.۵ گل را ۶۶.۹٪ می‌داند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140689" target="_blank">📅 12:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140688">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
علوی سخنگوی فدراسیون: تراکتور، سپاهان و پرسپولیس پیشنهاد دادن جام قهرمانی فصل گذشته به شهدای میناب اهدا بشه‌ و فردا تصمیم فدراسیون در این مورد مشخص میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140688" target="_blank">📅 11:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140686">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9d2810e6e.mp4?token=g2skGok6KgEXqdZLVfQrzHqT_WYV-0UpZjiEpaa8t7pSeZSOBOBxNl7bAXl5mEv2FNvWnzjBsxJakOal25bVWqn8ODGsNWYLGK4_Pmm2stCi4i_Fjz0nKLn0R2_XIfX_CLzfX6wuQ8hurtAVb7DDjogbUvpW4UZYk5zGcAdo8unkaN5sY2dk15NHw3Pl2kyxi2ArD7YVnMVT0AzJzg8ZZdhhdOIjH5hbFmPaMErstWDKp40GZ8sz70X9Je9GygtCojptiNr2zPMOm86z3dMCRFbwuiDEvx2QK3uJZRYOHylvGoeGlEAi1rF6712XpuIf-RgNffU4QM1P1M_owW2TGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9d2810e6e.mp4?token=g2skGok6KgEXqdZLVfQrzHqT_WYV-0UpZjiEpaa8t7pSeZSOBOBxNl7bAXl5mEv2FNvWnzjBsxJakOal25bVWqn8ODGsNWYLGK4_Pmm2stCi4i_Fjz0nKLn0R2_XIfX_CLzfX6wuQ8hurtAVb7DDjogbUvpW4UZYk5zGcAdo8unkaN5sY2dk15NHw3Pl2kyxi2ArD7YVnMVT0AzJzg8ZZdhhdOIjH5hbFmPaMErstWDKp40GZ8sz70X9Je9GygtCojptiNr2zPMOm86z3dMCRFbwuiDEvx2QK3uJZRYOHylvGoeGlEAi1rF6712XpuIf-RgNffU4QM1P1M_owW2TGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😳
⚽️
بیرانوند: سربازی من نهایت ۵ماه است!
❌
فجرسپاسی؟ شاید اصلا به تیم نظامی نروم/ کل سربازی من با کسری‌ها 5 ماه است؛ در همان تبریز به پادگان می‌روم و با تراکتور هم تمرین می‌کنم!
🚫
❗️
۲۱ ماه خدمت چطوری و با چه کسری‌هایی یهویی شد ۵ ماه؟ بجز تاهل و ۲ فرزند و راه دور[سرجمع ۹ماه کسری]، چه سهمیه‌ای گرفت یهو؟
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140686" target="_blank">📅 10:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140685">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
یک شکایت جدید از استقلال؛ پیکان این بار از ماشاریپوف شکایت کرد
✔️
باشگاه پیکان مدعی است نام ماشاریپوف فصل گذشته از لیست استقلال خارج شده و با توجه بسته بودن پنجره نقل‌و‌انتقالاتی آبی‌پوشان، حضور مجدد این بازیکن در لیست بازی با خودروسازان غیر قانونی بوده…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140685" target="_blank">📅 10:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140684">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
❌
تا نیم‌فصل بیرانوند میتونه به‌ صورت کاملاً قانونی و بدون هیچ مشکلی برای تراکتور بازی کنه!/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140684" target="_blank">📅 10:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140683">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
فوووووووری از بیرانوند: چرا فکر میکنید سربازی نمیرم؟ 3 ماه معافیت تاهل دارم، 3 ماه فرزند اول، 3 ماه فرزند دوم و 3 ماه دوری راه تبریز تا خرم‌آباد و یعنی کلا حدود 6 ماه خدمت دارم؛ اصلا شاید نرم تیم نظامی برم پادگان تو تبریز و بالا برجک وایسم موقع مرخصیم میرم…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140683" target="_blank">📅 09:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140682">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
✔️
فوری و رسمی/ دلار 250 هزار تومان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140682" target="_blank">📅 09:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140681">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
✅
بازیکن پرسپولیس نیامده جدا شد
🔹
فرزین معامله‌گری که از تیم شمس‌آذر به پرسپولیس پیوسته بود، با توجه به مشمولیت، برای گذراندن خدمت سربازی راهی ملوان بندرانزلی شد.
⏺
پس از پایان دوران خدمت سربازی، وضعیت ادامه همکاری او با سرخپوشان مشخص خواهد شد.  «سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/140681" target="_blank">📅 09:22 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
