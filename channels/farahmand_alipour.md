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
<img src="https://cdn4.telesco.pe/file/XDGMX1kUkNs4lajqhaMhIejrqBTdlxKUraYZTHWrkw9lvcZ69DdPN4RQAfSZbI2vV_cNgNU5xftrRdk5L9gmoOdb2b2P7_I6g2qYr5WzggVivx-VF5A2MCB9aU9UWT4k-XioNRQJvOnEzC7P_5waZzK2drS1x_eWSkTaY_W95tVDcRUDylV1HzY5UnTOWzoo4wZ8nVckihgEoA8oYVu08KrF3CRGgPrjLuYJKagwdmGsot6omXmaqI1Tbv2PIiy6BxxVTK4ffR54pOsZbDQPRP7T-camkskxtyJfVYXgLoLrzRNhd6H0Zwokx7W8yb0dfBm-Q9vZtagyfqlLeVS0Nw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 14:19:37</div>
<hr>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=IU274KViiR9b3O7YWr8GacLJXXqShsd2a1npVj3O2ItFHCIWt3IDyBvu-KeKGglYkcqRmDixbIdiqLX-rGsur5jPeJxmw6LtMZw-RsM9tuHNhUKcYTSxskqmGEhFdrbEuYUZDkdK_waYHcFK6CYZHhFm18p8jfGX0ru_Z9Pt9nir2R0paxlmrKLlkZKlzBtd22pS69EDBSeW_HnLhX7EWql-LTmbXm510ZgC717ny1n8zD_M0lpXrmsOZO8YTytZvTGDVJadmLCptR_f29DlaNtSzOmLvbtt-qnZFZOohEse1NM9gKqIrUmJLcc1KZBdH79L5bLtM5VYbUc2L_MMpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=IU274KViiR9b3O7YWr8GacLJXXqShsd2a1npVj3O2ItFHCIWt3IDyBvu-KeKGglYkcqRmDixbIdiqLX-rGsur5jPeJxmw6LtMZw-RsM9tuHNhUKcYTSxskqmGEhFdrbEuYUZDkdK_waYHcFK6CYZHhFm18p8jfGX0ru_Z9Pt9nir2R0paxlmrKLlkZKlzBtd22pS69EDBSeW_HnLhX7EWql-LTmbXm510ZgC717ny1n8zD_M0lpXrmsOZO8YTytZvTGDVJadmLCptR_f29DlaNtSzOmLvbtt-qnZFZOohEse1NM9gKqIrUmJLcc1KZBdH79L5bLtM5VYbUc2L_MMpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=M6CzRIqyg4ICwVOp6wIcy7goRUkS9heIOuRgzCYG5gaMfPVQzqzj8f19Ic-TSgdSU9qZo5hLWQXQYolCmU3VtYMie3303BUEEmx83QfjmnS0WE6Gfu25SVJSfVZn5NiZ6aOauETTVPvL9PpexGsgid3poHiHHnXzOkJH_VimKJ-Hr6EnJ0ajs5SD06oK-APv_qYB9aoBKwhUFxYQctyLRUZi-LQeBNLBbGxS_F0biusxGgNBRCTKcyUsCh1vs4OxJLxWdJrbplvJavd6R2PllQyc-rCniX4oRQIOPU_gAFhA1RGFju5UQ0hIqLUS8lnZv7KTcZjxVQdwbc_cevxA1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=M6CzRIqyg4ICwVOp6wIcy7goRUkS9heIOuRgzCYG5gaMfPVQzqzj8f19Ic-TSgdSU9qZo5hLWQXQYolCmU3VtYMie3303BUEEmx83QfjmnS0WE6Gfu25SVJSfVZn5NiZ6aOauETTVPvL9PpexGsgid3poHiHHnXzOkJH_VimKJ-Hr6EnJ0ajs5SD06oK-APv_qYB9aoBKwhUFxYQctyLRUZi-LQeBNLBbGxS_F0biusxGgNBRCTKcyUsCh1vs4OxJLxWdJrbplvJavd6R2PllQyc-rCniX4oRQIOPU_gAFhA1RGFju5UQ0hIqLUS8lnZv7KTcZjxVQdwbc_cevxA1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=HIpZkecyjlswLl1I9n6eWU_PXqTPdGcQs9nzWDgl1h7A9sUm2Am5UbcsAQlmOVtpMuYglGXmzotofbFzjhrQ68smFjoidsI7YQfM_IN3ZX381HMShOPf0TsCq7zVWVgfYUxXpL0qzXdI05p8UYzR0GOlpWiQjHlCXaYxl2p9e5UxF1Yjnq9-vLgT5BeOabKvPXYnvrNJ2Y1I6pVvuGjzRXRa-23TzMwq_3ogbogmy5hNTD5tHUdjFq20fMygOhXlMZ_YeBmC3-vOxYNGMdOVR7p4lZfX7zGrkE67vBLoilq9YQiOGZqDPMkUPutL7xQhJqqwPtUNVCbU7ao7eOXkMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=HIpZkecyjlswLl1I9n6eWU_PXqTPdGcQs9nzWDgl1h7A9sUm2Am5UbcsAQlmOVtpMuYglGXmzotofbFzjhrQ68smFjoidsI7YQfM_IN3ZX381HMShOPf0TsCq7zVWVgfYUxXpL0qzXdI05p8UYzR0GOlpWiQjHlCXaYxl2p9e5UxF1Yjnq9-vLgT5BeOabKvPXYnvrNJ2Y1I6pVvuGjzRXRa-23TzMwq_3ogbogmy5hNTD5tHUdjFq20fMygOhXlMZ_YeBmC3-vOxYNGMdOVR7p4lZfX7zGrkE67vBLoilq9YQiOGZqDPMkUPutL7xQhJqqwPtUNVCbU7ao7eOXkMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=O1_p8wpk8d825BO6UCX2hCigJwul7281ltIAiQ1uDwGAIH0XCPjDlBQg6Hd4wIS3t517sau9z67MIRpC1Y1CxIarSFx3_Un9d9dQCmfaCrQ8jNsLst5CbON3XShKXnARFqypRPj0SnYRrLtjAkHtykZKjZv9MsZKHqjLs-8y_s19fL5-UOMKVBBuRPWXh0MkvtQr8zpm_XARRKsXhGPBv7qb6Ti3die8xGcPQ8A26vk5TRdmLchOg8ua5VB8l7VVes2iN62mjZEj4h4b1QtTHviaOb-EZnveZ_Eb3YXnYECi_7-cAeUVKRWQ--C9atAyJBQVudsgwqOYLpxK76RDEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=O1_p8wpk8d825BO6UCX2hCigJwul7281ltIAiQ1uDwGAIH0XCPjDlBQg6Hd4wIS3t517sau9z67MIRpC1Y1CxIarSFx3_Un9d9dQCmfaCrQ8jNsLst5CbON3XShKXnARFqypRPj0SnYRrLtjAkHtykZKjZv9MsZKHqjLs-8y_s19fL5-UOMKVBBuRPWXh0MkvtQr8zpm_XARRKsXhGPBv7qb6Ti3die8xGcPQ8A26vk5TRdmLchOg8ua5VB8l7VVes2iN62mjZEj4h4b1QtTHviaOb-EZnveZ_Eb3YXnYECi_7-cAeUVKRWQ--C9atAyJBQVudsgwqOYLpxK76RDEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnGh-YpDmfRCMmLPD7nb1dh1lmMEVB5QuLZEgSJGrQQxBi5s5hl4xfdIdG0Wbqq6SBC8cpK5kept9hHdecChdzfw1cIjcMqp4iHcAa1iXEyYb3ufTOOV-dabNlsfRZiqTTk7C5khsUe437CQnGn5UQk3q_o9t7FhkSfCm32pCmNn65pU8T0kcjAnSmF__MoP-LcomWUptwsS29r4qm4JVY_ZakK5Az3JZejHwDtHEdmnnBwusp4zoYwyoW3Flc6ivm2ptj6P5KEDNMh1keqx7Mkrvw58AYBYHmw-POI4xqUmf2MwKjFSTuhlIenatfsshTVXnfsLq3oyKyr2qqNTXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=AzjG_SL-HbH74xDsW-qMmq7T60FPjARxVa4osEK2rGiB9aQfABXr1mb03jyySs91xAviC1O9v65bRh1T_qngIv-jnL7tYZxfXUILP0H9FWKEp629EfRzIqE9vwYfc1JWMsB2sDNPuAIB_944JP41PtByW578JoyGnA1XtQMABsPzbQLds0GpOReKt_WPc_nvDV5ilb1dF6gmW-ZmXrHrnHGG6JDSRjs9X2Vw9jNEFxn1YSCkfLz0xUf1qUsKk61DlbRrPsGFLftd8MNjcP2CDM-ZHo67Kp9U4h4e2CqV-ynzuWO08poHTETPB3WgSI5tOrY7tcLAPtTHpExHXVKZ_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=AzjG_SL-HbH74xDsW-qMmq7T60FPjARxVa4osEK2rGiB9aQfABXr1mb03jyySs91xAviC1O9v65bRh1T_qngIv-jnL7tYZxfXUILP0H9FWKEp629EfRzIqE9vwYfc1JWMsB2sDNPuAIB_944JP41PtByW578JoyGnA1XtQMABsPzbQLds0GpOReKt_WPc_nvDV5ilb1dF6gmW-ZmXrHrnHGG6JDSRjs9X2Vw9jNEFxn1YSCkfLz0xUf1qUsKk61DlbRrPsGFLftd8MNjcP2CDM-ZHo67Kp9U4h4e2CqV-ynzuWO08poHTETPB3WgSI5tOrY7tcLAPtTHpExHXVKZ_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZJd5mdJLZcoBbHrOZLmlLpxJGfYFiroZAUZy59hTWo91kAukuJ58VtFMvW7cqgh9XG6DyZIx7cRrm5NBsuAA6yja8GyLHXfvPa7mpMx6Tn_TLL-E1qq3b8PmGagKL9kgtG9WZLAjYnTooR7eXUm7ZokvTonAPBI7J3GXh2gVZtFHr-ifJU8Kk4v2xNNK6kN0lf-P-l1msmj9OiWtDL0YI4y44BEZ2hCeoS-38q5wB3QqaKKf4d0_nAPo4rc-EQdLxIJRZVTChM4rZ8RmrbjCyHqeMM5T0_ExTbFm-o4iXMl6v2maRgqUrZQxtVtpUlfmpZ2oVbgR3eqMTUitILGxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZ_kiQkmCH5xpIUfQsJxkeQsNskPAUnp4yYjUa2_hJPxBU8L1iaWkRvygcc_Rj33O9A9Nn_ueiMIw64ZR1D5D6VYxJAkXkkVHaoi9hlREZLqg2EoDJMyKNgZZJ9z5aW0ZqdkohR8EaKC-zklWGfWWD06vVhSzjrphUCM1XbgNei4dVLdjWMpMj6CHKe-Ip9lVzv_L4D1tIZbTuyf56Yv_18vSLjb9KIClZnoL40uW-OssLQo6J1TuqIO3erQqsPiDSVGKBIwISVnxD9Vglidzv62RSxA0pDeW4rrDlEokVg-lXDDTcwdPM38qQPgATrdpjkX8T9rhzioh1H1OzW_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لکه نفتی به جنگل حرا رسیده
و حیات درختان این جنگل به خطر افتاده.
اما این لکه نفتی که تهدیدی برای سواحل قشم شده از کجا اومده؟
جمهوری اسلامی ۱۲ مرداد (۳ آگوست)
به یک کشتی باربر (و نه نفتکش) حمله موشکی یا پهپادی انجام داد. کشتی داشت از آب‌های ساحلی عمان عبور می‌کرد.
پرتابه به موتورخانه کشتی «مینوان پایونیر» اصابت کرد و نشت نفت رخ داد. این لکه نفتی رو موج‌ها آوردند به ساحل ایران.
سخنگوی وزارت خارجه ج‌ا (بقایی) هم تایید کرد
که این لکه نفتی ناشی از یک کشتی‌فله‌بر است،
گرچه نگفت هنر دست خودشونه که برای بستن تنگه هرکز به کشتی‌هایی که در سواحل عمان حرکت میکنن، حمله می‌کنن.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6549" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9HOcmPk6OFctAPQYmho7HSwrAlyRgeuIStHhDJ4BIbpFsSWgN-5jfggVpBB6gMowdulFuMUCGWF7nYj5jIELAFxCkJ_tDPZuePJrmVXCKUgxeWeF4O2CAqoFO0FJI-UUSnGofAly2F6ow_88ABsBQc7KeFaa7LBmIOv4eWwgBdFh4nxwurj0gLsZ-C5I0tWYqcx2u85wxixFBO3CH3jD-lJoSAKLHjy723bxn8DKrhtvaLrfyP56XcPFXo9zgMKBmxV-0z8iFFZ015VWbPQK6i6K1oPYgzhSX-bR7hipuum35g_-6xudQrWOFLRDeLKalUnck1lCCZu1CflCaolxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بنزین در کرمان ۸۷ هزار و ۲۰۰ تومان!
میخوان آروم آروم و استان به استان
قیمت بنزین رو گرون کنن که بتونن
با تفرقه انداختن بین مردم جلوی اعتراضات رو بگیرن و قیمت بنزین
رو
۱۵۴۰٪
افزایش بدن!!!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6548" target="_blank">📅 21:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WU_WkNruyvGgmMTtTtqNlKd1cclAxuFdzc9OJ-rmh5qyny1hi5mdcgdtyYZbp5z6JVaM6mNRBhmSiJEPdOiefcHewWAF0UEM4JMOclZijA5Vv-j7oSBd78J-YYA9SA05lPi9ySaAhZk0BWbEa8mVi9ogBCba1Tv5FFKXCAOgyD4ZM7OBOdCD_pAKcqkec5X9S-lbUc0nllJySqzuCmlJyTsRQdazCZ2yDDm3J3Q0YQi-vCpJuJiQDkNOPeE7Ljjo_zi5-5IuTdLL7UH1MN-hryOkXVg0wsWUsBDbLMtrm4N_gY2bgowKGZCJxDcpICRPL9kt_Rvr5EeaQ4DSm_oMfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=G7QPXRrh9eiLnUBTykZQxAZGs8NgOrYEBLiEQVtlqekGe_09M2iBuB2i4sycYkJHZkYbKeI25OmOOEIuKuB9EnkIlr6Mh3RTgBObIDEouS-4jpDc5emqxhtVT8KKzGjuPAI4mU45naqfcCLApna_8t6OjEHGkB7Eq-3lx6P9hE5vbkzWjPW5szpcCbMe87fQil7cjU6rJ_kc0lCUbujYuqyr24qxrQuJdKLvCLog7XCi228HN6T4Coe4X693VTlFFwGrxR2YnP7d0oHIxBoUgf9urAt2WUekCeNgYv9Zc364l3fuHvQr6kOzwYKBAmooDknO-iLuWbsGSH1R5x6OLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=G7QPXRrh9eiLnUBTykZQxAZGs8NgOrYEBLiEQVtlqekGe_09M2iBuB2i4sycYkJHZkYbKeI25OmOOEIuKuB9EnkIlr6Mh3RTgBObIDEouS-4jpDc5emqxhtVT8KKzGjuPAI4mU45naqfcCLApna_8t6OjEHGkB7Eq-3lx6P9hE5vbkzWjPW5szpcCbMe87fQil7cjU6rJ_kc0lCUbujYuqyr24qxrQuJdKLvCLog7XCi228HN6T4Coe4X693VTlFFwGrxR2YnP7d0oHIxBoUgf9urAt2WUekCeNgYv9Zc364l3fuHvQr6kOzwYKBAmooDknO-iLuWbsGSH1R5x6OLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی میگه :
۱- موشک مستقیم خورد به خونه مجتبی
۲- مجتبی خودش هدف بوده
۳- زنش کشته شده!
اگه مجتبی هدف بوده و موشک خورده
به خونه، قطعا همون لحظه مجتبی کشته شده!
اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید
که دست اسرائیل (دست خدا) عیان شد
و خامنه‌ای جوان شد، ولی از قرار معلوم میخوان آروم آروم بگن که دست خدا، هر دو رو از زمین برداشت.
موشک خورده به خونه و زخمی شده  باشه :))</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJ06s1SQkPB1-tsRP_tyH_dtMhgEmV2HPdjWy-XoNmgkjmZOViw-ebc9r5g6b76x0VVJw0yfWsJ2PWWB_HbBs83Vs5n2XCSlxQ6-o0_uG8_k6wUPR7fkFy91sAj5O2utpoB-egDHzO6eOHd-821s3ywkh3A8nOXHWUIaF7xl6ekMrQ4N-HQXswxn1ySkvk9JM_-aHhMzTca4CuGr7st6GTsuqKFcEWbHTxCeSe9GCqIX0fal_DGw1e1_t2w2F7K2Jmzms9eu_0P52l7-30GPG-9QkHsFRpHgaMfkFXxFui0fY1hQ1CZYgaEJby-Ms_f_7s2zvfuxJGaaAJMVInVILg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=hFEnu1UoriN2fEBpItMdRE9zcG98DdLJ_J89wfDJQBPGFQG852l04FFADNUquj4gQu_VmrfWDAlisupJ14yFn_MTywFSdU1D7LDsfvFBEcS6rDDgpVzfS9a59ggcDIO1o3v3MUKPRSPCK6Fip2GzUiA8ryNlvI_D1ERp-ban7ho9zOz92b_FWNYEpiRh4rVoxBT4kNvle1edpn4CrDl2YzNlhaT3HfrPVE-E81C4IoMxYRC6LtybUsjY5bRQ-wEWiNcWXkotO3Sstp17aZ5pGA4oDlZymA9SI_ChIx79esOr47dOKy7cEGluk8KK1a8yQ0s0YXHP5aj-TWCA5YJDDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=hFEnu1UoriN2fEBpItMdRE9zcG98DdLJ_J89wfDJQBPGFQG852l04FFADNUquj4gQu_VmrfWDAlisupJ14yFn_MTywFSdU1D7LDsfvFBEcS6rDDgpVzfS9a59ggcDIO1o3v3MUKPRSPCK6Fip2GzUiA8ryNlvI_D1ERp-ban7ho9zOz92b_FWNYEpiRh4rVoxBT4kNvle1edpn4CrDl2YzNlhaT3HfrPVE-E81C4IoMxYRC6LtybUsjY5bRQ-wEWiNcWXkotO3Sstp17aZ5pGA4oDlZymA9SI_ChIx79esOr47dOKy7cEGluk8KK1a8yQ0s0YXHP5aj-TWCA5YJDDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.
جلوی دوربین‌ها وارد هواپیما شد،
اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!
نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=HnJVEEZLWJXiVtqZpOmB2dHU5YBIwB2UFPy2I8yynnsKZhwBltQBwebSUq98u81oAw_6Tvlum6DCi59iZB2eoy0mxF8HRonrbLeonPOx0oyQpbYWAtc7oLs6QBCXLoVlVbWKJ2OYk18Bxmrovtws2rhYNwWKVLXoCl-b1-8yUqdIJvc_gFmO7Cbuv2KiqTxIqdidJPVWS_F9S9RzBoEpBD_6vAKxchd87IA9lP8JmZC55n0_Hu1MJhPBigFZCCHQceNU6mOdNHZJVCjtbhUgHjgPB27GXWVdhR6cX7Ln49LFR2-ejbfxo9xUVakq8izerNLI2onbmgfBISV8jmEkNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=HnJVEEZLWJXiVtqZpOmB2dHU5YBIwB2UFPy2I8yynnsKZhwBltQBwebSUq98u81oAw_6Tvlum6DCi59iZB2eoy0mxF8HRonrbLeonPOx0oyQpbYWAtc7oLs6QBCXLoVlVbWKJ2OYk18Bxmrovtws2rhYNwWKVLXoCl-b1-8yUqdIJvc_gFmO7Cbuv2KiqTxIqdidJPVWS_F9S9RzBoEpBD_6vAKxchd87IA9lP8JmZC55n0_Hu1MJhPBigFZCCHQceNU6mOdNHZJVCjtbhUgHjgPB27GXWVdhR6cX7Ln49LFR2-ejbfxo9xUVakq8izerNLI2onbmgfBISV8jmEkNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون (نیروی شبه نظامی تحت کنترل سپاه ) در تجمع افغانستانی‌ها در ایران ؛
هر کسی گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frkIGB8EIbTyy_AoAtAuOlgYCpUPuLDdKgzo9ueQV-X2gU3TLWNw0dstxfxEalYyw6g7zsaLOYJI6cGt54td6Ui4YSJS1XjeKHbC4MMYUBjKJfWnqOV_Om2WJW1QWGln0Pm4heLLRqx4wIcKSIFfyYa-qUFDmXJxq56_Q7lxS3tW40qauo4fbJHzi4F0bZoXf3JfO7BsVMuKybo8FBAfij2-sLu_Oz1Gpoqt5kaMCzj2bmRBTHZOv82wBiN57old_r7xVpMY8qIG0236gl12lX0_ed9V0GYeV8ABvXS0jrwTjZGHMdKPncevhBnKR7EbcRkuIHtzkRIR_C4Ytn31Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s99c4fkx-8ns442-vAd8ISqLnRgk0b-b1pHDKD4m6w-k1z71L9OsKAKWLW6j6eT_yELShA48kB6AEP7Jhm-IJ8TdrsBe1iN2z_pTU6QyffuFRISSkMotiBRikzfMkPpgtWzE45Q4Yr84AGhP-KdCJlmxEC6PDyb0mwZvFI7yUEZTB-V6UP4_pagln9A-ppOBvP-Rvn7xW91cDvNqhoPAyhIgQ1WJ0MSKdBxO-IU_BbCA1_i-0rRmUM0-YxzLdWHeUuqiSTdtgZrTwK3kFID168xBtFyja2y35UH_deHLYkph1FqgmogN8jUAeDObY3-hNbLG278IlQ6nPuWhsjGSTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkCATwzYUlW333eHUi-oQMxbp-DpOhiCvs9NZZ3b6Ydv6uIrE9C-hJBbBv2504WLXCPsxr7EewWqFL1pUvuQg3BMttDFImHTB9zAQR9Uh7GDlyCNFMpQNw9WtEqh0vkBA2sZdHHMeVf_U0DfIIe6dc56EIQ0LTsvI7OoCar9NpH2szRo6tzSnogMxn_T5My4ad0rzlzUrcMoHvYaslTTeacDOW1YZLjfaWdFzTu2OgWc40fU0cNpls9y7Ve8WwBgEar6ZdOq11sLgsx0h7z7GoKs8QW0_IDBKwaP5VOan-mEm-C4kDmZl-3ZItGeAm0xmlgrxJJiCePEZk6vgh4Zgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=bVbcTqZI6RZ3IyiZ86YJw0WJ3gNuvC623PgOYeVGs2A_UDqtie2Tjoctx33MK1DJSHSfsxWeZR0Y0f-QiiQ9cvB_ZOn6B1xSYY7k2R2mY0sUuCWXFVehTZMT-TthS426b5k9Yl2b7pKXgn2FZD-F7fuCdHnVU9bKzvH7kaVMFicTFrgpuZQtjz-Li_zNz-K8Z4V6Zq_h48TygHklDTGgrmcV0zbdGEC3KxFrL8Z65NeXFOyQCQLHCQeWX-e1oYDPymTpB9o5itRtX5B8pm4t3YWoSavqQplOxGUFvv8OFYp3O5A7UgdPBcXMRFpDjgkzfsYUVrsuooNdTVw259gyeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=bVbcTqZI6RZ3IyiZ86YJw0WJ3gNuvC623PgOYeVGs2A_UDqtie2Tjoctx33MK1DJSHSfsxWeZR0Y0f-QiiQ9cvB_ZOn6B1xSYY7k2R2mY0sUuCWXFVehTZMT-TthS426b5k9Yl2b7pKXgn2FZD-F7fuCdHnVU9bKzvH7kaVMFicTFrgpuZQtjz-Li_zNz-K8Z4V6Zq_h48TygHklDTGgrmcV0zbdGEC3KxFrL8Z65NeXFOyQCQLHCQeWX-e1oYDPymTpB9o5itRtX5B8pm4t3YWoSavqQplOxGUFvv8OFYp3O5A7UgdPBcXMRFpDjgkzfsYUVrsuooNdTVw259gyeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل کوثری :
‏سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
‏سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود؛
‏وزیر دفاع با معاونینش در جلسه حاضر شد؛</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=nEzEBG912qeyU4A3DVGPYn-usjuYT2n-uLz2WZMOAQRgvtv6vIcotbMgTlgatwI5mI_s7rwecd3WOhEamAgeailQCs2dMtT_aHP3MYgVV1gSDzMk-pjdtqqSrnWhu3f-PXPZ7zxZgKksvyJcK7Pq3Nl8qfeUGDarjCgaTUyosW7NfKHcWhlXA6I13IcNQbidH3hGVS-Dffe3IfTb_QaaydsUwTm1sonawHINqIudlyVZzMuET3lFlmDTTd2HMC4JHyURdMDB3iWrfry7n_kBk8p6-IiinDUatQN7EcVbNaAosJK4cYplysftcbbjk295_flqBPdYBX3PMXwE-fNB1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=nEzEBG912qeyU4A3DVGPYn-usjuYT2n-uLz2WZMOAQRgvtv6vIcotbMgTlgatwI5mI_s7rwecd3WOhEamAgeailQCs2dMtT_aHP3MYgVV1gSDzMk-pjdtqqSrnWhu3f-PXPZ7zxZgKksvyJcK7Pq3Nl8qfeUGDarjCgaTUyosW7NfKHcWhlXA6I13IcNQbidH3hGVS-Dffe3IfTb_QaaydsUwTm1sonawHINqIudlyVZzMuET3lFlmDTTd2HMC4JHyURdMDB3iWrfry7n_kBk8p6-IiinDUatQN7EcVbNaAosJK4cYplysftcbbjk295_flqBPdYBX3PMXwE-fNB1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fW65fWfrpy0R-8f9zv6SBqKsCqEZvPzqEwIVhvTHV6jm4sKexqaCht1dfiE77t3OfCTdECVEtXGhbTJT_dl1xEsDufj1SBFkxLtqUh6AiedaYyWJDhbzyKw6VYF1LkNxjy1r1GaR865KU4CTwC3rXxOjDv8SzcCcmSMZPO3huwxAa9asLhQ_WrUUYu_OvWtTK-erDZEXjlpAxLMubAw50Q_anvun44jhruiVCNLpPlRhsWgs1WOiF_djI_s06E0fCP-Lvd7yi4wcYlhOQj-0tArfTXHJfegB6m_V8hpSfDeR6VvDbMg4ONt8BRDJZyYBvdFduqMuYWxJfPwstVzltA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQW_hYPeLThMeWu0ybZ-93OvLo4-tvri4YCC1lyV4IofPCImXjD97DG_ik8bMCt2AXasbe9CTmkqgoLeYjhqQcBrMsZGwYjsDNllBHqgmo8Tl5QfMDcGCYiKpIU1syaKCNL_W_9NExJynynkiri_drhkZH-0XPxlMZOdeCR92yGORW20JJ4yKMSOX1HBWE51l5-rg_QPJdKfGTX69OoTTHduSiXGnX7ykyDPBImYz9eueetkMUmjIf5k86-GKalyh9X4xqMnCO2KD0gfrbsHbcLy7oCnFo1EGbX1KBjCvwHnYw87UHmg4iLpZtPwkVsyNExEgMuhDe0GYTHTTdC1aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_wjGmNL1Xg8L0kAoWFcUI1KqEhCnZZHAwialXhq6U8SYKbvhWbox7F9PAoWQVlIwoAql0a8QFud87CREWOHbH4S0Brdg-IW33YCDg2jlJ1dX5fGW5cMIvk9fSAlXwnUSThIUjtXgxuQ-5VRVoD8AWLfuMrwX8a7pXGEubHXSpXL1vaB-5BfcBnUr-KAmdZVYm9X2ZrSfl6Vwr_IzdNKpBnZKZEBYqRbstHrFI6WZOI6GrOGrNPMoROEXKo3eDFmjZP_YY0bN27WFIV6JrVBMYhJ5zKykeZVlwZIwoP4qXF9ljXT3WVhhIhyp1bBjysT9SEC154J5rjXr21Apl63OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEG_NDmh1EnkUW6yFJbmtwhjHwpFvA_S5vK8vo38qmxIqZ_mqvFH9NZwW8w82Tjl34GigpPmzNB_qxjWie67CQQgGVcVhu5V-hcU9NX490q1hUhxMeBfvoqtwzZH1pWtMxXEqdAdYwqUZeq4ZQBqggPTOlpqL_fDcRWfyVFVLE-7dSdcwG4_FEFuS04qIqxqOsEVhPTaSyHUF0HNY2TIGm8Z5QDCz-MsQTIImwfKXijcE5iG5AOucYWNBMcnCHw-xMp6HYs8xwaD4MfQaOoNakxH1KVwwCftvVN0MBj8cHKDMAPUQc_9ZJ_Cr-7VlMGwguxej2b9uL34K9cgjonXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiXDGnviRBFk_fFDL0G8xjll5W4A5Ry_3Ids-EABy70EsP8FzgLIJgkDJrH3sUbmL1M9Obj2R01ITcQuENd8Jtr-mzEanzPwqcuL6rMzk-X5sTSTv_qkxw7fXQTirRMHgpAENlSCvrvoNjBTCTNOvawmw1-1nX1uk7EyinH0wXVv3tM2_ChSFmiosSCswLeAJFQ8WZSBETdLlO9LBSc6LvHvcwzjkz9sk0j1dxBXe4DR8C7p5fktU23-BPs3C9g79OC5kG_vFDdl41yccGtC7U_CJHBnMUyFRlVVmFbO-91J2U5sX0cKoKRXBImCwEm1aSlr6oxG8S9c6k-t5VTwOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JMFBL9et_ZEgaUXaeFp_l3WrTxIQvCCdo_TyFNIZs12iNN8WjjpyPeOCnec8qJdy-td3IixZransIbERpTlAiPyx0GD45WZHCwAy_R8YEHwMlXdEjHDKbOqfJjibqya0Tq46pTnigB9P1MUldPDYZIerqxU_W8vSCAMZgGuooEBdnNPeOoJg61-HwML2kwGWCTF72g-6IhfZJORBLU6raRidZ4Lgv4-_n6PgEAkClFSMpHFgAwuwidNIJ25D5JBdcnZRu1JgXC1u-1iu_N2zt9CT22u84fZGvMWIaJZru5PUsnfCRv0KLTxaHnYQb9y9OikYhm1S5ynS1lM0uJHOAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQ8AzHLhL5PMWTHQwstQIQCxX4l8ZrKTKDNLfPiVE_9-Tu3STMWW3DzffKsFiaGtwCe37DfY-ZhqeQ2u3rwW94rOb1lSEkT52ROG7yJQjRi8LaGxpByJEG_PxbQ1-xo8MM5rta1nGLDR0gE9yE5Rw1XlBARxTOJoYqQbdBcCOB5HYMWF0XRhQoYBxd9npEBoyaettnKC8ETO7wd0zMfMiBcqiWVG3rGMfH0enz1-QN_WClD6ZDUd28sCrEhXgbwG9Ieye7SEFP-Md0v6KzAcJQIsw0XcIjvF9gEOnR762l6I98W8gGVy4faRf1_iAaGyZMMTrx9R2RskH46vSEAAhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YNhSYrWKchNk_-FB96UqPOlhLJRXhZAOgCStPWySMka6u967ihg4e3QbNEx2K50-JzPJXsDiaBoCJvKQVFr6X8Y-ZKUnUumF27IYPKdjmfFHXdpBJeMXFC_Lmn7YL3TfZkfPTS-K6e7F5zzH6hS8eOfOZjIPpYlm-3fruALmFilyxd_vE5gZKmhNXHBG-atx_lMKUVqPxLjtoVbmqC2oqXXsf8pCa77kCYEvT8VZnSq7UErKQRb_QP0-rX2x6Eh1VGOjnpBJ1MHXLqLrApU9F0DuE9yFwPENUxmN4Vlh1rWPN53WzDTvfVtTQSTDDGiIXA2X4vD-dw1oNlyjl69r8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیرین مدرسه ساز در ایران،  ۶۲٪ از مسئولیت ساخت و ساز مدرسه  رو به عهده گرفتند. حدود هزار مدرسه.  فرض بگیریم همه اینها مدارس ۶ کلاسه هستند (برخی ها فقط ۲ کلاسه هستند)  اگه هر مدرسه ۶ کلاسه حدود ۱۲ میلیارد تومن هزینه داشته باشه، هزار تا از این مدرسه‌ها میشه…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_dLzMFx8P-qI7IBN8KuNiDRuoA95WciGDHV8Nezc7I9KLHjvQC0Se0Ahsk9YYdKd5QuZp498ngZzRD5gSPAMrfsjKHyDv8nOOr5x8oa59GyEaj1YE19gJOgiG4nJZrxXuB9Dmq4_8YSZUJScX4F5fzZsWYGdFFGC8RYQ9VBWcxOMG3si0Cf_7S-Dsp_3RtoqQ9B1zLzZOd7Fi9m5fjmTtV0iSLxQy3rgoX8ac-p52JmaGUztmrohyxK_ErOM_-KnqbaGhDtZamRKoR3e789Zkc6MS5RXYaH0WIeAHSr6MM2nXyxFJxYxV5m7kf6s9uDRCHq5bIK6_5XwsbakLkpHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا این متن با دقت بخونید و قضاوت کنید:    پدر یک خانواده،  نیمی از درآمدش رو صرف مواد مخدر میکنه،  موضوعی که باعث فشار  و فقر در داخل خونه شده.  مادر خانواده ، چون بعد از اجاره و….  پولی براش نمی‌مونه، معمولا از بقیه کمک میگیره که پول پیاز و سیب زمینی و…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6523" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">لطفا این متن با دقت بخونید
و قضاوت کنید:
پدر یک خانواده،
نیمی از درآمدش رو صرف مواد مخدر میکنه،
موضوعی که باعث فشار
و فقر در داخل خونه شده.
مادر خانواده ، چون بعد از اجاره و….
پولی براش نمی‌مونه،
معمولا از بقیه کمک میگیره
که پول پیاز و سیب زمینی و قبض آب و برق رو بده  برای سیر کردم شکم بچه‌ها و…..
هر روز هم دعواست که اگه پدر اعتیاد رو ترک کنه، هم پول بیشتری در خونه می‌مونه، هم کار آبرودارتری پیدا میکنه و پول بیشتری در میاره،
هم خانواده از این فشار و تلخی.
🔺
حالا سوال : به نظر شما افرادی
که به این خانم کمک می‌کنند، دارند کار خیر می‌کنند در سیر کردن شکم این بچه‌ها، یا دارند مسئولیت رو از دوش پدر بر میدارن،
و اون هم با فراغ بال بیشتر، با شنیدن غرهای کمتر، پول خرج اعتیادش میکنه
و در واقع کمک هست به پدر ناشایست؟</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6522" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=jxtxHph2GBnzs9Vucr4XbX1HX1KpdnGK67aVcRkGyU1CP7QaSbRdbB29twv-KYqhtGzp1viN9cQ-8wgXcfkygduGyHRfEcMTWEFr13B_iItM8Fa2HoDXlfnXmgZtPR6nJyUCP_xAFZUq3DrNKeHlP7ImIyyAGKGSzLLB5TU6K7mC3Te_kEKoqhKzJBGp-IEl-iOeDp1ihWkFRen5XMsh6TCUr7TVO_8TfIztqUuUYfi7fBD2Rho5e2oM8N1SzOUY--a1hAv8w-YVKF3-nV48quPvdQJEBEV0rfw_KnpkI2uPzi8ICeC7sGuSexqEMmkTb5sYheK_y3YaQPjJCPcewIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=jxtxHph2GBnzs9Vucr4XbX1HX1KpdnGK67aVcRkGyU1CP7QaSbRdbB29twv-KYqhtGzp1viN9cQ-8wgXcfkygduGyHRfEcMTWEFr13B_iItM8Fa2HoDXlfnXmgZtPR6nJyUCP_xAFZUq3DrNKeHlP7ImIyyAGKGSzLLB5TU6K7mC3Te_kEKoqhKzJBGp-IEl-iOeDp1ihWkFRen5XMsh6TCUr7TVO_8TfIztqUuUYfi7fBD2Rho5e2oM8N1SzOUY--a1hAv8w-YVKF3-nV48quPvdQJEBEV0rfw_KnpkI2uPzi8ICeC7sGuSexqEMmkTb5sYheK_y3YaQPjJCPcewIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، مرداد ۹۷:
‏همه ما انتظار داشتیم ایران درخواست ۵۰ درصد بکند. قانونی هم بود. اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین ۵ کشور، یعنی کمتر از ۲۰درصد
‏برای ما عجیب‌وغریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند
‏این برای بقیه کشورها مثل هدیه الهی بود. از خوشحالی نمی‌دانستند چکار کنند</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhXAt4oRCjsX0kdr88C0PFvHCz7hvL6MFJtmvSaivZ8WkbJ3vktwhWlE7h4muoATNSNuaMohm5I0SvX2kSN6E4g8xy96U1BL8Py8jGby27dMCFOzBTDLAKz34JhUg2xgR2kXuIS6vrnrBXCoRf_cisSt7yRWgobp_UGRL_jHBgVQBEgfQxPReszvIVTHdMPEBMZMO7uM1xASp65V97E65_4mFPNJweAhJjjkb34lXnnrky9ON9r_pyaDabihUxRYvPa0WsqITCN4Te13hhwcagOgkIe4TcUBURjJPdJa8uc15XlQlQVrlL1h3G_YB4oC2g44CO3o_SPxR3hhjM1byg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPljt30LocCTuBozb47nY3uYjI1vBqh4FEKow73VAWtVGXeXLROV8yHkW7iPiWRYZa-GcsO15nQAvnKG_hIMZH05VAGjGn6oqasMGEiaInE71IIwY69CuqmpRNoSxg0Kkt2YMS6Tvf7Fg0W-MWg9zAJYvSnCOdhF62hAlmd-8cQSWGQs5rEk0WA_8ils0kecpgO7eW8Iz3BluQyxNVRzxB93ZPE38lC5C11MRupRKj8B7dLgYWDQ2s1ci9lm-JwvKkG8gqX1H7A6GB_1B0l9i1KuLVRMWJu1EqWV1vYCfDMe_piayjs0MoaFDbsW23FXxKUTreqmRSOwbqo09Yonhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«حمله‌ای گسترده در راه است…
نه، صبر کنید، می‌خواهند مذاکره کنند.»
این یعنی «دیپلماسی نمایشی»
که مدام در حال تکرار است.
استفاده از زورگویی، وعده‌های شکسته
و اخبار جعلی به‌عنوان ابزار فشار،
راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید.  ما به نمایش‌های بیشتری نیاز نداریم.
- فهمیدن حمله به کشتی‌ها و زدن زیر تفاهم‌نامه نمی‌تونه براشون دستاوردی داشته باشه ، از ترامپ میخوان که مذاکره کنند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6519" target="_blank">📅 22:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5iWFysM5Mz1CHXM02n7JbkPsi0G807Rxtyri1SHHxiZcc8YQfBCPSh5NN-8oLqvwYSUYwlZsIO23JwYm8p9xLRsB7zfRqeyK6GZ6QD_GzhBp4VxtsJVFEL1hs8_YTMdEwFnwLwEpWB9T-sHb2jnVjINQp_ki6jYOjBU-XKBakLGgx3BVwkl-8bNT0ElltLy774awwHH_d8-VGM5bHO6bdT7hH_NJvYukyCCA-ORcQ9hhgwQ2VSQeifyQ6vfTdfrYo91ERdtEgJBoDAUXebHsWFbSH3WNlds1BtbwwJukWANoQRvGfMShxcgOYxqHLxjziexXprvB1OMwx1ianb5sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPtHJqBDoRULIU7SNI4Wg5Q7zZigsYCkxwmoH1ncvwP686WKB12mgtCwI6oI14MS6xuiczpZAvbBZUil4m9fzQlZIUvAEZjYtWPDRVHa6vX88Cu5BjNsU3WvHd1HNoDFRBhS7uKZBBnJ2wW0nvPIsJBn3Yc3qQsg1hScaWkdSPoG9cp2HW3nT_6jFKLqWKkri7LqNaQMtZqocOlkNRQcOc_hVS5W2zHN1Mv4gpI1fJg62sh4ZGrpMmjoXdb8NNitHJSegNHDTJDjH_2WhDbn96BcpOTi7dXfEUytagXPEuTalKCO80-Q0vcWKtbjmJRM5gURI7Oq-APltg67lmB7Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3pPEdQwIdw8aCzHAsij4Wu7UyYWnmtR-v-QVaJ_X4m4t6fCDb7sDwvZurhjQhMY_HqSU-XlJPaIjypo39qAZNx70zfvHu6LzftzMnxlnPa93kjL6_YU71iuf9gzH3i5CkU7_qBu0arRIwC86n1L_1yv3VvA01_N1JONFp7QE6imjJLmuAwLUuwhczAL_4gub8bG8cURfMuW41lP2o1gWv2jnyJ1AAXctahdf85gF42Z0Acb7GiBilzC8j9Nk26jfM-1Dti9RPanuDUppp-FEVzeF2DSJzAsSJ7S7sinU4_FGd1IuFXfQwQGIu9nEasFQI0rEwfB_kwsTBqSxlNAag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lGD_IQzomu06u_WtsBksleqDUq10Eqy-aqZ6s2pu0DtiaDscwa5_V1-h23bU3OojQgXU9tys6-BBAIL187LxwrsO0YoD3bj3ztNzDxhaZiNEUR33Rq1dQ3m7jCuRx-erTcKO39cIBED-DxUJomeKUIv64k21r8GsNJQBWHFnUnufL1METl3qEJDikHD6fY1hdbJ-NbF3KGDjWxwQ-tqCOkH0zfAPzz4EV0Gbh5FXmklesKCtfQwqra97gvXkt_6WsB-pQh6LSTWmJR300ZE0Wk-BwjurwaOrIklqmH5F23QfhvYgalP6zJK73ehyTGBRU0CSEcR_vOI9slMDK2FoKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dS7n43ynK61I7ez4jkaFDfcrE5bMYouOmmJBZ9k7XlWGUAKPhwqsRM2wAvO1ajD9hJi_rNaS2cbvOADtrjsVMsxLfqICwdbWlI36Jyd08IkqApdl6N_6IQKkwx493xLrW0RfjSas-UPyk1yafG2Xj5YN2hpSQvuySCJ7zjOdnzSUCVeCECQoBJAsYCInSrwx2h3shS9GZMfO7DfPcmEjHjmWXjoTn-k6W5ztJSuA4OOjqnR3EXU59tpFioHEMusGqfOhLL_j_mj2mtx2ZW2gt3n8VopQgea5BELebwogCkzk77PoJ2LESE5WEcbbn3scfFXuw6EhwYRgGp9sf2tfvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=YzV_CgMMAu57A_GCmVTq58j8QznSimaOSF6UTBJ71e0IjGoiqwYvFB_1Arej3uWSh3CciXbI3fHr7hLEharYzKwS0vTQvMfgEbgYQ0-oF5wJEbwIc8CTtqy1URB5fnZY2C1xdgGdVZe0JepicJWckK7B603M6otc-Y6uBvN2f74Sd64OTQXpkPwmAsOMrKgocYmYBLjy-OcYa4sG-v_y2Pg5u-LDsAw5ifLOB8OqvNGXlWDCfNnuu1yhb4tEf1XceKec-BJp_IXff1OE1kRhBuKwoajw_gj3xHxSHttmZ-F-r7beruPupbhEKbYGVuNZ1OWJ9_pG_XrirwLg3x5Gmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=YzV_CgMMAu57A_GCmVTq58j8QznSimaOSF6UTBJ71e0IjGoiqwYvFB_1Arej3uWSh3CciXbI3fHr7hLEharYzKwS0vTQvMfgEbgYQ0-oF5wJEbwIc8CTtqy1URB5fnZY2C1xdgGdVZe0JepicJWckK7B603M6otc-Y6uBvN2f74Sd64OTQXpkPwmAsOMrKgocYmYBLjy-OcYa4sG-v_y2Pg5u-LDsAw5ifLOB8OqvNGXlWDCfNnuu1yhb4tEf1XceKec-BJp_IXff1OE1kRhBuKwoajw_gj3xHxSHttmZ-F-r7beruPupbhEKbYGVuNZ1OWJ9_pG_XrirwLg3x5Gmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.
اینها دنبال «اتفاق مبارک» افزایش قیمت
نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.
اساسا با همین منظور شروع به حمله
به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6512" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.   خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.   او همچنین با اشاره به اعتراض‌ها…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=E3sHn9y5RXAsd9HYLTThSXv56L3Gpb1ju-UZqKY7CYbtMBxDulRQfnDOne0vBPD18LTWxsmsuStPCgy1oz5SU_iQofNX6zKewejPubCnw62W7RDh5xLvLOB0SWSCmp4hVcjI4rt6vxN3L4mpthalcAF2TR7mxEsu8BRPlklas4QcoMQip0KkdxOHbuLGYQ9T0MOumbylOwk2a00_s3DI7MgJQg5SpGkWArp_uZtTQdG4xtHf90dNUlLqcCA3YM1EtrI6sV7BYge4WIOrWyMTlDpW0y_FfQb0Qo96gUSDR2XvKWvJKdh8YikAIqXU0RgBwlNg6THfSoN8If73dJoHAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=E3sHn9y5RXAsd9HYLTThSXv56L3Gpb1ju-UZqKY7CYbtMBxDulRQfnDOne0vBPD18LTWxsmsuStPCgy1oz5SU_iQofNX6zKewejPubCnw62W7RDh5xLvLOB0SWSCmp4hVcjI4rt6vxN3L4mpthalcAF2TR7mxEsu8BRPlklas4QcoMQip0KkdxOHbuLGYQ9T0MOumbylOwk2a00_s3DI7MgJQg5SpGkWArp_uZtTQdG4xtHf90dNUlLqcCA3YM1EtrI6sV7BYge4WIOrWyMTlDpW0y_FfQb0Qo96gUSDR2XvKWvJKdh8YikAIqXU0RgBwlNg6THfSoN8If73dJoHAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.
خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.
او همچنین با اشاره به اعتراض‌ها و تجمع‌های خیابانی گفت دولت مسعود پزشکیان به پایان دوره خود نخواهد رسید.
@iranintltv</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XO_31-GffYxRHysHEluPKiLTRGIXcmnPXKNmEhQnlXVWhr12MGd36-BCY-kqdqJacwwIlcZ38T2cFhEL-xqo3VXEmPU5NyLnR-nsdaklS7OPfOMcTIpLdNVddp67Jtti_4xJYgdqSWIK7inSGouh5z1Qf3mdDeKDKTZij8R1Kvw_5cQsabbyY38Mx63CAzx4C7qUnTJ15iITPi7wkE6kQ79WqEm_lWKqy6D20oasAvNwVn6_AXPA8wtdaw_TTrBSgXiWa0QgKUKAns3AhegzbZOAGNHV3GhB3OBq7IzgoDIlFPW_9lstqhpMibF95aFKt-PaRvhIKH33Gfua3XiMFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akNzCn7sD5Ybr8YDJmFs9yeeX2ZfsNHIXp6Zp2gCELY8gDRpJvilKHSQneLbba9mBhMKyLoKkRxavSiOu7bqiDXQ-8TCct3svt3IQePYpX8xQJK0f3JgzfXUZ-ltVQ-QnKNW0hywiS-rZcYtEzp4b33EiW2KL5Owv5gXEfDf8eWSedHurYFS8hBzky9wsL7-SgkK9ypPNbILieh_q1K272Ij86Q5_c2oSjoZTnQbZEneRXB-mycefz6wKu7eL5jm8mDOgpZra21mNp8xn5F75pxvJOsN85Gwl5mG7PoXg0E3MWDK_UkO7B0bUVljxFlet2AggSwYxhjt1V0vj9OXxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=HU9bEkythbfIvoRSpW11wa1m1xsGLyPMmUbgO1a7bV7xH1p7q1snp2IHZxgL6M9Ht4vYxALImpQningKlgNRUVDgjMkfQpY_2HUVE5EYbO_2DlR1DYIUJDXYExCxVh13KYX-Awnr0yxyDAxdEi7StLTrogJ86Jf7fKWfYtj4GjC5Z9hmzLj5aoYdQnJO_8HE6_wyKhsHXghQsqfS_q_VSyJrNJ2Ytl1Cwlorj_ZyWM49knWyUda7y7wg48FiG-ENIKJhhPO8uLFdyi2EcmTBGlen_adWkYQ1Pdw05tfnHJQ9oVPddzB_11anDf7r9Q8Ct3avq4_0Hl9WMr1IRIlQ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=HU9bEkythbfIvoRSpW11wa1m1xsGLyPMmUbgO1a7bV7xH1p7q1snp2IHZxgL6M9Ht4vYxALImpQningKlgNRUVDgjMkfQpY_2HUVE5EYbO_2DlR1DYIUJDXYExCxVh13KYX-Awnr0yxyDAxdEi7StLTrogJ86Jf7fKWfYtj4GjC5Z9hmzLj5aoYdQnJO_8HE6_wyKhsHXghQsqfS_q_VSyJrNJ2Ytl1Cwlorj_ZyWM49knWyUda7y7wg48FiG-ENIKJhhPO8uLFdyi2EcmTBGlen_adWkYQ1Pdw05tfnHJQ9oVPddzB_11anDf7r9Q8Ct3avq4_0Hl9WMr1IRIlQ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!
که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده
و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSIoJfpzgdVsov4-bRYLxhnQn2UfRKvQ25n0HeOrKvMo5qASWKnVey9CUswJZgLDf4QToXpAiDb9MrzwTIsNYHHmo3Sl1LEZAcsx_rscC-7TdIDv1tHa1PzUNC_jPJbnk5_UfCbJ4DSpjE9JCaPNlwBzkRHpzse6-Ftzx6kEPjpB1a5Q0HOJO8aBH1fvLvg41HCOPSdr9JxgKOh2zD8CmNFikqnyvQmE9StFSCCzJy6ij-2Yt7naNPFWKn09_hEHeWo2QIaYHmcx4YWXI3b_wFl5A1GTspZs69mYZQU9fR8uHx4yRZtqsWSqOLaN-dKshcpvrxUQ70C7NTzIekiECA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBBCPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTsF_qR_EaeDUrbAhuZlPbn8st7yiv-mUCq1rXPzNcfk_EETKQjcw4Livwfy9vc3DAPRdX-jeOGUbVxTsEj1gjwIxhThIHB3HCyhxKRjINRVlzrmlQteAEZfqxYCbsiwaFL6cxg6l0flfnmv-nSf6MMv2rNAoapiiEYglio-iKyIMGR84ctjPgzk4xbnY0AX_hWuG3ZfV_rzV9A-76DV4OsV9DT4rOx_3w8F858soevJlcMYNz7xIVDLLIrjKS-2VJ7NEDcf5iUTEuzWWU9F06G8_5KAU4tEP1JQcXvFSvI_ANjeUJkYWbKiD2_rJmNPBzbOhvVRqAOzXwWtItargw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔻
سازمان عملیات تجارت دریایی بریتانیا می‌گوید یک گزارش باتاخیر از یک کشتی در فاصله ۹ مایل دریایی (تقریبا ۱۶ کیلومتر) از بندر «مخا» در یمن دریافت کرده است.
بنابر این گزارش، یک شهپاد به این کشتی در دریای سرخ برخورد کرد و باعث آتش‌سوزی شد اما خدمه و کارکنان همگی سالم هستند و نجات یافته‌اند.
به گفته این سازمان این کشتی اکنون غرق شده است.
جزئیات بیشتری منتشر نشده است. ساعاتی پیش حوثی‌های یمن که همسو با ایران هستند، اعلام کردند که با موشک بالستیک به یک نفتکش سعودی در دریای سرخ حمله کرده‌اند.
این هشتمین شناوری بود که از زمان آغاز محاصره دریایی علیه عربستان سعودی هدف قرار گرفته است.
سخنگوی نظامی حوثی‌ها به زمان حمله اشاره نکرد.
📷
Getty
@BBCPersian</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29785e012.mp4?token=hE38e42wBuRz9GnoXVT3iOOKisd5OuablSnijocQcralpuQAjm3LW0_JPa2LNE7m3lcyYGI99NobcGCSXNQi3gnruCMINklz_9-2FrIZFlOevYUAfkLhE9VoC5yVObNNwNfRCOdlIUN70dOdX4H_bT9X4rEZBPbJWAjg3iOF6Yp3eqWwPw2qeEsUb1IiHhFmjyrib57zaFIEV_JU6B5jbVP-qLsvcLgJy1rR8fIgY5TvG5AHsEWtCe8G-0bjmRQlrSip2ZADfe63GpR22b3oB_jFhAl86kytoR27wirIZJEVcKkFczu3J5R9WYmUFkFmwzilO7mx94ld6k5P-vzR6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29785e012.mp4?token=hE38e42wBuRz9GnoXVT3iOOKisd5OuablSnijocQcralpuQAjm3LW0_JPa2LNE7m3lcyYGI99NobcGCSXNQi3gnruCMINklz_9-2FrIZFlOevYUAfkLhE9VoC5yVObNNwNfRCOdlIUN70dOdX4H_bT9X4rEZBPbJWAjg3iOF6Yp3eqWwPw2qeEsUb1IiHhFmjyrib57zaFIEV_JU6B5jbVP-qLsvcLgJy1rR8fIgY5TvG5AHsEWtCe8G-0bjmRQlrSip2ZADfe63GpR22b3oB_jFhAl86kytoR27wirIZJEVcKkFczu3J5R9WYmUFkFmwzilO7mx94ld6k5P-vzR6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اثر یک انفجار در جنوب لبنان ۲ سرباز ارتش اسرائیل کشته و ۷ تن زخمی شدند،
ارتش اسرائیل دست به حملات توپخانه‌ای زد
و سپس دستور تخلیه فوری روستای المنصورن را صادر کرد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=uw66OPHpF7ji_NWA4uczEWJVLYjkO5pMIQHs0_wy7H8Q4OKQA9nKuBV_yVZrQTOCLU-_HniYBOzPTrTOWOjuxWoWiAzDmB1ZY0S_Bd7ro7vQAMe9Axy8F72G84QyL6te25KfdH_5EdXfX2o6ejY5nJN2Q8Y6L0dA_ogc4_6N2jFj4h3gGgjHi2ce0z4YXGnFW3E-Cyo0KOwU_IZdpPVgYrrpX-jGe5ESBlRDA4uwm8pd3w93hP2ggKs5kPYZCNF7_GBQBufucSIU23EeA3Js7N5eb2qOGdtBbc18KUYhJQ6g0PNMLE_byH293ul4SuS7qFHNbC69iN250oQ5PSAyBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=uw66OPHpF7ji_NWA4uczEWJVLYjkO5pMIQHs0_wy7H8Q4OKQA9nKuBV_yVZrQTOCLU-_HniYBOzPTrTOWOjuxWoWiAzDmB1ZY0S_Bd7ro7vQAMe9Axy8F72G84QyL6te25KfdH_5EdXfX2o6ejY5nJN2Q8Y6L0dA_ogc4_6N2jFj4h3gGgjHi2ce0z4YXGnFW3E-Cyo0KOwU_IZdpPVgYrrpX-jGe5ESBlRDA4uwm8pd3w93hP2ggKs5kPYZCNF7_GBQBufucSIU23EeA3Js7N5eb2qOGdtBbc18KUYhJQ6g0PNMLE_byH293ul4SuS7qFHNbC69iN250oQ5PSAyBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی منطقی بود!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=myx9UesId6ylcnV76WqaLl4PrScmK9gyj8Ct5cUsoRH34Dx-ozTqTwYic92FQqMafckh9PK7nIzaJyhyZ_biB1JAcVxGHDEzR-vNRUf4E3AlgcDoSxBbV_hYaFr3QWYFBOBJwwTJUP2rm9YMlks29b2_AvU8U0qVNO0a0vEm9F-zXISAOU63gwiPDYmaGgPtB67Z3-qFjorTCTeefLYFTWQ6bfzzoN_ilVUS42Pqn0VSYjEG8c4uTjp_Oh_ypC1hKDk3EyckBg-n-shPP25ttwRhJzJtlvxZCJWgR1TgKOAPbvA1jonCzFFva1JZVcqfHGXIamVdt64EiHShv2bxeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=myx9UesId6ylcnV76WqaLl4PrScmK9gyj8Ct5cUsoRH34Dx-ozTqTwYic92FQqMafckh9PK7nIzaJyhyZ_biB1JAcVxGHDEzR-vNRUf4E3AlgcDoSxBbV_hYaFr3QWYFBOBJwwTJUP2rm9YMlks29b2_AvU8U0qVNO0a0vEm9F-zXISAOU63gwiPDYmaGgPtB67Z3-qFjorTCTeefLYFTWQ6bfzzoN_ilVUS42Pqn0VSYjEG8c4uTjp_Oh_ypC1hKDk3EyckBg-n-shPP25ttwRhJzJtlvxZCJWgR1TgKOAPbvA1jonCzFFva1JZVcqfHGXIamVdt64EiHShv2bxeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWgObpXROjZNcf5nanqyzAj0DJ_mjP1q-eAe1QJlF0s-C-Sd26QdljJfff6WfBKf0D_ohNmB3BSdYlBorfu19i9diro-BDuvZSJidrnjoxlmRJGXWoDhlYq6kw7Ujt9s98xk7TARK-t7LauaGru5frVUkYi3n5x1MpOEAQeytfzUWlZYxmQAKLpWI722S6ft_G1JKxW7b4kPzUKNSyv1cqkUofVdcIczSuR5uii69ofmJ8xRAnPCblmobcF0Gjn8fCgWI1VTCwVjBmdIDanZNELIyaZb-427BMbL5pAN8kP7io6P4ZyaMLb_DvGtm3multSrKhz_iQyQGODHCorTGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSwlE41xiR5U1KjAmAizE3q2MpQQeQJ4aDsUBx6JmPHyW6soJsxO-9zZJSWlRctWQKQKARd57tdmIafiu5Kv38YY4N4e7TsXdoM5OCYAil2ga6E-rokANcg6287UHlCCLNbEM92DEhCzoNwcTWrWtevSAGEWYDD02iVp2dvg4YLWsncj1X2VvJZ95bz8yhPsvovNC1pUrOvsfDDtrebdWXPlWjgSUaq1K1xnlunFmI_MOsS-x-J9iv13XWUraoMTy3USXyvERwyiO93sIAHFaTLA0v8RaE5ZPfmfkvgNhjQ7OjV8g42npLaw4imufHDMRN5UebpsDV2mVqhLgh6I5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ooh8hVYlytdD0I77Z20n180EoN3rPWNCsGqN5T7t_PSiNPL_UsQrKQV3n1NWzY0IAQOI4AeM6V745MHm_FysHXHPcd6Wac8wYu7_49sTvpcqb1bpeAr-90KpqTriUtEc_asjXSLq54XWuEwhg89hCrXbVFqBB1SleK1cUkV8WVcT8dSMpBNGgywfo-pXoFhlMvSrWLTWXbw_OBILmp39-h5TBL8QE230-OiudBVO57Dw6NBzUjxszpX2y0CtAnf0Eo15Tdm9do1wS5og9QTMLiz6is_FR9kU7GzKLeQSyssy8EPcV0H7qHb0rRR1U6OSRvPlPdIWayuxM6kvXFD-2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=j-xcq_ydvWr8HvDveEPukX_oRTPZ9ZsDo4I7ZFTcUVJ6J-oTHdQ1QRJChjfEMOERW9BNuFHpfR-7KWo6hm1iPC4PE3h1AesrVg48pfVToVVj62lfF7xfVqUVFwEUT58DnF0XPz1GknnMBOj7s6xMHI-o3KC0pwTTIpgebNVHiQyUyu5enNFkrP1pT10T4gHgz9Pea4r7EDgtE9-nyTZpGBuK2XO-9s2xbQ8x9_j2jdmN4Wd8uPjjuLlER5dr86UJdZByLPdmo8QLfR5luTtIsyzscCFd4McI0XGrDOQ0XwuO-AvE_PPPPxtQmUDc7sCWvscIftpa3d143YUlwJpAYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=j-xcq_ydvWr8HvDveEPukX_oRTPZ9ZsDo4I7ZFTcUVJ6J-oTHdQ1QRJChjfEMOERW9BNuFHpfR-7KWo6hm1iPC4PE3h1AesrVg48pfVToVVj62lfF7xfVqUVFwEUT58DnF0XPz1GknnMBOj7s6xMHI-o3KC0pwTTIpgebNVHiQyUyu5enNFkrP1pT10T4gHgz9Pea4r7EDgtE9-nyTZpGBuK2XO-9s2xbQ8x9_j2jdmN4Wd8uPjjuLlER5dr86UJdZByLPdmo8QLfR5luTtIsyzscCFd4McI0XGrDOQ0XwuO-AvE_PPPPxtQmUDc7sCWvscIftpa3d143YUlwJpAYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم. می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر
همه مردم برای ایران سختی‌ها را تحمل می‌کنند!
[تحمل نکنند هم یا زندان یا کشته میشن]
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.»
اونهایی که به قول خودش بین ۳ هزار نفر رو کشتن، نامرد و وطن فروش نیستن، کسانی که به کشتار و ظلم معترض هستند، نامردن!!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">جزئیات تازه از طرح تغییر رژیم ایران؛ قرار بود کردها «زیر پرچم شیروخورشید پیشروی کنند»
🔸
یک روزنامه‌نگار سرشناس اسرائیلی در گزارشی تازه نوشته که هدف حقیقی این کشور از جنگ ۴۰روزه با جمهوری اسلامی ایران، تغییر رژیم در تهران بود نه صرفاً نابودی برنامه هسته‌ای و موشکی‌اش.
🔸
نداو ایال مدعی است که ساقط کردن جمهوری اسلامی در حالی به‌عنوان هدف اصلی تعیین شده بود که نقشه راه حقیقی برای عملی کردن آن ترسیم نشده بود؛ تناسب این هدف با امکاناتی که اسرائیل در اختیار داشت به‌طور عمیق بررسی نشد، دولت بنیامین نتانیاهو هشدارهای ارتش این کشور در مورد مخاطرات این طرح را نادیده گرفت و به عواقب آن، مانند آسیب به جایگاه اسرائیل نزد آمریکا، فکر نکرده بود.
🔸
این روزنامه‌نگار در گزارشی که روز ۹ مرداد در مجلهٔ ضمیمه آخر هفتهٔ روزنامهٔ «یدیعوت آحرونوت» منتشر شد، جزئیاتی را از مباحثات کابینهٔ اسرائیل و اختلاف‌نظرها در میان مقامات ارشد سیاسی، اطلاعاتی و نظامی این کشور پیش و پس از جنگ‌های اخیر اسرائیل با ایران ارائه داده که خود آن را «اطلاعات تازه» خوانده است.
🔸
گزارش «رؤیاهای بزرگ؛ افشاگری‌های تازه دربارهٔ طرح تغییر رژیم ایران»، نتیجهٔ «یک تحقیق جامع» نداو ایال بر اساس گفت‌وگوهایش با ده منبع نظامی و سیاسی اسرائیل بوده است.
🔸
این روزنامه‌نگار مدعی است که تلاش او تصویری دقیق‌تر از پشت‌پرده‌ها در بالاترین سطوح امنیتی و سیاسی اسرائیل ترسیم می‌کند؛ فراتر از ادعاهای پیشین که دو روزنامهٔ «نیویورک‌تایمز» و «هاآرتص» در ماه‌های گذشته در خصوص تلاش دولت اسرائیل برای تغییر رژیم در ایران و جلب همکاری محمود احمدی‌نژاد، رئیس‌جمهور پیشین، به‌عنوان یک گزینهٔ رهبری منتشر کرده بودند و به‌شدت بحث‌برانگیز شد.
🔸
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از بین بردن برنامهٔ هسته‌ای و مهار توان موشکی ایران را هدف‌های اول و دوم جنگ ۴۰ روزه اعلام کرده بود.
🔸
نتانیاهو اما از آغاز کار پنهان نکرد که هدف سوم جنگ هم فراهم کردن شرایطی برای مردم ایران است که بتوانند کار حکومت جمهوری اسلامی را یکسره کرده و اسرائیل نیز از وجود چنین رژیمی که نابودی این کشور را عملاً دنبال کرده و با تشکیل گروه‌های نیابتی در محور موسوم به «مقاومت» در اطراف اسرائیل «حلقه آتش» به پا کرده، رهایی یابد.
🔸
نداو ایال گزارش خود را حول این ادعا نوشته که «تغییر رژیم ایران» هدف واقعی جنگ بود، نه یک خواسته فرعی یا شعاری تبلیغاتی.
🔸
به نوشتهٔ او، چنین هدفی قرار بود بر اختلاف‌نظرها دربارهٔ ماهیت نهایی جنگ با ایران در میان مقام‌های اسرائیلی نقطه پایان بگذارد، در حالی که برخی از مقامات و نهادها همچنان خواهان محدود کردن جنگ به اهداف مشخص و معین نظامی بودند.
🔸
نسخه کامل این گزارش را در
وب‌سایت رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=SR1EhGWooVAF1U8HF6vcgxM47-19hWbRI-GgoH9fqfpFZLOa9kyz74x14sdY7Jx4-ewUi4fAlp8ArqRg7sm13abmDv_nTxzq1fTuS4VBk9fUqQgzcQam0bPGzQfbsk1ZKYpmoWLyfGqHZNDNRT55v1MdszOs0FUKWgLcTYOLmjYmoeD07y2NjNWzybRkz51GD_iCFKkNEGMXY00F5mRQO8w3xf7TjAbAQOo4swWpOzREGzVxQaLl7bHGPx3zpoeJo1MSeILAXmUPsj5akyjWwztz91QRTgRWXvSa2KlupYczmzmFJeR-yqN5v-2K9kLV2SQ7oBIOA6oI1LJ4uTqe8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=SR1EhGWooVAF1U8HF6vcgxM47-19hWbRI-GgoH9fqfpFZLOa9kyz74x14sdY7Jx4-ewUi4fAlp8ArqRg7sm13abmDv_nTxzq1fTuS4VBk9fUqQgzcQam0bPGzQfbsk1ZKYpmoWLyfGqHZNDNRT55v1MdszOs0FUKWgLcTYOLmjYmoeD07y2NjNWzybRkz51GD_iCFKkNEGMXY00F5mRQO8w3xf7TjAbAQOo4swWpOzREGzVxQaLl7bHGPx3zpoeJo1MSeILAXmUPsj5akyjWwztz91QRTgRWXvSa2KlupYczmzmFJeR-yqN5v-2K9kLV2SQ7oBIOA6oI1LJ4uTqe8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=rcyVxFTzPCvDX9mql4qvQbhzr3cEjUHqWutNOiQY27uRA_33N38QOLDNJbwGeFj7s3EMU1Cv_ZPgZkYJkU_YPTH4b1Sx2-1b_mZ9EjbULPXUtE789mlOJWwSh0j3q6YZSK0kcSprkOveWIFlWE0iEb-02IVQp9jqCj77yxVYmzAl8_kf73KC53lLgFt68S_fehOoE4i_CvDhZfHF86Oy4GGvpV8bqKls3Deyty1D1VOPpDDlL4nhDnvv89tlKvewJgRnD6R_0MnY-WdzgSbaeC7C6M35hjv3jbrjG9r6z6adgDlQl2E_xXA8soCR_j-2l5qKy1P2bYZZaCD79oebtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=rcyVxFTzPCvDX9mql4qvQbhzr3cEjUHqWutNOiQY27uRA_33N38QOLDNJbwGeFj7s3EMU1Cv_ZPgZkYJkU_YPTH4b1Sx2-1b_mZ9EjbULPXUtE789mlOJWwSh0j3q6YZSK0kcSprkOveWIFlWE0iEb-02IVQp9jqCj77yxVYmzAl8_kf73KC53lLgFt68S_fehOoE4i_CvDhZfHF86Oy4GGvpV8bqKls3Deyty1D1VOPpDDlL4nhDnvv89tlKvewJgRnD6R_0MnY-WdzgSbaeC7C6M35hjv3jbrjG9r6z6adgDlQl2E_xXA8soCR_j-2l5qKy1P2bYZZaCD79oebtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تبعیت از ولی‌فقیه بر مسئولان واجب است»
می‌دو‌نید شمر تا آخر عمرش
از اینکه در کربلا شرکت کرده بود
هیچ گونه پشیمانی نداشت!
شمر خودش از فرماندهان ارشد امام علی بود!
توی روایات اسلامی هم هست که
هر بار بحثی پیش می‌اومد دفاع می‌کرد از کارش! میگفت  تبعیت از حاکم اسلامی بر من واجبه !</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=PPKjeFKjXJgpn-4sCG6ntzl2qos3Kr9d32y_d1zG_41l25VNbT8YcYmpcJnQsFc9tEldMHTtqiHH52XdfX4uZuwmFqA9AoQU-nczQ3tgsvJhIY6jO3gRGP9pG3d7SP0u2GFphTfgroODHx944MqmdiVIgehdBMQpJnAdNBw6AfdluirrFzU2tPBbOSGh6-uPau8r57HfcHYkIeWzRgug7e6pKq8h-Tj7e4tg9RNXpaur1HkUjPQON1iWahOrZZct552wVNpJk_7IT5rI4hMJAW7VwZP7dmItwSrGbKkwIJazh0aQPMQiiNt4-2DS1kzowatOKhK_-6rLDrllSPe2Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=PPKjeFKjXJgpn-4sCG6ntzl2qos3Kr9d32y_d1zG_41l25VNbT8YcYmpcJnQsFc9tEldMHTtqiHH52XdfX4uZuwmFqA9AoQU-nczQ3tgsvJhIY6jO3gRGP9pG3d7SP0u2GFphTfgroODHx944MqmdiVIgehdBMQpJnAdNBw6AfdluirrFzU2tPBbOSGh6-uPau8r57HfcHYkIeWzRgug7e6pKq8h-Tj7e4tg9RNXpaur1HkUjPQON1iWahOrZZct552wVNpJk_7IT5rI4hMJAW7VwZP7dmItwSrGbKkwIJazh0aQPMQiiNt4-2DS1kzowatOKhK_-6rLDrllSPe2Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKF6ExTyzH7bxybmRQ36qssdF_yyAmteFGBq7HCef2WuhMxRN17MnWdZBKj9Jyz5kPllNpxawjYg0LU2Snh2qgGhwI06pol9moyLAMGplA1zdG8kxdG97Z_KMIVwSFghdmrNWt4ne8QRIXlp_bjB0ZEUDVmCNrXt8_NdMAoY-v5e_myTFwiDtM4VHcRz7WECOAgWC6SIhrUnYZ4EmCVn_lHlAN497aslYQZbKKpFWXcpJVOtErN8jK25d3JaGLjCAYD2APNPMKvGzYrurklOamwcFjFnwkRN1_oo-hnTb820B2ylaR-oUzptfAdZwyMtPown5BdKfQkjy7-CDWxx0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgKmoEzS_0MkjSqoFN29oAjTY_6ID5ex3tZVznmVqqiusu-Q5Hj0ctwn9dUa8A6NCJcnFhxuWdYaJLvzKO1cB5YgC7y2K9FVrPFLCgVZiTzeXy5fd_l9N3Q2eJ-NlaKNmviLTN8H_jlgI2NHiKRCMlvQTF9QbgjIDtRQ-OPXriMfTR7qIL8rj9mZ_PLTA3u8fVUkg1PLOX36IQWfWQJBMA1fP-V89Ru9j-fLLSOrpPe5xWyQf9s2jp1HRT1E9yHIEa0ddALaI8AulpV0rmPFtjD3azbqDFoRieuUf7RQArU6CzXTozoot-cbLolCDRJxeyTFDYujXfuA9Me4_TUz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHok6koLkd8lXwcEr-qaLnL1Qgp0iccANuvSqswDFMQ9wYBu0pj0bU3qaccU8ScAGDViNN_ecvIO1DLcFsSnIxMIXMXqETvtFugo95GLob2DMLsoKG7Vn7LfQjLl8h09cej8LXT4B86GlFAKajTDRlC4RMTltdAV-_Sn0Av3P8-NJUNuizfEeZIxffqGneyZvoPLaOYsQqWQtZqFfyfQXhizCF8q62R4iTpXpGE6l6YD7lfuGsUzACdp3HhBnNa5Qy26A72GezAqrWSiA2DWXkF7JmcOT3iz1qy6B9HmSyQKc6JqUmdquCuxjSGdr1JWpMoXzcAzQvW58bQ_fYx_HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oW5CPPljESdX5qw8r554dVyDPZEvgtm0JGofZVl8wszuE7ECBAfj_xgM4yvGd3FAjjZ0tI8LDBPShwU1BJkG4R4xfPZAfKXZYqz6BAiI-QMp58zfuGP2GTSB_NHgxhjPML-QGX7AVz8JehQO4GAO5g9D9PnDaIB7N46rLxhEq8ziprc8Vb8AWXKgGf6a4PpUKTnnT6R2LfRT7w8Ywp-l1GevpJa9twIRVtHBWDqjBw01YdjLsbXH0Rd5USh7HpJsib0kF3pyEN4mgjK_qCSs--unAKe_ELVqSMJXOwy2QNjRkO4NciS4VpP9IrpmlM5Rlj6mxJejKibrvmkOXdKwEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pz0oYkFc08Cqv1m5YaFZjHVyqjkbwEgue-sQRFmequryE6vwq3bKbQ9t94dkE63hsfLvPSytgm--FV0xwnhcQWZrYfIodTlGko9VSJphJH1CcYzxAHIqymJ_ZXA77yiFpQBvwtpHdqiB-qyN23N04Qxkr1yYEojAIR1LkNkb2RA6sw0yvY0H6OF1tSULr8JNzdhzoemzr1fXk14DRR1icIfQxXFbEBgWEkgK5DAJPg_jIov0tpt8yiN5POCXr_b47OQiUV_eH_o_NgPPJrHlybEPEPJuNrNKQ2SdQNiDHsd5xt5Tg9TKyD-WDov0_X32UHGZhk3iKAs99XDofBgFtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHKjgcW-bEhiysnhsxcxKcVydjlUB9-mTTQ4zgP0cR8szUsDbKCSp2wC9xiORLHEinJsi59bhemH3Q-eVSHPHNatcEs8HzH4X3sEEyWq4ttm4SCIgeQDJMvNQljtwPtg1L7PEUc-0z53E-TbqEJBFKDPWS_oPTzqMvGq1qXM_AOgVd2XxDHct0shmd3hFpKEowgM7LUj8ejTy_HmprsHKp-iLiexcZf_d7U01Gh8t9H5nqwQTozI-7Tamjwqyy4rkV7aT_1AtxanbosqvVW5_NuTCYkM7bBpZvtkghn4E_wgYF6ilCDu4yfXTi2zApqqj5iQ6pWbBDalrTYz7QhgIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q63vlIrHHFz-BCiRDuwrBKjnoX_GA5tu8aQKSvXvxE-VNTPEaRAM-6bRqOIWOMbgGwcO-dxeqRCojMu9EbxhS7VoH1LpEIom5CL3zvfMTwtZPuENVJz1X6enMaoz8RmJG4-n7I6ceyGfyjUPVNYzhDQaQwx4qYF85IjduzRCAigM-E3YWU4bYUUxEHIAirSVEdnWHRWEHnCUjarRGVy1-cFiSWgjINw8fvhrCbdmjfW5VPf-hLeHwROtdff4je2Ozm8NnUrhr3mXE-zGdjAbHSw6Ww0Cfm6oYi3VhTxCm6c-BrPZX1YzirQcYxtytnSHckVbQj_EGeaBs3TU56GEmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2htaFih16vtGRgJYq-_JHU82V3suJfh5L05Nf0mgVYxLmmsLY1hfFj4_GuLRmL6p-bG2fqTLTNQyxgxSNd5mm3-COohLjSu9uAT3qY646Nt3ByO4vXo6m8dAc7XNL5zsD05BdHeRxzmey3B6UtNlmZvS6pIoUWvo2LZUvSRelW7SXnz-2IF6bqto1YW0YPi5Hc1EynsDW6rWu-6kv_ij9XSaf7hu8TqpF81acI7vr41l1D0WbpIuPwJQ8x_8xu394ZZTu4sEvYnqIwZYEWAxhWxlfnsMnyXvCIuMDAXLnmrJmf_qKrguo70xsTNrDianWYULHiZJUyJBqxPn9Lcxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmK9hsH7cvb7xQzwBaW0Fg7rINhP7skrYREtFAwMzYW6q_0n7-bna5A4NXmHHQtZJN6ltb2G4gyk8rqgtuCy5CnZD_xiukg4ezy38NkCIq53GlONNdwd5sD1D871HqaW4AM_LS2uWUliPSEkiOZUprR9sjsxJb4MdP4MsnA9yTPqQzSG4sdZBMCr8TCXcqqjOISUcT7R0G8KSsB1IXCm0jStDggh6LN0S6sOSMZEaPT8G8G1oUwQn99j2T0mcG9R-IeT2ywhhpQqSNZ55YN6SCVHqIWnZhIJorMLQveYOjV5V5y1u1hGmMaHhgYmE1NX1vIfXUKi0OS2U6Dix56WEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرعون، جسد نخست زاده خود
را در دست دارد، زن فرعون گریه می‌کند
و موسی و هارون،
در گوشه‌ای از تصویر دیده می‌شوند.
برای مجازات فرعون، پسر او،
و نخست زادگان «همه مصری‌ها»،
«حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس
که در زندان بود.» همگی کشته شدند!
حتی! حتی نخست زادگان گاو و گوسفندهای مردم مصر!
و این تصمیم و اراده خدا بود!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyxfh3B8FxgzYqs21_I7f40FXnTPmMarxFlnnAF09HzA09Pz8HyiZrHPvVedv55anDobGSFYjNbvWVSUVImjfxQi7zAg0Qw0C5oQrraZvB4mo3xg9EWzgzY_2XiSagEuytorCOj3o_JKv3u0zwpOqwwSv6g2hQNIcMsis4sIp_WPW2aFi-OSjF9PtvrRbOjnRT4BIFJJ6bkAzNrKlIvXTyUaakOqT8B8WU-btV-ZbUUCoYb4NBy0w6WHpbtokbO-usM7RXnnwSpGApp5ON29ovkxsee1vNoXHZ6vUfd00_zSODtS0fS0_qVhNL3MUiy0lZmvIZ_YsRrc7JgaNbuTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIdaeAK-hQmDrtQ8w77qCy2u4jvOoyuNsDE2eeFccJhWpJvdBO1jzszt6H2bn75RVppOVaZ0objPfD8z4_R3bW8qTC4mx4xQ-4OgxeEvwc-XuuuVLr4ssBOPD_pr1voZAq9kFuac9I9FbaeWbs2TIWVQEPg_l74WAfloLmonEnjW9cepOVYmn_VQ-TbNofpg9NJpxe9TAPi6KP-6XKXfQMTbN-flk8rw2N894Z_LSs4te837R4ul3P57_FWb0SZ49zvJBPydOt9KnxDHWuwtayAO-y5N7_rs2q9rU-6v9vj-8babI3oW-aWK3s4MXq7VGmxATKGT_KzcqTbbMwRVlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMunzEHTF0GIYgRGqOjBHp7SX4rpioEXWafnY6KltRS9Qv9DxtuvU_A_keRyzSzp3SIMY3Q94yxi1JLsoEupuAkjlYidcBdWVPQnw5IXNHeLmrZXrDY1clm-tGp4r-ZZnmla37gq9wKo__gdIzMmoV6qnP_RVNmoICqPG01V8ACj5bLc_Ym9NpW4kAQbZu-BAlq0db1tq2PPqIwuF5M5H8YY_FITVZ4qoXHX_yP4PTirVMnlbgUMyxoivJGiIFaCnzGIEb_WF8SbGKDOfb_XomJewQ0YZxHfpsarUj0P2UTYjm_0o9Wm72FlucVeE87UW_jPSqye_ioyEBW3biBtGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbTK7WbdxxXOqdWAYCVEnT1eFrzddTb3GbxoE0clJ7XcLpINkPXheHM8jJpn-t3b73pJ0Q2mrFgB5oWHz_lkffU46ApwMGgtuipurGv_UchBg51VnxgvjhKZ4ExI6tjp5P3bV3dweVfbftPI2T8sWrqdZw5NvAU4ArE24NCMo9j7JoWfMLfdxhCzS3YoqykSDXBwrBtv_Lhgzb1XY6VW2NFyVN57IPb78_5P8kLehavzCs6AfUAS5iwW22CvVLUAwQbOfpwqVs5QM1SJrjPlNbe8Y_qCXu6aHcFPWwef29uEVj4U2gwVU8PwT2Ee5wlbXJdkiWc_vUU-yqZwkpbcWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -
سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!
تباه در تباه!
خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».
احمد شاملو - غلامحسین ساعدی - اسماعیل خوئی - منوچهر هزارخانی - هوشنگ گلشیری - باقر پرهام - محمد علی سپانلو
اینها روشنفکران ما بودن،
جامعه آرمانی اینها، ترکیب کمونیسم و اسلامگرایی بود!
از مسببان انقلاب تباه ۵۷.
از مسببان گمراهی یک نسل از ایرانیان،
از‌مسببان  تنبیه نسل‌هایی از ایرانیان که هنوز  به دنیا نیامده بودند!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7Y3bkePaL-rStRT6m_HIf_F8LoSlWtWDWRMjaiGg7MzwxEkb0igGaHzqg4D4rpSopf1HmE26is_sj4uLpgBXT4xuhy2yctRiqOsJFuiaxnOoN2nOE5Xl6-4mHaIsP7RhiVSn36F0bqGf-36FveqvU9O8pxgF3xNmChuzkdPQ1R-XuBfucfv_uhTl3DbUxZm1-JpfC4N4L7X7jqIwbicYlCX5Ozzw6URwdvQwxezPiiLUr2sVFQ-2DPx__IjF06ntoAgmo_uI0GqJZ29eoP6W69RKNBpYOzKGcDcRy_PW44ODpGto19nB-VzaRKP4qm-1wvDyRpYeOqv7APMR_dMeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=HatFNQSmY2tURNi3wi-SCI14xulvOyBbKw7aNDHWAUR5IJbRkgdTbaGFQom4_F0_dM1XpdvjpxM5nrnjuJt4p0ZRIkss2Vh5-ZLdz_uDPEXm0rg5tpmaM0uQneILvegaNYm65fRzVKwDnblwNvlfkjsR_piLrVEergf-SXm1e8DhtM11wWcpAzovjuPJoRtDajgHsUINI_tdjHdmvBG02rJFPAy64eprKz6i1gzb3iB0d05hpBLLkEPSVg17DKGSLacIqqBuFByPrrf4GSPS7qAVpi20e9ABMYJkp9ZUz9orYUJeOWk4PkOB1Q6KNEBJ_zn8IKJnnLjpALHLH1G1DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=HatFNQSmY2tURNi3wi-SCI14xulvOyBbKw7aNDHWAUR5IJbRkgdTbaGFQom4_F0_dM1XpdvjpxM5nrnjuJt4p0ZRIkss2Vh5-ZLdz_uDPEXm0rg5tpmaM0uQneILvegaNYm65fRzVKwDnblwNvlfkjsR_piLrVEergf-SXm1e8DhtM11wWcpAzovjuPJoRtDajgHsUINI_tdjHdmvBG02rJFPAy64eprKz6i1gzb3iB0d05hpBLLkEPSVg17DKGSLacIqqBuFByPrrf4GSPS7qAVpi20e9ABMYJkp9ZUz9orYUJeOWk4PkOB1Q6KNEBJ_zn8IKJnnLjpALHLH1G1DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6BTb1PhRAL8W7unk6NTWa9ghFtvLEIUOQDX0MtD3Zy32_pp2e2VOhITfj02LT2MTBEX2C2J_T3ioeKigFthYnI8wILArTSD1w6-DWOLR5_2RH6MFPsj4PYcQxgybdbZhTNMRFODR4h6McxhNyIGUVlLaqp8ei8vwzBR4ZdDHbGpYcWxhxzLR35Rrr_YvzTZkYNTEMBWxWC3YxhQdx9Pa6opXL8cNDFDRVaKvQHdxQBJszg9UcUBxSRLYZHgZOE5atM--aBfcCNSNNT9SW-7Kn8pgMVSI2q7W0IdzyNTPd0c_LHBJ5_Tw7J3opkVQSyIDTg0uGkW4CIs4GNSkwvkpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHZFjaWTDHW7bufCQUL7w3LjAdAGkCk_8-L4nZYnOOKZP8UnkgX0kVYHSHPk6iFWU1glpTBzACJkHiHqxuJCk_HwloQ4TDa-FKEFKdGdgpknGd_3c41rjZl1neUhGFNr_jnUAWK8wW4wi5eWJ1iWpVNyu6WuEDBUWu_7yuqw-jt-3zv9pJEoV5DaaSCeYp3CqX-27SjpZaadbSXORoKLth3iQBx9_5g_aQk-bBPtw60pmzeO34DbgRIn7brIVIOR4kgpd6U2-wE5NcSZRKglqdwNhJaBo8An7Sya56xA2cd4UKTlfjcyhXQ5VIqTqWUf6OJq8LZgtoJxm3ZfYcxgHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZD42IWsJNEMkmQNJ_ZHqxd3WEHNTzKGZMiOfyCBHksnYEl1yb09SE-F897k0Os5hfDEucXt5m6zR1C4qQW-b52fQIWnwXDKyiHVrZXwSChJw_Yx97oWYDVrk7Su8cPRj0sKXPQbxJmuoX674GxMOkLbdifetFcD6Ioo48K2uGlDFaJfTltNaHb_xxQCPo8lUGoP1hVfxAuVW-UOV8uGW9bgy6b5yqvtrkzJM2wON8XIackSnYm0BqTLJ7-obGo_pqdu7Kr2lwrCoVaa8-hKtQl4mKGmvIE1L1HV5d4uYpYWJtLWk3V6EGQlu4txuRlHugJgxp1nsbRvpMN_e_i96Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh--odXdngVU2ByDE-LuiVwcU-j2CcYyovYIxD1KbmpmN_ZumQBAavvF9L-p6g1i-jslS9j-1QeBga0qre1-f_dRqfnPaHqSKLrrdm0237p3HVJXwzGwoj3-UxgEekyr9s71kAyIM2jes-SAgKqgK27my1oT3pGaJPJZV0pqUs-aYI3w7_8MiY5eXxZQ4TGv1OgBiHEn9hMuAX2yyQqMmbWP_6287HxSG_prSthcKHpndIoQ1rRhHxmcpfCag3komPdALzGNO_JhubVE6MOpWunAA7b624sJg84yL8DvZVK8jQsOdKC8s6s69u4QX2og0QLD6jNodlkv9qzwOJiqRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_8d3Wd0HqbHzfc_cmW8F5-q5FV_aUBraggmU2H14Z6tcyobxifHbnNfEU3tdb1WgdxA5lVA5WGWcPeC8t5p2YPaX1OMym7uTWASuHUvog5aH5-zrTFhsuCI1JG80u-ZFh2-I8lJd87EqDFmpfzD2NtmCRvBChVGWBUvzy-NeWwYLAXJZDrgl8tUtIor4KA_vVuvFkGztNhBdBTkODIw7ZYCcJcGWmr3QOgaL4Icw_bnKpLmOncevo8QpYxqrZRSH38wzzC68SuB6cs4HCUxRXdFU-nvQ4oJZ1Et-xQVakpStRPSuHaOEWtBo3MrtE-H34TJrFwAUra87pFwri27ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArDtUiWGapo9T-P1deKqLMp5of0RdVuLIln4F2B6S2o7WvuWt3Z9IcRLwC45UNswD2PTTnJf1Ag3IEMyoUTfoFy3Akz3wQpbBohx9oqN3zyd3aDvb7ySwjkqznVUllwjsAnd5X72Yp53cCzTrujGxQOrLjorpfMIUIh_v1fxRKpjAQm6h6bx2XBK4vF2ySXDFgbouCysd1sEHDx-o3FdEH5FEqF2M_Xjv8yZ33KIvHtb2-2GYqLqcwVfdvb5MGmB3HOrfbc2R1oYRhogc-9eOqM_xw3ZwOoYKGdeifAkMwpu6tlke8BLhzub1Fa3f3dIHXXANrce3nwloaSgjXXxXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZpSnUremJtdTlceq4ruS5MLz4UG1yhm5O0MUiVJKtuR-8-pM_XLH3eynLgqHnBjWnNdp_n52j4YP0NIhQi1tT12zxmxLsjBnY8w4KSlxS3ZFhhqg8PpC4ShkQVxSOSjh8JgeQow8O5wjI-7he7LZNhGxK1SRaqWywQCo_4hoU58loVXif4R5522zVXCTOOA6uMWhrImRN_Qa-Tmm4PwDrBCl3SeCDRbDJonOmxk5zeIsKOkTGQlPg47Jc4-Q534YF_upwA5_cT2Dzaib_QBKdrSbBLwrbGeAtE7UgAgJ5N54cUcM5iAIryoPHkL5vb6evOvw9rLi8ZSOAlS2Ne1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObBPm2W5rcGrSRPa0PerueeHd5-IXh0YAhyVHCm41-FnSAIxyaA2YLv_Fy-7ScA1awPQ6E8ZM4rh_3IpUzk8CiZ8Ueq7xUeYXbbtjq5zU1QuVXWGIp6FCMuana85rDhAnaLzb3NFM0NBmnYuf_9zJBNE127YpNngiyMYTetUXYVRDqBBV-ZLd1TufTljriiy6dYh8oPQ8_hbSA0Tnep2iGKRavEM_ImFzC7r7Qk_swVsudLkzr9wMCeytvndrKQUcdgK88zQeYHvkxZLGiMbB7ahEuas32XTz0IjLGHWQte67rbeOc2OE8VKK7K6_7DCn8SxCMwb7rAsFn8KoUGbJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دولت ایتالیا آزادی رفت و آمد هوایی و دریایی
بین ایتالیا و اسپانیا رو به طور موقت لغو کرد!
این بدین معناست که تا اطلاع ثانوی،
پروازهایی که از اسپانیا به مقصد ایتالیا است،
دولت ایتالیا مسافران آن را کنترل خواهد کرد.
اقدام دولت راستگرای خانم ملونی،
فشار بر دولت چپگرای اسپانیا را افزایش می‌دهد.
دولت پدرو سانچز هم اکنون نیز دارای کمترین حمایت شده و پیش‌بینی‌ها حکایت از آن دارند که در انتخابات سال آینده از قدرت کنار خواهد رفت
گرچه برخی از راستگرایان امیدوارند با انجام انتخابات زودهنگام، انتقال قدرت سریعتر انجام شود.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=hrx82jxtNSzz8Xv4x7UnTyL7kmMmluRL7VoeE4d01sdqmgfWAk9eDbHiUKKK6WIfOJ3JivzVfesWvk4HmnpC1wWOKICbnH0Oyvk27vafokBMfEfZDN7RsV7G8GjuxMIv4xQ_yhQ5xfPICRWIeXUcGWr_AERdnVqY1O919oM6d4qNxSnxe_VRrUZJY9dl9eZzixsIYuXfvnlPXnrlSIU7Mi3ZkU0KEvYYuA0hJUt9rKqDxrQaWwHqmDw-im4jp9YK6tWgAXeuxE9W6yCUnLB16E0PA8HZfGbbBHCR0Qf5YABEFh9YwxvZZav74hE5y6tG5TBC4U-fciinNAl7FUKpBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=hrx82jxtNSzz8Xv4x7UnTyL7kmMmluRL7VoeE4d01sdqmgfWAk9eDbHiUKKK6WIfOJ3JivzVfesWvk4HmnpC1wWOKICbnH0Oyvk27vafokBMfEfZDN7RsV7G8GjuxMIv4xQ_yhQ5xfPICRWIeXUcGWr_AERdnVqY1O919oM6d4qNxSnxe_VRrUZJY9dl9eZzixsIYuXfvnlPXnrlSIU7Mi3ZkU0KEvYYuA0hJUt9rKqDxrQaWwHqmDw-im4jp9YK6tWgAXeuxE9W6yCUnLB16E0PA8HZfGbbBHCR0Qf5YABEFh9YwxvZZav74hE5y6tG5TBC4U-fciinNAl7FUKpBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcBcca5Z8qF3HMZg9nWoA64IvsZQ5mSb8damEHEyBfzvxbN6YbUBgWy3dA36N684HWmcX5gZZdCBOpvtoWtMAIubVnNLmDSBWCIbxgZeEY1ClQjMCiLDCUfuG81HwcY4RGu5iGsglyrWpLaMLqyJ1t8sfseHG8DTrpDFO-pUOSjYisg2JB5McPDhgimXzm1q7KmyO2TquLGC6u2-9sHxJwdNiB7NQprA9sxB7-r5fIyqaJFymEgrl85GblhMS8F50bsQn61KCkWgKMLuAa6fULT9yQD5pwSSr4r-fRTUHzULO9JHmofSA7-YVc-zNZ0V8xhq7EDUY924eEv1RxrYWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXVWd2o5ZRaB8ZaUWkzfwmv6h63_PDKcB46tV-kK3ty2R08mRSSiRgVDheQTpww2GVJlt-nHR_xjxVEKDQU2QXmpQuVRkkwgzlUKwwJhw-FeFyx9YIB8oZF3lpN5YUKQX4kMkZUxHp2gxcBt4DaZxZFt-296QTtQNhuqvt5TLsVZUUFE0DcnPrGSBnBLPEqKdFG54yritCHtOlztaM4rW-jaK7zXEY7AAI-IP5DDwcn5ASotYuzGYpJVGjdmkomih51MROCLV3oImLZKwN37E79sn5-yYhVuNtD_o56OHtWsJ_63HYaE9sssFdjxAd72kF4w2-kHMipJ2Scmtl8RKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7ijWHRpIeTttlurFN8AaJPPOAY_YuPCYf8oniJsnFZ6Vdiz4IwUNdZHLF7FtAgfS3yZb5HKxj31zUGrOiZpl_Orh6ruOAv0HOf_uT_F4TjrvgyTV2yHIAiLJFbrOBKhhCmQHcJaXvxsqFOEs_V3FaDvY-07H0CXUBOlBza5FwCi0XVwG3hNQzGmQEiGF6pzzSx6Ing8aW534p7qM-gvQbPplv0xFg2UvIAYIM9SCY9NjDDWV30qETkzAqjvZ56CefuUd3FJ41S1uXOE1I9QSMUZv6qvzSV1PKrzpULcdnnVnseugkysvlYEVkUeUeeVHVzIiGJJVJcVig-3-PmHOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Owz8kHpo6upqVlugG3c7CrGzeNwxEmT8Dm4lC7e52ToAQao7e19B2myoQkBITu6GMkWKmUpwRCbBF1uBLO3F4LUu40JifHLttjcCuNSKfMD6xygSgnsJqiqwLZdSNJkXzE4XVxwSsxYL3c4eP2uvEk6M0PWnL-Sj9nH3wua-fyx_EPN4y1nQs6GnwCeFBc0sDy6ywYuEB9sb4cywSC0lSYeZeEG3nNPp8rEZEwTVLeCbzTW6_WhJhcqLAYgwgyK5nNE-DM4-R_NRXiQm-3UD3he5rrD34o4_tkgDLpp9-3qsaYD8bec47ghpuwYJuC5cbg_xkw4RAzyWjt7jxW-54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipEFPllSOu0mlqMVVzHZboDoqpgbiXxCETGIdXRliPryk-vP9pA5R0FKLeudh_eKXML_4LAqnr2GMaWMU_8j3epx5yqfyc4USytPEem58hlAtKVdal7AcGV_7DEAGHY-KP0qnIzIQGKq_RIonOGq8Ey5P7Own7go2dpRWz5znnzHVPt2uu2VqeSvff0zy_xo4P2YH2tng7tjRRqNfdkV0MgsTfb6DlbkR6_iroNCmzQJI6Og9hRnh_QFlZb9yhMCkOlHpPY8dYb7zg-vDkNYJG4Zuq5PAgHsBagyk-khh5tz97brUOMwyKHw1HgwK6Xj0MNe-14y7MaHdBZ60cW8sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQuOdpG4KwIEtwVqUX37_tDkvECa3R__w3bS3fJfFYbTBI22mrO_nCLP_KHKvSqU3h3rB-aGcwlEoDpH5ZhUF3mtKGg4r19OJutcMlO55l6RsDXn-kA6Z0xbH0SnCJBWHcEN_34-1MiSnWqrYohapsJl75vGjmr6sN1on9811plF51OKE2U770PVuY_bT57mgIcMWWcWsm1QBkJiQskwsbSi17lUttIvpBip1RQcMg2Pk_ErNmwR__t3ThfkibKP2Hyz2A8aMKRizVmHk-ETTko_mzQhGIC8WP3PSMb-wIkO_Pz6z30oVfBXqgB4IehkKGFgVhCmCa-T4_hMuO8acw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTi6faezayV95PiHYo3J_CKDqHRVhxyiI9mLl0810QBPOhgJH3RJODJ3AzBnRujz58U9wTONqyGUqI2e-8_ht2hZ2VLwNwm5THCytPECIDkSEuMR266JRqDxGV8FN8A-C4Q6eVJcXgAXP1HHvzejWeJgy4V7iQdypLvu90HhK004e-JIA5hirjg_dIhzMQlO_SyOCNRRNIa-VeT0xwDud93RuhtUK97DjVmhJcFvmM46oKYbXjVlat3T4oQDJWJ_CIjbBy-wfzorbgv8WeQCuG9OYbVvpCrNIwa-bP1jCY9O1ryW5-r1qt5p_-mXIp7e5mx7cZHGyiTeimtt77m3_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
