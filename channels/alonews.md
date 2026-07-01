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
<img src="https://cdn4.telesco.pe/file/TKzzx13pQ25N9g9POIjlcvconfMgALIcTWtwV4OBNuhGcZZYkulVB1snPIMpNaqpDdVSl_cjziMJARugr5g2AQFUGhLIU1LR6pumS5yxuqqns5K91-3mW_B8VS1chc0HKpL2Rop9gLcqnJ8zsZxtcNeJF4LMnr2o0hJpYJsnt3gzLcHBpYzncTmLSQL5wb7VVPit-HvBRzEphRNonWtF8PcOy1GIQ6z31SVn2NzFnh2QKzv_gkQZJp7Ry2tzO-g08Ck0l_cUEHv55yoAh0ehS9KW0lGPUGPLpzkdtva02R1XZTCbj0-2wNQ0aa1v9C-0cFQFfu5CLY9Y8h2OfMHCsg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 943K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 00:15:32</div>
<hr>

<div class="tg-post" id="msg-131355">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ce1f21322.mp4?token=MLZQATgGTHYVcYNCUOjr92B6lUERsGKDU6xOg2T9QLlt14Vu9got_yvlDq_CKga6erz5-8Ind7175mx3LAIFZsOnU0EDLYiL2SJ0BPmbDJ3o2CFtR_DEmoYMNRGI3Yyap56Fbd6QZSlNq3bvyLiiNjaxqwpRPiDZgYS7X3WPxHeuOedGVp3t_UtjRd256ARtcXfmZR1y8zAy2274tle5gNhtmPZdRslwJN78VmuYHu4HCfxC3xhwUYmjKYqpyLbH16LghiVQjv0onBuywL0NlNeBoxJLxNkLkUuGuG1ITCU6j5UuIxvcMHSZUbfI6vZy7zOqfdFsccuRKp2KaK7BY4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ce1f21322.mp4?token=MLZQATgGTHYVcYNCUOjr92B6lUERsGKDU6xOg2T9QLlt14Vu9got_yvlDq_CKga6erz5-8Ind7175mx3LAIFZsOnU0EDLYiL2SJ0BPmbDJ3o2CFtR_DEmoYMNRGI3Yyap56Fbd6QZSlNq3bvyLiiNjaxqwpRPiDZgYS7X3WPxHeuOedGVp3t_UtjRd256ARtcXfmZR1y8zAy2274tle5gNhtmPZdRslwJN78VmuYHu4HCfxC3xhwUYmjKYqpyLbH16LghiVQjv0onBuywL0NlNeBoxJLxNkLkUuGuG1ITCU6j5UuIxvcMHSZUbfI6vZy7zOqfdFsccuRKp2KaK7BY4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : کنترل کامل. ما کنترل کامل همه چیز را داریم.
🔴
این فقط آغاز دوران طلایی آمریکا است.
🔴
بهترین‌ها هنوز در راه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/alonews/131355" target="_blank">📅 00:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131354">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a937d249f5.mp4?token=ZtbzlRBiShOYqk2cFeKfdgkl2_dpmm6I2t6CO0CXDCloIp966LAFz55b2rCg4zeJVZmlY--uSYi4AkY0g3UQmBP6U4mg54bd5r0a6X1JZZZWlCJaDCzptNc6vbRyuNU6HEz88EBNNjkdSyTgIFQGLrDb0xfv10ngv5NZJa3Ohs91oE5duuiD-S_kStqR0F0_g_RaQ3SiREWNnO_aXLkPyWtlNNEGSz-jjuZvG5HZVyCJO6ADKFjhi0NPaz7_pyPjpCL5G1XSQTP485jKF7pwnzVpyIuWrVVCDspNUY4zVcuwFSOK-GLim5EFuugnP2FgFcCRjW6hgZB0HTQtqmdi0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a937d249f5.mp4?token=ZtbzlRBiShOYqk2cFeKfdgkl2_dpmm6I2t6CO0CXDCloIp966LAFz55b2rCg4zeJVZmlY--uSYi4AkY0g3UQmBP6U4mg54bd5r0a6X1JZZZWlCJaDCzptNc6vbRyuNU6HEz88EBNNjkdSyTgIFQGLrDb0xfv10ngv5NZJa3Ohs91oE5duuiD-S_kStqR0F0_g_RaQ3SiREWNnO_aXLkPyWtlNNEGSz-jjuZvG5HZVyCJO6ADKFjhi0NPaz7_pyPjpCL5G1XSQTP485jKF7pwnzVpyIuWrVVCDspNUY4zVcuwFSOK-GLim5EFuugnP2FgFcCRjW6hgZB0HTQtqmdi0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما بزرگ‌ترین زیردریایی‌های جهان را می‌سازیم.
🔴
ما در زمینه زیردریایی‌ها و دیگر موارد ۱۵ سال جلوتر هستیم
🔴
ما دوباره با کشتی‌ها شروع خواهیم کرد. قبلاً روزی یک کشتی می‌ساختیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/131354" target="_blank">📅 00:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131353">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
اکسیوس: آمریکا تلاش دارد ایران را از دریافت عوارض از تنگه هرمز منصرف کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/131353" target="_blank">📅 23:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131352">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66ae0f5149.mp4?token=fn9OpLVPtPHqiWWsVNOsPP1OJ9yd_w4TGB0S2lw-xj9Dg9i4oX-YXpT8MLmvSfzgv2fSXv-IpqoCJcFUj5vJu2QqiTLAxg6iaaAY5LlHLCDVH3p2P6JXj5Yh2N2p68YOWWdBQM56tjbfZ0S6VfCSCCulQ5TZZoWL1ojkU3NFtRnRrV4GinyBi-b-X86H7vb0AjzPfESSM8BEnhQigwO9Izn-bKK5wyRXPdXqaIo6MJfUKpaF-RiY-xTw3REXacy35vY0j4h2FldU0gGniuHiBOWCq2TCtjwqXaYCAqlSUrlAykYDS4vf5E2OggJjVNOCAoY0uTAfd0Ynx5tVu3C_dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66ae0f5149.mp4?token=fn9OpLVPtPHqiWWsVNOsPP1OJ9yd_w4TGB0S2lw-xj9Dg9i4oX-YXpT8MLmvSfzgv2fSXv-IpqoCJcFUj5vJu2QqiTLAxg6iaaAY5LlHLCDVH3p2P6JXj5Yh2N2p68YOWWdBQM56tjbfZ0S6VfCSCCulQ5TZZoWL1ojkU3NFtRnRrV4GinyBi-b-X86H7vb0AjzPfESSM8BEnhQigwO9Izn-bKK5wyRXPdXqaIo6MJfUKpaF-RiY-xTw3REXacy35vY0j4h2FldU0gGniuHiBOWCq2TCtjwqXaYCAqlSUrlAykYDS4vf5E2OggJjVNOCAoY0uTAfd0Ynx5tVu3C_dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اسپانیایی‌ها — اعضای ناتو اما نه اعضای خیلی خوبی از ناتو.
🔴
آن‌ها به خوبی رفتار نمی‌کنند، اما یاد خواهند گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/131352" target="_blank">📅 23:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131351">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
جی دی ونس: در حال حاضر، مذاکرات به خوبی پیش می‌رود
🔴
کسانی که به دولت به‌خاطر مذاکره حمله می‌کنند، همان افرادی هستند که ما را تشویق می‌کردند چند بمب دیگر هم روی جاهایی مثل افغانستان بیندازیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/131351" target="_blank">📅 23:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131350">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ
:
عربستان سعودی و دیگران در حال نگاه کردن به چین و سایر کشورها برای محافظت از آن‌ها در طول دوره مدیریت بایدن بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/131350" target="_blank">📅 23:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131349">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cca332fee.mp4?token=qDjcF_KsyJM6FZa9URbDELYmp5bMex4hxq7ANXVHBWBWAfmuv3AliOMFNwukUFn3zTwhIrEURna8XyNXMnVuutAm-WIBwjOvYg51ykcSEWMXZayiMYIAPnnc2HGLCAJDV76JX6hQKXQhGzLi81GLZkztxHfr5qr3dAuFQKrO95Nxn74Y4ry9IGWEBjW3qppOn7rLHDA_pYIlrOv_yWYrZUrkt3zTXXUBub_ivvvCnaRItkabM59uGMc_W6ZZkSf-E3XzlB1615PVTQcqBVLkMmhhFE4TYdQsNz_WWkLoyArFCULADErBhi6amJz1NulxMRYF94W9n-5Y_16sJHqJ7jEapxDyIgjeppOuVcuw40FJzKQI5bfagGMhL45DYNaiI-FjEjVLYj8YMjzkADATLMIr-lNPPNTAOMbHNaSRemJuSVyCk_16DXvQLVHxIPQK51iuWRKVtruIzePZQ1M2VHty-OpzSzk5g5frC-_kycbvtLNoj4QLEt6pBvQIKdkAcpfESOe-zbBh4buEu-CXBKK9AgyrBtCbTxH6nkluK9uY3ff2o5NGDiVl-D1Ekqogx5rX4bLPQBbMlFNoAhgKSnwN6EvyOpS7_IJ-63rASbUfXSrf9lTQrTl7_BF36GU6Y7wR6TlkozBL1DL6c4VOf_ssiq_XvOjmk4PJEetsl-Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cca332fee.mp4?token=qDjcF_KsyJM6FZa9URbDELYmp5bMex4hxq7ANXVHBWBWAfmuv3AliOMFNwukUFn3zTwhIrEURna8XyNXMnVuutAm-WIBwjOvYg51ykcSEWMXZayiMYIAPnnc2HGLCAJDV76JX6hQKXQhGzLi81GLZkztxHfr5qr3dAuFQKrO95Nxn74Y4ry9IGWEBjW3qppOn7rLHDA_pYIlrOv_yWYrZUrkt3zTXXUBub_ivvvCnaRItkabM59uGMc_W6ZZkSf-E3XzlB1615PVTQcqBVLkMmhhFE4TYdQsNz_WWkLoyArFCULADErBhi6amJz1NulxMRYF94W9n-5Y_16sJHqJ7jEapxDyIgjeppOuVcuw40FJzKQI5bfagGMhL45DYNaiI-FjEjVLYj8YMjzkADATLMIr-lNPPNTAOMbHNaSRemJuSVyCk_16DXvQLVHxIPQK51iuWRKVtruIzePZQ1M2VHty-OpzSzk5g5frC-_kycbvtLNoj4QLEt6pBvQIKdkAcpfESOe-zbBh4buEu-CXBKK9AgyrBtCbTxH6nkluK9uY3ff2o5NGDiVl-D1Ekqogx5rX4bLPQBbMlFNoAhgKSnwN6EvyOpS7_IJ-63rASbUfXSrf9lTQrTl7_BF36GU6Y7wR6TlkozBL1DL6c4VOf_ssiq_XvOjmk4PJEetsl-Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
ما اجازه نمی‌دهیم کمونیست‌ها راهمان را ببندند.
🔴
آن مردم، کاری که انجام می‌دهند، واقعاً احمقانه است. آن‌ها واقعاً احمق هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/131349" target="_blank">📅 23:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131348">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/709087d4a8.mp4?token=aK7xOaoiqPHEDi6lCIPjFatG7NXU6kaULhNqhS3OczjdKbRo75D6qMdn_RjQiA1AlYp02oPuGuYSMsXGbwllsv3JfrwGVi9L79kzK1X3wUJpoTo9hNE-6gnmRtdziMT8kcPcvn3Wpz7-wgDvGLQVS_5ZWI7R1lRWkItENpq6hkuKjlEz0iVuHL25PDhlNEZ7Ke9lUcLeXVKTbyhT-O6a-M7wHZjAHLFQKTVMOfprn4LH0OwW1MUuPjR9MaQBq2sXeGv9dCX8wCWDITBLL-HQH4QaMHHSY4G7cCmZSpLYExWpwLzY7ZchTFvGdhYMRtluc6u_ZOvzEgRo4lEaIBV07A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/709087d4a8.mp4?token=aK7xOaoiqPHEDi6lCIPjFatG7NXU6kaULhNqhS3OczjdKbRo75D6qMdn_RjQiA1AlYp02oPuGuYSMsXGbwllsv3JfrwGVi9L79kzK1X3wUJpoTo9hNE-6gnmRtdziMT8kcPcvn3Wpz7-wgDvGLQVS_5ZWI7R1lRWkItENpq6hkuKjlEz0iVuHL25PDhlNEZ7Ke9lUcLeXVKTbyhT-O6a-M7wHZjAHLFQKTVMOfprn4LH0OwW1MUuPjR9MaQBq2sXeGv9dCX8wCWDITBLL-HQH4QaMHHSY4G7cCmZSpLYExWpwLzY7ZchTFvGdhYMRtluc6u_ZOvzEgRo4lEaIBV07A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
در 4 جولای، دمای هوا تقریباً 107 درجه خواهد بود.
🔴
و من می روم، و یک سخنرانی واقعا طولانی دارم فقط برای اینکه نشان دهم که می توانم هر کاری انجام دهم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/131348" target="_blank">📅 23:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131347">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/600b8e0075.mp4?token=sI6IoD3V-EKRp9dWB570M0Wl2oDucLLoIjSnSbIYne_sGMmnClz4KL9LkNDkrk6CvtR60j3hZ58I592N_qJaKdlu6lAOwx6G8YtiiIMSWLEcflOiRp6KI4GoFFqDMFeJD0L1P6JqJuOMcubknVI7FDg5-8YdY6NpZGml-EtqCX7bnN0i8midsBDqzZvKOrH2Y3MTgu8N78ta7wk5kaVMLaCbS8OU3WiVJT7w4at6PoWotK5E56u9V9BdbOj7JVd2jLOIcNRSbcy4eW9d7bA9mLX0o-mgN6WkfRHxWw1p1Z-wnIxGobFjgIXp_6s6Ua9iVi3wIyRHTwmo0YpUCq_KBnlGC97IHFJeJqaegk_Xl4ztkUJr0EII4BtuosPFwRI_vz3tfAZXDOCPOkcmUM1cVAUoDeOoETz1NbO1DX5tNnzIBTagil-jyOlR2JzF78wq59Yqwn0AcfoZN2itIjt-zTnN9kUGzAtsWT0Q44adkTyhHeB6GHzYo1d4pJ_9pCcNgaNabDvCGFMbZsaQWLUHmJKi3CNCE8mIME3qs9HWRic0fDXltSGmARfu0-V_AiespE7zhQXa7ShHsUkcEfeg20lYddAezVqW0D1hDguVijjPfhmqsWy7C9EljEZh0KkGmGa0ujD6MjmXfbb-Aftc0M6ONDWSOekLhqsCJDWcBaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/600b8e0075.mp4?token=sI6IoD3V-EKRp9dWB570M0Wl2oDucLLoIjSnSbIYne_sGMmnClz4KL9LkNDkrk6CvtR60j3hZ58I592N_qJaKdlu6lAOwx6G8YtiiIMSWLEcflOiRp6KI4GoFFqDMFeJD0L1P6JqJuOMcubknVI7FDg5-8YdY6NpZGml-EtqCX7bnN0i8midsBDqzZvKOrH2Y3MTgu8N78ta7wk5kaVMLaCbS8OU3WiVJT7w4at6PoWotK5E56u9V9BdbOj7JVd2jLOIcNRSbcy4eW9d7bA9mLX0o-mgN6WkfRHxWw1p1Z-wnIxGobFjgIXp_6s6Ua9iVi3wIyRHTwmo0YpUCq_KBnlGC97IHFJeJqaegk_Xl4ztkUJr0EII4BtuosPFwRI_vz3tfAZXDOCPOkcmUM1cVAUoDeOoETz1NbO1DX5tNnzIBTagil-jyOlR2JzF78wq59Yqwn0AcfoZN2itIjt-zTnN9kUGzAtsWT0Q44adkTyhHeB6GHzYo1d4pJ_9pCcNgaNabDvCGFMbZsaQWLUHmJKi3CNCE8mIME3qs9HWRic0fDXltSGmARfu0-V_AiespE7zhQXa7ShHsUkcEfeg20lYddAezVqW0D1hDguVijjPfhmqsWy7C9EljEZh0KkGmGa0ujD6MjmXfbb-Aftc0M6ONDWSOekLhqsCJDWcBaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: کانال پاناما گران‌ترین چیزی بود که تا به حال ساختیم و همچنین سودآورترین چیزی بود که تا به حال ساختیم. این ترکیب خوبی است.
🔴
کمی شبیه ونزوئلا. ما در واقع با جمهوری اسلامی ایران هم به همان اندازه خوب پیش می‌رویم. شاید شنیده باشید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/131347" target="_blank">📅 23:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131346">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ: اخبار جعلی اخیراً نسبت به من بسیار مهربان بوده‌اند.
🔴
وقتی شما همان کاری را انجام می‌دهید که ما انجام می‌دهیم، آن‌ها باید مهربان باشند، حدس می‌زنم.
🔴
من حتی با تئودور روزولت صحبت کردم.
گفت: «نظر شما درباره کانال پاناما چیست؟ آیا آن را بزرگترین دستاورد خود می‌دانید و در مورد این واقعیت که دموکرات‌ها کانال پاناما را به قیمت ۱ دلار به پاناما دادند، چه حسی دارید؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/131346" target="_blank">📅 23:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131345">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ: اجازه نمی‌دهیم چین آبراه پاناما را تصاحب کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/131345" target="_blank">📅 23:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131344">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8648b6f7.mp4?token=E4HU6PUhvRchw9Rx7BBtolGSemXYJdQLR0wiUzOhna7fFvil3HoFlDgX-7vcv5bH_HDcPTRFsaHNdvRQ4LcxfRoPVb49esK72pQLwkwb9uPXYW1RPEtO0vNh5rmKFoNsxlFNRmt7Nh64enN7nEl7IOj3ESdV73TRYjy9gIwVeCRbPrThaEUu1mcStdwAOKXiutuX6i8tOifj6dnPjiQUGSr5aB7vInpGI7cRcMv11kqnXlONYxe82C9jkBbqNnZpuRTtV6UOEnvyVUo6q5T_9QfWjU7bEK2wz8whnawP8oQtiT0SBtMWYYq_TEeb7NjRB4ZPRcNmvsTDleDNr801bkQ0SBxnpVpuSN_KmMzOePQhaa426l1MtYE85vxelWkgiykF8aeEpFhMmzPPxdnFHjfXWH9Ix5dtdRbjmvnwtg_Hz0RIavtiDWMUEdQz1Q7JzRFMAIGEcyaiwXCIBh-KrVYPPZQdL2bmczpmhMnDhDvz07edkY5jDjZMBkAr8KqW70eyl6zq0tTk7O1PVM98T6AFhSg8eZrGG62FBupnLEt4T-ytnUivTaJrM_ynPu8yHq4qbS-gr3gDENknO96W6mFio1qTUBM3T6yfQDB-CV-sDhVrMGj5Osp26ozt7ik3PJEX27IBmFqXWJoHtXDs5ms7GGGWqQGwopoVLvSqm-E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8648b6f7.mp4?token=E4HU6PUhvRchw9Rx7BBtolGSemXYJdQLR0wiUzOhna7fFvil3HoFlDgX-7vcv5bH_HDcPTRFsaHNdvRQ4LcxfRoPVb49esK72pQLwkwb9uPXYW1RPEtO0vNh5rmKFoNsxlFNRmt7Nh64enN7nEl7IOj3ESdV73TRYjy9gIwVeCRbPrThaEUu1mcStdwAOKXiutuX6i8tOifj6dnPjiQUGSr5aB7vInpGI7cRcMv11kqnXlONYxe82C9jkBbqNnZpuRTtV6UOEnvyVUo6q5T_9QfWjU7bEK2wz8whnawP8oQtiT0SBtMWYYq_TEeb7NjRB4ZPRcNmvsTDleDNr801bkQ0SBxnpVpuSN_KmMzOePQhaa426l1MtYE85vxelWkgiykF8aeEpFhMmzPPxdnFHjfXWH9Ix5dtdRbjmvnwtg_Hz0RIavtiDWMUEdQz1Q7JzRFMAIGEcyaiwXCIBh-KrVYPPZQdL2bmczpmhMnDhDvz07edkY5jDjZMBkAr8KqW70eyl6zq0tTk7O1PVM98T6AFhSg8eZrGG62FBupnLEt4T-ytnUivTaJrM_ynPu8yHq4qbS-gr3gDENknO96W6mFio1qTUBM3T6yfQDB-CV-sDhVrMGj5Osp26ozt7ik3PJEX27IBmFqXWJoHtXDs5ms7GGGWqQGwopoVLvSqm-E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره داگ برگام، وزیر داخله:
فکر می‌کردم بسیار تأثیرگذار باشد. راستش را بخواهید، فکر می‌کردم همسرش کاترین حتی تأثیرگذارتر باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/131344" target="_blank">📅 23:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131343">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/641158562d.mp4?token=iyPdCq15vn9pu1m3gdsyFoopuDW2BOCOZVx6pIQjpeTLSuvOIB8rk4MtlO8gMAUCVdf8U9lZfoTI3Q_yPEcH_PMzANJA0cqp0qxbApLFmdhMivveF0MadNtyqQs6UOfMZ9DVBnvDEJu3zVsWVn69SUgq1fncSMMrRYlH5pmgf4LJy216xgF6BCv1Dtm2NCawaCbBurvvHDS-UHfnTd4h9rX-FXDXw4AINmyxLIN_f2JSaPout5oDTqWJsNo9sf7BR2nAt0ADNCZL5hO1Q05qRVvrnxNuQGoO73VxmAJC920P9uH3UFvWu16XW4KdUFPzwDSKMC9FA5sQoO7oMld4QIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/641158562d.mp4?token=iyPdCq15vn9pu1m3gdsyFoopuDW2BOCOZVx6pIQjpeTLSuvOIB8rk4MtlO8gMAUCVdf8U9lZfoTI3Q_yPEcH_PMzANJA0cqp0qxbApLFmdhMivveF0MadNtyqQs6UOfMZ9DVBnvDEJu3zVsWVn69SUgq1fncSMMrRYlH5pmgf4LJy216xgF6BCv1Dtm2NCawaCbBurvvHDS-UHfnTd4h9rX-FXDXw4AINmyxLIN_f2JSaPout5oDTqWJsNo9sf7BR2nAt0ADNCZL5hO1Q05qRVvrnxNuQGoO73VxmAJC920P9uH3UFvWu16XW4KdUFPzwDSKMC9FA5sQoO7oMld4QIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من دو تله‌پرامپتر (دستگاه نمایش متن سخنرانی) دارم که کار نمی‌کنند، و اینجا ایستاده‌ام
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/131343" target="_blank">📅 23:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131342">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
قالیباف علنا به تندروها گفت خفه بشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/131342" target="_blank">📅 23:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131341">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
قالیباف خطاب به مخالفین مذاکره: بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید.
🔴
نه در دیپلماسی کمک می‌کنید؛ نه در جنگ!
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/131341" target="_blank">📅 23:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131340">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363ab4d62a.mp4?token=Wxa4r53ppiRPX-mPvddKiKmoGVwDG5NCvqfUPsYCVHxwHlZGBVdbbjuhEqXTVzK9JW9b5Z4IASXGifRYZM0fHFacGFzMB9lIQIqsa9OYuJ_HsiY0nxJJoBzEpcYdn8PwXdQWCM_H9NfAjy14Gish2yvlhvz37bD91t95UOBVxgfJF48CHw5RJfdVM63oeqydzfvp65yydclCqbNLYXGWHTa4eCU0lstSZRaWYM6DdJ3cSpPq8DpYLt9M7JO0m3Zqjxl6yPRBAib0WNzboJK-_teUVy5dD2i5Ij3r0HVshcj9PB_zplyNLqK8J8xV93nW8Kd51KXtG1SNFwlBjj6wFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363ab4d62a.mp4?token=Wxa4r53ppiRPX-mPvddKiKmoGVwDG5NCvqfUPsYCVHxwHlZGBVdbbjuhEqXTVzK9JW9b5Z4IASXGifRYZM0fHFacGFzMB9lIQIqsa9OYuJ_HsiY0nxJJoBzEpcYdn8PwXdQWCM_H9NfAjy14Gish2yvlhvz37bD91t95UOBVxgfJF48CHw5RJfdVM63oeqydzfvp65yydclCqbNLYXGWHTa4eCU0lstSZRaWYM6DdJ3cSpPq8DpYLt9M7JO0m3Zqjxl6yPRBAib0WNzboJK-_teUVy5dD2i5Ij3r0HVshcj9PB_zplyNLqK8J8xV93nW8Kd51KXtG1SNFwlBjj6wFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ: «باید به شما بگویم این پرواز افتتاحیه‌ی هواپیمایی به نام ایر فورس وان پس از ۳۷ سال بود. این یک هواپیمای عالی است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/131340" target="_blank">📅 23:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131339">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
قالیباف: ما خودمان در مجلس قانون تصویب کردیم؛ شورای عالی امنیت ملی هم مصوبه دارد. بر اساس این قانون، به هیچ عنوان به سایت‌هایی که بمباران شده و آسیب دیده‌اند، دسترسی داده نمی‌شود. این قانون است.
🔴
ما هیچ امتیازی بیشتر از دسترسی‌هایی که شورای عالی امنیت ملی تعیین کرده، نمی‌دهیم. طبق قانون، تعیین سطح دسترسی‌ها بر عهده شورای عالی امنیت ملی است و آن هم چارچوب آن را مشخص کرده است.
🔴
در حال حاضر، آن‌ها فقط در دو مورد حق دسترسی دارند؛ یکی نیروگاه بوشهر و دیگری راکتور تهران. دسترسی‌ها فقط در همین حد بوده است و ما نسبت آن متعهد هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/131339" target="_blank">📅 23:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131338">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
قالیباف: ۶ میلیارد دلار ما در قطر بود و ۶ میلیارد دلار بعدی را آن‌ها تقبل کردند
🔴
می‌گویند چرا سوئیس رفتید؟ خب من رفتم آن‌جا اوفک را ونس امضا کرد تا پول‌ها آزاد شود‌.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/131338" target="_blank">📅 23:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131337">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
قالیباف : می‌خوام تو سفر به چین
روابط تهران و پکن رو قوی‌تر کنیم و به سطح یه شراکت راهبردی برسونیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/131337" target="_blank">📅 23:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131336">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
قالیباف: مذاکره‌ای بین ایران و آمریکا وجود نداره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/131336" target="_blank">📅 23:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131335">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
تا کنون رسانه های خبری گزارش داده اند رشاف در نزدیکی بنت جبیل و بیت یاحون در نزدیکی صور توسط ارتش اسرائیل مورد هدف قرار گرفته اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/131335" target="_blank">📅 22:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131334">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ترامپ از هوش مصنوعی تئودور روزولت می‌پرسد: آیا کانال پاناما را بزرگترین دستاورد خود می‌دانید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/131334" target="_blank">📅 22:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131333">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0VTfWo03Ua2QYw-Wv8wn1-SvxaEklyY9_c_ZfHf3cX9w5TjF3AkBB0aX4lwf8qdJrqFUw5OB1Eq1dVlICBJcL7-inQnLf1zNQmRNI9xC_DeynczuNz7saQ7p1xQaQt1td_r0FwYYtdwtuSu5cdKAvi4IsSmB-7Abyf_Bsi_H0CeKAYzPc5Mrw9RiUeqlE-hih-DHJ9aYlCBsGtIzhxDCMOx2XZQPDin8R-4eqjRpXA1GJmntBqXPvZXiozMyb_tV4z4zpyAD3OsljCklfM8say4549g7kru44Iqo6T97p9_ws6f8eG67XwvD6ws5zoUTLgsTiir-tTs_9g18ftl3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/131333" target="_blank">📅 22:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131332">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
نخست‌وزیر لبنان: به‌دنبال تعیین جدول زمانی برای خروج اسرائیل از لبنان هستیم
🔴
نخست‌وزیر لبنان گفت اولویت بیروت در دورهای بعدی مذاکرات، تعیین جدول زمانی برای خروج اسرائیل از لبنان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/131332" target="_blank">📅 22:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131331">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نخست وزیر ایتالیا: من ضد آمریکایی نیستم اما در مقابل ترامپ زانو نمیزنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/131331" target="_blank">📅 22:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131330">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
قالیباف: مذاکره‌ای بین ایران و آمریکا وجود نداره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/131330" target="_blank">📅 22:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131329">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❤️
دیدار رضا پهلوی با گروهی از قربانیان سازمان مجاهدین خلق، جوانانی که دوران کودکی و نوجوانی خود را در «کمپ اشرف» در عراق گذراندند.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/131329" target="_blank">📅 22:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131328">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpXeq9fiu-R285Zd_xcFX7oN6oPYDREkBQ98sipskHeR1H0g9pBkmLTVXL8s76kSNYG78Eeb-C0_LEMKZ4cUmGcYkiTSDQHNSfE17p2TJIzeDc82SC_BglO2noA6bSHwsPWY5kIrgqVyF6wkWRxETqHIk3UA5V8nS4c57H8BP4q_bS_GOmfcFobv1kFlbdoQ5YnmfqKqe79vdYy35PlD7W2gxlYaVIlHVQwKdK-UTRWo230V764khaGbVh3Hj7GnZ7tfVtNHmziiwFVXuEsVVOqoid-MfG7_6z2kXQCxMMc8EJpBFeD4IRwqNMzBOpeYm_aHWqVXTkJcHEFIff5_IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم ایران اسفند ۵۷ وقتی دیدن براشون قبض آب و برق اومده
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/131328" target="_blank">📅 22:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131327">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✨
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید
➕
قبل از خرید، کانال رضایت رو ببینید خیالتون راحت باشه
🌱
@vpn_express_supp
🔄
در صورت بروز مشکل یا نارضایتی، موضوع از طریق پشتیبانی بررسی و در صورت احراز مشکل، مطابق شرایط سرویس رسیدگی خواهد شد.
🤖
خرید سریع
:
🤖
@Team_express_bot
🤖
@vpn_express_sup_bot</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/131327" target="_blank">📅 22:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131326">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚀
سرویس VPN (V2Ray) تیم اکسپرس
✅
اتصال پایدار و پرسرعت
✅
پنل اختصاصی (مشاهده حجم و تاریخ انقضا)
✅
سازگار با تمام دستگاه‌ها و اینترنت‌ها
✅
مناسب استریم، بازی و استفاده روزمره
✅
تمدید و خرید مجدد بدون تغییر کانفیگ
✅
بدون محدودیت تغییر دستگاه و IP
🛠
پشتیبانی تا پایان اشتراک
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 50,000 تومان
▫️
۴۰ گیگابایت — 95,000 تومان
▫️
۶۰ گیگابایت — 140,000 تومان
▫️
۸۰ گیگابایت — 185,000 تومان
▫️
۱۰۰ گیگابایت — 230,000 تومان
▫️
۱۵۰ گیگابایت — 340,000 تومان
▫️
۲۰۰ گیگابایت — 450,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 560,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 95,000 تومان
♦️
۵۰ گیگابایت — 140,000 تومان
♦️
۷۰ گیگابایت — 185,000 تومان
♦️
۱۰۰ گیگابایت — 250,000 تومان
♦️
۱۵۰ گیگابایت — 365,000 تومان
♦️
۲۰۰ گیگابایت — 475,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 675,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 240,000 تومان
▫️
۱۰۰ گیگابایت — 275,000 تومان
▫️
۱۵۰ گیگابایت — 390,000 تومان
▫️
۲۰۰ گیگابایت — 500,000 تومان
▫️
۳۰۰ گیگابایت — 720,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 820,000 تومان
خرید:
🤖
@Team_express_bot
🤝
فروش عمده و پنل نمایندگی:
📩
@expressuport
📢
کانال اطلاع‌رسانی:
🌱
@vpn_express_sup</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/131326" target="_blank">📅 22:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131325">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
پزشکیان: اگر لازم باشد نه 20 میلیون بلکه 100 میلیون بشکه نفت به نیروهای نظامی می‌دهیم، این وظیفه من است و به آن افتخار میکنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131325" target="_blank">📅 22:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131324">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f1501b9d.mp4?token=tL9rxlh67rKkVY25H9ZmmxQjlK0l4jVZ1giljmZ5JOqTZmdCjMsDCBWJKjhfIMn0kDXe4C3oRNIA-vqGvNj4WK7YoBEo6NiK-8NbXd_ZCY4IA6iiBTQ0ZKU5580Uzs2kyYqAh9e35wLOrot026xFiTlmvSQXZu7nIjd3VL3GyFJoN9VZ00KVqnApl2qL85do55vXlZYbh03G1yZxImNN_K_w2CY_PsliNJmveDb9iqjQGhKAYgHkPuGzmWqcgBr-PWwi7_PWwxbsn0MasHMUfb08SLJHG_TW3vDl1ALNiMoS2A-nLB-haIlm40w79WPaaqFoTlm9g5FgrgER6sDo_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f1501b9d.mp4?token=tL9rxlh67rKkVY25H9ZmmxQjlK0l4jVZ1giljmZ5JOqTZmdCjMsDCBWJKjhfIMn0kDXe4C3oRNIA-vqGvNj4WK7YoBEo6NiK-8NbXd_ZCY4IA6iiBTQ0ZKU5580Uzs2kyYqAh9e35wLOrot026xFiTlmvSQXZu7nIjd3VL3GyFJoN9VZ00KVqnApl2qL85do55vXlZYbh03G1yZxImNN_K_w2CY_PsliNJmveDb9iqjQGhKAYgHkPuGzmWqcgBr-PWwi7_PWwxbsn0MasHMUfb08SLJHG_TW3vDl1ALNiMoS2A-nLB-haIlm40w79WPaaqFoTlm9g5FgrgER6sDo_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خورخه رودریگز، رئیس مجلس ملی ونزوئلا، گفت که تعداد کشته‌شدگان در نتیجه زمین‌لرزه‌های هفته گذشته به ۲۲۹۵ نفر رسیده است.
🔴
او افزود که ۱۱۲۶۷ نفر زخمی شده‌اند، ۱۲۸۴۱ نفر آواره شده‌اند و ۶۴۶۱ نفر نجات یافته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/131324" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131323">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dece196b7d.mp4?token=roDkD8OxJRORFRE8KXCZ5SZ-CkqBsWvDuDa8IaxUzKWyWpFDrNqKdnN-gHd0tIB0DT3vp0OnTqnnuxmphvsrWfEzmtyXNTifbMp5wIkefi4caQXuC0LhxHkDHgREeDFjk50Pq9JHCspMD0IvXiuug-65Ni24TMt6D5p_2obE7jSPM-GmYKf8H69-g0xBKMfqQpMhwlPXSLcWADsF2RcpOhyioEf1Ch7gmUIDiyKV40FY7iJ16gy0OTwC8JL-_DG97SNQ3Re7j14PbYY3Mtj16OogSk9lfvGqnqDn_vZ9JxMKSu28ILRnJeeF2s6lWQQTSqWKfsnObxxHT35myyMMQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dece196b7d.mp4?token=roDkD8OxJRORFRE8KXCZ5SZ-CkqBsWvDuDa8IaxUzKWyWpFDrNqKdnN-gHd0tIB0DT3vp0OnTqnnuxmphvsrWfEzmtyXNTifbMp5wIkefi4caQXuC0LhxHkDHgREeDFjk50Pq9JHCspMD0IvXiuug-65Ni24TMt6D5p_2obE7jSPM-GmYKf8H69-g0xBKMfqQpMhwlPXSLcWADsF2RcpOhyioEf1Ch7gmUIDiyKV40FY7iJ16gy0OTwC8JL-_DG97SNQ3Re7j14PbYY3Mtj16OogSk9lfvGqnqDn_vZ9JxMKSu28ILRnJeeF2s6lWQQTSqWKfsnObxxHT35myyMMQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ با قطار آزادی وارد داکوتای شمالی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131323" target="_blank">📅 22:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131322">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سفیر آمریکا: «رابطه واشنگتن و تل‌آویو شبیه یک ازدواج ایده‌آل است که در آن جایی برای طلاق وجود ندارد»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/131322" target="_blank">📅 22:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131321">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
رویترز گزارش داد که مقامات فرانسه تجمع منافقین در پاریس را بخاطر تهدیدهای سلطنت طلبان لغو کردند.
🔴
خبرگزاری رویترز گزارشی از طرف نهادهای اطلاعاتی فرانسه را رویت کرده که در آن به تهدیدهای فعالان سلطنت طلب به بر هم زدن گردهمایی مجاهدین و حتی تهدید به بمب گذاری اشاره شده است. ظاهرا بر اساس این تهدیدها بود که دولت فرانسه تصمیم به لغو تجمع مجاهدین گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/131321" target="_blank">📅 22:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131320">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b73eec92a.mp4?token=lvAkTj0oPqqRpdcOYMt161BNO4w0en5qGQcqvo8c8zRy6zfhjPLHMFJsiAJOHRNdMbgPo3BfwnHtOTb-BLbXYHYYw8KO7cjZdohbxcxc00haDWKvc24BP13r3NKyk5RVoMIAEUryvlnUS2vr7YXz3o5zMgzLxPIiUBvbSclbRL3RazvHi1QF1ImdClLLJYRLRMxgbOQzcFPlCgG5QVcH3bgYB4bbfm7-h7sjbJSiscSGzPOmsIq_c5Y9DIAqyeQtttmqKYyrlJz9dIui5hXwaDko7BHsVjwGb_LQKusM29HPGcSVeMkALB7p3fA9761MJqRULo3CbUzbpGOHJ-F6Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b73eec92a.mp4?token=lvAkTj0oPqqRpdcOYMt161BNO4w0en5qGQcqvo8c8zRy6zfhjPLHMFJsiAJOHRNdMbgPo3BfwnHtOTb-BLbXYHYYw8KO7cjZdohbxcxc00haDWKvc24BP13r3NKyk5RVoMIAEUryvlnUS2vr7YXz3o5zMgzLxPIiUBvbSclbRL3RazvHi1QF1ImdClLLJYRLRMxgbOQzcFPlCgG5QVcH3bgYB4bbfm7-h7sjbJSiscSGzPOmsIq_c5Y9DIAqyeQtttmqKYyrlJz9dIui5hXwaDko7BHsVjwGb_LQKusM29HPGcSVeMkALB7p3fA9761MJqRULo3CbUzbpGOHJ-F6Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، نتانیاهو، درباره تیمی که در جام جهانی فیفا طرفدار آن است:
تیمی که من به‌ویژه دوست دارم، تیمی است که امروز در جنوب لبنان دیدم.
🔴
فرماندهان ما، سربازان ما، این ذخیره‌ها — آن‌ها قهرمانان جهان هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131320" target="_blank">📅 21:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131319">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca8845591e.mp4?token=ugxL1jpMKh70BnEMmHyY0ZHETs-JgZOruj4RUG1apXxH0XARUtiMH8J1BgSW7Sgte90AW5SDh13SNrzwrBNPHXg7eCbu1C39_DloJpveLwVqvE4oJwYsp_1js8_9xQoNjxBEyybpjnVrSzoPlfRTEaCMuw4FoF7Y2I_ms3Ig-_QXowxYqBuf0tcXJqwBMHKRs17L37mMtEAi-hItH9y3fX4Zc89kQL5oxVBVtQCMFYorzAQlN7B4fQmN5x-aAzIn9urAsQGLYwOr7-CM-VTMTqCPM9UmcF6F4RhCqAnHdQLHHiUE88aUBxTMLHRQYMDJh0aWTR_g5YYBM9pkDfhA0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca8845591e.mp4?token=ugxL1jpMKh70BnEMmHyY0ZHETs-JgZOruj4RUG1apXxH0XARUtiMH8J1BgSW7Sgte90AW5SDh13SNrzwrBNPHXg7eCbu1C39_DloJpveLwVqvE4oJwYsp_1js8_9xQoNjxBEyybpjnVrSzoPlfRTEaCMuw4FoF7Y2I_ms3Ig-_QXowxYqBuf0tcXJqwBMHKRs17L37mMtEAi-hItH9y3fX4Zc89kQL5oxVBVtQCMFYorzAQlN7B4fQmN5x-aAzIn9urAsQGLYwOr7-CM-VTMTqCPM9UmcF6F4RhCqAnHdQLHHiUE88aUBxTMLHRQYMDJh0aWTR_g5YYBM9pkDfhA0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: ممکن است روسیه امروز صلح را در اولویت خود نبیند.
🔴
ما آنها را وادار خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/131319" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131318">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
عضو هیأت رئیسه مجلس: حتی اگه آمریکا گندم رو به ما ارزون‌تر هم بفروشه، نباید از این کشور خرید کنیم.
🔴
نباید پول به جیب قاتلان رهبر بریزیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131318" target="_blank">📅 21:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131317">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
پزشکیان: اگر رهبری دستور می‌دادند مذاکره نشود قطعاً اطاعت می‌کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131317" target="_blank">📅 21:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131316">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی:
پیام آمریکا در دوحه به ایران این بود که «بزرگ‌تر فکر کنید؛ رفع تحریم‌ها در چارچوب یک توافق گسترده‌تر ۱۰۰ برابر ارزشمندتر از اخذ عوارض از کشتیرانی است»
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131316" target="_blank">📅 21:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131315">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
رویترز به نقل از مقام آمریکایی: در مذاکرات دوحه به تفاهم رسیدیم که تا هفته آینده آرامش اوضاع حفظ شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131315" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131314">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
خبرگزاری رویترز در گزارشی اختصاصی به نقل از دو مقام اروپایی و اسناد محرمانه گزارش داده است که آموزش مخفیانه نیروهای روسیه در چین در سال ۲۰۲۵ با تایید مستقیم وزیر دفاع روسیه انجام شده و دست‌کم چهار ژنرال ارشد روس و چینی در آن مشارکت داشته‌اند
🔴
به گفته این دو مقام مشارکت فرماندهان ارشد روسیه و چین در این آموزش‌ها از اهمیت راهبردی همکاری نظامی دو کشور حکایت دارد؛ همکاری‌ که در اروپا با نگرانی دنبال می‌شود اما چین آن را انکار می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131314" target="_blank">📅 21:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131313">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
اکسیوس: طبق گفته یک منبع منطقه‌ای، در جریان مذاکرات دوحه، مذاکره‌کنندگان آمریکایی به طرف ایرانی اطلاع دادند که قصد دارند به مهار اسرائیل ادامه دهند و اطمینان حاصل کنند که تل‌آویو به آتش‌بس در لبنان پایبند می‌ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131313" target="_blank">📅 20:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131312">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
معاون وزیر امور خارجه ایران: در نشست قطر تصمیم گرفته شد که بخشی از ۶ میلیارد دلار دارایی‌های مسدود شده برای خرید کالا بر اساس نیازهای ایران استفاده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131312" target="_blank">📅 20:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131311">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5882311cc9.mp4?token=vHO2OSfvMTaSMN5CAXiv-PVfH5NQipoO2dlSBTaKK2wu2l72bsCmDHJx044-IJaTgDX1wcEwg14MgB0tA01TWNrQREJ-ZSHz4ci14k1PtXhjs2IRmYM2t_7nw4vGFIHvYNtbgHJ-VthYE9wyTBRZLtFmrkrTzyujBO_FB8gkTGjxWKWthfCbpdEMbQrIe2PB59Qf5e1fNCIcSAkwSYU_KMYxtXpZZolHbfKRRvKvhgmzlb1fmiVgT0-g_djoCl9-fuTz2_lss96KoNb8GUPUfhtVIq4gJTQCCLKWo9QmfMELhZpHZAnCAHwpWDboskOlc18TpgsNU8xQ6zH_mRMmvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5882311cc9.mp4?token=vHO2OSfvMTaSMN5CAXiv-PVfH5NQipoO2dlSBTaKK2wu2l72bsCmDHJx044-IJaTgDX1wcEwg14MgB0tA01TWNrQREJ-ZSHz4ci14k1PtXhjs2IRmYM2t_7nw4vGFIHvYNtbgHJ-VthYE9wyTBRZLtFmrkrTzyujBO_FB8gkTGjxWKWthfCbpdEMbQrIe2PB59Qf5e1fNCIcSAkwSYU_KMYxtXpZZolHbfKRRvKvhgmzlb1fmiVgT0-g_djoCl9-fuTz2_lss96KoNb8GUPUfhtVIq4gJTQCCLKWo9QmfMELhZpHZAnCAHwpWDboskOlc18TpgsNU8xQ6zH_mRMmvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اساس گزارش Kpler، تردد کشتی‌ها از تنگه هرمز بین ۲۹ تا ۳۰ ژوئن بدون تغییر قابل‌توجه ادامه داشته است.
🔴
در این بازه زمانی، ۳۴ عبور تأییدشده ثبت شده که شامل ۱۷ کشتی در هر جهت بوده است.
🔴
با وجود باز بودن و فعال بودن مسیر، رصد ترافیک دریایی همچنان دشوار است؛ زیرا کشتی‌ها از مسیرهای مختلف از جمله آب‌های ایران، عمان، مسیرهای ثبت‌شده در سازمان و همچنین مسیرهای بدون سیگنال یا ناشناس استفاده می‌کنند.
🔴
همچنین، سامانه ثبت حوادث سازمان بین‌المللی دریانوردی تاکنون ۴۹ حادثه تأییدشده در منطقه را ثبت کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131311" target="_blank">📅 20:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131310">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سخنگوی ارتش: نیروهای هوایی و دریایی در آماده‌باش کامل به سر می‌برند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131310" target="_blank">📅 20:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131309">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری / وال استریت ژورنال: آمریکا در حال بررسی خروج نیروهای خود از عربستان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/131309" target="_blank">📅 20:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131307">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سنتکام: یک گفتگوی منطقه‌ای در مورد امنیت دریایی در بحرین با مشارکت رهبران ارشد نظامی از ۱۲ کشور برگزار کردیم/رهبران نظامی ۱۲ کشور تعهد خود را برای تضمین آزادی دریانوردی از طریق تنگه هرمز تأیید کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131307" target="_blank">📅 20:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131306">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gogUAgN2zEjttUKDHlmoIREmH6xEydSiqDKeadZfbhHo95Y3EWuRLV_gcSwGln5PQJOeh3bgFmO_fBBJuePoEmG_mnf_SEBqVy-ewohGabCSqKNkq09mVpV3olsuzcngGYbFbpp0ofDPjsGZyXWe0tYGjWzZWpeTRD5Mxv71QriOY7j2xXw487o15WvQjejOFqoGxxxsXt-W3hpOYuzXr2JRzvqawlghua50j74AQjxuh9ZrkzoUACFcKr3Vit1Auqwq-6EiekZc27oPwoSLXtC2pMJJE8ldh1Wsad8Euque-MbMRUsvrkiCAsW7iVYKzDVkkD0GTq79t0LjWkZGoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث
: خبر بزرگ! شرکت Micron، یکی از بزرگ‌ترین و موفق‌ترین شرکت‌های آمریکایی، اعلام کرده که ۲۵۰ میلیون دلار در Trump Accounts سرمایه‌گذاری خواهد کرد.
🔴
این اقدام تاریخی که با تصمیم مدیرعامل فوق‌العاده این شرکت، سانجی مهروترا، انجام شده، در آینده نزدیک زندگی بسیاری از کودکان آمریکایی را بهتر خواهد کرد.
🔴
این بزرگ‌ترین سرمایه‌گذاری شرکتی از این نوع است و به میلیون‌ها کودک و خانواده آمریکایی کمک می‌کند تا زندگی خود را با امنیت مالی بیشتری آغاز کنند.
🔴
مایکرون مستقیماً روی کارگران و خانواده‌های آمریکایی سرمایه‌گذاری می‌کند.
🔴
دقیقاً به همین دلیل برنامه Trump Accounts ایجاد شد؛ تا هر کودک آمریکایی فرصت بهتری برای موفقیت داشته باشد.
🔴
سیاست‌های من جواب داده‌اند، آن هم در ابعادی بزرگ. آمریکا از هر کشور دیگری در جهان عملکرد بهتری دارد و شرکت‌هایی مانند مایکرون هر روز این موضوع را ثابت می‌کنند.
🔴
این، عصر طلایی آمریکاست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131306" target="_blank">📅 20:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131305">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b10b9afb.mp4?token=h-m5HTHEbJzbMh0kk8wECAAEI5CAQP_XFl1nDcghC9xilOUfkn-Z1-qQrVibgZToSFtb3bcvwCG5-qj9wPw0q722PS2Mw2zOnk8K01GsTiB79p8d5uXfBX_PT2yHQo6bPNlXj5Tvz4Hdy6R9CsJ6X5--XA4P2rBl1hMmtbeCqUnI5q4cIEUoilcAHKCaemhvKjcGhKSEJeHvwO1fK86tzC_rNeKOyG4mIyqyJ5Y8oUWpBHYaulI59CTFyQb33NqE9V3xnnxbKc8qVFV4QA7hBhbzGuq1RLW8nQ8IxYTNCPz0KCXx-HRhDwxN3Yv2owTZVIr1rF320COyxntn3qwFdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b10b9afb.mp4?token=h-m5HTHEbJzbMh0kk8wECAAEI5CAQP_XFl1nDcghC9xilOUfkn-Z1-qQrVibgZToSFtb3bcvwCG5-qj9wPw0q722PS2Mw2zOnk8K01GsTiB79p8d5uXfBX_PT2yHQo6bPNlXj5Tvz4Hdy6R9CsJ6X5--XA4P2rBl1hMmtbeCqUnI5q4cIEUoilcAHKCaemhvKjcGhKSEJeHvwO1fK86tzC_rNeKOyG4mIyqyJ5Y8oUWpBHYaulI59CTFyQb33NqE9V3xnnxbKc8qVFV4QA7hBhbzGuq1RLW8nQ8IxYTNCPz0KCXx-HRhDwxN3Yv2owTZVIr1rF320COyxntn3qwFdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل با یه پهپاد به منطقه «نَبطیه الفوقا» تو جنوب لبنان حمله کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/131305" target="_blank">📅 20:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131304">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3583560ed.mp4?token=afP0wyxxDdiqDZKaX2lABYqv_WVf1F4wb22Fc_olL2CAxhrf6PGywQP4fNOjj7Tc6CoUO2PTmTCGZTeYyMQ2s363B-_Dij8v4So-NfBRFzxVV8xUm1ebfXjbS4HNpjswKPzsGjC19AIatsd1HAZB1CKDlM-3QrBOmQ0o5eYsRwRm3pHcyQIELUDdovZA_rMfRJ48RJVAWpYecyNl2ipcxLn6Iq-Nbm9XToGeBbWGumfj7W4O_i4ZT4aPj0kPWWm9-jLT6fh07DB3FkcW8Zzu19M0IOWeD3OXHvZjCP7JmrODKINF2h2t0iRtxTabpVeP7yRIjlL6JmFxyKOmV9DDMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3583560ed.mp4?token=afP0wyxxDdiqDZKaX2lABYqv_WVf1F4wb22Fc_olL2CAxhrf6PGywQP4fNOjj7Tc6CoUO2PTmTCGZTeYyMQ2s363B-_Dij8v4So-NfBRFzxVV8xUm1ebfXjbS4HNpjswKPzsGjC19AIatsd1HAZB1CKDlM-3QrBOmQ0o5eYsRwRm3pHcyQIELUDdovZA_rMfRJ48RJVAWpYecyNl2ipcxLn6Iq-Nbm9XToGeBbWGumfj7W4O_i4ZT4aPj0kPWWm9-jLT6fh07DB3FkcW8Zzu19M0IOWeD3OXHvZjCP7JmrODKINF2h2t0iRtxTabpVeP7yRIjlL6JmFxyKOmV9DDMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امیر رولکس: بعد از بازی با مصر خواستم بگویم فوتبال [با ما سر ناسازگاری دارد] اما اشتباهی گفتم خدا
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/131304" target="_blank">📅 20:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131303">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
خبرنگار: آیا می‌توانید متعهد شوید که آمریکا تا پایان مهلت ۶۰ روزه این تفاهم‌نامه وارد عملیات نظامی گسترده نخواهد شد؟
🔴
جی‌دی ونس: رئیس‌جمهور ترامپ نیروهای نظامی ما را دوباره وارد جنگ نخواهد کرد، مگر اینکه واقعاً مجبور باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/131303" target="_blank">📅 20:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131302">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
مقام آمریکایی در مصاحبه با جروزالم‌پست مدعی شد: همان‌طور که در تفاهم‌نامه ذکر شده است، ایالات متحده باید نحوهٔ استفاده از این وجوه را تأیید کند.
🔴
این در حالی است که در هیچ‌یک از بند‌های یادداشت تفاهم اشاره‌ای به این موضوع نشده و در بند ۱۱ آمده است: آمریکا متعهد می‌شود تا وجوه و دارایی‌های مسدود شده ایران را با اجرای این یادداشت تفاهم «به طور کامل» برای استفاده در دسترس قرار دهد.
🔴
مقام آمریکایی همچنین ادعای واشنگتن درباره خرید محصولات کشاورزی آمریکا را تکرار کرد و مدعی شد:‌ در صورت آزادسازی دارایی‌های ایران، از این وجوه برای خرید محصولات کشاورزی آمریکایی از کشاورزان آمریکایی به‌منظور تغذیهٔ مردم ایران استفاده خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/131302" target="_blank">📅 19:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131301">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
یدیعوت آحارانوت:پخش اذان ممنوع شد !
🔴
کنست با قرائت مقدماتی بر قانون منع اذان استفاده از بلندگوها را در مساجد شهرهای فلسطینی نشین به بهانه «سر و صدا» ممنوع و آن را تصویب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131301" target="_blank">📅 19:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131300">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
فارس : صادرات محصولات شیمیایی، پلیمری و پتروشیمی دوباره آزاد شده
🔴
فقط باید طبق همون قوانین و مقرراتی انجام بشه که قبل از محدودیت‌های شرایط اضطراری وجود داشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131300" target="_blank">📅 19:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131299">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ونس: اگر ایران سعی در بازسازی برنامه هسته‌ای خود داشته باشد، همسایگان خود را تهدید کند و از تروریسم حمایت کند، رئیس جمهور ترامپ گزینه‌هایی برای مقابله با آن دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131299" target="_blank">📅 19:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131298">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2eb6c3904.mp4?token=piBIDPT5qNvMIWDAZNcf6nSPAgTgubAJbtaleLPoMfS8stO-36PTpDEByIOZdTwrr6F7Qv9FkRNVnhmgdzwPVlUmx2A669effNGp7WHtCleJaAAa_U5hC06qmZbBJ9M6119cIXFlfEWDTuEm47yzAa0R5iE8juU59WCFoccziODH83skEXBaZhmQH0X5kOFkK2lq5u7xM500Ddyr9AxzwOp9t2-AUvTUruqS4X9HUQ4YzLazEKvaVsvoOwSQqOQqv0U1Y-M2dvl1Ws8eSe9XXMEe_U6XVNghw6mcvkEPftYeuGLZO2iXSB2tvLa7RAvoKsinWvF1iEv6O39uHrx9qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2eb6c3904.mp4?token=piBIDPT5qNvMIWDAZNcf6nSPAgTgubAJbtaleLPoMfS8stO-36PTpDEByIOZdTwrr6F7Qv9FkRNVnhmgdzwPVlUmx2A669effNGp7WHtCleJaAAa_U5hC06qmZbBJ9M6119cIXFlfEWDTuEm47yzAa0R5iE8juU59WCFoccziODH83skEXBaZhmQH0X5kOFkK2lq5u7xM500Ddyr9AxzwOp9t2-AUvTUruqS4X9HUQ4YzLazEKvaVsvoOwSQqOQqv0U1Y-M2dvl1Ws8eSe9XXMEe_U6XVNghw6mcvkEPftYeuGLZO2iXSB2tvLa7RAvoKsinWvF1iEv6O39uHrx9qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس درباره ایران: ایرانی‌ها از توسعه بمب هسته‌ای، از هر زمان دیگری در 20-30 سال گذشته، دورتر هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131298" target="_blank">📅 19:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131297">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECxfRO22FAaFSkW-WFMn-Yw_u-RQcjrQscN4JSCpz9_H4WP0MZGLXybdK__b_4QuzoWF3NvToIhDK7-om0O_MDFoVl4ZC4juxk2XFhuPLYmYJCAN2VlofcrLOWPfQtQi98znFAb3D7npO5LZUIRtVM-MkqSj4cVjksEZrhGLoijhHncKPRCzRZt_yc20n7u8zro2CWxShivPPyBklfdlDvTvU6di7NaHkQ-ttw2HwEX3_RqhwMHS5xi-3UxZbW5bIVGpxzyYgfWhNuXHS8oyyzyUkMlfz3szItEUG_F93RJavtIEqaX4DsRtynew4FOobbUmYXv6sN3uomHsYoj3Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمزه صفوی:
اونایی که میگن آمریکا درحال فروپاشیه و نابودش میکنیم، کصخولن
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131297" target="_blank">📅 19:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131296">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
معاون ترامپ، ونس : ترامپ از شما خواست توان نظامی متعارف ایران رو از بین ببرید و تا این لحظه که اینجا نشستیم، و نیروی دریایی ایران هم نابود شده
🔴
مأموریت شما این بود که برنامه هسته‌ای ایران رو از بین ببرید
🔴
طبق گزارش‌های اطلاعاتی آمریکا، الان ایران نسبت به قبل خیلی بیشتر از ساخت سلاح هسته‌ای فاصله گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131296" target="_blank">📅 19:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131295">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
آخوند قاسمیان در نقد مقایسه تفاهم فعلی با صلح حدیبیه: شرایط صلح حدیبیه یعنی واشنگتن را اشغال کنید؛ ترامپ را دستگیر کنید و به ایران بیارید
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/131295" target="_blank">📅 19:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131294">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
یک مقام کاخ سفید در مصاحبه با فاکس نیوز: تیم‌های فنی در حال بحث در مورد تمام مفاد یادداشت تفاهم با ایران هستند.
🔴
ترامپ راه‌حل‌های دیپلماتیک را ترجیح می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/131294" target="_blank">📅 19:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131293">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
یک مقام آمریکایی به i24NEWS درباره ادعای آزادسازی ۳ میلیارد دلار از دارایی‌های ایران:
هیچ دارایی منجمد شده‌ای آزاد نشده است و هیچ دارایی‌ای آزاد نخواهد شد مگر اینکه ایران شرایط مندرج در یادداشت تفاهم را برآورده کند.
هر دارایی آزاد شده باید به تأیید آمریکا برسد و برای خرید محصولات کشاورزی آمریکایی برای مردم ایران استفاده شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131293" target="_blank">📅 19:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131292">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dd8e12a39.mp4?token=IqG9fWQwEgzP1tx8nOU_6XwDr9zEGDotgwwdSBONvxepEI1KQeblEq2PpWxXriJeSEB1VV6ZMPmf4FFfPwbXw3Zv_Myf5TSufox5uzB5xEbCNGNc_v8_qvq5u_zgzIG_GBFVSdWNQxUU_meB4W8G9B3fTcum_W67l5MJQcLGi0-xIFFQyc4biHyt7bZ-_H3Ahk1y33MR6EWS_iy6g3PdjVy6V5iEYfvqlztjjOQn18UsIFkGcXs50Na26kyvRtpekLafeAdkJn5-zCXPBHTerSL2S-fSJDYOwWyTkz2mgydgHwkvfkjKORD74w4AkT64LGTUD6PWC6dc1LE58EuIcIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dd8e12a39.mp4?token=IqG9fWQwEgzP1tx8nOU_6XwDr9zEGDotgwwdSBONvxepEI1KQeblEq2PpWxXriJeSEB1VV6ZMPmf4FFfPwbXw3Zv_Myf5TSufox5uzB5xEbCNGNc_v8_qvq5u_zgzIG_GBFVSdWNQxUU_meB4W8G9B3fTcum_W67l5MJQcLGi0-xIFFQyc4biHyt7bZ-_H3Ahk1y33MR6EWS_iy6g3PdjVy6V5iEYfvqlztjjOQn18UsIFkGcXs50Na26kyvRtpekLafeAdkJn5-zCXPBHTerSL2S-fSJDYOwWyTkz2mgydgHwkvfkjKORD74w4AkT64LGTUD6PWC6dc1LE58EuIcIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خداداد: تیم ما دستاوردی نداشته است
🔴
کره هم شبیه ما بود ولی سرمربیش استعفا داد
🔴
مردم خیلی فهیمی داریم
🔴
سه بازی نباختن دستاورد نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131292" target="_blank">📅 19:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131291">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtxqLLoAG3vANO_xJulyaQn7A4t_kHkg2M8t72uZ9dYpQ3WeyNYJdiGJZAzvVjdNYYmPcB0_k18kjOUZuOVa0slX9OqYrucopbKbeWXWi8GWMSCtWaePC0UnvPTZHUAoUXG8FVI-c8Oc5J8N8J_K19YHE35AlmRVe0hznC1O2EfwEPyBJqJ-UvWafY_9H33JhW5D1R5kg607WggB-SDXZay7quMu8y_wABl1gkLnqXqdXXJo_zvtl8emYCRK8dThhtccZo-_Cbh4bPuwSYEsXRDtnSU06Njk9o7LgZea2R-o93Jwyz3FO2YcMr9NBIvrtz7xDF123pHDMccRJbbxGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با حکم مجتبی خامنه‌ای، اژه‌ای برای پنج سال دیگه به ریاست قوه قضاییه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131291" target="_blank">📅 18:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131290">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtVZ4BeZAN9i2kBaFpQ-RehvXNBpI9qEBVVzZvGdRP2k2coSuX19GDDFfl0Jfrf9jwbG2JAc8RKDBGPEIUEO25Vi-IFMkajnm25KQlULgMNqKr3zQbuOA3Rh-ZAAtixaOmPg54uXYYNXMjIQKJYFE4vvvD3VlXQlG2kceBWLdeNiS8-9uS1RT3mWKjx3vO9bkcCADFMcMlVo4NIsbn-0BGjx080BKPquMCekC2Ow18xRpZ-OhhSXeWMHfsJzECbk6_hUKvt5m-qdQVPpVZ6ji4jygXViA3Kwf0KsoC8WaQHpMsO6x8E4Yaf9rtpdpp9z0z3zwnHzERAXVtC3NH3N4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا قراره به بازیکنان فوتبال به پاس وطن دوستی حواله واردات خودرو لوکس داده شود
🔴
پیشتر نیز به هر بازیکن حدود 100میلیارد پاداش داده شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/131290" target="_blank">📅 18:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131288">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m3M1j-zWJnI18U4JqGTh7yK0vgBnQxhwGQVoFoqEAj0FT0MHvd6D9Hvknu6iU4iFu7FlLu4TZerTyyBbktK9INsggOeJUOsX-qygNI7I5mfWJ11zVvNfqVgCE-3R4q2e9vkubRc6qRnnjiyqc18EKPgqCn3NDu3JjdQnvG7DJGvoeHQ5VCsYqRC5G9JUWRRwyNl8XVGnDyiXK8CEmTUs5NYelN7NMjZIK1iyFd-baKlbsOo90edESvAn_GUFILQn5KLxBGNSXbnpSmSoIqvwDLn8TRs1bdApEOO4Gjs8nuLYogPIo5Uug9U_j194aWbuFvfYAtChQ1CpMWDfi-Sgyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mQ7a30iRgbg_aGekdEBP-j8lYxSdvnVEVIFLVv3cv_svrpZuTPsq0r-a1ZM-rzwxuRdck5lyucxCFBNIMQQeXMT6TL_7HwP7eww5FbDKk7r7gxtEJH0XH9_P-qADbHPsmEWumWP4gsTjy9tcw8kO1G_9mUP8RqihoSilYZb9K0q8GLl8XgAXwddjeHRSKGqGzBwUvIHuUymj7FIr7t5C2Yg4qWRO40pvlggRErggAHPBmsmjkBP3Jfy1P4LD1i3yPg9bp0lvRteSuzncO_VmaowYI_NE6VjgHA93SFT4bc6GKXAu_6nZBKuxv0tplrrhUGyFc_C8dSVbt9vq1dZtMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
گزارشاتی رسیده عده‌ای بیکار توی خیابون به دخترایی که حجابشون رو رعایت نکردن از این کاغذا دادن
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131288" target="_blank">📅 18:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131286">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0c588df71.mp4?token=BtAmWZl-o0Iy1XdAbwGg8QkFO5RVrdvn07y1GkCW3FjD47i-nhpSrmS9Mg3fZWUzOIhQ4ztLqZvh_WS8n_cKXwR9FN0jBbusCHJ95RokYWoE95Nr2UJVCso8uI3U5i95NqriObfDTKFg8otCS-rhtThZdVW_pzFauD98fqyAn7Zv_gICpXwvz5VBdexupNrnNQnXoPB6GKL2j1M1tTp6ou4T60Q55P7ntLArzOOk726SeqXrWHhhqaYv0nikdTRc0pLMkLqP6zC4YYibRCCKDX3rwUy4OgM1B6jCSLH_bXrY275N3lMtAupokMnCgCexro2u7NNfmvstB2bIxeonvA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0c588df71.mp4?token=BtAmWZl-o0Iy1XdAbwGg8QkFO5RVrdvn07y1GkCW3FjD47i-nhpSrmS9Mg3fZWUzOIhQ4ztLqZvh_WS8n_cKXwR9FN0jBbusCHJ95RokYWoE95Nr2UJVCso8uI3U5i95NqriObfDTKFg8otCS-rhtThZdVW_pzFauD98fqyAn7Zv_gICpXwvz5VBdexupNrnNQnXoPB6GKL2j1M1tTp6ou4T60Q55P7ntLArzOOk726SeqXrWHhhqaYv0nikdTRc0pLMkLqP6zC4YYibRCCKDX3rwUy4OgM1B6jCSLH_bXrY275N3lMtAupokMnCgCexro2u7NNfmvstB2bIxeonvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسین یکتا رو یادتونه توی اعتراضات دی ماه اومد گفت بچه هاتون رو بیرون نفرستین، اگه تیر خوردن مسئولیتش با خودتونه.
حالا فیلم تولد پسرش اومده بیرون، میزی از خوراکی‌های متنوع که شاید هیچوقت ما نخوریم.
ماشین های چند میلیاردی که شاید هیچوقت سوار نشیم...
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131286" target="_blank">📅 18:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131285">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
قلعه‌نویی: گل شجاع صحیح بود حقمونو خوردن
🔴
با آمریکا جانانه جنگیدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131285" target="_blank">📅 18:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131284">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXRmU-mFUgprvOWhjr35V-nMPJsrprwbu1tChcxQAgdP7JRaxLCtkmtENkGxieA88kAqUWyU1RccflD973wNmYBezvgChP0xp9jCNTxuJ2hpduAf07Ae6RhJnm5ALdPGDDnSc1QEewMTkbJ5nJeGYz7-Tz3qh28_dhkt2pzV1-lwHg2P6dOBBEzxTeDPlw9aexhXfOjDWfpED8gI-f_Dl2NciKjRDjJbChAtWdAAY3rrXzpppexg0YDAm95TT45Xsw-T1mmJKzvg49iR2JlxF9zj7JyRsbKdtD49dKC_Fr3UuCR5p3akMgypaXmhEGdvOEGgpfwD19nL6VNh5LWbkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکوچیچ سرمربی جدید پرسپولیس شد
@AloSport</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131284" target="_blank">📅 18:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131283">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
سخنگوی کاخ سفید به فاکس نیوز:
چه یادداشت تفاهم شکست بخورد و چه نه - ما راه را برای خلع سلاح هسته‌ای ایران هموار کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131283" target="_blank">📅 18:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131282">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krUiyN-GeyJ2hJ_lHOJYhgPu0WyIk2xFlKfs1LDOfyYOzyFgwXghZSsPDEeis-l58pDdh1ThFaarAhxSy8IB8iWGKBGtj1yvJCHHlt2fJMNU6qnaWP0fp-JYfQCzJS1WX2LwnBXvuoy3aSRSuDQV30TJvQ-XGhd_l-fwTgraV29CFohgd6VnVvhftaZwtJbVsH6JGLmY3SZuO8_d2ylOuLXLWHuzJ1R4p_UNKIJjryNo0T2UzbXSxGG9_hFRQAGZRLujdD11FADkchw4umyN8jdfDKy4PskHvwOTXmi1-w_VYIt__zMGrpPDQwSHv7oRrh9vEovjq0uaGHA0posiPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ کرملین: پوتین برای مراسم تشییع رهبر اسبق ایران نخواهد رفت و مدودف را میفرستد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/131282" target="_blank">📅 17:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131281">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/941b0221e4.mp4?token=Uo4LhUBDNlR8rMX3XzDxrOcVIvq3AYiYoFgVesb3pIStawIEumEu63iUDxn92JOF8Mj6oeOSC9mmt2WLc7czbKz3b8qurJcWfcoJOHvoj6Jkn4lDF2SekWorRTGW7AkkZrs_gsowgcIedK-ZfJ_2JuI7aFl679Zu0pOtxqpwhU3FDUwsddI2vQ8Tvwiogw6i_mfYZCQOmJU-MdbQTZmGi07VVsINR_6-f9pEw6VVhkXqk6a9klDUiUdEhsnyvT-Bk60Yl9HpZ3CSatBWBi22oQpdpDIMSStRWE5j-5NuTtFMlNy9dC_vHvXoDtFTx44LS0Uy4jEvhubnPcuAdAzI44WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/941b0221e4.mp4?token=Uo4LhUBDNlR8rMX3XzDxrOcVIvq3AYiYoFgVesb3pIStawIEumEu63iUDxn92JOF8Mj6oeOSC9mmt2WLc7czbKz3b8qurJcWfcoJOHvoj6Jkn4lDF2SekWorRTGW7AkkZrs_gsowgcIedK-ZfJ_2JuI7aFl679Zu0pOtxqpwhU3FDUwsddI2vQ8Tvwiogw6i_mfYZCQOmJU-MdbQTZmGi07VVsINR_6-f9pEw6VVhkXqk6a9klDUiUdEhsnyvT-Bk60Yl9HpZ3CSatBWBi22oQpdpDIMSStRWE5j-5NuTtFMlNy9dC_vHvXoDtFTx44LS0Uy4jEvhubnPcuAdAzI44WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: در تفاهمات اخیر دستاوردهای مهم و ارزشمندی در حوزه‌های اقتصادی و تجاری حاصل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/131281" target="_blank">📅 17:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131280">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
کاخ سفید به فاکس نیوز گفت:
رئیس جمهور ترامپ به روشنی گفته است که اگر ایران به سمت ما شلیک کند، تلافی خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/131280" target="_blank">📅 17:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131279">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ اعلام کرد که قصد دارد بخش عمده‌ای از اسناد و اطلاعات محرمانه دولت را از طبقه‌بندی خارج کرده و در دسترس عموم قرار دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/131279" target="_blank">📅 17:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131278">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c924191a.mp4?token=YNrX6m4esaD0FkYj-Z6LpUVsRP0ToIEyNLKnV8h3vVbGPJh8Ielukc0rEZ_FvcdAVUsLYkbfWL4jldPHi-fC3tAwHfbgAtiH_3354OVWbR6843OAKO1Gwzpz7jxTqapfhjozHlPwz8gbsS17K4WWLch_FQv4iEd8FnxIZTukh2Xqe7urkTik7Ix3GqaIFcZFyDt8gGwkLrmqIhZ9OfipeGPpZSs36t82-YoIDkIcBmuJMHJOlgqCf9HXxc9HeRxcPtfWEbfWRBpB7_cHPo34kO1vJ-1mbp1gIzggQeowYaq4C5GxW5pwVKCAgWAjjAYc_hg8ukh145WU-dbcYqBgpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c924191a.mp4?token=YNrX6m4esaD0FkYj-Z6LpUVsRP0ToIEyNLKnV8h3vVbGPJh8Ielukc0rEZ_FvcdAVUsLYkbfWL4jldPHi-fC3tAwHfbgAtiH_3354OVWbR6843OAKO1Gwzpz7jxTqapfhjozHlPwz8gbsS17K4WWLch_FQv4iEd8FnxIZTukh2Xqe7urkTik7Ix3GqaIFcZFyDt8gGwkLrmqIhZ9OfipeGPpZSs36t82-YoIDkIcBmuJMHJOlgqCf9HXxc9HeRxcPtfWEbfWRBpB7_cHPo34kO1vJ-1mbp1gIzggQeowYaq4C5GxW5pwVKCAgWAjjAYc_hg8ukh145WU-dbcYqBgpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو پربازدید از اظهارات سردار سعید قاسمی در مورد قالیباف سال ۹۸
🔴
قاسمی گفت قالیباف مانند حسن روحانی است و چه موقع جنگ ۸ساله چه الان به او بدبین هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131278" target="_blank">📅 17:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131277">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFq_lSXHZRmZFbYKBRl-I8K3uE4uNatbBa1XhH_syjsw3BwF7tnTHxd0DM-f-13cj1FqyGvhKzx03vMAw7ZT4__UtLAmxJEXLbLzUCH_3yO361Cl2tBkN7MTmSRrhnSWmCZmlHeH1JDdgmtaqnnISWThD9c_KF4DsvRQo2Zy_mkKRnlxqWgWGIGD7bQzMVKZzkNSGH9TLpjtkJ2ynXp3L1vTTgg6BkkGWTe_24VcIym0qei9OPVdCCdLxmIMlkaKaCJy6ONbRYC6vehF6AFtGmrW39howJw31xzNxct4LgKNG5vuu0OcBJJ9icut018-3ZepCzmJ8xMfzWYZ-surWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قاسمیان، موسس شِلتر: باید هرجور شده اسرائیل رو نابود کنیم و مردم باید سختی رو تحمل کنن چون ثواب داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131277" target="_blank">📅 17:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131276">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">دهم تیر، یادآور حماسه آرش کمانگیر و یکی از روزهای گرامی جشن کهن تیرگان است؛ روزی که نماد فداکاری، میهن‌دوستی، امید و پیروزی را در فرهنگ ایران‌زمین زنده نگه می‌دارد.
تیرگان، جشن آب، باران و آرزوهای نیک است و یادآور این حقیقت که با ایثار، همدلی و امید، می‌توان مرزهای ناامیدی را پشت سر گذاشت.
تیرگان خجسته باد؛
به امید روزهایی سرشار از شادی، برکت، سلامتی و سربلندی برای ایران و ایرانیان.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131276" target="_blank">📅 16:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131275">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
رویترز: قیمت نفت خام آمریکا به ۶۸.۲۲ دلار در هر بشکه رسید که پایین‌ترین سطح از ۲۷ فوریه تاکنون است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131275" target="_blank">📅 16:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131274">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
آژانس ایمنی هوانوردی اتحادیه اروپا (EASA) به شرکت‌های هواپیمایی توصیه کرده است که از حریم هوایی عراق و لبنان استفاده نکنند.
🔴
این هشدار به دلیل ابهام درباره آتش‌بس میان آمریکا و ایران و خطر تشدید ناگهانی تنش‌ها صادر شده است.
🔴
همچنین EASA هشدار مربوط به منطقه درگیری را تا ۸ ژوئیه تمدید کرده است.
این نهاد همچنین از شرکت‌های هواپیمایی خواسته در سراسر منطقه خاورمیانه با احتیاط بیشتری عمل کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131274" target="_blank">📅 16:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131273">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزیر جهاد کشاورزی: در صورت رعایت شروط ایران، از خرید کالاهای اساسی از آمریکا استقبال می‌کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131273" target="_blank">📅 16:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131272">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ahw1Yhve3S8wnLDREujAIhztyEbG354Sl7cR4ZujL5mTwANHo4kDwvEBZhJNVyKz9lNBTWxozYTpqWjRKX7ZhqFg4BvMuMiQjiMYXFXgQe59ATZn-dnyC3CF26OVT08fY8HqMe6XXPUwLz1fP9wC7qUaJN4b52q2gXbhJY_fiGrca99OE4e5-Oo9B8Cd7VxQLLeZX85nZ0PI4HSQZdMHhXOjeNNA9uvT8v2KOgKykKKzKwzS0IxB4_m5XMfcAoowWHzJAm0170MulIjdTwKTUTKGK-l-VurdwpRa4WtDQPjjZVkx0ju3BTeFC49yPygPZpBVgYy6_1IKt164rVho8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاهده شدن دود در جنوب تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131272" target="_blank">📅 16:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131271">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ترامپ: تا زمانی که دوره ریاست‌جمهوری من به پایان برسد، می‌توانیم ۵۰ درصد بازار تراشه‌های جهان را در اختیار داشته باشیم.
می‌دانید الان چقدر سهم داریم؟ هیچ.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131271" target="_blank">📅 16:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131270">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ترامپ
: اینتل به کمک نیاز داشت. به آن‌ها گفتم: "کمکتان می‌کنم، اما در عوض ۱۰ درصد از شرکت را به ایالات متحده آمریکا بدهید."
🔴
او گفت: "قبول است."
🔴
آن‌قدر سریع قبول کرد که با خودم گفتم، شاید باید سهم بیشتری درخواست می‌کردم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131270" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131269">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ترامپ اعلام کرد که قصد دارد بخش عمده‌ای از اسناد و اطلاعات محرمانه دولت را از طبقه‌بندی خارج کرده و در دسترس عموم قرار دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131269" target="_blank">📅 16:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131268">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ترامپ : باید ببینیم چی میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131268" target="_blank">📅 16:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131267">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a717d0815.mp4?token=o0Rv7a9kpnyG4-OPe8fV37BAQy5M-lsRNK59AqdFFswzVZQDJ7alpU7fhj1AVVRDRJn3KJmBQCZyKj0aWQ8urIDH2GdBUvAwb3bh2v2BxwDH-wreWL4U2qS1dz2_7BGF1UyFyVg_B0yv-vORrweYFeQrlnXXQvDVgo81EzT0RlDXSIJDintt0nWwAjdrwgyS9RcAIe2RGLGpRM2hzkDkU_YDEUDRe7IgL6bSPey3eN3aGVSwq6pcaCFCk53CKVI9eNOcpsL7CLJ4DmActyHZ0jDrDvAxXfhAJscu56tgKHjC7rPqLAaDV3LUgtSczuWa4f45zhy_Jxugf_sg850lypCl5ihV4rb3hzMRocUd4zyJo0MGem9IFsPisDl7FhY60ka5GS01rHwJKB9gZ_CYtSM8purALOtsy2MUIpe6KIW2bpaOv3XmNyCs0G2UQtRy91anRLRElB-Oe5lHYpD4gbeTd3y3wumXbj5mADvWoDUYGQI9AvgusOR8L49XW7ghtC7hf6e3pu0iGMCwQia7goueOihmDfLU5CUkZQy-K1VKDtZfHfpXwksgLFMSvOBdVwL7QrlWlzGhLqIa596s54LbgV2ddtRZGvqFNK10t7d-4tPVoEllQSv09l72mFAKgcBsFN2x1eKMMxMtKUNp1k4JPQ_3Xm5ExBmD4O1g4BM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a717d0815.mp4?token=o0Rv7a9kpnyG4-OPe8fV37BAQy5M-lsRNK59AqdFFswzVZQDJ7alpU7fhj1AVVRDRJn3KJmBQCZyKj0aWQ8urIDH2GdBUvAwb3bh2v2BxwDH-wreWL4U2qS1dz2_7BGF1UyFyVg_B0yv-vORrweYFeQrlnXXQvDVgo81EzT0RlDXSIJDintt0nWwAjdrwgyS9RcAIe2RGLGpRM2hzkDkU_YDEUDRe7IgL6bSPey3eN3aGVSwq6pcaCFCk53CKVI9eNOcpsL7CLJ4DmActyHZ0jDrDvAxXfhAJscu56tgKHjC7rPqLAaDV3LUgtSczuWa4f45zhy_Jxugf_sg850lypCl5ihV4rb3hzMRocUd4zyJo0MGem9IFsPisDl7FhY60ka5GS01rHwJKB9gZ_CYtSM8purALOtsy2MUIpe6KIW2bpaOv3XmNyCs0G2UQtRy91anRLRElB-Oe5lHYpD4gbeTd3y3wumXbj5mADvWoDUYGQI9AvgusOR8L49XW7ghtC7hf6e3pu0iGMCwQia7goueOihmDfLU5CUkZQy-K1VKDtZfHfpXwksgLFMSvOBdVwL7QrlWlzGhLqIa596s54LbgV2ddtRZGvqFNK10t7d-4tPVoEllQSv09l72mFAKgcBsFN2x1eKMMxMtKUNp1k4JPQ_3Xm5ExBmD4O1g4BM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: منتقدان شما می‌گویند از ریاست‌جمهوری برای کسب سود شخصی استفاده می‌کنید.
🔴
ترامپ: من سود می‌کنم، چون بازار سهام در حال رشد است. همه ما داریم سود می‌کنیم.
🔴
حساب بازنشستگی شما چطور است؟ ۸۵ درصد رشد کرده. باید بگویید: "متشکرم، رئیس‌جمهور ترامپ!"
🔴
من سود می‌کنم، چون پول زیادی دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/131267" target="_blank">📅 16:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131266">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ترامپ: هفته گذشته حملات قدرتمندی علیه ایران انجام دادیم
🔴
ایران پیشرفت قابل توجهی در توافق داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131266" target="_blank">📅 16:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131265">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
ترامپ: ما جلسه بسیار خوبی با طرف ایرانی داشتیم.
🔴
ما در مسیر خلع سلاح هسته‌ای ایران پیش می‌رویم
🔴
همه ما از افزایش بازارهای سهام و کاهش قیمت نفت و همچنین قیمت‌های بخش خرده‌فروشی سود می‌بریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131265" target="_blank">📅 16:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131264">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
جان رتکلیف» مدیر سازمان اطلاعات مرکزی آمریکا (سیا) ادعا کرد که جنگ آمریکا و اسرائیل علیه ایران اکنون جنگ فناوری است و گفت: «کشوری که بهتر بتواند از قدرت فناوری استفاده کند، آینده جهان را تعیین خواهد کرد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131264" target="_blank">📅 16:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131263">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
روزنامه آمریکایی نیویورک تایمز به نقل از یک مقام ایرانی و چهار دیپلمات منطقه‌ای آگاه گزارش داد که ایران و عمان با وجود مخالفت علنی واشنگتن، در حال پیشبرد طرحی برای دریافت عوارض از کشتی‌های عبوری از تنگه هرمز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131263" target="_blank">📅 15:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131262">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wlvyxy7ScpZDbyae6KO2SPaWRHI2dBRnFMNbrrvxU84rm7enVejQB6kYi-B4du8Gc9yUc6jWvkiPhi19qK2zQwhjdlHncW7oYStPSvWXweS9k417s6LS0rNfW2ua-KioOvQMhC4wSJCdOt2G4VNK_Fd8GpvLmFx1YG35MgPJy66KbzmFRGf8K8Il2fJrBHgqHTj65fqE4XglDG_izfVtrOGCoKRr3RolYAvNkdFfRucM3Q2VLlpsJDjapVPoGx1iz77h8nZUV-_KbuJ_oHaafzYOSQuPHrs4rIcQsXyYWQoND5wBGQg3y5Jvr_dzF6Cq2BOPoqjSSPDGufh_IzTeUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: مردم میگن نون خشک هم بخوریم باید مقاومت کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131262" target="_blank">📅 15:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131261">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
شبکه الحدث: مذاکرات ایران و آمریکا در دوحه در مورد تنگه هرمز طبق طرح جدیدی که توسط عمان پیشنهاد شده در حال انجام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131261" target="_blank">📅 15:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131255">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WQPJ-a2aC6wtiiuxR6poutsJOZy6ewSHUcSpAkHLlqew5NKFxzw3kZaoPFDilwVmV5-1fJLTE98wckmFzdqSBDmtQzR9LzIfP7OUDwDQ2B77NQLyfzy9jGJU5MrztvpOzAji8GixH-Iq5ujW6P5M_dTjIo6PSitBpU4vI2zrXy688A2DtSUh-AZ0I5S0DyyssanRFqr5ciPRnHPrkV5k8yXgcqvwrx-_SUf4DrGAbzABcdB3Om0gFmWiqUNlqMl28wStz5XTp7W7FI9OlJUgAypKhyfdZJ8wZhE9jrlyx3G0qO6InDPjvEalr7V2Cuwa1F2bOvMSzK-yvnvjieRPfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZRmWccPcUCRkXc9ZrTVuu2PVt8T-DYAVIv0QNC9QH0B_kRAV-oza_9-oF_XZ7Nr8W6v5-zjmx7WKcp0rMCGZqJV5R0VwHgdfd-GuIPzyfQWEEEXGob8FK7OAbOYaqbAt8xESAdDhnk4FVtqDDzQoOhaegjfXhev_PVj8mSyQ5AQGSkdPkeBzPyo13QWkToPNS25ourpZlrUmw4ZnXw3B72MhKrW40LaIvIi51O1qmFrgI3MttZRoZvND7HErytqDyXAy97Hck5az3pTUE1Kd_tjykF68DrlHhkXiJIVzmcC2hinxyISnsI2Ncea7h9bBTRB2adJmmYtdGv10y8k5CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXYEFY4dekbQ7Ja2hjlduqQECldZ_ReRffpRclXVD_HoKPalLsatHtXNf2afD-RBWbxfoE0jXzlR8nI2bJP2Fj6H_0XQMfII9XLe8KkqsfU8YdPwq40M5NoQ5oe6DfALrwkfu_ue2xDVUvIBG4E_p1yQ9I8Tu-3Xblb_v0czUj5DFvPQfkM6fhKD628hyJ-C55jm32W7rI_ncSpKbmvNQNp0XFrYltpF1S4TiKpmstyN2f8tN1uWTUvUoheG02SWNPTykHsZ5wXpjBClwcROPyc43LdPZvGmDYzlp7rqMGmT51kSqUsUIu1yUkQ57qHjyZgNdVA4YDK2u5pQlLhZmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c1770a4f.mp4?token=l9zg94dbk9pESps1AvSz2e1X94v-YXWx-QoNgfserqjQ5kNgWvV40_QPP8E-U4-F4Uo0pyA19OsFqM84GIo33By6dui5rvEGF5XkcWdS54jmn6el8hJJLSjHKtM02w9rbjI1xncXZrDvKEp1z9OPGvkaNrea7d9WV-GtrS7LpTsezfi3zfemEZoNYNVRIBVMhHvL3546AWCM3LUDo1VqZB6xbymkPQzuXEljiLNFvpxPVIP90QNQQWiI_TRDasrnYEgCr4TrES2UwkvJLanRQ0iy9gA2QIyF8lySqNxEtxstFnVzYCI_gi88RiPPWizQh54aDJOA9cVGZALMzbQ2XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c1770a4f.mp4?token=l9zg94dbk9pESps1AvSz2e1X94v-YXWx-QoNgfserqjQ5kNgWvV40_QPP8E-U4-F4Uo0pyA19OsFqM84GIo33By6dui5rvEGF5XkcWdS54jmn6el8hJJLSjHKtM02w9rbjI1xncXZrDvKEp1z9OPGvkaNrea7d9WV-GtrS7LpTsezfi3zfemEZoNYNVRIBVMhHvL3546AWCM3LUDo1VqZB6xbymkPQzuXEljiLNFvpxPVIP90QNQQWiI_TRDasrnYEgCr4TrES2UwkvJLanRQ0iy9gA2QIyF8lySqNxEtxstFnVzYCI_gi88RiPPWizQh54aDJOA9cVGZALMzbQ2XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایستگاه‌ برق تو شهر لوبرتسی، منطقه مسکو "روسیه" درحال سوختنه
🔴
بعد حمله اوکراین، اون منطقه بدون برق مونده
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131255" target="_blank">📅 15:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131254">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وال استریت ژورنال: اختلاف بین بن سلمان و ترامپ در پی جنگ علیه ایران
🔴
رئیس‌جمهور آمریکا به دنبال کاهش حضور نظامی در سعودی است
🔴
مقامات عربستان می‌گویند عدم سفر روبیو به ریاض در هفته اخیر، برای تحقیر آن‌ها بوده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131254" target="_blank">📅 15:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131253">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUnoYOMGIYFpGdFs3nH21LfWu_Vz3suIPkfaCKjhWNzu5go2AICwy1RypKfT6EX5ndT1I-SadQGWjIG6D0DH8vtVO_MiDVlM3GpKRMtTJJyJUWi54Llqa5WXFWpCxBJVVhw1R8BXIh63Om0yxh1sjoLPaTH8Of1MTYtbGr8aUTgsMZm3KYlpjzAwBwF3MtjiU0yRVnyQbsS94dyeUhj1vtEYc_UkGGYNw2r_IqwstqBL_ZX3zAB0BOdYC-jpBBbjhIugdTi9cYYh68V5jlWybejzg4SEXe43brhzVfFYB4fniaop_9i8U8jcGFv_iCeTGQ6ekra5NgU2MnRCCcmkcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشف لباس زیر طلا زنانه در بازرسی از خانه نماینده پارلمان عراق!
🔴
کشف لباس زیر از طلای خالص در میان اموال کشف‌شده از منزل یک نماینده زن پارلمان عراق، جنجالی شده است.
🔴
به تازگی و همزمان با بازداشت عالیه نصیف نماینده زن پارلمان عراق به اتهام فساد مالی، تصاویری از کشف و توقیف حجم زیادی پول ( دینار و دلار)، جواهرات، طلا و ساعت‌های گران قیمت منتشر شد. در میان این عکس‌ها، تصویری از کشف لباس زیر زنانه شامل سوتین و شورت ساخته شده از طلا با واکنش‌های زیادی در شبکه‌های اجتماعی روبه رو شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/131253" target="_blank">📅 15:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131252">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
مرکز تحقیقات صداوسیما: تماشای رادیو و تلویزیون در میان جوانان و نسل زد تقریباً در همه کشورهای جهان کاهش یافته و ایران نیز از این روند مستثنی نیست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131252" target="_blank">📅 15:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131251">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZX4x5JJ5e2PcVrpjXgqXsMzZFXOnKOZsQ_qPsvFkEhrarmCygyQBdh67IhgL4g7DOh0IXgJbRxS91TSMe4IoBO8oTYBItIECOTQI0BHFeZBQ_AXOuBOtxWCK3kiR8uf0bJCzEaUFDgY9DMnWB7_KO5pL89-r0NEUbomHS6DnfcUUtDiIxjWPerH1YbUWLGPS5IF_n27ONzECrBoP2wbiTzFqhFTMryn9gWgiBo-w8N8PjdlO9fXx_Er4GOwRP7dmcWw4Uq6sF0Wlta2s248jXnDtl9MlGwfGJkz7gIAa_6nXMM-7dLFGcszPTxKMJ0CPzpugHXiGj8grfekLoouaSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / منابع العربیه: توافق اولیه برای آزادسازی ۳ میلیارد دلار به ایران حاصل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131251" target="_blank">📅 15:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131250">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
جی‌ دی‌ ونس : فکر می‌کنم کاری که رئیس جمهور به ما گفته این است که از این تفاهم‌نامه برای پر کردن مجدد ذخایر نفت جهان استفاده کنیم و بعد ببینیم اوضاع دست کیه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131250" target="_blank">📅 15:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131249">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGwkSpd64IOD3-c2XNg-zpHSmtKC6_FSkrcPPQkARj7s9PO354JT3rXKBRm28TNx5uDW4Ubi7gIzpf9R-7UqkWbpR7PyCb-iGevreBKX_tNyCj0Fvphk_Ru48S3kvZycesNs3w0jx8lwY0AE5JNIGNIJccQmhlSCx5fZbrIBhMOG6D6L_JRx1M1n6BqgL5buY4pk8Ry4zcZdmgQmIU2kAbXMTBkYssQ7IM6t9bdM-4UFB6iXbmFO5SAmhInpUz5ZFOwFavwaKBT7mascAVII6Uv5vkvj0zXlXj4OeCDNelijq4iMR5qYAtu595D6hyfW5ZBz6bvlrj5ytaLEFLcg_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه هواپیمای دولتی روسیه بعد از توقف یه ساعته تو تهران به سمت مسکو برگشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131249" target="_blank">📅 15:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131248">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
پزشکیان:ممکن است در برخی مسائل دیدگاه‌ها و سلیقه‌های متفاوتی وجود داشته باشد، اما آنچه باید در این مقطع تاریخی به نمایش گذاشته شود، وحدت، همدلی، هماهنگی و انسجام ملی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131248" target="_blank">📅 15:09 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
