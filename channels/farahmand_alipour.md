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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 22:53:04</div>
<hr>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBLBI_814qgol_DQ-CIl1yYSfSaQxp2B1Wh4_IPFEmFgWj5VT2ZvlYgB9pb-ulo1GouS5z2tOfgb9OfNsrEo72Uz-5QdMHBy24nQbSTQMWih68uQAlNetn9-OoPgStEbfTHFcNbAxwHyQjDhm_c7q00qEh2N23igLiJzk6T1eJ8ppq2b6sqSJyXgaMIG4_CQWnN_Up9o5Or7YKfnf0QzqRt-lTdMKVWG162UQws8oCy_JDAK6ndbTkLL6z_PnTkX45uNns93HqbTJtqcf1XxoQj5cfl5zLfRBkViNdqFWpaxr4lMiagnhqhX5G0GklWkwuhTKnUbRg0f396JybuvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_V24fwnlSEn8pBtox3mpxpxImaYlFd8e44Kta2sIesLQWwRF7pDZ-lW_UHBH-F9OuUJXOBB1FfbiCJ1RibqaJ-snqF452VaujAF8rVwShBgO3Pk6yq55d_s2H5xZqJ1BmADKlUdgg7wCMYaL8kKomfWkB4F4aY63FA4JZmD_ZrXB_3XfVCVWmlGHdiiwsZmmIxrZdOLcLTU6DWWVfKm6fl0IAFlw74qL4ai0_-dPjszTWYa0THkpBJL_fHzGRBcshnkDDHwcT6yhQb-_h4SsAVMeeYzTPhMhtUFGHL-48vTp_vJzh-paPiVuic2vTSu7ImpBdUH03OUVD0BtmS7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmdjgjWxEQuckLdTv8N3YkIHT3mZ55uTCEXVEUmtjcfR3S65A0FeSghZc-Ylw45bbMoUqmy-q9SR91SOM5Ov5-vW049M9Lj7UBlVvKcH0KXXOZ3DraVoVEjjyCvNdx9F_UCmfjVONHnp1xhDmMBEyQvqL1y4VOCgA8zJyqel-NHIzFL2J2AAHcp57cvhoh6JOWAuIytaYpljmJUqWRJaDdPo0GfC3_JrIfeASDwpXycpqetSMCnQzC5f32nsLm0PZgj0YuIRJUEKMTn2pcinS_jnXxJxPBFJBs0hLFapJvQqs4iKiKJarxVXzDTCU3nV_LkymwNc6qxHFz3hrnn2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=DDUGI6h6sk2iTF0lDQyqYqpe0w--GDQAXtDqIiXUigsUI51HsfpwgqJadKBOx4kpcghFujV709qBHGgFCMqdw0DEBosAYcQLQoLqRtsFalgxwB6bFbCusaF2Fdp7KHnDLg0rVCFxm_CDPfDA_8oybEulmCHw3l31NbrVF2qx-ESlG-IH8I_DPX-LRb-ziu2wKoTnH2Oc3T8r9ZjZb1segzw34l82cADt3cna_72QDuK3j0i1LqS9s1tUZe73zy3gbiV54wzXh2smBwQjzyjDVh4jCrQ3R77BoKFXG6ZSEVqOGuQ_FrohLX9zlFCcfZvBemur09eTqOIce57TvNSQsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=DDUGI6h6sk2iTF0lDQyqYqpe0w--GDQAXtDqIiXUigsUI51HsfpwgqJadKBOx4kpcghFujV709qBHGgFCMqdw0DEBosAYcQLQoLqRtsFalgxwB6bFbCusaF2Fdp7KHnDLg0rVCFxm_CDPfDA_8oybEulmCHw3l31NbrVF2qx-ESlG-IH8I_DPX-LRb-ziu2wKoTnH2Oc3T8r9ZjZb1segzw34l82cADt3cna_72QDuK3j0i1LqS9s1tUZe73zy3gbiV54wzXh2smBwQjzyjDVh4jCrQ3R77BoKFXG6ZSEVqOGuQ_FrohLX9zlFCcfZvBemur09eTqOIce57TvNSQsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxFz44CZ3kCcIgGOUlCTGUOCPURyLb_cAeSaLvPM2ekdL4k2M37l5i5nh841-GHVldDo1VaB0hj9oNWOCYQ9-jJ1TgUjp9BYC-lLGlLhO2cyx2KBHh8guuCpZ5XuVljXTHBGW5gnbntOK6JHOr71R3wTYvKAufMCk4-8McBJ8VWQkEJZ4eItyPPiOkq7ixntWJl33r84zbsKvPaP0-10gZSbC9JRfjJc4AKIgTJhEAv4gmWuwxchKotejflOBmjiZbL4DkcnRrsYtoqqZjnpsxNPAk-wCdhIa1bYa4FSvo1SkBSdvmT8qvEJvlRJCU6hfh7FsMh5x3ichxPd0G-p4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JX2Em57BlV8AHrCHXvQjzSsDaWeE202zmSRAsTfJuGGzQsv-Jh8ge2zHT2DcmIyIgNLjtjcYMybGx2PhoCZpj3sozzZm_mgvUjOxPzGgihLVSe75kGM6KWfLDcqYDK_BsrdkhA5tJtnBE2xykOk0Rp_drzY3sOFcgnoAiWQsNXRD_DbrNC4y1rOgPYrMakY8FlT2ApJlTfrV7P3sqomo1OLUyErcB6gxvreLz5gedLYyhSzszeXYbKAukjh8Aytr0LRJTUgqev5ZiX8AB3rSUdDo5Jfh98HVtj2ccTs-LOj7G-2_DR1jgqjPwmhI_NFCkeISF_fstFLoSOXSasXSlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=PX3zHDXBqQEXd4oLvAo1UmUEkjo2iqRBfsAKrJidrJsi0y8Hi8xTOWD0cxbXjRgaCww4T7pUvjbhotVekWSPHeX78lQXRvKUKDp-g7fjp1O7IyEKtph-n5-sY-Isra4QVsj5WbCD27oPRWtH-VcKepqijtW0BY7KHeoXmAfDIMciMEox5HfQm_YRMiUhOaaMVhv8Ay7hTMYlGIf4RrHqe8IUWpOSKSWaflnUCPvb_i0Ctj57P6XM92TEXNLx-mZRWb_tD06yS06azx15woW4uMSyxMEUPoa9dgcJ1K8JS_mtBntjFYI65qZU_pWfzs-GcnogMytjxfQFN78op_0Jxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=PX3zHDXBqQEXd4oLvAo1UmUEkjo2iqRBfsAKrJidrJsi0y8Hi8xTOWD0cxbXjRgaCww4T7pUvjbhotVekWSPHeX78lQXRvKUKDp-g7fjp1O7IyEKtph-n5-sY-Isra4QVsj5WbCD27oPRWtH-VcKepqijtW0BY7KHeoXmAfDIMciMEox5HfQm_YRMiUhOaaMVhv8Ay7hTMYlGIf4RrHqe8IUWpOSKSWaflnUCPvb_i0Ctj57P6XM92TEXNLx-mZRWb_tD06yS06azx15woW4uMSyxMEUPoa9dgcJ1K8JS_mtBntjFYI65qZU_pWfzs-GcnogMytjxfQFN78op_0Jxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=SxPnhcOA_Ab1TO9oIDEk7ybUBFSjeyigopKpBXGtZGP0iO8SgPOuL7P6P9KlBTRbBV0GSC9tSsc6n4L1ReckjtsEB3VH_ik3neyPCnfM5LdBZXyAK4mlTEgE6V-UO8esp8On-ybHK5Msdqu5BClcfxtgErM3VgXy0BXE2HXvL6TfcxSYPlRybPF6AWN0gwL1gLbzsBjR5CZPZhlA5FRRUrtYM4YL4wFHPZA-WPtRq5I9Y2SEnYCVNuHdZk5p-Ax7Ff5u5T7WQw5CT2IcU04p7LMmdKavrHh8RTICq9RGpY50WVEtxkmkysx7ZmFPtQYIYyeuF5RvF6fccBrRi4VBlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=SxPnhcOA_Ab1TO9oIDEk7ybUBFSjeyigopKpBXGtZGP0iO8SgPOuL7P6P9KlBTRbBV0GSC9tSsc6n4L1ReckjtsEB3VH_ik3neyPCnfM5LdBZXyAK4mlTEgE6V-UO8esp8On-ybHK5Msdqu5BClcfxtgErM3VgXy0BXE2HXvL6TfcxSYPlRybPF6AWN0gwL1gLbzsBjR5CZPZhlA5FRRUrtYM4YL4wFHPZA-WPtRq5I9Y2SEnYCVNuHdZk5p-Ax7Ff5u5T7WQw5CT2IcU04p7LMmdKavrHh8RTICq9RGpY50WVEtxkmkysx7ZmFPtQYIYyeuF5RvF6fccBrRi4VBlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=f4aCp0NGD5T8tHXyMHIA7c0Ztf9__pBQsgjwb5U1YnbWKT9FG8p1LmUZpLdlrQfoxIQp8TZIj_OYdJAbSNbI0jKLlIzVboaQicmRAkPB1s-hPAwThWxfUr-Q-dxNuOk4-cgOL6cAdT66zKuvbO2LJRpNeWZRVPjYjotnuex9j8sefHjYByChM4JwXFk22M9EC3XJRBahlg8GkIiM2C4VYJbtcyqaW_5llzELVwNvITFlu5kJ5GyqzYk5PhMc5mHv-XWsS2kYxgSfkXQYK7DP29ELpDoVgYBq3WEDliDWSzORSiCpu759OFkdaAvxq0ku9XvNKPlJ01J5hvewOeBn8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=f4aCp0NGD5T8tHXyMHIA7c0Ztf9__pBQsgjwb5U1YnbWKT9FG8p1LmUZpLdlrQfoxIQp8TZIj_OYdJAbSNbI0jKLlIzVboaQicmRAkPB1s-hPAwThWxfUr-Q-dxNuOk4-cgOL6cAdT66zKuvbO2LJRpNeWZRVPjYjotnuex9j8sefHjYByChM4JwXFk22M9EC3XJRBahlg8GkIiM2C4VYJbtcyqaW_5llzELVwNvITFlu5kJ5GyqzYk5PhMc5mHv-XWsS2kYxgSfkXQYK7DP29ELpDoVgYBq3WEDliDWSzORSiCpu759OFkdaAvxq0ku9XvNKPlJ01J5hvewOeBn8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwwhQ_ldICT3cRxJOC9cnEmlZb48JEnIKoph0JojT3KgH-O8p28FTG36Cvr07UgOAhgc9_mFZHzr4ei0ZyZGrhY9cQHi_7RMxCp5g3omnn5u4oFU3FLJCe7vYMtNB73PS3tcuT8RIk772Ow3mPhqKPnNnFifO3HiTw7uauOX_XKGFuI1IG7InrMtof-xF2z_cdpoFbvRKxx16w4nNVLU1B7Vh2kmaJTbqs7p1PFrDC6yxyeYt0kZZFevLf-eokatdnmAE-4qY-IH68ha26oHawX3LVsRHeXX8UlrWFeNnqoExJaiy2C5AWA4OsXMQfpniReeBSU_PDFLKZFT4L-lLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uF-bgGTnmS1Orhyf88CBJNFxheUlj5iGZi-vOPKYWfk1DF0KSi_IlL8qoO_tztJELxNyE3VtAm_1UgBVhLOiDLBYtL-08TwenFMoM2R0fp2iiyVTgCA1XjBtHJIFGDpLz5hyi5n6ruvcstrj4LdmKbNUsn2sY_csSx2KZyP_YYTfWwShvugChMEXt9F3o0DKLD9jYgk2vj-IsXSZ4DXgJhICu5sy0mIMWLh97pmGZMaukT9q2VKO21TbK9Lq1fV1WXDTrMF9lV9LnOCMroyoakVKNsyMOq_bNPSNFhyEn5FWDWJbrI4EIuHrPSWws2RvbH0p2H9E8ZLKeS66lD402w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSff7t8ACHc96vKiMwUCL9JW-CshwMOjQPWMTpUxXMnjItKktpQ8VS9baK59qQ4xT1huavybta8psXlG2q4-2tkIfANrboUISw0QwPvEGoE4Nty2hGQAmTIChxcYVX4VmPXuNzCChi9fWbNPZBUtrUUuCLdKAnhQNwd5DFxnBLng1eK0KSaDlXNunlOwfE5h3-BLqHpZew5ZYDmbQbbUnGQbRRV9EmpUWl8uS55eI-9_rEo8W8GTS1dYL3GRGU4GWlQtxrmmve8ATkgEwkLC4Ke-xopzSiVqDGxUfAOgTWUsMEMHJbH6bBa4YysGBCucq0QyOech6f4fxHaKcjJSPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hVA0ZzOUVcIvYWXZPZ5h7eWQ2B7U2Vo99iygSHuN0Q77-lXV-0w3teaco_EqH_PkFZnpFVBIadowMQWag_dh3zVc8H-n45Xw7pBbZ1mHxEgbf5rZHpuO4HMpwfhll6KdZPXAFch7Jbi7oZ1FNI9s69sR_AC-emDjTlSjlCalq5PGx1YQyZ4p8ST_pa0iqPWS5RxmY_AYUBygluwCyf_qltOfRWy81Lef7IWtqorPcLG_ythiaKwFC8LdYFB0u8KcNcWcl4YwCzW8WUy2EcQXGpfAI5UaEnVvSU-OhuFMj_fGM5scYKxXoUHgWr61I74gLyoqIzk89dUEGych85nbYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qknrC7mLksBBdTnTuwUOIkYayIGk9Nkx9iF3GIMi8x207GNsWiz1k3hVXKm4rnzUGKYs9zV9qRwYHNULh0fLF1SCqs-RPAUoSTfk_sUHYESVjMGrArSgO-BlGNJ-8OeK061tMEM8tX2W_qLaeSkdqZEIuELoIeYWNc2zPIYRJU-LZWMYwFNyfxHx7ZTLqVKboVyYGIqARaJ9m8AA19qQGMBG1999BFDaK75gb7zDlaV52niRu1Hm81b088ywfMNp740zkx8TzqXp757qmunCHkcjTF3C69judb-2VA_GK3mZCC39dgdD0izwQq6noQ2_nV2sSNX2SSbItfT2Wsg--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHLfuIK0_jaLUUcwKuufdyRkMMbuR1R7VLmNbMIcv7Av9xpiokEo_iC4NRNCtNRMqKSgrFbjHii2edyYbDfbyPBy7_xL6bkZtPSMcELNZFnD4B5O1bvM62CiiY_Rvi6g785MwUl5K8iBvH8HpIRXJWf55E82zhGTfii0oE1aYcxTMA2NnQejFcqeAi99HQ3yx5W5TXuCObl28TaDTAvfXZAz22hQy3N6XXap6gesRsyW60SFkT0Rq511g_l-3hqJRnl3ZGFRtd8rgjy7GU3soxHXAbkd1ex7xKfcSEP5RPxBSXRh_RlrAug-43xUDem5wemNitk_7j4XMXYjjcv2xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WPIk-GNaZWqVNXWen8xZoB6wOOgtW5npGo6zc3kD4fFO43R1ty5ZOh4BL-PLaStUGSqJUPFDAGIgc3bYSeCLZrpfxOKL-nm7fvo1yy_i3sIQ7cJSlXZQIcF6mElsqhyYTSl5gWpq40acEP3zhjNzmBumUE05Fuk_q9H8KA-gxfJb-xAF5DXFUiDkPZrk1AiAdCKSs2iS9fdxCMOi7PGjnv5l7NvPyyhva3s81AXoY5hTR4lwMN2WwxcTFC1_JKEDqzSFhjd_SL5cij5cMrr8Dk-_vwe3hSRQo0f98dUWnLmM9bvFwgef_Ouzw893lgUGqM8se-FbygD5CIGufh_VWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJFTy9lfbqVVkLH13EOWPLnCIyQlNZjbpCOikQv3JIaEdieqXMrYP0FzwWIbRB1t6QfPI-b4_eJpRg1pC6pXwFmXHuydrFu1TaY_8qStbdXi0PR95Cn78rHEpuuEIFOyJJX-PvoW6YqMC9cPE9Ou9kWQHjUHFxlTTGoDbfn6ZJ8MPQS9LLzhFtrT_RvU6leo744rNtBWbzxryEyE80AtqqLKNwe2hIwm0TlLStDSZhLQ2HdfTf6u17T2SX_w5os_lTkQbgoFfk_hfi9Mouiq4FXo4j0ShzZWR86BQV_e36P0VNjbAMAMxn_UUE1hAkpY8op3RmcNWmnvS4i35gFR9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PT0w9rG7mg6vbn7JjJ4w32Y6oBratX_v5lIbZ8firJLVfOjQZu3uaHLBDmSGvMbuluDl77W9NOn0XCuLmA5YTYIJIcWGCsZYQfmZLSkCST9Yqu8rROeDnaP4IBF7Uv4hUq-_umPyas2g1Ti5voK66PEceMqRXvv8tpmUXDP-5Yra2JE5n1k83ZVqTfMCcX9f1daVebBeBZVxrFiaN0L38Pcy4yC2qBuS2LRra9ZdiaviZqv7Lp86lUi5Jv7xeoPl8G6T6e9dOy39zuC30qWerfrdmvqpEifu1xb4oglEJiC4hrtPzEtBPuQh75TkwgP0OR-CMlEga3c-J3OzJ5-Zcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_LRFOki-LX6-dnMKbtlP9igpfmL-GVS0OZBLz4k_SM2Zi39xMQPnj7WBZvbah9q971avwxcqi8m1p9JmoNaeIrIYNoBsyyZSaTKMtLHqA9lQBRcU27UU-qQiNAjP9JciKIQRQa0NwmsaBZSrkonyD1-WiOgSqvkGbhQ9SdOWup1_bHGJC7MzMixNKK4yWef4cT40GEFQu-OIZMdSYDf5V8DClibVEckS-cKoZMZJz8NRzU_heDe0UtJ_8bcs6NEAZ-ntVSRUB_AQJciREzYch4GG1XlScJjvQldP-gjQop8gTxT6la5-FJqnfl_De-OZh2sni2oE_kijRsYBxkOIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sS5pnmghps32kM8uDomg7aeMfBFUzES8iGE20rZ247dM2SeQgzaexh8gXF_hZUZMekXqjdt32XFyaZlwRpiJJHP1LGIlSyuf5NTgVPsNywX4PC-8yi6vfVUfwemJk_WyPozd1LmojPjNrHj1ReSJt5yjEkb-Ivei6By6AlIyYDOGugdsvitzQeZHH7PAW1NiGpA4Oa6T5ZgKlLFuQYAZQLlI1TTXSDxQtr8X88J-HMdAzOLXJM5aVArlau_v12B9IPkj_Oqd4e3ttop2Y26p2UXWYcv3msL26EZkEQrZ0EMre6Llnl01UXF2VNBfObZpdRZpwkxtknJpvUkxjMmzmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj0plY68JyFyIZ3wYkl_Bqs-huTEPe_WiDwh-YO-oE3VzbmKwDBSx9vk0k3xuwvauEh9FdbTNXCT_LMz2WwMUKtwwGTBLdUshmKHqGP2MpKkzJ8GOlOI5HnQV0J6o2lS3b9C9SRqoVto5viHFQG0m4GYWIRhD46hXMZ-Ywg2SJraopXev6A-Kec-cynyqfeT7w_H509Vj6lKFZQgsVhtVawEc_7VVBZ2W6TYjYAwiwIZBuqUKe-eQZYjN_RuThal2yDW1ecQ0hUsLwp5EckXA1NN6Yc_vhT_iNkpTpYUimFk0D5voixJv00K0nV0VXoyOjUbccogJU5lvn4vS4qdVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdajGkNNqzMEgIrPwJpR4IrOqCiVi1DBMVeK7GmYc-_IQZhbLSXYwyuDh5HN1Qw2K5cvORbyL_p7c5ORjemZqdmdqU-B6yUVBw3iqdLrgEJOwncjyQ5Mgl1428dlrW9gkjNdzgfO801IOR3sFJMFXPYjkK4dEzkntclF1mCuSnMhGOGtXddNqw71CxsQY57OizJ4NQEO3xOER4VqjZSvd-gkQ8dDwcZV1qg7VBKpgneVOg-N_a_HLUlKR7PBVGHn96RjgJwzafSL-09I9qFHwaJT0lveseFPrmF8SRNDvaYUp_rQZN4xcy5mdMKM8lRCkmehDfC-sKBjMFfzbLIGHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0Rkoocerqu7Dh--q2gXtN77FInBFt7pg4ofOyjL4tzWuskf5_9cO6uOO-NjYC_TmsY3T9PswbpIMTBhVSYo2lVgaVTYZSSSuXgoam-m2Ab7P9wet3q7bnJBnS-F5gLxe6OMXkqzMIksGvvU85BM4XRHGk6om5VjDukU2aC8ZcPa3A9dyGc0itvZcjNYlw8sQJxeqBPYWoXfjdvl1uNHbKjOPUVeqEQMWdmeLGeWr_x4amH7Emwnll2E8gZsat6pj_OkM1COFK_AVqVAqAsp_THTPItrBpS8FCeMF5jSt0NKKCqEl7zmGiDXtQVQ5M07xP30e1oTlCSIHpCk9FL-Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHMsbdkZN9QojKEeGXSSUTDpGh3VqPuHaRzAYvvoGSak4MF3k6YfMh-L7fUh5aDPQg4E-GqECvWBKFjNrp82CBRraBYpM_04No_2xttNlAHBOinsMwhtKQ6R3-naUJNKp0N_XZvZgnGhiDsh5CdjZ5ju0JcGEh3r1NBUL4OeX2jowwSubBXZ_n8qRxnsY8R7wdeHbmxIBXrYHIkz-1itwsYtw7hdZ757PA5FY6irPlNjw5p-STVNxCYQ3oESTD2eyslrXeC6vtesTIaqOa9Det1EqU5Di1WYU9d5YkDM-fYcT-Q74mGLBry3AOU_VBxVQsC-UiexvUFdG4h2xNgIwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=tGmar6pkGxSGgDxDZXWhUu5b5YCTMreLOyeLJP9WZHb8kql7dvv60WL_B7iFiSjlia8nvFCFgOfkzwyVIcSS6LXYeICHtElRXPYdAqEFtYOAia7dT2xFaKpR8Cl_I26CZ9iBkeH4YXLmKoNDySI74yhDKK7SX4BltzNKNPxFULd9iMaG1ui5Zg_QyxVk0YJFgHqDRovBewny92YkF4_ppL5DYLmFsV7aHJsttjq7eOI1_yB-z4dj6JIQDankFh24uWJylbLP2Icd4ptU5Dicg06mVNrF5udn5TqL0-hn_cO7DzyoKJuIVCJH2sVjNm3VGrvradIq9zm9Rz99RT-mIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=tGmar6pkGxSGgDxDZXWhUu5b5YCTMreLOyeLJP9WZHb8kql7dvv60WL_B7iFiSjlia8nvFCFgOfkzwyVIcSS6LXYeICHtElRXPYdAqEFtYOAia7dT2xFaKpR8Cl_I26CZ9iBkeH4YXLmKoNDySI74yhDKK7SX4BltzNKNPxFULd9iMaG1ui5Zg_QyxVk0YJFgHqDRovBewny92YkF4_ppL5DYLmFsV7aHJsttjq7eOI1_yB-z4dj6JIQDankFh24uWJylbLP2Icd4ptU5Dicg06mVNrF5udn5TqL0-hn_cO7DzyoKJuIVCJH2sVjNm3VGrvradIq9zm9Rz99RT-mIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALOlsBvLEcnPpggkwq9B6hni-C9V1_2M1Cw75PxKy5feWzGQOl58mAKM-cQxuBH5Ecf5Xn6fz_p--Anbm3l2nT3N_7L-60Ar1XF_-VXPNUSEA2fC5OFhcr3hWUAMgYY18kz0VAX4wV_z0Fnjyxfcy7AMN5ObtY25ctGSDpce8L5I4EpPxc33fyiM2PF1jVaRrGfTtKerPvbuauCVgBj5X9z_YrTICi3EhRfU1Y5_QZrWJRxEVnHg8HAcFwj5LLpLQXtmqFCJy5yVb7O4CqTz3n6USzfaJ-8V45LkbtW49Gu__if_GK5t0Yawzq084xGMrm2zkJt-w4oZHQkueoYWfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=HGo3MSotYkik40FiTxfR7I-LivsZ3Az02xGmh7XmKHcnByBuUBgm4-CupLEtOD_Jh2jGSMfVSRKwziI84Njpo6gtIQJTXdRsnAWJsS01ivA7E_MRkxIYxwdM9iedIVEuomkqGpuHe2nUS42J7l98ct64JXxal_eQF8gPr6pq4PkeAfxpVrqjRoIz72WWn7DTURG3fUzuTZJAOkS36c1-23hX_5jlngqmEh8gVpjojqbjsexJ0WnwjuLNftLyJkgfEgam47GhqnsgZgpN0LbkfMaR2tWsX2gjTV317Ym4ZqUcx6EOW4mB6_D9ZUuqOu_jn1IPQnbN7jrXSAvpheEbvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=HGo3MSotYkik40FiTxfR7I-LivsZ3Az02xGmh7XmKHcnByBuUBgm4-CupLEtOD_Jh2jGSMfVSRKwziI84Njpo6gtIQJTXdRsnAWJsS01ivA7E_MRkxIYxwdM9iedIVEuomkqGpuHe2nUS42J7l98ct64JXxal_eQF8gPr6pq4PkeAfxpVrqjRoIz72WWn7DTURG3fUzuTZJAOkS36c1-23hX_5jlngqmEh8gVpjojqbjsexJ0WnwjuLNftLyJkgfEgam47GhqnsgZgpN0LbkfMaR2tWsX2gjTV317Ym4ZqUcx6EOW4mB6_D9ZUuqOu_jn1IPQnbN7jrXSAvpheEbvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=npJrCaA1JCK-16JWYSp7F6zyueb5SINQV-dI2mZYool-t3HSD1MD0ZU27EnF3q4opWD7TnK53RrkU2As-EFY7aTX4JgliaJfEvzuB6xOtzI8j97m_EA2tIUKE3p_DiKLpFnLhdhd-QZBVgpYnEKm0yA_Al4uGr_UPWrdhiYNqRTU1h2CsvSl6AM2eLc2OJXLy4NIC0QR-9y0J_X0QRatQUs10kH2HM1bFNrJXs_FmyOC_b4qN6EKyCZuu7F9aloJ8YnNV4hPrX0G9be8TYuc5tCemfEsaiQrm4UdwIOBgnHS_8MrDKlk5r0lupOMHeJz5ZdUsEbP2RRgduuK_pJpqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=npJrCaA1JCK-16JWYSp7F6zyueb5SINQV-dI2mZYool-t3HSD1MD0ZU27EnF3q4opWD7TnK53RrkU2As-EFY7aTX4JgliaJfEvzuB6xOtzI8j97m_EA2tIUKE3p_DiKLpFnLhdhd-QZBVgpYnEKm0yA_Al4uGr_UPWrdhiYNqRTU1h2CsvSl6AM2eLc2OJXLy4NIC0QR-9y0J_X0QRatQUs10kH2HM1bFNrJXs_FmyOC_b4qN6EKyCZuu7F9aloJ8YnNV4hPrX0G9be8TYuc5tCemfEsaiQrm4UdwIOBgnHS_8MrDKlk5r0lupOMHeJz5ZdUsEbP2RRgduuK_pJpqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEeU3pEzCYZ_CUrKZFlhezPhBEreorICsMPAmp68oTSZZlg6d8q7tykw59COkf6l0OjclW5QThkt8j6zQH3qnulW-t9ryrfngF-g-Pd4Pdy2wrq5vl-Vhc2AYCZLGMWlOgmbTvzbcykdz6PU4llCCZ1TbDMemAj0HAMgwOiQG2ohR71nLavTOaRnw6PbdUNiggYodBx6F-m0ma1g2YBa5VbwPUlEO0UT0Ao1-MLlNvpT5haAvop_ydN8rOY2TJ_1U7ksgjnG_9PyVCgoRHbhyfyUMQz3hfy6FLm8IjHil8yig4qYV1Pv7pXyeMR91-5zQxdL1L4nBbaD2O6eowQQOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=cbHpBzNQdyTpuGyNQc1p01AEJ_jSL_fPklMujdYKHIqxahSXTXlJHczmWkKmTk4TIyoyTfl15mShAXwDS5sW3Ql9POqjGAo4JIThHuLfPzKI2fruv34f8eGBBWSdJUP6D6lAMw0N7qCib618oB1LXPg3FS-el5osbMH4wZdETwNrBGtHrNxS0fOUhBUdSKN31sTDOXdzjbeoBLdahqn_lz6PK35qhRhPnePYGWQVg-9AXNJkTyoK2y4xfDUEkU8KOgb_VuDDU__a52IHzmApxk9HMmQLRm2GsLqM3VJ7oCZMwYJCVwGg85Jc0-M-EPpUXqj6A47lvveidP_noWu-bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=cbHpBzNQdyTpuGyNQc1p01AEJ_jSL_fPklMujdYKHIqxahSXTXlJHczmWkKmTk4TIyoyTfl15mShAXwDS5sW3Ql9POqjGAo4JIThHuLfPzKI2fruv34f8eGBBWSdJUP6D6lAMw0N7qCib618oB1LXPg3FS-el5osbMH4wZdETwNrBGtHrNxS0fOUhBUdSKN31sTDOXdzjbeoBLdahqn_lz6PK35qhRhPnePYGWQVg-9AXNJkTyoK2y4xfDUEkU8KOgb_VuDDU__a52IHzmApxk9HMmQLRm2GsLqM3VJ7oCZMwYJCVwGg85Jc0-M-EPpUXqj6A47lvveidP_noWu-bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPLKkZI28HFLI9hKCTB3OFT7qwblHBe9K2e5pXV08PbNG5iE1DyRhQQAo8Sbpk9-4U74nhz7GDBCRdTTdzv1td1cNgt4XPIyMcCmQ0PnkNii5lkYhx0VlP1Gx0vvdenq-QJ8lQs-SC5i2afYwpvusZyooq3HneV2gCyQqKDuBwmYMERdN-ez_doNwgEbJH0edctRBYDYuObHd27l7xFbSy8VaBzOq5E7cBuAaMtfVzFElVuLHxWKaWPby3yMjq71nCgqfPr3V0k0dnTj8rIm3K6uyuI-rOs4pNogceyqcaY2VsN8XKddrLdxdMc3hkHCYYnnPI7ZT83vbOTKKtbbyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jdrss6aXKWaykilO7FXbvhsDqyzGH9ka8RhilXSuLWU8Ln1A5ZG3U2o46DXGDMKJgwS7X4todxOSdAIOtcTTZv06hvcnoCY5O_OuLqzaytFrEU-2-qV3LBD7Yk8pVKsP0gXocXJv3K7U5hgiLtbhY-Y2d086A0Tni4l4QkbDsnxiIOlVi_KmhCZntClGvJSGPwJzA0MIkKxaNJ_V5hE_rt9QxnbOye_TtS3ktohJUQD7hcXslxU5Adl01nX5BHMCw9K13He30mFdZ3hOz_AF-h2U2oaKQc1MYYJlwY2r4IE5BOu7oskvFZO8zz6Nir2FCo95uuAPf0UB9nR6wAKatg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5STR_yfKpmsduKV9oddIkmWppcFpzMlxrRipv8fGRwMjntwAaY1cYaxpb1za8ccfen-mLIx6B6L5W3ZQtoY5H9uQ3uBXvzpHyqlqdU4SymwgwzejZhWdWZq8-u_D98wUA46sstfUSgJoh4o3uN0BvBqnReyBSTKgIyP1YfXTndrPySjpHovaGQA7T5nviIAIFCcjfUnCQwu3lUqP7A95efSeDud6xfw7MsNQ9BU4pIab8r-27ZLNINkMJ6qGflbPNzQ8HuYocqvdVV5IEAjcRa2G2hjdnU05EEEpqi1DfGWQixp_2r0cmAaC9K7ysfYhe8X5-cAxoXP24_EWBLFfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEmlh-Cakom7Ag0dE881liXvLQkXGH83AFLW5AXb9t2JhCLQUaAuh0prw_B-seBpgga12ppOPtT5XU9AS4unZVapl2hTsQ5GBCEIwKs88yyR8J4RW-A9mXs_PTg4SnIyBN9mt98nXqe1hK47B6XLcmqkfs_jNZpahJAihWJ8wQVv_A1gN8muEh8or3_WejN1aMC3S_NzO-3QlrN6T1D8VEYdrLtbyH1--zOaRguBm081LDRLW6pjrwnMOT29w41NYaXtE7p6NcA0GX8OUMUW4GAvG_VlLfF2ELHabYrNCPGMWOnLT_JUXEo2Wpp94fdr-V--9jS-BWOlkavtr5Kgrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=WvcouiiSktMah9s73ga2-7pqiX6G4mbysWDQrHOpiCpXl7vcCWR-XUMHgc35NgFNNSpaARuX2dGQuK6oVHl1OZbnT3-arw9WYTyQTvvImBJscEd83fR8hSKPK3j2mHcZ7IiAEQUvGYAFKNi-3jCEahdDey6K8RWwbXrjMWa0BLM_FPMoQmjGTnadPdhlAixF_MVVyUK5NvuGucUNbIySD9_XzEElw7gJR3m5xrsyt5X965yHPmp27WCBjoHg-A4ja-A8R5vBRponLcKXu62aAJJYxgRVxL8hFcI2EMuxFx0LmEpF1m3wv7FX-27xgqWohkYD5OReBRC_8tC89uwTFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=WvcouiiSktMah9s73ga2-7pqiX6G4mbysWDQrHOpiCpXl7vcCWR-XUMHgc35NgFNNSpaARuX2dGQuK6oVHl1OZbnT3-arw9WYTyQTvvImBJscEd83fR8hSKPK3j2mHcZ7IiAEQUvGYAFKNi-3jCEahdDey6K8RWwbXrjMWa0BLM_FPMoQmjGTnadPdhlAixF_MVVyUK5NvuGucUNbIySD9_XzEElw7gJR3m5xrsyt5X965yHPmp27WCBjoHg-A4ja-A8R5vBRponLcKXu62aAJJYxgRVxL8hFcI2EMuxFx0LmEpF1m3wv7FX-27xgqWohkYD5OReBRC_8tC89uwTFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=ECtGteomGX-D66R_XIz4ccf5t_QCp-PkePGCQK1F0QoTwrFTwDngL7lTWwZUNvnLcV6XkP-Tt_2DOQaw03YuccreCvFBEGx1OYn09XXqKjDDGmRNYITle71YF3-KSRRWFzpIVe0p3WJ1hsTqHUMhwaXGGjRJfXqxqxOS1FhWPAKBsWcaIpjEdc4Ykhn0vdbuEJm-l2r9OHk2Fu7WXjbrxaY_j6FXMOKugm0lpUVj1cPj2fDZgr84fXNI0qiWy_2TdLJJsTZqj33UFk2TVJYsMsSxgYCgamcGQMkFsizC_ZEw_dw5A3PYCivsnvuqn-k2wVUVGbIJHNOcziV5ABOvcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=ECtGteomGX-D66R_XIz4ccf5t_QCp-PkePGCQK1F0QoTwrFTwDngL7lTWwZUNvnLcV6XkP-Tt_2DOQaw03YuccreCvFBEGx1OYn09XXqKjDDGmRNYITle71YF3-KSRRWFzpIVe0p3WJ1hsTqHUMhwaXGGjRJfXqxqxOS1FhWPAKBsWcaIpjEdc4Ykhn0vdbuEJm-l2r9OHk2Fu7WXjbrxaY_j6FXMOKugm0lpUVj1cPj2fDZgr84fXNI0qiWy_2TdLJJsTZqj33UFk2TVJYsMsSxgYCgamcGQMkFsizC_ZEw_dw5A3PYCivsnvuqn-k2wVUVGbIJHNOcziV5ABOvcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=sPMtaoq-pQ1d-xB3CCnl-0mqFaxoxwccAdAto31QJpJJfL16MdpswkVXAWVu3g7bQk25VwkHpTj5fEhDiZ2yHKNLrYpcLVxfQ-RBDdDfS3SdaCChWAtBz8qWvBaM5sLXrRIP4ccmfOPZUkBsesRkl9ZV1ch6gqVmAgRu6RRq-Nmj90rGS_sTCu1N3gYGBuE4U83Jy-qxRGyQucrCRn0wZKzDUkLOxKVhZpG9plFo0F-cgYJJ31_VLn6CRx1upAmjKb3ogQUathdYOQHfsxdhpBlzgh9gvlRcjv6at66wBpsAa_TrEQq4j6Gt4FBYGv0pDPSAJxYB6TJ__6ejVQcGqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=sPMtaoq-pQ1d-xB3CCnl-0mqFaxoxwccAdAto31QJpJJfL16MdpswkVXAWVu3g7bQk25VwkHpTj5fEhDiZ2yHKNLrYpcLVxfQ-RBDdDfS3SdaCChWAtBz8qWvBaM5sLXrRIP4ccmfOPZUkBsesRkl9ZV1ch6gqVmAgRu6RRq-Nmj90rGS_sTCu1N3gYGBuE4U83Jy-qxRGyQucrCRn0wZKzDUkLOxKVhZpG9plFo0F-cgYJJ31_VLn6CRx1upAmjKb3ogQUathdYOQHfsxdhpBlzgh9gvlRcjv6at66wBpsAa_TrEQq4j6Gt4FBYGv0pDPSAJxYB6TJ__6ejVQcGqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=czVGmqdg079AAdXjAgxaEAEJgfoK4oB9TUAgmfYdds1b5sH5UGz1AUEiwZrApm5ik2Ibd9ZHcKxUu6f5Vcy0Lbbg5b4e2KDmzviJBpZvJ8tgqPek4_nGfDnJ3aO3b2SsK-schw2DPoBfToMoo-efmfPnJfccJDU5Zog1jHBp8uygMRD25e8EC3lyLs-tsYA09aKmQQt6p4qZT9YYgjLwHaOY-OSKd543DS1r4eQSf4UVpE3w_MWdM6pP_HB7Tm3NqWGtDKYegIOy0WuvhqtYVZ1wv2JsHxxMjkk48sQ6GIqH1Dw9LFPqIxQbtfTVEAQKk9HeCb_lvANFMLFk8KMvup2wd3ySMlzUnYnSs5v3GHIgp3bGha_rzDpCAdK1Jj9geKl3Fn0LfpVeUdH5_qLv21QxrROrPJ3c9IGDSqmj-2Ut2G9C9FLuHE618j88Cf6l4Jeut9KQFWzbKClNYQBSDLXY0frzEC4tNDSOwW0nu_0er0tR3c9C_mHMHS2oOYWCaT5EdPcH1k77QtmV3n2p_0EwVDKTz1lbAKJKDwBqk5aAaK5x83oxYrs8FRa7Spk9dD3_1BCI9H1Ke4fEiE7_Y4c9XRXThUy64LqBbFcqeKayjj2xCvCg7DFpluAopy92ecYtDhLaheM6nImKXm6vpApJB3cb1xqwmV2Ir-nZM7s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=czVGmqdg079AAdXjAgxaEAEJgfoK4oB9TUAgmfYdds1b5sH5UGz1AUEiwZrApm5ik2Ibd9ZHcKxUu6f5Vcy0Lbbg5b4e2KDmzviJBpZvJ8tgqPek4_nGfDnJ3aO3b2SsK-schw2DPoBfToMoo-efmfPnJfccJDU5Zog1jHBp8uygMRD25e8EC3lyLs-tsYA09aKmQQt6p4qZT9YYgjLwHaOY-OSKd543DS1r4eQSf4UVpE3w_MWdM6pP_HB7Tm3NqWGtDKYegIOy0WuvhqtYVZ1wv2JsHxxMjkk48sQ6GIqH1Dw9LFPqIxQbtfTVEAQKk9HeCb_lvANFMLFk8KMvup2wd3ySMlzUnYnSs5v3GHIgp3bGha_rzDpCAdK1Jj9geKl3Fn0LfpVeUdH5_qLv21QxrROrPJ3c9IGDSqmj-2Ut2G9C9FLuHE618j88Cf6l4Jeut9KQFWzbKClNYQBSDLXY0frzEC4tNDSOwW0nu_0er0tR3c9C_mHMHS2oOYWCaT5EdPcH1k77QtmV3n2p_0EwVDKTz1lbAKJKDwBqk5aAaK5x83oxYrs8FRa7Spk9dD3_1BCI9H1Ke4fEiE7_Y4c9XRXThUy64LqBbFcqeKayjj2xCvCg7DFpluAopy92ecYtDhLaheM6nImKXm6vpApJB3cb1xqwmV2Ir-nZM7s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=uDn5rTHhzP0nGnOxjgTGMVFGgKASVJXzMTJrXZaV5aCICxDvK5Vs_lm7tvYguZf4s6x4mT00RpVS1mCPO5xlVedz62VsQLRFdibxBGeQbI6etIDNiqLK-ObHXOtogFy3ISdqmyKJBJtI03sc5FdR3Eltlqu8mCLU41Weh2ldhHxIE2F_Yt3Yc5-tY4kQrlLVK_QHcK7R2D6DfuDvbMqdR0-6vYvhvAHOlMZqtxIb-NzuneXoZkfUQssofoaTawAuDs6o9yhUw9VRTC-wQhWzp6oYUe8HOzq6oNerUo6p7AK9JJN0oy9BdRLJ94U5o8e94-q6kkrQY_dqbd46l8pUnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=uDn5rTHhzP0nGnOxjgTGMVFGgKASVJXzMTJrXZaV5aCICxDvK5Vs_lm7tvYguZf4s6x4mT00RpVS1mCPO5xlVedz62VsQLRFdibxBGeQbI6etIDNiqLK-ObHXOtogFy3ISdqmyKJBJtI03sc5FdR3Eltlqu8mCLU41Weh2ldhHxIE2F_Yt3Yc5-tY4kQrlLVK_QHcK7R2D6DfuDvbMqdR0-6vYvhvAHOlMZqtxIb-NzuneXoZkfUQssofoaTawAuDs6o9yhUw9VRTC-wQhWzp6oYUe8HOzq6oNerUo6p7AK9JJN0oy9BdRLJ94U5o8e94-q6kkrQY_dqbd46l8pUnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=T2bWujP9dM4N1AtSlZvyfcWJc5d0RAMnKffOJOkmVXFCIaGlsPy4JPo0BfgaIDDXygRpyeOqlv9Y4zwe4P_ItzeqmScI938dOFMgByU82VhgO__dMcFpJxplWBPj9cvVLeOEPxA7IFx6aitw06mP1gWUmhyMl9q6xmMsF8Xypfgc-IJsdN0ArtS7KThppW4Tm0TMdPqcrdXreIEWh6KllSa0ptVUMCTOjBMz7zU1_qlKfER-8XL6xTiuRv_9SJdLL7HUhpgR34N4qrIVwjNMohAZTg5VukpvUnfcJUvPE-Fle6is0PUVSKPPT4ZATSGNm2qbUfE5OZW_s4mgGxFQMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=T2bWujP9dM4N1AtSlZvyfcWJc5d0RAMnKffOJOkmVXFCIaGlsPy4JPo0BfgaIDDXygRpyeOqlv9Y4zwe4P_ItzeqmScI938dOFMgByU82VhgO__dMcFpJxplWBPj9cvVLeOEPxA7IFx6aitw06mP1gWUmhyMl9q6xmMsF8Xypfgc-IJsdN0ArtS7KThppW4Tm0TMdPqcrdXreIEWh6KllSa0ptVUMCTOjBMz7zU1_qlKfER-8XL6xTiuRv_9SJdLL7HUhpgR34N4qrIVwjNMohAZTg5VukpvUnfcJUvPE-Fle6is0PUVSKPPT4ZATSGNm2qbUfE5OZW_s4mgGxFQMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFk0csz5uRk4F1YraODURFClT0pAg6axTOWfRQ6ICyZwBdgdEKG12cyHmOOebZJrkw2pEVZ-dzFCR4S6WZ5YITgv74b-J5G6oo9j3XisQZnvpswQY2Fepf4wvjiqL0dAnHRdCV6ESE-_1azD5FDWMFXE9Ra5v-QzxeqJBiGhlmM1-EQRi0KwEq4liAn8BbDPCQBJnG-Qq-NBcFSKOGJpzrQ2bJFKElYpZ0Hs6Q9zGfv9TF_ZCiK8xX3ckVvLyVdnh5sjbCu2LXeR0XaCGOwXcivt7R9TogNpPaxAVur0YZPhtYqrzy-xAW-XCpAc9OaDjgyg5LPGqJiwmZDSpjd9ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=NoBqsFCfgM2S84teaH13zdXS-Gtwf_1rbb19prz-FPjw4zekno6xSbsFDYmLnjTYNX08WM6BduFLtFx-LwyR7moVYj2dL9To4isGtt2EPhhvDGPTX4FOJulvJ9t6Ee8cbh1sfoeySc02Hm3t-7hVvhAqGvGsWk9oFVEHckdn52bZOYz9uzeA0Qt8wwZY4wl5wa8bnY_Xx_1zwd3CszZsaIm0tZ5oFU024L4cHu9g7UYKNW3rbRcPiZXCF8ftc6NOVDCtjWvyug5ksm9st64uSNWMcEsnuG2JRu5s1VQgjIB2pMCEdGhGGKrfksO-mm9h3jmH9bQKX9scGsqOxTaKHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=NoBqsFCfgM2S84teaH13zdXS-Gtwf_1rbb19prz-FPjw4zekno6xSbsFDYmLnjTYNX08WM6BduFLtFx-LwyR7moVYj2dL9To4isGtt2EPhhvDGPTX4FOJulvJ9t6Ee8cbh1sfoeySc02Hm3t-7hVvhAqGvGsWk9oFVEHckdn52bZOYz9uzeA0Qt8wwZY4wl5wa8bnY_Xx_1zwd3CszZsaIm0tZ5oFU024L4cHu9g7UYKNW3rbRcPiZXCF8ftc6NOVDCtjWvyug5ksm9st64uSNWMcEsnuG2JRu5s1VQgjIB2pMCEdGhGGKrfksO-mm9h3jmH9bQKX9scGsqOxTaKHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHPMm3zlUF4AZEFmwQHoHbn_650IsclUp-iJQPRv0touOQCjQYyKpRy9J24Z2Vf3yMg8wlDnoAJA1GkVGXxgVrh29wLDvPQvMIJvC6VUYpXD9v7kfp2AnltTr9TfEG0Shp1ZRqp9NykIJbeM42BEWFyrHir2WO-GpsF4wAxI1vgRfjE5EyPHdjm4FsFTXcfrWpOKyazQPL3qKAatZ4STbkfRHUg9JfG9pyiw6fPeluZOPESsPceIp0Pu8QrqR6WzctkfmyqGcNCaauhwneFEwGPCd7T_KVWdqO7-hTgZdyNI5PrWCf0_5RzdKgKNhU0RVrdWrVdGzfKEVSa2Kldy5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ly0LO7868mhfyJV6Y3UDK7zPaPYx9MG3geWS9mOiLxjY6OjWipHTyAUcDQkRwbfpFhYhPkiB_0AayeOFJjUtx82zzqWAWZX53zU83g63eP8npfYr9p7I17jvsarTBsi9CJ7y47LnhYnxwvBMXmkdg8hgElOLUWvtfyJSk4Z386xeHHaIpv10KLUTBc8VxsuzO6PSAvcP9qtJ3hYnObrAeTlcdab6X07vLkoGAv8Ing7eMnpuoWQvv-qSx9fJDa3uJeUKhxTi2ACwNxmI5yhqRhEoohGfWNXz0BFn7MDTOH6x93qUH5EsIbqZoOWCLDtHqLgxxbMOYn5LO0TpzM46ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=ttcg-3M8RIpWS_zwQHEotm7bnDSYPD8ai01aRdh8pJE90r7eUzSlplzgtXr4aO9UoZ4TFU1x-Ul2XKWtIDSFTuZoOXb7FN7sET6zC8Z6Oku8JIN6x_RRRESrrKwJ2y9OkSIrQD9C_1LqwCR5jyA0u1URBkgA1akx-gQkj86PEfe7RlGO2MreAGZkVOQTSWSOFClYa3lFeQTEn_xoCq0GL8lSRKpIxA7p94T1yUVHphNyLJcsGhkVGxi33jVEFWNJ_qTuC3CjPp3RwnFTZXCdYuFNmC1R1JXqjIp6lPxVndFX1q0Vrq4QKHql1qhWXRd-v3YAc5SbzI51t3ymPbzjrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=ttcg-3M8RIpWS_zwQHEotm7bnDSYPD8ai01aRdh8pJE90r7eUzSlplzgtXr4aO9UoZ4TFU1x-Ul2XKWtIDSFTuZoOXb7FN7sET6zC8Z6Oku8JIN6x_RRRESrrKwJ2y9OkSIrQD9C_1LqwCR5jyA0u1URBkgA1akx-gQkj86PEfe7RlGO2MreAGZkVOQTSWSOFClYa3lFeQTEn_xoCq0GL8lSRKpIxA7p94T1yUVHphNyLJcsGhkVGxi33jVEFWNJ_qTuC3CjPp3RwnFTZXCdYuFNmC1R1JXqjIp6lPxVndFX1q0Vrq4QKHql1qhWXRd-v3YAc5SbzI51t3ymPbzjrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=Wy6dcsOmBW2jdYdcMHTY8fCIf5qjanc9ZXpdWaAR7gCjZ974de4COji4Nj-KXR-8UFV_iRiRHccVmwf6QmyK_o-7m7ZQMPt0X6ftenhQl3zEx6YDfc6IA0ro1aSKqQ1BSx6LXM0aO-Nzg8K2WRVH0qu3cTc3jnRql1jIwbXzR64WHokVRIrYYgXovQROpoXkRF_MR-hgBfEfnEV-OQQ5QIb4ijWUo-2cHOoxgnpDwkEMACZh_GN9WwtLqlTtKTCoY6F3aL5En_DKXtBz_CtAEE6BOY-VxhUFpD20Q-lSL0fJrtfJFABOjz31awMDr8gubUybj1E32DD6ODsPFLP5eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=Wy6dcsOmBW2jdYdcMHTY8fCIf5qjanc9ZXpdWaAR7gCjZ974de4COji4Nj-KXR-8UFV_iRiRHccVmwf6QmyK_o-7m7ZQMPt0X6ftenhQl3zEx6YDfc6IA0ro1aSKqQ1BSx6LXM0aO-Nzg8K2WRVH0qu3cTc3jnRql1jIwbXzR64WHokVRIrYYgXovQROpoXkRF_MR-hgBfEfnEV-OQQ5QIb4ijWUo-2cHOoxgnpDwkEMACZh_GN9WwtLqlTtKTCoY6F3aL5En_DKXtBz_CtAEE6BOY-VxhUFpD20Q-lSL0fJrtfJFABOjz31awMDr8gubUybj1E32DD6ODsPFLP5eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=rLwLhOOB-h_TCqlhp8rmbY9qmlWzcSdxIyjM4NNXskS0QsVfVxiPdCVvTgZwDid90954YfgRa9XcPajQEy1YIpdTVDf_UULKbQH_d8MA2kPoeoUhXOYKJ8norv43G5NJkylZJZO0kFY4Q8JhA9mV8faM6JKteQzBmJyOAY7XDAgHRa0yXVLzhd-S-TEF9DSdNSMzbcA6fawm1ih04_Dal6VXFz9AicRfrKOHd61D9iZJoyxN56Q9Y5-hUF1s_L7XGQ2qX4aopXK4ob5mQQGkbUuTbxP6tE7fCfd3MmyAhnRXqRZvrEDAIcJZaVnCg1VZoOcvNFtNlA3FpCjo2_fT4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=rLwLhOOB-h_TCqlhp8rmbY9qmlWzcSdxIyjM4NNXskS0QsVfVxiPdCVvTgZwDid90954YfgRa9XcPajQEy1YIpdTVDf_UULKbQH_d8MA2kPoeoUhXOYKJ8norv43G5NJkylZJZO0kFY4Q8JhA9mV8faM6JKteQzBmJyOAY7XDAgHRa0yXVLzhd-S-TEF9DSdNSMzbcA6fawm1ih04_Dal6VXFz9AicRfrKOHd61D9iZJoyxN56Q9Y5-hUF1s_L7XGQ2qX4aopXK4ob5mQQGkbUuTbxP6tE7fCfd3MmyAhnRXqRZvrEDAIcJZaVnCg1VZoOcvNFtNlA3FpCjo2_fT4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jg4oMsaj9vVByuLcU1YyrGbGNkbqG_izA5EUbB3-NZnsj7iOZ6NxGKgxubqMAkkYl65s2ZwgwP2sp6MU8UjZArVktVVy5r_l2nsqf2DaRj-83oUQw5TuFCDuSMaHVFFot_jz3zYHqxYR3a9zK1UMsl3J2cXNpUT2Uy8gAXXGQ6q55uUg9ufISq8VWbta0Wiwecm-NQgZVbs2rfs-zFx-SZ_ZgGfXmD6Ksl3TxvoavF-4cGG0RtFDQwURJXqISrGUQ4F5urlVIaivtNojBwkxyFCT2h7cbjOli3TbnnCuFC6wANl_3NhAfUziTtHqxa4QdJqjBZ_imnqR6s_wx9rzTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=dDuzZOox3mb1e8i8cy0j7WA2gokWqIMLCen_ZyHiI3S6D9N0ZIqWUfjEA9y93zDWE8E42wPrjLt7x5rvTibSIk06XsK1PEhx2PBMoBaMtYLTAC_mE2kGbb-QwB9uFhLSteLlihVamv0M8azO-FPt1Sx6Fv9vfIUUp47Z_TYRJ7sn1Q0NFEGYcYTgZbI_T5QxLUusUcmYHonnTz8cJHF1uK2fO6f1LMsPusGFygR_DRE65Rhy3D1kiM4j_wQH4VX-zyM_p12qQnZWLiLSqlK0jSB7MHXe5eiJV0RR0DPw1JjL4I7mazCJATqdHrw0qmaO19RDXPvoBhcexwH3PjhvPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=dDuzZOox3mb1e8i8cy0j7WA2gokWqIMLCen_ZyHiI3S6D9N0ZIqWUfjEA9y93zDWE8E42wPrjLt7x5rvTibSIk06XsK1PEhx2PBMoBaMtYLTAC_mE2kGbb-QwB9uFhLSteLlihVamv0M8azO-FPt1Sx6Fv9vfIUUp47Z_TYRJ7sn1Q0NFEGYcYTgZbI_T5QxLUusUcmYHonnTz8cJHF1uK2fO6f1LMsPusGFygR_DRE65Rhy3D1kiM4j_wQH4VX-zyM_p12qQnZWLiLSqlK0jSB7MHXe5eiJV0RR0DPw1JjL4I7mazCJATqdHrw0qmaO19RDXPvoBhcexwH3PjhvPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=cRNegXLkXDswV7auG5qVyDt4mnCezENQBZu2TVAv9CbRXwIpfCNjUKeITtqengRUA0UbS5YHZaYtw_tnR3f9HoUdHDDdhvVeUIFE03A0ygY9-p_a2tBS4gKQu8J3N7O7ETxXWM2uRVSxBFGwdQkApelPrj8zjP5Ff-yJzPVkhQBKYeQHdgAS5PHphBPVoHgm9MNUScGnxVy_0hRmAKYiaeuOv6tYFT5MVCT47PujGIhi0POwrocaEJ72b_onScZEwoPz-InXv0LzBdZD-iAcnXdtFzchJJj3IPLAMkxrlqwfGyHoryPKBnuLGZdqGAFpTwwDrTHVLif0SQB08G1G2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=cRNegXLkXDswV7auG5qVyDt4mnCezENQBZu2TVAv9CbRXwIpfCNjUKeITtqengRUA0UbS5YHZaYtw_tnR3f9HoUdHDDdhvVeUIFE03A0ygY9-p_a2tBS4gKQu8J3N7O7ETxXWM2uRVSxBFGwdQkApelPrj8zjP5Ff-yJzPVkhQBKYeQHdgAS5PHphBPVoHgm9MNUScGnxVy_0hRmAKYiaeuOv6tYFT5MVCT47PujGIhi0POwrocaEJ72b_onScZEwoPz-InXv0LzBdZD-iAcnXdtFzchJJj3IPLAMkxrlqwfGyHoryPKBnuLGZdqGAFpTwwDrTHVLif0SQB08G1G2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=a-MvxooYJZg3qdMy6Of85ASBXHNU5IVOyFA5qcExUkqmFUuYW89jNgm6WKE7UgrfA8GsckK8VwVnfCJ9gc4o3kJG79CbCUGHBDmVI6HVjHrZcFVA3byc8SSvZ8pI3ITpLbMBjHnpaYwU4B2MZJNjhh8twpCQO65C6W6gvknarB1X28PHPGzQfpk0OacEHICorelv8vys8rr92FDvJNhFKThI0WwWQ4FGrONPPDQp7z5tknseLaRnkwmOQg6ocJjEwyNfgSs3i8GFqVXCOhFCuO-dDcEXtjbcyub6RZ9N05Y-MZuEUl2K5hUkiW9__vkOaN9x27-Q0YyzIZmynba5BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=a-MvxooYJZg3qdMy6Of85ASBXHNU5IVOyFA5qcExUkqmFUuYW89jNgm6WKE7UgrfA8GsckK8VwVnfCJ9gc4o3kJG79CbCUGHBDmVI6HVjHrZcFVA3byc8SSvZ8pI3ITpLbMBjHnpaYwU4B2MZJNjhh8twpCQO65C6W6gvknarB1X28PHPGzQfpk0OacEHICorelv8vys8rr92FDvJNhFKThI0WwWQ4FGrONPPDQp7z5tknseLaRnkwmOQg6ocJjEwyNfgSs3i8GFqVXCOhFCuO-dDcEXtjbcyub6RZ9N05Y-MZuEUl2K5hUkiW9__vkOaN9x27-Q0YyzIZmynba5BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWvrKaXbJpGBfqGl2rM964xVUs02vA_EV8A1h77uJ2o8TgqelyNwq0UtpIIW42TtSgkw8oD50lJcpeOX5W9VHdAJOmvKWhGae-trCbpzowmZ669gHGNE2TeCzxoEhoQvV479d0fm48rpKAS-cwLAezMtPEbi22rHrvt4Mmz0fShF8ypwGiO17xJiZUK3G0ivSmSi32Cok086QeYY5N_eTGHuarNBDHm1vD1Oo0vVfrs4LeprB0Ft4w_j-OWN1uM8CxcDLqNzmoC3_ihnP8A0Awh7u0gRNyc5DxH7BrRMyvXjZ3SYL5hFtuoqhv1wHKItA6BzGz5e-MH9mFpGV9yPLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=YmtA7i3gNuSXHM7GENsWXpsMGSGNYtOYgE6epM_8S3pgLpbTubA6f7OzBRqt_0fIQ2ztrbnzGppWpA-1LnMGvWXpUntU8-fItedq8OYEFRlq07Tge659q7rv0ko5h_aNITOhZWh-DOwSS3BVKbVYZFA-gqNwPygOx3SjGektINEDV67XesUKwrKVyVcc8xatj3zqGq0BzunYbogc9zNqV94LOob1U0yjgsdIirLC43swya_v_-huGsteJ5TcfPoRAIYpstIOmEaEtkjLK7p6atpb9CdzqqDM0XHsDST2oF75_oRWd_MCzxt39y4l6PsrQi-hdPj-4JVgB1kB-lZUnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=YmtA7i3gNuSXHM7GENsWXpsMGSGNYtOYgE6epM_8S3pgLpbTubA6f7OzBRqt_0fIQ2ztrbnzGppWpA-1LnMGvWXpUntU8-fItedq8OYEFRlq07Tge659q7rv0ko5h_aNITOhZWh-DOwSS3BVKbVYZFA-gqNwPygOx3SjGektINEDV67XesUKwrKVyVcc8xatj3zqGq0BzunYbogc9zNqV94LOob1U0yjgsdIirLC43swya_v_-huGsteJ5TcfPoRAIYpstIOmEaEtkjLK7p6atpb9CdzqqDM0XHsDST2oF75_oRWd_MCzxt39y4l6PsrQi-hdPj-4JVgB1kB-lZUnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOlVUXQw_2aeJFPwzPhmkyVJTDtcefhHGL97yMd3KT3wtLY4tfOBsWb5JuxsWy1LiVnjKwZxAbIT_MLNoDIA6m3c6nxhXizgWSxVV_WL7Oak3lLB5v5L3gM_qOqRPIqndS8PhlGdQfjU2ow7Xdx-0aeYwDexUkoGCsbCtvJD77lzwmpuV-XBxZNl38f_0-2ca76-39G192wjN5LRNRM5U51ocHJtUw8hO7yzTORyzx2AwB01EHWMQsbYBXO5ARNhYNLVXkrEBpY7hZdSsji80httLCFXdwPdFJ7GHTruyY5P4ASyGbXKLj5TiySSorC2ELgBYPwQ5oZrjJ9YOe9OSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=P9-U79SLZq2sFd-mRdB-5dsKjscySfukdSgDnlFgPWY1tKbt981WZ6yChj7Zap1d9gSO3ln-7k09GQ6KOmib53C_TC9GOJX08iygUEYdTYK6Oc_7vbu-HGdtHkTzo3t3XOwKIhiPxJ59CgY02Ny6MPFF2Mce18FHDyjx8aK7L9arjOjunePV2LyliBeHqLlOvELRS6GsOaT24Ew-V9OI_VIGFOQHhFYiTYJP7JKoCK9UKP-Dntg5248Yr1DP7v4BFKYp3mTy6CsvylHdT0MoQERZ2Wn9HLmZ4wBw9RucTlQ0GregRXLgn_tFbfz5SqtsVX9N8AcCZZAwzlRvHvxTaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=P9-U79SLZq2sFd-mRdB-5dsKjscySfukdSgDnlFgPWY1tKbt981WZ6yChj7Zap1d9gSO3ln-7k09GQ6KOmib53C_TC9GOJX08iygUEYdTYK6Oc_7vbu-HGdtHkTzo3t3XOwKIhiPxJ59CgY02Ny6MPFF2Mce18FHDyjx8aK7L9arjOjunePV2LyliBeHqLlOvELRS6GsOaT24Ew-V9OI_VIGFOQHhFYiTYJP7JKoCK9UKP-Dntg5248Yr1DP7v4BFKYp3mTy6CsvylHdT0MoQERZ2Wn9HLmZ4wBw9RucTlQ0GregRXLgn_tFbfz5SqtsVX9N8AcCZZAwzlRvHvxTaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuJI5JlstPdQUxekmUeOjASa_CXbPrvZ0HqzHbefWTiu7W4eQvarxAeOjUbtfqm0vULBVNRLlJCt2dSARz6Lhi2w68JOupiLuqL4djD11hQrKBo6saeMC1YjZYeSpMz84awwxt0YA7E6lPGMEHG9sWTrFxaZGOfdoqiLWxmVOL9v_W_eKD23v3fsaoV3S99NaE3SBwK-HxOnBLCcezIn0s4Ys4ThZYaAs1vLejSmHfTRwJTA3Y0h6Anan8MGkyWNXucuiJNhtA5DDKYlCkoj1DudYthzOQaD02JYCOkW7__26igiV2MMw4m7LnPmvf2-66tps0eEsiQ7RQF5NJDsDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=C04TwtvIaHJYsNXVV8arltr__8BjbTv3GK6c47VR-YwXuc6BOSqQ86gjKuvamxgIqvbqHt9fJy0mD7k0YGS6eLJkfzMLB1a-OHBfwVwIfs0Xw3S7pOTl4b8lOcNhZDxo6LzY6HjMxViE_gvOoKT__V57xtbvVhvkqX2Fciig2AIzkx9X3WfzYBLXOzaQjsO6uHNq_bQ-4y6e3bD1_a9Qi6J3cYkMQ7fvurQaaN-yLPx-lZ8xUi_GhHZeefVx7NDFKAYd3e0lt4693d84nq7GY2g9LEeRj6LwbBE0JxqlG4pIKaZtBYHY5-qBINel6vH_EdmftKFdiMw2zG4c9VSB-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=C04TwtvIaHJYsNXVV8arltr__8BjbTv3GK6c47VR-YwXuc6BOSqQ86gjKuvamxgIqvbqHt9fJy0mD7k0YGS6eLJkfzMLB1a-OHBfwVwIfs0Xw3S7pOTl4b8lOcNhZDxo6LzY6HjMxViE_gvOoKT__V57xtbvVhvkqX2Fciig2AIzkx9X3WfzYBLXOzaQjsO6uHNq_bQ-4y6e3bD1_a9Qi6J3cYkMQ7fvurQaaN-yLPx-lZ8xUi_GhHZeefVx7NDFKAYd3e0lt4693d84nq7GY2g9LEeRj6LwbBE0JxqlG4pIKaZtBYHY5-qBINel6vH_EdmftKFdiMw2zG4c9VSB-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3nI9N4zWLjGo_Jtr23Oe1-el0cG65GVc6MiFy840aXwGw5iFmw3SJvjFOOefrd0lYpF3BUJynL9SJZXH_S03ALCBiDEbqEcCCswUFxVJJFAC0_UiJKcxZheAGb24Mhw58fwN0CXvp9eyhQlxAiCK_Ig3uqEJxAXCUgEcQEbsF2owQQI69GF0LSDvsBwDwDw_YeC-Qoxev4zZEUrr0a6ewliyak5u6TLf2o29QgM1HAFfn7vpV0eUoIG-1sConGWTlsHp1pYOT5WlibJ4l9KVPx8flXNOXatp8fNCGubzhlZ9gI6UIKFpYtSInnIuNXHiDv9DB7Xlo572h8pmisilg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tu0gF5Ggqh3ZMgDCyg56s6zqMumctjFWDSHZGUuOlG_gvKhRK3hBiaFsXhvAWbXuUH_9XoJ7uqWqA7j5a7KqbOt64fYJKdRbAMZ3BVW0pcXb7jjPnolo995jIOS0f4j0Rou8Qpt6cO7SXabs0zurFfb5V0sPWkAUgwy91XXqeDZgO-vADIOpK-cgWLBr8AAedsuKiKgw4VQ5eODzZiCyvY08Nxm5nU2tcTdhkiBBCOdfPRdVrC297W9UC1_8BwTX-7eOitAzLIfw8TEYgYmtEsowGAp5w5TEX6yYPoTAq2azeB1zrAxiwqls9ntGj8v9x4dBfl-DoKI1v9VXScPbRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=adni-wcIQ9zMWjWKsbpe1IErTs9C4BHoyqrmmnhRhrveFgW8GjYnHDTjOOTqB1dPgGbsEjT1_zPnswsf8doR2bac36CAb14qnWbdboP944sw4M6scXoSPkbpyy-IdZXtu-ICd6YIJVlLQqIalRIUl2Dii7xL8SEURx1zIHxoT1hAlluD1RYl3v2mkXhjxwZ43nUmzCxTsSlPpLvMGxODghwoQyfNA8vp-H3l_SpIAl8qrX1uGHX39Aqavgj5wOqVjZCYr7ZGHPcQWUYQ-HxUytnEt0RZM33G_x5iuJjsrTpgLEL8_LPEjYUg8W0_BbTIGV4DxsA_sGJQdY3QRyyrPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=adni-wcIQ9zMWjWKsbpe1IErTs9C4BHoyqrmmnhRhrveFgW8GjYnHDTjOOTqB1dPgGbsEjT1_zPnswsf8doR2bac36CAb14qnWbdboP944sw4M6scXoSPkbpyy-IdZXtu-ICd6YIJVlLQqIalRIUl2Dii7xL8SEURx1zIHxoT1hAlluD1RYl3v2mkXhjxwZ43nUmzCxTsSlPpLvMGxODghwoQyfNA8vp-H3l_SpIAl8qrX1uGHX39Aqavgj5wOqVjZCYr7ZGHPcQWUYQ-HxUytnEt0RZM33G_x5iuJjsrTpgLEL8_LPEjYUg8W0_BbTIGV4DxsA_sGJQdY3QRyyrPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slWXjMFjk8k3jNog6wAEWZGrpXRuyIApmpvBYqAosmf8bqFViiWf7TqIYlhku_N_n7osJGW7sw0lW9L6up610hqJCUswg3TcNYkVUXIg-bCmGyvRS2MFXjvSt0m0qXxrjVUtlDRX0Eqw9e-2kHQY53uvrKJYUG2TkQrrfD63lRNxR9s3B-QRXYCp3NLbvyYY68PNXOjsFk3nt2Xe0ZSfjpPhDS_OY6OSAe16Hkxm_VSfGyzeGn26M7I3PMGF239A8yfSbVRk9K_zJID1y59ybX_1RQrWQ70kmFwrKgU8mIMYadRRe3Z75uC8v-BgVCrSbmd53m0sWG9sOgQXAXgOXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7JYxi8gq_grIaFqXvYM5d4RMl77F3qLvZ8Qcg9g_QCd2FcXyGwXbGNoOSv4b1Tn9qarhJFq9XscW9ij3E9D7gyr6fEO6lIsdIIs995_YP3HCE91_WbrlwlKeYQkmN1jMO6XA1FbyqPhMJ3NPuAeaYbz7nBMKmuPSWudkKlbHiU6F8K-EEPdaiVO92PZpI85wX-LrtpRx-ewKN5mzGvDdlnmKE7CtNxyMVH6On_HZyf4QA2hhdtmauVhQN7dAY-KpZosEu9ddvzJC__s_C95Og0T0DvGz6ax58Er75yQp35HF_xsxHtNIh6kI6cTWCGrk_GhCCKfrQhKp0p6aYh_nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uysUkzLw_vBJhJXuYY1qkgrAQ4xljTqEBLzVrEW5-Y1_YsRRwDy3AZUqba5grYjFJo-PLYuvEBOHWGwzahCV7V8TEjWO6Q8xPUmj0rpvZ-YyfxHp8zPJG1UZlew4UyEHm7_tzGubPCwaX1EgYRrJzvSoh0xpszqaCBWzeaw-_Uo5gaL7mwPsDXCCLQca9NZinqVzapTX1FN1aqDY4BYkcKHRgkKLka_4H28RseqUONaLjoaVFcxWUr6nN98ULAPbnIu1rAUK3DJxBcghotbINNivxgDwkZJ4DrKXtT35Za98xyqRvMsliWnU-WB51FLA4R5a-_px0oWZUacC6qJ-tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuaH1xmOCD1vXwrcQYV5YFjTh9F4LjxXGu3CLaNnIIBvtjHiw8KSSEJCOQOrx_EMr74H_DuJpXM9UO984L3OZZfWM5Z579m5kyjdaoFUBira7pan8wQO0ZOQCqzDwl1OZrJhEuZE2fY7PXP75U8CsNys1hM9ID9z_T50o7y4b7ZAF1quss9SnV7d8P71NoQsSN__2S0yVjYr_TSS1bxQqf6eFw8mjm4LV6Qxcb5cr8vraI25VVv60M3FRQW9o5nz7SakIbpGC5x0FcU0xMmxTv8sLtO_9vZooY3Cxx58iHaYolh1bTPLCQu5Dxae0I4oHFUxb9qJPUC9I4Ip355CRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pG03XlZqE7vtG1Cfm36IyJ27dg1dFWIrAJRbgnInzkz1nD6hFS2wX8T-L_9F4lIj7v_76ymlABwf0pBkCUkPfNnoMkjau4tg053-qtKc28hCyRCnUylow6Cyjoby3pWr3kkFtSjZw1BKq_tOhO0N_q8NrSU81pTm877ORIFgFnpTwQCC2C_fC1O8ZuRBaikvO8D7xxmd1f-BhxjZYDjtYvf65NAH6LRNYoEWF0vq7hRZpcGMAOH9D8EzHWpzyDQJBEwuaPmQQ3qoa6ooUlL_8szAnf0fk1TJZoYtX3ap8e2JsritOE9mNOQa3ZnB5-_ySY6N_G1-TkThnEDcDLylYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=ArpO0-Ze_LHSYWQD4QueKjZvL5olI2M3PuSncNn53v4ZFTAl76vAnjS6i0fc-jZWmXX29mX9p6moVtiunfnYOA1idjMyHfiavfyDSdN-mlvV9mUTKxL90Ba6c4dLYj0UZh9oWXjt_ZekU7rOLThgqK82qV5P1uaUFRZez_tYCLVDW5fAOMTm3B5bobvQyn3Nx3K30fjOvniaR7d3s0i2LfB_-VOkyUZvXe-YlNkUDIKv_BPenNLPuNYwWMX8iOnf6C6-o3bHx4UVwEr4maVOTyTl2QA_hpJJVXWuovccLDzrS01vO0mAfXrLAaFHJTiBA8aGHlhDbNm5qFkBs5_0Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=ArpO0-Ze_LHSYWQD4QueKjZvL5olI2M3PuSncNn53v4ZFTAl76vAnjS6i0fc-jZWmXX29mX9p6moVtiunfnYOA1idjMyHfiavfyDSdN-mlvV9mUTKxL90Ba6c4dLYj0UZh9oWXjt_ZekU7rOLThgqK82qV5P1uaUFRZez_tYCLVDW5fAOMTm3B5bobvQyn3Nx3K30fjOvniaR7d3s0i2LfB_-VOkyUZvXe-YlNkUDIKv_BPenNLPuNYwWMX8iOnf6C6-o3bHx4UVwEr4maVOTyTl2QA_hpJJVXWuovccLDzrS01vO0mAfXrLAaFHJTiBA8aGHlhDbNm5qFkBs5_0Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=FPreCy3NLj4F4GEzxy9XbJWyGlrNJKanhaa3tmmCvvKV115bVTEs6ExkgVm5EBkCFC6-XaJ_M7K6d7kLqdN_6i2AXf1eO35Fr2bEle8u8wtyITvUzHNOmgGj8n2Gscp78dQdNjDcgbxnaxeYorC_yH2_lTyyy6NEGRw2HDzD3wno9kSGAqIfuRPxycxKli1x8t2ZuGAV6MZL8A5FrnZ1jLQ4imxKb_Kby7MHxi7hRPcu7pcysWbLqEcwX42t2rC5xZ_EOM5rrodx3wSyszUEgmd1uIg8maF9-v-bkGQ7tbjzOtBdT0nu08QgohXI6bSl0RFq3iZNZuxUJvXpW2eFvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=FPreCy3NLj4F4GEzxy9XbJWyGlrNJKanhaa3tmmCvvKV115bVTEs6ExkgVm5EBkCFC6-XaJ_M7K6d7kLqdN_6i2AXf1eO35Fr2bEle8u8wtyITvUzHNOmgGj8n2Gscp78dQdNjDcgbxnaxeYorC_yH2_lTyyy6NEGRw2HDzD3wno9kSGAqIfuRPxycxKli1x8t2ZuGAV6MZL8A5FrnZ1jLQ4imxKb_Kby7MHxi7hRPcu7pcysWbLqEcwX42t2rC5xZ_EOM5rrodx3wSyszUEgmd1uIg8maF9-v-bkGQ7tbjzOtBdT0nu08QgohXI6bSl0RFq3iZNZuxUJvXpW2eFvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=A8HiWTTOQ8BkFtxcmreD-88xZ8C5iiDD7zBBuYRe86lmeZHHdL1iN6RYGLTqW1H3e3gBeVdJLnVIvrrBctlDR2f4cdNxSlq6z8UR-xMxbSzJLR5B4hAFcmWizAty0aEzIv3evJ7dG_YOh8lre4HKSVwdERbMcb5VD1tOqGraIrfq-4B4gg3xzvWwQ2YtLHuZnjuu85tfsotnFcREg_9wV0f-2Zz8quz0C3XHc-rwuX9neRSzVcU3t42pp8S83cM6vlw0C9y8xGCXV_oEPe7V03CNcRSfOSjZgj1LMLQwB4zZ-hWNZszJ_NctmligzgtnhwweVjhHjUVH0pr89uqIqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=A8HiWTTOQ8BkFtxcmreD-88xZ8C5iiDD7zBBuYRe86lmeZHHdL1iN6RYGLTqW1H3e3gBeVdJLnVIvrrBctlDR2f4cdNxSlq6z8UR-xMxbSzJLR5B4hAFcmWizAty0aEzIv3evJ7dG_YOh8lre4HKSVwdERbMcb5VD1tOqGraIrfq-4B4gg3xzvWwQ2YtLHuZnjuu85tfsotnFcREg_9wV0f-2Zz8quz0C3XHc-rwuX9neRSzVcU3t42pp8S83cM6vlw0C9y8xGCXV_oEPe7V03CNcRSfOSjZgj1LMLQwB4zZ-hWNZszJ_NctmligzgtnhwweVjhHjUVH0pr89uqIqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=PoyxnhHnyHTu0OhIIgErC2uUcxrLrEefO0OSE91fitZZzbluas-7850WdM4JWk7WBQeai0Rifj6LQiD04LiAEVrKe2aNfRglaM25JpKKHD0WezM0XeE6xKJSoi6uV766V10qe0TpsFetcTvW_wP_92ZuzJBAstp5I6E5xEjkmuLPscpY_6QeSoMCPBw6jgMfPyELMcaRed0fANnl_JKOU4S2k4LAj6PHKdmYT7AiUIeEDLdg3mzPU4o5gaMzgt52I5MIS3ebhdUVmnRjFwHBZWwNs5GmC4yfL3_0Nm6UHgKq8YgUQG8dK_i6CzQpkK_vstzvn1wirFARywpUeqZVjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=PoyxnhHnyHTu0OhIIgErC2uUcxrLrEefO0OSE91fitZZzbluas-7850WdM4JWk7WBQeai0Rifj6LQiD04LiAEVrKe2aNfRglaM25JpKKHD0WezM0XeE6xKJSoi6uV766V10qe0TpsFetcTvW_wP_92ZuzJBAstp5I6E5xEjkmuLPscpY_6QeSoMCPBw6jgMfPyELMcaRed0fANnl_JKOU4S2k4LAj6PHKdmYT7AiUIeEDLdg3mzPU4o5gaMzgt52I5MIS3ebhdUVmnRjFwHBZWwNs5GmC4yfL3_0Nm6UHgKq8YgUQG8dK_i6CzQpkK_vstzvn1wirFARywpUeqZVjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOxtiGTWZMMxLdjGbH-BIF4N5amSzBUT7cSV3W4e-idMu2L73iuvLMhufuWhncKIg4vPkHjeupgx7tLLNO298y8cnGMFGgtsHSKo41n9a8zax_fovW5oV3q5zEswTMZNl7ZITIVwm1Lw9o4LUxAe5UKni_Hr-kUuTNXO7IfxQYERt-AN7De-rUPQGFPr2xsypnrnpnk1cdKTBTKHtiGysq1KnxWKEBlifVbwMsBO9yZc1adh8ppBRlNnV4b2p3wRRSxIL1A1aG9ElmaJDOlsDghxudG8CbwV9uUZWUw9CGDy2FizLZvK9LJnp_nNNeDbiXobTOyIbYTOtKRIlMkW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxQbXoqBTf5_e9AZDvqycsjkwP1A3-ggxTR4U3GsZcyYDHBtMmF5k9oZ9LBSIVbBTjYEeCfL_hGBXgM81V5NJ_o7xpPVyTTuHJl0vI1UWv2ZXUioaBB-YZAYSkj_Ppv9bN5usgs12ozY_KeG1Z3h4cT1sUk9msxhuuEKHvjt911UsovBQWSyB2KYZDgFNMo9UnGqJ3birLjkYTWwxvoZVWik4r8KNjHepUTQFTe8VS6evRGzxU1403knFF7ol4I9jFEFUSjhfj02J6M8SvhUBmAHtElomtIZFda7pTlU2bO9JzApd_xHFRoZz-aBV72_qZcSAz6JAxE824i9DbNyjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=DelDIbYdIB9xDlPvU7StjbtpbZqaRBOf6OBJZUakFyhihwfL442du4hRXsMCbHOLlmxG1WfcJSRumsAMl2QTA9vKMrgSl9fyp1TTB6xVZzGlzgc9ANcq3EwI6V8gcmShxBAep2Hx-nOG5tDYo3E4SqS0U-QSAL_mwMLw9rcb5Si1fI8Idsjl1oHuYA8THKCaxvC_c9tcuGn_JhxdQU-NPz4jNRSN-Kd3y32Y1_3Neq0L_WY2VNCtkG582Hi-zQ9m3Ka8L6WH2ZmsRJpjo0fSsOr-2sGlL-SuBxiF1ZTbJg0o8Eoq9pG7RNimFsSH24tjVdfjBd5r0d5oy4ECJIKC3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=DelDIbYdIB9xDlPvU7StjbtpbZqaRBOf6OBJZUakFyhihwfL442du4hRXsMCbHOLlmxG1WfcJSRumsAMl2QTA9vKMrgSl9fyp1TTB6xVZzGlzgc9ANcq3EwI6V8gcmShxBAep2Hx-nOG5tDYo3E4SqS0U-QSAL_mwMLw9rcb5Si1fI8Idsjl1oHuYA8THKCaxvC_c9tcuGn_JhxdQU-NPz4jNRSN-Kd3y32Y1_3Neq0L_WY2VNCtkG582Hi-zQ9m3Ka8L6WH2ZmsRJpjo0fSsOr-2sGlL-SuBxiF1ZTbJg0o8Eoq9pG7RNimFsSH24tjVdfjBd5r0d5oy4ECJIKC3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSwD9dhHYIS57rYJO_8aR4HtQe3dXVk2SdXHelj6Kgt4pr7vyPrV68lbc2T_gc8Uk4-dq1dswaJLq931c9a6ahirORqDcViVFxWtHMv1_0anvJgASFg574SiOQTPbuUti2EI-UXdywp6z-57YF4bVNA_p6y_SFkUIQTDTpTuYmatM50z1BlfX1qJaur7TXl5aqz6vS1sD4RceaQtVmZ0oHf-MO8vjkkkbOo0fRe6NWnfFJRg0A0e33MLwV2hb2l51Rck3c2Byvv5Dqmd-QK3bN1S2vPTg1vKXnFsxphrqFpZYw5MrKeaNkEBlEoo4DEjsFstrANQFxeFShK6FW5tVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=eVNMWFdm9oMlR8mwNhxeJ29BPyAkiFlL2IcJS1-AXfoVQOW9BlhvluewPAzkBe7IPBIjuHuhxdBffSg0eXnIRD29ffkWElbltX_ZBoXs0m1a3-PJjgZuRzb08M6WtCzfeUZBbxfDyy8v5DabcHvi4YdHS63izQRtPnQAAsxYQ0DLTFRYa8HQ6Z2MOG92-G7RN6Vckr5tbCA-uZ4lVj2YDZ700iDdsQ0A4otwMC7uQGkOgeHfyAhJ8WGWK6i8HXhOclyqPEwyYrYUJZ6Jq8NegNUNGMn4yhPKxydArRPzpVM_19vS-DdxxrsfajAJHSch4GV1lrohHvLYWT5GmD-kYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=eVNMWFdm9oMlR8mwNhxeJ29BPyAkiFlL2IcJS1-AXfoVQOW9BlhvluewPAzkBe7IPBIjuHuhxdBffSg0eXnIRD29ffkWElbltX_ZBoXs0m1a3-PJjgZuRzb08M6WtCzfeUZBbxfDyy8v5DabcHvi4YdHS63izQRtPnQAAsxYQ0DLTFRYa8HQ6Z2MOG92-G7RN6Vckr5tbCA-uZ4lVj2YDZ700iDdsQ0A4otwMC7uQGkOgeHfyAhJ8WGWK6i8HXhOclyqPEwyYrYUJZ6Jq8NegNUNGMn4yhPKxydArRPzpVM_19vS-DdxxrsfajAJHSch4GV1lrohHvLYWT5GmD-kYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_nPXRKuCCluJhavPxrbi03Mr5KnV-gGuW8_lYtYKI7tW3VK2nRmK_LY04vBNa8YlOVzEqAK6P6-a3Kg0ct8wpDiFrIfBq6W7mJdh5RZIn0MCbxW73ce-HqjEt7kml61JvZVmA0cYi4pqaDun67pKlCvGWKtOGMxWl1y6Rrc6fjLL_Tetut5q_mIrqFGDW3ozTs5-9ELWw7tCOI7VEn0Brz3aV21H7y08APRMEbHimV1TRYyTgGtiVpvY8-hGCwsEpvjBgSBsZtWbtBtLeL0PM8av4cZMHM4BchvLRsxGthv8x51ibobVDoWWjl8ALr-BIONgRKxDv_OEul1j6BRug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkRIleU-aghxcEOFOIgnkSAtW9x6DfVAJpTH1ooEE6ku6VODaScBDHzX7XinLKGDhve3YekXf9Cg8vPKuMmYUe5LPrlcl1aoi_-UzxtvS-gehZLC-0gHCw2bxIvkKVdL489MKt2oyZok1fB92fNnLs2SN-MFNgVuuWZbrp1SD6LFPeWqPf-03hhw4QVFAp-xL7wBYWJ8J-f8-Kj2QIcgTkd_2suXDYMQSjRDvzAw54gqaE13PUYOaxs4LYfp2F6yV_73BbckPBnykHNTmNmbvLslhlb0YM3-OpUGh7ku7ryCEIQQFGgPG8nUAPjI005sddxWmtxW0GY5rlu1dPc1nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=OifXofp8bPhcTagG8zFpdwKa0n4Rrq1dwBXww4YGYPWhufYxUK8eaxKbezDiooSNN3xQmEIq409-Byowzt7KPoTtvVQ1b0ocDhtrHY38PJvZ5bdnFnUO3skqP9_dVckYTYnxfO8qgyt5RSeHgGNtDSk-vp9VCIA8TT9so5dkLyE-wRSs0nI_GUWJCZVyMo_jGIVxPl3LAmcnN2rdkFTkgrXk-sHRQ16eXAedYnSVnQozcVrphet90LK6QLiic5iGoJb-nhNYt5hQb8tA9wI0heuPOD7m6Y0IwnCxkC-ekj6QgHGY1Qbf2yx3Q57JQlCRYdmyEFmGSJ0UZnBCKmQrQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=OifXofp8bPhcTagG8zFpdwKa0n4Rrq1dwBXww4YGYPWhufYxUK8eaxKbezDiooSNN3xQmEIq409-Byowzt7KPoTtvVQ1b0ocDhtrHY38PJvZ5bdnFnUO3skqP9_dVckYTYnxfO8qgyt5RSeHgGNtDSk-vp9VCIA8TT9so5dkLyE-wRSs0nI_GUWJCZVyMo_jGIVxPl3LAmcnN2rdkFTkgrXk-sHRQ16eXAedYnSVnQozcVrphet90LK6QLiic5iGoJb-nhNYt5hQb8tA9wI0heuPOD7m6Y0IwnCxkC-ekj6QgHGY1Qbf2yx3Q57JQlCRYdmyEFmGSJ0UZnBCKmQrQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=lSfyp6gzjZxUP-Ok5hfb-i_XMvNwmhPTsvqCKt_MKQuPafah5PqN4R5uXBHjKC4F6ojwcxLE0kMHGbCmr8tgeaY7WKJbFEC1UXRh31kCgNzMqLMg_N3D7N1dt5xYv25D1YSW-p4TWReX0fwk2P422ERGgpcz-HLTcPnNzSNpOSWT1Ivz44kYJcUTicjMi2CwnZozKgNeJASM0gKVR9Qyqwgt-xkpq6LPbDIAaalX83NCvoZrtiEVC3C6CPB3JUpD6sALTc4Mk7Y1c0c3K3J7qFyuRriULfdlv6oWr946gXpLK27azc9g4yG9SgJx12sPYvXQlNqUiMDpMMpPVdg-Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=lSfyp6gzjZxUP-Ok5hfb-i_XMvNwmhPTsvqCKt_MKQuPafah5PqN4R5uXBHjKC4F6ojwcxLE0kMHGbCmr8tgeaY7WKJbFEC1UXRh31kCgNzMqLMg_N3D7N1dt5xYv25D1YSW-p4TWReX0fwk2P422ERGgpcz-HLTcPnNzSNpOSWT1Ivz44kYJcUTicjMi2CwnZozKgNeJASM0gKVR9Qyqwgt-xkpq6LPbDIAaalX83NCvoZrtiEVC3C6CPB3JUpD6sALTc4Mk7Y1c0c3K3J7qFyuRriULfdlv6oWr946gXpLK27azc9g4yG9SgJx12sPYvXQlNqUiMDpMMpPVdg-Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaK4-dPCdNL5hnIuanHuelc2rTmuLJfE2wqJPnwtsjatyvFWgOKviuOduZ8O-uv1sWNEkSwTHerYeXSmeP2BU78hnhItAk6ZP5is-52SulCRXQsG8hOYl9uiB0rlrkNIs_Gr927Hoi6TSN_yH9GcerQ34MgyDgsJiceEg-F4L1Bz5KsTs4Xuv_padve__u-uY2udEo18hpyxdcKH63z6y-8QAXMNFErgh0nzWNFIQYFY5q83VuwwTjdL59mxWhkyVWI1kvBWSj7-A4yiYWNxnjQ9tYDZyvod8D8yuN7oHGTaeR8bvxLHL421DmHRHf5GtE0DyaC7s-auxvm1SwbjiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbkk1wd55u6q6v5JHz9VApwalSfoSLYVo7QrCs11IkZZSuVVCkbsJanA5m6YF_GYv1bHBie5rfrUzOJXGvSntaYZK-tz8eXEvK2eUD8QHR73xQT9vF6NGXsdhafV9WpnFK1gpKlOWYyt2S8ErnuTaJXJKQcpAVMAo069kJrRG4XAvQOWryTNGMpbA7zycL-iuSNxu6v1j7lJzbcXXoRArDe-g1SQlFyJpSFe-9ReVKWr4fmwo_PVB6I4U_V2WTj8JQ71VpCbsuhprIZyRRFH2ipu9Fp4af3T0xQQjW24R3xL7ipibim11aOk8muWFkCCGDuIdJF7Pdcoi6IKHUP3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFaDMf8nSDcuYrTJ0VVhLi_bhyxhC-3O1W5caiV-t9_OXKuK_ALmEEe2p1OURgRKIcU3ncM4WesZ0pUzQm4MJX47nM9_cfyxDCPgOHwba9sZX_j5KGYdXoU3KXb7QBJfE-PuGH0Ds7pTsO5LbZGdqCWQZH7ip3LNSVg5Dhs-et8hKeZO9-qFmlTecZIaIXdYREcQePcntyTDnF9NRrHHX3x-KB6Dj3fsFQDCy3_Yr_0uH3fmdtFzwPzva2YL8mN4x6r9WN6F7VuyJENYkQeXEtZyH9N1Yd6ooK8ozzy7TWARO658ny1JkkbQ2bKGU3AREarh1L3uONapl7ELq0olWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=JxbKkGGtRyj2lG0yR0v4emxkHZnAEayQSQJg8rghFrtn2ExYogvGBVvkNJ_CO2Gn-tO_cKGZQF1hAEuOf1llwEsAFacILOZdRPW6VSrmbMIR-yRY4Vyocqwf18klN-1P6WhVX7Hk_wLafKDU_AlZV5C3do1XVZAtn0L6OVc-zxg4h96t9S5MSs42xidpRcoKtyP3vl_R-irVprXWDus6DUaDLzoq61Y_hvYqqXJ1hZJCEQNdhPWCcaTbF-bI-ckzFMlBURh7HtKTXfcZu_786xCxeBAuZHU2R-hO1ieWNYSX1BFNI62Sf-3c-OH-eU7sEOrN0tjtJ_CXKkNECoa7yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=JxbKkGGtRyj2lG0yR0v4emxkHZnAEayQSQJg8rghFrtn2ExYogvGBVvkNJ_CO2Gn-tO_cKGZQF1hAEuOf1llwEsAFacILOZdRPW6VSrmbMIR-yRY4Vyocqwf18klN-1P6WhVX7Hk_wLafKDU_AlZV5C3do1XVZAtn0L6OVc-zxg4h96t9S5MSs42xidpRcoKtyP3vl_R-irVprXWDus6DUaDLzoq61Y_hvYqqXJ1hZJCEQNdhPWCcaTbF-bI-ckzFMlBURh7HtKTXfcZu_786xCxeBAuZHU2R-hO1ieWNYSX1BFNI62Sf-3c-OH-eU7sEOrN0tjtJ_CXKkNECoa7yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pupJlswl9Z-KDeflbkfiKQQ8eu-3jvgjkaznZ-vuAtcJ96ipXubnhzjbB13xzyy2BNp8ZQuFu8rz1OGKNPClriAAvY0b0-hZjFWDl_Rj22bldKTNu49Jx56599RsTUC0TXTR825QsesdH7EtdQTKBRLErRPuWM4EdzADYnYmcx9PY-dBPVhUD9FuG4uCIwsMsEC0OMNSu3NIkQFiOQ2tPIK8V8hREB-QDhOoGtPiJZ9yhKWlmHCllEdYf5wwxrwn1i5go8zq3rqhOpfLdrp1o6VQga9RRt-hOiezs8sG9Xd_dmlmXfy4ivQQlobBeJFcmHHGjm07WcQ5GCJM36hjcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZCwr49u8ye8Fg5Q_rkiHXJ7eut9f-smTNGLRHOi5h_u0OwNPYzTpC-ramAfcSUYGypyU6EpHWYflLLfuT-bvG6PaSYc6rrDhfIldi9aa0xwzuovtgxKISsmcP7P1f8KoVz2bEWCgEwk7txLEV67jCZtBwBWoWJfLUM8PqHHpu5O892H-FzlGzkVXKpLTVn4ARSH9nEf-mEBYrWiqcx-xTyfdTG8q4DlK_3bCiuRbPPoAwPX5DzScvaNJXW5cMGj5sObPJbadds_kRqU9wgaGjPBlk-hY2D8zKGnIeABYkhQsdKWqtuZWifyw2eo6YAWNoIpLz37nCpJ7Uh1bcfD5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">جمهوری اسلامی تا اینجا با آمریکا به توافق رسید، اما هرگز با مردم ایران همراهی نکرد
و به توافق نرسید.
از قضا با اسرائیل هم به توافق نرسیده.
مشکل آمریکا با جمهوری اسلامی
برنامه‌ای هسته‌ای اش بود.
مشکل اسرائیل با جمهوری اسلامی،
اما هسته‌ای، موشکی و نیابتی‌اش بود .
مشکل مردم ایران با جمهوری اسلامی
اما ذات خبیث و خونریز،
غارتگر و سرکوبگرش بود.
اینها هیچ کدوم حل نشده.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
