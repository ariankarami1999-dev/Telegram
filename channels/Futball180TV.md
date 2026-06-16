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
<img src="https://cdn5.telesco.pe/file/nsTl0sBdmqKtcYk2XxsvZzO3MDGr_0MmKNM2vPW6cUdNGivhTgOpC3D2O9WdMpTfXkxdy_X_3YHCtxsg9MGjBc_AITRIpG0fpJeWJ7mJa80CHfXAosuk4tpgCaSW7YKyE2NIkkcL-37f-ZrqH_ROAk3NZfOmFsd-8ZR9MiVuRYefRGDilIMXPobAyyzMr7v_s4K9Kee1rYPETDpAyThQnwZwL1tr3HwJky8Ha9xBUCaCRkSux18tdJ5eD-sgN8wDLjdy913hrksyJkDjR3PoHvJ-fy1cy65iog5x31JFVW67Udi9RmYhYdAGnOB6Ga3IiNbPV0NyLyF4p0XI5j3AVA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 591K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 12:10:17</div>
<hr>

<div class="tg-post" id="msg-93587">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f49a9fe65c.mp4?token=QigQQNj4-SLAjl2jk__Vv6LHkgS2XgAUQ1MsCZz8r9FbzF_Z3dApSJVhcsLl0G4xrTEGMGMslfyzt9HNr8HH691NKmzyrQxoAwgxd3ch4VKgtUikxudzpEU0i0FFvKoD9Whv9tClk-YjCQcFhQZPYr9cFBvNFekd6W03H8dPrdQdpYUaCMqyQEiqlr94PR3x78mI21-qmlR0jvKVIcuyj9zTqlUAUIRgQcT9ISqE8WF49_UHExS0b2UlMNUou8vLB3sX5Z4RfnMjc1KeE1RFz5R-alnL7NKlDH88ab_OZq5Nucf38XImtHqAc-yM4mfBVGGvyvYnD3fyAYm1bSAbGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f49a9fe65c.mp4?token=QigQQNj4-SLAjl2jk__Vv6LHkgS2XgAUQ1MsCZz8r9FbzF_Z3dApSJVhcsLl0G4xrTEGMGMslfyzt9HNr8HH691NKmzyrQxoAwgxd3ch4VKgtUikxudzpEU0i0FFvKoD9Whv9tClk-YjCQcFhQZPYr9cFBvNFekd6W03H8dPrdQdpYUaCMqyQEiqlr94PR3x78mI21-qmlR0jvKVIcuyj9zTqlUAUIRgQcT9ISqE8WF49_UHExS0b2UlMNUou8vLB3sX5Z4RfnMjc1KeE1RFz5R-alnL7NKlDH88ab_OZq5Nucf38XImtHqAc-yM4mfBVGGvyvYnD3fyAYm1bSAbGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
💥
🇧🇷
برزیلی‌های ساکن آبادان در جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/Futball180TV/93587" target="_blank">📅 12:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93586">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a638ae04ef.mp4?token=FDsKI6_ePIBZ__UXli_wfKqs1GW65cOni9hOzi3yHFAzaL9U-Csu8Kv8RKxMct7npr64Igse_zG8Cn6ZctrXagUxTsxBRCbEL7JqwYvAc3Gxzjffohgn3vVzq4vZLQqi4RiR6JFa22Tv3F23DgPH-Eqa2vKHl9VTpGVdcyqYUMRuoFc4cyeCkvQs8HiJ2m_AeQbuwiulbZKo8FmdfzoLIYazLpUpwCJX15yXJtMzvFS-FdE3nZbFMES76icZYi266Wn1xzsuDy06ipUPB_eCNTqhM0x7OdzTzEgFpFq5mNfogcfQjDXd8cLlwdvYERRREPR25g1idgHsfbkcwtE3uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a638ae04ef.mp4?token=FDsKI6_ePIBZ__UXli_wfKqs1GW65cOni9hOzi3yHFAzaL9U-Csu8Kv8RKxMct7npr64Igse_zG8Cn6ZctrXagUxTsxBRCbEL7JqwYvAc3Gxzjffohgn3vVzq4vZLQqi4RiR6JFa22Tv3F23DgPH-Eqa2vKHl9VTpGVdcyqYUMRuoFc4cyeCkvQs8HiJ2m_AeQbuwiulbZKo8FmdfzoLIYazLpUpwCJX15yXJtMzvFS-FdE3nZbFMES76icZYi266Wn1xzsuDy06ipUPB_eCNTqhM0x7OdzTzEgFpFq5mNfogcfQjDXd8cLlwdvYERRREPR25g1idgHsfbkcwtE3uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👀
پاراگوئه با این سیستم هواداراش حیفه امسال شگفتی‌ساز نشه و به مراحل بعدی نره :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/Futball180TV/93586" target="_blank">📅 11:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93585">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2uOibO9N4IeFYzYXyHXtPr6uzIVyFpmfUEH7BCOhp58fsmETHY3oklfdIuWkd02_u0dX4M71DkbxxovVz2OQKTacgI2XVwu0bNuCZLn4bWPAlxfVc7AOqVKbXeBZ6HQHQo2dLc-Q5p5RUpNB-j-SgkoqBMIexV_GGZb8K9cZe4IDgJ-SD8_KK7eXKjxRFqLowt2sq_SkNtRH8DNhYJIKm6LSesYy9IEVi3ZHPikiCnbj8KG4NlZ_fntqT131sH8oATY-130U9x-3O6p9bwV28JYXjq-iA_inzPhs6r34qXUdr8EQcDSD2Oflm01DwvN9MDqwY4VsCZO-dbxC2lCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
پشماتون بریزه ووزینیا بعد از درخشش امشبش جلوی اسپانیا تعداد فالووراش از 50 هزار تا به 1.6 میلیون نفر رسیده و همینجور داره میره بالا.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/Futball180TV/93585" target="_blank">📅 11:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93584">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15c36b833.mp4?token=mvXYn6P-OKf73WGSuLQoCtTIGkksWCWOsomqrdV5tPWd7M-u6ucccTSCzUtynJgSNgrD_zuIT30neWalkvfjZ87onGmIKXjKCotroom05-dEtxdxK0vw7abT_iEFhijfiwxfpVuOEKxHRI0nWPvq3skd7L1TlQrQ46yfz6T-LVfYsDfZMJ_q6yJnZt6Gi-x129wihzNeh5bwuIDu5YYWVks7q88U3LhZtlpftpC7oCMTxjCPiZ67PUtDEyBvPvTv9QTM_Io5G1X19YHBFQUlUC4JGzuXgcJIS1lsJIGudBe6bk1ajnytuikwNwMSiqVkgeWI0E3mflHLvzPXcqhOTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15c36b833.mp4?token=mvXYn6P-OKf73WGSuLQoCtTIGkksWCWOsomqrdV5tPWd7M-u6ucccTSCzUtynJgSNgrD_zuIT30neWalkvfjZ87onGmIKXjKCotroom05-dEtxdxK0vw7abT_iEFhijfiwxfpVuOEKxHRI0nWPvq3skd7L1TlQrQ46yfz6T-LVfYsDfZMJ_q6yJnZt6Gi-x129wihzNeh5bwuIDu5YYWVks7q88U3LhZtlpftpC7oCMTxjCPiZ67PUtDEyBvPvTv9QTM_Io5G1X19YHBFQUlUC4JGzuXgcJIS1lsJIGudBe6bk1ajnytuikwNwMSiqVkgeWI0E3mflHLvzPXcqhOTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
توجهتون رو به گزارشگر کانادا جلب میکنم.
مهدی گاییدی
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/Futball180TV/93584" target="_blank">📅 11:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93582">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jNUInv4em2nkbg3UX9l2C8LlHhI9-xMZMDQWlva28I3ccZ76WZ-wWPwlJy7EePdLGaz1svqFB8beU45RLngZZOiehDyq-b7pgciib0JU623uvB6uGlVIqMJN2q371ZBDB8Yrm60CXHqvzTqRv308VvUDv9Xwuj42IDrpp4uUHnMamB4b-oL4JAwEw6zzRO8qkdJ1uQeTDwmG54FfpkjftF2iE38n_qwzwWKqeH46y7v2SyFFzpbDAown6_W_KZssS-BEBdalNMHkJU8cKjHr2vpXs4VF5CAuKbvmgZJ9bh681xUuiM-MNCA1qWldEjcVxDjkdRDNK3xpC6POzdfDmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p9-5P710ByQsy2kPEt8LsF5Ea87xF25sWaTueCPveZjBMieNNYsRCPzUA-xdp0ajKC5ue0ToL2JRa3rf5yXTmMtHlITihO8ZpuJr00-OsZgQ9krdKPV_I7aoY1LuhTFBI2ttQgdfu9hXJYSuGDt-Rubd7_iJYxpK4veNrYLlgmMcJh7BDSmLVCq-Yg6o003n_EE258aBKS7OPCs2kLJZ8lLiTozdjY7HU7W1WS7fMBTzcWPJSXt5PKZxukLyI5vQ-6TWyTQegLjfQqlygkg-WciTGoHHRMGNEFmh5psAYhhVhjJ7iHR1qtmUgKeRXvJX6KSbZZaG2XsKRv-bUopjFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
گزارش اتلتیک از گزینه‌های باشگاه رئال مادرید برای تقویت خط دفاعی:
◀️
نیکو اشلوتربک
◀️
روبن دیاز
◀️
الساندرو باستونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/Futball180TV/93582" target="_blank">📅 11:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93581">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g78U_5QD-xNd-gpV99VYpkU_o8z7h8tmPIPvKjAEeMCjzsF03WD87hqKhBtTU9GnJYhbTaU5DM1YUj-fRxoYhwYUM8mKbetIPYFuQcDOr1P77OLIzpv5Ab_JysncDyeF57qF2XQEyv6VI_ZXFq2_8ZemTZiQfbt-Xkej5mixI8_qjel8n8111nQZwf_LTltwRe0lFTcnK8VZ8ImpjcnAq9B-U7j-GlPldPH3WwWCjjz_Tc6MZaUB21_S6pgT9o2hgqkp8T9n4QyW-9OSpNmbNNPe5PJrj393uuUDIIYQHIpKWf8q5epcap3-HsYB_OYR3iCcoR8r03bjjc-bRLb5zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
گزارش اتلتیک از گزینه‌های باشگاه رئال مادرید برای تقویت خط دفاعی:
◀️
نیکو اشلوتربک
◀️
روبن دیاز
◀️
الساندرو باستونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/Futball180TV/93581" target="_blank">📅 11:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93580">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7db3cbe5.mp4?token=teEA5Ms6YGPfXEWYJYlm7tkqn5WCHhFbezvtVKVb6fSZrHOjIXBIQY4zo3hIlUvZACW12xmH-c_CbfYGvlg4AuyxkUXIrdUeYlvgv3E6ydZGQsT1nGms4Facr5ECcwuCbQjnMDBCd1peQCrm3cPf_4s__I3ZDgGUS8kkb6BJyJ6kxo4vylDDUBwaBCW0MVWOPEOkJdZWHpSDVeB5CskBKl-25bxkvNft_g7ee_QrGgg4F9QLErnH0AnGx3J6YfC3hNup77C3sVVDPA-_rc1P03xzcBupXACd3UhnokO_7PCzW2TXkwsgc2sYVbFw6zAaeFkq3YJGjKLLBk9CAWiw8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7db3cbe5.mp4?token=teEA5Ms6YGPfXEWYJYlm7tkqn5WCHhFbezvtVKVb6fSZrHOjIXBIQY4zo3hIlUvZACW12xmH-c_CbfYGvlg4AuyxkUXIrdUeYlvgv3E6ydZGQsT1nGms4Facr5ECcwuCbQjnMDBCd1peQCrm3cPf_4s__I3ZDgGUS8kkb6BJyJ6kxo4vylDDUBwaBCW0MVWOPEOkJdZWHpSDVeB5CskBKl-25bxkvNft_g7ee_QrGgg4F9QLErnH0AnGx3J6YfC3hNup77C3sVVDPA-_rc1P03xzcBupXACd3UhnokO_7PCzW2TXkwsgc2sYVbFw6zAaeFkq3YJGjKLLBk9CAWiw8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🙂
کل‌کل بامزه ابوطالب با امیر علی‌اکبری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/Futball180TV/93580" target="_blank">📅 11:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93579">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCNN4_-u-0HVlITZ7o7FInOHCxcV8f8tXLNhw1iYpYrJrlKLmHuQwfTD4BJGlNjz7L7RHJlvkR1E9od9xrVehAEndCUB_co3xkLyYIBqVOzzWptMQorqJi8xIBQac7QjsOx9g_WDUbMc3-LD_cJPMn_8cEnFHMuf9AiPslPW_ROQO3iOs7IRBis4qrNTer1eytgGQjP0nLR0QrSWcC_Kt22cY0FOulZ34z4cJYurcwmfRkKdAD-yIX9-zxoMSD7hEmT1lqODRtenSUqsYRChSqxkdGVMyu5264k7wTBdMKlL-6-zMrUEHgMO5V3PII_vsK_zdRI98K3uCuXpiHWx_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇳
فدراسیون فوتبال تونس از انتصاب هروه رنار به عنوان سرمربی این کشور تا پایان جام جهانی خبر داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/Futball180TV/93579" target="_blank">📅 11:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93578">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUfV5yKClT9TXcvXBIC2XjK_650G4jETBAhdVZqXgIa2F5zlPg-Bs_mYKqvcPgP_zHyQFp4_AJYKh3jBItkKvDxdAM0lXBJ9MHiCWeTBf0IQyejE9WlCZoiad9PZgLYn2iP0dSSVF1lLxVOBra2DU0pFBeRxVsJXhtCuOMJ-uHI1glAKeDN5ACj6vd8vkc2DsOPHMWRXQfsQOgYUs0ICzOwX-R05hjwBCAPKEwPuJuBRR7QPYX1Sng6eMD3fRf4aLat6CwV_aTvsYTS8D6-Jkg5cyNJqOXiTI2WLfeo5SCNZXfzLd6Rf0OtIjpzGyxxy4GcPlXCpXyqT9C5dSm2KqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گنبد کاغذین:
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/93578" target="_blank">📅 11:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93577">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88a7c2e1de.mp4?token=uRhJuKGTxVfQhkPPwSrpQZUA327VQaZsEfYojKASIUMMJmfKsbOg6vk3TnY8Mhwc6ELY3_pEeLOURQCEthGFsMG6mTrSuvsSrdbI3Ka1obOgyO536-KkyYzTsc7SCYS3JdigT-aIEPdyx5yl-VVGzagBW5gqYZ24nhatAWIv02Ex_FpBb4sEJCS6E-ZNDp3euvOF_0kuoyD9qZIWx1NfGCuIa_YhlQc7ujvvYg1uZgmWVYgLf9r4tz7a0Jim_APD9RpHmMPodTgT2VggxX1dnYiF31K0MOtUHqVKFAoN1mIEACWUtgLkcWYBH-i_hRqm51LLu-oADwBP-HJL4c2vjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88a7c2e1de.mp4?token=uRhJuKGTxVfQhkPPwSrpQZUA327VQaZsEfYojKASIUMMJmfKsbOg6vk3TnY8Mhwc6ELY3_pEeLOURQCEthGFsMG6mTrSuvsSrdbI3Ka1obOgyO536-KkyYzTsc7SCYS3JdigT-aIEPdyx5yl-VVGzagBW5gqYZ24nhatAWIv02Ex_FpBb4sEJCS6E-ZNDp3euvOF_0kuoyD9qZIWx1NfGCuIa_YhlQc7ujvvYg1uZgmWVYgLf9r4tz7a0Jim_APD9RpHmMPodTgT2VggxX1dnYiF31K0MOtUHqVKFAoN1mIEACWUtgLkcWYBH-i_hRqm51LLu-oADwBP-HJL4c2vjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
🇸🇦
🇺🇾
عربستان سعودی در بازی سخت مقابل اروگوئه به تساوی یک بر یک دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/93577" target="_blank">📅 11:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93576">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31883b78b2.mp4?token=Z_8kz2yS-7SkMtjS2M3vUd8pOju0JI3OuIZB46vdAsEV14hV8pJ0NBxWpLPou4t39XRUI9-axhwWmn-whwCx-i35hMIXp4y0gBwTBiOitTourYP_eAfgIYHPn1pWq-ybf3JdAMLeHMmPkRPhGpYAgH1BHSHtWULHNJHsRll1WxamJy2Wyy6ZAgvl4JrhX_RJKPKqRDuu4YhV8K2DuXWc0aBCR8XoOfYIDrfP2L5q5DzaHwG2hs0bLOVmtrI36UJ6WqFuDn8GtxjLWgbW9uEEAO9u4Qhc2QQCVDTrguBUP86UdxFCC4hn4UKfHgSyaC_RXxX23JrpMIyEDrJoVegqpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31883b78b2.mp4?token=Z_8kz2yS-7SkMtjS2M3vUd8pOju0JI3OuIZB46vdAsEV14hV8pJ0NBxWpLPou4t39XRUI9-axhwWmn-whwCx-i35hMIXp4y0gBwTBiOitTourYP_eAfgIYHPn1pWq-ybf3JdAMLeHMmPkRPhGpYAgH1BHSHtWULHNJHsRll1WxamJy2Wyy6ZAgvl4JrhX_RJKPKqRDuu4YhV8K2DuXWc0aBCR8XoOfYIDrfP2L5q5DzaHwG2hs0bLOVmtrI36UJ6WqFuDn8GtxjLWgbW9uEEAO9u4Qhc2QQCVDTrguBUP86UdxFCC4hn4UKfHgSyaC_RXxX23JrpMIyEDrJoVegqpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
فیروز کریمی: از اینکه ژاپنی‌های رختکن رو جارو میکنن بدم میاد چون خودم شلخته‌ام!
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/93576" target="_blank">📅 11:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93575">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNTggg9NsC6FA7VWu0jvOzHw7Gm6cUZxN9WanUE_LyNiowZinYT9A2iHhmel6Gf-1e1bmtcuKvnmmASao_FDsYFp_7b6OwTZE3zPi5WK19IDRbjhgQJDIl60nWn8zR9nlpP8y2COAkOIuP-oYKRHRj_TEzRBkwqJHMn4Ku470EqK8F4uWEGx8QcSVkHJ6nbde958X2W6kN4cKYkBarHjgCByDeV9MyPqCc2eTVeLaf83rsMT892hf1Vs7Zow995x8EmJOK70atKjLmvUlkVVAWILwMlvSbFL_Dv8J4cLc7KzmTB3vCo1MVShhCB9FkZFn_8nvXwdcnVV5tBFWC0Mcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
#فکت
؛
پشماتون بریزه که کیپ‌ورد مقابل اسپانیا، بیشتر از آرسنال در فینال چمپیونز لیگ مقابل پاریسن‌ژرمن مالکیت توپ داشت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/93575" target="_blank">📅 10:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93574">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11f4a62cae.mp4?token=itt-ysBqDa0gH9jA1eWVFqSUzYhSo7sPkfO3iacuNcb3fc6brHdTx2Vi7z39z1QNSLu4izO-7F9Zn5P7v6Nb31hMhn9RQU1n9ulckgjtufMTWvTZctHdjFGlfqbmQKHq-MzWo-b03bRd9zzc8bCTG1_q5pfOflwIDY9FiG6-8qQRrICokrohKvx6TOH1HCrGbRCexC1y0fD3oVwWmEF_I-AjbU39qTGYNY5_Xd6q821rtSdlKrgwcB2AEzvoJb-oiuGzV2myD8PGikNMZuySrn4g5_ORz_GzYdRmsAyPWz-XesVTQKQ094AjjZLPnQ3_37Uu118kNU2xjMqszwrtNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11f4a62cae.mp4?token=itt-ysBqDa0gH9jA1eWVFqSUzYhSo7sPkfO3iacuNcb3fc6brHdTx2Vi7z39z1QNSLu4izO-7F9Zn5P7v6Nb31hMhn9RQU1n9ulckgjtufMTWvTZctHdjFGlfqbmQKHq-MzWo-b03bRd9zzc8bCTG1_q5pfOflwIDY9FiG6-8qQRrICokrohKvx6TOH1HCrGbRCexC1y0fD3oVwWmEF_I-AjbU39qTGYNY5_Xd6q821rtSdlKrgwcB2AEzvoJb-oiuGzV2myD8PGikNMZuySrn4g5_ORz_GzYdRmsAyPWz-XesVTQKQ094AjjZLPnQ3_37Uu118kNU2xjMqszwrtNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇪🇸
بررسی تساوی عجیب اسپانیا مقابل کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/93574" target="_blank">📅 10:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93573">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49803c87d4.mp4?token=ew5ptCkMFMJplP-Z6Cj8cmHooY-xMl1haMhIQBPeiU0g-1JxyqrNQPx4Unr2D6b8-eEcuLmV7AT4amAuTVNDubcvxFSYFJUp7fATswTN1HEbcMmUkQedYO0d9KbKe4to0ImRv3QkBSO6b4NY20_lu5dEehk6f7cSpJ6j-C1iYcnMh67qL2yybBlBovYA0YXynPhmHQAG5yMMZzEeX48bwoTMIiY33YZc5vWgnu3tv0vc6Ce50rm7hAwf5antaHm-tnBSNSKW3nv1CqmBmvF8RhV8X9fM33UV2D79Ph3ANA2Ae_qxuVQusidasCn7Su-1KVBc4CAT7Jz868SDkAEQIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49803c87d4.mp4?token=ew5ptCkMFMJplP-Z6Cj8cmHooY-xMl1haMhIQBPeiU0g-1JxyqrNQPx4Unr2D6b8-eEcuLmV7AT4amAuTVNDubcvxFSYFJUp7fATswTN1HEbcMmUkQedYO0d9KbKe4to0ImRv3QkBSO6b4NY20_lu5dEehk6f7cSpJ6j-C1iYcnMh67qL2yybBlBovYA0YXynPhmHQAG5yMMZzEeX48bwoTMIiY33YZc5vWgnu3tv0vc6Ce50rm7hAwf5antaHm-tnBSNSKW3nv1CqmBmvF8RhV8X9fM33UV2D79Ph3ANA2Ae_qxuVQusidasCn7Su-1KVBc4CAT7Jz868SDkAEQIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⁉️
👀
سوال ابوطالب‌حسینی از امیرعلی اکبری: شرخری میکنی؟
😂
😂
جوابشو ببینید عالیه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93573" target="_blank">📅 10:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93572">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osAvwe0ui8g1T6B_9nuTJ2Rv_ZVB4QddsRRhsIrF9tRAqq5R_pTgKtctu6MPuus40-AKpxRUgVGFP_mIIun4_W8pK5MptX-NnnFKgsgkZSBSbaZc-_O8O75tGWy2RdtVK7ioKSs40UMFUfACYZB1gbA33gun5rMg4OtQqKSjcidvZcdLRT2pBdJ4-Zq-FhsmBtSSk2lAZVk65zRAQqMD0wHtjI84VmYHVSS121hsJLbTFJshXTBs_E55HvCLtEyjiEYaoClkmDEkrLpXsBBB71g6e1zWwVw8B1xZXnhp1tItIHwgALfo68-dvVgL12BJpj6TggkfsPO4AM1ZGwmdmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ویزای مهدی ترابی یک روزه بوده و منقضی شده و اون دیگه امکان ورود مجدد به آمریکا رو نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/93572" target="_blank">📅 10:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93571">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fu1StWcHUpFlHPpc_NfkueYF5NMRo3FOIGajblaEh3Yx84x-hM9ogVmUyblzSMMMBBsgYDhBNACE9s1BMmemR653uunBfYXR6gNXoLx6ee-UOSpVz5UMfurAn-UVqEYNEEmBb7zBaPJ_9XEP8ZGhpSu7mtI2gJTMveCYRVJ5dXhyV-5CN_ZjXNqGyrYyMm3gXHFiaOQdsuqrG5v7tmOPSMBCBLUf4HLVH_ytd2ANAheZhVd0Vak4rqm3XcgRs9W_Pt5M8xyX9TgAf57TSbMf9EVx_BglGXtzAv4_szisYV5P1zNiIxA2rO9Kj4div9VPxaBdUFfOa26zffF3Au4gXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به دستور شخص اینفانتینو نمای کلوزآپ یا همون نمای نزدیک از تماشاگرا تصویربرداری نمیشه و به همین دلیل برخلاف بازی تیم‌های دیگه که تا نوک ممه زنا رو هم نشون میدادن این بازی نمای نزدیک هواداران ایرانی حاضر در استادیوم خیلی کم نشون داده شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/93571" target="_blank">📅 10:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93570">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd4dbbaa8e.mp4?token=LdgEvb3m2H8GcpKM9vqFAkbUaSGedmiShvaATUdKMvE7ccg0bVvlLUobbohu7Ikn5yPfwcns4mCPrkoxdSEczV1IqvxxI3OwCyLKPNCC2FHD4H25ZbFNXIntYpqW0Q8dlNlCYU38q13gL_aQ5Ib_vhGT4x-o1ZClBx3wwxMEiuD-3F-RWBSa7yp6MUp02nXp-EkCi1_z7baTDIb3400LiYl9_tZy0zPUCwSCfxVksG_e8xqPXuJtdQAFA-OdEXQuIiK2DHIoq_ARLfkg5kSOmbbKkyMSdErMSX3FibkZYts4FfyMEMOGpVAQhnh2nywSgDFhUaIn2egTbwaO9kgNmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd4dbbaa8e.mp4?token=LdgEvb3m2H8GcpKM9vqFAkbUaSGedmiShvaATUdKMvE7ccg0bVvlLUobbohu7Ikn5yPfwcns4mCPrkoxdSEczV1IqvxxI3OwCyLKPNCC2FHD4H25ZbFNXIntYpqW0Q8dlNlCYU38q13gL_aQ5Ib_vhGT4x-o1ZClBx3wwxMEiuD-3F-RWBSa7yp6MUp02nXp-EkCi1_z7baTDIb3400LiYl9_tZy0zPUCwSCfxVksG_e8xqPXuJtdQAFA-OdEXQuIiK2DHIoq_ARLfkg5kSOmbbKkyMSdErMSX3FibkZYts4FfyMEMOGpVAQhnh2nywSgDFhUaIn2egTbwaO9kgNmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
😂
حسین‌ماهینی بازیکن سابق پرسپولیس: تقریبا همه بازیکنان قلیون میکشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/93570" target="_blank">📅 10:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93569">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c278508f69.mp4?token=k_TAt8YCTr_nM2bRhe61_FOzyQL7u1g8YO1IACUrOUr_EkpIQnrXnW1eWkzPLw_k9h1VJTgm4WIS7PCvCj_z7lBuzlwNv2LG1MjWshHmkWu41zZZqlS_Dy1O9dbdfT_7FjC7ltoYx-qTO79uY0sA-NxaYSN6BKKIBJ_EXZv87I0EuL9-6ZRDIX4Gw0xk2invvlXuQLkCAqWvksw88jdnSp0rFcF2cUP-a8ewHcm7nnCtvR1C32Ta1wgk_ERaFXDtlCj3Ht-NoWPQzws-3Ul9K4MfQGcNho8w4uIXIj8jy4NPla7DMs_gQ8t6S3eJyevwGOLX1OVIeBYyAr1CQ68rqlXoYE3w6GJcqgn_hT2d5o37KQceEaFpV3XiiBEyeqOy7etxZHQ4VuMsDugpmrik825GamUXEWHTIiY2yzyuVJuKQpn_vx8-ZO4C5lZvZk0W6Hv9CWNYPG_1aHs30WK3bj5h5QL_msakUJlM1rdTmdl9uqYwMoOZ0cFrk9DQX3M9W9jOCGkFc9Dk0_c0uxNADfid-dSJ64t6wRnpc-5EN1fN0wZ3iaEnapayY4ihhlp3T3jerhsNHOM1iw_c-LSuGA1kCqK0dRXr7sy0Uni1jx3xrW-72k_t47ZMPeIc3b7mzmj3J3CNncreFAsfTxmnCqQSs1mRcz-i4-dMU7ozB8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c278508f69.mp4?token=k_TAt8YCTr_nM2bRhe61_FOzyQL7u1g8YO1IACUrOUr_EkpIQnrXnW1eWkzPLw_k9h1VJTgm4WIS7PCvCj_z7lBuzlwNv2LG1MjWshHmkWu41zZZqlS_Dy1O9dbdfT_7FjC7ltoYx-qTO79uY0sA-NxaYSN6BKKIBJ_EXZv87I0EuL9-6ZRDIX4Gw0xk2invvlXuQLkCAqWvksw88jdnSp0rFcF2cUP-a8ewHcm7nnCtvR1C32Ta1wgk_ERaFXDtlCj3Ht-NoWPQzws-3Ul9K4MfQGcNho8w4uIXIj8jy4NPla7DMs_gQ8t6S3eJyevwGOLX1OVIeBYyAr1CQ68rqlXoYE3w6GJcqgn_hT2d5o37KQceEaFpV3XiiBEyeqOy7etxZHQ4VuMsDugpmrik825GamUXEWHTIiY2yzyuVJuKQpn_vx8-ZO4C5lZvZk0W6Hv9CWNYPG_1aHs30WK3bj5h5QL_msakUJlM1rdTmdl9uqYwMoOZ0cFrk9DQX3M9W9jOCGkFc9Dk0_c0uxNADfid-dSJ64t6wRnpc-5EN1fN0wZ3iaEnapayY4ihhlp3T3jerhsNHOM1iw_c-LSuGA1kCqK0dRXr7sy0Uni1jx3xrW-72k_t47ZMPeIc3b7mzmj3J3CNncreFAsfTxmnCqQSs1mRcz-i4-dMU7ozB8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇧🇷
عشق‌بازی یه زوج برزیلی تو استادیوم جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/93569" target="_blank">📅 09:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93568">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d211a827.mp4?token=IQ8P-psZvnKv8cwHjihnKzHuJWeAYhQ_NcRaz-XIViEKckmnBVlf2Y721rYAHItozlK9JXi760Ku7AjmZT6VRlQnCAwBQKoDGrvv800YFBvUQZdHig7NJQFqRz-UnURbglGWRqIlEI2a7FcBTrWGl6nY8MmWxu2o5mzlducHCt1a7aKgRoir2926m2YIOgfiAtfDmf6w9Rabb-gN9x4qBx688EZLe-EFf9Z-V_MsWwU2X2GMvwJzXlQJioSLpZICoDz2x2FUbN8Rxm3NipUGKRJaeWrkXtgPNiZ9FMQo8mq9IjaCcZ04Q69gluPVcg3SWZiIsGZlka70ruy4L3OreQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d211a827.mp4?token=IQ8P-psZvnKv8cwHjihnKzHuJWeAYhQ_NcRaz-XIViEKckmnBVlf2Y721rYAHItozlK9JXi760Ku7AjmZT6VRlQnCAwBQKoDGrvv800YFBvUQZdHig7NJQFqRz-UnURbglGWRqIlEI2a7FcBTrWGl6nY8MmWxu2o5mzlducHCt1a7aKgRoir2926m2YIOgfiAtfDmf6w9Rabb-gN9x4qBx688EZLe-EFf9Z-V_MsWwU2X2GMvwJzXlQJioSLpZICoDz2x2FUbN8Rxm3NipUGKRJaeWrkXtgPNiZ9FMQo8mq9IjaCcZ04Q69gluPVcg3SWZiIsGZlka70ruy4L3OreQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
وضعیت سریال‌های نمایش‌خانگی در ایران:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/93568" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93567">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e14cad201b.mp4?token=dnLthTLFxMc9R-87DY9cDBMS5TkIi8KxMLrvQaAo3LEHTiwWOUH1SGO158Py-gu1x2DUf6tEiT5kxsaG9wBeSNgZGX-0ssZF3AM7Pimgy2g3G9ed8sfbZq20s33pafrjz927e3S2M9QC_KpAnEAdOY8tJW_dsYqw2liPuWYxPsdrtOcsBE6v6dpJqUG1T5k77uH-vS29aUb7-4jPbe2OLsYpXPnDa1mSsInaXIJLTuqzmPTKGPDGMBjvoa4XcNMRAR96x3IIL47OTnRR611c5ADq9zx8LpK_rGtLx8Tij4giOM9q2qQO3I97dApFTg3Peel2bjJMaYLwY0uVUsqCSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e14cad201b.mp4?token=dnLthTLFxMc9R-87DY9cDBMS5TkIi8KxMLrvQaAo3LEHTiwWOUH1SGO158Py-gu1x2DUf6tEiT5kxsaG9wBeSNgZGX-0ssZF3AM7Pimgy2g3G9ed8sfbZq20s33pafrjz927e3S2M9QC_KpAnEAdOY8tJW_dsYqw2liPuWYxPsdrtOcsBE6v6dpJqUG1T5k77uH-vS29aUb7-4jPbe2OLsYpXPnDa1mSsInaXIJLTuqzmPTKGPDGMBjvoa4XcNMRAR96x3IIL47OTnRR611c5ADq9zx8LpK_rGtLx8Tij4giOM9q2qQO3I97dApFTg3Peel2bjJMaYLwY0uVUsqCSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
یکی از بازیکنای ایران موقع گرم‌کردن اینجوری توپو کوبید تو صورت یه هوادار نیوزیلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/93567" target="_blank">📅 09:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93566">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlU8n21XJiEio926F1syb3AW4hTqQA6zXrsSXoClNG1R31CYz-KTGj9xjDCQBzAvPefs1tt3bh_qShYNRQn1o5oDkUzrGw0-wZ7_eirEn7Fl7qXGw6JD8iQ3D1GAXtJF36czcliY-673NCYE2Hl-t7SEQE89TTMjdC3DmYWdR7v6p0U7g7lqbRIPyFr2KR62Zk8iXI8yBPtjwvdxmrmZpLzkrM88b_dRJAadNQZRt1hOPiDcQLV18rF8yW5YpyI2vkeKQkczm_bnLsBvmP52dEI8twx2wLOKsuCMO5mhkxXmZw6Us40blnXJIGAM-9wbtI0JvrBLOCuI-gdKsh0d3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
پست جدید همسر نیمار که در آمریکا حضور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/93566" target="_blank">📅 08:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93565">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBn2bWi5ov7taSEU_eM9zKC7WxQJvsgs_LBJrnJXmN9X74QZs8rexIVJq8BGy3jNEHAm6atm7QYwsYtBo4qZLNdUIkuUyAFRqKTV8oESTjJufduPSEWcTPE7fwZ8Ryid0rSiM3QC7qZWqEXNF2Lo5PbQGo2asAP5Nt6RAssxFVLDhIsvATPOwBxBFPcY7JbJekZnJoXeF9h8QJCQ59uC3DE04Sm6aFtVz5SmEm4gedfP9mFyGs1qldFfVg9EV-7iSnvOLFoQqeCNQo0HHdQY4tTnnqSzeap2TN2u1yqqRnbG8BzlsE8BJV1JoQGMQPYd_OmTdpbEgspoh3-0bK70kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنری که به یاد تمامی جاویدنامان سربلند ۱۸ و ۱۹ دی‌ماه برافراشته شد، روحتون شاد و یادتون گرامی شما هرگز فراموش نخواهید شد
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/93565" target="_blank">📅 07:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93564">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ba8e65935.mp4?token=IKl1AP5-XHZPSbV7AyqIWTlKiQUbnHISswwtQydEPVQ-fTJkUC5pcMeIiMqmMsg-SL_Xc_tMxHqTjLEIcOC_Lfr-Sk8Kx5LywQkzEtqOZHopcuuWb6CzvBiWeWMQp8ZwBFdqDz75M_XA1oo5Qw3trWQLWzZ2DBidz5eOvlk0Pf-dlstodWmPbx-8845dod0GTSMEdAOZF-KgdrMHc-pRx8nWj-S8pT7NZ1SkmeaQqKj6wR3wfg03zF_tQdH16QlGuyvZVtOioKwastqTRKryZOVyiGhMwEkHbZ-JJ80rWVrHwmh_uu01J6giM6OPjdt-MNf78KpAZoHxxeC9q9GLZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ba8e65935.mp4?token=IKl1AP5-XHZPSbV7AyqIWTlKiQUbnHISswwtQydEPVQ-fTJkUC5pcMeIiMqmMsg-SL_Xc_tMxHqTjLEIcOC_Lfr-Sk8Kx5LywQkzEtqOZHopcuuWb6CzvBiWeWMQp8ZwBFdqDz75M_XA1oo5Qw3trWQLWzZ2DBidz5eOvlk0Pf-dlstodWmPbx-8845dod0GTSMEdAOZF-KgdrMHc-pRx8nWj-S8pT7NZ1SkmeaQqKj6wR3wfg03zF_tQdH16QlGuyvZVtOioKwastqTRKryZOVyiGhMwEkHbZ-JJ80rWVrHwmh_uu01J6giM6OPjdt-MNf78KpAZoHxxeC9q9GLZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
درگیری هواداران ایرانی بعد بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/93564" target="_blank">📅 07:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93563">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de82df63b1.mp4?token=fDNiQbKAVYz8M6lNR_r3qkwPZiiMT1xFxuhzy_BUEu3GZ9mTFejbDVWoJM4ghZ0YUGo3nH275DSqvLEamdretxUz2iFO9ib7LzlRdIxIZx3g6WaY8pY78jg-WzDPNnakYiZUUw3Nukl2TTgbkc6NeaVdhTo4icd3IdAPxL_j9Iomj2YaU5fxa41iu0G1j_Ow6ErSrTtpiCDloSpbnwXI4xLi9eGrsi7wo-fJ3O-LvACogfo-xRMB6gkuoc0VuXx9bhAECTb9vOBTmKzstUeeYEoto801jd3iTw6-Ax_dnHSGoOUZd6VvmnBzONxU4rsLPyYXgR0cCxwYudgz1Y3AaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de82df63b1.mp4?token=fDNiQbKAVYz8M6lNR_r3qkwPZiiMT1xFxuhzy_BUEu3GZ9mTFejbDVWoJM4ghZ0YUGo3nH275DSqvLEamdretxUz2iFO9ib7LzlRdIxIZx3g6WaY8pY78jg-WzDPNnakYiZUUw3Nukl2TTgbkc6NeaVdhTo4icd3IdAPxL_j9Iomj2YaU5fxa41iu0G1j_Ow6ErSrTtpiCDloSpbnwXI4xLi9eGrsi7wo-fJ3O-LvACogfo-xRMB6gkuoc0VuXx9bhAECTb9vOBTmKzstUeeYEoto801jd3iTw6-Ax_dnHSGoOUZd6VvmnBzONxU4rsLPyYXgR0cCxwYudgz1Y3AaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انتقاد تند یک هوادار ایرانی حاضر در ورزشگاه از عملکرد تیم قلعه‌نویی مقابل نیوزیلند
❌
صدا رو کم کن بگا نری خوشتیپ
👩‍🍼
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/Futball180TV/93563" target="_blank">📅 07:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93562">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اگه به قلعه‌نویی باشه که الان میاد میگه نیوزیلند ده روز پیش فقط یه گل از انگلیس خورد و باخت پس طبیعیه ما نتونیم ببریمشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/Futball180TV/93562" target="_blank">📅 07:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93561">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‼️
اینکه در ادامه آمار بذارن که هنوز تیم‌های آسیایی باخت ندادن بشدت آزارم میده  سطح هلند و اروگوئه و ترکیه و جمهوری چک کجا. نیوزلند کجا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/Futball180TV/93561" target="_blank">📅 06:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93560">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ منتخب ایران مقابل آسون‌ ترین تیم گروهش از باخت فرار کرد
🇳🇿
نیوزیلند
😀
-
😀
منتخب ایران
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/Futball180TV/93560" target="_blank">📅 06:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93559">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dr1DfWJfZVzxHkOliYBwtIBTTfvFNtpG0YUlJscOa2_YAlqpY4VZYaPSgglqj4LXHPiQzBTniHMNbRLse3ZBSUQi-e1kFq7e2I_glCzGzxJkudD2lvEaIbd0BT0mHC-tpitl8sPH73sUwrhUl-UObtJYd3mMLKz_jkqt5isHQwDztfqJgarSkthbLBgkuwshNNJ-PCpnTrvfy9BVPOGUombjd7WoLRf0GhMNGKS5_aYN47htdq8-Do4QPHHo7vsTr85qb9vW_t8bZxbXTd3HQx7nhwwLVEpGxHyNqSk-Y_rTAbgTo5bHxTvm7p5PXShBFUkBD9d5HPyY3TURHSyj6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
قلعه‌نویی میتونه الان تا ۵ روز دیگه از جدول اسکرین بگیره وگرنه خاطره میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/Futball180TV/93559" target="_blank">📅 06:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93558">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4LaGY0803XDAjU3cNBK1x9AVQkzBO1eq8Td2iSsU6ruUgkoqtbVND2qoTqguexSRLqjzLAzs0eVQNYwhvcIHnGocYioHFmYM9459ExmDDrlU8sk4J6wsuF9Y1pDf3DRKLoxvKolQfNxgkKTEXnLiFFmc-WTrWnEjqUHHuzo4GZDMTngh5Q1_eKolRkV6M-DZSnONU7UgPvZeVXTNpDjYqY7G1hMK7RPSYinZY-bxewxEocxsdajW2zPgFEmYXLy07ytAFt_4rAEhFhScnqCVMsOpI5saThRob15Y4L2SuLyo3le-rBOTPoxdj5FHSopJuQr64lsluLEfBZ9aszz5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
رامین‌رضاییان بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/Futball180TV/93558" target="_blank">📅 06:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93557">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ منتخب ایران مقابل آسون‌ ترین تیم گروهش از باخت فرار کرد
🇳🇿
نیوزیلند
😀
-
😀
منتخب ایران
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/Futball180TV/93557" target="_blank">📅 06:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93556">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ET-Wyo69jt6smBjU3Vfn8pI3Hq1ojSR3chzrSrZ4qPd42xtTuoJMYUTAMK6sfz2JEI5i6JusY6yfkr-XQZ5L473lYZ4QEXUjXTrcxls6fHhjU6NV0piNWZBuIBQ30lIwQigoP84rYro7iml5-DqJghCArLHwatY8vYhhxD67jGS98InKQ5olzAu13JBwqrasPIbtcVFEHpzrrivSB2XQLhdxZsHmXyIE5dO8Z5VFtkncd7088bGFf4fzIuxFHNONkSXGSfaQHr8gd6CYblfz80x7OmFQ3O_6HK4oyOpEgrydfJzgDWSo2LyhKoQTs1tnC6DVTWZLraA6uXBg5oAfjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ منتخب ایران مقابل آسون‌ ترین تیم گروهش از باخت فرار کرد
🇳🇿
نیوزیلند
😀
-
😀
منتخب ایران
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/Futball180TV/93556" target="_blank">📅 06:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93555">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آخرین موقعیت تیم قلعه</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/Futball180TV/93555" target="_blank">📅 06:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93554">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آخرین دقیقه بازی</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/Futball180TV/93554" target="_blank">📅 06:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93553">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گل نشددددد</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/Futball180TV/93553" target="_blank">📅 06:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93552">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">شاید آخرین کرنر</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/Futball180TV/93552" target="_blank">📅 06:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93551">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کرنر برا منتخب ایران</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/Futball180TV/93551" target="_blank">📅 06:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93550">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">۵ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/Futball180TV/93550" target="_blank">📅 06:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93549">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">حاج صفی زرد گرفت</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/Futball180TV/93549" target="_blank">📅 06:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93548">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پلن این بوده طبق حرفاشون ۴ امتیاز بگیرن
ینی اگه این بازیو نبرن حداقل یه برد جلو مصر یا بلژیک باید کسب کنن که با این وضعیت ریدهههههه</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/Futball180TV/93548" target="_blank">📅 06:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93547">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sylKtHLY-bB-TFghTSW6pR7tJaAFLDeeC3Jb1R8QpXcigZ4GW0ySV50bbDSVX8-xRVRvC1fkLfPeW6WIRowkw_0azSd5xDMrgaoNAbEN6bdABhofKQIopimeg82Dg5P7puizwJFBKQI-WocRjIlJTu8LajmVUO5U4OGBhJ2Id8glWSSddxN57KIsIp9tvabwOlQC5Tx0A6LoabjKWjZN4PG1kSBOmyBEVENlFYXSigHNuB3K7yqNClvahcteutmWo0zjWL0umh_JrSr0nACsqoDA0v_8FukHe50bpB6aQtP2_XSSI00-0eun_nQeOPPm3Q6CekXj7JVRcP9yQdb_mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#
فوریییییی
؛ به دونالد ترامپ اجازه داده خواهد شد تا مانند جام باشگاه‌های جهان، جام جهانی را هم همراه با تیم قهرمان بالا ببرد.
🔺
عجب قابی بشه بالا بردن‌ جام‌ توسط قلعه نویی در کنار ترامپ
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/Futball180TV/93547" target="_blank">📅 06:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93546">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">علیپور هروقت توپ نزدیکش میشه فرار میکنه
مرد حسابی آوردنت بازی کون بدی پس؟</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/93546" target="_blank">📅 06:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93545">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftQNLAfbnk6LE_9WHmWtMFKvvOUXiT5PTBof5zRud6R8fhov1rCsPA0gnOtXVEc7gebEHQfONa2iqkRADV76BA-FvE9pQYAa98NS_U_vvGua3q2ygk6iEAzIaVjNvg_51cUQYC7hQPz1VZhdS-l3R3ABJ8MFCh5LJcVsBVeQPm6_0wIhktcXurDPA4JSvLnsgyoIrkuIasXf-Sp5Te33XJ2VMQuPl3Arv8pI59tA_CEO7vYmDWVOQ-1oXjcP84Z5cdbDlXjZwIYtSRc9gSVkLdh64IVEflshOOougOF_clinFzqZHhpWrp3nfSnkudo6dQAiM39P8wHcs-drMK4sYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به دستور شخص اینفانتینو نمای کلوزآپ یا همون نمای نزدیک از تماشاگرا تصویربرداری نمیشه و به همین دلیل برخلاف بازی تیم‌های دیگه که تا نوک ممه زنا رو هم نشون میدادن این بازی نمای نزدیک هواداران ایرانی حاضر در استادیوم خیلی کم نشون داده شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/93545" target="_blank">📅 06:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93544">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">عزت‌اللهی ریددد</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/93544" target="_blank">📅 06:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93543">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الان دقت کردم اونایی که پرچم شیر و خورشید دارن هم بعد گل محبی خوشحالی کردن
😐</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/93543" target="_blank">📅 06:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93542">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دو دقیقه پاسکاری کنید چی میشه مگه
😐</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/93542" target="_blank">📅 06:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93541">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏با اختلاف بی کیفیت ترین بازی جام تا اینجا این بازی ایران و نیوزلنده. قشنگ هر دو افتضاحن.
کریس وود پشت محوطه استپ سینه کرد، با سرعت ۰.۵ چرخید، سه بار زد تو سر توپ، ۳ دقیقه فکر کرد بعد توپه گل شد</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/93541" target="_blank">📅 06:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93540">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">طارمی بازم رید</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/93540" target="_blank">📅 06:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93539">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">طارمی بازم رید</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/93539" target="_blank">📅 06:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93538">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ovesz0bc8CjRoI79sMSwZtBKd68nn83ITLWfoeoI0OZqX8G2zpt3SLeG6Utc8sowuuq2pqosUeAEAxbOJofDo1AadJUXR2QF-GVgVg2TGH2JHG5Iwlctt_cqjSBi_Xp8THxFZw8wsoqUQblFMVJ1IedtaKz5eAG9euCCgc7CmFzDuyw7Jt8D--GMKFTT_z5ZHYoIS9zi7dh2p2h_yr_CDMD9dTT_9R4gmwF5WxUkX6Pd0sIOCTYVp8ERaTGaz7anMtfFjs5UEmGCyOXAys-MTDEi4dxDjS2c_jwxSKRNmVwHDE9gzTU2Wes805AUTvcFu6mvEeX3sHjbFcvLjVfitA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سکوت میکنم که این سکوت منطقی تره
😛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/93538" target="_blank">📅 06:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93537">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">هافبک وسط نیوزیلند بیشتر بهش میخوره ورزش کبدی بازی کنه تا فوتبال
😔</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/93537" target="_blank">📅 06:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93536">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFZM2KQrUw-DEZx0o4S4Zs_3rjB_L0PskDebtFD8VfhN5HlxbrSxQhd9tV_xhvLc1GouMd0DzjxkW7obQg_pZMu9DnFpOpdqky7QAgNgrz7H7p-V5GgGzPJF7TYCYa2a-qcdy4qzFp2AIbzMCB3bEyT1incL1UPFFov7FOCGLfl5FYC2-yTYvoz8o7HCtk-BVgVV3bbVPEVstjohcOijWeRLjavum1FcLQ1kavn8lnbjrlLIM1Lg3KAEujkVs2Q1PXclKDKLKv2ql-TpjmvHv30IuyKcC_Rxv3Sp_4R06Mm6Axeqf_3Q97yeim2Jl7W8w4rcyKa3l0M0_WHYJs-XFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
کوارتسخلیا مناطق جنگ‌زده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/93536" target="_blank">📅 06:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93535">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اینقدر اختلاف ساعت کیری زیاده که ایران صبح شده اونجا هنوز شب نشده
😐</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/93535" target="_blank">📅 06:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93534">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نیوزیلند تعویض کرد</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/93534" target="_blank">📅 06:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93533">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رامین‌رضاییان یه حرکت دیگه بزنه تو تیم منتخب هفته قرار میگیره</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/93533" target="_blank">📅 06:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93532">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کرنر برا منتخب ایران</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/93532" target="_blank">📅 06:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93531">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حاج صفی بجا قدوس اومد</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/93531" target="_blank">📅 06:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93530">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/118bebbcf8.mp4?token=mLWy7Zja-BnOythS8FF122D8CDsts3mshkuPnHknx4lx0-sXL8HAq9lAC27db0Uw3wCwVEY5C31snsVClL34Jv811rXJ2S0wBjRzMGhr-Dk1VkMQwl_xWnGdLTZb1-Mg1LTVzq84GrtewDTdG7imFpzHfGr3hn_O7BxyFAB3ogbn8UIVRjvVYLxzDYxFcWa98D4kuYjfmQxURzMXXJ7BR_O2Ue-beD-7HM1v4gkcjGzFlrB7JhGbRiuKWzZ0uYy0AGWkTaBJVMURdne4Ttz7xPTktzpUaj-hg6IBdurfTFM7wSyvQJniuxBjr0SFdKj_PURPvR4qfm3tqPRtPKgqIg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/118bebbcf8.mp4?token=mLWy7Zja-BnOythS8FF122D8CDsts3mshkuPnHknx4lx0-sXL8HAq9lAC27db0Uw3wCwVEY5C31snsVClL34Jv811rXJ2S0wBjRzMGhr-Dk1VkMQwl_xWnGdLTZb1-Mg1LTVzq84GrtewDTdG7imFpzHfGr3hn_O7BxyFAB3ogbn8UIVRjvVYLxzDYxFcWa98D4kuYjfmQxURzMXXJ7BR_O2Ue-beD-7HM1v4gkcjGzFlrB7JhGbRiuKWzZ0uYy0AGWkTaBJVMURdne4Ttz7xPTktzpUaj-hg6IBdurfTFM7wSyvQJniuxBjr0SFdKj_PURPvR4qfm3tqPRtPKgqIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل‌دوم منتخب ایران به نیوزیلند توسط محبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/93530" target="_blank">📅 06:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93529">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تعویضای بعدی رو بذارید بگم بهتون از الان  حسین‌زاده و دنیس درگاهی میاره بازی این دوتا هم کسخلن کاری ازشون بر نمیاد بازیو میبازیم
😛</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/93529" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93528">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">محمد محبی</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/93528" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93527">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گل‌دوم برای تیم قلعه‌نویی</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/93527" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93526">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تعویضای بعدی رو بذارید بگم بهتون از الان
حسین‌زاده و دنیس درگاهی میاره بازی
این دوتا هم کسخلن کاری ازشون بر نمیاد بازیو میبازیم
😛</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/93526" target="_blank">📅 06:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93525">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این مهاجم نیوزیلند شجاع رو گذاشته رو کیرش میچرخونه</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/93525" target="_blank">📅 05:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93524">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نزدیک بود سومی هم بخوریم</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/93524" target="_blank">📅 05:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93523">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/93523" target="_blank">📅 05:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93522">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">امیرخان اگه بازیو نبری واقعا کیرم دهنت
اینقدر بیدار نموندم که باختتو ببینم داداش
😆
😆</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/93522" target="_blank">📅 05:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93521">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دفاع نیست که
تنگه هرمزه ماشالا باز بازه</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/93521" target="_blank">📅 05:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93520">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اوه اوه</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/93520" target="_blank">📅 05:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93519">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اوه اوه</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/93519" target="_blank">📅 05:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93518">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5aa3b3040d.mp4?token=nD_jQHo6WSxsjR_IK62t4e5ib0Yfe6j_KVFbunHAHvJeZtN0kxe5p5oGqkMpKd3qm8dIn4wluHMFffeL1vm5o8QyGembULnVPhRPWl-SLPhAR1ezoHwn_97Xn6s7hDhepg8uai9-hp-ydkF6JiESBAz-dJlI_WvBZPYOwGEY47LM0HstngHMAsOwOA0hcE3coWoflvH0N3IHAAXCX3TdHdHMNmoTVUUGWBtTAIS_Fu_iiVvKKxwtFajXKL6izuAgxS90QC2cnNWa-Fdi2br13qRXm0MBKsFsZSmmGhy8RKVYj6ahsq41i23_WmjZ-LsLlkkWdDvHbsw8IUKO6pMveg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5aa3b3040d.mp4?token=nD_jQHo6WSxsjR_IK62t4e5ib0Yfe6j_KVFbunHAHvJeZtN0kxe5p5oGqkMpKd3qm8dIn4wluHMFffeL1vm5o8QyGembULnVPhRPWl-SLPhAR1ezoHwn_97Xn6s7hDhepg8uai9-hp-ydkF6JiESBAz-dJlI_WvBZPYOwGEY47LM0HstngHMAsOwOA0hcE3coWoflvH0N3IHAAXCX3TdHdHMNmoTVUUGWBtTAIS_Fu_iiVvKKxwtFajXKL6izuAgxS90QC2cnNWa-Fdi2br13qRXm0MBKsFsZSmmGhy8RKVYj6ahsq41i23_WmjZ-LsLlkkWdDvHbsw8IUKO6pMveg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇳🇿
گل‌دوم نیوزیلند به منتخب ایران دقیقه ۵۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/93518" target="_blank">📅 05:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93517">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دقیقه ۵۵</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/93517" target="_blank">📅 05:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93516">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خوردیم
😐</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/93516" target="_blank">📅 05:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93515">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گلگلگلگل</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/93515" target="_blank">📅 05:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93513">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">علیپور بجا مغانلو اومد</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/93513" target="_blank">📅 05:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93512">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شما هم حس می‌کنید مساوی تموم می‌شه؟
🐸</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/93512" target="_blank">📅 05:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93511">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/946a01d6d2.mp4?token=gw1RirLImOL9otPptnNheCqrmBXSqmH_MbEPeGL63uHONHD5ksmUjEI0FZGkR-lLsT1apXnIYI35l1GfoJoMB6oN2l5jgo1FIyj1OrwrRliisl_qMWF5hSS2oWYfIGoaFnb6E-l-WFeYF6Meacxc0DPSz83cOPu-TiDYJxJYbbvph1xA4-jdoGptFJQO8pw8f3ySkw3dSOFwU0TTic-qaDM7W_7gbiintjdXlaUq1Nskm4iWLbE-d0M26yCZ9VDI4e3cjJUzHxSXJ2KUUQy0c8EJidRo7PnsF-Gunl6b4H9w1tH-AfZtI3H1ZN6NPElSjphR4muhDE_x3gKF01egQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/946a01d6d2.mp4?token=gw1RirLImOL9otPptnNheCqrmBXSqmH_MbEPeGL63uHONHD5ksmUjEI0FZGkR-lLsT1apXnIYI35l1GfoJoMB6oN2l5jgo1FIyj1OrwrRliisl_qMWF5hSS2oWYfIGoaFnb6E-l-WFeYF6Meacxc0DPSz83cOPu-TiDYJxJYbbvph1xA4-jdoGptFJQO8pw8f3ySkw3dSOFwU0TTic-qaDM7W_7gbiintjdXlaUq1Nskm4iWLbE-d0M26yCZ9VDI4e3cjJUzHxSXJ2KUUQy0c8EJidRo7PnsF-Gunl6b4H9w1tH-AfZtI3H1ZN6NPElSjphR4muhDE_x3gKF01egQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیس میلاد محمدی در لاین آپ قبل از شروع بازی
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/93511" target="_blank">📅 05:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93510">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ریدددد به معنای واقعی</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/93510" target="_blank">📅 05:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93509">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خاک بر سر طارمی</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/93509" target="_blank">📅 05:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93508">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">قایدی بجا آریا یوسفی اومد</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/93508" target="_blank">📅 05:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93507">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بریم سراغ نیمه‌دوم</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/93507" target="_blank">📅 05:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93506">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
هو شدن نفرات منتخب ایران در هنگام اعلام اسامی توسط گوینده ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/93506" target="_blank">📅 05:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93505">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddc1604caa.mp4?token=l7SsfwiRxwsE-d95GlZaG8NU4IxY_axqdZdRporwSCiunVQcPD_k0wCnbBiGncy2Fq9dkJQCsdC2R_GoFMUDh2C-PSjmLnVFrcXyrV78zLacpnoAUqcTqwRgeDXWEebPk24ufsyfS0n8gYCrMbO-BQQV0-xoVlYpQl0ejE6e8sAcMaSeoJcnlNSCBo-B7Wrn9nxdpaVL0IJXOky-jPe7A8fpoVi4YHgSD8Ft3LCVXTwARz1BpAxcQi4-hqiIxNg3xmrO-fRwz5_h7HohNX_bPjQDHixPnaD8xhKG2b-poMf0OMCz2OOXa2GIesGei5Voa9_YRm2v6OaumcEBA024AI0krXE0fGRokvzjq1L7t528wrTzsZJEcC6N2GVG0s0_09yQmwCAj9fXXAzyS8pPWHW16u9VtiC09HnDQOjXtEsR2buN_IBDXzE4nXLeEbfeqVYiDrUGUxQBJ__kH1RQdzsqr3DeFuyqpMgnfSEqMT3fU6VbDeon5KqmOu9wksk8xu0UrUjyBuuznBo0vnhaKw8Td_AwaQzeAJd8C8i2A1O-KFjY91pkzfnBpD9ssu_if2bkHUKfwWrzUpbF_kWi0G1Sy0y4spMcgDtDhAHpPrYStQ_kl7VkOQEa-cWSfi8IN6JbM29VvVVqclUJXjSYtkLpRMzEiGCOxIBgL5-zarM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddc1604caa.mp4?token=l7SsfwiRxwsE-d95GlZaG8NU4IxY_axqdZdRporwSCiunVQcPD_k0wCnbBiGncy2Fq9dkJQCsdC2R_GoFMUDh2C-PSjmLnVFrcXyrV78zLacpnoAUqcTqwRgeDXWEebPk24ufsyfS0n8gYCrMbO-BQQV0-xoVlYpQl0ejE6e8sAcMaSeoJcnlNSCBo-B7Wrn9nxdpaVL0IJXOky-jPe7A8fpoVi4YHgSD8Ft3LCVXTwARz1BpAxcQi4-hqiIxNg3xmrO-fRwz5_h7HohNX_bPjQDHixPnaD8xhKG2b-poMf0OMCz2OOXa2GIesGei5Voa9_YRm2v6OaumcEBA024AI0krXE0fGRokvzjq1L7t528wrTzsZJEcC6N2GVG0s0_09yQmwCAj9fXXAzyS8pPWHW16u9VtiC09HnDQOjXtEsR2buN_IBDXzE4nXLeEbfeqVYiDrUGUxQBJ__kH1RQdzsqr3DeFuyqpMgnfSEqMT3fU6VbDeon5KqmOu9wksk8xu0UrUjyBuuznBo0vnhaKw8Td_AwaQzeAJd8C8i2A1O-KFjY91pkzfnBpD9ssu_if2bkHUKfwWrzUpbF_kWi0G1Sy0y4spMcgDtDhAHpPrYStQ_kl7VkOQEa-cWSfi8IN6JbM29VvVVqclUJXjSYtkLpRMzEiGCOxIBgL5-zarM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ورزشگاه یجوری پره که اصن پشماممممممم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/93505" target="_blank">📅 05:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93504">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b25ed16f17.mp4?token=V6SzB_dJJsDMkr5kjWTci3iWkU7-FDMw68_RdC_g-m0BjCEcAv40MMECeAiN0cXlK-izBsJS3dPZjXTYf4CO9dEWadeMtnkZinXihU_g-1EvWRexryn_mMjq_btFYissJJnMdZq5DvH8JGZZDkH3kRkjAgf7Ch41-UDitRryNBRR9hHhYrW7Wc9xiaZocTV-rysMXVxScczY7k8cNK1ifWFHTCcoQMzSnVmj9mAQsMot0zlUmj6B0k6ZTYh7XJJrYIXavK9NNj0bu-644sFq9zJ_GlsaLk1ncfETEVMoOSndLH7qiLen6YqjSixaU1ga-Jp9rKscUrFC7YT52WLYyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b25ed16f17.mp4?token=V6SzB_dJJsDMkr5kjWTci3iWkU7-FDMw68_RdC_g-m0BjCEcAv40MMECeAiN0cXlK-izBsJS3dPZjXTYf4CO9dEWadeMtnkZinXihU_g-1EvWRexryn_mMjq_btFYissJJnMdZq5DvH8JGZZDkH3kRkjAgf7Ch41-UDitRryNBRR9hHhYrW7Wc9xiaZocTV-rysMXVxScczY7k8cNK1ifWFHTCcoQMzSnVmj9mAQsMot0zlUmj6B0k6ZTYh7XJJrYIXavK9NNj0bu-644sFq9zJ_GlsaLk1ncfETEVMoOSndLH7qiLen6YqjSixaU1ga-Jp9rKscUrFC7YT52WLYyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
واکنش هواداران ایرانی استادیوم به گل نیوزیلند؛ صدا کم کنید درتون نرهههه سر صبحی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/93504" target="_blank">📅 05:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93503">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZPq-VzR5oRghKLuM9Fkzb5qhTldPrz4o66BRC9ZsciL9FOdGuv7sfHD2kMCrftuj5LymSrw1B4dusH6rZ1YYreBZOHlkOY8AYn6lzJOTOum9ecLgUOWwsiSr7G1ZXXMu3LqcUkbs19sOopzv4Ei15wp6OKDD7-XTH0v0dInEJwOAfAXYoEASgo3m18G_X9BEB8d7EpB2AmYf45vHYKNidM_3cdyooaGeHNIFohMyYv4bh-MDLOBTG3S6GzgZGmjOWv_NoFgkUsCAg8lG97P7duNMwbxjJTeSi7OaeEQ9RLY7snR68aE3Ji_PTBsHVgw1bH9riGG7jy1ZmNxJRPyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفساید میلی متری علی نعمتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/93503" target="_blank">📅 05:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93502">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
پایان نیمه‌اول با تساوی
😃
بر
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/93502" target="_blank">📅 05:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93501">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">واضح بود</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/93501" target="_blank">📅 05:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93500">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آفساید شدد</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/93500" target="_blank">📅 05:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93499">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">علی نعمتی</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/93499" target="_blank">📅 05:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93498">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گل‌دوم برای تیم قلعه‌نویی</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/93498" target="_blank">📅 05:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93497">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مغانلو ریددد</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/93497" target="_blank">📅 05:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93496">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">۶ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/93496" target="_blank">📅 05:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93495">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nhp3jJ53SiShrA4VLUrg180YeXSB8KkD00u10P5BbvvAFOjiojHt9HLa9ISv-ua-KgSmGags05lDFRkP0Ngx_RGB9UWj4RR8r84A8ICE_w4aHI-K6uREO9iKZ3gGryX0EWpnXYPdSbBsfsJ_sCMqLe023ZjFOsc0XxpKZAxU0g3APDK5hswGlDMo5lDQoKX6ISw22n5Ppmu-M8s6JmpR6oAqBON50zLVAq6ZMzTwcT8zV74mY5wvFTPaKup39Wmjwls3-ZU84ZGhRzfq3Gej-C1DRMjUNxtffyLxR_TXbc8ADqV6FPhC656qEB1Zdupi6QkjNAIq5fGT1qL60YvQqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوادار نیوزلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/93495" target="_blank">📅 05:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93494">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خطای خوب برا نیوزیلند</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/93494" target="_blank">📅 05:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93493">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نیوزیلند فوق‌العاده کیریه حقیقتا با این نوع بازی باید چنتا گل میخورد</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/93493" target="_blank">📅 05:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93492">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بازیکن حریفوو
😂
😐</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/93492" target="_blank">📅 05:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93491">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e40878478.mp4?token=VJBRAoyQseLQLFcs2jV85jxZ6Z7qCybORIVxjxKL9sRZTWLGpKAdT28RjSzOlFBkSCGhAl32Cj7bTphqCzW9GH2i4Dr1R8jPvK0s_M_3wrfAY-WoUm0H7R0AyTbz19-2tzyIFTpNWbFmFsx-fD_h9EAqUzpcR4PG6xB7llHVx_8KjrACGZLyZz47jj3VDV_i7WK29psKOMDrkqOcLlfoV_LpoqnNVQkIB31md7URZbMp3oewM3iFDzSQkuxy9ssltjY0JSTeHXAtJ05TdAR8d_pdjUGkkj-cV5SU6b7XmP5K_pD3NBHmyFLyFHPWGmqwpicL6ffcGuecNV8yLhQKnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e40878478.mp4?token=VJBRAoyQseLQLFcs2jV85jxZ6Z7qCybORIVxjxKL9sRZTWLGpKAdT28RjSzOlFBkSCGhAl32Cj7bTphqCzW9GH2i4Dr1R8jPvK0s_M_3wrfAY-WoUm0H7R0AyTbz19-2tzyIFTpNWbFmFsx-fD_h9EAqUzpcR4PG6xB7llHVx_8KjrACGZLyZz47jj3VDV_i7WK29psKOMDrkqOcLlfoV_LpoqnNVQkIB31md7URZbMp3oewM3iFDzSQkuxy9ssltjY0JSTeHXAtJ05TdAR8d_pdjUGkkj-cV5SU6b7XmP5K_pD3NBHmyFLyFHPWGmqwpicL6ffcGuecNV8yLhQKnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
گل‌تساوی توسط رامین‌رضاییان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/93491" target="_blank">📅 05:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93490">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رامین رضاییان</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/93490" target="_blank">📅 05:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93489">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ایران</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/93489" target="_blank">📅 05:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93488">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گل زد</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/93488" target="_blank">📅 05:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93487">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کسخل خر</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/93487" target="_blank">📅 05:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93486">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گلروو</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/93486" target="_blank">📅 05:02 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
