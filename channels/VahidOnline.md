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
<img src="https://cdn1.telesco.pe/file/PeSsJILjTO8M8u4EQhmKG80ubha1wYMk6xAKagK6vxVna81wzYYdTT53suvikHSh_zz7v-f8HeyTVl8TKQef6Rlv1rYe3Axbd3H4wg9P6cYDmRaOIjsd1h2dyssdtc2SQfI_xk4dBbnPoDsfpS3Hs6w68aBeGQN7R1Cr2Vvm6Yezn1sHTnmaeRQO5w9zPn3chbc19-oozwJ5djVTvjQH61ip7oMqch1VGozYDXO1MfXi98KcTfhY8LzGNx7SNDQVUg5OzRvI_sJBzT13Ol7Ma6ec11bLo86nQ3-x3y6drPcPNiUGhPZGchRqTZTdwLar9SS-F1QBJNpWBSO6dTAWcg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.39M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی می‌گن. اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جوری که می‌خواستم به خودم نشون داده بشن می‌گذارم.ممنون از حمایت‌های ماهانهvhdo.nl/patreonیا گاهانهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 05:31:08</div>
<hr>

<div class="tg-post" id="msg-78715">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mzAAVf2zlXwZt5xaJLAfA6mekW_aL3_4DpzzgDDc3tlu3uI72GJiiF1fzRUQhywgVqBY3ErWysGYe95uIV8QJbJrz-PA1vfYfoUUMTSOIVl-YK23Qk35c4xAyfpTmad9_iYsGZlOjRghjbXCjBaAN_onxUm9n3zJLPbV1E9lewb3gKMNxomMsy0Pl82oFL9ArlSlH5m9BId7-Sh7SebHU-CQK8eF3ybf0caFWN8NZ7tTnYPhYEqPHW1JB1WwUPJGAMGDTj2RXCQ-CD_vtav51Y5CPXdxUGt8EoKyDi3KMPfOs1Dx16XQXyMTM1nfeopTQlaXbSFr8Cj3g884GTSYYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l7HmH___cNbCjQGSWo-TiIiYQtf92rMMvro6ssYE4WzGK_bVzMpsNpgnCWfv3zMU5Wfo-w-K7DiAFIZga3O5E2X-wCOxo0iuTGYV-duixYxOcktbw_ljClbt_KuP6za2IiWSi4UFRgZUlSL5TkZqrywyWLrHT6JIvajeJRH-hm_G496akpVHExBTOZCGGWF8LHdhYxic3aone70Kh5Lxbv7crClN-XLakj_0TTCEh0UO9esA2AJiq6UvdM7qiEkoD5ed2RNAkpnRjtgd8XxdXShh-g12TEFQRcNIg8bIBAXEit6lVnmnP_rvxZPNvosceJA74_ikjwO7Mh4vioORxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اکسیوس سه‌شنبه ۲۱ مهر به نقل از دو مقام آمریکایی، یک مقام اسرائیلی و یک منبع آگاه گزارش داد بنیامین نتانیاهو طی دو هفته گذشته چندین بار با دونالد ترامپ درباره ازسرگیری عملیات گسترده در ایران گفت‌وگو کرده است. به گفته منابع، دو طرف احتمال عملیات مشترک آمریکا و اسرائیل علیه اهداف نظامی و هسته‌ای ایران را بررسی کرده‌اند.
نتانیاهو درباره اقداماتی که اسرائیل معتقد است جمهوری اسلامی برای بازسازی برنامه هسته‌ای خود انجام می‌دهد، ابراز نگرانی کرده است. اسرائیل به‌ویژه نگران احتمال استفاده جمهوری اسلامی از «کوه کلنگ» برای غنی‌سازی اورانیوم است.
اکسیوس افزود اعضای ارشد کابینه ترامپ دوم اکتبر در کمپ دیوید درباره احتمال ازسرگیری حملات گفت‌وگو کردند. یک مقام اسرائیلی گفت ترامپ ابتدا به حمله متمایل بود، اما بعد مردد شد.
یک منبع آگاه گفت پیت هگست، وزیر جنگ آمریکا، و فرماندهان سنتکام از جدی‌ترین حامیان ازسرگیری حملات هستند، اما بیشتر مشاوران ترامپ ادامه فشار اقتصادی را ترجیح می‌دهند و معتقدند این فشار «روزبه‌روز بهتر عمل می‌کند».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/VahidOnline/78715" target="_blank">📅 23:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78714">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UjRklKiTAlCqcy-LcoSe0i29cUM3ExlQISvlaTGSTSkfxU4cEEtEnjab4nQ6_I6vpYZtMIF3zaAc-OrNsw-Aortee8VoKz678et83nlwPOHgnsv8nCXpTlOpW4gBOY9BpiQgcqhIk14qhp0q1iQ9QmjddCFJqOndeD1JMuzPoQAoK8OL3kaEjkc1_Q7ev-FJrmBb-rZkzhi_tGMpBKHKeoc87ygPkI8Br8wsADLsA7EwiX5CKl5DCIL79MdODA-HDmlCesyhXPQ5KX4FKKSvYA7tiGgJrs4yq32OI1c1u3su_uuud87MyPA2EgKAUGSNuxS-mSMIk8KgL6YeR4sawQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی هشدار مقام‌های عربستان سعودی دربارهٔ تهدید حملات هوایی، روز سه‌شنبه ۲۱ مهر صدای انفجاری مهیب در ریاض، پایتخت این کشور، و چند انفجار در نزدیکی مقر شرکت نفتی آرامکو در شهر ظَهران شنیده شد.
به گزارش خبرگزاری فرانسه، مقام‌های عربستان با ارسال هشدار به تلفن‌های همراه ساکنان ریاض اعلام کردند که این شهر با «تهدید هوایی خصمانه» روبه‌رو است. خبرنگاران این خبرگزاری اندکی پس از صدور هشدار از شنیده شدن صدای انفجاری شدید خبر دادند.
هم‌زمان، شش منبع به خبرگزاری رویترز گفتند که صدای چند انفجار مهیب در نزدیکی مقر شرکت نفتی آرامکو در ظهران، در شرق عربستان، شنیده شده و این مجموعه تخلیه شده است.
یکی از این منابع از مشاهده دود در مقر آرامکو خبر داد، اما این شرکت هنوز واکنش رسمی به این گزارش‌ها نشان نداده است.
ائتلاف نظامی به رهبری عربستان نیز اعلام کرد که قطعات ناشی از رهگیری یک پرتابه در منطقه‌ای مسکونی در ظهران سقوط کرده است.
مقام‌های عربستان همچنین در استان الشرقیه این کشور هشدار خطر حمله هوایی صادر کردند، اما اندکی بعد اعلام شد که تهدید برطرف شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/VahidOnline/78714" target="_blank">📅 23:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78713">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rwcrooE8yao---at7QCts4prauokMrPMqPO-I02TwuQZK-uteBM4Bhsp5-jX5HQkxP7-7kRY0zfpPjOgzEmnWdFwhFYXSEzvG68inqUupHd9wnDwFRqwLMHnPuvNE_2RCYE7EaZgYPm7ahym4mM_UYianMuj0Z6QkIzESWwCLsKH5sZYmvfbpLt2U9tWxhgD-b7Y6otF-CW8EpXGJgCmF9VEzfldf3DHubzyk_QXBPXRwMjknoZtHCdUsrP5a1O41rbbUn-0D4ryke78qAp1ZdM_MpK17L8ZiwGFtc4Dk9TbWlhGj-M0BRwCm1S1BiAnwbglJPH1emo9M4whCvhQVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است. یک منبع تأییدشده گزارش داده است که یک نفتکش بر اثر اصابت پرتابه‌ای ناشناس هدف قرار گرفته است.
مقام‌های مسئول در حال بررسی این حادثه هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/VahidOnline/78713" target="_blank">📅 22:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78712">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cTxiD2-BuUR1M_dVZ8VY0iO4CwUApfbRlBdEUwxZtYwwojziThIFt2QDKA523eTHE9f7zrkklm-yjp1DEjzfGeQ3-2S3C1GHuMNpoHk_tFjCLFKaDlJnN5k6KBliS0yf6zdzqR0szU1FTwyu80gz9S44Rv9iRJT2fheLNQjg7x8eWg1HXNvkafv5_qK9MkD-7vaAPkIuEI0maH6ifkJPqIhk-t_O_u6NWVQQb9fFqYrB7LxYM-Fu-EguprPPSoZ-pn5FbiHQ22s0INGNtJSxloh4hMBo_pV6Bfzaldpdi9xFtzsWExqoe9Wf2vB0gb_Gb__0PN9Ks3UcgVmiapCOuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
حوثی‌ها رفتار بسیار بدی دارند. فکر می‌کردم یک سال پیش، وقتی آن‌ها را به‌شدت بمباران کردیم و به درخواست خودشان حملات را متوقف کردیم، درسشان را گرفته باشند.
مدت زیادی ساکت بودند، اما حالا دوباره سر و کله‌شان پیدا شده، احتمالاً به دستور ایران؛
کشوری رو به نابودی که نه نیروی دریایی دارد، نه نیروی هوایی، بدترین اقتصاد جهان را دارد و نرخ تورمش ۳۰۱ درصد است.
حوثی‌ها به شکلی بسیار زننده دوباره وارد عمل شده‌اند، به عربستان سعودی حمله می‌کنند و عمداً می‌کوشند قیمت نفت را بالا ببرند، احتمالاً پیش از انتخابات آمریکا — اصلاً کار قشنگی نیست!
یکی باید برایشان توضیح بدهد که من در انتخابات نامزد نیستم. من قبلاً پیروز شده‌ام، آن هم با یک پیروزی قاطع و کوبنده، اما بعد از انتخابات هم سر کار خواهم بود و هرگز فراموش نخواهم کرد!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/78712" target="_blank">📅 19:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78711">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIonM0TEUt5PtSZGctf_GxElZttuNS-XxYLz387QbvQBCt17pBC2i08uGiy1Lzyyr8fVbO_AfMnEsn3edUgJVixFc5tZF-zEoaOCvhiXv5sYFx-baXp0Pq7IJB_SHVBbJYO8oLHQ88GkOMAznSBpiuNyTMisKYUd9ozh0dhlAU7h9JsrmfkN0cluSyzATudOxA0tpIZX4HlkyFFm2RVmlJE08mhRJRvV_1fHDh4msmcw5_PzyO4FlS1Z2zDLTSsVk6115JWVJas2eExHjd1uswRQ4983YhYfXWVP-jlf6GQ5M9NH1ps6CeL3XZZ5AzSj_4fRtIekJCCJHyvH9GvSgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهوری اسلامی و رئیس شورای عالی انقلاب فرهنگی، مصوبه اختصاص سهمیه به داوطلبان کنکور آسیب‌دیده از جنگ‌های ۱۲ و ۴۰ روزه را برای اجرا ابلاغ کرد. بر اساس این مصوبه، داوطلبانی که در جریان این جنگ‌ها یا حوادث پس از آن، محل سکونت خود را از دست داده‌اند، در صورت احراز شرایط مشخص، به مدت دو سال مشمول سهمیه ۵ درصدی ایثارگران خواهند شد.
بر اساس متن مصوبه شورای عالی انقلاب فرهنگی، این تسهیلات شامل داوطلبان ورود به دانشگاه‌ها و مراکز آموزش عالی می‌شود که ساختمان محل سکونتشان در جریان جنگ‌های ۱۲ روزه، ۴۰ روزه یا حوادث پس از آن، تا زمان برگزاری آزمون، تخریب شده و دیگر امکان سکونت در آن وجود نداشته باشد.
طبق این مصوبه، ساختمان آسیب‌دیده باید در وضعیتی باشد که نیازمند احداث مجدد، مقاوم‌سازی یا تعمیرات اساسی محسوب شود. بنابراین، صرف آسیب‌دیدن منزل یا وارد آمدن خسارت جزئی، به‌تنهایی برای برخورداری از این تسهیلات کافی نیست.
این مصوبه در جلسه ۲۳ تیر ۱۴۰۵ شورای عالی انقلاب فرهنگی به تصویب رسیده و اکنون برای اجرا ابلاغ شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/78711" target="_blank">📅 16:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78710">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKLsLyP38MrAKELsyVd5iyhHsxmrmGkXWrjHiaEf5YC2VpGGyhHXK3f0ZPaWBxaKhMhOv9oAwgKPtxkwrHX1zZb95SdVIS3PnD5Kfju8o71yJRvkJLRAtLYcvOX62Norjs7UlyBKU9dlhVyfJ6vMeDxPEb3VJxfDzrup9pG2d6w1513Ed7VeX1BLfni4Ll0ug0N20yrPdYIWKPSjKO9sxFrVEpzZMZetyMV1chTexDX59KNPHp9R-8LL5d46Ww-hxWjFzNWF2j0l3HEhQ8Kx2GSQFu9KqIZ0O7kbVHUu7daLceh6OZn9K2lfIwTa31yx0lm8ovoemF7Ag5TZ-Tnfkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عفو بین‌الملل در بیانیه‌ای تازه که روز سه‌شنبه، ۲۱ مهرماه، منتشر شد تأکید کرد که جمهوری اسلامی از مجازات اعدام به عنوان ابزاری برای «بالا بردن هزینه اعتراض... و ارعاب» مردم استفاده می‌کند.
این سازمان حقوق بشری در بیانیه خود از اعدام پنج معترض دی‌ماه ۱۴۰۴ تنها در عرض یک هفته به عنوان گواهی برای این مدعا یاد کرده است.
قوه قضاییه جمهوری اسلامی از هشتم تا ۱۳ مهرماه جاری از اعدام این پنج جوان معترض خبر داد:‌ علی همتی سیستانی و مجید نیک‌اندیش در مشهد اعدام شدند، سیاوش جمشیدی خیرآبادی در شهرکرد اعدام شد، و علیرضا سپاهی و علیرضا رئیسی که در شهر اصفهان به دار آویخته شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/78710" target="_blank">📅 16:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78709">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAkpIOLYDB8qv2J0yylsY3XqYZ5nnNJ1ATf3_YJiA0Z49oyd1cbf64flEok2lRGTkGEFouF1bTg84s__pgjWFpZgvCoeDMP9OtSIZCmGGrcqyEDafu8STM4sL2qu4xN1190Jmo-O-n0en0Ua3sezKF5BKBAwipW_YW3-ljCs2DL88SB2ZoaGVUfhojVprXNw4hzCTrnv-oTbc_OjMQpLbC3BOmaW4c8BF27BogHMTWwYw8jWJXdH3aERvgzM77XtVaAGELJNe-o18-lAMfhJCUc6m_ISEw-l-elo5RK8-1cPPhiTOLsV_jcir2QK4k-1KQt5-UCkt3swVO7vygBTyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال‌ به نقل از منابع مطلع گزارش داده است که برخی مقام‌های جمهوری اسلامی در گفت‌وگو با مسئولان کشورهای منطقه،  در پیام‌های علنی و گفت‌وگوهای خصوصی هشدار داده‌اند که جمهوری اسلامی حملات تازه آمریکا را با گسترش درگیری‌ها در خاورمیانه پاسخ خواهد داد.
منابع مورد استناد روزنامه گفته‌اند اشاره به احتمال ورود زمینی نیروهای ایران به خاک همسایگان، بخشی از تلاش مقام‌های جمهوری اسلامی برای بازداشتن واشنگتن از حمله بوده است.
به نوشته وال‌استریت ژورنال، مقام‌های جمهوری اسلامی در پیام‌هایی جداگانه به مسئولان کشورهای عرب همسایه گفته‌اند در صورت آغاز دوباره درگیری‌ها، اهدافی در منطقه، از جمله تاسیسات نفتی عربستان سعودی، ممکن است هدف حمله قرار گیرند.
محسن رضایی، دبیر شورای عالی امنیت ملی، نیز روز یکشنبه ۱۹ مهر در گفت‌وگویی تلویزیونی تهدید کرده بود که در صورت از سرگیری جنگ، زیرساخت‌های دیجیتال منطقه، از جمله کابل‌های ارتباطی، مراکز داده و تاسیسات هوش مصنوعی، هدف قرار خواهند گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/78709" target="_blank">📅 16:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78708">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M251Af_ZjAzGOC_N7-mS9KeIQu1e3QatLyCfocMTEECGThEG4FRYDPeDzFVn5JzymPByoqkXKyz-_G5jY8WrmyM1O4kjudIkZD8iwFHt7mho90N6kRsgwh_vGPwLxWA3dR5ABnCH1UZR8xoKJrTioZUrWLQwzG1bmYKiRTgPcjoFKhZl4iNh_C_1w4GRkyAtIc9KqdZFcFTGxq9scX-JnLhDNrna1KdW0QRa0fsKhBc9J6lQu83a93hEUubV7I94eHeRKMvOCh88o0Gl7R-cUij1z5vc9fv5iD-oQtQjBGkzeMIt5a27tFQPMhi7zTqP5vUSJlA3lu2jU1M_RkH6ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسدالله جعفری، رییس‌ دادگستری استان اصفهان، انتشار فایل صوتی عقد علیرضا سپاهی و مهشاد کشانی را از دلایل بازداشت امیر‌سالار داودی، وکیل دادگستری، اعلام کرده است. او این فایل را «دروغین» خوانده و داودی را به انتشار مطالبی متهم کرده که به گفته او موجب «تشویش اذهان عمومی» شده‌اند.
جعفری روز سه‌شنبه ۲۱ مهر ۱۴۰۵، در اظهاراتی که به نقل از روابط عمومی دادگستری اصفهان منتشر شد، مدعی شد انتشار این فایل در صفحه اینستاگرام داودی، زمینه «سوءاستفاده تبلیغاتی» رسانه‌های مخالف حکومت را فراهم کرده است.
علیرضا سپاهی، از متهمان پرونده «میدان علیخانی» اصفهان، بامداد ۱۳ مهر اعدام شد. داودی پیش از اجرای حکم، فایل صوتی قرائت خطبه عقد او و مهشاد کشانی، نامزد زندانی‌اش، را منتشر کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 201K · <a href="https://t.me/VahidOnline/78708" target="_blank">📅 16:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78707">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkN4dpF2YPE1xdXm3sC2QdNlNHJoG81n0N9EWo7buBDzYmjTE0Dqkcj81PV2o8yv8NHkoEsa8uZa5DjESQqEdLcMerb5btALI5010y0rK_dzKp_5QmnQYskMwOnhF6wSQ2DBPEZrGr-vyAhm1Q2fHU-jLImIJEJ9w7uLuV-0FkY8l4g9IDoIYCBW-c-wz6OhN2RSyOnwYT1GlOZ0Uzj0JpROwUbWSD4DrV7g8S073RIiBmQIvnJ01Fc_WH2R3H68vvx1tCpgxLUB4fjQhwtHcE0ez4QCjuu7FvUgWTtMLptWR6Y0-P69c5EbraCSQdh3OTWHk-5FHk7LQQhRXAn5Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگاه قضایی جمهوری اسلامی ایران از اعدام یک نفر در میناب خبر داد که دی ماه ۱۴۰۲ به اتهام «زیر گرفتن یک مأمور پلیس راه میناب جاسک» بازداشت شده بود.
قوه قضاییه روز سه‌شنبه ۲۱ مهرماه با اعلام این خبر، فرد اعدام‌شده را «قاتل جاسم حسینیان، مأمور پلیس راه» خوانده اما نام او را ذکر نکرده و درباره‌ی هویت او نیز توضیح نداده است.
خبرگزاری میزان می‌گوید حکم اعدام متهم مورد فرجام خواهی در دیوان عالی کشور قرار گرفت و در نهایت در این دیواننیز تأیید شد. با این حال از روند دادرسی این پرونده و جزئیات آن هیچ گزارشی منتشر نشده است.
از آغاز سال ۲۰۲۶ میلادی، این ۶۲۱مین مورد اعدام در جمهوری اسلامی ایران است که ثبت و گزارش می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/78707" target="_blank">📅 16:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78706">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nb51fXO1Nh1dv_BhRSjhrN8Rt5N6sLyF8bvM0zz6B5oRICldZYo-gHrpZ6hYc4dTbFHfXjFSy-xHyQTeMNRFwX0te4trg-F_VMi8OJd_81S6Ovh4R_VW8B4gXPkx8WMieqMEDlV0w14gt0dCDqix5ngEUZK-b6IIkZrL8zie6hujgqOXAJnQKHha3uMDbaJtJKEFA3wBePQ7lAQwxF9KgIZCfiY2oJuy4cJe1jsOX00utt3ncttDTRISiuQiWpnGXwzwYNFmPsVnoL7RkhtQ_ApKr0Cxu6S5-QxP_hya-Itlfql3synUozFB4sfXZ2VD8nU8bwWAWO9hWuP1IgEsAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
نظرات زیادی از احمق‌ها و دیوانه‌های چپ رادیکال می‌بینم که می‌گویند چین و روسیه دارند به جمهوری اسلامی «فوق‌العاده» ایران کمک می‌کنند. اگر هم چنین کمکی می‌کنند، در سطح بسیار محدودی است، اما من اصلاً باور ندارم که کمکی در کار باشد.
آن‌ها چیزهای زیادی برای از دست دادن دارند و اگر چنین اتفاقی می‌افتاد، ما از آن باخبر می‌شدیم، آن هم خیلی سریع!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/78706" target="_blank">📅 06:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78705">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n5zx03UCqxg3XcVcZyo-HFs4ljZmya4IUqBnVgar7S9LNvfeKhPOHN2GcqyRXa9awrZlFDaVvSUPCl0pt2XjY-D1glAsdh80GZlBm53wj-UDJRQU_m9jC-wVkauJCaJli0FD5dpZ9Dxgfsf3hIwfVl0jtYaMBaMZaLzTuhCwN9paoU81jYtT7aGUnWcNsJs_vWExGV6I1BZopmt_D2cVUsFL4xFlRMerXW9pt1P2capepIkBWAPCYYmgqh2hsBr43_YfYvK5H19D4SgPDpLHlw80EOTdzQmqRm9XoWPqK7sxFqUNQ2IsIt-0uI4nA449eZT0-bWacG_ok0-1CZ4gNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، گفت جمهوری اسلامی اکنون حتی رهبر و مقام‌های ارشد ندارد و واشینگتن برای مشخص کردن طرف مذاکره در ایران با مشکل روبه‌رو شده است.
ترامپ گفت: «مشکل همین است. شاید در برخورد با رهبرانشان زیاده‌روی کردیم، چون دیگر اصلا نمی‌دانیم با چه کسی طرف هستیم.»
او همچنین گفت: «هیچ‌کس نمی‌خواهد رییس‌جمهوری ایران شود. آنها نام افراد را یکی‌یکی می‌خوانند و می‌پرسند چه کسی می‌خواهد رییس‌جمهوری شود؟ هیچ‌کس نمی‌خواهد. من نمی‌خواهم.»
ترامپ با اشاره به دشواری یافتن طرف مذاکره افزود: «راستش را بخواهید، برای اینکه بفهمیم اصلا باید با چه کسی مذاکره کنیم، با مشکل بزرگی روبه‌رو شده‌ایم.»
رییس‌جمهوری آمریکا در ادامه گفت: «فکر می‌کنم زیاده‌روی کردیم. می‌توانستیم در سطح اول متوقف شویم. رفتن به سطح دوم و سطح دو و نیم احتمالا زیاده‌روی بود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/78705" target="_blank">📅 06:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78704">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uh6fyLl0xheMi7sokd575z44iNkf47KZgHgrVAoExGDlowe2Y9mE_2vDAB9y2naWTRwpp1EP1fSlW546r7hIJgJQDH3VYaYexR_jjP1dZFyirRhvkbb44o9MgrX-1nCrs8Vg4xq3XgvDjVJ0S1bFDLsJLYInsB3mlI3oTgxA2CfqFEp3qNPuaITIZliYdVCG4IrEQp5ihbw2X53W_na4Hffm9XrgiRL6gjSGTw2vM-5gqqQqpLUHYU93DD9O4ItcZLacBuQgpL3UWK4Itf9g293Bj_SRa1414yfqW72XUnl85J63uxNG41rf4KRmD_ilXTQd48uWGXWbcL2k7dawZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی نیروهای ائتلاف تحت رهبری سعودی اعلام کرد که پدافند هوایی این کشور موفق شده است آتش موشک‌های ورودی از یمن را با موفقیت رهگیری و منهدم کند.
دوشنبه شب، ۲۰ مهر دقایقی پس از ارسال پیامک هشدار تهدید هوایی به تلفن همراه ساکنان، چندین انفجار مهیب پایتخت عربستان سعودی، ریاض، را لرزاند که به احتمال زیاد ناشی از عملکرد همین موشک‌های رهگیر پدافند در انهدام پرتابه‌ها بوده است. سازمان دفاع مدنی عربستان سعودی حدود ۱۰ دقیقه پس از اعلام وضعیت هشدار، به شهروندان اطلاع داد که خطر رفع شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78704" target="_blank">📅 22:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78703">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/umgm8G3kl85Mec52HhxMu2ZkpgFQiz5x1zwHqHPXOTXXuwrAsyvMaHKpBkhOaEw2jzypdSY6roD5P6uHO-jw1zyuRi65CIBKoXS2L5adfdLOh5ZgYCVzV4zzOhFdRj8O1SSxScTuvemDMg-mZK6IxVLRDe0UOpiMsVZfyskYviZ36bwotejX5kIflpc2PeU68oweQBK-heR2yvh4J5On_q_ik40u_9G2NtjQ3RpptjZMNMmAicYZmAMwVFjMFYgfcXkcMps8L53K8xJ3lPgGJmL8QOgZ4oHhwKe5NrhL9yzr3uYq9iujSJXDvSLCl0FU972TIHs7Hwaa4U4Y1aXeJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا  گزارشی با تأخیر از وقوع حادثه‌ای در تنگه هرمز دریافت کرده است.
یک منبع تأییدشده گزارش داده است که یک نفتکش حامل نفت خام هنگام خروج از تنگه هرمز، هدف اصابت پرتابه‌ای ناشناس قرار گرفته است.
مقام‌های مسئول در حال بررسی این حادثه هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78703" target="_blank">📅 22:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78702">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JER2lxBAdpCxXJbUKJr9aGOxMbU_Dpc2WvKgcjsKWC6QV7T8xcKxjiQbt4GRYEjF3bYjYA1VtLvW0gTUcQhFQImYOiAznGffUtdzDEciT_dJt7_spvybpNxWRszZd6BnoKwj3hupXGrcKnL_xH3G5Hbn5IFxVIDyElsAcB9O-vRqqNhvcJnNuupkvJAHqozIoDxGB8KSCMB8dAO9K2yAJyH6XU0IExNNN7CTN7uJXdre3ZHyZH_WBVT9PyCiSEZw4L8WuFkvd25S0D3cFYwwwujONxYL6tpEcHf6RVhZz6_7diGDuBMAkdMojWzC98WTvoYBqHMGuGpfPBbF3Ahhyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیران خارجه ایالات متحده، بریتانیا، استرالیا، کانادا و ۲۳ کشور دیگر با انتشار بیانیه‌ای مشترک، فعالیت‌های خصمانه جمهوری اسلامی ایران در خارج از مرزها را به شدت محکوم کردند.
این بیانیه روز دوشنبه ۲۰ مهر، پس از آن صادر شد که اندی برنهام، نخست‌وزیر بریتانیا، اعلام کرد حادثه امنیتی اخیر در پایگاه هوایی فیرفورد در انگلستان «تقریبا به طور قطع» توسط سپاه پاسداران انقلاب اسلامی هدایت شده است.
کشورهای امضاکننده این بیانیه با اشاره به ماجرای پایگاه فیرفورد و سایر حملات اخیر علیه جوامع یهودی، روزنامه‌نگاران ایرانی و منافع ایالات متحده در اروپا، تاکید کردند که استفاده جمهوری اسلامی ایران از حملات خشونت‌آمیز، توطئه‌های مرگبار، آتش‌سوزی عمدی، خرابکاری و عملیات سایبری غیرقابل قبول است. آن‌ها هشدار دادند که هرگونه تلاش برای تهدید، ارعاب یا آسیب رساندن به افراد در خاک این کشورها با اقدام قاطع قانونی مواجه خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/78702" target="_blank">📅 21:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78701">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ac0389fe6d.mp4?token=ngVfJeWa5WH828qJxPdHaL0jg9YhY7v3olnloa6KbnVnoxX5xJKSIF-wUxUGu4U9-HDJIHFzS-L3fTnJEkHSiglmod7llaUpIRnehnqpN9pp7pViiRjSpypT8EI5c3OPZDcB0Kkc3GU127x4Z2ph79ZighFFObUGGtfHAMBcasEDGTJeWdhxTg4NlCdGhriptGXYq5CsnqImm8NpGXnstWhqRAQ5arWhTX_NdZPxZxyIiZ3SB9LVdrNmG1MwzyJ5kvMfvyXTe-KnGCR9KeidCnTo_ED9m1amOsOvPKtJB9X0kgByjej37CyNZLf2Bm7Fh0DM25ncKATCdkAdMiz1XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ac0389fe6d.mp4?token=ngVfJeWa5WH828qJxPdHaL0jg9YhY7v3olnloa6KbnVnoxX5xJKSIF-wUxUGu4U9-HDJIHFzS-L3fTnJEkHSiglmod7llaUpIRnehnqpN9pp7pViiRjSpypT8EI5c3OPZDcB0Kkc3GU127x4Z2ph79ZighFFObUGGtfHAMBcasEDGTJeWdhxTg4NlCdGhriptGXYq5CsnqImm8NpGXnstWhqRAQ5arWhTX_NdZPxZxyIiZ3SB9LVdrNmG1MwzyJ5kvMfvyXTe-KnGCR9KeidCnTo_ED9m1amOsOvPKtJB9X0kgByjej37CyNZLf2Bm7Fh0DM25ncKATCdkAdMiz1XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر بریتانیا روز دوشنبه ۲۰ مهر گفت طرح مشکوکی که پایگاه هوایی «آرای‌اف فرفورد» در بریتانیا را هدف قرار داده بود، «به احتمال بسیار زیاد» در ایران هماهنگ شده و قریب به یقین زیر نظر سپاه پاسداران انقلاب اسلامی هدایت شده است.
اندی برنهام در سخنانی در پارلمان گفت: «ما این تهدیدها را در خاک خود تحمل نخواهیم کرد. با استفاده ایران از شبکه‌های جنایتکار برخورد قاطع خواهیم کرد، با به‌کارگیری همهٔ اختیارات‌مان، این شبکه‌ها و منابع مالی آن‌ها را هدف قرار می‌دهیم و تحریم‌های بیشتری اعمال خواهیم کرد تا توان ایران و سپاه پاسداران برای آسیب‌رساندن به ما محدود شود».
اد میلیبند، وزیر خارجه بریتانیا، نیز خبر داد که در واکنش به این اقدام، سفیر جمهوری اسلامی ایران در لندن به وزارت خارجه احضار شده است.
پلیس بریتانیا روز یکشنبه پنجم مهر پنج مرد را در نزدیکی پایگاه هوایی «فِرفورد» در جنوب غربی این کشور به ظن ارتکاب جرایم مرتبط با مواد منفجره و تروریسم بازداشت کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/78701" target="_blank">📅 20:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78700">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oTYMwzkU9WSoemYscVw3eqbQdZGbsc54oIEabIxcNw-Cj5eMKK7XUdAn1_BnjLSU8qSNcSldQXnovrLX3VC3691RAH8ICRxGsx4p06mppOvdy3lYRrsusQnyiKcdpfNKpa8C2Nf6mjJoEX_ENXFqjKxkTyZg21UFds4d8pE6lfFZ-SzI3ebRnMLkDceHxN1sOtEtw7Q760BxdYF7WVhqd9eUEK8zA1t9_oBbNjB1vssisb-7ViPFKPuHHOfVdcRrWvO-hsKOLiyODrDsMb0tRIkvRpmP9InxeSeVrlZBC_9yjdaGLdGmTv3JrxtmO-lWn2gkERenOynNKx84c94zEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی برنهام، نخست‌وزیر بریتانیا، درباره حادثه پایگاه هوایی فرفورد، دوشنبه ۲۰ مهر گفت که به احتمال زیاد این اقدام در ایران هماهنگ شده و به دستور سپاه پاسداران انجام شده است.
نخست‌وزیر بریتانیا در واکنش به این حادثه اعلام کرد که دولت این کشور تحریم‌های بیشتری علیه جمهوری اسلامی اعمال خواهد کرد.
بریتانیا در تازه‌ترین بسته تحریمی علیه جمهوری اسلامی، دو شهروند ایرانی را به اتهام دست داشتن در فعالیت‌های خصمانه، از جمله جاسوسی و مشارکت در تهدید یا طراحی حملات علیه افراد در خارج از ایران، تحریم کرد.
دولت بریتانیا روح‌الله بازقندی و شهرام علیرضا تمرزاده جکی را به فهرست تحریم‌های خود اضافه کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/78700" target="_blank">📅 18:54 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78699">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3yNuPgzHEDN0EbcRb6yFLdsdjUc_FtycvJXEPm4a4eDVCwvBHQAg9U88qqOcchHJ80oexK3XRcDdArX8RavYAD-WRjdIy7nh-BEB85FhtTfM21aeC_kdYEMbG5ijVSXvocG8jUqzhTwfGSVj5iqcd4wDCvMoXAoNLJVJHLq1gYXxlaY8bsK4YFHiuGu3OFSB0l3ShdFRtstozA8HRL-vtEh5ruEK6FTuMfTUxMmvDkZK5gC0wVAbWg6EIOxdhd9B6AitRt3-SRGdqKpKT2jJk6pP7eybuUHMadOX2DG1GbWCHzg7yPJjiwJx4oBQfNay51OQ2CyM5CdvEJ0sfjtWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز دوشنبه ۲۰ مهر گزارش داد در پی حملات حوثی‌های مورد حمایت جمهوری اسلامی به فرودگاه ریاض، چند شرکت هواپیمایی بین‌المللی پروازهای خود به عربستان سعودی را لغو یا تعلیق کرده‌اند.
بر اساس این گزارش، ایرفرانس-کی‌ال‌ام تعلیق پروازهای رفت‌وبرگشت ریاض را تا ۹ آبان تمدید کرده و گروه لوفت‌هانزا نیز تمامی پروازهای خود به این شهر را تا ۲۴ مهر لغو کرده است.
شرکت هواپیمایی اتحاد تمامی پروازهای خود به عربستان سعودی را تا ۲۱ مهر و شرکت هندی ایندیگو پروازهای ریاض و دمام را تا ۲۳ مهر تعلیق کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78699" target="_blank">📅 17:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78697">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pp7KOaaBYCoHQ8yggz7YBYy6zBODtydWLyYpk2Cz0ol-7Wo9-vpQl1tIgNXb7_ZKFJOJbbrpHDlTm6hpnGkZoB2imIauNWDNc-UmVbpu8925KpJj8WhquaA7XR1ZSXjpZIhtuhZrXw5L67TKMGbnkKdPBxif5GCb_E_Lcs377HwDDhsRhoyv7y2eak4rfso2kaxzXe71joYcY7wfHiEIFVh6PlwDh1S2t-h9e93IehdKNOIlPGTGvRJTJKLk4AOrzDqhdbrm8gPHpF7ijPnfu0Pokvtl-shl-9cisOTLu3iyBpj56HEm5eqDK38swsTVFAFejUk_uJ0kUrUtDPwd1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nzVSsQUW9SL_VkbFvQB-7tJUVUZEE4MElR8S0N8GUWz8i6poyyviyCfcTD9ZsOqOLuqSOoFlV52As4RzEuI4EFSRWKLWWj60qoMOmrPtykbjo3LB-NFR8OTbR3cJMkyw53ER0S6Z-oWIYEj0P1eP2wjgWRI9DxoodqXYFABGrb_i5iy9_dBZShlhsjAgaEYcAd-ZpoUbbf7PU68jJ_OXjOWzg5eNOjlyC4jEilAoF1tB_dvqwhcQszaYlGGd-_qTRehEUjmDoJ2kn21ca4zjsGgtl3zwbVFhnMTLilqZpzcL5AYuyYcwXtmeGhwXvWMqKdwEGTxVnKvUinEYcSOSGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی می‌گوید که روز دوشنبه یک «عضو» گروه جیش‌العدل را اعدام کرده است.
میزان، خبرگزاری قوه قضائیه، می‌گوید که عمر درستاران به اتهام «بغی» (قیام مسلحانه) و عضویت در جیش‌العدل محاکمه و به اعدام محکوم شده بود.
میزان می‌گوید برخی از اتهامات آقای دستاران مربوط به حملاتی است که به مقر انتظامی شهرستان راسک، مقر سپاه شهرستان راسک، پایگاه پارود، و مقر‌های نظامی در فروردین سال ۱۴۰۳ در شهرستان چابهار صورت گرفته است.
به ادعای این خبرگزاری، تهیه محل اسکان اعضای گروه، تسهیل ورود این افراد به کشور، جابجایی تیم‌های عملیاتی برای انجام حملات مسلحانه، تهیه مهمات و سلاح و شناسایی مقرهای نظامی از جملات اقدامات عمر درستاران بوده است.
به گفته فعالان حقوق بشر عمر درستاران، ۲۷ ساله و اهل روستای چراغان شهرستان راسک در سیستان و بلوچستان و از طلاب مدرسه دینی شهر پیشین و از شاگردان سابق مولوی نقشبنید بوده است و از فرودین ماه سال ۱۴۰۳ در ایران زندانی شده بود.
تعداد احکام مجازات اعدام و اجرای آن در ایران از دی‌ماه ۱۴۰۴ به‌شدت افزایش یافته است. موارد اعدام به جرایم امنیتی هم بسیار بیشتر از سال‌های گذشته برآورد می‌شود.
@
VahidOnLive
, @
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78697" target="_blank">📅 17:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78695">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m8PVOu8Bv7Sho2JfyoLKp8Qqb2N5xmRXWurw9137qQrsF7ppQh1IsuFAvhF9w7itebzE1qIOwIbT2RqWtNBH5Q3U3yW1ArIA5UmmMDvAOpL093pXbg4V5r69uQY3CYziwfPCR92xAzexiBGQ_ePO_GhdDCaiEuBajLW3YR1sulmxXkSqNqyb1H8bLFTfIgWH4PB8E6CBUguo9uQAgDT_mXAT2CqY9ucypfMSk9dxx00FGktGzBoVgfmw784v2bgI0asrQCoF2bV-Ny1V7qsuXFAf1X86FQshwrA9dvHR55mJVqEzEwktbKx6KYJFON3E6qg4bM1YsQ2xosHKEOekuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1281277307.mp4?token=piyw-5izgU1aJZZ7pnJMDxpFUTjsKHE2SXPc-e2bylYrcQ5QAIMm5ki2P73Ik-oGnk6OWZvgbNk3gnMKuszQh9PC2vn4cAjrmiVZsfaxXuXvjb9p9-hbKty4gS5YgAUKZ8IlbQJcKT6VxwD0s-4T5gFx5siFP7BSzH7wsWdZYGxRyWbrysVagTpCwutyT9s_cfe0jxicCflFQN0d-ZwWG1-QNwP9D73qbwEsTqMbAENO2SRM49l1xum9iScLRfAazBFKa92DJmSHGtZ3ZbU76St1AoMYkvk7nJsUQqA4Px57J7ffs1N19Pe1j5OOwcHFZwtZ2VLTGtu1JA7AXtVQbA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1281277307.mp4?token=piyw-5izgU1aJZZ7pnJMDxpFUTjsKHE2SXPc-e2bylYrcQ5QAIMm5ki2P73Ik-oGnk6OWZvgbNk3gnMKuszQh9PC2vn4cAjrmiVZsfaxXuXvjb9p9-hbKty4gS5YgAUKZ8IlbQJcKT6VxwD0s-4T5gFx5siFP7BSzH7wsWdZYGxRyWbrysVagTpCwutyT9s_cfe0jxicCflFQN0d-ZwWG1-QNwP9D73qbwEsTqMbAENO2SRM49l1xum9iScLRfAazBFKa92DJmSHGtZ3ZbU76St1AoMYkvk7nJsUQqA4Px57J7ffs1N19Pe1j5OOwcHFZwtZ2VLTGtu1JA7AXtVQbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO)  با صدور هشداری فوری از «حمله پهپادی» علیه یک نفتکش در نزدیکی لنگرگاه بندر صحار در عمان خبر داد.
بر اساس به‌روزرسانی این نهاد نظارتی، این رویداد پس از تایید اصابت مستقیم یک پهپاد به این نفتکش، رسما به‌عنوان «حمله» طبقه‌بندی شده است.
بنابر این گزارش، مقام‌های محلی عمان در حال کمک به تخلیه خدمه کشتی هستند، اما تا زمان انتشار این اطلاعیه، ارزیابی دقیقی از میزان خسارات وارده، تلفات احتمالی و اثرات زیست‌محیطی آن در دست نیست.
@
VahidOOnLine
روابط عمومی نیروی دریایی سپاه پاسداران با انتشار اطلاعیه‌ای از انفجار و آتش‌سوزی یک نفتکش خبر داد و اعلام کرد: «یک نفتکش از نوع شاتل با ۷۵۰ هزار بشکه نفت خام، بی‌توجه به هشدارها و اخطارهای نیروی دریایی سپاه تلاش نمود از مسیر غیرمجاز عبور کند که به مین دریایی برخورد و دچار انفجار و آتش‌سوزی شدید شد.»
بنابر گزارش خبرگزاری فارس، این سومین نفتکشی است که طی روزهای اخیر در اثر برخورد با مین‌های دریایی به دلیل «نقض هشدارها و تردد در مسیرهای تعیین‌نشده» دچار آتش‌سوزی شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78695" target="_blank">📅 00:56 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78694">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCexReAXD9cvZk9l33zDngIqgmHkeT_JfksoZJxervjRxRITlyLhcKwxcGLxi-Oslp1KK0POAikWl0W-Ys3jbF3F7Z0YG9RdqKRuDRsG_a-Jh-mWaC_CtKuresR9RBp-9zbml6xeL8WiQlLkpEqtHS3fTgaXyoXibLZlI6VwAX2QSOFyg0arjJ7VmrH1EoM547rQRMjYu4OkjBCV82wiz4PKEIPYn1pQqNR5xYdUICNUrXswQXgSUbFEvgrwFftYEBohgcnKztInrfSSvlT9ncghVG9y-OUs7cUGbva-23f7HNdqQWPSM07yBLY0HE7VkfMFzU8cJDGFcfdPCyw7-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرودگاه ریاض روز یکشنبه ۱۹ مهر بار دیگر هدف قرار گرفت.
ائتلاف به رهبری عربستان سعودی در یمن اعلام کرد که یک «پرتابه ناشناس» فرودگاه بین‌المللی ریاض را هدف قرار داده است.
ترکی المالکی، سخنگوی ائتلاف، گفت این پرتابه به پایانه ۴ فرودگاه بین‌المللی ملک خالد اصابت کرد و موجب آتش‌سوزی شد.
این در حالی است که حمله موشکی روز گذشته به فرودگاه بین‌المللی ریاض که حوثی‌های یمن پس از ساعت‌ها تنها به طور تلویحی مسئولیت آن را پذیرفتند دست‌کم ۱۲ کشته و بیش از ۳۰۰ مجروح برجا گذاشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78694" target="_blank">📅 19:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78692">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dt9F9g6jM154RmO8_rrGdFRlxEvAjyhZw-YT0G0mHE4Hk4WmOry6p5RHtbAi_lYubC2KKkDWjzIAHiN-c2rjqQWxF2xpDj1yseXKxzPapb4VTuxGw3QqTa3kiWcOYpIjVq1pbAyoT5VufZhQi_WOG9jIYcWTk2aK4TBFvuZSYWoWvQF0iZL501f9l9mPXhtdaHd2i9dBDcoKogqPCdvBGkhb08O8UtINTVMwAiD1IUZE687Z8TGHKD7uOjuHQqPe2xPNKwxSUV7KP8QaQaCLBRR-z4z2FUmSzVnA5JwFDagK3p421UBhTRCGBT3boyo78YsjTmIZD1a7-9BB9dLoPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3ec7037002.mp4?token=EUTNmlXb5uQudmzXdd4XXwZfaREkaMZV3RQwsCF1diA6HW_gOO20yEgTydl0PbybF36L_ShvQC2D38k55054mdxvmOxLd36WdqIXE8nP5r1q5H6oTvL3ajHMa5rKlSsSduDni5mfWOFEQg1aw47x9DdHzat-oLKTVpUSnTHX6abayf2ojbuR34aaitwVzB5wB0YyxjZYmNQFuXOZQO3B78kUZ7R67kba6WOTIRbXwgjfBq27JDUcACPvr0qG39jUlwGqc16t6NaD6_Oy7zduzY5K009I5JwxOB6glDxEfgM0mZoKvwkiP16eWRqVZBLY564nSwfHAFXb8oieQ-Oqzw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3ec7037002.mp4?token=EUTNmlXb5uQudmzXdd4XXwZfaREkaMZV3RQwsCF1diA6HW_gOO20yEgTydl0PbybF36L_ShvQC2D38k55054mdxvmOxLd36WdqIXE8nP5r1q5H6oTvL3ajHMa5rKlSsSduDni5mfWOFEQg1aw47x9DdHzat-oLKTVpUSnTHX6abayf2ojbuR34aaitwVzB5wB0YyxjZYmNQFuXOZQO3B78kUZ7R67kba6WOTIRbXwgjfBq27JDUcACPvr0qG39jUlwGqc16t6NaD6_Oy7zduzY5K009I5JwxOB6glDxEfgM0mZoKvwkiP16eWRqVZBLY564nSwfHAFXb8oieQ-Oqzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا
گزارش
کرده است که یک نفتکش در حال عبور از تنگه هرمز مورد اصابت یک پرتابه ناشناس قرار گرفته است.
براساس این گزارش‌ها این نفتکش در حال خروج از تنگه هرمز بوده و «از ناحیه سمت چپ» مورد اصابت قرار گرفته است.
مرکز عملیات تجارت دریایی بریتانیا همچنین گفته این اصابت به کشتی آسیب رسانده، اما تمامی خدمه در سلامت کامل هستند و هیچ‌گونه پیامد زیست‌محیطی نیز گزارش نشده است.
@
VahidHeadline
خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از منابع خبری گزارش داد که یک کشتی در مسیر جنوبی تنگه هرمز بر اثر اصابت یک پرتابه دچار آتش‌سوزی شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78692" target="_blank">📅 18:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78691">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rra_4y1CPbQUitKo2I5USU8wIvgl8DPYxmWOvpJKdFwlP3wjAvpM_uNA7OIHhwzzxNnX73k2aTVKtOUvMqUZFvJSXgMYldPKhL84PXBwrln_uiYiWoNuPH8VhUqemW40YoUjyDIejdA4-bhhZBZambWyGWArmPzKw7IqlwJqX5mpl42tRqtKVxqjpTdiHmfCjBeWvBgdm3jbpKzYNaMZCGaqQwuyaw-xwgx8ON0vmMCGXcO9Skyu9FIY6yc1WF5p8PR642pD61pIqW9tcDlHWnXA5bnxs0QDZC12GlecxpNouxuApq0jKjgsME7GT8b41cv25f6LvZWw7LZrkpT6FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرزاد شهبازی، از وکلای متهمان پرونده «میدان علیخانی اصفهان» و وکیل علیرضا سپاهی، با رد روایت رسانه‌های حکومتی اعلام کرده است اتهام قتل ماموران انتظامی به هیچ‌یک از متهمان این پرونده تفهیم نشده و دادگاه نیز به این اتهام رسیدگی نکرده است. تاکنون پنج نفر از متهمان این پرونده اعدام شده‌اند و هفت نفر دیگر در خطر اعدام قرار دارند.
اظهارات این وکیل در واکنش به انتشار مصاحبه‌ای در رسانه‌های حکومتی مطرح شده است که در آن زنی، معرفی‌شده به‌عنوان همسر یکی از مأموران کشته‌شده، متهمان را به قتل و سوزاندن ماموران متهم می‌کند. انتشار این مصاحبه پس از افزایش انتقادها از اجرای احکام اعدام، به‌ویژه اعدام علیرضا سپاهی، صورت گرفته است.
شهبازی همچنین حضور این زن در محل اجرای اعدام‌ها را زیر سوال برده و پرسیده است وقتی موضوع پرونده قصاص و حق شخصی نبوده، بر چه مبنایی به او اجازه حضور در محل اجرای حکم داده شده است.
شهبازی روز شنبه ۱۸ مهر ۱۴۰۵ در پیامی در اینستاگرام نوشت: «به هیچ عنوان اتهام قتل برای هیچ‌یک از متهمان پرونده میدان علیخانی و میدان شهدا تفهیم نشده است.»
او تأکید کرد موضوع «سوزاندن ماموران در راستای قتل عمد» نه در دادگاه رسیدگی شده و نه از اتهام‌های مطرح‌شده در رای بوده است.
شهبازی علت ورود نکردن دادگاه انقلاب به موضوع قتل را نداشتن صلاحیت رسیدگی به این اتهام عنوان کرده است.
پرونده میدان علیخانی پس از کشته‌شدن چهار مامور یگان ویژه در جریان اعتراضات ۱۸ دی ۱۴۰۴ در اصفهان تشکیل شد. رسانه‌های حکومتی پیش‌تر ویدیوهایی از اعترافات متهمان در بازجویی‌ها، بازسازی صحنه و جلسات محاکمه در شعبه اول دادگاه انقلاب اصفهان منتشر کرده‌اند؛ اعترافاتی که نهادهای حقوق‌بشری آن‌ها را اجباری و فاقد اعتبار می‌دانند.
علیرضا سپاهی بامداد دوشنبه ۱۳ مهر اعدام شد. مای ساتو، گزارشگر ویژه سازمان ملل در امور حقوق بشر ایران، در واکنش به اجرای حکم، از نگرانی‌های جدی درباره شکنجه متهمان و رعایت‌نشدن دادرسی عادلانه در این پرونده خبر داده بود. به گفته ساتو، حکم در حالی اجرا شد که وکیل سپاهی همچنان برای رسیدگی دوباره به پرونده تلاش می‌کرد.
سپاهی پیش‌تر نیز در آستانه اعدام در ملأعام قرار گرفته بود، اما پس از حمله قلبی به بیمارستان منتقل شد. در همان شب، شهروندان برای جلوگیری از اجرای احکام تا سپیده‌دم در میدان علیخانی ماندند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78691" target="_blank">📅 16:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78690">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEo90YGyZUdzbnSg-1c5tgWyBlM-DZ_MF2FazYhadYD2IZ5-CvG5iKdXH3-oH-0ktGI9oZiW0dYjLlDY9HzUVc7GjC3WkF_igqk4tBgqPRobZk9GXLDcjvG1yjbja9prZ5NQxHKDTGnzlVTHx-0fva9lhvvO37Qn_fd7gTVexj4YVw7hO3kDcbd9xj8OwfSiN1g5FU9KXtzSm52k1AqZ6ecSfb6UozbaNA9gldbcX51f9SGDHFwBBAnFL5-TcAuq80XZT9NesH5YKf9_RNFk0aMozomtvquXSNMzv0avnIxccMPOyZJhIFn4yiMSr9LLG7s3Xoppf-AsdRwra1Tyyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان مدیریت بحران ایران اعلام کرد در سیلاب و رعد و برق پنج استان کشور هفت نفر جان باختند و دو نفر مفقود شدند.
به اعلام این سازمان، دو مفقود در استان گلستان ناپدید شده‌اند.
در شهرستان سوادکوه شمالی استان مازندران دو پل کاملاً از بین رفت. آب‌گرفتگی در معابر و خانه‌های این شهرستان گزارش شد و شماری خودرو در آب ماندند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78690" target="_blank">📅 16:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78689">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CnDfLkbfd_Yt58gts6j_rAd6rh1hgIl12gn-Xzs5uF-H97zfpBcDjW8MQcYGEQd83xd7XX1lpUV-QOaHFfyw29oKn_EJueOGtzTltNMB6VR-4-JBJUfN3KwDa0jPLkOouz_kj_fzy5ykM3ZBi8ii53J80eU376WtN506-iqkwfNRPYcGS6myAykS7sW98bJVXEE4EHid2OnN7h2Q23FqbIWX_SuAybkovia7qDRnUB5R2V16K4F8cfxeEGVUVhPIZlu4XASKLxyWUjkkSri7XsMO79wrTjzTcYxo-ya0x4b1vkBYev18GGKLy137WotjrcTcUw2Ue7y2IVWFh3GhPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی از اعدام یک مرد به اتهام قتل یک مامور نیروی انتظامی در بندرعباس خبر داد.
این مامور نیروی انتظامی رضا احترامی و مأمور یگان امداد شهرستان بندرعباس معرفی شده است.
متهم نیز پیش‌تر با نام «دانیال» معرفی شده و ادعا شده بود که این قتل چهار سال پیش هنگام درگیری با قاچاقچیان سوخت، بر اثر زیر گرفته شدن با خودرویی که مرد اعدام‌شده رانندگی آن را بر عهده داشت، روی داد.
شنبه نیز دستگاه قضایی جمهوری اسلامی از اعدام جابر خسروی، زندانی محکوم به قصاص در پرونده قتل یک مأمور انتظامی خبر داد.
این پرونده به حادثه‌ای در بیمارستان ولایت دامغان در ۱۱ شهریور ۱۴۰۱ بازمی‌گردد؛ حادثه‌ای که بنا بر ادعای مقام‌های قضایی، در جریان آن سلاح مأمور انتظامی گرفته شد و او بر اثر اصابت دو گلوله جان خود را از دست داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78689" target="_blank">📅 16:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78688">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fm5cJdcxi98e5Af__JfRAHZZZmJKLTGMlL6OReqxVmSnChvEB1wgYlJQ0Z6L7UxVzzGRyIcZWF7c2-ZP5mF4fBFffmx-p0zCKxGARiYZVJFDdcPEuESZXXibu1smlET-_NftOSgmqru8T2qHKZoz5y1OagRqL9fdlggHjYjqsmFtDgnkfDZI0mLw-RW3KLjHunz9kPssZvraAu11JUOSJ7eC126wWpUuTav1D2IkPCgZpT9q1lUfnFPFi6PC2xYgqZwUhjEoDGQuETW7JvFbp186Hn65NhzKkhk9zbb0jUz0qIwmMYfBr8-Mogqh9mqvH0LxdNEIXKLJ_5kBRy5Y1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان هواپیمایی کشوری عربستان سعودی در بیانیه‌ای گفت حمله روز شنبه ۱۸ مهر به فرودگاه بین‌المللی ملک خالد در ریاض، ۱۲ کشته و ۳۰۹ زخمی بر جای گذاشته است.
بر اساس این بیانیه که بامداد یکشنبه ۱۹ مهر صادر شد، چهار نفر از کشته‌شدگان شهروند عربستان سعودی و هشت نفر دیگر اتباع خارجی، شامل دو بنگلادشی، یک آمریکایی، یک مصری، یک اردنی، یک سوری، یک فلسطینی و یک سودانی هستند.
این سازمان همچنین اعلام کرد که شرایط سلامتی شماری از زخمی‌ها وخیم است.
به گفته سازمان هواپیمایی کشوری عربستان سعودی، تمامی مجروحان در چندین بیمارستان تحت مراقبت‌های پزشکی لازم قرار دارند.
در این بیانیه همچنین آمده است که حمله به فرودگاه بین‌المللی ملک خالد خسارات مالی و مادی نیز به همراه داشته و ارزیابی میزان این خسارات همچنان ادامه دارد.
حمله روز شنبه سومین حمله این هفته شورشیان حوثی مورد حمایت جمهوری اسلامی در یمن به فرودگاه بین‌المللی ریاض بود. شورشیان حوثی مسئولیت حمله را بر عهده گرفتند. حوثی‌ها همسو با تلاش‌های جمهوری اسلامی برای ناامن کردن تنگه هرمز، سعی کرده‌اند به کشتی‌ها در تنگه باب‌المندب که دریای سرخ را به خلیج عدن و اقیانوس هند متصل می‌کند و یک تنگه حیاتی به‌شمار می‌رود حمله کنند.
طبق گزارش‌ها روز شنبه، مسیر تمامی پروازها از ریاض تغییر داده شد و فعالیت‌های فرودگاه به‌طور موقت متوقف شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/78688" target="_blank">📅 03:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78687">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NuB11ziggNO939JNjxyHdn-IoVhQlD49Xlx8wKf8bqveyMHS1dzHkzk2yElduwwRCFM4NqpnyTklilyol-kne_d46QpVKtGvngRGY01HOZaiI8nHPK2G1GCk5Dft-zyUG1iuft0GN0RbMS9syjUQSEJSkrTLQfUvDIuE6rcR3jsTvgTm64y4iK6m1iNjEF1zmI54egXFimCpBzT88ETfo7H1Drz9qZdjfAHN29pBPrEQmusXR5qfflZIAtjMvySZ8NKUNjsSaovu60lj2P4h1qhScKdpzGFlJNsOWqCYKJ07CpkpM96oNh81SBpHFRGk6OysaPre2meH-Rs3NjWAlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
سازمان عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
ناخدای یک نفتکش که در حال خروج از تنگه هرمز بوده، گزارش داده است که یک پرتابه ناشناس به سمت چپ کشتی برخورد کرده و باعث آتش‌سوزی در آن شده است.
بر اساس گزارش‌ها، خدمه کشتی در سلامت هستند. در زمان انتشار این گزارش، میزان خسارات و پیامدهای زیست‌محیطی حادثه مشخص نیست.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78687" target="_blank">📅 01:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78686">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEn-GokBWVQAAJzDzxLyVCJghDyq7SkI0r8Ju4FVJlPaMthsHq_rGfbjL_uqjGYBORbAHLxRFHEp0j04Bru2RhHtOEJLj3MCDnwDq9GiOt-8MtxklPRd1wAZBVulXxfd4pnj5U60dN3SQq7cT2RJ3nCv0XoVKinuMv9awsx02XKNhQehonhp89jDrvmTyfEN5cL_XFXtIfW5ckG1LyXb_hjK9rQOxHLr1N-TSqg4xWNH0tGi0HQPbPIRLhgLwhnS8YmNDNBYgguz2hjp_NwPWiD0ufNpoC2opBN2I9eG3mdD-yD2ekLK7nHMNSpCSKC94wpInuBgFwctcrw9hqSB1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، روز شنبه، طی سخنرانی در ایالت تنسی درباره ایران گفت: «اوضاع تا حدی آرام شده است. آن‌ها احتمالا پیش از انتخابات دست به اقدامات اضافه‌ای می‌زنند و فکر می‌کنند این اقدامات به ما آسیب می‌زند، اما ما می‌توانیم این ماجرا را خیلی سریع تمام کنیم.» او در ادامه افزود: «آن‌ها اصلا نمی‌دانند من چقدر با آن‌ها خوب رفتار کرده‌ام. واقعا خبر ندارند که چقدر با آن‌ها مهربان و با مدارا بوده‌ام.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78686" target="_blank">📅 01:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78685">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dcdec5c24b.mp4?token=and8_xbv7UOwlOSl3NUVXo8evgnPxAqFYrSrLN0ePbMHBMaQICTu5kvEs6sNAAjUUk5AX4LWMjRVuCgqv2AW3-aBMs3L5Uo-j-aEVD74TtWnkP10DvohPPauQnOY2hxDfDxLgYuAZ0-ZRbUJZ3DOFMLkSIj9UNqpwJX5c795q0UKHAZEw8kKj0zuv31SZfDCrJKDyWqDEe7Kwy7k2fQcXD9-BjVwnF2L78sXx6n1R7kwLy-WuLlMJQlsFKews3JydR5NSU4HYW6HF9rb7xjA83o6oASoIUlpU707v_xEvcOAaeIbyoAP1ql-IWuYcC7aA25Z-sY7j90V8F4pZFYfoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dcdec5c24b.mp4?token=and8_xbv7UOwlOSl3NUVXo8evgnPxAqFYrSrLN0ePbMHBMaQICTu5kvEs6sNAAjUUk5AX4LWMjRVuCgqv2AW3-aBMs3L5Uo-j-aEVD74TtWnkP10DvohPPauQnOY2hxDfDxLgYuAZ0-ZRbUJZ3DOFMLkSIj9UNqpwJX5c795q0UKHAZEw8kKj0zuv31SZfDCrJKDyWqDEe7Kwy7k2fQcXD9-BjVwnF2L78sXx6n1R7kwLy-WuLlMJQlsFKews3JydR5NSU4HYW6HF9rb7xjA83o6oASoIUlpU707v_xEvcOAaeIbyoAP1ql-IWuYcC7aA25Z-sY7j90V8F4pZFYfoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان هواپیمایی کشوری عربستان سعودی روز شنبه ۱۸ مهر تأیید کرد که در پی حمله به فرودگاه بین‌المللی ملک خالد در ریاض و زخمی شدن شماری از افراد، فعالیت این فرودگاه متوقف شده است.
دونالد ترامپ، رئیس‌جمهور آمریکا، در واکنش گفته است که از این حمله مطلع شده و درباره آن تصمیم خواهد گرفت.
دونالد ترامپ در جمع خبرنگاران و در پاسخ به این سؤال که آیا آمریکا به جنگ عربستان سعودی با حوثی‌ها خواهد پیوست، گفت: «ممکن است. این موضوع را بررسی خواهیم کرد. ما تازه از حمله اخیر مطلع شده‌ایم. تصمیم‌گیری خواهیم کرد. خیلی سریع اقدام می‌کنیم.»
پیش‌تر برخی رسانه‌ها خبر داده بودند که حکومت ریاض از آمریکا خواسته حوثی‌ها را هدف حملات نظامی قرار دهد.
پایگاه خبری اکسیوس یک هفته پیش گزارش داد که شماری از بلندپایه‌ترین مقام‌های امنیت ملی دولت دونالد ترامپ روز جمعه در نشستی چندساعته و اعلام‌نشده در کمپ دیوید، درباره گام‌های بعدی آمریکا در جنگ ایران و همچنین درگیری عربستان سعودی با حوثی‌های یمن گفت‌وگو کرده‌اند.
با وجود تأیید رسمی وقوع حمله و زخمی شدن افراد، مقام‌های عربستان هنوز شمار دقیق مجروحان و میزان خسارت واردشده به فرودگاه را اعلام نکرده‌اند.
حوثی‌های مورد حمایت جمهوری اسلامی نیز تا زمان انتشار این گزارش مسئولیت حملهٔ روز شنبه را بر عهده نگرفته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78685" target="_blank">📅 22:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78684">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9492aa3856.mp4?token=Gr17IsbWNH6rcPQE1USr1DDK6ICow8ukrlp_wpnLTS4nDyKNqN6bYtofCA971ryWomMuNEdWdpWHKXU6WiRNj_MY2soHY5kPDhdiT9xx-2ED0I63XZAahh0oxfOgbUt1x4iGO59OeZx1ZNigeOzpRMQ70-tMKwplGJPxjeRp2O0SZsk0LHQN4Gk-vbWYO0aa0_bpeLj1fB3PhwlHSZibecQ55h3ntbVfE0gCdsvbM2JCiVGkazg8YBtL57vwkIlvYHc8p6PtZ8Et0HTjHFqmzhciq1tD16K2QHFXbuD5-ghRBN7uUP1rVs06X-96r4lMsL4w7AHIl6cbmVyaBWjezg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9492aa3856.mp4?token=Gr17IsbWNH6rcPQE1USr1DDK6ICow8ukrlp_wpnLTS4nDyKNqN6bYtofCA971ryWomMuNEdWdpWHKXU6WiRNj_MY2soHY5kPDhdiT9xx-2ED0I63XZAahh0oxfOgbUt1x4iGO59OeZx1ZNigeOzpRMQ70-tMKwplGJPxjeRp2O0SZsk0LHQN4Gk-vbWYO0aa0_bpeLj1fB3PhwlHSZibecQ55h3ntbVfE0gCdsvbM2JCiVGkazg8YBtL57vwkIlvYHc8p6PtZ8Et0HTjHFqmzhciq1tD16K2QHFXbuD5-ghRBN7uUP1rVs06X-96r4lMsL4w7AHIl6cbmVyaBWjezg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از هو شدن اسماعیل بقائی، سخنگوی وزارت امور خارجه جمهوری اسلامی، در جریان اجرای ارکسترال «آرش» در سالن اسپیناس تهران منتشر شده است.
این اتفاق شامگاه جمعه ۱۷ مهر، هنگامی رخ داد که بقائی برای سخنرانی پشت میکروفون قرار گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78684" target="_blank">📅 20:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78683">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/54a079f69b.mp4?token=F8zpl_-_GEWDXNaAHHuCzdSJt7G2AxvRmsW_5DgllJe8bGuul6PUtydAoF4eOjHeFpKl4HIWgXEu5F0zquUo6mit2WMpuEmIlkWkCY1miksQ_out42cF0uJps59qDuW0bvbbOWehVgxfMt_eR2utbHFnknidNrba-x2j3Cq4xp-CsqNhMkCAWuASOBCB0ylAV5Lykuiic5GNfvPdGpteviNd7pOknZUXIIQZtuGRmzxdLdO_4dEkWiH0Cnao4oBNQNjgVVbre1AJ2uL5P0HlfDvlK-1b0yySlrlShtj6Poe1CnvrXCh2nRmLBiEETDHDUGsNP0XCZs9Twohf1KGFUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/54a079f69b.mp4?token=F8zpl_-_GEWDXNaAHHuCzdSJt7G2AxvRmsW_5DgllJe8bGuul6PUtydAoF4eOjHeFpKl4HIWgXEu5F0zquUo6mit2WMpuEmIlkWkCY1miksQ_out42cF0uJps59qDuW0bvbbOWehVgxfMt_eR2utbHFnknidNrba-x2j3Cq4xp-CsqNhMkCAWuASOBCB0ylAV5Lykuiic5GNfvPdGpteviNd7pOknZUXIIQZtuGRmzxdLdO_4dEkWiH0Cnao4oBNQNjgVVbre1AJ2uL5P0HlfDvlK-1b0yySlrlShtj6Poe1CnvrXCh2nRmLBiEETDHDUGsNP0XCZs9Twohf1KGFUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان هواپیمایی کشوری عربستان سعودی روز شنبه ۱۸ مهر تأیید کرد که در پی حمله به فرودگاه بین‌المللی ملک خالد در ریاض و زخمی شدن شماری از افراد، فعالیت این فرودگاه متوقف شده است.
یک منبع دیپلماتیک به خبرگزاری فرانسه گفته است که حوثی‌های یمن حدود ساعت سه بعدازظهر به وقت محلی با موشک به این فرودگاه حمله کرده‌اند. بر اساس گزارش‌های اولیه، ده‌ها نفر در این حمله زخمی شده‌اند.
روزنامهٔ وال‌استریت جورنال نیز به نقل از مقام‌های سعودی گزارش داد که موشک‌های شلیک‌شده از سوی حوثی‌ها مستقیماً به ترمینال شمارهٔ سه فرودگاه اصابت کرده‌اند.
یک منبع بیمارستانی به خبرگزاری فرانسه گفته است که پنج نفر از مجروحان در بخش مراقبت‌های ویژه بستری شده‌اند. یکی از شاهدان عینی نیز گفته است هنگام حضور در گیت ۴۰۳ ترمینال پروازهای داخلی، شاهد اصابت موشک به محدودهٔ گیت ۴۰۱ و زخمی شدن مسافران بوده است.
این شاهد به خبرگزاری فرانسه گفت: «دیدم که گیت ۴۰۱ هدف قرار گرفت و افرادی جلوی چشمانم زخمی شدند. همه فرار می‌کردند.»
حملهٔ روز شنبه در حالی رخ داد که فرودگاه ریاض پیش‌تر نیز در روزهای چهارشنبه و پنج‌شنبه هدف حملات حوثی‌ها قرار گرفته بود. این حملات در مجموع چهار کشته و چندین زخمی بر جای گذاشت و به یک فروند هواپیمای مسافربری شرکت سعودی آسیب جدی وارد کرد.
سه شهروند سعودی، از جمله یک خلبان، در حملات روز پنج‌شنبه و یک شهروند سودانی در حملهٔ چهارشنبه کشته شدند. حوثی‌ها مسئولیت این حملات را پذیرفته‌اند.
تشدید حملات موشکی به عربستان در پی ازسرگیری درگیری‌های گسترده میان حوثی‌ها و نیروهای دولت مورد حمایت ریاض در یمن صورت گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/78683" target="_blank">📅 20:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78682">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFPccod7FrBKq3wyDQHmm5a16tJV5PdBbHzNI9_CTZn03IHGOKtooLlpP_gTYD9kpNd61GGXAnxmeWVz4qnZtTcoa7wA7sa_4N10THxPs-OlUDyqfYbEH3SFmiJipZ2nxZ_NZPvu5DCTauLgeW0vuG2ngIQnzcZAxbtLxzLngDYt77ymz3hFkJ4SMF2Ozx0uj4T8Qp2MsoG2u2OHlJi8QPgWIQU25zIepjA6F6tcbuD9xpiYJz0A3zz3UCDlUkbnGN5EfHs54_xSP7qE6kPD6BMzmxJAScpDO_Nay62CLNNUD4OKjBhOCHs63WBAO_t-q2w8O1IKQFU4a1xmgYBQLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ کرملین اعلام کرد ولادیمیر پوتین، رییس‌جمهور روسیه، با هماهنگی مسعود پزشکیان، دیدگاه تهران درباره راه‌حل احتمالی پایان جنگ با آمریکا را به دونالد ترامپ منتقل کرده است. هم‌زمان، مسکو از ادامه مذاکرات غیر مستقیم تهران و واشنگتن حمایت کرده و گفته پیشنهاد انتقال اورانیوم با غنای بالای ایران به روسیه همچنان روی میز است.
@
VahidHeadline
در همون انتقال به
توافق گازوئیل
رسیدند؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78682" target="_blank">📅 19:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78681">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WIbutOEmrJSrnA72kdBixDQC9cfpGriKvTmESEQ6IZRbBpVmftZAwAh2F68z8E4PpQMVbAAUXPk01Nv2U_cKo_DzFFsmuVDN9rErResrbwas4oEfumuCMB7DgNab6wgjc6TJ_-k98tWYEsyjNGmmtsi0LfphB4ws3Sjt6GVILt6v6eA_uwnhJi3CX6rOEJnnt6XV_7yHuzt2fB0LgPV6jnnxVrQNQt8Weyr3O9h2Q1t_hHAlGNCURenlxj3fXihCHsQpJyzaDdW_eV6YMXZqJw3XN1PzNJPQ6nZDe5j7sMW7-rTwPB65DyHwWWfCgzH3uAkyMKVIkuiPgOc6XjYwfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجموعه فعالان حقوق بشر در ایران در گزارشی به مناسبت روز جهانی مبارزه با مجازات اعدام اعلام کرد طی یک سال گذشته، دو هزار و سه نفر در ایران اعدام شدند که دست‌کم ۶۹ نفر از آنان با اتهام‌های سیاسی و امنیتی روبه‌رو بودند.
شمار اعدام‌ها در این دوره نسبت به دوره مشابه پیشین حدود ۲۹ درصد افزایش یافته و از هزار و ۵۵۳ نفر به دو هزار و سه نفر رسیده است؛ بالاترین رقم ثبت‌شده در ۱۰ دوره گزارش‌دهی.
بر اساس آمار این گزارش، شمار اعدام‌ها از ۵۰۵ نفر در دوره ۲۰۱۶–۲۰۱۷ به دو هزار و سه نفر در دوره ۲۰۲۵–۲۰۲۶ رسیده است.
در تفکیک اعدام‌ها بر اساس نوع اتهام، ۵۷٫۵۶ درصد مربوط به قتل و ۳۶٫۲۵ درصد مربوط به جرایم مواد مخدر بوده است. سایر اعدام‌ها با اتهام‌های سیاسی و امنیتی، تجاوز، محاربه غیرسیاسی، فساد فی‌الارض، جرایم اقتصادی یا اتهام‌های نامشخص ثبت شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78681" target="_blank">📅 19:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78680">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6008e28bbf.mp4?token=Eaes5ibXiWPDUCp52qS_6ABbnCiNCwZGEIFOF8A8lkT63wofEvKAzm4J40f6FXqKWKGaVJl2GOaj5kVELCvNhG1AYmcXnKq87Eg5iM0pNViOUeCRGzCdMYY-LMdPUhkwBj3mrAKchSZj-SVhPFfJy545_i8AacO4YUb3Qop3WKUh-C8BwXidIyP_F-bTmjrKMghi1hFiOHZww9iwlFWMSbbWNyXZmHmH6HwESE3rgqPeyr_kabOImX7Oba7VnM5gj3gS3sngJXbrr4zAKgJbRjdYD8rd1VjpejhSR2zpMnSp6vMpFESqKZbiefdo0SFaWCxK_F2jJOkBUV4i6G3Kfg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6008e28bbf.mp4?token=Eaes5ibXiWPDUCp52qS_6ABbnCiNCwZGEIFOF8A8lkT63wofEvKAzm4J40f6FXqKWKGaVJl2GOaj5kVELCvNhG1AYmcXnKq87Eg5iM0pNViOUeCRGzCdMYY-LMdPUhkwBj3mrAKchSZj-SVhPFfJy545_i8AacO4YUb3Qop3WKUh-C8BwXidIyP_F-bTmjrKMghi1hFiOHZww9iwlFWMSbbWNyXZmHmH6HwESE3rgqPeyr_kabOImX7Oba7VnM5gj3gS3sngJXbrr4zAKgJbRjdYD8rd1VjpejhSR2zpMnSp6vMpFESqKZbiefdo0SFaWCxK_F2jJOkBUV4i6G3Kfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، طی سخنرانی در ایالت نیویورک اعلام کرد: «مسئله ایران به هر ترتیبی که شده، خیلی زود حل خواهد شد. یا آن‌ها همه‌چیز را به ما می‌دهند، یا دیگر اصلا وجود نخواهند داشت. خودشان هم این را به خوبی می‌دانند.»
او همچنین با اشاره به بحران اقتصادی عمیق در ایران و تسلط نظامی ایالات متحده بر منطقه تاکید کرد:
«ایران در ورطه بزرگی گرفتار شده، از تورم ۳۰۰ درصدی رنج می‌برد و هیچ پولی ندارد، تا جایی که ارتش و نیروهای پلیس آن حقوق دریافت نمی‌کنند. ایران هرگز به سلاح هسته‌ای دست نخواهد یافت و ممانعت از دستیابی آن‌ها به این سلاح دلیلی بود که ما را وادار به رفتن به آنجا کرد.»
ترامپ در ادامه افزود: «به لطف ارتش ایالات متحده اکنون کنترل کامل تنگه هرمز را در دست داریم و امروز حجم نفتی که از این تنگه عبور می‌کند حتی از دوران پیش از جنگ هم بیشتر است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/78680" target="_blank">📅 07:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78679">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIlcP7VapFIwA7Uy2JE-OLD1MPtIuCzDOgu_5z2uYtYoK2VmGwXeplM9mf3dBIliFqG6Ifg1Tq60C_JSJG9j8Ol_h5Zbq6diChAXEQPhVmAr8s7xdAWe3E8MdTRSB1C5z3Z1izKOG8X59-692wDvFa41CKiH5mGtZrg80n-byAwGIoQx7hS95TXM4hE6mnagZvPQ7M8ec8_yn_XQHS7JyLGY-rEX_8TomELP3k52onKb_jVkx1Nk_mQLqGHpOfYu38p-Kh3-2kFMzm3nmnM2ZbdOKITk7nwprROUPmHI1kDEOdF_12Zhi3bSAkeSYSpcS8BE9o3LCcMTN7b5a8-5LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در شبکه اجتماعی تروث سوشال اعلام کرد کنترل کامل آمریکا بر تنگه هرمز، همراه با توافق تازه واشینگتن و مسکو برای عرضه میلیون‌ها تن گازوئیل روسیه به بازار جهانی، باعث کاهش سریع و چشمگیر قیمت این سوخت خواهد شد.
ترامپ گفت پس از گفت‌وگو با ولادیمیر پوتین، رییس‌جمهوری روسیه، توافق شده است که مسکو بلافاصله بیش از ۳۰۰ هزار تن گازوئیل به بازار آمریکا و جهان عرضه کند و ۵۰۰ هزار تن دیگر نیز در ماه نوامبر تحویل دهد.
به گفته او، روسیه پس از آن یک میلیون تن گازوئیل دیگر به بازار عرضه خواهد کرد و با توجه به وضعیت پالایشگاه‌های این کشور، سه میلیون تن دیگر نیز در مدت کوتاهی تحویل خواهد داد.
رییس‌جمهوری آمریکا گفت کنترل کامل تنگه هرمز از سوی واشینگتن و افزایش عرضه گازوئیل روسیه، قیمت این سوخت را برای مصرف‌کنندگان آمریکایی و دیگر کشورهای جهان به‌سرعت کاهش خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/78679" target="_blank">📅 22:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78677">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/97e3d7ab08.mov?token=SIM7uDmMTOd8SiJ8-SzhdyB4LM467jfbXXuDI5z-31tlllxvECx9f5nTIxxianlhgeuIckHi1Y8ohyOG4tRHjFHBM6znOEBCVsobfsVOZzpB0RTVcoCCckpxugyM0ijmNOXM1djfZMkKiYHFGpXWIVE6VlH12FShlKHqLpbQecoacEyz67Y4q5Y66fpxdYAjM-cIbh7qeSqZhVPntyA4KxZRqBTyHImdwP8j0VrZYvbQOUBfuT-Z7MBd7HenGvnJRxmFLY1R4Xi2v-3EP1nbBmLeAYtnvJBwa1GRO2EMvFK64uymQ6Aa3H1pr3Fw8WD38olAcGsC5hhYE2rZmF_xgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/97e3d7ab08.mov?token=SIM7uDmMTOd8SiJ8-SzhdyB4LM467jfbXXuDI5z-31tlllxvECx9f5nTIxxianlhgeuIckHi1Y8ohyOG4tRHjFHBM6znOEBCVsobfsVOZzpB0RTVcoCCckpxugyM0ijmNOXM1djfZMkKiYHFGpXWIVE6VlH12FShlKHqLpbQecoacEyz67Y4q5Y66fpxdYAjM-cIbh7qeSqZhVPntyA4KxZRqBTyHImdwP8j0VrZYvbQOUBfuT-Z7MBd7HenGvnJRxmFLY1R4Xi2v-3EP1nbBmLeAYtnvJBwa1GRO2EMvFK64uymQ6Aa3H1pr3Fw8WD38olAcGsC5hhYE2rZmF_xgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی درباره صداهایی که نمی‌دونم این بار هم آتش‌بازی بوده یا چی:
سلام وحید جان شرق تهران صدای پدافند و انفجار ممتد
صدای یک انفجار و بعد چندتا پدافند شرق تهران
وحید تهرانپارس صدای انفجار شدید بعد ضد هوایی الان ساعت ۸/۳۰
صدای شبیه پدافند یا تیراندازی در تهرانپارس شرق تهران
سلام وحید جان خوبی
پدافند تهرانپارس 5 مین  کار کرد ساعت  ۸:۳۰ دقیقه شب
وحید جان شرق تهران صدای تیر اندازی اومد الان
دود هم دیده میشه تو اسمون.
آپدیت:
دو ساعت بعد دوباره شرق تهران:
صدایی شبیه به تیراندازی در محله مجیدیه
ساعت ۱۰:۴۰ دقیقه ۱۷ مهر
چند دقیقه بعد: دوباره اومد این سری انگار رگبار بود
سلام ساعت ۲۲:۴۷ صدای تیراندازی چندین بار. مجیدیه شمالی‌
چند دقیقه بعد: الان هم دوباره اومد
صدای پدافند شرق تهران
سلام وحید جان
صدای پدافند همچنان پست سر هم
مجیدیه
صدای پدافند
مجیدیه
سمت مجیدیه تهران صدای تیر اندازی و پدافند میاد
صدای پدافند میاد
دولت کلاهدوز
سلام وحيدجان سمت اختياريه صداي پدافند مياد ساعت٢٢:٥٧
صدا پدافند سمت پاسداران
چند بار شلیک ساعت ۲۲:۵۷
سلام صدای تیر اندازی شمال شرق تهران ۱ دقیقه ممتد اومد الان قطع شده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 442K · <a href="https://t.me/VahidOnline/78677" target="_blank">📅 20:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78675">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lpcnnRggxYlC6DnPgALJYM8dnUPtOHuf5BRU0MLZFihCPUWqsGVMYLr1E6QOBzYDWhGcYR844aTyOXfKQUTRltO3vF4gUFo1pOXzmeAUKPSWW_tCWUPZK4CKNv4VOG-jUu5S_XqUrkFkKx1DI-FM1l6oVgIVV6-nHE1cqmtEU5IqpJhPvE8O4AyBMpzcH5hqERg_WtDShS8zRiB8-5DZdkGocSsUeGAZQCl86EvnTSqeRdY3cI_W7kbOYlZX6IIET9jLic1_4ObXnP8krsoj9STTWULTncHiRvTOB_2XrndZ87tyOZTNXvOM5yryziLtQfkW7JHKRPEdNeSLTJSSUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f20c8d9bec.mp4?token=CmXSnrMvtUSDaUoXhyoYix-A3IK3NWYGLfI6GrC1Cyzsm2IpHu8NOH6km_XQfFqdHCzm7KnF8DGzroztesrBt97U2nUSbZSsb0io9nm1W-tnoZvD5GePEN8M7zmYvHdDtnj8WZ9wueoRO6cQcdMFmzBTgB4yz9uChiWRa9o0uFI9V4Ho3RnIcNnhJV2yuPZX8709NrUQmTR4NPUPBfo9jbDt3reKzryuvAdF67zwNXkQn3y8JSFiE6wxRHQna0iyOd0mLdDazZU7mFqc_s0sPswWTJO4wNKuFlX6ECyB1gtlKsc3ih9RpkCHgK5Cs9J0B_XJ0upesf46PpRYRqGJ-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f20c8d9bec.mp4?token=CmXSnrMvtUSDaUoXhyoYix-A3IK3NWYGLfI6GrC1Cyzsm2IpHu8NOH6km_XQfFqdHCzm7KnF8DGzroztesrBt97U2nUSbZSsb0io9nm1W-tnoZvD5GePEN8M7zmYvHdDtnj8WZ9wueoRO6cQcdMFmzBTgB4yz9uChiWRa9o0uFI9V4Ho3RnIcNnhJV2yuPZX8709NrUQmTR4NPUPBfo9jbDt3reKzryuvAdF67zwNXkQn3y8JSFiE6wxRHQna0iyOd0mLdDazZU7mFqc_s0sPswWTJO4wNKuFlX6ECyB1gtlKsc3ih9RpkCHgK5Cs9J0B_XJ0upesf46PpRYRqGJ-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، گفت اگر حکومت ایران به سلاح هسته‌ای دست می‌یافت، ممکن بود پس از حمله به اسرائیل و دیگر نقاط خاورمیانه، کشورهای اروپایی و شهرهایی مانند لس‌آنجلس و سن‌دیگو در آمریکا را نیز هدف قرار دهد.
ترامپ جمعه ۱۷ مهر در مراسم روز کلمبوس در کاخ سفید گفت جمهوری اسلامی پیش از حمله بمب‌افکن‌های بی‌۲ آمریکا، تنها دو تا سه هفته تا دستیابی به سلاح هسته‌ای فاصله داشت.
او گفت در صورت دستیابی جمهوری اسلامی به این سلاح، حکومت ایران به‌سرعت از آن استفاده می‌کرد و ابتدا اسرائیل و سپس دیگر نقاط خاورمیانه را هدف قرار می‌داد.
رییس‌جمهوری آمریکا افزود کشورهای اروپایی احتمالا پیش از آمریکا در معرض چنین حمله‌ای قرار می‌گرفتند و شهرهای لس‌آنجلس و سن‌دیگو نیز می‌توانستند از اهداف احتمالی باشند.
ترامپ گفت: «دیگر لازم نیست نگران این موضوع باشیم. آن‌ها به سلاح هسته‌ای دست نخواهند یافت.»
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه ۱۷ مهرماه در مراسم روز کریستف کلمب در کاخ سفید، با اشاره به درگیری‌های نظامی با جمهوری اسلامی گفت که این وضعیت به‌زودی پایان می‌یابد و قیمت سوخت نیز به‌شدت کاهش خواهد یافت.
ترامپ در سخنانش با اشاره به عملیات نظامی آمریکا علیه ایران گفت: «ما مانع دستیابی ایران به سلاح هسته‌ای شدیم.» او افزود که پایان درگیری‌ها از راه‌های مختلف امکان‌پذیر است و تاکید کرد: «به هر شکلی، این وضعیت خیلی زود پایان خواهد یافت.»
رئیس‌جمهوری آمریکا همچنین درباره توان نظامی جمهوری اسلامی گفت: «آن‌ها نه نیروی نظامی دارند، نه نیروی دریایی، نه نیروی هوایی و نه تجهیزات پدافند هوایی.» او در ادامه با اشاره به محاصره دریایی اعلام کرد که آمریکا مسیر عبور کشتی‌ها را مسدود کرده است.
این اظهارات در شرایطی مطرح می‌شود که واشینگتن هم‌زمان با ادامه فشارهای اقتصادی علیه جمهوری اسلامی، محدودیت‌های دریایی و تحریم‌های مرتبط با صادرات نفت ایران را دنبال می‌کند. تنگه هرمز نیز به یکی از محورهای اصلی تنش‌های نظامی و اقتصادی میان دو کشور تبدیل شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/78675" target="_blank">📅 20:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78674">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QexDVnbm0tbHmY-43c7Sn56EAT05ZAeRj_BaWNxJzOuI9MPvMGRnp82C9jEdlsgBdiohv0Tj4Ejrx8e93tSRel3uv8aTt35bh-PRFuBhJFZ-SnWqZqOerXCAISasaXrG9QmwBbGrVqdlpN3ktvh0-peTBs9yZ8NzuEgRsZKNH9Hs7_NZC0OEgFHN_rI-cY081V_jeTHeGqO4mv1ZqipeqxjjjaqrWrRO-8aQ-bDQExaszesH03v5ZCECrrELPBYN8wiA1P2RuGmlrwbT5_6KMHSTIqXJI1mYTU6KLJ769dhYF_xi5YUqMSBT7iyrapOAhfJpkhW1c6UKBAwWA2RQUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری صداوسیما با انتشار گزارشی اولیه، از انفجار بمب کنار جاده‌ای در مسیر یکی از خودروهای انتظامی استان سیستان‌ و بلوچستان خبر داد و نوشت در این حادثه نصرت افتخاری، معاون اجتماعی انتظامی استان سیستان و بلوچستان، در منطقه چشمه زیارت زاهدان کشته شد.
این منبع نوشت عامل اصلی بمب‌گذاری هنگام فرار کشته شد.
خبرگزاری فارس، رسانه وابسته به سپاه پاسداران نیز گزارش داد این حادثه در مسیر حرکت یک دستگاه خودروی پلیس در چشمه زیارت زاهدان رخ داده و چند نیروی پلیس در جریان آن دچار جراحت شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/78674" target="_blank">📅 18:18 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78673">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BlNZCr7ItBx239vSm00YNNwGkvCQaGkhv7diKlr1qvcsR0xVUU0h-YrrR4nRE_E1D_njvyyh2kzV4m48vUS2WQuxb9Uoujz_z9Dp68d39kWQuaP1K8piOUFQxnOBVwnmbyOL5gKsa4mzEvseLcxHknFy5ytHfWU79DEbaGmaoTGAEhVcXbY2K3sDAeItRYuIL1dyQ6yjc5AyJ2-1QMQl6T5qNkND03mdFmL7sYiN1olheDGV8Fi7di9gNGoN1J01EGSvVZbnf8MCD1JeVLqRP59Xv8dQ4_706OWK6oMezdt1nKDWlenSp5yMU8p7u_5bMFf7uvryZXk2Had4fqaY8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران،  اعلام کرد یک کشتی حامل گاز مایع به‌نام «ان‌وی سان‌شاین»، متعلق به شرکت نات‌ویت را هنگام عبور از جنوب تنگه هرمز هدف قرار داده است.
سپاه پاسداران اعلام کرد این کشتی در حال عبور از مسیری «غیرقانونی» بود و پس از اصابت، موتورخانه و سامانه رانش آن دچار آتش‌سوزی گسترده شد.
نیروی دریایی سپاه همچنین اعلام کرد کنترل تنگه هرمز را در اختیار دارد و اجازه حضور نیروهای نظامی آمریکا در این منطقه را نخواهد داد.
سپاه پاسداران در این بیانیه اعلام کرد شرکت‌های کشتیرانی که با آمریکا همکاری کنند، با تحریم و اقدامات تنبیهی علیه شناورهای خود روبه‌رو خواهند شد.
بر اساس این بیانیه، سپاه از این پس برخورد با شناورهایی را که از مسیرهای غیرمجاز عبور کنند، به تنگه هرمز محدود نخواهد کرد و این کشتی‌ها را در سراسر منطقه هدف اقدامات تنبیهی قرار خواهد داد.
@
VahidOOnLine
سازمان عملیات تجارت دریایی بریتانیا (UKMTO)، روز جمعه ۱۷ مهر، با انتشار هشدار جدیدی اعلام کرد که حادثه‌ای در ۱۳ مایل دریایی غرب راس‌الخیمه در امارات متحده عربی رخ داده است.
بر اساس گزارش‌های دریافتی از منابع مختلف، این شناور مورد اصابت یک پرتابه ناشناس قرار گرفته که منجر به بروز حریق شده است؛ آتش‌سوزی مذکور تاکنون مهار و خاموش شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78673" target="_blank">📅 16:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78672">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c25vDYzC5YCJX4RytJeHFV9UgU05tblPqa7-WXMcfsdEghfLGpiqitCavssB8ZqmSLM3S1HPJwTqK9nC61aQjx77DbeUwVadSiBBKKpsbitE8kcsrXBgKGpO3FiZ5uHnhL6DcPWiGjyAPsW28XmlBymwiOCYQd-abOKAgxIE6k6KXQA7xJ60NMCh4FOGRdWgVyRndHe_VZ56hKCYd6q2ZrrVl2GZFV-Gdc44IWFgnShkltqkmHnVPDPQk7RxgaIpbJfl7oQ3cJ848pMVhCU5Gf9MvQiUt2_FKHk1BUAqM3GRu3Knq5kyfiPhpM7PPKOs2h52eSYkDuhzGCO3_VM7eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه‌های نیویورک‌تایمز و وال‌استریت ژورنال در گزارش‌هایی از بررسی گزینه‌های تازهٔ حمله به ایران در دولت آمریکا و تقویت حضور نظامی این کشور در خاورمیانه خبر داده‌اند.
این گزارش‌ها در حالی منتشر شده‌اند که دونالد ترامپ، رئیس‌جمهور آمریکا، روز پنج‌شنبه ۱۶ مهر اعلام کرد ایالات متحده پیش از انتخابات میان‌دوره‌ای سوم نوامبر به ایران حمله نخواهد کرد.
نیویورک‌تایمز به نقل از مقام‌های آمریکایی گزارش داده است که ارتش ایالات متحده در حال تدارک گزینه‌هایی برای ازسرگیری عملیات رزمی گسترده علیه ایران است و پنتاگون به دستور آقای ترامپ طرح‌هایی را برای حمله به زرادخانه‌های پهپادی و موشکی، تأسیسات انرژی و دیگر مراکز نظامی ایران تدوین کرده است.
به گفتهٔ مقام‌هایی که با این روزنامه گفت‌وگو کرده‌اند، تیم امنیت ملی رئیس‌جمهور آمریکا و پنتاگون در ماه‌های اخیر پنج پیشنهاد برای انجام عملیات‌های بزرگ علیه ایران یا حوثی‌های یمن به او ارائه کرده‌اند، اما آقای ترامپ هر بار این طرح‌ها را رد کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/78672" target="_blank">📅 16:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78671">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfEwebRbBz8qnzz45AlAje4ob__emZV-bcyb4ZAxsrG8a3MAHXSR1orO3tg2qXVqdUe1S7WLrVvo1Tp-eiHnRC4Q6haN1bOSg0rOyRcCMEPG1BxbR355_J_5HX7-2M3SuZr8745Fzv3dtXsr9iy9CzzPJdDHp3BJYfJXJBmRcqIPUbMgW3_ArIUf4j7yRVJfq8RtjSkgWVO1vC9PKRAeAQLmtLi9E7ZcGqJRPErl8Zi8G07VXlfvx96ajKb_tglI_GMC2cXAs_7WbvT6_WFOTOpclci4GFl8vU4f_koHjYOnl1JzIkZIzQeTvsv0QMbBjxFiTmap0uXGbTVdDe6u8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت اوپن‌ای‌آی اعلام کرد حساب‌های کاربری مرتبط با یک عملیات نفوذ رسانه‌ای با منشأ ایران را مسدود کرده است؛ عملیاتی که در آن، گردانندگان با استفاده از چت‌جی‌پی‌تی و هویت‌های جعلی روزنامه‌نگاری، نزدیک به ۱۰۰ مقاله درباره جنگ ایران و آمریکا را در حدود ۱۲ رسانه اینترنتی در کشورهای مختلف منتشر یا بازنشر کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/78671" target="_blank">📅 16:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78670">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SV1U4TpeZzaUJlLRYRzFQWIcJ8oxEDC2eEnPf0aMe6ml_qPzpafqakto_oeBdbrMPdVzcaAYXUIQIW_DrfqzDWaF39Kte46IXlKHrXLVblqsrDpUq-bBzqYlnyOWtfZQKvzlGyZfXwerB1g3I4ONqCSnXvYpKi2Vve-Bh0guvXvhKsfB2CFyhbVU5ZaFE1L37o32YFwHbz6onWPfh0IoUbU5ZewWEvpE4s6NR376VihTh3TfLh_xE7UqDTMfQWf5DPVZrt1pAsjToGl8VBVs7YeRbPudFPVbRdaFtqKSwWumO_diH1DnNRrukFbCSUfg-MewA0lvCw7wpD6yMSL5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، اعلام کرد واشینگتن احتمالا تا پایان هفته حدود یک میلیارد دلار دارایی رمزارزی مرتبط با جمهوری اسلامی را مصادره خواهد کرد.
بسنت گفت دولت دونالد ترامپ کارزار «فشار حداکثری» علیه جمهوری اسلامی را به کارزار «انزوای کامل» تبدیل کرده است.
به گفته او، این سیاست علاوه بر محدودیت‌های مالی، مسیرهای دریایی، هوایی و زمینی ارتباط ایران با خارج از کشور را نیز در بر می‌گیرد.
وزیر خزانه‌داری آمریکا گفت امارات متحده عربی و عمان در اجرای این سیاست با واشینگتن همکاری می‌کنند و دولت آمریکا در حال رایزنی با پاکستان و ترکیه برای بستن مسیرهای زمینی ورود و خروج از ایران است.
@
VahidOOnLine
اسکات بسنت، وزیر خزانه‌داری آمریکا، با انتقاد از سفرهای خارجی مقام‌های جمهوری اسلامی گفت اعضای سپاه پاسداران دیگر نمی‌توانند برای دیدن «جراح پلاستیک خود در لندن، معشوقه‌هایشان در پاریس و پول‌هایشان در ژنو» به خارج از ایران سفر کنند.
بسنت در ادامه گفت: «اگر جمهوری اسلامی را دوست دارند، حالا همان‌جا گیر افتاده‌اند و می‌توانند از آن لذت ببرند.»
وزیر خزانه‌داری آمریکا گفت سیاست دولت دونالد ترامپ برای منزوی کردن جمهوری اسلامی، فراتر از تحریم‌های مالی است و محدود کردن سفر مقام‌های حکومتی به خارج از کشور نیز بخشی از این برنامه به شمار می‌رود.
او همچنین با استناد به گزارش اخیر نیویورک‌تایمز گفت اقدامات دولت آمریکا باعث ایجاد نگرانی و آشفتگی در میان اعضای سپاه پاسداران شده است.
بسنت افزود اقداماتی که واشینگتن علیه جمهوری اسلامی انجام داده، پیش از این سابقه نداشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/78670" target="_blank">📅 16:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78669">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a954e7da9.mp4?token=aDz3hlC2sLsncefou8CZsUqRwJAOXxVwI0RI_7MGxjwkHT4QEc2-McK4uzxW0qgxmmBpPnc47l7a1BcsFY4Hey9cgC_o8Ub_aKcUSYfiJxqhOBQcYoBb2TMPr0SD1lXMiMQdFfPyjhZIcYu0tKpk_BLARDdqLlOjyqmLIruO3VVk1L54xNi3JAovgv_kcN_Un7jbC-UtyhzqE3AhVp-d4Xtl66Jifd6NbWEbVaypel_pGZ76Sq-xEtQzPXA0f7HzUgp9Lg8a1Lk1lvuirB_pgPuO-UArOZCeOcpktAXNOnF3tz12cANEon-cgCaSl2QIkrKSt5sW9Sl70Dr_RL1VmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a954e7da9.mp4?token=aDz3hlC2sLsncefou8CZsUqRwJAOXxVwI0RI_7MGxjwkHT4QEc2-McK4uzxW0qgxmmBpPnc47l7a1BcsFY4Hey9cgC_o8Ub_aKcUSYfiJxqhOBQcYoBb2TMPr0SD1lXMiMQdFfPyjhZIcYu0tKpk_BLARDdqLlOjyqmLIruO3VVk1L54xNi3JAovgv_kcN_Un7jbC-UtyhzqE3AhVp-d4Xtl66Jifd6NbWEbVaypel_pGZ76Sq-xEtQzPXA0f7HzUgp9Lg8a1Lk1lvuirB_pgPuO-UArOZCeOcpktAXNOnF3tz12cANEon-cgCaSl2QIkrKSt5sW9Sl70Dr_RL1VmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان روز پنج‌شنبه ۸ اکتبر (۱۶ مهر)، با ولادیمیر پوتین، رئیس‌جمهور روسیه، دیدار و گفت‌وگو کرد.
این دیدار در ترکمنستان و در حاشیه دو نشست «کشورهای ساحلی دریای خزر» و «سران کشورهای مستقل مشترک‌المنافع» صورت گرفت.
پوتین در این دیدار خطاب به پزشکیان گفت «ما می‌دانیم که ایران تلاش‌های واقعی برای پایان دادن به این درگیری انجام می‌دهد؛ درگیری‌ای که ایران در آغاز آن هیچ تقصیری ندارد.»
پزشکیان هم در این دیدار به پوتین گفت «هر بار که [با آمریکا] گفت‌وگو می‌کنیم، دوباره حمله می‌کنند، ولی ما از میز مذاکره و گفت‌وگو کنار نخواهیم کشید.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78669" target="_blank">📅 16:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78667">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C9QHpY0z1d3Md8R3KXye7GlGvqT58TpjLEj6sY-YsC5kXlF163DbIF_YO7kvyfjx4KbNzIqf5XfGv4eTaEK7hbLqjeaYnbysBLtFsszIHDAty_eDIegyGi1kM1z6aNwwsrUjzyKids_u_iho6CIfo7Wg9KYSlfXT7I_GL50QJhBxudOAUN3Fx06DpJVhgc2d99jrfj3J5P2ppsQhJo7GAS9pzUa8glYT2_tuNhMlZAC_kKl074H8K6mVZbGqDOTipA1gXyzxL3VxKkDrdj_b99akTGGScVgEMhxntLXZiDHQBtkqYJsxMZxOzaKGvfAqnE5LgDEnAHCDYHocYSnRcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZEYbRrC3R9sfBWUv-Xs3EJoUL8g2bc2XTaDhQaRCcQktUws4_ifZxaWOYVq0j2mV-ku1H-0eFcSstGoFX7sdU4rQZp-OKoS3JawqpQpZR4Su2-fVN8nNbUOO8cbAIcObUKrDsf_G6hZRuTa56CeE76JRuszI8Ss2Pyk9KQouYbZ2fkYlh6j6ml3GmyClxACBvdU6RZs8DkK_ewqbsAyN3BFeU0j8egWq23HEmaYF9MESZpjoCmfysT0Zw4k_e9lUdoli94WTUuGlFp3ZSlPCf0hy5RhDNk-wrOb0z3zFpr6RasvIfMk-oImd2CfYBdzC2-9SPR56fkzb7k7PCUiR-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان هواپیمایی کشوری عربستان سعودی در بیانیه‌ای جمعه ۱۷ مهر اعلام کرد که در پی دو حمله به فرودگاه بین‌المللی ملک خالد ریاض در روز پنجشنبه، سه شهروند این کشور کشته و شماری از شهروندان سعودی و اتباع خارجی زخمی شدند.
بر اساس این گزارش، در حمله نخست، تاسیسات فرودگاه و در حمله دوم، یکی از هواپیماهای شرکت هواپیمایی سعودی هدف قرار گرفت.
این سازمان اعلام کرد پس از این دو حمله، فعالیت فرودگاه از سر گرفته شد و تردد پروازها به حالت عادی بازگشت.
شرکت هواپیمایی سعودی نیز اعلام کرد که یکی از کارکنان این شرکت در میان کشته‌شدگان بوده و یکی از هواپیماهای آن هنگام توقف روی زمین در فرودگاه آسیب دیده است.
سازمان هواپیمایی کشوری عربستان سعودی همچنین اعلام کرد که فعالیت‌های عملیاتی فرودگاه بین‌المللی ملک خالد از سر گرفته شده و تردد هوایی در این فرودگاه به حالت عادی بازگشته است.
@
VahidOOnLine
شرکت هواپیمایی سعودی (السعودیه) اعلام کرد کاپیتان حمود علی الکثامی، خلبان این شرکت، روز پنجشنبه ۱۶ مهر ماه در حادثه فرودگاه بین‌المللی ملک خالد در ریاض جان خود را از دست داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/78667" target="_blank">📅 16:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78666">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxcX6LVmLxW5Lnt6U-E_74kVGPaIsYtoM-ptImAl8xrvILpWjHzoENRzlrsNWDtKEE4T6RYRkcpVJ8KxSNvZOourjNDzVFEpg-DKdgHMt5uBn4RtgxYlrGf1FlX-eSNw9f_WgcU0tAeWxrAI6oGYq3pR0Vg0TunBA6dzXe1VO_MSMog_8Sdcv6f-B5QZEQrB16chV5ML0NdGlNvn4u_cBKGwnad4KWL55_C_zIUXZGbl95tzLrEyFbRDeP8CHCegsMi7bIs25R4bFCLGCZfbF2fPh286w2i1byIVRgqmxcRIfh-1rXCAjovj4VSZFzcl9IefI24NCYUSZljhSFmMSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های جمهوری اسلامی از کشته شدن رئیس پلیس پیشگیری شهرستان فاریاب در استان کرمان بر اثر تیراندازی افراد مسلح خبر دادند. این حادثه در حالی رخ داده که طی دو روز گذشته چندین حمله مسلحانه دیگر علیه نیروهای نظامی و انتظامی جمهوری اسلامی در مناطق جنوب شرقی ایران گزارش شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78666" target="_blank">📅 16:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78665">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ruqGDexrzYek7hcbY6Hm8kewHou97pA197pi44_mPuHb-wbw6EfiNO_VZCqKRmbgqRkYNrWogSZdoUuLstY30J5tR_pNsSm_EPjyvpfZxYveuTJaj7CgQPNgz5iM3HsBwtrAPq2EvcFN7CNuIDKdxKfzp4vfAjBRBKj0X0_xZV4IJCJngNiVfdgMSunGZ2x8On_ySRHPjGbEM7jwfFokceQA8kVNghgqUKyRpfyud048BGioqW8Za0wHJX0M1sR2rQEV4pZW-rrdryKczk2IB96mtShObmNzV_T94QFcJpW6LkIxen5_kTRdd3seeDgfbp0GxLA61xZXF1sRtbYyyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترانه و رومینا رحیمی، دو خواهر بازداشت‌شده در جریان اعتراضات دی‌ماه ۱۴۰۴ و از متهمان پرونده موسوم به «میدان شهدای اصفهان»، در زندان دولت‌آباد این شهر به سر می‌برند.
ترانه رحیمی در مرحله بدوی به اعدام و ۱۱ سال حبس و رومینا رحیمی به ۳۶ سال حبس محکوم شده‌اند. وکلای آنان به این احکام در دیوان عالی کشور اعتراض کرده‌اند.
#ترانه_رحیمی
#رومینا_رحیمی
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78665" target="_blank">📅 16:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78664">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXhTpQUD7_x0j2N6SEr6kf9fn-VQ7MUwDA9taKSkVEJtbU3pyQvCBcOAFaTJMVlP8zoEhfnKApqRWbsE9uNYOfFklgTEN5ZI2zVC89STjYmprKLq3BRLB2M-7EUE-IAa8xIMKkwO6A_SnAujxlQGXYjX1s5fissMZ3J_oN71dvEFNmVgPgfwYaVO7_R3myIDV1n9-H3Ro5pyrm-QZU91JMELzVRq5X9xuQAMSQ2mGftKZ_zleeafcs4f7vx0LM4EylvPZB3Cyqph7MfayeJMvc4LASfKwwKpUKZPaXN8qVNMjY9L0j9z9jTnHz2fjD7Yhh_eyU806N44n9GfQMF97g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
رسانه‌های جعلی و ساختگی دارند تلاش می‌کنند این‌طور وانمود کنند که من از دشمن دعوت می‌کنم سن‌دیگو و لس‌آنجلس را بمباران کند، در حالی که آنچه واقعاً درباره‌اش صحبت می‌کردم این بود که افزایش موقت قیمت بنزین، بهای ناچیزی است که باید برای جلوگیری از دستیابی ایران به سلاح هسته‌ای پرداخت کرد. و اگر می‌خواهید بدانید بهای سنگین واقعی چیست، می‌توانید تصور کنید اگر آن‌ها سن‌دیگو و/یا لس‌آنجلس را بمباران کنند، چه اتفاقی خواهد افتاد؟
تنها کاری که من کردم، مقایسه پرداخت مبلغی کمی بیشتر برای بنزین، آن هم برای مدتی کوتاه، با بمباران شهرهای بزرگ ما بود.
همه این را می‌دانستند، رسانه‌های جعلی هم می‌دانستند، اما همچنان بیرون می‌آیند و می‌گویند که من از دشمن می‌خواهم دو شهری را که عاشقشان هستم بمباران کند.
«حرف‌های من کاملاً روشن است، اما این‌ها آدم‌های پستی هستند و فکر می‌کنند می‌توانند مدام اخبار جعلی منتشر کنند و قسر در بروند!»
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/78664" target="_blank">📅 23:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78663">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hEz22T6W9urcwAoXKNuR8bxhRJ8zyMIoVjKTknYp9xzOh7AJHw1-5-_C7kzYQvhZTPtRmz9hy9R9KDSQzzl-2pfV3d584YvZYY-N9xxhrAHQYFizhSXkOGNHYJrm_D0VW5H3FLiBqkxhUgy2UWiRXpBr6lt-MO51oKG_zJkosvl7GC_fhC5vs2J5q6LRGTikP0Sn4BtRhfvOQIwGQS2ezyw1AIU6isTWS5ln9ArDjMtD_RCNoxhugNC8xOIcuJHTM638ykCOCiZlHykk13M6BZDyWWr2VGlZ5ZZ7uU5Yprd3rRYtB9lneZ6wsQlVvkR-nLFMeOoWuoGyf1qOVH9OLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: مذاکرات در جریان است، پیش از انتخابات حمله نمی‌کنیم
ترجمه ماشین:
ما در حال انجام گفت‌وگوهای سازنده‌ای با جمهوری اسلامی ایران هستیم. می‌خواهم برای همه روشن کنم که اگرچه ایران هم از نظر اقتصادی و هم از نظر نظامی در وضعیت بسیار بدی قرار دارد و اگرچه محاصره همچنان با تمام قدرت برقرار خواهد ماند، در حالی که نفت با حجم بی‌سابقه‌ای از تنگه هرمز عبور می‌کند (تنها دیشب ۲۲ میلیون بشکه، بدون اینکه حتی یک بشکه از ایران آمده باشد یا به مقصد ایران برود!)، ما تا پیش از انتخابات میان‌دوره‌ای که قرار است روز ۳ نوامبر در ایالات متحده برگزار شود، در هیچ زمانی به ایران حمله نخواهیم کرد.
ایران سلاح هسته‌ای نخواهد داشت!
پرزیدنت دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78663" target="_blank">📅 20:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78662">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b534ce975d.mp4?token=gZccgpZ206TuKup9LOVEXz4mI53HVhHKD1Q4xWzdEZwWaeOeX2SbHSWtJF81v4sdNz0-AOmqkiiZ3HrV4OsAC76bc-ljg9KUZRYu3TnAVAlcC461YCvCZuuxp0sGsVVimemqoLKJz5MMF3CUx6E1H6jLTOks93pYUIOc9XugAfdv1m4Vnc_oeNsX7UbZ5a4HcmRGOscxvB08e6fbXI2sDT3Iasg7Rb37S5_THaFVCEGy4i6OTpNVZBktBfkiM0-vF2MimX173ExN_sc2OGnU2AW6ISB5ufH4hvcEybF1CdZfXsV2mJ2QnJedU5w0857furrr0ONmCBhaq_Qe_KK6jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b534ce975d.mp4?token=gZccgpZ206TuKup9LOVEXz4mI53HVhHKD1Q4xWzdEZwWaeOeX2SbHSWtJF81v4sdNz0-AOmqkiiZ3HrV4OsAC76bc-ljg9KUZRYu3TnAVAlcC461YCvCZuuxp0sGsVVimemqoLKJz5MMF3CUx6E1H6jLTOks93pYUIOc9XugAfdv1m4Vnc_oeNsX7UbZ5a4HcmRGOscxvB08e6fbXI2sDT3Iasg7Rb37S5_THaFVCEGy4i6OTpNVZBktBfkiM0-vF2MimX173ExN_sc2OGnU2AW6ISB5ufH4hvcEybF1CdZfXsV2mJ2QnJedU5w0857furrr0ONmCBhaq_Qe_KK6jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ گفت: «من باید در مورد ایران اقدام می‌کردم، چون آنها به سلاح هسته‌ای دست پیدا می‌کردند و آن وقت می‌فهمیدید مشکل یعنی چه.»
رئیس‌جمهوری آمریکا در ادامه با اشاره به احتمال حمله موشکی ایران به شهرهای آمریکا گفت: «ببینیم اگر آنها روزی به لس‌آنجلس یا سن‌دیگو حمله می‌کردند، چه اتفاقی می‌افتاد. این دو شهر به دلیل موقعیت جغرافیایی‌شان بیشتر مطرح هستند و منظور من حمله موشکی است.»
ترامپ افزود: «اگر چنین اتفاقی می‌افتاد، وحشتناک بود. بگذارید لس‌آنجلس یا شهری مانند سن‌دیگو را هدف قرار دهند. بگذارید یکی از شهرهای بزرگ ما را هدف حمله قرار دهند. آن وقت است که می‌فهمید مشکل واقعی چیست.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/78662" target="_blank">📅 19:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78661">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ys49Q42XkbW1Xuo4Qttowb2c0td1scpyY7B41Uv9Ou1HP0GPEkVJrOXn5k5DHCFFrEkrqOdE7bLcf1m9tJdvtGn78i9Z4EJke4uRnFgAJ7C0mEDxUA15UUX-IzawrkCWCQCUMri-zTLkRSDFVpK-iGbGmM4ckmY12G4r8MhpAotlWyhJUU0rPMEllivt3YtdTTTR0Q5VzHjBZ7OYYcfk7ssTKOz6Xek4ye0l4eV7R2_3RMFD7C2XtYAz-M9pJwU1rYlNMT0WVOgVUBJiDkxUeK7RteBw1GylkRMkUNMT1IF5yttrPeTNj2u3_sHOTNdOV2c0nU9WORA0lSMmRYtLFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز پنج‌شنبه ۱۶ مهر گزارش داد شرکت هواپیمایی لوفت‌هانزای آلمان پروازهای خود به ریاض را تا ۲۴ مهر و ایر ایندیا پروازهای خود به مقصد و از مبدا پایتخت عربستان سعودی را تا ۱۸ مهر لغو کرده‌اند.
این تصمیم همزمان با تشدید حملات حوثی‌های یمن مورد حمایت جمهوری اسلامی به فرودگاه‌ها و زیرساخت‌های عربستان سعودی اعلام شد.
حوثی‌ها اعلام کردند فرودگاه بین‌المللی ملک خالد در ریاض را با موشک بالستیک هدف قرار داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/78661" target="_blank">📅 19:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78660">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CNi4eghSoy3YVR2aLwi3lVBZfX2tW8wvPfhUu3hcvWqGlokLCMU15qfPjf7VR1OU6N1GQj4ex_mcm_qPzgm9638fsFVRSIxJoIEIxZxSI4-Njfe3apJ3tEX40pRTp1BbbAONTPEO6NyN4IVj56o5VEksm2hZFGrab8BbEswbvJV72VT8NRJ6HNWBXCctkKG0Sdg_U2uoLVIU5wZLrZVKIKxXOU1G2CIOlBWQptDG19G38patCC61jzj8ehHiSznbpTsNXvSlYzF1m4hrwDUqVdYIDf96Ye0XW5Z4KO6OwvjtkojfPOSi38DUxsOPPyvB9S3njYj6GS1oEHXQj2LcIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارگارت همیلتون، دانشمند آمریکایی و از پیشگامان مهندسی نرم‌افزار که نقش مهمی در فرود نخستین فضانوردان آمریکایی بر سطح ماه داشت، در ۹۰ سالگی درگذشت. او رهبری گروهی از متخصصان را بر عهده داشت که نرم‌افزارهای مورد استفاده در ماموریت‌های فضایی آپولوی ناسا را طراحی و توسعه دادند.
موسسه فناوری ماساچوست (MIT) با تایید درگذشت همیلتون اعلام کرد که او روز چهارشنبه هشتم مهرماه ۱۴۰۵، برابر با ۳۰ سپتامبر ۲۰۲۶، از دنیا رفته است. این موسسه در بیانیه‌ای، همیلتون را از پیشگامان علوم کامپیوتر توصیف کرد که پیش از فراگیر شدن حرفه مهندسی نرم‌افزار، در توسعه این حوزه نقش مهمی داشت.
همیلتون از سال ۱۹۵۹ تا اواسط دهه ۱۹۷۰ در موسسه فناوری ماساچوست فعالیت می‌کرد و مدیریت بخش مهندسی نرم‌افزار را بر عهده داشت. گروه تحت مدیریت او نرم‌افزارهای هدایت و کنترل فضاپیمای آپولو ۱۱ را طراحی کرد که در فرود تاریخی نیل آرمسترانگ و باز آلدرین بر ماه در سال ۱۹۶۹ نقش تعیین‌کننده‌ای داشتند.
در جریان این ماموریت، رایانه فضاپیما لحظاتی پیش از فرود با مشکل پردازش بیش از ظرفیت روبه‌رو شد، اما نرم‌افزار طراحی‌شده توسط گروه همیلتون توانست با اولویت‌بندی وظایف، عملیات فرود را ادامه دهد.
باراک اوباما، رئیس‌جمهوری پیشین آمریکا، در سال ۲۰۱۶ به پاس دستاوردهای علمی همیلتون و نقش او در پیشرفت فناوری فضایی، نشان آزادی ریاست‌جمهوری را به او اهدا کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/78660" target="_blank">📅 19:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78659">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THzJT1MMZzCit15bLfliNjeTHRDzWVQModLPY4KBl_EOdmQYXrbQ4rh9SRwY9XgAUB1_Tlc3i0C86W8Le1vQznY6neBDl1XxW8R4f0cBYckEl56b0xWpgXLYK3bi2AUn5TWkGO8DJuR850Za1Vxa8pw9mYkVz7A_PBabtUo1MAfZkqyJJl3wzyoHY6bqiD_McGt9wgGWk6xwo1ChRmvA4XS4ISgYcktB-X9wDqynvsAifVZGHLeBQSl-E0JMOd56ARnVwjY1xz8h-rcRkovHiYltYlnLTQjZj775WKLYPsCCe7sxNTWsTGdLhuN8qxm5Rdx1mdxE7dwernlpirNfNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان سعودی در چارچوب طرحی به ارزش حدود ۲۱ میلیارد دلار، توسعه میدان نفتی مرجان را برای افزایش ظرفیت تولید نفت و فرآوری گاز دنبال می‌کند؛ میدانی مشترک با ایران که بخش ایرانی آن «فروزان» نام دارد. براساس گزارش مرکز داده‌های باز ایران، عربستان روزانه حدود ۷۳ میلیون مترمکعب گاز از این میدان برداشت می‌کند، در حالی که ایران از بخش خود گازی تولید نمی‌کند.
در تازه‌ترین مرحله توسعه مرجان، شرکت نفت عربستان، آرامکو، قراردادی با شرکت آمریکایی «کی‌بی‌آر» برای نوسازی تاسیسات این میدان امضا کرده است. کی‌بی‌آر روز سه‌شنبه ۱۴ مهر ۱۴۰۵ اعلام کرد خدمات مهندسی و اجرای پروژه را برای تاسیسات فرآوری، فشرده‌سازی گاز و زیرساخت‌های برق مرجان ارائه خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/78659" target="_blank">📅 15:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78658">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6E8tt8nj1-zUv2A_EyvwBP4vkFLvdWr9Zk6pvi5Y_nSXcfXvlqQ7FwV4gdG5FOpg5EaeUPFNKJH8JLJMEMolvOnUYAJYm-wKy_hpNsBUZCPFVVhfcFxSJzxhc-t98mo5BMJMFgrb9YZR9McNo-EyPZr1QOBRpZ6sQ9j1T9wK2TRK1Ixhd5Bj-mRdCvcZOwYnjOjvlFwyPqDzJNjgfmnUX7iTsDyRrsT7tz2otqQ1sxOh2VqidUaAawic5_Bwf2vqCBhWxQzYQP9TEPn7UW9myhUVEC1cV8qnXCm5WY-uGU1HAa88QuZDgS6Fs-yOb320RnowJkTdJw19XeIudPVBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز، روز پنجشنبه ۱۶ مهر ماه، گزارش داد شمار کشتی‌هایی که از تنگه هرمز عبور می‌کنند، پس از افزایش حملات به نفتکش‌ها در هفته گذشته، به پایین‌ترین سطح در بیش از دو ماه گذشته رسیده است.
رویترز بر اساس داده‌ها و تحلیل‌های شرکت تحلیل کپلر گزارش کرد، روز سه‌شنبه فقط ۷ کشتی تجاری از تنگه هرمز عبور کردند که پایین‌ترین رقم از اول مردادماه تاکنون محسوب می‌شود.
عبور نفت خام از این تنگه نیز با کاهش ۲۷ درصدی نسبت به بالاترین سطح زمان جنگ در هفته قبل، به دست‌کم ۱۰.۱ میلیون بشکه در روز رسید که معادل ۷۴ درصد سطح پیش از جنگ است.
به گفته تحلیلگران کپلر، بخش عمده این کاهش به انتقال محموله‌ها از کشتی به کشتی در دریای عمان مربوط می‌شود.
به گزارش رویترز، با این حال، صادرات از سواحل دریای عمان و دریای سرخ به ۶.۷ میلیون بشکه در روز افزایش یافت، رقمی بیش از دو برابر سطح پیش از جنگ که به جبران کاهش عرضه از طریق تنگه هرمز کمک کرد.
داده‌های کپلر نشان می‌دهد تعداد کشتی‌های عبوری روز چهارشنبه به ۱۰ عدد افزایش یافت، اما همچنان بسیار کمتر از بیش از ۲۰ کشتی در روزهای یکشنبه و دوشنبه بود.
این گزارش پس از آن منتشر می‌شود که حملات به نفتکش‌های عبوری از تنگه هرمز در هفته گذشته به بالاترین میزان هفتگی از زمان آغاز جنگ ایران رسید. پیش از آغاز جنگ در نهم اسفند سال گذشته، روزانه حدود ۱۲۵ کشتی تجاری بزرگ شامل نفتکش‌ها، کشتی‌های حامل گاز، کشتی‌های فله‌بر و کشتی‌های کانتینری از تنگه هرمز عبور می‌کردند.
همزمان، دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنحشنبه نموداری در شبکه اجتماعی تروث سوشال منتشر کرد که نشان می‌دهد سطح تردد نفت از تنگه هرمز به میزان پیش از جنگ آمریکا و اسرائیل علیه ایران بازگشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/78658" target="_blank">📅 15:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78657">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vazdy-cgK-Gb616QBlpkLtJXb0r6El6OH39YYwgksZC4Le3Yho3TsBSAuKPwYGBrGZwTSwBs3p_jDc14p2CtRreCX17aQ9ELRqZdvdp86Z-CUCHHlDw1R7ZJ1ItaUNLYRoU7SGfpgIOEXnejttOWKlBOAc8rTSbois2nskqQnwQ067Kc0vpRhpWDXXTbvCcv_oO6xgAmq2TJWjMn2JGlCDL9AR2XZdmsFGLZkG_kgYVogMKe95XC55SlHc_jRcMPjyDwcJ7rNmze8ff6s3wQvE8AXGjvTIe3EQ956dF-qJEKxIHweO46JfnzdZkXkq1QKLgUWC0hpSt1EdAuGlgbpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی حمله افراد مسلح ناشناس به ستاد فرماندهی انتظامی شهرستان گلشن در سیستان‌وبلوچستان، نیروی انتظامی وقوع انفجار و تیراندازی در این منطقه را تایید کرد. هم‌زمان، ارتش جمهوری اسلامی از کشته‌شدن یک نفر و زخمی‌شدن سه نفر دیگر در حمله‌ای جداگانه به مینی‌بوس حامل کارکنان ارتش در زاهدان خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/78657" target="_blank">📅 15:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78656">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S8Xz3xBAr7a6bYwv9YXiPJ40-jYoKl7X-CtU1KJPJ5d4V8pJ5jNzFYtYCdcYqlWDES_RoD83xAZv94JH3OkM0hlGbir2h2kYiI9m_JH4iEdH0kitTQ2kGJ3UPDiGLyqNhtOy796KNwX_VNmqXVIvhn30ga9H5ul1ZD4hngJyEiN98vn8pIG3s9KWvSTXbd76fnSdlzpxh3TU3IldwrV1dzhFrTrw1k1aL_S_OEL6_2ufpoXsDY-_0VHYsAhN6aIOduuah7L2ToPnr4jrpg29SM31TlBRrItK7uVS94LHFbGiZbleGT5MZQEdWWY1RD56DyjHItWmVdCIljpKmSEGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز
پنج‌شنبه ۱۶ مهر در گزارشی تحقیقی بر اساس گفت‌وگو با بیش از ۷۵ کارشناس حقوق بشر، وکیل و شهروند ایرانی نوشت ایران پس از اعتراضات دی‌ماه شاهد شدیدترین سرکوب چند دهه اخیر از سوی جمهوری اسلامی است.
به نوشته رویترز، دستگاه‌های امنیتی و قضایی جمهوری اسلامی با همکاری صداوسیمای حکومتی، از طریق اعدام‌های شتاب‌زده، محاکمه‌های غیرعلنی، پیگردهای قضایی گسترده و انتشار اعترافات اجباری، در پی ایجاد فضای ترس و خاموش کردن مخالفان هستند.
بر اساس این گزارش، از ۲۸ اسفند ۱۴۰۴ تاکنون دست‌کم ۳۴ نفر از افرادی که در ارتباط با اعتراضات دی‌ماه بازداشت شده بودند، اعدام شده‌اند. پنج نفر از آن‌ها تنها در ۱۰ روز گذشته اعدام شدند. در مقابل، طی چهار سال پس از اعتراضات ۱۴۰۱، در مجموع ۱۵ نفر در ارتباط با آن اعتراضات اعدام شدند.
رویترز همچنین گزارش داد مقام‌های امنیتی ارمنستان در ماه مه به گروهی از معترضان ایرانی درباره تهدیدهای جدی علیه جانشان هشدار دادند و از آن‌ها خواستند برای حفظ امنیت خود و خانواده‌هایشان این کشور را ترک کنند.
اشکان، معترض ایرانی ۳۰ ساله که در جلسه با مقام‌های امنیتی ارمنستان حضور داشت، گفت به آن‌ها هشدار داده شد افرادی احتمالا برای ربودن، ترور یا آسیب رساندن به آن‌ها اعزام شده‌اند. رویترز نوشت روایت او را با گفته‌های معترض دیگری که در همان جلسه حضور داشت و فایل صوتی آن جلسه تطبیق داده است.
رویترز همچنین نوشت نهادهای امنیتی جمهوری اسلامی با تهدید خانواده‌های مخالفان ساکن خارج از کشور در داخل ایران، لغو گذرنامه‌ها و خودداری از ارائه خدمات کنسولی، فشار بر منتقدان را به خارج از مرزهای ایران گسترش داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/78656" target="_blank">📅 15:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78655">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DynOBcSKeSBi_Erth7mKJvBvwhKQAFbd-r1fjGspO7PxhA8-GR2d6DKMefBC5O_VyGd7UkFCEcdPvgS7qCvGkMXkfpAQ5MJpaAYbiYya5p3d7tIJ9oaEpDOiBUuXWwh5Tawj4SKuA1W1vwU0703lw-4thItxg0NtphpEnt-iyp339_qPLLjzt4RIVfeLjiDfp4DPdpYO5mp5dSj5rL-adKXPQL_0pgQdmZSRH-W-JojiotjRYDF8jXVieUTFGJJQ2DIBRqUZzd4s15rzzHjusGP7tCvb22tzJXUigfuMVYXi42dd-RBDC5ee15zJEtgr4TIi0EgUi1KcKF73ZgSG9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، بامداد پنجشنبه ۱۶ مهر در سخنرانی در ایالت تگزاس درباره جنگ با ایران گفت این جنگ «خیلی زود» پایان خواهد یافت و ایران را «کشوری شکست‌خورده» توصیف کرد.
ترامپ گفت: «وقتی این جنگ تمام شود که خیلی زود خواهد بود، آن‌ها یک کشور شکست‌خورده‌اند، کمی رمق برایشان مانده، اما نه زیاد.»
او همچنین با اشاره به نفت عبوری از تنگه هرمز گفت این نفت در سراسر جهان توزیع می‌شود و بار دیگر بر نقش آمریکا در انتقال نفت از این مسیر تاکید کرد.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا در جریان یک گردهمایی انتخاباتی در تگزاس گفت «ما به زودی از ایران خارج می‌شویم و قیمت نفت هم مثل سنگ پایین می‌آید.»
او گفت افزایش بهای نفت ارزش جلوگیری از دستیابی ایران به سلاح هسته‌ای را دارد.
رئیس‌جمهور آمریکا همچنین در مورد احتمال دستیابی به یک توافق با ایران گفت: فکر می‌کنم این توافق واقعاً چیزی است که می‌خواهم انجام دهم، اما آیا آن‌ها حاضرند برای متوقف کردن برنامه هسته‌ایشان چیزی به ما پیشنهاد دهند؟ و ما قطعاً هرگز اجازه نخواهیم داد ایران سلاح هسته‌ای داشته باشد.
آقای ترامپ همچنین با تکرار سخنان جنجالی چند روز گذشته‌اش در مورد حمله فرضی ایران به لس‌انجلس و سن‌دیگو گفت: «همین چند روز پیش گفتم: بگذارید موشکی به سن‌دیگو یا لس‌آنجلس اصابت کند... بگذارید به سن‌دیگو یا لس‌آنجلس حمله کنند تا شاهد اتفاقات ناگوار باشید... ما اجازه نمی‌دهیم چنین اتفاقی بیفتد. ما از شهرهایمان محافظت می‌کنیم. ما از کشورمان محافظت می‌کنیم. ما اجازه نمی‌دهیم چنین چیزی رخ دهد.»
این سومین سفر دونالد ترامپ در طول یک ماه گذشته به تگزاس برای تبلیغ نامزدهای جمهوری‌خواه محسوب می‌شود؛ نامزدهایی که در تلاش برای حفظ کنترل کنگره، اکنون با رقابت‌های انتخاباتی میان‌دوره‌ایِ به‌طور غیرمنتظره‌ای فشرده روبرو هستند.
ترامپ در ورزشگاهی مملو از جمعیت در سن‌آنتونیو سخنرانی کرد تا از کن پکستون، نامزد جمهوری‌خواه سنا در این ایالت حمایت کند که در رقابتی تنگاتنگ با جیمز تالاریکو، رقیب دموکرات خود، قرار دارد.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78655" target="_blank">📅 05:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78654">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egq0lw2PybcuPEZwe600vxCsNMlVuxIfVvsQNeMHLSnc4daYaOaMSksj0Hx7Tyd_x8KLYl_M4402r-Wh4KeluosnM8OWzS9vB1D-CE3Nk6M0UHXb_wi-dfJFmhMD2zi1fzaBZr2T5xltlxmLqxvxX0OLuM753kefSHcUlJrtvrEKaV6fJJk5fNs5Eh-KgMsy27hfvAWSUrgYbmKiPGN2JGuYMTQabCWP0KxP4yJEdL57ehMwnWK4lk57cbX2kyFUWtB-vKB2FfKHgwEUfCbGKTeBaxICkoSTJmgQa5lvlRUvbCrXJB8M5EikksoKti58X9QIjW3l7QxSQSdSQWJKvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رسانه آمریکایی گزارش کرده‌اند که پنتاگون برای حمله احتمالی مجدد به ایران طی روزهای آتی آماده می‌شود.
سایت خبری اکسیوس به نقل از مقام‌های آمریکایی گزارش کرده طی روزهای اخیر پنتاگون با صدور دستورالعملی از سنتکام (فرماندهی مرکزی آمریکا در منطقه خاورمیانه) خواسته روند آمادگی خود را برای از سرگیری عملیات رزمی عمده علیه ایران تکمیل کند.
همچنین مجله آتلانتیک هم در گزارشی اختصاصی به نقل از دو مقام آمریکایی نوشته کاخ سفید از پنتاگون خواسته است تا گزینه‌هایی برای حمله به اهداف ایرانی تدوین کند که امکان اجرای آن‌ها پیش از انتخابات میان‌دوره‌ای وجود داشته باشد.
به گزارش آتلانتیک، دونالد ترامپ مشتاق است پیش از انتخابات، قیمت بنزین را کاهش دهد و به پیشرفتی عمده در مناقشه با ایران برسد.
به گزارش اکسیوس، دستورالعمل پنتاگون شامل تاریخ مشخصی برای آغاز حملات نبود و دونالد ترامپ هنوز تصمیم نهایی را اتخاذ نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78654" target="_blank">📅 05:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78653">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jy__P5dybUbcvobjenVBenZtbmwjCwDBMKEZe4-jd8RRCjylYY_tsX3NZiHVuHH5tTFHTBqYhuQPUG-agArCD7Q0d960UIO6pO6qNh1ocRyg4KWWGyhh04a9DOIzTGnc6kmHWBOYMaRo2q0zL7ukozur0sadSPxrWOvPmDoR9EGuSzCNTdJDhe8_yBZ_-InoK-oiDdgXpErj_94GKU9VL88-tCEXAfISGoKFN_2kEnhNMi7KLuMVt_9HTj72ry-DxXj-duSEWnTURct4j9SUhH2je0zU-C--J-wyhy1CHCFwkUfF6ZhVjSKe77n4F8WYfIv8r8JRs8VqB6kCUgIDNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی ارتش آمریکا، سنتکام، بامداد پنجشنبه ۱۶ مهر با انتشار پیامی در اکس، اظهارات یکی از فرماندهان سپاه پاسداران درباره بسته بودن تنگه هرمز و کنترل کامل ایران بر آن را «نادرست» خواند.
سنتکام اعلام کرد تردد کشتی‌های حامل کالاهای تجاری و محموله‌های انرژی، از جمله ۲۰ میلیون بشکه نفت خام، در تنگه هرمز جریان دارد و افزود: «ایالات متحده و شرکای منطقه‌ای به‌وضوح کنترل تنگه را در اختیار دارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78653" target="_blank">📅 02:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78652">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f4IqVCJENy1sexCQf8V4twBzGZSlwWCHciiQdC5qBnmKkQoiw7OgQujnmBaIIhHx7yKulEg_mBlVnPW8a4nA6tbJZkJJjyj4SHTEctN23ilzM-E2_PtF0A5HG0ro24_Ahf23QPFad3xxCI8tw52plVlkF6mvcITdUWDF4kHJNFquCs3Q_uQkvxftfqXY77lJCLloTtj5w9xoqumRS_HaYYahbNHNZrh5RTHyC9TZ3MsqNukfJ2M_mkeLgDePvuC_D6TGa5G8J1SNfV88wduduDquIg-ZRyqlfXoPSsPGFoi8rXEa7xgdP1RKMFzqWiz4zlCQv5UHasPmTBKQk-UXbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملیات تجارت دریایی بریتانیا: در حمله به یک نفتکش در شمال قطر خسارت جانی گزارش شده است
سازمان عملیات تجارت دریایی بریتانیا شامگاه چهارشنبه ۱۵ مهر اعلام کرد یک نفتکش در آب‌های شمال قطر، در ۵۱ مایلی مدینه‌الشمال، با چند پرتابه هدف قرار گرفت.
بر اساس اعلام این سازمان، در این حمله تلفات جانی گزارش شده، اما هنوز جزییاتی درباره شمار کشته‌ها یا مجروحان منتشر نشده است. مقام‌ها در حال بررسی حادثه‌اند و از کشتی‌های منطقه خواسته شده با احتیاط تردد کرده و هرگونه فعالیت مشکوک را گزارش کنند.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78652" target="_blank">📅 23:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78651">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-ZbVkUkIRfGGImlAILqddL5RyNlu0Q4wtBc8Ir8QcqbzA1sSpVwEHobsljYQ-33_mqnMW_znr56WPvBUSGkylyQHq7uLgM88pf7QQ1oUl7mV_oLg9KfUaHFdTbaq7U6oTtQ3wyd7vwDbMhKXUPeZCsKkT6dc0uY49OF2AYr4Rrqo5NToQzTGWVzXIa3AZUz-pDDtD8lfqjT1d2NZMRMRgewNhYOWypqIbiFnYjLg1fwc7mdaGQllUEwxbsyW1NUEOB0uXoZzxAl9jApi7mb_r05eoHhoT8MDMvV46BAzfA6sTRCDMTpeilZ7vx8iCAON9ZHmaWjtxKbAexUCBgvPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو منبع مطلع به خبرگزاری رویترز گفته‌اند جمهوری اسلامی ماه گذشته ۲۰۰ میلیون دلار در اختیار حزب‌الله لبنان قرار داده است تا این گروه به خانواده‌های لبنانی آواره‌شده در جنگ امسال با اسراییل کمک مالی کند.
بر اساس اطلاعات منابع رویترز، حزب‌الله قصد دارد در مرحله نخست به هر خانواده حدود سه هزار دلار کمک کند. اولویت با خانواده‌هایی خواهد بود که روستاهایشان ویران شده یا به دلیل حضور نیروهای اسراییلی در مناطق جنوبی لبنان امکان بازگشت به محل زندگی خود را ندارند.
یکی از منابع شمار این خانواده‌ها را حدود ۵۰ هزار خانواده اعلام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78651" target="_blank">📅 18:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78650">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppxUvuBF3bVhScG0NQEDqggXfHMJarpqBI0oPPIK-FF7l2JYMAk2O9zCJOf7_j74y-njmVBwE_pCHI6cSuvI6KwU2gd9-0FPUJZ8so1yswQ6iWQr9bjn9e8mO2zfOfXCT_5Ixz-dckqejVKVvWz0fHRcRVQFE-8f0dFbMVmw-KupLuKMhC3M3dw9lSBGhKoAtiyLi3iDd5c3ZcLFMYxnM5OKQnDLTgCND3URuHYSeHFFdnghbdJOB9wAlcJV2Vdm0qdHviL5gWeJRCJehaDICAg0eG80jKWjnYAxlSxjr5Kk-fC5FGxMdlQ5PPUnq66844-IRIxBA02SbNXPXFB4pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهاره آقایی، وکیل دادگستری محبوس در زندان قرچک ورامین، به ۲۰ سال حبس محکوم شده است.
کانال تلگرامی شیرین عبادی
با اعلام این خبر، حمایت از معترضان دی‌ماه، حضور در مراسم چهلم سپهر شکری و کمک حقوقی به خانواده‌های دادخواه را از موارد مطرح‌شده در پرونده او عنوان کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78650" target="_blank">📅 17:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78649">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6AZ2VdF3YblKmM_Og9Y-zEJY6M8iND6fpcAT0_TTUChFRV2PA5bG8BsXP6LoyRy6gSekMN0Haq8PRB2yMmf656xVDbRyQSCGOhknrnsRX4v1p1cnxzTT_dofPsKafSGnAIVYp2tyaYfShKTUFSjRRWeWss7zMoG8_sp6Byo5CbFgFsXpjvqT7jMO0kY6XyTW_Ed9dEkwTSqaA5ElCAJZg9nwmzvpjuWr0itxjBZcWW30Ro57FBpHXIPMtTLa5dLqQLIVyiQLvWz0tI9-wo9uOO52-cJkgEZSMMw9B8p2-a30ErO37RWgU4gu_Stw3r2HE67LdqHf_muvzDQUOZYQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده آمریکا، با انتشار پیامی در اکس و با لحنی کنایه‌آمیز نسبت به استعفای محسن پاک‌نژاد، وزیر نفت ایران نوشت: «ایران وزیر نفت جدیدی دارد. با توجه به اینکه از ۲۵ اوت تاکنون حتی یک بشکه نفت خام نیز توسط ایران بر روی هیچ شناوری بارگیری نشده است، این وزیر نفت دقیقا چه چیزی را مدیریت می‌کند؟» پیش از این، مهدی طباطبایی، معاون ارتباطات و اطلاع‌رسانی دفتر ریاست جمهوری ایران اعلام کرد، پزشکیان پس از موافقیت با استعفای وزیر نفت، طی حکمی حمید بورد، مدیرعامل شرکت ملی نفت ایران را به عنوان سرپرست وزارت نفت منصوب کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78649" target="_blank">📅 17:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78648">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLcINC6BQ2D_e-w0dYPG4Ao2G0ngPRFH7RqH5_8m5N4TMrR0WUvqEP0IW_m0UJpp43Cdh_qJ-q93XJOmQfADmenFnzNQ-1gfHJjilTnzkST5f8QMjfeYshXc3QJn_LXHgpJkEvAAL26fiO3w3iIdgtcAcSNaf-awZqnYGSXJh399RlSXcxEIHSdt8TGACdFAu2r3wI77gc8P-hYVaZqQuTnoV6uWIFsxV-6_7PzxwD7TqiWxmuH1PzLxJpTGNae4aJnQ63Es2bV8kdY350pFCwo0pgGgbKdeP9ICOtkn5bVoPSJY2Okz1kFPKE7B6nW76hYn0y6FaHjiZ2FIoWPV7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام امید گودرزوند چگینی، معترض ۳۷ ساله، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ و محبوس در زندان چوبیندر قزوین، در مرحله تجدیدنظر تایید شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78648" target="_blank">📅 17:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78646">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YPGRJO-NeopHCAVHXMGk3CPUlbZfZKiWo0vtk7ZscyEASYW7aGfTbQnITjEla-p1DbgEokXL32fNNG_H7xUtqVPO5Slcox3LCDUOZR1m5M6dJiEBjVNDwJXSSgzvy2eBhzeNHHkO3N35c2gCWtPKsnbPxuXlipx10CypseMWkx7OYLNTidHNtjUjuGUdjVQotBtcpJ_y56wOj0jOCqvTpaS8jWe2rUia-IZ-jBZUu3jSOSQxsbhWLD1fRpUTDPc1K2knTBWZR7n3qrDOWwTpCbMUbrw56jXot2d8p-Fzl38ZPsT4-ToPwiGVSukjbghg2SPhUhb2l9tO_HLr-PzAvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/20e0cac582.mp4?token=oj-s92geQcXsQ1P5Y6F_FClfWVdEglmWnXRYh3knAzGz-tOxkBNVN2vaZRe5EbsMHuuHjXNpEIZnIWofsGYMhfiVE3MCaYfB0mtha81cXo_VJA7bcnh21pCi58fmvo_TwHnjBEx1-4bq6rhu9Iw4RriC_2DkGUfzWEq7dRzG0EwRtlyJ6DKp0aIthkCQtOh4ECylJKHDHNvyGKWO0inY_dejYj2jy5EXS57pmQDPTfBsN6zcMNnhqJYcagHf_ktl2YMnoV5Xk6mgADVHijDJGnsQavl7GwWbFjSRvMSjhzMJWs_LvOYpGTrfRSnawmxqC1y2Y8ulgG9aovB_shCW4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/20e0cac582.mp4?token=oj-s92geQcXsQ1P5Y6F_FClfWVdEglmWnXRYh3knAzGz-tOxkBNVN2vaZRe5EbsMHuuHjXNpEIZnIWofsGYMhfiVE3MCaYfB0mtha81cXo_VJA7bcnh21pCi58fmvo_TwHnjBEx1-4bq6rhu9Iw4RriC_2DkGUfzWEq7dRzG0EwRtlyJ6DKp0aIthkCQtOh4ECylJKHDHNvyGKWO0inY_dejYj2jy5EXS57pmQDPTfBsN6zcMNnhqJYcagHf_ktl2YMnoV5Xk6mgADVHijDJGnsQavl7GwWbFjSRvMSjhzMJWs_LvOYpGTrfRSnawmxqC1y2Y8ulgG9aovB_shCW4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، می‌گوید ایران فرصت‌های متعددی را برای دستیابی به توافقی دربارهٔ برنامه هسته‌ای خود با ایالات متحده از دست داده است.
او روز چهارشنبه ۱۵ مهر در یک نشست خبری مشترک با همتای یونانی خود در آتن گفت: «ایران فرصت‌های متعددی را برای رسیدن به توافق هسته‌ای با آمریکا از دست داده و همچنان مبالغ هنگفتی را صرف تروریسم، تسلیحات و حزب‌الله می‌کند.»
روبیو همچنین گفت ایران اکنون با اقتصادی رو به فروپاشی و تحریم‌های تازه روبه‌رو است و مسئولیت این وضعیت را متوجه «روحانیون تندرو شیعه حاکم بر ایران» دانست.
او گفت: «اقتصاد ایران در آستانهٔ رسیدن به وضعیتی است که از نظر وخامت، کمتر کشوری در جهان آن را تجربه کرده است و همهٔ این‌ها نتیجهٔ عملکرد روحانیون تندروی شیعه‌ای است که در آن کشور تصمیم‌گیری می‌کنند. آن‌ها هستند که مردم محروم ایران را به چنین وضعیتی دچار کرده‌اند.»
وزیر خارجه آمریکا همچنین با تکرار موضع واشینگتن دربارهٔ جلوگیری از دستیابی ایران به سلاح هسته‌ای گفت دونالد ترامپ توان نظامی و بخش بزرگی از ظرفیت صنایع نظامی ایران را از میان برده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78646" target="_blank">📅 16:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78645">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CqnE7yJ7zz-ka-NwxvhI6uw54oHLLfFNVV7Wlpv7zX_CgFxosxJudybRvuEHCAGOwcG_sQA3kIIsTbwm5Gb3IEQ89WstD5qMcZBpdVUoiSpCkQffLPED8Kxw0DPoBS665dyDAqmGVGagRTpPB8foE8FUSymS9YrehBYyx2jPb3_wWd_VSTk-7tgba2dit_fZdowUqZW31oLBTToY-cKxyawsXVhtujbX6vvQEasfqZsimxLMb5W3DrC5goDJysmlTM7p7jXYBlRaTPDBrZdbhMrWGZtmaOzu6f43Yu_LxJkHScw7VHiTjiI4ebWH7c1A-sKAxeEkxbSJCIJQ1A79JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه خراسان نوشت که نجمه امینی، دختر ۲۳ ساله، به اتهام «سب‌النبی و توهین به ائمه معصومین» در فضای مجازی، از سوی شعبه ششم دادگاه کیفری یک خراسان رضوی به اعدام محکوم شده است.
امینی پیش‌تر در یک فایل صوتی از زندان وکیل‌آباد مشهد از صدور حکم اعدام برای خود خبر داده بود.
پس از انتشار این فایل صوتی، خبرگزاری فارس، وابسته به سپاه پاسداران، اعلام کرد که هنوز هیچ حکم قطعی برای نجمه امینی صادر نشده و دیوان نیز درباره پرونده او اعلام نظر نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78645" target="_blank">📅 16:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78644">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cA3OTe877YWO88KIMzCiy3ibT2jB32cd8X3RKtgNKyUOLWNHQAk8Xyg2PsuM4urqWjNcZFlJRQRSqi0BJheM2zTqpYKPzuynUcDtWSF1YTd67PXxz3G2knkWiQmlUnz0IiGph5tP7zmvtow5Ew-YavgiaGogT07eShd0TyO4qEhmWRHHyjLIxEQEgcYihPC4al69tPpUqZlObIimO2vpZudCiAt2iu7LiUUDMBDZNRlGzD8Nep4bp5TLdfyZLlVgMhQ7ReSIJPQ5QZoKJydZ8qvmudsf2zzWHDMOUnsqnBgD29LL9ehrYECSpN53cL64IW4Uhq4YjVb_snyHexSo9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس: ایران باید غنی‌سازی را عملاً کاهش دهد؛ میزان اختیارات پزشکیان و عراقچی روشن نیست
🔸
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، می‌گوید حکومت ایران برای پایان یافتن جنگ باید ظرفیت غنی‌سازی اورانیوم خود را به‌طور «معناداری» کاهش دهد و ایالات متحده در مذاکرات با جمهوری اسلامی، به وعده‌های لفظی بسنده نخواهد کرد و خواهان اقدام عملی تهران است.
🔸
آقای ونس در گفت‌وگو با خبرگزاری رویترز که بامداد چهارشنبه ۱۵ مهر منتشر شد، همچنین گفت ایالات متحده با مسعود پزشکیان، رئیس‌جمهور ایران، و عباس عراقچی، وزیر خارجه، در تماس و مذاکره است، اما برای واشینگتن روشن نیست این دو مقام تا چه اندازه در ساختار فعلی قدرت ایران اختیار تصمیم‌گیری دارند.
🔸
اظهارات او در حالی مطرح می‌شود که تهران و واشینگتن طی هفته‌های اخیر پیشنهادهایی را برای پایان دادن به جنگ و بازگشایی کامل تنگه هرمز ردوبدل کرده‌اند، اما دو طرف همچنان بر سر دامنهٔ مذاکرات و مسئله هسته‌ای اختلاف اساسی دارند.
🔸
معاون رئیس‌جمهور آمریکا در پاسخ به پرسش رویترز دربارهٔ شرایط واشینگتن، خطاب به مقامات جمهوری اسلامی گفت: «اگر سلاح هسته‌ای نمی‌خواهید، پس چرا به سوخت غنی‌شدهٔ ۶۰ درصدی نیاز دارید؟ و اگر می‌خواهید تعهد خود را به نساختن سلاح هسته‌ای نشان دهید، سوخت با غنای بالا تولید نکنید. این یک مسئله بسیار پایه‌ای و تعیین‌کننده است.»
🔸
او افزود: «فکر می‌کنم اگر آن‌ها بخواهند تعهد خود را به نساختن سلاح هسته‌ای نشان دهند، باید در زمینهٔ ظرفیت غنی‌سازی خود اقدامی معنادار انجام دهند.»
🔸
آقای ونس در عین حال تأکید کرد که آمریکا همچنان برای رسیدن به توافق آمادگی دارد، اما چنین توافقی باید شامل امتیازهای مشخص و عملی از سوی ایران در زمینه برنامه هسته‌ای باشد.
🔸
او گفت: «ما قرار نیست حرف را با عمل معاوضه کنیم.»
🔸
این موضع با مواضعی که مقام‌های جمهوری اسلامی در روزهای اخیر اعلام کرده‌اند فاصلهٔ زیادی دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78644" target="_blank">📅 02:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78643">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/74ccbd7257.mp4?token=LGKPRAROqxM0Vi__YaAkjvAw9WZEJyuuuOoNs_IS8KZhqsd-7BX9zYT08BfTHK3rhQyz0B9v192HQ7jknayfWqE4oN9OY_rq7NieluYrQwj0QZAougAZ51gIMZKUMTQbogpY1Ao-BtzG4HK5M99RlDDPgZgDbYZShxnnbfphV8O3A98XjtgHqyLmnrHYw4O5q7rOskeFX2CBl_ZhoVgIGuSTmzM0IJmtqws8J8j_Vn-rIN_37M0jT4K9fcYjnV08bYoZ7-pmaAgAj0XMFYEdOLULq-wdFh5OLZpJ8CbspVWSjZ46A0qy8iujRsoar2vExoImAnd-k34btVn1rrtIwrk53XsNqJgWAhYvir28HScenCWL-B5ehueAQdUksjpC7mZMJHiGS5i5QfEDEWulZjmA83k07uF7v4BGcRH5YjidDYJ95ckiz3s7glBDOrl_V8082D6RNGtA4DNKVn4VMI23xZUZ26omZa6F58exrz6Z-nSzoXAlV8e8QAnGqqRY7TPgcOE-zngtCSbZUi_RyeIx_8jQtuSAJI70bbkfPYoU4FFnMZ5g8Tfhol3AIwS9d3fPBVUbPEilBYHljwf_LqbTkJeoAuhlwV7rqJFeOYMbgIZJ25XU2i6PQdYJDXyNY34KMzK6AVfpGMDShjco9aw25dPhuoW71Owjf_q7auE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/74ccbd7257.mp4?token=LGKPRAROqxM0Vi__YaAkjvAw9WZEJyuuuOoNs_IS8KZhqsd-7BX9zYT08BfTHK3rhQyz0B9v192HQ7jknayfWqE4oN9OY_rq7NieluYrQwj0QZAougAZ51gIMZKUMTQbogpY1Ao-BtzG4HK5M99RlDDPgZgDbYZShxnnbfphV8O3A98XjtgHqyLmnrHYw4O5q7rOskeFX2CBl_ZhoVgIGuSTmzM0IJmtqws8J8j_Vn-rIN_37M0jT4K9fcYjnV08bYoZ7-pmaAgAj0XMFYEdOLULq-wdFh5OLZpJ8CbspVWSjZ46A0qy8iujRsoar2vExoImAnd-k34btVn1rrtIwrk53XsNqJgWAhYvir28HScenCWL-B5ehueAQdUksjpC7mZMJHiGS5i5QfEDEWulZjmA83k07uF7v4BGcRH5YjidDYJ95ckiz3s7glBDOrl_V8082D6RNGtA4DNKVn4VMI23xZUZ26omZa6F58exrz6Z-nSzoXAlV8e8QAnGqqRY7TPgcOE-zngtCSbZUi_RyeIx_8jQtuSAJI70bbkfPYoU4FFnMZ5g8Tfhol3AIwS9d3fPBVUbPEilBYHljwf_LqbTkJeoAuhlwV7rqJFeOYMbgIZJ25XU2i6PQdYJDXyNY34KMzK6AVfpGMDShjco9aw25dPhuoW71Owjf_q7auE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌های مربوط به ایران در سخنرانی ترامپ، به تشخیص و ترجمه ماشین:
ما در جمهوری اسلامی ایران خیلی خوب پیش می‌رویم؛ خیلی خوب. آن‌ها دیگر نیروی نظامی ندارند؛ نابود شده. همه‌چیزشان نابود شده و آن‌ها همان طرف شرور بودند؛ قلدر خاورمیانه بودند و دیگر چندان قلدر نیستند. اما هنوز باید کار را تمام کنیم و فقط مسئله این است که به کدام روش. می‌خواهیم این کار را به روش خوب انجام بدهیم یا به روش نه‌چندان خوب؟ خیلی زود خواهید فهمید.
وقتی به «دیوار فولادی» نگاه می‌کنم، همان کاری که ما انجام داده‌ایم و آن‌ها اسمش را محاصره گذاشته‌اند؛ من اسمش را «دیوار فولادی» می‌گذارم. حتی یک کشتی هم نتوانسته به ایران برسد. تنها کشتی‌هایی که عبور می‌کنند همان‌هایی هستند که ما اجازه عبورشان را می‌دهیم و این تأثیر بسیار بزرگی داشته است.
برای همین کشورشان از نظر مالی شکست خورده است. یک کشور شکست‌خورده‌اند؛ همه دارند کنار می‌کشند، همه دارند می‌روند. به نیروهای نظامی‌شان حقوق نمی‌دهند، به پلیس‌شان حقوق نمی‌دهند، به هیچ‌کس پول نمی‌دهند؛ اوضاعشان به‌هم‌ریخته است. اما هنوز باید کار را تمام کنیم.
نیروی دریایی ما پیشتاز است تا تضمین کند که ایران هرگز سلاح هسته‌ای نخواهد داشت. و این همان چیزی است که همیشه گفته‌ایم: هرگز اتفاق نخواهد افتاد. هرگز اتفاق نخواهد افتاد. این دیگر یک امر انجام‌شده است.
ملوانان و هوانوردان دریایی بزرگ ما قهرمانانه جنگیده‌اند تا ارتش آن‌ها را نابود کنند. آن‌ها دیگر نیروی هوایی ندارند. نیروی هوایی‌شان از بین رفته است. نیروی دریایی‌شان از بین رفته است. آن‌ها ۱۵۹ کشتی دارند؛ همه‌شان همین حالا در اعماق دریا هستند، کف دریا افتاده‌اند. رادارشان از بین رفته است. تمام تجهیزات ضدهوایی‌شان از بین رفته است. ظرفیت تولید موشک و پهپاد آن‌ها به‌شدت کاهش یافته است. به‌زودی آن هم از بین می‌رود. دقیقاً می‌دانیم بقیه‌اش کجاست.
اقتصادشان ویران شده است. تورمی دارند که هیچ کشور دیگری در جهان ندارد. و آن مردی که چند روز پیش رفت، گفت: «من می‌روم چون کشورمان تمام شده.» این را گفت. نمی‌دانم. من هیچ‌چیز را قطعی فرض نمی‌کنم، اما اوضاعشان خوب نیست.
و به لطف مردان و زنان نیروهای مسلح آمریکا، ده‌ها تن از رهبران تروریست ایران از صحنه روزگار محو شده‌اند و مستقیم به دروازه‌های جهنم فرستاده شده‌اند. همان‌طور که می‌دانید، رهبرانشان رفته‌اند. گروه دوم رهبرانشان هم رفته‌اند. و بزرگ‌ترین مشکل من این است که هیچ‌کس نمی‌داند واقعاً چه کسی کشور را اداره می‌کند. هیچ‌کس نمی‌داند؛ شاید هم این چیز خوبی باشد. اما خامنه‌ای را یادتان هست؛ همه‌شان رفته‌اند و حالا ما اینجاییم.
ما داریم کارهایی انجام می‌دهیم که هیچ‌کس قبلاً انجام نداده است. مثلاً تکلیف این کشور باید خیلی وقت پیش روشن می‌شد. حالا ۵۱ سال است. قلدر خاورمیانه. این کار باید خیلی پیش به دست رؤسای جمهور یا کشورهای دیگر انجام می‌شد. لازم نبود حتماً ما باشیم. همیشه ما هستیم. کشورهای دیگر باید خیلی وقت پیش این کار را می‌کردند، چون با گذشت زمان فقط بدتر شد.
اما ما کار را انجام دادیم و راستش مدام از رهبران جهان تماس دارم که خیلی از من تشکر می‌کنند. می‌گویم: «خب، کی می‌خواهید هزینه‌اش را بدهید؟» می‌گویند: «آقا، بابت این کار خوبی که کردید ممنونیم.» و من به آن‌ها می‌گویم: «عالی است. می‌خواهید چند کشتی بفرستید؟» می‌گویند: «آقا، ترجیح می‌دهم درگیر نشوم.» آن‌ها هیچ کشتی‌ای ندارند.
واقعاً داریم بار تمام دنیا را به دوش می‌کشیم. روی دوش ماست. و به یک معنا دوست داریم این کار را انجام بدهیم، چون خودمان قوی‌تر شده‌ایم و دیگران ضعیف‌تر شده‌اند. آن‌ها فقط ضعیف و ناکارآمد شده‌اند و ما کارهایی انجام می‌دهیم که هیچ‌کس دیگر، هیچ کشوری، هرگز نمی‌توانست انجام دهد.
...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78643" target="_blank">📅 00:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78641">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/141ace0942.mp4?token=IuaLOtbZEYxIful1e88kUvE28B_Nga3PDKq6BduA2_ftYr3lItajGiun4g1Lctys0uyRS92ktX3nu9nVtQvQ0MhTPoSHM_qjI9rLHNEYeEprhz5gEOH5XmEBnVfMVidybBqIw28bvQN2ORdJZz0ToPIaOU4y2-1kIkZqLXCCH7-WqY5Q977dQ1gy9XrpYz68ciRKQLMt7TOE3-tOcSS6oG0im3I9fNctEmAvdYPqCm14VeKNiSmUG-Ofzdt_W_R2d2Y5dFrd4lnIyt4DkrINqxHh_-RZfUEv7Zs-dHK-inwllxzs3sWQJoHdrDEQSAzDaBHovElUInyQiGltd-QbwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/141ace0942.mp4?token=IuaLOtbZEYxIful1e88kUvE28B_Nga3PDKq6BduA2_ftYr3lItajGiun4g1Lctys0uyRS92ktX3nu9nVtQvQ0MhTPoSHM_qjI9rLHNEYeEprhz5gEOH5XmEBnVfMVidybBqIw28bvQN2ORdJZz0ToPIaOU4y2-1kIkZqLXCCH7-WqY5Q977dQ1gy9XrpYz68ciRKQLMt7TOE3-tOcSS6oG0im3I9fNctEmAvdYPqCm14VeKNiSmUG-Ofzdt_W_R2d2Y5dFrd4lnIyt4DkrINqxHh_-RZfUEv7Zs-dHK-inwllxzs3sWQJoHdrDEQSAzDaBHovElUInyQiGltd-QbwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ یک کارمند ۲۸ ساله موسسه تحقیقات ضدطاعون در سیبری پس از ابتلا به بیماری که گمان می‌رود طاعون ریوی بوده باشد، موجب نگرانی‌هایی شده است.
بر اساس این گزارش‌ها، داریا شیپیلووای ۲۸ ساله در ۷ مهر ۱۴۰۵ (۲۹ سپتامبر ۲۰۲۶) به بیمارستانی در شهر شلخوف در منطقه ایرکوتسک منتقل شد و دو روز بعد درگذشت.
ده‌ها نفر که با این زن در تماس بوده‌اند قرنطینه شده و تحت نظر پزشکان قرار گرفته‌اند، اما مقام‌های روسیه می‌گویند تاکنون هیچ مدرکی پیدا نشده که نشان دهد مرگ او با عوامل بیماری‌زایی که در محل کارش با آنها سروکار داشته، مرتبط بوده است.
مقام‌های روسیه می‌گویند وضعیت تحت کنترل است و تاکنون مورد جدیدی از بیماری‌های عفونی مرتبط با این حادثه گزارش نشده است. با این حال، گزارش‌های تاییدنشده درباره احتمال ابتلای این زن به طاعون ریوی در شبکه‌های اجتماعی منتشر شده است.
مارکو روبیو، وزیر خارجه آمریکا، گفته است واشنگتن این موضوع را از نزدیک زیر نظر دارد اما در حال حاضر دلیلی برای نگرانی نمی‌بیند. دونالد ترامپ، رئیس‌جمهور آمریکا هم اعلام کرده که آماده کمک به روسیه است.
@
VahidHeadline
, @
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/78641" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78640">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BF6511lbo5d44Qp16F9flZm6nxwAz13yyazB7Y9m9U16MatXfTQpybax8s__Nmsugk3zxF5PMKFhyaLisVTrSdh3vEgDoJ-Ud_dN3Cc2jfmsNaVGuJDkxw5K3lnsQui3ABc-0klhHVrCQlGOQlQShV2ZQ_UCVaTgNcJxiTg8X14uDFE-Lj7JxofuN97lCzz3zKMJW2vleMJ5AsKB7rMLL0Pern-w7-OT7gMkoc0shVoWoqXvGau5dSZF07oCxdQAoei1kS_ivFIyXPoWH6Dv6K00XI-LvL2K4FNdG7phEEr2aeHaNbfE-CDxgTuGdV7WnqRCUAeYTRxSMnW26e085A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: رسانه‌های دولتی ایران گزارش‌های نادرستی را منتشر کرده‌اند مبنی بر اینکه یک بالگرد MH-60R نیروی دریایی آمریکا، پس از اعلام وضعیت اضطراری در شب گذشته، در دریای سرخ سقوط کرده است.
✅
واقعیت: گزارش‌ها درباره سقوط یک بالگرد نیروی دریایی آمریکا در دریای سرخ صحت ندارند. همه هواگردها و نیروهای نظامی آمریکا در سراسر خاورمیانه در امنیت هستند و وضعیت همه آن‌ها مشخص است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78640" target="_blank">📅 16:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78639">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L2NBPLzL_q0RB1K96PNBpfi_dtuRIyLG8BQqNr6Xopl2TsSmVeOLHMh6v_AQhtFmKRvolPT7JMQvHyBTtzA0cuDM0614DH5k6NY6xampho37z4aJ6zefjpj4TFAyVBMyo6-OA513iTmYLT_8-c8Cq3Dj6fg9C1gjGDHzRNeF_jwKv5kk8E7apGNfXbtoeCFKV6jNTMcoBhOm-Ri8Mhr8yKm6hi7e5hDr7H3Yt1S0g4Fjr_jC4ceEwsZnzzJDyzU-hh3sxzqIDR3hnRkV2lJtIXjeUaDYifII5f2Va5-aqMxG5i5CEF876UK-xQ-0Ary_qwFoHuhBT7EY-kgOCd4N2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا بعدازظهر سه‌شنبه ۱۴ مهر اعلام کرد گزارشی با تاخیر درباره حادثه‌ای در تنگه هرمز در ۱۳ مهر دریافت کرده است.
بر اساس گزارش یک «منبع تاییدشده»، یک نفتکش هنگام خروج از تنگه هرمز هدف حمله قرار گرفت.
در این اطلاعیه به هویت نفتکش، عامل حمله یا میزان خسارت احتمالی اشاره‌ای نشده و سازمان عملیات تجارت دریایی بریتانیا اعلام کرده است مقام‌ها در حال بررسی این حادثه‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78639" target="_blank">📅 16:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78638">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHJZpmG17JxL3mFL9dLz45gyeg3FWMRRrtFDx0NRKZFZIO3-98pIGgSjdr-WIp3fyLcQ6sv5m5P2dwNBuG72xLJujtV5DJSMOGhqX1EdiI9td2M8ajctZMNO4LJgpQFCzBfGs3Ogq58anN_x3X5YXgfY2BELjuMZdH1esGUwvBUzBpwmor_YD-xN8ydSY3lFB1hCdJQQ_YTjl3zICTXovus8LJG3_2pPiKJwQbcZC7jnKYhnsmCmCbg352l0lAI2eGlzEWG0bI0YuWHNPj9miuLXwjeAtcKf9ABSJ5XlXglLFkmytb9DJACwvh4V1QDS4qk8HZjysxVApkAO4sXInA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان هواپیمایی کشوری عربستان سعودی روز سه‌شنبه ۱۴ مهرماه اعلام کرد شامگاه دوشنبه، فرودگاه بین‌المللی ملک عبدالله بن عبدالعزیز در جازان و فرودگاه بین‌المللی نجران هدف حمله قرار گرفتند.
براساس این بیانیه، این حملات منجر به جراحت جزئی سه نفر و بروز خسارات مادی به فرودگاه‌ها شد.
شورشیان حوثی مورد حمایت جمهوری اسلامی دوشنبه از حمله به فرودگاه‌های عربستان سعودی خبر داده بودند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78638" target="_blank">📅 16:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78637">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3x8rFJFYcjvyau3i5jBUQ80SLi9prP1xpY_c1sjSovYk_xG8pIIuY8Y_nPv68zOAn6sXaDHz8oq2GAzjy-UW3JDBKwiT9T7GGOTtEVsoLqC3aXx6q4BB4aTkKf3IleARUYD5FDCm5XHZrR7RCWcrLhZIPCYKUWf6-mTZE7PUs42norckzMdHqhnaZ9FBf33sijX3mBZg5uc5LfDbim-tILODwcDQnctBzlLeopTcwZN2-j_VOpK7zKlDe-Ojkp1P4FBXYNkHCBPVouA80_6kgg8BR2myyQ0qgn6WHc2x4-FQ77D_fDkd6AfKiBsJMw5m7Zta_R6bfRpqo4IzninTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ کشور قاره آمریکا در بیانیه‌ای که روز دوشنبه، ۱۳ مهرماه، منتشر شد «اقدامات تروریستی» جمهوری اسلامی و نیروهای نیابتی‌اش در نیمکره غربی را محکوم کردند.
در این بیانیه به «تلاش‌های خصمانه ایران و نیروهای نیابتی‌اش از جمله نقشه‌های مرگبار، تأمین غیرقانونی پول، مداخله سیاسی و فعالیت برای نفوذ خارجی» اشاره شده است.
این بیانیه اشاره می‌کند که هدف از این گونه اقدامات «تقویت شبکه‌های تروریستی، تضعیف فرایندهای قانونی یا دولتی و ضربه زدن به امنیت منطقه‌ای» است.
ایالات متحده، آرژانتین، کانادا، کلمبیا،‌ کستاریکا، جمهوری دومینیکن، گویان، پاراگوئه،‌ پرو، و ترینیداد و توباگو امضاکنندگان این بیانیه هستند.
این بیانیه پس از آن منتشر می‌شود که آمریکا و پاراگوئه در ماه سپتامبر گذشته به طور مشترک «نشست مقابله با تروریسم فراملی» را با هدف همکاری در نیمکره غربی علیه «فعالیت تروریستی» تهران برگزار کردند.
سال گذشته اکوادور که متحد آمریکا است سپاه پاسداران، حماس و حزب‌الله را سازمان‌های تروریستی اعلام کرد و آرژانتین نیز در بهمن‌ماه ۱۴۰۴ نیروی قدس سپاه پاسداران را در فهرست تروریستی قرار داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78637" target="_blank">📅 16:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78636">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m3depmK2-F7zJJNMEb3GMKhSnoYB95i_M7enk3z3b6lpLjUfaOqII823oLJeRjWy-FJpSjkFhkSfMmKEWlKruO81EBmL7muDW5sMK3zUI1y9L6rYkFZZvj2yvM5it7EjeWi9elgZv8382wqQECcF63G2JBRr97w0xlrBQHwsZVpI2oH_VfwaVKtA32qa6e1H7L9WDjHG8T4XFmrReU5A0qeAZV5fnhwO57BETRIuU26gtEWY3GUFXd14ENxdNMHjOhWcKzzsSqj3zIKsW-OafWnL7_nxYXS-4QuXrGEPp6uM9bhHiDfzrBkdHUTVs-AuG-CHOpZYEaQMOjnJ6oaZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هادی عباسیان، ۳۸ ساله و ساکن شیروان، از سوی دادگاه انقلاب بجنورد به اعدام محکوم شده است.
یک منبع مطلع به ایران‌اینترنشنال گفت حکم اعدام عباسیان یکشنبه ۱۳ مهر در زندان شیروان به او ابلاغ شد.
هادی عباسیان در جریان اعتراضات دی ماه با انتشار ویدیوهایی از مردم خواسته بود در اعتراضات شرکت کنند.
تاکنون اتهام دقیق منجر به صدور حکم اعدام و مستندات دادگاه علیه عباسیان مشخص نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78636" target="_blank">📅 16:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78635">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUivCuvNQ79wcdOWYg06KdPkhYbJSgHPnQSogVA3o_F3mobHxB5rutYmzaPTw51rLnHVh7xe3KQcA_ALqYVxopEiM5TOUXaMTqxiExZM9JP4xyALqMkPi-cWLMRAww3sqhX7NvDAv1gGOhlqti_ggf9YbUikpfBjZrRq5Vpuv6whlc1bs8k4unb9254WdJBwl2C8ouobyZQH4yqLfOSM0JQyG_HOSyRK_0ouKWP8mo_EgEKnxkFeZR5f6vHmXbQH3M2iVIuB_Ftbu-oggZzCTe12sMTT10maQOsdp-Q9lZLXicwoktn-8CrBdlj8q5VNipMpO3Btgv0qN3n1FnVrDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حقوق بشر ایران از اجرای مخفیانه حکم اعدام «تورات محمدی»، شهروند ۴۲ ساله افغانستان، در زندان مرکزی کرج خبر داده است. او با اتهام «جاسوسی» به اعدام محکوم شده بود، اما مشخص نیست دستگاه قضایی جمهوری اسلامی او را به جاسوسی برای کدام کشور یا نهاد متهم کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78635" target="_blank">📅 16:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78633">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/flk35pH1JRPe85FTh1hAfpItH1o_5Ab1qiPlxm-UREK-paLtqE9WYFxrCXoEGVI264_8pgFz6Su7W7rWR1f_jTsShOKhrPTTepT8xauHKqE4EcRtLftiGKlV6PKwEICCwO91noAh-HfgvMfB8_PPtI07JyiN0sYJQmJq4Mi7xXCywg-2gnqBFu0MtWrkHSCJnLf_Npzde2YaMmE7IDJEu_UYvTZud_3tyGSWls2P2WiUGTmNaTpaBVXXfbL5MKL5gFLA-zCJdGCiLK-OBsT9Qg1hMjgLBZppYiX2GasQmp7HOZI0n-a7Mn9NBHFVlkFI5D1LdVskEyfZqE9a602LAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kVCGFUtg6269LgxKGgueTx4X6UiSSfD85m6UhcXzDFMryL20iSuv0GglZyYMV6ZXlTgkFPAub_dk3H-pavF4CIrVqUaq7XHCKRmMzeULl09uDGVgF0_j41ksNTFe0278uUKobFiuiRM7ozhfgduH0E99DBq8a-EgpGoU7sfBEMi7I51yD7Gqv8fMrt1F-iFkBo0FZrbCQ7QWrTzyUtfvi67PuYXGDhQDi9lTANQktGG6suhPngv0p4Vzvjz9iS2qQCxOX1gpo_9Z6PwehPY48sUg5Ilp_jCVs0_IdZ2-K_zvD0DK1_dP024hUscvnY6oU9TVbXxpvmpSXoD_ntjF-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وب‌سایت اکسیوس به نقل از مقام‌های آمریکایی گزارش داد ارتش ایالات متحده در پی دریافت اطلاعاتی درباره احتمال حمله پهپادی جمهوری اسلامی، ۱۲ فروند بمب‌افکن بی‌۱ را از پایگاه هوایی فرفورد، متعلق به نیروی هوایی سلطنتی بریتانیا، خارج کرد.
وال‌استریت ژورنال علت خروج این بمب‌افکن‌ها را «نگرانی‌های امنیتی درباره طرح‌های احتمالی حمله به پایگاه» عنوان کرده بود.
دونالد ترامپ، رییس‌جمهوری آمریکا، دوشنبه تایید کرد بمب‌افکن‌ها به دلیل تهدید امنیتی جمهوری اسلامی از این پایگاه خارج شدند.
این در حالی است که مارکو روبیو، وزیر خارجه آمریکا، ساعاتی پیش‌تر این انتقال را بخشی از جابه‌جایی‌های معمول نیروی هوایی توصیف کرده و گفته بود ارتباط مستقیمی با تهدید ایران نداشته است.
@
VahidOOnLine
روزنامه نیویورک تایمز در گزارشی اختصاصی به نقل از مقام‌های آمریکایی و بریتانیایی نوشته است که آمریکا پس از دریافت اطلاعات جدید درباره احتمال حمله پهپادی که گفته می‌شود سپاه پاسداران آن را طراحی کرده بود، به‌طور ناگهانی هر ۱۲ فروند بمب‌افکن بی-۱ نیروی هوایی آمریکا را از پایگاه هوایی «آرای‌اف فیرفورد» در جنوب انگلیس خارج کرد.
نیویورک تایمز به نقل از این مقام ها که درخواست کرده اند ناشناس باقی بمانند نوشته:‌ «حمله احتمالی بخشی از یک طرح پیچیده و چندمرحله‌ای ایران برای هدف قرار دادن هواپیماهای آمریکایی و کشتن شماری از چندصد نیروی آمریکایی مستقر در این پایگاه بوده است. به گفته آنها، تمام بمب‌افکن‌های آمریکایی در آخر هفته از پایگاه خارج شدند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78633" target="_blank">📅 08:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78631">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UsrNhpm0Nr5E5KyEiyowOMRcYdOsV0XWqX6qmprwmwRgAVY9ccMe0WHkU8KuFLefxcaoKCmKZ7rAZkvdzXxDA__6XurhejCIqxrlXcQbOq94uX3c1_iw8JbiLBcP_kdDUfPVHkddWKuReiJHKnMORULhh3pjhI6x398BcLbyVZY4vPRjSBUws-fIhWePxjsVmDIzaF-Z-YvFe0TT8duAXYJHwkTfB_GMYz3fZ0tLUSfwGUdAFjJBuhbVjhhAKOAcjtH_Xc4OTYgdcsGbtJikNXHX4VWjTImuYI7h2b7SfLhrjAN3wYwOb6oJoSUGX3VMmIvEzCsXUl81BsdyaV-Qxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hzbRE1g_VnPPBEj0Yi3Zs6mayGTlw8JrB4SyBlfQQxiLTHgRMi6qij5NakjLnsp88ZwDUKxuZM_TaKgn41of-JN2AD44CNc6Vzjbl9hS_l8LMGbmENsZtoBCH2C9HmkHQG8FhmFG6dNNGWqDKemh0pfksrsFHztPZdjGKiexWZBDxBMKx_brKVt2i5DlzTOOV9CrVI4Se7QA6V9vr_e2rD5nusy2dtjqXO7Q1nvS6v20gjRL_LNKDV3TqHYHypJR4ShXkuxAdggNzXFbuvebU3hCcq8Mcr3jQTFFS7aqma5br9JgKij_zenWY-ML-C62Wnxwg_i9Th2bFXiAJgnBTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در پاسخ به سوال خبرنگاران درباره حادثه امنیتی در نزدیکی پایگاه هوایی فرفورد بریتانیا اعلام کرد که ایران با این پرونده مرتبط است.
ترامپ درباره دلیل خروج هواپیماهای این کشور از پایگاه فرفورد گفت: «ما با یک تهدید مواجه بودیم و اگر قرار باشد ما را تهدید کنند، هواپیماها را جابه‌جا می‌کنیم. این اقدام تا حدی مشکل را برطرف می‌کند.»
رییس‌جمهوری آمریکا تاکید کرد: «ما افرادی را که این تهدید را طراحی کرده‌اند می‌شناسیم و آنها خودشان را با دردسر بزرگی روبه‌رو کرده‌اند.»
@
VahidOOnLine
ترامپ روز دوشنبه ۱۳ مهر در کاخ سفید و در پاسخ به این پرسش که آیا احتمال می‌دهد ایران پهپادهای رزمی را به بریتانیا منتقل کرده باشد، گفت: «نمی‌توانم این را به شما بگویم، اما اگر چنین کرده باشند، بهای سنگینی خواهند پرداخت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78631" target="_blank">📅 00:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78629">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/668a44a1f7.mp4?token=eNg0jZGU8s2gvj77mupzux6ejq1gdxRR03xR9fhFAs9vOXmnRMuy_y9hd54N6tLikUZcCKkdyxCR0j-uig1x0SNh81JISAt4S8XI5pjNvNepIIaafaxgh5S_oVy8Iu28cR8YkDckAb8OfDIU_Tp1A9-SDnJJKgvQd-Oeh-o4-oHg4uNVa56rDm3BqiSMq7byGfbHoQFgu4A0IrpYh8P-eO82MpQvA7a0K9qYtEt_2_eE96E1fUzPxd4xpQSfiMx5ynlZYGElgwurG13UvYpFeU14K6_Zva52MSfZ3mWG3dzmBJdciGx6iaufsbxW9gZtW66DjxuHTt099pfv-mq0pw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/668a44a1f7.mp4?token=eNg0jZGU8s2gvj77mupzux6ejq1gdxRR03xR9fhFAs9vOXmnRMuy_y9hd54N6tLikUZcCKkdyxCR0j-uig1x0SNh81JISAt4S8XI5pjNvNepIIaafaxgh5S_oVy8Iu28cR8YkDckAb8OfDIU_Tp1A9-SDnJJKgvQd-Oeh-o4-oHg4uNVa56rDm3BqiSMq7byGfbHoQFgu4A0IrpYh8P-eO82MpQvA7a0K9qYtEt_2_eE96E1fUzPxd4xpQSfiMx5ynlZYGElgwurG13UvYpFeU14K6_Zva52MSfZ3mWG3dzmBJdciGx6iaufsbxW9gZtW66DjxuHTt099pfv-mq0pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ هنگام ترک کاخ سفید، در پاسخ به سوال خبرنگار فاکس‌نیوز گفت: «شخصا باور دارم که ایران مسئول حمله تروریستی فلای‌دبی بوده است».
این اظهارات در حالی مطرح شد که جی‌دی ونس، معاون رئیس‌جمهوری آمریکا در همین روز به خبرنگاران گفت که هنوز مدرک مستدلی بر دخالت جمهوری اسلامی ایران در این حمله دریافت نکرده است.
در پرواز دبی به تل‌آویو که روز چهارشنبه انجام شد، کمک‌خلبان با حمله به خلبان اصلی تلاش کرد که هواپیما را با تمام سرنشینان که اکثریت آن‌ها اسرائیلی بودند، ساقط کند. این اقدام با واکنش به‌موقع خلبان و مسافران، خنثی شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78629" target="_blank">📅 00:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78628">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YA3hqxGE93ZEBbNJbQeRMyJ3rxI4-URfd-C8mjs9rUiI9-lUvBWrzm4nxlmXOtR2_xI3PofSMQr-ut-BrCkCF1bcSnLGSG6Ej6FOko1M0DVxod4fygEdZwlcbCzoY9ZZ_a3YSKmA-Ie5VyGEna-Mnq_44q_kv0plKBQitxFphkrxhRZPDWYqpN2uMOG2CtKFDyzo1bfG25cxHDOnTWqdZW2CuJAWDQtrYPnKx4ytWuc8v_-Tivx3OGFF0TWFVuYh-XgNzdzxkwtfE7VjDO9R444ym_jzOsM1U33t__pyrl-9WIHMFQag1nLYh_xqtpZGmb2Zoz8vIKC4YClEyFwF6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور آمریکا می‌گوید آنچه باعث افزایش قیمت گازوئیل شده دیگر ربطی به تنگهٔ هرمز ندارد، چرا که به گفتهٔ او، اکنون مقادیر بی‌سابقه‌ای نفت تقریباً به‌صورت روزانه از این آبراه خارج می‌شود.
دونالد ترامپ روز دوشنبه ۱۳ مهر با انتشار پیامی در شبکه اجتماعی خود، تروث‌سوشال، افزایش قیمت گازوئیل را به «پالایشگاه‌ها» مرتبط دانست و نوشت: «پالایشگاه‌های روسیه توسط اوکراین هدف قرار می‌گیرند و پالایشگاه‌های ما که در ایالت‌های آبی (دموکرات‌نشین) مانند کالیفرنیا، توسط "دمکرات‌های احمق" تعطیل می‌شوند».
اشاره رئیس‌جمهور آمریکا به گزارش‌هایی است که در روزهای اخیر از افزایش میزان خروج نفت از تنگهٔ هرمز منتشر شده است.
شرکت کپلر، ناظر بر کشتیرانی جهانی، روز ۱۳ مهر گفت که داده‌هایش نشان می‌دهد صادرات نفت خاورمیانه، بدون احتساب ایران، طی هفته گذشته، با وجود حملات به کشتی‌ها در تنگهٔ هرمز، از سطح پیش از جنگ فراتر رفته است.
با وجود افزایش میزان خروج نفت از تنگهٔ هرمز، قیمت جهانی نفت در محدوده ۱۰۰ دلار در هر بشکه باقی مانده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78628" target="_blank">📅 21:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78626">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد روز دوشنبه ۱۳ مهر یک پ نفتکش در حال گذر از تنگه هرمز هدف اصابت یک پرتابه ناشناس قرار گرفته است.
بر اساس این گزارش، این حمله موجب بروز آتش‌سوزی در موتورخانه کشتی شده که خدمه در حال اطفای آن بوده‌اند. با این حال، سازمان تجارت دریایی بریتانیا تایید کرد که تا کنون هیچ‌گونه تلفات جانی یا خسارت زیست‌محیطی گزارش نشده است. تحقیقات در این زمینه ادامه دارد و به سایر شناورهای عبوری توصیه شده است با احتیاط کامل در منطقه تردد کنند.
@
VahidOOnLine
پیش‌تر:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) روز دوشنبه ۱۳ مهر، با انتشار اطلاعیه‌های رسمی، وقوع سه حادثه امنیتی جداگانه را در آب‌های تنگه هرمز و در تاریخ‌های ۱۱ و ۱۲ مهر تایید کرد. پیشتر خبرگزاریهای فارس از هدف قرار گرفتن یک نفتکش در روز شنبه خبر داده بود و روز یکشنبه نیز ایرنا از شنیده شدن صدای انفجار در حوالی جزیره قشم خبر داده و احتمال هدف قرار دادن «شناورهای متخلف» را مطرح کرده بود.
بر اساس هشدارهای رسمی UKMTO، روز شنبه یک نفتکش حامل نفت خام حین تردد در تنگه هرمز، هدف اصابت یک پرتابه ناشناس قرار گرفته است. روز یکشنبه نیز دو شناور شامل یک نفتکش حمل گاز مایع (LPG) و یک نفتکش دیگر حامل نفت خام که از سمت خلیج فارس وارد شده و در حال گذر از تنگه هرمز بودند، توسط پرتابه‌های ناشناس مورد اصابت قرار گرفتند.
سازمان UKMTO ضمن آغاز تحقیقات رسمی درباره این حملات، به تمامی شناورهای تجاری و نفتکش‌ها توصیه کرده است با احتیاط کامل از این منطقه راهبردی عبور کرده و هرگونه فعالیت مشکوک را فورا گزارش دهند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78626" target="_blank">📅 17:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78625">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G-dupyVT5dIPvG8uB5rpzrgZv8vs_pCRum_q91x3FL2S62OLk8oqvCT2pmRq4GlvCk1sCkMc8cZYVx_n5Kw1UA0JDwb9L0Enj5v1MS2_ImL0eR_lLKuCb1PEYViMaqAvk0UesFpjJuo_KHaXQWl7z64nWSVkS25YqYfAK-30JSYJ7vykMmOjUZiRemJb7dtRqjhocIVrJnwNyhhXwO30eVcogjCwUSh2gjTicvx8ah8QVhuuFSUXg9r65iPnHYTnJAisN3E3ri8hrST7Qlqq1PoPPpaS8SHMCJ0boh2JsMAw68p0CqSAzKGrT0F_zQkuiilnE01_PPwvRkqJpY_HLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی علیرضا رئیسی از بازداشت‌شدگان اعتراضات دی ۱۴۰۴ را اعدام کرد
- علیرضا رئیسی سحرگاه روز دوشنبه ۱۳ مهرماه همراه با علیرضا سپاهی، از دیگر بازداشت‌شدگان اعتراضاتدی ۱۴۰۴، در زندان دستگرد اصفهان اعدام شد.
- روز گذشته برخی منابع خبری از فراخوانده شدن خانواده علیرضا رئیسی به زندان دستگرد اصفهان خبر داده و گفته بودند این زندانی سیاسی برای اجرای حکم اعدام به سلول انفرادی منتقل شده است.
- علیرضا رئیسی فرزند دختر عموی جاویدنام رامین رئیسی از کشته‌شدگان اعتراضات دی۴۰۴ است. رامین رئیسی ۱۹ دی‌ماه با شلیک مأموران حکومتی در جریان سرکوب اعتراضات کشته شد. پیکر وی را ۲۸ دی‌ماه به خانواده تحویل دادند که در «باغ رضوان» اصفهان به خاک سپرده شد.
- علیرضا رئیسی روز پس از خاکسپاری رامین رئیسی بازداشت شد. خانواده علیرضا تا ۲۰ روز پس از بازداشت فرزندشان هیچ خبری از او نداشتند. او طی آن سه هفته زیر شدیدترین شکنجه‌ها و فشارها برای اعتراف اجباری علیه خود قرار داشته و حتی تهدید به تزریق آمپول هوا شده بود.
- علیرضا رئیسی و علیرضا سپاهی از متهمان پرونده «میدان علیخانی» اصفهان هستند که به اعتراضات شامگاه ۱۸ دی مرتبط است و نهادهای امنیتی مدعی کشته شدن چهار بسیجی و مأمور یگان ویژه در جریان این اعتراضات شدند.
- در پرونده «میدان علیخانی» ۱۲ شهروند به اعدام محکوم شدند. با اعدام علیرضا رئیسی و علیرضا سپاهی، شمار اعدام‌شدگان متهمان پرونده «میدان علیخانی» به هفت تن رسیده است.
KayhanLondon
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78625" target="_blank">📅 16:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78624">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p_EAzl4hns6Mx1Pd8NOejSj0bd8E570PEK0Q6vbA46pCaU3dv31cZIsuhsfzP4QTsWebm84sanHUZg3vRa1uz5DKgeN6RqNV1xMBYAtVqynKTEYzDqCxibBXxiGo9XTszZTd1a9XAu5gknTMWViP4TroT_rrfZlphIiDrIevgZVLqMkALbmeuUazlZFV1nTTqXatGhctPSibbac93yeKInIHChp7LZaoOGjcg_D6Xo5qlLFgaVEE1x8hvUPGHAbS4p4yfCpaLgLy5qrzvnP_h_kKacumSccMDWAGvrDSr-2czBUjPoh1ryOFjuFwIzFUYvKluVALWx-nQJ7JK6T6Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی علیرضا سپاهی از بازداشت‌شدگان اعتراضات دی ۱۴۰۴  را اعدام کرد
- خبرگزاری «میزان» وابسته به قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام علیرضا سپاهی بادجانی، معروف به علیرضا سپاهی، در سحرگاه روز دوشنبه ۱۳ مهرماه ۱۴۰۵ در زندان دستگرد اصفهان خبر داد.
- وکیل علیرضا سپاهی روز گذشته با اعلام خبر فراخوانده شدن خانواده علیرضا سپاهی برای ملاقات با او و انتقال این زندانی به سلول انفرادی، از خطر اجرای حکم اعدام وی خبر داده بود.
- علیرضا سپاهی پیش از اعدام و به صورت تلفنی با نامزدش عقد کرد. مهشاد کشانی، دانشجوی ۲۲ ساله ساکن اصفهان، نیز در اعتراضات دی۴۰۴ بازداشت و به پنج سال حبس تعزیری محکوم شده و در زندان زنان دولت آباد اصفهان محبوس است.
- علیرضا سپاهی قرار بود سحرگاه سه‌شنبه ششم امرداد ۱۴۰۵ به همراه ابوالفضل سپاهی بادجانی -پسرعمویش- و امیرحسین صفری حسین‌آبادی در ملک شهر اصفهان و در ملاء عام اعدام شود اما پیش از اجرای حکم به علت استرس دچار سکته قلبی شد و اجرای حکم اعدام او عقب افتاد.
+- علیرضا سپاهی چهارمین شهروند بازداشت‌شده در اعتراضات دی۴۰۴ است که طی هفته گذشته و پس از صدور بیانیه ۴۶ کشور در محکومیت اعدام‌ها در ایران، احکام اعدام آنها اجرا شده است. سیاوش جمشیدی خیرآبادی شنبه ۱۱ مهرماه در شهرکرد و علی همتی سیستانی و مجید نیک‌اندیش روز چهارشنبه هشتم مهرماه در مشهد اعدام شدند.
- پرونده معروف به پرونده «میدان علیخانی» به اعتراضات شامگاه ۱۸ دی ۱۴۰۴ مرتبط است که در محدوده میدان علیخانی، میان ملک‌شهر و کاوه اصفهان رخ داد. نهادهای امنیتی جمهوری اسلامی مدعی شدند در جریان این اعتراضات چهار نیروی بسیج و یگان ویژه کشته شدند.
- با اعدام علیرضا سپاهی، شش متهم پرونده «میدان علیخانی» اعدام شدند. عرفان اسفندیاری و گل‌محمد محمدی ۲۸ تیرماه در زندان اعدام شدند. ابوالفضل سپاهی و امیرحسین صفری در تاریخ ششم امرداد در «میدان علیخانی» در ملاء عام به دار آویخته شدند و قائم حسینی نیز ۲۹ امرداد در زندان مرکزی اصفهان (دستگرد) اعدام شد.
KayhanLondon
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78624" target="_blank">📅 16:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78623">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EkJVHqrP5JzzOe1hv2OIjImO0_Hn0LMjXx0URh2dl5zhpvsLscQBZtFuO13OlkpFg9jDskKI7nqSlu_UFyHyb2J0DYrsAjctjcsFdkC-DWjY9tg-r0d9FdDNVSQeSTmEKqj4UPViSm5GL0fY7TGnpS6p5CqMtile1-ju_dd0CwynyAkGXnclh2uXS8IxBsHb5D83r7ihutHuGG--7xUCPcMHesKwhi7ikjCkkM0J_GXVDAdZdCIv-pCnihE6YyrMMAI3slWX-DwzEPqQlEdnlxlBpMLBWUQsYI35gqvhXHuqPvlL0ki5j-65CXgeTviEz_uboo_TXMxM4B3qhRch1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نفت ایران در پی افشا شدن توقف کامل بارگیری نفت خام کناره‌گیری کرد
معاون ارتباطات و اطلاع رسانی دفتر رئیس‌جمهور ایران روز یکشنبه ۱۲ مهر اعلام کرد که استعفای محسن پاک‌نژاد، وزیر نفت، مورد پذیرش مسعود پزشکیان قرار گرفت.
مهدی طباطبایی در شبکه ایکس نوشت که حمید بورد به به عنوان سرپرست وزارت نفت منصوب شده است. بورد به عنوان معاون وزیر و مدیرعامل شرکت ملی نفت ایران فعالیت می‌کرد.
کناره‌گیری پاک‌نژاد از وزارت نفت در حالی رخ داده که محاصره دریایی ایالات متحده علیه ایران که از ۲۳ تیر ماه دور دوم آن آغاز شده است، صادرات نفت ایران را به‌شدت کاهش داده است.
وزیر خزانه‌داری آمریکا روز نهم مهر اعلام کرد: «ایران در ماه سپتامبر صفر بشکه نفت خام روی نفتکش‌ها بارگیری کرد» و افزود دولت دونالد ترامپ در حال قطع «حیاتی‌ترین منبع درآمدی» جمهوری اسلامی است.
داده‌های اولیهٔ ردیابی نفتکش‌ها که بلومبرگ منتشر کرده و همچنین اطلاعات شرکت‌های کپلر و ورتکسا نشان می‌دهد در سراسر ماه سپتامبر هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
اسکات بسنت هفته گذشته در گفت‌وگو با شبکه فاکس‌نیوز اعلام کرد برآورد دولت آمریکا این است که حدود ۱۵ میلیون بشکه نفت ایران همچنان در مسیر تحویل، عمدتاً به چین، قرار دارد و پس از تحویل این محموله‌ها تهران «چیزی برای تجارت در برابر هیچ چیز دیگری» نخواهد داشت.
محسن پاک‌نژاد ساعتی پیش از استعفا، بر اساس ویدئویی که رسانه‌های ایران منتشر کردند، گفت درآمد ناشی از نفت فروخته شده «وصول» می‌شود و این روند ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/78623" target="_blank">📅 21:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78622">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2QOih1UXqxgqAXcFjsOsKQl2cXSEo7lTnyvO69GOxVTFNg4djD2K3hf-ekcOn18x9l4TYaMNvSE14kTCrWWEAzzGVgYMJZNt15uOIUX5eiZd4rZNRHsiSYhKM36XDH5X39B_DTDbZ8V0YSX5bD2TbGK32YV32RqlVBrcoeDF7CeLrVZlxvG9dzGMYpbX9EObVMCN-41doXElQcw0ykW6_c-thB-fgErMtZrcozDVMbHilsn1GRw76E0sCxaMHUy8sUkan5y7n45ny7SnLPt8pRnsXYWmJHTy7GORlGOXQDEzV-gYGV79wQOfowfrova-WRVvKCqxJT8FcXkCCuahg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار ارز و طلا در یکشنبه ۱۲ مهر همچنان در مسیر صعودی قرار دارد. قیمت دلار آمریکا با افزایش نسبت به روز گذشته به ۲۷۳ هزار و ۱۰۰ تومان رسیده است.
دلار در ساعت ۱۵ روز گذشته ۲۶۸ هزار و ۵۰۰ تومان بود و به این ترتیب در کمتر از یک روز ۴ هزار و ۶۰۰ تومان، معادل حدود ۱.۷ درصد افزایش قیمت داشته است.
یورو نیز از ۳۰۲ هزار و ۲۰۰ تومان به ۳۰۷ هزار و ۴۰۰ تومان رسیده و پوند انگلیس با افزایش از ۳۵۲ هزار به ۳۵۸ هزار تومان معامله می‌شود. درهم امارات نیز به ۷۴ هزار و ۳۵۰ تومان، یوآن چین به ۴۰ هزار و ۸۴۰ تومان و لیر ترکیه به ۵ هزار و ۶۴۰ تومان رسیده‌اند. قیمت تتر نیز ۲۷۱ هزار و ۶۰۰ تومان اعلام شده است.
در بازار طلا و سکه نیز روند افزایش قیمت ادامه دارد. بر اساس نرخ‌های منتشرشده امروز، هر گرم طلای ۱۸ عیار حدود ۲۶ میلیون و ۳۸۵ هزار تومان و سکه امامی حدود ۲۷۳ میلیون و ۸۳۰ هزار تومان معامله می‌شود. سکه امامی نسبت به نرخ ۲۷۰ میلیون و ۹۰۰ هزار تومانی روز گذشته حدود ۲ میلیون و ۹۳۰ هزار تومان افزایش داشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/78622" target="_blank">📅 15:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78621">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/choskpOIGDTmpCE6yRgh02Io6dt0izxGtWgXcP6Stv7eQdsqv0gkH3VqYbNj2vVmPxKU4Gpsl9jT5Qw_NqvJyrxTkWzjaM3Oy_0CzHIZYDQWWvq41JeaLn6PMsRuL44poCHWYl1xCpPtectWlxjBqR6gA4PAjMQemUGznyHJO6Tb_5sK77Dv6DLs2t_DkhdU1JE9QfHUYqU4PqZE0om5UU15oYIa8ucoYDmJGQ7W1RQ-l5mKUI1WDekOHJBCXk4cs_t7MGYPfkIGWT2bKcXXTw_3ew0EwQF0stQ5J5UpB39kjV25zB4Kbt6BgZDK-rn52nq69PcPaeSrs6nFh_INYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یکشنبه ۱۲ مهر با اشاره به دیدارهایش با مقام‌های کشورهای منطقه گفت این رایزنی‌ها «بسیار موثر، محترمانه و دوستانه» بوده است.
او افزود: «ما مسیر جدیدی برای ایجاد اعتماد میان کشورهای همسایه و جمهوری اسلامی ایران آغاز کرده‌ایم و به‌خصوص در حوزه خلیج فارس، این مسیر را به خوبی طی می‌کنیم.»
وزیر امور خارجه جمهوری اسلامی همچنین گفت کشورهای حوزه خلیج فارس در این روند با ایران همراه هستند و به گفته او، «اراده مشترکی برای ایجاد صلح، ثبات و امنیت در منطقه خلیج فارس، با مشارکت خود کشورهای منطقه، شکل گرفته است که اکنون به‌طور جدی دنبال می‌شود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78621" target="_blank">📅 15:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78619">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uPq2S0wZKT5ULnqZABN4hL4VxnF_rKgp_P8UTuKB_ymYn2R-TkiL_onpjg1LaAVrKM9xieQvkUJ0EcrjHloPSJy0uszYngiRgbhCT0yUHzZwO27bc7FUYTZ7_1_5ME09K97vX1YtAmtqW7Ub6w1OWW3YHo_hBSihPJGsc8IVaTln1MDt2LtsD_LjXLVgkMrOyADpBCYapWxw8QGJebIyxontXaJYaQDut08MxRQ0pn9sfkfHLEV66C-GrQXmoRTX_mH7yirAApRjIJXqDws1rFPeDS1TXJ_hayz7lb8yldiPGLyceTSyLB3McxtJ_NIzW9XS3bcMpF32j1ObW05GbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2e9c326279.mp4?token=h9hXoZUMzTiJQK1fHo6JRVYeAEbiL97XORxAWdh5PLjI5eZg9QLMJmjfKv9f4Prmz_R6IvO0LNHX7GLoUX6naRP3-DTpptqQO5yUIxmsbnWcUlmNlgQkULwGPA0BYIq_GgLWS7LAam1V_MXX7y8DwanoZsfL4nCPidLDpYoY7CsqOtgX7eIoCwWJMiNl9Zyr4rFNaZUO3CilgHp9hR-PGxCVw_uaRkIK3AShGiWlNW77JXQepQar83xe9W8xmA6GOa2PiQxAAcY_9cLYl3dTFNavmhAqL9I6ZOlbhtOH9OfH8aPwu5aUBqKjrPZHjoSbOiLtOlZoBD3oU8lMzkdVbA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2e9c326279.mp4?token=h9hXoZUMzTiJQK1fHo6JRVYeAEbiL97XORxAWdh5PLjI5eZg9QLMJmjfKv9f4Prmz_R6IvO0LNHX7GLoUX6naRP3-DTpptqQO5yUIxmsbnWcUlmNlgQkULwGPA0BYIq_GgLWS7LAam1V_MXX7y8DwanoZsfL4nCPidLDpYoY7CsqOtgX7eIoCwWJMiNl9Zyr4rFNaZUO3CilgHp9hR-PGxCVw_uaRkIK3AShGiWlNW77JXQepQar83xe9W8xmA6GOa2PiQxAAcY_9cLYl3dTFNavmhAqL9I6ZOlbhtOH9OfH8aPwu5aUBqKjrPZHjoSbOiLtOlZoBD3oU8lMzkdVbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، روز شنبه، با اشاره به تحولات جاری میان تهران و واشنگتن به خبرنگاران اعلام کرد که به‌زودی درباره ایران تصمیم‌گیری خواهد کرد.
رئیس‌جمهوری آمریکا با تاکید بر اینکه «ایران درهم کوبیده شده است» گفت: «تصمیمی است که درباره ایران خواهم گرفت. تنها مسئله این است که یا از راه آسان خواهد بود یا از راه سخت. ما این موضوع را یا از راه آسان حل می‌کنیم یا از راه سخت.» او در ادامه افزود: «ضمنا همان‌طور که می‌دانید، ایران عملا از هرگونه برنامه‌ای برای دستیابی به سلاح هسته‌ای دست کشیده است.»
@
VahidOOnLine
پیت هگست، وزیر دفاع آمریکا، روز شنبه، ۱۱ مهرماه، از پاسخ به سوال‌ها درباره اعزام ناو جدید خودداری، اما تأکید کرد که رئیس جمهور آمریکا «مصمم است» از دستیابی حکومت ایران به سلاح هسته‌ای جلوگیری کند.
هگست که روز شنبه با خبرنگاران سخن می‌گفت از پاسخ صریح به این پرسش که آیا جنگ با ایران تا پایان سال جاری میلادی، سه ماه دیگر، به سرانجام خواهد رسید خودداری کرد و تصمیم در این باره را با دونالد ترامپ دانست.
روز شنبه، چند رسانهٔ خبری آمریکا گزارش دادند که پنتاگون در حال اعزام ناوگروه ناو هواپیمابر «تئودور روزولت» و یک گروه آبی‌ـ‌خاکی تفنگداران دریایی به خاورمیانه است؛ اقدامی که در صورت اجرا شمار ناوهای هواپیمابر آمریکا در منطقه را به سه فروند می‌رساند.
وال‌استریت جورنال به نقل از مقام‌های آمریکایی بدون ذکر نام آنها نوشت این اعزام، همراه با گروه آبی‌ـ‌خاکی «ماکین آیلند»، بین ۹ تا ۱۰ هزار نیروی نظامی دیگر به منطقه می‌افزاید. به نوشته این روزنامه، «تئودور روزولت» به ناوهای هواپیمابر «جرج اچ. دبلیو. بوش» و «جرج واشینگتن» خواهد پیوست که در منطقه حضور دارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78619" target="_blank">📅 15:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78615">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LL4k6Ii6AJU_Wfz5R0XgyMzma6wWqU3e_mTb6sEG3P10mkPsBKuVfaTbbIGDsw-NkjWOImSHQhW8YspRvRHC2bFsbc7-T_m6gokfCD98zN49WcFfAXdguhz69H1knoIDiM_cGKBBECd1I_wgP8UBGQU33jqY3W2K3T9UyI5PChuY-oAern7ePFhhdurMN5-q8aH6Wm8F-ZDeKf83Z4HZXBml9cgZdeYNwSIBe2ngfzAIofr51XXUuBeBTiVgFuVCKdcGwbk4b9JW9Oso6e25UwWqLI-c10imF3qDjZ_NqnnhfrnhSzBaBoFxjgB_aaEyBOjUODKll-GC3qsJ2vuBfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uU5eXTV-6GH3L-SFhHhlRjDeO6SBqC8r_7Y7eL1U1UAgdf2nUgRCZWNIDsL7pw7MRZlpjUsl2z27gwbhFy7_a2f0yjNfYjoNwUFSv_QyikgdXVgebMeqtoraISnTjybfztcmcBNGfsdrYQJFZBhW1oCVCjfRAFFhlAeoJrkP4zyDwdCWNsqNNploHMIUvACiOxjoOMTd7hKnsdGbRof7W48QPqougKfBGKVIKVj5FLQWzXeLsIm4kr4d7yPH1Bap3xGLD_ll5fsIfATUSM5XiALFOhe1JOuFPTwnZlmvN12ozAJEwCHRuGFETPbZrYl0Z4geBLizqFiFPgKJGaH7HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bde04Jfish6DH96pmj4w-yfci9V7v2Wh4JeB-TI4AE6Y-BLxo4YY--umiXXIGgsDuGYK_POOThr8YVNkFF1zuDeLPNY-xNGUXrI85gvXyFCDT6FlWM_trJKwOoX79sn38aHWR5U6M03cmCogY38Es1Aq2WdPwJbCv_2UU3YZ6Mi-zK8UM-ooPtBbYrJGhbIqq5yaxU1ywFDnZiUZ0b20c56DIcDfyRaatFTxgWdh_iUQ5Dinhm49s9nf1gbfvIoiAFW-7XIQUFItQ7l1f0JG_FzFAle4C9YZWruybWf-2ynoiOUdVEBgSu2anz2e-RXy_XXaVfdQsvu3Zw4_i8kQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GOeR_CFIyWuKdUXv_jvLbe5_GYGUQp_8wmriBy0sR2ED2vwEMheDO9kDfNMre85-LZmKSrwxAvL-MtpNKK0qKzgiUI-nBMVu8cylTR0yymSKcH4-oiOhdldPtGmMHbHnI5-FhG6Q8peDSDc2JUuCPtim8meybPCCHm9NllBe-svQRhLBZv5_GddPpj8UXVkzrGdUr-dQ_gFC2wwHxQPAwQhWySexvAqtr2qL7VLuKAHUm1Q0YLewhNWTbQqvzHxt7EkmDSLlx2YuaErdBhxkkJipwQvX_VIvQxPqq_Ufg03IUjO2a9SX_WgSQzDFXTgS0kEubD7iH8Fj4yJ4zkVJzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
صدور و تایید احکام اعدام برای سه زن در پرونده‌هایی با اتهامات امنیتی، نگرانی‌ها درباره استفاده گسترده‌تر از مجازات اعدام علیه بازداشت‌شدگان و متهمان پرونده‌های سیاسی و امنیتی را افزایش داده است.
🔸
محبوبه شعبانی در پرونده‌ای به اعدام محکوم شده که امدادرسانی و انتقال معترضان مجروح از جمله اقدامات منتسب به اوست. مژده هاشمی بازرگانی، که حکم اعدامش در دیوان عالی کشور تأیید شده، از شکنجه، اعتراف اجباری و محرومیت از وکیل انتخابی سخن گفته است. سودا ابراهیمی شمس‌آبادی نیز با اتهاماتی از جمله فعالیت رسانه‌ای و ارسال تصاویر برای رسانه‌های فارسی‌زبان خارج از کشور به اعدام محکوم شده است.
🔸
هر سه زن با خطر اجرای حکم اعدام روبه‌رو هستند.
@IranRights</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78615" target="_blank">📅 15:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78614">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ahIGpVWT9TmWRQtSuHQ6iy1rxpadpk4VSRHf85yO_WkdBoVpZYsGcRk3k-f0JRFENI9bBZPKYHwST2vcClcPpn4eIUFdNbihHpOuOpKPEw_rBldTJf-sGVqMyEcIJ7fZ2NwuftajAmEP-ZwOkXQXqh52y0WmOs2hbV-JJnIb5mnjFR-ya_4rfOzcQIhV77SYl3Eau01_oP_-YJVsuqRtT9g08-DWigH2dYMBYXvgz7woXZYrLZFfeVisWg3M9911bNMevDaijuPLX6bHjR7rM-_VZi86ThQMJwZj0nJjEfHeVyj0xcPe9VGe509Afc_9oAvXrdO0Vek-BfH4BkJO0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس روز شنبه یازدهم مهر از شنیده شدن صدای انفجار در تنگه هرمز و هدف گرفته شدن یک کشتی تجاری در مسیر عمان خبر داد.
فارس مدعی شد، نفتکش «اور وینست» که تحت اسکورت آمریکا قرار دارد، هنگام ورود به تنگه هرمز سامانه رهگیری خود را خاموش کرده بود. این خبرگزاری دولتی نوشت، این دومین هدف‌گیری یک نفتکش در تنگه هرمز در روز شنبه است.
این خبر پس از آن منتشر شد که خبرگزاری مهر ساعتی پیش از شنیده شدن صدای انفجارهایی از سمت دریا در جزیره قشم خبر داده بود و احتمال ارتباط این صداها با شلیک به «کشتی‌های متخلف در تنگه هرمز» را مطرح کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/78614" target="_blank">📅 20:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78613">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sha3lRidoC6Zyk1s4pRB6ak96BIhGp91XMZxgIlxqXyDC5L1aVedd39tBFt0VvdvIE8vty82HbcduD8bZRUC4jU8YCXhrWiw8rewimf_zhNnMSIl2O_Z17BQxpnJGL0oflJXKr2TgZCtEyHVSU09M8w1y-LMZLWb3cp6ix80eYPS7DLrquCSPrjKUNvWD42GTq9Om_BHfIzOXt3x6Oc8oDP0f9NHdVUd9z-90w1iE_vk9FHSuu-0Oja_YbwyP_bXzwr0sL_mgYqwDGG1a83S1uGUmuuVKNLUuj9-kU5FV-I6FOml8GDq6ZES9QsVJWnx_aq8_ERTtfrYwy_PXvokQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی انتشار گزارش‌هایی از شنیده‌شدن صدای چند انفجار در جزیره قشم در عصر شنبه ۱۱ مهرماه، خبرگزاری مهر نوشت این صداها مرتبط با اقداماتی در خلیج فارس و تنگه هرمز است.
این خبرگزاری بدون استناد به منابع رسمی نوشت «هیچ اصابت یا حادثه امنیتی در پهنه سرزمینی جزیره» رخ نداده است.
خبرگزاری مهر در عین حال این «احتمال» را مطرح کرد که صداهای انفجار شاید به «شلیک به کشتی‌ها» در تنگه هرمز مرتبط باشد.
این در حالی است که همزمان، تصاویر متعدد و گزارش‌هایی در شبکه‌های اجتماعی منتشر شده که یک قطعه بزرگ و استوانه‌ای‌شکل را در محدوده‌ای شهری در قشم نشان می‌دهد که ظاهر آن به بخشی از یک پرتابه نظامی-دفاعی شبیه است.
گزارش‌های تأییدنشدهٔ دیگری در شبکه‌های اجتماعی نیز حاکی است که پیش از سقوط این قطعه، صدای عملیات پدافندی و چند انفجار در قشم به گوش رسیده است.
مقام‌های رسمی تاکنون توضیحی دربارهٔ تصاویر منتشرشده و این حادثه در قشم ارائه نکرده‌اند و رادیوفردا نمی‌تواند جزئیات گزارش‌های منتشرشده را به‌طور مستقل تأیید کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78613" target="_blank">📅 20:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78612">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O3hUYJ-47eP0wHfGVh8BhVDqT6UT48S9zpXYxG_-EL_JG9gcPsbFqa6tLkjFncZqlshKd5NzBzPjtCVy2fpjiCLTn67L4bIBx18bJth3v71ae7mfqMn4qbC3uvKczYylW39gAYWUgaFvXqxwCFP16lUocGMRENZwV-3-apV-lCIemcdAhnHTNNI5w6aTgwLkZh_OXxfYA93ZDwvYAcorDolv7RePh28s9i59qvpeqhWVAzXVF78s1VD7RqFb3MKnHNd4x5IHRcmhMNfEyx_lm2yzfo0aNticATwePxPn4lBIwkz-lGZmmLbY2fHCeZ1kxlvpB0sP1gw2t3jzAIShpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی از قشم  حدود ساعت ۱۶:۳۰:  صدای جنگنده خیلی نزدیک اومد صدا زیاد قشم  همین الان قشم موشک شلیک کردن  16:34 دقیقه   وحید جان از قشم سمت اسکله بهمن موشک شلیک کردن صداش خیلی وحشتناک بود معلوم نیست شلیک کردن یا جنگنده بود ولی هرچی بود صداش خیلی زیاد…</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/78612" target="_blank">📅 17:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78611">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QagXR3l07uGttVIslwxfR06vu9k-TmE0_8hdK20-_LnXqGVm1q3q9TX3aIF0-rmcnlRI7RgevZvmwBGxmB5AjXJZjpxmr3gf-6Qj6b6c6DrRHIWxLitF8Uv5PBG5L4ynYzbLX8Ba8R4LiqxxVfAeRm6Qwqr8W7WKBSpEYKNpLUm2d8O_KCpqVoNa7lcLTVpm3mWGo3fh27ebz_zT-H4K_qhchVZnQuGi0aabCd7RbTA_zAXUENmyBGJIX_j0vpxq87gD6KkWhsvE0MZmXECERqzMLVilpqGFaq3L-dsX4DygZ_wN8jwtljW109PzwQuobrZNuBrBdTWFzPe1WclpDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند کاهش ارزش پول ملی ایران روز شنبه ۱۱ مهر ادامه یافت و بهای دلار آمریکا در بازار آزاد برای نخستین بار از مرز ۲۷۰ هزار تومان عبور کرد.
بر اساس نرخ‌های اعلام‌شده در ظهر شنبه، قیمت فروش دلار به حدود ۲۷۱ هزار تومان و یورو به بیش از ۳۰۵ هزار تومان رسید.
این در حالی است که روز پنج‌شنبه قیمت دلار در بازار آزاد حدود ۲۵۸ هزار تومان گزارش شده بود؛ به این ترتیب بهای دلار در فاصله دو روز بیش از ۱۳ هزار تومان، معادل حدود پنج درصد، افزایش یافته است.
افزایش قیمت ارزهای خارجی در حالی ادامه دارد که بانک مرکزی جمهوری اسلامی روز چهارشنبه از برنامه‌ریزی برای عرضهٔ دو میلیارد دلار اسکناس به بازار خبر داده بود.
قوه قضاییه نیز از برخورد با کانال‌ها و صفحاتی که آن‌ها را عامل «قیمت‌گذاری کاذب ارز» می‌خواند، خبر داده است.
اقتصاد ایران همزمان زیر فشار جنگ با آمریکا، تحریم‌ها و محدودیت‌های فزاینده بر تجارت خارجی ناشی از محاصره دریایی قرار دارد.
ارزش پول ملی ایران، از ۲۳ تیر، زمان آغاز محاصره دریایی آمریکا علیه ایران، تاکنون بیش از ۳۱ درصد کاهش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78611" target="_blank">📅 17:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78610">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBr8g38QH4D2lFG43Gb37Qwqe5nvFohlEQT5D02T4LAw-COJtGo9RkzPgwySypsVXW_xSG7FIPICO3sR5tvM7l_G0SivIqB8PRaKcD7POhIhsUG-e22FRaaKY7OI3rsUGB_x21tz09_5QGFgqUFDRXbrivN27xYPwUe43Z2FJlGZE055ITeQdtxtWsZ4nrdtWa-MeUkabUoVEbqCR7W57zVKAaSw_p-rkf5yrRpwDzUtQA5STyOwdBEQeywDILWiMPmVcZleE46bhPF_xyoc9ox4FaXnfnV122ntJTka_-QavILkpSG4akoBQOAXThXfuYzOQk-nP_Ue0UhmkXKPdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا در گفتگو با رسانه آکسیوس،‌ با تاکید بر تاثیربخشی محاصره دریایی ایران اعلام کرد، ایران برای نخستین بار از زمان آغاز صادرات نفت، در هفته جاری هیچ نفتی برای بارگیری و انتقال از طریق دریا نخواهد داشت.
او همچنین با اشاره به کم اثر شدن نفود نیروهای مسلح جمهوری اسلامی در تنگه هرمز افزود، آمریکا عبور ۱.۱ میلیارد بشکه نفت از را از این آبراهه تسهیل کرده است.
وزیر خزانه‌داری آمریکا همچنین گفت واشنگتن در حال منزوی کردن ایران «به شکلی بی‌سابقه» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78610" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78609">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vt-XshWbZAWXAfvLyaimlncsyBJCoKjGIlfhe3f8y4WPpFl-RYV2CELVWp0amPMnO4J8PP8ifVxsyXZk3mn8JHYZ1IZ2fsj9VYbqAY44jWcTGY0pThjtoKD-xybN6ydU_6eMiSXi1V6A75NLAFJUZpaqCUgSweeMKk8Ez6FdWxCdvtu-BLFu6X2XUhhCUT8Hnd8LzU3Alqv67TSNd4TxJryEku5h5gjxFSRUVx_5kEgfyut5a_12mTj8L4zlTPwFs8HUUErPnQ9xU9BFS_CLd7MFbFk2JkzGEoMNu6br-akjr_B22lXb0vH1c9nh_Kn6t5nr1SvgK88NKGmfU1tD7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس مبارزه با تروریسم بریتانیا دو تبعه ایران را به برنامه‌ریزی برای حمله‌ای تروریستی علیه جامعه یهودیان منچستر متهم کرده است.
پلیس بریتانیا روز جمعه ۱۰ مهر ۱۴۰۵ این دو نفر را «سلام احمدیان»، ۳۶ ساله و ساکن لیورپول، و «رحمان صالحی»، ۳۴ ساله و ساکن سالفورد، معرفی کرد.
این دو نفر روز یکشنبه ۲۹ شهریور در منچستر بازداشت شدند و روز جمعه به اتهام انجام اقداماتی در راستای تدارک عملیات تروریستی تفهیم اتهام شدند.
قرار است احمدیان و صالحی روز شنبه ۱۱ مهر ۱۴۰۵ در دادگاه حاضر شوند.
پلیس می‌گوید این دو نفر برای پیشبرد توطئه ادعایی خود با فرد سومی در خارج از بریتانیا، که احتمالا در ایران حضور دارد، در تماس بوده‌اند.
به گفته پلیس، احمدیان و صالحی از طریق پیام‌رسان‌های رمزگذاری‌شده با این فرد درباره تهیه قطعات لازم برای ساخت یک بمب دست‌ساز گفت‌وگو کرده‌اند.
این دو نفر همچنین متهم شده‌اند که فایل‌های ویدیویی آموزش ساخت و مونتاژ بمب دریافت کرده، مایعات و تجهیزات مورد نیاز را تهیه کرده و برای شناسایی و بررسی اهداف احتمالی حمله از اینترنت استفاده کرده‌اند.
«ویکی ایوانز»، معاون دستیار کمیسر و هماهنگ‌کننده ارشد پلیس مبارزه با تروریسم بریتانیا، گفت این بازداشت‌ها نتیجه تحقیقات مشترک پلیس مبارزه با تروریسم و نهادهای امنیتی بوده و به خنثی‌شدن توطئه‌ای علیه جامعه یهودیان منچستر منجر شده است.
او اتهام‌های مطرح‌شده در این پرونده را «بسیار جدی» توصیف کرد.
این توطئه ادعایی هم‌زمان با اعیاد مقدس یهودیان، سالگرد حمله تروریستی سال گذشته به کنیسه «هیتون‌ پارک» و افزایش گزارش‌ها درباره حوادث یهو‌دستیزانه در سراسر بریتانیا خنثی شده است.
دولت بریتانیا دو روز پیش از اعلام این اتهام‌ها، جمهوری اسلامی را به دست داشتن در تلاش برای خرابکاری در پایگاه نیروی هوایی سلطنتی «فیرفورد» متهم کرده بود.
«دونالد ترامپ»، رییس‌جمهوری آمریکا، روز چهارشنبه ۸ مهر ۱۴۰۵ در پاسخ به پرسشی درباره نقش ادعایی جمهوری اسلامی در حادثه امنیتی اطراف این پایگاه گفت واشینگتن در حال بررسی موضوع است.
پایگاه فیرفورد پیشتر در اختیار نیروهای آمریکایی برای انجام حملات علیه مواضع جمهوری اسلامی قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/78609" target="_blank">📅 17:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78607">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZdVozMOn9hhlbXWW7mZ0Y_FlkeN6iXN2vi1AVjrOhRcdwJGmyRIA7iqRmt3W4QrhS-PCFjWtBdp29XvaPHYkkO5BVDG4J_ZgY4LqKJDSjiEe4OMd0XzESdMxJzraO7cmaSov-FMB2PNybaec5s1XJGjRVJw5GnDUlF2sXZIeexNmUnn2VXowLIUfe-ft-x1xMg7XaJ-xOUq8_SGVzdi2pxoojF7G6V2Tg1MNFsXXFKfOb2_VZT2qggJrQXqV4k1KuURhodLD14aQhD9r02ZED67ruN7Yyw_Y2MA9_u8Tusb1Jbv60AFqNUJstlbHVfJOBGr_BXdcke7qGPQoYQ5mNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D8YhSSJd3nwNXJfRw5kF3CbxOPUF5TifuX-gK-WmL40y14JNOSAo5Vftn7pCWzcOfpPRP9JO-lutptrEkiEqJ9ImCjmYP13_UmZnHmglL7e8sdbsFfNhOsbSlS9FdDw4FdA-fH92y6YEiyjWBu1CpjfT5roWPLTL039tWgKI4TiqoycyhI7uhC_u8HXqDrslL4NkARs0Oq2poE_hnr-Thz_YdLKII8SyUm9AJME6yxr9GPvhfuoV7OzSkBS2C905Y08S_Ia4rBnHULs10wrGiPQRgoTfHgDllj8ho8_0nbEh6NPZBe8ed7YtJJq9LiLsKixIuvKx4QgI3SkjNc113A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتانیاهو: جمهوری اسلامی سقوط خواهد کرد و «روز آزادی» مردم ایران فرا خواهد رسید
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مصاحبه‌ای اختصاصی با روزنامه دیلی‌میل که روز شنبه ۱۱ مهر منتشر شد، گفت که به اعتقاد او جمهوری اسلامی «سقوط خواهد کرد» و خطاب به مخالفان حکومت ایران گفت: «ایمان خود را از دست ندهید، روز آزادی شما فرا خواهد رسید.»
نتانیاهو در این گفتگو مدعی شد حکومت جمهوری اسلامی ایران در شرایط کنونی «بسیار ضعیف» شده و گفت محاصره آمریکا به رهبری دونالد ترامپ، سپاه پاسداران را به‌شدت تضعیف کرده است. او در عین حال تاکید کرد که سقوط حکومت ممکن است زمان ببرد.
او درباره برنامه هسته‌ای جمهوری اسلامی نیز گفت اسرائیل با همکاری آمریکا، مانع دستیابی ایران به سلاح هسته‌ای شده است. نتانیاهو گفت: «اگر ایران اکنون سلاح هسته‌ای داشت، چه اتفاقی می‌افتاد؟» و افزود که جمهوری اسلامی همزمان در حال توسعه موشک‌های دوربرد است.
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتقاد از سیاست دولت‌های غربی و به‌ویژه بریتانیا گفت آنها انتقادهای خود را بر اسرائیل متمرکز کرده‌اند، در حالی که به گفته او، تهدید جمهوری اسلامی و نیروهای نیابتی آن را نادیده می‌گیرند.
او خطاب به معترضان در بریتانیا پرسید چرا به جای اسرائیل، مقابل سفارت جمهوری اسلامی اعتراض نمی‌کنند.
نتانیاهو گفت: «چیزی که به مردم بریتانیا می‌گویم این است: کجا هستید؟ کسانی که علیه ما اعتراض می‌کنند، چرا مقابل سفارت جمهوری اسلامی اعتراض نمی‌کنید؟ چرا تمام زهر دولت بریتانیا متوجه آنها نمی‌شود؟»
او افزود: «چرا علیه جمهوری اسلامی جهت‌گیری نمی‌شود؟ چرا علیه نیروهای نیابتی آن نیست؟»
نخست‌وزیر اسرائیل همچنین دولت‌های غربی را متهم کرد که تهدید جمهوری اسلامی را به رسمیت نمی‌شناسند و گفت: «این حکومتی در ایران است که ده‌ها هزار نفر از شهروندان خود را کشته یا مجروح کرده است.»
او افزود جمهوری اسلامی اقتصاد غرب، منابع انرژی و آبراه‌های بین‌المللی را «خفه» می‌کند اما موج خشمی را که علیه اسرائیل وجود دارد، متوجه جمهوری اسلامی نمی‌بیند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/78607" target="_blank">📅 17:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78606">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIGdqATkyvRbTTFGna-DWDXiRTwYhFaKs2HTN0Gtm-7QOI_LgufADBwL5FiiBxlIYhakw8vTLb7O0xfTatjRn9GIqNj9HKIye1jp7_67cgyLGftcawFn5ZHqrgGNrNeGgWF3t4CdFMFTENlq4XmcahBCIFttmbrs3ItOPuw8tVl0jjDDsBYNgCMkhrHwSCJVjCS05nwpuwAfjmzNow-K5LMNArrY-55ROLVVyXgLDg71M8G4FhTVwTq5l7o_zZGdEmlW_NT-Q6ImpLb3457NlDn_Rbh8aD6P3vyVDwP0loXEST9JwFwVAUBJw6Q24xRGcM3fBxX06je8CieZoUk4pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تیراندازی مقابل ساختمان دادگستری مهاباد در روز شنبه ۱۱ مهر، یک نفر کشته و چهار نفر زخمی شدند.
امیررضا رسولیان، فرمانده انتظامی مهاباد، اعلام کردە  این تیراندازی مقابل در دادگستری این شهرستان رخ داده و در جریان آن یک نفر کشتە  و چهار نفر زخمی شده‌اند.
یک منبع مطلع به ایران‌وایر گفت فرد مهاجم که چند سال پیش فرزندش را از دست داده اعضای خانواده فردی را که او مسئول قتل فرزندش می‌دانسته و در حال حاضر به عنوان متهم در زندان تحمل حبس می‌کند هدف تیراندازی قرار داده است.
به گفته این منبع، مهاجم پس از تیراندازی توسط مأموران انتظامی در محل بازداشت شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/78606" target="_blank">📅 17:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78605">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mq9Jsdnk7ORaOgpGnoAAydgAiHvzOVe7IUpFNFqoRXyf1FYcwfMG-nELB3PU23etlQEbrT2BsAlmj9UGenrCi9IWMKm8XvQ2ehFe9jx7hGK2s4pUtUe5sesNu9bbjzJQs6Wr03mLCrkPeYn2sa7r-NWEd19fJZcC6RosAqbS9CsW_sD4rzfPPJxaWfFhOb2PYnHPeb0eO1yO0HePWqGJDVr8KzcsTteVwPYHUEql9TpmYjILhtwCoI9uzHmlAac-AfMQPU47r69GpD8GLLqNMY2yx7IYCK-NfymSYVlp-DB3wMHj9TZZqQ_RSsyf4LatXLR6Bu4U8Fg59Gt2WgFjOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت اطلاعات جمهوری اسلامی روز شنبه ۱۱ مهر از بازداشت ۳۱ نفر در شهرستان سیرجان در استان کرمان خبر داد و آنها را اعضای چهار «شبکه سازمان‌یافته خرابکاری خیابانی» معرفی کرد.
این وزارتخانه مدتی شد افراد بازداشت‌شده برای شرکت در «فراخوان‌های سراسری» سازماندهی شده و در حال تهیه کوکتل مولوتف و ابزار تخریب دوربین‌های شهری بوده‌اند.
وزارت اطلاعات همچنین این افراد را به دست داشتن در «آتش‌زدن فرمانداری، تخریب بانک‌ها و ساختمان‌های دولتی و حمله به مقر پلیس» در جریان رویدادهای دی‌ماه ۱۴۰۴ متهم کرد؛ رویدادهایی که در اطلاعیه این وزارتخانه از آنها با عنوان «کودتا» یاد شده است.
در این اطلاعیه جزئیاتی درباره هویت بازداشت‌شدگان یا مستندات مربوط به اتهام‌های مطرح‌شده ارائه نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/78605" target="_blank">📅 17:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78604">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/reu7Ej8jNG4qA9gnAdHiqh6SCWewFMjRIaFrLuGz0em_oJF0sTjOpmhlMwhSwjpuctNw-dc6JWvNGv0wzsXMW5NW8izcZp9uF2arVpBHuQPaMRJT8aXyJVBOEtpFuCvi1cBmHQ_inKcWL3h9Q7p1ztjy_wZTjT7EDypp-fc2Fx5jxIwLschn-1R-jRQwCUY5U8ZEOlsvp9LOen0UIUwYcBFwC-qPvJ8PItZL8F7gg0qT-4rIdsjv8LMK26Mfw7NVVzDq6rE87V1OgrOKW72Se2ytL8UD7cbFFHTmIib8HdJQrIb_IFE3dpiEEuaWdznUKoOwKU3-xusmLam9beufyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام «سیاوش جمشیدی خیرآبادی»، از بازداشت‌شدگان اعتراضات سراسری دی۱۴۰۴، در بامداد شنبه ۱۱مهر۱۴۰۵ خبر داد.
قوه قضاییه همچنین ادعا کرده است که جمشیدی خیرآبادی شامگاه ۱۸ دی ۱۴۰۴ در خیابان ناصرخسرو شهرکرد به‌سوی ماموران تیراندازی کرده و سپس از محل گریخته است. براساس این روایت، او دو روز بعد، ۲۰ دی ۱۴۰۴، درحالی‌که یک قبضه سلاح کمری همراه داشت، بازداشت شد.
در اطلاعیه قوه قضاییه آمده است که حکم اعدام این معترض پس از تایید در دیوان عالی کشور اجرا شد. بااین‌حال، در این اطلاعیه توضیحی درباره زمان برگزاری دادگاه، روند دادرسی و دسترسی او به وکیل منتخب ارایه نشده است.
مقامات جمهوری اسلامی معترضان دی‌ماه ۱۴۰۴ را «کودتاگر» خوانده و آن‌ها را به ارتباط با آمریکا و اسراییل و تلاش برای ایجاد ناامنی متهم می‌کنند.
«مسعود پزشکیان»، رییس‌ دولت جمهوری اسلامی، نیز در سخنرانی اخیر خود در مجمع عمومی سازمان ملل مدعی شد که مردم ایران طی هفت ماه گذشته برای «دفاع از ایران» در خیابان‌ها حضور داشته‌اند.
او معترضان را افرادی توصیف کرد که به ادعای او، آمریکا و اسرائیل آن‌ها را «تهییج» و مسلح کرده بودند تا در داخل کشور ناامنی ایجاد کنند.
صدور و اجرای بسیاری از احکام سنگین علیه معترضان دی ماه از جمله احکام اعدام ذیل قوانین «تشدید مجازات جاسوسی» صورت می‌گیرد که از منظر حقوق‌دانان و فعالان حقوق بشر شامل موارد جدی‌ نقض حقوق متهم است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/78604" target="_blank">📅 17:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78603">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پیام‌های دریافتی از قشم
حدود ساعت ۱۶:۳۰:
صدای جنگنده خیلی نزدیک اومد صدا زیاد قشم
همین الان قشم موشک شلیک کردن
16:34 دقیقه
وحید جان از قشم سمت اسکله بهمن موشک شلیک کردن
صداش خیلی وحشتناک بود
معلوم نیست شلیک کردن یا جنگنده بود ولی هرچی بود صداش خیلی زیاد بوددددد
قشم همین الان یه صدایی شد
سلام وحید جان چند دقیقه پیش یک موشک به سمت تنگه شلیک شد.
سلام وحید
دور و ور ساعت ۴:۳۰ جنگنده رد شد
سلام ساعت چهارو نیم بعداز ظهر امروز قشم  صدای جنگنده امد خیلی وحشتناک بود
[این پیام متفاوت هم بود که نمی‌د.ونم چقدر درسته. بعد از یک ساعت معلوم نشد صدای چی بود.]
قشم پدافند بالا نریمان و زدن
وحید
خیلی شدید بود صدا ها
معلوم نبود چی بود
رادار تازه ۳ روز بود درست کرده بودن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78603" target="_blank">📅 17:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78602">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/742b2ddd5c.mp4?token=o1-zyEcSBsxVt-UKZGH7NdOmREbZvJZ2vqV1hHsboeEHPL9rOG4oTiY-q3EKrhoqCSqTMIdkxFFy_yyBMrcF1lDIaNmaZWF9D4MyVTnKP1BojXPW7hFk2TtUzwZjB2kk1bfdlvx3d6KIuiLWm9dPN4-gz4wqbmVGu3H3KhRK91__04JGrUIsvSZXqKd8ixC78VO67_cpPf76HR5949jOn1bDvQMXXct-htk4IkqXreAon6_w7ZDFLOUdK-8S-jQRTmfdpvYpUGuZh-5ky60cTR3KeNXpqduYxWHIR0RJ5FDkdsG0IWa61Lzhzn2aDK12Ju3HOHkMlkoaEdcxe9FhZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/742b2ddd5c.mp4?token=o1-zyEcSBsxVt-UKZGH7NdOmREbZvJZ2vqV1hHsboeEHPL9rOG4oTiY-q3EKrhoqCSqTMIdkxFFy_yyBMrcF1lDIaNmaZWF9D4MyVTnKP1BojXPW7hFk2TtUzwZjB2kk1bfdlvx3d6KIuiLWm9dPN4-gz4wqbmVGu3H3KhRK91__04JGrUIsvSZXqKd8ixC78VO67_cpPf76HR5949jOn1bDvQMXXct-htk4IkqXreAon6_w7ZDFLOUdK-8S-jQRTmfdpvYpUGuZh-5ky60cTR3KeNXpqduYxWHIR0RJ5FDkdsG0IWa61Lzhzn2aDK12Ju3HOHkMlkoaEdcxe9FhZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، روز جمعه، در سخنرانی خود در آلاباما با اشاره به ضربات نظامی به ایران و انتقاد از برخی رسانه‌ها گفت:  آنها نمی‌خواهند موفقیت ما را ببینند. وقتی نیروی دریایی‌شان را منهدم کردیم، نیروی هوایی‌شان را از بین بردیم و چند ماه پیش ضربه‌ای مهلک به ایران زدیم، نیویورک‌تایمز و رسانه‌های جعلی می‌‌گفتند اوضاع ایران فوق‌العاده است. آنها همه‌چیزشان را از دست داده‌اند، از جمله رهبرانشان را.
او با تاکید بر خلأ رهبری در جمهوری اسلامی افزود: آن‌ها یک دور از رهبرانشان را از دست دادند، بعد دور دیگری را، و سپس نیمی از دسته سوم را. حتی یک دور رقابت راه انداختند که ببینند چه کسی حاضر است رهبر شود، اما هیچ شرکت‌کننده‌ای نبود و همه می‌گفتند من نمی‌خواهم.
بخشی از مشکل ما اکنون این است که اصلا نمی‌دانم باید با چه کسی طرف شوم. هیچ‌کس حاضر نیست رهبر باشد.
می‌گویم در ایران با چه کسی باید حرف بزنم؟ اما هیچ‌کس آن اطراف نیست.
در می‌زنیم، تق‌تق، ولی کسی در خانه نیست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/78602" target="_blank">📅 05:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78600">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b9Hn3O_CVrLgc6LJsnI3W3Zp3wP0svgvWuIIFpeShycQ2aMhfdkTnbHrL-A8ZE2zUKWG961ISpIst_S1MZJ_xRhDMhbVVl31_WZULVeMuoNQgxH8VuysMo6dv1CIYIk9SiqN2l0lPmmWl-F9_lOhNrxxifNMV7Q3gZFq1YJjWLNun9Ny16r1FxaIKhvYbq5t0o8STc5iF41t0BEizq2nGBnfOMGkhQ1wjJ6kk3vQWTbmit-cztXjm-JtzDwKexsmAoMdwNrrR0s577fd-sIE_XviVuYUSGMP8rMS5rvVYnLn_47Y0C22BWd5ww5s-Sdb2Y5Du03AoppdjD7LNH22jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rz5qBTpzv8Bhjj644Ak4jFGqvaXfEuUXILrXeUppZS9E8tGRl11Tn3eC5kh1KFL_Z5uvdJjdy6LD1SQYqG8gBo5e16BwL0nUXzEemRNZLbFx6vazh99buWspgudsXGz5ZQoGAoQAt5UIAWampHzKDlGkeUNQTBTrPN__jtheGqX9YrnX2aVcgchr-Rjbv_wUQdC8MdlAboq9ZirQppqO15NEB5GgXM9LNB6Fce8H4bc1sG3IESbrEMDM0wK-jzN01K3HXaRnZiOCTew5-WkgkW_LuXDVRwak6U03V9LqQ1HsYRXCgRlRTGKeFJB2o9BlJX4xmHVrZyYD8HenljUbJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وکیل «الناز شاکردوست» اعلام کرد دادگاه تجدیدنظر استان تهران، حکم بدوی یک سال حبس تعزیری و دو سال محرومیت از فعالیت‌های سیاسی، مجازی و هنری علیه موکلش را تایید کرده است.
الناز شاکردوست، بازیگر سینما، به دلیل انتشار یک استوری مرتبط با اعتراضات دی ماه ۱۴۰۴ به دادگاه انقلاب احضار و به اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس تعزیزی و دوسال محرومیت از فعالیت‌های سیاسی، مجازی و هنری محکوم شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 439K · <a href="https://t.me/VahidOnline/78600" target="_blank">📅 18:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78599">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/84b4ce621c.mp4?token=dPY-svcJNfPk9I01QHxNaQbaJzyv0rvcOwDsCG1-nMLNmLQsGWmGz37k_oHjHtCIJPtnVxPBPz2PGhhB50LHMjINmVcm0JKJxXXb0Gg2Vy9vCAmhLlIDRUsJrnYA6Me12CPTipP2R9OIP8LUVdqRWiZTRe5SBy20Sle81kaPbSmpSM5DyPjFUXW3NnKHYE98IJoHD1BdE-IAsCIfxne6fuxxGRuEHBn_FshaVcrJZwV3IjVuXEP3NHyw1U5bcLI2XBd-Wa13pnnG9tT23MiJv_LaygtkYir5FyXkRxeoHgE7SRbMp_bFW2VG-L7p9KV1_o9zyAiaXxItunAA80AV3A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/84b4ce621c.mp4?token=dPY-svcJNfPk9I01QHxNaQbaJzyv0rvcOwDsCG1-nMLNmLQsGWmGz37k_oHjHtCIJPtnVxPBPz2PGhhB50LHMjINmVcm0JKJxXXb0Gg2Vy9vCAmhLlIDRUsJrnYA6Me12CPTipP2R9OIP8LUVdqRWiZTRe5SBy20Sle81kaPbSmpSM5DyPjFUXW3NnKHYE98IJoHD1BdE-IAsCIfxne6fuxxGRuEHBn_FshaVcrJZwV3IjVuXEP3NHyw1U5bcLI2XBd-Wa13pnnG9tT23MiJv_LaygtkYir5FyXkRxeoHgE7SRbMp_bFW2VG-L7p9KV1_o9zyAiaXxItunAA80AV3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا، شامگاه پنجشنبه نهم مهر ماه، ویدیویی در شبکه اجتماعی تروث سوشال منتشر کرد که حضور گسترده معترضان در جریان اعتراضات سراسری
دی ماه
در ایران را نشان می‌دهد.
در این ویدیو، معترضان شعار می‌دهند: «امسال سال خونه، سیدعلی سرنگونه»
realDonaldTrump
این ویدیو رو ۳۱ دسامبر ۲۰۲۵ ده‌ها اکانت عربی و اکانت‌های مرتبط به یک سازمان سیاسی خارج از کشور منتشر کرده بودند و گویا بیشترین توجه رو هم در اکانت این مسئول اسرائیلی گرفته بود که بارها ویدیوهایی با شرح اشتباه هم منتشر کرده:
GadbanWaleed
اون روزها خودم هم کلی ویدیوی مهم از شهرهای مختلف ایران منتشر کرده بودم ولی به درستی تاریخ این یکی شک داشتم که مربوط به اعتراض‌های ۱۴۰۱ باشه و نگذاشته بودمش. به ویژه اینکه منبع اولیه‌اش اکانت‌هایی بودند که همیشه کلی ویدیوی قدیمی رو هم با شرح نادرست بین ویدیوهای روز منتشر می‌کنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/78599" target="_blank">📅 17:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78598">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحسین باستانی Hossein Bastani</strong></div>
<div class="tg-text">🔻
معمای «تیم شش‌نفره» در حکومت ایران
مسعود پزشکیان اخیرا به «تیمی شش‌نفره» در حکومت ایران اشاره کرد که در مورد بحران جاری با آمریکا «اختیار دارند تصمیم بگیرند و تصمیمات با هماهنگی آنها اجرا می‌شود». به دنبال انتشار این اظهارات در مصاحبه با سی‌بی‌اس، رسانه‌های رسمی ایران روایت‌هایی را از ترکیب تیم شش‌نفره منتشر کرده‌اند که عمدتا در مورد پنج نفر مشابه و در مورد نفر ششم متفاوت بوده‌اند. بخش ثابت روایت‌ها اغلب بر رئیس‌جمهور، رئیس مجلس، دبیر شورای عالی امنیت ملی، رئیس ستاد کل نیروهای مسلح و فرمانده کل سپاه تمرکز داشته، هرچند نفر ششم را برخی رئیس قوه قضاییه و برخی وزیر خارجه دانسته‌اند.
اشاره مسعود پزشکیان به وجود این تیم، البته اهمیت داشت، ولی این اشاره نه اولین بار بود که صورت می‌گرفت و نه نشانه تحولی کلیدی در ساختار تصمیم‌گیری کلان، یا مثلا ایجاد نهادی با اهمیتی مشابه شورای عالی امنیت ملی بود.
در تیرماه گذشته، عباس عراقچی در مصاحبه‌ای با برنامه یوتیوبی «ماجرای جنگ» گفته بود چارچوب مذاکرات با آمریکا در شورایی تعیین می‌شود که به «کمیته شش‌نفره» معروف است. توضیحات او اما نشان می‌داد که جایگاه این کمیته پایین‌تر از شعام ـ شورای عالی امنیت ملی ـ و در حد یکی از کارگروه‌های داخلی آن است. عباس عراقچی در گفتگوی خود، مشخصا از کمیته‌ای «در داخل دبیرخانه» شعام سخن گفت که ابتدا «کمیته هسته‌ای» و سپس «کمیته مذاکره» نام گرفته و در نهایت به «کمیته شش‌نفره» معروف شده است. مطابق اظهارات او، این کمیته از مدت‌ها قبل از جنگ چهل‌روزه فعال بوده و در زمان‌های دبیری علی شمخانی و سپس علی لاریجانی در شعام، به‌ترتیب تحت مسئولیت این دو نفر فعالیت می‌کرده است.
البته روایت عباس عراقچی از قرار داشتن این کمیته زیر مسئولیت دبیر شورا، این ابهام را ایجاد می‌کرد که آیا ریاست آن، مانند شعام، با رئیس‌جمهور است یا اینکه سخن از جمعی شش‌نفره است که رئیس‌جمهور را شامل نمی‌شود، ولی جمع‌بندی‌های خود را به رئیس دولت ارائه می‌کند.
در هر صورت، عباس عراقچی تاکید داشت که تصمیم‌های کمیته باید «عینا مانند مصوبات شورای عالی می‌رفت، تایید می‌شد و بعد ابلاغ می‌شد»، که اشاره‌ای به لزوم تایید مصوبات از سوی رهبر جمهوری اسلامی به نظر می‌رسید. او همچنین، به این سوال که آیا تصویب آتش‌بس (موقت) در پایان جنگ چهل‌روزه «با نظر آقا مجتبی» بود یا نه، پاسخ مثبت داد، هرچند در مورد شیوه تصویب گفت: «ارتباط ما با کسانی بود که رابط بودند و مسائل از آن طریق منتقل شد.»
قابل تامل است که مسعود پزشکیان، که در مرداد ماه از دو نوبت دیدار با رهبر جدید جمهوری اسلامی خبر داده بود، در مصاحبه‌هایش در سفر آمریکا هم به همان دو مرتبه ملاقات خود با رهبر اشاره کرد، که نشان می‌داد دیدار جدیدی با مقام اول حکومت نداشته است.
به عبارت دیگر، با گذشت هفت ماه از رهبری مجتبی خامنه‌ای، ارتباط تیم‌های حکومتی با رهبر کماکان به حلقه «رابط» اتکا دارد که، در مورد آن حدس‌های متنوعی مطرح شده است. از جمله، گمانه‌زنی‌هایی که حسین طائب رئیس جدید سازمان بسیج را از افراد موثر این حلقه می‌دانند.
🔹
ادامه  مقاله در لینک زیر در دسترس است:
https://www.bbc.com/persian/articles/cr9dw7dvjxj1o
@HosseinBastaniChannel</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/78598" target="_blank">📅 16:37 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
