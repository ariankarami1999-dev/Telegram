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
<img src="https://cdn4.telesco.pe/file/fRaQlvmooLqLU8p8Z4Wz0yOfMmxbJOjGlzMvpUWfH-BJk5PoETVEUkvyngyIpWZPbatoHR17xyztdYcdBNNoagckGbRE2HarH4Ap6_XzbmPhv2swpSYMb9kGesbcPP8pHE64Ah9V-x78UAl7ePQ1nqAWyEEzkTdVBOyzksEhUwr7SAYHNZtCKix9sgh4H7t2PczQzbascZm8BdhLuDlQ5Z9cVn4zrAKqsxGm4QE_q3DaekWCbiDEc0xn74yfLFZzlgzkdAYSe82XBDcRiCyIEXFqyqMOV1Hip4lxVmIWkAkxTvBBY365v7CMt8OCIB7YOIt_r4LOflYoa0gIaYFpNg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 02:13:40</div>
<hr>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=uaYyv8daaW-2OgmvzFIGpqMIDH_00-NHrDSTQKY2Fppf17qLRsy2c6LIMRh3XjQF0Owr3fkNGd1_Elg3CECjf03RS2rsyZDzFVOTFT3qW257LyolwldN1CVQLaNGEYLXnArSa4An2Ii6NGSTUXesjGFWqqN_NNO62GIdE6XwmbfKtSXgv5IeRQCYAr85Tbw4-ssA7ECrKufQwY5BUznEcy_vojx8r29O64NEN1uPA_xDRmuw-InNmb0rUDoz2xVlPy0g0bJjGLhVyhlIcXZkFitwZYIxWkN6nDMgstRzrtKaWQibj0rdlq_nyiItX2wC1GZWllU_Vy4y5ais39dN4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=uaYyv8daaW-2OgmvzFIGpqMIDH_00-NHrDSTQKY2Fppf17qLRsy2c6LIMRh3XjQF0Owr3fkNGd1_Elg3CECjf03RS2rsyZDzFVOTFT3qW257LyolwldN1CVQLaNGEYLXnArSa4An2Ii6NGSTUXesjGFWqqN_NNO62GIdE6XwmbfKtSXgv5IeRQCYAr85Tbw4-ssA7ECrKufQwY5BUznEcy_vojx8r29O64NEN1uPA_xDRmuw-InNmb0rUDoz2xVlPy0g0bJjGLhVyhlIcXZkFitwZYIxWkN6nDMgstRzrtKaWQibj0rdlq_nyiItX2wC1GZWllU_Vy4y5ais39dN4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBLBI_814qgol_DQ-CIl1yYSfSaQxp2B1Wh4_IPFEmFgWj5VT2ZvlYgB9pb-ulo1GouS5z2tOfgb9OfNsrEo72Uz-5QdMHBy24nQbSTQMWih68uQAlNetn9-OoPgStEbfTHFcNbAxwHyQjDhm_c7q00qEh2N23igLiJzk6T1eJ8ppq2b6sqSJyXgaMIG4_CQWnN_Up9o5Or7YKfnf0QzqRt-lTdMKVWG162UQws8oCy_JDAK6ndbTkLL6z_PnTkX45uNns93HqbTJtqcf1XxoQj5cfl5zLfRBkViNdqFWpaxr4lMiagnhqhX5G0GklWkwuhTKnUbRg0f396JybuvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_V24fwnlSEn8pBtox3mpxpxImaYlFd8e44Kta2sIesLQWwRF7pDZ-lW_UHBH-F9OuUJXOBB1FfbiCJ1RibqaJ-snqF452VaujAF8rVwShBgO3Pk6yq55d_s2H5xZqJ1BmADKlUdgg7wCMYaL8kKomfWkB4F4aY63FA4JZmD_ZrXB_3XfVCVWmlGHdiiwsZmmIxrZdOLcLTU6DWWVfKm6fl0IAFlw74qL4ai0_-dPjszTWYa0THkpBJL_fHzGRBcshnkDDHwcT6yhQb-_h4SsAVMeeYzTPhMhtUFGHL-48vTp_vJzh-paPiVuic2vTSu7ImpBdUH03OUVD0BtmS7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UN2yWvrNuER-W3B0ndpNnCGs6MScI-lgAV_vzMVa_NcHDrat6h7_hs1rxcPF29p85DxzsAQ5FOXF90LyLokbuifnquZDxkTkK99iyYKhcXV8wNrigBU_Pr02JBvSY8nFKVy95hcCl7ys3rwWIG6eW4L_hKW1OmaI_74kWwMnl-h8Kd8nuUesSA9U4W_Sa5teROcy1wzLH_zK0J5LaRC6nxRhWv5DDftpaGRMjk5_6Gm8R7ZS1eQSaTL8ebjEthlvTgL19pKgNZ3Qbl19_ucx9AzJS1dJP4q126jcnSP7OXNS3igOg97wxABesnzZwPMr7A1rOrpE7orKHj0lQGp8ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل گزارش داده که در عملیات خون‌خواهی خامنه‌ای، توسط تروریست‌های حزب‌الله ،
۱۱ هزار ساختمان،  که میشه
۱۸ هزار واحد مسکونی کاملا ویران شده!
بیش از ۵ هزار واحد مسکونی
هم بالای ۵۰٪ آسیب دیدن!
هزینه‌ این عملیات قهرمانانه!  ۱.۳۸ میلیارد دلار بود
که قاعدتا باید از جیب مردم ایران
پرداخته بشه!
بیش از ۴ هزار نفر رو هم به کشتن دادن
از حمله حدود ۸۰۰ کودک! بیش از ۲۰٪ خاک لبنان رو هم دادند دست اسرائیل!
🔺
آمارهای این گزارش سازمان ملل، شامل ساختمان‌های ویران شده در یک ماه اخیر نمی‌شود!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmdjgjWxEQuckLdTv8N3YkIHT3mZ55uTCEXVEUmtjcfR3S65A0FeSghZc-Ylw45bbMoUqmy-q9SR91SOM5Ov5-vW049M9Lj7UBlVvKcH0KXXOZ3DraVoVEjjyCvNdx9F_UCmfjVONHnp1xhDmMBEyQvqL1y4VOCgA8zJyqel-NHIzFL2J2AAHcp57cvhoh6JOWAuIytaYpljmJUqWRJaDdPo0GfC3_JrIfeASDwpXycpqetSMCnQzC5f32nsLm0PZgj0YuIRJUEKMTn2pcinS_jnXxJxPBFJBs0hLFapJvQqs4iKiKJarxVXzDTCU3nV_LkymwNc6qxHFz3hrnn2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=DDUGI6h6sk2iTF0lDQyqYqpe0w--GDQAXtDqIiXUigsUI51HsfpwgqJadKBOx4kpcghFujV709qBHGgFCMqdw0DEBosAYcQLQoLqRtsFalgxwB6bFbCusaF2Fdp7KHnDLg0rVCFxm_CDPfDA_8oybEulmCHw3l31NbrVF2qx-ESlG-IH8I_DPX-LRb-ziu2wKoTnH2Oc3T8r9ZjZb1segzw34l82cADt3cna_72QDuK3j0i1LqS9s1tUZe73zy3gbiV54wzXh2smBwQjzyjDVh4jCrQ3R77BoKFXG6ZSEVqOGuQ_FrohLX9zlFCcfZvBemur09eTqOIce57TvNSQsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=DDUGI6h6sk2iTF0lDQyqYqpe0w--GDQAXtDqIiXUigsUI51HsfpwgqJadKBOx4kpcghFujV709qBHGgFCMqdw0DEBosAYcQLQoLqRtsFalgxwB6bFbCusaF2Fdp7KHnDLg0rVCFxm_CDPfDA_8oybEulmCHw3l31NbrVF2qx-ESlG-IH8I_DPX-LRb-ziu2wKoTnH2Oc3T8r9ZjZb1segzw34l82cADt3cna_72QDuK3j0i1LqS9s1tUZe73zy3gbiV54wzXh2smBwQjzyjDVh4jCrQ3R77BoKFXG6ZSEVqOGuQ_FrohLX9zlFCcfZvBemur09eTqOIce57TvNSQsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxFz44CZ3kCcIgGOUlCTGUOCPURyLb_cAeSaLvPM2ekdL4k2M37l5i5nh841-GHVldDo1VaB0hj9oNWOCYQ9-jJ1TgUjp9BYC-lLGlLhO2cyx2KBHh8guuCpZ5XuVljXTHBGW5gnbntOK6JHOr71R3wTYvKAufMCk4-8McBJ8VWQkEJZ4eItyPPiOkq7ixntWJl33r84zbsKvPaP0-10gZSbC9JRfjJc4AKIgTJhEAv4gmWuwxchKotejflOBmjiZbL4DkcnRrsYtoqqZjnpsxNPAk-wCdhIa1bYa4FSvo1SkBSdvmT8qvEJvlRJCU6hfh7FsMh5x3ichxPd0G-p4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JX2Em57BlV8AHrCHXvQjzSsDaWeE202zmSRAsTfJuGGzQsv-Jh8ge2zHT2DcmIyIgNLjtjcYMybGx2PhoCZpj3sozzZm_mgvUjOxPzGgihLVSe75kGM6KWfLDcqYDK_BsrdkhA5tJtnBE2xykOk0Rp_drzY3sOFcgnoAiWQsNXRD_DbrNC4y1rOgPYrMakY8FlT2ApJlTfrV7P3sqomo1OLUyErcB6gxvreLz5gedLYyhSzszeXYbKAukjh8Aytr0LRJTUgqev5ZiX8AB3rSUdDo5Jfh98HVtj2ccTs-LOj7G-2_DR1jgqjPwmhI_NFCkeISF_fstFLoSOXSasXSlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlrkF_uOBjBspnUxnru03JVdiZqjQE52T0JcY7tLPb6LKL9R4FDdVhkB7LHiKfN0dNqLjiHhrOrgPfmi_XURGCGNigvtLEXDu81YOXotODcWekauSIRQQGKHeJ3QLRXTZ6fP7-SdAvhEv1C6ZzI-yCwGQGvar3H20Yum9mOpwXLdfngYwhcp_yQrHhk_kfmJ7j96-EOwnf7uhyeQVHyVClCFFPdAFApFsxNjevfG4HIz9OEu5GahLVHXnTquka-JqaZkd_4wXfh1Lt8So1PSDcPBYbu5hSRiIHZucwzzJJq1guwsoR9T6ru7P22gb-nt-r4lm2rX6Gj4LRV4LHoV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=PX3zHDXBqQEXd4oLvAo1UmUEkjo2iqRBfsAKrJidrJsi0y8Hi8xTOWD0cxbXjRgaCww4T7pUvjbhotVekWSPHeX78lQXRvKUKDp-g7fjp1O7IyEKtph-n5-sY-Isra4QVsj5WbCD27oPRWtH-VcKepqijtW0BY7KHeoXmAfDIMciMEox5HfQm_YRMiUhOaaMVhv8Ay7hTMYlGIf4RrHqe8IUWpOSKSWaflnUCPvb_i0Ctj57P6XM92TEXNLx-mZRWb_tD06yS06azx15woW4uMSyxMEUPoa9dgcJ1K8JS_mtBntjFYI65qZU_pWfzs-GcnogMytjxfQFN78op_0Jxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=PX3zHDXBqQEXd4oLvAo1UmUEkjo2iqRBfsAKrJidrJsi0y8Hi8xTOWD0cxbXjRgaCww4T7pUvjbhotVekWSPHeX78lQXRvKUKDp-g7fjp1O7IyEKtph-n5-sY-Isra4QVsj5WbCD27oPRWtH-VcKepqijtW0BY7KHeoXmAfDIMciMEox5HfQm_YRMiUhOaaMVhv8Ay7hTMYlGIf4RrHqe8IUWpOSKSWaflnUCPvb_i0Ctj57P6XM92TEXNLx-mZRWb_tD06yS06azx15woW4uMSyxMEUPoa9dgcJ1K8JS_mtBntjFYI65qZU_pWfzs-GcnogMytjxfQFN78op_0Jxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=K6Zf2KpWDsTScUGf8J1m-heHOOKfO1AScVLqlmZ0qO99qhhHiXAUpbAYIlusTbwhAnVccgpmXxyCzCR3hCF4DHlTFAY9qjewju3Wvtl5qELMXXIyFBVXGbFV05qxU8U53lIyBgii5CzYZzgIR7i11aSs4Bh-mfSKQrQNzhrMtZ802eYlmt1vd_HoSlkRbF-CxXWhgH9kdtqn2kOlefSehGHENf2sqDCfgX21sYRjbdxE5W5M2n8FcdH_laMnz7aZX8NibCE4x8OOruS5zyFVEuX06bO1GBtCRzpT4b918Gy09wWH7VYVVo4pcfKnAUXVnkG7eTdm2s6HDmCTojLAfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=K6Zf2KpWDsTScUGf8J1m-heHOOKfO1AScVLqlmZ0qO99qhhHiXAUpbAYIlusTbwhAnVccgpmXxyCzCR3hCF4DHlTFAY9qjewju3Wvtl5qELMXXIyFBVXGbFV05qxU8U53lIyBgii5CzYZzgIR7i11aSs4Bh-mfSKQrQNzhrMtZ802eYlmt1vd_HoSlkRbF-CxXWhgH9kdtqn2kOlefSehGHENf2sqDCfgX21sYRjbdxE5W5M2n8FcdH_laMnz7aZX8NibCE4x8OOruS5zyFVEuX06bO1GBtCRzpT4b918Gy09wWH7VYVVo4pcfKnAUXVnkG7eTdm2s6HDmCTojLAfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=IZyW1Tjmq5ZJQP3eHdCmajmYLVTOGlEvzYdRScYT5GYQaPep67WOuDeaDqQV7OxcGij2haTRCSeYTLFBCvLA9Bwn61cDersfXkLRmBSkwr1aSkDZk2j5a_EZAWiLvNCq7eOxe2BaiXnQKj3oFY-FT7TjukTWeb1iHbUAsPXKdQcW9C7GoOXP2n70xxdhRmNsYN7UI0on7YfQVOVEidP1KmvgsJliRbNgaLj9kZe-C9M7pKn52I7a1VgMZm_ueRg2SGQX8WqGHmCU2gwxedghNK9-YOohNyAsfa1mL6t2UuffPviS-nXtBMcZKydwASRnQrvQYuyyO-Kf8zQgvsQqLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=IZyW1Tjmq5ZJQP3eHdCmajmYLVTOGlEvzYdRScYT5GYQaPep67WOuDeaDqQV7OxcGij2haTRCSeYTLFBCvLA9Bwn61cDersfXkLRmBSkwr1aSkDZk2j5a_EZAWiLvNCq7eOxe2BaiXnQKj3oFY-FT7TjukTWeb1iHbUAsPXKdQcW9C7GoOXP2n70xxdhRmNsYN7UI0on7YfQVOVEidP1KmvgsJliRbNgaLj9kZe-C9M7pKn52I7a1VgMZm_ueRg2SGQX8WqGHmCU2gwxedghNK9-YOohNyAsfa1mL6t2UuffPviS-nXtBMcZKydwASRnQrvQYuyyO-Kf8zQgvsQqLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">🔸
گفته شده این آموزگار زن به جرم تدریس آنلاین به دختران و زنان که از آموزش محروم مانده‌اند، این‌گونه مجازات شده
🔸
براساس گزارش یوناما طالبان تنها در سه ماه نخست سال ۲۰۲۶ دست‌کم ۳۱۲ نفر، از جمله ۳۹ زن، را در ملأعام شلاق زده‌اند.
🔸
با آغاز سال تعلیمی جدید، ممنوعیت آموزش دختران بالاتر از صنف ششم وارد پنجمین سال متوالی شد.
🔸
آمار یونسکو اشاره می‌کند که حدود ۲.۲ میلیون دختر افغان از آموزش متوسطه و عالی محروم مانده‌اند.
🔸
زنان در افغانستان با محدودیت های چون اشتغال، سفر بدون محرم، پوشش، فعالیت‌های فرهنگی و ورزشی و غیره روبرو اند.
🔸
در پی بازداشت ده‌ها زن و دختر در هرات به اتهام رعایت نکردن پوشش مورد نظر طالبان، اعتراضاتی در ولسوالی انجیل شکل گرفت که به گفته یوناما با سرکوب خشونت‌آمیز مواجه شد و دست‌کم دو نفر کشته و بیش از ۲۰ نفر زخمی شدند.
@RadioFarda</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwwhQ_ldICT3cRxJOC9cnEmlZb48JEnIKoph0JojT3KgH-O8p28FTG36Cvr07UgOAhgc9_mFZHzr4ei0ZyZGrhY9cQHi_7RMxCp5g3omnn5u4oFU3FLJCe7vYMtNB73PS3tcuT8RIk772Ow3mPhqKPnNnFifO3HiTw7uauOX_XKGFuI1IG7InrMtof-xF2z_cdpoFbvRKxx16w4nNVLU1B7Vh2kmaJTbqs7p1PFrDC6yxyeYt0kZZFevLf-eokatdnmAE-4qY-IH68ha26oHawX3LVsRHeXX8UlrWFeNnqoExJaiy2C5AWA4OsXMQfpniReeBSU_PDFLKZFT4L-lLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uF-bgGTnmS1Orhyf88CBJNFxheUlj5iGZi-vOPKYWfk1DF0KSi_IlL8qoO_tztJELxNyE3VtAm_1UgBVhLOiDLBYtL-08TwenFMoM2R0fp2iiyVTgCA1XjBtHJIFGDpLz5hyi5n6ruvcstrj4LdmKbNUsn2sY_csSx2KZyP_YYTfWwShvugChMEXt9F3o0DKLD9jYgk2vj-IsXSZ4DXgJhICu5sy0mIMWLh97pmGZMaukT9q2VKO21TbK9Lq1fV1WXDTrMF9lV9LnOCMroyoakVKNsyMOq_bNPSNFhyEn5FWDWJbrI4EIuHrPSWws2RvbH0p2H9E8ZLKeS66lD402w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSff7t8ACHc96vKiMwUCL9JW-CshwMOjQPWMTpUxXMnjItKktpQ8VS9baK59qQ4xT1huavybta8psXlG2q4-2tkIfANrboUISw0QwPvEGoE4Nty2hGQAmTIChxcYVX4VmPXuNzCChi9fWbNPZBUtrUUuCLdKAnhQNwd5DFxnBLng1eK0KSaDlXNunlOwfE5h3-BLqHpZew5ZYDmbQbbUnGQbRRV9EmpUWl8uS55eI-9_rEo8W8GTS1dYL3GRGU4GWlQtxrmmve8ATkgEwkLC4Ke-xopzSiVqDGxUfAOgTWUsMEMHJbH6bBa4YysGBCucq0QyOech6f4fxHaKcjJSPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hVA0ZzOUVcIvYWXZPZ5h7eWQ2B7U2Vo99iygSHuN0Q77-lXV-0w3teaco_EqH_PkFZnpFVBIadowMQWag_dh3zVc8H-n45Xw7pBbZ1mHxEgbf5rZHpuO4HMpwfhll6KdZPXAFch7Jbi7oZ1FNI9s69sR_AC-emDjTlSjlCalq5PGx1YQyZ4p8ST_pa0iqPWS5RxmY_AYUBygluwCyf_qltOfRWy81Lef7IWtqorPcLG_ythiaKwFC8LdYFB0u8KcNcWcl4YwCzW8WUy2EcQXGpfAI5UaEnVvSU-OhuFMj_fGM5scYKxXoUHgWr61I74gLyoqIzk89dUEGych85nbYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qknrC7mLksBBdTnTuwUOIkYayIGk9Nkx9iF3GIMi8x207GNsWiz1k3hVXKm4rnzUGKYs9zV9qRwYHNULh0fLF1SCqs-RPAUoSTfk_sUHYESVjMGrArSgO-BlGNJ-8OeK061tMEM8tX2W_qLaeSkdqZEIuELoIeYWNc2zPIYRJU-LZWMYwFNyfxHx7ZTLqVKboVyYGIqARaJ9m8AA19qQGMBG1999BFDaK75gb7zDlaV52niRu1Hm81b088ywfMNp740zkx8TzqXp757qmunCHkcjTF3C69judb-2VA_GK3mZCC39dgdD0izwQq6noQ2_nV2sSNX2SSbItfT2Wsg--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHLfuIK0_jaLUUcwKuufdyRkMMbuR1R7VLmNbMIcv7Av9xpiokEo_iC4NRNCtNRMqKSgrFbjHii2edyYbDfbyPBy7_xL6bkZtPSMcELNZFnD4B5O1bvM62CiiY_Rvi6g785MwUl5K8iBvH8HpIRXJWf55E82zhGTfii0oE1aYcxTMA2NnQejFcqeAi99HQ3yx5W5TXuCObl28TaDTAvfXZAz22hQy3N6XXap6gesRsyW60SFkT0Rq511g_l-3hqJRnl3ZGFRtd8rgjy7GU3soxHXAbkd1ex7xKfcSEP5RPxBSXRh_RlrAug-43xUDem5wemNitk_7j4XMXYjjcv2xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WPIk-GNaZWqVNXWen8xZoB6wOOgtW5npGo6zc3kD4fFO43R1ty5ZOh4BL-PLaStUGSqJUPFDAGIgc3bYSeCLZrpfxOKL-nm7fvo1yy_i3sIQ7cJSlXZQIcF6mElsqhyYTSl5gWpq40acEP3zhjNzmBumUE05Fuk_q9H8KA-gxfJb-xAF5DXFUiDkPZrk1AiAdCKSs2iS9fdxCMOi7PGjnv5l7NvPyyhva3s81AXoY5hTR4lwMN2WwxcTFC1_JKEDqzSFhjd_SL5cij5cMrr8Dk-_vwe3hSRQo0f98dUWnLmM9bvFwgef_Ouzw893lgUGqM8se-FbygD5CIGufh_VWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKOktxPvsUcFuw_2SADLxWm62LPtUsyTLEiGeGya7CPLcFJbx6Tyi-Dp6r9GzqS8MUvHXzm2bmyF_PxPxhJ3qA1oT3pv6lQDAtC3QbhNRHIyDZ-P2gcH5nkzIItV2sz0Zbdf7ysoVJ8REijIowDaTi0aie1RIxGUt2ZFodEfICPD7dgHoJsfYN32ip4xI4Lv2Dw8W9UzEYBg_QTkAZ3ga_tfg27hPydx-p_99zIAiLY-wEX2I-B6rnyvjZ_tIGnW0908QkoVOEkFuBGW7Wvbfhq0U08e8W4eRDs1xFB6YSd7KZHzfgm5UqIYjPxbAIUtH8lIPuxn6eCupFSSSRDIpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره از ایتالیا انتقاد کرده
که چرا علیه حکومت جمهوری اسلامی
کنار ما نبودید.
این انتقادها و حرف‌ها  شاید ۲ ماه پیش،
۳ ماه پیش یک معنایی داشت!
حالا با اسرائیل که کنارت بود چی کار کردی؟
خودت که «ناوگان بزرگی» داریم!
و بزرگ‌ترین ارتش دنیا دستت بود
چی کار کردی؟ مارکو روبیو وزیر خارجه‌ات حتی صحبت هم نمیکنه!
که توی بازی‌ای که تو درست کردی آلوده نشه!
بی‌آبرو نشه!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZeaYfBO13mR3iztdu0cpZTVnmQzT91YZotAPrMF3tYj51eVBbhnv9GKE7nV9GpKG4-z5sV-hQTmup1soBor7zhLW7kViBT_gF2IXjiPVHmgJ7KHOiuWj8fL8H7v1Rl6wKzY1TFQxyOPmCsEZkPQPPIUeRfQsPvznNKP0-HAExgMaE1Mud5jYdcyFv_CIebsFWjrR4l2vi7semr_BI3z6Ef-WhaaK65NP9BOBhsDIpT79_RXpm-xIvp9vM2OYURu7_6eFs6NxB4ViYh29JZFnSTt1PUpqx3l6bGIsohGWJEeRXaR9fLVlB2h9Q3OtjXg5ERHbkiViYeEaaXrNr1BcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7X1Zx1xpW-09xns5k2fJfxkQ5iRU1mBLTJFCO0qLzTJK10yfv2t2_bMchmSoQ9xIU7FKc23zoENpeTj0BlHfWcXw1eFJl3u96FsNd0LvAHb3eNQQhPpnOTA-Hr3uuOvQ729C3P2T097DffJrCZwJWj4PXxFCJ4pe6pGb4rLmvSwjThZtEIHYOb_1R5uND4cLq6YL0tE_MHSg3-wu7w4VGyuYu_Pui01s_Cg6An8McC-4GDQE5hiFWN93ArfHSSpEkUdFcOb5XPtbOWf86FPuQ-VgXqmM0E5EEEby4FXHS_A3Kz-jMYnGVXA32mMjgYYWDaGmdxvUdrKpQCIEcDZCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxkDZU4q4EOH2RNXZxyMs5vn9TJtQXtDD2XmYOiuASV168szPfdL43PL9NfLmfQu-LoWBle4Y_PGDOyZORi4CNN0hgTvJpeeBeHsxCebLaAMew8ghAJcWxzlll5ieiOmHnIBaPN9pddtAIqT-2ATYlTnAWJxeiMfPXdBoOjoDJRDRBsB90bT4o063OIer-YV_HOFEjVuhiKQaB8u79p-tympXRlaXCKSniopE0eoTPjUn2d6_oz1_BN2LTLXmzeRswAVkhlI8iJQNON5hBPrgnimK6MsoS0a8Y2OSnVITfO1COj0xAuTUozlSSn4Lqp7iXHkUx7paIjrFG4GDYFuGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxUJVobbcHwkspRfNQYvAV7vtE7cwdA8abXkoDylgPXQaXCXP3A6UIL0oGx5AY0BcEQFS5x0kR-5fgat_VIyC6kdYhxs1eUwatWGfdihSbRqaHrbPjj064UZmBT4RvTZ2BgH01pvQpegNYjeTtF1s-EOHjLbApWPtHQcsrbuorPL3rh5O6-mdoX64lWNMjEbJS_TYJQFbd8n75tkQ4yvHqLXfu9barjR9g3xmjrs2Na4LXc1DqO17Nnq5gi5o64sOKmZi-m-dxROgSYyM1-gZYZYF8MCOMdfqvuzeIKhVorZcOefkqNR9INzJNpxwdCAdym3ZC2gbpyxxKiMFrxm9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0Wt2MxLqgPSD9q6WzaKBDtNog652DInSBwKprIrd-IeaznhdMzqbcZbAazGpr6inDsoNnY54Q_D6y-VqQyad0TcPiyoU74xbujWOyT-7I9YweLrSUFnbp2S1SXinv-Hv5g3lxchB18HQvcjE4CLPjvwasNRbTzwk0xAdYUPV9JePRvZgpSumJ6qWm8g8K8rdZFB4Rjc300YqO7e3tOIV4GuWYcSxXKyA_HZTz0oD3HJUtat41zcM0h4LmOrlI2KjDuimPHXEEBE6NBVoNIuMOpWL0ArwvptPR37W9EGRX-7YR3j1PTJmkd66nbYv6RafkBtoTxnHVs08u8Xy9cBFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PH9dN6pXjHq0NlWur_R3-_V73Gump5rZ9tAv9zj4FqioEUtDXzLzhJEkDYTCsmrgyNQJWqlfWODDNqCbsA0oCz8KR-WkJLWe_nJtsODiPWF3-AShsSiKEeFNmudiddTjLzYelzF6lAHuAvtY99ibU07ezG4up7_CmsB4OvRy-tlQQQK_aIOukGVkhzNPp5blRI-38mdkdXgoqmZsFMz6vkcWClbg8b10ahSwf6ZFhoTBVgnT4QkPV386eeOvtY661tPWgZmc-QGCO1vnFPy48m_IJTk1C2reTYfpasz-PhG4fqInJexxftRuNhHAzQsInGxVQRpt8qt3JA45iOnVRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMQVO-V7GmJ52RPBQIkl8Sg57XSI-OEMisEov5O8MhPU0sbXEEDxy4vgy4Jc6LqcbutC6kTCSXZ07eCggxCm4qxi9YHBZXj8ESibxDxip8BKwP0zA5RRrWO9s4I-xb5qplUgg3PV9RT6cGUBwhEDAqLx_vOBcmgYZEBsp4eWjrnwS5DeDhx8NCtknx6PBIxxutFq8z6hOVxcImGL63CmO35IWGl0iskbq4SG2AcB7tBu7CWoEP8ZP0I-dJ0CHWSByrSFuM8Om9x1sC9t8Rdh5zF3iCdXppQrWqbFF1dYhvaRZqVXaqZ919BKd_kgck84i-pOkid9U2KPt4OxBirxjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=pdDZeyxnmkQWMJxJwCOtmqDQuCXNM5CCYuigu-gADxl_dIOO3vO2AxUiH4BSzyKIkps-RVXYfpw6bvpKFbgZITdF_R7X3XMBSIe4_t5T0HFBVgRKVcLc6yjhUIh6ZlLQgWBk_XZOomEiQoW1QmnTLIa0CNx2CcIMptFCmc18jzATeywxYN1HBhHnxVh9EkvcxttoFOjIFs66BNZHXKJxyS7WgD4EmM09aJXuBLPVnsCH7VMvSkKIZaEEN20JXjFpwaIvrv9aOYgTnjnr7cTpz7U52an7fyMuYlCeWQVCgUjOZtPwdCGhZe44riAbEMl74kMWGdylKP8miwVkxhLpmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=pdDZeyxnmkQWMJxJwCOtmqDQuCXNM5CCYuigu-gADxl_dIOO3vO2AxUiH4BSzyKIkps-RVXYfpw6bvpKFbgZITdF_R7X3XMBSIe4_t5T0HFBVgRKVcLc6yjhUIh6ZlLQgWBk_XZOomEiQoW1QmnTLIa0CNx2CcIMptFCmc18jzATeywxYN1HBhHnxVh9EkvcxttoFOjIFs66BNZHXKJxyS7WgD4EmM09aJXuBLPVnsCH7VMvSkKIZaEEN20JXjFpwaIvrv9aOYgTnjnr7cTpz7U52an7fyMuYlCeWQVCgUjOZtPwdCGhZe44riAbEMl74kMWGdylKP8miwVkxhLpmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIRV69OLv9t8BfqPrB6844SM7aTh7ZhgFzmRvbPj4k9ZzrdaUB2Ps26mQ0sZaTCEsbLfXK042yAov1-HLkCP-9zt86kJBgiVI9SqnqUab112qq8y0vyqmhNvEShDP6Pq-S2x4kv36hAH95lgUPgfHunI4l-mfg_YVTx3uOLGkqtfgn_e7c5-nBrjTVXC8sxVnLAO_R4YfalNWf7g8hgQkvgCzXDB8dRymoxwHLiEY6Yizt6b7WWzYsl3aZICLEr-gpeeSqD5FRaSGrJr5ZE5SDTElonjLP7D63e_xaG5DZpPdHEXBu_IP1gt-5p7qKtww6yd-xJbynlVWhUVWJDoeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=k1Cmsf4ESiYIKgVRplg8ZRDXQ5YnQHohV5xY7l7iNqssZSIirVA7GJKWyUKUUvqem0D8td4Rtv_CvK0oTr8_zoLyXDWnIdKFiGZtDJ3UKKhP4nnYHxdF5p5iy3M8efqDr7MfLNZlWhDs0uIqVrevJ-KLjrhqzYVqPeIyS9JSzZ9tQCwsrniYZm_dRWM26oPG1xxcdykdWprMrqx8WR8Xcgwi0PuorGYzSaTTD4XXsqOveNbWClcQv72hIOOsNzaKh7jIfpw8RFOxeLmS_ssXmsI5g_ctoTQ3ELDtvBKrh46iOyFj4aucvHOeUYqQu18QKXnYbvTEuUeOkCAKpFt7Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=k1Cmsf4ESiYIKgVRplg8ZRDXQ5YnQHohV5xY7l7iNqssZSIirVA7GJKWyUKUUvqem0D8td4Rtv_CvK0oTr8_zoLyXDWnIdKFiGZtDJ3UKKhP4nnYHxdF5p5iy3M8efqDr7MfLNZlWhDs0uIqVrevJ-KLjrhqzYVqPeIyS9JSzZ9tQCwsrniYZm_dRWM26oPG1xxcdykdWprMrqx8WR8Xcgwi0PuorGYzSaTTD4XXsqOveNbWClcQv72hIOOsNzaKh7jIfpw8RFOxeLmS_ssXmsI5g_ctoTQ3ELDtvBKrh46iOyFj4aucvHOeUYqQu18QKXnYbvTEuUeOkCAKpFt7Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=mWh9obhBFzAdz7M26-CYgu0J4ngw0yrXNVrcFXgHBdK74dO3QOTh4XSGBUUxpXzpDRIz5ufsd6n-aBMv0k7SQiQ8yCUygHsFlXztaNeVjis8b1y27Xm1zh6bdkzKjkBoT3zsFYQcu_uTe7pTTq0yk9Jl9F4No_s7Ppuc9x4gzhGvihUx-HypLqFQWxLgFpYB_iFQR8jACll-fvdNWf0r4CEsuqWpXpC9NCkXb-u-Rp5Q3NaMhOhPJKcqQ6B1y94trEZb3mhRfc8Ssl5CHOHFgtOdhjTd01WprlRoF1VkJ17Gv0eLVHTxDMY3DHJmEG1nwoT-G2san2u0986P1qcSMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=mWh9obhBFzAdz7M26-CYgu0J4ngw0yrXNVrcFXgHBdK74dO3QOTh4XSGBUUxpXzpDRIz5ufsd6n-aBMv0k7SQiQ8yCUygHsFlXztaNeVjis8b1y27Xm1zh6bdkzKjkBoT3zsFYQcu_uTe7pTTq0yk9Jl9F4No_s7Ppuc9x4gzhGvihUx-HypLqFQWxLgFpYB_iFQR8jACll-fvdNWf0r4CEsuqWpXpC9NCkXb-u-Rp5Q3NaMhOhPJKcqQ6B1y94trEZb3mhRfc8Ssl5CHOHFgtOdhjTd01WprlRoF1VkJ17Gv0eLVHTxDMY3DHJmEG1nwoT-G2san2u0986P1qcSMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEeU3pEzCYZ_CUrKZFlhezPhBEreorICsMPAmp68oTSZZlg6d8q7tykw59COkf6l0OjclW5QThkt8j6zQH3qnulW-t9ryrfngF-g-Pd4Pdy2wrq5vl-Vhc2AYCZLGMWlOgmbTvzbcykdz6PU4llCCZ1TbDMemAj0HAMgwOiQG2ohR71nLavTOaRnw6PbdUNiggYodBx6F-m0ma1g2YBa5VbwPUlEO0UT0Ao1-MLlNvpT5haAvop_ydN8rOY2TJ_1U7ksgjnG_9PyVCgoRHbhyfyUMQz3hfy6FLm8IjHil8yig4qYV1Pv7pXyeMR91-5zQxdL1L4nBbaD2O6eowQQOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=cbHpBzNQdyTpuGyNQc1p01AEJ_jSL_fPklMujdYKHIqxahSXTXlJHczmWkKmTk4TIyoyTfl15mShAXwDS5sW3Ql9POqjGAo4JIThHuLfPzKI2fruv34f8eGBBWSdJUP6D6lAMw0N7qCib618oB1LXPg3FS-el5osbMH4wZdETwNrBGtHrNxS0fOUhBUdSKN31sTDOXdzjbeoBLdahqn_lz6PK35qhRhPnePYGWQVg-9AXNJkTyoK2y4xfDUEkU8KOgb_VuDDU__a52IHzmApxk9HMmQLRm2GsLqM3VJ7oCZMwYJCVwGg85Jc0-M-EPpUXqj6A47lvveidP_noWu-bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=cbHpBzNQdyTpuGyNQc1p01AEJ_jSL_fPklMujdYKHIqxahSXTXlJHczmWkKmTk4TIyoyTfl15mShAXwDS5sW3Ql9POqjGAo4JIThHuLfPzKI2fruv34f8eGBBWSdJUP6D6lAMw0N7qCib618oB1LXPg3FS-el5osbMH4wZdETwNrBGtHrNxS0fOUhBUdSKN31sTDOXdzjbeoBLdahqn_lz6PK35qhRhPnePYGWQVg-9AXNJkTyoK2y4xfDUEkU8KOgb_VuDDU__a52IHzmApxk9HMmQLRm2GsLqM3VJ7oCZMwYJCVwGg85Jc0-M-EPpUXqj6A47lvveidP_noWu-bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRtx41_j_pCt2fSpdg-B3Fv3v-cKxeYjTRK5ou9buG6cTUR07QsBT_hziKXOQozxgH876kprv6-zGoFPw_5gaJdQhxL_QUeW6EiBOyxqsjV-OANI8GZ94MNjBntIDCXJy2T80NVs2YWUC3eE3blDNV5-LVBWxJs0opTbn-NbPLL4JX4NR9WoQQGHSNNS8OkxlIIeGOjUzsC1j8j7k6Vio4cUr1H5rUsK-F2J6YI4yNlBnj7MauJHcZoyMNBEDMugo-sQmcDh7uKXB7YaeSTgXkAz8R7XMeK5bEDNKuFvbb6bOQ8XeLmVO4zdJg-_Wthw1yGiZ5yrQaNKFEB7iv6ddA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkVT2i4c0s39QtS-Z2iCq3Zzl9ULI1y7cr1jlLoaS645klEWsjfeanNGN7_GIvPRcCREGCatgZqBkhR4LaJbuyUU9cZQurz-kQEzaRnFKqTIrpklvB0exs2jHCmOBVIujFqriJjAYRbXyMXIvfp7ugtPaBr2LoxOg_jb9-p_HHjRUxWKzBzYahTiXb7TNk_kUR4GzZ6sMU1uKOvTX88tEPGN72TttAu61W4DN6j-USHdt1e46E6Hja4y6XTk8nt588xM-OkOOh6a4zzIbq2RTVGpyoXKJaoaGsZiP-k0b9vC3Jkqlsg3h7FdxYwoFkPGCfWhd7Ut5P-cvgZf7p9whA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLoDdaZHjkdCZAzo7glB2d6fnURe0zrGeUBgxVxPLoyI10kMtyL-OHvRkUeVKGe0q2IUwusgN2wfYuSKtVmfqXDCyoWSM3J5FvoenvucF17Ei7RMF2BYJl2Bn7aSrM9x5NeJJdOZkLkDhgZCzpfpU9Fmew9Wx8ITxZx2TQEj9XjLmB1npYLqD4AR291gzEYt-zpv_vPip1I0x97Mz31D9lxQHkHz35m0-GlutWJcrIynAoHt9-oPuhgWWz69ZeX5P6B1iB6qxxBiSFBKxnYwARWOF-L7AKubZ_a-1bY-BkTcWcB4Z54qg8gOPcaDvFrHanATAVb67n8PlvTRngSnyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5FVn_AO77zIm8kzoAmsuZxZKKkIhcCjtZT8myhlUdgkX7slWkryCPW844N6x-HlgulpH4Ev9QDtEOhBBS4z51yrRjiRya0d8ow0XWBj4gvx0BXqgN1SIklYf4tSS_Tq2_glx3r9rXLhCGRITliKtt6XUK78MRS2-xY1jejtFzWtGhKQJBB4dS3pPBnU35GnfaLv1RkYo5f3iFi0QQY2TbiZyELMRb5t351EUElrwGEnOsqiFx7tDYm6_7A0QXUzqttOALt8h54Jw8Hebx1NBemXmI-GQKBU8psbew0T_VQmntvnRsMw1yXjJYpvDCOSX_KJ3WFY2Zb0xqL2uBL5jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=p2c0liVsn5b1WG7rb_0li5BNFudqEErpnpQGNFd-MUWeCVHT1sAmNRNuPl7bJyMoyLeMP1PcgeqOI1ayGfMe-K1-PdtN5cNCO6TSw3WkT9MaTMG1ec8V4D8usIDc00bpJIJHdp-o58wDxJtj-gAbVYNfwi0xYiiAaitLZMQA5xkGDEL1K6beYNeITXi_pN-XXv43dia_206Hyg66yuRXYKRhP0XPgXlUdeGp3Jcq12Zaz4IFFxJgFwa2pqj7ZGYDZL5j6QQEHgeqV6v4bzokAQeMXsinBXmNNo7M71e7gp1gKnqL7DtgxNztEPcWDV51e9v8dYlH3LyOJRYjopraCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=p2c0liVsn5b1WG7rb_0li5BNFudqEErpnpQGNFd-MUWeCVHT1sAmNRNuPl7bJyMoyLeMP1PcgeqOI1ayGfMe-K1-PdtN5cNCO6TSw3WkT9MaTMG1ec8V4D8usIDc00bpJIJHdp-o58wDxJtj-gAbVYNfwi0xYiiAaitLZMQA5xkGDEL1K6beYNeITXi_pN-XXv43dia_206Hyg66yuRXYKRhP0XPgXlUdeGp3Jcq12Zaz4IFFxJgFwa2pqj7ZGYDZL5j6QQEHgeqV6v4bzokAQeMXsinBXmNNo7M71e7gp1gKnqL7DtgxNztEPcWDV51e9v8dYlH3LyOJRYjopraCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=eWDE4ePIuPwMHD65VpmzU3RO2sTQeyAiQCutANuIwiLbYK23rwKkPJ5pPMIW66oA7kUgxFJ713WlqNdrFzZ1Xy3XpBkX5Br1Chbhmzzm-ALn3XZJrjTQzFc4ILYbB_iqJ1KPBH42w6T-j_LsSOl7v2Nuf0y2YoUA5eBicdZkO5U52O_xGLyF2frst6I4f3DRrRNWNR4pXUSSQ9Nkg5ffOn8EcABaaoFshrs_bvGD7Ef1mf_dgwUxRtuArK_jfAQyeMyeLu_4ABBvTFTjsijeD5YpN3gCqX92njFJk06dSDCpgBt0Fldre_Y7RMj4LYuro56xyjj9xhU1t16sP4cYMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=eWDE4ePIuPwMHD65VpmzU3RO2sTQeyAiQCutANuIwiLbYK23rwKkPJ5pPMIW66oA7kUgxFJ713WlqNdrFzZ1Xy3XpBkX5Br1Chbhmzzm-ALn3XZJrjTQzFc4ILYbB_iqJ1KPBH42w6T-j_LsSOl7v2Nuf0y2YoUA5eBicdZkO5U52O_xGLyF2frst6I4f3DRrRNWNR4pXUSSQ9Nkg5ffOn8EcABaaoFshrs_bvGD7Ef1mf_dgwUxRtuArK_jfAQyeMyeLu_4ABBvTFTjsijeD5YpN3gCqX92njFJk06dSDCpgBt0Fldre_Y7RMj4LYuro56xyjj9xhU1t16sP4cYMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=QXADizSMNPzB3H5pAcS8kDwsHw12wH1i4HQBhXH9Yl1jg2mrBLOtjlihmvelkY9OFP77dBdmXSGIVVblRVLNK7MwVeViyI1e5Y4RIegl5C4LzQnf7mVg8P76nj9KHROr338RHon9cQmqrGCTcdrhoYfID2IZix4yuOzswtLxFxCRrGX7rUay-zX18DftPYf9PVKht5VlaLNPgmuJyGAADtFrJdqSKTsOmWMRX59ofbas_PqODVrBBvK5ZmzINgeMsc6XA4fWHennfvJEDFUQjv2DA_OHVeejhHM9gwk3js-WMVL4WSnZXjHly0pKfFRGgB7na9pGQ3tiM_6JckrKlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=QXADizSMNPzB3H5pAcS8kDwsHw12wH1i4HQBhXH9Yl1jg2mrBLOtjlihmvelkY9OFP77dBdmXSGIVVblRVLNK7MwVeViyI1e5Y4RIegl5C4LzQnf7mVg8P76nj9KHROr338RHon9cQmqrGCTcdrhoYfID2IZix4yuOzswtLxFxCRrGX7rUay-zX18DftPYf9PVKht5VlaLNPgmuJyGAADtFrJdqSKTsOmWMRX59ofbas_PqODVrBBvK5ZmzINgeMsc6XA4fWHennfvJEDFUQjv2DA_OHVeejhHM9gwk3js-WMVL4WSnZXjHly0pKfFRGgB7na9pGQ3tiM_6JckrKlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=SGdNVLE23mTScLY3kHuAWUhU6XXSnwzyz3RnS3v73R_le8UC6INPidSzrfVgDXX2l6MNc2QANmR3t9Q83fYrip60eZ6fstqS_tLRKGyQHRLNyHPPY-xkVhbeHnJLqW80h3eL1mNiWKKDsjN2k6zFTxK_QwNxBUnd6T7Ni8sT5y3etMU5VNRVbK2nn0qk9lxNjdk0io80HCd1huJ0HHuJ_LRlCQEcO8kbo5FCi-U7wo6mb1dwRjAniIwLsUOSEmOwmqqeoUhFHn4Tnc8cjTKl9fDSm6_uIlmHy61oIGKwUMTMEw1Fqyqf-8qWvoUHJzMn1Zumyn3AmRWL_HHvX_EoFUJ-vyBErmb1ALfmP3LrG-VQBeXQ-zpeICNBFNIwlXI_re6CvYXocPk-SQKV0Tx8Q2xGbD0Z9w3K1pe9lxdY9wher0On0YkOGbnoe8ZnqsG7Na0ARcNTuk3i87kbUsKJ1EOPH93bJmtU76amiiVZEEFI8MW3aVaz_ku9Qrm_MQggHW8s0uGzufxu-lrvJVOZWUt43NG8dIkZPqag5u0PA8gQcg07fGrvkkX-d2-dETgeQzyvkfFLJJVE1ArW-OqoGvS3D2A8SzZ6GxNpuX5GdmaMQXGWfehBXEzX4sukowq2lRf1OGMmoKcxJNmB4HzREC-lx0Dp-c8p9GkUKd05ME8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=SGdNVLE23mTScLY3kHuAWUhU6XXSnwzyz3RnS3v73R_le8UC6INPidSzrfVgDXX2l6MNc2QANmR3t9Q83fYrip60eZ6fstqS_tLRKGyQHRLNyHPPY-xkVhbeHnJLqW80h3eL1mNiWKKDsjN2k6zFTxK_QwNxBUnd6T7Ni8sT5y3etMU5VNRVbK2nn0qk9lxNjdk0io80HCd1huJ0HHuJ_LRlCQEcO8kbo5FCi-U7wo6mb1dwRjAniIwLsUOSEmOwmqqeoUhFHn4Tnc8cjTKl9fDSm6_uIlmHy61oIGKwUMTMEw1Fqyqf-8qWvoUHJzMn1Zumyn3AmRWL_HHvX_EoFUJ-vyBErmb1ALfmP3LrG-VQBeXQ-zpeICNBFNIwlXI_re6CvYXocPk-SQKV0Tx8Q2xGbD0Z9w3K1pe9lxdY9wher0On0YkOGbnoe8ZnqsG7Na0ARcNTuk3i87kbUsKJ1EOPH93bJmtU76amiiVZEEFI8MW3aVaz_ku9Qrm_MQggHW8s0uGzufxu-lrvJVOZWUt43NG8dIkZPqag5u0PA8gQcg07fGrvkkX-d2-dETgeQzyvkfFLJJVE1ArW-OqoGvS3D2A8SzZ6GxNpuX5GdmaMQXGWfehBXEzX4sukowq2lRf1OGMmoKcxJNmB4HzREC-lx0Dp-c8p9GkUKd05ME8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=HykAc_M5cOv7JNwDlEGV4lHVy3SXw7Rd5WXtgPn4v-AZcYGu_dL0LJi9zZPcp4OhfweR2Rg-WEsJig5hyd78dww5vgesz74MfZ121x_ScNfI92TbuM-EIhNprUQFfvZT_wDhH7TDX20W33Jx2sCUVrukxVMZKwxaTZzk3UJ20M-Nnd-LzYcc-ofoS3BL1QjttTeQU3plAWXDvZiaokpAV34H912rRoUz1Yr003lWnB268kNotVmxZeXjk_9dqIkHDY1ONNFStKk9PsBeIG74SNPST02NCHugMksjjiSru29I3XabIcjNCgwr4lksPD1MNs4UQ2lr4kavX65AGD1-FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=HykAc_M5cOv7JNwDlEGV4lHVy3SXw7Rd5WXtgPn4v-AZcYGu_dL0LJi9zZPcp4OhfweR2Rg-WEsJig5hyd78dww5vgesz74MfZ121x_ScNfI92TbuM-EIhNprUQFfvZT_wDhH7TDX20W33Jx2sCUVrukxVMZKwxaTZzk3UJ20M-Nnd-LzYcc-ofoS3BL1QjttTeQU3plAWXDvZiaokpAV34H912rRoUz1Yr003lWnB268kNotVmxZeXjk_9dqIkHDY1ONNFStKk9PsBeIG74SNPST02NCHugMksjjiSru29I3XabIcjNCgwr4lksPD1MNs4UQ2lr4kavX65AGD1-FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=hzpanN7acsAURHgFJjepKkfjB9SNs67-JeICbxwNQwMDQBX1CE6v9Sdv4OzPPbnXu9keLs_FBCHwyD94HaT1bAoDpC-1iSJi97N1B4u2jHUzSZDCTdvXXsombKviBRrbn8UWs5vfmctZJ_fl6kJpgJal-8YkpqZWBao5kr4btqVOReEVximrmHudjppLLb7HAOlO41vh0Myopn6h66i4lUthcav45M_0sCaAGxYvWDv0vQEErs28WtUFrpGK-EUXmq32ukXqYokw6fZP2EbZGOzSC-20XMXwu5R5oSSSC_Znp7Ot4qSZOZ4FcU0uiPXPiuTVtpZFIDooJF45EKkSkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=hzpanN7acsAURHgFJjepKkfjB9SNs67-JeICbxwNQwMDQBX1CE6v9Sdv4OzPPbnXu9keLs_FBCHwyD94HaT1bAoDpC-1iSJi97N1B4u2jHUzSZDCTdvXXsombKviBRrbn8UWs5vfmctZJ_fl6kJpgJal-8YkpqZWBao5kr4btqVOReEVximrmHudjppLLb7HAOlO41vh0Myopn6h66i4lUthcav45M_0sCaAGxYvWDv0vQEErs28WtUFrpGK-EUXmq32ukXqYokw6fZP2EbZGOzSC-20XMXwu5R5oSSSC_Znp7Ot4qSZOZ4FcU0uiPXPiuTVtpZFIDooJF45EKkSkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJ_LedEnWatn6y1efgTUCAINeAwQf9_zgLF-IP_-FYv5gLMsZs1TcvWUkC_UH7HguzeyG7Zv7b7c2F_9tJD3qs6WnVIbF8r1MEk6ouT77l9dk_HbWzEKxmsJT9qCRkq0eonEnI-GxtlwUokv_Irkmwrq_Oq8C8Kb8lMNlsxrOS_n7fdJ3f8PWynXg5PYrc-lPQ-oy9IkzsM6sqAZ852FGyCfRf66HvwQ3N7DdCfQFTdrOfAtgBbu9RuluGA9YoiTgRV2GmBvroE982VEa86WLHVzlKkv9kGGVztDZHiZs_MWjwn3iZDwEMI2rdm_70J-faVzvM7hrvnlbWqPfyVDRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=NsibcaCuQbV-1F4XXujWODVFQJOLyO5HkzchLDdPL8NDv3chovnLwzHsrOzs5PVMNc9Vj_ycvnp7a55MEWuRmm1rxfukNdsETtBo5GsWMTzKJkS6Vza4sStxVXsuY7y4D9I7GEYs1HqpdNCoqssuHKdpn9IouHAnvdhQi6Gv2k-H3F89zf1pkHaUjEfvlskDG9nQpU3s1YzyhMB05EQq8c-G1txx-SxecMDbJhNhpfx8DwkBV3ZvOnjK_9INzPfQMQWUfhiPPyeCjWE8r7J7a7rcPa_pCAWqzNBDpgQzzI4xgs7EYl3Lup_Ir0UvLOGZ0nhA1Df1luaQaTkJ4s6yhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=NsibcaCuQbV-1F4XXujWODVFQJOLyO5HkzchLDdPL8NDv3chovnLwzHsrOzs5PVMNc9Vj_ycvnp7a55MEWuRmm1rxfukNdsETtBo5GsWMTzKJkS6Vza4sStxVXsuY7y4D9I7GEYs1HqpdNCoqssuHKdpn9IouHAnvdhQi6Gv2k-H3F89zf1pkHaUjEfvlskDG9nQpU3s1YzyhMB05EQq8c-G1txx-SxecMDbJhNhpfx8DwkBV3ZvOnjK_9INzPfQMQWUfhiPPyeCjWE8r7J7a7rcPa_pCAWqzNBDpgQzzI4xgs7EYl3Lup_Ir0UvLOGZ0nhA1Df1luaQaTkJ4s6yhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUE-NsS-1b8a8o6TTvVrmwU6pe3vYpQ0ZSyj1AI0QcF1lZm6hcZ-M04o-fknl7kW_2C8AER9EFjgNYffd2t7yDteRRTlxHWYiknD6dJL3Jjtcq4CNCzpBCb1sT7vH4BE5_zSDqkoV4ReyOYliac_TpBKFUWc0dSGDyAPcBITCQUUflYbJw4oRD3PBJFbFiJunRQ1mH5_odUOhww2Q3Way1C6pQChok8nKXiWdibSXtRc7ZrDxxDneeu_3GXco-vz5UsTHJTzmc8_qUhbgimd2lr8w8bCkENu20r4dxE67MjyKNcoTTjnK0KkO8TlDn58IVZWHZEwVqOUUw8zQVotpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRgO1WWzAjq2nnauFxpXZVqQgK7Y01P69EtIBWncml8C-i7BZxVBGhDih_d9RPWn34Vre5WGftnV6-EBChI4is2ksw-1Qs4xm_qfSfZ_MVL6TzAog8NDIM-B5LznOwiLQ6Kt4HwQo07WuNSUsDQpjXY2wFK3kY8W116LDFDIsXtKBkIN6RFecoEdlyvnszXTSOtmZ0xQC0XhU3GNzaHliz6akDAV_rHsDkEygHrW-ARee7N0eoAxZebSH_t8OcpZSgtP6eKO6GC1ZTKcXL79EWfzZ4pifAwc9fQSE_4q0cl3_5Cb6yjcdZep7FkVUBMKHwQ1jwB1176P-0tlmp_jHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=cSquakSDCg4fFOHVPJKi3zDKcTTPyiU1li4_FSp7zN0tfeaZz43vVVlppTiaBRCwwrDAAGgMK697Q1L6ssqHEEPV11l8MAvkeasnihDPAKVD1a3SBs9VPfqQoi47H5oIZ8R14NCg0PES9hXYEVASVHysRX3Z3TimMSFPdY-oHRbRxCzsPc6mbTs7t_m4ZXjho27maxAjGrjz1-_RkKRhk1uxS17Ulx8nK5KiYho_NT52I_0yE5_8FB-uVV26wjs4ERY-mOXBRZfOW4H59WKnU_VSZ2fowggil1xMeWA43qcnCnLHXvn416Wq3XHP3KfA532gv0Vet5bk2m-zUKGtiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=cSquakSDCg4fFOHVPJKi3zDKcTTPyiU1li4_FSp7zN0tfeaZz43vVVlppTiaBRCwwrDAAGgMK697Q1L6ssqHEEPV11l8MAvkeasnihDPAKVD1a3SBs9VPfqQoi47H5oIZ8R14NCg0PES9hXYEVASVHysRX3Z3TimMSFPdY-oHRbRxCzsPc6mbTs7t_m4ZXjho27maxAjGrjz1-_RkKRhk1uxS17Ulx8nK5KiYho_NT52I_0yE5_8FB-uVV26wjs4ERY-mOXBRZfOW4H59WKnU_VSZ2fowggil1xMeWA43qcnCnLHXvn416Wq3XHP3KfA532gv0Vet5bk2m-zUKGtiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=EOpQTzfbR14geAYX0z-nWL-WI7ZrQU4T3zP8FbK7lqCplOb6imLLyFawtlU2-M5htBzWH92PXZAMdQ9LCCK1GCVoknTdKgvoRzxAtW-oER6sycsnMx0H_4WcdrCBPzb921Xnb6i5Es3U2Hlioxeei9l9mnLtiTFI_N0eQ8yBtcNlLWXzT4qZSAXNsJihhSv13JcKizy4rohbG5SZpb0ypsJsQtD-kaixxTJKBBecDuxl-1GotTfZ8f6NYBmbkzc0LZIj0Z3l4uQIW_7Pmg1KcdK9F6T64nIcPlpafmZNCJKR_ZD9PnTBMPSafZt3Y-STQKO-UaOKOFHu27jYn_T3OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=EOpQTzfbR14geAYX0z-nWL-WI7ZrQU4T3zP8FbK7lqCplOb6imLLyFawtlU2-M5htBzWH92PXZAMdQ9LCCK1GCVoknTdKgvoRzxAtW-oER6sycsnMx0H_4WcdrCBPzb921Xnb6i5Es3U2Hlioxeei9l9mnLtiTFI_N0eQ8yBtcNlLWXzT4qZSAXNsJihhSv13JcKizy4rohbG5SZpb0ypsJsQtD-kaixxTJKBBecDuxl-1GotTfZ8f6NYBmbkzc0LZIj0Z3l4uQIW_7Pmg1KcdK9F6T64nIcPlpafmZNCJKR_ZD9PnTBMPSafZt3Y-STQKO-UaOKOFHu27jYn_T3OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی، فرمانده کل قوا ۱۲۰ روزه قایم شده :))
خودش هم در جنگ ۱۲ روزه رفته بود «کمین» کرده بود برای دشمن!
که در جنگ ۴۰ روزه غافلگیرش کردن!
«ما اینجوری نیستیم!
خود ما پیشاپیش لباس رزم می‌پوشیم»!
مجتبی کجاست؟  :)</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=jcz1cnBJK_2z1EEHobR7T8yITxE3ZX4enMKxWTU2-iymU9vu96Z6_4fTNTazvPzWvLDPn8ajDDCYZ1WxDIB3iK4gad_CdIq6KaIH_d34sQZ1lctub1qRYQCOSUCCjnpGgCJAz0I6KLU9Hwigmi_IPP5DHeTZHXzFc3AAsCHkinNoh6IH3iAbDicHgo61oQCATuExJQr6embHIUHC5z4yQVcULGo4rHE3V3oCvn-Els4HcestLr1iKGW4IYr_OPpw8ozzG2xwiIwzCGpZCOj6QISwqBNqrnE97uSCm7SGMJlKA6ZZrSxOpLp-nXc1ORPT9Iz76udgaY35c0p8wLFDJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=jcz1cnBJK_2z1EEHobR7T8yITxE3ZX4enMKxWTU2-iymU9vu96Z6_4fTNTazvPzWvLDPn8ajDDCYZ1WxDIB3iK4gad_CdIq6KaIH_d34sQZ1lctub1qRYQCOSUCCjnpGgCJAz0I6KLU9Hwigmi_IPP5DHeTZHXzFc3AAsCHkinNoh6IH3iAbDicHgo61oQCATuExJQr6embHIUHC5z4yQVcULGo4rHE3V3oCvn-Els4HcestLr1iKGW4IYr_OPpw8ozzG2xwiIwzCGpZCOj6QISwqBNqrnE97uSCm7SGMJlKA6ZZrSxOpLp-nXc1ORPT9Iz76udgaY35c0p8wLFDJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrIcdOHfXERahUz2oFkyveDwpvWia0_UkbrNIfNFHzmVz864JDngYVt-h7yPvSgm0PiSXx3K1amt2eAK7ftd8FHnetUaz2e2AJJwj8jTfSvzNJd7vL8WITkB8Bif3GOhUSPXlZHotByH-lZGG3BzhK-ZoEZE6xxHN6-g7MCVOMVB-hSv7cH7DyS757Pfat_qpiXzURbI-CfkE9kcXG1pOk0ZJD9gU7Nkp0YOckSfHgNiAWFrJzNvQtoc0zCpFxwX06tZUU5_fmKbWJoeiDHcjOCRzy8qJ84Q737_qmhseWTKREaMaxQoBgXsamwL7utKegjgeJxoACMIjyfrkkxqHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=vhJyY6EBEzYEC9d3jYtJ7LNMCV0EMImqky9s_EGlVaBvxVTsEBEvUeC2aT6YxbYtU4lrrOu6gqj_gPC4FOSAkCLhyQD8fIuzegvaOTulm7PfsfqVZYuHsJddZrSg1vTzOiWM-W1DME-VT13FKMH8OPPW-0gAqPAvUQqJ2NevbMrT1aUQ6QmUGuTy3XYwPa_nMcGSvpsUMuXCbA3u9U5NytfTXjvrkV-Yz453PqUxvEgDJ3bYhgZFe8aElC-3x1Ygw8759GpjLzFjuiBoaeA3FuYybDlbmPiHGRgwf8EOavF1PXeRI406t1Bq6xiRrrN3-1LoH6xro-uEsm3RPfWSyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=vhJyY6EBEzYEC9d3jYtJ7LNMCV0EMImqky9s_EGlVaBvxVTsEBEvUeC2aT6YxbYtU4lrrOu6gqj_gPC4FOSAkCLhyQD8fIuzegvaOTulm7PfsfqVZYuHsJddZrSg1vTzOiWM-W1DME-VT13FKMH8OPPW-0gAqPAvUQqJ2NevbMrT1aUQ6QmUGuTy3XYwPa_nMcGSvpsUMuXCbA3u9U5NytfTXjvrkV-Yz453PqUxvEgDJ3bYhgZFe8aElC-3x1Ygw8759GpjLzFjuiBoaeA3FuYybDlbmPiHGRgwf8EOavF1PXeRI406t1Bq6xiRrrN3-1LoH6xro-uEsm3RPfWSyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=IqPPR1Fc98QJKNmtLmbQ3rGCNPV8NXBaPtQY-T0qe5UUl_I-p_LGvF52eMggBJj8pwBIFeWy6l6t8UZ4W5Vqi9zqS6bYY1BRUM_0VahdMHdUWb8hrZb0siMrbKUjI39W6rkjs0S2sTaiXduZaUCSdAs5bg0m2t5OHR5n3dWiy9sFbwyAu5ykTnzwPxITEa6rzHcgJubd499Pwz2rcCd9udwAoMWZFbwY56TMtXKZIb0J_lcUF_RZerUIlzGFC3E5nQxW61kGh4wQmAvlyQZIC2zMNwfHSK6frjzrLvYla9rHrO-hKUAuUsFzDOm5gTz47spC0MsHZmbme9pwA_CitA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=IqPPR1Fc98QJKNmtLmbQ3rGCNPV8NXBaPtQY-T0qe5UUl_I-p_LGvF52eMggBJj8pwBIFeWy6l6t8UZ4W5Vqi9zqS6bYY1BRUM_0VahdMHdUWb8hrZb0siMrbKUjI39W6rkjs0S2sTaiXduZaUCSdAs5bg0m2t5OHR5n3dWiy9sFbwyAu5ykTnzwPxITEa6rzHcgJubd499Pwz2rcCd9udwAoMWZFbwY56TMtXKZIb0J_lcUF_RZerUIlzGFC3E5nQxW61kGh4wQmAvlyQZIC2zMNwfHSK6frjzrLvYla9rHrO-hKUAuUsFzDOm5gTz47spC0MsHZmbme9pwA_CitA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=qKCaFamnsjJqJ2mNfJ_leYx83KXuuJfhU0b4TI6yC7q00JsaVWZ0sA_1vJ1LWmbUnfndXuYCN8MSVU0DduSM3PVRRfeboswCFWk7edP-peB5H-1ZO1_HQ5CGPbkh9g3LRjE9YDJUxm_qZ8_2hh2GEJj0e_gl5JL1Mvs1nMwQiMOWpEQRiRvthVLytOd7tMcVZlLTwPKBzjWFI4Tr0CV429WOsuNbxzuLbVlHEft_AeN7TJ6slnMc3dgk7Tv5tAtAgC5gZAqdCG3y0yv3o8iS0NFMTM2j4SPeETLy4YY13h1TvQYRUCnFVxDq1Shz1vPMXQgLANTFgBmxaPor2_yh5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=qKCaFamnsjJqJ2mNfJ_leYx83KXuuJfhU0b4TI6yC7q00JsaVWZ0sA_1vJ1LWmbUnfndXuYCN8MSVU0DduSM3PVRRfeboswCFWk7edP-peB5H-1ZO1_HQ5CGPbkh9g3LRjE9YDJUxm_qZ8_2hh2GEJj0e_gl5JL1Mvs1nMwQiMOWpEQRiRvthVLytOd7tMcVZlLTwPKBzjWFI4Tr0CV429WOsuNbxzuLbVlHEft_AeN7TJ6slnMc3dgk7Tv5tAtAgC5gZAqdCG3y0yv3o8iS0NFMTM2j4SPeETLy4YY13h1TvQYRUCnFVxDq1Shz1vPMXQgLANTFgBmxaPor2_yh5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-atI1weuTUgfLR93vq1VnIArOU-mJtE10riKIIOmSx0oR4udBg1sSA0I-Y2vEZRfK9rywU4qT_gXlxQZzwMpz7vLa_iBA2q1bfi5vjN9_LTUgtHK3QNtjDUHg84zV_IDNr7g1OxR5njBMzsk_RMkHxzKIfYKz7316IJ7fUQqAPe6we-6LXb4udJuR5Nyddbhi8JGknWRknJ47XndBrdMbWeK6rtRaW5c7bCigFo9nQ3kGhBs7XJUmIJ12b4qe1HQ-SrQTxJJmokxSH5EUeD_uX-0BBchEc15ZIZ0V8UjAuBn-XKzuKlEA6MC9vRXkwzkLNVK0NqcL7FMinoOKhUEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=BYKTjr9zPjgJx7fZFbvZv-IwABsMTToh0f6YvkWkkDQ8ApvHg0I7mEgRLfF9dxxDz3231KloPSr8ZgPuwWcyr8t-yydjtPW2fDiKDD5wj1y22A7rE1dHVbBCr2ctOtc0ikiwr6DOlLy1WyxDbaa5Zx7NxC1QxRzau8g4A1-ZFZt2YTArT3fEsoeyKZ6PuPe41GB3q_Ca7joJzKlfMK-xoIRN9v_lLeNy_z7-RklqAbae0M76sCikW5aiKL1MHr4Y_54qx1ghCAxUZtGYBUp0jAVFz4HVa-JnRN8w05MCmwdObdKKiAkBAtYzydXgtH4AUWi49mhbBNIR3PvXdjkaeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=BYKTjr9zPjgJx7fZFbvZv-IwABsMTToh0f6YvkWkkDQ8ApvHg0I7mEgRLfF9dxxDz3231KloPSr8ZgPuwWcyr8t-yydjtPW2fDiKDD5wj1y22A7rE1dHVbBCr2ctOtc0ikiwr6DOlLy1WyxDbaa5Zx7NxC1QxRzau8g4A1-ZFZt2YTArT3fEsoeyKZ6PuPe41GB3q_Ca7joJzKlfMK-xoIRN9v_lLeNy_z7-RklqAbae0M76sCikW5aiKL1MHr4Y_54qx1ghCAxUZtGYBUp0jAVFz4HVa-JnRN8w05MCmwdObdKKiAkBAtYzydXgtH4AUWi49mhbBNIR3PvXdjkaeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_XxaaDNRMHyY4Wga9J1qCzzQHF2u8OLL97UtM_NDeHWvVi-KTAvtt9uBig4OTweM9-6pUlLYREIvUQdSkWJv9YrmYypsGpU2P_-viiy2hGfJrwkD0aTCHXQumg_iEqnDjB-iSaaz2dogTtiI2xAM9Rcwwp5UO9lA84dZsvUTgm9YGYHs3r8lt6mLyekHbLmbm6qJWfEHRk5a28eIxYgArtrgtfDrhGuEmWDBGYDhlCwScO-VcTzWxdWvNkwmVAnMzAI7GZjgsXrhC-QdrYA4LL8Ap2s1id8B_yqrdkQQNoFQxXSqg6GTxwbByRnmRU-vH1JJalCn-Axpb-Qi0bGNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=QFa9X8UC1qmX9L4TavB3gtGA07ew1ORfNBVZBM1iwDdKVNraxZAIe8PGO-UklZyqC3l5trKUcvCxVywBRjmd-tqW4PZqHsYQT9NtC_jvW2c_qcyBzVJbUgldiLgY4ApNDh2SZf6YNfQSsT8XwsRVRL8Ekk0iz8EKAT18ibpaN7k2kkJA3FMSYB07BTjB8ey20uDOG1A1X6jKbNxPAbBmfDr0krPgEosArKD7nCPuonitXOMnZXftFAJTBgxu5Fq5f4S0cSb6dbChPcrw4U_4YYvRH_TVI39pLdvDjHpJb3NOSKQ81VeBbJFYnV8vGqzzi19CjrkACNfy95MYTtjk4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=QFa9X8UC1qmX9L4TavB3gtGA07ew1ORfNBVZBM1iwDdKVNraxZAIe8PGO-UklZyqC3l5trKUcvCxVywBRjmd-tqW4PZqHsYQT9NtC_jvW2c_qcyBzVJbUgldiLgY4ApNDh2SZf6YNfQSsT8XwsRVRL8Ekk0iz8EKAT18ibpaN7k2kkJA3FMSYB07BTjB8ey20uDOG1A1X6jKbNxPAbBmfDr0krPgEosArKD7nCPuonitXOMnZXftFAJTBgxu5Fq5f4S0cSb6dbChPcrw4U_4YYvRH_TVI39pLdvDjHpJb3NOSKQ81VeBbJFYnV8vGqzzi19CjrkACNfy95MYTtjk4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVCyQdsinB2WSzYFYHgZIXXsUEz0DgTKF1lFDbaFRfchQeHVDaILBJtXOWAHbHCavudQgsdGkCpn8UEk826kGmHBMiJ2K0oVCVVMMbc1uBDqzGsE8N7PKSatoNHFdAMcTeT-QsX3RauNmJ6GqkCg5NMEX5uA9h2IyXBDoKVreJx6Z_JERB3oHKSmtKWlK7s_ZFsCWZc9TsXHXNNS8fghiLXqfTquyuMMzI987GONIg3czkNuV8VjIVkUMK-7rpExV2Egl9FKRBHtum8lGUMR4NgibU1dq7f9wKcuWS0zrLNCbYu0JtF9DjIEdyV0ii_71FCA59rqag93ATk9k3oMyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=LVedQkB8j-TNG99peac9U5rmGGGcsa-rNV4YsmraOryQznf3PSw9TEDtgtETFCy_2e_QOgP2S4qE-R4pR0WlQAn9aRSIdmgpU1576oT9ZnhN_6uniyt1fty3tV8GotdjNSV13S7D7CmmgDuEWTut1uHw4VLu0C26iu4ZK6OLvmSfWW1KozTUTkRR1y67Q1qF_BhdR1BJWojc3XSfCSO2czgjiXygr7CY2NZzOujBZH5szsDccb9cq0nv0ICV5zkS_c5TlHGnqW8cIB_rvuQUyZdwWVhZLQaCOxgVZ4A6Sj7BZYNf7Z8Q-6SEfr6QWPWkTN0kwh9qZVLhLmn4x1FmzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=LVedQkB8j-TNG99peac9U5rmGGGcsa-rNV4YsmraOryQznf3PSw9TEDtgtETFCy_2e_QOgP2S4qE-R4pR0WlQAn9aRSIdmgpU1576oT9ZnhN_6uniyt1fty3tV8GotdjNSV13S7D7CmmgDuEWTut1uHw4VLu0C26iu4ZK6OLvmSfWW1KozTUTkRR1y67Q1qF_BhdR1BJWojc3XSfCSO2czgjiXygr7CY2NZzOujBZH5szsDccb9cq0nv0ICV5zkS_c5TlHGnqW8cIB_rvuQUyZdwWVhZLQaCOxgVZ4A6Sj7BZYNf7Z8Q-6SEfr6QWPWkTN0kwh9qZVLhLmn4x1FmzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tgcrLr91Yfahi7aDd5prmagy5AqneqxMOPiGLS7BU3L02AklWeoDuz0EX2pkDaQ37HHk_fhweVQKuGPJPjlpMABfhtd1TfsUILs-3cv80g4Os0oDbpEv3AYuCg4naekg9AdRyRDR50Jjc2cS7csuIbt2Vq3hGrIBf2CAiXIwpaYvaFncv4tuwNanXIVdtBgpzCKWam5--cFh1VF8AIPNyc3Pd7_K9jUJeRbp_F9aqLCRyXtQvJM9Xpxu01mSgsfwBvd0-ZAxaBwzqrbTTopoMsMqCakf9QOZd6n24EBMpRDYmrrCMmtb8jGxRHHbB8EcRfxkKPEbpTn7QBZ6PvSatA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uFEEyOxDZ_H4cQEx7_g98SPT1bCn6DjsHgWgySsBtjqOj4gEpZsWWnDU9VCEWgcSM5x7qGakysgYejz0pMzoemj8SFlTXwBCtnOLXzNdDQpITSuwy4mnHZr-OdwVkG93MhcDGaRfbhTDDBNl4fZHfijs6PIWZ2S0iZPgcfemORv_DvQirJNLbgXQzFm4Dc1rB_6PpyLQx2h3_47d6gbLHhCWQRaB8JYYeKf_3AbHbrPR1rT6-_eJZgq1YPZg0XhwnHpzzXVMlCQrXqWdZiUCzR1Y4pNaHxnUkSIbDH-c9ibRpNkrJRMnseP7zD-Lv7PNc2PjANAl9NVhS4pzOyI9jQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=mpjpfS4NDjUzmUj11h_L9Rxvv1x370aArN-JWGVNuOrTN0_T3avqcBX4n51Nz4s-nSm0luBmaWHmBCISc7ZkV6u61L3olJvZ_0PSNLQWbAB4elrJZYh9MIBF-8dwnd3RThNhXBu6r0w1jsxaRCKHKBfrSmbSgKVL6yPgzoBfLGB3pZUdqvNNwP1JBrUn952is-SJ9wD7XSX3_nBu5WUC9zCoZWGZxjKJeqFUIji8O_fHiDYdzkgvPwqJ07VZ8Zk5lIxg-OCLJnpcL2VOJTyc4Swep8DGOLOIzMdsBN9O-Ei64MRUIZJRsLZxnlakOEVvH7P64IFYeRj-NvMPkEZ8JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=mpjpfS4NDjUzmUj11h_L9Rxvv1x370aArN-JWGVNuOrTN0_T3avqcBX4n51Nz4s-nSm0luBmaWHmBCISc7ZkV6u61L3olJvZ_0PSNLQWbAB4elrJZYh9MIBF-8dwnd3RThNhXBu6r0w1jsxaRCKHKBfrSmbSgKVL6yPgzoBfLGB3pZUdqvNNwP1JBrUn952is-SJ9wD7XSX3_nBu5WUC9zCoZWGZxjKJeqFUIji8O_fHiDYdzkgvPwqJ07VZ8Zk5lIxg-OCLJnpcL2VOJTyc4Swep8DGOLOIzMdsBN9O-Ei64MRUIZJRsLZxnlakOEVvH7P64IFYeRj-NvMPkEZ8JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I36udPQzagJBD1RfKK2Kk6nuydgB4enVMNcTxRvw9mn-ESTmYPfYsE4RDrxxnezIY-fKG0y3osGQm_2xoXyg7mrKouKJuoo9uSGvPZXvx_ON3xKH8TNEQOfZZ-xGu6GMio-fbzCZtz2eLZrogvKiz3aoocoyWY7ALvTphs-uV4_4hU76AamQakEuMktQ90TxWF0WnbO0pmgksq6VCxc2x5PtOEETrXSRTAS9rghEoUUnsTiK2Sxm-qMDXKEgbUTugKlEEIg-D-HHcu7gUUKu3oFzwSt8h8-0UvWH2XB-4VhvfWiqhGrIGdfnlLBVXfmJyiX0hF0areipYVri5XtFMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4Gt7bWHXE3BbullfFON0vwRmBr9lFFBLfvUC191c5lGxksAZk3JGSZ3nN67DToxXaLYdNWLFNZGTZSpkzzn3dDbdgcass1N6OeDt2tWHJlqjbjwIpcH0W4J6nUXVUh0FdRB3wts3O_9PpaUd8mE-lkOpQArm6P8zbDWegfHMD-uammyxPAfQpOd1zl6ZZECS_Kji1udTCiZFYa_3wQUWtdcMSQgw2eVYpwWchf3i9ZI0LRkSUxg9VGhr6I4RWwwPqAbqSArlYRcmrQRvBQeSgyjXvKvJS8vwTvkForZx_CbG-QuAum2yZotgNt0RdxX2xDA4iuCF52ojKzG32c-tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cw3VLzPJj-iPeyJ4JNnbvX0nalp0rVf6mehbFTqEBvSTYCqK4_Jk4prMYu9NWZwAqWroD6zlrucUH3R5Z3s3HHfBMDB-jxli2o48yYz9xEKK-WtLf8D31U2iV-SVRaLBtg7iwRW2Oc-sqzkVjEXq7NYIv55z0fcPghIZGprTxC1Cpn1UFu524tAVRK08Uouh92XX4cMSVbP5HoYyRg5YkryzhVov2L-b5Zak5BmX_yMeVYCNGhZIpodpa2bwPuk2BDXiPOduhIP7Ul4FQsCR0cC49k76BlUtUa8UPejtwNfIPLjqjinFe5jqYcNUN4acoupRzxNlEbJdp46we3lTrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_TRvksuhvSDs1QuCR54AWBC_9P9lKbffxXFs0UuvQQFuGtJZdcbEERpH3azEn1gGfRw1VO7SM5Q0N0qBFfNPA6Nmt5jNMEqQtFrwL_NZH3zWTW-ZHRxIuggK2p686d5zlifBUW-c8cVGmui72bh338JQWF9dv5Qj6l4jkvW8kcJmsqRA8FQAPK-bvEnPE0cLZ4Ph3VNPQ7ALsz1i32PVqvt9v-OGCIvOjrFagkFVwkJlN3voLpKW6JQz021FsLvfWDQuqzE1xc0fJGOarMGYL3Ho0b3tFBVoaPWK2ZoQ5rqHt8uVYGCDwPljnEapAd9HKbHDTwZw73Vpe1TgUEX2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
عراقچی : مذاکرات برای دستیابی به یک توافق دائمی با آمریکا، پیش از اجرای این بندهای تفاهم‌نامه آغاز نخواهد شد:
🔺
پایان جنگ در لبنان
🔺
رفع محاصره آمریکا
🔺
صدور معافیت‌های تحریمی از سوی آمریکا برای فروش نفت ایران
🔺
آزادسازی تمام دارایی‌های مسدودشده ایران</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-iDxyDyRAVNKRRvPZ4gCA9UuvJLzQNfBEpsWJ-raz7E2wLBu1LIDmR2FrHKzExD-hc5DWo_ovHsdE0Dx-nzNn_2LK6Mdmr5v4et45zL_GcN6fq2EFB7a2jloiyA_hl20uL-fDustXc5F5mAv6EokxNnD4Osyg3_nu3a70KzG1pMb5rT92ynzH29hVyMAmA0BxlnCUtLdEOSBrPwHTQ5r-_Iszf4uCgb2f63calRH0mD7ocbTYbEXdkBtLy_5-8DGdgrOj3plKmTO2sqQJ18MNxXopk561a63NJSW8xPPqf4yTgwYm2CrxWK6yxCCLHFoECiARvNdp33xGFaYIPa8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=FgmPfU_Lazfl40JQ8Vf0wrswKOWuZV_JpaTB6O0ccimNRpZzhp3qDdD6bC7qXunJEAYGNjlQFNx6TLLCmlHd3Xymfzl2WUI5CFFtZcu3qshCIAmrQnhgGD1PYBrQlonOjmaF4IxmV1207zxkcGy0rIb02zPuzGftDEsEJVnBWHFqR7HlexPelLTxriLUHYvVSWt_H687WPrgM1P-uH3l3kq67av97ob4KGi84d5QEexES1XkmJc9eC9i0hziwYpM_tnNreZIC8dVl4I4y0QVapk7oGQaDO7PCCo7o42eitnY7xkmLahGv3iWt8crd2_FwDzXIsiAwKOadAU0XUmp7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=FgmPfU_Lazfl40JQ8Vf0wrswKOWuZV_JpaTB6O0ccimNRpZzhp3qDdD6bC7qXunJEAYGNjlQFNx6TLLCmlHd3Xymfzl2WUI5CFFtZcu3qshCIAmrQnhgGD1PYBrQlonOjmaF4IxmV1207zxkcGy0rIb02zPuzGftDEsEJVnBWHFqR7HlexPelLTxriLUHYvVSWt_H687WPrgM1P-uH3l3kq67av97ob4KGi84d5QEexES1XkmJc9eC9i0hziwYpM_tnNreZIC8dVl4I4y0QVapk7oGQaDO7PCCo7o42eitnY7xkmLahGv3iWt8crd2_FwDzXIsiAwKOadAU0XUmp7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=gHl_lQt7xQtIyLzzzBoNC64J--lZ8TQArwLvzmOIDAD4ak2uIO7BA9Ilm7alH6GwTVeJDR9uBWi_dsq7xsPEHItv32G2vnXnsiJqCbtpZzZNgNF5hMCQfa-Vi45oBiw39AezhCdRx7cVKvrz8gPgiQ9EZZ2jg2ersg83vfphEVKKQ42VwTQzwXDV7IJskNJhh_xE0_Y39gFBO1gBBUb2b2O4gQ37oFhLwv3cXULOGCDN8c7TnBwJHbgrAM3EPTsy_0v2uOSBSkNIHHHrR2-9J48g9hMpK2jeEEHJ5i2D-npm-OwjLHSdjo3diCSMqXjEYtJGr5FMrD0IYNtnjSqi2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=gHl_lQt7xQtIyLzzzBoNC64J--lZ8TQArwLvzmOIDAD4ak2uIO7BA9Ilm7alH6GwTVeJDR9uBWi_dsq7xsPEHItv32G2vnXnsiJqCbtpZzZNgNF5hMCQfa-Vi45oBiw39AezhCdRx7cVKvrz8gPgiQ9EZZ2jg2ersg83vfphEVKKQ42VwTQzwXDV7IJskNJhh_xE0_Y39gFBO1gBBUb2b2O4gQ37oFhLwv3cXULOGCDN8c7TnBwJHbgrAM3EPTsy_0v2uOSBSkNIHHHrR2-9J48g9hMpK2jeEEHJ5i2D-npm-OwjLHSdjo3diCSMqXjEYtJGr5FMrD0IYNtnjSqi2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=KdaVskOwJ_qmYLoWxZPtEsBfwjQz2JKEaOeqEREf27gdUnwhfB0DNNBW1vUtL2AD4hmmet9Rqh7Lj9unM-RAVpkG_tlm2lPI14Sx1P9Y0Ew18v8z-nrQwD7UR0STIrvDO_URO2gFuf2goLHHgQH8VfC_dLQIL1LKlUs1PngrNy_M1H6SoNrs_hdGyD5BG6ToXcIdBdQDFZ84zwVj1Z02quKtqoC-2JHt7pSeRmCQBbl9mLtNv6RMQHO5HGp_e_4S2GzXTrIY4ik3oZe1DDQAGqxEIaZ1y60rXS_lGdPzAqEtjtE1-yWGhJXkGWxqULCijD82APvmYfZFON3nYGRoEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=KdaVskOwJ_qmYLoWxZPtEsBfwjQz2JKEaOeqEREf27gdUnwhfB0DNNBW1vUtL2AD4hmmet9Rqh7Lj9unM-RAVpkG_tlm2lPI14Sx1P9Y0Ew18v8z-nrQwD7UR0STIrvDO_URO2gFuf2goLHHgQH8VfC_dLQIL1LKlUs1PngrNy_M1H6SoNrs_hdGyD5BG6ToXcIdBdQDFZ84zwVj1Z02quKtqoC-2JHt7pSeRmCQBbl9mLtNv6RMQHO5HGp_e_4S2GzXTrIY4ik3oZe1DDQAGqxEIaZ1y60rXS_lGdPzAqEtjtE1-yWGhJXkGWxqULCijD82APvmYfZFON3nYGRoEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=gtl0YneLU3OMTJfbu_wXzRFj0YNMvy1AtWI61oDxREHkgfcDrq5YCaKSfzlQH_22P7x__QKoesB078SHBaHWMm8saiANUw2ZpAfdZEllzp_qb7EVSCprFTIOLnySi8Vzz9KUOW8qeLrAp5mOtFCbrxq3ABoNm1wI5R-vqrBhP_sACaUQRiUz1K8PiSlernEOtp9aWPdvxyj4Phhj-q7USBcdYCSw7J-uZM5DgCQfDbhfjYtZbuZDhC35n4larqViwCQRqAjPboWaiX7PUUPkpG0JOmxwvX6B2wbOyHmQ-C4gSL7dVV_HecnV6ZqgkkdgdM50wSP6a74Q6BReT6QHrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=gtl0YneLU3OMTJfbu_wXzRFj0YNMvy1AtWI61oDxREHkgfcDrq5YCaKSfzlQH_22P7x__QKoesB078SHBaHWMm8saiANUw2ZpAfdZEllzp_qb7EVSCprFTIOLnySi8Vzz9KUOW8qeLrAp5mOtFCbrxq3ABoNm1wI5R-vqrBhP_sACaUQRiUz1K8PiSlernEOtp9aWPdvxyj4Phhj-q7USBcdYCSw7J-uZM5DgCQfDbhfjYtZbuZDhC35n4larqViwCQRqAjPboWaiX7PUUPkpG0JOmxwvX6B2wbOyHmQ-C4gSL7dVV_HecnV6ZqgkkdgdM50wSP6a74Q6BReT6QHrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIPPfwdEkjTWarDsi1j9n1y9xFCN-jAF32ZxKlcF25lb76GLyQjIODFvdNrpj0c_qOqiSXlDn4G0PYyWDTYc9cwo1oomulSIULWWxHiy8xkHnzyFU70-eVsuaO_3YhSebze6FZEcG6cFoY564Cw_2yt0VKeSl7CVokvW43OMvCtvslZngmNQzFEEP-GET8m679cyiW88bzaUMnYuydE7vgObtySZvXnNqGH2Lw_xROyHTNINiwWul0L1O_r5UF6e8A7Ihq20DT8HCPOoFiWrpuLDJ4geqjo1NMvPa0qg9SXWpCd7XQAiC1Ppg7DZkBUZqrJgz2uO5MpHOZLo8yHgbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSRS00OfU0Kk64fmcsgHvMaOXa49p1P4BwhcAql8HTFTUrONZklZ-BTL7JUxAHjWKt3U2UMCUcTmvCPK5AYMQm8TGVm3dHVYz--ET85aNk95UQDqMKYLQ6R1i_i5ayYckgT_Hr1bmy3FIQbVikigAB70Y_iQ6n-MmemieCxblHjSbfcpoS2hYRafZ84Qex9sECjRjuM7T7xjyk79ysHsCCNEl3yzws9TDhO5mlCYS8s_eHDcVUNGZ6zU4xX8hxn2ZIpEAnPhqJJjvvuTV9k_zFCflQIhHOvcYT0Gw8TIRZ-n2NbF7hNaoo36t1WsIzuX_m2h2FJMCGL3xJQBFx0oVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=M9ujGD3bMVW__vtGmkTqgzzEWahkCoUgX_9lcG98QHSf0RzyLDdetdOvC3vhA_2R0IvBerEr6cyqz5drK2KB_5WcuDOtyatqxsk7VDnyFTZBOu2QIHB2L4eLSuxJQO8tJVyRZ1zJNUbe1iFo2_Hvr521ilUu5F8lfuO5jFUGxjaPJxUKcFjh6UXLX-6qMwBPAqU7VTXabUplIgEwrXujYgoV3M_HzN5PNIrhk_Ku2D8mawIxatbn_lrQlZdaPsfddpmHe9ClDgBX0iGaBNttmUszlCnE0o_z6RZp3azMCFZ8P0ZvQeqf71tZilr1_AYXUtIwxUZ7tR-u8I9fIIYLpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=M9ujGD3bMVW__vtGmkTqgzzEWahkCoUgX_9lcG98QHSf0RzyLDdetdOvC3vhA_2R0IvBerEr6cyqz5drK2KB_5WcuDOtyatqxsk7VDnyFTZBOu2QIHB2L4eLSuxJQO8tJVyRZ1zJNUbe1iFo2_Hvr521ilUu5F8lfuO5jFUGxjaPJxUKcFjh6UXLX-6qMwBPAqU7VTXabUplIgEwrXujYgoV3M_HzN5PNIrhk_Ku2D8mawIxatbn_lrQlZdaPsfddpmHe9ClDgBX0iGaBNttmUszlCnE0o_z6RZp3azMCFZ8P0ZvQeqf71tZilr1_AYXUtIwxUZ7tR-u8I9fIIYLpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaXaz4ggFOW5UWdC7K369qgQPExz9yh5AGcLupF8_l5Wxuma7L3oQHQazfaLfg8v8un9WuhXuSIzE3kjM2_H_jqbct2wz7D2ux62gaS6BVG94PriPnYHI0yW7E0zHRuO88WOAR5FNcqengD0mmpklE50E9bT1Wew-eXPXQ2IMGL9MlGB82nUZJNSdpBleCknOyuvkN-hiA0mpMENyruiF9cnnvnBz0K5BYH4HSyF6ebJjmdTw3Kn6jrl_OjcUCUW0cFmWmBux7tPu55phcNrVV-38O0PDdFv93Wj4N3KbGoBJbH0MSZ52cFrYJGQy5CZ2mc6B1rNijmnKJsQj8-Dww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=H-U82FoiBvuliUJJ26hQa5NI1FwvruKkACxq8r5064o2ikwVIwE-rcWN2FABXNG7bdCK_5OGmIdpWxT5OUurZbO_gQkOJ1x8HCcrnpquY4YpBQF7FutUz3YDVs1gCHQmHfNuYa7x-Fn_AWknm198OyApRDCrr8ueuk_UzLvUz670JqZ324XXzumuXBwMtLvj23E3brVEUi_JIByhAVyhOHG7KcHRHTKkdfya1cW7McsJIoKCUZwcYl4zYucpB2EeET4IIZ_bUQLYJaKABzBUEi5L-78f0e-dTyFYbGv_VtAkNwApuTUIqiyEBbHsz7s5YqgspELVVV-ij_vhb1jCuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=H-U82FoiBvuliUJJ26hQa5NI1FwvruKkACxq8r5064o2ikwVIwE-rcWN2FABXNG7bdCK_5OGmIdpWxT5OUurZbO_gQkOJ1x8HCcrnpquY4YpBQF7FutUz3YDVs1gCHQmHfNuYa7x-Fn_AWknm198OyApRDCrr8ueuk_UzLvUz670JqZ324XXzumuXBwMtLvj23E3brVEUi_JIByhAVyhOHG7KcHRHTKkdfya1cW7McsJIoKCUZwcYl4zYucpB2EeET4IIZ_bUQLYJaKABzBUEi5L-78f0e-dTyFYbGv_VtAkNwApuTUIqiyEBbHsz7s5YqgspELVVV-ij_vhb1jCuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lerx-WDXEUwK5fX_WRrUctnZejmFjQh3HYMhy8Sglfb0zNExqnmaEOBn5Ru42XiRolrsdwa_g6LcIDZerB1Rygmqko2gh1PHWdCb1H6dgNLf0fQNBWhOtWmwHVsEF0wDF-bowOjgEZVr-OiBEZH5mER38qKLOpi677MGpThLjCXuVO2kMxJWtLJzBCfwrQ8RWZyI4l3gG65oIEZoFDBEha00DolIPt8TZUyY3mxEGOjVj540YkoE_vEcr6xF7soZ1QiqhbSPW9lT6eEJrlVJr8g94W-faE1ucf2Ki-dWM4zwULCZRgkwfTFhmQb_jKowMfVwyuTvLPo4nGNfarOCgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fL6cjaEBZ_TarDXHdD-MBTbG5DV9hiQrwt7T-xat6XjVrqpKT-07ONEhR-vWX5zF2S3wPU6WIIvnvoCXBZaH4wRm2Wq6s47s_I_J11YeZdnG2YLryOoYLM27QioqPvvs_I_KCDOHZSAL8iuulAcFj_GIDTZxOJWgG0rYDmxa2xPavIWiGEFW7_mPrOKjpzJznykRqyf2Re6RbJMTrXLmHtEg8_J18F6I7SHqGMM8FNJjfckFDP3KfVHPI8Hi2oYcpwJG2P8euhgoEtSZfN9LDqRijAPmMQERWZT2CJBa-nObp0CfDusuzkRxCxuV0nTg1t0njJIsMDy044uUldnldA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=pEvizL76KowG4QljtVAYa3eV-JLJ1jInVg2lPqKad0iROlVSU8PQxdpnRmgo52cSsjdal79joQhEJbDkxUtH35j8SauLlKYvT0BVsqoEWfRVeI1Vp4_XF_FmyI1B_Ed9R_3Q2ovu4UYTk4dHjIC1d75uK_PlT2Haj-f0KQ7y3HpLpWDYQcenwJvAEQN5DotbYWIj-kS6C1l2HhcTPAtZufZ7oaH3NdBrYIohEffXLSQm_9FkbvE0tqe9ASe8e-ef2B8gF92y_ZMSv-YnhrAIZp-tS9LJ3D-OxugA4Hrjs0UQRxfV5L_fwotZ2W8gmYWhrEZpoaQf40RC7RjMf35lpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=pEvizL76KowG4QljtVAYa3eV-JLJ1jInVg2lPqKad0iROlVSU8PQxdpnRmgo52cSsjdal79joQhEJbDkxUtH35j8SauLlKYvT0BVsqoEWfRVeI1Vp4_XF_FmyI1B_Ed9R_3Q2ovu4UYTk4dHjIC1d75uK_PlT2Haj-f0KQ7y3HpLpWDYQcenwJvAEQN5DotbYWIj-kS6C1l2HhcTPAtZufZ7oaH3NdBrYIohEffXLSQm_9FkbvE0tqe9ASe8e-ef2B8gF92y_ZMSv-YnhrAIZp-tS9LJ3D-OxugA4Hrjs0UQRxfV5L_fwotZ2W8gmYWhrEZpoaQf40RC7RjMf35lpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=ZhZWZMDxk4imLvIXYTQGNrONNy-cVwIvcbdWmdnAbwlrw2a2M2Hgkie8z7joN6UI2fxgxd63tJa8cckNftYZue6jRR0GyV4kS-Z2vbS1KGk8t5YDH3MymOEbhTs6cyW6buzumRUtFHrAHnRSgnRTS3_i3KvC9FLxJXfqgbyM5h9Gq3ZnYmJClgDMix8KjUEAytFLUHOejQGcrrSPsqmGc39D1L-uTqO8FuAdpPbE-3MCzvg16pr32FReJo19mVY6_mNAK-dOIhi3PO_ekaddXwzJBwh0uSK4lzp8ErEA_rPIDY6aUBxT0lixnNz-dLdcidn6aNakB4aZfXDlE6vMPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=ZhZWZMDxk4imLvIXYTQGNrONNy-cVwIvcbdWmdnAbwlrw2a2M2Hgkie8z7joN6UI2fxgxd63tJa8cckNftYZue6jRR0GyV4kS-Z2vbS1KGk8t5YDH3MymOEbhTs6cyW6buzumRUtFHrAHnRSgnRTS3_i3KvC9FLxJXfqgbyM5h9Gq3ZnYmJClgDMix8KjUEAytFLUHOejQGcrrSPsqmGc39D1L-uTqO8FuAdpPbE-3MCzvg16pr32FReJo19mVY6_mNAK-dOIhi3PO_ekaddXwzJBwh0uSK4lzp8ErEA_rPIDY6aUBxT0lixnNz-dLdcidn6aNakB4aZfXDlE6vMPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOlH59G8Dwyi14RB3lbfXLPuQndu_7FH52XsvblG5sbZEkHPz6oBX9epFE7bAdLJ09NsbCK6j5RlT3rgHKPYBaVxLuFXcAGcVo3YZnbgsJmf4Rnjptffo3b4XeH-a2zrJ8MkEcTqPswB1JFBXlrreyibEowIDTCRuuoyx1GzZQfsjZqXBqu5YG-XH4E5_ble7g4ijb9k9Q1_DA_sVFnK5iv-Je3-fihYptlVp7RT7PxFXkNj5TL6OqKDY8XTqh60Df54XkhUGIgK_cqau3Xu0lZJZcWDwXybGR9LE3aJd9V2dRKbKfHt4pn9qDebICtVgxjJlCTUeCS1g9yCSjqKzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxn1vFgsPOZNsoLvjDsgpXwFnLAaf9E4xc4219UF_djy91BDt5XN9bWap4FMxOYqY4HfKPVuaGxkSfWqQDV-xYUtN8O64haAmEPfMpAEVbh_VockVgpRDjCUJTSo7G_uNVQ3F3YkGI46gy3AiqUc27w9ZL5OVnub3JWCY-76E5BWde2DAXqZUzfbgrhiTMFhbo-DrAxq4huX30ppOiDoFo1ZIBMypPrbP30cH80LZwOYr8pYI0svNWoezFPfZr0HCo3QzqUdtVvD3eCQyommmRR1LFe5bk23VIEeCJnAWSF-tQe-YfbeEKRt_kVwWtY4DO1LqsnxO1Wikpna4dcXpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMzYTsbwTRwPh_VwkW9zdTpKu3qKdJsPONUwip66HydGVq6gPf_IFMriuQUffKoJ90YQK65GrtwmsVv2dwgjK7tu0kafhHnYnEwLgtEAxXGn1u-9ZHmPHwUDa2lhK7bbU2FDizH5OhHhFQbQ3UlhnYXPQeOEnCiUyHf3ss0oS1oCwkC0-vFGpUjj5Q6xueksIMUD6f1qGf2BpbRS2xQyNCHLg_k8F2dkNcIMjjOnf9lMs-L60r6S9pjiYbAOAVGypVrefQUsVhSz1daAuy_eiPfLujiA2UTZfhelN_bGjYAWSG9DgwSPJz3qlMynzlWQeqAwKEPBKiqQn01zk9Q8VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=qh_udmqDQN5kSVXKYGDc5H2S5TIwiijzraOk0bDgD0-HqhNJ2pOK2oN6qxu_CWyF8OFpK8RvcVFd6VFXHCpge4SNDQnAKSHga4cJzTJJSOB2I98SSQKWK79vshAEYM0OW_WRwaLnFUzVd2vnuvSiJvfzB92ckIF7GVUtkNO1a2HFAYrSya8sVjBRm2pNdKD98J7xdNRJ5ecsIEniy9gmFOyYhhB1nqfKPwnUZ266V133eGqLsVYUdP2tqyisQN-xy1ZlW4dELHCRJSYqpmQ7IHdzbQuvTEO2w_mgHGlJT5C6LW9ndW5bz9CZxPomIWHl4LOM6-AomaUisS7xQKYuMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=qh_udmqDQN5kSVXKYGDc5H2S5TIwiijzraOk0bDgD0-HqhNJ2pOK2oN6qxu_CWyF8OFpK8RvcVFd6VFXHCpge4SNDQnAKSHga4cJzTJJSOB2I98SSQKWK79vshAEYM0OW_WRwaLnFUzVd2vnuvSiJvfzB92ckIF7GVUtkNO1a2HFAYrSya8sVjBRm2pNdKD98J7xdNRJ5ecsIEniy9gmFOyYhhB1nqfKPwnUZ266V133eGqLsVYUdP2tqyisQN-xy1ZlW4dELHCRJSYqpmQ7IHdzbQuvTEO2w_mgHGlJT5C6LW9ndW5bz9CZxPomIWHl4LOM6-AomaUisS7xQKYuMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShcSWVM9Gs9QphBoT9j5Ai2qnIsVg9KYuYD7IhS7uQA6HIGY-t2FOfGWUuKq6iS_SBLWwj78TBSGJ1EtlSNcC7RDtRxmvfMGTbSAG0H-E9e-ral59P5bf0FdELgAZIENE5rzsc_0iV_0RtvyPnFdFmq9uDtLwjWDVtiEVlcpPhoVjnXNUCdjGaqWW5x33OdbctYjamso9NkpB3KP9iIp4Sn8dPlOrwN615jpt8nxpibo9_wraJdJG-MDFVuHkUAfdY5CnxmSJPxOrb10rNUjLaRV2WddQArks1dexVRSphZtTGePvzu3iMlDJthdkWkBWmlGYDOENfyUoSckz0VOhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو
به
ترامپ
اعلام
کرده
است
که
اسرائیل
بند
مربوط
به
پایان
فوری
و
دائمی
جنگ
در
لبنان
را
در
این
توافق
رد
می‌کند
و
به
رئیس‌جمهور
گفته
است
که
اسرائیل
خود
را
متعهد
به
آن
نمی‌داند
.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-JkKRjD3g92n_FSeVjKYZtrRCOxdx2UEjz7qn6Gkp-1HtjCSIpln3-SzzH7v3ioSx-YlcIIwCYM2-b6-vU2gHL13fIFmybaBdRfu1xiUVC3CXkphsZsXPyN3gmRNAcn8r6KMfJ8zHZJs7QNQk7XIZaMXM9B95PUEinatEuN9jHeYRAjRO84f6jATTnbtGK1fdjMbcGGzkvKXfPOyrd8MqKBZfxL8gdRdQnIMWfQtYce4SrPXjITzUDbwCZqOv1bNTsbejvAo6nTlssU0lp8gMOojmI8zdTRx3IrMc2-G0qNLoC-3ERgpkTdhIUALp2DRPmJQB15XLbhYIVKq1aLgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
