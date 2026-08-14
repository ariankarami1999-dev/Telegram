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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 20:53:56</div>
<hr>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=IU274KViiR9b3O7YWr8GacLJXXqShsd2a1npVj3O2ItFHCIWt3IDyBvu-KeKGglYkcqRmDixbIdiqLX-rGsur5jPeJxmw6LtMZw-RsM9tuHNhUKcYTSxskqmGEhFdrbEuYUZDkdK_waYHcFK6CYZHhFm18p8jfGX0ru_Z9Pt9nir2R0paxlmrKLlkZKlzBtd22pS69EDBSeW_HnLhX7EWql-LTmbXm510ZgC717ny1n8zD_M0lpXrmsOZO8YTytZvTGDVJadmLCptR_f29DlaNtSzOmLvbtt-qnZFZOohEse1NM9gKqIrUmJLcc1KZBdH79L5bLtM5VYbUc2L_MMpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=IU274KViiR9b3O7YWr8GacLJXXqShsd2a1npVj3O2ItFHCIWt3IDyBvu-KeKGglYkcqRmDixbIdiqLX-rGsur5jPeJxmw6LtMZw-RsM9tuHNhUKcYTSxskqmGEhFdrbEuYUZDkdK_waYHcFK6CYZHhFm18p8jfGX0ru_Z9Pt9nir2R0paxlmrKLlkZKlzBtd22pS69EDBSeW_HnLhX7EWql-LTmbXm510ZgC717ny1n8zD_M0lpXrmsOZO8YTytZvTGDVJadmLCptR_f29DlaNtSzOmLvbtt-qnZFZOohEse1NM9gKqIrUmJLcc1KZBdH79L5bLtM5VYbUc2L_MMpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=M6CzRIqyg4ICwVOp6wIcy7goRUkS9heIOuRgzCYG5gaMfPVQzqzj8f19Ic-TSgdSU9qZo5hLWQXQYolCmU3VtYMie3303BUEEmx83QfjmnS0WE6Gfu25SVJSfVZn5NiZ6aOauETTVPvL9PpexGsgid3poHiHHnXzOkJH_VimKJ-Hr6EnJ0ajs5SD06oK-APv_qYB9aoBKwhUFxYQctyLRUZi-LQeBNLBbGxS_F0biusxGgNBRCTKcyUsCh1vs4OxJLxWdJrbplvJavd6R2PllQyc-rCniX4oRQIOPU_gAFhA1RGFju5UQ0hIqLUS8lnZv7KTcZjxVQdwbc_cevxA1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=M6CzRIqyg4ICwVOp6wIcy7goRUkS9heIOuRgzCYG5gaMfPVQzqzj8f19Ic-TSgdSU9qZo5hLWQXQYolCmU3VtYMie3303BUEEmx83QfjmnS0WE6Gfu25SVJSfVZn5NiZ6aOauETTVPvL9PpexGsgid3poHiHHnXzOkJH_VimKJ-Hr6EnJ0ajs5SD06oK-APv_qYB9aoBKwhUFxYQctyLRUZi-LQeBNLBbGxS_F0biusxGgNBRCTKcyUsCh1vs4OxJLxWdJrbplvJavd6R2PllQyc-rCniX4oRQIOPU_gAFhA1RGFju5UQ0hIqLUS8lnZv7KTcZjxVQdwbc_cevxA1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=HIpZkecyjlswLl1I9n6eWU_PXqTPdGcQs9nzWDgl1h7A9sUm2Am5UbcsAQlmOVtpMuYglGXmzotofbFzjhrQ68smFjoidsI7YQfM_IN3ZX381HMShOPf0TsCq7zVWVgfYUxXpL0qzXdI05p8UYzR0GOlpWiQjHlCXaYxl2p9e5UxF1Yjnq9-vLgT5BeOabKvPXYnvrNJ2Y1I6pVvuGjzRXRa-23TzMwq_3ogbogmy5hNTD5tHUdjFq20fMygOhXlMZ_YeBmC3-vOxYNGMdOVR7p4lZfX7zGrkE67vBLoilq9YQiOGZqDPMkUPutL7xQhJqqwPtUNVCbU7ao7eOXkMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=HIpZkecyjlswLl1I9n6eWU_PXqTPdGcQs9nzWDgl1h7A9sUm2Am5UbcsAQlmOVtpMuYglGXmzotofbFzjhrQ68smFjoidsI7YQfM_IN3ZX381HMShOPf0TsCq7zVWVgfYUxXpL0qzXdI05p8UYzR0GOlpWiQjHlCXaYxl2p9e5UxF1Yjnq9-vLgT5BeOabKvPXYnvrNJ2Y1I6pVvuGjzRXRa-23TzMwq_3ogbogmy5hNTD5tHUdjFq20fMygOhXlMZ_YeBmC3-vOxYNGMdOVR7p4lZfX7zGrkE67vBLoilq9YQiOGZqDPMkUPutL7xQhJqqwPtUNVCbU7ao7eOXkMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=O1_p8wpk8d825BO6UCX2hCigJwul7281ltIAiQ1uDwGAIH0XCPjDlBQg6Hd4wIS3t517sau9z67MIRpC1Y1CxIarSFx3_Un9d9dQCmfaCrQ8jNsLst5CbON3XShKXnARFqypRPj0SnYRrLtjAkHtykZKjZv9MsZKHqjLs-8y_s19fL5-UOMKVBBuRPWXh0MkvtQr8zpm_XARRKsXhGPBv7qb6Ti3die8xGcPQ8A26vk5TRdmLchOg8ua5VB8l7VVes2iN62mjZEj4h4b1QtTHviaOb-EZnveZ_Eb3YXnYECi_7-cAeUVKRWQ--C9atAyJBQVudsgwqOYLpxK76RDEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=O1_p8wpk8d825BO6UCX2hCigJwul7281ltIAiQ1uDwGAIH0XCPjDlBQg6Hd4wIS3t517sau9z67MIRpC1Y1CxIarSFx3_Un9d9dQCmfaCrQ8jNsLst5CbON3XShKXnARFqypRPj0SnYRrLtjAkHtykZKjZv9MsZKHqjLs-8y_s19fL5-UOMKVBBuRPWXh0MkvtQr8zpm_XARRKsXhGPBv7qb6Ti3die8xGcPQ8A26vk5TRdmLchOg8ua5VB8l7VVes2iN62mjZEj4h4b1QtTHviaOb-EZnveZ_Eb3YXnYECi_7-cAeUVKRWQ--C9atAyJBQVudsgwqOYLpxK76RDEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5TDZUffIh8JV3Smqyqy_s3bOpO6PVfr52EdCgcy0ub_StzR3PLbVwg-vaqMtC9nEejmMlhfOoqtngwPOMi7jaouY5FA4VWURWbivbF7kEn1GPGR_qcpDit-_TsQV6WpuG2hO8x_URdSEQ4TGFnMpLGljjId8x3kWB3gEPW2H83Fx8pVWbAjpq_48c-r3Eio0FFuAw9z1hvFwK11s6ibPjC0aEWxMKzSSxapylnHoHK2qx1zjeugKYmTid0YnKh3cNLSALyryQ1cTDYX4i3pj0J3AK6D9fCvRfcY6_WheOEhLCHPYGfLaD6Z9sWX8AwHhuaigc6tF0dblsZ3gqguFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=VJrDj8rnrS-FaxeNjU7HHL_H6hKJfghyMnSL2cRz-7Ub8-CbUg9MJG8SIEg9qc2nUU7mO3b19a5PbiqCNuKUvFutPs_8opv-hBcTVOYHYSxX5BRunFN8EpKv_QXnSV9xFQSd4VDWjAXoUqej1p45Xm1zdn2_Wqf2WRvHzEDVC9SYROBa8H0Qr-1pcb0uyq6GnnQ535OFgkbLheKvi0GF6knmb5PnTVo-rCVCe3rbMilOxahGRbIaAJTTn96p9o8K6JY4wopLo0a-Q2J2kw7IeN5fj_fIuiP4BhBX6FhjbwwhjbIcSkOk6OYhmcRj7_BIPmQZ72YCgHUD-xXr5ajVwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=VJrDj8rnrS-FaxeNjU7HHL_H6hKJfghyMnSL2cRz-7Ub8-CbUg9MJG8SIEg9qc2nUU7mO3b19a5PbiqCNuKUvFutPs_8opv-hBcTVOYHYSxX5BRunFN8EpKv_QXnSV9xFQSd4VDWjAXoUqej1p45Xm1zdn2_Wqf2WRvHzEDVC9SYROBa8H0Qr-1pcb0uyq6GnnQ535OFgkbLheKvi0GF6knmb5PnTVo-rCVCe3rbMilOxahGRbIaAJTTn96p9o8K6JY4wopLo0a-Q2J2kw7IeN5fj_fIuiP4BhBX6FhjbwwhjbIcSkOk6OYhmcRj7_BIPmQZ72YCgHUD-xXr5ajVwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZJd5mdJLZcoBbHrOZLmlLpxJGfYFiroZAUZy59hTWo91kAukuJ58VtFMvW7cqgh9XG6DyZIx7cRrm5NBsuAA6yja8GyLHXfvPa7mpMx6Tn_TLL-E1qq3b8PmGagKL9kgtG9WZLAjYnTooR7eXUm7ZokvTonAPBI7J3GXh2gVZtFHr-ifJU8Kk4v2xNNK6kN0lf-P-l1msmj9OiWtDL0YI4y44BEZ2hCeoS-38q5wB3QqaKKf4d0_nAPo4rc-EQdLxIJRZVTChM4rZ8RmrbjCyHqeMM5T0_ExTbFm-o4iXMl6v2maRgqUrZQxtVtpUlfmpZ2oVbgR3eqMTUitILGxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6549" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6548" target="_blank">📅 21:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ox6ItQUJ9qG3qVYishrE44LGB6AsY-xMCViqFY7cva4MWyPTQ22JvgEYuxhsa4SRJsAOvySUnxDUM8piJKgFadKnlF3ecGcWGa6VCY4D_3vIO9AMsLCY4_D9bda3re0V5syw3la0h_hcy48_-Hm21XIdoDaDnw3fPFS1IyZV_ADYWQJztgoGii7Tkz_BaQcHA1caG6cYuMGANHHajPN9vIGbk0Y1OwAIOZgLquf0ICGK0XkcEVYw81Jk5EpOoz94fmSFDMVlnQcedaPD13v0BdDs57kAHWhFykYJDc06BC8rCVJy0Y81wI5uWIW6Y1MVArD6iNQ1YwFfIYPQbZLigA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=Tt5HqmGMCUuBYCu1ozc-sGtM8RkGl4V72NK5tpn9EG2vgalKNB_q-0P3b6qJiYvTuRUkOgn1u06yUFMXNwJX36iYNoc9qRQfKnWYFDUgu8gVM6v8a71dRb7pQGXeEd5F9TfNGrarjrwxPkXSa2XY9PfrJEr0sjO2B-Ecc81l_wXFAoihZ-OOvPY_kkNq2j9dz_oqc0MyREDSRH420_D9LSVxam04Ro8C7QDUW9XCM4GVKZT28W-PYTy_jbwDEi91AWwqWh64zpnNpiPmhv9G8TtENHu0nBkI9MlxpsFpycn8i4jj3V-w60oyCGecouSxstQckruJd_TUBaxZRysqVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=Tt5HqmGMCUuBYCu1ozc-sGtM8RkGl4V72NK5tpn9EG2vgalKNB_q-0P3b6qJiYvTuRUkOgn1u06yUFMXNwJX36iYNoc9qRQfKnWYFDUgu8gVM6v8a71dRb7pQGXeEd5F9TfNGrarjrwxPkXSa2XY9PfrJEr0sjO2B-Ecc81l_wXFAoihZ-OOvPY_kkNq2j9dz_oqc0MyREDSRH420_D9LSVxam04Ro8C7QDUW9XCM4GVKZT28W-PYTy_jbwDEi91AWwqWh64zpnNpiPmhv9G8TtENHu0nBkI9MlxpsFpycn8i4jj3V-w60oyCGecouSxstQckruJd_TUBaxZRysqVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJ06s1SQkPB1-tsRP_tyH_dtMhgEmV2HPdjWy-XoNmgkjmZOViw-ebc9r5g6b76x0VVJw0yfWsJ2PWWB_HbBs83Vs5n2XCSlxQ6-o0_uG8_k6wUPR7fkFy91sAj5O2utpoB-egDHzO6eOHd-821s3ywkh3A8nOXHWUIaF7xl6ekMrQ4N-HQXswxn1ySkvk9JM_-aHhMzTca4CuGr7st6GTsuqKFcEWbHTxCeSe9GCqIX0fal_DGw1e1_t2w2F7K2Jmzms9eu_0P52l7-30GPG-9QkHsFRpHgaMfkFXxFui0fY1hQ1CZYgaEJby-Ms_f_7s2zvfuxJGaaAJMVInVILg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=HnJVEEZLWJXiVtqZpOmB2dHU5YBIwB2UFPy2I8yynnsKZhwBltQBwebSUq98u81oAw_6Tvlum6DCi59iZB2eoy0mxF8HRonrbLeonPOx0oyQpbYWAtc7oLs6QBCXLoVlVbWKJ2OYk18Bxmrovtws2rhYNwWKVLXoCl-b1-8yUqdIJvc_gFmO7Cbuv2KiqTxIqdidJPVWS_F9S9RzBoEpBD_6vAKxchd87IA9lP8JmZC55n0_Hu1MJhPBigFZCCHQceNU6mOdNHZJVCjtbhUgHjgPB27GXWVdhR6cX7Ln49LFR2-ejbfxo9xUVakq8izerNLI2onbmgfBISV8jmEkNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=HnJVEEZLWJXiVtqZpOmB2dHU5YBIwB2UFPy2I8yynnsKZhwBltQBwebSUq98u81oAw_6Tvlum6DCi59iZB2eoy0mxF8HRonrbLeonPOx0oyQpbYWAtc7oLs6QBCXLoVlVbWKJ2OYk18Bxmrovtws2rhYNwWKVLXoCl-b1-8yUqdIJvc_gFmO7Cbuv2KiqTxIqdidJPVWS_F9S9RzBoEpBD_6vAKxchd87IA9lP8JmZC55n0_Hu1MJhPBigFZCCHQceNU6mOdNHZJVCjtbhUgHjgPB27GXWVdhR6cX7Ln49LFR2-ejbfxo9xUVakq8izerNLI2onbmgfBISV8jmEkNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون (نیروی شبه نظامی تحت کنترل سپاه ) در تجمع افغانستانی‌ها در ایران ؛
هر کسی گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frkIGB8EIbTyy_AoAtAuOlgYCpUPuLDdKgzo9ueQV-X2gU3TLWNw0dstxfxEalYyw6g7zsaLOYJI6cGt54td6Ui4YSJS1XjeKHbC4MMYUBjKJfWnqOV_Om2WJW1QWGln0Pm4heLLRqx4wIcKSIFfyYa-qUFDmXJxq56_Q7lxS3tW40qauo4fbJHzi4F0bZoXf3JfO7BsVMuKybo8FBAfij2-sLu_Oz1Gpoqt5kaMCzj2bmRBTHZOv82wBiN57old_r7xVpMY8qIG0236gl12lX0_ed9V0GYeV8ABvXS0jrwTjZGHMdKPncevhBnKR7EbcRkuIHtzkRIR_C4Ytn31Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kteh6qmhMlTRcdaKj7YMNoltcRUw8DNFzGh3Iy6cnAhvhFAQy4CG6b40EMf5pAB5aa_N0wwIBrOGRsAXMf9LERPi_NmqxSmJUFN86ta5nfozBZvD7X_0QfPTIu4MLDPe0Uy9z2Sc27KBpDjGP0IcnXbrEBHDrro1alUrPX6PLIie5OVu_ug8yyVocWIGUNZCFy1UhuoWHbm7FsjeKH-ezuBHu0jFzTN7ls3qA5Xbs0G0K4SdkMuZaq7yW2r-T1rgBjoaRuYnDy7To7ObD0EeCqEW7_zBHKqlbGM_glN76OQljjMBmb8Gqa95vwgVUcUOD1wna_obozjLVKe5VLFzCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkCATwzYUlW333eHUi-oQMxbp-DpOhiCvs9NZZ3b6Ydv6uIrE9C-hJBbBv2504WLXCPsxr7EewWqFL1pUvuQg3BMttDFImHTB9zAQR9Uh7GDlyCNFMpQNw9WtEqh0vkBA2sZdHHMeVf_U0DfIIe6dc56EIQ0LTsvI7OoCar9NpH2szRo6tzSnogMxn_T5My4ad0rzlzUrcMoHvYaslTTeacDOW1YZLjfaWdFzTu2OgWc40fU0cNpls9y7Ve8WwBgEar6ZdOq11sLgsx0h7z7GoKs8QW0_IDBKwaP5VOan-mEm-C4kDmZl-3ZItGeAm0xmlgrxJJiCePEZk6vgh4Zgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=nEzEBG912qeyU4A3DVGPYn-usjuYT2n-uLz2WZMOAQRgvtv6vIcotbMgTlgatwI5mI_s7rwecd3WOhEamAgeailQCs2dMtT_aHP3MYgVV1gSDzMk-pjdtqqSrnWhu3f-PXPZ7zxZgKksvyJcK7Pq3Nl8qfeUGDarjCgaTUyosW7NfKHcWhlXA6I13IcNQbidH3hGVS-Dffe3IfTb_QaaydsUwTm1sonawHINqIudlyVZzMuET3lFlmDTTd2HMC4JHyURdMDB3iWrfry7n_kBk8p6-IiinDUatQN7EcVbNaAosJK4cYplysftcbbjk295_flqBPdYBX3PMXwE-fNB1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=nEzEBG912qeyU4A3DVGPYn-usjuYT2n-uLz2WZMOAQRgvtv6vIcotbMgTlgatwI5mI_s7rwecd3WOhEamAgeailQCs2dMtT_aHP3MYgVV1gSDzMk-pjdtqqSrnWhu3f-PXPZ7zxZgKksvyJcK7Pq3Nl8qfeUGDarjCgaTUyosW7NfKHcWhlXA6I13IcNQbidH3hGVS-Dffe3IfTb_QaaydsUwTm1sonawHINqIudlyVZzMuET3lFlmDTTd2HMC4JHyURdMDB3iWrfry7n_kBk8p6-IiinDUatQN7EcVbNaAosJK4cYplysftcbbjk295_flqBPdYBX3PMXwE-fNB1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fW65fWfrpy0R-8f9zv6SBqKsCqEZvPzqEwIVhvTHV6jm4sKexqaCht1dfiE77t3OfCTdECVEtXGhbTJT_dl1xEsDufj1SBFkxLtqUh6AiedaYyWJDhbzyKw6VYF1LkNxjy1r1GaR865KU4CTwC3rXxOjDv8SzcCcmSMZPO3huwxAa9asLhQ_WrUUYu_OvWtTK-erDZEXjlpAxLMubAw50Q_anvun44jhruiVCNLpPlRhsWgs1WOiF_djI_s06E0fCP-Lvd7yi4wcYlhOQj-0tArfTXHJfegB6m_V8hpSfDeR6VvDbMg4ONt8BRDJZyYBvdFduqMuYWxJfPwstVzltA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VX-080ol3KnyR_WKDBIMJvf2sWZwLwQitFRbdZbQ1YHENcfTqxOQpejcYQCA1FsXAa_dmAFPp6oIyCY5MmXNxVNrATeNGYqTpFbsTBWOOwpeXCv3AXXEzRgY1eu-vs_RM4yhANQBV3UIX5YtKatVChYfAYU7odYr2BJLBmGFii00ZOvKAx4MpLw3eNA9NXacGiY5X29_2hxAckpUB0loVJqXBKC4jFao2XOhF_9VGpqk_CwbbqFQvg9-TdNsHVl7Zi5bGO-W-hdB26DA8sBP2K9BZvDop88L0YlzAi8EC0Q5jGroHgfdCN4YKGxnA6ym4BFAXfClMApGqrMHCJT0Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_wjGmNL1Xg8L0kAoWFcUI1KqEhCnZZHAwialXhq6U8SYKbvhWbox7F9PAoWQVlIwoAql0a8QFud87CREWOHbH4S0Brdg-IW33YCDg2jlJ1dX5fGW5cMIvk9fSAlXwnUSThIUjtXgxuQ-5VRVoD8AWLfuMrwX8a7pXGEubHXSpXL1vaB-5BfcBnUr-KAmdZVYm9X2ZrSfl6Vwr_IzdNKpBnZKZEBYqRbstHrFI6WZOI6GrOGrNPMoROEXKo3eDFmjZP_YY0bN27WFIV6JrVBMYhJ5zKykeZVlwZIwoP4qXF9ljXT3WVhhIhyp1bBjysT9SEC154J5rjXr21Apl63OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEG_NDmh1EnkUW6yFJbmtwhjHwpFvA_S5vK8vo38qmxIqZ_mqvFH9NZwW8w82Tjl34GigpPmzNB_qxjWie67CQQgGVcVhu5V-hcU9NX490q1hUhxMeBfvoqtwzZH1pWtMxXEqdAdYwqUZeq4ZQBqggPTOlpqL_fDcRWfyVFVLE-7dSdcwG4_FEFuS04qIqxqOsEVhPTaSyHUF0HNY2TIGm8Z5QDCz-MsQTIImwfKXijcE5iG5AOucYWNBMcnCHw-xMp6HYs8xwaD4MfQaOoNakxH1KVwwCftvVN0MBj8cHKDMAPUQc_9ZJ_Cr-7VlMGwguxej2b9uL34K9cgjonXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiXDGnviRBFk_fFDL0G8xjll5W4A5Ry_3Ids-EABy70EsP8FzgLIJgkDJrH3sUbmL1M9Obj2R01ITcQuENd8Jtr-mzEanzPwqcuL6rMzk-X5sTSTv_qkxw7fXQTirRMHgpAENlSCvrvoNjBTCTNOvawmw1-1nX1uk7EyinH0wXVv3tM2_ChSFmiosSCswLeAJFQ8WZSBETdLlO9LBSc6LvHvcwzjkz9sk0j1dxBXe4DR8C7p5fktU23-BPs3C9g79OC5kG_vFDdl41yccGtC7U_CJHBnMUyFRlVVmFbO-91J2U5sX0cKoKRXBImCwEm1aSlr6oxG8S9c6k-t5VTwOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OHQ7bf21LD29ZZC0SYxIEo1sApxXre0aKLbhBOKA3whqfgrjIGS5zAU1DqPPVSVTIrnISYwW0EVU9A-hcGt3BXA6q7SSlOhjYd-aGhcIv-NpTIM6uhnllc6GtJ2V94sR-2ZPU9ZSuDOJleIzHUASay0AZOr0RMki5eHO2rBLPWLWquVOn7EZmvQcLFZAX4XjDLMilks_wBSRo2RyiQ1dHwm5LFQwgedLWCWXQfebIJOVUAjesA7atk6hZjd4zlcIgj8GZdTQNtpv60D9VAXuq-LARNGBRvC_mT8SRW1CKC4Y-SCLhYQpilR2yTYqAW77t0ru9dD95A36BsoaDZev_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fm7aW1xFsIyOMBJFfz9i3H4Gk-A_tBmJWS3fWJKojID4850Sye-gxSDb0-_VAI6Bur-EuwQSv7Bg__GqH4rHHpz4heyQYSUUn1Kup2UrDo5Eh-TOIHltVOe-ZumwV3fXlDBB6UO2jOCh6d03kiNZaOMNXt5Dh8mJ5pDczlKtNPqS9IrWIeDpDDNDr8rPVJQEVRR3ohoir5utJzucR4MNBNv__WG88vgR33__tVL3WuO35YGK33Ol4dxOxQh_gyEyNafGrSI1SgIbknr4wSm_Ihlcoi9ZV4c1rk2LCuezS0DK70HEbLwKMP5AAVe7xOdOw3qD0ISbVrxkgSrucNVMjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/laC0rWChPFyExxjNwwybvIXf9jCmMkM7wvSVJqu6LSxn6lWrgLy7RK5mbAMCNciogFMWITARBSwxKaVhF8LHzIs0BaYCUleuaSludmgostVLI4cKDCgecxAy89bcnGTKhQ6pxhly5rJ8yq4kt8HvzuYCATtWjMrCY4wFRSBBN85-Xk5cDz2nlBATDPieTh6ygFthSbOx8mAEIPb3YntiN68QkTYENK-b1v0IoA44ml6xfo5lXzXeGlwEGYm7cY0GG-FSlrUEWmPIu-04syVvi8gifewpbEodrzi5piw8yb4IS_30DjUoWw8En-WAinQwJF3Udec35r1xWzS6PjHTUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیرین مدرسه ساز در ایران،  ۶۲٪ از مسئولیت ساخت و ساز مدرسه  رو به عهده گرفتند. حدود هزار مدرسه.  فرض بگیریم همه اینها مدارس ۶ کلاسه هستند (برخی ها فقط ۲ کلاسه هستند)  اگه هر مدرسه ۶ کلاسه حدود ۱۲ میلیارد تومن هزینه داشته باشه، هزار تا از این مدرسه‌ها میشه…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHlP1HsyJfTKYocXEkIQv-hIA7xfY-nlTdiK3RU4BCXqgF8eC0k06Jyt04awDnKqwZJS7mz8z0vCiX2JhRcaSU88PgjR_uFBD_lPlEVTmO_ImEMCXbWVK2uTTQKmM1rhheN4aOj_jgnpHTzov4eoC-wC50FDxvB-MSsBoV32v-BBVJkXR2MCvqP3FR6cVApbTNH-vb2bbtTrI8N597zge1QmnlBZdTDwnxU5WUN9nZbzijIYTgUQ1MX6BRGABJKLqcvUl919EUu38G2_GFz5kqyNywfxgqu4szq5GnpzIZqDF5chTLMaIV15CQZ_R9m3gA1W_e1xckmaQ-hwf2WEjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا این متن با دقت بخونید و قضاوت کنید:    پدر یک خانواده،  نیمی از درآمدش رو صرف مواد مخدر میکنه،  موضوعی که باعث فشار  و فقر در داخل خونه شده.  مادر خانواده ، چون بعد از اجاره و….  پولی براش نمی‌مونه، معمولا از بقیه کمک میگیره که پول پیاز و سیب زمینی و…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6523" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6522" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=R3p2pXX1aMnvuSTe2HmFAILQZCvu2uxDo23eAQJ-OLQyJOLgp9XkcDv6Gb8ZE2Z3fdSqujeC-jsc-1z86HRWyhSSPYpojZAwwL7zvUk-n-XWq_iKvVyFKjk2VA3xy5AtOy0AlE24rsA4QMoC30CVweZEGzzQsMGqYUFAJaH9PsqNbAjTAS85Hyh1Rq3a7UCoy_omFUkLUGXPzJveHoZ4CcutQCFoRDlA07ltiu3H5AwZZlBh5Fr6TQ_sJwktNjoSFmfY_Jac3lCZfZVrG3Jk66xphncPs_Z97aUAbs8boic4LpOyluHLNvlimSGmwEQkmoyQCB87yQeApnNyPqMceYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=R3p2pXX1aMnvuSTe2HmFAILQZCvu2uxDo23eAQJ-OLQyJOLgp9XkcDv6Gb8ZE2Z3fdSqujeC-jsc-1z86HRWyhSSPYpojZAwwL7zvUk-n-XWq_iKvVyFKjk2VA3xy5AtOy0AlE24rsA4QMoC30CVweZEGzzQsMGqYUFAJaH9PsqNbAjTAS85Hyh1Rq3a7UCoy_omFUkLUGXPzJveHoZ4CcutQCFoRDlA07ltiu3H5AwZZlBh5Fr6TQ_sJwktNjoSFmfY_Jac3lCZfZVrG3Jk66xphncPs_Z97aUAbs8boic4LpOyluHLNvlimSGmwEQkmoyQCB87yQeApnNyPqMceYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، مرداد ۹۷:
‏همه ما انتظار داشتیم ایران درخواست ۵۰ درصد بکند. قانونی هم بود. اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین ۵ کشور، یعنی کمتر از ۲۰درصد
‏برای ما عجیب‌وغریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند
‏این برای بقیه کشورها مثل هدیه الهی بود. از خوشحالی نمی‌دانستند چکار کنند</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s44PxQadKfxLvxCaCodaUo-yHr-JPItEEBiMzMT80ZIOPyrCdVBnhgOdIQt2BkqfQ0QvunxOMRHkScbPNlf5qwlAUctEzIwPz7c1qkc0-9Ku2B1rIRaoX6AgqXH79vQf09z5LQbBg4n-jImOhNfnJ__o6riA58HO4fKlp1FblXGCScQebTktMM1ATfGMjz-Hd_Z21GZR5pSjawHL5KwzyxcenlMOJHScXHtPMA254iPGHynofaL7hSfFVfUoN8T4KJnVhKuMFTeFJqCx2d9cXzxMgmQe16c22IS0N4Pncy8rPYQUIJxYf7dbtI0gDsVr1i5Y4vm7-EM0mhbJ2fzDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6-S5SiywoVUQftGEguG2RgzZB4m_dxYN8YDZDM0UKm4QLaPkCJkRRwGtrZsETahKMcKvKAzrGugKWk1ZBH5Z9yLDyah5PwG7dfSEMNKvnoVp0XO5gG7BEFyIsB_LG9rDqL8to9YrUi75LxeNJwptsVcwZrcqmbzipFqS9BEp_YTb5LjI5oHEyqH9OBZN3L01GYxaSW1-lR5qSSMjVQ73mtnX1Cb1DXoce7psm7RPg0x6CV26VGKox3s1Xe2ShL4RYFsQ5FQI6s_t8GOKS8TU6L-hZj2pr7wXS8Oq7ezbsYOI_ujXnoW9oY7rbzgXDEPmkkbbhEAQ3PUee46qsN5Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«حمله‌ای گسترده در راه است…
نه، صبر کنید، می‌خواهند مذاکره کنند.»
این یعنی «دیپلماسی نمایشی»
که مدام در حال تکرار است.
استفاده از زورگویی، وعده‌های شکسته
و اخبار جعلی به‌عنوان ابزار فشار،
راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید.  ما به نمایش‌های بیشتری نیاز نداریم.
- فهمیدن حمله به کشتی‌ها و زدن زیر تفاهم‌نامه نمی‌تونه براشون دستاوردی داشته باشه ، از ترامپ میخوان که مذاکره کنند.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6519" target="_blank">📅 22:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zp3pI5ZiqsMmyFWYsSD8gnpxghslisPA4_Xl2cSw87P10m7WJNC-4HIC52HzSqoKdGa3Aex81bWLQSYnKZJayfwNCY5e03YX4atvh-kLQLbkMirzKR8oPK5xc0g6nKlkeP30Ryt1i4Y8f5Hz362luGM9gHoZH5tevTw3APty3asH_zDXjWxlVPQONFdTrHWeEOxEuXuxsvD4lK6IGmMcd2I29KJCg6gjYVEgx2yWQGp9_ZrRASy5-3enMPHdZL3KLCsga4zxVrefT2giK6KAicrSmLFfSe52OYzqJCxE7XZoi_VHfpbhUERWT9_IuCuXBZjI40D_aLGU9TNI3VyQ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPtHJqBDoRULIU7SNI4Wg5Q7zZigsYCkxwmoH1ncvwP686WKB12mgtCwI6oI14MS6xuiczpZAvbBZUil4m9fzQlZIUvAEZjYtWPDRVHa6vX88Cu5BjNsU3WvHd1HNoDFRBhS7uKZBBnJ2wW0nvPIsJBn3Yc3qQsg1hScaWkdSPoG9cp2HW3nT_6jFKLqWKkri7LqNaQMtZqocOlkNRQcOc_hVS5W2zHN1Mv4gpI1fJg62sh4ZGrpMmjoXdb8NNitHJSegNHDTJDjH_2WhDbn96BcpOTi7dXfEUytagXPEuTalKCO80-Q0vcWKtbjmJRM5gURI7Oq-APltg67lmB7Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVBG1O6w_0zInixPVnzaVZeqiC3mBqYFjr6NZTn0mqnDNDbfUkzM6GV7Jjtz30Oco0vj_IXYYxAfideUZr7X1-7Ht4NKKGmCD7-_3WdxgfIOtjBNi5iT1fmhOUdoh86aR9uaXN7KUc6-dyQqFCTErGj8C0_rNkB6j91ATEPer8gjRtzj4yM0M5PZ7zT4cVKVNfViKFWuZIXwUiUqVUrN5OSQWKL_25Hv7IOjeGcLEkD_IJuiSeYWPBssl8P-GkHYz4F08lwEOCWVwmuSOSUbKQWfdWA5hewWUY3LN6jB6nEcOP7gZxgLXUtK5fndCBb5NzoMjxkMW6LxqEAsuerHWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hLnnq1JnXzmC7JPYkpZTxgXs8b2fvlKyw_6ClE_Ryo_6MmHGVE9ugrdjvS4LmOMYzeW3poef1HWcAPev6EVhW-Encz0njRE_YhHviBKcAv9ricQzL-lBNUCsHzTFJ1bH0EKy9FeEPeSFNhPbijDzcNBomNWCyWq-JqsXIfkQU_ZgInlGwaDalI2zrpoBWbwxJtniCmCIuAmKxLqBaKK_5kljDvhDMD-PWefzyUG9QG7oes7fP39qrc6kSIc_9EcKnJr9_7SUvMeNCr73brhbZJ6wvz7DxArjYTXpR-AqeGT2wGXavxucHxS4Lqt91_51yp9jl76woNDEUcZdSK-j5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N2wPQEL2Z7KwOOTV5KHas3MJn_UyS5-wxVpS5T4DYt1PTsbdoLLDLIlnygPjum6aQXXodoKmzZagVRqnbw-vJFzGObmI5AB1QgkphnkLt-g1uVuJoufKMXYZCgcQBLQiS_y20hXOrfRvej6RJTCk-g8Cka1F4TUnvUo9vf1chusmFTNac1rB1nsAkL0Hlljq74gNB29lEkE1UoCN4UOqF6Sh43QlAEPKDqBDj3cOUrSiRKMjrle7fYTV0ajR85jcbvLdot-_k7O4EhcZlK-py6LeNzfMO3IFv-i-B2IsXGkIiK0esofG37mc7sABM_DPq_GsGnSD1V7PYzjgEbEALw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=EZXHawl4cPF3adtpyt5kX8cBViJNyE1tmHI5bRx8BclceOF84fm61UqtRTNlH2sEONS2RVeYbN_YM-pLMzvJEtY-bulfVhU_jCW9nV81ziBkoqXPlOICYmstyNxuTI_gJBRTZ_PiS0Avle7BGRhIv8m2EC4TvG1l8-dOzdqLb41JfjhmD_9d84Lk2LpIRiWzhIpHbibAuc8n08XsjguBPFp1-Hq6QUL2yBKng1B3FnfIP2XmjmFL0LH3Qi0nz8dmgyxEAScalUH3WnrB0zIRI3417D21iXwG5WX1YADGVUn23fL1uJOC3XnWDYqEqFy9q-Yq_wKKLTafwNadUWHoWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=EZXHawl4cPF3adtpyt5kX8cBViJNyE1tmHI5bRx8BclceOF84fm61UqtRTNlH2sEONS2RVeYbN_YM-pLMzvJEtY-bulfVhU_jCW9nV81ziBkoqXPlOICYmstyNxuTI_gJBRTZ_PiS0Avle7BGRhIv8m2EC4TvG1l8-dOzdqLb41JfjhmD_9d84Lk2LpIRiWzhIpHbibAuc8n08XsjguBPFp1-Hq6QUL2yBKng1B3FnfIP2XmjmFL0LH3Qi0nz8dmgyxEAScalUH3WnrB0zIRI3417D21iXwG5WX1YADGVUn23fL1uJOC3XnWDYqEqFy9q-Yq_wKKLTafwNadUWHoWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.
اینها دنبال «اتفاق مبارک» افزایش قیمت
نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.
اساسا با همین منظور شروع به حمله
به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6512" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.   خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.   او همچنین با اشاره به اعتراض‌ها…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=Qhp3XftkhulXgLcrhBLLmYc3ly8ag2CYbmAv2xlaX-45wZukTr4gm3CNbcKCDHwWXhmCbkHT8UqeoTLqRmd6TZoY2csrX99EMO03OemblIA23c-ax9zauO99K4S08Bgr2Y6qXm3Y7njbM4jip7-c0F3Dgsc5cMtiWceZJIeleSsT2qfLtAjhsRvBiGt809OS47-YdTsJwF8SfOLyhFS_OYbRQ3JLsPBWcLD4-rJh4NijKhVtApPmYnOe2vmEzkVFpurbLieVCpZWqYVIinJ77r96caEuqyVGbPlu-KM8j8hV5CDSI9lf8wJPIf5bFpw-h8QDbzlgQ38ERWkF-UL1GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=Qhp3XftkhulXgLcrhBLLmYc3ly8ag2CYbmAv2xlaX-45wZukTr4gm3CNbcKCDHwWXhmCbkHT8UqeoTLqRmd6TZoY2csrX99EMO03OemblIA23c-ax9zauO99K4S08Bgr2Y6qXm3Y7njbM4jip7-c0F3Dgsc5cMtiWceZJIeleSsT2qfLtAjhsRvBiGt809OS47-YdTsJwF8SfOLyhFS_OYbRQ3JLsPBWcLD4-rJh4NijKhVtApPmYnOe2vmEzkVFpurbLieVCpZWqYVIinJ77r96caEuqyVGbPlu-KM8j8hV5CDSI9lf8wJPIf5bFpw-h8QDbzlgQ38ERWkF-UL1GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.
خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.
او همچنین با اشاره به اعتراض‌ها و تجمع‌های خیابانی گفت دولت مسعود پزشکیان به پایان دوره خود نخواهد رسید.
@iranintltv</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XO_31-GffYxRHysHEluPKiLTRGIXcmnPXKNmEhQnlXVWhr12MGd36-BCY-kqdqJacwwIlcZ38T2cFhEL-xqo3VXEmPU5NyLnR-nsdaklS7OPfOMcTIpLdNVddp67Jtti_4xJYgdqSWIK7inSGouh5z1Qf3mdDeKDKTZij8R1Kvw_5cQsabbyY38Mx63CAzx4C7qUnTJ15iITPi7wkE6kQ79WqEm_lWKqy6D20oasAvNwVn6_AXPA8wtdaw_TTrBSgXiWa0QgKUKAns3AhegzbZOAGNHV3GhB3OBq7IzgoDIlFPW_9lstqhpMibF95aFKt-PaRvhIKH33Gfua3XiMFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8AOZj7Daxq6BIift4KJnY3nmls7IYNFux0k6xdwfLon8Dro6mvalQIghrQIJynTqfY34PWQ3o28pJmy0gaQBB1UXakuv1rG7HIHYia00dMLB-vMtN0jrZQkAGA7G4jnoMxCssSguBxn8CJA8MdDKsBgfYvpIv5Wbs9BFCs_7WRIb-9Yc8P5WCcy3RV-rSTB30pJVq7H3RTQUgX_PwPe7vHjt3Nob47MqDDqsiC80AHZ-uPiB55wpcM2Xx9w7POgFYy4-iWg2CZ1h0WL0y6auyZak8YAT8P_YSQL3MK7DHXKkRcIkQ_uR6HylixjAAXOGzUsUMLxrrVxHx6WfvIlLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSIoJfpzgdVsov4-bRYLxhnQn2UfRKvQ25n0HeOrKvMo5qASWKnVey9CUswJZgLDf4QToXpAiDb9MrzwTIsNYHHmo3Sl1LEZAcsx_rscC-7TdIDv1tHa1PzUNC_jPJbnk5_UfCbJ4DSpjE9JCaPNlwBzkRHpzse6-Ftzx6kEPjpB1a5Q0HOJO8aBH1fvLvg41HCOPSdr9JxgKOh2zD8CmNFikqnyvQmE9StFSCCzJy6ij-2Yt7naNPFWKn09_hEHeWo2QIaYHmcx4YWXI3b_wFl5A1GTspZs69mYZQU9fR8uHx4yRZtqsWSqOLaN-dKshcpvrxUQ70C7NTzIekiECA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBBCPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPQsShpvqtmZSPCnScriU0xXUvtXFdMBWo3PLQmsrclZIxWc4doKdNsCnhFWXIjHkbKjhjtCz0PazjtRYENwqb661lnt1CmQVp9Ndq1-ZpEwt90gGdb25LAbq-jt0MxEKeUMNr-7ONcsFZIFmvm0lgzyCz1-r3W87J6WHOGrL3ivHgIotSOe-I9eZLs73z_86pbxlrnjKbY1f9LXMJYw2RC9mNqau5WTnG7ZnlqOt_lkWB4fl5vTU0tae4XXC4qRp_a6bqlGc-K-P4awvVw-RGXPrGCoNrEySWF-NTKrvSh3A7qWA6K9wM1LjVlQa9gFQ74ONUfkhQ1TyCSPRCcX8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29785e012.mp4?token=RNeY3eSAIqY07rKjIrHDNk1Kj3EsJD4ODOWZVdU7bYMeZoyGG8ozX1vLUb-gVfuIyMoQPTWoWkv5XfTM_KGpW7TzPHU7tBMXwXnKw9f_2H8OYdpSD8JEs1N8AZ45-INd-yelnltJ6ZPCPz2IPMdLooNcZEj1HJaYcUyPc1mjJn1LSXO0Hljc349auTEOJCNih1AolvhfbAJeVBCaLzmv9JpaFd4TPNMoFcVoyfBvlGwG3xiaSaBtcMjCtN6poMQ4Dr-udJ7-O3Ew_Kj29xThFVKeLI5c-EdlDEMkmSHt9yFZXfwHQNknskZlHCwpwZCIILwbBGf51oqs0Qy6IwlCGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29785e012.mp4?token=RNeY3eSAIqY07rKjIrHDNk1Kj3EsJD4ODOWZVdU7bYMeZoyGG8ozX1vLUb-gVfuIyMoQPTWoWkv5XfTM_KGpW7TzPHU7tBMXwXnKw9f_2H8OYdpSD8JEs1N8AZ45-INd-yelnltJ6ZPCPz2IPMdLooNcZEj1HJaYcUyPc1mjJn1LSXO0Hljc349auTEOJCNih1AolvhfbAJeVBCaLzmv9JpaFd4TPNMoFcVoyfBvlGwG3xiaSaBtcMjCtN6poMQ4Dr-udJ7-O3Ew_Kj29xThFVKeLI5c-EdlDEMkmSHt9yFZXfwHQNknskZlHCwpwZCIILwbBGf51oqs0Qy6IwlCGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اثر یک انفجار در جنوب لبنان ۲ سرباز ارتش اسرائیل کشته و ۷ تن زخمی شدند،
ارتش اسرائیل دست به حملات توپخانه‌ای زد
و سپس دستور تخلیه فوری روستای المنصورن را صادر کرد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUENDhwzX6ulAhQvCgoRytPZzUgapcGW2O5FKmmhwP-aTUmq98EgNtNcXV9sOe7VUggV2tfM7A1r7bHsD-r4ZGVxQnG0WRp74QdxmnZ-n6zQ2wdtFpGaC7b88fCwIdAK-6ccTNCs1go0zcH9EJWvgMvzbjj9Kdl1kiYtdbghrkrGJC464ttMD1_t08rsZL3jOahfs4N56kRoOFomcCgN778YPrsTaw9rJ8uJ59TbZjgm6dn2kCtcYTYKz1qYhZATts44-_Hvnd7qME-40veNGiYc9EuQqVEPsOpqetafv3SOk3zjudIg1FCe2Izj2BcPTrXhMgC_T_i_wS-J3O-SJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3Zj9k7bblUlrU1JX0IsEhGb0ua47LgJ-Um3-v9LPTO79BYhADCVsroJyeVpzgbq1wKJfkhb5wdhmw3xG6ClJNEIqYH52t5AR8ZQkvucPO_9nUVi1FYS3o_FXhAXtqkhQz_iAj32fWU6ZAH-lP5laUOfIdKhk4zZWSZqEAECO69Eo-a8iNr--WfChBGnUCsTNNY0zdKxdFy_9jT0m0F7sJNgyGF59ksTpbR0_T2pAlB_AZnb05fTQJXmYgEli9xl42rRUeedZlCX704ughNXhGwwak4vvpDYDVY7eJ6UDnPqw9YCqUHD85K-SDApOkoNQnKGe8I8hiUI_SUsMmBPlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQ2nCbVOs23aJ7H6WOTb5l6zUXbizpfiIPyIxsL8nKBxezBqYmMbN4I8HGOPqtiserFB9g5W5DDuJrVn4fJMYYy0CJLddIMAE7ykeAEmgfrSylHkoksLw-3se01F2LvGwNoHqkfj4Cr8eoQhbX7bu5gH4oApH97uvEM9RaN0_Fs_wmocTisT3cyJ6xXDqVKve-hYAseKMHgm_BbTXSbvNwezLHauirI5KcAX-kC3oI4mSGfFQpy4si8U4loWSRnDyi0GnsdxstujQsqNG2BSc3lKcB2PdThSR2WmCdR3KoqIFA2_tozdH_64tt4GXq_PBvFUbqoakRwLbMcjAuYfsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=MsoA3gHJq8R6jeRmTpNzghsPq2dHvUm5ZaD9xMwhyjyVPj70Z2opvJbMfd5UamICcnqy6rzmnX8v5Cdt-dbWp96D79bSmldE-BxkoSX2ku33706gxLmMkm9kHr-29UOFRRfmtnsncdqqL98XQ0HFZ41du6JsuEayCLASGgskJTw6Ss19yoZtwi1-9AVGFXc4nTp_yan2GIFqwzJQhR5BmnJ4nnUQHmH21Le5WvCTZuDM7liKY9WT46nXi3IAURDTDhkMdj5QwLWURLOKO3na15GrfknaaupYCV5JlS7dokRbWDqG3O1C7PIUZS_4pm22pFLEJJYflQN4nbOOYs7pwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=MsoA3gHJq8R6jeRmTpNzghsPq2dHvUm5ZaD9xMwhyjyVPj70Z2opvJbMfd5UamICcnqy6rzmnX8v5Cdt-dbWp96D79bSmldE-BxkoSX2ku33706gxLmMkm9kHr-29UOFRRfmtnsncdqqL98XQ0HFZ41du6JsuEayCLASGgskJTw6Ss19yoZtwi1-9AVGFXc4nTp_yan2GIFqwzJQhR5BmnJ4nnUQHmH21Le5WvCTZuDM7liKY9WT46nXi3IAURDTDhkMdj5QwLWURLOKO3na15GrfknaaupYCV5JlS7dokRbWDqG3O1C7PIUZS_4pm22pFLEJJYflQN4nbOOYs7pwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=A2_JpxQZP7zZg-SKLk_CjteKkc1nc3-Ao7KwhEnfbuBA4bvDVEl70vbyjAb_Ur6e7lXxm6R9wrr7pJWzeOPs8oWdxDCCbAU59gAS0P3rhoTUU_WD6_y24H_qjhJZjz4-cnZPXukgyvGqonwaJGkhgYi5OSOqm7dgxbk5uoMtrrD_hKpRANd6gr2_HpSJ-xNhPf0q6vdmsI8t0GNE9R1CgElmcdsAMthdqj469KQ21a7zmIhZgEUsPdMv-jPCne-6TzwlIVN4iGHTiJCkUgM8Ljp33VQCnC3wkJvT16aAGgYKYfYMqxFXJF7dFKhhw7pi7b9ohJTqXa4HkJ6MSqZABw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=A2_JpxQZP7zZg-SKLk_CjteKkc1nc3-Ao7KwhEnfbuBA4bvDVEl70vbyjAb_Ur6e7lXxm6R9wrr7pJWzeOPs8oWdxDCCbAU59gAS0P3rhoTUU_WD6_y24H_qjhJZjz4-cnZPXukgyvGqonwaJGkhgYi5OSOqm7dgxbk5uoMtrrD_hKpRANd6gr2_HpSJ-xNhPf0q6vdmsI8t0GNE9R1CgElmcdsAMthdqj469KQ21a7zmIhZgEUsPdMv-jPCne-6TzwlIVN4iGHTiJCkUgM8Ljp33VQCnC3wkJvT16aAGgYKYfYMqxFXJF7dFKhhw7pi7b9ohJTqXa4HkJ6MSqZABw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=PPKjeFKjXJgpn-4sCG6ntzl2qos3Kr9d32y_d1zG_41l25VNbT8YcYmpcJnQsFc9tEldMHTtqiHH52XdfX4uZuwmFqA9AoQU-nczQ3tgsvJhIY6jO3gRGP9pG3d7SP0u2GFphTfgroODHx944MqmdiVIgehdBMQpJnAdNBw6AfdluirrFzU2tPBbOSGh6-uPau8r57HfcHYkIeWzRgug7e6pKq8h-Tj7e4tg9RNXpaur1HkUjPQON1iWahOrZZct552wVNpJk_7IT5rI4hMJAW7VwZP7dmItwSrGbKkwIJazh0aQPMQiiNt4-2DS1kzowatOKhK_-6rLDrllSPe2Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=PPKjeFKjXJgpn-4sCG6ntzl2qos3Kr9d32y_d1zG_41l25VNbT8YcYmpcJnQsFc9tEldMHTtqiHH52XdfX4uZuwmFqA9AoQU-nczQ3tgsvJhIY6jO3gRGP9pG3d7SP0u2GFphTfgroODHx944MqmdiVIgehdBMQpJnAdNBw6AfdluirrFzU2tPBbOSGh6-uPau8r57HfcHYkIeWzRgug7e6pKq8h-Tj7e4tg9RNXpaur1HkUjPQON1iWahOrZZct552wVNpJk_7IT5rI4hMJAW7VwZP7dmItwSrGbKkwIJazh0aQPMQiiNt4-2DS1kzowatOKhK_-6rLDrllSPe2Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPXumW_DdVUm7o326rtZYA3JrMhU2cfiVGFBnrFCo3f8LsrRqXTi2Gk80XGIjDTY3cKf5D6_P8QWjOvu3ACInNey0muchpuKrxlWaYI0FiPF0WAtFWWVyACoV0owc1VdHEOY-Aou3WSMRefcv_KnnyF5KRprywoa9dXUWjdSBYSgfNsUEbuslTjrle8syY_-NFYfZb5plZ3Q3K0xEYWOw2vblV9CbzoLcklnTcgk-4hBkZZLT5Cadtntj_0W0fau-11mtWxNBtPSzS5AL6cGiGUUpM8ieg5B47zEIJvOeV0loOrPJZBaFAOs5y8i_Q2Ave6syVrLcXNq4LSIQzgU1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgKmoEzS_0MkjSqoFN29oAjTY_6ID5ex3tZVznmVqqiusu-Q5Hj0ctwn9dUa8A6NCJcnFhxuWdYaJLvzKO1cB5YgC7y2K9FVrPFLCgVZiTzeXy5fd_l9N3Q2eJ-NlaKNmviLTN8H_jlgI2NHiKRCMlvQTF9QbgjIDtRQ-OPXriMfTR7qIL8rj9mZ_PLTA3u8fVUkg1PLOX36IQWfWQJBMA1fP-V89Ru9j-fLLSOrpPe5xWyQf9s2jp1HRT1E9yHIEa0ddALaI8AulpV0rmPFtjD3azbqDFoRieuUf7RQArU6CzXTozoot-cbLolCDRJxeyTFDYujXfuA9Me4_TUz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k1lASgsR75B1r1Sggg61_-YyT3Oi6cpqtkYSorfyTqG7EQzGf8Ghq2ADe8XkUZKmg5zvcLUCSSYG9P5hHZZC3hrFOhK_dqImBLzGW0uzjuaHWs2bbrbb4CTCYp7SqCby_m7eqQNVqytMX4sULiFdQBcBUiz5Dtb1QO8SSm65RjotQjCRjdLH2CDGoes0EvEVp_4vuBefahuFxzjKKs8L-hYDj8GC8CusXqHnj3wN3GVAxN8aewZ7eexVh9BYJuqy6yscXMm_Zw8crMDTrTASYVG-Vj9O10oUQ9D2eilmC8BjOpiX1mlkxlUm2o4Vb8YuWzT4s1fi9icA6a3qjThpkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s-d1K0YJ4KID3PzunAdRdCaOaEhe2TItHY_rgVXjJWRy5aPyWHYh9dnU-Kwz8U92a5YgUrG8p489VGJ7YiO6ctKxGofdjG9ZeS-telp1WGlKBRhYAYBSK8sP9lfccoFbrhPMUMqJb8p6hgC_8jU5EDPm9Eq6xgooo9R_VlGOb4rWRdfd692wITPh_lwH6dkFucMjBOzvsvgcHaHTvo0nTh0bTPuCrOQiO6HIGXrNTQwvZWWwkF787KfmkyivBm7mJOrU4RRaIzHu9ynznH7FtCU2ODeInRFEOjKJeeLraicOrDjcy7_wKFjyhYE4N129O0M1pjXuSttu2f0HcSFq1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pz0oYkFc08Cqv1m5YaFZjHVyqjkbwEgue-sQRFmequryE6vwq3bKbQ9t94dkE63hsfLvPSytgm--FV0xwnhcQWZrYfIodTlGko9VSJphJH1CcYzxAHIqymJ_ZXA77yiFpQBvwtpHdqiB-qyN23N04Qxkr1yYEojAIR1LkNkb2RA6sw0yvY0H6OF1tSULr8JNzdhzoemzr1fXk14DRR1icIfQxXFbEBgWEkgK5DAJPg_jIov0tpt8yiN5POCXr_b47OQiUV_eH_o_NgPPJrHlybEPEPJuNrNKQ2SdQNiDHsd5xt5Tg9TKyD-WDov0_X32UHGZhk3iKAs99XDofBgFtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHKjgcW-bEhiysnhsxcxKcVydjlUB9-mTTQ4zgP0cR8szUsDbKCSp2wC9xiORLHEinJsi59bhemH3Q-eVSHPHNatcEs8HzH4X3sEEyWq4ttm4SCIgeQDJMvNQljtwPtg1L7PEUc-0z53E-TbqEJBFKDPWS_oPTzqMvGq1qXM_AOgVd2XxDHct0shmd3hFpKEowgM7LUj8ejTy_HmprsHKp-iLiexcZf_d7U01Gh8t9H5nqwQTozI-7Tamjwqyy4rkV7aT_1AtxanbosqvVW5_NuTCYkM7bBpZvtkghn4E_wgYF6ilCDu4yfXTi2zApqqj5iQ6pWbBDalrTYz7QhgIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RK3EWujxzDx6ohTulXnv2HaYAc5C8w9J73-hiPRMefX3brqwxPEnJsUvfFOJadiIHHcFyta2lIVPn3KxCo63whij_Wml2hcN8DyuU37_2crjpvVWrTy6CEAGGGjLQ8IgvM9_EkdtgDUKnO4b_EiTSTXG1f8952yhoJjhcQp6VZPtegyXPumPUL6KBmdsT7Cm_sl-Bu8YTnPoiHicg_y729VT0kJtT71F4niErHdhRzPek3VK-DbbgM_0gn9AU0JRZ7g5FrpogE2rJ1Y2QAdOKb4s9GCrSCDAP4Xa9PTQQDS755AisujFcnqS0rQyqGEA1EDju8S7fcPxXkypIph94Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2htaFih16vtGRgJYq-_JHU82V3suJfh5L05Nf0mgVYxLmmsLY1hfFj4_GuLRmL6p-bG2fqTLTNQyxgxSNd5mm3-COohLjSu9uAT3qY646Nt3ByO4vXo6m8dAc7XNL5zsD05BdHeRxzmey3B6UtNlmZvS6pIoUWvo2LZUvSRelW7SXnz-2IF6bqto1YW0YPi5Hc1EynsDW6rWu-6kv_ij9XSaf7hu8TqpF81acI7vr41l1D0WbpIuPwJQ8x_8xu394ZZTu4sEvYnqIwZYEWAxhWxlfnsMnyXvCIuMDAXLnmrJmf_qKrguo70xsTNrDianWYULHiZJUyJBqxPn9Lcxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRUPzYbSleBGcuCgY-AQn13MqXybeQ926sJmxRiH-hxu_pXpVoLjftJnPXb1_VvvmVDLWPrJm95vTSCfh5WChHeoGttD9uxbCNUn61lNvpAE4sZ2OmpyYpnXJ93twYHgcfwNqF7CjZ44qR1Fg82goJLNRK8InflGj7HOu2jup7yTwHTgnQpLhw-C_COCbqybszv2NKf_bVZ1CqQL5yzuFZ1r2dPCG22tXiTrV2icNnUs4iu_VWkMJWRyMV1mhd717vkJZaWwgm2JuEig3s-SwR4SRBimIZjzn5f33f2nwEtZmgmw9sP-922nexehIaD7NNifSBoE-D9TshzJD1VOVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ig4TRqCW12SJnUSKxDpZ_OWFohSd6ZqPcDGGhnuaPKKkVGDMKQqlRBLKNOMKRfl5zVmYodshDTkWDzxVyHux4pSiBl5ZAKzJr4-nUjYpoxtcfbt_mCtzYYzH-5EZJMpUVWjDR51KBTqYLGdUpXzy2X5qYEJT92KgRMWvEmwqRi8nERkME1oRk_9HDenXNkEucjM5zmSk1QhuWk7_-vC6T2fOJ7-TOWm7z1eO_rr4gNnFqYWNq9PWcPWDghNQu7RtIsWzLIiKvdqG-6v8ckx8B_oYR9DtW7V2hSyUivvQNsHYiNgEfV8S_5XJtFo_9oUI3MXn14Tq9q88Mtd4oP8vqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAvfTFGUz4k1PNX5CRjOBgVmUa6el7yaq3Opm-KA3JM2LV_AQZBekDjqetYw12pAwwJXa2FLMVK_38-6T2Gm1G5IPq7oLMKm-glXUSA5__oQMV-6QqaHYprTMum-VrTweInASuseZYvYy6GcHxaz1rZWEPx9mH9vOPC2IvmddMiuKZZFTt2wvYGo3O3-CckGAr6T1szXPJ0KbuNHmtO4YCWp3fGjrymGvCz8_WNVAUXHcYwjjqj-bwOTC9qiauKhvC5qo1Uai-kC5ez5uG-4uPajXWgf2WPe51rOatT9CTkINgWmdxHIl2e7mT0xHdGmD8VpgVzcrhXbKVyNCNOYJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMunzEHTF0GIYgRGqOjBHp7SX4rpioEXWafnY6KltRS9Qv9DxtuvU_A_keRyzSzp3SIMY3Q94yxi1JLsoEupuAkjlYidcBdWVPQnw5IXNHeLmrZXrDY1clm-tGp4r-ZZnmla37gq9wKo__gdIzMmoV6qnP_RVNmoICqPG01V8ACj5bLc_Ym9NpW4kAQbZu-BAlq0db1tq2PPqIwuF5M5H8YY_FITVZ4qoXHX_yP4PTirVMnlbgUMyxoivJGiIFaCnzGIEb_WF8SbGKDOfb_XomJewQ0YZxHfpsarUj0P2UTYjm_0o9Wm72FlucVeE87UW_jPSqye_ioyEBW3biBtGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bg9Lsw45VTMz-20nq3dlXED-wJV_aPX6xxb6DwNoqkSpPKlEGGXQhYTVEgzPth2fz21jmt5D-7PY8pnYac8O_OoZZjsp47pKrJmyuPgrG20Al7qaNJMVjhGrWhO8oFjyymT9NMIby4TnMKP5AYhS-7tC_yYrvIuiRBCbnszfz2eHjBbO3rCWpEKQjMfcQvgRT3SjwD7zQRYVfnpjDSxPsFxpUdlV3WvP7jni8XCcAoHeFxOdJrNJJD0Ij6zD59Y-gmajVdqs5rxtcJLxK5TfpvEpefk28uw2l8qaBIL3PHwJdYvk5GYnUnwBveo9dAvknvPGXmsh8A6lEUVF5RNxuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_mGrlFqU2Z1suceYf240P-_-yltyLAxftVGF0xhyh_0Lh0g2g_nbB2VjJcRTSfgvNbD4UiLLaaxhB9V0UtENLTfw8nnzcedRmHzfJXJd2cQdWsoVEVRS8uqdYs6f0mOvuD4pBwyE7ctVnD2Yb65QFnjAwyvCi3oHTffY9C0uQvPFnAAkNCFKHl6uc4J9TOPhpVdVBp3bUdU_i-OVP5BHzwb5NvhRAz0efT0sLIPHG3eFXGB0arE9xr8FJ1LubPwoyNvwmmRD1otNFOMFdcAJRQ7gUMiyzY3RhlAE7DNI4Bw7eWgyx-mEI2cMKSmwFW6u1w7PJVOE4QmQQ7THlWdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=kSScr7LzBsGDiqh4i5Td4weTIqzOSfB7bynHIFgMPivyG0PmDVHGnRf-94qs6HWfIdd6CKwqSTXOzqKTpXqPplEfCsPFff1DnfVwFsv8u9SO_XQiDztUy3QAAtYT_MP01haR89P4uv2GPU1fSXoVDIfnf-0THzOp9peFT63VTwWYeDI8jOJMf-f6cnNB5TU8z0W3cbxfdkui4lQ2oVckaqUQN5bjC9nUAp75vnNNxXt4uvV3qOJlKkZtQyxaksRhP_2oovr9t-GCqDrXmhO6nWXwIoDKxxmcDd4Qma6kgv44RWWYHG1UUr6WYgqFrvpzurHtyED4X14E4DjCJbQyzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=kSScr7LzBsGDiqh4i5Td4weTIqzOSfB7bynHIFgMPivyG0PmDVHGnRf-94qs6HWfIdd6CKwqSTXOzqKTpXqPplEfCsPFff1DnfVwFsv8u9SO_XQiDztUy3QAAtYT_MP01haR89P4uv2GPU1fSXoVDIfnf-0THzOp9peFT63VTwWYeDI8jOJMf-f6cnNB5TU8z0W3cbxfdkui4lQ2oVckaqUQN5bjC9nUAp75vnNNxXt4uvV3qOJlKkZtQyxaksRhP_2oovr9t-GCqDrXmhO6nWXwIoDKxxmcDd4Qma6kgv44RWWYHG1UUr6WYgqFrvpzurHtyED4X14E4DjCJbQyzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6BTb1PhRAL8W7unk6NTWa9ghFtvLEIUOQDX0MtD3Zy32_pp2e2VOhITfj02LT2MTBEX2C2J_T3ioeKigFthYnI8wILArTSD1w6-DWOLR5_2RH6MFPsj4PYcQxgybdbZhTNMRFODR4h6McxhNyIGUVlLaqp8ei8vwzBR4ZdDHbGpYcWxhxzLR35Rrr_YvzTZkYNTEMBWxWC3YxhQdx9Pa6opXL8cNDFDRVaKvQHdxQBJszg9UcUBxSRLYZHgZOE5atM--aBfcCNSNNT9SW-7Kn8pgMVSI2q7W0IdzyNTPd0c_LHBJ5_Tw7J3opkVQSyIDTg0uGkW4CIs4GNSkwvkpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHZFjaWTDHW7bufCQUL7w3LjAdAGkCk_8-L4nZYnOOKZP8UnkgX0kVYHSHPk6iFWU1glpTBzACJkHiHqxuJCk_HwloQ4TDa-FKEFKdGdgpknGd_3c41rjZl1neUhGFNr_jnUAWK8wW4wi5eWJ1iWpVNyu6WuEDBUWu_7yuqw-jt-3zv9pJEoV5DaaSCeYp3CqX-27SjpZaadbSXORoKLth3iQBx9_5g_aQk-bBPtw60pmzeO34DbgRIn7brIVIOR4kgpd6U2-wE5NcSZRKglqdwNhJaBo8An7Sya56xA2cd4UKTlfjcyhXQ5VIqTqWUf6OJq8LZgtoJxm3ZfYcxgHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/at4AZTiruIS5adwL57l2ti0vIv7VnxS-71EjDUQE88p8z5f1pOxcaO7zT9dBlXsvPMjaalsN9RcAVUF0uz3yPI4gz7K9fQh7p6BBH9VVQNNC3tHAwJrhFhrneWqyzcnsVEDEqDDFFnU2l0buaXiUppU_npuSc3KqzWJEfNV6TMDe-x85h1v4rLX5dEkaMmgFF6ZUVv6UIrpRqcQ0aXnQfv4wtpxb3BUGcR-OwoBRsZcunEIPDRfM9scRwbOWYo0tQWoNTvqYA1GWU1MI8T3jqYxBACRujTsJIMJUUrpUnOulVNnGXoGyKRz7IP_bIVJU1nSfM44nxww9SnbAVsILYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1I3zDKZ_HRhVvK2mbnP06Pmu_hmpFLVf-0tEYQ0AqhdGrcOFCwZijpiou018kGLiNyhF8OAAWyfW97qFnNxcXpvu9s1J6Zx-ZNZuIq9ZboBdjh_ku6Ee7ZReXxf-m4T1Ymh8QArezUYo5JC2OACP0t7YAbmlc8dRff8rn2n0ik_RdxLjCC8YbKivm2mI1c_VCz2SQf_NFB9xaON1PuzJ3W1J2MQXUI23QqfHtzhVj1WSf5g4ZdTuZeapr7yfA5FRGRDnFI_-im8aBzp1xOrDNNiBXYbcb4AEBtycfjRmK1putnakMujN5auE_8JDijgDNaR4m2A-_iFC8-I8ABohw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_8d3Wd0HqbHzfc_cmW8F5-q5FV_aUBraggmU2H14Z6tcyobxifHbnNfEU3tdb1WgdxA5lVA5WGWcPeC8t5p2YPaX1OMym7uTWASuHUvog5aH5-zrTFhsuCI1JG80u-ZFh2-I8lJd87EqDFmpfzD2NtmCRvBChVGWBUvzy-NeWwYLAXJZDrgl8tUtIor4KA_vVuvFkGztNhBdBTkODIw7ZYCcJcGWmr3QOgaL4Icw_bnKpLmOncevo8QpYxqrZRSH38wzzC68SuB6cs4HCUxRXdFU-nvQ4oJZ1Et-xQVakpStRPSuHaOEWtBo3MrtE-H34TJrFwAUra87pFwri27ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mI2i6luwat2v-0ILCA_zP3QZIZz4ZiWtfPbaupqA2bAFjkeDzQrxSatJj6VCWfq3I1j6OzQwiI0AcLKVSt76ioY5DzfpZy3cwtdO144FnPU7Y_aB-f4Nb85Zr8mkV721PsSVbM-wpuLBcXY4pj79OTA9iVnWwAB_pB3pCIq1DU8e0A1ylPW6XqIEbEewjpHY4Ugh7ZJc0HTd-pVSagVNx9eBjnqCAca3noNnAlqhQVD6TfQU1jCf-xFnBbQHAhkEDilC46YC_lIdpvQJBkkpnDPZWBP_b3SPKbbc-Lv7iuvx-z4LXUw0In5eoH-Z5sj7eMIucmB2Jz9Y9QFQteTCVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZpSnUremJtdTlceq4ruS5MLz4UG1yhm5O0MUiVJKtuR-8-pM_XLH3eynLgqHnBjWnNdp_n52j4YP0NIhQi1tT12zxmxLsjBnY8w4KSlxS3ZFhhqg8PpC4ShkQVxSOSjh8JgeQow8O5wjI-7he7LZNhGxK1SRaqWywQCo_4hoU58loVXif4R5522zVXCTOOA6uMWhrImRN_Qa-Tmm4PwDrBCl3SeCDRbDJonOmxk5zeIsKOkTGQlPg47Jc4-Q534YF_upwA5_cT2Dzaib_QBKdrSbBLwrbGeAtE7UgAgJ5N54cUcM5iAIryoPHkL5vb6evOvw9rLi8ZSOAlS2Ne1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=u4v6mMbtNcvkt7kcDHlrUAWduGMQrCOk5L-C8ggvJ_1CRovFOMgjTozNIkpEyI2L6zrnIG5sy6GS_s7zpzxg3944IEGuX-5SQ46rqZkt246GU3ihko0GkYz9Rg1wNqqF-pruLxVgRZZoBNOV0eo6q2cnbd8iUvQDk4kavwsJvsdZ-cnWkun-gMNiEu43p_XVsR1L4rLEPAAgyZJcvXz3qcEjNmM9wy7Bfo8qstp_WG5zyGk3qL7zoBZ9tw-k0s1KO1BjmKdL8z0ihP_zMvPSoBXahWj3vz2DdPEdNaaEMWAe3wEi4jzPpWDN5LKcoEHWb--L0q_UqNCGPAYSqS4sTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=u4v6mMbtNcvkt7kcDHlrUAWduGMQrCOk5L-C8ggvJ_1CRovFOMgjTozNIkpEyI2L6zrnIG5sy6GS_s7zpzxg3944IEGuX-5SQ46rqZkt246GU3ihko0GkYz9Rg1wNqqF-pruLxVgRZZoBNOV0eo6q2cnbd8iUvQDk4kavwsJvsdZ-cnWkun-gMNiEu43p_XVsR1L4rLEPAAgyZJcvXz3qcEjNmM9wy7Bfo8qstp_WG5zyGk3qL7zoBZ9tw-k0s1KO1BjmKdL8z0ihP_zMvPSoBXahWj3vz2DdPEdNaaEMWAe3wEi4jzPpWDN5LKcoEHWb--L0q_UqNCGPAYSqS4sTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGhkHMsyfeOD_ABxn0KC65I5BxYhHMKdxlaGHDsq2kieQ3m6-T-15OaiUrIF2OcuOFr-g-iiIRjJmmE9xme8TCXUVWyyt3dQAxlv00JAntiDyECs6k9tLtjZabOc3pnc9jXvh1rwCS6huyaL41XWDBZirMyrjKGB2gqLrFUlENEfZylvnKCqouk-6pEwvcQb981OC2DOBbVT71BPwDunMzs-8F6C-y1qfdNGulpmHfkw7BPMhh77pcGI_EAA-WSNCXC8C091ZfRlULMGj1iN7OUURKNfDO_Lwmup664jV7W8K83R0byJqRCr-kgbd4g09Ahwp3bn0G_Wdl1Ps84g4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXVWd2o5ZRaB8ZaUWkzfwmv6h63_PDKcB46tV-kK3ty2R08mRSSiRgVDheQTpww2GVJlt-nHR_xjxVEKDQU2QXmpQuVRkkwgzlUKwwJhw-FeFyx9YIB8oZF3lpN5YUKQX4kMkZUxHp2gxcBt4DaZxZFt-296QTtQNhuqvt5TLsVZUUFE0DcnPrGSBnBLPEqKdFG54yritCHtOlztaM4rW-jaK7zXEY7AAI-IP5DDwcn5ASotYuzGYpJVGjdmkomih51MROCLV3oImLZKwN37E79sn5-yYhVuNtD_o56OHtWsJ_63HYaE9sssFdjxAd72kF4w2-kHMipJ2Scmtl8RKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGpDE_gkVaorOLIKbCoQuhTWj5XrUSbMFAiWE5Hj7ARyaXKA5tv4DzMqvF1oKnVSGSumF_pjayRLzoFBy9MJXzoSaFLQaYfRajw4EThkbzY3x8f53mrF_S0ArmKNJ0YBN2JdTzBkJeBYjEGlbI91j12ERSw-8l7-WHVaJA8tLQUZVrXKJ4_TlQTLV4EEjML9RNWwfJp3pZVQ8-tJjhPaPgM6lwK6isWgOoJtTvExmzGUurz-WiZ2H5NZK-itcwlZW6nEdtO5tkTM2gd_ZEoL9TlpZ3auZKKccESMaXmb-MU1ua9bY0_Df3EpA-CqMiSfJHGynUuUdMzTiyiNqaawBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yzihn5lROeFBrar7i7AuvFT9JoY6vzsORPsBvjkm03papaU1jT70VY0SfybmqUePojMKNq7FFWXNCdodkpZ0ggW7cMmwlTbc-tOmSti1WrkXRHk2CU-ArSRjeNE_Fh2I-MzqFbOw9BOI5ZgtP_KcaDFTYnm8kheQEikLolMhdu-XatuKSEHOmvmRPqImGcPwlUDgW73uNJ5_ci9mndYa-zvae02v7_0iuCxip-Akyvn7Nbi-HpGH2RCa6QLXkGsyT76M8OWJPqNwJU2T1bLtzpN_1iGMiHEcnFBVxZ8CLl4s6ZrJV4Gz5-GVStSzzEKwNzm0fmH22P570X5RWnDg_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipEFPllSOu0mlqMVVzHZboDoqpgbiXxCETGIdXRliPryk-vP9pA5R0FKLeudh_eKXML_4LAqnr2GMaWMU_8j3epx5yqfyc4USytPEem58hlAtKVdal7AcGV_7DEAGHY-KP0qnIzIQGKq_RIonOGq8Ey5P7Own7go2dpRWz5znnzHVPt2uu2VqeSvff0zy_xo4P2YH2tng7tjRRqNfdkV0MgsTfb6DlbkR6_iroNCmzQJI6Og9hRnh_QFlZb9yhMCkOlHpPY8dYb7zg-vDkNYJG4Zuq5PAgHsBagyk-khh5tz97brUOMwyKHw1HgwK6Xj0MNe-14y7MaHdBZ60cW8sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQuOdpG4KwIEtwVqUX37_tDkvECa3R__w3bS3fJfFYbTBI22mrO_nCLP_KHKvSqU3h3rB-aGcwlEoDpH5ZhUF3mtKGg4r19OJutcMlO55l6RsDXn-kA6Z0xbH0SnCJBWHcEN_34-1MiSnWqrYohapsJl75vGjmr6sN1on9811plF51OKE2U770PVuY_bT57mgIcMWWcWsm1QBkJiQskwsbSi17lUttIvpBip1RQcMg2Pk_ErNmwR__t3ThfkibKP2Hyz2A8aMKRizVmHk-ETTko_mzQhGIC8WP3PSMb-wIkO_Pz6z30oVfBXqgB4IehkKGFgVhCmCa-T4_hMuO8acw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
