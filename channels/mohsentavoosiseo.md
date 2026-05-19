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
<img src="https://cdn4.telesco.pe/file/E5PPmtgOkNu7V94yr71J4Oyiss0Ztuit03i6w4QjxtVF4FI18agLZtSWBhaiqRkfHbkjVjl9n6B5y-a_aLqMe-OIkF71eJ3zh3y7Fzt4Jbc6wMBQ8zS7lssfMcJinCMc-U1jlO-bWyxlVN7OG7Fnv3oSYMoAYSzTs_zQFq7a7ivWdCcfXwbBkiPcTEpvDRUgo8yHSYzdA_0dd5nnO3CsSm1lN5jQRlWUhEL5mgsWgel9NfMcHgYkjIGaQeSCKJyyEh9FFdmfftYC9faBD2z6GenXqZHZd7NGV59Zn2jf_ZtOXfE3MJEcje02C75sD7A_63YeOGGL60FUTJStU_7skQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 آموزش سئو محسن طاوسی</h1>
<p>@mohsentavoosiseo • 👥 7.36K عضو</p>
<a href="https://t.me/mohsentavoosiseo" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا فقط تالیف، مستندات و تجربه هست. اخبار و ترجمه کار من نیست.دوره:https://mohsentavoosi.com/course/seo/یوتیوب:https://www.youtube.com/c/MohsenTavoosiاینستاگرام:Instagram.com/mohsentavoosi.seohttps://www.linkedin.com/in/mohsentavoosi</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 01:23:00</div>
<hr>

<div class="tg-post" id="msg-686">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">احتمالا متوجه شدید که من زدم تو خط نادیده گرفتن. سرمو کردم تو برف فقط دارم فنی حرف میزنم. انگار که همه چی گل و بلبله.
علتش درد زیاده و خستگی. ظرفیتم به پایان رسیده. صدام در نمیاد. من سال ۹۸ گفتم فاز ملی گرایی بر ندارید هی بگید موتورجستجوی ملی. ضررش بیشتر از سودشه. تازه کسانی میگفتند که تو حوزه سئو فعال بودند. پست های لینکدین این موضوع هم لایک میکردند. اون موقع خیلی تنها بودم. تنهایی داد میزدم...
و کلا خیلی حرص و جوش ها. ولی خستم واقعا از دست و پا زدن بیهوده. از خون دل خوردنی که فقط پیرم کرد. از دیدن شرایط و صحنه هایی که جز فرو رفتن تو زمین کاری از دستم بر نمیاد.
اما اینو میدونم نباید همدیگر رو سرزنش کنیم...
به امید روزهای خوب.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/mohsentavoosiseo/686" target="_blank">📅 16:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-685">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIEY1baNmbsSv6ToVTlFOC_NEwSEkZ40Bt8LINQgHQavOFMyQBvIr22Ozrtus8fJe7FRKkqGBqE2Njrw88Gx0uYzYkDiyoco_o5pK_1en7xiqdRtVl_OWSodezOQZAG-DNdp_bAvcJfbyYrhCycEtDnQBoXT3tdC0r88s_CNNn89IyQ7c9Vu4PlCtJCX0gmez6sGfUYWiSfmUBe4QIUs4orY9A07wDAGKFbUEpVlVySfSa2Q8xoK91zSzDf00qeWnY66hZRTxMsQ0Ml5-UHsUECQ-H1Ij1_4RJgKNCEOwhhc3eBJeV1_bfEN4Ey7LVqpH2m4NL523varFoXcoBe_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مرحله ای رسیدیم که هوش مصنوعی، خودجوش، خودش از دیتای خودش ایراد میگیره. خیلی خوبه. تبریک میگم
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/mohsentavoosiseo/685" target="_blank">📅 21:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-684">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4-tzgGRWGzGbTl1ejDXAdV-pCY0zsroOERf4k3Z0C73oYrPuVQha6rMlnaQXx7dghBM4lKPg6DRodeJDBZHeEYcOLen_DgzNv5kEamJ336G9AMRK_bi8AGeu9hZT9d2-VHJ7sos8bpa5wutukIJZwlPewFxCLngzjwoa4Znudh_1Y3-P6XM0tHCynB076yqKZKdPL_p050PqDw90c58wxkgz-_8UN8EoOnllB_5bZP-uAlm2MORsEAggj4tMXO-xHI9LVJIXKrgjb4gs3Pdk4C6PdRPGDFIbffenCfbrDs3-gt99Ye40GCiuGCLM1Q4761D8uvjFof-40RsMyjDlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من یه معتادم! معتاد کلاد!
خودش پیشنهاد داد یکی از قانون هامو که بهش داده بودم تغییر بدم و پیشنهاد خوبی هم داد.
اصلا انگار بشره. توقعمو خیلی برده بالا. خیلی هم ریز بین و دقیقه. خیلی هم عمیق میفهمه.
آنتروپیک پس فردا مثل Horizon Zero Down و Forbidden West، ربات هاش زندگی انسان رو می گیرند و باید پناه ببریم به پناهگاه ها و ربات های Anthropic بشن موجودات اصلی زمین.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/mohsentavoosiseo/684" target="_blank">📅 17:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-683">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔆
به خاطر شرایط جنگی، قیمت دوره از 12 میلیون تومن، به 4 میلیون تومن، کاهش پیدا کرد و این قیمت تا زمان ظهور دوباره امید به بهبود در دل مردم این سرزمین، این قیمت باقی می مونه.
❗️
هیچ وقت هیچ کمپین تخفیف و فروشی نداشتم. این هم کمپین نیست! کاهش دائمی هست تا برگشت…</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/mohsentavoosiseo/683" target="_blank">📅 15:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-682">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/mohsentavoosiseo/680" target="_blank">📅 18:48 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-679">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQtBSe_Kz082VQV6BpiXimg0sEyON9UmTuNnFsKrbM8qv0gpk1JDZgqEFTLzy_lxlaWkD44vMcwH_wrriRYExy4IDtxC9n7Co5layKUS3jq3BXGyI-JOFhOd986fyWG1pK-AemUac0_Ef0X1z39WYmv3GWMmB047CfyKgatxzuIZmhEJeKO22HfMiZFyojydzTng5QaEHB68rgf4vaupWpiCIBTLgas6xvDRq5AmE87ahsrawR9CaIRfKd9QuZWZrxR1eAnYbr7uWyeF4ma-MTVUwa4dK0i6jM-MRJHybdPFggzmoPFKHrIj5qf9yBskDKqmQc5M6vlZ9P6CypqDhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعا خوشم نمیاد از این خسیس بازی بیش از حد کلاد. دوتا لینک کرد و خوند، یه دونه گوگل شیت دویست ردیفته و ده ستونه ساخت کلاد مکس(5x pro) شد 22 درصد!
البته با Sonnet کمتر مصرف میکرد قطعا. ولی حوصله خنگ بازیش رو نداشتم چون کار گوگل شیتش پیچیده بود. آدم هم مغزش از جا درمیومد با این تسک.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/mohsentavoosiseo/679" target="_blank">📅 14:32 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-678">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">صحبت تلفط شد، خیلی ها خارج رو شامل چند تا دونه کشور خاص میدونن و ملاک ذهنیشون اینه: ایران و امریکا. ایران و کانادا. ایران و آلمان.
هرکس که مهاجرت کرده، ایران و کشوری که رفته رو راس میدونه تو ذهنش.
ولی بهتره ما جهانی فکر کنیم و کل کره زمین رو ببینیم. جهت خط خطی کردن ذهن هایی که ناخواسته محدود شدند، یاداور میشم:
خارج شامل هند، بنگلادش، نپال، سومالی، کنگو، هنگ کنگ، فیلیپین، میانمار، تانزانیا، گامبیا، بوسنی هرزگوین، مغولستان، لیتوانی، لیبی، مصر، غزه و رام الله و کرانه باختری، صربستان، مراکش، قرقیزستان، زامبیا، شیلی، بولیوی، گواتمالا و... هم هست و این ها هم خارج محسوب میشن و جمع کوچکی از سرزمین ها و کشور های غیر انگلیسی زبان هستند!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/mohsentavoosiseo/678" target="_blank">📅 11:42 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-677">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تلفظ Claude به انگلیسی با لهجه بریتانیایی و آمریکایی، کلاد هست. آ کوتاه. کلود نیست. حالا شاید با انگلیسی غیر اصیل مثل هندی و سنگاپوری و اماراتی یه جور دیگه بگن.
تلفظ Claude در بعضی زبان های اروپایی و اسپانیایی و کره ای میشه کلودی.
کشور های مختلف هم به مدل خودشون تلفظ میکنن.
تلفط Claude به فرانسوی میشه کلود. با صدای O. صدای اُ . بعد از d هم e گفته نمیشه. کلوده نیست. کلود. ریشه کلمه claude، فرانسوی هست. در نتیجه کلود هم درست هست.
مثل BMW که متولد آلمانه و آلمانی ها میگن بی ام وی. و آمریکایی ها میگن بی ام دبلیو. عملا اصلش بی ام و هست(نه دبلیو). پورشه هم درست تر و آلمانی تره. پورش رو انگلیسی ها میگن.
اما کلاد، فقط واژه اش ریشه فرانسوی داره. ولی شرکت Anthropic، که سازنده کلاد هست، یک شرکت آمریکاییه.
خلاصه: هم کلاد درسته هم کلود. آ و اُ . کوتاه.
نظر شخصی: برای اینکه با فضای ابری قاطی نکنیم، کلاد بهتره. چه برای مخاطب انگلیسی چه فارسی. تلفظ رسمی انگلیسیش هم کلاد هست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/mohsentavoosiseo/677" target="_blank">📅 11:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-676">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZdSJrhaFSIQObJDI66nYm7Kiz8fa3lcw2fYxTsH0wUsGsbd38ZD4WuHkhZoz0NsSc8gtvCOoEWJ0Q6ex20JWI_0Oyy5Ts0-744xkoZPV6fqbxfkm1MmPoMPLfC-cqrTi0PZ15agH_mHeYV0jRXu6g1itFVKLODO6x6OOPmJy1ng70-ipTgV3NjG293VmWHPZ-ke8EIz98dJtyWn5kuQBfVnCmLrPHVh--7OHJi53xoVAOiHwP48X5pSeP21r-D1KGKi6UFmP0G3GO9Wsje1Tquu0QuIULMcVwFMQFr_p-xFtjLy1Pi_Vh6vRPXk5VcZ2D4pRYY2HU9RGY8BoSz0mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این همه خوبی از کلاد گفتم از بدیشم بگم. مثل chrome که اندازه اسب، رم می خوره، این هم خیلی مصرفش بالاست و گرونه.
کافیه یه کم تسکت متنی نباشه، نسخه Opus بسیار بسیار مصرف می کنه و البته بسیار هم باهوش تر از Sonnet هست.
این سشن ساعتی بشه 70 درصد برای کلاد مکس(5x pro) که ماهی 100 دلار پولشه واقعا زیاد هست.
کلاد پرو برای من اغلب کم میومد. کلاد مکس 5X اغلب زیاد میاد.
یک سری نکته برای بهینه سازی مصرفش از نظر زمانی هم تو
این ویس
گفتم.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/mohsentavoosiseo/676" target="_blank">📅 16:16 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-675">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حالا من یه جوری از کلاد تعریف می کنم انگار اکانت کلاد میفروشم(اتفاقا پیام زیاد میاد برای خریدش).
درحالی که برعکس اکانت ChatGPT ارائه میدیم. چیزی که همش تو سرش میزنم
😅
ولی بهرحال اونم کاربرد خودش رو داره. من خود اکانت چت جی پی تی پلاس دارم اختصاصی رو اکانت خودم.
اکانت Cluade Max هم دارم که 5 برابر Claude Pro هست محدودیت هاش. ولی همه اعضای تیم ازش استفاده می کنیم.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/mohsentavoosiseo/675" target="_blank">📅 15:51 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-674">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/mohsentavoosiseo/674" target="_blank">📅 15:48 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-673">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/mohsentavoosiseo/673" target="_blank">📅 15:36 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-660">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">هزینه اینترنت ثابت فیبرنوری تو ترکیه 1100 لیر هست با سرعت اسمی 1Gb در ثانیه و سرعت واقعی 600Mb در ثانیه که دیگه Wifi 5G هم جواب نمیده این سرعت رو. و با کابل باید ازش گرفت که افت نکنه.
میشه ۷۰ مگابایت دانلود، ۴۰ مگابایت اپلود. در ثانیه. (هر ۸ بیت، ۱ بایت هست).
با وای فای 5G تا 300Mb میشه اگه نزدیک مودم باشید. با وای فای 2.4G تا حداکثر 100Mb.
یعنی با دلار ۱۸۷ هزار تومن میشه ۴ میلیون و ۵۰۰ هزار تومن.
بدون محدودیت حجم.
تو کافه ها بدبینانه(استارباکس، اسپرسولب) حدود 30 تا 70 Mb در ثانیه هست(حدود ۳ تا ۸ مگابایت در ثانیه). بدون محدودیت حجم.
هزینه کافه: رایگان. یک بار خرید که پسورد بگیرید فقط. بعدا تو هر شعبه ای استفاده کنید بدون سفارش. بدون خجالت. بدون احساس وظیفه برای سفارش دادن.
اینو گفتم که بگم انقدر ما تخریب کردیم بقیه کشورا رو حالا اینه وضعمون.
به خودمون گفتیم متمدن و باهوش و به بقیه گفتیم وحشی و عقب مونده و کم هوش و خنگ...انقدر که گفتیم هه هه ارمنستانم ادم شد واس ما؟ ترکیه که فلان. یونان که فلان. بابا ایتالیایی که خودشون دارن فرار میکنن. دلار دیگه به درد نمیخوره. دلار مرد. امارات بیابون بود برای ما ادم شدن. عمان؟ اون بیابون که هیچی نداره بابا. گرجستان شاخ شده بلیت برگشت میخواد از ایرانیا! ژاپنی ها که تا قبل بمب اتم وحشی بودن! چینی های حشره خور! عرب های سوسمار خور! اصلا همه جا ایران بوده. همش مال ما بوده.
عاشق توهم و چیز غیر نقدیم! هیچ کاری یا واقعیت موجود نداریم!
حله. فعلا کانفیگمونو بخریم
😏
...
ایران چراغ قرمز مخصوص عابر پیاده نداره. یه دونه به من نشون بده! یکی فقط!
چراغی که فقط برای عابر باشه ها! نه اینکه یه گروه ماشین چراغشون قرمز و گروه مقابل سبز بشه. چراغ مخصوص فقط عابر.
چون از نظر مهندسی عالی و از نظر کرامت انسانی بی نظیریم.
فرض کنیم موتوری هام تو چراغ قرمز رد نمیشن! (فرض محال کن).
ایران از این نظر، هم رده افعانستان و پاکستان و بنگلادش و ویتنام و هند و بخش هایی از عراق و کشورهای شمال آفریقاست.
تعصب یعنی نپدیزیم. خرد و عقل یعنی بپذیریم واقعیت رو که بتونیم تغییرش بدیم.
پی نوشت(بدیهی برای اکثر شما)؛
Mb یعنی مگابیت
MB یعنی مگابایت
واحد سرعت، بیت هست. چیزی که ما بهش عادت داریم و تو دانلود منیجر می بینیم، بایت هست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/mohsentavoosiseo/660" target="_blank">📅 17:41 · 13 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/mohsentavoosiseo/659" target="_blank">📅 11:19 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-658">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">به زودی در شغل های در سراسر جهان و ایران:
استخدام متخصص فلان (گرافیست، مارکتر، تولید محتوا، توسعه دهنده و...)
ملزومات مهم (نه امتیاز!):
تسلط به کلاد
رسیدیم به این جمله که در آینده افراد شغل هاشونو از دست نمیدن. بلکه کسانی که بلد نیستند با AI کار کنند شغل هاشونو از دست میدن. (فعلا غیر از کارهای دستی مثل آشپزی و ماساژ و خیاطی و...)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/mohsentavoosiseo/658" target="_blank">📅 00:48 · 08 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/mohsentavoosiseo/657" target="_blank">📅 00:39 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-655">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نکته های تجاری ارتباطی مصاحبه ۴
چیزی که بار سنگینی از دوش من برداشت
رها کردن چیزهایی که میخواستم حفظشون کنم
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/mohsentavoosiseo/655" target="_blank">📅 17:20 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-654">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نکته های تجاری ارتباطی مصاحبه ۳
مصاحبه بین المللی
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/mohsentavoosiseo/654" target="_blank">📅 17:13 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نکته های تجاری ارتباطی مصاحبه ۲
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/mohsentavoosiseo/653" target="_blank">📅 17:09 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/mohsentavoosiseo/652" target="_blank">📅 17:05 · 07 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/mohsentavoosiseo/651" target="_blank">📅 14:02 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-650">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کاهش مصرف Session پنج ساعته و هفتگی کلاد.
مصرف دوبرابر کلاد در ساعت های Peek
چرا اشتراکی خیلی معنی نداره برای کلاد؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/mohsentavoosiseo/650" target="_blank">📅 21:32 · 06 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/mohsentavoosiseo/649" target="_blank">📅 21:32 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-648">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🏴
در جریان باشید
🏴
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/mohsentavoosiseo/648" target="_blank">📅 21:32 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-646">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/mohsentavoosiseo/646" target="_blank">📅 15:25 · 05 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-644">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOkMQUITQno2agxEI9VG3qasTj3Rw7Or-U3cVART8Xk3ZjVvWQTQv4WXuTb-o2hAcYa4IlbGIxS4FSWYJDHbCOp9w-vjXVN0FZnxXfBsFyLmICxuEaJaQrcEqWTeOURcSPeL3cEe6GA6275dS1UFbYRYn2h41zbA5TSA7aUIX8VzmhVqymgpt-f2n_zDVpcb63vAIJCOhNZSvABtCMyc1lMqP3WWxj6YXEDJU8goIUuKPphHFnJpXKFIJO91qQObjVUz3Klv50ccEVCn9mGZQr1kFHTHqBiLwIHSHhrpKHL4QVE61lZzx4FEWx4MNy1U0B2NEW--b2TY29y3FgeJQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/mohsentavoosiseo/644" target="_blank">📅 13:22 · 05 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-643">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">از اینترنت طبقاتی استرس نگیرید.
🔴
آبان ۹۸ بحث اینترنت ملی داغ بود و موتورجستجوی ملی. دو هفته هم قطع کامل بود.  خیلی ها ترسیدن و رها کردن. زمان مهسا هم همینطور.
🔴
الان که در وسط شرایط جنگ و برزخ رو به بدتر شدن هستیم، اینترنت وصله. وسط جنگ ۱۲ روزه حتی گوگل باز…</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/mohsentavoosiseo/643" target="_blank">📅 22:43 · 04 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-642">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">هوای هم رو داشته باشیم
✅️
چه قبلا قسط دادید چه قبلا اصلا پرداختی نداشتید، سعی می کنیم با شرایط فعلی شما در این شرایط ایران، بتونید تهیه کنید: @mohsentavoosisupport
✅
کسانی که قسط دوره داده بودند و مهلت تعیین کرده بودیم و قرار بود قیمتشون افزایش داشته باشه،…</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/mohsentavoosiseo/642" target="_blank">📅 17:47 · 04 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-639">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">احتمال سوم:
قطع موندن اینترنت بین الملل و وصل شدن بعضی جاها بصورت لیست سفید و استثنا</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/mohsentavoosiseo/639" target="_blank">📅 15:29 · 31 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-637">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee89341378.mp4?token=Gsg1N4B9qAWZP9qIfTi8BAYMyXQL0FGvsOFLrvsdgx3FVybGysVmho59GH51LIcK7DOpVyiqCgDhv1ZaEj4IuE1qAUPQ1o3APdnMs3cKk2basNu1H5gxviQSBVlZb-Wmngsv5ZTOz7ZbL_Fp9XRSO3aLY-b9S0agwLp-yAZ-T34INWBxsJJXxtBYh2Z2Dt6iQq7LnecDO_VrdIsg-aHQBB7IhJ1Ch1P_4KopZqwgsceu3hQHDqcqNQyNg5z43MfPNVgoxXF9ZNqj2Pr6xmvKeM5XGvUN8DvRa7b49yDfXyMzPm3YdE5D8Ek4g56sbZGE6KD3iushjtqoMQ5cBmDx8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee89341378.mp4?token=Gsg1N4B9qAWZP9qIfTi8BAYMyXQL0FGvsOFLrvsdgx3FVybGysVmho59GH51LIcK7DOpVyiqCgDhv1ZaEj4IuE1qAUPQ1o3APdnMs3cKk2basNu1H5gxviQSBVlZb-Wmngsv5ZTOz7ZbL_Fp9XRSO3aLY-b9S0agwLp-yAZ-T34INWBxsJJXxtBYh2Z2Dt6iQq7LnecDO_VrdIsg-aHQBB7IhJ1Ch1P_4KopZqwgsceu3hQHDqcqNQyNg5z43MfPNVgoxXF9ZNqj2Pr6xmvKeM5XGvUN8DvRa7b49yDfXyMzPm3YdE5D8Ek4g56sbZGE6KD3iushjtqoMQ5cBmDx8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/mohsentavoosiseo/637" target="_blank">📅 22:07 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-636">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دوستانی که نگران قطع موندن اینترنت هستند، این نظر شخصی من بدون قبول مسئولیت هست و من برنامه هام بر این اساس پیش میره همونطور که قبلا هم گفته بودم:  احتمال اول: وصل شدن دائمی اینترنت بین الملل بهتر از قبل یک بار برای همیشه بدون ترس مجدد از قطعی.   احتمال دوم:…</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/mohsentavoosiseo/636" target="_blank">📅 20:49 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-635">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">قبل از اینکه حرف اصلی رو بزنم این رو بگم که دوره از داخل ایران در دسترس هست.
✅
اما در این شرایط چیکار کنیم و خودم چیکار میکنم؟
✅
برای کسانی که ایران هستند: تولید محتوای فارسی و کمپین های رپورتاژ و محتوای داخلی وب سایت و استخراج عنوان ها با ابزار های داخلی…</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/mohsentavoosiseo/635" target="_blank">📅 19:50 · 26 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-634">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خیلی ها نمیدونن میرور چیه کلون چیه.</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/mohsentavoosiseo/634" target="_blank">📅 14:39 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-633">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سایت من از داخل و از خارج در دسترس شد و چه مراحلی طی کردم؟
mohsentavoosi.com</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/mohsentavoosiseo/633" target="_blank">📅 14:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-631">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">روش راحت بالا اومدن سایت از داخل و خارج! بدون پیچوندن بدون GEO DNS!
امیدوارم هیچ وقت به چنین چیزی دیگه نیاز پیدا نکنیم.
آرزو میکنم به محض اینکه اینکارو کردید پشیمون شید بخاطر وصل شدن ابدی اینترنت بین الملل. آرزو میکنم زحمتتون هدر بره! می ارزه!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/mohsentavoosiseo/631" target="_blank">📅 14:21 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-630">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فاز امید الکی دادن ندارم. صحبت من فنی هست. انتخاب های متعددی پیش رو داریم. ولی من همیشه دست و پا زدن و یه کاری کردن رو ترجیح میدم به هیچ کاری نکردن. هیچ کاری نکردن و تماشاچی بودن و منتظر بودن من رو از پا میندازه. ته چاه باشم ترجیح میدم دیوار چاه رو بکنم تا بشینم منتظر باشم بالا رو نگاه کنم.
دست و پا برای بقا همیشه مثل فیلم Pianist  نیست. یکیشم مثل وضعیت الان ماست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/mohsentavoosiseo/630" target="_blank">📅 11:36 · 22 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-629">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✅
اما در این شرایط چیکار کنیم و خودم چیکار میکنم؟
✅
برای کسانی که ایران هستند:
تولید محتوای فارسی و کمپین های رپورتاژ و محتوای داخلی وب سایت و استخراج عنوان ها با ابزار های داخلی کاریه که میشه انجام داد و شما رو جلو میندازه. ماه های بعدی دیگه این مراحل رو تکرار نکنید. برای سه ماه بعد اصلا جلو جلو انجام بدید.
اگر هم سرور داخل هست، بهینه سازی داخلی هم میتونید انجام بدید.
✅
برای کسانی که خارج از ایران هستند:
دوباره باز تولید محتوای داخلی، استراتژی و عناوین محتوای داخلی و آف پیج! به کلی ابزار هم که راحت دسترسی دارید! بهتر نیست از رقبایی که فقط درگیر خوندن اخبار هستند جلو بیفتید؟</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/mohsentavoosiseo/629" target="_blank">📅 11:36 · 22 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-628">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">برای پارس پک origin rule هست روی سرویس CDN. و GEO DNS نیست! به گفته خودشون دقت origin rule بسیار بالاتره و ارزون تر هم هست کلا:
https://parspack.com/cdn</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/mohsentavoosiseo/628" target="_blank">📅 18:18 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-627">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">درباره یک سری ابزار های جستجوی داخلی از اونجا که دوست ندارم این وضعیت رو دائمی ببینم و عادت بشه و تبلیغ کنم، اسم نمیبرم.
ولی اون ها ترکیبی از گوگل و بینگ هستند به علاوه یک سری شخصی سازی ها و اسلامیزه شده.
شرط اول اینه که هم از داخل هم از خارج بالا بیاد سایتتون که تو پست های قبلی توضیح دادم.
چون اینا خودشون از بینگ و گوگل دیتا میگیرن، گوگل سایت شما رو نبینه اینا هم نمیبینن.
اگرم گوگل ببینه و کاربر داخل باز نکنه سایتتون باز نمیشه و بازم فایده نداره.
بقیش همون سئویی هست که بلدید ولی یک کم سنتی تر. مثلا اگزکت مچ بک لینک با عین کیورد مهم تر هست برای بینگ. و بینگ هنوز به متاکیوردز کار داره.
آموزش سئو بینگ و چت جی پی تی ChatGPT
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/mohsentavoosiseo/627" target="_blank">📅 17:15 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-626">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پست های بالا ویرایش شد. دوباره ببینید. تو اپ های داخلی هم برای کسانی که اینترنت ندارند بفرستید شاید مفید باشه براشون.</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/mohsentavoosiseo/626" target="_blank">📅 17:09 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-625">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">این متن هم محمدرضا زراعتی از بچه های پارس پک و دوست شفیقم برام فرستاد. با شما به اشتراک میذارم. درباره SSL هاست های داخل:
راستی محسن جان الان سایتهایی که داخل ایرانن به خاطر همین قطعی ها مشکل خطای ssl میگیرن چون احراز هویت دامنه پیش‌فرض از روش HTTP هندل میشه برای همین ریکوئست های از صادر کننده سرتیفیکیت نمیرسه به ایران
راهش اینه که اعتبارسنجی ssl رو از روش DNS انجام بدن دیگه مشکل حل میشه.
تو این اموزش یاد دادم چطوری با CDN پارس پک بتونن هندل کنن(برای ssl بر خلاف ارجین رول نیاز نیست دیگه ابر cdn روشن بشه فقط از رکوردهاش استفاده میکنن)
https://docs.parspack.com/ssl/free-ssl-issue-iran-access/
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/mohsentavoosiseo/625" target="_blank">📅 17:00 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-624">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سایت من از داخل و از خارج در دسترس شد و چه مراحلی طی کردم؟  mohsentavoosi.com
1️⃣
اول انتقال بکاپ. که بسیار سخت بود. انتقال بکاپ 10 گیگی از خارج به داخل سخت بود از نظر قطع شدن و سرعت(الان راحت تره خیلی).
2️⃣
دوم خرید هاست در دوطرف. هاست من از قبل آلمان بود.…</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/mohsentavoosiseo/624" target="_blank">📅 16:57 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-623">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/mohsentavoosiseo/623" target="_blank">📅 16:51 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-622">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">از عادی سازی نکردن دی، رسیدیم به اینکه چطوری درامدمون رو در حد بقا حفظ کنیم تا به شرایط عادی یک بار برای همیشه برسیم...
ادامه موارد زیر جهت کمک هست. دست و دلم به پست و تولید محتوا نمیره. ولی میدونم با همین چند تا پست ممکنه کار چند نفر راه بیفته.</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/mohsentavoosiseo/622" target="_blank">📅 16:47 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-620">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رسید مژده که ایّام غم نخواهد ماند
🔆
شماره در زمان اینترنت ملی در پیام رسان "بله" (متاسفانه):  جهت موارد دسترسی به دوره، خرید، قسط و...: 0919-268-19-56  سایت mohsentavoosi.com از داخل و خارج حالا باز میشه(اپدیت فروردین ۴۰۵)
🔆
🔆
🔆
رسید مژده که ایّام غم نخواهد…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/mohsentavoosiseo/620" target="_blank">📅 19:27 · 08 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-619">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بیشتر از آمادگی بابت قطعی های مقطعی اینترنت ایران و دسترسی از خارج،  در فکر آمادگی برای تغییر قوانینی هستم که در سود و زیان وب سایت ها موثره و بازی رو عوض میکنه. آیا خدمات و محصولات شما بعد از تغییرات بزرگ همچنان تقاضا یا سود داره‌؟  بر خلاف تصور عموم، به…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/mohsentavoosiseo/619" target="_blank">📅 17:27 · 18 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-616">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بیشتر از آمادگی بابت قطعی های مقطعی اینترنت ایران و دسترسی از خارج،
در فکر آمادگی برای تغییر قوانینی هستم که در سود و زیان وب سایت ها موثره و بازی رو عوض میکنه. آیا خدمات و محصولات شما بعد از تغییرات بزرگ همچنان تقاضا یا سود داره‌؟
بر خلاف تصور عموم، به عقیده من کسب و کار های مهاجرتی، همچنان پررونق تر و راحت تر پیش خواهد رفت.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/mohsentavoosiseo/616" target="_blank">📅 19:33 · 03 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-613">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ما نهایت همکاری رو داریم می کنیم همه جوره که دسترسی همه با مبلغ کم راه بیفته تو اسپات پلیر</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/mohsentavoosiseo/611" target="_blank">📅 16:03 · 12 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-610">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">این پیام رو به کسانی که اینترنت ندارند هم برسونید: الان که شرایط جنگیه و نمیدونیم یک هفته دوهفته ادامه داره یا یکی دوماه تا وصل شدن اینترنت، اگر قسطی دسترسی به دوره داشتید، با مبلغ خیلی کمتر میتونید دسترسی رو کامل کنید یا اگر ندارید جدید بخرید. هم به خاطر…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/mohsentavoosiseo/610" target="_blank">📅 17:18 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-609">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">این پیام رو به کسانی که اینترنت ندارند هم برسونید: الان که شرایط جنگیه و نمیدونیم یک هفته دوهفته ادامه داره یا یکی دوماه تا وصل شدن اینترنت، اگر قسطی دسترسی به دوره داشتید، با مبلغ خیلی کمتر میتونید دسترسی رو کامل کنید یا اگر ندارید جدید بخرید. هم به خاطر…</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/mohsentavoosiseo/609" target="_blank">📅 22:26 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-608">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اگر سرورتون داخل ایران هست، الان از ایندکس خارج شده صفحاتش.  اگر سرورتون خارج از ایران هست، مشکل گوگلی و ایندکسی نداره ولی کاربر داخل ایران بهش دسترسی نداره.  راه حل؟ هیچ راه حلی نداره. راه حل اینه که کلا اینترنت بین المللی قطع نشه. اگر هاست داخل و سی دی ان…</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/mohsentavoosiseo/608" target="_blank">📅 19:19 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-607">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/mohsentavoosiseo/607" target="_blank">📅 20:45 · 30 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-606">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🟢
ساده لوحی در SEO
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/mohsentavoosiseo/606" target="_blank">📅 21:24 · 06 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-605">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔍
این به روزرسانی سومین تغییر هسته ای گسترده در سال 2025 است و مانند نسخه های قبلی، هدف آن ارتقای کیفیت و ارتباط محتوا برای کاربران در سراسر جهان است.
🔍
این به روزرسانی صرفا روی یک بخش خاص تمرکز نمیکند؛ با بازتعریف معیارهای رتبه بندی، توانایی گوگل در ارزیابی محتواهای مرتبط، مفید و رضایت بخش را افزایش میدهد.
🔍
گوگل بار دیگر نشان میدهد که ارزش واقعی در محتواهای با کیفیت و تخصصی است، به ویژه در زمینه هایی مثل پزشکی و سلامت که E-E-A-T (تجربه، تخصص، اقتدار و اعتبار) نقشی حیاتی در رتبه بندی دارند.</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/mohsentavoosiseo/605" target="_blank">📅 16:49 · 04 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-604">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/mohsentavoosiseo/604" target="_blank">📅 11:48 · 04 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-603">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKOwBGLskEKYB7mbAM52a-Fmo43VJlSIli3GF0OA-R2FUfxMVXXfGuoPECSt4gXjd_qdn6DvK1ICDK2h-tizFCZ5vyUmGEWSGJxlXt74-tGVfbZIpXNfAWxJ3UmcWKNdgPHvfysB2E2lnM1evlBNSDke6VlFxdbnqOClJFdSV2QZd_ngWawFytE75VK7vLsYaQy7_TnIL1CR3TShu8Y8NIA7rdQMl3s_kqx42GeoQXJ3-qHTuQvIWcfREaj0XPpvCG-wFYhEKmz80l8bfNY6n9dFTGxSwYCvTKxIQJCmzj5ojRv6ogxbFONGO8nrVdWiqAhF-LVJQUJMmd2NNn2f6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/mohsentavoosiseo/603" target="_blank">📅 17:38 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-602">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRuCwzqGu0VMVPsq-Xp4dwxaSydH5BBZhXEeK0TQYdED3h2DUFSJLxn7AJ8y5CQJiEsjnchkV_18xEG8UHrakIur0FD-1xxckHqiRgWzfs_Y2gkh6WtgJVfkxrA4BVl6OeOqn9XrxVfNuvklGkfYjoaoXYosiN_msoWjl9UpoGQL-eomc8dhVaBJ9g7vLdp14Ywa7FVCfgYvFPQlXQvRIKKYQyJQ7rIufKRnIPzZWQ9uNFv71Y1GZrzT3NoX8xhK6Q_Agkg4wrpgN4xlD3L8MyYwDIdJjdm4-G6bp7iiSetdMdeIvM1RNSkNizy8Vk-qzhS5reUBntd8x3BCmeQYCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
تو ویس های بالا توضیح دادم
✅
اینم سایت های من که تو اپدیت ها تکون نمیخوره. همیشه همینه. آخرین چیزی که من بهش توجه می کنم آپدیت های گوگله! چون مسیر من ثابته همیشه. به صورت کلی در دراز مدت رو به رشد بر اثر فعالیت های من و با توجه به رقابت موجود.
📎
اسکرین شات سرچ کنسول. شماره 2
💵
درامد این سایت: بالای معادل 200 م.ت. به صورت دلاری. غیر فارسی. مال من نیست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/mohsentavoosiseo/602" target="_blank">📅 17:38 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-601">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIsoIT3mXd3dRX-KKbuSlmIHE-O4C6HogQ5W_12BQOgRXwtC7fTjfZwk7ZMNoxy1NOQmusCmp-vHjkFc3f9Zp5JzSnwdD6GAZesQH4tPe_DKXpqsPw7PtTtzw6vif92VofCAXbZJzgQq_wC5ZSU__4khRUPtamHywPfwyhug6rOn9ItxuDCjwjGYn7MIIiy9icRgrrH_79u5iccV9fsjB2ZIcZU3nGiVUiz4a7rupRLeeiTyDGus478wEkRqSIw1Be66TNUs_RbUWVGM6i2wV2nudpp7E1_aJhKP3drGMI9QZQS46dkmUjrg8i5GKO5osyYxvEP2Q3Enh07r-djHqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کلا این صورت مساله که وای الان چیکار کنم گوگل آپدیت کرد، از دیرباز صورت مساله غلطی بود، صورت مساله غلطی هست و صورت مساله غلطی خواهد بود.
تمام پست های انگلیسی سایت های دیگه خیلی از زبان های دیگه هم از اون ها کپی و ترجمه میکنن و درباره راه کارهای افت بعد از اپدیت هست، کلیشه چرت و پرتی بیش نیست!
مثلا میگن تکنیکالتو چک کن! بک لینک های غیر طبیعیتو حذف کن! عنوان ها تو بازبینی کن!
ولی این محتوای بلغور چرت متقاضی داره بهرحال. ترافیک میاره برای اون سایت ها. می طلبه که بنویسن. چهار نفر هم بیان بگن ممنون از پست مفیدتون! اما نفهمن خب آخرش چیکار باید کنن! فقط ذهنشون مبهم تر میشه.
https://www.linkedin.com/posts/mohsentavoosi_aebaeoaew-activity-7409525124615348224-5vg8
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/mohsentavoosiseo/600" target="_blank">📅 13:19 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-599">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تو آپدیت گوگل چیکار کنیم؟
قسمت دوم
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/mohsentavoosiseo/599" target="_blank">📅 12:44 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-598">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تو آپدیت گوگل چیکار کنیم؟ چرا افت کردیم؟ راه حل چیه؟ کجا رو بخونیم بفهمیم چه تغییری بدیم؟
قسمت اول
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/mohsentavoosiseo/598" target="_blank">📅 12:44 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-597">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">معلم زبان عالی ولی غیر تجاری!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/mohsentavoosiseo/597" target="_blank">📅 12:34 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-596">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/mohsentavoosiseo/596" target="_blank">📅 19:15 · 02 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-595">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🟢
حرفه ای بودن به سابقه زیاد نیست
تفاوت SEO specialist با senior seo و junior seo چیه
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/mohsentavoosiseo/595" target="_blank">📅 18:08 · 30 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-594">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تو ابزارهای اشتراکی، قطعی ها و ایراد ها و اینکه یهو میگه تو حداکثر ظرفیتو استفاده کردی(با اینکه نکردی)؛ رو بپذیرید!
طبیعیه. همون لحظه رسیدن به محدودیت اکانت، نمییتونن درجا شارژ کنن. دستی انجام میشه.
پول کم میدیم که استفاده کنیم فرقش همین چیزاست. قطعی، یه روز یهو از کار افتادن تو زمان مهم، غیر فعال بودن فیچرای دیگه همون ابزار و...
بدون مشکلش رو میخوایم باید پول دلاری کاملش رو با مسترکارت مجازی یا واسطه بدیم و بخریم با ده ها برابر قیمت اونم به ازای تک تکشون.
ما اشتراک ماهانه SAAS, software as a service رو نمیدیم و بجاش با نیم میلیون تومن ماهانه ده تا SAAS رو همزمان میگیریم. نمیشه انتظار بیشتری داشت.
لیمیت پس (کد تخفیف mohsentavoosi)
نوین ترند
فعلا اصلی ها هستن. هر جای دیگه ای ارائه بده تفاوت زیادی نمی تونه ایجاد کنه. مگر تو ظاهر مثل یو آی یو ایکس و راحتی نصب و دسترسی.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/mohsentavoosiseo/594" target="_blank">📅 21:00 · 29 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-593">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/mohsentavoosiseo/593" target="_blank">📅 23:16 · 24 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-592">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🟢
تعداد ریکوئست مهم نیست
کاهش تعداد Request در سایت اختصاصی و وردپرس
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/mohsentavoosiseo/592" target="_blank">📅 15:29 · 24 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-591">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaYyOlxpJPYmaYXAo-ESDyReStAMCkVlCj0Olx2EH4eF6Dbhtjlm80BevGEGP9VBlSpvlW-1_MK5RymL8mNnBV0vH0XDHv2VooTQZ-iyfQ9Y60PqvKM62VcWo2CfJ8i7ZOcRRUaBX0d5i6yAZ1vL9D4VbZ6ZJymSSuHWK1joCLJZ6-zbK-x_V9e6HAyYwpcZo34goiULGBWO9g1bAPEbjMF8WrF5M9Zlgy_FhwvIk83vyXQxJ9v4GF5rwiUUa7a0cQLYW6v6muKeaDJUMO-aAb0WTjThmUaXN8Vgg-ygdOHc21hTDkYqGdUpU9uhKxruV0PCHJHb1js9fonCuGpiKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://eseminar.tv/webinar/%D8%B1%D9%88%DB%8C%D8%AF%D8%A7%D8%AF-%D8%AD%D8%B6%D9%88%D8%B1%DB%8C-%D8%B3%D8%A6%D9%88%D9%84%D8%A7%D8%A8%D8%B1%D8%A7%D8%AA%D9%88%D8%B1%DB%8C-%DB%B4
در این رویداد حضوری، قراره من و جمعی از دوستان در پنل درباره بحث قیمت و بازدهی رپورتاژ ها در سئو از نظر فنی و تجاری صحبت کنیم.
من برگزار کننده نیستم و صرفا یکی از اعضای پنل هستم.</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/mohsentavoosiseo/591" target="_blank">📅 20:59 · 23 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-590">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🟢
Disavow & Ahrefs
دیسوو گوگل هیچ ربطی به سایر ابزار ها نداره
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/mohsentavoosiseo/590" target="_blank">📅 17:11 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-589">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اشتباه ها و تفکر اشتباه رایج پروژه گرفتن در این زمانه
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/mohsentavoosiseo/589" target="_blank">📅 12:05 · 18 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-587">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3aS-qb_DxlGXyaYJlmGL12DQLuCQHqIwYCkuEO9esH7vlG3ZUf0m7lW3WV1rdWrs26n8mItC8uIUkvgUTE5Z-eg57ObodeFLE9Gg6fwfSYKXnvnPuExjQ6HoBCDxw_AEnO-aXNbcw0-yHaRGISCB_4oHGTIO_OlPjSf3VGkysyb4yqiKz2m4c55CeFETcbUUHA8UPLdPJijYcEKkkU9xvEccl1iNKqgPNjnUAsPhnd7llx5xSOP0uev2qvhlj5vMWLLZ9c5ILxgGZkptnHKb85QFojgCi0bjHY_8af9GxfqS4HG4u_Hf-IKM2MHgiQQNoVSE7vbu9jc3yJbecl4Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ۷۸٪ تخفیف خرید رپورتاژ (انواع بک لینک)
تا ۳۵٪ تخفیف سفارش محتوا
از ۹ تا ۲۲ آذر
لینک مشاهده جشنواره
.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/mohsentavoosiseo/587" target="_blank">📅 13:38 · 12 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-585">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🟢
اسکرول نامحدود یا کلید مشاهده بیشتر؟
این ویدیو دارای یکی از نکته های مهم سئو تکنیکال هست
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/mohsentavoosiseo/585" target="_blank">📅 19:34 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-584">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🟢
مالیات سایت
با باید ترسید و فاصله گرفت یا باید رفت تو دلش!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/mohsentavoosiseo/584" target="_blank">📅 17:42 · 10 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-582">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZCHMWsrXZDYNIOkAmwAR5_D_Wn80LJl8FBBgV7MF22z5Cglr79Ejvfjiks8QOYrrIPld426gKi_BAuR2MtRguC-NeQFiTrvs9LqysDO92VUcwtxiNdxUtkfskV3Lzb0_OiNUa2PUPCBNQ2JPedW54NX-wFf2BTcW3qPoC9uMWyMbEfCan0P2wXd-hiOXE_9vTRYKxwwFHaiioatXi4eA6XQy-FJfi2jzu26_b3_wmxN5pI29fSqVeX8ko4Y3aZUhjF0ZKnnY97GcOfNV9p3vCLqyXMgEPH5IrHjzMTIHZ8Y6JQVYDTrLJxXw9PH7_2QJJG2Fnw65s689VRmL7veEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوباره خرید اشتراک Ahrefs ممکن شد. بخش Link Explorer و Content Explorer در دسترس هست.  با محدودیت تحلیل روزانه ۵ دامنه.  کد تخفیف: mohsentavoosi  لینک خرید: https://limitpass.com/clients/cart.php  بسته Titan یا Ahrefs Standard هر دو Ahrefs دارن.  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/mohsentavoosiseo/582" target="_blank">📅 17:27 · 08 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-581">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🟢
عنوان رپورتاژ
حرفه ای یا آماتور؟
انتخاب عنوان رپورتاژ تو فرآیند سئو خارجی خودش یه تخصص و یک دنیای وسیعی هست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/mohsentavoosiseo/581" target="_blank">📅 17:23 · 08 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-580">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/mohsentavoosiseo/580" target="_blank">📅 23:12 · 07 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-579">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رقابت گوگلی با برند های قوی
🟢
برای چیره شدن در رقابت با سایت های بزرگ و برند علاوه بر اینکه باید حداقل های مالی تامین باشه، انتخاب کلمات کم رقابت و صفحه بندی و تارگتینگ دقیق و فرصت طلبانه به شدت مهم هست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/mohsentavoosiseo/579" target="_blank">📅 20:28 · 06 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-578">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🟢
رتبه گوگل ایران و خارج و VPN
فصل سئو بین المللی دوره کامل به این موضوع پرداختم و واقعا موضوع ساده هست درباره رتبه گوگل در داخل ایران و در خارج از ایران
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/mohsentavoosiseo/578" target="_blank">📅 16:45 · 05 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-577">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwGlLBQfu4efsRIMyddjf_8OnH9wFSqU3fAznj2USNJB-6daIqBBNjpl4f0vEiBXmEMbfFBV5tnaCyoA1gmMpTrBuCcw_DuwWTrvCSCgShzWFSsuvvK4RPC6IIexdrfiCfeCqkCbZZy_kYGqFsOpn0O3rSe7po491cURQgkdV6q44VFVtQq5ug9vY6RoKRsGIAcA1z3AZK3AK8oxoMS2_HPJNXCE_5DvH-MWDvVY9j1eeY36Oj2dQATDSjEPjZvdTBWyKNe46RYklMofrcbRI7TSiCYGD8y-ooa2sGyHirAD8IVYvrTtLK4JmV02kHcECL4Sqiu3STQxE0O9nkOrCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته هایی که از نظر من مهمه. اما پراکندست و تک موضوع نیست. قسمت اول.
توضیحات زیر ویدیو، فهرست زمانی داره.
https://www.youtube.com/watch?v=P9NGXdQF1Ks
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/mohsentavoosiseo/577" target="_blank">📅 13:46 · 05 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-576">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">به خدا من زنده ام!
تفکری که وسط نداره. یا باید آمپر بچسبونه یا باید یخ بزنه.
مهم پوله. وردپرس و افزونه برای من و شما و پدران ما نیست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/mohsentavoosiseo/576" target="_blank">📅 13:01 · 05 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-575">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🟢
کمپین رپورتاژ سئو
اف پیج سئو اصلا به این سادگی ها نیست!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/mohsentavoosiseo/575" target="_blank">📅 14:25 · 04 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-574">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🟢
رتبه گوگل سایت خدماتی
اولویت بندی کلمات کلیدی سایت های خدماتی مثل بقیه سایت ها شاخص های یکسانی داره. ویدیو رو ببین.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/mohsentavoosiseo/574" target="_blank">📅 12:27 · 03 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-573">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🟢
بک لینک Sitewide
لینک سایت واید نزن!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/mohsentavoosiseo/573" target="_blank">📅 09:46 · 02 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-572">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🟢
کسب رتبه گوگل در یک ماه
این ماجرا افسانه ای بیش نیست که سریع بیایم بالا و بعد بریم پایین
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/mohsentavoosiseo/572" target="_blank">📅 09:18 · 01 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-571">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">از ۱ آذر افزایش قیمت دائمی داره دوره.  طبق معمول هر سال که کمپین فروش و تخفیف نداره. حتی نوروز. و هرسال نزدیک زمستون افزایش قیمت داره.  https://mohsentavoosi.com/video/seo-course/</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/mohsentavoosiseo/571" target="_blank">📅 09:55 · 30 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-570">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ویدیوی کامل:
https://youtu.be/P9NGXdQF1Ks
نکته هایی که از نظر من مهمه. اما پراکندست و تک موضوع نیست. قسمت اول.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/mohsentavoosiseo/570" target="_blank">📅 14:33 · 29 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-569">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🟢
ریدایرکت گروهی
چطوری به صورت دسته جمعی، صفحات سایت رو ریدایرکت کنیم؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/mohsentavoosiseo/569" target="_blank">📅 13:08 · 29 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-568">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔆
من در اینستاگرام اعلام کرده بودم که تا ۲۵ مرداد و الان تا پایان شهریور، قصد دارم حداکثرم تلاشم رو در این شرایط برزخی کشور انجام بدم که کسانی که قصد صد خرید دوره رو دارند ولی توان پرداخت ندارند، بتونن تهیه کنن.  چه نقدی چه قسطی، شرایط ویژه ای در نظر گرفتم.…</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/mohsentavoosiseo/568" target="_blank">📅 12:22 · 28 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-567">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a79e28f998.mp4?token=NywguxoZT0Olb9R9Z4L3YpKAfSkjjZ6WQASwLzKMDSaPXwQP81UOSDKiWEF_wf-jG-YRWU-1kHjBvbIWm6gp_6-iO57MM-27a28F4vzfrEIvcNC2kJ0pBsoXp_Ag0LQRukC6ljRe5xvHr5fgeTtr1qrQPSaEzT0pS1j_JBlqBIylBAe_uiCIMqW6rEBSbHc64qU-6tWt9a1l2qSrASokKZ3Qe0FbzSysP2zfJyWDXlFNe1CWrcxZroeZFVl6TAFB-NAxOhA1hV28m4Zr5P5cB6cd1Q3s3NF8t-9XSikBZVZ8j0S0ekFflN5dp7WMREypVmACNn1RXoXuunDCIbzR0FMAFu3RhvJxI4BVEJ_tPpoHfvtscONCcryv-EwL_hZoXJIg2bIObTruFBNg48y_FNrA5y_6OkfyJPD4HCl3SPoDtO2wH1ittyYOtbcn2NBmgmM0RzfrGWF2glGZ3Lvg2cJj6ggYe1stO0HhZOudXPk2xPV9TL1QHu92O08G1jA-aAt1O_ysVsldVgxv_B8x2VBQOTG5dSpHgoerE2xcnbEMsgzJpw2PZ6TZQnH7F3GY1upXOVq61XAm2ZV1mTeu5mstbaicT5E1HxAC3aG8t2SzWE8lUA14PYVfptUjx7ykEes3KRfnZ9x0Dg5yZ5LDsEFwTX-BzWh7oHlqoqWkZcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a79e28f998.mp4?token=NywguxoZT0Olb9R9Z4L3YpKAfSkjjZ6WQASwLzKMDSaPXwQP81UOSDKiWEF_wf-jG-YRWU-1kHjBvbIWm6gp_6-iO57MM-27a28F4vzfrEIvcNC2kJ0pBsoXp_Ag0LQRukC6ljRe5xvHr5fgeTtr1qrQPSaEzT0pS1j_JBlqBIylBAe_uiCIMqW6rEBSbHc64qU-6tWt9a1l2qSrASokKZ3Qe0FbzSysP2zfJyWDXlFNe1CWrcxZroeZFVl6TAFB-NAxOhA1hV28m4Zr5P5cB6cd1Q3s3NF8t-9XSikBZVZ8j0S0ekFflN5dp7WMREypVmACNn1RXoXuunDCIbzR0FMAFu3RhvJxI4BVEJ_tPpoHfvtscONCcryv-EwL_hZoXJIg2bIObTruFBNg48y_FNrA5y_6OkfyJPD4HCl3SPoDtO2wH1ittyYOtbcn2NBmgmM0RzfrGWF2glGZ3Lvg2cJj6ggYe1stO0HhZOudXPk2xPV9TL1QHu92O08G1jA-aAt1O_ysVsldVgxv_B8x2VBQOTG5dSpHgoerE2xcnbEMsgzJpw2PZ6TZQnH7F3GY1upXOVq61XAm2ZV1mTeu5mstbaicT5E1HxAC3aG8t2SzWE8lUA14PYVfptUjx7ykEes3KRfnZ9x0Dg5yZ5LDsEFwTX-BzWh7oHlqoqWkZcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
انتخاب عنوان رپورتاژ
انکرتکست خیلی مهمه! مهمه معنیش این نیست که عین کیورد باشه!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/mohsentavoosiseo/567" target="_blank">📅 11:12 · 28 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-566">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🟢
بهترین جایگزین Dynamic Rendering
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/mohsentavoosiseo/566" target="_blank">📅 17:05 · 27 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-565">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-0xS3qOcidRUbMyNB4iMM0UWGRMR8--XfPW59WM89UqJ41cC-eDv2shLmSHFitiwsMxoVZJDDb2Ps2EPjIlBMxRpepz3S0JiaqJc0mA3Dyf8gQgoz_DmzWpNGiiJJb5BY4rdHTNkccbcptlgNsCn9ycyFNxQFwOT6gk7UERdYu8-2QMoTSMNQAIDLBefmdvgi6_Y4TNtxseMt_owyB1Bgu02BioU6kdvrcC64Y2X9H8iQ5A5Xwf7eexnEOYWqUdZPDRfxejZ2qN82GixrFxN_hcv9K3MAuVuxl7efEZiL_KSAYiVkPpJA2vxxlY3QUq2Gu-lFNZ5c57FzvvLFlsYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز خیلی ها فکر می کنن که ادرس سایت مپ حتما باید sitemap.xml
یا sitemap_index.xml
یا post-sitemap.xml
یا... باشه. که سخت در اشتباهند.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/mohsentavoosiseo/565" target="_blank">📅 13:42 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-564">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">mohsentavoosi.com/sitemap.xml
😶
😶
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/mohsentavoosiseo/564" target="_blank">📅 13:32 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-562">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شرایط اقساط ادامه پیدا می کنه اما مبلغ در کل از ۱ آذر افزایش خواهد داشت.  https://mohsentavoosi.com/video/seo-course/</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/mohsentavoosiseo/562" target="_blank">📅 19:09 · 24 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-561">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMvdXo6LueKZ7ZYAlyhIE6glwSRlNrxPyyWgy8M5YWzmGOb_Vs7Pi8oz-PWF06jpH4Id6Gq3Cq3u6BAYhDayPUj-jWrXwe4o1Cn9fPJTXQAe7WvmLodA1jqsSWXdWXQmwLACLuwX6v0ABJ-6B6Q0gqg5lXHWahr-2Itj06mh4bKOlsoT3wGyfvg_njvPnfanAM0iZ1VLJjJsmuG0W1zVNWdKDZgrkORTG9YIZ8s9knZ8QuIs3dlBeRNf66Vo1Ky1QUvIllwlinodO_qrTmlBvV_3C2pYfro7SFId1iEVmuUK146LuNOMY8_M8Hys1aNXNEbPTCe9ZlHZ-jJAfes8zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش تخمین بازدید و کلیک سایت در آینده
لینک آموزش:
https://youtu.be/G1wyAeQxAnM
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/mohsentavoosiseo/561" target="_blank">📅 16:03 · 24 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-558">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔆
من در اینستاگرام اعلام کرده بودم که تا ۲۵ مرداد و الان تا پایان شهریور، قصد دارم حداکثرم تلاشم رو در این شرایط برزخی کشور انجام بدم که کسانی که قصد صد خرید دوره رو دارند ولی توان پرداخت ندارند، بتونن تهیه کنن.  چه نقدی چه قسطی، شرایط ویژه ای در نظر گرفتم.…</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/mohsentavoosiseo/558" target="_blank">📅 10:19 · 18 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-557">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pv4g0lmZ_wYhLpcjOEe5xrN0M-RYQhBpPbwC9goHAMKxybU3Oo87PLlGrnFzqS9aEiFkeJHeyrtpk4hW129eXEJeQwkjLXHKURbrBx1ZhzvdPUr95HeJehi6FJAKT5Rk5bDp58kjPm4Ez6K0_Y0wQuvyBlSMkc_LrkOY3tYtF-YwaXrXRtn747uCAEF1E7xjJ1du628kublPvwHY_PM0DR6F4o5ettIkHIbl8GTx4gUpeuPvyM7D17wpA4TM-ZrmhLvRfLFfP_XFw7TKgmTFjqbPB0BGfK0LiQjL-j1TXV0oQnKm8CrDynFhUBK_IFnyAwMcfbDQW1x0JH7qENbz0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدایرکت گروهی در SEO
لینک آموزش:
https://youtu.be/QVNgzWYGTks
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/mohsentavoosiseo/557" target="_blank">📅 18:29 · 17 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-555">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACUiqLv585IlH9tGn7fqIUStMMuJ8NxlHbqMPKgBZbi78RAsZ0RhKxzG_u19iQvGBpTgtF9KrUmAZOwhdnc7OoqcW6LmiCDpsuprYENiDXIZk4xw7ZIxefYptj0AHwYj-XH4yRu-lwhkFgpqx707QWypJiP8gM9W5caKCyMtxUIcdONLCm2hOzVsMmxVTH_bibrQd4zGXrVEUtSSE69uA4qG3Rkmx2V6TgJL8J-ZQB_QsMy8YEW9PSpSYKGvIDrnivOZFkZ3HiZ2GN_3CTTZo04d9U_qEJZap4Hg6xQIEpKgph6jlYM6BzY8aYFbGJENsShwIrOKgdY9KsrJ7BFvig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایراد گوگل سرچ کنسول در نمایش تعداد Click و Imperssion
لینک آموزش:
https://mohsentavoosi.com/video/search-console-click-count-bug/
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/mohsentavoosiseo/555" target="_blank">📅 17:15 · 13 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-554">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZ1HuDypVj_gO82FlZTymq-zYTTgWa8AhxC8obA34ow29jovx7blZX08JLDWsFoyoi5Ont7cWDEoOvuVHx2XaUs4O-zxt9TgJUdErMR8uLMRnlBXOL1y8gM_wAybaI0XQfBql9OzSwCbAofWX5_WdftpTBd_3lc84GTHKGY9jDcfqfA-6JJv9udyERWTur55Y9g2xnHgIX0_alBN4tmZs6P7axjdpfBpJbFIrDbIP8WClk4gOBGuYj0Wy8gCIJthWVlVY5M_3L3yyNdWnPbeO6NnCOgpP6YhRXOo86zkw9jPJO1_xWib6wo_yCS3TzH72Pc0tu1bBB52oz7La473zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من خیلی می بینم که به دنبال ابزار رایگان هوش مصنوعی هستند. یا مثلا میگن فلان ابزار AI همه ابزار های هوش مصنوعی رو با مبلغ کمتر داره! این به خاطر عدم آگاهی و اطلاع از این هست که هیچ رایگان شدنی بی دلیل نیست و هیچ ارزان شدنی بدون تلفات نیست.
برای مثال ابزارهایی که همه ابزار های دیگه رو یک جا ارزون تر میدن، دیگه امکان آپلود فایل رو نمیدن. یا ارسال ویس یا حافظه ای که پاسخ دهی رو برای شما Customize کنه! ابزار های رایگان هم که تکلیفشون مشخصه!
یا صرفا دوسه تا تقاضای اول رایگان هست که دون پاشی هست برای خرید بخش پولی. و کسی که حاضر هست این همه انرژی و هزینه مالی مستقیم و غیر مستقیم بابت ارزون تر یا رایگان گرفتن چیزی بذاره، قطعا یا کاسبی و درامدزایی نمی کنه یا داره پول بیشتری هدر میره و انرژی بیشتری تلف میکنه.
این صرفه جویی ها به نظر صرفه جویی هست اما درامد شما رو به شدت کم میکنه! توی ویدیو با جزئیات بیشتر توضیح دادم!
لینک:
https://mohsentavoosi.com/video/ابزار-رایگان-هوش-مصنوعی/
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/mohsentavoosiseo/554" target="_blank">📅 20:53 · 11 Aban 1404</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
