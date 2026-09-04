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
<img src="https://cdn1.telesco.pe/file/tcKSGmeFex1wtc5tUrxkfmlQTfJ4d588Vzm7CxJGLhdnkTn94yZegkigMrphtloa0R3b8MI3t_IKtX8lGorAwK-FrBIdLQIQQQvyzBBcSrquvcN6ECVO8DnHpaHrj7cCcfK2nB3NOsySJwNLSskNtEpCOAi0_RSSnhpxp5gCKSF7VPCm1ma8u3AMfCriOkeTYJemkeCJf0PdH9AaXExzYabOu_LwUUISEKgLoPH_RQ47ahe6Fyb25qrESFPRmMw6vPa4mtmX30oCU2P9GlacavHSSBsj-Ucd7bZaOX8hKV3ayc59DuQcyVwmzTMrYVs0se2q0uOqcQomGLc_g8rZ4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 20:46:44</div>
<hr>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=BnEKwNTt3Z64PrFnMaV4pZYjs_SjZvU_EfdYiJOMC6C9xH_JFCyLJ7lqvGIXeueDu9AdfEhzXKZQGvF3jrPsnLT1o-bSiJNusH9gMFt1-GWNAMP-8mOWp9c0lLkW-t4hy8NVwB_zkx3JegHvIcw6Njkm2GHhKVDjEZ8ztl3Ac_t4EebfPMyUokZvBy-mlQOgNKJpfSpiIUAi7Zi6HN-a5FQ8azUxJsEZGw2Wgexp_K8Z1omCysIHQs9lD3ADVeJOKS8PSW8c5IHGB_byy3pYnmc_haoVYiAA7bRX5-jN0pvUYdLFVVmDAejaxTpkeNNAoKGIQKH3cm6IsShKBs62hw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=BnEKwNTt3Z64PrFnMaV4pZYjs_SjZvU_EfdYiJOMC6C9xH_JFCyLJ7lqvGIXeueDu9AdfEhzXKZQGvF3jrPsnLT1o-bSiJNusH9gMFt1-GWNAMP-8mOWp9c0lLkW-t4hy8NVwB_zkx3JegHvIcw6Njkm2GHhKVDjEZ8ztl3Ac_t4EebfPMyUokZvBy-mlQOgNKJpfSpiIUAi7Zi6HN-a5FQ8azUxJsEZGw2Wgexp_K8Z1omCysIHQs9lD3ADVeJOKS8PSW8c5IHGB_byy3pYnmc_haoVYiAA7bRX5-jN0pvUYdLFVVmDAejaxTpkeNNAoKGIQKH3cm6IsShKBs62hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل
GPT
-6 Astra بالاخره اومد
💻
بعد از چند هفته شایعه‌های مختلف، OpenAI دیشب مدل جدیدش رو با اسم Astra رونمایی کرد. گرگ براکمن رسماً گفته «فکر می‌کنم رسیدیم به AGI» و که خب فکر کنم بیشتر منظورش AGI ِتنظیم بازار بوده
😂
1- چی فرق کرده؟ برخلاف نسل‌های قبل که بیشتر یه چت‌بات باهوش بودن، تمرکز اصلی Astra روی کار کردن مستقیم با کامپیوترته: پر کردن فرم، کار با اکسل، رزرو نوبت، جست‌وجوی شغل، حتی دموی ساخت یه صحنه توی Blender و بردنش به Unreal Engine. توی بنچمارک OSWorld 2.0 حدود ۷۲.۶٪ گرفته (Sol حدود ۶۵.۷٪ بود) و کارها رو تقریباً با نصف زمان قبل انجام می‌ده(حالا اینکه هزینه‌اش 2-3 برابر شده رو کاری نداریم مثلا)
😑
2- کجاها واقعاً می‌درخشه؟ توی کدنویسی و کارهای عاملی طولانی، ریاضی و علم (توی FrontierMath Tier 4 حدود ۹۸٪!) و امنیت سایبری که توی ExploitBench صد از صد شده. برای همین OpenAI قابلیت‌های تهاجمیش مثل ساخت اکسپلویت رو برای کاربر عادی قفل کرده و فقط توی برنامه‌ی Daybreak بازه(فکر کنم همین بود که رفته بود Hugging face رو هک کرده بود)
3- داستان اون ۹۹.۹٪ چیه؟ OpenAI گفته Astra توی ARC-AGI-3 نمره‌ی ۹۹.۹٪ گرفته که واقعاً وحشتناکه. ولی وقتی خود سازمان ARC Prize با harness استاندارد خودش و API خام تستش کرد، نمره افتاد روی ۶۲.۷٪. اون ۹۹.۹٪ فقط با یه harness اختصاصی خود OpenAI به دست اومده که حافظه‌ی استدلال مدل رو بین مرحله‌ها نگه می‌داره، و هزینه‌ی تستش هم حدود ۱۹ هزار دلار(4 میلیارد تومن) بوده. پس این عدد رو نمیشه مستقیم با بقیه‌ی مدل‌ها مقایسه کرد.
4- توی مقایسه با Claude چطوره؟ این‌جا قضیه واقعی‌تر می‌شه. توی بنچمارک‌های خود OpenAI (کار با کامپیوتر، ریاضی سخت و...) Astra جلوتره. ولی توی Artificial Analysis Intelligence Index که میانگین چندتا بنچمارک مستقله، Astra نمره‌ی ۶۱ گرفته؛ دقیقاً هم‌سطح Sol
😂
😂
، و پشت Claude Fable 5.1 که ۶۶ گرفته. توی Coding Agent Index هم ۶۷ در برابر ۷۰ برای Fable 5.1. یعنی توی خیلی از تسک‌های واقعی استدلال و کدنویسی، فعلاً کلاد جلوتره؛ عوضش Astra توکن کمتری مصرف می‌کنه و برای خیلی کارها ارزون‌تر تموم می‌شه. (حالا اینکه Input Cache اش چهار برابر Fable هزینش هست رو کاری نداریم)
5- قیمت و مشخصات؟ هر میلیون توکن ورودی ۱۰ دلار، خروجی ۵۰ دلار، کش ورودی هم 1 دلار و کش Writing هم 12.5 دلار؛ تقریباً هم‌قیمت Fable 5.1(به جز Cache که فیبل 0.25 دلاره) ولی ۲.۵ برابر گرون‌تر از Sol. پنجره‌ی زمینه حدود ۱.۰۵ میلیون توکن، خروجی حداکثر ۱۲۸ هزار، دانشش تا ۳۰ آوریل ۲۰۲۶ آپدیته. توی ChatGPT هم گفته می‌شه سهمیه‌ی پیام Astra روی پلن‌های پولی کمتر از Sol هست طبیعتا(بله AGI تنظیم بازار)
6- دسترسی؟ فعلاً فقط سازمان‌های محدود (برنامه‌ی Daybreak) بهش دسترسی دارن(مثلا ادای Mythos رو در میارن). توی روزهای آینده میاد روی ChatGPT Plus و Pro و Business و Enterprise، از طریق API با شناسه‌ی gpt-6-astra، و روی Azure و Bedrock هم در دسترس قرار میگیره که برای ما ایرانیا زیاد اهمیتی نداره. ما اونقدری پول نداریم که پول api بدیم خوشبختانه
حرف آخر: روی هوش عمومی و استدلال سخت هنوز از Fable 5.1 عقبه. گویا توی طراحی Front و سه بعدی خیلی بهتر عمل کرده اما خب، متأسفانه اون هم نمیشه اعتماد کرد. سر Kimi3 و Fable 5 هم همچین مقایسه‌هایی میکردن تهش گندش از آب در اومد که اینا پول گرفته بودن الکی قدرت Kimi رو خوب نشون بدن و خلاصه تا خودتون تست نکردید، یا عمومی نشده 7 سپتامبر، اعتماد نکنید.
منم هیتر GPT نیستم؛ صرفا واقع‌بینانه مقایسه میکنم. وگرنه همین الان اشتراک GPT رو دارم خودم و میدونم اگر روی هارنس درستی باشه، توانا هست اما خب، چه فایده وقتی Ox Alpha انقدر قوی‌تر بود ازش:) متأسفانه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بچه‌ها من یه ده روز نیستم کلا و مسافرتم
بعدش قول میدم حتما استریم راجب دانشگاه و انتخاب رشته داشته باشیم و ادامه‌ی استریم‌های Rust
تا اون موقع مخصوصا بچه‌های کنکوری سعی کنید تحقیق کنید کامل. از بچه‌هایی که مسیری که شما می‌خواید برید رو قبلا رفتن، سؤال بپرسید.
دانشگاه دولتی رو بررسی کنید
دانشگاه آزاد
حتی پیام نور
ببینید هدفتون چیه؟
شاید دانشگاه نرفتن هم یه گزینه باشه
این وسط برای پسرا سربازی هست
و خیلی مسائل دیگه مثل خود کار پیدا کردن و ...</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BcwwXhTK2tJy36bIl9vCWMc48iJJ_rHTsx6sgGKAQsWKYf7A4NujwsjkTwo-UQpGcVgdZc-YJK6a4bOejJKo7mWK6-OORdnvYlf3-09nkIeOoHQ0XVzluWDGcFIuvPzVt9h56p5331nf_rIWJHiQLxGNl3RsG92SW8c0x2bABZAkGA4e4MDXkECaMdwQaWmQW0RkzQ0By8CuynoK9VByPLNKiWr2D6E9ex_46T41vimwRwJ5DXz6u8njY_U7gu_XIerYaz_CkRUqjyOQ48bHBLpKdmc9R6lDSgrjSfwYfwAbK5sFNOv-ZhHXaE0PdJ5DDVF6HtN7Q8LrXw5C6yDO0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NJwsxIv8uT8niTAKbk2zTEZflKgCbid0ibVtta2rzZCMk09rrQFLlEnBUavz1mJJ6QHQz2Ce5xEYi4bnSi1d46CsE-TZuZ1xjHuVl2Yvy58n_jMgS7OHwq_SIPMEVL15CxM3fVhMRZHumKTdcldJy-HvgHfa0w4EnYoAA0CWPgJZf1BWlhhvgIprF-cxIWiIm3u8XpjTDKJ0j7xvxbU70ts74oY94ELbqykQTjzbO-ORwEl5Bu9KMyQJt2GGZ0Hr8Hc2me_P300FZDo-_34jw-P0ZJP5xyf3tSH_R8q7Q9aYmrBYCj54EZ8WHrzFUga3vJRVBBKycXhm9IX-muTEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uZMDODnRuLS5_x8ye64QM8YE8lNarqRnFnNgP6Berm-ZH014UG9_IQLTFaISY1ifZyT4rbyPxVJtlSfGAERvIFwdB6WhFUlhM9VN7RJvisfeuUjRibiR_zmFu9wPogcT-ZB9KA4Z93xH9iIdOOGk4II7pN4sMfn2nvNZ6Dg_ipfqOInVEu380y1XDtsT_AFZO4D8n4fQ4iR_o082WFKU-D7dZtZ-2-SnUChcC9Q0NwYu_NVNwx451sj2uk8aOI57zMzpV65KN9iukl_1nYJ-7BXIxjU5-mqCEiYZyulnauJdYYjr13bnftiU2_d9EDTqdGukQILqsaJysttsPDePHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aRVUelBdYf8gJ72fBHDAI_vOvoaomhp3X-2-TumRHRe2Bx3jbwj6UJvLDs48J5O9qK_w1w7q7Xvkq9oKzKX_1qGhobVu3CszL3Gt0FDM6k5XzEL1tSmDZWF5oNNjlr-a7F08FasP2bnacimn3Yly0l9z0YCqC5dsZ7eJZWSFY6m9sr4OVgThydfSNkkvQ1_E3YCpe_Au1qQ5YRqg1rRtsfd0eLFQ6b6bJ0oUtUJMG2n9MgNrpyvsr2Y5fXY_2plaE3_yGb3aJMlrOar8v5k_gMsn6TbrE_NNTZg8q3W4dZeA3FFxyWFhGHzjf0yKXcjXwSIWeVOX3sKlFrvqlss0Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RfdbCUvI5jkAnlFnvoiram3ZrNsc6jtQhlzUzGMhAR2GJXYvJNru4oD5_hveNyy3Hnp0g8f7GLBzah6Wx-X4Z9P7JsQhoUhRDwaZzvX4g3ipkpVZLsFp2bOFnGMn0v76frOzsc_V8vj-C0UJbYFtm6jT8FkfIGPj7HYLKN1tNME_V2Q4XfTEXWea7sZuuQSZFps0a2QbMuewbonhovrE-V39szfnBgRzS5QPQrJ_LME0rY18nf5_tp6nuXcIQkIe-1njXFWnbl2rwFjmeqdcViKdNCzGCSOWdkpHJoSqMOeHwzqORRnv8VA09y5Ix8v71TeyWGa2jA8JZZ43_MRkNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FHGDGlp2bkSrXtdJkTjogdIDJMCvmxD756XwGUAIpLlDkn7UURHDZc3f0sXd9uKb1iugk0rl-JMGcQ7wr2tsP0joXXZNHu3V-8YPaFAOhGx6lhyOBrzX6Ug09OzT403TRYnUIZdYSDxalMw5L-hWIR0dRCPzp54z0GGolr25o10vTvBvo2INSIDQ9jvo_vh0JHfKK_vbquQRW0x6w2knCoqjSYhEfJJZsaLNaQTJ3cDsZXXIBudJbNF_UzNTjE41faBVcqSfnKY4b1g133vUg_pCTvAD_eyefbNpW-hWXChMDAuKTo9nNZS06p1k7SVvVXFiTl7MmLxottEVsxzB4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KpBZyx2rY4ElA8xjM1pGhm6yrgNSBKYBBQS0jFSJTRioGxXVV2KbKE-lwtt2mcsVb9lZ5UiyWWIQJhxD4mGvxTfVBre0yK-9QB_UdZOBBqOu2dBLSwgEf_QlvS1njRDKdk7rwfV-E-jx9WoFYnVF9OYsvS9zhM0cb-1Z0oXrjfQhn9DWq_phuzhByhI09Wgxv_BHVbhltChlSp04uWobLl5vSyF7V5yXn5dpM8xXIHls3sFy_k1uR4YY8cffk6gxO0xzvpN578nyCJT3gTZvFde9TCzjty1i8icy5s_uK39M6qMN25-JH33v4nHFLpduYxp7BYX21NTw8bfhSegkwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UC0tllpU9e2Ot6lVDRLDUkYpP8TNIdXCAg5KF_P2x8Lo2ZLC2h9MnfS3-6SD7bXAhZ29beRy7zWpfEKK8jac0c6OFCxDFEYmuchq3kcupddkCPJHTdZUvp97gQGHn2frSMr5E7jf9tAzC99Lm-D0CRZG4T0pLKUCmOMjyxREWrGP34UBmut_5N0tE4jZCD56qkFIhrQcaRpZ3HVOQrvb78RrbL3zoiXofFh7pDOQHoCsdMVCImgttFVxSIve6-mWFWD_sOKxEn8RejlUCOV6yZ6uLlkY0F3eYssUYPwMlxuZpg28y9vl2eAwhCxFkkvDvBhzNPKklXhohfeFweAt5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VrHVJlgal-1x0Dade3jNoWDa2PM9wc5Tto4Fv7lILvN6PntkR2cuC70ueqB77OGx1QxfDRjd5efsbplXu0vlQ0B6doc18EV91R5XoDZu_-zZxZ7VAI9_bS5xlKIPAdAfFa1ku3APSCQzCrYHuUqYTEe85u8ar1MV9T7qLimPin3UFGHZTb0kZp2Ot94usHIXPVWjekkKofxY3iBnvCmM-i3ZaceNv26c5eFxgJq8ynPbI9zG3amu4b6HVMCE1OlSt78thSo8FLx_EUJh7n3RC_PPs37d66EkA7ofV_vmmuke205KnRisZjJexP4qLck4lpqbplQu1vCMm9kqMyZ6vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ga8dxo0hRUtqErKCn_0v2qmB93j-mylLf1hCKK6io4MMrj-9c3Vwxr-eZ654-Qsg-bGZ4UwNrmaWjuzkk14TX13OXZOas5a3CauUKrF4WYzsf5qI_meBfbEVHZ7dIIKBqva5oeP1jRd1y7eoxjGWokbMpemOSfN_cemv1gZ4xcqlIw3ulZh2ZxM56nnf8VTCOuGDmP_F8iF4MxcUCRzhHp9Y2U4EziAenHvqGxlT9BicpoUUTy_nRcKirNb3G5NyirEt9nWmJIVlWCdqVC70k4PM0u7tVF8rsc9deyUjund8MenBLssyYDuctZ942ySbbvABuf0Wf0KMXQRCc1nyUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Kc0Ah0h0I6_nesWoI2pN9eYEL21Ulq6CVHZcpJ1x_3dqXEXPnLSGKg5FGYICsVrPlb4kT5HAMMtUooHKzj2sllo-2QLkURyXzDjiR7k44R139MvkBV2W7jHjml4hQ7syH-7BngYCQCp1PJmfPTZTXFfc3suVB8wQaVNzS4UjjPfnNeT2Ycn5ao7LF43W6cxo-A0Xzbnq66OJdx9sb7n8fCgW3oVTz3f9g7y-gc5WYWM0hMtz6HuuJJdffQEi5jwqs2hhOEHU_O_bGzQbQSk-XcncSVIHOAeRaWat497VRiMU4KKh3-JZEvcIQN_3sS_r3RCG-qhKIzEtCKe5Maiffg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نمیدونم چرا انقدر از مدل Kimi 3 خوشم میاد
زیاد هم فرصت نشده استفاده کنم توی تسک‌های سنگین
اما در نهایت برای کدنویسی، compatibility ای که مدلهای کلاد با خود هارنس claude code دارن رو هنوز توی هیچ ابزار دیگه‌ای تجربه نکردم</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/5163" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o6JvtoOK6RYbi--ibdFOnjFhsNIHDBFbxnYtFZrpepkqfwnbWNEtOom5jxUATiAOQTmOAFojk0Z6Tvs0_aKI1WRFXlRgKZZmGXAXMPHmjh0-VyDBCyjN5w2jCfReJYD9hmoPBSC9tkE7usGzC3AiTEUZiu3fKBLpa1by9klDodAZsF1pXtFj7SHRzVoSSk8GoqJr1Xd_IjHaLe4X36doxsQBE9dleuXqtuktIe9S1jo3ON7lU88baV0ZOQcIkoZPOLN5H6KFzjkjApxeT7acAB1jKZpyco5YF09LYtTVdo2wKxLK3d0_tS2k64WzRlWIC8WHOvnpQMGraDNjHujjfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/adeIv7abP6xDFjCwUsf3P-wUqM22hdzkLe6BcoAiQEyQxavwfrO_azOpNdj3BXwosolvYa9Mqs0rr0iXqQFipY5m5rueUuVGmJlJ7S4SrWVP0D_tEYKKyHjJEUMB6XV-pR45dePsHFDt8gdWDdFMrPWMbzY9QZZLd739lKPYeCFNbQiJrshItXKBRPWERxjyd2XASeVkfqvOMO-tHf2avBgW-u2iDTC_fGm2wkO6Zj4s5E_jTLqntPEuhekHHR71sPgwXrxRz87nfk81a-YpPE6hNFGivthqkj81jL8Kym3xreXTlideJkmA7BIdl5PNt6r-K_0UbXQ4Pz5O60HMHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dIZ6EJxBrNNXYPix3vLvkSWBbTRZXfBVRDucinYiaPleozZU1I2rHDwW6-bpOCJZCNAxdzJiutvs-l0Cqgh5f57zR6rbnp9mkSHcZwSitQCVL0_5EuacSyDltaYY3SeCA752J2zZduYBMvNZAEsylwlYEkXI4ST8rtl-wdiR-4PNYOBNI-c9oAdF5Lqhf5-Vz8pzN8h4Cf5pOlcvLmxx-rEzuigU_jeGJCx10QkN10qoRcqxYTdq77102OzEjTnQN3lgafr3rIP0ebcGEe5VFRC-VTN8wm39kMASw0Qcoko5npeS7XYSeE0SSJuz59dC5MXaicaAL45H8A46uslhiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا مگه میشه مگه داریم اصلا  حس میکنم خیلی اغراق و بزرگنمایی داره. امکان نداره قدرتش از Opus 5 انقدر بالاتر باشه توی این بنچمارک‌ها:) باید تست کنیم</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5160" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کار کردن با مدل Fable 5.1 به قدری گرونه که می‌ترسم بهش سلام کنم لیمیت هفتگیم تموم بشه</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/5159" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vJJiMeB-eq1mPPU9g4_18EnIEpiYmTpUCCGmBEZ9-Kf6npFdO-1QbyFh1C7_Ns5OklbDUjESpViwyNhm_lD5gPt2MVKd2V4HSr1b7yzLFbTxvbzf9-6oPqlroTzsPztmCO_-62C1CKCBIzrk15_LeE2W7c4gJknTcrnsPLySGubjhO7T_lbQCmgktWUP75ihLRd3mB-NnGMt95l1ZpwuB7p-nZOZ0OotT2ZZUEFjt8fH_UdR0G9G0TTusHDUe4io68rinuqg5I3bmHOVvoIuq8v5t9l7X7L-98ZUWIwRRENYXFpWwrHXDwIAA9sbCjIO0nUNimpzs8khPfI-Qkrj8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K-G1nV_HAnjGkZwGxo0RsZWYwwqfxkjMdqDXMgN1N_BXclMJepLUvV7vwv-C7hDZ9iIE7KRjFvJ2QfPYwYTzpW6rG-ItAvz5eQ8WF99DZvbJRbTAmRV0eL7rJLydOgsEEOPCRnpGYvKOJGGqpFZGaS78yLA1iX_ITPtL6cwtKBucAdlnPmZkMBHgTw25LwN75eeAqTWaDq16o6E24I-NTwewaGcYFe8TsL_wZVfQR7AQEV5ug8vy8Re-0QqX_-DrcC4Sq_nyLwmGUf8VU6m4cbw13PZ_BZvXoKJduoSGDWpWlgMBZLWOeBbBIXAXjX-NSPvUkqypwVgOwETa-e6iQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EzAOWx1UYavAHfLA3Zuq-SLNfDvueXP2YPt0MjL79rHOugwEOl3ShFmPxx3VVjIbIcqYlm-I1RTkzuPv9moV0_2NdDbrDLS60ehWpZtOF2CU9YP3uGlgAhN6w2K78zB9dak2IYFui3qHYzCl_Klxw5g6t9SwdFjFDA7mZjH9ZJDKSrKHnO4CNarzn7P5IA87iLP2NXrbGggV7SDUvfS_Ebg4H0yFoS5SlKnRRy3La47fUc-TgCyRryNcWWDmvO4fxfKxvwWXNIKtKlOP0oGeRTFuvaLsQf2ZU2040kxW1R13x8YaVYMA_WOD7Oltu1L2MXCOe22sgOsu1FuzEMDfTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم
هم Gemini flash 3.8
فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5154" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سعی می‌کنم آفر و... خوبی اگر باز دیدم که بتونید با این ویزاکارته بگیرید، بذارم واستون</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5152" target="_blank">📅 17:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud  این سرویس Free Tier دائمی داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)  و همینطور با این کردیت می‌تونید دسترسی…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/azCrTe6YnbrL0hnsiE6UQaWH9oKqMzX5km8z2ZPum11w-0xE1OzghknpRyr3ubFx3pY4RyM1Iyx2GjGtvszoDtIsF8bTAt6VdY6d5oMg7epIBuK3Idg5LwavOM2dK7bDklGKylv1yPHVElWTOO8SG0CmuvaLiJ3PxltcxaXIcTDunuikt8Zs-thXtaBduf9mvRLptoLCgWAJa4llCkwrq6LiYn4zU_8WSgEv-7E28ayR-yTUaFZ0U_vDFfckURW0RvjAw3uAQA3xbWTLwAqGqUdrq4BsOFwUscMI6A-p8UVmL2dNjod5XY1XAdZLsQxTeGLP_TiUuu-eUPGDczb-KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud
این سرویس
Free Tier دائمی
داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)
و همینطور با این کردیت می‌تونید دسترسی به
بیشتر از ۲۰ محصول
محبوب مثل Compute Engine، BigQuery، Cloud Run و APIهای AI گوگل داشته باشید.
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://cloud.google.com/free
بشید و روی Start free بزنید
3- این قدم رو من حقیقتا چون واسه‌ی خودم جواب داده میگم. میتونید بدون این هم امتحان کنید. ابتدا از
https://policies.google.com/country-association-form
درخواست تغییر ریجنتون به امریکا رو ثبت کنید
4- تایید که شد، توی سایت آفر گوگل کلاد، ثبت نام کنید با یه آدرس فیک امریکا از
fakexy.com
5- دقت کنید که برای این کردیت باید حدود 10 یورو موجودی داشته باشید. و این برای من کم شد و در عوض 257 یورو(معادل 300 دلار) حسابم رو شارژ کرد. برای یه سری دوستان یه دلار خواسته بود و نمیدونم داستان چیه
6- من تونستم بگیرم و تا الان هم مشکلی نداشته. دقت کنید من تمام مراحل رو با یه آیپی ثابت امریکا رفتم و لوکیشنم رو هم امریکا زدم با ادرس و همه چیز، تهشم با گوگل پی پرداخت کردم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u_4cqibIsdg-JYMfIUyr5I-L20RMl3LDMUjN7sbGmim78ikE4f0zCvok1x0TUxGiaCmWKVrVA_rOcZ-DRUQRWzkK2-wNUvP4ziG29DVS6EBWDCAqgdHXBS3U-dhFv3nHdOFAELNCdVdCFfTPhYVW4dZoR0uSe6EKXNEKXVJgimAfiwaxHzRuA6aMlFlVaJU2fXY_tls0vIRkQURvSe7yh9GwW9-8gTsQMW6sjwGUySkTtToXnsmAMrmiYXzO-rtp31y7RDk_SgLAKOb9oD_ZcFSuBU3woL_tsd9HFQ0eB0cwDwa8Dyl0i2qqphjURoGx-DnJRq1TN6grFeEpOzEvGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cJ1ahSK7jMwxWVDnwZXnMroZxpVK3ooENTPaAt55TjprfwL57GtAL2VrpHN4DBgAnCZK95RddV2MtadE4Q6NzuFqUyvluy8xl2N9bkNjmNVEDwTIzaUVhwsHego8RlTosSaFLgAlQZbY4yCTQmgvIgPKQMKOtlYNyzv-oi0ymXSLW6QCD8JqAymbBMe_7VqoAHoy7o0lIZm4ONK1S_X-ay6V3HDMdm0wEWXC2B894mJ9JknhFJ170_LqT7dyrdk6Xo_oMnyh9Oq_kbvc_qV166DYnZgGG9fiMytXSO--dGyNlU3T-G99Qz9yVILspGmK5Gg0zNBiw-0Ii6T83WRXAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pFIf99x2XPuWMHAkHLyf_aVhW2FhxK044rI8MONRPHK4JCI486iyMWw02VYFcAL_Ql_M66kCeOXXEHm_MPPuFjNxdYaAxpAEmd6tDiG6ccwlgVwktqgxJC9WhuYk1sjkzKSvITygzC7Q0nHIKlthZ243qxGSu10u4MF-WCDy99_YWfxMeyoOiruwr0ReJheRMfU8bMpqGtPc_zHCJDS7OfLPgzDRMcIVGQy82zxqc-mz69UKHaAmrCDykJJqdr9Lu1ctXj5IkmiNXWwjCyulgBcUQsiuv1WfFP_zeT5XJipn1DJuyVDll_xwGq1D7MogbovY6ubp6L8IKXFsJGFy4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">و دوستان، با این کارت نمی‌تونید کریپتو بخرید. هرجایی بخواید کریپتو بگیرید نیاز به احراز هویت سفت و سخت داره
راه درست و خوبی برای نقد کردن پول توی کارت ندیدم من</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5144" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bzJTAvM3iI9PxAekaRbEP22DpuUM0kUMo2KWLIjfv5lHv3XNxj_vhiwSifkCUsagu2PmmlI29tKDPEppEDW4qbKq_hkkqnSbsOc4EVeEo72O5UHidwkRpUQ8_-ZPirVQgDuhr-Zi4se-3GybClVAnL0jbkHFHAfR0n6kiSInchmNjUtZ8Qkju-qLZ1Z3AGvRpWHEY17oolCsQQuTimL2HWliALozSLY0KRRjchTgqdhKi2o98J2hBK5iMGRUwxfL8owHKe6FN0Tg4WGGwhBJNaJvOtJ3HINFceWlcT2_BaKokM696VYZe5LsoIMu2gus_3qjb_xWCG_ceOLTsj-olA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشستم دارم به کامنت‌های این ویدئو جواب میدم و دیدم ای داد بیداد:)
هیچکس نه دیسکریپشن رو خونده نه کامنت پین رو نه تلگرام
متاسفانه تغییری که سایت Mpay داشت این بودش که دیگه با پنج دلار و ساخت کارت، اطلاعات رو نشون نمیده. و من هر طور تونستم این قضیه رو اطلاع‌رسانی کردم
برای دیدن اطلاعات کارته باید ۲۵ دلار رو واریز داشته باشید و گویا این قانون رو برای جلوگیری از سواستفاده و سیاست‌هاشون گذاشتن
من سعی می‌کنم به تمام ۲۰۰-۳۰۰ کامنت جواب بدم که هیچ ابهامی نمونه.
این Ai جالب یوتوب هم که دورش خط کشیدم خیلی به درد بخوره</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5143" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5142" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">چشم روی هم می‌ذاریم دلار ۱۰ هزار رفته روش</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5141" target="_blank">📅 09:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بچه‌ها من می‌خواستم آموزش کردیت ۳۰۰ دلاری Google Cloud و پلن Always free اش رو هم بذارم اما واقعا خسته‌ام. فردا می‌نویسمش واسه‌تون.
اوراکل متأسفانه خودم موفق نشدم؛ به شدت گیره روی آدرس و آیپی و...
اگر موفق شدم روی لوکیشن خاصی، بهتون میگم</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5140" target="_blank">📅 23:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pRi79TFOVkXWRmoAqdokI4ldomWRIrXJfFcGccMqVOoO5sd59SPgwwBWsj7wre1dg7hE8pW1aQV_7LDFeHVBmN83SfVlceaWbIwRsVG01uuKoVzVW_y8dH6wQQkn5z1voVb5yry-AwwQILt89-imVVFUmCwDHorPUp9twMFLTop_XFPevXSPXfNHb5Nd1kFCocELZ9LRQn1GJXNKBmabYVDcB9UT1ron9ISi_Srpc3XT7eG4yTkivDSEhbOeuOilRTHQ6h4VVEOlgIX6lLa1de7DGrLdVNQr5bbgLEpBvcb_fC99LGhq345wAEI8oXjEvXrJmIM5pB_o9PrnwRautg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربیات خوب یکی از دوستان واسه‌ی استفاده از آمازون</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5139" target="_blank">📅 11:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وی پی ان رو ساختم. باید از بخش Networking، پورت ها رو اجازه بدید استفاده کنه. بعدشم پنل سنایی نصب کردم و یه اینباند TCP+Reality ساختم به راحتی هم مستقیم کانکت میشه بدون تانل، لوکیشن آمریکا</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5138" target="_blank">📅 11:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bjmnxQ_cZc2Tuws286Pr29T-UWLJrW_J_6KOWcFaQKmDWJckJgy3dydGZv0QvVOCNL2zH1X0Q6WIC_kq_6Ry9Wz4N2hpHIvp8ahYKx1fxtcsFvxwvd0dThuoDpty4N7whTyX-wnO0EFtjA2cA3csa48vsA4lTLUDWfcG67ZlTrab928FEPs_S153bhyaZKgPcV_Fi5q7C8M03c_PtSx3t-nMHNbqAd-9uf6YNK3GlSwGZAlNvSmfmPLND95LOVGk9mmzin9qZWcDISIWk0v4lASm5Z5OPsKp-3ykcV5RQ05lUlda2Fzcns9gRzys8K1lujNFVh4XSdpAxuDOp0YRiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5137" target="_blank">📅 11:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZkjCx4uPGjujodrBvsWoldrV9NxO4HrYRUlDO38poL-60_5hK6HmrX9LZtUjdwIDurlsSxBMRjOiVMDNWPszvbRdBf_-zeibTRuJ7tUM5ExPHd2LAB7OfCXVcNTQ3CZuWHNKPlfz_BFCaqYRt54rfpFMHsI6RCaiziz8ZjMVCF4hmRQZoUqrMxv01Jb_73YnN7eXVc_U1JAJx1QznYqv3DEd0DyXRpsOCkWr7s8j_O3v6Bj03e0ADn2YS5g_ghb0RQ6n0jgP45RgAaZSKD5A5uqsz-EF1Z1O4AKNM9CgkMsEToYSbYCwlLhOgJOD1R7zw4sljvrXVnFio6UIF8z1ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری از دوستان میگن که اکانت ممکنه ساسپند بشه اما خب.. خودم هنوز ساسپند نشدم این ریسک رو در نظر بگیرید رفقا</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5136" target="_blank">📅 11:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون  با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)  1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه.…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5135" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fNqBCga-KvGhFAyw8M120NCNyYJC2WwrvnYjqP5jjy3fMZLbuN11r4Yrtd-LKdrQ-TdOgY-JuJSzm2k4vAKrHkiO2XznTLYjJ7QXt9yYXT1QvD9IN5CU9bQM7FNFjHm-nHYbQYips-st6Hqb3CM1Xygpr0KCnNz4ybubOqqqNH_dnRu_PNNaMUUOu77oLRKXRquqh4PGng3L3cPn1TRPnED6vjBpDKsGsH7LXqLAynYYKXzXip6QDjBHkLfJNtd2pqPt-Ca65RSrnr8AzqoRcQdVui3VuCFOOFA8_2MaKlqRb1UoTVY7c-cn73MkFFnkl-y8uHQpQXq5SW6UBUv59Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5134" target="_blank">📅 10:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gos88vPIaccXdmPkP2twR6kAgCJxy4CfeUu2m-Xt3BniDNWpRTxFP2hBJXmcc4m5DxoUFhuxUHeU0fARD9ZlMwo1f1PdAxvFiLSCi4kmecZ0iY6OiRnAzAJq-meUeFWUnB5V1TGnqe8M321N0yc5Dq9TpjBVzFj_UvMnzR3eZBv98o2b4jyO8N7urNxLnCIrrKV4J5J-dkOVkm5qYuX8m6BPSsLuft_0G3lxvk06iqz9X3_KWy7l0bHiVV7LQQMFNqB5MrXHp2w_J0Y40JMYzM5W-1abrtgFJIBRMl9hQVwhcGTsd61h57dt0ZTI0ys3qEuehE-Aw_SFuKoRf3GMMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/m9GkvEmbd1DoA-u24R3R5d_H4fVeUvcn-r3Mw6n_jRmELtbKbgvv4sjtxPVeUVVefSwpCTmrYuOETXpN9T_4SdOCVIlZQCDQKjHfvH7-zwAUgdvbyNepXjQosTwqujnjOhbt9fpTSqwyxEMzw4fWtDDkGquB8E7eOiYutD0P_ItMo-y-1itPIHcYEPDFytTErmkDeHByHmPCWD0y_wxbwCH5eTAEVVZPmrgy2mw1-Op781FmmwTsHv-7XhDi61pTfcVq0puLSZhINmcQF-ugwIz-Gy6kApuyi8ZV9FVHvN8wxfVZSwyF8bqZFzAUmzvLk-fm0Is538HVBG_nnsPSjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vlhiiUhPpKisR5a7jRw2NKC6iBpDqCnFIuttVH6zQV0Wuxr7RMyZ0WDAShF58OyzXe-L6fKianROzDbPyAmN1Vec_gy2T34FA9fWGZtLx0Mu7pLBzBy_2N4qcu59-FyvS3T5QRzLifvouoliKK34n5Q_iK1X06QDfH_SH-C5zm6w2zXZTB1PMr-x9NP8z19nWfLYbhHLVSrDMmiCmJCF_9XHSFF3fJKkFDxZsyHSGVrsIH3frf0uzb-on-tjvuDpE2G3TozXXj1RteDuFT2y_y_n4OC6xmmbtFRop2i5c0VGSgcjapbCt-AqioUQ-bEM1pZWCmzpDxFIiQzxEgKjqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SRDXtnXTADSdzzRq40WiyZ0e1hzZk3ScSfPLbXYe8GXxUqjItDbZz6YZMICSoKFU1UUNJeVWsvvV8tAj0DmmDpIRiSAVfhrjeFKkmZPWMvJg9ibQya3hH4MsCzRDn2lmCAvMKsAvBSN0qB25znY6bdIhggNzdw-W7lx-ZhIibew1pXfVAPQ1_FNkdY2z7HKO2XNRr0uWEOBhGDeUbjcodvMBh-dnDV6IihYejRx4rVsb28ERfdtUMl2M5pJp1YiH8Yjiifk774ZQ1TI_TOLf9yNwrQeU0Mb83ad-oyzvud6oi3e22LnR6tr0saP4PrddRk32c7XcZyvsHRyzV_pe3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون
با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://aws.amazon.com/free/
میشید، و روی Create free account میزنید. بعدش سایت خودش شما رو هدایت میکنه به قسمت ثبت نام. VPN هم زیاد مهم نیست چی بزنید. من با کانفیگ‌های BPB رایگان رفتم که آموزش ساخت اون هم اینجاست:
https://www.youtube.com/watch?v=iAbYpjXyLpY
3- برای آدرس، یه آدرس فیک از سایت
https://www.fakexy.com
وارد کنید. شماره تلفن هم من گوگل ویس زدم اما نامبرلند و سایت‌های شماره مجازی، همه‌شون برای Amazon یه بخش مجزا دارن و زیاد هم نیست هزینه‌اش
4- یه ایمیل تأییدیه واستون میاد و تمام! 100 دلار کردیت رایگان میگیرید، بعدش هم با انجام دادن تسک‌های بخش Explore AWS که تصویرش رو گذاشتم، می‌تونید 5 تا 20 دلار دیگه بگیرید.
5- ممکنه محیط آمازون واستون گیج کننده باشه. نزدیک‌ترین بخش به یه VPS معمولی و راحت، توی محصولات قسمت Compute، بخش Lightsail هستش. چندتا نمونه قیمتی هم واستون گذاشتم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5130" target="_blank">📅 10:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5129">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CgLkpew0Nhzedw-73SzUJBXBruy1FRcjLrB3LZMZgx0gPKDzq0vTjWhaiNH57GQypIwUYfjmNqErZzGP5ufAHkbyRQCSn-ytF99rHRBQ30xUnS4pWmoeESZ8ZgaObQ6ClXb60Z3K_zqKz6LBhCiSskBr6oooQE7wEhnF_Pus5pqu_oXYHzrMPkN9hGT1Ir8PHT0vMEifiN5L86PPLvRCK7-cVK3ihk4jRlXejp2zakRHjOvzPTGgGVS0-9MG9P2UXlp6oEfEND9JSjuLmgptXA-rAkKvTnU1ciB7tulvTnCe3xmAQrD232m8yhQchbhq-Qpsg1Ze-15qhFp7gZ_CCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ثبت نام ۱۰۰ دلار میده بعدش یه سری تسک کوچیک انجام بدید ۵ تا ۲۰ دلار دیگه هم میده
و می‌تونید ۱۸۳ روز استفاده کنید
به نظرم می‌ارزه</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5129" target="_blank">📅 09:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5128">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این کردیت ۲۰۰ دلاری آمازون رو هم موفق شدم بگیرم با Mpay
آموزشش رو می‌نویسم الان واستون</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5128" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خب بچه‌ها من تمام مدل‌های چینی و آمریکایی رو تست کردم. فعلا برای ترجمه، رتبه‌ی 1 رو
Gemini 3.7 Flash
میگیره. رتبه 2 هم متعلق به
Claude Sonnet 5
هست
که خب فلش توی هزینه، می‌بره. رتبه‌ی یک و دو به جهت قدرت ترجمه هستش
هم برای ترجمه‌ی کتاب فانتزی مقایسه‌ی سنگین کردم تمام مدل‌ها رو(از جمله GLM و MiniMax و.. تا GPT Sol و اینها)
هم برای ترجمه‌ی متون تخصصی علمی
هم برای ترجمه‌ی کتب برنامه‌نویسی به زبان عامیانه‌ی فارسی</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5127" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bd6oos7Ecpsq2oyvi-GlvEdDli2KL6rUEPoq-HeCa8F_tc6nzAZAXxfpgJN-93f_5hQX18QWKZVV0R0SAqL6uD-G-62x7TeghxJ2t2qF-8-AeBkCbShe41JjdDTIwaMWDeQ131R1QB_77h1weVFFd5JHixWQkpHP6TOaom6So0vS57qgJ_Q4-GLn_7oclpJtOmnb0f18JU7xFNcdMEh9yhXWAwUbgA283scAyOFwRB9fgRZmdqSOB4rdsgVb_OKwMBx2r4nWT0xN3pR3Kn0rPU1XiSnb446Ki5wXAwrpMwZ4sVaGQuqBn0X5jsnszsqYkZHufY3108DetWdJc1pgBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه دنبال ساختن یه AI Agent برای کارهای علمی و تحقیقاتی هستید، این پروژه رو حتماً ببینید: یه مجموعه از 163+ مهارت تخصصی که به Agentها کمک می‌کنه کارهای علمی رو فقط با تولید چند خط کد انجام ندن، بلکه بر اساس workflowهای تخصصی جلو برن.
از Bioinformatics، Genomics و Single-cell گرفته تا Drug Discovery، Protein Engineering، Molecular Dynamics، Medical Imaging، Machine Learning، تحلیل داده و Scientific Writing. حتی برای کار با دیتابیس‌های علمی مثل PubChem، UniProt، ChEMBL و ClinicalTrials.go‌v هم Skillهای آماده داره.
نکته جذابش اینه که این‌ها خودشون مدل AI نیستن؛ در واقع یه لایه تخصصی روی Agentهایی مثل Claude Code، Codex، Cursor و ابزارهای مشابه قرار میدن. یعنی Agent می‌تونه بسته به کاری که ازش می‌خواید، Skill مرتبط رو پیدا کنه و از دستورالعمل‌ها و workflowهای تخصصی اون استفاده کنه:
github.com/K-Dense-AI/scientific-agent-skills
@Linuxor</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5126" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5121" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5121" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqOPI_h_qVoZOzeNhsffmZNAJ1ok-jnx7rXTedSM4knrwEtj1Z-jT2WEtjmz7fDP9CEX8wgrEXvM4E4HIOtWtvsrSCj07pPt75yp0wPRodb5Km9jf-jbKAWJoo1kEJjDaOilLyguDDCe1Pg6mdrUmlgr0GBuihdqN1pE1zCmIwiwyqqJZayMtwKAA5AkI4H8w8OECaVps0c3K2l6jNBmb4TThZSVmK807mCGxyQ2rJZ15asdL_94YfkEaIACo_ZFuVwVrmMr7KTaOAiZIDDvr2EQo8toHpODAFJlFrTOqW6EmMxuYMl0WdR-O_2IF8vcrOdc7-YujY19Ouwp0yohZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
ورژن جدید WhiteVPN  1.6.4 برای گوشی های اندرویدی
تغییرات در این نسخه:
🎯
اتصال و قطع اتصال پایدارتر. رفع مشکل قطع اتصال.
🔒
بهبود امنیت با رفع مشکل لیک با IP V6
🔭
افزودن کانفیگ با QR Code یا Clipboard
🎨
نمایش واضح‌تر وضعیت اتصال و بهبود ظاهر برنامه
📱
دانلود آخرین نسخه از گیتهاب
نکته:
⚠️
در صورت دانلود نشدن از گیت هاب مرورگر خود را به فایرفاکس تغییر دهید</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5120" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5119" target="_blank">📅 10:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5118" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آموزش ویدئویی رفع مشکل آنتی گرویتی و سرویس‌های هوش مصنوعی گوگل:
https://www.instagram.com/reel/DZ7NWUOMeHy
هرچند ارور ۴۰۳ به خاطر vpn هست و صرفا باید از کانفیگ‌های bpb استفاده کنید</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5117" target="_blank">📅 09:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">زلزله به بزرگی ۳٫۸ در پردیس در شرق استان تهران
در عمق ۸ کیلومتری زمین</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5116" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟  توی این ویدئو، با یزدان عزیز در مورد این مسائل صحبت می‌کنیم:  1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور 2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن 3- تجربه شخصی خودم…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5115" target="_blank">📅 07:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IGVbKeMle1QAcxml2poa_8lzhLhmcbCNEqdN56zkc4xjjy1BIW-wXG-LY6vZGkWAo61kccu2PY3yg4rAfIlGqD705fBqvuEIo7332vhPwxA6QUqrXH_DEzUc_OvnynKaGf_bkPzbg5-XJBhmP3Z8R4t1zxy_E_SAG3LBRcoI1NGinw-0DMRhdkerR-R0BZx62Oer4WDBv5I3F0V5r9OqCJm8VTR55nI6icED64rZj4Ves0L7nHKn8NLtbqZIYJxJht6zDSshfwx6MuSc1AwyvsU2Ore1akrnAgBwEPpQ_NHuWgmnvfGE1nWDH3K-hmBv4DKxtAynHqWecNpEKFxZPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا کنه هیچی راجب
mpay
نفهمن
😦</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5114" target="_blank">📅 07:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مجددا:
این api های رایگان ممکنه امن نباشن پس توی پروژه‌های حساس استفاده ازشون توصیه نمیشه</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5113" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RPU2ysxwd9mqy-JgEl_wNe-AVISqB3qerHsfa9gP-vl1opjf8YT5viuOsN6UH1sxjUx0x9_pc7gfNOG-W1mn0yj9Sw3mgQOpiKTJOD0SI-8hUVhO9UUuj8qWgIXZBvW5S7Znm6uSibYIfhlOUgDXnT2SNm5iyyroXLz0_A3eqwsRqo7WLmiQdB8uLgRfyqIer63WTRoy7GK8CnxUdz3ILSHH1-Af1LxJj0KFHUQJKFD29tbkRBDlb2nQMX2Kkulyv9Hybz23jU-A2PudgfA1BIZACnBtLpJBKuCCf8XmrhimV5hNHtaKs0IspYBwCc3Pzdv0bpH6DR8HOdxBNUGuAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دو سه تا اکانت بذارید و Round Robin رو فعال کنید، خیلی خیلی کمتر احتمال داره که به لیمیت بخورید
تا تموم نشده استفاده کنید</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5112" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a0EuLUMm-i-MP9GHgdVb8Q4ja3QjnsJ8FkpIJJljFa73sj6iCP8_cqKoDul3rBAPY8--0L-7TWcPl0tysBgtd4VsE7axd9a4_T8ikeh3pPNJzGwHq_SpjYna6wlzEbhJnr9rfzDkFzQAWgnUAg0xMHVFrmkZjE1J5Ff-IhzLnHzbD6r32r7-KeZD3M9WCWk1gZIuUKWLFS3uSCESv3a5HuS1FNExkik4IdW_0UBRvm0mCrrNLUbzvAy-V-O1TL3CIsUDX47NWyc1ZzslQzTzm1NK1KwO06IB3xjGFHN44-A9wpLKJA62DL-vP5BcZ1q-iN_MsQxyRp5NVdN65Hzu9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hVFAIdfd--tymWt8pbQbAjoPpVdtDM0Pb4_i5LYZJ17Lo1lXYhC9bpyYEV0UcoaFK0ltV0rcnUsYAGiar9jquKTEX1YTWJ0ldh6n7g04A2Mhvi9VlLc-Vb0QhcWpz0iIabJ0al29CVDJsGoEV5L82qjyO1a23-1zglwYmygwAfzdc-5zqQc-SRn9_BPw3YN6qIr6qg7tVSYTfe9QRHiCEqWL3UDUWTiQUmORpYbLONUIJ9IekilgjZUJCSiSaL13P34pCO89Chqv4GzCUVwwW_X71uH40gfwzT7FVCovWWhvUixmyjB6KTwEwUnjrAh3XCdXwKAXx4SYXZlyPgIEJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها انگار هر api key اش حدود 30 میلیون توکن روی 9router میده
بریم اکانت‌های جدید بسازیم
🥸</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5110" target="_blank">📅 17:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شاید براتون سؤال باشه که من چه کارِ بسیار مهمی دارم انجام میدم؟
باید بگم که 18 تا پرامپت الکی بازی سه بعدی دادم به هارنس کلاد و وصلش کردم به 9Router و همزمان با 18 تا ساب ایجنت داره واسم میسازه
😂</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5109" target="_blank">📅 16:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FPAelbubH4HFtPZshZc_W8NkmWv_8g0WSjIkqVHT1tUjkWpm402F3KjWhRakmZu6PlhiuVvPHLXH7Fy9W8yZDjr9PTKOyvibNUVZKQGlI2wDeEEI93kTsSBoFHf8nMRBGiW8EBS7mwLUrY39S39FGnYdgjazBwnZeq1tGW0Eknn2tQlVq4xtRBijIIBmG7dhLZQeDPnRoxlBAIjiuXf8Qw62s6hDDmWb6uEkNPBZRfKZJeViiOZ2cHzsYWruS-47b5AbFL3cQsQhYJWs-ck439FSuTH-jq6-ZsH5O1XwneWwJ1Tg1i5ajUtCc438_PqrCTy2tGjMiP_LrUknJFrG_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشالا که خیره</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5108" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NGpO6KN32SZ69Jc0ElbKh-rqHsKW1LqPXKMYpz6vO-3tFSpXh08n7OECX1NSF-D_srdOuaaVsgPm9Z4zUx-21B5_th57jJdBSfi75PoM7x9gET6U0sDFQd9yEIzAOcRbFcgttu5Efubv2mPFvvLCm-tAsAobdDXCb-SRXeM-eucjI-OCAiTayRh2E1O4nUP2-RdonprD-DN0-rlyEXYzUT3W66CoiTcrHP_ExkL52T1WuIBFT8cVMnRjfn1LIK-4yka4VjDgicjAVIwkrY-Ox56qCDOjX_a9ZF_OJJrkCRCgU9fBmxIP6un1EFh979aVNg5SYrhZCIQ8sgPy9Mqxbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا از B.ai هم میتونید api رایگان بگیرید واسه‌ی GLM 5.3 Flash یه ورک‌فلو سنگین دارم میندازم پشتش ببینم تا چقدر توکن جوابگو هستش</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5107" target="_blank">📅 16:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mHI9wZClwfumdmr4wX2ZDi2wGgVx1GCOwUzLVhlXGB-gWX0r44mDXdUmRK2tPjZSbY_eeGT-b2Mys4byIO8ZLEHooNcSdAz3dDyNGr6nAHe8GuqPzWdzKdZDuSPBr4oQ0o_S8ic2wSMWuKv07EuELn-H1KWutAErIGEKqUN-gQ_te7KGrBZ2f0Bowa822IAXueGdNYGYEK6bcOwyvnoqg5-SaBfCjowcXex1dc-dMwecSdW6MnO1p2gr9jDQ50MRlFkvrbNexQugZqiwESwz8tFQGv8kRyPoIT8rkMD8vFXieRwruAGIWdrOEl3URMu68a-guxTDOiTosqeYA9AOog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5106" target="_blank">📅 16:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iOsPMdb3NObscg8uffAsvxU4LVd8RAM7l-fBeVO7ar-Nm7fzQ2Jd_wCU-Xr9peNA5HFN-nRQue_g5QAetKUjZnq5xuG324eNIPL91GoQcNV357Q1Ff-eAjSj-VW9-48z-eHaRHMovjWmFG7pK8YBd-O0hwWcGrDfnCLrBTc9IKTtVYAAkacNSQEePT_BYk6WDrxRosUh7t1h-_YqdmUh3RIta8PH03zZ_rqGXH3XWcmjVkfVfO43vX79IBrNxhMpEOFyNokJSGiK05WnUk7e726FQxFVdF4-41O6HMCtK6D1U7Hk4oAvzHgTKXKpB1O08AJRQ5FpBTIc-Jf8t4-lyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
🥰</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5105" target="_blank">📅 16:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KJriZ2M-8rFVsmhG3Z0pAuAi6tqU2hVxINiRB7H2AmW_A-Y8QbK9QCq4iwD8zaOrKRyVRd4ym6RRe-4OUf9dJOHjblhMB3eOMX82E0McIRyMuELo-K6p7PTV1lg5HD3EzcVR3oQiTM3iUppGWMfP4PHnCIQp8Fd6pNXEztRmNxWV78hDzLk1CEs-6Qn6jNTnkPSlTTfyJhCcOrKEehV5JmtCG22GAOlrq7_NKE2OEjhbA1oU9kODUS6sRtbuj5emAny41UfunvxQX7i3oEIjYrQGBk1Q_Zbf_aF9C6gIkaA5dgc52Z6S3jdZa7M359xFQOlfgIwdEvgLoyVWutsNZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟
توی این ویدئو، با
یزدان عزیز
در مورد این مسائل صحبت می‌کنیم:
1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور
2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن
3- تجربه شخصی خودم و شروع واقعی برنامه‌نویسی و مسیری که خودم رفتم(به علاوه چیزایی که به درد شما ممکنه بخوره)
4- تغییر قوانین بازار کار و حذف جونیورها
5- اضطراب، فومو و جو الکی شبکه‌های اجتماعی
6- درس‌های حباب دات‌کام برای هوش مصنوعی
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5104" target="_blank">📅 15:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت: https://app.mpay.cards?startapp=ref_S4FPMh ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر: https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5103" target="_blank">📅 15:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">و آره، منم حس میکنم یه کم ضعیف‌تر شده نسبت به پرومو Ox Alpha</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5102" target="_blank">📅 14:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sXERXqQ5l_pNgJ8QGLS8OtbVU_9ZbCVV9v8lIjB2yo2Ip3XBpTdJw-wMHxKj_wDt1ZKy748tnlc02KEbg3qxRzP2ptKheOlpxQyzo2_89rrc3ATud05L5PfPe_keNIkMX9VRuDHwP9qHzbAavq-tomZg2JsAgbe_pAG-Lkc6vfASVEQjdDr4yZjw8mHwiSxtrS6s_z35Nm5dslQu39QCKorbi3I39W1mM3fHfnrybwKSth3RrlKZWCuT5i9rK4sg8ioxtIg9nyBMnmtc677EHOS2n8FkiUXncfiCxBomwDBqYJWHlTzEG1SJIlwnBPhrjBGxi2Cpp_X6FVIKy0bPJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5101" target="_blank">📅 14:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GK2pLmKnW2xwV1CES8qwnxIsoGPj7M31cX_nQLb9gZvfYxe-Y607O3-sNXCd4vRJW5kmm8uYk0hD-Qmwjo9acl3fFsbjP7HTBF8nw74uI8JTTiv_knzqd9EXh-CDB1k9F_AkyTZgw2MOhsCfa8lOoaBoZKuFco9D5C7uJ9Y62G9867SvJEFOYg2ya6ZCrJVqujtN40PHInUcuUdT8IRJqKxm2zYkpDRYUhaPi7JLmXGObKvFpozPos2XVyHmR-VkT9nYllcXeUe6gN_-Ym2JGFeZR9m66ol3quUIZNMQiqNLRm0PkEQ-yQuiHgWZDnoxH3Xy5M8NBzkk-jptU3BZUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/auupCdnnGsannCae359DyujF96idIU5hpprdIxGd29EfrZjWg2HwnPwIhf9P6tHSJG-Mkw5oufppLlUGJq7S5w6R415B0Zd9tVFWAaNSetLXRimcWNVlLOPBlMdJmG9EvvQTkQgSl39Zz8XemD8N0rbO_GJ5mFjj48S9vd8vTOcmwj3zJC0aNKeUB7rI5A6up6XaXY7Ym9RRPDXo7acsUoVFaothLDIiDeRar0gFNy6mNTJ5VJr6fNo3_JUMTvLz2NPgkBmc7xOSFW0DSeateQUI6w0kkt-cBg9qPZOl8mLySMLkxQO4JyoWoD2ph0Jb-neYf5jSfFj4xLZzd60xlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:
با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.
1- خود 9Router رو
که اینجا آموزشش رو دادم
باز می‌کنید
2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline
3- این مدل رو از بخش Add Model، اد میکنید. دقیقا همین رو بنویسید: z-ai/glm-5.3-flash
4- می‌تونید چندین تا جیمیل اد کنید و استفاده کنید به راحتی
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5099" target="_blank">📅 14:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rBhhknl-SF4FJd0n7mXDVQxLJ_EbniA7m4167tNMKcS75CHr9lU-fF5sgZsXzcdrffB-55aEZRUg7nDXvTrkIKL83_grHWGZDHt2utSaucVCip9YKL9SkIh1UwGG_CzB3mZWEHky6Rrukju2tyGwl9B3SWn6T4FKLSBRmdlLN379LQhwu3_jWStAAOtj-0I0bAYceQJST5O6JKv9AxzyQmQEyupmY8PvC1katimz3uaXf79QzVVFFvE-ct2jfCByOlmS4ATyeKImHxkcOKJK-2Q7r3NutAM7gMrxPWZwJG42XbYy24MUIpGusJSD4aiPPRvCibSNYS913_AjjCLfhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن #ClosedAI</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5098" target="_blank">📅 13:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دوستان من به نود درصد سؤالات غیرتکراری توی کامنت های یوتوب جواب دادم. بخونید شاید جوابتون اونجا باشه
هم راجب کلاد توضیح دادم هم پلن رایگان Oracle و...</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5097" target="_blank">📅 00:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u5quyRbmaFufnWkuAKDqSszfI_iG3FU2_qlxn2ytR9nol0Ku61x1aD7yuX1KEUB50z0W0vn-9T1aR8pX_AzHMKhSfqsGAAIfzm3Mqy50pHnYeCoLQ4l9WpthwBA7PbxLacaucoBT3eVPN6246iXGIA8Ziklqi5sby77CA66M6pyen4QNaXtWhLOH6KD-6qSDBiXwtMdLXBpXeE5Vu1URbgl4cM_SvrTV7ZlPE8GkX8rr9phrIME-g7HV7q8XCGh3zNqpSdkKahSLK4bBBJx3XPygU2JugYP9XGMDMmJzEj0Qv8fZd7A_zFk-NIzj4lEe1A7SYEyORueoGmZLVNk0pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد پرداخت توی بازی‌ها</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5096" target="_blank">📅 23:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cm6wo1dPXSPrkUha17bQ57dtvPR938zTT-dTxE-dJx0TVx8NvTy3R_d49Mx_LyILsGgYHkfb8918pAgpjhRe1-9pMLmVD-zBDSQ1xOutR6uQjSEh1vX0jDPp5xmanCp5iLupMIEKoSsw8q3TzPkqg2ApMMTTE_1mEUOn2a8QxWLDeOSl4tnJqj5ARVeioUhw4eLS7PUo3P30-7EsEApu1P27hzUDt-gGjPChTVcllU0-AsJSFJa1Ev7YG-kuQEkvfnkEKdgv50vFC0fMiWsjj7UDTIWCLsT2uZHWdewUtmoDtUAt6XhM4cFMlTx76y2O27zltsa9z206Kced78H-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها بدی‌ای که صرافی سواپ ولت داشت این بود که اسمشو هی با این تپ سواپ که دوره‌ی همستر و اینا بود اشتباه میگرفتم ده بار مجبور شدم کات بزنم
😂</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5095" target="_blank">📅 23:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">Iran is not for beginners</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5094" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5093">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">روشی که اسپاتیفای رو گرفتم، این شکلی بودش که هی ارور Country و اینا میداد و میگفت ریجنت با روش پرداختت یکی نیست و این داستانا. منم ریجنم رو رفتم آمریکا کردم با راهنمایی از grok و بعدش با خود google play پرداخت زدم کامل اوکی شد
حدسم اینه که برای اشتراک‌های AI مثل Claude هم خیلی ریسک خرید با گوگل پلی کمتره با اینکه شاید یه دلار اینا کارمزد بره سرش</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5093" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ببینید من خیلی از نکات رو نمی‌تونستم توی ویدئو بگم به خاطر قوانین یوتوب. اما برای اینکه پرداخت موفق داشته باشید چندتا نکته هست که باید لحاظ کنید:
1- برای خیلی از جاها می‌تونید به راحتی از Google Pay استفاده کنید. یعنی میرید توی
https://pay.google.com
، کارت رو ثبت میکنید و تمام. اما نکته خیلی مهم: برای اتصال کارتتون به Google pay، بهتره که با آیپی آمریکا وارد بشید که با همون روشی که توی ویدئو گفتم من تونستم وارد بشم. اگر کانفیگ‌ها واستون پینگ نداد، کافیه که Chain کنید با یه دونه BPBای چیزی.
2- تمام چیزهایی که روی گوشیتون از گوگل پلی دانلود می‌کنید، می‌تونید این کارت رو بهش وصل کنید و خرید کنید. حواستون صرفا به اون آیپی آمریکا باشه
سؤال1: اگه یهو بدون آیپی امریکا رفتم بن میشم؟
جواب1: نه بابا. من دویست بار با آیپی آلمان و حتی ایران رفتم. صرفا ارور ممکنه بده یه وقتایی که ارور کانکشن میده و ایپی آمریکا که میزنید تازه درست میشه
سؤال2: آدرس و اینها که ازم می‌خواد و کد پستی و... رو چی بزنم؟
جواب2: خیلی راحت سرچ کنید Fake America Address و اطلاعات فیک وارد کنید اما سعی کنید همه جا همون رو وارد کنید. حتی یه جا از من کد مالیاتی و اینا خواست من الکی یه کد 8-9 رقمی زدم و گیر نداد دیگه.
سؤال3: کجاها نمیتونم پرداخت کنم؟
جواب3: ببینید یه سری سایت‌ها احراز هویت با Passport و... میخوان. مثل اکثر سایت‌هایی که کریپتو میفروشن با Debit card و اینها. فقط توی اونها من نتونستم پرداخت کنم. تا الان هرچیزی که خواستم رو گرفتم. که اکثرش هم توی همون گوگل پلی بوده</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5092" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KPyIfqa3oKPjJ5cF7v6JA_gceG0HumJlCB97B73qah_ColT1M3Qg9xALB5o_C1Z83IS1_kyJYNxKVBtgebXVY4NOnbJBfioc-SsbQhKDzmfg1OdFwKXib2ypwT7X5pr4ouA-JK6yz-FWB_8YLgJoRUpznkLmnP0tWo0e1aSo4Rn7sj1Cl6yO-KF7vK0SE0KKzO5nRguXEGz9sx6SPj9TGI8Dv2CCwWAn6xv8ZxoyLHE2HeEtF_ksPYuL49Ucxz69GRtom2CmRVgsBe9weTac4X747pwQWmfcwjLeBCpp2YDlVpd9mF4-ki19o0qIoCmno80CFmlx6Sw9hCDtih9tTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت:
https://app.mpay.cards?startapp=ref_S4FPMh
ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر:
https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت برای گوگل پی و اینها:
https://t.me/MatinSenPaii/5092
⭐️
توی این ویدئو:
1- بهتون یاد میدم که چه شکلی می‌تونید توی اکثر سرویس‌های خارجی دنیا پرداخت دلاری داشته باشید که وصله به ایمیل خودتون با اسم خودتون
2- با کریپتو حسابتون رو شارژ کنید و از هرجایی خواستید خرید کنید
3- حتی بدون شارژ، کلی آفر رایگان بگیرید
4- و یه صرافی با کارمزد پایین معرفی می‌کنم که می‌تونید به راحتی ازش خرید کنید
5- سرور رایگان V2ray آمریکا بگیرید و ازش استفاده کنید برای پرداخت‌ها
6- اشتراک Command Code رو هم با همدیگه با همین کارت میخریم توی ویدئو
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5091" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uP3KQOVJQDt_rP-hDLP5KHbrMMXkiHoiwk1PSi8uFGFnjYf6GHJueJS_hBjlO_ETBD1pDxgLB53EJExcD3eaE2vhk5l6YMrIpS-HaYtO8548VSTU2El2tpsv6sAeMqxS0n01Of5sqzZrmRCvteMeJbd7qxaXQBJDfpQ6D0dqGl1pqNcdjhdzoFSvP94iWAJErr0wmj7O9QlUR4rD97oTSXmiXBfKoIUVxO89aPaL3H7gJnp-9a9EvVR1QnMrHpbqwGSklmTvaicpmDZ2nCWFDWquQUY_ByYjWivxjRfhF8jRCPB8-TzPitYkD6Xrqpqc9SU2iBzgTS62iqUTxvHtzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی که خبر خوبیه یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5090" target="_blank">📅 22:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5089">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی
که خبر خوبیه
یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5089" target="_blank">📅 21:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5088">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">این وسط واقعا چیزی که حال یه جمعیتی رو میتونست خراب کنه خبر کنسل شدن آزمون تافل بود</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5088" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5087">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5087" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5086">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خوب شد امسال مدل‌های AI پیشرفت چشمگیری داشتن توی تولید تصویر؛ تا این بنرهای درب و داغون الکامپ یه کم زیباتر بشه</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/5086" target="_blank">📅 13:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/5085" target="_blank">📅 13:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5084">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن
#ClosedAI</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/5084" target="_blank">📅 13:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91f653dec.mp4?token=bZYzpYdwLMeRd6RMDGnCnUmI7qXShdYx8qZB89eBGbuSefvWn423n0pE91qQcH9nkLzM14kdji2oLOCX24D0LnE6bieIJ0p8fgSdPO__UqSxRJnO4P_pOVNryWayiTHl6M5xvEGcTn4NROedoJlWJjYbeVfSJ0QT9veKeacfHHupBKh-6y8nDgrWeMds-YptGtzpYY7OsKW37DxF4BoXZcGxuEgJuHVBV85W-iDTgj2J0-ZHmEYYnUjGbkrAFrV7Kvrsgndt6yXNPfTBYtLw74p9B9wRxsym6BbkFJimbG4oju-yRpKbBLl_WWJEFWV2Gs-VS205X_HkWoDGDaDK8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91f653dec.mp4?token=bZYzpYdwLMeRd6RMDGnCnUmI7qXShdYx8qZB89eBGbuSefvWn423n0pE91qQcH9nkLzM14kdji2oLOCX24D0LnE6bieIJ0p8fgSdPO__UqSxRJnO4P_pOVNryWayiTHl6M5xvEGcTn4NROedoJlWJjYbeVfSJ0QT9veKeacfHHupBKh-6y8nDgrWeMds-YptGtzpYY7OsKW37DxF4BoXZcGxuEgJuHVBV85W-iDTgj2J0-ZHmEYYnUjGbkrAFrV7Kvrsgndt6yXNPfTBYtLw74p9B9wRxsym6BbkFJimbG4oju-yRpKbBLl_WWJEFWV2Gs-VS205X_HkWoDGDaDK8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شرکت Tencent مدل Hy4-preview رو منتشر کرد
🚀
مدل: Hy4-preview — 770B پارامتر MoE با 49B فعال، کانتکست ۱ میلیون توکنی، لایسنس Apache 2.0  مشخصات کلیدی:  1-مقدار ۷۷۰B پارامتر کل ولی فقط ۴۹B برای هر توکن فعال میشه — یعنی قدرت مدل‌های فلگشیپ با هزینه‌ی خیلی کمتر…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/5083" target="_blank">📅 21:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/N1YHSPJyzL_ozHgq17gLD8HhWi9y-0gMfVROW9-IaVOoCJ2Sbg_lmFfd5CWK06SL9vcEWDDw5mCrUxRbpJwhXA2-98scdc6F9VRWr9vgSb3Ym7LZga9_pK5-m9WmcU1LJ1tDvVcavIkfXbzwEv9Ym1am8ZVrMvgHpoHXwapdfMqHZ0DYKN85rYcAJ7qbPMp9jCKaIwH0q7SoO0wl7Qj56Yneb7Ug432TG1CxWSG-PtYxlmd9MYdPVuQsNW009eaPqScVUWv7P1D0AKrYyeA4CASDVhbf_QNjKkLlBMt_ASYMWOsYqfxh6HygAy4HHVLFXOwogn6enST3j6iWOTNJyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/XcU8ZQeaq7SVOS9nEr-nAfqWElqUzae65fCA_d4ZdEuKwTG2jPEhmDa8-Nc50NLwzm-sUJ71FpDmhtXYdwtm_EOqgF1uktkSaVqfeBv8SJTQ5-mU0a-wJF-lkrxa6947uop_AMyMPILBrC4WQz5N6rDjbrmF4ehg4P7WOGZh1n4TCUNR_ePCXQticzgBkcITFoSoW_oZaneEK_o4gcrqFHBO_fFGeQrb760XOrF3bPq6WpiFCZgnh1LBmXguZUG2IaxQo8hWnuhrwB8NccmOIKZSwZMumQrjhYepiRScpoPEZhL94FyHbUJdIOrEAA3yNI6LNeL5rZdO5NIOHr7E1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/qKIrmvj_qMm1qjaMCmJ1sT_kTl1Jv8ykoULMPS2KFL5Fmj7usYenhSQ02aupSAIigy2_fhpavbUlfAnxeUDzXbh7bxAd2j_Ur5Cl2eEg63zjEOaD1edzko1zI2Dm0dgn5ZwnGa_b7mYVEzxdjujwKHeVU_fYAVAGl2Xh18atQNdNPtcNBUta5y62TFr7IVEihhAAgNor968fuzHiHfQ62VAjbA_c1rwPW10EqJTE786K0eVu6eoOcgZgDWXlw1mS_Z_lrjw-OgIs9nzJv12Ko9IiT08PzOAyGqYoEGggyWCkvxM0eJyiBX44RtTvuPEbHuSpnA6_DHPxSvX4NXWtYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راهنمای زنجیر کردن  Psiphon Desktop
با
whiteaesther
Desktop
🔥
🔥
اول Psiphon را وصل کنید.
در تنظیمات Psiphon proxy محلی را پیدا کنید. و یکی از پورت های زیر را وارد کنید . توصیه میشود از ساکس استفاده کنید
SOCKS5:1080
HTTP:8080
WhiteAesther را باز کنید.
بروید به:
Advanced
→
Routes & transports
→
Anti-blocking
در فیلد
Dial through a local proxy
یکی از این‌ها را وارد کنید:
socks5://127.0.0.1:1080
یا:
http://127.0.0.1:8080
بعد
Save profile
را بزنید.
حالا Connect کنید. مسیر  می‌شود:
App traffic -> WhiteAesther local SOCKS -> Aether/WARP -> Psiphon local upstream -> Internet
اگر میخواهید که whiteaesther سیستم شما را تانل کند روی Full tunnel و اگر نه از پراکسی whiteaesther برای نرم افزارهای خاص خودتون استفاده کنید
نکته : قابلیت exit chain را توی تنظیمات خاموش کنید
⚠️
⚠️
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5080" target="_blank">📅 19:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با npm i -g cline خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5079" target="_blank">📅 15:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sIH7g2SiNe77rCNTckzViYAilf8d8Z5cz9JWRDrPbWDh4NloICCEdg_6LoDjTz8DtJM2YdGMaQJZ8nBc4atMKlTNZV2BUSpzgcf2U7mrVLZ8zHLY7K6y7r3GBJ-MQsFynpFdWPwtkbZWADq0_Mam2IkEYITSbX2TlWFUAiSIzuPg_YGAgh_Ql7LHiKNFTpQ9SNEc5_h_LEeKbZGXk_Wn5aI3Epu8zkh9i6oZviSCBkmWZnDLGkUTIZ_TIeEhGOGqUW9r7-4yU8BKueCcpn-huH3ZXDrs9GHu7mrvY5ARLfGuN3tF-RKzajlkudSb2yZ7-AwNikS_pXNRFDSLexv12Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه‌ای که GLM 5.3 Flash برد برای تمیز کردن گندکاری‌های اون دوتا، مقابل خود هزینه‌های GLM 5.3 که تقریبا 20 دلار شده بود</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5078" target="_blank">📅 15:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">این سیستم Re-Stream همراه با بکاپ استریم رو ابتدا با GPT 5.6 Sol و GLM 5.3 در تلاش بودم که بنویسم
اما چون نسبتا پیچیده بود و تانل هم داشت و سر اینترنت ایران یهو پکت‌ها غیب می‌شدن،
می‌خواستم Claude Opus 5 رو بندازم به جونش
تا اینکه Ox Alpha اومد
دادم و کلی از جاهاش رو کامل کرد، جوری که واقعا Glm و Gpt نتونسته بودن انجامش بدن
و در نهایت هم خودش، اما نسخه ریویل شده‌اش(GLM 5.3 Flash) اومد و کاملش کرد و فرغونی که از Gpt و Glm 5.3 تحویل گرفته بود رو تبدیل کرد به بوگاتی عملا</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5077" target="_blank">📅 15:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k9aN5JzuTfOVLiE6h-6Sbw4uhPgy4xgTE2EHUp8lSwypYMVQdMs_IwOfoQD-V3YRjScMhQ_zQf6S-Ng_oKE1_7Liyax-mgZwLHFi8x6GU-AUEYmfIvwYmQjJssm6ssS6WB8gH-8gclQNBd9RCEDfAj1F1X8ExdohtZ0HxLsUmvm8mCIKI6mFQT54oBrvd94eCSKg9Q2Uwar6Mjv4Ig3lBBPTeDbdcdSfoi3ibE7vDeEosHWl4HGdQLzKI3W9ztgZGhN33lBpeaIJ7SBDLLpJOS63-_n5euA8CBji9VubqOiDLrEmOWNs1remugxl2ACgUOPM02tLLNVsDb9FkypFDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم. دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه  و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5076" target="_blank">📅 15:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FZgv2WsH5xhBfYf8VqpPzvCbSw5K1PJ_Q3XjoO90s7jNuBGa0yMcCWWRopEFaWpZfCUFYM0m-F_wljl2xDdRF1jm8qpfdFH_ZQqgQv5SLszn0KvNKT28QlmMVamo5aikJDOvhuUYjiuOOdvhgdKRGrGPYGax8-ArrQHzoCnfRLMhskIUBN0IXomnSqJAre2eF0i62oxdTxARt_lZCODLziLr8mysbv2cmt5YXZKIyd-aIx2Ok5a2YSes1RDjR8uJlIBW8neypqQRlWRWxYrWBV7OblhynrDzjlWEDpnu0z6xDSOUMvol9k_wfLIowS3tZSvt1oAhl3MNCsefcTyHMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم.
دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه
و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5075" target="_blank">📅 14:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AyXidjXDIfAyuHpr6WNotzVpoRAFB9ZOYMVlB4zLkNmP_O53kixJAVEbc7n-1qLsZeQp_HUYKtwZksnG03JEvAevqNyLnLrqau7-D6-n8fh3d8X-YIPvlNtCL47EiBz3VuZNTE2Tx8ELLkWyCLjI8YkCO4-j8CmLWtXW-8kcPewrp1tmvxwzDVYnPMHFeirkck5mv8ndjyuHKdT0DN0TtIg2YtSLzlXEQLSy2R3OsJnws_TTSEBM23Xa5vZSf_O6X-jtJgPe8yfyvDpbA0Ae_KoYrnVNH3CwLBcWOoTe6OveAEYYPiEsa9QNc5ikC6jy-a3wbSTlMehmu-P0jYy1vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Tencent مدل Hy4-preview رو منتشر کرد
🚀
مدل: Hy4-preview — 770B پارامتر MoE با 49B فعال، کانتکست ۱ میلیون توکنی، لایسنس Apache 2.0
مشخصات کلیدی:
1-مقدار
۷۷۰B پارامتر کل
ولی فقط
۴۹B
برای هر توکن فعال میشه — یعنی قدرت مدل‌های فلگشیپ با هزینه‌ی خیلی کمتر
2- روی بنچمارک
DeepSWE
از ۲۸ (Hy3) رفته روی
۶۴.۳
— تقریباً دو برابر
3- بنچمارک
Terminal-Bench 2.1
: نمره
۸۵.۴
— هم‌تراز GLM-5.3 و Claude Opus
4- بنچمارک
Code Arena WebDev
: رتبه
#5
با ۱۶۳۳ امتیاز — بین مدل‌های متن‌باز
#3
5- ارزیابی داخلی با
۱۶۳ متخصص
: Hy4 با
۲.۹۹/۴
بالاتر از Kimi K3 و GLM-5.3
قیمت API (خیلی رقابتی):
- Input:
$0.83
به ازای هر ۱ میلیون توکن
- Output:
$2.50
- Cached input:
$0.04
اما هنوز، رقابت رو به GLM 5.3 Flash باخته به نظرم</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5074" target="_blank">📅 13:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MfEC87m3JWKUXhiLen4bg7vzs3qL2s92bnZX4kskWf6nCEUwezYsRDg-s9Ez3Mb003fDyJvIpGIRmbuklk0ruX5h1b7p2ZzQabPXKWwXoRkdfzGrbuQbWGFUwzWJolnkp7QPeXHu8O7qLoOdCl5fqaSr7rej2TIuVOtvtbPjEMVqj8Zj-ytRPXED2vQbAGSbN-E6lCcIWGRJVHmqsbKmu0KVu1wkj0jxm1YmjspVlQ3CmdVv1DlQyGk73yLahsHqvFxJ0XAD2MBTMmq0OBFgmmzHlgqXFr5xqroIcyIATKCAeDrHg1sXduJ5Jg82KWlIjNTgWKeE0-SyqnzlUcJ3yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5073" target="_blank">📅 13:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dRfrUoLC-uZV1qRpvi3YvnjjAw2NFi-0ZcVO0y16ucFlyvd3j_TcFem50T3ncssuHebV_gH-A-0LchP_fnonoK36ZaN6pa9Zxu-87YCruhyndTh2aWO64o_sH0XkwftYyTFEZ6NhMIv8iohXBad8dXPQBOAOcjnMeSdd_o2UvVxoLPd7CmimKX9XgjEHvUCN-idIAFeCZzIvBdw_zWyM65zZ3lWW3gnaDCdpjTBK4O32JmNKcOQRvW61ZwNahqRO6IjI59PIpK5b_yiH35QJSmbACr1xdkD9OrfmoYEWAD-dGFEPbkEtG2cKZvtiX7z8o4DO52OfCP1r-lD870_M0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل ۱۲۵ میلیاردی Qwen 3.8 Flash Next در بنچمارک Agentic Index با ثبت امتیاز ۵۶، توانست Kimi K3 Max را پشت سر بگذارد و با یک قدم فاصله درست پشت سر Claude Fable 5 قرار بگیرد؛ اما نکته شگفت‌انگیز عملکرد آن نیست، نحوه اجرای آن است:
• سرعت: ۲۱ توکن بر ثانیه
• پنجره زمینه: ۲۵۰ هزار توکن
• سخت‌افزار: فقط یک کارت گرافیک RTX 4090 و ۱۰۰ گیگابایت رم اقتصادی DDR4
مدلی با این ابعاد تا همین دیروز به کلاسترهای گران‌قیمت نیاز داشت، اما امروز به‌صورت کاملاً محلی روی یک سیستم دسکتاپ اجرا می‌شود. مرز بین مدل‌های ابری و اجرای لوکال عملاً از بین رفت.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5072" target="_blank">📅 12:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=QXwdr1ZDuuobmqcDM3Cu8waiGqZGihMQ_gq9_j3HUCvpzUKzhoxYQFdUD2WKqxbS4uYPqDKM2g11VTB8sj6qOnKPkY85OSQ8NtvAEP2lAq5QItzdjh9mmsjwcELDe3BqkP7TpVPBtXuk_ysJYSEvAOx0caDTux8u2XnbUnQFsCOG9UCQsnjX_mY1pC4_cO2kFK4ICbRMV_3OBS7fZOA-E3-t6458kDmBLdCsk6Pm10myL-Fa5JXlge6mq5ilBho5nlpj4V7twDSxwsej2ko-nGZHcqlbxfbr6WNYdvl6fWOorOFFjEMFIF_kdZFQJlHuB4fp58S3tyvMa5hUQrnq5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=QXwdr1ZDuuobmqcDM3Cu8waiGqZGihMQ_gq9_j3HUCvpzUKzhoxYQFdUD2WKqxbS4uYPqDKM2g11VTB8sj6qOnKPkY85OSQ8NtvAEP2lAq5QItzdjh9mmsjwcELDe3BqkP7TpVPBtXuk_ysJYSEvAOx0caDTux8u2XnbUnQFsCOG9UCQsnjX_mY1pC4_cO2kFK4ICbRMV_3OBS7fZOA-E3-t6458kDmBLdCsk6Pm10myL-Fa5JXlge6mq5ilBho5nlpj4V7twDSxwsej2ko-nGZHcqlbxfbr6WNYdvl6fWOorOFFjEMFIF_kdZFQJlHuB4fp58S3tyvMa5hUQrnq5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این لودینگ ها هم جدیدن و خلاقانه خوبیش اینه که SVG هستن و توی سایت و اپلیکیشن و هرجایی می‌تونید ازش استفاده کنید:
circleloaders.dominikakissi.com
@Linuxor</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5071" target="_blank">📅 18:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AhNGaRuPbCp9wncEHhFxyz2nGlqcsYE68LE2Gs-OPkFwPxNwNm0Rck1I08LlIPHNhvAeZ61ciHe59JQYJS2YSVNObCkn7asoiCB85-7v5UfmTA4eKF5cgB6ss0oXZKcEXrZQbRnxUgXge4IpnX10GR7SNytbMXGtjVlMQ86PLqG7i72weVH6pw_3iRY54JjNXfB_UpXpuOPj9XksoOqsbXsstxp4uSZjufRj6HcaP5XQNefCQ1XOowR0JM-xlw87lPzf0rt1rAQsmZhrRu4ILxkVIbS4Q6YAnbRuvgBNWIkcBTHF3anVcb4Fhd1vAvh6tRRf2Kddc3VEaOVjjS32_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچقدر از هوشمندیش هم بگم کم گفتم</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5070" target="_blank">📅 13:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S_UhW7XksWlZWAdkFFag3XcoeSrBbhBuXA1SfRymaigb2uR7W6LgkYm02dwxBtxC4T6GehUV0AYSNcUqEwWkszKxOQ97Mu1hBnMexTkr9_9H0rEhJp3hBMXRpNPeQ0FsOSZQhCE6Esh4k7piAR0tRVltJuefSXkRRSl0vNKlHSITVRcOvJeWnUrbVy431fTL10la4cXJcJLsAPviWCjVFV6C5lFxo03gHn3rDgv69FXe_2_bnomX6UrneU5Zx5mlaEiIr-CcZY-k8TgGMxExSPy7jZBIZX55rnBm3FStEmEX-4HhJ7d8y19KkgvCd8eFu_T7Ga-GB6_oEZazvw8wDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ Input Cache اش خارق‌العادست
روی خود هارنس OpenCode</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5069" target="_blank">📅 13:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B5ziwgWmxlL3SUId3eNLGAQSWe9-KcupVc_bBweDKQFeQRV_V-xowTrqwn_TbQWrdMmeRTVrMQ3-8GkFChC4RgyRrT1PvsnXZY-u3UOAMglS4PZigiW9zTLthvKAHXD10vkUucUw8_gU0lucyE6sdS5BvTHNGUn77S4S1kYqm1K6OfnRiPP5h_AOisSsAcmVIbHn1h2NiR7K0o1uc4Hj05nGyc99Oa4NL6mzZ1Hlo-LouVYzVmrT0Q30TO08y4uJwKIrrq58lEdBBOrQOs9cyyrt8syDWXpr6lv4MPCiluRcCvohVRHcJGyFVIy7v3y65sAve3XL7qwt62ufciRbXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصرفش خییییییییییییلی نسبت به GLM 5.3 اوکی تره
و راجب هوشمند بودنش هم که دیگه یه ویدئو کامل دادم نیازی نیست بیشتر صحبت کنم. باز ما میگیم درود بر مدل‌های چینی به یه سریا بر میخوره</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5068" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5067">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gjUsnCUZqY1Lux_GFUswJ-0YnLRDXmWxZ2XO-zMjFeiBtJrCuA4VjZFaOtMVUf0LcDmtmDRuShzVp_37DLo22sjQy3i3ngGT5W-7Kb0ZgZ3NLNnSnIl6F8NB8dW9WQSSaO48OFKvNNAAR5CDvhj2zghLeiIjGW5etD_n_iIXCq_BXhrC6tGcxLfwl7EYIZ7iXADa83nOM2umf8Ao1sagCZgcGV0c8tQ46AZPg_nI8bsRo4Cw45OvUg8BNlvnev4NBzTHk3qJOiZDguTJm_xTqBsO8iC6G3YXhwDbnP9mMlAknFskDL9aICCqAMj9jVl5XYBb8K6imob4-tD8w_Z2PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5067" target="_blank">📅 13:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5066">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5066" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5065" target="_blank">📅 12:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y52cXTrDAtk2bSGcu6pbdtxwAcjpTyrmJdnHdy0m24gSfkPsRXOUaVOwGQ0mdciZqk9gjW6g_VPHqVjHraB2GomgN_S3MxUMsAovWBLEiTPamO58DRzX-fHJrf9O9esPKyvsm27-3JOrky10rf95H49gXb1rtVW1jgnNhkTuinIgJB8vLlH1hSEubEmjNoeA_dp7nHUXZM7Z8L19sKZ47xV0XAB-bBW5f-YEarJxcjiJ0bLMw1iMpZ4j4zvm8Ks1vEF8H7h_kJQ6GRsIBZesScafwqZoHZVGtscIJWdN6XTYu-LkEWHk18Zfrsv3phOb7jRSsi4lZpvOkpPkRl2u6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با
npm i -g cline
خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5064" target="_blank">📅 02:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RdSkUuHDGyoMO6aEH2xZBLRMUo55EEmsNznH-vyod-sPxmDVjFzSoxlY4NaxufCp8CRm8BONJHkAoeaoy89s57j_knIz4wJ0uJQSknUex_6hoJYIxD0qy8x5JKaX42Dd2BUOEG5j-zEoY6Ce3mKpSlaloS8GYBXU2mZSXYQvAm7tSiF9XM8_V9iPEpLNcMf8ZLlrtZOv5ovjFSD1YGd2cD6qOVPt-bBLGogP7OChTorddMpsuYu3cGKHruG2khHD1mjIed6jjAQNuoJgSGfGmDnVerCjQnf9sUtbKRA3LYwKcLfm19kiitKXI9RQxZXa82qAVTcz7OvOhCm75Y7wDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5063" target="_blank">📅 21:16 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
