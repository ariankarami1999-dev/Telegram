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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 09:59:19</div>
<hr>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBLBI_814qgol_DQ-CIl1yYSfSaQxp2B1Wh4_IPFEmFgWj5VT2ZvlYgB9pb-ulo1GouS5z2tOfgb9OfNsrEo72Uz-5QdMHBy24nQbSTQMWih68uQAlNetn9-OoPgStEbfTHFcNbAxwHyQjDhm_c7q00qEh2N23igLiJzk6T1eJ8ppq2b6sqSJyXgaMIG4_CQWnN_Up9o5Or7YKfnf0QzqRt-lTdMKVWG162UQws8oCy_JDAK6ndbTkLL6z_PnTkX45uNns93HqbTJtqcf1XxoQj5cfl5zLfRBkViNdqFWpaxr4lMiagnhqhX5G0GklWkwuhTKnUbRg0f396JybuvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_V24fwnlSEn8pBtox3mpxpxImaYlFd8e44Kta2sIesLQWwRF7pDZ-lW_UHBH-F9OuUJXOBB1FfbiCJ1RibqaJ-snqF452VaujAF8rVwShBgO3Pk6yq55d_s2H5xZqJ1BmADKlUdgg7wCMYaL8kKomfWkB4F4aY63FA4JZmD_ZrXB_3XfVCVWmlGHdiiwsZmmIxrZdOLcLTU6DWWVfKm6fl0IAFlw74qL4ai0_-dPjszTWYa0THkpBJL_fHzGRBcshnkDDHwcT6yhQb-_h4SsAVMeeYzTPhMhtUFGHL-48vTp_vJzh-paPiVuic2vTSu7ImpBdUH03OUVD0BtmS7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmdjgjWxEQuckLdTv8N3YkIHT3mZ55uTCEXVEUmtjcfR3S65A0FeSghZc-Ylw45bbMoUqmy-q9SR91SOM5Ov5-vW049M9Lj7UBlVvKcH0KXXOZ3DraVoVEjjyCvNdx9F_UCmfjVONHnp1xhDmMBEyQvqL1y4VOCgA8zJyqel-NHIzFL2J2AAHcp57cvhoh6JOWAuIytaYpljmJUqWRJaDdPo0GfC3_JrIfeASDwpXycpqetSMCnQzC5f32nsLm0PZgj0YuIRJUEKMTn2pcinS_jnXxJxPBFJBs0hLFapJvQqs4iKiKJarxVXzDTCU3nV_LkymwNc6qxHFz3hrnn2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxFz44CZ3kCcIgGOUlCTGUOCPURyLb_cAeSaLvPM2ekdL4k2M37l5i5nh841-GHVldDo1VaB0hj9oNWOCYQ9-jJ1TgUjp9BYC-lLGlLhO2cyx2KBHh8guuCpZ5XuVljXTHBGW5gnbntOK6JHOr71R3wTYvKAufMCk4-8McBJ8VWQkEJZ4eItyPPiOkq7ixntWJl33r84zbsKvPaP0-10gZSbC9JRfjJc4AKIgTJhEAv4gmWuwxchKotejflOBmjiZbL4DkcnRrsYtoqqZjnpsxNPAk-wCdhIa1bYa4FSvo1SkBSdvmT8qvEJvlRJCU6hfh7FsMh5x3ichxPd0G-p4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JX2Em57BlV8AHrCHXvQjzSsDaWeE202zmSRAsTfJuGGzQsv-Jh8ge2zHT2DcmIyIgNLjtjcYMybGx2PhoCZpj3sozzZm_mgvUjOxPzGgihLVSe75kGM6KWfLDcqYDK_BsrdkhA5tJtnBE2xykOk0Rp_drzY3sOFcgnoAiWQsNXRD_DbrNC4y1rOgPYrMakY8FlT2ApJlTfrV7P3sqomo1OLUyErcB6gxvreLz5gedLYyhSzszeXYbKAukjh8Aytr0LRJTUgqev5ZiX8AB3rSUdDo5Jfh98HVtj2ccTs-LOj7G-2_DR1jgqjPwmhI_NFCkeISF_fstFLoSOXSasXSlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwwhQ_ldICT3cRxJOC9cnEmlZb48JEnIKoph0JojT3KgH-O8p28FTG36Cvr07UgOAhgc9_mFZHzr4ei0ZyZGrhY9cQHi_7RMxCp5g3omnn5u4oFU3FLJCe7vYMtNB73PS3tcuT8RIk772Ow3mPhqKPnNnFifO3HiTw7uauOX_XKGFuI1IG7InrMtof-xF2z_cdpoFbvRKxx16w4nNVLU1B7Vh2kmaJTbqs7p1PFrDC6yxyeYt0kZZFevLf-eokatdnmAE-4qY-IH68ha26oHawX3LVsRHeXX8UlrWFeNnqoExJaiy2C5AWA4OsXMQfpniReeBSU_PDFLKZFT4L-lLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dl5_706qAeyEVQZOZwb8026rWeGnLRdv1eBYl1YQw_IywGq8wn4aBsbMHiTg4rw-oi5pohrqpEfayuTfW27dIADP1UofdqhJCAViC4tutaSUdh-gDhBQ5kXM2EqFbwV0h06W27p2jl-YH-BU1_9Os68HaJAuRjCeeQj0XHPtYqFGxoOECXFHjlD-68LIZpizX6TPRNKdLWSQhssHgD-pZRmRY2iEZ8awQA1oK0fvDjBzeqoS3ms3n3AAOVLrtOvKzeKZNmYZEanYLdWrYhZ7Bfe1L8V8GaDs15DZFtS5EAUI9LsGD_pVBmDtm01rydJ7pvSS-z_KgMXJ5LpumLFOOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caIPrYhuQcgMo35MoxTHT6AAN6m5S_7e_yfcCiCKwHYDRFEscewt4zJIeMXzWr5c2YMS8Ro2O7BXv0c5sAtHvRsbskOJiXSzfA7zu9H4BN0QXBG0vjNqMXwGzmuNSN9M7O8e8wq_n2q2vCmL9xcXM9N0h5vSWxT8-q5xhng2R6H7Fd1goYHNJC-wAB5ISPZouD5Wo9EH4D_zAjbdaXZgRrC8YULWW9QFsDjL8SQcV0TEhwyJ1HORqjGJ3GL1wcMKie5GnKbDcQuHXFGe6k3YzYAQLHSWzU704fLv39INdxMR5pN24kx-eOZo6q2HFbncfYJgr2sHY3tNt4SeqkeGrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBryuNEQuBDySzreCzly09fCOnemLNTA8P4HK03ColOTnR09Y3FNzw6KprhHPquMBsQmhRu_ECzJGPFCQONPFzQCfvHnKJa7GS3sbxfJNrnOl9v9K6tsKCRzWXaonWjbEdn5On3xCF9uVjre1SRRgyOsv972OsS3JyLAFl3T3VjfOOGoZSd8WsAMOVebNBAN5poTjD3NFKjVqfr2ic0xcFSblO3juMUksujNDLsDjQDMbYX0OKibzfg9cd_rPeKYvfgQQFMtjQyVC5uxbSKFpRBFPF1CfzLQh6lfeQPsBmZzdiPS_NzxAai1BrMaT2QkYEBtLNoEtv8YeIdDbzYW6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtxVEOqwkMg1Y-taiD-wDFLIZ6Qc704omIfrOZfOkvdkFJDqjLp8k4BJsfZbgaHxu476acRJQnbwA0--uOs4dbBOdOikAkMrZJwFiGunn5mh4qpC4l80O655TtVH6d8ocsf3qjJu61GEmrgr0x4v8yj8mqbuyN1u_WCY11Nw-mRHhElZTSIlUdMX8rnD8JL1XM2lclRPrfdVO_P2uLh6IAt8w0la1_PuUHSUVS0WKMPVKr2lbUPp3JNu9YK2j2y-YxJCp-sncJ8NwibGKgyGTu3xOqHEaGuwX2m0xGzahj5nYXc6ZXBVIGVhjPqJ3-vtGQgUheyzTWNhaayoE8SGyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuQ_vei5UgXNcWziIZ7FYWH_Y3oBdDisSkrFgoLM01cxj-WrERddSCb8oW-bThZa087yPeep0FFIyiC-VmDPLd3qwMAFYQ3EeMwRmE5WRBHLeDVq2HDx4a8euujhluPPhqwSq8ngDa8n9Too6YGz5j_iCUy-mSp8YhUR6A1vNByD93SAOyp444zn1Wz2UGwab_fuDgsjPp1M3GnC7B12vd3JMSX_k5uYiwG036dNiYxZfjOSgsQDfx1zZJgBaq3DbdDk-7Z-JVxS0ZbutPsgPPO1o-ni-WYRUPwzGbAaqbjbPazGJ0kWKDGOQIEJ6pYGlBBrfOOcrNY-UK51y3bUpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJ3mnEYWlmdpKR-DYaLd5K9trgGEpH5etdT-5Efq2OS8Oo6xpMX0cAWFFustakzLGw-aEHKqlrxe2zImR6w67tLMFeOYIh1CR3au9YGViqV1diu4uUpAPsRFF2b4XvRlTfq3C3wRHpopEDZpUSxf2EzTRrWnpFCmAZiu3LfRFIwlf2-R4tUQlmuwYeQHyoOYF5j9nTq-PyitL75f3jtoQfIcrXdUVsyvsxH4sADsYnHe2pcCZIT65JtyVpJF1X4rakS1cRDKrIjMPfAh7xEB__kJWhFmXiSF1INuHyEMpJS07a15Wv9_kqzKT2eEg2IJ90Nu0NQlShTqPrsO_YNokg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDWAvEJtDA5gKYZnviRmkwFfjBh_Kyyxl3WY7znZUERrIqief069siDMDPVGCdfs_8oh1spblKKTyqrxS_uCTNVKT-6OOff7PY3pD6tPA9ej_YQBuR13XQG_O_q-udtWFFh8Zi8s1xRxABUZE6lIBa81EAX5YGESF6-vxY_6G14JaJwdsAp5YPyJ60S03TPN1XrVQlpm3V60wwQYd_4lLZpdX65duQ21om2BBXgsQX5wlHYeEkOX0Ho7IeLNH62Hk541GEPRiVwxF2HWVS7lm52iPHTN4_D3HFOV46WYrOyTZfrbIwSqJ5Hop-dQYko9pg_wlzPvDTKdfGe3qHlihQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPbN-9vWQuHD1yPm-dUkjDCwsEU3qN6r4xeuf0ftjZ0GgncGN4Caymu6vA6iLqbZqe7ir8_88vtvyJz1JUERgzWR79JGn0L5KUIKIRp-Gr8cr1kjnBgm8QhqlhCrILf_QFt7V5O6icLArbjYGzFaDilklSUBRe_k0xU6j7eirxusN13wOamuZX57MSMwYbO67QDKk1ym3pGczWLzRcIozsG2g6aTak9fixUFILqvSCN8GRuxJ2S1iFx2tJeeEgqqP57fsrVwLZ-HrB4LVNTPmtGCJQw6hSlsb9jbzNsU48lvDrTN3zG5DgVpTHk8nlO77DfNEo9Q-hGeZ0chj-t9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=pEYorJTO295n5kf5jkTgGGvJKhiKHFXBqBNlnIq1v6sBTLcHBfy0n68663MYMvKWpC1o5-Gd8JQqG1invr6Yv6BLVhriZysLbwwuKiWzmpHGsWDs3VFZmNvnUm8kopW7_JCKrumu4Ot1HBCMk87lFs-P-M0WakICtI50Rc4MMkhx8ZkCYf3_gcP9HkrKnaJ0Wo-bdV0fXnR2S42B5HHN0fdgMv5Z5i0FydNYWlj3hA906MD9B87yymikqw8tRAluXpkspw_Pe3qr9EPt-TtQn09ngfw1V_RGyHbAlMKqypLMlqLr5PcTCL2zKWhAk9IkB4Fr3CL3LFe2P2iWzJGqXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=pEYorJTO295n5kf5jkTgGGvJKhiKHFXBqBNlnIq1v6sBTLcHBfy0n68663MYMvKWpC1o5-Gd8JQqG1invr6Yv6BLVhriZysLbwwuKiWzmpHGsWDs3VFZmNvnUm8kopW7_JCKrumu4Ot1HBCMk87lFs-P-M0WakICtI50Rc4MMkhx8ZkCYf3_gcP9HkrKnaJ0Wo-bdV0fXnR2S42B5HHN0fdgMv5Z5i0FydNYWlj3hA906MD9B87yymikqw8tRAluXpkspw_Pe3qr9EPt-TtQn09ngfw1V_RGyHbAlMKqypLMlqLr5PcTCL2zKWhAk9IkB4Fr3CL3LFe2P2iWzJGqXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5Xw_JiFVRv949mXiShsiRJ2aUM9PDiwZhpzohhWikybcDl-NI7xdVzUpPIrmy1kWw-S1d9rYDr-eQmSvet10E5O8-75pRt6Pxaw5h-9ZAOvS7rXUsYSm0aj1vO7WAosyhhSwKxTDGjRagkB9EdWui68oEUFyC0ebKWxgsG2VkGIqW4Ts4yO3mpvQBwjKv70u2Bo7nmfdgcxsWMY0MzrxuqJRhWMqNhYsyeT8qXezTI0SnBcwFGvPFsWlC9ieBRSoDqFizrHoCPqvUwQ48xZQEtUgb48hrKT8mSx3_D4aU3YEanF_M7IB76_Gb03QIvnVSf0IXVaM1OPs15vR9TQTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=m1yFCOPoCk4YgWpv9hzoR6PS_2sAhHVd0roH-MXz65bgvOmtkHye7rGIsmqwRc65Wopb-Al7s3dz9PfE07FFHsrpsYFhelSFgJCsz9qLXO3OQw3Pb7ap3B5HkQriCtXJ-ovd4ri43mG5KL19OC9wCHUiHCsjA7ySTZ8lbBkWNj_okIjhDQViLAMw_hILBboGkPsaF76psRDCf538SOoSHB9qNczhGKpViln7-oFoA3Gg8sJze1cSjuXM55xZq9SKe1On8CV8-nBFuMBs2VFXxhSrkvL8qPExW16uslxpzfI1Z1hybKMqwfITGL1lia9iYjrGKHFS2OgFesR3LKFW_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=m1yFCOPoCk4YgWpv9hzoR6PS_2sAhHVd0roH-MXz65bgvOmtkHye7rGIsmqwRc65Wopb-Al7s3dz9PfE07FFHsrpsYFhelSFgJCsz9qLXO3OQw3Pb7ap3B5HkQriCtXJ-ovd4ri43mG5KL19OC9wCHUiHCsjA7ySTZ8lbBkWNj_okIjhDQViLAMw_hILBboGkPsaF76psRDCf538SOoSHB9qNczhGKpViln7-oFoA3Gg8sJze1cSjuXM55xZq9SKe1On8CV8-nBFuMBs2VFXxhSrkvL8qPExW16uslxpzfI1Z1hybKMqwfITGL1lia9iYjrGKHFS2OgFesR3LKFW_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=TAJbSQjAX42Wp529_s9WdOf9grNRCZnr3BQIcomqcsxJQLhSM0pTFP7vM1Mpwnkv62jJumNdTTJLRfB1ARyJi7jqbO8pzR9DDGJsNUyqqzX8P2rceuLkgZ9qoGVp81rOdWU6Zsj_zPH0XputsdqLCTtraUUTVT7TZhyupgbmJiDiW2D9RmY3wVmahsevo7jhLEWWolGJ4GHd6P9TIhx5SZ5D-clWwR7BWcWNnUpItQ65oPW90GhaURFgQ_Nti2Juh-d57AeKZbAhM4DPwE7rcVE7SCKJzaCKtR1MK2QFAgWjX9vR8IdBLQjolHYRRsjFqa8H_DhaicNS99yjzsuLpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=TAJbSQjAX42Wp529_s9WdOf9grNRCZnr3BQIcomqcsxJQLhSM0pTFP7vM1Mpwnkv62jJumNdTTJLRfB1ARyJi7jqbO8pzR9DDGJsNUyqqzX8P2rceuLkgZ9qoGVp81rOdWU6Zsj_zPH0XputsdqLCTtraUUTVT7TZhyupgbmJiDiW2D9RmY3wVmahsevo7jhLEWWolGJ4GHd6P9TIhx5SZ5D-clWwR7BWcWNnUpItQ65oPW90GhaURFgQ_Nti2Juh-d57AeKZbAhM4DPwE7rcVE7SCKJzaCKtR1MK2QFAgWjX9vR8IdBLQjolHYRRsjFqa8H_DhaicNS99yjzsuLpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tv2QaXmTmqMUIvCV7OMcItmMxbpqBMNJsFTL1uvlPeMQUB_Yee5KqYpSBgEe-0gfTV4y-G2xtQNrVGDgtZDAT4fE3rcSVweOrwta2u79EXZwqaA7Kim-m9eY1sj5N6hpx51S61dUgBTKTMvQzqsxK8qryROZX30DpubG8SDgfvTqPE7bw7vAjkHQIlQoaaICOAOiNQZAm8ccVHNCGHGAsSKDwIorze37qCIeFo-HLqAWBfzcY0q2cIZPcRp3070XzAO8a81M99pBe7eZITuYoNVG6uxgJKxc5iYX1wYA4uQhKfjJ1XtcHtvn9T5lFtIersew8LGJeVSsLr8mo3yTRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=sWYZw1YTz2EuZhIycgjbcMAr-RCvu-g68WV-QmfN2qp2OE5M0KWF2gV8d4Nu79_d2jISY2oMo1_ipul2llbGGCdYGcxAhMwePSdZ4rNXyFncpTdkGCpOjyCDoz4pjyvHYBQIc3cOSBDYdAIirOlK3VzRjrhEKQ2NjNY9WReAIscR1-kKw87U6N3cMS5logzrg29OFQJeWpf91SXRB6veTvgSCYCK2tRDViwsAagTPI8w778ztB0j0o2tx2944q4edg1u5L4U5-6PrsD4GQ_n0MD7mK9dTVJNRoCwTHNUWstpMVM_L7EF5svGChuR9tbl4MEXS5ZOfU1k8LNjgeCsFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=sWYZw1YTz2EuZhIycgjbcMAr-RCvu-g68WV-QmfN2qp2OE5M0KWF2gV8d4Nu79_d2jISY2oMo1_ipul2llbGGCdYGcxAhMwePSdZ4rNXyFncpTdkGCpOjyCDoz4pjyvHYBQIc3cOSBDYdAIirOlK3VzRjrhEKQ2NjNY9WReAIscR1-kKw87U6N3cMS5logzrg29OFQJeWpf91SXRB6veTvgSCYCK2tRDViwsAagTPI8w778ztB0j0o2tx2944q4edg1u5L4U5-6PrsD4GQ_n0MD7mK9dTVJNRoCwTHNUWstpMVM_L7EF5svGChuR9tbl4MEXS5ZOfU1k8LNjgeCsFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9igvGtfylfVVzwHut6KUQec89kGM63X1XpE-1aBH4rUXaC-PyF5c_ZAVUhKVc66xQg6Xrx1SsyJEo_HM0sw4wRmhKNOo-9pv867FEClrxfvwAUae112spZv-qVQa9Fi_B6-YWp0CBrtijOfbm_ncwvQqD2KfEGNichu7nVXslseNJheuLFDTnYYvjDpi7Nv7enm4Z-oOojdJZBc52K36pt3P73vZYh5ot_RhlnnYXfSyw82d-eEgPRxN7ydqE909QE-s5ozyQBQTkmq2NqsXBUnn3V9Q3x6r75isyCW1X9-mieuSclT6vbhUpKEaOZllQTDnrx5PEGItiCVfERnmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKER4JvRLpw3jlLDu97dBZhDOa04OYkJak1_c53SsQzqDm3t6CZpOQSJ0jvrlIA4eORp0Mrff44jr7QQiro3-aPsOCnmElcZd_CSB-599Kmo1-qLpT7ZE1X1S7yNRdZB7iiySdgxdncCK3H2p4REpThgjeTNRcktAuKwB60cfdnKzowOjUcgzmG-iSwNhqGpELv1L1dagFsDS-hHs9SlcnIr4vNwHyiDGHyT4uCo9Gwt3y6XTeLBgUXZWNwVHJ8wSJr3zJCnRXFson3wzsqCkISO6VQ3ngW-EEbN7GAE6O3OeNPQvyGEuHBiyh84Au6vLnoHy_9Oj1xDnhgpXXGe_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1NcOn0_Tp0FsAsfnQlHHZpV_G_lIerC56bIji5Ci6G62fPa45P_l6vf2rwZ0fgSF3I28Ik7ySY28t2z-Qzmw4N5vT2mTIRZ-OgzeSfgG1BP5ZihaDcSwGAdRX5n9kkrlrMw3O4mNX1fB6cYRu_NVjf1NW-DWIyORdhf0jI67-SwG2A2aJubGNuIUaYqVUz-xFVs_449e9Md96yM5JqdhTw4ROsIeK-dFlil-UCO8CMPffVv7zvw3CKR71BHYJfeVT8J-tjBFBuP3nI0NxwjOFXLTuQPKdWvygEBkjTqISE4mqYLgLhpijYEZ7oizSgEiIYhKDNVyCdPea82-UpInA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDbdQZ3prrQ4-H9WEhLnVP66qV0erS98Fxn-GDZG4y4wqdqcvrOBUyzukEBHDSojJrlSRUJg91-gqI8S4IgwFcdoKlxhXxnxxN0ni4d2rk1rtXuE89Cq-ZV1CVeEjc4NFqWQnSAl2KfmRgcvthsC55D5bqN-eewA9u-i6uSC6bQp4lMy7SOrUk_ZddyadoTl0__0TCS-uMBI0hI6cOxDWZjASSkSCMca9-8eNP5Y-HOyU8SOQZRqEFAL7ndTY31UmKoH8iVW1d1-o4_c8uJDxUrZ8tupLmxfHIxh40U4Km6ZL-4P6kPOpqevyi7MZVu_c11Bamu9Zf6ZIEO4dnRRkg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=C_YW6brGN0xKzp0mZwL-es06Ef9p-JsjPaEsdmTuFFj2Eosv_WgCrDQPdDlGbONg2YdkXRw3zHdoJ23kcjnj1hesvokO1FGNa9PWMB_fyzyZttYGYau03hh26JPlgPERTXvII7M7Aq5Pe-YH-Yk_2rEyoiFC6_Nw5Vdw9-Dh_23GipQTrEeKtHU0B5OPHR9nr9e-Jmk9NKbMOZgbfTqHWPF3edvamYKl3H1SbCxZ4BvdvHny-r4A7HLULj2Dt1eRv0186_qEJxNh8KShlEzE1NWZYFn6IaV3vhsCovhSzS9zAljTis3PZy00Qc5h-KvEhmiatRguNULYT9gvJ_wtug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=C_YW6brGN0xKzp0mZwL-es06Ef9p-JsjPaEsdmTuFFj2Eosv_WgCrDQPdDlGbONg2YdkXRw3zHdoJ23kcjnj1hesvokO1FGNa9PWMB_fyzyZttYGYau03hh26JPlgPERTXvII7M7Aq5Pe-YH-Yk_2rEyoiFC6_Nw5Vdw9-Dh_23GipQTrEeKtHU0B5OPHR9nr9e-Jmk9NKbMOZgbfTqHWPF3edvamYKl3H1SbCxZ4BvdvHny-r4A7HLULj2Dt1eRv0186_qEJxNh8KShlEzE1NWZYFn6IaV3vhsCovhSzS9zAljTis3PZy00Qc5h-KvEhmiatRguNULYT9gvJ_wtug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=BBKtMhAMNPSc7sMXyu6mH-LkdBsF9ZGupUPp8VeTEKnPK2MO1FhwHlR--ltBAhNJ0bFWFYooNZR12IzGiEII8yZ_h8hQOGOMck1EQjY9hd7ELlzR378YQKcsKXrPGCx9SGS4OH_Ewqn6dc_upyMF1xmgi894d8EWfJfzpobEIiAGmzu2bX6NPk0IcIIMqYI_xNAU03P65RtXfLPI5pFNB_rOxgGlfmUZfVYmzF1Og0od_e8TYS0Ne6rpI2ztGqqwAW8d5KjgTfm7FMTVFBGI7YcNQF4atFmc0EJmEaF5AryZJ0OghTjrJ5dIO-_vVc-k3VHXk47NiDs_zfiqM82-Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=BBKtMhAMNPSc7sMXyu6mH-LkdBsF9ZGupUPp8VeTEKnPK2MO1FhwHlR--ltBAhNJ0bFWFYooNZR12IzGiEII8yZ_h8hQOGOMck1EQjY9hd7ELlzR378YQKcsKXrPGCx9SGS4OH_Ewqn6dc_upyMF1xmgi894d8EWfJfzpobEIiAGmzu2bX6NPk0IcIIMqYI_xNAU03P65RtXfLPI5pFNB_rOxgGlfmUZfVYmzF1Og0od_e8TYS0Ne6rpI2ztGqqwAW8d5KjgTfm7FMTVFBGI7YcNQF4atFmc0EJmEaF5AryZJ0OghTjrJ5dIO-_vVc-k3VHXk47NiDs_zfiqM82-Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=LmpzABameRKbcAfCZG3efHDCwsLH8j1feQvOFHrxHKXXqnPOJ49jE2hemci0cU4xwAd82HnvxcsNu8_QTkIHn08bTDs9caZnqMpCDABbtHBd5jeWWOlx1ZymjVnUSSxwy15UZmSZxb8r7Cj_WLcFC7vz0ixcOj-2SchLWasz88JURRHtmdhE-hlzs4T0InZDopZFGpnTDJv0Qp65AajvB9vdP6L_-qO-AIMNUlQNT5LuoXvHwlvAZfgcpOoQdp3o2LO-2zmDsP1ik8B_UXPKzO1wbZ91tBTWGimTkdCzdK9fRNoAerWFSeG8gjbhU7_uv9HpJndA--ZX45pdYinSdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=LmpzABameRKbcAfCZG3efHDCwsLH8j1feQvOFHrxHKXXqnPOJ49jE2hemci0cU4xwAd82HnvxcsNu8_QTkIHn08bTDs9caZnqMpCDABbtHBd5jeWWOlx1ZymjVnUSSxwy15UZmSZxb8r7Cj_WLcFC7vz0ixcOj-2SchLWasz88JURRHtmdhE-hlzs4T0InZDopZFGpnTDJv0Qp65AajvB9vdP6L_-qO-AIMNUlQNT5LuoXvHwlvAZfgcpOoQdp3o2LO-2zmDsP1ik8B_UXPKzO1wbZ91tBTWGimTkdCzdK9fRNoAerWFSeG8gjbhU7_uv9HpJndA--ZX45pdYinSdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=O9F9e_o1rhPVGFfmFCg_w5lUtsU49LYav4DiKhgMmi6n6BFRTQki4fwKGQhqqG7zUuvXUTA8KFxW3igrIOx_ocTj0OevBwwsFuomMIawVx5viw6ar-cXzXanbgwuL5UyClnvaEqRzP1jI-EEUBmq7vsQ8VerHsL_KV3fjPCkZebQaj3sn0mv_lSZ4qP08sq1i5ElE3WEXlLujD28Fok8uy4VQPRNRPYSos0HjcOhzSo6xjkIK0VgE0jbuP00bLpW0uPORZLDQQpdE_69LpmwloCwersuFuwz0fCbFAp0xR3shfTRQeWlt1xLNZS1hmqK6FC25HAYAj1buaOqQar5cqwrNrKIa0ArWMSN4sM189g42rCmopAKqWhkU4jczANPNCIhX3y7tUb8dFUB5ybuKtY4htxKEh6mCltqxzPZP9NOAxhc50NJGoajXSr3F8pdjd8m4U5ps1GR8cZfI31qVJWLt0aEv82Zd09dx3GJbcVZHNkbxBPrnw-b0CnMv70VUPSFzcXUHe3CmwaxqE_fK8Q6wsjG3db1KUdtPsHJRISXVcwDwU-ml2NDSCZT3y8RTk35IQbRiF_qRt1qQBY3doN9Q1rDgxkHD1YpczGBhpi-Q3leI-4qg4zVitQoM6qPtYm30luS37yJbtb9jZcWNrY-CjxSb2FQZmfy-QsZ-Wc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=O9F9e_o1rhPVGFfmFCg_w5lUtsU49LYav4DiKhgMmi6n6BFRTQki4fwKGQhqqG7zUuvXUTA8KFxW3igrIOx_ocTj0OevBwwsFuomMIawVx5viw6ar-cXzXanbgwuL5UyClnvaEqRzP1jI-EEUBmq7vsQ8VerHsL_KV3fjPCkZebQaj3sn0mv_lSZ4qP08sq1i5ElE3WEXlLujD28Fok8uy4VQPRNRPYSos0HjcOhzSo6xjkIK0VgE0jbuP00bLpW0uPORZLDQQpdE_69LpmwloCwersuFuwz0fCbFAp0xR3shfTRQeWlt1xLNZS1hmqK6FC25HAYAj1buaOqQar5cqwrNrKIa0ArWMSN4sM189g42rCmopAKqWhkU4jczANPNCIhX3y7tUb8dFUB5ybuKtY4htxKEh6mCltqxzPZP9NOAxhc50NJGoajXSr3F8pdjd8m4U5ps1GR8cZfI31qVJWLt0aEv82Zd09dx3GJbcVZHNkbxBPrnw-b0CnMv70VUPSFzcXUHe3CmwaxqE_fK8Q6wsjG3db1KUdtPsHJRISXVcwDwU-ml2NDSCZT3y8RTk35IQbRiF_qRt1qQBY3doN9Q1rDgxkHD1YpczGBhpi-Q3leI-4qg4zVitQoM6qPtYm30luS37yJbtb9jZcWNrY-CjxSb2FQZmfy-QsZ-Wc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=VHQAiKbZ9JIJRhfTmLAR8L4NvOJAR-J1O-usIJQKTJVUoZ_NEp2i4E_1m4RJsM-it0jHGpAxC6VPzVsUt6FhjdWFwzVIcPY6FYxsLpxiyHs4AZJpu9CGX5_Ul6beYkM1DoUJ4No5cLV1hz-om63OKp54guPuDZYdRjROyJm_qnQW7gjD_2W7genkn1FwW1ub4hey5tK8-U9hz0rhkIRP_oHJ14hD8ON296JzFndHT5GbCG9EoLDtD0aHBhm4145sWXVCo7jZluPI58LTZGhyidwlOVBOpyDYYIoFd6eKX-fhaSMOpM_zsLdfMFnXuyh7KkwOb33qaxUiz_91vWteOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=VHQAiKbZ9JIJRhfTmLAR8L4NvOJAR-J1O-usIJQKTJVUoZ_NEp2i4E_1m4RJsM-it0jHGpAxC6VPzVsUt6FhjdWFwzVIcPY6FYxsLpxiyHs4AZJpu9CGX5_Ul6beYkM1DoUJ4No5cLV1hz-om63OKp54guPuDZYdRjROyJm_qnQW7gjD_2W7genkn1FwW1ub4hey5tK8-U9hz0rhkIRP_oHJ14hD8ON296JzFndHT5GbCG9EoLDtD0aHBhm4145sWXVCo7jZluPI58LTZGhyidwlOVBOpyDYYIoFd6eKX-fhaSMOpM_zsLdfMFnXuyh7KkwOb33qaxUiz_91vWteOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=g3czQpwwx_BMeN9GV5CCRHAFyX29GJF4B1jxkObgZyN18m7LsSy3-WdpYeJMPVgxenSI_bnJas-1GNzAGXACi5e1vTsA6TUUu-f9RPDjDVOZN9dybcyouVxRmaFyEyt-BsgPJv-raEWVpGUTAeDn6sFDJWwG7pduRfkREzVbDNMvrdfTLKvTb_LLYesLZ0Xb4jbjWtXBj20Wu6F8syvFHOq8d3RteBvRgdSibsaTq402AZY2ecsGyjoG1PzdoRGWZq5NluuxQpWHx83J-vY5qesZKfvCVEkc5ZuoHX75ZffojjE_6zLKDVsI18T2DCn0ix-ujj95lt7hQWYfPs-1Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=g3czQpwwx_BMeN9GV5CCRHAFyX29GJF4B1jxkObgZyN18m7LsSy3-WdpYeJMPVgxenSI_bnJas-1GNzAGXACi5e1vTsA6TUUu-f9RPDjDVOZN9dybcyouVxRmaFyEyt-BsgPJv-raEWVpGUTAeDn6sFDJWwG7pduRfkREzVbDNMvrdfTLKvTb_LLYesLZ0Xb4jbjWtXBj20Wu6F8syvFHOq8d3RteBvRgdSibsaTq402AZY2ecsGyjoG1PzdoRGWZq5NluuxQpWHx83J-vY5qesZKfvCVEkc5ZuoHX75ZffojjE_6zLKDVsI18T2DCn0ix-ujj95lt7hQWYfPs-1Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPKvmjDpHS6syhcuGuP5SzcY9_YCNt25s45C-wZK5jlHpXhK8wz8hK8JmGEGvJmvh1nkxgeSABnPl41vo0jFJQSDwz3D_2a9dcofpUR1FLm-OdX3WC0UGJzwNCQ6Ou3tlgx3lUkkPVA0fwHKDsPlzJmWzp3Yp8v2l7KvTynQCPvhZ7TzgeRUoe9oy9WPzqkX_GQSaD2eA3PzhwvolfYkZsWpZPA8VCDX_5Waj_I-jN1xBWU4JXAkFRAH762a2dWSG3y2eBe9I0t6RLxpWRfgEpDVaCFPI5sWnSNUoVaOOA1KBjsdReHusbpTA3r_6-2Tp4_hz4oBBdNw183qUHPXLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=Fy-Wb_KAZAoGpaE7R-2cTPLw4isuH0S5rjGEOwL-h6bLUK29qdXsehG6x6EjuCiqt6NH6E5OF8JWELoRz0RN2eCeKupztZnCKcZt9fTsAMVi7KVQ5IpXmTAP9G87gLYq53NNrL26eb-NAa8NRNaHjDRvMV7oh-0_GNhhjY7Ttk-gAzgXHGqDmrYD0MWVUnzLDklulP8d97S6BqB_NMNw93EfnFYc0opZ4zE0TfnAh4LfSrTpRxRM7WlA8DbTPFtepCy9SW1wjfs5qGPoCdnzN8ZhaSS4GYgY2UN1Fj_HaCk2GKNK8ybr02Bypmtnn5OEr60aKIybxTvWA9taD9V48w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=Fy-Wb_KAZAoGpaE7R-2cTPLw4isuH0S5rjGEOwL-h6bLUK29qdXsehG6x6EjuCiqt6NH6E5OF8JWELoRz0RN2eCeKupztZnCKcZt9fTsAMVi7KVQ5IpXmTAP9G87gLYq53NNrL26eb-NAa8NRNaHjDRvMV7oh-0_GNhhjY7Ttk-gAzgXHGqDmrYD0MWVUnzLDklulP8d97S6BqB_NMNw93EfnFYc0opZ4zE0TfnAh4LfSrTpRxRM7WlA8DbTPFtepCy9SW1wjfs5qGPoCdnzN8ZhaSS4GYgY2UN1Fj_HaCk2GKNK8ybr02Bypmtnn5OEr60aKIybxTvWA9taD9V48w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COvuHZBsmF32TgyVmnQosJFI3JdgH7YRiupjopjFod8C7HiYs4UlrXMQVPbD1Z4tw53Y4x3pLnZyTyoSuFR0eGm83ocZ4neEilpXPwjZ9sTVXTAtdeVhkm20aoxwxpql36Jz2iAdqwKCizShg9Ad7ms_x2-JMLA28HuUVc15yZnRk5xublDFJqAGxOgOqiBi4emXcDYaNAUxzvyvTLtdhjWldq7hHvQiW1clyCWteRaniHk9hqqsTPlYQIOUx5gEzcUk8AiE_-9XU81NWid2k35ahdn-7q_TSqK1pL5AxRi62pAK9GC-trvlRYRw97zR3SGB5Ay3dfVC1Fxz0oUURw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0_laHE0_ts8vfxQmWMqtCE6DuUeTDN2rpJg6wTVA_WTkndPMsm4TUT45mcQvLsSeqw0ydvYRi6wLttPwTCO4DH-PVxjkGSX8qD4vsb1WxuwGUmkCOYU_DlVxdKurWSgZ2ooHvckhvsvCGRg3lsvuKvvtCUhCb_lxQ26ct1YG01VCityKGa13cHZhSnQ3SixcQwzHEfMdDoRiHcLe7T5TPgAq5t5vH4rl5MYhc6DYQ3ini4-8XYpd4Xu6UAV4B1Lrv7_1b0yIyG7dadjdwQIAddCbnPoex9ocxRIA6R2n26Fq9rjpgbC0-aAdzP9Qo5slu2CgCv2I7sQuY2HSQfgxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=oLjqWVJP3kkpQx2YzCeddlLmxV8iw2LU3PGV5DyGO0CI_3D4vw2E50NpCX4xI6yTvc_9u3bKJ0UGUvM5_tT1AOh7aWvVEA6TpEzdyQgjjFYuu2TRwCPQMERPxzqGw4xAOvSt3_XfkS-N6ua1aJ-7nfUbSYCacXRZeJ7KAipm3T7ouv3ziRDcDmz9wsO43IDAOcZ5x6z0p4eKCnt2dio1fd9c5Bloz2_v4YZDKFO_VwKTTCwIq9KgGk_us6abylWp125quBLhnl1sHHfgKTGSycWmgVeRmRxHYXiRxwIqVtAdlPHDuZgvlMVIC3GozFvge__fccmXxP_WhnYFQk5a0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=oLjqWVJP3kkpQx2YzCeddlLmxV8iw2LU3PGV5DyGO0CI_3D4vw2E50NpCX4xI6yTvc_9u3bKJ0UGUvM5_tT1AOh7aWvVEA6TpEzdyQgjjFYuu2TRwCPQMERPxzqGw4xAOvSt3_XfkS-N6ua1aJ-7nfUbSYCacXRZeJ7KAipm3T7ouv3ziRDcDmz9wsO43IDAOcZ5x6z0p4eKCnt2dio1fd9c5Bloz2_v4YZDKFO_VwKTTCwIq9KgGk_us6abylWp125quBLhnl1sHHfgKTGSycWmgVeRmRxHYXiRxwIqVtAdlPHDuZgvlMVIC3GozFvge__fccmXxP_WhnYFQk5a0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=fwAuOpEdzDgVYISBmJkIgaTWTApYoBNqlz4g9Rdv7UrlQx0uPv4tJjATg9psb92RuqsZ7p0hmr7FgL5J2SX_dKU0WAKliIVYVpACQRiEGYdMJc2ko2A2JTOJEYbLXXp_41Fqz83cqyHRtKf5jYhzrdyY1D8VnmfJj5FF6gHPZBEfLvplMzblwLzO4pfnv6LomDKCZVPQqq7Dx9Od6ahtkuWa3BhJEI6lUPJzVcQ_NPyDyRsAQmzGnpK4AzfVI594rzdlAilorUaYPeUMtgtv2OysZKz7krbHeAbc46qnZsPmbO2YsC_JHxmJfiQg_zIfmNSZoD0xtgyQe878F9D-BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=fwAuOpEdzDgVYISBmJkIgaTWTApYoBNqlz4g9Rdv7UrlQx0uPv4tJjATg9psb92RuqsZ7p0hmr7FgL5J2SX_dKU0WAKliIVYVpACQRiEGYdMJc2ko2A2JTOJEYbLXXp_41Fqz83cqyHRtKf5jYhzrdyY1D8VnmfJj5FF6gHPZBEfLvplMzblwLzO4pfnv6LomDKCZVPQqq7Dx9Od6ahtkuWa3BhJEI6lUPJzVcQ_NPyDyRsAQmzGnpK4AzfVI594rzdlAilorUaYPeUMtgtv2OysZKz7krbHeAbc46qnZsPmbO2YsC_JHxmJfiQg_zIfmNSZoD0xtgyQe878F9D-BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=Wi_fSxnHQ9nwKxILow_aD4I-l8TZUDO8wlmI1LbRE16OkOxRIxP7FzGrG0w-gTjwd5TlqHBXHOTvRHXnOptw4vPSMZKJo4EZcAnpO3eYqskP848T9RYbtBq_fpaKZN7OsbGk249eIIWE5MOeeU-ZIU1V98YInj3Cq6Ep8vFUxGDXoXwEQMU0PKx8Og70EHtx92Wt5KkgriTReonKuAEG6Jbhb6MYp3XTfkR0QFFHtwap7ZDCiZFZYcobpPYnX50RFKXNpFYMLqkJ68mAkMzgY-xPf0r-KzcXCzPLgq5To0w1Ikav3FnbcqszjnyehcFPYF4aRm-2VTkNek82aZFSVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=Wi_fSxnHQ9nwKxILow_aD4I-l8TZUDO8wlmI1LbRE16OkOxRIxP7FzGrG0w-gTjwd5TlqHBXHOTvRHXnOptw4vPSMZKJo4EZcAnpO3eYqskP848T9RYbtBq_fpaKZN7OsbGk249eIIWE5MOeeU-ZIU1V98YInj3Cq6Ep8vFUxGDXoXwEQMU0PKx8Og70EHtx92Wt5KkgriTReonKuAEG6Jbhb6MYp3XTfkR0QFFHtwap7ZDCiZFZYcobpPYnX50RFKXNpFYMLqkJ68mAkMzgY-xPf0r-KzcXCzPLgq5To0w1Ikav3FnbcqszjnyehcFPYF4aRm-2VTkNek82aZFSVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-jrRTtERCr0_W3a54Foq0qrTeLx1IrKRhScGi3MF9qaQF2FI1uX52F6nE2BmzxQ1Gp2Aaqs9epAYa9Fnw3uC-vR1nxP_dxn3sDVwZObd6ECDKTDD4pSqWmvDlCu1Nsa--0ql8XxrHk4lzWFkXMhYYujWaO5KnMipkWxU826UbZiOfXgDm0CylICPPvIEeEyrBrmKTVbwpXsGzfUmTuMSGjH_iWgo2UBgOwsteFeG6j0_ty_7b6SLeKkzY8RUfIt1Kf5K6E7ipI3NZcAvkQc11Icw3Qc6V-IBnSUPHBhvv46Xiq0JLPW3r_SgB-biGfWsek9jBNPS6rl06lr-7WAgQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=uUy4qgpUZhIkJMedAYH2qIJOHsHwOSFz1iF6bW9dLhOidGH9Hc9WVf6NbLXg7_U1Cgc5PSTFoXOLLxKGxhpg3Kcxk3-NUxfjZBgZGRsj1_9akQMY397T99Dwn43vFgL22YEcC4Lq-IsRa_a2YeJ9ZO3YjUeKiCeh0NVEBLM77wS1HTohv0nwovbankvM05G9op8407ohGxzsXyW1YTmQOFkLCZRoSJiT73GH4GHdrg_F0ic-khdFUr1QTqAOoePo3wj7sLcHgKq-qm51klzWXiTl2MzWOrtVkcU9ODpJ-Ww89uFg7j7-v34Cubsj-PayPnKjsG5A5EW8M8ISiGxWlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=uUy4qgpUZhIkJMedAYH2qIJOHsHwOSFz1iF6bW9dLhOidGH9Hc9WVf6NbLXg7_U1Cgc5PSTFoXOLLxKGxhpg3Kcxk3-NUxfjZBgZGRsj1_9akQMY397T99Dwn43vFgL22YEcC4Lq-IsRa_a2YeJ9ZO3YjUeKiCeh0NVEBLM77wS1HTohv0nwovbankvM05G9op8407ohGxzsXyW1YTmQOFkLCZRoSJiT73GH4GHdrg_F0ic-khdFUr1QTqAOoePo3wj7sLcHgKq-qm51klzWXiTl2MzWOrtVkcU9ODpJ-Ww89uFg7j7-v34Cubsj-PayPnKjsG5A5EW8M8ISiGxWlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=R_9QJ7BiTjx8-jJo1wqWfDSHlwZ69UiZqsivZeCznYScPXtPHgLD7-A6wEzm0wGzLenbAHdfFWarJxuQx8gsuw8BIAV4scznpeiYsoUHqbce_60YkPV_KHsk3aDudUfcHQF9_u6GDz2WrUqxyjJQpWPXCACaPdPIwtsfOzNdUxO1AKnwYZss_yRN2oRTKXRrQPjsC2GLJwHZbmBF7r9aqC_x9pacsASzFQB5F77CHllFppHXvxPpB1u69yiYCPRqla_-E5nYfpnj5pMTM3yyDACH7I63xzZ5rY0CIjkXBQkuVZg0ur3I1JT8F6gzl-znA89nRiNdS8LOg3zuyaD7tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=R_9QJ7BiTjx8-jJo1wqWfDSHlwZ69UiZqsivZeCznYScPXtPHgLD7-A6wEzm0wGzLenbAHdfFWarJxuQx8gsuw8BIAV4scznpeiYsoUHqbce_60YkPV_KHsk3aDudUfcHQF9_u6GDz2WrUqxyjJQpWPXCACaPdPIwtsfOzNdUxO1AKnwYZss_yRN2oRTKXRrQPjsC2GLJwHZbmBF7r9aqC_x9pacsASzFQB5F77CHllFppHXvxPpB1u69yiYCPRqla_-E5nYfpnj5pMTM3yyDACH7I63xzZ5rY0CIjkXBQkuVZg0ur3I1JT8F6gzl-znA89nRiNdS8LOg3zuyaD7tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=hJpnXEI3PMk8BwXGnHhJJsKLysWr5yuPOe-2O_L3u4D8g7QDvSxqXqEXJToUQKqzYlnI2f1i0ir6aREzdoaFFgUzRdhFBQFnnAnet08FQp-dIAztuIDLFXDeInrTQf7t9HP0C1r6O9WTTrZd_mQnZlVtK1dKQ43YhVWsFvccNQXu3eqW-1ou7sGWOw8prFQbgtTl3Ehgha2y3nFiOHovh7qFd-A3pzoZdqh_WQ1BuWO8_ok3rXBKGMYIi9YZMY2MDTwceYaic3UgsOLwkyLkFazVjj3We8Imgr1zdSXx4q-s4Uf4vT-wX6Oxw6wlst3pGsk9-P7iqszHkh3Q0HCoaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=hJpnXEI3PMk8BwXGnHhJJsKLysWr5yuPOe-2O_L3u4D8g7QDvSxqXqEXJToUQKqzYlnI2f1i0ir6aREzdoaFFgUzRdhFBQFnnAnet08FQp-dIAztuIDLFXDeInrTQf7t9HP0C1r6O9WTTrZd_mQnZlVtK1dKQ43YhVWsFvccNQXu3eqW-1ou7sGWOw8prFQbgtTl3Ehgha2y3nFiOHovh7qFd-A3pzoZdqh_WQ1BuWO8_ok3rXBKGMYIi9YZMY2MDTwceYaic3UgsOLwkyLkFazVjj3We8Imgr1zdSXx4q-s4Uf4vT-wX6Oxw6wlst3pGsk9-P7iqszHkh3Q0HCoaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQumlX7lDfABf-LtiHNApdBLyrECPSdfZL_ym465bg_urNE02kv-WR67Kt2Q5Lf9KOuL7bWU565nMOBzQnKa0RqsNOwHijqmG4MTO7CvXWNu4L3a_B914r2Q7OcdRSLOI2eDJqsCeynTrUIsc9wIL9HnVbXc9fgSn4evpCGuB-mkax4-l8MxziMY-JQOCAAtaJIi_zzj72_WSdXz1NoyE2HzvczerTVugI5tODN62QjxytFuh2xGaQBy73_Gbg-IdxLLcJ7IcRu4Rw0WpSl2QJZ6FDEKWBMC3RCpcO5kOYe2-mfG5RgnIoV9dtCLIMcXupdcFL-bwrgx1D-ZpeHBBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=GHSGR-lRZCnM4OySmbDkIYmydJ6nJM53lTce7Vid3fYOlp0u9CXJl-lWL4ih30SDX_o2Q7epFzaEzWcCZa0wktCBH_iE28Rmr5XKEBo6v1lkDz6sQCIFOXVxe3xkagUwoMLjNKfIePQpgOkT_BLBLc12SB210IviYIVHiPQG1FIPs4yBu-ggcpupyZB_9YfzIbRmJJQAaiAX0CIJhEfCFVpLnZXtjewMZpqVdSg7r6Iq08KvsswLRyLvb2Ddu6Q0q_5Da7detc_Hvoqe5XPXgSKjmaESKn-rVwI0kZL73Wm6rQCaTxzNfngQAEH9NROayu7XIInTzIPMjWTgTXOiZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=GHSGR-lRZCnM4OySmbDkIYmydJ6nJM53lTce7Vid3fYOlp0u9CXJl-lWL4ih30SDX_o2Q7epFzaEzWcCZa0wktCBH_iE28Rmr5XKEBo6v1lkDz6sQCIFOXVxe3xkagUwoMLjNKfIePQpgOkT_BLBLc12SB210IviYIVHiPQG1FIPs4yBu-ggcpupyZB_9YfzIbRmJJQAaiAX0CIJhEfCFVpLnZXtjewMZpqVdSg7r6Iq08KvsswLRyLvb2Ddu6Q0q_5Da7detc_Hvoqe5XPXgSKjmaESKn-rVwI0kZL73Wm6rQCaTxzNfngQAEH9NROayu7XIInTzIPMjWTgTXOiZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W46OBADSz63AFBFbug9j0Fx0ckMbkk564xyqDw6qt8rxehLk8T0FwfeqydeFj3BvkJ2H05ldy69jUhkUHTAWsbaUSr6FPZICLEQ3RdcXqzT2EL8fkinUMPeITBgKfLZ2IXjAz2xDOOiCs-HD5St3SReJN8bUDsiFspDZv24oFCtjL_KXJSjn-uxMxYIi8wZPVxbMWHJvnIDPSk5FuflPJL6ZEOxyRFn-lwsSQAGKBVP7fIByycEADqWeUOR7m2ivl8u_YfoaVAA5tND6QpU-OOIrWs0F2dLtgaflXZdYqAn0XXSaYTxIeNP3_ZB5tGXoK-a0BMWVB4qHroMp0cwcWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=vrqlvr0-mQ-Ji9EK0PHGaPgptK1w4WPgzpXEw5sHg4NsLTWByKzicN1ziwAObkhZ2iNkl-kStAMivSMljexXd0nKxb1GijQ0v32WAjZH2qEjwEjXZjaOv6S2mo4fjcw9AzTG3-s8C2mKEXoBzl-tbAOr5vDXlQPveTcLNkV9_5DsMBJgMTII6jPfCpY3jDNLV2iqixf9sZT_4OlHcuCj7bLCcUYNxCNXzDbHnMrcrfLk1PE3IwA4JXtzlh2XKV8eXXOBM3ZZ5vaUnYOCP6Ivdf-XIfaRIBa1c1XPx_Kyp4qf0k7SEfmTVl5IqITZejse7sZKNq9XHXdk03shGU2QeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=vrqlvr0-mQ-Ji9EK0PHGaPgptK1w4WPgzpXEw5sHg4NsLTWByKzicN1ziwAObkhZ2iNkl-kStAMivSMljexXd0nKxb1GijQ0v32WAjZH2qEjwEjXZjaOv6S2mo4fjcw9AzTG3-s8C2mKEXoBzl-tbAOr5vDXlQPveTcLNkV9_5DsMBJgMTII6jPfCpY3jDNLV2iqixf9sZT_4OlHcuCj7bLCcUYNxCNXzDbHnMrcrfLk1PE3IwA4JXtzlh2XKV8eXXOBM3ZZ5vaUnYOCP6Ivdf-XIfaRIBa1c1XPx_Kyp4qf0k7SEfmTVl5IqITZejse7sZKNq9XHXdk03shGU2QeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1eqiRGhxT8tq03O23XBzy1PjXb6-wOhR5MwPXSyxKN3hZWGZD2paMNuaEM_tDwmE2mAMK6aOONy_4kuZQKRlgMdKIcBX6bfyDZXXVaHAEx6mAVQH8yfKaISfQKY2JDQVBht5npKJVSajjVVt3U-A3bhlAQ1G0nL9w5F9WPico3mLVrHUYvvxmjyqhlEQU15xK8EUVX_3-kfBCDMnIhOWXbg4Mhyv5Uhd1OvjsEteDesbfcb0uCpWwH3kYITsvIiQpVqF6EwqqiJ1J5I3zWtEeH3UPTU0XCaKGbhacazH8pYnyruj2PTI8dSrkrgxNy3gR9MkGqySSI5bo10dV2omw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=lzAEuMNnyOQVOfr2qD-qOe2RmaDIdMiZxzjdpxzUWcSIQyPxrfB-BbzB9egVYnZcmlJPNR3gwb_LhhoacMQjoAMAvrw6dxTNTV_uwuE2f8nmyHFx6MufuzcmXLnVtwxqgtmZcsnL8mnHRaabeolIpklMEcg5_xHwJbtNjy3Bwnjt4O7pl8fkTkiltObQsozn4IK5tQrV9OnBe_A9PbkeV1I7bvotZcIbqEq6cWKtk_1H41V6epsiCAFa-XEso38BaYTaFXojrA1GE8yaRPwtXmhSYMsNtorbPO9-HDlGLI4JBHjgRks-TcCJzR_Bmzrzq91Y3Imy7cibhlRqG-cYnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=lzAEuMNnyOQVOfr2qD-qOe2RmaDIdMiZxzjdpxzUWcSIQyPxrfB-BbzB9egVYnZcmlJPNR3gwb_LhhoacMQjoAMAvrw6dxTNTV_uwuE2f8nmyHFx6MufuzcmXLnVtwxqgtmZcsnL8mnHRaabeolIpklMEcg5_xHwJbtNjy3Bwnjt4O7pl8fkTkiltObQsozn4IK5tQrV9OnBe_A9PbkeV1I7bvotZcIbqEq6cWKtk_1H41V6epsiCAFa-XEso38BaYTaFXojrA1GE8yaRPwtXmhSYMsNtorbPO9-HDlGLI4JBHjgRks-TcCJzR_Bmzrzq91Y3Imy7cibhlRqG-cYnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XD7UNyt6PCRpoxMObgB8sPYw_Z_jcq3SRt4H41E_bi7MUvJhPJOz5oHWOuMmDHl4iV32zEMfpsLHlDccvcfIZilhTpei7z1dACrkPNkoW9eXrjeSXRLcAcdZ5xisb8PbJ3xzHp-BlPlubEynTyuMa7Pn_2VtLMSDFvj0MXx1CrOcESmQdJXNoNydYZzb2QN5l3xbJF3lP831kP8cKmPa8aZkgYgVoEVJ4R71G8S9whI1wn-ICZ_aSp-IemMa9JlQANkbpphROfUyiZUSbWSNqr9ryZF4-PLOesnPInMe1SDusf6avzMgX3OkIDG86MIyjieeG66zqQHCdFJ8DzqKWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQMoa0GpLkez6xTfpwPN5z2E4d9IK4buqmg28azzNfEkGsJkMAo-JwVlZ-icQVDg5OdOGN5pBnxJQ1pv7wE43CY3kEBPfJjvGehZg6HJSKeU98u00eoCj3OwNBmBhWhuXCPgZYDEp5ZEORhiclgl8D_VexAQ0dFj_JDLSbnEPFP27S3wMtogbutx0UnQTvBaDVM3yYikCKpn4pa0igStdf3LpxitVFeoYAKoZhFkxC0ytaZ_F5mOwkfva1lZBp-qFJSJfhgMzimzNlZt3Kx_rLB4IQ2bdf2UGEE-cKb1hAp6XVjydbhC6-kip-Xnk0qysZcW6gmc6I2P5_WqyvAiOQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=besfrrs5P5VW917_8hevopR1b79aAfqcyt5zoujXIdU0bRztj9Z6LpA8RGeGJ56cQOST4TqZ2t9VFwUYvsXEC6Yw7RzthUXNppDDtVeJNUI_91jcOKEozANKL6rxoRCHiqGnYCV3vle4wxXAzurdxutT62lr9_ZgiyiMuZTxrPvMIR_kajwSgdcqVPHwcarvrqQs-2EDDSsvP5y7jjpD2aXskNhCNtQj8OYafwGCeZVjRjmZr3OhatLP-EaxYqOPJstG-MEP7T4mpGbO4RHTP7T5_5g7du1ZZ3hE-U6UyTWjGEuuGt3HcV8XiP6vE4DSoLtsrf_-whtfsoubg7p2TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=besfrrs5P5VW917_8hevopR1b79aAfqcyt5zoujXIdU0bRztj9Z6LpA8RGeGJ56cQOST4TqZ2t9VFwUYvsXEC6Yw7RzthUXNppDDtVeJNUI_91jcOKEozANKL6rxoRCHiqGnYCV3vle4wxXAzurdxutT62lr9_ZgiyiMuZTxrPvMIR_kajwSgdcqVPHwcarvrqQs-2EDDSsvP5y7jjpD2aXskNhCNtQj8OYafwGCeZVjRjmZr3OhatLP-EaxYqOPJstG-MEP7T4mpGbO4RHTP7T5_5g7du1ZZ3hE-U6UyTWjGEuuGt3HcV8XiP6vE4DSoLtsrf_-whtfsoubg7p2TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-CEUU3rG7mdc0co8Xqjxb1BIv0a1EwiKJFB5QXKTaB03_a7jo3F7M3wHhmGBV2pc-e-JKykxxfAsXQ8Or-jfYWq3LO5XwTadtt4mR3Kskt9pPjFGRgex5u_8t_qkXFo0otUGEYnxuLgKTV_V2Ar0MyI6X8V15S9GmMtTke9xaiW33RMttXNqGFSGUhnnHW8u2LHLaSXJuRAMu5s8Shv56G4dxfo-4R1TN8ikwZam3BbkzYjbWNCkocomAM1ZVqlRNzrDh2LA833qUQU7NYxk1CPImDyfwmEzRPCEM01_Sb1OzQGT8JA-NzlawM0Ag8OxtvpUVLttgbE_x9f5jUigQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eogbYfC7TqBHZK-2UnIP2bHa_nKj923xZezDwruHMxtF-jLTuicJ18iy2qZKOAeVrqCGrTjbr3oWk75EvBiPJ-UVfwut3Pjn1KWxMOeXc0H_6HFzW7RdCF_3S3tHGBRnEEQ_JL_StZILtbm4H6NfaAhxryo1s25ATn4EaDCx9zLw_vJ2ghAbKdtcCJGblf74v96GDM1zX7DSTPBUODdVVwbIIyaUDi-3xnT5UWsJ9c3lklZFHQfk1Po1bALI7C34YifZd16ilyHNNj-8ncjasCgjBJV3Dl0GFG8yT5zjvFIWf99FU303i05MCKWlCwKaAv2KfjbC24Ptu5Aom1aqpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6445sHuVOI1ppWxA-pDEKEVfmPoCm7ou3JfJhS56GzG0iel4U7jXEDeiKusujmv_QPIKhg_5bEAAXi6VU6_i7NPib3HEV6WjaCalrBqFdnwjiBQII_x6vwr6hx678uLk3IPpUe57-DELJQ6uwlhaEiHhRvlBRDyP3oJPd6ww4hIw5aOov1mD_NIwKNSnBj_sBGaLJnxBcF-uIeGajvdcg0jSaG8lcveMXkCAno6oEKEcECe0e2CHE_6CGSowwJWhUsDljBBeGQRTumWyNaUiTR8RwTRaaWZM94RCfbw3dlSZh_WXpJ8d9aZwOCKNEXeVdxLRKtHilUA6UJSsBnLrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISy4SL-Q635VORmTDB6VKNSKyQ8gQex2BKnexaeFe9qXax2QSWi9bDJuUJqSO4WMmBAKDpOvk-Fi7o2TsdQ_wOUkkMCEWmbakHATttWbhxWJmDP_rZ6d1eYS9aaUKAALXp3eYiR_bMOXHsYJ_a3RJJcdz7Oz3BUmzTEmzzGhvyxn6aT30Jy-0CXdpel1P7XaPGmGB2sn8tFQPH9WwJ4XazLMi6LnuwMJJH-NlhHFILgM9-vAH2OOyvt6fbXPj4Ox-ap82WB5VDqNEpVaqxVbzRJtC4jesRaMvOIrQw_jc-NKJ7ywkFg4POdrhrgLRx_Ai1GK3nZURG-Qh4KUOAO4Lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKkqCO77L-C8ewPY5E_-qyATe6TpBlFuhqepm0UzKKlYIqJRskjxCL1jc3uYg7AQ4R2Rv8Vwkx6wDBayj2IHn60m_0FgL10R0JknwDOvnj5EA2BCabBPbKa2obKctudHa0BLEZVQX__Krhl7Q9XvzxYZ0pdxGhmHG6EFdm6KffKbOg9RAe7PGZeF2dL0QhK2FApmsc26DjOaBxoZBKIaKSpXbbGN_IjBDpeAsGsSvpJqfLuA-lCgeckSo3Rj0JMovp0WwIalXyHJrBGup-CgLcLxufyQzTL41ELMc3Jso2gDljQqEdOWzPIha30rteS5h_l9lNuUu9l8zcKJMxggvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=PRLZVxuCgwtvm2f5A5kdElBmNa9BO7xSCovGuZnK4G9eBtVw0cDS2aD_GST08YXiPmWYsBImg1C0s9AfbaEsTv5dDk7fEfJo44F-jEoI8iY_o7UPS6MEgFsu13aY6fyGantv4fFzIwZtF-9XD17tLq0J8LCBJ0yfIBwzaOWfT0QutYrlGTDZeAkSDJOSlW4x4ZkDAA34xpEqlhI1uHG1z44dmhyp3sAIuTKDf4-szZEwdqhXtFL4hD2iAsjDXtcZ_RFSWqywVRg02ob_YpXgVZMuGc7xT2ChT66N-LSPfqYjSIoWWZXcuy2pjiDwpkgELbhEug3Y69hxI9_W0l7olg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=PRLZVxuCgwtvm2f5A5kdElBmNa9BO7xSCovGuZnK4G9eBtVw0cDS2aD_GST08YXiPmWYsBImg1C0s9AfbaEsTv5dDk7fEfJo44F-jEoI8iY_o7UPS6MEgFsu13aY6fyGantv4fFzIwZtF-9XD17tLq0J8LCBJ0yfIBwzaOWfT0QutYrlGTDZeAkSDJOSlW4x4ZkDAA34xpEqlhI1uHG1z44dmhyp3sAIuTKDf4-szZEwdqhXtFL4hD2iAsjDXtcZ_RFSWqywVRg02ob_YpXgVZMuGc7xT2ChT66N-LSPfqYjSIoWWZXcuy2pjiDwpkgELbhEug3Y69hxI9_W0l7olg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=aBOzBPOR9nlCK6B6D6859XztQRcRxba6NVCtXaJxllAZl6JAf6eNjodLa6R8nVdeU6CwA6Li75vN3l03opzgPd1wmZfKlEsKa5jDoUA_WMIuM_u3dJfH66yPZN0sIXTGMjDiaAiQQXxgDtuaKeIpNmkK2ZhljxbpuP-_-pOQn5zaqloKZo0gbeiAVQQlL_b43IvIU5C-3GFTp9pUCQHjvP_UKOkjAxe-l-oO19_140mGC6wXvqfVrIkruSeTtn6lZ1Cq3cz5czf7ELlzEtHubs3gVuBHl8GJZUhepF7wZcyv7CqoDJM427Zi54saHlGQObKWflr2trGJCAxy61yAkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=aBOzBPOR9nlCK6B6D6859XztQRcRxba6NVCtXaJxllAZl6JAf6eNjodLa6R8nVdeU6CwA6Li75vN3l03opzgPd1wmZfKlEsKa5jDoUA_WMIuM_u3dJfH66yPZN0sIXTGMjDiaAiQQXxgDtuaKeIpNmkK2ZhljxbpuP-_-pOQn5zaqloKZo0gbeiAVQQlL_b43IvIU5C-3GFTp9pUCQHjvP_UKOkjAxe-l-oO19_140mGC6wXvqfVrIkruSeTtn6lZ1Cq3cz5czf7ELlzEtHubs3gVuBHl8GJZUhepF7wZcyv7CqoDJM427Zi54saHlGQObKWflr2trGJCAxy61yAkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=fbuOyO_F88PWtt9G5xiSAhlgbVdSd1sm21ZMoaEt1qeLSwKbUXxlGT8Mjl2QU6XxKTDlCTjaO5EeIIPqgEI2hi8Rv-o6Wzul6roUXH8oYJqWWASpY2tsIPFj6HXFGPcStcVPSwz1D7FUNurTKN1U4y_DF2jRUTIMVOKpC4u00S0ys7shPTbu2hH4mQ_1B6CCsG3GS1cLo5SX3RyzKmB9-qEsehdQ4JPl71h_iOWcxZW7D8l8YJcIk8C4nBQ1K0WyFT2bEYNFa2A4h_Rx3i8CNbxPfYx4rscTs5yWFFlf6PRWdukAqTsI0AX-bhU_Hs9ne08oJDWs4DZVprIsMPAEhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=fbuOyO_F88PWtt9G5xiSAhlgbVdSd1sm21ZMoaEt1qeLSwKbUXxlGT8Mjl2QU6XxKTDlCTjaO5EeIIPqgEI2hi8Rv-o6Wzul6roUXH8oYJqWWASpY2tsIPFj6HXFGPcStcVPSwz1D7FUNurTKN1U4y_DF2jRUTIMVOKpC4u00S0ys7shPTbu2hH4mQ_1B6CCsG3GS1cLo5SX3RyzKmB9-qEsehdQ4JPl71h_iOWcxZW7D8l8YJcIk8C4nBQ1K0WyFT2bEYNFa2A4h_Rx3i8CNbxPfYx4rscTs5yWFFlf6PRWdukAqTsI0AX-bhU_Hs9ne08oJDWs4DZVprIsMPAEhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=aoen2js4K4zA6hurL1TjtkUlKCGJS-Ewo_mqbECxrayKiiyQETG5y-2s-MmqaY2nDaEr6l931jRLxSEFxmIJPgcv5BNQKjov3N4X5bbUCJfcvVCl7HXsF0VYv2y6XT8z55lEWkYat9NQsEHFJVnnNv654L2eGWSIF9X_IXUbayBoWGGQdh8755Ityn1h6VgY0kqGBOPCRq8qPRAgx5_V5ohbyCRiOPreVlgOC78ugTQbBGwhBnkDVoxXqbmFuvi-09_oUEzA1CVRzyqsSj3aAgIJNh_nvjA40xwofHyjVumivudc-QTW5angCosgBFe7xQEhNUG3S3dtTKmvO6o-yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=aoen2js4K4zA6hurL1TjtkUlKCGJS-Ewo_mqbECxrayKiiyQETG5y-2s-MmqaY2nDaEr6l931jRLxSEFxmIJPgcv5BNQKjov3N4X5bbUCJfcvVCl7HXsF0VYv2y6XT8z55lEWkYat9NQsEHFJVnnNv654L2eGWSIF9X_IXUbayBoWGGQdh8755Ityn1h6VgY0kqGBOPCRq8qPRAgx5_V5ohbyCRiOPreVlgOC78ugTQbBGwhBnkDVoxXqbmFuvi-09_oUEzA1CVRzyqsSj3aAgIJNh_nvjA40xwofHyjVumivudc-QTW5angCosgBFe7xQEhNUG3S3dtTKmvO6o-yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7J6NQtvs62zV1nwb6hpJYy4indX96MZ9xJbJIGU_czmgnebdrqLoKN5nrI-U9qwYQJVyDB-7krPfV4Rd7puOuZCOh6eJVz0FWvVUd4B6kPUKX_nNzWCb9uG1nMQFZk88Yffk_39saLPgFIwpGlsqjRSN4B5DTJ6nl4nJSza0AdKGU0kd1mDOx2qekjB0NG0_GFyI0LMG9CU0X7R73lSwCY0-aNV4O8BbAIou4XuNZxaNkQucJZIbN55WCu_xYdCQnmuu63hlz-8Asm791M5k6tImGLAieJu0to0O8EI6Y5rCnbaCP565XTziJqQKbeeNcVRDAYbUzApYzFpUM4BbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGvWuj_Vi-EauqF9FYddiYFnVMKrYutHuww7E0cEyhs45bHuL-vq2tvdGK76B3HTwp35Wb4zxuzsYWhAG1GBLrZiTwCAGI3bIY4aVqs6k9Yta99oIqn0TkCeb6c4WejdJpDegzM-8N8af36tnsr24taAmTqvXVeQSxg6tJ8PKlYABvRGlth1CvoMeXFC5-3WvNunzZgirmEqNeSAqly5E4KHWpU8qwwGnlBDga-oe5gPqauqx0tsYUaW5zI2EZFJW8l4JYNvIbdNraqZriORKRDK0eZysEOtaxRM6iPRbb2fzUxhl_WuA0IfrWASWdUCG5i4CRlsUdCrW3gyzwderQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=k8MpaYb42rbfHpxZWaJXH94ZPbzEY0bRarLhbIgyA1KvpQIX6u4mzb2jzOYcDADNMF3KxeEH6CeFJULLTj5VGWaLNFPgpdKWcUAG6XZmsr4QRl1YsEDETzyJIzhz8_oz-2PEQ2ZFtF5ypVP6QKwt6LaT4pO9PBdjwg1sbEY8O4lMMANsu8usXua3SFA6WOl4LF1jXkQZV5i_57VENtoX92tHLghxGQHQfE9adoTEt8Zc7eZAiL7vn--a0vCB7ICjfFUEgbCT2zRUFtc6HS-WLdtX9SO80hiwCjW9n-WhNooxVbCGCk0V4XXF4r7FTve0hgAp98sxH0OnYCGhULGlmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=k8MpaYb42rbfHpxZWaJXH94ZPbzEY0bRarLhbIgyA1KvpQIX6u4mzb2jzOYcDADNMF3KxeEH6CeFJULLTj5VGWaLNFPgpdKWcUAG6XZmsr4QRl1YsEDETzyJIzhz8_oz-2PEQ2ZFtF5ypVP6QKwt6LaT4pO9PBdjwg1sbEY8O4lMMANsu8usXua3SFA6WOl4LF1jXkQZV5i_57VENtoX92tHLghxGQHQfE9adoTEt8Zc7eZAiL7vn--a0vCB7ICjfFUEgbCT2zRUFtc6HS-WLdtX9SO80hiwCjW9n-WhNooxVbCGCk0V4XXF4r7FTve0hgAp98sxH0OnYCGhULGlmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hspHJj93XzR8z2cSlWZ-r3E5e_g_aWvSPgREx5eCICQkJgB0UH2a5_cuVQbTiuzfgFgye359z8PuJDAgwtevj7ALHiIZ9Vn9KSLjhvw6soq29sn50Vg8I8Rv_keyMJWYsddXBLUN0N-7aO9lyHOCzUtzuo9cEjxynd9zB41q-kz3lGtT2LuYs3I3zDTVgpr-F5khR35NQ3vHIll9dPpuZcFIKnuNIDC38MEgEfamJb75T2_6RvNZuJJo7rVs_aBLwlz6Om8PK6hw88qf9JzP_HNi2vTb7HB2gFq-jMtNcEzpHb71niMzhCUBQgGVl53cBEJHzQZ1wqwe_ZZrsuC0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=A5c6QjEkCYfnccHP6DaQaG4BQvZ2sirzhycTieUrkBGah-rK28SlQ2MIVaVTAnG4o7wn77nLRbxtorpdYcMrol1orkXlWHGJxihsncqPGuk_UyM8jg133DwCGJLXz27fi1ZctHlPLC6czYSdNaIBfdu4tA-IXWL7pQ3nPQklMtgM6jMY5MVYv6TuiJ_kmxVSK7fLvng6b0ejqPk02fsiNdtPAdBPm8qRY6H65YW2aakcS4tUJCOGkKem_ibrI9JEbGof5dvk5Y_syXSN4an9vEhsoGTko74IaUYGD5o-Ztq3-Bf1USkL10rkg3XPZgFXcV2p6kISPUWzhI5aCCaKgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=A5c6QjEkCYfnccHP6DaQaG4BQvZ2sirzhycTieUrkBGah-rK28SlQ2MIVaVTAnG4o7wn77nLRbxtorpdYcMrol1orkXlWHGJxihsncqPGuk_UyM8jg133DwCGJLXz27fi1ZctHlPLC6czYSdNaIBfdu4tA-IXWL7pQ3nPQklMtgM6jMY5MVYv6TuiJ_kmxVSK7fLvng6b0ejqPk02fsiNdtPAdBPm8qRY6H65YW2aakcS4tUJCOGkKem_ibrI9JEbGof5dvk5Y_syXSN4an9vEhsoGTko74IaUYGD5o-Ztq3-Bf1USkL10rkg3XPZgFXcV2p6kISPUWzhI5aCCaKgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCoAIG2kQTVex_GONWnuZKLF9qGmmYuRO-hvZ_3TprwuNEsCd-l8KRKNKJSejBfrn98W4LikIskBBd02AOnAbbyjsSQODIXzxw9gJ4TKFR-aFuKoaAxkEH6FG02GjqYfgZ7dh5CTKIP0m94MtdsSN6Qv380McHTormNq4nHnWq0D3bcNC0dNhpCrtEZD6qyA6Ak-4h1aLAf4sIKQMs47cIkT-gDRDRMz67NI9T9B_A9vlqE8BTWRP5_wY1P_kB0b097sYohk1vdlbqRYvc55PoDxlaq9KOSsDVfqD5gXd1qKajvUvKgrqF9Qj2wPsHHoy1cwewoLNiAOT7F3YdBUjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnPjWHhkh6Cnn8Eu38i9bK6sjIXRAQIRjLXiEnLGpmZ2F3y2_-mHS74vKTnq8aTY9Cc10G1F99a40ba4AwD97OBfVM97ghAxrr92lokcLkywN1yj08qVOc4q_d9F4JiOBFR16RBs0NGHJoLHjofQWG38WrP91RO-UyTqY9pBlDSeX3Ti0LJso-BlWFS3shwKcc3g8JgdtDw9uUfDZpLt4ql9F8s2s2C1v4X1yRDCEctt6NM5KCf0VC-zPQXfs1ieBXgy0ARWu9PTvJ-abhFQ6v8jRX68tZekAPP3vqMJc6gDTMh4mK9mq8yHED5yWa3j0Yt80AMZZKuM3iAw3Bzxyg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=f-cfMW3SL_NWhJFDJvhnIDxq74pnDvNv2RrhHFIY8HihETXivOBlkzGQLWr2IL2w1R5NAUeNENuDtFN2_d2zI0QlpGrB51pML1q1BzHF0z_gTl6wdygxLExXToXjugLiM_3fRJTWeRQ3jv_TG2OdSaU0PrJpNqJ1YoK8Li7vzB-Ffgb8vI9KqxtLoFV0Kuqff4ffwgMMoas0NUb6IJRwVrxUV_d78s9alGuWTDfRfay2GUqhAJc7x67byzah3-n1naClaJKxVQe15YZExCGzvBFNEdE0BKFhzmxSeRzqwF5HMh2osLnQz6esshYgieAH_5t1PpU4Iru8apwH2Y9zew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=f-cfMW3SL_NWhJFDJvhnIDxq74pnDvNv2RrhHFIY8HihETXivOBlkzGQLWr2IL2w1R5NAUeNENuDtFN2_d2zI0QlpGrB51pML1q1BzHF0z_gTl6wdygxLExXToXjugLiM_3fRJTWeRQ3jv_TG2OdSaU0PrJpNqJ1YoK8Li7vzB-Ffgb8vI9KqxtLoFV0Kuqff4ffwgMMoas0NUb6IJRwVrxUV_d78s9alGuWTDfRfay2GUqhAJc7x67byzah3-n1naClaJKxVQe15YZExCGzvBFNEdE0BKFhzmxSeRzqwF5HMh2osLnQz6esshYgieAH_5t1PpU4Iru8apwH2Y9zew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=bxITFoGblSgD-nW2nKWUVD2eFwxo6w6Rn99Vqi3OJ6kfDqilg8T544jbm7O-ttak7OujSbArsroIcy-VzH4jqRq4STFNlX7Lbt0SqJagCnGcQGL8W-L0uLjNMy71k9AVCsREOYAOBfy0ek9C2Dqu2JOpdKxUygKMUUvVWn4zklJs4YC3m4zkVnZkZBwmANIdZXLL815gajz02lfBgiF9n6yFZvWQvj8j4Z57vle5G1AnEmR7aaE49Xc05NH-g_pSCdM3enDstwoU3qqoCGWBo5jKHB4hpowyb0LgXXzaySuGO3MnKsCQETj7et_Hf1FFDR9R07gK-qProvWU06zVeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=bxITFoGblSgD-nW2nKWUVD2eFwxo6w6Rn99Vqi3OJ6kfDqilg8T544jbm7O-ttak7OujSbArsroIcy-VzH4jqRq4STFNlX7Lbt0SqJagCnGcQGL8W-L0uLjNMy71k9AVCsREOYAOBfy0ek9C2Dqu2JOpdKxUygKMUUvVWn4zklJs4YC3m4zkVnZkZBwmANIdZXLL815gajz02lfBgiF9n6yFZvWQvj8j4Z57vle5G1AnEmR7aaE49Xc05NH-g_pSCdM3enDstwoU3qqoCGWBo5jKHB4hpowyb0LgXXzaySuGO3MnKsCQETj7et_Hf1FFDR9R07gK-qProvWU06zVeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1Zs9Gimwso6jtnYI5SOiqwjzSX1Dhti1QAOa1Vy_zfoPaoNKlSJvNN4VqCXpuX3_HxXOJGfUugKmrXk1ztTwcREXLG8TfluQqkHgFX9wKM-wg1iciT4cmN9MfzCppkVR3Qzvt0H5WXREUGyWO1MA6p9v43Knaw5jVDbUiYf_QagD5fHsAO4rjxuKXugNfMBaQwRBZLBBvmlPbAMYSWb5FUDzgNhODRa98j6G00L9CuwRyoka--vetbbxbDUDa093JuKplaQGUb4J32KAWIc-MyurbmPa8yPcKcPTVgOhUeLyQRVSUNXtpc_LyHAmQ9_NIC85B-qWtYnTEhAoW3Zwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYQkYyBW0hkXyBBKCVnGVzMbkIA5ErI50zZcGzD9iHoNfa_QK7bzjlVpE18o9QlWxKMT8Hf89x02gnpPaGvSN2KznoInfQDbq1BlH-f56iS0EB9O3hOxbGLg9oUX7cU1K5XwYKOMmPh4m7lwG3446tzuPax4TDfK2QnCrEd7JDK2cU8TXwkVasQ5fvA-AClZxleU41Q4i31C5cf0WpmdrEFqKRVqji1F40ilR7yqmS-_2p297Fay2QB74Myaou9h4gUEKuS2pEye_YMPUrbWewZwKSdoyxx1Aa128V5O13mrvQ8RUw9am2IUsLJUIJSVUxZT1qL3PYOEAvHOWsbiBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQDBC_Prl55QM-0isb0Lc-Fv24GR_QvbvqruyOm0KMdUWjdsmAX2dSr_cXjfros8LXcQmcY_nYIjAl2uRiNIgylGLa_GcnCpC5dutUizmG_qC-r-oD33CyP-DFQ-s0mivj79a2h_o4uIY3EjcDdoYY2OZhNnftQFRdlPgy_UqP5vfio58FE-uIDrXYmocSPbyY6_0ZOO7GAiRM2Fkvw_9DvaHSpZbzE_JgHIGJs6JkLDj2CtZNstxf3lxzeG1JCXdZGy_ms-Bp7Nbo-oYSGSZ3KrF4hFgpmMX2Vr5GAZQzYltAWqYHhRVy42VaT4eSWHOU6R6CjFDbZwnqpMkGwW3A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=RtwXR_OQrKzCqxmO9auTvUwVOJzuqo83DqQAREfA9SA6IpXKUV5eeGer8w7aZx8L7AoC-1Nq16jCLF3jZlG3b3KyJfRRHswB5IBQtT0mCm8alVZQoHDOyWcxqiAevj5NDmdPRdl27n_Jgx_FuweM6ZK99qzaafitbAbpxUbkrYpFxLfopPDXbncUkx6T-0D5d1vw-lUMkkatwcki-GYaFl8Sh_Fu9f3kOd5tcs9dPXDP-wY6-EPkatVrXuC523Me4el01UJ9HflQzj9AOFNqsPve8OsmeaCnmF6MT6X-5KvXbQ77hMW7faNtwDJ1_tP19cehh6hsyLYiYHedxInEcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=RtwXR_OQrKzCqxmO9auTvUwVOJzuqo83DqQAREfA9SA6IpXKUV5eeGer8w7aZx8L7AoC-1Nq16jCLF3jZlG3b3KyJfRRHswB5IBQtT0mCm8alVZQoHDOyWcxqiAevj5NDmdPRdl27n_Jgx_FuweM6ZK99qzaafitbAbpxUbkrYpFxLfopPDXbncUkx6T-0D5d1vw-lUMkkatwcki-GYaFl8Sh_Fu9f3kOd5tcs9dPXDP-wY6-EPkatVrXuC523Me4el01UJ9HflQzj9AOFNqsPve8OsmeaCnmF6MT6X-5KvXbQ77hMW7faNtwDJ1_tP19cehh6hsyLYiYHedxInEcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYCb5TLdLcSgbuTYubDmcLSNiCbr_DJ4JdlaxfOhgMVceDA0ZPzOmaMsdUimU9WdQODjRxgcB-E8htsju6bx3OM4krHTds_piVXAQAf0NIgFOgIycHUqBhddj28MrsHqyw_9upsBKwvWe3Vt77YiP24JVJqIi_FVYHKUxcry5OTzjIsePvBzyJDfKacini7KWVlWNtiNsqZ4_riNub-1ZFnVOGxvARa-8LWxSUJ2q2mCwj6J-z8e_wUoEJbCJGcYD_nq_4yulU8KDSpez1RvDCu7RnvmFTe-ci83uhhVAJX26yJzVUuy0NtgApZ_R2scY3kCrDVRHP6wTczMhYYQdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dV2sDIMb0eICdLB-iIq-F1-bGHC01ArmmOZEmgpAS_iYFp15UWcTx4nqzhMx2adTTxr3zEGwbHDw6hHiccqFe2m55wotO4yXKzqQIS2jqnTGIdydFhba_34HDIe8eYjHtK7HocrxTHqDNgW2ZUUr6xBvCV6G4c33Iw0Hmc263gUwVSYxmVUm9WA-ZAqyJAbZNfaht0SrEol4wPPH_7FyAMNuvb4DxrX-YniCTEgGiCJjf-WTCeeNIa5vNqpETKhJRNzBOLjHgK7WnmGoVWhJVvRG2T7jF_hgNgeJ7x8QnbwV8xngjkBAzfwwXHrJAgTw838OpxoJ175cyCEMnbLIJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
