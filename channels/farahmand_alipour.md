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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 12:35:10</div>
<hr>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=bZSRQN0_-i1IBfNceXCS3m1cslXegyECZ2VqCPfX5HY4t8EeTiKbDG5i_DHiThRcEUiPYYh5mUj9CtT4XiXAzEdkC4LOap6MvoCzpFU7lYMeURcoV43bVXdvvHTOWoswQlgx5n_lnYUpwgLMKet_qFdp8bc_pUuuuqfXLqCtAW6sU5lsIPlmtm0Veg0s21w0qQESmU3pYCIbiFCpCnIJREFT1k3J8SeIwEIhkk_M-qgsmuOt4Ol1NAjA5JM44gE2xcMNcy4LWNIz2LkCYzj9Gg3hGuW5GujQjQRTD8dWuoXJLDznwj8t0_Kan0IQc7b61u2Z70x0zV37-5pWrnsxOQetezIhK-WZaojfmaSGX1PXJRQrhn9f10lSzthamRfYE6c0BxLmcS36b-CJc6f7u7dApHvaWBMxs-NsYRW_PezkWyYFuoTgIaC_AvomAZJWs3FGsMzlDoNAVMKp1TQuiYkYodaVPRUxV6ONhENiIZoKdMtSZgKMKOGvvYL1ndV_0BM6A47fVS5YiPLwtxXwT6hiiNdY6uTB9X012Zt8-CoYXxBUzJFrDRf3geH4mrkTAOTuwjC1ZVER4UnJmjSzIoFu2TDhiohWLcUhqO-2Sl33nSOG0m-oeOJuWWU72nO7fWs87nGvP6DW2Sn7Rbag-FhNhN3kYj06W_p6Irv8igg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=bZSRQN0_-i1IBfNceXCS3m1cslXegyECZ2VqCPfX5HY4t8EeTiKbDG5i_DHiThRcEUiPYYh5mUj9CtT4XiXAzEdkC4LOap6MvoCzpFU7lYMeURcoV43bVXdvvHTOWoswQlgx5n_lnYUpwgLMKet_qFdp8bc_pUuuuqfXLqCtAW6sU5lsIPlmtm0Veg0s21w0qQESmU3pYCIbiFCpCnIJREFT1k3J8SeIwEIhkk_M-qgsmuOt4Ol1NAjA5JM44gE2xcMNcy4LWNIz2LkCYzj9Gg3hGuW5GujQjQRTD8dWuoXJLDznwj8t0_Kan0IQc7b61u2Z70x0zV37-5pWrnsxOQetezIhK-WZaojfmaSGX1PXJRQrhn9f10lSzthamRfYE6c0BxLmcS36b-CJc6f7u7dApHvaWBMxs-NsYRW_PezkWyYFuoTgIaC_AvomAZJWs3FGsMzlDoNAVMKp1TQuiYkYodaVPRUxV6ONhENiIZoKdMtSZgKMKOGvvYL1ndV_0BM6A47fVS5YiPLwtxXwT6hiiNdY6uTB9X012Zt8-CoYXxBUzJFrDRf3geH4mrkTAOTuwjC1ZVER4UnJmjSzIoFu2TDhiohWLcUhqO-2Sl33nSOG0m-oeOJuWWU72nO7fWs87nGvP6DW2Sn7Rbag-FhNhN3kYj06W_p6Irv8igg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qd3yTUNjUOWKdAe59-Yx4yY48MA6mLKAnx56xVdFzJfZj-SJgRA9gDIa3I__7HypgYOO9Zd9-ucfYhaI-U3YPDuDOESL_lcpFvkFvF35hYXBJNzNdeWMg5lWCsyvggI7OHojJNWxJkM8hBYY9XgnrzACqG9I4Pw_qfNlnmwI8VLIDqHBzkeogvkCYVFn7CY40Ohy9fHcrmON6NWXkOrFVQttiNCTnsyZ7DDnO3YaHjmLUPsekRD7GhuwOKX5rOExEEctZ-n8JTmNItZqWJ_T7PK-OvHcXEy7Um6ypO-t110Wppmz4Lb3FRKomj6dDsCgY8s4b_NLMYvriugQvqh3VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6123">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=KIZqWIToUzGnJhKmw4nD0sMVeY1f0oEQh5JIY1nLqY3231xQTzZeoxpkmTEaY123tsKh_cog2q3fUO4LPPbwkibGd9q_tR2tq0SjC_86WqRtMgEMmT8WeuWX3c1FqOQvZuc4IqwY-eIMFI0Yoy5b3LZVrPCkP5Xm9bYr5cWzrc9Lg6UoHYYlcs-UUA3xWVDQZmeDaWeiZlDKXpTpbfQy0Nv2feRsFx0un2Vrn_35qXjDRiaHElNVTJHGmWULPaj8xp0Dd9B051W4F_UysTDcd5xETlmE-ZHnLzzhnXry5DYKJHO-Up4dwFGGkhQnJjpdOGu8_n3VPyrxs3Fu1ZFCXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=KIZqWIToUzGnJhKmw4nD0sMVeY1f0oEQh5JIY1nLqY3231xQTzZeoxpkmTEaY123tsKh_cog2q3fUO4LPPbwkibGd9q_tR2tq0SjC_86WqRtMgEMmT8WeuWX3c1FqOQvZuc4IqwY-eIMFI0Yoy5b3LZVrPCkP5Xm9bYr5cWzrc9Lg6UoHYYlcs-UUA3xWVDQZmeDaWeiZlDKXpTpbfQy0Nv2feRsFx0un2Vrn_35qXjDRiaHElNVTJHGmWULPaj8xp0Dd9B051W4F_UysTDcd5xETlmE-ZHnLzzhnXry5DYKJHO-Up4dwFGGkhQnJjpdOGu8_n3VPyrxs3Fu1ZFCXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=uukUbxq61Kc79KDOGiiAtbEmFRYZw5TL4_2BBsuM1eIVLrPUetfbacuT6ldWCpehbdl5_2EDMCO-NZYpDIN7M19sMs6Q315cushn4qcTCtAbnlw0SaRCgcmFP-Q0pRx2IzxQpYyiN0FtxNtcPslSvFVCQE2xuBjxczkY3R0cA1PC1DvOkWH1Uqv4ZvAdkvvF7YmZbAtPNVffIuYX5kOtmB1acRZLXfkQEL4RVNsIQ4Nfq9tF7kwKa30JTOS9TjHoD_Yh_S8_1yV1H-cWWPgEJRKETn1TysLIyE5ZAs9Hydnrlf-XtiIp2ectbTCS6zh6n4tF2ulfvlnB8N8dUVJVrij3gLkCIuHwzaSLrZRRgKiWtOm2WifkC7uaLX-AxWJ_V4oi-tND-NlKRxoNoBpaYj5iRb14uJ0W_Xa6bFvSwiFihlandHb7LLsJKEbnEUvVqUg3okPPVqOwdCHuO-99cbvtVyJXl9K8H5gQAxm1HZBIII_jh6lftfxk7bab6FpS7a4x-zT89_Dn0sYa2_k1Sknkw0BvhsIiwVZWEsPRwN7LtvKMYIKu3Trx0OklwXIqkXd6UYwXjBMJR-d2zIz9iKl_VFDJxQ7B8_RGDB40b4ZLjb0-XfTdrduFlkvb79TUQC0mQFIQ2vOt3fb9QHIFuBWaigFWo5bHSJSENFIvar0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=uukUbxq61Kc79KDOGiiAtbEmFRYZw5TL4_2BBsuM1eIVLrPUetfbacuT6ldWCpehbdl5_2EDMCO-NZYpDIN7M19sMs6Q315cushn4qcTCtAbnlw0SaRCgcmFP-Q0pRx2IzxQpYyiN0FtxNtcPslSvFVCQE2xuBjxczkY3R0cA1PC1DvOkWH1Uqv4ZvAdkvvF7YmZbAtPNVffIuYX5kOtmB1acRZLXfkQEL4RVNsIQ4Nfq9tF7kwKa30JTOS9TjHoD_Yh_S8_1yV1H-cWWPgEJRKETn1TysLIyE5ZAs9Hydnrlf-XtiIp2ectbTCS6zh6n4tF2ulfvlnB8N8dUVJVrij3gLkCIuHwzaSLrZRRgKiWtOm2WifkC7uaLX-AxWJ_V4oi-tND-NlKRxoNoBpaYj5iRb14uJ0W_Xa6bFvSwiFihlandHb7LLsJKEbnEUvVqUg3okPPVqOwdCHuO-99cbvtVyJXl9K8H5gQAxm1HZBIII_jh6lftfxk7bab6FpS7a4x-zT89_Dn0sYa2_k1Sknkw0BvhsIiwVZWEsPRwN7LtvKMYIKu3Trx0OklwXIqkXd6UYwXjBMJR-d2zIz9iKl_VFDJxQ7B8_RGDB40b4ZLjb0-XfTdrduFlkvb79TUQC0mQFIQ2vOt3fb9QHIFuBWaigFWo5bHSJSENFIvar0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgL8F0WQAHw2bRtcWGoPLrN68cjCVvQASKkc20M9PZOiwtiQFPfF3P1JF_WwFafDIhpYNP56xpgtisC9EtLMuZlqQxcabtKOhNz-zfS_VBiN2jn6fbdZnakWv7a8pG34612RUh6gqnFWJC9RWE_Ht3Wj6KGVu4u6SKa4mlgnaKV4Er9vHxRTXvlj9xcIXe4yv_ME5EHc4wSZTH8WcPCtRBcBulgzd0VpOUnx6W73GAUguUBcJK5rW7ge-2jB6pfqgAG8Mssbv9QK8iMKyrl5iqQ9et4ducq5xxWdGgvexY2nm0Kj39GTFgFC26TuUGeu69ZBfgkTNT6xfMVPPKAulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMtQpgqKReoQfynZcgc0MAOK6T1LWbnAqVCmU3H0is_Fo0WO574sn7NYgOTzxeCbkhzbjpfeilAPf_VblR0zgrDhIsz9wk2uvIFAFYmQjeYEoADljOeScRvXzF06OiGymr8rxuXoriGKZeS1KRxPxDBehGhJ6LY_SzJwDGp36FnAwowtpBgDqrs64jvELkz54UUi9-zqA3SgYt-qWHe75C4UjyMMdW9BPPpRtZ8K2mSa60ssIJbF6_RnIC7-7FYg4E1NkQlKO7m2SZXqRFlQ5SigwPSXvzYhS9yKimyQih6JQemhnU_qtzy8FVkWXfU2O7qm1dr5tOExPe8udvIe3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=S5xXhbEjKCJsB__D8UchXoPehz5H5V2HJTd3KPP0FJ6z7tWpZIfstaV_6aHt5FKG0bh_dMgI_ECpMCPq1Jlv72-7eR-QQBUKT_nt3VgPyZziNWT3hXZ3oNOCnV4nXP7lU8WjewwyeJetV8h7cr9xPA-AlJg4x2qvkfElmgtGzmRjpofXhWWCy1vaxoBdx1ytdniDQbfhlRloJLx1mZ5ehLnua3hdBmM0zYEFZeBs_DTrmx2gus3uS2vA02_nRgdhyzN_fIDx6UUquU8oa9niCczQmUdbm9GhJvktA3adgnm_dJz9K8I12zRR6oWHeJFxkgLm_3deSihAbLN0Tw37GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=S5xXhbEjKCJsB__D8UchXoPehz5H5V2HJTd3KPP0FJ6z7tWpZIfstaV_6aHt5FKG0bh_dMgI_ECpMCPq1Jlv72-7eR-QQBUKT_nt3VgPyZziNWT3hXZ3oNOCnV4nXP7lU8WjewwyeJetV8h7cr9xPA-AlJg4x2qvkfElmgtGzmRjpofXhWWCy1vaxoBdx1ytdniDQbfhlRloJLx1mZ5ehLnua3hdBmM0zYEFZeBs_DTrmx2gus3uS2vA02_nRgdhyzN_fIDx6UUquU8oa9niCczQmUdbm9GhJvktA3adgnm_dJz9K8I12zRR6oWHeJFxkgLm_3deSihAbLN0Tw37GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=NF_6oUCPn0BV3S8mKbcg86QuBkyRAKuBStVuJU3kEX37p9pCusoOj9Jh6uczG-2g8D5FgXkfC2bJ92urGKwAobl87XqsYlAkKYrI7EdRNwURU0MqcwR71j7SDSaKchZPZTnUtnN5W-n0ry46d5NrCqmuM5YdFSktcFO5KmZsh6Iv5ROsULTwpIY86dzRxXSJltFQxBW-3_xyaTmud6rmKeUEunozKjg2aA54qTu2eVDTmaiVcKgjpkzsxtV8q3duPIJhUP3zwubU54V7NTCrmc1s-PVPlM3CrOjWTRYsCmJzyEPTZMnnGRAbZm3CRUojF-O4YGFW04WgyE9pgVMCSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=NF_6oUCPn0BV3S8mKbcg86QuBkyRAKuBStVuJU3kEX37p9pCusoOj9Jh6uczG-2g8D5FgXkfC2bJ92urGKwAobl87XqsYlAkKYrI7EdRNwURU0MqcwR71j7SDSaKchZPZTnUtnN5W-n0ry46d5NrCqmuM5YdFSktcFO5KmZsh6Iv5ROsULTwpIY86dzRxXSJltFQxBW-3_xyaTmud6rmKeUEunozKjg2aA54qTu2eVDTmaiVcKgjpkzsxtV8q3duPIJhUP3zwubU54V7NTCrmc1s-PVPlM3CrOjWTRYsCmJzyEPTZMnnGRAbZm3CRUojF-O4YGFW04WgyE9pgVMCSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=J1UyMRNGoB9A2K5jLwz92TxKZVSf7esypNzLpeYTdw1fQ6dr78mJYQArbpZxRsGDqKYIxiXSzqW9YVHtkuDy0KN5IUPHBvdre6VIGNfZ7Kyd7nTHDXMi9tdfreTdzEeBf-EEe_BEErl7QtuFF_iteqfGkqDSoGOFslXWqcvCYGdd8qP3_5xgDNnauwFXheI2o6s7O8pPy1CXxzTnu4ND1uZQDWeddyvK6V6lpgBFkupVgbJfWKkpHSdLXpbcl5-XTtVdz4pMNF5o4KTtqftGDppEY1DN-L9UvjKl6cSccfob1DTqhsI1d9bvs_TKmkhKwTzBEin3Jxbej0DizA7rKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=J1UyMRNGoB9A2K5jLwz92TxKZVSf7esypNzLpeYTdw1fQ6dr78mJYQArbpZxRsGDqKYIxiXSzqW9YVHtkuDy0KN5IUPHBvdre6VIGNfZ7Kyd7nTHDXMi9tdfreTdzEeBf-EEe_BEErl7QtuFF_iteqfGkqDSoGOFslXWqcvCYGdd8qP3_5xgDNnauwFXheI2o6s7O8pPy1CXxzTnu4ND1uZQDWeddyvK6V6lpgBFkupVgbJfWKkpHSdLXpbcl5-XTtVdz4pMNF5o4KTtqftGDppEY1DN-L9UvjKl6cSccfob1DTqhsI1d9bvs_TKmkhKwTzBEin3Jxbej0DizA7rKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=I4sRwziSIcacoPJvv3AC4ABuCtdgT9VBpvQTIeRj1ygrtLHE5DJiBSzP2T7LYxxSfsgWfy33eFP2Vh8wCUUe6yhAbpXJ7dsUzMSD5fgIc5A67XaD1XsHcknyckZVWam7PL6hGJ5vrwcGq6jfahZJ3c8X0SIoN-9jAZEdxVmq6jjYa7VyOlqeMjYQTncqvICzpOH3HGqYNdzWH22ukMrgUsJh0xHG1SV158TDcLDOiPdS8Mi2Eykjq_PgrOXPnnMMPTeNpIOOAhAmfS3fmaa3vcmISln2VQQIk6pTcETduWbwDa3HPSIgMzupF446K9Y_F4C73OtJ9YREL-mNpzTlWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=I4sRwziSIcacoPJvv3AC4ABuCtdgT9VBpvQTIeRj1ygrtLHE5DJiBSzP2T7LYxxSfsgWfy33eFP2Vh8wCUUe6yhAbpXJ7dsUzMSD5fgIc5A67XaD1XsHcknyckZVWam7PL6hGJ5vrwcGq6jfahZJ3c8X0SIoN-9jAZEdxVmq6jjYa7VyOlqeMjYQTncqvICzpOH3HGqYNdzWH22ukMrgUsJh0xHG1SV158TDcLDOiPdS8Mi2Eykjq_PgrOXPnnMMPTeNpIOOAhAmfS3fmaa3vcmISln2VQQIk6pTcETduWbwDa3HPSIgMzupF446K9Y_F4C73OtJ9YREL-mNpzTlWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seDtoBUvfbJ39Au6Rk7tUBj9xJ1WgC6OgSfdQSiRnwNGDwSBoONWMcOe1ZlQAla89lDB6FNpY-f_wBhzo6Q6nLf4yJEWylk261ngT6lX5NylvC6mX68GF89KvhwgY1AgEotYB6uEa2pcW4AOr2qNNzn0nHgWZJLJ75L5gf7DdEyTzUtbm1hbs790jqOZIcNCTFxDmjd57fVqY7SYfspdOd0bo2wrnXlM_g9vxRRpkRgNIHoAa58OrtRmIua6lyHrqMvvL-s7eER0o6qemgITrgMwEJrIcr8HewfAhL4qlUOsN-eZ04KvgcjOSTZO5XVZ8QVw1Lj4fqOM31dNrlpuYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVwk0MF1CymWQNvBspQ8qRvgCbc9OMnrwCCLvSSTmnNZG7h63TSeiBWtiMjICz44yaJh8FcDCbzEZAQrmBV-uZwz5BLiYRSq8gMvbZtzFABq742ir3Fnz48EBeSeG-EPf6pVH32S5ObLKiOmWTCPNl1wuKN6B2T09g9Q7bfvv-G-lBTFyukyL9TxmjkYB6TwNTMVSXGFJcYhgHAysEy799dAyianAAZdGsNOyLQVXCKCuthOA4kdvPxzKbtTCbGn_MFVUHfjstJ8fsr3VUoNl5ywPXjJRTMk_QEj_zesVne1WPthz_tBI_0fIXMMiubnDq-1X9wrTkke9IXGEUrNBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=kxUHmvDaGCUiGVFA4Z-TPajerepMWZWgH7yBcFrvHCqav6IE4mp5bFahXsmiWZz0V0oEE_AK71IyEAmcGfBiRlgcMMrh0WHbyEpPn0HmDiVMig8npG6VnnmeDONmdYjKYijNh_peHTdSIw8vtmoJ69x8kERbw13kexIc0fnBJ7T5_ut03b6q6QVo3czO7iM-pqG6It_4JcrNh4NgzTtLv2v4OBeJsufrnLH2_XxevPLjWGxn4JXjBw_lJpei7cab5jL-wWBiDlhFf0201HK4BlWEKEGANVx0_0g0p5B11wkELUkMPLpJULLBbVF0or7hCBu-PfvYRA_JHWtJK_0iYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=kxUHmvDaGCUiGVFA4Z-TPajerepMWZWgH7yBcFrvHCqav6IE4mp5bFahXsmiWZz0V0oEE_AK71IyEAmcGfBiRlgcMMrh0WHbyEpPn0HmDiVMig8npG6VnnmeDONmdYjKYijNh_peHTdSIw8vtmoJ69x8kERbw13kexIc0fnBJ7T5_ut03b6q6QVo3czO7iM-pqG6It_4JcrNh4NgzTtLv2v4OBeJsufrnLH2_XxevPLjWGxn4JXjBw_lJpei7cab5jL-wWBiDlhFf0201HK4BlWEKEGANVx0_0g0p5B11wkELUkMPLpJULLBbVF0or7hCBu-PfvYRA_JHWtJK_0iYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=NUJpRwMmcErmKOMXPwTPmwidxKbxO_xIEovTZ3e2sNTv93lgJV14d3vNWOA8O2xwigmVk-nZImdUjJV7nEHDwqT-UxnvKB39nCCK0emspc_bkS3q8DG9GbkgJIbhVAJXYdMwCQZTasVsBnF5bwU9JsMNiTCcIlbPCGkua9RQkYee-dqLVjBZECX_b6eK_M8bgqxDy0Td7ox-MArsrbHMqalR7suaN9c-D-Zts0gW2OXXmR5JA9FeCiHu0xSR6xNBMUC0QIoX6qASdNAzpCIGB7-sNrg9tJl6r9ujMXUBfiY9yMNq2oNuzV-ths36bkNJkqF4X5mvhXPdxxMFeNWdGSwrIAj43dQMee7JQKLfKfUOj4mgBQ2Mq8rl74j2hfpH6CZFDsy4h_ytVTMtZArBoXdKv41fYkWUcrK89YNET3moc_Vtt5dXZ4QKaSvvApM2Z2_d-sErEqH75SZTex-eareWfVPgHNpzdpESGYNIOrtmco5XXRSk38gLVxm-yHZ3S1b4GT97JSU6cqvLcCOQAsF3p29kvINjLKZtsxdd1RFcIj78fAFhKrDKG5r72hjlOvTvJlNfJXwOybhY5AoWt686zqWACejPaNvA08809MuO8MBbX8ksnxs6hfnW54Ws7ly2tWjSGr2hz8qJwe75P0HBb--hdWiRpcSz7NB-wf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=NUJpRwMmcErmKOMXPwTPmwidxKbxO_xIEovTZ3e2sNTv93lgJV14d3vNWOA8O2xwigmVk-nZImdUjJV7nEHDwqT-UxnvKB39nCCK0emspc_bkS3q8DG9GbkgJIbhVAJXYdMwCQZTasVsBnF5bwU9JsMNiTCcIlbPCGkua9RQkYee-dqLVjBZECX_b6eK_M8bgqxDy0Td7ox-MArsrbHMqalR7suaN9c-D-Zts0gW2OXXmR5JA9FeCiHu0xSR6xNBMUC0QIoX6qASdNAzpCIGB7-sNrg9tJl6r9ujMXUBfiY9yMNq2oNuzV-ths36bkNJkqF4X5mvhXPdxxMFeNWdGSwrIAj43dQMee7JQKLfKfUOj4mgBQ2Mq8rl74j2hfpH6CZFDsy4h_ytVTMtZArBoXdKv41fYkWUcrK89YNET3moc_Vtt5dXZ4QKaSvvApM2Z2_d-sErEqH75SZTex-eareWfVPgHNpzdpESGYNIOrtmco5XXRSk38gLVxm-yHZ3S1b4GT97JSU6cqvLcCOQAsF3p29kvINjLKZtsxdd1RFcIj78fAFhKrDKG5r72hjlOvTvJlNfJXwOybhY5AoWt686zqWACejPaNvA08809MuO8MBbX8ksnxs6hfnW54Ws7ly2tWjSGr2hz8qJwe75P0HBb--hdWiRpcSz7NB-wf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=J7lmiUmWdyW-RL5x2-i15L8phbIJ_P6cDdUFCvAcUnBEZMJfDyeUbRtnIZObQ_5VJrJKXL_DdKLhOj5xhDwQcQJsgyxkN8Taz8VyglmaByrHCvTiPbVCGNKrBjdMAhMDvWLPqrLtDSmHCAj09bMKNfQ_210MIafNy2N7ricDjKIs0Yd-sVGP3ryK58sOR900ve6Nq0VxE1pPlB-LnSG984qpVz47RjBBBJrlKCluKHtC_2cd-z_3cQl9e2Mya4tuVcfOi_8cTckus1mxgEh8LCouFyQB_yEBpWQ4SQUFInX9-MbnmVS9mahv3bQgQ3nG1dJtLpB3W7Nav7YF-JLP9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=J7lmiUmWdyW-RL5x2-i15L8phbIJ_P6cDdUFCvAcUnBEZMJfDyeUbRtnIZObQ_5VJrJKXL_DdKLhOj5xhDwQcQJsgyxkN8Taz8VyglmaByrHCvTiPbVCGNKrBjdMAhMDvWLPqrLtDSmHCAj09bMKNfQ_210MIafNy2N7ricDjKIs0Yd-sVGP3ryK58sOR900ve6Nq0VxE1pPlB-LnSG984qpVz47RjBBBJrlKCluKHtC_2cd-z_3cQl9e2Mya4tuVcfOi_8cTckus1mxgEh8LCouFyQB_yEBpWQ4SQUFInX9-MbnmVS9mahv3bQgQ3nG1dJtLpB3W7Nav7YF-JLP9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2_NxrDf3lqgi08vo8y-vLhn240A_uzfeiQYrm-_DqPBGXpK1Gf-smStOIYIsNGZhKuHwC0d7SPvqqIPuVtXbMlfDdNEVYrEKgpmvdJKw1jAs997HPCWzBwlYLblGOzYkSIiHevncRnVvP0sLaiHpuouyAAhC7quzcwB3MrcJuQNbJZCMpUkd0Nyv1I9wBuOnUzPBnfJVCpFIB_tz9LgUu1fos7ImgwiqCLH30MOkbe7zg6iCNlcT4IRqgZdyxzj9K-3itP1fg550uH-Ucq9r1nWZg61nt77YVNw66phZ_fWlWYpkmrCPp-kieaFtXxoSI8kKgGGqXuU2k4tKXGZJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6103" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVU-nDZkvVMadV7tl3LNLTuxH72pYU5CaNIsDpSVAfsYyWebLiP8fhqd727ZvWTwz2u-zDA4xF0zWoyg2IFWTcY0B4qovADQl-SCOxzhUPXuYiEZuEjk3eJYAsD9PDTpG3M5qKyjXFI9bXNVt4ANlpq7x-xWP6MmFRa6H57xCSejt71lZd-ngv7jIdaGFFXHrElikrNWv_-WkQRgIAECXSmEDWz7IhnnMYdfLXb1KMNczAgpHEXsWY4zZqlta8I1QjB249pzOjAAINpWiH_NpqYQobDKJaIWptEaxlPOURJOARy3H8YMisIQSTSeta5rg2zo38F7EHphnLi0wWWvSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=BI7blTNc4DAgtiT-V1PeoCa66mb3TZZnCQ2LbbNat84x1Te_T7NX__vk6qdtiCmH8qPNY7oC_Q-lEhA3HyGuvJejhd1FFl2CuQC3JvDsXdsd_YKyXOW6jT5hnIXU5DPnSnuEnlli4wLlyE5QF9z2Ouum4IEqSVhu52JuXTrlf8lZb1sYYlg_aHXUZgbB4_aA-lh9ak10EZ2cfHum0IdWZlNTuz669wWlsihJ7wagQ0U0yzkn2rOVlfFKrGd_bUwRx6FDE99vY8IT54ZHvWK8Gh4_5S7o9650sEtbuXJ6y9A_QIPQea4c8ub_W5aXHGFyLR89X8FXMoDvSFwJWhU1Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=BI7blTNc4DAgtiT-V1PeoCa66mb3TZZnCQ2LbbNat84x1Te_T7NX__vk6qdtiCmH8qPNY7oC_Q-lEhA3HyGuvJejhd1FFl2CuQC3JvDsXdsd_YKyXOW6jT5hnIXU5DPnSnuEnlli4wLlyE5QF9z2Ouum4IEqSVhu52JuXTrlf8lZb1sYYlg_aHXUZgbB4_aA-lh9ak10EZ2cfHum0IdWZlNTuz669wWlsihJ7wagQ0U0yzkn2rOVlfFKrGd_bUwRx6FDE99vY8IT54ZHvWK8Gh4_5S7o9650sEtbuXJ6y9A_QIPQea4c8ub_W5aXHGFyLR89X8FXMoDvSFwJWhU1Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjIPXzCbYPwjFi9oe00DJVtesjM8S4PFKJLr3g4b251jI1q8a0Wwxy2JolqH3umtm-vobb_2Bn7_mBadHvUIFAk_hRvVRbBFRHUxg5e7Hv_XQrRL28sh31xCgjk6mbY0lR1NTfvNN8KmTFUUemnVXkjXf5ns3POtZsFpxfuVQF2uLSf10V023zCc90QXuFmmoqTi5pw4vIIIoRTG6iEm61XoPIY6tN-s4kMnodT4HA7w6s21416OCh30JnFd4RtDGHyPauEQD4qLTjRgIoKXdhTNz9DgC-o7Lr20m0a8-dHnChi_24IrBDleutOkXo3Eg_w3iQEfgrKi4Jc4ab7Y2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioAlXwoT1WjcSVkXHdC8oKgqvQxwI7L9M-XaqsyLeti0UKKxsC2U90KF-2U0dYwAt_gH6x9uf4gySU-d44vzxyonALETRk6reFC4u-Q5ozI9mk9-1uWkAhEj51sqxvGvAORSJvqJ7GF2HsCN8yjzr8Yq4NjxSAvnmlaKegNFvguvGic35-yIskyrxm518SyVtGV7dIgfZBbq8pRmAk9e7QPPtWuw0bj_VFvb2TvqppCobHn-VRWhCxzh6SIgFa7cKQNLV75AbmW_tRFdd4NuMvTXtDj0IYbz6QsDPFKx3TsFWpoR7RG3EBwsNou0EAiK1Y42bf2SUIhqFdl7_KTmqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6097" target="_blank">📅 14:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6096">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DI1f61vL42ySxQn5kYMCloRcoaUAkfAtXCjC_lNTA0zTKTDWkOQy_ZWZfgmhenzwH7EdwIPX3IUij3OHPCgMi2KDQIiJ33IS5-eZECTj7rLA8Xc4TO8Eke7v2MO2dXSL7Wz-S-Uhvl9BAsodrP8dylVH33cX8ktvdGZmshCvOCD1J7X04Dl98qBTAA3sHfUTTIPB7YT8PRVflBfyS3LHm5ihIH_S14XgvhZcEpTbJUbBUviyq8e_Lk3AaSCkCSSrvGiRylZ8fKHkdB14aHaJGh1TvjV_oyJsZEcmpe_kVlcAOwz6Dv59yJsV0qQUAH-YXt7R1w6XROe7UhLx9z2nuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6093" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=YJ_ahBNX0CB8E1_PujKGxpovK_AgRNwIwgZgBAteHBIEySDx8JWkFZ03GE6QRtia33BHZ1rfOJlXmGMidCv6TK8YN25NsKTiZ0fBTV40d9L260tcaeuWXuBS8OkCHjrZ1WiQ8ufPckN0YFCNB5jlOPHEHSBsJ-4QxyhtlX8lA7TPm_9ef04Po8AQuBzIKcsXRbO0B7j1lWacmPG1uEF3gLCEFMbTs_SaWMg_BIyPza_gqBvYcTXBDUQIVLy6RTZlvSNZpkipH8HWgwMhOcqbymfJFgZ1wJLwJ8bORmLeO3NttHVxf_5v6L5yURJSe1oXfg6LJg0gomjkOqYTixgfiw3TDl597dwARUi2NEgppPHYsl7gOFxEDrDw2_OFqkHTJSMAIp7o_s7YWK43s_jtz3lee_VUWLNipVv3kNpIK419xJ9ipLqH4ZvZ9O0z60gE-W2XYtrd37raN1Rabhd7LvojZwStTbCMHtxmmYVzSVCqE5FxcesJ8xsiLLABHqBrRk7qUl39LZ6A5fEO_RRC_9h66c-yj_tDZiEThqRy3jxUaTKdD94fHMuI78lLxuVUUxP2eztmVdqc_rhfi5PnnCzJIs6tFlnE6phtTl13lUIsxRAlMzhvnXjBOKHoi9gPtdfUB2YcT2IFuIkSAz5LxazdRkw8CfCSp3p7CP89E_4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=YJ_ahBNX0CB8E1_PujKGxpovK_AgRNwIwgZgBAteHBIEySDx8JWkFZ03GE6QRtia33BHZ1rfOJlXmGMidCv6TK8YN25NsKTiZ0fBTV40d9L260tcaeuWXuBS8OkCHjrZ1WiQ8ufPckN0YFCNB5jlOPHEHSBsJ-4QxyhtlX8lA7TPm_9ef04Po8AQuBzIKcsXRbO0B7j1lWacmPG1uEF3gLCEFMbTs_SaWMg_BIyPza_gqBvYcTXBDUQIVLy6RTZlvSNZpkipH8HWgwMhOcqbymfJFgZ1wJLwJ8bORmLeO3NttHVxf_5v6L5yURJSe1oXfg6LJg0gomjkOqYTixgfiw3TDl597dwARUi2NEgppPHYsl7gOFxEDrDw2_OFqkHTJSMAIp7o_s7YWK43s_jtz3lee_VUWLNipVv3kNpIK419xJ9ipLqH4ZvZ9O0z60gE-W2XYtrd37raN1Rabhd7LvojZwStTbCMHtxmmYVzSVCqE5FxcesJ8xsiLLABHqBrRk7qUl39LZ6A5fEO_RRC_9h66c-yj_tDZiEThqRy3jxUaTKdD94fHMuI78lLxuVUUxP2eztmVdqc_rhfi5PnnCzJIs6tFlnE6phtTl13lUIsxRAlMzhvnXjBOKHoi9gPtdfUB2YcT2IFuIkSAz5LxazdRkw8CfCSp3p7CP89E_4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی خامنه‌ای «علی الاصول»
با تفاهم‌ مخالف بود!
و نوه خمینی هم این چند روز گرد و خاک به پا کرد و گفت هویت ما در مبارزه با آمریکاست!
اون‌هایی هم که نگران زیرساخت‌ها بودن
الان سکوت کردن  و صداشون در نمیاد!
آغاز دوران «علی الاصولی» !</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6092" target="_blank">📅 09:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6091">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سنتکام ساعتی پیش
از پایان این مرحله از حملات خود خبر داد و نوشت :
🔺
جدیدترین موج حملات خود علیه ایران را به پایان رساندیم
🔺
در این عملیات پنج ساعته، به اهداف نظامی در بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردیم
🔺
سیستم‌های دفاع ساحلی و موشکی، سامانه‌های پهپادی و ظرفیت‌های دریایی ایران، هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6091" target="_blank">📅 09:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6090">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMxuUvIJjwzhbyARG6t_toqfdY7r1GRsUnna6PbO-edfS7NUYnY8xgF5-oEMPl23I9xcXzFbfB6YDMusytLhBBHeCI0qlxoMamrjf0uxWbNuGRL1vGMDeuAeuTteKntkg126bk3C818N4mVqHuuY3vm6bcRO_IVkYtD5tdyxMEp1FI6jMVUGX6-cjWsfNCc1d0Y1FJNLl11MlY4ichaSN8rqV1_bz7X74AXuDhdr34oextvgiXxIeHMy39kpQabL4WZCNjQq46QB4K5RB-hR3eVFpJlyZnsbUs5THG6ItCgw068nuGyfq6DAHoXLjFjj_ecpIMZA2e70nsC8rVuk2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV08K2YuHTY1HSnMe-4UMF1uX7Mr7h_FhMo_ujD42LRGtq_YVcXHvtNw-bw79dlrAHphuSGGshY725B8E9j5hKSc9ivrH9cZmyAhp826YyiGeVOLjaXRbrzQ8DJyimBdpUyDTpjk8mGspkIpgYqYBMo2BMzcoGIrvJ8ihydhE4XQRjgkeH6ro3BLlI6w1nvzOxarfIEjyzlN03rhORvRfaH7dIlocmFdveoU4fVL8YImf29cQ-D2QGML0WIG3d62GoBtZcODk71utpcJlpxWBs7NYhBMK8PGVXPo28Us_OWMa08pj9OATsMEQugS6SjFSU5aG4xsmvOb1X5s4AylOV8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV08K2YuHTY1HSnMe-4UMF1uX7Mr7h_FhMo_ujD42LRGtq_YVcXHvtNw-bw79dlrAHphuSGGshY725B8E9j5hKSc9ivrH9cZmyAhp826YyiGeVOLjaXRbrzQ8DJyimBdpUyDTpjk8mGspkIpgYqYBMo2BMzcoGIrvJ8ihydhE4XQRjgkeH6ro3BLlI6w1nvzOxarfIEjyzlN03rhORvRfaH7dIlocmFdveoU4fVL8YImf29cQ-D2QGML0WIG3d62GoBtZcODk71utpcJlpxWBs7NYhBMK8PGVXPo28Us_OWMa08pj9OATsMEQugS6SjFSU5aG4xsmvOb1X5s4AylOV8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: بیشتر موشک‌هاشون رو از کار انداختیم، بیشتر پهپادهاشون رو.
🔺
توان ساخت پهپادشون رو حدود ۹۲ درصد از بین بردیم. توان ساخت موشکشون رو ۸۹ درصد نابود کردیم.
🔺
یه کم توان براشون مونده، اما برای ما هیچ توانی ندارن. این دیگه تقریباً یه درگیری نظامی کوچیکه</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=TSSTYb178wN9q0OctYxuvWcgXHHsCVI3djdq2eWO5P5IeA3V3rzvEPHN5wTe9xOA3dIDQmLEYb8qNcRkHB0vncpPVV-oZYxpxgjtFSmcN8yoLy_4Q1IJDX6y_RuEWJHoeQ1hkvDwEo453Mgy86963cXltkXCAdlXhhFO2D_mDkm-LwhabX78tkCJU2UIpizhSFLTUcwYjHHTUBexnTwAQQlbJH-EbAvWm5rh8DT87kXaT4PHNwkzDCeV9HeXtnNrZUHUqVD-k5vD8yel_uKette4kkg-SE1a173Hw7ge871zphD0VOVHgOrb9XYLeiJOuJzERwb-x2LZOQVHvdHL7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=TSSTYb178wN9q0OctYxuvWcgXHHsCVI3djdq2eWO5P5IeA3V3rzvEPHN5wTe9xOA3dIDQmLEYb8qNcRkHB0vncpPVV-oZYxpxgjtFSmcN8yoLy_4Q1IJDX6y_RuEWJHoeQ1hkvDwEo453Mgy86963cXltkXCAdlXhhFO2D_mDkm-LwhabX78tkCJU2UIpizhSFLTUcwYjHHTUBexnTwAQQlbJH-EbAvWm5rh8DT87kXaT4PHNwkzDCeV9HeXtnNrZUHUqVD-k5vD8yel_uKette4kkg-SE1a173Hw7ge871zphD0VOVHgOrb9XYLeiJOuJzERwb-x2LZOQVHvdHL7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
ترامپ : حملات جدید می‌تواند برای دو یا سه هفته ادامه یابد.
🔺
سنتکام : موج جدیدی از حملات را برای سومین شب پیاپی آغاز کردیم.
🔺
باشگاه خبرنگاران : ۷ انفجار بزرگ‌ در بندرعباس</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6087" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
شنیده شدن ۳ انفجار شدید در جزیره کیش
🚨
انفجارهای شدید در جم - بوشهر
🚨
چند انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
ترامپ : امشب و فرداشب با قدرت به ایران حمله خواهیم کرد.
تفاهم‌نامه آزمونی بود که جمهوری اسلامی به آن پایبند نماند.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6085" target="_blank">📅 23:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آمریکا سفارت خود در ابوظبی و کنسولگری‌اش در دبی را به دلیل نگرانی‌های امنیتی، تعطیل کرد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6084" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6HLbB9w_C1fmBi1An640Z2OWLwwiHYOl0e9ci9k4CJU3igryJiAIziE1LO3WtQ2umrfLyca1nV-9wLosVxG9Om0d3bggGgszEFUkx4_B-3VLuxub2RTAa0OVja9kxXlOcM1AoP8hSRAlCayV_l5FbpZkiZRdA9okWKWctr_FvFqvbZnsb1i3n1-4Ow5zObuy6Bq-D06gBGFFZKX1W0cljoBjh3CAAilK5n4fXyntiCVdtDpLffhwyA6hN-RASxCGa7gANUeJfMfeyIFFPpIOf9kAg-PQ9ygknYSjBs4xTZXHqWdTrhO8cfhFIhM0XIEFqyfzgopzQGkW__kMqlv6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انفجار در چابهار و کنارک</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6083" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645219e055.mp4?token=Ce-kk42gFk2DmkaxSCF5BwyP-ObYHcfdJEzMmCBnKSxQPlZXIUn6uVKerxWemETic1lPobhxpdgFf-zLYdQGMCoeJQDU8QoIsCs1K-gD6PCRMkhrMrbdFxrI9H9GNqHFfm4da2dgbUP21CuHoWE37DlyJ-7_EZ6TmwzMlYM8Z4vWlqTH8hAeRIx-cFrtJn5OMnNQ9oQK14BCWBsfumcnMpxP3AcpXcZ2bjXtmD3AvkoEqSAgV1IzSgatYLJl2pyugGFucfTbTjcT7waOwGOw7IgyMDsHiwPUhg-ivGLhH71KKA0kGW7cQOA4Fl1P7pUddzH9KyiDivehROQfwbhELw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645219e055.mp4?token=Ce-kk42gFk2DmkaxSCF5BwyP-ObYHcfdJEzMmCBnKSxQPlZXIUn6uVKerxWemETic1lPobhxpdgFf-zLYdQGMCoeJQDU8QoIsCs1K-gD6PCRMkhrMrbdFxrI9H9GNqHFfm4da2dgbUP21CuHoWE37DlyJ-7_EZ6TmwzMlYM8Z4vWlqTH8hAeRIx-cFrtJn5OMnNQ9oQK14BCWBsfumcnMpxP3AcpXcZ2bjXtmD3AvkoEqSAgV1IzSgatYLJl2pyugGFucfTbTjcT7waOwGOw7IgyMDsHiwPUhg-ivGLhH71KKA0kGW7cQOA4Fl1P7pUddzH9KyiDivehROQfwbhELw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.
این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6082" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6081">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏
🚨
🚨
محاصره دریایی ایران از فرداشب ساعت ۲۳:۳۰ دقیقه اعمال خواهد شد.
‏بر طبق قوانین اعمال یک محدودیت تازه دریایی باید ۲۴ ساعت قبل از اجرا، به صاحبان کشتی‌ها اعلام شود.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6081" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6080">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=VIa-3uL0ZxDpQhSxtgxf4ZfmhTvKTOh2mXFgqkBnLz66w2XNAMmMvo8xwX-eLooXaNR4JPgPEuypUEGRol6q2rfJ5hB1Cn8E08uKGPGM1-U4YjnjEuwB8GsXzsGXnfnJUCe6LnN86NwR3oKRkTDbmNeEcjpfeF2OYRkZl_eCyvn5C_y0vzrqfdSXN6vjT6y04GARArxs0jCfOest2p7qD0POYlUAPjWEFt0bELO17jV5gpx0dBVh8EWTj9wWM38PPaC2-hKVySZwfgLwh9sG_qyU5FZUpTd2rOLCNmBDH8AKulTiV2yQXKO175uYLYSYTTMCgfGuvcuEpanSJF63exDa_xJ6RMwexE_-lPcTFYequQQNfKSvvlhYsdNRIF8zmKo6bk-c1RK5DL65m1OiMOShnJKAhd_EQ07pYhGi4L_oF58jrrBVz7I16O51fIvQvty8X5jMj-K4mNw82GGKkWFW0WBuhMPo_hDFpZgcf7bNg6PbuYypo8Z8521D-qS8pmVPm4QVLKPIiRN4aCR6p8w1dC_ZL1BZaukk1i0-maVR8fnMCLHkQbBPRCrtb8yD_B2geFHh1CkTj55VVjhOLGoofJJe1vKG4S3X4KpBXcJkpJWja3ROLeAnyf99Lk-42HtpPNyYoMmJ4zbtmnUIdGgMHcnOy-_yG5ehHP8bx08" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=VIa-3uL0ZxDpQhSxtgxf4ZfmhTvKTOh2mXFgqkBnLz66w2XNAMmMvo8xwX-eLooXaNR4JPgPEuypUEGRol6q2rfJ5hB1Cn8E08uKGPGM1-U4YjnjEuwB8GsXzsGXnfnJUCe6LnN86NwR3oKRkTDbmNeEcjpfeF2OYRkZl_eCyvn5C_y0vzrqfdSXN6vjT6y04GARArxs0jCfOest2p7qD0POYlUAPjWEFt0bELO17jV5gpx0dBVh8EWTj9wWM38PPaC2-hKVySZwfgLwh9sG_qyU5FZUpTd2rOLCNmBDH8AKulTiV2yQXKO175uYLYSYTTMCgfGuvcuEpanSJF63exDa_xJ6RMwexE_-lPcTFYequQQNfKSvvlhYsdNRIF8zmKo6bk-c1RK5DL65m1OiMOShnJKAhd_EQ07pYhGi4L_oF58jrrBVz7I16O51fIvQvty8X5jMj-K4mNw82GGKkWFW0WBuhMPo_hDFpZgcf7bNg6PbuYypo8Z8521D-qS8pmVPm4QVLKPIiRN4aCR6p8w1dC_ZL1BZaukk1i0-maVR8fnMCLHkQbBPRCrtb8yD_B2geFHh1CkTj55VVjhOLGoofJJe1vKG4S3X4KpBXcJkpJWja3ROLeAnyf99Lk-42HtpPNyYoMmJ4zbtmnUIdGgMHcnOy-_yG5ehHP8bx08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی جدید قرارگاه مرکزی خاتم
در خصوص تنگه هرمز
ویدئو رو باز کنید و به چشمهاش نگاه کنید :)
یک دقیقه و پنجاه ثانیه پلک نمیزنه
ابراهیم ذوالفقاری محصول هوش مصنوعی :)
یک انسان عادی، هر ۳-۴  ثانیه یکبار پلک میزند، در یک دقیقه ۱۵ تا ۲۰ بار</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6080" target="_blank">📅 20:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6079">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLQOwF37zlA4RapdfobwjstP0UtMnN9ddpqv5PLOZY1c8ke_vLJVgLRtyOXIHyQsaEKGTse90v3pUrspoQEaKqawKaqPjPoUPgdEdIrstBdapnd3H80Du07ZccWiHWUf1daGmcmXJThDRw8iWFGWcs0u7thD3s5wJ2RdUhbiw9chv_xYJ2iHPoez6KVZ7o76YON6qataArYCQTYpTpD0QbOCrjbyC8an2uNiWnNerhG0Ne5D_bZ4Y3PARNBuJLb7HucbVN5AyCWQYOSdI6Sky7k4vRYLhV4LISHbBq_s8MWh2YA0ELDQ7zAzt0hoHJh0xu0WMQLMJfTc-IaDbrdRBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : از این لحظه به بعد، ایالات متحدهٔ آمریکا با عنوان «
نگهبان تنگه هرمز
»  شناخته خواهد شد.
اما در این جایگاه و به اقتضای انصاف، برای جبران همهٔ هزینه‌های لازم جهت تأمین ایمنی و امنیت این بخش بسیار پرتنش جهان،
۲۰ درصد از ارزش تمام محموله‌ها
ی عبوری را به عنوان هزینه دریافت خواهد کرد.
روند اجرای این طرح و شکل‌گیری سازوکار آن بلافاصله آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6079" target="_blank">📅 17:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6078">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fc7BeXUw6Czsi41U0t5GGP6yRf1cRV3-Xyq0asKrqMcatIN3z269XaRc5jcaK1r3jNhxvmo9I1kZychq_6FeFHUolfqNs7Fp8CSAilWTmEsRZWXXKnGQ52nL1SJ_m9USw6cgRlH09RL1fD4YJkXl826EnkZQMrXMO9ci1V_dKbB7sGkhyvOj1bGDBihHlESDH9MQHcnviaAVyXp-PXtfu7u5Czv8DD46urCCu1WmxSg5_s7nL41m4mYy40tHTccPRd2gaj36m1y4B7IiSR0ttgeyYm7-HLSJy8s94M7f4w_KURLR14ij8esw50K1WRD1r3jjA7Y20qgbaN3RZAiDLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6078" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6o-PD_1uI8vhPj26coZNxP-cztslB2rDS--bFa5Sg5-x4pOCWP9jPdrH8roGo2ygfKhtX7xe2PjBsiB89jUXmzXxC2GruQKYtE9GsoDXY_dxCAQIjO1KF8N7bUG6nGvIqAoJkXsq_0J0wxqqNCWNCfrYhSgXt9VqK_CBcLD0uSIAcNzFY-RKdH0y0NAbY02scuKqf2mO-nZzU_nm6npI8bL48536XbmBojO8fewVa4T9knERWpQTR0tMoeaLOy-XQYazk2tIyFvjqMtoLyS1yMDBahU0DD10ITDQY_jLitR1ereqSYe0wE_YWH65BS-iBeRJ7-IO3CLzEjJhqz0og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6077" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ درباره ایران:
‏ما کنترل این تنگه را در دست خواهیم گرفت. احتمالاً مدیریت آن را نیز بر عهده خواهیم داشت.
‏ما به نگهبان تنگه تبدیل خواهیم شد و وقتی این کار را انجام دهیم، هزینه آن به ما پرداخت خواهد شد.
‏ما ۵۰ سال از این تنگه محافظت کردیم و هرگز پولی بابت آن دریافت نکردیم. بدون هیچ دستمزدی از آن محافظت کردیم، اما حالا از این کار درآمد کسب خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6076" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
دولت بریتانیا سپاه پاسداران را به عنوان یک
سازمان تروریستی
اعلام کرد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6075" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">عربستان برای مراسم ابراهیم رئیسی «وزیر خارجه»‌اش رو فرستاد! برای مراسم خود خامنه‌ای، ولی امر مسلمین، این بار «معاون وزیر خارجه» فرستاد :)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6074" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdJoL_IyL1xKHpyrQVFrBjaKkw3aVqlz0Yme8FFgIFnDv6_vIeBhkq837hn-iYZVWhPC2j_86cq1GPyfsMTa_LR3w2dZIvr3hcPMNh6g_l47lHXZj7bJVRpQHtghGzA4pEw3P3CIrGrCP80ErWknBav1awVrCjds5sTErzIrqbuoigIwem1pBqlLIHozcwBYJL-0qzVHPo_zY8cSd2gE2km5oiYPscjQFSqhB67wseV49bCudyM-IuIksFPrVpsFIS6o8x_rRx1w5hGhUafktPdbpM3rvZIIusaRW38SQ2B795K3nbxhXmW6jSAngTbQAJbFFK__w5gLgiER0x_7Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTsJPg31RIKFjMj_iFIOlbO0DX1aZ5KoZwM4EIsjSkdc2Xb3g2apIUHv6l6uPuz0CLjxiIh_-qy8csvJf4BXJNHOonAhGLXAVWMevzIsC6m1w3YKLXpUMOspKF3g51iUS7A0FjRN2dxvRlvmEFwRyLz9kNvL9Iwrwo_qqQA6ninOqZ__dNFJw24kh8Hpo50HERuEF3F6zAZfY3i2y24wtNhBnqlSb6cGdHdqi5l3jkKDjiI2O7Gxqke_YzT8bEekmsXZfMegAcPz5CxYjTMXpz-Fhjba4GsVLcUYJgexod9Ne8bjF66pZT6rtibdEzaYQToOJHW2_WIvQteXAY-HuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6072" target="_blank">📅 13:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6071">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKNG6oaZ8Sz8tklfEKk6sd-PQFv7WUAqQKinbP25qNtXalrwrE8Pyx4FoDdcX1pftk4l8HZq9-APw_SIW7_NXMevenj0b2BghDxY4YmMoVyEO9ZEFgH6EMDORT9bjtj6_33tNpeK1R6XY11h2eAHUBoEUwseeCWCggyDwSuonpPDCiOh17t1b_jVUhMNkRpRraLwEosxxiFEcuQG8od2XEmj5lbzVj7Nhle19YsXswTx1l7I9f2dQyAAknyMKoTmO-JpaH6CVEbfYVMZ0ycEqlp-Z30xRWEgb_lwtSBbl1oxILeqVV6BgyraLsRoGmMqVVkZgDGVfVDsLPcR3NNlPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6071" target="_blank">📅 13:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6070">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5qp75RaB2ruCLJfvLkOvgy6H4Y1DWgfr3BveIje4NZw_-iN6JlSXT_Hd83jz9lRT3b4z2mkU4B3nz94giz6OWs3agDn0cSK0Fkij3iOI4UVHd28WPUwAf2SAVUz0vw0gESKQkwhBCIcHfHudHxq2JwrVsyhLo85cK2rm_R6lw6OxOtXX2mXihkKc_3pl4QlqO5U06JaNhWuGlmUgfkLhspFTn32mTQq2gf4lpQmdeiCnaOjJeG7WvvpYOPdsQPKkRIBs3X7TPIbbLWbg4ugwmKCFbSOduKYjwa47jcGdJvP2DuXiqEQ2aBfvyAbjndNdjqDWvuy2O6lwSIIVlBdqHndU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5qp75RaB2ruCLJfvLkOvgy6H4Y1DWgfr3BveIje4NZw_-iN6JlSXT_Hd83jz9lRT3b4z2mkU4B3nz94giz6OWs3agDn0cSK0Fkij3iOI4UVHd28WPUwAf2SAVUz0vw0gESKQkwhBCIcHfHudHxq2JwrVsyhLo85cK2rm_R6lw6OxOtXX2mXihkKc_3pl4QlqO5U06JaNhWuGlmUgfkLhspFTn32mTQq2gf4lpQmdeiCnaOjJeG7WvvpYOPdsQPKkRIBs3X7TPIbbLWbg4ugwmKCFbSOduKYjwa47jcGdJvP2DuXiqEQ2aBfvyAbjndNdjqDWvuy2O6lwSIIVlBdqHndU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56pmOuqhyLIyrOj_X36tAhBIaFpwtZ6ZwQge-XVeXNEazxkSEIWKir7TBRT57Ug9-1ZNSqet9ZR7juTw1JJ4EqGnkMe7mHNfqyxZT-tPTHCay6lO2awd-5PSSHvf62fVEAdCIYLbZUnWsKNh6Z5yfO96iiSrHrQuzo_GyTnPhvuvFP1TV6b0hfk9o2U6UXpAWO6zqmVAhY6Hc4PfHNj4nPi3gl0cvzwMdzQ11b_OTS4Jnspbm3Ezo86v6J333Rzjs7sK2-zi5nW-RnTEeTfg8Nj09W2S0w9bzYakvg7DoYYu3y7KGynZx-l5AFkdH7uLiGH67KG7vKDPrEUexCAyaQ5Go" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56pmOuqhyLIyrOj_X36tAhBIaFpwtZ6ZwQge-XVeXNEazxkSEIWKir7TBRT57Ug9-1ZNSqet9ZR7juTw1JJ4EqGnkMe7mHNfqyxZT-tPTHCay6lO2awd-5PSSHvf62fVEAdCIYLbZUnWsKNh6Z5yfO96iiSrHrQuzo_GyTnPhvuvFP1TV6b0hfk9o2U6UXpAWO6zqmVAhY6Hc4PfHNj4nPi3gl0cvzwMdzQ11b_OTS4Jnspbm3Ezo86v6J333Rzjs7sK2-zi5nW-RnTEeTfg8Nj09W2S0w9bzYakvg7DoYYu3y7KGynZx-l5AFkdH7uLiGH67KG7vKDPrEUexCAyaQ5Go" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6069" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6068">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=Eikf8nQQ-wTdgPXD850_ODeJOl4B0-x_MRO5npNE3LWor71mFyDMZ7uvoHxiGJCNAt_NX03m2JBCEQMcodMGH1eKQjZLohwMnvY_tnavzfC8nB9JXr7JxqISDKTj7Jz0oBT0UG5eTnzG25ZzlCuZKVM6WgZg5Qj_maohel9bYhxkIuG51GIOZc70oMwV_H223CrVAjlLdjBl4MmnQZYzGTA-IY36P71xyDM2xrrQx8aQKh7QD4dY8wofDQOfiTajAEfzcTpYK93A_6D80Yys_rZqOl2qz9WUuN7LCvvl3tYY6CKG0Npd9ZUZH6kFTT-9YaTy3OPcNHEnCugZuY9QdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=Eikf8nQQ-wTdgPXD850_ODeJOl4B0-x_MRO5npNE3LWor71mFyDMZ7uvoHxiGJCNAt_NX03m2JBCEQMcodMGH1eKQjZLohwMnvY_tnavzfC8nB9JXr7JxqISDKTj7Jz0oBT0UG5eTnzG25ZzlCuZKVM6WgZg5Qj_maohel9bYhxkIuG51GIOZc70oMwV_H223CrVAjlLdjBl4MmnQZYzGTA-IY36P71xyDM2xrrQx8aQKh7QD4dY8wofDQOfiTajAEfzcTpYK93A_6D80Yys_rZqOl2qz9WUuN7LCvvl3tYY6CKG0Npd9ZUZH6kFTT-9YaTy3OPcNHEnCugZuY9QdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=qC-g8xgiqgyDjpbo5bcxGREfvUOWqfp1LHSJs1qqCLqrDmLoVFIdt_Mv3AnSmdLITywWFFuYFOCpYLTZBcNRMtZczdkW-oQa050UHtBUP-sQedM2IDDLw7ATn5hmUndHiy6ivTNC7koXepcrCPbApe59WwOXYO9aYlV-D0TzW4I8gpwg9dXfcAusMJ4qLjM_4M9YNX91x9qEiJ4A_z1jqJ8MVQklga6YHUfKUTiI6YodsuIAFd7yUSwTo3MRM4A19WgBCtChY0tRt3mVfylA79RlMRfTz02OALMczk5zIc_9NIcGztVBp18c4EIeB7dAqwFY199gGfWuc-FDCXPcAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=qC-g8xgiqgyDjpbo5bcxGREfvUOWqfp1LHSJs1qqCLqrDmLoVFIdt_Mv3AnSmdLITywWFFuYFOCpYLTZBcNRMtZczdkW-oQa050UHtBUP-sQedM2IDDLw7ATn5hmUndHiy6ivTNC7koXepcrCPbApe59WwOXYO9aYlV-D0TzW4I8gpwg9dXfcAusMJ4qLjM_4M9YNX91x9qEiJ4A_z1jqJ8MVQklga6YHUfKUTiI6YodsuIAFd7yUSwTo3MRM4A19WgBCtChY0tRt3mVfylA79RlMRfTz02OALMczk5zIc_9NIcGztVBp18c4EIeB7dAqwFY199gGfWuc-FDCXPcAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که این ‌تصاویر از نتایج‌ حمله امروز آمریکا به جزیره قشم است.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6062">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=hr8BlR-Wc1w3P4nf1ttKzJTy6_L4JZx6CKqM1dnMLGNxhPO4oeLLPS70jj_TcaYy7j8RWgVsCFkcsqMzFCTpE11P99cs6xSbpfWd1fdTegtcSw3JJGG29uv2ylxhVWSE-jFXgDxVskRgYLD_7QiNunNcASDFM94M3Rei08vNl357AAWJnXUXWXOx_lgzsBGDSHFNAArUHzIozODvgcvsb_2psn8CukFW6q6cdbKeRQK63GVcvkeF0D_1d-M7EEAst4ZLfiM1-v7ckjCvrpx9KPyEZOK8DhQGJVbga1hIFqtl8pqDyf6yBKYF7H1OdGT7rE_h_kuouz1yNLXncjOCMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=hr8BlR-Wc1w3P4nf1ttKzJTy6_L4JZx6CKqM1dnMLGNxhPO4oeLLPS70jj_TcaYy7j8RWgVsCFkcsqMzFCTpE11P99cs6xSbpfWd1fdTegtcSw3JJGG29uv2ylxhVWSE-jFXgDxVskRgYLD_7QiNunNcASDFM94M3Rei08vNl357AAWJnXUXWXOx_lgzsBGDSHFNAArUHzIozODvgcvsb_2psn8CukFW6q6cdbKeRQK63GVcvkeF0D_1d-M7EEAst4ZLfiM1-v7ckjCvrpx9KPyEZOK8DhQGJVbga1hIFqtl8pqDyf6yBKYF7H1OdGT7rE_h_kuouz1yNLXncjOCMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=ncodWPQI1rd2Ry6E_C5nQi_-9-N9NTAey2J_FNnoltE53K-Ka8nf_iHOr4QiCzcJdqiLh2_ZduNDNMbwcdR5hhtAjk2BQYeYso4aJgjHhITCq6o2cXyXIGjfkJ0G6sOoecHDh5IW5U2oDzpqfpoaleD3ga7255yKYft0kscMaS3R8rf80NPtFiGkdPzQjCbnue0L9_iF2qklQvVH6UHV9Jy0rmZ6Rvxk4KwMViVsLrt-2IYFh-TZHy_wsSnh-p5rT0ZnHbtIlo8mZ5s2jek5ax0HlQM1KsVwRnjwq3sd9ZdvTBa-zw6-1PqrOhUorcj8MVbrHlEWmyD7QxRW7Joh_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=ncodWPQI1rd2Ry6E_C5nQi_-9-N9NTAey2J_FNnoltE53K-Ka8nf_iHOr4QiCzcJdqiLh2_ZduNDNMbwcdR5hhtAjk2BQYeYso4aJgjHhITCq6o2cXyXIGjfkJ0G6sOoecHDh5IW5U2oDzpqfpoaleD3ga7255yKYft0kscMaS3R8rf80NPtFiGkdPzQjCbnue0L9_iF2qklQvVH6UHV9Jy0rmZ6Rvxk4KwMViVsLrt-2IYFh-TZHy_wsSnh-p5rT0ZnHbtIlo8mZ5s2jek5ax0HlQM1KsVwRnjwq3sd9ZdvTBa-zw6-1PqrOhUorcj8MVbrHlEWmyD7QxRW7Joh_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrHwaAYPwoRlXqm5cCbN0sbMvvhW1aUE-Aq5_NrFUa1bM1Eb5etQUg_PtSJArrmpEuCi2025E-Qlmd8_GVIvdnlloTf8-YZTCEy21UfmB-fLi4Vg9f-TJIC4bc3WbmqkqlD32NxFGKanDsgWsb-_vLPIrP4NgjrMzXlIQH3ZL0PtsUxzAp8S6xpOpqEfnbgx6UvnrB749bPUT2nBwHIrax2pWu7y2f9TjTAixGO4749vR7KESxACft3ESpEJtKHqKsNaH-CFFDEElVKCoCv7f8aR04c1FgU3tmbMhfn72LSbpTQma4yYRpyroYpvGA3D25C2cm40u3PA21L60Yf_oA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dckKy5tRi-zDxeo2mhPfM3Dp6nLdKeP294HbiHOHHqfasapBzpwXA0AeM69uH6v9GoDupuPFXuiAjr2st9e__IVJxjKZka12RXjpMQorxFYu_mKfCtqlUqtmfH1yD8CyMLm_hSiTcISyp8LfQ0CQ34KJWg3ntrM3hHTfhhiOcr5XAZlxj4BmOEfX_BokY_G_Y926sh61PTliSFE2hulICgdboR4GDKTnkXmDHcV2Zwa8wTQu527S4UyRNrSZozhSIR9NXFExRUhhjlxrYSZaEBC_v1-wXKogaDk8lqdX50O5lMpuzIEKh4bk9isjpUWsVB2OX19e9L2jBZyJNd_3lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=m91Vg_yR85Pb68NecLn09sAn4sPOx_ilnyxJPBJZsz5pbjFc4aGL41Oqn_wXBvuKdkauK3MNxkNVwUkKtTnxcsQLkIMmXY6-M-ciwsCItGX3i2JfIQkxh7HwAhgVik_KwXyZluF_KM17Yli1A7Os6IZRagUPBVdvtL-r-STSzp_y7OZrZizkzkJwqFIAsojg31cfaMtn_N5khVaOd0d5IW0JXodVXnfOmieiGQQ2ImsuVrOxHq2wjMJhOkayfgKmt57FKnsZsdcJ6SpJxarjJjWMVYoaLc4PDfXtSfL1iZTIjthWwztM1Zd54edIwoOudvgPhvImcRkOmDdUIuswrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=m91Vg_yR85Pb68NecLn09sAn4sPOx_ilnyxJPBJZsz5pbjFc4aGL41Oqn_wXBvuKdkauK3MNxkNVwUkKtTnxcsQLkIMmXY6-M-ciwsCItGX3i2JfIQkxh7HwAhgVik_KwXyZluF_KM17Yli1A7Os6IZRagUPBVdvtL-r-STSzp_y7OZrZizkzkJwqFIAsojg31cfaMtn_N5khVaOd0d5IW0JXodVXnfOmieiGQQ2ImsuVrOxHq2wjMJhOkayfgKmt57FKnsZsdcJ6SpJxarjJjWMVYoaLc4PDfXtSfL1iZTIjthWwztM1Zd54edIwoOudvgPhvImcRkOmDdUIuswrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوینده شبکه خبر جدی جدی
خبر درگذشت لیندسی‌ گراهام رو دوبار خوند :)
فکر کن تاثیر یک سناتور آمریکایی رو
در برابر کل نهاد مجلس خودشون که ۴ ماهه
کلا تعطیله و کسی هم اهمیت نمیده :)</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6057">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uutsz7e-tCzm-L5E7esQPT-wLfgWh_9VkxjEejQYzAfuNJp5RqpWb3NeZIBKyY7GzH0hptpa4aNLMejUJsVzFIHRpUCB6RYWnV1cG6pVjBlsl9FqAz1Y_6dctu3R_-Yk9gPgJPh-EOivgmNmk2hT_BNptVC-7AS4bmWDX1WH21QdpKCgY3KIz_8Kj4gwZvrkenEsSmg_t0rokuw1M923ce82PBfmgbz6T8Xmx4mHvk54g-FsVxZWipA_GmVRpPcu18-ijDxF70ijv53W8mlW4JzJV1wxKGoiTETElXKK68iIj_l5uNTsaWPdgs0PKOViugifsIIMf9X7kgGFmokS8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=mxQKKBTvkc5ivR9LZIe7D2PbwjymfMJr9HYhHWv_ann-Z1YrK5dOBIQPNWVsgkHn4NBUdeQaqGJRL2uUZdwk8ttTkRvmWXC8yaiZIPZTFdPSPi2EJr5n8O11YNRCTs7XTHcGAex_5rvwJLz1rCM0oyJkjTan1S-W4u03PuCJmkIGNBlm8GYWZIgQCxQzPq1f_hWZBrq5NQIL1jc_20yG_xFV4M2FAfMms7UdzGmU7I37jJWT07RXV1JnCfT6u3UGM_9TYZiTU8cHdbCWGU0dhdkEDe8_794zF6y_xpGSgtu3El4kXvqbjoUNxFC1K1noevF35tux97H31z3lYBIfow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=mxQKKBTvkc5ivR9LZIe7D2PbwjymfMJr9HYhHWv_ann-Z1YrK5dOBIQPNWVsgkHn4NBUdeQaqGJRL2uUZdwk8ttTkRvmWXC8yaiZIPZTFdPSPi2EJr5n8O11YNRCTs7XTHcGAex_5rvwJLz1rCM0oyJkjTan1S-W4u03PuCJmkIGNBlm8GYWZIgQCxQzPq1f_hWZBrq5NQIL1jc_20yG_xFV4M2FAfMms7UdzGmU7I37jJWT07RXV1JnCfT6u3UGM_9TYZiTU8cHdbCWGU0dhdkEDe8_794zF6y_xpGSgtu3El4kXvqbjoUNxFC1K1noevF35tux97H31z3lYBIfow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAta7wxtvILrfOnWJVCKUj4v_x8AuJ9CZ7pcrqWF7iCMFja_WxNKgBae4vl542Hq7ZJxPmz734ESdBD4s4KShB-VSyBGTAj9NyZJGgLeJ4TKd9UuQNtn7ONGIh-zWGhygD0kIUb-wOH3AiRRdNH69AqT3FFe8I3jn18PcuJUyLHBglM3niiW1wsNSX35WMEJCsbLlf5ZAVVJ5O8EyaH6lppLf-1ruuoGohz3RXenW0sfNYQCX_GQhI9GU34BegAyjEmlnL8rin4GKGMJbQvmQVSt18U-7VCaC50cLqRO4R9VtnDBWu1SA8CVtrGR2lZRhSWfvWQ_4G6XBuM28aCmOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم این خبر تا چه حد صحت داره
ولی ظاهرا دولت اسرائیل
مهر ابطال به پاسپورت خامنه‌ای زد
و خامنه‌ای از سفر به بیت المقدس جامونده!
او هم به یاسر عرفات و عبدالناصر
و خمینی و صدام پیوست.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spVc_mqdD8pcAZpCXS-7QajLy6-TDBJXzXv5TIP0GJjLWCeNAqDj3i_2YLEM8omxZD_SFeSQFQCpkLR4KgOdUJ95bG-E7k8t7YGnh9wILZ9Yi3s-dNZR2aY316D-1dqDt9e61jpjeTMLONGCEoF9BBOhQ27lm5UL6UK3TpACavc-FXrbx-JKU5hOChrLLgzC75njd7CjI_XA9pqeM7s3VyeXpNDhkiEXYoywRIuEwyJzwYRYCGkp4wGH-F5oPB2tjozBWKbUtOu3Fz3zdCRv7jFBWpwiZoYMvnQ71afAea_64DRytEnNqikYgZuzVcC2eEYXje4-tFLnxbylTl1F5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgZ_I6arx1WS_18pTIn0sgLE6kLfF4kgnmaxU0VMxMXsRcVqhYE1wwNhct75kjJgiO1MVg7UtAL46kMXG0Y62mG0yF_2VNYPnQWQaoS7BH6WrDZCR8IYr8y_A0mwAroHBi52B_56q6hSBBFqkZkCHBC4H7A7JbVXmP5I45WR27SkkOZpC23KOvh_mNWtJhHRo-aKcEtmq6EjbaNDIijgQAZWWC87LTKXhca30BeQdjH-Kfyvau7PoUiESA6E92M4mZMpBgAU8ViJa2y7ulNwGJUQfaWzMBVspfcWPkDrw0zzpvbh1GtfQ7nlLXEPLDxOeE9o1R8cPNbpu_b030g-NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOqJh6QojPDeBUdkzvUXsjyz5HetwPR_CCWyT2KKZLfaP8JdYHePUmF6GxPElFSWsoYLkKdCJYZoSRmHDEhYLxUpMzDlfuEZpD4oMTlHv6EhPJ_zDSH2ye95g1Hz_HUEPJMjatEu73bTN5xId5VePTSQ3jUAOV7kBGZhDoHANG9UdoJERBvD1CLnKjZTdjJ5AzeUQCIr2qh41BWNiY1h7vgjuH4cOQmxgE4xJMVLhdIIpgoB31Wt7Btp5b6GbTp-bl0czGvkPzNfkhvIKiWFygJOru3FS2rQepMcyNMUEk7pExMX96yhDbytbCHrBbTImynFl7Mxsz79KM-ilaUx9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-CVsKInjhbp0y_zqqVUZfMQc9pfmSVj9aZV2vhFtAFPpOCSgkA3a1e-_ynoLf_zEvWSUyUgwoMixYa9fF2bHbdEAMrvFzAO7_lEcK9j9f9J_nAhLV0Q72RPEee5kPndg1vyfD9un99Pi9rQaY9m29itGyXFkx0CPrlwdM_g2WbCZEeKcvOd3JAIPpTwVE6EBYMHmd0zK0rVOOiHLhdIEmKsT4w82uAE5YeM5buH9ub4CRzSbAA-tr06V8uUJDHhHi4RAqCsMm44caArD5I_ZoRwU4uBRnB5ZWHvOt0tPBZPdxJIKW9-Tc1GXZmRV3MKNnvrdOxYIErnSs2yUP9OUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DZOvgchY9lRlpfMJMXixe7Ovpz52cUFt7rwKqv4lihuhP828An3jr79PJB--nIjTSyNVQShrOx4g8FMEaLroGDyB5eT-B4gjCaelGgjYn7mjSG-lyXUKNiBvblf43xPZ2jWQLUvswEYytpclmB7Avm--ie9LkJ1P4-gSFkKgGFgwzMop-iXJJsrYqWqB1fzMflC5Rc83RGzb77wMG55Ixa6SgUbl8ez5Ivz7jcFxirVtVX11RMCRuSst8rY2zzYI2L75t_h6NCbw3rgZGHp0VSQbVAT8o-0Tpvjo3WJYY-Wdk2Z0qJ8s11GIhdBBQUANVal4dZy-XNF_9aAg37Ap4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGELpGnyR_DHKEkLJheoVD8ts010MGs-f5SGzUe1-Oye5LIncaO7ilMXVCbT9PiNMBv914zn7WnUixomA0hekGZ0q-ptEexU7RCDILNmA-TaYdmnJs4oquHLOWojlhPjrPjPSAQZHZaGOP3x8Glc8fXy66swtOVp4N9o5SbeDdVSMUwEdnmeCBXPWSpR77lFFv1xk0yfdZ6X_Rcyj2dt7fT1NlqlU4pYn4Uv_LPl4Ezc2QX8ZuRsuOqnRZPUe0uYK-Qy_z_qiEDUqMuJ0Dq3LCMlSEbhqGi8ELpLClr2baICkbML_bEWjM07adiupAPiBxabwgHgrDvHf0rN6w5Vgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUc2ApQ6Gw8ksHDjEJiBR09kWxIlJn3sgvgn5bETcl80wWzkIufwMbAcHVVbueljAKKPbLHd06KDHGPpDvwVCd6Qc162OaHzvrWezgGQR21oQF0pZNe7PXSpMkWg_yX7ihHXlHBwagNN845ieAtTXTzpFOByiCVRIvojXyQKc2nmoGKmp_Y5JEK6mgFQH9d267NiOu8CpJfl1dwL6Ui62g_Ut3WAkgVLuSvtM19_-_1FMkPBRuVFrVkFEnhDByeE1bj66_eGbNBK-g8XM-_K15T4b3MI67TWNQ2L2_HuZ9nDpQ4JzYZ0VpxOdPbQfmIFMP-GixfJOVPz8W9bNneCHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShYDaQT4hdykjiN1UVkI-oZQEW33x05kMwPzDIIcW9X6_OnaLVywJaUUkG_B67jc1Ucp1Kl7_D4_6pHdwbSy4JNv3emBloSkuH8N3ma2FL8VRQYO7MPnbgUIPaVlGOUmGwD_tHBofUiGwxoosrO3tYva5UahQpt532B1T6R5QYhdFOqnTR34tCPyT0kU5Hh451QQd3VUPdMjsSocZ3UovGMqU-yNRoWXm1g09AksYvbfMWZOlqeViqD2k3L60zb5O4QTiyt3DayNgSUCk4VTn9u9LrNFmzBD1rh8HfK5UJ79_8qWQ7PUewywH-IS1NColAU2kBUKJQW1IhP9rqbyrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5PIx6IbHV9ndGPUCjdS83QPYZW4y0UtHSQ_9jhcGvn47LD_7QAWwlste-r94zl2a9MMnCdrnKGrOj_i-nBYJ4uB-ZAS61uFPplZfp1XV92Uwzc2vyHWAQTbPX50OPTvICt1N7mNld0yrB5f8b2yb3TjvGR4PTTWPnjHKTySOZ5GiNjpvg2dIwEP7z6L2jv373DdpJwTrcn8123z2ZAbLWq0aaOLMnIVI47D4icQJOYEBVXhbXReJSd6QdbPipOGX_8HGyjOlzBHqW-VT8BxgDqGYqtQ5zO_ZDo_YOOkvly0fKr3dic7r0kl8JiUTVeFeaOWh3HrwJ2VBZfP_fpmbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nvv8cAk2AxD9Cp8FSsRHOqOYP1Y6vgMQMuXQlIglvymDsbVL5SHPrO2o4L8MW_3qEBni5A_5Z40hQtuz_51Kn52qBrHM6myutHpGdXHlgMVvjB7Kkie8Rldv2NeTuBqjbfsyjX6flz_N1APxPr9zM6fsubo3_KmPWFx1OPDDSGLC-B1tEcYlltA3HTUKnXXyAeM_N2UJSGOIGN2l3S0PBKhiCzYA9KTYVhmqVazz3X4u6peqHnRkypq4Mo1ktbZCg8TOSzDM4JwTXZzk4XCczUOKPDjzGU98WYWagboSzLkjIgZ5xdJ8jALrkwyDjuRrMuY3hQJw19AeWUO12C8c0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=fyF0Qgf8mh1L22oVf2A58ndzQcOJ4pqv4AWbfSM4qlbjeZKMRy11Kyu4igtDvW3PACrNY3JHCPQpvvd95aiPYPIhiSuTYdcGb_9G6op1hYnXAvuuvTnTpGSnDZCXwZh3mMRQjny8CZN-VTQ1aVK_uqDyEq7hUSZI88PGW_69R3gs3V4-Z1gV1kXuj8-lzrHhAbdkSOaAxL4P6b2xk3VaXRM0CeZUO31Qrfp175CvkMF4D7-5KOCdpO0Fc--YX5JOaIpy_Om47FfiOZtZfhjYqA4OnSgxCZfCDTJM08awEoev8lG0H_GDsV0Ch9PghBNN_QXhtH8hElAJq6FT4zzYag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=fyF0Qgf8mh1L22oVf2A58ndzQcOJ4pqv4AWbfSM4qlbjeZKMRy11Kyu4igtDvW3PACrNY3JHCPQpvvd95aiPYPIhiSuTYdcGb_9G6op1hYnXAvuuvTnTpGSnDZCXwZh3mMRQjny8CZN-VTQ1aVK_uqDyEq7hUSZI88PGW_69R3gs3V4-Z1gV1kXuj8-lzrHhAbdkSOaAxL4P6b2xk3VaXRM0CeZUO31Qrfp175CvkMF4D7-5KOCdpO0Fc--YX5JOaIpy_Om47FfiOZtZfhjYqA4OnSgxCZfCDTJM08awEoev8lG0H_GDsV0Ch9PghBNN_QXhtH8hElAJq6FT4zzYag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cn_XUxgQsm4SLYahtKrsIMV48OnGu5dFEWK-eYcVy4A6eWMdr_sK2otNHLAmhJz2QOG8pb8tjCRqXcEa-e7GLcCd_A6iaKg8E5TI1thr6X7hUGCF6F1BO6Cr_JVMRUBlmy_lHmYes2oUeutYSVQ-zuDuK_BPJxtSeKxsXBWncxoLFfA6r2k1-3IcrJZAT5CyU-K2cleR7KHRfkVVt9-eDLHCc1jtZNpiKx54eWX27xvXJrIfB-Ms6PnOI7tY6J0YzYq_VhlJyun9rCqPMB1zouJl0KVR759KAgm0hKjJGUCcRnQkYcGByGH_BCAeeq_OHZFPg3Ak8da-VdjztAY1tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=vPuIbtplFfU3ClTiKVlrwh1fEPeN2CHr8dhIQUNiuXLZ7QN1hG96bp_bvJTsBEneyfk-eGXEWiHiqhqxZv_TWjUz3yIv_A1oiG-tA6g6jR0giH-3HCV03ALzdMSVy-87Jdd2QKV9rAVf0G_Mk4hjvY8lhCy9EMkQxO0uTIpKqXAm-hs81SMJUoOlsC3A5ScS5k1Ozy1CwOni9t-Y8e-vtZ08tbCWfZCo4_702ySB4IX_kE2oAH6RMHHCmMkEi2mvtnt5hFL82dJMoGfjYP9XTD84bzmYUwBWDgX_cFKFpP_MIG4X2687P-R5EtSjtEowV2lNY02Hi0BqePzRT3Llsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=vPuIbtplFfU3ClTiKVlrwh1fEPeN2CHr8dhIQUNiuXLZ7QN1hG96bp_bvJTsBEneyfk-eGXEWiHiqhqxZv_TWjUz3yIv_A1oiG-tA6g6jR0giH-3HCV03ALzdMSVy-87Jdd2QKV9rAVf0G_Mk4hjvY8lhCy9EMkQxO0uTIpKqXAm-hs81SMJUoOlsC3A5ScS5k1Ozy1CwOni9t-Y8e-vtZ08tbCWfZCo4_702ySB4IX_kE2oAH6RMHHCmMkEi2mvtnt5hFL82dJMoGfjYP9XTD84bzmYUwBWDgX_cFKFpP_MIG4X2687P-R5EtSjtEowV2lNY02Hi0BqePzRT3Llsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdBuBVXK_JDPeJuplrydvjFL53pGwGmDEezpqza2MXTNIUn1gguOC4UWlfBaCJxPrvvF2ptKysFqg30Lej5nUfSe1D-AwOeU_W9sSVZdSu87BfyBowBzWStEFEAVbWiA3tDLyVOPYthbNGmJ8rpBDsHNaVCEVnqRUa7lHEnZHYZta049wDFQXmfXs1CZ63hjTuThHVczbILl6X3REsy33WRV03Jjv8f4O3NZguaxuSHZHTuR9Q0Rhpvs7eCArBSc9iSYOItPYSbWzvC8WrnvD3V5Ubulg_F-eN6YlLR1txKD7i7tNNDAb0xcpOfytRqd_Z_wmDiW6eCprdNno8lUWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
