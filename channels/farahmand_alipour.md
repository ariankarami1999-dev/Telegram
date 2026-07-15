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
<img src="https://cdn4.telesco.pe/file/bFnBQThKdsOYoX-fQ0ytNgyiy953ap99a7UEb2jJs2jQAL2p92ItCLrttPhsR6BWDdFyAdfAWeQNO21LedwX4V2ZllbnUWks8xVeHnCT1H4sLBW_lteinROWdxnFHDuU3B7lgXnAwr011kd6Hxl8Rgfmo6YiTx1fL1oCY0MaDP2FnJIeudDuZ2zSFJlpeW_9nxpcCN5lvageOk1SONR9Sc-uycICU1BMPum7izDFloFjGQqAI-50UYLz2M2qdGI-VpAB2XjzvixNXvxgmDTLp31gRAomm7x490UJx2diuOSuUY6I3EyKoyBrLnSd3WAhLoszFyvl2q-O79Z0HJkDBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 07:57:58</div>
<hr>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=aEExiIsY1Ihv4h6-lLp_NksQyzRwuebf0RxZZeY7VF55zRnbG4ljpTAC6qZM91O5-sitamGjC1EdCo9JWgcQzsLuRgeoiE0TtAkQPWsR-htVP4qeIAwPeshtmWXRqjE7wNKt-7HLcTvsKhL0O6snqPFwuEjkWcVJQpDYwwj-LpTQJLAqQHihpDpO43_LiJUNxubcINxKiOhl7jMC4CVru1hxPAXamcXPEXDiBHfD2FbtazKyDXFJuVQWAdlFEDn-i2lH9elNlfGuSt65TPO7I-n582wNseqwtWLjJtktrI3fpkqBYVV-RIjy7mt2gPStM5oyHtJI_rXXLH4xG-EjcCyQG41YszjXc6zE-HIRQFIHIAlVAN4ecqLm255KzmGmUU35FssMsPaqF4SlavnYeuF4lBVN6SbpZjkqubX9DaEHox4LRor6HGqOkptQAq2DfqGYnKicxsdaibEQ0YoqMXFudle4DknVYdOb4o8wrwKPkjfxSg9nOjbby7yaVrv-hNdnoQmkCoVqSlajw1w93TnByOv8dwHiAr-CfTaaBklVkdS94okxA30iCOwJA-yS9960I20Jr7Dse-o3Rcirki_zLirQvq-HB057n7riwbt9RwkIO9IUcrv4703H1MzHeqa0CzS9smd8TZlS5Wvo015u_kImpJMtjgcXVHibe_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=aEExiIsY1Ihv4h6-lLp_NksQyzRwuebf0RxZZeY7VF55zRnbG4ljpTAC6qZM91O5-sitamGjC1EdCo9JWgcQzsLuRgeoiE0TtAkQPWsR-htVP4qeIAwPeshtmWXRqjE7wNKt-7HLcTvsKhL0O6snqPFwuEjkWcVJQpDYwwj-LpTQJLAqQHihpDpO43_LiJUNxubcINxKiOhl7jMC4CVru1hxPAXamcXPEXDiBHfD2FbtazKyDXFJuVQWAdlFEDn-i2lH9elNlfGuSt65TPO7I-n582wNseqwtWLjJtktrI3fpkqBYVV-RIjy7mt2gPStM5oyHtJI_rXXLH4xG-EjcCyQG41YszjXc6zE-HIRQFIHIAlVAN4ecqLm255KzmGmUU35FssMsPaqF4SlavnYeuF4lBVN6SbpZjkqubX9DaEHox4LRor6HGqOkptQAq2DfqGYnKicxsdaibEQ0YoqMXFudle4DknVYdOb4o8wrwKPkjfxSg9nOjbby7yaVrv-hNdnoQmkCoVqSlajw1w93TnByOv8dwHiAr-CfTaaBklVkdS94okxA30iCOwJA-yS9960I20Jr7Dse-o3Rcirki_zLirQvq-HB057n7riwbt9RwkIO9IUcrv4703H1MzHeqa0CzS9smd8TZlS5Wvo015u_kImpJMtjgcXVHibe_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مزدوران حکومتی شعار میدن
«جنوب ایران نکند جنوب لبنان شود»
عجب! شما دیگه چرا؟
خامنه‌ای میگفت «جنوب لبنان الگوی پیشرفته
و موفق مبارزه ایمانی است»! سالی یک میلیارد دلار از اموال ملت ایران رو میدین به گروه‌های تروریستی اونجا  و تبلیغ اینکه ما اونجا پیروزیم و …..!
ولی ظاهرا اسرائیل در جنوب لبنان چنان درسی بهتون داد که الان خودتون هم میگید نکنه بشیم شبیه اون «الگوی موفق»! معرفی شده توسط خامنه‌ای</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6123">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=KIZqWIToUzGnJhKmw4nD0sMVeY1f0oEQh5JIY1nLqY3231xQTzZeoxpkmTEaY123tsKh_cog2q3fUO4LPPbwkibGd9q_tR2tq0SjC_86WqRtMgEMmT8WeuWX3c1FqOQvZuc4IqwY-eIMFI0Yoy5b3LZVrPCkP5Xm9bYr5cWzrc9Lg6UoHYYlcs-UUA3xWVDQZmeDaWeiZlDKXpTpbfQy0Nv2feRsFx0un2Vrn_35qXjDRiaHElNVTJHGmWULPaj8xp0Dd9B051W4F_UysTDcd5xETlmE-ZHnLzzhnXry5DYKJHO-Up4dwFGGkhQnJjpdOGu8_n3VPyrxs3Fu1ZFCXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=KIZqWIToUzGnJhKmw4nD0sMVeY1f0oEQh5JIY1nLqY3231xQTzZeoxpkmTEaY123tsKh_cog2q3fUO4LPPbwkibGd9q_tR2tq0SjC_86WqRtMgEMmT8WeuWX3c1FqOQvZuc4IqwY-eIMFI0Yoy5b3LZVrPCkP5Xm9bYr5cWzrc9Lg6UoHYYlcs-UUA3xWVDQZmeDaWeiZlDKXpTpbfQy0Nv2feRsFx0un2Vrn_35qXjDRiaHElNVTJHGmWULPaj8xp0Dd9B051W4F_UysTDcd5xETlmE-ZHnLzzhnXry5DYKJHO-Up4dwFGGkhQnJjpdOGu8_n3VPyrxs3Fu1ZFCXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=uukUbxq61Kc79KDOGiiAtbEmFRYZw5TL4_2BBsuM1eIVLrPUetfbacuT6ldWCpehbdl5_2EDMCO-NZYpDIN7M19sMs6Q315cushn4qcTCtAbnlw0SaRCgcmFP-Q0pRx2IzxQpYyiN0FtxNtcPslSvFVCQE2xuBjxczkY3R0cA1PC1DvOkWH1Uqv4ZvAdkvvF7YmZbAtPNVffIuYX5kOtmB1acRZLXfkQEL4RVNsIQ4Nfq9tF7kwKa30JTOS9TjHoD_Yh_S8_1yV1H-cWWPgEJRKETn1TysLIyE5ZAs9Hydnrlf-XtiIp2ectbTCS6zh6n4tF2ulfvlnB8N8dUVJVrij3gLkCIuHwzaSLrZRRgKiWtOm2WifkC7uaLX-AxWJ_V4oi-tND-NlKRxoNoBpaYj5iRb14uJ0W_Xa6bFvSwiFihlandHb7LLsJKEbnEUvVqUg3okPPVqOwdCHuO-99cbvtVyJXl9K8H5gQAxm1HZBIII_jh6lftfxk7bab6FpS7a4x-zT89_Dn0sYa2_k1Sknkw0BvhsIiwVZWEsPRwN7LtvKMYIKu3Trx0OklwXIqkXd6UYwXjBMJR-d2zIz9iKl_VFDJxQ7B8_RGDB40b4ZLjb0-XfTdrduFlkvb79TUQC0mQFIQ2vOt3fb9QHIFuBWaigFWo5bHSJSENFIvar0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=uukUbxq61Kc79KDOGiiAtbEmFRYZw5TL4_2BBsuM1eIVLrPUetfbacuT6ldWCpehbdl5_2EDMCO-NZYpDIN7M19sMs6Q315cushn4qcTCtAbnlw0SaRCgcmFP-Q0pRx2IzxQpYyiN0FtxNtcPslSvFVCQE2xuBjxczkY3R0cA1PC1DvOkWH1Uqv4ZvAdkvvF7YmZbAtPNVffIuYX5kOtmB1acRZLXfkQEL4RVNsIQ4Nfq9tF7kwKa30JTOS9TjHoD_Yh_S8_1yV1H-cWWPgEJRKETn1TysLIyE5ZAs9Hydnrlf-XtiIp2ectbTCS6zh6n4tF2ulfvlnB8N8dUVJVrij3gLkCIuHwzaSLrZRRgKiWtOm2WifkC7uaLX-AxWJ_V4oi-tND-NlKRxoNoBpaYj5iRb14uJ0W_Xa6bFvSwiFihlandHb7LLsJKEbnEUvVqUg3okPPVqOwdCHuO-99cbvtVyJXl9K8H5gQAxm1HZBIII_jh6lftfxk7bab6FpS7a4x-zT89_Dn0sYa2_k1Sknkw0BvhsIiwVZWEsPRwN7LtvKMYIKu3Trx0OklwXIqkXd6UYwXjBMJR-d2zIz9iKl_VFDJxQ7B8_RGDB40b4ZLjb0-XfTdrduFlkvb79TUQC0mQFIQ2vOt3fb9QHIFuBWaigFWo5bHSJSENFIvar0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgL8F0WQAHw2bRtcWGoPLrN68cjCVvQASKkc20M9PZOiwtiQFPfF3P1JF_WwFafDIhpYNP56xpgtisC9EtLMuZlqQxcabtKOhNz-zfS_VBiN2jn6fbdZnakWv7a8pG34612RUh6gqnFWJC9RWE_Ht3Wj6KGVu4u6SKa4mlgnaKV4Er9vHxRTXvlj9xcIXe4yv_ME5EHc4wSZTH8WcPCtRBcBulgzd0VpOUnx6W73GAUguUBcJK5rW7ge-2jB6pfqgAG8Mssbv9QK8iMKyrl5iqQ9et4ducq5xxWdGgvexY2nm0Kj39GTFgFC26TuUGeu69ZBfgkTNT6xfMVPPKAulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMtQpgqKReoQfynZcgc0MAOK6T1LWbnAqVCmU3H0is_Fo0WO574sn7NYgOTzxeCbkhzbjpfeilAPf_VblR0zgrDhIsz9wk2uvIFAFYmQjeYEoADljOeScRvXzF06OiGymr8rxuXoriGKZeS1KRxPxDBehGhJ6LY_SzJwDGp36FnAwowtpBgDqrs64jvELkz54UUi9-zqA3SgYt-qWHe75C4UjyMMdW9BPPpRtZ8K2mSa60ssIJbF6_RnIC7-7FYg4E1NkQlKO7m2SZXqRFlQ5SigwPSXvzYhS9yKimyQih6JQemhnU_qtzy8FVkWXfU2O7qm1dr5tOExPe8udvIe3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=S5xXhbEjKCJsB__D8UchXoPehz5H5V2HJTd3KPP0FJ6z7tWpZIfstaV_6aHt5FKG0bh_dMgI_ECpMCPq1Jlv72-7eR-QQBUKT_nt3VgPyZziNWT3hXZ3oNOCnV4nXP7lU8WjewwyeJetV8h7cr9xPA-AlJg4x2qvkfElmgtGzmRjpofXhWWCy1vaxoBdx1ytdniDQbfhlRloJLx1mZ5ehLnua3hdBmM0zYEFZeBs_DTrmx2gus3uS2vA02_nRgdhyzN_fIDx6UUquU8oa9niCczQmUdbm9GhJvktA3adgnm_dJz9K8I12zRR6oWHeJFxkgLm_3deSihAbLN0Tw37GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=S5xXhbEjKCJsB__D8UchXoPehz5H5V2HJTd3KPP0FJ6z7tWpZIfstaV_6aHt5FKG0bh_dMgI_ECpMCPq1Jlv72-7eR-QQBUKT_nt3VgPyZziNWT3hXZ3oNOCnV4nXP7lU8WjewwyeJetV8h7cr9xPA-AlJg4x2qvkfElmgtGzmRjpofXhWWCy1vaxoBdx1ytdniDQbfhlRloJLx1mZ5ehLnua3hdBmM0zYEFZeBs_DTrmx2gus3uS2vA02_nRgdhyzN_fIDx6UUquU8oa9niCczQmUdbm9GhJvktA3adgnm_dJz9K8I12zRR6oWHeJFxkgLm_3deSihAbLN0Tw37GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=NF_6oUCPn0BV3S8mKbcg86QuBkyRAKuBStVuJU3kEX37p9pCusoOj9Jh6uczG-2g8D5FgXkfC2bJ92urGKwAobl87XqsYlAkKYrI7EdRNwURU0MqcwR71j7SDSaKchZPZTnUtnN5W-n0ry46d5NrCqmuM5YdFSktcFO5KmZsh6Iv5ROsULTwpIY86dzRxXSJltFQxBW-3_xyaTmud6rmKeUEunozKjg2aA54qTu2eVDTmaiVcKgjpkzsxtV8q3duPIJhUP3zwubU54V7NTCrmc1s-PVPlM3CrOjWTRYsCmJzyEPTZMnnGRAbZm3CRUojF-O4YGFW04WgyE9pgVMCSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=NF_6oUCPn0BV3S8mKbcg86QuBkyRAKuBStVuJU3kEX37p9pCusoOj9Jh6uczG-2g8D5FgXkfC2bJ92urGKwAobl87XqsYlAkKYrI7EdRNwURU0MqcwR71j7SDSaKchZPZTnUtnN5W-n0ry46d5NrCqmuM5YdFSktcFO5KmZsh6Iv5ROsULTwpIY86dzRxXSJltFQxBW-3_xyaTmud6rmKeUEunozKjg2aA54qTu2eVDTmaiVcKgjpkzsxtV8q3duPIJhUP3zwubU54V7NTCrmc1s-PVPlM3CrOjWTRYsCmJzyEPTZMnnGRAbZm3CRUojF-O4YGFW04WgyE9pgVMCSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=J1UyMRNGoB9A2K5jLwz92TxKZVSf7esypNzLpeYTdw1fQ6dr78mJYQArbpZxRsGDqKYIxiXSzqW9YVHtkuDy0KN5IUPHBvdre6VIGNfZ7Kyd7nTHDXMi9tdfreTdzEeBf-EEe_BEErl7QtuFF_iteqfGkqDSoGOFslXWqcvCYGdd8qP3_5xgDNnauwFXheI2o6s7O8pPy1CXxzTnu4ND1uZQDWeddyvK6V6lpgBFkupVgbJfWKkpHSdLXpbcl5-XTtVdz4pMNF5o4KTtqftGDppEY1DN-L9UvjKl6cSccfob1DTqhsI1d9bvs_TKmkhKwTzBEin3Jxbej0DizA7rKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=J1UyMRNGoB9A2K5jLwz92TxKZVSf7esypNzLpeYTdw1fQ6dr78mJYQArbpZxRsGDqKYIxiXSzqW9YVHtkuDy0KN5IUPHBvdre6VIGNfZ7Kyd7nTHDXMi9tdfreTdzEeBf-EEe_BEErl7QtuFF_iteqfGkqDSoGOFslXWqcvCYGdd8qP3_5xgDNnauwFXheI2o6s7O8pPy1CXxzTnu4ND1uZQDWeddyvK6V6lpgBFkupVgbJfWKkpHSdLXpbcl5-XTtVdz4pMNF5o4KTtqftGDppEY1DN-L9UvjKl6cSccfob1DTqhsI1d9bvs_TKmkhKwTzBEin3Jxbej0DizA7rKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=I4sRwziSIcacoPJvv3AC4ABuCtdgT9VBpvQTIeRj1ygrtLHE5DJiBSzP2T7LYxxSfsgWfy33eFP2Vh8wCUUe6yhAbpXJ7dsUzMSD5fgIc5A67XaD1XsHcknyckZVWam7PL6hGJ5vrwcGq6jfahZJ3c8X0SIoN-9jAZEdxVmq6jjYa7VyOlqeMjYQTncqvICzpOH3HGqYNdzWH22ukMrgUsJh0xHG1SV158TDcLDOiPdS8Mi2Eykjq_PgrOXPnnMMPTeNpIOOAhAmfS3fmaa3vcmISln2VQQIk6pTcETduWbwDa3HPSIgMzupF446K9Y_F4C73OtJ9YREL-mNpzTlWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=I4sRwziSIcacoPJvv3AC4ABuCtdgT9VBpvQTIeRj1ygrtLHE5DJiBSzP2T7LYxxSfsgWfy33eFP2Vh8wCUUe6yhAbpXJ7dsUzMSD5fgIc5A67XaD1XsHcknyckZVWam7PL6hGJ5vrwcGq6jfahZJ3c8X0SIoN-9jAZEdxVmq6jjYa7VyOlqeMjYQTncqvICzpOH3HGqYNdzWH22ukMrgUsJh0xHG1SV158TDcLDOiPdS8Mi2Eykjq_PgrOXPnnMMPTeNpIOOAhAmfS3fmaa3vcmISln2VQQIk6pTcETduWbwDa3HPSIgMzupF446K9Y_F4C73OtJ9YREL-mNpzTlWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seDtoBUvfbJ39Au6Rk7tUBj9xJ1WgC6OgSfdQSiRnwNGDwSBoONWMcOe1ZlQAla89lDB6FNpY-f_wBhzo6Q6nLf4yJEWylk261ngT6lX5NylvC6mX68GF89KvhwgY1AgEotYB6uEa2pcW4AOr2qNNzn0nHgWZJLJ75L5gf7DdEyTzUtbm1hbs790jqOZIcNCTFxDmjd57fVqY7SYfspdOd0bo2wrnXlM_g9vxRRpkRgNIHoAa58OrtRmIua6lyHrqMvvL-s7eER0o6qemgITrgMwEJrIcr8HewfAhL4qlUOsN-eZ04KvgcjOSTZO5XVZ8QVw1Lj4fqOM31dNrlpuYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVwk0MF1CymWQNvBspQ8qRvgCbc9OMnrwCCLvSSTmnNZG7h63TSeiBWtiMjICz44yaJh8FcDCbzEZAQrmBV-uZwz5BLiYRSq8gMvbZtzFABq742ir3Fnz48EBeSeG-EPf6pVH32S5ObLKiOmWTCPNl1wuKN6B2T09g9Q7bfvv-G-lBTFyukyL9TxmjkYB6TwNTMVSXGFJcYhgHAysEy799dAyianAAZdGsNOyLQVXCKCuthOA4kdvPxzKbtTCbGn_MFVUHfjstJ8fsr3VUoNl5ywPXjJRTMk_QEj_zesVne1WPthz_tBI_0fIXMMiubnDq-1X9wrTkke9IXGEUrNBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=kxUHmvDaGCUiGVFA4Z-TPajerepMWZWgH7yBcFrvHCqav6IE4mp5bFahXsmiWZz0V0oEE_AK71IyEAmcGfBiRlgcMMrh0WHbyEpPn0HmDiVMig8npG6VnnmeDONmdYjKYijNh_peHTdSIw8vtmoJ69x8kERbw13kexIc0fnBJ7T5_ut03b6q6QVo3czO7iM-pqG6It_4JcrNh4NgzTtLv2v4OBeJsufrnLH2_XxevPLjWGxn4JXjBw_lJpei7cab5jL-wWBiDlhFf0201HK4BlWEKEGANVx0_0g0p5B11wkELUkMPLpJULLBbVF0or7hCBu-PfvYRA_JHWtJK_0iYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=kxUHmvDaGCUiGVFA4Z-TPajerepMWZWgH7yBcFrvHCqav6IE4mp5bFahXsmiWZz0V0oEE_AK71IyEAmcGfBiRlgcMMrh0WHbyEpPn0HmDiVMig8npG6VnnmeDONmdYjKYijNh_peHTdSIw8vtmoJ69x8kERbw13kexIc0fnBJ7T5_ut03b6q6QVo3czO7iM-pqG6It_4JcrNh4NgzTtLv2v4OBeJsufrnLH2_XxevPLjWGxn4JXjBw_lJpei7cab5jL-wWBiDlhFf0201HK4BlWEKEGANVx0_0g0p5B11wkELUkMPLpJULLBbVF0or7hCBu-PfvYRA_JHWtJK_0iYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=NUJpRwMmcErmKOMXPwTPmwidxKbxO_xIEovTZ3e2sNTv93lgJV14d3vNWOA8O2xwigmVk-nZImdUjJV7nEHDwqT-UxnvKB39nCCK0emspc_bkS3q8DG9GbkgJIbhVAJXYdMwCQZTasVsBnF5bwU9JsMNiTCcIlbPCGkua9RQkYee-dqLVjBZECX_b6eK_M8bgqxDy0Td7ox-MArsrbHMqalR7suaN9c-D-Zts0gW2OXXmR5JA9FeCiHu0xSR6xNBMUC0QIoX6qASdNAzpCIGB7-sNrg9tJl6r9ujMXUBfiY9yMNq2oNuzV-ths36bkNJkqF4X5mvhXPdxxMFeNWdGSwrIAj43dQMee7JQKLfKfUOj4mgBQ2Mq8rl74j2hfpH6CZFDsy4h_ytVTMtZArBoXdKv41fYkWUcrK89YNET3moc_Vtt5dXZ4QKaSvvApM2Z2_d-sErEqH75SZTex-eareWfVPgHNpzdpESGYNIOrtmco5XXRSk38gLVxm-yHZ3S1b4GT97JSU6cqvLcCOQAsF3p29kvINjLKZtsxdd1RFcIj78fAFhKrDKG5r72hjlOvTvJlNfJXwOybhY5AoWt686zqWACejPaNvA08809MuO8MBbX8ksnxs6hfnW54Ws7ly2tWjSGr2hz8qJwe75P0HBb--hdWiRpcSz7NB-wf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=NUJpRwMmcErmKOMXPwTPmwidxKbxO_xIEovTZ3e2sNTv93lgJV14d3vNWOA8O2xwigmVk-nZImdUjJV7nEHDwqT-UxnvKB39nCCK0emspc_bkS3q8DG9GbkgJIbhVAJXYdMwCQZTasVsBnF5bwU9JsMNiTCcIlbPCGkua9RQkYee-dqLVjBZECX_b6eK_M8bgqxDy0Td7ox-MArsrbHMqalR7suaN9c-D-Zts0gW2OXXmR5JA9FeCiHu0xSR6xNBMUC0QIoX6qASdNAzpCIGB7-sNrg9tJl6r9ujMXUBfiY9yMNq2oNuzV-ths36bkNJkqF4X5mvhXPdxxMFeNWdGSwrIAj43dQMee7JQKLfKfUOj4mgBQ2Mq8rl74j2hfpH6CZFDsy4h_ytVTMtZArBoXdKv41fYkWUcrK89YNET3moc_Vtt5dXZ4QKaSvvApM2Z2_d-sErEqH75SZTex-eareWfVPgHNpzdpESGYNIOrtmco5XXRSk38gLVxm-yHZ3S1b4GT97JSU6cqvLcCOQAsF3p29kvINjLKZtsxdd1RFcIj78fAFhKrDKG5r72hjlOvTvJlNfJXwOybhY5AoWt686zqWACejPaNvA08809MuO8MBbX8ksnxs6hfnW54Ws7ly2tWjSGr2hz8qJwe75P0HBb--hdWiRpcSz7NB-wf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=J7lmiUmWdyW-RL5x2-i15L8phbIJ_P6cDdUFCvAcUnBEZMJfDyeUbRtnIZObQ_5VJrJKXL_DdKLhOj5xhDwQcQJsgyxkN8Taz8VyglmaByrHCvTiPbVCGNKrBjdMAhMDvWLPqrLtDSmHCAj09bMKNfQ_210MIafNy2N7ricDjKIs0Yd-sVGP3ryK58sOR900ve6Nq0VxE1pPlB-LnSG984qpVz47RjBBBJrlKCluKHtC_2cd-z_3cQl9e2Mya4tuVcfOi_8cTckus1mxgEh8LCouFyQB_yEBpWQ4SQUFInX9-MbnmVS9mahv3bQgQ3nG1dJtLpB3W7Nav7YF-JLP9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=J7lmiUmWdyW-RL5x2-i15L8phbIJ_P6cDdUFCvAcUnBEZMJfDyeUbRtnIZObQ_5VJrJKXL_DdKLhOj5xhDwQcQJsgyxkN8Taz8VyglmaByrHCvTiPbVCGNKrBjdMAhMDvWLPqrLtDSmHCAj09bMKNfQ_210MIafNy2N7ricDjKIs0Yd-sVGP3ryK58sOR900ve6Nq0VxE1pPlB-LnSG984qpVz47RjBBBJrlKCluKHtC_2cd-z_3cQl9e2Mya4tuVcfOi_8cTckus1mxgEh8LCouFyQB_yEBpWQ4SQUFInX9-MbnmVS9mahv3bQgQ3nG1dJtLpB3W7Nav7YF-JLP9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2_NxrDf3lqgi08vo8y-vLhn240A_uzfeiQYrm-_DqPBGXpK1Gf-smStOIYIsNGZhKuHwC0d7SPvqqIPuVtXbMlfDdNEVYrEKgpmvdJKw1jAs997HPCWzBwlYLblGOzYkSIiHevncRnVvP0sLaiHpuouyAAhC7quzcwB3MrcJuQNbJZCMpUkd0Nyv1I9wBuOnUzPBnfJVCpFIB_tz9LgUu1fos7ImgwiqCLH30MOkbe7zg6iCNlcT4IRqgZdyxzj9K-3itP1fg550uH-Ucq9r1nWZg61nt77YVNw66phZ_fWlWYpkmrCPp-kieaFtXxoSI8kKgGGqXuU2k4tKXGZJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
ترامپ به فاصله ۲۴ ساعت، از ایده گرفتن ۲۰ درصد سود از کشتی‌های عبوری از تنگه هرمز کوتاه آمد.
«به لطف نیروهای نظامی آمریکا و همه اعضای قدرتمندترین نیروی نظامی جهان ــ با فاصله‌ای بسیار زیاد نسبت به دیگران ــ تنگه هرمز برای تردد همه کشتی‌ها باز است، به‌جز کشتی‌های ایران. و این هم به خاطر رهبری دروغگو، خشونت‌طلب و شرور ایران است که این کشور را به سوی نابودی کامل سوق می‌دهد.
بنابراین، ما
یک محاصره کامل
اعمال خواهیم کرد، اما
تنها علیه کشتی‌هایی که به بنادر ایران رفت‌وآمد می‌کنند یا هرگونه محموله مرتبط با ایران حمل می‌کنند.
بر اساس گفت‌وگوهای بسیار سازنده‌ای که با رهبران خاورمیانه داشته‌ام، تصمیم گرفته‌ام
کارمزد ۲۰ درصدی بازپرداخت به ایالات متحده
را با
توافق‌های تجاری و سرمایه‌گذاری
که کشورهای مختلف حوزه خلیج فارس در آمریکا انجام خواهند داد، جایگزین کنم.
این سرمایه‌گذاری‌ها عظیم خواهند بود و در عین حال برای خود آنها و آینده‌شان نیز فوق‌العاده سودمند خواهند بود.»</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6103" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVU-nDZkvVMadV7tl3LNLTuxH72pYU5CaNIsDpSVAfsYyWebLiP8fhqd727ZvWTwz2u-zDA4xF0zWoyg2IFWTcY0B4qovADQl-SCOxzhUPXuYiEZuEjk3eJYAsD9PDTpG3M5qKyjXFI9bXNVt4ANlpq7x-xWP6MmFRa6H57xCSejt71lZd-ngv7jIdaGFFXHrElikrNWv_-WkQRgIAECXSmEDWz7IhnnMYdfLXb1KMNczAgpHEXsWY4zZqlta8I1QjB249pzOjAAINpWiH_NpqYQobDKJaIWptEaxlPOURJOARy3H8YMisIQSTSeta5rg2zo38F7EHphnLi0wWWvSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=aOWdx-kjqpNlLf_hjd1eb5E2Sk6qQqxN5yqmFeN-NyKk7KCPsSEQvt-PKFPbNUvN_toki5Uc4P1XZPv9YpHMVCqyVZ24I_h8Kp-VIrWOrx-A_feVKJ8tyGog3A-WApFMHrrRqPDGkUFqNOJcV_nGheECSiOkpGz3jHbrC-PTsoyAWkRx2BcQgW-iHqeLTBeTwzKjvDrqW5Rhzcu3eEbbfECTLzW60kDOE-1eTewufalRdFXDLCGNLlYtzBsr2N5FXM0bMnPyiY8vC1KqQCwaN6gO-mOn4OHkAFnfm_yUFfCfVvAoEBTh7II_LViYFNNJKi2QqNe8XM3AD2fcE62NYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=aOWdx-kjqpNlLf_hjd1eb5E2Sk6qQqxN5yqmFeN-NyKk7KCPsSEQvt-PKFPbNUvN_toki5Uc4P1XZPv9YpHMVCqyVZ24I_h8Kp-VIrWOrx-A_feVKJ8tyGog3A-WApFMHrrRqPDGkUFqNOJcV_nGheECSiOkpGz3jHbrC-PTsoyAWkRx2BcQgW-iHqeLTBeTwzKjvDrqW5Rhzcu3eEbbfECTLzW60kDOE-1eTewufalRdFXDLCGNLlYtzBsr2N5FXM0bMnPyiY8vC1KqQCwaN6gO-mOn4OHkAFnfm_yUFfCfVvAoEBTh7II_LViYFNNJKi2QqNe8XM3AD2fcE62NYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjIPXzCbYPwjFi9oe00DJVtesjM8S4PFKJLr3g4b251jI1q8a0Wwxy2JolqH3umtm-vobb_2Bn7_mBadHvUIFAk_hRvVRbBFRHUxg5e7Hv_XQrRL28sh31xCgjk6mbY0lR1NTfvNN8KmTFUUemnVXkjXf5ns3POtZsFpxfuVQF2uLSf10V023zCc90QXuFmmoqTi5pw4vIIIoRTG6iEm61XoPIY6tN-s4kMnodT4HA7w6s21416OCh30JnFd4RtDGHyPauEQD4qLTjRgIoKXdhTNz9DgC-o7Lr20m0a8-dHnChi_24IrBDleutOkXo3Eg_w3iQEfgrKi4Jc4ab7Y2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-cfYJQNLiQhORzcP8Yw_97m9JovkSFq8nUOZxJpTfGXIMupYO6eNxllsMiVEPfWEaKp7AwRPa6O23oe71cTJkd1DmuMjcGvCUup3qc0skYAWlaIgz9RheD7BvR832qfbgBNp4Pp6f_vkBn0yJXBvW0AXykzxmZt-erxBEx04mF88lip38kqomYJXPPTjTLTBOCvWR6xE5MNiKDDaxNscdxf3imM2gO4D_Ujm0oYHCAyQLYladGlSolw22O98SnjFgFUHJl6MFVZactJ1jtVWJt-KH7cxdViRxenvlpVCbe_l4Ibbc3fx_r2enx1VOJP7U26x2oLbXzoKwHhX1dnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
حمله به آبادان و ماهشهر
معاون امنیتی و انتظامی استانداری خوزستان:
🔺
امروز سه‌شنبه ۲۳ تیرماه،
در ساعت ۱۳:۲۵ نقطه‌ای در شهرستان آبادان
و در ساعت ۱۳:۳۰ نیز نقطه‌ای در حوالی ماهشهر هدف اصابت پرتابه قرار گرفت.
🔺
حادثه دوم به دو انفجار شدید منجر شده و جزئیات تکمیلی پس از ارزیابی‌های اولیه
اعلام خواهد شد.
🔺
جمهوری اسلامی در این ۴ شب و صدها مورد حملات، هرگز اعلام نکرده که چه تاسیسات
و مراکزی مورد هدف قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6097" target="_blank">📅 14:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6096">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=GPLQnmigjpdwyJSJiV6t-uCx4iG8dazsXwaNZrTBrR1i2Onv59IFIl0XVLC4J-FmMAI6mODeNxTVvryiWAE2Ac5QcbxunzyCtadWZl__OfyTNWt4YH8316m3fYSe9czc_kmAqmmNKH3--HD8_l2CPu7MaFElHBfRxXkdtn3r1ouai-HfqROe2cQjFgZJEA-L9RwD2y5kZjQLe9AxPRHJMJSfdHA3pzpDOGk3mZo81HugC0dpgIc8v99-0RvIVj7lydSAn47n8VZAUjn4NqjbrRd8oAwN1NbTW_NIQMV2qw1u8X-OB1fKYoggAnM9PpJybLkeOyq5dOt9iKR093BjOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=GPLQnmigjpdwyJSJiV6t-uCx4iG8dazsXwaNZrTBrR1i2Onv59IFIl0XVLC4J-FmMAI6mODeNxTVvryiWAE2Ac5QcbxunzyCtadWZl__OfyTNWt4YH8316m3fYSe9czc_kmAqmmNKH3--HD8_l2CPu7MaFElHBfRxXkdtn3r1ouai-HfqROe2cQjFgZJEA-L9RwD2y5kZjQLe9AxPRHJMJSfdHA3pzpDOGk3mZo81HugC0dpgIc8v99-0RvIVj7lydSAn47n8VZAUjn4NqjbrRd8oAwN1NbTW_NIQMV2qw1u8X-OB1fKYoggAnM9PpJybLkeOyq5dOt9iKR093BjOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌پرسه نظرتون درباره اینکه بدون هشدار قبلی برق رو قطع میکنن چیه؟
‏چمران میگه:
‏شما اگر بدونید پریروز چند نقطه برقی رو زدند دیگه این سؤالو نمی‌کردید.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DI1f61vL42ySxQn5kYMCloRcoaUAkfAtXCjC_lNTA0zTKTDWkOQy_ZWZfgmhenzwH7EdwIPX3IUij3OHPCgMi2KDQIiJ33IS5-eZECTj7rLA8Xc4TO8Eke7v2MO2dXSL7Wz-S-Uhvl9BAsodrP8dylVH33cX8ktvdGZmshCvOCD1J7X04Dl98qBTAA3sHfUTTIPB7YT8PRVflBfyS3LHm5ihIH_S14XgvhZcEpTbJUbBUviyq8e_Lk3AaSCkCSSrvGiRylZ8fKHkdB14aHaJGh1TvjV_oyJsZEcmpe_kVlcAOwz6Dv59yJsV0qQUAH-YXt7R1w6XROe7UhLx9z2nuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ge21nCCb68rC7OiRrhNXHZSaBmAekuVYVy-oHMedOGNqVdINDTM8aFLq9Q5Sfg9-BHiDMC7fdCHNH6Pk-pOmRJBvFbjAR_821w9FgnxgRR7-wNblk7yMN9ITc5kBIXUp4JQkv0Df_QRg7BI_mNI8IaM_foIeG5uLsAe-30y-hc71Q9m9N9VhLHULsHF2QRuULbeKlJKyfxrJhRS8JtAc7qWVZo1Usgqo4A85HY1nL8JYedcRvIN3lKJmtNoGJ8CZ2RqScQ8rpBVr0043Q5AdQtycLWZuzlI6pyXj2bh4BN3qdWy6fNTvEjRqtlirnEL9AN9xy8uHpJb1XqJ3Bsk_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.
در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!
مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی) نیز در این حملات مشارکت دارند.
🔺
دفعه قبل هم که امارات در پاسخ به هفته‌ها حملات جمهوری اسلامی به جنوب ایران حمله کرد، مقامات ج‌ا تا چندین روز نگفتند که کار امارات بود.
الان هم برخی از این حملات مثلا دیشب، با حملات دقایقی پیش مشخص نیست کار کیه.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6093" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=vdb0DPy_eqH4dlYnjprrj8TQjNqel7SOv6ThkDDuD1DoPgySYxyaVE0_hMSjiL5SuQf9cU5lqVDefxx1cdH6Zxkiynwnx79TbrpabzaUgkLf3Gv5HiFZO8R0GW0eTV_7RcfE5QzR1CKzqfY1qMx1Td2bj9qV2aqJm4NJV58G65hoKViUxBwZv7gh8398k-VVY1JvSsUPi5yd5fumr5DYfF8sNAGnNvDDF_Zzcr69ro47TrElm6iY7su2omaymPXJMrV5CHsEOT93J-ULNtJyVJVtCiGqKzK__mB-787VgTGbmToY6anV42QVxbmNmEvWk8FloVds4Pa7xsnMYlvO6XzjiztmNJgIWJvkvlG0mAkYYQATX7_QkUKJ0EYzlyym7y2mRCugaTLFoM0aQBx1dWJeM-5z5quclj2hGH83GjSYhYgnFVfrUCqxBzhniLtFMONW1XzlXKju64nGn8ZP6NFP-05CL-tLL6uBVNbyCMCHMZWRQTp4_pbqv37l6Bl0YvGS9LYT3tlR9VLHYDOM7QtuwAsIB3cAT4DzJKsJLSF1OL6qjmlq0HbpCaCIEsR7ldjC00B92kS5ecqTh_hNaJOwsH9LSr6HNUkcXop4RjfbiEN-Wire812BYoDWm2Q9cIfcqiGrNCK3Y2LSuxZf4uv7nmORCYS1CNL50lAtaqE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=vdb0DPy_eqH4dlYnjprrj8TQjNqel7SOv6ThkDDuD1DoPgySYxyaVE0_hMSjiL5SuQf9cU5lqVDefxx1cdH6Zxkiynwnx79TbrpabzaUgkLf3Gv5HiFZO8R0GW0eTV_7RcfE5QzR1CKzqfY1qMx1Td2bj9qV2aqJm4NJV58G65hoKViUxBwZv7gh8398k-VVY1JvSsUPi5yd5fumr5DYfF8sNAGnNvDDF_Zzcr69ro47TrElm6iY7su2omaymPXJMrV5CHsEOT93J-ULNtJyVJVtCiGqKzK__mB-787VgTGbmToY6anV42QVxbmNmEvWk8FloVds4Pa7xsnMYlvO6XzjiztmNJgIWJvkvlG0mAkYYQATX7_QkUKJ0EYzlyym7y2mRCugaTLFoM0aQBx1dWJeM-5z5quclj2hGH83GjSYhYgnFVfrUCqxBzhniLtFMONW1XzlXKju64nGn8ZP6NFP-05CL-tLL6uBVNbyCMCHMZWRQTp4_pbqv37l6Bl0YvGS9LYT3tlR9VLHYDOM7QtuwAsIB3cAT4DzJKsJLSF1OL6qjmlq0HbpCaCIEsR7ldjC00B92kS5ecqTh_hNaJOwsH9LSr6HNUkcXop4RjfbiEN-Wire812BYoDWm2Q9cIfcqiGrNCK3Y2LSuxZf4uv7nmORCYS1CNL50lAtaqE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی خامنه‌ای «علی الاصول»
با تفاهم‌ مخالف بود!
و نوه خمینی هم این چند روز گرد و خاک به پا کرد و گفت هویت ما در مبارزه با آمریکاست!
اون‌هایی هم که نگران زیرساخت‌ها بودن
الان سکوت کردن  و صداشون در نمیاد!
آغاز دوران «علی الاصولی» !</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6092" target="_blank">📅 09:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6091">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سنتکام ساعتی پیش
از پایان این مرحله از حملات خود خبر داد و نوشت :
🔺
جدیدترین موج حملات خود علیه ایران را به پایان رساندیم
🔺
در این عملیات پنج ساعته، به اهداف نظامی در بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردیم
🔺
سیستم‌های دفاع ساحلی و موشکی، سامانه‌های پهپادی و ظرفیت‌های دریایی ایران، هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6091" target="_blank">📅 09:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6090">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_kWza-Ol5frBCLnmexrS8u2AGjYT1ApPyNVoG9lA7ADKY8GXUqknQoT5TwQOHsXDVVVZR_9EcdpFYnYBtCyg4LFBNWNyyR9utQLCD1so_xACpttTuWNYYtvQiHkoT_juGVOg-wQ4YMu8dZ10-cYJ29au0z9POgXSGSDbP5Z4MUdPzDuy_Q0smSjBqsXrdV1rpjViaKFFJMKYlfsakYct-xMYOfZC_6AEsN9texy1-zCWxLDyzO6yaIzIEm2xEaB59HKDVcAEjomeM0acaBljhotP-2A4_x5l91AX6BbrO7RWr9naJ0X3RfVrmoKke3kKi3AkcKEB2jmVT8Ko7VZqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV7GH96eqBzXzYIjklO9g32erecuA-J-wxmTE2Ed7sXrupmkfd8nfy5wJ9UlZABFNUVsiZvpOKBAmKlQFiOUBT5DFLG3q5sKSjYBc8T2uRdIPngWAFH4WbzV1tfG4k9oDKCw3IHn9unnW9HTKCK5GjIkCzFbyxVZE6IGr0sRmf6oyIlgaCA1Moyt_ZiYDTN7756uoh7-DST4D6q9Iz3QNdtTBS0atJ-LRonzhe9tJOKOOD56JZil9v7RT59iQntX3CAkyA07BybEyD3al4CEgxNvbJMdIfkekr0UXANVdYYt6W2pokXWWPFWfeRmQT_JIWpy7xYbKJgM8skkaERLqUt0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV7GH96eqBzXzYIjklO9g32erecuA-J-wxmTE2Ed7sXrupmkfd8nfy5wJ9UlZABFNUVsiZvpOKBAmKlQFiOUBT5DFLG3q5sKSjYBc8T2uRdIPngWAFH4WbzV1tfG4k9oDKCw3IHn9unnW9HTKCK5GjIkCzFbyxVZE6IGr0sRmf6oyIlgaCA1Moyt_ZiYDTN7756uoh7-DST4D6q9Iz3QNdtTBS0atJ-LRonzhe9tJOKOOD56JZil9v7RT59iQntX3CAkyA07BybEyD3al4CEgxNvbJMdIfkekr0UXANVdYYt6W2pokXWWPFWfeRmQT_JIWpy7xYbKJgM8skkaERLqUt0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: بیشتر موشک‌هاشون رو از کار انداختیم، بیشتر پهپادهاشون رو.
🔺
توان ساخت پهپادشون رو حدود ۹۲ درصد از بین بردیم. توان ساخت موشکشون رو ۸۹ درصد نابود کردیم.
🔺
یه کم توان براشون مونده، اما برای ما هیچ توانی ندارن. این دیگه تقریباً یه درگیری نظامی کوچیکه</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=TSSTYb178wN9q0OctYxuvWcgXHHsCVI3djdq2eWO5P5IeA3V3rzvEPHN5wTe9xOA3dIDQmLEYb8qNcRkHB0vncpPVV-oZYxpxgjtFSmcN8yoLy_4Q1IJDX6y_RuEWJHoeQ1hkvDwEo453Mgy86963cXltkXCAdlXhhFO2D_mDkm-LwhabX78tkCJU2UIpizhSFLTUcwYjHHTUBexnTwAQQlbJH-EbAvWm5rh8DT87kXaT4PHNwkzDCeV9HeXtnNrZUHUqVD-k5vD8yel_uKette4kkg-SE1a173Hw7ge871zphD0VOVHgOrb9XYLeiJOuJzERwb-x2LZOQVHvdHL7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=TSSTYb178wN9q0OctYxuvWcgXHHsCVI3djdq2eWO5P5IeA3V3rzvEPHN5wTe9xOA3dIDQmLEYb8qNcRkHB0vncpPVV-oZYxpxgjtFSmcN8yoLy_4Q1IJDX6y_RuEWJHoeQ1hkvDwEo453Mgy86963cXltkXCAdlXhhFO2D_mDkm-LwhabX78tkCJU2UIpizhSFLTUcwYjHHTUBexnTwAQQlbJH-EbAvWm5rh8DT87kXaT4PHNwkzDCeV9HeXtnNrZUHUqVD-k5vD8yel_uKette4kkg-SE1a173Hw7ge871zphD0VOVHgOrb9XYLeiJOuJzERwb-x2LZOQVHvdHL7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
ترامپ : حملات جدید می‌تواند برای دو یا سه هفته ادامه یابد.
🔺
سنتکام : موج جدیدی از حملات را برای سومین شب پیاپی آغاز کردیم.
🔺
باشگاه خبرنگاران : ۷ انفجار بزرگ‌ در بندرعباس</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6087" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
شنیده شدن ۳ انفجار شدید در جزیره کیش
🚨
انفجارهای شدید در جم - بوشهر
🚨
چند انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
ترامپ : امشب و فرداشب با قدرت به ایران حمله خواهیم کرد.
تفاهم‌نامه آزمونی بود که جمهوری اسلامی به آن پایبند نماند.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6085" target="_blank">📅 23:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آمریکا سفارت خود در ابوظبی و کنسولگری‌اش در دبی را به دلیل نگرانی‌های امنیتی، تعطیل کرد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6084" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1yROZXme7Jz6MtSMEqF4mPW8kOyrF5aUfl_HVrjGe-aAeWHwevXJg1d9SVFSNX68uFGRZtUi4jZ4gJLsQlk4pOXZvAto_t9O_1OUmAzvNQdAjQ2eqWCLpr1xch1XfxphnfNW51M6juJNm3k-ZOZg3xEtd6pkR9K-ez70RygzFa9cEH52a8j0IE4a8aDjO62-PACGl2FC2OH6KL8i3RuhGPAElT_AiD084WxsO3eUP4ynlXu0CBcn-Z73S9vO0bE33MKxK_BR33f6rz952x5EuQ3quYAoOJ9ipRCTeSplkDSSmmKYelZWbaOSU2YJngrqFiFN0E16Q-vdQvVkn3dmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انفجار در چابهار و کنارک</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6083" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645219e055.mp4?token=lVNsbB4Ed_1IEMGYjNDU6q8Of8cpjHQRK8sB337M0zoeS5tQCBPlNKIi7tWeDcE2K91ZpXGbr-6jy0AE9oeSbP8AbkN8goWre0JAFFD9z6bjNJAZFi--oY9ouoO92ZsqWf7H4s0dZM6gUW-8OyYggJZLpXgAUrOhOhDmDMFSIEP9_JX7YA9UW2DyZSK-efphJugH6XCO5gTk4M6dixFijZAKPIabxYnm2deO5rdE_EoX5zPPCiAioTaholSosszz_hj_ew8bA18aTDqrELGC8R_d2jzzwiJoYqZBgglbVOabzeWqmDEMzu36Kjald1ZWlkaphWpevsTtjS91QE_qxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645219e055.mp4?token=lVNsbB4Ed_1IEMGYjNDU6q8Of8cpjHQRK8sB337M0zoeS5tQCBPlNKIi7tWeDcE2K91ZpXGbr-6jy0AE9oeSbP8AbkN8goWre0JAFFD9z6bjNJAZFi--oY9ouoO92ZsqWf7H4s0dZM6gUW-8OyYggJZLpXgAUrOhOhDmDMFSIEP9_JX7YA9UW2DyZSK-efphJugH6XCO5gTk4M6dixFijZAKPIabxYnm2deO5rdE_EoX5zPPCiAioTaholSosszz_hj_ew8bA18aTDqrELGC8R_d2jzzwiJoYqZBgglbVOabzeWqmDEMzu36Kjald1ZWlkaphWpevsTtjS91QE_qxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.
این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6082" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6081">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏
🚨
🚨
محاصره دریایی ایران از فرداشب ساعت ۲۳:۳۰ دقیقه اعمال خواهد شد.
‏بر طبق قوانین اعمال یک محدودیت تازه دریایی باید ۲۴ ساعت قبل از اجرا، به صاحبان کشتی‌ها اعلام شود.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6081" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6080">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=W1Dpbm_ZXqh4xzIClc0ZtFrozERnlvp9JfM-42WPvluCt524Ll3uqt41ThxyY2KVZ74pcEQDuhfLqktf_-L3-KDoAbIvTdvQE2EDmguhxTl9xDwHhmlc-q52QgYQ3OVEiTx8gW624JkUV5hb2k1lztEFd5hdLFn-oKWP4IK3OtOZ0Vvc0d-aJZKx5JPnz0Q9jnrxaA2Gl6WJ2BMZC9V5jSlg0ulyrT9fsIigcejPrqFbxSsu0njG8rzCjpFirhXgDJXYFQTuNRMO5dyWu-BFddRK6s8qq7eciT4PAK7bGdQUsHrHlWv02SYnq24re565Hk0wusnpZF7reKaK3MPhm1Nlujjb9ljFXPnA8oZfN5Vu7oFfcL2KuNEK9-YCrzIXW0qYxVcszqrh3csSAyX-FFppx5tJrvQE6vsjwQ37eSJ9_IzD5lOa2j3j3_Pt_7_POzsxpBWb4wu5Q_WWeBFG4iemdOiT4yBM-WpI-cs9zF-DAQUb-os7JQgR5SeyG-_qtFRqg63ulbdbqlxZmu_GbWmQGrMv1I86bL5Pv4LrDrCx5xt5NoPwn8thRUR2MBR1i8PvW1-X9_1UfsqZsUVuhvJNKp4ORq685Mgtxw8icuxFAUzAOsKxfoJL1alcvbNLuPOu2ETe6uv63dGBi-CDEBWUExsxotwlk3dtgEQHZII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=W1Dpbm_ZXqh4xzIClc0ZtFrozERnlvp9JfM-42WPvluCt524Ll3uqt41ThxyY2KVZ74pcEQDuhfLqktf_-L3-KDoAbIvTdvQE2EDmguhxTl9xDwHhmlc-q52QgYQ3OVEiTx8gW624JkUV5hb2k1lztEFd5hdLFn-oKWP4IK3OtOZ0Vvc0d-aJZKx5JPnz0Q9jnrxaA2Gl6WJ2BMZC9V5jSlg0ulyrT9fsIigcejPrqFbxSsu0njG8rzCjpFirhXgDJXYFQTuNRMO5dyWu-BFddRK6s8qq7eciT4PAK7bGdQUsHrHlWv02SYnq24re565Hk0wusnpZF7reKaK3MPhm1Nlujjb9ljFXPnA8oZfN5Vu7oFfcL2KuNEK9-YCrzIXW0qYxVcszqrh3csSAyX-FFppx5tJrvQE6vsjwQ37eSJ9_IzD5lOa2j3j3_Pt_7_POzsxpBWb4wu5Q_WWeBFG4iemdOiT4yBM-WpI-cs9zF-DAQUb-os7JQgR5SeyG-_qtFRqg63ulbdbqlxZmu_GbWmQGrMv1I86bL5Pv4LrDrCx5xt5NoPwn8thRUR2MBR1i8PvW1-X9_1UfsqZsUVuhvJNKp4ORq685Mgtxw8icuxFAUzAOsKxfoJL1alcvbNLuPOu2ETe6uv63dGBi-CDEBWUExsxotwlk3dtgEQHZII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی جدید قرارگاه مرکزی خاتم
در خصوص تنگه هرمز
ویدئو رو باز کنید و به چشمهاش نگاه کنید :)
یک دقیقه و پنجاه ثانیه پلک نمیزنه
ابراهیم ذوالفقاری محصول هوش مصنوعی :)
یک انسان عادی، هر ۳-۴  ثانیه یکبار پلک میزند، در یک دقیقه ۱۵ تا ۲۰ بار</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6080" target="_blank">📅 20:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6079">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQJHBRdSg3YAfBVWpbd7knF8mWw1dP25ewOBlslqk-_lgS7xwXWQnsm5Be7K5xZc9URwoYZaxUzccQrde17NXQej2qfsV-143VFVVBeQNMqKGF9URFuh2qBw7qM41aK-p91oHOcrioPoh5VRPdWNZ7yZYhm4sDyJnKn4l2jqRVDSjPz1Zn7qeHhemysj1YQy-L6XUmayVyrl61Qetj_04De-KadpVEAuWXSfUMD-k9f3y3dPvLFpyzgCK3cOT2Wlq_I1b1wCG9Bb4vKWRXvaq4i5bWVXyxJBIZj_l-rSCcX1wdr1ndTVKkf6gtoL4YXS-BCH4qz3Ac-lY-YM-PY5ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : از این لحظه به بعد، ایالات متحدهٔ آمریکا با عنوان «
نگهبان تنگه هرمز
»  شناخته خواهد شد.
اما در این جایگاه و به اقتضای انصاف، برای جبران همهٔ هزینه‌های لازم جهت تأمین ایمنی و امنیت این بخش بسیار پرتنش جهان،
۲۰ درصد از ارزش تمام محموله‌ها
ی عبوری را به عنوان هزینه دریافت خواهد کرد.
روند اجرای این طرح و شکل‌گیری سازوکار آن بلافاصله آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6079" target="_blank">📅 17:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6078">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rw1NBjjOlknWr70s8OEfLS_TuvtQcgnF9G6jx2Rb5or7lp111IMUFg5Sfl5VciVXHOe-fv_ex4TUW-0-hOvngZe5DI3JlIqWP9XNMaMrzM97Gtu4VPdTdVGkCFgnKjt6JbVG9jJfgceCF-ab49dLBtoLHu5-gD3amkhJlu-6ut3lTm7ysfpahqLX0M5DKnQPfDSKbSblPEgswerLFHgneomx-eXFyaHSfmMMzunASg_lCyQOFEGgdJUO-0oB6cxy8BYIQGtKIlCrjqDehfP-A7REGHBAlScLeTNAL_b5CmdhBVBjMHpe3JwW3OSMEY2DRu0slL7YOKpzfB1EDBg_DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6078" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crDfMRckaIEiYPMm8cyci01xOehXX-S02xbYYGYFB846Y7pm7PMYcuwbRQrLNgCX2YkhSRYgsC1PZOvh_pK8vFZZrQ2aBj6jBeeosH_esvdjnb--xvxbXAHsh-QilWRQW-m340keqio0FjQe9R4XT6zBHNGlVynwdhVPuzrv2g_UoDbwqXeEYxCgePnrLbgdrwczimbYX1iF9ZsjCxIp2aMmr56N523Bc4S_jJOPt4G80JvYhkzNs8razLTy1qDWdY9kVSejnipoep0tgWaWnTN37SsxPldFe4GIbSiHRZxyWJ2J4mMuy9wHgeP0zBdjXjc_iFixCK7ess7VwrxQsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6077" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ درباره ایران:
‏ما کنترل این تنگه را در دست خواهیم گرفت. احتمالاً مدیریت آن را نیز بر عهده خواهیم داشت.
‏ما به نگهبان تنگه تبدیل خواهیم شد و وقتی این کار را انجام دهیم، هزینه آن به ما پرداخت خواهد شد.
‏ما ۵۰ سال از این تنگه محافظت کردیم و هرگز پولی بابت آن دریافت نکردیم. بدون هیچ دستمزدی از آن محافظت کردیم، اما حالا از این کار درآمد کسب خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6076" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
دولت بریتانیا سپاه پاسداران را به عنوان یک
سازمان تروریستی
اعلام کرد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6075" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">عربستان برای مراسم ابراهیم رئیسی «وزیر خارجه»‌اش رو فرستاد! برای مراسم خود خامنه‌ای، ولی امر مسلمین، این بار «معاون وزیر خارجه» فرستاد :)</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6074" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f91JV9rMlAdUJdGKRnzCy23fWNlc7djjz-rUyQv3WPhsL51bkDOxQFpqE0rQpl5nJTZ8t38XRoGvPnhvRw6yAyY31iM-ESWoGCzZtaA-zGUdqZpeai7C3h--BH5Ex0vD9G88jj6bB69_P450bVyVZT_GNjoJM08zL1iZINdXjcqKGnuUxjGpAAwTzeDbnls4K4hnXyeQ4VtAmsyHBjNU026chd5R65x7R6J9BgIZRAc6vd7K5QhaJ4kzY3cnmK6isSk2iaOpIIoU9VnMlv-c0pnuY3gADk3bPOyvaSjg7C0IaUkQ7qoxZJWVTO2Tvwff4IC_87KUGnrRMV4k8cjpSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2StTAWpLIUcKw4e3gul62SmgnDJ4G82cl06vcF20PDgIS4Ld3HDs2MHoGy8AqPU5vbSurebeCtZJxtxPXXoePDUFmTTV8JUHRx8yZyMZBXLpAe0ZAWLk_K_OMpOF9_zShEXGETJD1EJ6kXZGfF3NUrshRs5wLsmJ_iOSgd9jNDpBRdP9Cbmz_mQCQq0U9hpnQkzpaPIBOf0ddGkMUYSfI-7VOevSZkSSf-xhltSnp_qhIHIQSNB5bbge5mSrVCGnNmHZ-MkwKSUGuMKbSXm-UFf4ZAEi5ipQ2kaCuuoqp_lZ3IT4DLzf4NPwGzGdiZLLYQUn0IDhCaKRQ-ENobWyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»
شخص امیر قطر به تهران رفت،
همراه با نخست وزیر قطر و وزیر خارجه  قطر،
اما برای خامنه‌ای،
سطح هئیت قطری به رئیس مجلس
تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم
شخص خامنه‌ای شد!
از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی که قطر برای
خامنه‌ای و رئیسی قائل شد،
خودش به تنهایی یک توهین به خامنه‌ای بود!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6072" target="_blank">📅 13:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6071">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_VijeakzLzicNfuc_2G8liQthE3yxtR-o1Igz3rAPQPUqdgrXp_VksiufbUAaLPoMqjo3oFxWeyCDtVM6Fra7wAt55HthtMI24ZpNvPVNx0hcfSQ3fsmMQ6vlWfY25Uy5fIWgYZ1sNLRfTbovRi-WzsW34hbPLczVYrRlmkhDTtiJERW-42rlUAyq9ejPrtz355RJnQVhvNowNQRPUjLzMCEAptdgx6KvEqYOGpqvgv_6kAqjfsDibGr1nzZNIBzKvf4YdubTGw_vRCvPZdxv_xhG63gzv6wewH9qui4JWB1gNlmyNMr1tzXkPrQoKddhSMQfly-NiXVmJLGy3mrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مناطقی که در دو روز گذشته
توسط جمهوری اسلامی مورد هدف قرار گرفته.
عمان، قطر، بحرین، کویت و اردن.
عمانی‌ها از حملات جمهوری اسلامی
بسیار خشمگین هستند.
عمان همواره یکی از دوستان ج‌ا در منطقه بوده  اما حملات مداوم ج‌ا
به این کشور باعث شده تا سران این کشور از ج‌ا خشمگین شوند.
🔺
بعد از اینکه در آخرین روزهای جنگ ۴۰ روزه نیروی هوایی امارات دست به عملیاتی در جنوب ایران زد، ج‌ا کمتر به امارات حمله میکند.
🔺
عربستان هم در میانه جنگ ۱۲ روزه به طور رسمی و جدی به ج‌ا هشدار داد که دست به حمله متقابل می‌کند و ج‌ا نیز رویکرد خود را تغییر داد
.
🔺
ج‌ا در هفته‌های اخیر بر بحرین و کویت  و بعضا قطر و عمان تمرکز کرده.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6071" target="_blank">📅 13:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6070">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5qkFTby4DiOr4dB8BhDbr44PHxInGCkM_Igs6NHABunZemRIL8sxHqYKjafXiVYUyiFFQa-al_9ISo6_n9IZFIVnZwhQlYUHfpkNRxLgHVIaZsCrNb-YE6A6fMKirnZf6z9_KrqY8T-5E3hUVtQn-ombH_0txcpb0u6EIWWVEToItsjNfSHnCeEn47VKEOXpIV5gykG6tOuI1-vbfLwezIjJXnLb1xo48D9ul5celRof-2RyFU0WAFpuo6l_q6tum_anLRFWuxYIna2rBeTACW_ivYfCk2P_xXN4Uy5awNJEGAQ41kYKy8VD9WsJQK7kxi5kWQDCJv1tQhjW1t4R6kVk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5qkFTby4DiOr4dB8BhDbr44PHxInGCkM_Igs6NHABunZemRIL8sxHqYKjafXiVYUyiFFQa-al_9ISo6_n9IZFIVnZwhQlYUHfpkNRxLgHVIaZsCrNb-YE6A6fMKirnZf6z9_KrqY8T-5E3hUVtQn-ombH_0txcpb0u6EIWWVEToItsjNfSHnCeEn47VKEOXpIV5gykG6tOuI1-vbfLwezIjJXnLb1xo48D9ul5celRof-2RyFU0WAFpuo6l_q6tum_anLRFWuxYIna2rBeTACW_ivYfCk2P_xXN4Uy5awNJEGAQ41kYKy8VD9WsJQK7kxi5kWQDCJv1tQhjW1t4R6kVk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56pmVUP92VnZx4ffOvY3kixmnTEegsMwPrE73ESavXu8njoyao5LKctda6CVUk_IzLTmWcUj9vdMQFB8vhepo6sAoZNi-wkridYUgkVcUvRltTaSaTvVHZHeckcxpf8N1dxc3_WRvArIE3t4JxFr_nzEb9t_ehZYABi5nCG5njrPUOEM-A1H5z8GkZ8c3IEUy5hCMO3jgCYBU7fPpm8A3JJnHRpQkH8d-MzFJ5suhhcVn7WjtixKVIVr1SSI2s-OrMsPJQI0MBPhcMzTEoAy0aBllsGWYHBx_sqT1r2lu202acC7G2LJv0L1-G1JsvoBUuQDSF-U0RPOys8cdhIhAt1QY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56pmVUP92VnZx4ffOvY3kixmnTEegsMwPrE73ESavXu8njoyao5LKctda6CVUk_IzLTmWcUj9vdMQFB8vhepo6sAoZNi-wkridYUgkVcUvRltTaSaTvVHZHeckcxpf8N1dxc3_WRvArIE3t4JxFr_nzEb9t_ehZYABi5nCG5njrPUOEM-A1H5z8GkZ8c3IEUy5hCMO3jgCYBU7fPpm8A3JJnHRpQkH8d-MzFJ5suhhcVn7WjtixKVIVr1SSI2s-OrMsPJQI0MBPhcMzTEoAy0aBllsGWYHBx_sqT1r2lu202acC7G2LJv0L1-G1JsvoBUuQDSF-U0RPOys8cdhIhAt1QY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ارتش آمریکا شب گذشته به ۹ شهر
در استان خوزستان حمله کرد : اهواز، آبادان، ماهشهر، بهبهان، شادگان، دزفول (پایگاه چهارم شکاری)، امیدیه (پایگاه پنجم شکاری) اندیمشک و خرمشهر
🚨
بندرعباس، قشم، جاسک و سیرک
در خط ساحلی و «خنداب» در استان مرکزی نیز شب گذشته مورد حمله قرار گرفتند.
🚨
جمهوری اسلامی نیز به اردن،
کویت و بحرین حمله کرد.
🔺
ویدئو : ارتش آمریکا این ویدئو
را از حملات دیشب خود منتشر کرد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6069" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6068">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در بندرعباس،
سیریک، جاسک، قشم،
سنتکام : از ساعت ۱۷ به وقت نیویورک
(از ۲۵ دقیقه پیش) حملاتی را شروع کرده‌ایم.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6068" target="_blank">📅 00:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6067">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=AxuRhSj6CikkxvTqhdb8l3bg7h4MrjMvyD0jmivnnZMy3n76R_jIeprsOJjIKgV9cR2klS9ujuP10dKSE77yyCqBkgeYvgheB3xnUFmh-Od1mINFZYsVZxOQXobIVIQT2231HyBUbCCK-NtlPbLjxGeL9ZcN69MSjUCBcjWtz1_-gtBX6DFu9aoA8afIpRiNaLEcY-Zl-g2hPRKMc-K9o2eEx8SOyN8skHeBFA4KtZBG6M7H9RBPW-oqnpGI4TuNK-aSpCGpe5oqJBGR9Rp_7neu3X3N-KEqxcuq9zqvhTw_LPYRF6OTEwcPYO16Frh2zoL4bIJ88p2RS9KQXf3XZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=AxuRhSj6CikkxvTqhdb8l3bg7h4MrjMvyD0jmivnnZMy3n76R_jIeprsOJjIKgV9cR2klS9ujuP10dKSE77yyCqBkgeYvgheB3xnUFmh-Od1mINFZYsVZxOQXobIVIQT2231HyBUbCCK-NtlPbLjxGeL9ZcN69MSjUCBcjWtz1_-gtBX6DFu9aoA8afIpRiNaLEcY-Zl-g2hPRKMc-K9o2eEx8SOyN8skHeBFA4KtZBG6M7H9RBPW-oqnpGI4TuNK-aSpCGpe5oqJBGR9Rp_7neu3X3N-KEqxcuq9zqvhTw_LPYRF6OTEwcPYO16Frh2zoL4bIJ88p2RS9KQXf3XZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=IMxchWGYSuIvkrJkuqJ08biQaBetW3BtxkJQ5vBQbzp_TY3Xx0mDc8U3VoSx7ZIyMy6XWMJe4r0PjgDdYcBZ33irBO6NAVbx_Ga9qCXyRiZwJPRDNIfTgjR42qyXOyqyXsIncwUJ15OMQDdWGIRV4dm2yLUORvEO2HTPi2nT0LvLIv8DMzoJehpD7S4jkiXYcX6XVICbbifIp_fjWUVdAwe8wkX98cvsKSbO8enLVyyXSIICn9OFwQ3KU7Y5D4KzkhcQ2H5BMy9EJAclIXEAzvjr6bpiovRziFWByzSiLONyIvWEG7Ne-qNXsfq5RdJbF4MzSOjftlUGVhwlzAfunw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=IMxchWGYSuIvkrJkuqJ08biQaBetW3BtxkJQ5vBQbzp_TY3Xx0mDc8U3VoSx7ZIyMy6XWMJe4r0PjgDdYcBZ33irBO6NAVbx_Ga9qCXyRiZwJPRDNIfTgjR42qyXOyqyXsIncwUJ15OMQDdWGIRV4dm2yLUORvEO2HTPi2nT0LvLIv8DMzoJehpD7S4jkiXYcX6XVICbbifIp_fjWUVdAwe8wkX98cvsKSbO8enLVyyXSIICn9OFwQ3KU7Y5D4KzkhcQ2H5BMy9EJAclIXEAzvjr6bpiovRziFWByzSiLONyIvWEG7Ne-qNXsfq5RdJbF4MzSOjftlUGVhwlzAfunw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که این ‌تصاویر از نتایج‌ حمله امروز آمریکا به جزیره قشم است.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6062">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=nz71kh4mfK9-1jno4GgFGGTYzhAPXNEctDmLaRL9SLTkqYliCZcHJ9vlCTUoh7NbghYhMd3wgWsUSueqK3bR5WbcPDYEPQQXPjiUPyEyouY6zTrCpixJoavtgLE6IvlEivrlEm-8l5zoTHP_rje6k-GmUG8FZXdCy9DSWCcvrCafWY-avZa66Sh3VU6EZoGIR8u56EN0LXTPKbvW6ZV0QWwrm3JXQ76-YGALZoo0aMoY0QcBipnw2Miyco_YBobCI2CWAvgSDQwFS6OR0lrZqcFs5iSc2I9SeEWmUkKdMiU-kmCw9CZOYoUX7WqQvzjvRbAK-X47pqwfhLtIqsUhTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=nz71kh4mfK9-1jno4GgFGGTYzhAPXNEctDmLaRL9SLTkqYliCZcHJ9vlCTUoh7NbghYhMd3wgWsUSueqK3bR5WbcPDYEPQQXPjiUPyEyouY6zTrCpixJoavtgLE6IvlEivrlEm-8l5zoTHP_rje6k-GmUG8FZXdCy9DSWCcvrCafWY-avZa66Sh3VU6EZoGIR8u56EN0LXTPKbvW6ZV0QWwrm3JXQ76-YGALZoo0aMoY0QcBipnw2Miyco_YBobCI2CWAvgSDQwFS6OR0lrZqcFs5iSc2I9SeEWmUkKdMiU-kmCw9CZOYoUX7WqQvzjvRbAK-X47pqwfhLtIqsUhTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=Z09SPqi-0ET9rbXsw_wQ8XtGIOAdloReJuBjz3rwjFpsNUG1cEtUhbhGMjTLF57RJ1eTvufOqIWgDj5fCwbcoRKexFyInXlpvdClGL_2g-QZX1RUkjilJip_sOHp-g5etwWbwQieVx7MohSPOuMpe20BbmLHZb09TLNp5dMjEU83neTnP1hfEQOCh81fOlIrPt850ks7Cu5QTCZtHH4IFu_l0QSvwIRPwOdUV7cKUcnVnql9Q92mUihD9M5E0eQlhNwTcttBwDSkAw4lahnX6E6XmrdfyqI0WQozdxBChWqAT5lJXp8imu3PXwBjidXsvkrBexY-NMcAm6qCVyeUNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=Z09SPqi-0ET9rbXsw_wQ8XtGIOAdloReJuBjz3rwjFpsNUG1cEtUhbhGMjTLF57RJ1eTvufOqIWgDj5fCwbcoRKexFyInXlpvdClGL_2g-QZX1RUkjilJip_sOHp-g5etwWbwQieVx7MohSPOuMpe20BbmLHZb09TLNp5dMjEU83neTnP1hfEQOCh81fOlIrPt850ks7Cu5QTCZtHH4IFu_l0QSvwIRPwOdUV7cKUcnVnql9Q92mUihD9M5E0eQlhNwTcttBwDSkAw4lahnX6E6XmrdfyqI0WQozdxBChWqAT5lJXp8imu3PXwBjidXsvkrBexY-NMcAm6qCVyeUNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRWdK5J75V6lVCeVxn8RKBVt-FKaJVpGGEdgqiLFsl9hc_s3drHa6BUG1D6dtRVkl8z10Cj3pOdiww7n7hNeIw_cmG9zazRBm0AihdHaMEJ2FJw0KPYHh3twuW8MQ8hDCyst_li5bvW9g9HJvspGblQtxaBmh-vLya1tJ1RGqB7Xv0buo4j-SmsLwpSvwccB3PDZwS7ARg7R6bwPe5fgXCw0s-vI7YPPYENBFdaOWeU989YMjicU0zyeM3puiDUdcGOG_yyNJL9pMO5mZ2icfDltnCL33QMEmvEJP-5TrvSbqft8WM3g5YG_pmqcp29EShiVlReUwPF5CnJ7tWBkAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»
بیاد بیرون، پوستش نور آفتاب رو ببینه،
شما هم به جای هوش مصنوعی،
قیافه خودش رو ببینید،
ببینید اصلا چه شکلیه،
بعد به نتانیاهو بگو بترس.
راستی گفتید مجتبی دقیقا از ترس کی
۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6060" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vqm_c_d6P2BvphqPY4NNfcdE9zeL0ZMEFLKCRP-BOsHj2LDIfW6oGqYSlzrVaZVM5tlRBzZQ6KUx02JQ6QV8rYGCXuodyzSUJtwr74Q4PaVfo_aRsq_bM8nkXyL-0jeidXvUa0bsp4vV3fcrJxoQYF3acfJghM7nM8FVaxQIUzp5h45tRq7PtgDCCD0D1qmYeYss42pkiKpFE1e_K3kHUO2zc6aH8tMlHZiliTD30drqP6fL5J_UiLL7oTq0TBWYNgJLbFh0VwUtJwtQwyKnDOhtVMQbFW8VFzh5l9Lt0-1_DMl9QMAYBA6t8zvpnJvZ77TwoQE8i3eDVdwr6cZu8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=FnJe7c97r0UOruHOoQVZQXSMDZQwZXJxgKkEvmCxCdJK8GipCcYFxQnXZ9CgzvFnAoVp1ZZNXMzGkE2_PW1tS6m5SVKY0KF_aQLUmGLhQR87n4DsbPrkZPiEHuAKCstos0QBHkyk8BCp-gQptY9dRonxqVWI5ik-Y72Ne8weeW2C5FjzdZM_RY-zY7iUm5aCwfr5O7fL1usGgilRHlX8Yam-LrtR9b3zUDCP-qBRB57PB4V_1SZ08t7cWiE9LYeF7zaq0KTWPi2RZuehxG6KLXmQGJIvW8vUS0Qc3WQOGtOe9o31tLtKl-QNxud2U6sDpuJJP_r0a8gn2LQv8diIYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=FnJe7c97r0UOruHOoQVZQXSMDZQwZXJxgKkEvmCxCdJK8GipCcYFxQnXZ9CgzvFnAoVp1ZZNXMzGkE2_PW1tS6m5SVKY0KF_aQLUmGLhQR87n4DsbPrkZPiEHuAKCstos0QBHkyk8BCp-gQptY9dRonxqVWI5ik-Y72Ne8weeW2C5FjzdZM_RY-zY7iUm5aCwfr5O7fL1usGgilRHlX8Yam-LrtR9b3zUDCP-qBRB57PB4V_1SZ08t7cWiE9LYeF7zaq0KTWPi2RZuehxG6KLXmQGJIvW8vUS0Qc3WQOGtOe9o31tLtKl-QNxud2U6sDpuJJP_r0a8gn2LQv8diIYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوینده شبکه خبر جدی جدی
خبر درگذشت لیندسی‌ گراهام رو دوبار خوند :)
فکر کن تاثیر یک سناتور آمریکایی رو
در برابر کل نهاد مجلس خودشون که ۴ ماهه
کلا تعطیله و کسی هم اهمیت نمیده :)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6057">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6E921P7SOwJAoyBcFz2q3DoJMdG7ziXgWOnNo-ez3g-kPcpi7EYeyp88NJ-F5wyPciF-sj8AKLc46I-b2MR38jJBCnZgEHoP0a30jFjFFot6KzNAtiuTB9HHWj70iQtM1ON_Z3MlV7sTX-xj9Fky3HP3DXMgdhkUkltUHCm9nep3OP3qd-QPEyxn2XtaydZJeDdbd-eMhyKb85uCSrANu3INlMDrE6hmpNw8LrhQ440DzzIAaSDyHUSXppuheihHvugYNS0JfQiGOKqvPsVd0QIc4Jx1HrfddMFZspr9ShgBm9HdmhvNuYVSKtmSZ-jjcE0OOoZDNkw1G-_lHQWOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این لیست عاقبت و نحوه کشته شدن چهره‌های اصلی که در کربلا نقش داشتن رو نوشته،
خیلی جالبه، چون نحوه کشته شدن اونها تفاوت زیادی با نحوه کشته شدن افراد در کربلا، یا ائمه و… نداشته!
یا با تیر کشته شدن،
یا سرشون از تن جدا شده،
یا تشنه بودن و کشته شدن!
مثلا این رو نوشتن که ببینید عاقبت اونها چی شد!
هیچی! همون عاقبتی شد که مثلا نصیب بزرگان اسلام و شیعه شد!
مثلا یاسر و سمیه چه مدلی کشته شدن؟ به مدل کشته شدن سمیه هم میگید عاقبت بد برای کسانی که مسلمان شدن؟؟
در مورد یزید نوشتن در حال رقص افتاد  مغزش متلاشی شد :)) از روی پشت بام‌ افتاد؟ روی پشت‌بام می‌رقصید؟
بسیاری از تاریخ نویسان مهم و اصلی از جمله «طبری» و «ابن خلدون» نوشتن مرد! نه در حال رقص و نه متلاشی شدن مغز!
عرزشی عقل نداره! با عقل دشمنی داره!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6057" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=LtgkmUcTurivln4NTBASgVwp6avLYaxj1uK53TP6aj6LDE16__PJFYIYuGldIohnlxFvnTy5-MGxSWbKUNzuBY7ifF1n07Xu_N6400dd1CUg0bjIY0FghJtQO4tfpSWndA5NDu41uVK8_i9PEO0VPkdrchX1D-qqBhASGFkfdHTkPCsMjKltOOEcSgzEvg_PmL-5i72hVpCcs0IsVOc5eMxReEF6uLSsq1e5gpY3dLSgVIaAjbbFSFMf_RfCaFnlwik4oeryQwc9zIuqK2f7nYEbxHJEJWIugt9uTzeznndXgvjCltESgHxrUt_LV_R8x4gt1DYeIYFaoCzfkuqhbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=LtgkmUcTurivln4NTBASgVwp6avLYaxj1uK53TP6aj6LDE16__PJFYIYuGldIohnlxFvnTy5-MGxSWbKUNzuBY7ifF1n07Xu_N6400dd1CUg0bjIY0FghJtQO4tfpSWndA5NDu41uVK8_i9PEO0VPkdrchX1D-qqBhASGFkfdHTkPCsMjKltOOEcSgzEvg_PmL-5i72hVpCcs0IsVOc5eMxReEF6uLSsq1e5gpY3dLSgVIaAjbbFSFMf_RfCaFnlwik4oeryQwc9zIuqK2f7nYEbxHJEJWIugt9uTzeznndXgvjCltESgHxrUt_LV_R8x4gt1DYeIYFaoCzfkuqhbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDJ5mZ8YW7bRM3oTtw_5dsNY4He3iV_nAqRCNZQxy_YICBliLFBmZCbWYpv8MoApNxbodcuxLyNUw5Ut0d-gyqFa7FiHVL9tN8v9draQ8UrWqKN8qaw1cALEXkUQUR2H_oK5LWpGV7cSVuqfZ2_J4q410Spek0auZ-KbDIC-hEs7R1C0naMla4TsiZaj8zXl_1QMP_uvlf_mklfSMUQOLpFmfAzdRtW5--LBp5jKP6AJLtNeG9Y21lOuQ7unIG-8h6ancw71lMG96eATH2TL2k8GhvBm_q3GN873mkfym6nc1u4MNobDLvUOV7RlXQeX5IojB83rLf4qdATvAjz1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم این خبر تا چه حد صحت داره
ولی ظاهرا دولت اسرائیل
مهر ابطال به پاسپورت خامنه‌ای زد
و خامنه‌ای از سفر به بیت المقدس جامونده!
او هم به یاسر عرفات و عبدالناصر
و خمینی و صدام پیوست.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbhOUNu-jsXXACwd-iTrHUxIxgRHDlC4Lm32gsQZrdcIjZ8rQlYWOMsdM70H0DC9L-uwQLkipyjT_OCDnbLHAOKhTOhDEBKA9uqJn2Sz2t1SEpT83P-v6qi8IN1NF-zx_I0zSqslbgyDlJ2mc243I6qRurrehXkTiuXpRDVm8d-AJEJcn2rk1AeuLzM4Y94Q9uS78FunH2FC0D9lM0oNszReoqwdWPzlJDTf6c8MUlaOPSWdbY6QYJkFKm4pilSP7Yby40VrvCmm4Fn-JR5dtmqJpDcIa4X13ZKqjoio-o3yLPzdYrPqb3I_RNWJDfKSoqLI01IELQc0xn8qmAvTHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDToyRPMqUE4OK6QjdBS_rMsoriEHinGCZJksxcPtr9Vuv1QdFIUdZEpIrbyn2CqOrreKZK9F7uzTerwVkrGn-YAFcLH1yhKuNAjm865MCZM88DkYYPYXf7iyyjGhRlLslQWBEeCXdEQT5ME-YsciU0lqOAuGxIMosQV25lIMO8oKHkFG1I86eHBqH9GhTO3FkpGQ4znKmo9BJGTw3o8YR4E_jLILYTQO6nkwRi2gStnuXwg4NFR2U4ZefW79gdVgtMhG0yIRX2L-87bYqubQCLTigmBwZ7zexpWDdR7qHYAxwxxkFezS8k6JIC2-cV837uBn0WuSOAAlUkYm2h-9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGkc1v2wLSRDTYWPnpv4uT5tLkuhRsP3RP8EcnbzqpGeQh3kO9Gg4xW4PqfefYm9duW0GmjG5AgMTY-ugGuk7MZsHdZIvBwCHFvqO7hUFk7XBv85NOdfDNMiGC4NfRfUue001DFgZ4EkyZtQhLA9sc90IF9cJtVGWL4hmwIq4H1gRadNnB4S891SC2rmxv9pcLtZjyv3tbt9wnkB2229_VpmDuW32WAnSqLQ4hkcBmde5TqWUZxACVWo55xpGBINqPQ--1ra2uVOYUs1yf44NriIZuHooJ-Eu_NJNQfVA1cBuXvDAF5NFVRyRxI8D0sIJWZ-Jr-s1mtju9FDNjRznQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SRY7lu0zmLnaGcyAS6xmuGzLr-nR7OR0jadPk7TwWT-JbO5_zHVVGiKyDneslEXLKF_YJ484JUNecxWMdguMxZQFhqdEVb-QL639eC8ybgd3qYzvfKLYfXs35a37hcxlZjCJ-XGU9Yibqlsn_hm1ZotzFRw0ScmsG2EXbw32RI-a8BPGJ4cDpbozaaBTiKJZOPLNbR1G_j_keMYPKc7ZrEIlK-f6Mw7gKcAPBP95Vbg3QEs-vgtYYsv4muIi3xakFXE1MFHjEqwtrAy5xsidPvf501rzC1IUTj90MvSc-vhQrarTsJJ4hJVkp9K5abU2gXfiIrNiBWkY4Ri1we-ixQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Km0p2u-WzFHMdsrkt9FdW1lJycZlolXDl4EaQsRdfE650nRrAAxZF3s3SiPhAhGq3ZEwjsMhd5km4UIEZYn-onPCmCB-GLChhIOxaGd_2ebZIOQmLpl0UpSohJU5lggNbr9PWPdNA-1hOJ9PSoDee41VECQn8ncRlWGCYsH3_Kgp_qCCWs2Mt0KougtEZlE1NnhZkG86d03wY0RTQO3ND8jto_hBJb59Gztyx2Daio9ekKC8SZWgDFIp1C61-iKOiX8Iu3zljcy70FalM5GTnyq8w6bk6ZL7cbg1F10Zgmouh63o48GfdbNiGV3GZbFuLK2Qgshb2CrO0s0mYMCZKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIAGW5BgntVN7xW0ABJFBNJnR21TisVgV0FEwi5TWHTUStRPfQI7Facpd2f57V6WhcRK88srS6EtRQq0NqAzssq3EKAOzo5egbYcgu1xk8XFqwo0RO5WQhu2bSxSXcJYdO0UMTiOXEYaxx7fzezUv1ci7zpLPJwgx1CNqFFgj7ms-5wnyuvb5zOJiw81jklqh9Sa7BZZQx3bACQnMbqWEhlEO9ZxFvdDklT3czgRXpCSDnNsALZI79vKA29O4faAk89yeLgJ7l98f3y0MmfdFA4DoYa-h4ox4hdZCNilPhEKb9KhEQCnM7olO9YRIUDniQD1ij2DI_HUSSdNp8Sy5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMYKNt0HZK8WZvJZJsecOX4jKoMuaAX1Bmg6_OOdVuX1XAwsdX1qQzitr2SVZ7_mUrsWX4yUg-FBscHsvJyFLX8fUsjOUCSf7x6HxHqboFi7bQEJe0HZ4jz2BA5oVZfsEiLTusSBTxp7Fhf2s-aYYUpcbp85bzlkF0ZgfHpDK2ORpwteyrju2uVVWZQOpfCa33Rlw7dTEdaiY78eob1dgjkYbWrgFpeIiEQLWlf8G8Zt-jcxno-tX5XSs9KZQf_L5Jm6u71n5ogfcuCVpsIkGl0MbrM8qNIdL0q_Pat3M1MxtSmLbJ8a2dJzc0ITK8TO0w8gqTCXusUgByK-lfVwuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Avyv521ud0paP212nBL4KzXlCGoZdGXkzB_pbxdtXtDKq11R-jTb8ZEKTQbX1XLw2P6s9BxPmp_eo8FjSkLxvQp4JzEbceI6N4nvqqInKPc68yY6pa4TIanxAtnsmfSNvHaA_5lROfSJR-_9Y0Kd7dHjF3-Or0IoEUurRW0uPz-61AvRveD-mlxI5sOx32AAohQd0nFQZyiow47WDvqi9-1H8MrWLHc4q6olE97X3ObFSpPaBR6IaAcQ_vxZEM3BGX2OrM2zx_LQevCqVfolZmZnojJ-QPGh3rV1OjAGB-HGnAKAsflZnZXU11bln1vgQN133K8I_-6_txjkrfwO2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر
و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)
که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار کند است.،
🔺
خلیفه بن حمد از اقدام پسرش برآشفت
و این اقدام را «غاصبانه» خواند.
در سال ۲۰۰۴ با یکدیگر مصالحه کردند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6043" target="_blank">📅 08:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFZoQ73g3v1MzNgX_wrCuPffGkX3CZJtYf8qU-mGVIkinbW30GnYv27JAiyoRGZapag61qq1yRBP1FSMx3rUqVh8PjRH7xAf_dD49oHbAVwqKJahWlD_QIbTjgWScTuGt9kc_njUx51DvBGoZ13Xvin30RXjB0EkABQmEZdKdbg2Ka8EeWpmqbPWwTwg2yBHoZUljuoW9zLKGeGY-JngMJ7o_Nxea0Huz4HpP83AhSq86vDodndln3BMo7b_T_z0WzG5-aDfuwLl1xGWMD9PaNWfiDIrceyAw30ek8qpWDgXMVn0xkg13UJ58PZAUB8jVLIjSQYm9hYfwH2T4-cEqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saUx8cTXe_UsiTtaZzoLtpf0YD1GW8LB3x1EqiZ1a0pwn37hEMV9wdj_1BSMauAYsHobqAP6G6QxjKe1F7PflTbE-Rro3Z-h2tszmN9Uh3WNQCVoX4LpmGs0DF5cTnC6wRvN5wW0ksy6_UwXFA-kjRnNp8tTBSdMfpQZjGwt1UUwZeXWMhZzPJtjxorGgUKCDYkqxR92Fh4z8WRYOTN-CkmFjK0Wx-S9Hd6VSxHy-5lnHwIHY7Vj4A7PPJXCTXU9XDgERJLeb3lzEEniRZzJrpyVSE2wjI_Qrqwkz48ejBrB-WiVyZqJ_gEAmsiPvgmvXjmFNdzd3u6V-QhMfVJ3Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=N1_aRMtKFuqy_EGmr9_Pl86KLvzswNk2kvQbuskC3SeW3W8Mqv-Zp4oliT9DJW9a-Sl1_Zq5n57BgSvT7qDaR_RN1Mq2fGhHe4htqL0I8K6JvHhL-3jNexd4tCap_pLoyDJ1K5sPivkdEEi7wuDsffZBJVCQUobdpx5TulQqA-J6PyJtbxDAe7FsBNhKV73Y09VjkLXKFQiaQsy80edxM8vTEgqiQoJGIMGuuOCh2MmsH7QTsh1_U9dE8GFHPKULo147hlhPv9WQ6e9pRNxx6Vz_5_OJ6yQDKSVRQ-sPm_GkpMA9Cf46WcDFLxWTiLwb31fRTHfRPDAi9qJ1IT9m_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=N1_aRMtKFuqy_EGmr9_Pl86KLvzswNk2kvQbuskC3SeW3W8Mqv-Zp4oliT9DJW9a-Sl1_Zq5n57BgSvT7qDaR_RN1Mq2fGhHe4htqL0I8K6JvHhL-3jNexd4tCap_pLoyDJ1K5sPivkdEEi7wuDsffZBJVCQUobdpx5TulQqA-J6PyJtbxDAe7FsBNhKV73Y09VjkLXKFQiaQsy80edxM8vTEgqiQoJGIMGuuOCh2MmsH7QTsh1_U9dE8GFHPKULo147hlhPv9WQ6e9pRNxx6Vz_5_OJ6yQDKSVRQ-sPm_GkpMA9Cf46WcDFLxWTiLwb31fRTHfRPDAi9qJ1IT9m_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
سپاه: تنگه هرمز بسته شد / به سمت یک کشتی موشک شلیک کردیم.
در بیانه دقایق پیش سپاه آمده است که : «در اطلاعیه قبلی گفته بودیم تعیین مسیر غیرقانونی حرکت کشتی ها در تنگه هرمز، برخورد قاطع ما را به دنبال خواهد داشت.
ساعاتی قبل، این تذکرات نادیده گرفته شد و
چند کشتی تلاش کردند از مسیر غیرمصوب حرکت کنند
و به اخطارها و تذکرات ما در اصلاح مسیر و حرکت در مسیر مصوب بی اعتنایی کردند.
به ناچار یک فروند از کشتی‌ها مورد اصابت شلیک‌ِاخطار واقع و متوقف شد
.»
🔺
جمهوری اسلامی به زور میخواهد که کشتی‌ها از مسیر آبی ایران از تنگه هرمز عبور کنند و نه از مسیر آبی
عمان.
🔺
آمریکا از جمهوری اسلامی خواسته بود که شنبه - که دقایقی پیش تمام شد - ‌به روشنی و علنی اعلام کند که تنگه هرمز برای عبور و مرور باز است، ج‌ا اما دقایقی پیش آنر‌ا بست
.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6031" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJ1csWAEhN-mP8aCwcYaBMBCrlr5PUfhmefaG7yQVQo6krCqoPrW8lBzKXDMIacmOme-F-nA8T_mlO6Rc3v_zc4Kt38PX_gLM0rc9QADdJ38EyhRxDOWMuwbBrdnnCq0SYsBZaJoz5z5yX3S6DcbGpHwjqeYLsxybLkhAzECeRZcVher1gbgeFHNAMHiMqt3XVnrhw_vSJNgYPHe_p-sGENfvsThZDNpZNe2qLZS3heEA0cX84heqT_UgWzaKEbwCe_NyipHCcVNEfYT3oagg0xHPDbtiZfarRO78iF4FNuIK_tDYCsR7G4sGvAZpYVsmxyWU5NwCnemBvHk6fJkBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=TpQgUaqOtlWPmTJAih7f9KMXiXJsLVQqI0VjcBhebI9ZjqF-k1st7tpHFhN_IhwTleM3eLCzmHwcjrLqDAsLEl9VGTMg4P2X_bY3eEQiccKMKIHhTdS6a7FUEqzLET-C9aAGV-fjBgd_sI2FJZ56AH2heBWHjyik9zoI5w8SdladFGDJmgZmgq6GeehfYi-Wcq71KGhp8baI1NovezabmraDtaby2v-XKvNAGjmI3_BQ06CjyCq657aQUboUKEqh2-aIp3gjr0dpNt5_7ci10i3eJmnVu8fGEddQes_O0GR6N7SNeHtEaHatCDttMvsioFzWGVFetLJoH1fuDQDnJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=TpQgUaqOtlWPmTJAih7f9KMXiXJsLVQqI0VjcBhebI9ZjqF-k1st7tpHFhN_IhwTleM3eLCzmHwcjrLqDAsLEl9VGTMg4P2X_bY3eEQiccKMKIHhTdS6a7FUEqzLET-C9aAGV-fjBgd_sI2FJZ56AH2heBWHjyik9zoI5w8SdladFGDJmgZmgq6GeehfYi-Wcq71KGhp8baI1NovezabmraDtaby2v-XKvNAGjmI3_BQ06CjyCq657aQUboUKEqh2-aIp3gjr0dpNt5_7ci10i3eJmnVu8fGEddQes_O0GR6N7SNeHtEaHatCDttMvsioFzWGVFetLJoH1fuDQDnJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X68zyO-wf4Q9HIAuKpJppNYzbc7EuXz4MBTK_DVjjXRJDr_c-QZ6BtQpAV6-3eFpfpS0KxvaLE5j5uxQ-fQGMVv6Bed1pWhcWfNN-w81h_iE3Z1OZEirD5EkotDbv5QMWX5Jq7ytoW-NYiTtyngiggskYFhk68w5nrb4Q5hFSv4Jvkti_tLJUV5jMTcdb2zh-kqSyTiJyqBzXTHM05FuTxdVFBHjx2Fg4N0sQIrim7Fs_DzFlTcApL0uPuqz6SPMXdtocni75FEio2s9J6hcHT08DF7b92K8ll9KZGg2fLbBNgesDcAcrdKhRkL6VJjZP0ObC-Q9GSm2GTBmNK64SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkhpycQA1b4AVGUJ7D0dPa5w-p-S9M_K1eqNry2-QbJ8RxmySsoos4o75HlSefIxy6KDirPNafaI1z9ZI7225gEWDLi_-RMdcLzTspdFdqS4RgKmc1maDFFB7W05X49mjGcR2oDxyUSxireA4EMsAoAahJ6qXAyRK3sHJIBDD5ZQqMBjDGDtDqdoGObWijgJ8P8P-7N3Jaxoky4ZhRkE78LPhVDD6CFBaR3EBHXgvif8rHXpNyyuu-UQZXWhn065_pwCA1Qwg0ZnOTAiXwRoeyOwPi9wXsXv1V6HOBIplelYQ4BVrBrXDqWlfF_re9AwGsiKZpk_MaCZSRcRZsJoDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر یک مجله ژاپنی
در آستانه جنگ عراق
که پیش‌یینی می‌کرد جنگ جهانی سوم راه بیفته و…..! رسانه‌های غربی هم پیش از جنگ، ارتش عراق رو باد کرده بودن و بهش میگفتن : چهارمین ارتش قدرتمند جهان!
رسانه‌ها عامدا اینگونه می‌نوشتند
تا خطر رژیم صدام‌ رو پررنگ‌تر هم کنند،
اما این باد کردن‌ها، در عراق هم باعث میشد
که فکر کنن بسیار بسیار قدرتمند هستند
و جهان به قدرت اونها اذعان کرده.
رسانه‌های غربی با «قاسم سلیمانی» هم همین کار رو کردن!
و بعد ترور شد.
تروری که ترامپ هر روز یادآور میشه
که اون دستور کار رو داده!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=SPKo3jXcsTEpuYd4_fGCU1RWHY0jUgSCB1llKS-z34MflhAn-3s3NVxFhTo7wBzsm3MZ9rbnX4kvgRRk2-XR-5oJYrVBA68m_mrTty3FbG4jXPTBZCmjJfMeMUicOceCPeQL5xMdg7iRP4IIAlstvkinLOYXOSpY3QwQddblGiqV7MQ48x8JwbYHweo3KSvoOhW73h3MYdXP5dJ8TxDih-Bnf67WcjNRPV6697aWPK5Brj27sq96n9uMtEWRZ7WKPAftL57SDvvO_qC2YPo5U5PL8wBCMBn-i4xTXXpQc_lz7JKJzfAedgY6OCCVf2iwoytnGEJuiDLNm4Bt6Zelim5s_rH-Akgo2qUKEOcbnbgkuuBQupgv3VKT06-DhDV55TKPubx3vvIGMmlZyYDsz3MqJKEx3cZ_FBE2fSvXshNLJ1rQW85t9LWIPvbDyQDtwzrhhe2-3mLhhS29W25rkIYb_PLExEzxitma0t91WBvN8yxop6zkY3I_gZKjPdbhZkfDmbWCa17STX2jiaDDqYPlan54IQeeUcjL6XXi-Uptn-hPg5yCTwg6m_5Xb6j9LcDFsuep01iCqPD72cdTF_i7k9lmU7IFt2-_soTBYvBBRRy5Feh6JaJJ_dWsJPznzMBBJV9qaMLuQNvLi7pJhzMrG27jT-jcn1Bh331RdDs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=SPKo3jXcsTEpuYd4_fGCU1RWHY0jUgSCB1llKS-z34MflhAn-3s3NVxFhTo7wBzsm3MZ9rbnX4kvgRRk2-XR-5oJYrVBA68m_mrTty3FbG4jXPTBZCmjJfMeMUicOceCPeQL5xMdg7iRP4IIAlstvkinLOYXOSpY3QwQddblGiqV7MQ48x8JwbYHweo3KSvoOhW73h3MYdXP5dJ8TxDih-Bnf67WcjNRPV6697aWPK5Brj27sq96n9uMtEWRZ7WKPAftL57SDvvO_qC2YPo5U5PL8wBCMBn-i4xTXXpQc_lz7JKJzfAedgY6OCCVf2iwoytnGEJuiDLNm4Bt6Zelim5s_rH-Akgo2qUKEOcbnbgkuuBQupgv3VKT06-DhDV55TKPubx3vvIGMmlZyYDsz3MqJKEx3cZ_FBE2fSvXshNLJ1rQW85t9LWIPvbDyQDtwzrhhe2-3mLhhS29W25rkIYb_PLExEzxitma0t91WBvN8yxop6zkY3I_gZKjPdbhZkfDmbWCa17STX2jiaDDqYPlan54IQeeUcjL6XXi-Uptn-hPg5yCTwg6m_5Xb6j9LcDFsuep01iCqPD72cdTF_i7k9lmU7IFt2-_soTBYvBBRRy5Feh6JaJJ_dWsJPznzMBBJV9qaMLuQNvLi7pJhzMrG27jT-jcn1Bh331RdDs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند غیر ایرانی در ایران صاحب خانه است.
ایران، منافع و ثروت‌هاش، برای همه است، برای تروریست‌های غزه و لبنان و یمن.
برای آخوندهای خارجی ساکن ایران.
سهم مردم ایران اما فقره و سرکوب و گلوله</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ys7ZYzNWbORoUQy7Z3t3-cZ4s7RDrr2g7W0zggNhBIz_CfHZZ3Jlib_QCRI2oz7zQed0XZXk5y06EIp6unCJgejKYNn2-FtNxfLM2YHg-cWh0XmoBqfR7QRVGl2jGa-hzc83P0WsDUsHOU2Lzu9l4jxl72dB77oat94MW1_Dk3XBwMtu-eOs2IsezrHFzFIqVkM22IA1vg5ERU-PPVX47loVyrOBFypRA6NKvwFPc1xHDJXXJmVFxp56Np-PcKG2ihDOER2bchtYjWFfZOmVqc8UREwt8bJlHKnkotLPvKlkMrB-y-30dqt0i2vjMLTdSqdpzWDaadcffp29jpVUHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
