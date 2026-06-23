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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 00:41:14</div>
<hr>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBLBI_814qgol_DQ-CIl1yYSfSaQxp2B1Wh4_IPFEmFgWj5VT2ZvlYgB9pb-ulo1GouS5z2tOfgb9OfNsrEo72Uz-5QdMHBy24nQbSTQMWih68uQAlNetn9-OoPgStEbfTHFcNbAxwHyQjDhm_c7q00qEh2N23igLiJzk6T1eJ8ppq2b6sqSJyXgaMIG4_CQWnN_Up9o5Or7YKfnf0QzqRt-lTdMKVWG162UQws8oCy_JDAK6ndbTkLL6z_PnTkX45uNns93HqbTJtqcf1XxoQj5cfl5zLfRBkViNdqFWpaxr4lMiagnhqhX5G0GklWkwuhTKnUbRg0f396JybuvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_V24fwnlSEn8pBtox3mpxpxImaYlFd8e44Kta2sIesLQWwRF7pDZ-lW_UHBH-F9OuUJXOBB1FfbiCJ1RibqaJ-snqF452VaujAF8rVwShBgO3Pk6yq55d_s2H5xZqJ1BmADKlUdgg7wCMYaL8kKomfWkB4F4aY63FA4JZmD_ZrXB_3XfVCVWmlGHdiiwsZmmIxrZdOLcLTU6DWWVfKm6fl0IAFlw74qL4ai0_-dPjszTWYa0THkpBJL_fHzGRBcshnkDDHwcT6yhQb-_h4SsAVMeeYzTPhMhtUFGHL-48vTp_vJzh-paPiVuic2vTSu7ImpBdUH03OUVD0BtmS7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmdjgjWxEQuckLdTv8N3YkIHT3mZ55uTCEXVEUmtjcfR3S65A0FeSghZc-Ylw45bbMoUqmy-q9SR91SOM5Ov5-vW049M9Lj7UBlVvKcH0KXXOZ3DraVoVEjjyCvNdx9F_UCmfjVONHnp1xhDmMBEyQvqL1y4VOCgA8zJyqel-NHIzFL2J2AAHcp57cvhoh6JOWAuIytaYpljmJUqWRJaDdPo0GfC3_JrIfeASDwpXycpqetSMCnQzC5f32nsLm0PZgj0YuIRJUEKMTn2pcinS_jnXxJxPBFJBs0hLFapJvQqs4iKiKJarxVXzDTCU3nV_LkymwNc6qxHFz3hrnn2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxFz44CZ3kCcIgGOUlCTGUOCPURyLb_cAeSaLvPM2ekdL4k2M37l5i5nh841-GHVldDo1VaB0hj9oNWOCYQ9-jJ1TgUjp9BYC-lLGlLhO2cyx2KBHh8guuCpZ5XuVljXTHBGW5gnbntOK6JHOr71R3wTYvKAufMCk4-8McBJ8VWQkEJZ4eItyPPiOkq7ixntWJl33r84zbsKvPaP0-10gZSbC9JRfjJc4AKIgTJhEAv4gmWuwxchKotejflOBmjiZbL4DkcnRrsYtoqqZjnpsxNPAk-wCdhIa1bYa4FSvo1SkBSdvmT8qvEJvlRJCU6hfh7FsMh5x3ichxPd0G-p4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JX2Em57BlV8AHrCHXvQjzSsDaWeE202zmSRAsTfJuGGzQsv-Jh8ge2zHT2DcmIyIgNLjtjcYMybGx2PhoCZpj3sozzZm_mgvUjOxPzGgihLVSe75kGM6KWfLDcqYDK_BsrdkhA5tJtnBE2xykOk0Rp_drzY3sOFcgnoAiWQsNXRD_DbrNC4y1rOgPYrMakY8FlT2ApJlTfrV7P3sqomo1OLUyErcB6gxvreLz5gedLYyhSzszeXYbKAukjh8Aytr0LRJTUgqev5ZiX8AB3rSUdDo5Jfh98HVtj2ccTs-LOj7G-2_DR1jgqjPwmhI_NFCkeISF_fstFLoSOXSasXSlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwwhQ_ldICT3cRxJOC9cnEmlZb48JEnIKoph0JojT3KgH-O8p28FTG36Cvr07UgOAhgc9_mFZHzr4ei0ZyZGrhY9cQHi_7RMxCp5g3omnn5u4oFU3FLJCe7vYMtNB73PS3tcuT8RIk772Ow3mPhqKPnNnFifO3HiTw7uauOX_XKGFuI1IG7InrMtof-xF2z_cdpoFbvRKxx16w4nNVLU1B7Vh2kmaJTbqs7p1PFrDC6yxyeYt0kZZFevLf-eokatdnmAE-4qY-IH68ha26oHawX3LVsRHeXX8UlrWFeNnqoExJaiy2C5AWA4OsXMQfpniReeBSU_PDFLKZFT4L-lLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auWQhte181tZtaQ8odEbOwJH8ebEO_cW6ipgqWAMhphckX9ARTWzv-M9ZtAZbZs_M4B9YDd1dKlsXBvUodvuTiuXyXStg-Iz25OAerezG6YozWoS_f2i2tBI_K6QDoreoXRIhKxGO0xCObK8fiocWpOOyhpk10AGhty9ziTp1USJN-5Fn5RDH84GYVO1LceoRda8iKVV7BRJkR2XKH4MqhwKJB9IQh7mwqQo58guACQagKwIO9pYHTOfr2LpVoaBsHWourWhWtaRC4p0jBQ2JDXlW-0cAhCtiN2yuZHkRIdSivbUemHeg-HCzmX3yDv4ZiM1eVMuYg5_dpplOKP9vQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXNug49A-F96RAU5CFhuXWl_z027fZ9BeTgLFQ3hsJZtpD86nabrkNhPK8haCFDaSjYCR1ozW2kaWl6bVyY6F30stFKSckHdsS5JNgbokkv-xQBpJG37UOuX3oENvJiIne4nV3BndTDUSu8mUuQhxa-LjdKxE4WSSzqCp5YL3t-KgEpweZ2GBimdxP4iJHfXlaPoD6YdTPxW6cDNaK8vkiNk91EJBxrYx0DNGoBeZw4G0H0jnwy3Q9y7V7wWR4l3RMvaAcwvNTB0ux-NvxVsy_lde_HqItyESmLOvy5g7OFNmTvc42YevUfp6OEMABsjNYBpsNIhRWR3zxqNVVdfXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxUJVobbcHwkspRfNQYvAV7vtE7cwdA8abXkoDylgPXQaXCXP3A6UIL0oGx5AY0BcEQFS5x0kR-5fgat_VIyC6kdYhxs1eUwatWGfdihSbRqaHrbPjj064UZmBT4RvTZ2BgH01pvQpegNYjeTtF1s-EOHjLbApWPtHQcsrbuorPL3rh5O6-mdoX64lWNMjEbJS_TYJQFbd8n75tkQ4yvHqLXfu9barjR9g3xmjrs2Na4LXc1DqO17Nnq5gi5o64sOKmZi-m-dxROgSYyM1-gZYZYF8MCOMdfqvuzeIKhVorZcOefkqNR9INzJNpxwdCAdym3ZC2gbpyxxKiMFrxm9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=ARQtdT0WWzGXwxH0S6bc8r0x4QA0iizPZCeQjGWvtyQH1aANsVxY9MX6nmeXo5X_xxgs-df1jpxBrSPSkKNbR53bgjCx8q830E8crWG9Gf80QvS81P8t1KP8UpvHmg1SM2ivaq01w1cUDG_LpEDaDvJk8kGEHa8sNuWBaHPmb6XMkzo_FyKVMisgY98B9l_jbxhG-R237-6NL1h0SEa7vkSMiHaoYfH-y_xj9QEqAFImwdLlwytGCYnl0pFG8oR7q5LRNq2wet2lO0nbf6YuwXYeQvW55Fn-PUWaIpQaHO3kVHtbyCBLFQyFrPabASliGHH5Jnt_KSQAP_7IwnlesQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=ARQtdT0WWzGXwxH0S6bc8r0x4QA0iizPZCeQjGWvtyQH1aANsVxY9MX6nmeXo5X_xxgs-df1jpxBrSPSkKNbR53bgjCx8q830E8crWG9Gf80QvS81P8t1KP8UpvHmg1SM2ivaq01w1cUDG_LpEDaDvJk8kGEHa8sNuWBaHPmb6XMkzo_FyKVMisgY98B9l_jbxhG-R237-6NL1h0SEa7vkSMiHaoYfH-y_xj9QEqAFImwdLlwytGCYnl0pFG8oR7q5LRNq2wet2lO0nbf6YuwXYeQvW55Fn-PUWaIpQaHO3kVHtbyCBLFQyFrPabASliGHH5Jnt_KSQAP_7IwnlesQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZ2rfVjKKuPLDGVPwncWMp_Uv530PwhqIM9xpLvX7uPl947a-RyQcH2GIx8IA4G5dLrpCu_oE2oR1Wa0RGMHkTFR9lm0GP5LHty26Ry_u8Y7EDLjM4o1BF7UAQn5id5jqmRDohB0LMV_wAhtmmYcNo5CzlBRglJfxLdHpmiu_UU5_9zd4ns0OlKZwR0CXVzJBmOmK81gzGJvWLpDHmZocrcd5mx5J3jeZW1GrptXZ7m6K1Ly30_vTawPETegbhzp9v6A5j7XWr05FskBBSejjOVya6aPPUFIBRTCBJciHkr4i_ElR7gISyWry3oWvRFHgNtr-YyvMGBH2TiXryTdnA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=DCQkEmGx6uYSopzHls09Ajn7zLUXL2o8K3ws5Kca9eBpHOX4hR3qYZvF7CXYjbhHMjuaaM6yz1D3GDs3zf0gg6ls1p_ODg2qkq5y3GjD81JKdaoZUyo4k1EnLionNdfrxWIzAwMrDPGciaNMkW9VNbOScD5Gwu_kspT_Xrr_YKSs1PzYikePooGS6lVKv6c3FcIFrHruifELGSnQTO-xB5cyF_JprgB4oMxjyMWSIx1WfyceHRDcdYhumv2Ij9vhf-VDYldaX02e4WWEZHTj4hRZarpvvAMI-pa2-N0afoMAfrq5ZFglR91Su_2O7vwhw3l2C6kgyV8EwiwwWRJ1SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=DCQkEmGx6uYSopzHls09Ajn7zLUXL2o8K3ws5Kca9eBpHOX4hR3qYZvF7CXYjbhHMjuaaM6yz1D3GDs3zf0gg6ls1p_ODg2qkq5y3GjD81JKdaoZUyo4k1EnLionNdfrxWIzAwMrDPGciaNMkW9VNbOScD5Gwu_kspT_Xrr_YKSs1PzYikePooGS6lVKv6c3FcIFrHruifELGSnQTO-xB5cyF_JprgB4oMxjyMWSIx1WfyceHRDcdYhumv2Ij9vhf-VDYldaX02e4WWEZHTj4hRZarpvvAMI-pa2-N0afoMAfrq5ZFglR91Su_2O7vwhw3l2C6kgyV8EwiwwWRJ1SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BP62j5J8uEwKO63AVFYXmSa7jZB-V_jbQpnA4pXzyDnTvw_EwvtpZoeon805fGWrIx9X60TfGB8NUm3r7cDA4hxJWoWze-6M4AtEK53kYcud1bLoiSIO5-dJD8xA8g-umnp4CCdNiGG3aHwxMWy7E23Q0D2UFh1nunj0DuZgqpP9AJhP81iWxMAmxNpV9ZalHXR4qQRUPmv0324W38svRz0X2yp4UnyK__-GZwQXNaXMQoulHZDlCVfPJO8_CysmS7MtOE122uXyV3lZYT7A3QG7FkuhKrHVzBIm9bTokcUBPqNxSiu5MfFntWiUle8FxhavI7ZwfKm8AilvncbN8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoZRaHdkuap8tiRTy4IYBR8fXtvkQyQvIXvRZobDhfBmWRAPG45jjrsZpsCKF9YpE4mSa-hoPaZVTxVyMq_cNfVkoCP27T9RrUL8_7g4QlGvsAEcpB0zFgPY7_qCipMwFsF3H6NgaUafVPKRzBkMG_G6pYfD8khSuSXYnV1LLk-2YxlxrqwOC03ta5rzUZM-BTC9Pb_x0xSDvPTQp_kJp2PbuymR0URlTlhTVwTN8e_MNMrlXmMc4QAqS1gmapC8pvOmRrffq9tNNpWPabU4eNpZgiumVumNvXdrGOiWg6e5_D609wbqU7o01nGBxraX1HRUC7vQgvhSvUYTLlo35g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amsIYaT97CHUAML4uTpD3mYaAjjYQpb1tIaX3aQTPYB-urX6OgGMVeSoBkIyRkjOq-f55ngPbF1jclZYHvOvkR0XMmB8L_iQFXIf4ib0wrijJDCXp_Tb-jxN9mYS4EkwjUSValYi-p0TApd_Z9la-TRhVEKeCHSaC_cX_FCM_8GxJL5hMTYpwZ1SaPgZRGnOWEb4BYAHep47SIe2BD_Eed20hRzsrQz2G0ctQXCbuuChEHJEaRF2hie67-XZanxs1tMvlGwzgF9hXuYA05Xr8NPWPE5mZYmrnyjeLq7V9gI0I4sWOW8oB9Tg4YDv1k7I3F4jNZUkpkxF4FhO5E1_3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsQv48Kv-9zlq6T3PfGUepc1JD522_KVZxyIpipL_dfW83A1bqIgX_8POOolpuN9VTOi4xnq29nGH1hpR0X63_BVoL3-frUprNI2p6V0Ggrr61sIDYjJRgrUrRnqGS-zB-HWLJ6oybiWKaEVCYcZKVp3ZXZbl_m4TRW0UDbOG4p_wLBx1tWzwFBBcf7VFKgLc_6KsHB6bvUYRXOVm-mEkcLFNyjXQrBWr9Y_MYNrKJDw5og0m5ltD9ai7WQ1TJpqm5LZU9VmnghbH-qbC7sCbTAy3gti15fW7CTnIWwwyJulAsBpqr3CaJiqVsfebtA9A28LpBaMUvWLB4vZqRSUmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=D5RbbKzBySoQxOYg7vGUyKCM6dlsNzigVggTVoRtCBQaHtyRmNziXhTVf3bxgpyW6Xb3n-Dr89f0CLLmloo0cHJ3omE9rllc2CCvioPnTiMjwqrIx88VATz9HcNKGHPugFquAeR2C5CodIAdMSV06wQDHB0Yrt11lUgNlTn3KD1ftYWlz-xxYv3tX2okjqY6K82SWCJwUBorUhYAQJT0roXw7eZP934CHivHhXWFTciSRz9kaYofFF-CI78WwzDG-CkPRCO6Edq_9USAWUmWl7ocU7sw0yd-HtVW4UrIRI0h1Vkggnj9bGHPEaDMhQOzNVXcyxTRQb9qpxJysXDcbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=D5RbbKzBySoQxOYg7vGUyKCM6dlsNzigVggTVoRtCBQaHtyRmNziXhTVf3bxgpyW6Xb3n-Dr89f0CLLmloo0cHJ3omE9rllc2CCvioPnTiMjwqrIx88VATz9HcNKGHPugFquAeR2C5CodIAdMSV06wQDHB0Yrt11lUgNlTn3KD1ftYWlz-xxYv3tX2okjqY6K82SWCJwUBorUhYAQJT0roXw7eZP934CHivHhXWFTciSRz9kaYofFF-CI78WwzDG-CkPRCO6Edq_9USAWUmWl7ocU7sw0yd-HtVW4UrIRI0h1Vkggnj9bGHPEaDMhQOzNVXcyxTRQb9qpxJysXDcbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=JqE2ogJ6DgsS5xcGkQfiwXacxa-kRpn6ZovUBkK0IoZWqBP6mBLJ9TpGk8Z7hE2IDkmy9CpV2rHuG5R09XxHeqY_mSAOvCEohsEknFawmdnA1vke0NLdjYjc-Mk5TvNbK7qUoo-8s4UhICKRTxsqueqxHII6ixetNGJy-dSixf566iCEsMxDX5QwjrKr-onTKecDX92X-J158Oj5hRTyMWrKumQvpcMdTjsEnnKyeWH8Srn_N2t8ENjz6K3ELrgFq_J9ruILiZnI9cbB35WXsK5lsl4EbYCewRuW8Q3bzqLIHsX-f5LRGRkiUkC4vS7JqPbq-pHmplsiRwkDT9p-ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=JqE2ogJ6DgsS5xcGkQfiwXacxa-kRpn6ZovUBkK0IoZWqBP6mBLJ9TpGk8Z7hE2IDkmy9CpV2rHuG5R09XxHeqY_mSAOvCEohsEknFawmdnA1vke0NLdjYjc-Mk5TvNbK7qUoo-8s4UhICKRTxsqueqxHII6ixetNGJy-dSixf566iCEsMxDX5QwjrKr-onTKecDX92X-J158Oj5hRTyMWrKumQvpcMdTjsEnnKyeWH8Srn_N2t8ENjz6K3ELrgFq_J9ruILiZnI9cbB35WXsK5lsl4EbYCewRuW8Q3bzqLIHsX-f5LRGRkiUkC4vS7JqPbq-pHmplsiRwkDT9p-ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=DEQI8oxizBiZ3duC84d1hc21a6RjoyIibEWJbg8e4oqX9uTfxj1qtbr55Ww1IEYU05fMtNZoQxRGamVFYMZkr1Pgz2PsE92SJPpvh1mODYGwil6eDKN_NaHLbHX5KZBURcquj22bb5wdPWE_MQtUrfDYcdrf1GcAsil3moPktq7p45xjUJ2QtKJbemdREAiCdZRwAQeYXlxh2zTeNFP9myq0ApVs_5NgIYJcrQt-jCYLwahkthe9PmTBKR-gGWniGReKiWIb1yBtetTH2-R-irSnbKDSlPejm0YkMvVDWcopSDauCYWZc2hou_K6ZNKyNUcs9JCzkd4seeQLAPzWUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=DEQI8oxizBiZ3duC84d1hc21a6RjoyIibEWJbg8e4oqX9uTfxj1qtbr55Ww1IEYU05fMtNZoQxRGamVFYMZkr1Pgz2PsE92SJPpvh1mODYGwil6eDKN_NaHLbHX5KZBURcquj22bb5wdPWE_MQtUrfDYcdrf1GcAsil3moPktq7p45xjUJ2QtKJbemdREAiCdZRwAQeYXlxh2zTeNFP9myq0ApVs_5NgIYJcrQt-jCYLwahkthe9PmTBKR-gGWniGReKiWIb1yBtetTH2-R-irSnbKDSlPejm0YkMvVDWcopSDauCYWZc2hou_K6ZNKyNUcs9JCzkd4seeQLAPzWUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=VbiM4MIr0mx5CpEjdmVhyOLG3oIj6dHYTRJEErpduS4jncoWIo_Z1W5crAu93qT9t4Qpw6c0AG7ni9iBxAI3w3Itn1TmXIuutBIWT13eZW32poHvP0jClIk1k1Bg7wmaw9reEYXj3mA0iD7JC_1TiXRg1GkNjxonGUW-PdNvjiFZRGW67Rlf3XAKtSboYCeGG4mwk4Y7IfFh0e2d2PfOhNKvP02YqOM9Y5XgqQ-Hdi7rtWNCu4kSV1-jxVzNAbzUSxV8YqYQaepKgHnKnk1dLc3wTZK7PjUPPfuguCfavzNoDqYgpZMLmPgA67ONmnrzqwB0KByOL53QAcp3pAE83izNrNKzzSyo9L4qKVlDPyQwqFOnlO5uCd88dPQCJc2mTr_6fbcEv6fcpc0NV7vBUTh_lR4adQZhhCozsxi8S0eEMyUcT3levk1BIjI411W8-aKD3T2s4f2lKVU8Nn0XvVaI5Y4yQ1Itt7rGC5CnArMcRRgHK5WQYeDjmh-oxfWnXIO8WKTuOXvuRLlFInG9SIoRQzDUN7B60CvrZTjM2xbz7w9gF5a4xL1rLV8sm4lX19PLzffmEaAzN2jDe8lq_dHuXAtQSJXAb3lyJ3wQGOKirnJvjJFb_3mQaweLAADRkPfKOQ6unXuRIvTUbysDO_yi3Q20Cw3BsS3UKzSz6NY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=VbiM4MIr0mx5CpEjdmVhyOLG3oIj6dHYTRJEErpduS4jncoWIo_Z1W5crAu93qT9t4Qpw6c0AG7ni9iBxAI3w3Itn1TmXIuutBIWT13eZW32poHvP0jClIk1k1Bg7wmaw9reEYXj3mA0iD7JC_1TiXRg1GkNjxonGUW-PdNvjiFZRGW67Rlf3XAKtSboYCeGG4mwk4Y7IfFh0e2d2PfOhNKvP02YqOM9Y5XgqQ-Hdi7rtWNCu4kSV1-jxVzNAbzUSxV8YqYQaepKgHnKnk1dLc3wTZK7PjUPPfuguCfavzNoDqYgpZMLmPgA67ONmnrzqwB0KByOL53QAcp3pAE83izNrNKzzSyo9L4qKVlDPyQwqFOnlO5uCd88dPQCJc2mTr_6fbcEv6fcpc0NV7vBUTh_lR4adQZhhCozsxi8S0eEMyUcT3levk1BIjI411W8-aKD3T2s4f2lKVU8Nn0XvVaI5Y4yQ1Itt7rGC5CnArMcRRgHK5WQYeDjmh-oxfWnXIO8WKTuOXvuRLlFInG9SIoRQzDUN7B60CvrZTjM2xbz7w9gF5a4xL1rLV8sm4lX19PLzffmEaAzN2jDe8lq_dHuXAtQSJXAb3lyJ3wQGOKirnJvjJFb_3mQaweLAADRkPfKOQ6unXuRIvTUbysDO_yi3Q20Cw3BsS3UKzSz6NY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=GPWX1hpqyJETwkIrV2MJPjiDdlmCSeJIuqyvfIEdrmXVHVMLzAMaOf-ygKpy73XNe9GXN1CJ4lmdosxMJ1FKAwndZ6pd6BFFZMvbsRaLcBYgUsYZfyEmph3y-f_pDof5jUaz9XAA1XBN4w2EeBSGj5L-OZ4xv3Y-PVvmz6mCjF4yZRmkh7Pt2dOR41reFzli-0sMkLyCId4Ru2dKZ659pMfUa3xDV3hjCZXDzjWBYuGsnHu-elyJNeBi8HVtdaiYlRY81KKf_bIO7K_swb5djmlMtH23qNI5z2LqOWHJbSXB3N3Fw0KC7ECjEpkRql0UHr2-OYo2Q8ZhpFtE1Rn-fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=GPWX1hpqyJETwkIrV2MJPjiDdlmCSeJIuqyvfIEdrmXVHVMLzAMaOf-ygKpy73XNe9GXN1CJ4lmdosxMJ1FKAwndZ6pd6BFFZMvbsRaLcBYgUsYZfyEmph3y-f_pDof5jUaz9XAA1XBN4w2EeBSGj5L-OZ4xv3Y-PVvmz6mCjF4yZRmkh7Pt2dOR41reFzli-0sMkLyCId4Ru2dKZ659pMfUa3xDV3hjCZXDzjWBYuGsnHu-elyJNeBi8HVtdaiYlRY81KKf_bIO7K_swb5djmlMtH23qNI5z2LqOWHJbSXB3N3Fw0KC7ECjEpkRql0UHr2-OYo2Q8ZhpFtE1Rn-fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=n4oR8_7mFyzIpN4V9F9uSAHmATRf5aiYEu4ASjQ_Wy6c_Bi707k4YCjHg3yNCqLY1rkuLaSHWazlxssaPhlV-9CjgdIwfCCqcL15SJ8e8Tewedyhm5pk0XbuyLa27oOXkngUxcguynThRCf0DtMVNw2P2JMYJAfvlqSczEvno1w72DD5mR_Wrz7x_YIXZl5einbm8DH2yUOuAKwwbcf9rPA0JwIyxFk5vX-yEwl4HYSiZ8JLlLO9OupC9RHiXVqMd1__3ZKR7RNImIOwvNSADXemPq-hOrC6L2jzZ6SKXg3z_gksxscYbzKi4zrMG_jJPJtmjhJ0z8AxL8XthpmDOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=n4oR8_7mFyzIpN4V9F9uSAHmATRf5aiYEu4ASjQ_Wy6c_Bi707k4YCjHg3yNCqLY1rkuLaSHWazlxssaPhlV-9CjgdIwfCCqcL15SJ8e8Tewedyhm5pk0XbuyLa27oOXkngUxcguynThRCf0DtMVNw2P2JMYJAfvlqSczEvno1w72DD5mR_Wrz7x_YIXZl5einbm8DH2yUOuAKwwbcf9rPA0JwIyxFk5vX-yEwl4HYSiZ8JLlLO9OupC9RHiXVqMd1__3ZKR7RNImIOwvNSADXemPq-hOrC6L2jzZ6SKXg3z_gksxscYbzKi4zrMG_jJPJtmjhJ0z8AxL8XthpmDOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwoBAL-0_xkshYikzvLO_CQCx8DPZpew9BaxY_rCDI_yTApPRPrIF08PV4ycA0B5CaP3K2VJabY9JW-gp4RfsaDrpie4OIhQaAwDkj_hiaZppuwzYg9l2MGTyISmdkrZdFWiTofodT8iMZtj-jDGzSpd1tSzoSHuvOZRB6dMzqIfE2E_JHg5iD12l8lWONZSTVyAcBHtqruROXhe_nhi0NOYj8XuUIrFGQpddhwcvRFXcNok-pCfeJXGgyHjkx7oNG-hrxUd2T0Nj_cXOMB-tX9OU8gqxAVjDgti-CpRxc86VkmKBjRdzBzgFr6NVL6R5XrY_GxkjT_4bZLjhAWirg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=h_vTnMs5V6_-SGGnCMCABd-TW_HdpAvot6x4S8ZdnytZvH1uPznoBrCWFA4DrLYSaDRS-Abl-EoY698nlwOhtJtxNdriwLf58THJGuKM3BJs1OTJhsViIA-Rcp_F5RLVOTP33Px42LsEZqLXnAfR64LFre9e68DJRCI_Vs9wchd9gWgpmrQ_CD_eRmEtGEK4kYFkwXADq4DYyasao9NWrBZtmIw2g1j8p--8c40-NYyKStNolLWS0CEMsrjx6cYvr_cc2qYQe3NXxAmkN-dCRK85amP42hoIBYyMiQNAHWHnAs8qjZYRic53EurDQroWtXWS4F-f8Bytd_dOjkbr4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=h_vTnMs5V6_-SGGnCMCABd-TW_HdpAvot6x4S8ZdnytZvH1uPznoBrCWFA4DrLYSaDRS-Abl-EoY698nlwOhtJtxNdriwLf58THJGuKM3BJs1OTJhsViIA-Rcp_F5RLVOTP33Px42LsEZqLXnAfR64LFre9e68DJRCI_Vs9wchd9gWgpmrQ_CD_eRmEtGEK4kYFkwXADq4DYyasao9NWrBZtmIw2g1j8p--8c40-NYyKStNolLWS0CEMsrjx6cYvr_cc2qYQe3NXxAmkN-dCRK85amP42hoIBYyMiQNAHWHnAs8qjZYRic53EurDQroWtXWS4F-f8Bytd_dOjkbr4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiFymGQ_9CZHO3Bau6RQ2gN6oUZFq-fFT1VzZAL41UgDbR7dPn0Whidgmnk9u89S3ujMzKlhBLF4onspgYkNraik1A6V2LwXhnwknxpQNMs6ZWZsMzBx6aVs5nlfOVTJ0g-ClSHbf1a0GQqkjD881Oo76xzg5czFSIbHucnEK8PrZ11qq7sbixZgdv1pPC3IdKmkZBdNyKmIlUVDs2WS3Gnwlk9RBWfOLbhvlVWoAYksGk2ZP2AeYqKmXiYLTgdLGj5yflwT6ODc9i7e4bdkERLXd_8f0HoQ1X5Ttjum3dxL4EHssu8NSMyzim3uYC2y1NXeUes0GU56e5G0HKUdKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMKA3fAot4rsX3GE3uMq5mejlTei5uRXzgFVAPRdGmjFWdwuLs_GfwEp1mSlN34TBLqJFs8KSVbjH237BBEcwtlzydWnRiRZmsf_udqJOifyBshP6dSe7LIJZathuiG-xaEDR3cAUoeqf1FJYv-NcXzmHGvI3Sr6lXANzkRstAJSayoyFwj4Lefghv3MoImRHa1ajXuBd_4ZFAPwZcujb_DtiuSVmga0T3XiJ3wsMsoeaB0QLfcCb2EloOQWRHoAANusbgf1eeUWQ6Rxu51GbfjIcqSX1hJKp84O6jowZVejTAmkgKwI37zpocng5QbJrGuATaHKcj6hPQ2ZSqV8-g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=lyEptSA86S1QhjZ5LzQznKLJYzuBuwCZ-5bcwo9I0Rumvk6Obs7waUwVzdXYvIw8IM1nmAM9djs1gwm_407nmKxrKPhpORtEBCAaFkUPxbSTxeie_gKvUQyvmkdLtAmzNjYOzqNxUoCd8Zd9GmGYXi3wY1ly6Ejs20YzVSUcOHsXenvdVcnJs0wF8UrMriu8uE9nqghawBGnUe7CJA8r8JWaWcv-mgJP41NShNFgdiGGO8NRc5dHerrvhONz1S3llAy54_tj4gQUz8X0GhVHUJQ8DHKmt4pUxvQ3a1PJnKZBgiF7p2jyfAiSkY2eRInRRSXgONV3jy9NBmq4PrqyTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=lyEptSA86S1QhjZ5LzQznKLJYzuBuwCZ-5bcwo9I0Rumvk6Obs7waUwVzdXYvIw8IM1nmAM9djs1gwm_407nmKxrKPhpORtEBCAaFkUPxbSTxeie_gKvUQyvmkdLtAmzNjYOzqNxUoCd8Zd9GmGYXi3wY1ly6Ejs20YzVSUcOHsXenvdVcnJs0wF8UrMriu8uE9nqghawBGnUe7CJA8r8JWaWcv-mgJP41NShNFgdiGGO8NRc5dHerrvhONz1S3llAy54_tj4gQUz8X0GhVHUJQ8DHKmt4pUxvQ3a1PJnKZBgiF7p2jyfAiSkY2eRInRRSXgONV3jy9NBmq4PrqyTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=TvK8stDL_vTUCUt7wS-ZSL-5FP3r3VRQD4kDbgAjiYdErCQKxgArOUeoiPgj_HjYPlVfKNUk5vd9Yvb6iQx4QId-U01e_rlzZCFub3FQtVDubwu5Z5yNWVRUZOosLGbAnHRUusMAph_g2QEQPvpYwu8RbEf5hw6K6lR8TT0Ee1BrYVdG5T55CIEjn-xgQDCjQyPHjQ9YEWNS_xiFQkNp8HhLiK87wgrAfafZcJ_bz31cGBDMVlfukK3AO4UcPuMc_haXxjyqWv70hb_pN5FrXV5-_nrM4B2tyO4tnJDWuOcrjAp7_PGMOvm0CeIwUogsaDWuN1iEzbdX65sOwfKkNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=TvK8stDL_vTUCUt7wS-ZSL-5FP3r3VRQD4kDbgAjiYdErCQKxgArOUeoiPgj_HjYPlVfKNUk5vd9Yvb6iQx4QId-U01e_rlzZCFub3FQtVDubwu5Z5yNWVRUZOosLGbAnHRUusMAph_g2QEQPvpYwu8RbEf5hw6K6lR8TT0Ee1BrYVdG5T55CIEjn-xgQDCjQyPHjQ9YEWNS_xiFQkNp8HhLiK87wgrAfafZcJ_bz31cGBDMVlfukK3AO4UcPuMc_haXxjyqWv70hb_pN5FrXV5-_nrM4B2tyO4tnJDWuOcrjAp7_PGMOvm0CeIwUogsaDWuN1iEzbdX65sOwfKkNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=GBdG8S41-dcs9oZFafk0Dz1pQioL7OMGQ58mwH94e5oa_gmfAlzNd_xK61KnQPmYrMk3PTZcel6ZapU9vJl9UM_Cs23kDWj0e6sEUQOg3g1lab6NUN0a7vlDjVQvzHjvAZb-VX7Ji81lufQ7CHiwOpqcF9GuRypJMWyR1xo0gbQuO3Tlh_KGlhy7bgFZ6xl2_2Im_8xYVF7L0YihmmTssd-tODbotCs_6zLFUSJ3k0lesJxE-us_NYm0nsAJZaE5qIx5J26H4fm0ZlFq4vp5fQNQNYi9VCIC8gICKtH-HBku115TfLt1LWdo7-NDLQANNpuTqSrvdeO-2BtQSX_V1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=GBdG8S41-dcs9oZFafk0Dz1pQioL7OMGQ58mwH94e5oa_gmfAlzNd_xK61KnQPmYrMk3PTZcel6ZapU9vJl9UM_Cs23kDWj0e6sEUQOg3g1lab6NUN0a7vlDjVQvzHjvAZb-VX7Ji81lufQ7CHiwOpqcF9GuRypJMWyR1xo0gbQuO3Tlh_KGlhy7bgFZ6xl2_2Im_8xYVF7L0YihmmTssd-tODbotCs_6zLFUSJ3k0lesJxE-us_NYm0nsAJZaE5qIx5J26H4fm0ZlFq4vp5fQNQNYi9VCIC8gICKtH-HBku115TfLt1LWdo7-NDLQANNpuTqSrvdeO-2BtQSX_V1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxdLcrXUJa2Au03_UZ9j4RglEZeh1GPlLOmdklOsTxwApMF8I_Yb4ucthFIZrtaxeQ64TxmQAjG_TQP6p4GpXNWIHZt9DYLCmls2hgQJN7I6fsLY-2WcfUpe2unko0riS670w97bmueTWuY9PFrM4s7DGnidS7XW5ZcszN5utcuYWfzEdhSEITqqRYvNShZOhYRY1VUGXuNDK2vQZfEgPlFmIipJ4bcE3NVRS34hGErNAkZ4QmrIlBpslRzzqNPI0mTejUClUSISO9zYaXXnwXhZRnPDc5VpNE1v5UKsIoJe3uxp1nyqKDqLqn5Mg91dlrs2iCF7C4W_X4pVbXmtdQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=XUNOh8IW0aBeaNN-WBqAAzbq_Nh61eIabgMZpt1M7KLZVH-q4LpazHnVBsEamoO4B9bb8iOdWY0WUDWOMTrFniHFWnkEeF0841HElMZ0MT8G3tQCzz4fWB4mmWSBv6k1z9ACp4rUqkzDFIZM2q51-6BY5wSOPcNq_qQExOIPf6TGLkq51WLs_7WTO0ub73CF0mBXkFYoFrHWZo9q3s4Qv5YAk6f_dldE2RZWvbLUChaurFxTjuqpJVRZlsgt44ezibZeEJ__xQk9c-xQBbz04GvsHMj8DOKOsylQbZJIJOTnptkdkGDQ0fmxu-_iBi5gje7dF5qgO9oxLHCglHp6Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=XUNOh8IW0aBeaNN-WBqAAzbq_Nh61eIabgMZpt1M7KLZVH-q4LpazHnVBsEamoO4B9bb8iOdWY0WUDWOMTrFniHFWnkEeF0841HElMZ0MT8G3tQCzz4fWB4mmWSBv6k1z9ACp4rUqkzDFIZM2q51-6BY5wSOPcNq_qQExOIPf6TGLkq51WLs_7WTO0ub73CF0mBXkFYoFrHWZo9q3s4Qv5YAk6f_dldE2RZWvbLUChaurFxTjuqpJVRZlsgt44ezibZeEJ__xQk9c-xQBbz04GvsHMj8DOKOsylQbZJIJOTnptkdkGDQ0fmxu-_iBi5gje7dF5qgO9oxLHCglHp6Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=mFBZ0DMCvE3jITduFFNv4_yS46luBQYNctxPEFoiBYywhAYRjCsZVqnv2OiFH7YvHxwhhMNy9y0WaBtxZyekeePzhGXywaqB9LV_Not3V2_FloP3liJYkgwr2WGiN3KBhoAHVambbOnV7tYxMjCwvPtggvvSZXxtoCbaJcOUo0FZSESYPcTW4MYhzjaY16uHTlL6nbzb-E56IEfD88JpGVosWPLo9MsM4HfGy9BmUJQWYsoZuZHXYExw0DY5kpI8RZ4Wb-PyurLNWEsF422nJ2EiO_y_su-sDlpKmnmlIkDXsbMMtxKs7t9VOXRRQ-XWJNebMzE52YDYC5BwX3HtAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=mFBZ0DMCvE3jITduFFNv4_yS46luBQYNctxPEFoiBYywhAYRjCsZVqnv2OiFH7YvHxwhhMNy9y0WaBtxZyekeePzhGXywaqB9LV_Not3V2_FloP3liJYkgwr2WGiN3KBhoAHVambbOnV7tYxMjCwvPtggvvSZXxtoCbaJcOUo0FZSESYPcTW4MYhzjaY16uHTlL6nbzb-E56IEfD88JpGVosWPLo9MsM4HfGy9BmUJQWYsoZuZHXYExw0DY5kpI8RZ4Wb-PyurLNWEsF422nJ2EiO_y_su-sDlpKmnmlIkDXsbMMtxKs7t9VOXRRQ-XWJNebMzE52YDYC5BwX3HtAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=ZeD-UsQTfQ0dYeVbC9XH23lQ3VWOtCWX304ApVJdUb3uGpkNYnApvl5mZBcFNYrMnuus5O-48pRGU7ZPsB4VaTkuo8-eubWhEYXijrkFI8bHaXP-SrjJWT4vwyLOuuxMnTMPztaJ8Q9KRTwMmOrDp2QF5Y0oAqR9ibKlCaiPivLlQZwC_wWGlIYF475h7bgzLQqmWkeL6BznwTFpl4vVvzq-XjnbXpebltAQ6V5cRSq88wDNFxb3btLWIh2ZAZy9GEHOUtgUOyCiC5G_9FQBZTVdVxlX1ud8jNTBlbknRFEw-TXFcQ0eZEVe1huHtyJ0n_fVPMjVCBJfReDoQpZK1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=ZeD-UsQTfQ0dYeVbC9XH23lQ3VWOtCWX304ApVJdUb3uGpkNYnApvl5mZBcFNYrMnuus5O-48pRGU7ZPsB4VaTkuo8-eubWhEYXijrkFI8bHaXP-SrjJWT4vwyLOuuxMnTMPztaJ8Q9KRTwMmOrDp2QF5Y0oAqR9ibKlCaiPivLlQZwC_wWGlIYF475h7bgzLQqmWkeL6BznwTFpl4vVvzq-XjnbXpebltAQ6V5cRSq88wDNFxb3btLWIh2ZAZy9GEHOUtgUOyCiC5G_9FQBZTVdVxlX1ud8jNTBlbknRFEw-TXFcQ0eZEVe1huHtyJ0n_fVPMjVCBJfReDoQpZK1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7gGwoZyuCDkMzcSP4-1cacJ1m5FOJZcIEgPuEdWwVnACdaC_ou-fpj5kIQoMdw0hfiDzctTqIo_zgKZe18SMnCYldf41ejobEw4YHEoZGL6AjpuvtKKd822TmYgg9fc_4OSk08DT6vTy45PsP6keHRZ0GpRF2gq9R_U08Wj2IGi6HAiL0ZRZU41rMEv52to8y6S9DLEVIJ1xwBBU1BQUCUk5KCswmWoIndg3eouhngPi-8VrIhy5RTJ9XuXpNWFAe4VMsk7hQCPH_FrE4JNS2LXt5AliFsBDMXSdL7JJDfFDzjYMDAP11NhnC2eWN4HAecpeXFZeoc99FxqO8qGHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=FD1-MyHA4urA5shPqJncKa7INGTMKt2LFtUixaYW-uw45MtPkEUXmpR4EM3k5G4JZ3boGtYh-tDwvffLUykiCDVWDql8t3PoDACm1p6yF6yI9lFE5CTb9pyLWjANtA7782DevMSLxYaDHzz6WvMpGLYs78CHCFfxt_FVrp-EzDL6kJDgtASeJ3gp3IRRWTnwNaDprYoUZhFDbPgZwkQGSL_95l_25XdURtdKyDNTSxHFkIehXlj0Km1ZCMrvfXEkyAdeazL_1_khWdnTlxcmrM2MX_VtqcMJ1dIPo7oE1iLYDyeC3Gv-irR-sVJqEELo0JyhXD8gsT2x_f1r2xyETQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=FD1-MyHA4urA5shPqJncKa7INGTMKt2LFtUixaYW-uw45MtPkEUXmpR4EM3k5G4JZ3boGtYh-tDwvffLUykiCDVWDql8t3PoDACm1p6yF6yI9lFE5CTb9pyLWjANtA7782DevMSLxYaDHzz6WvMpGLYs78CHCFfxt_FVrp-EzDL6kJDgtASeJ3gp3IRRWTnwNaDprYoUZhFDbPgZwkQGSL_95l_25XdURtdKyDNTSxHFkIehXlj0Km1ZCMrvfXEkyAdeazL_1_khWdnTlxcmrM2MX_VtqcMJ1dIPo7oE1iLYDyeC3Gv-irR-sVJqEELo0JyhXD8gsT2x_f1r2xyETQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbOwT7tJlUzVIovj5_DdUcEY6niEXpDzfc4A9R05t9lVX8IB_Pg2se095xO-x7jOANP3T_OCeMl6NgW5LvIjmJv1yDu7Iou07noVq9ViqUroRervS-NFGnirdH3b9jHmFFhV_ZzzOJElvM74IahUC9BBW8BECduDR7DSH9o2P-mdXs-lM8tzNytNmj6mV07BWO9bu0C3KpXeirKEhufRjvieyS6nAisPHUQMbOPaTMs7HwvwRWpsW6cKc84Lek4ttvaBsBWbigCCzYLRHGSF1a09Z7_cP0cwtCstGGhzcYlhl_hKBEGwDz4bLV3UBVGgsk-inz1aqesWVhoaee37dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=esdgf10sW-KqWZ6s-NFLfJSYbCfOP67N368Y5lWE8PZNqCMAByRD9O4sak6AeaPFYx1UWwv6_za66MDwgIBUvmPQaJi-d2q2Az9YWTc4bj6D4xA9hi3_BFNxQxu_Rdx6Y5pFQPb7oifj0YZVuJNfyLQb_T7Le8eihu3j6IWfEt15A6yyN2beY1L5MmXrzOZQeRTzwi4JQkXPpbVgGtO4xRt-FlEQFjoexSkYkYZ5QMWlEo1gco8q2KbiOPR8UuoWHhEBWBvYerDktc80khzKHE2mGpBCpHSLrBRtTq7IQI8ItpwButhYIVU2H_Mbxm3--mtdH-rV0V7jeWCGETi7Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=esdgf10sW-KqWZ6s-NFLfJSYbCfOP67N368Y5lWE8PZNqCMAByRD9O4sak6AeaPFYx1UWwv6_za66MDwgIBUvmPQaJi-d2q2Az9YWTc4bj6D4xA9hi3_BFNxQxu_Rdx6Y5pFQPb7oifj0YZVuJNfyLQb_T7Le8eihu3j6IWfEt15A6yyN2beY1L5MmXrzOZQeRTzwi4JQkXPpbVgGtO4xRt-FlEQFjoexSkYkYZ5QMWlEo1gco8q2KbiOPR8UuoWHhEBWBvYerDktc80khzKHE2mGpBCpHSLrBRtTq7IQI8ItpwButhYIVU2H_Mbxm3--mtdH-rV0V7jeWCGETi7Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSb8Ij2znY-VOP8a2jNmRKS-to4fOwx18z3aluhHXX7Uq2kWdD82TZdelR37IdeBKtiDtj70yZfzjHhYDeMEtmffnVpxsUZrS--WknOnF40yfaxeSmkYqKinMKfXlYf4LkvobJTabVwMk6tpdUwHkI80UNOQoTXd3Pp1i8wubzz_hNajpSOMMCBLA6A2kFx3QWXfr3aQmkVrt3-B5KDu5rjtBArXFlxY0V55-j5cbJ20V1xBNZZpeQlhCANxIDjp6D1BSR2xnzvEGI8Cjr_qD8Wrbdk8Y6_qGbCj6YWtttoNYP2pjlQvrnz0_UsMb-x02ZIPCSx5OP9WnkC_oDImRg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=RvUkn7OKaKXeaBXEQ3RSygvhB_F-BtUTTEg7x4uOwR4RZRVWez4C5pmtTkT-45_snIhisCqCCR6BCTOo4dxtFOWYnto5BT7JL--FGY45Dt00D2olWl3gNdJyyRqURidLdoScQhuxNFLnGNbGje66cy7jHOWe-VymMuThmQKbOKRJy_B2ljAqCASFEPpQNy31I4USbADH-EfDlQCF5Fw5ZsBcnMV-3YUCSenNAZOpbFLqpQ8bszbGZITrrDgdtLXt16x6AceobPSscGW1UMg42FPE6qY8iZO7XZOqb2MdXyeYgYEzZRbp7RHJcrbAYENmF_tnRIhDRA-0Uf-7Kfr8tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=RvUkn7OKaKXeaBXEQ3RSygvhB_F-BtUTTEg7x4uOwR4RZRVWez4C5pmtTkT-45_snIhisCqCCR6BCTOo4dxtFOWYnto5BT7JL--FGY45Dt00D2olWl3gNdJyyRqURidLdoScQhuxNFLnGNbGje66cy7jHOWe-VymMuThmQKbOKRJy_B2ljAqCASFEPpQNy31I4USbADH-EfDlQCF5Fw5ZsBcnMV-3YUCSenNAZOpbFLqpQ8bszbGZITrrDgdtLXt16x6AceobPSscGW1UMg42FPE6qY8iZO7XZOqb2MdXyeYgYEzZRbp7RHJcrbAYENmF_tnRIhDRA-0Uf-7Kfr8tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uiGrsaxlgLXVmSHHUyWVXxBWlLV1x2Squ2JsJOC1FUIEXjo-dDW2vJLabZhej-RWcJCzmEaHERloZGIqNDkUJyV8qC4Xu8OQiU772nWFRgGWzy2aEWCP2hrqzVhwDyEYDgma3Wbg3nP8py9jUl4MeufwiSVpqWiqK3A8D8VqdrAFy0twP7pBzeSqwrRvXEhHFZ__2v-600pWr-KZUPfMIt3QVEMHb86jxYpUJQTbel9xcg9Qf6Kve3HGHT01MCBE5_lawPAjVu12tcE1Kw5yEVvHP2k7C6o7wf83ZJH_ZJRw0SBqmc80J54DXeXm6koJtgh2zY2HHxGYz1XAsxPPZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mbGlKyYTVO_PI6RnYMkyldpaHptL8hEYFdVQsxWWClnwiCbv9Ld65lw_gZ6idt54EZDqj_-_R7-Pn3zQ74198jyzD8CH3pUiBX8XWokh2NAYJggZhdHldHAxsJbsZxPpL4PSXug9c92HW0XuTcE4HS6dog8liNKZSF03IlumUF8Kppsc83i342CUjq7FLyYbkS54hU6ALzP3xJmP5R1HjRVcYFTd04TrqCrGD5sSdKP3DYdRRr9yTvyjfFGaNoefEqunWJZ5CtBAe2ErwG6Bml_hP5WU4dGpHv6e5xBy093xUPDpHSst8hTKJNgxMT4mno7k3jZQrl01wt80N9aBig.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=slVnOLoW9n01b3zFJ8vpnpYPcnJYgZWjbCCPBnLQpnPuINrVG4TKSLLIBvbPbzUuJPoxxVheVwl9HXkPTgCszYaetv-t1FkrVGMyFZKLiSvE1lxSrhZJo4t9Td3oJ_4FtspP78mZHS4HcDS1BKZY71nZpO-bVW6hQ8PHLVDlMTo5W6s6fH70KtLMTG11m7F5ewK7VeHeK3eLsNBbP9stR4NrGPFM_R4MmRrLKHgbmKthaptG1jU4K5zjf0KeYAvA2YZNVZAgK86SG967nz7H1PEOem1WVyRbOSoGbkBC564UmX7y8GcJ1I_Jq6qLj0GEdQV3aMnMLrniwzZ4wG0MrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=slVnOLoW9n01b3zFJ8vpnpYPcnJYgZWjbCCPBnLQpnPuINrVG4TKSLLIBvbPbzUuJPoxxVheVwl9HXkPTgCszYaetv-t1FkrVGMyFZKLiSvE1lxSrhZJo4t9Td3oJ_4FtspP78mZHS4HcDS1BKZY71nZpO-bVW6hQ8PHLVDlMTo5W6s6fH70KtLMTG11m7F5ewK7VeHeK3eLsNBbP9stR4NrGPFM_R4MmRrLKHgbmKthaptG1jU4K5zjf0KeYAvA2YZNVZAgK86SG967nz7H1PEOem1WVyRbOSoGbkBC564UmX7y8GcJ1I_Jq6qLj0GEdQV3aMnMLrniwzZ4wG0MrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-6ffa8UslYlVMe7sSyqRH7oc6xcEZTJykgoYGA37_WdCwlH_NNn3AvRHUdK36wGHplgf6W1Z-Z4ToM0MHzADTMMeeXFHVHAHQ-Hj5tlacQI3x3TY43pi5XldueshEYOKlqGKswEYVaLuRZnaZ48HbeIKN9Dx3HQ3pNdwVAA2M491TM-GehYu2xhHr0QMefyvIxV_ri88JLEw9KBylswBknA-6t5LOrI9Nlbz2CYOfMjT2doiIGSbb8r-swvg554IpEWD4C2iHlrM-COmvLPPumYeC1PWHDoQLr9x_KXnro8_BXloJHyyr8QS60SklTVEMmO_Fh7gbbAmzAqZtuEIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1KrrY1JUjcn83I_o_hP3XIUFUrIxFvQtl05KLmCe6Z_mMNP194I74WmpGI5eEDRJ-CBc7i3a5qgtea6yDfJc7nnPdVcVBbdT09bB6xmMaxkG_umyAoIy68WsENsZthbHUZyuq-Giv5Rl0nzzXiDpvvHA09lk2SkccgCNyG1Nz80XeoAi1fsdpDwr4Ro33ZtggPRzLDqEWCTpgA3g_wLQFp5K2dvskkGHx6N8EzOHIGer0fTJCmi1XBJPKS8m0ETDkFNlyC_wUYV1O32ex71y7XbclK39rCrqSj_h9zdHqZXLdx1HmhzELr9AXvkJ5Sgv5v-yRWWHlf8bCktV2nW3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_DyvQsErTba9E-cdaUYzIEHSPkuO-fzD5rT4pu3p-fuqgB2LW_iHDFvEjQr0A06iTK-obrX9nq57FIw0eurgFmzwgWU3VevhCfdD4xEnSe9eFITdlohqRDtbzIQZAGY_K8IcxEQHPeRu_miyCoXkKnL13ApBY2UR90jEtEEkA-7zS01uSH62etedDeyZwxfGomKNv5iD7mS1IpoeNeie0kHM267AgRJtjuKIy8SdA7amrYtXoFodN2jCdUI8zNtjIBliPsR0MnUcYypHR3G0pCOBQDYklbqBSABljMstQdRCuHkG6zcYVWfg1oxheZLiaaKIusaqaPWt7Q-j0M1lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKw8mKBZcsnI52UA5LmoR2klA_vMyXgtQZ7RnsszeIw1EVi5CY4M6GMzyNiAn1FXbmxfBV58Dbj4k4lzUbE54IbtHlZWcY71WHTP0LoVDOixRmsE0MrvOI8Omdnb4uxPl57lCkmU_zaIaq3M6NTgx9TNUWqRsurFUZWMZIp4YxqLrIdyjcGLTOwZ77M-oskvOMqPT62xuoIk6HGseOLh_0cglB98E8L3V9rPlLm8Hsnw_PSPjP1aDZMaoEm-ndHktF1pvMkJGQJhhZiZaSv1AzAXiCkcS1rjDNcaKy8r4kQRa5GSSClI33thKvz_PMn-ejydI28-1Y6fucPce70yJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TV6pzGQahh5cCNpwwGppRNDCCIVMFliRtB-dSrT5US8140qcpGxb3RQZmGaGn6hd880U_H98vpzxjl0VH77XCEgbaUU0p8sH0hjJCo2UDguoKZPVVIpco2C0rd3gRLalf-UoxVbl11b5SDTwtMO-uGM_dN0dv5LIKoviXkX_lSUOHorhu6rszCdEUXcmhVgYlhTYOKm4Oaz_UP2o6-f61BLyzUse25AWqVOBCP-i6dckcXG1umFRJz71KaxA_tp-ppyHwOF1ztKJ1XJusIPWni4OL1awROfUWLrr3yOG6aWrEervLieEVeUP4ZsxY3QF3p8MVn4iGuPVRf5oRKW9og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=DADRXQBLHvM328ZS5BjcFJPhZ-sdt2Ah9b3Gg90HcZsh79XYjxHCLyFYFKhfl2aivB_Pyuv-SpQaO3kiDeLQRuFphJBLn-4XybDLxd_NOEyP4Z7GJ6sW30a5hGnSBUGuSPAfHiOQIN1xU7wDwZMOTYeU5RlYx0Z9Egm13_PKaulYHNGrm3VehzllNRY_dJdqhW9i47zNiXNjNL6DtPEbV7amuXPG0q772o3r9jZsYndXPqV4OhXd9B-k4s5QDNGcba1H8Bx7ZvZ9M0HUO1ilbg0j6hWmkDpDQit8y93aIMutcPEg4f239JiWmXVPNTCqx1TSyabf42hvrfelWjY12g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=DADRXQBLHvM328ZS5BjcFJPhZ-sdt2Ah9b3Gg90HcZsh79XYjxHCLyFYFKhfl2aivB_Pyuv-SpQaO3kiDeLQRuFphJBLn-4XybDLxd_NOEyP4Z7GJ6sW30a5hGnSBUGuSPAfHiOQIN1xU7wDwZMOTYeU5RlYx0Z9Egm13_PKaulYHNGrm3VehzllNRY_dJdqhW9i47zNiXNjNL6DtPEbV7amuXPG0q772o3r9jZsYndXPqV4OhXd9B-k4s5QDNGcba1H8Bx7ZvZ9M0HUO1ilbg0j6hWmkDpDQit8y93aIMutcPEg4f239JiWmXVPNTCqx1TSyabf42hvrfelWjY12g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=IjYtpirELKERRN3qOPhCaon7zXhcG-z4l_BN-FVj8EfyoAOspLKExWvacf5ywwb5vUJh0n-a-pRFpLGjG5rpBU716r_h2wWT1M8lS4rZp5HEGyf2AaHuuh8ll63XdTcQENMwbo-u6eNQ09ohrDYPbn1qXjrWT4dExpE4gts6osLo3XL9XUfzwGYWBr0K9Gjn2yZp4ZmH5uCx-t2fnlh1nnV_2kZQBbLEWFoaesfKm3Tf1zeqySn1e3PgHAf8QzvdqAaAzDaL7ltgtJVVduGl6MK6Za2kphdHTfg6L74rfpKa44B03hdHsoyYbw6f4LLDBNCkrXlj-HOs_nqkZ6_fCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=IjYtpirELKERRN3qOPhCaon7zXhcG-z4l_BN-FVj8EfyoAOspLKExWvacf5ywwb5vUJh0n-a-pRFpLGjG5rpBU716r_h2wWT1M8lS4rZp5HEGyf2AaHuuh8ll63XdTcQENMwbo-u6eNQ09ohrDYPbn1qXjrWT4dExpE4gts6osLo3XL9XUfzwGYWBr0K9Gjn2yZp4ZmH5uCx-t2fnlh1nnV_2kZQBbLEWFoaesfKm3Tf1zeqySn1e3PgHAf8QzvdqAaAzDaL7ltgtJVVduGl6MK6Za2kphdHTfg6L74rfpKa44B03hdHsoyYbw6f4LLDBNCkrXlj-HOs_nqkZ6_fCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=OodnB8GPcYFfSyARfog00uudpo7jftrAcFOT9_FvdVKXzSLkwy9YIKZ7XFB69Yot6quqRcgoSbQnwrle1wBkoYcuNM-jSWNYaaEMeV1MnYbnIfJGwUuhC3TdP7hpI5Bf6jS5_XF8D3ln8Ff607Dhhb4LOupeSDAF3nUQ6ttqFSYFyBkhLX_khAKrGEzgP_Qd3bm10ht_YFFBidww-efCrA4CSqx9XyYhgBa8Es8l34hfYOla-Bai2UMnlB_N6O2WeyRcScxplZGkc-ePBJJKT8_LuBPK-aXfGQ_WqOW-7bOYBfKGjjw72DDI3xUh_5tCzVH381HbnWjN7eOHI9BGCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=OodnB8GPcYFfSyARfog00uudpo7jftrAcFOT9_FvdVKXzSLkwy9YIKZ7XFB69Yot6quqRcgoSbQnwrle1wBkoYcuNM-jSWNYaaEMeV1MnYbnIfJGwUuhC3TdP7hpI5Bf6jS5_XF8D3ln8Ff607Dhhb4LOupeSDAF3nUQ6ttqFSYFyBkhLX_khAKrGEzgP_Qd3bm10ht_YFFBidww-efCrA4CSqx9XyYhgBa8Es8l34hfYOla-Bai2UMnlB_N6O2WeyRcScxplZGkc-ePBJJKT8_LuBPK-aXfGQ_WqOW-7bOYBfKGjjw72DDI3xUh_5tCzVH381HbnWjN7eOHI9BGCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=hbX7wTZfSEEgtz0Dni2fle_0P1BidJolpKQU5OgH2-Cs8YMQI_oLVCsFOqAKVx19w0LWQ40Oqa7vm-85qUrOKEE54pMNT3QPXjPTSTnYWJZE6fASQfNpX5Hg4s7SQAm5ve9tTravohok-nRga5u43Hg-xpbaAnXzNtRJ8jWEKXB5WMLG_R17kqytYdfph-PxiYBFh8SJ39l-Kj2j_6T-eDmj44rAKWR5dvZYhUS_YYs46vB7aS40xgo_E9qSRbVlZKDDxw_cJ2nIZiusiS8Q3PpU9dA9866Vz0d4w_6mWROPNljb5IS4fc9LevEst47BNSddTLsw77dUZkKMuRvT7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=hbX7wTZfSEEgtz0Dni2fle_0P1BidJolpKQU5OgH2-Cs8YMQI_oLVCsFOqAKVx19w0LWQ40Oqa7vm-85qUrOKEE54pMNT3QPXjPTSTnYWJZE6fASQfNpX5Hg4s7SQAm5ve9tTravohok-nRga5u43Hg-xpbaAnXzNtRJ8jWEKXB5WMLG_R17kqytYdfph-PxiYBFh8SJ39l-Kj2j_6T-eDmj44rAKWR5dvZYhUS_YYs46vB7aS40xgo_E9qSRbVlZKDDxw_cJ2nIZiusiS8Q3PpU9dA9866Vz0d4w_6mWROPNljb5IS4fc9LevEst47BNSddTLsw77dUZkKMuRvT7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8TPEc8TFhPg04JplIUcp8MYKqmMp99hh10DUWo2NWDUoi3xd90XkvypGSrC_lo-H9FghJOymf_FI-KIjvDm1qlI2s4V55xRte54STQ66EJ6rqCe--2Vcl91gvR_wE8KvaYqsRJa1FlHeS0AK-rLIUJasb18P6usOfPMYtBj5WpiUiQrJcDsh6qIkuLc8s00k6P3PKeOQbQwAY-F3RRHc-Bw6ikz422cl1qSPqdLQgG2yCoy0n6PtKk1YAnVs56V9B8rN3awoVgT9fv_d-18x8FHZDY-kDG0gUPtGYh8oLQ038JaxjGEtrK7piJA2-jr9AnR886RXZYfiAAgr_YJ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxxpRpZzgWlrMgPLEbvVzcZ83dlIBseWNcAaWl_661qk721F8lUYRvrWWBTz-kkz_DiM0UmhRfZkmnX2pJaW6ZhlXV_EaTk6rTDAlqZvRJLcqLKsrvMLGc7neMu9OlORiyzNdhEZAdSBj9mxvJa-GElwGQpTsBjzEjlw1dj3EpmHM17JUDKQQFuBt_YqY2G0J6-Brm2IL4Jz43xBfCv8S0meSj9ByMQnnzPf71Ci2ktV1FI83InaYIZPZP5Jo5RdZWaBl4fYGjOhm-ZHIejnqEfCuFVL2WQcCFv7mvZLY2v7tCUtADkw7vuWYXTtlUTWukWveGoUh5FXZF4iKfRWZw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=uM69mrXaG2e1FX-5yu8bPl4oJ2dq1aQOvM62mO6o4YyQh8StwMaGlRlru72u43AYoZV9BJu4rO-WF5WLZPyvEkiGeRPp-pkEWo015br25z0Phs4pFonLm1js4S-LArRA29VMcC06gaSveRB_cxh726MoH-f-4Gh60rVdA0FhenK69J2ebgn4lbdVvaMdGzXaXBEBYS9qQWh428bxmjTJwihTl4U29z_n3mtBBjzKUFtz1Nl-kEsopY9GGgCMYCUEcarwmG7-SLoXm7ADeZNvKb6fMHgwALtvcx9l0OxuxonkqxWGPLTh9FcQFj-FMqMWSRSWqPsD5Bxtlcjq1ioHDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=uM69mrXaG2e1FX-5yu8bPl4oJ2dq1aQOvM62mO6o4YyQh8StwMaGlRlru72u43AYoZV9BJu4rO-WF5WLZPyvEkiGeRPp-pkEWo015br25z0Phs4pFonLm1js4S-LArRA29VMcC06gaSveRB_cxh726MoH-f-4Gh60rVdA0FhenK69J2ebgn4lbdVvaMdGzXaXBEBYS9qQWh428bxmjTJwihTl4U29z_n3mtBBjzKUFtz1Nl-kEsopY9GGgCMYCUEcarwmG7-SLoXm7ADeZNvKb6fMHgwALtvcx9l0OxuxonkqxWGPLTh9FcQFj-FMqMWSRSWqPsD5Bxtlcjq1ioHDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYqXLKSwrQPmsh-oCv-at-5-hzKVCaYgomkPLWkwhOZ0iw6iUZXG_mAmXNlEkWuoemV_v0yvuxY_H9tpYbRoKANhjVP44EQkqAkT6ZzQv4I5qAOnuh1vrCi9x1HJ1XZBhYtEYiQxtCFZxNqvifHbwfJLdgZf1Wtuz9IsztQwJe4QKnjJBKJty365HlsRGd2rsb6RYG_ZzQhEbRKtQcVWDlMKukAGlqLi4Xbw_GuVmPWjOHzKbwDJjZGmpfcKj_B5d9VPYiWXuNEJc0h0hi8OEd7q-H5ZgN_lhDAsHxU5Pp53y_lufg6fae6Y7C8Urp_OMBbxPNxUOz9qyck3sYj-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=TbnjW1laWkKwuN7kG0dnIpWhkBoO0G2BfsBBQ6NjYtTfsNz0p8dVL5WAKkn6PcfwfCFI7pTzAfEzayeEULtUAiW0EJxhKbJBxPa8tZMUWpiNVe25TV1FB3qqT2u5TQYYLJ_otLaD4i0Rx31n01DBFuLp9fN4VjcRQx8RHUFJj0hbj6mcpvZCdCFb81Q25qHAWYM_ZxjN5XIjLUqSdrco3XVzMy1TJ0W7PwBGV5aAupKvbTtO4rhIX06MUobFfThdkawd1uaCS1l6cYUxddPAj48B6d09brhEIpjA6D2BhneGqZolppGoocUVKB5nPjR0gTKGkCEUxVFYWw4JP68oeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=TbnjW1laWkKwuN7kG0dnIpWhkBoO0G2BfsBBQ6NjYtTfsNz0p8dVL5WAKkn6PcfwfCFI7pTzAfEzayeEULtUAiW0EJxhKbJBxPa8tZMUWpiNVe25TV1FB3qqT2u5TQYYLJ_otLaD4i0Rx31n01DBFuLp9fN4VjcRQx8RHUFJj0hbj6mcpvZCdCFb81Q25qHAWYM_ZxjN5XIjLUqSdrco3XVzMy1TJ0W7PwBGV5aAupKvbTtO4rhIX06MUobFfThdkawd1uaCS1l6cYUxddPAj48B6d09brhEIpjA6D2BhneGqZolppGoocUVKB5nPjR0gTKGkCEUxVFYWw4JP68oeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rASHPoWo2iXC7qVdWr9YN308sFBg4aflY8ovHBo5gnkdz4fmqvWqwrMR3Y-zMbHxPjubNdv8LeqROzSh_LIbNI8XtXZ1jDc7L1Xwj43e1diER8ahwxIdSU-bLEWHNRMkgUqoc1O5tVMl-oseH0UIN9QGep80Ul3cs04U4ijwqODCzpa7RpxX0q0n7ZgqPZiuztrQlv9BzwkoIb9PlfR6IUmBeWXU9tvHKKXKACCPaGtc4kHCo9WqgcClIVjTEbYdm-Sa62gnNTRu1Xn8H3IQA-XuGlAVk8AKtdXr8eT3VZL0vlyYPw1dyBS5THAQVOTSsyY20PNeWrZi_xRrevJQxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-_N647_MmhZhRT7PHk-7M4UBiqht1ZJJvI5YsypbZsfz89FGD4lyhWUy2gkVyd30G_URSMKctV-JSYn53SyMZX_9v7XIbEFmI0ku7syjDR-LgdLYJCE2l3oYVWaW7ncN0d-5qj2J0qRE0-Y-DO6WaHwVNtOFWZFgY1CG3vFLFmvd07JND6HbgKUqVWrbsyG1BVsJsjB4ySs1xs8YOvUWwa2W1MTPbmOQ-Ax3Do4lvJ92HVzko7BB12wA1dxh566IMvOjJbQSsWqKAk4YhRHTRUY8qAFcwaodaE3SVw-pkYXYyiCLtiLCq3JvOGesXUGk2UV8_3G6vDb4tthLC1sAg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=dHUbkC3bjAWjEXpy7D_ktxOFM70jgP7H8IeXEfoSXAFiTSeDMiid90I6NxNlRdM3PCbaUwDc26vuj_tx3QQAuGRxATMvkZpGjmy4oXN6fnoR2RmlEhAC6iy_G2guVpRaQ9zBfL32PRli9wpmvgmiKrVyz0onounk0S2G7WTfcMIFuLMF3z6W9tNC1X9tV6LQRWuzr5cwk7-2DG1rnPLfVPEPkwz0AHjJpR0re7QvPw3SA4cBLbiVK1OG_1yYW1LmSKktyOpBpXQAIPyvmPmhE75tE4FFY2IL3eXGO4VojFlpRiczV4-PKAirV-jNWZKB3iVATLG6gOUpAb5gFrHmaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=dHUbkC3bjAWjEXpy7D_ktxOFM70jgP7H8IeXEfoSXAFiTSeDMiid90I6NxNlRdM3PCbaUwDc26vuj_tx3QQAuGRxATMvkZpGjmy4oXN6fnoR2RmlEhAC6iy_G2guVpRaQ9zBfL32PRli9wpmvgmiKrVyz0onounk0S2G7WTfcMIFuLMF3z6W9tNC1X9tV6LQRWuzr5cwk7-2DG1rnPLfVPEPkwz0AHjJpR0re7QvPw3SA4cBLbiVK1OG_1yYW1LmSKktyOpBpXQAIPyvmPmhE75tE4FFY2IL3eXGO4VojFlpRiczV4-PKAirV-jNWZKB3iVATLG6gOUpAb5gFrHmaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=t7Jj-V6AQ2VTyb_cBQ5s3GiLb0EDsyVGfWNNQlD3AM6YAccVjtcvUI9wdSaxdd_yJ-8StD5qhHXVbrQgIZazs7qLy32FiwmNa15QzY1hU8V4i-7hdo-hFXcHA83J5yNSp4m3sv4PH2pHvBSXF4RHZA0d43jC4-g6eKJbL9lpQMtmcssNm6cO6f0GrTq9gx8x9jlvpCLcPLK7XIkiy6PqZ8YCVJzcQgk8L_FzBJae4UBX7OuIvTCOyMl3gLqPENqJK9Ohr48fB5FRMisbBNtmiLt_fEFgmDkuud_R-fW3Oz3OzEwYzVNmNG30Fzh9qgrD6ok9zcCguMaMeg-LWWPYMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=t7Jj-V6AQ2VTyb_cBQ5s3GiLb0EDsyVGfWNNQlD3AM6YAccVjtcvUI9wdSaxdd_yJ-8StD5qhHXVbrQgIZazs7qLy32FiwmNa15QzY1hU8V4i-7hdo-hFXcHA83J5yNSp4m3sv4PH2pHvBSXF4RHZA0d43jC4-g6eKJbL9lpQMtmcssNm6cO6f0GrTq9gx8x9jlvpCLcPLK7XIkiy6PqZ8YCVJzcQgk8L_FzBJae4UBX7OuIvTCOyMl3gLqPENqJK9Ohr48fB5FRMisbBNtmiLt_fEFgmDkuud_R-fW3Oz3OzEwYzVNmNG30Fzh9qgrD6ok9zcCguMaMeg-LWWPYMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ds0-c57RyB6w88Mi-suAFnHz4kO_7Ad4fhN0En0GJh9m2Z7GNQJhVr_t4r9-sOdIla9UFfH-FIpeej8xthQegFU2I1ohmAn1j8IMzwb8MWuZnrZV44wcBxhAqT5OIaDB0a7IHOl1fg_OoCEQDGHo4T4oedelmKsTUyH60sYo_w3DQYMUyjMkFOi5mWP6HjXMFlTJe8WkzlhXtsLal2WV4dNgdJWeQ1J6o4dQnSBHhopouCJfCjQ4XjKWbsbaVygnK1IjSoc2YWbhhih4F_BpBQ6PU5stGNHVAQjAI35XCjKZkDje19okjNeImCY1Xvp987Wh9yV3cKtiIa87dwIDeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAgutjZqAptw7FElyBOU9YAwcAmXiOoqE38DGb6EZhbHhyQCypF8r-_4LzguepsmGVrSVDx5_Uk6K-Kbb5h0hmhd-im9eOYchHyQEtU1a1tbXoWC-_V0tbU6eDrnvrzjUMWKYv-S2nRBfOjgv_mEMT4pTmFl7wbA0JJJ9FVWNozBWBYBVnQ366tZ0xORZVBmcgU-5IN2h7wsGKeOVrGlTs1EspcI8pHn9C4QRDbHxHcDr5rOzdaWqpvj6xYiwLybWk1qKE2FhfaH9wsrtlYYb1fC_Jp7BHPHKJJEmMO-5t-cz-QjULQ2T-1bf9tMRSynQlw-MY69m5-i3ZiHFqxoUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdXhoypnLadK7D_hkyNiGCF5P7uEnVkdufH_x8vDSUlEtKs3GSAuY8MUzK3lgxJe5t5eE_Lz-DNuVabC4e7uxVPrq-71-POkqFzeXRPMq4LPgYNYdtuy7O21uLRlQxBXwntZyp8otJYRUIWoXdFQkEt2Bks2gzos27pmdKhfjADhYshGMAzd0RgxVgQVhWNC-Mp1kObqV6GoaiWqM_xvge0NxvDPdDP-5h9ntqZzmfB1fYIoLPnXlb4RzwIqccYepcFHR6k4fPdtcr4EClrt8B59w7aPAFHVbsX_dGAMFb0qne0mKbawqxhI3IQLNVqhlf0O1xSFSaxQnib4u_Ss5g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=CsvZ43Fs8t82wrVy4XNoc2J3PlIXNvdqt0wCFBQ2OYFfd_Wwpf3pwX380R2MWIjfe-1ImJHXB7lglTMqi8ISazFp3vftHJ8uXj_2nMfZFooFD9zp7rzI9NdrLkmiu7CgaPi6Kf5eBU_6kOUs9T9rvyL38F6AK9hsjjgsF4RUIHpt6IXwpB2eB6QEscCwTcZNDbJ9pEL5UU0zoESkWsCyr4AN94JDJ8h19K17JTHiZ0vA1A90CKRKnKQSEGJwplRl5zpVDYSIVXtFI5kzYwmG8vWa9EBxz8-KZZp6cZw1w5Onxip63uWSNE-AdfDyeGIbtadn_jZQUTb5AIS5F6tXLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=CsvZ43Fs8t82wrVy4XNoc2J3PlIXNvdqt0wCFBQ2OYFfd_Wwpf3pwX380R2MWIjfe-1ImJHXB7lglTMqi8ISazFp3vftHJ8uXj_2nMfZFooFD9zp7rzI9NdrLkmiu7CgaPi6Kf5eBU_6kOUs9T9rvyL38F6AK9hsjjgsF4RUIHpt6IXwpB2eB6QEscCwTcZNDbJ9pEL5UU0zoESkWsCyr4AN94JDJ8h19K17JTHiZ0vA1A90CKRKnKQSEGJwplRl5zpVDYSIVXtFI5kzYwmG8vWa9EBxz8-KZZp6cZw1w5Onxip63uWSNE-AdfDyeGIbtadn_jZQUTb5AIS5F6tXLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Llr2BMTXhfqUCu6x-cT3lIb2Theq52HPVyJBKz6YfhKIzSCBX-M2aOI_QGPnsaQiOMpnJB2JKw6QLWJgzyFlOKRaOIJLtE70IMl5_mLGhdqcXby7NY8DcGauCZhcpbSSG9MR0kqX8961L4KRCenak9tASWazZChIm6V55wpeF-9ROR1ABLBTV9TPjYATuksX48nYowzmjlez7aMY9H7ZiMATChk0Tsqddw7MRjtrIcYrU7DeQwo2yisbuH2ltUvbeke7Fktx7ABLt7kRETQxsDnlt11ESDyZtvmLSdLbPraG-yaR6c-hMFoPqZfiZtol6nfELGR6-zk8oZShnX3r8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_YWqc0QhEELohyKWOEX-YUyfivRTk6RGixfYvt55ZOmSnnhYk8AdraEc3LdMt_XwFUpt1PlFINYvyAEz33hiClg_ksLlp67yjHXxI3CQkffLGxER6R67JhJhXlZgHisVdNnYyqwtEIosXVlyMUWzc6Z0-KeNa75AK-kr2rT2xSywt1hw-VmgJ71NBkueJ-JwdKbQCSYOktYvSjzEDJ6QmI9oVZX9lOQFjabnBEqKwo9v1K_iEMATfkSHiq1vgEQzFVte5HEUAfq_i-72PcBJclcGWk2Qvix9tK2S0qwZVPOGAyafzCfonkLIxfOPTT_x3tAQVQ0tkPDzUGu2yQR3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
