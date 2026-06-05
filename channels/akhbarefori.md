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
<img src="https://cdn4.telesco.pe/file/DGShUanv8_LWDxyF8PR0FrPs1WjMxZyO4rPM1U5RMu0Zv7SL6Y73mjygwN7OfSNE69SMQ6NSEXslUJBgNdFjRjAEepWsdCUijUfUBpKrmLWAfsJNZk8WYywg_VfU7hqcP_FP1UEdb6fyEEz9ZWLEb9oiyY5NVJx8NJzPdtJYKTilhTv3skObCLNSSpxDVNmouCEKNmIIxOJjYXbofnan4D5swVqAOQIO1cUCdpJTUxoaDvU5k5RBo9rdkChHNbHy_bUsmR3A4JjaxJkVHngBWN38_LlzvLbu-uvvkiTux1bC2W6rLKZcXt_a_D4Nap2Gt2YBnazfEgwHk2fOHQ7zSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.15M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 15:12:48</div>
<hr>

<div class="tg-post" id="msg-656341">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d14e75aa6.mp4?token=atrUVplvp0_Hbl8_5i3gC-QpKqq-8ZcRoqN3mm4FKlDMs_00YCid19QLlqIOTtqTqh0CSDkg10F_FW94tFnG-QQyIIdFklJ57uXau_uyRwihl-CEk9aR0tDTyWXePksKsVVLGJMdzhJ1jI1wro9DXKN65O_Va1fN19Y3YYEtiBnpWciNkOHmjBtyN1op7xCo2MAc2OrLD-h7Omngh_0vfJby2UYoomInCKuE7H2P-wmCMglFHnjyHrlv0ZzGPsdeJ3E8vo_As7pPHx6lk_Oo1sLM8yCKP7Q9qE21XmWaHoRrbT7Ajx7-JHOLRZYDLchK41P7jVEQ6CBQZ6gCa9nm_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d14e75aa6.mp4?token=atrUVplvp0_Hbl8_5i3gC-QpKqq-8ZcRoqN3mm4FKlDMs_00YCid19QLlqIOTtqTqh0CSDkg10F_FW94tFnG-QQyIIdFklJ57uXau_uyRwihl-CEk9aR0tDTyWXePksKsVVLGJMdzhJ1jI1wro9DXKN65O_Va1fN19Y3YYEtiBnpWciNkOHmjBtyN1op7xCo2MAc2OrLD-h7Omngh_0vfJby2UYoomInCKuE7H2P-wmCMglFHnjyHrlv0ZzGPsdeJ3E8vo_As7pPHx6lk_Oo1sLM8yCKP7Q9qE21XmWaHoRrbT7Ajx7-JHOLRZYDLchK41P7jVEQ6CBQZ6gCa9nm_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شلیک اخطار موشکی - پهپادی نداجا به سمت ناوشکن‌های متجاوز و مزاحم آمریکایی
روابط عمومی ارتش:
🔹
پس از شلیک اخطار موشک‌های «قدیر» و پهپادهای تهاجمی نیروی دریایی ارتش به سمت ناوشکن‌های آمریکایی DDG-103 و DDG-87، این شناورها دریای عمان را ترک کرده و به سمت اقیانوس هند رفتند.
🔹
همچنین ناوبالگرد تهاجمی آب‌خاکی «تریپولی» نیز از منطقه خارج شد.
🔹
در صورت نیاز از موشک‌های با برد بیشتر استفاده خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/akhbarefori/656341" target="_blank">📅 15:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656340">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ff94c6303.mp4?token=cYM535HRya5x6w_dJvBJzwx0LapvtNdk5mCkODYFLXNJv9YivHc-0CuIm2CN_OftW4iFGjgMGvtqKorGmRcE5vbk1ZoDnn_u2NDdmcYxgnzZneuYVz6Wtas2l5WLnAXMvAsPdeER5R9aLgbsUxbg57n_0eG5gKn4AJ3jPHMD36vSUZ_iwg96y80BInr8kpZ-GejqGwZ7x0Uhm0g_JeVuXX-dXBQJtYETOMyzDh3B5t8UUmoQ27PcnerldKuEU-HpqEdog4-20zWMhkTIa7s1lRxadst4vzZfmRSbk84G7vAs42jmqnV8nqnbX4puIrmljriVCJVk-V7ZIqdBj5VUYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ff94c6303.mp4?token=cYM535HRya5x6w_dJvBJzwx0LapvtNdk5mCkODYFLXNJv9YivHc-0CuIm2CN_OftW4iFGjgMGvtqKorGmRcE5vbk1ZoDnn_u2NDdmcYxgnzZneuYVz6Wtas2l5WLnAXMvAsPdeER5R9aLgbsUxbg57n_0eG5gKn4AJ3jPHMD36vSUZ_iwg96y80BInr8kpZ-GejqGwZ7x0Uhm0g_JeVuXX-dXBQJtYETOMyzDh3B5t8UUmoQ27PcnerldKuEU-HpqEdog4-20zWMhkTIa7s1lRxadst4vzZfmRSbk84G7vAs42jmqnV8nqnbX4puIrmljriVCJVk-V7ZIqdBj5VUYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پست اینستاگرامی عراقچی در داغ دانش‌آموزان میناب/داغ ناتمام میناب
🔹
داغ کودکان، داغی نیست که واژه‌ها تابِ بیانش را داشته باشند؛ به‌ویژه آن‌گاه که پای دخترکان و پسرکان معصومی در میان باشد که با رؤیاهای کوچک و قلب‌های بزرگ، پا به مدرسه گذاشته بودند تا آینده‌ای روشن بسازند، اما خود، چراغِ آسمان شدند.
🔹
گاهی تاریخ را کودکان می نویسند... و این بار کودکان میناب تاریخ‌نگار زخمی شدند که بر پیکر انسانیت وارد شد.
🔹
و وجدان‌های بیدار تا ابد خواهند پرسید: به کدامین گناه کشته شدند…
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/akhbarefori/656340" target="_blank">📅 15:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656339">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
منبع ایرانی: ادعای العربیه دربارهٔ موافقت تهران با انتقال ذخایر اورانیوم به کشور ثالث صحت ندارد
🔹
یک منبع آگاه نزدیک به تیم مذاکره‌کنندهٔ ایران روز جمعه گزارش رسانهٔ‌ سعودی مبنی‌بر موافقت تهران با انتقال بخشی از ذخایر اورانیوم غنی‌شده خود به یک کشور ثالث را رد کرد و آن را نادرست خواند.
🔹
شبکهٔ العربیه پیش‌تر گزارش داده بود که ایران به‌طور رسمی با انتقال بخشی از ذخایر اورانیوم خود به کشوری ثالث که مورد توافق طرفین باشد، موافقت کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/akhbarefori/656339" target="_blank">📅 14:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656338">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92e2301c57.mp4?token=bw4EAWAu7ezICSvqV4WYM5xwGx18p5d1w3qrIiSquboDi3Nbw3gWECPeDDcCArvu2Kor10ClhgbVUqM9SwdK49PjOF58OQz7mKkU8_-6PqJj4etxV2OtPsRAQJz3WVQUvFfli85QummNYi1sqSyyVWKHcWGOCzoVTePWHHTthk32ofsNOJ__Vd50kVG5SWncSnkT2riB-AY-rnzdKDe43wwZlruf26iatzitEU9-zDzihxCrSX3lp-euIAMu806eqXNHCZI8SQEhKTSACB-zdsMOZefCMUA8-fdf8azhS1__VQNhcd2EyPpBcxhaqEeERpypjqNHlsMeK2rqQf7EjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92e2301c57.mp4?token=bw4EAWAu7ezICSvqV4WYM5xwGx18p5d1w3qrIiSquboDi3Nbw3gWECPeDDcCArvu2Kor10ClhgbVUqM9SwdK49PjOF58OQz7mKkU8_-6PqJj4etxV2OtPsRAQJz3WVQUvFfli85QummNYi1sqSyyVWKHcWGOCzoVTePWHHTthk32ofsNOJ__Vd50kVG5SWncSnkT2riB-AY-rnzdKDe43wwZlruf26iatzitEU9-zDzihxCrSX3lp-euIAMu806eqXNHCZI8SQEhKTSACB-zdsMOZefCMUA8-fdf8azhS1__VQNhcd2EyPpBcxhaqEeERpypjqNHlsMeK2rqQf7EjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی پربازدید زن ایرانی در رمی جمرات
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/akhbarefori/656338" target="_blank">📅 14:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656337">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
گروسی: آژانش استاندارد دوگانه ندارد
مدیرکل آژانس بین‌المللی انرژی اتمی:
🔹
فعالیت‌های نظامی علیه نیروگاه‌های هسته‌ای «مخاطرات غیرقابل‌قبولی» به همراه دارد و در هر کجای جهان ممنوع است.
🔹
در آژانس بین‌المللی انرژی اتمی، استانداردهای دوگانه یا سه‌گانه وجود ندارد
🔹
ایمنی هسته‌ای امری بنیادین و قابل اجرای برای همه، بدون هیچ استثنایی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/akhbarefori/656337" target="_blank">📅 14:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656336">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Va9hgn3eg6yuivcXAnYQ53Gn-PhWCENVpsr_8FqCwGdCLNrzLglx5f8TX5DJxbqLedzyW-F9BldaYhTDuQX3w2Ffw0spVVY-pr0c55SMs6OqYwH1oniW_y6ywlOSD_wlqI6Zb7fTgpcjCWVofwW68NpLS-nkzx0acg6aZnpCA_Cx5FFyA3tDsh1LMKhs5UydrN_JmoVbmbjK-JMPVa79p-F1AXuJuN81ygsKpcIX5ZFc7z7AHNiwFE6V1vCRHYOlmLT-tpiTH4MannayKigOgmVfZsPEF1gGAxTWqnUyYhR9_x02CjQhdvpAI6X3v_mpEjwAhC0fshMVfmKdn6TIFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای ویتامین‌های ضروری: مزایا و منابع کلیدی غذایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/656336" target="_blank">📅 14:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656335">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXTKi5puDBEF_Vsv0-d1QWbPnvGh-JnTTnA5qACXdjGeu8g9mod30Y2afukdTlkg2UQ2bZG1GFNhqGarZNCvXVMjvTEVGTM8OUlTol7i_0u63SG3juZiqViTKXyHRHlkjYkB86o8PutPACHASr_X03qC1hL3fHHfVNYOVYCIb4OwG16kiXyetb_XutBFpAk-eZcd036pETLWnMmThV04yQ3P2RtA-9TyulUB9vzUKYHpQaXlQVOlV49kgx6dK9pcaAH2vdNsdUBui3_OClvIfW7MgSganQMrt0yZPu3_5Rz1Et0Np1opCiAkhUM2uSFsZYRWt6fwv1_FCYSQBr6dag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت روز جهانی محیط زیست؛ «ایران سبز»
🔹
همراهان عزیز خبرفوری، برای شرکت در این فراخوان کافی است تنها یک اقدام ساده برای محیط زیست را انتخاب و همین امروز انجام دهید؛ از کاشت یک نهال یا جمع‌آوری زباله در فضاهای عمومی گرفته تا کاهش مصرف پلاستیک، صرفه‌جویی در آب و برق و استفاده بیشتر از دوچرخه یا حمل‌ونقل عمومی.
🔹
عکس ها و ویدئو های خودتون رو برای ما ارسال کنید
👇
#ایران_سبز
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/656335" target="_blank">📅 14:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656334">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ابراز دلتنگی مردم به رهبر شهید در مهمانی کیلومتری غدیر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/656334" target="_blank">📅 14:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656333">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ec1c1c628.mp4?token=JB3UvMXnQP62z8vDUAIA2TcN7jrLnpEEfjUx26iyQDR0iO8612f7rPtSQiYI8LGBxQWHZ6P0i3P0i4EONCRxdsC0tjNNkqbkyYyO6VEzeUoexKVt5f2S085AEzQvZ0Y1nzwrYXiBIkkaQL0yzOf9ivJ6m0nvTeHH7EnqmpOH4IEX2DzSbHEuevyOsePV4t8x37omuLP-iJbpu5GwFEL2D-ycnZR5Fb0Rvarea_epiJff3IpVTVEwDOQwfqK0alSI26f_v6jMp-OgU1Br5JKMALWJBE2kg0a5dqpsw5610oYhBoN_lnsa5bOo7loFrsxtUJ0-aPhG_NxE8clNkVrK6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ec1c1c628.mp4?token=JB3UvMXnQP62z8vDUAIA2TcN7jrLnpEEfjUx26iyQDR0iO8612f7rPtSQiYI8LGBxQWHZ6P0i3P0i4EONCRxdsC0tjNNkqbkyYyO6VEzeUoexKVt5f2S085AEzQvZ0Y1nzwrYXiBIkkaQL0yzOf9ivJ6m0nvTeHH7EnqmpOH4IEX2DzSbHEuevyOsePV4t8x37omuLP-iJbpu5GwFEL2D-ycnZR5Fb0Rvarea_epiJff3IpVTVEwDOQwfqK0alSI26f_v6jMp-OgU1Br5JKMALWJBE2kg0a5dqpsw5610oYhBoN_lnsa5bOo7loFrsxtUJ0-aPhG_NxE8clNkVrK6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای امیرحسین ثابتی: آمریکا بعد از جام جهانی سنگین‌تر به ایران حمله خواهد کرد/ ایران را تبدیل به غزه دوم خواهند کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/656333" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656332">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
در جدیدترین رده‌بندی تیم‌های ملی فوتبال جهان، تیم ملی ایران به رده بیستم دنیا صعود کرد.
🔹
لاوروف: یکی از اهداف حمله به ایران برهم‌زدن عادی سازی روابط اعراب و تهران بود.
🔹
روسیه: ممکن است ظرف چند ماه آینده کمبود نفت رخ دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/656332" target="_blank">📅 14:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656331">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDqSN4mbfFDRYnrmQAn9ull6mMFTcvDxuCX7X6rueIGbc0_sAJNXo7rgwEFpA7d2V7ThU5q5t1QmnFPFT5uDBmsqOPMa9sVxh387TtYJJvhm8kahnAn6CUxiA05qLckHJ_o4IYlyHKxPl_klTDqQO7qyQFRmzVd1gVfiV5klmznyFkVyktXziGYSwvkCpLsLfhVoB1nWkVH5wI5sgxb1VYG6k7OmP-eqoeHL4JUGS78mAZcheleET1FSFDTYiRmbULtg5Dd443gj85I5PN8Q3df3I4gxTaXLeHQlI1eZr89ZVl2lXHRK0a8FGgMHE1QliMV35lkKMXEfGhQpBqMI4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فیفا تأیید کرد که نقصی در وب‌سایتش باعث شد ده‌ها هوادار بلیت‌های رایگان جام جهانی دریافت کنند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/656331" target="_blank">📅 14:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656330">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
نماینده مجلس: میزان کشت خشخاش در استان‌های ایران بسیار بالا رفته
جمالیان:
🔹
در استانی که قبلا برنج می‌کاشتند، امروز به کاشت خشخاش روی آوردند.
🔹
با توجه به اینکه این محصولات خالص‌تر هستند، قطعاً شدت اعتیاد را افزایش می‌دهند
🔹
خشخاش‌هایی که [غیر قانونی] کاشته می‌شوند، جزو کشفیات‌است و به کارخانه‌های داروسازی تحویل داده می‌شود./انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/656330" target="_blank">📅 13:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656329">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
حمله پهپادی به کشتی‌های حمل غلات در دریای آزوف
رویترز:
🔹
در پی حمله پهپادی به کشتی‌های باری حامل غلات در دریای آزوف (در اروپای شرقی) ۵ ملوان آذربایجانی کشته شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/656329" target="_blank">📅 13:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656328">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a3232953.mp4?token=UBmx3cHI6nFsp1P6MCePo_BMOcH3QrojGvufz4TE4ZzvTQGZ0ZsFrh9gv5xSmsoyXhmCZhqmkIUf2VhydxE74Ce1-AnQ5134GX_2rPnMJ82FED1kxeBkudDtE9MwlS8lb_mXsbxcbwkLQ2S3YRL1Yn12XVmPqBkHusQfA8RTlN-9JcHbx-2ImpaDYzTy3BxwRsiFxBO_NfnkqDaWpQDuy7rDHb9I9ebiTLP5EH1ohJMyJ-mxAFMLp1IfVuepbiiBs7P88oaQP8p-MC3UdeRNFQ83clVqSCp9ohL3UEfUGBy6piBCACxqNw1gIYBs7o-TYL9RePgiH4ytNseAvJWM03BGMjoUmxWh6EAp_USTeSrgfOilf3T6kVFjlZv5Lbe6dhu1AqJwuLzWD0lcbmqQUC-YapGC3PNOHo5CLJv-cydFpo7ubE8_8z2WGNu-IwOCYTEdu-aHtSAmIIXsOPcU-uzgQ5kgUqWdPUHcdg0qpDO-OPz_xEfN2p4FLsT5iVZQ0G7nJcRePMpxpgJ3Wg7-YgiImilj_4pWNx8zZVrm9EFW1wtBN5FJQptmRW3d9j-dF1INby1H7suOzFhiu3EPUzsAaqOn0kshCSY__rpbUhHwLeeVgKvq39tAWYdwtFDyTT5yAxz16RDKOrGizfbQnWNg53vsB9D7PCtblsCdIMU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a3232953.mp4?token=UBmx3cHI6nFsp1P6MCePo_BMOcH3QrojGvufz4TE4ZzvTQGZ0ZsFrh9gv5xSmsoyXhmCZhqmkIUf2VhydxE74Ce1-AnQ5134GX_2rPnMJ82FED1kxeBkudDtE9MwlS8lb_mXsbxcbwkLQ2S3YRL1Yn12XVmPqBkHusQfA8RTlN-9JcHbx-2ImpaDYzTy3BxwRsiFxBO_NfnkqDaWpQDuy7rDHb9I9ebiTLP5EH1ohJMyJ-mxAFMLp1IfVuepbiiBs7P88oaQP8p-MC3UdeRNFQ83clVqSCp9ohL3UEfUGBy6piBCACxqNw1gIYBs7o-TYL9RePgiH4ytNseAvJWM03BGMjoUmxWh6EAp_USTeSrgfOilf3T6kVFjlZv5Lbe6dhu1AqJwuLzWD0lcbmqQUC-YapGC3PNOHo5CLJv-cydFpo7ubE8_8z2WGNu-IwOCYTEdu-aHtSAmIIXsOPcU-uzgQ5kgUqWdPUHcdg0qpDO-OPz_xEfN2p4FLsT5iVZQ0G7nJcRePMpxpgJ3Wg7-YgiImilj_4pWNx8zZVrm9EFW1wtBN5FJQptmRW3d9j-dF1INby1H7suOzFhiu3EPUzsAaqOn0kshCSY__rpbUhHwLeeVgKvq39tAWYdwtFDyTT5yAxz16RDKOrGizfbQnWNg53vsB9D7PCtblsCdIMU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از عجیب‌ترین چشمه‌های جهان
🔹
در یکی از چشمه‌های ارتفاعات دهلران به جای آب خالص، قیر و نفت خام بیرون میاد
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/656328" target="_blank">📅 13:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656327">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoF2HiYGkkGXDsrShsOMvqp5k55TYCspsCjLS17TYKFubVGR4BQumwQM8PBUlxLayK3GhCZp6K3c0bPpvOqfKZ5q9seJ3sUDNMRvFBVG8kNTrazGvHM4y5g0KfP1Olo3zCIxdCs-8QBgZoNo965glkSswAub6_wVgewE9YpfmkTQXCNlSEMSbc_IqKu-Ycaqcb6mzSbp0r5D5Vx67KzQhbrBt_7zrPnrg8oIMENQhgAWpyderTDfSUD52l6ufYknd8twx5y9rgyNmFK1N_Jeio8wy37SlJGg0ZH2cI8IH9aChlIBun9MpnqMTzd8IUexVJgbHxksMZscpO8aQjs-Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم منتخب مسن‌ترین بازیکنان جام جهانی ٢٠٢۶
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/656327" target="_blank">📅 13:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656326">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
سرنوشت دارایی‌های مسدودشدهٔ ایران همچنان در هاله‌ای از ابهام
🔹
در حالیکه یکی از اصلی‌ترین خواسته‌های ایران در مذاکرات، آزادسازی دارایی‌های این کشور است، شبکهٔ العربیه مدعی شده است که ایالات متحده همچنان با درخواست ایران برای آزادسازی دارایی‌های بلوکه‌ شده مخالفت می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/656326" target="_blank">📅 13:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656325">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
از یک اتاق بچگی ساده تا یک سوئیت لوکس شخصی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/656325" target="_blank">📅 13:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656324">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14e51c158.mp4?token=ZORfgDAStcrzzrKe3iiOEqFbAl2do1yPOpF4XXPjEDGP9SY52G06tpRNyPgPWIEwE2F3A0ZSiS-b9xdi5QlMSl5G1_N-HWq0jAGUvshOiZrRpRfnd1jnLu3vuZEBaoQx-DOumCf_b8sayamt_TdFLFL4iK-FnfdadwUVLwdUtYKaU5iYD4fhB-GeZrKXegWJ3b6gF7XtJtniFR93DPHWPEVBYS655ZJCKhozUOgSZclPwqx06TGqJ6lJfY4ysdTXqDATT0rMAXJgIFOreJplkB-vKvAuEVoDPuRnqgTUqa-vzMv0SD-oSfYqWK9LAevSLvlY_SYgQ9h--aOX2YbK5rTpO3vu3Q9YQlN9lFhXDaMXRiFSwUp3GK2H49446bUCn1ouzqkKVzJVgiByBnfVzGrKqxAZUyVtbsk7_9tKlEpgFuf2pdlTD97xFqTnjFtefcym9cEKD-KjqI-irKKncBxi6_3Iz5CJrRhzSjKKZ0Y_va2P5jP5jgAqNxtUslPj-NX7QNjq13h-FvP0fGoof48U0vuQh-XEnlmSOEatczKj8w_pbPuBPR0RH9W3wqW2X_u45tm8efqKYbeY5rIkzXPUGjmZ2XC6MQxK8tSvqtfCMv6hd2O0dJO1kc-dxGvCYL0DCy5wIXJRfJ3oKXEqBevlaYXXB6XlYQFhAVc4A2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14e51c158.mp4?token=ZORfgDAStcrzzrKe3iiOEqFbAl2do1yPOpF4XXPjEDGP9SY52G06tpRNyPgPWIEwE2F3A0ZSiS-b9xdi5QlMSl5G1_N-HWq0jAGUvshOiZrRpRfnd1jnLu3vuZEBaoQx-DOumCf_b8sayamt_TdFLFL4iK-FnfdadwUVLwdUtYKaU5iYD4fhB-GeZrKXegWJ3b6gF7XtJtniFR93DPHWPEVBYS655ZJCKhozUOgSZclPwqx06TGqJ6lJfY4ysdTXqDATT0rMAXJgIFOreJplkB-vKvAuEVoDPuRnqgTUqa-vzMv0SD-oSfYqWK9LAevSLvlY_SYgQ9h--aOX2YbK5rTpO3vu3Q9YQlN9lFhXDaMXRiFSwUp3GK2H49446bUCn1ouzqkKVzJVgiByBnfVzGrKqxAZUyVtbsk7_9tKlEpgFuf2pdlTD97xFqTnjFtefcym9cEKD-KjqI-irKKncBxi6_3Iz5CJrRhzSjKKZ0Y_va2P5jP5jgAqNxtUslPj-NX7QNjq13h-FvP0fGoof48U0vuQh-XEnlmSOEatczKj8w_pbPuBPR0RH9W3wqW2X_u45tm8efqKYbeY5rIkzXPUGjmZ2XC6MQxK8tSvqtfCMv6hd2O0dJO1kc-dxGvCYL0DCy5wIXJRfJ3oKXEqBevlaYXXB6XlYQFhAVc4A2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای امیرحسین ثابتی: آمریکا بعد از جام جهانی سنگین‌تر به ایران حمله خواهد کرد/ ایران را تبدیل به غزه دوم خواهند کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/656324" target="_blank">📅 13:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656323">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c85382a72e.mp4?token=IdjyE_DWC8jBm2gX8N6F7V6sksZqeZkuiDS6_tJp9VLk7_gSjnLOPZ0o7Z8E4bdZEcmQ82PalOy6MQFtezcbJUYp-um2j7YaUDdaT65NLmHgCAhgs1bzL3YiptIt59EFZa5djrS_qk7f-zr-vpSASY4bprkjYIkcE8NeXtUUaQDzXGNizFFaVMBgBKCKOabFNn6a7skciwaZqcoQiW-zM28CE7ZXxS9D_ZFHP7JTDffjNLEwBybzWPscfpek4_AQkjbn4S3nGH9mu68-l9GZUC1dVwKCKjnQgi5xD1GY-ULcmobNNwnu1tDpbnWBE_Tl7dB6vScCpuqPMTHRXRwepS7KOXvWYI-o9o1B6lkVHM71cGf1K8lFBd2DfSjOM_dxBEcwSRFkj4rebNEE7e_3YyVz91PelYz1WvyzqYafgb2grb8CKbxtjwoSYWxERqCxR0X3QC0ThyKbPjpcGdL7zPnwYKqOzeo2i9PLSyqx_CZnmgCzg4BCQAQmpjNFiU6LHUdK2HEmCW0GytfHP_7yyWN4tydxO0W2XWnDFKubh-tOxTuj_HXzxsspLSw75tKxlfah3HNgcvdFdzfAI1zW-oWDuAFo4OzjuGXGHRvGzAHhRqWFu4DiPsVJqxqwB61nz2jGLJ4KLPese3c3Lz8hhYsY_iLhCftzFVqAt2cXnvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c85382a72e.mp4?token=IdjyE_DWC8jBm2gX8N6F7V6sksZqeZkuiDS6_tJp9VLk7_gSjnLOPZ0o7Z8E4bdZEcmQ82PalOy6MQFtezcbJUYp-um2j7YaUDdaT65NLmHgCAhgs1bzL3YiptIt59EFZa5djrS_qk7f-zr-vpSASY4bprkjYIkcE8NeXtUUaQDzXGNizFFaVMBgBKCKOabFNn6a7skciwaZqcoQiW-zM28CE7ZXxS9D_ZFHP7JTDffjNLEwBybzWPscfpek4_AQkjbn4S3nGH9mu68-l9GZUC1dVwKCKjnQgi5xD1GY-ULcmobNNwnu1tDpbnWBE_Tl7dB6vScCpuqPMTHRXRwepS7KOXvWYI-o9o1B6lkVHM71cGf1K8lFBd2DfSjOM_dxBEcwSRFkj4rebNEE7e_3YyVz91PelYz1WvyzqYafgb2grb8CKbxtjwoSYWxERqCxR0X3QC0ThyKbPjpcGdL7zPnwYKqOzeo2i9PLSyqx_CZnmgCzg4BCQAQmpjNFiU6LHUdK2HEmCW0GytfHP_7yyWN4tydxO0W2XWnDFKubh-tOxTuj_HXzxsspLSw75tKxlfah3HNgcvdFdzfAI1zW-oWDuAFo4OzjuGXGHRvGzAHhRqWFu4DiPsVJqxqwB61nz2jGLJ4KLPese3c3Lz8hhYsY_iLhCftzFVqAt2cXnvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥇
احمدی‌وفا طلایی شد
🔹
علی احمدی وفا در رقابت‌های کشتی فرنگی  رنکینگ اتحادیه جهانی در دیدار فینال با نتیجه ۱۰ بر صفر یو چول رو از کره شمالی را مغلوب کرد و صاحب گردن آویز طلا شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/656323" target="_blank">📅 13:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656321">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WaIdFO2feRYwd6IHr0yfheUPsIouuya4pP0cZTDr28GMXPEg8g4HqQ7jxwZeZKlsmH2XJ-tcViuCN-_k-KmxByMTWLDANJjkJTEZmBrOpQkVODb6TeuB3MYrfTyQWPEklCkHATeglB2PwyARucd-RhEOzP2-g2p2X0dOtyRPvT_01ZbUrQuYhr7rzBRX86OOZyHl7xwky0EiKr_bVMWU9lW-G8m6Q55zrKMI6rM1evlzdzPvOzkD1nvXHwWCMs1ZgkTITQgIbpDYYO_r0KjJOckP3AGQ4ltPqJoJJTkbngWncKYvGgnYk9q61XVsG2smlPQsh26BGSKGiG7D_PicAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bkG2yXc4yDDGDhjIGlGP47XCeC2AyhGdvJP80iHytIzEliY-pnsWEKCqKm-BuIOPmRwrbYoAFsQi2Q9U68a2j9VDmeAq2kvJGkHzSbU9IIc8B9y5XyFQNf4VVWwHsMKtYrNVkDAnZO-79yczIxxv_SZpCge3IAhtUKn7yhY06GCO3vxSbX18muM_wLBhITfAns2Mux5-RbFDxJd-D3mJmZ7URMz54yL1VuGFL5OU480zVzb1kd0kzgarHg65UgeFcNkpKuo8sLBABxfRpwBBA0wN8z_gkFwoy-3WiHgkfq5m5kvwgIAblXB2o3yhLN73tXDI6wu5eZd3SHgghrbfRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تخریب کلیسا ثبت‌ ملی انجیلی شهر مشهد
🔹
تاریخ ساخت این کلیسا به دوره پهلوی اول می‌رسد و ثبت ملی بود.
🔹
هنوز خبر رسمی از علت تخریب منتشر نشده است.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/656321" target="_blank">📅 13:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656320">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
برگزاری مراسم سی‌وهفتمین سالگرد ارتحال امام خمینی(س) در حرم مطهر
🔹
مراسم سی‌وهفتمین سالگرد ارتحال حضرت امام خمینی(س) با حضور پرشور زائران و ارادتمندان بنیانگذار جمهوری اسلامی ایران در حرم مطهر ایشان برگزار شد.
🔹
این مراسم با تلاوت آیاتی از کلام‌الله مجید آغاز شد و در ادامه، مداحان اهل بیت(ع) با مرثیه‌سرایی و ذکر مصائب، یاد و خاطره امام راحل را گرامی داشتند.
🔹
همچنین در این مراسم، پیام رهبر معظم انقلاب اسلامی به مناسبت سی‌وهفتمین سالگرد ارتحال حضرت امام خمینی(س) قرائت شد و حاضران با آرمان‌های والای بنیانگذار جمهوری اسلامی ایران تجدید میثاق کردند.
🔹
اقامه نماز جماعت ظهر و عصر به امامت حجت الاسلام والمسلمین سید یاسر خمینی از دیگر برنامه‌های این مراسم معنوی بود که با حضور گسترده شرکت‌کنندگان در شبستان‌ها و صحن‌های حرم مطهر برگزار شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/656320" target="_blank">📅 13:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656319">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
موافقت رهبر معظم انقلاب با عفو یا تخفیف و تبدیل مجازات بیش از دو هزار نفر از محکومان قضایی
🔹
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای رهبر انقلاب اسلامی با درخواست رییس قوه‌ قضاییه برای عفو یا تخفیف و تبدیل مجازات دو هزار نفر از محکومان محاکم به مناسبت عید سعید غدیر خم موافقت کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/656319" target="_blank">📅 12:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656318">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSs1n1Swt-Cmpjpfw71L1k4Le-fOGy_20LIDt6Q2fMNdd8Bf5yVwfvIZox8iqw7SKmTJ9RuMoXaKHk6DoABjvBQt1R9q98j20VfP3oeByOZiDQgM1y-kdsB6Vre7lDAkdh2iN70rZ2BSisKUmT8JQQf7mYUbbdbAbdUw737zrfFUi4ai8TlQQRQ02nkyqpobb77t7KVv-FDur6Za44vXGXQaDk4NemERA9PanISIuwXEDUEhvtmNdbyHB8Td2OYqcWNX7YuS9wWhiue4iTiifkPmb8n2DL9DGYvk6_de4dAIFVW9xgprfaQNXvXzhEFLIN8i3rWvlZVq1aVm78Qg4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بچه‌گربه‌های جنگلی، مازندران
🔹
حامد تیزرویان
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/656318" target="_blank">📅 12:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656317">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f690f90a.mp4?token=kc2eZxIPM3QZzojRTqrJmY_J-fK4xyHvC_Laex8TMXN46-342MfM-MnaxBB7_5JcktdioEYS7WK1FjLLUpwuFSmU8hs0rlg5Vlfd6oXuv-AlygdSaHpuczfCfMVUZhoCJsVEBGPTUYjuhmAQBtVJFZ4n8udGOfMDdWcmr7y5QoW0osY1pk4U82SCQ-oDMqG6h_gpY83YBn_GkZUr-inxE0sAsvKWOtQVmB0nuL43Ri2vW8-q-5aHKlQqUyHFrI1fwC-i6pG7RXRJdf72w0-ixmo9ZU-Q63pcMUlzfqcs0UHRNNnG_hFssohhgTieZZcOLIUxjUtjDyJyAEhoK2O-w4mZlWy86xggfTRmf3ZfLm5ib3SHsDqesuDhXbIN75Q8CgJeiALaa_jzUcRmkLMm0cl-VUuvePslU7u7ugnC5zjheS4IVQ0wKJVAZn1xmsshP48jPoHaTYBMo667DJ2i-7iy3ovrH8iZ5krRWxNUQVri91HAoLA_37AuPQsRpn4xZdGco8y9XCKH1TQala9ooYd0tklPImGZcR8gEjRk26pwBFGu3fmQbG0MwxVqznEEBEDrRwzuJMul9cFZWjcd3nz3j1i_JXzNIIrQHymDMr55-G7cOnGLbLk8lxr_ZsmFW86VfDItVmVuc5CCSw-JF0tzerKSa15pZTuiTFvIwSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f690f90a.mp4?token=kc2eZxIPM3QZzojRTqrJmY_J-fK4xyHvC_Laex8TMXN46-342MfM-MnaxBB7_5JcktdioEYS7WK1FjLLUpwuFSmU8hs0rlg5Vlfd6oXuv-AlygdSaHpuczfCfMVUZhoCJsVEBGPTUYjuhmAQBtVJFZ4n8udGOfMDdWcmr7y5QoW0osY1pk4U82SCQ-oDMqG6h_gpY83YBn_GkZUr-inxE0sAsvKWOtQVmB0nuL43Ri2vW8-q-5aHKlQqUyHFrI1fwC-i6pG7RXRJdf72w0-ixmo9ZU-Q63pcMUlzfqcs0UHRNNnG_hFssohhgTieZZcOLIUxjUtjDyJyAEhoK2O-w4mZlWy86xggfTRmf3ZfLm5ib3SHsDqesuDhXbIN75Q8CgJeiALaa_jzUcRmkLMm0cl-VUuvePslU7u7ugnC5zjheS4IVQ0wKJVAZn1xmsshP48jPoHaTYBMo667DJ2i-7iy3ovrH8iZ5krRWxNUQVri91HAoLA_37AuPQsRpn4xZdGco8y9XCKH1TQala9ooYd0tklPImGZcR8gEjRk26pwBFGu3fmQbG0MwxVqznEEBEDrRwzuJMul9cFZWjcd3nz3j1i_JXzNIIrQHymDMr55-G7cOnGLbLk8lxr_ZsmFW86VfDItVmVuc5CCSw-JF0tzerKSa15pZTuiTFvIwSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لاوروف: ادعاها درباره برنامه هسته‌ای نظامی ایران «بی‌پایه» است
وزیر خارجه روسیه:
🔹
هیچ مدرکی درباره تلاش ایران برای ساخت سلاح هسته‌ای وجود ندارد و این اتهامات «بی‌اساس» است. تاکنون هیچ مدرک معتبری ارائه نشده که نشان دهد برنامه هسته‌ای ایران به سمت تسلیحاتی شدن حرکت کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/656317" target="_blank">📅 12:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656316">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abae735a11.mp4?token=FWMjDAkzPM0zT_nm_n_idSkP2BDz_TRmPbOhmY9gnu_671Og1NX1S42ZilaqZtlVMpGhy-HOFuG3w3F_HDVHwvsAHdlQb4LSELWuU1YZ8wdo8c4myop9YW33EDsUKQMLpbyaUaD1vbBaz914uOtAZGb-t50zX9OgNAZFRI4FrLcb-CvWabp5Egp_frEfifAy5ifNOCscUPnWPEnyLKczcz2IudIF0Gy7O4Wr9Jn8W1U9RD5deOdqeRR3NtVv8zt2uI-K-baHCxf0mP7kKMwGRTDiDwelOQvJsjXeAEvs0E6BLgjEhxK0eZMMTbtTqlbkCKMEbTTqcgmBlHg2X2utpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abae735a11.mp4?token=FWMjDAkzPM0zT_nm_n_idSkP2BDz_TRmPbOhmY9gnu_671Og1NX1S42ZilaqZtlVMpGhy-HOFuG3w3F_HDVHwvsAHdlQb4LSELWuU1YZ8wdo8c4myop9YW33EDsUKQMLpbyaUaD1vbBaz914uOtAZGb-t50zX9OgNAZFRI4FrLcb-CvWabp5Egp_frEfifAy5ifNOCscUPnWPEnyLKczcz2IudIF0Gy7O4Wr9Jn8W1U9RD5deOdqeRR3NtVv8zt2uI-K-baHCxf0mP7kKMwGRTDiDwelOQvJsjXeAEvs0E6BLgjEhxK0eZMMTbtTqlbkCKMEbTTqcgmBlHg2X2utpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار مهیب تانکر حامل سوخت قاچاق در مکزیک
🔹
انفجار یک تانکر حامل گاز مایع در مکزیک آتش‌سوزی گسترده‌ای ایجاد کرد و ستونی عظیم از آتش و دود را به آسمان فرستاد. این حادثه موجب تخلیه اضطراری حدود ۲ هزار نفر از ساکنان مناطق اطراف شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/656316" target="_blank">📅 12:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656314">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfwnwXKGqOlAbx0Br8O1zSogaITo4_zHrTXAMmUJJ1u5Dmr2q_hMq_qua126Y_PwVyvicoS2SPkDKwifPM8biLzX-W9TtRsWjYsrG4qmExwCGyurGnYX7kpnOJjlawax558ZbDGVyB-HTKkvZoKL6HwUDDKoIU2C_dkNXFBiNKttpcoZIqxGwpvtbDbAvDDNQXvOMZZN2e5MYojj3_YEy2pK_ER-RXRtNMEwdAavZCMG7IEHGdj0x-9H6nHR0a6tmyYSUz211H4pT1TcEUyHCN2njpuemL14HLgKVUA-ABssZdHtsHWNk0PEEEn6EjlngMBW9q_jTTqCXE1PedMB_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JaYmntl1vTT9wG6TK63O4ZASl1Gd9cejXka4Zl-nXJbb2cRSZ81f2MasA7K_-PCJWx_ZGZrvIEBxDX7cvPrv_1zxANF4lmfGVkZSelLR7DMoo-eAszqLLJK3aC0-921iHfxcNnicLGUegz10gTdUTmZJ1tVVuFLpfLlMBZY_Rft-GTP0Jd5IRFA6e4D9BsDNkBZke_-blqHJqqk1OLZTexnoN8pncI9izWTrI5gaUMMgsum2xtMY_ukqJR5bAOO1S8h-_9kOCZ8e4YnJ0RHvKszJY61ozDO3Hf8GpjgJ9FJsmIBdoTmAUGuxSuMeXTM5oASbwz9qiUOb-ZRC4ZPa5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نخستین اطلاعیه‌های ستاد تشییع و تدفین پیکر امام خمینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/656314" target="_blank">📅 12:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656313">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
تاج: انتظار داریم ویزای اعضای تیم ملی به زودی صادر شود و بازیکنان با در دست داشتن ویزای آمریکا اول به مکزیک و بعد به آمریکا سفر کنند #جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/656313" target="_blank">📅 12:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656312">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/010c76d2c7.mp4?token=E9mjGTTxDOjccMh3K1Kb_Cj5V1LiCHNfpvjPb4LkEc2nYVYJL5816B-cwZAdxQ_ef6lZZ8VLLeveT6dFChYezPQ49cISAsZNkM-A_zQhXbEFF_ByYqr70Kp7y_gZ3RtqGorCKims3quqQNtov6JIT2ddvLtM9d2g9Y5dmQGPA6rkaHEytiO1IdFfs2LzOrt6AYZyr18EF5HcsYfAby4GLKgU4pvpLhbsWm7Rp26ES09YfGDksTRYEz8aJkpBzX4wjpJZNQAhXQEuHOuY1DmDpkiOVEwlMiG74n67JY5JW-ZXg6ibL3MCpr_jxPcXtD8-9nl9Lh34J0V45fDju1UOwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/010c76d2c7.mp4?token=E9mjGTTxDOjccMh3K1Kb_Cj5V1LiCHNfpvjPb4LkEc2nYVYJL5816B-cwZAdxQ_ef6lZZ8VLLeveT6dFChYezPQ49cISAsZNkM-A_zQhXbEFF_ByYqr70Kp7y_gZ3RtqGorCKims3quqQNtov6JIT2ddvLtM9d2g9Y5dmQGPA6rkaHEytiO1IdFfs2LzOrt6AYZyr18EF5HcsYfAby4GLKgU4pvpLhbsWm7Rp26ES09YfGDksTRYEz8aJkpBzX4wjpJZNQAhXQEuHOuY1DmDpkiOVEwlMiG74n67JY5JW-ZXg6ibL3MCpr_jxPcXtD8-9nl9Lh34J0V45fDju1UOwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه جالب در نشست خبری رئیس‌جمهور مکزیک با توپ جام جهانی ۲
۰۲۶
🔹
در پایان یک نشست خبری، رئیس‌جمهور مکزیک، چند توپ فوتبال نمادین جام جهانی را به میان حاضران پرتاب کرد.
🔹
در این میان، یکی از خبرنگاران که مصمم بود یکی از توپ‌ها را به دست آورد، برای گرفتن آن به سمت جمعیت حرکت کرد. او در نهایت موفق شد توپ را تصاحب کند، اما درست پیش از آن مقابل دیدگان حاضران تعادل خود را از دست داد و روی زمین افتاد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/656312" target="_blank">📅 12:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656311">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
تاج: انتظار داریم ویزای اعضای تیم ملی به زودی صادر شود و بازیکنان با در دست داشتن ویزای آمریکا اول به مکزیک و بعد به آمریکا سفر کنند
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/656311" target="_blank">📅 12:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656310">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGjDHueXSGybar-EOEh5fYbDV4kUUM5SfNvEVBvv7-bLYRqXpEmTpKcZNdWzOMDKKmPfb6cvS6DEBtH1B5P7CLg18hW3-NDdCsGNzxg3bTXG382hQai_QktCNXwducGZF5bvv0-vLHZRE2T7ziSpkZfQLjI8F2o06O2OHRl4a72CblnPNU5GzQQJC26bXS-M3Mk5v35RFDeI243L77wT3FglgV_AGxchnZCaH4_dUlQfZ2MZmWGC_kVZtpxcNL4l9JXkcRKyPVhBKWX8x2t0EUrBUPctCndaczUmkWtgGDR_iCdrmq55fuaEjZdTPvXaw110uEPpcTEpCpSkiVDl1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش اسرائیل در پیامی برای ۶ شهر و روستای دیگر شامل الصرفند، تفاحتا، البابليه، قعقعية الصنوبر، المروانيه و السكسكيه هشدار تخلیه صادر کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/656310" target="_blank">📅 12:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656309">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de025c702.mp4?token=M_irtnwxH_4Be3Hde_r3uvUfR_uwifDTGkAVmc3F51Jtz02-6VNksM6ayYjBeRuRLprUMIYqvxVPt9G37IKQdCAbCEqv4UAu1YilOHtmR3lCYMaWIsxw7s8j9-hNonY0Rrz9Eogalc6mFWg5dSe7i8om1wfPU9jkAK4bugZTvGVDFYa_BXgkFBW6QPNRw3lAbSWlkmtIL7eEI3X_ciyFe0PZnA4iMsTfB2iwQhbNzycrHGQ06WZNXposWGeHBZX2QlrCidlFEbUm3IRS64M34mrxHJje1Q_FS_fPE3PD9_zel2cxZy5rEnUMKWH5IYQR8angrDVgvg7cdWbwDNcpFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de025c702.mp4?token=M_irtnwxH_4Be3Hde_r3uvUfR_uwifDTGkAVmc3F51Jtz02-6VNksM6ayYjBeRuRLprUMIYqvxVPt9G37IKQdCAbCEqv4UAu1YilOHtmR3lCYMaWIsxw7s8j9-hNonY0Rrz9Eogalc6mFWg5dSe7i8om1wfPU9jkAK4bugZTvGVDFYa_BXgkFBW6QPNRw3lAbSWlkmtIL7eEI3X_ciyFe0PZnA4iMsTfB2iwQhbNzycrHGQ06WZNXposWGeHBZX2QlrCidlFEbUm3IRS64M34mrxHJje1Q_FS_fPE3PD9_zel2cxZy5rEnUMKWH5IYQR8angrDVgvg7cdWbwDNcpFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و احوال جسمانی‌ ناراحت‌کننده خسرو احمدی، بازیگر سابق سینما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/656309" target="_blank">📅 12:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656308">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: اسرائیل در دوره جنگ علیه ایران به آذربایجان نیرو فرستاد
🔹
شبکه سی‌ان‌ان مدعی شده اسرائیل در جریان جنگ با ایران به‌طور محرمانه نیروهای ویژه نظامی و اطلاعاتی خود را به جمهوری آذربایجان اعزام کرده بود.
🔹
به گفته دو نفر از این منابع، این نیروها…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/656308" target="_blank">📅 12:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656307">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: اسرائیل در دوره جنگ علیه ایران به آذربایجان نیرو فرستاد
🔹
شبکه سی‌ان‌ان مدعی شده اسرائیل در جریان جنگ با ایران به‌طور محرمانه نیروهای ویژه نظامی و اطلاعاتی خود را به جمهوری آذربایجان اعزام کرده بود.
🔹
به گفته دو نفر از این منابع، این نیروها از چندین مکان در جنوب آذربایجان، در مجاورت مرز شمالی ایران و نزدیک‌ترین نقطه آن تنها حدود ۶۰ مایلی (حدود ۹۷ کیلومتری) شهر تبریز که اسرائیل در جریان جنگ به آن حمله کرد، فعالیت می‌کردند.
🔹
دو منبع دیگر گفتند که یگان‌های ویژه کماندویی نیز در این مکان مستقر شده و مأموریت‌های اطلاعاتی و عملیات پهپادی را انجام می‌دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/656307" target="_blank">📅 12:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656306">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWjoS3B37WhrZgippOb8UM0VkkV7_K8-6dJ6TlAtVb7xpAFJ8hsxFkL96nCDFWcN5ErRhr9Pkh3KIiVE3YnglYSUQFQmhtn7hMcliyUREYuWt7H5UhdDDs6bHaW7Y58VRHI_c0VFaFhBnn3fRlFVPjgrkcdm9JtvcVRt1W3uQ_7SAp-MssrgPGYUDkXe64PMe6M3-5e6_et9_5DRpgeMsfjkGKAu2kVyBhbwN6-RAPalXOeEWIR6tCUTqHHl-R3zc6jXjIldJiKNevOujI9yU2qnIKhY6PNoLxsXZ0bddP86NwWLfgJ6Q0x2jDT8OjAZsTS1m9Q3tU0mx18mPI7ong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سوتی اطلاعاتی نیروی هوایی آمریکا
🔹
نیروی هوایی آمریکا عکسی از عملیات سوخت‌گیری جنگنده‌های خود در اواسط ماه می منتشر کرده و مکان آن را «افشا نشده» اعلام کرده است.
🔹
این درحالیست که در پس زمینه آن جزیره مصنوعی پالم جمیرا مربوط به دُبی کاملا مشخص کرده که این عملیات در آسمان امارات در حال انجام است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/656306" target="_blank">📅 11:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656305">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
اسرائیل برای سه منطقه در جنوب لبنان دستور تخلیه صادر کرد
🔹
با وجود آتش‌بس جدید در لبنان که از سوی ترامپ اعلام شد، ارتش رژیم صهیونیستی برای سه شهر و روستا در جنوب لبنان هشدار تخلیه فوری صادر کرد.
🔹
به گزارش الجزیره، در پیامی در شبکه اجتماعی ایکس از ساکنان…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/656305" target="_blank">📅 11:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656303">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/COcJbpb6qHa0SSQjkixMTkfajpKn4WqCmARB0XFoCLSa_BvDjDuxcx28gTelWozV5ernBeHTOX86YDzOX_xTtoVoqbnF8GWzL9iPDWIEDxtJ9qGkm2eA-GXI87KgcG2ou4c96FsYlUvbYaA3bnU7R_KIwEW0l92lrW8jviDP-xmFIjBiYLpUv7zhtcQG3IPySmOVvCviV3dCeTEVXFOtH1ATIGtTHi2ddVK5TuT7sfAd0jVWMD0wpr083n114NuOWCyp7FiV76kvD5nzsQgEw5KcNiVEKOj0Rf-zIdhLSk0KGKnmIXgjJr43nqW2u3zhG8ISxIJTK9vfkNeSmlLO5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zr4jHf9MVTqpoFwcGvfh8k4Vcux8okk8KMr4ZhK5NTaL4p_-TW3oGvMvK_K7eFXbueFs3R8JXbPIcrL5QVlyKCjPH-qqmWZHb-Ks2OTVeLRHMaEC7ydDpgwO8TKIpgaEwoJGIFcuRQwcGBcDiWl4AYdklnvfB2uPCAD3Z0vMa4UwLLD5HyXfItVzvlWphXWBDxeNjcNAjxyXfj3GkOeNJgMYoigLvjkFHUjtvOtJFnOco5Mv27UzYA48t3mJiH7HrzK9KCXVNCKEhQTWpriLtf4s9yNukmi8ZzowJmmHDzBZj9iByNOJhvRGDOwW0qeINsc8WKwNToCUHcytzP8nIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خلاصه اخبار سیاسی، اقتصادی و اجتماعی هفته در یک نگاه
#مرور_هفته
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/656303" target="_blank">📅 11:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656302">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JldT1X_SeyM0_k0RVsggXhuG81YObPwsTytYCVLlajtR6rHdW3RL2ELPv0J6ILySvG28cddPq-zTrPQt4JYxX4uruREVzsh0zWwT6Nq-cyfNiMwFUZHd51koKQf7kjKx9jexJpn86O3z5g4XFHdj6hGNIi7h_1S_hUtMRnppWTYFBKr-oB47R0-4srsqHTB51mokr_nBnQR5n7wUmuliANQ0anyAKcOIGObpyTNhcFY1qZryJr325KlgLI2yrwi3RgDd0ny_mQzyR_KHQXOPHYqdZseYyBhOsG-8MGNl1YEsEjpjYfexUHL-bdgoyXwj_eiPqMbRLCdUCn-EwCl-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعرض رئیس جدید موساد به مسجدالاقصی
🔹
رومان گوفمان، رئیس جدید موساد، برای نخستین بار پس از تصدی این منصب، به دیوار براق در مجاورت مسجد الاقصی تعرض کرد و آیین‌های تلمودی را به‌ جا آورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/656302" target="_blank">📅 11:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656301">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndrxDNCi6Ypy2rRaevMuc66R3aSX0RKHC4U-LvDsgujDbaHW-qIt6kx4VoETnOMrOXw3NY0OmP33orbRzuTDN9jzkkNR2KN1nNqez2-JQ25cCmQAjAB3nXJ3AjauXRev_5Mw4QBnyiqLUJ6RRyiVUr10G1CmqLmIhbcCqJ-UXxW9pPxci62Oq1dr3TKTiUFwjfuS6QvivWlh-JThhl26J8dL70PS3dcHidUzuhDkGlLPvQigArXZPuRCfEKwswJbPh1FMUijq9hpHLb4_vCaDRsW-rM5PVG1EZ8mkz0FiOYkcsr8imUV7qjhbySIw3SgjppIQhYNzFT5N6EwiQUr6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/656301" target="_blank">📅 11:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656300">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42b1f3b02d.mp4?token=mNakMuWE0qDkljF1LdIcG6_abF6wQByBGe9nn8yrsnUgxs4DHiDlaQpJQbG1Hlw-aTKlym_EPvUkPM6EijF7gVLD-wlAF98F6ni3lzhSp9EsOTddfos5yh-VaIHgHnHmGPzMFGb3hMmYjURqAEQionUKMy5cjaRo8OVPXDIkzfHtCjSpu0cn8KQ19PiZKCNEjRdO5iL9veQLO3RAq4dC3vOMHLdvEvb5HYsLxFEK8TiMl6vjhUAsQboPLTx0brOVVRk3gNJ_R3w_w4RC-MpxsGYfi5oPHlvGwncEQAwyyG59R0vnLoG4C_fZnPjTKfoz5DpVI38lv7LtqjueeU19xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42b1f3b02d.mp4?token=mNakMuWE0qDkljF1LdIcG6_abF6wQByBGe9nn8yrsnUgxs4DHiDlaQpJQbG1Hlw-aTKlym_EPvUkPM6EijF7gVLD-wlAF98F6ni3lzhSp9EsOTddfos5yh-VaIHgHnHmGPzMFGb3hMmYjURqAEQionUKMy5cjaRo8OVPXDIkzfHtCjSpu0cn8KQ19PiZKCNEjRdO5iL9veQLO3RAq4dC3vOMHLdvEvb5HYsLxFEK8TiMl6vjhUAsQboPLTx0brOVVRk3gNJ_R3w_w4RC-MpxsGYfi5oPHlvGwncEQAwyyG59R0vnLoG4C_fZnPjTKfoz5DpVI38lv7LtqjueeU19xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک ربات انسان‌نما در جریان نمایش کونگ‌فو در باغ گیاه‌شناسی ارومچی در منطقه سین‌کیانگ، هنگام اجرای حرکت «لگد پرشی» به شکم یک پسربچه تماشاگر لگد زد و او را نقش زمین کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/656300" target="_blank">📅 11:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656296">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKwfXJO54a5EoX9g1GTU6CacFvEJRyQqB0qdNAUhMrBbvJVGr-fkFNq7EPxMAp2TP4MndI5t8HwIgrSAzJU0kOl8VCTONwQARyotwwWPIntQ-RK-2xnGOsMhTNvOEE6HuEKsZq5ql3NsZ-f2i327i4d-zofsTgKRjP4Dbbh-0ZaIYWwWxuYkS8SSLqxlk1AfVLLjhtac5SP_R71IGcAcd4VFmWLupsSemcFRTB8hZQhLXWD3Lj4t8PpQf9Wu-PCLI5buCONa1_3H4p8Mx2_59iNIo7o-VCabPE4G86jxGxMTsu3GrMFMnGQXk1D2fMBIoELth9p2qKLAtJUp9luX9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntUgxLUXFTXt3_TNSmZVeGvSufO2M4d9WT7uqqIblQOYXAq9k0piObkkkdVb922Iz3CfKC4o3r237XYuvv-wqOrqeB3ILkmRec2OWGqg-7Mlm5DLXDeIMmjWYO6OeYZE-qC3J3_OgTTRXeDUmDfoqjAPNon2zZuzonLRerOe-hQ41asPs6z2xoEIRvGu-D3lCNwYQgOw39qaionPzL9nGOk5nrbQ7wbImglOW8Dp39dT3a11mA7Ip_jNBhDzJePkUXiL3GHiNnm_2BqU7uLKVQoHOf7OEgeM2H9QRXP_r9L3m5yDNKYitVETdJwkyGzN3u8Gb5uUvvhjRNgUakobMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hYNzx3xBJsIbteLe0caM3CS7wXdAXS4ekP8Spq5miFyT7JvzPzg-_7GeJyLvtnfxEzk7-_54JCTxL80OZxOWPwwHoJE8iP1jiEo6GP4TxUhVZx0rJa3YrpkrfAWyntSzOls2JgpTGK-xnXA6qUbqkJeJ7wld6JEhpTpinXtfhlNrAx2V6UNxYyk7QcREWs_GJgb57ZB4ufxw3aoTSmIz7vk6NYskX7tv1uy_k0D9ShAgRVS2lieCr5ejgTzWAxV3dIOKepiDkcE4qJ-PWvcofra3FwmyihxiDCMaSX2_P2APHQ-QFKBFMyf8fbQJ6BBSXUDgxkOXRf7laSsXx0PxSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZLf7cWcfOTMbA8ZLX0i1b5RhqzhoPnO3WBQH-8K_Q9UunkyJqN1o_q_qlLTEuFyFVUDWtCk3vd_HYXWgaQjMXtEiNppd53VCEjONwC46ZF5o9OQQdGK1HFfVkwWDULHL0qHCpWieaTbEf2kmPu7VfGu5OjpWxixbcyx9sNI6DOTWwF5AX-ZBEXlDSfAa9Kb2BsGoxQKbcGbZFwp8JYdVUG_Rzz-koSOFOADxgV5-smbqRW5LcdvQycA8Kntt7QdLl31HkN_qKQZ_0Dkb52xQiQjtqFJzPGydHtWPCvwp5SzZOetlFdppfyqYwfdH3JTxz9A0N5Y2hj5vpWrE_F_ung.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نمایی تماشایی از وقوع طوفان در داکوتای جنوبی آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/656296" target="_blank">📅 11:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656295">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
اسرائیل برای سه منطقه در جنوب لبنان دستور تخلیه صادر کرد
🔹
با وجود آتش‌بس جدید در لبنان که از سوی ترامپ اعلام شد، ارتش رژیم صهیونیستی برای سه شهر و روستا در جنوب لبنان هشدار تخلیه فوری صادر کرد.
🔹
به گزارش الجزیره، در پیامی در شبکه اجتماعی ایکس از ساکنان چندین منطقه در جنوب لبنان خواست فوراً محل سکونت خود را ترک کرده و دست‌کم یک کیلومتر از این مناطق فاصله بگیرند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/656295" target="_blank">📅 11:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656294">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c003bf26.mp4?token=a3824weWZBYHZpQHX-3l50e__wraiN1K6UQks6a1Wi7k5LKarjiGBUfv5EL4XGVWBOeBgdtsjSr9mSM_o_Y1PMAT3dgOjsAgDU0Sn7yd_NcjqZ9kSK4yItDR8jO0_6B47TlZouvTFNqfW5raVRvMvJok8kxt4BsRH9USIKz9ojnPNSqVRQsdvxYG1-Zw7ara0jSgT4les6omiE3pX19-ezjy-Ln3H1CRa0NgZua9TBl8QGnUse3qzYpHrvHCa39OJtVggikTGnaUvB7qziFSuzcWQ1LSXw_BS8mGhbu3Q7iDFZo6He5YXZkOBSzOrmjXr4cflBfR14320DGW3b4nAgLrhZjLpVS-sBJKQiQGmhadFUUwZY5bcUWcvaH7aJq36oXY0Tz9bcncDp_XUXUc2qRWjffCV2tbOvgsfjLQazMAnbvcZeey-uGjjF4tf3qShrdVhD7J5ULSGms5nGUa8hR6W7gracIT1vvsHk7nzsM5nksrfh8fcHy-zysuEEQ7d5OyfgcutbacwCYeG4vTISDaoeK1Q4Z21UxrdIgrIQ3LB6pnsouwHCxS4Px-aG_qI_KpAy9CQ96sfea-IrWrdrzp9EG5JlumwuN0HLLgV8JmohDAiqKLXzWG5yuKXDGDhlPE3YIN4IioJf9JW4l62X7POjxXu66_YPhLf0LOCj0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c003bf26.mp4?token=a3824weWZBYHZpQHX-3l50e__wraiN1K6UQks6a1Wi7k5LKarjiGBUfv5EL4XGVWBOeBgdtsjSr9mSM_o_Y1PMAT3dgOjsAgDU0Sn7yd_NcjqZ9kSK4yItDR8jO0_6B47TlZouvTFNqfW5raVRvMvJok8kxt4BsRH9USIKz9ojnPNSqVRQsdvxYG1-Zw7ara0jSgT4les6omiE3pX19-ezjy-Ln3H1CRa0NgZua9TBl8QGnUse3qzYpHrvHCa39OJtVggikTGnaUvB7qziFSuzcWQ1LSXw_BS8mGhbu3Q7iDFZo6He5YXZkOBSzOrmjXr4cflBfR14320DGW3b4nAgLrhZjLpVS-sBJKQiQGmhadFUUwZY5bcUWcvaH7aJq36oXY0Tz9bcncDp_XUXUc2qRWjffCV2tbOvgsfjLQazMAnbvcZeey-uGjjF4tf3qShrdVhD7J5ULSGms5nGUa8hR6W7gracIT1vvsHk7nzsM5nksrfh8fcHy-zysuEEQ7d5OyfgcutbacwCYeG4vTISDaoeK1Q4Z21UxrdIgrIQ3LB6pnsouwHCxS4Px-aG_qI_KpAy9CQ96sfea-IrWrdrzp9EG5JlumwuN0HLLgV8JmohDAiqKLXzWG5yuKXDGDhlPE3YIN4IioJf9JW4l62X7POjxXu66_YPhLf0LOCj0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دست برتر پهپادهای ایرانی در برابر سامانه‌های پدافند هوایی آمریکا
«محمد الصمادی» تحلیلگر نظامی و استراتژیک:
🔹
ایران راهبرد خود را بر فرسایش، پراکنده‌سازی توان دفاعی دشمن، تحمیل یک نبرد استهلاکی طولانی‌مدت و همچنین ایجاد فشار اقتصادی، روانی و سیاسی بر طرف مقابل بنا کرده‌است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/656294" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656293">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
دبیرکل سازمان ملل در بیانیه‌ای خواستار عقب نشینی رژیم صهیونیستی از مناطق اشغالی جنوبی لبنان و احترام به حاکمیت این کشور شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/656293" target="_blank">📅 11:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656292">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef77db9be.mp4?token=cCb07-n44sdvi3wvWsqGJ5zyQK1QS-_tnxLLH6-uk3EMwl5YmUEQfRICTlModIo6WKQYesV-kLns9BUT6JdtYVgcyBWSXlX4OgXcC9iChkmlQ77_bxTN67a9Ayx5ADiFZdN1cNfCz8AHqxTohM77W-I5sX_JVwYEzkjfRemfR88nhpKDwswKbTCvvfjI5nULnk9G7IpKvaNM_J3AZfcEJR4HBkWYJFvU0Jt8Qaq-qDAxF8DIxjN33VeaPP9EEtYeFNoKfSGnZYMMP61YjfDIbu-bFugGugL3c1_ai9b50oWf9mPW_JPnxT3rMr0grKkPVlh32JSfrY-a1dyk5_2LZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef77db9be.mp4?token=cCb07-n44sdvi3wvWsqGJ5zyQK1QS-_tnxLLH6-uk3EMwl5YmUEQfRICTlModIo6WKQYesV-kLns9BUT6JdtYVgcyBWSXlX4OgXcC9iChkmlQ77_bxTN67a9Ayx5ADiFZdN1cNfCz8AHqxTohM77W-I5sX_JVwYEzkjfRemfR88nhpKDwswKbTCvvfjI5nULnk9G7IpKvaNM_J3AZfcEJR4HBkWYJFvU0Jt8Qaq-qDAxF8DIxjN33VeaPP9EEtYeFNoKfSGnZYMMP61YjfDIbu-bFugGugL3c1_ai9b50oWf9mPW_JPnxT3rMr0grKkPVlh32JSfrY-a1dyk5_2LZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقال هندوانه با پهپاد در منطقه کوهستانی چین
🍉
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/656292" target="_blank">📅 11:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656291">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
نشست مشترک نمایندگان ایران، چین و روسیه با گروسی
🔹
سفرا و نمایندگان دائم، ایران، چین و روسیه در نشستی مشترک با رافائل گروسی، مدیرکل آژانس اتمی، موضوعات مربوط به موارد مطرح در نشست بعدی شورای حکام آژانس بین‌المللی انرژی اتمی را مورد بحث و بررسی قرار دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/656291" target="_blank">📅 11:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656290">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7WhixmSKPdT49vw1GeEft-rec-CAUKK_MZI4BHN9jsUII3Vr1ChDipRVEwcBGlSGWE1l3kIRNrhRoYnlBgR4k7sCb_RRzkxhM57jjmR5FlH1wfhFb3JYY0_WJIW0z2KfnA0lTwLQnenn682pu0uMGZandRBLbqGtXb-CBpZWNAu6yX7iavRtls3Sn4IoNrnku8o_0do-3-wKn14UVUrwwLdfHMeDRW0J7qG59VNsBvs7IO664uCz2meLly3NYiObvEd3y02lkWLJb_bl4HPvzGNV1yZu-B2zj-DHUsWAPtJJet0tE4A2BLR04ri9wRpjOPxajOYPSYS7Ta0yySy0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه‌های لبنانی خبر از ترور حاج آدم عبد الحلیم حرب،از فرماندهان یگان مرکزی نبطیه حزب‌الله خبر دادند
🔹
پیشتر ارتش اسرائیل اعلام کرده بود یک فرمانده واحد مهندسی حزب‌الله را ترور کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/656290" target="_blank">📅 11:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656289">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f4873087b.mp4?token=o3RoKjVi4Qs24I6eUKyASNYBTuXVLhbBSCcew9mcnA1bIQYsUTRD1tOtrC4gQ3tCj8OJWHKOTq6CsfmwXyGHXKDFXVECbkT48GRlYzXc5ssdyrZbbvayYpBrAF5IartzGsJuwidHxKor7XAfemr3g-ckkCjVAi0zV-YsyHRq99Mj4XC_hiIYtXhyO8D65I7azpqplbtCgw2oyo4DPSgulA-GY_F1-27-_m2N00vsHkK87J1DmLhShts353GQmhw_D258ozpCQvBNb_6zgbwCmDsOqhHIPN3QSbb0O7BVKgj9wuqqVGU353QI1XNFwzrsKNF9GJZseTwpuDhRjbEHag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f4873087b.mp4?token=o3RoKjVi4Qs24I6eUKyASNYBTuXVLhbBSCcew9mcnA1bIQYsUTRD1tOtrC4gQ3tCj8OJWHKOTq6CsfmwXyGHXKDFXVECbkT48GRlYzXc5ssdyrZbbvayYpBrAF5IartzGsJuwidHxKor7XAfemr3g-ckkCjVAi0zV-YsyHRq99Mj4XC_hiIYtXhyO8D65I7azpqplbtCgw2oyo4DPSgulA-GY_F1-27-_m2N00vsHkK87J1DmLhShts353GQmhw_D258ozpCQvBNb_6zgbwCmDsOqhHIPN3QSbb0O7BVKgj9wuqqVGU353QI1XNFwzrsKNF9GJZseTwpuDhRjbEHag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش جالب امام خمینی(ره) به تمجید آیت‌الله مشکینی از ایشان
🔹
ما آن قدری که گرفتار به نفس خودمان هستیم کافی است، دیگر مسائلی نفرمایید که انباشته بشود در نفوس ما و ما را به عقب برگرداند. شما دعا کنید که آدم بشویم. دعا کنید به ظواهر اسلام حداقل عمل کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/656289" target="_blank">📅 11:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656288">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bead13e540.mp4?token=bcAoCnrTzRZiRCs1FbmW2NMW2sHZMkIKM8oypuEMIKdN-fGxVNnB3uRDSyKBipBVN_Oq164-DMcpl_VjazyrekjoV7hmgG3JAbUOVThi88n89OHkK5UvFrfj5rs__R-6ikK-Odt3EN0JW2CEjwdcl9XdYMDtiDzQt2sZO4BPsACEB_GwTDAT1uwkhZaV66t-OmeCTTBdwU0pL2NIVdqoxRIwZ9qajlZ84LJUKXDOCPP5ChrjRYW_xWJcafP8OGlpgnusUPaI23sea4N5jXlqEdxXXmcmwqQvSxr7QUVS9VxkSsvRXH2QXnBwJOSNYPH1_le5f3AH4yM14q72IFS10w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bead13e540.mp4?token=bcAoCnrTzRZiRCs1FbmW2NMW2sHZMkIKM8oypuEMIKdN-fGxVNnB3uRDSyKBipBVN_Oq164-DMcpl_VjazyrekjoV7hmgG3JAbUOVThi88n89OHkK5UvFrfj5rs__R-6ikK-Odt3EN0JW2CEjwdcl9XdYMDtiDzQt2sZO4BPsACEB_GwTDAT1uwkhZaV66t-OmeCTTBdwU0pL2NIVdqoxRIwZ9qajlZ84LJUKXDOCPP5ChrjRYW_xWJcafP8OGlpgnusUPaI23sea4N5jXlqEdxXXmcmwqQvSxr7QUVS9VxkSsvRXH2QXnBwJOSNYPH1_le5f3AH4yM14q72IFS10w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از این دسر سالم و خوشمزه که ترکیب سیب و شکلاته درست کنین و لذت ببرین
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/656288" target="_blank">📅 10:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656287">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
العربیه: وزیر کشور پاکستان برای دومین بار در عرض ۲۴ ساعت با همتای ایرانی خود در بیشکک دیدار کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/656287" target="_blank">📅 10:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656286">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqIdcdVAQVTr-UaJLAz-3dyMGw-A9d20OgsKDjurVjOKDSoDhs7e2yJZjzMXKsPVM6G954IqWuJTWjtJ6dCGcaCo77LIZRUXVi_lMd_eyCm1Dt6PH_RaqC4m5iEMNm34QAL4hQayXnr0xpbzpmg92JRlVaUICBNFf33hjy0eJQc0KT5Ict5Dtd6E_AElBiD_qNQyhNQvyYca8MO95qbjT_I_H7n0sE3SmJbk3S2zzwShp8NZAB-KhgIQGuATr2UpFXrwIJPwl6SJDZkwu7X9ryonJbMqldu0KR3x9tZ2LB4toxZ2bVVBj7eYJNDcR7zdAqrdkCXkWEYkkDQ6OYZJZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس پلیس راهور تهران بزرگ: تردد اسکوتر‌های ایستاده و نشسته بدون پلاک در خیابان‌ها و معابر به جز بوستان‌ها و مسیر‌های ویژه ممنوع است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/656286" target="_blank">📅 10:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656285">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نتایج آزمون EPT خرداد دانشگاه آزاد اسلامی اعلام شد.
🔹
وزیر خارجه روسیه: آمریکا و ایران باید گفتگوها را ادامه دهند
🔹
پاکستان: تلاش‌های دیپلماتیک برای صلح پایدار در منطقه ادامه خواهد یافت
🔹
فعالیت در بندر الفحل به روال عادی برگشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/656285" target="_blank">📅 10:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656284">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea408e562.mp4?token=nfjEIecc10UQaczbIhwzD-miqAGnPPvq7bsju0iIJSKIEyWWYLjEB86fHve-cfvEHEs5yJThR9wsygC-i2kAfSPWgReEl9qLQsBz968kFZKDHLySWAA0j3j-PsRvwINuNfPP7zhQGkxwK13sGl8aP5mGvxcwyln9wa7fm5JDQWriI1NnbUZCcAn0u4cl-vkg8atHWaY5KJUUN6VEp8gKBqvFHioNA2RWj8r82E8_1kui16N8RqF4OPtzz9mfqkwPxRJ-0TzIcTXKJtSGv3HczaOUcApXqlDXMblbwfb_7YyKlC11fk64pEOXYs1nUC-HfsAlAwGMfXj13HKDiaPxuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea408e562.mp4?token=nfjEIecc10UQaczbIhwzD-miqAGnPPvq7bsju0iIJSKIEyWWYLjEB86fHve-cfvEHEs5yJThR9wsygC-i2kAfSPWgReEl9qLQsBz968kFZKDHLySWAA0j3j-PsRvwINuNfPP7zhQGkxwK13sGl8aP5mGvxcwyln9wa7fm5JDQWriI1NnbUZCcAn0u4cl-vkg8atHWaY5KJUUN6VEp8gKBqvFHioNA2RWj8r82E8_1kui16N8RqF4OPtzz9mfqkwPxRJ-0TzIcTXKJtSGv3HczaOUcApXqlDXMblbwfb_7YyKlC11fk64pEOXYs1nUC-HfsAlAwGMfXj13HKDiaPxuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از اشترانکوه زیبا و باشکوه
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/656284" target="_blank">📅 10:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656281">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4UgZSc45aCGZQyI6nWK6VXtIcGCvsfrv987GqhY-ebU_q4f9LtKtJcipmKzpTlro7ABc3gXIPO5WQE3HgzomXYFUnL3f6lKKOEsdimxVqonUmWmf3wckOnwTKG8AFA8nb36qs9bvGBZnVkLmsUGKeTrUMi-VUqRFGjAiajlaVe7T6G96Cv06GuvYMzWM4ZOvLlVZnNaQ9wIz8xFfVHhLdmudPM8E3yWw-O0QKDo5ZHxT3NfWbpSy6zdS2YhUpvuDtF-X3rDzheal_ILUuCWtsBcmV7noUFHvkXZ--ESf2Sm25ash2TOYo-mCbJGqDKBgRPjAwHXGVeKKuXN_pgQdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f540d5f5.mp4?token=SFiC1owhvqHhyxOGlt7nhCpz-fUDyCXUtXkqz_rB9CdsWvl2ljjduOlFUjPLYEA-ljH8v5Avnjx6S0Ty8fDlnL8Kzi3hmCbx4NqVhmNBZyjAIm7tgxkdTR7Urfq9UhcIUM2IlLLUmqqo4grlEmSkRt97PUSd4wi0uke4z7_LdNQs1haxZGkV8so8rBRK2V7kuNGFx-F0wLZgpqJoqJp8T3iwdcYXwMAfivrUZvuO-wUZR3SbzPSxTgH5uatEEZw5UYa1EyfrP8BaO_hcZr5LAPuWx273YrwI-DyZHdqjVORenPf17kzWuvkqriB17MmxzDTI8WYUE_-MW-xoj5zvAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f540d5f5.mp4?token=SFiC1owhvqHhyxOGlt7nhCpz-fUDyCXUtXkqz_rB9CdsWvl2ljjduOlFUjPLYEA-ljH8v5Avnjx6S0Ty8fDlnL8Kzi3hmCbx4NqVhmNBZyjAIm7tgxkdTR7Urfq9UhcIUM2IlLLUmqqo4grlEmSkRt97PUSd4wi0uke4z7_LdNQs1haxZGkV8so8rBRK2V7kuNGFx-F0wLZgpqJoqJp8T3iwdcYXwMAfivrUZvuO-wUZR3SbzPSxTgH5uatEEZw5UYa1EyfrP8BaO_hcZr5LAPuWx273YrwI-DyZHdqjVORenPf17kzWuvkqriB17MmxzDTI8WYUE_-MW-xoj5zvAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنجال بزرگ پروژه لوکس کوشنر و ایوانکا در سواحل آلبانی
🔹
پروژه تفریحی لوکس با حمایت جرد کوشنر و ایوانکا ترامپ در نزدیکی تالاب حفاظت‌شده نارتا در آلبانی، با موجی از اعتراضات مردمی و فعالان محیط‌زیست روبه‌رو شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/656281" target="_blank">📅 10:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656280">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlSbN6JuGHq9M9Hwu-GnsBz0R9zcHS4J1kiXBFbTw5_6tauYwK-KorJEMUakDlyabiwxwGEtZ71nKMm6EYojyl1x7BBiW_HrhlJ6racx9oZDcdF4hdA53_k-WGlZRv6qCQF9zO9ZO91tyB9Z-5ld1QgvOdsV-LJ09rJMjdlsvp0a4qUv8OFfkGsOfJqg0TrS-LV_Qxg54ih4zBxvNGbXoqae6LsSTdicyE8l_GLdpjTQBXUD6cxA5UK9VZ080RR0nL9wwQF04Wc3KahB34VHAlAbo4FtkuAeJP46yKIZliBm2xD2X947du-HcRlaxtc_IG0L7GRp8OpWNytx39P3Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تغییرات عجیب و بزرگ فیفا برای جام جهانی ۲۰۲۶؛ از آرایش جدید بازیکنان تا پرچم‌های غول‌آسا!
‌
آرایش جدید:
🔹
هر ۲۶ بازیکن + داوران هنگام سرود در زمین حاضرند و دو تیم رودررو می‌ایستند (نه پشت هم).
🔹
پرچم‌های غول‌پیکر: قبل از سوت شروع، پرچم‌های بزرگ تمام زمین را می‌پوشانند.
🔹
هدف اینفانتینو: نماد غرور و اتحاد با نگاه روبروی بازیکنان و داوران در مرکز زمین.
#جام_جهانی_۲۰۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/656280" target="_blank">📅 10:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656279">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b234d7bd0.mp4?token=W5oiMubNxaeq-ggyiMIVGAkAZQmTEKRks57iiGPpic3sp-_AZeM1QKdBNIWhgn13SM95Z90428bjwnI5qouk46GtmA-xKDWgQoWrFNr9l4gLzMmLXRlFk3F-FFBRu5xNvlttsz7n1Kgqvt812F17266NlbMDx_PcLWMCDGFv_X4OCvuaah3pLb8MpG-7ioGDeZ-4ygzXLog80zswDCG8PuWmK5mMxBdJVcxmjVRbggKKsLXif0awPoHl3Np2RPpXGaUqoOlnTbPA2vTvXeNitsvbP0xhmedLIUYfIhfZzhkh1-DJZoP-BViXR5nMvuhI7YEEy6LZo4a2cvwgr8oQYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b234d7bd0.mp4?token=W5oiMubNxaeq-ggyiMIVGAkAZQmTEKRks57iiGPpic3sp-_AZeM1QKdBNIWhgn13SM95Z90428bjwnI5qouk46GtmA-xKDWgQoWrFNr9l4gLzMmLXRlFk3F-FFBRu5xNvlttsz7n1Kgqvt812F17266NlbMDx_PcLWMCDGFv_X4OCvuaah3pLb8MpG-7ioGDeZ-4ygzXLog80zswDCG8PuWmK5mMxBdJVcxmjVRbggKKsLXif0awPoHl3Np2RPpXGaUqoOlnTbPA2vTvXeNitsvbP0xhmedLIUYfIhfZzhkh1-DJZoP-BViXR5nMvuhI7YEEy6LZo4a2cvwgr8oQYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گربه‌ ایرانی، فرش ایرانی و موشک ایرانی
🔹
یه خانم در بحرین این ریلز رو از حمله موشکی چند روز پیش ایران گذاشته، اما بهترین کامنتش این بود: گربه‌ ایرانی، فرش ایرانی و موشک ایرانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/656279" target="_blank">📅 10:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656277">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ff8fa43c.mp4?token=aODbV-E5zZ0-CWTu5KtHVRcHuQLFpiTD87fgMDOwWsnPlwkzs5sVhIcdBrsHM6Xnd7p0zbXZStlts8Fl-fZBb-xPAHacZ-lNr6x32lIdPo0yPrgzvgOcRXRy0jEIsIuxbKLp6s-uO8YbAN4iEyIThDQyH4Ffu3hrSFYt6qDrvimKEpKFNIFTzrQT06pFai05rkKQxA6sdy08pGNvFoL6blrv57zVJp2wqVpB2SKzNKYpo4jkgPyhwWEQzqXwWjA7PpfLxWs2O7Sga1cnoPQVHRLE5WoPO1_BzN-nURzDZFvhTpD_Vl0yPxlUHxILjFKrg-br2kZOGean2oUcasm3kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ff8fa43c.mp4?token=aODbV-E5zZ0-CWTu5KtHVRcHuQLFpiTD87fgMDOwWsnPlwkzs5sVhIcdBrsHM6Xnd7p0zbXZStlts8Fl-fZBb-xPAHacZ-lNr6x32lIdPo0yPrgzvgOcRXRy0jEIsIuxbKLp6s-uO8YbAN4iEyIThDQyH4Ffu3hrSFYt6qDrvimKEpKFNIFTzrQT06pFai05rkKQxA6sdy08pGNvFoL6blrv57zVJp2wqVpB2SKzNKYpo4jkgPyhwWEQzqXwWjA7PpfLxWs2O7Sga1cnoPQVHRLE5WoPO1_BzN-nURzDZFvhTpD_Vl0yPxlUHxILjFKrg-br2kZOGean2oUcasm3kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرتاب کفش و زباله روی سر کاپیتان اسرائیل
🔹
تیم فوتبال رژیم صهیونیستی در یک بازی دوستانه مهمان آلبانی بود که تماشاگران این کشور در جریان بازی با پرتاب کفش و زباله روی سر کاپیتان اسرائیل از صهیونیست‌ها پذیرایی کردند.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/656277" target="_blank">📅 10:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656275">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHAgzhPneHXl0Kfdfb9a7vtLF9-Slvwg9WH_brIEKG74LjDH07bP4oH-yimCN6qtvSMiZcRj3ULeGUqCGMSFI_CSSIh347FqMFpNW7mEqssGs7jbcZjS7zTxniJDXYAvHNo2CdhmDNimkZ5xQ21ql7H4VQyOWQavW-AYBIdStQj8NbHE93OC922x5geqSv8o8dB4xdg43rCqTRGkDuU9w7JTpbBa25bIdeQ3EJSKZIv7GI4hYxizzUW7b5uv9WTR2WMcdGqaglMw1DqScyCY3rftj7SJ3l0htSrf7ibOUUs5ZamAR268cCCmP49vKoX5GyU7m37__bGHLsdMnAHwfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس‌جمهور چین بعد از ۷ سال به کره‌شمالی می‌رود
‌
دولت کره‌شمالی:
🔹
رئیس‌جمهور چین به دعوت کیم جونگ اون، رهبر این کشور در روزهای ۸ تا ۹ ژوئن (۱۸ و ۱۹ خرداد) به پیونگ یانگ سفر خواهد کرد.
🔹
این سفر در شصت‌وپنجمین سالگرد معاهدۀ همکاری‌های چین و کره‌شمالی انجام خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/656275" target="_blank">📅 09:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656274">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
مرحله یازدهم کالابرگ الکترونیکی از امروز آغاز شد و حساب سرپرستان خانوارهایی که رقم پایانی کد ملی ۰، ۱ و ۲ و همچنین خانوارهای تحت پوشش نهادهای حمایتی و نیروهای مسلح شارژ شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/656274" target="_blank">📅 09:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656273">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osc9pSHtpj1ifnJHXL7eS-r4zZ2Di9Et8pOaTmZfQs63l6YD9QvdtSZ6u5yaPCRpWUtzCct8wKNXV5lUE5LMcD2QaLHHwipfx-U18Z8u4nN1wnjz02KgMjku416XKR8e0wZjPPaB5hHOafQAXOabsdPe2ckWhYHQd3a6vdJ-nupMStUgYEcP9sVqJiLeAjP4CoMbPVBG_z-ZPVGtOFQbY9uouEjYyKgKRrxZmDVRL-AjT-URUb3Vyc8btI8BV1AisuYr177YdlPXnCheitwILvrV4udNz3q_j6vd8Rg2JuOkdmq1DJDFPUJbro8NvNSJ3n67vWwsGzQpzBanUZA1Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دماوند با شکوه
🔹
امیرحسین گوهردهی
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/656273" target="_blank">📅 09:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656272">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c003bf26.mp4?token=pixPHAg4bL_FMcyntG3_B6yyL7cwuU3db6A3Gc_6ZBkJRgBoYJuZ77hALmg3Z4ofM6WJbFf2_ta5ipsbg7iR6bLvT4hBodjrabmRkGSurEs1jJDiOhWMd4h7jU5k9fRhV3q8DKHPyYC1F35ReB-whq0ugHlsWX3tiDJhJcsEfRVKJCBK0SMPIy1s54SfoZ7neiYuITtZ1DayFljyoIEWEm7t5zZGStfU-hnquE04AxYLZ_e8YEVJV72DWs1ZT6WEriZevKcTVcYovxVMKBlqXPGDZv0vEB8r92aBc9gJV91tIH8NAY2wNTo6ojE8Op4gBxF5NsVO7rcE0E8wHDJWQWsfyKM2-V2U6UGdKGTzBYuOnAHmQoMExNMW3VBe_E7_q6cqHM5XSTmoMAGJmh-PuFXGWzqFccnpvGfwFKaq4bcVGeQHnYvhwBgbH1a3Ac94k5NZ-EUm1V6-5nUT5LLyAYpO2CZLw5IYoZ-0rhzgiSxq8ofEub8WrqHF5iolkU0LhYr6bb4bnNDiqaMSsu1j5QqV-SxX-1rLtM36MOz3iYiuiB8yQDpSYZ3YZ8vPxtXzBwwYDjnH5Rt2vczuTKmaULcQXokFkH6W5Xk0mG9OMNP1_0Rt_2iUDIgI3qZkqM5W_7rT8VBJqHGbMc46gzzq54XIokqZjeCLmITUU7rBZ7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c003bf26.mp4?token=pixPHAg4bL_FMcyntG3_B6yyL7cwuU3db6A3Gc_6ZBkJRgBoYJuZ77hALmg3Z4ofM6WJbFf2_ta5ipsbg7iR6bLvT4hBodjrabmRkGSurEs1jJDiOhWMd4h7jU5k9fRhV3q8DKHPyYC1F35ReB-whq0ugHlsWX3tiDJhJcsEfRVKJCBK0SMPIy1s54SfoZ7neiYuITtZ1DayFljyoIEWEm7t5zZGStfU-hnquE04AxYLZ_e8YEVJV72DWs1ZT6WEriZevKcTVcYovxVMKBlqXPGDZv0vEB8r92aBc9gJV91tIH8NAY2wNTo6ojE8Op4gBxF5NsVO7rcE0E8wHDJWQWsfyKM2-V2U6UGdKGTzBYuOnAHmQoMExNMW3VBe_E7_q6cqHM5XSTmoMAGJmh-PuFXGWzqFccnpvGfwFKaq4bcVGeQHnYvhwBgbH1a3Ac94k5NZ-EUm1V6-5nUT5LLyAYpO2CZLw5IYoZ-0rhzgiSxq8ofEub8WrqHF5iolkU0LhYr6bb4bnNDiqaMSsu1j5QqV-SxX-1rLtM36MOz3iYiuiB8yQDpSYZ3YZ8vPxtXzBwwYDjnH5Rt2vczuTKmaULcQXokFkH6W5Xk0mG9OMNP1_0Rt_2iUDIgI3qZkqM5W_7rT8VBJqHGbMc46gzzq54XIokqZjeCLmITUU7rBZ7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ژنرال بازنشسته اردنی: پهپاد ۳۵ هزار دلاری ایران رادار ۵۰۰ میلیون دلاری پدافند تاد آمریکایی را منهدم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/656272" target="_blank">📅 09:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656271">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNAYWa40l9nmadme9Zpd2P28-TtEKErGwwSIY4-HgqldI8gLrwRlM9wGytnLMrQqnb3GngM5XVK-FuxpzWedN9hCKap2dAcQqKz1vAvveGd3beZS2WBkt0Qcm6VJiQR3BcMMHxRt7vCINxs2BCB-UFSWq7uGVFuA9nZcklqX4OJy6DM1m_iDtMxv2JzEHQmlfbGJmJEvAdciAQHJJ1uhIjSGM2b31OXLb3LlJj_y0vLSS-dbE6oJtO0hHCYqABlMywXWVWnCtzdrc_95XgcjqwILQhmTG2IqfQeNI7XLHC6my1_mjltpU_Wy57HDBWOptgQpHqYtRQpiMreVCs68vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir/
نوشهر
📍
دریابیشه
۶۰۰ متر زمین
۷۰۰ متر بنا
تعداد خواب ۴
استخردار با تاسیسات
شهرک با نگهبانی ۲۴ ساعته
سند تکبرگ و مجوز ساخت
دسترسی عالی تا دریا و جنگل
🔻
برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir/</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/656271" target="_blank">📅 09:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656269">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFTq9tWHnV7hEgfU5fgc_zD_gG8KqtDjclGfKvEV7dSSfeUFicniKjEXzu7VEzvD9gpNxUblmMeXY8kNPNZBx4EpKEew9gIsrsGlfavRnAtIWh8eM4PqKp145SCbePqGueLY_w-gUYUexA4URtlpJ-JATGsi-5J4jTdBr0VSq5O0l74wF8AmCZokkj3kL6ZvXV2BFzd55xzQgCKDUxxbkLjhrG0x6OY7jfCyDgF8UyZErVs_pZiTGguQU_gaufdED-44T3PdRsxdNMW1pQ9dYJFSMnb7ixP4dq0pd7qCNjcIRx6QjVtNavzmlatcGRwPuBYOgeUSdgpTyikKFDbIog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس تیمی جالب نروژی ها قبل از سفر به آمریکا به سبک وایکینگ‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/656269" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656268">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpMDlj-Bvr39MQkbpr0ReD-Sw7stbbJm87T_WQeFgpuNQQ3_ejP2jwdyuI5Vk0uu9ziOQ6_u64Z-yaIJIq0F_AMahOvYJbhtNaC_jgBIsLfMF_2XNHOWieIWxxjCiV30Mv72Qu8BSaxcDAlEwa-WW8Te6TQGjJuwVxo_zwRUq0gtfnRQdEceQzrsewis_pSGPfzbpnWlJDq8bTNtfyIV-ZzvyG0_TOZdKXTg1e585Ge6rQw1F-UHBfwBwIVn2u7RQHZdGKtJwsUtgojWELY64PWbyBMBTU4dA01GKBO3ezzzZjXuLkwDfXzY1-joPIIEX0W8jAI5ibJP5fBKBSt53w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش بقائی به ناکامی آلمان در عضویت در شورای امنیت
‌
سخنگوی وزارت امور خارجه:
🔹
ناکامی آلمان در کسب کرسی غیردائم شورای امنیت سازمان ملل برای اولین بار پس از دهه‌ها، نشانه اعتراض جامعه جهانی به رویکرد ریاکارانه و غیرمسئولانه این کشور در قبال نسل‌کشی فلسطینیان و تجاوز نظامی رژیم صهیونیستی به ایران است. وی افزود: آلمان سلاح به رژیم صهیونیستی می‌فروشد، نسل‌کشی را توجیه می‌کند و تجاوز به ایران را «کار کثیفی که اسرائیل برای همه ما انجام می‌دهد» توصیف کرد.
🔹
بقائی همچنین به سکوت آلمان در قبال کشتار ۱۷۰ دانش‌آموز در شهر میناب توسط موشک‌های آمریکایی اشاره کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/656268" target="_blank">📅 09:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656267">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAzA1ShcyjfxJzk4bfmYb2Gf4EkprLA2VWfLnT-jYbezoVZZ53eCsejV3poXUPA7Elw2qjpjuCiVB8ig40ckDUEp1N_mdHUff3QgmgJfyXreiQR_xBX4PQJ5xbKhP-mv5QepfCq9hJBpmbJCHESOodmOSgH8qOCeW5e1nUPyWAGWJMwG29L5FMafqJfUfB_IJI4a1eoDomambr6mFUVzRd2pYC8_o3ckO9AyJ2crH_aAqppB4fwkCwlyEJu2F6PyVFxqVN0inYAeWPvS0uV_ECim94B1DBohftXa_DcAX49TxXWpafYiLOYUJXVRHSyvy9YxgSvQ6_EYOryRWrht8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی: با دیکتاتورهای منطقه به جرم تامین مالی و نظامی آمریکا برخورد کنید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/656267" target="_blank">📅 09:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656266">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95f26bbeb2.mp4?token=M5kBo6WJxADVUiUta3hWexVWLuAME5tAZgVsfYSmevBo0Tx6qBst0zkKHkiOqhHTkWJPtThzh1PI3aP51qYTj-omCiIDtzM022shNfs0p3EP3qKhRf46oHpbX7zISXaZEQBZ1nl0LHf7UQzahCeMmKAi1v5iYXMokKVi8pmX0mkUnYjM6rnORpD1LiJtwyd3kfab25VjAekC-w9dgFAS6e7axPo-mMEQt3RU46Z2xbMBp7S5X-m-EVA4bvB-0cLmIawCweIxTOEnLHVHRenJKVLqmXHFtuRUnGc3q8svuuN0yIYDdLgvmMARUmSd65mnVE6Vak3Y3jVDE0d_cgBM6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95f26bbeb2.mp4?token=M5kBo6WJxADVUiUta3hWexVWLuAME5tAZgVsfYSmevBo0Tx6qBst0zkKHkiOqhHTkWJPtThzh1PI3aP51qYTj-omCiIDtzM022shNfs0p3EP3qKhRf46oHpbX7zISXaZEQBZ1nl0LHf7UQzahCeMmKAi1v5iYXMokKVi8pmX0mkUnYjM6rnORpD1LiJtwyd3kfab25VjAekC-w9dgFAS6e7axPo-mMEQt3RU46Z2xbMBp7S5X-m-EVA4bvB-0cLmIawCweIxTOEnLHVHRenJKVLqmXHFtuRUnGc3q8svuuN0yIYDdLgvmMARUmSd65mnVE6Vak3Y3jVDE0d_cgBM6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بزرگترین نقشه سه بُعدی تهیه شده از جهان هستی، شامل بیش از ۴۷ میلیون کهکشانِ کامل
🔹
هر نقطه نورانی در تصویر یک کهکشان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/656266" target="_blank">📅 09:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656265">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
مرحله یازدهم کالابرگ الکترونیکی از امروز آغاز شد و حساب سرپرستان خانوارهایی که رقم پایانی کد ملی ۰، ۱ و ۲ و همچنین خانوارهای تحت پوشش نهادهای حمایتی و نیروهای مسلح شارژ شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/656265" target="_blank">📅 09:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656262">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dt4SE8LP1O8rHxJKBBR6Aq1a_86oOhDmnkNlkl2129pfl5EiI6la9j9IAQGG-XClusO9VZYhfGzS9HWOKYT7HqRoVsqq22KT3QieuacIh7a_ANBxtj3sIHt5oSfxxsmyaW6tJ1LhcWOHFZIkeMD4gOM_vaAbpoMU8vK4SrTr43C0gcHMJaNfud6sokHT3i0xVVSpvPG9DNh4dKXmpXdQ5SPZo41Spk4GmpFPBT60CPi_8WCoMPfzJ3n9M2916JFzIRgn7WGzGqEoA1jPlEEyNgPRQAnUvF1yzOk7WBgZpO-XPoU9LC_PuAIqHjChEPcgFKsx6khGCCE-3-ANaFk5UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lqhaqeapn3C813_IdKoYML2lKQbMirgFiWqkrlRXrzIsv-Rq1csc5dI4k1tegeDcLSn8aaF0KFNj0Jzep4wEfi3wVeV372KATH2pYker0OKc34ZL7mP0mIogBqXojblLa9SyWARcrgtUpuPQbGFA91w1JJfEepx8RriRpgYAVjFVInieKIYcfu6sDue-5Bb5CbZsnHbEpI1ryOFCGqTy899LtFe8MW_1H1VJR9Uv6TIqdeb7llDbXGo7T5fPzWA2NUDB_oiwGif2PHBAtBansvBJfNkHNDFBCZODnF9AlfT9T42ge89jPKElPv8RGE7E485TA74JIKzCbUEkDSeGjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqZ3Gty7e5lK_kZMQRcTcFBTg7P3u1ChhSrRghZNCQnwAFl6vbwr2MTRdKzk-r_M2E0vCojNMzVp4KjWsuBaaUe9jBmIOIbNBw9eEQNXPlz2L-8FtmUl4IPFv8ubNtyYw6cgdyxJc-uMu1xYF5i_9qKS44LJR_kIPVhNaa1YKzk1GKkLuppCQu_VqLpMD_Apodx0JswT8c6JPTjXJMSTc0tqC61ZMaS25CQRnv59qXP7CFrnR_eMAAGTFe0-6lE_Sd-GSjltkw2Y8TO5cr_EEnBf-H-y-GOBOgfOXnqLyWcUQmwnsCFMaPALYWquPS0OsJA1CYB8sH2x-wIfK9Z4FA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری دیدنی از لحظه وقوع طوفان در منهتن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/656262" target="_blank">📅 09:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656261">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
روزنامه عبری یدیعوت آحارانوت: کابینه امنیتی دیشب به پیش‌نویس توافق آتش بس در لبنان رأی نداد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/656261" target="_blank">📅 08:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656260">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون عراقچی: اصرار ما این است که ۵۰ درصد از وجوه بلوکه شده بلافاصله با امضای یادداشت تفاهم، در اختیار ایران قرار گیرد؛ مابقی آن هم بعد از طی یک یا دو ماه
‌
🔹
رفع تحریم‌ها و مباحث مرتبط با هسته‌ای در مرحله دوم مذاکرات قرار دارند./ مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/656260" target="_blank">📅 08:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656259">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
نقش استارلینک در تسهیل حمله به ایران
🔹
به گزارش رویترز و بر پایه اسناد افشاشده پنتاگون، استارلینک با تکیه بر دیش‌های قاچاق‌شده به ایران، زیرساخت ارتباطی هدایت پهپادهای انتحاری مانند «لوکاس» را فراهم کرده است.
🔹
این پهپادها از طریق ترمینال‌های استارلینک، تصویر زنده و فرمان هدایت دریافت کرده و حتی بدون اجازه مالک به دیش‌ها متصل می‌شوند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/656259" target="_blank">📅 08:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656258">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a2ca91df.mp4?token=FpNntAhoigT-mjDUYDEnzR8j_0C8WlTPc3CH7IoDLUvGzDqeKlypUHnOL2cAfbq_5cGa1OuwDxUpBx5Pi7oxqYiM1PRJpEFNWHp4b7eHLz9PUSLTALBG50Ul9WC-NFCza-i9_G38Dzz5VdYoa1oBM0C1NVNDgQVNmqWkSGWQR3h0rfr9BfzI7Xa0dzOyTIAC7Vbx0XhZPufdgh4D0LirAcz5deyqdPM4BYFz2wCLLj37hU_nz190MJH1o8R6jrEjYH-CPwyGOYwAMfxiQFU6ZTxbsr6_5YMoPlKZcuLj5j2V__I-pXyFlViJE6wYaTbljFH2z3cLwKufmoU8acZIqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a2ca91df.mp4?token=FpNntAhoigT-mjDUYDEnzR8j_0C8WlTPc3CH7IoDLUvGzDqeKlypUHnOL2cAfbq_5cGa1OuwDxUpBx5Pi7oxqYiM1PRJpEFNWHp4b7eHLz9PUSLTALBG50Ul9WC-NFCza-i9_G38Dzz5VdYoa1oBM0C1NVNDgQVNmqWkSGWQR3h0rfr9BfzI7Xa0dzOyTIAC7Vbx0XhZPufdgh4D0LirAcz5deyqdPM4BYFz2wCLLj37hU_nz190MJH1o8R6jrEjYH-CPwyGOYwAMfxiQFU6ZTxbsr6_5YMoPlKZcuLj5j2V__I-pXyFlViJE6wYaTbljFH2z3cLwKufmoU8acZIqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرت ترامپ در کاخ سفید سوژه شد؛ بایدن رقیب پیدا کرد!
🔹
ویدئوی چرت زدن ترامپ در نشست رسمی کاخ سفید سوژه فضای مجازی شده و کاربران با طعنه می‌گویند او که بایدن را «جو خواب‌آلود» خطاب می‌کرد، حالا خودش رقیب جدی بایدن در این زمینه شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/656258" target="_blank">📅 08:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656256">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
آژانس بین‌المللی انرژی اتمی در گزارش جدید خود اعلام کرده  که ایران به جز نیروگاه بوشهر، اجازه دسترسی به هیچ تأسیسات هسته‌ای دیگری را نداده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/656256" target="_blank">📅 08:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656254">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6145ccd1e6.mp4?token=GxpCgp7jwzG_S4PZepsIlRKpnlYOimEngtXD2wJIBCRdLV3F6feLxDHhfd-XBUMgZFLj3ZVHB0sxDaKMKock2sD_ZENzu0sb_7rvF1weIvLlvqtEmrD_2Q_0ze_OAIO9CAKxv2zNfhab1uZ-hVQG6Q0vpdu2oZe60FkO55Icd17eaHYTL6MgCOJauZkZu2gHpG3L4C7UFLN_BMCoWg_E_mgkEthAn_gfLr0YAqbAbsOZHLtMiVcG10t9rt9ZcbiSKioA29auBFswxDmhfjJJZ-0myAbrTVK0Tc_iaC3FOlSK_ZV4ZMXHKqxTXEzFJ07X9tUpYZpM4gQAbe5Bc9mCjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6145ccd1e6.mp4?token=GxpCgp7jwzG_S4PZepsIlRKpnlYOimEngtXD2wJIBCRdLV3F6feLxDHhfd-XBUMgZFLj3ZVHB0sxDaKMKock2sD_ZENzu0sb_7rvF1weIvLlvqtEmrD_2Q_0ze_OAIO9CAKxv2zNfhab1uZ-hVQG6Q0vpdu2oZe60FkO55Icd17eaHYTL6MgCOJauZkZu2gHpG3L4C7UFLN_BMCoWg_E_mgkEthAn_gfLr0YAqbAbsOZHLtMiVcG10t9rt9ZcbiSKioA29auBFswxDmhfjJJZ-0myAbrTVK0Tc_iaC3FOlSK_ZV4ZMXHKqxTXEzFJ07X9tUpYZpM4gQAbe5Bc9mCjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقام سابق آمریکا: جنگ ما با ایران از سال ۱۹۷۹(سال پیروزی انقلاب ایران) آغاز شده است
«برت مک‌‌گورک» نماینده سابق آمریکا در امور غرب آسیا:
🔹
ایدئولوژی ایران که تا حد زیادی سالم باقی مانده این است که آمریکا را از خاورمیانه بیرون رانده و اسرائیل را حذف کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/656254" target="_blank">📅 08:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656252">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
خبرنگار الجزیره در تهران: یادداشت تفاهم در مرحله نهایی خود قرار دارد و در انتظار موضع نهایی، چه مثبت و چه منفی، است/ تهران هنوز تصمیم خود را نگرفته
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/656252" target="_blank">📅 08:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656251">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08f96b91ae.mp4?token=HhSkYVttHJZs4_FWZPtV3LfpyEExVi1QZpdG4vuvyEOPtS00M_vsKAiOnk5hR3epHezGXuohXAquGK1oeAFGLb0irogMgFWS5KzWUEJ70YM7l9FVgecm3Z2kuRrR48qd4QaWu3mumt_8iE1PA-Fnbrdk0kEESCXJjLXll3IND_mXZ1ivpW_g8Jfxq5npxBPPh56JjFte75G7Tf2NB6QR7blZ_xS1uUUzFKYw5J8IS7qgeHAiCY16t33EMkx2qs827AgTz-KTZykvbZ0J1TO2fn1XZ1ApPBLMa6v4e_T-pxkHZRiMzm0SbDtkR-FkVyZG5zqjvjIPhahmIm_iNTpPHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08f96b91ae.mp4?token=HhSkYVttHJZs4_FWZPtV3LfpyEExVi1QZpdG4vuvyEOPtS00M_vsKAiOnk5hR3epHezGXuohXAquGK1oeAFGLb0irogMgFWS5KzWUEJ70YM7l9FVgecm3Z2kuRrR48qd4QaWu3mumt_8iE1PA-Fnbrdk0kEESCXJjLXll3IND_mXZ1ivpW_g8Jfxq5npxBPPh56JjFte75G7Tf2NB6QR7blZ_xS1uUUzFKYw5J8IS7qgeHAiCY16t33EMkx2qs827AgTz-KTZykvbZ0J1TO2fn1XZ1ApPBLMa6v4e_T-pxkHZRiMzm0SbDtkR-FkVyZG5zqjvjIPhahmIm_iNTpPHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: در ۳۰ تا ۴۰ سال آینده چین، روسیه، آمریکا و غرب آسیا، ۴ قدرتی هستند که جهان و منطقه را اداره می‌کنند
🔹
اگر آمریکا مدعی حمایت از تجارت است، روزانه ده‌ها کشتی تجاری از تنگه هرمز عبور می‌کنند پس باید محاصره دریایی را کنار بگذارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/656251" target="_blank">📅 08:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656249">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ترامپ: در رابطه با ایران نمی‌خواهم به سرنوشت جیمی کارتر دچار شوم  رئیس دولت تروریستی آمریکا:
🔹
موضوع اعزام نیروهای ویژه برای انتقال مواد هسته‌ای از ایران مورد بررسی قرار گرفته، اما نخواستم در شرایطی مشابه وضعیت جیمی کارتر قرار بگیرم.
🔹
اشاره ترامپ به شکست…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/656249" target="_blank">📅 08:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656248">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
عراقچی: با توجه به ملاحظات امنیتی، دستگاه‌های اطلاعاتی حضور علنی رهبر انقلاب را توصیه نمی‌کنند
🔹
سطح اطاعت و پیروی که نسبت به رهبر شهید وجود داشت، اکنون نیز عیناً نسبت به رهبر جدید انقلاب وجود دارد.
🔹
ارتباط ما با رهبر انقلاب برقرار و مستمر است و رهنمودهای…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/656248" target="_blank">📅 08:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656244">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUEU1p-LbHBBa-JJoK-M0et8c7U-ynJSpGYf2syyfGMrQxJBKdiDLf67hTQ_dp6hdE17rL2LehCJbjELTHCImcN9Ny4GLErQ5NTXAaIGsD-Q0MxQ9LKJELuBHsG99ZDGBS8IyX-jnlsFxpv_PQXKNW2n50txDWE9DaTFcr4o4YdKY3O2PKwZYY_tdautSqulezes_WFqj8zDSHS0UwV516dcuQ78uQCoCQ0VEe0R2dBDDSB6HS4EHBRavCA3Dj8LnoRJQihnNp9yQa-9p89fDjPxcVAJ56prinCx9nILClqvQWtIaAW8ePF-sPWQGSDEikdQHA83V32WHzPpF-2MQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4hFpaEcRetBn3kmmub98cE3c6N2ieICqjUHGEXjUl_8lfhqVDX7NLcj9u9HohZFw5J2TduyXGw_7GLvRn-xnOM4QdrkelcJ9qDI35dVEH_VpC1WBeY-kiaO71MVuqIpGZJmBWmX-wGfClonsHphCdy3gdgUoukbHFKtUWr8gyYOVNPuk7yh4XUTdhb1KmPuN_1I5y68FuaJfI_guJHe8R-hPUhGq5bryf6pQwUwFZbZVPoVRx-i5jDpmaMdXx6GgklhyNiBwH77JuUsn5idJHqsB1hvoYTajg7Mc-Zfa-_Cju_1GhP1AGxJ9z4Z55Or_TUKM_PZ7-WbYCpgYHHR3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87279c03a8.mp4?token=H_kujMlr7PxtwR1N5cHVI4rcdNdnY3bl8VK1I9hWhq6k1LTCcLgzjIr1AvMhz3oGs2zclty59VcUYtKkwuGmS8mK63Yvi9roZBPQsTWK9JpYS3q1tit8j8djPYkMwO79k2rffRdZoNCFN5qyR27qjq8a-l-_UZJ82AS_5dq46iBnZLjZt6jq8bRN3Bu98TkoqQTM1XtAkud9LdzUqs8AejFfgMDPCc4DEIJ-GpfoAQNxciVh0e7M4WwuazyhfdVC-FTjoctMnNX531kVTWapALkiWB8lrMl0yTu03lrqCCpCj_Q279dZ15UvHCchA1fETZayvZdJzEWSP4Zv-MSzdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87279c03a8.mp4?token=H_kujMlr7PxtwR1N5cHVI4rcdNdnY3bl8VK1I9hWhq6k1LTCcLgzjIr1AvMhz3oGs2zclty59VcUYtKkwuGmS8mK63Yvi9roZBPQsTWK9JpYS3q1tit8j8djPYkMwO79k2rffRdZoNCFN5qyR27qjq8a-l-_UZJ82AS_5dq46iBnZLjZt6jq8bRN3Bu98TkoqQTM1XtAkud9LdzUqs8AejFfgMDPCc4DEIJ-GpfoAQNxciVh0e7M4WwuazyhfdVC-FTjoctMnNX531kVTWapALkiWB8lrMl0yTu03lrqCCpCj_Q279dZ15UvHCchA1fETZayvZdJzEWSP4Zv-MSzdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سی‌ان‌ان: آتش‌سوزی ناو «جرالد آر فورد» شدیدتر از اعلام رسمی بود
سی‌ان‌ان:
🔹
برخلاف اعلام نیروی دریایی آمریکا، آتش‌سوزی ماه مارس در ناو هواپیمابر «یواس‌اس جرالد آر فورد» شدیدتر بوده و به گفته منابع این شبکه، سامانه اطفای حریق کشتی نیز در زمان حادثه عمل نکرده است.
🔹
در جریان جنگ رمضان ناو هواپیمابر جرالد فورد بر علیه ایران در دریای سرخ فعالیت می‌کرد؛ در تاریخ ۲۰ اسفند سال گذشته سنتکام در بیانیه‌ای مدعی شد که ناو جرالد فورد دچار یک آتش سوزی جزئی شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/656244" target="_blank">📅 08:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656243">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaIz4uGAm156bLwORl4Yvpziq2u41lJ2Bv-wxISk_qWKPH3zTzeEkJ83Q10akXrkpIjT4bgw_WqMiHfNpryQz_C6y6iCBbbcnDb79dAswXwY3XHy7l2n3PY2tGFcHhmaGjOxhSq4xzYm6qmRlvv4GjI4TiwTAHq5IVduQWg67HKiMemm9ZbF7XxPzEsPeDb5XrdGMFdhHOoaaq8aU2teKEt3asGql8ZF_3gmPI8-jCMVtw8jS4JeYFWNCz7_yLsUdMb4jQ2HgkXfOXf1t0zVJds3MzrrjFwveexnzlevfIic3EOti0s2gqmYiYP_4dIu6qP9Bo3TVk3BBJRCJ_J87g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۱۵ خرداد ماه
۱۹ ذی‌الحجه ۱۴۴۷
۵ ژوئن ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/656243" target="_blank">📅 08:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656242">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpWl-gWwHzG1EUa-aOdPRZruQIKYqg0ouybt7CUSONgWyAz3jCJiM_J9chHUH5zTsxJg89tAJMa0bWkHFZBvA5JXw_oT4BtS3Srga0snODS5dFHjViQ11A3G9Wqx_VfT_Y4sqAuhJpjzS6nHGnH5FwL0c2mY4K8zaolUapOB9yPg6THtxQnL-9VbN_UiFDWWNjpyHWzXgJjot2rcdBrz4oui3Jai0JpgeZEP7t4uH7TcpyMDIa1nDYN-GY0j89We7akJLJVz7a7vX5Fen5LE3zO-EWEwM4_BxFZCDramHG5smORmcdNbV_SCrtod275jgNBGG3_LztF1wA1kVAK-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦷
ایمپلنت کره‌ای با روکش
💰
فقط ۲۴,۶۰۰,۰۰۰ تومان
🎯
ویژه ۱۰۰ نفر اول
✅
ثبت‌نام و استفاده از این شرایط ویژه فقط با:
عضویت در کانال تلگرام
و ارسال *نام و شماره تماس* به آیدی زیر
👇
📩
ادمین:
@robindentalclinic
📌
کانال:
https://t.me/RobinClinic</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/656242" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656241">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKsowoENSRlUgjBGAFbuCCImM8j4yhPRk-sQgO-FMS3_inu4-fafuZEB0ylKhqkmQy5NYUztPpauN1YZdFWDoPOGmaFy_PrBr9zDYFjooCRppgrY42evBdso0xI62nc4_HVpOtucgeuxrWC256Xi6ITozUZJyASOgA22ySUk7DV3_8ibHehqF_19BOzUyIVPEUVpnfItG9Qkc0V9a4sIknHUtOXSMgLlmjaCruoeEjaVXy2j9h407rFYjUpjfbdATeK317_71aKoBqHrukEV1Axh4_vtCj9ndfhR3xVs2oCr54tUeIyiBNt1gZG6WDZMHl762NsKCBolra3OXzq_qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فراخوان نجات محمدحسن ۶ ساله
، محمدحسن برای بار دوم دچار عودِ مجدد سرطان چشم شده و برای درمان، نیاز به شیمی‌درمانی و جراحی فوری دارد
😭
💔
پدرِ کارگرش، با درآمدی بسیار ناچیز توان پرداخت هزینه‌های درمانِ سنگینِ کودکش را ندارد. هیچ مبلغی کم نیست. نگذاریم به خاطر «پول» نورِ چشمانِ محمدحسن خاموش شود
🙏
😭
🌹
💳
برای کپی کارت/شبا کلیک کنید
6037691990480709
5892107047084630
IR420190000000216756895002
پرونده بیمار
|
مجوزها
|
پرونده‌های تسویه‌شده
|
تلگرام مهرآمن
|
سایت خیریه
|
برای گزارش پرونده های درمان زیر ۱۸ سال پیام دهید
@PoshtibaniDarman
👈🏻
خیریه مهرآمن با هدف کمک به کودکان بیمار، تهیه دارو و درمان، و حمایت از کودکان بی‌سرپرست و کودکان کار فعالیت می‌کند. مازاد کمک‌های مردمی صرف امور مؤسسه و یاری به سایر کودکان محروم می‌شود.
💚
کانال ما
👈🏻
https://t.me/mehreamencharityy</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/656241" target="_blank">📅 00:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656240">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T4F1aisunp4n-dhxOO5UPSA81cPtTMP48qdZNyKWbidBU6EdLAKEALsofcfArTflQlV283feeFarnuhqtxQ0iSVhusVJPG0OUQ8AFtnU9GO-nWJPYVReCX3QsSKfjncOwoAunzqJZqFwtiFK8QHMOgJj7HS15Jcv1z97P7IQUTLZezkkBLzOBfwpi5EgyI6DqyhewhRyVGybg0I1Ry-FQ6qwCPf3iytxeUtBf2hQTVEu75QScd69Pb8DvReYB-2vIyURJvbhNaXHVCBvlecl_tVYf7_zRE7FZU1bzHegFugZR0SDOfSG16kg3aVXa-ZKZyRJJN7HDTOIQPn2m9h6WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🪄
🌟
از تخیل تا واقعیت: با هوش مصنوعی و برنامه‌نویسی، ایده‌هایتان را زنده کنید
🪄
🌟
🎓
مدرسه‌ تابستانی هوش مصنوعی روبوآموز
🚀
آموزش‌ پروژه‌محور و مرحله‌به‌مرحله
🧒
دوره نونهالان ۷-۹ سال:
🔹
اسکرچ جونیور
👧
دوره های کودکان ۹-۱۴ سال:
🔹
برنامه نویسی مقدماتی و پیشرفته اسکرچ
🔹
دوره تخصصی هوش مصنوعی و ابزارها
📲
کانال آکادمی:
@roboamoozacademy
🔗
لینک ثبت نام:
www.roboamooz.com
☎️
پشتیبانی:
09105253867
@roboamooz_admin</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/656240" target="_blank">📅 00:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656239">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOR666XjV-R-5-ZtE6hLyS4Qag1M2fACo00BykzkuYdKeM203U_rwtti44Mojkgc65biGoZkNxr5w4noV1j-pcBIjlmLKXaHCxKIvIXO9jf-rj5F37plKvKchJ2WYAIZ1ew2jHAUj0tLVgLDQYvWPqwAIY1LQKROc1vyoCG9uom07944lbw_KzI7H_FbgiABnNBNA0o4B2W3nxNMV0fg62H5e2-HJB70xd1JI5JlE5_biLGHikwsF8Vcj7ROEIefSfgGMKG_fndOXPY70SvmTUaCnDj0q4kJDwKgYKqUlK5YZen7RNNIOow8VuEfxgNUhB0NaJNlBdzLnt5mGKUGOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/656239" target="_blank">📅 23:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656238">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
عراقچی: با توجه به ملاحظات امنیتی، دستگاه‌های اطلاعاتی حضور علنی رهبر انقلاب را توصیه نمی‌کنند
🔹
سطح اطاعت و پیروی که نسبت به رهبر شهید وجود داشت، اکنون نیز عیناً نسبت به رهبر جدید انقلاب وجود دارد.
🔹
ارتباط ما با رهبر انقلاب برقرار و مستمر است و رهنمودهای ایشان در زمان مناسب به دست ما می‌رسد و دقیقاً براساس آن‌ها عمل می‌شود.
🔹
رهبر انقلاب کنترل کامل امور را در دست دارند و با توجه به ملاحظات امنیتی، دستگاه‌های اطلاعاتی حضور علنی ایشان را توصیه نمی‌کنند./اعتماد آنلاین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/656238" target="_blank">📅 23:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656237">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qq-PBUKxoGzFyZAF0ZC01qU-d4d7ZvrfV-W-pN-5Gq6NPufcM1imCkMk2-c2lSl-v0Lc5VfhD7V01TED0ELJl3lwdjXkCOqN2qbGkgKjVaXgZ04lCnRJTrtSnnOXsvkOPbTM6NJvJT4_uN0AijXfe4PmIz6Ch2Y9Kri5BaexPRmrQsqB7D_vU_RIIi7r6SZq5ruYDTso2a7z14MaujecKAT15YVebsqwSup6NA1xCOtBet1Y12Ix2rizNKuqCT9bqH8zEnnzgLnV09yULrXGlgbfldHYlwhgo939lJuL-C2cYGLz_6MvS1uTSJxl-8mp8jyNcMEwF6oxQgB76QXj9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاب خاص مهمونی کیلومتری غدیر تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/656237" target="_blank">📅 23:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656234">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae25f2633a.mp4?token=sIJQHVs7jf6J9GV-7NCSRqq-teMyLk_afxJhbyj55m4ElLBoVPfFnXECrJ4dIbLmvyq0ovb6ffTWPmai3VeLABcR1RCqjldIajHPBppY1QIR8GAIYQD3PC6jv34K0JT2UhAEMIekWMoNkMWtKB5qdYjLP9JhtrRaj0CEddS3VtuVOrWzi1_UifIVAut9Fo8X_HaHUxzwdL6m0G-v3p2J2RWy9dZavaue2_dZk53-q1JbHavYs33a2L_DfWLKAwQ8Dv_6kS5D5vUzBCmE3HirjSXH37HkfhiyPQm53wG1gEKkFVw4EyW-f11YH8Lc8dIeTq-zyqhfoGW5Qxsfwx99YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae25f2633a.mp4?token=sIJQHVs7jf6J9GV-7NCSRqq-teMyLk_afxJhbyj55m4ElLBoVPfFnXECrJ4dIbLmvyq0ovb6ffTWPmai3VeLABcR1RCqjldIajHPBppY1QIR8GAIYQD3PC6jv34K0JT2UhAEMIekWMoNkMWtKB5qdYjLP9JhtrRaj0CEddS3VtuVOrWzi1_UifIVAut9Fo8X_HaHUxzwdL6m0G-v3p2J2RWy9dZavaue2_dZk53-q1JbHavYs33a2L_DfWLKAwQ8Dv_6kS5D5vUzBCmE3HirjSXH37HkfhiyPQm53wG1gEKkFVw4EyW-f11YH8Lc8dIeTq-zyqhfoGW5Qxsfwx99YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قدیمی‌ترین کتاب ریاضی جهان با قدمت ۱۳۰ سال در زمان مظفرالدین شاه!!!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/656234" target="_blank">📅 23:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656233">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔹
خبرهای داغ امروز و امشب را از دست ندهید
🔹
🔹
رأی کنگره آمریکا علیه جنگ ایران
👇
khabarfoori.com/fa/tiny/news-3220428
🔹
علی کریمی داماد کیست؟/ چرا پدرزنش اعدام شد؟
👇
khabarfoori.com/fa/tiny/news-3220492
🔹
اولین واکنش «محمدرضا شهبازی» به جنجال های دیروز/ ویدئو
👇
khabarfoori.com/fa/tiny/news-3220475
🔹
عراقچی: هنگام شهادت رهبر انقلاب، در دفتر ایشان بودم
👇
khabarfoori.com/fa/tiny/news-3220486
🔹
حضور قیصر خواننده در تجمع میدان امام حسین/ ویدئو
👇
khabarfoori.com/fa/tiny/news-3220529
🔹
ویدئو‌های جذاب را در آپارات ما ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/656233" target="_blank">📅 23:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656232">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbcf6abb0f.mp4?token=Zl_EySCFEsk9RYeft2atw4mR9CPBVhP7Lf32orNwK0Bat2acuAJnGre_rW1Ho_8GSul3-tQ1VdKgCH9bU7Z48JTYrVxNbUtFJGx0j6Aj82Iz5ZDYx-EzsQDz-riwITjJ9zbAsG5wqAhUF4c09H5zuN4JU4TjXfjzT7P4jXGsR5HA_0uKinQNj8tyR72UuJlkoQ7XKzVMrbg4AnQOAylQFsARoMtNxE8n8OEo6DBEYMOOxuTXfYvlnpYBcc-6gjbm9WKKm_ivK75D4ZmSuLG91mSA02f-iOqHDfdpi8ZDlcHGKmDx3yHFAy5rD-97rjnF7FFpns_caP9HVzmE-CEDMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbcf6abb0f.mp4?token=Zl_EySCFEsk9RYeft2atw4mR9CPBVhP7Lf32orNwK0Bat2acuAJnGre_rW1Ho_8GSul3-tQ1VdKgCH9bU7Z48JTYrVxNbUtFJGx0j6Aj82Iz5ZDYx-EzsQDz-riwITjJ9zbAsG5wqAhUF4c09H5zuN4JU4TjXfjzT7P4jXGsR5HA_0uKinQNj8tyR72UuJlkoQ7XKzVMrbg4AnQOAylQFsARoMtNxE8n8OEo6DBEYMOOxuTXfYvlnpYBcc-6gjbm9WKKm_ivK75D4ZmSuLG91mSA02f-iOqHDfdpi8ZDlcHGKmDx3yHFAy5rD-97rjnF7FFpns_caP9HVzmE-CEDMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور محمود کریمی، وحید شمسایی و سالار آقاپور، مرد فوتسال آسیا، امشب در تجمع مردم در میدان انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/656232" target="_blank">📅 23:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656231">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ادعای ترامپ درباره توافق با ایران
🔹
ترامپ در یک مصاحبه خطاب به خبرنگاران گفت که آنها به زودی متوجه خواهند شد که توافق با ایران چیست.
🔹
بخش اصلی این توافق این است که تنگه هرمز به سرعت باز خواهد شد و دستیابی ایران به سلاح هسته‌ای هرگز نخواهد بود.
🔹
بعد از «به پایان رساندن موضوع در ایران» سراغ کوبا می‌روم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/656231" target="_blank">📅 23:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656230">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">✨
بلاگردون بلاگردون بلاگردون ایرانم
به درگاه رضا شاه خراسانم رضا جانم
▫️
اجرای قطعه «بلاگردون ایرانم» با صدای حسین حقیقی در برنامه غدیر
@Heyate_gharar</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/656230" target="_blank">📅 23:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656229">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RK_bWVjvBOoW1VJiMNBxUcaMpQAdpyklUQSH2HZm5o7NfggN_PL2SLYLEjFJrltpkmn5tFfhN9cYhHNbxLjMgfIYFi-0y4E43wctirApl-h_F_45IBYl_GwJ0UJW6_hnY4y1IXMBAJhBbOODgIG_LlNd32G5shb3hllq_zYjjGLAzZXtWGJe2IHawku_pHPfQ2N8--ZVa_dlanl2GjJBPD1AS0VdPUfZwRFKTmbW0604aPI1dlrkOa6sFamBVyAMhzPnfUlqrQhjcl3N-ngiwt19vc3CGetRK63GzMrFSYDq00LqwLs5sRp9q2DRk7T_qEH8sxuTZdU1DDFStHF3Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شرط ترامپ برای ازسرگیری جنگ با ایران مشخص شد
🔹
نشریه «وال استریت ژورنال» بامداد پنجشنبه ادعا کرد که رئیس جمهور آمریکا گفته فقط در صورت کشته‌شدن نظامیان این کشور، حملات به ایران را دوباره از سر می‌گیرد.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3220519</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/656229" target="_blank">📅 23:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656227">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikCwk-EsfFnCWjBCCo6UWcqajcgKYJwU2938MXrqYXMJVuGIz8-XWo8mVHSQ6vSG6SVB2Asn8Q_VmmMffMMVFbSejikPAlEI7tGewnr4QMjhEjJyUibukuaLkQxHVCjbu_yVNNO1GZ191KH5bZMCF1AxNqnnrWWrQtiiPn5Y8p-RSRRHRLdGcDeB21x9Szz3Lr3MSarsx9Q_vArT_Dv6MdY1WMcGBuMR0bUm6hwcoppB4IWgr7eQK01__ikgQs6ptaoK1-w4uF9yNtt-OZqszAG9obULwyVGGKJFwt7zaURl8qnRe0Yuyv_J_gLHwzRmY63SXmIfMkuNpvABvKRb2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتراف ترامپ به شکست طرح ربودن اورانیوم از ایران
🔹
ترامپ درباره طرحی که آمریکایی‌ها برای ربودن اورانیوم غنی‌شده از ایران داشتند گفته که جابجا کردن مواد هسته‌ای مستلزم حضور در مناطق درگیری به مدت یک تا دو هفته بوده است. ایالات متحده به همین دلیل آن طرح را پیش نبرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/656227" target="_blank">📅 23:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656226">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b22c0e31dd.mp4?token=G7agVVTWAiS9k050_hbLfb1Ym1pcjLnj4ryWMy6ioZuZF7sdnGLDc0NTxHrWwaj-gaTKFWqzzkLq6VYud3WShjJwVaN3LJSIt1ltkV2XWqLdYCEOmhHKfQFXyqX96HdtgLvQNQEz-sCWbt_InEsPVCMR6CMdKN5CQL6uZGoCgLy-tl2yKlOYHaaUSyA8uh215qC-C5GVW5L7XCxiix5fhen_DuNifdDeHr7hWXWsEQMUvKzcUf2Xy54EHQyXQOSTZCSOlmxTl9PkXt00ID3AiXcRtsmYdV5FhH6NoQ5pnFljrKQglSQpsaH3X5p_uBrwZPb-jmWl3dLd9xARxlrmCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b22c0e31dd.mp4?token=G7agVVTWAiS9k050_hbLfb1Ym1pcjLnj4ryWMy6ioZuZF7sdnGLDc0NTxHrWwaj-gaTKFWqzzkLq6VYud3WShjJwVaN3LJSIt1ltkV2XWqLdYCEOmhHKfQFXyqX96HdtgLvQNQEz-sCWbt_InEsPVCMR6CMdKN5CQL6uZGoCgLy-tl2yKlOYHaaUSyA8uh215qC-C5GVW5L7XCxiix5fhen_DuNifdDeHr7hWXWsEQMUvKzcUf2Xy54EHQyXQOSTZCSOlmxTl9PkXt00ID3AiXcRtsmYdV5FhH6NoQ5pnFljrKQglSQpsaH3X5p_uBrwZPb-jmWl3dLd9xARxlrmCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور خانواده فرماندهان شهید موشکی ایران در میدان انقلاب
تجلیل از خانواده سرداران شهید طهرانی‌مقدم، حاجی‌زاده و محمود باقری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/656226" target="_blank">📅 23:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656225">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">✨
در طالع امسال برایم بنویسید
یک روز نجف باشم و یک روز کنارت
▫️
شعرخوانی زیبای حسین حقیقی در برنامه پناه غدیر، دل هارا هوایی کرد
@Heyate_gharar</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/656225" target="_blank">📅 23:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656224">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ce4a6e0c1.mp4?token=MPvBy_8e4ikIv11SMHohwZwR5iSKJTqx_xw5asbhJZB_KbI34FB2c3Fy6rfljRpbyqL8sD-60WVkTZ4nOr9dA1rB6i96ebOo4cT8Zpp5rqe6jjJ4eapRrM3u-BYCHeLBFH4o-ip2vLlNG77oDNiIbEcSbORQ0DeApgJpqAdYT1HFiDhkkxS8YD23-1fJnK87VTVoElpsCNwfu3yoxQQ_M3IiTxXpZh6G2rNeLfwL8Q4NnPuc9aTB4yadMnzv4bM7LGpwC5qiXomqIBw2hHAkneOkz3gvwsC-cH4lMOEXQQDOjTI-72RVf3XnRtGCYb9_i5OLZEVl14uCo_YLd3vS-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ce4a6e0c1.mp4?token=MPvBy_8e4ikIv11SMHohwZwR5iSKJTqx_xw5asbhJZB_KbI34FB2c3Fy6rfljRpbyqL8sD-60WVkTZ4nOr9dA1rB6i96ebOo4cT8Zpp5rqe6jjJ4eapRrM3u-BYCHeLBFH4o-ip2vLlNG77oDNiIbEcSbORQ0DeApgJpqAdYT1HFiDhkkxS8YD23-1fJnK87VTVoElpsCNwfu3yoxQQ_M3IiTxXpZh6G2rNeLfwL8Q4NnPuc9aTB4yadMnzv4bM7LGpwC5qiXomqIBw2hHAkneOkz3gvwsC-cH4lMOEXQQDOjTI-72RVf3XnRtGCYb9_i5OLZEVl14uCo_YLd3vS-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار برای اولین بار | تصاویر جذاب و دیدنی از اولین دیدار مردم ایران و امام خمینی پس از ۱۵ سال در سال ۱۳۵۷
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/656224" target="_blank">📅 23:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656223">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✨
فهرست بهترین نماهنگ‌های  ویژه
#عید_غدیر
💚
👈🏻
جهت دسترسی به هر یک از مطالب زیر، روی اسم مولودی (آبی‌رنگ) کلیک کنید.
شرف المکان وحید شکری
بارون نجف محمدرضاطاهری
ولی الله حسین طاهری
خوشگل آرین اسمش حسین عطایی
حیدر حیدر سجاد محمدی
به به نجف امیر برومند
فوق بشر محمدرضا نوشه ور
ازل آید یکتا آسد حسین ستوده
اعلی حضرتا امیر کرمانشاهی
بیعت با تو محمود کریمی
المنت الله ابوذر بیو کافی
حیدر مولا حسین ستوده
مست نجف علی اکبر حائری
مقام والا سجاد محمدی
اسدالله حسین طاهری
الصبوح الصبوح حسن عطایی
نقش انگور محمود کریمی</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/656223" target="_blank">📅 23:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656222">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ادعای سنتکام درباره تغییر مسیر ۱۲۷ کشتی تجاری
🔹
ستاد فرماندهی مرکزی آمریکا موسوم به سنتکام، به رغم وعده دونالد ترامپ رئیس جمهور این کشور برای لغو محاصره دریایی علیه ایران، به بدعهدی خود ادامه داده و مدعی شد که تاکنون مسیر ۱۲۷ کشتی تجاری را تغییر داده است.
🔹
این فرماندهی افزود، ۶ کشتی را نیز که از این محاصره تبعیت نکردند، غیرفعال کرده و در راستای «حمایت از کمک‌های بشردوستانه» به ۳۶ کشتی نیز اجازه عبور دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/656222" target="_blank">📅 23:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656219">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd978bc00.mp4?token=popfQSEHNAw_YEz-PbDOEvnFkTj-cnDRAvFFYDnb8i48b3F4WfhIW0NMg_mZ7PL8BAK5umOcLcQkrD0vXpEJr0Oycz7THUdy107TvfHP1N5JK6ZHqOgLEZ2RqzuJMwM6rVd2sSxAU4uTi3gmtER1o1UdekGQlWP7xlThkIAozD_dBNNMZw_Dm9ta01aolxUaMV16KOMk0f6si8Wl6_A3UMOYC7O8rDRZ9yqcfJXKe-WStgPdTsQ9RWwR8AY7zSV37TQ9tqbeyemJe0usKcmlCs0lwyCggMAuAFE_D1M1tC0gYDLwm6fT7gHwAxw3bNoEs3uqkqB4LF-ZfTr8wlhrPKsh0upfdUb0px0rIqScm-vBdf2h6vYmZ8xjtVN9jFxXr6Zwt6V6K_3WmpIZBOxDXoRA5AcSQKGJsGxsyGUAwt57A3t_caghvaUVhzKJ7X-JW_4IxfurYdUgdBider6Wp3wEPYLiCtCD8BSkYpCvWuzZAYeB3IMwq59RgbvG6AQKD1nNoOYDj6OULAakmGEhe3SuqF62GGuCWrQ2HG79ourNWGHhRU49z14HfvC9AHZ1XgfgzOKHgGN7JYvuNYSuSRh0OJKMtN_MjLCuiq9olVol2Yh_ZEdRiOSvdCt78y5wu5ognqba-CkPWRbS6dwOlGrQsJfvPGYclQwg3pMOpcE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd978bc00.mp4?token=popfQSEHNAw_YEz-PbDOEvnFkTj-cnDRAvFFYDnb8i48b3F4WfhIW0NMg_mZ7PL8BAK5umOcLcQkrD0vXpEJr0Oycz7THUdy107TvfHP1N5JK6ZHqOgLEZ2RqzuJMwM6rVd2sSxAU4uTi3gmtER1o1UdekGQlWP7xlThkIAozD_dBNNMZw_Dm9ta01aolxUaMV16KOMk0f6si8Wl6_A3UMOYC7O8rDRZ9yqcfJXKe-WStgPdTsQ9RWwR8AY7zSV37TQ9tqbeyemJe0usKcmlCs0lwyCggMAuAFE_D1M1tC0gYDLwm6fT7gHwAxw3bNoEs3uqkqB4LF-ZfTr8wlhrPKsh0upfdUb0px0rIqScm-vBdf2h6vYmZ8xjtVN9jFxXr6Zwt6V6K_3WmpIZBOxDXoRA5AcSQKGJsGxsyGUAwt57A3t_caghvaUVhzKJ7X-JW_4IxfurYdUgdBider6Wp3wEPYLiCtCD8BSkYpCvWuzZAYeB3IMwq59RgbvG6AQKD1nNoOYDj6OULAakmGEhe3SuqF62GGuCWrQ2HG79ourNWGHhRU49z14HfvC9AHZ1XgfgzOKHgGN7JYvuNYSuSRh0OJKMtN_MjLCuiq9olVol2Yh_ZEdRiOSvdCt78y5wu5ognqba-CkPWRbS6dwOlGrQsJfvPGYclQwg3pMOpcE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر حیرت‌انگیز از برگزاری جشن بزرگ غدیر در شب گذشته یمن همراه با نورافشانی، روشن کردن شعله غدیر در کوه‌ها، ارتفاعات و سقف منازل و جشن و پایکوبی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/656219" target="_blank">📅 22:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656218">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">✨
«عشق من حیدر کراره... آقایی که توی شهر نجف یه حرم داره»
▫️
حالا و هوای برنامه غدیر با این نوای علی اکبر حائری که حسابی رنگ و بوی علوی گرفته...
@Heyate_gharar</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/656218" target="_blank">📅 22:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656217">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/148dbf71a8.mp4?token=R5L3jBeaSxGLoB3gHRyOfHttm5CcOUk1PIS7GzWfNaXDnB7CTn20WDZdRddR7D1QHLN8UDzt7nhonZql9CY3BaVmK5nkEc9keQk_45T-w80IoABT9bv5ozFerVRVYH6rXgd5nQmNHaLvH9Tv77Jj1cuxtcTMfXxMCUrirTP8p3Fz7WqWIbvtbkNnLP54oJkSDxK-vnIvMx8axagKSMobsyN8JVc_P0zCiEb1YwQzmm9t-Tz6vhRlsoDIEVPn5ZX8NuCtyivii5Cx3u-9bUpTr1IYMaSw_vhqnUjc6GH3COsW6VDe80ZU04EHMUGjDqwNWRuoD-xQJ_VCwPhuwxcohQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/148dbf71a8.mp4?token=R5L3jBeaSxGLoB3gHRyOfHttm5CcOUk1PIS7GzWfNaXDnB7CTn20WDZdRddR7D1QHLN8UDzt7nhonZql9CY3BaVmK5nkEc9keQk_45T-w80IoABT9bv5ozFerVRVYH6rXgd5nQmNHaLvH9Tv77Jj1cuxtcTMfXxMCUrirTP8p3Fz7WqWIbvtbkNnLP54oJkSDxK-vnIvMx8axagKSMobsyN8JVc_P0zCiEb1YwQzmm9t-Tz6vhRlsoDIEVPn5ZX8NuCtyivii5Cx3u-9bUpTr1IYMaSw_vhqnUjc6GH3COsW6VDe80ZU04EHMUGjDqwNWRuoD-xQJ_VCwPhuwxcohQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت آب سد کرج، امروز
#اخبار_البرز
در فضای مجازی
👇
@akhbare_alborz</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/656217" target="_blank">📅 22:44 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
