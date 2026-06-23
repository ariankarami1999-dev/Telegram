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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 20:30:22</div>
<hr>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBLBI_814qgol_DQ-CIl1yYSfSaQxp2B1Wh4_IPFEmFgWj5VT2ZvlYgB9pb-ulo1GouS5z2tOfgb9OfNsrEo72Uz-5QdMHBy24nQbSTQMWih68uQAlNetn9-OoPgStEbfTHFcNbAxwHyQjDhm_c7q00qEh2N23igLiJzk6T1eJ8ppq2b6sqSJyXgaMIG4_CQWnN_Up9o5Or7YKfnf0QzqRt-lTdMKVWG162UQws8oCy_JDAK6ndbTkLL6z_PnTkX45uNns93HqbTJtqcf1XxoQj5cfl5zLfRBkViNdqFWpaxr4lMiagnhqhX5G0GklWkwuhTKnUbRg0f396JybuvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_V24fwnlSEn8pBtox3mpxpxImaYlFd8e44Kta2sIesLQWwRF7pDZ-lW_UHBH-F9OuUJXOBB1FfbiCJ1RibqaJ-snqF452VaujAF8rVwShBgO3Pk6yq55d_s2H5xZqJ1BmADKlUdgg7wCMYaL8kKomfWkB4F4aY63FA4JZmD_ZrXB_3XfVCVWmlGHdiiwsZmmIxrZdOLcLTU6DWWVfKm6fl0IAFlw74qL4ai0_-dPjszTWYa0THkpBJL_fHzGRBcshnkDDHwcT6yhQb-_h4SsAVMeeYzTPhMhtUFGHL-48vTp_vJzh-paPiVuic2vTSu7ImpBdUH03OUVD0BtmS7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmdjgjWxEQuckLdTv8N3YkIHT3mZ55uTCEXVEUmtjcfR3S65A0FeSghZc-Ylw45bbMoUqmy-q9SR91SOM5Ov5-vW049M9Lj7UBlVvKcH0KXXOZ3DraVoVEjjyCvNdx9F_UCmfjVONHnp1xhDmMBEyQvqL1y4VOCgA8zJyqel-NHIzFL2J2AAHcp57cvhoh6JOWAuIytaYpljmJUqWRJaDdPo0GfC3_JrIfeASDwpXycpqetSMCnQzC5f32nsLm0PZgj0YuIRJUEKMTn2pcinS_jnXxJxPBFJBs0hLFapJvQqs4iKiKJarxVXzDTCU3nV_LkymwNc6qxHFz3hrnn2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxFz44CZ3kCcIgGOUlCTGUOCPURyLb_cAeSaLvPM2ekdL4k2M37l5i5nh841-GHVldDo1VaB0hj9oNWOCYQ9-jJ1TgUjp9BYC-lLGlLhO2cyx2KBHh8guuCpZ5XuVljXTHBGW5gnbntOK6JHOr71R3wTYvKAufMCk4-8McBJ8VWQkEJZ4eItyPPiOkq7ixntWJl33r84zbsKvPaP0-10gZSbC9JRfjJc4AKIgTJhEAv4gmWuwxchKotejflOBmjiZbL4DkcnRrsYtoqqZjnpsxNPAk-wCdhIa1bYa4FSvo1SkBSdvmT8qvEJvlRJCU6hfh7FsMh5x3ichxPd0G-p4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JX2Em57BlV8AHrCHXvQjzSsDaWeE202zmSRAsTfJuGGzQsv-Jh8ge2zHT2DcmIyIgNLjtjcYMybGx2PhoCZpj3sozzZm_mgvUjOxPzGgihLVSe75kGM6KWfLDcqYDK_BsrdkhA5tJtnBE2xykOk0Rp_drzY3sOFcgnoAiWQsNXRD_DbrNC4y1rOgPYrMakY8FlT2ApJlTfrV7P3sqomo1OLUyErcB6gxvreLz5gedLYyhSzszeXYbKAukjh8Aytr0LRJTUgqev5ZiX8AB3rSUdDo5Jfh98HVtj2ccTs-LOj7G-2_DR1jgqjPwmhI_NFCkeISF_fstFLoSOXSasXSlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zi9io86Op95OGkoodVGRmLU3JqldejETKqeEaUeJ7ubKoTMmxaYJdJOd14AF7aUc0pS-FMXOHfIt1pbx-7v_9R0WbCVF2NnVKUmGIPfBI76-Rvqlhs_9aCYqFTNN2-PXR4mdZACdF_nRiuanKKluJG_cZP0AhtPPOHbRl08q11xIV17rrQBpVIh0rfm3ihDeWjNuIGz9RY6dhnuTObPna63n3EYlJkgDpp1w9dbZUfgGFE-zZSevUBEAWt3w1xBT9mYreejg00D8to2OofUi1tZmJnNZhKNxqfd04abFuwtn42WNOWxSkirBwI7fF-loYDqsnJPNqpPVqyyTughrmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbOqLFTONgpyh6AEhBFZCYvICODuqbi1-57QxM-nKM0vylhlD1Xbu8kVKSoYc6jOiVrpCa7yfwADJ-mDOvf7uTmdOcvu86CtedNx_W1k5my9wT99i7Gb8lapq56g-A2fE26KmRICln4BxeoeWP0iaB_2Iu6H5rAzd9lU0R8V8ZDI9xEAJdzEZvqWbfK5rcbwa0ibhgPhUZ8QEnWb94rgDdMLDc0_T6OyqdY1pt-Q9yEPqvLdyI0PKbjtBySSKYHSKWhgoJsh0Gr3EIFSP_mgx2hHxvdfboNGRAOFp2b6oSSipDmbITwid1ru2tCp1dRVCQmkjT4oTztQfyB-qWmoJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=BUFHqGZa96pPBqe8MijflP57_EjMNLrrGFK7WgAjdxw9T7ixCOpLSNd6S3FnGbikDwIrVyFLXO1PDneOx4F_N5qm8bJhcCsIuMnCrI9ulRE0ui-Mm_klRekx0dRq41Af2GQBIgovlcBfGe4HF4UZHf6lpob_onxsfAWNcJorzsvpw7Um3p6xvxGX7SUQRB-Jptmpj1kuC8Ccwd7y4YhL_Kn8uIZpNufJpycPs8l64NfDcnkq6lL-gj3VzMYDQTIjHXu9j9JxO9dujme8L-VaW8yyKt6ruNx_Fc1SGSSUhG1J4AhGTqFsxHz0Ao57QqJ8G6f-FPP0RAGp7q6_DovBEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=BUFHqGZa96pPBqe8MijflP57_EjMNLrrGFK7WgAjdxw9T7ixCOpLSNd6S3FnGbikDwIrVyFLXO1PDneOx4F_N5qm8bJhcCsIuMnCrI9ulRE0ui-Mm_klRekx0dRq41Af2GQBIgovlcBfGe4HF4UZHf6lpob_onxsfAWNcJorzsvpw7Um3p6xvxGX7SUQRB-Jptmpj1kuC8Ccwd7y4YhL_Kn8uIZpNufJpycPs8l64NfDcnkq6lL-gj3VzMYDQTIjHXu9j9JxO9dujme8L-VaW8yyKt6ruNx_Fc1SGSSUhG1J4AhGTqFsxHz0Ao57QqJ8G6f-FPP0RAGp7q6_DovBEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qThh87DnQ2X_y-3_OkCj9PTxSCQ9GEhc1zYGCM3AxkmWRtoor-1KfxXc1Xpi5uugGTjNDOZ0AOfV9JeTzF_UsaUh-wAxTsxzHhgX6yciSQWJJvqlpVaxUYZj9-UD0z_kqnRwXkAPTQefB1aJ1xKWj1qsz5Jq_B3ivni8byuecfdpz10klt508gQ8kGGddJ6MUmZAisNMYrd-8jkwbvX2398kvT74NKuVgGYks6h5Hu79sxmoG8Gc8DfZE8fG8_GNG0IIdiRhTZCnVRFWshaabbAFAbiXoyXESxLgIpy-khsP8csXIdDljkDmOdf3iiIgC1uVChZMPMaCk8_n_Rjb4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNwUVWP9kxDy7Eaca8GmC4fQVzoqjiswqzzhEhCf81zSD2rEZNa0x6EfDV8PYMDbUyroQ1xDuq1WpvYKPAlgVUX26MCP9x4SME9SICHj_CsOBe8uPAWie-LfQFna47uCq8iA2Bkbhc5k2D0onyLXU3gnoGqP4uiCdCgB0TIRZK80HzW8bRhxaWBCFgODM9DpAMu4ECQxLnUrnojppAjU9gLkThpInti1EvmfzUKma__tY7C2qwNwxmGOJDvwksccDaNUWHcfGuxxf_TKNafKyAK3JDMn4ipvtYTY75IuETttjFqWoI0M1DSfrwZ5UeLTSO76t6ZLEBVf-85fPbzEDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btnc9mIDx7sAh0IAO48w2lOAwKc3-U_Lg_5sT0QmttdP-sWC2UClENMSpGvajSMVz5zVB87d5DTT3HF-7FsBQjgw9ONhxRwOH9OGvdAFkjY9jU8urb8ZP60LgFgu_IGh7w73ua6CZIufkPJOitNY5BCqTRoh5Gc25Kg3gJc8e2wZBcKzol9rn8qr0J1j6AhYGNKETOG8lleJ3xU0szJhIV_ecV6ulgLxMV-GmAV3uzlqYNWc4Nbm4eyBBhutrR7e9NDw05nwZG1xxHLApMADDM0kuJIg4zrFJAPuCILWUvX32uqDCtavY0SrG8uPe3Q3lTlxNoFLKWr_u--pJedALQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=VY-f7Fs2HT4ghZt487lmBpN_Dipcj7kb6J2NzjUHwZ4C0Dl_VSc6jwkCRu1Qd-f8_KNI7gW9Vky_KM53rQ9219nc_uJfE5gpXlni_sCrjvdfa7YvwYfw4hfcQzMd7imcJECnbGhHx95WQXlsLPSi25xmV7wAzsF2IUT1TEhVTI12oc83XyzLCTS2n6A4LoZHqsmZnLDj8tgDZYDOR4GkDnrMp-ZrpXvYCQKlJXCg03wN3DR7VMgEuj0St3AGGcqmU4iQs3AlBVFpEDyp_AvafErdzw8sPcleZ7CBgoFfNfDqDoAPCmXX3NPreS68-RE4H6CMFPZ-7fWOt-QmofLzow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=VY-f7Fs2HT4ghZt487lmBpN_Dipcj7kb6J2NzjUHwZ4C0Dl_VSc6jwkCRu1Qd-f8_KNI7gW9Vky_KM53rQ9219nc_uJfE5gpXlni_sCrjvdfa7YvwYfw4hfcQzMd7imcJECnbGhHx95WQXlsLPSi25xmV7wAzsF2IUT1TEhVTI12oc83XyzLCTS2n6A4LoZHqsmZnLDj8tgDZYDOR4GkDnrMp-ZrpXvYCQKlJXCg03wN3DR7VMgEuj0St3AGGcqmU4iQs3AlBVFpEDyp_AvafErdzw8sPcleZ7CBgoFfNfDqDoAPCmXX3NPreS68-RE4H6CMFPZ-7fWOt-QmofLzow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=hLDJW4OKUShavjHhNrS-6-3nvvDQJDbNicCFaic4HK8Sc5vn2Oq6HJoDgjU21YpwaLmYZC2RNWQYX4o5JFxULRSIJlZbosJ4WFQGM2YcyBytVnFYnv2woYGf_LCgf8DcwVXGgIPa5gC9bOM0_GVz94G0m6xGgfYopAdiYcfquVhL_cM00KtmOf8GkPEehXFwKOG9jN5HZ9hWsw6e31Gmf2K2UsHnV8JWENhLoaBk29ihcHmJpqWdnpf-eZqZi5Ajyz5ZqUJ_w-LONFOMq_v8naMyD4QUeIexG6564Eyu9bqMIlvXeIkK7Dil-lX2wuglrOPcr0O5BcqTUC2P9MAXbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=hLDJW4OKUShavjHhNrS-6-3nvvDQJDbNicCFaic4HK8Sc5vn2Oq6HJoDgjU21YpwaLmYZC2RNWQYX4o5JFxULRSIJlZbosJ4WFQGM2YcyBytVnFYnv2woYGf_LCgf8DcwVXGgIPa5gC9bOM0_GVz94G0m6xGgfYopAdiYcfquVhL_cM00KtmOf8GkPEehXFwKOG9jN5HZ9hWsw6e31Gmf2K2UsHnV8JWENhLoaBk29ihcHmJpqWdnpf-eZqZi5Ajyz5ZqUJ_w-LONFOMq_v8naMyD4QUeIexG6564Eyu9bqMIlvXeIkK7Dil-lX2wuglrOPcr0O5BcqTUC2P9MAXbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=bugE_Iwvqjr5ZEAt_KyNBx1CfIpG9dQrf4DMnhrjwsw1_1QmKPqKg2rOAdZY4GIBeBRqQT_O-LAoqnwhr1c3PoRGnFUMPyVDZdonavzyIKepJxy9J4YgwZZF6Q3dWkz8e0MH9sfqaPHFt0CVqbd3qpANORSK7zgRhJakrcr2Q-p7iyIFqP19A80-E22_4AP6EpJoWwd-dEoT2gK5QcRsfocMbj-GsDqv-qc0iLv9_VBjQ6GA6cpE1i-zk3anzIaz1iIBCDVCQZHL-kqSTNFAEFG7WMHJzE2_YUfQQl4KLXo6A_w3OZ_V2Hg7QVPh1H-ByehRrGLZxFpGFMbYeHiQcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=bugE_Iwvqjr5ZEAt_KyNBx1CfIpG9dQrf4DMnhrjwsw1_1QmKPqKg2rOAdZY4GIBeBRqQT_O-LAoqnwhr1c3PoRGnFUMPyVDZdonavzyIKepJxy9J4YgwZZF6Q3dWkz8e0MH9sfqaPHFt0CVqbd3qpANORSK7zgRhJakrcr2Q-p7iyIFqP19A80-E22_4AP6EpJoWwd-dEoT2gK5QcRsfocMbj-GsDqv-qc0iLv9_VBjQ6GA6cpE1i-zk3anzIaz1iIBCDVCQZHL-kqSTNFAEFG7WMHJzE2_YUfQQl4KLXo6A_w3OZ_V2Hg7QVPh1H-ByehRrGLZxFpGFMbYeHiQcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=KsqgnhQwVTFWg22sUEn-UoucIN1F_cSaBYS-yUCBF24Be__0Mq0KjW7iF5s33MQLU3EkvCSWuq7hysA8UmqzryGxBrOpxbjl-cbHUWX-U6UptcRNC3AzM5XQqmBh2SDeepuuZ-CMd7qiQuSg_vOypD4SlzXCNcoPW0iEi_IS9Nw2wqyBUxhVU5hqYsvt5X-w8wunXPlggP__Ee1s_lwwMspbfDaJ8eqMSFXe3G6uLy8qXWcd7H6N1wtvAkcsGBje7t8MSTrUu3d08Lkq3wRN1L25s0vxa04d1nrFkP6_JgIi_MAktEmjQZxAEjhW2G_OdtnbE1JODCkmR1hm9D5w-Gmk6SiQd0joZc2XJhS5OinDI34BEqouLnuoH5effevQ_XfRJkJVCjGdSaq0MFXO0G_u_W1Ad8eXLkU998DC-OqOr3hsoBLtfinanZYBmQU-puw5CYFOW12mNxf8l-phqWxeDJr92m1JLQq3diWHlgXL39ROc-hARD5MZFt3NJwqt2JWP96HNq_xGePtg6SShU6cWg5Ver6ojsz71lD6o2034lZDiydUHALLaU08zDGtBsjswf4uQqGXriYBd_TYUwVlcvZUZ70_CuowxOQhyeAt4XvylEPc79LCjhjMwilrxorIkM8C3UDwnh6J0FxW7L7cpgwV9EyXG2oE5Qzfl20" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=KsqgnhQwVTFWg22sUEn-UoucIN1F_cSaBYS-yUCBF24Be__0Mq0KjW7iF5s33MQLU3EkvCSWuq7hysA8UmqzryGxBrOpxbjl-cbHUWX-U6UptcRNC3AzM5XQqmBh2SDeepuuZ-CMd7qiQuSg_vOypD4SlzXCNcoPW0iEi_IS9Nw2wqyBUxhVU5hqYsvt5X-w8wunXPlggP__Ee1s_lwwMspbfDaJ8eqMSFXe3G6uLy8qXWcd7H6N1wtvAkcsGBje7t8MSTrUu3d08Lkq3wRN1L25s0vxa04d1nrFkP6_JgIi_MAktEmjQZxAEjhW2G_OdtnbE1JODCkmR1hm9D5w-Gmk6SiQd0joZc2XJhS5OinDI34BEqouLnuoH5effevQ_XfRJkJVCjGdSaq0MFXO0G_u_W1Ad8eXLkU998DC-OqOr3hsoBLtfinanZYBmQU-puw5CYFOW12mNxf8l-phqWxeDJr92m1JLQq3diWHlgXL39ROc-hARD5MZFt3NJwqt2JWP96HNq_xGePtg6SShU6cWg5Ver6ojsz71lD6o2034lZDiydUHALLaU08zDGtBsjswf4uQqGXriYBd_TYUwVlcvZUZ70_CuowxOQhyeAt4XvylEPc79LCjhjMwilrxorIkM8C3UDwnh6J0FxW7L7cpgwV9EyXG2oE5Qzfl20" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=FdoEuZWTSSgh3yQ5uRUv29pJqPzqFKO9CCcjV4aGyM4IosZLHGmO2e5vNxabkGr9Kdj1bcyEZhnVs8G_JHULI_oD523W9R5x8h-6FBujAZhkiHHR6spiiSDWiEO5-Qdg8wk6o1jtS9YL3v3ocjj5N7_LM85fyHsdXN7BQ22yRsa3MpEamqgEdyaXXXgQGF0hpXU01zRbo7rbSFIKmMDi5i3o9tliH_N86HetRub5bAZJSdOKBLYWkJ40vGLrZoBMLGfU3pMH493gu9Bj6hLLorMrulhhLj14Tm_v64GNAeRWiPzygDfbPqfi0LbN57Nrlw-zyLDvFK_auaYSHXYDUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=FdoEuZWTSSgh3yQ5uRUv29pJqPzqFKO9CCcjV4aGyM4IosZLHGmO2e5vNxabkGr9Kdj1bcyEZhnVs8G_JHULI_oD523W9R5x8h-6FBujAZhkiHHR6spiiSDWiEO5-Qdg8wk6o1jtS9YL3v3ocjj5N7_LM85fyHsdXN7BQ22yRsa3MpEamqgEdyaXXXgQGF0hpXU01zRbo7rbSFIKmMDi5i3o9tliH_N86HetRub5bAZJSdOKBLYWkJ40vGLrZoBMLGfU3pMH493gu9Bj6hLLorMrulhhLj14Tm_v64GNAeRWiPzygDfbPqfi0LbN57Nrlw-zyLDvFK_auaYSHXYDUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=iCNiZEGiOmcAPOPHIF_9cEtFcQHFUDGowE7Fao4KWtij-DU-PSkrlI9P3BCss_UmcC2MvJQLUB-2uPS3r0IcZJHeDxAzokdY0OCi0BI5w86pDsXffVKKRFF47tY7DA7ipYLCmdnKWzJ-4hMybHkdf0BGcvxRFGP-HVpPQKpD86fKEcK65oHTshFnFSel_O74aNrhWXRw2mqbYk4nM_rzyehRNx3fj8quuyUJt6UxuB6Cc3LljEP64HipMculHjaCPAXm8bR2cLIZxaU24780fQcSkJjFcQ3c5U44Bko2NR-PjRIcLJSFSJf5NbzFZ3-4zpwS_3BnCnF4mXvM9pPfmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=iCNiZEGiOmcAPOPHIF_9cEtFcQHFUDGowE7Fao4KWtij-DU-PSkrlI9P3BCss_UmcC2MvJQLUB-2uPS3r0IcZJHeDxAzokdY0OCi0BI5w86pDsXffVKKRFF47tY7DA7ipYLCmdnKWzJ-4hMybHkdf0BGcvxRFGP-HVpPQKpD86fKEcK65oHTshFnFSel_O74aNrhWXRw2mqbYk4nM_rzyehRNx3fj8quuyUJt6UxuB6Cc3LljEP64HipMculHjaCPAXm8bR2cLIZxaU24780fQcSkJjFcQ3c5U44Bko2NR-PjRIcLJSFSJf5NbzFZ3-4zpwS_3BnCnF4mXvM9pPfmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7uePF0HEc5b26in-9kk6XPhuBpStOCTPnvqjBHzzRkLRSkoraH_XsFY9dt_7oc3uReGkh1Lo83DBpTslnYLtUo_pme5UDPWVT8OpqtOr_M_UinKob5BxxkVHY-_4AhgcawROT-veqFv6rLf_GLzUTU8TFzooqujx1KCz_tIzdrKpehtwlaDfsHM31oBOe1m33664Bxe75TFQNHByve92aiqOlOKIrWw755IM4k3MQ7aqQWBrf48p4ZCPfJ3IG_CUpDB8O3Ya88wAAf10EP991c5XASeBzTHaHVSoKSaX1uvbkEFTyQu5XdgFm2g1YN6jkloXhAdTjGkCniqCwH1ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=b6qMRse_IbVvA9LRV4dIzaZEFNNc1EMOumK4KnAPXKHr57SqqrdFfhI8Rm6mkGhJXTW7RgLaaaMDcX-jHrgCATAOMyXTuNUWCwx7d8ur6ft0dWiEJgxZ5rCTuKFBQQX3Of22MpyBEvghp7iWrHuEpWXtyc1m_SSTZOJOpPsYQDO3bRw60-gZCmJDeiFF6HasMvQXejOvNrYx_Vwe6m6EUeMwjtrYrqmA9nH_-q4nEqHxQKSrEhLNtiu2owPo4Mdi5VyEcZRcAovOvM6k2JMvErePxA693hIXKWf643pSY2PiFLjfgEYqWGSLgmvqng0dLwDJwoZTwQiuE2kBkyyEAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=b6qMRse_IbVvA9LRV4dIzaZEFNNc1EMOumK4KnAPXKHr57SqqrdFfhI8Rm6mkGhJXTW7RgLaaaMDcX-jHrgCATAOMyXTuNUWCwx7d8ur6ft0dWiEJgxZ5rCTuKFBQQX3Of22MpyBEvghp7iWrHuEpWXtyc1m_SSTZOJOpPsYQDO3bRw60-gZCmJDeiFF6HasMvQXejOvNrYx_Vwe6m6EUeMwjtrYrqmA9nH_-q4nEqHxQKSrEhLNtiu2owPo4Mdi5VyEcZRcAovOvM6k2JMvErePxA693hIXKWf643pSY2PiFLjfgEYqWGSLgmvqng0dLwDJwoZTwQiuE2kBkyyEAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWl6tTkfsgS5fnwU16MMS71Hg3R2ekm6kShCxzXeT9KuXA5GPpN5EJjdjAv5GRa3tS9D6-4lZRrh87LiV_GWb3_j6Z5q-Agrmwh9koA-s8nQrotqrIVl_cEQt0N_nFIWIGOZvIa8_AllVbkiJ41l8B2fwblpETy9_Nrvh_wUjTeRs2bjIkZM9kpbrpRy9tePWL8ioj9pT79Y-lzCnah2d4SYYblfoetYmpDdnVSuOMptYpv5qSczMlG4MJj9QN6O4aVuwWhTntmz7kq7VgDjMQi-67dPD6RBwqcBAcBhyLOB4Tv4095W62U8ZcnGSftP7X0MKlBxtQdiTQTk0UU0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7mf12pC6oxH9cXPoqMuelB5qErqUVtI5u7C7uw7tBiHYa1OmAwoN9zG3Tw0cGN2oIsB9o8Wp3DC26inktX0fRcPe0Wk1gCrz-87D-Yb2fLMKqVcZBkwoYc7V9D_YRaBxqFE_zJHM1lvHZ7Qa4pD0yuQdvAe0RLs3Z_PvFTuog--6wOq3qBGxhV87bFUeQ78A5M80n97XZdxEqMmhjx-n2IBCWzkjfPWvpNczu5M8TlG_atgMXDgcQggC96zTHWlyujV4iqhcj1NUYgMeqI0gDl4u2MFP21ufojhSwE6UtFneMeGkjRoxqiiFI9kffuWL9DE6tOh6DTVrhhldg2rVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=R5a1LLFatstUnRr8TElLYeEq0Mf8dWC20xV8Fu_CeBSayHTm_d153XrOtwZuQ_HD25wnfxVjwOH4QGKc0eyes14_3CuXBIGl0k5d0GVvpNOXpgT2VHkbZxARhrqTnQmyfXXUyFY4tHz2QCZq1hJRbOb-YGw-g-ahuo1enwUIXb3Pja2hYWodEQwYyFy-IpGsZcN2NsMWc9sqqT4zkwdsAnH1F9OQr1QYK7YbrLwPdjAkaPSQI5-269pNEGAzkWcvl1l8Fatup50v0J1VuueIu2ObbGYJeTnW2lbeclW-RmEcECxtFsSPbZ0F5LRODmtfe0g26p0sROUFnVHXZO9L4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=R5a1LLFatstUnRr8TElLYeEq0Mf8dWC20xV8Fu_CeBSayHTm_d153XrOtwZuQ_HD25wnfxVjwOH4QGKc0eyes14_3CuXBIGl0k5d0GVvpNOXpgT2VHkbZxARhrqTnQmyfXXUyFY4tHz2QCZq1hJRbOb-YGw-g-ahuo1enwUIXb3Pja2hYWodEQwYyFy-IpGsZcN2NsMWc9sqqT4zkwdsAnH1F9OQr1QYK7YbrLwPdjAkaPSQI5-269pNEGAzkWcvl1l8Fatup50v0J1VuueIu2ObbGYJeTnW2lbeclW-RmEcECxtFsSPbZ0F5LRODmtfe0g26p0sROUFnVHXZO9L4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=og4hFETU0S4sTIKk9-LitKeb8DgNGvKAQoBBK88IQKAboFm4IeOaesuWMtpa98qb3suJoxZdHcmiGLT5n_4LxvAuOg4-waNYIprbcP8QuOvR-_CJxMxhxN-PebDoVStfqcX58JYXWGPCW5fFjcTP02CXwAPuUrutv74GCc9y874dcJ_7_yeOoZCgSJB5CTLN42HvYsPTv9qouwDe-n2Mp8X7ntXlbSZRspwvGGOU5tXg3rqe0FgvKbrK50p5g0IHrPYMaFEPU57USBD1IXCSc5sT9Fj6fg3hoHdViIt0GotAsUPKCRvM8t13nIF3mgH3pyxxb-mkCKtBMtRyvwA1sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=og4hFETU0S4sTIKk9-LitKeb8DgNGvKAQoBBK88IQKAboFm4IeOaesuWMtpa98qb3suJoxZdHcmiGLT5n_4LxvAuOg4-waNYIprbcP8QuOvR-_CJxMxhxN-PebDoVStfqcX58JYXWGPCW5fFjcTP02CXwAPuUrutv74GCc9y874dcJ_7_yeOoZCgSJB5CTLN42HvYsPTv9qouwDe-n2Mp8X7ntXlbSZRspwvGGOU5tXg3rqe0FgvKbrK50p5g0IHrPYMaFEPU57USBD1IXCSc5sT9Fj6fg3hoHdViIt0GotAsUPKCRvM8t13nIF3mgH3pyxxb-mkCKtBMtRyvwA1sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=qaOEFdQGQ3Zkbo25V8B8SGITNyzwzEmJ-Xcvjy2mbwXbFGgB8cxPqcJutGCjnvAqVJ5isXAdap3JSSnLehUxm1baNoUIYFC-6xvg63URCwvFSFui9OV2HNnSuKnK2OearrZFKcWvwTHbbSH9Lf-PhaCDZun_Dz_2VY84ehxe1nHVZW9GRFyaYbdiYiWXb86L2D8rLrS5V7ngvmQhrQbt1xaPhyVmAp37YkPq0LJWfGdU9xNM3SPTfLi92uw0iaNPRqk07YNyiR8bgCqnoF2T3Mrrzn5JVJeFcRvWmqcH8C5UJCYWJecMiIrhKGokHLxwfA7844hCxyJIK1ljOHY6uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=qaOEFdQGQ3Zkbo25V8B8SGITNyzwzEmJ-Xcvjy2mbwXbFGgB8cxPqcJutGCjnvAqVJ5isXAdap3JSSnLehUxm1baNoUIYFC-6xvg63URCwvFSFui9OV2HNnSuKnK2OearrZFKcWvwTHbbSH9Lf-PhaCDZun_Dz_2VY84ehxe1nHVZW9GRFyaYbdiYiWXb86L2D8rLrS5V7ngvmQhrQbt1xaPhyVmAp37YkPq0LJWfGdU9xNM3SPTfLi92uw0iaNPRqk07YNyiR8bgCqnoF2T3Mrrzn5JVJeFcRvWmqcH8C5UJCYWJecMiIrhKGokHLxwfA7844hCxyJIK1ljOHY6uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSrp1NzzbGgYwcu_FVG7ZoC-kOX6AZ8i6jN0g9Sd_9Kvp_iibZtTP1sa5bDz1fLjtTDiSce9DSgQHDjZu4R-phueGWIgO-b5n8jTSm9aT3OPjFIHeWHPeeXw9t3HMGUq4qgxOEuuByutgGUGslVw41GMclj01qEA9OW5mXQxRZ2iIkSRUxBRznWlnu0dxtyI_QK6GHiAfTOuI8o89kUrZzx8Qsu2r-EBmspPOGQmU-r9FlXMB2OBZkNbi-3LDg4gqkC7lnzWDZE8m4C6BPxMK89UgsJ-ezj1W2ZBp3onEezjHrOX08eaaVcEY0abj60YitQNJga90U1yzoRfwfRZFg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=F9aLzznpAqgek68hldk7TXR89e5ek3K54ru1jFOJ7ceV0wxxWbB3gqkP3x9aGDb__mPkA4XAdu4Aj0M2s7jRKXDKlwMnJDDIzUazrNmDytk-jJUQDZ8SSO97lJNjzY_6LAfLOi3EQwigej19ZrrfSEiSKfWuL257ne3c_mJRWojaVQnutRZLP7dXaPP-fzN4uzIFJWUc_RAw0nb9tLjyDjgoLgTYOy-MiZOug9aFdlNIF_0B8kHJUJyOy4UOkvYas2HYCYJqO5Srng0iBiZbOCWKkAPbF5u3uaSQtN-1H4qOrqt_wCrEBh_Tnd6v0wSRtexZvLftydSr2AopdaonxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=F9aLzznpAqgek68hldk7TXR89e5ek3K54ru1jFOJ7ceV0wxxWbB3gqkP3x9aGDb__mPkA4XAdu4Aj0M2s7jRKXDKlwMnJDDIzUazrNmDytk-jJUQDZ8SSO97lJNjzY_6LAfLOi3EQwigej19ZrrfSEiSKfWuL257ne3c_mJRWojaVQnutRZLP7dXaPP-fzN4uzIFJWUc_RAw0nb9tLjyDjgoLgTYOy-MiZOug9aFdlNIF_0B8kHJUJyOy4UOkvYas2HYCYJqO5Srng0iBiZbOCWKkAPbF5u3uaSQtN-1H4qOrqt_wCrEBh_Tnd6v0wSRtexZvLftydSr2AopdaonxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=rpOlrOcJWBhGVSjtj3y07r87Q_F67BQ-4Jn4KFOQCsIsQ786jdiCwoBjjqQollban4_ZVlNC7WVeyorko6-8HLNKPm0mQ86zxG2jr5kNpv51_jUalLCziVZshj2iD0q-8MZEdmjE32zbVw7YZ4RrVMVqnamSCNijx69P2ti14moB6XeXVocr1QrEgfDhVu5dsGwkwr8btNZ_i6k8vI0bCZya0UQsF0iw3CC6m5Ji8ST8abNUrBklzC-YOi5G-IXCnsNe_-tEllrP5r51K02yjUgG4iseHKRIZf73jHNmXpo6gtlCwCAhqi0KpMSaquLgTqUzcZWaQgFlx7ZrI6G1xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=rpOlrOcJWBhGVSjtj3y07r87Q_F67BQ-4Jn4KFOQCsIsQ786jdiCwoBjjqQollban4_ZVlNC7WVeyorko6-8HLNKPm0mQ86zxG2jr5kNpv51_jUalLCziVZshj2iD0q-8MZEdmjE32zbVw7YZ4RrVMVqnamSCNijx69P2ti14moB6XeXVocr1QrEgfDhVu5dsGwkwr8btNZ_i6k8vI0bCZya0UQsF0iw3CC6m5Ji8ST8abNUrBklzC-YOi5G-IXCnsNe_-tEllrP5r51K02yjUgG4iseHKRIZf73jHNmXpo6gtlCwCAhqi0KpMSaquLgTqUzcZWaQgFlx7ZrI6G1xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=iN8K4Qp1VUJyQbYaIl-3cI9IfStyugWx10Ye7tm5zOuBQ9W6n0eqAdm-wTeQxOd97xmNi7nrBas2AN0mf6HFMOTe0StPTU2O4mdExD5eO2y-Hc6-3-FrLmmzw4XB8HUFtnuFQAN6hULoZOR3j-8Ws_79MXYkPwBjDg2siAoL4dvCF8pUP-2Vfo-jpFyG1LOD6NMpeBldLgj3JBd0KA2_r-qZrQAdPv3tURzobQPCd_AdkSzsQaCMgvK98ZsW9R9PpH8ws1LbBylvZyXeawlWzHzvj_WRW_WRZF5sbV3xcePiZ3OiFGmCoN0kDQYwWSFzXhqedxuYQVJiUcUOCu0BMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=iN8K4Qp1VUJyQbYaIl-3cI9IfStyugWx10Ye7tm5zOuBQ9W6n0eqAdm-wTeQxOd97xmNi7nrBas2AN0mf6HFMOTe0StPTU2O4mdExD5eO2y-Hc6-3-FrLmmzw4XB8HUFtnuFQAN6hULoZOR3j-8Ws_79MXYkPwBjDg2siAoL4dvCF8pUP-2Vfo-jpFyG1LOD6NMpeBldLgj3JBd0KA2_r-qZrQAdPv3tURzobQPCd_AdkSzsQaCMgvK98ZsW9R9PpH8ws1LbBylvZyXeawlWzHzvj_WRW_WRZF5sbV3xcePiZ3OiFGmCoN0kDQYwWSFzXhqedxuYQVJiUcUOCu0BMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrthQ0Dc900wJfEcS2wzrifB_2RhcYMOcgCmgTXCeIJoA415EFZSJkaTc0740j9aL3Fr3_D9ardegzttupNdAWDF8aCF06jUl59y2Bex2sYunskWoikr0xVUlNTBeu1cDIosKKaMT2waBoVBu7mG3m2xqOmkkO1CIuWjCQ9mjHEuzPQjHVdIWfi5ySZXQxDI-IjZWcILBO-YV7YtUxJicojh0WO9dH_bLLBjiCBatsU2Mzb5V3jnK9-w5w73ccTuN4r_Bbc1HIr1d9iVCu67NqrUJuWFdtPLTnfrR7irWdCIWY_cvdVa_N2ME6B2BDg13moMSfIBFd1ZEX-cvn1O4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=ZjFpPtczVd1yruYrV1nFQrqK_gmGQu5B0YFZJnFDw5DSpM3ZRrL1l7M6Tzu1lymoNGO50d-fAJE9zbhJdoJe6uZaCcmEKhJBUC1avGCVsGKUyD1d7FP15tPIZ4EJVlX-MagLqYNmALQ2aDgBBTRte5YXG40wqDHKwyK8AfGOpSaOqUr5qTytHQfQp7oO0wfyh8JGg1tMV0nzCvcCzitf9JxdY3F9jdg3h-5Vd6qXF6s_yO3a7ZQMl_skBE7rDeGlPr8f9d9b5_B9GoHXOVWT5q0afFzczeyoWjpsD5R46ScXnHDT2uy9z8intCtQqKk7aBazB8BGeFvKuuAz27pltQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=ZjFpPtczVd1yruYrV1nFQrqK_gmGQu5B0YFZJnFDw5DSpM3ZRrL1l7M6Tzu1lymoNGO50d-fAJE9zbhJdoJe6uZaCcmEKhJBUC1avGCVsGKUyD1d7FP15tPIZ4EJVlX-MagLqYNmALQ2aDgBBTRte5YXG40wqDHKwyK8AfGOpSaOqUr5qTytHQfQp7oO0wfyh8JGg1tMV0nzCvcCzitf9JxdY3F9jdg3h-5Vd6qXF6s_yO3a7ZQMl_skBE7rDeGlPr8f9d9b5_B9GoHXOVWT5q0afFzczeyoWjpsD5R46ScXnHDT2uy9z8intCtQqKk7aBazB8BGeFvKuuAz27pltQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rK7oxIMKjd0wcCqP0z1FOBGG6aXqJRy18Es0x5dmEpccaQ83wVtaMv4cVf1eHQAOphQz201a4jduHBMma64fV2KvFKmZ7o7sQXuj2OdK7D0Ad4bn8rnR16jsW-V0FQ1ccSqTxO8Yc_CL4z7RbkqtVkAkG5Ue58KLOnYo6YpnLOQ9xScSFExNTIyqbBlMoseIweQqeJiFKw1lyP_Zr4-A6mYihxskzalr6GUCYCLDVKOIsMR9tMKK8DM-t2AcyeXXlWzA6J9TnWtTYhPX9oVcQeQIb-68Ki8N8xl_h5qe2vYnu_pEtuYBofB3b5UB7SNxuxN0hXsZEcQaqS4KOEdGvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=a8xdJXZqstfpyJE8CVZd1Oj8Kr8yu7OK27FMQFW2slz3mO0enSelGEA92OmFrFGHpxBxEm2dn-y5F5HnLOOpSncLUoJA8QAtX-ZB312ybjSm_Bg1WXGuWQwr7Sf4V3a_yw0LAzxENwJ5JJGvkfUyIeahfAqvLtAhwYjjGrm4jnrP1YsTFj-OKoYKKzMhaSf3LdqfngXG4m60Y2gVh0k5WP6mO7Q8K5fEPx8_G-Y012R75E_uROz6qNiXHiNjKUspq1YnMDnXO1lZIFSzJmvBG8VrgWdOA8QMTXzp3wGPCwiGViyHOp_aec2sZGFZf32Gow5X72y2b-eEIB0xIbDEZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=a8xdJXZqstfpyJE8CVZd1Oj8Kr8yu7OK27FMQFW2slz3mO0enSelGEA92OmFrFGHpxBxEm2dn-y5F5HnLOOpSncLUoJA8QAtX-ZB312ybjSm_Bg1WXGuWQwr7Sf4V3a_yw0LAzxENwJ5JJGvkfUyIeahfAqvLtAhwYjjGrm4jnrP1YsTFj-OKoYKKzMhaSf3LdqfngXG4m60Y2gVh0k5WP6mO7Q8K5fEPx8_G-Y012R75E_uROz6qNiXHiNjKUspq1YnMDnXO1lZIFSzJmvBG8VrgWdOA8QMTXzp3wGPCwiGViyHOp_aec2sZGFZf32Gow5X72y2b-eEIB0xIbDEZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovIlb6Vd-X2qtykLVZeLGroHP89BzOaXevcjxwi6fQ1kiy7aoo6rPSTTs-NN01tYhoDhZ6E8fcVCpjdbl6VKNDgdCawLM3KRBCUBf3829cH1K-Wbs2SQVuhAOBdtEf1xWaT5Nj5dBy3li6U7UcDA8Jg6Bh_0N8TN6KyI1qn9XiHY_fLVbxrFWzUT1ZcGH6IQKx_NbpntHyAo45SdBg2v7eBRj9Vb6mt0-6YGmXzzjJyzEFHCluPy9igUuYOdjU4ZSxxaDxxfHYUAmdTuQTVlf7vN425aPAcK4wZckJt7tUanh0fF-6T0d1yCEB8FPUbdkRwZExIL5IzNmzHbrgiW4A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=Y907mt_OYj7u-1XUMzzj_5OGRPvpAmLTnFWZGMohHA2eDGgIKR1ejmbYc-DlmW-XgkB-aWiJPsq3TaO6xkRQxZdIbxW2ZyY4rcfjnfQ1p9Ukdz4koCnUvLhnPg6a66dAVwtB7WiKNeIz9OFTxjBo_cWms9SDpnsVf7RtWL_DGy8r788EowN9F9F5ksUhoM1sWv07ILD1Z9mdXFdzyxuLoBmPjslnmNgywTNjX5Rh_wLWn9vdysBWcXpnjpSyCeJ1zUfIK_lCeFPNp-7UP-p7n029sYi4lgdjklPkTA0eo1vLE_7OhfLupKpiJpff4YSpcGRIWrOJVqabifkC8o88KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=Y907mt_OYj7u-1XUMzzj_5OGRPvpAmLTnFWZGMohHA2eDGgIKR1ejmbYc-DlmW-XgkB-aWiJPsq3TaO6xkRQxZdIbxW2ZyY4rcfjnfQ1p9Ukdz4koCnUvLhnPg6a66dAVwtB7WiKNeIz9OFTxjBo_cWms9SDpnsVf7RtWL_DGy8r788EowN9F9F5ksUhoM1sWv07ILD1Z9mdXFdzyxuLoBmPjslnmNgywTNjX5Rh_wLWn9vdysBWcXpnjpSyCeJ1zUfIK_lCeFPNp-7UP-p7n029sYi4lgdjklPkTA0eo1vLE_7OhfLupKpiJpff4YSpcGRIWrOJVqabifkC8o88KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bDm29vFSQGaBZ3jSGNB0h_zdFVpT1jw81CTRhFNQedfzH__b-ulxs0f54IYrsNIkKBehDweT67SzlQP7T1_QlGNQVxruZ3mA72fOLOp-KTwT0yaNDK9h20D2tOeVwi3czL2ERwz1JUY31xGluvqdxHd_DVam30YF0KJGXgxbcKW9PbctD9pVEuGKmG00HN9OMMHGmszEtsefDGnfKQiKflZthMwQ_gs4BMWcW_1A-BdQ1RUp-JCJNiKnXZi2j__4vOwj17kEmJTFHYari_XNQcPI3KfWsWf5IAvCa6jFtjlJepJIfK8pfIWmrHAwpmLwQLBmHGoGH-3enKqisSgzRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ng6oc-YNjgDUf3Mapfn4L12aMm4knyBmW5Xir2K2pabj0xZ9inijxicd7wun7OPx1qge05MFiJJ26MiScVJiGQDnpee-0XCJw5SY_QiicSpc-m4R0DGyQV07LAgF1EBxzoMjqls3qOVcvspnC6WG5XTyUIEHVR-XI-n0aEBOjV7Nw17mLLbuMHcLlOzPfKFbj9kuwSCkIgyk6Y0njMPnFvdzAk-vBSQ2RYv5u1mHlVu7NbzZC1Bt4c6XmsgiWNvB5LPVTZt_KnpU_uS3uJlEP4Y8802PW9qgD3by1mH7mf934qlTGk_InY94LKxeFb4rAt0sNTsjLUKB1ltiRsgBeA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=p4CXVXGGvAmWojw6s85Am3VO0FgB4lSsxlwLLxGaJI1tYrTPgntFaNX445V9DwJxcnpOhRiG9zFKGXThqjf6H2J6jA-TJMzsPmQsBnIPGC4r8sveOYFDn2QAl5r2Pnf5GegFns9ZQoylNe45W82v---Xpbi5Lfg7sg3cDUchq_3t0wTCjOyD9fFR2YK0X51Pcc-1D4le0WiMO1NdwcZBVDi0gRrhJqoMIgIGfjuNWm4avBWb_KrvlWKdreHqnqG4eksrbAKJ9CrCIBmKVqEPLIFYNgu4mzqVs2vXtS4x-E5PDlf0lW1qykHLx8EHN-bHvrGdb3LAQCKXy_DIBxiAWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=p4CXVXGGvAmWojw6s85Am3VO0FgB4lSsxlwLLxGaJI1tYrTPgntFaNX445V9DwJxcnpOhRiG9zFKGXThqjf6H2J6jA-TJMzsPmQsBnIPGC4r8sveOYFDn2QAl5r2Pnf5GegFns9ZQoylNe45W82v---Xpbi5Lfg7sg3cDUchq_3t0wTCjOyD9fFR2YK0X51Pcc-1D4le0WiMO1NdwcZBVDi0gRrhJqoMIgIGfjuNWm4avBWb_KrvlWKdreHqnqG4eksrbAKJ9CrCIBmKVqEPLIFYNgu4mzqVs2vXtS4x-E5PDlf0lW1qykHLx8EHN-bHvrGdb3LAQCKXy_DIBxiAWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0s3aHkf27s1ZzVPqF5wISdBm1xPteRUpACqEgTOMEXEy0mvtXHtOx56ugkq-9LyRwtf_nRBJ_riimz-aQQd5XAif8U8s86wvwO3wk5VeFJZVttrXFZI2iggwWPFUae3WF_AekS2dGqnj-W9Jr0x0d_QHEjqkV3FBm6ODYNNRYOP6nSA4OaoelUz7h7hKfUUEVmil_z9_S3UUg7QXCKgOf1T2eGx7_YBJNGFocv_sYU1Izfw9OTlO3ls_jLv75dCrZXbz5mu4e2otcnCCdwMzTA89RU65q1GE9gAiLboRt-t3e27wHwM9_hys9nm9iCpmPp3-nl10kr1SX-_BPi8bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCqBlj2vlDlOvEhnNFJCPozGDSlsmEzFWlKDFqN-8kImJf9BoW-e0kBdDIAgiw4pqwNacCRjYnzBmAuI3gwx7o-y8sZd932e1HyFPQcsYYghLtd24ODFA56q-lmJLKU2GiJGFSBxQgWwoETcrIWkKAxmxZXPfpyBmHsJZvIcHkr6savBsS0tMNbNpJPbCyJzCB3a-31uShOqTmXOEEkDFain5893Hocq9mAfSt1XdqBFTxGssc3Y66ZJmnkrSCgws1vWF1jLMSwZ4jqrzfPVMIgXhaTsXLvOUDturRl3Ds0p6BMF97m1A6lacaoo4R0NrcPDIqF9tvpCzxmF4Pv04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEeyRyFrnMPcB-bGFbbHVZt49OZkTBRMLJdn0EZFnzSlFOICVNScG4Trf2p0MnT20NFyBJ59VWD_o5VSiV6IZPuestt2_UZZBzGp7pOn1cNhGWq7EThNNqtytpeojK4PUVcGtcbgfQ7XJ90Wzu-Mue4EbUQhHTkPjPOFthRlyux0VYmcv-eWYd7XCqrk1eEMyJpjVRGcjoxASUihmMB6ebrFs3Z1pCWVFKM9_6sAtWTEMKvCoA97MACpVTcYZm0ZTR5jmVQZFNJrGN4XR41e7X93cRtAafjNOMVb5CCasZdqZVQkHS2roTqBR7uJHXKUIIofC2NDKlVw4UnAzlbZMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGvmtQ1n24CTm-droi8WfywCd7rTZHCzgT6u6l6FLzg0RsFukZ2utt1ZfrgNbtScf9VsZq0pkNMtXpgBwAxda43uS6EwDS6j2K4L6v8taMzFgUEUXL0WKeTggXs9rfJCc1J9GwUr7O4Llc4MhzMT8vYz6eCmm_juXU4OAkZ1oroFMpAlkYw6xHDRuwKvz5xbo41wdF0Uib8PeDM7s_Ra1wuhym3Lnkiv11M4tqBumEqJlKZrJk4dMfbIpetB6gUUstpTi7EWdhGsnJ0lDB0R7neEGke7JczMjc5w5BiApB1mTU4ZGAJlergt6A8wbGaNJES8UkSie7arn7Fo9lG1cQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGwnLpg7IGt12tKd_EKhCzhh2oCtga3U4Re4lEZ21jLrt2_Wx-e9UXYLqthosgpynVLHMbmXZpAtd7lKxkf0-6s-LX03IjDNl2Rg6A5xssaaORgHIr8hDpvnA6dKgH1kKXGYSLkJvGmWUDH27vgho6FbQubzrdF-x1g0dfC8HPNwcXzYifvEHfm_rxFss2ceN_3mltZOCqaJ6XYwqO5P671rvnYSb2mfT2B7jt3o44YpUwq1t_O1G-06VmzjqJyT8Frh_gRMbDNELyOI4xEk8Rhr5vKsoeaL2qHeOeLXoiWvdM9wcY5TmfUvkk6EFv3xKQb1TX9zU8DtqMBfQwlKaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=s1-HdBs05mMEVHQv9mfA8fyM1hzFw8p14XgciVrWSBOzJQKFwFzJ8VetT13YIKKjz8-EjUNO9MItKvRZrMR3-DeyN0H90J56DRflWt-x-1wThmi_1xwiDa0A1MimodNt2GoDm5hDbGNkMRqRk2H5lWOV1OX7b4VHEJLpYyv8r7RgffedH5u9oVNwoP-cnC62nXUBRv3jv5V8f4_YH3IVufJsqRj7ZOJw6ofYH0eavoPxhG4GDoPbM8AFLIkvjoERu8P8dxQuQTBV0xQDpyPbpVzK7w-8iImN2Zp7EalpPvTRGTeEYOj6Eq_bTF5PZdYMwKwerEQshkU4wAaabDXtOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=s1-HdBs05mMEVHQv9mfA8fyM1hzFw8p14XgciVrWSBOzJQKFwFzJ8VetT13YIKKjz8-EjUNO9MItKvRZrMR3-DeyN0H90J56DRflWt-x-1wThmi_1xwiDa0A1MimodNt2GoDm5hDbGNkMRqRk2H5lWOV1OX7b4VHEJLpYyv8r7RgffedH5u9oVNwoP-cnC62nXUBRv3jv5V8f4_YH3IVufJsqRj7ZOJw6ofYH0eavoPxhG4GDoPbM8AFLIkvjoERu8P8dxQuQTBV0xQDpyPbpVzK7w-8iImN2Zp7EalpPvTRGTeEYOj6Eq_bTF5PZdYMwKwerEQshkU4wAaabDXtOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=ZDKzTDAQaBxgT6vwYjGi2Qzj4E_Q1lVTG9smvYeV3UQm5bawoRMcNZ8LAnf8l886UUpTkL3QHIgisbGtUk0bwUiFEvPNJU9E4VtZeDkTwF08frmQC4j5I9SLnS1xVQurcJGggItKV9CTKuTVu1oLjvqGwVIZk4CoMaPgcR8vPabnAQu2dJkpP9-RqWZSwEioqE2t7BZ89BxezX8FkYOAkKA2C55eQ2w8ovmPfP-N0tJ4CAIprSMNY8Sflhjy_6jZ8NZLANVUSoaHAjfQWyEtAMjxIu7vEe8Dn1rZqv-w7HABKKchKlJLjuFL0xBK7qgLzdzVjMFfKMtmDkHiwnI57g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=ZDKzTDAQaBxgT6vwYjGi2Qzj4E_Q1lVTG9smvYeV3UQm5bawoRMcNZ8LAnf8l886UUpTkL3QHIgisbGtUk0bwUiFEvPNJU9E4VtZeDkTwF08frmQC4j5I9SLnS1xVQurcJGggItKV9CTKuTVu1oLjvqGwVIZk4CoMaPgcR8vPabnAQu2dJkpP9-RqWZSwEioqE2t7BZ89BxezX8FkYOAkKA2C55eQ2w8ovmPfP-N0tJ4CAIprSMNY8Sflhjy_6jZ8NZLANVUSoaHAjfQWyEtAMjxIu7vEe8Dn1rZqv-w7HABKKchKlJLjuFL0xBK7qgLzdzVjMFfKMtmDkHiwnI57g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=ZQRUmvkixKvfiUjVPzGLXK6fCmV_pkA7PqRMPwXTKwVhDPliSe6Ulzxv_l2ty2B_91RYY09eCgi6BN-gLVW0LpyJtklleu_snz8gOuqs5gCKSGX2Q6NunhJWlLoOerTNfSBOuMPdeIrL2sJqSrl2CTVB0A8h_SRH_FgaVywcLDJaLVukpdlckg_YFgmjIqlnYgnSxlCTQTJQTNxtsY_ZkKNZG49ISf4kn4yIS_1IAlt1QYhzAt8AO6-id7fvFVNI0dJMer146vvRKqpQgpwyMBPvUcCT3JUMALmhAHcy-ck8Wj-EJEW8LQ_LiddJpMLDbPGjOe0iRvRTFuIJrLXp4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=ZQRUmvkixKvfiUjVPzGLXK6fCmV_pkA7PqRMPwXTKwVhDPliSe6Ulzxv_l2ty2B_91RYY09eCgi6BN-gLVW0LpyJtklleu_snz8gOuqs5gCKSGX2Q6NunhJWlLoOerTNfSBOuMPdeIrL2sJqSrl2CTVB0A8h_SRH_FgaVywcLDJaLVukpdlckg_YFgmjIqlnYgnSxlCTQTJQTNxtsY_ZkKNZG49ISf4kn4yIS_1IAlt1QYhzAt8AO6-id7fvFVNI0dJMer146vvRKqpQgpwyMBPvUcCT3JUMALmhAHcy-ck8Wj-EJEW8LQ_LiddJpMLDbPGjOe0iRvRTFuIJrLXp4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=Men7N3XEp9Kvpw_HrxURWylMMfj2d_ZknMHnD911nCvRLlgy3Yan4crX2OlPmLHMFw14t-7kYtgkISKtGKybqYXm0jvP5u8nUlHPImamCau0A_I5j5A0dq_PkKrjW7N57_umDx8B1HWyrSvfU5yIm2_rQUuLTo1yqByGfYahWW5PTaA41yfH7WZdGVAFEHzgY6qJwE8DjKY0UZXVDGf0XV8QYb9-r8_t4HnJBM1acloPsfI3ecWqLB0ZHDXteuiqVKHi_--9Dzz8C4pW5AF55LqZZPhwa_OU7R0abHFfs9W9C0l9vJUePsdwksoNq7pL2-WAosFMzMnYgPhzugVb_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=Men7N3XEp9Kvpw_HrxURWylMMfj2d_ZknMHnD911nCvRLlgy3Yan4crX2OlPmLHMFw14t-7kYtgkISKtGKybqYXm0jvP5u8nUlHPImamCau0A_I5j5A0dq_PkKrjW7N57_umDx8B1HWyrSvfU5yIm2_rQUuLTo1yqByGfYahWW5PTaA41yfH7WZdGVAFEHzgY6qJwE8DjKY0UZXVDGf0XV8QYb9-r8_t4HnJBM1acloPsfI3ecWqLB0ZHDXteuiqVKHi_--9Dzz8C4pW5AF55LqZZPhwa_OU7R0abHFfs9W9C0l9vJUePsdwksoNq7pL2-WAosFMzMnYgPhzugVb_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6x8ivjbHGKIUG7BDREU2u_GSYXpgeo1IFjoojI03F0DbRgbiPhIW7XfIGubil8-Hv6wB11uTdlusrpowwENq5STfeEcrPEsiuVKITOdZZSX9RvF4wVJ1HCyAKBBl72if65miVXdLR2ViPPdg87vN4oEEd4I4rtqPa-Le0jZrZYIX49GgEwg5ZcvFxtpvYrFLB8uztYY7lVqJAjHEOc1vRCTDg7UAJZVkVPAoo2YqQHjDwK1oS50CaCTqZ6XwJNKHAb_Y552jJBmsPe1tZ0z4TyIgekNBGUfMCuFMiSvwCj1eSbjUeDkviT3jl3dv_LksyYFrwN6KOslBAr_ozucLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uD8UHcpSB1m5f1dQkuUGcL6rG_w__FRaQyJWzbN3ZQMJTBFXBkVzi66Ma8FGmk3ktUR3Kl4emTqjtiAjMfHjOvaeZkBobCiNLEKYXbWd-wM_Xi-8pwEkMW8VH0CokLGtcqN3WFz9pA19-P9_fe-aaM_4kH_KITfJPXMX-_HjheFayNiOKLanH-1WU4b_UUIUctfIjEiWrV6kuxddTRjoQDx8M89BdfaUpVTsN91EZPCnMkpydvURi8VbDk6TwPkIYdKeS4pMLdblqblf_bUHT1zdNWTp4kOCSfH0nI3-AmS-Xcpxoyc49hg5Ht52PMj3MeQcB-KOgil05jlP9gtWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=Gz6CkELg1nLwrIu5YT39_d4ZuOr54BhMvjoVbae-6tTpjzmCAritoIm0DAhNFnqKk-7qaCTb9TkD9irJeWbO4jXd_ZX3KDAyjNM9J4wCw2E8nDQ0wBRSHnlACwVfOIipwRl6t_OCs8_sLUYJB4KRT27hFKTbuWdhjRtAlagpbHqxDwlaIzGCOU6ErshHgGqzGe-7F3SBRcOMgwpLz1_86DRcnGhyCMVeRmgH68MYxJCSEJt9j756C30iaJUwfluR3GIlMmLzT-KjmOcleHZSHIUcSLe6c8rO1q3qDTSeV9cPWjLpcg-pRFB-tcrLw1-8NHwZMQXvD0PVML2O-TZlBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=Gz6CkELg1nLwrIu5YT39_d4ZuOr54BhMvjoVbae-6tTpjzmCAritoIm0DAhNFnqKk-7qaCTb9TkD9irJeWbO4jXd_ZX3KDAyjNM9J4wCw2E8nDQ0wBRSHnlACwVfOIipwRl6t_OCs8_sLUYJB4KRT27hFKTbuWdhjRtAlagpbHqxDwlaIzGCOU6ErshHgGqzGe-7F3SBRcOMgwpLz1_86DRcnGhyCMVeRmgH68MYxJCSEJt9j756C30iaJUwfluR3GIlMmLzT-KjmOcleHZSHIUcSLe6c8rO1q3qDTSeV9cPWjLpcg-pRFB-tcrLw1-8NHwZMQXvD0PVML2O-TZlBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSldDMDg07sZWFhOMmaE4ekztNmu7zwN4LRiH3jUuVgiG-2kz1N357yMzCM-LC1G2VzUHjqkBGnl9zvUgGTIbRtBDbasdUiXSZg9Wz28vUzobHREWta3ay3gwnlvRnwGy62dz8rm5zX5z7QA1cPqwkPKZzut4664WR6XrGZ46Ni-kQrz1oh365H0xMqteRDuH4d8AUAzIcZrK6XZ5b6c-qXioitxEzCutSCHuofi9bUAorpp9YJz-qsBcBWZAPsLxtdQeljrsDjwcVj1jkd6_5T0FTVysSthJCCKSppbFQA4G-CdC7X37Kasl4d6XCgKsntfDYFtcD0QptNQS6COdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=OzecGt_8sxR5Q6ghrVnVxESVl1h3y32lytGAssvOZfjrsUtt1JE-QbiAdF24G6vueLiURTR62gwhOWQQA_Ikq6_2dfsB8o1aYrBJbE5FGFsVooF2xLNH6uD0EUuzbQiyq7wHguUmGvbCcxqpuMfimK2tD04c7xMk4CCZRscWZ6LQ__RM8wB40C9Lslwt8_q_Hqn4EOZwJqGovbYmNWc1yF1IRROH7Z1wVFD8SzF7itn2j-a2zhQk0cJZ0bDglMGpzJsY4cGkzAtpx53SAY4v-oM8GmRUDDzwk4V5MNOtNVkLSOfh9pbCwb3jmkTQuDhnusT_MKEo1HllqaVcg8LGbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=OzecGt_8sxR5Q6ghrVnVxESVl1h3y32lytGAssvOZfjrsUtt1JE-QbiAdF24G6vueLiURTR62gwhOWQQA_Ikq6_2dfsB8o1aYrBJbE5FGFsVooF2xLNH6uD0EUuzbQiyq7wHguUmGvbCcxqpuMfimK2tD04c7xMk4CCZRscWZ6LQ__RM8wB40C9Lslwt8_q_Hqn4EOZwJqGovbYmNWc1yF1IRROH7Z1wVFD8SzF7itn2j-a2zhQk0cJZ0bDglMGpzJsY4cGkzAtpx53SAY4v-oM8GmRUDDzwk4V5MNOtNVkLSOfh9pbCwb3jmkTQuDhnusT_MKEo1HllqaVcg8LGbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOVE5oTc9X5i-zSgc2Jyn8eOoRRDuUCC2AgajzIinE5LFi3zIeMZUIAObzOz8ZUJvGPWE3RqcwY24hUypwupoeM9roQGJBLylXcBQ8C-loOJ2V8ZMVbNZ4uAALASsMcIiCv9P9K91Us1DsyjM8QPOUHcj0ccV6aRQNgGLFo06H6cqsFrYGkawBauU6eGtXL6f7-EE5mWPdKpjvQmeOwRM9Bose8QTdnKQ8pxb966ur5xvxtikQLaMphlUamHu3ByjyZOZk1BtX2BFyUYllaMuCnHn0w4DtjoXHOAPE0k9gTYKaSsUvgCJZKqALN-pZkkZdcAKQXy_EjTNeHNHEqp-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snQitWJxDpaBLDx4j1aiFuc4OrB4TAbRPpo2sZWfAlqyB15-0o8unICYIWiCD2lDZd_6DjvlxMhdIoOsDrJF03QsN7L1vf1VHzo4y0PhltLuByzC15ZH9VfC2QApdW5SRvbxfv1y4DNP9SfsQE0uPyE0a8Q0m6nZCO6FyWb07SKWfzIIQwCx6qPsXtrP5tBNcNbpVVYiUL9sPhuIriTDo0vRXqULWZ8rVOItiPCGQvm6MBOVw4vWJyJLMjF_eoDKJii4wIpmP-OsgQWJFzP82S4TS7h49sbFgmVAlsT_96wBKJZZMCy9jJCG4oCZJQV-trpVPtwR8533rBka8YFvCA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=prhhfBZ_PFWcNoUz4kC2wqu7GEjZN3YXAuHRfCMIhba995m3P6Y1WUrA8BoburOxtJLZvVuyGyKu4ePRBO8vuqqeO5nOSIK75fhRgVXFyqg66U5LclPF2BehMUc5MV24p2zgzQCXffg2kflC9gXUK8jYYatexon1-W31erKbtRgLaowGFOUlpeEiO1u7DITlUGifFAMvuZVlAJgQbBwwGNLWbUXA0QVWjz8gvoswIijyAD-dSn_SB6fqrIaWW92tsvJfDzf9dfUIBmRDHNlo20nfgL4YLjEYLh7s1dDY6G5Qhds4PV_xTh0Lh9FmYzcnxBQOW_cUa0kCP6_vr5DnrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=prhhfBZ_PFWcNoUz4kC2wqu7GEjZN3YXAuHRfCMIhba995m3P6Y1WUrA8BoburOxtJLZvVuyGyKu4ePRBO8vuqqeO5nOSIK75fhRgVXFyqg66U5LclPF2BehMUc5MV24p2zgzQCXffg2kflC9gXUK8jYYatexon1-W31erKbtRgLaowGFOUlpeEiO1u7DITlUGifFAMvuZVlAJgQbBwwGNLWbUXA0QVWjz8gvoswIijyAD-dSn_SB6fqrIaWW92tsvJfDzf9dfUIBmRDHNlo20nfgL4YLjEYLh7s1dDY6G5Qhds4PV_xTh0Lh9FmYzcnxBQOW_cUa0kCP6_vr5DnrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=tpqZizU71vwzBr2Dop7d6kEdhdxDtrqjEh5q4Ek6fMgq82m8qmsXmoFsAgNsOlDk2v5R9RLjzyvTQK1sWEifYzzZeU1vNyVo1hX0Dluo_nxWydKSonTdCkw3eF1gVECrHkmsrhTFim22AZ7WUt2h06kb_9JmDdlCRDb87Jh3UbB48c4ug8F67bszMTIAyvUyO8Ec_RqFWyjI4dWNVTZnYnTe2l4RvGvHHjwnGDryIirn4v5uo0PvcYkq17-UJvdffWKfcnelsHUt3Hv0ckZNGU3jWSOOmNkDzuSQPgFEfG3YhfZqXNZOv7Uf4HRPxkvVtJJ7jna7aujALKg9AEIRgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=tpqZizU71vwzBr2Dop7d6kEdhdxDtrqjEh5q4Ek6fMgq82m8qmsXmoFsAgNsOlDk2v5R9RLjzyvTQK1sWEifYzzZeU1vNyVo1hX0Dluo_nxWydKSonTdCkw3eF1gVECrHkmsrhTFim22AZ7WUt2h06kb_9JmDdlCRDb87Jh3UbB48c4ug8F67bszMTIAyvUyO8Ec_RqFWyjI4dWNVTZnYnTe2l4RvGvHHjwnGDryIirn4v5uo0PvcYkq17-UJvdffWKfcnelsHUt3Hv0ckZNGU3jWSOOmNkDzuSQPgFEfG3YhfZqXNZOv7Uf4HRPxkvVtJJ7jna7aujALKg9AEIRgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LK0rH4HE9OMLHm_UKyPt9ziEEwx-desISrreQ7joqfxfEb90xyNXtXu7NIaQTHjnBXdYTCoqqkhF8E3f02eIUOmz27sPDinY3fu5_s6cJ8lf5OdmSOF1OUNnzMg5aRUxGezIPYjBSKWuWN1PDmGNy3QkjBmZcc_Iu7_vRqjGWwGusZdy6V1rLs-VSij-I6WG8Fn-MSgWDQR4VGmT0MmM4Q_uuuGFwZNKcJDSBsJLMopdh-IKrQcI59DxLH7Cxwkg6qvIfQ6qMXufXCW543s2Q8uoCoHxLjoKnayjVam_cD7lryS-wnY5RCqd0168LkYd8EOjZf4tcf2JyVB1wzhcXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRf46G8c_vLAQRy3IZsZz8gaA7kE0FkZHQTsmUCzszNR7u8e16ipyOrMu0qq-73B_8qkFZFU4eAQb8NtizY9qS03xMYfUo6wxWzbC26Ou0FAtDriughS-LPfAxpe8NLaT94rUOmbv-aY2TT-pkusq3ofM8Oy0XJTUbHc3kFVehTcljKWAQb3BSprkeTx1m_bAGUjYV-d-PeZ0Z1mSq26ge9PkwG4YncZZcQH7WW_9jFHXp1CjJM5yVjMJZJuwBBmW18MRDxOGoK2WU0mAfBqA3ld1Ff9i1Byqf77aQVe6Xm1VCVvesQ1yDrIJEiZDjCq3BR7Bmz-7IBzl3VM4Gx2Sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZ6QYKDdACd-I_vx2lLK5krFk2hrLz0e5FlNFKHufhVpme7rLX57neMyzkw-P7R5R5qMD0B8X1tWe82ja4DUeM1gFb64-Y88BnhYGZd7px8WcWeyEoVSad3xp5V2kRLS-qTz-GrDpni-wUh3P9TaiOlqCK2H4kVJcZrkLPvuTIEf2ZBUse3Gw3qHLnwJwU-1HUBokUZ9YZtp2Y6N3p4ayp1vTDIqCWNcaVqGy5qOYYGQ0hUIrDj-nfXWEAb5KtU0oA0J0mamKT0eKWjpUwdWW6RRfe9pk9QkS8349aF5-2LUDQfPOa4EWkkeklu-GAJSMIts2xtfqYpMXIWFwYrtLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=PZlw0KuW5MD2A1Z62En5sjFC8m_tmBvXS6WS_iGPwAkSQBQ22ZjammXjmub8Bi4kdgO7Va6X9kpUTAwByfHZThTvdB0syiXfK-MTQiGCpHDjW_NnFbU88tme1ZCZXd2-ca27-iNL_PzHdIkktcTRF7eE6MYNpf7YFYEL6X9OIznJt-ZqRRudBqTJo9DcikC5aT1z5bcUy1WdaDyqa2OxKCLLw4ZFYJTTUyR2WlP8--HUjuGZykItgVodIAXc06SfEnuK5lChZAUx0g4SxexSqvBHJoCYbTI88e-GKMvdtIJ75R1AXr16T9MfS0xQrcRX2yP9WE99dLKa6JLi_Sjldg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=PZlw0KuW5MD2A1Z62En5sjFC8m_tmBvXS6WS_iGPwAkSQBQ22ZjammXjmub8Bi4kdgO7Va6X9kpUTAwByfHZThTvdB0syiXfK-MTQiGCpHDjW_NnFbU88tme1ZCZXd2-ca27-iNL_PzHdIkktcTRF7eE6MYNpf7YFYEL6X9OIznJt-ZqRRudBqTJo9DcikC5aT1z5bcUy1WdaDyqa2OxKCLLw4ZFYJTTUyR2WlP8--HUjuGZykItgVodIAXc06SfEnuK5lChZAUx0g4SxexSqvBHJoCYbTI88e-GKMvdtIJ75R1AXr16T9MfS0xQrcRX2yP9WE99dLKa6JLi_Sjldg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgNA90PW82lijufNfFUapVS2T-6s6bL0KA2VoCx4SGOl6Eux66xVGoLlnY1N2tS1orkvsW6fpxBvBkmLdBNClJMU7K26w-6RGt0hOOKgBEpnGWaq5CLU1d_ReyHWp3b3tRVZqiSeyHmA9pizYASwChFnmwXQGgzvuo2NVU6s7asBHKgwS5s-GDc8HifXLH5VtK-MmZxqTmwcLxdv5b1vjN6VsCDLMwNAUUyGVUAQocxYXTjLrrUL3IH2JPLobi7Faay4T5sHXOLhWDeYl9b0VlcI6lxP793goTpDDImeEEfO5JG1-pgryfcTz_q5GLqn48hvj5wyRfESli7Fbj8Awg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6F3zN8-TrZ8d8BqylU_nuJVbSCveXPzElL0vqmUIuGivZGPdifzJTItVGFzRh27x04e_UjBRMtVk3SO5VdEn808SaNDJFOLKOp7hIG0PMvZ-m3nG0aYFdW4BUek2SpX88PG9B2yKXr5nHPL8z7zI5kPGQOT5ckMUai1hM9aKWocBUZ6ehOiD08MtKKZIKLHpReVYqvJUh4mqTq13llm36v0Cl2ji96-OIxqgxauEnEc80n0KNZS6Hft4N0bxkKvqOLyjs2lJKCn5lM9Zr_2ZG_2f-4N5cuKLfiscl-OfT6zIy3kGUvzhRQhi2Y3MXe_syhG9UdoeiRMoINB1lt4bA.jpg" alt="photo" loading="lazy"/></div>
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
