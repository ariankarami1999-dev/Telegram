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
<img src="https://cdn4.telesco.pe/file/c53FGN8spbQYSpqXwfXgo75BoDWEX_pV_XC3w-c9WMPL4Ubn_sCzj07VLDPNmsl-N_KHrA2x6ees08ZmAFI2wlB5_17cRJ45EMfjuXMWTzqHPSSMQp6FHoqkDNdeGnbRbCvsnnyG2gr5wSedpU2EMZjh8EU7fTqSxS7wL4Xhlt4B1Vns-M11piZpIislSePNDgwAAuhJptXjot2xObkoLG-MAhohsLIYEjv3LezF19BXtZytvUkjtcxopoB1FN6ay3uzWHn-aPFLT_zAPoM4nzwxCDm_K4yn-QzV9_WbTq4uSHfLkarIIxrIvIwB6ExCywp5bl_0wPnodjDDeJe4Xw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 224K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 02:49:00</div>
<hr>

<div class="tg-post" id="msg-82705">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad6P4u9DLEBxJh1PEANooD8oGfoymf6tTd44nkFIpOL3kLFOCyESjEmouHpXLsw0uXXEy96oMUeJHXyFvOmJUQ1XFbRz7FeWRxJvpZROKTmSo_HxgZqMM_98qYsPoTLWOloNPDaFDfPFCqX-WSm9d9CXH3rkOSrL0FeMGh4DbuE0qABzncxzHbM1s-AOnKzfnGMVpQcHeMUsTT4wTlWH_DQPbUFFfqo6lWYhUYBqOlqHQ3xw2U1CWLKsDAnI_AqvL8w19iy8jDP2CPsroHUPNWpar1HQLIdRwhmPmKeLXUJiCRkAdePQ3CHtIfxD-vp58TkSo8q8F8zqTe9Ard-EcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیلی بازرگان: شاهین نجفی برای پدرم با صوت قران میخوند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/funhiphop/82705" target="_blank">📅 00:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82703">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJ7c0gF-F4tCAt8Amq9uRo0DuBvLJfbGvhzkdj0dVNK00ZNzdTtMfk_xrxS-wpui90qJTOqiOq8_Mdpy_PiiGUZyPiINgJRnkalAAhXsjDUs4GD5Ay3iT3affm09S69PnmK2FTrgQ0p9ABqVnfEaPFAgXvQCjk2iUk-rnXfQ7xmQC9RbE8Hn_GAddW8xeKh9384R_aYtk91MwkkY536NZtB-eqqVcTCMi2v_1VCmUCQianC-9qezqfVV-Bf4KJtr7_SmP-WCYsD6VaBieMjcuf6TdXOdcgWWCyH8MtGwWUugYtemtUU4wAslIKActouk-_cPi5JzdtHqBG8tYEvZ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a8b3495ce.mp4?token=MiuxxK6_VLK8Ay2hiPFXz8H1a5wP3W4WuLl0DsW3ZQTkOcSpoMrMZVitv10t1pNrnUk_YWYi1uosdbOm9bu4b-GBHfdIX0s2KMu5mrU6L3OBp58Jevxl6OXZAMSGiXBMJ48-H3y6_UuMg_Q4URPgwonLteL3rt8k6QhnKlycVAH55OaMFTnOnlx39QXHwd3nTilZ1vSB95cOMh6hOdZj3EHVAmbD_CAXM09Uy5402kgm4C_J9GgPIWLFqQofsmqJ_d524_MPuP5ui6dm_fhaeLLkRjj2en2l-QIKyl_Hp8E9IgGC8IDeKtJX8zLsCrQzXn1o01OUSpxnu7BuVtRG5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a8b3495ce.mp4?token=MiuxxK6_VLK8Ay2hiPFXz8H1a5wP3W4WuLl0DsW3ZQTkOcSpoMrMZVitv10t1pNrnUk_YWYi1uosdbOm9bu4b-GBHfdIX0s2KMu5mrU6L3OBp58Jevxl6OXZAMSGiXBMJ48-H3y6_UuMg_Q4URPgwonLteL3rt8k6QhnKlycVAH55OaMFTnOnlx39QXHwd3nTilZ1vSB95cOMh6hOdZj3EHVAmbD_CAXM09Uy5402kgm4C_J9GgPIWLFqQofsmqJ_d524_MPuP5ui6dm_fhaeLLkRjj2en2l-QIKyl_Hp8E9IgGC8IDeKtJX8zLsCrQzXn1o01OUSpxnu7BuVtRG5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به هر حال کمی روغن میریزیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/funhiphop/82703" target="_blank">📅 23:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82700">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a822db941f.mp4?token=YNL1XbHMyzKv6RCL8-7UqsclqtRsDS5NIyDRq862SE5CujTlAEYIV4jDkZDp8CecDL7oNMQINBGB0D6axKRCkBrsaES9r1z6Cj5toGhFOtIdQ3zwfpbQqmfNMLFTYy5Nf4lxmXPnaU0dHCGCApoPnvhVgDq3xqz5WxAQqts6WlxhXv82M4h6q23DL_uIYDc5Ls9zQWgFXRnqDGtBzA4QMZpKZQm387Ag9aDYQSV-Azv_633Vsz0J-yqyXW5ORk8Pr_6n791lkUFK7yMBNQeAtNd4SkPS8N3a9Xu2WqJXJ6Nm1rJrqRmSsUULgsbrpsv7jVTYvwl9g9oKi5_KxZv49g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a822db941f.mp4?token=YNL1XbHMyzKv6RCL8-7UqsclqtRsDS5NIyDRq862SE5CujTlAEYIV4jDkZDp8CecDL7oNMQINBGB0D6axKRCkBrsaES9r1z6Cj5toGhFOtIdQ3zwfpbQqmfNMLFTYy5Nf4lxmXPnaU0dHCGCApoPnvhVgDq3xqz5WxAQqts6WlxhXv82M4h6q23DL_uIYDc5Ls9zQWgFXRnqDGtBzA4QMZpKZQm387Ag9aDYQSV-Azv_633Vsz0J-yqyXW5ORk8Pr_6n791lkUFK7yMBNQeAtNd4SkPS8N3a9Xu2WqJXJ6Nm1rJrqRmSsUULgsbrpsv7jVTYvwl9g9oKi5_KxZv49g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکوندی شیر
مسعود پزشکیان:
نرخ سوم بنزین از ۵ هزار تومان قراره بشه ۱۰ هزار تومان ولی زمانشو هنوز خودمونم نمی‌دونیم سورپرایز باشه بهتره.
(احتمالا بلافاصله بعد از پایان شهریور)
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/funhiphop/82700" target="_blank">📅 23:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82699">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBuo2LCY2_uPj1qaPDxCH2sdg22wz_solA2YnN5zN3bgyTzIe87Gy8TOQPINvHivto0dC5STUD6whHqWstTtETqqMCNeh0FX0p635SGjFiKyPGqBfaBikTkGyx3bSIJqw0OivppsstpwX67gfF4glWFq4-3Srcgza-lyuDjA0BohuFZUQ6EO2BTMJ7dvoMlB7vVeYLtmFMPz-LpM5RDOah0I94w8fCydJp5dkRwT4U17yzvpWkYKJY9fxQ36X5ixOG8q78egcIffEkxUOc07Fj3fE6x_W4GBX2NVoaMC05IMO1JzAOncXz-zK4v9JqYQd8bBBLgu_wnyhuJdma6wGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای تکمیل بازی Gta 6 بیش از ۸۰ ساعت زمان نیاز دارید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/funhiphop/82699" target="_blank">📅 22:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82698">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cd-pQNmjixAwFCo3k8sA_v_MuJ4Jwn9lUvSlBWnV4wxL-R-2d_eNwwQgDwyG3UVHG5qxi_x9GFDHVEPd2TPHuXC3UwsYDgsBHouqKCeCqtB6xQPSQIpmfQ-2Ng3ktjUXf_haPuQnStAUW7gckffBT6x1hAbEDc74aJof0xh74BGjGIOQJ4_jcFOIjZJURwJmeUgIMt6sVUV41_joBJO4qT6rbRSVpisLuEq6jiqIR4EtW7pvkoC6XNvZFhdPLGMR7oElelUuIGFcAvxdIlEvnqjqKm6t1C7v9SKro30NhVULOrlspxjdZ9dxhDjoDNSOntXV-b4KGAm6OeWiSXExLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الکی گرون نخررر
حجم نامحدود واقعی یک ماهه فقط ۵۹
هزارتومن
تست رایگانم داره؛تست کن راضی بودی بعد خرید کن،خلاص
❤️
@VpnRgbot</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/funhiphop/82698" target="_blank">📅 22:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82697">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فیت خلسه و هودادکا رندوم ترین چیزی بود که میتونستید امروز بشنوید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/funhiphop/82697" target="_blank">📅 21:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82695">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AXGBR4cd9uigLcZt8bTvScO-N9BI1b2fguj8WztyUL5f5sCTthvcNVPFBX7aFKN8yp67F94hCjGzLGyJ8q199n8jR1k9wsGWo3mdwL6VYOFv_Y95G-lUBvUERJW1CZKyyXNc2oLAYKDVovY7ZKPxCbpfyGkpKr8NFnSrSO4p-cVLYta-2zloDDydmjv6G1MKMwA9-4_HZK5foMGsonli0faJkOy1wFGbyEluvuSKCfQhjiYbfXWPRJ150J49jxXYodMaJZm4v0AfqVTNMuNlh3E53ss7fpP1EDi_X24OZEVzp4FYihAWEVmDU2DYAf_a_R3sccol6Eu3ZDNgI8XLyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JSQoK0YYKylJMAR64ZNNzndMEehmISDkixNqf_jGw_H3WMf2aKtPAG1FwbWiyki9OycUdUGv_yj4m4jcrcXN9hc4NitVyzmtrY8cS_XHI8I3bSaLZ1lJ3OYCQBGLpuUSXaQwmUhWjbvmwQbxTUvW6RdY94JG5LeVMPccfPZC9xAyU0vrK7ZG65anRR1SYKqnLD6Q5kHQL0HZSbT0vsIiBX5ZLXUxpXBrhPFPv1Ft9JBQVT-vC4BbjeAN1V_HCnqIl3l7qdchzSI34FRemszeDbAnY6IvsYVTIkXJnN3l6eqxhyOP24kxtxKnQC1iSnhmw7fO1ozxWJvW4tiBRh1IQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ای کسکش
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/funhiphop/82695" target="_blank">📅 21:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82694">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvwQdXfWE-LvkhDBklU6b60ETVRqmN94D9qlDu4DfJYdfgvwlg5PLaGkgqSH6_gRJPqbUugb-tcIPYRLyW-6-TuahyvMizKJLiI9Mqma7nDRrKBeoKrjwVGWiG6PlKrRCtstNcryBg-WPb-SBhs1SpNxjUq3ik9-7yLAxMO8LSYPgZrmZ5QOI6R_pDZkDT2f049G3Vym6Q0UXBQCmaZijrAB_ogjL91ljLbHgFhdwRf5DTYMn01kSJ8siUet1SjTfg-D8leV_OFXVvh7_toN4-dFUrfunxawJFgroXrrNlB_7UkArHbbZOm3kk5UAxFf8ylkKQlsvjGxCrYc0VrVKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن نامجو برگشت ایران.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/funhiphop/82694" target="_blank">📅 21:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82693">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">مجتبی_خامنه‌ای.pdf</div>
  <div class="tg-doc-extra">250.2 KB</div>
</div>
<a href="https://t.me/funhiphop/82693" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مجتبی خامنه‌ای: به طور جدی اعلام می‌کنیم که هر چیزی که به همبستگی مردم ضربه بزنه، ممنوعه؛ مسئولان هم باید حواسشون باشه حرفی نزنن که روحیه مردم رو تضعیف کنه یا باعث دودستگی و اختلاف الکی تو جامعه بشه. دولت باید قدرت و مقاومت ایران رو به مردم نشون بده، چون اگه…</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/funhiphop/82693" target="_blank">📅 21:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82692">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مجتبی خامنه‌ای:
به طور جدی اعلام می‌کنیم که هر چیزی که به همبستگی مردم ضربه بزنه، ممنوعه؛
مسئولان هم باید حواسشون باشه حرفی نزنن که روحیه مردم رو تضعیف کنه یا باعث دودستگی و اختلاف الکی تو جامعه بشه.
دولت باید قدرت و مقاومت ایران رو به مردم نشون بده، چون اگه خودمون بیایم ضعف‌هامون رو علنی و پررنگ کنیم، عملاً داریم به دشمن کمک می‌کنیم.
مشکلات و ضعف‌ها هم باید با تصمیم و عمل درست برطرف بشن، نه اینکه مدام درباره‌شون حرف بزنیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/funhiphop/82692" target="_blank">📅 20:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82691">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a618ede86e.mp4?token=gEzm752gQtfuDr6328RAAO_9ZhXnm2b5cEcGvNzieHeg0qCCTfB0DICd0kD53uznWXMawBZMlDT3gWpTHi0xqiI5AkvP95HcW1UY_1e6mK1ERHsoO0Mgt5iBdsYLTTTLiaUBIBPZeY1e3CdS4TQYTIRgr0FYi1JatpZ7wDTJhmdoH2GjH-9bD74v38Ngtf0gMhroEStTUQl-770f5oixkzRbW2vjGqkxWsz_3hWTXv9nlGSOK3DoHA8FfD6KpbN_zQ31IWCL8VJODdx08CjPjN6f6BKYl37rcNgcOwkquTHmOn7NJsvwz95mPV30v4JOaEqOcPeB1n-b4s1ElFUtXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a618ede86e.mp4?token=gEzm752gQtfuDr6328RAAO_9ZhXnm2b5cEcGvNzieHeg0qCCTfB0DICd0kD53uznWXMawBZMlDT3gWpTHi0xqiI5AkvP95HcW1UY_1e6mK1ERHsoO0Mgt5iBdsYLTTTLiaUBIBPZeY1e3CdS4TQYTIRgr0FYi1JatpZ7wDTJhmdoH2GjH-9bD74v38Ngtf0gMhroEStTUQl-770f5oixkzRbW2vjGqkxWsz_3hWTXv9nlGSOK3DoHA8FfD6KpbN_zQ31IWCL8VJODdx08CjPjN6f6BKYl37rcNgcOwkquTHmOn7NJsvwz95mPV30v4JOaEqOcPeB1n-b4s1ElFUtXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر کلمه‌ای که اینجا تایپ کنم فقط از شاهکار بودن این محتوا کم می‌کنه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/82691" target="_blank">📅 20:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82690">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIlNBbTuIZdDxV0yl23lo7TMXW3CkibtTE9kUtWAlozHtqpn7NgL6toiCrfDn6DxR2etfdZwkJ3uTZ4oL9IiC6C3R7qbHqbomSNStFKr3KlbMpx3vzCAkJ78AVruUGreQHrD91er4F9v0Wmf1b1c3sskuVN6hKhivFAMf00fkQAiIzfL-dB7kW2c1pb-D6oHuSU1RnJeaHtF0d2sR6xcpp9sc9Il_rJcqd5q1XTOO-p0IP5krGmXqZSWGHYZQQBiinoMWVn6cN06rfwGQmur1jS-SDzvbzxVi3Ne2thBgtI6hS3CCWkbG9SFKyvxWX1n9Yw3m6OwEHNWTYKad1P7dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بیمه صد درصدی سری آ ایتالیا ویژه هفته دوم
💯
⚽️
با ثبت حداقل ۶ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های هفته دوم سری آ ایتالیا، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/SEA2
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g6
💻
@BetForward</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/funhiphop/82690" target="_blank">📅 20:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82688">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNm753tpZQcNP6YPLBtvsso6Jvg_lapd2EhxP-xhl7-iejJTS-sOnkZfuFXq6mN_T4OZ-CcSXw2gO3EFhjmI87QdpsYbuiLzlXmFTHJmE8gCsDiPoxLxigsZVA4vJBvkW_Zgbkls3s_iyPEKWcUJZfS_7heOBYDfXiIveDxhoPGOsS5_eRHzYOymMjOt5NV3tcHjwoLyyPA81lmfDvXcGk8UqO5BdDViV7RRruRal9APIpKEWM71QTL1QPG8bLdaSgXuV1LtObe4KkwH5ZxrCRSLryS4q7S1hotFc45WuLH7oq0FVilDadWnaQECVtU7mJMEP2HsZteWTTDcNm_3hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولینگو معروف ترین برنامه آموزش زبان که آزمون انگلیسی این اپ اعتبار بالایی هم داره و مورد تایید دانشگاه‌هایی مثل استنفورد و هاروارد هست، اعلام کرد آزمون‌های این برنامه از یکم سپتامبر (۱۰ شهریور) برای تمام ایرانی‌ها متوقف خواهد شد؛ این تحریم شامل ایرانی های خارج از کشور هم میشه.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/82688" target="_blank">📅 19:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82687">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvAlSnsiy1zaksTz_UYHaDiG2LzC_WX-p5BpyQB3yPp0i7w8jRE2dssU-Nknhz2ddtv1kxYtUyH3GNu_bP8R5aFEeaE92HlSDzWlvCWd7KhEKrYqkC_rygRqrmmbMoDpz-DjaX4_ZpoKoFvTHbwxvOA6aWZ4Pi5oaC4JO8YG8oYQVJqPaQgvfCyT7Ty_7FYw1xx76Hf_j3JEavnra6GsmvgHpf2gruKJ_7zuMCyjckLh9ld_IEXKn_4YZ-UnWChGc9HNHz2tvGenLXCwtzZbuVsSMCPJnq7IYG_C70oohiDuTGEoaIiN_zOpe8pYd-zO8wYpsLfVDRhHBGqOQBKGjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یا راهی میابم یا راهی میسازم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/82687" target="_blank">📅 18:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82686">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐍𝐢𝐦𝐚</strong></div>
<div class="tg-text">حیف بازیو نمیتونم بخرم وگرنه  تمام کاراکتر ها رو میگاییدم زن و مرد فرقی نداشت کل شهر رو می‌کردم</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/82686" target="_blank">📅 17:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82685">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1PGVswspDwr08eNSPNKesqw_iFqeJ9g_Tyer-IXe5Zx_ooKbywF8Kdnky1tX6mINIZBD7fdO_MNUZUa5ej6DkwK_8j4hf55En2oTshxqQTELVWzp7_dc4r_N7n4T71gpLQcU5Ksg9ohSwllvkJr5Cytoikab0Ium_lvDhzsMEleSHfqEgjcKwlRb6j6qO5wtxk-x-pPZSf95s6Fd6v9rg48VW1YfDYhxuDn2FajFdtE2DoJtpWjtrvQK6GDXYI_UbZ0QUjA_ZSC81DZ2DZ6dT613AjF2SQZN4L4GoASdIhXjenn63t2WR2dZcypDWCx1kuwL67laOXX72OPzIWapg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیم ساعت کسشر خالص بود</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82685" target="_blank">📅 16:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82684">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پوتک آلبوم داد  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/82684" target="_blank">📅 16:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82683">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پوتک آلبوم داد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82683" target="_blank">📅 16:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82682">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نتیجه نهایی اومد برید و کارنامه طلاییتون رو این زیر بفرستید ببینیم چه کردید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82682" target="_blank">📅 14:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82681">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03afa533d5.mp4?token=duOPZDDJx5V4hAhCSEUcBLbmP9ScqoA24mC4dblHp79E3ALAcdcssncjwUYGwqlZaEU8A1NlhWkdJKBhSssfGlrmAG3J1qWGPWxuqv_s6DhjepoV577KEOxFxp9NFkyOS4ZWXy7yxW32--buOGp7NOFRqWWxDAdftLj2-Hf1HZ8eBsC2gB0IYVH0kHyE-MoiEw1fIMdRJ1r3s0Nc3p_6DSM2rXqZDtyTR5fTL9hF8XZv-quiz9SYcTDXQHiifXbTldhHHrOG-m1UpJDeuUs3N8q2xQAestcb2oqM_fRyMofOfk5UH9ePQC8PRYzWRCigmEdQSmBE-TjKpt8grrSOgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03afa533d5.mp4?token=duOPZDDJx5V4hAhCSEUcBLbmP9ScqoA24mC4dblHp79E3ALAcdcssncjwUYGwqlZaEU8A1NlhWkdJKBhSssfGlrmAG3J1qWGPWxuqv_s6DhjepoV577KEOxFxp9NFkyOS4ZWXy7yxW32--buOGp7NOFRqWWxDAdftLj2-Hf1HZ8eBsC2gB0IYVH0kHyE-MoiEw1fIMdRJ1r3s0Nc3p_6DSM2rXqZDtyTR5fTL9hF8XZv-quiz9SYcTDXQHiifXbTldhHHrOG-m1UpJDeuUs3N8q2xQAestcb2oqM_fRyMofOfk5UH9ePQC8PRYzWRCigmEdQSmBE-TjKpt8grrSOgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرش عمید، معلم هندسه و گسسته‌ موسسه ی مدرسه آلفا وقتی یکی از دانش آموزاش گفت ما برای کلاست هزینه کردیم به جای صحبتای بی ربط، بیشتر روی آموزشت تمرکز کن هر گونه توهین و بی احترامی که دوست داشت به دانش آموزاش کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82681" target="_blank">📅 13:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82680">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeMaabiuTt9wchI7mOgMNYU-PwJoDD6bE2K_pO7VT71SBSTh6ofIMe43p6lxclgY6XQyBk2huv3atKySVQ-y6xzuRSHuPk8t4_kID69tQ7CiKTh4TOMB5BQfu-F6-qjMYeD6n-z-tNTdn_eV9JUVNrCVaXUcUXyD7dYP02xFNBT_07_fxdChZsnT_3nFMgwXk7ofpNLsSciw5XurhXo9XUGVFP03EqR3GyLqhbNF4ag54mBYklez0_nQ5aQMxqCNiuKptzobfmZDy0adNP-givW7d86JquV66oA8o_o_00RSHe8-T343y2GaLgSIhu4JRMuC3aZmR8ZoJ11tI_E9Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بیمه صد درصدی سری آ ایتالیا ویژه هفته دوم
💯
⚽️
با ثبت حداقل ۶ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های هفته دوم سری آ ایتالیا، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/SEA2
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r6
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/82680" target="_blank">📅 13:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82679">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTPnrs8V_3lrMkCHokigziQTWXB8ipekceuExjGaxNcazd7WmRH8UqPBZdL5Bx68w5MD2LRTtmG1J0BjFTZMqW0K2B8Dy0Ns6BH2O2shAF3KSsNxpwfrBYRTJi5yXAnmwf6-7U1PNkpUGA7Vz8iIlLK_O3HM9jXoDIFRN-uMVmoSISot1_4SfzKJtOOwdMiUx0mXh3n4FfFZ5Mk6OibwAhD5k87wcUVX1lw-ViAbpTctWjEwcNUbawMppbN77UghND-qgrp_kWMHs7DULa4FGFMABbQXeqYx_t7O9KkWiRu7PGpjhYLow1u0FXugh9Ct-ZRyOAXLP7OCx_k8BYpCiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون دکتر عراقچی جوکاش قابل‌تحمل‌تر به نظر می‌رسن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/82679" target="_blank">📅 13:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82678">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrVSqvn-MkNCYySwPiSTJL_gai2S694gdEPDyHRti6mJdKe0Ndi4eazYN_RrkEaMg5KyVDeNAsqx9RvlIUe8la_hxNijxBQy2rtP97T1mqO93_PhYPBwONUWoLv9skSSbtn7Dncaeg3mMjR2y8ATV9EwUdhHterwacAKUTHmBQbkKFQH9mWCMHUTQD2GmiG0muhduPabfV1UjGzG2iSG2IbIkrdA0O3G8b0JRXl-ACRriUlJDg6d0V-EgvHRSVr2hggf3ESG54hx5JYAvrOPOfLguZANB8NevXGZvsKJOjXmlut25PAWpbcrPb0HlPTRzKxdSQfxbCCDC7O2tWVlfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم از همین الان پس‌انداز و لحظه شماری می‌کنم برا کنسرت استاد نامجو تو برج میلاد. واقعا حیف این همه نبوغ و استعداد که این همه سال از وطن دور مونده بود. ممنون آقای پزشکیان
💘
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82678" target="_blank">📅 12:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82677">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bcfb73b16.mp4?token=X373UV8gXABiyvaq1inn7BnKnROPzatyDxl_cB1hposGQMNnHerCLTZ1Q_Bze-XVu5FK_B6_HBXrZtybvc8-fk0HNmzkVY77DM7lSY6kEDrfAUhCSJnVq2gpEoykgly8EwN9oKZ7TE71gJcWrmTIJPEQ1BKqCUpGbHR0K8YefenNCTYhIjqehukqk1WoFCx91ty5HUq4WaIfbLaofVKcf4UyM0O-z83Ix8CUqcS3qw0leOq6LBzwCWRcq6OVo7rKpqdF5ZzU1ZpiUpthgzAQWO5P5K6S9eCMZwt_aJ6QtcVhCP_MlPuF2tQfzD63QC8td4cYREOsJdWy1WWMWMMCOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bcfb73b16.mp4?token=X373UV8gXABiyvaq1inn7BnKnROPzatyDxl_cB1hposGQMNnHerCLTZ1Q_Bze-XVu5FK_B6_HBXrZtybvc8-fk0HNmzkVY77DM7lSY6kEDrfAUhCSJnVq2gpEoykgly8EwN9oKZ7TE71gJcWrmTIJPEQ1BKqCUpGbHR0K8YefenNCTYhIjqehukqk1WoFCx91ty5HUq4WaIfbLaofVKcf4UyM0O-z83Ix8CUqcS3qw0leOq6LBzwCWRcq6OVo7rKpqdF5ZzU1ZpiUpthgzAQWO5P5K6S9eCMZwt_aJ6QtcVhCP_MlPuF2tQfzD63QC8td4cYREOsJdWy1WWMWMMCOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن نامجو برگشت ایران.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82677" target="_blank">📅 12:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82675">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/trYZd8WQ9GXybF_mAAFOqgT7CW6GNC40NF0pb6hpcL8khFgh7RrpisXn6b00kHS6wZ4N_8K2A6U2ymWVJKmriD-MxaS-wIAQq83IZfae6L3rTawIGQpdnm7Mu97b31LiLWq0qfzSjF-jKQK3bXRzoeFK3OEEtMyH9XJfPuXG2OkTJVu9URjwx1nN5gCTgt5EI8g6us7j5IsGrT5haCSTIIf73sCu71YVCqJdr9U5NjV7whJJ_0NeSfHJihHAj02XT7hgBSBWfcPwTxmXN7P02FLAAFMpFe2beyp-rH7gHSM9hDAWZjXoNH_3lbQp0ztjED9LUnWkfx_vOvJFhBN5hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qokovE5udJXmiKUFD3h8LELLekW2aBIs2aeLzfy82FPKtFMO6IbxDVQMb4kTDwnQpgpIvxJuJL7vbCe8UVz6oNJiVWtSALfvWkGMNwB5Oo1wfb8KZAsaF-ra_2JNQt_GFMV-hkSx91z6ZetUqLTN2zjryVOqll6AUMbi6NkOxjNt-zGsbVsuDxi2tlrAgAqeAOup-VdEMlE9Q1hXBwXB8xPQk4KkahHMiRYXQJ-lMz--GDmlyzkfXccpv9dYwp7ktN0c6CaGUhrsXso2PJu37GykvP5Tx6MQQ1Ei8YlfH1X_V6GUDy8g6eWmdcNv5Re4hToqhvOyGEpH0bqAUenjtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ارسلان دیگرد (یه رپر زیرزمینی که احتمالا نمیشناسیدش)، چند وقت پیش تو یزد یه اجرای خصوصی و محدود می‌ذاره و تو اون اجرا یه ترکی رو اجرا می‌کنه که یه لاین سیاسی خیلی تند داشته؛ برای همینم براش پرونده تشکیل میشه و به جرم تولید و انتشار و اجرای موسیقی غیرمجاز، ۳۷ ضربه شلاق می‌خوره و ۸۰ میلیون تومان هم جریمه‌ی نقدی میشه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82675" target="_blank">📅 01:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82674">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGN_nZq2XZKPjgs8VDsUg5iuNTE9u1OrqqXSJDTcdMoPWM_hj65Gfrr6RQFJ9tAriYnHcmKvvwnh_F8MMY1UjeIl90G3am_mUJ3rfRxg46ClJY4LVIhCLctye8sN7CzR_Elm9Xb_638nFBSvb-EwWfU5jA5ApPKsphbCKWO_sHItwS8XF_f_Y7HjA7PuC7AO6Kj2jAqnJUSxQYpgv43f7HrJv_NSVCTSUTu-vkgxQO-lZc1wgqEQ8w7bsjuz8uqHsgxi-hNFiHZjKKR4P9PAiRWDCy3FSpfJhH4hIWel1cDtfqhMp4Kb4aA5HXJYUIj54OAvqSNMo9HWyhZrdFct1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نا امیدی ممنوع
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82674" target="_blank">📅 00:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82672">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پدری شاهکار ترین هافبک تاریخه</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82672" target="_blank">📅 00:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82671">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">از تهدید کردن فک و فامیل ترامپ با زبون فارسی تو صداو‌سیما منظور خاصی دارید عزیزان؟ زبونم لال دیگه اینجوریم نیستید که مثلا انتظار داشته باشید پسر ترامپ میان برنامه‌های ضلال احکام شبکه قرآن رو با دقت نگاه کنه و بترسه مگه نه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82671" target="_blank">📅 00:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82670">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نیم ساعت کسشر خالص بود</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82670" target="_blank">📅 23:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82669">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کمتر از ده دقیقه تا نمایش رسمی گیم‌پلی کامل و همه‌چیز GTA6 توسط راکستار مونده. اگه نمایش خوب باشه بازی و رو PS5 پیش خرید می‌کنید یا Xbox؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82669" target="_blank">📅 22:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82668">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کمتر از ده دقیقه تا نمایش رسمی گیم‌پلی کامل و همه‌چیز GTA6 توسط راکستار مونده. اگه نمایش خوب باشه بازی و رو PS5 پیش خرید می‌کنید یا Xbox؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82668" target="_blank">📅 22:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82667">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کمتر از ده دقیقه تا نمایش رسمی گیم‌پلی کامل و همه‌چیز GTA6 توسط راکستار مونده.
اگه نمایش خوب باشه بازی و رو PS5 پیش خرید می‌کنید یا Xbox؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82667" target="_blank">📅 22:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82666">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اینکه هنوز ترامپ نیومده بگه برای آه کودکان مظلوم ایران و گریه‌های سحرگاه عاصم منیر همه‌ی تحریما رو لغو می‌کنم و بهشون ۵۸۴۳۲۳۹ روز فرصت مذاکره می‌دم کم‌کم داره نگرانم می‌کنه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82666" target="_blank">📅 22:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82665">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ بعد از تغییر رسمی اسم خلیج مکزیک به خلیج آمریکا و دریاچه مرزی کانادا به دریاچه آمریکا: ببینید، ما الان یه خلیج و دریاچه به اسم آمریکا داریم، شاید وقتش رسیده که سراغ اقیانوس اطلس یا آرام بریم، اقیانوس آمریکا تنها چیزیه که کم داریم.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82665" target="_blank">📅 21:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82664">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=QBX5yDzMnHXjdbJBxkQmLxD-dvPGRX9I4qloakOhUI9V1Ahd92HrQyWj6yYKVeWC-hqu1dVpSKVtolQ5GQEUGvujmu730W9u_f5CQ1gUCIMTZPA0TOSIaPjTIyVVbs0Gh3kgV88uZBBZ38euzTzEMVEoTJ6iEEzxiZY9Iiy3h_N7MF80dHHIiFs-PnrqXE8S2OjzA-9oqxV-eywU2n2jWMMZbYMK9S4BjFQyB-ukqPLA0HeTYDeasvuHJWAxuDexewChgOxN7REapdK6qAXb4FHvHtkkB8_PoaswZoZIrG9K3pt6spkIrIdqJGR3CvHAmqHQ88DC_Hm_asakrpUFtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=QBX5yDzMnHXjdbJBxkQmLxD-dvPGRX9I4qloakOhUI9V1Ahd92HrQyWj6yYKVeWC-hqu1dVpSKVtolQ5GQEUGvujmu730W9u_f5CQ1gUCIMTZPA0TOSIaPjTIyVVbs0Gh3kgV88uZBBZ38euzTzEMVEoTJ6iEEzxiZY9Iiy3h_N7MF80dHHIiFs-PnrqXE8S2OjzA-9oqxV-eywU2n2jWMMZbYMK9S4BjFQyB-ukqPLA0HeTYDeasvuHJWAxuDexewChgOxN7REapdK6qAXb4FHvHtkkB8_PoaswZoZIrG9K3pt6spkIrIdqJGR3CvHAmqHQ88DC_Hm_asakrpUFtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بعد از تغییر رسمی اسم خلیج مکزیک به خلیج آمریکا و دریاچه مرزی کانادا به دریاچه آمریکا:
ببینید، ما الان یه خلیج و دریاچه به اسم آمریکا داریم، شاید وقتش رسیده که سراغ اقیانوس اطلس یا آرام بریم، اقیانوس آمریکا تنها چیزیه که کم داریم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82664" target="_blank">📅 21:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82663">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXnWWbwFKg8zCgXFVjJp-VUb18-XCZqhZWg8l-lFwQvhZ22MvXyp0ckIytFt0-d-IoUErLZ7nTw6ZXnPHoKPT08hy3FmxiWUlt110sMcZYwv5HnW_ATM-B-WtdQ1BfO700iHyMx5GQBcxCk6QNeVLD7CPBLKjO4f2tgoe8cWyYXulgbH2Y-hL7K4nEfE3rY9_4yb2nvLrl5VLboOzmGM30g7pQhdmMpWujTv_7fmWkD9D5AVPopRGwxGd0gSJ2WS19CRQ0rBOtTaSAbOSiswGijPv2GxoKaydxFehsbB2QvPToLsXanhO1prPJ-25vvR8N9agLU1zOUbg9zoRZq4aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کافه‌ی اسطوره‌ی نون حلال و ایلان ماسک نابغه‌ی ایرانی به خاطر حجاب پلمپ شد.
💔
این بچه تازه با کلی زحمت و امید و آرزو بالاخره تونسته بود یه ذره پول جمع کنه تا به آرزوش نزدیک بشه.
اینه جای تشکر و حمایتتون از یه کارآفرین مستقل؟
لعنت به قوانین سختگیرانه‌تون.
😔
آقای پزشکیان و مسئولین با غیرت لطفا هرچه سریعتر رسیدگی کنید.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82663" target="_blank">📅 21:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82662">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9SQ1ORCbcgypcMgFLey738MLRGxwJzF0EVSvrqkOCe16BWXZvzAwYRPFWn46U8MAFDFrvF-b2F1jcHHTfkpiL2_qlfAjYOw3aB9QU9QqR-vioKaynpIDK-HtW_Prv4etjVx4Qdqj6hZgZIatPhZKqAQiQ0HpnAeDfIR63Azk_cepNPtalWxfZCcIL4Wkv_2R9wHq-vHsZGTWWk5-qVesgNXEHP5g4N5UPADBmByhFke4Hw04tyIQKoypSIQu1kULBfbfZAvUbc9wzNhF6n1hP50acxDhyKHdEh0HGTYJ-2ng2uJU8Sn8oxFx3ror_mINXfo3rSiDVz2ta01JyUu3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه این دوستمون اون اسرائیل رو اون وسط نمی‌نوشت، خیلی جالب می‌شد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/82662" target="_blank">📅 21:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82661">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShirazVPN | شیراز وی پی ان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLGFWAPn9xIfiFyRysPFEWsfVxBAJqlkiKXDOYTayL4-DbPfGSQ48pRaRqTb8BUJoqdroAAQlDz-bNxOk8ZMrlhNHtsf1w22BNJaG5IinDi4Jcfw5AxjdhTdFB3_R6ISaZTtCbmvNEPzoH1RonAr0kKgR0npq4qhMPrSyHaTUiiaHePKNdl-3RfBhEctGk3K_ouD43Mz9fDpJxcboHpV0819_qeQ9lms99e8Hvy1bCnUw0-dDJ1I5444JjsI19IYat1s8OYot7PSm0MD_SIxVWFa3uvxMe2eZyaFNB-zEh4GVzhGh1TE8j_AZaT1XCfqtpOS8lD6CxNoFsA5HcAQPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
پلن نامحدود فقط 180 هزار تومان | خرید از
🤖
@ShirazVPNN_bot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/82661" target="_blank">📅 20:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82660">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4gkhr29RpyyXGie7LKX72Z8c0SH5KfrtmBicyqXYLiv6TRrNItdj5qzVhX-0KaeEz_MX8al4tHGiVWeuoTUfzQwefO5IXjMGanNznYKsgd_oKR76GN9VkVqj16vhblJZMrnxvzD19gxQA7KUfroq6ENtowcki4-eyUqfR4Sw99cYaC3E9F0qhYm31GhQ2k0jrYYsI-WLEznjT-D887eSr-DjujpgZfFTUCA0AVg_-I5xwfNL4vjeyVfIuEHctBzULdoKN_VSvNnDcPRxFYNPu-Z82J0XUW8zTsCYOZPZz4zi0HSIQIzCVElHNuJaYJg-iwQ7duemBlxkqTfpOi7_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارسا خورد به سیتی و پاریس</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/82660" target="_blank">📅 20:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82659">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بارسا خورد به سیتی و پاریس</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/82659" target="_blank">📅 20:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82658">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyNnf6SaZGpjoFHcHAY7UUj9uskgftAtebnpskfTT_-If7aqKH1hahhZPozNocOLFZlGp19OfgkYjDXket3mEmSU78YORvwDW6dgiTMysB6DkfcYaSgcEd9c2BW8bZpeDO2DEQ-M905Z_JxWcV0ySOLkSx5ceXdx-v-DADRk2UE83Qx7XayeHmZo7R5GgkitD94ALUdUz8b3kDVCnMrBLmoS6zQiIbnA73MnZO7kRbxFiseFs7XjAkB4PF8idsp6p38_FRHHJF-IOuJTSAUNmhF2R4Wc8NeA0qgWBVtNlDtuRL7soHlgPbeT2G5f-8DgjNWyUjcIHgHFmQzVTXaNfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرعه رئال تو سی ال چقد سخته</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/82658" target="_blank">📅 20:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82657">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بارسا بخوره بایرن بریم برا انتقام</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/82657" target="_blank">📅 19:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82656">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plTRX-Q3XJnJG3dtAeiQZA9dyJjXuiHVAr4GbofQqufVIfYjY6SpEEwYtWKPpgbdqVjLamY5Tnyw0IlKPqoDp4oCDoAgnweAATS1JgHIDeZiwrBX_cITZDDY7mVw_aUGVKiQWDp9PS51QG9dEbWAK52F6WsQI-fUlZAPIq6Ja5uEvqcnC5rXLkNEyDc0N2yHJ7O833RxS3uRq4Ajfry17SqSEiGABto4wX4TlqiFJKAxkOEDbJL6GxC3DFztiHmLvS3_o67Sqja0Gx5x8sWpjt7Y7rewy7kY8g3dRPPGIKMSIBWuOToA0a6I3KMqG9L7JxksyeU5Ivsck-4whzCpHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/82656" target="_blank">📅 19:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82655">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17918269ee.mp4?token=EM5JwG7uoMmTVKrnwL1JuIfWTEwId9lus3u7OGRxTAFgvp7oX4lqb9rf1oQNotW2wL3xOd1RQAWd9Vq0Cd8tbiE08QN60Besh9O7148efiH2hCXWKFnom-bPK-rZVFo3alswqoC8AToJVBSjniBZ86dcocOF3fyfB4QUrgO0uRCrq-Zqvk20p9SFMdpd-kqxwoThUl3MMb_Iltz1NIo-DB1NrhszR8wUeqNv3YeWsZnpkjDpXf9samcRQPQGlsyIODExPFpgCBdIGA1IJHCvlGgdxKcVQqlJ5WlTw4B075zOb8SZ4Gxu82hI6PB2A_nuWkkM81bwoursRs01u-ALVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17918269ee.mp4?token=EM5JwG7uoMmTVKrnwL1JuIfWTEwId9lus3u7OGRxTAFgvp7oX4lqb9rf1oQNotW2wL3xOd1RQAWd9Vq0Cd8tbiE08QN60Besh9O7148efiH2hCXWKFnom-bPK-rZVFo3alswqoC8AToJVBSjniBZ86dcocOF3fyfB4QUrgO0uRCrq-Zqvk20p9SFMdpd-kqxwoThUl3MMb_Iltz1NIo-DB1NrhszR8wUeqNv3YeWsZnpkjDpXf9samcRQPQGlsyIODExPFpgCBdIGA1IJHCvlGgdxKcVQqlJ5WlTw4B075zOb8SZ4Gxu82hI6PB2A_nuWkkM81bwoursRs01u-ALVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داش علی تو لیگ عراقم داره شاهکار خلق میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/82655" target="_blank">📅 19:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82654">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFt_SQgm0SCebXp51Fjsd-BXHpPyG57vEIKbKIMPQyKXikg8xpCJTCOQBB5xgC5KvnuyVrfaPOW8AMUoNwdXnKay-AbKMwkMmEKy9JBx50akutIVBt7HuETrau4lPAwc_60GqKllLtwlQPnLld2KvqoQZAnjzAdybfMHVOoU5rmIqSG5KksaCwTzGvWUGwfK427GbIs8d05U8k94PrjQN8lh2zgDvwaIkSx1n4WJpYXmJOnrzGtVjMJlPMYK0gz4216WUr3uz_xSV9mfkBkHEyjgAKhElp6o3OBOoCeRp_7Lkq9fRqkgvJBW7Il9umcFZB-irw05unBgJC3wC43UdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بارسلونا
🇪🇸
-
🇪🇸
اتلتیک بیلبائو
🏆
لالیگا اسپانیا
🇪🇸
🕔
پنج‌شنبه ساعت ۲۲:۳۰
📍
ورزشگاه نیوکمپ
🎲
با بیش از ۶۰۰ نوع آپشن پیش‌بینی
👆
با بالاترین ضرایب پیش‌بینی
📊
نگاهی به آمار دو تیم:
✅
بارسلونا
:
۶ برد، ۱ تساوی و ۳ شکست در ۱۰ بازی اخیر.
✅
اتلتیک بیلبائو
:
۵ برد، ۱ تساوی و ۴ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر بارسلونا: ۳.۵ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر اتلتیک بیلبائو: ۳.۹ گل در هر بازی.
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g5
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/82654" target="_blank">📅 19:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82651">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THfviHbpr0XTivv4tO6wbChe7dKfv3ddMeaWfkiRhtoX13y1_XJrr6bwtNr53bdQO1n7Hcz4Z33dQoXy3ndFbaMpsfTIiX4c9ReTvuovYf4UXQv9QQZFGxwiEgCXlo7q78BT1hSVoCxbM0VQS9IcOn4tiPU9UzvH4pwEQopHQ5eC3MRBq4OlmogxTKOLgAxUDbM3k2FIU1lv2FM4Tk-ItOB_uJMd6yQ19u5P8dQ0MtHlT4VexCX1kdu8hr2IOEepp8mUax3YGuMFppRuNvP7YuF-NPfQS8NNffRFyLfXUKWDMgeMVZzkViA4Q45lxq1W21OmxEDUMFjgxNrHo4oRhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی این خیلی جوکه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/82651" target="_blank">📅 19:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82650">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">listen to demo</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/82650" target="_blank">📅 18:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82649">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lk5xMtyZ9-Y0G4IjIZyZ8bO6y9bfbDc7LfvutOYNL4ebbkX0-zwKy5cwAiWmHHruEq05jIc9spvnTVstR_PDR7jDDYw6da4VA9xa5BLHvft03HUSvl6VQn_09KBvsdxyQZSzsMIN6reqvQzyVUE6BkWyrpEdyWh9sm92_Pmh_JJCx0ZAvyTTPS7SwlhoMK1KT6d0m3U_1dkS5cLlmUvZF4cSIIU-cZjP_Jg-G1a5KeFnF98ZJqzPN6Ud1fkJqaZPvAgtmHf60v2gEQOEdj7qJMYnuecW2Tl6oOsfxZ3Dvk96sP8Lijat6v7Ltl41Ic6uDgM6od4XOHc1-NCpK8u7Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید زبر به نام ثاگ لایف با همکاری سعید دهقان و سیامند منتشر شد.
SoundCloud
🔸
Download
حمایت
@FuunHipHop
| فان‌هیپ‌هاپ</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/82649" target="_blank">📅 18:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82648">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6cb16ab0b.mp4?token=dorecoT_TmfJHg_tvE1tTbuNDw74dvpIRlooZwrRDRQz2uP7oInokph-co1I5gcNYfg7-iHDNLa-K8hYJ6-q6Gk7j-WkTxoAFMUKvKyQ7sI1-l844zSNI2SOkUH9w38AtwwbmS98da_by-f6E1kBFh1rCJqRSo7j_A7VchXpDZqHQ9HP4pgxxZMSa86EX_rYmKvgSECnuBp9QyfNsjlSWGPb5zM7frcmSHqiX26hKgD9l8N4ASFREQ_FyYMdmlb7myi_JBZHe197ys1KPvRa2MkNBqG1k1M3aG8wLaKPwuHCGHg7mff1AE9rEkAd8vSsUgO_UhWKLt91n8PRYcaznQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6cb16ab0b.mp4?token=dorecoT_TmfJHg_tvE1tTbuNDw74dvpIRlooZwrRDRQz2uP7oInokph-co1I5gcNYfg7-iHDNLa-K8hYJ6-q6Gk7j-WkTxoAFMUKvKyQ7sI1-l844zSNI2SOkUH9w38AtwwbmS98da_by-f6E1kBFh1rCJqRSo7j_A7VchXpDZqHQ9HP4pgxxZMSa86EX_rYmKvgSECnuBp9QyfNsjlSWGPb5zM7frcmSHqiX26hKgD9l8N4ASFREQ_FyYMdmlb7myi_JBZHe197ys1KPvRa2MkNBqG1k1M3aG8wLaKPwuHCGHg7mff1AE9rEkAd8vSsUgO_UhWKLt91n8PRYcaznQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاره شدم
😂
😂
😂
@Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82648" target="_blank">📅 17:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82647">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">محسن نامجو برگشت ایران.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82647" target="_blank">📅 16:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82646">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">محسن نامجو برگشت ایران.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82646" target="_blank">📅 16:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82645">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73b53927e2.mp4?token=PJCLGtl2nDW3-DnwYd3V4PoryWTSzqVrzGQ8U4nIiJbkdYZeZ0p0qvNgWNke-I4DVe1yGig75GKJwCIir0tggfaAWbKRPWOgYIixX4sjlfsAlmomqAo_L1xch7lqJc--J5dm2azmbM9F9NPDyBTU2jyJLSJStc3Je_UAxPKIILs4vUrEsXq2ZRSq-eYNs4k9Lt6tzE4S9cqn3OLf-jr5AKkEh0pjfwUgwnSm_cN5LE0nYQWJRYr4sIdGurByQpxRnbpq7wKxYj-PWEYoER5hiyxlrfHT7PHqg-HXrkg3nikGqJX26VBnmm-aHT1mR78esFLotqvAasWDiDI7CkTDag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73b53927e2.mp4?token=PJCLGtl2nDW3-DnwYd3V4PoryWTSzqVrzGQ8U4nIiJbkdYZeZ0p0qvNgWNke-I4DVe1yGig75GKJwCIir0tggfaAWbKRPWOgYIixX4sjlfsAlmomqAo_L1xch7lqJc--J5dm2azmbM9F9NPDyBTU2jyJLSJStc3Je_UAxPKIILs4vUrEsXq2ZRSq-eYNs4k9Lt6tzE4S9cqn3OLf-jr5AKkEh0pjfwUgwnSm_cN5LE0nYQWJRYr4sIdGurByQpxRnbpq7wKxYj-PWEYoER5hiyxlrfHT7PHqg-HXrkg3nikGqJX26VBnmm-aHT1mR78esFLotqvAasWDiDI7CkTDag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن نامجو برگشت ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82645" target="_blank">📅 16:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82644">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پاره شدم
😂
😂
😂
@Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82644" target="_blank">📅 15:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82642">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MSSzw5faMxt7hBDpCidnkoxCwHv6mccWzxWo5tzhqhTlLEMTppRsW9WNaVT8nNW1uPimz7P78xpEZbLDsWwzUH96fYioSSFCqz0hWE7pV82i_-zMafeX6B3LG67Xp875AswyQiIeeY_qkWY-OPXJo73_XMsS40Jp60ntf2tRZfy5vzhsQPjRjzEupg277jupguYF8qghqFYHN2j_jPcQu-dOLJFnaJta0kYmcV9eOZycVndXYPr6-1rO28hArmSL7tpkmTGmvwhdsjA8X72f7cWpp8JVORhf6aZo33LAku_RLHPOSNpCOFhrY5IO7l72_pn5MheghqVpRY6sq3152w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eZvMiOlDOtkz_2zu32LlozbIp8NZXIStitWng5uHEGV8swLros6CgoKmtrPLtRCypsY2bPShaMAtEyc5jrcXCaiE4bPeHFSClkPnYGIw4fa2YDlqNMzDcMyOBEfSjmq9sFXDJU1N32As4Jw2MG8khbV9VaII81-mvrFlIvz0ASMJAAfGmQlq0QEPhM1k5b8j2eoj-TSFNFjaj3eWUmFSTq6fW-YoFtkbCS21qdKBlukV570v4nRMW22It7UkttQnbE9Rn-tNt5_TXWabXGOlMFs5Lff_2fKuly0VgVfF7-tARuzVMzDJLsAPQtkCQhBg3kXJfEUOPxTbV8PbExVdmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پاره شدم
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82642" target="_blank">📅 15:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82641">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33d8214fc7.mp4?token=AbAGTDS2MtJNbGnqN7TThOBMHrvDjoh6pGzJB-2pUzQywDzQ8HwYqAjALfiRY9l8M6tpxLtEWNaHrcXdKGbcdgqBgB8cfvUYtighXTPyKIFqEH8yI-hkadc2zE5f7iRJFmQYz6swXuu2cVs5cwvBG2l79OOC75CUvpQcfUrvgvYCabui5JyLTIqnOzNVpoHlYHG4d8QqMEtboOVbrpOMq85TsppKAcoxyPhovvvKEVrJfeiHIrdiBp3o9CzKIuvCq0bghj5VoUsM3rzYXQW_t02w0pk2xRclZy9rAIvsR3Fq_-4SycJekh-8-WXasPwxLIT9p1aQFWyP_ZekCH8lkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33d8214fc7.mp4?token=AbAGTDS2MtJNbGnqN7TThOBMHrvDjoh6pGzJB-2pUzQywDzQ8HwYqAjALfiRY9l8M6tpxLtEWNaHrcXdKGbcdgqBgB8cfvUYtighXTPyKIFqEH8yI-hkadc2zE5f7iRJFmQYz6swXuu2cVs5cwvBG2l79OOC75CUvpQcfUrvgvYCabui5JyLTIqnOzNVpoHlYHG4d8QqMEtboOVbrpOMq85TsppKAcoxyPhovvvKEVrJfeiHIrdiBp3o9CzKIuvCq0bghj5VoUsM3rzYXQW_t02w0pk2xRclZy9rAIvsR3Fq_-4SycJekh-8-WXasPwxLIT9p1aQFWyP_ZekCH8lkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82641" target="_blank">📅 13:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82640">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONJIybF0RkXFCp5aODlIq0Ac2kzZ1jDthQjXlqTHcKEz1GGwbLt7UEbBC5m_bvGUeQXUosCu4t2xBvZx_9BgeaN7LllsU0Bgj0aUlJ2Nky_BFP4q4ftAxkdEnNHXZ6OER7gqwiYU0F7zw4XP5FBjCOBaDxxAwHnkbzUcSJlVs8RlUL2FbltmlSHvJjPT093nPbcCzZdoKHt4Z-9lcNcjDEYQJUFbtgRLw17_qvxqWJZxzFyvYKOXAiaiZJtaoAm5tn33YlMTZWtkSU6ZwRf1dFMe0npjldprH9luie4ejx-P7GLNXhmx1EpVHEZwYp39cGrOcEDjsfXU9H7DXcsqog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی این که چیزی نیست، پوری سه ساله قراره پک فیزیکی فیل رو بفرسته برا خریدارا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82640" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82639">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgrCBYphSZA88MsbLD3d1xX7vMK_Aq4AwWHd3z_aUVNEG_qReZJJhI1b-n8IWsPAZWD2FJhtW2jb4AX-W59FPi7yqekjwWeW5OjYStwEdb0OopcGnJN-HE8furqjPouLGuBmsbaxTGVJiqiphVjmREe-hfQKN9IQtRZX7GldsNuEmvEm6c5ZlRfb-92JVb-oYKp4vb-wfqmyOOGjPj8JLwnXZuOSmEYnJAVxpiGcl-FLy84yFRORheLtP-ivC-ZdIbz_jolGJwuqwi4rbOw72nnD0qJKgXg9yLt-XhVBGcLjgFi66ha6jiBEUe-8LjYxfSy69VJ74Of4QZXLZPV5xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا میدونستید راب استارک تورک بوده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82639" target="_blank">📅 13:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82638">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سبک جنگ اوکراین خداست، اینطوریه که ما که چیزی برا از دست دادن نداریم همچیمونو زدن هرچی دم دسته تو روسیه رو میزنیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82638" target="_blank">📅 13:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82637">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آلبوم جدید ویناک به نام "Concert Type" ریلیز شد.  Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82637" target="_blank">📅 13:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82636">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGBy6oPCt6RjApUwYe5NOcVKr4bDcj6bzwVaihByA3TeI5QwwmN6rID5UvviyjWJPE3FqZZusmRCg41JwZR7PzY2wp8kGmLRKqjsDJh53kS1bzASJzc59aXtxWR2GwkQGBMF6abayNjRehN11W5e0hCcEFv0Zq4VK5jMsQNbEIdQPrhuVNZmPmP1f2A839ERF4LT-dA1KEt659D1YouPzEJwwzMUKgcf3926zC67IeBNvOOojSxSltnYcIvHC5uYKmpMaYBMajEgVgadXKEOXlQmMmB4fTR4Rxj3gNKSjvlYEjtGgOd7Fs-VPlxL5JG6_ueFO0JkxlaJ8JE2kMsnIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید ویناک به نام "Concert Type" ریلیز شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82636" target="_blank">📅 13:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82635">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خدا برا ماهایی که تتلو ۹۸ رو ندیدیم محمود ویناک رو فرستاد
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/82635" target="_blank">📅 13:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82634">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d048ddd9f1.mp4?token=EpIblSsy-m4U8lddWa6mx0kZB0-_USymWzzmttjm0p3qgTEjT3dHd6h29vIFhUxOcz_pT4tdFdHQdE88IbzZLVoNWsdnnehCZErGy4ghbo2hA01lxlG4mc3oEnGQRbtrYBFEsB93SypP-eP8NF9-j7Qm1tvzpJJdFSmE9ofdPz3XfO3H_f061T0d1irIjM2di2L9QOzaw-gQmbbJ758lzr_DQg-0PtoY6dO74dnWX1cLoFG1i2n_mrigtE1j4L-GaxsQRzmfV1SmBJB6N300ql2dLrii7FPxQ4kBg4zce6gEkbBNY5hDpycBNmy6D_420BtmUnQIhHQbl2IVbIMTEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d048ddd9f1.mp4?token=EpIblSsy-m4U8lddWa6mx0kZB0-_USymWzzmttjm0p3qgTEjT3dHd6h29vIFhUxOcz_pT4tdFdHQdE88IbzZLVoNWsdnnehCZErGy4ghbo2hA01lxlG4mc3oEnGQRbtrYBFEsB93SypP-eP8NF9-j7Qm1tvzpJJdFSmE9ofdPz3XfO3H_f061T0d1irIjM2di2L9QOzaw-gQmbbJ758lzr_DQg-0PtoY6dO74dnWX1cLoFG1i2n_mrigtE1j4L-GaxsQRzmfV1SmBJB6N300ql2dLrii7FPxQ4kBg4zce6gEkbBNY5hDpycBNmy6D_420BtmUnQIhHQbl2IVbIMTEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82634" target="_blank">📅 13:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82633">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">عجب چیزیه پشمام</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82633" target="_blank">📅 12:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82632">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ویناک دیروز اومد گفت این پنجشنبه ترک نداریم
شاید فک کنید خب ترک نمیده بالاخره یه هفته، سخت در اشتباهید چون آلبوم داد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82632" target="_blank">📅 12:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82631">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ماشینا شمام تو تک استارت روشن نمیشه و بخاطر بنزین بگا رفته؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82631" target="_blank">📅 12:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82630">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اگه پولتون زیادی کرده بیایید چنل بتم باهم بگاش بدیم:  https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82630" target="_blank">📅 12:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82629">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اگه پولتون زیادی کرده بیایید چنل بتم باهم بگاش بدیم:
https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82629" target="_blank">📅 12:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82628">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خبر خوب هفته علی گرامی و سجاد شاهی آشتی کردن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82628" target="_blank">📅 12:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82627">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7ff60b305.mp4?token=BT3T4lb-ayzINHpKjZGRhjU0uUty1mL11ieDcQVBDnwSU5iAnPOlkETt7KPY7uSMXXOmpbtxKfoaZKz5Dg5JxHr8aW-219v3fHO5iBede1zET5cwndNcKN2NF04SK4Hd3s7hIqMUdRoNGyQy8iCR0iwAvOxK49ozfuzhwN9OIHuysNwwNbLCcAUcmlYfRP4gO8eHP2XOQYGbXwJlQeN1TaEz69Ioxai71s47lRmEDWeLJr0W5JHVNzePgQstlddvZ9iZCAUxRSplcZtkkjQWzLcNu9a7O3iHtOepLHsbC7dx6x7vWrj_s4rHOOTMPkUPhhwV_1i7WGfHdStRsA7n1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7ff60b305.mp4?token=BT3T4lb-ayzINHpKjZGRhjU0uUty1mL11ieDcQVBDnwSU5iAnPOlkETt7KPY7uSMXXOmpbtxKfoaZKz5Dg5JxHr8aW-219v3fHO5iBede1zET5cwndNcKN2NF04SK4Hd3s7hIqMUdRoNGyQy8iCR0iwAvOxK49ozfuzhwN9OIHuysNwwNbLCcAUcmlYfRP4gO8eHP2XOQYGbXwJlQeN1TaEz69Ioxai71s47lRmEDWeLJr0W5JHVNzePgQstlddvZ9iZCAUxRSplcZtkkjQWzLcNu9a7O3iHtOepLHsbC7dx6x7vWrj_s4rHOOTMPkUPhhwV_1i7WGfHdStRsA7n1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر خوب هفته
علی گرامی و سجاد شاهی آشتی کردن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82627" target="_blank">📅 12:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82623">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vjvT03Emur6wEIGxzvNxFGaCNVUdpauDBTGUnauSMQ7Pazji2DmUwedMoQIERawB721S4jtvVu7YzH-hcxeswY8JzBeRxW678t4DZD_92EGFJqRQocC52ZembXQrEPgz6cmQqy57zWf_7mWVI7jkcCBzhbuTUbJ_MMaiqL6wbkz483pbpGcJPVlfB8kThTWeFgav4JPwZvkQH83auucKxSl70K1Vp7_WXj08e5c4CtlXZaZQVDSny0W1HuoPh8wuBQ2f04hW4HujVRHh7IXuLlY1Yu7ootfh673uQs6pBj9_3lxN30NLH7tWlEqoCyvs0lCMyD119yRvBSUqhuqe1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AmA4qkinAJSU1XnVUH097bfx1XL64FH6JUgLSxNRJJUbWtqY4Xg0azSYmggQLjkN8CKeia5Gat476LIZnls_5B-tUrZNJV7-ZrT_LEcrKYF3uYFuOD22-U7y0NYtIyJ_oSr-BcWZN8r8O3MlmYQ77EVWc6KRN90r1OXOCXJKUmRJXof2hT5YHJ3veib9evVH1nwP4SeCm6Qg0VSmbJCYKnhojW5HmcNSN6Cys9HkROLSX4KDiXw_fdfaUnFOc0p7Zp58o_DcM5PLvdq6k5KHv4QIvBINzp9iSEeYzKo-lBwIlZzdvzU37irCRL4gAVtCRoJjNLhNJGzqYCoaUsuOLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GM966592SlyU_BWDDSpFbhq7EB-p80A8oovPKLWDLX4eoy4C89l-WsuvYGwNcl14GjNmCqah4P0AHtDlCfFWqE2d1CfWpFwtk7AJ8ptQXllM6MAcOW5E8mYaQ422AsJUlR0eQKWvOYgE11OzNXKYSkF8lrpvTBRle0-i_iTd84yPuq5anYXLd0Xei2iGCtbOoDEJZB32elCPQzzCUF0lr5e9WYz1Bt9Kb1fYXUYb11uFD1gSDyXhZ-F7STdgBnrPM02Tv7faTIa2-A0RZWDJP0AmP-1PVTGV6ggyrdXv4ubD6D2ZurUbySezszMsM3wEoC6rsbUrttNVLUcLKEdHGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oUS03ccx0xDJoWsC8FgM3_LbKrd7hkFIPG2W3f0i3C2y1RGSn_bSS3A8Bc7Ljr-PvbtrCPygAEXso3jZYjQB7ekv3O7Iop36FX0u-ygavtqwemEH4ocYPP5zWfRsdARZP4HUW0Qdkd9Dqu8meW6AgO0Z5AoRVhgq44djp0ppJwFfAYkQXUIiBtcZqq6eipLmToXtPmLj5XX4d7XNyJqtjnmho0x0ewmZo563VbBJXkVKFuzr1QgnKqPVEm7-dzirarbtIEvA3HseJ-lNMYF0iDGiwNdkI4m_4pY5CyzjJKCxrZW5BiDXx1dD_MdKZtVyn9MjP9C4EoI9mj33tfLlsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ماجرای ناپدید شدن دختران نوجوان در تهران و کرج
در هفته های اخیر تعداد زیادی از دختر های ۱۲ تا ۱۸ ساله در مناطق مختلف تهران و کرج در حال ناپدید شدن هستن!!
همچنان از هیچ کدوم هیچ سرنخی وجود نداره و طبق گفته منابع خبری احتمالا بهم دیگه مربوط هستن و ممکنه حتی یک نفر پشت همه این ها باشه!!
زهرا متقی ۱۲ ساله چهار باغ البرز
ندیمه اکبری ۱۵ ساله پرند تهران
هلیا عین الهی ۱۴ ساله پرند تهران
زینب سون قوریی۱۷ ساله پرند تهران
آنیتا شفیعی ۱۵ ساله اسلام شهر تهران
پرنیان ۱۸ ساله فردیس کرج
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82623" target="_blank">📅 11:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82622">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ddigia8IQUI_kg-OfCx4k2LST23YEZdqYMVHlaQnkSRlvmhTSD0eu8FlFCo7rSxe8I3VY4zyJW7AQ2G6M2K_SmaCCh_5tdltZdeNkPhqwiKfTAkV2mKxVCG3AMf05QtpcbLjJAHfJSm7RoLfmHt8N3jEz5YzB6ZtDYqVd4AmrRyPWHabZu_tLVQnDhCJRqMMy4lYdsmbVR7Do_CIOk9EblrKjskPkn0hyLoMqNrnJHd27weFeKTpzv4UlX-bezmbTjHAq-o3BejRJozejl3L0-9LGQToB5xFWaOxhP68lJt2Bgk_BQhIzcTjI9_HMEMEPI9WU5EbHvIt_xSJ5ep6uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بارسلونا
🇪🇸
-
🇪🇸
اتلتیک بیلبائو
🏆
لالیگا اسپانیا
🇪🇸
🕔
پنج‌شنبه ساعت ۲۲:۳۰
📍
ورزشگاه نیوکمپ
🎲
با بیش از ۶۰۰ نوع آپشن پیش‌بینی
👆
با بالاترین ضرایب پیش‌بینی
📊
نگاهی به آمار دو تیم:
✅
بارسلونا
:
۶ برد، ۱ تساوی و ۳ شکست در ۱۰ بازی اخیر.
✅
اتلتیک بیلبائو
:
۵ برد، ۱ تساوی و ۴ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر بارسلونا: ۳.۵ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر اتلتیک بیلبائو: ۳.۹ گل در هر بازی.
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r5
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82622" target="_blank">📅 11:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82621">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAacXX0KLYY3sIL7Y4v5qy3LD1YCujf-ClKI59wmEYJFIg6QEbzMvBxZY5QrdfINq7DG_wljKaBMzyi0PYxmjvEJlF2104ZA_QCoYbrAP2XKCobOUL3mbvqjgIR92ap71dF3oN6Hec66-z-C4cnn6BVt2xHnqHUenCbnLmk1ShiGLNqUIjq5DblmvKGucPnUxvI_w8hY3HfJ4_H7-nu_WWkOPEzci63YiI44LrPdBXqzlX7kP-6Hog9ER5hNXCJ7Q9NK6IiVvtafbF53T1uXbirPDjw3MPEyufSsov3QQfEmwAFzP2X4GDvKXXQTK2ROrAlE1DS1Z6hZ1fnQqe6z6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام صبح زیباتون بخیر. 8
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82621" target="_blank">📅 10:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82620">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">هادی چوپان به دلایل سیاسی اجازه ورود به خاک امارات رو پیدا نکرد و نتونست به سفارت آمریکا بره تا ویزا بگیره و نمیتونه در مسابقات مسترالمپیا 2026 شرکت کنه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82620" target="_blank">📅 01:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82619">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">امروز 4 شهریور زادروز کوروش کبیر بود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82619" target="_blank">📅 00:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82617">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Mehdi)</strong></div>
<div class="tg-text">رئال جذاب مورینیو</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/funhiphop/82617" target="_blank">📅 00:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82616">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY3GTT6X4Ha6jqSoj27ibcBH_p0-nwLAK7mLhfYkHakpL-ioHp75qWKgBbsneufh6raKbFI-f38qgMYbaggiWd9zh-vKQAy8XfKs3YD9cLztlr_aou_FXKypUFHZ43CeJ8ir4cfBwFcYlx_-DwwduUXbkZYnH-J-RVU0MFtT11SbROgppTRJn2tocUMC0k_GyX19Z7KQJJl7kUZuJRmX7Qf566HGF0Eo73jLnL4UVbg-yutENJv-h6whXzyLoKoGKDztKx57IpIKxqljOgqr6ezrD_eAmrYAemxRqki2lPdHli36PwVFfmMZX58HvlPu38Cx5NOxLtq5ebTu6g_VvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه خدا لعنتت کنه با این جوک بامزه و سکسیت، حضرت آقا شاهده که ترکوندی شیر.
فقط دفعه آخرت باشه لطفا.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82616" target="_blank">📅 23:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82615">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RO6en1CWCxIUvuI5PPZlwncZYZAxPo-NAF1Y3E4OPwtdmlBcOpK1wuGwTWitX9izKoxc0gnnsJP3Zk0T3rdS8m3Y86KSZIq93RHilGjEmlaWeZ97oKc5770J2Oeq31_N98Mw2SIckNCGLzG83Q4f35M-UyqJBV6AKeXUoeIW0GFxqeVuSXLRAvKd0vBNjE2IA9IhDnC-MsNwHATikKo1DKn6-ueNxmYLGAKqyiAeAJWNIxHpNPfJ7FwW_z9o2aEI53fzxIbUtHmeERU7QSR27UO_NSY--Al3BP1q9vBBM4jtt70oRvMov70V43S6vPrwv1KS_ivymjqWckeTeNp4Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناراحتی دیامونده از بازی نکردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82615" target="_blank">📅 23:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82614">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رئال جذاب مورینیو</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82614" target="_blank">📅 23:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82612">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cisT85lYso3lVjSIqZDGkF8JCqPuVxSMBsNMGzUqWNgSeXsDEf2jkjgrbLQDnQzjbSEJIPbplpv9EFu0QH6b4kREs-4_xRWKkDcKL_FYEEoj1HoZ9vWmqu_WPNKPPO1GweoJ2DbWK7eXiO7qKAELmj4gyWmNy1juq1ggEzuR4eGuqfaKJfpjBWeG8lREtuILVed3dlPHRvmSwPkXtGgHVey2q-gCsa7ERpE-kxg7xPLDchu6zU5PPAGa3kdkjTWnYghLyrU-_3I5EsX8nBFM0SwORbYksDnQ030BRX8KpfLD4GfUcLDWvXxqZXL1US-63_K-KKIWzgps_43Kc5Vtfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه فان هیپ هاپی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82612" target="_blank">📅 23:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82611">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuNrEeXg81UgxADuz5VPmaGM-hRMGwqvKNzMmfccTka_8KLxiVDH_ytaKY6s2HSj5F3kwC36sb_f0MtOaneYZlHYUm_IzuAPT6Z0Mylx0Udn-F7HYYf8z6InfZdlPat5_AV5gDEblDIrz_KUXm1DBeDjgk39KPGTemZ2WA-RVcepz3Yhxe_0hR0KODQFQKEOEruiC21I2NqP0eMGLfO2PuQn6bh2wepZ8j_gqma_bb3bHIf8i7H825yDw5lkbw9M4TzKHVvG70ynvhS95AprPxGF8lNBXKA5NCokNWgMW5S3g-pieS-eN0aoNaGZsPx-_P3ZhaAT-fw9DtNT9OsXGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الهلال از وقتی یادمه داره سالی سه تا نوک میخره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82611" target="_blank">📅 22:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82610">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y82PMFBcv7WXxO9GJpmReuR1jNrlbbr-4xMsXboTg6AT6sgkc6wNIKT1xI1uh6OUQXYX0abRLdC8Tfec4BbXeq90q2ZrFgHey68tO1tfhDOq769Z-EqVUU3xK0lFe2ytOXZD31I_mQ--zQISuhwrKj97e4eH9ZWOhTPj1KpB-J6--DITXsoIs3d5XO-Kas8A2gVcS8qbuJL7RjVnvmydb2dO-zpQ13nYNND-U-Rd38Qau171vtzt1ITsK7Si5XGYVg-oY15cVxSzMD8bRVGxsWWjipki-JNlY2JbsWQrOarhanTQgitX5YnFDymaqEPL8dX34uMeKNmPVk_KWSFNFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت کشورو ناموسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82610" target="_blank">📅 21:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82609">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_lsX1CCb_mKkOI3KEgUOM88e63CuxKkzdaMv3PJzXla9b_yoa-nzrZjVQyWEYkx_SxndDkWYFXTwhZs1OIac6_sng_KQppSAmBbM-m9HYyUFA5fGl1HvwgpKr2fBsZ0AD7V4WGnh7jPlfIwpCR3AdqtulwUuA-XPQ5QhyGGb0pfQIpGqwCA_2VE9Dd4JgnocjqjwOTM0dFIjtLEq2HoIIwu9kMdlVqN5wE9T-G8SrEkQCDYw3oNGIypkfgTgtGTYNZWsHihg8IHXQbYV1bKNd8i1BCSYaMwZAZwGqXWUZ08nLsQwqcRsuIZLAGJcjNoSlkWx4KdlAVUEtAvXnhMDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس یاس چی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82609" target="_blank">📅 19:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82608">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a262ee6c0f.mp4?token=HKS1geZi1d9NCTNRIsDdifyxGnfFw__lwBiHerB7P9UoDRSiEj2Qv4FY1-I-2nEVm2H7e6UKSuyxVmVQ2RQR22cRoqkz6uNWTrSLRsinMQHWBc0kNegXVVvm-1UfBbiTOlLrcRkGpx3Vh2dST3f-ZwjODm-CsEqko02YSwt2LVnRng7QRElmxx1s9ZAfOiEuV2ljjAxDczHpEC_Vk_lNJ9sjmXXjo5F0NTs12A3Ye7eMClq8XZAvRWAosCnCXomeQ_-u8yG-l6Vi0yTPTAV29x0Kc92N8j5jnqdGIgvmJoUY7f69l5hjgsTewaxFV3vj6MGBQTLs3E-zvjHN8o3jPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a262ee6c0f.mp4?token=HKS1geZi1d9NCTNRIsDdifyxGnfFw__lwBiHerB7P9UoDRSiEj2Qv4FY1-I-2nEVm2H7e6UKSuyxVmVQ2RQR22cRoqkz6uNWTrSLRsinMQHWBc0kNegXVVvm-1UfBbiTOlLrcRkGpx3Vh2dST3f-ZwjODm-CsEqko02YSwt2LVnRng7QRElmxx1s9ZAfOiEuV2ljjAxDczHpEC_Vk_lNJ9sjmXXjo5F0NTs12A3Ye7eMClq8XZAvRWAosCnCXomeQ_-u8yG-l6Vi0yTPTAV29x0Kc92N8j5jnqdGIgvmJoUY7f69l5hjgsTewaxFV3vj6MGBQTLs3E-zvjHN8o3jPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر خوش، نیما تکیدو آزاد شد
❤️
💘
💔
🥵
😱
💋
🔥
@Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82608" target="_blank">📅 19:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82603">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PjukXUp0Utz5ri6xQiLtG1Y7RjvVea6WFpumRxcE60PjlJ5GtffQlTbr2fP4Fwz5ijCgxbRMRs9SHPijruWWZfQhCbpdI_e6EnCWSaEO5rOSflmH7eDXcc-b89hYGMpEpCzEhv2qlFxBKa1p3ErFBFGnkaT4hVH3ERHz_IpwI6Gf-l7eBLnY6YctcTOMKzR21-izbxt2QtUBIvzak9oSSd0excCiXWXsiitiE_HaO5FevlT31vKXvFQQOgzosU7xe6uLZNm5oOdJkupF-g9mqip_YZqify3GJACHARqss5w2tLJyPb3CwAm0uPO0p5eR6rWKLzBvT4h1rgkUcnWi-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n8LHZmBauYDWrpF5ZHmoWuQJnWYoQds4EPVK9IkvU6o63Ok_LBg3ZbdR7ymmE85n880CNlqlJArJ4lvq4oMBaOny1m_rAL8wcBIEd8ISE0qYxXYIkgp8V7zl1pwEIWt1Zmh1v1TkIg4C1FMvj7dRxtch4Mp7z4bnJCztBdxHNYXVWG4bgOBuiYomOvjNgIdzEWw8nx_V7LpWvO5pwsnRb_j91MSf0S_2IKPx4B60h7uqPk1nOUnYSePs5uvfoHr546fBNI-cMy_kHKW6zOVUQfTF1ykiHWP88RYlZYR712EsLBWl4ru28Meyo9A2ub0IxxT-Lj2JeEVivbvtp2jXHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BsPDHKNsuT0n8iVD6Ns-_ThKyDliM4-rhewkVnB6cK_RzbStMNsSYN8HSPfHJbenYqs6BMhvP9VdtHO4tAyzUXFxDeD_UYH1rlyD5D4wed_qgeWoSRJZagxA2CHdaAISo8jCy6LV-TNpemxgSN9VoRghbbieCId3PdJWcAsxOfxqmCaPZaYnbjQt8uEfBbIfjJ4eBRSCj_BAM5LYcv2QwrAAe1G0AcvQbToSD8CCeO0ypRPUcqx65d8VrOdcfLmRwdw2t3Ol_R-veP-UXkoplgjEYZW2D6VlU0xmX5s8I6Z9oBFKrBq6Y8pZtDYzbTgZtZAf8hos_dmraCm_BLuulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jR9QSbkh8B02_XaLOH32SQEiPjWtHUuwhM57uJ66qi_ZYM3GD3wsyY-VCsFmmZnyTfG_2K0KZcJN8j8rGZeFOdCoTwdPz92__w1GAFn2bIuJXX2DTYZoyYMbTaGXzSjcvVfFIlLUreG3pkyucKVsuPr2gDVjljSCuz2jzMdVHFyBIaMCKAXTixpKtEJ2eTrUxAEejUQU2hlK6cCx9CFAm-2Lr_nX-DGxphbkWh-H2sa7iJqdckMssF7qG5F2NC1dDZYz4J6TL9TlUDi-6Iq7qvwyT92HPLLFt5p4n3nuo8STNfpt7T1eAIQo7NrY-7w7p-lHEbnS9CCsvEUcWZDFdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8d5151d06.mp4?token=K09YHvSysDd25kZ9L3hPX2NA5RfAhx3-0oJh7dHnjklbkVp_fzrb4iMxkRXkk9P0-zZTg2piDcB_9WFQCwk6lGH0hA9x8FXakxi1ni5KPDtWql3fvZr-3h2-aRdgs1FUpDxZrWJk7-c1Q1CJIJaRD4bPtHStDDSsdO8UmmtCqrM9huwitQUqVy122Eboz0eVn_WnH-vD1v_Okt-NU8N4LMmigsUG6lqBX9LuR1h9Gy6UkxY7DAB7D-CmFUm0ZUryekTMQTIFG8NOQx1yG4z8zRdUQ0rrUCzqwYxertTADSB6JRREodkXqC7wPX5Zst17iajGPhbyunae0zSKeBVm9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8d5151d06.mp4?token=K09YHvSysDd25kZ9L3hPX2NA5RfAhx3-0oJh7dHnjklbkVp_fzrb4iMxkRXkk9P0-zZTg2piDcB_9WFQCwk6lGH0hA9x8FXakxi1ni5KPDtWql3fvZr-3h2-aRdgs1FUpDxZrWJk7-c1Q1CJIJaRD4bPtHStDDSsdO8UmmtCqrM9huwitQUqVy122Eboz0eVn_WnH-vD1v_Okt-NU8N4LMmigsUG6lqBX9LuR1h9Gy6UkxY7DAB7D-CmFUm0ZUryekTMQTIFG8NOQx1yG4z8zRdUQ0rrUCzqwYxertTADSB6JRREodkXqC7wPX5Zst17iajGPhbyunae0zSKeBVm9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر خوش
،
نیما تکیدو آزاد شد
❤️
💘
💔
🥵
😱
💋
🔥
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82603" target="_blank">📅 19:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82601">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27e5d7bb63.mp4?token=GPqPsc8Md0Prm5tfJwitCAKvpU2kMU7U1hkPPiMeW724v7oh3oq6T1iV9GibcNtY40TxXcNUXMgafL-TWodAs_eWEVwEYK61ekx0-yX-Lkje6U-5n3JkkdaKJB956XZpXuOhPrEM-jrwQeqNx9N6ja8OyyTr3dt9_p7QlfRzaAdEEyUzCzsNQgZ8pCzfSRaX1ghydRfHZLYKfUo6N9MVQa7eLrnSLpARAp8buvN71CcXDsgbBt7viWWgOj636u0TQ00-nQLyAwOJLzi896nTZIodW8uuvOrq1Y7fEZe_xkktvBsFtnxt4an7zTl1jVwWmhdF3PvZpbKG__6NDsYdjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27e5d7bb63.mp4?token=GPqPsc8Md0Prm5tfJwitCAKvpU2kMU7U1hkPPiMeW724v7oh3oq6T1iV9GibcNtY40TxXcNUXMgafL-TWodAs_eWEVwEYK61ekx0-yX-Lkje6U-5n3JkkdaKJB956XZpXuOhPrEM-jrwQeqNx9N6ja8OyyTr3dt9_p7QlfRzaAdEEyUzCzsNQgZ8pCzfSRaX1ghydRfHZLYKfUo6N9MVQa7eLrnSLpARAp8buvN71CcXDsgbBt7viWWgOj636u0TQ00-nQLyAwOJLzi896nTZIodW8uuvOrq1Y7fEZe_xkktvBsFtnxt4an7zTl1jVwWmhdF3PvZpbKG__6NDsYdjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از یه ایست بازرسی بدنی تو یمن امروز وایرال شده و مردم جهان که زیاد با ساز و کار خاورمیانه آشنایی ندارن پشماشون ریخته و براشون خیلی سوالا ایجاد شده.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82601" target="_blank">📅 18:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82599">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ow4be8K8Z2KzYKXFLbbL9EWteMZZ6gHeyCXe6iBcWAHmxNDh5aAnkkB9bbdTat5DnEG2F4HG_qJEpllXCT_Cpx-J1IIPgWykkoHqqcPbYAsxsBXJ1X9xK_7dAf9DvGqMvCbexKtq3U71dmXYv5lgYnzoHTo8rb5IQAA4wOsmbOQaVrgLuBqMnt64PgISNSEE7bHzehjkOcSDG9m4IO91eA08tuJyJcK7ABI_ux8MzhGIfs_HbzEhq0jFXrqn5wFPNmz5fUWazDOxfn3f4qiCZNE1R79iYApTkEm-X5hbtuAACArYfBS8UUItwDmQ681am1Fi_RwEMqsqgfWew4d8WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bPif6YqMbwXjzqaJCygvy2yecRh4hnH9Gc3YRyANqSRCYiPPbEjxa_3ET-rwbeG-g_Z_5nhi1l7jdtshRi0V8Jz2mCvE3z1MNScfLbqEwGcpbx2z6nMsmNdqb9C9oaft2PDNRbB_Ni3u8dQY4TfNX_uQFurQHJsYb0RKAYiyMkO-Aii-6ciw-2DW0rL4JftZ5jY0AQkWJMH-mRXgH0AVWJbaSIrwfuyV6YuY14mfQCNSGxsuzaBChilWiUJiW3AuA6fO6N-uew4nO3HN80I-kz31USWbWF_0xu4BofHw5G4rJ2yUvPfyDd52j2JApW0zZTP-12A0pq9J9MXooS4EFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هالند با یه مو کوتاه کردن از غول کصکش سفید تبدیل شد به کراش نصف دنیا.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82599" target="_blank">📅 17:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82598">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">قالیباف: مذاکره با قاتلان رهبر برام افتخار نیست و برعکس برام خیلی سخت و امتحانی سنگینه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82598" target="_blank">📅 17:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82597">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ریدم   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82597" target="_blank">📅 15:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82595">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تو کافه بابک زنجانی اسپرسو ۷۰.۳۰ سفارش بدی ۶۰.۲۵ میارن برات
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82595" target="_blank">📅 14:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82594">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efhKz5jv7pD1AJTgeGlMvnKpz0FNxDByKzed3X-Sea-ryPFcl3DP8VTirJPXzDZYeAW7MZABGEZIOPfzlns-xB6Tm8k2S1wE0fNR-T3ZQgv71BUbDuAiIh8ZsbF-D4JfTu8pW8Y80u0G7mSuLR8ZvgEXjE9pBHr1VGdsmEEls0co_4glu1dG3kSwxhTnORTPLPQRlh9hQ96IoICLFrQctqCOKEe3l143aUTt3G8wkVxOxKxJ-DaT06T-PDvrMBzKmAsaM9RBWJ5ivu-6sU20fMgZyx9GBEvM8IiyIMeqp2pxLqehfON9EKb_1OeSiM4l-ExnnCUUiX4Q4ICY-UyWMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین و آخرین کنسرتی که تو زندگیم قراره برم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82594" target="_blank">📅 14:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82593">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">این پیرمردایی که میگن روزگار خوبیه، ما قبلا نون نداشتیم بخوریم ولی الان همچی گیر میاد هم دنیای جالبی دارن حاجی</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82593" target="_blank">📅 14:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82592">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4y7zdo0L0XHQkySX6oEo8Mc_OY-DkxvcBZH52Uqsk65K2COdDZ0NlfYfC-aC8g3fvposyteo2n1n62UZQ3V08Rpmtm3_UNRmduajOIpA1pVtC0wNp4Xve8VCPOiiFFQtF2drF0KlZng3FHxePlV6cvR6NIEaePXHrkH0NZLBZwisyma4fqq41MNsLy4MYCPweYi1iahF7_LS8UBRWwf00PsRNQU2FAKrbDmbBD-y85YWo85cLRiqzWTZ1XpmZCcU6b_bOmqfMS6EsjnDDjifhpzyeXjfPXDPgCjAjI37s2zGPxjrcLGVNsY4ihmMjxl_oAPB0A1i6uYlTS09cVO0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها بین این همه خبر بد و ناامیدکننده بالاخره یه خبر خوب آوردم براتون:
قرارداد سفیر برند رولکس با تیم ملی فوتبال تا آخر امسال تمدید شددددددد
😍
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82592" target="_blank">📅 14:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82591">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slooChB2tg1ciOrHCw3ol1k5Uhw6ZW-QC1sfwmU__SgmgoT-uhE3dpWqN9TPBG-RNStupziSHB4OEuvxMj7qdRep7inVIfLh4YkDgCteOuMTikHJ90pqGVIIzQCHSUjsMILzf-SqM_J_mVfs5hCF9aR_Vc55n9x7U-GRa2_Ri5ntfiTNnaZ254KqBEGuKLchEUJt49zwuxn5w7YVKrmtCJ_QE92ENvI2LwLvrT52wLd7QfIlNisXu59Lthsc3EuCjwPpcidJutnI1bvpOaX3iNNxCSlFt9ObAL96BAFKXYrn1fLD7__XVRoHZTI4ob-gJs0bgICk_o-1XCxOXPyT8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82591" target="_blank">📅 13:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82590">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZ2y_ilkejANuDWOgMz1BVSk9wGW_pvnhIopVsBG7aL6xfOvPjFWhO7wKB3yhu3rBeuJYJB_cSb6P8z9Dg5WNoEiit9fey9AE6-5fXXEroo5nmPchviZCsQgN5zQqYEVY2lwnD2aMtwgxn43K9uAGr0mv3svUqLnTuUDyPG2jJxuox0Gk8STwSebohR6oeNj0m4KnYG--g2XK3nujQ_830YMNB4_5ps-LKho4Q8W_KM4M1fXn5R3PjHvOeuFNHtCvXEBj7JbPacXqASi94h-DPFuK44lQ4KzN-8ijpDtZe-X9s1c4e-0ArEOGlM_B_FRbD5E8aK9S9Q4w4NAbQJejw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه تاریخی داداش سریع بیا پیوی همین الانشم کلی عقبیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82590" target="_blank">📅 13:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82589">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ckhvp9hLKSDu2hkCiPQmPmZxF-yHGTWlWT3R3ONHCVsEqETo8oGEGkasdAY91wPqgpeCyaNetH2GqfouFdDy9PY9DPccKUqpcF1oge7geBz7NetevTz3vXaIGBA0i3PQzwD62pEZwFCr4FeNcdgGC7duNxBMwE-3vTgjUttS-cHNMd960fKgrNIzHqBcI1rdDpaCcqKdPkNZpIuEC_Be523KY6lmV_pWBb9beoq-yeaNyMjBoUZB8US_FF5dPB4mmM_b5ib3KWld_A4f5lpr0Ea4lxNVweOaFhAvghYt6hEu3RXIR3IBsMmhcRmRbCaC00YbWmFsH8kS531JrtanYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هادی چوپان به دلایل سیاسی اجازه ورود به خاک امارات رو پیدا نکرد و نتونست به سفارت آمریکا بره تا ویزا بگیره و نمیتونه در مسابقات مسترالمپیا 2026 شرکت کنه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82589" target="_blank">📅 12:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82588">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQGOmTNpOLzpmshnas1UfCtJsD_wypGnnQaXedq63rpnOBXzwWcNzoWPmKEQTJR7yF2L3I2WifXZQrqAz63FKPd7vYyavDVlbBdvyHClVnx7EoQldNv3J44D4Wj3p-gcJR82lAaSKjUp5ZNDNKwNN9INE2-felMmOGelY30XYJvrlUFbgZEhBzfJZ6RxQ40K8MGOev0SF0pvnqapP2fuPMualQiIDjctv-_NeaZPYN6x9f2KA-WdPwGizGYcV7zYBC7-f1Mw2gXBjB1r-ZKwggGaKEQOTgMLFwAaAf9gWn-V9kxI8gnBsn8SLqGLiHXsozl9MpBIElh1A6ieGtTxxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هادی چوپان به دلایل سیاسی اجازه ورود به خاک امارات رو پیدا نکرد و نتونست به سفارت آمریکا بره تا ویزا بگیره و نمیتونه در مسابقات مسترالمپیا 2026 شرکت کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82588" target="_blank">📅 12:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82586">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ef19c3dd8.mp4?token=EdGCbkx3btq4WYBRoZZgo_mph5lehjF3GKE6_ldtZ9BnjEEanoM6J92Nsax0Y3G46EEo1UiFWw1QrJBNbnaikb0B60speSBdEIJkjbYQLT8yMFUW-XREKp7X2ixgPZUCZL6ErkIZD4864pEqkSfFiaT3I2QnWygq1DHsm0cKrKTjcl_gIXPbt3eY32be5C8FVLMIQgxahc0Jy-RQK5iYU2Ys5n3kWfqS2zRCGDjt06o77P7HuwgspXPdDN7g2_j1ri4Y80KydTvvOYicyK1iW6n9Ehg2l83y3EC5gVNmalW2JmwbvMZJzUB5NJj2JjuI-thFcJoyknhlk-ngsi8CDFJC0uoizT02V-FqD1hryegBfo2f0ewjuu7J4LhGaKmD74IDCmxwf8w7A8GNqcQLcxixsW0dxtaSf2vn6iyy7j5aeAczm6e8Mg530ReVQxjateUfIuZxWJWqUwEBk7psDhXHXOxq_BMz8P_aw8sAz7SBqJ0GFnKZyd3FeZt436Bw4JGJFQFzeLYdoamUMANfAxGapJN4Hkk8zaQa3_06qmEAa5T5o08q41MEQPooVRVf76EsPxNB_M7bJ8Vl9fWX6ZMTfnB3p3q_oNp268xWe1JB9osMDQoAqIX6bob1BLtcdGdF3-69ZzuX8U3E_27KSwW3iOqfHXTA0fBaxtULGm0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ef19c3dd8.mp4?token=EdGCbkx3btq4WYBRoZZgo_mph5lehjF3GKE6_ldtZ9BnjEEanoM6J92Nsax0Y3G46EEo1UiFWw1QrJBNbnaikb0B60speSBdEIJkjbYQLT8yMFUW-XREKp7X2ixgPZUCZL6ErkIZD4864pEqkSfFiaT3I2QnWygq1DHsm0cKrKTjcl_gIXPbt3eY32be5C8FVLMIQgxahc0Jy-RQK5iYU2Ys5n3kWfqS2zRCGDjt06o77P7HuwgspXPdDN7g2_j1ri4Y80KydTvvOYicyK1iW6n9Ehg2l83y3EC5gVNmalW2JmwbvMZJzUB5NJj2JjuI-thFcJoyknhlk-ngsi8CDFJC0uoizT02V-FqD1hryegBfo2f0ewjuu7J4LhGaKmD74IDCmxwf8w7A8GNqcQLcxixsW0dxtaSf2vn6iyy7j5aeAczm6e8Mg530ReVQxjateUfIuZxWJWqUwEBk7psDhXHXOxq_BMz8P_aw8sAz7SBqJ0GFnKZyd3FeZt436Bw4JGJFQFzeLYdoamUMANfAxGapJN4Hkk8zaQa3_06qmEAa5T5o08q41MEQPooVRVf76EsPxNB_M7bJ8Vl9fWX6ZMTfnB3p3q_oNp268xWe1JB9osMDQoAqIX6bob1BLtcdGdF3-69ZzuX8U3E_27KSwW3iOqfHXTA0fBaxtULGm0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در یک حرکت شاهکار مهندسی پارک لاله نوشهر با ظرفیت 10 نفر افتتاح شد، مساحت 307 متر.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82586" target="_blank">📅 12:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82585">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/090cf184a9.mp4?token=e9tQkVKcQLehh6B2PO7cGlxRah27p_0ZMDpin-zngbBM6lDdAOD7UX-9S1k50F5BRXfl8rL1oY7yDa6dyLgYnyhijHGIrBB6qFzcRJc8I33ZMRLKwy9aXy0WoEPCR-f2GTcNYArn6SAuLEfo-FB0rTmGgIWj3ygyBNJcQt5JcQBsYVZTAEV-HFBI0W8jjDKVa9q72NYTyy-uf0liOza3G1H-YrE-O30kjXPjxgNAWhd69dKkagSl3cIUD6St8PCCVxDpwFzhWMAdNAdBvKWPbSIMd9z0tPoewT01L-6Ah9mZxNSRHOXPvCzLBimbDt1ZAcdvHQSJ9zvrrJiMLYoOlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/090cf184a9.mp4?token=e9tQkVKcQLehh6B2PO7cGlxRah27p_0ZMDpin-zngbBM6lDdAOD7UX-9S1k50F5BRXfl8rL1oY7yDa6dyLgYnyhijHGIrBB6qFzcRJc8I33ZMRLKwy9aXy0WoEPCR-f2GTcNYArn6SAuLEfo-FB0rTmGgIWj3ygyBNJcQt5JcQBsYVZTAEV-HFBI0W8jjDKVa9q72NYTyy-uf0liOza3G1H-YrE-O30kjXPjxgNAWhd69dKkagSl3cIUD6St8PCCVxDpwFzhWMAdNAdBvKWPbSIMd9z0tPoewT01L-6Ah9mZxNSRHOXPvCzLBimbDt1ZAcdvHQSJ9zvrrJiMLYoOlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو تروخدا
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82585" target="_blank">📅 11:48 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82583">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGo68oiZFXJCIwPFzhbmv3CGLu8HLWCXdpzKTA5PJApvSrsf7QOBJo5JPatYyalSOYkViHfVBrHdO_NN5tMWnR_01iJvJUI5I-bMD7OkJYBG1eO1U-jgtn8l-o54komgg9gCUn6DHWQi-8PQ43wdcyj5Po66d2y2YxyG3H04dJ8-Mz2YSl4pw4k-9is_s4thIe-qHtAYVMzmTFXQ8Fu44Pv_QRq1uwUYsgiMdCKi1_OhPZ6rj0fbIbojJtWamkQ6vvpOlC3yXtEDnpLPlCIuhsKg48K6FFHCSmZRM6pE0BJvmeWLNXJU6lIxAZ505AJs1tTZuMYShGn6vFxUuTbwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد خیلی بیشرفی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82583" target="_blank">📅 11:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82580">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MuXBeMICOqzJJ30_KdySGvlw6-pZdkqtryB7yWAy37sqaz-6GcYua7_hvQhOjxZNrutayEqwMDsv3YWnv0wP_sqZXo-9mjbxqs1opXpKO3nl7IwoCq1ZTK-ZDdDN50hgf4FX5p8BObnUq-GuALlk6scFQJBByDj--dPyxrwtT-UpRaXWMtMxt5b4Dr8tGEMDH6F_JrDCWfeUCoIg_DyM7fh3gfHzMlwLhHHurfo2XclWAbaa4SnCfCpNYdMT-asI948Qw6M6iuEV9L1FVzsRZmx4_yTiY86PC7xPMGrjM6PGc_JX66BBCgptchZC6E0J1LtVAIMGMgKQqs4C5WYzIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMMgnbZfxB-4aR7CzbUTeurwdDSGeLPGTWHDPYQ6uREhhKxijLwNePkTIqYafSaU4S0kwxyg8s7UxJzcW1o67pNBvzzPke4e9A6a-saTD0eiWJ-z_B84IAS3qOE7nvgx1GenkRafYTXBGXHKvLLmNxTF7g7Izd_rPWN_VJSRFjPw0UztxNc0QZRfZcDOfbnfQyqHUoLPPveYkpbno0dWi7fmOYV2FJzE-73FAYmGc-r-iMIbG9prz7rk_lN-SLeGIW-X6eQsxfM078nCjQ0DmlE18VRCBU90mBcfXDL9SR8EtEpqQwqZY65IgwPCoH6ryY-5Owzwzyp-qylYG2d1eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rr27QLj2anW_B08PpT6snbP71cag8f8VDjMWetAkCATxukG16PmqBrbyqsXWeuFk0IY2gRpYHYgsC1CD71vSOtkDI5vLQR2jknsQKleVVfPovuAxeWn7xtMU3gYPO0sxJAUOXQz0uhjXVgiF-C1LdME9RLGOcnqtU8eyoVqX16aoQgrjhvVjhYWWPrBs_FpRNlf_JN0QZWs83OUpNozt_Ynwm6woILqiatpSzlYlEf_Yfu6MiulgAylr8HOIhgKoT5R18Df-Ysy9wbGQKElXLvVPoN_kFep5o0v-Qdtq7rNXBC4FhoVDYx0ZdvspO2RwbBxdzR1Y5lHSEtRoYhTCow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تو عشق ابدی ورژن آمریکایی یه دختر ایرانی به نام پارمیدا شرکت کرده و اون ته مونده های آبرومون هم برده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82580" target="_blank">📅 10:36 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
