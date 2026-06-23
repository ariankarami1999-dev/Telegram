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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 17:59:56</div>
<hr>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_V24fwnlSEn8pBtox3mpxpxImaYlFd8e44Kta2sIesLQWwRF7pDZ-lW_UHBH-F9OuUJXOBB1FfbiCJ1RibqaJ-snqF452VaujAF8rVwShBgO3Pk6yq55d_s2H5xZqJ1BmADKlUdgg7wCMYaL8kKomfWkB4F4aY63FA4JZmD_ZrXB_3XfVCVWmlGHdiiwsZmmIxrZdOLcLTU6DWWVfKm6fl0IAFlw74qL4ai0_-dPjszTWYa0THkpBJL_fHzGRBcshnkDDHwcT6yhQb-_h4SsAVMeeYzTPhMhtUFGHL-48vTp_vJzh-paPiVuic2vTSu7ImpBdUH03OUVD0BtmS7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmdjgjWxEQuckLdTv8N3YkIHT3mZ55uTCEXVEUmtjcfR3S65A0FeSghZc-Ylw45bbMoUqmy-q9SR91SOM5Ov5-vW049M9Lj7UBlVvKcH0KXXOZ3DraVoVEjjyCvNdx9F_UCmfjVONHnp1xhDmMBEyQvqL1y4VOCgA8zJyqel-NHIzFL2J2AAHcp57cvhoh6JOWAuIytaYpljmJUqWRJaDdPo0GfC3_JrIfeASDwpXycpqetSMCnQzC5f32nsLm0PZgj0YuIRJUEKMTn2pcinS_jnXxJxPBFJBs0hLFapJvQqs4iKiKJarxVXzDTCU3nV_LkymwNc6qxHFz3hrnn2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=DDUGI6h6sk2iTF0lDQyqYqpe0w--GDQAXtDqIiXUigsUI51HsfpwgqJadKBOx4kpcghFujV709qBHGgFCMqdw0DEBosAYcQLQoLqRtsFalgxwB6bFbCusaF2Fdp7KHnDLg0rVCFxm_CDPfDA_8oybEulmCHw3l31NbrVF2qx-ESlG-IH8I_DPX-LRb-ziu2wKoTnH2Oc3T8r9ZjZb1segzw34l82cADt3cna_72QDuK3j0i1LqS9s1tUZe73zy3gbiV54wzXh2smBwQjzyjDVh4jCrQ3R77BoKFXG6ZSEVqOGuQ_FrohLX9zlFCcfZvBemur09eTqOIce57TvNSQsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=DDUGI6h6sk2iTF0lDQyqYqpe0w--GDQAXtDqIiXUigsUI51HsfpwgqJadKBOx4kpcghFujV709qBHGgFCMqdw0DEBosAYcQLQoLqRtsFalgxwB6bFbCusaF2Fdp7KHnDLg0rVCFxm_CDPfDA_8oybEulmCHw3l31NbrVF2qx-ESlG-IH8I_DPX-LRb-ziu2wKoTnH2Oc3T8r9ZjZb1segzw34l82cADt3cna_72QDuK3j0i1LqS9s1tUZe73zy3gbiV54wzXh2smBwQjzyjDVh4jCrQ3R77BoKFXG6ZSEVqOGuQ_FrohLX9zlFCcfZvBemur09eTqOIce57TvNSQsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxFz44CZ3kCcIgGOUlCTGUOCPURyLb_cAeSaLvPM2ekdL4k2M37l5i5nh841-GHVldDo1VaB0hj9oNWOCYQ9-jJ1TgUjp9BYC-lLGlLhO2cyx2KBHh8guuCpZ5XuVljXTHBGW5gnbntOK6JHOr71R3wTYvKAufMCk4-8McBJ8VWQkEJZ4eItyPPiOkq7ixntWJl33r84zbsKvPaP0-10gZSbC9JRfjJc4AKIgTJhEAv4gmWuwxchKotejflOBmjiZbL4DkcnRrsYtoqqZjnpsxNPAk-wCdhIa1bYa4FSvo1SkBSdvmT8qvEJvlRJCU6hfh7FsMh5x3ichxPd0G-p4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JX2Em57BlV8AHrCHXvQjzSsDaWeE202zmSRAsTfJuGGzQsv-Jh8ge2zHT2DcmIyIgNLjtjcYMybGx2PhoCZpj3sozzZm_mgvUjOxPzGgihLVSe75kGM6KWfLDcqYDK_BsrdkhA5tJtnBE2xykOk0Rp_drzY3sOFcgnoAiWQsNXRD_DbrNC4y1rOgPYrMakY8FlT2ApJlTfrV7P3sqomo1OLUyErcB6gxvreLz5gedLYyhSzszeXYbKAukjh8Aytr0LRJTUgqev5ZiX8AB3rSUdDo5Jfh98HVtj2ccTs-LOj7G-2_DR1jgqjPwmhI_NFCkeISF_fstFLoSOXSasXSlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=PX3zHDXBqQEXd4oLvAo1UmUEkjo2iqRBfsAKrJidrJsi0y8Hi8xTOWD0cxbXjRgaCww4T7pUvjbhotVekWSPHeX78lQXRvKUKDp-g7fjp1O7IyEKtph-n5-sY-Isra4QVsj5WbCD27oPRWtH-VcKepqijtW0BY7KHeoXmAfDIMciMEox5HfQm_YRMiUhOaaMVhv8Ay7hTMYlGIf4RrHqe8IUWpOSKSWaflnUCPvb_i0Ctj57P6XM92TEXNLx-mZRWb_tD06yS06azx15woW4uMSyxMEUPoa9dgcJ1K8JS_mtBntjFYI65qZU_pWfzs-GcnogMytjxfQFN78op_0Jxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=PX3zHDXBqQEXd4oLvAo1UmUEkjo2iqRBfsAKrJidrJsi0y8Hi8xTOWD0cxbXjRgaCww4T7pUvjbhotVekWSPHeX78lQXRvKUKDp-g7fjp1O7IyEKtph-n5-sY-Isra4QVsj5WbCD27oPRWtH-VcKepqijtW0BY7KHeoXmAfDIMciMEox5HfQm_YRMiUhOaaMVhv8Ay7hTMYlGIf4RrHqe8IUWpOSKSWaflnUCPvb_i0Ctj57P6XM92TEXNLx-mZRWb_tD06yS06azx15woW4uMSyxMEUPoa9dgcJ1K8JS_mtBntjFYI65qZU_pWfzs-GcnogMytjxfQFN78op_0Jxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=SxPnhcOA_Ab1TO9oIDEk7ybUBFSjeyigopKpBXGtZGP0iO8SgPOuL7P6P9KlBTRbBV0GSC9tSsc6n4L1ReckjtsEB3VH_ik3neyPCnfM5LdBZXyAK4mlTEgE6V-UO8esp8On-ybHK5Msdqu5BClcfxtgErM3VgXy0BXE2HXvL6TfcxSYPlRybPF6AWN0gwL1gLbzsBjR5CZPZhlA5FRRUrtYM4YL4wFHPZA-WPtRq5I9Y2SEnYCVNuHdZk5p-Ax7Ff5u5T7WQw5CT2IcU04p7LMmdKavrHh8RTICq9RGpY50WVEtxkmkysx7ZmFPtQYIYyeuF5RvF6fccBrRi4VBlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=SxPnhcOA_Ab1TO9oIDEk7ybUBFSjeyigopKpBXGtZGP0iO8SgPOuL7P6P9KlBTRbBV0GSC9tSsc6n4L1ReckjtsEB3VH_ik3neyPCnfM5LdBZXyAK4mlTEgE6V-UO8esp8On-ybHK5Msdqu5BClcfxtgErM3VgXy0BXE2HXvL6TfcxSYPlRybPF6AWN0gwL1gLbzsBjR5CZPZhlA5FRRUrtYM4YL4wFHPZA-WPtRq5I9Y2SEnYCVNuHdZk5p-Ax7Ff5u5T7WQw5CT2IcU04p7LMmdKavrHh8RTICq9RGpY50WVEtxkmkysx7ZmFPtQYIYyeuF5RvF6fccBrRi4VBlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zi9io86Op95OGkoodVGRmLU3JqldejETKqeEaUeJ7ubKoTMmxaYJdJOd14AF7aUc0pS-FMXOHfIt1pbx-7v_9R0WbCVF2NnVKUmGIPfBI76-Rvqlhs_9aCYqFTNN2-PXR4mdZACdF_nRiuanKKluJG_cZP0AhtPPOHbRl08q11xIV17rrQBpVIh0rfm3ihDeWjNuIGz9RY6dhnuTObPna63n3EYlJkgDpp1w9dbZUfgGFE-zZSevUBEAWt3w1xBT9mYreejg00D8to2OofUi1tZmJnNZhKNxqfd04abFuwtn42WNOWxSkirBwI7fF-loYDqsnJPNqpPVqyyTughrmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPv4zlnOPtBcyxvpNu53dEjnxLCY9FSYzpUGEa8o5G8wPV0waLcREqAJZtb1H5HCsKlWz-gXL0OF4KqsWCGj7jngJOBuZuZWxloo5L8fZtG3v2qHg17S8uwjZsitxOAPoa4XMtFpyqC-5HGc1BieB5QExO531_P-kz4MVKsbVbm2oc8Verf1I5Pg0478VUh0zrmwYLcEH-Cq-fA_VjyRuRAYfXBbx6pY9ulPF4GhZAdIghMVarN_zC2toQ3ZjtBS2_My7SIOPFYDYPEb24BaAGy4Dk--6j2r7KBlllinWIOBj-G2ttarumz_-_6uc9xvCpFnU2CWkG162nSZHZ0SiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r3z67X9JkE0iA6VGYTVb7vqyZUkVjtXzKoYKxqA9JjfZGG5BhKzYtjBpJkcJsb02p0Ud77sD4jGuW6DVr4XLmmMSUPfX0Cu1Rq6zDp7kSGLEmlkSwDYwlPcVeLOmBkCR3FE92fN5_TgNtsEE8StX-h2D3EvnXXis_Gk_Lwyd-CQhBCOWxcpmpLiCyATmOQxW4b5xL45RmMoIQkMWhmaMFbflpwE3xjTw5rlrpjm7Qw9zekNmreEJhEyI6R-2zIAXOPz7HOXBVcPfAcBWwCZx0BTwK0NRGgXKGVFIB6dqlNXeXxqq3vMH6vI6DF7i-rTrD24QASs3zFlZo-t7KpW1zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ScwO_3xK60fcKFljmgBJYNV4e4DxBgqzEO1uLenk2HPvA7TS5onQn5rZA_X2yNFwcZsHXBsbUikXWCTpD9Dr1bu9JtbtVedrgMQI9QZmvCLi_PztZ6ukdWeP28RVTYs88n-DsmIQ5n_V6Q0rhUG7HnPbRNGF1ZOungfj6kIo9mnYIjjQy8jshqJrI5xfyrAB3nKIrxWKv6FCSfeBJ914TRN8xF08ZwcpvygjimUi9h5waxF8iLjah4-GFvuCGZuDM2YdSyRHbpCg0zaYXAeVt7Z3CMkGrAUPdK886X9d2YhCYO6u2zrCJiFyY-7JMqw6eW2Hq7YRWaeKmdo_W9xGrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3bxx4fxSx63_FfohgEqFjE1qGXeTDA3PbgbUXfn4-UBWE2tNwtZpY94ILw_HFCpqV7gDm3U4qyrTJW5URhuOqlkFeXrX0msXySBvg3VzD1230_-Ky0eoCs6ROVCXB9yEqoxkBhT9IDTTaxuRapMh9WoVAFXVa8R8sazgR4khfsfc4kcWhD4G3fe4VRhKnJXsgjWJqnbEHE0QbKwE1m76EHzHQ282hdhodCQ3QGwSwwtdsJsVG9Mo6mO7LCXniobGjJpBYTnlr4l-RS8PeVcDPWe58b-aCKLB1-TRzymFHshMCQrVLVtPMllBtxnnLo3bolui9VpDrC0FUrH-nitKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JMEJDHImA3LZAKp0PlrLbwyqddPAs-Nx8LbBSYrTVEqk23uh8oppLDPO-HYR-MOlGIzDmRfs-ftdSEVHW9-1G1UZQM0FGPVxRIQz2GfdVji1to_LDR-UkVXAM3lFNvbITVwojZpIy4C7prwsBuGcV8WcAu9xUihIkvGcZHK4YU_FOz8QP3ifMaMLHhA74iSaGQmI9cLQf8d_kx3Uj1RZaufuYiLQZEOLgKgQEQryLmPjDS1hQi3RShukQZ7_wjDwZ6ZijgCHNatQ_MDjeQbcP9Tysr2yJh-G8xzdobbrigcfzNhDiF6vrjxML2O-g2gkFjubhaSgF66LIuL-WQbElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYnfPFsRRGpKzNNfc8YAodSzpW0H_a4thhaeJ_XXbdUtteXIyJye54Rvd0MhzD5SIhc_I_4ReovGtP9fdpMdQG_T6SXAOJCSQhJDXf0FPepfXTQTuIdkaVtZkgyFia6jPmu_zSkL2siOFaRRmhMX0IRz5Wq9itjlC4FyOVDD4LGYiiEu-hXgZ6xEDzhObUaQRsYEjIieVIZmSY8oPHs9FUt3SXTII_D-bFZWAZiXWxSSorVS4e_K6MO042IcPNZznsnbIa07XJvLMYhdT_HWMSnRNGgbFbXLsvzNsehd8J1UdkbieK68wEqaWYsUzoYsNArgmdkkh1KGcgOSLSoUVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J42E682GlouYeL1GriPYvPfZjYDiyNGgQGewLcElydHdIOG1cFH2jnN7JOLtWtalzBPGj6MCSsyPI03Peu36ALRQfz63IExiHghLWyBoaREDGIyvrF7ngK2VnsIa1c2NWltJG2RsJx5pytvZ0S15FP-wvCxrhNRi7zQEKzPnVzrJiRFwUlJH49ac-W6QLTxJUjaIG0qRl3gW7dst2oIZvvzkFYFKNLQjVR3T6LOCyIUkS44bwEinMwYH65kShJgFk9zBELH7YWVP9gIRh3xl5ETYyyRq5NIm8Yd113-GKi5yfzPZbW7A4Wtul_Hiypu05u0US0SUmXIm_fXonUaWzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol6IGRrFiVjtb0BKaqEgTzznMnDBLKK9b9H9PhxTWVei3z2U3kd5xR-_UxoaYg1yxKhgb1dcX6fDmneiFx--pt0tkLCoO6c3vxlwPpBwE_HPPc0oAqeQswUiZ3zTKEOOMmKbP1BB0zgJvoh7qXjHd_nybb2m2gqpDHFdyop-ZDF7mtyEzBQ_I9sJ764fPmVjSoevPP21actM1A3m3S-kdmAOFDe1UmbY_dpGAOn0IcXViUJ8xEQ_ErCtPy4YhFeZvE2OdLiOhmYZBiNO-Mjh05ZferGqrIWlm8RAdGgs49aiM-kqeZDa5AEFWmUbtt2WLp9wUcwyRXDK3OjtTef4ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkNFar1wQXzMnfk9p5Qw8vwvgK9QBM_HhQKxkzYIjobRLZvhVdXEXpo9Bu38pn3ksfk2eBxuccSDJ3w-7yXrm-GHDAwh-zyAV8KuvwE6oqBZ1Yuk0_TzpV8hD8ZJ_DtQHPkWfU5meI1wCKZmMm5Ie9TXufzKh6y0pQRgyJMgpnpmenlwWiwsxIF-Jbm-knoZExL2bha5UQYjrXLF3jpHfJJzXg_S2XyhCjbU9mrwVUvklHU5O_NMha8wdbQv4Ldzi0pMXROpPoyUx9LVsS-YoXQ0s6Q_TZCdrMw5XEBnIuDDa1kcsuVGf7609GU-ZUzmBNeZ599b9jEgE-dAHJbtRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEthxSf2pHsZqBYys4O9kPPNIafPp_PIivoZvL-fXyJdP_UpjY1qHWj3qX_yXuxy_rNa4XMYhmU61uFJ1MhcEvBGDYHsX2emawAapIiX56ylSZN7TIAW-YtpeFCoXKl3Dg5rcyskwZbpYUNQ7sDi89ouzVd-WGoz2y2UhDXUKaGBCJO_rpSN-arVWl7YaBHpH5AxebSEK0TFCEaa35XkkcGhTABFZUybnAQoHsaO9mFraz5zQrlZRkC_PzLPvc2EYAqv0ZwltXQurLNVm3fI0qTkHKSr6Ixp3KCzMzUlVQ_hWMZXAqcR1aoxl8C17XIQaG76OR69aZ1eANgI9D3vRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AX8d1pDNe1iYN6Lst4AZQ9mnLxsaa_pHtxeGlGZxbszcbLeF0ocwuc2XG31F1XsCMj1RxmdJRzujQ3Sw3xP7SLjuZC3t7bz8kQBnmI50K83FVutN92rVho6llfkjzjYiBlfpSUZgwQwBNNxNbOY78_BgOrdg1Di7tCgtjPsejdnC0uf_c8Plwgy7e73TP8s0T86ux8ONtufN3dTuWfBDTRbKAgBN2r7FmShWXGMGN58bhd_-mdcqbVzASZdrHHA0wTyafpvTUvN3cw9TCIeiT3E-0UWHlLQNxUaInR8XNICFYUibuknHME8Qo2kipfHWbdDLIFNpo0v4yXL7uT0vZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNQe7ZlYKA46Lt5y78OVOIoRAwNJG0a1u_Ic5Ofqfq78-yuEhy61WYm6bHcH0MYvzA1aF070E486o7JQzlffG-s0-7sdWlv3Ack9ykxtxzXISGo9PAV6Oea8wSBpAhIHA1snTgb1g3XG_Z-c5aHsb_CMOHttKS8XLyNMbAPDXBuuUGSO2ZrNKyDmKUn0WcZz8WJJY7W7mqg8h0uqz4MpXWmIb-zgInWrWIM5OFExRmOeVuy5_-fV0wUdaOB2Ody6y02rthHrTvMoqMGE4CER3yYCCFHoi1pZBfyMOtpgwi6dcBF5QLmW8fX7xp_5R1Zo-q9iwJrYLGT3yeuadLC-4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9BQXCy30Ue5EEe9QRGjJ2b3snJQgWM3MyyQyd7fOc3pzmEB5GHWzOHHMUjy0MDUBdkiGHSX8sgjA0Myim9zgeWLIq48qSg3pWgR8_G45YgLNvvs8jF452kYitEX5dQwa8kxb-v8CwF2G3Wh_6o3Q4vOqbkRQBHR0ooO9mudKy3uUJNeUvxkNtYDcePRcQt6KMC0fZjmg-ECaXvj169XFlxDHadrtP_u0tfL_UBxnkfpkjUusMctzve1cpyVuILMtwOT-DBu0wjOXwpZEXHwFCA8bJC2ulUd7HZN6J_ku8S3bzWeTx1iBn2PQ5jI2Rut_q1VwAVJmgRQYBZuSFTsmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjcNSL_rlnpdoOZ-zEG5LS72IE9LDbF18heeV9xqXKdb4WSEf0AN12aqjgmUkROV0AWNRB0hM1CjNubjA0jsby2q92MERxVgZcsF4MMHMshvh1aRHsuY1Gx4nQhxZUK_99lntj2d6nbEcjDsulR86XA3B6ELZMCHOzEvrmMpaD0Lp5rHdbvfEplOEArOXOGnuNXwCnWMVC8S7hs4M26geXmfqJ8QkxhEGmStbos-QyG4ZGjledLtxoDC8WDhl13K1p5QBAuRMm3wY-v9AIj82Ye0um2_aWWXtUX8-P_8s7Ay9x03PY_lWdKWR3TVpPwUHmEJ5BohATF5dB05AoALRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=phbw4nqkDumybF-qEvT0wugOW5Z9ghJZOfKMyD-vQU9vI4pATb1wMbjPCHbJQjyWrBdRiqA5nOtkby76g_jeh75-kmA1De8DTW29qiLbJeQBomaOn5ZxHUf_i1OZoovKW9_OSIOXWMXt6BkWrT8OPSszs6w8xf0n_cn27CU3vd3smpA4xHdNpjonZPhpADO-LSHs080HaTtmqqsI97G71nWDhVzi91vbMRimo3g30-fUNPvQRXF9CeFNbSB-TAu4owBAZLM8ezMhy64sBB6Ccw68GRFkiFP2XR_-OHxL950NgVUE9AJdjJ6bu5y8JOSoYDC75dJl9jKeTERlFnGhWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=phbw4nqkDumybF-qEvT0wugOW5Z9ghJZOfKMyD-vQU9vI4pATb1wMbjPCHbJQjyWrBdRiqA5nOtkby76g_jeh75-kmA1De8DTW29qiLbJeQBomaOn5ZxHUf_i1OZoovKW9_OSIOXWMXt6BkWrT8OPSszs6w8xf0n_cn27CU3vd3smpA4xHdNpjonZPhpADO-LSHs080HaTtmqqsI97G71nWDhVzi91vbMRimo3g30-fUNPvQRXF9CeFNbSB-TAu4owBAZLM8ezMhy64sBB6Ccw68GRFkiFP2XR_-OHxL950NgVUE9AJdjJ6bu5y8JOSoYDC75dJl9jKeTERlFnGhWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXShhZzRq91veWS9zj2uhQIgQJnRJeHlVeNckFlGFBKL-UGdWKI2T2qq1vUJe3CxmavEvkVeqIs8luUOAr0VVA8q2GABLB0p5DeLKmkMQO-fRCzAPYpVo0dKGZFxPBL9qy3OXjXBsJbMBxve8rQys6gosHk3oKAmn6QJkJXXD9CFJhSjfF6s7eRYwkvHalBBPvfsw3bBAzp6lbEp6HIBmdRunROkUxOphoAnlxSvvdRP1RtIDfOss-RbXTElmtngOs6uP6I8W3Bqow8ExaSh9iIFvgcWqegtxH9wjrGZB1g1NtBc8PESk-1_tL1UqUUBdExSUQrlLzwDT_peErKnJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=VIv1J8KmWRiTk3_u4KiWsyed0x6gQw6aJyFK3r8ajSiOlyMUXX7XW1Ag6noZcncIXKPqxytDx9HKrdU11XrdsXuDalo6uTAntnZNw72bqpGl3OS8xOlKVKVJiWcVPdJNXUCqJoaNiLuwBnUBXSgFNrwhMaYux45xT7krYrWVlLc6bbIFmDDZhz0tFeZQr4v6x--XMMc_xjCSIhxWpnd7MGDbItVC2Qq2TkY8ygI2EkO3E1MXwF6LN2joJZCPWNrWh9t-pP0N0Z9QR2hflSkPRE6FdfFgFpcEU0XcljNDnocyZDTfkYdz_yuA_iDGolXd02CQyRpMOw-9o8Y_Ut6kcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=VIv1J8KmWRiTk3_u4KiWsyed0x6gQw6aJyFK3r8ajSiOlyMUXX7XW1Ag6noZcncIXKPqxytDx9HKrdU11XrdsXuDalo6uTAntnZNw72bqpGl3OS8xOlKVKVJiWcVPdJNXUCqJoaNiLuwBnUBXSgFNrwhMaYux45xT7krYrWVlLc6bbIFmDDZhz0tFeZQr4v6x--XMMc_xjCSIhxWpnd7MGDbItVC2Qq2TkY8ygI2EkO3E1MXwF6LN2joJZCPWNrWh9t-pP0N0Z9QR2hflSkPRE6FdfFgFpcEU0XcljNDnocyZDTfkYdz_yuA_iDGolXd02CQyRpMOw-9o8Y_Ut6kcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=fGHOprV6g6oXLLPNHCSl8Xry9YV0Wp6BvDmHTCdZPYVxNSMw6dghFTgu4i2sNoo4aP3Wtn99mLj818_OytjuCCxbwkb9x3a0OLIVJK5Ykq9i-fEUGwL448rOJMhSbLreA3FIdBQI4B3LnhMukc9AQ5H8eFhPrDjyLeKp31IqClvX0TgcuJoudADCxGk6dUCsO9ajLlmG67UzO3L_encJGFq1v352d88aXxbIPh0MuxCP0wTczAKTuPL7LDz8QV8Wr6Y-oxHaBfuG9tnJpFlznCRG3qQA-YqD3U8XJ7_pbhZ5yydJRlRUmZ_sQgZs95FJYUY19wELUx_w7ZHozXOsIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=fGHOprV6g6oXLLPNHCSl8Xry9YV0Wp6BvDmHTCdZPYVxNSMw6dghFTgu4i2sNoo4aP3Wtn99mLj818_OytjuCCxbwkb9x3a0OLIVJK5Ykq9i-fEUGwL448rOJMhSbLreA3FIdBQI4B3LnhMukc9AQ5H8eFhPrDjyLeKp31IqClvX0TgcuJoudADCxGk6dUCsO9ajLlmG67UzO3L_encJGFq1v352d88aXxbIPh0MuxCP0wTczAKTuPL7LDz8QV8Wr6Y-oxHaBfuG9tnJpFlznCRG3qQA-YqD3U8XJ7_pbhZ5yydJRlRUmZ_sQgZs95FJYUY19wELUx_w7ZHozXOsIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsjRrFb4bv7eQ4Y77Y2708l_fkw1nMvT55NTmMqTivjG64EYLLofZuakmGf1n_ud_AYHWMVrlJQB1Ca1pKE3FsQMbE-6X4x96awa2cWzB0Y5ibF-YlHMhMP7hQTm6u-Gmm7OVmIuv2oIizgpdvcb-4uB97InxDt7O46MyJbGOEL_t1dU_T9uZlSU5vGJZedNAD5Xgr9mh7VYsh-x77BlgpgAGS9dWNbxta6WQUGP5qSvz8YoMSjgLDJblVwe7zESmWVg0Nc263aoMMSvLZTs9Y-Usy9j91hwatLTjXWux2WPdV4TEKGmRKqD8AFTwkfNtPVboy0dORuWZLvLplTtaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=hpyDLE8GFzxlzIidbZXPmLRGtC8dioMXMAxpWiH0J6jRTHa46_G9jek64RkHRSHpg5oFe9CrPHRtE-B0fjPbV7rjQg6i3fz2ioesslaXl1ZF5c0LBUbgSyqqPK4YKDnOfzq11fxO5iZO2vnfji6UoNkSr6zDj36m6v4jZujm0NIc09WwdtdiyFf1TY4N0gwLQnMbbQdygiP6Ut5xzsDWOEd-uy1OJGftXucnIlbGkxZufo5DNrRYS2W24UaTs44KBLdLbfvs-YIMrzVrewEyHyHJgXLoCqfMpOkkTf8gEOvpfk0ceuZ-wjAXoKKKTkF76ykviUX9_U3crXRC_3yXKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=hpyDLE8GFzxlzIidbZXPmLRGtC8dioMXMAxpWiH0J6jRTHa46_G9jek64RkHRSHpg5oFe9CrPHRtE-B0fjPbV7rjQg6i3fz2ioesslaXl1ZF5c0LBUbgSyqqPK4YKDnOfzq11fxO5iZO2vnfji6UoNkSr6zDj36m6v4jZujm0NIc09WwdtdiyFf1TY4N0gwLQnMbbQdygiP6Ut5xzsDWOEd-uy1OJGftXucnIlbGkxZufo5DNrRYS2W24UaTs44KBLdLbfvs-YIMrzVrewEyHyHJgXLoCqfMpOkkTf8gEOvpfk0ceuZ-wjAXoKKKTkF76ykviUX9_U3crXRC_3yXKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmvfPXWlCaT8eAoxgK0o48X0d_WHsownjHDQmNavWEv-pRCXZRucxIQs1PXQarvASFWN3abKbjINW2h1eGwjMJ7q9Vn7-MDXLvSPBGveb0qvZD_lQHIRyAtE_ctBh_x4KWdKNMHwOo05wbe0CWYrH-Kvafzdh-QqgWjh0tRHm0z_Qmmh_H7Dqm3r8ZaoZKE3tJP7aGI9hBbxrX4xEKSknPxcYsk9hJ4R_1OcD8MHVc02-1hj4oE428FEyzDqyaxyQzWam8kFGYcqhdyWNTgIQxJDia_YofNv3-feinmACaK9oJNYVvzVqFw6n8zPJMwIZU4rN85-zX3Rj57NIr-luA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmvtByKz4FsW1yg42XmqoHgdtAecMiCJbazPxVEjCNoBFIBcauGV8LSs6BESeKHUhlv3FQTSOqiy6r2xOyEpBZ4IlRIjUunaVVQdb6-G33K-9zrFTsJxMJAWoiZyo647l1TxZEBbimM_6-2r4O5MrYtrgnlgrp8W-RKdDIU3flF9Jy_k3IvgvRJYGKZYjRMkc9-Q4P4C_yfYN4ahKq2l4EHUz8mHmU0KBlB2-pkl_JGWW0McYdy06CeDABxbv60EhOmgt5jY6DLwM1GKNviryIXhp82x4mfjhMdgF5j9Q1q6q8013rI5t-jxAl_2qil6y-BsrScIBhIvQL9olsJVfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2nVLCBeVgh2N7sM3oifW_ooB1xB-hPYh4NXjkTLlVyR_k1EUKT1GA9nmC0gTf4RTdJm4EIUluiJ81jxkgp8-B-rGlCEa2749-mBl-fZ7t2cN0TXdqRMEQr5awn4BcMe7F4WeO3HC_7llGRk263_tHpVpsGsCH_j5zscJoTZNTrldViFSWxUgFJ7Z1HXhVn6EYN2KA83unWX3tcLLf7VQ5o2o0tCsGv1nnsHC6WWC-UrJe6RAsIxetg1cVX8knniVKZVjfaGiCSYfPHElrPKKp3VWOHypKTBMDUFl7i3LZJgknbBsISi6ZBLLtDBzu58DMbvATgW7Iwok65M8gHzUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLBmT7ySfBVnSQmqZvPybcvwZlOYN3t94Diq1uObXh9N5o3XGwDHldJYNWsDV8ztC7hSnt_LOdLcFjAfgAm1hcI1vSSxs1tU9YO3Kk2PYKZ0sp6jfwU8Vjnok0VDiy_oBloqtn4KQELb2je1C3irOVUbEuaX-9j7SARVI7TwJZz1fT-zU93Mv-hYJ1sI5Tztf5e-OJzKKpBgOOFxTTEAU8p3jN9EZbh1afWgS-aywJcFcGbSbWxr6RSrejtcbLaLfTPMCCHxzDFvBC2z8Q8b8KaaQRLSbTI9XICj3dsLFNJnZRDxagxObF9d0koEbIazw6rby0-RypVtEK5JKdDxcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=VfnTp6SUnuOF6kql33p1kN9EdZ5rnss5Tfe3DT01gYCCH8aCWA1VggaskFwfyuyuAirIazo2PygbnghI7wniuF4uHG_l61dinOp4QBJ9zc6Yqj6_KqIy2ctwQcu9ElWZ-Yqxph5JF3O6JDQzsBHiPWaF0IoiQ2IlrStqa-XVHyXjQG1-AVqOuuBIb9af15dMFcxQe4QQI3RD-LexotITevZOMNxAN1xlLUFooEpF3tnzBDQWd2vIM1QV0X-XvrshpiNU3XlNT4WBDQ3l0nEOC8O0uzHDz-jjNrJ2Gij0d9_bVUMe2Ff_HN9ehCdNR4BtpAD31fsZQHTeduzEJV5zpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=VfnTp6SUnuOF6kql33p1kN9EdZ5rnss5Tfe3DT01gYCCH8aCWA1VggaskFwfyuyuAirIazo2PygbnghI7wniuF4uHG_l61dinOp4QBJ9zc6Yqj6_KqIy2ctwQcu9ElWZ-Yqxph5JF3O6JDQzsBHiPWaF0IoiQ2IlrStqa-XVHyXjQG1-AVqOuuBIb9af15dMFcxQe4QQI3RD-LexotITevZOMNxAN1xlLUFooEpF3tnzBDQWd2vIM1QV0X-XvrshpiNU3XlNT4WBDQ3l0nEOC8O0uzHDz-jjNrJ2Gij0d9_bVUMe2Ff_HN9ehCdNR4BtpAD31fsZQHTeduzEJV5zpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=jvFV86Z41g1aL3bxDi-T4DVaSNWEOUv_9iqJ7ml24Bxq37NGxQFqOD2KI_FPbPMot6H1_dpNrY3twq4lQU_fEUdhsDpDKPxF053JljeXJQC5FcWjOXxSnGw0yInk5GGbzjKZZqZKX55G-0-f2NqjgwfY1DVNIDN4hIn9PzFV2O-OttAwP2GhD5u7yK3yc1eZRhnTLM4Bk1rbl4P4tMsNkjaB4qO9ggnns1ZWPRk36f5JR-_ArwEcgs_FlLrNV1EAU-GcotMqN6iQkHC5fd2eYR2lwhcLqFqKRCkh2n0hp7tMDxYjWvGmO1tLU5SWHAATLhSMHvBeC_WdUHegr9W-PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=jvFV86Z41g1aL3bxDi-T4DVaSNWEOUv_9iqJ7ml24Bxq37NGxQFqOD2KI_FPbPMot6H1_dpNrY3twq4lQU_fEUdhsDpDKPxF053JljeXJQC5FcWjOXxSnGw0yInk5GGbzjKZZqZKX55G-0-f2NqjgwfY1DVNIDN4hIn9PzFV2O-OttAwP2GhD5u7yK3yc1eZRhnTLM4Bk1rbl4P4tMsNkjaB4qO9ggnns1ZWPRk36f5JR-_ArwEcgs_FlLrNV1EAU-GcotMqN6iQkHC5fd2eYR2lwhcLqFqKRCkh2n0hp7tMDxYjWvGmO1tLU5SWHAATLhSMHvBeC_WdUHegr9W-PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=D3bjTPzPYI7Dzyu3UpidSgj3QQInMTrSb7OLP7oXOZBINQYqN9pAUgK9VxeSdSH69OP-yUrv0EDAmExa4a-FmcwXYIiZhmgcswNeFegRI3GAFmVzeuMs9rRwSPJPWLvlUgK3t-9j9HE7tHcIAqI5w1iuKhqGiw0aS26kewc2Qy0WRwa6oS_pKc5m9-nSnW3GYMWVHeABG0byFzZJd8eq6cbngw6b7jsmJRFW3lbvxIK0ARltJXFplLejKt4VweQ4uN1rz8u8zlJEmjOuYzTELcpSv8Trqauqwgh-rNBxltM_HK5ac8K22F6nQG-8cdT7oVo0dtb4BtJ2PmjED8uu7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=D3bjTPzPYI7Dzyu3UpidSgj3QQInMTrSb7OLP7oXOZBINQYqN9pAUgK9VxeSdSH69OP-yUrv0EDAmExa4a-FmcwXYIiZhmgcswNeFegRI3GAFmVzeuMs9rRwSPJPWLvlUgK3t-9j9HE7tHcIAqI5w1iuKhqGiw0aS26kewc2Qy0WRwa6oS_pKc5m9-nSnW3GYMWVHeABG0byFzZJd8eq6cbngw6b7jsmJRFW3lbvxIK0ARltJXFplLejKt4VweQ4uN1rz8u8zlJEmjOuYzTELcpSv8Trqauqwgh-rNBxltM_HK5ac8K22F6nQG-8cdT7oVo0dtb4BtJ2PmjED8uu7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=mQjX1K9I1pdi7-36MJoLyHVa0POZLAeqg3vvPSZxoGFdgDnEFSO-ULU-HOZb-pbM7mGl9rUne0Okv2VqGgMB-bXHbq_rLxhiXmqR3oL32rjMg3bWNHT7IcVbkKbTZR7qzxW3yL-2Ks8NDfKOLpsxPwRyTSlcqZH-47diHkNFfWQMSWpKx753ibGHMbvJqxYVVe5qXfBLG4CHagyZBy9pArfWyharAURo9VWQ4qiL044rnbKEYuOT3YKubrvMkqLpFXQnDnG9xFFAt_D0zsb7bB0hUiAqjP-pEEqLpM3jNJgDy9CaOw05iAMRJYI-ijJy_L7AXYiTWf5h_R5BOSdDwABHgrJqJH-TB9LJ1l6e2BU4ZZinzYlUwrbKCqVtAXF_ttmslWwdmi0REOYujX9bZNpf7WmgCz-SxdyZ9ydYRVrG1Dcy70cv2fxLzWlbzRrjuu4Ikxwc6bSNnhFKe7NG8GhqmEQ1dKjEQ9FhlIVr4KPtgv-N1tF4i5ckbdlv7uKxIejTeHY8Fvim5SOHrLLgKyBFlzpdKBYgySo7cHC33qiORlyDSWtAaks3smg2BY__H8MEK91-VW55lhqaeyr60fQwmlx06GrAeU60RE5wq13Ifh9yf3Y7GZFGxS44hQhFUCApvMpEfheDB7yeser1Yr91w8mCXEqJcso6hE_Qr8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=mQjX1K9I1pdi7-36MJoLyHVa0POZLAeqg3vvPSZxoGFdgDnEFSO-ULU-HOZb-pbM7mGl9rUne0Okv2VqGgMB-bXHbq_rLxhiXmqR3oL32rjMg3bWNHT7IcVbkKbTZR7qzxW3yL-2Ks8NDfKOLpsxPwRyTSlcqZH-47diHkNFfWQMSWpKx753ibGHMbvJqxYVVe5qXfBLG4CHagyZBy9pArfWyharAURo9VWQ4qiL044rnbKEYuOT3YKubrvMkqLpFXQnDnG9xFFAt_D0zsb7bB0hUiAqjP-pEEqLpM3jNJgDy9CaOw05iAMRJYI-ijJy_L7AXYiTWf5h_R5BOSdDwABHgrJqJH-TB9LJ1l6e2BU4ZZinzYlUwrbKCqVtAXF_ttmslWwdmi0REOYujX9bZNpf7WmgCz-SxdyZ9ydYRVrG1Dcy70cv2fxLzWlbzRrjuu4Ikxwc6bSNnhFKe7NG8GhqmEQ1dKjEQ9FhlIVr4KPtgv-N1tF4i5ckbdlv7uKxIejTeHY8Fvim5SOHrLLgKyBFlzpdKBYgySo7cHC33qiORlyDSWtAaks3smg2BY__H8MEK91-VW55lhqaeyr60fQwmlx06GrAeU60RE5wq13Ifh9yf3Y7GZFGxS44hQhFUCApvMpEfheDB7yeser1Yr91w8mCXEqJcso6hE_Qr8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=KCyF7z9_O8O20gOWcyjfM_UrGT3kom6soKg7epe4kQ7ebWkGxGfR7yevCEZ3LPfdTC9PR6gUOpemJ6LqjkyK2kENXFPYpgSPYK32yTQNNzU2lnotHM4q_EA63Os78WyA_OefC6n5vY609WTONBxbp17vdWvVhd_Rvvs0_olUBYP7TDTG9FjdF1GfkbAjfCTFZ1DDxCyhgXx0Az2CH2nNjkEgIskzH0K1o_lxPph618-iZxIP0i1YYJ4dbeO58mlRl3yGaNNwggEN06iI70doUcxuu-MhnncRuHdpaCT-7gxv4XkrDCGp6irsWorpzQ_Jjmd0X1jHR6R-cULs8Divzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=KCyF7z9_O8O20gOWcyjfM_UrGT3kom6soKg7epe4kQ7ebWkGxGfR7yevCEZ3LPfdTC9PR6gUOpemJ6LqjkyK2kENXFPYpgSPYK32yTQNNzU2lnotHM4q_EA63Os78WyA_OefC6n5vY609WTONBxbp17vdWvVhd_Rvvs0_olUBYP7TDTG9FjdF1GfkbAjfCTFZ1DDxCyhgXx0Az2CH2nNjkEgIskzH0K1o_lxPph618-iZxIP0i1YYJ4dbeO58mlRl3yGaNNwggEN06iI70doUcxuu-MhnncRuHdpaCT-7gxv4XkrDCGp6irsWorpzQ_Jjmd0X1jHR6R-cULs8Divzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=TrxESjRi9J3jrCJksBJtbVKSXlDccjU6wx6lzgmkXAHn1ikiiLR9sfCPAwq3iC30fT0PwmODKoQ0H-0F_wacYS9jH6cM7NWmzs8eWJA2Fr5HliRVWDpzioJ0yzZUfY2k4JOxjcJ7Rdv3IDVckhBslzoMdVTSHsxMi7w6lcJlUdmgH5n2Z0JwLj-MuJh0U1ETmgRd83HZ8AzTRwJ6UAcM1cfTuIr9epyGf9mKgV9FqtHRS8A8HXm2uKiemP8vemeZymzh7zqQPxvAABfi1gxzPHg4XkxYpOr2QQFJRkHamDIK-kw4qhHpKAjtDluSFqftMhvrjBzy6dm09oprWE6SUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=TrxESjRi9J3jrCJksBJtbVKSXlDccjU6wx6lzgmkXAHn1ikiiLR9sfCPAwq3iC30fT0PwmODKoQ0H-0F_wacYS9jH6cM7NWmzs8eWJA2Fr5HliRVWDpzioJ0yzZUfY2k4JOxjcJ7Rdv3IDVckhBslzoMdVTSHsxMi7w6lcJlUdmgH5n2Z0JwLj-MuJh0U1ETmgRd83HZ8AzTRwJ6UAcM1cfTuIr9epyGf9mKgV9FqtHRS8A8HXm2uKiemP8vemeZymzh7zqQPxvAABfi1gxzPHg4XkxYpOr2QQFJRkHamDIK-kw4qhHpKAjtDluSFqftMhvrjBzy6dm09oprWE6SUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_aPHtfHLUSnat3PDWtkN6eKLegJE-i8JbWJZUUYFr0b-cbGfUJVsoDNdzfG9ub3MBrIoBZNCcHJ-B-W4YUePJXdyujYt5OMR3iVRYXcATUamiWcOD4vnt311Zw_v7au0d-PhPwA4KoCRFKqbmm9zMXlBQfvCvqtV_zYUZFra8Ku0KK2DTFiDD8nAm5dKnEHQnOspJ6fQLTxvcbgGV2nL33RqZd7JmIs-SYDMA8Dt_GqZyGIJh8PE3TQvnp5TxK4PPPZFpB9Wtc3fLd9b3WYTjP_whPtd-_AcbW_vz2OK2cWIPpnkLtX_4Uj6QuZ9O1ZJvzLZClo5ilxeJTzepGz6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=J52tOIWktRfO4LteClWxTgS2z0xRCJogB81P9FZTpjHJkdohOcpPNmYPp4D-n7ARRACKfNnDuWAscLfG7DkNkcTk72RAGqzuIyy-G-IKBkBA6DXWqnFlw3QHbUAXxRWnFqe1K2SkuxPqIkAW5QHe8trZzKepr0FBq0G9rM2U9n3rFtvUSnTGFNK9BrRu_iy3NbOQ7uhFOsBM2Idm5tRsGOl_RHQy1gbD0my7ymxyGZc9TVsBXY7zscWIS3VDv2fz4QOQQBm8zlv0ZrtZfxr5gr9sT_xzsHSp9eNYIzDt_edvbKtd6Byy1mNDtYXIFF3j7a17OijTqilwychfxUb9dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=J52tOIWktRfO4LteClWxTgS2z0xRCJogB81P9FZTpjHJkdohOcpPNmYPp4D-n7ARRACKfNnDuWAscLfG7DkNkcTk72RAGqzuIyy-G-IKBkBA6DXWqnFlw3QHbUAXxRWnFqe1K2SkuxPqIkAW5QHe8trZzKepr0FBq0G9rM2U9n3rFtvUSnTGFNK9BrRu_iy3NbOQ7uhFOsBM2Idm5tRsGOl_RHQy1gbD0my7ymxyGZc9TVsBXY7zscWIS3VDv2fz4QOQQBm8zlv0ZrtZfxr5gr9sT_xzsHSp9eNYIzDt_edvbKtd6Byy1mNDtYXIFF3j7a17OijTqilwychfxUb9dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwLh4jE8r0PV_NepaqiVwWbQcoRl8ZbNBqV26FHE_Oyoh3QrhZtWxfAxJPOrDD3aMtsIMJ_baX5PRojZHHo3Mo5TU-jVNwAyW89Ikvex40QmWw3MYHGMge2NPoqIIgliFnfR135PxHbBxn1gTnHOxjDSTC2L-sEKMfrXbh32sA-m3b2DVLwVYA-kdmAsQX9nGlQ9QiCcghcZveRXQSrchmlKNGafG-sYKfRlgkU7I7jOxrAtOQCYH_aFkYkGkDsm4DfKbP3s1YkT5ScRpaD3vR3EbyI5zQ7udqKxldAklcX7tpB4Ync5vdWYJbZ2laFpZpfjiMlNaM36feUN4IqxTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_shd8-vevqhbQEAaPT6v3tONkrewCwv6hakgcpbLGGzTiak-hpAgXakjydpYRir3dlFNwmJDrPn1kqoz4VXYMw71yOTMpLo5je1AKbO6yuXR7aTfdwwNBs-6RQyXvBh9FJkE6cD9LCRRbObajGHhv_xOGJtu41cvDIAvhxyhsexvDOvddOBdHiCuNma00sOGnoGz0cBY_mTRzWRJiHKNSgSUGXpbbx4kZSzKO6ZQfeYzZHY1ePjpI22n8nmrz-p_WooQApb2MfNjsZMunwViwyJPnkYjD4H1j1SO_p-vg1fs7f9JBpsL35PPgbrMTQeLmUndPay7FQhvuatjSiBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=D_B6QOguQeEkAMDl9edA8cKEu1MRk3h6j-MyTcpwHQwPZg3fDAiTsHUdEBsd8blOOBpWgHccjngeXiPomY8WWC6MGTfolUG7awsLxvWkqJDs2orHeJt9cTYiZqjdqYQhf7DcOIdmpYLIaleoK_mexEMVTNnOWWZ17Wxy5b2nMzaWgVP1vkRuaCblnzJgda9WA-qHoxWLmOPSuqMnBPShqmXc5ZxYRZylcNYI1qGDi1MmTGPQZDlQafr-bJ_JKTNh_HP_uvjdcPBuzZy0ar0RtADgoR5djQ5m0BdOS26ag-mKNh-74m5WxUyX3Dm0gv1BLqj4o184-2i7IMMwyFfG_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=D_B6QOguQeEkAMDl9edA8cKEu1MRk3h6j-MyTcpwHQwPZg3fDAiTsHUdEBsd8blOOBpWgHccjngeXiPomY8WWC6MGTfolUG7awsLxvWkqJDs2orHeJt9cTYiZqjdqYQhf7DcOIdmpYLIaleoK_mexEMVTNnOWWZ17Wxy5b2nMzaWgVP1vkRuaCblnzJgda9WA-qHoxWLmOPSuqMnBPShqmXc5ZxYRZylcNYI1qGDi1MmTGPQZDlQafr-bJ_JKTNh_HP_uvjdcPBuzZy0ar0RtADgoR5djQ5m0BdOS26ag-mKNh-74m5WxUyX3Dm0gv1BLqj4o184-2i7IMMwyFfG_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=R6OkWghThFXbti4crh1pRZPSGdKH-B_aF7Dj0g80d26rhHIP8BW-nOJwvshcWxcuCr0U7HLTvDA-LS4SJUJe_HerLFLzkoOmsdK1QJ4OnxSzGvVrtaTa41arDqTs7mtnVObRuMmJA9ETuS5nJO1Pce8hUB5ReAqIA5Vh_xwF-dsvH8hIVbZaV0Tfa1yL46Zbwi8rU4w4WAvJ6i6yMdUnC9qamihQGAnyT3CuuyGbpKWV4oSUtYcFieUQ6RVM1cKMc5oynuMZQdDCKCxlkpizV62iumSh52y5pWELotuw585E0CXZfbg_vnr14sIEhg_BLvyzb1MFL-xIrTyPkFMmzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=R6OkWghThFXbti4crh1pRZPSGdKH-B_aF7Dj0g80d26rhHIP8BW-nOJwvshcWxcuCr0U7HLTvDA-LS4SJUJe_HerLFLzkoOmsdK1QJ4OnxSzGvVrtaTa41arDqTs7mtnVObRuMmJA9ETuS5nJO1Pce8hUB5ReAqIA5Vh_xwF-dsvH8hIVbZaV0Tfa1yL46Zbwi8rU4w4WAvJ6i6yMdUnC9qamihQGAnyT3CuuyGbpKWV4oSUtYcFieUQ6RVM1cKMc5oynuMZQdDCKCxlkpizV62iumSh52y5pWELotuw585E0CXZfbg_vnr14sIEhg_BLvyzb1MFL-xIrTyPkFMmzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی، فرمانده کل قوا ۱۲۰ روزه قایم شده :))
خودش هم در جنگ ۱۲ روزه رفته بود «کمین» کرده بود برای دشمن!
که در جنگ ۴۰ روزه غافلگیرش کردن!
«ما اینجوری نیستیم!
خود ما پیشاپیش لباس رزم می‌پوشیم»!
مجتبی کجاست؟  :)</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=HeGswjY3gvVuTOeb0Z2_1cddUdtdm_SRN7CAzcDJiJnl_-AbApluMYqJHAQBJBioEf5-1MK-667Sc6kTTs3E6l6dXonWlu5meBKlR5Usjc6aBHwI63XY4OoD1-cYmdgAitIWe3MU81sHDFw6EmXnqpFpb7sI5PMJq3gCV-YTnc3I5PWggg3NRvbdfuDkFf2u2De3qpeMxq7US_o0WYA7gtqvsKrvSPInEom_f6kLE61h0rRiRaD3abiLlutQM50syTsVg16WlCqMC279sWCQDe1_1-dALus6MlOz8OGQ5D4LQHma3rkWp7YMH3iKJe8b8mDVXixuLnk6GWO0A8SghA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=HeGswjY3gvVuTOeb0Z2_1cddUdtdm_SRN7CAzcDJiJnl_-AbApluMYqJHAQBJBioEf5-1MK-667Sc6kTTs3E6l6dXonWlu5meBKlR5Usjc6aBHwI63XY4OoD1-cYmdgAitIWe3MU81sHDFw6EmXnqpFpb7sI5PMJq3gCV-YTnc3I5PWggg3NRvbdfuDkFf2u2De3qpeMxq7US_o0WYA7gtqvsKrvSPInEom_f6kLE61h0rRiRaD3abiLlutQM50syTsVg16WlCqMC279sWCQDe1_1-dALus6MlOz8OGQ5D4LQHma3rkWp7YMH3iKJe8b8mDVXixuLnk6GWO0A8SghA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LO1BpHMq_YsFRpXHA9xWHfK_zXl6YT_6rMsb8BpYmQyEYB2nu8CifX2zCUTPQbXR06DQYtqFgeyOlqNGpWf0BeG2Bpb1zKphJl0uJz8DuXqiEmnhyeRUy5RFk7YuxgQY3R4X_fjQBdGmFynj_4IZW-555uecXlFphkD1SrRvE-NQ7H1ZrQQYP6cMnAWiEOpwn-3CYQkLTvKVw2gg0da6Qlo0hkfKRy61IMyYkeaNezIuxiNYlPAfxnIduA1tu12QXrY9_qQJKeP7vNgOKa41tIwqAwaguTbyY8wXLBx1eHPkOWJqvEiciUXsF47Ruqgc184XZjLY0ashRERjiR2h-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=HhL7u_Eu22Ujm613fJZpvxisA4SEuZPrciufOd1jMc2XwI3thSh9tNQrXS96URkeWy0K3g6QY0y3U3o2KGf8V4L8cF0ximBhqpaovFvyjfGI0q-2ygDlvFJ-hLWeQfdxQbKSn9nQYwcNTOxlSg75X2FtO15H5nPPbn6EdFo-nzzKDnD5udHE09lFtFIUNIM4Wo9jQ66OXJ2rUrcqGF_xOoPSGR-ePyns8-otG8x2TIQd-sIjS1zaKtNpEpnE1mIob0ESbWkbbz83rcChir3xFOvLl6egSU3DuH21pgreG8bfZBMgtjr1sDOlxAYtdFWLOlU_JoNtFIH1qUs51q-enw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=HhL7u_Eu22Ujm613fJZpvxisA4SEuZPrciufOd1jMc2XwI3thSh9tNQrXS96URkeWy0K3g6QY0y3U3o2KGf8V4L8cF0ximBhqpaovFvyjfGI0q-2ygDlvFJ-hLWeQfdxQbKSn9nQYwcNTOxlSg75X2FtO15H5nPPbn6EdFo-nzzKDnD5udHE09lFtFIUNIM4Wo9jQ66OXJ2rUrcqGF_xOoPSGR-ePyns8-otG8x2TIQd-sIjS1zaKtNpEpnE1mIob0ESbWkbbz83rcChir3xFOvLl6egSU3DuH21pgreG8bfZBMgtjr1sDOlxAYtdFWLOlU_JoNtFIH1qUs51q-enw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=U9Rz9Y_EdbnvacqymgNiyMJNztOuulZ43La4xte23ntlp39kn7iMaK-5GgcRwTaKVNt9bTecFZAmUmlV4BftQmii554gCmLhTzluCgskfNzZkdEpmLV1f_CK6nk-em9AYtNovTFcWOgiiPXGZR0nb1FdW8__iUV27JDGaodyKgNDtY6A387iClSyUCnasgW59DzGjXUrCrZiZXHtNdHH4dOsDxphL5vx_9RDOmqZdC3CfrBi24ON2fw-_3xJjxXYlZjwth3LSPljOFWDu2eZou1xamGzMwAQYReSCPbGLfK-TBvX16F3bYDjN5WL_fHPZORY_9aiQvU5kXXetUp_KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=U9Rz9Y_EdbnvacqymgNiyMJNztOuulZ43La4xte23ntlp39kn7iMaK-5GgcRwTaKVNt9bTecFZAmUmlV4BftQmii554gCmLhTzluCgskfNzZkdEpmLV1f_CK6nk-em9AYtNovTFcWOgiiPXGZR0nb1FdW8__iUV27JDGaodyKgNDtY6A387iClSyUCnasgW59DzGjXUrCrZiZXHtNdHH4dOsDxphL5vx_9RDOmqZdC3CfrBi24ON2fw-_3xJjxXYlZjwth3LSPljOFWDu2eZou1xamGzMwAQYReSCPbGLfK-TBvX16F3bYDjN5WL_fHPZORY_9aiQvU5kXXetUp_KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=kLgrvB1kVGY3uO0ixsqKaIkB10M8riLU3KZQdDJ7WPB1XLZgKEUAvGwRRyTR9hhGZlpF6XdhFjxeM8ZqQdBHyBsUVml96LKsh5RLf6rIkRrBOflafnKBdDJdDQ4Y-Ty5MB_VMLvgFE34t7g4HwnUn9umZ8SgWaTHDmvTmFkJj8euCBf8L67AVqiN9Eogks9DJmiayAzq7e7DTeXWay7LqZs0w_v3PfPUHMudTGupbExdyR0OfsYxBUyALQ4v5gcBoHlQkstfLoLnC3Vbz_5NWFOqA1gKmBTzfXyADdUQ4TPkk5vUAWMqLCP4pTJpH5QX35DqoxV-mrvq7MiJSRZiEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=kLgrvB1kVGY3uO0ixsqKaIkB10M8riLU3KZQdDJ7WPB1XLZgKEUAvGwRRyTR9hhGZlpF6XdhFjxeM8ZqQdBHyBsUVml96LKsh5RLf6rIkRrBOflafnKBdDJdDQ4Y-Ty5MB_VMLvgFE34t7g4HwnUn9umZ8SgWaTHDmvTmFkJj8euCBf8L67AVqiN9Eogks9DJmiayAzq7e7DTeXWay7LqZs0w_v3PfPUHMudTGupbExdyR0OfsYxBUyALQ4v5gcBoHlQkstfLoLnC3Vbz_5NWFOqA1gKmBTzfXyADdUQ4TPkk5vUAWMqLCP4pTJpH5QX35DqoxV-mrvq7MiJSRZiEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVDJzBWK4qUboWaRdrL-Q8gzAZSwerLjBf7MPwHRs_ZZ873Coetr2nkkCPK6OPcJZf0ehG7uQSwDXta3gb_bHG6J8mMmcbTJ7Kg5PffwTbgkoUgCl2P545tknAcFyYOOKVScBB0ZEkm1ozUixMd_t5ij0s8nt1-PCo1MyymW5Jiv5K1adMplAa0mAyz2CzPYybTeXoA35k3uNisYjBqQNUOKxEWQWcPH0ltLmYIQV6FfOi3C6rxlvdploQo-8SddKyVbVZNUhpAwXVT9SO0ZNM5GmHAzgLEzgJ9FXilMZ9hHi1VUDqITIxlXEMupyHr-80vcDEvbYWDRm9KNOhXV9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=neINQLjQmyEGmxjtCrTrNTEd1jVWgeJmAIr_NQPbwCfqCSQNqevA9_szAYFewE7l1ugMAy_zaQqB_CCuB_HQndlN9xrRJSE0n8YOGj5sNrZX2eDDHFic1QwvWju-ReUniUdchZ-kXddhrAi30UfkiqMG7_dS_3SkguBB1qHnqBMIyU7x_0g_4B-tm2LgmbuLHw3IxvhpfOPI697pfv7T5gqhSsQ25gYKvIBp7C-_VJVfl-QxiPxsrzKzVCbWjtY7xsT0hMZdg70YOQ9I88iaswSN6Us02MOP67Rm-k_2A43sTGw1Bl75ny2sY4X_Jyg_XS4j6mZgpD03EjOStUK7tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=neINQLjQmyEGmxjtCrTrNTEd1jVWgeJmAIr_NQPbwCfqCSQNqevA9_szAYFewE7l1ugMAy_zaQqB_CCuB_HQndlN9xrRJSE0n8YOGj5sNrZX2eDDHFic1QwvWju-ReUniUdchZ-kXddhrAi30UfkiqMG7_dS_3SkguBB1qHnqBMIyU7x_0g_4B-tm2LgmbuLHw3IxvhpfOPI697pfv7T5gqhSsQ25gYKvIBp7C-_VJVfl-QxiPxsrzKzVCbWjtY7xsT0hMZdg70YOQ9I88iaswSN6Us02MOP67Rm-k_2A43sTGw1Bl75ny2sY4X_Jyg_XS4j6mZgpD03EjOStUK7tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoXRpyboP7QwKUOdKuLDs872iHYAzLPiSpv8yDh_8QqRSbObFkdbzNnvWANbRpeFDEiJoiU2dWUae6UhzOhi1PqAvOySeJiKNTq6P2xMnUy8CpQfR86NL0UybZNth7AzV6NK4DflCHYI_wYr3kz-Oog0P5luztrY8jZbrhLrxZe1PRYUuHfY4-1L3BJJ867FjNkQN2HcJT4cWpwuq5eUXC7OiJqgNV67kQZFuPzoxRy4ocFYRSp4VU1Y9aiykFLfQRlZPus3Dnfeye6zzRHFif5xCODWFf7NbNk3kWGyfA9KEazPfn6rRZkr-g1jcD-ZWk0GVGavbvWYjaJebPRPUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=MBzxUPAIGj451DdEN8-xeIW_9yRBFwDDEcPBC_gcApTl8qq8QcVDpM9wM8H7V_CbdxSjmDEeFxjhO_JPE6SaUUp8seLBrRAFy-6dKTqOzYe9xqZO_5SfXe90B34CxI5p-BnzHmaUdmw0tNJvlV8slsljTET6vKxoychknsT6zc4YHOV_QxGHNv3jAkNMeQYC3QxDOFEfgbIMkTtdoeuzBiPvWtqnOGNr3uae5tfi7gC3mpoa3vNBYCYcBWrBV81FkR1JCr7G4VMnm9mH0BTnyhBK10xhL8oR5jUfQ3htgsj1z9wj9nD2lBPhlBig-kkFD2qwGjw385idFwqpfwcgbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=MBzxUPAIGj451DdEN8-xeIW_9yRBFwDDEcPBC_gcApTl8qq8QcVDpM9wM8H7V_CbdxSjmDEeFxjhO_JPE6SaUUp8seLBrRAFy-6dKTqOzYe9xqZO_5SfXe90B34CxI5p-BnzHmaUdmw0tNJvlV8slsljTET6vKxoychknsT6zc4YHOV_QxGHNv3jAkNMeQYC3QxDOFEfgbIMkTtdoeuzBiPvWtqnOGNr3uae5tfi7gC3mpoa3vNBYCYcBWrBV81FkR1JCr7G4VMnm9mH0BTnyhBK10xhL8oR5jUfQ3htgsj1z9wj9nD2lBPhlBig-kkFD2qwGjw385idFwqpfwcgbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWcDt0cRKMaqel3hi7Iowm4haWMdKQKWWSfQO0zksnBQorAtIdW2YXFrxeHOkdQTl4nSqVHhjm7PxlG_Jl7YgVdjkqSchhbDX0W4yyEPZoULZlDtqbiL9t2gZ13uVJAX-Isgr6jTIpcAvfI71XVEJljTXeressTTEfzhM0xC0yzeHUIf3fAPu0GzjhY3BiryIoTv7mT7MO-iwQdvAlTopScb_6SQsRxP8XuGleiwLg2hXa0AcoNfxuE-p0uPj5Uu9-f4qSuEILBY2XfgB7e8BR-CDbr5smPf81t_kIfy1x7UOGEB1CDrQb_hgJLTHTXbH948AtHomjk9kJ-1WOZcog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=FN5b7BfJUYvabKgWJvpxykHG3RGDohcfIeBTBy_uI11AeHu8pcLyeKO-jrKyCE2KATfGDUULoSBPaq9jOhRMXL-DfkYHDkRVcHx2x8nfU4SbkiKY6uieVPrc-6DS37ga8yyaOHpDIwoZ4357TnRbClmbuhp8ZoUFmghMDrOjoimLscOzS3283A9ZPBMkHyphodLM_Lo_OgRLQSM_FefP2RfY_C4jQdagOC1dtFJ3Qdzl6rktBwylTz1XXfCmerrihjgbb_w2g0FUxKpSGnuO5CxhQno_c-BYpUB_840OhGWg0ciHja-FU4aaHUvkAJaBkTj8TS8lqgNxZZzEYCBY4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=FN5b7BfJUYvabKgWJvpxykHG3RGDohcfIeBTBy_uI11AeHu8pcLyeKO-jrKyCE2KATfGDUULoSBPaq9jOhRMXL-DfkYHDkRVcHx2x8nfU4SbkiKY6uieVPrc-6DS37ga8yyaOHpDIwoZ4357TnRbClmbuhp8ZoUFmghMDrOjoimLscOzS3283A9ZPBMkHyphodLM_Lo_OgRLQSM_FefP2RfY_C4jQdagOC1dtFJ3Qdzl6rktBwylTz1XXfCmerrihjgbb_w2g0FUxKpSGnuO5CxhQno_c-BYpUB_840OhGWg0ciHja-FU4aaHUvkAJaBkTj8TS8lqgNxZZzEYCBY4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qwH7k3tAkUKOiPVLefWP5jfsvBnTPMCJdPwXeX8IvKyC4B-kUzK-lAy_1AOSF4U4llbWbn0nwwUKvOxikEOYmwBsmI5CDEomes9yVQ26pDlFShCoNmSs-CuIupU_inSHznP88Gt9AdM_NHp1RVAvb3JGR6inEn8_j_4oojm6_e9d_gPW-t5PDf1pW1EhduIkEdoj1sFm1wbvebBagyFnUJwccrp86-9Uoned3rc2qcCw6vkL51Rl0paigHfiBf4_Bmu44SUg3VJ0Ldj1MAGmn2zUqOhAS04Mzq2tf-eaq2Tr8grWw9aXmBVejTym_8PlcPSl3s3brnCiGHm-6mdbpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mugbDKU1vroqr01rIe-lszlJLFb2C3EolrQDFQpikFoowqS-55nd9EdliXkgIfG85s6n_lNI9LjCqd_aqRX7e_sjh2nh6r9IkQwDGtKsKNmbEW3BYWH4qXKcb1xxU3T-816D1_3sap9GEkjCxRKsLxj5k5OrgiV0XrTJRZmkriOFvy5fhDHrJVqalXnFoenox9hcVMg5Ht0a81-IFYE2CZVP2XYOsEGsrlPej4akzemNuUOK6KoyagPHb8Bc9TD4wd1MWjgJO2adS89tK2PeG17JXlEHzNGBb9tQcgKrd2e2Pl9l1XC0QGRAgwDcxxqAbseH-x2q0saLyXvw5XkdxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=DYXBWiInTe14RDuL44cxK2novG6hhvbvcH8xuBnI2k_zHgn48Vqp1XtQ31ioEHZ8uHdz7_fvMZIco73zmiQ_mkpScuGiq6tw0Bf1tDIO6MCFSlzllXbbWzlplISMNwJoFGkd_ztn4QIZhkhbrc0Qaj0Wld9wdaIHpG4szcooFV8JF3UVNww4PTg8WJv-g--zxyf95K4Uxc75Q4TQrjmhJdpbzFLkvBXyBxhMB-XtsI-9QpwNKfjsDZz2d_UaTAmbHTszPeKDhTXqH6fWpWuevkpZL8VYeY4xIL_f4aS7vwSoin3OBkTz8clJd9TKYLI4a3Yff1UZ50eFKrI4hJZnqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=DYXBWiInTe14RDuL44cxK2novG6hhvbvcH8xuBnI2k_zHgn48Vqp1XtQ31ioEHZ8uHdz7_fvMZIco73zmiQ_mkpScuGiq6tw0Bf1tDIO6MCFSlzllXbbWzlplISMNwJoFGkd_ztn4QIZhkhbrc0Qaj0Wld9wdaIHpG4szcooFV8JF3UVNww4PTg8WJv-g--zxyf95K4Uxc75Q4TQrjmhJdpbzFLkvBXyBxhMB-XtsI-9QpwNKfjsDZz2d_UaTAmbHTszPeKDhTXqH6fWpWuevkpZL8VYeY4xIL_f4aS7vwSoin3OBkTz8clJd9TKYLI4a3Yff1UZ50eFKrI4hJZnqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dw2vgnNyZ0Jp64uSRAQ-xHx5Bq8QOw6MU9t31qg3DnBvovJ_Ru0B3np4zl-SRmxhRdxKWoCOgk6NStWFpr9deR8EzyXKAFVmsesPZboKAtdqOvslO9tx4etZ3drpiSAlJJeJxMZTVzRUwFq3D_lJ0hg2T3WS_BUf8e7UbZukSG69I1Lgq7Ce1kLaRnG8DbssOJRjUo5doOMlyNW_RhNC7sor857jPb-L_3N4vUB1IgD2A7m22OUMVjWlREflnLuEPEzwzc7TyIN_viW-z9Onca7tDQwOk_Nf7sHcNkjUx9rJCvv2kruXolQ5wTbvblBdsP9gWR4gT-mt3S23YZhRTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tp5izpDLNNJ5_HQoKiNDcCCaOYEP6jDlMCpdeu1Pm3MHvpL-aI-cNlbh1OxZ6wTYfU1y51BF-G0fuFZ5gvJ-kBtAoCVZxxJLrCGxPwtGSmUe54yIPiA_fI06psbV-rlVJCOPzbZ2cpSZl1w_6wQMg6aiJFLjjNrQLkAI2LW8XxNAFGJoqBeDNUEfAoLsmQ7OeoqDpRWhiU8U4MPKsAcPmqTd4RenjuFBCxV9iSWlC7MGZMkayR_q2cLQPQp9KeXAt-OSN-oB_o1l2X9Gaf2SyOcw0yjTb-9GFBBG-VyUQS0q4M5S89giMmih_9MTXMP78-sCnxKm1LDRZNuFD2uW6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEIAds7YNVGH1U6xqejsdUY48kpBzKU-RaeE5TIF2rFXQw2oRfIFcJkPo93YXdusyUDDtaajdxvZKrjw0IzJBJo2sqJ5g6OQ8CuWUC2gnvOwdX21tj5OxSD1SlTfwpgXkBjvWavn8PdcHOPV0oHX1mJUVl2YvrkLiVo4WPP_YZsGbhUFJuYG87KosfT-MA3ayezQhxybUytD8HnvVr1Ytg8wwA2xom2aLAbStr1JoOTAYMpvso8yO_uqvsS5HWlUGPD2hQ-avaBOZ98sfX1RtnLzwCkJ-yq5vsCg4DBfn3mXryxtRyufWf3vh2o_pyYnKbNiifn0qLFZ0awMt2pvbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kmxuh8GhSgD54lhh9YaXrT1vtlG8tvUwj8f7GetSbyh_-YkC50-OERP-72Lkzm32ZjpnytS_vqDwq6DwsWfzhODbswFJ5tOwezt_wV5u0e-Hygx8eO6GjXCZ2-6XoCacYXb57tQspmywzoryoi311Ozbj7SQwW284Dn5Z9csrT1xYeVABklzCIc9dPDe3mxLDEMUR7C5fh8-wV_QsJvfB-Rat9SbI-lsaD9HGzToqlQ3u7pHmeTWvOxz6ss1xAoAGL0rMrxbk3rG6kA2y8f6lisK0e77JHXkVxKnsvwiTXq6HBgTyG9V7MmbtgGfXNsERGgcGaaneIcVlz8oxCtWUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RszXiHKA5JfKlHnRcugrurX6ctAKqETfIHTXcBHz2Mc2WdzzVL2SJB-tcCNdL9unJTXU0mchY8gHlxVT0BgUGFVJVMAhlAziSw4ofL1F7rrgnUf79iU6bGtz7RgbfNKUn2_9jrqip9xM9QwzuG3_GWv1La8UGERWFtZ5kmRlGW5BbyowLWRTdJJSyirFRGG4zJZIYtc-PqUYZpuKphz_eRrQVAm1hxEszqJc23ilAuCc6p1nIzB_Pa9eWEAus61Jc7GQt7x7yHlhh0-eaAte10_47JtjevgAHGbRwYVrGTGdI3Lj24oufzCZ6YcliVfKwGd8mBMFUkYCEi06qPnYPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=hxU5DReOxrs_xqOqYthTs2cy0BGq0NgNAq-shfK7aL2lL6olvmtWplSa6J_39Hcg98X135SNZZ9JkYQCrNWgiC2yf5-yOlHVToNwt9DyRp4jP-LkJF19u90PiTgpB6s3i9FcfL9SAEFn9b39BxglV8CDWstN2oXzL9uMuW817ajKoJrrMX73z151azpV2uulyjc4kXW3495Srl0IntmYCKUqH4HBgkt1Cr7UMYmnQuPE0G3PER8vfE91BXPujCX2ETVgIOQGbbZW8whjO187nCesV_Tg21j4TgWOgQGndnFtx90q5K2ywBgXfTplQghcHTeHcb-Q-W14HBM1FsMGlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=hxU5DReOxrs_xqOqYthTs2cy0BGq0NgNAq-shfK7aL2lL6olvmtWplSa6J_39Hcg98X135SNZZ9JkYQCrNWgiC2yf5-yOlHVToNwt9DyRp4jP-LkJF19u90PiTgpB6s3i9FcfL9SAEFn9b39BxglV8CDWstN2oXzL9uMuW817ajKoJrrMX73z151azpV2uulyjc4kXW3495Srl0IntmYCKUqH4HBgkt1Cr7UMYmnQuPE0G3PER8vfE91BXPujCX2ETVgIOQGbbZW8whjO187nCesV_Tg21j4TgWOgQGndnFtx90q5K2ywBgXfTplQghcHTeHcb-Q-W14HBM1FsMGlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=P1ou05w7piCOFZgK_XL9MmN9NVHicrTd9e0kEUZAGXYq92I3ky-KF6cLeFeygBzqvDqdA6VheB_yjrS45-NKRGZ2_fbnhirQcVVzdj3Um95MgIHfN1faPtmX8UCc2WnLl-ZwYH-x_mLuOrSks5UDIRvfvaBOIMBf-2Ck-M0BQ0FCKVzQgGvQUv2laQtxX52Q1Hg3NLgBqpN0M4yxNtvYq46g4WmJRShx1i3pkaj6ShxZ3kQvEKRq4MQde1_wctMGYTVuY-hGHOKu_oPYXIzZc9D3HaVfDPCLQjrZ_MObgnnnp7zepFQMEYqOoC4NoYv7__SJn3yk41X3uKB8CdHlUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=P1ou05w7piCOFZgK_XL9MmN9NVHicrTd9e0kEUZAGXYq92I3ky-KF6cLeFeygBzqvDqdA6VheB_yjrS45-NKRGZ2_fbnhirQcVVzdj3Um95MgIHfN1faPtmX8UCc2WnLl-ZwYH-x_mLuOrSks5UDIRvfvaBOIMBf-2Ck-M0BQ0FCKVzQgGvQUv2laQtxX52Q1Hg3NLgBqpN0M4yxNtvYq46g4WmJRShx1i3pkaj6ShxZ3kQvEKRq4MQde1_wctMGYTVuY-hGHOKu_oPYXIzZc9D3HaVfDPCLQjrZ_MObgnnnp7zepFQMEYqOoC4NoYv7__SJn3yk41X3uKB8CdHlUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=WPYLUfKZzRclSlI4uPD6q2IYP8HaC53yQC5y_ndX5c4hzFMujWMN9o-IyHZm5WcZadG0fXbvsNGINUF0KJ1X9UIQJV_oDQYVhOvszFO1OvM9-yHDWs8omVueCVOSRwWy-cPbNGOMfV9JI9J7fIlWfMMD7XL8UA_NWO7bCx34zfN75rM4KzbAy8gAyn0-QN4ujeCwS8Rvqw0OqxAdm9A4AIKU8Qrt3AKI2UjtL1j8TznqiARz2_cC4s2VM7L1ftJ1kijif0IeCwndkyMLYEglzISvQWByC6GZY28RLtZfgufH43G-KnTTydAljikagMuYMMDOprcH6ZI5bL0qoWc2qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=WPYLUfKZzRclSlI4uPD6q2IYP8HaC53yQC5y_ndX5c4hzFMujWMN9o-IyHZm5WcZadG0fXbvsNGINUF0KJ1X9UIQJV_oDQYVhOvszFO1OvM9-yHDWs8omVueCVOSRwWy-cPbNGOMfV9JI9J7fIlWfMMD7XL8UA_NWO7bCx34zfN75rM4KzbAy8gAyn0-QN4ujeCwS8Rvqw0OqxAdm9A4AIKU8Qrt3AKI2UjtL1j8TznqiARz2_cC4s2VM7L1ftJ1kijif0IeCwndkyMLYEglzISvQWByC6GZY28RLtZfgufH43G-KnTTydAljikagMuYMMDOprcH6ZI5bL0qoWc2qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=IG_-efe-HmMEU_pUjEbcadHe0TNKucdnmpmbT6kZyuHxEUQwMPnwNLOvkQcOy2Q-c2v8EkYz9E3h6g6g-tsusq4irJpWdvdQGB-421DM4sGTcGKg6cUs4U2ai4NxjiidWrAf540e_UwERcaAceR2wmf4g2Cqq-vRAkL2CMXvSQ9sna0ExRzY1Ty5EnQ4QxxeH6NFgvC9q5M8YHcl_gTYGVYchVWIv-Y0-8WYpz3v7xKrMwK6v6bdxR4wvmAl8QA6_vU4ddoxZ9LMIxPAzRS16K3PSuXmdSq51ukfvdWYy6OrsO5EJgDk3Irs4rM_NA8TVdlAK6qk5Qw4fH6D6kXfLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=IG_-efe-HmMEU_pUjEbcadHe0TNKucdnmpmbT6kZyuHxEUQwMPnwNLOvkQcOy2Q-c2v8EkYz9E3h6g6g-tsusq4irJpWdvdQGB-421DM4sGTcGKg6cUs4U2ai4NxjiidWrAf540e_UwERcaAceR2wmf4g2Cqq-vRAkL2CMXvSQ9sna0ExRzY1Ty5EnQ4QxxeH6NFgvC9q5M8YHcl_gTYGVYchVWIv-Y0-8WYpz3v7xKrMwK6v6bdxR4wvmAl8QA6_vU4ddoxZ9LMIxPAzRS16K3PSuXmdSq51ukfvdWYy6OrsO5EJgDk3Irs4rM_NA8TVdlAK6qk5Qw4fH6D6kXfLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDkumP8EZF6-lC0uPTZnNl5GXRUS17IjGeg3xSMeanMj55TWG23t93l0eygLLDqTynVwmG4g5s08pAr9j85kjTTAiMS-hxiGIXN0a1yYNJu5mR_2stDBVgb1AqjWQseLR83i-fRKIUExLmPkV9qUxNU3ELQDLEHke_9pERrBehE6fU0PoVrMwCZ_zTcrbNH34R4tlDsp2UDQYdIgyaRcggD6S_gIl_bmgnkrRcklP2IzsZ9tHSt89PXFp4ghgoKjfpE1Bo3fJI3lX1gEq6iVPxRAwJCcQYbfZzp2UQcfw-n8XKnO7GMj8jFD_BT1YZ_d4s8NIxzzXmDoDgWEk2j7_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URxUrGebhI--qwIqYv6mra6tuNavPKrWq9xG8TSq2uddJaFwV868gZwp62LByWFkB5vDo4SyLs8DKtD7cFPfO7aGi2eboz7cPwHhenVdFswu9HZq3J-LciTFq22HiW0VXuc4iudogB_OmQ3eCX2920Zpo5SIJjx1_tBs7tcHlw9zdSr9MSB_UI6QTg-fy4aroYa-6B3_c9ZkmJElURqYXfExbTyhjB1uGCawhZJm_LFV5Gg5X_cZeZmT5tVfAKQuIM5ckO8r1UFlMzcLjgQ-D6p-SpSHOXYVCp0AkhvDgfgqykmd6wNx4Nj-SXV2SxsoHc6vapMz8tSD54s_5yMQQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=tFomIv1nK6nPzBRmVYpAwG6Xe2oBYHdO6L8LUyLoWH8qt8stS2iWTLLNG8cBR2gX7pcTCklzWtrVTt3xbAcfVecJfNysY_ukM1HaZhFnp0H0TKK8YaU56PevhYVdCeme3GrKeqjRkb9nu0iDFTNYZzWbUQQKnJpZY--QVmzFBIOzGgmXcG1UrkYpTdfkEVy7fe52qOdu6mdrZ21GuPnyCje2gDw3NvxPAu6Q5q6JJ3uWiwSIKfLCpN3L1RLfPFp4HfElXztq89xHQkQ7QWQV11qI1_veVwqwBKDAx-xFXFV1sZPOjNvvvE5TsbquCrveCix1zIbfEOLgrG6MuEEreA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=tFomIv1nK6nPzBRmVYpAwG6Xe2oBYHdO6L8LUyLoWH8qt8stS2iWTLLNG8cBR2gX7pcTCklzWtrVTt3xbAcfVecJfNysY_ukM1HaZhFnp0H0TKK8YaU56PevhYVdCeme3GrKeqjRkb9nu0iDFTNYZzWbUQQKnJpZY--QVmzFBIOzGgmXcG1UrkYpTdfkEVy7fe52qOdu6mdrZ21GuPnyCje2gDw3NvxPAu6Q5q6JJ3uWiwSIKfLCpN3L1RLfPFp4HfElXztq89xHQkQ7QWQV11qI1_veVwqwBKDAx-xFXFV1sZPOjNvvvE5TsbquCrveCix1zIbfEOLgrG6MuEEreA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHEGK_COFd4WCbmzh4p9gkyb2ymvyCOA7LRznRf6MZICBV8nh-VXDenFcNaOpY82061FiSEdL9tCYi9c4BblvRogvWHNdcJ0U5BPPdhuIQCpxB9yszveJAd8CjxbdOEb_12h-jFJxtWSOrJl8-eARYfkkydqkKaAa_EQRiUHypdt9-oHFok5FpXkgFxkj53GRpBN-XkR5l4TGkxk8WBjd64zkG4ViHL9DFdTi2OX4yz4mRCl0ZqDoM-jgoUNJ0qyeNpalFPIj0WWL2QKI3zt9qo3IW4-ctAUGCKT3GC9NzrngJtd1kp7LiTpUCJgajHK9c4uL-cljY4wUMlIBTu5OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=TCadY2vJWBdDZTJVJlgtdRY6g8h_U0CRkOdCtMvgoPyPsi7CVgOgHffDrz5T7QZUbBnssSdspKYpKRsMbKJT4fqnrVpjUw7YvHSbNmzVjQSmL3-queUi2qLKM4RhzOxYwuV9jajd6G3n0UfCJ2mKtkjdYOIrMjYe_FsQFQNOHoWTNnmNh5zYQ8xJNbPLwfE7Nf4bPZLPw4WC5RKlDuOCdCxUvWYcylYDd0mCOrIYLEkPXa0H-lCiS-SBlL5dhwZv75FNG98TtTx1wuqCZENQIFAJmtIX9izgp6kBdIAMmfh0pXmAp_j70-yd23yrwWvENzPb1rw1qsd6cY_zxTNcig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=TCadY2vJWBdDZTJVJlgtdRY6g8h_U0CRkOdCtMvgoPyPsi7CVgOgHffDrz5T7QZUbBnssSdspKYpKRsMbKJT4fqnrVpjUw7YvHSbNmzVjQSmL3-queUi2qLKM4RhzOxYwuV9jajd6G3n0UfCJ2mKtkjdYOIrMjYe_FsQFQNOHoWTNnmNh5zYQ8xJNbPLwfE7Nf4bPZLPw4WC5RKlDuOCdCxUvWYcylYDd0mCOrIYLEkPXa0H-lCiS-SBlL5dhwZv75FNG98TtTx1wuqCZENQIFAJmtIX9izgp6kBdIAMmfh0pXmAp_j70-yd23yrwWvENzPb1rw1qsd6cY_zxTNcig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJcXoVpwty262WtJac8dQyDBwiemUD4pgHl8IPlHV6QOAgmv2ZxOWLiUOEUUBMYbBZlI3Tvj45mr2XPDHMxCh4uiFsUIpUW4fJGCftnl9vDKwT2XUbEskWi4I5otrpt7Ac7Oymp4Wn5TKc4mz5ZjqGhkLKiY4J-TlrNdpEDhyIXkT0aQUJxNmoqIV8p1Ppe30JkmPG5SXLvyAndv7MCQdu4EQPRn04ANmHBBp3sOZr3WA8GjLONnrZ4KBgFzfG1HibdLoOzZnvOvTe2XU_MHE9Ll3uHkAsZ36mjNMJV54CeZ4baA1YR9jh_3ZLcQuuuBV_9VRyFC9hTPlzaJvkMtig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4eh_OVlfpoTv9KIEEW8Ebn7sz0Ekn8WdvzqDOnJgBfhOM9lNz9sRjfAsAx9NuxzkN-er_urYmaQwfWjhK4ST-QMVGD1KbybBBPT5SOu9MuscvQPahoeCH7M_4EftCRjzgmFNmaqScqBhXs72AtiNeTAGbF1AbPigQBFPaMCVY9NWf_CZrTQ4reH4HYOC0C--CMbgbkSv2wxSp7dDwgCoJp-R2Ei6nt8pAOwtxkWOp0PcjDx4bH4NbM3DLDmP-u2rx7ulxh2-3-eJdW2HSx_CsZobdVXyFCkMzbS0-X_JfWqplBfGrNwNGd5oS72Lf_jkJrUq1UtUxq3_CA7wny99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=bzhI5pT_V6f2ao95iF-R7h_F1Ng4Mu10hJclunWQX7uW87TcuZ9t2uL1uHLLVyzvnMUrqCSRAKhrQ7kUa-PLEVB1S_gtxXYWfr3mEoS-28Th6FKpfJVnLDxpiayNAlr9VPVZuo5UuNTiDmp06dv2wm2NKjdQZJc1X-9Iy-1seIvagMgfS1N8wxMQIiLRNul07XjLuuGl8yGNctGgnuq4tVAcPYecStKWQJs-VCCfqyd5aQZvYp81T9HzG1tgGU8bwKloBOBpZ4BBUDxra2PW1wIvrJg6U-kPvHdGMptSagxvou2NY6j0_b3FFW7IffPsh2LETvzTMjxFPm2tbg8oEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=bzhI5pT_V6f2ao95iF-R7h_F1Ng4Mu10hJclunWQX7uW87TcuZ9t2uL1uHLLVyzvnMUrqCSRAKhrQ7kUa-PLEVB1S_gtxXYWfr3mEoS-28Th6FKpfJVnLDxpiayNAlr9VPVZuo5UuNTiDmp06dv2wm2NKjdQZJc1X-9Iy-1seIvagMgfS1N8wxMQIiLRNul07XjLuuGl8yGNctGgnuq4tVAcPYecStKWQJs-VCCfqyd5aQZvYp81T9HzG1tgGU8bwKloBOBpZ4BBUDxra2PW1wIvrJg6U-kPvHdGMptSagxvou2NY6j0_b3FFW7IffPsh2LETvzTMjxFPm2tbg8oEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=BF57U1M47hoLbZoWiTmqzUD7N52-7HRXSEmTX-T4jZ73X1JLYv-sqvzg2-fLqnPL4Rbq-R7TNSpm0i9wak7HEZtx5_PGZlQ4IqRtsS6DyGhqA2GEyyhxtTGV8iZsdb4YccL68gXynD-nYMj8Poi2sMrrkDF8vFlpp-rMHfTK0-L6E_gXh0rSh8Z8wxNzf0grB07DIHy50hQe7Jt3bgBrRHLmtDoboOYRULWTdS9o-_y5QWAkSs2OsFFBCVEYkjqV4cmXW-RFc9h-XcmsfG1_xKRnYv6ZOUJv_CXAd7F0XH6d4lgbO5XSH9V8mJfQVDmJQVA1ln8228v0UNYSkicdDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=BF57U1M47hoLbZoWiTmqzUD7N52-7HRXSEmTX-T4jZ73X1JLYv-sqvzg2-fLqnPL4Rbq-R7TNSpm0i9wak7HEZtx5_PGZlQ4IqRtsS6DyGhqA2GEyyhxtTGV8iZsdb4YccL68gXynD-nYMj8Poi2sMrrkDF8vFlpp-rMHfTK0-L6E_gXh0rSh8Z8wxNzf0grB07DIHy50hQe7Jt3bgBrRHLmtDoboOYRULWTdS9o-_y5QWAkSs2OsFFBCVEYkjqV4cmXW-RFc9h-XcmsfG1_xKRnYv6ZOUJv_CXAd7F0XH6d4lgbO5XSH9V8mJfQVDmJQVA1ln8228v0UNYSkicdDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8He7aFx9GoFLMTh1h_4-HKHz5HnWba6tNVOrQR8TjxFFtZParJr3g_uU-ZSD_hVu9ul1miCWbwRZjemj1FqdHyWCiNd9wki1D2r6QzVybkIlmv5Q2jhdT-3K2RU2h0bIo8OR6Dl5-ivb1a5YsYiub2zMWTjQg8NEVBzUUPZJU3Svp1qiHmIlkmYIXqFEWBdvGiwIFdV8grr2LjIZcztBRD_zYOb07-euJKyK9jCDSlM0NF_jccVXliFZMUFs_XKL5GQ8_6cAe1Q6di3y3tc5Bxw9NkiEESceUdVHMcTrY_tA1HIFTryETHiQeTwimX0ctug56HET-Esxm7IWT239A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOS-AyXJ2swXg21mKy1kUPx6nGbvctDCPceD1WIL9PvIvJqw-9W7DnEFXVLaxw7tdEJCwv3Bk0ZFBOFbcvBGKu72eWt6awlbAbAbvrqBJBg0ZRL0hj-A7p_ZEmujM9m2kU6lzxtUMiTknD4w1jepH9fz_2RpmX2EPAlbdnT-WzitQyzh7TTjFqwzOBHmKVIpMWwfpU2L_EbHxS-QHUyvxa9Ca7VjEhpRNdSEkbOyOlJB_bxjEobVbDaM7VBCwkuNjmpZBwIu3QMM140377NcXbQhnV8-sqN_f4jehzVUE8w7xNDL5YxgglJIYGnXxgCtUdATyIGQ7yg5Wple72j5gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVWu1IUP3FoJyBBD1LCbS9HwpVoaP17EjzqeOQgTcmOg8boxkYxVX7mSVbsvbMQrwCf8S0EC-SJ3sBsGm_pZXlX3aaAyxs7_Tf4QkA4FS5M8ZPpv0XmbGxMCxwE7z2qHQjv-wQEaJgplTFmn_-kYJpUqr1Yu19H2UzedOXy70AwX-88PpOwZW1wrkGgsmbiZi3GFVbKcfuXfNvZrq39CFU2FaIxZdgRBkwKjIWnBWg2l0mxaSpJKNkreRCDC7FhPwLoi9e83jjGhRO2nmEKhdAN35XlSVsWhOLjhTjilTjtKuefyWGU1Yw9Wvx8lx_iKBOcMrDCGO8Ny-_4lkv4ltw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=HgZJ74G4mQhrivTO94HL7noVcB3E87hdY91vCaexdTbBCXhE04WEyuU7SQAbsW1pI4qB7GtyLTQ4te6yY36BCDuZrNZyXk007HdzoOKR7lfHK_kQal7J1SAGTVcfM263gyiZ9Ns78i7_VY2HUr_P0DUyyVl0_yJRn9pNn_6DS5xIGB6deIO7DN_bvWZn_7l5jLRxNOxAo44qfpWZtK5h0mFIGa8axLN2i_ViykvnMt6GnybrrcsQJdFIDs7DNpV23XHOUzX8k7ZGql4zBi-umX55LsdPVWxmBCO0HT1VPxtVUkv5ruNDFlHRBGe7t61Bvmv9EJbTWxjMXjtalMc6WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=HgZJ74G4mQhrivTO94HL7noVcB3E87hdY91vCaexdTbBCXhE04WEyuU7SQAbsW1pI4qB7GtyLTQ4te6yY36BCDuZrNZyXk007HdzoOKR7lfHK_kQal7J1SAGTVcfM263gyiZ9Ns78i7_VY2HUr_P0DUyyVl0_yJRn9pNn_6DS5xIGB6deIO7DN_bvWZn_7l5jLRxNOxAo44qfpWZtK5h0mFIGa8axLN2i_ViykvnMt6GnybrrcsQJdFIDs7DNpV23XHOUzX8k7ZGql4zBi-umX55LsdPVWxmBCO0HT1VPxtVUkv5ruNDFlHRBGe7t61Bvmv9EJbTWxjMXjtalMc6WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQmn5mhROuzoETaXmKQkcczfubtgWY-yu8cAzZj6mtPfJpz-T-eG1F_7sYY-8rL52glsRubmDBnqZcOK0QOfxCM8bpvuL31f75xZWkEuMd7UTglS6jR2eT8idR3aSPkVJyv01YlalNhFbWJx-IcXs7c9KwJaop2T7gZqPDNz5t1XmdJZ_jLv2PavOyG0WKCkIh-QFq8G5koQft-l59l6sMi0hl_dLbq47G1Rh6PmUVKJISVxsgjK-KnzAsVQroQzMsEY7eJhFHiv3v22Au4CwFjIRdXofQY4MSrPN1m6YQLpbjXQbpmciK0uvn9hkRxRbnPKTanJ4iJl8enoojoGqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wb4R3wh4awpaqhCv4in6bTQaVH42jVDHhA8Ke2M0nklPgd2-iABgN651dj-pyvHAIys_9X9SCnHtJZgloj6SQ397TwnNq2u06cJ5GqMIAEZjsI8jg5vecP7THgXOIXmVNYJ_ifZDoeNShlsVyUe-Sy-Ghqs1ZxVwVXGOrHYBateDvlvI8maUfBRsu4Yo3NDHg8CkaHYMZYUUqW8itWKSoD8r8agW4XLZmT68_mYA1E3pQLrwguc0YO478hU0-2f4Artfk6J6skuBR6_ZCba6yKr2jaerWVpfdr6INnUqou61aMvufGnI4Ftcxd4DnPAX3Ce1FgmRh5rmIN56-udXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GopH57Qlx2IBQivRP1yOOQ_oGYMqh--7xP7ctuCtHe_2MlFf-mESaeLBDIsZ9jbDY17BmoQ9Q149CSXZsCLwMT4AUiEs7KK406K5Gn_HYXIOWK1zrJq1fLGgXSr1K3jQRv4x2LQuJ8FJ3EqAyE5tBOLgPsA9jrMYLeD_2RGki2Wf2GiFRCRFjbMsSYT-aT1woxMKA2Sqxkrkjz4uDgBbooJGNF8EVC8d1m3MgDEEBnxgYaG_Jx7JjyVCALPKgRpt_HllnVEhujwwy5oNQVelbEpof6mDaTvGeeXzNabtkhgIj6r4fGlsEOkmpRNtKMdkNucWl0f4OCIAWWkd7eCxqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
