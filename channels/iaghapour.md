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
<img src="https://cdn4.telesco.pe/file/v_RFVP3X5c4J6MD8CRqKkGZRzLlX3rGQ7PpblOym8hG5uojP71BglxlE_at7d9e4HqJx17zA0ZgDrmxmj6vgzzfu4vERa0uk9SALGN2qx9Uz_zzOhP5VeaWAqqYidEFS09OUBGlkNuiGLKCBmGb9v5GrltXYHHEPSSga3SDdZxA8Quj3szvbSdvsw58aP3vHz3Zyc-0NC8GnJEV7l2jJN-nJpFUu_iDq3j8X4J4dtednJpeYKZO8MM5CB0IjPBdDnhg5juzbLv6UK_PG8kXmoFSsJC_EHVovc_8xW16ufRvjJwuAWHaxx0RVJWWtqGIv5c-1hIT2Ov-Gh_AwHIFE7Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 51.9K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 23:51:20</div>
<hr>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔻
این روزا انقدر شایعه و خبر بی‌خود درباره وصل شدن اینترنت پیچیده که واقعاً حس و حال خبر زدن در موردش رو ندارم.
با این حال، سعی می‌کنم اسکریپت‌هایی که زحمت کشیدید فرستادید رو حتماً بررسی کنم، به هر حال از دست رو دست گذاشتن که بهتره. راستش با این وضع زندگی، اصلاً هیچ انرژی و انگیزه‌ای برای آدم باقی نمونده.</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/iaghapour/2630" target="_blank">📅 21:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2629">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMegaCenter22</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BByeSNcHh0tmGQPyckD_YzGgjb8AiQF_1ZnoNWghq88IGG23Roi8G5DZja2uYpYx81ZTSFWq6B4BBWuOpU8EdSaqOTtGXA-LSv2jBg-7jYZuyukYklQhtDSkrazxmnRqlHExvgkzvc0q5bjFj2uf8iPn-yhyuZPGzqdX_YIeW3DtbyVk1uxw2pQ7bNVDJ_jGMYI3EOuDysxqo9TcyYK4qOMjKdCeMZUO6B8_d0yQIjZdYG_5dp3_PBAoD8hkZXy5OLcK_ZHlZiFeAqh6sEtvPWV6AwZy1OzDCn2Yl_Ls7-05fmr-ABI4dI3rVtmWoY6e3J_uCdUEpCyzatzCx0WzAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💠
Mega Center
💠
🪩
📈
ابزار مورد نیاز شما در دنیای کریپتو و تریدینگ / احراز هویت پلتفرم های خارجی
از افتتاح حساب های ارزی بین المللی
تا پکیج مدارک لازم جهت احراز هویت صرافی ها و سایت های خارجی
صدور مستر کارت و ویزا کارت و خدمات
ارزی
سیم کارت های فیزیکی خارجی
خدمات وریفای تضمینی صرافی ها ، سایت های فریلنسری و گیمینگ
اکانت های اماده دیتاسنترها
آیپی رزیدنتال اختصاصی
اشتراک ویندسکرایب و ...
👨‍💻
لینک دسترسی ها و ارتباط :
www.megacenterx.com
www.megacenterx.com
www.megacenterx.com
https://t.me/megacenter0
https://t.me/megacenter0
@Megav_admin22
@Megav_admin22
در صورت بالا نیامدن سایت ، بدون وی پی ان امتحان نمایید
✅
سایت دارای اینماد و درگاه پرداخت اختصاصی و کریپتو
✅</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/iaghapour/2629" target="_blank">📅 20:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyLZbKfPbNG_o8Uo-Jvxdb-ZfE8-1NwboIYHc7673BhIqjeDf4uADOkxdjN2PJO6DhAfhoDb7AxbTghPn5cIpIbIr5O9vX1MTUCA_dyihqr_n7MstWVc6m4UV8gvSt3zuhcNofEFj1Wq7jKlGT4mnA-3deuzeWpZsvyIbkpDg3pGxfkhod6kg-xSCtIG93ESw5nlI0_U422UySrhWEtHUii1oz0OiTcSRZi7TV6hVhu6cUnA0KgTQ3dWSM2WbT2_LC0S3PRW5yhUhNZVGvUBwg_Ll8Aa5xcZVyk7_RpKU3BLfKLesKpNIGTpBZi4XpRYnW1GkuHqCw6hNDlFKc3h5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت جدید کلاینت اندروید GooseRelayVPN
🔹
این مخزن، کلاینت اندروید GooseRelayVPN است که هسته GooseRelay را از طریق Go mobile اجرا می‌کند و رابط کاربری کامل برای مدیریت VPN، پروفایل‌ها، لاگ‌ها و تنظیمات ارائه می‌دهد.
🛠
پایداری و رفع کرش
‏
🌐
رفع کامل لو رفتن آی‌پی (IPv6 Leak) با موتور جدید tun2socks gVisor FakeDNS.
‏
🎛
پیاده‌سازی کامل Quick Settings Tile.
‏
📊
نمایش کاملاً دقیق سرعت و حجم مصرفی.
‏
🗂
اضافه شدن حالت Bypass به بخش Split-Tunneling.
‏
❄️
رفع فریز شدن برنامه در پس‌زمینه.
‏
📜
اصلاح پرش ناگهانی اسکرول لاگ‌ها و بازطراحی کارت وضعیت اتصال در صفحه Home
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/iaghapour/2628" target="_blank">📅 20:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⭕️
رکورددار تاریکی دیجیتال: ایران طولانی‌ترین قطعی اینترنت جهان را تجربه می‌کند!
روزنامه معتبر اسپانیایی «ال‌پایس» در گزارشی تکان‌دهنده اعلام کرده است که ایران با گذشت حدود ۸۰ روز خاموشی دیجیتال، رکورد طولانی‌ترین قطعی سراسری اینترنت در تاریخ یک جامعه دیجیتال را به نام خود ثبت کرده است. این محدودیت‌ها که ابتدا با توجیه شرایط امنیتی و جنگی آغاز شد، همچنان ادامه دارد.
طبق گزارش این رسانه و به نقل از نت‌بلاکس، این وضعیت حالا حتی از قطعی طولانی‌مدت اینترنت میانمار در سال ۲۰۲۱ نیز فراتر رفته و زندگی میلیون‌ها ایرانی را در بن‌بست قرار داده است:
🔹
آوارگی برای یک اتصال پایدار:
ال‌پایس داستان تلخ افرادی را روایت می‌کند که برای حفظ شغل خود مجبور به مهاجرت موقت شده‌اند. مانند معلم زبانی که برای رهایی از اضطراب قطعی اینترنت، با هزینه ۴۰۰ دلار در ماه به زیرزمینی تاریک در ارمنستان پناه برده است.
🔸
ضربه مهلک به کسب‌وکارهای زنان:
تداوم این اختلالات، آسیب‌های ویرانگری به مشاغل کوچک وارد کرده است؛ به‌ویژه کسب‌وکارهایی که توسط زنان اداره می‌شوند و حیات آن‌ها کاملاً به پلتفرم‌های آنلاین و شبکه‌های اجتماعی گره خورده بود.
🔹
فلج شدن زندگی روزمره:
از کار از راه دور و تبادلات مالی گرفته تا ساده‌ترین ارتباطات انسانی و دسترسی به اطلاعات، همگی تحت تأثیر این محدودیت‌های بی‌سابقه مختل شده‌اند.
گزارش این روزنامه نشان می‌دهد که جهان در حال تماشای انزوای دیجیتال جامعه‌ای است که شهروندانش برای دسترسی به ابتدایی‌ترین حق ارتباطی خود، ناچارند هزینه‌های سنگین روانی، مالی و حتی مهاجرتی بپردازند./ دیجیاتو
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/iaghapour/2627" target="_blank">📅 16:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uo281RikOJsoIDez8CxKb1k6R1IHrpNthDKaPaWYm2kmwdEbVrd6LfHcGnDX8cDT9laWBFDeJ7oqqXeNDjsU0lgYFj9Q-1lBp1lmRWaVCGpN0uNbxJ7Sz4_S4OO76tpbfanEtrSV4OvmVtbLXjS5M0q4MAnjeueCOU-2_U5MlXxsClYensls9X9LIkMIhN1yuD19miK6JUgaLRBrYRBz1W5V7iz-OHUpgmIEQ6Nl9hUT3vr6rLD_XEQDoBHmx08QKobv0vPMFZQnONfkc70IdgPMjnhgM8VI77cUePuErEpJEKWwfqUCYGReKGGF9rADJmjPs-uIZUPcEzE4BzrKOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پروژه XPlex؛ راه‌حل هوشمندانه برای جلوگیری از قطعی و پکت‌لاس کانفیگ
اگر از کانفیگ‌های v2ray استفاده می‌کنید و پایداری اینترنت در کارهای حساسی مثل آزمون‌های آنلاین، جلسات ویدیویی یا ریموت‌ورک برای شما حیاتی است، پروژه جدید XPlex یک راه‌حل فنی و کاربردی برای شما دارد.
منطق این اسکریپت ساده اما بسیار کارآمد است و به شما کمک می‌کند تا یک اتصال بدون قطعی را تجربه کنید:
🔹
استفاده هم‌زمان از چند کانفیگ:
منطق کلیدی این پروژه این است که اگر چند کانفیگ v2ray داشته باشید، اسکریپت به صورت هم‌زمان از آن‌ها استفاده می‌کند و ترافیک شما را روی کانفیگی می‌اندازد که کمترین پینگ ممکن را دارد.
🔸
خداحافظی با پکت‌لاس و تایم‌اوت:
این ابزار برای افرادی که کارهای حساسی دارند و ثانیه‌ها برایشان مهم است طراحی شده؛ مثل شرکت‌کنندگان در آزمون‌های آیلتس آنلاین، جلسات کاری با خارج از کشور و...
🔹
هزینه مصرف حجم:
باید توجه داشته باشید که به دلیل ماهیت کارکرد این ابزار، مصرف ترافیک و حجم v2ray شما تقریباً دو برابر خواهد شد که بهای به دست آوردن یک اینترنت کاملاً پایدار است.
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/iaghapour/2625" target="_blank">📅 20:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⭕️
نماینده مجلس: ۹۰ درصد مردم با قطعی اینترنت مشکلی ندارند!
علی یزدی‌خواه، نایب‌رئیس کمیسیون فرهنگی مجلس صراحتاً اعلام کرد که اینترنت جهانی فعلاً بازگشایی نخواهد شد و مسئولان به این نتیجه رسیده‌اند که اتصال مجدد آن به صلاح نیست. او مدعی شده که با پلتفرم‌های داخلی، احتیاجات اکثریت جامعه برآورده شده است!
این اظهارات نشان‌دهنده اصرار بر ادامه سیاست اینترنت طبقاتی و نادیده گرفتن نارضایتی‌های عمومی است:
🔹
انکار نارضایتی‌ها:
این نماینده مدعی است به عنوان نماینده مردم، مراجعات مکرری برای اعتراض به قطع اینترنت نداشته و ۹۰ درصد مردم هیچ مشکل عمده‌ای با این وضعیت ندارند!
🔸
رسمیت یافتن اینترنت پرو:
به گفته او، تا کنون به بالغ بر یک میلیون نفر از افرادِ واجد صلاحیت (مثل تجار و دانشگاهیان) دسترسی به «اینترنت پرو» داده شده و هر قشری که نیاز داشته باشد هم می‌تواند آن را پیگیری کند.
🔹
کوچ اجباری به پلتفرم‌های داخلی:
او مدعی شد که ترافیک شبکه‌ها نشان می‌دهد بیشتر کسب‌وکارها به پلتفرم‌هایی مثل روبیکا و سروش کوچ کرده‌اند و تنها یک «اقلیت ناچیز» باقی مانده‌اند که آن‌ها هم بستر مشخصی برای پیگیری دارند.
در حالی که مسئولان از پایداری وضعیت فعلی و رضایت مردم سخن می‌گویند، بخش بزرگی از جامعه، کسب‌وکارها و متخصصان، اینترنت طبقاتی و محدودیت‌های فراگیر را تلاشی برای حذف کامل دسترسی آزاد به دنیای دیجیتال می‌دانند. / زومیت
پ.ن: اینا نماینده کدوم مردم هستن؟ 90 درصد مشکل ندارن؟ عجب!
حالا فارق از اینکه این ادعا از اول تا آخر دروغ هستش ولی من قبلا هم خواهش کردم اگه مجبور نیستید وارد شبکه های داخلی نشید! اگه مجبور نیستید لطفا سیم‌کارت پرو نخرید! اینا واقعا فکر میکنن مردم به ایتا و بله علاقه دارن! متوجه نیستن خیلی ها به اجبار مهاجرت کردن! در غیر اینصورت کی این اپلیکیشن ها رو به تلگرام و اینستا ترجیح میده؟
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/iaghapour/2623" target="_blank">📅 19:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔻
دوستان عزیزی که درخواست معرفی افراد معتبر برای خرید فیلترشکن دارید؛ طبق بررسی و نظرسنجی که در
این پست
قرار دادیم، با چندین نفری که از سال‌های قبل همکاری داشتیم صحبت کردیم و ازشون یکسری درخواست‌ها داشتیم؛ از جمله ضمانت بازگشت پول و اینکه مبلغی رو به عنوان ضمانت پیش ما بگذارند.
به همین دلیل ۹۰ درصدشون قبول نکردن و فقط تعداد محدودی پذیرفتن که هفته پیش یکی از اون‌ها رو بهتون معرفی کردیم. بازم اگه کسی از افراد قدیمی شرایط ما رو قبول کنه حتماً معرفی می‌کنیم.
افرادی که به ما تبلیغ می‌دن می‌دونن چقدر تو تبلیغات سخت‌گیر هستیم حالا در هر موضوعی باشه. بیش از ۳۰ درصد کسانی که پیام می‌دن، چون کانال قدیمی یا کاربر زیادی ندارن یا سایت معتبری ندارن، با نهایت احترام تبلیغشون رو اصلاً قبول نمی‌کنیم.
🔹
با این حال بازم سعی می‌کنیم همین یکی دو تا فردی که می‌شناسیم و شرایطمون رو قبول کردن بهتون معرفی کنیم؛ البته اگه خودشون دوباره قبول کنن تبلیغ بدن :)
ممنون میشم افراد جدید برای تبلیغات در زمینه فیلترشکن فعلاً پیام ندن. شرایط رو کامل در
این پست
براشون توضیح دادیم.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/iaghapour/2622" target="_blank">📅 21:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⭕️
اعتراف رسمی دولت: ۷۰ درصد مطالبات مردم، رفع محدودیت‌های اینترنت است
معاون اجرایی رئیس‌جمهور صراحتاً اعلام کرد که طبق نظرسنجی‌های نهاد ریاست‌جمهوری، بیش از ۷۰ درصد گلایه‌ها و خواسته‌های مردم به محدودیت‌های اینترنت مربوط می‌شود. او تأکید کرد که سیاست پایدار کشور نباید بر مبنای فیلترینگ باشد.
نکات کلیدی سخنان معاون رئیس‌جمهور درباره وضعیت اینترنت:
🔹
تصمیمات اضطراری باید تمام شوند:
محدودیت‌های اخیر به دلیل شرایط خاص امنیتی و جنگی بوده، اما تصمیمات دوران اضطرار نباید دائمی شوند و سیاست پایدار کشور نمی‌تواند بر محدودسازی بنا شود.
🔸
اعتراف به شکست فیلترینگ:
تجربه عملی نشان داد محدودیت‌های فراگیر ارتباطی به نتایج مورد انتظار منجر نشده و استفاده گسترده از فیلترشکن‌ها اثربخشی این محدودیت‌ها را از بین برده است.
🔹
حق آگاهی مردم:
اعتماد عمومی مهم‌ترین سرمایه است و مردم حق دارند بدانند محدودیت‌ها بر چه مبنایی اعمال می‌شود، چه دامنه‌ای دارد و تا چه زمانی ادامه خواهد داشت.
به گفته قائم‌پناه، کشور به یک تفاهم ملی در حوزه ارتباطات نیاز دارد؛ چرا که آینده ایران متصل و فناورانه است و دسترسی پایدار به اینترنت، پیش‌شرط تحقق این آینده خواهد بود./ زومیت
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/iaghapour/2621" target="_blank">📅 17:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fydAuTYc_fes1H_3Zkx7aie-4ZJ7un4O2Vgi4mDUl6SmeRemTHGIU0ctbzwQfKmjKlcA8LLjSKrD3jDqMMsFzFyws6L6Yphg8P9zVMnmm_CGmyXFrUjfBOx3is-B34eyhM4wyz4dw9bplkwFoEM3bOvnbpORMDkZPDxYEi3jWZYFV87WDyaWGhy8dS_QQ7kfEeUKC8xUO5LiH6ZTsj-BMDsZYcxov_IzoDoJ6z4y9IVRH6FUBmdChlYHd-vTcNd1T6Ey4NLVHTAaznc_CakZQ0W5K9HRKIESC38_ydL2aKLrLk-Uy9ar4vY19mjhdZ6yLwdrLsBxfBvh1r_EHtfY2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
بحران خاموشی دیجیتال؛ ضربه‌ای جبران‌ناپذیر بر پیکر اقتصاد و جامعه
🔻
بیش از ۱۹۴۴ ساعت خاموشی دیجیتال، تنها قطع یک ابزار ارتباطی روزمره نیست، بلکه یک «بحران تمام‌عیار اقتصادی و اجتماعی» است. در زمانه‌ای که در سراسر جهان حتی چند دقیقه اختلال در اینترنت زیان‌های هنگفتی به بار می‌آورد، تداوم ۸۲ روزه این وضعیت در ایران، آسیبی عمیق به شریان‌های حیاتی کسب‌وکارها و زندگی عادی مردم وارد کرده است.
در واقع، تداوم این قطعی طولانی‌مدت نشان می‌دهد که حفظ حیات اقتصادی مشاغلِ وابسته به فضای مجازی و نیازهای ارتباطی جامعه، در اولویت تصمیم‌گیری‌ها قرار ندارد؛ رویکردی که پیامدی جز نابودی معیشت هزاران نفر، فرسایش سرمایه اجتماعی و آسیب جدی به بدنه نوپای اقتصاد دیجیتال کشور نخواهد داشت.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/iaghapour/2620" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMtKr0fRwgQF8ZI5Z-rQ6wkWflSDCtgbJahgO5osIGKUBviA4NDPCMjO_yFIm0qVxnwT4EYE9cMtAsQhBSG0g0kP0rqQ7nTjapqs77qHeHoloDC1kqL1Z_91tqs8aWQyCQy08C0zSAdHKW1wBTqKvWRNM1mBf1q6ED3_bMCMU3h99_RcVdtoVB2mL5IuUxbCMLUF1XtKwuNpSmaIiO7tUsjbvjqc9-RvQLniAS35RUT3ChcuTEZXd6mFgsuIA7p-HnzM9zYvnA5q56NHbojkBg8Rk3cg6OB03l713iF1ALPpMGss7k5AqU_VkhE4MApdq5MxCHuLIJhDfTEzh1czxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
شگفتی گوگل در Google I/O 2026؛ معرفی جمینای ۳.۵ فلش با سرعتی باورنکردنی!
در گام نخست، مدل جمینای ۳.۵ فلش عرضه شده است؛ مدلی که با وجود طراحی شدن برای سرعت بالا و هزینه کم، در کمال شگفتی توانسته مدل‌های پرچمدار و پرو نسل‌های قبل را در بنچمارک‌های تخصصی شکست دهد.
🔹
پادشاهی در بخش ایجنت‌ها:
این مدل با توانایی برنامه‌ریزی بالا، می‌تواند چندین ایجنت را به صورت موازی برای پیشبرد پروژه‌های پیچیده و کدنویسی مستقر کند.
🔸
سرعت خیره‌کننده و کاهش هزینه‌ها:
ساندار پیچای اعلام کرد این مدل با سرعت پردازش ۲۸۹ توکن در ثانیه، حدود ۴ برابر سریع‌تر از رقباست.
🔹
شکست رقبای سرسخت:
جمینای ۳.۵ فلش در آزمون‌های تخصصیِ مربوط به کارهای ایجنتی، امتیاز بی‌نظیر ۱۶۵۶ را کسب کرده و عملاً رقیب سرسختی مثل کلود سونیت ۴.۶ آنتروپیک را پشت سر گذاشته است.
🔸
همچنین نسخه قدرتمندتر یعنی جمینای ۳.۵ پرو در ماه ژوئن ۲۰۲۶ رسماً عرضه خواهد شد.
جمینای ۳.۵ فلش هم‌اکنون به عنوان مدل پیش‌فرض در اپلیکیشن جمینای و بخش سرچ گوگل فعال شده است.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/iaghapour/2619" target="_blank">📅 09:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9VvL0K1mOZiJBo_umufvcu14w1127LPSNUFSBhEQj59YNJqILke_OZKK6o5a27dwkb3oSyf5DRsyjnBiwn6QwTRAS3N4LDL30rDz5N3zSbqUndA7gbuWl1h1ddIuRCdCDbtTY1qS50sCW-wxLHv2NoWoejjNwHu_fmXrIK4-OD4k99OscONY2kaYgz3LqpZDOCqdH_shPTmiPdZUXSFem1gFfQ-RncfAK1wEzjDb8PJcIaq-tWj8GXnYY_SvPnvz__m8YU24K7OGlEjefUa0LAg3PxhCl4bOpBOqoly9MOKKyq8Xtgwfbsmwkv-hQSdCMx72-9cP1QI2Z5fgNMWVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دیگه پول فیلترشکن نده! آموزش ساخت فیلترشکن شخصی و رایگان با سرعت بالا
😎
🔹
در این آموزش قدم‌به‌قدم بهت یاد می‌دم که چطور بدون نیاز به دانش خاصی، یک فیلترشکن (VPN) شخصی، امن و کاملاً رایگان برای خودت بسازی. این روش روی تمام اینترنت‌ها جواب می‌ده و سرعت خوبی برای تماشای یوتیوب، وب‌گردی و … داره.
🔗
تماشا ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
#آموزش
#فیلترشکن
#رایگان
#novaproxy
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/iaghapour/2618" target="_blank">📅 16:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">از هر 10 نفری که که تو اینستاگرام وصل هستن 8 تاش دختره, 2 تاش هم پسر کانفیگ فروش
🥸</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/iaghapour/2617" target="_blank">📅 17:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAN_B3i80ingG8zIvRD2YPGgz0INLlVF2knVFtk46tYPV0FSdef57bHXhZ2ORXPSkUUM5gshrtZ_1-VGtmmAjSdZ7JjcmSk9j2klTI0plM_MG6T7lDOHZCY4a0j1Y0IcvTzB8ulx5VCYiwNWLh7jSLg7VJwh3STQxEtbNqd6kbwPxiWVc5dmsHpsbrbLz9wtIy3TNKcVAhHIQXHyi1JQHOvDkbWudKJh5GrcyLfFuJ5YEEcsqc8gR_8qdqcdF3Fq4wKdmv8E7bIfkL_4HhQBRphAgcQuVPPR53sAuOb78O0g2kSEf-T9pbT9hlhUHyR2-s_qsq2SSdzhWrw2HLFt6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش نصب ساده و آفلاین 3X-UI روی سرور ایران + SSL (+ معرفی قابلیت های جدید)
🔹
در این ویدیو به سراغ یکی از بزرگترین چالش‌های این روزها رفتیم: نصب پنل 3X-UI روی سرورهای ایران همراه با سرتیفیکیت به صورت کاملاً آفلاین و بدون نیاز به اینترنت آزاد! همینطور سعی کردیم یک معرفی ساده از قابلیت های جدید این پنل داشته باشیم.
🔗
لینک ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
#آموزش
#فیلترشکن
#پنل
#xui
#3xui
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/iaghapour/2615" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⭕️
بحران در زیرساخت فناوری؛ سقوط درآمدها و خطر عقب‌ماندگی ۱۰ ساله!
اختلالات اینترنتی دیگر فقط یک مشکل ساده برای کاربران عادی نیست؛ بلکه به گفته رئیس کمیسیون شبکه سازمان نصر، تیشه به ریشه‌ی زیرساخت‌های فناوری کشور زده است. این وضعیت نه تنها درآمد شرکت‌ها را تا ۷۰ درصد کاهش داده، بلکه باعث فرار متخصصان کلیدی و فرسودگی شدید تجهیزات شده است.
🔹
سقوط درآمد و انفجار هزینه‌ها: شرکت‌های حوزه شبکه با کاهش درآمد ۳۰ تا ۷۰ درصدی روبرو هستند. از سوی دیگر، به دلیل اختلال در مسیریابی و افت کیفیت، این شرکت‌ها مجبور به پرداخت جریمه‌های سنگین ناشی از نقض توافق‌نامه سطح خدمات (SLA) شده‌اند.
🔸
تهدید امنیت سایبری: محدودیت دسترسی به مخازن اصلی و سرورهای به‌روزرسانی جهانی، ریسک نفوذ و حملات سایبری را تا ۴۰ درصد افزایش داده است. در واقع، امنیت سایبری قربانی ناپایداری شبکه شده است.
🔹
تخلیه ژنتیکی تخصص: صنعت شبکه با بحران خروج نیروهای کلیدی مواجه است. تربیت یک متخصص ارشد سال‌ها زمان و هزینه‌ی ارزی سنگین می‌طلبد که با مهاجرت این افراد، سرمایه‌های انسانی چند میلیاردی کشور به راحتی از دست می‌رود.
🔸
عقب‌ماندگی ۱۰ ساله: ادامه این وضعیت، ایران را با شکاف تکنولوژیک ۱۰ ساله نسبت به کشورهای منطقه مواجه می‌کند؛ شکافی که در فضای پرشتاب فناوری، جبران آن تقریباً غیرممکن خواهد بود.
زیرساخت شبکه کشور به جای اتصال طبیعی به اینترنت جهانی، در حال حرکت به سمت یک ساختار جزیره‌ای و فرسوده است. اگر ثبات پیش‌بینی‌پذیر به این فضا بازنگردد، شرکت‌های بزرگ فناوری به اپراتورهای ساده تجهیزات قدیمی تنزل پیدا خواهند کرد. / دیجیاتو
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/iaghapour/2614" target="_blank">📅 10:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQcd0Jh-EICZWFa46rw21yaTyz09Y-IiZswIn_sfg-5QE4HLUckhU9iggjRQnbFgCUh8T1jXp-lpJ7auDBgiubPtGXP5eo_Zdj8-49iUwyclZuCkjhFVvKmSXv6Ii3MEzcGTO8jerAEr-8MjeUAWXEHm_AhUAVZWrMqloE3fEy8D7aAcjIt6ZVehHijv8avua5Ek_XWklMXRDF50SXHzDEblnWLUzKoVI0-5cHBCa86FHog9o3Y6GHMcMYMSAqPOOjmy2ekHklShRyiYne3-xrvNYQlz6ulu8M_5HFr0totNj1e80TsNNGsxkmP84_xdiyWg_1k5IV1dh88_8tj7Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
حرف‌زدن درباره‌ی قطعی
#اینترنت
شاید فوری اینترنت را برنگرداند؛ اما
#سکوت
دقیقاً همان چیزی است که ادامه‌ی این وضعیت به آن نیاز دارد.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/iaghapour/2613" target="_blank">📅 22:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کل ریپازیتوری گیت هاب علیرضا که شامل X-UI و S-UI میشد بسته شده و هنوز دلیلش مشخص نیست.</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/iaghapour/2612" target="_blank">📅 17:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کل ریپازیتوری گیت هاب علیرضا که شامل X-UI و S-UI میشد بسته شده و هنوز دلیلش مشخص نیست.</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/iaghapour/2609" target="_blank">📅 19:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔻
سوپراپلیکیشن ایتا اعلام کرد امکان ارسال فایل تا حجم ۲۰ مگابایت مجدداً برای همه کاربران فراهم شده است!
کاش تلگرام بیاد از شما یاد بگیره :)
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/iaghapour/2608" target="_blank">📅 12:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✍🏻
دوستان عزیز، همون‌طور که احتمالاً متوجه شدید، در یک هفته گذشته به دلایل مختلفی فعالیت ما کمتر شده.
🔹
در این مدت پیام‌های زیادی داشتیم که درخواست آموزش «روش جدید سنایی» رو داشتن. وقتی بررسی کردیم، متوجه شدیم خود ایشون زحمت تهیه ویدیوی آموزشی رو کشیدن؛ بنابراین نیازی به آموزش مجدد  نبود.
🔸
برای اطمینان بیشتر، این آموزش رو به چند نفر از دوستان دادیم تا تست کنن. بیشتر افراد موفق به اجرا نشدن، اما یکی از کاربران تونست متصل بشه. طبق بررسی‌های ایشون، این روش به‌شدت به رنج آی‌پی‌ها (هم سرور ایران و هم خارج) وابسته است. مشکل اصلی اینجاست که بعد از اتصال و مصرف حجم کمی از اینترنت، ارتباط قطع می‌شه و باید آی‌پی رو عوض کرد؛ هرچند آی‌پی قبلی بعد از ۱ تا ۲ ساعت دوباره قابل استفاده می‌شه.
🔻
متأسفانه در این بین، عده‌ای بدون این‌که تست درستی از پایداری تانل بگیرن، شروع به آموزش کردن که نتیجه‌اش فقط ضرر مالی برای کاربران بوده. چون کاربرا رفتن سرورهای گرون قیمت رو خریداری کردن که البته تعداد این افراد اصلا کم نبوده. (نمونه‌اش رو در عکس ضمیمه می‌بینید).
🟢
در مجموع، به نظر می‌رسه این روش هنوز پایدار نیست، اما از بچه‌های تیم خواستیم تست‌های بیشتری روش انجام بدن. اگر خودتون هم مایلید آموزش رو ببینید، می‌تونید مستقیماً به کانال یا گروه سنایی مراجعه کنید.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/iaghapour/2607" target="_blank">📅 22:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⭕️
خلاصه اخبار چند روز گذشته
🔸
اینترنت بین‌الملل به گیمرها ارائه می‌شود؛
ثبت درخواست در سامانه همگرا (اینترنت طبقاتی)
🔹
دولت و مجلس به دنبال حمایت تازه از پیام‌رسان‌های داخلی (رانت و فساد جدید)
🔸
نماینده مردم تهران در مجلس:
درباره خسارت‌های قطعی اینترنت جوسازی می‌شود. (حرف بیخود)
🔹
معاون رئیس‌جمهور:
اینترنت بین‌الملل حتما وصل می‌شود؛ دولت قصد دائمی‌کردن محدودیت‌ها را ندارد. (حرف الکی)
🔸
برآورد انجمن بلاکچین: خسارت ۳۰۰ تا ۷۰۰ هزار میلیاردی از قطعی اینترنت.
🔹
معاون رئیس جمهور: محدودیت حجم و گرانی اینترنت پرو برای جلوگیری از استفاده غیرضروری است. (عجب بابا عجب)
🔸
قطع اینترنت به هفتاد و پنجمین روز خود رسید.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/iaghapour/2606" target="_blank">📅 18:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYQ2WYYZ819looCTPu9n8aB0DWgsOeTuuUxvFYBCWRhKitd9TBEqO2acMijQim1xVvVv-hUrHnRB6gW7htc9y1-Hv9rIeMY_WxTgG2itot2X7I1won1h_qAGCUY1R44F5Nb5PfE4bm8CDkEa1V1dBigUoug0rEz-MeKkZAfrxM9c88DBkHBCgMWi6YPtYHjiKXu6CKxRa9-rvHOobm1TB-lgamwB_kjtteVHoMr-HZkE1i71UA9JrLkV3g3Stk4JXn_0bmR5xJCTYXDzp2sDEje-mI225maDfH9DeuWP-eh14a2PXHg07of0aOghGlaw90ATGlP8zYHBg6oBMuEEBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
با اپ TunnelX در ویندوز از قابلیت Split Tunneling استفاده کنید.
🔹
اپ TunnelX برای زمانی ساخته شده که کاربر نمی‌خواهد تمام ترافیک سیستم از وی‌پی‌ان عبور کند. با این برنامه می‌توان فقط برنامه‌هایی مثل مرورگر، تلگرام، ابزارهای توسعه یا برنامه‌های مشخص دیگر را وارد تونل کرد و بقیه ترافیک سیستم را روی اینترنت عادی نگه داشت. همچنین در صورت نیاز، حالت Full-route برای عبور کل سیستم از تونل در دسترس است.
🔗
دانلود اپ از گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/iaghapour/2605" target="_blank">📅 14:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✍
آدم راننده شوتی باشه به مراتب اضطرابش كمتر از کسیه كه شغلش تو ايران به اينترنت وابسته هستش...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/iaghapour/2603" target="_blank">📅 21:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2602">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚀
آپدیت بزرگ و انقلابی پنل 3x-ui (نسخه‌های 3.0.0 و 3.0.1)
بالاخره یکی از مهم‌ترین آپدیت‌های پنل محبوب 3x-ui منتشر شد! در این نسخه‌ها شاهد بازنویسی کامل رابط کاربری، اضافه شدن قابلیت‌های مدیریتی کلان و بهبودهای چشمگیر امنیتی هستیم.
🌐
۱. بازنویسی کامل و سریع‌تر شدن پنل (مهاجرت به Vue 3)
رابط کاربری از پایه بازنویسی شده است! این یعنی سرعت لود بسیار بالاتر، طراحی مدرن‌تر، صفحه لاگین جدید و بهبود چشمگیر تم دارک.
⚡️
۲. آمار زنده و در لحظه
: با جایگزینی سیستم قدیمی با
WebSocket
، از این پس تمام آمارهای داشبورد، مصرف حجم کلاینت‌ها و وضعیت سرور به صورت «زنده» آپدیت می‌شوند و دیگر نیازی به رفرش کردن صفحه نیست!
🌍
۳. مدیریت چند سروره (Multi-Node Deployment) -
🌟
ویژگی طلایی
یکی از مورد انتظارترین قابلیت‌ها اضافه شد! حالا می‌توانید از طریق یک پنل مرکزی (Manager)، کانفیگ‌ها و اینباندها را روی چندین سرور دیگر (Remote Nodes) مستقر و مدیریت کنید.
📱
۴. رابط کاربری کاملاً سازگار با موبایل
: داشبورد، لیست کلاینت‌ها و بخش لاگ‌ها حالا به صورت "کارتی" و کاملاً بهینه برای نمایشگرهای موبایل طراحی شده‌اند تا مدیریت پنل با گوشی بسیار راحت‌تر شود.
⚙️
۵. خداحافظی با کدهای JSON و تنظیمات آسان‌تر
فرم‌های ساخت کانفیگ (Inbounds) کاملاً ساختاریافته و گرافیکی شده‌اند. دیگر برای تنظیمات پایه نیازی به دستکاری JSON خام نیست (البته تب Advanced برای حرفه‌ای‌ها همچنان وجود دارد). همچنین مدیریت DNSها بسیار پیشرفته‌تر شده است.
👥
۶. مدیریت گروهی کلاینت‌ها (Bulk Actions)
امکان انتخاب گروهی  کلاینت‌ها برای حذف یا اعمال تغییرات اضافه شده که کار ادمین‌ها را بسیار راحت می‌کند.
🛠
۷. امکانات جدید Xray و Outboundها
اضافه شدن پروتکل Loopback، دکمه
Test All
برای تست همزمان همه Outboundها و ارائه گزارش دقیق از تایم‌اوت‌ها، و همچنین خاموش شدن امن هسته Xray.
🔒
۸. ارتقاء امنیت و نصب راحت‌تر
➖
اضافه شدن سیستم امنیتی CSRF Protection برای جلوگیری از حملات.
➖
اضافه شدن گزینه
skip-SSL
در اسکریپت نصب (بسیار کاربردی برای کسانی که از ریورس‌پروکسی یا تانل استفاده می‌کنند و نیازی به سرتیفیکیت روی خود سرور ندارند).
➖
اضافه شدن صفحه مستندات API (API Docs) در داخل خود پنل برای برنامه‌نویسان.
و بسیاری از تغییرات دیگه که میتونید در
این لینک
مطالعه کنید.
💡
نکته:
برای تجربه این تغییرات فوق‌العاده، پیشنهاد می‌شود هرچه سریع‌تر پنل خود را آپدیت کنید. (توصیه همیشگی: قبل از آپدیت بکاپ فراموش نشود!)
✍🏻
با تشکر از ثنایی عزیز.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/iaghapour/2602" target="_blank">📅 18:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⭕️
عصبانیت سخنگوی دولت از انتقاد خبرنگاران از قطع اینترنت
فاطمه مهاجرانی در نشست خبری امروز خود به اعتراض خبرنگاران بابت ادامه قطعی اینترنت واکنش نشان داد.
سخنگوی دولت گفت: «در شرایطی که رئیس جمهور آمریکا اعلام می‌کند آتش بس به دستگاه تنفس مصنوعی وصل است، پاسخ شما چیست؟ کشور در جنگ است. بپذیریم که ویژگی جنگ، امنیت مردم است.»
✍🏻
پ.ن:  خانم مهاجرانی اگه دوباره عصبی نمیشید خواستم بگم کاش به فکر امنیت اقتصادی مردم هم بودید! کاش به فکر امنیت ذهنی و روانی مردم هم بودید! کاش یه فکری برای چند میلیون آدمی که با قطعی اینترنت بیکار و ناامید کردین هم بودید!
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/iaghapour/2601" target="_blank">📅 14:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔻
نمیتونم خبر رو تایید کنم ولی میگن:
— افغانستان اینترنت 5G آورده.
— عراق تلگرام رو رفع فیلتر کرده.
— سوریه هم که ویزا و مستر کارت و...
این که ما درگیر فیلترینگ مسخره هستیم واقعا گریه داره...</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/iaghapour/2600" target="_blank">📅 09:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سلام خواستم یه نکته کوچولو بگم
فقط بحث کسب و کارهای کوچیک نبود
فقط بحث آنلاین شاپ ها نبود
ماهایی که ۴ سال تو دیجیتال مارکتینگ بودیم توی طراحی سایت و سئو و اتوماسیون کار میکردیم هم کاملا ورشکست شدیم
نه از ۹ اسفند
ما یه بار جنگ خرداد زمین خوردیم تا اومدیم بلند شیم از جامون و داشتیم اوکی میشدیم دلار دی ماه سر به فلک کشید و بعد یه قطعی دیگه داشتیم که خیلی ها بهانه کردن و پول ندادن آخر دی ما هیچی پروژه نداشتیم حتی بهترین کارفرماها اومدن گفتن کار شما خیلی خوبه ولی ما واقعا پول پرسنل رو هم به زور میدیم نمیرسه به سئو
بهمن اومدیم خودمون رو جمع کنیم تیر آخر رو اول اسفند بهمون زدن
دفترمون رو تحویل دادیم
نیروهامونو از بهمن تعدیل کرده بودیم
و الان چه جوون ها و چه پدرانی که بیکار شدن
منی که تمام تخصصم همیناست
یک متخصص بیکار محسوب میشم.
©️
پیام ارسالی از کاربر shafikhany</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/iaghapour/2599" target="_blank">📅 01:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✍
حدودا 500 پیام بررسی نشده از 2 روز پیش داریم که پشتیبانی تا فردا همه رو بررسی میکنه.
جدا از بحث بالا، از ته دل آرزو میکنم تو این روزهای عجیب و غریبی که داریم می‌گذرونیم، حال دلتون خوب باشه. می‌بینیم و حس میکنم که زندگی چقدر برای خیلی‌ها سخت شده و دغدغه‌ها چقدر زیادن.
امیدواریم هرچه زودتر این روزهای سخت جاشون رو به روزهای روشن‌تری بدن. هوای خودتون و دلتون رو داشته باشید.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/iaghapour/2598" target="_blank">📅 03:02 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAmOm8Hh_1O2iBiMxUP-cleKfER6hUV_byp6atmxoR6hMaWaaqF-BG8w4P5gYmKBP4QLXTYypEDAw40UlF8H88RU5vPNQtXrii1744DkmX7O8FeLWhyeUFzLj1Jixvqo3g_q4m1TWXGYhC7hw9eYiPPsd2N9CnPVbZF3dGQLsngI6BYNVZPQkQieBDcoap-JbooI-lMPuOSlTkd1n3Ebt8tVUHlriAMwB46agDZneWx66xDx5ujiUW_0fSaTOIM4S-fln6V3fNM3pSPpEsmx73FdhzN0wdEDykcjyuSOo4GdKm40Yn6-hTKUeQhChAdgF-Gq63w0bcWv9bsaoLJ_uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت ورژن 0.10.0 سانگبرد منتشر شد
🔹
با این اسکریپت میتونید در سرور ایران خودتون یک مسنجر شخصی بالا بیارید و با دوستان خودتون چت کنید.
توی آپدیت جدید سانگبرد با فعال کردن قابلیت Remote channel، میتونید پست هایی که تو یک چنل تلگرام ارسال میشه رو، به یک چنل توی سرور سانگبرد خودتون استریم کنید.
-
📡
قابلیت Remote channel
-
🔗
ساده سازی سیستم Invite link
-
🎨
بازطراحی بخش ساخت/تغییر کانال و گروه در UI
-
✨
انیمیشن build-up پیام ها در چت ها
-
🔔
بهبود عملکرد push notifications
- تغییرات گرافیکی اسکریپت نصب آسان
-
🐳
پشتیانی از TLS با سرتیفیکیت self-signed در Docker
-
🔧
رفع باگ های گزارش شده
-
📄
اضافه شدن نسخه فارسی فایل readme
🔘
اگه به هر مشکلی خوردین، حتما تو گیت هاب یک issue باز کنید و گزارش بدید.
⭐️
اگه از پروژه راضی بودین، با ستاره دادن تو گیت هاب از پروژه حمایت کنید.
🔹
چنل پروژه
🔗
لینک گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/iaghapour/2597" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⭕️
ساده‌ترین راه برای دور زدن فیلترینگ با تانل DNS
اگه خانواده‌ شما هم داخل ایران برای اتصال به اینترنت مشکل دارند، این پیام ممکن است به شما کمک کند.
این برنامه یک برنامه‌ی  گرافیکیست که کار با آن بسیار ساده است و برای اتصال به اینترنت هر دو روش MasterDNS و VayDNS را پشتیبانی می‌کند.
👈
لینک گیت‌هاب
👈
دانلود
اپ
📖
آموزش کامل MasterDNS و VayDNS
▶️
آموزش روی یوتیوب
📱
آموزش KevinNet DNS
▶️
آموزش روی یوتیوب
🔄
آپدیت‌های جدید برنامه
در صورت وجود هرگونه مشکل یا سوالات مرتبط با KevinNetDNS میتوانید با آدرس ایمیل زیر در تماس باشید:
©️
متن تهیه شده توسط نویسنده اسکریپت KevinDNS
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/iaghapour/2596" target="_blank">📅 23:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⭕️
ادعای عجیب نماینده مجلس: با ۴ هزار میلیارد تومان ایتا را به سطح واتس‌اپ می‌رسانیم!
رئیس کمیته ICT مجلس در اظهارنظری جنجالی مدعی شده است که فاصله میان پیام‌رسان‌های داخلی مثل ایتا با نمونه‌های جهانی مانند واتس‌اپ، تنها در کمبود بودجه برای خرید سرور خلاصه می‌شود. به گفته او، ارتقای این پلتفرم‌ها هزینه چندانی برای کشور ندارد.
این نماینده مجلس معتقد است که پلتفرم‌های داخلی از نظر فنی کمبودی ندارند و تنها زیرساخت‌های سخت‌افزاری آن‌ها باید تقویت شود:
🔹
بودجه برای رقابت:
مصطفی طاهری مدعی است با صرف ۳ تا ۴ هزار میلیارد تومان برای خرید سرور، می‌توان کیفیت ایتا را به سطح واتس‌اپ رساند تا توانایی پذیرش بدون مشکل بیش از ۲۰ میلیون کاربر را داشته باشد.
🔸
هشدار درباره جاسوسی سخت‌افزاری:
این مقام مسئول همچنین به موضوع استفاده از بیگ‌دیتا (داده‌های بزرگ) اشاره کرده و مدعی شده که آمریکا قوانینی برای جاسوسی در لایه‌های سخت‌افزاری و تراشه‌ها (حتی پایین‌تر از سطح سیستم‌عامل) دارد.
این اظهارات در حالی مطرح می‌شود که کارشناسان حوزه تکنولوژی، موفقیت پلتفرم‌های جهانی را فراتر از صرفا تعداد سرور می‌دانند و مواردی چون امنیت، پروتکل‌های رمزنگاری، حریم خصوصی و نوآوری‌های مداوم نرم‌افزاری را از عوامل اصلی برتری آن‌ها به حساب می‌آورند.
یکی از کاربرا زیر همین پست در دیجیاتو کامنت جالبی گذاشته بود:
مامان‌بزرگ منم با چند میلیارد نیکی میناژ میشه!
پ.ن: حالا فارق از این حرفا داره میگه اینا دارن از کاربراشون جاسوسی میکنن برای همین ما باید اپ های خودمون رو داشته باشیم... من حرفی ندارم.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/iaghapour/2595" target="_blank">📅 18:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7TRBrdvjkHp0oxuW_nQXy-4M3BZw_07SisTRLLS8LAqjI9sN28ZAQNkF0F8O3pde8BI5VYUasF-fnRXW-0RLZmIN9ppQ5NHBY8AVEKKPlkU9qVJIfNV-DAbG4eP_Jls02N9RgGCfQO-XGvrQT4YXWxJw393vxgI8DPWl7tal7RehQQ6wX1F9qLmAw4BVJ6Sa08N5xgaD0KWBCwPwEt_rKB7DE-PBIJrx0QYOuMPQaCSpPxbJWXW0YP6rhKCmSWWBWJ3BDPAyJx5G0Is4MT03fZZI7JP2mYwrdJNm_yDqd0JXGELmABP5Ctq38LgcIFC7-_qOwVwcJHljTuTqSGpNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
ایران 11 هفته در خاموشی دیجیتال!
هیچ‌وقت تو زندگیم فکر نمی‌کردم یه روزی برسه که این‌جوری تلخ، شاهد از بین رفتن زحمت‌ آدما باشم. ۱۱ هفته قطعی اینترنت واسه خیلی‌ها فقط یه اختلال ساده نبود؛ قصه پدر مادرا و جووناییه که با هزار امید یه کسب‌وکار کوچیک راه انداخته بودن تا خرج زندگیشونو دربیارن و الان دستشون به هیچ‌جا بند نیست.
تا همین چند وقت پیش با کلی استرس می‌گفتیم کسب‌وکارهای نوپا و خونگی تو «مرز نابودی» هستن و همه‌مون چشم‌انتظار بودیم زودتر اینترنت وصل بشه؛ ولی الان دیگه حرف از مرز نیست. خیلی‌ها کل سرمایه، جوونی و حاصل سال‌ها تلاششون جلوی چشماشون دود شد و رفت رو هوا. کاش دردی که افتاده رو دوش این مردم، میافتاد رو دوش مسئولین...
🆔
@NetProPlus</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/iaghapour/2594" target="_blank">📅 11:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">#فیلترینگ
به ما تحمیل شد,
ولی
#اینترنت_طبقاتی
رو شما باید درخواست بدی تا بهت بدن...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/iaghapour/2592" target="_blank">📅 18:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULKdecyLgH4xFVBgNR288TTYEycq4JyxtsxKVJ1x5j0IpQXHtznAaqV2FNgDJwciYWEtKFJ1OJvBUgnwhvUgoQ6zZkzkr6GrzASlM9iQgeLTH2BOEqwsM4JUU1JsZ_3XhWQ71eBHrvawPoaC8xA7l0ZDlwUGRCsCZgaVwgS33Ocp3WdzTQY-EoDja-bV7oDfgNlJTLvgifw_OP7k5oU0jPZHmYsaFdpk4cBlxn08bvicvFxukiav_tzQI5gokZKTfY9rpcSoduA2Ax5Bc9lozK4B85gL7cFMuxAR2TNn8b210ARaohmbj8QdXSdka5isyvPVrNALzq8TnbYQ5RjEoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت بزرگ تلگرام: ورود دستیار هوشمند به پروفایل شخصی!
تلگرام در آپدیت جدید تمرکز ویژه‌ای روی هوش مصنوعی داشته است. در ادامه مهم‌ترین تغییرات این نسخه را مرور می‌کنیم:
🔹
ربات‌های مهمان:
فراخوانی ربات‌ها در هر چت یا گروهی، تنها با تگ کردن آیدی و بدون نیاز به افزودن آن‌ها.
🔸
منشی شخصی هوشمند:
قابلیت اتصال مستقیم یک ربات به پروفایل شخصی تا در غیاب شما به پیام‌ها پاسخ دهد!
🔹
تعاملات زنده هوش مصنوعی:
تایپ و نمایش لحظه‌ای پاسخ ربات‌ها، به همراه قابلیت جدید ارتباط ربات با ربات برای انجام وظایف پیچیده‌تر.
🔸
امکانات جدید برای کانال‌ها و تولید محتوا:
قابلیت محدود کردن نظرسنجی‌ها (بر اساس کشور یا عضویت در کانال)، مشاهده نمودار آرا، و همچنین ساخت استایل‌های متنی سفارشی.
🔹
اضافه شدن قابلیت انتخاب فونت از سیستم خودتون (میتونید فونت وزیر رو نصب کنید و استفاده کنید).
با این به‌روزرسانی که شامل جستجوی هوشمند ایموجی‌ها، ارسال بی‌صدای پیام زمان‌بندی‌شده و رفع ۲۰۰ باگ فنی است، تلگرام قدم بزرگی برای ادغام کامل پیام‌رسانی انسان و هوش مصنوعی برداشته است.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/iaghapour/2591" target="_blank">📅 14:13 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔻
مومن‌نسب: فضای مجازی به هیچ وجه نباید به حالت قبل برگردد
حالا این آدم انقدر مهم نیست که دربارش صحبت کنیم ولی خواستم بگم این همون آدمیه که چندسال پیش تو صداوسیما میگفت من خطرات اینترنت رو میدونم و اطلاع دارم یک نفر با 2 گیگ اینترنت حامله شده و پدر دختره با گریه اینو برای من تعریف می‌کرد...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/iaghapour/2590" target="_blank">📅 11:35 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔻
اطلاعیه مهم: معرفی فروشندگان کانفیگ
طبق نتایج
نظرسنجی اخیر،
قصد داریم فروشندگان قدیمی و معتبری که از قبل می‌شناسیم را یکی‌یکی برای خرید به شما معرفی کنیم.
📌
قوانین و شرایط مربوط به فروشندگان:
—
عدم پذیرش فروشنده جدید:
در حال حاضر شخص جدیدی معرفی نمی‌شود؛ بنابراین لطفاً در قسمت
«تماس با ما»
برای معرفی خود پیام ندهید. افرادی که معرفی می‌شوند، همگی پیش‌تر در کانال ما سابقه تبلیغ داشته‌اند.
—
تضمین خرید شما:
مبلغی از پول این افراد نزد ما به عنوان امانت می‌ماند تا در صورت بروز هرگونه مشکل، بتوانیم مطالبات شما کاربران عزیز را پیگیری کنیم.
—
ضمانت بازگشت وجه:
این فروشندگان موظف‌اند در صورت لزوم (بسته به شرایطی که خودشان به شما اعلام می‌کنند)، بین ۴۸ تا ۷۲ ساعت امکان عودت وجه را فراهم کنند.
—
قیمت منصفانه:
تمامی این افراد تعهد داده‌اند که نسبت به شرایط بازار، قیمت‌های منصفانه‌تری برای کاربران کانال ما در نظر بگیرند.
— معرفی فروشندگان صرفاً در زمینه
فروش کانفیگ
انجام می‌شود. هیچ‌یک از فروشندگان معرفی‌شده مجاز نیستند پس از معرفی، در کانال شخصی خود تبلیغات مربوط به "
اوتباند
" قرار دهند و یا به کاربران پیشنهاد خرید آن را بدهند.
⚠️
نکات مهم برای کاربران عزیز:
—
انتظارات از کیفیت:
کانفیگ‌ها باید بتوانند تلگرام، اینستاگرام و یوتیوب را به راحتی باز کنند. با توجه به شرایط فعلی اینترنت، داشتن سرعت‌های بسیار بالایِ گذشته کمی دور از انتظار است (هرچند ممکن است کیفیت سرویس‌ها عالی باشد)، پس لطفاً واقع‌بین باشید.
—
اختلال و پشتیبانی:
ممکن است در طول هفته، گاهی با اختلال مواجه شوید. پشتیبان‌ها موظف‌اند در سریع‌ترین زمان ممکن مشکل را حل کنند؛ اما لطفاً صبور باشید، حداقل یک ساعت به آن‌ها فرصت دهید و از ایجاد فشار زودهنگام به پشتیبانی کانال‌ها خودداری کنید.
— در ضمن، توجه داشته باشید که
ما ذی‌نفع این کانال‌ها نیستیم
و فقط به دلیل درخواست‌های زیاد شما این دوستان را معرفی می‌کنیم.</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/iaghapour/2589" target="_blank">📅 23:36 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUylMkHio-ByposVqubKGRTVFJl0eUKiJF498JaqvLlCFWdI5H6F7aO0hz26DJ1pk0vRc_8yIvABB580vVjxDTqq28nG-niOG7bncp536p8j7YZYwPjAKwU-him7VyVlbHOws4BX9Pn-_7BlGS_XCicfuhdDL4Bx39W3PST2gTkhELoBcmrJlx7q50W_VPf29B2MKUlCv81fTSU_uH9vaoo4yEyGZ7kohl3siiHirSJ4j1DnW8-9l46boVUuMc_gDhatwOPmnetq2mozFje41jZMShZOKHvo7MOKOhsiF_QLuODy7q-iztowqBXcDKax7lx66HI_QiC53uUFeIiVQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
سخنگو وزارت خارجه حذف تیک آبی خود در شبکه X را (سرکوب حقیقت) خواند.
68 روزه اینترنت مردم ایران رو قطع کردن، بعد یه تیک آبی‌شو گرفتن میگه حقیقت سرکوب شد.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/iaghapour/2588" target="_blank">📅 20:22 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔻
تسنیم: درآمد طرح اینترنت «پرو» در سال به ۹۶ هزار میلیارد تومن می‌رسه!
🔹
خب با این رقم‌های نجومی و پول هنگفتی که درمیاد، معلومه که از این تبعیضی که راه انداختن حسابی راضی‌ان. وقتی محدودیت و فیلترینگ این‌قدر براشون سود داره، چرا نباید اینترنت داخلی و بسته رو بیشتر تحویل بگیرن؟
🔸
این وسط یه تشکر ویژه و خسته نباشید هم باید بگیم به اون دسته از دوستانی که رفتن تو صف اینترنت پرو و این سیستم طبقاتی رو خیلی راحت پذیرفتن. از رئیس فلان اتحادیه و مدیر فلان اداره بگیر تا نماینده صنف لاستیک‌فروش‌ها و یه سری کسب‌وکارهایی که واقعاً بدون اینترنت آزاد هم کارشون لنگ نمی‌موند. تو شرایطی که ۹۹ درصد مردم هیچ دسترسیِ عادی به اینترنت آزاد ندارن، مرسی از شماها که رفتین این اینترنت رو گرفتین و با این کارتون، قشنگ به این تبعیض و نابرابری رسمیت دادین!
پ.ن: البته به این نکته هم توجه کنید که خبرگذاری داخلی اینو گفته و ممکنه دقیقا مقصودشون از این حرف هم همین باشه که بگن چقدر این طرح خوب و سودآور هستش و...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/iaghapour/2587" target="_blank">📅 14:33 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⭕️
وعده بازگشت به وضعیت عادی؛ توجیه محدودیت‌ها یا امید به بهبود اینترنت؟
معاون ارتباطات دفتر رئیس‌جمهور به تازگی اعلام کرده که وضعیت فعلی اینترنت مورد تایید دولت نیست و رئیس‌جمهور، محمدرضا عارف را مامور ساماندهی این شرایط کرده است. به گفته او، این محدودیت‌های شدید و قطعی‌ها صرفا تصمیماتی از سوی شورای عالی امنیت ملی و به دلیل شرایط خاص امنیتی و جنگی بوده‌اند.
🔹
وعده روزهای بهتر:
این مقام مسئول قول داده که با عبور از این شرایط ویژه، اینترنت نه تنها به حالت قبل برمی‌گردد، بلکه وضعیتی بهتر از گذشته پیدا خواهد کرد و وعده‌های انتخاباتی رئیس‌جمهور در این زمینه همچنان پیگیری می‌شوند.
🔸
دفاع از اینترنت پرو:
در واکنش به انتقادات، دولت ادعا می‌کند طرح «اینترنت پرو» صرفا برای نجات کسب‌وکارها در روزهای محدودیت ایجاد شده و نباید به آن برچسب اینترنت طبقاتی زد؛ چرا که به گفته آن‌ها، در شرایط عادی اصلا نیازی به چنین طرحی نخواهد بود.
🔹
کاهش محدودیت‌های عمومی:
خبر دیگر این است که قرار شده تدابیر جدیدی برای دسترسی بهتر سایر شهروندان به اینترنت اتخاذ شود تا فشار محدودیت‌های فعلی روی مردم کاهش یابد.
در حالی که دولت تلاش می‌کند قطعی‌ها و طرح‌های بحث‌برانگیزی مثل اینترنت پرو را صرفا به شرایط اضطراری گره بزند، کاربران و کسب‌وکارها همچنان منتظرند تا ببینند آیا این وعده‌ها در عمل به یک اینترنت آزاد و بدون محدودیت ختم می‌شود یا صرفا وعده‌ای برای کنترل نارضایتی‌های فعلی است.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/iaghapour/2585" target="_blank">📅 21:12 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⭕️
ایده عجیب در مجلس: تاسیس «اینستاگرام دولتی» و مدیریت کامل اینترنت!
نمایندگان مجلس در تازه‌ترین نشست خود با وزیر ارتباطات، از طرح‌ها و نگاه‌های جدیدی برای کنترل بیشتر فضای مجازی پرده برداشتند. در این جلسه، پیشنهاد ایجاد یک پلتفرم کاملا دولتی مشابه اینستاگرام مطرح شد تا به زعم آن‌ها، نیاز کشور برطرف شود.
🔹
اینستاگرام دولتی:
یکی از نمایندگان با اشاره به بازار سیاه و چند میلیونی فیلترشکن‌ها، رسما پیشنهاد ساخت یک سکوی دولتی شبیه اینستاگرام را برای پر کردن جای خالی این پلتفرم ارائه داده است.
🔸
رویای مدیریت اینترنت:
نایب رئیس مجلس تاکید کرده که مشکل آن‌ها اصل اینترنت نیست، بلکه می‌خواهند در صحنه بین‌المللی، مدیریت اینترنت کاملا در دست خودشان باشد و این فضا را به یک جبهه تقابل تشبیه کرده است.
🔹
فرصت‌سازی از بحران:
بخش قابل توجهی از صحبت‌های نمایندگان، حسرت خوردن برای از دست رفتن فرصت در شرایط ملتهب و جنگی است؛ آن‌ها معتقدند باید از این شرایط استفاده می‌کردند تا مردم و کسب‌وکارها به اجبار به سمت سکوهای داخلی کوچ کنند.
این صحبت‌ها به وضوح نشان می‌دهد که دغدغه اصلی، کاهش نارضایتی مردم از قیمت و کیفیت اینترنت نیست؛ بلکه تلاش برای بومی‌سازی اجباری، قطع ارتباط با شبکه‌های اجتماعی بین‌المللی و کشاندن کاربران به پلتفرم‌های تحت کنترل و نظارت است. / زومیت
✍🏻
پ.ن: از سوپر اپلیکیشن های ایتا و سروش و گپ و بله که از تلگرام کپی کردین مشخصه توانایی اینکار رو دارید.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/iaghapour/2584" target="_blank">📅 19:36 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⭕️
مرگ خاموش اقتصاد خرد: نابودی ۴۰ درصد از کسب‌وکارهای اینستاگرامی!
قطعی‌ها و محدودیت‌های اینترنتی فقط حق دسترسی آزاد ما به شبکه‌های اجتماعی را سلب نکرده، بلکه تیشه به ریشه‌ی اقتصاد خرد و معیشت مردم زده است. طبق اعلام پشوتن پورپزشک، عضو هیئت‌مدیره اتحادیه کسب‌وکارهای مجازی، فیلترینگ و اختلالات باعث نابودی بخش عظیمی از مشاغل آنلاین شده است.
🔹
فاجعه‌ی آماری: نزدیک به ۴۰ درصد از کسب‌وکارهای اینستاگرامی برای همیشه از بین رفته‌اند؛ این یعنی مرگ مستقیم بیش از ۴۰۰ هزار شغل!
🔸
دومینوی ویرانی: وقتی شوکی مثل محدودیت اینترنت وارد می‌شود، ابتدا کسب‌وکارهای کوچک و آسیب‌پذیر می‌میرند، اما این نابودی با کمی تاخیر گریبان شرکت‌های بزرگ اقتصادی را هم خواهد گرفت.
🔹
زنجیره‌ی به هم پیوسته: کسب‌وکارهای بزرگ در تولید، تامین و توزیع به شدت به همین کسب‌وکارهای خرد وابسته‌اند. توهم مصونیت برای شرکت‌های بزرگ، در نهایت منجر به فروپاشی خود آن‌ها می‌شود. منبع: زومیت
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/iaghapour/2583" target="_blank">📅 19:29 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اسم این زندگــــــی نبود
یک مبارزه تمام عیار بود...
#جوانی
#زندگی
#جنگ
#اینترنت</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/iaghapour/2581" target="_blank">📅 19:09 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⭕️
حل مشکل دانلود از ریلیز گیت‌هاب با LatestReleaseMirror
اگر در دانلود فایل‌ها از بخش ریلیزهای (Releases) گیت‌هاب به دلیل محدودیت‌های اینترنت مشکل دارید، این اسکریپت کاربردی دقیقاً برای شما ساخته شده است!
ابزار
LatestReleaseMirror
به صورت خودکار فایل‌های آخرین آپدیتِ ریپازیتوری‌های دلخواه شما را دریافت کرده و آن‌ها را به عنوان فایل‌های عادی در ساختار پوشه‌های گیت‌هاب ذخیره می‌کند؛ در نتیجه می‌توانید آن‌ها را به راحتی و حتی با اینترنت داخلی دانلود کنید.
🔹
دریافت و آپدیت خودکار آخرین نسخه با استفاده از GitHub Actions.
🔸
امکان فیلتر کردن فایل‌های مورد نیاز (مثلاً فقط نسخه‌های ویندوز یا اندروید)
🔹
دسته‌بندی تمیز فایل‌های خروجی در مسیرهای مشخص.
🔗
لینک ریپازیتوری و راهنمای استفاده
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/iaghapour/2580" target="_blank">📅 16:09 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ركورد جديد سرعت اينترنت ژاپن:
با سرعت 1.02 پتابيت بر ثانيه، كل نتفليكس را در 1 ثانيه دانلود مى‌كند.
✍
ما هم اینجا باید با DNStt وصل بشیم تا بزور بتونیم فقط این خبر رو بخونیم...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/iaghapour/2579" target="_blank">📅 13:56 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⭕️
اسکریپت بهینه شده XHTTP Relay ECO برای Vercel Pro
🔹
نسخه ECO طوری تیون شده که علاوه بر امنیت سفت‌وسخت v1.3، کم‌هزینه‌ترین رفتار ممکن روی Vercel Pro رو داشته باشه؛ یعنی با کنترل هوشمند Timeout، Inflight، Throttle و Logها، مصرف منابع و هزینه نهایی تا جای ممکن پایین نگه داشته میشه.
🔸
فقط با GET، HEAD و POST کار می‌کنه تا امنیت بالاتر بره.
🔹
احراز هویت فقط از طریق هدر x-relay-key انجام میشه
🔸
هدرهای اضافی پلتفرم و hop-by-hop رو بی‌رحمانه فیلتر می‌کنیم.
🔹
روی آپلود و دانلود محدودیت سرعت (Throttling) واقعی گذاشتیم.
🔸
بردیمش روی Node runtime با لیمیت ۱۲۸ مگابایت رم و مدیریت کانکشن‌های همزمان.
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/iaghapour/2578" target="_blank">📅 22:28 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⭕️
ورژن جدید کلاینت اندروید GooseRelayVPN منتشر شد
کلاینت اندروید GooseRelayVPN که هسته GooseRelay را از طریق Go mobile اجرا می‌کند و رابط کاربری کامل برای مدیریت VPN، پروفایل‌ها، لاگ‌ها و تنظیمات ارائه می‌دهد. این اپ یک SOCKS5 محلی روی اندروید ایجاد می‌کند و ترافیک TCP را از معماری GooseRelay عبور می‌دهد.
🔹
هسته پروژه به ورژن 1.5.0 آپدیت شد.
🔸
قابلیت fake dns اضافه شد.
🔹
باگ ها در این نسخه برطرف شدن.
🔗
آدرس گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/iaghapour/2577" target="_blank">📅 14:05 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWcJYgkckMEait5TGi-Pw9QMBGR0f8lb8yf0_vpyGRnzCqd7uhK2RvELJ9YKOCQGUoEikJzfBgvEeGgOnlLbtYGJUS3-hd3oz_5xdIgy52IxqOnWVG07_g259qiZsACamwh_B_cnRsDn_x5t9K_a3G9SbqiJVhutWqst2Haagezn_v7_gLaCCItQbOZxtiI_hIaPo0em_xZ2IK5eAJ-smzXkrdnCD9MiR7bNUCsbQm-sysyzQYtWE6ZyMIVLNfKYyCpfrWZsA3KwGxhkTmHQPZiKlPevZ2P7OuMy60kwbavbqKuCzCAXCCQUNbNnAZbTJ_M6XVlhNLSIorQa7n0f-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت فیلترشکن رایگان و شخصی به 2 روش با نت ملی
🔹
با استفاده از دو ابزار قدرتمند MHRV و Nova-Proxy، دیگه نیازی به خرید کانفیگ‌ها و سرورهای گرون‌قیمت ندارید. تو این آموزش قدم‌به‌قدم به ۲ روش مختلف پیش میریم تا بتونید یه اتصال پایدار و بدون قطعی داشته باشید. حتماً تا آخر ویدیو همراه من باشید.
🔗
لینک ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
🔹
دانلود کلاینت ویندوز
🔸
دانلود کلاینت اندروید
#آموزش
#فیلترشکن
#mhrv
#novaproxy
#رایگان
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/iaghapour/2576" target="_blank">📅 19:53 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrdHYQMO8gtRXe0S7-uost7SbHUhgb4trtI6xV1dlmIt68c6eL2XFzZWAooqR2K2T2uM4Y4hIAev99E1H7MkCVUeuEVoRTiwyK2UShwK5eRVnKgyVPJWDCZhIlZXmbDS4paLfX0w7tts5uIugfNZkK0AzAFpakhkep7H3BqhOWkUDrGHay6VU3RAFU8uQPC430hPFY8AAcskHcVsUH_VLQLHwEl1wHeapIR0P2KufdqXoAslopo3Uo-uXcSKZnQmhvBjWKR7u6sLsqvR4W8-_3k7-ekTbi4cVFYba5rfkM2B_OY5oBtvmgiQq3QEzMu4X2EBfDWxNV-gxMMlKX4ruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
پشت‌پرده‌ی «اینترنت پرو»؛ امتیاز ویژه یا تله‌ی نظارتی؟
این روزها سیم‌کارت‌های بدون فیلتر با نام «اینترنت پرو» در ازای دریافت هزینه و ثبت کامل مشخصات هویتی به فروش می‌رسند. اما هدف اصلی این طرح، دلسوزی برای نیاز اینترنتی اقشار مختلف نیست.
هدف اصلی و پنهان این ماجرا، چیزی جز «تشخیص هویت دقیق و رصد لحظه‌ایِ کاربر» نیست.
👁‍🗨
وقتی اینترنت آزاد را مستقیماً با نام و کد ملی خودتان دریافت می‌کنید دقیقاً چه اتفاقی می‌افتد؟
🔹
پایان گمنامی:
تمام سایت‌هایی که سر می‌زنید و محتوایی که می‌بینید، مستقیماً و شفاف روی نام خودتان ثبت و مانیتور می‌شود.
🔸
تزریق خودسانسوری:
وقتی می‌دانید هر کلیک شما رصد می‌شود، ناخودآگاه وارد یک «زندان شیشه‌ای» می‌شوید که خودتان هزینه‌اش را داده‌اید!
🔹
تجارت با حقوق اولیه:
حق بدیهی دسترسی به اینترنت آزاد را مسدود کرده‌اند و حالا همان را به قیمت نقض حریم خصوصی، به عنوان یک «آپشن ویژه» به خودمان می‌فروشند.
«اینترنت پرو» یک امکان رفاهی نیست؛ ابزاری برای کنترل نقطه‌ای و عادی‌سازیِ اینترنت طبقاتی است. بهای اصلی این سیم‌کارت‌ها پول نیست؛ حریم خصوصی ماست.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/iaghapour/2575" target="_blank">📅 15:30 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQyP8HaK7bhzX8zBsaCRiEsrhauVXFM5HOm-TsdrTp1f3Rib9jOJ5ka8mBp-B316ITwR48zzP3XStK7410c40x1R0FZRM_2vpUyLYYQebBF6GmQwptO3ixoiX3P9rwiOgi9sqCrADwRgj2anJKt9oudhyWl7rj98zIJtLvKsoUKOgt8fU2G1C73-_ZxhQUpze47KHMXtFLOVttOf5sf1rAE90uyiHYfoOoH4VRfbzcQHWrC8dr3xXhAkE92aOecepNi5Tv5pEj6Wsm-oS4AKL7vhTRtihfwjFP0nySRo0QanudN5LpxkaO9KGXtj8sof7cBwTmbWuL-eMvTfGd-I7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
کلاینت اندروید GooseRelayVPN
🔹
کلاینت اندروید GooseRelayVPN که هسته GooseRelay را از طریق Go mobile اجرا می‌کند و رابط کاربری کامل برای مدیریت VPN، پروفایل‌ها، لاگ‌ها و تنظیمات ارائه می‌دهد. این اپ یک SOCKS5 محلی روی اندروید ایجاد می‌کند و ترافیک TCP را از معماری GooseRelay عبور می‌دهد.
🔹
پیکربندی مبتنی بر پروفایل
🔸
وضعیت و تله‌متری در صفحه Home
🔹
تب Logs برای عیب‌یابی Android/Core
🔸
قابلیت Split Tunneling و Internet Sharing
🔗
آدرس گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/iaghapour/2573" target="_blank">📅 20:06 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">💢
رئیس اتحادیه کسب‌وکارهای مجازی
:
به شرکت‌ها زنگ می‌زنند و پیشنهاد فروش اینترنت بدون فیلتر(پرو) برای کارمندانشان را می‌دهند.
⁉️
اگر موضوع واقعاً امنیت ملی است، چطور با پرداخت پول، امنیت تأمین می‌شود؟!
منبع: کانال خبری
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/iaghapour/2572" target="_blank">📅 13:23 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-poll">
<h4>📊 ⁉️نظرسنجی درباره سوال بالا (اگه واقعا نیاز دارید بله رو بزنید).</h4>
<ul>
<li>✓ بله معرفی بشه.</li>
<li>✓ خیر نیازی نیست.</li>
</ul>
</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/iaghapour/2571" target="_blank">📅 00:25 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✍🏻
دوستان، همان‌طور که خودتون در جریان هستید، من در این چند ماه حتی یک مورد
تبلیغ فیلترشکن، اوتباند
و موارد مشابه
قرار ندادم.
الان هم واقعاً تمایلی به این کار ندارم، چون شرایط اصلاً به‌گونه‌ای نیست که بشه کسی را معرفی کرد.
با این حال، در همین چند ماه پیام‌های بسیار زیادی داشتیم که درخواست می‌کردند حتماً یک شخص معتبر را معرفی کنیم؛ چرا که خیلی‌ها از کلاهبرداری‌های پیاپی خسته شدن و ارسال این دست پیام‌ها تا به همین امروز هم ادامه داره.
به همین دلیل، اگه خودتون موافق باشید،
افرادی رو که
از قبل با ما همکاری می‌کردند
و تا حدودی قابل‌اطمینان هستند، یکی‌یکی به شما معرفی کنیم. در این مورد ذکر چند نکته ضروری هستش:
🔸
عدم تضمین صددرصدی:
ناگفته نماند ما واقعاً نمیتونیم کسی را با اطمینان ۱۰۰ درصدی تأیید کنیم، اما افرادی که معرفی میشن همگی سابقه همکاری با ما را دارن.
🔹
عدم پذیرش تبلیغ جدید و اوتباند:
تا زمانی که شرایط استیبل و پایدار نشود، تبلیغ
هیچ فرد جدیدی را قبول نمی‌کنیم.
در ضمن،
تبلیغ فروش اوتباند هم به‌هیچ‌وجه پذیرفته نمی‌شود.
🔸
قیمت‌های منصفانه:
تمام سعی ما بر اینه افرادی را معرفی کنیم که در این زمینه منصف باشند و قیمت‌های بالایی ارائه ندهند. ولی خب، طبیعتاً نمیشه انتظار قیمت‌های قدیمی را داشت؛ چون همان‌طور که خودتون میدونید در حال حاضر هیچ‌کس با اون قیمت‌های قبلی فروشی نداره.
اگه تمایل دارید، لطفاً در نظرسنجی زیر شرکت کنید.
البته نظر شخصی خودم اینه که اگه در حال حاضر واقعاً مشکل خاصی ندارید، در نظرسنجی همان گزینه
(خیر) را انتخاب کنید
.</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/iaghapour/2570" target="_blank">📅 00:24 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⚠️
هشدار مهم درباره اسکریپت VPN Over GitHub
▪️
لطفاً از این ابزار به عنوان
فیلترشکن
استفاده نکنید!
🚫
بن شدن اکانت:
تبدیل گیت‌هاب به تونل ترافیک، خلاف قوانین این سایت است و خیلی زود باعث مسدود شدن حساب شما می‌شود.
🐢
سرعت بسیار پایین:
برای هر ارتباط به یک بار
push
و
pull
نیاز دارد که آن را عملاً غیرقابل استفاده می‌کند.
🔻
خطر برای برنامه‌نویس‌ها:
گیت‌هاب یک سایت حیاتی برای توسعه‌دهندگان است؛ سوءاستفاده از آن ممکن است باعث حساسیت شده و دسترسی به این پلتفرم مهم را دوباره از کار بیندازد. (خارج شدن از لیست سفید و...)
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/iaghapour/2569" target="_blank">📅 19:21 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ای بابا روش Vercel چرا بسته شد؟ هنوز آموزش نداده بودم که.
😁
سازمان فیلترینگ زرنگ شده ها. فک کنم خودشون رو آپدیت کردن دیگه به کانال من نگاه نمیکنن :)</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/iaghapour/2567" target="_blank">📅 16:34 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‼️
دلار 177 و طلا 19,400,000
شب میخوابی صبح بلند میشی یه پله بدبخت تر میشی!</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/iaghapour/2566" target="_blank">📅 11:10 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حالا نیاز نیست پول بدین ری اکشن فیک بزنید.
😁</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/iaghapour/2565" target="_blank">📅 20:52 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GooseRelayVPN Guid -- @iAghapour.txt</div>
  <div class="tg-doc-extra">1.2 KB</div>
</div>
<a href="https://t.me/iaghapour/2564" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
دستورات
برای ویدیو
GooseRelayVPN
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/iaghapour/2564" target="_blank">📅 14:21 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdBaJR1_OYVliEB7AJ5NmDz8bE_tRr9oTsh7uuZUpi011oDOz1y8QnJf6Zr7rRhgcQla-OdHtIIZ_ndC93WDZFpzQy4P9OsfN3wlo4HbG0Z76wi8aPAXrl40gjSpOBwvwg4V7AqU6H1UZCLA6TH4BiM2nIH9VNjcBI2jZfnHRPV6xfWRUarPjc7hFxEn7T-NuCXEzu2U2iqhZNGfLMZAmtEYnGeprRxsexZLrxz9kp5K0PpfqaaRwsHp_A-_PHVs4JrR_vJ8EskdKs3zd0D5cEaHVhQk4r3vdFrzKALIVruuNJQT-ex97EIL4Jf2Vm1L_uOtiaAy1ALcdDJMs8rznA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ساخت فیلترشکن شخصی و تانلینگ امن با سرویس‌های ابری! (GooseRelayVPN)
🔹
در این آموزش، یک روش عالی به نام GooseRelayVPN رو بهتون معرفی می‌کنم. با استفاده از اسکریپت‌های ابری (Apps Script) به عنوان واسطه و اتصال اون به سرور لینوکسی خودمون، یک تانل امن میسازیم.
🔗
لینک ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
🔻
دانلود فایل کدها
#آموزش
#فیلترشکن
#گوگل
#تانل
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/iaghapour/2563" target="_blank">📅 14:18 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✍🏻
از اونجایی که دیگه کسی حوصله خوندن خبر رو نداره براتون عناوین خبر رو قرار دادم :)
🔸
دو ماه قطعی اینترنت؛ تعدیل ۳۰ تا ۵۰ درصدی نیروی انسانی در شرکت‌های اینترنت اشیا
🔹
ثبت ۳۱۸ هزار درخواست کار در یک روز در جاب‌ویژن
🔸
کانون وکلای اصفهان هم اینترنت «پرو» را نپذیرفت
🔹
ارسال پیامک اینترنت «پرو» این بار برای مهندسان
🔸
خزنده‌های گوگل پس از ۶۰ روز قطعی، دوباره سایت‌های ایرانی را می‌بینند
🔹
ضربه سنگین قطعی اینترنت به اشتغال زنان
🔸
دبیر سابق شورای‌ عالی فضای مجازی: اینترنت بین‌الملل می‌تواند ظرف ۵ دقیقه وصل شود.
🔹
سخنگوی دولت: با پایان بحران وضعیت اینترنت تغییر خواهد کرد
منبع: زومیت - دیجیاتو
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/iaghapour/2562" target="_blank">📅 11:54 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اسکریپت KevinNet DNS با پشتیبانی از VayDNS آپدیت شد
حدودا 1 هفته پیش یک آموزش ضبط شده به اسم
(بهینه ترین روش اتصال با پروتکل DNS)
و توی این ویدیو ما اومدیم اسکریپت
KevinNet
رو معرفی کردیم. و الان در آپدیت جدید میتونه از VayDns هم ساپورت کنه.
🔹
اضافه شدن قابلیت تغییر مقادیر در برنامه
🔸
قابلیت تست ریزالور حتی در vaydns
🔹
قابلیت ایجاد پروفایل متعدد برای دامنه
. قابلیت های دیگه ...
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/iaghapour/2559" target="_blank">📅 19:22 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agVQ2mGqViBS_lCdKZ0TNyMFVBMEHnkkAFIVRufYy2HVDzSaPbe_fmBkCY5pW0XJQoC7RzQDx0xm2e4N9W6_Tn8dFOU_KICJDC3tNPOQeoMVJjx9JhVY_oLXIZ1M4WWv2zNc0s6uxI0yNpeZE4vVNyr7z0PddDl--8Od01wuLQfzlfTPlxX0r0PlkeSsSDMjf5HSdeEu5u826f3wiVpCrqlMYQK7szmfeIOYUTvL2I30hmi2wqFM2toRqqOvRWmklqbem29fuhDRsa6d2irTe7Mis7yxD8oHibCbCkc7KghVoXjHZ32p2aVOAMGEOr3k_WpJoSM-p41Q82l3EywkfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت هارد ۱۰ ترابایت بنفش (Western Digital Purple) ناقابل 108 میلیون
🫠
همینطوری ادامه داشته باشه برای خرید یک گوشی دکمه ای هم باید همین مقدار پول بدیم....
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/iaghapour/2558" target="_blank">📅 09:34 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzWe5uH6N1XrrHuEiN156Kj2Ro1cBPp_ZYN8UadmMqxP4wIKUBqBT9xWXS0OI1NNsBo2yg1CDLg6x125-2ZQgSNP-v6WPy2vKWcakcUmdYqQBWEyiuxbg98_jBYsMvVVGQdFv7WJLe5oH_C_MKNt9pJFr_NVnzfqHQAJDs14DtL1WNSxecLYtjlRJ0je9nQYBdwjCYnv2NQiMKNzQidN9aUCQHJPx4xJ3Loiqe2yDe9KHCy0Wg2RXS1FNgvekiaCeqOXLSgrNE3F0_O38lFNCSd2ZJ87mso6J5hRzx1SDa9EDoS5DPdReTpSkAGaPGIRANws3Dnh_JwrqACujRG_ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نصب‌کننده خودکار Parley Chat
🔻
از اونجایی که راه‌اندازی و کانفیگ کامل یک پلتفرم چت روی سرور (با تمام دردسرهای تنظیم دیتابیس، وب‌سرور و گواهینامه امنیتی) کار سخت و زمان‌بریه، این ابزار جذاب اومده تا همه چیز رو براتون ساده کنه!
🔸
راه‌اندازی کامل بکند (Backend) و فرانت‌اند (Frontend)
🔹
کانفیگ خودکار Nginx به همراه دریافت گواهینامه SSL
🔸
ایجاد سرویس‌های Systemd برای مدیریت آسان‌تر و پایداری سرویس
🔗
لینک گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/iaghapour/2557" target="_blank">📅 21:48 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YigaTa5lN9QWj2MvuDi4TN_Pg4SUwqVQBOgfoxq4OfKOUC7qeyLL6HlNFkGCnrzxTIz0cOgwU0t672eESpUkoCDKuLPRsnwP2THE1JHIznFQxreFTrUFIExJQWEcDetzIPwkd_crWOelFIoyQAIa5QzdyQg1MQi_bwjaA2108-zKNNxhoVdxj_G77I1Y12U-WsXWCN2EEfflqApEdeyfa0y0DUk9NMWeo85kILA2is6GS8aLON3ecKQNVkMJlKHScVJShBJtDCWVaTJ9TAfMGnGaIJ-R5hANQhC91UZfpSiqPbOSH95zHsGrI0c8Rw3zCSskUFlxF7-3f8qWDq432w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
لینک همه سایت‌های کاربردی تو این سایته!
🔹
از اونجایی که پیدا کردن لینک سایت‌های کاربردی در دسته‌بندی‌های مختلف مثل آپلودسنترها، سایت‌های دانلود فیلم و سریال، ابزارهای آنلاین و... خیلی سخت و زمان‌بر شده، سایت WebDX اومده همه این‌ها رو به صورت منظم و دسته‌بندی شده یک جا جمع‌آوری کرده.
🔗
لینک ورود به سایت
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/iaghapour/2556" target="_blank">📅 21:40 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">💢
سازمان نظام پرستاری:
با وجود اینکه امکان برقراری اینترنت پرو برای اعضای خود را داریم، تا زمانی که همه مردم ایران به اینترنت متصل نشوند از این امکان استفاده نخواهیم کرد.
🔴
در اطلاعیه کامل سازمان نظام پرستاری:
«بسمه تعالی
سازمان نظام پرستاری جمهوری اسلامی ایران به اطلاع کلیه پرستاران و مردم عزیز ایران می‌رساند؛ با توجه به محدودیت‌های ایجادشده در دسترسی به اینترنت بین‌الملل به‌دلیل شرایط خاص جنگی کشور و ارائه دسترسی محدود (اینترنت پرو) به برخی اقشار، امکان اعطای این امتیاز به اعضای سازمان نظام پرستاری نیز از سوی مقامات مسئول اعلام شد، لکن سازمان نظام پرستاری جمهوری اسلامی ایران براساس بررسی جوانب مختلف تا زمان رفع محدودیت‌های دسترسی عموم مردم به اینترنت بین‌الملل، درخواست هیچ امتیاز ویژه‌ای را برای اعضای خود نخواهد داشت.
ان‌شالله زمانی که این امکان برای همه مردم ایران فراهم باشد، پرستاران نیز در کنار آحاد مردم از این امکان استفاده خواهند نمود.»
﻿
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/iaghapour/2555" target="_blank">📅 13:20 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQA5_EDJYe0tx-0-ICxuxYz5oXMgaBCG7tCe5KKG9iDGJDhGWfBhKlYHYNexdFhwjsD5oXAtJvDw5FfvbE86a4XjbuA1twO3SXeflr3fNvMQ_P8h9vVQyNqcRrPPpMMt5Pfy1LIs5ik5Thy4OhX3RB-zMG9qpUU60VAWvUhly8ZPJvHodH3MrJRk_QUn3i-M3am2xw2g1RyZYlS4uzh2hPypqU4Ejd65EevQ_zQ1BXWh4NuoVVwo23zAloUMJNK_gVj1Adz6py3DSvmWYNiL971sSOAGqddgDF-jEilaVhEOsk5Wn8tIexdSRdQ1hhqJAQOMyyD7dTFVpVBBZt529Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ربات‌های کاربردی تلگرام برای شرایط اینترنت محدود
با توجه به محدودیت‌های فعلی، این ربات‌ها حکم یک اینترنت آزاد و همه‌کاره را در قلب تلگرام دارند:
🔹
@GPT4Telegrambot
دسترسی به ChatGPT، جمنای و تولید تصویر.
🔸
@WebSearchAiBot
جستجو در گوگل و خواندن محتوای سایت‌های فیلتر شده.
🔹
@apkdl_bot
دانلود مستقیم برنامه‌های گوگل‌پلی (جایگزین استور).
🔸
@SaveAsBot
دانلود ویدیو و عکس از یوتیوب، اینستاگرام و توییتر.
🔹
@reddit_download_bot
دانلود محتوای متنی و تصویری از سایت ردیت.
🔸
@UrlUploadBot
تبدیل لینک دانلود سایت‌ها به فایل مستقیم تلگرامی.
🔹
@ReadabBot
تبدیل مقالات وب به حالت مطالعه سریع در خود تلگرام.
🔸
@vtovbot
تبدیل فایل‌های صوتی پرحجم به ویس باکیفیت و کم‌حجم.
🔹
@voicybot
تبدیل ویس به متن با پشتیبانی از زبان فارسی.
🔸
@fakemailbot
ساخت ایمیل موقت برای زمان‌هایی که جیمیل در دسترس نیست.
🔹
@newfileconverterbot
تغییر فرمت انواع فایل‌ها مثل عکس، ویدیو و داکیومنت.
©️
با تشکر از ایوب عزیز.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/iaghapour/2553" target="_blank">📅 20:41 · 05 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2552">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">💢
اردستانی؛ نماینده مجلس
:
حکومت تصمیم گرفته فعلا روایت خودشو بیان کنه. برای‌همین به خبرنگارها؛ دانشگاهی ها؛ نماینده های مجلس و هنرمندانی که با حکومت همراهن اینترنت داده تا برای خارجی ها تولید محتوا کنن.
پ.ن: عجب بابا عجب دیگه کار از مخفی کردن و شرمنده بودن و... گذشته. خیلی قشنگ این تبعیض رو فریاد میزنن.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/iaghapour/2552" target="_blank">📅 17:38 · 05 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✍🏻
یه تناقض عجیب بین حرفای مسئولین و واقعیت اینترنت کشور هست. از یه طرف رئیس‌جمهور میگه موافق وصل شدن اینترنته، از اون طرف سخنگوی دولت میگه اصلاً اینترنت طبقاتی نداریم و وزیر ارتباطات هم کلاً وجود لیست سفید رو گردن نمی‌گیره.
ولی خب تو عمل، داریم یه جور تبعیض و آپارتاید اینترنتی رو به چشم می‌بینیم:
افراد رانتی:
اینترنت کاملاً آزاد و بدون فیلتر (همون لیست سفید).
شهروندای درجه دو:
یه اینترنتی که بدون فیلترشکن دوزار نمی‌ارزه (همون اینترنت پرو).
مردم عادی:
محدودیت کامل و حبس شدن تو شبکه داخلی.
از همه جالب‌تر مسئولینی هستن که میان میگن این محدودیتا موقتیه. یعنی ۶۰ روز قطعیِ پشت سر هم، معنی «موقت» میده؟ اصلاً می‌دونید موقت یعنی چی؟
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/iaghapour/2551" target="_blank">📅 19:30 · 04 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1ND00HWxtooc26ukKgSY3zlq73botCXqfeQWyxXmG80I-YbJ1-qUCc-yJRh4F6NLidOxamYllz1SOVhXSkzAHVY2y9GltS2cWlCoKQifnTRLfjrxMgshryNfl5Xw-QBt7e-atOC5NZjlK9RGfQM3SW_ISJPly2AXgBJGLe4gW2DyVeETQvcrRO9ILWX1UeXCZLfSbwVt3vw1QK7kWvjEG_CblEAZo9aelpwOx0YukZa5-p0H75oIV00xbuBlHvvp-UadDAQjX-xXbN2UgeFncX6y8i9CZi2Wq33rzs6lPfWvJ0y_A_FzGKxNl_jX2jXv6wo9i9aqC5MuBjtj222Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
روز ۵۶ام از قطع اینترنت در
#ایران
هستش و اتصال بین‌المللی بیش از ۱۳۲۰ ساعته که قطع شده و کسی پاسخگو نیست!
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/iaghapour/2550" target="_blank">📅 11:19 · 04 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⚠️
یک یادآوری و هشدار خیلی مهم به دوستان عزیز
دیگه واقعاً حسابش از دستم در رفته که تا حالا چند بار این موضوع رو گفتم، اما باز هم باید تکرار کنم:
ما اصلاً هیچ گروهی نداریم!
متأسفانه بعضی‌ها با استفاده از اسم و عکس ما اقدام به ساخت گروه یا کانال می‌کنند. حتی بعضی‌ها خودشون رو به عنوان «پشتیبانی» ما معرفی می‌کنند. من قصد قضاوت در مورد هدف این افراد رو ندارم، اما این کار باعث سردرگمی شما میشه و اصلاً درست نیست.
لطفاً توجه کنید که فعالیت رسمی ما فقط و فقط در چند آدرس زیر انجام میشه و تمام:
🔸
یوتیوب:
youtube.com/@iAghapour
🔹
کانال تلگرام:
t.me/iaghapour
🤖
ربات تماس با ما:
@iaghapourbot
🐦
توییتر:
(که البته خیلی اونجا فعال نیستم)
نکته مهم: هر گروه، کانال یا شخصی که خارج از این لیستِ بالا خودش رو مرتبط با ما معرفی کرد، هیچ ارتباطی به ما نداره.
ممنون از درک و همراهی همیشگی‌تون!
🌹</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/iaghapour/2547" target="_blank">📅 15:42 · 03 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚀
معرفی پیام‌رسان دلتا چت و سرور Madmail
🔹
یک پیام‌رسان امن و غیرمتمرکز بر بستر ایمیل که حتی در زمان محدودیت‌های اینترنت هم به کارتان می‌آید! با پروژه Madmail می‌توانید به سادگی و سرعت، سرور اختصاصی خودتان را بالا بیاورید.
🔻
ویژگی‌های کلیدی:
- امنیت به شدت بالا: رمزنگاری پیشرفته و عدم نیاز به شماره موبایل.
- مقاوم در برابر قطعی‌ها: امکان راه‌اندازی آسان رله‌ها روی سرورهای داخلی.
- اجرای سرور چت‌میل تنها با یک فایل باینری (حتی روی سرورهای آپدیت‌نشده و بدون اینترنت بین‌الملل).
- پشتیبانی از تماس صوتی و تصویری.
🔗
لینک گیت‌هاب برای بررسی و نصب
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/iaghapour/2545" target="_blank">📅 13:15 · 03 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✍🏻
دوستان، اگر برای باز کردن تلگرام و سایت‌های مختلف از روش
MasterHttpRelayVPN
استفاده می‌کنید، حتماً حواستون به این 2 تا نکته مهم باشه:
۱. آی‌پی شما تغییر نمی‌کنه:
برخلاف فیلترشکن‌های عادی، آی‌پی شما تو این روش همون ایران می‌مونه. در نتیجه سایت‌های تحریمی براتون باز نمیشن و حتی ممکنه سایت‌های حساس اکانتتون رو به خاطر آی‌پی ایران بن کنن.
۲. جیمیل اصلی‌تون رو استفاده نکنید:
یه سری گزارش‌ها به دستمون رسیده که گوگل ممکنه اکانت‌ها رو مسدود کنه. با اینکه هنوز مدرک زیادی وجود نداره و قطعی نشده، اما بهتره اصلاً ریسک نکنید و از جیمیل شخصی‌تون استفاده نکنید.
۳. نسخه اندروید رسید:
خبر خوب اینه که از امروز می‌تونید نسخه اندروید این روش رو هم نصب و استفاده کنید.
🔻
ممکنه مواردی رو من پوشش ندم ولی کانال
IRCF
که یکی از قدیمی ترین و بهترین کانال ها هستش میتونه راهنمای شما باشه.</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/iaghapour/2544" target="_blank">📅 13:09 · 03 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⁉️
جواب به سوالات پرتکرار شما + بهینه ترین روش اتصال با پروتکل DNS
🔹
توی این ویدیو به پرتکرارترین سوالات شما درباره ساخت فیلترشکن جواب دادم. در نیمه دوم هم یک روش فوق‌العاده و بهینه برای اتصال با پروتکل DNS رو به صورت قدم‌به‌قدم آموزش دادم تا پایداری بیشتری…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/iaghapour/2542" target="_blank">📅 17:08 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqPuFYaposCwkI6Ch61JqkEG38evuh0dI43-MkFXdxZMxWhDPXNp6mkc-23JNE1aJVe3M5CvXFLA8KvOL6EXI9513TgZsxWzrC5g92EGNiugNVxmQq79KqMtIdy78k2ojoMJ1SvwRbmPYztagaZXqmfkekiimuZfHXJ0eNjLbwQxJPdDi9Nwhs2fcVoSHUGsYuKx1LMSFFFB0aom2n17xMeUcSvghT6Nq08RNx-X225YMIb_MqFmwJ_na7joaX5WrmQhZRALDM8oQinMJv7CMSNTCDEzH4HF8of670bXvqbpCtoXXI7pXyTWShnChun7x1HwWm2rXN3IzyCmFXxLrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
جواب به سوالات پرتکرار شما + بهینه ترین روش اتصال با پروتکل DNS
🔹
توی این ویدیو به پرتکرارترین سوالات شما درباره ساخت فیلترشکن جواب دادم. در نیمه دوم هم یک روش فوق‌العاده و بهینه برای اتصال با پروتکل DNS رو به صورت قدم‌به‌قدم آموزش دادم تا پایداری بیشتری داشته باشید.
🔗
لینک ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
🔻
دانلود فایل exe اسکریپت
#آموزش
#فیلترشکن
#dns
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/iaghapour/2540" target="_blank">📅 16:25 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvtBY-OSFnDFqAUfxV15GjyhsMI0CS_J7mRupTHSBs3V0IsY4rRDJNMdtYO5DiHx_Wp3a1BFMRiVp-SfZQCoKs-syeJy1LkIdOlSmmgGL1sldwyfuU8jjOZXcLXlGsg3fiQ_uzhNGXrrGrdAw0w_ghheN2HZrHU8aTAp10bim40M7H-DQgOuNRRatkmNG9Otgd1KQgUzRWkY2zRUTXcZ7TepVuA0GjWvIY9KCCiCc-95Ywmh0XaxntGIZCZQkIzN0kxHE89CkGFtNfoqEAA4zeQJU30RqWv7t2rJ6NlS8ye4A46pzrhdvpZmpA6rGT_JFCkxOiWCX5bfzBwfinapdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
درخواست ملی کردن کامل اینترنت فقط برای طرفداران نت ملی!
🔹
هرچی از طنز ماجرا بگم کمه :) یک
کارزار
ساختن و گفتن کد ملی طرفدارهای نت ملی رو بگیرید و اینترنت رو برای اونا برای همیشه ملی کنید :)
داداشایی که سنگ اینترنت ملی رو به سینه می‌زنن، بفرما این گوی و این میدان! لطفاً اینترنت این عزیزان رو روی کد ملی‌شون برای همیشه «ملی» کنید تا دیگه غصه ما رو نخورن. ما خودمون یه جوری با این اینترنتِ پر از فسادِ بین‌المللی کنار میایم!
🤣
🔥
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/iaghapour/2537" target="_blank">📅 01:02 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بچه‌ها حجم پیام‌ها اون‌قدر زیاده که اون عزیزی که به عنوان پشتیبان داره همکاری میکنه با ما واقعاً نمی‌رسه همه رو سریع بخونه یا جواب بده. شرمنده‌ی روی ماهتونیم و بابت این موضوع از همگی عذر می‌خوایم.
🙏🏻
🌹</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/iaghapour/2535" target="_blank">📅 00:37 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⭕️
آپدیت مسنجر سانگبرد منتشر شد
(
v0.9.0
)
🔹
با اسکریپت زیر میتونید روی سرور ایران یک مسنجر شخصی برای خودتون و خانواده بسازید.
-
📥
قابلیت آپدیت آفلاین برنامه از اسکریپت
-
🔒
رمزنگاری Client-Server
-
📃
قابلیت Context Menu اختصاصی برنامه
-
↪️
قابلیت فوروارد کردن پیام
-
🗑
قابلیت پاک کردن پیام (یک طرفه و دو طرفه)
-
✏️
قابلیت ادیت پیام
-
💬
قابلیت پاک کردن خودکار پیام های متنی
-
📜
امکان دریافت سرتیفیکیت 6 روزه برای IP در اسکریپت
-
♻️
دستور بازیابی دیتابیس از بکاپ در اسکریپت
-
🚫
دستور بن کردن یوزرها در اسکریپت
-
✨
بهبود UI/UX
-
📜
قابلیت نصب سرتیفیکیت با فایل های کلید SSL
-
👤
دستور ادیت مشخصات یوزر در اسکریپت
-
⚙️
قابلیت تنظیم پورت دلخواه برای nginx در حالت نصب با دامنه
-
🔧
به همراه رفع باگ های متعدد
اطلاعات بیشتر در گیت‌هاب
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/iaghapour/2534" target="_blank">📅 00:31 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">2 تا آموزش عمومی و خوب در پیش داریم.
👈🏻
یکی آموزش نصب و اجرا هوش مصنوعی لوکال و بدون اینترنت.
👈🏻
و یک آموزش کاربردی و پاسخ به سوالات پر تکرار شما.
فردا یکی از اینها منتشر میشه.
💚</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/iaghapour/2533" target="_blank">📅 00:26 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✍🏻
همان‌طور که احتمالاً دیده‌اید، اخیراً آموزش‌ها و اسکریپت‌هایی (مشابه Spoof SNI) برای دور زدن فیلترینگ یوتیوب و برخی سایت‌ها منتشر شده است. البته قبلاً هم شاهد موارد مشابه بوده‌ایم.
دلیل اینکه ما این روش‌ها را در کانال قرار ندادیم، درخواست بعضی از دوستان بود! درخواستشان چه بود؟
اینکه روش‌های جدید را «پابلیک» نکنیم
تا مبادا هزاران نفر از مردم عادی از آن استفاده کنند و روش بسته شود؛ در عوض، فقط یک عده محدود بتوانند با خیال راحت از آن لذت ببرند. واقعاً عجب منطق جالب و «ازخودگذشته‌ای»!
😇
ولی خب به هر حال، کانال‌های دیگه این آموزش‌ها را منتشر کردن و میتونید از اون ها استفاده کنید.
این توضیحات هم بماند برای آن دسته از دوستانی که قدرت تفکر دارند و متوجه ماجرا میشن. :)</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/iaghapour/2532" target="_blank">📅 00:25 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔻
آتش بس تا اطلاع ثانوی تمدید شد.
🔹
ولی اینترنت باز نمیشه. چون امنیت به خطر میفته. این که 2 ماهه سیستم خودمون و حتی گوشی رو آپدیت نکردیم و آنتی ویروس خودمون رو آپدیت نکردیم و.. خیلی به امنیت آسیبی نمیزنه. حداقل به امنیت ما آسیبی نمیزنه :|</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/iaghapour/2531" target="_blank">📅 00:14 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">💢
رئیس شورای اطلاع رسانی دولت: قطعی اینترنت موقتیه و یکم دندون رو جیگر بزارید تا دشمن رو به یه شکست ذلیلانه بکشونیم بعدش حتما وصل میشه و به شرایط عادی برمیگرده.
پ.ن: کاملا از ثبت نام اینترنت پرو در رسته ها و شغل های مختلف مشخصه دارید راست میگید.
👌
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/iaghapour/2529" target="_blank">📅 17:53 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔻
گوگل و گیت‌هاب دوباره باز شد!
بازی موش و گربه شده قشنگ!
🧐
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/iaghapour/2528" target="_blank">📅 13:31 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⚠️
گیت هاب هم بسته شد
احتمال موقت بودن یا اختلال هم وجود داره!
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/iaghapour/2525" target="_blank">📅 11:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⚠️
گوگل مجدد فیلتر شد
البته وقتی سرچ میکردی سایت های توش رو نمیتونستی باز کنی پس خیلی هم فایده نداشت! مثل این میمونه که بچه رو ببری ویترین اسباب بازی رو بهش نشون بدی ولی بگی حق دست زدن نداری...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/iaghapour/2524" target="_blank">📅 11:44 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gz3d-_KKNU2u8GUbuP8hs4l9LVbz5QYJZ8SEmiyskkYO06HUwjoCfF3pdr6747EQXoHJxzruTRmurnExWly37aic2y1oGdNygTdbJkBbZwCoy2vdEW2QGixF17XFcNugZUvxCe7LNHjD-g2H_xGBx6h3imO9cIX8VU-QLhT3fiLSiXpH4rT4gNNVjqifbtFIBRlPhnUiPUGrQEHY8-fZC_fopUBUPSJ6B11P4XxaR3lrMo0dGsBwsYBCue7V4O1oJewUJyne8ixPthHOEEekDyTui8J_Abst4g2joGDpKRmeKOUn7vl0ieDaN_5KEUkBypze21l2yUB16qz3CKBpKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استارت اینترنت طبقاتی توسط همراه اول!
🔹
همراه اول رسماً از طرح اینترنت طبقاتی خود رونمایی کرد. با افزوده شدن بخش «اشتراک پرو» به منوی این اپراتور، زین‌پس تنها افراد خاصی که فرآیند احراز هویت را طی کرده باشند، امکان دسترسی به این سرویس را خواهند داشت. گفتنی است هزینه بسته ۵۰ گیگابایتی در این اشتراک، ۲ میلیون تومان تعیین شده است.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/iaghapour/2523" target="_blank">📅 00:27 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfYwEvhfnd_QErzPoIxdCUZXKrqcvum_YpyHwuB7Klg-vYSCqsxwv1XxNPNC-Xflh1w_Yu0v6_FB8-ZyIjZiOXkvE1WauTxshu1JouP5nY4CUHCpG7gENiPM2l7MHiGvcbrClZbL7yVXHYJm-anSsCTFRj2p5tUVTLVxTa_7XKxNmK8ab8D_pnHxhy3EJl92OIqusaKIiuhJwXptHnEyUGT4qoRJPwAFlZxW5xWdiZwHNI3eXhjv3AiZb_98LEgetA2sHXh3x8nyXhFzpPvcUNz7fjPbjwsZS3hhCP_wMMdoN1hNegUkzJDmFk_W0znaDOz4E90EC21mVJO_uSkoag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
چرا جهان، زندان دیجیتال ایران را نمی‌بیند؟
بیش از دو ماه است که اینترنت در ایران قطع شده و میلیون‌ها نفر در یک «اینترانتِ» محدود و ایزوله حبس شده‌اند. کسب‌وکارها نابود شده و ارتباطات فلج شده است، اما در کمال تعجب، سازمان‌های مدعی حقوق بشر خود را به خواب زده‌اند.
🔻
چرا نهادهای بین‌المللی خفه خون گرفته‌اند؟
سازمان ملل سال‌ها پیش قطع اینترنت را نقض صریح حقوق بشر اعلام کرد. اما ظاهراً وقتی نوبت به ایران می‌رسد، این قوانین چیزی جز کاغذپاره‌های نمایشی نیستند.
اگر اینترنت در یک کشور غربی دو ساعت قطع شود، دنیا جلسه اضطراری می‌گذارد! اما ماه‌ها حبس دیجیتال در ایران، ارزش یک واکنش قاطع را برای آن‌ها ندارد.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/iaghapour/2522" target="_blank">📅 19:45 · 31 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8XidzF8i_m_Hq4sCELsRcSuX23B3UoV7Sp4gXuhsrCn2PqcUBvgHNulMVQAMtW4TuZEo1DE_HeU1yva5Gcg8TKUc2vd20dIsY-wjrfL3DeJ4Cilcxmldw667Ju77rRLz5BIuAPE02fnD2D7vpnExLxbYmJcXUh3CF8a_tbP8gNwcgnEvxXoDpHfBt3WMsUAHcDKdkJlHKlCtcTDVVU5hqKBAo_nSupCmYZ_H4A5KWp0EPimPvA9OzXJ7tHQdIHz2gbYEw-B4RwxN84DTDNT4WDpbRKBgII2OE4vhQ-wStjxUfEx0uQkM1eJ2lr6Rv5u9l6cjJbXQh31Uo6WJ4Ct5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین کانفیگ فروش دنیا
😊</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/iaghapour/2521" target="_blank">📅 15:30 · 31 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
موج حملات در کمین سایت‌های آپدیت‌نشده!
تو این دو ماه اخیر که اینترنت ملی شده و دسترسی‌ها به شدت محدود بوده، یه خطر امنیتی پنهان اما بسیار بزرگ، خیلی از کسب‌وکارهای آنلاین رو تهدید می‌کنه:
عقب موندن از آپدیت‌ها!
فکرش رو بکنید؛ تو این مدت چقدر سایت وردپرسی و پلتفرم‌های مختلف داریم که هسته اصلی، قالب‌ها و افزونه‌هاشون رنگ آپدیت رو ندیدن؟
⚠️
خطر اصلی کی خودش رو نشون میده؟
دقیقاً همون لحظه‌ای که اینترنت دوباره به حالت عادی برگرده و دسترسی‌های بین‌المللی باز بشه. ربات‌های مخرب و هکرها منتظر همین فرصت هستن تا از باگ‌ها و آسیب‌پذیری‌های امنیتی این چند وقت (که پچ و برطرف نشدن) سوءاستفاده کنن. با وصل شدن اینترنت، باید منتظر یه موج گسترده از حملات هکری و بدافزاری به این سایت‌های بی‌دفاع باشیم.
🛡
چاره چیه؟ (همین الان دست به کار بشید)
آپدیت دستی:
منتظر آپدیت خودکار از پیشخوان نمونید. فایل‌های آپدیت‌شده افزونه‌ها و قالب‌های ضروری رو (از طریق منابع در دسترس یا شبکه‌های داخلی) دانلود کنید و از طریق هاست یا FTP به‌صورت دستی جایگزین کنید.
بک‌آپ‌گیری فوری:
همین الان یه فول‌بک‌آپ از دیتابیس و فایل‌های سایتتون بگیرید و تو یه فضای امن خارج از هاست ذخیره کنید.
محدودسازی دسترسی‌ها:
موقتاً تنظیمات افزونه‌های امنیتی (مثل Wordfence یا iThemes) رو روی حالت سخت‌گیرانه‌تری قرار بدید.
🔄
حتماً این پست رو برای دوستان وب‌مستر، طراحان سایت و صاحبان کسب‌وکار بفرستید تا اونا هم آماده باشن.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/iaghapour/2520" target="_blank">📅 14:32 · 31 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یادتونه یه زمانی می‌گفتیم هوش مصنوعی قراره خیلی از ماها رو بیکار کنه؟
هیچکس فکرش رو نمی‌کرد یک روز سیاست فیلترینگ و نت ملی و... نزدیک به 10 میلیون آدم رو بیکار کنه!
بیش از چند ماهه که هزاران کسب و کار نابود شدن و هزاران آرزو مردن! پاسخگو اینها چه کسانی هستن؟ تا کی قراره قطعی اینترنت ادامه داشته باشه؟
#اینترنت_را_وصل_کنید
#اینترنت_ملی
#DigitalBlackOutIran‌
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/iaghapour/2519" target="_blank">📅 11:30 · 31 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-cvbIEvuA5QYYJBZa8COeet0cyIJKJmLmJ3Jji7mGW_6VWV-ISkBql_1uV1XR4BIUbR3IM2agiiFyU9ia2OsGRZ_DDS4Dg-ewbR4U2IqWbheZkR9HUmflp0Ly5jHK0-pNP57k-PR5hBZT-eoMvWGf6MdJMiYrgVeX4rjkxmCT931yzkuNfA8IYm4jLQ1L9kBauUAsEhVgJSdAL9BvNYR2zeVemp0KBBi17o0lvOAu0mmlFvQq8SfkW1Skiu8dPCrsit-unl5mbDPrOTWu1eBVrasJyx8oo-MA-FazaA8psAgvSDoJgbkgWOwK9SjFXiCU8Cd3mfRnkUNS3v65p_3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
تعطیلی پلتفرم «کاموا» در سایه جنگ و قطعی اینترنت
🔹
پلتفرم فروشگاه‌ساز باسابقه «کاموا» پس از ۸ سال فعالیت، به دلیل بحران‌های سنگین ناشی از دو جنگ و ماه‌ها قطعی کامل اینترنت، از فردا برای همیشه به کار خود پایان می‌دهد.
🔸
هادی فرنود، بنیان‌گذار این مجموعه، ضمن اعلام این خبر تلخ اشاره کرد که اگرچه در سالیان گذشته توانسته بودند از سد چالش‌های اقتصادی و قوانین دست‌وپاگیر عبور کنند، اما تحمل بحران‌های اخیر غیرممکن بوده است. او این تصمیم را فراتر از یک اتفاق تجاری دانست و کاموا را بخش مهمی از زندگی خود توصیف کرد.
🔹
فرنود به مشتریان اطمینان داده است که تمامی هزینه‌های آن‌ها به صورت کامل مسترد خواهد شد. وی در نهایت تاکید کرد که رسیدن به خط پایان به معنای بی‌ارزش بودن این راه نیست و کاموا یکی از مهم‌ترین تجربه‌های زندگی او باقی خواهد ماند.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/iaghapour/2518" target="_blank">📅 23:33 · 30 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNZQ2vjWPH6VdjZHBwKyUzvjsneV_ZiI6HMKjOoiInlWumrfZrHAE0v7wS1WoYdr5RrBKWOByJFf2fwqEdwyROzPzkNl1rx58AgoDIg-h0S7A0vW6BAQL8mU-y_KPEiZTYabku8cSvmXVup_PO3pGKV3yDCDhB1W6K35YuGlF-t1c4Ci7hHZUMbSYdLRRE3OdqlHMnJtzXVYFZLMtXsFnWWy9GSWPYVQ3NQfoh841NcFUkUjTo-EnsUzsNVd8BhZP7erARpexdmU3L1ipLOXA9-Tgoowo9M6YTp-2UsVLANb0k9tt94n6iDjW14meiZ5iBjxR9xoEKlNjfA1aSUEEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت بحرانی اینترنت در ایران؛ رتبه ۹۸ در میان ۱۰۰ کشور جهان!
📉
تازه‌ترین گزارش انجمن تجارت الکترونیک تهران از وضعیت اینترنت ایران (زمستان ۱۴۰۴)، تصویر بسیار نگران‌کننده‌ای را نشان می‌دهد. بر اساس این گزارش، اینترنت کشور را می‌توان با سه کلمه «کُند (رتبه ۹۲)»، «پراختلال (رتبه ۹۶)» و «محدود (رتبه ۹۸)» توصیف کرد.
📊
آمارهای کلیدی و نگران‌کننده:
🔹
سرعت پایین: میانگین پهنای باند در ایران تنها ۵.۴ مگابیت‌برثانیه است، در حالی که میانگین آسیا به ۱۳ مگابیت‌برثانیه می‌رسد.
🔹
اختلالات شدید: شاخص تأخیر (Latency) بسیار بالاست و تنها ۳ درصد از وب‌سایت‌های پرکاربرد برای کاربران ایرانی در وضعیت مطلوب و پایدار قرار دارند.
🔹
فیلترینگ گسترده: با مسدود بودن ۳۹ درصد از دامنه‌ها، اینترنت ایران از نظر میزان سانسور پس از چین و میانمار در انتهای جدول قرار دارد.
پ.ن: به نظر میاد این آمار فقط مربوط به سال قبل باشه در صورتی که تو کل سال جدید که 1 ماه ازش میگذره هم اینترنت نداشتیم!
©️
زومیت
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/iaghapour/2517" target="_blank">📅 22:45 · 30 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A862fac6qd-swNVhltwk0dcJ5gjlJob7C2UyURjUILe6mAOlJ3Lbf72xX2dtlgLTLN8ynPwl1Oa-R5dzSbrs8xqzETDanytZxz-NwWGKy88Y9IUd1FeJVdpMszc15dVYythD75jMaHAgrTdeOwHsvXi8BS6uumcVeX0CubB57_DRTxOK3L5UTADQDWLLXubWU-C7iskis0AB6uzBtdP7KTb1oq8DfXOzlZ1HOCdakra14DTeQ16WJa1Y3Dse1B_GFR2ZXHPUHq3CFspzmQBUquoQuUuYucZ0pvH8pEnzp6x-0JEFKV8G1W0UQUEbXJ-JQRgQVAGD6Q2tDr5BhJqN0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
معرفی اپلیکیشن Range Scout؛ اسکنر قدرتمند DNS برای اندروید
🔹
اگر به دنبال یک ابزار حرفه‌ای و در دسترس برای اسکن و تحلیل DNS resolverها هستید، دیگر نیازی به سیستم‌های دسکتاپ ندارید! اپلیکیشن Range Scout یک ابزار کاملاً رایگان و متن‌باز برای اندروید است که این کار را مستقیماً روی گوشی موبایل شما انجام می‌دهد.
🔸
این برنامه با موتور اسکن قدرتمند خود، به شما کمک می‌کند تا بهترین و باکیفیت‌ترین Resolverها را پیدا کرده و آن‌ها را بر اساس عملکردشان بسنجید.
— اسکن منعطف:
پشتیبانی از اسکن دقیق روی IPهای تکی و همچنین رنج‌های کامل IPv4.
— پشتیبانی از پروتکل‌های اصلی:
موتور اسکن DNS با قابلیت پشتیبانی کامل از هر دو پروتکل UDP و TCP.
—
تشخیص پروکسی:
قابلیت بسیار کاربردی تشخیص DNS Proxy به‌صورت شفاف (Transparent) در اسکن‌های UDP.
📥
لینک گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/iaghapour/2516" target="_blank">📅 21:53 · 30 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnWUQcgSXENR8d-p_MBLPTN9JtfjeL8aKrnnxWqriO6faMWsthPpATiLwA_dwjThlaX962LsUZGA6_ZusE-4dssBACp5TJz7wne3rZ9f7zUFnDRN2of-ikBIndvFXP_1gm2gB4G92RkgLC42inZVDjqisZM3WeW_MVptBGpHYh6NaF3vSww5KoKTYtiVTm8D9vyGpuhExOgmRVMqbG0k38avUfjJUBVNQJuhMqbofpS596eE-Hste0haMdwxKUuksQbi-7L-AkOO-VAl5qcD60de9UvTS4cRGzwSSH1gtqK8cIaj8WC3fhw2nEaU1fncZLP5DP2rsy5noy6ANxhPfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی ابزار MasterDnsWeb
🔸
این ابزار بدرد کسانی میخوره که، روی سرور ایران میخوان نسخه کلاینت MasterDnsVPN رو نصب کنن و از طریق وب مدیریتش کنن.
🔻
ویژگی‌های اصلی:
🔹
قابلیت ساخت چندین Instance به طور همزمان
🔸
قابلیت مدیریت و انجام تغییرات کانفیگ و ریزالور روی وب
🔹
نمایش لاگ های هر systemctl و قابلیت ریست کردن و استارت کردن.
🔗
گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/iaghapour/2515" target="_blank">📅 20:28 · 30 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-poll">
<h4>📊 به نظر میاد لیست سفید داره اجرا میشه و فقط به سایت‌هایی که خودشون باز میکنن قراره دسترسی داشته باشیم.هیچ نشونه ای از بازگشت اینترنت نیست!⁉️نظر شما در این‌باره چیه؟</h4>
<ul>
<li>✓ همینطوره و قرار نیست باز بشه.</li>
<li>✓ باز میشه بزودی.</li>
<li>✓ بعد جنگ باز میشه.</li>
<li>✓ نمیدونم :(</li>
</ul>
</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/iaghapour/2513" target="_blank">📅 01:24 · 30 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✍🏻
چندتا از کانال‌ها لطف کردن و تو چند روز گذشته کانال ما رو معرفی کردن؛ به همین خاطر افتخار این رو داریم که میزبان چند هزار عضو جدید باشیم. :)
🔻
دوستان عزیز، به کانال خودتون خیلی خوش اومدید!
💚
فقط یک خواهش کوچیک دارم، ممنون می‌شم پستی که
بالاتر
براتون قرار دادم رو حتماً مطالعه کنید.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/iaghapour/2512" target="_blank">📅 00:36 · 30 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmfA_Nxv_o19PV3Jzys88UZlbfi9ByRbp1-iaiM6e0wky6qaFyJhM3SCojz0IjKdLt8XRkGihTApT2CI1kKP3uEMCRlfoP56U_AqMGW_RnrjIyuSDT7gTh3MNBSYzWBNKfByudNOgHrmlzMWdJQchp4RuAiZuxoi-1iWtujpw02Q-QCqYzFVVORQ8mKaQtOYrJ6ZxA5B66DKq_0SDztSzqOpJG5EuQS00vHsphFhRD01Rkm_H4SsiHghSExfJ6UuH0nE26Wi3Fngj5iYZgpKLlZ0_UkNKsbSuwXirjhMYfrKMCagyoiDngaWIUvMcnulWuvdcdSr3EiomtKJqXPsVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گیت‌هاب در بیشتر نت ها و دیتاسنتر ها باز شده
سایت گیت‌هاب (GitHub) به‌تازگی روی اینترنت‌های مختلف و دیتاسنترها باز شده و در دسترس قرار گرفته اما ظاهراً ماجرا به همین سادگی نیست!
🔹
طبق گزارش کانال IRCF:
ترافیک سایت‌های پرکاربرد برنامه‌نویسان مثل Github و Npmjs در حال حاضر به‌جای اینکه از مسیر عادی و بین‌المللی خارج شود، در داخل کشور به رنج‌های داخلی (شبکه زیرساخت) هدایت می‌شود.
⚠️
این یعنی چه؟
این اتفاق به این معنیه که دیتای شما در حال عبور از یک مسیر دستکاری‌شده هستش. این نوع مسیریابی غیرطبیعی (Hijacking/Routing Manipulation) میتونه خطراتی برای امنیت داده‌ها داشته باشه یا نشان‌دهنده‌ی پیاده‌سازی سیستم‌های مانیتورینگ جدید روی ترافیک باشه (یا شایدم من دارم اشتباه میکنم).
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/iaghapour/2511" target="_blank">📅 23:28 · 29 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⭕️
لیست لینک های مهم و کاربردی (سری دوم)
این لیست، یک راهنمای جامع و دسته‌بندی شده از تمام آموزش‌ها، ابزارها و مطالب مهم 3 ماه اخیر کانال است.
=================================================
🟢
بخش اول: شروع از اینجا (بسیار مهم برای اعضای جدید)
🔸
لیست لینک‌های مهم و کاربردی
(سری اول)
🔹
پاسخ به پرتکرارترین سوالات شما عزیزان
(حتما مطالعه شود)
🔸
چرا آموزش عمومی، تنها راه بقای اینترنت آزاد است؟ (حتما مطالعه شود)
|
لینک دوم
🔹
مراقب کلاهبرداران باشید!
=================================================
🔵
بخش دوم: مفاهیم پایه و آگاهی‌بخشی
🔸
وقتی اینترنت ملی می‌شود؛ چه راه‌هایی واقعاً باقی می‌ماند؟
🔹
اینترنت ملی چه تبعاتی دارد؟
🔸
چرا الان خودمون فیلترشکن نسازیم؟
🔹
دلیل حمله فیلترشکن فروش‌ها به کانال ما
=================================================
🟡
بخش سوم: ترفندها و آموزش‌های عمومی
🔹
آموزش ساخت کانفیگ محافظت شده با Npv Tunnel
🔸
حل مشکل گیر کردن و لود نشدن سایت‌های ایرانی در زمان اختلال اینترنت
🔹
اشتراک‌گذاری فیلترشکن از طریق هات‌اسپات گوشی
🔸
ابزار رایگان تبدیل فایل JSON به لینک Vless و...
🔹
توقف کامل آپدیت مرورگر فایرفاکس، کروم و ادج
=================================================
🟠
بخش چهارم: آموزش‌های تخصصی عبور از فیلترینگ
🔸
آموزش VayDNS و MasterDnsVPN حتی با ضعیف‌ترین ریزالورها
(پیشنهادی)
🔹
نکته بسیار مهم و اصلاحیه درباره تنظیمات VayDNS
🔻
آموزش ۴ روش اسکن بهترین DNS سالم در موبایل و کامپیوتر
(برای روش های مبتنی بر dns نیازه ببینید) | چندتا از پست های پایین تر همین پست رو مطالعه کنید.
🔸
دو کلاینت اندروید برای MasterDns منتشر شد
🔹
آموزش متنی SNI-Spoofing
|
لینک دوم
🔸
کمی توضیحات درباره روش Spoof Tunnel
🔹
پیاده‌سازی همزمان NoizDNS ،DNSTT و Slipstream در یک سرور
=================================================
🔴
بخش پنجم: آموزش‌های کاربردی و مفید
🔸
قبل از تانل زدن ببینید: آموزش تست ارتباط بین سرور ایران و خارج
🔹
آموزش نصب آفلاین هر اسکریپتی روی سرور ایران + نصب X-UI
🔸
آموزش گرفتن سرتیفیکت برای دامنه پوینت شده به سرور ایران
🔹
آموزش ساخت ربات تلگرامی برای SSH زدن به سرور
=================================================
🟣
بخش ششم: ابزارهای کاربردی | اطلاعات مفید
🔸
اسکریپت کبوتر برای دریافت خبر از تلگرام با DNS
🔹
پیام‌رسان شخصی و رایگان موروِب
(قابل اجرا روی هاست)
🔸
نصب آفلاین مسنجر songbird
🔹
راهنمایی درباره کامنت‌های یوتیوب و ربات تماس با ما
🔸
درباره تبلیغات تلگرام و کانال
🔻
ممنون از حمایت و دلگرمی شما
❤️
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/iaghapour/2510" target="_blank">📅 20:20 · 29 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">💢
هشدار اتاق اصناف درباره ابعاد فاجعه‌بار محدودیت‌های اینترنتی
سخنگوی اتاق اصناف ایران با اشاره به سهم ۵ درصدی اقتصاد دیجیتال در تولید ناخالص داخلی، ابعاد خسارات ناشی از قطع اینترنت را بسیار فراتر از پیش‌بینی‌ها دانست.
وی تأکید کرد که رویکرد «دسترسی گزینشی» یا اینترنت طبقاتی برای واحدهای صنفی کارآمد نخواهد بود؛ چرا که در صورت عدم دسترسی مشتریان به شبکه، عملاً بازاری برای فروش باقی نمی‌ماند.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/iaghapour/2509" target="_blank">📅 18:39 · 29 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">💢
در حالی که دنیا با سرعت نور به سمت پیشرفت‌های نفس‌گیر مثل هوش مصنوعی پیشرفته، مأموریت آرتمیس ۲ برای بازگشت انسان به ماه، و هزاران نوآوری دیگه پیش می‌ره، ما اینجا اسیر یه چرخه‌ی تکراری و خفه‌کننده‌ایم: هر روز باید اخبار رو چک کنیم و ببینیم که بالاخره کی قراره این چکمه‌ی سنگین سانسور رو از گلوی اینترنت‌مون بردارن.
این وضعیت نه تنها فرصت‌های برابر رو ازمون می‌گیره، بلکه ما رو از جریان اصلی جهان عقب نگه می‌داره – انگار که به جای پیشرفت در یک مسیر، داریم تو باتلاق محدودیت‌ها دست و پا می‌زنیم.
امروز وارد پنجاهمین روز
#قطعی_اینترنت
شدیم.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/iaghapour/2508" target="_blank">📅 12:07 · 29 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✍🏻
یه سری از دوستان گله کردن که چرا من فقط به کشته شدن بچه‌های دی‌ماه اشاره کردم و حرفی از بچه‌های مدرسه میناب نزدم.
تو فضاهای دیگه چندین بار راجع به این اتفاق تلخ حرف زدم و ابراز همدردی کردم. ولی با این حال، مگه میشه آدم به این فاجعه فکر کنه و دلش خون نشه؟ از دست رفتن بچه‌های معصوم میناب واقعاً قلب هر آدمی رو به درد میاره.
این غم خیلی بزرگه... به خانواده‌های داغدارشون تسلیت میگم.
🖤</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/iaghapour/2506" target="_blank">📅 21:12 · 28 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">💢
فضل‌الله رنجبر (عضو کمیسیون اجتماعی مجلس):
«دسترسی به اینترنت فعلاً به مصلحت نیست و این ما هستیم که زمان وصل شدن آن را تشخیص می‌دهیم.»
✍🏻
پ.ن: آدم می‌مونه چی بگه! بیشتر از چند ماهه که با این وضعیت، کلی کسب‌وکار رو به مرز نابودی کشوندن. حالا به جای اینکه بابت این خسارت‌ها شرمنده باشن، خیلی راحت میگن «فعلاً مصلحت نیست مردم اینترنت داشته باشن!»
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/iaghapour/2505" target="_blank">📅 21:01 · 28 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">می‌گویند وقتی سنگی در تاریکی پرتاب می‌کنی، صدای کسی درمی‌آید که سنگ به او خورده است. این روزها شاهد دست‌وپا زدن‌های حقیرانه عده‌ای هستیم؛ همان‌هایی که اینترنت آزاد را که حق مسلم هر انسانی است، به چشم یک تجارت پر سود می‌بینند و خون مردم را در شیشه کرده‌اند.
✍🏻
هدف من در این کانال از روز اول فقط یک چیز بوده و هست:
کمک به دسترسی آزاد شما به اینترنت.
درد شما این است که من و امثال من، با آموزش‌های کاملاً رایگان، دکان شما را تخته کرده‌ایم. درد شما این است که ما به مردم یاد می‌دهیم چطور بدون پرداخت هزینه‌های گزاف و «گیگی فلان قدر تومن» که به جیب شما می‌رود، به اینترنت آزاد دسترسی داشته باشند.
من هیچ‌گاه نیازی نمی‌بینم وارد حاشیه شوم یا پاسخ کینه‌توزی‌ها را بدهم. تمرکز من فقط روی ارائه بهترین روش‌ها برای شماست و بهترین پاسخ به بدخواهان، همین استقبال و حمایت شماست.
دلیل وقفه کوتاهی که در انتشار آموزش‌ها افتاد، دقیقاً مدیریت همین حواشی بود. وقتی منافع عده‌ای در خطر است، با تمام توان سنگ‌اندازی می‌کنند. در مقابل این هجمه‌ها، سکوتِ کسانی که از این مسیر استفاده می‌کنند، کمکی به ما نمی‌کند. این مسیر دوطرفه است و ادامه آن به حمایت و صدای شما بستگی دارد.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/iaghapour/2504" target="_blank">📅 15:00 · 28 Farvardin 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
