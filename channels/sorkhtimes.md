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
<img src="https://cdn4.telesco.pe/file/ImPoUW4ZnVcsvQH267dLrX65Qf-kW8VYx0FaFG0r47jYt5tXdYWj3qnEdyjYuD9dvLkK2fFZucj6JKVf6eGzi_MLnyz_ueZ_r-MoHvfgxnV0I-iWdhgZRYMRoBYYyY3OhkQQmtjkAKCnfs2uMvFgw2mEeiSydpSZFrnlziYAVkZHu3rvZU4dxFnRnMK4PAg6KinXRysshe5BsMZvxxzoBLhRjKYpyDVH6JINtdlz4nTsNSeIG1QKlUhaKD41H2XcYXfmLvHvFug1lbvJu8yNwaGWIZrO6F7XI4aCTboex7A3bWmh_t4ZknhmYjgvxc8GKpHLoIbOhaFSgX7aEHfQPg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 21:30:48</div>
<hr>

<div class="tg-post" id="msg-135056">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpghB9YdI5vtB6ycAJk5DJQifhTtiI0XjsBUYG2Brx0Cx1eiiC8ovTzsi1XOKR2du3aX_6DQPGA8ApSsAH0ZP2PflKQEPfHPn_P-d5AwZ2HkyqRLNeRbSvGAu_bYwvqY1fdMT-sAA2xWQBbIZfjKPJaBiUe0YnSw8Wvzy37KWNnSVXdONtQAOtUE8GHao6rdmBtPBo7mGXzsJBM2xdCHOafx1GEOJzx18MFxR-0X60bPmwr_X84Mv3g8ZLie4MZbosUvgKvSe60eEwKBfwRhJ1gCsbvmojJZMU8_umqG9wOwP90fUddfAnsisEwiSX__C4CBEZY33YREjibG2MujuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
فیفا به درخواست ترامپ، کارت قرمزی که مهاجم آمریکا، داخل بازی قبل گرفته بود رو بخشید تا محرومیت بازیکن تو بازی بعد جام جهانی رفع بشه!!
❗️
پ.ن سیاست آوردن تو فوتبال و ترس از آمریکا و ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SorkhTimes/135056" target="_blank">📅 21:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135055">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
پورعلی‌گنجی، عالیشاه، بیفوما و گرا تا حد زیادی جدایی‌شان از جمع سرخوشان قطعی است.
🔴
کاظمیان، شکاری و سرلک نیز مهدی تارتار بعد از بررسی وضعیت آنها تصمیم گیری خواهد کرد. / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SorkhTimes/135055" target="_blank">📅 20:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135053">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافقات با مهدی تارتار انجام شده است و باید تارتار رو رسمأ سرمربی بعدی پرسپولیس بدونیم!
📚
مهدی تارتار یک دستیار اسپانیایی انتخاب کرده و با خودش به پرسپولیس میاره؛…</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SorkhTimes/135053" target="_blank">📅 20:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135052">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
جواد نکونام با گل‌گهر به توافق رسید و جای تارتار و میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SorkhTimes/135052" target="_blank">📅 20:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135051">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYa0Q8bpjhI1p7TNV3v0cMuSbLCQ7njIQGTEqLP07TN0UEFfr6tDzNY3e697FA2hbJJb02Z1adRSdl-PZlKAhoMk9hweLv-b1TCK0TGXFtfrqta4tz6gcIN5yYMx71wtQTLgiuw8jtDwcuyqsvYvRXyfrknJt3NieVyc04gdplG-m9Bj1BOZlONK30q-PSeQV6Rx-iHyuP7tmfmi9qGqzrzIyiIC1jaMxytGj3iImffM5xMX2boTlx9b62wxnVpA4d9rwqPGnzrAw9BZqoZMT5CNmN2I7A0_t5xmhksxWvWlcrEbp3OYjGWaedhJPPrn4qKA-vISJnfub1Bl-KDioA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
#تایید_خبراختصاصی | #اولین_رسانه
🏅
مهدی تارتار سرمربی پرسپولیس شد!
🤫
دیشب به نقل از مدیران باشگاه اعلام کردیم تمام شده و ته دیگش رو هم خوردن…دیدید که امروز رفت باشگاه و بست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SorkhTimes/135051" target="_blank">📅 20:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135049">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join
Join Join Join</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SorkhTimes/135049" target="_blank">📅 20:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135048">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZGaTrNZULVYn6794rihIHeALl03Op-4-rzHrdoyKB5ryo4ajmOdj1PnXc7K--o2cgSDqLjt2pXljiRnLYmDa4zV_xzfHW3dZa_8eqTebWWjwqnYoF8tCXgBZeOsp4EkG_lhkrHdLUAiUkdHrjOxGwQ9uexSyl5PhgkZvSzD84SY_e-36sekPi-MN8w5cPydRmGbPBnSZi10Nt-LA_-SowEdBBGZendCmMtpD9chTr-gszJrrTMQ2W-VbMwbjcAyULqeJKBqM_5uqgYXSTMVpm1VmgQv6KGwwNvdtyZDSH2V2HFCaj_Yuiyriju5i1_W5zsB2yeO2ZRT9ri2JmANLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@HaJFixed</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SorkhTimes/135048" target="_blank">📅 20:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135047">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❗️
کسری طاهری و پوریا شهرآبادی به ترتیب دومین و سومین خرید باشگاه پرسپولیس خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SorkhTimes/135047" target="_blank">📅 20:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135046">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5elwLOWOSwrv7jrxwgHxyOkrFYo8EX2JE2m2bxO2n_XoDRvLsv1z0AkrVinz2G4uFynzvXltYASmkfuHiVeqIhm8MMg2dlnz39LGJSS9bWF67MehSf-KW3IxORh3UiEQr4PcS_9uLUknpIExhyyPEJJUg67YIzvDVxGdns1y9nePXJqF6I8oopyQnzM_PKn5CIcRrh8CkgugxqLRoKVnep7lPB7IMnKk9KkGQTkSRJ9enO4TeM4WN3RJUwcPzAbkbm_qLNYUQl263_yuYHYDjWDcnQRfySv4I8LSkYL5VrlDYO62lDbqBak9SlQySgViE9YQHWuADPZ-p6TeOoXKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جواد نکونام با گل‌گهر به توافق رسید و جای تارتار و میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SorkhTimes/135046" target="_blank">📅 20:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135045">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❗️
کسری طاهری و پوریا شهرآبادی به ترتیب دومین و سومین خرید باشگاه پرسپولیس خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SorkhTimes/135045" target="_blank">📅 20:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135044">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❗️
کسری طاهری و پوریا شهرآبادی به ترتیب دومین و سومین خرید باشگاه پرسپولیس خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SorkhTimes/135044" target="_blank">📅 20:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135043">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
✅
سه دستیار تارتار معرفی شدند
🔴
حسین اینانلو به عنوان مربی دروازه‌بان‌های پرسپولیس فعالیت خواهد کرد. اینانلو با ۱۸ سال سابقه مربیگری و دارا بودن مدرک مربیگری A آسیا، یکی از مربیان باتجربه فوتبال ایران به شمار می‌رود.
❗️
وحید فاضلی، که سابقه سرمربیگری نساجی…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/135043" target="_blank">📅 20:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135042">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
✅
سه دستیار تارتار معرفی شدند
🔴
حسین اینانلو به عنوان مربی دروازه‌بان‌های پرسپولیس فعالیت خواهد کرد. اینانلو با ۱۸ سال سابقه مربیگری و دارا بودن مدرک مربیگری A آسیا، یکی از مربیان باتجربه فوتبال ایران به شمار می‌رود.
❗️
وحید فاضلی، که سابقه سرمربیگری نساجی…</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/135042" target="_blank">📅 20:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135041">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
اولین بار گفتیم تمومه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/135041" target="_blank">📅 20:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135040">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
یاگو به عنوان مربی بدنساز فصل آینده پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/135040" target="_blank">📅 20:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135039">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d10HFZUzFBTNvv5mymNgI9RK1yeFGuJnaCMrbgPlwp8jg6g30VmGl_g7V5O63p0ciLomBcvTtEkz261G71GbAr2bwcpqJtFIWnY0sNF-h-w2ORAMelk5-Y0hDHaLQ2BOHOsAxXqk-SeVylKlbQDQNK1VxEItTHPmnS8XtHHCusupU176MbZqmWuJzNDIhPNfVFamDzr17rBqah4kUz3EuTXvsybfNtJBz4uwgMh9iTE_BxuWd9ORUFONMBdh9nVBRxlPLWDZzB4yrp6aspxJWWmNGkeolDlvoneBg_KL2f-KUmiwa6QK8ODFQ8XLgf19sPOV_-1y4ZCFLHeMLU6O_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یاگو به عنوان مربی بدنساز فصل آینده پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/135039" target="_blank">📅 20:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135038">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
❗️
فوووووووری
🔴
علیرضا محمد مدافع سابق پرسپولیس به عنوان دستیار مهدی تارتار انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/135038" target="_blank">📅 20:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135037">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
🔴
رسمی؛ مهدی تیکدری، مدافع راست ۲۹ ساله فصل گذشته گل‌گهر سیرجان، با امضای قراردادی دو ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/135037" target="_blank">📅 19:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135036">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpjWwm1GQ32alTpjsH3CZpArEdzn8MCKwEgLLChfEY3V9fOsFeFU1P3zrb-c9NToCaBDXUjRh-kQDFlsA7cbXtXaT9rGIgM8_RE6eCzwe1NGqh4rWtYphYsDUppeAz-S5SAXeYV2iM_QgxwndIhJBEkoShbUQGrYW1wh6B7CgkH3LF_YYRwBYugJwTxDHxhWDm3KIsfBpSVqtUwQjZRnDcm9ZkEgOXjH_5cfynHbUfJ5RkcHFKmZENGcCbAzOAvTxqej7kYlDQDnMlMVDaeMcwLu8SkGrjc9b-xxTyzmF2zPmkF_RyGfumgGjNRg46VQs_GeF_tAAps0yArLCVQcUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اولین بار گفتیم تمومه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/135036" target="_blank">📅 19:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135035">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔖
🔖
مهدی تیکدری بزودی رونمایی خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/135035" target="_blank">📅 19:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135034">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
❗️
فوووووووری
🔴
علیرضا محمد مدافع سابق پرسپولیس به عنوان دستیار مهدی تارتار انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/135034" target="_blank">📅 19:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135033">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
🔴
یک سرباز واقعی، ستاره متعصب و جنگنده پرسپولیس؛ بازیکنی که برای لباس پرسپولیس، سر خود را جلوی توپ می‌گذاشت.
❗️
❗️
مدافع محبوب هواداران پرسپولیس، امروز ۴۹ ساله شد. تولدت در قلب آسمان مبارک، "داش علی انصاریان".
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/135033" target="_blank">📅 17:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135032">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
🔴
فرشید حقیری: تارتار از هفته ها قبل سرمربی پرسپولیس شده. حتی تارتار دو روز پیش زنگ زده به آریا یوسفی و گفته پاشو بیا پرسپولیس
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/135032" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135031">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
❗️
حقیری :علت جدایی خداداد عزیزی از پرسپولیس مشکلات مالی شدید باشگاه اعلام شده است!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/135031" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135030">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❗️
مهدی تارتار سرمربی جدید پرسپولیس خواهان حضور پویا پورعلی و پوریا شهرآبادی در پرسپولیس شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/135030" target="_blank">📅 17:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135029">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
✅
مهدی تارتار تصمیم دارد چند بازیکن از گل‌گهر را با خود به پرسپولیس بیاورد. در حال حاضر تنها انتقال مهدی تیکدری به پرسپولیس نهایی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/135029" target="_blank">📅 17:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135028">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔖
🔖
مهدی تیکدری بزودی رونمایی خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/135028" target="_blank">📅 17:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135027">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
#تایید_خبراختصاصی | #اولین_رسانه
🏅
مهدی تارتار سرمربی پرسپولیس شد!
🤫
دیشب به نقل از مدیران باشگاه اعلام کردیم تمام شده و ته دیگش رو هم خوردن…دیدید که امروز رفت باشگاه و بست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/135027" target="_blank">📅 17:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135026">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❗️
ادعای علیرضا محمد، دستیار تارتار در گل‌گهر: باشگاه پرسپولیس با تارتار مذاکره کرده و اگر اوسمار برنگردد، تارتار سرمربی میشه! او می‌تواند پرسپولیس رو قهرمان کند! باید چه کاری دیگر کند تا سرمربی شود؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/135026" target="_blank">📅 16:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135025">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❗️
✅
باشگاه تا ساعاتی دیگر از اولین خرید تابستانه خودش رونمایی خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/135025" target="_blank">📅 16:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135024">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
❗️
فوووووووری
🔴
علیرضا محمد مدافع سابق پرسپولیس به عنوان دستیار مهدی تارتار انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/135024" target="_blank">📅 16:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135023">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
#تایید_خبراختصاصی | #اولین_رسانه
🏅
مهدی تارتار سرمربی پرسپولیس شد!
🤫
دیشب به نقل از مدیران باشگاه اعلام کردیم تمام شده و ته دیگش رو هم خوردن…دیدید که امروز رفت باشگاه و بست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/135023" target="_blank">📅 15:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135022">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافقات با مهدی تارتار انجام شده است و باید تارتار رو رسمأ سرمربی بعدی پرسپولیس بدونیم!
📚
مهدی تارتار یک دستیار اسپانیایی انتخاب کرده و با خودش به پرسپولیس میاره؛…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/135022" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135021">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNQUX-zlw4MrTonqrWQcn40wUaueRSMmNPaxctuNsq40vPzsc2okKwy92yiqZdVi6UyaWRe9Qo-gKDMiDrYx6Y-LAwrUU_EXvNtyv77RpJk4tDmZd3Nx-WgJATXW4dg_R5qzbSf0yCK6u_AcksNe1lfXulZSc2_yiA9vq-2-B7f-35egLK93CugX0b7wPqd-v0H-frNKpiG5LvpTmp3GdOgQDipy8TPnRA98cXyFonhW7CQMlv9k5fkUyt8dTMxkgB-mGr1QVwzf1EmXReRvWkmtoRuLOa03bgqLyruzGAlrhtNzFvMWerKKDLWCQKVV-nltVTa-mMtfBQW0FhqWfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافقات با مهدی تارتار انجام شده است و باید تارتار رو رسمأ سرمربی بعدی پرسپولیس بدونیم!
📚
مهدی تارتار یک دستیار اسپانیایی انتخاب کرده و با خودش به پرسپولیس میاره؛…</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/135021" target="_blank">📅 15:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135020">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
🔴
🔴
🔴
سرانجام تارتار به آرزوش رسید
🚨
ازش حمایت میکنین؟
👍
👎
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/135020" target="_blank">📅 15:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135019">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
تموم شد مبارکه..تارتار رسما با پرسپولیس امضا کرد/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/135019" target="_blank">📅 14:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135018">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🔴
🔴
🔴
سرانجام تارتار به آرزوش رسید
🚨
ازش حمایت میکنین؟
👍
👎
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/135018" target="_blank">📅 14:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135017">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
ورزش سه مدعی شد تا ساعات آینده باشگاه پرسپولیس رسما مهدی تارتار رو به عنوان سرمربی معرفی میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/135017" target="_blank">📅 14:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135016">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U86I0xNTT1FRI3X-qQA45Lb52wf-UbdRGkOPlXWyiUyrmoQF12eJ4PbS9dc2t4qQ0AXZTTDaNuQm_d8lAumiGvB5-SgT_5GGTlid1gHqtbRpqsFf46TT95kvXbQRzgtw1ShKvOATgNf70bV1dkQzrX1wmQeGecIfVRi-FdG19D-yojSxN9w4ns3zb1jpHWMC0mW_330NAGSg2SoXavdHgV7Pl1Rq1ezE8vGoGzXA3x0vdZtN088w8zLl_v8NSbpbxX0Ju-DVO-p365fx8sL3l9raUHmQfcVi-GqVS67SXywL8Sbm938GJOsGZ2oB-wgqfPiJRfUejRQtfrHblRYQjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شنیده ها: محسن خلیلی ساعتی پیش با حمیدرضا گرشاسبی برای انتقال ابوالفضل رزاق پور دیدار کرد و قرار است در صورت توافق شخصی با بازیکن و واریز مبلغ رضایت نامه این بازیکن راهی پرسپولیس شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/135016" target="_blank">📅 14:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135015">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7568e30ff8.mp4?token=jYErEuUI2lEVIyOLN3-Vl8_Zb5PQjoD169E5e79HR0xptE0U0_8liDb5wWq_jWfpMYMXriZ-7ebxszuEKOu1bOAMn_a9aL-SYTAk1DhLL35KOFhSXh8fWxP706cfGn6CWsSSHnNFhK-HMMQp2UQiMwkdarFe6on_FPdXPv0kNiqQSr1xBiHC0dQfpML6vIxIOLe6KNslpr8DazWRR58E3foLu_E9-9x9wfzNvM-mGXtbuQ_Rw391dCPGipptcIBXePZ6CL2sHa6_BN0WwNNaQ8rkQtvYqb7nwR2tFuTipRNPJkYFuin8a1Rgz3jtJeecxs5fL9d_amg1upYspRQu6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7568e30ff8.mp4?token=jYErEuUI2lEVIyOLN3-Vl8_Zb5PQjoD169E5e79HR0xptE0U0_8liDb5wWq_jWfpMYMXriZ-7ebxszuEKOu1bOAMn_a9aL-SYTAk1DhLL35KOFhSXh8fWxP706cfGn6CWsSSHnNFhK-HMMQp2UQiMwkdarFe6on_FPdXPv0kNiqQSr1xBiHC0dQfpML6vIxIOLe6KNslpr8DazWRR58E3foLu_E9-9x9wfzNvM-mGXtbuQ_Rw391dCPGipptcIBXePZ6CL2sHa6_BN0WwNNaQ8rkQtvYqb7nwR2tFuTipRNPJkYFuin8a1Rgz3jtJeecxs5fL9d_amg1upYspRQu6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
مارکو باکیچ : خانواده ام به من گفتند به ایران نرو!
✅
قطعا آنها دوست نداشتند من به ایران برگردم. پدر و مادر همیشه بیشتر از خود فرزند نگران او هستند و من حالا که خودم پدر هستم این را درک می کنم. من هم اگر الان فرزندانم بخواهند به کشوری بروند که هر روز در اخبار می خوانم مشکلی در آن وجود دارد، مخالفت می کنم. نگرانی آنها طبیعی است اما من هر وقت خبری می شود برای آنها عکس می فرستم و می گویم نگران نباشید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/135015" target="_blank">📅 14:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135014">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🔴
🔴
🔴
سرانجام تارتار به آرزوش رسید
🚨
ازش حمایت میکنین؟
👍
👎
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/135014" target="_blank">📅 13:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135013">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">😀
دوماگوی دروژدک با پایان قراردادش از تراکتور جدا شد/ ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/135013" target="_blank">📅 13:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135012">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
فوری؛ با پرداخت 20 میلیارد، رضایت نامه مهدی تارتار برای پرسپولیس صادر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/135012" target="_blank">📅 13:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135011">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0jCuFJes6TXRV1ZuD1LHlyvXFV_tMH0bOxOMz5XK0P_E5vo2vXFNe8xuVNmwG9YjUhqCFyMrp1CFLw64IJrtME_XqGlXkcVtoxfW1Rxphwi0BeFxG7sbcsS_zYsCBp5Nc7r_Y-oK9LooU0E45EEKfy9J4xHquASgmq-fWRadMBQgVGWpCJQjQ_YLa71Df3lBylyn3oYHjBTOam04zTxwdDuRTkkg6d9IFo5Jne1pu37tcgZd5iBFmpgH9sEkECVSbPb3VCUbKbEFvSeIMmdht9bfV8c4Vy38Au3GPIR6edtf6-tJmYA1LpCP1mPtD_OmT8TUx9RpWeVqpifOVThWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری؛ با پرداخت 20 میلیارد، رضایت نامه مهدی تارتار برای پرسپولیس صادر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/135011" target="_blank">📅 13:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135010">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rl7P8r9Io9dRZCy3ISaYvf5E22sj0sDxgY_jMSWBn34QgUK-87gYxvzdlcDtFh-tDMTJpc6W_B9-ohfgtTp8OpKYJ420sGfiAsnikp0580NTbRqdEFJ2YbArpcRNv9DEElkdjq_G4CCv4XxLyS2rUoFprbt01IPt7p_ghaebKBNqLvTZENB1gjNuJenx6iAEvMG6wXf28THOzLxo6bHJxJgGTfIkP1KxA5ONGKbDfxcTW9NR6vcCB2h--Ak1zMKr3nXZp25zcuID_7DOX782bGpqKqf1IAk9BzsNtyrhizWYuPA99CZOTeM1NoFifzONp_BtIYmJCBA8tAT5NQWBiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جام جهانی جای عجیبیه!
🔴
🔴
توی یک شب میتونی راه ۱۰۰ساله رو طی کنی و این معمولا برای دروازه بان ها میوفته
🔴
🔴
مثلا همین ووزینیا دروازه‌بان ۴۰ساله کیپ ورد که تا ۲۵سالگی زباله بازیافتی جمع آوری میکرده اما با یک شب درخشش شگفت انگیز از ۵۰ هزار فالوئر به نزدیک ۱۵میلیون…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/135010" target="_blank">📅 13:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135009">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❗️
#فوری
؛ یورگن کلوپ سرمربی سابق لیورپول با عقد قرار دادی 4 ساله سرمربی تیم ملی آلمان شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/135009" target="_blank">📅 13:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135008">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/135008" target="_blank">📅 13:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135006">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135006" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/135006" target="_blank">📅 13:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135005">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
🆕
معرفی سایت و اپلیکیشن مل‌بت
🆓
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/135005" target="_blank">📅 13:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135004">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
🔴
🔴
🔴
سرانجام تارتار به آرزوش رسید
🚨
ازش حمایت میکنین؟
👍
👎
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/135004" target="_blank">📅 13:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135003">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1xAXeUKTqiMGvHsnnMHPE4q9RVa86PiycKo_Cjlq_AKRgFeGDrLJMnqiVsxidTyFNt9u1bO5ZmcKGGjP_hjD68qOs22-jwGzeuUYo4YIqNAJBcmf7MeW_6hFIEMuBWeoq-f66Wt0IcrRyW9C8uYrrS8QM5QspQxaa6JxLcJLP_1JK6I8amaCp9I2hA8sxZAfMKrGPkx0IrquH82wy9YMquiRk1EGJkAmVX8B7ZWGQhpSmmrJl1s5wspXFNl7kzfljjC4gB4fMxQCJxECT6qf5Cq2z2YvLUdGwJBG_gfWrOHVceEr24WC122v-0buljOHoZa85oVyy4FYiuK5U-0sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔴
🔴
🔴
سرانجام تارتار به آرزوش رسید
🚨
ازش حمایت میکنین؟
👍
👎
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/135003" target="_blank">📅 13:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135002">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
باشگاه گل‌گهر سیرجان ساعتی پیش رضایت‌نامه مهدی تارتار را برای باشگاه پرسپولیس صادر کرد تا او سرمربی جدید سرخپوشان شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/135002" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135001">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
جلسه با تارتار در یوسف‌آباد و خارج از ساختمان باشگاه برگزار شد!
🔴
یک قدم تا مربیگری مهدی تارتار در پرسپولیس.
🔴
جلسه تارتار با فردی برگزار شد که شخصا اسکوچیچ رو در ترکیه هوا کرد.
✍
سپهرخرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/135001" target="_blank">📅 13:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135000">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgv05UZxKqI7kIxBY7aJ-pWQlXnTU6RFYGE8bvmJSXgXDIM0AfGaNjq5SVOtQywlDKsV29HHXH8HddG7wTZNOKFZaPfsDCkKkGsDBxZh5l4sDsk9ZCdVvEfSUQVfgPIQUf6U2zrozw1oo00EzX_eZ8jc1XnHvpRvHwlY7jSms2d6XZKxtNYx01PDBzpvulskRBIsk5vm2HamBumCoUBD4vpcjamaY8HXEdeTs5Gpx_Hy2aiOR5tE-V-StaKquKEgcJIQ3wS0EaZVoVyRI1ejs3GAYCWHpn6GgyU5LlnSA1sALDqhWZ462Ml-_d3faItC8BwIiTfQYrF_eD1AbhBghQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جلسه با تارتار در یوسف‌آباد و خارج از ساختمان باشگاه برگزار شد!
🔴
یک قدم تا مربیگری مهدی تارتار در پرسپولیس.
🔴
جلسه تارتار با فردی برگزار شد که شخصا اسکوچیچ رو در ترکیه هوا کرد.
✍
سپهرخرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/135000" target="_blank">📅 12:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134999">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
#تسنیم‌‌‌؛ مهدی تارتار در آستانه امضای قرارداد با پرسپولیس.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/134999" target="_blank">📅 12:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134998">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
#تسنیم‌‌‌؛ مهدی تارتار در آستانه امضای قرارداد با پرسپولیس.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/134998" target="_blank">📅 11:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134997">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
✅
باشگاه الشمال قطر با ارسال ایمیلی به پرسپولیس خواستار جذب اورونوف شد. این تیم اعلام کرد که حاضره 3.5 میلیون دلار برای‌ جذب اورونوف به‌ پرسپولیس پرداخت کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/134997" target="_blank">📅 11:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134996">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAZ-MvfVYnM4bPWV-l_bl8azoPfRUo8FkfhKBPbJoXF54ikx505YGV6MZxLE6G7DkL7jcpvOk0y6HNa3tYnYhDqI6hbiJKKryqoWKSTSpRfJi1A2ZzJAFXas_CctinQEPCAsUvKn6-ndrpn5N51RDqBUXde1IR8M_MHdUOkTgOQCoIpJdKm2zveOMvzJjqOf6IVjpVL4kZSlqpCgSJI5_V-ARdpw3hAbLkXl2ug2U_0_Ctjvcu13cMrkHYvNOnWMjZyCVeIykZnu0-f0bILMEDyrvzbED8luMsv1amz_eaL31SZLQfbd6jLUCN0HO9evMOMSHFaKCeg-1kwHdWbS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
بانک شهر از این موضوع اطلاع داره که اگه این فصل مثل سال گذشته رتبه پرسپولیس جزو چهار تیم برتر جدول نباشه قراردادش به عنوان مالک با سازمان خصوصی سازی فسخ میشه!؟
❗️
حالا برید دنبال انتخاب مربی ضعیف ایرانی و نقل و انتقالات ضعیف تر….!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/134996" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134995">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
❌
قرمز آنلاین ؛ اگر تصمیم مدیریت و هیات مدیره به سمت مجتبی حسینی تغییر نکند تارتار سرمربی سرخ ها خواهد شد .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/134995" target="_blank">📅 11:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134994">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❗️
❗️
#فووووووووری از قدوسی
🔴
تا ظهر سرمربی پرسپولیس مشخص میشه که احتمال خیلی زیاد آقای تارتار خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/134994" target="_blank">📅 10:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134993">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
❗️
#فووووووووری از قدوسی
🔴
تا ظهر سرمربی پرسپولیس مشخص میشه که احتمال خیلی زیاد آقای تارتار خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/134993" target="_blank">📅 10:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134992">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✅
پاسخ یک مدیر ارشد باشگاه پرسپولیس به سوال قرمزانلاین : فردا به احتمال فراوان سرمربی معرفی می شود
❗️
این مقام مسوول ساعت ۱۲ و نیم بامداد به سوال ما پاسخ داد و به نظر می رسد منظورش از فردا همان دوشنبه باشد//قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/134992" target="_blank">📅 10:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134991">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
❗️
خبرورزشی: حدادی روز اخر مذاکره با اسکوچیچ که همزمان بود با روز عقد قرارداد دو تا بند به قرارداد اضافه کرد که اسکوچیچ مخالفت کرد و همه چیز کنسل شد
🔴
1_ اگه جنگ شد تا روزی که ایرانه پول بگیره
⏺
2– 500 هزار دلار از مبلغ توافق شده کم کنه
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/134991" target="_blank">📅 10:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134990">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
۳ گزینه نهایی باشگاه پرسپولیس برای هدایت این تیم مشخص شدند:
⏺
مهدی تارتار
⏺
مجتبی حسینی
⏺
حمید مطهری
❌
شانس تارتار و حسینی تقریباً برابر بوده و شانس حمید مطهری کمتر از این دو نفر می‌باشد…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/134990" target="_blank">📅 09:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134989">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
دیگه همه گزینه شدن باید ببینیم کی مربی پرسپولیس میشه ....
❌
مازیار
❌
یحیی
❌
تارتار
❌
مطهری
❗️
مجتبی حسینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/134989" target="_blank">📅 09:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134988">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkjhUEjykbZfmdaTQuSlgYcHRB8th5i3-SAL_8jb36uUKBfWt5qxt6CEKHiCU_0Xt3hExqiOh7KA3OqfcxNM-4mw0J76YgyWJlOBFjDs4a01OZwQw4NFloLx2ogvUNogaOWRw3Ltrj4l3URzxkmmVpGeLNvYKvUXIFBsUtBXHs-AqqQT-JU1o-UcfWNhdqVCmWrDjdU0yfESWSEZjxzG-WkqoclIO8pI-mgLVOqOG6Wc4MLhNqFjqNq0k-Ut4r05dA_3hfqn7Uc-cznkI1RyENOcY0qombt4_h4vzBWS4oCMgwucrh-1rviWNHYGeAeOODQs7pvnMQ1S9RknZOaYug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/134988" target="_blank">📅 09:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134987">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/134987" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه ها تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بد نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://t.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/134987" target="_blank">📅 01:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134986">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfHDbYUzDCnx4DWvMNJcKsZQPhuPuAa6mqfEz79g67jVPrOMppT0p4XONYY6i-pvTDs1AZgwNah3NL-wQ9JlmL3rGj6BAqbjTNgbKv-b_QH8aun24im_b2MYaDr_zFOAOKvsP4mg8m9tpHQ3zGzUiAlAG0KeAYTP0JNn2Sha62Q8BtrsVDOfec4ZBXopyDEQPTa67ECJNpkVJjleALOYyGshqT9kroxLKfs8A2crfoR2crk64FtpwccFfWNsKLdbvptmcIAff9WH86d2cTcUuxYhAvxPPtpivrZihEr1l4j5K81rNwg5zO6TwdPa9AqL-wy-2GROih2n189ZjAO_3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《 لینک سایت برای کاربران ایرانی》
👍
《 دانلود اپلیکیشن اندروید》
❤️
https://t.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
Ⓜ️
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/134986" target="_blank">📅 01:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134985">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tS_Hl3I35DBo9qCp2sbAXXIDPdH59UZWkMCaUKE3YQXnK3ECossufGLyrQ_oxS_ot1u2iDjpN19ed5kE0LaIXbeUk0WYFCfDI1xWUANDdGxeH4ULu_nd-ZohrhtXdhw0vpaDFKOvush5YnhQlj0WrEbDRCb9hJ8BEifG4ncKSnJHCQ-9WQ7r9AAAKgX8EzCjisa3PSXNEh49WlDW3PnHcLluBgc6LozL55MC1Hl_63_XCzdZm5JbvGeHbZvUWtM2FYbgU1BGgfFq2BQSquBt2QoiR7aFbqPu6vLnXwAHNnW6c6c3HCPrbR_iXu6nGa5vasRRguZpkxLhaq3mUfppfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
یحیی گلمحمدی با حضور در تمرینات دهوک عراق به شایعات حضورش در پرسپولیس پایان داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/134985" target="_blank">📅 01:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134984">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
✅
باشگاه پرسپولیس از ساعاتی پیش دوباره باب مذاکرات با اسکوچیچ را آغاز کرده است و کریم باقری مسئول راضی کردن اسکوچیچ برای برگشت به میز مذاکره است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/134984" target="_blank">📅 01:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134983">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
🔴
خداداد عزیزی: آقا کریم ترسو نیست ولی دوست ندارد اینجوری سرمربیگری را تجربه کند. آن هم باشگاه بزرگی مثل پرسپولیس. شاید او شرایط را مهیا نمی‌بیند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/134983" target="_blank">📅 00:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134982">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❗️
❗️
کریم باقری آخرین راه ارتباطی باشگاه با اسکوچیچ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/134982" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134981">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
✅
شنیده ها :
🚨
انگار حدادی دریبلش خیلی رونالدینیویی بوده و دوباره رو میز مذاکره با اسکوچیچ نشسته است.//قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/134981" target="_blank">📅 00:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134980">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فوری | حمید ابراهیمی:
🚨
مهدی مهدوی‌کیا سوپرایز بزرگ باشگاه پرسپولیس برای نیمکت سرمربیگری است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/134980" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134979">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فوری | حمید ابراهیمی:
🚨
مهدی مهدوی‌کیا سوپرایز بزرگ باشگاه پرسپولیس برای نیمکت سرمربیگری است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/134979" target="_blank">📅 00:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134978">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⚠️
هوادار باید فشار بیاره کنسل بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/134978" target="_blank">📅 00:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134977">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⚠️
هوادار باید فشار بیاره کنسل بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/134977" target="_blank">📅 23:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134976">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
شنیده ها : محسن خلیلی دیروز با مهدی تارتار جلسه داشته و این مربی اعلام کرده در قرارداد جدیدش با گل گهر بند فسخی داره که میتونه به پرسپولیس بیاد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/134976" target="_blank">📅 23:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134975">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافقات با مهدی تارتار انجام شده است و باید تارتار رو رسمأ سرمربی بعدی پرسپولیس بدونیم!
📚
مهدی تارتار یک دستیار اسپانیایی انتخاب کرده و با خودش به پرسپولیس میاره؛…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/134975" target="_blank">📅 23:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134974">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافقات با مهدی تارتار انجام شده است و باید تارتار رو رسمأ سرمربی بعدی پرسپولیس بدونیم!
📚
مهدی تارتار یک دستیار اسپانیایی انتخاب کرده و با خودش به پرسپولیس میاره؛…</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/134974" target="_blank">📅 23:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134972">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافقات با مهدی تارتار انجام شده است و باید تارتار رو رسمأ سرمربی بعدی پرسپولیس بدونیم!
📚
مهدی تارتار یک دستیار اسپانیایی انتخاب کرده و با خودش به پرسپولیس میاره؛ همچنین فردا جلسه آخر بین پیمان حدادی و مهدی تارتار برگزار خواهد شد،که «شاید» منجر به رونمایی شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/134972" target="_blank">📅 23:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134970">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/134970" target="_blank">📅 23:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134969">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
همه دوست داشتیم اسکوچیچ بیاد ...ولی با شرایطی که گذاشته بود .مبلغی که میخواست بگیره .کار و سخت کرده بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/134969" target="_blank">📅 22:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134968">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
پیشکسوتان پرسپولیس! همچنان علاقمند هستند مهدی تارتار سرمربی پرسپولیس شود و به دنبال فشار آوردن به هیات مدیره باشگاه برای انتخاب او هستند!
🔴
🔴
مهدی تارتار حمایت های علی پروین، خودش رو تبدیل به گزینه اول سرمربیگری پرسپولیس کرده!
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/134968" target="_blank">📅 22:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134967">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فووووری از قدوسی: مهدی تارتار به احتمال زیاد تا ۴۸ ساعت آینده بعنوان سرمربی پرسپولیس انتخاب خواهد شد
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/134967" target="_blank">📅 21:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134966">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/134966" target="_blank">📅 21:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134965">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
مارکو باکیچ: دوست دارم وحید هاشمیان به ‌پرسپولیس برگردد
😕
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/134965" target="_blank">📅 21:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134964">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❗️
دیگه چاره ای نیست باید حمایت کنیم ..دیگه باید بپزیریم .شرایط مملکت جنگیه و هر لحظه احتمال جنگ هست ..خارجی نمیاد ..اگه هم بیاد ..جنگ بشه سریع فرار کرده و کل پولش و گرفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/134964" target="_blank">📅 21:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134963">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">https://t.me/+Bt80HN28Ils5YWE0
همه فرما رایگانه رفقا
✅
✅
⭕️
فرمهای امروز از بازیهای جام جهانی رو از دست ندین
#VIPرایگان</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/134963" target="_blank">📅 21:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134962">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/al0q9ypk3HDgE7c1urq8-T7z8gyTF5-OfN3pPIFS2Z43NqM_8umCMXcZCO0B8kwvFzIEImDDExGXk5OosQ-uVaxg0HAvCRyWttbwWvbzFqrxvR8O9nMeG3hL_UTVVPd-0icQcxssu0V6aA1s7Mub4i8EvZBAiz0HsMoy3UEoUTpeCdOQN9hL9fYDItlQ0RuHco7NqFqqz0TvMBTS05_hOkn98ftCoeBo4Mx3BKf6hl03lKPUvvQe_9odWGF3rTZfHleE288djx5A20flIf-19qVkM1h4MBS_iOyA23z5PnEkKzGjtbRNk9kKscJGVdsSYhmY47deQ-TyCvn66yRwHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دوستان بت زن این کانال مخصوص شماست
بهترین آنالیز ها و آموزش ها
🆓
📈
اشتراک سایت های معروف خریداری میشه و براتون رایگان قرار میدن
💥
🥇
آموزش های جذاب و سود ده در مورد شرطبندی فوتبال
💡
چالش و قرعه کشی ها با جوایز دلاری
💵
✔️
⬇️
⬇️
روی لینک کلیک کنید
⬇️
⬇️
https://t.me/+Bt80HN28Ils5YWE0
https://t.me/+Bt80HN28Ils5YWE0
🏆
فرم از بازی امروز
🇫🇷
فرانسه و پاراگوئه
🇵🇾
با ضریب 3.50 گذاشته شد</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/134962" target="_blank">📅 21:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134961">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
✅
حاج مهدی تارتار بلاخره به آرزویش رسید ..امیدوارم صدش و بزاره و قدر این محبت خدارو بدونه ....
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/134961" target="_blank">📅 21:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134960">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فووووری از قدوسی: مهدی تارتار به احتمال زیاد تا ۴۸ ساعت آینده بعنوان سرمربی پرسپولیس انتخاب خواهد شد
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/134960" target="_blank">📅 21:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134959">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jc71vZ-N1PrmdefQkXcVWz37yvFnBPBrO6uOiCmPzoGfS0mxSOF61wEaNBvEV9MRpFjV2OIYjd5q6XNXEDnX2zjJF0racI4H02pX98IO6mXyHm0Ln3uG1jr-20jhJfo-S84XoSQS_WU5oKyyIKkNn8jhp__ANtEBIzcc6LE9N_uozRcrWh889f3vy9jFKV65RYtxUx-qgK7a6wLHWti2g9cxCKdl2pt36ynLvK0_3VEtXeh_GGuFKwaDHLQfOGFmWaze8dz9fKCIdyCkJPnEsDq7cieQfZ6BZeoxHe_aLRtV4dgVWAZ1cS7NbfqNG7byBwi8DoU8KrdK-YvmhCbnaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فووووری از قدوسی: مهدی تارتار به احتمال زیاد تا ۴۸ ساعت آینده بعنوان سرمربی پرسپولیس انتخاب خواهد شد
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/134959" target="_blank">📅 21:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134958">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/134958" target="_blank">📅 21:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134957">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❗️
دیگه همه گزینه شدن باید ببینیم کی مربی پرسپولیس میشه ....
❌
مازیار
❌
یحیی
❌
تارتار
❌
مطهری
❗️
مجتبی حسینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/134957" target="_blank">📅 21:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134956">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
سرمربی جدید و ایرانی پرسپولیس فردا نهایتا پس فردا مشخص خواهد شد/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/134956" target="_blank">📅 21:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134955">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❗️
دیگه همه گزینه شدن باید ببینیم کی مربی پرسپولیس میشه ....
❌
مازیار
❌
یحیی
❌
تارتار
❌
مطهری
❗️
مجتبی حسینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/134955" target="_blank">📅 21:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134954">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
✅
باشگاه الشمال قطر با ارسال ایمیلی به پرسپولیس خواستار جذب اورونوف شد. این تیم اعلام کرد که حاضره 3.5 میلیون دلار برای‌ جذب اورونوف به‌ پرسپولیس پرداخت کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/134954" target="_blank">📅 21:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134953">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
⚽️
❤️
عبور اوستون ارونوف از آلن ویتل
🔴
اوستون ارونوف با گلی که به سپاهان زد، با پیراهن پرسپولیس ۱۵ گله شد و به این ترتیب از رکورد ۱۴ گل آلن ویتل گذشت.
🔴
ملی پوش ازبکستانی پرسپولیس حالا در جدول گلزنان خارجی پرسپولیس در رتبه دوم قرار دارد.
🔴
همچنین سرگیف، هم‌وطن…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/134953" target="_blank">📅 21:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134952">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
ترامپ به آکسیوس: همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/134952" target="_blank">📅 20:54 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
