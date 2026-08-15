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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 07:30:40</div>
<hr>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=WWlbq1brtgg1WfodOL-t0wkcINXdcHlRmrcbY3BunK8BCMS0PSmdMdvS9xnquj3ApXeeFBBtjh3ZUek2jXbcU5gi9k_I9n1qNfU3Ezcp3nWbs1KgDEjyKtTdwmYQXHmwVTqcWFM-yLahXgPTj_Q4SKlZoPH6r2IbQ04eeMeH_PJDClZvaTN_poflUg_wgGR2Yb_NFTLIEeMkQR26RdPGs29G8UWZbb5bvOQR_JTgV79FaPnMl31XS7MG34bsI6Vyg3XxzDzgtAODrwVcn0lbkPbA6B1QjBCzBKHZzGWSthEEBhwuWysgTb4Zq7h5NlPfIAiqeSaLUqAkIyJ9MK-NNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=WWlbq1brtgg1WfodOL-t0wkcINXdcHlRmrcbY3BunK8BCMS0PSmdMdvS9xnquj3ApXeeFBBtjh3ZUek2jXbcU5gi9k_I9n1qNfU3Ezcp3nWbs1KgDEjyKtTdwmYQXHmwVTqcWFM-yLahXgPTj_Q4SKlZoPH6r2IbQ04eeMeH_PJDClZvaTN_poflUg_wgGR2Yb_NFTLIEeMkQR26RdPGs29G8UWZbb5bvOQR_JTgV79FaPnMl31XS7MG34bsI6Vyg3XxzDzgtAODrwVcn0lbkPbA6B1QjBCzBKHZzGWSthEEBhwuWysgTb4Zq7h5NlPfIAiqeSaLUqAkIyJ9MK-NNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=JaZEQG_vKIczqAAIo_gOepEpUemntpZ1OvyZxYsfgztwluuTY7b7a4WYId09KcOgOJBB7I0u4mASFzfin2GFd_4qFkmzdE21AradPrcWyGYwpJ5IIj18FWGIXDC3WovHyy-V8A_tt1-bV6o3soip-8MkcXM4cK1iuhObIYRJFs_ipc1ZBEtDbPtdHFGzr1gP15YhKNWDTv0CVgHkKzCJyikd6WfM6eP8kCN6aI0k1cD-eA8dYewYNEr-XBxNUPF6vjy8bcfWJJBloTLbrSB5nLTLWseUlVwO27MMDIbPnOKJoAvvGHo6xvKDLkReQ3WNLwNn1YeAo08jbwgatduDzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=JaZEQG_vKIczqAAIo_gOepEpUemntpZ1OvyZxYsfgztwluuTY7b7a4WYId09KcOgOJBB7I0u4mASFzfin2GFd_4qFkmzdE21AradPrcWyGYwpJ5IIj18FWGIXDC3WovHyy-V8A_tt1-bV6o3soip-8MkcXM4cK1iuhObIYRJFs_ipc1ZBEtDbPtdHFGzr1gP15YhKNWDTv0CVgHkKzCJyikd6WfM6eP8kCN6aI0k1cD-eA8dYewYNEr-XBxNUPF6vjy8bcfWJJBloTLbrSB5nLTLWseUlVwO27MMDIbPnOKJoAvvGHo6xvKDLkReQ3WNLwNn1YeAo08jbwgatduDzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZJd5mdJLZcoBbHrOZLmlLpxJGfYFiroZAUZy59hTWo91kAukuJ58VtFMvW7cqgh9XG6DyZIx7cRrm5NBsuAA6yja8GyLHXfvPa7mpMx6Tn_TLL-E1qq3b8PmGagKL9kgtG9WZLAjYnTooR7eXUm7ZokvTonAPBI7J3GXh2gVZtFHr-ifJU8Kk4v2xNNK6kN0lf-P-l1msmj9OiWtDL0YI4y44BEZ2hCeoS-38q5wB3QqaKKf4d0_nAPo4rc-EQdLxIJRZVTChM4rZ8RmrbjCyHqeMM5T0_ExTbFm-o4iXMl6v2maRgqUrZQxtVtpUlfmpZ2oVbgR3eqMTUitILGxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6549" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdZX2tXfkvZmlsY6cZYn2EWjfIQ0IcoVa73Af9e8LxTm7j0B0y5QsR0Ec1EsWFfncaDHO9Fdg1Cpx_PRwfvpNiWvO_j3zEIbixMXXz6CLS2emP11khkFIDqRRyX1isZJI3Fd-l3rMTEiVkKVEsYmf4e0upoikTkZGm_KMFFP7OdWkVEgP-lAOeJRh_uybh31GzPDajxcYW0Qe1fK3cFJd4eCNNjp-4wscFjNLn0KQkuCWp_8QTEK3Zo9IW4ibunyDJvS-H69bmbwCF5PFiifiUpcY5Q-E5Am9hFNMswvuV-u-9ICsyMgby-WuwpjvGr7e_IRPNkGY0d8J8GO5uu0PA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6548" target="_blank">📅 21:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ox6ItQUJ9qG3qVYishrE44LGB6AsY-xMCViqFY7cva4MWyPTQ22JvgEYuxhsa4SRJsAOvySUnxDUM8piJKgFadKnlF3ecGcWGa6VCY4D_3vIO9AMsLCY4_D9bda3re0V5syw3la0h_hcy48_-Hm21XIdoDaDnw3fPFS1IyZV_ADYWQJztgoGii7Tkz_BaQcHA1caG6cYuMGANHHajPN9vIGbk0Y1OwAIOZgLquf0ICGK0XkcEVYw81Jk5EpOoz94fmSFDMVlnQcedaPD13v0BdDs57kAHWhFykYJDc06BC8rCVJy0Y81wI5uWIW6Y1MVArD6iNQ1YwFfIYPQbZLigA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_mLDEXVE6afhWlfVK7LwRd3kuFtefrYPVkI49_UpjbBm5ldV2oahBQwLG4lKgF331N_NpynVYKMhKo53eAAmp7lsamFuPfH0IPNav8e_R9xAKzzh1RFFm63_5mKlBA_YDUKt3bXyg88Q3JjxpVgwmEpJPckrq6FRYBGEMh0bzwbc456iN1zQA7r1_QLWClShUGarhz6MISkhGu4o0b0dPr_2dP-gCg0QPcnoY5-K11FZywJQBpWc10CjT2Uhv24LcaTmTPP9Vhfe83O-BG0OBbuYND2td7Hr-loaiuI6YJBrLqYgzUkoQhQ2t8RjAn16NIv3pnM1yc-LEAx7xWyxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjkKT4DIiebID-QcGbujVPaEMQ4CbK12SDlQkdCElKdQevyy0Lb4yw9VavKpRFG8uKmi5Fnn2kVuR4QSh1_-tpD4zSXd68X5ui2QWckM_FZ-izKl7mDoC7MlSmbTcnj90jbFu90ALzp6F5Q3xQlU1YsZy0QN0I1POrO06NX-3FPYXnR_cVbqZ89Cl8UIwoqCzeHqpFLM24fc226-jz0dqOkgsnzqsHsn2Me_iwzUIQVIUI8qyurAe2YMuSXReCCH5DhADxkiMiCjlkoYp05lvNfoAIc1RIqLRFpOgdFp3Z35JPc1NRpWH6N1AmtGNKul7l-Yf3Hvnb9l4rwm7NlNTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZW32EcWqecWnEUCOC6uVNrfnJcJllqG_Tihd5S5MIuGOHDXKGojhCjmuVXbTLfxzRR9eF4_cj_IG_t_xVKwGseFVEsxlcJov793TmFrq6SHgC3D2s_fkGOEMiTZCEeH1U4zkoKAak15isdzT-aaHhAQXE0vNJo2VpUwdQqkcAUQ7FqYe6F8A_EkhcIn3KSdSdVloi8eTCFGEBElo1JSpMLIIXXjpvJpw3PC-3a_ijqNmBJitM4hk7MuHxjbBpZgEwNJeN7CDtTcTWuKan3bJ4E9CBDq26LJARGZx0I9WIWb4fIZNKbXft8yD7ncZ9zrc2MxgSfYnQpyrVSh7Cr03w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmAiCd1yptHFNnfgEGbP1fuYTc9DnwksDyP4QLTm5Mi927WP2zw5vRwLi5kcvWy6BhlDEtouE69KQKWNRnas1aNkQ5wAvHWBMFxBnPluEQwdn-_NlYGQsx__hX0kOYLm0LLWy1BQM3fZ7qpHlgsc_KtJM-xpS6-tFkhz93VHHJA87xtLEJbfoI1huOE95wc7rl2wlP2LJjHjohcBOgWRVA6pJr6mhVem2Pu8w4fHaL7K6IxnLa_CEgXhBaOJchmekDi7hXCgU_YIkhx_iAs-N41f21QeignRC-_IvEsw3qs_lHSFla6CHqWj9-sEIg_ftSF0SGuFtMik8baDfXfoAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=SNu6oo2JFkpSR9LEInFamQxg03vnariPwnJTTXiVUcqykXIqjelsSJSkzzZSlBDfEH5x-85okxgrJJKUkN5rpgaSItLKQxEjvBiDSTvxBdFIeb5M_U7V4iQKddZj7pGovWEfGDsWDDKlYhvrLqsBjk-e_j1j4N-GgKC6lqhDjxUc_3s-7vxBomuDQQm3nXZFe5fC6ClPjSHgkvZn8ZPycaFXPzri8jFoyJMuZUl-qaDBCdxwt5bSlszAFQjNvXy16U4saFgq8uEYv8KZk00m31hRLTfRWW3d1Ewu15pAVAk5toTnYaAlRJS-53l04-nuFSYa2qjEN7NkGzBGfELPbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=SNu6oo2JFkpSR9LEInFamQxg03vnariPwnJTTXiVUcqykXIqjelsSJSkzzZSlBDfEH5x-85okxgrJJKUkN5rpgaSItLKQxEjvBiDSTvxBdFIeb5M_U7V4iQKddZj7pGovWEfGDsWDDKlYhvrLqsBjk-e_j1j4N-GgKC6lqhDjxUc_3s-7vxBomuDQQm3nXZFe5fC6ClPjSHgkvZn8ZPycaFXPzri8jFoyJMuZUl-qaDBCdxwt5bSlszAFQjNvXy16U4saFgq8uEYv8KZk00m31hRLTfRWW3d1Ewu15pAVAk5toTnYaAlRJS-53l04-nuFSYa2qjEN7NkGzBGfELPbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل کوثری :
‏سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
‏سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود؛
‏وزیر دفاع با معاونینش در جلسه حاضر شد؛</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=KsWGU0BC4HHuPiH90yNELeMKHjkyrcjdx5WxMz79-jDgVcOeztAXr5mlqUQdchNCYpDVNsXIjCqtNjLdvwAGdh0miP2oGvTJqr0AKlgCP7PHgo48F583pubEist0bFSzTgo6-KiHz3TGgE5shXoEYVKUlcyWd3BL8tcGidWU-kT_bp0BkYYsT60GSe6kj6VPzEGlmbhFZKq1GsOxrM_YQKdqsDWsyAiXIZLMMdjIyT1cCyUglYtVi9bWl_uwtIQkirXAbjEOdrhq31_GJ_P_fRGapB0j3DNlu401_FzvQA24gJkMG4qVYb-HvetsNEJTVQeqqFO8oUwbSbx-61uQ0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=KsWGU0BC4HHuPiH90yNELeMKHjkyrcjdx5WxMz79-jDgVcOeztAXr5mlqUQdchNCYpDVNsXIjCqtNjLdvwAGdh0miP2oGvTJqr0AKlgCP7PHgo48F583pubEist0bFSzTgo6-KiHz3TGgE5shXoEYVKUlcyWd3BL8tcGidWU-kT_bp0BkYYsT60GSe6kj6VPzEGlmbhFZKq1GsOxrM_YQKdqsDWsyAiXIZLMMdjIyT1cCyUglYtVi9bWl_uwtIQkirXAbjEOdrhq31_GJ_P_fRGapB0j3DNlu401_FzvQA24gJkMG4qVYb-HvetsNEJTVQeqqFO8oUwbSbx-61uQ0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fW65fWfrpy0R-8f9zv6SBqKsCqEZvPzqEwIVhvTHV6jm4sKexqaCht1dfiE77t3OfCTdECVEtXGhbTJT_dl1xEsDufj1SBFkxLtqUh6AiedaYyWJDhbzyKw6VYF1LkNxjy1r1GaR865KU4CTwC3rXxOjDv8SzcCcmSMZPO3huwxAa9asLhQ_WrUUYu_OvWtTK-erDZEXjlpAxLMubAw50Q_anvun44jhruiVCNLpPlRhsWgs1WOiF_djI_s06E0fCP-Lvd7yi4wcYlhOQj-0tArfTXHJfegB6m_V8hpSfDeR6VvDbMg4ONt8BRDJZyYBvdFduqMuYWxJfPwstVzltA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6Q2B3EA13bS8n9EEXjliGthWApLTeVxHATvEm-jbuSL7ki0HoF6TLsNggJxOfL8sGCB1WOGXo98EX-Rs0wOn8vnKS2ijUJ302mPKlI-09OiCEtnYhE6ZwhwLi31kW9xf4ualQaedx0XuSNNLKTE26VIm7SSKUnYyXkVNCagI1snsutdVlKClqPrWsjmZzqGt650vfDe8DoqGCYOFziBjlUiZBpYk0HUp9_2smrSw3IXrHSq988B8vLZ9B3fivQKEoKqdMMmxzpRo3doVr3O4WAQ8R5ZZRfrxCcImtoBjQZd44UpoQ9Qe7VNUqNkdG1fpcE_-Xn0ytKc3HPsQj9jYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OI0gRPSFjcMV7tgFOImrhIvku-SdVhIGbzwmoS4jvTci3hn5H4yVaEhUu5aJL4SQ3OTYSuaNtfxgoyi46-Va2SttED1LExdEOdZThh4knncMsOC2Etd4kynIfzlTghuVncLATeCfoiEvEnBsqDuOLxF_Lqm7hoM5SsbGznAJ3qpZ-XM0USCPbkb8MhXCgG5sdPNG-HheD66xaROhPe_NEXHzwwReUAWGh8s-8cC_RvnVhVMmPW6rxrQ4l9ykDoyYSgHZF1__qEIVuCe8wrKKCHrT6okxHSIyNSi3Yy943yQ-ixlV5ICw0MgPpU4wIOT41SVM1Z9aD8kWQzJph4rIcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEG_NDmh1EnkUW6yFJbmtwhjHwpFvA_S5vK8vo38qmxIqZ_mqvFH9NZwW8w82Tjl34GigpPmzNB_qxjWie67CQQgGVcVhu5V-hcU9NX490q1hUhxMeBfvoqtwzZH1pWtMxXEqdAdYwqUZeq4ZQBqggPTOlpqL_fDcRWfyVFVLE-7dSdcwG4_FEFuS04qIqxqOsEVhPTaSyHUF0HNY2TIGm8Z5QDCz-MsQTIImwfKXijcE5iG5AOucYWNBMcnCHw-xMp6HYs8xwaD4MfQaOoNakxH1KVwwCftvVN0MBj8cHKDMAPUQc_9ZJ_Cr-7VlMGwguxej2b9uL34K9cgjonXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhkaKuy-3Ms2KPzT6Gw8tOzJ7o5LIYQiH7_5qkmUTLY7AqQBFfNOFS8Ml03Hzw_rsQR0KQs8SALQodqEPUIwf0iq2Cda1eBcBwn_yyjCbm3j2O9LvNlnmYwibAv2PPn6tlDT7yHxd5-3_A2DfrXY90XtvSznFR8p6Xga32RMnJyo7hhHSG-jax7LAtgT82T9-z3LsnR-et5XUvwovK_gGSi0HdevdkSpnqnvgdq4yRJT_UeLKhAz7zzsIDgpg8gMlBNxE3-44kITHQpfcp3CGjngtr3JVos2tG6m52o9oVAIIt0dWeE7ye7p4U3rKlUt_TazaKSlJygc9tEeZ9vczw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uNjvG0soaZVCyusknZCkOAS7P7-fM6HL8RAhMAUGamTrIXqi63JfvvaRWogy-R6wHwNosG0J8MrpoDU-XttvF2nLtdZYsteJy9TiMPtU2a-uiBvr7aSMksrQsLxJDlbViH8ciDXoo_3R5lR2rk5aDVVbKbpQX0QuUIqFXgr7S6znfmyOK1KMQ_Ke6NUIn2-vf7Q1kRF0l68hNhc6cI-FBfE9fvyFvcFvRrgCZo0MWJby85bQdj9Chc1YwMKXiO5cXPXxEwK1itACXXs9vTpvkeFnXfpNHkngphzPaLw9xDy1w9WdbQizI6jSrZgQfZMGsr7KUCPtP5k9y8nNwpbeHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pZOJm05E29zGnxQDXzgIi_S1wdvfZdppCpx_OtI39xfO8UJv219Da6-w3CoEaZ8FfT2ZuS86FYRSL1Oo_Bryw5AQE3uhNrMn9J2_z5d_YP7N-0Na8l_xIn7xKljVTC27NoJWH1sLDiHf_60MmtSHGdOo2T2IVh4GviamJM7VvjPyt3PgaqK_4vex8e4Ri93bMI3D4Rh4eLWTf6qCS2QugfX6UMp_9PF7JyKFJzelWjcf0S0WvjrvDPo-CzeV2dTlIJ1f7VM13F6sYMLp3LSZd1wZtYq8V_EhL6lU04X2d-3rezgMqXY-IW2HfrF7Mqfiu8KfgORO86r-9hmXNmf85w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R--0PqgCAYgbY3g1lP_-Og70B713ugvwhiKKG8RBCzMUbFEuu33AKtuxU-Xz_goJLn8rMpagpl9FzjTIqDsT57377JSVxi7jeu6Jz12CJGGEZuYkyxI2HNMehZmuXawUN5mcIZs_T2siScdclOz-5dKGiIOws_FsbceYTkkuX52EspaceQSke7zZrtmCADC3-dIeirifrX4QBGU4RlUlEuOIyRhyNWG5oZGn1ph-lsZLKTWVy9LknqQ0Hi60-8ta1oX4nmamWaIwcIh3WZJ4TgXous9bMEDyeDKGvbeQBSONBRBp74Pm9d-CM5iVJj4TxdMSzcIvJfu4Lj7RsrSgDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیرین مدرسه ساز در ایران،  ۶۲٪ از مسئولیت ساخت و ساز مدرسه  رو به عهده گرفتند. حدود هزار مدرسه.  فرض بگیریم همه اینها مدارس ۶ کلاسه هستند (برخی ها فقط ۲ کلاسه هستند)  اگه هر مدرسه ۶ کلاسه حدود ۱۲ میلیارد تومن هزینه داشته باشه، هزار تا از این مدرسه‌ها میشه…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHlP1HsyJfTKYocXEkIQv-hIA7xfY-nlTdiK3RU4BCXqgF8eC0k06Jyt04awDnKqwZJS7mz8z0vCiX2JhRcaSU88PgjR_uFBD_lPlEVTmO_ImEMCXbWVK2uTTQKmM1rhheN4aOj_jgnpHTzov4eoC-wC50FDxvB-MSsBoV32v-BBVJkXR2MCvqP3FR6cVApbTNH-vb2bbtTrI8N597zge1QmnlBZdTDwnxU5WUN9nZbzijIYTgUQ1MX6BRGABJKLqcvUl919EUu38G2_GFz5kqyNywfxgqu4szq5GnpzIZqDF5chTLMaIV15CQZ_R9m3gA1W_e1xckmaQ-hwf2WEjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا این متن با دقت بخونید و قضاوت کنید:    پدر یک خانواده،  نیمی از درآمدش رو صرف مواد مخدر میکنه،  موضوعی که باعث فشار  و فقر در داخل خونه شده.  مادر خانواده ، چون بعد از اجاره و….  پولی براش نمی‌مونه، معمولا از بقیه کمک میگیره که پول پیاز و سیب زمینی و…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6523" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHhAO5XsaDqANfVg8tbwilLZORcmDadeLA5_kI0nh0pI01nEIue2vjp8q3oAEwxZq1Kx4Jpx8c8E8njFdNsVvMufwIIhZ2xf9kZ7H2FW3mQqaDZBc96KBUCtEdSV8v8WBWay82-fjUU1AMbK93jZtI-m5d0YsOSyb4JFrb54IGWPN-G6oRAT1ULkO-ok616phv4K08L5i7If23mo8mz6cK7XdF5hC0j60dP7r0gP3GCckUV-5SjrRKAmkIwDfht1kt2oVU4sKeZGLImVInScjY1wNijY0W9MnEig95nrA6fByxP3b428aArvetG9L3JDzyUPDOLG5SvjDlBaZPc51A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsrtDjYa1hcU2EZaIZdfHYxvoWMRHpAANSL0pwOLv6MiKM_Ad8nOhH-JXOqrHUibgKSaN-Z0qBp3FpeiHmHBBLI2XwUshpcPvqqAYDQwCHwNwJ5lRtUH4aIDXnP4MBBe-5bt-4h-FxGe0xxiz-Zsl4-vN-ygSuC1bieyll3hYeT7fAzK-dHsVJ4op9NJeycVtAX4CJOE-ZTuLEwaUqjgslQnv40eo9HDK_a-0naLW7VHvw86cUGtpwfjGVB2ohw32IIqzEgDiN_-fvapadF5rTW4tNQRxk0QH2hbZd03bIRqWBVzoaOVd-1NaW7EQwNmfoJ1jQzuXVYO8n2HfxXUPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDGTqnUDtCExaoL-twl0y_CpmPLu2-OWppbittRzmgbCTdDEeRYLoS2b7KYAxTa-ymAqsizLyN7W2OT3Cfb5Crg22sZ1Bclej5NaHs7_QpDd0TBxWkmon3USJiTxKbq0JgR_AuA4HVF_MDUm3BweX6qrlRHLMwtXZfISHPhtrg35w3cZzeQ-Uwq0xmZ2bjNLhJKgfr8nLLMq5DkuOLEXm2L171FfbuB1sMZYpRrYx-wd8BvmUt5Cj3Fs6weV4NALzsMXI5zKuSr_x9X1GDnZwPVZm6S3p7psa1jT6whOAo7ZV2VWmQL04Fb5Q2bnBrz32-Zmj7cq0ynQsDDYfWiy6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k3arc1g1p9VJB_OvetjpBomgAcH4zKiea-qy2_H-ef2kCZsytJytZFPidXBIPcDTsfz4K0tC6jVqMEtlHS1NfVVA4pDKP92nsH6WDuLcpthZ-OUc3LyORyA7B98qOHpKy9n79-KcZA1ZELFBjE1TtA2Rz0HALtBpYwz9qIuE4IioPJSyXVotSOFKtBxVIcFIDMQnx-CiWDGcJkNk2g6UVgcq7TEYkN10VvE5MP8puEUKBw6uV7i_PEw3u4u4Xy9iXn1TqXDW8oW6G6QmfCDhock6bigCQq0qpI6b2HMqWEG4dQN1Mg1eZKUOEVGUBfeZ6SwAvK_I5Fcq0MM2zWkO3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gEtGa3ySABSBWAK7y7mqXFFuFD42iKxhLQBgjEeTVosqekZmXuHOwP79TrsME0yh26J_QaAuhC6QLFZpYmr9thRGmLOs7f-NhfYiXbVl4bLhULoQeZp-4T-KwPA9JwFqmVP3AaA3U7PWtAUiuwRGk1BohG3RpmLwdcEEiwVgP2_ibuLKm8BkQYGHTIsN65Wzdo8ZYQ4vzRbbfxppM38mLGoPFEQxsYYjz-TLCl2SnTnF4g9iMz5O03WwDp1WEZeFuRujGzjf7-3BLoEs-dRoYkmvmFkaE3xlHx5ILo9vZC8_KtJR-V5TPYbxSXkatJDEPoveh9S50GLuU1c9idvdBA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=fRou1SRVOis_IpRFjdwZUjFpQr20vTy2z6fD2KWGU4a14HYJ0WwYmnhM2O0MP1jnLrlQEq7JeHivxGUd4zgBRYWqKKcgt2mQ_Y_koIuFMvlJJr_wfjlDyPRfyywnVEyaAL5mgyo8h0JR_MT3vDjvmEtpuEXrXRzQZ1A2S97Mkd30tZJ1Vx1aMirLbu8ZoqAdhUnafL7JDC6x74QiCwU-1F8D_badfXxPltcWad63IaozbPcFq9MSeT2rl6IGfRMwk31r6w8ZH7SJ1MKtG0VPDygKt_oD1oNOR8SOlMwAitndOSefaExI4v5rrHFrFaWa552_QhIUX-5bhKhtK9MeBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=fRou1SRVOis_IpRFjdwZUjFpQr20vTy2z6fD2KWGU4a14HYJ0WwYmnhM2O0MP1jnLrlQEq7JeHivxGUd4zgBRYWqKKcgt2mQ_Y_koIuFMvlJJr_wfjlDyPRfyywnVEyaAL5mgyo8h0JR_MT3vDjvmEtpuEXrXRzQZ1A2S97Mkd30tZJ1Vx1aMirLbu8ZoqAdhUnafL7JDC6x74QiCwU-1F8D_badfXxPltcWad63IaozbPcFq9MSeT2rl6IGfRMwk31r6w8ZH7SJ1MKtG0VPDygKt_oD1oNOR8SOlMwAitndOSefaExI4v5rrHFrFaWa552_QhIUX-5bhKhtK9MeBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8n0tnPoWvkfoJ0w7j68cqU-fC4OHtJT0i6tj6RNSiPl9y6iMW42QQW9uWkZ3bWUQdULrdVLQsSQ_woS7RcnoALIgmFAEdWcXvsbg-LZ-oV5UDPdtjYdw8xBhZIoIW-hA7EFJ1q5FhmQuLTEl46UJ0lhVF0vFI5aslHNkJV61276HJxToROSWaGOwL7yFVOIUu-IGJaeUZuaZnDuLX8B3kntqa60bLaClU154x0w5s3-a05hsU49L_gtUoqSD3B-7EZuf8SBK3RIoDeCT1PisruSkTDrU3xBTFrsjWMsceEC0G5gCbmRAEF7XXG2HvK-vD5n3Bp5Wc4SVQQDm_E-uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8AOZj7Daxq6BIift4KJnY3nmls7IYNFux0k6xdwfLon8Dro6mvalQIghrQIJynTqfY34PWQ3o28pJmy0gaQBB1UXakuv1rG7HIHYia00dMLB-vMtN0jrZQkAGA7G4jnoMxCssSguBxn8CJA8MdDKsBgfYvpIv5Wbs9BFCs_7WRIb-9Yc8P5WCcy3RV-rSTB30pJVq7H3RTQUgX_PwPe7vHjt3Nob47MqDDqsiC80AHZ-uPiB55wpcM2Xx9w7POgFYy4-iWg2CZ1h0WL0y6auyZak8YAT8P_YSQL3MK7DHXKkRcIkQ_uR6HylixjAAXOGzUsUMLxrrVxHx6WfvIlLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=gqcNNScA7F7OK9gXEiIl4ORmvnmHCJRCu_O54F4BAKVb4BsUqy309BHLStE0_k6w3Mj54GPKx2oMPNXj9Juj6H7wmkebWlh4BjCTakraxjEA27zFgk41C6ya4DAA39zdRvqUUsRdNRO6xVpixls1xA4iZQB3p3ldtUADEyQWCvjSOWP_1Bn_B5DglFgBdp2YZfaq-lhxiNVwkRiSeW3_0Vrgcb5_gR70SFo1PNhsXnCkGbsSvkGUEQcPQOdH1iMs3jVD6ewz_7iMtxnBmbXZ2mo5lRbER_iQ3TjG508VHb3Mz4IG3Ad1WcD1cN3pXdk9kqQrq8ca-sInl0RL_BMD9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=gqcNNScA7F7OK9gXEiIl4ORmvnmHCJRCu_O54F4BAKVb4BsUqy309BHLStE0_k6w3Mj54GPKx2oMPNXj9Juj6H7wmkebWlh4BjCTakraxjEA27zFgk41C6ya4DAA39zdRvqUUsRdNRO6xVpixls1xA4iZQB3p3ldtUADEyQWCvjSOWP_1Bn_B5DglFgBdp2YZfaq-lhxiNVwkRiSeW3_0Vrgcb5_gR70SFo1PNhsXnCkGbsSvkGUEQcPQOdH1iMs3jVD6ewz_7iMtxnBmbXZ2mo5lRbER_iQ3TjG508VHb3Mz4IG3Ad1WcD1cN3pXdk9kqQrq8ca-sInl0RL_BMD9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-zy6Ze3PDOAmVUKAHJbiPGI5Y-Nra6XK_8d9GbMU-Ryiqrq8PHLh3VhHBSN-oe2QwgbSo4C_XQe_wvgwTiBKZO0ORv996GMsZljD7U5w29HDfjmpa0_tL1k9p9_H22IAeoVTlU8TeJplK3vZSScerWCI_D26IeTT9wgcduN0VRfaq3BrsAsXyirCWodpF96PcTwDQpKIt__cuspBT09utk8ZwBHW_lV6cK5y0tgOFf8GPlfsnXlL9fpfdDfVBgmVMmfiZ0lWIp5BU7Qq5rh3f8Z8H1XFGrWijRQ3eSngb37kdmdKcNV6sXKndRoC5kWcKFDv0VyIIVsxiLPLTfQFw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f29785e012.mp4?token=YIgCIlwMttIoUwPdVFckngWThdwChJmL0Do9KJmOvEx7lER9MF_NPgHDlq67JOxn3WqJCE4LJx3GXToZ63kGEiOnCU_mQQvJUPeLTQGjOz6Ds1rDU2bchXtoJyRqhMr21_cy2RRDU3QUOOlC4-jUHvV-wgLuClSTSGs0G0xI6jDzGeuC9Dv-s2RwfA49vhoVXIxWg3_imaDnR4DJ_5JXuTWUMUHUzdm1fn1EvzmXu_OMgNR4ugLNym6bxSyfCGblQSG0q1UM3lddG0d4uSQE-949MD1giuoOcDFRb1kCvMftZW2_KgQTtZiEk2CwBAiXl-aHXSrlPQvujBuO8cUlvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29785e012.mp4?token=YIgCIlwMttIoUwPdVFckngWThdwChJmL0Do9KJmOvEx7lER9MF_NPgHDlq67JOxn3WqJCE4LJx3GXToZ63kGEiOnCU_mQQvJUPeLTQGjOz6Ds1rDU2bchXtoJyRqhMr21_cy2RRDU3QUOOlC4-jUHvV-wgLuClSTSGs0G0xI6jDzGeuC9Dv-s2RwfA49vhoVXIxWg3_imaDnR4DJ_5JXuTWUMUHUzdm1fn1EvzmXu_OMgNR4ugLNym6bxSyfCGblQSG0q1UM3lddG0d4uSQE-949MD1giuoOcDFRb1kCvMftZW2_KgQTtZiEk2CwBAiXl-aHXSrlPQvujBuO8cUlvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=PdeVoGTdCUgnUj0aFIf7afkqsErWzbCvYeGFDaSQv61IAad8H8lYQHpxGNrUGG2IgSA0wAWdVfONv7shPrrqKau2S7j2xQIl4G95PLQjr-MG7MkocoTmdQyqZ8hl5Jb2eABhuw-m0nCg8KUY8KJzOD8bOL9q-RBdXGR8efig_okSG_YCf3NXqB9pc9xqgl1PHjGBmSVJDrnAy_IBYkiOoiuG7Q8tmhWxgV2V8VAWtahN1gygkqhDpmW-zf9zw6ptqUM5oAVGMb9pNjcyqL73So2sxoDrBFHYxwEbTOrkJqUhl9hOaFlFC8HGl2Z-NPrmODKoRlo7NBf8dbqeFKET3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=PdeVoGTdCUgnUj0aFIf7afkqsErWzbCvYeGFDaSQv61IAad8H8lYQHpxGNrUGG2IgSA0wAWdVfONv7shPrrqKau2S7j2xQIl4G95PLQjr-MG7MkocoTmdQyqZ8hl5Jb2eABhuw-m0nCg8KUY8KJzOD8bOL9q-RBdXGR8efig_okSG_YCf3NXqB9pc9xqgl1PHjGBmSVJDrnAy_IBYkiOoiuG7Q8tmhWxgV2V8VAWtahN1gygkqhDpmW-zf9zw6ptqUM5oAVGMb9pNjcyqL73So2sxoDrBFHYxwEbTOrkJqUhl9hOaFlFC8HGl2Z-NPrmODKoRlo7NBf8dbqeFKET3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUENDhwzX6ulAhQvCgoRytPZzUgapcGW2O5FKmmhwP-aTUmq98EgNtNcXV9sOe7VUggV2tfM7A1r7bHsD-r4ZGVxQnG0WRp74QdxmnZ-n6zQ2wdtFpGaC7b88fCwIdAK-6ccTNCs1go0zcH9EJWvgMvzbjj9Kdl1kiYtdbghrkrGJC464ttMD1_t08rsZL3jOahfs4N56kRoOFomcCgN778YPrsTaw9rJ8uJ59TbZjgm6dn2kCtcYTYKz1qYhZATts44-_Hvnd7qME-40veNGiYc9EuQqVEPsOpqetafv3SOk3zjudIg1FCe2Izj2BcPTrXhMgC_T_i_wS-J3O-SJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXpXPTFdGEem6HTm0VCTF3haq_4KxziuqI__AK8VZ6vXfq-qLm_VdDWXd6XHlMdsPiX_Q8K28KyqjHs3rplsqqaiPxOzc3-m_qTg1-OesrqAEDtZRgOTHQNamfy7Vq-oBoZXsZdBoO7vkg6FX7ikWATexche_y7zFMMCwTn7-cpzx6FRpidvGwDkmhoTI-ewWbnvAxoqk0cUirIJd1ofN1eiHc4-RDpGBAeCJ3l3H9WBovM8PkkccgVma3vZ2CTpVvBL6QuSQ0LUyI2JSKm81A6JjtC-FnJjNYVWUNk0bwBW3bxKJGg4iSSX___wlpmPr4kRvJwlT3lu82myixIN5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g45mb8arwh_9V_IVY6a3doNSCHhJl_8drrr4FZDBFSJJYB8H2wXvLDCxJDH5t_tzgUh-SYwAGc2rD5bj-3p9Z9Nh00Ir3UC5LfUdRpkVOpkv1BtxxWUtXPzpkGEFYPlHnjD5KIWffXpFRNmBoPxrZVyhRG4gr5D_RxTYxi9zB74j-qqQxqvv1WYTsx0XE06bNaFbzGoQB4TgsfA5MQJbx-lo9eKY95sFzK-S0HLSXZgLQWsFu94xyoEo0ZFt1WI6eN2iSdxfHTI19qY6fUIP2rSdY6-MbNhyF20X2MqkMvM0tUrYJx9wf4IAi6y9CWJyVvD-Os5qAdzrjrGukzM72g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=Tn8Sx7D0b_KgISoKeoYcH9AV8iSoEGMt2_O31fGvhrIEFvkMnu4FaHG5FSwFdw7wRhJWfrupcgefV0ZJfriAoFTvCWlHJttTxvMxYrJjoaqu3-v_CnNsMY8RnDAKaeBLnEllSYbYa_noFnPzvgXNIbVO523nsTCF3-8FfbKqRgRq4K0S8uCg7d7bHSib-mWffc8Jxj27MInS35RsXLFNhOC3508lhxAJgZo543VK--mawP7BqZM7uWmGMOyAPwazfqneJGpjCib17teqKV8dJEmT6XkXnPwhrBIHM1avEngnQb2wEojysK07-oXxbt3SbwxI6chQ23vX3jZY6lbbdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=Tn8Sx7D0b_KgISoKeoYcH9AV8iSoEGMt2_O31fGvhrIEFvkMnu4FaHG5FSwFdw7wRhJWfrupcgefV0ZJfriAoFTvCWlHJttTxvMxYrJjoaqu3-v_CnNsMY8RnDAKaeBLnEllSYbYa_noFnPzvgXNIbVO523nsTCF3-8FfbKqRgRq4K0S8uCg7d7bHSib-mWffc8Jxj27MInS35RsXLFNhOC3508lhxAJgZo543VK--mawP7BqZM7uWmGMOyAPwazfqneJGpjCib17teqKV8dJEmT6XkXnPwhrBIHM1avEngnQb2wEojysK07-oXxbt3SbwxI6chQ23vX3jZY6lbbdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=jsELbd_wQduzLztH5WUVGUIEmLPTjnHGUEuXdFlcSCR-ZqK26S3hKgtU4QXTRwNedcq6xXcFeTBhsph1xZ7wBdZazuaxMrtFL6SITsPFT2DGvx-5Y8VHvGv1-RcV7n9DK3xUfoOOJ_H97GOeeZ5C6znqXzfercYeDqP6cIAb0HfWGnFrH8Re4jOhTEFjgCnv_DkVT0aV2-QvvIR16OGiGaykk8ciOGWevZ5mXcBtisehWPCyvI0y8G54mI7_xj3enssZhKs6Dee1O3MmL8keZ67p1w7Kr0ecf7uwizJ44IlMYCg-5mDZf2GX0GH4M8zqotI3hhclM0o1b7wbPZZpLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=jsELbd_wQduzLztH5WUVGUIEmLPTjnHGUEuXdFlcSCR-ZqK26S3hKgtU4QXTRwNedcq6xXcFeTBhsph1xZ7wBdZazuaxMrtFL6SITsPFT2DGvx-5Y8VHvGv1-RcV7n9DK3xUfoOOJ_H97GOeeZ5C6znqXzfercYeDqP6cIAb0HfWGnFrH8Re4jOhTEFjgCnv_DkVT0aV2-QvvIR16OGiGaykk8ciOGWevZ5mXcBtisehWPCyvI0y8G54mI7_xj3enssZhKs6Dee1O3MmL8keZ67p1w7Kr0ecf7uwizJ44IlMYCg-5mDZf2GX0GH4M8zqotI3hhclM0o1b7wbPZZpLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=YvGRjQK_2Qh4hIqDzuoFnI4iBrm0Mp9DQ3VayXp5v9dmn61akioMHCSqOFsFJF5AUVuOeudoceBZG4xN1zRIhNbfrbtU1pXb1ClWoupMQaUn7xvLOGWjb6jBng_qXyPVFoP4ppT2Xrp9unAO0ux4n-aTfagxwE7jmcwsGqC0w9FPN_5Ms8qzHLCU8rN_FR9hJgP5En48dqMXBFi8Te3_4LKWILkL8WhE93ypN2n39F1M_HDbsynFKYypVlmZkygJ7dB2TIcHyh48CuUXe3F9v9vgRIIzJCZBocF6T-aI8QQJvWwgjRvLuxiBa-Z5zEsMiwA4p403cGUNEkHZD-TgbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=YvGRjQK_2Qh4hIqDzuoFnI4iBrm0Mp9DQ3VayXp5v9dmn61akioMHCSqOFsFJF5AUVuOeudoceBZG4xN1zRIhNbfrbtU1pXb1ClWoupMQaUn7xvLOGWjb6jBng_qXyPVFoP4ppT2Xrp9unAO0ux4n-aTfagxwE7jmcwsGqC0w9FPN_5Ms8qzHLCU8rN_FR9hJgP5En48dqMXBFi8Te3_4LKWILkL8WhE93ypN2n39F1M_HDbsynFKYypVlmZkygJ7dB2TIcHyh48CuUXe3F9v9vgRIIzJCZBocF6T-aI8QQJvWwgjRvLuxiBa-Z5zEsMiwA4p403cGUNEkHZD-TgbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpbmwD-lVdGzFEfddSUFsBTnV-_AjSgvCDR28rNJ0oOAyIjgVpDgIkpZUI2FFOJcdHSWo0kY5dFLqOv4_W9_BmMA0halh-Gul_avF7-yLrwDY5UGygBCyyZTyU7swe2Lnl-7H_nZwCJ8S4kfWUIY_TRJHm9BJtycr_bhcD9VCvFKerCBsyq_Ms7SxvaGNQs8Ex6coO6FiC3Rj9fj0eq9SYGHMBeoLM2on22VWXlpE7muyjtfwkjnrqBWnNZct5KbZuGljNW9Bd_UD-30mwYXL_Ni9Ha7syWcQ169n_l4-LaTrrRaVjC2-hnVUY3tC6ycllcdeN6x0z07X-jZG-RDug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hS-HJPz5413OB1Lg2pZIU_qB2-XNr7-VQfk_Y5qmW738VRqDwyNbvjstoPtt24Jfey-TC2LhF4JMCxb4RIjhyINkNnRGSTEroRVGN4-pIyWY3LxkEGluN4Cn9iPqfSGmCTYmLaIAjr8hHWbEjEniNIpFXgUsojx0QPLfjgu2jFPXfcqtf5mKmkeJaPtvxbxbIPby6oXNETcfMLWN_qW9YUgDw0auUKPsP8MuTEJ2b11IH1NcLnSpR1nOUEAeOg8Hhsf7Q-8WUUGdgZuiA8flKTTv-XSD7BFgYbZVM1PRrdntkqZll9xYtFu6lq4TykByiP7SHGEx3xOixzOxoXFjcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R5DMnQ6uvsTHlGT8qFIjE6OXTz05LU2ZCi3c6C12Ke-eSNeDbGd5AkUohSdWSC_7oF9DR5cfRTrb1TA44U4bgQHWn1HLrYLjXtn_OF0jKS8ukxENAI1i0Z62B72EH8qsJIfuSQcSTiuOf_jhOPSBUdCZ-04vDGucIyljm5PHUzJ8PhrH7NUPsXYDXujlCywBO752lx3Mm_QAS4mvs3tADx69CdbiYJVOHjNEDzKVhgCfqByHjLk8PF-CYMTfpbOuzWysEYAYGXIiBZEn1XGMzNsMvvVa5wW53z4x_DDKWeSa9uI0dVkNIZk26Fbgh-ntQFpeiKNzgrKfzzIDTkUKfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s-d1K0YJ4KID3PzunAdRdCaOaEhe2TItHY_rgVXjJWRy5aPyWHYh9dnU-Kwz8U92a5YgUrG8p489VGJ7YiO6ctKxGofdjG9ZeS-telp1WGlKBRhYAYBSK8sP9lfccoFbrhPMUMqJb8p6hgC_8jU5EDPm9Eq6xgooo9R_VlGOb4rWRdfd692wITPh_lwH6dkFucMjBOzvsvgcHaHTvo0nTh0bTPuCrOQiO6HIGXrNTQwvZWWwkF787KfmkyivBm7mJOrU4RRaIzHu9ynznH7FtCU2ODeInRFEOjKJeeLraicOrDjcy7_wKFjyhYE4N129O0M1pjXuSttu2f0HcSFq1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-E6gZ2NKsG2glfpMLAVH96mxsxDTZxMYMsfDEHKgeQWZa3HlmAmMlxm_LhoocpldGR_KgZp57O5vYEWj7EvfrdhjNppKsCGG3gOdm_A8hGq4RM022MTglHxH5MR81iCuZ1RRxZoFMP0mg37yBQj2DhvXujZPl7l84l34ijDKEV16OMPRtzbtzD6jpsqGmKAMmPiIRTzbWHmfWAiBJ4vh2nFi3m9zEJES8S1Stz5l7-FXS-iEoQ2Z0ivCw778EWsbKnPci05kzzWyCWehmcyAcAG8UI7lB2oEo550yMGUgWw5lQMnnpgIxm1mN4GTHy-HthH9poUPx-3PN9aDwXbvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8KxahtGsn-l_2kGlJprYs9EgU2MLSRa12DWxifxA-yEMUbk21PnPNjRQeAszj8wpJ7UBwuDuehxtp05IXO_RB12ZPTN5-OpFdDIMJHSczEivi2ZzjbWRBgWQ0Iio3-H-SyVRI0pIo306p6UDrqFPjUrOOWjxPzOC6gKeLB86pW0axD_KN_yMy-sfGKqyGNLY-9aerkcaEOzw3yvou8OMzfF4JgC5ya6-WgQo6b6618XHLmW9yQFQ5e1z26npIXv2YkNZds5f8SX-DKvOigie5Q_uvTH-ulTImUHr3_-sXOpO0DnWQ-sAwbsg1DO6dkrgTSd7C4Vzrno1GzyEKVvYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2OSTtPgQ0zz2lBCtu_-ctpH54XHMOZYTW-WWUXXYCibWAyRF8AGxvsqJwJakmlg2QjYVNs1xB0izsNpJRKd8mNm6vhX4nl5DFqAJCOZF5mKU6Wt5sSCblmO0SnIxe9RoMdPPGlvU9z3dFwbTOqeRGNb4rGrMZFjZuo_qDo5m-vKq_e0Z-gevNoFgH0eTQ4vRViZJOuf9GcuVqVSFSrqHULG2lXFfHPEX6a5LaHDkp2l2SAAIQuaORVX9lQN2qdIQrroRDVhUv3t75l3oyzGiwqs8qe_xdTqVJzKBCOfn33jxspDwNoNy3QQc-GEOSR30dtiWbykaImJmkTW_akKIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWUK_hvSPA3peK3UpHDlcmX0yANEGjl9D9Vz7q2cqCp3r9fsAcQhpWyIRiu4RsjrRm6wjAPRCPWvkxS3wkRQk_yXBaHMWH-4kFPMAFT3fWcd7LCpJj10ND1_2V7H0RmueKpqx7wayDu-giRkvcrhIIur4q67-2_V3LKBI5aY3Rvt5E_TAVjAaiXvBjk6QZV6eb9xICT2WCfEKMS3sQq4a2ZaZmIQj6HLC35csdjO4AIV3rGrNcODJ_DKjYTHR1VJEPJ4II1TJsKkxcfB_rE6DYI-VWabIpOmyeN--rrAJlb34RcU8_xs88Tp7CdkfqC6dxLnUChBSr466QGy1lZ_rA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcep-BkoVFPOvJq7c1JvPzZIoajyBYY7TU3M-cEGy8oxUbKEEstih_bOIXyOz45XbjwfDscHdBNbQW8GOtMA1ckdp7Oauf3QbKl2WyQ98Kyv6sl2J7O7JQkr8Oj8yrIE7j3FH7K1bwzq21UkLz9LhgHa9wGE3Lq2HG7-AAyPQ5KZBCHHA8n0ueinhD-kxdmRVSWKPewamcxchdEDiQ_FO9yMiaYdvrJFM2fa4jp40FanExwiA-tIq14D62075BZeT9FWsmFMhX4TPK0JYLPWjG6DDbtlhuj9owGC8vM48eAd9FT5xK_VVGd7ECaxKpP1BH3zbTzgoDq6P7Aj8ohtcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3daNDOdYvEyWcOvwAxn97yGfFJyxRSE-bxK0hIcNDMWSq8QzikjC6sBGXJNZMJSP6r8km5vt6E7UodHCEPldd-Sge8I1vnqG20-lmxy0ZjS2RHGTbKtpUdwXE_DJHJMao7lv1bFxkR8GPYliitGZXfeFvliB56b1-Wth6FCx3_Y3NYt1wMkBM3IxO_OOqDrr0_Pn1WZPXfpQ0baiQTJw15P62ImIoVPpWSlqiziERJm67Q6axTaIdfa1k35kOMXDwubS-RAU4aJBB6bkHbSkhmUnMwBqxe0bpKIPNsXhUNcHQZOEzUnIfWiUaF_kLlOGCeNpyQMqt0_6Blgzbbcug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgxnJprokPey581OXi1LZQYcOsPJU6ctS8ptPmziWZKBrH9N2JcHDEhJgDaRfzUVAk7DE_MD1cymzCRjjLMKasJxSs5dn9lTCSngel_zDD_75lxA2-i9j5SlDaCnhbP9JxOp_-F7VWCcaBQl6NYxPagLLAPKh338cqc8e49GU1MRBBzXNJBWiOR6ue7-6dEN1JdVO6ugiKyV2cdOHSMAZZ1lkeAgMArAOAoxbFPA5RJGLxNuPqhPsVLiW3n2kjU9mHrTdRXWQOPbbf4uIydnvOpPK5xJtrO6xYBoeLeDPTmllZTDz9IsWk2BtyGIY-tRSA1XLZlZhvNX-Wv6KUh-ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OD0ScWJ_H9RuIJWdFKsUQAxxyio_VQf7XSMBZKqLRFFk8_lAAZKsAOTrsHwXnGAKdKpr_Pg33i0TmO_CRrOllFsJ6v3u6Owhv0mdWGcVn32M1j05Nni3pIsWjn6OJnzyiab7wBW70XqmipIixW_lk8KeIlJ2FUDQCz7zcyhnX5MKY1zZbFZg6FeXxXWBgeznRobr0rJ3KWuSsAAuTzdPipkO2cV6TlEN1dqi0X2zi5_E07qe7RHP7NlOaVEM4-pFaVMdavl7GAbKNjrOFIhIPSbzzfBmVJAMkQYqmfCOm_EybfKlTlY0gdiw-qCQEtk_OEpKzQHloLDX24fYLCGqrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jq2WsKKg1xEIRWRHTX4Wi8opALDoFYlHsbCmeh0HrVzc9w7ntVpGt5SK1RF741NNMjcTHbNaMKaghiM0euZY745Dc7O9UihEOvqEusUHY-Siwgig0EJTO0zJyhGxbKG12HU1bd88wTut8tzMFATT2rScuYfbULYmuBzdwV5bXoFhqZPvYz0M5dLj3PLhVcgsyMvF7--gWbbcbnQ4V1REUsHDCVAC2QyOLFmIfNc5HHyI6TUH0nr_lL3r6CNWvSYiG15o07eAs1sd_PG7saK3nMJeIvGnyU-795HkNbgMGSrpz-WceLymM-1whvcUh6ccv4_epGhQXw_dmKODXl2Oog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHgVMLaiJbYK9BljLyMmGAEUTaLev4TQG--sJaw3RoxqetILFZbG4Y16nvPheuwQ5PAZeMPQIw7NqyVMJYe5mV_uIIYfvUtOuJFITmQbCra-bm_hG60ALlE7dgJvz28JD__QL1Jx2cRFR7PDjXsquUhq8fyRLnnGBUWJLfJ2x5AkNn0TWTxuY8HdBAQrxRyRZyTDhQKaKomAw99-IxpgxgjN0WSqVnF4krhJw1hHw2bI0wt3tV61-sPKk3TTu9IbXEyHK2cEWTwKVO8TIUwIHlxDtMpR965eBXATDxlgU9xgDu6dKEgdx2IZaMg99fCS_cfIsQ7xukl-vnQDzV12Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=dxwTci5fKusAD7nc4mcn2k56PzGR5lUjG5_sJKNuVTDpAMvht_8tnWvj_6EtOOCafPrzqCKzt5vdomsb8FMj8ob9xlPCdMsqVx_LqZ6tGBL-HwWf1flG0ozXka2sV4slZ9gAjLPv2Ubk9VyiigmC03x17gWSdSUg9-0tXoezH-t0slMO2HMK978XzpCuwUuXlMwLZpO8d53rRtk00m2PjoIBLSwzvWX4yELowtJ8UfW1QznhO4CU0ZHUg5XOkHAoeNeffwvV8ZKSBFEQWlcxXRlvxz-R5mvk5rFpL3DQB9OONR5Tfpx4jR3GAhviuc3DCzzDlyoQ_441mgEFhk6R_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=dxwTci5fKusAD7nc4mcn2k56PzGR5lUjG5_sJKNuVTDpAMvht_8tnWvj_6EtOOCafPrzqCKzt5vdomsb8FMj8ob9xlPCdMsqVx_LqZ6tGBL-HwWf1flG0ozXka2sV4slZ9gAjLPv2Ubk9VyiigmC03x17gWSdSUg9-0tXoezH-t0slMO2HMK978XzpCuwUuXlMwLZpO8d53rRtk00m2PjoIBLSwzvWX4yELowtJ8UfW1QznhO4CU0ZHUg5XOkHAoeNeffwvV8ZKSBFEQWlcxXRlvxz-R5mvk5rFpL3DQB9OONR5Tfpx4jR3GAhviuc3DCzzDlyoQ_441mgEFhk6R_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOb6KlwOUo0M5xydGsRoAwde2hBSdfg3gJ5-uRR80DkwLC2R544JIs5SK3PBTR_EaNz8JBMQDfofidTCtKdRVVF_sIl7oQx3MtXq3hNKYd85QaeWXWirUvXivCphWkOZ5zLSXOycbViK4PV7SGtKtnW5wOD5n2w8X1hieSfRlFE_SaSyPdxnC-APOeImC2FSfCI-wwuJ_QNyYBgtfXPgLPBt086rl19YDgUa74HHSQT-l6cyQpTzSnSePih0GuDp7JrjJd7tMhd8MfluQK_QVUhiiqh3pepRLeXkmxyMJafHCAFa0TDlIQiu37Zk6jY-Wu112vxeevJppeICC6fV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBgm5nwnFZUhlsKXVhwSrgw0KxOgLpApQ6fygDUTsN4d_wsixZ-nyPgw6lp3WzjiHYpMC7E4r1Eqm_IYE2wwzzO_pniHLiEWMS11_qJN-bbEIxBiY7kU5pqERXyNiMo9KVnLivVfYWMbE14ACOzkfazOyhDREVY0kRAAqocOEtaFQfwF4IzUZVooK7ui8paS3UKaJ7Yd77Ukh_XKP7SBIdvGZ0VgXb35uz69NTOuxeWKbHIHE0DhqAzLb818gEyXb510289q0amHmUsRBAntdIMY_aCFXZw2isGxGtEO6tnieBjAdZwhG1rRN4Kt9Qc4cHNotd4vQR9YRAhxxCzkeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R22yGV1XOBtPjzWONhs2Di6ahvYIBj4Hys3_egvbEfmVwgFb0cUCu2WCsUb15MwaZL0eTRGXJUv8l4fWSpaz7dOpvHOHhoAchUDNNHMbS5cKT-tBarq33x62GM3xBB2js5os6kyd_BL08bZZNqnzLygjBznPx9US8ih8L24rrL8CetP9mg_iw-F8YwLBMETl6gFc-HzCktZxe5Zmbaw2ejLZw8X5KGy1pF488o_fWpK5Kt3-Eft3vgZokLMK-Frw2Ys1ykfsLfYODzJn86rA9IdVKxZUtZgRP_JXNVRembldx2QDRV8soI6xqKWTCeg9HmUo_kJbamsywYbqDgdJUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4yUqLltfGUMk_pZZiDpkRU1_ammcUeIZP4CRMcNSSq_Nmmz8BHEF_f5oXDrW09QbRTqP4ekz-QoCcG_tI7Dmsi3U0NHNwBz5IbbDcH_UYDbHKoNeY4vAab2gGBHV-71bHElOELRTCCPVoLcxaIhDKKMT2___oHjDLZvMbSk5heqo7F1KVkzYCEIzHcSqKYNSFMYP_3U81NxsmSWcmvrRSciefTKhOYeXqsmR--MTwcbtqvmGzZa1QJqa386e1xz8KCNzOSamAoSUKy4Q1HeM82KeZtTydEdBC07AQvrO2w8Dx1ONPvRIbGiBDneDGX3v8UzvAggMvrP3xfM9uecFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSsN8k9Fqu1UV2gnRAs2ricGRpZssxxF3xZ_QzpeBio5MQkOJyQzucZDUcFXXfBG5LYW1W8X5PXreg1x6TRWMqBvA_KnSIwV0F89sbbZNl6jxMDUP-ActWU8WVS4MHBZU1qGMe1PkLTVT9fs4q596RAVgTM_MtJLok1Hjl4cIE6YkAJbR7mi2dMWBGxFWuaZJofPzm0iANF3JrAnlYj3EHsjK8TP9a5zjxN2kmrrG-t1NRwjzML6W8_mT4AQF1HiIgcSKVfCaI7vomuw5XSwngTHqPRdN2BU-9wpirqcqezo76WWa8HJUdNiDAgzhtJLN5ySpf8jRNIwn9bFzqQ86A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOS6Al0Mdiiy1ukOGrUD53CQUAgAG6SwXmXmUijGCUxLjXBMN5mO5sE47gOnyC4BdKUIL7dJ3oa5e_ANYHrO-sTrRX3yCvpxHZs2RW3newLBR6qB7B_Lv5oi1HCkFEbU5RtCmQPT9051566VtDbrpfTySqpncGzuUe9h_0DEQAaRDyAVrE9UGPUCRh08Inii6t5kRFLLeWy8E80FJND_iOXrzXXm61zcTe55Y9lFowbDhAOxzX-4xzUWZlyTWq7m3Gi32mTQo576nhS4gA7R4WqXLWDManOj5eVRtx9NSIcfYIjYF0LJ2mdW5e0zDk_mp4Xn4tY6s7BxTnVjkZELcg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=WOrmE7r6BarBYJFKxopklPJ44o5SGmZGH8vXHgCeMJ_qbXeVgc1gv7NJh9tqstFC2rAshL-FHLcKVejmEO9uql9yCYqCZyy9um-vTs84OGhIClUayP3fCbt7worbnBZChT9e0udqNxXPcj51N9yWJWGoKZnFj1owWX29csuwdyQxNIxPwskdynp3-J48EzB_k-egePzpz-yHBz_eaPZ6hZoP5KTjPBpKcobWsWQxk3IdoMaWPgEkY3t84Fx7q28A50EpOfUwlYc7bOM5ORApbahJ7LE1JsUHFu_aH2E1poNaeZOxAu6qM2iF6qe2ndyhYTS0cAw64TRRxicsBoXcMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=WOrmE7r6BarBYJFKxopklPJ44o5SGmZGH8vXHgCeMJ_qbXeVgc1gv7NJh9tqstFC2rAshL-FHLcKVejmEO9uql9yCYqCZyy9um-vTs84OGhIClUayP3fCbt7worbnBZChT9e0udqNxXPcj51N9yWJWGoKZnFj1owWX29csuwdyQxNIxPwskdynp3-J48EzB_k-egePzpz-yHBz_eaPZ6hZoP5KTjPBpKcobWsWQxk3IdoMaWPgEkY3t84Fx7q28A50EpOfUwlYc7bOM5ORApbahJ7LE1JsUHFu_aH2E1poNaeZOxAu6qM2iF6qe2ndyhYTS0cAw64TRRxicsBoXcMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgFLNj-DUhB5VhvXWy3k35SVJMAowu-PqvpCGEWR0tSpspJsYM6KLRyeLIMcWCdCbVvxUyxmbKiz8thZKq-LaHrY2ddsfQOsoK_hbAVCjiPfG8Hqhq5leLsd_2hMzrh2_NSsfvk9ADH6fDKYFu8QijI9DApOg0G_oZB9biu7yFz--y7ApmEYn7tHZeNI9oWcTG20d7D_GbNdc6JkCqXWbkfe7LT8NRwGAvt_9hLsa4NHH_ip4kLqS3W4KtHsO5ziMz8MvyP_YvO72mmtUbnl7U5QnbCT2BfuK_AtlunNj1YOG9nr46YPchJ4jNjhTw7JGaqRRXoqhUwFhG_gcxExUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRHQuyAKpQ5EDlPhuCTi_4_R-WDnB3Pqe0dUyyBmnjvnlzsBIL9uZPjDEy0edhYkDAzyEHKnjaGTr2DiKhTcOiwKCgIM6w6ESTJO3GW_nqA-spztyUWPpmMzg0iwye0al7nwBOfCIiJ2aZeA3bhKSbk6E73swHTBg2uqgK-0M16jpBJxFnLhzy_8gjERKsLSMxgOOxR5d7kDi5h77KwcmcROi9cL737RcMt7BP2fhhbXpq6pm2SCwwV5QRNT3CfhMRLZ6Bwi7L_qkF-ZsrniRfgOYxj3ffA4C_NYmnjcnG4g4nbfp25VVcSSqlds-8_V2KQFUIexa8UDCeYgyCA15w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZqk88En88Vruh0nFddBCQP12x8QMYHHddwarI8c8tVO4_pbRaNnuEUq_mN5BTtxhp47mxCYDvG6LNNIbyrdFLzqhZJXZTUKPVx95damHpsLOIxKz-s1ASiQ5ie2zDvXM2A8PCDgUtXhowYwg5BI4LAXod8SQBzRpTyl9w2qQcgQ1lkJ63a007yjuZCCv1wJohKWLT1oDw121sxOaSDpYxa53Sc_f0f17QqGX_lFa3Q74398zsriY7Sf1xZfpFvhY8qnQP6rWCEVhxrhNgfQSdmYbABfi7gyvALqrIue0VFu9qSdzemm9IorkMw9tQBRVurN5m91AyDuUiGF5xp4Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBBaA6w1IfxzAfupaCINSHiJ6m1WQEQX1V2FvJaNcbtZaHGZpAwyhSbfymvsizlImc17vkiAKw8kM9FnOOJqx7yJ41uj-ME_ESw5OY88ZXXv30knO53pZL3QqbsJqQyApbMlzu-ZyV28YpZDVcWV_jRyDUorYzUaEx5BFBBuUuCYIX9NLOD6hByPhnT6O0kYVV5Rkm8jeIeAH87Qu5TRSK7ddCGR-o-j15NfTzCeCAIWZNoXnM-heLEh2nU2jpaxo7DpG1FFGMy1mDugbF2epYIiIH-_ymj_IOdmfbcuhWXj0zx8X0JX-EhtJa9XiLC3f18lTWU3_1UEHqJWynx2ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTW3d0f9DOybIKZwjgiEGXkf6aTJlHLxfCxjhX5cMLrC8Gpf50Q9vnrVwmFGYcxXcizoIQ58tgczAGK7XUtQocNSbRovVlLCYMzHly1UhAwL3YLj-lclqexpJr0xRhKdhgpSH9SWfAzjLgKrwPgej4pfyCrV2HkFu3f2nZ6pnVhsA-nJVt-kdzeLC1ie_sCpWRw-pVy_1GSnl7I71qQNAdadCELQzy0nLJlsh3i4aZiCTU_j3Eoci9xRx4xSGSf6TY0GhmVpfvJK2tXzrgbiAE66KMSTlIidZjs-2UP7Nsn5SuaveaMuoWYQB58TnuT3e1ntS9OuasADdaGn8Uc0Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
