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
<img src="https://cdn4.telesco.pe/file/jlemP-NkJMeld-NrjcZ2hpCIXiVA0hYpupmLE_Ekvk2_dDYlNKEQ4hfwXNm4p6PGp45AG6stlAOY6Efg3HXkMLXdmbrJPsK5DoQjYwpDpkisPttTCCeBq8PxVxhhUqCXUUKc9zkglhruVM3N9gq8UZPHaeuNFs8VjPAJOeR-NDU0GYt4x_qX_GixzgbEOq2bTMjDaGnzL9TAfQAuZ-xF5QtLHiaLRYkaccLJcSDIOokOBlDDkUvL2vQPMzaVaxFmeBk8WEmimr3o2IlXc9pPPGu1XEX6kKiPbdJwpowFy3kUOWVJfobTFW0hA0Wx2oWeMRYo02kLJo5M0wlEiUN83w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 196K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 19:49:56</div>
<hr>

<div class="tg-post" id="msg-79590">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پسر خوب فیفا و داستاناش
😏</div>
<div class="tg-footer">👁️ 244 · <a href="https://t.me/funhiphop/79590" target="_blank">📅 19:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79588">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/funhiphop/79588" target="_blank">📅 19:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79587">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">به گزارش بابک تقوایی نویسنده و خبرنگار حوزه نظامی: متاسفانه چند کماندوی تیپ 65 هوابرد نوهد ارتش که از اعتراضات حمایت کرده بودند بازداشت و در خطر اعدام به جرم قیام مسلحانه و کودتا هستند. نام دو شخص از این کماندوها: سرهنگ حمیدرضا خلیلی و سرگرد حسین مجیدی است. این عزیزان از حق تماس با خانواده های خود نیز محروم شده اند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/funhiphop/79587" target="_blank">📅 19:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79586">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTaumfgjFAHwpc7KHhURTkLopAr9JhhiDkkiq3RFOathWUiUD6L85qYC-k0Wi9MRY2e7vxPsOYB2a6aSTzSoceBqZYaFqeFJOdGH1lBIYF1n-R3SVDiMQG18otGkIDmrwMF4WQKHGTcRnRx80KwRzMSrpwyCrXuEAeVx0MAV2azyioR-4BRFyIGBDjrH_6H5PvYfEtGfRWGilU7V6g1qBRSOUjKwvucPZ6CrxJCYWdF88D_nPMrmwxF_74vJ4GlqvRO3yDjF3GY5QkHKUHdaduvX1kwLjePw_YIJI9RQ6bkVbyxCsyGn2WN1NonZh2epqoJ3uc5sZgzoUgKlXuyNrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط مخصوص نابینایان پیاده روی شهرداری که مستقیم میره تو تیربرق.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/funhiphop/79586" target="_blank">📅 19:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79585">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lw5Ne6GvVrjDz35aWYqOEnNx6Prz6a5NfXuxmdULD4hQz1wRwezjxQ-6CahXO3CLWW_R3vGC9morq0j9NFjxp5ZVna4jd86rOkGXHDmdXfY6MknzxjywNPCJKFAf9kWyis9_HYigTPmEod2jH9zAOkBnAUIqGBtDwaC0QvruMKcr9mNOmdw668A9Nz31yroivHnPcIrcoiVFeEZNAhQGDlz8_G2qOfvlKzclGqPt5Wgssa6vfPmfm2ItqTKRykyedanLILgRFUuKj0EVkN90M5HYrkhn60PXGWUB2-j06aolWEBS7gFOJDPrJj7ABy37Z3n7QwcO26JRtxTBTaoziA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پیدار به نام “بریدم” ریلیز شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/funhiphop/79585" target="_blank">📅 18:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79584">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgH1OGSZZEub8WcoHQ-mgGUtA6ABaDh_wfmHdkmrG5VLDzUZ4zCJfjSvM7m6RqmKyGxgIE8wTd765-DKS-CvKYC0PzcHZDphdcWQar54CQIx0dLl_GSBKVZdeiGiW5xoylFTPHkxIMj7D5jYGedGw1qwgWXat-9sdk6Q7IOU1jZMZAtOhTECtEI9JtBXNzYq9LWFs2YLcrZh8dwKMZxI-EKvqKu5gNI2cmYovXB_-dIkYzdyzgTWZMA_fnFA3EaCD3rLpSXiBGlKYgbiICSNKCFCgiPEmJvU5tny6kvwysWMcRKcDZfDYfuuYIKds97elD3CH1WaVkOFZa-nPjy4KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار: بغل لامین یامال؟
کریستیانو رونالدو: چیز خاصی نبود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/funhiphop/79584" target="_blank">📅 18:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79583">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-m_pA8_D1UndlRvKk5L-gevBslHM-MS-wUqT7gsBgmF0TlhlotoAFwQJ16ApGaAzAbylj8ZHAnIM_lZOCAt7FiwGzYcRfVfTpAslaEEcIBTiculkpQ8bU_FOdibkXLVY4GJC5k6SorO2R9n2lM8De5WKXNJvt-PSuM_rwrNZ4S02MOH92clfuNCzvoa5T9kxVpt9isscugw88Y0mJt67Ar5oe5GPBM8eUFPK8QmQlXJle3Wl6Y5oOec3dZyWyZFEH5sE3v_b1ipuKnOkLzl-JOS4dg4LYJfz1FbO_8Me9uSWB-4eprIvQKlbQG0p0mabajKAMTVyslO4EL64yHMCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا رونالدو کاپیتان تیمه موقع باختا اول خودش گریه میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/funhiphop/79583" target="_blank">📅 18:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79582">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⏩
دسترسی به اینترنت آزاد، با ربات تلگرام بت‌فوروارد
🟢
🔥
با ربات تلگرام بت‌فوروارد، هر روز جدیدترین کانفیگ‌های رایگان و پروکسی‌های به‌روز را دریافت کنید و در سریع‌ترین زمان ممکن به بت‌فوروارد متصل شوید. کافی است وارد ربات شوید و از بخش
«فیلترشکن رایگان»
، کانفیگ اختصاصی خود را دریافت کنید.
👍
همین حالا ربات تلگرام بت‌فوروارد را دنبال کنید و به جدیدترین کانفیگ‌ها و سرویس‌های فیلترشکن پرسرعت دسترسی داشته باشید.
👍
ورود به ربات تلگرام بت‌فوروارد
کلیک کنید
@betforward_bot
کلیک کنید
@betforward_bot
R16
🅰
💻
@betforward_bot</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/funhiphop/79582" target="_blank">📅 18:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79581">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0addb56dc0.mp4?token=vaNqDLwS3JXa1hFp2xPQgDoDXTn4b57lPZNegQfSXBKYIi-UMEz8_B2n0b-mp_dfM72xwibUBy7FmnZkIteCNN1G-noOr-j4XpFrWk-v-1oEloBFFFLlLtLdgeRHTDWhD7xFRFFqgPGquB8QGY4-EZCN1dFJss7HpWRkuiMBrJvdHbTO7yq0z59uNanFnz0MfDDPe18rzSymqVbhAvxdop7nc8YIEmA9POLsSvb1BTnBoQTRdDKE2F1ss0dlXPgpyQ8RknD4AVJmfEq8vg_XiFAwc5FO2IKFznouAYpnUjJqlLAuZfMHdCjiWhw_nVqs-CoGrAXQS8bLKgDnmer_WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0addb56dc0.mp4?token=vaNqDLwS3JXa1hFp2xPQgDoDXTn4b57lPZNegQfSXBKYIi-UMEz8_B2n0b-mp_dfM72xwibUBy7FmnZkIteCNN1G-noOr-j4XpFrWk-v-1oEloBFFFLlLtLdgeRHTDWhD7xFRFFqgPGquB8QGY4-EZCN1dFJss7HpWRkuiMBrJvdHbTO7yq0z59uNanFnz0MfDDPe18rzSymqVbhAvxdop7nc8YIEmA9POLsSvb1BTnBoQTRdDKE2F1ss0dlXPgpyQ8RknD4AVJmfEq8vg_XiFAwc5FO2IKFznouAYpnUjJqlLAuZfMHdCjiWhw_nVqs-CoGrAXQS8bLKgDnmer_WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله‌ی عده‌ای اغتشاشگر و آشوبگر با سنگ و کلمات زشت به دکتر سید عباس عراقچی.
تقاضای برخورد با این اعمال زشت و تخریبگران اموال عمومی را داریم.
#منم_به_این_مذاکرات_اعتراض_دارم_ولی_الان_بحث_بحث_سویا_و_ذرته
#منم_به_این_مذاکرات_اعتراض_دارم_ولی_به_این_مدل_اغتشاش_هم_انتقاد_دارم
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/79581" target="_blank">📅 16:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79580">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8hgdi215uTnrAjOBS5uO726TE_XMII0h6qV30MAuarlxlOJgb5aPXPRNzVH-UhQR8fMzjEzbfdl0f3QILv75DC3Y0PK_gQBx3f_ERnA7feNkiOUFHVMjuSYSckkZuFXKw_huG3nWxN0h_5DFo-Y3ViQ49nHL8ggbfPWgXpHOXoFRST9FfOWtRTtqBWlwu8LXO7tnf1T411D9Mf2chOp09nvJjGAfRpaDYapR2m7rV-hdZLF0DLOFuSGgo9nkK9R2GTZaogSU4F466x2OIF7IF2rEtEGUXbz9kZtPRw1lcM2NaG8t5at_Qw7ImBR6b3NpORa64Cvuum87WgKUjOkKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ازدحام پشممم ریزون جمعیت در تشییع جنازه خامنه ای  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/79580" target="_blank">📅 16:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79579">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeK4Ytxp9A8e0e4y754jo4CZJWdJ3wAx4hjVHC0owSr-xKbvibJla_R-LXZLsVrmvMPprWAeIdN1eE8_yuWOQS72WV1KvyMq3J7jGzpOS57stKvmHOqQOuOemLl4psmFYwu0lHoJvza-BavyH1_eu45mhwvlhFoAS0C97D_TjiVNTjZtraEG5HKum_PmlJSuOgz9ebhMDS80STZtnBTwqSNg-zyo4JFVpH1hr1DsxyJ0xXab0hwOSCthjOnPp_6ifiSjg33eGLyDhrM02RU7q5abQTPx8EuQecqieEtyR9YdhZqMCF7ZMv3to5wCijE01m4KdrmW1TstrxDRpmscmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ازدحام پشممم ریزون جمعیت در تشییع جنازه خامنه ای
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/79579" target="_blank">📅 16:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79578">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یادش بخیر ی زمان هر چی میخواستیم هلدینگ میخریدش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/79578" target="_blank">📅 14:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79576">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iOHdwQZqJWeoZtzmuXkgpC3B65c1rzwMQzvXeRaQgsGfIoRWw-XvwLwICc49xfq2g44xAaVtuxr41DyF81VX3Q3IfkVAqPl0H2frvDjJAOpclb9VA8bc2Y6w2lsHqBqKf-mXahtMS85jXhtr6rGEq5h-QVEJpW2U2Fsl6gyWHa1M3HqHqm7SyLdgGx56RoyA3SS5JbyEJvy_RSiaAXT2Xs0mK3pyngO16rTb7XFU2VKbPP3bjTx_qNNGO0-diO7Ov-2rqEq7eCNuj60iGOfZZc2fD5bXhkRRnmmS911Ur0eEwaLxVeFbhWjH-ppUy9MUOtLaf7X8_dE6CqJqFK9wIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BblbHHBK9K-5du3sk3x1K6SJiLv4viId_in8fpobuJIO-0aPsX9XPPOsPxBRyU6wyOdqPrt5PmsMSbSaQHRpi-TSH4pPI_zCIWbSrK5nTCNLYqTEsnbbgHrSwN3UTj9twHNDdnafSgPe69xxDPweWR1JmSUZPdQV7fb7cOsRWMWgVKUnyrIlIPd9mfmfdAADcqVOPNtBTEGeY6pMKmRBVrjPtySkuO9UnTUmssjxn0dax8yEWyTlPfsa5-SG2oubnC5ahNsNGLryc1Twa46din_hyujxhgBPpaNHrtKHvlYVNsIssHJohoMWzZGvEmpC-O2s06myA957Ves06gnLtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیوید کیس مشاور نخست وزیر پیشین اسراییل و از افراد نزدیک به موساد:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/79576" target="_blank">📅 14:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79575">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ویناک بلادو دوباره را انداخت</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/79575" target="_blank">📅 14:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79574">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O87moylNzYldv4tEhn4cxtmlxlB6R0YOAGpwwAWOtxzJT0Z8MGe7QJzwDzasMbLTk_GnWa9eFAIIMjDUzPjWQAWvbGTM-txUHEY6aUeGNitU-QAJYwI8dOybpdyA-zHDA_lrrYka1ICvZK0IgxOXAnP4ceQScXWRe2ixEA2fSwVY_MLTnNeIvwC8eRWC2s_KYzKAYuIB-g5zGPNCsMhjxtl_OOYVG8Iv1Ar3NZwJmRzF1xC3l_myzIFvcsm9rP2wcEs-BEQYD8N01gJpmj1GHynGvX4tPC91sbgRTzEwbSBMQ5ErGxacTqbmxxdgYXjmjOvF4gyW_pnf1yUTN4KD0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی میتونی با کلاهبرداری از ۱۰۰ هزار نفر که ۲۰ دلار دارن ۲ میلیون دلار در بیاری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/79574" target="_blank">📅 14:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79573">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">هیپهاپولوژیست ی فوت فتیش دزده که بعضی وقتام آهنگ میخونه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/79573" target="_blank">📅 14:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79572">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ویناک بلادو دوباره را انداخت، بنزین زن دکی هم عضوشه دکی لباسا و کارت صدا عمرانم برداشته نمیده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/79572" target="_blank">📅 14:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79571">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jK7lkSG--_ZAPBb5efUFhf_4iutrqacnli74HIHbZ8nf2p7dmFdizX4zYjhiwSFWB68k3AsGrEhPr1AtY0O1I6svoCuWadb1bH9oZj0Ga6-a-r_foyst3sfrB4L8oBYoZYSKOuo6Sx7lvT8bBHUyMdL-1F2cJ-88aPnmVGHNg00JWF014vhasCEnz_FWVEYdWFVokaVNxf2JMLUQPhnBpkSnBoK-LvH5Y4uBBGvNlxt-p4_qTHI54vWrQ288xze8jpm600_hb7LyWC7GNx5FMRFsw9diKglfjpAMbKGratZVP0E892K3ju0vKNGJopY3IVb--CLpm6AC2IxewEqVVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک بلادو دوباره را انداخت، بنزین زن دکی هم عضوشه
دکی لباسا و کارت صدا عمرانم برداشته نمیده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79571" target="_blank">📅 13:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79569">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glAjdqjOCwzHcS-t4p_QFxbrTCjuabM6JgRvzn-ngRAsS17AmEiRWZ7yuQEl8oUc_vpMi12MvykQKiBD9cpjlh3RRZEmLbuUnmzfjwtnb6ySTOcFEc5mmOhvPclfGq9kkGNuBQwtwGvfnbqTdO0ATRHJR4TIHCvmEjoKvH4H3HtCStlwEvaX-gXInAZAD7r0-qgkRqI4HX5kByA_rk2bXTX3XZt8hGqvsFRtb2EWyyptMIn7CNkqGGap2bBfvjlYDWlaX40D4IODH7xXHOV3pP4CsWBViWO5EepfHd_rdq3Mw7THvdzGdLECO56boTtkQFvk3313jX2G00wnyZnhgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق این نقشه باز هم میشه نتیجه گرفت که سمنان چیزی جز یک تئوری توطئه که ساخته دست دولت ها برای کنترل انسان هاست، نیست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79569" target="_blank">📅 13:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79568">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">امشب سیریکو میزنن
بماند به یادگار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79568" target="_blank">📅 13:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79567">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qv_yaMIG3nHJpVorqMEuXH1JRqPM-7KlUO5r4k-a8CdeqLdDF5OyHk28nQseAtNQR801ToNSaQW0x0168-BUoGd5YU0CK8GZyw-rhlhBA49Qv-aGToqb2az8EvEjOUeWoEfRD5Yfbq8XPn-VRR9s3ow7Y0ui-c328VoFjOoPp7oP8qsRsWiGuzIUZHgYk582x2i2jJv6ee5gvQbLLGgebQ0e7lUpO9_00Xo3pKy_aHoM3wOKslyXU9LtY1OGmbPaHxsX-DQXQZRAz5jSqRDZRMH7t_pXP2xrR4Q-mKabmTjq1ZsNDZhNqjn-BkTQRiez3JDvrSXFyl9AAdsbFPMxOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من که میدونم مارتینز مادرجنده از قصد باخت ولی نمیتونم ثابت کنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79567" target="_blank">📅 12:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79566">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">امروز تا اینجا اتفاقات زیاد هیجان‌انگیزی تو خاورمیانه نیفتاده متاسفانه.
فقط یه سری آدم ناشناس سعی کردن با ترکوندن چند تا ماشین روبه‌روی هتل محل اقامت مکرون تو سوریه، مکرون رو ترور کنن و سوریه رو به دوران اوجش برگردونن ولی ضریب هوشی‌شون اونقدرا زیاد نبوده که بفهمن برا ترور رئیس جمهور یه کشور دیگه، علاوه بر تروریست بازی به نقشه و برنامه‌ریزی و اینجور چیزا هم نیازه و متاسفانه موقع انفجار، مکرون اصلا تو هتل نبوده که بخواد آسیب ببینه.
فرمانده‌های سپاه هم دیدن حواس باقرشاه به مراسم تشییع پرته برا همین دستشون خورده دوتا کشتی رو تو تنگه‌ی هرمز فرستادن هوا که ضمن تبریک این پیروزی بزرگ، متاسفانه باید بگم که اونقدرا هیجان‌انگیز و خاص نیست.
به امید اتفاقات هیجان‌انگیزتر در ادامه‌ی روز.
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79566" target="_blank">📅 12:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79565">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnuglonPyEzZ4FmfTxVrLpb7swxYwGoCk47DEpkTtjWhdBbpbmUeXYixuq3JyRml4JxIq4gh437Y5opth2s2KsiCQZGSAS3kG2-UC65OxINTU7l3FedVzeS7KP2UmcObxP0EevP-fzy_VnVXqPiyBliV6UGcrPRSv_FM7Y7ZhbIjWzWniplNJzvV9yKAvtL0OXOkZd7ReFeyZhbB04y_TI-TEQoEEYFhH59yYefRW0jN0KGGBWIKsbHuOdKqeB8q9eN2RZjJfPWlLfwG6Rn2oh_FpX98-trse-nGNQczg5T0fES1xl-q7PBw5MC_XDVajlyO6ViKAhpAmNyrU3Vy0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده شدیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79565" target="_blank">📅 12:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79564">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اینهمه به یامال فحش دادید گفتید بزرگتر کوچیکتر سرش نمیشه، تهشم همین یامال بیشتر از هم تیمیای رونالدو به فکرش بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79564" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79563">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ببین تلخون چه موجودیه که برا اولین بار حس کردم ادرویت کارش خوبه و بهتر از کسی بود که باهاش فیت داده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79563" target="_blank">📅 10:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79562">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFWpv7ZUxS9SCXtBiowiymnH24X4GPQo9KogP4OnskzRMGJGea-PZtxp-_QMSU2yRhZt7eOMAzO0V4oOP0gSc8KphJ7Ga0cpTnKm0WhtzJXMu_aA4YHCetICOzAQaE6MqfY7V4rBI9Ql4j0R7ACZWpLghVaEShKMtq2BbJE1wiH-JI9suIHMm6IBNdyfdx0YppIqk9WPxCoZvnT6H7PzxWX1ByktQl9mztQfRcWjQ-fwa-mrKCRuI8muGRWEGMdB1A3XLhDKTcA7R5t8nKSVgELNH7x_d805cc8vSoStOSkYQF2msqGvgq2G7W27pkbzBfkDbMvUaGj6aWBUsCXQig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این رفتار لیدر طلبی برونو فرناندز که حتما باید خودش همکاره تیم باشه بعید میدونم منچستر هم گوهی بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79562" target="_blank">📅 10:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79561">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⏩
دسترسی به اینترنت آزاد، با ربات تلگرام بت‌فوروارد
🟢
🔥
با ربات تلگرام بت‌فوروارد، هر روز جدیدترین کانفیگ‌های رایگان و پروکسی‌های به‌روز را دریافت کنید و در سریع‌ترین زمان ممکن به بت‌فوروارد متصل شوید. کافی است وارد ربات شوید و از بخش
«فیلترشکن رایگان»
، کانفیگ اختصاصی خود را دریافت کنید.
👍
همین حالا ربات تلگرام بت‌فوروارد را دنبال کنید و به جدیدترین کانفیگ‌ها و سرویس‌های فیلترشکن پرسرعت دسترسی داشته باشید.
👍
ورود به ربات تلگرام بت‌فوروارد
کلیک کنید
@betforward_bot
کلیک کنید
@betforward_bot
R16
🅰
💻
@betforward_bot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79561" target="_blank">📅 10:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79560">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">عجب یک چهارم جذابی شد ولی</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79560" target="_blank">📅 09:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79559">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بلژیک ورژن فوق تخمیشو برا قلعه نویی گذاشته بود
از بعد اون بازی همه رو درو کردن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79559" target="_blank">📅 09:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79558">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سلام دوستان صبحتون بخیر
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79558" target="_blank">📅 09:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79557">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHExtvZ9Mt69LWPsMyEWHb3SGBNy_aZn1AsMDo0ZsE8eQyw9la7ebVJjpd1hPCZGFmBCwFWWyfWRyJ9RNCQH_woNjzAYjESKEFxKLva2tbWRyoaVUSud7ALO7s3LAVCm0tAvZz_k9fAGvHnOG7ArBB2a-sO_9xMXGCjMN-BITMz-r7-trYQLxgpfqXShtlR2I2YTMKbls7TXDq1J5MqTyc8ImcKEImp_TiKcSRBwWpeP15eOBMeuuHRzbot8qb2QLjGENs8TdWWo9oBKbk2Wmcud0o8nSZdiXZJhtbGGUlwKxdIqZ9sC-luPSnAY-aOyAFZB4txvG2FPcWKHE4aupQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ذره حرفات به قدت میومد هم باحال بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/79557" target="_blank">📅 02:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79555">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tWxgxblhojsSx4_sDydGPDIA2HwX359kVdX9yhXuvTBnAs6An2QTa8DUERCMYIyKkVGWCZhcABRkvnhaousnnSULFQn3JV8tfPNSvf49USOjtt_W-kTdMlsBobiH0jVnMFLWNhQRoXMvEmGcY6PoANWZJq1jqVMIqWp9NVXiUxN8o9ffi2qU2vCDNOeIa70WWYwbHYz7CWTgHcPCoOTYlaAy6LcffmsoiJyUXha_aWxJu08iPuUZUrpJ4AV2Ybf_Kv81aG-WuL7qYmYA8UqNQEdRJlRjub7qLHnpg5HgSgUDoFQZ3-u3DCxUBShsPOf_1XNF2vdsSknr4C0X4pfStA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfiv8rhi8IuAplyxVgIWZtxTKSTklIcg6ZuWWtlhWXEfLmHNDNhtI_fHMgwau-zpOmTM04POuCiWw--10wiRJj3Bi7QkFFY-Glj-I4-tdsV_UiP8wE94wl-pt_bWsPNtXHa7qylEEJG_wIRWPESjJ5DsEqMlFN51q7GTBovHnbMEIYCf7UX5JPVa8w_wEZ1KPOoNatrO-vbZXk-FqDaalSYZhMr15Pcn5u-mmVEhQz5lXOSBVvrV2gr29qwJAH3dteU49jyZiC4xg5qFdfOufR7WfN72QNMI5-JyVHG9n5i5icdBcFCTqduQWuT7w6uP8ZZzaN2qoD15Kd5V3rn7Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فک کنم دعای خیر زید یامال بود که بردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/79555" target="_blank">📅 02:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79553">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دخترا پاشید بیایید چنل دیلیم دلداریتون بدم، پسرا میتونن برن بمیرن  https://t.me/+q5Ml6Hl1Af5lMTI0</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/79553" target="_blank">📅 02:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79552">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دخترا پاشید بیایید چنل دیلیم دلداریتون بدم، پسرا میتونن برن بمیرن
https://t.me/+q5Ml6Hl1Af5lMTI0</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79552" target="_blank">📅 02:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79550">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0585a7a92.mp4?token=ok95xaTKysb6vzOJwVD00G3Pj3AR228C81_6KlLBuWdxx3rU4OqxZKnMyuEhCv4nINDn6aiG89AfVEmOsBKCyqlO3Sp7ukYP6FNhP6ta5ofnIVCk3z0dAitNZ2IjOl58K3yBmZVW-5YLy5UcnhCX2s4D_LZPQrhFHtrFaQiC_-JgbX42OQteOXG89Gi8XxGnRG9t7ST0i9pzwqVLcs__2G1-CxmAaYDRmLkeu0DDW7tCwWz6u4DBhSQQf2J40AtvSz08oU-r47Q7YJsJLXwnDS7tf_5OQ0I3KPlXazViEGoSAORDov7uqsZfguwTELhFWy2XKGDbgBsfWobB1JQ6zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0585a7a92.mp4?token=ok95xaTKysb6vzOJwVD00G3Pj3AR228C81_6KlLBuWdxx3rU4OqxZKnMyuEhCv4nINDn6aiG89AfVEmOsBKCyqlO3Sp7ukYP6FNhP6ta5ofnIVCk3z0dAitNZ2IjOl58K3yBmZVW-5YLy5UcnhCX2s4D_LZPQrhFHtrFaQiC_-JgbX42OQteOXG89Gi8XxGnRG9t7ST0i9pzwqVLcs__2G1-CxmAaYDRmLkeu0DDW7tCwWz6u4DBhSQQf2J40AtvSz08oU-r47Q7YJsJLXwnDS7tf_5OQ0I3KPlXazViEGoSAORDov7uqsZfguwTELhFWy2XKGDbgBsfWobB1JQ6zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شب بخیر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/79550" target="_blank">📅 02:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79549">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEliAS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoX9HJwO5D4QrwccaQyxIEe9Ao2FVptB7aJgXyUYabOrq-x4SChypWhD9fht7U0fowCurfrzs4mZXAvdfr87Jb1Bfd3GDOz0Fg3vVu_WbLLxQfNblJ-ue9ZIPJ-C7Qq9I1PuU_OSAFSDikDQHzu89yh15QpLrYBkJa31Rzhjt6ULovCutFjDjQXvVLojJKrKHA74-iW3wD9K7UbxjmRrnn6bef4ZTwYJYK_hTP80pdMa-rkMAfNH7aGVHxJhoAkO283d_V9v5gmmolNV4_haOxZ2Ru1fQfR-BYys4s6Lw6EVjdHTJoCa91MxJ3VZv4nVW8_VEqhRd73zyIPfSw8IPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعصابم از تیم تخمی پرتغال کیریه پاشم برم فیلم ببینم:</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/79549" target="_blank">📅 02:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79548">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دوستان رونالدو فن نظرتون با خواب چیه؟</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/79548" target="_blank">📅 02:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79547">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رونالدو باید بقیرو اروم کنه بلاخره سه تا جام جهانی بیشتر حذف شده تجربه داره</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/79547" target="_blank">📅 02:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79545">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHadi(idk version)</strong></div>
<div class="tg-text">رونالدو باید بقیرو اروم کنه بلاخره سه تا جام جهانی بیشتر حذف شده تجربه داره</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/79545" target="_blank">📅 01:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79544">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaueZdQax4uzvG-g1Lqx384cOjXMWr4KqNUNH8xBJbFM1I3CHvF0dyO1ShRy-63XxIXSL3XuzRq07ie02rD4pXKNEtPXz1hCy8Y-IZIz5X5GOmbEkX70z3RKMHcXzAZUTVaDZR5AfazHoO9JmnV8hv9P-o7RO9iLjMa5bpHzzcjPvxwxTAigJkj-adAGt9J7zedcr_S_vhDt2rqq3OkkZm-MNLSHeVpHLOcYJwZ1obuzGOU85iuPC0qKL_tIbPxzoevfLjiorwxDw6pwElyzh4x2cw0fs_5f1n3ReEpKG9wwugVl0lBqOYgOvvvamNh2Wensrz_tCSk-v6jdeK_rFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یجوری به بازیکنا پرتغال فحش میدید انگار آلوارز و مارتینز نفری ۱۰ تا گل زدن و مسی بدون گل و پاس گل قهرمان شد  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79544" target="_blank">📅 01:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79543">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یجوری به بازیکنا پرتغال فحش میدید انگار آلوارز و مارتینز نفری ۱۰ تا گل زدن و مسی بدون گل و پاس گل قهرمان شد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79543" target="_blank">📅 01:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79541">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aylktyUTVtbRwmrugHu0sCZ4_SXeLG0YFRwfBSmU0Kvfefege5g76vMD_USrdtnOMjzRx0-1br3TTVqVVuDANeGj-DxIZyhDl0rexxgMw6DCnlibwBuPtupL8TtfbufQWWw-kBw0aq_zT_Kknmveb6kb4pucCYTlnH7YtgEhU03-W7bJWY-b9mLGge3alfwqwmFcE_SqqldnmGdPbcBzTWA8IAiS2LlDDGguZEJu5DLSivNHEFi_L57qps2vEIU1t46s2pEHy07ylD2K0lk5seFxUlLy1Noze5A8D-YXfV8hDXTOwAAdLuRRV2QO7RDSuTUisGDg_MmbqVqorqpY3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیاد گرونم نیستا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/79541" target="_blank">📅 01:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79539">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شما یادتون نیست(منم یادم نیست) ولی اسپانیا ۲۰۱۰ هم همینطوری بود، خوب دفاع می‌کرد تهش یه گل میزد صعود میکرد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79539" target="_blank">📅 01:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79537">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کاربر Mmd به ائتلاف تحریم پرتقال پیوست
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/79537" target="_blank">📅 01:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79536">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMM_UbqHaqqnQPIdOEwjtb9vOphGyO2b24Bn51UyqxakUqcAtjOb6w7J3OblKSjShT8w6G9XEV-qbLjVHXHlJT5Cb9CTKKtzXExIU3JzOleFlQIEV7k5T5LBnhwf9N4xBQ3X-8ewLvSxzeKH9Qde0WOxZ2doBNbo0K3uHXlhxvE1MiUkcdSCVSYJWRO41KkDJOxw9LmVy2Gt5J-s8a6HI6h1EArnQQI5K5ezaWhsSQI_SGro68AykhmGZI-WQF9kjAIdBdSfeED3hK2ZP8FaODmOUACtL4c2bA1B14NEntKi6phGzU89nDGVE8bX-GlJJCa6Kd6oy5-zefGoETGC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا داره مارو میکنه
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/79536" target="_blank">📅 01:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79535">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رونالدو بعنوان سرمربی جام جهانی میگیره
بماند به یادگار 405/4/16
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/79535" target="_blank">📅 00:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79534">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPmxyNHnMwtNrV4fNNcgJPnGKAwk7JLCOK-ngrQVWsYUFzch0VXtzaWoC2Uo50_o4vVnDkf-e4yK_YeZkkSqPNM_rfN5CtuGS3OXz7NEYvhvnrhfc0pK1BHG7eGVX-P6qgLcrba5OPk0DV1R7njao-KKCMksy8hwXO3D_oWEXHKPUXHhQKyyWDw4cJ5upNZsbqZWO6KzEqO-BHGIQiu2ACune2dsZuW3UP8QCsWz3ITrKz09zENAGpCrFPCCYSXVXZSc5xVqEn2zL142xO2v5ghR50KVwbNgP24ahULT1WYSBzsrw9sexL9hgSoOeHquAsDd6Kf9gv2xwxp9j8vZ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا ۵ تا بازی تو جام جهانی انجام داده یدونه گلم نخورده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/79534" target="_blank">📅 00:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79533">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دوستان بالا برید پایین بیایید مسی و رونالدو ۲۰ سال تو یه سطح باهم رقابت کردن و الان دیگه داره تموم میشه، با کوبیدن طرف مقابل شخصی که فنشید نمیتونید کارایی که اون یارو برا فوتبال کرده رو نابود کنید، پس شل کنید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/79533" target="_blank">📅 00:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79532">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">عزرائیل فوتبالیستا داره در خونه تک تک اسطوره های کودکیمون رو میزنه، نیمار، رونالدو و به احتمال زیاد مسی هم بعدیش(
فقط رامین رضاییان مونده
)
جدی جدی دوران طلایی فوتبال تموم شد</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/79532" target="_blank">📅 00:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79531">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8fDRp9NV7qfiQEzB4zEBv9hLyYC9UC0VpZhdigOE8kujbo6RuIrKAbpFJFqGvN4kVXSBCTW95ly2e7tw0NGFrDp_Qzpe1fY12rg38v-p7W39bJT13ObDuv_U8uX2s8vmt7oWdoq6J-kBQ_wfVoglxGQ8CooUwS16G419gXiCELOil55NFZi3oDeiQExx988NeIf1ajoTYpdAdURzpDgZpaS8kFs-aJVf9fHV5mR-P9XNmvqTVyQKdwUCgs73qoauLoQfYVDNbU1IoHcgN-_He0YmmMYECFGawEuC8lP9pLSbExlYWqGTUo4fiHHvTdfIHfn5L-7gY1ntqUM7e5UBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/79531" target="_blank">📅 00:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79530">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rK6H_Ibjg9PeSzWKx6tdxZMB08aT19rZLldgAsxLodXoiDJyRY13W2rqumuqnxRJMFom8094TiDpvQXKgANohqA3mRZekTPwTM8imZrM8xV2ld-mfcpHpk92QZsokrXNyKR2uAAP_Tz0-2ieI99BjqvB4v2abXa-6XRu6Lcqvoney7c-KQx3QJ1HTdtJL1OwnLvWiV7F0U5NhixpYaAioAIdJQLYpqDF7hqrZS8_5MQ384xmT8IG5F6eRqVksOyb9oqfbjSv-F0SgSpp6HGq4kTIGjbvrzbmY6gJMTlHAEaIUxL3YCwiSfwy9W1eokxWdq6SgniVOMMVXKp4d9e2bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدای تمام شوخی ها و کری ها، پایان ۲۰ سال سلطنت، ممنون برای همچیز و خداحافظ برای همیشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/79530" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79522">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beeb485ed8.mp4?token=CKsk6GGKNW-DjzWd55kUtOzVj57afOT8M0Xg4ropi9EdLuJBCclhI2CL7HkEK-L4cLKX7Phuxeo9SKwhhYagSP5XFqB0STzEzBNzxSLHASppiBBPzRYWuvQiilBbQN84bLrS78axQXjd4HUGNPpU8cuIGFg_4NP75-jSKVHaoSyimcYsW0daXVo_GweNe4mJm27aqrITz9gKwFolakr0TfJsWzRnPtLm3vL1Ei_SXEKdZV6jWkhR3ifHdX2-gFmEd5Q946rPDQC9Hf9SWaP0n0K6Vuyg2maZjq00Nci8sd5d8t0JfPwawZkGJayNY4eEZiZiR8T7gs_DLIQfPT8vsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beeb485ed8.mp4?token=CKsk6GGKNW-DjzWd55kUtOzVj57afOT8M0Xg4ropi9EdLuJBCclhI2CL7HkEK-L4cLKX7Phuxeo9SKwhhYagSP5XFqB0STzEzBNzxSLHASppiBBPzRYWuvQiilBbQN84bLrS78axQXjd4HUGNPpU8cuIGFg_4NP75-jSKVHaoSyimcYsW0daXVo_GweNe4mJm27aqrITz9gKwFolakr0TfJsWzRnPtLm3vL1Ei_SXEKdZV6jWkhR3ifHdX2-gFmEd5Q946rPDQC9Hf9SWaP0n0K6Vuyg2maZjq00Nci8sd5d8t0JfPwawZkGJayNY4eEZiZiR8T7gs_DLIQfPT8vsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/79522" target="_blank">📅 00:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79520">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/79520" target="_blank">📅 00:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79518">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKVatudk2AskUx2d23FGeV3yTMB-CA-BtvkmG9D8d2GywFUEwbV8nT0AqYdDXvLGwErXOtEfaaJ6mVe1hc_0jOLUKpDiDYgVVoumyHwvfxwrvB-l4Su9eRCF09HiJMZRZkVnQe9_-Vdy1v7_wF-lDfy3HvpSM04yGd9caUmi4ofK-r958z65RGhCSwQjf5fAzry0iG7XnpCWeprHUfIVQd5HRTCkue-RMxjpYwFETkmL2pMV08IWj3OlwibosVbmis_8wtHehMSdamdysm5agUGuqghkvGUCcVAZ0zEaHylQmZJAbyAvOFkdHqofTNjXQ3Hiykpv_81cWsPI_5j-sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرهنگ صفدر سلطانی جانشین سپاه پاوه در مسیر بازگشت از مراسم تشییع علی خامنه‌ای توسط یک خودروی ناشناس منحرف و دچار سانحه تصادف گردید و کشته شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/79518" target="_blank">📅 00:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79516">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یامال داره گرم میکنه بیاد تو زمین</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/79516" target="_blank">📅 23:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79515">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بابای یامال مصدوم شد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/79515" target="_blank">📅 23:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79509">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wAdk0hYeHu7uViUfL2xXG3R052J1Pxp73nGIg4AZWLR6LHJFMwDnlnICrf1VbcN4h84s1xWFqfXZ0AJamvQ-L2NpAag5sx3_nutOPlNRbxS3yscGR4vKzJhxmlyVedF4LyrzX7QcDBl6-NKpEXVlsFkKnTB6rNXi6bX3mbcW5QuwuTysbUqUyUBYUL0OTaTPpKkJEfjdItz2J0N2_uGOwrBB71BsbPGGcbDv8sH9anPYXQyyFWsQGv3cmosREvM47_THeF-pI2JeiMjEsIFUtS8JlhcEdN7BY9zNpbVJzshvDmY1hbnO9HahU6UVzo3ugDYzyTmxfDUhzm2yGsh6pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NP4cg-o6HVcgFmq4bUa4ngGQoZBm8RqQ4EDYgJaIu1YD2gOijQFF65Wyda8CqemeWPYbiXXYHBHGrAiV1tDRnqfrraTA98FACglcW02BU0wEMI_xfQ20ioZLfg6m7rcEqizES2Oriuh7tgv1d9AQT5SANcZEW8IqN-IN1PlXunRleo19JwzRtB_iwKIWsvjEAXGWc9AlZUeTL9h9EcVSAe_8g-KqZUBWUTCFsnMbYQxWWwSWy3UcW5p9NSUu5rpKenAnjhxhr0dj4JMPZdrCSuoOzd9XCU9hS2NvxyB1DzUWTd_mtcjvZpybLslR2tYNFJL-mKFueqNriDNaRfWSlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خلیفه سوم سلسله عباسیان هم امشب داره بازی رو تماشا میکنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/79509" target="_blank">📅 23:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79496">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">امشب حتما ی تیم صعود میکنه و بازی صد در صد ی برنده داره و ی بازنده و احتمال خیلی زیاد هم بازی گل داره.
بماند به یادگار
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79496" target="_blank">📅 22:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79495">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbUXVc0m7Cl4wmdgBuzB8LNo89vqrfdYQ-wx3OTPALuSFHeaTF2LKM2Q0LpBYmIRu7rjVN2wX5qUq5Z1pnp_JL69SSDDA3Pr25-XBRIygJGOvN_jnyuInVenIc1PgzuVVTN5DK578Hqe9-oeaHdseEfLJFKFejqBVY63aPdv7bQaEGdLYwGwOtcHhhiz1GTbt8Lv4e0wetaqFpAyzxB8OQoavz3VMgJQ7EVQciYd8OasR6lnqgT_nsnG5MBoX94vCgzh1c4jsTgqq7Ff5CSMiLHawaXgWVosZxE8j2nKeQrXyZYF0eIzZx6fmZ4bc-upPjOeRHdhtoI5a4kaDe0AAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودکشی نکنی کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/79495" target="_blank">📅 22:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79494">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTlXAbWsCExarjcI2eqpIGVGzyesNoI8vcv8Y8ZDwaFYRUaqYd7gZFg_tTHhllWXzGFOWjuEF5OdoOt_VhjZ6pDr5xpVj202uoEZtuT7hxodgkwTUpLP9V7XMPCKNespkr9220Zuuk4IO_Y-EZNBeLlqpMPWff0qFbVyz-SmW9ThWPHzeHNdz-OOHGRGVlG3iWOVlj9cMME_zA14Fl6ksOqB5C9eShwaAacRIDhbQ1TYlXJl-IzysfPS2WDIyGmRG3OeIor2Fd2rtlWNw9yw7jCzhbvPtQ8AtBQwAzzXqDxb58RC62cexsyILYStd6BssoTa5PrRcNlZWbN4JvcAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند کصکش
😂
😂
@Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79494" target="_blank">📅 22:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79493">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lar4bHTZKzodB4euhsz11eqASny9z75aPr_iPbybJfR7QnLtLt5XFRLPod2mZY-d-K-BGabgUUBXMNFJm4cnzeDfvgV1G3-qAVWUBqgdvKYM27n85r3JfngLqZpG_GyghLTbQrwW-balCIzdldho601Mzo3DF6FVLXaJRyGkRBWhvL5pjaIlpR6VnXJxi2dINhCI7IQUNig4NCJEQoQvKEEh5xQ555mVHuDGSraiiCWAiC8S9eMdxwY1uE7EcvvXvkgvmtOHQxkREZveUcuoYj3l4JDvJoDWMjE6zwZMa_dTcpU6IJ4JLHzYN-Ams9Xpm6coXHYPhmHRvUQJe2vIEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند کصکش
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79493" target="_blank">📅 22:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79492">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔻
HappySmile VPN
🚀
🔺
فوق سریع
🔹
فوق پایدار
🔻
بدون لحظه ای قطعی
✅
متصل با تمامی اپراتورها و نت‌های خانگی
🔺
تمامی سرویس‌ها آیپی ثابت هستند.
🐱
مولتی لوکیشن واقعی در 7 کشور
🇩🇪
🇳🇱
🇦🇹
🇫🇷
🇸🇪
🇬🇧
🇺🇸
🚀
10 گیگ --->
❗
فقط 40 تومن
🚀
20 گیگ --->
❗
فقط 79 تومن
🚀
30 گیگ --->
❗
فقط 118…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/79492" target="_blank">📅 22:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79491">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔻
HappySmile VPN
🚀
🔺
فوق سریع
🔹
فوق پایدار
🔻
بدون لحظه ای قطعی
✅
متصل با تمامی اپراتورها و نت‌های خانگی
🔺
تمامی سرویس‌ها آیپی ثابت هستند.
🐱
مولتی لوکیشن واقعی در 7 کشور
🇩🇪
🇳🇱
🇦🇹
🇫🇷
🇸🇪
🇬🇧
🇺🇸
🚀
10 گیگ --->
❗
فقط
40 تومن
🚀
20 گیگ --->
❗
فقط
79 تومن
🚀
30 گیگ --->
❗
فقط
118 تومن
🚀
50 گیگ --->
❗
فقط
198 تومن
🚀
100 گیگ --->
❗
فقط
388 تومن
🚀
150 گیگ --->
❗
فقط
578 تومن
🚀
200 گیگ  --->
❗
فقط
768 تومن
🟩
تست رایگان
♻️
ضمانت بازگشت وجه
✅
خرید فوری از طریق بات
👇🏻
✅
@HappySmileVPNBot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79491" target="_blank">📅 21:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79490">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ژائو نوس امشب برای رونالدو بازی نکنی مادرتو میگام.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79490" target="_blank">📅 21:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79489">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaUjdDvUus-NU-0Vv3DQWklyQeW2Xi8C7JztDmTmmUfKLfqriQro63YTimoKQAAcXd8BqVBrYJUg95eDdPvX0i2MwpYeQCly9Fx-oXSqLun1N7ClIpOTS9u3pZ_6nJN3aX3kxciUu-L66h6kQTzbdenG4W_4lL0hnPni064NeoebTcPgEtpq8djdbDaNrkVJoOI47gAKFtfQRovQDFcF6BbqhXto-ZbYSaUC1I2MKfGjt5voWpsNCjTvdIZVxrEXV26-vlb_Mcshr689oEv9q8tX1O-OntUkrIuU-OPE9NAYOHGmbDedvVeC6om0iGSetp3pQ_lonPUtSxFaC80eIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دماغ بیرانوند تو گلوی کینگ گیر کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79489" target="_blank">📅 21:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79488">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glcABuvg2332OxDPqwrnhfH9TT1ahy_DmlPaYeFko8SmAK6QqbpQOgukw1Be6bzk5K9Tp4JdnADabh8-EWEmovjfJENZ1JJwxqik4KkcFEYa93AQIxkP7BnENMjFVjbkCWFhvkTShS4glsIDiVPskQ4rjeGHBaRR-O_jeTGr3AEC7pImHgK8Rruw9056xDx2TkGkYalAg3ekHPcvp78NFVrkn9RQ_oVlw90Cbg4LtpKkRY_e67gcUnXqEPSzDtmpkjOZACPY0h7DxN5KHahdS4B5iZCxEGfBprMwzFYnt7bc0oX7wHgQ7JyJf0i5ywIYf9eMaPA1vRznIv5FTRuHsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب اصلی پرتغال
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79488" target="_blank">📅 21:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79486">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انگار این ترکیبه فیکه</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79486" target="_blank">📅 21:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79484">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T8pOuMZoc0B1zeXmpesOZjExaD4k1EU_rxuJ6mOHw9jeOqgiy0BmEDyDWWWBhyV1r9--3XO3161w1keGsAWz_-kifuXn0HyqdwYAXrkgcUKTbeaf1e7frTJ4O9Vot_mX7XSaLgTHAgN5XpscQswZ23LKC6WRH8182TjRIhkR3PDpoM2W071SVB9vmUwc7HSj3Hpa-nuUCUcnqv6XsVsiXmSRbAzp1MRG-jM5l6kFjrAZyBZHjlH0Q41-zrwJDjfmKlTBTZuF2Lzw7M40hyxrfz9YolIvwViIBYD92ZAHew0m_uwSUPRtb9WNJS7PTCpVQLyZ126_T_dQGmMiMKdP0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hWaCjLqwmhfBA-XnBXmpd_m6Ge3O2KPt4499tEaG5GLA6rq5eVrOaNvUu89ipsNHbbf7ErzW1AEHYpTO_mrio9oIHT_f10SheqbhHFQyjj4LnDx2oT74_ldaxa3wEvPEzcg0wDNLVn4Ny08eSL5PugLr817Odfn8VjLy_A4KzA9Bz2iV3YCz843l4MB-wHkCOg6elnRbxuTZ7thHHkoyzCtGw-AASVubH8n7wZNdWiAjgC36d_3nYKOwnK5kCwnNvnajQ60YX9R7LbUF61VjaOYRaUAOVyLm6gqb5FQ9hCEJq_8xl_aQ1Eim6ZKCNHyx2eub9mKJBfT-tgV_9VUxaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ژائو نوس بدبخت چرا نیمکت نشین شده جاش روبن نوس پیر سگو گذاشتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79484" target="_blank">📅 20:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79483">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مبارک رونالدو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79483" target="_blank">📅 19:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79482">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaQ5_LDXmEr6wUyooU5whYSSHyZPv-QQO9GUoxDd4cH21LMlcuSjWOj3PieYyISf6SavM-dXMC0DtwW-MsrnJ29R0kbNe9uIgbSDZth0uRPlAynrrCbrjwYasyEKwWTpTBy5om5Lm_1-fQchsrv4XwTcGT4qkrzlHrre_XiJDFpLxBjbhZT5JsiqtCp7DqSI5b3EX-PuPKoxwn_rZSDPDQAR3_rBoGA9rihGykzfbm4Onm0UfhlOnMRnc4Hd3oy3IWS4Yhq7Lbxox6p37SUcz8OemDdgu96IfYS-9t4uRzN5E8e-Xlbx42zc-3Uu9GdR_PZWDluwbFH3-s-R9yQKzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مبارک رونالدو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79482" target="_blank">📅 19:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79481">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTMTP0IYqWWnRU2cbCbVmbrEkRBjSHOansNV2oboooary9_ReVDkgAyqR_DyiunrJ06tkwFYNY_k4ln0EVw3L3oP_H2pukhhOVImw-OAw1jQ4XRh5fjPLG3G-qHSqIvPwCVz3q1jYOnWjTzQDltg-qYFhuwnWKzR0NM_Tq7Q3JOERtRc_l3uEBwQrqQRoO2En07WRcJSMI-Y0xQsZjOkZqV6TB14AbRykuELT7Pws20kko25xWZOES-nSSxTaKC4em1bUQZ_Wm9wOVaz5ueZ9kmz7jTZEYlPX_7Bv8SI2Du9WmM2Nv6KT_4iJaoHrcGBaGdoh01mWHYwTq-aNbP73Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79481" target="_blank">📅 19:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79480">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RttLUZ0FmV0filOxlprU4xny5NSxvLlg6IEBX95fqkhJ7TlhF6tOIm6_rlodeLA_pTg12PlriKuUh1vXd7HVahBXF0hdaTvagiVUR1ZQSdOSq7clKQcdspzpAJX0dhXx-0zeLHygYQVRcdFSPuJE7jbNI1DSD8g8j7EkFmFAJZf3gVPGPCaHhRFNm9iQUcGxJkijfb6y4DtUsm7UKdeh1s7VT_0nlySm1Thzdr7iijSmbXIXNE_izKHWXUjSpfSFo570mZ7m9O7deMQnWbfYWUf9yc77p3_Ac8FrKYPNgkl9ZtQ-t2Lt-ISKNBZ9FovIpMSVj2JQ_YbZpGhEH7j1DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79480" target="_blank">📅 19:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79479">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjBJxTPv5O2e3fwhiIl8x7_FWPJ6qRAyMITbpyirl9RuLpvTg3nd-GYPtWk-8LD8mS0ieT-OHGPCe3eeCFWScMLz0ZsnNVAj41STkqbzR0rg2PQp4BcTjhkyy2f55lHQHjbG8G6yqSsiZzEYWiNpYehw-fWjAkL4zaIlF9o3rh5QAAxcuyQPKh3MBSpi2JRqdOg4jV36PCyLA90IB0NFsrGJKhcSesyUcXmHKQ8Nx83FRVYkyLU_HFydTV5_gXPO3-fu10Poa3K05W_AuFYpR7w6kfI9WfcjFRyoZf3Lk-_QwscinpgbrffEYI9TcFyDWPpDfXyYXiSin7Cj1y2P9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79479" target="_blank">📅 18:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79478">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">جام جهانی امسال یکی از Pay to win ترین جام جهانی های تاریخه، خودتونم بعدا میفهمید  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79478" target="_blank">📅 17:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79477">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حماس قراره منحل بشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79477" target="_blank">📅 17:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79476">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjwwaMhhZGzee3qt3rwJ98VLd75TX5BFwTaMCD8uJVw0rt7m3xWxXMALaAjvvv9YRCZDqevS9DC6QGbToWEeBoWOzPGXtOOjYrrRa0sn8cPUzGo_XsTvUHRZby1ACtmmHbCMiQZ0s60L6zyMyY5agF7VZT7aMW_CtabJ2JWsU2PyF-Icw0xNv6f-ytc0Q15TfiFfIDQvpBHaYQ0gviLWMb-WZm2lXC4nlS-fpArzkXy0MTB0LbCKa8c9WtQB0rlC_C5DTrxGP9VX2vcey18awwJmiCXclf5jgkTKmMZtBBvfqKgnlZ3s1de7Z0RYy3n5lK8_Ze2VrzH7jC7_XwRObQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیت هر تیمی پوشیده اون تیم حذف شده
امشب هم که با کیت پرتغال میاد تو استادیوم
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79476" target="_blank">📅 17:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79475">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RC6FEoGjzn5A039RYHiL_qI1qpYYnDi54ABddjgbyDQKI2WIoYJW-dLzj-bQm3bpc548jriWPPAgZJCDz2m9UxlbifjdLbrifaXXhjzAplmIKfrjnHuAbe_9UQ02dfBUwx_9Fnl5jV4T0RRZrVfZEO2v-4dDFdRlnP_C4MqUqbWadIRCJMWkdaHuQN38a-pnd-r6EZ739yrTVJHSUw3Piwy8jNp9Smo6I_yxp6iS9lMjbT95bhZVyFGveXm6TrteOA0K3IKoj8nZaY_GzxArYLJvtVmfShJanwf-Xj91ZkhILhKUtGpIHSQZscJ1QT1GnKlzccnIVuKk6q76RShdMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇪🇸
اسپانیا
🏆
یک‌هشتم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
دوشنبه ساعت ۲۲:۳۰
📍
ورزشگاه دالاس (ای تی اند تی)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- پرتغال در مرحله قبل در یک دیدار پرهیجان موفق شد دو بر یک کرواسی را شکست دهد.
- اسپانیا در دور قبل در یک دیدار راحت اتریش را با نتیجه سه بر صفر شکست داد.
- برنده این دیدار باید در مرحله یک‌چهارم‌نهایی به مصاف برنده بازی آمریکا و بلژیک برود.
- با توجه شکست‌ناپذیری مداوم دو تیم و تساوی آن‌ها در فینال سال گذشته لیگ ملت‌ها، تساوی یا برد خفیف اسپانیا گزینه‌های مناسبی هستند.
🧠
تحلیل بدون داده، خیال است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
R15
🅰
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79475" target="_blank">📅 17:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79474">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دیس جدید دکی به زنش  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79474" target="_blank">📅 17:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79473">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bddb338012.mp4?token=p5wE9HZu801L35syxHk4fSzmy7vLSQLnWL4OWQPC1TdA9iC2l1lMK9C8I8GQWq9rYEwCyYQmmZPYseTXX4rShRy9_XTpbXVU9hEGUv0HbSCsaQL9JtJD9MnhC6quPNwORP9SPQlHKaIVwjJSaiB3Bog_4d9GyD3Nr5KzqmhlQfWlhu2_juunFFnt7aZVCibFoQ4C37lekU3txGf2usxCu7O5u7M7-hZBBzL3ZlRT-QhiCJjih0MWI0CG9_vb84g0VCpae1PZ3bs7zBBN2Y4x5zyqgptFkLZ50aLqSlBAECwoy5jEf51UTpqNtI9yHz-Aze9CH0WbopNAyrYl0ZS9nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bddb338012.mp4?token=p5wE9HZu801L35syxHk4fSzmy7vLSQLnWL4OWQPC1TdA9iC2l1lMK9C8I8GQWq9rYEwCyYQmmZPYseTXX4rShRy9_XTpbXVU9hEGUv0HbSCsaQL9JtJD9MnhC6quPNwORP9SPQlHKaIVwjJSaiB3Bog_4d9GyD3Nr5KzqmhlQfWlhu2_juunFFnt7aZVCibFoQ4C37lekU3txGf2usxCu7O5u7M7-hZBBzL3ZlRT-QhiCJjih0MWI0CG9_vb84g0VCpae1PZ3bs7zBBN2Y4x5zyqgptFkLZ50aLqSlBAECwoy5jEf51UTpqNtI9yHz-Aze9CH0WbopNAyrYl0ZS9nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیس جدید دکی به زنش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79473" target="_blank">📅 17:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79472">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbb8eb97fb.mp4?token=sYEakvPhUptkIF3deHTUbEmc7fc6c8iZfba-pDrqohoP9XexaXv2yjfzbUz50F-22heT3gklsdGb8AL7lpdqxGKku9YBZcOv8KFtlH_EXkSpOXQdLCzMq3WWWrR7jA0W-0s76MvaV8xe3hIM6mxDZ-OW3yOiJDHxBeWaafILplZqSO3i-T_DDsY4t_YL_dL3SZuMXEAmZW-dOZ1UvlAV9uwrp4t9wULioZv8pFRxG4UwpJO3dIAfNaZzlD7GtaJ5xAig5oA1LqtbMVeOQKYql8CMGbX7NhoQaIMjLmJmcQWOogG_3zQcBjBt0uybBRCTWaOA8wT7pcNySDzBMVHbNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbb8eb97fb.mp4?token=sYEakvPhUptkIF3deHTUbEmc7fc6c8iZfba-pDrqohoP9XexaXv2yjfzbUz50F-22heT3gklsdGb8AL7lpdqxGKku9YBZcOv8KFtlH_EXkSpOXQdLCzMq3WWWrR7jA0W-0s76MvaV8xe3hIM6mxDZ-OW3yOiJDHxBeWaafILplZqSO3i-T_DDsY4t_YL_dL3SZuMXEAmZW-dOZ1UvlAV9uwrp4t9wULioZv8pFRxG4UwpJO3dIAfNaZzlD7GtaJ5xAig5oA1LqtbMVeOQKYql8CMGbX7NhoQaIMjLmJmcQWOogG_3zQcBjBt0uybBRCTWaOA8wT7pcNySDzBMVHbNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمیر دیگه حرومزاده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79472" target="_blank">📅 16:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79471">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">امروز روز جهانی بوسه نمیدونم چیچی آمیزه، به همین مناسبت روز دختر مبارک.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79471" target="_blank">📅 16:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79470">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مندز و یامال کدوم سگین، امشب رقابت پدری با ویتینیا و نوسه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79470" target="_blank">📅 16:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79469">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ex5r1hfXeEXunvEoscObiqGGhj1PJ-o2_OnLVmo4mjKsGiYERIhssy_tp1DLuC5ri7HytH38J1tU5duaULbmgMUiuqxC_s0Jlf06ECu3duomcEyBru7cXD1iYVhPp8OZFHoYXnAX-_vtX5aSC2eSOVCdHiryMLZsP6ck2dl0Gf0q3L4AaVA-FkGWWjR4ktspvrIZIfy7EGOpIwJYIXYESVLV2aMTrO_xb_1SBsTvRl50TwpPfc3GmVR8u6RkBeuwwBwwZgAAgaD9ciEgvBASTF8PKQGfnJ6Nynd3liek-Swwxrghv_rn1BmiIKpkVCDTHvji0u1BjtyK-Rdp9eEqtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به همین مناسبت ۲۰ تومن بکش رو بدهی دکی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79469" target="_blank">📅 15:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79468">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBig10c8suly4mOB6ncCF0RSpUyNW2i-I5rk6oG41On_xZRoWIikFZ82HMsk0LPbc7lhLWSgWn8bmuXkeNL2OUem9d32GP5iDi3vhykFVikw2liT9loS0dW2hyaM66kIwv1Sff5A4og9opqhWQt9oqJbnZ3kBs6cb9xRcwt5dd6DqkCnWRrk_dZBq8yjyB4aDWRCWQOtvwsxZ8JDFF-A69gtX4eb4jlPTqyEgeTGS1-aZdhP9avNwouNIcghUBE27jGnHVL7b1G4BU_B1LX3BPT5cyOLxMjkA0I0Uak6UxodvFaEJ2P-DBKw-iJ9hsZVLEDpT3j_IjMivPWFrXyALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گنگ گنگ
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79468" target="_blank">📅 15:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79467">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YT89bhcqyn5eO_4dEAbpaAoe4gmVz-qOVm7lgg9RGtiun3NqyvybnkEPEkzoyErrpAx59lyiHTju9XUBPrKuBB6A7zhURkjT2q-wpDfV8LV8ZX4XJTkhIqrIvWO768cZH1aaETabRJAy5JrItF_A3t3xIeT0urH-EmHC0opKmYuvlvooPcNXrZjklDlCll0p61TbTKlcnhOlMa0gQ2sxe_jNa1EYBvB-4l4qcuHINjBNKtxfdeh2Wn-Sb2Hursz6G4BFIiJQLH3p-tQ6Uo-1-kpka4PeJW4TVuBaG95wUCnVlByfuOydDljpRRIwP7SSeS13y21koHScwqUWsqpRmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام مجتبی بالاخره رویت شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/79467" target="_blank">📅 13:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79465">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">جام جهانی امسال یکی از Pay to win ترین جام جهانی های تاریخه، خودتونم بعدا میفهمید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79465" target="_blank">📅 13:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79464">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">صبح امروز اسرائیل در طی یک بازی تدارکاتی دوستانه با دولت لبنان، حملاتی به مواضع حزب الله در جنوب لبنان انجام داد، این بازی با نتیجه یک بر صفر به نفع اسرائیل به پایان رسید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/79464" target="_blank">📅 13:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79463">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">لاپورتا کصخل کینو بیار برا دو سه سال پولدار که شدی برو سراغ هالند</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/79463" target="_blank">📅 13:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79462">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">برترین های جام جهانی در یک قاب
🔥
@FunHipHop | Farid</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/79462" target="_blank">📅 12:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79461">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fK1W9jCjHPT4wUe653NuPVxDHG4H5Nwj1Jq4K1xrcPlFQqAV78mFpyfUvc232tmi0lpbCOF7pjTiDETedIksEUVJEVD8GgIjABwyLVfKhUbXcyl1i7btNAWhwmi4FaIGb4gngRyezrcY7vtMSAVHFNcY6SoqgtSi-5nJetpufT-tn-j6NF13Qe2Cp2v_RQWoT8F969QThoNeHoM8BbyZF8abXG4MWBS9WtFTQ46DNK0SVjVO38OskgmBdBXGNfoWFegg8RJmbB0FRlaaQEOPuI275asUFxs4zq2kezkagjVsxnuRTgCfd5orloubzcjJGQB-vtA2Kdv-BwddyJntrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برترین های جام جهانی در یک قاب
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/79461" target="_blank">📅 12:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79460">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">میدونستید وایکینگا تورک بودن</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79460" target="_blank">📅 12:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79459">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حس میکنم نروژ انگلیس هم میبره</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79459" target="_blank">📅 12:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79457">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ozyDvG5SudnFgY17Z3Dyf7mYVtYUSXUhXf6hnLgnI13mPfLO8Wp0zS0JNnKJVIBFzITMed46ijYRwjdWnDvcUHIP0t9Cn7MzlWnJ4omJerwQVZmvcFbABMUj2XbSXAJPoICKv9mCvTkfledgY3wAr01f_Z2PoZWSo3Ti52bS7OnSlQIYXceTCaDDnQlynSaJUjuwA82nt0dpmYac4bIWshDFucGK9KJZqNRjIn_vU8LFgWEpRCibeKp18eGMHRRMYwHT_zhWPmYOdNHs10XDQTFUWz5bT7c3Mbe0h_N5U-I3sns4OFhK0wtZ6ISEsqfs214idu8bWRGDusjq4uYlHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JU-3OnattzfUf1KwODPPK8OUT9JMw9wsjuLmh5FMpvDlBzKy3XAgYNJdakchehK61tvVdAPInzwrk10AvVVcXKk8lKgWal1pQRIJR4vBYLWgcC3nbJOrHtO_OqO7Dd-Ia3KwJSML237yo9o4eHzrOYW8oh6HpGrqKGshOsTO1yVAJlyKu_3WOayvGiu5dvBSGr0dZC9pgTHPdEtOhxg6nlmv9P2rlc5NniX99VlkKl0ZaymTogYVS_l4EQ5Lu6kp2QqYvA2kkLkL92zmVFmHe5TpTFcAK7ZyQRR58WTkYxa1_F6PUGS0z-EjVECmdFOUtBhEVPMnlrDqjCKPI6I-SQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آقا این حساب نیست نروژ دیشب 12 نفره بود
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79457" target="_blank">📅 11:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79456">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtFmtGVcq5OKBUSkLvrIk7Z6Q7sJbVZhDavebcenMBlzB2_fNJdDmFCVE_y5-QwdT9UI0uPv2DO85p-dX923jikZRiFIhIy-x7qBE6pVnbO38n-UpELA1hR-4vA2vrvGl1JS8xMBWOBpYkCicL5w_1HHdc4Y7pFr1TuUSx_vGV7YIzsk-XH-eNZLFHFoMBShR3bYOmf3bM65IiLk3rD8bYb12jSHgOAj4BBa9FpLWm-1CA9t5DXAYZvhfzzaZExcubbEQ6I5__p8ehkW3q_vuiRH0Bt070WyMWS2ckHaxJuVQ4Wd1T4k_XSCa5OLQrjKZ1gijtakjhdFh7H-ti9zVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیپ ورد :
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79456" target="_blank">📅 10:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79455">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WR1DdRM1gLyQi_0IEsbBVfgut6ywFIC7sFZDwPqhFGiOurtrQz8FUAFyj68xjc7ngZ4izJr6DD2Lhw3AAGvRFbGpcLoz5msGy57oVorFtDgO_EESO76GrU5n4GXIQrvgURJCXY3-RsyScCYEoMRlP4Q1P5tNDSrftkq1ZaCHOOUna6cHTVlXW1MwpxHfSxt0ofJqyS7SdmjXzaKfsF3IYo-ZmBjqFpHo9HIhHePdVgAT_mszhbmRzdvkGTwDnNZC198Ql792pRqOAUEGnevfPtMiB9D6Zv1QV2ljZL46JjnZCyDEmYFc_h59sOSWoWN8166tHiWa6roobTUsd44umw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇪🇸
اسپانیا
🏆
یک‌هشتم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
دوشنبه ساعت ۲۲:۳۰
📍
ورزشگاه دالاس (ای تی اند تی)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- پرتغال در مرحله قبل در یک دیدار پرهیجان موفق شد دو بر یک کرواسی را شکست دهد.
- اسپانیا در دور قبل در یک دیدار راحت اتریش را با نتیجه سه بر صفر شکست داد.
- برنده این دیدار باید در مرحله یک‌چهارم‌نهایی به مصاف برنده بازی آمریکا و بلژیک برود.
- با توجه شکست‌ناپذیری مداوم دو تیم و تساوی آن‌ها در فینال سال گذشته لیگ ملت‌ها، تساوی یا برد خفیف اسپانیا گزینه‌های مناسبی هستند.
🧠
تحلیل بدون داده، خیال است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
R15
🅰
💻
@BetForward</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79455" target="_blank">📅 10:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79454">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">چه بازی بشه بازی رده‌بندی فرانسه نروژ</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79454" target="_blank">📅 10:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79453">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">عجب بازی شده انگلیس و مکزیک
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79453" target="_blank">📅 05:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79451">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRPu0zg6ykxhYI3kE5pxs7YEi3qLb0HdZNNfGfts1upDPsWEfgpBdHqbK4VL_bmxCsil1BUGLi3zQQnpEv0DMqh2yF2yv9qYwRhjf2RIqFKLRzUEQFBF1gXtakcjgHAJ6L0RHiNl4GwJ--P9DlGOCxRRXDhsx9btYU_7yWf0qX4KQgJ7gYKORUPzn3ud1FgY-9HBf20Kxqozd2C6OHwj5XmKWuipvhpv982oCTXf30CkqbqX6Vipr342JZYj2p43kxXq-VU8aPkBG2fLdj_PNsVu9Ip5WPk98W-qlsMO02RUCU2KrrojO5ZmyNiJRYn8wTB25sM5HanPLVHZOOk6Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا تو امشب نباختی، ۸ سال پیش باختی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/79451" target="_blank">📅 03:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79450">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">استوری جدید علی آقا دایی خطاب به کارلتو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/79450" target="_blank">📅 03:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79449">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRTPNMuFnZ43EoL8UU1x5rtRVHgHoDFPYjxPiRaaFlA-uXirmmeuOPFKckj_bTLn-CGo-zS2Ttnx0Bu06KfwHtEFBx0YX_heKZzsf1sGYiwY5VKFQzMgWj1yXY6VddYwRp2X7_B6Mg8ddCOAFcr-piFEf5Fnta-CJhv1gP_9_eudsvbuL6_nFNQjqvPuidmmaIu4e0OhPSwm6g2Y3WFLWLYdUYn1IK7zz-xbWln6C-yYMDIbsi3tz06zNG4PL9QP-GO53TQORN6bodtzx9J_0G922rpyOv-X_vHXtJ6MA1B7rkInpi1kyzdcYZJ7bx976vq1qM3HxCT0NNjZpwgsVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/79449" target="_blank">📅 02:19 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
