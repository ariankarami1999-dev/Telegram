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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 15:06:33</div>
<hr>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmdjgjWxEQuckLdTv8N3YkIHT3mZ55uTCEXVEUmtjcfR3S65A0FeSghZc-Ylw45bbMoUqmy-q9SR91SOM5Ov5-vW049M9Lj7UBlVvKcH0KXXOZ3DraVoVEjjyCvNdx9F_UCmfjVONHnp1xhDmMBEyQvqL1y4VOCgA8zJyqel-NHIzFL2J2AAHcp57cvhoh6JOWAuIytaYpljmJUqWRJaDdPo0GfC3_JrIfeASDwpXycpqetSMCnQzC5f32nsLm0PZgj0YuIRJUEKMTn2pcinS_jnXxJxPBFJBs0hLFapJvQqs4iKiKJarxVXzDTCU3nV_LkymwNc6qxHFz3hrnn2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=DDUGI6h6sk2iTF0lDQyqYqpe0w--GDQAXtDqIiXUigsUI51HsfpwgqJadKBOx4kpcghFujV709qBHGgFCMqdw0DEBosAYcQLQoLqRtsFalgxwB6bFbCusaF2Fdp7KHnDLg0rVCFxm_CDPfDA_8oybEulmCHw3l31NbrVF2qx-ESlG-IH8I_DPX-LRb-ziu2wKoTnH2Oc3T8r9ZjZb1segzw34l82cADt3cna_72QDuK3j0i1LqS9s1tUZe73zy3gbiV54wzXh2smBwQjzyjDVh4jCrQ3R77BoKFXG6ZSEVqOGuQ_FrohLX9zlFCcfZvBemur09eTqOIce57TvNSQsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=DDUGI6h6sk2iTF0lDQyqYqpe0w--GDQAXtDqIiXUigsUI51HsfpwgqJadKBOx4kpcghFujV709qBHGgFCMqdw0DEBosAYcQLQoLqRtsFalgxwB6bFbCusaF2Fdp7KHnDLg0rVCFxm_CDPfDA_8oybEulmCHw3l31NbrVF2qx-ESlG-IH8I_DPX-LRb-ziu2wKoTnH2Oc3T8r9ZjZb1segzw34l82cADt3cna_72QDuK3j0i1LqS9s1tUZe73zy3gbiV54wzXh2smBwQjzyjDVh4jCrQ3R77BoKFXG6ZSEVqOGuQ_FrohLX9zlFCcfZvBemur09eTqOIce57TvNSQsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxFz44CZ3kCcIgGOUlCTGUOCPURyLb_cAeSaLvPM2ekdL4k2M37l5i5nh841-GHVldDo1VaB0hj9oNWOCYQ9-jJ1TgUjp9BYC-lLGlLhO2cyx2KBHh8guuCpZ5XuVljXTHBGW5gnbntOK6JHOr71R3wTYvKAufMCk4-8McBJ8VWQkEJZ4eItyPPiOkq7ixntWJl33r84zbsKvPaP0-10gZSbC9JRfjJc4AKIgTJhEAv4gmWuwxchKotejflOBmjiZbL4DkcnRrsYtoqqZjnpsxNPAk-wCdhIa1bYa4FSvo1SkBSdvmT8qvEJvlRJCU6hfh7FsMh5x3ichxPd0G-p4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JX2Em57BlV8AHrCHXvQjzSsDaWeE202zmSRAsTfJuGGzQsv-Jh8ge2zHT2DcmIyIgNLjtjcYMybGx2PhoCZpj3sozzZm_mgvUjOxPzGgihLVSe75kGM6KWfLDcqYDK_BsrdkhA5tJtnBE2xykOk0Rp_drzY3sOFcgnoAiWQsNXRD_DbrNC4y1rOgPYrMakY8FlT2ApJlTfrV7P3sqomo1OLUyErcB6gxvreLz5gedLYyhSzszeXYbKAukjh8Aytr0LRJTUgqev5ZiX8AB3rSUdDo5Jfh98HVtj2ccTs-LOj7G-2_DR1jgqjPwmhI_NFCkeISF_fstFLoSOXSasXSlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=PX3zHDXBqQEXd4oLvAo1UmUEkjo2iqRBfsAKrJidrJsi0y8Hi8xTOWD0cxbXjRgaCww4T7pUvjbhotVekWSPHeX78lQXRvKUKDp-g7fjp1O7IyEKtph-n5-sY-Isra4QVsj5WbCD27oPRWtH-VcKepqijtW0BY7KHeoXmAfDIMciMEox5HfQm_YRMiUhOaaMVhv8Ay7hTMYlGIf4RrHqe8IUWpOSKSWaflnUCPvb_i0Ctj57P6XM92TEXNLx-mZRWb_tD06yS06azx15woW4uMSyxMEUPoa9dgcJ1K8JS_mtBntjFYI65qZU_pWfzs-GcnogMytjxfQFN78op_0Jxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=PX3zHDXBqQEXd4oLvAo1UmUEkjo2iqRBfsAKrJidrJsi0y8Hi8xTOWD0cxbXjRgaCww4T7pUvjbhotVekWSPHeX78lQXRvKUKDp-g7fjp1O7IyEKtph-n5-sY-Isra4QVsj5WbCD27oPRWtH-VcKepqijtW0BY7KHeoXmAfDIMciMEox5HfQm_YRMiUhOaaMVhv8Ay7hTMYlGIf4RrHqe8IUWpOSKSWaflnUCPvb_i0Ctj57P6XM92TEXNLx-mZRWb_tD06yS06azx15woW4uMSyxMEUPoa9dgcJ1K8JS_mtBntjFYI65qZU_pWfzs-GcnogMytjxfQFN78op_0Jxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=SxPnhcOA_Ab1TO9oIDEk7ybUBFSjeyigopKpBXGtZGP0iO8SgPOuL7P6P9KlBTRbBV0GSC9tSsc6n4L1ReckjtsEB3VH_ik3neyPCnfM5LdBZXyAK4mlTEgE6V-UO8esp8On-ybHK5Msdqu5BClcfxtgErM3VgXy0BXE2HXvL6TfcxSYPlRybPF6AWN0gwL1gLbzsBjR5CZPZhlA5FRRUrtYM4YL4wFHPZA-WPtRq5I9Y2SEnYCVNuHdZk5p-Ax7Ff5u5T7WQw5CT2IcU04p7LMmdKavrHh8RTICq9RGpY50WVEtxkmkysx7ZmFPtQYIYyeuF5RvF6fccBrRi4VBlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=SxPnhcOA_Ab1TO9oIDEk7ybUBFSjeyigopKpBXGtZGP0iO8SgPOuL7P6P9KlBTRbBV0GSC9tSsc6n4L1ReckjtsEB3VH_ik3neyPCnfM5LdBZXyAK4mlTEgE6V-UO8esp8On-ybHK5Msdqu5BClcfxtgErM3VgXy0BXE2HXvL6TfcxSYPlRybPF6AWN0gwL1gLbzsBjR5CZPZhlA5FRRUrtYM4YL4wFHPZA-WPtRq5I9Y2SEnYCVNuHdZk5p-Ax7Ff5u5T7WQw5CT2IcU04p7LMmdKavrHh8RTICq9RGpY50WVEtxkmkysx7ZmFPtQYIYyeuF5RvF6fccBrRi4VBlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zi9io86Op95OGkoodVGRmLU3JqldejETKqeEaUeJ7ubKoTMmxaYJdJOd14AF7aUc0pS-FMXOHfIt1pbx-7v_9R0WbCVF2NnVKUmGIPfBI76-Rvqlhs_9aCYqFTNN2-PXR4mdZACdF_nRiuanKKluJG_cZP0AhtPPOHbRl08q11xIV17rrQBpVIh0rfm3ihDeWjNuIGz9RY6dhnuTObPna63n3EYlJkgDpp1w9dbZUfgGFE-zZSevUBEAWt3w1xBT9mYreejg00D8to2OofUi1tZmJnNZhKNxqfd04abFuwtn42WNOWxSkirBwI7fF-loYDqsnJPNqpPVqyyTughrmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPv4zlnOPtBcyxvpNu53dEjnxLCY9FSYzpUGEa8o5G8wPV0waLcREqAJZtb1H5HCsKlWz-gXL0OF4KqsWCGj7jngJOBuZuZWxloo5L8fZtG3v2qHg17S8uwjZsitxOAPoa4XMtFpyqC-5HGc1BieB5QExO531_P-kz4MVKsbVbm2oc8Verf1I5Pg0478VUh0zrmwYLcEH-Cq-fA_VjyRuRAYfXBbx6pY9ulPF4GhZAdIghMVarN_zC2toQ3ZjtBS2_My7SIOPFYDYPEb24BaAGy4Dk--6j2r7KBlllinWIOBj-G2ttarumz_-_6uc9xvCpFnU2CWkG162nSZHZ0SiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r3z67X9JkE0iA6VGYTVb7vqyZUkVjtXzKoYKxqA9JjfZGG5BhKzYtjBpJkcJsb02p0Ud77sD4jGuW6DVr4XLmmMSUPfX0Cu1Rq6zDp7kSGLEmlkSwDYwlPcVeLOmBkCR3FE92fN5_TgNtsEE8StX-h2D3EvnXXis_Gk_Lwyd-CQhBCOWxcpmpLiCyATmOQxW4b5xL45RmMoIQkMWhmaMFbflpwE3xjTw5rlrpjm7Qw9zekNmreEJhEyI6R-2zIAXOPz7HOXBVcPfAcBWwCZx0BTwK0NRGgXKGVFIB6dqlNXeXxqq3vMH6vI6DF7i-rTrD24QASs3zFlZo-t7KpW1zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ScwO_3xK60fcKFljmgBJYNV4e4DxBgqzEO1uLenk2HPvA7TS5onQn5rZA_X2yNFwcZsHXBsbUikXWCTpD9Dr1bu9JtbtVedrgMQI9QZmvCLi_PztZ6ukdWeP28RVTYs88n-DsmIQ5n_V6Q0rhUG7HnPbRNGF1ZOungfj6kIo9mnYIjjQy8jshqJrI5xfyrAB3nKIrxWKv6FCSfeBJ914TRN8xF08ZwcpvygjimUi9h5waxF8iLjah4-GFvuCGZuDM2YdSyRHbpCg0zaYXAeVt7Z3CMkGrAUPdK886X9d2YhCYO6u2zrCJiFyY-7JMqw6eW2Hq7YRWaeKmdo_W9xGrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3bxx4fxSx63_FfohgEqFjE1qGXeTDA3PbgbUXfn4-UBWE2tNwtZpY94ILw_HFCpqV7gDm3U4qyrTJW5URhuOqlkFeXrX0msXySBvg3VzD1230_-Ky0eoCs6ROVCXB9yEqoxkBhT9IDTTaxuRapMh9WoVAFXVa8R8sazgR4khfsfc4kcWhD4G3fe4VRhKnJXsgjWJqnbEHE0QbKwE1m76EHzHQ282hdhodCQ3QGwSwwtdsJsVG9Mo6mO7LCXniobGjJpBYTnlr4l-RS8PeVcDPWe58b-aCKLB1-TRzymFHshMCQrVLVtPMllBtxnnLo3bolui9VpDrC0FUrH-nitKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JMEJDHImA3LZAKp0PlrLbwyqddPAs-Nx8LbBSYrTVEqk23uh8oppLDPO-HYR-MOlGIzDmRfs-ftdSEVHW9-1G1UZQM0FGPVxRIQz2GfdVji1to_LDR-UkVXAM3lFNvbITVwojZpIy4C7prwsBuGcV8WcAu9xUihIkvGcZHK4YU_FOz8QP3ifMaMLHhA74iSaGQmI9cLQf8d_kx3Uj1RZaufuYiLQZEOLgKgQEQryLmPjDS1hQi3RShukQZ7_wjDwZ6ZijgCHNatQ_MDjeQbcP9Tysr2yJh-G8xzdobbrigcfzNhDiF6vrjxML2O-g2gkFjubhaSgF66LIuL-WQbElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYnfPFsRRGpKzNNfc8YAodSzpW0H_a4thhaeJ_XXbdUtteXIyJye54Rvd0MhzD5SIhc_I_4ReovGtP9fdpMdQG_T6SXAOJCSQhJDXf0FPepfXTQTuIdkaVtZkgyFia6jPmu_zSkL2siOFaRRmhMX0IRz5Wq9itjlC4FyOVDD4LGYiiEu-hXgZ6xEDzhObUaQRsYEjIieVIZmSY8oPHs9FUt3SXTII_D-bFZWAZiXWxSSorVS4e_K6MO042IcPNZznsnbIa07XJvLMYhdT_HWMSnRNGgbFbXLsvzNsehd8J1UdkbieK68wEqaWYsUzoYsNArgmdkkh1KGcgOSLSoUVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGDpQYbsRnHcRhiuLK-CHbGv71MFTGG5GPZFl2r3elL4oKOtw-pv9Tvnisyu_tgGOmHwRc-GEKsZfk60emItmd4mipuwhF2CADw4GzXrr18Qlorbg-vgCyJyee973YEmvBD8D3QidZo5AI7rRGyE-_Ey1Dj08pGUu3CJyu7AtKX_q__8l954K5B5H5GQwtScfyCuq9nFb3X5YqD4tVmL1oFz8oqmg_EWueYBcptR_I0t-ZnSENUAa6XmO9UTIh_wWt0JDReInQVcx7uMKS8GPQRJos-TmaSqySb7dOjyU-fqnA-FOAJHGXHBqdR_U6HtoMfL_uYIWn4-azMK-2W-Dw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pnzq-SJCeK5iUsRqrtzeIl9PiPEA8q3oSzYdnbVRLY80icvC_4LTQciHrnV9pRKte7WeyE-jBbb7S46Bhhx8Tuf25UUn-H8UrM2QSzbH9tgN7ATXL_hE8NlfaCv8jXLQ-QZlxogfOW5npf4VGrKBt4wovK8rC7H3y4Aak66zjJteOhkmZQGcBL0iyKnTau4tjoTyYssEh_wu5vzDhg_G47-vDe4dl1y58G3MUmn-zfxX0DCeTHV6yT4SSVYNg9lOZM0NYQxG1q3YwJpqAgiFwQ6A0qSXw5dtPjrVLT2DRu2pTeto4sAKY1rDdAdPhW5d20-XCq0zuWNuZ0o8rtW-jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhC4k_D4kmcdQPM9IDOw8K_CP0yk98ef_9pD6Y39DS8t3z1EJuxrb3lXtak3c-WtqOfvZDg_YVhllbUazxFUuv0nT4oTZIGpUeDz3ikbfM1lPqo8xAv_sXZhdEUe9aof3yHM6NjWIitFexg3Tlh5f7ABUGUfLvijJnSYHSL_Uz7ZeTgg6Ayvf-uVRtQeTL9k9OCp5N6typoqybHszwc9H7J-4gtripSmKWBV1G1Wa8srxHz_R7LDhbZPoYsKeNULYjqD2iYN_E4PLy85jVvOG6frjaKUk2yVSPQNzhtmmG4dut-KW4tdKI_7xuEoleSW2neuc2KjcGxGRpHHnavI6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9o7BERHRgLBKGOYB2iT0UiMQzMKTr7GSpl72-crHpNbnCnDgp_peCqxTtl85AsvzsycCKws8mz8f5CZmN-z3PE5XHklI5cH2HzpHZwyMocqRmeH0DSDeLKWxW6sdIoW6wjnO4y0CCyUyl5wBq7BXHQTISVR11aNNWRFkkOqPc78yB7QEQfTDPopVKLyKO0o0rHIBa0-gRPOldEri-PZpr7TtxNVlqxt4typMLURms6btmePEx-vwpyo0hpkFwFZJAhcsgBtHlsQme486IIWqzMJZqhDfzsUFOZp3VosB6Mupnf9XYRQvrNy9pCGW4jYJC0j6xSpj7K63fP011Xy9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjBG8hQuYl8uxJ8wSAxmyicbvrZETZMMQb2clG8PoDl5rBURI-xm3M8EV2gvqBNtCAlezPuBPvrHrG-HZS8laTyfHZdTZos18T-GdIWehTbNtm-bZ63r_DpMqLEzn6a61xEifaW2hhjJ7pzDZ6fIztX6mJE9xJqJuXCImMlqr-_aWYpJeXZzhLURp-fUfPoIAirEEOgLE7J9uLzTgBySkgudfwA76OsPmQ8gEs9Jiu0PscRNCtzaVBPIEXbHqglznn70fQ-zrMx3dja4mdXxIaTj5u2whGOZEFFWRj3kZcikj6ErcpDUWslx3b-vgR8fisVniGhC5yoS9YZlM42aUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRsa3taXDcJwZabYxlc_chq-LT5q-gq9o6eY3Kk3joe-Y5AQTCp8TfEpsuvJ2QWLtZLNMShtN0P6ufF0yYCsKgEWxwoxUwoUV7TJy6CR3T4z1bEfGuGX-P4sAi7vGdrxpljzjZybJN9aLa_k6PTb3uLc4M3ui3HAXqWvaTTPSNwkj-4AhCQff9aTqF8UaIdrsCsBLw-EwKGULbYq2ogJmYKNRJMprY9CmTKl_1Q2ZesioCayrdDBHAJwQqZ7uQtZ_ycoWjIF_KXxJ5SQpjWaVSDcVSlJCZEQQM_MnEBliS-gxxqmv597L02bGq4lPnKJwJ1z4Xtl1fuVAhLDunR0Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMb3dsDpGT6h2rRrzJWRmCY9Vt7Rm_Vo6-9S6741c3icQZzAs_IqrdqWPHawaAcf5u0z--0n1z2f0UsAfvKqscPifTfwXZlGySAcd-BlbMQLDU7bnTyjZwV0te4hB_kq0GVO8fOPoDe4Tz2z9zUwD7NWMsvY8Nypl014Eth-lCCjv4NBool5Oo3VPhdhGbSaeJLS3XMeyBHN7hQlalSfk3I1QuCDP9chILQk4zyNUkcVOO1Jhw3ngx1hf3tpKE7gw-QQUHxv4Nq06WW94XMOJNgPK9m3E4ko32K_4rfkMFQqC9qD35BuLAAq8qzXtShEoebierm095X2BfyWGhKRdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuKaNcPXgapA5Ly176tS1GRqF7zu_votDePfAuAxaAsirNioSuAy8yDcaQigVaWeDb5HrmLBhJWpK8-s_4d4GQIxwgJamj-tCUZK35mNC4cVkHWyoMu5ered6qP2i99X0VVDPVQ01Jyi4kvtfuM7Vus7y9qH7bD_GjJoC3VrtVE4qO_G87yoWBTiIfpXuMYUPnl7q1SY1KXa-QFsux34lfj82yrzpeJPXM9u2QbcJHg5bzLpfPKfN5d9VlynGS0d7NyT2gbuJndHf1-AJdVhs_w-vW1o-a9KriaN8pWjdc2cvU06j2Ke2gbDQJGxjsCUP78Ahe9PTDtQS9TyL0M27w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=L7oMq3jrADgDXsdbsGS8Sr41oi2lhdkBcOaoiBIJMuFWnX0DhRuGkgxARSnR3EmWLpzAAOQspqD_neDI2-VPmKNJPB4-bnex4NGEpIEjE2CdN1Q07oydJT6777eu8YdnB5JbffsKIl_afHZB-MyaHHjCQYhADLeqUjiVEEodB5rEDY4z9HQuR4n7aON3QNsfWZ7tLqzn8B0OueYBQweUyyg1-u8QlsOKwuq6VcjReoR_ffhgfcojAChfOOptlmen3cYykU6IwrHBocJu7Eu7PuM-Qkx-BdwZo7rQIZspsmvAIcqJ3EBAeqOPewM2aW6mw3ikBHUTtjPLsAcDTnBKlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=L7oMq3jrADgDXsdbsGS8Sr41oi2lhdkBcOaoiBIJMuFWnX0DhRuGkgxARSnR3EmWLpzAAOQspqD_neDI2-VPmKNJPB4-bnex4NGEpIEjE2CdN1Q07oydJT6777eu8YdnB5JbffsKIl_afHZB-MyaHHjCQYhADLeqUjiVEEodB5rEDY4z9HQuR4n7aON3QNsfWZ7tLqzn8B0OueYBQweUyyg1-u8QlsOKwuq6VcjReoR_ffhgfcojAChfOOptlmen3cYykU6IwrHBocJu7Eu7PuM-Qkx-BdwZo7rQIZspsmvAIcqJ3EBAeqOPewM2aW6mw3ikBHUTtjPLsAcDTnBKlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWpqEddvWeA4BoNp7gyTGgkFx6g3NX4dW-hZtrWb4K1Lgn8nZDDPrqKvuWKYB6xYAnUIhXoJ5x85uZDsG2MW0ocaJDfh58chK-nfhcYBT8SIM-s_Bbj3DcSTXkV2IVuiddpK-BES7skyC9nJ8im3MQWlM8AwaUAxQ72vbn4f_GZn63HuFrZnZXEYNkMoMKfZHxP2lSeLSdP6GHZliFhh0eOeiqAkdRZOtZYWNl-SfvRGt91kcT5eBJfHosQLGXoaiFiRYusEg3M5v56P5NIX5UOQB-0NqdMkwDSQMSlw9g_O-aSuA8U9hr8RI5LmU3PIMIfknLmId0t7pzDv6HoWZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=LcYz_im8RLjZe6EsLgmCgdvX5B6Mk2zCT_TxQ_FdQEgNRNpX7WimwxVTOLQW7uljleAjT-OH9nZYNLveD7yQHy8LkzSQdk4Xl13SmHenP4ohofjiLHR6llbhGTNs1Qpd2cyU77wqVwEEwZRcC8LDWitgIj3sAvcV6iLX9lTGkMaH6SRuCoeZjE_AiizFkiqo6DW1BDM-3acuhR4xTrcKBIKEaFjNVxBwqNafbAF2o_UvWJroYiTxisnjSjjiNyrDphKC9cT0yz-EcFw43JI5OORk2AYlyGQhftBJ3FWY7nPzrv5w6eiTSp1qepcu6LSBAwKuaq1yXg8ojNeubpwsWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=LcYz_im8RLjZe6EsLgmCgdvX5B6Mk2zCT_TxQ_FdQEgNRNpX7WimwxVTOLQW7uljleAjT-OH9nZYNLveD7yQHy8LkzSQdk4Xl13SmHenP4ohofjiLHR6llbhGTNs1Qpd2cyU77wqVwEEwZRcC8LDWitgIj3sAvcV6iLX9lTGkMaH6SRuCoeZjE_AiizFkiqo6DW1BDM-3acuhR4xTrcKBIKEaFjNVxBwqNafbAF2o_UvWJroYiTxisnjSjjiNyrDphKC9cT0yz-EcFw43JI5OORk2AYlyGQhftBJ3FWY7nPzrv5w6eiTSp1qepcu6LSBAwKuaq1yXg8ojNeubpwsWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=kDkWwqBkyX3PlguouobMT3JHWbKh_MMX-_VpW3VYkXgE_0Li4CMCCu53RzUXwkGiV5hojX4JhHOiIr1xcM1IJDa1aNHg2dy8yLBnO8IbTt7375MXFFj6f0N_nZrKN_cFW9bE4ZK2gtYkWlT2xkmlBZPMKCtx_SGgrdScR1OJfYZPo9bQa-nPU5NkGFOR6agHCquZ_c4kFNoUk0LrRo2qAs1IdcyTxOdkF4y0jjDaKeXwKfuzh7aHlBJjJResAWq_CyN0F3UMwTVaugZubVIAZnmDMRqG6CI8yJdk4KRFEo9nArvtdMizGStyuaWaSSWZidBhD_GY3f2d3NZVrWLb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=kDkWwqBkyX3PlguouobMT3JHWbKh_MMX-_VpW3VYkXgE_0Li4CMCCu53RzUXwkGiV5hojX4JhHOiIr1xcM1IJDa1aNHg2dy8yLBnO8IbTt7375MXFFj6f0N_nZrKN_cFW9bE4ZK2gtYkWlT2xkmlBZPMKCtx_SGgrdScR1OJfYZPo9bQa-nPU5NkGFOR6agHCquZ_c4kFNoUk0LrRo2qAs1IdcyTxOdkF4y0jjDaKeXwKfuzh7aHlBJjJResAWq_CyN0F3UMwTVaugZubVIAZnmDMRqG6CI8yJdk4KRFEo9nArvtdMizGStyuaWaSSWZidBhD_GY3f2d3NZVrWLb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEsBmeiYbfxZHQMP4ILHA4KlBSoA__9bI_PKs5hzcwIFkcD7SxUlPmJoCbGWYs8B3dVOZup2dBA3xTyh3ji_GDmxcPsm3eXQsdELRaxYhNoQgIvwifZTWMsCLKxC5oPzviEd0Lq6xQYuSsU91QGAW12R-FmnEju3i-yYi3QMvc1m1O9O7Pe35mJVAX4CvnnaDsfdu6ZqB7DWghRqWAbekGsLjsoGBm_xHPKuOdtQrl0AZ0--D20BJdWyQCMEFC3aiBWhiFS_oe1_13oj7zZI00TVuGpKCvSg5LtR6Ivt1ft1M5Gkb2RHUWyuAfUcbDy5Ob6XBnB58Fj4DzlgQ-g9PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=unpRnk7C7dEtavychLwlXxXLDJcBNY49AqIK8bT2wJX16ffKTyJpOcMqEedYetOscVq6m3uu8QY7bTWRiaIbEqXMAkcbzYanwlpwCZQnibo0IjEpRE_2IKx0NlZMeQXAX2x2Jyd2jVtpTbGN2dOkA5jXiO-Dw5FXgGxjvfQhrB1IFZcPNkDLJDbrlWXgtkL5OOuvXykYuBHCv1Mn5TF8vH6a76SYDjut7SHH1gX4zpWa8r1AxypH9FP8JaRGEMYLFtS1dJjE6cQJayZhMUXY3ytnvBMNIZwW0QgHYO88a1sygYwSanyBphZd0MfQKogdvWXAqagGpDEI8dn9e1VetA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=unpRnk7C7dEtavychLwlXxXLDJcBNY49AqIK8bT2wJX16ffKTyJpOcMqEedYetOscVq6m3uu8QY7bTWRiaIbEqXMAkcbzYanwlpwCZQnibo0IjEpRE_2IKx0NlZMeQXAX2x2Jyd2jVtpTbGN2dOkA5jXiO-Dw5FXgGxjvfQhrB1IFZcPNkDLJDbrlWXgtkL5OOuvXykYuBHCv1Mn5TF8vH6a76SYDjut7SHH1gX4zpWa8r1AxypH9FP8JaRGEMYLFtS1dJjE6cQJayZhMUXY3ytnvBMNIZwW0QgHYO88a1sygYwSanyBphZd0MfQKogdvWXAqagGpDEI8dn9e1VetA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRw51j86Yw3E3Qx2xquxf6FB04MqPzRzf5W8FnFdwEigFRJOaZvBP6wYGRr_DUBkvBBfcRHSXNrpSx6SAa-_-2NzB6404rdWMUwAxe2lG1PS-oBNgTgERIHlj-6SKQGzf35Gvj14RdjMl2GTj7x7aKMnFJw7iXRTUebLIt38Augf8QDDaHFBLDKHUFUrB4vtvYOpM00w57eherZbPmdAR93DiQ6ol27Xs3EYi4kgNx_AHB_74F-WT7eXlPObB3tlvGcJOxI_WO4lfv6IbqvrIyM62ypKQaVaPbyEUiJJlUwiDtDC_nCxQ7YuAduY2HAqoML3sdoc-oMuPca3kmQTBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_sWpYqSAPaSZdwMihhP2U_ZJNh1RjqJkGomCN8IgiVdpYORB2f0LPvr9qwEyOlZKqmTJzY7rQh1lVqSCxHKis9dj1FplTl4WnR4P3HV8kWU3SpltFlFmBqfhhueDYo73KteMqtgu1VTRMFPpEveYtP5a050SKWtykL-IFli5ogmvXrW_XnXtI3hAjI_qEzIXcIfRbTeomgBrjxR2S2NX7i2zelzZriJINHl4N8U0Gl8QAgQh2vWax4ZSniO2DvFm00WLIKXlF40hiqtq9zQHdJtyhbU8f-eO1-ihnR2rNFLLS02WwNnrOslmIOZ6NnOFKk4a3VXFGUMUg4KLAhNVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GigooWZOUwVylCvg48BlBDZd4dl8vTfVYBhtRMVDyGWlsKSeIFylMUaTOorS8nrnd79Yu75NqMy55dkgAHyzOC0iKyoNQPvLn-Ni0dpKEtVH-K4o_jhMXXjcyiJuHnvUQ28FZrCFSWV4oUY4L3JhlHlgeoc669vcYpo-Bpf8AOS18y7KFu4AdEc-RUm3HxicwWfcgSWWHX8Ssrx5W7qSpsMfE8tRQG1TW_PcGcCyPGoL1Gf6Z137Me7OyHSr1HDwVzpeClIgr0l9wZxdKlG65JdZ3qEbJ7v6ffhaJx8LJhcqYSycUpKokdcMuxicfNgUpi2dVnikPM00gYcAIyA-Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYN7RgVDCojDKUOFU57rT979MXQwFQ_IijSjwoxfpdQi_Wwb0n3jVOr4o2rLIu-lO13YovPdjMTRll0ryfFPZa09mgRJ_A6yAWWmDdk-iQ_Dq-6b2jwWe7aJFtXat_IdfkpVEVY-K5521P0G5VLlNfxyfUpNUKTY_5xbN3riG9erOMwQ8bEzyjoBPOkw6qxdE-YnXoFdTdrHQumj9lzgbFCaTsIoUjcNqni5O82atOj5krgHLP7RW2Gx-PAvPACTERWOQTCqMH6yHyHfxL9HLglGeNEzKlTz-xBt__2S9zaVGHg3HntO2GSv5mT2r7QgAvY2fHsnrbZpNHAJhNsqnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=hh96JVus4lm2U6a9VQk4hiKGuEFentmpCTZZ-FgKHGtyV2jlOdvYlpeZJF24krM_C2O0fT6Ixv9RECBS_uiXTzWSS70tHdd1NN5Z-YW3o51X0G1hyFMsuB_wDwf1h-yqDsX-3J6WU_6ArMbx9qE-WzTGtVwWtaU_pXuBErLxBzNJlGSdN6HZfU7AmBT5hLYmATBFxoR2zPGzbj8n-hI8mFqueDjFJf6u-CkjwGcaGGPS4OJDaJwizwUEfpjYfNHNAVAV2uHpm4VK3MdMClwZ11IDvbCjy9sQPHrIDtFYJ7Vz__pXlYItuXvqlMMkC-_W9mMfkHfUFV_6o3qpsqqyZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=hh96JVus4lm2U6a9VQk4hiKGuEFentmpCTZZ-FgKHGtyV2jlOdvYlpeZJF24krM_C2O0fT6Ixv9RECBS_uiXTzWSS70tHdd1NN5Z-YW3o51X0G1hyFMsuB_wDwf1h-yqDsX-3J6WU_6ArMbx9qE-WzTGtVwWtaU_pXuBErLxBzNJlGSdN6HZfU7AmBT5hLYmATBFxoR2zPGzbj8n-hI8mFqueDjFJf6u-CkjwGcaGGPS4OJDaJwizwUEfpjYfNHNAVAV2uHpm4VK3MdMClwZ11IDvbCjy9sQPHrIDtFYJ7Vz__pXlYItuXvqlMMkC-_W9mMfkHfUFV_6o3qpsqqyZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=PSr6-vyGhs6xbovQack86EqCeCMOOvrordO3aFNusdI53T1ylaIAC9trXzfMGVq_vgngwQ-dXpiyPD5zgrNZOMZizZhMjwQlPXeCs-NyuM80EErPeLb2WCOpvTFAEoDsJs2gaut6MfdJPrdMb-Q8bLci_b88aCeo2Rel2waNioZDqVFTK7VsYbgUz1f0-eaHY9fwinnfZGAGT_EYrv50ISCkpEI8-WJdOU1jNflwzeioieFAnYMeJr9-cx6FsviP-0zDnrWoWDB5PZykgECrqpjOQTQH7EYQDx5di7ibgyduLODKbWnCluBff7XM1KoKEEivLobVWZlFepfz7TmYrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=PSr6-vyGhs6xbovQack86EqCeCMOOvrordO3aFNusdI53T1ylaIAC9trXzfMGVq_vgngwQ-dXpiyPD5zgrNZOMZizZhMjwQlPXeCs-NyuM80EErPeLb2WCOpvTFAEoDsJs2gaut6MfdJPrdMb-Q8bLci_b88aCeo2Rel2waNioZDqVFTK7VsYbgUz1f0-eaHY9fwinnfZGAGT_EYrv50ISCkpEI8-WJdOU1jNflwzeioieFAnYMeJr9-cx6FsviP-0zDnrWoWDB5PZykgECrqpjOQTQH7EYQDx5di7ibgyduLODKbWnCluBff7XM1KoKEEivLobVWZlFepfz7TmYrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=qWU5aKmTO6MEwO8YFLU8RGYqXFNyQRg5sieQtCM1Pvs4N2Sqhrm_q1kEC8YVvU6lHaYcAg1LapsayvhCHY3_XMYIoLrarvO77R_2KcWf9CEvxianpzMc-kEvDtd3acu8lmPit45pxOn3WJvZTHb98dowDc2ikSgpggbXcAoqAjcYeYgQqV33PKlRqBd1ovU5ZbM7XIfBtVZXAvDTQQpsIbJGXTLay1BAw_Z6jGj-JHmIxaFDcIw6hWz00EdSl9RGlAr5UHzG_eLWyslZfh6TXJrZ71kgO_2iBk6b3oZ7MVLZGmnauBzMAqjzBG6bemg2Co00PH-DxYHLsCE12FDpOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=qWU5aKmTO6MEwO8YFLU8RGYqXFNyQRg5sieQtCM1Pvs4N2Sqhrm_q1kEC8YVvU6lHaYcAg1LapsayvhCHY3_XMYIoLrarvO77R_2KcWf9CEvxianpzMc-kEvDtd3acu8lmPit45pxOn3WJvZTHb98dowDc2ikSgpggbXcAoqAjcYeYgQqV33PKlRqBd1ovU5ZbM7XIfBtVZXAvDTQQpsIbJGXTLay1BAw_Z6jGj-JHmIxaFDcIw6hWz00EdSl9RGlAr5UHzG_eLWyslZfh6TXJrZ71kgO_2iBk6b3oZ7MVLZGmnauBzMAqjzBG6bemg2Co00PH-DxYHLsCE12FDpOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=uPVW0f1WDthgmT54RlAK0GeKWArOBG36Gmp45XTwnSBjVjDFo7dcmkPDC55Do7q1p0K2-OzW-w8obUGs6sVw3qc7wygRypEedjk2W5RZNErdCW4Miyp3uC4aSKi0y9NjiBSWeqfWDSM1aiPy3TcuEa_icGJbhSsgCBzYC-LDbprKusjo0uiY9HVTdMXjSnsxkWtHpKevumXlJ8_Z-TRfZ-b25TauCTvjEfGuQR1zgHdtcbdhi0XxSg7u2Px43FsulcOUtM9WvbpQY8FZFQyh1sNQ08XTk1etbSjvGnLhe50lRODAM2qXrvfO4uAz7w7VEYVmPUc-34mJv4WGqovvB5E-76H8KQPDBOJLB-2G8jvZkKSpRgDEwPsbuL4a5ULJrStJOkuXNYVOe6HqlpVxX459vfrjnWkanJckcXwTsPu9CeiLG-Vc5JVULmUfmIh00kGnjS1P19ZD8a31VnVEEZc2YuuGYhB7X9WwBwhoOY-_kphULnCfzQlygZAgj6rKjCqxG9ZQIT_-VBddPwi_FaLdkviIZxtWIBKdCVjpmRVb06UyAnTAAngBCsRjDHm8m3KTd-LgBVV4700dmkFtk2oJSf178biBe5sVzTcliE6Zctrr7i5JoLRxW45LFzgztK2EfCKwhXt7uDSqzATochIVAfTuq9RUYqbbnBEDOVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=uPVW0f1WDthgmT54RlAK0GeKWArOBG36Gmp45XTwnSBjVjDFo7dcmkPDC55Do7q1p0K2-OzW-w8obUGs6sVw3qc7wygRypEedjk2W5RZNErdCW4Miyp3uC4aSKi0y9NjiBSWeqfWDSM1aiPy3TcuEa_icGJbhSsgCBzYC-LDbprKusjo0uiY9HVTdMXjSnsxkWtHpKevumXlJ8_Z-TRfZ-b25TauCTvjEfGuQR1zgHdtcbdhi0XxSg7u2Px43FsulcOUtM9WvbpQY8FZFQyh1sNQ08XTk1etbSjvGnLhe50lRODAM2qXrvfO4uAz7w7VEYVmPUc-34mJv4WGqovvB5E-76H8KQPDBOJLB-2G8jvZkKSpRgDEwPsbuL4a5ULJrStJOkuXNYVOe6HqlpVxX459vfrjnWkanJckcXwTsPu9CeiLG-Vc5JVULmUfmIh00kGnjS1P19ZD8a31VnVEEZc2YuuGYhB7X9WwBwhoOY-_kphULnCfzQlygZAgj6rKjCqxG9ZQIT_-VBddPwi_FaLdkviIZxtWIBKdCVjpmRVb06UyAnTAAngBCsRjDHm8m3KTd-LgBVV4700dmkFtk2oJSf178biBe5sVzTcliE6Zctrr7i5JoLRxW45LFzgztK2EfCKwhXt7uDSqzATochIVAfTuq9RUYqbbnBEDOVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=mU4fZXZYn1KhnB0ZeW6C-vJO29vF59J7rP1ze74WjhKVvDobakQ4btBuzKFshKcjAYIDnBLyfpgOHSjEL3OH61DlUl5isd1-YSr9EKkcFObuXFFK49yVkfCZDCobTWoj2RYBvNIy9yxgHVsHzzWzo4RhVWjiW_YHoDXPjALPZahLfHpaR8UUUKzkg-UBZpJci-YT9sCf9DREZIYGf3pV4dFQSIxRAazNIUQKGpQuaTVMA1JcJjBinDIpEh6zkOjepp-hsXajoJIcRL_ATZKjr9GLODDvPek-rcdTje5MCKfIglyag4sIcUTAWFSX9z5q03NUUaYDW_OiN3WTOT62fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=mU4fZXZYn1KhnB0ZeW6C-vJO29vF59J7rP1ze74WjhKVvDobakQ4btBuzKFshKcjAYIDnBLyfpgOHSjEL3OH61DlUl5isd1-YSr9EKkcFObuXFFK49yVkfCZDCobTWoj2RYBvNIy9yxgHVsHzzWzo4RhVWjiW_YHoDXPjALPZahLfHpaR8UUUKzkg-UBZpJci-YT9sCf9DREZIYGf3pV4dFQSIxRAazNIUQKGpQuaTVMA1JcJjBinDIpEh6zkOjepp-hsXajoJIcRL_ATZKjr9GLODDvPek-rcdTje5MCKfIglyag4sIcUTAWFSX9z5q03NUUaYDW_OiN3WTOT62fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=A4D5BUFOx2gWTmsCmI_BfkF8NSSFfeUGHK0dUdPGdyg9cWEHpaEQR_v5j28YuUHO2nc6lKS9im01pLbvuqcEHd5pAL8N2B9lc9iSDYGLryn5986qdqiwilnh4ifmjmSCM-9l4qZWOe5a2eGDR-tSWS1GfLDJFWrY8IwYN6UUzdu6sUdkoFaNUJBAvz5Ita_ZU-yXSyT3hRVN6Hn9kbPZSSb8Pt_808wG9-MwL-fUiIWPcRfsnQE71KGd_0Au3RDffPMMoJ835cOBZXCvXjV45QYBZyvdC31Qp_CrLCZ6DECjheuiwq5Ma-_7fJoJ1aCMF5cUS9iYpWZToEtVNskAkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=A4D5BUFOx2gWTmsCmI_BfkF8NSSFfeUGHK0dUdPGdyg9cWEHpaEQR_v5j28YuUHO2nc6lKS9im01pLbvuqcEHd5pAL8N2B9lc9iSDYGLryn5986qdqiwilnh4ifmjmSCM-9l4qZWOe5a2eGDR-tSWS1GfLDJFWrY8IwYN6UUzdu6sUdkoFaNUJBAvz5Ita_ZU-yXSyT3hRVN6Hn9kbPZSSb8Pt_808wG9-MwL-fUiIWPcRfsnQE71KGd_0Au3RDffPMMoJ835cOBZXCvXjV45QYBZyvdC31Qp_CrLCZ6DECjheuiwq5Ma-_7fJoJ1aCMF5cUS9iYpWZToEtVNskAkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIlJJwzKohTGz5c4Fr5d3doscKUXvRn6puV8_1Wc2b11ciqctgB9MYX9cyGBMNluSAUxVK3G3twcJDFiYRxYUAIGmGRHApngnMvniiCK5430IktwGiSawwrzrsMDkeskfOdb0zQ5ZnSEoA63jpMo2zGWWMVF8pynDSNHPaWcIGRNI0VQWMW1Fu5rRF7G57W1FcCYz_f0szuBOLJ78EqZ-UN8vy65wlrEM6DFte2lZgu6pEdMtS4Xp-Am0776BxW9KE5gtT-ydlARcNsj_9MsXOylNm46kGGXW5Y3liytsGntQHKMl1BpwfMZRvZbtIP9KrBdCL_R-IK1VGbNU_RMtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=czE5BAkJFgy_f7ffvTw8yqCga7AJj1ly3HqR5kz9X_0U736qVyS2wudzGIi5PKmcNOMZILbcgsqYhZwYLPZP6jh-Ovh0EIx5gbTmdA9IEmhtbAtIRaShWgOWDd0zGrzG3GMl8mDnR_rl0sJ3EkEJJe_O6lWGcJDn8EkmBYZ31fp6u2_F0X3m3MujHjIij-yyUTaNZpeg3qtkR18dn1iSLUifbGS4I12z7DGIPU7gvCGXM0udhCmPj0uhdSWL6rA3jLw-5eENySdRi0fmKrrrxmDO1mbeIyLZusP7posjLz8l3-68FtKg-KoDhFm9Lg1nGzC8Bxby9vRsip0tuE3Npg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=czE5BAkJFgy_f7ffvTw8yqCga7AJj1ly3HqR5kz9X_0U736qVyS2wudzGIi5PKmcNOMZILbcgsqYhZwYLPZP6jh-Ovh0EIx5gbTmdA9IEmhtbAtIRaShWgOWDd0zGrzG3GMl8mDnR_rl0sJ3EkEJJe_O6lWGcJDn8EkmBYZ31fp6u2_F0X3m3MujHjIij-yyUTaNZpeg3qtkR18dn1iSLUifbGS4I12z7DGIPU7gvCGXM0udhCmPj0uhdSWL6rA3jLw-5eENySdRi0fmKrrrxmDO1mbeIyLZusP7posjLz8l3-68FtKg-KoDhFm9Lg1nGzC8Bxby9vRsip0tuE3Npg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igsLaJ28vTqMQzBGqKSXyltm1iWxiYkRwrcSTKW2qv90rStbAlJVFKWHM7fwDoP7IfrszpFODfkrc6nIXeMlydksoDf8B22s_uO74ao_gWSOzL9WuqY8cke-9azMDeGrugz_dz8x1s-mKMRP6sMnijAc7Z3qGHZYuj2PkeZiRP1r5sgOXI4qLhhgW8Bi2hYrzLq4eD2vniqMHJxSMY0QU_hBotGUyMfETlWHOepT_XTwQf3OynuKhgqD26MRliv-v_nFr0pbARq7GjLOHcv-YXsaqGA0I9bDxDSF0DCs_k4WqimjTklQf_Sbz8UolNbGHNqFYWGf3B9_jYOP7x3UKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQe8UCukHpS7MMAoU4BhXlsx6tQdVXXlGCKWwgSZBMbxbyp1ynUFOMjU73Vm0aMbj62y34faPhSeIxpFZ0yk-ZUoPvx9xNURTtgZBnNgl9JpnTm8RDWtXsESNsRMfkTsS8TTQY_7oiQ7kiV4XwWmFpcyyzTjg2lgASooi_grKENQO7q1aOcybGk2QeQ16_B21Akb1xnQRj2ZT_eqbIL36BUy9JUDlHNFXjuziJtxUZdO1JrqNwOL6VBaE7ddujmmVjyHAubR_rccPq0tXbj1Fehymv4Ed4Sq9I6o9h1giU9MNq1tMqRjKDsKCgrMHJeVKbj21Ng9lX42WGxkLYIHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=Zpoe-LBb3MyO0r_jyA_TMbmGq2_xACTe2p-uehIIPRf4jzHSLAOVNmFYkE_PJ6keuT_uNLZGp2oIN2-jz6GnAmj52f7K9Tuh55M2QtHIB1oVovG33xu8ocHtX00Xd_SmGD3V773nJF9oRBH8NJZQyNXaivg0MxEZhjYCExcmkoUW79VU3N4KdRUYM1_dQyZ22FNZWpTZk0hd0xVhrMw3M6BzA4fqXxaK0-TnFsmR7Una8562jGvDGcO5ox7LsJbpHX6kEq-wP_vvt0sGHbSf8nkOQWakElh_6nkp4VKfNl1UOk8qZQ-jk5Oo1mbek0DSNvzjRwpMoYZFVQz3tEi9UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=Zpoe-LBb3MyO0r_jyA_TMbmGq2_xACTe2p-uehIIPRf4jzHSLAOVNmFYkE_PJ6keuT_uNLZGp2oIN2-jz6GnAmj52f7K9Tuh55M2QtHIB1oVovG33xu8ocHtX00Xd_SmGD3V773nJF9oRBH8NJZQyNXaivg0MxEZhjYCExcmkoUW79VU3N4KdRUYM1_dQyZ22FNZWpTZk0hd0xVhrMw3M6BzA4fqXxaK0-TnFsmR7Una8562jGvDGcO5ox7LsJbpHX6kEq-wP_vvt0sGHbSf8nkOQWakElh_6nkp4VKfNl1UOk8qZQ-jk5Oo1mbek0DSNvzjRwpMoYZFVQz3tEi9UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=LSWkXi9py-6ui9R1y3zD81A3mWw-vzDstkvno-GdRQG4VVE7Tefp7TMa8Aa1pbon_suMxVoDolpFxYfDlwRwgm3TgDQAQ_asp0DILK7zgKVXVeYlfjtv17dLUGJgeroiFkANqCdxGb9p-zIB-Gm7vS7oWRNYoSxAncHmOh3zE4t7ms3dHaUplIY9Q4PdeivfOCHCwSZ1yYFFJTWvfjNDWfBepG2UkYCRWCR7MF441I-49lCCdWajyltbvue7FW7ECT9J0UcG3TvgZrqwry75wz70K7XvOLslc1MA2DL7ybZTGJRxZUSoYJxih9L0UlaLQVk1kWDfn9Q6J3uExw1m0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=LSWkXi9py-6ui9R1y3zD81A3mWw-vzDstkvno-GdRQG4VVE7Tefp7TMa8Aa1pbon_suMxVoDolpFxYfDlwRwgm3TgDQAQ_asp0DILK7zgKVXVeYlfjtv17dLUGJgeroiFkANqCdxGb9p-zIB-Gm7vS7oWRNYoSxAncHmOh3zE4t7ms3dHaUplIY9Q4PdeivfOCHCwSZ1yYFFJTWvfjNDWfBepG2UkYCRWCR7MF441I-49lCCdWajyltbvue7FW7ECT9J0UcG3TvgZrqwry75wz70K7XvOLslc1MA2DL7ybZTGJRxZUSoYJxih9L0UlaLQVk1kWDfn9Q6J3uExw1m0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=MPBRZIyk15WM8rswUPtwR7w7vjBmAzu252Xbb-Hf65euQr_y3bNYjY0uGMWgCKjlgkgPkQ4zRXwojNywn1GmdKffwh1F3Q4Ir_9FxRfQnCmkkRTSxABLZTdOAnqmYMg_9s-8OjuQaSU3wCzEJMINoA-3zLB-nCqlxaSeUzaOqXIRsawBLqOPfsPRGv36j3busgmq0pM0ny6waJxxCEeV8qXp8t6vrK0GY7KDzLD575n5kVvhw-nrUKAyt8HgE0Mi6N42eHIhdjvzu6sLp7XhDEMCTRsJZy5C5uxduRIC0Rd6H1heFBlk2vgjSlgMSWgJ-fxGYCQRIxDx8TZLxpgY-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=MPBRZIyk15WM8rswUPtwR7w7vjBmAzu252Xbb-Hf65euQr_y3bNYjY0uGMWgCKjlgkgPkQ4zRXwojNywn1GmdKffwh1F3Q4Ir_9FxRfQnCmkkRTSxABLZTdOAnqmYMg_9s-8OjuQaSU3wCzEJMINoA-3zLB-nCqlxaSeUzaOqXIRsawBLqOPfsPRGv36j3busgmq0pM0ny6waJxxCEeV8qXp8t6vrK0GY7KDzLD575n5kVvhw-nrUKAyt8HgE0Mi6N42eHIhdjvzu6sLp7XhDEMCTRsJZy5C5uxduRIC0Rd6H1heFBlk2vgjSlgMSWgJ-fxGYCQRIxDx8TZLxpgY-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVWUHhWa95EUKGsRfBkvay13o_sjFl0bgLpGfRNyCmi4FEOBAk4-SyNfNedCWNsdzVT_F8kOn_6h0STw9fMmS88YxoBzSP2Kbqsegc8lF0v2__WyM22qP1VMBwFQaTuiXr8cYrMFmfS-tfbuRkenTaPwhF207AzsKICLps-lx1m25TIA_gdhroHQJBSyHeimW5U-Wh7HhAaqs0HTe1prF8gJcRaXrXewKV2bLV9EbrwcDbuTkFjsc4EQpeu2poRm0E6-9lN9N8yidqvFoeRlCMd96-JXLYm4v4LV0vGARQP9gouGnuTV3Yje-JLn3ANH3jDkxo53rXfUwa7MAcfbCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=NRvGs0RsP0dwwn6xs6cK91TTVfB4vHyPA7VhPodINgv0R1oFFakEolz1j11vm0e3hwjVHSt4BwiniW1uEHcQ6xnKnwh48EDgkewjob9C7pTM0hLSK-N4p0tMtlVmSCqgGSjU6cLQEFGDUqFet1JiURrqMrpJMg5kjvo3oUweakAuKP8Vm25p1sTVV12VHH3a6Jl4swiStohx1UZDTSKjZIckYCZ3yCz78S44Zu0vZ0qrF5TuAFZRwSpPK_YriX4RultFutc_1ovT644d7H8hTphUCqc1q1Hc64Mc8Xe6h39oSjibt64g39FfCD7kIew0dB1WzSgMw_0q_cUMNi-Z-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=NRvGs0RsP0dwwn6xs6cK91TTVfB4vHyPA7VhPodINgv0R1oFFakEolz1j11vm0e3hwjVHSt4BwiniW1uEHcQ6xnKnwh48EDgkewjob9C7pTM0hLSK-N4p0tMtlVmSCqgGSjU6cLQEFGDUqFet1JiURrqMrpJMg5kjvo3oUweakAuKP8Vm25p1sTVV12VHH3a6Jl4swiStohx1UZDTSKjZIckYCZ3yCz78S44Zu0vZ0qrF5TuAFZRwSpPK_YriX4RultFutc_1ovT644d7H8hTphUCqc1q1Hc64Mc8Xe6h39oSjibt64g39FfCD7kIew0dB1WzSgMw_0q_cUMNi-Z-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=baJxzIZJyikpaQKnqpLMUkysvEheXiU398tKMO-1cm-AsJWkEovmnlvhUO_a8hIz7l7B24sf_Pml8MgZcY5wTXjN9SYWgryb_WI9Vt2qBjpj6v6RDzI2cOlua7qS5S2eR4bSLtgWQCnQJo36qk0TBODs49ZukdfDOnqUANVpqfle0O9TdVtiwe86m1N5tyT8U22WAsUc8XtIJ6BKCbwxaU7YynvKTaLvXzo0pi70h7i9CbBczvslV7JpU91EFMhqhgfAirvB65IkfXsHQsq3TnNxUgVJL0VWQm72Arpv0vzEz1tdOoEXh0dQs_pNL5LHFZF6DVdP43W5WxaqDJtmog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=baJxzIZJyikpaQKnqpLMUkysvEheXiU398tKMO-1cm-AsJWkEovmnlvhUO_a8hIz7l7B24sf_Pml8MgZcY5wTXjN9SYWgryb_WI9Vt2qBjpj6v6RDzI2cOlua7qS5S2eR4bSLtgWQCnQJo36qk0TBODs49ZukdfDOnqUANVpqfle0O9TdVtiwe86m1N5tyT8U22WAsUc8XtIJ6BKCbwxaU7YynvKTaLvXzo0pi70h7i9CbBczvslV7JpU91EFMhqhgfAirvB65IkfXsHQsq3TnNxUgVJL0VWQm72Arpv0vzEz1tdOoEXh0dQs_pNL5LHFZF6DVdP43W5WxaqDJtmog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=RgpT_xANtEWPYfI4qjnFffa8PaSoDtRUPj2Ez1T1VfUqbO25Yzd8S1pzgOBRrKSTGqJX4cZS3t9yMqZZKAjnOUQLkY-mB70aHJ3XVkmX0V380iddzjQLFobaP984sOAxWgdtpAVWsY6J_4aTse_VM8h_2dOrvZKOi6EaFppZ6myArw5SfYe1bsrzBJO1FVLliBTk_c_e8Mkk0FnGFSjN8qP_cyiConHm_gEBfruIjtqEHi_9tYuBS_dqTYpm43hGMzYW1ZnVsSMnEuQXbXwhsYt_ADCV0kgqZ9UPhSu4waAZZ1Jd5cCzoIAq6S_F6Vl2Kc6wo_6zl3VCjgNyaiil6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=RgpT_xANtEWPYfI4qjnFffa8PaSoDtRUPj2Ez1T1VfUqbO25Yzd8S1pzgOBRrKSTGqJX4cZS3t9yMqZZKAjnOUQLkY-mB70aHJ3XVkmX0V380iddzjQLFobaP984sOAxWgdtpAVWsY6J_4aTse_VM8h_2dOrvZKOi6EaFppZ6myArw5SfYe1bsrzBJO1FVLliBTk_c_e8Mkk0FnGFSjN8qP_cyiConHm_gEBfruIjtqEHi_9tYuBS_dqTYpm43hGMzYW1ZnVsSMnEuQXbXwhsYt_ADCV0kgqZ9UPhSu4waAZZ1Jd5cCzoIAq6S_F6Vl2Kc6wo_6zl3VCjgNyaiil6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ea-tgcVwxr9vWjmdUTvzXaJXvQV4fbTVC7YijmHWS9LATDuyXmLF0swg7SKQMwygvzGe7yjvpaycNgD2rZy6jlrnAZ-hYLYP6G87QqFaQmx-_FkKMUOiXyqIyEyaP0V07wP-JQarxu5Pqv68BrZU2iupFTtAAht_Qg9DAvx2dTFlPX5Ghxb6THvjqiYrDE8AH4B2i_ynfOihF-Vk9sqc3xxMgiOGP_IhvVYyODYUAwTKKIEgMcU55Sg9UhxGWycCH5SnfUaSarMhlKDSghRFpZX3HhYMZ7IrxU_fmXn9OmVIbJ5GBIaaiVLFdJRa56u6dpcczGkI9Xd5BaYjTsuVKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=fhXGOD5y87M3LmP_GWqmsko3qzcx1C0_sNveIP7xe5fAuj9xJ2r7aZhLLoZRtwNBQ4FuxJxdgMeBS-99jEfX_3h1LbvifQnzvheKzD_v1TzZJV5JYn5ssGiKflxXEQmtnC6XrbuNdbAgJ0VWZ-p409P3kQKU3WzTU3tFGovT8mc1AeTmbI8Ng98ondgcRHQdyKj0n_9REea42LT0ENm5FZrM_WwcMajkkqMdysqMgVnWe-ug5E3j1GuY9cOpbTeNwVNsbZ-lAgf_oSBYepylSHRxResS8glcub2RIefzD1hjaMWXF66IbdesmfIAK9zaBAO_umewzd8teticcTTm8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=fhXGOD5y87M3LmP_GWqmsko3qzcx1C0_sNveIP7xe5fAuj9xJ2r7aZhLLoZRtwNBQ4FuxJxdgMeBS-99jEfX_3h1LbvifQnzvheKzD_v1TzZJV5JYn5ssGiKflxXEQmtnC6XrbuNdbAgJ0VWZ-p409P3kQKU3WzTU3tFGovT8mc1AeTmbI8Ng98ondgcRHQdyKj0n_9REea42LT0ENm5FZrM_WwcMajkkqMdysqMgVnWe-ug5E3j1GuY9cOpbTeNwVNsbZ-lAgf_oSBYepylSHRxResS8glcub2RIefzD1hjaMWXF66IbdesmfIAK9zaBAO_umewzd8teticcTTm8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Be6IoMBYddlCzmoCfL4iZC4GkmQS-_27ECdD1enOcZzVTknwPLlJLKgInhBrU6J3_Ghr-9C5T0lyt_3XTIVqtpvSohnPMu_faG-ebnKVKiQyRT0MRMYki719DSW2l1HpQj56i3yhhKazk3Ac6pL9TV1z6MmXWUsPtuB7QFF8bLsuwi2xyGDCkkAVmC1lvto3Pc19rEZoOGyN0xGOtCQRkC4oZj8d-3thrT9GNlZbG7xYkPoSf52U1Wum0DTJLzpMN-_-fOb3f7CVyq_Nf7KIYxS9vwOEFSF_-7dByLZwT60QWs7q3TBClW3lWkrlqcetuCkmUgVHWm52iRaS7XRYtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=n8dH7o00Q6gWBThndHpfTC_ALbWrlAbZldvkL0QRF90C6bM6Yle0yTqxMNn6LD0GxFdXxV3koBIQCRDPCOf9KDy60GxbniR8qNSGe2bBQImfUikb6EhlPA0wW14EgM8eLYfv897BgR1zpLjAZymHYTjZcOGwlAcEzcpqP6pBkYWYFbNRQ0Owf3Ame1bMRrd_XwYthO1INRQTPPC11L5n8GUKTORZIGsDcQVHRDsQMCTCRcuTklxD7uzlLK1IsBopy47IoojqZUxaX9J-5GGQ-niSBjdrwbOUF7A1E11nTLG_xz2lIDflmoXwGib548v-S2D0LCwB80EThIW8cxWZUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=n8dH7o00Q6gWBThndHpfTC_ALbWrlAbZldvkL0QRF90C6bM6Yle0yTqxMNn6LD0GxFdXxV3koBIQCRDPCOf9KDy60GxbniR8qNSGe2bBQImfUikb6EhlPA0wW14EgM8eLYfv897BgR1zpLjAZymHYTjZcOGwlAcEzcpqP6pBkYWYFbNRQ0Owf3Ame1bMRrd_XwYthO1INRQTPPC11L5n8GUKTORZIGsDcQVHRDsQMCTCRcuTklxD7uzlLK1IsBopy47IoojqZUxaX9J-5GGQ-niSBjdrwbOUF7A1E11nTLG_xz2lIDflmoXwGib548v-S2D0LCwB80EThIW8cxWZUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Snj76cwJCjB39MHOKh_XkRoFeLXKtqG0PMhVQFlajUGRp1ON3eUiVeBNMgn58Oync_GFCcHJhjS0u4iZvHiXnd24COAW-f0dPT2-HGhAoXec-_03vebaqlIk_y-FvpkBIFIKpeG_Nje0J5OJ3MXfvMFcYwWlBbUzmgomMCgvihcb-gqYmqq6PlxHqOoq9XvGpWYZLSwiJfnhIiaN04xlcjFhEBjn_tlZy8B06CLxkORPI3Jwln6e-jJh6pxWzKqoI9A9vT3swkpa3cU4hDHKZGTk0_Lqq4aOwxtcj4-5l3nBytyZcpx-zokPnwIPVRjFIgT8OHA91qXaIHRIjtSiYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=TepzPbNfOS3lT0klyAKGba_inguz_ZsOZdAfG9TEJDOPf4nbZwKBfBpahaEGHm8rAGt08lEUJvf1pPFnYLz8-QMoMqAI_oW6a8jqCyxowXl-JL_G2nz1NmagXigwQbxAvxxrF8SdBoNvrpbdkuOtGs9o4jerUXqEwY_G1kOvxf2EsMbI38k4vKqnLeLSP1H_8WSEoVRmXzoEzd5ejkbJ5nGG4KY5R2VANWVCjqM-9GqNAfI6ZGHzpjJ1ye_GVSuXjJL_lrPIg2s0uD-DLxI30J2WCUWxDILr7gpNb0_XqlmoToksCeveSjyXxai2pLvKlrGNdgOc3p3CJtTK24wbnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=TepzPbNfOS3lT0klyAKGba_inguz_ZsOZdAfG9TEJDOPf4nbZwKBfBpahaEGHm8rAGt08lEUJvf1pPFnYLz8-QMoMqAI_oW6a8jqCyxowXl-JL_G2nz1NmagXigwQbxAvxxrF8SdBoNvrpbdkuOtGs9o4jerUXqEwY_G1kOvxf2EsMbI38k4vKqnLeLSP1H_8WSEoVRmXzoEzd5ejkbJ5nGG4KY5R2VANWVCjqM-9GqNAfI6ZGHzpjJ1ye_GVSuXjJL_lrPIg2s0uD-DLxI30J2WCUWxDILr7gpNb0_XqlmoToksCeveSjyXxai2pLvKlrGNdgOc3p3CJtTK24wbnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c--_Fku8PHKmQ1B4Z5lsOXfe1aXCOII_lrnySYN3_UQj75ZC09SRbRtx2JWek2LB754G6rwYB0D8sfJi0IAuqqW5AYQC5Sgspxe6h14dugiMlphgDskBH5oEZVDgyNpsuUiLo8jmvBRnt2NVUrMTUldGLMsbVtWP3N9nGB42HGvo5pJlywXhvjG3v58P4om9XpXfmMuktJ4Fz3K64TqAvodZ37RNvyZnl-F0c5pXp1Py4EQHKe8jbbkREIoRP_byVZ6nIWzvtV-s9FXr-6MXzOmUsiMWVNtMao8HrkLIkzVPBDZKFXoJ36Pa9SD9Ywa3_WRoevqqpQ4NneCrqkqnUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n_gxqVeoxGvSrwO80SsAknQ1xM7OQzczFonYBOQD5buQpy3G3yd1T8Vv6A9VIK_NM0YV2muKWYXZxMizm5FVUA_QxEp6TpaRwirw7XKDZ_jq-izTvP53VEBuqG5xdrtTP22M654uX_O8Xv_bySSBEnzqbTnaXOGi51_scY--CR12tgdFFfXaR_yUFKDydaxoh3oqFhL3wOEphiUocNeDlpCDcn_YoZbak2sqQSeDN-jKTNQ3xTKVXjEU1Ga7G2TtyzYJpvVYHoh3hxFikycRmizHgZ4DE-LPfgcag6TZnawboedEfMfBkTv-dt3kJQuR0bEXg_55xneISP2S1bAeqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=kuSrnUw-ehIVUIJdPa7-SZpbmou6lFDOblxSacgYFNO0hNtLQ99wXm3exLd-aTXkARMsOuWqafK4SvklxyphC-RofRyyb5EHGd6XZ3lHXZhQfLFotdpb4NpYncAXJp2SyvGhLaUGNTfpdqOZ5fY5pDuMVU-1pZuXk9KTro6zCI-O34ApApwXhhAvIg2onvDxcJoqDkHx2scXor1xmjpsjC7xnNw98nh8SOb1wfXzb9N5LZRoA5AoHjQ2t4pq6y20DjvlbaaHpJAHwfxNethIccVS3eP6fMiUoTlhYjybVZ7Og2dqYSzsBK_qmmgeyLME01WpcpWHRfKXMVh7h-ugsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=kuSrnUw-ehIVUIJdPa7-SZpbmou6lFDOblxSacgYFNO0hNtLQ99wXm3exLd-aTXkARMsOuWqafK4SvklxyphC-RofRyyb5EHGd6XZ3lHXZhQfLFotdpb4NpYncAXJp2SyvGhLaUGNTfpdqOZ5fY5pDuMVU-1pZuXk9KTro6zCI-O34ApApwXhhAvIg2onvDxcJoqDkHx2scXor1xmjpsjC7xnNw98nh8SOb1wfXzb9N5LZRoA5AoHjQ2t4pq6y20DjvlbaaHpJAHwfxNethIccVS3eP6fMiUoTlhYjybVZ7Og2dqYSzsBK_qmmgeyLME01WpcpWHRfKXMVh7h-ugsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvsgogrX-f2P6_eu2AHf1CbtJ5qX8kURyQnjKfBteNxiCLGaFSG6KiHUpsrrpfs8mhmUF_phX6q78l9wulVSrt4Po1tKnKFykdPIO51IQIRp_Kg6ZT5wWne_FMjYH-2pnKh_uqdIAOttVDq9LLPaUlWczLkOit9ZhRPAWUFhP6hwLNGX9XwJaLtcqzT3iKsn26vwZAwjnHtH6jw6YQA7qQsDUdwDOnHQLQdl2EcyINwYh1_U7VUeh-CcicDUsPv1F97ThlBUYXdmB5aT-6MgtIySd03xoolW3iYQ4ETk-S0uUjZptzr_ICE3FIvk9klAPlslX-wApXu910hJ9O0C3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7YmxSxE7ESlXrNNXLcK-towdlOyBX0o8LTxjyo-89N1bdJoR0WI2uIg85hkSCONqHpfLVEomc21ynU5_Ptu2EAYFj5hnKcmCDIcgtdtx9wgzovp1bW2fvbc4M1d3-_QVmxSkU47msZkmSTiWD-bdmTaGYHHO6xhsQtMroby_XV_IaMIAs_mh2pHkYckqnGi0l-INFMUdEMIeV_Bk21uBIdVlbn8iKqUMan9l7zIR2EqpPVy50NTBIGn-0XQQFy4Aj62EC7RWrb2vkjAcM_eyc1sqLQggyV6r3OsPbIFQbTD0le8WmstkYDrdNgcuA9p3z5_2p12ukKRSPw8olU_ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afOjOYKJ9StvRGATZO4Fvcs-nhkSAu5b0rj2rIwXgXomP5mXUAkaIzwiGYOOYb_9OOEgHuYpHw2H1iHUjhHv9z7EjdXmyEDgrP7d78pDuLry7MDaypNi29gpJ4ZfvLdi5Ng7_65UZFaGQ8cJVYWVpwdDQyP_ZsvLv6Jwj_WLmGifhP9cjyzUcVmJJWtF5Y8rDiLkDfLOdGJ59d2UqJbGrfq_b9IaeqJX33CmaiN1dK1CxValtnHoDaisSi8PNffdrxi8Qm_LuM_OUIrxnkDRYPS3cwhPfdMR4G-6aT8vjo0arucMLiDv93eNdl3EX2dR_xc6hT5EZJd4R8Z7mwdpZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNNJrKLWF950R8nNbOcP375zlSasCaLUJhmRuACjhfb7tp7vC0WdHqB8ja5R2r_biEtRc0-5pWDESvX_ielUt9rOQtWljMmu5AruDhXJ4prQlNy_OANqE8hHoXbNsjpy4AyoybXG9xC_L84YUhmL-X9vvJla-VLukCOCI5jGyvPw9jwlffqbYgvL94qEE_5BrZHvL3ztcHSOkH-v7sWAfS5tOKdjlhheNRNl8TXHbBW40r5PIjyFXxUJPke4Y3WXBXRhcRBY7trcTX-00f5fxjSyp4wl3Hef7F_4zzDOzXceuH0MBPbNxOE2zZRhAYQMhi-iQF2uW8-gDFdbjlGP-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbSWaZVDSFPkXI6W6Ow67FZvXL5aSGmiSYduEIqT6nNOseq_TKQ2gilbro38FxrxItubHWQPb8u59uIruD03GPI2TtQriDUMiPuR6Pj8Jl2DySvKgGtw43xkWKyREDRoNYsUyL3yAU0XFMr3cyuFgUtIFHRqFc8yLuqA2DT1XWjtB687_4yXyjtPi84B87MFoRPAPCu21G9VDhu9zghlg452GzWAxjDlv8OzAofatbz9dHDxepa4aot4Jx_CNMNY8rye4e4MZI0Ebmtu_k8CxGyOOH5_20KbjPM1hYEhayAJ2STzYDDN2lR1_LqEx4tlc4LKBxfiNIbGzZkgA2oD9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=XISJ2fGH5aq8yaoRYF50gSHeIvYgwfddMlJfVrfFxcxsOghyOMJkYrsEb1PVRck1GjgCVhxehotUHzvociBVVGIdhxCYO0AqEruxTePPOkr-d5uh9X7_9WyGvzPI-WlLzm5QYmQ1dUXlFJz4jriC59o5iP998_UpcLwLV-vw6fHmZymAH3RQOaMoHBrwRrCkY7UmDUi63v3fvpIraPtmb8ThI3oN3Xvu14eSLMr3Ji_bHOTDinVo1SpX0dKWnZ8tF80g4fPU2xab-bpW6Y2K7NV1Q1u7kGUOEnGUrRZSqlcbEYyDqd5SCZacxl3OoPtA0oClop7kTd4KXSfe6PPagg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=XISJ2fGH5aq8yaoRYF50gSHeIvYgwfddMlJfVrfFxcxsOghyOMJkYrsEb1PVRck1GjgCVhxehotUHzvociBVVGIdhxCYO0AqEruxTePPOkr-d5uh9X7_9WyGvzPI-WlLzm5QYmQ1dUXlFJz4jriC59o5iP998_UpcLwLV-vw6fHmZymAH3RQOaMoHBrwRrCkY7UmDUi63v3fvpIraPtmb8ThI3oN3Xvu14eSLMr3Ji_bHOTDinVo1SpX0dKWnZ8tF80g4fPU2xab-bpW6Y2K7NV1Q1u7kGUOEnGUrRZSqlcbEYyDqd5SCZacxl3OoPtA0oClop7kTd4KXSfe6PPagg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=n610IWT9N_Zp_R4Lrhaq2xEYlwkAHUicn03tf7VcjkkHkuH50VpXkfNu9YRpnOsAN5-i8uaIl03DIGp8AV587rdNeAvZ2cjXdMY3TeR9Bm2qHTc3-yzbT8PTjRUjorLFqFQkTaE2yjl8Hbo5o2AFqTdhhzBItQrZ9Zm_NznQHTE84SuqoULY8T5Zzysms29gxadpiBaIfH91wrUzrkLaH3BGdzy2WCDiNVP-UjLblvzNY2GLHP0JQ_WODd-mnBDMLGgzjw8lTHjuLJYBKs6xDPFi35z5lRfFQ5uROLE2zto1k2xKLYuAxIyFXF8xhIdQ9VsJQ7s_eFZWFQudRBA5Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=n610IWT9N_Zp_R4Lrhaq2xEYlwkAHUicn03tf7VcjkkHkuH50VpXkfNu9YRpnOsAN5-i8uaIl03DIGp8AV587rdNeAvZ2cjXdMY3TeR9Bm2qHTc3-yzbT8PTjRUjorLFqFQkTaE2yjl8Hbo5o2AFqTdhhzBItQrZ9Zm_NznQHTE84SuqoULY8T5Zzysms29gxadpiBaIfH91wrUzrkLaH3BGdzy2WCDiNVP-UjLblvzNY2GLHP0JQ_WODd-mnBDMLGgzjw8lTHjuLJYBKs6xDPFi35z5lRfFQ5uROLE2zto1k2xKLYuAxIyFXF8xhIdQ9VsJQ7s_eFZWFQudRBA5Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=P8lKrbxqyKO-mKRlihf-RrChUQFh2x_YgzMnpZGQfUeQKd58DfHhc7fm9YDCMkuO2hgQQLkMw9xdqrS-xEnCkTaUl1DYZ-URvoFo4kqmGAgEBjqXDQiWz9nFGFAr5sXtscWMqzsYn1eqG-598N_Pr-Jf_0ApVyRseaYz54W8j17wPGP6vcFLSS6noGXzGq0YbpYAalUatzQUikyelQqn_w4_9cRdhYB33-P48iXd7nhw_scFrzmRIfTlEKjzCSZtnhkVehvY1WbsKiy39e4PYusOClpLJUmL5fvXvnwd6pmP9y2AMDZsC7vDpnMRG3q9he_A9NT8Qqbya1IgeZ6b6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=P8lKrbxqyKO-mKRlihf-RrChUQFh2x_YgzMnpZGQfUeQKd58DfHhc7fm9YDCMkuO2hgQQLkMw9xdqrS-xEnCkTaUl1DYZ-URvoFo4kqmGAgEBjqXDQiWz9nFGFAr5sXtscWMqzsYn1eqG-598N_Pr-Jf_0ApVyRseaYz54W8j17wPGP6vcFLSS6noGXzGq0YbpYAalUatzQUikyelQqn_w4_9cRdhYB33-P48iXd7nhw_scFrzmRIfTlEKjzCSZtnhkVehvY1WbsKiy39e4PYusOClpLJUmL5fvXvnwd6pmP9y2AMDZsC7vDpnMRG3q9he_A9NT8Qqbya1IgeZ6b6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=taTMyfLDf4tCDzxnyImaAhjIROze7OjAPC15AblXc5gVXieh1u6MOJzrSt4muXPdC-QwpRivWSUlmeWNg7I0a3gG4Tsce4wGaRgtkJ46gkDkom4g4pMrQm074Der09UqLnPNfMTRSh60iDJjgQYi4BZm-x0WM7rvLwKGV9k1TpyhG0MZYr_FjMowzNNhvU7SXwRvvJYumABa_zMXvJCQBaGQllArWIDLmP9UAeag3-mevjTjzt3_vgOEt6qshptQaWGyINIe_q9-oyhNtZs4g4xOcHKNmNoftzbkCwFD5Efuq81uUsI34SeRY8MmjG-TDIUStVeBOy3wg9cgo2xFtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=taTMyfLDf4tCDzxnyImaAhjIROze7OjAPC15AblXc5gVXieh1u6MOJzrSt4muXPdC-QwpRivWSUlmeWNg7I0a3gG4Tsce4wGaRgtkJ46gkDkom4g4pMrQm074Der09UqLnPNfMTRSh60iDJjgQYi4BZm-x0WM7rvLwKGV9k1TpyhG0MZYr_FjMowzNNhvU7SXwRvvJYumABa_zMXvJCQBaGQllArWIDLmP9UAeag3-mevjTjzt3_vgOEt6qshptQaWGyINIe_q9-oyhNtZs4g4xOcHKNmNoftzbkCwFD5Efuq81uUsI34SeRY8MmjG-TDIUStVeBOy3wg9cgo2xFtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mx5p1Sw193NwCSWvYTuCqqxhZ8N3-eDJUqPajqL1ugIs457qrXhy-qJdhViTZz1xQNjkwSsbJn06hfjvD37HdeHSdzhK1cpcuh_wUeECSc3Klpz49SyGG1AKRv_NLzRK_3b76xvkoyo2XcVhsgfdv2KiViuzJzBNYStR305p5IQcG8O8nEetSu3sQE8yrPia6D2d4aWZlCoTPWBSgGq6RHdJU-jBcY82MH5INWZdhaBKOSgA_HzJ81Gc-ISyuvt5VX_PSVWRU_H_murJYnDhTS6XFy2yTlwq69Kl0ZKIbcSdQnVij20b9OzKHLdY6fWOLMywEnKwXUchcddi7nH9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dt5DmdvJ55kQ6NM41dzIpwRsgrk7Z2ZmvNslnzZYu689epxGzmMMH5M6sTVUIVEMW1s5ScAzASYMvpMGc4NfuggRCLbiOHPd7wOAqm-oQV-rJAxp7Egz1yZl2xI6oB7w2Jq9aPXfat-XmEGdhWMisAAfVT4WEIcZCrKOhA_cHAf_vTO6OYEuBupJ9BoaPD-0i-QbrN_a8vV-nYniGAEpZafhP9ixl8ePkAHmBGkvPGXEo8Gi6K7YBjbUNIuDoHO0bofh40K4JzpoNFkPp4PNlw6-fgO0hzUOj-SIlIBko6ghJDkg4XbwK6mAXiguevkyFUwRsNITSH9ZH8TF31MbMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=BaETyhCSG_Jw0PSE4akDfyJWRC_Hogl-jPgDCZKBw6jZPi9Ktq--WnD__zyz73bt1-9o2skL1TSee1CrzLqkE8LFUDF2bKdiJwp-vfFYcGQLlyUHGCJ0W6DjAmYCIMoCbRgsbPWex8Xydfa_WoVI1KPkuV1mCgdtQBxDtYZJSbtRz0g9QG9ERbGpUaQjO4onA-j3ff4He8du1HYOqJGhmjAaOgVZvJapbbWwL2IKeCJ04ygT-2-0-HTYbGiSbW7xGThhn13wh4kDovSR9Ra7xVG2kXPI4UOA7CIdiZH8SZk5KYL4Awn6DsFOG77AbscSzHqW5x_1fqptMcZ6m2nCbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=BaETyhCSG_Jw0PSE4akDfyJWRC_Hogl-jPgDCZKBw6jZPi9Ktq--WnD__zyz73bt1-9o2skL1TSee1CrzLqkE8LFUDF2bKdiJwp-vfFYcGQLlyUHGCJ0W6DjAmYCIMoCbRgsbPWex8Xydfa_WoVI1KPkuV1mCgdtQBxDtYZJSbtRz0g9QG9ERbGpUaQjO4onA-j3ff4He8du1HYOqJGhmjAaOgVZvJapbbWwL2IKeCJ04ygT-2-0-HTYbGiSbW7xGThhn13wh4kDovSR9Ra7xVG2kXPI4UOA7CIdiZH8SZk5KYL4Awn6DsFOG77AbscSzHqW5x_1fqptMcZ6m2nCbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqPyEbxYXlFCdwuhaChxYi0zTA5JCJsCB-V1ZCipoqdD7pRaY49GoUMs6SupFtPcugn67U6ytw7Ul1EeubPMzp7_cTj1tK3J2r3LUVBxTewB0ewnk-e3Zs-9PEjkccqKSNVGoVLF7Cmg55CE_g8QvYVSFv3vU7FivsDSd4oDDpArJMW_g3ydDaNQqpCvJLMBUcswEBkX_xoWXzbFA_k8OhghAGTWTxUXLBD6e0D52z41Ixzqh7GB538fpETJ4RX585f6zpqohprfE4ziTfSLSQnpDLgZw_54E_2TFybydXzG_2XdaeR-3V7xbXTLRY4VTXl8GpsPhGoHcNnSiaZq9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=Ef7S-qfUZw008kNiM4cuJM-ZGPkAW3xRJssaBGAq6W0JlJs289HQYxQHUg4snysv6M9-DCjl6xrciaK-9s_i8Kzr61gH9KgVDzy8wD5E_emJRHl1GE3Hbb1xEsD1yCUd5iBOoa92vP5NgWDvjRwMX4YvjJxgROdtTICxljYzQkjRDl5nQ1XtlHfXwiksO8qD4W6Zet3OTh6paSIeOsEWM1HQYAYe4F9JuzSZyfvjEp7cQjjLVT5_SvRs2G8HH53AP_Dno_zvNJYlxjq_TFJutosXuAqUUPcqKMbitCtQpILJSqPHjSjsV3BBUuePr7F4FIZIlYiTXJ3lQGz5KK1ltA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=Ef7S-qfUZw008kNiM4cuJM-ZGPkAW3xRJssaBGAq6W0JlJs289HQYxQHUg4snysv6M9-DCjl6xrciaK-9s_i8Kzr61gH9KgVDzy8wD5E_emJRHl1GE3Hbb1xEsD1yCUd5iBOoa92vP5NgWDvjRwMX4YvjJxgROdtTICxljYzQkjRDl5nQ1XtlHfXwiksO8qD4W6Zet3OTh6paSIeOsEWM1HQYAYe4F9JuzSZyfvjEp7cQjjLVT5_SvRs2G8HH53AP_Dno_zvNJYlxjq_TFJutosXuAqUUPcqKMbitCtQpILJSqPHjSjsV3BBUuePr7F4FIZIlYiTXJ3lQGz5KK1ltA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBryoIjTI3geibKI80kq7hnYFPYr1CVswF376CWXDM20C-sMY7zEt2tERKPVXQ6lpygWr8xdk1T1Y3QmhiAi26ZB_ydlqmphvcRzO3m79bGPVTxZfUvLjkXhmrLMfCEmhnVIYbfLxLzbNup0gY9_Pi6UsJ-tDb3UcU9qTEl4PKP_Iin6TvS4BnU7CR8lwOvjZzKi9voTJEWMn_GBAijo6uLXoX4Ii-fnqJTF94-1uSWI20FACuFCe5pjcPnglhi2SuZI22dXmerKDiwX6jWh0szNv0fzVGx4AmeUrThHuNJzCLbTn90tGEsH8vxIUakS3fdhEPwk4TzpaoQDW62Mhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4Nz8OqjZmq6-bFGdRIhTbmWgyoXN_hUSiiMjsUn4691Z7CzZxCBXLbLTuiJl34tZtJnwQF83VqwE5b2Qq-KPXW8HAkcc6hxqXtZnZQjejPccCJgWFHLOY14V13Hw176ipgtMpV2LRgTK0R4I1DGinsHB40GF2b6T0nJGoMjRLCVA083EKViAUHmVF7nMTT5ivj9p1W1frv_tGkpv0peQbIrQsCqDvqyXvOPqzj6yvBrPdtOqwjSmQdjy_WDcbEymF3GCFpFzvn1WV-kYltKFhIEAQ74iXPE7VT28XWgacJpAw70AK8NlPajNy-TGIc5dncxjHY0TvQyA9UMXAPk0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=snKrnAog6-5RL6P4U_hgtGbT-vIIIlw2iP9l4KdE4Avdxy_oHHl4JPQoVWleXSszQm77aZBZauWjWVAtPZK4RT_NNa1JGBpGb2LSOLLDCYkqBVX19qiuC3f43s2m75Xijt-jBdvSr8oC7TcAF05SKlsMqXr6Svfjp48FoZ_Ib102jIvKh0pPKutUcV9tzHN4tKBgnjVsEyvhOxN6TB7vHeBJ2jSfmIe07BG4rvq8ybSRraC8dFQ0fIZdqIvA3NKMzhwt32d8wLzsXRDAgm-Uy1FBU8EWmK7bz7-wjgXLLJEjv-7vrr6Nc40oEPVsMFk2lB2RTWd4c9hSQ4dBc_uIEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=snKrnAog6-5RL6P4U_hgtGbT-vIIIlw2iP9l4KdE4Avdxy_oHHl4JPQoVWleXSszQm77aZBZauWjWVAtPZK4RT_NNa1JGBpGb2LSOLLDCYkqBVX19qiuC3f43s2m75Xijt-jBdvSr8oC7TcAF05SKlsMqXr6Svfjp48FoZ_Ib102jIvKh0pPKutUcV9tzHN4tKBgnjVsEyvhOxN6TB7vHeBJ2jSfmIe07BG4rvq8ybSRraC8dFQ0fIZdqIvA3NKMzhwt32d8wLzsXRDAgm-Uy1FBU8EWmK7bz7-wjgXLLJEjv-7vrr6Nc40oEPVsMFk2lB2RTWd4c9hSQ4dBc_uIEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=eKH6pAMbU_rphrhM5X0sAok_RUuXdo8MGmllMNLk4NFNspjzfRPY7FKenBK-G2t54AoF91gXKj8SJzgzjZhqDHV2flJTszAvz9rgnSZwaUlGHrlI60m-CGNZE_i447QgC_JaQMHQOv1EJtYWUdKywHLLAzYRJiFRsJG6Kf5apILq53Nj3b8izmlcxb84UYikF3aPS41FwaW8VbKJAxq3um5UPJdkLH8sJPmgGaFLuYZga8yaBu67DsbR2zXtuBzPRjG3bMRKrxAqsJOq9niSox729FHN6kWG2pkA11W5E_DbRDB-U2XCuXFYlngaSZzELnTbV-Myu1rVyxkUZx2fCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=eKH6pAMbU_rphrhM5X0sAok_RUuXdo8MGmllMNLk4NFNspjzfRPY7FKenBK-G2t54AoF91gXKj8SJzgzjZhqDHV2flJTszAvz9rgnSZwaUlGHrlI60m-CGNZE_i447QgC_JaQMHQOv1EJtYWUdKywHLLAzYRJiFRsJG6Kf5apILq53Nj3b8izmlcxb84UYikF3aPS41FwaW8VbKJAxq3um5UPJdkLH8sJPmgGaFLuYZga8yaBu67DsbR2zXtuBzPRjG3bMRKrxAqsJOq9niSox729FHN6kWG2pkA11W5E_DbRDB-U2XCuXFYlngaSZzELnTbV-Myu1rVyxkUZx2fCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5VKOs4etI3z536ZrnlfF9dMFG4qG8AeDK-7DIVDuwcZ-J38EkW64Ldj20upl8khAR0ZbK0UWysd-2HLAtCRR1pt-hI1710firzhdetIx_seiiSzoa2A9qGGqkdL_Q1NoI8oi7Cwnbn9y-VyGhV0VSs5grTQaN_C30K7YCV_3-rKSOlyo9bhbCUzV7KCCIavsITLhpxc5sYr3ry06qAHE2LWDDRP-pslUG00Khr1dQKydxZWiao9hOA3spuPuGHXzTpMBsbxpp88NZ2vpuMJ_7840UTXb5vi8poohgIYSDFvWCx5otEScoDmMC8qNlhiLStSn9NTzCGn2TFzsx6dpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpcqfdCEBmNdQ5fF8_pIlPs1uO8LWe9SYLtrr5PVZg9D0P3ZwZgTe81DFUpmN2B_N-03kpMoZI6_r2Z58rAayhAkCRZmnIwIP72TsTDXzdv0wZ-FLlpEmVIAcz4TCrsQlZQJm4vRTmZWowW8L5ty6pzPAzVvVrw0pA3IfXbpuqSqgVx1oawQyIjlX3jwFrStXDUF0woFLh_ApSPw93IRMAOIOGmNvWInkn4CHizaq9sDe_bEblK85qy4Qk9oQg0qKP3MjXjWAJFU1li6PnYYf-HSYwT00gL6l4PCO8ArQQEjFJhmcMaE8OHb8BayDNI4bFQezPp_Wumrpt8Bnbu7nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQMaS8iQdyi2ytvlXqRwirFf9K1ncdPMlXYKzzw3zyK_Hg7paSC2Tt18W3Z9srxJKS3WvxP4pb5AteV4KtnSw13o4BinmDFJBo5MU5AvjP_JZNQN1K6MXio04fLmD8RLpsDUu1fjaHY544GEqiuf1JBnUk9ET393_VGD1SWWZjj9eIEARLM0GCBqN8nz8v2YbjqjBhsnfDb_jOx7nOw__9MuSJD_AW21PkinIWZDmt7FOqwdaa5GNhJskxD-2epGFvmWddbvsDkzh40EXzCM7kwKUo6rnBkEytD_0KJo0jOsTGTX6LEebi844W3BpuE7p6Ai0KiC7YnQ-Nc2_bdFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=fVvpYN3M7y0Itd9AgJzB-NBl4vfYl3wzcpqi0-NHnB-wKe6lHhgOCFcc2IjwTvxKlkQjnLIcXun69C4CNxbiYSI5Xoj30RZemVvIVZQLnIqQ_JYFhGBT5K4zQCons9F5ap9BQwz8IX2i__0J8FP6I2a_Sistok0YS10ttb9D2_vL73BI3UK75E8C0GT9ZMAsGB6KHiY6KsZqP-wbxuti13CnwqRUFiUQQDmYNYNp9i8JUSKit8V_ux5Qc4urRW4Q6o_4_m-s2MJI3O1Xw9LAFMGl-olgMuK8CS0h_ey9E1-7JDna_6-GK0QoeeD_W9ivAu8IdkxYSHTk_eq3bFSm1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=fVvpYN3M7y0Itd9AgJzB-NBl4vfYl3wzcpqi0-NHnB-wKe6lHhgOCFcc2IjwTvxKlkQjnLIcXun69C4CNxbiYSI5Xoj30RZemVvIVZQLnIqQ_JYFhGBT5K4zQCons9F5ap9BQwz8IX2i__0J8FP6I2a_Sistok0YS10ttb9D2_vL73BI3UK75E8C0GT9ZMAsGB6KHiY6KsZqP-wbxuti13CnwqRUFiUQQDmYNYNp9i8JUSKit8V_ux5Qc4urRW4Q6o_4_m-s2MJI3O1Xw9LAFMGl-olgMuK8CS0h_ey9E1-7JDna_6-GK0QoeeD_W9ivAu8IdkxYSHTk_eq3bFSm1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDVPe3atb90grAJk8qgwozyIDDpSg4pMsrSZbUXhm0IiiY4Hn6T_vekNnAgto0zdnKVHlnaK31l64nwHoPGyiAw5EyM6b5WW_SVmzxSgfJT6Hs1KyREk-mZ50sYY7RDxM20Uho91qn7PFt8_ocdb8iCh8TFu96JSvRJ_jgZC4IfwH5t0Qkzllkpj-pKrXR4f1rxuBX-wMf8S2OR_DKjtdXpauOIzMvUUDukHAicJpSvQhRnITxVjfmitfXHAxvTax5CxfkiObhExAKkHY4RJhJx6u8Pjdaopa59I9O6xD0q4mypFIk8ghIWyHKz8SB7cD0K_Se-lVgswLg3t5gKocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSfQB5R8HmnOhjjfCe-oN2ZhYuY3_knsEhbd1bdMBR26HJ4KnHzzMVYtI3Ss5GpVNXumOLBuwpJEzPV-xJzWj46hhMszUf4TRdTBjtXE62NutdoByIy4F-looQImbhEMEJotsAE00sS5bkpkI49wT9r-c7jbqPwovob9NA39C5kthICTJQII6cU12MXoGUd_aGsfhuZZMTubP-ilgezhW705R7ANcwHknN5SgzFLqAsO9hcg-vfaFTjfMRSaMLSsgoOfo46lHhnMF1ZVaJXyTh3mF9MKPoZB2koaByoC5HPIn9vHCy60lMQ5DBLphp_WRMrWuKipv4ncN2VKKJdhTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhSTDehU_CLy_wRt2fYCJzJWrszSB-0bKKViTKPj4x_slbru--gQMddgYGS1vECrgxiovAS6sTSBH2CayIY5OniIe19QGhgT1HV37FIXi1GAsDvWhwIp1khNLg0rNxd3BzGXy2wo5oopZubyD3v4dW1rl2V_BGnBwyoVhmxqH92sLTKRA04qYWgLSReyXHWl0sRooBS5CuGF_OxZsI9y2uPMab48vBuknYPHElw0vJrdWCiR5WDGuWqNNAdzh0IZB9c9JYDL71C3a6_CeqH31VuP8Cxx6ovcRf_Wum4l4sAa2QXyyJi0nCiZTxb9OvFnssAaPfTZc13bOqP43jhGNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSWheaqq5io7d1O5BqgxLQLSnE7HQRjq8TO2PaM5THEeWgEUFS3mRhvrDfGERZd3eICJb8WVf3japoIwP2JSR6nxggXYWklIzgYWEvt7-EOy8KfgyUbjKqeqLWPWftPfV9ZLHdKo1oBS0SeYVz8gFYAQT7NBRwJcJf3Lg_liIl2hvt2sCwrS6lkkOgmqQmiNc3gyzCCcw3udphcsNciO2mqokewEfUhGyR_cFwzKxSkS1yJBZoateKK1xlY530dz5i8h4xhMJBQ-vZAYNCfbRzLuFI7TjVbfn3SPJROgibRMTbve3kzAZym1MZW79IzMdAk4RRUqhV-zcMLCQO7ZLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=r6ABWQeO6vTdDlOnVubGsP-qsKnOU1YUdJbcfkJRKF9kGvui0pWLynzcRaHhWVexENs_AVShnaI1ETGUsuKPSGdY_JpQ-Vu7zuxZT3y3OoUYRIhS1X8o9ip6KeKdodydb0oNl1yZ2HWC_LB0yL5XAJv3Ex25bFXhTWr8Es7X40YYAJDmIQeqUKbEbXhS8qn1wfmpLYbR2CVAwYd6RVpfC4cMFeFOsQYcoZba0J0UxohUZ3B8wBzXsfJAck-2Q9SlzuAu5PoF4IfqLYbJIpD2gzO4yoAAgiSg_NngZpJKsu5CDx74eXPqjZTUz-4GFSOjGScpHTTnoIFGl8OGPRPi3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=r6ABWQeO6vTdDlOnVubGsP-qsKnOU1YUdJbcfkJRKF9kGvui0pWLynzcRaHhWVexENs_AVShnaI1ETGUsuKPSGdY_JpQ-Vu7zuxZT3y3OoUYRIhS1X8o9ip6KeKdodydb0oNl1yZ2HWC_LB0yL5XAJv3Ex25bFXhTWr8Es7X40YYAJDmIQeqUKbEbXhS8qn1wfmpLYbR2CVAwYd6RVpfC4cMFeFOsQYcoZba0J0UxohUZ3B8wBzXsfJAck-2Q9SlzuAu5PoF4IfqLYbJIpD2gzO4yoAAgiSg_NngZpJKsu5CDx74eXPqjZTUz-4GFSOjGScpHTTnoIFGl8OGPRPi3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
