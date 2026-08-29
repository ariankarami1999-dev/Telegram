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
<img src="https://cdn1.telesco.pe/file/pjKR72E44-lPbqav8rGpFk7UPwQkhtax7_2BylLi9bAq9us5Mj0nXijbg5Z8eq1KOuQQaZ8x4JFp_AUPxaUvuKMNS3L0YTQjaDW79XRxBHi0YTIM0jW3vIorbNVPe205sbGcJdcM1wleEO2mm5CHnQLAla5yWg_poju7LZxtmzBvQMxFN2ITXad8Erzny_bnjd_ipFXRrp4MU9m6EuikhdgcGxithHmRerdNftv8i-FVMQBpmxhHP6sToGcOdcAuM_2X-HWEZRsSDYF7siw2se8oE0nAdbZZzP-LJLCIcYGbxev9UGetLDciZz6I3_Xd6ULgnTiNoeCvAknmGpx1PQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.4M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 14:44:54</div>
<hr>

<div class="tg-post" id="msg-78080">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nTtlrlwV04RF1T_yXXneXEWSTEneyDfLBz154MpW7IGfD7UaiLmvJ9AO6nniwrkuYkamtsM8vxSJSVFP6jVNCqxWRDRkzWx6HypNKVpJvjCL7MLwuoTuPOk134C1xpKyNffIPFDzAkovQ3uRLJyKUlef-g2_3uLP8ClG0_TYCXyeO55WXn9nZYuRgyFEoZe76iqmsRqkBlXIKLCjoMGqsrLweqt9lEAQGPr6IoYTheuULTd-MqUPSyOea-ljk3c5POrO5niCsi5EIxWl-bB69552_CUDiePJxn4DN_jzVSOLzLuBxCWc1O9xn6AKs-RJGgpr-kWRv5j9X8ICIuO06A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pnw_m2bNbKeKICQKYtBnhkO8Rdfea4gpbbuNCLSV4Fgfb24FLHEiQUMrpzccNGxT48d3YYmgboLqD1kkUVG01CFFZaK4x34IKIIvKomYrUYgm51-78NbCS8MET3MJhz5oKw466i6ng42rjKuALiqPyF-oMgckSpkvUfjbyTT89skTlNj_JKuusZNlliS1k76za3NqMctk1Fx_FchXMrEAQ_aGHjsUPYTntuADsd3IeTSopyd5Wp2O9ujBZVQuAr25WArO792d6SpmJcYH_y2IANpj7wxbARtgpDUykhkBaqg8KJkX-NMsj696WCdQZRvi_s1_o_JOidbnC9IMBp_uA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در تروت سوشال اعلام کرد آمریکا با ونزوئلا به توافقی دست یافته که آن را «بزرگ‌ترین توافق نفتی در تاریخ جهان» خواند.
ترامپ گفت بر اساس این توافق و با مشارکت بخش خصوصی، آمریکا کنترل اکثریت بیش از ۶۵ میلیارد بشکه از ذخایر اثبات‌شده نفت ونزوئلا را بدون تحمیل هزینه به مالیات‌دهندگان آمریکایی در اختیار خواهد گرفت.
او افزود مارکو روبیو، وزیر خارجه آمریکا، و پیت هگست، وزیر جنگ آمریکا، با همکاری دلسی رودریگز، رییس‌جمهوری موقت ونزوئلا، در دستیابی به این توافق نقش داشته‌اند.
ترامپ گفت این توافق ذخایر نفت آمریکا را بیش از دو برابر می‌کند، عرضه نفت را به میزان قابل‌توجهی افزایش می‌دهد و در بلندمدت به کاهش قیمت بنزین برای آمریکایی‌ها کمک خواهد کرد.
@
VahidOOnLine
مارکو روبیو، وزیر امور خارجه ایالات متحده، روز جمعه با اشاره به توافق نفتی جدید میان واشنگتن و کاراکاس اعلام کرد که این توافق علاوه بر تضمین ذخایر پایدار و کاهش بهای بنزین در آمریکا، نزدیک به ۱۰۰ میلیارد دلار سرمایه‌گذاری بخش خصوصی را به ونزوئلا سرازیر خواهد کرد.
روبیو در اکس نوشت: «برای مردم ونزوئلا، این توافق نزدیک به ۱۰۰ میلیارد دلار سرمایه‌گذاری بخش خصوصی به همراه خواهد داشت، از هزاران شغل با دستمزد بالا حمایت می‌کند، و پیشران بازسازی اقتصاد ونزوئلا خواهد بود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 205K · <a href="https://t.me/VahidOnline/78080" target="_blank">📅 04:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78079">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/034defbf1c.mp4?token=vejrRw6pKzCmUwniHXly-zhKVHLJvPlIZBnlY63295vGQWc_D9qPEMtYy5MOOPWUe4wB331SXFRCnKMH6uH4X3MEdrUp1YQyggsJ2vkZZxXk7P-RP7G0gknlphFnAhMrlrQBgK2zHY96on1-aDZp6t7d4Z7ajTSTg_4ucby7gYTQHLhHr5Vegt3kvq8-pVbXyQ62jVQKZIZUjKpx-426Pvlu6djWamixlFsqMQWvbtsSkbNedlz5i9lxh7ChxT9EUqyTbCzNeWYgAA_UrBMMDlepj58VxR6ywPVBNDWLHj0GauE645PTjC94T3akz7WOlvKmZKCVqafxAOTplE-kgg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/034defbf1c.mp4?token=vejrRw6pKzCmUwniHXly-zhKVHLJvPlIZBnlY63295vGQWc_D9qPEMtYy5MOOPWUe4wB331SXFRCnKMH6uH4X3MEdrUp1YQyggsJ2vkZZxXk7P-RP7G0gknlphFnAhMrlrQBgK2zHY96on1-aDZp6t7d4Z7ajTSTg_4ucby7gYTQHLhHr5Vegt3kvq8-pVbXyQ62jVQKZIZUjKpx-426Pvlu6djWamixlFsqMQWvbtsSkbNedlz5i9lxh7ChxT9EUqyTbCzNeWYgAA_UrBMMDlepj58VxR6ywPVBNDWLHj0GauE645PTjC94T3akz7WOlvKmZKCVqafxAOTplE-kgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: نرخ سوم بنزین حدود ۱۰ هزار تومان خواهد شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/78079" target="_blank">📅 22:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78078">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JdJyOupl3YyiI09Xn92UuMV3kJtX9eXMTpM_sP5uabwlTpQyhKgU6sPFL8E1KDY3XULjK-w1R7XZWBuRB1qKPmsye1bOu1nMrT4usW_nXrdBfHJf53ULvLFcKgoWWGtZx6ZdltTKZ7aJ1XIW2VYp4xJ-epJ5OqNLIZW80D_MMnZpaWQOl8LUchNQnrTF7IejlfjxypyeGY3Q25nIhpyt2l-FzcOUgIet2Jv6MsfR4cnl2KkTI6XmDuO7hCrN6SX64at7dXCx19_U_IEU-XX2-YlKDpUvS6YTT8cLsomaiRtUEo0weBE8eYEiBjrXl5Ace5qD4Ou5-jpAcyThbly9nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون اجرایی رئیس‌جمهور ایران تأیید کرد که دولت جمهوری اسلامی به‌دلیل محاصرهٔ دریایی آمریکا نمی‌تواند بنزین وارد کند.  به گزارش خبرگزاری ایرنا، محمدجعفر قائم‌پناه، شامگاه چهارشنبه چهارم شهریور، ایجاد تغییرات در قیمت حامل‌های انرژی شامل بنزین و گازوئیل را لازم…</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/78078" target="_blank">📅 21:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78077">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا:
وزارت خزانه‌داری وعده داده بود که هر شریان اقتصادیِ باقی‌مانده برای تهران را قطع کند و سرانجام به تهدید رژیم ایران پایان دهد.
همچنین هشدار دادیم که حامیان ایران نمی‌توانند همچنان از دسترسی به دلار آمریکا و نظام مالی جهانی برخوردار باشند.
بانک مصر امارات تصمیم گرفت این موضوع را به شیوه سخت بفهمد، و امروز نخستین گام را برای پاسخگو کردن آن به‌دلیل حمایت مستمر و فاحشش از رژیم ایران برمی‌داریم.
SecScottBessent
وزارت خزانه‌داری امریکا:
امروز، در چارچوب «عملیات طرد اقتصادی» (Operation Economic Outcast)،  شبکه اجرای جرایم مالی (FinCEN) قاعده‌ای را پیشنهاد کرد که دسترسی بانک مصر امارات به خدمات بانکداری کارگزاریِ مؤسسات مالی آمریکا را لغو می‌کند.
علاوه بر این، دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری (OFAC)، رضا محمد تأییدی، مدیر بانک ملی دبی، را به همراه یک شرکت پوششی مستقر در هنگ‌کنگ که به پول‌شویی وجوه برای یک صرافی تحریم‌شده ایرانی کمک کرده است، تحریم کرد.
«عملیات طرد اقتصادی» در حال قطع کردن آخرین شریان‌های مالی‌ای است که رژیم ایران را سرپا نگه می‌دارند.
USTreasury
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/78077" target="_blank">📅 18:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78075">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j4Y4ebKxB1DXysztWRZn70J3I-YeaFQEDXAap4scOyJJxviXLTeqEwxtTfDlPY2IcuwKI1--PhKMIKSfv3iEFRa7NvPBM9ikIIdMzmyMBdn9j5FF-85ml_IzI2zVplVJaqvQUtFOZaernc69u5bnWQwJQ9orKUYUxUI4yYLEeo-b54yOrgb37PNnRBpw2ndZnTqIV0zyudGUe9b0_u-M27gjJfLivd1n3oA4FqOpUnxXnSR4rUrK_1ldkrO8m_QmqmeEJSCx9a9qMR3Ix7tf-KKPJPIZ2y3WCK2uC6j5OI2Jxpv2APuDvAU1t4fm7JMHmcCx_Rw0wrrRCZmqQ0YESQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا نوری، امام جمعه بجنورد، در خطبه‌های نماز جمعه این شهر گفت: فشار اقتصادی کمر خود آمریکا را هم دارد می‌شکند و با فشارهای مردم در آمریکا بر علیه خود ترامپ، او که رای اول را در آمریکا داشت امروز محبوبیتش به زیر ۳۰ درصد رسیده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/78075" target="_blank">📅 16:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78074">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kt0w3mu0t04qBKkjD_SE9lkWUhJYLDzfAa_uRnje6R3EoKWLLpaIBjtIks8SoPs9aL96XekjD4IStjiALu51emYej3tUqCmd55m45ka9zPlzL7tugjUVpWlVYpdlY85DCh7hu_81VkzNnf9o2aQit17SdiCeWNNmZUbsHDh3Z1kcjmMxrH9JjML3aAZKz6Avz72Ot32_aeN8pQS702jW3Sg4s7_5uvrE2xmDjBFiG_HGFU70--HuQh9-X9dbCD_gupYGuV_RsHbTA9tp8flsgbigKLi9vSf1VMj5JB0XKs07903g6_RhCBcWW3MaN85_r6ZKpt8ZR1a4Gll2l58vYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه جمهوری اسلامی در واکنش به دور تازه فشارهای اقتصادی آمریکا، از کشورهای جهان خواست از اجرای تحریم‌های یک‌جانبه واشینگتن علیه ایران خودداری کنند.
این وزارتخانه روز جمعه، ششم شهریور، در بیانیه‌ای «عملیات طرد اقتصادی» آمریکا را «تروریسم دولتی» خواند و مدعی شد تحریم‌های جدید واشینگتن با منشور سازمان ملل و اصول حقوق بین‌الملل مغایرت دارد.
در این بیانیه، جمهوری اسلامی آمریکا را متهم کرده است که با استفاده از نقش دلار در نظام مالی بین‌المللی، کشورهای دیگر را برای قطع روابط اقتصادی با ایران تحت فشار قرار می‌دهد. وزارت خارجه جمهوری اسلامی این اقدام را نقض حاکمیت ملی کشورها و اصل برابری حاکمیتی دولت‌ها دانسته است.
وزارت خارجه جمهوری اسلامی همچنین به قطعنامه‌های مجمع عمومی سازمان ملل درباره منع مداخله در امور داخلی کشورها و اصول روابط دوستانه میان دولت‌ها استناد کرده و گفته است دولت‌ها نباید آثار تحریم‌های یک‌جانبه آمریکا را به رسمیت بشناسند یا در اجرای آنها مشارکت کنند.
در بخش دیگری از این بیانیه، تهران تحریم‌های تازه آمریکا را ادامه «جنگ اقتصادی» علیه جمهوری اسلامی دانسته و مدعی شده است این اقدامات با هدف تحمیل فشار و آسیب اقتصادی بر مردم ایران انجام می‌شود. وزارت خارجه جمهوری اسلامی همچنین از سازمان ملل و کشورهای عضو به دلیل آنچه «مماشات» در برابر اقدامات آمریکا و اسرائیل خوانده، انتقاد کرده است.
این موضع‌گیری پس از آن صورت گرفت که آمریکا در روز دوشنبه، دوم شهریور، از آغاز کارزار تازه‌ای با عنوان «عملیات طرد اقتصادی» علیه جمهوری اسلامی خبر داد. هدف اعلام‌شده این کارزار، تشدید فشار بر روابط اقتصادی ایران با دیگر کشورها از طریق تهدید به اعمال تحریم‌های ثانویه و محدودیت در دسترسی به نظام مالی آمریکا عنوان شده است.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، نیز در نامه‌ای به آنتونیو گوترش، دبیرکل سازمان ملل، از این سازمان و کشورهای عضو خواسته است در برابر اقدام تازه آمریکا واکنش نشان دهند و واشینگتن را مسئول پیامدهای تحریم‌های یک‌جانبه دانسته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/78074" target="_blank">📅 16:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78073">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/693aecab40.mp4?token=P_Q2ceE6H_j8UQwaE0tmYRdqBWFK_2S1ujdnVuVH0kC64Q2pwot67LqvWMBYhcltRiq1Vhlpu3-BRYHNuZcvgayznIWj6lVMoMtDXNlZrKuRDGUhmNjIR892k4zc3gBdHDgneIU6leYaBe4KubMMvfpgA6pyUSYPXbiHiaOlLWbTrawzExfxGQR35_s71oA4PbnLaAcl90eWmwoYclcZD5bKfl03D5ykxQILrOUvrhcnTzqx38teMTmPzrZnZRQCP4cHbAjK80e9_PtWw4eqxVeqqKrZenD8DMcRBmX2KDKFpwAccYXe4AaUumA0FrZK_eehRDV0_23FPSJtNdpS_g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/693aecab40.mp4?token=P_Q2ceE6H_j8UQwaE0tmYRdqBWFK_2S1ujdnVuVH0kC64Q2pwot67LqvWMBYhcltRiq1Vhlpu3-BRYHNuZcvgayznIWj6lVMoMtDXNlZrKuRDGUhmNjIR892k4zc3gBdHDgneIU6leYaBe4KubMMvfpgA6pyUSYPXbiHiaOlLWbTrawzExfxGQR35_s71oA4PbnLaAcl90eWmwoYclcZD5bKfl03D5ykxQILrOUvrhcnTzqx38teMTmPzrZnZRQCP4cHbAjK80e9_PtWw4eqxVeqqKrZenD8DMcRBmX2KDKFpwAccYXe4AaUumA0FrZK_eehRDV0_23FPSJtNdpS_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش ایالات متحده در ویدئویی که روز پنجشنبه پنجم شهریور منتشر شد اعلام کرد که نیروهای آمریکایی مین‌های دریایی را از تنگه هرمز پاکسازی کرده‌اند و مسیرهای بین‌المللی کشتیرانی باز هستند.
دریاسالار برد کوپر، فرمانده فرماندهی مرکزی ارتش ایالات متحده، سنتکام در یک پیام ویدئویی که در رسانه‌های اجتماعی منتشر شد، تاکید کرد که «امروز، خطوط کشتیرانی بین‌المللی باز هستند و تردد در حال افزایش است.»
کوپر با اشاره به پاکسازی مین‌ها در تنگه هرمز گفت: «شرایط، می‌توان گفت، چالش‌برانگیز و خطرناک بود. اما ما کار را انجام دادیم.»
پیشتر دونالد ترامپ، رئیس‌جمهور آمریکا، هم از پاکسازی تنگه هرمز از مین‌های کار گذاشته‌شده‌ ایران در تنگه هرمز خبر داده بود. سپاه پاسداران اما با رد این اظهارات بارها تأکید کرده که تنگه هرمز همچنان مسدود است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 203K · <a href="https://t.me/VahidOnline/78073" target="_blank">📅 16:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78071">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Jevo7JtumDD6Q9FSIml_u1HWQKQ_MhQwWF8APjnPft5cd3R6fQW_ITii6ClnyMMTiZOi9HisqVmAZ3HKuooRei_1r_-zz9quPPepgkW6lz2DpiEgSfugbLwVbv44ghmgw_FmwuIIMFg1BzyFZ2IN0fLRJNmGXN1NM9WHaZTnKqZpbyxXRLKr-d7ILJdvlS2T3B1to8EwmYiXHXq96JEUsZG0ZC7wiIH9tJP91N2zuo5UT3p3WE5gU1c2MkgWF_Th8xCaL34a5CY04c5xhtgSoJ2W11jYyMlZhgObxIynUCT6rJQljaHiQMXI14dZ4_QJtqoOCeOxXNABI1IwhPbPJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kUQGwONeLxZz35k56Ax_SCcfmIXnnG95C81o3rifNU88jwxbajhHBIUwHbZ90MR7EeXSN9VELQQbLPAWW1TEX1GW-ouYbo5_px1tNhnvE8iUIqXuTSemdzdvSJ5eodsHJ-Qcqx88p922zQJ8-WH9NApTsPE8ke1b_wDkrQlbLTPkqgyNbib3e8jnLd0xc3NT4IFzinsTjIU3K_geAv41RQ8CUvRhsl4Z2NK_R6o07KKcFHPta_YJ2QfB8UUX3oCbVeg685w8Ttwo20CflrLhYAULJaTKxvJ9-qQFiTmpFG7q1LP92qsEXnlBOQ4Yl2hfZHkJO0QzIXqM0wGbzA_YfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در گفت‌وگو با اکسیوس درباره تنگه هرمز تاکید کرد که این تنگه «باز است.»
او گفت: «پاسخ ایران بسیار ملایم است. آنها نمی‌خواهند ما دوباره به آنها حمله کنیم. تمام ماجرا همین است. بقیه چیزها اهمیتی ندارد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 195K · <a href="https://t.me/VahidOnline/78071" target="_blank">📅 16:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78069">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fYaVDE2573SSJgfJx7UDmuwcs01GPGmb8ZmVnoJ0aspThsfqwHRxylgkSobU18hMwPw3bZ3q0vHl9YnSFGYpPTzd69pv5PECLErwgbAIMqkPD__cECfDVcSKm9uAIoWPNY9KU7NAIu7-Rlp2lGOKlcVkF8TIqZy3o41VpKm7PcDiM8mdRR3SifnCrapl9IYHM-DgmAH8kNQdBnRrgk5eZF-9EPbLLo8Ay6Wy4yThYOygUXQPMWw8sGX9Qut1zRPhTykxoDfSAo0lMMFDl1TAO9CMBx1W4a4AXioCfFUzeVpZYKCXKse58uvM9voZejzeacdqWubIevIgVV1pH5PazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/neKRrMdkVUWLJNrdjetuvc0jPWBKQLKgP6ua7reZosogJQ0GRqETS7V-5SJB2EZV6QUCBWBLfHP7wv3498yqOShsHYgxb6rVhB5dz3ZfY9RIL9NLWXDNxUKuvtHX9JwqA8lFoGTGqdSMHl3tvi2wYcwgWGwvlqFFz7UkzzFPVTtdhYhvix1gfdFYI0iPXlGcUZZkoe_H_SqTwZtYBAQgcDZhzPPA4nDqKoTPWqUY1XP_3zsm9ScBBHVvOyY9KGdJhew4x2G9vf7_TrbRp3HKOnA72BUdQzIdJHzE7rpWyBAHETOrJ8_sCUplTL19Spe8slCgEhtD1Fd1cRa2_E81yg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">منابع آگاه به رسانه‌های آمریکا گفته‌اند جان رتکلیف، رئیس سازمان اطلاعات مرکزی آمریکا (سیا)، در جریان سفر محرمانه خود به مسکو از مقام‌های اطلاعاتی روسیه خواسته است اطلاعاتی را که می‌تواند به ایران کمک کند، در اختیار تهران قرار ندهند. همچنین گفته می‌شود موضوع حمایت روسیه از ایران از محورهای گفت‌وگوهای او با طرف روس بوده است.
این دیدار در جریان نخستین سفر برملا شده یک رئیس سیا به مسکو از سال ۲۰۲۱ به شمار می‌رود. کرملین تایید کرده است که آقای رتکلیف با مقام‌های اطلاعاتی روسیه دیدار کرده، اما با ولادیمیر پوتین، رئیس‌جمهور روسیه، ملاقات نداشته است.
بر اساس گزارش‌ها، جان رتکلیف علاوه بر موضوع ایران، درباره نگرانی‌های آمریکا نسبت به امنیت کشورهای عضو ناتو نیز با مقام‌های روس گفت‌وگو کرده است. با این حال، مقام‌های آمریکایی و روسی جزئیات رسمی درباره محتوای مذاکرات منتشر نکرده‌اند و سازمان سیا نیز از اظهار نظر درباره این سفر خودداری کرده است.
@
VahidHeadline
وزیر خارجه روسیه می‌گوید مسکو با دریافت عوارض از کشتی‌های عبوری از تنگهٔ هرمز موافق نیست؛ با این همه به گفته او، این موضوع به مذاکرات بیشتر نیاز دارد.
به گزارش خبرگزاری اینترفکس، سرگئی لاوروف در گفت‌وگویی با تلویزیون «آربی‌سی» با اشاره به باز بودن تنگهٔ هرمز تا قبل از آغاز حملات اسرائیل و آمریکا به ایران در ۹ اسفند پارسال، گفت: ایرانی‌ها «تنها برای این‌که تنگه هرمز امروز کاملاً باز باشد، در حال بحث در مورد عوارض عبور هستند. تا زمانی که ایالات متحده و اسرائیل آن قمار را آغاز نکردند، هیچ عوارضی وجود نداشت».
لاوروف تصریح کرد: «آمریکایی‌ها اکنون از ایران می‌خواهند تنگهٔ هرمز را باز کند و ایران می‌گوید که در ازای آن باید تحریم‌ها کاهش یا لغو شوند. و آن‌ها این کار را خواهند کرد».
رئیس‌جمهور آمریکا روز پنجشنبه گفت که دیگر نمی‌خواهد با مقام‌های جمهوری اسلامی مذاکره کند.
ترامپ افزود: روسیه رفتار مناسبی در تنگهٔ هرمز داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 194K · <a href="https://t.me/VahidOnline/78069" target="_blank">📅 16:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78068">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fBKb1eTUgDbx3ZuEGceCD97r9ydCxTm0SpM2ArqdpAkQPNVEcshRX-twG2QJGlBCuYzbMmkjMLTlGxlbF0IGsBjD1-a7UIRrwFqqFgfTVKYGTUC5wKfatTySD8zwnNtSuMIG8cLCSVnx9L9NqHDZJ-V8jwFt4f5hr8hExMigMVP_aqykKu2soxd7cyAKx-oST_1nUGVgLtRA7Aw4M-h5Wl6k70yMagoVC9Z3Xs5Ap2ePov1iPAlXkBSBpkgxcGbeCkAPYbpz_NudZwxDtlbrtdMtgtLo--Sk4mF9WNTweGJZXF09rYJrBmrx9DvBfYbe0cCRoNbVwin9y-0Nl6kR4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه جهان صنعت بر اساس آمار بانک مرکزی گزارش داد که تورم نقطه‌به‌نقطه در مرداد ۱۴۰۵ به ۸۴.۴ درصد رسید؛ رقمی که نسبت به ۸۳.۹ درصد در تیرماه افزایش نشان می‌دهد.
براساس این گزارش که صبح پنجشنبه ششم شهریورماه منتشر شده، تورم نقطه‌به‌نقطه در بخش کالا به ۱۲۱.۵ درصد رسیده و از افزایش چشمگیر قیمت اجناس طی یک سال گذشته حکایت دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/VahidOnline/78068" target="_blank">📅 16:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78067">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/67cc2d39e8.mp4?token=UE8HFqGEkqkqVQXn1yDZfD-7Z_MkzdYYPjD7D8z1RGBZ4BpwcGsA2f7W0BqzXoxvCc7jk3gQAn-p7LvAVv_fEfUa5XwHQRrHVe8T0SgRJdmiyrJh6MlnShUtktFJR-nEHUjB78LvidFMVnaGHEaefztDf0esK2IrqLIFTxMdyu4mOP5ov7jc6FhxHA_CQ98bksV609YBAiYWLEpVh61B71bX0yr3BfYwEbY0sGxDIJ04ssA3PF4vOo3dGJmmdNvqu0Ehn6myt57tvFdVhasVRq_dH4iZN5Oo4y74sEpkDU4Cn4FjIn24JUcGgYJDnzvDdbw4ZHpGd6zSabJSqP6-8A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/67cc2d39e8.mp4?token=UE8HFqGEkqkqVQXn1yDZfD-7Z_MkzdYYPjD7D8z1RGBZ4BpwcGsA2f7W0BqzXoxvCc7jk3gQAn-p7LvAVv_fEfUa5XwHQRrHVe8T0SgRJdmiyrJh6MlnShUtktFJR-nEHUjB78LvidFMVnaGHEaefztDf0esK2IrqLIFTxMdyu4mOP5ov7jc6FhxHA_CQ98bksV609YBAiYWLEpVh61B71bX0yr3BfYwEbY0sGxDIJ04ssA3PF4vOo3dGJmmdNvqu0Ehn6myt57tvFdVhasVRq_dH4iZN5Oo4y74sEpkDU4Cn4FjIn24JUcGgYJDnzvDdbw4ZHpGd6zSabJSqP6-8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک زن شاغل در حرفه قصابی با انتشار ویدیویی از وضعیت کساد بازار و تشدید فشار معیشتی مردم می‌گوید مشتریانی به مغازه‌اش می‌آیند و می‌گویند شش ماه یا حتی یک سال است گوشت نخورده‌اند.
مرکز آمار ایران در تازه‌ترین گزارش خود از ادامه جهش قیمت مواد غذایی در مردادماه خبر داده است.
در میان گروه‌های خوراکی شیر، پنیر و تخم‌مرغ و همچنین گوشت و فرآورده‌های آن، از جمله گروه‌هایی هستند که در ماه‌های اخیر افزایش قیمت بالایی را تجربه کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 197K · <a href="https://t.me/VahidOnline/78067" target="_blank">📅 16:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78066">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EQJzWW2ipmBQZ51C95uAJytUcC25i6BmK37_SPcAf0OeMD4Outhd4TYeSliDB-US19UzaMfzdiFf5UNQvpECzWWDaPMe7KmYxaULj_O7tVFQQPliAac1uk72fFv1Q-auSFvxov_HhNUF9d7ZMcRliiEoPYj3JiIKEqzsh9Ph2YsFkTGaq9qy98aOREpwVbAdX6sP9FGLS8IJhxZz13qAsTzwwxo6TX6mRPd9AZ7VFKsS5Ut4w6ZxpgrzVxke-EtxLUkEhcK-YPw0-mNvqA2A_5K_Z2y-EPjeXMWIsaDNt3wadxTWc4K4SZ0W96EVB_P9dwHrlpk5iM39rJCDnMYEAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌رضا زنگنه، جوان ۲۷ ساله اهل روستای کلیل‌آباد ملایر و ساکن کرج، با اتهام «محاربه» به اعدام محکوم شده است.
پرونده او اکنون برای رسیدگی به فرجام‌خواهی به دیوان عالی کشور ارسال شده و در صورت تأیید حکم، این زندانی با خطر اجرای اعدام روبه‌رو خواهد بود.
بر اساس اطلاعات رسیده، رضا زنگنه روز ۱۳ فروردین‌ماه از ملایر به کرج بازگشت و روز بعد، ۱۴ فروردین، هنگامی که مغازه خود را باز کرده بود، مأموران به محل کار او یورش بردند و او را بازداشت کردند. شماری از مغازه‌داران و کسبه اطراف شاهد بازداشت او بوده‌اند.
زنگنه تعمیرکار خودروهای لوکس و خارجی است و هم‌اکنون در زندان قزلحصار کرج نگهداری می‌شود. او از ابتدای پرونده وکیل تسخیری داشته، اما خانواده‌اش در جریان رسیدگی قضایی، وکیل انتخابی نیز برای پیگیری پرونده معرفی کرده‌اند.
@
Tavaana_TavaanaTech
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/78066" target="_blank">📅 16:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78065">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PfWAicfvKe4ye5trpiiY0vbH0ojp6PQXY41VCrmzqe6B6pKvHCa_BgvQRiXMjmcSpzbZAQ73koltuMXEx6s3eTWaicQc3SjLIv6i7QNoTwLchuh9bQQ3-lojCjXKZYkqW_aT35GOkMny2DWzDphiS_4mVMai0C_aBZ8LnKZccXTtcI-9EJ0hb0F5fSpQFcUBe3uUKG_WLn6BQXXRMwAJm-3BdO6Pz4GPO3xgLS_f8hKYhl7POztVdruKtPP1llNt4pbnDSYP-AhSAcmqz3dw83YUEFKHikh0OCkM_ri6TFUL62s3SYqfdsn9ZKqMExT8r4dWYavdxWAJHXHETV1FlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت دونالد ترامپ به میانجی‌ها اعلام کرده است که تمایلی به بازگشت به مفاد توافق اولیه ماه ژوئن با جمهوری اسلامی ندارد.
این موضع تلاش‌های تازه قطر، عمان و پاکستان برای احیای مذاکرات میان واشنگتن و تهران را با مانع روبرو کرده است.
روزنامه وال‌استریت ژورنال روز پنجشنبه پنجم شهریورماه به نقل از افراد مطلع گزارش داد که دولت ترامپ این موضع را بارها به میانجی‌ها منتقل کرده است.
توافق اولیه که با میانجی‌گری پاکستان شکل گرفت، بازگشایی تنگه هرمز و آغاز گفتگو درباره برنامه هسته‌ای جمهوری اسلامی و پایان جنگ را دنبال می‌کرد. در مقابل، کاهش تحریم‌ها و دسترسی تهران به دارایی‌های مسدودشده در نظر گرفته شده بود.
به نوشته وال‌استریت ژورنال، ترامپ اکنون فشار اقتصادی بر جمهوری اسلامی را در اولویت قرار داده و آماده است برای مشخص شدن نتیجه این سیاست صبر کند. آنا کلی، سخنگوی کاخ سفید، نیز گفت هیچ مذاکره‌ای با جمهوری اسلامی در جریان نیست یا برنامه‌ریزی نشده و محاصره دریایی و «عملیات طرد اقتصادی» ادامه خواهد یافت.
این گزارش در حالی منتشر شد که عاصم منیر، فرمانده ارتش پاکستان، اوایل هفته جاری برای گفتگو به تهران سفر کرد. وزیر خارجه عمان نیز برای دستیابی به تفاهمی درباره مسیر عبور کشتی‌ها از تنگه هرمز با مقام‌های جمهوری اسلامی گفتگو کرده است. نخست‌وزیر قطر نیز پنجشنبه پنجم شهریورماه در تهران با مقام‌های جمهوری اسلامی دیدار کرد.
وال‌استریت ژورنال نوشت اختلاف بر سر نحوه تفسیر توافق ژوئن و شرایط بازگشایی تنگه هرمز، دستیابی به چارچوبی برای ازسرگیری مذاکرات را دشوار کرده است. هم‌زمان، تهران بر اجرای مفاد توافق پیشین تاکید دارد، در حالی که واشنگتن مسیر فشار اقتصادی را دنبال می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78065" target="_blank">📅 23:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78064">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0c8bbd6d37.mp4?token=fzZ_MYdNs_7mJ-HdN9GWEyKPj1Gx4J7NJKX9fYh2NNeztokVcuiJk1qlrQMPE6oxqsflnAFwuzCXMFcb-7N_R0W1Ds_BPs5yjAcCs5ot_x0920jMtkAzXPowr3Vx1XrN6nYumtNT-ExXTv1omr9hpDNSEI1mY9WP5ng9bfsBDVASzISizaWW3gtVaazCSameFJwRkQxGEnU1PpTguPaCdOLy3ZBMbwszTty5W3_a4O7bd2fY2ALbaO6gcAm5UFPjbeJF6B0fZTX3fq1TRN_sW7EdFDINiwhUJmX_MmqSpIy9jPl3cNEWeHnGOnXAstP9dK-8MnMNhDcAEabyG1xEig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0c8bbd6d37.mp4?token=fzZ_MYdNs_7mJ-HdN9GWEyKPj1Gx4J7NJKX9fYh2NNeztokVcuiJk1qlrQMPE6oxqsflnAFwuzCXMFcb-7N_R0W1Ds_BPs5yjAcCs5ot_x0920jMtkAzXPowr3Vx1XrN6nYumtNT-ExXTv1omr9hpDNSEI1mY9WP5ng9bfsBDVASzISizaWW3gtVaazCSameFJwRkQxGEnU1PpTguPaCdOLy3ZBMbwszTty5W3_a4O7bd2fY2ALbaO6gcAm5UFPjbeJF6B0fZTX3fq1TRN_sW7EdFDINiwhUJmX_MmqSpIy9jPl3cNEWeHnGOnXAstP9dK-8MnMNhDcAEabyG1xEig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در کاخ سفید و پس از امضای فرمان اجرایی تغییر نام «دریاچه اونتاریو» به «دریاچه آمریکا»، به پرسش‌های خبرنگاران درباره نحوه اعمال تحریم‌های ثانویه علیه کشورهایی که با جمهوری اسلامی ایران روابط اقتصادی داشته باشند، پاسخ داد.
ترامپ در واکنش به پرسشی درباره عملکرد روسیه در منطقه و برخورد احتمالی آمریکا در صورت تداوم معاملات با ایران گفت: «تا اینجا رفتار روسیه در رابطه با تنگه هرمز بسیار خوب بوده است.» او با تاکید بر تقابل پایاپای واشنگتن با سایر قدرت‌ها افزود: «باید در نظر داشته باشید در برابر هر کاری که آن‌ها انجام می‌دهند، ما هم انجام می‌دهیم.»
رئیس‌جمهوری آمریکا همچنین در پاسخ به نگران‌کننده‌بودن اقدامات پکن گفت: «یک نفر درباره چین می‌گفت شنیده‌ایم آن‌ها دارند جاسوسی می‌کنند؛ ما هم از آن‌ها جاسوسی می‌کنیم. وضعیت همین‌طور پیش می‌رود.»
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز پنجشنبه پنجم شهریورماه، فرمان اجرایی جدیدی را امضا کرد که به موجب آن دستور داده شده نام «دریاچه اونتاریو» فورا به «دریاچه آمریکا» تغییر یابد.
ترامپ پیش از امضای این فرمان در دفتر بیضی کاخ سفید اعلام کرد: «ما نام دریاچه اونتاریو را تغییر می‌دهیم و این تصمیم از همین لحظه لازم‌الاجراست.» بر اساس اعلام یکی از مقامات کاخ سفید، این فرمان وزارت کشور آمریکا را موظف می‌سازد پایگاه داده‌های جغرافیایی ایالات متحده را برای بازتاب این نام جدید به‌روزرسانی کند.
این اقدام نمادین پس از شکست مذاکرات تجاری میان واشنگتن و اوتاوا، وضع تعرفه‌های تلافی‌جویانه و تیرگی شدید روابط میان دو کشور همسایه رخ می‌دهد.
با این حال، مقامات کانادایی پیش‌تر صراحتا اعلام کرده‌اند که این تصمیم یک‌جانبه واشنگتن را به رسمیت نخواهند شناخت و نام این دریاچه مرزی مشترک در خاک کانادا همچنان «دریاچه اونتاریو» باقی خواهد ماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/78064" target="_blank">📅 23:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78063">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X-e616tenIQeMkjkYBMdafdzPi4a-dd2sS4pLho90Prfl0bheJmsdyNd_3-0a8SJEE501VuSwp0xVPbY5_lO5MwGG4GclJiJU4wDETt--b2RSkDKz8_7RW9kCFDP37csc_LiWlDuhOy0LMUchl4DdT3WFu7c9LUmVKg4TMp9F7mVc6-sP8EaNFRU25UMfn0ISjlXcbEtbsRI5uqe3NhVmhabQgRn1JD4AtB4Yi0APPfceVSjzZ_3yy1aecPX5woW1UuuUjxBMGJFjAtTUifNcNBPVbkKMgrR9A6nRQAvQCYctDUguUqzI6wOH95NrWzyQihDsdb423SdoHd7N473Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان اطلاعات سپاه روز پنجشنبه ۵شهریور۱۴۰۵ با انتشار بیانیه‌ای نسبت به تشدید نارضایتی‌های اجتماعی هشدار داد.
در این بیانیه به ناکامی «دشمنان ایران» در «تلاش برای تغییر حکومت ایران از طریق حملات نظامی» اشاره شده و آمده است: «مخالفان جمهوری اسلامی در حال تغییر راهبرد خود هستند.»
این نهاد نظامی و امنیتی مدعی شد که فعال کردن بحران‌های داخلی، جنگ روانی، فشار اقتصادی و عملیات‌های امنیتی از محورهای این تغییر رویکرد است.
سازمان اطلاعات سپاه در این بیانیه نسبت به افزایش نارضایتی‌های اجتماعی و احتمال اعتراضات خیابانی هشدار داد و گفت مخالفان جمهوری اسلامی بر «برهم زدن ثبات و کاهش تاب‌آوری ملی» از طریق «نبرد شناختی و تولید ترس و ابهام» تمرکز کرده‌اند.
این نهاد همچنین از شناسایی آن‌چه «ساختار محرمانه و اختصاصی» موساد، سازمان اطلاعات اسراییل برای اعمال فشار از داخل ایران خواند، خبر داد و مدعی شد این ساختار از طریق ارتباط با گروه‌های مخالف، انجام عملیات خرابکارانه و به‌کارگیری عوامل محلی فعالیت می‌کند.
در این بیانیه ادعا شده که جمهوری اسلامی از وضعیت «صرفاً پاسخ‌گویی» به حملات خارج شده و در پی افزایش نقش خود در تعیین روند جنگ و دیپلماسی است.
در بخشی از بیانیه منتشر شده آمده است: «ایران دیگر صرفاً در موقعیت پاسخ به حملات طرف مقابل قرار ندارد» و به سوی «افزایش ابتکار عمل راهبردی و اثرگذاری بر زمان، مکان و هزینه جنگ و دیپلماسی» حرکت می‌کند.
سازمان اطلاعات سپاه همچنین ادعای حاکمیت ایران بر تنگه هرمز را تکرار کرد و نوشت توانایی‌های نظامی و «نامتقارن» جمهوری اسلامی حفظ شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/78063" target="_blank">📅 23:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78062">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jmce2-GoXk9Uq17KZswRVi_W70_ijdz3UbN4ytmgVF2dwHvW9IJRooQo9r7EtJYMBTjlUFNXW6G359oL2bSi7xsi3unrZLx8H06ykGziR8nAohtPyO58NgiVDheYf59buFtyYm0RqNWnO0XSco4TdKI5DpAlr-ooi7ePvPp8xB4DPqzUe1Y5VQb5BG-qywzjWuXjxT0610Hfv2-fMrq_iKMRLRZ1erRzxztSFhicnu_VmOPIsubxpcq2Uf7n-NgJt97piCxjkYdXTFvfHs9kVGX3gDDnzpKRlRonY2TkO0pUOUeYI7bbvbyFkeclT1SXB5sj3hpAFX5NE1WeYWRx_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون اجرایی رئیس‌جمهور ایران تأیید کرد که دولت جمهوری اسلامی به‌دلیل محاصرهٔ دریایی آمریکا نمی‌تواند بنزین وارد کند.
به گزارش خبرگزاری ایرنا، محمدجعفر قائم‌پناه، شامگاه چهارشنبه چهارم شهریور، ایجاد تغییرات در قیمت حامل‌های انرژی شامل بنزین و گازوئیل را لازم خواند، و در توضیح دلیل آن گفت: «توزیع بنزین عادلانه نیست و تداوم این مسیر غیرممکن است. ضمن این‌که تولید بنزین کفایت نمی‌کند و با محاصرهٔ دریایی آمریکا نمی‌توانیم بنزین وارد کنیم.»
این مقام دولت ایران در عین حال گفت مشخص نیست این تغییرات به چه میزان و چه زمانی انجام می‌شود.
در روزهای اخیر، هم‌زمان با افزایش اظهارنظرهای مقام‌های جمهوری اسلامی دربارهٔ لزوم افزایش قیمت بنزین، گزارش‌های مختلفی از تعطیلی برخی جایگاه‌های عرضهٔ سوخت در تهران و تشکیل صف‌های طولانی مقابل آن‌ها منتشر شده است.
بر اساس آخرین آمار اعلام‌شده، تولید روزانهٔ بنزین در کشور حدود ۱۱۵ میلیون لیتر و مصرف آن حدود ۱۲۹ میلیون لیتر است. به این ترتیب، میزان تولید روزانه روزانه حدود ۱۴ میلیون لیتر کمتر از میزان مصرف است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/78062" target="_blank">📅 19:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78060">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GsKBKVV8sXs-MvMmWqmhPB-sREfsetNzG9tSy7ng7WlMG0M7tpUs4SXvmplRY2zRCF8NXn4ZALAIZoNbs8bkWbBVtTTQaZyj8LZaFE7gQ98mkEW8DwG0EIGRiVDN9lTmRjTYtcDotRNF0UZx_gFNfPo6JZFKFcRi78cvRHTYchU8E21JvLUXoalDMdM7A58UOO1wCdIoubEEDw4984FH2KoZdLkj2AdAWjSzEiK8tdnrL8FsXkDLiDtjiXadg1nFxp0hNICHXENzwlDjPzwfEdN8gZSx2On1rwM1-3KMwGp8IGCJbxshAYk4QNnWunj-x4fuxFhSD9icW2SxaNqhpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HJvjzWU6kk_b_RUTW3imtM-IIdPr1jVE26Ydoc7pkDuXjbyHC1bVm60FLSt5HKAl7fjSq784vpbKDTa026S3QZVlKtl4PzCyueV0WMSpkTpskF0E7TjNKKNtVngOX26J8E9pd3uAA2_gUURG3rkqCOKSsy2eNOPmfgq4ZTM-S6zLnKs1KjYReTPSdXDCPV8X6dkxsHpjMJ5j6WI7dReVBqkZ80GJJ2uLnNu4Y3q2itf-zJy_9yMDJxp8UXf-geWWG2-Yog3EFC0OoPkyMw-B9WJqoHWRoq_tvcjqpXDNuW9N3ZphP5Ra7c5uW7MTUKzqGxxPoWHTXrSDGcvl-Ur9Gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر خارجه قطر، در سفر به تهران با مسعود پزشکیان دیدار کرد.
وزیر خارجه قطر در این سفر با محمدباقر قالیباف، رییس مجلس شورای اسلامی نیز دیدار کرده و درباره راه‌حل برای از سرگیری مذاکرات میان واشینگتن و تهران گفت‌وگو کرده بود.
@
VahidOOnLine
وزیر خارجه قطر همچنین به قالیباف گفته است که گفت‌وگو بهترین راه برای حل اختلافات و جلوگیری از تشدید بیشتر تنش‌ها در منطقه است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/78060" target="_blank">📅 19:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78059">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qv-Cxwm7cWpUdnAcU2ffaED0M6mdJT079x-vu42s0jCh4N3ze_wesS72Oqz67jHevtecwHEEtlLAVmPbF8MUKzE4H6mPX-FGatpaj8wI5CmGCoIXlY-FBmNR0RnM1UTYCBE0Y-bvsVtJxtpUQ6lSfBhWQQtEdmQeTOquXzCG6HH60VE_eXTRldGa09W0oDeaiB1ZyZOnVqRD-YfUBSx4QG3rHd8ORL9pjlswLTdBnq4zP6TxmHhpH3UK0DxbaMmbZSlaEufZF-Ml0K-harP_oMt2VHb5kD-68WtEmr8eSPGyByFoWf8tSPCAe3rsZ8Ot4D87nS-Loa5ZC4O15WhQPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسیه رمضانی، زن ۳۹ ساله و مادر دو فرزند، در جریان سرکوب اعتراضات دی‌ماه ۱۴۰۴ در تهران با شلیک مستقیم نیروهای جمهوری اسلامی کشته شد.
ماموران بامداد جمعه ۱۹ دی ۱۴۰۴، از فاصله‌ای نزدیک و از پشت به رمضانی شلیک کردند. گلوله پس از عبور از پشت و قفسه سینه، به قلب او رسید و جانش را گرفت.
آسیه رمضانی مادر یک دختر نوجوان و یک پسر دبستانی بود.
خانواده‌اش می‌گویند پس از تیراندازی، او را به یک درمانگاه منتقل کردند؛ اما بدون رسیدگی پزشکی موثر، برای حدود پنج ساعت در حال خون‌ریزی رها شد.
خانواده رمضانی پس از بی‌خبر ماندن از سرنوشت او، سه روز میان پزشکی قانونی کهریزک و بهشت زهرا در جست‌وجویش بودند تا سرانجام پیکرش را پیدا کردند.
خانواده، زمانی که پیکر رمضانی را یافتند، گونه‌اش کبود بود و از زیر کاوری که پیکر را در آن قرار داده بودند، همچنان خون دیده می‌شد. آن‌ها گفته‌اند پیکر او در شرایطی «ناشایست و دردناک» نگهداری شده بود.
خانواده رمضانی همچنین می‌گویند لباس‌ها، کفش‌ها و دیگر وسایل شخصی او برداشته شده و به آن‌ها تحویل داده نشده است.
آن‌ها پس از تحویل پیکر متوجه شدند قلب رمضانی که با گلوله شکافته شده بود، بدون اطلاعشان بخیه زده شده است. خانواده آسیه رمضانی در روایت خود نوشته‌اند: «ما آن سه روز را فراموش نمی‌کنیم. آن پنج ساعت، آن خون، آن کاور، آن قلب شکافته‌شده و وسایلی را که باید به خانواده‌اش بازگردانده می‌شدند، فراموش نمی‌کنیم.»
آن‌ها تاکید کرده‌اند که همه واقعیت‌های مربوط به کشته‌شدن او هنوز روشن نشده است و افزوده‌اند: «هزار سال هم که بگذرد، خون عزیزانمان پاک نمی‌شود. نامشان را تکرار می‌کنیم، روایتشان‌ را زنده نگه می‌داریم و دادخواه می‌مانیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/78059" target="_blank">📅 17:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78058">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o207ZtayzRot4M7-s8fkB9GK8N0pRotvGqfVoyKOSyGj1q8xwjfPU1U7KYp2y2SZRZ2hao2b__-X0884JKkK3cAPdr_jnm9Uq_pBWM6nmJnhq_1NktJsiMBAGgmvEiKH-ncVTLSH7dKRT2WW-RQN1AdpLEebdTHRLnevBSm2ggxwQGElOtsrbJ-PMEztYzVIah3wlWsp96IgTM3Xuwa2-HZcDRDXJMScYxwVYRtLn0cG3G97m7w35bzqYQUccLOSN2kQACxEFwdrg5BHo1NK6SzPRXp6thxUN9GpxsxuhPhzrNMbaciv6NB8VYW3FAQib3UFvWJWgX7TNJX2eAtenQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، با انتشار پیامی در شبکه اجتماعی ایکس، با انتقاد از سیاست‌های مالی جمهوری اسلامی، خواستار اختصاص منابع مالی کشور به مردم ایران شد.
بسنت در پیام خود نوشت: «در حالی که مردم ایران برای تامین نیازهای اولیه خود با مشکلات معیشتی دست‌وپنجه نرم می‌کنند، حکومت فاسد همچنان مبالغ هنگفتی را در خارج از کشور هدر می‌دهد.»
وزیر خزانه‌داری آمریکا در ادامه افزود: «حکومت ایران به جای تزریق میلیاردها دلار به گروه‌های نیابتی تروریستی خود، باید این پول را صرف مردم کشورش کند.»
این اظهارات هم‌زمان با تشدید کارزار تحریم‌های مالی ایالات متحده برای محدود کردن دسترسی حکومت ایران به منابع ارز خارجی مطرح می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/78058" target="_blank">📅 17:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78057">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UwcQ0xXtylfjevPvbwGj1-bygCf1TjTK4WmuSBXe3mqEqEGqrae8RO3dkYxHEQStmj4LV-eLDx3dMW0CsPqqCv1uFLRN4-wv_0XDXt9z-8Rq6MdJXbM4_haw6zP-z5v7IUViw2fAMMMdM0VKw9qEqH34a6hRIn77dWajuU0XpeJZ0LkssdifbQUYEpVgXwv9LaX-P7dWmHeW5K-gYmsbCNKq1w8LHaNC5hoHy7S5Fy3nlCcZj_o8uS7kJ6EMFk6I7qY2H6rvBnMKtoi-llayLPcxm_MG9dmkn9qRKrRNH6dNzaABkWnmSSu-sPx8z6W9IuP7wA1qUJ0042OSjnCB4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت شاخص برنت در پی بهبود وضعیت تردد کشتی‌ها از تنگه هرمز و انتظارها درباره مذاکرات مثبت میان ایران و قطر روند نزولی خود را ادامه داد و روز پنج‌شنبه به ۸۶ دلار و ۷۵ سنت رسید.
قیمت نفت طی روز جاری نسب به روز چهارشنبه بیش از یک دلار و نسبت به هفته گذشته حدود هشت دلار افت کرده است.
در پی سفر وزیر خارجه عمان و فرمانده ارتش پاکستان به تهران طی روزهای گذشته، اسماعیل بقائی، سخنگوی وزارت امور خارجه ایران، روز چهارشنبه اعلام کرد نخست‌وزیر قطر نیز قرار است به زودی به تهران سفر کند.
هم‌زمان وزیر خارجه قطر در تماس با همتای ایرانی خود بر حمایت دوحه از تمام تلاش‌های دیپلماتیک و اقداماتی تاکید کرد که هدف آن دستیابی به راه‌حلی برای تضمین آزادی کشتیرانی و فراهم کردن زمینه توافقی جامع برای برقراری صلح پایدار در منطقه باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/78057" target="_blank">📅 17:24 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78056">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JF9PJzrJN4mEBLAfwBAe23fzTZZetuoolMxjttCdofkOVpOiA3m1H9VLxN5XaoblYh4CdEfe0p3OrEJ0SHOVZAw3ZGqRYHGV5VyoShdL2atw0QZN_iT6Qyl3ruPtCc4dlBSatKHh7L2_QtaVk3wOK4xagkpn3MF_X2GKGoE_O4kaNTTFWJh04paSldTh0C2KqgBc0kQ5jjZpo8dlENylJblZdVbqKMuslWZAh5mz9ac9grbl7MaKgDBef42iK_bbMzSa9DdgGGE1yHvEw91SOzgZiXQGQ63AdRn-2PU2fTVqFC_zdHyROnNXmdfJO_rqOi9TLK0HGkGnRa8sP3pC5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه مدنی، پژوهشگر و متخصص ایرانی حوزه آب و مدیر مؤسسه «آب، محیط‌زیست و سلامت» دانشگاه سازمان ملل در کانادا روز چهارشنبه چهارم شهریور جایزه آب استکهلم ۲۰۲۶، معروف به «نوبل آب»، را از کارل گوستاف شانزدهم، پادشاه سوئد، دریافت کرد.
این جایزه در مراسم رسمی هفته جهانی آب در استکهلم به پاس پژوهش‌ها و فعالیت‌های کاوه مدنی در زمینه مدیریت منابع آب، حکمرانی آب و ارائه دیدگاه‌های نوین برای مواجهه با بحران آب به او اهدا شده است.
کاوه مدنی پیش‌تر در ماه مارس به‌عنوان برنده این جایزه معرفی شده بود و کمیته جایزه، از پژوهش‌های او در مدیریت منابع آب و پیوند دادن علم با سیاست‌گذاری، دیپلماسی و ارتباطات عمومی تقدیر کرده بود.
جایزه آب استکهلم از سال ۱۹۹۱ به صورت سالانه اعطا می‌شود و مراسم آن را بنیاد آب استکهلم با همکاری آکادمی سلطنتی علوم سوئد برگزار می‌کند.
این جایزه که شامل یک میلیون کرون سوئد و یک تندیس کریستالی است به افراد یا سازمان‌هایی اهدا می‌شود که دستاوردهای برجسته‌ای در حفاظت، مدیریت و استفاده پایدار از منابع آب داشته باشند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 220K · <a href="https://t.me/VahidOnline/78056" target="_blank">📅 17:24 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78055">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kk0fMvDnKQnmFDEO8D3zShIRo-LRaUnKDN-hHXOk4BtdLNb6t3IYMxjd0zcT3RfTebwgxlZsvas8ksfz-2afntFVUJk7P8aGAXpKRQk5FySO03N1lFls-KCYc2MHKxkouscteu8HKMj4PZDddNDq2H4nxzxZk8_WVEvvaGUjDAKmEl1P43pSAJkCNFCoYQLb14Vlh3cGNv-ciZkG_-MlNUiPTfbWxaESpk4VjxUE-hCJ9h2tOa1jA5g2uO0BhnDF6m1ApP1FFMOSbBlJsX4mn7AcAOlNk4x9CtAvyVcq_ygMsCm3ctC61yDCMTBw3DOK3yrowdTT4Mz6P5OulKC50g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیلا ابوالحسنی، از بازداشت‌شدگان اعتراضات دی۱۴۰۴، به اتهام «محاربه» به اعدام محکوم شده و پرونده او پس از اعتراض به حکم، اکنون در دیوان عالی کشور در حال بررسی است.
لیلا ابوالحسنی، حدودا ۴۳ ساله و مادر دو نوجوان، از ۱۸دی۱۴۰۴ در زندان دولت‌آباد اصفهان نگهداری می‌شود.
یک منبع گفته است که ابوالحسنی روز ۱۸دی در شاهین‌شهر و هنگامی بازداشت شد که در حال عکس گرفتن از آتش‌سوزی یکی از فروشگاه‌های «افق کوروش» بود.
به گفته این منبع، دستگاه قضایی او را به دست داشتن در آتش‌زدن این فروشگاه متهم کرده است؛ اتهامی که به صدور حکم اعدام علیه او منجر شده است.
در حال حاضر، دیوان عالی درباره اعتراض او به حکم اعدام در حال بررسی پرونده است.
لیلا ابوالحسنی از زمان بازداشت تاکنون، بیش از هفت ماه را در زندان دولت‌آباد اصفهان سپری کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/78055" target="_blank">📅 17:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78054">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S5OiekCAAP_xI6obyWYGvuBRnT_2vlKpVeILu7WVlAxMKBHhaUn07YLv17kUciX15vyS1YIJ-vIW_V0ofywIstXjt63aJ4p5iIgZIH_ecVjyCjtNVikRWGDWyYY4AxsiktQ3orTkaAYSswKabO4SXqMJxhqG7ul7TCC--DWmsfSS6AXme3nEFlQyXP2x7xQO6WSET-JIEvbvR9qkdaIs6HTKkw7FSi1ZRq3LjgoTwh0U5CiuNJ9Wjx7e962ZCkKDa8yPTf93iL_KiRrYd4nj2dDgdKBkRDQ-DXEwbYpwBegDAHaYquWJQT2wRHQ5bXnyBaeF4A61DDa-FtG5uRnAmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
مقامات محلی گزارش داده‌اند که یک نفتکش با پرتابه‌ای ناشناس هدف قرار گرفته و در پی آن کشتی دچار آتش‌سوزی شده است؛ آتش‌سوزی از آن زمان مهار شده است.
گزارش شده که همه اعضای خدمه سالم هستند و حضور همه آن‌ها تأیید شده و هیچ گزارشی از پیامدهای زیست‌محیطی دریافت نشده است.
مقامات در حال تحقیق درباره این حادثه هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/78054" target="_blank">📅 05:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78053">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b0498b32fb.mp4?token=RxVx55LfouzJvL0ejUlq_-1-DtImYZcwQKpvFvuov0my7W82XmKV8UxVVf9vlLEeERWw9YYAeKOXxOlXBIFeUwjGErIFiB7ZCyAwbHvDiCeuggqRQJFke605PjsQuoN8w1qmUK33ht03S5LYMP3D03wCUJj8nsQ8NVhfn2CEj4bmSRLQ43Zg6iKhoOQ-pSKx6T6fNizAOGOL125WTYVbuPI0cuAgifMZ9sRRTXcfcvPhFTTc5C0rvDYKXt_8cct0boUD3cVkYQ5eE98noBGtgwV43oQq5NpNZG4NDBnMHGHL9CIkNE51ltktGTTui_hvbhQCADI7HDXd1t6F6r97PA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b0498b32fb.mp4?token=RxVx55LfouzJvL0ejUlq_-1-DtImYZcwQKpvFvuov0my7W82XmKV8UxVVf9vlLEeERWw9YYAeKOXxOlXBIFeUwjGErIFiB7ZCyAwbHvDiCeuggqRQJFke605PjsQuoN8w1qmUK33ht03S5LYMP3D03wCUJj8nsQ8NVhfn2CEj4bmSRLQ43Zg6iKhoOQ-pSKx6T6fNizAOGOL125WTYVbuPI0cuAgifMZ9sRRTXcfcvPhFTTc5C0rvDYKXt_8cct0boUD3cVkYQ5eE98noBGtgwV43oQq5NpNZG4NDBnMHGHL9CIkNE51ltktGTTui_hvbhQCADI7HDXd1t6F6r97PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی نیروهای مسلح: رسانه‌های فارسی‌زبان در بانک اهداف نظامی ما جای می‌گیرند
1:11
سخنگوی ارشد نیروهای مسلح جمهوری اسلامی،  در مصاحبهٔ تلویزیونی با خبرگزاری «دفاع مقدس» مدعی شد رسانه‌های فارسی‌زبان خارج از کشور مستقیماً به «موساد»، «سی‌آی‌ای» و «سازمان‌های اطلاعاتی دشمن متصل هستند».
به گفته ابوالفضل شکارچی  «نیرو‌های مسلح جمهوری اسلامی به این بنگاه‌های خبرپراکنی به‌عنوان رسانه نگاه نمی‌کنند» و کسانی که در این رسانه‌ها کار می‌کنند را به عنوان «سربازان صهیونیست و آمریکا می‌بینیم و حتی می‌شود آن‌ها را در بانک اهداف نظامی خود پیش‌بینی کنیم».
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/78053" target="_blank">📅 22:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78051">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bYuLl3fp7tQfrGbujKSwmux8qNTFO1E96s5tM1gVEZgjqqNHvqNWa4PE2FQLN5yDGbtvGIVdsTn4O1MZhPe9PPmNk7C2TjpJBwT1grB0-NJM6Vj8UU39rafO0fLVPp0c5PL0NDZR67eBN_mddmtCra_x3Yog6hFxq3zI1g8nrLty41aupyF3B4rekK45sgrnm388IingqY4mtK9E_0vBvPfhQSRgKVTBCLyKZz1SH1L_yRdBzxUABEdZ_3JX7yvHvfnA8A6ICTfw1IWV4C3Onohl1bZykRE5I0Yw1P2_cIVOJipfntDkds_t_lwWVt8g372mPA-lyQV8NTqtFx5zJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JSsGXCxFd0UTINww0AIfe6GsPeZ1Fty3BVs2OYoED7_zNNp0_s3dP_YZHjwyMm1JgeAnc-QVZ75_9mlDsEcFI5JykmoSiNjbtvDWbzjaQcVO92h-aLSA4XJzRCBFK3-aRdPWi76BMXR8-Mg3sOEgEkHYhQwEe50on2hxxeiKrX6KtV4J8qe7zNAZxKJ9AttpfoEhE3OWSr8tTHRG3rv2N_U9vriQM-9gbkJ7NpqCsXcBq_Qs3FDC_5F_r1_XkvgI-wEJewpAI8RD_tK8RLpN5AHqs7m0bqIcBIJFBHVGKYLaiEds_QEvpiM3OJJGN9lkb4VfEod58EEByadjfwJEoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ درباره اعتراضات در ایران اعلام کرد «فکر نمی‌کنم وقتی یک مسلسل روبه‌روی شما باشد، آنجا بایستید؛ تک‌تیراندازهایی واقعا بالای ساختمان‌ها هستند.»
او گفت: «مردم هنگام اعتراض هدف گلوله قرار می‌گیرند و جمهوری اسلامی برای ایجاد ترس در میان جمعیت، لزوما نیاز ندارد تعداد زیادی را هدف قرار دهد.»
او افزود: «وقتی می‌بینید پنج، شش یا ۱۰ نفر در میان جمعیت ۱۰۰ هزار یا ۲۰۰ هزار نفری به زمین می‌افتند، مردم محل را ترک می‌کنند. فرقی نمی‌کند چه کسی باشید، می‌روید. وقتی افرادی آماده‌اند به شما شلیک کنند و شما را بکشند، اعتراض کردن بسیار دشوار است. به همین دلیل است که آنها اعتراض نمی‌کنند.»
ترامپ گفت: «نیروی دریایی‌شان همان‌طور که می‌دانید، کاملا از بین رفته است. نیروی هوایی‌شان کاملا از بین رفته است. بسیاری از سربازانشان حقوق دریافت نمی‌کنند. فکر می‌کنم تورمشان ۳۹۰ درصد است و پولشان تقریبا بی‌ارزش شده است؛ منظورم این است که وضعیت خوبی ندارند.»
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز چهارشنبه چهارم شهریورماه، در مصاحبه رادیویی با گلن بک اعلام کرد که وضعیت حمل و نقل انرژی در تنگه هرمز به حالت عملیاتی بازگشته و حجم بالایی از نفت از این آبراه در حال عبور است.
ترامپ با اشاره به اقدامات انجام‌شده برای پاک‌سازی مسیر گفت: «ما از شر مین‌ها خلاص شدیم و این تنگه اکنون فعال و در حال کار است.»
او با اذعان به وجود برخی تهدیدهای پراکنده افزود: «بله، هر از گاهی پهپاد، راکت یا چیزی شلیک می‌شود، اما تنگه کاملا فعال است و نفت زیادی از آن خارج می‌شود؛ به‌طوری که همین دیروز ۱۰ میلیون بشکه نفت از این آبراه عبور کرد.»
@
VahidOOnLine
دونالد ترامپ، رییس‌جمهوری آمریکا، چهارشنبه چهارم شهریور در مصاحبه با برنامه رادیویی گلن بک گفت فکر نمی‌کند مجتبی خامنه‌ای، رهبر جمهوری اسلامی، کشته شده باشد.
رییس‌جمهوری آمریکا اعلام کرد: «او به‌شدت مجروح شده بود؛ سمت چپ بدنش، دستش، پایش، همه این قسمت‌ها به‌شدت آسیب دیده بود.»
ترامپ همچنین افزود حتی اگر مجتبی خامنه‌ای مرده باشد، جمهوری اسلامی «نمایش خوبی» اجرا می‌کند.
ترامپ گفت: «جمهوری اسلامی همچنان درباره مراجعه به رهبرشان برای گرفتن تایید نهایی در امور مختلف صحبت می‌کند.»
رییس‌جمهوری آمریکا همچنین افزود توافق با جمهوری اسلامی آسان نیست و آن‌ها «چندان پایبند به اصول» نیستند.
@
VahidOOnLine
دونالد ترامپ روز چهارشنبه چهارم شهریورماه، در گفتگو با شبکه الجزیره اعلام کرد که هم اقدامات اقتصادی و هم گزینه‌های نظامی «اثربخش» هستند و او در رابطه با مذاکرات با ایران «عجله‌ای ندارد».
او در پاسخ به پرسش‌های تانیا نوری، خبرنگار این شبکه، افزود: «من هیچ جدول زمانی ندارم؛ هیچ عجله‌ای در کار نیست.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78051" target="_blank">📅 17:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78050">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V6FlKQ8G-fcLwmc05xZ6dUjrBMLFqF-FMGR_wAh09hUYbAtVju_3ZkZWxJx82QAq8KbB8v1CL4tfx0EliRcQxc2VJQsUwwDhGVZrnR-pF3NxojiHiv_dlIYR-9q5mC6OIG9o5I6h_nSnHTfYiJsWn263gEPsTEa-PZj3hxNQGCnfnWYvI5wIcQTt336rLVzPtpmGDYdmf3iKbUzb-fPfqqn5X6sVgtNBaZtGx2L7Q5NX4yEtmMkqzrUtM2KdSK9SjOit0miuFyyqXYuhivH-0btcsJVvl6NSmgak1KdIp_L8o00qw6uNYzj0juUzbfnyC3vO7DbmkMJWd58GcrXpaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، بار دیگر موضع قبلی خود دربارهٔ ضرورت پایان دادن به جنگ با آمریکا را تکرار کرد و گفت: «جنگ همیشه راه‌حل نیست. گرهی را که می‌توان با دست باز کرد، نباید با دندان باز کرد.»
پزشکیان روز چهارشنبه چهارم شهریور در یک مراسم عمومی بار دیگر ایران را «پیروز میدان» خواند و در عین حال افزود می‌توان با «تدبیر و اندیشه» از این مسیر عبور کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/78050" target="_blank">📅 17:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78049">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/npV8hLHrGEV4kBO2XyrTLuODui54JldTD0Nn-Fq9ZosUuCFWZ2gpxrXWanaC37s2abMNGAFuZyI_uPsg6jUSvPo7TOROkrL6QGh6ObpSfZh1xlx11toL6tSY44J9Edq99lDD2iqUSgYca28tiaRbb5eQqztL-2w3XDzNMeeEFuV9nAbfAfif-nbYLJCwx9shCCYVk6ahW_gFavvxwsb32rAQu32xEJ3unNpSKiMyf3HurPM9NDQ605l5auMdhy9fPhAeNJe1LGcU08yunR60gMCoYllICCJWImZfBdjX44bBpORQnA8ypfkG4jUG6Z77Ny8vMhWCU03Dr0zTZeUKuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری هرانا گزارش داده است که حسین نظری، شهروند ۲۵ ساله و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، توسط شعبه اول دادگاه انقلاب مشهد به اعدام محکوم شده است.
بر پایه این گزارش، دستگاه قضایی جمهوری اسلامی آقای نظری را با اتهام‌هایی همچون «ارتباط با دول و گروه‌های متخاصم» و «اجتماع و تبانی برای ارتکاب جرم علیه امنیت کشور» محاکمه و حکم اعدام او در تیرماه سال جاری صادر شده است.
نظری، متولد ۱۳۸۰، در جریان اعتراضات دی‌ماه توسط نیروهای امنیتی بازداشت و پس از طی مراحل بازجویی و قضایی به زندان وکیل‌آباد مشهد منتقل شد. او همچنان در این زندان نگهداری می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/78049" target="_blank">📅 17:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78048">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BI1B2NhlKjCypbRLPafA7MV3S_kB5QC_tnbwkiqvTxlO-0CeOeWGOL-FDoeXlswY_JhPmNgSr41Z8zyGIQmR7AT47oBTR93jP3dnt-ja-HGDu2su62_bLAE7USdcA_HPEuGFePmMD6hH3yk2aJXsr5ACUob_KANdDPN_ljSzKSZivRxxqQ0n1EO471GEmToAoJSTrJxa8ZisscEmVBbAJNuHSNHWrtiye39rfW5-tJHDi5x5JxB0XlfouAUMmfEvh7whiW9QpqYKzHW50X-1CqVUFdrXp5SlqmYvP-b_z6S5e9zdxse_AgdpgXB_NxWX-S4KK3poYOvIPYFLqJtk4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش وب‌سایت‌های اعلام نرخ ارز و طلا در ایران نشان می‌‌دهد که قیمت دلار آمریکا روز چهارشنبه چهارم شهریور کاهش یافت و به زیر ۲۰۰ هزار تومان بازگشت.
در لحظه انتشار این خبر، قیمت دلار ۱۹۸ هزار و ۵۰۰ تومان و قیمت سکه طلای موسوم به «امامی» هم ۲۱۰ میلیون تومان گزارش شد.
این اتفاق پس از چند روز افزایش قابل توجه قیمت ارزهای خارجی و طلا در ایران رخ می‌دهد. قیمت دلار آمریکا در این روزها تا ۲۰۵ هزار تومان افزایش یافته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/78048" target="_blank">📅 17:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78047">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/66d56a19f2.mp4?token=axPtURPPevTQ6awhz3ogeNZDk3Z3fdA6on1Vkdih2c_0jbw8NrCkRuaCEU1ilzrUXUT6tUO2xUYnFsyefmdlo1E1lEbWHZM4hDu_3tRHZ79wKbj7N0MqKdtCJ0k3vXGzI-9pmaUY9yl7Hb7mm4dKL4KLWtuVZqJotPhXXel1rZTggeGAkjeqzgJJcxIJm_QtzwdSiBzFbQjQTWh0vYT7jHg_iWkhX9r97FjXdXlXjqBTmaS96ZT4OBTJ4Tk7TbrIfOkxgCEaf059hEn4p2_TcsnShuhAdb_gifH7qWm3W73y8H9s1GfpRicAvvuKYNLDftz8Yk_XqS5D-7b0UO5H_g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/66d56a19f2.mp4?token=axPtURPPevTQ6awhz3ogeNZDk3Z3fdA6on1Vkdih2c_0jbw8NrCkRuaCEU1ilzrUXUT6tUO2xUYnFsyefmdlo1E1lEbWHZM4hDu_3tRHZ79wKbj7N0MqKdtCJ0k3vXGzI-9pmaUY9yl7Hb7mm4dKL4KLWtuVZqJotPhXXel1rZTggeGAkjeqzgJJcxIJm_QtzwdSiBzFbQjQTWh0vYT7jHg_iWkhX9r97FjXdXlXjqBTmaS96ZT4OBTJ4Tk7TbrIfOkxgCEaf059hEn4p2_TcsnShuhAdb_gifH7qWm3W73y8H9s1GfpRicAvvuKYNLDftz8Yk_XqS5D-7b0UO5H_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: با «وحشی‌های» حاکم بر ایران نمی‌توان به توافق دیپلماتیک رسید
بنیامین نتانیاهو، نخست‌وزیر اسرائیل شامگاه سه‌شنبه سوم شهریورماه درباره احتمال دستیابی آمریکا به توافق دیپلماتیک با جمهوری اسلامی گفت اسرائیل در اصل مخالفتی با یک «توافق خوب» ندارد، اما نسبت به امکان رسیدن به چنین توافقی با حاکمان تهران تردید جدی دارد.
نتانیاهو در جریان یک سخنرانی با اشاره به گفتگو با دونالد ترامپ گفت: «به او گفتم یک گزینه، البته، رسیدن به یک توافق است؛ یک توافق خوب. ما مخالفتی با آن نداریم.» او سپس با لحنی تند افزود: «اما تردید دارم بتوان با آن گروه، با آن وحشی‌ها، به توافق رسید. به شما می‌گویم: نمی‌توان به توافق رسید.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/78047" target="_blank">📅 17:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78046">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AQDjQodwK8OB9d6QyyyONB2bey_FpsOu2-nrHqnrQiFvharL0QcW4NYn5NiBc1A2z5PIcVpqd-fyMihBCSxmOBsSEKwUfxft4ddOsDJ7q4q-fXjjPzhVzPKp-5tGb0WKwAgu3ahjHrEzpi-3NfCa_O5GjswvnW48e6HWmUMIpQlDS_g2Z0AP3fhWp_PfSBdhdnT13SMBeJY0m09AOpFUv4WTcLxc0MQT-GLAbLlbpA2Bj8CY7CaLk9ioc4aLsfoXhqypiOsUOyQL-d1LlydD-_TjzcvBuhLg1OmV59G_zfFhO4GW0V0XjFFoeCnnvljEXsbY2Z_NtcVmPz-quYBgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیح شاهوردی، بازیکن پیشین تیم‌های پایه باشگاه سپاهان، در جریان اعتراضات ۱۸دی۱۴۰۴ در منطقه «خانه اصفهان» هدف گلوله جنگی نیروهای حکومتی قرار گرفت و جان باخت.
او ۱۹ سال داشت و تنها دو ماه به پایان دوران سربازی‌اش باقی مانده بود.
مسیح شاهوردی شامگاه ۱۸دی در منطقه خانه اصفهان از ناحیه پهلوی راست و کلیه هدف گلوله قرار گرفت.
اصابت گلوله باعث خون‌ریزی شدید داخلی او شد.
به گفته یک منبع مطلع، فضای امنیتی حاکم بر منطقه و شرایط آن شب امکان انتقال فوری مسیح به مرکز درمانی را از دوستانش گرفت. آن‌ها پس از گذشت چند ساعت، او را با پای پیاده به منزل رساندند.
مسیح شاهوردی حدود ساعت یک بامداد در آغوش برادرش جان باخت.
خانواده او با وجود جان‌باختنش، مسیح را به بیمارستان منتقل کردند؛ چراکه هنوز امیدوار بودند بتوان او را نجات داد. براساس اطلاعات دریافتی، کادر درمان پس از معاینه اعلام کرد که هنگام انتقال به بیمارستان، خون‌ریزی فعالی وجود نداشته و مرگ او پیش‌تر رخ داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/78046" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78045">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qrmJA_oB49pxfF75DnVygualVw5OYgQhLDNcjfuaBVPwZIEUs5uXbKnnCB6ACwdKWhaXZ76TSmqQguzE1XYpEaJq21wd_UQXp0fB9ro5cKYTx0V8amniCscmo43HUfzd3AifIF5q_ATjITYuiGE051UWjSiD9T6jD1Z_qHysPUKsQHMwcZmKlB8jx73VAVr-oNvWnghUry5-eIi3hrvhPTJs_eBIllRseikayh1RLjrksw6ua5dHG-6c34XKUAmGrenmRlprH3YVJdt5dISG1kS0lkyalhlTLsWNaBkPoaN9Irn8f0ECXOOKarQcbfSM-QDgsv7OcQSiDQ1b1AxGdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ با بررسی واردات گاز ترکیه، ارزیابی کرد که هشدار جدید واشنگتن مبنی بر مجازات اقتصادی کشورهای طرف معامله با تهران، این کشور را که متحد کلیدی آمریکا و سومین شریک تجاری بزرگ ایران است، در برابر چالش قطع واردات گاز از ایران قرار داده است.
ترکیه در سال گذشته ۱۳ درصد از گاز وارداتی خود (۷.۷ میلیارد متر مکعب) را از ایران تامین کرد و ایران پس از روسیه، آذربایجان و آمریکا، چهارمین تامین‌کننده بزرگ انرژی آن بوده است. با وجود انقضای قرارداد ۲۵ ساله در پایان ژوئیه، دریافت گاز ایران همچنان ادامه داشته است.
اسکات بسنت، وزیر خزانه‌داری آمریکا، اعلام کرده است هر کشوری که به روابط اقتصادی با جمهوری اسلامی ایران ادامه دهد هدف تحریم قرار می‌گیرد و دونالد ترامپ در حال رایزنی مستقیم با رهبران جهان است. این موضوع احتمالا شامل تماس واشنگتن با رجب طیب اردوغان نیز خواهد بود.
بلومبرگ ارزیابی کرد اردوغان که ماه آینده عازم واشنگتن است و برای خریدهای نظامی بزرگ از جمله جنگنده‌های F-35 و F-16 به چراغ سبز آمریکا نیاز دارد، بعید است به دنبال خشمگین کردن ترامپ باشد. به گفته کارشناسان، در صورت قطع گاز ایران، آنکارا می‌تواند این کمبود را با افزایش واردات گاز مایع (LNG) گران‌تر— به‌ویژه از مبدا آمریکا — و اتکا به ذخایر پر شده خود جبران کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78045" target="_blank">📅 00:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78044">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jQLZ44rGr9l2q7Ml1zQhV6ZJPYqCS-thVDBkQWMsDK00EVXxb029ThITYDePcB7Fpw44ivC1SDFNpnw7EhJWoVI-8275rs2xieNPq8Sw-jsLca0LPlY0vQi4axrI-oZDPy8-hRratpUZ8-INrEcvhe0c1J8GbiCVua_pFfY1BFJ4C9HWGuguOoU3IN2RGbbUMbA8XJfPRkYsDdZePMnOcY8KiurDPwhU06uHiyc0gEfiGzJqo04CKwV2Ka-tEgBUuJ_apsMLBPYKTlPC0pos8cG-gCcBEEc902_egQYXiLyfbJxVU5IOiGSYg9WxfYSTt9ucHzmEbZRg5Slfcy_Fzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان هیلی، وزیر خزانه‌داری بریتانیا، اعلام کرد دولت این کشور در کنار آمریکا و دیگر شرکای خود به اعمال فشار اقتصادی بر جمهوری اسلامی ایران ادامه خواهد داد و برای بازگشایی تنگه هرمز و مقابله با «فعالیت‌های خطرناک ایران»، اقدام خواهد کرد.
هیلی، روز سوم شهریور ۱۴۰۵، در بیانیه‌ای گفت دولت بریتانیا از زمان آغاز به کار خود تاکنون بیش از ۲۴۰ تحریم علیه ایران وضع کرده است؛ تحریم‌هایی که به گفته او در واکنش به اقداماتی اعمال شده‌اند که امنیت مردم و بریتانیا را تهدید می‌کنند.
وزیر خزانه‌داری بریتانیا افزود لندن مصمم است مانع از آن شود که جمهوری اسلامی از اقتصاد جهانی یا نظام مالی بریتانیا برای پیشبرد برنامه هسته‌ای و فعالیت‌های بی‌ثبات‌کننده خود استفاده کند.
او همچنین از تلاش‌های آمریکا برای دستیابی به راه‌حل دیپلماتیک حمایت کرد و گفت بریتانیا از افزایش فشار بر جمهوری اسلامی، از جمله در قالب عملیات «طرد اقتصادی» آمریکا، استقبال می‌کند.
هیلی تاکید کرد بریتانیا به همکاری با شرکای خود برای حفاظت از منافعش ادامه خواهد داد و برای بازگشایی تنگه هرمز و مقابله با آنچه فعالیت‌های خطرناک ایران در منطقه خوانده شده، اقدامات لازم را انجام خواهد داد.
وزیر خزانه‌داری بریتانیا از جمهوری اسلامی خواست فعالیت‌های بی‌ثبات‌کننده خود در منطقه، از جمله در تنگه هرمز، را متوقف کند و وارد گفت‌وگوهای دیپلماتیک شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/78044" target="_blank">📅 00:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78043">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dzeP8Wk94E0wX3Nv1y2-ATYFwa9xjH6DiqaRVEX1ojpnoz0Q9eUvkDfdpgLu4miqEw16D3d9O78bK-74Y3P3gBYW6JlQpeTc24OiiPfuhWohFtDQMeNvf74VuAsWgB9wKnvgSzeaoCiFkpB03_rxddBFX40YHvcxrg5Vgp3HPX5xGZu3UA59FlN87cauju7gfnFeshjWx2rx12pKrRQYN3PGN07QUbe462ETqeLNloKVSj0Ptkm1lyMgjNpaJCHxSM3Ey3NYWbCOyusRTeURqK_kG6uME2LQQOZtX9SbHFoI9DWFIXNiZnYVlitaOwOYJ9CLlQ5DBKxSmleeVBzx4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود نبویان، عضو کمیسیون امنیت ملی مجلس، سه‌شنبه سوم شهریور در شبکه ایکس با انتقاد از عملکرد وزیر خارجه جمهوری اسلامی نوشت عراقچی بر اساس کدام مجوز از دستور مجتبی خامنه‌ای مبنی بر «انحصار» مدیریت جمهوری اسلامی بر تنگه هرمز تخلف کرده است.
او افزود چرا وزیر خارجه بدون ملاحظات امنیتی اسباب محکومیت و اجماع سازی علیه جمهوری اسلامی، به سبب «اعمال مدیریت لازم و درست ایران در کریدور جنوبی» را فراهم می‌کند؟
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/78043" target="_blank">📅 23:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78042">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZQ1rLr-Jzsa0AEqxZMHUk-3xOMBQoIN0CQ0djG3R7cmI85Fgo7LHFUAl18-sV5JUTgWS-8d3fvOOFS5R0pGjgn83zjTZefWxeekJ0ZTMPNt1O7AQbhXbScMn2L1M83-czLWAxZQ9Z7hpa2TGJUl8vIkwExFuRZONyT3wJgZdOEcpMme_M4mbeHnZGDwo4fb4cyqnMTTb3cZOmozEqJyakdl15zE9UAnXslT92So13TKmH50vXoSq0jFqucgSv9kSpF5NEKlgprXz5_B3X1PQ0AqL18g3xKtwstV87zTaLPM-_trMYmKwrPaasP2ZVWtbxqYvQlrbXMosffKiHmx5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی، با انتشار بخشی از ویدیوی نشست خبری اسکات بسنت، وزیر خزانه‌داری آمریکا، در شبکه اجتماعی ایکس، با کنایه از اظهارات او درباره تحریم‌های جدید علیه ایران انتقاد کرد.
در این ویدیو، خبرنگار با اشاره به ادعای بسنت مبنی بر آغاز «روز دی (D-Day) اقتصادی»، از او می‌پرسد چرا تحریم‌ها بلافاصله اعمال نمی‌شوند، و بسنت در پاسخ می‌گوید: «چرا باید بخواهم سیستم مالی جهانی را منفجر کنم؟»
قالیباف با طعنه به این تناقض در سخنان وزیر خزانه‌داری آمریکا نوشت: «او ابتدا می‌گوید روز دی اقتصادی! اما پنج ثانیه بعد می‌گوید چرا باید بخواهم سیستم مالی جهانی را منفجر کنم؟ جناب، اینجا ساحل نورماندی نیست؛ این یک نمایش کمدی است و شما فیلم‌نامه خودتان را هم فراموش کرده‌اید!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/78042" target="_blank">📅 23:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78040">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uf0O5p_7K3tLT7bblXWFKnKbtz1P4mk3LaB_U-sWOd7cZBA8JkwXyEoabAe1oJdVsY4IHMZfvySRvztkM3NsP1egBcYeBFgdGg2w7XdzEXd2BoGVeCtOa2fm3I6sOLjLftImkFUlzqbpufq0p52R8KS0wIeh3RjW-ow5bTKpLcW_DKOeanNkSRvw6S-UeewIzDfPT0dkY0wovyws3kvQmIcxuy7dY2Wtgkj0W51uXyB5XDchN8tS3s2XsxT-kPOA6c8zi51S5Z_d4kLgwcoGk-qqXXFIuEKVOf0ef3ZaE9blHxj-XibSG7z5PZ8WggHzallhFCs9TACU94-a3xIfAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NiAKKMvjQjN3AYGOG4WG94QbjrVaY3KwDTaLqhgQ75WaAzqsaOyyaPkaWABEqf7JfKh4NPVakMvo45_qKnn-6dgV1AGLilxyyWu2iuGvHJWtGJ43EahrAovRX08btJMn98jrZiE1UcGgfxEfTEsBUf6NMAI_tXaGaAQ2jYlf1LV-KVphANx6acRiN4nVM23l_h_kJe0erdblJbEGfkNIH9BBPbGJvyc-BMWTOKZlHE3MFl3nxOd1HlCkTyCRtBOKkWw0Fa9TB_kRIZpBzFEmtuWN_b5QznZdnOuycfQcCBXHFbuRhp30Bd7Bj-x3w3ozLTz_AgOrdpoknXRUTCe-fA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو منبع آگاه به گفت‌وگوهای مارکو روبیو، وزیر خارجه آمریکا، با مقام‌های کشورهای مختلف، به کانال ۱۲ اسراییل گفته‌اند واشنگتن در حال حاضر انتظار ندارد حملات تهاجمی جدیدی علیه ایران انجام دهد و تمرکز دولت دونالد ترامپ به افزایش فشار اقتصادی بر تهران و تامین امنیت کشتیرانی در تنگه هرمز معطوف شده است.
به گفته این منابع، روبیو احتمال اقدام نظامی آمریکا را در صورت آغاز دوباره درگیری از سوی ایران رد نکرده است.
این تغییر رویکرد همزمان با اعمال تحریم‌های جدید علیه جمهوری اسلامی و ادعای دونالد ترامپ درباره پاک‌سازی تنگه هرمز از مین‌های دریایی صورت گرفته است.
بر اساس این گزارش، دولت ترامپ قصد دارد در مرحله کنونی فشارهای اقتصادی بر ایران را افزایش دهد و شرایط را برای عادی‌شدن عبور و مرور کشتی‌ها از تنگه هرمز فراهم کند.
منابع آگاه به کانال ۱۲ گفته‌اند انتظار می‌رود این رویکرد دست‌کم تا انتخابات میان‌دوره‌ای آمریکا در اوایل نوامبر ادامه داشته باشد و پس از آن، احتمال بررسی گزینه یک کارزار نظامی گسترده‌تر دوباره مطرح شود.
@
VahidHeadline
پیش‌تر:
پایگاه خبری اکسیوس به نقل از مقام‌های دولت آمریکا گزارش داد انتظار می‌رود تحریم‌های ثانویه گسترش‌یافته، دست‌کم تا پس از انتخابات میان‌دوره‌ای آبان‌ماه مسیر اصلی اقدام واشینگتن علیه جمهوری اسلامی باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/78040" target="_blank">📅 22:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78039">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ggiMMIacDkbrKaIqmkOlER4ePbU3S-v0ufmyMyRU2Wrk9C84CwtlIm5f-E2t4Yseir9KwjzvkXIzdYaPBMTZEvclBL41xHkxwGEH0l9WRvAOOEhtsRcy7Tv2ISeWrGNEGrVykOdmoM6uxJNXgSbxNCF97a5257YUT_4S5kbjcsd6QWU_pYxsHBJYXb0nSxvcAP5LVzpNYI8VssZwhiJN810sFIyOfcNiqqKXM9vQDvc8vghKJB9Y6F4WllryaAIsOPIg6D7hx3PhE03NpcJrXsro8EgZVCptJbqG0aQL2rfdsYy-cFVn1eG7HB2Hwg98FX4fNTfoHuYWds4wtzMDoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی نیکزاد، نایب رئیس مجلس شورای اسلامی، در گفتگویی با خبرگزاری ایسنا از کاهش دو سهمیه بنزین بر اساس آخرین تصمیمات مجلس، سخن گفته است.
به گفته او سهمیه ۶۰ لیتری بنزین با نرخ ۱۵۰۰ تومان محفوظ خواهد ماند اما سهمیه ۷۰ لیتر با نرخ ۳ هزار تومان به ۵۰ لیتر کاهش پیدا خواهد کرد.
همچنین سهمیه ۳۰ لیتر با نرخ ۵ هزار تومان هم قرار است به ۱۵ لیتر برسد.
او البته گفته است: «براساس آخرین تصمیمی که درباره بنزین گرفته شد، مقرر شد که قیمت بنزین افزایش پیدا نکند.»
اشاره او به بنزین ۱۵۰۰ تومانی است.
آقای نیکزاد تعیین نرخ چهارم بنزین را رد کرده است.
دیروز رئیس دفتر مسعود پزشکیان، رئیس‌جمهور ایران، هم گفته بود سهمیه بنزین حتما کاهش پیدا می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/78039" target="_blank">📅 22:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78036">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hUsbzC8Aj3gUsTe77QfXjNwQtCOx5hoLbg5RDiTo6ivp_CTkeNYxPQrFKjjx0-Xz4ZDJ85QRv2y1QHGH9rGD95STfEqYKmby_PeK6E4pb1h65nYkt27DdVksF8GKgNPgpkiUpdVkv9lpyvWsmMydwMKKyK8oH56sHRNpOAdyk0bmo3GO18L8DvJRv3B9ho8qNojLqTSbyOV5af25hlIB00-tDFCIm7HEUWNtgQxA09uN_Bb66u4YrN-fFS60EGDNLNNdjn2OU8TO7zW21uXyr40jajgFzNsier4aviMDF_wst101TmfGfpWy0tUSZGJP_t5TSZ9vdG6x2bMmCfLCIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pb0l0_fKL7QdBvpNJ_t5fuUX4rC7fwoDHw1cYGePDIINEM3DzAqtUcOUgx3DC0JN8LynRbQLm1SN14sCgsyW30snIs6H8flT1u_eVdW52LYG7yxZbBjzAuScKoM35D8ih5uXzkiM7YAxTJmYlqioTcWbwOXVH6lTvDB8FwCKNXI14TM3VLZICVZ3cZYPfIiMWdgdaBKIqVDZzWjkvNkJXg9HLhPM_KfdXNRV3zkeRIBarUlbDb9EMPFXJ0jO8CLFbUwsbPtDfOxe18i6uZv7KHbF8hJmPQ3lLbmG53ksomNDafuDgAvKwOABcF3HX1IrmOqGFu8k1CaKHIW7LyLSLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SQdtGoPLYCh_vWQvFW8nYwVX_OEbOd_7S_KENck3KMCh2FsWIRKaA13K0I26aUiakblKb-Jifcz0w0liocutzF_CCH1j2JCmhq-oNPD91uzPdYun90G73ZjuFpN2qLr5GcJ3--fqyeJuejfQ7fE-UNdqg1iMDgmXVYn4M8M7JJK54PsoKDmOtCDdQ2Q9XudUq3pWKnqCXHKAdgFQm2Ww7vhrElNFbp0_3c6SZJQeMDZTNRBHA7qfz0YnaQC3lyNyzwBysGMa6ecfqXJr7vVsJqSgdhYfcGaiVURK0Trh0oYMZBYPHOSbe4ObVAvehRFzH5vfaoZN5oRCzEd6TQdjxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست اسکات بسنت، وزیر خزانه‌داری آمریکا،
ترجمه ماشین:
رهبران ایران دارند به چیزی اعتراف می‌کنند که حالا جهان می‌تواند ببیند: فشارها مؤثر واقع شده‌اند.
مسعود پزشکیان، رئیس‌جمهور ایران، با اذعان به کمبودهای اقتصادی کشور گفت: «جنگ بالاخره باید در مقطعی به پایان برسد.»
محمدباقر قالیباف، رئیس مجلس ایران، حتی صریح‌تر گفت: «هرچقدر هم قدرت نظامی داشته باشیم، اگر مردم گرسنه باشند و گردش مالی، رشد اقتصادی و تولید داخلی نداشته باشیم، دوام نخواهیم آورد.»
در دوران ریاست‌جمهوری ترامپ، وزارت خزانه‌داری به قطع هر شریان اقتصادی که این رژیم را سرپا نگه می‌دارد ادامه خواهد داد، تا زمانی که تهران تنها بماند.
SecScottBessent
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/78036" target="_blank">📅 20:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78035">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ctocHWM_MHrMpf57DHFhLLhZIKYhBI1Ob-oK8ghsYC9_WMfrhoHXK0lhPUKPaBg79n_CbSPGpcLYI3yiZefiGTM-UajtmerMnGo2Y_pZdVZgf0Ib5UOJV3UXqdmwgG-5TS5Pv2OMR3gyE0AYVB5nm99esCBAR7tqF96pGUQQXKOBzvu-UH8XecZikvyvQY-tWRJ6Zt5BWOBgFC2bsAQcrZrRUdskhV85Xh1nrseBc1XNuObXDF80kr_2gDrKsbPOpPkxWEcdBioAFDAKo2QH4ExY8WHp5n1dq-2q2QNgefqdLEidYG-7FVaxFggdfSbHzLAq3H7MnHIG6Dk6rCb-1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه
بیانیه
: گفت‌وگو کردیم که مذاکرات ادامه داشته باشد
در پی سفر بدر بن حمد البوسعیدی، وزیر امور خارجه عمان به تهران و رایزنی با عباس عراقچی، همتای ایرانی خود، دو کشور بیانیه مطبوعاتی مشترکی در خصوص از سرگیری دریانوردی ایمن از طریق تنگه هرمز منتشر کردند.
بر اساس این بیانیه، وزرای خارجه دو کشور با تاکید بر حفظ حاکمیت و حقوق حاکمیتی خود، درباره چارچوبی مرحله‌بندی‌شده و قابل اجرا برای مواجهه با وضعیت کنونی تنگه هرمز و پیامدهای ناشی از جنگ اخیر گفتگو کردند.
چارچوب پیشنهادی شامل ایجاد یک گذرگاه دریانوردی موقت مشترک از طریق تنگه هرمز و اجرای پروژه‌ای مشترک برای پاک‌سازی تنگه از مین است. طبق این توافق، مذاکرات فنی میان تهران و مسقط برای دست‌یابی به کریدور دائمی، مدیریت ترافیک، تبادل اطلاعات و ارائه خدمات دریانوردی و امنیتی ادامه خواهد داشت.
همچنین دو طرف بر اهمیت گفتگوهای مشترک با کشورهای هم‌مرز با خلیج فارس، رعایت حقوق بین‌الملل و احترام به حقوق حاکمیتی کشورهای ساحلی تأکید ورزیدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/78035" target="_blank">📅 20:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78034">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mQTvI26EqTYOcfg-ClX1fC1UvdvUqV67sHslRDYamHHtSiIzVyzje3xuHgcFU3gonFqPr6kx8s02sUSCtynw0hxKFVlp3QlMqeORIpQ1eFQbwJcJsi9fenb2IvD7C3HZX1Nx8gy_dgsaLteU-y80LKKNK_ol_cijbFJ0oZQGPi3auY9LHdBjYCp_0FFQE8i7Qqhgia_lWAakErM_CEByggWmfc-H22oDL2mMJh5aOT4q-nItOhJ8NEFYesuZqzecjUA_rs3FQ17z6foMLxKdhfsQJO39DsmyarFNE3DSCc8O5sBsdYSELkyDffj73tnyJgYhHwPmik6NXu-qG8e1gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌ها و ویدئوهای مختلفی در شبکه‌های اجتماعی از «تعطیلی» تعدادی از جایگاه‌های عرضه سوخت در تهران و تشکیل صف‌های طولانی در مقابل پمپ بنزین‌ها منتشر شده است.
برخی رسانه‌های داخلی از جمله خبرآنلاین، خبرگزاری دانشجو و عصر ایران نیز تعطیلی چند پمپ بنزین در تهران را تأیید کرده‌اند.
در همین حال فریدون یاسمی، مدیر منطقه تهران شرکت ملی پخش فرآورده‌های نفتی با تأیید تعطیلی چند پمپ بنزین در تهران، «افزایش ناگهانی تقاضا و ترافیک مسیرهای مواصلاتی» را «منجر به تأخیر در ارسال محمولات و اتمام بنزین در تعداد محدودی جایگاه و بسته شدن چند ساعته آنها» عنوان کرد.
به گفته او، در روزهای اخیر توزیع بنزین در تهران «۳۰ درصد» افزایش داشت. یاسمی مدعی شد «تأمین سوخت تهران به‌صورت پایدار در حال انجام است.»
خبرگزاری فرانسه نیز روز سه‌شنبه، سوم شهریور در گزارشی از تهران، از تشکیل صف‌های طولانی مقابل پمپ‌بنزین‌ها خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/78034" target="_blank">📅 19:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78033">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cnP6PrK1l3oA5dYreWHjpBfMrr6cXBHRYXAojP20t2HdM36NWJ4At74lnrhK8ZzzQF9MAC9tretN3ORtgF-bcFYiJlDQ97baRmbwtUuefWYi9b87l4UOfwFvabQPJHWxAzefV9HB0g4bsMMAgcYCCdL8o3TWc5Fjd9Q4y1Z3oU5ruYA3JphbVSblrWuHuOmuyZZzktVV4ue-puWchnUg2_xhEZN-i3kq8Rs2rQBmDEHF2XrLuPGzpWg_WNhX3OxueksZuJ5DoOL0LZrupXGRR3krMldigsG1EFkoiwIzycRlrwzdynrTl-ha5Lpm1xz786bswVKJwVQYqOtQX0QdOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ، چند دقیقه پیش:
همین الان نیروی دریایی ایالات متحده به من اطلاع داد که همه مین‌ها از آب‌های بین‌المللی تنگه هرمز جمع‌آوری و/یا منفجر شده‌اند.
به ایران اطلاع داده شده است که هر کشتی یا قایقی که مین‌های جدید کار بگذارد، فوراً و به‌طور نظام‌مند نابود خواهد شد.
از طریق نیروی فضایی، ما تک‌تک وجب‌های تنگه را زیر نظر داریم؛ همان‌طور که کوه پیک‌اکس و سه سایت هسته‌ای دیگر را که پیش‌تر نابود شده‌اند نیز زیر نظر داریم.
سیاست «تحمل صفر» در قبال مین‌گذاری به‌طور کامل برقرار و لازم‌الاجراست.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/78033" target="_blank">📅 18:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78032">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VX9Oc2UNcVr2ZoSaUfg4BA5INaaVuVxbWGSCCVdVf7AaWFDagy1ysvAubsUmKEvum3VuZ_QrOfuqHjLu3SQTpUd4DGq0n4DBwF27lp-nOrqyuUv05ivPslOPTPKaeq32PusRIGzPC4bd3UjShQci8VAqb_4wFQ0-5Ygu6ZyvwHBiuBA6rR1H-632mcvzm1lCXloKELsTmGTO2neO-GLu1stHvB9KXCnJc25lZ8KF9dcE0zZWHBTMhIm_Z7X4-HC6j4Kl1Ttkvfiw8ZYJfuLwlsG-1lFXysLkhvz7Yacy6s6RWakA2G31vpagQ1OLq_nYLd9cuqJ9uMIxw1IW9Ox3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ چند ساعت پیش:
جمهوری اسلامیِ رو به زوال ایران، حقوق بخش‌های بزرگی از نیروهای نظامی خود را نمی‌پردازد و هم‌زمان، معترضان را ــ حتی زمانی که در حال اعتراض نیستند ــ در ابعادی بی‌سابقه می‌کشد.
این یک بحران انسانی در ابعادی عظیم است و باید همین حالا متوقف شود.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/78032" target="_blank">📅 18:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78031">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JF54MKNpSdp0Mq7zkcQoW-If8-s4MXbuZiuoHpV8SSqYpfRmi3rgc7y5pvpFKHais0z1TiP3B8m6JhK3-qGcRbBGRYPQq0s2yupecXn1Y2Vhx2-q0ujf0YImbjGMxJe-eqeBL7lC6No6OGdy7TqjkOEQohlXdfFv1cpdhmbV_OAp9dTuNNqzzpASO3VezPqlNSbWFV3hiPCkVJ0gdIWTOwPvRK4-Dic7SxbQEv8KkbECS7ZEUWR3Cyg_vLwx-bBrRa7nsIs0Nh52fe7y8fduqgN-7u_rREf6ebEEo4FKkWyndAJExwzfLIAiklvuElZLPJesT6XCGdlISyHZtXW6Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران روز سه‌شنبه سوم شهریور ۱۴۰۵ به ۲۰۵ هزار تومان رسید و سکه امامی نیز با قیمت ۲۲۴ میلیون تومان معامله شد؛ رکوردهایی تازه که ادامه سقوط ارزش ریال و افزایش التهاب در بازارهای مالی ایران را نشان می‌دهند.
براساس قیمت‌های اعلام‌ شده، هر پوند بریتانیا نیز به ۲۷۹ هزار تومان رسیده است.
دلار در آغاز هفته حدود ۱۸۶ هزار و ۵۰۰ تومان قیمت داشت و روز یکشنبه برای نخستین بار از مرز ۲۰۰ هزار تومان عبور کرد. بر این اساس، بهای دلار طی چند روز نزدیک به ۱۰ درصد افزایش یافته است.
سکه امامی نیز که در ابتدای هفته حدود ۱۹۱ میلیون تومان معامله می‌شد، با افزایشی بیش از ۱۷ درصدی به ۲۲۴ میلیون تومان رسیده است.
جهش قیمت ارز و طلا یک روز پس از اعلام بسته تحریمی تازه ایالات متحده علیه جمهوری اسلامی رخ داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/78031" target="_blank">📅 18:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78030">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gs56BvvkyS7pEdJ3n7_ehXnL0T8R86QWNpAT27t_cNipZlRihzIn-6gJF6HJEVcdGLW3qf9O0ETnvoOmKdCJQShKTZg7RbM731GOpzDadBEGLniioGZqMl2A0-JfobAnHRzmRFbSPNrSV_Ej2gh1IlyG2eJ3OdDJBFDW-oAF9jY5AT3T5YMLHxN2Sss1F36T_2Ey4JZsNbfnGf5XmdzxcnTk1SHs5qKEjPXxWvdvcQsvarUpm5N4TQ3UjA-QZj_blrteoqrxs6VHp8K3BO64LwJ8-YZQzOUGVl5WF1ivMMSXXfwHjoab7yl9gkPxLdaAoFheJwDlEp0lO0-GInYwQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتایون ریاحی، بازیگر پیشین سینما و تلویزیون ایران، از تشکیل پرونده‌ای برای خود و ارجاع آن به بازپرسی دادسرای فرهنگ و رسانه خبر داده است.
این بازیگر با انتشار تصویری در اکانت کاربری‌اش در شبکه اجتماعی اینستاگرام اعلام کرد که پرونده‌اش به شعبه بازپرسی دادسرای فرهنگ و رسانه ارجاع شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/78030" target="_blank">📅 18:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78028">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LB3tT0YBWoZRjXUIt6YpU5qAhiJVrnRPcy_vVr0lr4LKsAxML9kDmlfkrKUTkVcy_riB_JucCsIa1212Z_4W9ZeFqW4pdx7EydlwqXe4LqV_a-y6d3R2M73CzwdlY1Ru8e3FrVRm13e_uMp7qTuKAadMMlL06r-T_kEylVEKWfU3f7AVKewaVZSYDZCswo_ax_8OToXwZmNjLNE8IqSW_4-dErRDKKWBaJXgA_L47wamqB7oLAbPeVVexkBF9dsrG5UMGGdvB6DL5rniYOfhGUYvLR8OI9qxAO2XffreuQcq0ctIzBwE-egfL6HSOdGbd9EOGO0laAMvAsZqlbmsfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ade157391.mp4?token=IfVcWkxo_fkeXsMKhcnOs7vAk_RmYjDge37bx4MHx8tVuY4lp0JVigDWeDPL2kcuNsHM0RqV7kbu5adduKtQygqYEqjW9iK23iewLPBXjLf_eeiTqy_0ZGiWbL22nYl0tCrUbOcRb1kJb1Xpk799i_aztyIlUCS0aCH2A4yF2alCEQu2j2vPf-UPy1ajp8Xp4n45haez6fyvt0Foq0m15olNHRzkaA0Fj2dbp7-YHOQZubuBNyVl-FxUB5NuFCGPLifGjHr18aCU150oUdrpB0SEMo42P1jOC07HPsn-3lkLMWRjon0TbFOI3A8IRvC5pPtslde_e1g_XrGczpzHGw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ade157391.mp4?token=IfVcWkxo_fkeXsMKhcnOs7vAk_RmYjDge37bx4MHx8tVuY4lp0JVigDWeDPL2kcuNsHM0RqV7kbu5adduKtQygqYEqjW9iK23iewLPBXjLf_eeiTqy_0ZGiWbL22nYl0tCrUbOcRb1kJb1Xpk799i_aztyIlUCS0aCH2A4yF2alCEQu2j2vPf-UPy1ajp8Xp4n45haez6fyvt0Foq0m15olNHRzkaA0Fj2dbp7-YHOQZubuBNyVl-FxUB5NuFCGPLifGjHr18aCU150oUdrpB0SEMo42P1jOC07HPsn-3lkLMWRjon0TbFOI3A8IRvC5pPtslde_e1g_XrGczpzHGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرویس پلیس مخفی ایالات متحده که وظیفه حفاظت از شخصیت‌های سیاسی در این کشور را بر عهده دارد در بیانیه‌ای که روز سه‌شنبه منتشر شد اعلام کرد از وجود ویدئویی «که به نظر می‌رسد بارون ترامپ را تهدید می‌کند» آگاه است.
اشاره این بیانیه به ویدئویی است که گفته می‌شود در شبکه سه تلویزیونی حکومتی ایران نمایش داده شده و حاوی اطلاعاتی از محل اقامت و رفت‌وآمد بارون ترامپ، کوچک‌ترین پسر رئیس جمهور آمریکا، در شهر نیویورک است.
سخنگوی پلیس مخفی آمریکا در بیانیه‌ای که به شبکه سی‌ان‌ان ارائه کرده تأکید کرده است که این سرویس درباره هر تهدیدی علیه افراد تحت حفاظت خود تحقیق می‌کند.
شبکه خبری سی‌ان‌ان در خبری در این مورد نوشته است که از زمان کشته شدن علی خامنه‌ای، رهبر سابق جمهوری اسلامی، رسانه‌های حکومتی در ایران بارها مطالب و ویدئوهایی درباره طرح سوء قصد به جان ترامپ و خانواده‌اش منتشر کرده‌اند.
حدود یک ماه پیش نیز خبرگزاری تسنیم، نزدیک به سپاه، ویدئویی منتشر کرده بود که در آن شکاف‌های امنیتی پیرامون ملانیا ترامپ، همسر رئیس جمهور آمریکا، بررسی و درباره راه‌های هدف قرار دادن بانوی اول آمریکا بحث شده بود.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز دوشنبه دوم شهریور ماه، در جریان یک تماس تلفنی با برنامه زنده تلویزیونی در شبکه ۱۴ اسرائیل، در پاسخ به پرسشی درباره تدابیر امنیتی برای حفاظت از پسرانش گفت جمهوری اسلامی یکی از پسران او را هدف قرار داده و تلاش کرده است او را ترور کند.
به گزارش تایمز اسرائیل، نتانیاهو بدون ارائه جزئیات بیشتر گفت: «ایران یکی از پسرانم را هدف قرار داد. ایران سعی کرد یکی از پسرانم را بکشد، به قتل برساند.»
نخست‌وزیر اسرائیل در دفاع از توافق خود با شین‌بت برای تامین امنیت اعضای خانواده‌اش گفت: «بنابراین، امنیتی که آنها دریافت می‌کنند یک کالای لوکس نیست.»
تایمز اسرائیل نوشت، نتانیاهو با اشاره به توافقی که بر اساس آن امنیت پسرانش و همسرش، سارا، دست‌کم به مدت پنج سال، حتی در صورت شکست او در انتخابات آینده، تامین خواهد شد، از این تصمیم دفاع کرده است.
او با اشاره به مهاجمان احتمالی افزود: «بدون این امنیت، آنها موفق می‌شدند.»
مشخص نیست کدام‌یک از پسران نتانیاهو، یائیر یا آونر، هدف این سوءقصد بوده‌اند و این تلاش چه زمانی و چگونه انجام شده است.
آونر در اسرائیل زندگی می‌کند و یائیر که از برادرش شناخته‌شده‌تر است، بیشتر سال‌های گذشته را در میامی گذرانده و به اظهارنظرهای تندروانه شهرت دارد.
بر اساس گزارش تایمز اسرائیل این تلاش در زمانی رخ داده که یائیر نتانیاهو در اسرائیل حضور نداشته است، اما مشخص نیست که آیا او هدف این سوءقصد بوده است یا خیر.
در این گزارش تلویزیونی همچنین آمده است که طرح ترور ادعایی چندین ماه است که برای نهادهای امنیتی اسرائیل شناخته شده، اما مسائل امنیتی مانع از انتشار جزئیات آن شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/78028" target="_blank">📅 18:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78027">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NGCcIK_litxC7h_ODd33Iq07SXy3gZCsEsSntHWNbM7h5FTv9rRRMPulx7SyEilXmiOzOxQlFDaNl_4ZBwfj-Nl76su_5cww8sfBYd8XO2N-e03RcsIx-3hI4fFFPxWjOrzNefJpGUaGrzRkbMA0liMVG2AjcnN8wVW_Zhma5_PcIIeKnvGSfQ08Yw8vf-q_UN1EFDsoWcTIrJ6ihaIvE4TpE-VAyJOh33od3bJfHlCE8AOK-VTmCtMr4kb_u5tAls18BoR70ELuaYmABQiPqVX6fjFMnGKfTKozEO0ppnPiGPomZv4A5It2yl39JdK53nIRnj0nr0m5D2NLO07hkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه چین در واکنش به تحریم‌های تازه آمریکا علیه ایران اعلام کرد همکاری پکن و تهران در چارچوب قوانین بین‌المللی انجام می‌شود و «نباید با دخالت یا اختلال روبه‌رو شود.»
لین جیان، سخنگوی این وزارتخانه، روز سه‌شنبه سوم شهریور گفت چین تحولات را از نزدیک دنبال می‌کند و برای دفاع از حقوق و منافع خود «تمام اقدامات لازم» را انجام خواهد داد.
او در ادامه تأکید کرد که چین همواره مخالفت خود با تحریم‌های یک‌جانبه آمریکا را ابراز کرده و آنها را غیرقانونی دانسته است. به گفته او، جنگ اقتصادی و فشار حداکثری «تنها به تنش و درگیری بیشتر دامن می‌زند».
آمریکا روز دوشنبه تحریم‌هایی علیه ۶۰ فرد، نهاد و کشتی مرتبط با ایران وضع کرد و هدف آن را قطع «راه نجات اقتصادی» جمهوری اسلامی خواند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، روز دوشنبه دوم شهریور در یک نشست خبری درباره کارزار جدید فشار علیه ایران گفت: «در سراسر جهان، هدف ما این است که تمامی شریان‌های اقتصادی را که این حکومت استبدادی را سرپا نگه می‌دارند، قطع کنیم تا زمانی که تهران کاملاً تنها بماند.»
چین خریدار اصلی نفت ایران است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/78027" target="_blank">📅 17:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78026">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/opN961NkIc6tJk5Oq642tXUJDMm0oNBYZuqATVC9rjwC1n10KCS64UUEAqcOspIKkyY382FSf1fH2TH_m_HTqMEN4YWWaMINkjqd2NR8UvDS5qRE0tHeivSSb912DKSpVSv3EtZLhhZ9VRqpFPqLSmlsLAnLVXC5Wf9LYcLtTyosfik5KdukVfEHJckGyd-rWgty2RR7WSosIk9ppVfOWjg1LrKmr18uy2XuokhIcUf6j-B-ZyP0u6vWnWicOYECiHxMCiN47i1FdDu3ypAYHjEl77UG_Pm201tQjv4y7d8dHQdeJ1Y_ofkcjtHZvgj9alofYJu8WfWiWPuO3zfwOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی پیشه‌ورزاده، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در رشت، از سوی دادگاه انقلاب این شهر به اعدام محکوم شده است.
کمیته پیگیری وضعیت بازداشت‌شدگان
خبر داد که شعبه دوم دادگاه انقلاب رشت به ریاست قاضی محمد‌علی درویش‌گفتار این حکم را در مرحله بدوی صادر کرده است. پیشه‌ورزاده در جریان اعتراضات روزهای ۱۸ و ۱۹ دی‌ماه بازداشت شد و اکنون در زندان لاکان رشت نگهداری می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/78026" target="_blank">📅 17:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78025">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aaccb368d5.mp4?token=AuACegFH-zGwdIcsb0atMcOw6HW08nyieP1xIYZVUCL76wZGN6UKdXsqQH7u8-VW9oL1Aigu28sNvPrUO8q1HsVifjgWQmmho_BwsBN51CSYifPNDfGOg9qX_uZzsp2i7NWj89sKF1IH8nUXyeiZYUTsBh5ciG55-U9M_6hTd15OGXv39ogfq1XupbvWDOlphpzk1FWap1N-RL-XYmNIMWnD6uZZCKTyCcg7FmpRInpdQV0JNdnCw8vXtyDk0Yl_Qg4Twth34ofz73wJF-JR-G0gQ0eoMdPz9nr5b7zJcc8PmlAGoOCwwyHBUh843SQgQulsQzBS2qKf_NXF77AlXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aaccb368d5.mp4?token=AuACegFH-zGwdIcsb0atMcOw6HW08nyieP1xIYZVUCL76wZGN6UKdXsqQH7u8-VW9oL1Aigu28sNvPrUO8q1HsVifjgWQmmho_BwsBN51CSYifPNDfGOg9qX_uZzsp2i7NWj89sKF1IH8nUXyeiZYUTsBh5ciG55-U9M_6hTd15OGXv39ogfq1XupbvWDOlphpzk1FWap1N-RL-XYmNIMWnD6uZZCKTyCcg7FmpRInpdQV0JNdnCw8vXtyDk0Yl_Qg4Twth34ofz73wJF-JR-G0gQ0eoMdPz9nr5b7zJcc8PmlAGoOCwwyHBUh843SQgQulsQzBS2qKf_NXF77AlXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر دفاع آمریکا می‌گوید اعلام کارزار تازۀ اقتصادی علیه ایران، به‌ معنای حذف گزینۀ نظامی نیست.
پیت‌ هگست که شامگاه دوشنبه و پس از نشست خبری اسکات بسنت وزیر خزانه‌داری ایالات متحده صحبت می‌کرد، تأکید کرد که «به‌هیچ وجه گزینۀ استفاده از حملات نظامی در تنگۀ هرمز یا اطراف ایران را کنار نمی‌گذاریم».
وزیر دفاع ایالات متحده در عین حال ابراز نظر کرد که ایران نمی‌تواند فشار اقتصادی تازه را تحمل کند.
وزیر خزانه‌داری آمریکا روز دوشنبه دوم شهریور در یک نشست خبری درباره کارزار جدید فشار علیه ایران، متعهد شد که اقتصاد جمهوری اسلامی را از منابع حیاتی خود محروم کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78025" target="_blank">📅 09:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78024">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g7c3TDkyOuS9P-1ELt6rTSxxdfO1UBGh-Md7Bsxduxwoy7HzdTTzUlF7nXaVoXQu8x2-dnwlVxbiOxdBx-1geoToYwjtLpq5wG_hD5G62fRHXxg2qyttD9PxagSxDBchrc_mXAk8JGuNU9mFdzNsmuCpVulatsdXpH_Z3zv8ddjW-T3Z5voJ7hAhRQVqaDhu6LInAbCkpIt4ZP1wO8XeJpZNTUeHr3jiNq13c8M-WaF6a5743NbtNaC1jRj9Qr6L1wSftTFQigV8t7syUm0pp0R1dScyDXq2CLc9-P--PEaOe0P4JE7Puc_8LQqGBiLriFbOxK2TYYF4JvSMWWzmcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در ۹ مایل دریایی شمال‌شرق «اش شیشه» (Ash Shishah) در عمان دریافت کرده است.
ناخدای یک نفتکش گزارش داده که شناور با یک پرتابه ناشناس مورد اصابت قرار گرفته که باعث آسیب به موتورخانه و از کار افتادن شناور شده است.
گزارش شده که خدمه در سلامت هستند. در زمان دریافت گزارش، تأثیرات زیست‌محیطی حادثه مشخص نیست.
...
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78024" target="_blank">📅 01:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78023">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">(۱۸ دقیقه، ۳۰ مگابایت)
متن کامل سخنرانی و پرسش  و پاسخ:
telegra.ph/bessent-08-24
اعلام کارزار اقتصادی آمریکا علیه ایران؛ بسنت: همه شریان‌های حیاتی آن‌ها را قطع می‌کنیم
🔸
وزیر خزانه‌داری آمریکا روز دوشنبه دوم شهریور در یک نشست خبری درباره کارزار جدید فشار علیه ایران، متعهد شد که اقتصاد جمهوری اسلامی را از منابع حیاتی خود محروم کند.
🔸
اسکات بسنت گفت: «در سراسر جهان، هدف ما این است که تمامی شریان‌های اقتصادی که این حکومت استبدادی را سرپا نگه می‌دارند، قطع کنیم تا زمانی که تهران کاملاً تنها بماند.»
🔸
وزیر خزانه‌داری آمریکا این اظهارات را در جریان تشریح راهبرد جدید واشینگتن برای افزایش فشار اقتصادی بر ایران مطرح کرد؛ راهبردی که بر تشدید تحریم‌ها و محدود کردن روابط اقتصادی و مالی تهران با سایر کشورها متمرکز است.
🔸
او هشدار داد که هر کشوری برای متوقف کردن فعالیت‌هایی که واشینگتن آن‌ها را مرتبط با ایران تشخیص می‌دهد، مهلت مشخصی خواهد داشت؛ در غیر این صورت با اقدامات وزارت خزانه‌داری آمریکا مواجه خواهد شد.
🔸
بسنت گفت دونالد ترامپ، رئیس‌جمهور آمریکا، در حال تماس تلفنی با رهبران کشورهای مختلف است و از آن‌ها به‌طور مشخص می‌خواهد تعاملات خود با ایران را متوقف کنند.
🔸
هم‌زمان وزارت خزانه‌داری آمریکا با انتشار بیانیه‌ای گفت دامنه تهدیدهای خود برای اعمال تحریم‌های ثانویه مرتبط با ایران را به پنج بخش عمده اقتصادی گسترش داده است؛ اقدامی که به گفته وزارت خزانه‌داری آمریکا، در راستای تلاش واشینگتن برای تحمیل یک «روز سرنوشت اقتصادی» بر تهران انجام می‌شود.
🔸
در این بیانیه آمده است: «خزانه‌داری علیه پنج بخش حیاتی شامل دارایی‌های دیجیتال، فناوری، طلا، هوانوردی و کشتیرانی تصمیمات جدیدی اتخاذ کرده است؛ بخش‌هایی که رژیم ایران برای تلاش جهت سرپا نگه داشتن اقتصاد در حال فروپاشی خود از آن‌ها استفاده می‌کند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/78023" target="_blank">📅 22:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78022">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hbH15A8j3VqWHxRqIV8rQIM7zd1KA0MqVzbX4lkmkOCg_VCOXLCpb51kswWiyQyD1VRTyMIJBqAolqV3TKQpdULtJTemQZraw50o0ZE6XgAlbTN-ShrpCN0eA3Tj3EOuUi0K_gVyOUm2oc_ysq1FWx7bnYNi17rvZx_mnktSfJNrVE_vZc5tstE77ogee42gyJu5_S4TowUVXdiDinIqpiGAaAECEXd5TSzX3MA3LC7q_8_WxhIEbAAiFM5i3LepD29i7yuK0IqXE2O8AbnH_bh-aLmEJh7oyhfbF486TEYISoztOhRBY6kqxDm8p-KzzfjPqpPqfV2CxKy6UcYDGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران روز دوشنبه دوم شهریور بار دیگر روندی صعودی در پیش گرفت و در معاملات صبح از ۲۰۲ هزار تومان عبور کرد.
همزمان قیمت سکه امامی به ۲۲۲ میلیون تومان رسید و بهای طلا نیز در سطوح بی‌سابقه‌ای معامله شد.
بر اساس آخرین نرخ‌های ثبت‌شده، دلار آمریکا در بازار تهران به ۲۰۲ هزار و ۶۰۰ تومان رسید. سکه طرح امامی نیز ۲۲۲ میلیون تومان قیمت خورد.
در همین زمان، قیمت یک مثقال طلای آب‌شده به ۹۶ میلیون و ۲۰۰ هزار تومان و قیمت یک گرم طلای ۱۸ عیار به ۲۳ میلیون و ۲۰۷ هزار و ۸۶۰ تومان رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78022" target="_blank">📅 18:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78021">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z9wIGzG8uk9rjf1ZGREXRbvQ6sphC3KVUqM_c1YnhIrMY2l0esqUOgzD7L89q-f1sCpgVWfZ-Zw79TJcox9qCsPW16kG4ehKqxICBu1jB6eDodLZPsBhZoDBL9ShoDGAvxgtWFp4T2yW2tzlonvE2wquZGSkgqQfPnH8mnD-oGUYe9FgWDTLAZrqINHwEfuc8_Vwl0g1SHHx8wYPuvOUleDoflsYrNq9XwZsogfB1aBH4c4w7kG_5UOPVThOHadnjLgJFQcJ9EgNePovRXNz-9m5OSX6EExoN3SmpVtz-MNZp34iOoqQnzkKfHf5KWGdAQPTMN_h_B7zaDywnysA-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
ایران کاملاً در حال فروپاشی است!!!
رئیس‌جمهور DJT
realDonaldTrump
اشاره به ایران در پستی دیگر:
دموکرات‌های چپ رادیکال با نظرسنجی‌های جعلی دارند دیوانه‌بازی درمی‌آورند. آن‌ها این نظرسنجی‌ها را در سطحی منتشر می‌کنند که هرگز پیش از این دیده نشده است. به این‌ها «عملیات تضعیف روحیه» می‌گویند؛ جایی که تلاش می‌کنند روحیه جمهوری‌خواهان را تضعیف کنند تا آن‌ها برای رأی دادن بیرون نروند — اما نظرسنجی‌های واقعی فوق‌العاده‌اند و روحیه در کشور ما هرگز تا این اندازه بالا نبوده است.
ما در برابر همه در حال پیروزی هستیم، از جمله ایران که کشورشان در یک مارپیچ مرگ اقتصادی و نظامی قرار دارد.
از توجه شما به این موضوع متشکرم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78021" target="_blank">📅 16:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78019">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OxYOaie1Mha_YE2wUvp-6YovomXcGen0en34tsxg4Bj1uwRRfqMH7BJ0ohjRhCrfCZ5y_HjSFSL0F9sS2EPv6Szmx_ir6T76bZAci9DDweyH7FT5l05ZSflfFAiLVMjqlr5QdthjeNRkloJdXvc2FFfVPxxDrWrOWQM96NEgp788RDkZS8Y90vpIIO3hdlVa0Itv9eFL3Dok4K4Kff7KyTVjyROmbImIfRfbv3EeG4rnA8u2n1U-DTMQsOmlrHkLk9pCv2pRKaQxweNPU_6SqjORkY-sqFpc1keYKbdXqLNKInXmLx8Fo1KsLvILsHu-N1AjnUULRq39G8L7yrcl0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/joNuuQP1z0yo-enJ_o6UtOQuzgI-mPjE16WQy8PjsgAhYYk2FGU8vXe0mmyp3I9D85iGdat4vAisUvOeCOG7pUWvvXaqrb00S_11xcH0qP7TyxGTWH4WGmB_kJ7A1lPCMDcRXFteaoBCFlpjRjnd7iWprSMyjSjSbt9NUAf2NCuQKMcrs6bbiufVq7i_dva_Zd4ftt-Dm0Uxtl9yzs76ilcyVOD8dy1GFfZdmPEv6Cg9E0STN7Y3Ca-3AP-ETGzttJhjTdrKFuCJ6mnBEhBN7rA63Mce6xaGoNPyGzxihTCJM3A34JC519LKvDYTjJBs7Vt9u5DNXVlXaMMh-c3n3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری ایالات متحده روز دوشنبه دوم شهریور مقاله نیوز مکس درباره سخنان هفته گذشته محمدباقر قالیباف در عراق را بازنشر کرد.
رئیس مجلس و عضو ارشد هیات مذاکره‌کننده جمهوری اسلامی ایران، هفته گذشته در جریان سخنرانی در جمع فعالان اقتصادی ایرانی و عراقی گفته بود آمریکا در جنگ نظامی شکست خورده است و حالا به سراغ جنگ اقتصادی و شناختی رفته است. اگر در میدان اقتصادی قوی نباشیم، شکست خواهیم خورد.
ترامپ این مقاله را در آستانه اعمال تحریم‌های بی‌سابقه علیه ایران بازنشر کرده است.
@
VahidOOnLine
محمدباقر قالیباف، رئیس مجلس شورا و عضو ارشد هیات مذاکرات جمهوری اسلامی، روز دوشنبه دوم شهریورماه با انتشار پیامی در اکس، شعار انتخاباتی «آمریکا را بار دیگر باعظمت کنیم» دونالد ترامپ را به «آمریکا را دوباره گرسنه کنیم» تغییر داد.
قالیباف در این پیام احتمالا با استناد به داده‌های سازمان غیردولتی «تغذیه آمریکا/feedingamerica» و ادعای ۴۷ میلیون گرسنه در آمریکا نوشت: «آمریکا را بار دیگر گرسنه کنیم. با ادعاهای واهی نمی‌توان شکست‌ها را لاپوشانی کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78019" target="_blank">📅 16:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78017">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a_5xPqZq35Y852ukazKmcQVPmi7T9szUKsR6dpsTLP7Wr9pPC_kHjm6ek0_fQgNNkrLgZ0LlR46dGMNVexWxpm-U6fZhZRaSFpNfSMFzbIom_oAhf6VnEMbq8sMAMSdYqBwQR9YTEdpTCDw2Tg93n4N_FA3IbLlqzBuCXivoFFp_R8_o8ZjIM6lOY1cAwpTO8EeGvRD_puihuaFMxT7EzA5BDuRPeBOuME7bGrnyi_H415xTC7scjPHQg9geHPYE3WH_Nmb6Q9CiDCKyPQSGrn88JXG97TtVoXBVonX54sijoNAFY2ee-Ly7P_JvHJutmXUqPeXQiwleSaW2m7fmRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mYFtaZ6Zhme3lmirsA23TheNShlWijx7T876KXuzY-T71TYm8JRHr7djITxaqD6ZHtHhl3YdB69ZdIdfnYLgjowHojy6u9GnYqTV0o2hAIwcqa3TQnqumn31OzpMOFqzXkV1otW5c0nemor8B6oR7uo9wGC0WP19mP-xTWPb3jEkMntesJk_-TVDxRFwrG8PsGehmH-RE2KJcNO28TQE_Ly8xDyopflFFR36SsPdZMKNyIiiLEqATDK9D_shX49lVkCROiCT0nTygcIn-pwlAeQVGfF9WS6-EKB0kY_JAUfw3z0OXymm4nffJUlUaem1cQ-G82izUL1DGHSI8PcONg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فیلدمارشال عاصم منیر، فرمانده ارتش پاکستان روز دوشنبه دوم شهریور ماه وارد تهران شد.
محسن رضا نقوی، وزیر کشور پاکستان او را در سفر به پایتخت ایران همراهی می‌کند.
ارتش پاکستان با صدور بیانیه‌ای اعلام کرد سفر این فرمانده ارشد نظامی به تهران «در راستای تلاش‌های اسلام‌آباد برای ارتقای صلح و ثبات منطقه‌ای و مذاکره با مقام‌های ایرانی بر تقویت تلاش‌های صلح و یافتن راهکاری مسالمت‌آمیز، پایدار و جامع برای حل درگیری‌های خاورمیانه متمرکز خواهد بود.»
خبرگزاری صدا و سیما گزارش کرد عاصم منیر با مقام‌های ارشد جمهوری اسلامی دیدار خواهد کرد.
@
VahidOOnLine
خبرگزاری رویترز به نقل از چند مقام پاکستانی اعلام کرد عاصم منیر، فرمانده ارتش پاکستان، هفته گذشته و پیش از سفر به تهران، با دونالد ترامپ تلفنی گفت‌وگو کرده است.
سه منبع پاکستانی در گفت‌وگو با رویترز تاکید کردند این تماس چند روز پیش از آن انجام شد که انتظار می‌رفت منیر دوشنبه برای گفت‌وگو با مقام‌های جمهوری اسلامی به تهران سفر کند.
به گزارش رویترز، این تماس که پیش از این گزارش نشده بود، در شرایطی انجام شد که آمریکا اعلام کرده است تحریم‌های اقتصادی گسترده‌ای را علیه جمهوری اسلامی و شرکای تجاری آن اعمال خواهد کرد.
در این گزارش همچنین آمده است انتظار می‌رود فرمانده ارتش پاکستان، دوشنبه با افرادی نزدیک به مجتبی خامنه‌ای، دیدار کند.
رویترز نوشت تنش‌های میان آمریکا و جمهوری اسلامی یکی از محورهای مورد انتظار در این سفر عنوان شده است.
یک منبع دیگر در دولت پاکستان نیز گفت: «منیر همچنین قرار است درباره حملات اخیر حوثی‌های وابسته به جمهوری اسلامی به عربستان سعودی، متحد پاکستان، گفت‌وگو کند.»
@
VahidOOnLine
اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز دوشنبه دوم شهریور ماه اعلام کرد بدر البوسعیدی، وزیر امور خارجه عمان روز سه‌شنبه به تهران سفر می‌کند.
به گزارش خبرگزاری صداوسیما، بقایی به خبرنگاران گفت بوسعیدی در تهران با عباس عراقچی، وزیر امور خارجه جمهوری اسلامی دیدار می کند.
در پی حمله آمریکا و اسرائیل و بسته شدن تنگه هرمز، جمهوری اسلامی مذاکراتی را با عمان برای تعریف نظام حقوقی جدید تنگه هرمز، آغاز کرده است.
تهران، مسقط و دوحه از پیشرفت این مذاکرات خبر می‌دهند، با این حال دونالد ترامپ، رئیس جمهوری آمریکا هفته گذشته تهدید کرد که اگر عمان در مسیر «توافق» تهران و واشنگتن مانع ایجاد کند، این کشور را بمباران خواهد کرد.
البوسعیدی، سال گذشته میانجی دو دور مذاکرات میان جمهوری اسلامی و ایالات متحده بود. هر دو دور مذاکرات بدون نتیجه و با حملات آمریکا و اسرائیل به ایران پایان یافت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/78017" target="_blank">📅 16:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78016">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b9437ec72.mp4?token=jp7Gp6i-X87UCTjYlyYTtUFZiHkWtuwW7S_3S1nvLObD0sVYrMlKMXLi3voM8GaUBT0AH3Rqcq3fzwc--10631fLW1T3w73NHU7clco3GVVFz6dZztcmL1lPafhOaFCQX_x86hhcuLCx7oQat8kX7aFgddLNu_b-407hz0GDzhSwnZmvYfZTbuhyeuvfaXIeKGIWXSH35wzD3VjD0ktrqob--o2PNp22UM4vnjsaaEl8XuDQFTsUk26MxBewM4YQ7uX-SLzcnoBSkYJ_yBUMJA4FPRhhB5QiHyYFHhn96cUPzTbFkQO9EqwYdP-WLONbGYQ0Fk7olxS-f2qcka6HuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b9437ec72.mp4?token=jp7Gp6i-X87UCTjYlyYTtUFZiHkWtuwW7S_3S1nvLObD0sVYrMlKMXLi3voM8GaUBT0AH3Rqcq3fzwc--10631fLW1T3w73NHU7clco3GVVFz6dZztcmL1lPafhOaFCQX_x86hhcuLCx7oQat8kX7aFgddLNu_b-407hz0GDzhSwnZmvYfZTbuhyeuvfaXIeKGIWXSH35wzD3VjD0ktrqob--o2PNp22UM4vnjsaaEl8XuDQFTsUk26MxBewM4YQ7uX-SLzcnoBSkYJ_yBUMJA4FPRhhB5QiHyYFHhn96cUPzTbFkQO9EqwYdP-WLONbGYQ0Fk7olxS-f2qcka6HuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@
VahidHeadline
این عدد ۲ از کجا پیش‌فرض گرفته میشه برای تعداد جناح؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/78016" target="_blank">📅 15:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78015">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qz5y62SWCoreXlzBYKs1Vx3xtzhqNXH2R09wy18wEs32usSGuki4HeTawwhYLKW9U2xYMB5P1W51ZUmmwCmjRl_tKLXVn9Z1hcSL2sKLClkitRkbaW5S8LyF3Q0iXl8pKRyRAroGM9MWndPt2ljdf46Ex1-l4nbyyzq0gbPAkWMRqzpPG326o0-D1GDsDYzPGBCO8PEB0OWhZr2mOV2G6HV6V5DsVM21EJLcTVeByizDjp_OM4FHH0dwAOjRa7Wu_V98Id3LvspoTp_XJ7xp8nwn3o1Una3Vq0wEWY4zThxaC6wIW3qLtMAxYeguMWKa1ZgciksFNatQgdsy0cahgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت روز دوشنبه دوم شهریور، در آستانه اعلام جزئیات طرح تازه آمریکا برای افزایش فشار اقتصادی بر ایران، بیش از دو درصد کاهش یافت.
دونالد ترامپ، رئیس‌جمهور آمریکا، این طرح را «کوبنده‌ترین» عملیات مالی علیه جمهوری اسلامی توصیف کرده و از متحدان واشینگتن و همچنین چین خواسته است به آن بپیوندند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، قرار است روز دوشنبه در یک نشست خبری جزئیات بیشتری از این طرح ارائه کند.
در معاملات روز دوشنبه، بهای نفت برنت و نفت خام آمریکا هر دو ۲٫۳ درصد کاهش یافت و قیمت نفت برنت به حدود ۹۲ دلار در هر بشکه رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/78015" target="_blank">📅 15:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78014">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SqZgac-xqdgIY9AxG2WA_RZ644DjBeIh5NwXvhmQIvM4PkaD5KQIn7fufGvIIuxMPGKmXXu0rjIW9OrlwISbuvonLMKuRaDtcRIJnyEQgbHZABJi36yKumtZLaWcJT9h_Jy3bwvFzaM6lTDsTsYvw_1YlCAtcXx67UDplH8bityHLwovErOGZnBZ7SdA_uFVONLdaQeyE5riaMfgK2mOnYNI2jcz3FEESflqC9uKYRQjMC_3tBgw-SVvjhp38Q0aEoWLEwtBffz6MN_WUHjYYuNwyvPXnnHUFrh_bxWztsbt7vpmrWq5IIeNyib_RRR0GQNNaoqupGGwxWeW7s6kTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریانوردی تجاری بریتانیا اعلام کرد: یک نفتکش در ۶۳ مایلی شهر بندری ینبع عربستان سعودی، هدف پرتابه ناشناس قرار گرفت.
این سازمان زمان حادثه فوق را روز دوشنبه دوم شهریورماه اعلام کرد و یادآور شد:‌ بر اثر اصابت پرتابه ناشناس، قسمتی از عرشه کشتی دچار آتش‌ سوزی شد، اما خدمه در سلامت کامل هستند.
سازمان دریانوردی تجاری بریتانیا همچنین اعلام کرد که تاکنون خسارات زیست محیطی بر اثر این حادثه گزارش نشده است.
نام و پرچم نفتکش اعلام نشده و تاکنون هیچ گروهی مسئولیت حمله را بر عهده نگرفته است.
ینبع پایانه اصلی صادرات انرژی عربستان در دریای سرخ است. حوثی‌های یمن ۲۰ جولای ممنوعیت دریانوردی برای کشتی‌های سعودی و مرتبط با عربستان اعلام کردند و از آن زمان حملات متعددی به نفتکش‌ها را بر عهده گرفته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/78014" target="_blank">📅 15:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78013">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/onns3DM-k1cYpOM4mEdzl3xMvvnLNJQ_wgYtaRSZBq9e0s1xWYSrG_-CLkkqueL4PKyprGPKsH5H1pyBX_lySf8K24aNYaJpv3NmYpHv9XnInnIzBMFFhiXkGccexVcWOI_YDpfxpbv25z-7XmhcwMlhCDvDbxLlviLaexDB9i5dvRJ9p2ihWb8_NQPqyKJ3TtCwciVHDYJqE8vtf5hCSkRo3466xFUQigbeAAqeyDTyPeQ-WHM5LvSdnSzXwOIBopMEFvIrPgwJH8QCV9NQ9QXzUbUqhfVxPkd-Dr5t7x247gHhMm4a0x1jc3EVKoTWPzV-Pvqmjg0vuxBFgXfaUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«آتوسا جعفری»، زن ۲۷ ساله اهل سنندج، یکشنبه ۱شهریور۱۴۰۵ مقابل منزل خانوادگی خود با ضربات چاقو به قتل رسید.
رسانه‌های محلی و شبکه حقوق بشر کردستان گزارش داده‌اند که آتوسا جعفری هنگام خروج از خانه و پیش از سوار شدن به خودرو برای رفتن به محل کار، هدف حمله قرار گرفت و با ضربات متعدد چاقو کشته شد.
براساس این گزارش‌ها، عامل قتل همسر یا همسر سابق آتوسا جعفری بوده است. منابع محلی گزارش داده‌اند که او با هشت ضربه چاقو به قتل رسیده است.
درباره وضعیت تاهل آتوسا جعفری در زمان قتل روایت‌های متفاوتی منتشر شده است. شبکه حقوق بشر کردستان گزارش داده که او دو سال پیش از همسرش جدا شده و با مادرش زندگی می‌کرد، اما رسانه‌های محلی نوشته‌اند که آتوسا طی سه سال گذشته برای جدایی از همسرش به دادگاه مراجعه کرده بود و درخواست طلاق او پذیرفته نمی‌شد.
براساس روایت منابع محلی، آتوسا جعفری در این مدت بارها از سوی همسرش مورد خشونت، ضرب‌وشتم و تهدید قرار گرفته بود. یک‌بار نیز در نتیجه ضرب‌وشتم، دست او شکست.
شبکه حقوق بشر کردستان نوشته آتوسا جعفری کارمند اداره پست، دارای مدرک کارشناسی ارشد حقوق کیفری و مربی و داور رشته «کنگ‌فو توآ» بود.
این دومین مورد گزارش‌شده از زن‌کشی در کردستان طی چند روز است. روز ۲۹مرداد۱۴۰۵ نیز «لطیفه محمدزاده»، زن ۴۹ ساله اهل سقز، در یکی از جاده‌های روستایی این شهرستان توسط همسر سابقش با ضربات چاقو به قتل رسیده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/78013" target="_blank">📅 15:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78012">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UQ1EaP670Qh1aPLcFPDv8VnW7LjfwZCRLlQIYIrUM0kSKfWN3sVEYsX_RjZGV0lLKDpmb0B-dXZKTbiPKH7y8G6y79V3ZQ4NyFZTKceWuj6OhBhjmdWDaF13yhE85gpsufsSoTlABCU_TyiazjHpKEfMzurXeqlD3aoC4UuJkgbFi0aWncAhXub9cNig96gQ5pN0TF1v53ijJCViIgPn98LIL1EmnDjMqf9oWF5Qq7TmkkiKqdPjJOW0QUQXJxCCOEP4IAbmcrOG_q_lUJ-U2K-dR2sEZa_pAzFTPFQgJe3Rbrkuirs_M1h0pylvKwcLk2ayH-LMtYIu6iofF9NpDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۲ شهروند بهائی از سوی دادگاه انقلاب ساری مجموعاً به ۲۶ سال و ۱۶۵ روز حبس تعزیری و ۷۶ سال محرومیت از حقوق اجتماعی محکوم شدند.
بر اساس دادنامه صادرشده در تاریخ ۲۹ مرداد ۱۴۰۵، راکوئل عطائیان، کیومرث اکبری، سهراب لقایی، زهرا گلابیان، بنفشه اسدیان عربی، فؤاد لقایی، آناهیتا کوشکباغی، نسیم صمیمی، حسین فنائیان، امیلیا فنائیان، ملودی صمیمی و سهیل حقدوست، شهروندان بهائی، توسط شعبه اول دادگاه انقلاب ساری به ریاست عمار رمضانی محکوم شدند.
در این رای خانم عطاییان به تحمل چهار سال حبس تعزیرى و ۱۰ سال محرومیت از حقوق اجتماعى محکوم شده و دیگر متهمان پرونده هر کدام به تحمل دو سال و ۱۵ روز حبس تعزیرى و شش سال محرومیت از حقوق اجتماعى محکوم شدند.
در دادنامه صادره، اتهام مطروحه علیه این شهروندان «انجام فعالیت‌های آموزشی و تبلیغی مغایر و مخل به شرع مقدس اسلام در راستای ترویج و ترغیت فرقه بهائیت» عنوان شده است. جلسات رسیدگی به اتهامات این شهروندان در تاریخ‌های ۱۰، ۱۱ و ۱۲ مردادماه ۱۴۰۵ در شعبه مذکور برگزار شده بود.
یک منبع نزدیک به یکی از این شهروندان بهائی در گفت‌وگو با هرانا ضمن تأیید این خبر، درباره روند رسیدگی به این پرونده اظهار داشت: «اولین جلسه رسیدگی به اتهامات این شهروندان در اردیبهشت‌ماه ۱۴۰۳ در شعبه اول دادگاه انقلاب ساری به ریاست شجاع ذوقی برگزار شد.
این شعبه به دلیل وجود نواقص در تحقیقات، پرونده را سه مرتبه به شعبه بازپرسی بازگرداند، اما به دلیل عدم رفع نواقص، پرونده از دستور کار این شعبه خارج شد. در ادامه، پرونده به شعبه ۱۰۴ دادگاه کیفری قائم‌شهر به ریاست رضا مجازی ارجاع شد و جلسات رسیدگی در تاریخ‌های ۲۱ و ۲۲ تیرماه ۱۴۰۴ برگزار شد.»
این منبع افزود: «در جریان این روند، سهیل حقدوست و همسرش راکوئل عطائیان بازداشت شدند و امکان حضور در جلسات رسیدگی را نیافتند. این دو پس از آزادی موقت، به‌صورت جداگانه از سایر متهمان مورد محاکمه قرار گرفتند. شعبه کیفری در ادامه با صدور قرار عدم صلاحیت، پرونده را مجدداً به شعبه اول دادگاه انقلاب ساری ارجاع داد و این شعبه پس از برگزاری سه جلسه رسیدگی، نهایتا اقدام به صدور رأی کرده است.»
وی همچنین گفت: «راکوئل عطائیان در جریان بازداشت سال گذشته با پرونده قضایی جدیدی مواجه شده بود که بنا بر تصمیم شعبه ۱۰۴ دادگاه کیفری قائم‌شهر، روند رسیدگی به آن با این پرونده ادغام شد و در نهایت هر دو پرونده به صدور رأی در شعبه اول دادگاه انقلاب ساری منتهی شدند.»
پیشتر، جلسات آخرین دفاع این ۱۲ شهروند بهائی در اسفندماه ۱۴۰۲، به‌صورت جداگانه در شعبه ششم بازپرسی دادسرای قائم‌شهر به ریاست رضا مجازی برگزار شده بود. همچنین پیش از آن، منازل این افراد توسط نیروهای امنیتی مورد تفتیش قرار گرفته و آنها با دریافت پیامک‌های جداگانه از تشکیل پرونده قضایی علیه خود در دادسرای قائم‌شهر مطلع شده بودند.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/78012" target="_blank">📅 15:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78011">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tmpuejm0pP6AJqXqLTxFTOh8XBnXhTWYbjN6NXHIW8KQR_qYdYxSBPEOpvAJsm5X9QvOZp7XR19YqbpnrgioIiKjzE827HIf1bp-R5F_o7GB_2Z7uisioD-zq5Z7WB_R_pzHtJqcIxub--m9FNWm-YLTnUfT0xs4YQhdo124_D1lu4TTpsOi-lGCel7HIv3bq-mJfRKkPIf1cGuQt8_GRgIT0FS_Ni1fO1_Vyopbjl0fkjN6XzkLp574TWBbKpSfUeAtmivWgrlkxxCjjU9tDFpIIaPxfRFUgZuGZaRLA2_kVMM7LBjfIsJYeKFkd6bTTS3UZIWqhegp85-bWB91Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، در گفت‌وگو با نیوزمکس گفت با وجود تلاش‌های جمهوری اسلامی برای بستن تنگه هرمز، آمریکا موفق شده است روزانه بین هفت تا ۱۵ میلیون بشکه نفت را از این مسیر خارج کند.
ونس گفت واشینگتن در تلاش است مانع وقوع بحران انرژی شود که به گفته او جمهوری اسلامی در پی ایجاد آن است. او افزود یکی از قدرتمندترین ابزارهای آمریکا، «وادار کردن تهران به پرداخت هزینه تلاش برای خفه کردن تجارت نفت و گاز» است. معاون رییس‌جمهوری آمریکا تاکید کرد جمهوری اسلامی توانایی قطع مسیرهای تجارت بین‌المللی را ندارد و این مسئله اهرم‌های فشار تهران را کاهش می‌دهد.
معاون رییس‌جمهوری آمریکا گفت واشینگتن ابزارهای متعددی برای مقابله با جمهوری اسلامی در اختیار دارد که به گفته او برخی «قاطع» و برخی دیگر اقتصادی هستند.
ونس همچنین تاکید کرد هدف نخست و اساسی حضور آمریکا در خاورمیانه جلوگیری از دستیابی جمهوری اسلامی به سلاح هسته‌ای است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78011" target="_blank">📅 04:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78010">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hVLWPI-icb_3-VlR3Qd5qTWKZKUoxwhoRCu-mM_TX0rs6Z2pOkQjbgwML5NQgAwNOUpXJG9NM_FQNPCnkczHzpMPUZw8b-Ggiio4PYCC1FnNTvNi5AH4ixnMoT5-6xA8R8dDlg-jV9os_rP-i6LAPINL_iG9xaVXJHoG_03311RlMBk2f_2ngp07zZY3xNpIhBTZKEXpZnjBBG0MBj65GQ7QUbo_e7XtD-SVfVsOmFMYLKFDlyWqGgKAZa4RYu7RIoMSMpBoiR5BcmnH_KT54ZTPFiBWUmEG2TwqaHPNOPMjK8gEkwRyQVEGB7n9oT4fjyjwip61M3AUZiHkGBuFyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست اسکات بسنت، ترجمه ماشین:
رئیس‌جمهور ترامپ توانمندی‌های نظامی ایران را در هم شکسته، نزدیک به ۱۰۰ درصد کارخانه‌های نظامی آن را نابود کرده و برنامه هسته‌ای‌اش را مدفون کرده است. اکنون وارد مرحله نهایی می‌شویم. با سپیده‌دم، یک «D-Day اقتصادی» آغاز می‌شود — بزرگ‌ترین تهاجم مالی واحدی که تاکنون علیه یک دشمن بسیج شده است.
جمهوری اسلامی با جا زدن اخاذی به‌عنوان تضمین‌های امنیتی، به حیات خود ادامه داده است. این رژیم از محاسبه‌ای قدرت گرفته که در آن، تلافی ایران قطعی و اجرای اقدامات از سوی آمریکا قابل مذاکره تلقی می‌شود. تحت ریاست‌جمهوری ترامپ، آن دوران به پایان رسیده است. و کسانی که از خطر سرپیچی از تهران می‌ترسند، نباید هزینه آزمودن واشنگتن را دست‌کم بگیرند.
رئیس‌جمهور شرایطی را فراهم کرده است تا از هر نهاد، هر اختیار و هر اقدامی که بسیاری تصور می‌کردند هرگز به آن متوسل نخواهیم شد، استفاده شود. هدف ما قطع کردن هر شریان اقتصادی‌ای است که این رژیم استبدادی را سرپا نگه می‌دارد، تا زمانی که تهران تنها بماند.
SecScottBessent
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78010" target="_blank">📅 03:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78009">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، به کشورهایی که به روابط مالی و تجاری خود با جمهوری اسلامی ادامه می‌دهند هشدار داد که باید میان همکاری با تهران و حفظ دسترسی به ایالات متحده و نظام مالی جهانی یکی را انتخاب کنند.
اسکات بسنت، وزیر خزانه‌داری آمریکا با انتشار مقاله‌ای در روزنامه فایننشال تایمز تاکید کرد دولت ترامپ قصد دارد با قطع همه شریان‌های مالی و تجاری جمهوری اسلامی، تهران و کشورها و نهادهای همکار با آن را در انزوای کامل اقتصادی قرار دهد.
او که قرار است دوشنبه دوم شهریور در کنفرانسی مطبوعاتی جزییات اقدامات تازه دولت آمریکا علیه جمهوری اسلامی را اعلام کند، هشدار داده است که ادامه همکاری با حکومت ایران، دسترسی این کشورها به سرمایه و بازارهای جهانی را به خطر خواهد انداخت.
وزیر خزانه‌داری ایالات متحده از آغاز مرحله‌ای تازه و گسترده در فشار اقتصادی علیه جمهوری اسلامی خبر داده و آن را «روز سرنوشت‌ساز اقتصادی» و بزرگ‌ترین تهاجم مالی سازمان‌یافته علیه یک دشمن توصیف کرده است.
بسنت در این یادداشت با اشاره به کنفرانس تهران در سال ۱۹۴۳ نوشت رهبران متفقین در آن زمان در پی یافتن راهی برای وارد‌کردن «بیشترین فشار ممکن بر دشمن» بودند. به گفته او، تاریخ اکنون همان پرسش را بار دیگر پیش روی تهران قرار داده و زمان آن رسیده است که ایالات متحده با تمام توان به آن پاسخ دهد.
او تاکید کرد دونالد ترامپ، رییس‌جمهوری آمریکا، با استفاده از قدرت نظامی ایالات متحده بخش قابل‌توجهی از توانایی‌های نظامی حکومت ایران را از میان برده و برنامه هسته‌ای این کشور را تضعیف کرده است. بسنت افزود واشینگتن اکنون وارد «مرحله نهایی» شده و می‌خواهد فشار نظامی را با حمله‌ای گسترده به منابع مالی و تجاری جمهوری اسلامی تکمیل کند.
وزیر خزانه‌داری آمریکا در ادامه، جمهوری اسلامی را حکومتی خواند که طی ۴۷ سال گذشته هم در داخل ایران و هم در خارج از مرزهای آن نقشی مخرب داشته است. او گفت فساد و سیاست‌های حکومت، اقتصادی را که می‌توانست یکی از قدرتمندترین اقتصادهای جهان باشد به ویرانی کشانده و مردم مبتکر و کارآفرین ایران را با سرکوب روبه‌رو کرده است.
بسنت همچنین جمهوری اسلامی را متهم کرد که در خارج از ایران، شبکه‌ای از گروه‌های نیابتی را برای ادامه فعالیت‌های خشونت‌آمیز و تروریستی حفظ کرده است. او گفت ایالات متحده بهای سنگینی در رویارویی با این شبکه پرداخته، هرچند تنها کشوری نیست که با پیامدهای فعالیت‌های آن مواجه شده است.
به گفته وزیر خزانه‌داری آمریکا، با وجود گستردگی تهدیدهای ناشی از سیاست‌های تهران، واشینگتن در بسیاری از موارد در عزم خود برای مقابله با جمهوری اسلامی تنها مانده است.
بسنت کاهش شدید ارزش ریال و نرخ بالای تورم در ایران را نتیجه سیاست‌های دولت ترامپ دانست. او گفت اقتصاد ایران چنان تضعیف شده که ارزش پول ملی این کشور به پایین‌ترین سطح خود رسیده و تورم نیز به یکی از بالاترین سطوح تاریخی نزدیک شده است.
او یادآور شد آخرین امید جمهوری اسلامی، ادامه همکاری کشورهایی است که از روی ترس یا ملاحظات اقتصادی تصور می‌کنند سازش با تهران می‌تواند امنیت یا صلحی پایدار برای آنها به همراه آورد.
وزیر خزانه‌داری آمریکا بدون نام‌بردن از کشور مشخصی گفت برخی دولت‌ها و نهادهای خارجی همچنان نفت ایران را خریداری و حمل می‌کنند و انتقال منابع مالی این کشور را از طریق صرافی‌ها و مناطق آزاد تجاری تسهیل می‌کنند.
به گفته او، برخی کشورها همچنین به پروازهای ایران اجازه فعالیت می‌دهند، کشتی‌ها را به نمایندگی از تهران در دفاتر خود ثبت می‌کنند و بر انتقال سوخت میان کشتی‌ها در دریا و استفاده غیرقانونی از نظام بانکی‌شان چشم می‌بندند. بسنت این کشورها را متهم کرد که هم‌زمان می‌کوشند میزان همکاری خود با جمهوری اسلامی را پنهان کنند.
او گفت این کشورها بر اساس این محاسبه عمل می‌کنند که مماشات با تهران، در مقایسه با ایستادگی در برابر آن، گزینه‌ای امن‌تر است؛ اما باید پیامدهای کمک به بقای جمهوری اسلامی را نیز در نظر بگیرند.
بسنت برای توضیح این دوراهی به دیدگاه بلز پاسکال، فیلسوف فرانسوی قرن هفدهم، اشاره کرد. به گفته او، پاسکال معتقد بود عدم قطعیت، انسان‌ها یا ملت‌ها را از داوری معاف نمی‌کند، بلکه آنها را ملزم می‌کند خطرها را دقیق‌تر ارزیابی کنند؛ زیرا در چنین شرایطی بهای یک محاسبه اشتباه می‌تواند سنگین‌تر باشد.
وزیر خزانه‌داری آمریکا گفت «شرط‌بندی پاسکال» اکنون درباره شریان‌های حیاتی اقتصاد ایران مصداق پیدا کرده است. به گفته او، کشورهایی که برای در امان ماندن از واکنش تهران همچنان منابع مالی حکومت ایران را تامین می‌کنند، در عمل همان حکومتی را تقویت می‌کنند که از آن هراس دارند.
بسنت هشدار داد که این کشورها از مرز تحمل آمریکا عبور کرده‌اند و باید میان ادامه همکاری با جمهوری اسلامی و حفظ روابط اقتصادی خود با ایالات متحده و نظام مالی جهانی یکی را انتخاب کنند.
او گفت ترامپ در حال انجام کاری است که روسای‌جمهوری پیشین آمریکا از آن خودداری کردند: پایان‌دادن به تهدیدی که دولت‌های قبلی به مدیریت و مهار آن رضایت داده بودند.
به گفته بسنت، طبقه سیاسی آمریکا برای چند دهه چرخه‌ای بی‌پایان از اقدامات تحریک‌آمیز جمهوری اسلامی را پذیرفت، در حالی که باید منافع ایالات متحده را با قاطعیت بیشتری پیش می‌برد. او گفت نسل دیگری نباید زیر سایه تهدید نیروهایی زندگی کند که شعار «مرگ بر آمریکا» سر می‌دهند و در پی تحقق اهداف هسته‌ای جمهوری اسلامی هستند.
وزیر خزانه‌داری آمریکا استدلال کرد که انزوای کامل مالی تهران می‌تواند نیاز به استفاده مستقیم از نیروی نظامی ایالات متحده را کاهش دهد و هم‌زمان امنیت و آزادی عمل متحدان واشینگتن را افزایش دهد.
او همچنین برای کشورهایی که روابط مالی و تجاری خود را با ایران قطع کنند، مشوق‌هایی در نظر گرفت. بسنت گفت قطع همکاری با تهران می‌تواند دسترسی این کشورها به سرمایه جهانی را افزایش دهد، اعتماد به بازارهایشان را تقویت کند و جایگاه مورد نظر آنها را در اقتصاد بین‌المللی بهبود بخشد.
در مقابل، او هشدار داد کشورهایی که روابط خود را با تهران حفظ کنند، ممکن است مسیر دستیابی به رفاه پایدار را از دست بدهند. به گفته او، در کشورهایی که اعتماد سرمایه‌گذاران و بازارهای جهانی به آنها کاهش می‌یابد، فعالیت‌های مالی غیرقانونی معمولا گسترش پیدا می‌کند.
بسنت گفت هر کشوری که به‌عنوان شریان مالی یک حکومت رو به زوال عمل کند، باید انتظار داشته باشد در انزوای آن نیز سهیم شود. او افزود کشوری که به پناهگاهی برای فعالیت‌های تروریستی تبدیل شود، از دید ایالات متحده به بازیگری مطرود در جهان بدل خواهد شد.
وزیر خزانه‌داری آمریکا جمهوری اسلامی را متهم کرد که طی سال‌های گذشته، اخاذی را در قالب تضمین‌های امنیتی عرضه کرده و از ترس کشورهای دیگر نسبت به اقدامات تلافی‌جویانه تهران بهره برده است.
به گفته او، قدرت جمهوری اسلامی بر محاسبه‌ای استوار بوده که واکنش [حکومت] ایران را قطعی، اما اجرای تهدیدهای آمریکا را قابل‌مذاکره می‌دانسته است. بسنت گفت با بازگشت ترامپ به قدرت، این دوره به پایان رسیده و کشورهایی که از ایستادگی در برابر تهران هراس دارند، نباید هزینه آزمودن اراده واشینگتن را دست‌کم بگیرند.
او افزود ترامپ شرایطی فراهم کرده است که دولت آمریکا بتواند از همه نهادها، اختیارات قانونی و ابزارهایی استفاده کند که بسیاری تصور می‌کردند واشینگتن هرگز به آنها متوسل نخواهد شد.
بسنت هشدار داد هرگونه ارتباط باقی‌مانده با تهران می‌تواند انزوای اقتصادی کشورها و نهادهای مرتبط را تسریع کند؛ خواه این ارتباط آگاهانه ایجاد شده باشد و خواه دولت‌ها و شرکت‌ها عمدا آن را نادیده گرفته باشند.
وزیر خزانه‌داری آمریکا همچنین درباره احتمال واکنش نظامی جمهوری اسلامی هشدار داد. او گفت اگر هم‌زمان با تضعیف اقتصاد ایران و کاهش تسلط حکومت بر قدرت، تهران علیه نیروهای آمریکایی یا کشورهای همسایه در خلیج فارس اقدام نظامی انجام دهد، ترامپ «به‌سرعت و قاطعانه» پاسخ خواهد داد.
بسنت در پایان هدف دولت آمریکا را قطع همه شریان‌های اقتصادی توصیف کرد که به بقای جمهوری اسلامی کمک می‌کنند. او گفت فشارها تا زمانی ادامه خواهد یافت که تهران در انزوای کامل قرار گیرد.
او بار دیگر با اشاره به پاسکال، تصمیم کشورهای همکار با حکومت ایران را نوعی انتخاب درباره آینده آنها دانست و پرسید آیا این کشورها حاضرند در برابر موج تازه فشارهای آمریکا، آینده خود را به خطر بیندازند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78009" target="_blank">📅 03:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78008">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L8FqWCA73xJBZw_7MmtEMEZiAbqG0MCf_pQETRaIgMtxDEo_UVp0ybcvgj_H4WWaGvrxUqrhvEQ4MHaGaBcor2og4iD5sL5ypO088jQEBc9sO-qTMWqCrIjRlsHk4_WTBv6TjEIfC37uqgY3WdLiXU9wXxRnQw7RnH4R-Pv_Z0GEOydKnhkgW5RtZc6AkGkm4QoZMTB7df0VTdEvNr5Qz5vshkbzBmzh8HKEtUfFcsTm4gl-Sb5WKfGQjveH-nTmr_h_oOg9wXw3diky2nIRVwINtaFo5YwHQooOyzKnpH-8JiV_RLrBCNW55fznJ-hs19KCCZttU2viWCnf2X1ypA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهای دلار آمریکا در بازار آزاد ایران روز یک‌شنبه اول شهریور از مرز ۲۰۰ هزار تومان عبور کرد و رکورد تازه‌ای به جا گذاشت؛
همزمان پوند بریتانیا از ۲۷۲ هزار تومان گذشت و یورو نیز به محدوده ۲۳۴ هزار تومان نزدیک شد.
قیمت سکه امامی نیز از ۲۱۸ میلیون تومان فراتر رفت.
این جهش قیمت‌ها در ادامه روند کاهش ارزش ریال و همزمان با تشدید فشارهای سیاسی و اقتصادی بر جمهوری اسلامی رخ داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78008" target="_blank">📅 16:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78007">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F2JR50WkyQyBmpbKeP9_ipOaZWNydq-42dpK4InLE0hAqa2qmHeK9h0wobv0cl9QYPMp0ecNGnfaym1sKyilrnc1Cr3enLNAohyEXDiNLE6Pht6YdjuQIvLCcSC1ZsZqDoMUQWQuZWqfuy_Pv1_8WP-HbsmmYIU5iIw69E0nAOr0eVL9AYs7BFXDQTF27nZaQhR-oIk6QTKHic27QHCbdxC7epzWBB5r9kcib0jxhk9Tl3lsqvwgw9iGeyZkMNd74DsN8TBZGj4zB7J_KsR4EXhi3X3EaaGPhgiPa1oeWrdn43WU1g8lpCJmCWsmTKiXU7dmPSqK35_xruwDRtyhNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر رئیسیان، وکیل حسین شنبه‌زاده، از صدور حکم بدوی موکلش در پرونده‌ای جدید خبر داده است.
بر اساس این حکم، شنبه‌زاده به اتهام «نشر اکاذیب به قصد تشویش اذهان عمومی» به یک سال حبس تعزیری محکوم شده است.
رئیسیان در حساب کاربری خود در شبکه اجتماعی ایکس نوشته است که این پرونده مربوط به پیامی است که شنبه‌زاده از زندان و به مناسبت روز تولدش برای دوستانش فرستاده بود.
او با انتقاد از حکم صادرشده نوشته است: «فقط تصور کنید یک زندانی با استناد به "نحوه انتشار در رسانه معاند فضای مجازی" به حبس محکوم شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78007" target="_blank">📅 16:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78006">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CwEN1gL6uFkcHZp7LUEM8_EBxxa59YCfPBBZEKvf8wMidxfJ9DCluFv-_9oulHn7UYENSSHut9_FHqU_lmMLsVhZVdVPYMwWIKSkx8zCsAni8zKpKQxBkm7BeuTH1ahsSrph7-_JOfICcTg8pnFsdlZyoE2Fyx9YovEzML8KBU59Mve8ODWTsscuhl9yO-AA-ziT2JrG9_8xKlmkyx7MrGrRjxzarMIZllhDrMJqMDTzt1t0bWgy3GjARQMf6uNW1_57i1nFkAFlElfv-Uv_WWlCXu1l9gBpgOUanoegK4IvDysvoj9xXcX0D61x2BQAkkOOnbvEdsCTkUq6jwgAZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی از اجرای حکم اعدام «مجید آدینه»، یکی دیگر از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در کرج، خبر داده است.
براساس گزارش تسنیم به نقل از قوه قضاییه، این حکم صبح یکشنبه اول شهریور ۱۴۰۵ اجرا شد.
مجید آدینه روز ۱۹ دی‌ماه ۱۴۰۴ در محدوده محمدشهر کرج بازداشت شده بود.
مقام‌های قضایی مدعی شده‌اند که هنگام بازداشت او یک قبضه کلت کمری، سه خشاب، ۳۰ فشنگ، دو شوکر برقی، دو افشانه گاز اشک‌آور، یک اره برقی شارژی و یک بطری بنزین همراه داشته.
قوه قضائیه اعتراضات دی‌ماه را مطابق روایت رسمی جمهوری اسلامی «کودتا» خوانده و آدینه را به همکاری با آمریکا، اسرائیل و آنچه «گروه‌های متخاصم» نامیده، متهم کرده است.
دادگاه انقلاب کرج او را با اتهام «محاربه از طریق تحریق عمدی» و براساس قانون موسوم به «تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی و کشورهای متخاصم» به اعدام و مصادره اموال محکوم کرده بود.
اطلاعاتی درباره دسترسی آدینه به وکیل انتخابی، روند دادرسی، زمان برگزاری دادگاه و نحوه اخذ اظهارات او منتشر نشده است.
اعدام مجید آدینه در ادامه اجرای احکام اعدام علیه بازداشت‌شدگان اعتراضات دی‌ماه انجام شده است. بیش از ۳۰ کشور روز ۲۱ مرداد ۱۴۰۵ با انتشار بیانیه‌ای مشترک، ادامه صدور و اجرای احکام اعدام برای معترضان ایرانی را ابزاری برای «ساکت‌کردن صدای مخالفان» خواندند و محکوم کردند.
عفو بین‌الملل نیز گزارش داده است که جمهوری اسلامی در سال ۲۰۲۵ دست‌کم دو هزار و ۱۵۹ نفر را اعدام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78006" target="_blank">📅 16:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78005">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4d23144315.mp4?token=c2EKIxdY9hC62p_tc8wb-x9XtIqOShZetsu6cGLqUDb8TDgD4EK_GaOBtMxU0o7mmN7_LFN1MVB0JqwegMtqmaJU8OeBmifWwQM_zx7bZOv8m9JP_LVeq8FM_15VxrTz7Vw1bonY1UJ4SFoUczwKrqsVihMjDvjJr8OaXyVhv0jdGiyS7BDWOIyl0wUq-whXW3NrvmygVSj_qt9Hv-ytFU6-0MovLYQtt9MzqE3_VbzKH-URAl1fiNC3-tkQZKxMdbUrLdEl_pP4lB4Xq1n-OqLhjxWYFvqML-JZnQfnO11RI4GMWwIM_jLQn47pOPUyTvIPBXy3ryDZ0GMxSi5uaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4d23144315.mp4?token=c2EKIxdY9hC62p_tc8wb-x9XtIqOShZetsu6cGLqUDb8TDgD4EK_GaOBtMxU0o7mmN7_LFN1MVB0JqwegMtqmaJU8OeBmifWwQM_zx7bZOv8m9JP_LVeq8FM_15VxrTz7Vw1bonY1UJ4SFoUczwKrqsVihMjDvjJr8OaXyVhv0jdGiyS7BDWOIyl0wUq-whXW3NrvmygVSj_qt9Hv-ytFU6-0MovLYQtt9MzqE3_VbzKH-URAl1fiNC3-tkQZKxMdbUrLdEl_pP4lB4Xq1n-OqLhjxWYFvqML-JZnQfnO11RI4GMWwIM_jLQn47pOPUyTvIPBXy3ryDZ0GMxSi5uaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی، می‌گوید از نظر حکومت ایران هر کشوری که با آمریکا در ایجاد محدودیت اقتصادی بیشتر علیه ایران مشارکت کند، «دشمن» تلقی می‌شود و تهدید کرد در چنین صورتی این کشورها هدف حمله قرار خواهند گرفت.
محسن رضایی در یک گفت‌وگو تلویزیونی که شامگاه شنبه ۳۱ مرداد از صداوسیما پخش شد، همچنین تهدید کرد اگر طرح جدید آمریکا علیه ایران برای ایجاد محدودیت اقتصادی بیشتر اعمال شود، جمهوری اسلامی اجازه نخواهد داد «یک قطره نفت نه تنها از تنگه هرمز که از کل خلیج فارس» خارج شود.
این اظهارات تازه‌ترین واکنش مقامات تهران به تحریم‌هایی است که دولت آمریکا قرار است روز دوشنبه آتی جزئیات آن را اعلام کند و اسکات بسنت، وزیر خزانه‌داری آمریکا، پیشاپیش آن را «سخت‌ترین تحریم‌های تاریخ» علیه ایران خوانده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78005" target="_blank">📅 04:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78004">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NWo7nDjjt9PV4xkvxi2rXryEl4wglJbPbeDyrJ8gUHt29Nv3-fns-6_p-cwgwh_2vGDyTPf8p3C6d9-non45izwXqBaUkPryVNL0nM_o2o-ZDRtaYQ4zPAIDvAH14tmGUZSjC2cEJEojMjO6huxalf1w9D2irDbJ5VjTIceiFJtK6k8DdI4fmQx9DqYe2F6YHQRNBxNZPhErVZQocASSw70k02Hb1_y4kWu6hJpTCtTWozHbozEaArAZDtKVMBjUwjF5pRsCWYI4u4ie0WJK7LaLfrJU4j-p2nGtLKu4GywIm6HFz5ldkbuoyl2Pz41YW8tkzEjiTAimN1y6bHuj-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، با انتشار پستی در شبکه اجتماعی تروت‌سوشال بر عبور کشتی‌ها از تنگه هرمز با اسکورت نیروهای‌ آمریکایی تاکید کرد. ترامپ مطلبی از مارک تیسین، مفسر آمریکایی را بازنشر کرد که در آن، تیسین به آمار خروج بیش از ۱۰۰۰ کشتی از تنگه هرمز با اسکورت نیروهای آمریکایی اشاره دارد.
@
VahidHeadline
دونالد ترامپ، رییس‌جمهوری آمریکا، بار دیگر تصویری از نقشه تنگه هرمز را در تروت سوشال منتشر کرد که در بالای آن عبارت «قلمرو جدید آمریکا» دیده می‌شود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78004" target="_blank">📅 02:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78003">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BNIdKRacZmim-DsFi-8sqlyJu5uRR48SquK_osiiZfE54t9xGsktumrfMBO5xTAhr9kJtRB-CpuXN5mjZ1KtAJs-oWYc4SjZFgb_LT3gJpnRHTUZqfsGSLtOBTQTpMAofp-7C-YXpRkkOXUFIbkJTQm2rlHSktG7JHYyckeKpBPQwdwp8lgLVU3DaRojaT6nMQxg0uoTmAdbzcsHdbgZKlW9Bqvavp8eZv6QjAtumRMlKIKF905G45qRsaT2OGMnLDi38-0ZxTk266qbHzKN3gaLqZ6VvrEBCScIhpUwezX8CBZr6MVcIJRACw7g-8n7ZJ1T-i9ITxyODx8KnGj_Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باراک راوید، خبرنگار وبسایت اکسیوس، روز شنبه ۳۱ مرداد ۱۴۰۵ در شبکه ایکس به نقل از سه مقام آمریکایی گزارش داد که حدود ۴۰ نفتکش شامگاه جمعه از مسیر عمیق جنوبی تنگه هرمز وارد یا خارج شده‌اند و حدود ۱۶ میلیون بشکه نفت از این مسیر به خارج از تنگه منتقل شده است.
همزمان، رسانه‌های دولتی ایران مدعی شدند، تهران پس از درخواست‌های مکرر بغداد، به شماری از نفتکش‌های عراقی اجازه عبور از تنگه هرمز را داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/78003" target="_blank">📅 18:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78002">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fZ3ByTTreHQiXMZKl9qXw5js9AJyQcMkd6UPZ3kUbUn3HczSCd5CpNsKGmc5LT6EoVN7NCBDCHNhI3nLIvLGPcKoHG3rnxL9embYW79M-Kr9BhISy3rF3s3OJoeBCJr9_OQ-LemQ8HZoP6UT2kDSurc85OMEurdFkPNMHt33xCvyObQ4Scg9K-NxUb8S-f_RlfyI0CvNx6Ka3uyVFOUsZHDouXWR529x3bcQf-M6Keo9wNPvBmujlBazt5HdjVkylGiABiRjrm_k9eZSJzaYVAAQ6VUiEiOVPONlGfw3RsPgInwsWT1T-dBsUvDmgwZbIYnMdfhYW-PQsWwRg8TbHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی، فرمانده کل سپاه پاسداران، در پیامی به پیمان جبلی، رییس سازمان صدا و سیما، ضمن حمایت از رویکرد این سازمان، نوشت که صدا و سیما در دوره جنگ اخیر، «در ثبت و ماندگار ساختن این حماسه، سهمی ارزشمند در تقویت جبهه رسانه‌ای انقلاب اسلامی بر عهده گرفت.»
وحیدی همچنین عملکرد صدا و سیما را «مجاهدت ارزشمند و نقش‌آفرینی موثر» توصیف کرد.
این در حالی است که در روزهای اخیر، محمدباقر قالیباف و مسعود پزشکیان صراحتا از عملکرد صدا و سیما انتقاد کرده بودند.
محمدباقر قالیباف ۲۷ مردادماه گفته بود که صدا و سیما در زمینه «جنگ شناختی» تاکنون موفقیت‌های لازم را نداشته است. رییس مجلس همچنین گفته بود: «تبیین ناکارآمدی‌های ساختاری، رویکردی و عملکردی صدا و سیما فرصتی مبسوط می‌طلبد.»
مسعود پزشکیان نیز در چند نوبت از عملکرد این سازمان انتقاد کرده است. پزشکیان ۱۰ خردادماه گفته بود روایت‌های صدا و سیما از شرایط کشور غیرواقعی است و این رسانه نیازمند بازنگری جدی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78002" target="_blank">📅 17:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78001">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PUuwHY4IHrJZSmupDe1kQhlBzykeRDc0S8Z98CoOdJDgzW-D9Hp85Nv8TfFvYROXsP5Fw-rQhxNsB8SpWWM1a9TX8jTSsOWn8Sb263W_RZmpZ9ELGP_BZP8ZDVTIZX2CvNBAMJzQAb4u6WRVb3-oem3HCnXci9Zbq_rg4xtjlZZcd2UTslPA_yJMcJGSXG6M0MmnnvZ586eWBrVPUC7QEQYv2lLQLp1wW0ZLq945odkpFD83qMYwS9YW4YU3ntGxOtFh9Qgg7MraY9HcXoqJS76kL6Le4WPLHh0MYEMUPOkG2AK1UGPvffQUED9onbO5NgycrZe9L81l9EW-4nNYoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول رییس دولت در ایران، با تاکید بر ضرورت آنچه «اصلاح الگوی مصرف انرژی» خواند، گفت: «باید مردم را توجیه کنیم تا بدانند که اکنون بخشی از درآمدهای کشور صرف تامین بنزین می‌شود و این موضوع هزینه و فشارهایی را به بخش‌های دیگر تحمیل می‌کند.»
isna.ir
عارف شنبه ۳۱ مرداد در «همایش ملی صنعت، معدن و خدمات سبز» با اشاره به تفاوت مصرف سوخت میان گروه‌های درآمدی گفت میزان مصرف دهک دهم، ثروتمندترین دهک جامعه، حدود ۲۳ تا ۲۴ برابر دهک اول است.
عارف در ادامه، مخالفت با گران شدن بنزین را به واکنش اقشار کم‌درآمد به تغییر سیاست‌های مرتبط با مصرف انرژی مرتبط دانست و گفت: «وقتی قرار است اصلاحی در این زمینه انجام شود، اتفاقا بخش‌هایی از اقشار آسیب‌پذیر و کسانی که به هر حال در زندگی با مشکلاتی روبه‌رو هستند، تحریک می‌شوند که بگویند بنزین نباید گران شود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/78001" target="_blank">📅 17:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78000">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GJltFmnTg2BjvOuyJ-bLvfLCDh4dx4T2DlqRED0CrNNrnbh0T7RD_1FHHj3MnpaMmzxfDnFVU9l9xqiE-nJuK-29CuoC6ktARAqLBazM1XCgBZkBHdG90DJDdNmqi3fIYkY8qQT1-kfqafjTU9JsdIu-K5QRX5g7yfxGAkvi-SqX7sDR9RHqeVjBpaDbKgDPJ0rpfUNRHLSJkK58m0xmeStU8-J2KIur8z9aRQB-oOG_sSjuqj3S0B5nYj6nGKf8eywCR46zJxWZvnc61Mxm9wPXLbQu-NFAkLmHBp5t9O_mQYWFU4URPqutU9UGP09KrPjcF9263UD8CGr-zxbNSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فرزانه فصیحی»، دونده المپیکی ایران، گفته است پس از اعتراض به کشتار معترضان در دی‌ماه ۱۴۰۴ تهدید شده و مسئولان مانع حضور او در مسابقات قهرمانی جهان شده‌اند.
فصیحی در
صفحه اینستاگرام
خود نوشت که در این مدت بارها به او هشدار داده‌اند: «مراقب رفتارت باش، می‌دانی که قهرمانی جهان و بازی‌های آسیایی در پیش است.»
او در ادامه نوشت: «همان شد. قهرمانی جهان را که بزرگ‌ترین رویا و آرزوی هر ورزشکاری است، از من گرفتند؛ بازی‌های آسیایی را هم خودم تقدیم‌تان می‌کنم.»
این دونده ایرانی گفته است تنها ورزشکار ایران بوده که سهمیه حضور در مسابقات جهانی را به دست آورده و فصل را در جایگاه نخست رده‌بندی آسیا به پایان رسانده، اما مسئولان از ثبت‌نام او در این رقابت‌ها خودداری کرده‌اند.
فصیحی درباره سکوت خود در ماه‌های گذشته نوشت: «صدها بار نوشتم و پاک کردم. هیچ جمله‌ای نمی‌توانست عمق ظلم، بی‌عدالتی و خیانتی را که در حق من شد، توصیف کند.»
او بدون اشاره به هویت افراد یا نهادهایی که تهدیدش کرده‌اند، گفته است پیگیری حقوق خود را از مسیرهای قانونی آغاز کرده و اجازه نخواهد داد حقش «به‌عنوان یک ورزشکار زن ایرانی» پایمال شود.
این ورزشکار در پایان نوشت: «من همچنان می‌دوم؛ برای مردمم، برای رویاهایم.» او همچنین ابراز امیدواری کرد که «عدالت جای ظلم، شایستگی جای رانت و پاکی جای فساد را بگیرد.»
فرزانه فصیحی پیش‌تر در بهمن‌ماه ۱۴۰۴ و پس از سرکوب اعتراضات سراسری دی‌ماه، با انتشار متنی در اینستاگرام از خشم و اندوه خود نسبت به کشته‌شدن معترضان نوشته بود.
فصیحی از چهره‌های مطرح دوومیدانی زنان ایران و دارنده رکورد دوی ۶۰ متر داخل سالن ایران است. او در بازی‌های المپیک توکیو و پاریس نیز حضور داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/78000" target="_blank">📅 17:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77999">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mZ03wapC5IXQM8d2AP3aWb_mvXwB0Y8fkoBrxgfTww_YKimErvB9fTRvnNG7vvYmSgPz1S304QYlxbVp01viSisEpTD5CcrYsqQPjdPj-4R6Dvage_koy_uq43UAD0TRtJFcmNQT44zTmge0cXy8esjdWMhJ1Y5-yhK6QgFhX5vVFfoUmJYyuvxOEvouvJrZD0lEEO8eASl3SuLzDDzHXJauC15pPLA5GJ3BRv2ZkdFyIdIHOhenwxCqBU6y2UIzB1ej59HaUf7kI19zch079SMyfX0X4-XawF1GpolInmCVBjGieaslZZtnvfon5eBywduEwvhkxBCILQVAJXBEAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف در شبکه اجتماعی «ایکس»، بدون نام بردن از کشوری نوشت: «پیام‌های متعددی از کشورهای همسایه درباره شکل‌دهی به ترتیبات امنیتی جدید و همکاری‌های اقتصادی در منطقه دریافت کرده‌ایم.»
او مدعی شد آمریکا با «قلدری» و نادیده گرفتن منافع متحدان خود به سود اسرائیل، امنیت آنها را به خطر انداخته است و افزود یک «نظم بومی و مستقل» می‌تواند صلح و امنیت واقعی را برای منطقه به همراه بیاورد. رسانه‌های حکومتی ایران این اظهارات را واکنشی به تهدیدهای دولت دونالد ترامپ علیه کشورهایی دانسته‌اند که به همکاری اقتصادی با تهران ادامه می‌دهند.
اظهارات قالیباف در شرایطی مطرح می‌شود که روابط جمهوری اسلامی با برخی کشورهای عربی خلیج فارس در روزهای اخیر با تنش‌های تازه‌ای روبه‌رو شده است.
علی عبداللهی، رییس ستاد کل نیروهای مسلح جمهوری اسلامی، روز چهارشنبه به کشورهای حاشیه جنوبی خلیج فارس درباره «هرگونه کمک یا تسهیل» برای نیروهای آمریکایی هشدار داده بود.
عبداللهی گفت جمهوری اسلامی فعالیت هواپیماهای نظامی آمریکا، از جمله هواپیماهای سوخت‌رسان مستقر در پایگاه‌های منطقه را زیر نظر دارد و هرگونه کمک به ارتش آمریکا را به منزله مشارکت در عملیات نظامی این کشور تلقی خواهد کرد. او خطاب به کشورهای منطقه گفت: «هیچ‌چیز از دید ما پنهان نیست.» کشورهای عربی منطقه پیش‌تر مشارکت در حملات آمریکا به ایران یا اجازه استفاده از خاک خود برای این حملات را رد کرده‌اند.
همزمان، امارات متحده عربی تمام فعالیت‌ها و مبادلات تجاری و تراکنش‌های مالی خود با ایران را تا اطلاع ثانوی متوقف کرده است؛ اقدامی که برای جمهوری اسلامی، با توجه به نقش امارات به‌عنوان یکی از مهم‌ترین شرکای تجاری ایران، اهمیت ویژه‌ای دارد.
این تصمیم پس از آن اعلام شد که مقام‌های اماراتی گفتند دو موشک بالستیک شلیک‌شده از ایران را شناسایی کرده‌اند. بر اساس اعلام ابوظبی، یکی از موشک‌ها خارج از آب‌های سرزمینی امارات و دیگری در داخل این محدوده به دریا سقوط کرده است. تهران این اتهام را رد کرده است.
ادعای قالیباف درباره درخواست کشورهای همسایه برای ایجاد ترتیبات امنیتی تازه در حالی مطرح شده که او نام این کشورها، محتوای پیام‌های ادعایی یا جزییات طرح مورد نظر تهران برای «نظم بومی و مستقل» را اعلام نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/77999" target="_blank">📅 17:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77998">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ovMzdE4yj8nNmxWPyNkNRbQmEfVauIsKXXDoKUaW8-WwOV5-rGd-0Mx0gEBCNXtfnHHKUz4jEsJ9Y1c60-ghctiL2HNcUo7UdGzOQ0ayx5jR_RmaIjYjkecwzdGngJXnWcaBtHY-GhTiHDIs1VjxihAxzDuJHnEKMKTM8AaswZECtCGDeIPHJBCczBPfw-FDOgp8xKoJPPk1I41wlToCHGFDW_JZghFJKqSMCl_Hr-BwwS1ANmBzz9O3Mfo4OhzkYEFkoGV1CSJulJEPdw1F7BJXTBiiFBSXOoozj-d9EhfjxotsMap1whMxm-m2Pe2fdiApaoUenB_PeZnh8kHZcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«آرزو کشور» مالک و مدیر یک سالن زیبایی در اصفهان به اتهام «ارتباط با دول متخاصم» به ۱۲سال حبس محکوم شده است.
آرزو کشور از بهمن‌ماه سال گذشته، در زندان «دولت‌آباد» اصفهان نگهداری می‌شود.
آرزو کشور پس از بازداشت در بهمن‌ماه گذشته، در سلول انفرادی نگهداری شده و تحت بازجویی‌های طولانی قرار داشته است. مواردی که به‌تنهایی مصادیق «شکنجه» محسوب می‌شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/77998" target="_blank">📅 17:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77993">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b0gL5OxGTaJA1QHfzi3xuR2pz_IogebrIg_61j0-bUpXoQFU-d4kOkrCIwdkZ644LKlHLuCCSUxlbmahNYvPYcG-0yUOBHl3raptAZ307Wsn7zTGqswBt8J05tf6mZIqYuexESKZscstS_PvsCIuVdwRdPp7rT_jQRepCrF5mYbE4Je4EDnXnUYUjVE-ZVM4N-02py4Im0IloRsbTfrpMQfoMKYOQdK1b3e9Ni_UfVnbQ3uLi_ieKayQJF-IRqlEtXbiR6TNiVS-JbKNfRKoaogbpVVSPWC-BgnsTow81-98Z5FX0E-VrJYNZGUh_5-idN2YXFRNIHIcuLOnYBeb7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FsF0KdnEADd7fJPJHop-wJgh_25K33TXieSgZdSWncnAueNcrYQA31aCjJ1y3cFPRxp8M9toKieWFmz52RzrCc-xbGReJYYtTOFrUepwfgmj0BXdwi2eu8AiuwgHy6D4K7s_jlLfWwgzZhx1PRWys55mY6D_jxR-8heMX-UqyFtmuknmSsblwxvSw2js1VCg2f15aBcqp1c6sG2zmqJya-2uyOqPykMB0BBvnnuaKFYQuOVPWScXrlPyp7oW62tu6waP2_dZAzlsyVFRffuH1pZBbsiaN5NyyeOTOrI8e9LZMJc7kWAPrkPCcNiBijP2MW2hSeMF4_G3Q2S6iVhROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FTFvO8TA_ZObGI4nnbG_kcaxZTjjMr5oazyBCqkqbZP_1ZMgHREw6uo50SYDLZJ4f9NkKPrS1AVeWHPI37jhXAu4b-K86v-JqVjSerFkgR2_zOywbiCEndv5TFwT5YAso5NZzEDfK5L5SDvRIS4VN4jcfc6Q5tt1y6Wdt_cSU593Tz5mrp78AIJ5rrTBU791S41jo7bQXtZ1HVhi2c3BBlyu5Q-20yl9HCWqugl3sxsgplAntMFGg3lD43zp36z0bqlPU1LJbH8zd9xE-HJbAlf2vKcjx8PcwOcJ9ELYqUIldSPgUF-rqkKIVSyyHqx7qhjDIfWr4adV7R_Ke75sGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u4hpgAV2gotWTD4QYQhmE3m0GMKwJX2Q4kcoNZWojKghq9NUgCDdRoUSKA-ktdMYt7iwWl8WFdnh4eyoaO0Wy2FotIiNB3wwsSYQIH-vU-6f4JxWEMWxF2m1fWcpcEurEMyOqYnPBJHVDZNB5NVH_xzPY9bhauYAK1gl7Hkez07zhgcz4tD2U5KR0AsXJi9sib7ZRvE52F-TMZYeoDRCWnbQkTcLWWfCq7ZcqFbZD1h6WPPOQ9PxjKb4i-tdA41528GytbtGV9HDXjnV3tP4WCkC_yEwgWUwn27h_IRiYqq2la7MAAk_P3aqjmTMY0I-EKevVY9J_4oYjGj-OMuTsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0b28f575c7.mp4?token=MKKJELlPAooeZW1YV6RKaQUhdzq5ZD5dos45nZjuK4c_bZMwfCyI5xpWGZo-ixHdaYrGbm3y6EwAZLD9_qly-Csf8QGP7ks_xsnK-zOnAxBnlR7p07D_q9ITsR1WtQiAhdS0ikqlvK1PR8mue74SXhLpVgb3QOXh9kRDNstR9GsQI6hF4DfmoKEJ4ccPsHh5_6OnTpAtvHs3uFMx-auCRe9a8DIvy8leI5SgQL3ooX_xE7vXEaLLxT6yBpEz2LWrsDsp1xL-a40VenKfey6muWp0ZChJPe4IYT76voGKpl66nM5QQkLPZWn2PCOhV1gxEQLufXh9tib3IhN9cwJypg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0b28f575c7.mp4?token=MKKJELlPAooeZW1YV6RKaQUhdzq5ZD5dos45nZjuK4c_bZMwfCyI5xpWGZo-ixHdaYrGbm3y6EwAZLD9_qly-Csf8QGP7ks_xsnK-zOnAxBnlR7p07D_q9ITsR1WtQiAhdS0ikqlvK1PR8mue74SXhLpVgb3QOXh9kRDNstR9GsQI6hF4DfmoKEJ4ccPsHh5_6OnTpAtvHs3uFMx-auCRe9a8DIvy8leI5SgQL3ooX_xE7vXEaLLxT6yBpEz2LWrsDsp1xL-a40VenKfey6muWp0ZChJPe4IYT76voGKpl66nM5QQkLPZWn2PCOhV1gxEQLufXh9tib3IhN9cwJypg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌های مرتبط با ایران در سخنرانی دونالد ترامپ در ایالت کارولینای جنوبی، جایی که رقابت‌ها برای کرسی سنای آمریکا در جریان است، با تشخیص و ترجمه ماشین:
🔻
و به‌محض اینکه کارمان با جمهوری اسلامی ایران تمام شود، قیمت نفت پایین‌تر از چیزی خواهد بود که حتی همین مدت کوتاه پیش بود.
🔻
اما با وجود همه این خبرهای خوب، گفتم از گفتن این خوشم نمی‌آید، اما باید کمی مسیرمان را عوض کنیم و برویم سراغ جمهوری اسلامی ایران و باید ماجرای سلاح هسته‌ای را جمع کنیم، چون آن‌ها دارند به سلاح هسته‌ای می‌رسند و ما نمی‌توانیم اجازه بدهیم سلاح هسته‌ای داشته باشند.
نمی‌توانیم اجازه بدهیم ایران سلاح هسته‌ای داشته باشد؛ خب، چیزهای بسیار بدی خواهید دید. پس رفتیم آنجا و جلویشان را گرفتیم. آن‌ها هرگز سلاح هسته‌ای نخواهند داشت.
آن‌ها به‌شدت می‌خواهند توافق کنند. ما حتی نمی‌دانیم خودمان می‌خواهیم یا نه، چون من در حال حاضر تنگه هرمز را قلمرو آمریکا می‌دانم. این قلمرو آمریکاست.
🔻
در مورد ایران هم به همان اندازه [ونزوئلا] خوب عمل می‌کنیم. رسانه‌های جعلی فقط نمی‌خواهند آن را این‌طور گزارش کنند، اما حالا دارند کم‌کم می‌پذیرند، چون چیز زیادی برای گفتن ندارند.
وقتی کشوری دیگر نیروی دریایی، نیروی هوایی، رادار، تجهیزات فنی یا تولید ندارد، رهبرانش هم دیگر نیستند. دسته دوم رهبرانش هم دیگر نیستند.
بخش‌هایی از دسته سوم رهبرانش هم دیگر نیستند. در واقع، این یکی از بزرگ‌ترین مشکلات من است. نمی‌دانم اصلاً باید با چه کسی طرف شوم. این یک مشکل است.
تنها کشور دنیاست که هیچ‌کس نمی‌خواهد رئیس‌جمهورش باشد.  می‌گویند: «چه کسی می‌خواهد رئیس‌جمهور شود؟» «نه، نه، من نمی‌خواهم رئیس‌جمهور شوم.» پس کمی مشکل است.
🔻
او [لیندزی گراهام]  واقعاً دغدغه‌اش این بود که کشورهای خارجی به کشور ما آسیب نزنند. دغدغه‌اش این بود که ایران سلاح هسته‌ای نداشته باشد. خیلی شدید روی این موضوع حساس بود. ببینید، اگر چنین اتفاقی می‌افتاد، اگر آن‌ها به آن دست پیدا می‌کردند، از آن استفاده می‌کردند. اسرائیل را فوراً نابود می‌کردند. خاورمیانه را نابود می‌کردند. و فکر نمی‌کنید سراغ اینجا هم می‌آمدند؟ می‌گفتید: «شهر بعدی کدام است؟» ما اجازه نمی‌دهیم چنین اتفاقی بیفتد. ما قبلاً... آن بمب‌افکن‌های B-2 را داشتیم؛ یک سال پیش، آن‌ها به آن امید پایان دادند.
🔻
ببینید، جمعه‌شب است. وقت زیاد داریم، درست است؟ اصلاً چه کار دیگری دارم بکنم؟ برگردم، ایران را یک کم بیشتر بمباران کنم؟ دیگه چه؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77993" target="_blank">📅 05:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77992">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/edb3c61b37.mp4?token=bxI8RyvkcgYzqrAmhu8HzCDEZDbw6Gj7JbIrz7zNTTcGU1cwAGYS95gyh4YT8nwwhNQj0OjkxFkVhjYzA1r7LtmfM7A48ZYHY9vUtyyPKt4QbPIickhfL6WgcK40rgOeWlatE0Kyt85rYSJvNfnDt-y6Q2qJ3XHNPZElsOfivj2cCdfYZnDjTvLloPqE2V7cop_3GIKSt3JJTl835GuP7XXfUd275e-bMsiLviAmHtigJY92hbPfhDSRCZQ-kJJpsZEGQdwzNrAUoF6Q1QAdmi1nlyoEV7IsFZbJoJSQzo_dyn1BJGwS35L9do5eljb3K_pGuErLXnI5-QZ6aXAKWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/edb3c61b37.mp4?token=bxI8RyvkcgYzqrAmhu8HzCDEZDbw6Gj7JbIrz7zNTTcGU1cwAGYS95gyh4YT8nwwhNQj0OjkxFkVhjYzA1r7LtmfM7A48ZYHY9vUtyyPKt4QbPIickhfL6WgcK40rgOeWlatE0Kyt85rYSJvNfnDt-y6Q2qJ3XHNPZElsOfivj2cCdfYZnDjTvLloPqE2V7cop_3GIKSt3JJTl835GuP7XXfUd275e-bMsiLviAmHtigJY92hbPfhDSRCZQ-kJJpsZEGQdwzNrAUoF6Q1QAdmi1nlyoEV7IsFZbJoJSQzo_dyn1BJGwS35L9do5eljb3K_pGuErLXnI5-QZ6aXAKWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
خبرنگار: آیا حرکت به سمت جنگ اقتصادی علیه ایران نشان می‌دهد که گزینه‌های نظامی آمریکا در منطقه محدود است؟
🔻
ترامپ: نه، اصلاً. فقط یعنی اینکه داریم می‌بینیم چه اتفاقی می‌افتد. آن‌ها هیچ پولی ندارند. نیروی دریایی ندارند. نیروی هوایی ندارند. به سربازانشان حقوق نمی‌دهند. به پلیسشان حقوق نمی‌دهند. تورمشان ۳۵۰ درصد است. بنابراین فقط می‌خواهیم تا حدی ببینیم چه اتفاقی می‌افتد.
و همان‌طور که می‌دانید، کنترل کامل داریم. اگر به محاصره نگاه کنید، کنترل کامل آن را در اختیار داریم. تمام آن منطقه‌ای که مربوط به تنگه هرمز است، و این یعنی تا عمق آن، مناطق خشکی را هم.
پس آن‌ها خیلی دوست دارند توافق کنند، اما از نظر من هنوز آماده نیستند که توافق درست را انجام دهند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/77992" target="_blank">📅 01:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77991">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بنا بر پیام‌های دریافتی حوالی یوسف‌آباد و امیرآباد و فاطمی و... صدای شلیک پدافند شنیده شده.
ساعت ۲۳:۰۸
🔄
پیام‌ها همچنان ادامه دارند.
کسانی هم معتقدند تیراندازیه ولی خیلی‌ها هم پیام دادند که صدای آتش‌بازی و ترقه‌بازی این وقت شب در کشور جنگ‌زده مربوط به یک مناسبت تازه‌ساز و "عید" جدیده!
دو روز پیش:
اجتماع "عید بیعت با امام زمان(عج) " برگزار می‌شود
به گزارش ایسنا، این مراسم با هدف تجدید پیمان با امام زمان(عج) و همچنین تجدید بیعت با مقام معظم رهبری، حضرت آیت‌الله سید مجتبی خامنه‌ای، از ساعت ۲۰:۳۰ تا ۲۳:۰۰ در میدان ولیعصر(عج) تهران برگزار می‌شود.
در این اجتماع علی‌اکبر رائفی‌پور و شیخ اسماعیل رمضانی به ایراد سخنرانی خواهند پرداخت. "
isna
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/77991" target="_blank">📅 23:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77989">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j0ZfZpS5_RA0syj-mxw-J_gh2GJ26BYDCq3iItdNrExyqF-R3OmlxOe_esluKJiwWJjrtWUinVkCgJbeRsxAqBF9JcIxOX53_qHvvA1-yjNeJ_V0wIe02vZA-7D0CMBB7FSLrfHVIxIOAvJBgAAadRi5aO4Ko8ZAO2LHoFBGFp5eEkYwPTyivKnG06n_9fenKVtwXxKj7QA8M8ZGJL8ThzwXyf5qHhUKf9aszHVvc8bkUG__aDlc9rOXc2DDSPeVP7_V_i7BttvaCgbwvYE_SziobGuFWsdl-T-ahmfUeMquEMZyHUlNKK-S-QmqLQ_yJRgL-u8_5w9TvolNrY-2LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر عکس من در آوتار اینجا جزو تبلیغ بود کلاهبرداری خطرناک‌تریه.
این تبلیغات به خود تلگرام سفارش داده میشن و کانال‌ها امکان جلوگیری از نمایش اون‌ها رو ندارند.
هر روز صدها نفر برای اولین بار با این تبلیغات مواجه میشن و به درستی احساس مسئولیت می‌کنند که باید این چیز خطرناک رو اطلاع بدن.
هر روز خیلی‌ها هم لطف می‌کنند و راهکارهای مختلفی مثل درخواست برای ریپورت کردن تبلیغات و بوست کردن کانال و حتی سفارش تبلیغ برای خودم و... رو پیشنهاد می‌کنند.
یک مشکل بزرگ الان حجم پیام‌هاییه که درباره این موضوع دریافت می‌کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/77989" target="_blank">📅 20:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77988">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VN5usRpgKygcAZPDrqijS4_K15c1Y-aLJQjNPDezVG0UnQ36vCUoHiH7n8sspNaU_YwozYH8mdpkfb6XIVy13lF6bICOW-JhQJb1d5S403jnclMe9wVz_SPyTRuU41nN3dK0qVMg3piVjA5-955l7eTQ1FhgSQSBBOn8s2gNlgEti0PmkBvuce4qbCKj2NxavvdhiL6b9j4ZS9XhwnyzVs74TR5-SikAS0Xk31nT8byYRU-Hx6xDMPMNuC6FwLVPn49j0sE2T3HyaaliZGsHm03s7aAsJiK4O5m4svOvKXcF0ImJaKFq-gfJP-u81vxNRTrk36SAPvLOksOASmjLOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«هرانا» روز جمعه ۳۰مرداد۱۴۰۵ خبر داد که دیوان عالی کشور، حکم اعدام «ارغوان فلاحی»، زندانی سیاسی ۲۴ساله محبوس در زندان اوین، را تایید کرده است.
حکم اعدام برای این زن جوان در شعبه ۱۵دادگاه انقلاب تهران به ریاست «ابوالقاسم صلواتی» در تیرماه ال جاری صادر شد.
ارغوان فلاحی که اوایل بهمن۱۴۰۳ به دست نیروهای امنیتی بازداشت و به بند ۲۰۹ زندان اوین منتقل شده به «بغی» متهم است.
هرانا به نقل از یک منبع مطلع نوشته است که ارغوان فلاحی مدتی در بندهای ۲۰۹ و ۲۴۱ زندان اوین نگهداری شد و برای گرفتن اعتراف اجباری از او درباره کشته شدن «محمد مقیسه» و «علی رازینی»، دو قاضی جمهوری اسلامی، تحت فشار قرار گرفت.
فلاحی پیش‌تر نیز در آبان ۱۴۰۱بازداشت و به اتهام‌های «اجتماع و تبانی» و «تبلیغ علیه نظام» به دو سال زندان محکوم شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/77988" target="_blank">📅 19:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77987">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KyYgvpF_HDKhr48v9Q5HcvKaP3pVfXP4fxmuHL1GX1vqVPkQi9Pe2ax1DDVMT5Xmo22YzmBhPwH97rqPBZ4-vqaxB_S_gFcbnJeHlqrclvg2aJWTS9VZVB5myW4iMOCgTpXGKf3mPhm97TDCv6zpRLaiPAYmeLM-0UkorOnAa7VQJebxx5mKNsMbY2aU5oxC1vV1cZjhXcBPO0ON4KGIElHoXEl7L9DYPvIuRCBW1l7Zdjl-B80BAUxEonm3IXJFHsGwqTk25M0iiuF_Z6pmiOgdxMKcfG_GmPdX9RBD8jSUHcEb0NlRp4mwu9wZll6pBStBN1nab25m3zeGz03akA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
۱۴ سال پیش: «فلج‌کننده‌ترین تحریم‌های تاریخ.» شکست خورد.
۸ سال پیش: «فشار حداکثری.» شکست خورد.
۵ ماه پیش: «تسلیم بی‌قیدوشرط.» شکست خورد.
امروز: «کوبنده‌ترین عملیات اقتصادی تاریخ.» محکوم به شکست است.
این فیلم را قبلاً دیده‌ایم. همان مزخرفات. قلدرها عوض شده‌اند.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/77987" target="_blank">📅 18:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77985">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dd72c517e9.mp4?token=cmicr1ZQpJHSnsaZM7FlkqqIEfCY9_L6AezdIo7Qkod6-4Wt5l4VGuUAt_-CWOPItpYXwS_JoE0X5WgNy4JdHH7uboRxfz2r_1tvH3FZWwEeLQT1ghAX-KvjrEE193k3OymZVzTuOHyhqcUQFUY3o4xQnR51JuYnzvmrNQ8hMh1qPCTlxppqDBiC9iuyVpVh3DHyt33tnAF_lZEb_yoU9FlSHkspi4dNHtXUgzmpnHihWNC8ocT9nh10WtUvfeg9enm6PQku_lT571h2zHTy4woywdm4h_J1budpkHWSynQODluc59VZex44Rnk9lJdY60THhz-fYZYqFx_3pu_67g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dd72c517e9.mp4?token=cmicr1ZQpJHSnsaZM7FlkqqIEfCY9_L6AezdIo7Qkod6-4Wt5l4VGuUAt_-CWOPItpYXwS_JoE0X5WgNy4JdHH7uboRxfz2r_1tvH3FZWwEeLQT1ghAX-KvjrEE193k3OymZVzTuOHyhqcUQFUY3o4xQnR51JuYnzvmrNQ8hMh1qPCTlxppqDBiC9iuyVpVh3DHyt33tnAF_lZEb_yoU9FlSHkspi4dNHtXUgzmpnHihWNC8ocT9nh10WtUvfeg9enm6PQku_lT571h2zHTy4woywdm4h_J1budpkHWSynQODluc59VZex44Rnk9lJdY60THhz-fYZYqFx_3pu_67g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمیدرضا حاجی‌بابایی، نایب‌رئیس دوم مجلس، روز پنجشنبه ۲۹ مردادماه در گفت‌وگو با خبرگزاری فارس با اشاره به تحولات مرتبط با تنگه هرمز و تلاش برخی کشورها برای ایجاد مسیرهای جایگزین انتقال نفت، گفت: «کسی که امروز خط لوله می‌کشد تا تنگه هرمز را تضعیف کند، در واقع به ما موشک می‌زند. نباید اجازه دهیم خطوط لوله جدید ایجاد شود.»
او با تاکید بر اینکه احداث این مسیرها در راستای منافع ایالات متحده است، افزود: «هر کشوری که در زمینه فناوری یا اطلاعات به آمریکا کمک کند، عملا وارد جنگ با ما شده است. احداث خطوط لوله‌ای نظیر فجیره و ینبع برای کاستن از اهمیت راهبردی تنگه هرمز، مصداق بارز جنگ و حمله موشکی علیه کشور است و پاسخ ما باید ممانعت از ایجاد چنین خطوطی باشد.»
این اظهارات در حالی مطرح می‌شود که شبه‌نظامیان حوثی یمن، وابسته به جمهوری اسلامی، در هفته‌های اخیر با حمله به کشتی‌های حاضر تنگه باب‌المندب تلاش کرده‌اند صادرات انرژی از این آبراه را مختل کنند.
از سوی دیگر، مرکز مشترک اطلاعات دریایی (JMIC)نیز، روز پنجشنبه، از عریض‌تر شدن گذرگاه جنوبی تنگه هرمز خبر داده و اعلام کرده بود این تغییر امکان تردد هم‌زمان کشتی‌های ورودی و خروجی را فراهم می‌کند.
مدیرعامل آرامکو نیز روز ۱۳ مرداد ماه، اعلام کرده بود این غول نفتی با تکیه بر خط لوله شرق به غرب عربستان سعودی، کانال سوئر و تنگه باب‌المندب، به صادرات نفت خود ادامه می‌دهد.
@
VahidOOnLine
مصطفی خوش‌چشم، کارشناس صداوسیما در مصاحبه‌ای پیشنهاد داد، «نیروهای محور مقاومت» با استفاده از «مین‌های دریایی هوشمند» خلیج فلوریدا را مین‌گذاری کنند.
خوش چشم، در تیرماه گذشته در تلویزیون به شدت از عباس عراقچی، وزیر امور خارجه، انتقاد کرده و تحلیل‌های او را به «رانندگان تاکسی» تشبیه کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/77985" target="_blank">📅 18:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77983">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vkx7x-kOPfTz0nqkJqNbAJaqm9NFxIixVoy6hRZgQKSZu_2IpVh9V1XzbWoHMHpCNORYeRIxlmJkgkay4ihfDQ4c_xBBw5UtKRUTEPrV5zLdJgIJB9ig2wmkdvLU6f_Sptjhj0Zad3QEKZm0DpFWujDnR3a8et82pWCjecztamIatJcx1Ji0q6dIbN4cekx_RwFdNaR08flBmP4WAw80kdF6brjEwQJM7w-oP7onMCrPT9-o433xcSD5bZF9PPiArgD0zXF0NHO1vNayP-kwigiDEz_V3avsbES5jmZ7T_xoLMMNU84Tfe2y86CiLiSgwTT4pugtF0f8ozV-O0JiEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Dpya2ooyBDe_O4tNz7BOf0NJXBAXOw8g8msdKI7NsWVwvvYecBai15sdJzcrCTlbJHz-yNm09v0pH8l0RWtsQt0DSVXb3SZOMG45G85T_HkDbn6PhWog7gW1Fyb2bgfwMnON-Ffympl5G6TN6xxkZOSLDNsVj6DeDsTYXmJ-UEDH4F-038AyRJ-Mh7jdGeztXkIOeXU6bv-nOxVbHM5LCRs6Bas1MzkOsFyOF-T6zhf9W42IBNsaJ0VyCzxsLe_AoEXeiSnvWfrEBBONHLlXXbPBof4UKvRnr-dgFXXErOS-X-U874EicQo5dHZKRsiVl5y7xKjdy9GAs9lQrP855A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس پازوکی، معاون ارتباطات و اطلاع‌رسانی دفتر محمدرضا عارف، معاون اول مسعود پزشکیان، اظهارات منتشرشده عارف درباره تعیین نرخ ۸۷ هزار تومانی در دولت را تکذیب کرد. این در حالی است که رسانه‌های ایران پیش‌تر اظهاراتی از عارف درباره تعیین این نرخ منتشر کرده بودند.
به گزارش رسانه‌های ایران، عارف دوشنبه ۲۶ مرداد در جمع خبرنگاران گفته بود پس از تعیین نرخ چهارم بنزین با بررسی کارشناسی و تعامل با نهادهای امنیتی و سایر قوا، قرار بود این طرح به‌صورت آزمایشی در کرمان اجرا شود، اما بدون هماهنگی با دولت متوقف شد. نرخ چهارم مورد اشاره ۸۷ هزار و ۲۰۰ تومان است.
با این حال، پازوکی در ایکس مطالب منتشرشده درباره اظهارات عارف را «ادعای ساختگی برخی کانال‌های غیررسمی» خواند و گفت: «معاون اول رییس‌جمهور هیچ‌گونه موضع‌گیری یا گمانه‌زنی عددی درباره نرخ‌های جدید بنزین نداشته‌اند.»
او افزود: «موضوع مدیریت مصرف سوخت در مرحله کارشناسی قرار دارد و هنوز هیچ رقم یا تصمیمی به جمع‌بندی نهایی نرسیده است.»
@
VahidOOnLine
فاطمه مهاجرانی، سخنگوی دولت، روز جمعه ۳۰ مرداد ماه اعلام کرد مطالب منتشرشده به نقل از محمدرضا عارف، معاون پزشکیان درباره تعیین قیمت ۸۰ هزار تومانی برای بنزین صحت ندارد.
مهاجرانی گفت چنین عددی نه از سوی معاون اول رئیس‌جمهوری مطرح شده و نه مبنای تصمیم‌گیری دولت قرار گرفته است.
او تاکید کرد در صورت نهایی شدن نحوه «مدیریت مصرف سوخت»، جزئیات از مسیرهای رسمی و مستقیم به اطلاع مردم خواهد رسید.
@
VahidOOnLine
مسعود پزشکیان، در مجمع عمومی «انجمن اسلامی جامعه پزشکی ایران»، گفت: «جدا از بحث محدودیت‌های مالی و محاصره دریایی دشمن که کار صادرات و واردات ما را با مشکل مواجه کرده است، چه کسی گفته دولت باید بنزین ۱۳۰ هزار تومانی بخرد و بعد آن را ۱۵۰۰ تومان بفروشد؟»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/77983" target="_blank">📅 18:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77982">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IpiPUi7jJ6ad8C3iKwHMgDvdZi_RkcSRnw29_cmeZ-kuTFyJ1QlbiwdgIjssHQj2dHNReij2IsjZ-tsl4C24ZdHicWq3lmHR7O3KkZ-dXHeCKuqZ0SFBCISisb_oQeIDCVJlojpM95kNa6BXgobt6lmznRjpqjTt3u2SbVQ1LZ3z_rbchoS1t7HFpP6crOrrf1fG8bJ7ayMed4_b1NKql5ggIgs-AFIObSZSuKS1W3mRviFsGilVvndn1PbXKCTSEW25N9jCADYDGxOBjFGgjMtTP9qTmciEjP8prkfxniq_AQsJLU_Az__IDuvag8-6Mi-gUD2sTc0ZL23gikEfmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس دولت در ایران، می‌گوید اکنون زمان آن است که به جنگ با آمریکا پایان داده شود چرا که تهران در مقابل واشنگتن در موضع «قدرت» قرار دارد.
آقای پزشکیان گفت: «بهتر است امروز که در قدرت و عزت هستیم و تمام دنیا به پیروزی ما اذعان دارند و تأکید می‌کنند که آمریکا برخلاف تمام مقررات، به مدارس، بیمارستان‌ها و زیرساخت‌های ما حمله کرده و در دنیا منفور است، جنگ را پایان دهیم.»
رئیس دولت در ایران همچنین نتیجه مذاکرات ایران و آمریکا را که به امضای تفاهم‌نامه اسلام‌آباد منجر شد، «دستاوردی بزرگ» توصیف کرد که «با وحدت و همدلی در شورای عالی امنیت ملی به تصویب رسید و همه کسانی که در این شورا هستند و دستی در آتش داشتند، با قاطعیت از آن دفاع کردند.»
آقای پزشکیان در ادامه از کسانی انتقاد کرد که «خارج از گود نشسته‌اند» و «نمی‌دانند دولت در چه شرایطی است، مجلس در چه شرایطی است و فرماندهان در چه شرایطی هستند، بی‌محابا اظهارنظر و تحلیل می‌کنند، هیچ رنج و سختی هم به آنها نرسیده و بعد هم دم از گرانی می‌زنند.»
مسعود پزشکیان در عین حال تاکید کرد که اظهاراتش به معنای تسلیم شدن در برابر تعرض احتمالی نیست: «ما به هیچ عنوان در برابر قلدری سر خم نخواهیم کرد و هیچ تردیدی در آن وجود ندارد. تا آخرین نفس مقابل آنها خواهیم ایستاد و پاسخ کوبنده به آنها خواهیم داد.»
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/77982" target="_blank">📅 18:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77981">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9359b0410.mp4?token=s4AB-5BCCNam7247C2ko8v5JgcsHGWEjzyY54FV5WGkDshCl9aMANuENTtboW1JcYOZeydcrH2CLOLRAkCMwva2dvKfpJkowpaQF_uqha2z1lTdN6HFfuJWKbXJu-WaUeL5J-De9I4_s_SKTKizZauVFFFjsVqO2UaofUe52pBz6a3-RzzfwRi6917dvOeGxlDH49TDf_cMZ57CT5d_a4vjHTGBF7frJZctmFvzszIoDdDYDUDcEjTuBA_juxitQhylmj5f2exiv2EoGgZwYdmqhRS3tqDjmmP-PRRYfHkzGJV_Jm9Gw2sO5pN5qpmaLBtkn-1UYm3Me31uVe94VMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9359b0410.mp4?token=s4AB-5BCCNam7247C2ko8v5JgcsHGWEjzyY54FV5WGkDshCl9aMANuENTtboW1JcYOZeydcrH2CLOLRAkCMwva2dvKfpJkowpaQF_uqha2z1lTdN6HFfuJWKbXJu-WaUeL5J-De9I4_s_SKTKizZauVFFFjsVqO2UaofUe52pBz6a3-RzzfwRi6917dvOeGxlDH49TDf_cMZ57CT5d_a4vjHTGBF7frJZctmFvzszIoDdDYDUDcEjTuBA_juxitQhylmj5f2exiv2EoGgZwYdmqhRS3tqDjmmP-PRRYfHkzGJV_Jm9Gw2sO5pN5qpmaLBtkn-1UYm3Me31uVe94VMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک هاکبی، سفیر آمریکا در اسرائیل، گفت جمهوری اسلامی بیش از ۴۷ سال است که شعار مرگ علیه آمریکا و اسرائیل سر می‌دهد و تاکید کرد که این تهدیدها را نباید صرفا حرف یا شعارهای توخالی تلقی کرد.
هاکبی روز پنجشنبه ۲۹ مردادماه در گفتگو با شبکه ملی اسرائیل (آروتز شیوا) گفت: «۴۷ سال و نیم است که می‌گویند ما را خواهند کشت، اسرائیل را خواهند کشت.» او افزود: «این‌ها صرفا تهدیدهای توخالی و شمشیر تکان دادن در هوا نیست. این‌ها کسانی هستند که واقعا می‌خواهند ما را بکشند.»
سفیر آمریکا در اسرائیل گفت آمریکایی‌ها باید این تهدیدها را جدی بگیرند و برای اثبات سخنانش به حمایت مالی و تسلیحاتی جمهوری اسلامی از حزب‌الله، حماس و حوثی‌ها اشاره کرد.
هاکبی افزود جمهوری اسلامی علاوه بر صرف منابع برای تسلیحات خود، حزب‌الله، حماس و حوثی‌ها را نیز تامین مالی و تجهیز کرده است. او در ادامه گفت: «اگر در جهان اقدامات تروریستی در جریان باشد، معمولا می‌توان رد آن را تا تهران دنبال کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/77981" target="_blank">📅 17:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77980">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZHEwyg_Ex6_QF0rrD5H5ZrFWYoSx9VXvrmDXeMvifxYFa-A83l8WjCmyTkJ1NSJzTycZMZ8z_VFUgJ7Ig4ISe79opMYzi3ixmHu50LnaF5Ay6wzQQTIQRVxOQljwvWuBK2kaVrELZK_M1TlrafP5NbAvRrOrZODRsJ0ZruoDtb3Z0vTfw0qqzvegzCYFQ4Iyvh9kUoVftQ_a74VMYEwdz_FFp1_m9CRkDBpNAHtFa1ScXUdtYWzSUBlP5T6Car0Plkj3dFkbKmVVAL-aQSAqVFT-LgwmnLzSX3jzYuPYomFBSrQGSMo9TwVon8OJ2Y9i-mpk0JrYNLubQtVhqLrAgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مجلس شورای اسلامی با هشدار تلویحی نسبت به شرایط اقتصادی جامعه ایران گفت: «ما هر چقدر قدرت نظامی داشته باشیم ولی اگر مردم گرسنه باشند و گردش مالی، رشد اقتصادی و تولید ملی نداشته باشیم، دوام نمی‌آوریم».
محمدباقر قالیباف روز جمعه ۳۰ مرداد در اظهاراتی در عراق برای افرادی که «فعالان اقتصادی ایران و عراق» معرفی شده‌اند، با «ظالمانه» خواندن تصمیمات جدید دولت آمریکا برای اعمال تحریم‌های اقتصادی شدید علیه ایران گفت: «باید برای غلبه بر آن‌ها برنامه‌ریزی کنیم تا بتوانیم بر آن‌ها فائق آییم».
قالیباف که رئیس گروه مذاکره‌کننده ایران با آمریکا پس از جنگ اخیر بود، در اظهارات خود خواستار استفاده از پول ملی ایران وعراق در مبادلات تجاری بین دو کشور شد و گفت: «می‌شود به دهان ارز آمریکایی زد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/77980" target="_blank">📅 17:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77979">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uBEDlGM0DkLjkSD8p8bs-dyOudmDgtmhl1pmrb7Vkucs6P9aqvyA9u_MlJQYC7a_vip_dWx9kDO74ZO4lkUdmFWM-qRwZZucs5BGo8lB3d-v7SE9zWSah4oWqwyKsYtbGdzSjF9f6t6K6cVFgWTiWVcD-k2kpvmeYae3R6hhmKvQc69nhytAIlln95WKZV3ezJe_JL7wOS6cfQqrYnrGEn959B1ymO7TJ5McbYwOz95s-UsDfGIam0scG_ifOxeFsIvhIG-eBV2lUQmcIOQpeHSsaFeB0fomhVnQ_qxaSmMzDXxxy4xmtlXWB4SUjInv895kXLLqy5Qrh0XSMM8l2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه لبنان می‌گوید روابط عادی با نمایندگی ایران در لبنان تنها زمانی می‌تواند از سر گرفته شود که تهران مطابق با رویه‌های دیپلماتیک تعیین‌شده، از تصمیم دولت این کشور پیروی کند.
یوسف رجی در گفت‌وگو با روزنامه «النهار» با پافشاری بر تصمیم قبلی‌اش در «عنصر نامطلوب» خواندن سفیر جمهوری اسلامی در لبنان و اخراج او گفت: «ادامه حضور سفیر ایران نقض یک تصمیم حاکمیتی است. این تصمیم باید رعایت شود و هیچ تفسیر، استثنا یا مصالحه‌ای را نمی‌پذیرد».
دولت لبنان چهارم فروردین امسال با رد استوارنامه محمدرضا رئوف شیبانی، سفیر ایران در لبنان، او را «عنصر نامطلوب» خواند و چند روز فرصت داد تا خاک این کشور را ترک کند.
با این حال، وزارت خارجه ایران این تصمیم را نپذیرفت و سخنگوی این وزارتخانه اعلام کرد که سفیر همچنان در بیروت به فعالیت خود ادامه می‌دهد.
اسماعیل بقایی آن زمان گفت: «سفیر ایران با توجه به مباحثی که توسط جهات ذی‌ربط لبنانی مطرح شد و جمع‌بندی که صورت گرفت، به کار خود به عنوان سفیر در بیروت ادامه خواهد داد و کماکان در آن‌جا حضور دارد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/77979" target="_blank">📅 17:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77978">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/282709f91d.mp4?token=gb6I-YIApf0QXHluf6XUD1_ZgefCPZF2OgnkMBwL_XUdhJA6FpIuaB-oElXom6_FbaAEGtfTWWtVwSu8-K6-N5QrKE24qyPByeVYg0K1T_ts6h_lW10YM3iGHY8A1OOKFdd_zWtpUrf4w0ly9CB4taZ2kaIf-PAurFmlhB0_Ee3eR5qAsEw2YaD5lKUReCrH7275pgQBUHKnK1jpOOpZOAawSYOnT3VN8fhObAPZYzmRtRUv-I63uj5Apa7_7gKjerFjkXFQJjUKe9LEJxIfghBPEyKpcv3JwZtWF3haUvkFGw7PNYIdYFYKTwIAjHaCy1OecNywUa5pnZGFu7Ex-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/282709f91d.mp4?token=gb6I-YIApf0QXHluf6XUD1_ZgefCPZF2OgnkMBwL_XUdhJA6FpIuaB-oElXom6_FbaAEGtfTWWtVwSu8-K6-N5QrKE24qyPByeVYg0K1T_ts6h_lW10YM3iGHY8A1OOKFdd_zWtpUrf4w0ly9CB4taZ2kaIf-PAurFmlhB0_Ee3eR5qAsEw2YaD5lKUReCrH7275pgQBUHKnK1jpOOpZOAawSYOnT3VN8fhObAPZYzmRtRUv-I63uj5Apa7_7gKjerFjkXFQJjUKe9LEJxIfghBPEyKpcv3JwZtWF3haUvkFGw7PNYIdYFYKTwIAjHaCy1OecNywUa5pnZGFu7Ex-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"حمید مهدوی، متولد ۱۳۶۶، آتش‌نشان ساکن شهر مشهد شامگاه ۱۸ دی ۱۴۰۴ و در جریان اعتراضات کشته شد.
ویدئوی کوتاهی از او در حال حمل یک معترض مجروح بازتاب گسترده‌ای در رسانه‌های اجتماعی ایران و جهان داشت.
پیکر او در آرامستان روستای تویه دروار در شهرستان دامغان، زادگاه مادری‌اش به خاک سپرده شد."
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/77978" target="_blank">📅 17:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77977">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dX5ZeoBgrYWqyF_fb5gIffdcjJhr-HIvajD17k51NnDYzW8Wc4iMq8FCXNKQdzLlF1GZIT65OgLr71llENdk08FOqow4yc8Zy3uwfMFybkeUXYHWncinWiJ0U7RZeN6NdMKAzAUON8g8pLRv8WFjhxTtGtrRScbbNtKRav3gbfhAdbks-5z3H0XGD1aoMAEBiXLfYD8P_b24kA9AVQNZLO_nRmbsjk7od6lUUc_uV46tjQamvJ5nSjI2Nfwrzn-i-B9rXmVhS7NEnFuv9CdqFPR0sQV9-dz0QcckjZ1n1smqkgYU2i_lEWDOl4RHrj4jrPw4aVEye4cxBz5tJq2HfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حقوق بشر کارون از افزایش شمار زندانیان سیاسی و عقیدتی در زندان شیبان اهواز خبر داده و گفته است بیش از ۶۰۰ نفر در بندهای مختلف این زندان نگهداری می‌شوند. بسیاری از این زندانیان، هستند که در موج بازداشت‌های پس از جنگ ۴۰ روزه ایران و آمریکا و اسرائیل بازداشت شده‌اند.
تعداد قابل‌توجهی از بازداشت‌شدگان جدید را جوانان تشکیل می‌دهند و سن بیشتر آنها بین ۱۸ تا ۲۵ سال است و اکثرا از اهالی اهواز، فلاحیه (شادگان)، ایذه، بهبهان و مسجدسلیمان هستند. در این زندان بیش از ۳۱۰ نفر در قرنطینه محبوس هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/77977" target="_blank">📅 17:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77976">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ry304B10oWyhmKUQ580PG1G04E2b4-1Riy7LFBsBQQ1AduYu8SkA8CXwTE4Ef8tiiUMgM9Kuv9UnZzp3lsnrhvp45vEKUs3qfgzOAJ6MpDYRh4kgefYXSbX9wF8esVHZPoKvbbzgE8gk80NQ_3UfNJJ9VVd_EFx_wldNEJC2P2sOyfLVI1NLRuJlJwq6DYZINAQBgXlapqStzU0QwDI1JC2hVEUW5yTP0dBlmQ1zi3U8DsKb9FSC_NjqioXD-goMaHMNdSWM_M8Rsi88BesnlVf6ba5NOBQpLjJ6wpoElW1zW8EENx1pfj3xa5-HUMXwerTapoyG1RDQHfXyZD59lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از «دونالد ترامپ» رییس‌جمهور ایالات متحده و «اسکات بسنت» وزیر خرانه‌داری آمریکا، «جی‌دی ونس» معاون اول ریس‌جمهور آمریکا از آغاز «مرحله جدیدی» از جنگ ایالات متحده و ایران خبر داد و گفت: «موثرترین ابزاری که برای اعمال بر حکومت ایران داریم، فشار اقتصادی است.»
جی‌دی ونس که در پادکست  «کلی تراویس اند باک سکستون» صحبت می‌کرد به «تعامل ظریف» بین دو کشور اشاره کرد و گفت: «ما به آنها فشار اقتصادی وارد می‌کنیم، آنها نیز سعی می‌کنند به ما فشار اقتصادی وارد کنند. اما آنچه در چند هفته گذشته واقعیت داشته این است که آنها فشار بسیار بیشتری نسبت به ما متحمل شده‌اند.»
به گفته معاون دونالد ترامپ آمریکا این روند را ادامه خواهد داد چرا که بر این باور است «این بهترین راه برای دستیابی نهایی به هدف نهایی» این کشور است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/77976" target="_blank">📅 01:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77974">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J8dmAsrqToiE11cTpOEXDSUVzu9UHaC0v7319nbobIGWx4tZsUaZ9Opz182OrYIMW2_TVb6rF-bWnTtTT-dnXOQPGRBzhMhSgCYrbgQFgIUR9UWjsPOM4RCUu2hQe65Xxwee5nbEDwOpyLuIZg-h2pU4ylCZKAfRuM_CuL_OA6Dx6TZqDdZ6PVXHdZqXdQIgub9alFqGvsWUGmHaBH7sGT36AvTRbJUIeUEyqmxmAoRffoaAr3DM8UCgeb9iM_UcLcNS8KA5dOmM_H1kYyWK3zuDCZ9sNb66Yd8B_slf3xUzD0p1vi8gfkRJW0BRk0RWZGrLq7T7Vlpf_KptJmuMBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jcTdaYRfifBzcrfUHEsQZolY9pQExHYQ7kXbff78S5ATb1U1eomxzdAOpJ2Zmfakq4OWJkVZNrBn0mjxi-USftoxFeGdSA28-gycDIUU32I6HKFZ2hXr9-jP6z69J7vDdKWoztxDMaAkOgN8YOfC9Ws98EocPNIePCQsjVdVOJLwpPHasLKbzUtAABzo8koSJKIoXk7buNN5eHcwUzEpJSylH558Tr38DN_mH7E_kmtI2_ytx9mjEYV6WvnJCLEYe39T99bTgHyIn5wS4dznVcDjEbDSlqPiegdlBxiR-IiFtnwgkPL3_C2wudvuANxEvSeYnNheHvSOR__XJYj01g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتشار تصویری از محمدباقر قالیباف، رئیس مجلس ایران، در جریان سفرش به عراق که در پس‌زمینه آن عبارت «خلیج فارس» دیده می‌شد، واکنش همتای عراقی او را در پی داشته است. هیبت حلبوسی چند ساعت بعد تصویری مشابه از خود منتشر کرد که در پس‌زمینه آن عبارت دیگری دیده می‌شد.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77974" target="_blank">📅 01:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77973">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PHxTkI5Ykb-CPLg09Q7C3JJN-sT6zN0mSPNM-6Jey-dAJ9N_Koivi3igiNO-pqPc4yjSUimgnSrJIENDehe_18uJkyXvBxW7-uQdvFdv_EwRzLFGi0XsRi_edLprre5Hh8TBC78GNz9vNb8vkLhX9Kgj2RtKjtR9cW3sb9oio04Pp9D_X0-6sYUB_NP5NIcVIgqtsU8UlNQ6A5rfWvF_7MmU2W1R18ieccC7hWywwNa-NvPWv-0Ts2Zm71axAklWZSmiMDb4ibkzG2Tms_7rxGonBOcHNXDo0juo1r6aVBLP7f1Y57mnaPO_PkZHVUUUvuBnrNEYNBlgQgXl2Jymwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، روز پنجشنبه ۲۹ مرداد گفت طرح واشینگتن برای افزایش شدید تحریم‌های اقتصادی علیه ایران با هدف «سرنگونی» حکومت جمهوری اسلامی دنبال می‌شود.
بسنت در گفت‌وگو با شبکه سی‌ان‌بی‌سی گفت: «این طرح در ایران جواب خواهد داد و ما این رژیم را سرنگون خواهیم کرد.»
او افزود: «این بزرگ‌ترین انزوای اقتصادی هماهنگ‌شده در تاریخ جهان خواهد بود.»
وزیر خزانه‌داری آمریکا روز ۲۳ مرداد نیز خبر داده بود دولت دونالد ترامپ قصد دارد اقداماتی در مقابل ایران انجام دهد که به گفته او «در تاریخ انزوای اقتصادی یک کشور بی‌سابقه بوده است».
او گفت: «اگر ما حداکثر فشار اقتصادی را اعمال کنیم، به احتمال زیاد دیگر شاهد ازسرگیری یک عملیات نظامی گسترده نخواهیم بود؛ اما تأکید می‌کنم که این وضعیت مربوط به حالا است.»
اسکات بسنت همچنین خبر داد که روز دوشنبه هفته آینده یک نشست خبری برگزار خواهد کرد تا «دقیقاً درباره اقداماتی که قرار است انجام دهیم» در قبال ایران توضیح دهد.
هشدار به متحدان آمریکا
وزیر خزانه‌داری آمریکا همچنین در پی اعلام طرح جدید دونالد ترامپ، رئیس‌جمهور آمریکا، برای تشدید فشار اقتصادی بر ایران، به متحدان واشینگتن هشدار داد که در موضوع انزوای اقتصادی ایران باید میان «همراهی با آمریکا یا قرار گرفتن در برابر آن» یکی را انتخاب کنند.
او دربارهٔ پیام خود به متحدان آمریکا گفت: «این بزرگ‌ترین انزوای اقتصادی هماهنگ‌شده در تاریخ جهان خواهد بود. ما به آنها می‌گوییم که یا با ما هستید یا علیه ما.»
وزیر خزانه‌داری آمریکا در پاسخ به پرسشی دربارهٔ احتمال اعمال فشار واشینگتن بر چین نیز گفت: «بسیاری از گفت‌وگوها بهتر است در خفا انجام شوند»، اما همزمان از پکن خواست «با این برنامه همراه شود.»
او گفت: «ما اطمینان داریم که همه خواهان بازگشایی تنگه هرمز و کاهش دوباره قیمت انرژی هستند.»
بسنت در ادامه با اشاره به وابستگی چین به نفت خلیج فارس افزود: «در نظر داشته باشید که ۵۰ درصد انرژی چین از داخل خلیج فارس تأمین می‌شود. بنابراین، همراه شدن با این برنامه می‌تواند خدمت بزرگی به خود آنها باشد.»
این اعلام موضع وزیر خزانه‌داری آمریکا یک روز پس از آن است که رئیس‌جمهور ایالات متحده اعلام کرد که کارزار جدید و بزرگی را برای هدف قرار دادن اقتصاد ایران به راه انداخته است.
دونالد ترامپ شامگاه چهارشنبه در شبکه اجتماعی خود، تروث سوشال، نوشت: «امروز، من کوبنده‌ترین عملیات اقتصادی‌ را که تاکنون علیه کشوری انجام شده است، اعلام می‌کنم! این یک جنگ و انزوای اقتصادی در مقیاسی بی‌سابقه خواهد بود».
او افزود: «همچنین اعلام می‌کنم که هر کشوری که به نهادهای مالی، کسب‌وکارها، فرودگاه‌ها یا ارگان‌های دولتی خود اجازه دهد هرگونه راه نجاتی برای ایران فراهم کنند، خود با عواقب اقتصادی بسیار سنگینی روبه‌رو خواهد شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/77973" target="_blank">📅 20:18 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77968">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NilThx-UhRpJjFZ0C_JhmESPylLM7xOZby1-HppJ2xNqsfuCuF8jGKjuOI4ipwRYFA3fg1AksKbhn62t-40oG5F7WOwXD6MRFFa7wE0vmTDippcQgQv6IsrLMXmtJdYrHrI5GrcJb_NTzrZZ9859VyQ4PhRDh0KOI9DUfiO_COW35CbgpDzLFq11Lly8_plS-lyfx-GSW7U3rZVyLXWfWLh9X3yyC3y-Md13zorik67MHga1Y5_wstCXQJLnZ_QOS-wDNE8Q3hUofwSct3ubvgOKhMf0RSUjGV-sb8DMbTCySIA7hxVd_ByHJyFen3tXi9bHE-mxiR1lVv4AwX18Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NV_BklrIJv_LIQCMdlAkjQdsNfLH0kxSfF_xEtCt57lmpxaD1dLF2UFMvfh7XYzVmiV4FqjzpEp71yJ5VG3g781lIuwDjScr5-1W8Rcqk1IIzRqDcshgF84YPvC4n6sz4KDK8OGkzmVH1z0bj5-MG5Y_NzhngWeTxnZ_oxrKZX45KMuYTC9HHh4igM_ECdpmAH0IG2m3veNkZAv0ihjpdd0CNavFTSV52HtccOYDzf8QpqJQS-jqoVYouiheMaaYgVKDkaj4zTg96be8iSqF8D-LwN4vdfvXxhrZeSUzLvoz0q1MxZ8EZqtYOyWZP7G-bm5ryDnqbg0gCU9eY7YUUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S_LcFqKcYhBGgXtzkg6hFdXkFhrySoOg-6MkX1aFMgXvGgWOL8b1GRDn8G30TT6yIuPjiBGCTTxnQgsOMKQNkuifROB2PMvdoZ0Ddf0rBX3JRqcitcjcvdc9eXdJwNXTLzrKGTXz7NoTxJ2BPAf4s_2XbwgckAz7b3YpaxaiLRIklu8-uNeMrTZuBYAZetddcso5_WiZR1xPPVnHwoOxdn8IcNrp7t_lI7opmlp1BKiLlpqYM3WWgAnmXfQ8ODAJe7_KWCkLMzEYVC6VGfy35b165OH_HrIttGyjYNM0OPtWZdr41B7EphFWCqJoFQllWSYVnCNYZXxAIYEK2NA6ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e50a342f2.mp4?token=JG3X3BXQWTFzbHfuf2MOMXwGtCxYhTsBqMKBIJkZ8VwiVT4ORLMSnTiwWsiRGqCUsPl3_lQYZbi_YINyBSrvZJ3MyXjBMOqUAeSjW5ML3i-Mny8Hw5OJdoJeMAe5oBPfYGqrcs7cWOIJAjsIxjfoJeW8kOTM0klo6UxHqIef6cIAcjFrIXzKr_3hYymEMnzNqiww17PoR_Y-PC9w6hQVrT3mosx1DAfpyxWhfZkstwK--RNd-ph9DjvU1imo532Q_GTwFZa-nCmaLLIRjLT-REtwq9D6BvSX5DXYbMYIU7IMFWWf-Gon6Prb0zmDDtFwpOGHeeTpLlPcGZEIwcRGIKBMccoYLW44HdcIEabRDdz0wkHzApnRQtk6SFkOQGfr-BXUo2UmSIOf3ajaskvhUQB9sviWQMGWaozCYfANmlA6EnPe4bIxwidk1PKOMEGsBgL-1Tg6usD8EW7-rAfbjP2IiMP3QylNAePXn8KVtYakavoFTahXzIjx_hKqLFS0r2SrzxDj5_SLd5D8ktRJwCsKCfULkmsQcTbhNthXzAjGLQEuTbtEhLb3OoHnpQsz6VyEVDkUIeSPBcgsCP4Z65nRCTkYCYpuzSfz8GUfLUseWJYnT-vurd04WuzBGy3tlPy5Pp0er4IExaB-96vBKVWrXsr4nXRFCbIYxupAcWE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e50a342f2.mp4?token=JG3X3BXQWTFzbHfuf2MOMXwGtCxYhTsBqMKBIJkZ8VwiVT4ORLMSnTiwWsiRGqCUsPl3_lQYZbi_YINyBSrvZJ3MyXjBMOqUAeSjW5ML3i-Mny8Hw5OJdoJeMAe5oBPfYGqrcs7cWOIJAjsIxjfoJeW8kOTM0klo6UxHqIef6cIAcjFrIXzKr_3hYymEMnzNqiww17PoR_Y-PC9w6hQVrT3mosx1DAfpyxWhfZkstwK--RNd-ph9DjvU1imo532Q_GTwFZa-nCmaLLIRjLT-REtwq9D6BvSX5DXYbMYIU7IMFWWf-Gon6Prb0zmDDtFwpOGHeeTpLlPcGZEIwcRGIKBMccoYLW44HdcIEabRDdz0wkHzApnRQtk6SFkOQGfr-BXUo2UmSIOf3ajaskvhUQB9sviWQMGWaozCYfANmlA6EnPe4bIxwidk1PKOMEGsBgL-1Tg6usD8EW7-rAfbjP2IiMP3QylNAePXn8KVtYakavoFTahXzIjx_hKqLFS0r2SrzxDj5_SLd5D8ktRJwCsKCfULkmsQcTbhNthXzAjGLQEuTbtEhLb3OoHnpQsz6VyEVDkUIeSPBcgsCP4Z65nRCTkYCYpuzSfz8GUfLUseWJYnT-vurd04WuzBGy3tlPy5Pp0er4IExaB-96vBKVWrXsr4nXRFCbIYxupAcWE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر پرنیان دبیری با انتشار ویدیویی گفت دختر ۱۶ ساله‌اش پس از اصابت گلوله به کهریزک منتقل شد و پیکرش در محوطه این مرکز روی سطح آسفالت قرار داشت.
او همچنین گفت هنگام پیگیری تحویل پیکر دخترش، یکی از ماموران با قنداق تفنگ به او ضربه زد و تهدید شد که در صورت ادامه اعتراض، پیکر پرنیان تحویل داده نخواهد شد.
او خواستار پاسخگویی عاملان کشته‌شدن دخترش شد.
این جاویدنام ۱۹ دی ۱۴۰۴ همراه پدر و مادرش در خیابان بود و از پشت سر با گلوله جنگی سرکوبگران هدف گرفته شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/77968" target="_blank">📅 16:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77966">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M8edA4aMnFV2Ia7FoaLwiuaxsIpNegSm_XRnFmK6GfpZhfFNtKZBJk7ZafHmuAual6J_MxzEg_tRZxrEtvB5NioWqdgoB4-n7tdOrotmvCp0OCuu53H-bkBLQh7kQGn33cHueYTDBplBZkxFSisft8dhspqSAsXSzUBCdif5Ys3WAyp3i9_RNVee8ahVf1d7auER8gf54qoprik-P0ljqfu4tQ6IICqjLxIrQNpEAdEHofvuEg-n5Yy-Wzm-57gRknrq9P-9J2p8nwOXGIL3BBRLFGVVFI7y-mrT8OrbFksglOKtoYWoMk4Cl9dA0rtshm-VPydZe7_YO_YkJaaXVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qzJV1CF5hPJqb_2lxEpoO2vrJwylgViOft1aeZpL9SFbbX2UybaWJaW6GHEuaAKPUCxVrMGhWhYqI79x_IQckfzlfSwbP5kT5v6t1rko3EB4vOt23ieSENV0oJZzqh04Bvyj1qfj4mHKDwkLa2lUrC8lkaNv-NFmq9v_eOHhuHAjf7B50GyJS0F6p52gOADDzw3-rnZiRr0HlRB3JqrhvYdQ8WfANkxqp3-oWSXlNhnslPFUj5AbnjanMdNRx7M3uHf6Vgfq2fBkTKnTPYSvLPSaLvgMgywsibTR3BZshvL7MqUp1dvaPL2R3X4pPnmrq8rxOR3o7fQO0VLSCfg7vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس عراقچی، تهدید دونالد ترامپ مبنی بر آغاز کارزار اقتصادی گسترده موسوم به «روز دی اقتصادی» علیه ایران را تلاش برای سرپوش گذاشتن بر «بحران‌های داخلی آمریکاست» توصیف کرد و از «بدهی‌های بی‌سابقه و هزینه‌های فزاینده نرخ بهره» به عنوان نمونه‌هایی از این بحران‌ها نام برد.
@
VahidOOnLine
معاون وزیر امور خارجه جمهوری اسلامی ایران سخنان ترامپ در مورد کارزار «روز دی اقتصادی» علیه ایران را تلاش «محاسبات غلطی» خواند که برای پوشاندن «شکست‌ بزرگتری» ساخته شده است.
کاظم غریب‌آبادی نوشت: «ادعا می‌کنند ایران در آستانه شکست است و به یک نخ بند است، اما به همه متحدانشان التماس می‌کنند که کمکشان کنند.»
معاون وزیر امور خارجه ایران در ادامه افزود: «جنگ نظامی نتیجه نداد، حالا اسم شکست بعدی را جنگ اقتصادی گذاشته‌اند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77966" target="_blank">📅 15:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77963">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ab9ff1cf5.mp4?token=tZ5FLP-c5xLryDZlS1JHHdnKRkp_vLP6R9KQYTgzpA80teNz3vuVlUeCYC_jm0a8gdT7vN9FEmpTU5leJmO36z7rLkLblekz5V9LLp0MLLzRh_jiLO001bb5rwrOM2a_KF6dSLJGlym_ygqTGEPB_mMD1vYWHMSwSbkvCqWCzYLrFLuhuJGjAaTsZi5KFX1S0ASw5YP2g5Xj2Y3vfNnpt_Gb4X9NNM-fPhgkilIFHLtg6p22ovnXOB1EFB7PbFbkn_3GOBzyD-Q1HwUm14yZfIKAPE4EAkyQDyyog1ZmnRSczU4YuUlyU1-IjJxFDvGdmKMV2iczraXBkOsSLdVWKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ab9ff1cf5.mp4?token=tZ5FLP-c5xLryDZlS1JHHdnKRkp_vLP6R9KQYTgzpA80teNz3vuVlUeCYC_jm0a8gdT7vN9FEmpTU5leJmO36z7rLkLblekz5V9LLp0MLLzRh_jiLO001bb5rwrOM2a_KF6dSLJGlym_ygqTGEPB_mMD1vYWHMSwSbkvCqWCzYLrFLuhuJGjAaTsZi5KFX1S0ASw5YP2g5Xj2Y3vfNnpt_Gb4X9NNM-fPhgkilIFHLtg6p22ovnXOB1EFB7PbFbkn_3GOBzyD-Q1HwUm14yZfIKAPE4EAkyQDyyog1ZmnRSczU4YuUlyU1-IjJxFDvGdmKMV2iczraXBkOsSLdVWKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالناصر همتی، رئیس بانک مرکزی ایران، در یک گفت‌وگوی تلویزیونی تأیید کرد که صادرات نفت ایران در حال حاضر متوقف شده است.
او شامگاه چهارشنبه ۲۸ مرداد اظهار امیدواری کرد که تفاهم‌نامهٔ ایران و آمریکا احیا و مذاکرات از سر گرفته شود.
این نخستین بار است که یک مقام رسمی جمهوری اسلامی به شکل رسمی از «توقف» صادرات نفت ایران خبر می‌دهد.
در هفته‌های اخیر برخی مقام‌های جمهوری اسلامی با اشاره به تشدید بحران اقتصادی و معیشتی، نسبت به دور تازه اعتراض‌ها هشدار داده و از آمادگی برای برخورد با آن خبر داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/77963" target="_blank">📅 15:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77962">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YYBvRzz4p8YUhfWLqLZ5MvMPR4OxV-c9nihiE4ymlbIjAQLEHY-PHljMI5C_lcPasM6Drcbzy0bm81Bf8qT_R_QVmMcELu1Ke3xDInMzPcEpbba2xY0aQJ55Kib1g19m9ES1YsM0Pt4GhkXhDRZttMtxLOIEG52eJtun1zKZu3wOAfbBX-5-P340KJqkh-TtLXVPCnRpdIv_rT-tTY3aDT1C0V8RGhARw3hsONPJ-sFho1Px5NKkYI1umU4NNBLlRR6I6dUpTufZN8-_ArvijZ7BPaHqea06DTARBIOneWGjev3zs0n_DAYS3uF8GAJXigtU6t35Koi2jCHS1vo_lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی صبح پنج‌شنبه ۲۹ مرداد ۱۴۰۵ «قائم حسینی»، معروف به «آرین»، را در ارتباط با اعتراضات دی‌ماه اصفهان اعدام کرد. او پنجمین فردی است که در پرونده موسوم به «میدان علیخانی» اعدام می‌شود.
خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، حسینی را «تبعه خارجی» معرفی کرده، اما تابعیت او را اعلام نکرده است. در این گزارش همچنین اطلاعاتی درباره زمان بازداشت و محل نگهداری منتشر نشده است.
قوه قضاییه حسینی را به «دخالت در وقایع میدان علیخانی اصفهان»، کشیدن سلاح، ایجاد رعب‌ووحشت و ناامنی گسترده و اقدام علیه امنیت ملی متهم کرده بود. براساس گزارش رسانه‌های حکومتی، حکم اعدام او پس از بررسی فرجام‌خواهی در دیوان عالی کشور عینا تایید و اجرا شده است.
قوه قضاییه پیش‌تر «ابوالفضل سپاهی»، «امیرحسین صفری»، «عرفان اسفندیاری» و «گل‌محمد محمدی» [پسرعمه قائم حسینی] را در ارتباط با همین پرونده اعدام کرده بود. همچنین میزان اعلام کرده بود که برای ۱۶ نفر در این پرونده کیفرخواست صادر شده است.
شروین باقریان، امیرحسین ملکی و علیرضا سپاهی، سه محکوم دیگر این پرونده‌اند که درباره احکام نهایی و وضعیت کنونی آن‌ها اطلاعات شفافی منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77962" target="_blank">📅 15:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77961">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p8IfdfXULxKQu5eHS7OWBczubk-di1o1bjbhuVRSgp5f_hpO46Kw01rtzCesBNiFLsifGUiJ3sdQcYEvMQ8gvUX8jaBnxtrk4_na_kcSDnBAn2GOZFPnmTaydn7f6951cIu2YNX-ebDElZOJhbQEynLFCfsMmBRQTEZzE6qysex2Sf08CIrADC-nyqI2bIkcUZhlHfao5ILXFLkIhU4dHlb_xKCUgJKMK1zwIBNypAUWIAHO5aZsRMErqoF5uNpW9IK1Ox0dOadUeh4alpT3OdrwY5M8PkEiLyblDEmgD9lnWth6B_NT0KBLGlLScC5gCHfWy7zi_B-19zxtGt1W8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ:
هیچ‌کس بیش از من به جمهوری اسلامی ایران فرصت بزرگی برای رسیدن به یک توافق نداده است. به‌طرزی فاجعه‌بار برای خودشان، نتوانستند از آن استفاده کنند.
بنابراین، امروز اعلام می‌کنم که
کوبنده‌ترین عملیات اقتصادی‌ای که تاکنون علیه هر کشوری انجام شده است، آغاز خواهد شد!
این، جنگ اقتصادی و انزوا در مقیاسی بی‌سابقه خواهد بود.
نیروی دریایی‌شان از بین رفته، نیروی هوایی‌شان نابود شده، کارخانه‌های نظامی‌شان اکنون به تلی از آوار تبدیل شده، پولشان بی‌ارزش است و کشورشان به مویی بند است.
امروز همچنین اعلام می‌کنم که
هر کشوری
که به مؤسسات مالی، کسب‌وکارها، فرودگاه‌ها یا نهادهای دولتی خود اجازه دهد هر نوع راه نجاتی برای ایران فراهم کنند، خود با
پیامدهای اقتصادی عظیمی
روبه‌رو خواهد شد.
قاچاق نفت، خطوط سوآپ، انتقال پول نقد، صرافی‌ها، ثبت کشتی‌ها، شرکت‌های پوششی — همه این‌ها باید
همین حالا
متوقف شوند. خودتان می‌دانید چه کسانی هستید.
این یک
D-Day  اقتصادی (ECONOMIC D-DAY)
خواهد بود و ما به همه متحدانمان نیاز داریم که در کنار ایالات متحده آمریکا بایستند تا تهدید ایران را منزوی و شکست دهند.
این دیوانه‌ها به آخر خط رسیده‌اند و این اقدامات تاریخی آنها و توانایی‌شان برای گسترش ترور در سراسر جهان را فلج خواهد کرد.
ایران هرگز سلاح هسته‌ای نخواهد داشت.
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور
دونالد جی. ترامپ
realDonaldTrump
توضیح چت‌جی‌پی‌تی: D-Day در اصل اصطلاح نظامی برای «روز آغاز یک عملیات بزرگ» است، اما در کاربرد عمومی تقریباً بلافاصله عملیات نرماندی در ۶ ژوئن ۱۹۴۴ و آغاز تهاجم گسترده متفقین در اروپا را تداعی می‌کند. بنابراین ترامپ با گفتن ECONOMIC D-DAY می‌خواهد بگوید این اقدامات اقتصادی قرار است چیزی شبیه یک حمله بزرگ، تعیین‌کننده و همه‌جانبه در جنگ اقتصادی باشد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/77961" target="_blank">📅 02:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77960">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77960" target="_blank">📅 01:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77959">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JiezDc3TZPptyCCASXljs3TTRRRmD6oxL08zO1WN_Igw1A5S9kMTJ4zbaatMIv0s5NPD597VH8m1aFhd-X7BysDepBfa8ylE7LIYNCVWCdyiyiPooHFYelBOtAOkk8oePMV985zX0L0hfsGUCuGkZJ1scZk2413SMttsfaRX92BbaMoWPoz6NMqs-Kw6JPGCL-wZkYD0k9KlPzq1Ch51JNw2Wkdc_2M_ZCq4_18XnQeyxWrVcDARXhfNcOAa4aAnMGtzZ5tH9SqzbvfhgJYf3xyGQbM7ACvw8kyZbp6ANNHO5sZhx96PcfmJvRkmA19FlmwZ62_PX3F62fOBEskRcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت اکسیوس، روز چهارشنبه ۲۸مرداد ۱۴۰۵، گزارش داد، ارتش آمریکا طی هفته‌های گذشته یک مسیر کشتیرانی تحت کنترل خود در بخش جنوبی تنگه هرمز ایجاد کرده که امکان انتقال روزانه میلیون‌ها بشکه نفت به بازار جهانی را فراهم کرده است؛ اقدامی که به گفته دو مقام آمریکایی، بخشی از اختلال ایجاد شده در صادرات نفت در جریان جنگ را کاهش داده است.
این دو مقام آمریکایی به اکسیوس گفتند در چارچوب این عملیات، هر شب حدود ۱۵ تا ۲۰ نفتکش از مسیر جنوبی تنگه هرمز و در امتداد ساحل عمان وارد یا خارج می‌شوند. به گفته آنها، اکنون حدود ۱۰ میلیون بشکه نفت در روز از طریق این مسیر از تنگه خارج و وارد بازار جهانی می‌شود؛ رقمی که تقریبا نیمی از حجم انتقال نفت پیش از جنگ است.
به نوشته اکسیوس، عملیات آمریکا تنها به اسکورت نفتکش‌های حامل نفت محدود نمی‌شود. نیروهای آمریکایی نفتکش‌های خالی را نیز از دریای عرب از مسیر تنگه هرمز وارد خلیج می‌کنند تا این نفتکش‌ها پس از بارگیری نفت در بنادر کشورهای منطقه، دوباره از مسیر جنوبی تنگه خارج شوند.
یکی از مقام‌های آمریکایی که از نزدیک در جریان این عملیات قرار دارد، گفت آمریکا حدود دو ماه است مسیر جنوبی تنگه هرمز را تحت کنترل دارد. او افزود سپاه پاسداران ممکن است برای کشتی‌ها «مزاحمت» ایجاد کند، اما کنترل تنگه را در اختیار ندارد.
بر اساس این گزارش، عملیات انتقال نفت از سوی یک گروه ویژه مستقر در مقر ارتش آمریکا در فورت براگ در ایالت کارولینای شمالی هماهنگ می‌شود. این گروه با کشورهای عرب منطقه همکاری دارد و هر روز فهرستی از کشتی‌هایی که قرار است از خلیج فارس وارد دریای عرب شوند و همچنین نفتکش‌های خالی که برای بارگیری نفت وارد خلیج می‌شوند، تهیه می‌کند.
کشتی‌ها هر شب در دو بازه زمانی مشخص، در قالب دو کاروان جداگانه برای ورود و خروج از تنگه حرکت می‌کنند و با هدایت نیروهای آمریکایی از مسیر جنوبی عبور می‌کنند. جنگنده‌های نیروی هوایی آمریکا نیز برای مقابله با موشک‌های کروز و پهپادهای ایران از این عملیات محافظت می‌کنند.
به گفته مقام‌های آمریکایی، ایجاد این مسیر پس از یک عملیات دو هفته‌ای فرماندهی مرکزی آمریکا، سنتکام، علیه سامانه‌های راداری و نظارت دریایی ایران امکان‌پذیر شد. در نتیجه این عملیات، توان ایران برای رصد تردد کشتی‌ها در مسیر جنوبی تنگه هرمز کاهش یافته است.
مقام‌های آمریکایی می‌گویند ایران اکنون برای نظارت بر این مسیر عمدتا به چند رادار بازسازی‌شده و نیروهای مستقر در قایق‌های تندروی سپاه متکی است. به گفته آنها، کاهش توان رصد باعث شده است حملات پهپادی و موشک‌های کروز ایران بیشتر به سمت مناطقی انجام شود که احتمال می‌رود کشتی‌ها در آن تردد داشته باشند.
اکسیوس گزارش داده است که شماری از کشتی‌ها در حملات ایران آسیب دیده‌اند، اما نیروهای آمریکایی نیز تعدادی از حملات را رهگیری کرده‌اند. به گفته یکی از مقام‌های آمریکایی، نیروهای این کشور در اوایل هفته جاری هشت پهپاد و دو موشک کروز ایرانی را سرنگون کردند.
بر اساس این گزارش، طی دو هفته گذشته هر شب ۱۵ تا ۲۰ نفتکش از مسیر جنوبی تنگه هرمز عبور کرده‌اند و میانگین انتقال روزانه نفت اکنون به نزدیک ۱۰ میلیون بشکه رسیده است. مقام‌های آمریکایی می‌گویند در برخی شب‌های هفته‌های اخیر، حجم نفت خارج‌شده از خلیج فارس به ۱۵ تا ۲۰ میلیون بشکه نیز رسیده است.
به گفته یکی از این مقام‌ها، در یکی از شب‌های این هفته بیش از ۲۰ کشتی برای عبور از مسیر جنوبی تنگه برنامه‌ریزی شده بود و در صورت اجرای کامل برنامه، حدود ۱۵ میلیون بشکه نفت از خلیج خارج می‌شد.
دونالد ترامپ، رییس‌جمهوری آمریکا، نیز در گفت‌وگو با اکسیوس گفت «حجم بسیار زیادی نفت» از تنگه هرمز خارج می‌شود. او در عین حال گفت آمریکا در حال حاضر با ایران مذاکره نمی‌کند و افزود جمهوری اسلامی در مذاکرات «وقت تلف می‌کند».
ترامپ همچنین گفت ایران هنوز توان مقاومت دارد، اما در مجموع «بسیار ضعیف‌تر از گذشته» شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/77959" target="_blank">📅 01:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77958">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1a65b09283.mp4?token=kjqUhQVvz2X7rs_Wdj6SL0v_e8mbH4wNG9ZcL8ZlfLCXfAsFo7nwiSscz4gHsN1nWVlHaRk8GJlpaeTxjRO-9CA6fcW4Bh_mGyTl4FVZsJBRCBvzApF2yaC7lB7urQIoSwvBTnH7oUHVRuoHnXaRSi5dww7mBPLFrRrN2jv_j4w_9DRcWltM91LSyGYdWG2eEZpxFEyY4JbKhtKyGspL2Y9pPuGzuO52NnJgiQ1VkY4NbRtf3x7-eMWgxu0AxzILeeWve8l4Y0XoxUdxmAHAH8ICbvcE8RvsokbhPPpl2Hp3ahr7egsg7Np6dGwmPJm7Qcb93rmwrLMb5FKV-FfIqw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1a65b09283.mp4?token=kjqUhQVvz2X7rs_Wdj6SL0v_e8mbH4wNG9ZcL8ZlfLCXfAsFo7nwiSscz4gHsN1nWVlHaRk8GJlpaeTxjRO-9CA6fcW4Bh_mGyTl4FVZsJBRCBvzApF2yaC7lB7urQIoSwvBTnH7oUHVRuoHnXaRSi5dww7mBPLFrRrN2jv_j4w_9DRcWltM91LSyGYdWG2eEZpxFEyY4JbKhtKyGspL2Y9pPuGzuO52NnJgiQ1VkY4NbRtf3x7-eMWgxu0AxzILeeWve8l4Y0XoxUdxmAHAH8ICbvcE8RvsokbhPPpl2Hp3ahr7egsg7Np6dGwmPJm7Qcb93rmwrLMb5FKV-FfIqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
خبرنگار: وزیر خزانه‌داری می‌گوید ممکن است همین هفته شاهد اثرگذارترین تحریم‌ها علیه ایران باشیم. این تحریم‌ها چه زمانی اعمال می‌شوند و چه چیز دیگری ممکن است در ایران تحریم شود؟
🔻
ترامپ:
خب، چیزهایی داریم که می‌توانیم تحریم کنیم. ما تحریم‌های بسیار سختگیرانه‌ای داریم و خواهیم دید چه می‌شود.
در حال حاضر، تنگه باز است. کشتی‌های زیادی در حال عبورند. این را گزارش نمی‌کنند و ممکن است در مقطعی کمی کند شود، اما همین حالا تعداد زیادی از کشتی‌ها در حال عبورند.
محاصره دریایی بسیار مؤثر بوده است. صفر. یعنی واقعاً، تا وقتی برقرار بوده — و مدت زیادی هم هست که برقرار است — به‌جز یکی دو وقفه کوتاه که عمداً آن را بر اساس یک توافق باز کردیم. اما آن توافق به نتیجه نرسید. می‌دانید، توافق آن‌طور که آنها گفته بودند از آب درنیامد؛ وقتی یک چیز به ما می‌گویند و کار دیگری می‌کنند.
اما محاصره ۱۰۰ درصد موفق بوده است. هیچ کشتی‌ای وارد ایران نشده، اما کشتی‌ها برای جاهای دیگر وارد می‌شوند. خواهیم دید. خواهیم دید چه می‌شود.
یا اوضاع بسیار خوب خواهد شد و قیمت نفت مثل سنگ سقوط خواهد کرد، یا دقیقاً همان کاری را که داریم می‌کنیم ادامه می‌دهیم. می‌دانید، از ۳۵۰ دلار برای هر بشکه حرف می‌زدند و امروز ۸۴، ۸۵ دلار است و ما داریم نفت زیادی استخراج می‌کنیم.
اما اتفاق دیگری که افتاده این است که مردم گزینه‌های جایگزین دیگری پیدا کرده‌اند که هرگز به آنها فکر نمی‌کردند: تگزاس، آلاسکا، لوئیزیانا و جاهای دیگر. علاوه بر این، تعداد بی‌سابقه‌ای خط لوله در حال ساخت است. بنابراین فکر می‌کنم تنگه هرمز دیگر به آن اندازه که در گذشته اهمیت داشت، مهم نخواهد بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/77958" target="_blank">📅 01:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77957">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q3SriTp7-Ke66OVnqC44SkrT2U8osybOQiR_mEKFlcKeSM8_Jn24rvroGhZmudvNkawFWq6BJxexPH4E0xcME_iJlUrRDkLbq-Mawu260mMWAN1Es8G52TztRWCrqejQfGq0Z6SPZZPh0N6gXJYc9wlFoIUM21UCSoXMbXuZF81rQnbI4xp0mZNnVmnDHyDGhTEU-BfFu7mYUmH32h9251TZtFYY7YEgz_BPG9LO2gCZiDZQZdPDn_6D_ojG13guVESVsqqlJzycacunBVvplE2O-_ICgbqAEb_H3zrtl268zIezJI1Z3SqHPp-JexEIGnvzxGoABhBRbII_ilAkog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت فرانسه روز چهارشنبه نیلوفر شادمهری، رایزن فرهنگی سفارت ایران، در این کشور را اخراج کرد.
ساعاتی پیشتر وزیر امور خارجه فرانسه رسما خبر داده بود که به عنوان اقدام متقابل دو وابسته سفارت ایران را از فرانسه اخراج خواهد کرد.
هنوز نام و سمت فرد دوم که از فرانسه اخراج خواهد شد اعلام نشده است.
پس از آن که وزارت خارجۀ ایران در بیانیه‌ای دو تن از کارکنان پیشین سفارت فرانسه در تهران را عنصر نامطلوب اعلام کرد، فرانسه نیز از اقدام متقابل درباره دو دیپلمات ایرانی خبر داد.
در بیانیه وزارت خارجه ایران آمده بود که با توجه به «فعالیت‌های خلاف حقوق بین‌الملل، به‌ویژه کنوانسیون روابط دیپلماتیک ۱۹۶۱» از سوی دو مامور شاغل در سفارت فرانسه، این دو فرد عنصر نامطلوب شناخته شده و حق بازگشت به ایران را نخواهند داشت.
طی روزهای اخیر مشخص شده که این دو فرد، از کارکنان بخش فرهنگی سفارت فرانسه بوده‌اند و ظاهراً در ارتباط با پروژه‌ای فرهنگی، با دو گرافیست ایرانی دیدار کرده بودند.
این دو گرافیست هم از همان زمان در بازداشت هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/77957" target="_blank">📅 23:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77956">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/168f12d8a1.mp4?token=qvfQxQnCwrT0fza8CgRdzdoznbGdarsrpee6LuJ52oCVXWCj_zEPJsm-ELx2hSTuhF6UHcdluXh7Exrtc-FK2QTjQJX0XoI35auZB9o_0Q6DYgcEGiRXuZksG9c9vH7VgVomYrhS4mXPyU-vxC6_qduHjL9lWOH_KLp1zgptaPxPpAbWLrIxgd5ckoFwN3P_MaNp_ZkngFRZeoeiJMAM7gTcxUMk3RlnmK_OROVZmOnUidclrtmqzIPxe4GoAheEA6mt5NElAab_sPUASg8oaTDcCLxtjE6jTnI58AMJUP58NR-dIM2rWljN641OIfI-l30SGBinsHzsCQW5hKFgXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/168f12d8a1.mp4?token=qvfQxQnCwrT0fza8CgRdzdoznbGdarsrpee6LuJ52oCVXWCj_zEPJsm-ELx2hSTuhF6UHcdluXh7Exrtc-FK2QTjQJX0XoI35auZB9o_0Q6DYgcEGiRXuZksG9c9vH7VgVomYrhS4mXPyU-vxC6_qduHjL9lWOH_KLp1zgptaPxPpAbWLrIxgd5ckoFwN3P_MaNp_ZkngFRZeoeiJMAM7gTcxUMk3RlnmK_OROVZmOnUidclrtmqzIPxe4GoAheEA6mt5NElAab_sPUASg8oaTDcCLxtjE6jTnI58AMJUP58NR-dIM2rWljN641OIfI-l30SGBinsHzsCQW5hKFgXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ هنگام بازدید از محل احداث بالگردگاه جدید در کاخ سفید، در پاسخ به پرسش خبرنگاران درباره احتمال گفتگو با تهران اعلام کرد که در حال حاضر شرایط مطلوب است، اما امکان مذاکره در آینده وجود دارد.
ترامپ با تاکید بر موضع واشنگتن در قبال برنامه هسته‌ای ایران گفت: «موضوع بسیار ساده است؛ آن‌ها باید به‌طور کامل سلاح هسته‌ای را کنار بگذارند. ایران نمی‌تواند سلاح هسته‌ای داشته باشد، چرا که از آن استفاده خواهد کرد و ما اجازه چنین کاری را نخواهیم داد.»
رئیس‌جمهوری آمریکا در نهایت تصریح کرد که ایران نباید به سلاح هسته‌ای دست یابد و دست نخواهد یافت.
@
VahidOOnLine
ترامپ افزایش عبور کشتی‌ها از تنگه هرمز خبر داد و گفت آمریکا کنترل کامل این آبراه را در اختیار دارد. به گفته او، شب گذشته تعداد زیادی کشتی از تنگه هرمز عبور کردند و اقدامات ایران، از جمله شلیک گاه‌به‌گاه به پهپادها را «مزاحمت» توصیف کرد.
رئیس‌جمهوری آمریکا همچنین گفت قرار نیست همه کشتی‌ها از تنگه هرمز عبور کنند، اما تردد در این آبراه ادامه دارد. ترامپ پیشتر نیز از کنترل کامل آمریکا بر تنگه هرمز سخن گفته بود و مقام‌های ایران این اظهارات را رد کرده‌اند.
@
VahidOOnLine
ترامپ می‌گوید مردم در حال یافتن جایگزین‌هایی برای تامین نفت به‌جای تنگه هرمز هستند و تگزاس، آلاسکا و لوئیزیانا را از جمله این گزینه‌ها معرفی کرد. او گفت خریداران برای تامین نفت به ایالات متحده روی آورده‌اند.
او گفت یکی از دلایلی که قیمت نفت به ۳۰۰ یا ۳۵۰ دلار در هر بشکه نرسیده، افزایش عرضه و روی آوردن خریداران به منابع جایگزین است. او افزود قیمت نفت اکنون حدود ۸۳ تا ۸۵ دلار است و پس از پایان شرایط کنونی، بسیار پایین‌تر خواهد آمد.
رئیس‌جمهوری آمریکا با تاکید بر اینکه این کشور نفت کافی در اختیار دارد، گفت: «مردم دارند جایگزین‌هایی پیدا می‌کنند. یکی از این جایگزین‌ها تگزاس است. یکی دیگر آلاسکا و دیگری لوئیزیانا است. آن‌ها برای تهیه نفت به ایالات متحده می‌آیند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77956" target="_blank">📅 20:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77954">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DB4DOmg-8MZqTpp3iAtFODBu3lktHFgb5wD6yf4bkR0IuDDKJFunb7SBVgRBe9H-KU6dbZq4guYD41oJSDbfkUUcWUmS7rwO-IWwj5GKqv8Sc6lgK_01PfmgIWdajKyUB_guJwYAXDkVCT1M5POAkL2iUe2u55Z6OwLYwX7DdRuQQCoCBMqdZdQfaacdltXHBEXhTuWo0z6GGrBNZ1IX_vZ5yWXy121FvtHr392iz8eTM7T4t3o75WZEOntmtIsibAS7eXP66EZQcRgpB1ckivmeQCD8aoOgZqDZEqtsuey5rs9C1vFTVWXqzCpihrJJ1_wBZJmtMz2G8aXJfZyn4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r8UNwJ8WebNrzGtexnqfKxLOgpPU5jTMhkmG2zREvBkhM_n7z0b_H3M8ELGV0d-TWjv_Y1tcGZafZv1uq_mxQj-YvU-M8fqH-1tUv5B8jmWkxuRuHDwrhoZXhDtkFvoRLqi-O2_tdS-rVIW8Ey8goOT2Y0AJzfzYzBz0WNqSe1pRzAn0T98LBqdc5T9-HObiGnbExz-GT-TQDVTUvKOqme5vmXp8ADgOPU_kYA6q2G3W4aaWAowr4tpl3eU4eMsjk-NvsEC0u411m1MtNnvPgOTIQzRvD7-UJ50YIdQC6HuJPMbsuwsz2NwHuOVjwN29uWo14jH2ps2fcewfZbF8OA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فاینشنال تایمز روز چهارشنبه ۲۸ مردادماه با انتشار گزارشی به نقل از دو مقام ارشد جمهوری اسلامی گزارش کرد که اگر دونالد ترامپ تصمیم به گسترش جنگ بگیرد، هدف قرار دادن پایگاه‌های نظامی در جنوب شرقی اروپا را بررسی خواهد کرد.
براساس این گزارش، یک پایگاه نظامی در بلغارستان و یک پایگاه نظامی ناتو در قبرس از جمله اهداف احتمالی جدید ایران در صورت تشدید درگیری‌ها خواهند بود.
مجلس بلغارستان ماه گذشته با استفاده آمریکا از یکی از پایگاه‌های نظامی این کشور موافقت کرد.
همین دو مقام که نام آن‌ها اعلام نشده می‌گویند نیروهای مسلح جمهوری اسلامی به‌طور جداگانه حمله به کابل‌های فیبر نوری زیر دریایی در تنگه هرمز را در صورت تشدید تنش‌ها، بررسی کرده‌اند.
@
VahidOOnLine
یک مقام سازمان پیمان آتلانتیک شمالی، ناتو، به خبرگزاری آنادولو گفت: «ناتو برای مقابله با هر تهدیدی آماده است و همواره هر کاری را که برای دفاع از همه متحدان لازم باشد، انجام خواهد داد.» این اظهارات پس از انتشار گزارش‌هایی مطرح شد که بر اساس آن‌ها، ایران در صورت تشدید بیشتر جنگ از سوی دونالد ترامپ، حمله به اهداف نظامی آمریکا در اروپا را بررسی کرده است.
این مقام ناتو همچنین به رهگیری موشک‌های بالستیک ایران در اوایل سال جاری اشاره کرد و گفت پدافند هوایی ناتو در چهار مورد جداگانه، موشک‌هایی را که به سمت ترکیه در حرکت بودند، رهگیری کرده است. او این اقدام را نشانه قدرت و موثر بودن وضعیت بازدارندگی و دفاعی ناتو دانست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/77954" target="_blank">📅 16:51 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
