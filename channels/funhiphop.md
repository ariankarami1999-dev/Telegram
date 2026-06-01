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
<img src="https://cdn4.telesco.pe/file/Jpu_gqbddtMMvReKYupgzpQSUY1RPa1n8OHEOWanyUEkDDb7TtCK9yiQvsrlvjN30xfnLCOKagVVJ0ESog3jdRrzkDBZnNBypRX7PcVBA6939hAGeiiG5ozBkX3JWrK9SYWtvLO7kWXyPxWuUQ-YtYhEZ2sr7xgHLp2y6YYgliPWOcKycfcdp200Me3F5n1Lh6rvQPvkGpBrm_0JEO1zCqY5wDcRtJhD4SWl0RAJGzYjVkka6GZlPO7ts--jUlyXq-bF6SUZNwbI7mlZWtKP0Z7weewdjB02LOhlGQx8UvHPuiM-JV_7Bdb-b5IyeE3lQ7q-fhq8uKFTPQxp6ySgyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 178K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 13:09:42</div>
<hr>

<div class="tg-post" id="msg-76542">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">قالیباف:
محاصره دریایی و تشدید جنایات جنگی در لبنان توسط رژیم نسل کش صهیونیستی، گواه روشنی بر عدم پایبندی آمریکا به آتش بس است.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/funhiphop/76542" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76540">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MpgRLhx3NQNQH-4LyrQP7ApZBLhYjlDRScuOPwPke1fcwWYZabxX2IATQUA-wSwnbb_lmNoDMrn43tlqOJfuwGE7julpaHxtZtdZwfuSofl_YHnj1PGW-e3MgWvsPslZuF_EIWPuM2slDV6r5E5re2PG04vLg1VogQbM-yScJwFT9fzzFW35XK6Op913QRqZHVK8ow8i65tLZn-0HPteAQcUNjeJAMz9k5P5V0JSd47MbeKf17rP__JmfsBNWljVVD8sS7y8VwXM3OgZA0lGcqMP_nBmz13-dDegHcdnIYELuAK4BSM0CYHB-fj2F5ZnSBcF_V3C-qeIC_Ivb66A3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQhi5Qi6EL3xFz1lxgoL7S6vi5zquFFzkYBJK6viclfFhQ0TgMMCQsoKMWgudyaEZLGgjH7cC0yp1fant6WOKXOOPny5H-HnUW8jJMpxlTMmgemp9ZLkgeGfcp2C9hQY80szSJAUaM774yZdmU5GkaDZEdev0_v1BLbZjFmxlbh9ewlDX7gMndBGW1vNFVHfQY3ypcLvWEMl4J92M1CbFhdAiEylQ3lCl01fufz9aB_g4Nas1F2rugdhMy3u3Ensc4KRMIjuCUKo8NKl9pLeOcSK2YsFHQwBTGKFRi3M3mHSdrIw2vi6Ekttpvz5XK5HnDTY7ay9k_2l6UTnZ2fzsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هکرهای سپاه رفتن اکانت اینستاگرام جان اف. بنتیوِنیا، درجه‌دار ارشد ارتش آمریکا رو هک کردن و این عکس رو پست کردن.
پ.ن: یه بار دیگه‌ام زمان اوباما کاخ سفید رو هک کرده بودن و عکس علی رو گذاشته بودن.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/funhiphop/76540" target="_blank">📅 11:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76538">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">من در کاخ سفید داشتم قدم میزدم ناگهان یک ایرانی از 300 متری به من سلام داد پس من تصمیم گرفتم به ایران 2 هفته مهلت بدهم
آنها آدم های فوق العاده باهوشی هستند ولی نباید سلاح هسته ای داشته باشند چون دیوانه اند و به محض تولید آن را به اسرائیل خواهند زد ما الان جذاب ترین کشور دنیا هستیم به پاپ بگویید کسمادرت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/funhiphop/76538" target="_blank">📅 10:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76537">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تهران هم صدای جنگنده میاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/funhiphop/76537" target="_blank">📅 09:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76536">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oypgOH4rDAG92eLrh1JB7GVCWF7XLRt9LRUvfBhLZyCa5Xmd2GHb20f3Z0WY255gNzNfEeFg2SawVzOav6zTwy-TBDpK56OalmDYy4PYoiLixTjl2kbe7vrAltcQfXHTpGpDOb2-WmbqGJhbdOpHXnJP7cwPp1zApVFTH2uic-ptiliSrnEIZfBNiw4RaPktBVqs_RdzRfvr8isXvf7UNHnBSXkpScKKjL3y8tsiz_irMkx1dGnytPd31xsOy8DNm5ZXuubFy1xtNmE38OQ6fCf5bZfLmelLR1Lae6AsUtnvPnWldZY3HIUhwujiMwo3w7LfUJx6bLqd-BQXCmgG7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه: مهرداد محمدی‌نیا و اشکان مالکی رو به جرم آتش زدن مسجد، تخریب اموال عمومی، مسدود کردن خیابان ها و درگیری با مامورین امنیت صبح امروز اعدام شدن.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/76536" target="_blank">📅 09:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76535">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76535" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/funhiphop/76535" target="_blank">📅 09:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76534">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEqbG1ncoFRWXbDFZZ9E0hVsLzSBSCpH3GMUFdmK16AHWtR0W31uh8cqUDa9N0tqDWFoufe-n2XRx7lMBmJxiaQge-v8Ie7IyCrZUj98zyuT4eEeHK7_cNRfYn0WY9Z3FKMozO1YMgzSF5pBYGBKlsmGziiwocuMYM9bZ7YJBGDSB01D_bm4ZkejbF5fMmIUDO2xA7Vgiq8TtMEaHt4zHQ6aPDOc0mjNH-1kb0QH4V2aMhx1MOt7TFmt83ssb5N6CJssCOr0jlNE3Q6qe_njocCNHh1stBOpAqXOr31B87XTN7j-8j2OwPod2mA7B7UPT8sAeR0nVz9BCJ57cUJQIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r11
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/funhiphop/76534" target="_blank">📅 09:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76532">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بندر عباس انفجار
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/funhiphop/76532" target="_blank">📅 09:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76531">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVnHhxTD2aDvAk2pBDs9TOamarqHl7g4RQPdWhT3V4j4wI7USf4DfxozYLIIUo15FROCcQIfu-zCiVDrVa0uib3qdws185FSWtoxzz3ATAlLMMkDNOrk486MgAuyPfQhe-HNRTgFUn6O_E4eTnosMFDwbxQFMzh6-Fb-K9nsZiL_9AA9o8W2vsMdgt9EnPd_6G1xhg5hR6E9TZp8NkQXWLZrxDc3j4S-Ix4prrfKyLcXOLSt-tChqG4GX84oRpwAfAG3b3sxlCjkHteEs8rNvVZvSTyYbIA4plZd-Rt1E-XI8W0zr1ZS12_F74z-1LnLvDLv_1YM3eyw-7zhmRqBMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ خ       :
ایران واقعاً می‌خواهد به توافق برسد، و این توافق برای ایالات متحده و کسانی که با ما هستند، خوب خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهان ظاهراً غیرمیهن‌پرست نمی‌فهمند که انجام درست کار من و مذاکره برایم بسیار سخت‌تر است وقتی که سیاست‌بازان به طور مکرر و با سطحی بی‌سابقه منفی «جیک‌جیک» می‌کنند که باید سریع‌تر حرکت کنم، یا کندتر، یا به جنگ بروم، یا نروم، یا هر چیز دیگری.
فقط بنشینید و آرام باشید، همه چیز در نهایت خوب پیش خواهد رفت - همیشه همینطور بوده است!
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/funhiphop/76531" target="_blank">📅 08:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76530">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وقتتون بخیر، امیدیه هستم و صدای دوتا انفجار شدید ساعت 8:33 اومدش.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/funhiphop/76530" target="_blank">📅 08:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76528">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سپاه:
آمریکا به یه دکل مخابراتی ما تو جزیره سیریک حمله کرد؛
ما هم درجواب، پایگاه هوایی‌ که این حمله از اون انجام شده بود رو مورد هدف قرار دادیم و اهداف موردنظر را منهدم کردیم.
هشدار می‌دیم؛ اگه این حملات دوباره تکرار بشه، پاسخ بعدی  ما بسیار شدیدتر خواهد بود.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/funhiphop/76528" target="_blank">📅 08:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76527">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXWfiYT4PMuF09FvoCqxxQomdsZbkgeuRrAkM-R0_XHZEQxElVO6iK_BXWhc91uMymnNJRr0QHlwBhlIXwHeYzRy5Hv9fePW7i6FVk8_OVv0ujiRThrG0yp_VaFlRJw7cijFr-ML9iK_ncRe3XEY1RnJBFSih8u4thLIe5QzfIqIQXBdO_qBL6wpTvXTiBtiH20yhQUKzEwQiR_3DHDtRzFBfo7dt3vNAAyqQrWvWJ4ln37vJ7ds1GJlNkdGXHWvIOe_ajn4TioZjGKvBlBJM-W8TlABoEqQTbh-kydf8ZTWynPE2TkGuOUAwx-QP5L7yjEkPSL0oKLePOVQjHJDtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تامپا، فلوریدا - فرماندهی مرکزی ایالات متحده (CENTCOM) این آخر هفته حملات دفاع شخصی را علیه رادارهای ایران و سایت‌های فرماندهی و کنترل پهپادها در گوروک، ایران و جزیره قشم انجام داد.
این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی ایران از جمله سرنگونی یک پهپاد MQ-1 آمریکایی که بر فراز آب‌های بین‌المللی در حال فعالیت بود، انجام شد. هواپیماهای جنگنده ایالات متحده به سرعت با از بین بردن پدافند هوایی ایران، یک ایستگاه کنترل زمینی و دو پهپاد تهاجمی یک طرفه که تهدیدهای آشکاری برای کشتی‌های عبوری از آب‌های منطقه‌ای ایجاد می‌کردند، پاسخ دادند.
هیچ یک از نیروهای نظامی آمریکایی آسیبی ندیدند. CENTCOM در پاسخ به تجاوزات بی‌مورد ایران در طول آتش‌بس جاری، به محافظت از دارایی‌ها و منافع ایالات متحده ادامه خواهد داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/funhiphop/76527" target="_blank">📅 08:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76524">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JivsMGHXE0yKFEmwuaoJtlp8VRfGsJdcs9mJv9yeTsZnNUepaJkZz1l7AnjBL8tm7YzMxqi6kSMy4kka4cPTEtUI_bsiufQ3DD4GQ0R0adz2CDoFo6AjA2fKx-Z7_QnByE6gH4jgjQdcG9v-TppeM19wbFOLG3FZgmG11jycM_FLupPN5cZFtrxF0peChPgQZz4X_x6t3kE1UGGHc13W1BirBZof9h7msqtehsQT6qgIq0I_B7gqEc6Yd45a3bnXK2MInfgY7QT9WfUy0qqf4Samof17EAyW2fBpHsEaE7BvOHiVeUhyO9nIGmmF0nXmCE8P-IssoXerdZulUTWufQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر تتلو تو پست جدید یوتوبش برا حضور تو جام جهانی ۲۰۲۶ اعلام آمادگی کرد.
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76524" target="_blank">📅 02:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76522">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مرندی: اگر نتانیاهو در جنوب لبنان متوقف نشود، اقتصاد آمریکا در ماه ژوئن فرو می‌پاشد، زمان در حال تمام شدن است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76522" target="_blank">📅 00:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76518">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">جدی باور کردید یا دارید شوخی میکنید</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/76518" target="_blank">📅 00:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76517">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝕻𝖆𝖗𝖒𝖎𝖉𝖆💤</strong></div>
<div class="tg-text">مشتی کارت اصلا خنده دار نیست واقعا الان من بخاطر تو کل خانواده رو از ذوق بیدار کردم بعد ریدی تو ذوقم؟
زشته کارت اینجا چند نفر واقعا شرمنده شدن جلو خانوادشون بخاطر تو</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/76517" target="_blank">📅 00:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76514">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromarshia</strong></div>
<div class="tg-text">کیرم تو کونت من اقامو بیدار کردم رفت پای تلویژیون دید چیزی نیست یه پسی زد بهم</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/76514" target="_blank">📅 23:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76509">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkZuhn6X0MOObS0IHRRU5wwcP-fRFmuJccRsTUB9ysTE_QfZCRWK0WPZRNyLfDZR9zSOMUdBrsv0AC4fN2VeaQcAGAqvoa-3n_d5r3_2nyl-ZAl4R4FCf8IX-U4m2fHLl-ae84qnEUsKtpEiweOQ7smdD9HAdOB5fJLjTdsD2kjheCOR9duFpXPJZm04h331DsPZbjV0HFTrDxkRJPLwmJUUxv1LNuG1oV49c5wEz1Q0SsBx3AfHfw1An2jxN8yJuqGNm08v_J0coWElXLOn27pZi1UHLHhhYM2c0U46csRvEnDjKNtXeSPSTUSZf1DTLuysZjDEqhd77vK5R7UMvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویویویویویوی  ارتش اسراییل تایید کرد  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/76509" target="_blank">📅 23:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76506">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjpQjLQ-V3mgowwOvaPHzJFfHqE_eC_fcBi5VwyPfHJeQZ8aIz93I0LocmSu_lAsfU6gjnSgyluXYL8751HPWbwdYKlit-1hMa7ilwtunOxt_f51HGT2izd7u6zpQ5aD3rgrQ7lIfkpeJQCSiiuSB0jg-A97BceFGdtb8l11gRz8ZXeVvR3m76wGw8Yg9YmXTlAEaYSSCTnDtQbup-9TyVdbRXYrvrI5x3v-mRrYUJHQe7azV4hswtM_my9lHKMpThG8kckQnT5_CcOcTBFXedjgpDbmTiQmDseW2FHjmiDzjAjZoTdjRsRIe3KuTKW4TeXbJN-v3T27Nk6pdg5BOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویویویویویوی
ارتش اسراییل تایید کرد
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/76506" target="_blank">📅 23:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76504">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تو اندیشه تهران یه خونه مسکونی لوله گازش ترکیده   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/76504" target="_blank">📅 23:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76503">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تو اندیشه تهران یه خونه مسکونی لوله گازش ترکیده   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/76503" target="_blank">📅 23:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76502">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کار اراکی هاست
یک ساعت پیش تو کرج فعالیت جت های جنگنده گزارش شده بود
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/76502" target="_blank">📅 23:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76501">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تو اندیشه تهران یه خونه مسکونی لوله گازش ترکیده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/76501" target="_blank">📅 23:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76500">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">جدی مگه فوتبالو مردم برا سرگرمی نگاه نمیکنن، چرا باید طرفدار تیمی باشی که خوشگل بازی نمیکنه، حالا اصلا هرسال ۱۰ تا جام بگیره
جام باعث میشه تو سرگرم شی؟
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/76500" target="_blank">📅 23:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76499">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYqqjnJCcQE_uwBopW-5uwsKpW5AYngW83tQ8bklRV2KfAeU2s8UAJ89RRySCLkHN7yTEUfcXau81rCFqb1u82xW6H2hAjXClsu2se63x-iwdBJIhN0lhFe149c8-tYl8hnEpTZkEaG1hs0rOIQmV9BUlsJ02HyFfZxaQR1KJ1wDTwOJ_BvuipfSF2D4x1VnDndC2abXMo2qujS7dNRwxwaq4vSjuPjaiE037e5rjeCcgJQ-zLBV7M8ni-ZDJHD7d6yW6yagabrh-1w4G3_bd_8FyyzdQACiTj6ApSTy_YahKRpBwPk7eFPnGTpvoSEC8d9gWGaTg2Qs-u3BsBFdPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرسنال به اولین تیم تاریخ تبدیل شد که طرفداراش بعد از باخت تو فینال لیگ قهرمانان جشن قهرمانی میگیرن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/76499" target="_blank">📅 22:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76498">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پزشکیان :
استعفا از ریاست‌ جمهوری؟ من کارمو با قدرت ادامه میدم و فقط شهادت میتونه متوقفم کنه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76498" target="_blank">📅 22:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76497">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76497" target="_blank">📅 22:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76495">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTn5SSiOPz8mrAoVdPYSNVK-9hl1nj_Ty9yss5yVzbJAmYk-4otLDE8nj_kTfz0aKEx0_w3ejOGnpj7F_46X6YpmNM89QWou6w9yb9deKeBSsxYWpABagcROaiefnWEAiJP4hpv_SXfb5cFqKoL93nffIbMmdM_8bELZJEcc67HChoZDHdnWKiQ3WmizFZ5n63x2-uAn8Z2XPBvcu-pMVNig7a8k2Id4Tou8bnabZaYpp41o2Y4XnYAdRi-Unji1GHhn_ED97l8EXpl9A1H4iWejrfWG8OIJemTV_bxTvkei7Q4QmMG8QAzFmscQmE6600xxMzDeO3YyYAiKASYXNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76495" target="_blank">📅 21:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76494">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">آخه فکور (منیجر پوری) گوز کدوم کونه دارید استوریای دوماه پیششو پوشش میدید، خود پوری هم به کیر کسی نیست دیگه</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76494" target="_blank">📅 21:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76491">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پزشکیان زیر نامه نوشته
من نه استخر میرم نه با هلیکوپتر جایی میرم</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/76491" target="_blank">📅 21:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76490">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ki1Vdo1PJJTbdI-Y3RpH0WzaovPC4d-dYgJ7vG-jPrg8Qu3vxn_JxoXjZzXYkpYDeX-OtToKwpqOqDvJkSIU5cdZA6Jx-vVIXoYviBsk1Rx7h8YbfYZ8Ng4WHwiwBGtHSr6N_vKVdH5J2Amwvk229hC90iWC2bj6W1ia661ejSWlvdqQSKWpoBGqkHWAor8qYebnCBl5FcDW9TusnJ0PgRuMxSnjpMox9TK063DW58aElPE0Di_FCWPc2MjS5OJa7LihuYYRcQR79IW3I-FE3Yk5Df-z81Y2zO4CJw8v8EznB0sd0pdMTCyJOIk2G228a5lXO7INndjcTKneWlrJaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استعفا نامه
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/76490" target="_blank">📅 21:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76489">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فرض کن امشب هم قالیباف هم پزشکیان هم مجتبی ترور بشن
روحانی بیاد روکار هم رهبر هم رییس جمهور
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76489" target="_blank">📅 21:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76488">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تا 1411 با پزشکیان
✌🏻
@FunHiphop | ALI</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76488" target="_blank">📅 21:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76486">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الان مثلا خیلی شفاف باقرشاه داره میره تو کونمون</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76486" target="_blank">📅 21:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76485">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">قبلا پشت پرده یچیو میکردن تو کونمون، الان جلو پرده میکشن پایین میکنن تو</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76485" target="_blank">📅 21:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76483">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خبرگزاری بسیار معتبر تسنیم استعفای پزشکیان رو تکذیب کرد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76483" target="_blank">📅 20:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76482">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">در جریانید اگه مسعود استعفا بده نت قطع میشه و کانفیگ رو میکنم گیگی ۲ میلیون؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76482" target="_blank">📅 20:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76480">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خبر اختصاصی ایران اینترنشنال: مسعود پزشکیان استعفا داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76480" target="_blank">📅 20:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76479">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نمی‌دونن تا گودال ماریانا هم بگردن پیدا نمیکنن رهبرمونو  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76479" target="_blank">📅 20:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76478">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بعید نیست این یه تله تروریستی باشه تا محل رهبر لو بره  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76478" target="_blank">📅 20:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76477">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">@FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76477" target="_blank">📅 20:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76476">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مجاهدین خلق از 021کید به جرم تهدید به شلیک گلوله شکایت کرد
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76476" target="_blank">📅 20:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76475">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خبر اختصاصی ایران اینترنشنال: مسعود پزشکیان استعفا داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76475" target="_blank">📅 20:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76474">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4ePVnEYuYHTsszypqBhHaHphNnHeKemN2SYCSdttDbFO_JYOfo21BcQ4_F-aAngsKuki-eowjJEJNkTY9sFWAzAH0jQvH4PYFSoOin72qTTnGTHpdOz8w9fjwvSKd4XACmcAeIvRGhoqXzDbEZwp1OpVN6agkwT4j8Ed-Lwl0XDVA2WPf3gmv5zcO95Smq9XDScW0EbBw5gUgQ4Xm2YbKqY533rhhjQxhkrIvlj1qqAXX73GyXZsJajSR-QN1_v0K-LaEX5XwLqKu7GDTim0DO6F-FqXZVnnicT_Dg9Vz2AlTN9AvCdfx3JaZDBYO4dHqC6tTwB79IPlC_v1OnJ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر اختصاصی ایران اینترنشنال: مسعود پزشکیان استعفا داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/76474" target="_blank">📅 20:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76473">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مسعودو تو یارکشی فوتبال آخر نفر انتخاب میکردن
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76473" target="_blank">📅 20:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76472">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حاجی دوران پزشکیان یادش بخیر بمولا
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76472" target="_blank">📅 20:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76471">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خبر اختصاصی ایران اینترنشنال:
مسعود پزشکیان استعفا داد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76471" target="_blank">📅 20:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76470">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">برنامه واشقانی توقیف شد
😂
😂
😂
خایمال تیر خورد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76470" target="_blank">📅 20:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76469">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سی ان ان:
ترامپ با آزادسازی هرگونه دارایی ایران در توافق احتمالی مخالفت کرده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76469" target="_blank">📅 19:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76468">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حسن و حسین امیری، دوقلوهای ۲۰ ساله، توسط دادگاه انقلاب تهران به اتهام جاسوسی برای اسرائیل به اعدام محکوم شده‌اند.
آن‌ها پس از بازرسی گوشی‌هایشان در یک ایست بازرسی دستگیر شدند و مشاهده تصاویری از ساختمان‌های آسیب‌دیده مبنای اتهام قرار گرفته است. هر دو در زندان قزلحصار کرج، به صورت جداگانه و بدون حق ملاقات با یکدیگر، نگهداری می‌شوند. نکته قابل توجه اینکه این دو برادر از کودکی در مراکز بهزیستی بزرگ شده‌اند و هیچ خانواده‌ای برای پیگیری پرونده‌شان ندارند.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76468" target="_blank">📅 19:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76467">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMi6DtNbeCo2LOwPKgAZUWFkmS3q_cKRTRcriLK9hYNgBPtC3DXa4rqRiSQOEFEhxWP1GuNrH4smJ8Y6wUN5czPR_4ABbWTA2kX1gwm5gx626LJUyg0ZN0RX3l2J9Ub7eLlWm3GILoyVB0sjlKeVeIAGSxiS071gjKcT6bG9blSTKrWoA8CJiAlHVej4XH8ne5KBB39cXPHs0S7OPmGd8Uf-NuKIxm4woWoHjMZNm6v9uoGe3aw43Mr4mvBtsJ85OozMSky9Vtes2PKV15qAg2gHfOSTaK2IH0Vh6Bsubcw-hIf0cNFdhOU3PXC-2lGEeJBatB-mkr4oYxCnaEuTDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوآ لیپا و کالوم ترنر ازدواج کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76467" target="_blank">📅 19:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76466">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSeniorVpn</strong></div>
<div class="tg-text">😕
بهترین ارائه دهنده فیلترشکن
𝙑2𝙧𝙖𝙮𝙉𝙂
😀
آیپی ثابت ، مناسب ترید و وبگردی  (اینستاگرام - یوتیوب و....)
🛡
مولتی لوکیشن
🇺🇸
🇩🇪
🇨🇭
🇳🇱
✨
سویس آلمان امریکا هلند
✨
😀
| بالاترین سرعت روی تمامی اپراتور ها
☄️
تعرفه سرویس حجمی یک ماهه :
😀
50 گیگ   | سه کاربره         ⇐ 500 تومان
💭
70 گیگ   | سه کاربره         ⇐ 700 تومان
🔄
100 گیگ | چهار کاربره       ⇐ 950 تومان
🥇
150 گیگ | کاربر نامحدود  ⇐ 1,400 تومان
😀
تعرفه سرویس‌های بدون محدودیت زمانی( Lifetime ):
🥶
50 گیگ | کاربر نامحدود  ⇐ 800 تومان
🔵
100 گیگ | کاربر نامحدود  ⇐ 1,400 تومان
💢
💢
ارائه خدمات پنل ویژه همکار انجام می شود.
😀
خرید از طریق پشتیبانی :
✅
@VpnSenior_admin</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76466" target="_blank">📅 18:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76465">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">فایل صوتی وسط بازی عادلو رو فیلم گلدون گذاشتم خارکسه به اونم خورد و غمگین شد ویدیو
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76465" target="_blank">📅 18:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76464">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">شی سی‌د شی وز پرشین استارتد
اسپیکن فارسی و کیرخر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76464" target="_blank">📅 18:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76463">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSgkHhSzj-L4xMR1KgwuICTOfJY32RV5cE_jKbe1QZMhvomxMMcyDkAUtnFhP4yBrU9KihdK-408E2QlionqFzJE6s03Lpp--__EP2i3U--7KhJM_uosxsF3fJYVRgYFHeW8hhvH8I78URiYRxjJFhp99OJrQIusomTO0oSKWwBcpgY7Vkxd0qEHR84DJ2XiJrUxqJ9GIL0uh3kfljiQxrZDFGMXTqyLtHvP9rYFB0KX_OS8_JX4GfspRtoMELZ6DWwTOARVtBpkLzZZHKuACFoXW4We6cMShkqoZcuAbUMCxHFWAQXzg18inDkAk8buBSnzvBbFg3WmKD19mb9XLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف غلامی مادر میثاقی رو کرد تو چرخ گوشت.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76463" target="_blank">📅 18:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76462">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9uQfWiAWD_yrRJUWcV5_K9usYx3OiB5sruYZ08KjDp0lBWNXgJ99H8dvulRwMJV1y4sbGVz2CFFClkgwxElCkIT2mSB9LsNucwCjZHOSq4744gcJQqhBsqvcEe56c_DKrJTMbVWaXF46b5haQamLBerJZpax8i1RAcsaRohootppqqqjmVAEm_n6NqX14Zd4bq1d4SZwA9Z8aRNcxazgAB727r_42gXSDAHYQo2j1Bc-tlm2ujzNExBg5R7fjCLw8_uGH7OTScPGOJUVsJ7urKoayOX7P6nx3LRiSQVcysOmQd3K-uSn27PCPBKkxSWRlBJZTRefd2JrvnJHDQbvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خالق مینیون‌ها فاش کرده که همه مینیون‌های تو انیمیشن مرد هستن، چون نمیتونست تصور کنه زنا اینقد احمق و نادون باشن.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76462" target="_blank">📅 18:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76459">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نیرو انتظامی تهران یه کافه ای که توش اسلیپنات پلی میکردن و پلمپ کرد و گفت: اینا شیطان پرستن.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76459" target="_blank">📅 15:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76458">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نیوزسیتی پرو: با گذشت ده روز از خرداد، همچنان آمار رسمی تورم اردیبهشت 1405 منتشر نشده.  @funhiphop | reza</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76458" target="_blank">📅 15:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76457">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">چیه دوستان
میگم خبر مهم فکر میکنید روبیو بهم پیام داده از پلن های ترامپ گفته؟</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76457" target="_blank">📅 15:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76456">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تلخون از لیبل سابقش جدا شده‌.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76456" target="_blank">📅 15:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76455">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خبر مهم رسید دستم</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76455" target="_blank">📅 15:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76454">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">امین منیجر یه دوتام به پوری بزن بلکه سفید شه برا چهارنفر
@FunHipHop
|  Mmd</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76454" target="_blank">📅 14:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76453">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پیام های شما در چند دقیقه گذشته:
فرید جان سلام من بندرعباسم اینجا صدای انفجار میاد
درود فرید جان ما قشمیم اینجا چند بار صدای انفجار اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76453" target="_blank">📅 14:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76452">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfaIC1EHJLBIj1Sj9XXOyh6BOkMtcoMx6omBVmjUYirVShpGgNlT3M71X0A_uxclxD9PGJVO2NiCtwJ__qnRVWTaeoC-xTkrv8-1FYjPfhr32mVEpJMymxoNEK_Bbrh2Ps9lgrkLLhoPSNpa-rjm_DwKxHoMRMXA_bGDXa7zEu4Uz5M-NWHzHbFtzVyhtGtbmSpxzXckXfWJoGtYOOORuWxqJQ16aLJV0r0lOJoxQNQzISV01p_cWjSJRnSnoHPtMFwd_INn5kyBV4ljqkt9aN3nE3YYbIy91N4cvTG5XKC52nw0jEve79BTk5W1YrWjnWWOIAjdG6S2Qsi3EYrv_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بحث کالچره پسر
عکس خمینی میفته رو ماه
عکس اینا میفته رو گوشت
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76452" target="_blank">📅 14:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76451">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آقای باهنر یجای ثابت وایسید از رو موتور پیاده شید صداتون نمیاد</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76451" target="_blank">📅 14:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76450">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">الان رسایی دوربین رو تنظیم کرده رو صورتش فقط عمامه گذاشته
نه لباس تنشه نه شلوار
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76450" target="_blank">📅 14:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76448">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">امروز مجلس مجازی بود  @funhiphop | reza</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76448" target="_blank">📅 13:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76447">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">امروز مجلس مجازی بود
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76447" target="_blank">📅 13:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76446">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وزارت قطع ارتباطات دست به ماشه هست
ترامپ بگوزه نت رو باز قطع میکنن
کار مهمی دارید انجام بدید این روزا
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76446" target="_blank">📅 13:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76445">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یکم دیگه اعلام نهایی توافق و مذاکره طول بکشه از لبنان فقط اسم "سیب لبنانی" تو میوه فروشی های ایران باقی میمونه.
اسرائیل امروز لبنانو شخم زده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76445" target="_blank">📅 12:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76444">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مردی براي همسرش پیام داد   عزيزم تو چه كرده اي پيش خدا اينقدر عزيزي كه همسری همچون من بتو داده زن جواب داد نه نماز خواندم و نه روزه گرفتم و خدا از من انتقام گرفت:))
😂
😂
😂
😂
😂
😅
@FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76444" target="_blank">📅 12:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76443">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مردی براي همسرش پیام داد
عزيزم تو چه كرده اي پيش خدا اينقدر عزيزي كه همسری همچون من بتو داده
زن جواب داد نه نماز خواندم و نه روزه گرفتم و خدا از من انتقام گرفت:))
😂
😂
😂
😂
😂
😅
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76443" target="_blank">📅 12:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76442">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مطهرنیا:
واشنگتن به دنبال مدیریت ایران در دل یک نظم امنیتی و اقتصادی جدید است برای همین حذف کامل رژیم در دستور کار نیست
میفهمم چی میگیا ولی متوجه نمیشم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76442" target="_blank">📅 11:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76441">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نیوزسیتی پرو: با گذشت ده روز از خرداد، همچنان آمار رسمی تورم اردیبهشت 1405 منتشر نشده.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76441" target="_blank">📅 10:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76440">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خاتمی جلو عادل اصول گراست
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76440" target="_blank">📅 10:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76439">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آکسیوس: ترامپ همچنان به خطوط قرمز خود پایبند است و تاکید داره که هیچ توافقی با ایران امضا نمیشه مگه اینکه ایران تضمین مشخصی برای عدم دستیابی به جنگ افزار هسته ای بده.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76439" target="_blank">📅 10:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76438">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d2dea055.mp4?token=WHjRuIzzfnS-WVRelnQLWlCNg4kurj9d2dxASFJ3SPq_VypbjE5PCYBKYB4dr9Js-3lCDH_KAJjsLuYuw2ftPy2-1R3M8lzUromHwUnN-f5qisJ9SDDuu5ecboQ-NIQ8NlV0hBe56lY0DR1KAEu5D46axeLtezJ6LC9ZqpGYkrvNrJWE2CxIDNDWwly4o8dngWcyA4mjWBLTmtmhVcR7UESZUA6uGuUplwFd2kreIUQOB49RPeyYHpOrk5YxJW-RxNDvfuFs7AgBoEShS1VSzJhxjnfqivciVXbeX2agqQ-4TLxTVN4EpdXeagQpr9dVotluxiCAJrOvtWRpYiLIsamsj2oseqETxxIFn89twIqzCZovpnVkxWjBsHHCHfa7YzTUEQMOtKtU25a35VchxYvHav3UAH4Kjr0O0IpLudNH8kA1_EEhIf7EF9SxYVXY4kjvWpobNflivZjwrxzLB15Sou-mVZNmKgn1evKL6LB4xtKzpED_tp_5Xb8mY3RgkIdtoptJ1ecFFx1g0UT60KjR_QnUfAvxvP052hMbFhKLruz6ZeagptQ2BLoLlFTc3yY4nvXwy8Pr4QV0_v1_DElauLi20YSuocf7ORVWdtyzvl5gbQg_XAL8TnGh2QMS-FT1O4CANMKd3KkhosuLnNgtL4m34Ap2og3bNj_4xEM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d2dea055.mp4?token=WHjRuIzzfnS-WVRelnQLWlCNg4kurj9d2dxASFJ3SPq_VypbjE5PCYBKYB4dr9Js-3lCDH_KAJjsLuYuw2ftPy2-1R3M8lzUromHwUnN-f5qisJ9SDDuu5ecboQ-NIQ8NlV0hBe56lY0DR1KAEu5D46axeLtezJ6LC9ZqpGYkrvNrJWE2CxIDNDWwly4o8dngWcyA4mjWBLTmtmhVcR7UESZUA6uGuUplwFd2kreIUQOB49RPeyYHpOrk5YxJW-RxNDvfuFs7AgBoEShS1VSzJhxjnfqivciVXbeX2agqQ-4TLxTVN4EpdXeagQpr9dVotluxiCAJrOvtWRpYiLIsamsj2oseqETxxIFn89twIqzCZovpnVkxWjBsHHCHfa7YzTUEQMOtKtU25a35VchxYvHav3UAH4Kjr0O0IpLudNH8kA1_EEhIf7EF9SxYVXY4kjvWpobNflivZjwrxzLB15Sou-mVZNmKgn1evKL6LB4xtKzpED_tp_5Xb8mY3RgkIdtoptJ1ecFFx1g0UT60KjR_QnUfAvxvP052hMbFhKLruz6ZeagptQ2BLoLlFTc3yY4nvXwy8Pr4QV0_v1_DElauLi20YSuocf7ORVWdtyzvl5gbQg_XAL8TnGh2QMS-FT1O4CANMKd3KkhosuLnNgtL4m34Ap2og3bNj_4xEM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی زرنگی عادل جان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76438" target="_blank">📅 09:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76437">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4daCSWvi5MFACUaiHUtP0Y5HuUXoEPBpCSvYPLgjI1kyPpLpPvWG6fA-4EbFEfM_5A9f2o3-3u_9H_uEB2Vnzf-H-C3ME4HMPqPHkNr51ndwNDDU_YS9vWmEyD6y76XjnXfbFn-3280iMVH4O-Q8ktmaC57a-M8KXfOPSTtt2PAuVggiCUfp3gOdhVEzrBQ3GHpGlSzAzEBU_uf4w4wShHwe8N26r8lm_hCChOcagsMonDZHf_v_ODsxdQGEGq_gQQ6rN83nOHX22FBUE9JRqn40gzLqUGWpBZGgt5-BwO-Kso37w5wsl4PS1a0dKr5yuHM_6BZuEv82oZ1jHkeLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صب وسط بسکتبال داشتن همو میکردن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76437" target="_blank">📅 09:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76435">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfTR8xp7t1BD9WgZmB2u26mLkoK7uoC3NkvzNYmug7IfRQHsglQhXJWjmWK7lp1xsO3Op27zQNthYSgfN35aD0Ry-elBbB8VHF8mvWvmz22dwUz_Er16UawB3zJqN_QT5j-r0wWynJUXRd-mvRK4YTzgUHqsjALs4NcrgZzCLfe797YcTLJBeTm96Qg8aSU6MPuy47ArMupYOJgXcsj29O7Xen4rXLDfJkvrD293VCPlf1y-AL55o3SyFSTNp-yhLFaeXgs4GfRfF1rmg0poxCnoKmriVc5_SLEvybSmH0P5EiRSIatkpRClP-y-bay9nls7e_jn7sLKWQVXAcKFdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ce07890ba.mp4?token=gnJcIeq81DiLvgXU7IrNb26Puqx1vMKBc2y1OVmdQVjP4UmmkrQY8cbqR5bscK8bzvwTIkJn8p17iEoq1UYuOVzjKTdPS-q6PZOEeaeRZzRYIsnn5jqRFMNhj153gwcEtIuZSDKEg_FUSmrsMvQgsC2Fz24t_flxhyljELn8EJ9NLGvjbY4Pg-p0SmpduBkUrkK5envA1mpHb2bkHdHW5zVrIGtdYjF8pRsRXS5L-3nxi7ZCY_K-kuVtoGO1rq3m8Pf-YK0q-WTCD7lGuB0tU5gF8sDClrQnEDqfycyE7jgzfz9koO9BOwj2bFe03OQxKfLuGfskc9l_eEXaa7I9aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ce07890ba.mp4?token=gnJcIeq81DiLvgXU7IrNb26Puqx1vMKBc2y1OVmdQVjP4UmmkrQY8cbqR5bscK8bzvwTIkJn8p17iEoq1UYuOVzjKTdPS-q6PZOEeaeRZzRYIsnn5jqRFMNhj153gwcEtIuZSDKEg_FUSmrsMvQgsC2Fz24t_flxhyljELn8EJ9NLGvjbY4Pg-p0SmpduBkUrkK5envA1mpHb2bkHdHW5zVrIGtdYjF8pRsRXS5L-3nxi7ZCY_K-kuVtoGO1rq3m8Pf-YK0q-WTCD7lGuB0tU5gF8sDClrQnEDqfycyE7jgzfz9koO9BOwj2bFe03OQxKfLuGfskc9l_eEXaa7I9aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو پادکست جدید بنی بلانکو ، بنی جلوی سلناگومز میگه که از نظرش زیباترین سلبریتی زن دنیا سلنا نیست و مارگو رابی رو خوشگل‌ترین می‌دونه.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76435" target="_blank">📅 08:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76432">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ به «فاکس نیوز» درباره ارتش ایران: «ما آن را بی‌سروصدا رها کردیم، زیرا فکر می‌کنیم ارتش آنها تا حدودی میانه‌رو است. آنها افراد دیگری دارند که میانه‌رو نیستند و ما به هر حال از آنها مراقبت کردیم. ما انواع مختلف رهبری را حذف کردیم، اما اساساً ارتش آنها را بی‌سروصدا رها کردیم.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76432" target="_blank">📅 08:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76431">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2028de58a.mp4?token=F7P-ID0aFrRV-X7UJRXnCGuCK598STYkCv7MDqQ1cFAMqi3gdxSrawb6iBuz61ggO1hBJH7yWlRe1ANNfGAuGSxMMAWAy9Mia6zVhTvx41jAA_aVLepIdUixxUgwyaf5tiC1wo3R6Y3OQhLWv0d1Y4kDZchL97MpdET1hn4Qa-tjoxL9rJ1oNS0Gw9LNx6Dsb2XpUtCf-WhOmzbnhIIINK3YcMyclNY-6c9TP2ovrjf2iQ8Q794j22FuqsFEbEaJ4WnHqoXxfhjVyc6kM58ejoEZh93oPGAW236MekfnvAk1O33kapHnYBAgU5xwo2rcuhGmOuqJTi2Q3rdctQvQbmxpJBZZQKmA1Iw0K0HXGUitNguDd2KpohkP8wCy88zzJ_wI4mzC8zmbJjJ_SCin0XAYVL8ifOI81o_MtOvTwzjWWiCE3aDr14r5x2BgaZt0gUmHhPhVGIGo_FLvERkLEHoMuytmKSW7q6bAI-Kt9AIy1AKiqp1GNJ0NWMY2PwBfowLM5KudRoMxtQ1x84-0lV9wqavoEBu9UzJ0vocxD6cl-Ao8KCBeCyWGG3jCkE3iWCWCYdr2X9O6dZqTbjIC9w-MFOgz23qyNSOc1OWOASin2G8stl6WYt6dME04wPZUXnfqcXiAm89HGOZEILsafg5yPz11y748WwXaZQAzEwk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2028de58a.mp4?token=F7P-ID0aFrRV-X7UJRXnCGuCK598STYkCv7MDqQ1cFAMqi3gdxSrawb6iBuz61ggO1hBJH7yWlRe1ANNfGAuGSxMMAWAy9Mia6zVhTvx41jAA_aVLepIdUixxUgwyaf5tiC1wo3R6Y3OQhLWv0d1Y4kDZchL97MpdET1hn4Qa-tjoxL9rJ1oNS0Gw9LNx6Dsb2XpUtCf-WhOmzbnhIIINK3YcMyclNY-6c9TP2ovrjf2iQ8Q794j22FuqsFEbEaJ4WnHqoXxfhjVyc6kM58ejoEZh93oPGAW236MekfnvAk1O33kapHnYBAgU5xwo2rcuhGmOuqJTi2Q3rdctQvQbmxpJBZZQKmA1Iw0K0HXGUitNguDd2KpohkP8wCy88zzJ_wI4mzC8zmbJjJ_SCin0XAYVL8ifOI81o_MtOvTwzjWWiCE3aDr14r5x2BgaZt0gUmHhPhVGIGo_FLvERkLEHoMuytmKSW7q6bAI-Kt9AIy1AKiqp1GNJ0NWMY2PwBfowLM5KudRoMxtQ1x84-0lV9wqavoEBu9UzJ0vocxD6cl-Ao8KCBeCyWGG3jCkE3iWCWCYdr2X9O6dZqTbjIC9w-MFOgz23qyNSOc1OWOASin2G8stl6WYt6dME04wPZUXnfqcXiAm89HGOZEILsafg5yPz11y748WwXaZQAzEwk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باز خداروشکر فینال رو بردن میباختن چیکار میکردن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76431" target="_blank">📅 08:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76430">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">MFGA
دیروز تو فرانسه مردم دست به اعتراضات زدن و  با پلیس درگیر شدن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76430" target="_blank">📅 08:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76429">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">داداشم ومبی ضرر دیشبو شست برد</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76429" target="_blank">📅 06:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76428">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAsPbMfhNuDNv2YQfZUhUdRryidch5nvJDra4hpnkrpma-VAoLqkYPR7WhgH-e88QO2ZwRCAV-ArOj7ONks2lSC-W8FDr3H5qV0TjUXBywVRf0PwaEYjYQdNzTTDnov6sIDHzilf021zSJ5n56KicDYu2YIu-ebIJOS5iZxMrqxZiz9jvxSqVnrUDJlICkpcbe9gywKocX6deQJIQx58c8P23NUjJKkAGVxZ2zjSn_mUzA_z8nDfiCi7V9MM5k4reLYH7GoAakpegSrQrv6aXdu3ArBGqlCjvHN-VITir-GBLbeNUszyp436qgURNFBYR23Wl-kC1JnD8qOy_MBzJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترمب با پست کردن یه عکس از جنگنده‌ها و ناوهای آمریکایی:
شما درحال سردرگم شدن هستید.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/76428" target="_blank">📅 02:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76426">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NegbXcy3AkDleAaTG9Ot8E2wOe6_mARMRu0wywBRhavtHWZzwVsRd2PfoAq3gehzlpnpDaRHUgip1DzMn1ccm5q0ZjTQZcf1fWxIfbGBkaObXqWQFJf-DcLwp8M_VgFxIRCRVPXJT6OaXtY8toYFxPh-8qfqKms1mjIiwCY5VJBQu8mU8T7z0NpmNE2VzfphsaOlDr0AC_CcWRfOXR1fGIGeDSP9CX9Abl8w1OZXcyRcCfnSCLjXXEdc9l8oFLS8iyil5RYueTa46qwYfG0NNvq8DERDHcEoryKZkkcdHMrZ4jX1mLx9W1B7R6FLLZ6uEp0ilbKhoKd10KfESX4DJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقد خشن حمایت نکن آرتا، بهشون رحم کن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/76426" target="_blank">📅 00:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76425">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLhoWKnRRn3EcrVB6VaC40EFzXFIzNw3x668RylHUZgeIVVHa7KjQUrOiOO0cS73yXYeA67g51dcSOjEXWhOAfPJWpve-w7P0qkLagx8vkV8LD41mzb99Y4JhaLKVJPWMxxBsHg7PNO0uaxBch5yfQXRigYBst7A49y604pQH0VreaXxtXmittTVb6Nl95nHZtpwKKiOETaL5_wKfE2jPOPqzwM0O5BB5iQXBzIQ6Gd5IPmgQeNBH2JuyXFdqDf7vACe3Kyeb8MrwNpi4g624UiK1u2rnTc5ydX_64MxJA6dhArVGta_qgLYq7qDA1cVlih_EsiVqxwEu6AOSgjakQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو میخواستم با کپشن سه تا تیم نجس تو یه قاب بزارم یادم رفت
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/76425" target="_blank">📅 00:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76424">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اینم توضیحات منیجر ویناک راجب حرفای امین منیجر
خلاصش اینه که برا ویناک پرونده سازی کردن ازش باج گرفتن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/76424" target="_blank">📅 23:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76423">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrxnfZFXgnKxAL9tvBtcLUuBjTw0pcxyi0Y1zMgB09y5RdORAz96p50L1pjRr4u5CATmlQZIJ4_-2J9-n3Mz-GwfSwCS7WyBl9HkAGrVlg7jntnRi1SAPQGsc0iDXXUgo1BjOujHrDWt7n4wvdpdP25T4gTCXpPgaSN0L_4vA0Q63kcHz5TNYr24LaAJnWWeG6AEUTO2-LTCjAanR9Oo8Ne-gjV97GXTVun1FKnaZ1dV3ovG38xWLhW9DLB-2GafHXphmN8AJTz6ArSm9CkCBcZeE4bz3Eim4wPrMaI-wpg9ACfjSecT2AWgAo3-iS8hX-pX5kTNBeKPEvHMEZmexA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم گذاشت چنلش گفت بگم اینایی که باهاشون عکس گرفتی شغلشون چیه؟  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/76423" target="_blank">📅 23:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76422">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoTpc4e2V3wxrF0McuupIfPygCpswavWu2fb08yQFIxqp_TWVbnSTlW4D9NUf6kTZ_VUW3G7Grvdsv1ejAJ3QjIiF0asieeVH2iR0vjtUtL-0iJBME56slhkufTlJ5OWlztumbvO2w5NonvM_VYAkGl1YMnDCXMpvTiRDYdDLbkxIAbzzL9IC7IbQH-z_swN0Bwtnj0nV5-UWJWG6wyWYriCl2w2g1Yt1X6fbH5HgnN8Dirlnx87YqfnwecMfAb5-ltaGRW1JOdkeqIgaPAed2Q6H_otsVZCc0Ws5oiotxGULw9fMefNTlQSs0sN8GdFxhDwvnjvidhFVbwAwFXT6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام آرسنال قهرمان شددد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76422" target="_blank">📅 23:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76421">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhUCSEUrFgLYbVMkii8DoBrHBcw1WYM4dQbHVw91_D7GVA2KxJ9cZiAHWmsu8P5LjWWjo6TsYkm3IqVE9tggkdblJJoqjnV2pHXdb50fGHBj8n_ygPV2LVUFmNnqYpT93gJW0kCIVy4g_8V6KEr4A5M071d9AGpLLYtM7z3-saD7AYRm4x8B8n_RJVZq8zE0M3qwA6PQKoIpLYjamPETHYKiFOdv8ali2azfa1AM7IFo2LCYXguq1uDUA_Gl0KLYRrseGNFkv1DO28eD-u13hzPEXK9yXYEnRX3xKpyyJlWg65cmdrH0iKnq_lXRg5zDaYeOWG7d9j8Xlop-DU-xVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم اینجا کیرخرم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76421" target="_blank">📅 23:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76420">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">حاجی فیلم خاکبرسری ریری هم اینور اونور توسط یکی از اکسای قدیمیش پخش شده واسه زمان زاخار رکوردزه
😂
😂
😂
😂
🔴
برای دانلود کلیک کنید روی لینک زیر :   https://t.me/RapiFreeBot?start=get_uplzypfzeequaabv</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76420" target="_blank">📅 23:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76419">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iymQAzcERsbgCzaCIwi-TxWUG2nlR7yk5iJmtLt6COdfHuxlqcuEvc42cbmEIZl08qfhdY2QA6fWDGCr0msiH1Abxb5uNWXUOSncHC2NvSeImXnjYtsF6auP-DGAbhfWYimdrLUJ-ma5N7CbXA4v_UrMupDPOD6m1IlVGXUORxuKXFFayqcoRdHuLKA4tpsQ8WJD8jfVx1H4dlPj0wCaaIl0sp1UyHwFxDl6QWYwSGFmNkftP-z-h6Wqp4YxyKIdAemUKDpnq0DyENa9wVg8WfsnpWwiJx_gMHRoZQ0AGDZ095trDYcm681uAUbzE-90MujSn7De0ot_VZjN7wknNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه من همین الان با یه اکانت رندوم یه همچین چیزی با عکس خودم پست کنم زیر ۲۴ ساعت اکانتمو می‌بندن و میان میبرنم تیمارستان می‌بندنم به تخت
ولی این کصکش چون رئیس جمهور آمریکاست همه می‌گن پشمام دیدی چی گفت پسر
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76419" target="_blank">📅 23:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76418">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDs7aKi_buW9903nRIW_fYrSAy0_7R5sUSFlIXnCID7tLuedWuEVHXVKiLtMVoKHYFZGAVh9IHWxz6xiuQrRmJgGLVj2fdxWmax5vE3o98uXNBNHcZYcaf7knWr34XGt0lyUaASqdHRXm9qiP77v4V4xXu6J8N2gvCPOPBM8xmMW79g2pmyC2f280LygKT_PRusIc-3nQNo9gRPT_ueBtEd7f2ZPlsYzzoT28rnIp2mL0iBy4MTz4Ar8BU4OodNWh6PdogyhsogyqsSRPrruV2QyJgkuiNflLAxbrNAIlEuhEivqYOm6KDDIAUZbYYx_yQvosBumZSm_mdytl2U9SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی فیلم خاکبرسری ریری هم اینور اونور توسط یکی از اکسای قدیمیش پخش شده واسه زمان زاخار رکوردزه
😂
😂
😂
😂
🔴
برای دانلود کلیک کنید روی لینک زیر :
https://t.me/RapiFreeBot?start=get_uplzypfzeequaabv</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76418" target="_blank">📅 22:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76417">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">با این نتایج انریکه چندسالم نتیجه نگیره ناصر بهش دست نمیزنه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76417" target="_blank">📅 22:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76416">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اما امباپه عجب آدم بدبختیه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76416" target="_blank">📅 22:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76414">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8Vp5oFZ0lH15QoZMLJYanIjF5LpzTTM67KqsosNXKWVMEeRT8DX8FH027HHqnynhUE3FhIe7RbWgvnxf4uVEp5w_7XB5kJe7qcA3-bOLPT2wC8fP_msSpMU16bJLozgIJLarVV_M0JjQW1uCDRmDkFlSZqdAExjl_2gPGNXA2ASPOhFId5dqD8kCjQ1J9wKGfsI0r9HaLPIQjhnry8JQTeuOy5hzq-pMB_0vlhMrCn9B8Czs330TiCpCbU8c-JPlJWyxGK6IXn4vcOhUDC0r_AA_wS9WVwfvK8wQuOjSsCT9nX-0vP0Z0YzYUn-RG0jEvrApBPHTMjd_UtgWac9sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده مشخص شد https://t.me/FunyHipHopGP/12247710</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76414" target="_blank">📅 22:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76413">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تو کامنت نتیجه بازی امشب رو پیشبینی کنید  اولین نفری که بعد از اتمام بازی درست گفته باشه نتیجه رو  یک گیفت Nft میزنم برا اکانتش  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76413" target="_blank">📅 22:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76412">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">هوادارای آرسنال الان یه دوش آب سرد برید حتما چون بشدت حالتون خرابه امکان خدایی نکرده سکته هست،حتما یه دوش آب سرد برید و سعی کنید گوشی رو بذارید کنار تا فردا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76412" target="_blank">📅 22:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76411">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhgKM0qMBcOaxTCuxP30MI4C_WciI59mfj2uf2hvYHMmXtYvusQ4cUrjIckJikVSPcURaoG_j_-z28Gl11L8rLVzoF7BkxdzK9NIbuCvMB1IjRcbieEwE65xr024hnPacuj9FEs2Awc2IZZZJM1d1A3LqkDvf2LdPFVfbwWVeuyeth95zpP8zb4NaoU6IH5ukONkHQkZkaJBKMJPSxJbqMXe0Tmdtk_zP3lnkerv7JRQ6hsTkmi_YW1hCik7NwaOcTmQMCpJ4keAl4Bk-ggNRNGz4OrlaIwtjX-zkB_1HbkJ90HNgmbsBeJ5D2RGVA_e31uS3DetNcvBJkZYa4Drlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پروف
#غمگین
#شله
#نور_از_دل_عالم_رفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76411" target="_blank">📅 22:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76410">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تو کامنت نتیجه بازی امشب رو پیشبینی کنید  اولین نفری که بعد از اتمام بازی درست گفته باشه نتیجه رو  یک گیفت Nft میزنم برا اکانتش  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/76410" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
