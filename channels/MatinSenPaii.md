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
<img src="https://cdn1.telesco.pe/file/tRkviYgkwrtR9If8g5A1mOa2Sd0lQfKUtE3hTOViNefLZ_nfYqlqdqbhxw7TcDUtoOw7QAE9ZxiG5KE1g6hDzS30jV3zwkoFgfap2wPOp3vCHcFsokiupFB6d-L3YlGLOm74pv8pgCp91YfYNQpHZV1BQfd96xMuYGJIuN5EZHp8TWiRL_wZcw3IUCu2DqqCsiT8Nx90uUiXutXRH71U3YFNScd3SSTDuwNp86DFVThE9Mm6iZFfppToM9aRwaJMvS3NevbCoX4uOLEzwGkdvTadSLplplR0fWYEPGo211GadcGctA8FJ0v6d-qQYtLJYN2s-GAHzqQNP4bnQMj9-Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 17:51:40</div>
<hr>

<div class="tg-post" id="msg-3473">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فایل Json جدید برای Spoof:
{
"LISTEN_HOST": "0.0.0.0",
"LISTEN_PORT": 40443,
"CONNECT_IP": "172.67.139.236",
"CONNECT_PORT": 443,
"FAKE_SNI": "security.vercel.com"
}
برای من روی مخابرات اوکیه</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/3473" target="_blank">📅 16:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3472">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آموزش ساخت کانفیگ BPB شخصی:
https://t.me/MatinSenPaii/3443
آموزش  Sni-Spoof هم این:
https://t.me/MatinSenPaii/3186</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/3472" target="_blank">📅 16:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3471">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pcrknjVanFzNDGZVUr9iBtlmH8abXZ2mv_JHU-Wn2CUfPUy3OmqmTRHRrmVbfyLqCN2DwVcxkx-yA1DYTybXavzaj587tFJ4SgwhE6FV5IZfys5WC0Lsn6J7bEjUyH3qFsn-In6V1wP5LIsYlonhEK6Dm23c26Roj5_EAgSoIMhTGI_ziaRkdjMYUz8Jc5qD_S4P70DCLR8O_5boJsnxNlGziC-YyCZXDMR7xEWWuKcxwJgP0l0fChTnVn7khP7uBSmy2XGm5LqOKvVLGRgI562uIxiAIREJr3SD4IcyUSxqiUWfNh71FjbVD_Fl0-KEifxF0GwzijlH850Y6I-v4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت سرعت آپلود روی CDN و Worker Cloudflare</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/3471" target="_blank">📅 16:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3470">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/paCEZ6qc8O0l_EXB2D4-PZLLY9rFebyybauQ7xNpqrDiJDSnOgmnq2oSkYt2URYGG1_WHiEpAwG2HIVJJY0SaF4eX_M_Hip4PnENIQNLax2-DGdDV8J3cgzUSbBVbuEmwNViCS9HCxVD809o_36aE9xQ73PYHCZx-SjEzlXE4mCMD4O6yYvig0y0JYrn0g-aUf9BArlGbeQzDJTUUYq7VdkO30PoigSgQ-i_SD1n8CItmFSGvOxm_mMHjZMuEjEhudD2edWdY4CPUvONc8fdSAUwE6nsPNrvrZ_MTmlmbj-XnQOskX3mlfnBZWYYyITBrF0XOfZEVCSm3ds6BCz4HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت سرعت آپلود روی CDN و Worker Cloudflare</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/3470" target="_blank">📅 16:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3469">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kg32tIKe0VtS2xlxR0YBEMXRJyNfRPrdjWi6K1J4RjaQKifMswqxtDJSiKIKc9FZBgJsFlDISHCS3ETseVzdtoA6JEFTT2SxztwaiCg3dXDd3yzj6bkXjBdtuGGxLNUBXcmfLh0-8t6NJiw8BgjjFja1DEZrWk63cqWj3HlDvYl9Hq5DlH699WUhFdkvrIBniuW9DriYihafGoIIVyxV2NLHJZ7r3veQWSW_q6rV3aU23rahsx-8dUlfNkdflG7Fg7pMgDjODhvOYPJSVhZfrCFCwmxEnLBJZ7ErDIs3AfCgMAHKwe-moWYbDd_gkMim078XjRtQ-wsyCsP_yZHT_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از اهداف من اینه که آموزش‌هایی بذارم طی چندوقت آینده، (هرچند قبلا هم گذاشتم) که شما رو بی‌نیاز کنه از خرید هرگونه کانفیگ. و هرشخص بتونه برای خودش و خانواده‌اش به راحتی فیلترشکن شخصی راه بندازه. منتها اگر فعلا نیاز دارید به لوکیشن و یا سرعت و... ، می‌تونید بگیرید</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/MatinSenPaii/3469" target="_blank">📅 12:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3468">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بزرگترین نجات‌دهنده‌ی ما، WhiteDNS و MasterDNS هستش که از واجباته برای خودتون ستاپ کنید! توی کل این 80 روز می‌شد باهاش وصل شد. آموزشش رو هم ضبط کردم طولانیه اما حوصله کنید و ببینید:
youtu.be/6Pm7kNQb3mo
‎</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/MatinSenPaii/3468" target="_blank">📅 10:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3467">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">💭
چرا زمانی که اینترنت را قطع می‌کنند، درجا این کار را انجام می‌دهند اما وقتی نوبت به باز کردن می‌رسند، انقدر قطره‌چکانی این کار انجام می‌شود؟
1-
جنبه فنی
(دلیل اصلی تفاوت سرعت قطع و وصل):
🌐
ایران اینترنت را از طریق چند gateway بین‌المللی محدود (عمدتاً تحت کنترل شرکت ارتباطات زیرساخت - TCI و ASهای اصلی مثل AS49666) به جهان متصل می‌کند. این ساختار متمرکز است:
"قطع کردن آسان است"!
کافی است BGP announcements (اعلام مسیرهای روتینگ) را withdraw کنند، یا ترافیک را در gatewayها بلاک کنند، یا IPv6/IPv4 را محدود کنند.
با دستور مرکزی، همه‌ی ISPها (مخابرات، ایرانسل و ...) در چند دقیقه یا چند ساعت، آفلاین می‌شوند. مثل کلید kill switch.
وصل کردن سخت و زمان‌بر است:
وقتی همه چیز را قطع می‌کنند، فیلترینگ، routing tables، DNSها، و سیستم‌های DPI (Deep Packet Inspection) و SNI filtering در لایه‌های مختلف (gateway، ISPها، IXP) به هم می‌ریزد.
برای برگرداندن، باید تدریجی تست کنند:
اول routing را باز کنند، سپس DNS resolution را درست کنند، بعد فیلترینگ را لایه به لایه اعمال کنند تا "نشتی" (leak) اینترنت آزاد رخ ندهد.
هر تغییری ممکن است باعث باز شدن ناخواسته سایت‌ها/اپ‌ها شود، پس مرحله به مرحله روی ISPهای مختلف و مناطق تست می‌کنند. این کار ساعت‌ها تا روزها طول می‌کشد.
در قطعی(و سپس وصلی)‌های اخیر (مثل جنگ دوازده روزه یا دی‌ماه) هم دقیقاً همین الگو دیده شده.
2-
جنبه سیاسی-امنیتی
:
💬
قطع: تصمیم سریع از شورای عالی امنیت ملی یا نهادهای امنیتی گرفته می‌شود (برای کنترل اعتراضات، جلوگیری از هماهنگی یا جاسوسی سایبری و هر مزخرف دیگه‌ای).
وصل: نیاز به هماهنگی بین نهادهای مختلف (وزارت ارتباطات، سپاه/اطلاعات، شورای فضای مجازی) دارد. گاهی اختلاف میان این نهادها در بازگشایی یا نوع آن، باعث تأخیر می‌شود. آن‌ها نمی‌خواهند ناگهان همه چیز باز شود چون کنترل را از دست می‌دهند. پس "تدریجی و با احتیاط" اینترنت را باز می‌کنند تا فیلترینگ جدید را تثبیت کنند.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/MatinSenPaii/3467" target="_blank">📅 10:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3466">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2Ray Proxies with Khosrow</strong></div>
<div class="tg-text">کانفیگای توی
لینک سابسکریپشن
رو چک کنین. کار میکنن براتون احتمالا.</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/MatinSenPaii/3466" target="_blank">📅 01:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3465">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اسکمرها و کانفیگ‌فروش‌های دزد و گرون‌فروش، هم‌اکنون:</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/MatinSenPaii/3465" target="_blank">📅 23:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3464">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-text">حقی که نصف و نیمه بهمون داده بودن و با فیلتر رو ازمون کامل گرفتن، بعد ۸۰ روز هم پسش دادن، به همون حالت نصف و نیمه.
شرمنده اگه یک درصد هم باعث خوشحالی من نشده این وصل شدنه. هیچی تغییر نکرده.</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/MatinSenPaii/3464" target="_blank">📅 22:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3463">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سرعت آپلود شما هم پشت worker و کلا کلودفلر پایینه بچه‌ها؟</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/MatinSenPaii/3463" target="_blank">📅 21:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3462">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⚡
cfray v1.1
یه ابزار تک‌فایلی پایتونی که همه چیز رو برای مدیریت کانفیگ‌های VLESS و V2ray پشت Cloudflare یکجا جمع کرده.</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/MatinSenPaii/3462" target="_blank">📅 21:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3461">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اینترنت برگشت، و خوشحالم که توی این مدت تونستم کنارتون باشم و توی اتصالتون به اینترنت آزاد راهنماییتون کنم
❤️
همونطور که همیشه گفتم، زحمت اصلی رو برنامه‌نویس‌های عزیز کشیدن. افرادی از جمله پترنیها با sni spoof، امین محمودی با MHR و MasterDNS، aleskxyz با پروژه‌های خفنش، iampedi و تیم خوبمون با اپ WhiteDNS، سارتو با پروژه TheFeed، سم، مارک، Samim با پروژه شیر و خورشید، و همینطور بچه‌های کامیونیتی زیرزمینی Vasl، عزیزی، امیرپارسا، ریتالین، GuardNet و... که اسم‌هاشون بی‌شماره.
می‌خوام بدونید که خیلی از افراد پشت من بودن تا بتونم آموزش‌ها رو به دستتون برسونم. و اسم خیلی‌هاشون رو نمی‌تونم ببرم. از اون عزیزی که به من صد گیگ کانفیگ داد گرفته، تا بچه‌هایی که قبل از آموزش‌ها باهاشون مشورت می‌کردم تا اشتباهی نداشته باشم و همه‌چیز بی‌نقص باشه.
همینطور از افرادی که به من دونیت کردن و من تونستم کیبورد و موس بگیرم که وضعیت بدنیم بیشتر از این اذیتم نکنه، و راحتتر بتونم تایم بیشتری رو پشت سیستم باشم.
صمیمانه از همه‌تون ممنونم
❤️
ما همه بدون چشم‌داشت کار کردیم. و هیچ منتی سر شما نیست و شما هیچ چیزی به ما مدیون نیستید.
و ما کسایی هستیم که امثال سگارو، یوسف قبادی، IRCF، وحید فرید، یـ‌بـ‌خـ و... رو دیدیم و قدم برداشتیم توی این مسیر.
هفته‌هایی بود که چند روز پشت سر هم نمی‌خوابیدیم، با درد مچ دست و کمر و چشم و تونل کارپال و وضعیت جسمانی افتضاح خیلی‌هامون ادامه دادیم؛
فقط و فقط چون به آزادی باور داشتیم.
زنده باد ایران</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/MatinSenPaii/3461" target="_blank">📅 21:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3460">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تا فردا-پس‌فردا به احتمال زیاد روی همه‌ی اپراتورها کلودفلر رو باز میکنن. و منطقه‌ایه مثلا اینجا حتی ایرانسل هم قطعه هنوز</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/MatinSenPaii/3460" target="_blank">📅 20:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3459">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تا فردا-پس‌فردا به احتمال زیاد روی همه‌ی اپراتورها کلودفلر رو باز میکنن. و منطقه‌ایه
مثلا اینجا حتی ایرانسل هم قطعه هنوز</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/MatinSenPaii/3459" target="_blank">📅 18:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3458">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دوستانی که همراه اول و شاتل و زیتل دارن، حالا حالاها باید بشینن تا وصل بشن</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/MatinSenPaii/3458" target="_blank">📅 17:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3457">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmin Mahmoudi</strong></div>
<div class="tg-text">نقطه قشنگ ماجرا خارج شدن این موضوعات حتی از ایران بود، این افتخارش رو هممون بدست آوردیم، هرکسی به نحوی کمک کرد.
یکی روی توسعه کمک کرد.
یکی با ساخت ویدیو کمک کرد.
یکی با توییت زدن و معرفی توی کانالش.
یکی با استار دادن.
دوستان برای پروژه ها نرم افزار اندروید ساختن و ....
همه باهم کنار هم باعث شدیم پروژه ها خفن بشن.
همه با هم کاری کردیم که پروژه مثلا MasterDnsVPN، چندین روز بهترین پروژه زبان GO توی گیت هاب باشه.
همه با هم کاری کردیم همین پروژه 2 روز توی ترند گیت هاب باشه و اینا همشون خیلی خفنه.
توی پروژه ی MasterHttpRelayVPN، هم همه باز همین کمک هارو کردن و موفقیت های خوبی بدست آوردن.
همه با هم این کار رو کردیم، کار یک نفر نیست.
این مدت جدا از بد بودن و سختی ها، همه با هم افتخاراتی رو بدست آوردیم ...
که همه با هم باید به هم خسته نباشید بگیم
❤️
درکل همگی خسته نباشید.
امیدوارم این روز ها دیگه تکرار نشه ....
همگی عشقید و خسته نباشید، دم همگی هم گرم
❤️</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/MatinSenPaii/3457" target="_blank">📅 17:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3456">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اسکمرها و کانفیگ‌فروش‌های دزد و گرون‌فروش، هم‌اکنون:</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/MatinSenPaii/3456" target="_blank">📅 17:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3455">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/18fbc73a71.webm?token=qwUscnUTIEtTLicQeQ98VAm7vf_lXkAvM8U0bGuJtdWg4iM4-wUSEkoBjx7Mj_vYKk6QfNEel8nZ9KJgoMpsKD6XTCPfMaudrJ8633kbruAKAUJSZMCwiUqBJDPgOpWS_8BmDasO2evGnFQDyPuCFPc5KTVnKOy4I_NTSFXkSE1JYouxIBWQVWG2keNp_jPpYjhUUrkKOOAg2cyOhIy8hV7JeVk18FFfT4aG2ZFnJYjCzizaiDhDK4NL0ograwB_eM827myMbnNKm48iEYOhlDFOUfct3sLU0RKn3S7GL4eB0F71vZ6F_RRQ90eUiyg5fNJgBjjozPy7yNdC_Spg9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/18fbc73a71.webm?token=qwUscnUTIEtTLicQeQ98VAm7vf_lXkAvM8U0bGuJtdWg4iM4-wUSEkoBjx7Mj_vYKk6QfNEel8nZ9KJgoMpsKD6XTCPfMaudrJ8633kbruAKAUJSZMCwiUqBJDPgOpWS_8BmDasO2evGnFQDyPuCFPc5KTVnKOy4I_NTSFXkSE1JYouxIBWQVWG2keNp_jPpYjhUUrkKOOAg2cyOhIy8hV7JeVk18FFfT4aG2ZFnJYjCzizaiDhDK4NL0ograwB_eM827myMbnNKm48iEYOhlDFOUfct3sLU0RKn3S7GL4eB0F71vZ6F_RRQ90eUiyg5fNJgBjjozPy7yNdC_Spg9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/MatinSenPaii/3455" target="_blank">📅 17:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3454">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نت خونگی اوکیه
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.21.7.21:2096?encryption=none&security=tls&sni=sni.111000.indevs.in&insecure=1&allowInsecure=1&type=ws&host=sni.111000.indevs.in&path=%2F#Humanity%202</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/MatinSenPaii/3454" target="_blank">📅 16:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3453">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">قربون دستت حالا که دستور دادی اینترنت باز شه
یه دستور هم بده اونایی که کارشون رو از دست دادن برگردن سرکارشون
یه دستور بده اونایی که زندگیشون از هم پاشید برگردن سر خونه زندگیشون
یه دستور بده اونایی که سر اجاره خونه خونشون رو تخلیه کردن برگردن خونشون
اینترنت شاید برای شما یه دکمه روشن و خاموش باشه، ولی برای خیلیا نیست واینترنت زندگیشونه که با دکمه خاموش و روشن به حالت قبلی برنمی‌گرده.
✍️
Reza Jafari</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/MatinSenPaii/3453" target="_blank">📅 16:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3452">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🍷
بازگشت همه به سوی سایفون + v2ray هست چند تا جدید که گفته بودم میزارم استفاده کنید ip جدیدا رو
✅
141.193.213.11
104.18.38.202</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/MatinSenPaii/3452" target="_blank">📅 16:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3451">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مجدد کانکت شد</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/MatinSenPaii/3451" target="_blank">📅 16:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3450">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nj_FbHvCE3zmdnJYXTGsauT1K6o9ShANphpTZHawx4kpyZIP1AU9hH6zTki9s3rkHH4WSOLkHPszLPjmY4IzHHH5zEZNlr3NvUOdJ5LzfXk90mpavDT3lX_9WyLD86iPCXWM-awsPjPb69VKpCq74HXKBQtabnanMWs9gnOuSCkFbmqjebt42SQbuuTsnDQHsDS4c8gGW3afNNeaRk60K3pxzYAO4BLMSg_A_BqSd8cmdoVMxbYPiExS6iOIX3QAi7eLlj4NlBt4-s8hYFg0vvzudpBSWQ-lptLLoqFeXBsONzA0R63GXC_OWVW4NP-JPcIGkHHeDfYVc7vYp1uweA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجدد کانکت شد</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/MatinSenPaii/3450" target="_blank">📅 16:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3447">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">قطع شد
😂
چیکار دارن میکنن</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/MatinSenPaii/3447" target="_blank">📅 15:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3446">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.7.70:2096?encryption=none&security=tls&sni=sni.111000.indevs.in&insecure=1&allowInsecure=1&type=ws&host=sni.111000.indevs.in&path=%2F#Humanity%201</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/MatinSenPaii/3446" target="_blank">📅 15:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3445">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.7.70:2096?encryption=none&security=tls&sni=sni.111000.indevs.in&insecure=1&allowInsecure=1&type=ws&host=sni.111000.indevs.in&path=%2F#Humanity%201</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/MatinSenPaii/3445" target="_blank">📅 15:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3444">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">Matin SenPai
pinned «
☠️
آموزش اتصال رایگان با آیپی تمیز کلودفلر و کانفیگ‌های BPB  1- ابتدا ویدئوی ساخت پنل رایگان BPB رو از اینجا تماشا کنید(هم با گوشی میشه هم با سیستم. از نصب دستی استفاده کنید): https://t.me/MatinSenPaii/1965  2- سپس آموزش قرار دادن آیپی تمیز و سایر تنظیمات BPB…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3444" target="_blank">📅 15:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3443">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">☠️
آموزش اتصال رایگان با آیپی تمیز کلودفلر و کانفیگ‌های BPB
1- ابتدا ویدئوی ساخت پنل رایگان BPB رو از اینجا تماشا کنید(هم با گوشی میشه هم با سیستم. از نصب دستی استفاده کنید):
https://t.me/MatinSenPaii/1965
2- سپس آموزش قرار دادن آیپی تمیز و سایر تنظیمات BPB رو از اینجا تماشا کنید:
https://t.me/MatinSenPaii/1980
3- این لیست IP رو طبق آموزش مرحله‌ی 2، توی قسمت Clean IP قرار بدید:
104.19.229.21
104.18.139.67
104.16.80.73
104.16.117.43
104.16.89.120
104.16.118.43
104.16.63.25
104.16.7.70
104.16.79.73
104.16.90.120
104.16.62.25
104.16.6.70
4- از قسمت Raw (without settings)، یا Normal، لینک ساب رو کپی و داخل کلاینت V2ray خودتون وارد و به راحتی استفاده کنید.
5- اگر دامنه
workers.dev
روی اینترنتتون فیلتر شده بود، از طریق این آموزش دامنه جدید ست کنید:
https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/MatinSenPaii/3443" target="_blank">📅 15:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3442">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یه کم دیگه واستون مرتب و تر تمیز میکنم آموزش‌هایی که قبلا دادم رو دسته‌بندی میکنم و می‌ذارم خدمتتون</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/MatinSenPaii/3442" target="_blank">📅 15:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3441">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EYoeJu3Y7Ny2WD60JmxenFeYmrPZwrrHYTeyRKEjHLJzJ3GCZQHbA78eUu9SxDgeO1YmChz9gE627YpfCyaigCU-zyBz20FZYY1D0yooaI84bVsVX7TKxkk4T4ucC3EmDl0_zzfDYjzZdFKZcqWsHnOk53kVcYTJkxy9whlCIiV8NhXGc-NB0LFAU5gTZI6ZhtBk4XbfhzaSKjdO2I5cLfMb2GxoGUmAmvjoVG4xA9afGsdIHRrLG9dTpMSCrSl9zsIEO__lZQN7BVwF_FQw4Y-garId8atScUNIgIOan6wgulq5cCgYjUoSrVGmx-pRTszqmPeZwTvaomw6Tgy7GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/MatinSenPaii/3441" target="_blank">📅 15:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3440">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">با این وضعیت، کم کم نت‌ها رو دارن آزاد می‌کنن
از اختلال و اینها گذشت دیگه</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/MatinSenPaii/3440" target="_blank">📅 15:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3439">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">همچنین 104.18.139.67</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/MatinSenPaii/3439" target="_blank">📅 15:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3438">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خود آیپی 104.19.229.21 رو توی کانفیگ‌های معمولی BPB و کلودفلرتون تست کنید. یکی سری از دوستان میگن آیپی سفید شده</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/MatinSenPaii/3438" target="_blank">📅 15:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3437">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خود آیپی
104.19.229.21
رو توی کانفیگ‌های معمولی BPB و کلودفلرتون تست کنید. یکی سری از دوستان میگن آیپی سفید شده</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/MatinSenPaii/3437" target="_blank">📅 14:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3436">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B8XboVZQB70Zn8kZ-LSvVhd0H86Ls6v3cEg8S75U8lODe7HewZ2qFfu83PHjVC9J_7hgagZSVZbLlnHOt0gFflfTtE-ADu8kIsJZAxQmkkfDRFXSMitqJC_MAkIZMev28Q5ly09dzsQ7AB6tDrOybLVMEuR_3kRay8rgmojq6ZOwS0Eg3SWdIFU49tPi3LR3-dV0yNACkSEytekZTHPZXTE3dD1ghZgofhVo8NRN_VfrVbTq0aNPfFv-AKnQiYSaM8dFFXowWAKDzyJHrqH6WX8BG9ZpQNCaFKPm6JNChVWFsGU9MK5DYXQV_5KE-2Dz-Y8fIym_BzsjWxypnGk1sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کم کم داریم توی هرم مازلو اینترنت پیشرفت می‌کنیم:) از صبح دنبال اینم که بتونم یه راه ساده و رایگان برای گیم واستون پیدا کنم، اما متأسفانه فعلا فقط تونستم با پینگ ضعیف با ترکیب سایفون گوشی، گنشین ایمپکت رو بالا بیارم و بازی کنم</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/MatinSenPaii/3436" target="_blank">📅 13:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3435">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نمیدونم احساس منه یا واقعا این شکلیه اما انگار اختلالی که روی پهنای باند سرورهای ایران تأثیر می‌ذاشت خیلی کم‌رنگ شده از وقتی Spoof باز شده</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/MatinSenPaii/3435" target="_blank">📅 11:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3434">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">قول میدم اگر فردا و پس‌فردا اسپوف همچنان وصل بود، یه سری آموزش باحال داشته باشیم ازش. همینطور یه سری آموزش راجب چیز میزای برنامه‌نویسی و ستاپ کردن IDE ها و نصب کردن آفلاین اکستنشن‌های Ai و این قبیل موضوعات چون خیلی آسون با اسپوف میتونم واستون ویدئو ضبط و آپلود کنم و کارم هزار برابر راحتتره</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/MatinSenPaii/3434" target="_blank">📅 03:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3432">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Sy4LWHC8kZ05vdEzOc7-drC0LgFeCxDmfvmoCHua10UZubBhxHBBa5kHdDYhSEwr4viWCCYIwImBbcBfJbQ62OX9hV-Xjof7Tq4CbHFXOu1JxiFxKule_ItEnBKebCTigRsaaIUhJ2H6cBi07NZE7NO-djs9DGJdRJQN2OsLjmWKdw6R1MDwPlfMdtIKAUWGNXy3JfdUdfx71ps23OhvsI_rcmHlEcwUmiLYMYeuA2raRta0bMZb-B-jWEeVlWuwtGutk_oj-wyNI2BdXdyr6Mqa3U_Xs1egJwAP2WXIrVgHyEIC1erWkIaZnsVXUyAxAJss6YRKgsRtt8GthkzGEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XZ1NjiylicMIc8zqNGEBdqEaC1EspWnrXx4Q5sW3q3JewGa_672vHFmxpm0MZEWKD8iab1yJkmddQwjJlwNLeEfnSiy7d9oTDkdViiVkIyLLW_yEcUCNWNy-EkUqeGai4ano16exzGjHvc5svN--5uuLsyvYcsT6sPVQhZwXQ_PCjN41qZfTU5AmsAef-qDrLwnMEuxPocud8N2aXFMGCNgNH8LhLKBc--A_hgYgTfP7I45QGXnaoTHhSZjM-GXB9WOeesZ42k-EUkL5Sozw-dd-4AKDws3xLbMzQOHmzDUWlz0QZMI-ylt-lKqh6_aG6anmh4ivxDetBQjyEwzaGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پولی که قراره آمریکا آزاد کنه: 6 میلیارد دلار
ضرر قطع 80 روزه اینترنت طبق گفته خود دولت: 6.4 میلیارد دلار</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/MatinSenPaii/3432" target="_blank">📅 02:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3431">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">صدای تیراندازی سنگینی که در نزدیکی بندرعباس شنیده شد، پس از آن آغاز شد که سپاه پاسداران یک شناور را در دریا هدف قرار داد و در پی آن، جنگنده‌های آمریکایی قایق‌های تندروی نیروی دریایی سپاه را در خلیج [فارس] بمباران کردند.</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/MatinSenPaii/3431" target="_blank">📅 02:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3430">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نمی‌خوام دلسردتون کنم اما باز شدن Spoof روی فقط و فقط یک دامنه، به معنی اقدام برای سخت‌گیری "کمتر" نیست لزوما. مسئله اینجاست که فقط و فقط
hcaptcha.com
روی sni باز شده. مابقی سایت‌هایی که وجود داشتن برای ابتدای متود، هیچکدوم باز نشدن و الان ده تاشون رو تست کردم با config.json های مختلفشون.
اگر واقعا شل‌تر شده بودش، روی اونها هم باز میشد. بیشتر اینطور به نظر میرسه که دولت الان بهش نیاز داشته که بازش کرده و هروقت هم بخواد می‌بنده.
هرچند همین متدها، هزینه‌های بسیار گزاف روی دست دولت می‌ذاره. هم برای مجددا فیلتر کردن، هم برای خود فیلتر بودن این سایت‌های ضروری.</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/MatinSenPaii/3430" target="_blank">📅 02:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3429">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو: https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو: https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این…</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/MatinSenPaii/3429" target="_blank">📅 02:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3428">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انقدر چیز میز می‌خواستیم دانلود کنیم زمان قطعی، حالا که Spoof وصل شده دیگه یادمون رفته چی می‌خواستیم بگیریم</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/MatinSenPaii/3428" target="_blank">📅 01:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3427">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o5dtKJ1IA1Fi6YN5-Ut4EiA8NthZoAJVQT5UAD5rC0wzuWu9gjz3WueJ8raLKO8w_Ry_w6oMr1hqv3D8bI20mIzCRGdGuODq4MA3GYrnypbJv23UMPvGi19Svb7dDTm3klfJlYGu23DBKbOjFgXqtT14spw-VVkPOF0oWxb-7LvtSDCF1zNScT2vLuxwVSiSDR0KeRD8qAyLAgw4rhXOOaufyfFzLgl1mIcERDIJkD2tiFYwxQwQsPtzt_enPK0yOkVcAP2dreX7p0ptnfvp-cZlinQBv_88em_TGYYTuSghf86G5qrbI7LidnhnpAiuT_YyXzSBJfrMR9WL2bTJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aleskxyz
:
واسه sni spoofing من یه اپ با go نوشتم که به جای اون template واسه client hello که توی کد اصلی هست، از utls استفاده میکنه که میتونه رفتار مرورگرهای مختلف رو تقلید کنه.
همچنین fragment و ارسال چندباره fake sni رو هم بهش اضافه کردم.
توی تست خودم واسه لینوکس و ویندوز کار میکنه ولی نمیدونم داخل ایران هم جواب میده یا نه.
اگه sni spoofing روی نت شما جواب میده، این رو هم تست کنید، هر دو نسخه‌اش رو. ببینید کار میکنه یا نه
از firefox واسه utls استفاده کنید. خیلیا مشکلشون حل شده:
-utls firefox
توی نسخه جدید (v0.3.0) میتونید کانفیگ رو داخل فایل config.ini بنویسید و بذارید کنار فایل exe رو فایل رو run a admin کنید. نمونه محتوای فایل:
listen =
127.0.0.1:40443
connect =
104.19.229.21:443
fake-sni = hcaptcha[.]com
utls = firefox
قبل از اینکه بخواید از این روش استفاده کنید، لازمه این دو تا شرط برقرار باشه.
اول اینکه لینک زیر برای شما بدون vpn باز بشه. اگر این لینک باز شد مقدار ip رو بخونید و یادداشت کنید:
hcaptcha.com/cdn-cgi/trace
‎
بعد این لینک رو باز کنید و ببینید ip داخل ایران شما چیه:
ipmyp.ir
‎
اگه هر دو این ip ها یکی بود، این روش احتمالا برای شما کار کنه وگرنه قطعا کار نمیکنه.
https://github.com/aleskxyz/SNI-Spoofing-Go</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/MatinSenPaii/3427" target="_blank">📅 22:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3426">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اما تنظیمات داخلی برنامه در این نسخه بر اساس آخرین نسخه MasterDNS ساخته شده و در تست‌های اولیه، از نظر سرعت، پایداری و مصرف حجم، عملکرد بهتری نسبت به نسخه‌های قبلی نشان داده است.</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/MatinSenPaii/3426" target="_blank">📅 22:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3425">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaKTldgBn-OVInKOrKtkh0L9JgevkZ8pmeNMA3HIvI5ovO-HHpUdcuPe6aqPibjaYPUWR41hd8fnYzpvFJJZrnml5OsaWzAnb93uLzLcSErQ7GEnJOthLN0YixUtawn3PgX700CpBTt8ZFRzvuB_2-0_X4MbyaL26oCwN0EnYzNxLxzOCj-EtnGVIpmQfy2VKVVRRxcx7CGB-iQYyxo4ee1UYbVA9uvMYj122b_TLeMbrFI8rr1b2ArX3VJqOmANbjX1N35pM0IuYaxx6rVKMWK8cj-1zWTG1lpfhcgpVOhYfqQ2pRhBcp3cFFmBeRxzcjW-NoEvaJzNVspIM3eq618I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaKTldgBn-OVInKOrKtkh0L9JgevkZ8pmeNMA3HIvI5ovO-HHpUdcuPe6aqPibjaYPUWR41hd8fnYzpvFJJZrnml5OsaWzAnb93uLzLcSErQ7GEnJOthLN0YixUtawn3PgX700CpBTt8ZFRzvuB_2-0_X4MbyaL26oCwN0EnYzNxLxzOCj-EtnGVIpmQfy2VKVVRRxcx7CGB-iQYyxo4ee1UYbVA9uvMYj122b_TLeMbrFI8rr1b2ArX3VJqOmANbjX1N35pM0IuYaxx6rVKMWK8cj-1zWTG1lpfhcgpVOhYfqQ2pRhBcp3cFFmBeRxzcjW-NoEvaJzNVspIM3eq618I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آموزش کامل TheFeed از صفر تا صد
اگر تازه با TheFeed آشنا شدید و نمی‌دانید از کجا باید شروع کنید، این ویدیو دقیقاً برای شماست.
👇
در این آموزش یاد می‌گیرید:
✅
اضافه کردن کانفیگ
✅
آشنایی با ریزالورها (DNS)
✅
پیدا کردن ریزالورهای سالم
✅
مشاهده کانال‌ها و دریافت محتوا
✅
آشنایی با بخش TeleMirror
✅
رفع مشکلات رایج کاربران
✅
نکات مهم برای استفاده بهتر از برنامه
دفید یک سیستم مبتنی بر DNS است که امکان دسترسی به محتوای کانال‌های تلگرام را حتی در شرایط محدودیت اینترنت فراهم می‌کند.
📢
کانال اصلی پروژه:
@networkti
📦
فایل‌های نصب:
@thefeedfile
⚙️
کانفیگ‌های عمومی:
@thefeedconfig
توضیحات متنی
👇
سلام. توی این ویدیو می‌خوام خیلی ساده و سریع نحوه کار با برنامه The Feed رو توضیح بدم.
بعد از نصب و باز کردن برنامه، اولین کاری که باید انجام بدید اضافه کردن یک کانفیگه. برای این کار از بالا روی علامت جمع بزنید و کانفیگ مورد نظرتون رو وارد کنید. کانفیگ‌های عمومی داخل کانال
@thefeedconfig
منتشر میشن و می‌تونید از اونجا دریافتشون کنید.
هر کانفیگ دارای تعدادی ریزالور پیش فرض هست که توسط سازنده کانفیگ داخل کانفیگ قرار میگیرن. بعد از اینکه کانفیگ رو اضافه کردید، برنامه شروع می‌کنه به بررسی ریزالورها. ریزالورها همون DNS هایی هستن که The Feed از طریق اون‌ها اطلاعات رو دریافت می‌کنه. این مرحله ممکنه چند دقیقه طول بکشه، پس اگر بلافاصله کانال‌ها نمایش داده نشدن نگران نباشید. بعد از پیدا شدن ریزالورهای سالم، لیست کانال‌ها دریافت میشه و می‌تونید وارد هر کانال بشید، پست‌ها رو ببینید و در صورت وجود، عکس‌ها، فایل‌ها، ویس‌ها و ویدیوها رو دانلود کنید.
اگر یه زمانی دیدید برنامه کند شده یا اطلاعات جدید دریافت نمی‌کنه، معمولاً مشکل از ریزالورهاست. برای همین داخل برنامه بخشی به اسم «پیدا کردن ریزالور» وجود داره. وارد این قسمت بشید و روی «بارگذاری لیست پیش‌فرض» بزنید. با این کار حدود ۵۸ هزار ریزالور برای اسکن آماده میشن.
اگه خودتون ریزالور خاصی دارید، می‌تونید به صورت دستی هم واردش کنید. علاوه بر این، ربات
@dns_resolvers_bot
هم می‌تونه برای پیدا کردن ریزالورهای جدید بهتون کمک کنه.
بعد دکمه «شروع اسکن» رو بزنید تا برنامه ریزالورهای سالمی که روی اینترنت شما کار می‌کنن رو پیدا کنه. وقتی چند تا ریزالور پیدا شد، می‌تونید اون‌ها رو به لیست فعال اضافه کنید. فقط یادتون باشه موقع اسکن بهتره VPN خاموش باشه تا نتیجه دقیق‌تری بگیرید.
داخل برنامه یه بخش دیگه هم به اسم Tele Mirror وجود داره. این قسمت با سیستم اصلی TheFeed فرق داره و برای نمایش کانال‌های عمومی تلگرام از سرویس‌های گوگل استفاده می‌کنه. با TeleMirror می‌تونید خیلی از کانال‌های عمومی دلخواهتون رو دنبال کنید، ولی محدودیت‌هایی هم داره؛ مثلاً امکان دانلود فایل یا پخش ویدیو توی این بخش وجود نداره. همچنین اگر سرویس‌های گوگل در دسترس نباشن، ممکنه Tele Mirror کار نکنه. البته این موضوع روی بخش اصلی TheFeed تأثیری نداره و سیستم اصلی برنامه همچنان از طریق DNS به کار خودش ادامه میده.
در نهایت اگر جایی به مشکل خوردید، اولین چیزی که باید بررسی کنید ریزالورها هستن. در اکثر مواقع با پیدا کردن چند ریزالور سالم، مشکل برنامه برطرف میشه. برای دریافت آخرین اخبار پروژه هم می‌تونید کانال
@networkti
رو دنبال کنید، فایل‌های نصب رو از
@thefeedfile
بگیرید و کانفیگ‌های عمومی رو از
@thefeedconfig
دریافت کنید.
ممنون که این ویدیو رو دیدید و امیدوارم از The Feed لذت ببرید.</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/MatinSenPaii/3425" target="_blank">📅 20:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3424">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">☠️
رفع مشکلات رایج SNI Spoofing و آموزش تغییر لوکیشن هر کانفیگی به آمریکا
⚡️
لینک داخلی ویدئو: https://guardts.ir/f/00871d86ad44
⭐️
توی این ویدئو قدم به قدم مشکلات رایج SNI-Spoofing رو بهتون توضیح میدم و میگم که چه شکلی میتونید با ترکیبش با سایفون و یک سری…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/MatinSenPaii/3424" target="_blank">📅 16:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3423">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZesiRfybUneQ6-mlh2xhQKc8Re32LEOxmv_Wk_9n8vCAr1QrltR94CYVo1BITxeNKUHp6kT731_86nZUAlEULGQSGQc-IDAXam1P_9gTuWIqJ_yoD3lUIYSfteezhrYnBTe-wawrvlUSGCvfXw-inVS9n7hDEyw1Q2Hb0A99hGEmqljNODg9LqbFE7PTRT0mKuqsZJDUFBU12i1GfsA50yZRUT0_OfgUM9of-ESQdb4bKPSYIRvPOPtJOnJ7458rzItNagqQf5hrKVxevH35PPYddoKmsCGGXAZsJCmrJj-bTj3Rg3t3_5LfpSol6VAHM1e8diSuIBTpPOkw97RdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این ارور رو میگیرید روی دسکتاپ،
۱- چند بار تست کنید و تلاش کنید برای اتصال
۲- گزینه Parallel test رو با تمامی گزینه‌ها بزنید تا شروع کنه به گشتن
۳- اگر باز هم نشد، یک بار MasterDns رو حذف و مجددا روی سرورتون نصب کنید و با تنظیمات اولیه‌ی خودش تلاش کنید برای اتصال. اینکریپشن و اینها رو تغییر ندید ترجیحا و دقت کنید که دامنه و اتصال و دستورات رو مو به مو مثل ویدئو انجام دادید</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/MatinSenPaii/3423" target="_blank">📅 15:54 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3422">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وقتی می‌بینم یه سایتی که پیداش کرده بودم و توی یه ویدئو معرفی کرده بودم، توی آموزش‌هایی که بقیه می‌سازن هم استفاده میشه حال می‌کنم واقعا.
وقتی می‌بینم یکی یه پروژه‌ی خوب نوشته، خیلی خوشحال می‌شم از share کردنش.
وقتی می‌بینم یکی یه ویدئوی آموزشی خوب ساخته، لذت می‌برم از به اشتراک گذاشتنش
شخصیت من اینه. و حسادت، دورویی، دزدی، بدجنسی و رفتارها و صحبت‌های ناسالم و غیرانسانی توی کامیونیتی اینترنت آزاد جایی نداره
✌️</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/MatinSenPaii/3422" target="_blank">📅 14:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3421">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کانفیگ ترکیبی متصل با تمامی نت‌ها
😎
بزنید بترکونید
❤️
آموزش اتصال ترکیبی
👉
ویتورای+سایفون</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/MatinSenPaii/3421" target="_blank">📅 14:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3420">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sF7bHG6UWDlwHE9R3YSpmHvGwmMafLKHoeSxc5bz-8nyfWz6ecMS7vFoGF9Ui9jBPcPWhrtgAMsYHw1xy_81Vy3a-O5-qAIiZbLXvik3eaJv2t7xURaFOOKKCeYT6veQbffwGOAzxPJGMIljLVI6lS38hDjGH8GRYPUt9WsQKB8gEd8e94AlQf3-FpabzvTIVVQoYDydPszA2ReaxlMiDIahakNIlHrpGiH_74u9lSd4pCkbGXhowG9cH-afXHmszxQrjp6g8UjMCxKJqXtnAFoCVD6EsY9mpOG-AQlNuXOwJ5Bu7FtFaLyJl-dSLYJ0JPTZ3lJelPYchzHSjrlsRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر وصل نشد، این خبر رو هفته‌ی بعد دوباره بخونید</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/MatinSenPaii/3420" target="_blank">📅 13:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3419">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">برای کدنویسی با هوش مصنوعی، به شخصه دیگه Antigravity گوگل رو توصیه نمی‌کنم به خاطر rate limit بسیار پایینش که با چند مرحله تا یک هفته شما رو محدود می‌کنه. حتی برای اشتراک Pro هم صادقه این قضیه. پیشنهادم اینه که اولا اگر در توانتون نیست هزینه بدید، دوتا کار…</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/MatinSenPaii/3419" target="_blank">📅 11:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3418">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">برای کدنویسی با هوش مصنوعی، به شخصه دیگه Antigravity گوگل رو توصیه نمی‌کنم به خاطر rate limit بسیار پایینش که با چند مرحله تا یک هفته شما رو محدود می‌کنه. حتی برای اشتراک Pro هم صادقه این قضیه.
پیشنهادم اینه که اولا اگر در توانتون نیست هزینه بدید، دوتا کار کنید. ۱- از Codex استفاده کنید که کمپانی Open AI توسعه‌اش داده و از مدل GPT 5.3 High برای دیرتر پر شدن rate limit استفاده کنید. مثل آنتی گرویتی هم دردسر تحریم و... نداره. فقط یه vpn می‌خواید که Chatgpt رو باز کنه عملا. اپلیکیشن هم داده برای ویندوز اما به عنوان Extension VsCode هم می‌تونید نصبش کنید. و محدودیتش هم سخاوتمندانه هستش و به صورت هفتگی هم صفر میشه. کما اینکه میتونید از ایمیل‌های متفاوت استفاده کنید و یه گفتگوی یکسان رو باهاش ادامه بدید!
۲- وسط کارهاتون هم می‌تونید از خود Ai Studio و مدل Gemini Pro به همراه گزینه‌های Google search و Url context با thinking budget بالا استفاده کنید.
اگر هم می‌تونید هزینه بدید، پلن‌های پولی Claude code و یا Cursor رو تهیه کنید. به مدل‌های چینی Kimi هم نگاهی داشته باشید.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/MatinSenPaii/3418" target="_blank">📅 10:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3417">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">متاسفانه دید همه به dns، کلا dnstt و ساعتها اسکن بی‌نتیجه و دنبال ریزالور تمیز گشتن و سرعت دو سه کیلوبایتیه. نمیدونن که من با همین WhiteDNS به راحتی میرم اینستاگرام و یوتوب و تیک‌تاک و...
چیزی که بهش دقت کردم، روی اینترنت‌های متفاوت نتیجه ممکنه زمین تا آسمون فرق کنه. در حدی که یکیش تلگرام به زور لود بشه، یکیش بشه به راحتی مثل قبل از دی‌ماه رفت اینستاگرام</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/MatinSenPaii/3417" target="_blank">📅 07:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3416">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d4ssmQMqjIxn0ybqnM44e0hy-PIP5fihdS9VVWacg2NaIQU2HQcniWLA_5rYz92tCp5tb0XzQ2pYz3cp91H9fLQzDE-QJBCuv6-NeiiAXU1AIMsx6NnsaCyXX4whPpCIFofMlYKvnmyMxgiF04ySBLpX5weZKKODELXJw3kNHQsh7Axhdwc5D6aCHZ_mgBuoJzyhn2PDPe-mygrI4-5t_MqC7LBui-ThEdcb6nioehm5Htk8TEEkxvrJ2U-erxkFT36cuOG-B6ZnkNOUAfS5g7PHmv64_V88mlUiGa4Qa1SF7Zcihx4k0fxiTELaHQn0ULE6grKwgGbKUGYJNM2CMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر خارج از کشور هستید، برای خانوادتون نمی‌تونید V2ray کانفیگ کنید و بفرستید چون ارتباط از داخل به خارج و خارج به داخل قطعه. اما به راحتی می‌تونید واسشون روی سرور مستر دی ان اس نصب کنید و همه‌شون رو با WhiteDNS وصل کنید. که برای شرایط ابتدای جنگ تا به الان…</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/MatinSenPaii/3416" target="_blank">📅 06:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3415">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j4kIp2HCZFLBDnAfW7cJ64s_qulJfYTlv83UKReRWKuAU2SGbqkc1ybEKC8YjZudcXQGmiGo1EJgVvBAKiqdtpueQafJxSBAt75s4WDwSHtsfgtfCWNt2dxR-j-YPJp8D91AfWPrvFWHr2QwxKQjb7lnBokjH39q8rThLW4uPhWDxzwbgQKODGDI9S4VdabCEX6P5ucDFcVY_A2um3sCgkclHs9mMm2Bdus3xQyBJIG_Rg2HsbUOiPea59253Nj-xWxG7Ft3UCkUTjPEjGtSoHK4Pa5sf2LUaGzyRED5eE8Odr9GZ-W9jYB8DDdzOdQ4ziNG_4nwuU9qHDPMtl4sOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر خارج از کشور هستید، برای خانوادتون نمی‌تونید V2ray کانفیگ کنید و بفرستید چون ارتباط از داخل به خارج و خارج به داخل قطعه.
اما به راحتی می‌تونید واسشون روی سرور مستر دی ان اس نصب کنید و همه‌شون رو با WhiteDNS وصل کنید. که برای شرایط ابتدای جنگ تا به الان کاملا پاسخگو بوده. اینم آموزشش:
https://t.me/MatinSenPaii/3372</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/MatinSenPaii/3415" target="_blank">📅 04:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3414">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rQ5RiHDqxW4ai2vBLh6c6Pc-DKu4w24j0aH0zprRH5eEgOZVPJYfgeu1DeMHG9wHgjf3Cffvb-y6zpizKSdRrHvetrgXvOGJzzLm5o8TUOiBdVZxpOeULqf8PcVkK3WSiloPNSd0BOvJgGJ6bMq9Re_YVWSiLGT3Bg3A584vR28kHDFcoPXOQwzSBDBYfxfyRN6RlNhsvglkxn0LVQOyck-2vbAKesVTMLEKaznX3WU_SK6GK4dgv3nJXO5LAgXHXpseiGXpD09ZM4JtofI6oYUU7WJfucdnBrG6vxlptcGSCfXEssQFfj0WClU65VlyqGf-XobiMzTPG-A3lkuM9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچنان SNI وصل هستش
گزارشاتی دادن بچه‌ها که براشون کانفیگا پینک میده و کار نمی‌کنه، که خب باید بگم اختلال از سمت اپراتوره. یعنی شما دو بار پشت هم پینگ بگیری، بار اول پینگ میده بار دوم پینگ نمیده‌. در این حد هستش روی بعضی اینترنت‌ها
اما خلاصه تا وصل هست، استفاده کنید</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/MatinSenPaii/3414" target="_blank">📅 03:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3413">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EpwVjaLAL6ndobmW00afS1c5pfH0W6DXwDgyxf2-Vp5M58ImscXCv045CM4vnq5BF9xa0aFgHVfF9yVFJyAdX7BwOaEej3fbSjvHmoYr0xHRvp4uSJx7hqwQWZhwMpGQ0uGYkw6bYHi7NXakIiR2Uob7T48YBU0MmDpPMDedsGmp4erg0EStctALmFDzix91fItdN401UaAgHLYnu5NLOAVth0qgCLsxMkMtyTkFdhhnUxGf1AvBtlNqoS0_P3_iecDNL0P5W4hmUVU2mEKH8W-xU0CPTASpC5QVfmGt4zCk8rBHdvUCawEuzJyUpsa1LjSwRxiMZjFRfeCMBUbxTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعضی آدما انقدر خودخواه و بی‌شعورن که انتظار دارن کل کار و زندگیت رو ول کنی، و تک تک ۱۵۰۰ تا پیامی که روزانه می‌گیری رو بشینی جواب بدی.</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/MatinSenPaii/3413" target="_blank">📅 03:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3412">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو: https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو: https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این…</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/MatinSenPaii/3412" target="_blank">📅 21:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3411">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">برای SNI SPOOFING روی Mac می‌تونید از پروژه‌ی خوب Cloak استفاده کنید:
https://github.com/g3ntrix/Cloak</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/MatinSenPaii/3411" target="_blank">📅 20:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3410">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گویا پولی که از صرافی‌های ایرانی میاد رو بلوکه می‌کنه کلا. حتی از Trust wallet هم ممکنه این بلا سرش بیاد. ترجیحا از این سایت نگیرید اصلا</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/MatinSenPaii/3410" target="_blank">📅 20:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3409">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو: https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو: https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این…</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/MatinSenPaii/3409" target="_blank">📅 19:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3407">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3407" target="_blank">📅 19:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3406">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">زبان‌های مختلف برنامه‌نویسی، هر کدوم قاعده و قانون خودشون رو دارن و به درد یه جایی می‌خورن، اما یکی از پارامترهایی که می‌تونیم اونها رو بر اساسش مقایسه کنیم، «کامپایلری» بودن یا «مُفَسِّری» بودن(از تفسیر میاد) اون زبان هستش.
۱- زبان کامپایلری (Compiled) چیه؟
توی این زبان‌ها، قبل از اینکه برنامه اجرا بشه، کل کد به زبان ماشین(کد باینری) تبدیل می‌شه. این کار توسط کامپایلر انجام می‌شه. این که ماهیت کامپایلر چی هستش، بماند.
مزایا:
۱- سرعت اجرای خیلی بالا
۲- اکثر خطاها قبل از اجرای خود نرم‌افزار پیدا می‌شن (Compile-time error)
۳- پرفرمنس بهتر
﻿
معایب:
- باینری تولید شده معمولاً فقط روی یه سیستم‌عامل و معماری خاص (مثلاً Windows x64) اجرا می‌شه. و برای پشتیبانی از پلتفرم‌های مختلف باید کراس‌کامپایل کنیم که پیچیده هست و دردسرهای خودش رو داره.
۲- تغییر کد و تست دوباره سخته (باید دوباره کامپایل بشه)
مثال‌های معروف:
زبان C --> سیستم‌عامل، بازی‌سازی
زبان C++ --> بازی‌سازی (با انجین Unreal Engine)، نرم‌افزارهای سنگین
زبان Rust --> سیستم‌های امن(به خاطر مموری سیفتی) و سریع (در حال رشد و توی هایپ شدید)
زبان Go(گولَنگ) --> بک‌اندهای Scalable(مقیاس‌پذیر)، میکروسرویس‌ها
زبان Swift --> اپلیکیشن‌های مک و iOS
۲. زبان مفسری (Interpreted) چیه؟
کد خط به خط، موقع اجرا ترجمه و اجرا می‌شه. نیازی به کامپایل قبلی نداره.
مزایا:
۱- توسعه‌ی نسبتاً سریع‌تر (تغییر رو میدی، فوری اجرا می‌کنی)
۲- یه سری به عنوان مزایا می‌گن خوندن کد راحت‌تره که من قبول ندارم اصلا
۳- در کل Portablity بهتری دارن. هرچند شما عموما مجبوری سورس کد رو کامل تحویل بدی چون نرم‌افزارت همونه!
معایب:
۱- سرعت اجرای پایین‌تر (چون هر بار باید ترجمه بشه)
۲- مصرف منابع بیشتر
۳- خطاهای سینتکس و DataType، معمولاً زمان اجرا (Runtime) تشخیص داده می‌شن، در حالی که توی زبان‌های کامپایلری، خیلی از این خطاها زمان کامپایل گرفته می‌شن. این موضوع برای پروژه‌هایی که با این زبان‌ها نوشته شدن، باعث می‌شه دیباگینگ پیچیده‌تر بشه.
مثال‌های معروف:
زبان Python --> هوش مصنوعی، مهندسی داده، اسکریپت‌نویسی(ابزارهای قدرتمندی داره)، وب (Django/FastAPI)
زبان JavaScript --> فرانت‌اند وب (بک‌اند با Node.js و فرانت)
زبان Ruby --> وب (Ruby on Rails)
زبان PHP --> وب (WordPress و لاراول)
(هرچند جاوااسکریپت و php رو دیگه نمیشه کاملا مفسری دونست. به خاطر JIT Compilation که بعدا توضیح می‌دم)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/MatinSenPaii/3406" target="_blank">📅 19:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3405">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4659a46672.webm?token=EOVlmkZr3VnuAqtOz-ZsR41p8DbevBnkISdrcEQmyxDJNFqAZ-aPYhzuT9kPoM4GxxYBapk1G5P63u72iY4ZOEs28ccbrZ-RB12__7eEEfSPw-Hmmczm0SGAeb4INqAnqBX73nB6MDbt1-BbOEPT_3EzAgWN2ZzNeDZYGBIKvixACloStBrg-cg6UrkSklaQNRQH24E1nPL9IQaqCOzMJ3nbwO7ceVUG8XzVAZzFSNfHJNMAscOFrnQcXSo3x44K26arRh4KJ9YeHLGI67qTm3B_PL_rEwGjpYV7e0u21Wh7inB_fHR9_R1VD5xsp1_zWWVR5l679EnQY2QuWiU13w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4659a46672.webm?token=EOVlmkZr3VnuAqtOz-ZsR41p8DbevBnkISdrcEQmyxDJNFqAZ-aPYhzuT9kPoM4GxxYBapk1G5P63u72iY4ZOEs28ccbrZ-RB12__7eEEfSPw-Hmmczm0SGAeb4INqAnqBX73nB6MDbt1-BbOEPT_3EzAgWN2ZzNeDZYGBIKvixACloStBrg-cg6UrkSklaQNRQH24E1nPL9IQaqCOzMJ3nbwO7ceVUG8XzVAZzFSNfHJNMAscOFrnQcXSo3x44K26arRh4KJ9YeHLGI67qTm3B_PL_rEwGjpYV7e0u21Wh7inB_fHR9_R1VD5xsp1_zWWVR5l679EnQY2QuWiU13w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/MatinSenPaii/3405" target="_blank">📅 15:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3404">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">⭐️
کمی مرتب کردن مطالب برای دسترسی به اینترنت آزاد با SNI-Spoof:
1- آموزش پایه:
https://t.me/MatinSenPaii/2627
2- آموزش پایه رو که دیدید، بفرمایید از این json استفاده کنید:
https://t.me/MatinSenPaii/3168
3- و کانفیگ‌های این پست:
https://t.me/MatinSenPaii/3183
ترجیحا با ایرانسل یا سامانتل
4- سؤالات متداول راجب این متود:
https://t.me/MatinSenPaii/3189
و تبریک میگم! شما به اینترنت آزاد دسترسی دارید.</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/MatinSenPaii/3404" target="_blank">📅 14:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3403">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اسپوف روی یه سری از اپراتورها برگشت. هرچند با وضعیت دیروز، و گزارش یک سری از دوستان توییتر، اختلال شدیدی انداختن و در تلاشن برای یه سری CDNها بدون اینکه مردم بتونن تانل بزنن، دسترسی خارج باز کنن. که احتمالا سر همینه این وضعیت:
{
"LISTEN_HOST": "
0.0.0.0
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
104.19.229.21
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
hcaptcha.com
"
}
﻿</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/MatinSenPaii/3403" target="_blank">📅 14:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3402">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">توی دایرکت چنل یکی داره میگه شیر و خورشید جدیده زیر پنج ثانیه وصل میشه، یکی میگه دو ساعت هم شده و وصل نشده.
به نظرم باید بذارید حالت هواپیما و با rangeهای متفاوت تست کنید. انقدر زیاد منتظر موندن هم دیگه فایده‌ای نداره.</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/MatinSenPaii/3402" target="_blank">📅 14:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3400">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نیم ساعت تا یک ساعت شنیدم بچه‌ها گذاشتن تا وصل شده.
اما طبق گفته‌ی برنامه‌نویس پروژه، خوبیش اینه که بعد از اون دیگه نیازی نیست انقدر منتظر بمونید و به همون آیپی تمیزی که برای شما پیدا کرده وصل میشه
خلاصه که اگر گوشی بیکار دارید، بذاریدش سر کار</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/MatinSenPaii/3400" target="_blank">📅 12:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3399">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکلاینت شیر و خورشید</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.24.apk</div>
  <div class="tg-doc-extra">25 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3399" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/MatinSenPaii/3399" target="_blank">📅 10:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3395">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکلاینت شیر و خورشید</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pbEbkUY9QbjuBwryX92pklQhCdxlXIFxN3iCdIKhs9BhFV6ld2edMGumXOx2P5E5rWottkXaZlV8kee5a9cOhkbTH5kNQauFtn7n4-qa76r3jSBQrXr4GpLfVwk_srJDyUFZQJrltLI-GtDnAqH5Rt4t3ao9_CmxIQma3l-rAEuyS-_AS-A4v55KH85oKTU-3B_TtlxTidQpBqn01a9oRG77XnKWH_0ykAX2Yguacjh_zPJGN8JJAAJM-DA2IHTNvX8EtptPvVrLK4BcdXrckDRz1GMIfcVbSWD38PnNf_-oOb7H2ziSotGZ0YcW_kEGGgloh_zYcIEthOFyfQaJRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qGg6WZ0IzqlezysHmfc4fNsrV7SqoMIKpVHkn9jF60X3lPtePOQ3ERrGflmkwgN7MQQVic_o3xyTA36nRLNpFTOuZNHQyJCDoeNsq8rclp6DVU3ykC9pf1AR_LhStAZ_bxrYGrvawugd3BJH2hNO9ut3HL7tFD4UqhJsYgemfvLgYJGmw_LQx2DBsdXeLfkVgvTcpXo_lMqECxW5NKNHljF-4txJSg25aqPIIKesYhG80cFTJ7hAbzxjSKq1oHxwKN5KN6Vg3siQ1eIZdq1HCFQLaMt5UYQD6MIFUFNej1_BSnqWp5H1LfwtA-37myYrNzHMqEXY-yeR-hBgpi5CKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jL6GWYv7NgXMxVnRQFjJDrz49jEVF-FPGJ3B_szi2qJ77YJPLunOpeTKTF6leSdt8_-J_l3LGCXhwVG9Hzy_agyeL9aOHuwEIHV6911jP6X6AagS6WMNUqpn210UiCBEAJ9MFfliaavgtwAJkvsmu51LFSuOb4myeLbQQ7E5-JbVWJGR1V38Ujw8sVRTwJueZnZVHJEstzT_RSNF8jThku7s2wznX72tKnc3JCuyTn2-8-0hbEA68F-sJCXc1yjA0j_09kf6a1T_i78vDuoPYOzGkP33NV9tU58Q-7RwysZpCUNpZHDWfj6A5---bmES8afF5n8sk06jBTzs9Avj2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mKxZXzDpZcKCHTnnrF-ewZvSWBKSsuz13Hs6B05uxU2VDDAJnyFySrJVoGRiNIS1Pf91aB7n7wasnlV0kBnsnywZ5cvDWNp1Sw0GI6gmTO6As0lTMNtcswqUpCDY8qvh9z036rOIlVS_yfy5lKfAjB25PvquAf_u-VioDU1GudP64UYbCckTATC4wCZrNd_U5UYEyX9pmvC9VrqvHpiSV32QJoE8iHrADfwjF4iRSwOMGn-K1eeDxhdK3beAL3QfOuD1dNcm8AxWWNsSGsyZuetAV17olssbAwrm1hmbHvutyKc_kEYiTsm4SY-n0Kxxxyd1nbxftXxmXHyhgz5CBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آپدیت جدید کلاینت شیر و خورشید 2026.05.24:
- آپدیت Beast Mode برای درست کار کردن روی CDN Fronting
- اضافه شدن اسکنر ای‌پی. برنامه لیست خیلی بزرگی از ای‌پی های ممکن را داره٬ پس اگر در اتصال مشکلی دارید پیشنهاد میکنم تنظیمات قدیمی ای‌پی ها و SNI رو از قسمت settings برنامه حذف کنید (خالی باشه)‌ و اجازه بدید برنامه خودش کار رو انجام بده. دقت کنید ممکن هست بار اول خیلی طول بکشه٬ حتی چند ساعت!
- اضافه شدن پروتکل های بیشتری که با CDN Fronting کار میکنند. احتمال اتصالتون و سرعت باید یکمی بهتر باشه الان
- قابلیت غیر فعال کردن سایتی که زمان اتصال٬ سایفون باز میکنه!
- قابلیت تنظیم پورت مورد نظر خودتون برای LAN Proxy ها.
- قابلیت تنظیم username و password مورد نظر خودتون برای LAN Proxy ها. این تنظیم دلخواه است و اگر تنظیم کنید فقط با این username و password در شبکه خانگی میتونن به شما وصل بشوند.
- آپدیت شدن هسته سایفون
میتونید از اینجا دانلود و نصب کنید و ممنون میشم اگه به اشتراک بگذارید که تعداد بیشتری ببینند:
https://github.com/shirokhorshid/shirokhorshid-android/releases/tag/v2026.05.24-a3b91cf</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/MatinSenPaii/3395" target="_blank">📅 10:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3392">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N5XRN13L3gymjmZ5vDBSFzrIkjoOUhjVwpeRVjacA4kx2c3nQVjnmMp8qk3ltb-eKz2Oha5qqocn9K_OfTgBO6WgIt36UW0qnbU1F-_sEwjlV4uYtOiE5w6s_h-A5rQgcz4eg1hPDd5uvAE1UM5M35hI2CgNd6B3ykUyHMacMh8g65PhzKqZTmwyVEc_1a0-UtiQSa6pRNVcvmgMP9DaCN5fKZ9QFnIcyosfFu_2xV-3yAx-7m-J3i2WmW26j74NRWaa-VofZWiOGaZ6NsvIjvxYp8BO-M4pq1I0ZK3e3k3fkGq4CO7U37SicWhamSJIVz8xLp4AH-3IvqTQAUHECA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو: https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو: https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/MatinSenPaii/3392" target="_blank">📅 09:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3391">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام خدمت همه همراهان عزیز
ویدیو آموزش ساخت سرور شخصی که متین عزیز تهیه کردند دقیق همه مسایل رو ‌توضیح‌ میده.
تنها‌ نکته‌ای که باید اشاره کنم، متین از ترمینال برای وارد کردن دستورات و نصب MasterDNS استفاده کرده.
من پیشنهاد میکنم برای راحتی کار شما، بعد از خرید دامنه و اتصال DNS از ربات
@WhiteDNS_installer_bot
استفاده کنید.
اگر از این‌ ربات استفاده کنید، فقط با پروکسی کردن تلگرام‌ میتونید سرور خودتون رو مدیریت کنید و در شرایط بحرانی فقط از طریق تلگرام همه چیز رو مدیریت بکنید.
ممنون
@WhiteDNS</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/MatinSenPaii/3391" target="_blank">📅 09:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3390">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اما تا ۵۰-۶۰ گیگ روزانه نباید موردی داشته باشه. سرور رایگان هم خواستید از سرورهای کانال مسیر سفید می‌تونید استفاده کنید ولی خب تفاوت سرعت رو توضیح دادم توی ویدئو که به چه شکلی هستش:
https://t.me/Masir_Sefid</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/MatinSenPaii/3390" target="_blank">📅 08:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3389">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DEke3Ku2l6S7qRHaylslBseJHr_v7sxVctRywYZZ13F0JuhmEAodt85XSrfQtaWC2L4Z8fsSddWPCCr0Abcn1GqBE5CAv9ijEreA1Ny1IP1rvV_f_ymrPO4UcTI7_8Oa99sJFZp7m-Xt_f0MO8Vi138EH6VT3TSauZV_Ynz9IHyVnn9U51J-k4JFjXtsIEuCj0YHYbbdQ_A17X0Q3QH9_AEclrOKMn9U4tBDOkaAi96bHc-geKSPyq9an5viXE5z5YEK4iSZ7R_VZ3nAAOsjOqmCUCC_eCHAdE5byEEhIzDQ01s3T6e7qkYP-MQuQQImhyUq672szAhe5rKqVTgKDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ حجم دقیقی وجود نداره عزیزان. اما از چند ده گیگ متفاوته تا ترابایت حتی
گاهی اوقات فیلتر شدنه کاملا شانسیه متاسفانه</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/MatinSenPaii/3389" target="_blank">📅 08:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3387">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ProxifierSetup.exe</div>
  <div class="tg-doc-extra">5.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3387" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این هم پروکسیفایر و یه لیست از Activision Key های مادام‌العمرش (برای مک و ویندوز)</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/MatinSenPaii/3387" target="_blank">📅 03:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3382">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3382" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه Universal اندروید لینک داخلی:
https://up.theazizi.ir/download.php?t=e8a7a62516394e4aecbd26ca36dbb113e0aa</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/MatinSenPaii/3382" target="_blank">📅 03:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3374">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta3-linux-amd64.deb</div>
  <div class="tg-doc-extra">17.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3374" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه ویندوز X64 لینک داخلی:
https://up.theazizi.ir/download.php?t=4b31fefbad0c08f180216f8e4c1eecc316d7
نسخه لینوکس amd64 Debian لینک داخلی:
https://up.theazizi.ir/download.php?t=bb6cfd1d86d4ed7a1826a4850b901ed46c58
نسخه مک amd64 لینک داخلی:
https://up.theazizi.ir/download.php?t=acbf869993172d51c2286fc812931ef48fd4</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/MatinSenPaii/3374" target="_blank">📅 03:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3373">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Master-White-DNS-@MatinSenPaii.zip</div>
  <div class="tg-doc-extra">25.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3373" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">حاوی فایل دستورات سرور
فایل لینک تمامی سایت‌ها
فایل 5800 ریزالور جمع‌آوری شده توسط بنده از سرتاسر تلگرام
لینک داخلی:
https://up.theazizi.ir/download.php?t=b9162802b5da63cf5b39b02133170f4ad2bf</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/MatinSenPaii/3373" target="_blank">📅 03:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3372">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو:
https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو:
https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- خرید دامنه و سرور ارزان با کریپتو(+آموزش)
2- تانل کردن ترمینال با Proxifier و ssh زدن با خود ترمینال
3- تنظیم دامنه در کلودفلر و راه‌اندازی ساده‌ی سرور MasterDNS
4- استفاده از سرور MasterDNS در کلاینت های ویندوز و اندروید WhiteDNS
5- توضیح استفاده از Parallel Testing در WhiteDNS
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز به خریداری یک عدد سرور لینوکسی و دامنه داره(مجموعا 5 دلار نزدیک به 800 هزار تومان) کافی برای اتصال نزدیک به 5 نفر
کانال مستر دی ان اس:
1-
https://t.me/masterdnsvpn
گروهشون:
2-
https://t.me/MasterDnsVPNGroup
کانال وایت دی ان اس:
1-
https://t.me/whitedns
گروهشون:
2-
https://t.me/whitedns_group
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/MatinSenPaii/3372" target="_blank">📅 03:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3352">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UCUt5tADdd6db443Zx6oZPfaPS2EOt4JUAawePLeoeZegyuV0lvT6HkSbRbBdBuEbXGlw1vbMpskLvAbG_em2Nv2AqYSmapd-K_rWsuE77vUzm22hkQSYeleRPg8iG5NvmbLlHpnWdjTgnCbxIRYHGi1EN-ZOKs3K3dEmlSjsdGClm20CoaOzI1RTdupOyjCjWY9Fl1eXlW6NDApXH5bYUSZTXF6Gkp8JeUmigdbEJlbZFt7OSXS21MfuLoYDGGnoZPdOlKaUmLHCJdWtHSy77O-fIXSJnHuktUl9_dcDLfOUaSwoAI-td2oIuvYp0dPulZz6jKqnnbCu9OQf1qfbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدرام وقتی
یه پروژه جدید
میزنه و مردم میریزن سرش هی سؤال میپرسن ازش:</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/MatinSenPaii/3352" target="_blank">📅 22:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3351">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آموزش بعد از یک ساعت و نیم تایم نفس‌گیر تموم شد ضبطش(خودش شاید اخرش نیم ساعت بشه اما مشکلات فنی‌ای پیش اومد اواسطش که متأسفانه باعث شد طول بکشه اما در عوض خیلی کامل و جامع شد)
نیم ساعت دیگه میرم برای ادیت، تا ۲-۳ صبح ایشالا حاضر میشه
با تشکر از همه‌ی بچه‌های گل تیم وایت دی‌ان‌اس و مستر دی‌ان‌اس</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/MatinSenPaii/3351" target="_blank">📅 22:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3350">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">Matin SenPai
pinned «
ببینید همراه اول میتونید وصل بشید؟  {   "LISTEN_HOST": "127.0.0.1",   "LISTEN_PORT": 40443,   "CONNECT_IP": "85.9.112.219",    "CONNECT_PORT": 443,   "FAKE_SNI": "www.hcaptcha.com" }
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3350" target="_blank">📅 19:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3349">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MWrTWRUOKIN3AkjZy_q86AB0-2FYK5HaS308skXCIxqtGQprse0QX-6oBzb70SGIYp9LqILvdvI7yzYQq0emlxX86Rf_nMTXYkY5UrOEIQDgwq9RXcK_qwF_73lqvQ1wYuhz4YMc8KtKi4KqDtNV2BNDyuCdLrHHkUkeKiLkYcB4fK5DLT5AteZekHPJstFHWB2mYd0Lhv0CKpIbycNC9Xmj1GSHEkr9EwaxUQoUOYaaFz9nBIAXWoqW4WvfTWJ1K-YrWzZ8itblR9VwznsvarlrVB42hM0hx7lKuTAW5h8ffHJGrvV6BLX-MBMcZraZJJjf7TnUJ67YXbPWn1XzmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متد مستر دی‌ان‌اس که توی WhiteDNS ازش استفاده می‌کنیم، مبتنی بر DNS و برای شرایطی که گوگل هم قطع هستش. لطفا انتظارتون رو ازش بالا نبرید در حد دانلود و پینگ پایین و...
بهش به چشم برادر ارتقا یافته‌ی dnstt نگاه کنید. که نیازی نیست در به در دنبال تک تک ریزالور بگردید واسش.
و یک متد اضطراری هستش هرچی نباشه. شاید بهترین کارت و برگ برنده‌ی اضطراری ما باشه، اما همچنان اضطراریه.
برای شرایط الآن، شاید Goose یا Skirk یا Mhr برای شما بهتر جواب بده. به این دقت کنید لطفا. Dns برای خاموشیِ مطلقه.
پینگ و سرعتش نوسان داره، اما مقابل خاموشی‌ای که هفته‌ی اول جنگ تجربه کردیم؟
بهشته عملا.</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/MatinSenPaii/3349" target="_blank">📅 18:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3347">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EnAnoTvBsWSkCUcDLhUwdnmjBum3EJgFiR03WCUMPGmEMOFwHLn6PbOtGBc8P230xGWasexHvGNdVytYhqyKqv0xa2IKZPXgg44VwoFfWduXDsJw67kjWfFR3WXb-1IA1PzfsfTwlhYzGvlYPt1cMWe5q7xSZCfDquUX4q_dnEVCUcHVBvehavVhx1KQ4RhwQ0eYQ0IGaQuufNqXpYDDSAWODGDfw7R-DM1AIqPz9uZwQDHkYpUlSDKTvkihF6oIU4vdAuMmWSN6bAV1Nlarpve9gcyjy0aXF2TMIysfbOMVEn4DPR0pXh14WFLY8qGstotyjZKOeK1UYhbS_KhRiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DTu4c7XPXhUQ_vM81w7B9nZyrT-EM36sxzXOw8k0q372-qTausjXMlK3NS4pd_1fcNck0C2kCePl46YAx5wRDqOH3I_pAyjyEDFW4mUh1zF_HWxbPHfpwfntM13RDNOPosspjccwrOi4b7Q5hPAM_qTYjsCZXjwrZoiWwlLtDIG_66ZeWc8iorJ6WvOxYjmOLFsqJlgcd2Ul34nC-o5c-NWXu5iY_K2DtLhHd82TlJDk5NlkI02nTTnIm55U7HsgMi0BQip72wPvgwpa_USKW74td3zGiPwmhknVLhhJEJ4qUvXXyOHrQTMDN40ApLsUmndv6j_J1eFS7Q1kUpJmHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حدودا ۳۰ به ۷۰ انگار وصله توی یه سری مناطق
هم همراه اول شنیدم هم ایرانسل</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/MatinSenPaii/3347" target="_blank">📅 18:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3346">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V3-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">7.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3346" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لیست جدید 40 تایی کانفیگ‌های ویژه‌ی متد SNI-Spoof که از سرتاسر تلگرام جمع‌آوری شده و همه هم پینگ میدن</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/MatinSenPaii/3346" target="_blank">📅 18:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3345">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ببینید همراه اول میتونید وصل بشید؟
{
"LISTEN_HOST": "
127.0.0.1
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
85.9.112.219
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
www.hcaptcha.com
"
}</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/MatinSenPaii/3345" target="_blank">📅 18:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3343">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YnY0sSwIueuUncU1V51r-FIaToC5IcvJ_sGUiXq_AdFis9AIyI81DYh-_7UfdqCBz7XfbQWOiYuJmrJ1gYvsCWRQeUsewvpb05maNiw5YoVno6O5Eq3-lJsEWbZ7XTEVniGDTSruSMkDxJwfaeVAiBNe6YCSRYvJkkH0LHumdu0pMkJvpQCBFJuBvx0Hkyrb6zJszsxMwcKGKkomh0F_HtbhafAQ8c3L6SekH7g7rQEY8p5sdf7K92a49jjAkxf3CEdDHOQAblWVwyeQaIWY7xxgvYQ8mM2g1fDukC4bGi8YwH757xDGcnzlxQxKrMM24B9UzTlv0olZKCa2oKSRBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سایت خوب برای خرید سرور با رمز ارز بهتون معرفی میکنم که قیمتش حدودا فکر کنم 4 دلار بیفته با کارمزد و اینها، و میگم که چه شکلی با صرافی‌ها کار کنید و از طریق چه ارزی بخرید.
منتها نکته‌ی مهم اینه که تصور شما اشتباهه از بسته بودن دیجیتال اوشن.
دوست من الان همه چیز بسته‌ست. همه چیز
و اگر چیزی باز بود که دیگه از DNS استفاده نمیکردیم.
پس بله، شما اگر VPS بیکار داشته باشید، میتونید این رو ستاپ کنید. دوستان خارج از کشور هم میتونن واستون ستاپ کنن طبق آموزش اگر که حوصله کنن. هرچند برای تعداد بالای 255 تا، قوی‌ترین سرور هم جوابگو نیست که خب این رو هم مجددا توضیح میدم که چه کار کنید. فلگ شدن دامنه هم توسط کلودفلر و هم توسط DPI ایران رو هم همینطور</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/MatinSenPaii/3343" target="_blank">📅 16:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3342">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LK2OyrtF70EZ2k6VSJmG-yJUppiC34ddazWEWaMTos9rL5LN5xUrNfrDr6IkqDYVu8f0gYQ0WEuYkBkSQxb8D45tBNIHR6yfALXs3n2oWMdWgvEZQo2KlyKspvY9JTqqhFR_upvP6pPgluTu2MyfWU_HImo1JBOv6ayje1UdffBAP-jiV0c9cPU2sGIPrnJlmIlF7pCHOVhwUqAp-5cRCHS6JjALOBBBpt188lZBVU4nPoj4MSxXJtAN3YYo16T3yxGxZO2_OFm0QuOe528CbLf0IdX8QJ_cY4CCf5KvC3Ceo9nUtzUXOZMfXPamd0unjPxOlm4lWjDJ5QTnKIunKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصلا آموزش "برای" سرور شخصی هستش. و برای ios هم تنظیمات به همین شکله چیز متفاوتی نداره. خودم آیفونی ندارم که بشه روش یاد داد متاسفانه اما طبق آموزش پیش برید، همین مسیره</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/MatinSenPaii/3342" target="_blank">📅 16:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3341">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cySjA1pYmEp3560ZTt5v_-ZE-Bh7Z_c2esMxh2YIewTj2qH_89WiXwCIT5nn_xvHaw2HlkDn08II_D5diVhleY7p2W_ieNaagu9Cuv8xu34FjYNJ90SBLr1vXlDYYvizLquVKePwN7340WXYaHHiNJZg_79shLBi061KX94b--7mAx6np6h0-sUR4B_SI3jM63m67dGpXnCJQdimnESm17R5xGIdjWm46gkU8SHhT5QzdnPVw1j5VaYh06ISH1gIBEf3T67Q1mI7NMrBDr6yU-vfVXYGHlU-9J-73kGRq33PTdmRHux9Zf3--A_fwJLELImh9Eba0gmHRJKP421x9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ترفند جذب مخاطب نیست واقعا:)) بلکه هیجان خودم از متدیه که به شدت خفنه و میتونه ما رو نجات بده توی شرایط خاموشی مطلق
خیلیا پرسیدن که چطوری داری این سرعت رو میگیری؟ مگه میشه اصلا؟
بله میشه و توی ویدئویی  که تا شب می‌ذارمش 2-3 تا علتی که باعث میشده شما سرعت خوبی نگیرید و کندی تجربه کنید رو بهتون میگم</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/MatinSenPaii/3341" target="_blank">📅 16:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3340">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ebddd60447.mp4?token=pU3YzShT0isnCdC1Yi-DNXgSgCOIOB9PkFdWTtVunbJx1mqKf1IgDVCfuHp5S9HeVfuEMCGqLT511xm5csJD2BtinsQM90NSIiP8d8hT911NvOkWeWJaHIkL4U9a_M_g_l24MWjPE5WPJ-tQXNy7313iTFnRw47ScCh2-Srq-R3LDhp2fy96H9o8eqhzMSqj9zosKvS0M1XgxeQND8q0SsNyqhGXpsC_Rm1MYCtyXjT8FXT6AYOtnX8HpZOgooIZE8OU33x0rYhC-4ZP1LwWmzvH1Q9QNEUyUxB99D9uUN9npuYS6yiJzK62t0c2IQ7PVWrLnP9nQwwxNGxJY0PR3g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ebddd60447.mp4?token=pU3YzShT0isnCdC1Yi-DNXgSgCOIOB9PkFdWTtVunbJx1mqKf1IgDVCfuHp5S9HeVfuEMCGqLT511xm5csJD2BtinsQM90NSIiP8d8hT911NvOkWeWJaHIkL4U9a_M_g_l24MWjPE5WPJ-tQXNy7313iTFnRw47ScCh2-Srq-R3LDhp2fy96H9o8eqhzMSqj9zosKvS0M1XgxeQND8q0SsNyqhGXpsC_Rm1MYCtyXjT8FXT6AYOtnX8HpZOgooIZE8OU33x0rYhC-4ZP1LwWmzvH1Q9QNEUyUxB99D9uUN9npuYS6yiJzK62t0c2IQ7PVWrLnP9nQwwxNGxJY0PR3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حقیقتا به نظرم سرعت Master+White برای شرایطی که جنگ بود و هیچ چیزی جز DNS و کانفیگ گیگی خدا تومن کار نمیکرد، مقابل مابقی روش‌های DNS مثل Dnstt و slipstream خیلی خیلی بهتره. کما اینکه نیازی نیست در به در دنبال ریزالور بگردید به اون صورت. نیاز به اسکن و... هم که ندارید</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/MatinSenPaii/3340" target="_blank">📅 16:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3339">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d08Eoi1jMES6xUfFZb-wlUwmxBJCYKqvM3ZsOuj4kNJVO87Xl8kkhYYLPKuLbtxR16v2o7uJ733QdRoX2GyYqYRoIcpm4w3_qBEgXMkXRcJnY31nx2mIHvWY2vODOwd6U2tQB2HZ8sQUfW9ukWHWBYWM-FJrXrVriJcJIvzjCFFMmR6BjXmW1pWVlwSCsy-_JJQJ_JQP4SUs3LJrQdo1glD3WUHBAu8NZPDEutOeLklynrmM-u1AbLjoScxh1xNN8-H0aE_SGRNCznEpDWMO15Z1fyGllS1VpK3TAjdlS0ynwRgZhBFCca_KzegLJLwNF8GJOfiZPHVFJDJ3KwX4pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نزدیک به یک ساعته وصلم، کلا 100 مگ رفته
اینم برای اونایی که از ورژنای قدیمی میترسیدن که یهو دو دقیقه 200 مگ میرفت</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/MatinSenPaii/3339" target="_blank">📅 15:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3338">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">از MHR و Goose relay واقعا لذت‌بخش تره</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/MatinSenPaii/3338" target="_blank">📅 15:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3337">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این عکس‌ها و پست و همه چیز رو هم دارم الان با همین متد ارسال میکنم</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/MatinSenPaii/3337" target="_blank">📅 15:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3336">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خب دوستان، باید بهتون بگم که WhiteDNS روی سرور شخصی خداست.   با MasterDNS ستاپ کردم. که خیلی خفن تر از Storm بهم پرفرمنس داد تمام تنظیماتش رو هم ویدئو میگیرم و بهتون یاد میدم. به همراه یه لیست 6 هزارتایی ریزالور که جمع‌آوری کردم  به شدت ساده‌ست و بچه‌های تیم…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/MatinSenPaii/3336" target="_blank">📅 15:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3334">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ssuDbd975rErs2aBOQnup3ZMRL_St3eAi_cmu0K6EAMDOtePunDl1V_C2th9o8PK4JTIS_W1x_zJ-jyI05WgSAdEyIKHiZckOPHBAA0d5MSrqtNIfC1cLLW3RuuQEa98dgzhP4X80RylVHe8uP3ypJEi3u8XuJVa7qRQP9KW1kcQJwo-5aHXe1uYZFoKhNCi6jhDvmGdyJoEYVuhIdg2sevkrNoZM3oAMWdOLqarWR1PPx3JaHkHmbC9wSnq2CHLEglWnsSWNP-a3hlEfVJVMNyyvigNSXEsdmp3WilRn_ilgPkvT8O1GcEZqIHvd1zwXn-RH76HTsouRRQkZyZEbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GB7ZjZ7C88kM1o9dj4R8lYYd3AgywUv6ZdjhfatTlZgPCEWNZovVl-GCQWB0s3-yFxeElvap2DcQD-O2gzFt7yIHzSTlOIrjxxLF5bZzuXMYR77BNo0FKW2t3uPjcNW2mU8SpJztOZ2Ro8m5kufCPRiTVDhF39BE9MaT9zaQ3ZBQ2D7jxx3xSNEqCxf_Vc9uAE1jwZFEt7DWBrNuscHs1vMFV6MS7NPcm2R2hqbB-Ij-NUo5cm5_CmbbJJahs9CMdPnpJmSOUKZbQC3rNVMj3puE89xmGJibBAWT_yh4vCDl35xRZ1OdcIeK8cSBNHfQtYfWajyZFjJ9QY_pr_rX9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب دوستان، باید بهتون بگم که WhiteDNS روی سرور شخصی خداست.
با MasterDNS ستاپ کردم. که خیلی خفن تر از Storm بهم پرفرمنس داد
تمام تنظیماتش رو هم ویدئو میگیرم و بهتون یاد میدم. به همراه یه لیست 6 هزارتایی ریزالور که جمع‌آوری کردم
به شدت ساده‌ست و بچه‌های تیم در تلاش هستن ساده‌ترش هم بکنن واستون
سرعت دانلود تقریبا 500 کیلوبایت بر ثانیه. بیشتر هم میشه بسته به نت و ریزالور
اینستا راحت باز میکنه
توییتر همه چی به راحتی لود میشه
و مصرف حجم مثل ورژن‌های قبل اصلا بالا نیست</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/MatinSenPaii/3334" target="_blank">📅 15:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3333">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آموزش Goose Relay رو می‌تونید از اینجا ببینید: https://www.youtube.com/watch?v=tzjVg4O6dVs  چیزی که دیدم، روی اینترنت‌های متفاوت از بد تا خیلی عالی جوابگو بوده</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/MatinSenPaii/3333" target="_blank">📅 15:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3332">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آموزش Goose Relay رو می‌تونید از اینجا ببینید:
https://www.youtube.com/watch?v=tzjVg4O6dVs
چیزی که دیدم، روی اینترنت‌های متفاوت از بد تا خیلی عالی جوابگو بوده</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/MatinSenPaii/3332" target="_blank">📅 15:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3331">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3331" target="_blank">📅 13:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3330">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l8ychdyQG8sphmWhpfUDps3oOEygZdc0AZJzLvmm5PKrBcnqMOG8T8LSvRUM3pm6Etm_V1hhK7W447AiXNxxl3W1DTAPcaHT5BKKWKFzfbdZfDVOU_Sb5mm9x9RwCps5pr82Ju1ZlRyoP2ffRDXPvFvK_XyBfYEFCsITAG-WcQkq4DcFDquJthWQyIm1G6LA1sYi2h2vTbyfZZdaA_8n9XXTCyMcDDM2CpiWuEoNykQ6Mp5eV8HZ6NBkSbUW6nX8v42LXqGn9uwvPCDlLeaO-4Qj3uVQIteIFp0bLNmzuJqmovkSCU8sfdbs2jHu2-NzJD9NqAZfxFDW5WKSogBRjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک سری از دوستان روی مخابرات و اینترنت‌های خونگی دارن با SNI-Spoof وصل میشن مجددا. زیاد دیدم از صبح  hcaptcha.com  46.38.137.156 81.12.32.136  امتحانش ضرری نداره</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/MatinSenPaii/3330" target="_blank">📅 11:33 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
