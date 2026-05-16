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
<img src="https://cdn4.telesco.pe/file/nYXhqiFHSToMN9W4OrJvHQrELvzIlYcKsO2SxMfwHa_cCLzXlVXLIcYpth6xq1NztjHtJlC-ujIODKryxWfsbi_LeaGX-VFhpfSH_WCStG-x4syJZEK-fkOKkvDeUsiCsp7sscG7BQWGhjKb6EzhZXZURrSx-w2PP8EB-pFrhIhzqsDYqHjHQrgg2lEu1ZCfsmkmUwkkM9o_Vc6hV5GO3yZpbEyyNLFzLdnGaSrmozEZuO7HFcf570nArMPRQJWesZ5-rn5DI9YRLQArCNQOJApoUjE6ljY-VMmaJOdVtmndthLhqu6j6TDF7qu-AR7VFvmIfJSvqDjjOGVMJrrUuA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 آموزش سئو محسن طاوسی</h1>
<p>@mohsentavoosiseo • 👥 7.36K عضو</p>
<a href="https://t.me/mohsentavoosiseo" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا فقط تالیف، مستندات و تجربه هست. اخبار و ترجمه کار من نیست.دوره:https://mohsentavoosi.com/course/seo/یوتیوب:https://www.youtube.com/c/MohsenTavoosiاینستاگرام:Instagram.com/mohsentavoosi.seohttps://www.linkedin.com/in/mohsentavoosi</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 19:20:19</div>
<hr>

<div class="tg-post" id="msg-685">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPhu2rVd57XNKfUbsUgQ5SMBySckLogIcHy1dIgQy_gpN6SkK3pHarNlHc1tknNg2ylVYAokua37FiUJxnjE5GRWaDgMKgK_ctTr8IbETX4aoZATGhbcl_csoLpc5dwuiy-07pZ425kkQpmUnOuJpqnLg4o97Iu6q98NOM0TN_237AbYC5afVOFfFAWYYsjRB7qhoPQbGxJ5QjOR0_t96utyMA3OVtFQmE0mIVNloTC26G27G5B5SKO7jtfT8KFjGvE-9GXR-1dO4Sl2UWHAdPym38aXzlnpitoug8rbwIkevHZ4p5ggXrpqH71jEfitguvBhndPx4ntYw73w5AY5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مرحله ای رسیدیم که هوش مصنوعی، خودجوش، خودش از دیتای خودش ایراد میگیره. خیلی خوبه. تبریک میگم
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/mohsentavoosiseo/685" target="_blank">📅 21:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-684">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxG1A_-gFfOfD8lhQGqYmzGlVJ_0RoooX17GSwSa84ho-RvfNUSa_rjyM_g2MT-MyAsyTGoqPgEudW7fo9TLEexynoPFS_sg9yjINkeJTwxYBscfX1by84U5olt90LP7SMJHOhmhXID8a_UjhAlvJYJxh8SdUY28RLnjNOPP8Y_Fp1dPwVPYSsQ_kd4Jn1lnTsAp_2L6wfF7JcDkVum1PR2YIksehwwLoofOC4-XRxBhTMm7rCXrvIqE-8sHvcHgLjMY63Zkg0K8nOABD6DqFox1hSPdLJ-IbS4rENz2HMWaVIw7iIsK_Oaw859_v-6c5XW-8eFu9D3hE-_QEesvvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من یه معتادم! معتاد کلاد!
خودش پیشنهاد داد یکی از قانون هامو که بهش داده بودم تغییر بدم و پیشنهاد خوبی هم داد.
اصلا انگار بشره. توقعمو خیلی برده بالا. خیلی هم ریز بین و دقیقه. خیلی هم عمیق میفهمه.
آنتروپیک پس فردا مثل Horizon Zero Down و Forbidden West، ربات هاش زندگی انسان رو می گیرند و باید پناه ببریم به پناهگاه ها و ربات های Anthropic بشن موجودات اصلی زمین.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/mohsentavoosiseo/684" target="_blank">📅 17:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-683">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔆
به خاطر شرایط جنگی، قیمت دوره از 12 میلیون تومن، به 4 میلیون تومن، کاهش پیدا کرد و این قیمت تا زمان ظهور دوباره امید به بهبود در دل مردم این سرزمین، این قیمت باقی می مونه.
❗️
هیچ وقت هیچ کمپین تخفیف و فروشی نداشتم. این هم کمپین نیست! کاهش دائمی هست تا برگشت…</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/mohsentavoosiseo/683" target="_blank">📅 15:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-682">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">آموزش سئو محسن طاوسی
pinned «
🔆
به خاطر شرایط جنگی، قیمت دوره از 12 میلیون تومن، به 4 میلیون تومن، کاهش پیدا کرد و این قیمت تا زمان ظهور دوباره امید به بهبود در دل مردم این سرزمین، این قیمت باقی می مونه.
❗️
هیچ وقت هیچ کمپین تخفیف و فروشی نداشتم. این هم کمپین نیست! کاهش دائمی هست تا برگشت…
»</div>
<div class="tg-footer"><a href="https://t.me/mohsentavoosiseo/682" target="_blank">📅 15:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-680">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تمام صحبت های من درباره هاست و سرور و دسترسی و Origin Rule و GEO DNS، پست های زیر هست. درباره sync بودن سرور داخل و خارج هم در لحظه نظری ندارم.
هاست های ایرانی که اخیرا میگن دسترسی گوگل بهشون باز هست(ولی از خارج یا باوی پی ان باز نمیشن)، دیگه چون فقط داخل هست، بحث sync نداره. با تست های من و بازخورد دیگران، بعضی از هاست ها اینطوری هستند و گوگل هم بهشون دسترسی داره(اما وریفای سرچ کنسول باید فقط با دی ان اس باشه).
چه هاستی؟ اسم نمیبرم. پس فردا بد میشه میفته گردن من.
این هم بگم که در تمام شرایط، اختلال وجود داره. الان اپ تایم 90 درصدی(به جای 99.9 درصدی) ایده آل هست.
راه دیگه ای برای هم sync بودن هم در دسترس بودن از داخل و خارج نمیشناسم.
البته که متخصصین devops روی سرور های اختصاصی با هزینه زیاد میتونن. یک سری پلاگین وردپرس هم برای sync دو دیتابیس هست. ولی من چیزی که خودم اجراش نکردم آموزش نمیدم.
تمام صحبت های من در این باره:
https://t.me/mohsentavoosiseo/620
https://t.me/mohsentavoosiseo/623
https://t.me/mohsentavoosiseo/624
https://t.me/mohsentavoosiseo/625
https://t.me/mohsentavoosiseo/628
https://t.me/mohsentavoosiseo/631
https://t.me/mohsentavoosiseo/633
https://t.me/mohsentavoosiseo/634
https://t.me/mohsentavoosiseo/639
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/mohsentavoosiseo/680" target="_blank">📅 18:48 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-679">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeTqDvukHtKHa-Q9t6oqKdtujh3QBoPAbwuhGGAquFD2NDU2Y1X3RepiN-yFvcwcvmjuraBkMFuMl50K52Zx8Smi0cR-Gv4bd39s4dAOqvoq5dvYtUZbToK2gI227uq7hVnWgFcFshEJGbuWdHFK1BUGZV5Y4IXD8uff_pH8LU4gG2_xDV9jluDND2XXmJgQbD1HpEVhaA2w3rFVbGbCRSfne4ybpvfm8PMPiXVZ0-15mLDHUTB2jIPvvxDU9Igu9zwFgQaWmvv2mfNAxHebTJ4JE43vIbNoNYQybCN_yBp5atz_Q_jtggMSW1LknNMq21n6ZvZzsvK-jLhONTrj5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعا خوشم نمیاد از این خسیس بازی بیش از حد کلاد. دوتا لینک کرد و خوند، یه دونه گوگل شیت دویست ردیفته و ده ستونه ساخت کلاد مکس(5x pro) شد 22 درصد!
البته با Sonnet کمتر مصرف میکرد قطعا. ولی حوصله خنگ بازیش رو نداشتم چون کار گوگل شیتش پیچیده بود. آدم هم مغزش از جا درمیومد با این تسک.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/mohsentavoosiseo/679" target="_blank">📅 14:32 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-678">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">صحبت تلفط شد، خیلی ها خارج رو شامل چند تا دونه کشور خاص میدونن و ملاک ذهنیشون اینه: ایران و امریکا. ایران و کانادا. ایران و آلمان.
هرکس که مهاجرت کرده، ایران و کشوری که رفته رو راس میدونه تو ذهنش.
ولی بهتره ما جهانی فکر کنیم و کل کره زمین رو ببینیم. جهت خط خطی کردن ذهن هایی که ناخواسته محدود شدند، یاداور میشم:
خارج شامل هند، بنگلادش، نپال، سومالی، کنگو، هنگ کنگ، فیلیپین، میانمار، تانزانیا، گامبیا، بوسنی هرزگوین، مغولستان، لیتوانی، لیبی، مصر، غزه و رام الله و کرانه باختری، صربستان، مراکش، قرقیزستان، زامبیا، شیلی، بولیوی، گواتمالا و... هم هست و این ها هم خارج محسوب میشن و جمع کوچکی از سرزمین ها و کشور های غیر انگلیسی زبان هستند!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/mohsentavoosiseo/678" target="_blank">📅 11:42 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-677">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تلفظ Claude به انگلیسی با لهجه بریتانیایی و آمریکایی، کلاد هست. آ کوتاه. کلود نیست. حالا شاید با انگلیسی غیر اصیل مثل هندی و سنگاپوری و اماراتی یه جور دیگه بگن.
تلفظ Claude در بعضی زبان های اروپایی و اسپانیایی و کره ای میشه کلودی.
کشور های مختلف هم به مدل خودشون تلفظ میکنن.
تلفط Claude به فرانسوی میشه کلود. با صدای O. صدای اُ . بعد از d هم e گفته نمیشه. کلوده نیست. کلود. ریشه کلمه claude، فرانسوی هست. در نتیجه کلود هم درست هست.
مثل BMW که متولد آلمانه و آلمانی ها میگن بی ام وی. و آمریکایی ها میگن بی ام دبلیو. عملا اصلش بی ام و هست(نه دبلیو). پورشه هم درست تر و آلمانی تره. پورش رو انگلیسی ها میگن.
اما کلاد، فقط واژه اش ریشه فرانسوی داره. ولی شرکت Anthropic، که سازنده کلاد هست، یک شرکت آمریکاییه.
خلاصه: هم کلاد درسته هم کلود. آ و اُ . کوتاه.
نظر شخصی: برای اینکه با فضای ابری قاطی نکنیم، کلاد بهتره. چه برای مخاطب انگلیسی چه فارسی. تلفظ رسمی انگلیسیش هم کلاد هست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/mohsentavoosiseo/677" target="_blank">📅 11:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-676">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQ7rYVD22-vFMcXdkhDtMS1rTmFyJY5ml9Qi5wGPQC1zmbpOL3RVJfv88Dn6uYpSs8BW5ezywlpA3c6-ey2hr1b6fk01G53WZyEla_iKI-JNpgrW3VgULOZXve94YMlIFqKEXBt_zcjT84Qo-A942WiCL1u61LtyNU02tpQliy92SMHIX-y6DFUBhnklW1390xUe27MEIl1HV6Bs7P2kigM6-VWENtRvdQ4feGiAwCRajeMsAhngzYAlApTS4oco2GDpsqgOxhnGp7WT8fCVM991M_yChgyTAfNmz-liw1SmJgzRa58S-qRl-sZOGfZin3owFwvHL0ME6EZuzX9Plw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این همه خوبی از کلاد گفتم از بدیشم بگم. مثل chrome که اندازه اسب، رم می خوره، این هم خیلی مصرفش بالاست و گرونه.
کافیه یه کم تسکت متنی نباشه، نسخه Opus بسیار بسیار مصرف می کنه و البته بسیار هم باهوش تر از Sonnet هست.
این سشن ساعتی بشه 70 درصد برای کلاد مکس(5x pro) که ماهی 100 دلار پولشه واقعا زیاد هست.
کلاد پرو برای من اغلب کم میومد. کلاد مکس 5X اغلب زیاد میاد.
یک سری نکته برای بهینه سازی مصرفش از نظر زمانی هم تو
این ویس
گفتم.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/mohsentavoosiseo/676" target="_blank">📅 16:16 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-675">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🟢
اکانت ChatGPT قبلی مبلغ 1 میلیون تومن بود که یک workspace اضافه میشد به اکانت فعلی خود شما و موجودیش فعلا تموم شد.  الان اکانت ChatGPT Plus یک ماهه موجود هست که کلا یک اکانت user pass داده میشه و شما می تونید پسوردش رو عوض کنید و استفاده کنید. مبلغ: 1700.…</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/mohsentavoosiseo/675" target="_blank">📅 15:51 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-674">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‼️
اگر یکی از موارد زیر روی شما صدق میکنه، یعنی هنوز بسیار بسیار عقب هستید در دنیای هوش مصنوعی. راه حل چیه؟ برعکس موارد زیر رو انجام بدید و رویکردتون در تضاد با این ها باشه:
❗️
- تو سر هوش مصنوعی نمی زنید.
❗️
- از هوش مصنوعی ایراد نمی گیرید.
❗️
- تفکر نقاد بهش ندارید.
❗️
- به عنوان فکت چک به حرف هاش و بررسی هاش نگاه می کنید.
❗️
- حواستون به سوگیری هاش و مموری که با در چت با شما ایجاد میشه نیست.
❗️
- از حافظه و مموریش برای اینکه چیزی بهش یاد بدید استفاده نمی کنید.
❗️
- بهش فحش نمی دید یا تند حرف نمیزنید و سعی می کنید باهاش مودب باشید و احساس یه انسان باهاش دارید(جدی)
❗️
- در صحبت با شما گستاخ شده یا به شما تیکه میندازه.
❗️
- از بخش های مختلف و نسخه های مختلفشون مثل instant و thinking و deep research و agent و کانتکتور ها یا خوندن فایل و لینک استفاده نمی کنید.
❗️
- موقع پرامپت دادن برای تولید چیزی یا انجام کاری، بهش دیتا نمیدید یا دیتای کمی میدید و بعد از اینکه تولید کرد تازه یادتون میفته بهش مشخصات بیشتری بدید. مثلا برای تولید عکس، نه سایز میدید نه نسبت نه تم رنگی و واقعی بودن یا کارتونی بودن یا استفاده کردن یا نکردن از چیز خاصی و... . اما به محض تولید هر خروجی یادتون میفته که ااااا اینم باید بهش بگم. تصورتون اینه که مغز شما رو باید بخونه اون بدبخت.
@mohsenavoosiseo</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/mohsentavoosiseo/674" target="_blank">📅 15:48 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-673">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تفاوت کلاد و چت جی پی تی درباره اتفاقات 28 Feb 2026 یا 9 اسفند 1404.
چرا کلاد بی نظیره؟
یه گوگل شیت ساخت و دانلودش کردم. کپیش کردم. و تو یه لینک دیگه بهش دادم. گفتم بخون ببین چی میفهمی.
بهم گفت: این همون فایلیه که خودم برات ساختم!
✅
شما این کارو با Gemini و ChatGPT کنید میشینه توضیح میده. نمیگه این همون فایله.
✅
کلاد بهش گفته نشده هر سوالی رو حداقل تو انقدر حجم محتوا جواب بده. گاهی یه "نه" خالی میگه.
✅
کلاد علاقه ای به قانع کردنت نداره و سوگیریش به شدت پایین تره. سعی نمیکنه راضیت کنه الکی.
✅
از همه مهمتر، کلاد خیلی سریع تر میگه غلط کردم! این چت جی پی تی، یه موجود لفتیست دموکراتیه که کلا فکر میکنه هیچ اشتباهی نمیکنه و تاکید هم داره روش.
فاز اینم داره که نه فلان چیز شایعه هست. شما همین الان برو درباره اتفاقات 28 فوریه یا 9 اسفند ازش بپرس. متوجه میزان و درجه حماقتش میشی. وقتی جواب اشتباه داد بهش بگو برو سرچ کن. باز میره تو فاز اینکه نه شایعه است و... . و یه جوری تاکید میکنه و نقد میکنه که فکر میکنی حقیقت تو دست هاش هست.
بعد گیر میده که تو اشتباه میکنی. بهش میگی سرچ کن میگه نیازی به سرچ نیست!
حالا کلاد چی جواب میده؟
این سوال شما بر اساس فرضی است که نیاز به بررسی دارد. بگذارید جستجو کنم تا ببینم آخرین وضعیت چیست.
کلاد 100. چت جی پی تی صفر.
البته من دارم درباره Opus حرف میزنم. Sonnet بسیار خنگ تر هست ولی باز بهتر از نسخه 5.5 هست و گاها برابری میکنه.
بی انصافی نکنم، باگش تو 5.5 خیلی رفع شد. شما همین سوالی که گفتم رو برو بذار رو نسخه 5.4. کلا در حد ناندرتال ها خنگ میشه دوباره.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/mohsentavoosiseo/673" target="_blank">📅 15:36 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-672">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🟢
اکانت ChatGPT قبلی مبلغ 1 میلیون تومن بود که یک workspace اضافه میشد به اکانت فعلی خود شما و موجودیش فعلا تموم شد.
الان اکانت ChatGPT Plus یک ماهه موجود هست که کلا یک اکانت user pass داده میشه و شما می تونید پسوردش رو عوض کنید و استفاده کنید. مبلغ: 1700. یک میلیون و هفتصد هزار تومن.
تمام امکانات یک چت جی پی تی پلاس رو داره. سر ماه هم غیر فعال میشه و قابل تمدید نیست.
برای خرید به آی دی
@havijmtx
پیام بدید.
——————————-
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/mohsentavoosiseo/672" target="_blank">📅 12:52 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-660">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اکانت ChatGPT نسخه Plus روی ایمیل خودتون بدون نیاز به ارسال دسترسی، ماهانه با مبلغ 1100 (یک میلیون و صد هزار تومن) از طریق آی دی  @mohsentavoosisupport  قابل تهیه هست. (اشتراکی نیست).
❓
چرا قیمتش پایین هست. مگه 20 دلار بالای 3 میلیون تومن نمیشه؟  به این علت…</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/mohsentavoosiseo/660" target="_blank">📅 17:41 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-659">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کسانی که میگن چرا طرف رفت ارمنستان یا ترکیه؟ اونجا که ظرفیت نداره فضای دیجیتالشون. اونجا که اقتصادش فلانه!
باید بگم
قرار نیست برن شرکت ترک یا ارمنی کار کنند. ظرفیت اونجا مهم نیست! از دیجیتال مارکتر ها بعیده این حرف!
اونجا فقط یه نقل مکان سکونت فیزیکی هست که اینترنت داشته باشند و بتونن عین انسان با سیم کارتشون ثبت نام و verify کنند در سایت ها و ابزار ها و... .
ما انقدر خوشبختیم که کلا جز ارمنستان و ترکیه جایی نیست بتونیم بی دردسر سه ماه بریم و یا نسبتا ارزون و راحت اقامت بگیریم.
یک کم داره اندونزی و مالزی هم مد میشه برای دیجیتال نومد ها. ولی اون ها هم دورند هم سه ماهه نمیشه رفت هم پرواز پردردسری دارند.
بعضی ها که از اسپانیا و ایتالیا و یونان هم ایراد میگیرن! انگار قراره برن شرکت اسپانیایی ایتالیایی با حقوق های کم اونجا کار کنند.
چرا ذهن باید انقدر محدود فکر کنه که محل فیزیکی فعلی زندگی یعنی شغلت هم باید وابسته به همون بازار باشه؟ اصلا چرا اومدی تو حوزه دیجیتال اگه اینجوری فکر می کردی؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/mohsentavoosiseo/659" target="_blank">📅 11:19 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-658">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">به زودی در شغل های در سراسر جهان و ایران:
استخدام متخصص فلان (گرافیست، مارکتر، تولید محتوا، توسعه دهنده و...)
ملزومات مهم (نه امتیاز!):
تسلط به کلاد
رسیدیم به این جمله که در آینده افراد شغل هاشونو از دست نمیدن. بلکه کسانی که بلد نیستند با AI کار کنند شغل هاشونو از دست میدن. (فعلا غیر از کارهای دستی مثل آشپزی و ماساژ و خیاطی و...)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/mohsentavoosiseo/658" target="_blank">📅 00:48 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-657">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">https://www.zhaket.com/web/speedix-plugin
این شما و این هم افزونه افزایش سرعت سایت وردپرسی در اینترنت ملی.
کسانی که سایت وردپرسی دارند(که اکثریت هستند)، می دونند درد کجاست.
این پلاگین درمان این درده.
✅
باعث کندی  با وی پی ان  یا از خارج از ایران یا زمانی که اینترنت بین الملل وصل هست یا اگه هاست خارج باشه، نمیشه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/mohsentavoosiseo/657" target="_blank">📅 00:39 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-655">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نکته های تجاری ارتباطی مصاحبه ۴
چیزی که بار سنگینی از دوش من برداشت
رها کردن چیزهایی که میخواستم حفظشون کنم
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/mohsentavoosiseo/655" target="_blank">📅 17:20 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-654">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نکته های تجاری ارتباطی مصاحبه ۳
مصاحبه بین المللی
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/mohsentavoosiseo/654" target="_blank">📅 17:13 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نکته های تجاری ارتباطی مصاحبه ۲
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/mohsentavoosiseo/653" target="_blank">📅 17:09 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/mohsentavoosiseo/652" target="_blank">📅 17:05 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پست بالا:
https://t.me/mohsentavoosiseo/649
درباره Opus بود. نه Sonnet یا Haiku
و من Opus در حالت Adaptive Thinking استفاده میکنم.
خود Opus مصرفش بیشتر هست. در حالت Adaptive Thinking باز هم بیشتر میشه مصرفش.
برای کارهای ساده در حد ترجمه و ویراستاری نقطه ویرگولی و...، اصلا نیاز به Claude نیست. مثل این میمونه که وسط آسفالت صاف، لندکروز ببری. سلطان رو سر چیزای بیخود بیدار نکنید.
تسک ساده هایی که خیلی هم ساده نیستند ولی پیچیده هم نیستند و فقط نیاز دارید خنگ بازی کمتری داشته باشه هوش مصنوعی، هم روی Sonnet. خیلی با Haiko  تجربه ندارم که بگم دربارش.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/mohsentavoosiseo/651" target="_blank">📅 14:02 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-650">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کاهش مصرف Session پنج ساعته و هفتگی کلاد.
مصرف دوبرابر کلاد در ساعت های Peek
چرا اشتراکی خیلی معنی نداره برای کلاد؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/mohsentavoosiseo/650" target="_blank">📅 21:32 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-649">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">چرا کلاد خداست؟ Claude خداست؟
بدی ChatGPT و Gemini و Grok چیه؟
۳ Anthropic فعلا
Google, OpenAI و
X.AI
صفر
سه هیچ به نفع انتروپیک(شرکت کلاد)
سطح این ویس مبتدی هست. بسیار مبتدی.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/mohsentavoosiseo/649" target="_blank">📅 21:32 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-648">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🏴
در جریان باشید
🏴
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/mohsentavoosiseo/648" target="_blank">📅 21:32 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-647">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اکانت ChatGPT نسخه Plus روی ایمیل خودتون بدون نیاز به ارسال دسترسی، ماهانه با مبلغ 1100 (یک میلیون و صد هزار تومن) از طریق آی دی</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/mohsentavoosiseo/647" target="_blank">📅 15:58 · 05 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-646">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پیامی از بچه ها:
خود ما از این روش اقدام کردیم و ۲ روز تقریبا سایتمون داون بود و هیچ پاسخی نمیدادن.
پیام دیگه ای از بچه ها:
من هاست خارجم نت افراز بود بکاپ داشتم ازش
هاست داخل هم از خود پارس پک گرفتم ریستور رو انجام دادند ولی سایت بالا نمیومد در نهایت تنظیمات رو خودمون انجام دادیم هم هاست هم cdn بعد اوکی شد الان هم خیلی خوبه هم سرعتش خوبه هم قطعی نداره
از داخل و خارج هم همزمان باز میشه
نظر من:
سایت Down میشه. برای من 24 ساعت down شد. ولی ارزید.
احتمالا پیام اول، مثل پیام دوم بوده مشکل فنیش ولی خودش از پس کار بر اومده.
جواب ندادن تیکت(بعد از فعال سازی) و... هم چیزی که بچه های پارس پک باید بررسی کنند که چرا چنین اتفاقی افتاده و چی بوده ماجرا.
من فیدبک رو میذارم اینجا. امیدوارم چه با روش من چه با روش خودتون، سایتتون رو در دسترس کنید و دیگه از وضعیت "در حالت انتظار" خارج بشید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/mohsentavoosiseo/646" target="_blank">📅 15:25 · 05 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-644">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUoiJCDv1fSZ_BJSFbW8rdkxEbDfbDDnY3fBsW-goRE-M4EqvOwQlc_MhGwDCfeemumDQy2h3zc-Kns-5_wPgQ2pD8fHyuPkLPun49O22gkBRJSJHbbMiHPT1VA9U5jnLzDgR2VmyfCqk6x6o5IZtAgYh2c8k4vp6I9uY4tBrxeoOxlQ2bBi9BBY2WvnhvWEJauYDReUE0xz98BFL14qJij7eCM0HRisASyVjFjJonOAuwR1sTbpyhZ4faaWXDRr8z36YCtt1rY4VAIvXasyZFR4fG6Bnp26ePffLD1TUhy1zfIMtzIR0PEU71Tx3c2jZG26Pyzp0LONxyJATcQoZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و البته ادامه دادن، یعنی سرور اولی هم از خارج هم از داخل در دسترسه. آموزششم بالاتر گفتم رایگان:
https://t.me/mohsentavoosiseo/623
این که دوره نیست. این که دیگه پولی نیست! این که با این نقل و نبات شدن اینترنت بین الملل وسط قطعی، دیگه هزینه ای نداره عملا.
دلیلی که انجام نمیدی چیه؟ بیا با طناب محسن طاوسی برو تو چاه! چاه خوبیه! قبلشم رو سایت خودم و چندین سایت دیگه تست شده.
قدیمی ها میدونن من نسخه تئوری الکی، نه تایید می کنم نه نقض و انکار میکنم.
اون میزان کم جریان مالی و تراکنشی که برات یا برای کارفرمات میاره کافیه! همه چیزم صد درصد باز شه چیزی ضرر نکردی! وقتی بقیه بازارشون صفر مطلق خوابیده بود، تو یه سودی کردی.
از همه مهمتر! بعد روانی موضوع و امید به حرکت هست. بخوای مهاجرت کنی پول نمیخوای؟ نباید بگذره روزگارت؟ که بعدا بری؟ انجامش بده!
رایگان یادم دادم و واضح و قدم به قدم(
اینجا
).
هیچی مستقیم و غیر مستقیم تو جیب من نمیره.
هزینشم برای خودت در حد خرید هاست داخل و خارجه و پول اینترنت برای انتقال بکاپ!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/mohsentavoosiseo/644" target="_blank">📅 13:22 · 05 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-643">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">از اینترنت طبقاتی استرس نگیرید.
🔴
آبان ۹۸ بحث اینترنت ملی داغ بود و موتورجستجوی ملی. دو هفته هم قطع کامل بود.  خیلی ها ترسیدن و رها کردن. زمان مهسا هم همینطور.
🔴
الان که در وسط شرایط جنگ و برزخ رو به بدتر شدن هستیم، اینترنت وصله. وسط جنگ ۱۲ روزه حتی گوگل باز…</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/mohsentavoosiseo/643" target="_blank">📅 22:43 · 04 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-642">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هوای هم رو داشته باشیم
✅️
چه قبلا قسط دادید چه قبلا اصلا پرداختی نداشتید، سعی می کنیم با شرایط فعلی شما در این شرایط ایران، بتونید تهیه کنید: @mohsentavoosisupport
✅
کسانی که قسط دوره داده بودند و مهلت تعیین کرده بودیم و قرار بود قیمتشون افزایش داشته باشه،…</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/mohsentavoosiseo/642" target="_blank">📅 17:47 · 04 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-641">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اکانت ChatGPT نسخه Plus روی ایمیل خودتون بدون نیاز به ارسال دسترسی، ماهانه با مبلغ 1100 (یک میلیون و صد هزار تومن) از طریق آی دی
@mohsentavoosisupport
قابل تهیه هست. (اشتراکی نیست).
❓
چرا قیمتش پایین هست. مگه 20 دلار بالای 3 میلیون تومن نمیشه؟
به این علت که یک بخش جدید به اکانت شما اضافه میشه و فقط اون بخش، پلاس هست.
فرض کنید یه پوشه باز میشه توی اون پوشه پلاس هست و خارج از پوشه پلاس نیست. و اون پوشه هم سر ماه حذف میشه.
عملا اگه حافظه و تاریخچه چت های جدید براتون مهم نیست بسیار به صرفه هست. حریم خصوصیتون هم کاملا حفظ میشه چون اشتراکی نیست.
✅
چت های قبلی و جدید خودتون که خارج از اون بخش و پوشه هست(مثل الان)، باقی خواهد ماند و دست نمیخوره و حذف نمیشه. اصلا کسی به اکانت شما دسترسی پیدا نخواهد کرد.
خرید:
@mohsentavoosisupport
————
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/mohsentavoosiseo/641" target="_blank">📅 14:58 · 03 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-639">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">احتمال سوم:
قطع موندن اینترنت بین الملل و وصل شدن بعضی جاها بصورت لیست سفید و استثنا</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/mohsentavoosiseo/639" target="_blank">📅 15:29 · 31 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-637">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee89341378.mp4?token=MCGBXmpLn7NQeRLQeiwY8czX1azTf1gioOTeiP_gJZQlgSGev6coRAO190p49wrUYAiGnUqxBsYNdM7Lk_l73Xl0jyQfuuOydjuyCQ83qhL3uZz3Js56d0ciHAVx5d1zawwPV-sROYm3kPj1EqyWmvKGnyXxWHjdlFxJTR_HaqEzyyc2GRmfSt7gzb9CSGPRt5KCZ2Xad1OBmzckKRHkpQYrHkJjhiDifmG4qDHudU6FY-w5mPckohsMiFvUBMTInivtLT2OQA0YF3nSJvpglKEGkeO8IJPsSEm0T2OpdC-f5t22pE0Lz-Vb935ji74pzf3hY55xoNAQyw55hQCdKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee89341378.mp4?token=MCGBXmpLn7NQeRLQeiwY8czX1azTf1gioOTeiP_gJZQlgSGev6coRAO190p49wrUYAiGnUqxBsYNdM7Lk_l73Xl0jyQfuuOydjuyCQ83qhL3uZz3Js56d0ciHAVx5d1zawwPV-sROYm3kPj1EqyWmvKGnyXxWHjdlFxJTR_HaqEzyyc2GRmfSt7gzb9CSGPRt5KCZ2Xad1OBmzckKRHkpQYrHkJjhiDifmG4qDHudU6FY-w5mPckohsMiFvUBMTInivtLT2OQA0YF3nSJvpglKEGkeO8IJPsSEm0T2OpdC-f5t22pE0Lz-Vb935ji74pzf3hY55xoNAQyw55hQCdKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/mohsentavoosiseo/637" target="_blank">📅 22:07 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-636">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دوستانی که نگران قطع موندن اینترنت هستند، این نظر شخصی من بدون قبول مسئولیت هست و من برنامه هام بر این اساس پیش میره همونطور که قبلا هم گفته بودم:  احتمال اول: وصل شدن دائمی اینترنت بین الملل بهتر از قبل یک بار برای همیشه بدون ترس مجدد از قطعی.   احتمال دوم:…</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/mohsentavoosiseo/636" target="_blank">📅 20:49 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-635">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">قبل از اینکه حرف اصلی رو بزنم این رو بگم که دوره از داخل ایران در دسترس هست.
✅
اما در این شرایط چیکار کنیم و خودم چیکار میکنم؟
✅
برای کسانی که ایران هستند: تولید محتوای فارسی و کمپین های رپورتاژ و محتوای داخلی وب سایت و استخراج عنوان ها با ابزار های داخلی…</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/mohsentavoosiseo/635" target="_blank">📅 19:50 · 26 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-634">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خیلی ها نمیدونن میرور چیه کلون چیه.</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/mohsentavoosiseo/634" target="_blank">📅 14:39 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-633">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سایت من از داخل و از خارج در دسترس شد و چه مراحلی طی کردم؟
mohsentavoosi.com</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/mohsentavoosiseo/633" target="_blank">📅 14:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-631">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">روش راحت بالا اومدن سایت از داخل و خارج! بدون پیچوندن بدون GEO DNS!
امیدوارم هیچ وقت به چنین چیزی دیگه نیاز پیدا نکنیم.
آرزو میکنم به محض اینکه اینکارو کردید پشیمون شید بخاطر وصل شدن ابدی اینترنت بین الملل. آرزو میکنم زحمتتون هدر بره! می ارزه!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/mohsentavoosiseo/631" target="_blank">📅 14:21 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-630">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فاز امید الکی دادن ندارم. صحبت من فنی هست. انتخاب های متعددی پیش رو داریم. ولی من همیشه دست و پا زدن و یه کاری کردن رو ترجیح میدم به هیچ کاری نکردن. هیچ کاری نکردن و تماشاچی بودن و منتظر بودن من رو از پا میندازه. ته چاه باشم ترجیح میدم دیوار چاه رو بکنم تا بشینم منتظر باشم بالا رو نگاه کنم.
دست و پا برای بقا همیشه مثل فیلم Pianist  نیست. یکیشم مثل وضعیت الان ماست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/mohsentavoosiseo/630" target="_blank">📅 11:36 · 22 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-629">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
اما در این شرایط چیکار کنیم و خودم چیکار میکنم؟
✅
برای کسانی که ایران هستند:
تولید محتوای فارسی و کمپین های رپورتاژ و محتوای داخلی وب سایت و استخراج عنوان ها با ابزار های داخلی کاریه که میشه انجام داد و شما رو جلو میندازه. ماه های بعدی دیگه این مراحل رو تکرار نکنید. برای سه ماه بعد اصلا جلو جلو انجام بدید.
اگر هم سرور داخل هست، بهینه سازی داخلی هم میتونید انجام بدید.
✅
برای کسانی که خارج از ایران هستند:
دوباره باز تولید محتوای داخلی، استراتژی و عناوین محتوای داخلی و آف پیج! به کلی ابزار هم که راحت دسترسی دارید! بهتر نیست از رقبایی که فقط درگیر خوندن اخبار هستند جلو بیفتید؟</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/mohsentavoosiseo/629" target="_blank">📅 11:36 · 22 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-628">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">برای پارس پک origin rule هست روی سرویس CDN. و GEO DNS نیست! به گفته خودشون دقت origin rule بسیار بالاتره و ارزون تر هم هست کلا:
https://parspack.com/cdn</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/mohsentavoosiseo/628" target="_blank">📅 18:18 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-627">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">درباره یک سری ابزار های جستجوی داخلی از اونجا که دوست ندارم این وضعیت رو دائمی ببینم و عادت بشه و تبلیغ کنم، اسم نمیبرم.
ولی اون ها ترکیبی از گوگل و بینگ هستند به علاوه یک سری شخصی سازی ها و اسلامیزه شده.
شرط اول اینه که هم از داخل هم از خارج بالا بیاد سایتتون که تو پست های قبلی توضیح دادم.
چون اینا خودشون از بینگ و گوگل دیتا میگیرن، گوگل سایت شما رو نبینه اینا هم نمیبینن.
اگرم گوگل ببینه و کاربر داخل باز نکنه سایتتون باز نمیشه و بازم فایده نداره.
بقیش همون سئویی هست که بلدید ولی یک کم سنتی تر. مثلا اگزکت مچ بک لینک با عین کیورد مهم تر هست برای بینگ. و بینگ هنوز به متاکیوردز کار داره.
آموزش سئو بینگ و چت جی پی تی ChatGPT
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/mohsentavoosiseo/627" target="_blank">📅 17:15 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-626">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پست های بالا ویرایش شد. دوباره ببینید. تو اپ های داخلی هم برای کسانی که اینترنت ندارند بفرستید شاید مفید باشه براشون.</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/mohsentavoosiseo/626" target="_blank">📅 17:09 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-625">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">این متن هم محمدرضا زراعتی از بچه های پارس پک و دوست شفیقم برام فرستاد. با شما به اشتراک میذارم. درباره SSL هاست های داخل:
راستی محسن جان الان سایتهایی که داخل ایرانن به خاطر همین قطعی ها مشکل خطای ssl میگیرن چون احراز هویت دامنه پیش‌فرض از روش HTTP هندل میشه برای همین ریکوئست های از صادر کننده سرتیفیکیت نمیرسه به ایران
راهش اینه که اعتبارسنجی ssl رو از روش DNS انجام بدن دیگه مشکل حل میشه.
تو این اموزش یاد دادم چطوری با CDN پارس پک بتونن هندل کنن(برای ssl بر خلاف ارجین رول نیاز نیست دیگه ابر cdn روشن بشه فقط از رکوردهاش استفاده میکنن)
https://docs.parspack.com/ssl/free-ssl-issue-iran-access/
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/mohsentavoosiseo/625" target="_blank">📅 17:00 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-624">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سایت من از داخل و از خارج در دسترس شد و چه مراحلی طی کردم؟  mohsentavoosi.com
1️⃣
اول انتقال بکاپ. که بسیار سخت بود. انتقال بکاپ 10 گیگی از خارج به داخل سخت بود از نظر قطع شدن و سرعت(الان راحت تره خیلی).
2️⃣
دوم خرید هاست در دوطرف. هاست من از قبل آلمان بود.…</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/mohsentavoosiseo/624" target="_blank">📅 16:57 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-623">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سایت من از داخل و از خارج در دسترس شد و چه مراحلی طی کردم؟
mohsentavoosi.com
1️⃣
اول انتقال بکاپ. که بسیار سخت بود. انتقال بکاپ 10 گیگی از خارج به داخل سخت بود از نظر قطع شدن و سرعت(الان راحت تره خیلی).
2️⃣
دوم خرید هاست در دوطرف. هاست من از قبل آلمان بود. ایران هم گرفتم.
3️⃣
سوم پیدا کردن جایی که بتونه تقاضای داخل و خارج رو هندل کنه و کار GEO DNS یا سرویس مشابهی انجام بده (مثل قابلیت origin rule). که از اونجایی که از قبل من مشتری پارس پک بودم، این کار انجام شد.
برای پارس پک origin rule هست روی سرویس CDN. و GEO DNS نیست! به گفته خودشون دقت origin rule بسیار بالاتره و ارزون تر هم هست کلا:
https://parspack.com/cdn
پس قدم سوم شد خرید CDN با قابلیت GEO DNS یا Origin Rule (که پارس پک اورجین روله ووبهتره و ارزونم هست)
4️⃣
چهارم دامنه من از شرکتی خریده شده بود که داخل بود و امکان تغییر DNS نداشت. سر اینکه بتونم دی ان اس دامنه خودم رو عوض کنم هم کلی مکافات داشتم و تیکت زدن و... .
5️⃣
و در نهایت با تنظیمات توی پارس پک(تیکت) که واسط بین داخل و خارج بود کار انجام شد.
‼️
راستی میرور و sync نیست! یعنی هاست داخل من عوض شه خارج نمیشه. اگه فروشگاهی باشید سبد خرید و سفارش های هاست خارجتون با داخلتون هماهنگ نیست. من روش هماهنگ رو بلد نیستم. برای من جداست. اهمیتی هم برام نداره.
اگرم فروشگاه باشید اکه بتونید سفارش هایی که با وی پی ان و بی وی ان مدیریت کنید هم کار تمومه. اکثرا دسترسی از خارج رو برای گوگل میخوان و سینک بودن براشون مهم نیست. ملاک رو میتونید دیتای ایران در نظر بگیرید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/mohsentavoosiseo/623" target="_blank">📅 16:51 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-622">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">از عادی سازی نکردن دی، رسیدیم به اینکه چطوری درامدمون رو در حد بقا حفظ کنیم تا به شرایط عادی یک بار برای همیشه برسیم...
ادامه موارد زیر جهت کمک هست. دست و دلم به پست و تولید محتوا نمیره. ولی میدونم با همین چند تا پست ممکنه کار چند نفر راه بیفته.</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/mohsentavoosiseo/622" target="_blank">📅 16:47 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-620">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رسید مژده که ایّام غم نخواهد ماند
🔆
شماره در زمان اینترنت ملی در پیام رسان "بله" (متاسفانه):  جهت موارد دسترسی به دوره، خرید، قسط و...: 0919-268-19-56  سایت mohsentavoosi.com از داخل و خارج حالا باز میشه(اپدیت فروردین ۴۰۵)
🔆
🔆
🔆
رسید مژده که ایّام غم نخواهد…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/mohsentavoosiseo/620" target="_blank">📅 19:27 · 08 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-619">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بیشتر از آمادگی بابت قطعی های مقطعی اینترنت ایران و دسترسی از خارج،  در فکر آمادگی برای تغییر قوانینی هستم که در سود و زیان وب سایت ها موثره و بازی رو عوض میکنه. آیا خدمات و محصولات شما بعد از تغییرات بزرگ همچنان تقاضا یا سود داره‌؟  بر خلاف تصور عموم، به…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/mohsentavoosiseo/619" target="_blank">📅 17:27 · 18 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-616">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بیشتر از آمادگی بابت قطعی های مقطعی اینترنت ایران و دسترسی از خارج،
در فکر آمادگی برای تغییر قوانینی هستم که در سود و زیان وب سایت ها موثره و بازی رو عوض میکنه. آیا خدمات و محصولات شما بعد از تغییرات بزرگ همچنان تقاضا یا سود داره‌؟
بر خلاف تصور عموم، به عقیده من کسب و کار های مهاجرتی، همچنان پررونق تر و راحت تر پیش خواهد رفت.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/mohsentavoosiseo/616" target="_blank">📅 19:33 · 03 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-613">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آموزش سئو محسن طاوسی
pinned «
هوای هم رو داشته باشیم
✅️
چه قبلا قسط دادید چه قبلا اصلا پرداختی نداشتید، سعی می کنیم با شرایط فعلی شما در این شرایط ایران، بتونید تهیه کنید: @mohsentavoosisupport
✅
کسانی که قسط دوره داده بودند و مهلت تعیین کرده بودیم و قرار بود قیمتشون افزایش داشته باشه،…
»</div>
<div class="tg-footer"><a href="https://t.me/mohsentavoosiseo/613" target="_blank">📅 12:19 · 24 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-611">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ما نهایت همکاری رو داریم می کنیم همه جوره که دسترسی همه با مبلغ کم راه بیفته تو اسپات پلیر</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/mohsentavoosiseo/611" target="_blank">📅 16:03 · 12 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-610">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این پیام رو به کسانی که اینترنت ندارند هم برسونید: الان که شرایط جنگیه و نمیدونیم یک هفته دوهفته ادامه داره یا یکی دوماه تا وصل شدن اینترنت، اگر قسطی دسترسی به دوره داشتید، با مبلغ خیلی کمتر میتونید دسترسی رو کامل کنید یا اگر ندارید جدید بخرید. هم به خاطر…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/mohsentavoosiseo/610" target="_blank">📅 17:18 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-609">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">این پیام رو به کسانی که اینترنت ندارند هم برسونید: الان که شرایط جنگیه و نمیدونیم یک هفته دوهفته ادامه داره یا یکی دوماه تا وصل شدن اینترنت، اگر قسطی دسترسی به دوره داشتید، با مبلغ خیلی کمتر میتونید دسترسی رو کامل کنید یا اگر ندارید جدید بخرید. هم به خاطر…</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/mohsentavoosiseo/609" target="_blank">📅 22:26 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-608">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اگر سرورتون داخل ایران هست، الان از ایندکس خارج شده صفحاتش.  اگر سرورتون خارج از ایران هست، مشکل گوگلی و ایندکسی نداره ولی کاربر داخل ایران بهش دسترسی نداره.  راه حل؟ هیچ راه حلی نداره. راه حل اینه که کلا اینترنت بین المللی قطع نشه. اگر هاست داخل و سی دی ان…</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/mohsentavoosiseo/608" target="_blank">📅 19:19 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-607">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اگر سرورتون داخل ایران هست، الان از ایندکس خارج شده صفحاتش.
اگر سرورتون خارج از ایران هست، مشکل گوگلی و ایندکسی نداره ولی کاربر داخل ایران بهش دسترسی نداره.
راه حل؟ هیچ راه حلی نداره. راه حل اینه که کلا اینترنت بین المللی قطع نشه. اگر هاست داخل و سی دی ان خارج کار کنه، باز اینترنت بین الملل یک کم بازه. چیزی که میگم در شرایطی هست که اینترنت بین الملل قطعه.
حتی دی ان اس هم در زمان قطعی اینترنت نمیتونید عوض کنید. چون دی ان اس هم با اینترنت بین المللی هست. ممکنه آی آر ها رو بتونید روی هاست داخلی. که در این صورت گوگل نمیبینه. کاربر میبینه.
در نتیجه، الان یکی از حالت های زیر اتفاق میفته برای همه سایت های با مخاطب ایرانی:
1- از ایندکس خارج شدن و حذف شدن از گوگل (هاست داخلی ها)
2- کاهش رتبه و عدم دریافت ترافیک از کاربر(هاست خارج ها)
امیدوارم یک بار برای همیشه این مشکلات ما تموم بشه و ما مردم ایران، بعد از چند دهه، نفس راحت بکشیم و طعم آزادی و امید و تکاپو و رونق و رشد رو بچشیم و دیگه کف خیابون کشته ندیم
🖤
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/mohsentavoosiseo/607" target="_blank">📅 20:45 · 30 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-606">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🟢
ساده لوحی در SEO
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/mohsentavoosiseo/606" target="_blank">📅 21:24 · 06 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-605">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔍
این به روزرسانی سومین تغییر هسته ای گسترده در سال 2025 است و مانند نسخه های قبلی، هدف آن ارتقای کیفیت و ارتباط محتوا برای کاربران در سراسر جهان است.
🔍
این به روزرسانی صرفا روی یک بخش خاص تمرکز نمیکند؛ با بازتعریف معیارهای رتبه بندی، توانایی گوگل در ارزیابی محتواهای مرتبط، مفید و رضایت بخش را افزایش میدهد.
🔍
گوگل بار دیگر نشان میدهد که ارزش واقعی در محتواهای با کیفیت و تخصصی است، به ویژه در زمینه هایی مثل پزشکی و سلامت که E-E-A-T (تجربه، تخصص، اقتدار و اعتبار) نقشی حیاتی در رتبه بندی دارند.</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/mohsentavoosiseo/605" target="_blank">📅 16:49 · 04 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-604">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/mohsentavoosiseo/604" target="_blank">📅 11:48 · 04 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-603">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_lzV8WPvl-Bup8ETsqLVbj_OdrnU5r-L7SPdFtZVVR--0W5iRZlRzceeOgCnmuigOG_dZiT4beMUyHew-ofKG-N7XrzuM4Dy9paqD_C0BrLahHrvCujlW1xrMezHPEKhhz5bezvRNRciovFUkAwOv1AtuSeGbM-qZ5a29xXWhC6jr0yZ5eLVyIw8es3y_uBsJEuTwx6PXKWkzVH1lqDM5M2zorOswA3SFNWcJ_5p5SzR8RAIM8RXW1Jq6nSR6-iZYxt4n67MVX1d1coZa6BEMftKK7oenzcbDqIOW_msETk1CFViqT-wn1O-JvIm-4dh1_KU04KnLjoWYMDtxLbUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
تو ویس های بالا توضیح دادم
✅
اینم سایت های من که تو اپدیت ها تکون نمیخوره. همیشه همینه. آخرین چیزی که من بهش توجه می کنم آپدیت های گوگله! چون مسیر من ثابته همیشه. به صورت کلی در دراز مدت رو به رشد بر اثر فعالیت های من و با توجه به رقابت موجود.
📎
اسکرین شات سرچ کنسول. شماره 3
💵
درامد این سایت: ماهانه + 40 م.ت خالص
⁉️
تو ذهنت اینه که سایتی که روزی بیست سی تا ورودی گوگل داره درامدش ماهی 40 تومن
نمیشه؟ آره با آموزش های غلط و بی بازده سئو و تحقیق کلمات کلیدی اشتباه و صفحه بندی و تارگتینگ اشتباه، کاملا حق با توست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/mohsentavoosiseo/603" target="_blank">📅 17:38 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-602">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDEVjYqFEkplJIxODUxKRox4jTFI2ko8rYYmPFgNX34D8OrYXB9uxtDQf2YT1yQlhpvyNLmpMUMSIPNNB1NcecfX2A37gX_lrSdrUnxhBC1NZvn3qR-1IkuCfvHrp6xXTefCue9rvf88F5DH-Cgxz_l6_gmMwq4dHFjCmEovLTlcYUjtXVlQbbanqKnv7QeU1F0Yka7kPphBGGeGlk9KbMKEFv75rEb1RX23Sjz15_Nwfc35Rt8vrcZqQi7VGUkq_DmHlwKzKSs1DskmtazL706WzQJB4KrtIjx4l3w6wKYr1SZbTG_iZYrVF01Xecx94Zs3mCbYZZUAot82XkKU9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
تو ویس های بالا توضیح دادم
✅
اینم سایت های من که تو اپدیت ها تکون نمیخوره. همیشه همینه. آخرین چیزی که من بهش توجه می کنم آپدیت های گوگله! چون مسیر من ثابته همیشه. به صورت کلی در دراز مدت رو به رشد بر اثر فعالیت های من و با توجه به رقابت موجود.
📎
اسکرین شات سرچ کنسول. شماره 2
💵
درامد این سایت: بالای معادل 200 م.ت. به صورت دلاری. غیر فارسی. مال من نیست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/mohsentavoosiseo/602" target="_blank">📅 17:38 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-601">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E26OxNLdX96pE1RYNo_uJQqrQQ8_wHlana3m3GN4vrQfJ4gIF14OLQmLeXrBsHtPUg9pqRD1_LMMQkUfSEvAxQexxFfN42oKpLCejcdjFtf5iFLpTVhCV6046DZjbRnVl7n3HbhQifJlozhqBXOaOLnjgsACSEA9PMADr-Jo7Y90e4n19lT9NmFywCAPV9xKf0KpxJ7ksJ3F57cFbftq_0Gp-Rc7-yVqllcY0_iEtc6j7Ru8qUO1jM6N1xFwYRJISbWUGH_uip7mDq2S6geeE1NtSe3HGSDC7dcnjTWVEWzlVadOIKYdrfrzrr4wlY893u4zPumx8BnRqhvlVbNmmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
تو ویس های بالا توضیح دادم
✅
اینم سایت های من که تو اپدیت ها تکون نمیخوره. همیشه همینه. آخرین چیزی که من بهش توجه می کنم آپدیت های گوگله! چون مسیر من ثابته همیشه. به صورت کلی در دراز مدت رو به رشد بر اثر فعالیت های من و با توجه به رقابت موجود.
📎
اسکرین شات سرچ کنسول. شماره 1
💵
درامد این سایت: ماهانه + 300 م.ت خالص
⁉️
نرخ تبدیلش بالاست؟ درسته. این برمیگرده به استراتژی تحقیق کلمات کلیدی شما.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/mohsentavoosiseo/601" target="_blank">📅 17:38 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-600">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کلا این صورت مساله که وای الان چیکار کنم گوگل آپدیت کرد، از دیرباز صورت مساله غلطی بود، صورت مساله غلطی هست و صورت مساله غلطی خواهد بود.
تمام پست های انگلیسی سایت های دیگه خیلی از زبان های دیگه هم از اون ها کپی و ترجمه میکنن و درباره راه کارهای افت بعد از اپدیت هست، کلیشه چرت و پرتی بیش نیست!
مثلا میگن تکنیکالتو چک کن! بک لینک های غیر طبیعیتو حذف کن! عنوان ها تو بازبینی کن!
ولی این محتوای بلغور چرت متقاضی داره بهرحال. ترافیک میاره برای اون سایت ها. می طلبه که بنویسن. چهار نفر هم بیان بگن ممنون از پست مفیدتون! اما نفهمن خب آخرش چیکار باید کنن! فقط ذهنشون مبهم تر میشه.
https://www.linkedin.com/posts/mohsentavoosi_aebaeoaew-activity-7409525124615348224-5vg8
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/mohsentavoosiseo/600" target="_blank">📅 13:19 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-599">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تو آپدیت گوگل چیکار کنیم؟
قسمت دوم
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/mohsentavoosiseo/599" target="_blank">📅 12:44 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-598">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تو آپدیت گوگل چیکار کنیم؟ چرا افت کردیم؟ راه حل چیه؟ کجا رو بخونیم بفهمیم چه تغییری بدیم؟
قسمت اول
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/mohsentavoosiseo/598" target="_blank">📅 12:44 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-597">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">معلم زبان عالی ولی غیر تجاری!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/mohsentavoosiseo/597" target="_blank">📅 12:34 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-596">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">😶
جمع کردن توشه برای آخرت و رستاخیر و جهان پس از مرگ، با تولید محتوای رایگان در راه رضای خدا و خشنودی خلق خدا، یا پول گرفتن بابت محتوا؟
😶
شاخص های تفکیک ذهنیت کودکانه با ذهنیت بالغ و تجاری
😶
قهرمان بازی و کمونیسم!
😶
چی شد من دوره فروختم؟
😶
شهرت باید درامدزا باشه و نرخ تبدیل داشته باشه! شهرت خالی به درد نمیخوره! دردسر های شهرت نسبی من در حوزه SEO!
😶
مدل کسب و کار تلگرام و گوگل چطوریه و آیا ما میتونیم مثل اونا کار کنیم؟
😶
تلگرام مگه نگفته بود همیشه رایگانه چرا پولی شد؟
😶
😶
آدم خوب نایس گوگولی اصلاح گر بچه مبصر رابین هود نجات دهنده، چرا سرخورده خواهد شد؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/mohsentavoosiseo/596" target="_blank">📅 19:15 · 02 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-595">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🟢
حرفه ای بودن به سابقه زیاد نیست
تفاوت SEO specialist با senior seo و junior seo چیه
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/mohsentavoosiseo/595" target="_blank">📅 18:08 · 30 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-594">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تو ابزارهای اشتراکی، قطعی ها و ایراد ها و اینکه یهو میگه تو حداکثر ظرفیتو استفاده کردی(با اینکه نکردی)؛ رو بپذیرید!
طبیعیه. همون لحظه رسیدن به محدودیت اکانت، نمییتونن درجا شارژ کنن. دستی انجام میشه.
پول کم میدیم که استفاده کنیم فرقش همین چیزاست. قطعی، یه روز یهو از کار افتادن تو زمان مهم، غیر فعال بودن فیچرای دیگه همون ابزار و...
بدون مشکلش رو میخوایم باید پول دلاری کاملش رو با مسترکارت مجازی یا واسطه بدیم و بخریم با ده ها برابر قیمت اونم به ازای تک تکشون.
ما اشتراک ماهانه SAAS, software as a service رو نمیدیم و بجاش با نیم میلیون تومن ماهانه ده تا SAAS رو همزمان میگیریم. نمیشه انتظار بیشتری داشت.
لیمیت پس (کد تخفیف mohsentavoosi)
نوین ترند
فعلا اصلی ها هستن. هر جای دیگه ای ارائه بده تفاوت زیادی نمی تونه ایجاد کنه. مگر تو ظاهر مثل یو آی یو ایکس و راحتی نصب و دسترسی.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/mohsentavoosiseo/594" target="_blank">📅 21:00 · 29 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-593">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/mohsentavoosiseo/593" target="_blank">📅 23:16 · 24 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-592">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🟢
تعداد ریکوئست مهم نیست
کاهش تعداد Request در سایت اختصاصی و وردپرس
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/mohsentavoosiseo/592" target="_blank">📅 15:29 · 24 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-591">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4bapwZLRJAHcPT4vFOFLomCeidx9L8M_wO63sDAIjC2MizW_eBK59h6H9Ftw-qPr4LsfE_iDnSh-QGTy1OcaiYK6MmMRSkv9qUyFry1paOxydYh4lc1agsi3MBBbXm6WN0IzutkxwY8J7nJH6SlCWSyvMcBI2M88MxhvXpNqVGX3yW-Ko-KwPR6Rb6wtNGjNb3Nu76RgUtw5spS7TMIvfgyAyoaB1vYfHlRUCuUU4XWXY1bw9aP79y3nWy7TtAYCpI2HhJJ_O-cl5pZUQV9Tl07NIEP2yqYqSZYXTUTFh7nrhxKeBNleEl2M6WKtzYr7wLUjimj3T7hcKLNT_vMxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://eseminar.tv/webinar/%D8%B1%D9%88%DB%8C%D8%AF%D8%A7%D8%AF-%D8%AD%D8%B6%D9%88%D8%B1%DB%8C-%D8%B3%D8%A6%D9%88%D9%84%D8%A7%D8%A8%D8%B1%D8%A7%D8%AA%D9%88%D8%B1%DB%8C-%DB%B4
در این رویداد حضوری، قراره من و جمعی از دوستان در پنل درباره بحث قیمت و بازدهی رپورتاژ ها در سئو از نظر فنی و تجاری صحبت کنیم.
من برگزار کننده نیستم و صرفا یکی از اعضای پنل هستم.</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/mohsentavoosiseo/591" target="_blank">📅 20:59 · 23 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-590">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🟢
Disavow & Ahrefs
دیسوو گوگل هیچ ربطی به سایر ابزار ها نداره
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/mohsentavoosiseo/590" target="_blank">📅 17:11 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-589">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اشتباه ها و تفکر اشتباه رایج پروژه گرفتن در این زمانه
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/mohsentavoosiseo/589" target="_blank">📅 12:05 · 18 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-587">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icgon4cgrtcbqV7cXvLKg8aCOlmzvIXmoH3RCs-izUjh2oFmDyLRbqQd10XnKdzEGU_eDzvqvxhrQ9NCNlpQVYSHeO1OHPK_cI7kxVWF3Var1Vw7I40dLhCneZuwRpk0KICJQUNOPvEyE2wcPEh_R8jYhW_3tYfsskzkXZGP-RnRn_Ro66XWnNmFFubxw-fZhAdKbUhGB827sa3StJ3eZvLPA46zghoKlQJ8e7_CosyWCdMxm1QW5kOTX6E1CdK1JvqWHi0sHkx6iQVqzhZWvd7IJqcZIpo1w7GijyiYN6xDBveShKVaHkI1Qc_X17PR4zRDpj1UjmRgORdFZuQvDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ۷۸٪ تخفیف خرید رپورتاژ (انواع بک لینک)
تا ۳۵٪ تخفیف سفارش محتوا
از ۹ تا ۲۲ آذر
لینک مشاهده جشنواره
.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/mohsentavoosiseo/587" target="_blank">📅 13:38 · 12 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-585">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🟢
اسکرول نامحدود یا کلید مشاهده بیشتر؟
این ویدیو دارای یکی از نکته های مهم سئو تکنیکال هست
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/mohsentavoosiseo/585" target="_blank">📅 19:34 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-584">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🟢
مالیات سایت
با باید ترسید و فاصله گرفت یا باید رفت تو دلش!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/mohsentavoosiseo/584" target="_blank">📅 17:42 · 10 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-582">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQZ37x9tWJDeADe3H6ndyZV5tF7Ht6ApUgMDPBwathISvyB72d0uI2G7QHYNu3HaVvy2newjUwqQxZWVU7poujexE6WwQLy8BV7CFhQgnbba_LsxbrDYhCJliftQmGSbxIr8zc8IQyDCSYAuydaWVw_lUrgT97CdvmqPisGMMMG9E-yHHoLm5mt5jQ_hhuqC6pGoo19_bXnzzMXBnYCTbdWYzUbNpPB0rJlDjzokpmSTDwtHQsytUgHchw9tG5tTo277bHcfyyM_U8gx-czkNiYcgKOHVf7ky5jtMkrSf1IS9KDtdxogxRGjemyOQZs5kZQ_freO3_-gZKBxzbxtyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوباره خرید اشتراک Ahrefs ممکن شد. بخش Link Explorer و Content Explorer در دسترس هست.  با محدودیت تحلیل روزانه ۵ دامنه.  کد تخفیف: mohsentavoosi  لینک خرید: https://limitpass.com/clients/cart.php  بسته Titan یا Ahrefs Standard هر دو Ahrefs دارن.  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/mohsentavoosiseo/582" target="_blank">📅 17:27 · 08 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-581">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🟢
عنوان رپورتاژ
حرفه ای یا آماتور؟
انتخاب عنوان رپورتاژ تو فرآیند سئو خارجی خودش یه تخصص و یک دنیای وسیعی هست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/mohsentavoosiseo/581" target="_blank">📅 17:23 · 08 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-580">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅️
سئو برای حساب کتاب دقیق نیست. باید حدس و گمان و عدم قطعیت رو بپذیری.
❗️
Data driven SEO
مزخرفی بیش نیست از نظر سنجش تاثیرگذاری ریز کارها با قطعیت در رتبه گوگل
⁉️
ساده لوحی تو سئو چه شکلیه؟
❗️
جمله "فقط به مستندات گوگل توجه کن" چرته و یه سوپر بولشیته. ولی معنیش این نیست که به مستندات گوگل توجه نکنیم!
⁉️
ادبیات گوگل چه شکلیه؟
اگه ذهنت به هم ریخت ویس رو گوش کن کامل. دلایل اینا رو گفتم. به متن اکتفا نگن. بیا اصلا این موضوع رو به چالش بکشیم از توش یه خروجی خوب در بیاریم.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/mohsentavoosiseo/580" target="_blank">📅 23:12 · 07 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-579">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رقابت گوگلی با برند های قوی
🟢
برای چیره شدن در رقابت با سایت های بزرگ و برند علاوه بر اینکه باید حداقل های مالی تامین باشه، انتخاب کلمات کم رقابت و صفحه بندی و تارگتینگ دقیق و فرصت طلبانه به شدت مهم هست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/mohsentavoosiseo/579" target="_blank">📅 20:28 · 06 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-578">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🟢
رتبه گوگل ایران و خارج و VPN
فصل سئو بین المللی دوره کامل به این موضوع پرداختم و واقعا موضوع ساده هست درباره رتبه گوگل در داخل ایران و در خارج از ایران
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/mohsentavoosiseo/578" target="_blank">📅 16:45 · 05 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-577">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVV8dxc71gqqknsCDSIdagCPTg2EfT40qZRtvYZ2-qdZ1lxzCRZyACaxaqXGFqQSSUsYNNknZMf24Iq9YpXqKpumBNCp3tIcb_PRhuUcKNp0u4jw1d4qB-Uzm8DpzSKQxbuM6DdAN-FLxxHN0oVDom-ZZR87p1U-KTuSxCCM7bFBoAardPH-jGgklLhwlfTLhNVFHpjgL7in4e92vZ6bMD2G34NQxhIY2CyFasX6cP_00c870eJxi4_wCjssCL2CpQ8P2RMe04-FOR1uUVDaAK1_nsus_kPLkIFacSntAGMFf5is13xEb2oYmXZX7F0dox4JvZnT6PTww502Eb7M0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته هایی که از نظر من مهمه. اما پراکندست و تک موضوع نیست. قسمت اول.
توضیحات زیر ویدیو، فهرست زمانی داره.
https://www.youtube.com/watch?v=P9NGXdQF1Ks
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/mohsentavoosiseo/577" target="_blank">📅 13:46 · 05 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-576">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">به خدا من زنده ام!
تفکری که وسط نداره. یا باید آمپر بچسبونه یا باید یخ بزنه.
مهم پوله. وردپرس و افزونه برای من و شما و پدران ما نیست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/mohsentavoosiseo/576" target="_blank">📅 13:01 · 05 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-575">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🟢
کمپین رپورتاژ سئو
اف پیج سئو اصلا به این سادگی ها نیست!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/mohsentavoosiseo/575" target="_blank">📅 14:25 · 04 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-574">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🟢
رتبه گوگل سایت خدماتی
اولویت بندی کلمات کلیدی سایت های خدماتی مثل بقیه سایت ها شاخص های یکسانی داره. ویدیو رو ببین.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/mohsentavoosiseo/574" target="_blank">📅 12:27 · 03 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-573">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🟢
بک لینک Sitewide
لینک سایت واید نزن!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/mohsentavoosiseo/573" target="_blank">📅 09:46 · 02 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-572">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🟢
کسب رتبه گوگل در یک ماه
این ماجرا افسانه ای بیش نیست که سریع بیایم بالا و بعد بریم پایین
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/mohsentavoosiseo/572" target="_blank">📅 09:18 · 01 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-571">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">از ۱ آذر افزایش قیمت دائمی داره دوره.  طبق معمول هر سال که کمپین فروش و تخفیف نداره. حتی نوروز. و هرسال نزدیک زمستون افزایش قیمت داره.  https://mohsentavoosi.com/video/seo-course/</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/mohsentavoosiseo/571" target="_blank">📅 09:55 · 30 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-570">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ویدیوی کامل:
https://youtu.be/P9NGXdQF1Ks
نکته هایی که از نظر من مهمه. اما پراکندست و تک موضوع نیست. قسمت اول.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/mohsentavoosiseo/570" target="_blank">📅 14:33 · 29 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-569">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🟢
ریدایرکت گروهی
چطوری به صورت دسته جمعی، صفحات سایت رو ریدایرکت کنیم؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/mohsentavoosiseo/569" target="_blank">📅 13:08 · 29 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-568">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔆
من در اینستاگرام اعلام کرده بودم که تا ۲۵ مرداد و الان تا پایان شهریور، قصد دارم حداکثرم تلاشم رو در این شرایط برزخی کشور انجام بدم که کسانی که قصد صد خرید دوره رو دارند ولی توان پرداخت ندارند، بتونن تهیه کنن.  چه نقدی چه قسطی، شرایط ویژه ای در نظر گرفتم.…</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/mohsentavoosiseo/568" target="_blank">📅 12:22 · 28 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-567">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a79e28f998.mp4?token=NywguxoZT0Olb9R9Z4L3YpKAfSkjjZ6WQASwLzKMDSaPXwQP81UOSDKiWEF_wf-jG-YRWU-1kHjBvbIWm6gp_6-iO57MM-27a28F4vzfrEIvcNC2kJ0pBsoXp_Ag0LQRukC6ljRe5xvHr5fgeTtr1qrQPSaEzT0pS1j_JBlqBIylBAe_uiCIMqW6rEBSbHc64qU-6tWt9a1l2qSrASokKZ3Qe0FbzSysP2zfJyWDXlFNe1CWrcxZroeZFVl6TAFB-NAxOhA1hV28m4Zr5P5cB6cd1Q3s3NF8t-9XSikBZVZ8j0S0ekFflN5dp7WMREypVmACNn1RXoXuunDCIbzR0Hs-DTjzhqQ4SaFVpr8tKtlg74zTb3O0B1jaCn9OsDAfPefblus4DM3KolGGRTzCpmdJdI4EVVZVv6vp9PKjs0wCnwAEn6AljvS0WGsw3vvaTGR-3Ip6IvFOxbQRaH8PzBwGXN19uzTPXbfwXFfObK5cFE61uBuwfr3Ngt3iovcnaZxyxS0tB09M-MFD9Mxfg1-WF8OQhawWPSXLcrze2YrwviQfrgVvEk7TF0Rk0yXSGeB9SLJyj2nwQW1Y8alAXcrINIwXGv_OMapST7G6DwaVaPwxk_QH4gBnOQErviZeAYwWNR1mwNzGsp7fjzKPpUJG7jfyHQ15hWqOTIhaOII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a79e28f998.mp4?token=NywguxoZT0Olb9R9Z4L3YpKAfSkjjZ6WQASwLzKMDSaPXwQP81UOSDKiWEF_wf-jG-YRWU-1kHjBvbIWm6gp_6-iO57MM-27a28F4vzfrEIvcNC2kJ0pBsoXp_Ag0LQRukC6ljRe5xvHr5fgeTtr1qrQPSaEzT0pS1j_JBlqBIylBAe_uiCIMqW6rEBSbHc64qU-6tWt9a1l2qSrASokKZ3Qe0FbzSysP2zfJyWDXlFNe1CWrcxZroeZFVl6TAFB-NAxOhA1hV28m4Zr5P5cB6cd1Q3s3NF8t-9XSikBZVZ8j0S0ekFflN5dp7WMREypVmACNn1RXoXuunDCIbzR0Hs-DTjzhqQ4SaFVpr8tKtlg74zTb3O0B1jaCn9OsDAfPefblus4DM3KolGGRTzCpmdJdI4EVVZVv6vp9PKjs0wCnwAEn6AljvS0WGsw3vvaTGR-3Ip6IvFOxbQRaH8PzBwGXN19uzTPXbfwXFfObK5cFE61uBuwfr3Ngt3iovcnaZxyxS0tB09M-MFD9Mxfg1-WF8OQhawWPSXLcrze2YrwviQfrgVvEk7TF0Rk0yXSGeB9SLJyj2nwQW1Y8alAXcrINIwXGv_OMapST7G6DwaVaPwxk_QH4gBnOQErviZeAYwWNR1mwNzGsp7fjzKPpUJG7jfyHQ15hWqOTIhaOII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
انتخاب عنوان رپورتاژ
انکرتکست خیلی مهمه! مهمه معنیش این نیست که عین کیورد باشه!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/mohsentavoosiseo/567" target="_blank">📅 11:12 · 28 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-566">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🟢
بهترین جایگزین Dynamic Rendering
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/mohsentavoosiseo/566" target="_blank">📅 17:05 · 27 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-565">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xp9LYeDcpPi11HlosXD-0I3sj-M8yb4ZYpBnLldU-HPnxnjeV0eIcSdmXmUnGNBx8SzlKayLJpcatZDxhQGpy1IkN7oi9cee-Ah9bNLEqmSXfngzPv4oF7m6DEE0pKbTgF0QF3nQlGDQAEaNxkxxhEDMucKp1djAUXiC9wT5lvUsOiuwwskkdkJTDrTfOT9K33ivq10ddZk9FMgS-zkyM3THnthLXbRM0RkdfGPViDt3Te1SD6gVUtUMWHroiFTYSFwKsNnZh3m6nm6khyd4qamgm2aBUdyh_0gHbJWdvumX6aFEpQXIoyRN0nPoMjaFGhWVYuhWzY2sjLWaa1M6wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز خیلی ها فکر می کنن که ادرس سایت مپ حتما باید sitemap.xml
یا sitemap_index.xml
یا post-sitemap.xml
یا... باشه. که سخت در اشتباهند.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/mohsentavoosiseo/565" target="_blank">📅 13:42 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-564">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">mohsentavoosi.com/sitemap.xml
😶
😶
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/mohsentavoosiseo/564" target="_blank">📅 13:32 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-562">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شرایط اقساط ادامه پیدا می کنه اما مبلغ در کل از ۱ آذر افزایش خواهد داشت.  https://mohsentavoosi.com/video/seo-course/</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/mohsentavoosiseo/562" target="_blank">📅 19:09 · 24 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-561">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B01ZzmSZr9PaY5PL-tni7jMN9_7CPj37gnQXlRDo5oyS_awij9Ty4RP5ov_lJAxAzaTytOW6qklwl75QCM38SKpn_w62JZtMCb3w1qH5-8C59-3MqqwKjroMaeDoZy4P_myOhE5SmmFSc_Y2k5gAuIP7lh9c8zo6U1i9rpxnbx-M8NUi8GVZ6uUwbXWRxmIqF7BEzkZqkMwMD6PGGktiHnYJ4iG1jFEFAr8o_ydJDy-XApmLW7yNA6rMP6269BVmkv7QcTBZ8QmooDD6VSKQ1146Opt9o4YKSY8CTKWxqI5851OHaFGV9JPbvjk4rTmBAJsq4PDNQtZ21EQ-kTPODg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش تخمین بازدید و کلیک سایت در آینده
لینک آموزش:
https://youtu.be/G1wyAeQxAnM
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/mohsentavoosiseo/561" target="_blank">📅 16:03 · 24 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-558">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔆
من در اینستاگرام اعلام کرده بودم که تا ۲۵ مرداد و الان تا پایان شهریور، قصد دارم حداکثرم تلاشم رو در این شرایط برزخی کشور انجام بدم که کسانی که قصد صد خرید دوره رو دارند ولی توان پرداخت ندارند، بتونن تهیه کنن.  چه نقدی چه قسطی، شرایط ویژه ای در نظر گرفتم.…</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/mohsentavoosiseo/558" target="_blank">📅 10:19 · 18 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-557">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Am2eYKDaqOgkaFM5E9_x-xFPPFSabhtyV11LWq5-KLqjgaoxCk3yez44d-fjiDhaajcR1SmDNAnyp19qIn_pDUz4mWtESlWz8YfIeWS_MqPOUmYD_8kIOE4SfvreES6YRgNWt6TLja9zuAHot-H1yXCO7BOuMoltZk98L2af5ryM0po6zawg4_x6HBlf0xFg7x1ZE1XwjHBs8Wb58jiXToqT0ocDR2VaXDCgGDpwXaGvwrwQOPOFd6JXXFWHv0Td-5FI2TuRQCtrQN914nswYpFdMo6W8-ijGMzrCaiKVNyJAky67b7mU5__UgsNJSohq0CwkyN4z5v-vFZy-mgmTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدایرکت گروهی در SEO
لینک آموزش:
https://youtu.be/QVNgzWYGTks
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/mohsentavoosiseo/557" target="_blank">📅 18:29 · 17 Aban 1404</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
