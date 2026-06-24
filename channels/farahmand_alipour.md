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
<img src="https://cdn4.telesco.pe/file/UGrTOBhuWzgOww0wXNEREE5BjVRiLPYFKvrvgDLUziz46mHJSGeuuPqkaGPQ_oKyab-gueii-mR-MpVg9nudsQyMrhY2ccggKL1HVOUmt6we3D6ZKsym2BO4B-Oa8FBcTHNLxNM3vU-YX9r77PYHLJ_RUwd3x4Ee8o6rjJISRJay-zYpBjOfUkF8nJrti_78iHuSH3y6zaGf1xy6kfTYRhqrgcayfChYNJlCt2PgooL6PMl2yyxC0Ks-6SL4WZvPe8X1vMii7IB8FdBAbjiuJrXkgTCoN3YyeAfHvqiCwI1Yc-FFi9zgR2Pcvn7Q-uaunI5pVhWoa0xXVAvqxJZu_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 13:27:32</div>
<hr>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBLBI_814qgol_DQ-CIl1yYSfSaQxp2B1Wh4_IPFEmFgWj5VT2ZvlYgB9pb-ulo1GouS5z2tOfgb9OfNsrEo72Uz-5QdMHBy24nQbSTQMWih68uQAlNetn9-OoPgStEbfTHFcNbAxwHyQjDhm_c7q00qEh2N23igLiJzk6T1eJ8ppq2b6sqSJyXgaMIG4_CQWnN_Up9o5Or7YKfnf0QzqRt-lTdMKVWG162UQws8oCy_JDAK6ndbTkLL6z_PnTkX45uNns93HqbTJtqcf1XxoQj5cfl5zLfRBkViNdqFWpaxr4lMiagnhqhX5G0GklWkwuhTKnUbRg0f396JybuvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_V24fwnlSEn8pBtox3mpxpxImaYlFd8e44Kta2sIesLQWwRF7pDZ-lW_UHBH-F9OuUJXOBB1FfbiCJ1RibqaJ-snqF452VaujAF8rVwShBgO3Pk6yq55d_s2H5xZqJ1BmADKlUdgg7wCMYaL8kKomfWkB4F4aY63FA4JZmD_ZrXB_3XfVCVWmlGHdiiwsZmmIxrZdOLcLTU6DWWVfKm6fl0IAFlw74qL4ai0_-dPjszTWYa0THkpBJL_fHzGRBcshnkDDHwcT6yhQb-_h4SsAVMeeYzTPhMhtUFGHL-48vTp_vJzh-paPiVuic2vTSu7ImpBdUH03OUVD0BtmS7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmdjgjWxEQuckLdTv8N3YkIHT3mZ55uTCEXVEUmtjcfR3S65A0FeSghZc-Ylw45bbMoUqmy-q9SR91SOM5Ov5-vW049M9Lj7UBlVvKcH0KXXOZ3DraVoVEjjyCvNdx9F_UCmfjVONHnp1xhDmMBEyQvqL1y4VOCgA8zJyqel-NHIzFL2J2AAHcp57cvhoh6JOWAuIytaYpljmJUqWRJaDdPo0GfC3_JrIfeASDwpXycpqetSMCnQzC5f32nsLm0PZgj0YuIRJUEKMTn2pcinS_jnXxJxPBFJBs0hLFapJvQqs4iKiKJarxVXzDTCU3nV_LkymwNc6qxHFz3hrnn2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=QaS_ZJN2tWAeOBCj6avsuO-47reSTC883ZAPruBJYv0pa6VatWIk8ynqO7mxVtKSsxnlIHHG1bZBCguObqAym7isX6vxgPamCHy7d4L9CADmtEF30grBPB2goXDpvxrHPJbhFfE8RS1jG92rHiw-K844PZR8TdmoTuNnI3gfxYYVZSlazWA6h8NzvxDS5kldLaYPLEOkK-hM8s48ihU13YwECzUAyZ1j2DN7Oy3EV0Da_9kgk4m1Q3eZQBvV0q4mW7gcdpIZTxmkl1_qSXWk7sJlWzDV1h19AU_hleTHb8rFm8zqY14wjhRTi-MuUcgy3Wa7CG4i4sl_Fd5zAR-OMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=QaS_ZJN2tWAeOBCj6avsuO-47reSTC883ZAPruBJYv0pa6VatWIk8ynqO7mxVtKSsxnlIHHG1bZBCguObqAym7isX6vxgPamCHy7d4L9CADmtEF30grBPB2goXDpvxrHPJbhFfE8RS1jG92rHiw-K844PZR8TdmoTuNnI3gfxYYVZSlazWA6h8NzvxDS5kldLaYPLEOkK-hM8s48ihU13YwECzUAyZ1j2DN7Oy3EV0Da_9kgk4m1Q3eZQBvV0q4mW7gcdpIZTxmkl1_qSXWk7sJlWzDV1h19AU_hleTHb8rFm8zqY14wjhRTi-MuUcgy3Wa7CG4i4sl_Fd5zAR-OMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNzC_EHdaJpPMhkbbDDzh3HcJR8r3Ue0SpkoS7_EvI8qJHoutX7yYxxrdVoz_278HGKLKh3JMer7dt8w6AYVrFLSE_kdBOhp-pXjxdqLxWaF3gCHNResanUTzKGP7JP3XTMzk0kombnH16nL9LH_MBKWKTP0xKCvBmUrtPSNWSv_w-hUALDeQmkktBM-zizbQSES-IDEu35zsvCgOEc2Q6njW5qkPyZ_dqMYU6ZHeVsxSsCrVqL1Rt8jgPNd_iBVe2lF7a_Kax_w6bSt8vSvGT4OvEeF5iC2Gztb7rpsIcol3hDOL35oO3vw_w6GJ5RxQsMzG0vEsk24KaBgCbNfhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALBZn9xG00ukVt-Zwp-SzpyrLM5t6WksgFugTcqmyzQXHQ9-1r-WjXLXhV3V9fcnRnYjLHY2RT7l4gW3SRTePhzDz9XudcS9L4csiBN3D6taPQvYXpTcYXVHh-f_hyzWunEDkBwIX7ZoQ9ooSFnueERu0Eu9-foE7oZ2_PvNGB43MavM80WV8GoBDqfWNK0ljZSrwF8K1kD0USDwVKH8pSMLnAjN-WNEwj3alHWfbf09-3kqYbfE-JpAu8JsDA_YC_j-Z4F8Fs5eszZkoO8HIuLMnF2tqgCN3R_J93U-YuOUuSCbyKUECz3u5CIN7g10jBP9OUE_ymbTPgnb9ZxaWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZeYh9RPtt8JT0oV05Krm6lQKse0sDn_VbsiLgusg5UJq7DLfgfvaO5DDXBQlVhPXjlMKV1zwjh8f9sqoKU28GzsB43QIYDpxpTJ0e0g-KrtHHhGS4692cNY6hU0e4x2iwC2T8MP9Bc8nb4mtxanQfjCtlht9UuMqRv_ynJipik5D4GgMNpaoQP_Ctq3ZFL4DpjdQJXZKYEfWK81xvCSye8Fer2WIZME9s9zGIwVPkT0Y0zjQFfxA5IloeqiV33Wi0Crvmt31e3H3ROTSHrl8HBryESJBwAU6jJfnYAAmNkR0jIQUB4C3TzKXOW-UabBhSWAIMjUBi-s25V_fnufYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=huWxXYw9OPFUt6Id_4Ov3XoJAn4h282ddcXKjwp88aERGY1irvZiwKUNo8AeVnBJpUJaZs6xWH_V-1BPINez7UoVWXW5Uqjt3JtDSkVFhuBtrOgsuhHgGox-ckczAzYNC0h5cSUckIsx65jLzf7xauFUQGpESL0vuUo5hRM--OUaJyQWz_2-kBu_q0taWTXJ0-hb39cDuWnt9K_i0BCZr7WWS0rUmLo2XPOoWnL1IvdosQJEFamMKPuWQl_hlbBpW2v4Bv--W_n6YUWziE7HTKeSw3_mhH5AAWaxnu4JgQyg2X8xcsN2AUQUO1hW-O-XxhLJg6McVp6Ix3ORchE_ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=huWxXYw9OPFUt6Id_4Ov3XoJAn4h282ddcXKjwp88aERGY1irvZiwKUNo8AeVnBJpUJaZs6xWH_V-1BPINez7UoVWXW5Uqjt3JtDSkVFhuBtrOgsuhHgGox-ckczAzYNC0h5cSUckIsx65jLzf7xauFUQGpESL0vuUo5hRM--OUaJyQWz_2-kBu_q0taWTXJ0-hb39cDuWnt9K_i0BCZr7WWS0rUmLo2XPOoWnL1IvdosQJEFamMKPuWQl_hlbBpW2v4Bv--W_n6YUWziE7HTKeSw3_mhH5AAWaxnu4JgQyg2X8xcsN2AUQUO1hW-O-XxhLJg6McVp6Ix3ORchE_ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwwhQ_ldICT3cRxJOC9cnEmlZb48JEnIKoph0JojT3KgH-O8p28FTG36Cvr07UgOAhgc9_mFZHzr4ei0ZyZGrhY9cQHi_7RMxCp5g3omnn5u4oFU3FLJCe7vYMtNB73PS3tcuT8RIk772Ow3mPhqKPnNnFifO3HiTw7uauOX_XKGFuI1IG7InrMtof-xF2z_cdpoFbvRKxx16w4nNVLU1B7Vh2kmaJTbqs7p1PFrDC6yxyeYt0kZZFevLf-eokatdnmAE-4qY-IH68ha26oHawX3LVsRHeXX8UlrWFeNnqoExJaiy2C5AWA4OsXMQfpniReeBSU_PDFLKZFT4L-lLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D71b2g-Mmg_20JznBr00iuFB7HEIrYD6ptNYdD7agMY8U97fYWnggDyLvC-fIcjLijj3mBuTVbawrapNx-WgXZVepYSNsKGULYo-6iPP2HgR9MCWD-5o_40WzyHq8mLdnWl-WLqCQx8b5_3g6-49zM-_FXOWPIE89DXJXlFEon9ffZwnLbZPXBUAJuBkGZQAdN_mDVIBRfM8Ah01UgfFXOLLmL-6g5GURIaTry22-l7IHWv9q1MysDDPLbNAX4ZrVpjLt8ywI0y8cFz2mtZfeq2WXLe6qxMGEpJYC1_VQK9ycWRUfNRw04GDYOHsfLkt2ETBU28vOu-ehjJysGZ0Jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ysl3TByPvkmflnNr_-TXUZcGRua6BcBlxLNJK3eCL7XvKI2f6yO24ErMiyxLt09eJ3MlC6N0J2dNLHURYTQF19-wRhQs9ycfXJ_wUq_lwu8p6qDYAJLVJj0fiDNVnmpVvKqcOYycT2JqqdFdpo4Em4m7ovXqSTOTy8CGFpEt890G4XpI3bseIMmVNl368lFv246SX6oR5KT-h9tR19XLSz6go-AQx5dxOkmUjCxPXKKw1ZRXlTvRU9muyD_bq-sXfFkbyGtmYYBqXEUiTKhhDAjx2HzdZ9T0uSZFG6xk5_Gb9ppy5ynABEGxI9WtSVEFjmt9WXgL8LKEnf-gMwF7GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQ2FBWf4gdxola2mF60uMGVwpmFK4SLiTZRo30xQi0BylLOfb6nuG1ZJ2KOL5SV8NyYlRbX1E3XQH9Tycvr_7vAVQ8ksI-TnfemMoXb8QZ72iL9sms1w2kZym0R-F-XvcqBpNKE1J9y7DsgSXSRVfRXb4iMpgDqI0-vmx23MoJG6w3nB5FiFcMjTuH7gq7tVO81V0Yr8eDNPwVTz0b-SdG46zOLzTsKAXI6hOTd51j3qX1ekwI8PDR_jeo6ugjMvxKZ7Eha1tZ79GpnbkQW8tHwI71W9GTrntwQ2MFOZG4QoLOG6Bj4SowypLVBIEB_NpmMLL3jDoeW0Jb90sm3L-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USS4UPNQeilg2Hl5liLybK2hQxC1WLYmmRvJVdCT000zSjyQ2lBdaHZrbgF54MRmL695CTRKVBnzc6u6Ljo69WiUaUuN_J04hE7coxaD3AZKFmlGCMWx2Eb54Bw9xXPsxJLjwFkfNGRr0SVLF6eMPYhk_QewaFEishVrIW2X-fQPjTdRk717BbpQIs42HsncxtQTCGbl7-Pz7kEq3yWwm_1yHzTUuZlsLhk9tUkDOcy0zZXGN8UUA73vGcRjRpc0sgPrB-rQoAU5a-nalOis1r-yRToWHeutLqZQt4tDg7_G0w29zbJTqb6UtC8pBbSlrPkfsaeXvXhSUS1GXnkKig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfAUn3QPj-QatK9dKYu6Flftc4Yn-9c5rHsNb2mJIkaZaX7NgCPeS9GZYB8-d3JMblc0HX3zMEIVKuewwCMO-WuV0SqOJYeOncvQYNzoAH3evRX-QQO4hvlx4nQeTX_n9cSzzuls5JZbvWjupp3JM16p-IQV23MNQzG7utTvYK0G02ORuRrIIYblL3763b-wvv8cGFqw6sK8l90gcd9iTBqi6N8eOmkBH7zbuI1LARVRJj7m1UldxkGQyRRm_U4CUWPmIzoYeuoyOEVeK4IWOYIFfKm168Hwf00N2oRIn-DnMu6sr8GaVx3r6vGdI0KOcL4Elh7oXt_jy8GwWUMEWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pjd4Lq9ojD2X9Olb3f3O9Z9M3NmSVs-5kEpZOe-8y9TQ-J_2qmUdSw1rCU18otlZnfIuGgE9GRWBXgMZN0CQUxd9z88_yh7TGumYXifAFwP7cS3f7-CLfORp5kSsW2uyGduAmtLnsEIzJgTpy3hI-lv80ke-WCi50_TzHaF4Tg4qD_C4Ss8DtF-29s4Sca_OD0kB4Kwgqp-JSS-Pp9_XvL7ETq30vqJOveCdnW50DjOp70TWT1ABi-VoFQRGe2cPmy6v-jkJGYhkfxIwO2G7rw-_UBnt_ad1sz5S-H60c2BWefDEaJ_bNmtULw3ZksEbEzKUofYrp9dG3rnHoVOBXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZLUfbZj_ShhQDmMopSZY5CCGOE-UG7B5Bpm6REzL6Dw-pT7OMisUSd0tBERc9VBhG9Fub3D9_ldhL-RWipLo3DIuCwC8qJLzEc2Tt7SGJpG7k-M7UlV8s4wembtUcQ-6uolSDf3hYIHwhiKs8ejsKoZVlYEmBfDEhYIBkUEol27l264Jlp5WA8gPdAkIogBldQIDyWzxBKKb2x571QDMbPVXBlHeo91ovEB7JyzkfHvm0h0MHFCglG5_edIQmAkdpKS2S_iMPVVXl0RFwLW-bhkQn6eXU7Txi2wFZlCk2MCtJscMlumVsDMuFZ7y1aTkogak6swfjUybz8zGKuRlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U90H6_j0kTQJnT8ZF2ZjmG71xxtLDVEua6ppd2ecMH81F7Ls2R8rAPKg4cK3as1iK7z8-RJ3VcEycxt6b2y49_-1Zp5MZnUdXEeXq8Eq_42vO9v1mtxGnI1UHZ6sg8G35LzBgX_4b0WwUgjmxHTts_pTcy0d_z9cxc6Ne2ME9KLRZp3mbsJciKiJJ8FFj6jaangM0dtFDOmNrZ1Z38qY7buz3IsYV_841u8ALZf4pRC6D3Ka9ueY5WGa6bhZYwN2aLfaNuPYglsRXzA78FCX4g-sgwkhTPwxbal5QkUQFZ2QUvc2KK8AX34D1lOjk7V5b9B9k4V8JsZpamdI8Cd9pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=mPNN0oDkVKfvVyWAp9_W4oglGgCwocuyeNjtBdDu6HU-bCW9HkhxAgBZGsq6Dt1kqk9ljBN9wnyAAmDpFeoBRd_6uKPfig1JIK0xwN2xIT42tyNOK-YpSmWkXil_8003v7ZzbrQ2mGYu6WHX5gdh_-KNtTpkwv4M4IJVI_u4SLd7-AS_v5wmzEI94rGEGlg-epMbsSOvIBwHmpjtYoCobAmRcND0W-Iig54MND2QR7cjcjjd5c6wUSSjzJORoMvQVOl_lR5Y0OSdzs_pdz_PnK5pAqz12_pnPMxOMx_LSr71DoIfGFgOBzGRSPW2qA0uOV9YdzAVr5h0cdufXmsZ9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=mPNN0oDkVKfvVyWAp9_W4oglGgCwocuyeNjtBdDu6HU-bCW9HkhxAgBZGsq6Dt1kqk9ljBN9wnyAAmDpFeoBRd_6uKPfig1JIK0xwN2xIT42tyNOK-YpSmWkXil_8003v7ZzbrQ2mGYu6WHX5gdh_-KNtTpkwv4M4IJVI_u4SLd7-AS_v5wmzEI94rGEGlg-epMbsSOvIBwHmpjtYoCobAmRcND0W-Iig54MND2QR7cjcjjd5c6wUSSjzJORoMvQVOl_lR5Y0OSdzs_pdz_PnK5pAqz12_pnPMxOMx_LSr71DoIfGFgOBzGRSPW2qA0uOV9YdzAVr5h0cdufXmsZ9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCZdFT4Octy9r5JGGNNpbj_VEpDEbhhG7J6lR8kIs1OYOOS8VbvU3KoCXwl6PF6iPyWVV3ihqA_Mlk7PeXtb9gi1D5z7SoarIX_GhIF2l_pAxckohyUvbiu-6NaHnkjxsK40b8ElBwg4bCP_obEV0aIj_DpAnypLYe_KeDHDQbnxffkToNa3VKRjhzrIAcD29RNUROYbKwzq5n5LJ1GRk6onIX6dRZKF4msWbWEgpSuHC6zG7sUoSg8qUcY6EGpjERn03IC7RnQG9KK8Oi5t8kd3Fg6tdSZ0qvmxnWP_XUw8pS62niNvGq8j5Vn8gxHHI4GN-EBj357mWBaHakbzhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=lGoNUCd38dsfKsenCvjjyZwSls7JU6tKFFxH1j-D7WeT_ftXh0xT8GKi1EA4aNqewELpsiaP9jDzZZYJGf4JcKTWxGoKK2ENdyMVDnIVji4gOMuubgRwq0cM0_NQsbz9sypn32aZoOHkw1jZKJhuNXCD8P5F7JwE_gGwWdLfWE62zaKUKAGzyXcEQaB-s7xKvOYOi6hJAPbD0tY_Ce0iXwZA_w0VTvY5cXnfnzFGVAayLyiB-RVuLEdkL9slEkeU3abvL8OIU9WndwVPKkGC8UnYLAIP8tDNuLY30JNk_8_0BP8oapEF2PdnFfTdc-ye-xk2zpc7xhH6n8rgYinNDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=lGoNUCd38dsfKsenCvjjyZwSls7JU6tKFFxH1j-D7WeT_ftXh0xT8GKi1EA4aNqewELpsiaP9jDzZZYJGf4JcKTWxGoKK2ENdyMVDnIVji4gOMuubgRwq0cM0_NQsbz9sypn32aZoOHkw1jZKJhuNXCD8P5F7JwE_gGwWdLfWE62zaKUKAGzyXcEQaB-s7xKvOYOi6hJAPbD0tY_Ce0iXwZA_w0VTvY5cXnfnzFGVAayLyiB-RVuLEdkL9slEkeU3abvL8OIU9WndwVPKkGC8UnYLAIP8tDNuLY30JNk_8_0BP8oapEF2PdnFfTdc-ye-xk2zpc7xhH6n8rgYinNDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=c_ZEuyg4hEznYs-eydslmo4oHh_6cJwUxlQcBT7PouTZZvHOJTlGn4ES5N-D22WBl8iiOlmX8UUUFN-apSrw9i8NXtamO9oJYrejKKw_nebZhugSKCUUJ3-UXWFlPehhODczgAKpyEOH8V7BzcTPMTq9VH7RIEaOjPtWt6eBVQSnS0S1JvsJq-c6bnq35kIp9nI_WQDms002km8CysQ-GQU4M_Q9xocnQqmG-CAhGFia4x_WoRpWsQIsjZm3PghttBl3Rn082prUPUv167YEwx9badQAYepBTGMoXA8Dp6vXqVRGqXbgt1PQG_cR0gLFAX9zN4IVOlXop25KiSBqGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=c_ZEuyg4hEznYs-eydslmo4oHh_6cJwUxlQcBT7PouTZZvHOJTlGn4ES5N-D22WBl8iiOlmX8UUUFN-apSrw9i8NXtamO9oJYrejKKw_nebZhugSKCUUJ3-UXWFlPehhODczgAKpyEOH8V7BzcTPMTq9VH7RIEaOjPtWt6eBVQSnS0S1JvsJq-c6bnq35kIp9nI_WQDms002km8CysQ-GQU4M_Q9xocnQqmG-CAhGFia4x_WoRpWsQIsjZm3PghttBl3Rn082prUPUv167YEwx9badQAYepBTGMoXA8Dp6vXqVRGqXbgt1PQG_cR0gLFAX9zN4IVOlXop25KiSBqGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzhvUKFtGcHgiOxxoXb9ayvu0-MT5tUMZnsgC-ypxtaz_1Br1kDmdkvIsEMUd8x90YhJzB2loRTsS4NOlmZ9QvecaANqrCXKrpAU_5lPKbuuVSDjK1ripD-rq7ASio_Q84FbtmgjNCEsnWOHGaSAX1Cxqoy9GgMEzDP3suawTn1A0QYun7n9k8TT0AIASGefrCPny21E89EcxFUODSrHQU7Jgfh64kLBzBemZ7WdokWpEmvodWa9pHEuVqVuGWwIH5LTJdB93Qc_vD5cUe4OscBG5eDr5BJYsuqUTAbb3Fmzn_Jy-XVvEiko9UMx7TFzRSlah-qqMd7YLojEWM_9rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=aaY5gqzBQ17i4SlTqrjTToOR7LuilDPc6Z7UIXeH1Rsm2Aw-AnKikpyvvHJxsBigbLTnX5-tGIpxynT5lvY5T3984Nse_q85OcF8nedL3jXwkLbNE3PWnPtZD3wM-sSqLfA5m1Fh1kmZqXfomjIpFm8h69ubXJA0pvF1pAG3xMTAkgwx7r6DzBtpZqgdn0-kAkvp3oAp56LeL9aRJ3bspXqalEtj54I4G6VpVUzaQe_P2V6mbqdCUdX-CvrF-AmZUPteQSMujT_X3qAI4zDrq_mY2hLv5QnlA5gM_MPwvVLxQRMvbbH8hlII8gOSY4Ad5CbsoZu7_JUFHUqhVFU3mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=aaY5gqzBQ17i4SlTqrjTToOR7LuilDPc6Z7UIXeH1Rsm2Aw-AnKikpyvvHJxsBigbLTnX5-tGIpxynT5lvY5T3984Nse_q85OcF8nedL3jXwkLbNE3PWnPtZD3wM-sSqLfA5m1Fh1kmZqXfomjIpFm8h69ubXJA0pvF1pAG3xMTAkgwx7r6DzBtpZqgdn0-kAkvp3oAp56LeL9aRJ3bspXqalEtj54I4G6VpVUzaQe_P2V6mbqdCUdX-CvrF-AmZUPteQSMujT_X3qAI4zDrq_mY2hLv5QnlA5gM_MPwvVLxQRMvbbH8hlII8gOSY4Ad5CbsoZu7_JUFHUqhVFU3mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvSDsfyME6cneZfHrd8TBPPgbstymxsr0CeYs8-7ol7ocAqqp1WxGbh6PAMGCuGbhOXqpeP6ry7dn3ck2sgFjQ5PXGB8zMvHsoPFMlhJYoNSdUNQbgTC153UpytxzuVddy08A_PMeN_RV1nD1jDQMoXXSdpE35D0xTNF5oHt9Gg7ExqNP5pFduvSWB8WkXd2fOp1eh3zPITNA9pKPkmBPBa8W_JTohqp_AhxzxAUqK2kS72DAcZkDAL3A-OpBjUHg-bveIb74O70wmkxNoNSRGvjFT-52-TPiSvuWYWevOmVN_fT01FQYNYcvY9vpzm0xWPLKbRpG_9fHK2AF_j85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDYPgFY1PB3Xh0jwOTfRUPihULDRFCiTDo2h6CLQtUilRunSBWjX0PrJIKsvUOMjG7hfR6uLCAG9HhkqtB86U_pzg5t_vaL9vUT5Q61ppgp5JIo3aqKYkuZAaqhhBTvW8o8ozmtIrRG4pqQMbIkpRWPIsgjxyaWKiZIviLo8lt0SgNBfeZp8TPI2iVnGfByub_XUKebk0AxeNmpT_dBPtOwDDHQCGcGjUYqAQO2T7zmTVcv7MgQgnzQ1XsyaF6YFXOmfSjjnZnIqwx47ofJviJAoYi1aO7YRcSf2BNkjnXjyVOz764bZp4V-XqVfTpDvXqUz_xz2yZ90_NHfTva27A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MK9dOCsy0egGT6aLk5baw6XU9D_Vx61nBfkJYyF1AQTTODkjyp9xTud2zZEvVfAWJdcgfralY7miEPwyWS8l8CH-V0Rb7_Tm0pN1YQ9zSSxFeCRqJmtjsMgAHYLccqmmGEjWLK-dh5D57Hf8xDcV127ipIyiA4kljM6ttKtl5t-WEM9piqqlT3uClAuiRrDQcFIv913J6qg3z-5ea813FxC74E79725ksGQG9dZjQSxB_vEsCfa4Bd-YsmbQUTyW_aGujnmSCD9QQtx4nuIMKFHkzR3lAoraJvoqLQYobN1JYLrlQWpZ926JTp9f-DvxvZSs-OWWD8cwyUGEs8y1jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWh2tlG8c_fFtmCbrwyilgE4mM00xP6q-jyjGHUGovyeE4ZmUN3ABrIqU52WnxNWz0Q9KDtz7sS_zmu54ajOpYKZNJYGGsEiJHwppBjWHg0J_mf9zvBfd3uPeJQHo7Dlk7DriBJQyqtN1qv-HD9u4JWm2xl4AVpbES5v4Mk1NHwYQmFZsgHtRdPohkPG4Fq3ZeKkhjpubRMiMTSudWBt73i7tsOJFfrAR4TpU164waBjmO1WgaXCb__Cut0ChJhBY264k_M5bSKN3dtZNKvFjdiFg6lqeXsdXnB6WwRPWE85epphbZzFL8Ajham8bmTiNG-LYayKlOPQxKoP8dlySg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=vrv5Mf3wAd9hY27Zf0mAXgQzkqp8E3LBmM3F2MsoZEjeLeeHB3rVHVrHpOWYpXrzUyBtvyHJPxuGtntq5m3_W43Gs2IAOMMB8B1nXpSbk0h_w8l0KFfFBRjHmSUeYyqwNcP1axh7tOVGzOYWcJqaYZOjNnA-0maarchOy8nlccyTjCp8u81SuVQAKKAqGivNJ3LPE7zg1C4Hvd99Yeyn2tVAw7WZroROD55NV3P742h4-YvQ3rKrNAlzSTbyhM1qKsjQI16mXZx41rzTU92kGps4A0wjb4svg7MnliroDVfKCSEWl_EfONc7v-_ZbdQZ6lok-Tx-Ylw08oMiCJTVnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=vrv5Mf3wAd9hY27Zf0mAXgQzkqp8E3LBmM3F2MsoZEjeLeeHB3rVHVrHpOWYpXrzUyBtvyHJPxuGtntq5m3_W43Gs2IAOMMB8B1nXpSbk0h_w8l0KFfFBRjHmSUeYyqwNcP1axh7tOVGzOYWcJqaYZOjNnA-0maarchOy8nlccyTjCp8u81SuVQAKKAqGivNJ3LPE7zg1C4Hvd99Yeyn2tVAw7WZroROD55NV3P742h4-YvQ3rKrNAlzSTbyhM1qKsjQI16mXZx41rzTU92kGps4A0wjb4svg7MnliroDVfKCSEWl_EfONc7v-_ZbdQZ6lok-Tx-Ylw08oMiCJTVnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=P4BrgGQ3IAspx2AWaNKQGGaQpuezQ95-InuOpiWfk-k7TdOX-J1jpuYKEgHq1RufKrupgrlzq0ovdG0HHm6qCrMLW8ZL_SeVRzDbZDMjZdY7kRRkmWfwr02BJux8aG9pGNluGNLN36LPAhViawPguYrkyJTRW6atNpNQzWLOcYZ_3MvF7frTgC5vmTB9Wknfur-Jx64A5_0MDBcY3SvVOf4Ld59cBFLosk7hDbcNb0kFWJVXj2UBnsUWw4hbO2P-iqm4rmgznPt2s20Kd1KD2NpTsAnYbtAffC_SF0Gnid5gmNq7p9DpZyl3Xp-430Sw-bF9EqEfPJkuURlzS1D2SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=P4BrgGQ3IAspx2AWaNKQGGaQpuezQ95-InuOpiWfk-k7TdOX-J1jpuYKEgHq1RufKrupgrlzq0ovdG0HHm6qCrMLW8ZL_SeVRzDbZDMjZdY7kRRkmWfwr02BJux8aG9pGNluGNLN36LPAhViawPguYrkyJTRW6atNpNQzWLOcYZ_3MvF7frTgC5vmTB9Wknfur-Jx64A5_0MDBcY3SvVOf4Ld59cBFLosk7hDbcNb0kFWJVXj2UBnsUWw4hbO2P-iqm4rmgznPt2s20Kd1KD2NpTsAnYbtAffC_SF0Gnid5gmNq7p9DpZyl3Xp-430Sw-bF9EqEfPJkuURlzS1D2SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=INWee8efXxlVdrOazoUNMwFMOPf2OBjKwfcdWOsx0-opr9e-fWM2oFM5aVzF7Bxbaur8HHtrKXzs7UKJj-ar8LPF-3oU8KVCLkMQo_K6lNePTxI8AAQvbc82CePB8qTKvgKDwxOOskxhXgU7qMjAVAoB2oiTKkH8R2kB4HguEJUHlE1DdPUfwr7VMmhnHNjtLCFBduHbHJXVyO4cYicWuNzdRhulriItq-UAbNtfT_0m-h2JQLicdILzOPZNaCqziWeNBTJmAm153YulvhJqR-RG5sHl9Pfi-5L23cDVbyZnvZSJpli79KyFXuewXPAhPrNHJW_bddDtXLwh8RSbMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=INWee8efXxlVdrOazoUNMwFMOPf2OBjKwfcdWOsx0-opr9e-fWM2oFM5aVzF7Bxbaur8HHtrKXzs7UKJj-ar8LPF-3oU8KVCLkMQo_K6lNePTxI8AAQvbc82CePB8qTKvgKDwxOOskxhXgU7qMjAVAoB2oiTKkH8R2kB4HguEJUHlE1DdPUfwr7VMmhnHNjtLCFBduHbHJXVyO4cYicWuNzdRhulriItq-UAbNtfT_0m-h2JQLicdILzOPZNaCqziWeNBTJmAm153YulvhJqR-RG5sHl9Pfi-5L23cDVbyZnvZSJpli79KyFXuewXPAhPrNHJW_bddDtXLwh8RSbMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=n4DuY-cH-x_QjbchyWOZRtwuKYRZGPcdMSzGGUY-knctUNAL7Wjk0oTFEX91IWVm9bXjvRXBYnclHiQddp7RXF8nGXwm2Qff4wWOGLjf6bvUUeMymK4h-lBRyq_aGEGHVYq8tyMC84xPnwD1FwJyYAjw_eY0yTxidDYpL_IoZ-lNGlzyR35LHgEA5VATGfmfFk4J2Uxr0qZsEEjue3DbXVAYL3HeGykjfWPipGcHkL-fh8mFfXpPux3c9sfWV0EYQS0pIn7A18AQk6OYCUAP-cHeGUhIPtgDFTa_cpMmivV7buc7lujvaUWm0kozYsxgSJDKPoGR4QrbTB0FgTA-6qnkMbZXVN5cYUqmNNpMJwavtC1sTVhbV66Zjg0vJGrxQPWM3r8YQJmmqZhYHP7pWt5-2jAE6Y24oLIH0JNCUgC6oiVri0Mp-8RSf1Jf9Wv9wTJUqZk9XbLamcPO2BZaZ2Xs0kYWogRVSyTlAmAubcq1xguQKUBYF1hiNm1djIaz8bvJewl5VrJajn_oWtAyupurT_N7WN-Wm-qzWLmmfrO2950jv_qzruN-B4nBheiBWpg-jj10VWMc7Nga_FN8a_G9gnZftr42wFj1ng0hQ7eeE0Ex7ZtiUU-_wcWWyoFAi2rqhPFZ-QHZhs_fX5IWnG_Rvr8AMSO53gVMPgEmEIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=n4DuY-cH-x_QjbchyWOZRtwuKYRZGPcdMSzGGUY-knctUNAL7Wjk0oTFEX91IWVm9bXjvRXBYnclHiQddp7RXF8nGXwm2Qff4wWOGLjf6bvUUeMymK4h-lBRyq_aGEGHVYq8tyMC84xPnwD1FwJyYAjw_eY0yTxidDYpL_IoZ-lNGlzyR35LHgEA5VATGfmfFk4J2Uxr0qZsEEjue3DbXVAYL3HeGykjfWPipGcHkL-fh8mFfXpPux3c9sfWV0EYQS0pIn7A18AQk6OYCUAP-cHeGUhIPtgDFTa_cpMmivV7buc7lujvaUWm0kozYsxgSJDKPoGR4QrbTB0FgTA-6qnkMbZXVN5cYUqmNNpMJwavtC1sTVhbV66Zjg0vJGrxQPWM3r8YQJmmqZhYHP7pWt5-2jAE6Y24oLIH0JNCUgC6oiVri0Mp-8RSf1Jf9Wv9wTJUqZk9XbLamcPO2BZaZ2Xs0kYWogRVSyTlAmAubcq1xguQKUBYF1hiNm1djIaz8bvJewl5VrJajn_oWtAyupurT_N7WN-Wm-qzWLmmfrO2950jv_qzruN-B4nBheiBWpg-jj10VWMc7Nga_FN8a_G9gnZftr42wFj1ng0hQ7eeE0Ex7ZtiUU-_wcWWyoFAi2rqhPFZ-QHZhs_fX5IWnG_Rvr8AMSO53gVMPgEmEIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=nr5FWAxaxGwRrqpj9j3_YMI8_BzbctNveLUC__MdF6vV-GwwUW1sXNYd2rE9bWzacfbyStxzNRslcXXQLk6Lybx_mT6Elmuir7fIkyl7Qmb1DKLLKqErRZmtO2uzFMU8iGBkAfs3chHG_iTE0IUgPlQGf3RcBJZDZgX2qXIGXIOsch7gFw8Rb3SzSCHe0H47_qqkYTnc70tr-3yVkcoGk2bIcWv7bU6LlpqUo6KNdPlhraw-P8h6EcDizE51MZDklksLV5h327aWGB_pHfFNwFfwVIgHE9JUdn-Hsiy0hx1T3w4SyxnwJEbGM1HqH5zSneVlweNlyV75P5okiivYKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=nr5FWAxaxGwRrqpj9j3_YMI8_BzbctNveLUC__MdF6vV-GwwUW1sXNYd2rE9bWzacfbyStxzNRslcXXQLk6Lybx_mT6Elmuir7fIkyl7Qmb1DKLLKqErRZmtO2uzFMU8iGBkAfs3chHG_iTE0IUgPlQGf3RcBJZDZgX2qXIGXIOsch7gFw8Rb3SzSCHe0H47_qqkYTnc70tr-3yVkcoGk2bIcWv7bU6LlpqUo6KNdPlhraw-P8h6EcDizE51MZDklksLV5h327aWGB_pHfFNwFfwVIgHE9JUdn-Hsiy0hx1T3w4SyxnwJEbGM1HqH5zSneVlweNlyV75P5okiivYKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=BXvMnl6vCLON4CyUBX5SudPzKzLjrTFr1Dqwzy5z0YapmGMCbRmJ-LmibMnIx__CZ9gA8mG5lEbcdy0cGEIQAhtmc6fPJ_jVhEaaAWjnpFP-WXuH2JIyqrj7WtHqLDvAYMuhApX_hDNy9kpTQbZwBUY73z7FC6zNKHn9EMyHAMYR5t_7T5K1SrWhw72PWj3UgiIa3o2Wo5UK6tiBwyI8ul5J3Y2YXBJ3BUDgLbrPUVNED_n_bM0KrZGqu37KdO5nBowpXgxygT89pgKLf9GtN3LnHwCUtxaQOIcTQcGpGYL7VxzAW-EwsgenKAyaXDi3lPG0-7EZjlpHTqZSZkSvDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=BXvMnl6vCLON4CyUBX5SudPzKzLjrTFr1Dqwzy5z0YapmGMCbRmJ-LmibMnIx__CZ9gA8mG5lEbcdy0cGEIQAhtmc6fPJ_jVhEaaAWjnpFP-WXuH2JIyqrj7WtHqLDvAYMuhApX_hDNy9kpTQbZwBUY73z7FC6zNKHn9EMyHAMYR5t_7T5K1SrWhw72PWj3UgiIa3o2Wo5UK6tiBwyI8ul5J3Y2YXBJ3BUDgLbrPUVNED_n_bM0KrZGqu37KdO5nBowpXgxygT89pgKLf9GtN3LnHwCUtxaQOIcTQcGpGYL7VxzAW-EwsgenKAyaXDi3lPG0-7EZjlpHTqZSZkSvDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTAui6dx1bszN_0wfGWLCw7CyMh40bKnDNz6DLokJJ21WVIOhii38DXwGPDLaZcChg6TM8x38b7UMFwM3fajdXUfpWwIgG0-DZLz5BBFXR9urh4pPenqEIi0i7xETgPokXg2SLjYr12mmuUBzx_9hz_guSm4ABqK4GeVhZULJ08fhHBbnztvILxlrkbj91qCXgwPT8kbUfFY_-vPMAbMaCvih_UPuwVr7WZgZNwjxlIRUE2JYWtlkmzrPStHeLh3NUU1AzzByOvJD4XJOXwWcZ0ZwQ2pMZyrAcbmkr729iHswQyx414sRyMCx7R4nnTGg-UVKaCvzID9ISGU9h4VUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=PJSFAgh0rJ8k2lqelAP7lm-OEKTgm2gfmed4UNYI44c3b6_8pu2H82haPE7FujSaQD0ShpqhoPXJHgKRWAVc_DXdACFm68chDtxOZXYk25bOud3VM6Ht3k8IuASfBLTY-zEuFQRMNsFyTkxVB_b1jXZF6TX8PCNNs1I93K4ZAHiZUGTg_pGie8zfvr61n8MdiX0UM7tlBQWSdYQoihEoc3GOMLKJmTdma0IBjMU5E3z7AQHgSqMt5CsGcWOGx6wodDrXfyEGLeg1ELGdKz9yNNceygluUSeDIV7pJy1aZCFzyaGT2rwuO4rRQ7ZudYPt5giRImmr6_OdVGNOHFi1hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=PJSFAgh0rJ8k2lqelAP7lm-OEKTgm2gfmed4UNYI44c3b6_8pu2H82haPE7FujSaQD0ShpqhoPXJHgKRWAVc_DXdACFm68chDtxOZXYk25bOud3VM6Ht3k8IuASfBLTY-zEuFQRMNsFyTkxVB_b1jXZF6TX8PCNNs1I93K4ZAHiZUGTg_pGie8zfvr61n8MdiX0UM7tlBQWSdYQoihEoc3GOMLKJmTdma0IBjMU5E3z7AQHgSqMt5CsGcWOGx6wodDrXfyEGLeg1ELGdKz9yNNceygluUSeDIV7pJy1aZCFzyaGT2rwuO4rRQ7ZudYPt5giRImmr6_OdVGNOHFi1hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fp9DfZAblCnbrpgRpoVuv32zyfDLz6t9eW4YNqlII0DTeDOHRX2xfEjMIV5Ubj06qqtLKRngRX4z9N8Qq_ZnimIx65EqEliXGIXWYILamxa3MmEqT7j0a16aHZGsP66dSz74UCNNz8VETYFZmZYjDku1WkpEKYz9zfSesl4Vu5FgkSmGBKZ0AFIXATRLicJmRJSbGt9uRsbH4LW0lq7FETFrMJMIPmHZhMrqi3yuWNgb7HUzjc2O81YKa6Yn00KnXzAK1mdQkkgarxMS3CdCDG4xjZ9JYV_GNvJcnmiS_cPL5zqqWSrdrcGv7JXmlUciVXr2gnXxB9rEXvJZBJWNiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLELoX39czeF-QcVEMslyc-dz9BlkA898YRgtsPRX28Ey0vilDjY_-EKEqg9xXF0ISc8dzctWBCq3P9ipeVJhFfN6gW77UhMI9sgmItXadGIqNKO-n5QrUUpdwvvZdSuOE3zqCfWHdSnqAYlrzIA2DZYYLnu_PQPfwYmjq66StjEbyhVwQRf5NDgdkwD4c2rCENCVfZe8QYMsWGYrq7gTwD8G9lzKumXGQypz-UTVoKUGZqLImF5W3wFaIRCfuKHj2tjSQWSyjRErwjM0d03S6mJsbYhk_3Pp7lGT3Mdi_jFL4X9xlZeeYqjbZIzV3ZSbc8wVbS2MKSCTMU4u_Zc2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=Pt64AZrGM745Cz9NuY8Jrunzwl7jhBSyYO8HCKA23Npcs8deIPmmqOJDT5BEZ1wjpg5Ruz88DZS4rPlTF9Tg4vnsB5MjW8OXaF4xWHp2sf8Mgj6Pd5WnjjAYUL-QPSEDlICgJcrEiueQn_MwS4qUgcYwKPicyFcA1csMUKq7uYmnvwuIF4E0l_mVz1jih6CvqPLzDORkUHEn31_H9n8keSc1CWcWjbVYtFG8y9ubYu3tUPTP9MomvNIerpBsEL7uEtohiv0W4XT0IZebcH6tvBTnehZS-GG0Teokg8CixftkqbEBM28Q_6fjGjOvzsFXuWI6BDjyfCmdtzRTKxQpwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=Pt64AZrGM745Cz9NuY8Jrunzwl7jhBSyYO8HCKA23Npcs8deIPmmqOJDT5BEZ1wjpg5Ruz88DZS4rPlTF9Tg4vnsB5MjW8OXaF4xWHp2sf8Mgj6Pd5WnjjAYUL-QPSEDlICgJcrEiueQn_MwS4qUgcYwKPicyFcA1csMUKq7uYmnvwuIF4E0l_mVz1jih6CvqPLzDORkUHEn31_H9n8keSc1CWcWjbVYtFG8y9ubYu3tUPTP9MomvNIerpBsEL7uEtohiv0W4XT0IZebcH6tvBTnehZS-GG0Teokg8CixftkqbEBM28Q_6fjGjOvzsFXuWI6BDjyfCmdtzRTKxQpwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=ouk2dAXXq6UAqxzvD0dWvPqiDqPVUdHZNVSldCP5FPV7kdQca2gBFU_qRd0Vawnqg0rYmJIn0Bcew1XiwSxJywWYBFnV2s4ugExAPA3-RmUuwxgaQxgb3wlL0mDI2lkuLCkc_yWftQcioYj4-Awbb3O6E-YzcUXXqOan5G8WHdys4gPeV3DuQc83MNNdaxX1F-rK0hgi5HhxK7mbPm1f5ih-odjdaUwnLXKpRCrWfEazYXFvbC4hymxDWpRwosvFdpvNULQLZoFeHJG7XKnh8VpPCYfeVvXdG42nWLSZxgdYxdFMSrMkXPzWOzKspKTslw3TKBvzZ2j4A2v5rpCF1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=ouk2dAXXq6UAqxzvD0dWvPqiDqPVUdHZNVSldCP5FPV7kdQca2gBFU_qRd0Vawnqg0rYmJIn0Bcew1XiwSxJywWYBFnV2s4ugExAPA3-RmUuwxgaQxgb3wlL0mDI2lkuLCkc_yWftQcioYj4-Awbb3O6E-YzcUXXqOan5G8WHdys4gPeV3DuQc83MNNdaxX1F-rK0hgi5HhxK7mbPm1f5ih-odjdaUwnLXKpRCrWfEazYXFvbC4hymxDWpRwosvFdpvNULQLZoFeHJG7XKnh8VpPCYfeVvXdG42nWLSZxgdYxdFMSrMkXPzWOzKspKTslw3TKBvzZ2j4A2v5rpCF1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی، فرمانده کل قوا ۱۲۰ روزه قایم شده :))
خودش هم در جنگ ۱۲ روزه رفته بود «کمین» کرده بود برای دشمن!
که در جنگ ۴۰ روزه غافلگیرش کردن!
«ما اینجوری نیستیم!
خود ما پیشاپیش لباس رزم می‌پوشیم»!
مجتبی کجاست؟  :)</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=N9kOt1ZxJ-CdHewX_As2lfa88XaQdw0qSxBuB1Y_4in7pu6X0bVOUy2nG1MZ--i4bf2CLocj-1WE_HufEK9dWS6NyRTETvrsvwohkbiI5ONfKExMOsFAbUUczd6y767VScGnpmsZLWUOBs16wJvt6Tr5AvasVMkr1e6hgnWC20nJrZ1gyiH3zE0wB4DDqPetjaFykA5s4lkNu35ZVRfYaSz6EHX6C4pr1vPQx2r__tjtd1Xl7K6zKtUClyUeMxWalaWaOFhy1PguiW9MyfMoveAsdAFmrYSlYSDEYfnnPk8678nWpkDYWf1wUCJmDoA1ZXgMna7dslrC26CFJmnrkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=N9kOt1ZxJ-CdHewX_As2lfa88XaQdw0qSxBuB1Y_4in7pu6X0bVOUy2nG1MZ--i4bf2CLocj-1WE_HufEK9dWS6NyRTETvrsvwohkbiI5ONfKExMOsFAbUUczd6y767VScGnpmsZLWUOBs16wJvt6Tr5AvasVMkr1e6hgnWC20nJrZ1gyiH3zE0wB4DDqPetjaFykA5s4lkNu35ZVRfYaSz6EHX6C4pr1vPQx2r__tjtd1Xl7K6zKtUClyUeMxWalaWaOFhy1PguiW9MyfMoveAsdAFmrYSlYSDEYfnnPk8678nWpkDYWf1wUCJmDoA1ZXgMna7dslrC26CFJmnrkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mB9stVjKoMT4OhgmCgRw9SfiSSvKTEU6n3OmoV7HdLl0--wpBYYh98_k8GGRpQZU2LIjbdettyBM59Xa_Ua1myXdHPrenSCTRMF86JGt-n-QvRc4O_wrgIIqYo4qeZrGkcQ_EkA-qKy19Xu4ZtVDpKqUxdtTrauaHQ2reV3Kq3A5aq0UzVclAChc6u8m1y9FzEM-nh8Ps9JJb1UHXogAArSxfe3-C0OVnmcU3YXtDDBtsUkOmnEBigoPFIG_W5WyJWTc_ORQMj8ESfecu92YVaeHynUtOUmmOp9si_W9ROEOvTW3gLbuAskSCgAow6t-JRPL4IbgVRz1aBI_1E9oag.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=GyAGeEguSGf8lFnP5LJH_1q9tEtdyY5XRHxOG3epQQ3Y9_6U6wSOvWI1S_ETjqhQgju5V9-0_xdHgxS1ZApXwtUvqhjg1cfrdY0ZujF3vhpgQ63AbfNCWKyiu0X0k-ChUdjeDDus_WqN8c5TpcAlyCULz8lSKEvfYKCe-iym3EYMw5DWEranj0utNiqB9Us_FWvWkM62Q9r28_vtJieB9vLNHfcIE_SPV-IGfC8Mc8P6Ka1RV6Yh7dK2ONndgZA9rB_rHzO_zx5pon1Lg2JuBMp1ByVOHz4VYhQOuOKM5UebitHHxcPnXACUmuHiog0TBBDJ1whGb6c-nQyU118uQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=GyAGeEguSGf8lFnP5LJH_1q9tEtdyY5XRHxOG3epQQ3Y9_6U6wSOvWI1S_ETjqhQgju5V9-0_xdHgxS1ZApXwtUvqhjg1cfrdY0ZujF3vhpgQ63AbfNCWKyiu0X0k-ChUdjeDDus_WqN8c5TpcAlyCULz8lSKEvfYKCe-iym3EYMw5DWEranj0utNiqB9Us_FWvWkM62Q9r28_vtJieB9vLNHfcIE_SPV-IGfC8Mc8P6Ka1RV6Yh7dK2ONndgZA9rB_rHzO_zx5pon1Lg2JuBMp1ByVOHz4VYhQOuOKM5UebitHHxcPnXACUmuHiog0TBBDJ1whGb6c-nQyU118uQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=MkhhQY9J_jD9GWSWhmqzzuUyU3u4EWQM_aY8CWTFFOjBU8qi2f5efYWXlSqhWOJOuALGXECeSv1o4ORpK_eBi-pqr_m9Dqr9Elvi997vjRjXR9k67o4ZbA-xyj_MidKHcYo_1c-JP342-yneD0SSm3O4sFz_wxNloFFVmrD4TcBvmyvyt6uPS-jhvFjXhxYtQ0NvtfiGHX79cIkmcz_fx-x2QVCUWobiLVVkdIsnC15B-qaBiVOTwNFHWJMozVZu6G7S2O-aEBynYsPPa3_oUSxfTKdpo_AgGyWoSBgd0ZDZHMvITPUqHh_fjfsxTZP1o0KVHR2QwhyWcsJ_o-_GWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=MkhhQY9J_jD9GWSWhmqzzuUyU3u4EWQM_aY8CWTFFOjBU8qi2f5efYWXlSqhWOJOuALGXECeSv1o4ORpK_eBi-pqr_m9Dqr9Elvi997vjRjXR9k67o4ZbA-xyj_MidKHcYo_1c-JP342-yneD0SSm3O4sFz_wxNloFFVmrD4TcBvmyvyt6uPS-jhvFjXhxYtQ0NvtfiGHX79cIkmcz_fx-x2QVCUWobiLVVkdIsnC15B-qaBiVOTwNFHWJMozVZu6G7S2O-aEBynYsPPa3_oUSxfTKdpo_AgGyWoSBgd0ZDZHMvITPUqHh_fjfsxTZP1o0KVHR2QwhyWcsJ_o-_GWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=SXzPh1mF-u7G0LqwJRSuHl95EfeLZ9RXe4JT5IAIGFoWgP0qNTz40daw5NPqkSxzj0UnTHZioWvndsz6KMqnoRzHIYVUUQhYzl8Iy8z4ZAU_Dyca31g1A1KreOht0oWVDm7RWI2-Z8hLW-wziz8KidONAx9s77E4y6dfJsDU2EpUeb4gfyF6EJDF-Tv5zdMP50NcESW-DwCid7xroGY6XQd7aeJmLpqIfb4t3kX7yISQzfmj1x1YIzxLh10kp9yWdTWzKTYezsEeszGJBiBaYGp2j3ChpyNGCtrJ07vIz6Gibdl8QJ3QgUxB5vEH2kUH6GiYPMcqw9fgOkgfwn9COg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=SXzPh1mF-u7G0LqwJRSuHl95EfeLZ9RXe4JT5IAIGFoWgP0qNTz40daw5NPqkSxzj0UnTHZioWvndsz6KMqnoRzHIYVUUQhYzl8Iy8z4ZAU_Dyca31g1A1KreOht0oWVDm7RWI2-Z8hLW-wziz8KidONAx9s77E4y6dfJsDU2EpUeb4gfyF6EJDF-Tv5zdMP50NcESW-DwCid7xroGY6XQd7aeJmLpqIfb4t3kX7yISQzfmj1x1YIzxLh10kp9yWdTWzKTYezsEeszGJBiBaYGp2j3ChpyNGCtrJ07vIz6Gibdl8QJ3QgUxB5vEH2kUH6GiYPMcqw9fgOkgfwn9COg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLEsNZelW1t6h0C4YH-p6wK-ZlZPFueZ54jw30NE_i5OUT8qVpmgrxvOjpRRkz2kw9Q44GNL8YpbFFPUKycMPoPBGDdFLnHWwq1GBO-y3tAQwlOmUIyEtvzeA6XG5gLvDngCiDS1HnRYlLn7zPMGSMYFSKGrougDD_fBXGCw41HSQEzvcRqCLhDjwB_7wgwLNGaM9xIycRtjLC-itedAXtqAeM2wtKWihOCwtrMRqovAMPVtHQrw0mTJWdanrPc16FJq5wonKaIN4VSPofy35DJtrj68JLKVcYumpp3xjDXDWyiBsUGWDfDPcls8U6eqW0Fs3U3qlgkDXyrGCJjVTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=ZcBW6npq4lEiO_msNGbXthGLk8KVwL_AGxIRhXfw_flHec8I1XvkO7N0v8ZvR51eAOnHRETYrVqf1pLChhAoqO8U2UN-kFo57KLsQgfvm8mL4Od8youTM3YcZbGox8ssLPg6E0pZ7guphzKAPJbfYBPjOr9z6speXvdU9w1eh-GPvOVG4zO9-tpZrbZZuBF5JfbAChW3PsAr6q38riEkfZ6xI09uUEkEufEgbL-zmRqKPddWUbmN35kJFYhaGItX2Cgc1b5yKIn0-2KqjDw_A3mNEy20ZRFU3rG7kCGZLbx1yoptfnDjLx9MzsNb4e21gMJjuwHXiKiZ3W1DZJGfAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=ZcBW6npq4lEiO_msNGbXthGLk8KVwL_AGxIRhXfw_flHec8I1XvkO7N0v8ZvR51eAOnHRETYrVqf1pLChhAoqO8U2UN-kFo57KLsQgfvm8mL4Od8youTM3YcZbGox8ssLPg6E0pZ7guphzKAPJbfYBPjOr9z6speXvdU9w1eh-GPvOVG4zO9-tpZrbZZuBF5JfbAChW3PsAr6q38riEkfZ6xI09uUEkEufEgbL-zmRqKPddWUbmN35kJFYhaGItX2Cgc1b5yKIn0-2KqjDw_A3mNEy20ZRFU3rG7kCGZLbx1yoptfnDjLx9MzsNb4e21gMJjuwHXiKiZ3W1DZJGfAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsDdFwlJwNPZ4APnd62W5aN667siKnBByulN6HEg80ywGsIfUk_6RfwbbzjBaf_LGYwSF7ItE1I9ombDlfaFms3GH7jh4zk9ErpX2HXUWiBkkF1V7HF70KkbnWXggpSvMjnzgmMPQUaxml8eWVJ6b5wEdNrtizY9FWWhZkGkXV1BwgtCuWlPmndqVH0rlnwjMuLCNTpNnbAvhdUy2R3UcenL4lkJvg62FJr69oQliUVnGkr6hy7nSdzcqi7mARjZOFiKNZPtHBca8BPfyqZkM7mK4U1DykTcgqWefgK5TI_nBLyJJum6AwZJt5moIoRoFoB9OjnvE7QHd7lyD-71aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=WeLaSxDNvLIbA6NasvsRriRUDXVGYdtAzZ6H-onRm6r4w4dh-_WdFVaFsSD7LGxzoizqA5tNGSKkSTdvVAjKlxJ31raiff0TIzIwaju9gTlJ4CYgDuuqCG0lNPkATs0rl7mMhCv_B0n5qYsGJJPaWUJL-uTGuEJ1GUMpg5z7--824MxKhKf5IWyf0ulR_XVHDjJbaTVHv9UqSFPMuYQOCfCasPar8p7LXpCrVMOIUIqlYD-dqRG0pjmhgPS6NixqMMN___xJRbPc66QKApzEUeigyDlgkMDxJViRJGLDtDPxRqAtdoAbTW2X2wslHW5BEkfB6LE-Ri5Z7oDmBynHXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=WeLaSxDNvLIbA6NasvsRriRUDXVGYdtAzZ6H-onRm6r4w4dh-_WdFVaFsSD7LGxzoizqA5tNGSKkSTdvVAjKlxJ31raiff0TIzIwaju9gTlJ4CYgDuuqCG0lNPkATs0rl7mMhCv_B0n5qYsGJJPaWUJL-uTGuEJ1GUMpg5z7--824MxKhKf5IWyf0ulR_XVHDjJbaTVHv9UqSFPMuYQOCfCasPar8p7LXpCrVMOIUIqlYD-dqRG0pjmhgPS6NixqMMN___xJRbPc66QKApzEUeigyDlgkMDxJViRJGLDtDPxRqAtdoAbTW2X2wslHW5BEkfB6LE-Ri5Z7oDmBynHXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ow-17pvgvsrK-VFhj0bj1s2jwHjBqqedDi1y9_Ci6ruZ231l_CO3JNYAVxA9lbgTIpRudp3Nql5uLXtiio0mRPq4kWf2WbBxDeMvGY9_L195EDD8d9aBt0l8WjMPsI-v64lRYaatDTD584i1pLWLAgL8NBM596RVLCu69O9_-wzIczC77UjbCJGV2VPayhM3B1NDzy9d4qD80E1vynW3hKWl-PHzzO22RkN-HCS6PWYPizh-rtroXtJ2R72FBhpVeZRrOmrlXHFTuCXTdekYhYCBmrqXi8I5vzF06EQ-kFAULEygVUn5yLSluFOYBvCBYKQtZWQIdyuJciCozF_zBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=C0a7zT8G6AePJ-PoMyxa5vyuhW66Jrt7ChgvzSGQyaQf66YImNV774lAI4jBGjPb4rHtQ9yqTdYLRnsQCXywi2LVEP0f9haoGYwxA3b2UGqSpdPBQ-ECQXGIqBucsUSTXNazLKSBLuwvwrTjaX_8EEP40Sl5AI8bfTwmZbeobgsvAO22pAzPwQRvAJNR7VHorBlkwc6Jnx7F6J_ccpCHInCMTMUkrAOxq_i8eydSmJWntTUW48mjODfjntU4He0RD0vW3cBoIfXhHp4-MABePaLf11xlFT3Uii-OjGNyk3btibYMWSM3eL0RCn9GLJ5qPULwmkhj3mm0ULcL-Lnt5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=C0a7zT8G6AePJ-PoMyxa5vyuhW66Jrt7ChgvzSGQyaQf66YImNV774lAI4jBGjPb4rHtQ9yqTdYLRnsQCXywi2LVEP0f9haoGYwxA3b2UGqSpdPBQ-ECQXGIqBucsUSTXNazLKSBLuwvwrTjaX_8EEP40Sl5AI8bfTwmZbeobgsvAO22pAzPwQRvAJNR7VHorBlkwc6Jnx7F6J_ccpCHInCMTMUkrAOxq_i8eydSmJWntTUW48mjODfjntU4He0RD0vW3cBoIfXhHp4-MABePaLf11xlFT3Uii-OjGNyk3btibYMWSM3eL0RCn9GLJ5qPULwmkhj3mm0ULcL-Lnt5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QuLX2WRdU6T-0Fs3etcV7eCAY_AJJYKS6LE0KfnDV52TC03bNHNJPa9Ukctf17kTRmX-zXNEkPQdu2cYgOT0O8UXC2QhBohtCRqT6Ksk5euAmYXnbbirW1W0zQF8p45reFENBujUmDjHEAw5Uwx2xEDLvEwKGl0j5kp6QGX4GjxAUrYiaSg3fgdTitGF_T4pD8OibHcYb3ZwEbyvqMkDpu5odUI8UtadDN2e2fDAphjcBIAXeoEiVYfWzBs37WOOG69CZaUP3CxaID9jkArLfHz70f-RR3dbOPWGo_R7gnL6Ry4Pddg5BGzLOJg-Vrgx51mpnrGbQGJBygvqUF11kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kgtuYu7LIQCn3uV9nCPkL2p_HXHxTZJZN9K-bL53OUYx9lTD0QSjGY0bfw0D9IKp6LhZP7UphV1_71SItUqJefQ0l5LUGEhQvG_WQ_VnxUruH6eix3Nn_lA51MvkK56BEoB0Tk56bDhdaAzEvYaDmjcC-UP2l1k8tqgfq9WwQJMUtNZaUIVFAcY80bfGDnhn1s2qvKjhVEf1nfo25_lTCTN295mQ6TjlA1trzX0HvoWMdTyn0NO9nbxQJpA2NbLluv2KoeTXzxLd4Q14XiiWKvp3qTTW3KV4GYuB37ce71ULyWk5Wg7calPdtAgWtiYcsrBADkogSlX6pghb7pQ4oA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=WV6W0_3EzYtxXYE9NFMZQepQVLvDzqBmiSFfuOlrltcaIPWgXAey4K0W0F_rQzimmxD8yWZAUwxwPdnAtdUaGq50mVotbyh9gjy4ewDpFpGbYtJXX0AfC8ImIyQNLFwdQV4RjizzxS8tFOP0n3tdsqVPwyiM4HHs8gCq0d83g5cagjk49KOXQ2D3dvmrN9f0q0b7SYqNrPbCQqgu_c-mVRTJ8k7Embc3TDDEPFUeqRXFbrgygwmTrQkpNty-F7t9Wx7RkI4Z-LziI7AhMJW9mIC-6QEcX5KArn-ZUf9aYpOiIqn2_His0Te2CzRtnC9F3TlZ-D8C0q0DUqs3dJxxpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=WV6W0_3EzYtxXYE9NFMZQepQVLvDzqBmiSFfuOlrltcaIPWgXAey4K0W0F_rQzimmxD8yWZAUwxwPdnAtdUaGq50mVotbyh9gjy4ewDpFpGbYtJXX0AfC8ImIyQNLFwdQV4RjizzxS8tFOP0n3tdsqVPwyiM4HHs8gCq0d83g5cagjk49KOXQ2D3dvmrN9f0q0b7SYqNrPbCQqgu_c-mVRTJ8k7Embc3TDDEPFUeqRXFbrgygwmTrQkpNty-F7t9Wx7RkI4Z-LziI7AhMJW9mIC-6QEcX5KArn-ZUf9aYpOiIqn2_His0Te2CzRtnC9F3TlZ-D8C0q0DUqs3dJxxpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiCDOkfR21fI1y0Zaxw6fGJL-ZTk17NnDfUnV-0C2CsNc7cnI87G5CEhhnS2yJm4crfj84AR1qcXMfnyTuEfVStiBRdwKACBLHlzqwWKeLzYLYk-YHMIMS0fT0rFIZVUzUxELpSGoMxAgbBazFnF5QvwYMH7z17adgLI01jf6wq60sKb1VOwgPMFTuGUpv8rvrqB4uUPJFugLnq6wO5_oOgsOjAhmj2ILVRqpzMF7rDGD7kq9-jb7fmkpWoV_josYl3wpSgTxZRb11AKqSbJGlCcus6yjnRvVEj1Ek0uHSzUAGevGU0lZgXLs2rfFTWXuIrMHOjPMtEkeEDIUBcS2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kk-LsXU8io7ot_SZ8XU84i9_X6ekrBD6GnOu7-UvbIu2xLAkv2cPU6S2oQFlrgmzw2iN9Ljd2CMCOo4nqNgVd0lSW3ZwuUA_sHzXDxmawWSJRRKc1pkdMSyAFVlVvrrQ0C9Wr5i7CuRTwBMg14IpGhlKQCEtOXOEjnq28PdvQr1VvZTcMAup9RlB5XdV21DfTsnio1nP8nPtnf8cX7LdAecf64qlVkMTBAPBUEYepWt2lFwv4A0SLT_tlPNporV6pgVo3tdlUflFG3L9CtztCdj8ZgfCs0pM00wS21S6_U5r_AUsvZIXjn2JEdJDoVleWMxm1VEvIFfIDsxoVERHfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqCqme8getJ1D9Ozk_edCwZmhdt0umJ3Sf8uuFvFzD1-6cIH-XZAIItyzDoRO2-Q7NCp3WkAkjmLdv3WsowD0MNewaD4-X6R6FI-t5FXUZYMzy5slDMIXFPOA5tV-7_z00Pz_Yz1SudrN9QyAZ_LN4TMgHUO69VTnH5BUDn7KiTZjRanWJlElmiv8u6N5qSqaPD8K8hJiSaWFJ4Wlb348gtpDujDyDTu6VRQDcVGp8hI7_sRCNl6euug8IzKi6-KBdrxYJuwtzqnlY79yLipnwmQFV3Xk5GfdIE6mcyA_4ds8xeyhlzseI2jnPzhXQL7yZN0qL5gpqjyhJrQQazCxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ep_LxCVz1Up2Ake4gaGNwIWTD1SFAXzOX1j0nc4oBn0RU2uiQsPQbzHdLbO6aRu1HIpftuCDtBxMS76aRRUC8lybojJCyXQafJQEadwiWrJmQweUbKAUQVFg6C4geZfJVTggo1QM9OKQsezmFR5UbJXsObt27ePRpd-CcnvXvOLqULYdTkXlXI5cvkmHIxl2-ar_o21z19uvqM2E7O9naeLYCDGDur_-MOWrz06Ikpxay12axsNSvX0BdUgjMWKE3YC_FjeS1Firv6bZl4Kwh01x03hd-_AsPsAEZqyiIsJwGQDO9SrJBTbG-PpEMFcpk28itHa6qaXdImZ_yIPlQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyXv8SP4V4ObO_-yJvNY3C1Y3wMcNTLUcheSieGyUt50x9uIR9a_WHCCrjYfZA7MDkf3z3FHPhOR6B0cT0gVS-GUVxHH3w2XnAvYtN9rYwDCy84lWtO9AB4dBXEo9l3aIdmYt90UMWCXf42kcd29k7r6GrGPrEhT0mUc7pd820xqJfJCQ6C0rmgGywXDhiNO-cQ1rXllGfdWKhzQSCOAFn0pk9tWsWxF-BTI-GTokqwF_fcZNMI2DUoRI5Abm-lt65enS9gyW6ij0xZJ4V3L80BHU4kaYPJOmgIFkbTXXWbOVx91adfDfxRx1-XolT0Egojb-nVb9t1tyRyPUvvCYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=nRABWY6yKwcI_mtwDS4SlkwnprUwQ0HTe1ygzjp9jkRuDifQtyb4vEs6y75dkzd3_3w9UPApME_GbbW_ptqXl6ArmeByE9lQDSfwCjtqAWll0IKp0aTDO3-KyRpEuJx1cBP8tlQQjTZR5DId34tvlvcGVYOUNM3zkMYiKxTzKUG06mZEFwDPxaU0IqOY11L8sYZjtag5zgvdwVJE3Kd-NQ8OxqC5Uj4YX5p7QYVYprj_k5CcDwZMsnpRJWo0aymwyU532J_JQ4-DqO0pT-7KPiGoSWTL5K4SZOExJ0f3DXTlaowqsS3ysRWSNa6iRkQ2id0RC24Sm2spcaZHkxBsHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=nRABWY6yKwcI_mtwDS4SlkwnprUwQ0HTe1ygzjp9jkRuDifQtyb4vEs6y75dkzd3_3w9UPApME_GbbW_ptqXl6ArmeByE9lQDSfwCjtqAWll0IKp0aTDO3-KyRpEuJx1cBP8tlQQjTZR5DId34tvlvcGVYOUNM3zkMYiKxTzKUG06mZEFwDPxaU0IqOY11L8sYZjtag5zgvdwVJE3Kd-NQ8OxqC5Uj4YX5p7QYVYprj_k5CcDwZMsnpRJWo0aymwyU532J_JQ4-DqO0pT-7KPiGoSWTL5K4SZOExJ0f3DXTlaowqsS3ysRWSNa6iRkQ2id0RC24Sm2spcaZHkxBsHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=popYYocgJD-D8Ne5aPUq223PrKdMxzEMSrlQu5J33fmv5Gb_oSFUWZkXvr8nfgkI4WXGSRFiYx-oBcXn6JGukAlxK7Fwzg6OeQBBUiWDMEcoNz_mYnZBomlUSW6v5ipWawgUyNLN9jjfblemOMusPZW6DY8vkWAC_uK7peSkL4o5Yx_gcf059B-wrG8hgwogL6qxB3J86mcMfpuBX3v1ahzHRSjXcGcV86KnAbuxi7bsrvwgO9sRdzPBtxaamFn228YzXQbTHTY12y19ujwO3U6jYGeIX0FPrdBqGM_otWzZI9QyxQ-2hay0jfgVSMGGETWTt5ExjcNK_84rSvP1Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=popYYocgJD-D8Ne5aPUq223PrKdMxzEMSrlQu5J33fmv5Gb_oSFUWZkXvr8nfgkI4WXGSRFiYx-oBcXn6JGukAlxK7Fwzg6OeQBBUiWDMEcoNz_mYnZBomlUSW6v5ipWawgUyNLN9jjfblemOMusPZW6DY8vkWAC_uK7peSkL4o5Yx_gcf059B-wrG8hgwogL6qxB3J86mcMfpuBX3v1ahzHRSjXcGcV86KnAbuxi7bsrvwgO9sRdzPBtxaamFn228YzXQbTHTY12y19ujwO3U6jYGeIX0FPrdBqGM_otWzZI9QyxQ-2hay0jfgVSMGGETWTt5ExjcNK_84rSvP1Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=QDCbLJ7Zeyizp4YnIIWIzxESUnHp44M4b9u03Jd7ofzYTjrHKkklbcPPTNVHmux_VC7RBBxgiKORqKQQpdKLaEcYtcqXJ40OttOgFuXIMtuoFELP-ViPp7a50VC8BEYmpJfjY3OfaVIhAA93Re5UGICNlO7y2EC8bbju419R4dNy8y1GnYzk_KyycDaTz8RPscpioOyKChCasFDlDiKodAO4RUVlqQVh8ZSXZzX834UsO0EfHmkvkR6HAqPGNasdjnmiYBoPLzfeiTEWZTOCyAxW824IJWqUJeJx8fW8mxdXNCVv-x0vQQA4vY9TarRGIOElSJMNGOhrTLwcbelKhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=QDCbLJ7Zeyizp4YnIIWIzxESUnHp44M4b9u03Jd7ofzYTjrHKkklbcPPTNVHmux_VC7RBBxgiKORqKQQpdKLaEcYtcqXJ40OttOgFuXIMtuoFELP-ViPp7a50VC8BEYmpJfjY3OfaVIhAA93Re5UGICNlO7y2EC8bbju419R4dNy8y1GnYzk_KyycDaTz8RPscpioOyKChCasFDlDiKodAO4RUVlqQVh8ZSXZzX834UsO0EfHmkvkR6HAqPGNasdjnmiYBoPLzfeiTEWZTOCyAxW824IJWqUJeJx8fW8mxdXNCVv-x0vQQA4vY9TarRGIOElSJMNGOhrTLwcbelKhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=nZu5tZfwao0XSLZRopHwdUpfPp8o7A0ZwLyyQbYHRDrnwQJeKKfLaMmPMcc0Gn1TXgZZv21QYHgWnxPPk4Ep1ONP7o9jrk1rltn7HcZSpaqwyAd3brOQuTg67DN-ef1bIokgTMYCp4rG_kCxQ7ZUJUrlMs5DjOAZETLrYsKSnE_QGmeaxOMU5JHtX_EzTRXhAKn8XMuq7FLs06LBPWN1D6iA9V-b-Yrp94lSyfMJ7WEBm1IxtqfGtshFV2hzBIHY-GMuP_EXZ9vLk6xYFDMU1Tmu1fc7a4iApb0GjWdKCsQ9OsO__2eD_sAKuhIsT88H7JwhhVnskFeT7Exup95y5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=nZu5tZfwao0XSLZRopHwdUpfPp8o7A0ZwLyyQbYHRDrnwQJeKKfLaMmPMcc0Gn1TXgZZv21QYHgWnxPPk4Ep1ONP7o9jrk1rltn7HcZSpaqwyAd3brOQuTg67DN-ef1bIokgTMYCp4rG_kCxQ7ZUJUrlMs5DjOAZETLrYsKSnE_QGmeaxOMU5JHtX_EzTRXhAKn8XMuq7FLs06LBPWN1D6iA9V-b-Yrp94lSyfMJ7WEBm1IxtqfGtshFV2hzBIHY-GMuP_EXZ9vLk6xYFDMU1Tmu1fc7a4iApb0GjWdKCsQ9OsO__2eD_sAKuhIsT88H7JwhhVnskFeT7Exup95y5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJz1Y5UAgbgrZ0h-xw6cJccUv8H7dyywt1QTX2q36KtTWn-DDnFfvlLDO_Tn3N4U9YLS9AcIqlDk3gefeKEujgPLYvXLaPE09oSN6WezHU51luu2rCibnS-UvfvHkQ3IvK454XQTzyRvm_-AU8UcdcmA3_cAjBAshWo4epxJjFhJmKj07XmyHVJw4FKf-MUNBkOf7X0UiG9rSoWFXkn6lViqf0IW7c5y6w4N4k67NWP1U-WDC3UAtxiRCByM9ntGUf8aR2UAnZ3-ysbXmpqFVAwXRbjj6e9yXO9j9viPA743j8gzXxqhdTrZz-bpxpfOh2ltf9NNrnp_u7a-z81JZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0-tFe3jS4VSNnSuZ8TO88B3mFGvvLcLSMYIxjJ2aaM6VLL6dX2BzL_m3zaCYLerrjx4YlrBmXqEm9M-LPE1iRkfWHB8x7DevJ8RHIB-zk669CkwGSH68MV9DGxWWOYVzCDooKaK21mBdR7kYpZauAvv7YDnaJAXj_g1u9BvMEooxDxVtyfJL_v4R2g8V8Bei-JERba_J2rMH1N4KXFFaOm_r7kZX8FD63aDLvkEDYbi52KT7oJWUn-WUqoTbKr96xWIU7RAWAvD6kUH9WUEMF1eLfBHZk0cAg1PB6M7BdyjOtnvOivhzFpCyQ-3YA1bu2mqfMsnsdZDgTs71ADt-w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=tSwgzfwa1AJPuXTr3GXB5PZ3PZ5rQjCN7Ihhmwf8XvUfqzub33kXEr-rLjwfo-H2BXFYpITBCa1vvMxEn8ip-Wh8790iWgqXn32RNJgwko0Wa6eweT8Lmk6hDkmbQRz38NBdBcC7YT9ECAPveV8I0oCu8UtZcY0zsoihdKM_p1jRYnkdXAzRXjmG0PJgam86cFj7kGPvvYhCbreM3atz_1B4IigYsBiabdXLBrmgQTO669HdGBwN5EhHGbNleS3YT7fEE6kbewociUpAGxh19zlKB8XGlHHQ6c2qhbSWxYsoZl5NU5lJ6oYYcvRYL7BwhECeYMSG1lgowvU0d4Dheg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=tSwgzfwa1AJPuXTr3GXB5PZ3PZ5rQjCN7Ihhmwf8XvUfqzub33kXEr-rLjwfo-H2BXFYpITBCa1vvMxEn8ip-Wh8790iWgqXn32RNJgwko0Wa6eweT8Lmk6hDkmbQRz38NBdBcC7YT9ECAPveV8I0oCu8UtZcY0zsoihdKM_p1jRYnkdXAzRXjmG0PJgam86cFj7kGPvvYhCbreM3atz_1B4IigYsBiabdXLBrmgQTO669HdGBwN5EhHGbNleS3YT7fEE6kbewociUpAGxh19zlKB8XGlHHQ6c2qhbSWxYsoZl5NU5lJ6oYYcvRYL7BwhECeYMSG1lgowvU0d4Dheg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jF4mAExYyuzHQRX989NnLT-fDSSrZzjIi8HVGtVCtFDAP5AWKgK_jSaGLE21zGcD8ZTKTLYicNEsjdeywtU0I6mWNDGwuUfQt0otNZNjbz7XH5f3g8YvY0gwn4Vl37WwbjLVGvOQJNxqmmuF-kugSQ56nQWlNRSLwLnD7NhRFbiP6QfpAW-6sz5fva4wb-wWw9oYVQptZrS2UWc09D7KP8GYByFxlyiEuriaOXWLuf91Hxgd4VJTouUp7xQRRLTPYe_8Ak_RjAE3xdoqNgMUdfDBiDudlQQ2cRaS-0P1lI-2ff8tbcrqdt7bjmB4x6VIuOganSpwefwIeCUyxEdVpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=IslTMl-2fOXJA5ceoaOldyNWkIYAi8jOUpHdmu0C4v0LgRsbBmQp203gofkI3e4OwOdqm46x_u98u8XKEMT8R2cWH1EMw-SECGKjiZdJtNuFEBXbmqcJn_pJMPR7uy8T-rwIjIUFtCzvYmz82vf7H-OKH8TcUNw2vcF6YDnZN0egA4Jgo-jmE_Cw9Ik66CY8s4e7GOUVa9CFswPnpiQysw5pGEN1PmDHnidj2L5hm_zclfcYRTNv6L8xh4Ey7CLX0Hmzla4hvdxhlU4iK-EL1qQ6d1PYmpkXtPErrunduNy8p8sH45enq2fRsigmMHKydcEr4QGDhPJWbbtJzOv7lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=IslTMl-2fOXJA5ceoaOldyNWkIYAi8jOUpHdmu0C4v0LgRsbBmQp203gofkI3e4OwOdqm46x_u98u8XKEMT8R2cWH1EMw-SECGKjiZdJtNuFEBXbmqcJn_pJMPR7uy8T-rwIjIUFtCzvYmz82vf7H-OKH8TcUNw2vcF6YDnZN0egA4Jgo-jmE_Cw9Ik66CY8s4e7GOUVa9CFswPnpiQysw5pGEN1PmDHnidj2L5hm_zclfcYRTNv6L8xh4Ey7CLX0Hmzla4hvdxhlU4iK-EL1qQ6d1PYmpkXtPErrunduNy8p8sH45enq2fRsigmMHKydcEr4QGDhPJWbbtJzOv7lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtIAlA6NNGZetI9SIR36rPnhZmBwlgzDo3xinAkbwJXNYW0uKTgPA6kWDc91lIgsuppbr0DgAcocF_nnPJbTSfaB6ovJ8FV9uhWyUKHHTz1ik3nPBbK4EQ30X-ToveEHM1gyGD0jGYfryKRBY9u50NmTqMunx54wn-p_mquyKs9tQU6YRod3fyCiA02DZZCTldikINx4kXQJWl0RuL_7J3QewTcofKCAroqPACwDivoKzz8ByFUdiRG_hFnfyLQUezXCVkysDsUDbpN7DkiE8v2BxdERb107RD2uPsaQNBbfPGdGlfMuOd5kfeZmJd1ghWvEacjegL40fnaXCXZPLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHLeVYreH-Ybnw3iQxJgUtb1grAam8aXyHwWSCu0jvArr_EKwQ5XSg4W06VTAgu6XHv8WSbP-iPSaGrXXtJBhD4Kjz-VZQyZyiDzga6LPQnhYJDzvkHsVRQ9CT-nE2Wrk5MoA3002EQwvaAEmMLNhSnYixWm5FhTnt-RuKPXAWacFddRpF0nz6ZdBa7dYJkf0ZF5Z5rc6w9jRC4_A1ehc-w7S8tw7sFsT_K3MOjpp5U7crqp3HSSFS_3ghETTd7Dluty3smbUb-9rgu9kx7QcpDoWsdE3V57rwWCH2kiUkw1tyXd7xI-20hs3Ej_lhBRltHVqJ9qBvHkxzrohLhSdQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=DLqe-vOoB_SUtG33zWrd4VUd9PczCkF9TJ-ef3T9YecPp-vM3S92sxvaX8xhBB27BlpWvKsik8HMVLFtekYC6R3s8XH6NTdX9L3O5rEInOr3V6x7QGcIt3ALgZmtDgU8XY-RoTDo1TqUR3wQf5uEUNtV8euF_gyYoDoc1rPEqI48zmBQHgJIEA2VYk3fmnJ7qumRhj2Z4h-aCrNNrM4jc6t6p68GpbXYEAIdOVyX0ZyneXUG8QgTOjT3AbLZNu8gEmzty2s2N7nhMrNauO16SnH1yrdHV-6zm6amap6EL_L0bWYxx6uEjqB4QCHtK9tU1xLRAol5EmP2rRyAExqdWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=DLqe-vOoB_SUtG33zWrd4VUd9PczCkF9TJ-ef3T9YecPp-vM3S92sxvaX8xhBB27BlpWvKsik8HMVLFtekYC6R3s8XH6NTdX9L3O5rEInOr3V6x7QGcIt3ALgZmtDgU8XY-RoTDo1TqUR3wQf5uEUNtV8euF_gyYoDoc1rPEqI48zmBQHgJIEA2VYk3fmnJ7qumRhj2Z4h-aCrNNrM4jc6t6p68GpbXYEAIdOVyX0ZyneXUG8QgTOjT3AbLZNu8gEmzty2s2N7nhMrNauO16SnH1yrdHV-6zm6amap6EL_L0bWYxx6uEjqB4QCHtK9tU1xLRAol5EmP2rRyAExqdWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=mOKe_1whMoFYALmZfWInqzhdtXnhgN6PSWRTWO1JQwi-smEbByJ8akxrZmFUZRjSvQqCYZNgAOyCFhs-qENdHGqHkucHabUfM9PB-jojyAbRmgTROAXcqcQRrrAKsEBBsYP7S8Wk4QaB3QbSZ5CoGZnL3IYkZnzJZ9w3Q3k2cfDWEMkf8wBiitMuuP9kqlxDn7-7kfgQvs627aMAJYwmBAnm9pvhd5eqvJliZR4Hzvq5EHtvY9X1HsOJi7QOk1T7rtH6osZDSYZpXoJilrUFKsHe0MgkbY3PYhkemtypixDFV39PALY3WVrAFPJqUVbKvHy0BHQcd9r8f7NDsG39bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=mOKe_1whMoFYALmZfWInqzhdtXnhgN6PSWRTWO1JQwi-smEbByJ8akxrZmFUZRjSvQqCYZNgAOyCFhs-qENdHGqHkucHabUfM9PB-jojyAbRmgTROAXcqcQRrrAKsEBBsYP7S8Wk4QaB3QbSZ5CoGZnL3IYkZnzJZ9w3Q3k2cfDWEMkf8wBiitMuuP9kqlxDn7-7kfgQvs627aMAJYwmBAnm9pvhd5eqvJliZR4Hzvq5EHtvY9X1HsOJi7QOk1T7rtH6osZDSYZpXoJilrUFKsHe0MgkbY3PYhkemtypixDFV39PALY3WVrAFPJqUVbKvHy0BHQcd9r8f7NDsG39bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNUC4A5m6iFiaJ6KX2q7x2V-vjTotlXS0GIj4us_-9b8u5Tst19c0G_DurWJDoLHnA-UyWJ1TjA8xsMLv0wVu5yMxXN9t1vDX75oVVlT5nXYMT6awIgPKPCSPLUMUVVg7bN9TZphZStvJatC0H6rkbEawaYmIrEOQCh7KnG8QEqp5m5c26upfueAhnt757arIMkOXm0Qs_OoPESgVRHMYdu3NgB15Gn1PhIk7OGnYKUeGciKiAC3--0VCAEEHlnRGuK9kNZKHQkHz21JBsdg071Dm5y6cJZsf6-j_KXMfoQK7N-NP05dbjBhOnU0AH1CbRO09pxJa1ygfmAHIh1XpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qph_9jV_IMpd7CV0QiHnFtl7DFUDYIcqIiQSmJCkLaLMdFDth0MLZkzTvG_QHsjkq3YIO6R0q5wwzTnLLOgfOmRKAMXGLt5bZVWQSujL5pu9tFHrlHTLZzI76AiYFzNWAURFmBwg7vw1Xw6ouIJQaTiYA38FjqM8acDNCGQ3KIogen7P2P2Yb4lHQKGneLwPUysKsLDLu0-HqJPVjgUQxcAZgMQFcqxCtKvnS9ZGEROAMzYFYzB_zRjIwTjYBK3SV81QjMLKz22hNxI3VkUjN2SlVZfvE1QBK7kzzRiAUc0eUMl-hOvBMvpw8logU8aKv5m2EvqaXPrwZhIBFCcwoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTbtFHGNChc4VFhUrVMMILrbpvNo5Jgcd5_whmOUszbPsRLhhGgQ0BUiu_Kxerl6iacsFOrZGls2VnG2EwcwhxDocsRZy1CvJEbhlcfb9MBotgdzS66WJQRNcu6zTL1qSRw39IerlDZ1F5wC8IX0nXgkVMpajK0ZzWqpftTEeNFLqyfSYFkuqi-IbHmLbvKYnO-1qYidVsBWO5xr1j_G0BaCLM8QzcgLybumnxZak4kP9P78yve8Pt72f78_GqV_H4JuglUvgPYkOGlwP5V4pT1PCtoRumzf-agtfP37JcRN32bnea664mrmziW_qJ8NP7t3dQlJWHkT-JUGdFR2Qw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=QP9U_LbMXuN1vAwmzVkmJ8dXMe02QRTbwWs7LTyWSRLqT7op0nAGRbOFFavA8wArJUF1wsvd0xfS_6gS17HfR_raI23bNCrxEHPCtOUBTpTeyW0dSliKjxmpMxXauX_O0Bimtuu7L4AJOMhRpcIdlzwAXmn4mQxtwbcEvOHUegVsNBmdrnFryGl8GSQw_U58J_1Q13FQkJLH0avqcMZnX3XAwzLg2iXdXXptS5xKWUH3YAlr3pca9rabf_gtYLLizHofhLNXkS9R_KaGDxIxjInGsagxF8QU3LeeI3bdBT59u52IAExfEHaXR_pTNGgMSv0TrvTb-U-n_FjCv1_KEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=QP9U_LbMXuN1vAwmzVkmJ8dXMe02QRTbwWs7LTyWSRLqT7op0nAGRbOFFavA8wArJUF1wsvd0xfS_6gS17HfR_raI23bNCrxEHPCtOUBTpTeyW0dSliKjxmpMxXauX_O0Bimtuu7L4AJOMhRpcIdlzwAXmn4mQxtwbcEvOHUegVsNBmdrnFryGl8GSQw_U58J_1Q13FQkJLH0avqcMZnX3XAwzLg2iXdXXptS5xKWUH3YAlr3pca9rabf_gtYLLizHofhLNXkS9R_KaGDxIxjInGsagxF8QU3LeeI3bdBT59u52IAExfEHaXR_pTNGgMSv0TrvTb-U-n_FjCv1_KEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTpwlSKNwVIQPyCpDhhsm4ReF2RFKrvH7R7R0CNhVZHk5EXGMHc75SM-8cj9_3kY09mofPu7AZx5DQxVgEIAhFM3HlwQy5AQNC2thIBgIY_8JUIj1Bwbll5uWAPfQAOzmODC6vNCATFdisep6PSRTBjU7ZEiq0uqkzqs-ZSBjnP4nGUkgHeNgUTQaWwCUOI89WgFXmPJFhneF4ImXQutZQs62WnvwSUY-tS3X9fOQZglLrGvHxTRwDvfeWVTpl82UnjimVIF8iOrPt5YwTCW59OVeYECG-XV5Zi_HmbTLSE89yM5tEwxCWKJSDfwB58GICzdoxwYAkf2f-eRlmMWug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIP2WYQaTTCd3eZfFoV0ODgG4f2KEpWxdSS05_MG9yqhtlkykG48hA2hYLZxS6bQ9xyg1uB6Y1VDpPSA2AVmi2f9yRYkndyqCRteeyfW0SbcDk0c8K0atJY1COZlaG7Q-qn125fq1RoajUc4hkQK98yUH2pShSogC5SkBEcgzDd4k4MCthYY1uOUQl4z-70GB97r017czor8o_EbvZMbzJbVwWbk_E2QHBe1LHQR-0VKQRjmsDmTcOMKOzmZNO9CQKN9BbPOLhcw2JLyW9sJKfH8k1Q9IBA1IsnAOQJQloI12edk_3sKlwpRHOsV9OIWNkSMXtPqwhtZrR80DYGy_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
