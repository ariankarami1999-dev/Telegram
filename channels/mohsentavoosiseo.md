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
<img src="https://cdn4.telesco.pe/file/azYLxRNBuiXCB3MRi8FEYc8l0vlhwZJ_wKxbgFiZPnsC4dWENsUWSdQ5ZoZCkQqEEfNESqqzvBtnDetA8a0giW4o1uonsj5DLuIr37KP3vbSSRULN1vv6V7XZfcOkhozbNC8XKpS3d-ArWBCIba5QXSBP3CRWR2Iepj_q3G6FLK97opirDO3KnUPjJw4jT2vKjTkXYBerYuf8ygrfoMMOjUJz10qsbbl_1onEDJ6oFEIaBKAA0uBaGSU4Is7ldQ-97iz15UARuLpj437xXMhD0Ad4QowVaUZi-BOYbp0jofs963IXBgJp-NpKPt9i6_Acu29uR6MYa2T2Aq2qOdd0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 آموزش سئو محسن طاوسی</h1>
<p>@mohsentavoosiseo • 👥 7.6K عضو</p>
<a href="https://t.me/mohsentavoosiseo" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 من تالیف و تولید می کنم✅. نه ترجمه.نه اخبار. نه گرداوریدوره:mohsentavoosi.com/course/seo/خرید دوره:@mohsentavoosisupportyoutube.com/c/MohsenTavoosiInstagram.com/mohsentavoosi.seolinkedin.com/in/mohsentavoosi</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 15:33:43</div>
<hr>

<div class="tg-post" id="msg-813">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مباحث امنیتی(امنیت ایالات متحده)</div>
<div class="tg-footer">👁️ 416 · <a href="https://t.me/mohsentavoosiseo/813" target="_blank">📅 14:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">صحبت خارج از موضوع کلاد:
چون خیلی شکایت میشنوم میگم. وگرنه جالب نیست بگم. چون اون ها هم بهرحال از دوستان من هستند. میگم که شاید تغییری ایجاد شه.
از ل............ت برای احترام اول به اعصاب بعد به پولتون توصیه نمیکنم خریدی انجام بدید. آدم های خوبی هستند. اما چون همه چیز دست مدیران فنی هست و ذهنشون همه چیو فنی میبینه و با ذهن تکنیکال غیر تجاری میخوان مشکلات رو حل کنن و تصمیم گیری کنند،
در مدیریت فرایند سفارش ها به مشکلات زیادی میخورن و بعد میان موردی دونه دونه حل میکنن.
افتادند توی لوپ و حلقه بهینه سازی(بازم فنی) که دیگه یک بار برای همیشه درستش کنند. چند ساله. اما گاهی باید ورود کرد دستی کار رو جمع کرد. باید هزینه کرد. بیخیال سود بیشتر شد و به روش غیر فنی، فعلا شرایط رو درست کرد.
بماند که در تشخیص فنی اینکه مشکل کجاست هم اشتباه میکنند. چون فقط از یک زاویه دارن به مشکل نگاه می کنند.
همون چیزی که همیشه میگم مغز صرفا دولوپری و غیر تجاری،
1- یا ایده هاش شکست میخوره،
2- یا نمیتونه بفروشه اصلا و جمع میکنه
3- یا نارضایتی از محصول یا خدماتش ایجاد میشه که نمیتونه حلش کنه(این ها سومی هستند و حداقل تو یک و دو گیر نکردند).
این نکته برای خود اون کسب و کار و کسانی که دریچه دریافتشون بازه، میلیون دلاری ارزش داره. باید میلیارد ها تومن یا صد ها هزار دلار از دست بدن تا این بازخورد رو از زبون یه مشاور که ایراد کسب و کارشون رو میگه بشنون.</div>
<div class="tg-footer">👁️ 535 · <a href="https://t.me/mohsentavoosiseo/812" target="_blank">📅 14:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-811">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⭕️
❗️
🟢
درباره معلق شدن اکانت های کلاد
موجی که راه افتاد ظاهرا همه کسانی که از سایت ا.........ت خریده بودند suspend شدند. اما از گزارش هایی از ساسپند شدن غیر از ا.......ت هم هست.
برای ما نشده. لاگین از ایران هم داریم با وی پی ان. و لاگین های ما از چند کشور هست. ولی هربار کشورش عوض نمیشه.
پرداخت هم از یکی از کشور های ثابت اتحادیه اروپاست با کارت شخصی. با کارت زراعت بانک، ایش بانک و وکیف بانک ترکیه و ورود از ترکیه هم مشکلی نداشته.
مکالمه ما هم فارسی هست اکثرا. ربطی به زبان شما نداره. حساسیت اصلیش روی پرداخت کننده هست و هویت پرداخت کننده.
چون بحث احراز هویت سنی و مباحث امنیتی(امنیت ایالات متحده) توش لحاظ میشه.
اکثر ادم ها هم استفاده های سنگین ندارند. حتی از skill و connector ها که پایه ترین و ابتدایی ترین قابلیت کلاد هست استفاده نمیکنن. فعالیتی که توسعه کد سنگین تو گیت هاب به صورت انلاین و مواردی که میتونه منجر به استفاده عمومی بشه رو بهش حساس تر هست.
اما خودشون میدونن دقیقا رو چی حساسن. تو متن خودش هم نوشته موارد خاص و این خاص رو تعریف نکرده.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 563 · <a href="https://t.me/mohsentavoosiseo/811" target="_blank">📅 14:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-810">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کسانی که گزینه "خوشحال" رو زدند که از جایی با قیمت خیلی کمتر به صورت اختصاصی میخرند،
ممنون میشم دایرکت پیام بدید(آیکون یا کلید message همین کانال) و من رو هم از این نون سهیم کنید
😒
. زشته کارتون که مخفی نگهش داشتید
😏</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/mohsentavoosiseo/810" target="_blank">📅 15:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-809">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-poll">
<h4>📊 اگر من ابزار های اختصاصی(نه اشتراکی) هوش مصنوعی رو به قیمت دلاری اصلش ارائه بدم با حداکثر 10 درصد بالاتر، هر ماه حتما تهیه می کنید از من؟</h4>
<ul>
<li>✓ صد در صد بله</li>
<li>✓ 10 درصد بالاتر نه. معادل دقیق قیمت دلاریش باشه صد در صد</li>
<li>✓ نه. فقط اگه یک کم ارزون تر از معادل دلاریش در بیاد میگیرم. وگرنه نمی گیرم.</li>
<li>✓ من از بعضی AI ها رو از جایی میخرم که خیلی کمتر از قیمت دلاریش در میاد. اختصاصی هم هست و خوشحالم.</li>
</ul>
</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/mohsentavoosiseo/809" target="_blank">📅 15:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-808">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">درباره این ویس و اون سوال، اون سه راهکار (ادز و کانال های غیر کیوردی، کیورد ریسرچ عمیق تر و out of the box و تغییر استراتژی محتوایی)، اگه همچنان شکست بخوره، جواب نده یا نصرفه یا توان هزینه کردن نباشه،  دیگه باید بوسید گذاشت کنار دیگه. سود ما تسلیم شدن به موقع…</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/mohsentavoosiseo/808" target="_blank">📅 00:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-807">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/mohsentavoosiseo/807" target="_blank">📅 00:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-805">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/mohsentavoosiseo/805" target="_blank">📅 20:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-804">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">https://www.instagram.com/reel/DaNzmW8MtPF/</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/mohsentavoosiseo/804" target="_blank">📅 20:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-803">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">https://www.instagram.com/reel/DaNzmW8MtPF/</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/mohsentavoosiseo/803" target="_blank">📅 20:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-802">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">من احساس میکنم آموزشی که جناب طاووسی میدن برای این مدل بیزینس ها مثل سایت ما یه آپدیت نیاز داره که نیاز هست برای سایتایی که کم محصول هستن و محصولاتشون قابل تفکیک و توسعه به صفحات مختلف نیست چیکار باید بکنن؟</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/mohsentavoosiseo/802" target="_blank">📅 19:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-801">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سوال یکی از دانشجویان دوره از پشتیبان دوره:  من یک سایت در زمینه فروش پلاگین های وردپرسی دارم. کلا نزدیک 13-14 تا محصول بیشتر روی سایتم نیست مشکل من اینه که توی مثال ما یک لندینگ بیشتر نمیتونیم بسازیم اونم برای خود محصوله.سایر صفحات میشه ویژگی های محصولمون...که…</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/mohsentavoosiseo/801" target="_blank">📅 19:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-800">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سوال یکی از دانشجویان دوره از پشتیبان دوره:
من یک سایت در زمینه فروش پلاگین های وردپرسی دارم. کلا نزدیک 13-14 تا محصول بیشتر روی سایتم نیست
مشکل من اینه که توی مثال ما یک لندینگ بیشتر نمیتونیم بسازیم اونم برای خود محصوله.سایر صفحات میشه ویژگی های محصولمون...که نمیتونیم اینجا صفحه لیستینگ بسازیم و مجبوریم بلاگ ایجاد کنیم.
اگه بخوام مثال بزنم مثلا پلاگین woocommerce gift داریم که براش یه لندینگ ساختیم و یکی از ویژگی های این پلاگین BOGO deal هستش..خب ما اینجا نمیتونیم یه صفحه لیستینگ بسازیم که در مورد BOGO deal باشه و فقط یه پلاگین توش باشه..نمیتونیمم یه لندینگ جدا برای BOGO بزنیم که اونجا پلاگین رو معرفی کنیم. مجبوریم یه بلاگ بزنیم که در مورد BOGO حرف بزنیم و نتیجه این میشه که کسی که توی حوزه ما یه پلاگین مخصوص فقط برای BOGO deal زده باشه میاد بالاتر از پلاگین ما قرار میگیره و ما هم توی برنامه مون نیست که بیایم این ویژگی رو از دل پلاگینمون در بیاریم و یه پلاگین جداش بکنیم. در نتیجه توی نتایج در صفحات عقب تر دیده میشیم.
یا مثال دیگه یکی از ویژگی های پلاگین ما Buy X Get Y هست که این کلمه خیلی سرچ میشه. ما نمیتونیم اینو جدا کنیم از پلاگین و یه پلاگین یا محصول جدا بدیم ولی رقبا اومدن یه پلاگین نوشتن فقط buy x get y انجام میده و اون الان بالاتر از ماست توی نتایج در حالی که این یه ویژگی خیلی کوچیک از پلاگین بزرگ ماست.
وقتی هم بلاگ مینویسیم برای این ویژگی توی بلاگ مجبوریم اینفورمیشنال صحبت کنیم و از روش های مختلف غیر از پلاگین خودمون هم حرف بزنیم که بتونیم با رقبایی که فقط بلاگ وردپرسی هستن رقابت کنیم. در نتیجه نرخ تبدیلمون خیلی کم میشه.
من احساس میکنم آموزشی که جناب طاووسی میدن برای این مدل بیزینس ها مثل سایت ما یه آپدیت نیاز داره که نیاز هست برای سایتایی که کم محصول هستن و محصولاتشون قابل تفکیک و توسعه به صفحات مختلف نیست چیکار باید بکنن؟</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/mohsentavoosiseo/800" target="_blank">📅 19:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-799">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سوال زیر رو 99 درصد آدم ها متوجه نمیشن. ولی تو جواب، ساده توضیح دادم سوال، چی هست.
مخاطبشم اکثر آدم ها نیستند. اما نکته های توی جواب، از نظر باز شدن ذهن، به درد همه میخوره.</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/mohsentavoosiseo/799" target="_blank">📅 19:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-798">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انقدر که رو وایب کدینگ مانور میدن تعجب میکنم. البته درک میکنم. بازارگرمی خوبیه برای اینکه کسی که خبر نداره بگه wowwww برم ببینم چیه.
vibe coding - وایب کدینگ
یعنی به هوش مصنوعی بگی چی میخواد برات کدش رو بزنه. همین! یعنی هوش مصنوعی به عنوان نوکر کد زن تو باشه. یعنی nokar coding یا vibe nokaring
😏
حالا میتونی روی پرامپت خوب زدن مانور بدی که اون دیگه ربطی به وایب کدینگ نداره. برای کار با هر هوش مصنوعی هست به صورت کلی.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/mohsentavoosiseo/798" target="_blank">📅 17:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-797">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اگر فروش اکانت کلاد، جمینای و سایر هوش مصنوعی ها رو دارید، و همینطور ابزار های SEO،  من به عنوان Reseller شما و شما هم تامین کننده اصلی، میتونیم همکاری داشته باشیم.
فقط با کد تخفیف و این چیزا کار در نمیاد.
ممکنه کد تخفیف بزنن سری دوم نزنن. و ممکنه یک ابزار بخره کاربر از طریق من، ولی بعد سری دوم بیاد ابزار دیگه ای با همون اکانت بخره. لینک affiliate خالی هم فایده نداره. مگر اینکه کوکی خوبی براش تعریف بشه.
اگر یک ساز و کار عادلانه و قابل track خوبی وجود داشته باشه، میشه همکاری کرد. تقاضای زیادی سمت من میاد. به خاطر سود بسیار کم و تامین پردردسرش، من نمیخوام خودم ورود کنم به کسب و کارش کلا که کلا خودم بزنم. در حد ریسلر فقط میخوام درگیر شم.
کلا به خاطر track نامناسب یا عدم اعتماد کافی یا ثبات نداشتن آدم ها یا کسب و کار هاشون، تا حالا همکاری جدی reseller نداشتم.
اگر فکر می کنید میتونیم همکاری داشته باشیم به دایرکت همین کانال، پیام بدید.</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/mohsentavoosiseo/797" target="_blank">📅 17:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-796">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سوال:
من 20 میلیون تومن پول توی بورس دارم. بفروشم سایت بزنم؟ سئو هم بلدم.
پاسخ:
سئو با 20 تومن در نمیاد. میشه 120 دلار! میشه 5200 لیر.
شما هیچ کسب و کاری رو با 100 دلار نمی تونید به سود برسونید. پول میخواد. با هر استراتژی ای حساب کنید(کیورد های کم رقابت)، باز هم با صد دلار به فکر راه اندازی کسب و کار نباشید.
در بدترین حالت، کم رقابت ترین حالت، حوزه خیلی خیلی خاص یا محدود شده به چند مورد خاص که سوداوری خوبی داره(بعد از تحقیق مفصل کلمات کلیدی)، مثلا در حد کیودری مثل "خرید فلان ماده اولیه" که اون مواد اولیه برای کارخونه های خاصه و شما هم مثلا آشناش رو برای تامینش دارید، رقابتش صفر یا نزدیک به صفره و خلوته ولی سرچ کننده ها مشتری هستند و پرداخت خوب دارند و نرخ تبدیلش بالاسات،(چون مثلا کم هست کلا)
در این صورت، با ماهی 200 دلار(نه یک بار 200 دلار)، میشه امیدوار بود بعد از 6 ماه شروع کنه به درامدزایی. در خیلی شرایط استثنایی، 3 ماه. شایدم اگه کیورد خاص پرسودی باشه مثل مثالی که زدم و هیچ کس هم کار نمیکنه و جنسشم جوریه که شما میتونید تامین کنید راحت، شاید خیلی استثنایی بشه با همون یک بار 200 دلار. بشرطی که از قبل بدونید. نه اینکه تازه بخواید شروع کنید تحقیق کردن.
روش دیگه ای بلدید؟ میگی نه! رفیق من فلان کرد و فلان؟ حله. من بلد نیستم. از رفیقتون بپرسید. نه بلدم نه آموزشش رو میدم.
شما اکانت 20 دلاری کلاد نیاز دارید حداقل. دستی هم انجام بدید موقع Off-Page نیاز دارید به هزینه کردن. خیلی چیز ها هم هزینه پنهان هست که به چشم نمیاد. مثل زمانتون که داره میره و از کار و زندگی مفتید. ماهی 40 میلیون تومن از دست میدید که سال دیگه تازه شروع کنه به درامدزایی.
سئو پول میخواد. رایگان نیست. ابزار هاش هم رایگان گیر بیارید، موقع Off-Page، پول میخواد.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/mohsentavoosiseo/796" target="_blank">📅 14:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-795">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مشکل ما با کسانی هست که سوال نمی پرسند از پشتیبانی و خجالت می کشند!
آپدیت مفصل سئو بین المللی بیاد که خیلی فشردست اون موقع هم میخواید سوال نکنید؟(دانشجویان دوره).
کی دیدید التماس کنه بیا از پشتیبانی استفاده کن! 60 هزار تا سوال بپرس! هرروز! هر ساعت! ما طبق زمان بندی خودمون جواب میدیم. ولی شما که میتونید بپرسید!
آگر تو دوره باشه و مشخصه که ندیدید، ارجاع میدیم به ویدیو دوره، بهر حال یه کمکی می کنیم در حد تعهدی که مکتوب دادیم(نوشته شده موقع خرید). ولی از سمت شما واقعا نباید مراعات و شرم وجود داشته باشه!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/mohsentavoosiseo/795" target="_blank">📅 12:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-794">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">چالش رایج دیگه ما!
آدم ها خجالت میشکن. فکر میکنن کنتور میندازه یا سهمیه ایه سوال پرسیدن! (پشتیبانی دوره رو میگم. نه دایرکت خودم).
مهارت سوال کردن، مهارت طرح سوال وقتی که جواب، دقیق به جواب ما نیست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/mohsentavoosiseo/794" target="_blank">📅 12:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-793">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سوال از پشتیبان دوره:(سوالات خیلی سطح حرفه ای هم داریم. ولی هدفم پاسخ دادن نیست الان).  مابقی دستورهایی که میخوام در فایل روبوت بزارم مثل قبل هست؟ مثلا disallow کردن سرچ ها صفحه چک اوت و ...   فقط ادرس لاگین رو دیگه قرار ندم  درسته؟</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/mohsentavoosiseo/793" target="_blank">📅 12:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-792">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سوال از پشتیبان دوره:(سوالات خیلی سطح حرفه ای هم داریم. ولی هدفم پاسخ دادن نیست الان).
مابقی دستورهایی که میخوام در فایل روبوت بزارم مثل قبل هست؟ مثلا disallow کردن سرچ ها صفحه چک اوت و ...
فقط ادرس لاگین رو دیگه قرار ندم
درسته؟</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/mohsentavoosiseo/792" target="_blank">📅 12:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-791">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خرید قسطی هرچیزی، intent کاملا متفاوتی از خرید اون چیز داره(بدون کلمه قسطی). اگر سرچ والیوم داره(جستجو میشه قسطیش) صفحه اش باید جدا باشه برای شانس بهتر رتبه گرفتن.
اگر صفحه یکی باشه و تو عنوان بنویسید نقد و اقساط، حوزه رقابتیش بزرگتر میشه. ولی این هم میشه. ولی روی کیورد خرید قسطی اون چیز، سخت تر رتبه می گیره.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/mohsentavoosiseo/791" target="_blank">📅 00:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-790">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سوال دانشجو:  و اینکه یکسری تعاریف هست برای سئو هست. این ها چی هستند؟  Topical Authority Internal Linking Strateg Site Architecture  Content Hub / Pillar & Cluster Information Architecture + Semantic SEO Link Equity Flow + Topic Authority Reinforcement</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/mohsentavoosiseo/790" target="_blank">📅 00:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-789">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سوال دانشجو:  و اینکه یکسری تعاریف هست برای سئو هست. این ها چی هستند؟  Topical Authority Internal Linking Strateg Site Architecture  Content Hub / Pillar & Cluster Information Architecture + Semantic SEO Link Equity Flow + Topic Authority Reinforcement</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/mohsentavoosiseo/789" target="_blank">📅 00:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-788">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سوال دانشجو:
و اینکه یکسری تعاریف هست برای سئو هست. این ها چی هستند؟
Topical Authority
Internal Linking Strateg
Site Architecture
Content Hub / Pillar & Cluster
Information Architecture + Semantic SEO
Link Equity Flow + Topic Authority Reinforcement</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/mohsentavoosiseo/788" target="_blank">📅 00:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-785">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کسانی که میگن چرا طرف رفت ارمنستان یا ترکیه؟ اونجا که ظرفیت نداره فضای دیجیتالشون. اونجا که اقتصادش فلانه!  باید بگم قرار نیست برن شرکت ترک یا ارمنی کار کنند. ظرفیت اونجا مهم نیست! از دیجیتال مارکتر ها بعیده این حرف!  اونجا فقط یه نقل مکان سکونت فیزیکی هست…</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/mohsentavoosiseo/785" target="_blank">📅 22:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-782">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آموزش سئو محسن طاوسی
pinned «
هرچیزی که دوست دارید یاد بگیرید یا از من یاد بگیرید، حتی خارج از سئو، توی دایرکت کانال بفرستید.  میخونم همه رو قطعا. (صرفا دریافت. بدون پاسخ و تعامل خصوصی).  قصدم از باز کردن دایرکت، صرفا دریافت نظرات شما درباره اینکه علاقه مند به یادگیری چه چیزی حتی خارج…
»</div>
<div class="tg-footer"><a href="https://t.me/mohsentavoosiseo/782" target="_blank">📅 13:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-781">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">هرچیزی که دوست دارید یاد بگیرید یا از من یاد بگیرید، حتی خارج از سئو، توی دایرکت کانال بفرستید.
میخونم همه رو قطعا.
قصدم از باز کردن دایرکت، صرفا دریافت نظرات شما درباره اینکه علاقه مند به یادگیری چه چیزی حتی خارج از سئو هستید.</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/mohsentavoosiseo/781" target="_blank">📅 13:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-780">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2T8XCp9CIiuq4rAcHDIc0MhMACHHW77C_YOA-1-3LdfhkSRs9Fi5jjHwpO9_I8pATVKioBCdhk4Ko0IIGe7iKO9MW8SeDdCCR6OwVSUsyFSXSksbvYiq9owHs_5iBUdvm0KWQdfSC47uR0MXC7NsIBTmwbfxP6G2TyQJv0pp_mLR9wQM8naL5mxH36-aUFAmJ5z9CG9ug7zyOWLK3VBWqKihblzCZSEon_7lk9lN_7l3mJ_2gLG8sUc_uYj55aFsPyTE3zMQD9nhT7cmanTEDDme3Rflw-AbWji06qcD8v4qyNpjqt4efL1rlK-doS2ZUoa7cJC4jN-Sp3Rw9LFhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسانی که نمیدونن دایرکت کجاست. پیام خصوصی ایکونش در اندروید اون پایینه. نیازی هم به ستاره و تلگرام پریمیوم نداره.
تو آیفون هم داخل خود کانال رو اسم کانال بزنید نوشته message.
تو وب و دکستاپ ندیدم هنوز خودم.
بدیهیه که تبلیغات، مال خود تلگرامه و در کنترل من نیست. خداروشکر این کانال، افرادش آی کیوشون تو این چیزا بالاست و میدونن که تبلیغات پایین کانال های تلگرام، دست اون کانال نیست.</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/mohsentavoosiseo/780" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-778">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هرچیزی که دوست دارید یاد بگیرید یا از من یاد بگیرید، حتی خارج از سئو، توی دایرکت کانال بفرستید.
میخونم همه رو قطعا. (صرفا دریافت. بدون پاسخ و تعامل خصوصی).
قصدم از باز کردن دایرکت، صرفا دریافت نظرات شما درباره اینکه علاقه مند به یادگیری چه چیزی حتی خارج از سئو هستید و شنیدن هر صحبتی.</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/mohsentavoosiseo/778" target="_blank">📅 11:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-776">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/mohsentavoosiseo/776" target="_blank">📅 17:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-775">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">توضیح در ویس پایین  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/mohsentavoosiseo/775" target="_blank">📅 17:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-774">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHJr4KeSpvFgyQu14-1_BVc2fy5x8Bfg2DhUaiQsz1H-eq4XawD9gls7-nfSToRSdl5EeVXdlUTHe_d_qGW_vpIuGXVyy6ssdpLgt0ItowoC6bdbXCMdeIg1zV312-ecYum8d6PZ3dSY25GWuHdg9rao3XqOlGQhWHItTvWIKWEqGyCySVCYxY5fvKGOQFSymeSe2sxPjmOcjlRXuX-iU-uzsjx7xgB6UlJ617FpL6gWKDoVRyQ407CjYuF1YQ--ITnmezydwDi1KA_Qcu3rYvtOSUmGvyvvAZ0h9zKOGcpow5-_rv4poHcfr-EQH2mX9OpArnE7LArW-xWw3f78vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درباره پستی که روش ریپلای زدم:   نظر یک نفر قبل از اون پست:  از این زاویه نگاه میکردم که آقا تفکر وقتی آزاد باشه کامنت هم باز میزاره که جامعه بتونه درموردش صحبت کنه  وقتی میبنده داره آزادی رو میگیره</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/mohsentavoosiseo/774" target="_blank">📅 17:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-773">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">درباره پستی که روش ریپلای زدم:   نظر یک نفر قبل از اون پست:  از این زاویه نگاه میکردم که آقا تفکر وقتی آزاد باشه کامنت هم باز میزاره که جامعه بتونه درموردش صحبت کنه  وقتی میبنده داره آزادی رو میگیره</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/mohsentavoosiseo/773" target="_blank">📅 18:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-771">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">چرا کامنت ها و ری اکشن هارو من باز نمیکنم؟ بخاطر بحث اقتصاد توجه: https://t.me/mohsentavoosiseo/364  نمیخوام ذهنم درگیر این شه که اااا پستام کم لایک خورد. کم ری اکشن مثبت داشت. ااا منفی داشت. . خیلی لایک خورد روحیه بگیرم. و وقتی کم لایک خورد ناراحت بشم. یا…</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/mohsentavoosiseo/771" target="_blank">📅 18:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-770">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/mohsentavoosiseo/770" target="_blank">📅 12:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-769">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سوال یک دنبال کننده که احتمالا شناخت قبلی هم به من نداره:  نکات سوال:  پارتی نداشتم کار خوب گیرم نیومد گفت ریاضیت قوی نیست پایتون نخون.  تحصیلات بدون فرصت خوب اشتغال.  نگرانی آینده.  هوش مصنوعی جای سئو رو میگیره؟  سئو رو برای کارمندی یاد بگیرم.  ۹ ماه کاراموزی…</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/mohsentavoosiseo/769" target="_blank">📅 15:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-768">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZD9Z7yB0PD8Uq2bIRgsOHzk806mBjSAhFTT0QZV9pGhFkbxIwrOmDvN0t1MPGBWKWtEZRty_4ma74Sz46gcOGhvpOqDap-zGOK721nN2vjJRXq-XGv7XDUpwyOEMLF78a7_1ooCurfTMXKCAuRbtF_c0Pa7FSULH9dzdeVo34KVhXgeeHzBFdvfk2htJe8zVFAFXHAS63V4ZbZUngKLglDnD_FzAbZYUn3g4KR7jdZ_ktkb-FLJa7onckNQsr7naDIdEu-I1XS1yw9hctFVpDvZG502NUlLLKUSiK8xR27z36vmk_yzVBEQqjd3UeEVdw2XS8uFJ6L9MqbQCS-CnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوال یک دنبال کننده که احتمالا شناخت قبلی هم به من نداره:
نکات سوال:
پارتی نداشتم کار خوب گیرم نیومد
گفت ریاضیت قوی نیست پایتون نخون.
تحصیلات بدون فرصت خوب اشتغال.
نگرانی آینده.
هوش مصنوعی جای سئو رو میگیره؟
سئو رو برای کارمندی یاد بگیرم.
۹ ماه کاراموزی رایگان
تو ویس بعدی فقط جواب نمیدم. تحلیل می کنم این  صحبت ها رو.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/mohsentavoosiseo/768" target="_blank">📅 14:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-767">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">چرا کامنت ها و ری اکشن هارو من باز نمیکنم؟ بخاطر بحث اقتصاد توجه: https://t.me/mohsentavoosiseo/364  نمیخوام ذهنم درگیر این شه که اااا پستام کم لایک خورد. کم ری اکشن مثبت داشت. ااا منفی داشت. . خیلی لایک خورد روحیه بگیرم. و وقتی کم لایک خورد ناراحت بشم. یا…</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/mohsentavoosiseo/767" target="_blank">📅 14:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-766">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">من دهان به دهان شنیده بودم از چند تا از دوستان که زمان مصاحبه برای مجموعه خودشون، کسانی که دوره رو دیده بودن خیلی از نظر فنی و مهارت نرم، متمایز بودند.   افتخار میکنم
❤️
❤️
اما الان دغدغم اینه که کسانی که دوره رو گرفتند، کامل ببینند. چون درصد کسانی که کامل میبینن…</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/mohsentavoosiseo/766" target="_blank">📅 14:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-765">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/mohsentavoosiseo/765" target="_blank">📅 14:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-762">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سوال دانشجو:  من ی مشتری دارم که سایت خدمات راپل و نماشویی ساختمان داره گیر داده که فقط مقاله میخواد و ماهی ۷ بیشتر نمیده و من باید بهش تضمین بدم تو قرارداد بیارم که رتبه میگیره صفحه اول. این حرفش منطقیه؟</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/mohsentavoosiseo/762" target="_blank">📅 13:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-761">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcFRgUYAo5mCU2T6-xBVx1g9LbBd-9dwdoDTp-A26JPjNCjgkL0nwxJ-IFTTaZyO2KkokNI5o2m-6YI96GK522YEToD3PeUEyo7k6yCxEcGPh6YRPblVnBKYdmJ06qhY7aQVAYxho2VPN_x-UZ6JNTLERS4MIUBkoM34_0rGBUcNXVLyZPaoA1hKMFj0-HD3oEgB319ZYpPtCzeUhiBdGNPccQSXHQBQbr-jxPKGHzDPa9ZlINC2MIEBje1o2nv9yXufCZFtT_nGPEMEaDDkCoe7BTAu7NZHm1XY9MDGOstifjiAbl158v5gqCjnyZRaJsxZAv48ZatxjTZjlAMW5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوال دانشجو:
من ی مشتری دارم که سایت خدمات راپل و نماشویی ساختمان داره
گیر داده که فقط مقاله میخواد و ماهی ۷ بیشتر نمیده
و من باید بهش تضمین بدم تو قرارداد بیارم که رتبه میگیره صفحه اول.
این حرفش منطقیه؟</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/mohsentavoosiseo/761" target="_blank">📅 13:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-760">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اگر کار دقیقا قابل برنامه ریزی میخوادی جای اشتباهی اومدید. SEO به دردتون نمیخوره</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/mohsentavoosiseo/760" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-759">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سئو برای این نیست که بهار شروع کنی تابستون بیای بالا محصولات تابستونی بفروشی یا برعکس برای زمستون و فصل.
نمیگم نمیشه. ولی نباید روش حساب کنید. اگر کار دقیقا قابل برنامه ریزی میخوادی جای اشتباهی اومدید. SEO به دردتون نمیخوره. هرچیزی هم میچینید فقط رو احتمال و تخمین با بیش از 50 درصد احتمال خطا هست.
کار با زمان بندی دقیق میخوای اورگانیک سرچ به درد نمیخوره. گوگل ادز و سایر روش های دیجیتال مارکتینگ ادز محور فقط. که میتونی در لحظه و در روز کمپین رو شروع کنی و تموم کنی.
گوگل خیلی تلاش کرد کنترل رو از ارگانیک سرچ باز ها(SEO) بگیره که گوگل ادز بیشتری بفروشه و برای گوگل ادز تقاضا بره بالا. و موفق هم شد.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/mohsentavoosiseo/759" target="_blank">📅 12:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-758">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/mohsentavoosiseo/758" target="_blank">📅 11:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-757">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سوال دانشجو:  من رو یه سایت دارم کار میکنم که تجهیزات آشپزخونه میفروشه.یه دسته بندی داره هود اخوان.و تقریبا ۵ ساله همین دسته بندی رو داره.زیر مجموعه میتونه هود مخفی،هود مورب،هود شومینه ای باشه با توضیحات و مدلاش.الان اوکیه من اضافه کنم؟یا چون همون صفحه هود…</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/mohsentavoosiseo/757" target="_blank">📅 11:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-756">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سوال دانشجو:
من رو یه سایت دارم کار میکنم که تجهیزات آشپزخونه میفروشه.یه دسته بندی داره هود اخوان.و تقریبا ۵ ساله همین دسته بندی رو داره.زیر مجموعه میتونه هود مخفی،هود مورب،هود شومینه ای باشه با توضیحات و مدلاش.الان اوکیه من اضافه کنم؟یا چون همون صفحه هود اخوان رتبه داره اینکار رو نکنم.</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/mohsentavoosiseo/756" target="_blank">📅 11:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-755">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/mohsentavoosiseo/755" target="_blank">📅 20:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-754">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سوال دانشجو:  من روی کیورد با مشتری کار میکردم و قیمت میدادم یعنی یک سری کلیدواژه میداد و میگفت اینا برای من مهمه و من کار میکردم میوردمشون صفحه اول  علاوه بر این براش مقاله هم مینوشتم و تو بقیه صفحه ها هم کار میکردم  و تضمین میدادم که میارمش صفحه اول اما…</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/mohsentavoosiseo/754" target="_blank">📅 20:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-753">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سوال دانشجو:
من روی کیورد با مشتری کار میکردم و قیمت میدادم یعنی یک سری کلیدواژه میداد و میگفت اینا برای من مهمه و من کار میکردم میوردمشون صفحه اول
علاوه بر این براش مقاله هم مینوشتم و تو بقیه صفحه ها هم کار میکردم
و تضمین میدادم که میارمش صفحه اول اما این تضمین از دید دوره درست نیست
حالا میخوام بدونم مشتری روی یک سری از کلیدواژه ها میخواد بیاد بالا (از 98 تا 1401) روش کلمه ها کار کردم و صفحه اول بوده الان افت کرده و میگه کار کنید تا بیام صفحه اول.
سوالم اینه مشتری از من در برابر پولی که میده تضمین میخواد قبلا من تضمین رنک میدادم
الان چی بهش بگم برای تضمین؟</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/mohsentavoosiseo/753" target="_blank">📅 20:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-752">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سوال یکی از دانشجویان:  هدف از صفحه دسته بندی محصول اینه که خب محصول بفروشه قسمت توضیحات هم که شاخص ها کیفیت و قیمت گفته میشه  صفحه اصلی هم که معرفی برند هست هدف از اینکه برای بعضی کلمه ها لندینگ پیج داریم چیه ؟  با کلمه هایی که براشون دسته بندی داریم هم نوع…</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/mohsentavoosiseo/752" target="_blank">📅 18:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-751">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ادامه جواب بالا
روش جادویی من تو مشاوره هام(توهم جادو)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/mohsentavoosiseo/751" target="_blank">📅 17:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-750">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/mohsentavoosiseo/750" target="_blank">📅 17:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-749">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/mohsentavoosiseo/749" target="_blank">📅 17:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-748">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سوال یکی از دانشجویان:  هدف از صفحه دسته بندی محصول اینه که خب محصول بفروشه قسمت توضیحات هم که شاخص ها کیفیت و قیمت گفته میشه  صفحه اصلی هم که معرفی برند هست هدف از اینکه برای بعضی کلمه ها لندینگ پیج داریم چیه ؟  با کلمه هایی که براشون دسته بندی داریم هم نوع…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/mohsentavoosiseo/748" target="_blank">📅 17:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-747">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سوال یکی از دانشجویان:
هدف از صفحه دسته بندی محصول اینه که خب محصول بفروشه قسمت توضیحات هم که شاخص ها کیفیت و قیمت گفته میشه
صفحه اصلی هم که معرفی برند هست
هدف از اینکه برای بعضی کلمه ها لندینگ پیج داریم چیه ؟
با کلمه هایی که براشون دسته بندی داریم هم نوع نمیشن؟
مثلا الان یه دسته بندی داریم که دسته بندی تجهیزات هتلی هست که داخلش محصولات لیست شدن
و یه لندینگ پیج تجهیزات هتلی برای تماس بگیرید و هتل های تجهیز شده و …
اینا الان هم نوع میشن؟</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/mohsentavoosiseo/747" target="_blank">📅 17:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-746">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سوال بعضی از دانشجویانی که تازه شروع کردند:  داخل این دوره ی اموزشی طریقه ی این که چجوری کلمات کلیدی که پیدا کردیم رو تو صفحات بزاریم رو اموزش میده چون من نه از رودپرس سایت یا سئو هیچ پیش زمینه ای ندارم و داخل وردپرس اگه من بخوام کلمات کلیدی رو جایی بزارم…</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/mohsentavoosiseo/746" target="_blank">📅 17:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-745">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سوال بعضی از دانشجویانی که تازه شروع کردند:
داخل این دوره ی اموزشی طریقه ی این که چجوری کلمات کلیدی که پیدا کردیم رو تو صفحات بزاریم رو اموزش میده چون من نه از رودپرس سایت یا سئو هیچ پیش زمینه ای ندارم و داخل وردپرس اگه من بخوام کلمات کلیدی رو جایی بزارم باید کجا بزارم ؟</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/mohsentavoosiseo/745" target="_blank">📅 17:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-744">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ba1EcUc3iZOX5_DGwa01Xry1PVK3bIQf4E0BQyFyYpoyfFjtCAJCmemXovI_U6KPmnLxQXXrpGHhFfwvd1wGKmbjN7npL1u6_XkdNAm11vH2vNH0CN_6UDEL-oSgrQzmCK1mrZQ3XsPe2_hCrRuUEPSRjwSaA4pSGKPNINkD3wQyNMi1QKsxN3KRjIz2Daj0KBKpDd428ES9L8R1uuS4Tn5fMtxdKKo7NQPPyiXz_NlWOlj16g2DDFHAP7hUkuPwLXydUo9W5RJZICCnTbqColN3B8E4CQJXFHI2oj3xk30zAruDON-RBdwDenSGFiiQSTsEYfBIC5GIoBXNEf4cHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما هم فکر می کنید این بنده خدا و این بندگان خدا، ساده اند؟ یا من تنهام؟</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/mohsentavoosiseo/744" target="_blank">📅 09:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-743">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">چطوری بعضی ها خوش شانسن یا مهره مار دارند و همه جا سریع کلی آشنا و رفیق پیدا میکنن؟
در ادامه دو ویس بالا
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/mohsentavoosiseo/743" target="_blank">📅 18:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-742">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/mohsentavoosiseo/742" target="_blank">📅 17:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-741">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">چرا اگهی میذارن استخدام نمیکنن؟
😏
چرا حقوقو زده انقدر کم با این همه وظیفه؟
😒
چرا همه تخصص ها رو باهم میخواد؟
😒
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/mohsentavoosiseo/741" target="_blank">📅 17:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-740">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">هیچ اشکالی نداره مدام request index بدی تو سرچ کنسول. گوگلم مشکلی نداره.
ولی حرف من اینه که الکی داری خودتو خسته می کنی. دست و پا زدن الکیه و نهایتا نتیجه زحمتت ریست میشه.
مشکل جای دیگست:
https://t.me/mohsentavoosiseo/737
https://t.me/mohsentavoosiseo/739
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/mohsentavoosiseo/740" target="_blank">📅 17:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-739">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/mohsentavoosiseo/739" target="_blank">📅 17:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-738">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سایت های ابزار تحقیق کلمات کلیدی خارجی مثل mangools و keywordtool و ایرانی ها، از کجا دارن search volume (تعداد جستجوی کلمات) در ماه رو میدن؟
چرا دیتاشون باهم گاها خیلی فرق داره؟ چرا نمیشه به فرمول رسید؟
پی نوشت:
میگم نمی تونی بفهمی منظورم عدد دقیق و حتی حدودی هست. وگرنه ابزار ها میدن همشون. سادست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/mohsentavoosiseo/738" target="_blank">📅 17:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-737">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">چرا التماس کردن برای ایندکس شدن درست نیست؟
سایت من لیاقت ایندکس شدن داره؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/mohsentavoosiseo/737" target="_blank">📅 17:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-736">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سوال یکی از شرکت کنندگان دوره از پشتیبان:  من نیاز به بررسی کلمه کلیدی باتری یو پی اس از سمت‌ پشتبان رو دارم. در واقع میخوام بدونم ویدئوهایی که دیدم درست ازشون یاد گرفتم یا نه  سرچ ولیوم این کلمه رو ۲۱۰ پیدا کردم و kd رو ۱۲٪ همچین lps برابر ۲۸ میباشد دقت کلمه…</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/mohsentavoosiseo/736" target="_blank">📅 16:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-735">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سوال یکی از شرکت کنندگان دوره از پشتیبان:
من نیاز به بررسی کلمه کلیدی باتری یو پی اس از سمت‌ پشتبان رو دارم. در واقع میخوام بدونم ویدئوهایی که دیدم درست ازشون یاد گرفتم یا نه
سرچ ولیوم این کلمه رو ۲۱۰ پیدا کردم و kd رو ۱۲٪ همچین lps برابر ۲۸ میباشد دقت کلمه کلیدی که بین عدد یک تا سه در گوگل خودمان باید شماره گذاری میکردیم من سه رو دادم. تحلیلم این است که در این کلمه بیشتر باید هزینه off page کرد اگر یک محتوای بی عیب و نقص و تمامی موارد تکنیکال رعایت شده باشد در بهترین حالت رتبه ۸ به بعد رو بگیریم .
ممنون میشم راهنمایی کنید که این داده ها و تحلیل تا چه حدودی درست هست
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/mohsentavoosiseo/735" target="_blank">📅 16:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-733">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/mohsentavoosiseo/733" target="_blank">📅 13:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-732">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یک دوستی دارم که همیشه فکر میکنه من یه تکنیکی بلدم که انجام میدم سایت ها رشد میکنن. هربار فکر میکنه دارم میپیچونمش و نمیخوام بهش یاد بدم!  همیشم این رو مثال میزنه. این برای سایتی هست که من فقط یک ساعت مشاوره و راهکار دادم. اوایل فوریه. حدودا یک ماه قبل از…</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/mohsentavoosiseo/732" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-731">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fE46mHVXX1p_LlkGzJLsxA3Pdzao9xRxU6MJ8qXEsGY5pPwoqInOiOvRlsllG9bEjAsQRhMgMskUbCS7xzKId1Ewfyg26mV-VNetp1zHkQR7jfJzJZ0QZjGlSUg1cMiC4_AnRqr4KyJmRWFBYCyVGgiBym3w0fmXOy0CRHwjWmV6_51Uck_pat10_1ESmL-ihViEJ9kA2X4oH0K0k4YBBNJ2tVuMwY0wRlinwP4go6YPlWPp2tx86oPTZfx6w7ZllK-wA_Uz6uz8sVV3Nrk_0QuyVSBNTW71gYKx-R7E0-7AS0ItyiPS9FAZITgtyS8oakZRMIOPPrS0xqqZq4xbVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک دوستی دارم که همیشه فکر میکنه من یه تکنیکی بلدم که انجام میدم سایت ها رشد میکنن. هربار فکر میکنه دارم میپیچونمش و نمیخوام بهش یاد بدم!
همیشم این رو مثال میزنه. این برای سایتی هست که من فقط یک ساعت مشاوره و راهکار دادم. اوایل فوریه. حدودا یک ماه قبل از جنگ دوم(اسفند).
بازار آمریکاست و زبان انگلیسی. و فعلا هم خدماتش در یک ایالت هست فقط.
محتوای صفحات تولید شده هم اتوماتیک به کمک AI و ابزار ها هستند.
من فقط گفتم طبق این اصول باید این تعداد صفحه بسازی. لندینگ نداشت! کیورد ریسرچ نداشت! یه صفحه نخست بود و پنج تا صفحه دلخواه به سلیقه مدیریت!
همین! من تکنیک نزدم! تو سئو کار مفت نداریم. برای همین رشد اتوماتیک هم کلی زحمت نیروی انسانی و تحلیل وبررسی مداوم کشیده شده.
صفحه بساز! (بعد از کیورد ریسرچ)
همین! صفحه با AI و اتوماتیک ولی آبرومند و خوب بسازی، بهتر از اینکه نسازی!
این سایت هم رشد کرد تا جایی که رقابت اجازه میداد. یه سقفی داره. بعد باید دست به دامن Off-Page بشی.
هم تو دوره مفصل یاد دادم. هم رایگان اینجا دو ساعت و نیم. ضبط 2018 هست. الان در نیمه دوم 2026 هم همینه:
mohsentavoosi.com/200
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/mohsentavoosiseo/731" target="_blank">📅 13:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-729">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">لینک رویداد چند روزه رایگان و آنلاین گوگل درباره AI Agent اینه. این رو گفتم میبینم برای محکم کاری، بعد ضبط رو شروع میکنم:
https://www.kaggle.com/competitions/5-day-ai-agents-intensive-vibecoding-course-with-google?registerForCourse=true
ولی معمولا پرت زیاد داره طبق معمول. یک ربع مفید یا یک دید و ابزار بهتر ازش دربیارم کافیه برام.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/mohsentavoosiseo/729" target="_blank">📅 12:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-728">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یک آپدیت بزرگ بین المللی بزرگ هم در راهه. کلا صفر تا صد سئو ولی با AI و چند زبانه و به هر زبانی (حتی نه فقط انگلیسی). این به روز رسانی، یک Game Changer هست.
هرکس دوره رو کامل دسترسی داره، (اقساط کامل)،  به رایگان دریافت می کنه.
بعد از اینکه رویداد چند روزه گوگل درباره اتومیشن و خودکارسازی رو دیدم، ضبط رو شروع می کنم. این رویداد هم برای محکم کاری میبینم. چون خودکار سازی دیگه اصلش با کلاد هست. خیلی قرار نیست شما درگیر شید.
پیام پین شده برای تهیه دوره هست.
اسپات پلیر از خارج هم در دسترس شد و راه حل با وپی انش هم با هزینه جدا هست. ولی امروز در دسترس شد از خارج از ایران.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/mohsentavoosiseo/728" target="_blank">📅 12:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-727">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پشتیبانی دوره قوی تر از قبل شروع به کار مجدد کرد بعد از یک وقفه دوماهه به خاطر جنگ.
پشتیبانی دارای حریم خصوصی در چت تلگرام هست. وبینار نیست. روزهای خاص نیست. آزادانه هست (برای من آزادی خیلی مهمه). زنده هست.
و توسط اشخاص قوی و قدیمی از بچه های خود دوره انجام میشه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/mohsentavoosiseo/727" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-726">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دوستان گرامی، کانال بالا، کانال محمد قاسمی هست که ایشون دوسال با من همکاری داشتند و بسیار شخصیت باسوادی هستند.
اما مسئولیتی هم بابت معرفی و توصیه کردنم نمیپذیرم. استفاده از مطالب هرشخصی که اطلاعاتی داره، کلا مفید هست.
من منتورینگ برگزار نمی کنم. ولی ایشون انجام میده.
با تأکید بدون قبول مسئولیتی از سمت من (بابت معرفی کردن)، می تونید با ایشون منتورینگ سئو داشته باشید.</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/mohsentavoosiseo/726" target="_blank">📅 11:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-725">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسئو با محمد قاسمی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Megop_serp_analytics_2.0.4.zip</div>
  <div class="tg-doc-extra">33.9 KB</div>
</div>
<a href="https://t.me/mohsentavoosiseo/725" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این اکستنشن فقط یک ابزار نیست، یک مزیت رقابتی سخت و مهار نشده  است واقعیت این است که آینده سئو متعلق به کسانی نیست که فقط بیشتر کار می‌کنند. متعلق به کسانی است که هوشمندتر، سریع‌تر و دقیق‌تر تصمیم می‌گیرند. و در قلب این تصمیم‌ها، Keyword Research قرار دارد.…</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/mohsentavoosiseo/725" target="_blank">📅 11:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-724">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسئو با محمد قاسمی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dd6ab0dbf.mp4?token=k003IqbN43QFc4Y9zrS9k_P9hfE7mTu9KhBQO3SLlu9mCSXg4rXdv71OoTm-XwNRbHiogqh2eEVQvD_6zj5kOXAGx_M_6rKQj_d3gnu-XSw6hAUcipjADaZmUasTNUDF3O5YUeekuMx6F6t7GK08nN2JmvyK-pKEADK0YtMeJHep3uOp7uDC4lRjZR_Pxz-8u2mTD6ZFVDgwuWDe2lsGIFgmWCcpfaomXACO0xdVytvL0v9Ay22zQo5TJPeneHoakb8EbhUPEMMj2CeP3WEbRjPZWnN5PHFv51Rm8u0pvvOwozoshfGxTJYq3jBL0kltotv7121Oun98Bkrmw1V7Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dd6ab0dbf.mp4?token=k003IqbN43QFc4Y9zrS9k_P9hfE7mTu9KhBQO3SLlu9mCSXg4rXdv71OoTm-XwNRbHiogqh2eEVQvD_6zj5kOXAGx_M_6rKQj_d3gnu-XSw6hAUcipjADaZmUasTNUDF3O5YUeekuMx6F6t7GK08nN2JmvyK-pKEADK0YtMeJHep3uOp7uDC4lRjZR_Pxz-8u2mTD6ZFVDgwuWDe2lsGIFgmWCcpfaomXACO0xdVytvL0v9Ay22zQo5TJPeneHoakb8EbhUPEMMj2CeP3WEbRjPZWnN5PHFv51Rm8u0pvvOwozoshfGxTJYq3jBL0kltotv7121Oun98Bkrmw1V7Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این اکستنشن فقط یک ابزار نیست، یک مزیت رقابتی سخت و مهار نشده  است
واقعیت این است که آینده سئو متعلق به کسانی نیست که فقط بیشتر کار می‌کنند.
متعلق به کسانی است که هوشمندتر، سریع‌تر و دقیق‌تر تصمیم می‌گیرند.
و در قلب این تصمیم‌ها، Keyword Research قرار دارد.
اگر این مرحله را با یک ابزار ضعیف، workflow پراکنده و تحلیل سطحی جلو ببری،
هزینه‌اش را در همه‌چیز می‌دهی:
در رتبه‌گیری
در تولید محتوا
در زمان
در انرژی تیم
و در فرصت‌هایی که رقبا قبل از تو می‌بلعند
اما اگر اکستنشی داشته باشی که:
فرصت‌ها را سریع‌تر آشکار کند
intent را واضح‌تر نشان دهد
من همیشه گفتم و همواره خواهم گفت:
intent کاربر استراتاژی است و keyword Research فرمانده است
چیزی که شکاف‌های محتوایی را زودتر نمایان کند
تحلیل رقبا را ساده‌تر کند
و تصمیم‌گیری سئو را از حدس به داده تبدیل کند
آن وقت دیگر با یک «ابزار کمکی» طرف نیستی.
تو یک سیستم شتاب‌دهنده برای رشد ارگانیک در اختیار داری.
این همان چیزی است که سئوکارهای جدی را از سئوکارهای شلوغ اما کم‌اثر جدا می‌کند.
🖋
شاید پرسیدی که چرا اینهه سئوکاری که میشناسی هیچ کدام هیچ نتیجه ای ندارند
آیا واقعاً مساله بلد نبودن کیوورد ریسرچ است ؟
یا مساله در ساخت بینش است ؟
✨
همین حالا این اکستنشن را وارد بازی خودت کن
#کروم_اکستنشن_سئو
#کروم_اکستنشن_Seo
#chrome_extension</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/mohsentavoosiseo/724" target="_blank">📅 11:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-723">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سوگیری شدید و نگاه صفر و صدی در جامعه ما
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/mohsentavoosiseo/723" target="_blank">📅 17:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-722">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">برای پروژ های فارسی، ابزار های ایرانی کیورد ریسرچ کافیه.
زمانی که من اکثر سال ایران بودم هم من اشتراکی نمیخریدم. حوصله دردسرشو و قطعی مدامشو نداشتم. همه سه سایتی که اشتراکی میدن همینن.
برای پروژه های خارجی هم یا با پول کارفرما یا چند ماه یبار یه ابزار میخریدم. معمولا منگولز.
اما درک می کنم که یک پنجاهم قیمت اصلی وقتی پول میدی، باید هزار تا اکستنشن کروم تنظیم کنی که اون اشتراکی استفاده کردن ها توسط اون ابزارها لو نره. با دستکاری سشن و کوکی و وی پی ان و خیلی جزئیات و مکافات دیگه. که از نگاه بین المللی، عملا کار غیر قانونی هست. هم فروشش. هم خریدش.
نمیشه هم پول خیلی کم داد هم دردسر نکشید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/mohsentavoosiseo/722" target="_blank">📅 16:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-721">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اون 20 نفری که تا این لحظه جواب این رو بله زدند، خیلی دوست دارم بدونم چرا منگولز نه؟
من خودم منگولز پریمیوم 40 دلاری اختصاصی میخرم همیشه. یه سئو هست و یه کیورد ریسرچ. کیورد ریسرچ شوخی نداره. مهمه. مهمترین بخش سئوست.
منگولز خیلی بهتره در کل. ارزون تر با محدودیت کمتر با کارایی بیشتر. البته برای کیورد ریسرچ فارسی، ابزار های بومی ایرانی کافی هستند و نیازی به ابزار خارجی نیست.
برای تحقیق کلمات کلیدی کلمات فارسی، ابزار اختصاصی و حتی اشتراکی خارجی نخرید!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/mohsentavoosiseo/721" target="_blank">📅 14:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-720">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🟢
⭕️
نتیجه گیری:
با توجه به اینکه:
⭕️
تعداد فعلی رای ها که همین الان که دارم مینویسم 200 تا "بله" شده،
❗️
این هایی که بله زدند نمیخرن. نرخ تبدیل پایین تر (خوشبینانه یک سوم) خواهد بود،
❗️
هرکس رای داده اگه اولی (همه ابزار ها) رو بله زده، دیگه نمیاد اون یکی ها رو بخره و عملا تعداد کل "بله" ها رو نباید جمع زد،
❗️
در آینده رای گیری بیشتر میشه. اینستا هم استوری بذارم. 10 برابر در نظر میگیریم.
طبق براورد من
❗️
خوشبینانه 400 نفر ماهانه میخرن. بدبینانه 100 نفر. بعد از 6 ماه.
❗️
سود خوشبینانه: 800 تا 1600 دلار. بین 200 تا 300 میلیون تومن.
❗️
سود بدبینانه: 50 دلار. معادل حقوق وزارت کار. بین 15 تا 30 میلیون تومن. عملا با انرژی که ازت میگیره، ضرر مطلقه. گل فروشی سر چهارراه به صرفه تره.
❗️
امکان توسته پذیری با تبلیغات و پشتیبانی قوی و زحمت زیاد در دراز مدت تا 2500 دلار. و با اوج ناامنی با توجه به تغییرات تحریم، دلار و خود ابزار ها و قدرت خرید کاربران.
نتیجه گیری:
با توجه به دردسرهای زیادش، جای مانور پایینش، پشتیبانی سختش، توسعه پذیری بسیار محدودش،
ورود نخواهم کرد
😅
به فروش ابزار های اشتراکی سئو.
بلند فکر کردم شما هم استفاده کنید. هم استفاده کنید هم انتظارتونو از ابزار اشتراکی 1 تومنی که همه چیو با هم میده بیارید پایین و با واقعیت های میدانی آشنا بشید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/mohsentavoosiseo/720" target="_blank">📅 14:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-719">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-poll">
<h4>📊 حاضرید برای Ahrefs ماهانه 1 میلیون و 300 هزار تومن (1300) پرداخت کنید؟ با ماهی 50 تا اعتبار. یعنی 50 تا درخواست(request).</h4>
<ul>
<li>✓ آره حاضرم</li>
<li>✓ نه! No! Hayir! Nein! いいえ! 아니요!, لا! Non!Yox!нет!</li>
</ul>
</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/mohsentavoosiseo/719" target="_blank">📅 13:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-718">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-poll">
<h4>📊 حاضرید ماهانه برای سیمیلار وب Similarweb ماهانه 800 هزار تومن پرداخت کنید؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ نه!</li>
</ul>
</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/mohsentavoosiseo/718" target="_blank">📅 13:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-717">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-poll">
<h4>📊 حاضرید ماهانه 1 میلیون و 400 هزار تومن(1400) هزینه کنید برای سمراش؟ Semrush</h4>
<ul>
<li>✓ بله</li>
<li>✓ نه!</li>
</ul>
</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/mohsentavoosiseo/717" target="_blank">📅 13:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-716">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-poll">
<h4>📊 حاضرید برای ابزار Keyword Tool ماهی یک و نیم میلیون تومن(1.5) هزینه کنید با روزی 5 درخواست؟</h4>
<ul>
<li>✓ بله حاضرم</li>
<li>✓ نه اصلا!</li>
</ul>
</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/mohsentavoosiseo/716" target="_blank">📅 13:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-713">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-poll">
<h4>📊 حاضرید هر ماه فقط برای ابزار Mangools (کیورد ریسرچ)، 500 هزار تومن هزینه کنید؟ با روزی 25 تا درخواست.</h4>
<ul>
<li>✓ بله حاضرم.</li>
<li>✓ تا ابد نه!</li>
</ul>
</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/mohsentavoosiseo/713" target="_blank">📅 13:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-712">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-poll">
<h4>📊 حاضرید هر ماه انقدر هزینه کنید؟ماهی 3 میلیون و 700 هزار تومن برای همشون. ولی ابزار ارزون تر کیورد ریسرچ رو فقط میذارم:   Ahrefs,SimilarWeb,Mangools KWfinder,Semrush</h4>
<ul>
<li>✓ بله حاضرم. میصرفه برام.</li>
<li>✓ خیر. به هیچ وجه.</li>
</ul>
</div>
<div class="tg-text">قیمت تمام شده (سر به سر به ازای هر خرید) برای هر کدوم از محصولات زیر با فرض اشتراک بین 20 نفر. برای یک ماه.  نرخ محاسبه ریال = 180 هزار تومن با احتساب کارمزد تبدیل و سایر موارد خرد انتقال پول. رنده شده به بالا به ازای هر پنجاه هزار تومن.      Ahrefs= 6.5$…</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/mohsentavoosiseo/712" target="_blank">📅 13:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-711">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">قیمت تمام شده (سر به سر به ازای هر خرید) برای هر کدوم از محصولات زیر با فرض اشتراک بین 20 نفر. برای یک ماه.
نرخ محاسبه ریال = 180 هزار تومن با احتساب کارمزد تبدیل و سایر موارد خرد انتقال پول.
رنده شده به بالا به ازای هر پنجاه هزار تومن.
Ahrefs= 6.5$ = 1200
نفری 50 تا اعتبار در کل ماه. 50 تا request
1 میلیون و 170 هزار تومن.
KeywordTool.io
= 7.5$ = 1350
نفری 5 درخواست در روز.
1 میلیون و 350 هزار تومن
Mangools = 2.1$ = 370
نفری 25 کوئری بخش کیورد ریسرچ. در روز.
370 هزار تومن
Semrush = 7$ = 1260
سمراش جوری نیست که به درد اشتراکی دادن بخوره. چون باید سایت ثابت بدی. عملا استفاده 20 نفر مقدور نیست. فقط بخش هاییش قابل استفاده است.
دلیل خرید Moz هم درک نمیکنم اصلا اگر کسی میخره!
Similarweb رو میشه به بیش از 20 نفر داد
چون حالت کردیت و محدودیت تعداد درخواست و روزانه نداره. این رو میگیریم 50 نفر.
Similarweb = 4$ = 720
720 هزار تومن.
این فقط قیمت تمام شده خود ارائه دهنده ابزار اشتراکی با این تعداد کاربران نوشته شده هست به ازای هر اکانت. سالانه بخره حدود 25 درصد کمتر میشه. ولی سالانه ریسکش بالاست برای فروشنده.
حالا هزینه جاری و توسعه ابزار و نگهداری سیستم و پشتیبانی هم حساب کن. من میگم بدترین حالت معادل نیم دلار و بیشترین حالت معادل 2 دلار به ازای هر کاربر. به صورت کلی باید روی قیمت ها بیاد. تا اینجا که هزینه خود فروشنده بود.
در حالت فروش دسته جمعی همشون با هم، باز 2  دلار روش میاریم در بیشترین حالت.
هزینه جاری در کمترین حالت ممکن: 50 میلیون تومن. ولی بهتره 100 در نظر بگیریم. حداقل 500 دلار. در ماه.
میزان درگیری ذهنی و دردسر فروشنده: بسیار بالا.
سود فروشنده در صورت داشتن ماهی 1000 تا کاربر ثابت(که عدد بالایی هست):
در کمترین حالت به صرفه:
90 میلیون تومن - 500 دلار
منهای هزینه جاری: در حد حقوق وزارت کار
در بیشترین حالت به صرفه(که کاربر کم میشه چون نمیتونن پرداخت کنند):
360 میلیون تومن. 2000 دلار.
منهای هزینه جاری: بین 100 تا 200 میلیون تومن.
مشتری واقعی پایدار بر اساس واقعیت فعلی هم، 1000 نیست. هزار باشه باز هم عدد وسوسه کننده ای نیست.
نظر سنجی زیر رو میذارم که عدد در بیاد.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/mohsentavoosiseo/711" target="_blank">📅 13:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-710">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">با توجه به افزایش تقاضای ابزار های اشتراکی، من قصد داشتم خودم به این حوزه ورود کنم.
ایراد هایی که به سه سایت ایرانی ارائه ابزار اشتراکی خارجی داشتند این ها بود:
- پشتیبانی ضعیف
- قطع شدن مداوم ابزار ها و هدررفتن زمان اشتراک
- نداشتن محصول مورد نظر
- طراحی و تجربه کاربری ضعیف.
حالا برای اینکه من بفهمم صرف مالی داره ورود کنم یا نه و شما هم بفهمید(!)، نظر سنجی می کنم از شما.</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/mohsentavoosiseo/710" target="_blank">📅 13:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-709">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvwQUOeOOWm4ap5ye9umvCOl9QtUSvdiHebHN0x473XaW3tOLh71XrShdakoF_n5NUZnI_el0iI9ISEzBi9R-OZwCnyza6LY4_4G7daxut2IzBa4UA4pvrU2kZN_kjUO8K73441q8bCF-_GI56qWwiyOqrKT6piuVKdhS8m5TSqSdkUYGHMrKQdw3s7whu6s2c40wrfhGuUh19ywO2X5Zq1K9dAMr747skB02xHa4AtHxyvLbcb1-rHHBXieLX6cgJmhYhu7Az0dEgQuP7YBTvsWQZ6_LmTWRd25aAg5tQkrNcn7OHbJMw9sEgOJzXBhV8417UCdxx7_gUGwdCZ5ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر با AI زیاد سر و کله زده باشید ارزش جواب کلاد رو میفهمید. هرچند که نسبت به بقیه معجزاتش چیزی نیست.
وضعیت:
گفته باید رو سرور نصب کنی. ولی به جای "سرور" گفته رو سیستم. منم اونو بهش گفتم.
حالا AI های دیگه بود چی میگفت:
اره حق با توست. باید روی سرور نصب کنی.
جواب کلاد:
منظورم از سیستم، همون سرور بود.
تفاوت رو متوجه میشید دیگه؟ خیلی تفاوت داره ها! خیلی!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/mohsentavoosiseo/709" target="_blank">📅 18:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-708">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3494a006a0.mp4?token=IYv6paeM3DqTXbZVY1j3wr5p9-UNhmTsJs_u_PBEh4tc3bXoc7Adrcc_Ggo1mW4l0kBQfuwjc2_nFXmVCFhbQT3CqdmYFGdguQk4H6HnoRSmsUpqkMGrlb6bh2IG2_W78i0RcCdNGpketC6hOMetiWW17B63GSvMmMpbRfCwyfWbtp1wL68dP0lSsQc3UWKnDsBC4yG84dgn_F-XQOJet3T0duG8kJXM0wFTfZra8ZpW54ZAmelDzssauK3cYSFXcLgDy-VXX0aIdka7_gvj2AKqVbvVfwF5nUxezuvq5OkRJ-2k_KKpH-1hsGDBp9sTafw0i6G_B2swl5el3YJkQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3494a006a0.mp4?token=IYv6paeM3DqTXbZVY1j3wr5p9-UNhmTsJs_u_PBEh4tc3bXoc7Adrcc_Ggo1mW4l0kBQfuwjc2_nFXmVCFhbQT3CqdmYFGdguQk4H6HnoRSmsUpqkMGrlb6bh2IG2_W78i0RcCdNGpketC6hOMetiWW17B63GSvMmMpbRfCwyfWbtp1wL68dP0lSsQc3UWKnDsBC4yG84dgn_F-XQOJet3T0duG8kJXM0wFTfZra8ZpW54ZAmelDzssauK3cYSFXcLgDy-VXX0aIdka7_gvj2AKqVbvVfwF5nUxezuvq5OkRJ-2k_KKpH-1hsGDBp9sTafw0i6G_B2swl5el3YJkQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/mohsentavoosiseo/708" target="_blank">📅 17:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-707">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lS-_6zH3c6guoWcww3VVn5DN9hNwlAY2LYMdEywiDafKJPSZIzzDeON8y0m1izzGahLDkd0FrdZG3PLPojWFOtWa8r0XYAZS32QAmaeZikdC30IOVMJxEA_xOULkeKlAFx5wHuBuh3bHsMGhAUqNIkh8CryOs7YO8wnRiFoBzALtUOL5khW_5mb-ezWprMRGucqLVTD4e0MzdmCWpBnjS8zH68f8jbh6tBVzxrlciZ8yLWc2uB9EG6XNz4m-AO-sQaDm24rmfQWjXcriYg5ppyQOp4hSKCX8M3wFzFFqOAOmQ3-ZjPbcUQw0v_F9OfHAOw3l6ntORPibtSZPWg42Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کم فارسی انگلیسیش چپ و راست هست. ولی همین کافیه تا عاشق کلاد بشید!
اه! انگار قبلا اپدیت شده بود. بذار!
😅
😍
😍
😎
فقط هم ادا نیست. واقعا بازدهی و خروجیش عالیه‌.
هنوز خیلی ها از skill در کلاد استفاده نمیکنن.
در اپدیت دوره، علاوه بر سئو بین المللی(که الان هم یک فصل داریم)، این ها هم آموزش میدم و هرکس دوره رو داره، رایگان آپدیت رو دریافت میکنه. فعلا زمانش رو نمیتونم بگم.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/mohsentavoosiseo/707" target="_blank">📅 16:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-706">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a993e8989.mp4?token=g60RqAaHUyMMdDfkJmJyTXwQeMpuv6S_gJ9hZdT5tFV9LER_e1pL7WVD2JPdQeIkLgSdk052QXQY3Zw-1MZsLOWB5k1oj1GBrQSTIR--UZtDyekDTmBi-gJF0agpDPynqowj-LK-L2xGCYDuXAbgbRV2osOuflK1LOHtWwzLkRvcFQ3u45UMgXoo09f8FbYqHIRL0Qx515WAtFrOjR5PQZ-dJca-j1U-eNY41TcFwXpF3TxFkiBl6mJ0y3sE0EnvntAeHOxAtSgA1auAFsmsWJSBdlsW6qwL8IuehLpO9QepzYMnJZHbNz3Y5wsB4g15lvHO8hG2t09_yCaaiTHgJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a993e8989.mp4?token=g60RqAaHUyMMdDfkJmJyTXwQeMpuv6S_gJ9hZdT5tFV9LER_e1pL7WVD2JPdQeIkLgSdk052QXQY3Zw-1MZsLOWB5k1oj1GBrQSTIR--UZtDyekDTmBi-gJF0agpDPynqowj-LK-L2xGCYDuXAbgbRV2osOuflK1LOHtWwzLkRvcFQ3u45UMgXoo09f8FbYqHIRL0Qx515WAtFrOjR5PQZ-dJca-j1U-eNY41TcFwXpF3TxFkiBl6mJ0y3sE0EnvntAeHOxAtSgA1auAFsmsWJSBdlsW6qwL8IuehLpO9QepzYMnJZHbNz3Y5wsB4g15lvHO8hG2t09_yCaaiTHgJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که بحث مقایسه مترو ها شد جا داره بگم، مدیونی اگه به ایران بگی جهان سوم.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/mohsentavoosiseo/706" target="_blank">📅 11:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-705">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فقط هم کیلومتری مقایسه کنیم باید مساحت کل اون شهر هم در نظر بگیریم. استانبول ۷ برابر تهرانه. مساحت توکیو ۲ هزار کیلومتر. مساحت تهران ۷۵۰ کیلومتر.
با همین فرمون سرچ کنسول گوگلو تحلیل کنی تا ابد غلط در میاد تحلیل.
مثل نگاه کردن به avg position کلی برای تشخیص رشد سایت!
تازه طرف فکر میکنه چون حرفه ای به کلیک کار نداره پوزیشنو نگاه میکنه! اینجاست که کسی که فکر میکنه حرفه ای تره آمارش غلط تر میشه!</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/mohsentavoosiseo/705" target="_blank">📅 11:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-704">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QK6VyEYtjU57ftMWo4v8IUAm-plM7XuqdKbMDtOKKVNH13nbseV92sfCwa9UmhdEdBE9sIiSmRkwNbhqiESfRPC9rTXlDInGEA4mOXqDQUtYm8bwmccFeZckZe0LU6yz6VG7KaKh6lN7rTrurCMsEuakGd1Z6uLPsYqPg9GbhYaG_9bSo5e-9Cn5A0mvaSCoyRv073qW11kujxLozpevu2tRFG3fhEgecdBmpcte-gCdP9whhL_DdluxqnS0CoSy3ZEw9RMBDQCOMZUp-bAT_P_54SQU8qbGH30VsG5EgktQ4uf0dKKnYP1M_UztYgMDmzjbve2JCgPsBumc3XXCfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/mohsentavoosiseo/704" target="_blank">📅 11:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-702">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzWfC8OoKuoIEqWfO5avZLK3qdNi4d-D0SuQrCJ5GLuaE5tIzarZlQTuiD5r-WPA9ZVtLKB7hfJ6sQIkQoBLoZCp7-tF3p26T7Sz6TbMzt_IyZpPHRnzo8eHT3hkYT-3SInom0gH3uNEZ5YLaJoeW6onI3CmiKESxtMYFRGYRwUApJ5hfBXt949iOeykUizLpKs9Q41GIbVcVhmPzDCoukWEc7cHCaWgsuBSdWf9e_ymdgPBPArcvIiGUdnzvp66_gvKQ_OPgA7Wo5QS657MwWbs6SAC8wkVQMjppu9uvpsTONqOYScB1nr2OQxNcOE40p8sl72EtyTfBMCI-exviw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سئول کره جنوبی</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/mohsentavoosiseo/702" target="_blank">📅 11:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-701">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODEStHLQXds0kqiF45Ljrk5O0UpZW-nOjDkvB6Z1pKFBJuo4QrlY8EOBHQFqev8grH7cXkpLNHe9jMX_7yaYTaviQ_v-dPFX9sX_VeYDHo6vjq4p5vhjQxt7NeNN9GDMnYMZyuSrJFvsqk5kmEoGTUxwasGQEY5pC8AfiApCkwvz9nj38OMEV4dvTEEyHuylJh7CdrI3wsFi2m3UEjEkrCHJgRqBJggWZms3_6lUBZyK6LMQVZmBUCAEEEOSx01ePHh0fejJoozOBae9RUMmvNfY20Fl7r5e_73wfLUORk4NDZ-QC2PqH-F3p21yh-oekLHKYt3ZTZEC8lQkrUuDig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/mohsentavoosiseo/701" target="_blank">📅 11:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-700">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDkB8uFQpzanvP9kN_y8cZw02cVPryALo3bvjcz0IlDQUilkGIozdwHVzfw7vdUE5Mijq5TbCToMsychEX_J-JI4p8CQCE3pJnV-aXMiHhXisJlmIHrKykR6SQbOSO6ktaTO4IF3y4EhewKY-mRv07XAGarYiD1qlmjsza1YiOGvUkux1qfj15pABUZPwt3ZhMQw_fI1SQ3dOH1FTC-QSAP_N5LE0NqRizu8UDjo31ZtoRjc44BQyO6uOHaNeK_xcFCqKuSdWarGXoUitdUjCuUkLGgD9avVPB4-LTpY5tUpZg-vXnDMuZYGt-cYSzl5Upq8kOnkeRWUIp5dlyW8yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیل هایی که به بیراهه میرن!</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/mohsentavoosiseo/700" target="_blank">📅 11:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-699">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تحلیل هایی که به بیراهه میرن!</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/mohsentavoosiseo/699" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
