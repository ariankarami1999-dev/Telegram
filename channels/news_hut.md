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
<img src="https://cdn4.telesco.pe/file/R40UbZuKXA7oHquC-G2mIX8M-XVY2G5K45mKiYWzmyM7Y8IC8aF2lKcOZKgPfQOhstpgzVBR84thxhnEadibitDgChbtUtpP0y7kzdVPWLkNL4pbosr9P5SN00hk0GFDiztVgAXU9SFR3MIM4wb8CwxTMKTnSbvWD4YfpxVIf5NU52RKCNZAYm46QpU9uTRmQn9AL6naKhUbevfmlH6QOUphOr-ChHMXJIPZPsOt5mL8yja3Isj8jFPcjw5FaIOPJrXqjqKeUX2qVogNzpFGSinYqLAe52_VYS7NoXiGTMcPsX_lP4g4se35PFVZL01yXA7KHth-kSkokaNx0LMZtA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 180K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 13:13:50</div>
<hr>

<div class="tg-post" id="msg-67897">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVFtAQ86MAylaXfE7xOaqQ3mHT6fOeoOEW2DM7IobdnCoVwfo-d93goVNcNkv2b-PCYCzzNWOha40_pn_Bqu8QAKblkDrF1Xw9wxIMfhDA8oOf85yxA5fOwc-xKoNZBC3NJrIbWqxwPWPWT7hADqt5GYcKNf021KJTkesZFqaV8pn3Okb_u_RwX8l2ol-N6XYm_V5d_UczPLFxrXYR4tBN5YMO3rKTySzd15pmIM8h2VoLUR9Q8QBD944DOINdGvKDvjJBftGTQnE3XKwpDvyidhi2riQOdGyKBcEvQQjvkznX6yC4bnNMO6fqgaHgvK3Z1O1jng-WkeMYJwROWf-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمیدرضا دهقان از اعضای پدافند ارتش در منطقه جاسک طی حمله بامداد امروز ارتش امریکا کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/news_hut/67897" target="_blank">📅 12:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67896">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvULATMieiLPn4GUZSNcv6Mc5K65DginSdhqU8Yk1YUM4ZpVxwm8W6KLY5_XSV--29MFEKc11Os2MQRGrKRrR3zyjXRA4-XhzLka-Vez6jVMIhmXR8dWcvkMDxJRsH3CPaL__QUxDw3R3fjpIq-GHgbfJ_HRhVYtBbyDPH3i4Mi4Qn4Eay4mlqb7G4IRo0k-TDiz4Hbzz6VczWwKqEJUfs7GNJRAxaEeFOM9IA1rz17u4Ov0j4CMPqZTjUQjBLAAjxCRybUrgk7yNgkGk7sfWSrQi3BncNq_uLnDeSV_rQKavPGsLMCXfApewE1tpLa7TChOWMiA-MAvmE2jLAem7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
واکنش مرندی عضو تیم مذاکره کننده به درگذشت سناتور لیندسی گراهام:
چقدر بد؛ من میخواستم او قبل از رفتن به جهنم قیمت بازار نفت را ببیند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/news_hut/67896" target="_blank">📅 12:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67895">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nF51OQyDSp1xoZijJUQBXccZOt-aQ_8tKQtdo1w47FLcLRc1pjREjqAc0qy7L6c28qLz9Ohng7wL59REulM201hrmJNfz08PNhQXCfqvVumC71iwq4Rc4uB6vEwiNCzClnsS_EjHPwl2KTKbbIAQ63ABgLXWCIZODW0L8rpe7dYvVYvTaANg3CG5_MLsOc93NNrN2Euqe0_Wj9CgOY5jCJVZw3hHk0IYDJ0JDH_8GtyUNn7ozqJLYjx_h9fiJwnE_8AytGcjIALjDgJL6CXBohhQjcAc1JwzW3idCcEvaVVYjrs5H32fjPhL93opd7Tz0nP-Vs40Uhwwp0h1pAsCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
👑
شاهزاده رضا پهلوی:
از درگذشت ناگهانی سناتور لیندزی گراهام، دوستی ثابت‌قدم برای مردم ایران و مدافعی سرافراز برای آزادی، عمیقاً اندوهگینم.
در لحظاتی که نیاز به موضع‌گیری اخلاقیِ صریح و درست بود، سناتور گراهام در جانب حق ایستاد. آنگاه که دوستانِ واقعی کمیاب بودند، او در مبارزه علیه استبداد، در کنار مردم ایران ایستاد.
او از صدای خود بهره گرفت تا اطمینان حاصل کند که صدای مبارزانِ راه عدالت در راهروهای قدرت شنیده می‌شود.
حمایت او از «انقلاب شیر و خورشید» ایران، لقب «عمو لیندزی» را در میان ایرانیان برایش به ارمغان آورد.
یاد او همواره با سپاس و احترامی عمیق گرامی داشته خواهد شد. ما مراتب تسلیت عمیق خود را به خانواده، عزیزان و همکاران سناتور گراهام، و همچنین به مردم کارولینای جنوبی و ایالات متحده ابراز می‌داریم.
روحش شاد و یادش گرامی باد؛ و باشد که دیگران راه مبارزه برای آزادی را ادامه دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/67895" target="_blank">📅 11:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67894">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTcdl1PxT_ym1lUzYmLFKk0kM-KMwTNj5WQoSEFOQqfdMnacomg4QJ6cAiSetwUFIWpNdX7w2R1o6A9RNmaS85xntGpTQ8RzYOqdEn_srUMfZxeMELP8EhkhBL4tKEmrX1_di9X2x7aYDr0Xn5UEy0OyvhXkliO-_ZBkANw60685jn-6OYCgCiSTBniY44gl3UcAezoS_ncRxJJkfp7VRDqbmXUp8g5h6RtPaCdOfX4kQh-yd1boSZ2WcePN1BMEFu7lcjeCoKntzg61adCFIJlHrHqE34ezozxLdQHL_wvLCoTw6C_-a257I3pQpS9LO5AE7nbz0W1aL8G2GG_fvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو نخست وزیر اسرائیل در سوگ مرگ لیندسی گراهام:
من و سارا با مردم آمریکا به خاطر از دست دادن دوست عزیزمان، سناتور لیندزی گراهام، غمگین هستیم.
در ملاقات اخیرمان گفتم: "لیندسی دوست بزرگ اسرائیل و دوست عزیز من است. ما هیچ دوستی بهتر از لیندسی نداریم.
لیندزی فهمید که امنیت اسرائیل و آمریکا جدایی ناپذیر هستند. او زندگی خود را وقف دفاع از آمریکا، تقویت اتحاد ما و ایستادگی برای جهان آزاد کرد.
اسرائیل یکی از بزرگترین دوستان خود را از دست داده است. آمریکا یک میهن پرست بزرگ را از دست داده است. من یک دوست عزیز را از دست داده ام
.
قلب ما با خانواده لیندزی و با مردم آمریکا در این زمان سخت است. باشد که ارزش ها و ابتکارات او همچنان ما را به سوی پیروزی و صلح رهنمون سازد و یادش همیشه پر برکت باد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67894" target="_blank">📅 11:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67893">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5JO8oj6TiPXfxFXFBEuLvRR2Bsuy94cEGAXykRSA8cSSKRZgQIMLhJshrS3Q-oyEmr8H400ayLSp9v4tC7lGeCNC9Q0DVt_n-d-OIvTPIhv1zVGCLDQTiZrCIamQYMKZSOesEEg5C2msFvjd0KXB03mtXO-M6G0Jj9BX30NKyei9Mux2LHFV_Nqojlac9BvbgVQIN89ttbiVBYk6v-gWzQIeyB3-IyFQDVXUrAxOfQltC_2YAH4Zc9glqexmN9YwJnkWLYMQwlGujeQ3dg8Wkuh0-6qxMNGUsWJ3pEQb9KwS-F3WSv1kAXtpVCjl9bpeH56Ig-XFb5fkUYGDH0kdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ:
سناتور لیندی گراهام، یکی از بزرگترین شخصیت‌ها و سناتورهایی که تا به حال می‌شناختم، از دنیا رفت. او همیشه فعال بود و یک آمریکایی واقعی بود. ما لیندی را بسیار دلتنگ خواهیم شد. جزئیات و برنامه‌های مراسم تشییع پیکر او متعاقباً اعلام خواهد شد. چه خبر غم‌انگیزی!
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67893" target="_blank">📅 10:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67892">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDxQXll24mOFqniywF86zHqRxVkVRtLfGz6kh33rdtqOYUSN4kmNh2NkmZRKTrF8DTUISOULKLrca2BejnbnfV69vdDUqqyjNVn8NZOMjhPlOs0WW9gfhdQ0ajKovNPyRPDmQ02BCSVejSSRpx0PAYUX1E0uetnpZg8DMFetJAItkOVbGrSNeymMr4kfgmlHiVswpPch_7VDETiU_-S6ML10PN1g-iQCO2UKbISlb8cxk9Gnr3JxcxNrfVQz9n5FGPjr607dc6UQFeWCc6MhwmjNAHs2Tz-4nL3FhTE4S5XSUPgtbovAKvpbbNq-mCFKWJyGUKWB0amDAULUehCOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ان‌بی‌سی‌ نیوز:
در حال بررسی صدای ضبط شده از بی‌سیم پلیس مربوط به واکنش نیروهای امدادی به یک مورد ایست قلبی در خانه لیندسی گراهام است.
این شبکه همچنین گزارش می‌دهد که عکس‌هایی از شخصی دریافت کرده است که به احتمال زیاد لیندسی گراهام است و او را روی برانکارد از خانه خارج میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67892" target="_blank">📅 10:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67891">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB61_-4et-npGTWkU8NgnGhAPRZkL6pKlsoj619ZtOvrqSHNw449PhnBFTsWk4MFHyp0soElm2Cw6JWHJdzey3raaxY8UvF5QFU9kz4z-SGQevsjfgFWneJ2Opoyiy_66t0BbHYP6Av3S9F9l8ls5UuXd9A6E4qKy-q67dSyphukUokdJVt7XR8bdrIRndcnYBZrP71RhcILiBbEuN-j-p2xATpBlaJ1ft42EXMslMxTFk4RaX2XwvKReC4LP0OqILPXmJ8ZNTswX3ZfKWm9bVqIaJ4ydUD8n0fjXhb4WgYJLQhcL2BW8u-Si7X2sran_uJiYiliUySlxtQ7O-0EJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RIP, great man
🫡
🖤
#hjAly‌</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67891" target="_blank">📅 10:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67890">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHG_1B8n8RvtXkKBE7rWeTqDsRP47F56MLCmeLzAlNbXj6NZS05ytPJeYT0HNrpuwypBAS-IbtmUyOfWRs-66qyL-A12KAAQVmKNcS0daiDN6mPl1n1yIG4XpqWjyBcTWug5dcwclj7EvKv7jhagHTfdp8z9oK_BllCFS1VU-W_vDMpBd5bODeBj2Ae80OPzfJn6RQItkAzdTSpCbkcSBbo4ye8piJ9pIAjDUtJPS5C5Fkt-1t5HiRKpHviNSYR1kh2WH8555W2PbdPjFz5EknO3F30i5AFwobZi96Gk71-rSzezGNVRUL_Ej-66qO3FifJOWvbP_o2859JOnMwvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:   دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت.  @News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67890" target="_blank">📅 09:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67889">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJTJxusanixgKxANJOn2Z8UqavpcDW4MrKxUrX_2sIeDHRr-KJATF76LAnp7DM0ntAzU62wbf3G7JBgZMaGsnu-qODMXxfbD9gNghxP40zC8Nqd3Zx413lHp7B76yfILIzJKi6grFO8_Z1dn7Jx_fYGvvwfYdf-xa1Cr-aibGDmHJLBRsTnXoCtBLCQ46d4HyAwIgo_XCdWtRyiUXmfWQUdmtHaUT_W10JgPOcpLdO2Fq7n3aPD0iUXC62rs5GLfqn661mp5sXJrLV8Xpdp2s2X_phA_Xa59-F7L7ooGBoWNWcJUlMcamLX37nVgwqQXSnLGQiNuODckzPyyzDwBBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:
دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت
.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67889" target="_blank">📅 09:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67887">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVMjXNhhi-NHuR80GLac8HYbXdzZy4spU5MQTiUwUyeX_wzM8lpYXw7V_WS5BWkBnrLyiIRPkIFujiU17WCa8otAUCUWP4foQIhTbtqoN39ihmQHmFMEBXvj_6Mi4683ivFY6ajKGk1mNtPs23iThd1Ozfg14VpgLcdG2H1VTjFQon8e0u2lhsQoDPAIkg21KLl1QzEuYXTMABJTr_cD1vhkV_x39k3oCpX_OS-3QyRMhnqLCqd5EfO-0j_mvVMvM8BF3_tC31EDdYmRdzQ6GEoouxrx7NF8opaxbJOTG7pLL9lP076KeiQEqYyIzyYO2NioMsX5VkWLRpN_pBVxRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#فوری
؛
لیندسی گراهام سناتور جمهوری‌خواه آمریکایی و از حامیان انقلاب شیر و خورشید درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67887" target="_blank">📅 09:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67886">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
تصاویری که سپاه از حمله به پایگاه های آمریکایی در منطقه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67886" target="_blank">📅 09:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67885">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=AHAG5g2pJwwfcSRYzYvdvxbPDeusJAvZwJTWau0Wir2Q2VxNwG4S3pYe5i8bcSPkqBeg8avnIuDEa7VbHvypthz817HOyQDBGZYmTTMj9dnMHpfqLfQ2066r4jBFOMqUZtW58dNP9J9K2HsA5I3W9ZebrPBFNxQOS-Shs8DVhRwWoqzUrnZ-h6h4oXnFzNlOwpnnOs90MGeeZWgH1WGcTuETNiheyG9wsj18ACj2PGDZRQzM7bHJxIIBFU4SpIbnyzFB_y5N5Pk7eWmstYmV9drN1wwVJLPzj6RdaYqMFBXqt45p7ehvkeeq60Lr1DhImtpj-3FCmfCgNJdnZaMAxYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=AHAG5g2pJwwfcSRYzYvdvxbPDeusJAvZwJTWau0Wir2Q2VxNwG4S3pYe5i8bcSPkqBeg8avnIuDEa7VbHvypthz817HOyQDBGZYmTTMj9dnMHpfqLfQ2066r4jBFOMqUZtW58dNP9J9K2HsA5I3W9ZebrPBFNxQOS-Shs8DVhRwWoqzUrnZ-h6h4oXnFzNlOwpnnOs90MGeeZWgH1WGcTuETNiheyG9wsj18ACj2PGDZRQzM7bHJxIIBFU4SpIbnyzFB_y5N5Pk7eWmstYmV9drN1wwVJLPzj6RdaYqMFBXqt45p7ehvkeeq60Lr1DhImtpj-3FCmfCgNJdnZaMAxYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سرباز روس خودشو به موش مردگی زده تا کوادکوپتر اوکراینی شکارش نکنه
اپراتور اوکراینی میگه: «نگاه کن لعنتی طوری نقش بازی میکنه که دی کاپریو جلوش کم میاره»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67885" target="_blank">📅 09:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67884">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7O7-qLkfYWOHBltPeXc3djqJb35nVjJzjPYJvxVRzFqV85_lr5HvDbirnm4MdlN8IPKFxqQ2iPBJAanOVHNAgGucLeVZbnpA4oFKHRXaMGJ5bWuPU237nSPdMDEO_uT1utycWaZnph5RMQz-zWGHpdJ-MAEG9CbPk64cJIAC7AAhd1vO-n5Dm3eafE-sU-v_Tu4dKb7Vjv_DmMyoN86TK9ePKPYWy2lHCQ-c4uwvFKzJJIg_9l9zAkpw_Fp6hleY-SUSRImppCotZVm_qAiaDX3J5RA-H6esKu4zmqTAbkz9SGLTKHxXHE-vZxJUfmemkmwFQzz5_FLDi7ExgXXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
قاليباف: دوران معاملات یک‌طرفه به پایان رسیده است. به شما گفته‌ایم: به قول خود پایبند باشید، یا عواقب آن را بپذیرید. واقعیت در حال نزدیک شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67884" target="_blank">📅 07:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67883">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=QFdu2H_R4Nk7otBKyVUIVgzkNfwPi-TSAniY273mIgOm8_Zgx1ocb8kwHCcx1_czbFAUjkXFenCneJIIa0tK6wP3jKzgtA2SGPrBUY8G3XGsR0D6A0XDoUfpOg4-X28Ispd3GJ3h5QaXGNQ7bNIy4hEwKsH1F2wvXzYzm7GkFYvVDdcDAIlVzF9MquaqKTxltohP8hBt_uAE4sng-Efc7wF_P-yDlZiTOxjwfjiEBXCl5sk9kyhB-bDLwWzf79z3gP7K1wBiBuuucdeidjiWovprrmueJIhKTJyy3oUZUwAYy6LeRTHOxz2BenXTOobp9K2A6T2kPJ6dYe_2e4BpEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=QFdu2H_R4Nk7otBKyVUIVgzkNfwPi-TSAniY273mIgOm8_Zgx1ocb8kwHCcx1_czbFAUjkXFenCneJIIa0tK6wP3jKzgtA2SGPrBUY8G3XGsR0D6A0XDoUfpOg4-X28Ispd3GJ3h5QaXGNQ7bNIy4hEwKsH1F2wvXzYzm7GkFYvVDdcDAIlVzF9MquaqKTxltohP8hBt_uAE4sng-Efc7wF_P-yDlZiTOxjwfjiEBXCl5sk9kyhB-bDLwWzf79z3gP7K1wBiBuuucdeidjiWovprrmueJIhKTJyy3oUZUwAYy6LeRTHOxz2BenXTOobp9K2A6T2kPJ6dYe_2e4BpEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
ادامه حملات سپاه به کشور قطر
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67883" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67882">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
سپاه مدعی شد: مراکز لجستیکی که به کشتی‌ها و سکوهای سوخت‌رسانی متعلق به ایالات متحده در بندر الدقم در عمان خدمات‌رسانی می‌کردند، در یک حمله شدید و غافلگیرانه منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67882" target="_blank">📅 07:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67880">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=Vwwq4dwz5DdAgQX8ZLqKwRW12bRWxviA2T_ZVLQBA1Hh94H3qAbFH81uULOvmUHElafW_rD_zcu2KVmLQJZzggZA6sfSbTGZqMm1f4QN2VUY25L1QYA4DepYUC3IDHlbuvmZjARiikXx4KUG2V40QzQMOYT3_YqdJ0SAjMc0Y1MFo4H9Ph6ZcmC3HuKhD5r33rb7NuP0_MvlDBK2kD78Q_dJ45cbXWb_UqjERSzYCJ83ipb3D3iPe1IVwwTry2Xpn0gwlv3DCnJ5M4H8e54pReTY0odfnPhsR5fdU-8-mBw_B-EqknLhnrZUayJ4LVCLtlNz0DuTRJ4cT-oyt4UIEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=Vwwq4dwz5DdAgQX8ZLqKwRW12bRWxviA2T_ZVLQBA1Hh94H3qAbFH81uULOvmUHElafW_rD_zcu2KVmLQJZzggZA6sfSbTGZqMm1f4QN2VUY25L1QYA4DepYUC3IDHlbuvmZjARiikXx4KUG2V40QzQMOYT3_YqdJ0SAjMc0Y1MFo4H9Ph6ZcmC3HuKhD5r33rb7NuP0_MvlDBK2kD78Q_dJ45cbXWb_UqjERSzYCJ83ipb3D3iPe1IVwwTry2Xpn0gwlv3DCnJ5M4H8e54pReTY0odfnPhsR5fdU-8-mBw_B-EqknLhnrZUayJ4LVCLtlNz0DuTRJ4cT-oyt4UIEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
تقابل سامانه پاتریوت در قطر با موشک‌های شلیک شده سپاه پاسداران جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67880" target="_blank">📅 07:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67879">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سوپرگل تماشایی خولیان آلوارز مقابل سوئیس</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67879" target="_blank">📅 07:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67878">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
سپاه پاسداران مدعی شلیک و نابود کردن یک کشتی تجاری دیگر در آب‌های خلیج‌فارس شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67878" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67877">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فکت:
شما چند ساعت دیگه می‌رید امتحان بدین ولی من زیر باد کولر می‌خوابم
😎
#hjAly‌</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67877" target="_blank">📅 06:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67876">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=nSh6pJBIsNlLSwlVbFeE5FLzqWz628rCtUt8BEFD78wohB1UGmK3TCVjG86QJeHyX30FenPgRylxE3lCffJdLe6ocnci2pA1DRaRkfNnzlHpX6jZ9L0gmdqQI9XLN3z9VlA5veynnpSG2JOFVMpA8zxIYpyyp4aWfHLMRyvu1yDGgzsJdlm30kZ2ia9I2wLDPzrP_8zNLXuEAfoOvzfmLK3WGEaChIeftzH0HTFCY51v7TTSacZLBwQblq1FuzzjTL1lBk4oDwShpTZNv33DC-DCedPWwgBYM4Lt_lcUch_LkOAO-aCKNB2nSco9Pm6qYmsJ4V7whqbjV9W-bpUACQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=nSh6pJBIsNlLSwlVbFeE5FLzqWz628rCtUt8BEFD78wohB1UGmK3TCVjG86QJeHyX30FenPgRylxE3lCffJdLe6ocnci2pA1DRaRkfNnzlHpX6jZ9L0gmdqQI9XLN3z9VlA5veynnpSG2JOFVMpA8zxIYpyyp4aWfHLMRyvu1yDGgzsJdlm30kZ2ia9I2wLDPzrP_8zNLXuEAfoOvzfmLK3WGEaChIeftzH0HTFCY51v7TTSacZLBwQblq1FuzzjTL1lBk4oDwShpTZNv33DC-DCedPWwgBYM4Lt_lcUch_LkOAO-aCKNB2nSco9Pm6qYmsJ4V7whqbjV9W-bpUACQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات سپاه به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67876" target="_blank">📅 06:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67875">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/67875" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1میلیون شارژ کن 1.200 میلیون تحویل بگیر با پشتیبانی آنلاین ۲۴ ساعته
😍
🔵
برداشت آنی
👌🏼
⚽️
تنها سایت مورد
#
تایید
ما
✅
اپ اختصاصی با
دسترسی راحت</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67875" target="_blank">📅 06:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67874">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aT3lA4Y22NlHsNzrtVEQti0Oebefbt5GH1Qo52Mrxtgr_tIDExQ1FObbDEDGAVawsQolRarNKH3AOJIh6rF1HuR-MRKZKygEdly9VButoCaumEqjH_HIuXsgy5I3FlWIoA9WXbeYYB0HpxjHLPGj8Eg1Q86EqY8PzsgWyhtRwSSb6JrEAhG2--jjBlgIVCrFirioDlGaO7HiAaBQw7zAAzPBEQCQpt3D-YQSJRzDxoamHEZ25F-2aa1bttvjn-pCl5gxUZHN-SWKghv64b8RmOURBGbqXv33d_mPz8aig71cwSdUsY-LWofS_bFati30Jd2yvEN5Usd51WWrjW2nCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
تنها سایتی که توی جام جهانی هوای مردم‌ رو‌داشته تا باخت سنگین ندن
⛔
📣
خودم بدون نگرانی از باخت شرط میبندم با کمترین استرس
🛍
از این لحظه 20% شارژ اضافی همیشگی یعنی به ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان بدون قیدو شرط میده
💰
🤩
🤩
درصد هم برگشت وجه در  صورت باخت،دیگه چی میخوای؟!
🌐
betinja.bet
🌐
betinja.bet
کانال هدایا
a20
@betinjabet</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67874" target="_blank">📅 06:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67873">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaRDi0U6p-B7CoKTA_bF7zuxt6Z4v9jX4c6NnYmmDQovnGge-v5KKdCZxn2MLGmgJTL72FlUhWM6GArfK-FVFCqcbxYf4zLjdWZ6nkm4Ww597s_s1vqbAnlz_aamZXCweWfvKR0gLRAbzY8Wwe3cKV5Z4uX3ozTrcItyqCCp7y5jE0C6Dzq_gAtqquAl3KOw2urdxvZZOPQJ8lWFJFAwGJgmUe-8bFRTBAgpLz60e34OnE9eb-rq4eMAWryUx-4wN7G6datWoCb22Y4dp7hZNB7tAQF1kfsi4F7IM0CthK6eNOoanMoS7pLfrVvpV0cBQljSChhtSJ5HzpuQrPMmyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/news_hut/67873" target="_blank">📅 04:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67872">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نتانیاهو: تو جام جهانی طرفدار آرژانتیم،</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67872" target="_blank">📅 04:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67871">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپمپ بنزین</strong></div>
<div class="tg-text">ما که منتظریم اقا
❤️</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67871" target="_blank">📅 03:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67870">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67870" target="_blank">📅 03:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67869">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67869" target="_blank">📅 03:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67868">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
هرگونه خبری مبنی به حمله به تهران یا فعال شدن پدافند تهران کاملا فیکه
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67868" target="_blank">📅 03:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67867">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گروهمونو که دارین؟
😴
https://t.me/+5NElXlQWt_05OTlk</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67867" target="_blank">📅 03:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67866">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff21f4d079.mp4?token=PMhQYFiVn-FkG_0Vx8KrSkcZ3qH4GUp-4x_9fb4-iOhJGIIqR7vFPdyMI2AGlOjfVM8-pXaSWXBKGDBYQDcKRHN5Oeq9meykxsSwZPbDmvtEVHY2oqXDvWGHcc9Ofw61zh12OqF5sQI_pRWHBNL6uj04G2A8mUG8pH7uDewzoK2xIalCpEopM1nNvWWD8k6DPh8H-knH1ea25O5VJQlw5XKEnuyec3bldhTPQrnPfzNWzDhCW4ImbRr80_U9cx_Hz1ghGUrg6vbDzMxznLI7HUl-dtC8D30RxjwYfJ5qp_lA8chXaYxGnCMNtCODTX7Nxt-B9BTYMKFHeZCBK_IHYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff21f4d079.mp4?token=PMhQYFiVn-FkG_0Vx8KrSkcZ3qH4GUp-4x_9fb4-iOhJGIIqR7vFPdyMI2AGlOjfVM8-pXaSWXBKGDBYQDcKRHN5Oeq9meykxsSwZPbDmvtEVHY2oqXDvWGHcc9Ofw61zh12OqF5sQI_pRWHBNL6uj04G2A8mUG8pH7uDewzoK2xIalCpEopM1nNvWWD8k6DPh8H-knH1ea25O5VJQlw5XKEnuyec3bldhTPQrnPfzNWzDhCW4ImbRr80_U9cx_Hz1ghGUrg6vbDzMxznLI7HUl-dtC8D30RxjwYfJ5qp_lA8chXaYxGnCMNtCODTX7Nxt-B9BTYMKFHeZCBK_IHYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش نمیدونم صدات به جایی بند هست نمیدونم چی  جونه مادرت یکاری کن امتحانا تعویق بخوره</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67866" target="_blank">📅 03:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67865">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRazis</strong></div>
<div class="tg-text">داداش نمیدونم صدات به جایی بند هست نمیدونم چی
جونه مادرت یکاری کن امتحانا تعویق بخوره</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67865" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67864">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فکت:
شما چند ساعت دیگه می‌رید امتحان بدین ولی من زیر باد کولر می‌خوابم
😎
#hjAly‌</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67864" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67863">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑨𝒕𝒆𝒏𝒂</strong></div>
<div class="tg-text">آخرین باری که کل کشور باهم دینی خوندیم رئیس جمهور مملکتو خرس خورد
امسالم که اینجوری شد
فکرکنم سال دیگه انقلاب شه
😂</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67863" target="_blank">📅 03:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67862">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cU_uC8e9zPy43Soj61agJiV5yEqjSBttODxK3o0ZCOY1HU6aCP1mEyWb1co_y2dgr8Kt7gr_mieNAmTCTqVX1cCzriaCcjpCBK5XRGk7cxdKLhgXLv-R1za9eJTDILXfTfGNmoZftaNMLZ47EQ5ElXuos8isz8mTryAi92GMQ9JuE0-XOE3kKiMiZSISH_-8ZyJfSLEuiCHksyZRaPJfuUHFd7_HbacSmF1bg3rglQXTzgJD3rUfCaq9Uq4cyXSXj1u_XeOl5sBAy1k9rV0C0CAV5BE3_9y9hi-AfmgwsCDn1QmyRjir1ovSfUzSO3ul1TXx0fsquqYe6LrZ1ytWMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقیش اینه به تعویق بیفته حداقلِ حداقل تو جنوب کشور، ولی اینطور کل سیستم امتحانات نهایی بهم می‌ریزه و باید بخش هاییش داخلی بشه، و البته با این مسئولایی که ما داریم چنین چیزی بعیده #hjAly‌</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67862" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67861">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSjvbG6Engg9TtVyzix8OdKLeFXmWW1moBke_xWwMLOF39jbB7pnQfpBjlJmCjTjCWdRwOTYLnUSk2W52zrJfHcGS7iNItnuCMDzMITBsKnDAUCzBZD4L-cr-J8rOBMzt5IhbVyq1xQtEuPBoNJNcTuujki67TE0zENdJK_iSXoyXRWZaTV8GaghbcuhtWxE5HCnLhXTgWnY5OGCGHTNtCMLUE3TSyvCFnwhONEFZukUM_XTBB_quoLpwJyg6MaVMk133v1vfndObXTJaqdRn0qfL9UT3laul5fzZ9N9ApmuiIAiOLTOv6iBJSrygqpb4E9nw_OCA4NlQ4iSYEFvvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا اونایی که نهایی دارن بخوابید توروخدا، تعوووویق نمیفته نمیفتههه #hjAly‌</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67861" target="_blank">📅 03:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67860">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K31vk9IZwpnakuQQB6s7AoWokMoKdSwt-3Q7k_tMH0_p9BlH3TV3K6Bm-Wn2jLhKj6g5AA3mNITeK6NYfLfjcSZQKopbkNdXimp2zk5M3WdVM1zgqYYH8zoL6wicFdWnLInCGsET2ud_M2aoDZ_z8YwGsFo1r8ZyGn6XSk7r0ANINkyFCA8MRf__xqBlbJMyZSyw50j_rBULNzO9SVN-yRgQegVV3zuD7OyoJy6OBAQQVuHvg4ZNJyFhMGt2Oxc_uhhocHo3wTpepA-v-FL22uIiC9N2tbmua61UNtQi8wDHvOpyV9Bt0hu9m66w01Dzk_r6V35pymD1zgAZNid0_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67860" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67859">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJSVSvQDol8T-yu-XX8Tap7vlJztGo2BsXk7Zd0475KYD4-wO2HgfDMyXUZ0Cf1WqWgLteINl5WhunDaLZZ41O9c5YsizFu9oLd7AcalnYkP0c9c-BsKpf2HHWLL6juQcX9CCjmbu7lL8gxJKnVKvsZqQc8i3VEdLHo6fxELszpUqJZBbTy4DzdEMrD4q_9AksJf4RJMZJPsj-hZ-caf1dPi-giVJyrvE2gk0GfgD4kD5vtiOW9arGoYErvCdoFiQj0T3JaeQzT4jN_iF8A4e4bM3-vcaCs2aygooyqvzg4qJW_vugcJ0zGYvU-Uuzovx79df0S-sBpy6zqSPJ21wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ پیت هگست:  ایران انتخاب ضعیفی داشت. حالا پرداخت می کنند.  @News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67859" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67858">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
نایا:
دو انفجاری که در جزیره قشم شنیده شد، نتیجه درگیری‌هایی در آب‌های خلیج فارس بود.
نیروی دریایی سپاه پاسداران انقلاب اسلامی و ارتش ایران با ناوهای جنگی آمریکایی درگیر شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67858" target="_blank">📅 03:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67857">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
دو انفجار در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67857" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67856">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=unYQEpZ23logiOM3oPboU_xvrQ0ypZKhuPWjan52q9l5JxClPrQ1Yz2tGly5szpMc8kixdSJslGJfOZ2LslZwDJCPilQ5A7QsKkFsMH-YZR7vgqOL1EqvdAH-vk8XI7RqAIEPdkf2rs5UlRd-VCk7JI38iI1rwMerxEasf96Acm01jgHt6AKeP_7EUnWQGH7VL31igU4ZEh5V1amBrAy6_274W0ayaTCtk-D2iuwAzPokd2dv1hQw0wBOxXrclntZbdEXXdytMwHpQowhInXSyfTEo3DVgSKZepr21XdCoxTIbY6RqvSRhWIf7Ov_CYKgkmcwck-r_z6zxLYMhONmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=unYQEpZ23logiOM3oPboU_xvrQ0ypZKhuPWjan52q9l5JxClPrQ1Yz2tGly5szpMc8kixdSJslGJfOZ2LslZwDJCPilQ5A7QsKkFsMH-YZR7vgqOL1EqvdAH-vk8XI7RqAIEPdkf2rs5UlRd-VCk7JI38iI1rwMerxEasf96Acm01jgHt6AKeP_7EUnWQGH7VL31igU4ZEh5V1amBrAy6_274W0ayaTCtk-D2iuwAzPokd2dv1hQw0wBOxXrclntZbdEXXdytMwHpQowhInXSyfTEo3DVgSKZepr21XdCoxTIbY6RqvSRhWIf7Ov_CYKgkmcwck-r_z6zxLYMhONmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فارس:
گزارش زندۀ خبرنگار صداوسیما از آخرین جزئیات حمله به جنوب ایران
تا این لحظه سه انفجار در بندرعباس، و سه انفجار در سیریک تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67856" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67855">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
خبرنگار صدا و سیما در عسلویه: صدای ۴ انفجار در این منطقه شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67855" target="_blank">📅 03:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67854">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
چابهار رو زدن
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67854" target="_blank">📅 03:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67853">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
❌
شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67853" target="_blank">📅 03:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67852">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCJeuNd1Y0qUVS4einezdVbs5CJi9pzw5cFJi531_1LmGu7U0733uXkPaCqArR1LTqZ5YrzqdvwigLHvLZez20P_j-vtLaJT9CcCayyYEPQXECb9_bRb-E1ZLme_H8yQLNmpM8qymAZLm4hIOyJPcCJCUE0td5XPpoduovy2FABaBzchtWzXu-KKZUTPeqdNBYnX0uyO9izLge8yGpRHTIlITrc1CFB9ITpLknlOgi67scBYgItpDzBM-gtc1WYzr7zToRtg2dFCIMSuGxV4CldLmYBjC1Q2lvtc5V2yOf46aEh4i605BXGWHlwMGpr_9ENVja5y8qEx2g5ugNMJLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ پیت هگست:
ایران انتخاب ضعیفی داشت. حالا پرداخت می کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67852" target="_blank">📅 03:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67851">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed7140b74.mp4?token=FkpT3AbbAcQt1sIXOCaJ1XZig1RcYvMb-bDA-f2qu-Zl2dUicpPKZjHLEgbvjxyTT0EedUBdSe96TsV1vniI3xHdWkYZy1dVY8rTjtiN7IegZlvU00xVq7AznL4D_Cr7NENpKbqrPOdCW6n5X8Qi988-ltvsszXuMdzvMVusHAkIyKhFUIdgU3yFmwGG_B-FAk-kEXgm56WdfZFB_L4h1Vq016DA1Pu8jM3gb5WXxUcFc7MkcRaouqK6Dg0u-nxyBUk1SGdGa7fMhQbwrm8Unp3R4QLoT0_ew6BLOtXOmBKRTsgvN5w3DwjMiDJ8phGM1qNQvDA8pdOHAFvhHIHS9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed7140b74.mp4?token=FkpT3AbbAcQt1sIXOCaJ1XZig1RcYvMb-bDA-f2qu-Zl2dUicpPKZjHLEgbvjxyTT0EedUBdSe96TsV1vniI3xHdWkYZy1dVY8rTjtiN7IegZlvU00xVq7AznL4D_Cr7NENpKbqrPOdCW6n5X8Qi988-ltvsszXuMdzvMVusHAkIyKhFUIdgU3yFmwGG_B-FAk-kEXgm56WdfZFB_L4h1Vq016DA1Pu8jM3gb5WXxUcFc7MkcRaouqK6Dg0u-nxyBUk1SGdGa7fMhQbwrm8Unp3R4QLoT0_ew6BLOtXOmBKRTsgvN5w3DwjMiDJ8phGM1qNQvDA8pdOHAFvhHIHS9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
شلیک موشک های آمریکایی از بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67851" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67850">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام):
ساعت 7:15 بعد از ظهر امروز پس از اینکه نیروهای سپاه پاسداران انقلاب اسلامی به یک کشتی کانتینری با پرچم قبرس که از تنگه هرمز عبور می کرد، M/V GFS Galaxy که در حال عبور از تنگه هرمز بود، به طور آشکار، نیروهای فرماندهی مرکزی ایالات متحده، سومین دور حملات خود را علیه ایران آغاز کردند. یکی از خدمه غیرنظامی ناپدید شده است و کشتی به دلیل آتش سوزی داخل کشتی و خسارت قابل توجه موتورخانه قادر به ادامه سفر نیست.
ایران فرصت دیگری برای نشان دادن پایبندی به یادداشت تفاهم پس از پاسخگویی به حملات قبلی به کشتی‌های تجاری در اختیار داشت، اما باز هم شکست خورد.
در پاسخ، ایالات متحده هزینه سنگینی را با ادامه کاهش توانایی ایران برای حمله به کشتی‌های دریایی غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، تحمیل می‌کند. این حملات به دستور فرمانده کل قوا انجام می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67850" target="_blank">📅 03:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67849">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16f69bf83.mp4?token=LquoL92e6LjTuhhuJ_hq44sIdqSwpikZJdhNNMhkE8cZTzp5QDnGdbaWTdOFBSNEJJWcmQLiIundOjuf6Hsb4-Xx58VWc6gJSGB6wd08wctlUqxgbU8gDVw17WPSDf-puru5aqdPbKe3PMKp8IOJp1-w1MV8LuSsaXrNJwXYxi1CczPRmcVgr8O6cQHrdcSOXDTdyIp9KUaIiPOaqBcwwNbdyMx8ZX1MpVOpRraNjkQfV-ZE-dmrnpbMNvEwjQgbGClJm1E9YxiH-m2YVRggOT3qYID_XnORiZO16P7Z5bZzTPNTP49SQegQSlcukKNAvMPcyg2DCcHcXXJfEqR1lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16f69bf83.mp4?token=LquoL92e6LjTuhhuJ_hq44sIdqSwpikZJdhNNMhkE8cZTzp5QDnGdbaWTdOFBSNEJJWcmQLiIundOjuf6Hsb4-Xx58VWc6gJSGB6wd08wctlUqxgbU8gDVw17WPSDf-puru5aqdPbKe3PMKp8IOJp1-w1MV8LuSsaXrNJwXYxi1CczPRmcVgr8O6cQHrdcSOXDTdyIp9KUaIiPOaqBcwwNbdyMx8ZX1MpVOpRraNjkQfV-ZE-dmrnpbMNvEwjQgbGClJm1E9YxiH-m2YVRggOT3qYID_XnORiZO16P7Z5bZzTPNTP49SQegQSlcukKNAvMPcyg2DCcHcXXJfEqR1lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67849" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67848">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇸
🇮🇷
باراک راوید به نقل از یک مقام ارشد آمریکایی:
ارتش آمریکا در پاسخ به شلیک سپاه به سمت یک کشتی تجاری، چند هدف ایرانی در منطقه تنگه هرمز رو هدف حمله قرار داده .
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67848" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67847">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67847" target="_blank">📅 03:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67846">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67846" target="_blank">📅 03:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67845">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
بوشهر رو بد زدن
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67845" target="_blank">📅 03:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67844">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
چند انفجار در اهواز و بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67844" target="_blank">📅 03:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67843">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
تصاویر بیشتری از اقدامات تهاجمی آمریکا که از بحرین آغاز شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67843" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67842">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=Fqm43l9F6T2PJ1e2U-jTfd_2XQ3jxwrkBh6BluDEBIFYWqbOjpwGkDPjKh073o7ocHR7TOwTB_wZCNwO9yUhKWkihsR6uCEYGaDRtjrjwPeZVLhjXtlQ2lq-Hygnw04pZJXmC0GHqDKZbBLCKkMghc6jvvDZSG4G9S7FXrcGiQqYItTbAdb8whnexywPbjenwDTPjUAEOG-JTAHcVRTClpXhv5H0BFYk09iDq00ZwL4tAgPh9dgTMbFlX0GC7-81zIV2S42o56lqqORxH0yhfC75fRWbGMBnxEua0Qk2f_sJ1DRNxo2y7r26_y9zCHDmBEXP8ZsFWrx54AFJ2yW_ezcCBHOG_3RqsElBk9RZIGGxCRiezarGs3w476JoIbEwWHaUGHJoUQjB6oZssa-oqIRM_nRAuRn66tkMGc17sjvU7AMWXqhtdqB-zAaQ6mlzYkwNsgvse1sU0GA5FWaJWXRze1uf-WhlCg-kQuVX35zf4EJhXoXy4rnDmrYWIgeMRnvvhMJdkcnL-4Fd9RepvAGOCsOmVULg7X8w0PtPFpRwrnZ0x41GUp_-1sX6ayTl9lD38gW3yEqb3yIHNVXco3x5GVrxb5AGmUAzkP2y5xYeZ7pgLuvg7NslG2FCTOiaipDy0WsyW6QZAyGLJMCOoSeasYGoSpx1zpvD5yXw36I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=Fqm43l9F6T2PJ1e2U-jTfd_2XQ3jxwrkBh6BluDEBIFYWqbOjpwGkDPjKh073o7ocHR7TOwTB_wZCNwO9yUhKWkihsR6uCEYGaDRtjrjwPeZVLhjXtlQ2lq-Hygnw04pZJXmC0GHqDKZbBLCKkMghc6jvvDZSG4G9S7FXrcGiQqYItTbAdb8whnexywPbjenwDTPjUAEOG-JTAHcVRTClpXhv5H0BFYk09iDq00ZwL4tAgPh9dgTMbFlX0GC7-81zIV2S42o56lqqORxH0yhfC75fRWbGMBnxEua0Qk2f_sJ1DRNxo2y7r26_y9zCHDmBEXP8ZsFWrx54AFJ2yW_ezcCBHOG_3RqsElBk9RZIGGxCRiezarGs3w476JoIbEwWHaUGHJoUQjB6oZssa-oqIRM_nRAuRn66tkMGc17sjvU7AMWXqhtdqB-zAaQ6mlzYkwNsgvse1sU0GA5FWaJWXRze1uf-WhlCg-kQuVX35zf4EJhXoXy4rnDmrYWIgeMRnvvhMJdkcnL-4Fd9RepvAGOCsOmVULg7X8w0PtPFpRwrnZ0x41GUp_-1sX6ayTl9lD38gW3yEqb3yIHNVXco3x5GVrxb5AGmUAzkP2y5xYeZ7pgLuvg7NslG2FCTOiaipDy0WsyW6QZAyGLJMCOoSeasYGoSpx1zpvD5yXw36I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر بیشتری از اقدامات تهاجمی آمریکا که از بحرین آغاز شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67842" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67841">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-mGWNOX0YnOPd4cjSET_EXjbyBPdABE8bfXe0BKeBX2-TZ0B2HVNLwebPhzLDc5wVQHz0R1x_k0eKm81L_6yxDqBYQCMFqv0PKxQdpILaBnODkI0yZy-3MpjStMYsgBwR9dp0Wuif6Da0gsBxCPNoxtGjLngCkJJoyft0qzGBz1iNUWVTYlgCFdOjJ1PBBlNAoRo5QbRN88ynY5OvtOeqpCx8Oqzac7xq-qr8ZsYHCL4Tei1epv0w9JTet_SFCvk5vw3hdfJsuCFh9oPP_LF0JnUqJmPGIfVR5mWTcQcuiXLWvqwMe25ltM106w7qDoQP1tb1NRcBkVYazj_p6fjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منتسب به بندر دیر
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67841" target="_blank">📅 02:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67840">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
چند انفجار شدید در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67840" target="_blank">📅 02:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67839">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
کاتز، وزیر دفاع اسرائیل:   من و نخست وزیر نتانیاهو به ارتش دستور دادیم برای انجام عملیات نظامی مستقل تو خاک ایران آماده بشن.  @News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67839" target="_blank">📅 02:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67838">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های شدید در عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67838" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67837">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b4e512f5.mp4?token=EebxJ-yVxdnKyH396roQAzeyw7Bqlza9YurW4fwy6-RvL47pCr3vly14rfRoEoU3laaojPvj4Ceq7znqzvmn_45FjXaWcaJm5oNYDp20O4wAS9y3re0MdKdwXmDhj0pmOb0fbk1cIzBKs-SoMo7LvpgaVkU1RA3IW6CHkrHWdT9D2QSl9axap4oUcN0mdZo5iGg8m9MaQvUTK6uw2FPLOzqGgz5FURjhA8IT8o1wh3sKQSN_p5HfgUlFrlFHJmuXqbr2WRTNNUSYN7mABdGmNa7u1r_5I_oE1kCB-BMtj0HLMa3xbP3jT0C9hFBf3XdmF7MTQRZwHud8XY-f0UfzfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b4e512f5.mp4?token=EebxJ-yVxdnKyH396roQAzeyw7Bqlza9YurW4fwy6-RvL47pCr3vly14rfRoEoU3laaojPvj4Ceq7znqzvmn_45FjXaWcaJm5oNYDp20O4wAS9y3re0MdKdwXmDhj0pmOb0fbk1cIzBKs-SoMo7LvpgaVkU1RA3IW6CHkrHWdT9D2QSl9axap4oUcN0mdZo5iGg8m9MaQvUTK6uw2FPLOzqGgz5FURjhA8IT8o1wh3sKQSN_p5HfgUlFrlFHJmuXqbr2WRTNNUSYN7mABdGmNa7u1r_5I_oE1kCB-BMtj0HLMa3xbP3jT0C9hFBf3XdmF7MTQRZwHud8XY-f0UfzfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شلیک موشک از بحرین به سمت اهدافی در جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67837" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67836">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خسته شدیم از این چص‌حملات خدایی، قشنگ بزنید جاکشا
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67836" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67835">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
ارتش آمریکا رسما حملاتش به ایران رو آغاز کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67835" target="_blank">📅 02:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67834">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از حمله به بندر دیر و بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67834" target="_blank">📅 02:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67833">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67833" target="_blank">📅 02:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67832">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش‌های اولیه مبنی بر شنیده شدن صدای انفجار در منطقه عسلویه منتشر شده است. منتظر تایید این خبر هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67832" target="_blank">📅 02:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67831">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4398edce9.mp4?token=bbKv_p92q3_Nw0f9EiaupChfFzRNaYq_Q_wWa_qR-GlkFSyA7Lh35X2x6Q2YGONlR8NPiow3L2fOz1kXkufocG_rWwjaB9ikVeazJlgT0bL21oFx_lejiFWbNakNnrUi4PnTc8hW46rYC-gS0eMN4422a_DNeXFvjZIcf1E9WsD-zBUWn8xlznYUpHQzJrAktLaM9ssoCofIl4zNA2gA89uU_Spj9MoXygQr-5zwxV_e1RyjFItuEgFqlSPuZw2s0wRFvBjCVcHNZcb_HSHY5zTzhzxAOdVIIFCFpmSCHmZD0hqh1nzvZgG8-Fdofbz4NIE4PyTFBHrshaEDG2rQnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4398edce9.mp4?token=bbKv_p92q3_Nw0f9EiaupChfFzRNaYq_Q_wWa_qR-GlkFSyA7Lh35X2x6Q2YGONlR8NPiow3L2fOz1kXkufocG_rWwjaB9ikVeazJlgT0bL21oFx_lejiFWbNakNnrUi4PnTc8hW46rYC-gS0eMN4422a_DNeXFvjZIcf1E9WsD-zBUWn8xlznYUpHQzJrAktLaM9ssoCofIl4zNA2gA89uU_Spj9MoXygQr-5zwxV_e1RyjFItuEgFqlSPuZw2s0wRFvBjCVcHNZcb_HSHY5zTzhzxAOdVIIFCFpmSCHmZD0hqh1nzvZgG8-Fdofbz4NIE4PyTFBHrshaEDG2rQnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
کاتز، وزیر دفاع اسرائیل:
من و نخست وزیر نتانیاهو به ارتش دستور دادیم برای انجام عملیات نظامی مستقل تو خاک ایران آماده بشن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67831" target="_blank">📅 02:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67829">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
تابناک:
گزارشات تایید نشده از حضور تکاوران ویژه دریایی سپاه  "S.N.S.F" به صورت تیم های غواص مین ریز  و قایق های تندرو در تنگه هرمز مخابره میشود.
این تکاوران از یگان های نخبه دریایی ایران مستقر در مناطق دریایی سپاه در خلیج فارس هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67829" target="_blank">📅 02:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67828">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بابا اونایی که نهایی دارن بخوابید توروخدا، تعوووویق نمیفته نمیفتههه
#hjAly‌</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67828" target="_blank">📅 02:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67827">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🇮🇷
سردار عظمایی فرمانده نیروی دریایی سپاه پاسداران کسی که دستور شلیک موشک به سمت کشتی در تنگه هرمز رو داد.  @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67827" target="_blank">📅 02:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67826">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guQ-E7BJFlL13QFDksv6ENAFjPwn31a3UKMaEo-eP_u8XGnqHRNrYT7LVXsfae8n2tnpJ6vDFMMjcx3S8O8zdxZJP4i1aUFjAykKnj43GDN8d1eSluOi09nObeoak76xSrMJBUBx_4kxtdcYqyyWZEOg66xfWCwRdb728onEQbFQfdD3A1tvCREq5MkinDaxpDOh6NlR0vlLVMTciErJzWr1Y4jpXMQJQGXHRvr1PfGm5ikvMyZnN9yIMN3SBjwANR_nytPRcU6CruDD4T4g6A3al1yPUUNdJj1hKI2Rr-ZYhmABde7p-H5nZExiZQPTGFQ4rjoKCq0solKhHRfSMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حدود 35 دقیقه پیش یک موشک کروز ضد کشتی از سیریک به سمت تنگه هرمز پرتاب شد.  @News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67826" target="_blank">📅 02:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67825">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HD7WmcKnIKENHggre-31T7AbpEqKaXPOSGmrLS6R69sKSfXfuZFdCe7HMBKQ9iiK9zcNHYK3P88oxusmN4OQddUnDdPpftYD6dPUH8wz7qRw4vkFGEalgCgKhAwCQtEp7EDj16Dz9M5oX9QmH6Z3jhEAX42dV7fbid2AruuiuKz0cg7Jrg5rtMbJ2uShpPt1cwQkCL7Mei-HDBOiu_LBjmMdPzNWXkjtZD0ZY2c2w1pQIWt60nKnm55mppVSub8mk09bekrnTThs14jsQPwC2QLvn6xNEevn34GCNOSfO_eLei1-O7Lj255ZXolW18sDc6omaE77Jj4Wv-fV6NsP9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هم اکنون زیرنویس شبکه خبر
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67825" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67824">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB332lVk3J1ho4Zp-UnGzRsbAPbpksWZPeh9Xwaodw4RnaOxHadSLa2zYcM-jymbgZ9tkKGQQxibJoSNBB_QNVQ0hs17TSGBgiVzomch0dvnwAAraGlYcLAbFS_VW3LwsHQNFvRZNeOm8Rk293VJL4t1-etjJ-Wq1fgHIbKWI9ZhHgQBdWm86KrtYKI8ZD2XKUNbvlimQ2YZoL1oyNUM7EUJqlP800uPmxJat0yOKhu9xR15ik9kLBKe1UddSF4bflwd0LZNSm7qXR7Vcng7TgNYlNOC1nGq4lC3xTOUYwkLe_hb3iswh5T00FG3R1KrLWxZ-nhqOJdfgbANJXIZig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سردار عظمایی فرمانده نیروی دریایی سپاه پاسداران کسی که دستور شلیک موشک به سمت کشتی در تنگه هرمز رو داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67824" target="_blank">📅 01:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67823">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
صابرین نیوز :
به دستور مقام معظم رهبری، حضرت آیت‌الله خامنه‌ای، مدظله العالی ورود به تنگه هرمز مسدود شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67823" target="_blank">📅 01:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67822">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
حدود 35 دقیقه پیش یک موشک کروز ضد کشتی از سیریک به سمت تنگه هرمز پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67822" target="_blank">📅 01:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67821">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🇮🇷
بیانیه سپاه :
همون‌طور که توی بیانیه قبلی گفته بودیم، هرگونه دخالت خارجی و تعیین غیرقانونی مسیر حرکت کشتی‌ها در تنگه هرمز، با واکنش قاطع ما روبه‌رو می‌شه و روند افزایش تردد دریایی در این تنگه رو مختل می‌کنه.
چند ساعت پیش، با وجود این هشدارها، چند کشتی با تحریک طرف‌های خارجی سعی کردن از مسیرهای غیرمجاز عبور کنن و به اخطارها و دستور تغییر مسیر هم توجهی نکردن.
در نتیجه، یکی از این کشتی‌ها که با خاموش کردن سامانه‌های خودش امنیت دریانوردی رو به خطر انداخته بود، هدف تیراندازی هشداردهنده قرار گرفت و متوقف شد.
از این لحظه و با توجه به شرایط امنیتی ایجادشده در پی دخالت‌های غیرقانونی خارجی،
تنگه هرمز تا اطلاع ثانوی بسته می‌شه
و تا زمانی که مداخلات آمریکا در این منطقه ادامه داشته باشه،
هیچ کشتی‌ای اجازه عبور از این تنگه رو نخواهد داشت.
همچنین اگر دشمن متجاوز به بهانه این حادثه، که خودش باعث به وجود اومدنش شده، دوباره دست به حمله بزنه، پاسخ ما قاطع خواهد بود و پایگاه‌های جدید دشمن در منطقه رو هدف قرار میدیم.
کشورهایی هم که اجازه دادن نیروهای آمریکایی و اسرائیلی از خاکشون برای این اقدامات استفاده کنن، مسئول عواقب این دخالت‌ها هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67821" target="_blank">📅 01:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67820">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
#فووووری
؛سپاه پاسداران انقلاب اسلامی از مسدود شدن کامل تنگه هرمز خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67820" target="_blank">📅 01:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67819">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2J7UybzxW6fzCbz5oSHW2iaysZMve6JRkSiv_yIf1_MO6fSEjeEJL69WvpQaK60-6663Tn0Ry-gO4IoTlIUUQfsAQGxNKz1ooBPFpkeNqLnVovDpgCIBTd7LOxuUUdPDVG8DgBPK1EC2x0omEX2oiQL-X4WBNb1hDGH_CBVJbG6AMTtlr8mx2QIPoDhbAsjxGCPU63UtbgBoyRMhpU0cfT6YST2QFw39_YLEGmytkcozs5dQVAvpmz62RnhhyNKR0FuPOP-6eWdPmFvWjivRqbuYJeZ7TR1GaTr1ZXGvwb8aRQTxI7XGyasTxguK9k7yYa9k54YAPWoHi0r95CpgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67819" target="_blank">📅 01:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67815">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ufYi8aKQcurubgjuYc-7PY3tSqDe_AfuG1TpsLsQbnxxfh4iJ7vQF0OwQStnOIdcyQo1RViCdOFosu3FXfxRvb0CLq3Y0tDOafDfv4g9MpjeuAuh63OGaFtL-np6GYvhv2d2vxTl3pGM4mp7GjBsz5Xg0t-PvE04IzSw55r5p_I6VVYBhYMXOOBzUXU58P7ZFYHMuhGSv9uywjL8moAtsTB7u49arKhnz5X0xELNAYEAe5obXG8rns5UR7Ze7-CGAzFfMFGGQDduA-FN6SLseqxlIXMOojHdq3XFiwi_Ad4EjnWi26LyHEwdbR3dL7FJiLQh7u_qilDDBQI_AFHr1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JTDRD5hbtc3zNuLXNIQ81luRd2GpWSl1DSC9s6Y4FNT-XotQuaSsOgMfU7KMs_LXzGYeR-DyKZjuBFcHLCxkiEdujQnfMqRkp6C5J_pGIdeUdnWqBHMG06BpmsEi358IUlN40AnN_-V-XtdJVzNSEuFJ8J9cKCbGcccALd3MqhO93gh8X6CA9TGqFgBJs2msd77zIcClOzlII4No8A94QOck-JsFM0ljKl2X3QS2E9Zry3D3K-5kxpLqU6fIGoa7FAfxqnhve9apCbFpMnxnzjzPaw8_WWxPRrsAm_7f5YcRz9ezZ312qkNzeICnTdh2Hlpnaa62ssGUO8PORLfdeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LXQBJzXmqaK0CuJYNJULGHdL9aM6kJKXAqsxq9sFN8rgXSQLUY_RhcavadrIrp3pJkp0sIoZsbicn9Njq7E1P7dDTuKKvq1Qyb5m8kGiqS1hi6gZG9fogioQFqnTFU0x4lvI4SEWJUdGounYTO4sQ49tDD0hv9yPXCzf7QqFXKPDp_0aAkIAqjVOfhOLREUMl36xoVCx0HU2bFeVhOYutbtr7FJ0vxSyUe1pDpNYwz-CQQPzR_qWvlqz227CC4szEF2QDVxT7-otTvZp0JXfR32wrzP7UQTa_Tm8p-jYjBr9bfHZ4cNgepBcUtbV5QHWENxuS1yAHiqSt9Ex8MTqxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VhU08_O6zg6A4J6wLn2v682LJZb9RYYpipWIvKjIGJTVvyp5J9q8wpn7x8i7yFVj3TOmddwuokBSzarWs-ZEN60xqa_POJk2fSajuSwRKz004wFJFriNmOsaDra0BLNKvH3LpiAXtKTCsUEhC_nIAEXgF-TPaEnRICm6kWbw-hkS2Hj7TamB4gZHzL4_mWOSKVk0f86gv5TWmpepgyLYssJGTRmE9YldPrrMbSA9UntHbkLR_j9S8AGPSjrLqmzrL46fErpjPmX7liVTj1m8YRLcuxnHTPWua83x6UwjJsB9g6UkRBU-1AEky5Nz1RN6FynEXAOasYt-R31Q1jJntA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚠️
هواپیماهای باری نظامی آمریکایی از نوع C-17 در سه پایگاه نظامی که توسط ایالات متحده در داخل اردن اداره می‌شوند، فرود آمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67815" target="_blank">📅 00:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67814">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbae51b67.mp4?token=lPpRU3qN-EdZvqyJTuWbmND1j1dNpRQMRLjNz8lsnM7Thgxi5kpYRoc0lHpe8UN9mkw20DjgK2ijGuPuR51fCIGAygbXVqroRQmcMvYmfnlFFZ-ToNF3E4eHg_EO2JQeLkbwc4j-lKgfH1h9ZnE2l2W_1f1Pbghv-suioT1MoWdFYdul9_Tc85xNfd34S_4I03LzOqT8UGsj_VBThEUDoeI7tT8BNM2sBiOgIiMuVCOl1kTQBJTumdIAkflsXPQGrpQ_G2JhPHYgFB0SCYAatG6ZbrZR9dHCyIS-IWoHYcOD4wEe1D-URuKwwkdz9a6_IoGvA7gy3OuSb25773BacQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbae51b67.mp4?token=lPpRU3qN-EdZvqyJTuWbmND1j1dNpRQMRLjNz8lsnM7Thgxi5kpYRoc0lHpe8UN9mkw20DjgK2ijGuPuR51fCIGAygbXVqroRQmcMvYmfnlFFZ-ToNF3E4eHg_EO2JQeLkbwc4j-lKgfH1h9ZnE2l2W_1f1Pbghv-suioT1MoWdFYdul9_Tc85xNfd34S_4I03LzOqT8UGsj_VBThEUDoeI7tT8BNM2sBiOgIiMuVCOl1kTQBJTumdIAkflsXPQGrpQ_G2JhPHYgFB0SCYAatG6ZbrZR9dHCyIS-IWoHYcOD4wEe1D-URuKwwkdz9a6_IoGvA7gy3OuSb25773BacQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک پسر هیجده ساله یه رولزرویس رو یک روز بعد از ترخیص شدنش از رو کفی دزدیده
یعنی رولزرویس رو تریلی ماشین‌بر بوده این با هیجده سال سن اومده دزدیدتش.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67814" target="_blank">📅 00:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67813">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SV7hKvBjHoZvOHzNEQWG8X-l4OpRrd4e7WesToUEzz-voiCK11qre1a4dwPDQ7wTvas4NhzW0jXN7v_qilJIB0gkr2pu3wBZFrbz0CqBQIEXQcK0_pzHZ9yywimhv-t5BrvkqdvgezFE0lH9mHRmwYrxiwBP4p9be5tO6Op65DsLLXbhF7kLmi9QvL9r1xmpxxs9dqNtdY0JZ8_AKGHLWjyoLC4IN1EhPI8wE9mfhB1Vpg2FruVAJoNJrnsIFbOTsnBGCAXA9beWcrcyF13-xZTxawQyKhqBKEYI4hMW4n4nPWqj2GkkqV2GK0DGESWpVj1uULQ_Ir_TmjxqrgU0hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کانال 14 اسرائیل:
اعلامیهٔ مهلت ۲۴ ساعته دولت ترامپ، که روز جمعه، ۱۰ جولای، صادر شد و از ایران خواسته بود تا حملات در تنگه هرمز را متوقف کند و از آزادی تردد کشتی‌ها در این منطقه اطمینان حاصل کند، در ۳ ساعت آینده به پایان می‌رسد.
این توییت دو ساعت قبل زده شده و تقریبا یک ساعت دیگه مهلت یک روزه ترامپ تموم میشه
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67813" target="_blank">📅 00:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67812">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
🇺🇸
مهلت اعلام‌ شده ترامپ تا پایان روز شنبه به‌وقت شرق آمریکا ادامه داره که میشه حدود ساعت ۷:۳۰ صبح روز یکشنبه به وقت تهران…
تا اون موقع به ایران فرصت داده ترامپ که اعلام بکنه که تنگه هرمز بازه…
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67812" target="_blank">📅 23:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67811">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrPy-5tqO9A-OZDlYgFdN3vAlShl2HbN4XrijGujW7AqBJqs56RxyjpKFS0mL7aAqKJ4PLetf9B5avjddx6C_Iz5gPdhcuV_-Sw1-UpsmFuz59p9lvuYIV9g3g0hLfcPgBeS31e361rMX1UC5fiuAvFXuXkcKV0-qfVLBBLvUo7pJweP69dUWGnXVZCENBqS_8wrGM4g3cg3pMp-5JumbUQM82vhrJC_RxRMDgPKSIjOrRlp3lgz3C1wLyb7MO8HmoHKkh5vO31owiQIag6qNcEfh6ezTVh-0yepDGrNeqm9pKs7C0Imds6a5ECntCdDjMIuCZyxN0e5dHvVTlV_qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پویان مختاری گرداننده‌ی سایت های قمار که خودشو مخالف شاهزاده رضا پهلوی جلوه داده بود و معتقد بود عاشق جمهوری اسلامیه؛
امروز صبح ساعت ۶ با هواپیما به فرودگاه امام تهران اومد؛ که توسط وزارت اطلاعات بازداشت و راهی گونی و منتقل به طویله شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67811" target="_blank">📅 23:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67810">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7GPwqpDv8LSgL2OG0nT6TLVKguCu8YrRc2C1jNMktYbNBA7EydVwCPActj0dKXSoyAN84tinrYxpyNOprJnvMofTXDh8gcOuUX4PqBGun6dsf5JWEBPsrmYb4bevH6vuqIAztgztVjql_9WyYWbPAetkLSutgVdX51NH9nL9Oggo_E3m-xUEGC5myq4r6zYuc6bxH9zYtvwOEYByttFwxLGfOJobW-YOlw4Qto2t3j5ptqlQ_pBtVR346Zz0CzXM7oVVnF_SoCU4y1l1IGCNg_V_i_-3sswOk9c80dK7uWWDP9zO_JsZbOwT7WpDOCtwqDiqrLNtv6cvsWSG12NDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علی قلهکی:
قرار بود سفرِ عراقچی به عمان منجر به صدور بیانیه مشترک درباره مسیرِ شمال و جنوبِ تنگه هرمز گردد و در ادامه نیز «قالیباف» و «ونس» به مذاکره اضافه شوند که با بازگشت عراقچی، گمانه‌زنی‌ها درباره به بُن‌بست رسیدن دیپلماسی در مورد «بند ۵ تفاهم‌نامه»، بیش از همیشه تقویت شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67810" target="_blank">📅 23:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67809">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
اکسیوس:
ایران نتوانست در این جلسه، موافقت عمان با این پیشنهاد را جلب کند و مجبور شد این پیشنهاد را برای بحث و بررسی داخلی در تهران مطرح کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67809" target="_blank">📅 22:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67808">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJFgKB0ZqL-vw-UX3SKCFvJ_GzR5rxWdHAXwV2btuzFhZhZyItkUqFsAKTVmmopX6QEL5SX9-EXPh1QIroRyuanTBM-E3dMUiTftzhEYzwDIbzZbD_N_Fbrz5oxfBIKUx8d2EiMTKOcWr59clLSWbBlnPL42ZGKppw5YgdPWFs7ciJGLHq9h9aGi_6b6yjD6KnNHENoSSa2cE8-Uuqn1XeAeBtT_nogwCbfd4srTByb76MAsGQjyW76eoc0xC2Og0BFIoQmMA_Wb2bIno3TuONjBbER8CpVLJleBB7IxDzTJFlT8NWH09FnAfj_BNtxIM6tEB0vUMkkNccAVydgp4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سی‌ان‌ان:عمان پیش نویسی را برای مدیریت کشتیرانی از طریق تنگه هرمز با استفاده از دو کریدور جداگانه کنترل شده تهیه کرده است.
بر اساس این پیشنهاد که هنوز نهایی نشده است، کریدور جنوبی از طریق آب‌های سرزمینی عمان برای کشتیرانی آزاد در شرایط پیش از جنگ باز می‌ماند.
کشتی‌هایی که از کریدور شمالی از طریق آب‌های سرزمینی ایران استفاده می‌کنند، به تایید قبلی تهران نیاز دارند، اگرچه ایران هزینه‌های ترانزیت را تحت ترتیب پیشنهادی اعمال نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67808" target="_blank">📅 22:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67807">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d2e49f67.mp4?token=FOR78X1do2lW7sfG3oRrRTSX1Z5jsvNfHUE3K1ECRy7QZRDNpgbdLtSo9Bd3yqs4vapraiP5rBiz-KPWiZ-w9JqhN6kx84GDhJMHRKbJbAxVbXG_N4V-AOtdqPxDWjacr4ipig0lLWvWoaqjt0emR-ZhqxZFJi7-3mT8Wh1Cp6_PihVg4WjVsJsCQF7FWFkGYGfCZOleRiRrSsqs4_0pBsEvPPSsdbjqWjZvhXHcZLBo7ZlMqt2Qua4qm4xzMjAeMl2BBpqWodnhHClZ-wF48fPNhUUmr4-KLe2mcB7PC8i0XrcL6pV4bHbZXJsEI_Z5Pi0ORSX9CRyYotzf3YNfoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d2e49f67.mp4?token=FOR78X1do2lW7sfG3oRrRTSX1Z5jsvNfHUE3K1ECRy7QZRDNpgbdLtSo9Bd3yqs4vapraiP5rBiz-KPWiZ-w9JqhN6kx84GDhJMHRKbJbAxVbXG_N4V-AOtdqPxDWjacr4ipig0lLWvWoaqjt0emR-ZhqxZFJi7-3mT8Wh1Cp6_PihVg4WjVsJsCQF7FWFkGYGfCZOleRiRrSsqs4_0pBsEvPPSsdbjqWjZvhXHcZLBo7ZlMqt2Qua4qm4xzMjAeMl2BBpqWodnhHClZ-wF48fPNhUUmr4-KLe2mcB7PC8i0XrcL6pV4bHbZXJsEI_Z5Pi0ORSX9CRyYotzf3YNfoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سی‌ان‌ان: برای نخستین بار جزئیاتی از حمله موشکی رژیم جمهوری اسلامی به ناو آبراهام لینکلن منتشر شد
.
شبکه سی‌ان‌ان در گزارشی به موضوع شلیک موشک‌های رژیم جمهوری اسلامی به ناو هواپیمابر یو اس اس آبراهام لینکلن پرداخت و جزئیات تازه‌ای از این رخداد را منتشر کرد.
این گزارش در حالی منتشر می‌شود که تنش‌های نظامی میان واشینگتن و تهران همچنان در سطح بالایی قرار دارد و موضوع امنیت ناوگان آمریکا در منطقه بار دیگر مورد توجه رسانه‌های بین‌المللی قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67807" target="_blank">📅 22:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67806">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
کانال 15 اسرائیلی:
ایالات متحده منتظر پاسخ ایران به درخواست‌هایش مبنی بر توقف حملات به کشتی‌ها در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67806" target="_blank">📅 21:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67804">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08bce6837f.mp4?token=Hpw6pqBEEEKyE81eYN0gVODFsgJXyqcQJwS0JYtpbr-EFWKdtCRKLbxaGJ0CLNxjwN70V0BswXFw9KD_0UP60qb5q9gc-xGNvxkjgcCXlom9oqN9MsEZjcInCyT29yyoqpx_M2Soqb9Kbf5mDwsTVYHHRkx-WDkbMP2TrMxVLjq8wEX7oYcrLP23gq97Oe3HAq77YTW58Xvfy1VSK1m8NqcvDwcu-V2bT7B0FKsXwYKjTaAj4LzrOzk8nwN4i0tsAyi9wpva--8BYUizFB4uzj_TFX4X-BEoWtRSxtvU1fna_my5z80G7ls4WEiA4HsR9YfrnPbnoUYzVe4qcySB9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08bce6837f.mp4?token=Hpw6pqBEEEKyE81eYN0gVODFsgJXyqcQJwS0JYtpbr-EFWKdtCRKLbxaGJ0CLNxjwN70V0BswXFw9KD_0UP60qb5q9gc-xGNvxkjgcCXlom9oqN9MsEZjcInCyT29yyoqpx_M2Soqb9Kbf5mDwsTVYHHRkx-WDkbMP2TrMxVLjq8wEX7oYcrLP23gq97Oe3HAq77YTW58Xvfy1VSK1m8NqcvDwcu-V2bT7B0FKsXwYKjTaAj4LzrOzk8nwN4i0tsAyi9wpva--8BYUizFB4uzj_TFX4X-BEoWtRSxtvU1fna_my5z80G7ls4WEiA4HsR9YfrnPbnoUYzVe4qcySB9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ارتش دفاعی اسرائیل:تروریست‌های حزب‌الله در حال انتقال موشک‌های ضدتانک در داخل منطقه امنیتی در جنوب لبنان بودند.
این تروریست‌ها موشک‌های ضدتانک را به یک ساختمان در آن منطقه منتقل کردند، که نیروهای دفاعی اسرائیل (IDF) آن را از هوا هدف قرار دادند تا این تهدید را از بین ببرند.
پس از این حمله، انفجارهای ثانویه شناسایی شدند که نشان‌دهنده وجود سلاح در داخل ساختمان بود
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67804" target="_blank">📅 20:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67803">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e14ad8a91f.mp4?token=M3mgcNpkWtrfOyUTk80mnN2cuLOVa0IcuhYblmzeawHVqGt44CkKRT3MSkLa4U_G0Kq9LuemYhq0MP1ttdY3eFX_d7bit7F7iDnMC3preZlVkDzCBqkGQoTkGDsoSAYCyI__JzVyuZZD6vXDzXxE9PHLMHzfdcqDdZwPOzbFkWvWkxlagXVJzVlvWP3FGq-3GSZVB-KixaSeRv7nvDkNCXf9robcbeQ_E0PIINEN2krXFGVpunGyp6eCQKF2Kln_e_SYiaEfhFny7ZHDJQEIHNijT0fk6xuK_MQOc0lutX4kpImewRstxfmeW0RnPqGgTXO-ukC1U4AbeuTScJC3qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e14ad8a91f.mp4?token=M3mgcNpkWtrfOyUTk80mnN2cuLOVa0IcuhYblmzeawHVqGt44CkKRT3MSkLa4U_G0Kq9LuemYhq0MP1ttdY3eFX_d7bit7F7iDnMC3preZlVkDzCBqkGQoTkGDsoSAYCyI__JzVyuZZD6vXDzXxE9PHLMHzfdcqDdZwPOzbFkWvWkxlagXVJzVlvWP3FGq-3GSZVB-KixaSeRv7nvDkNCXf9robcbeQ_E0PIINEN2krXFGVpunGyp6eCQKF2Kln_e_SYiaEfhFny7ZHDJQEIHNijT0fk6xuK_MQOc0lutX4kpImewRstxfmeW0RnPqGgTXO-ukC1U4AbeuTScJC3qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که رسانه جبهه پایداری از تغییر موضع ممد سامتینگ نسبت به مذاکره با آمریکا منتشر و وایرال کردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67803" target="_blank">📅 20:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67801">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vfGLOAM0aufkFAJTQUYBeZiU62kQcDYJKzZIui-jpylyFVH37SVhqORyHNf3T5Q32fH_aBMXzS09LmyX7L-gz_0h6I27M8scPKnduQ6GAlg_A64bZ9dHYWS7G_XmhjaIeOEMKBWknKmUjkV7mC_MYg_Z1UUg0FoTFNvzK1Oljn0YfuRmBeI_vMkJHILvCWqlLg3DKzdFzRCZOZvNCAQYWgw84tDXry-b0gDY0BxG8C3LQ4oBJ8knvtKsG4jh9KJBFpF1CmwWb4jYr0_q_KA6IYhW4XRc-8dT2eKc1QQ3EhJhU8I-Ukdye_E3h1eiyzdU0pakmLH_2XsuWLJTKbXNoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gp765VBY-Kvq2q6dnP9o2CVZCMO3_yJJ7BaA5C_Pl_sXyr1y7A5i2RdT1Oi5jq2dGH41EjwquMEGlSw-Xec5FX6Mx-Dwa8E69VBUWn6y1Roo1YTUWP0RsL5__Pka4nuF02DNywKu9sVtKju4RVKS9KquDhaTSZs46f6Llk_n38MX4Zu_-nx620MBxozszyKpMoDtSQUiCsIAFf6ByEw06GRPSLIV5zNB4sjWLydrVEOeSbTl8GIpa9kboHG1BuoHW97PJuRGmnxbAasRbq5NlzkOBB6Pjv3dMM0S1lHrjz7okfSapziDbV3OMYoMXBiBNna-iZ0-cqNWC_goprCr_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بسیاری از هواپیماهای تانکر سوخت‌رسان آمریکایی از پایگاه هوایی الامیر سلطان در عربستان سعودی خارج می‌شوند. این هواپیماها معمولاً پایگاه‌های خود را در منطقه ترک می‌کنند، زیرا نگران هدف قرار گرفتن توسط دشمن هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67801" target="_blank">📅 19:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67798">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSxBEYgQP56FiCsRWK9TBi2JaO8iR6koDo81C3ups0FlitDNMmNEMt1eXhwDLKT4gG_r9tP7c6aeXUaaPIggxEThzn8lsUqn8q0_yiHUSNLu5RzCe2NXtTWLyAn5NIU9WAL1Nq34d41XXTWvolJTZ8037pu8xFJVPN4izIb2m6xk2wfl1VYUJBh2LU-iWaQmUar7bcSCRKzmPEZYke9uixFXVqQ0AJvZqRp6EfmCwZ1khyad3NUwZAhscLFBNH1WoPowFzwA6ICVGl91c3ulIEB63prW9j6HMVj5RJMFTBm-dLpgvOofSfEpWBJ_6KdBLepDHTIy-8Ml73jns1uzog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنالیز و پیش‌بینی نتیجه تمام بازی‌های فوتبال جام جهانی 2026
💻
📈
🇫🇷
⚔️
🇲🇦
وین شد
✅
🇪🇸
⚔️
🇧🇪
وین شد
✅
پیش‌بینی نتیجه 2 بازی‌ باقیمانده 1/4 نهایی انجام و در کانال تلگراممون آپلود شده
⏳
🇳🇴
⚔️
‌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
󐁧󐁢󐁥󐁮󐁧󐁿
🇨🇭
⚔️
🇦🇷
لینک رایگان ورود به کانال
👈
بت جی‌جی</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67798" target="_blank">📅 19:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67795">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lky_LxwI66Ht8eYTvc9gGotorWa7fc-ZTNYjdAAj4bfPSijvlOqGoilZsJBO7w18oBis51DSc6TbVLmy39r2moXu2kiyfTYTIQG1W7x1gWMp1LTBTB6lRkZrpBa3fTliXkGdVeIMQLig_nAW-98RvOnAoSkbOcfbPKBz9YHz8Zd6-XryE4nGAPKun4jh6YXesXSd_OrWuMdFanmdvmWbMV-g30nvi0zXPmHsjdHTyaSlEsR3QCMg8QIajTtWLC4quB-oZrjf0zryIZGolD-FlKbhUOdqda8ng6vKg-WRJ5vUoMccwsb3CCvOrMkkHivO5dprFmd6GpVOnF5gFiQXzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
به گفته یک دیپلمات مطلع، مقامات قطری در حال مشارکت در مذاکرات میان ایران و عمان در مسقط پیرامون تنگه هرمز
هستند.
یک منبع منطقه‌ای اعلام کرد که طرفین در حال گفتگو درباره بیانیه‌ای احتمالی برای بازگشایی کامل «مسیر میانی» در تنگه هرمز (که در آب‌های بین‌المللی واقع شده است) جهت تردد کامل و آزادانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67795" target="_blank">📅 18:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67794">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00f69c138.mp4?token=aJEL_eFHy3lUTay9ux0nf3JACFVqNmIF1TmYDcvbw-4DcUsg2d_M34ZwL9jJB_5E0-eAtLIG38ajAZRXpCC9Ls8g03KTQDEpP26QF3fLZKtt6WhITrj5M5Fs7A1i0xJ-8LYXRBZyxa8b0p362AkMei3LtZQmR3Vc6YLf8HQLzp6EFbLfJF2ICts_MQl6QEfF3_qx9fBPgv-B_O9f45Ws3QHIcsMdJ3qUfTHrr1KrE291upKp2WuCSN2LQSkAoD_vFe_MXmCR0JZSNVIMwg-mKziNlJbxvI4cJUjE1lb3_qB6nqdaj9z1YzYbhcYnLZRFg1kDhz4pzaU_xf9EBjx76w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00f69c138.mp4?token=aJEL_eFHy3lUTay9ux0nf3JACFVqNmIF1TmYDcvbw-4DcUsg2d_M34ZwL9jJB_5E0-eAtLIG38ajAZRXpCC9Ls8g03KTQDEpP26QF3fLZKtt6WhITrj5M5Fs7A1i0xJ-8LYXRBZyxa8b0p362AkMei3LtZQmR3Vc6YLf8HQLzp6EFbLfJF2ICts_MQl6QEfF3_qx9fBPgv-B_O9f45Ws3QHIcsMdJ3qUfTHrr1KrE291upKp2WuCSN2LQSkAoD_vFe_MXmCR0JZSNVIMwg-mKziNlJbxvI4cJUjE1lb3_qB6nqdaj9z1YzYbhcYnLZRFg1kDhz4pzaU_xf9EBjx76w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریاست‌جمهوری core:
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67794" target="_blank">📅 18:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67793">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VU3AkQdv5WoxrVr3DpyEc8tGrKgl5vMnF4Uysox9ns_Etskc9dnV2hWPwrgnyPXOcXw2rFQ_H2Uw32n8P4v5b2euz2u-cjtRlBU-aXlyYKCBJNa1wKvKBVPf2wkQc1gJgw9La8PS_iARQMFP46BIy4bjCiH57LdRN2SMJhedZcypkNkvQdCU-WqyWO_LHaNp5uMrE56JHiwnl72gT_tvNzVtt2ZiylnovYNb0JANjyPrr5MRMkSaGNafkVm0vGb76eonfOdzsuJaiz5Z8dfhl2rmYLRTw2UJxz59RToGNkkDo72151CzHna1O15ScMZcjIsgaqFrHbjs2zsJzm83bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری مهر:
یکی از نهادهای امنیتی برای حضور فیروز کریمی در  یکی از شبکه‌های ماهواره‌ای گردش کار قضایی برای برخورد با وی را تهیه کرده و در دست اقدام قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67793" target="_blank">📅 17:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67792">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOeO66GfLWopZQIraNkSwsfAXv2t0AyfCvFqvF4AAcki6UZNYy_O_Jmaiyu2RXVq3sZYlzc6PZEtiYkJnwzfxE6bb-csji6xEv18emers6DL_gF5qp_aRoGFLSCGolqjAIXvZjGUFWVKvxnZJXO-XPmcERxE1fZrZ81r7te0BHVob1PTy52m4nvJKQmyd9_rf0seAIkQpoSxFYQMZj9hCiHBXbLiM-o1_WigXdm8zLPATbLLkeqRiUwv1mRk9q5Psnj6R5QfLv0QF1OicOltPpE0P4wQ7IncwE3fiVmAWmSLHd6cAwwZEG-NekNiVEWmzE26TbM9Hu37rEtJTDLNKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستهای این توله‌سگ خمینی رو ببینید؛ مشخصه تا حالا حتی یک ساعت هم به سیاه و سفید دست نزده. یک عمر از خون و جیب مردم ایران مکیده و حالا هم نشسته میگه «جنگ جنگ تا پیروزی»!
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67792" target="_blank">📅 17:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67791">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c1e2ae31.mp4?token=fAeoOM8N80FgRSh9BoQERrxet9NIdcZq74yG2N2HZuDgWQVEn7HT2Vbwu70j6iLuJlP3TJ7FR5OexsxjIQ_JzVcEvX1by7qNwcWSFlYprUq3uSvYzicBBPfy7xrtfu0xsQmefZ-H3fE4V56Zfs1UymFMTLd1SRHeeMBgGRP2Ii4KZcvIHFKVb2C9R84SCgfnE-8QW5tx6MzaaoYcZZgiykKqWQZULGRqtz9eNU4V3AgU5mCnq1a-iYAXw1b8dMrm_KfCzhq-BGKO3LZdTn8wz2SXGot3JpoQkqVqVjEQgE3RVtCCaKovP3mIAMyH2YiNepXiY3ypMo4eIKE11tyAcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c1e2ae31.mp4?token=fAeoOM8N80FgRSh9BoQERrxet9NIdcZq74yG2N2HZuDgWQVEn7HT2Vbwu70j6iLuJlP3TJ7FR5OexsxjIQ_JzVcEvX1by7qNwcWSFlYprUq3uSvYzicBBPfy7xrtfu0xsQmefZ-H3fE4V56Zfs1UymFMTLd1SRHeeMBgGRP2Ii4KZcvIHFKVb2C9R84SCgfnE-8QW5tx6MzaaoYcZZgiykKqWQZULGRqtz9eNU4V3AgU5mCnq1a-iYAXw1b8dMrm_KfCzhq-BGKO3LZdTn8wz2SXGot3JpoQkqVqVjEQgE3RVtCCaKovP3mIAMyH2YiNepXiY3ypMo4eIKE11tyAcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از کوچه پس کوچه های مملکت، یه دختر و پسر شروع کردن بوسه و مالیدن همدیگه، تا اینکه دختره دستشو برد روی شومبول پسره
👀
یکی از همسایه‌هام وقتی دید داره کار به جاهای باریک میکشه اومد و گفت جمع کنین بیست نفر دارن از پشت پنجره نگاتون میکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67791" target="_blank">📅 17:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67790">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‼️
ویدیو وایرال شده از بساط عرق خوری لات های کرج
😳
امیرعلی امیرعلی امیرعلی....
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67790" target="_blank">📅 16:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67788">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fW8b5hjWBfzvbBwUDCprtNUOsD4zgFyPGKj4ft-7d1BuBPAY6xlif8u4q0_vNkrgWVaJzlaxh4_i-2Ym_WTEm3lk0av9IFB8-vJNNy027W5PWn051byYWpjVijLkE3vzVcrdiuKOviQPdoRk7GBCFVcukrYvKOEq7yCIPy6wRuHk1sPcf7kNyBXpA2e7BmTcqsldqNGrPAJ1iVTA7RJJtJC4liszipOAYPQURHD3Yo68i7TPc6cRNQnCaw4r2mYK0rLxk4LpwxEBCzOikaE4zKilw7YkVmCC0JIc8RP_o1LKBXpymIrOcheBi7X7JTd_pfibFmdivoSUCnNHmKHOHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3354c0af73.mp4?token=gBh8DThOUpR5snxwe2AR5m9VQVyS3oF83iD8ebxeoUPEaN3idQ3bXApWwIIq0tyE_FZ5gJfineeLvDU5X31QBRzlOXtVC6wrCtspkHckf2-2auwdSUGuzNLF4eJy_qTKodE_ijOtZ2to4dPlDrm5Ld44jdY5LIc00kmnqQOm6ju8-PAqRO4DEWtUmANs2NYMi7Ux5oe6AFcR5TaG0H-MVZaMBHv5RTt5ZZP40aE9aa_-VVPbSzdsyt-MCNKQIODCQS3zh3rDiCHGxieV-3EiXey-zFgUPlrNQZdEI_l3jRKWVLxBhcirdV6FWa295GntfXDIVZGMWc_yiqQI1y3s8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3354c0af73.mp4?token=gBh8DThOUpR5snxwe2AR5m9VQVyS3oF83iD8ebxeoUPEaN3idQ3bXApWwIIq0tyE_FZ5gJfineeLvDU5X31QBRzlOXtVC6wrCtspkHckf2-2auwdSUGuzNLF4eJy_qTKodE_ijOtZ2to4dPlDrm5Ld44jdY5LIc00kmnqQOm6ju8-PAqRO4DEWtUmANs2NYMi7Ux5oe6AFcR5TaG0H-MVZaMBHv5RTt5ZZP40aE9aa_-VVPbSzdsyt-MCNKQIODCQS3zh3rDiCHGxieV-3EiXey-zFgUPlrNQZdEI_l3jRKWVLxBhcirdV6FWa295GntfXDIVZGMWc_yiqQI1y3s8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
حملات سنگین ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67788" target="_blank">📅 15:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67787">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a812a42d8.mp4?token=h5QLIDGsa71OM83aphC4a0LSM7G5eyqoeGWbZBWqorkePEsrlGd7XdUyXMTmdMl3e6QN7tNMJDj-AvNX18V-SPaI9juX__cTM6vIElMr1HozG1CMHpAUIV0Tu0SUHi8Wff9Sn0bh4JzawA_yNvQNS-gqR9bAwy4asVGD9OL7ajRXB-7w2Y3Xv7BS-shJsDpiBq0hjEhHtNTh14GkPr9dTeI8EytrM98JU5AZNeDQCsysn-GxXCaTZxtVWT7_PQAGFW0sYYCqbFJiqd7ruMo_kXzZluHngewVhTIQ0JzfAbPz-KuZGisj8UmPsZdF0HXPO30XeBiU_gSI5EgjugE_jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a812a42d8.mp4?token=h5QLIDGsa71OM83aphC4a0LSM7G5eyqoeGWbZBWqorkePEsrlGd7XdUyXMTmdMl3e6QN7tNMJDj-AvNX18V-SPaI9juX__cTM6vIElMr1HozG1CMHpAUIV0Tu0SUHi8Wff9Sn0bh4JzawA_yNvQNS-gqR9bAwy4asVGD9OL7ajRXB-7w2Y3Xv7BS-shJsDpiBq0hjEhHtNTh14GkPr9dTeI8EytrM98JU5AZNeDQCsysn-GxXCaTZxtVWT7_PQAGFW0sYYCqbFJiqd7ruMo_kXzZluHngewVhTIQ0JzfAbPz-KuZGisj8UmPsZdF0HXPO30XeBiU_gSI5EgjugE_jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری فاکس نیوز:
رئیس‌جمهور می‌گوید ایران دوباره به میز مذاکره بازگشته است. آیا شما واقعاً معتقدید که ایران با نیتی صادقانه و با حسن نیت به میز مذاکره برگشته است؟
🔴
هارلی هیپ‌من، تحلیلگر سیاست خارجی:
قطعاً نه. البته دوست دارم این‌طور باشد. هیچ‌کس خواهان جنگ نیست، اما ایران کنترل تنگه هرمز را رها نخواهد کرد. آنها به اهرم راهبردی‌ای دست یافته‌اند که به‌گمان خودشان، شاید حتی از یک بمب هسته‌ای نیز برایشان ارزشمندتر باشد. همچنین قرار نیست از تسلیحات هسته‌ای خود دست بکشند. بنابراین، آنها به دنبال حل‌وفصل مسالمت‌آمیز این مناقشه نیستند.
احتمالاً این وضعیت تا ماه‌های اکتبر و نوامبر به شکل اقدام و واکنش متقابل ادامه خواهد یافت و پس از آن، ترامپ میداند که در آن مقطع چه اقدامی باید انجام دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67787" target="_blank">📅 14:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67786">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🇮🇷
مجتبی خامنه‌ای:   آنها باید بدانند که این امر، متوقّف بر وجود شخص من یا سایر مسئولان نیست. ما باشیم یا نباشیم، این مطلب محقّق خواهد شد و بزودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این مأموریت الهی را انجام خواهند داد.   @News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67786" target="_blank">📅 14:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67785">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🇮🇷
بخشی از پیام مجتبی خامنه‌ای:   عهد می‌بندیم که انتقام خون پاک رهبر شهید و همه‌‌ی شهیدان این دو جنگ را از قاتلین جنایتکار و بی‌آبرو بگیریم.این جنایتکاران آرزوی مرگ آرام و در بستر را به گور خواهند برد  @News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67785" target="_blank">📅 14:14 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
