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
<img src="https://cdn4.telesco.pe/file/KdGPv1H3ReLCsOQt92ZxD9C9ciUYy-NW14i35gLm8gN40B4B2sF3FC2wAKhWnjJlX4f7NT31THFz8x-gIQWOaRUKCt3ef4067Gd37N7EX2yehVG8rBntc9a0jLGFGKvvTrol0QKqYJFJvKHw8EdudMxKYHxbnhQx1UjHNNRswGHfxpuCC1eGN5uDMQIHHjv9hpLJQzbVm34wZC-R5Dm1eGiFngi7GVrmYXGkrpzjr3uaAluNzjLKicpjJR98P0qKaKOXTnO9_UM1zF_2-3wnDpSp5Ej4CM9Q9ef6YOhh5GtENKDh4krifxj_IQC6LUHbfxYWxcHI3KZarfpGLVC7og.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 17:00:45</div>
<hr>

<div class="tg-post" id="msg-135192">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❗️
❗️
ابوالفضل جلالی با پرسپولیس به توافق نهایی رسیده و فقط یک امضا تا پرسپولیسی شدن ابوافضل جلالی باقی مونده.
🔴
سپهر خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 579 · <a href="https://t.me/SorkhTimes/135192" target="_blank">📅 16:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135191">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❗️
❗️
ابوالفضل جلالی با پرسپولیس به توافق نهایی رسیده و فقط یک امضا تا پرسپولیسی شدن ابوافضل جلالی باقی مونده.
🔴
سپهر خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/SorkhTimes/135191" target="_blank">📅 16:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135190">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❗️
❗️
واکنش مدیرعامل نساجی به خبر پرسپولیسی شدن دانیال ایری: «ما چهارشنبه جلسه‌ای را مدیران پرسپولیس برگزار می‌کنیم اما با توجه به اینکه سیاست اصلی نساجی موفقیت در لیگ برتر است، ترجیح بر این داده می‌شود که رضایتنامه ایری صادر نشود و او در تیم باقی بماند.»
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SorkhTimes/135190" target="_blank">📅 16:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135189">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
✅
ابوالفضل جلالی و میلاد محمدی سمت چپ
❗️
مهدی تیکدری و مجید عیدی سمت راست
✔️
پ.ن دو چپ و راست خوب داریم
🙂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SorkhTimes/135189" target="_blank">📅 16:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135188">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
فوری؛ باشگاه پرسپولیس پس از کنسل شدن جذب ابوالفضل رزاق پور، با ابوالفضل جلالی، مدافع چپ استقلال به توافق رسید و او سرخپوش خواهد شد. /تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SorkhTimes/135188" target="_blank">📅 16:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135187">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
نظر شخصی :به نظر میاد تیم خوبی داره بسته میشه ..و بازیکنان توانمندی دارن جذب میشم ..اعم از جووون و با تجربه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SorkhTimes/135187" target="_blank">📅 16:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135186">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
فووووووووووری از فوتبال 360
🔴
لیست خرید تارتار برای پرسپولیس
🔴
مجید عیدی
🔴
مسعود محبی
🔴
علی نعمتی
🔴
دانیال ایری / محمد مهدی زارع
🔴
پویا پورعلی
🔴
کسری طاهری
🔴
پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SorkhTimes/135186" target="_blank">📅 16:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135185">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
✅
تسنیم: ابوالفضل جلالی با پرسپولیس به توافق نهایی رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/135185" target="_blank">📅 15:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135184">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
تسنیم : میلاد محمدی و پرسپولیس برای تمدید قرارداد به مدت ۲ سال به توافق رسیدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SorkhTimes/135184" target="_blank">📅 15:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135183">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
✅
تسنیم: ابوالفضل جلالی با پرسپولیس به توافق نهایی رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SorkhTimes/135183" target="_blank">📅 15:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135182">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔸
شنیده ها :
🔸
امیرهوشنگ‌سعادتی ایجنت ابوالفضل جلالی با باشگاه پرسپولیس مذاکرات‌مثبتی داشته و احتمال اینکه ابوالفضل‌جلالی‌مدافع چپ 28 ساله استقلال با عقد قراردادی سه ساله به پرسپولیس بپیونده زیاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/135182" target="_blank">📅 15:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135181">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
👀
ابوالفضل جلالی نام استقلال و از بیوش حذف کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SorkhTimes/135181" target="_blank">📅 15:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135180">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6Qs0xn_SQo-vKNp6oj7ScayrtnPDtpQ0qkYolP-ZWj9mOHsHjVQ7ktW7h1JUCG80hA2j-TwbT5I9yc8JiIvumonHntRW_Wx8OM9zP4K5mBELSX_ttGwcIf6XK9Tcr0MnpQSmvYD0v5S3q4LTrjSF6vBjgRKD1dsvEErEL9C3l1tLPlLdHQxQWBTyNLeVCo6vR1ux-N4RObSvkgfv-ralgHA6BiLLYPiuDrnM5TnLk1PbPmFhFl87RBAuANc5W3WmfqF-F72whgUqlhxcvAmTDh_xSJ6XYEda0NoqQbgYS1e8lpJCo3bqP0bQ3IK11wgK8e2WnqYkgmKEZxbvlBmuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فورییییی به نقل از CBS :
🔴
علیرضا فغانی قضاوت فینال جام جهانی 2026 برعهده خواهد داشت !
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/135180" target="_blank">📅 15:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135179">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7L2jxZmVdBoX-EVXakDKfM7amsF9u3Vz1nryLIeXr-WX5_q6YAB_BXcPCMgDm_MuV73a6NsimUfCN8oPluGA1HU1S-X9beMzyjwptH4uuJ6a2W6VxgO9ubtZUUA2wu_f94RRQruIwQn5fSSmKHdmPBjioaukcurTPrORxxHGKwEiHiUZmJXjoMUjjBE8BRhJpUfdEvD87MG2bQPe246ZeaSLvEJTx9MNOf8encQHB6_KMolIC8oC1poIQ3WIu6hXinSLfg6TJujV7sESlj4xyjJlGEwDRoGy1bzOQxm9CUOrbqviZixZwRNlEHcACthchSJEJXSbqpCqDdEFGHapA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بخش‌رسانه‌ای‌باشگاه پرسپولیس طی ساعات آینده پوستر رونمایی‌از کسری‌طاهری خرید جدید این باشگاه را منتشر میکنه. قرارداد طاهری با پرسپولیس قرصی با بند خرید 1.2 میلیون دلاری خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/135179" target="_blank">📅 15:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135178">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUyvwOxeEn0hgQ6TYfqi4-HhKH6HDi5gl1gjytuOx1i94wZSkYgeSWPbcYRr6YGnnxFt2siycsbl5vRZg9Ysmceq57dkcmLSHTh1Wu-mjbmjdTfh0YtkmjEF7mFgebkjexTw-SRzfwTF1sW4D7AxnDysVVallpgkBrz3C9E906tm86vsPe8Q8QbjScyHoJS6CY3nwbOvcq7j3OCAWofxnjUGFnlghQVFJRacV08Mcfoon6iBlNkWd-5hxf7BkAcOPhu6VQRglFJJkN_1xLINccnQjnNSQ9J9a41Y6G6DnU35CwT0wOq-v_EpW3ORuDHu__Laa2Jbnchy_cmd8pD52w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» مدیران باشگاه پرسپولیس با نظر مهدی تارتار با این چهار بازیکن وارد مذاکره شدند.
⬅️
مجید عیدی
⬅️
محمد قیرشی
⬅️
پوریا پورعلی
⬅️
پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/135178" target="_blank">📅 15:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135177">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
مجید عیدی سی ساله، که در نفت‌مسجد سلیمان و پیکان و گل‌گهر با تارتار کار کرده، رسما با پوشیدن شلوار مشکی و نشستن روی صندلی فلزی، با قراردادی ۲ ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SorkhTimes/135177" target="_blank">📅 15:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135171">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135171" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/135171" target="_blank">📅 15:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135170">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GmI7qmfwgTL6Xkz9WOJO4mzxUuj5bACX5P-ADSrKVpijzog5go9dkHBdFw1GNuhf4BP963Ks2QZkQdaMFPzpC7bkHJp_e9tyL9egMrbkqOreyEwDTWL-owvD9ftucFPK6SACOZr3UMqEKj5RieZuOXG7YA8l6LOr9hM-lLoWWEq3D92kiaN71eXkft9mPtN5PXBAbkyAeWOxyw6Keddg0CF7TSZJuyEaW7vAu144ynk7J4YCnEVqW7wUYVC9SFpWKfGUCnnrPo-mL14G-Vm9UQogM0a5n5OLIZjY1llVc-l4rEalVbY6qRXQz06aHoTjhEs6d3ExwOaNSrbvhz13wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🆕
Link
🔜
MelBet1.net
✅
🆕
Link
🔜
MelBet1.net
✅</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/135170" target="_blank">📅 15:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135169">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❗️
مجیدعیدی
🤝
پرسپولیس=۲ساله
🔴
قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/135169" target="_blank">📅 13:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135168">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
✅
اختصاصی
🔴
رضایت نامه صادر شد؛ کسری طاهری تا ساعتی دیگر جهت عقد قرارداد راهی باشگاه خواهد‌ شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/135168" target="_blank">📅 13:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135167">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
مبین دهقان: بازی در پرسپولیس برای هر بازیکنی جذاب است
❌
هافبک الوحده امارات در مورد اینکه گفته می‌شود باشگاه پرسپولیس با او مذاکره کرده است گفت: بله، باشگاه پرسپولیس با من مذاکره کرده است.
✅
بازی در این تیم برای هر بازیکنی جذاب است، چون پرسپولیس تیم بزرگی…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/135167" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135166">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❗️
❗️
تسنیم؛ گرگعلی نعمتی مبلغ سنگینی رو خواسته و قراره امروز ایجنتش جلسه ای با باشگاه پرسپولیس داشته باشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/135166" target="_blank">📅 13:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135165">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
#تکمیلی؛ به احتمال‌بسیارزیاد مدیریت بانک شهر با علی‌نعمتی و نماینده‌اش به توافق خواهد رسید. مهدی تارتار بجای امین حزباوی که در لیست اوسمار بود خواستار جذب نعمتی شده است.
❗️
پ.ن تارتار به شدت بازی نعمتی و میپسنده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/135165" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135164">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✅
✅
اختصاصی
🔴
رضایت نامه صادر شد؛ کسری طاهری تا ساعتی دیگر جهت عقد قرارداد راهی باشگاه خواهد‌ شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/135164" target="_blank">📅 13:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135163">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
✅
خبرگزاری #تسنیم: دانیال ایری، پوریا شهرآبادی، پوریا پورعلی، کسری طاهری و مجید عیدی پنج بازیکنی هستند که پرسپولیس با آنها به توافق نهایی رسیده و به زودی قرارداد آنها را رسمی میکند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/135163" target="_blank">📅 12:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135162">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
فووووووری از حمید ابراهیمی: محمد قربانی در آستانه پرسپولیسی شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/135162" target="_blank">📅 12:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135161">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🔹
قدوسی: باشگاه با احمد نوراللهی تماس گرفته و ازش خواسته برگرده!!!
🔹
پ.ن احمد نوراللهی در تمرینات پیش فصل اتحاد الکبا شرکت نکرده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/135161" target="_blank">📅 12:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135160">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
پورعلی با استفاده از بند فسخ قراردادش از گل‌گهر جدا می‌شود و به پرسپولیس می‌پیوندد. چون گل‌گهر سهمیه آسیایی نگرفته، این بازیکن حق فسخ داشته و قرار است فردا با حضور در سازمان لیگ قراردادش را فسخ کند تا قراردادش با پرسپولیس را رسمی کند.
🔴
تسنیم
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/135160" target="_blank">📅 12:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135159">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Loyt97WOlodAwmR54is8l5IytVEX8g7bnI7tESLo-uH--tZjsbGVUDwl7VBKzRd2basmBAO2ffRCLQrIQG2067gpkz0z3_urz_bYGmVU3q8JVsjq-zDjMzAutVvFZYA-VaEYI_DxsfG27Nf9qlpnlcYYlbqIkMichNpXw6wHwUHEv-Nrj_E_j4wcA_dF_u-IhW9R331CSUUzEpG0KvFFF3k7mlN1ZSST8yTind9hjpP5myKqpIGf3qICSPBojerqCiYm8GIrOusINjZxgI9S4X3l0pxcTMroS6M2qJANCh-qQtLPmZBwZsxecrhVIzAgFWplwpmP1kwSgO1JDCj8eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
در جام جهانی که تیم های بزرگی مانند برزیل و پرتغال با شکست از آن کنار رفتند؛ تیم تحت هدایت این مرد بدون باخت به کار خود پایان داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/135159" target="_blank">📅 12:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135158">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
شنیده ها: آخرین اخبار در مورد جذب پویا پورعلی:
🔴
بر اساس پی‌گیری های ما، پویا پورعلی هافبک 30 ساله گل گهر سیرجان سال گذشته قراردادی دو ساله با گل گهر امضا کرده ولی این قرارداد مشروط بوده و پورعلی مدعی است قرارداد سال دوم نیازمند توافق طرفین بوده و مانند…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/135158" target="_blank">📅 11:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135157">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇺🇸
🇧🇪
تیم ملی بلژیک توانست با نتیجه 4 بر 1 آمریکا میزبان را شکست دهد و به دور بعد صعود کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/135157" target="_blank">📅 10:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135156">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❗️
فیفا به درخواست ترامپ، کارت قرمزی که مهاجم آمریکا، داخل بازی قبل گرفته بود رو بخشید تا محرومیت بازیکن تو بازی بعد جام جهانی رفع بشه!!
❗️
پ.ن سیاست آوردن تو فوتبال و ترس از آمریکا و ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/135156" target="_blank">📅 10:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135155">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافقات با مهدی تارتار انجام شده است و باید تارتار رو رسمأ سرمربی بعدی پرسپولیس بدونیم!
📚
مهدی تارتار یک دستیار اسپانیایی انتخاب کرده و با خودش به پرسپولیس میاره؛…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/135155" target="_blank">📅 10:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135154">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
محمد قربانی و مدیربرنامه‌اش طی ساعات آتی، احتمالا پای میز مذاکره با پرسپولیس خواهند نشست تا در صورت توافق ابتدایی، این مذاکره را دنبال کرده و شرایط نقل و انتقالاتی تابستانی را داغ‌ و جذاب‌تر کنند./ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/135154" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135153">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✅
✅
باشگاه پرسپولیس از دنیل گرا و بیفوما هم دعوت کرده برای مذاکره جهت فسخ به باشگاه مراجعه کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/135153" target="_blank">📅 10:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135152">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkuCuY_8z63ZSmUJmN2vbA8XrQRt_e5TuHnZtWAXZVzH6UHh-M3a6zP30TTunGLeNJSOGfxy7R_5eWSz9rdna0WlPk6MbIMR9_V5pY1QweGzXVrRO96ciSum5M0BFbmVVuF68y42AlXptjak-okerFP-cZv99AKHJtG71imQgelqkjw0tnLWg9h2PKKQLUqPXO1igYsdkwSfaiqqOl3pTLF_3jAV2LyocCZfUaY-Ne3Xm3Cr2nJ0UyY0QNs6DdwMASVdR0T5PUAt1c5O0QbITZdTzbZfo49U47RMAl02hWP3YeiMhy1zwukorQybYwrbcXCzJXCFMP5mJ83ZrkDfnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نمودار درختی دور یک چهارم؛
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/135152" target="_blank">📅 09:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135151">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
گزارش تلخ و ویرال شده عادل فردوسی پور بعد حذف کریس از جام جهانی
❗️
فردوسی‌پور: خداحافظ اسطوره برای همیشه
😭
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/135151" target="_blank">📅 09:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135150">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
گزارش تلخ و ویرال شده عادل فردوسی پور بعد حذف کریس از جام جهانی
❗️
فردوسی‌پور:
خداحافظ اسطوره برای همیشه
😭
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/135150" target="_blank">📅 09:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135149">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇦🇪
باشگاه الوحده امارات بند تمدید قرارداد خودکار محمد قربانی را فعال کرده اما مشکلی با جدایی این بازیکن ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/135149" target="_blank">📅 09:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135148">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
فووووووووووری از فوتبال 360
🔴
لیست خرید تارتار برای پرسپولیس
🔴
مجید عیدی
🔴
مسعود محبی
🔴
علی نعمتی
🔴
دانیال ایری / محمد مهدی زارع
🔴
پویا پورعلی
🔴
کسری طاهری
🔴
پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/135148" target="_blank">📅 09:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135147">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tc6JxTIRkjHLbteYXeaTuyvSKHO0tSMdyQECDRmUGfKoIYpDF0Bhh8oL7yQMrVp8OM8beY_R6d3ikOzG95y2SzmvV54gdcviVGaVcMm94YdOZb-Z8UOUsuelkNypbnObcoZFZqnoVvxuvrpIM08e1TMaFSZ4V93NMRL4DP8T4nVTsjdgGL7xCKz76ldW11TOR8p75ZOHqlvIUQeDURnt48xetb87_BmoSpIaxvy9aHSLH2ubVIvjKEJeYJF86CVYDbWXBUeGNd56AdnhpkuAgUiS7y-EYeOD4n583MBSoYeFTZ5NUl30sIAwV0cIvU19e3LIESJ9ORDwo7crZyR2uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
کریستیانو: من ناراحتم اما تمام تلاشمو کردم، آخرین جام جهانیم بود و الان با خانوادم باید به آینده‌م نگاه
کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/135147" target="_blank">📅 09:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135146">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135146" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر پنجشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
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
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/135146" target="_blank">📅 02:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135145">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIGH0uuwOCghrwIbqIYvPg6jL7g9UyAaCqFNCZoMFHQ1gqCsc1izXMy7jbFRWrmgx9_6Sbf6l7qSc1R0Gb_a7aLwPNwi2KKOZql77n9nNtaql4D0-v-ziko7p1l7biY9ZdNebHmxmn-xrTV0wiyHFM3l8a2paCmEYaopGCeYL6Ij9yZ1j4scXzBDIxGZKNUC_1CsSjsJcWvvO8PvwelzFW1944ujSxd1LfuFkCxEnEjjyibJguCu0ZSs2xjVO606b1fpv9HS2nWG_OxOxxcODfW5ClFdTquATHDDxg28TkPwngR9SiUJ_piCTcApCg-BcrJj7URGTeAYfu1Q-YKyJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/135145" target="_blank">📅 02:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135144">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
بااعلام‌ایجنت محمدقربانی قرارداد این ستاره 23 ساله به‌مدت‌یک‌فصل‌دیگر با الوحده امارات تمدید شد و این‌بازیکن‌تابستون‌سال بعد بازیکن آزاد خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/135144" target="_blank">📅 01:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135143">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
مطابق اعلام سایت ترانسفر مارکت؛ تا به این لحظه مهدی ترابی و مهدی هاشم نژاد قراردادی برای فصل آینده با باشگاه تراکتور ندارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/135143" target="_blank">📅 01:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135141">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpa_YlCG9kFFuJU19DbftjbCq3cdN57wL5dYylsArOMVt3Nn9-d-HO0ZU3Hf3vyZoecrXrBW2JUqBFhOSBw6G13uZ8-ya9Wd578Aq68c3UxUjuQ-uzwNMWSmi0MmH1ezJJfRIx0xMwBz_8fXP-WurUDoCCRkaQ3DrMTOkDErZZ1J4j4HUcR4DF6q9EvkO6byDlJEuje39-Vl5tUP5kM5BelJvYlci2I6Q6lgxoWkPTu8EQu4rNsXymY8XKZSatUdB4C5-UlnCGj2GK9veCh346al2emEqDAQQWNg_TsgIqAqCUhWuiM_xbaB1AzwICO4Rbt-xtU8L272MTzi23yluA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
لعنت بهت فوتبال نامرد
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/135141" target="_blank">📅 00:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135140">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzrPPezPIBQIKZENcqsmczuyIfrbL3iRaR8Ez-AS5jGYO-lUbLj9h0HHPcTzKCPT65XMYC1Udk9LulCKYgyE9vGydvtfsTdxS91VOR-C4UkUbpJCRq8ddwGciApYQ94w2_mCOwHQ_wyrUOLaqgN5cPE9q_jB6mLEaPie6-X9wg-m5jYvvH6yPvENNku8wyrM0aVy6KgbEp_dH8tT7_jSDn2BFE8A0ODXnOtnAcx988mNdcrjk5BQbjxIHRjIP_YLmBji7Oh5K2BKiAVfCV8eyIgC40tfidkCBzMaJK9SKs5yogCMf4JXRB3-IJ64U-WyNJrCdzcNtbf1m6DYxGPpkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
قاب ماندگار بازی پرتغال - اسپانیا؛ دلجویی یامال از رونالدو پس از سوت پایان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135140" target="_blank">📅 00:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135139">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwYj5TKmiwVTn7DyLUiS7lkPnmp6U8t0h16Cy641HSGqS0mKcRnn40N_hLr-iJwLmeUr-TKwiDueJ85wzjQFlz9BBSODPOApeKPsgj4GbbAJmZ6XPLKku8ox_xZKddGCggYY6UFJf6evt4ipULRJmESOWdGroXFlwJD-PLv_cAX4IG9CVuTxL0kM1ZpCPLgehC3skM8ooYqnR3oMNhTTXJsRu2quvrhUMyvOuAsan6ejk0QyhNAvrsVul8zReETmZFqIqKp2SOQjDSDXcZa-THrNUTekYBNwNFMNl80q3eQr3_gEoq1gme1CUQccCp1T0vRvNHVHSSyd5nhmPDl8bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خودتو کنترل کن اسطوره ما طاقت نداریم بخدا
پ.ن... پس از نیمار؛ امشب هم رونالدو گریه کرد...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/135139" target="_blank">📅 00:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135138">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✅
✅
اوه اوه اوج بازی ..اوج حساسیت ...بازی پرتغال و اسپانیا شروع شد ...تو 360 هم عادل گزارش می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135138" target="_blank">📅 00:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135137">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
بعد انتشار خبر ایرنا، از یکی از مدیران در مورد صحتش پرس و جو کردم که تایید کرد.
🔴
🔴
اما دقایقی بعد گفت من منظورم خبر جذب عیدی بود نه ایری//طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135137" target="_blank">📅 23:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135136">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
❌
کریم باقری:
❗️
من با باشگاه قرارداد دارم. سرمربی محترم هم با من حرف زده و خواسته که با او همکاری کنم. مشکل خاصی برای ادامه دادن ندارم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135136" target="_blank">📅 23:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135135">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
شایعات؛ باشگاه پرسپولیس با هادی حبیبی‌نژاد قرارداد داخلی امضا کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/135135" target="_blank">📅 23:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135134">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
بعد انتشار خبر ایرنا، از یکی از مدیران در مورد صحتش پرس و جو کردم که تایید کرد.
🔴
🔴
اما دقایقی بعد گفت من منظورم خبر جذب عیدی بود نه ایری//طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/135134" target="_blank">📅 22:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135133">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
فوری از ایرنا:
🔴
هایجک مدافع تیم ملی از سپاهان؛ ایری به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135133" target="_blank">📅 22:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135132">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
یاسین سلمانی در ‌پرسپولیس ماندنی شد / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/135132" target="_blank">📅 22:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135131">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
✅
یاسین سلمانی در دوره سرمربیگری اسکوچیچ در تیم ملی در حالی که فقط ۱۹ سال داشت پای ثابت اردوهای تیم ملی بود
❌
حتی توی تراکتور خواهان جذبش شد و اعتقاد خاصی به این بازیکن داره
🔻
آیا یاسین امسال به زیر نظر اسکوچیچ احیا میشه؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135131" target="_blank">📅 22:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135130">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
✅
اوه اوه اوج بازی ..اوج حساسیت ...بازی پرتغال و اسپانیا شروع شد ...تو 360 هم عادل گزارش می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135130" target="_blank">📅 22:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135129">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
برنامه بازی‌های روز نهم مرحله حذفی جام جهانی  پ.ن چه فوتبالیه امشب ساعت ۲۲٫۳۰ ..اسپانیا و پرتغال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/135129" target="_blank">📅 22:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135128">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
❌
فووووووووووری از فوتبال 360
🔴
لیست خرید تارتار برای پرسپولیس
🔴
مجید عیدی
🔴
مسعود محبی
🔴
علی نعمتی
🔴
دانیال ایری / محمد مهدی زارع
🔴
پویا پورعلی
🔴
کسری طاهری
🔴
پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/135128" target="_blank">📅 21:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135127">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jx51o-9HBdmFpAdWljVcEQ_D5RyyJxPOMvQMMcoWSpyhxN44dQcxxtoPwywjC8f2DDUMIttNCiKgTrqn3o4XkJ1F61pG5AOsD9oDpUVHVLX7QO8Hfh81Ll9fYkjay4HmY2unhoAArHwo7BYz0m3HW-7Of13cFjI4HAHYGx-hf4WdSDlE5QEQ1C6pmBccEwSzcj2dM_X5_tQK7o8x8Dbd5zqkvE8I_CeTZwx30ZguAw__ja8j_cF26F1vjXNtzdEOzvS0vldczUGHXZOowjWtWs4dAPKIECH59E_TZpQuhUd63tq2eGPdDyoWZLrAt1iOnWGu6NorNR6_6CDO7IST5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فوری از ایرنا:
🔴
هایجک مدافع تیم ملی از سپاهان؛ ایری به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/135127" target="_blank">📅 21:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135126">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
ورزش سه :تارتار لیست مازادش را به باشگاه تحویل داد
❌
امید عالیشاه
❌
سروش رفیعی
❌
مرتضی پورعلی‌گنجی
❌
میلاد سرلک
✅
✅
مدیران باشگاه این تصمیم را به بازیکنان اطلاع داده‌اند و این چهار نفر اجازه حضور در تمرینات را ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135126" target="_blank">📅 21:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135125">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❗️
اگه اوسمار بمونه فصل بعد وحید امیری به عنوان بازیکن یا مربی تو پرسپولیسه / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/135125" target="_blank">📅 21:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135124">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
کلیپ باشگاه پرسپولیس به بهانه حضور مهدی تارتار در این باشگاه به عنوان سرمربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/135124" target="_blank">📅 21:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135123">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
رفقا این فرمو میتونید سنگین بزنید
🔥
🔥
تخصصی ترین چنل شرطبندی تلگرام
‼️
#VIP
#رایگان</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/135123" target="_blank">📅 21:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135122">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imQ3miE3Bi-L8bwYv5K9NsU8HETeEBGz3x3DqWky-2pqMWb8aY2p8gDaBG0IqfVe7gh8mwNbXgfsjGGq_pzt6yFm0XG770G0G2ZFckKDbxQXiaf2fl9ZPgL2HjQHnOOvNccPYHVP269Dat3baUbamIBjuP15-A-GxzSaBDFxuIapNW8CY-TgUC_tfjFns3vwysIeHf8tNlbKHkCZXQxDwgNBSfIFLJMszAxfVTClsK9cdpYfVr9egaDzC9s0cqoj_dttAJvIzsawPixCVWCJ3MN67kPI_5IJoGhf530krIrR3Zd7m12yy3rJJm7D3XIdNAH11hxPL5kIYdMqrC_-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
فرم VIP از جام جهانی
🏆
🇵🇹
پرتغال
🆚
اسپانیا
🇪🇸
باضریب
⬅️
3.24
📊
گذاشتم
اینجا
حتما استفاده کنید
💎
شروع فرم ساعت
🔢
🔢
⬇️
👇
⬇️
⚽️
برای دریافت کلیک کنید
🤩
💀
رفقااینجا عضو بشین تا شما هم سود کردنو یاد بگیرین
👇
https://t.me/+nA_vmf86vLBjNGU0
◀️
https://t.me/+nA_vmf86vLBjNGU0
◀️
💎
💯
100درصد وینه
💯
💎</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/135122" target="_blank">📅 21:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135121">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✅
✅
سه دستیار تارتار معرفی شدند
🔴
حسین اینانلو به عنوان مربی دروازه‌بان‌های پرسپولیس فعالیت خواهد کرد. اینانلو با ۱۸ سال سابقه مربیگری و دارا بودن مدرک مربیگری A آسیا، یکی از مربیان باتجربه فوتبال ایران به شمار می‌رود.
❗️
وحید فاضلی، که سابقه سرمربیگری نساجی…</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/135121" target="_blank">📅 20:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135120">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
کریم باقری:
❗️
من با باشگاه قرارداد دارم. سرمربی محترم هم با من حرف زده و خواسته که با او همکاری کنم. مشکل خاصی برای ادامه دادن ندارم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135120" target="_blank">📅 20:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135119">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGfzVyoR12pYxmRzr1USfgRY0-hFLrnUCN0NrmOX7cQC1MLNvyD29q_acBpekUaU-HlczKjOskH5YgSiYUltC3-xqimETjekbulyKDrlRE74pHHUOdYrQFjSzI2Esyw25g88eAWTP9OUV4Me6jLTg99cuNtqEb_ky_rArGHK6UN7s5E7_fcR0gOwL4eWCZBnExTKWW5CpDxk44cxatItTskqhS0jl2GHM7L3guQeyvFbmr76tW3oNBpuHPz2Pu11eQVNfnxYDcGFZzt4D5mVBrS-g96axeLTLuEop1FoSU99fnED11jK6O9dLrfgP0QuJ6l00soDl0mcgbSBg-BbGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
کریم باقری:
❗️
من با باشگاه قرارداد دارم. سرمربی محترم هم با من حرف زده و خواسته که با او همکاری کنم. مشکل خاصی برای ادامه دادن ندارم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/135119" target="_blank">📅 20:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135118">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
ورزش سه :تارتار لیست مازادش را به باشگاه تحویل داد
❌
امید عالیشاه
❌
سروش رفیعی
❌
مرتضی پورعلی‌گنجی
❌
میلاد سرلک
✅
✅
مدیران باشگاه این تصمیم را به بازیکنان اطلاع داده‌اند و این چهار نفر اجازه حضور در تمرینات را ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/135118" target="_blank">📅 18:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135117">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
✅
#فووووووووووری
🔴
تارتار علاوه بر پورعلی‌گنجی، برای حسین ابرقویی نیز اعلام عدم نیاز کرده و‌ معتقد است این بازیکن در ضد حملات حریف کند عمل می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/135117" target="_blank">📅 18:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135116">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❗️
ورزش سه :تارتار لیست مازادش را به باشگاه تحویل داد
❌
امید عالیشاه
❌
سروش رفیعی
❌
مرتضی پورعلی‌گنجی
❌
میلاد سرلک
✅
✅
مدیران باشگاه این تصمیم را به بازیکنان اطلاع داده‌اند و این چهار نفر اجازه حضور در تمرینات را ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/135116" target="_blank">📅 18:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135115">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» مدیران باشگاه پرسپولیس با نظر مهدی تارتار با این چهار بازیکن وارد مذاکره شدند.
⬅️
مجید عیدی
⬅️
محمد قیرشی
⬅️
پوریا پورعلی
⬅️
پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/135115" target="_blank">📅 17:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135114">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗️
بعد از منتفی شدن حضور خداداد عزیزی، احتمالاً محسن خلیلی سرپرست تیم برای فصل جدید هست. باشگاه هم می‌خواد یه معاون ورزشی جدید به‌جای خلیلی بیاره
❌
✍️
آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/135114" target="_blank">📅 17:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135113">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
فووووووووووری از فوتبال 360
🔴
لیست خرید تارتار برای پرسپولیس
🔴
مجید عیدی
🔴
مسعود محبی
🔴
علی نعمتی
🔴
دانیال ایری / محمد مهدی زارع
🔴
پویا پورعلی
🔴
کسری طاهری
🔴
پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/135113" target="_blank">📅 17:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135112">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
با اعلام ترانسفر مارکت محمد قربانی بازیکن آزاد اعلام‌ شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/135112" target="_blank">📅 17:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135111">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❗️
ورزش سه :تارتار لیست مازادش را به باشگاه تحویل داد
❌
امید عالیشاه
❌
سروش رفیعی
❌
مرتضی پورعلی‌گنجی
❌
میلاد سرلک
✅
✅
مدیران باشگاه این تصمیم را به بازیکنان اطلاع داده‌اند و این چهار نفر اجازه حضور در تمرینات را ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/135111" target="_blank">📅 16:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135110">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❗️
ورزش سه :تارتار لیست مازادش را به باشگاه تحویل داد
❌
امید عالیشاه
❌
سروش رفیعی
❌
مرتضی پورعلی‌گنجی
❌
میلاد سرلک
✅
✅
مدیران باشگاه این تصمیم را به بازیکنان اطلاع داده‌اند و این چهار نفر اجازه حضور در تمرینات را ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/135110" target="_blank">📅 16:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135109">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❗️
مهدی تارتار: می دانستم حضور من در پرسپولیس دیر و زود دارد اما سوخت و سوز ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/135109" target="_blank">📅 16:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135108">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
مهدی تارتار مخالفتی با حضور کریم باقری در کادرفنی پرسپولیس ندارد، اما وضعیت همکاری باقری با سرخ‌پوشان هنوز مشخص نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/135108" target="_blank">📅 16:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135107">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
🔴
به امید عالیشاه، میلاد سرلک و مرتضی پورعلی‌گنجی اعلام شده در تمرینات حاضر نشوند و در لیست مازاد قرار گرفتند.
🔴
🔴
باشگاه همچنین به سروش رفیعی اطلاع داده قصد تمدید قراردادش را ندارد.
🔴
🔴
تارتار هم گفته هفته آینده درباره ادامه همکاری با بیفوما تصمیم نهایی…</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/135107" target="_blank">📅 15:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135106">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
رونمایی از لیست ورود و خروج مهدی تارتار در پرسپولیس
🔴
🔴
امید عالیشاه، مرتضی پورعلی‌گنجی، میلاد سرلک، تیوی بیفوما و دنیل گرا نفراتی هستند که مدنظر سرمربی جدید پرسپولیس قرار ندارند. سروش رفیعی که قراردادش با پرسپولیس به پایان رسیده نیز جایی در تفکرات تارتار…</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/135106" target="_blank">📅 13:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135105">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/SorkhTimes/135105" target="_blank">📅 13:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135104">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/135104" target="_blank">📅 13:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135103">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
رونمایی از لیست ورود و خروج مهدی تارتار در پرسپولیس
🔴
🔴
امید عالیشاه، مرتضی پورعلی‌گنجی، میلاد سرلک، تیوی بیفوما و دنیل گرا نفراتی هستند که مدنظر سرمربی جدید پرسپولیس قرار ندارند. سروش رفیعی که قراردادش با پرسپولیس به پایان رسیده نیز جایی در تفکرات تارتار…</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/135103" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135102">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
رونمایی از لیست ورود و خروج مهدی تارتار در پرسپولیس
🔴
🔴
امید عالیشاه، مرتضی پورعلی‌گنجی، میلاد سرلک، تیوی بیفوما و دنیل گرا نفراتی هستند که مدنظر سرمربی جدید پرسپولیس قرار ندارند. سروش رفیعی که قراردادش با پرسپولیس به پایان رسیده نیز جایی در تفکرات تارتار…</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/135102" target="_blank">📅 13:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135101">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
🔴
به امید عالیشاه، میلاد سرلک و مرتضی پورعلی‌گنجی اعلام شده در تمرینات حاضر نشوند و در لیست مازاد قرار گرفتند.
🔴
🔴
باشگاه همچنین به سروش رفیعی اطلاع داده قصد تمدید قراردادش را ندارد.
🔴
🔴
تارتار هم گفته هفته آینده درباره ادامه همکاری با بیفوما تصمیم نهایی…</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/135101" target="_blank">📅 12:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135100">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
🔴
خبرگزاری فارس مدعی شده محسن خلیلی میخواد احسان محروقی مهاجم فولاد رو بجای علیپور بیاره پرسپولیس‌
😐
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/135100" target="_blank">📅 12:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135099">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #افشاگری
⚠️
🔴
به گزارش رسانه «سرخ تایمز» محسن خلیلی معاونت ورزشی باشگاه پرسپولیس در ۲۴ ساعت گذشته سخت به تکاپو افتاده و دنبال آوردن یحیی گل محمدی به پرسپولیسه؛تنها شخصی که تو باشگاه خیلی سفت سخت داره تمام زورشو میزنه تا مربی ایرانی بیاد…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135099" target="_blank">📅 12:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135098">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbeSiK1uh1OIzuuAW9_YPi8oNfdF0DifxdFQ884wsdplznJN-rX7EoJK8yi3bBUK6Z8R-BAlfp-aagIPgr26PWv7vknZ8BWyNysdDnPNtbBHSL1-dYNmTBVgp91M3HHQ-YvrDvQtNdLgezLoND21iFVFRTyrSgZpJCEDj0vdCbJSjHswN2KFYSrUEPiZ8pVJcZ2pR_gyLdvJDgcNcrKFM0IWch81bJy_beDaO_4aFFlCIrsFYdkBVRcwZSkQk3itDZX09W_RR3h6pol44Pa-EeEjrg-NAQAlrpZkRq-4v7spKWtkEidLUknJbgV-r-DTP0Avalp91brZWalvYnL9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
برگی از تاریخ‌‌‌‌ ایران...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135098" target="_blank">📅 12:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135097">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
طبق آمار ترانسفرمارکت، تیکدری در دوران فوتبالش در لیگ برتر در پست‌های مختلف به میدان رفته است:
🔴
دفاع راست: 72 بازی
🔴
وینگر راست: 52 بازی
🔴
هافبک راست: 18 بازی
🔴
مهاجم نوک: 15 بازی
🔴
وینگر چپ: 10 بازی
🔴
دفاع چپ: 4 بازی
🔴
هافبک هجومی: 2 بازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/135097" target="_blank">📅 12:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135096">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhwlP6MyB9RMsrTi7Cx1jWcotTk4JFjjoWUddab0snhMHbi1AcqbTAezW5WGWSQTi2Rg9h5WviC1NYrzv_7F5nHoMFoqqNUp5GJS1VWxWQogdVCmHmvkSsBFZL-IjLJTs_QJtSBf2dJXOLYaWnIEwEGyRy2lN6dTjYfyYKjDnfi3KKM1jyVuiLy3J7u6YFE-LjF51BPWz4XB96Za4dWN_81m9KyHvGXyKBTz3PzUwovd6hLd77wE-eX0qrIoPFaPeESm_3TXR9WQ6Ag8hBgEgktlikRc9RMPB_P-MMMl9Kg6nftzV0K-iGAs9YRzQ7A-QUkIZ10VTS7hQ1p1hBvUww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
برنامه بازی‌های روز نهم مرحله حذفی جام جهانی
پ.ن چه فوتبالیه امشب ساعت ۲۲٫۳۰ ..اسپانیا و پرتغال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135096" target="_blank">📅 12:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135095">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
#فارس؛ کریم باقری تمایلی برای حضور در کادرفنی تارتار ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135095" target="_blank">📅 11:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135094">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
✅
سه دستیار تارتار معرفی شدند
🔴
حسین اینانلو به عنوان مربی دروازه‌بان‌های پرسپولیس فعالیت خواهد کرد. اینانلو با ۱۸ سال سابقه مربیگری و دارا بودن مدرک مربیگری A آسیا، یکی از مربیان باتجربه فوتبال ایران به شمار می‌رود.
❗️
وحید فاضلی، که سابقه سرمربیگری نساجی…</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/135094" target="_blank">📅 11:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135093">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
✅
علی نعمتی گفته 48 ساعت وقت میخوام اگه با باشگاه خارجی نبستم، میام پرسپولیس ///خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135093" target="_blank">📅 10:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135092">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
اولین خواسته‌ی کادرفنی جدید تمدید قرارداد کریم خان باقری بوده و گفتن حتما باید بمونه /طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135092" target="_blank">📅 10:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135091">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
خط و نشان مهدی تارتار برای بازیکنان پرسپولیس
🔴
تارتار:در پرسپولیس تغییر داریم چون من بازیکن جنگجو می خواهم، بازیکن باید اول جنگجو باشد بعد فوتبالیست، وگرنه فوتبالیست زیاد است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135091" target="_blank">📅 10:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135090">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇳🇴
نروژی ها بعد از بازی دیشب شادی وایکینگی رفتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/135090" target="_blank">📅 10:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135089">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdbe3de490.mp4?token=b8CHNZAEeHaoOV28vn_leilcPBKtt5QD9HWFOXfGCUhpMAkNpfhKK1PJAvYOrqtrJ8NAEkj99iIWkmQIGHDgWdSwfa5hcpCG9qq-B6Uar8iWIgOIGcpRf52hLg6Joyl5VcmDE2Qdnpfz2ZHTK94h2UDzfd-EnJdr72PiOlfvIx0AIsbSkUUGrtwWPI9YTVbCQV3zRv6IHGG-vjMJDVC0KZUYRyNtFQraySS4zEDNsD-8au_QXm5Hah2F-IpuI7sFO2ESezKSiPtwJDtdnAsPT_9mYuWg3_QtP4ODXcOsOIi3M82ZtPGZB0zR_v9w_GxWHoS5itMj12K2hdD4jYVfu12uoooNS_pN8trvybh3-_83no2CbEd-21lclGDUudUTcujGLCe6xZirhpfORrMmmkisN7f056F_H0PFLykDlUGj7GmcwPfn0EnpILfmpGvSU2c5yT7WWsDv2q28pLTEcBIAdoN15qSEM5bYbeTA6l7i_PbLIRgMucRXA60-_maJG_l1_2JwKYdFcHB0dvLkzBYqP-9vVH-U85PfR21h7-QH5Kg-9VfvbvYmDNgAVqy39ZWdPO4Vv9ppSVY9DDkA1wtATDY5x9UECE7XTm0ylZsk_YdLmZSbzuMAR-XPZVOdIt3Yprrzwg1uhnSW6EtrQ5rV-Zn97X9JqpSgwVj9qHI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdbe3de490.mp4?token=b8CHNZAEeHaoOV28vn_leilcPBKtt5QD9HWFOXfGCUhpMAkNpfhKK1PJAvYOrqtrJ8NAEkj99iIWkmQIGHDgWdSwfa5hcpCG9qq-B6Uar8iWIgOIGcpRf52hLg6Joyl5VcmDE2Qdnpfz2ZHTK94h2UDzfd-EnJdr72PiOlfvIx0AIsbSkUUGrtwWPI9YTVbCQV3zRv6IHGG-vjMJDVC0KZUYRyNtFQraySS4zEDNsD-8au_QXm5Hah2F-IpuI7sFO2ESezKSiPtwJDtdnAsPT_9mYuWg3_QtP4ODXcOsOIi3M82ZtPGZB0zR_v9w_GxWHoS5itMj12K2hdD4jYVfu12uoooNS_pN8trvybh3-_83no2CbEd-21lclGDUudUTcujGLCe6xZirhpfORrMmmkisN7f056F_H0PFLykDlUGj7GmcwPfn0EnpILfmpGvSU2c5yT7WWsDv2q28pLTEcBIAdoN15qSEM5bYbeTA6l7i_PbLIRgMucRXA60-_maJG_l1_2JwKYdFcHB0dvLkzBYqP-9vVH-U85PfR21h7-QH5Kg-9VfvbvYmDNgAVqy39ZWdPO4Vv9ppSVY9DDkA1wtATDY5x9UECE7XTm0ylZsk_YdLmZSbzuMAR-XPZVOdIt3Yprrzwg1uhnSW6EtrQ5rV-Zn97X9JqpSgwVj9qHI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔖
منهای ورزش
🔴
جمعیتی عجیب و غریب در تهران که انتها ندارد؛ تصاویر هوایی از حضور حماسی مردم در مسیر تشییع
پیکر رهبر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/135089" target="_blank">📅 09:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135088">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
پرسپولیس حاضره تا ۲ برابر سقف قراردادش به احمد نوراللهی پیشنهاد بده/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/135088" target="_blank">📅 09:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135087">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-_y-njjVZdjxqmL1bi4IGIYZCkXmEP2UvYKl6NtBPlaIX0UQHTIPPu3D9VTf_P8DA8Eknh_T4nRQqdy53-6qvwCmfuhzehPJp9kbMg1XerTxJ1HVdhPRjlHqAXPWfk_Emf9Q8sr5ussJFmeeiFO6VteEnx6peRLw8RypQ-fgiIJTrib0vngdGg9m0pyemqH5u8io1pyskkeFe4uAx737ja1izztDG_rIQRgRrGYbSVHvNd3P-cxR-Py2oeC_dcisRnI0GsZk9K20zme9l6Ru6gYf_5DTsTG7e1rOgvMnv38a1I1dkSnuPbO2OmrcpiF2cwQ4i8jdFQaxPRjbTuc7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
قلعه نویی اول صبح مهمون داره
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135087" target="_blank">📅 09:46 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
