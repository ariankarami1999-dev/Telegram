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
<img src="https://cdn5.telesco.pe/file/f-ZuP7v9L5eFSA1PNWBNWqWJ87aHBVEYlWO3b7UceFXyNu6wJkHD-VX9kRVK3bsg43xufk3ueMXdex-4oiAlWzspCFqX9AUXS7kNXI5VgY5PKp2EJo9sJo7YLfpAhdS3xpZ7gyUdql7ZKWowrQLLKhO-FvVAlE9JrUkMn6Kzj7rs_y3W5i9kk-PtER-EBj1xjo0xBfrac0ZxWlDxaoCQmnOzkh79pUAMZ6S6jqFw3zRTUn03DYWU3Q_y9ZNO30yknkBb53t7JYKgTJpDCqugZn1yG4iN_6rlhQpFckxGPzH6CpJLzaPBrbFJMbUbvOvwmUoZj8JVtAbSAdVvd_1w2w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 482K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-18 17:11:32</div>
<hr>

<div class="tg-post" id="msg-103172">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f66b01add9.mp4?token=EcaFyLx7tojD0XFaIp0BWlK86iixsUKijp-xfxyvNTvt3S48C2aL1bZKu9-L4fCt99JrjUAwNgKeBr_issC0f5IKR4qGUr4Uu1N_clehX2ptuMgpyPdoKQdKELhrJ9uhPa-X_OLG6hKM-f6BRHtdgIGBZeKTVzrSc35MpchLQ2v-5bKpnqQhcA7V0Y8lKxb6Q_JkevkFEKhAWwu2PJre3g1ckt-UhVs4cE9mPipB0X0T7tW6F9gLdiDDXDVcptXQPy1UFgFyCWyjZKkpj861FlisH94h9b-7RE4T_nTqsDB-7ewNfqBVrYt6GrYJYadEv6lfprEDqlCd1E8aZbnMCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f66b01add9.mp4?token=EcaFyLx7tojD0XFaIp0BWlK86iixsUKijp-xfxyvNTvt3S48C2aL1bZKu9-L4fCt99JrjUAwNgKeBr_issC0f5IKR4qGUr4Uu1N_clehX2ptuMgpyPdoKQdKELhrJ9uhPa-X_OLG6hKM-f6BRHtdgIGBZeKTVzrSc35MpchLQ2v-5bKpnqQhcA7V0Y8lKxb6Q_JkevkFEKhAWwu2PJre3g1ckt-UhVs4cE9mPipB0X0T7tW6F9gLdiDDXDVcptXQPy1UFgFyCWyjZKkpj861FlisH94h9b-7RE4T_nTqsDB-7ewNfqBVrYt6GrYJYadEv6lfprEDqlCd1E8aZbnMCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#نوستالژی
؛چالش‌دیدنی‌پسرمارسلو مدافع سابق رئال مادرید در رختکن کهکشانی‌ها و ادامه داستان...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/Futball180TV/103172" target="_blank">📅 16:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103171">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjHqXBDlf-9KkykGigTTVCGot1ZMEkLelYeFvd2gRQ6nhGP-L6cVOB5K8KPlwyBdZ3BolqJGFEDrudAJuRdv6Uk0L4uorC5eHFpk6tfrKZZQ8HoimSyKyXb-3y9St1i6XrOHz5tMhGtFgNS3iOHt1LH8jq4nVsMFMOjdzy90QBPLdWQk4Nh5GOzGy0KJPcEPTiqkqbdEY0w3FHfEzfIiv_xJH-ZTvaqLSMTz-wB_M2frz7CiImqFqzfg1VLg5qetwrz61RWkXIloVBXJUbLxHVYtF9R2L_RAAtT-TlljECJ3s1OF23LqTs1tjpwwz_rQwQiXkzjky-FGRkD352T2Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📆
8 سال پیش در چنین روزی، تیبو کورتوا با قراردادی 6 ساله به مبلغ 40 میلیون یورو به رئال مادرید پیوست.
🎙
تیبو کورتوا: تا هرموقع رئال مادرید منو بخواد میمونم و قراردادمو تمدید میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/Futball180TV/103171" target="_blank">📅 16:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103170">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca151bf7d.mp4?token=glQDDZvpMcq2cKrwAnt5xEopeq7gzrPCBz9P6CPgQqBFpPKWzjN4Zt6rHJel6GhGS-rjNzqnIGH2D4MZb4T_GAQUmy20t8tKw7Yosv3U0viqwSyeiauBCl6gEb3gTA-1vGZUdA0ZLpmazs_E97Opdd-ZZNXx4jc4Op4qFcU6C9mGtD8X4FAvKdEvjzccvCjKUHJ4y5aT6t_sZMfN-dlyfWgMix1PmGqG5Vta31aahikr1a_I4H5CbyWw-_Ms0LFLk5Kj2ZxkyGZIMiBR2g5v3WIRYCXJDxeA-PnQi75BzU_wN1WP-V9L030kwwgJBUsJq4S8C8FEpjGfNC47c1DLBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca151bf7d.mp4?token=glQDDZvpMcq2cKrwAnt5xEopeq7gzrPCBz9P6CPgQqBFpPKWzjN4Zt6rHJel6GhGS-rjNzqnIGH2D4MZb4T_GAQUmy20t8tKw7Yosv3U0viqwSyeiauBCl6gEb3gTA-1vGZUdA0ZLpmazs_E97Opdd-ZZNXx4jc4Op4qFcU6C9mGtD8X4FAvKdEvjzccvCjKUHJ4y5aT6t_sZMfN-dlyfWgMix1PmGqG5Vta31aahikr1a_I4H5CbyWw-_Ms0LFLk5Kj2ZxkyGZIMiBR2g5v3WIRYCXJDxeA-PnQi75BzU_wN1WP-V9L030kwwgJBUsJq4S8C8FEpjGfNC47c1DLBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طلای تاریخی کیانوش رستمی در المپیک ریو
❤
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/Futball180TV/103170" target="_blank">📅 16:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103168">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t8pDCAV-DOS9zpr1NcUxzGyu9dnl69EPeFbTiciQdkpm3eFd2k1xtALEyDrPOMYNfZw_XWDv-q3y00RTFtPvUfCnlyd3UEnOdBHHrd31AYOkwl1eEQBA4oqz3GtUOQxjkjcM-QK771UeSCLFEBawuv02HCe_S28R5KFOXFTdyA6Yt04DcZYqLGe6cvJ0Ue_GZP5AJ6dxf7AkaITpbNkLZiPmLCBjeOWGLrWgpoHNynLYvS5YBuJ_BHrwqiJYvzyZnzFjDAxI_J8_tclrQxBRPuzqpPi744O05jdkrZg4T2t9KUaqBFpWki_HCSkBBd6TGPMINSESRhyyrL5zMJ8Zkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NN3QANWX6Y4IZspuGMIg1Cqw2s6-swU0iiWnerdC1cX_gVfBFMaRb6-nNLmAEUo4ZICtdeIO-lSs0C1VIUO-xw0PyosihrsM8gwgZPyMy7k9v1EzaaT4Hn468D80Tp5YtXr78jLzTSZyf9Fp7pNlB1KpldqXqP9Zi3yTmrf8E7qbu9GG-0XHW1n4hcYWskVrCNTldWcjG55u4SlGEuA3j_T7WO2dO4zM0Z1p8ttQMNXQJw7VSkT193bRL37e9TCmU5OqqNCC1_VQiA9xZRezpqLobcvOu6_N-h--e9SogBWvS399c2jhlENIb5eNT1iIPjC2cs5QR0DzlFmHk3ApdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
حمیدرضا رجب زاده یکی از مداح های حکومتی بوده که چند هفته پیش به قتل می‌رسه، حالا یه کانال تلگرامی مدعی شده اونا این قتل رو انجام دادن دلیلشون هم اینه بوده که این مداح تو دی‌ماه جز نیرو های سرکوبگر بوده و به سمت مردم تیر می‌زده</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/103168" target="_blank">📅 16:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103167">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53383c27e3.mp4?token=A_9JbV0lr0WPnVUpEBBFxN_ur0EUEFXYq1N_FCG8wa-GNJpP8WNPO4hSZmBHyuX1WDKFcxjHeYs6yXqxQOLvx_j_rvdhXl4z1b2jcsMF3gC_syUfnO-DOxxsBRw2fWgadRL9F3Q07UECRov7oBGg9ZmUpvvZ2qm1VXlXehyYKiBr0B_Q25ktu1Tr7930wycBmYK7ROdrLl4G3tLz2hfvdXpJA_gmQPrOF8ciXh29LmzdpP-oD4boJrzy1syfhD5jZ_p-ws7l11RUhKIgNWKQQMTi2SdFmmYSPgRQHOKVwhVa-E0AOLfaZlAnIykmJrh5NTPJhz4Gt4CYxRmardMV5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53383c27e3.mp4?token=A_9JbV0lr0WPnVUpEBBFxN_ur0EUEFXYq1N_FCG8wa-GNJpP8WNPO4hSZmBHyuX1WDKFcxjHeYs6yXqxQOLvx_j_rvdhXl4z1b2jcsMF3gC_syUfnO-DOxxsBRw2fWgadRL9F3Q07UECRov7oBGg9ZmUpvvZ2qm1VXlXehyYKiBr0B_Q25ktu1Tr7930wycBmYK7ROdrLl4G3tLz2hfvdXpJA_gmQPrOF8ciXh29LmzdpP-oD4boJrzy1syfhD5jZ_p-ws7l11RUhKIgNWKQQMTi2SdFmmYSPgRQHOKVwhVa-E0AOLfaZlAnIykmJrh5NTPJhz4Gt4CYxRmardMV5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روی کین اسطوره یونایتد: اینکه‌دنبال بازیکنی بدوی تا بخوای پیرهنت رو باهاش عوض کنی کار خوبی نیست. تا حالا نه دنبال کسی رفتم که باهاش پیرهن عوض کنم و نه از کسی درخواست عکس داشتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/Futball180TV/103167" target="_blank">📅 16:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103166">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogYPOkeMGoaGLl0JWiChBFCmgM2AnxMVL9Ax2tLLa1hFxtKyFtsIe3uD2tlnIHCWPlzXIbyGXYBrc_HmK5cbsrEWJAYnyvqXf6CP0x43jLdOKeYdYmKsAA4Mrtgy2Bg6LFtCg2uROcZJsUa_guICBSaiX8fcIqepBM2XjDhqwCf4sZ9hGWMKoij6InSF6PwNIMdWib2dANMUbFSkwBaZefFNsa0NuxN50H2Yt8y2g-BbrV10pd_sIRyl6b9MXdOsOu7nvyZTmmcD83ERJ3ltXjws7mz77MyzVpTu6J-cJ9-GYf1FEkOaOCopeGWAo02j5O_vqDu97ew0uFB9GZDS6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چلسی از دارالتعظیم مالزی گل خورده.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/Futball180TV/103166" target="_blank">📅 16:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103165">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5F4M3NX816YsdtHJz-G4mSRVJa4n1Vt1IA1l_hKS_T3eXle7rJsdMu9x1nFA8FHv5bcILfDRUbvhFEqgnONyNdoRhnyf8_f83FwHvA0NIuRizDNmo-o1O_YEBfs8YavvdE5jLnGAQcWBVtUYrE4wErCH8t_vFof03ZB828PShdarNIwLzShFyMqPrLoNlIMqOtNh_zaJNeTMKIsJBtl5Yi0Hy4y5ZY-JfKbepRLLfR2oo0-zO6Oarvlrkbu5CcEuzRjXhcOWkLre1-6OT6hrqYLaunFvbBI7c98orAc1WB4YfTx1KvLQLDDvcnuzOC35XCmk4uPMsqbop914JhonA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عمق‌اسکواد تیم‌آرسنال در فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/Futball180TV/103165" target="_blank">📅 15:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103164">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa7513247.mp4?token=k-BlPddl_RNs6Kf59G94MRAxgneh7NU35ipgMJTuZ8SjAsu45D67FsQSuCWnwRTh-8-u58zLUMYC27vKUR5BmcMQ70w_D9do6CqNodKrrUHBgnG3i3EC1GNieoLdonB0DjvjeMzkMENxcyTBbQEmWGEP37rePgLzrJS6Tv-KcHGFzduMyadH7mlAVX5yON7XJkNxZ2d4Q6Z0kmM7ccyK--803tUu8Rael7vaE0wkz093HdBVZqV5T937X0QXRoM8tlitGWNLurVRz2sJT5kb7cIMEVggkMY2ovVBNnLRnqOt8h3zNR7P2AyzGJgRlMQVthnKxhjeL3GzOqT_JH98MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa7513247.mp4?token=k-BlPddl_RNs6Kf59G94MRAxgneh7NU35ipgMJTuZ8SjAsu45D67FsQSuCWnwRTh-8-u58zLUMYC27vKUR5BmcMQ70w_D9do6CqNodKrrUHBgnG3i3EC1GNieoLdonB0DjvjeMzkMENxcyTBbQEmWGEP37rePgLzrJS6Tv-KcHGFzduMyadH7mlAVX5yON7XJkNxZ2d4Q6Z0kmM7ccyK--803tUu8Rael7vaE0wkz093HdBVZqV5T937X0QXRoM8tlitGWNLurVRz2sJT5kb7cIMEVggkMY2ovVBNnLRnqOt8h3zNR7P2AyzGJgRlMQVthnKxhjeL3GzOqT_JH98MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
کابوس شب و روز بارساییا در فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/Futball180TV/103164" target="_blank">📅 15:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103163">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmRDtYPowlbrdvoGimkTm99fK88Cf5JTM--XbVhg7TdleMm_l0j0lN1Ej3WXMWHVRgD_60QxsellOENCvH8Iv4X1wfmNrrwfLWuZW5Z1sJ0JRrZB8SAxzo0m-6irumEYjMAZOLWLVlhVPu_VJAHl89dzLBTogOxYOBaDSvFwJrklekCK0nbz4XVGV1aENckTs3TBdyIHoOmGN-dcEXu2_XiY2FH_u7X4FsIi0-hg_Q05a0VFKD2wN6XJj6756_ycWTgyYm8f0cAI2a2lbcGOQ10Y_pYmK_qMjtCVSIPRD9Ox8OQ-LaRlpBqNhVcUbs_ABDfLk5hKTEqfqPAPVRaTcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آرائوخو وارد انگلیس شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/Futball180TV/103163" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103162">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVYxjH-gejZ3pd4WaEb3VRtQG3Fg0UN9riU4mbCNuwPL_gEVfH4Cwq23DwnkQt_6YaSrRClqjjFjlSzzo8wJR8Sfr-zf86IOcLBzXoFNTRTEPFVY9EmQyNID8gJUqgDCtOE3pBPtIl739uLRCA4JbhEDNm8BEedUy8KPlw1GjOVmGrbj3goOfEHvCSShUsGuc5AsS2z0ZYlq2nYCQg7TeU0kX4MCXZxN5-E8HcYilK0vIlgrfidGUTW8B0_b-QcmmVQ9kYrmFLwmZnjrNMLgRkTCfcXcL1cy2OrlzL-SajmlZf5QUSKpC719OPEtFmRyrcwZi_XbP9AcQjIjnXu6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
هایجک‌های تاریخی بارسلونا از رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/103162" target="_blank">📅 14:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103161">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729f5d60ed.mp4?token=BRaAyuYnH2NsAAqwG34b_WX2YJtk8X7CCJkJ4ZI6UUMQhXuyIg7ocnEQakQcM1-mrw9_0o2aE34FjFqAwmGSB_W-x1jf7TWCNDGmt5A9GIUpXpzmZLQ42IFfqD-UzZDiR231uVU4-LMgINMzwDZFhHEtRAEam7Ymk62E0thmsx9Ep_eC0CxOCDLYi2T9L4XH_3WrPCNYrC-SnLf7RFH22oLOUodzGFwyDpG1vuJs4vZWlQhbwThRGV_uj983ohQz3mYZZMdYM87hCRZlqgqQZUpMUEyhSEskv1bSLwwHjB3XQQPRk3vyu487HliLFSHP4dj4nnT2fxobyYmYAZWfww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729f5d60ed.mp4?token=BRaAyuYnH2NsAAqwG34b_WX2YJtk8X7CCJkJ4ZI6UUMQhXuyIg7ocnEQakQcM1-mrw9_0o2aE34FjFqAwmGSB_W-x1jf7TWCNDGmt5A9GIUpXpzmZLQ42IFfqD-UzZDiR231uVU4-LMgINMzwDZFhHEtRAEam7Ymk62E0thmsx9Ep_eC0CxOCDLYi2T9L4XH_3WrPCNYrC-SnLf7RFH22oLOUodzGFwyDpG1vuJs4vZWlQhbwThRGV_uj983ohQz3mYZZMdYM87hCRZlqgqQZUpMUEyhSEskv1bSLwwHjB3XQQPRk3vyu487HliLFSHP4dj4nnT2fxobyYmYAZWfww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
▶️
یه ویدیو کاربردی برای دوستانی که حین رانندگی قصد دارن ویدیو بگیرن و همزمان موزیک گوش بدن؛ بفرستید برای دوستان ماشین‌سوارتون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/103161" target="_blank">📅 14:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103159">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dmF_DGhb6m5u9AiHvms49l2E7ogfjR62Iu0BSU-KntJagcw2TLSfK9ep2-eV74sVh-4ceF2F3AN2D8W_mHMwzl2iVOEp-SWrNEVKoaNDTKt8FF4rTg4ab1qxk-fI2KFypCyA0QD7kDsn_tBAv76zScKcvwxNj8i0T67y6Q8PSmBBBs23hW9jy_553RgotrFeQ0mizXMs4O359hj4OUDbfwIjadq7eOKmWxACAyHLWIPWMl2Z3qjZ933iqwc-VGzfp4oFlAyKcboVtnWBrmS2I8zysCfPiNnjMgpnrfF_jJjIJpMiNF5UMQO3gBHRv6ub0TRhup4-JBoHZMInaEV5yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TuYxYB757tUjG0Xmy6G3cbGaNeWL76En0z_dcJtL_Zxlq96gSQtDsqYy9ArZ4PKn4Ygk0-gPqKBb-hwtFCizB794C_KrdzINzGaIXHs7E2fSOXDTYbpx5jD0sZ2HM6eaYVr5UEWwZkb7hZntLE54d844_C7b44mN7lFRsBeqHA07rxvaosWD8cgYKzwsePv50L9aKD_O5RHZUN1ujFqq05VHGM_KcnfWVb0lhUEgaxmBrHU8FczAvM77kTo_9iA2dxbFNXeGYvZVNAUbwvzPzSYydSQKfprTh-P-gIIAZw59_GR_IaYF_zl4VgTDyR7yJvp415jvp6yJ-j3etH6jmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🔴
ترکیب منچستر سیتی
🆚
اتلتیکو مادرید در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/103159" target="_blank">📅 14:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103158">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815f97cdbe.mp4?token=lkUllnGBaaePAekI5sonCVzf1_u_4sZgOj_P2W_BQQXGd8TXm98Yt5pLLetPGsdo99nG_Ogzvqj2g9kdn8_Sc5nNZYw9CeHJxV6-fKR2DQZO5LbCtd6bfSefqqcJcd0Onz2RlYOhUAleVTIIgxFRR77Q_n2NTcPRVpABzjyth5-pvhzLXhyS8y6K1C-kA-IgmypImUVD6MNr6yToz_cTz73zh0cobwDcg5EuXYHJHRDnlPbci3KyXvlJ3HEcT9Pw0C604PPgRKaBiOxavvhd0GqVHLcxek2mycTEWYROgLdyFVUJET7_dTu66aymgjusgdd2tq_Q1kz_j_JDaDDc5xavU0MAe045T3zVRlcFIcsmmn-brudsHmu_UhGtJ0hbOrUO8BGLISlNx9y2gVvju10rH6vhgyjTyMMfatOTWpGPjSUyU6I_oZ6_9Tt54cqzB_lE78fUSp1-maBA8WRQ09z5KdSv4V0u9aKU7FgWPa5dC46riLFe2u881F_oBwlUAPgykIh8PrCNpIz8Y6iDH9wnl-4KvHyUbiN9A4y0XJ3iwRutksnJjLepCGLt8atr-bUrclja6IRpmYG2cZsBR3eSq8JLmFEXE1OeoMpjUmFaTj2tTZM1zBUtfobEk2f0PQoPYT-2nZxMzrvEkLjAEicL95RDloW4IHtQIgKZ8I0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815f97cdbe.mp4?token=lkUllnGBaaePAekI5sonCVzf1_u_4sZgOj_P2W_BQQXGd8TXm98Yt5pLLetPGsdo99nG_Ogzvqj2g9kdn8_Sc5nNZYw9CeHJxV6-fKR2DQZO5LbCtd6bfSefqqcJcd0Onz2RlYOhUAleVTIIgxFRR77Q_n2NTcPRVpABzjyth5-pvhzLXhyS8y6K1C-kA-IgmypImUVD6MNr6yToz_cTz73zh0cobwDcg5EuXYHJHRDnlPbci3KyXvlJ3HEcT9Pw0C604PPgRKaBiOxavvhd0GqVHLcxek2mycTEWYROgLdyFVUJET7_dTu66aymgjusgdd2tq_Q1kz_j_JDaDDc5xavU0MAe045T3zVRlcFIcsmmn-brudsHmu_UhGtJ0hbOrUO8BGLISlNx9y2gVvju10rH6vhgyjTyMMfatOTWpGPjSUyU6I_oZ6_9Tt54cqzB_lE78fUSp1-maBA8WRQ09z5KdSv4V0u9aKU7FgWPa5dC46riLFe2u881F_oBwlUAPgykIh8PrCNpIz8Y6iDH9wnl-4KvHyUbiN9A4y0XJ3iwRutksnJjLepCGLt8atr-bUrclja6IRpmYG2cZsBR3eSq8JLmFEXE1OeoMpjUmFaTj2tTZM1zBUtfobEk2f0PQoPYT-2nZxMzrvEkLjAEicL95RDloW4IHtQIgKZ8I0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
⁉️
بهترین گل‌تاریخ فوتبال از نگاه امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/103158" target="_blank">📅 13:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103157">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjuEUCI40KUm3YKL9x27_nTCZDtmQvpXQCinB-ojXwNZpb_nzj3Xlnf6p_vf_2fiCDVgKpn5jiM39FHDVKv0fOvmT_iXAaD2WLYQ2B4FfHKFWs3CoiSeDK9fBNR0804hGFpB1B70Lz8LcLtLLfEaJW8H67ijm7jAflDIUQKX6EGRflTSTsIijnwR-fpWLXs43UWVseHDhdkoYHmsQkZK_HKKKz_vVc-JWfM16tF3INOGZX7S418sIbRr51reywDZrGgnY9-SvT9WIsLwC6WpFLcL-yadLDIAtA-IotCyLQkSNVQ7w_q2Mg7fbRmYaPxMbpL5uidVZIRoGEa0JV4YIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گستون ایدول (خبرنگار آرژانتینی) :
✅
علاقه بارسلونا به جولیان آلوارز همچنان ادامه داره.
❌
آلوارز تمایلی به ادامه حضور در اتلتیکو نداره و احتمالاً دوشنبه با سیمیونه صحبت خواهد کرد.
💸
بارسلونا آماده‌ست تا پیشنهاد خودش رو تا ۱۲۰ میلیون یورو بالا ببره.
⚠️
هنوز معتقدم شانس خوبی وجود داره که او در بارسلونا بازی کنه
📌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/103157" target="_blank">📅 13:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103156">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b2c9a3f73.mp4?token=i7zaqTtm8OQsTm0Y9yvJvbh9XQ9X6_Zxk5qL5JuxDHoL3iyBye-Lw7UnGU_zAWzMwy2tGwNn8B-qaQ0RKSl5tN97UyVdtowqaxB3Kc3SE40Y8g0qnQqmj2CAeSPB2W-qbjH_aL8w-MZ2Gg4VjSNmts5OJAexDXfGBXl109Uq8Q8_4TraEU10UHBjzDlInMX7Rgakzj1yclXUvrd9cUYWuZ7aabFTM9JEcvYouy_b-2j5CDZ4_KKDRVr_xkWC7OnlFL1QlZKH_ngxmio4cSOq7C9rcA4iIW1GeOCqaYdSnbSVkHaMEgCNG0o4f83yZ-VLd1w1emB45ORqfFUUOPIZJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b2c9a3f73.mp4?token=i7zaqTtm8OQsTm0Y9yvJvbh9XQ9X6_Zxk5qL5JuxDHoL3iyBye-Lw7UnGU_zAWzMwy2tGwNn8B-qaQ0RKSl5tN97UyVdtowqaxB3Kc3SE40Y8g0qnQqmj2CAeSPB2W-qbjH_aL8w-MZ2Gg4VjSNmts5OJAexDXfGBXl109Uq8Q8_4TraEU10UHBjzDlInMX7Rgakzj1yclXUvrd9cUYWuZ7aabFTM9JEcvYouy_b-2j5CDZ4_KKDRVr_xkWC7OnlFL1QlZKH_ngxmio4cSOq7C9rcA4iIW1GeOCqaYdSnbSVkHaMEgCNG0o4f83yZ-VLd1w1emB45ORqfFUUOPIZJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
تخریب یکی از ورزشگاه‌های اوکراین پس از حملات اخیر کشور روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/103156" target="_blank">📅 13:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103155">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ha3i2XhziiZ59SnrW8wanlJLalk2cmVpc627fg8o3uDSfZ0YMbjM98Oc-Cs0JJqAovQoKSUDZp_IhXYe2SGg3JfAOmPa0lD5M2ZI8Mu43otZK02WrlnjQDRaT4J9FGiV7nWw95NmzpZJzGaPhNLqBozNM4gohgqKfm3Zkcbf04fm5QEnAoq5N3FiS9QqDLh0dYdnbRBA1wqLAsKeSfUfl0nHij_op3mr9Gh_zEeZaDiNsBLu6pC7Y_IZhTh7jb_tSilSZ92T5OBmRS7wupbAQIVKjuS5a3g0MaiT-8r6Bj-FsIuInK7YufgO93NoX2CUGT4_sanUTDU8uds_gI7lmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دنیل‌مالدینی با عقد قراردادی به کالیاری پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/103155" target="_blank">📅 13:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103154">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMXhNSok93UIaQaEOM_N9mRMoNx52BG0AlpuaDUvvzE_7q_MxE2TaDQVZ2yDzh0DYQdZ5LjuZBMJgbMZ0zSTyqGnWxKHk-GQN7GfqSOVaUpAxWvGqscyTtgEmh895MfzO7R9hP-GRohleGC_IkMmVaSNPByhLApAOE3_TiBKMGxPFhMKoh1hFcT_8ZYH_ssVJuD530UKvohCpIj4EcE-U3WB6QhVXY5Bfd45mh0iWGGhpCLKDFdh5BYUioabKpaeLq2ikP0ZRZQPK_CO2PwF5lp8p--K76XFHY9iTQ-MnreqnmHKZTLj9B26cL9m6NGu1C1yQukKLX5EzQBu--xuKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🤯
🤯
😳
😳
ایران مهد عجایب! یه مرد در طول روز، زیادی به خانمش دستور میداده که براش چای بیاره!
بعد از یه مدت، زنش توی دوران پریودی میزنه به سیم آخر و وقتی مرده میخوابه، قوری رو میکنه توی
کونش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103154" target="_blank">📅 12:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103153">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoJtC48a3himsg4LHQZHLKnHsUu7oIXXs9OhXfF0S6dIKptBCctlSyO-i8ldM3AX_3KOA5szoTBlZ63vEb4OaBzm7b_GS2P-afQrbJoMjkPlh3Wy-DaqvL1irfCNSfNjy7m4omwZoJSG4IZzS3gyVEg-GlTg6RAWE5RgfGlWsqpcb47UvOrCu1mFcCFcZjfmjFPWroJb8_aeFI4MA0Mi7noyGo1tl1bRWDVo0MlkeS_zVgVNx7TNtJB4RG_GnO7p9exHg5h3qGrzBBwDUWwf2ZJ6url1w69LcIYDse8cbK6b_TKJNXFF6p7Snjns6wUdJFtl25R_3G1X8e-SUDgJhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
روزنامه موندو دپورتیوو:
❌
🔻
اظهارات سیمئونه استراتژی بارسلونا را تغییر نمیده. هفته آینده برای مشخص شدن سرنوشت انتقال خولیان آلوارز تعیین‌کننده خواهد بود. اگر خولیان نتواند وضعیتش را حل کند، بارسلونا سراغ پلن B خواهد رفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/103153" target="_blank">📅 12:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103152">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVDp3B_5R5mCIPyxvv1SiOLzIszgtkNgxgY8LDBZSO58AUk_WBWPWuZ0PbP0JAiB-g4NbEljYOvuEf6vLZHaPx4W71RLzxQgRd7W7xvKF5yp9Btu4dbkeARAT8aRf5U4UD43eoH-Dg_1k4P9Nr6Zn2pHqVIjLKthqERpv-abcG9CV4PGFsgESVxLYwSkYSfrGuaHFhg8dIL_PgaLumDv2XOZbq2Erp6m6qxFkWkCAErU3H2B6yg8HkIWMOI77mYh1nKfo_QNuGxXm7Q1vMN5qWOstoEamuNMYMO0M9FcueH7k_SlHthX7AZ5jdRTv1COWVZ6TcFxWVdpXvFrivnRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🔴
خنده‌های حجت‌کریمی و جواد‌نکونام بعد کودتا علیه محمد ربیعی در تبریز
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/103152" target="_blank">📅 12:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103151">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9cB75soBZR3a7wEF1Wd4-V0VFbglnjGiUaHvZknOhB1Md8G8o_bof0SDqNrS0CY8fWWL3LpCXwIKBxDEn2uirCufXg238kDrQPcKYSEySJsAwyCNKCXzx35uW021lnKvduyTB-pZDVmACS8sLNMR3mbhqccfCYGe0kz7bKJDj9FppkKPfyfUVWen-H5n6N3BFvxio5JjmFdpbI-L7qpQt5OwB6zT-eZ2KGUNblHp4N8fuJdpjqYds1MZfK07MvXGEYFpQTiAwabLywf6ROwBKDGe8qtFEXjyt0FRgAd6PBhp_oIzL9DYLLHFf0Xa9M5dADxlnA-MBOpesnxuqt-XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
۱۲ سال از بازی منچستریونایتد و رئال‌مادرید در آمریکا و حضور ۱۰۹.۳۱۸ نفری گذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/103151" target="_blank">📅 12:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103150">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/103150" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
r18
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/103150" target="_blank">📅 12:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103149">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWWx7iWig-cR_mhfrVAXbbx7M9o2Uvcx7Cjhv2PZrO7MZQRgsR3QkzH2SFv0RxcyRZbfJp_V-0c28JX6alQYqe5uEejBWd0DzNiIiE97j5wSsptJZ-ByQdoWAKdAoaz3yYzQRBMUKGnxnexLnShx_E65w0FdrErN9KjL-ZqmOmZh5OpthgAGc8IQY6qAkwvjb739UDN7H82zfv948dWacyAJpvI7EY2VUE5k9XYjIoOxEfDfy8ZF7vBfDJaHoHXy5AgIgDW8-HEmXyhseHP9n_nQBT8O_f73dEWiYzTsE60W2XWFKLEJrXZ1NcfCwSJOiyIliCepa01BrxHaQQ6txA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r18
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/103149" target="_blank">📅 12:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103148">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یکی از جذاب‌ترین دربی‌های سالیان اخیر منچستر و تقابل پپ‌گواردیولا و‌ مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/103148" target="_blank">📅 11:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103147">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eh7M0x--iXl1GVOv0hohUwNktEEww73Tez8gZ7vt4bqVr2ZAemfBZ7UYX2fahK3rq_UafUCb-4L7_FFJ3Oz3BN-9-MM5a2-W2l7_fQS-bNyy3Hgl2_o8NomVBhbldVnBF2fN-olag5OU1yvA3Zke7lgWQTddR3xoa7WLwHwa8Mk-LadbzHgcmoMFdJUAe4gs5mTNCCy-lcOH_rA6ow3TQnglXpUv9kCwvA0mx2-zLEFr5v7gDaQDXqVBJ0GgoFntQMF0olzq3YtxotT9jWTOZTCubN7xq0gb4d49H2yEi9lMN3uMOvumtDTqZCaN18cTp-MtqQ-712S2QNE_wsMHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
فده والورده:
من انتظار نداشتم مورینیو این‌طور باشه. او خیلی به ما نزدیکه. گاهی اوقات سخت‌‌گیره، اما فکر میکنم همین میتونه باعث پیشرفت ما بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/103147" target="_blank">📅 11:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103146">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68c18fc924.mp4?token=Vb-WQIzb7gSQP-BDwePMON-iu7gcd4R3JHkeVJAay550CGvm-qjxOtMLF7txsRzwrX8FqPhtEfkmxePoaTPZ94xnJ_6nne3uDRfoffyMcfCmiBqr3xO4JKDBnXELQJQGJdxs5Ic5qU64DUFVclsPLFsq1T5fViRz7I2u8qd2cTURq-HemKUdn7ejdo-5j_Hc_K0HG05MSIfUp4XkgC6eZC3jNU9R5QmSctA5yyc0-vwOFjpGHFlVMIH2DLATS1JvO7B2ydTkehDBnii3cBEtKM5PoaV1KaQXjhLivIyH4gF5FHgCP4iCovLBgqD5XRA0BhL58LP_ZRpWYgQRxa2leQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68c18fc924.mp4?token=Vb-WQIzb7gSQP-BDwePMON-iu7gcd4R3JHkeVJAay550CGvm-qjxOtMLF7txsRzwrX8FqPhtEfkmxePoaTPZ94xnJ_6nne3uDRfoffyMcfCmiBqr3xO4JKDBnXELQJQGJdxs5Ic5qU64DUFVclsPLFsq1T5fViRz7I2u8qd2cTURq-HemKUdn7ejdo-5j_Hc_K0HG05MSIfUp4XkgC6eZC3jNU9R5QmSctA5yyc0-vwOFjpGHFlVMIH2DLATS1JvO7B2ydTkehDBnii3cBEtKM5PoaV1KaQXjhLivIyH4gF5FHgCP4iCovLBgqD5XRA0BhL58LP_ZRpWYgQRxa2leQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اَبَر قهرمانی وفادار به عشقش فوتبال
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/103146" target="_blank">📅 11:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103145">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2bfa87a9.mp4?token=t7LdwZTQeNdGAI4OQG_KAVJNX-cqSvlCvFXvM9B_iXyu9F7TsTNJkQ823fBnxGm4gD1Wg1ofg8h4GaipWr7-6Yfw5zhF7Hzj7jZvRp7LclCgvNqE3il7CcDYj4K9rqJMai3gNWyzTMy3CvI5rhuSh4TpSEYh7cUHi_VSlhUxE_HyTKHGfqdDHS5NVWvkiPj9eWSJhcm-AsJN-csjmrLacoaEMx_aoZSNStAGDH0Z--10VWxL0cQsw260WvnX8qlXlNuy_TzG-XDgE1y7LctmjPgeknJRO_Tu99Z13HSXwaE5bwCTbDnw-miGTyy9PV91Z7gclLWl2GcUOMOHfdfLsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2bfa87a9.mp4?token=t7LdwZTQeNdGAI4OQG_KAVJNX-cqSvlCvFXvM9B_iXyu9F7TsTNJkQ823fBnxGm4gD1Wg1ofg8h4GaipWr7-6Yfw5zhF7Hzj7jZvRp7LclCgvNqE3il7CcDYj4K9rqJMai3gNWyzTMy3CvI5rhuSh4TpSEYh7cUHi_VSlhUxE_HyTKHGfqdDHS5NVWvkiPj9eWSJhcm-AsJN-csjmrLacoaEMx_aoZSNStAGDH0Z--10VWxL0cQsw260WvnX8qlXlNuy_TzG-XDgE1y7LctmjPgeknJRO_Tu99Z13HSXwaE5bwCTbDnw-miGTyy9PV91Z7gclLWl2GcUOMOHfdfLsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
والیبالیست های بانو رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103145" target="_blank">📅 11:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103144">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqSgYhnAaSVIN-4RQobCHqw5sbzDefvignjHd9PfchZL5LK-x-MTpTCbC1T4ZNmQ7Vh0nEqA2iV872WfStTqhz7gNUJnYjaNN2D0jEVyvKcMoHFSXcNR0IT8x6Tgt3s05CXssQPjM8fdI24e8iI9i0_PXFUdVeAFuFAg1KXyXgK-2Y02SlWwTcZgIDfBiqI62ICISXPIbhw6hKllvWv0Fe2L_I1fuKloAK8018qQ6v1MtuWcTfHmJe9saZ38VmhQS-F04mnCw9PbpuTOhjS5Al9TecdFKSUHCMRN6BVGcsJsP3xmGACX1UhrhxzrjiI3yE_zzaK0cUSxcamTEh9yCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اینزاگی عشق میلانی‌ها امروز 53 ساله شد.
🔻
فلیپو اینزاگی انقدر تو دوران بازیش روی خط آفساید زندگی میکرد که عملاً آمار افسانه‌ای داره؛ تو کل دوران سری آ 300+ بازی انجام داده که اینزاگی دقیقاً 368 بار آفساید گرفت! از 125 گل رسمی اینزاگی در سری آ، خیلی‌ها معتقدند اگه VAR اون موقع بود، حداقل 30-40 تاش مردود می‌شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/103144" target="_blank">📅 10:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103143">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8debb5a7.mp4?token=rGuGVkXgEx5R6KdaGNya0gKMbU99IDH0HRqI3YDMilrkuzalHfA2ViyRXcLH12OMPzYbZKQDrSmfgqdPgYL_rHyJynIgGNdu8lPgXMJZPw1BO5HzCtL8-6DaXh399970ni9CuiX5vLPdwY9Q3KSnsxOy0KA6dy5NkraS4k-uy_eeJ6ww1gk_G9QssbF8yrWixz3N3FLT_QhEj3_cQqF-nZZPjYpPhwdwLWUmENMN1Qxbz4YNpABnzc0qyIuCbzgXHfJZQ46l6UPYOaU5VbdHyYHzug1mnOEmJTpOzoNK9qjMd7bMHt_tFgJS-OEetqhX4xiFjHdv4tFXoHJw6S_X2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8debb5a7.mp4?token=rGuGVkXgEx5R6KdaGNya0gKMbU99IDH0HRqI3YDMilrkuzalHfA2ViyRXcLH12OMPzYbZKQDrSmfgqdPgYL_rHyJynIgGNdu8lPgXMJZPw1BO5HzCtL8-6DaXh399970ni9CuiX5vLPdwY9Q3KSnsxOy0KA6dy5NkraS4k-uy_eeJ6ww1gk_G9QssbF8yrWixz3N3FLT_QhEj3_cQqF-nZZPjYpPhwdwLWUmENMN1Qxbz4YNpABnzc0qyIuCbzgXHfJZQ46l6UPYOaU5VbdHyYHzug1mnOEmJTpOzoNK9qjMd7bMHt_tFgJS-OEetqhX4xiFjHdv4tFXoHJw6S_X2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شغل لذت بخشیه واقعا این فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/103143" target="_blank">📅 10:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103142">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cccf30963.mp4?token=nvEmcuQ1X6rKmCA0SK_lyn1vstZC9xCo3StVhpp54GKUTFhQzBghSfF2ojWzpAJ5Kt3uY7tQnaWIKx7GjS93gHREIBj806Lsaj1yxT6CKO6_oAhUUlCFiR6WT26bVyv-0RoHDyDlFr9srzDSYLQXlPe8T01_RzWyb_93-3shzFC4S8gARigNVlbki85VRWpVPZt3COYpFCA-kvgjafuVYYhuTXhsnhe9I_WaGwdQjxB9Mi1Mgf6p30HYWAsyQdSaHjYT6jTiTPB37r5OT8_JkYwv2o-WZ6hiWuGTOrqS5aFFORM11gPHJfsSr8Dhft-NfWLOgoyYiyjJmbfXjyy1ioi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cccf30963.mp4?token=nvEmcuQ1X6rKmCA0SK_lyn1vstZC9xCo3StVhpp54GKUTFhQzBghSfF2ojWzpAJ5Kt3uY7tQnaWIKx7GjS93gHREIBj806Lsaj1yxT6CKO6_oAhUUlCFiR6WT26bVyv-0RoHDyDlFr9srzDSYLQXlPe8T01_RzWyb_93-3shzFC4S8gARigNVlbki85VRWpVPZt3COYpFCA-kvgjafuVYYhuTXhsnhe9I_WaGwdQjxB9Mi1Mgf6p30HYWAsyQdSaHjYT6jTiTPB37r5OT8_JkYwv2o-WZ6hiWuGTOrqS5aFFORM11gPHJfsSr8Dhft-NfWLOgoyYiyjJmbfXjyy1ioi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🪄
هنر جذاب و تماشایی زین‌الدین زیدان در کنترل توپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/103142" target="_blank">📅 10:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103141">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP28gQaDdZiev5HO50MyBfHI9GghEJu3Cwf4-XBzS65c5sKSBu8-V4wvxAi3E5uixg1hPj3TUQvm4vzT8Ldtj-tmhgnfM_A4RCo7Of24Yze56jHBwFD3IZDivuJvOLeeag93D-BymXVN5tVZ1cwS3eJvMNZKBTudYuxof72mBlXcdO1L0QQ9mdNjmspsDOxfKvQdYgqSBIJtwie-0HOzhiLfim1YoBf35GQAksR4VmjmF4lRYnL-xb-_V3MKsA2_n2OV8IW_3S11FAenW6tTOt9mywG9OGEP6zUzG5mmqk5Z0t6QCqguSLhj5TOcRu_QgLBU6-8ls4VoNQxeP3CnLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فابریزیو رومانو: رونالد آرائوخو امروز راهی مرسی‌ساید میشه تا تست‌های پزشکی خودشو با لیورپول انجام بده.
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103141" target="_blank">📅 10:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103140">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ox7Rps37cCzTTzmB2HGxj4z0jDRr38sg6gT9MiTYkoorA-TeyUrDzcuP0Gs4jeAbh60s-lhkgPXKWRFkQibO5EJEzcsRfeJzts8EDyoeLW1HEzS0vIlS7VsHV8zoulMXbee2pntmpfPmfAJIWXmzd09wrEbGwoDflF2eW9DH3ULLhY4THy_nnwdK0Odfe70Ddg3ztNsaOeSGD5sHkVEmqm449H7XjkGEyDhiBB2r7iOZ7oMpN5kCLc97ZBo3Tx0rldSJSTMtgDA7B2FXDbAYzo-LUow_Cy9oBOVBGSrr7NN9SPCjNEQ-MPGDc-z4lML6nThvnAabec4T95kcRmPhRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🔴
آموریم با میلان هنوز تو بازی‌های پیش‌فصل هیچ بردی نداشته! حریف بعدی میلان منچستره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103140" target="_blank">📅 09:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103139">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رقص معروف لامین‌یامال سوژه عروسی‌ها شده
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103139" target="_blank">📅 09:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103138">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVGkKNoHEtUcY7434a3uQsnWmv2FR4XjFxO7cp1e143CJchwQk-FUINNo153fszsQjEAKDdQsStAZiXdRFbZw__nPRaCl4ouCrP_Z2AxLpv-16rZiaDEiz5e5ATiWv-xckM4uOjeN64xchU-tdEe4d5CePtOeXDkgOTMXnXpv5cN5fHdw3TfK2Z5vjTJnM1trb1s269kjv8pANHiOU430hPJUiZwaY5J_-m4A-9eimz7bAkgbV16jO8hfdK-dsB_wBiWSUv_tE5A2xiBA3Qj3Z9AAZz0gJtjxa4eAwWe547chM3RPurG0GJSMTQylmEwBTWMV1lFaHdGja_jCGsCVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔴
#فوووووری
؛ جواد نکونام به عنوان سرمربی جدید تراکتور انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/103138" target="_blank">📅 09:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103137">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5Oen7LUFCimZFCchF2ZGr4845jbDI04ZIyDxsftFMUDe8s0FbzEfWFUU6m1IYe0yCGMHm3lBZ2MXYX-U1OAST2z_10QLMnHt6ns333BI0VRR0Tudq968On0IX5AQPJ6BPU4vQaY9XsYxyFpScsOEGVJV-hObJsiDKnJIfjGdjozMBf3G2Al48rTPtUF-XPl0nvnXG6BWfuqSstVpDDy7BhH7J6aV5cH9kut7qtGrq_lVbO7WI-UB0lMEqVFsMolM2WlQplOoiQ2obRlsYuHd2QYhto_Net5CNsGxMW5TxqvSVlp6O6prfsaDsmeilXoTr9lrJykc76dfA-Jk5HBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💥
هرگز فراموش نکنید که لوئیس سوارز چگونه فصل ۲۰۱۵/۱۶ را با شگفت‌انگیزترین شکل به پایان رساند
🤯
🔥
⚽
⚽
⚽
⚽
🅰️
🅰️
🅰️
vs Deportivo de La Coruña
⚽
⚽
⚽
⚽
vs Sporting Gijon
⚽️
⚽
vs Real Betis
⚽
⚽
🅰️
vs Espanyol
⚽
⚽
⚽
vs Granada
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103137" target="_blank">📅 09:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103136">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/730562ee98.mp4?token=jgYzSq5qegvyJiMTHUKBeSKF9lll-8lZixd5G7TgukDyQjaViHYwHbEV7Qruvss6PJj_UkNTiZD8w0WljMswhuVtBDJAq-_bT0EIL5u5-Cg9zeyLEgqKSL2dCknuSsBLggPEmo7Ybz1VXF6HmwlNKwvkeTl0SE_x_vQsH1nxtwMJ4NASXjgnq5ZPIvLebJt1h64_0Mp6POEaI1j6WfaUUjAbQRyX9ffNXn0aJ_JPnC5pWRPNpfTaRpr5am-11u_ATuvXblt-5koKm26huHPZMRsrIRFEaFWcQml07CRkxC-4RTwC12a-XUUlqZgQ9WwH1TyVascrIpFaZ9WlIW_oRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/730562ee98.mp4?token=jgYzSq5qegvyJiMTHUKBeSKF9lll-8lZixd5G7TgukDyQjaViHYwHbEV7Qruvss6PJj_UkNTiZD8w0WljMswhuVtBDJAq-_bT0EIL5u5-Cg9zeyLEgqKSL2dCknuSsBLggPEmo7Ybz1VXF6HmwlNKwvkeTl0SE_x_vQsH1nxtwMJ4NASXjgnq5ZPIvLebJt1h64_0Mp6POEaI1j6WfaUUjAbQRyX9ffNXn0aJ_JPnC5pWRPNpfTaRpr5am-11u_ATuvXblt-5koKm26huHPZMRsrIRFEaFWcQml07CRkxC-4RTwC12a-XUUlqZgQ9WwH1TyVascrIpFaZ9WlIW_oRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نوشاد عالمیان یه سبک زندگیه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103136" target="_blank">📅 09:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103135">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZAc_7gm6-hMBPYaMaUPkXAE1buAeiOqBpCWiOjiqwiunCRcOgaWvIllZ5Dq95qosA0vOv2Q_UnwZNSzmL5jos-jd7vf-eDiLp6R7EnxzZgNwpqp7nfi9xsAfmx7gL9udPGX4zpU_Q4W_Ht_STOPhWJY9iSSprws66v8Umv6auKrCYh1UzfuQu1UB3uTtHj-R9jBqZFaeoMSE7IObkLCE3GlGhSnk-hDK6tj-YV3NXcjV2lEQHQFMMrqPuBKyWjg1Lo9YAbrKBdgtvJEZLBUVD-yuqYpdZos_qctcE5OqwDpLLmdS_CEvCEPNBTXY_mLBT9UUbL_qXC0QCcBXd3BoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهره مسی هنگام ورود به روزاریو
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/103135" target="_blank">📅 07:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103134">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee87aed7d0.mp4?token=ENQ0NbyMzHitjQ1a4WbU783EDtP9-m_vNQeWFB2Ld-Z_JL-ZfD1KSYTMLj3ope3tAnhBkX8ArEl9_S0RW_6PcWgfVmcT97atqyObzn2gogncFfvuPXkfjWbAbF--L438TXq7DFLC25sYt_FOTou8JSykye0NRaCfMbHAqJdKJMo0azCM2ngs0gyaKLKjT6tTHs8eDa9E2CMDz-ftIAV818o4FagyHiqyJAWqhMZTSRhpdsfLb9MejNg6JzICPt0U5Ea2zL3gEghUqbYGqrDMriuIbdjU7N7hH679R0s7ngMnf7Zlx9Eg5zX0z2R_OhX9gx9RCJBJzJ14O7o-dJc_Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee87aed7d0.mp4?token=ENQ0NbyMzHitjQ1a4WbU783EDtP9-m_vNQeWFB2Ld-Z_JL-ZfD1KSYTMLj3ope3tAnhBkX8ArEl9_S0RW_6PcWgfVmcT97atqyObzn2gogncFfvuPXkfjWbAbF--L438TXq7DFLC25sYt_FOTou8JSykye0NRaCfMbHAqJdKJMo0azCM2ngs0gyaKLKjT6tTHs8eDa9E2CMDz-ftIAV818o4FagyHiqyJAWqhMZTSRhpdsfLb9MejNg6JzICPt0U5Ea2zL3gEghUqbYGqrDMriuIbdjU7N7hH679R0s7ngMnf7Zlx9Eg5zX0z2R_OhX9gx9RCJBJzJ14O7o-dJc_Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رودریگو دی پائول، گل خودشو با پوشیدن پیراهن مسی جشن گرفت. لئو مسی به دلیل فوت پدرش، خورخه مسی، در این مسابقه حضور نداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/103134" target="_blank">📅 07:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103133">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0UUOS1E1MYciPBifaJ32Idk0haLWi0_joOl5uvQ2SHGltr3G0JOxkEfO2O2EAqHb4HJm7h1o0Y3RcGLlnubqNcGIMhcPu3IgBVtin9lOS8Cpc8wFWNlMRBDg9_1_QM3KUqlOdXuR-q7EabYgbHqb7zvkASvITHyx2O1Oq5gmEDq0xqVRLQ1vgmwPqD7TwB2kbq1NePdKsdYaAWLfEaelVioE1UkUwMsQw8px9Z0MwuRjQsl0qmq2NXsJXHbT_a_6r8tUiZineXE_6MHpIOX6HhPL2Us4l5ztESSiei2AsXW_lN23_TEVhPoXJpbVzZU2z0IZOAcX5eKDfxTlSfyFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری اینستاگرامی لامین‌یامال
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/103133" target="_blank">📅 01:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103132">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d3ae9a81.mp4?token=pdmqY2M6Yv5gvxMHdN0lm8DkGULgDrH1SZfhBHfoF8bqOhx7KGZghIbHq0QHho21QZXLz5DWAmn_YHJBtwlVlaby-uReHTDm9QPQ-auAHidXHPujbFyLUsWiFFsVOcSOvx5vBkO5rrjV-YHLf8eHR0TKGTfZ1tjTibgUNDPXJ1_9mNn0AkW7P4XEW9XU0vpecuJ_UqJCr43vlIQ16nu_w8p-cYzZ16bOH4ZezSnEwOnhUYJ6BJi2m1Thc2ilMAFFG3i7vmAliXzQZIGx8--dvMDel1woOjQD2plusPkMOEfxT_rIZaLzUTLoW7jxesPlB309nKTIZvvm7URDbCjqNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d3ae9a81.mp4?token=pdmqY2M6Yv5gvxMHdN0lm8DkGULgDrH1SZfhBHfoF8bqOhx7KGZghIbHq0QHho21QZXLz5DWAmn_YHJBtwlVlaby-uReHTDm9QPQ-auAHidXHPujbFyLUsWiFFsVOcSOvx5vBkO5rrjV-YHLf8eHR0TKGTfZ1tjTibgUNDPXJ1_9mNn0AkW7P4XEW9XU0vpecuJ_UqJCr43vlIQ16nu_w8p-cYzZ16bOH4ZezSnEwOnhUYJ6BJi2m1Thc2ilMAFFG3i7vmAliXzQZIGx8--dvMDel1woOjQD2plusPkMOEfxT_rIZaLzUTLoW7jxesPlB309nKTIZvvm7URDbCjqNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
یه اصفهانی که قرار بوده برقشون ۵ عصر قطع بشه و نشده،‌ زنگ میزنه اداره برق یادآوری کنه که در ادامه این اتفاق فوق پاره‌کننده میفته
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/103132" target="_blank">📅 01:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103131">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKfxT6vV-GmHWLjZferjKrjyFYbFcBYMHW-PFeNDovxyrvbJ4bNfQJv-vCCw71cVuV3mg76LQqf0kCBMj4jjoJxh1p3PCCyAcrtuBbzuWPS1u3E-x9f0AjB8ubaje-fg_5v0aZnmI6VyM4VVMpWTKreJEFGoLichUgZIk_OfMLCE8BeHnOna8ASgF5mamj9ANOVZWZVED5K4G5KUWAUl-QBrLaZe3-GGqs_xs5GmVHRtnE--0Xpy6Fi4o2A2D05pi1HKnY6zGEE2jgwcQGQ5U5T1ASseqOOk__GhSBuzVk3oUj3vsepTzF4p25S4oCvcSfMVRbXKRmE12HCuGrrCJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیو فیس و این حرفا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/103131" target="_blank">📅 00:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103130">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWZnRL3gox-ROlMyeLHPwXtTKPopugNRAejdQ3Dy9Lr12lLoXbHFCyNBZvWdtSmsqxO2H_FbJBL0hisSpmUD5bkYO5Dl6RBXGdruLisDfJHMwDSy3DMvz44ZaA0w2SXYrDinSnBUXkYfSeyLHe2JLHnsvA5voWK46CPlQTeW8KvEgOhAmcFNnVPJHwoo1cMNWHFAx6Y_2gfgAwv7TJqRj5pYrkTnhhF6oL0G2nCpNRfnO8XxRbOPovpIYv0cVk2GfEcRNZSodzI2BT24RWcvVzTFUbTCe1n3-x5T07lde8-IIrao6NbgnCrcPhY4Yn0C0OxtAd8QlmJ1Q8yVj4FJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🥶
🥶
👀
فلیک‌حسابی کلش کیریه که اولین جام فصلشو از دست داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/103130" target="_blank">📅 00:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103129">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6da2c1528c.mp4?token=HO9hgcCm84JMSPiVPBDQ3fbb_bHPRCo_H7gaZtagnq3yZdrMDhwMHJdRHLkuvG64rbAzM8tZMrZwFlpnxeOz_uqEFPZsP9vzCGKNSJN4Ae1mqEKvE5SeTOO7Q_B6wlm6I5--9H5u3zVytyDShD4cA8I0inQNSkuFAtEj4m_AbwaQHNT2Z1Kn7arEoDDWMZ08Ej2YhfVjfiT1xKV759_Ypdwgzy-lXT60DOtSaKJmVvcWwcdDA1ieOfvneUwEl_2TUvInGl-cLtRzkhg7S0DcGTGZzQ-zgzObZPOE0_EVNGgw10b4oF0O5j8PpljSevxOLf6YUGi1sTidpNnX6UXW2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6da2c1528c.mp4?token=HO9hgcCm84JMSPiVPBDQ3fbb_bHPRCo_H7gaZtagnq3yZdrMDhwMHJdRHLkuvG64rbAzM8tZMrZwFlpnxeOz_uqEFPZsP9vzCGKNSJN4Ae1mqEKvE5SeTOO7Q_B6wlm6I5--9H5u3zVytyDShD4cA8I0inQNSkuFAtEj4m_AbwaQHNT2Z1Kn7arEoDDWMZ08Ej2YhfVjfiT1xKV759_Ypdwgzy-lXT60DOtSaKJmVvcWwcdDA1ieOfvneUwEl_2TUvInGl-cLtRzkhg7S0DcGTGZzQ-zgzObZPOE0_EVNGgw10b4oF0O5j8PpljSevxOLf6YUGi1sTidpNnX6UXW2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
تک‌گل تیم اودینزه به بارسلونا
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/103129" target="_blank">📅 00:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103128">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
📊
🙂
جدول تورنمنت سه‌جانبه اودینزه، بارسلونا و ناتینگهام فارست؛ دیدار فینال لحظاتی دیگه بین بارسا و اودینزه آغاز میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/103128" target="_blank">📅 00:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103127">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/019d8fa87d.mp4?token=Qsg7Ngu8wwHhnypeypTFBL1zR8ZaSf6vIcp847NiBg0fDka93UyiVo7S-FBpWO9fLLNJgnc7AwZ2ceA6J9cLxNQwJbUNX-By-rEqXHbxKO733DSTvmyyoI2SWhnn-DbBy_jmAzjzXv_kwSbmfGNk6g6vIWeIDxcKtok6rNtKGLpzm4VqXbbBI_zenoInovcBA_o5tcaiubAu-L8CGJJzWV1H1mlpCcQiqvtauFNPir0j-mK3EAaDd-JPdT05JhIg7k5kMADlUdnMz_i5BYDh7Vni_ZWVuqLnvzKC62jjfF44lmnw944BsM3cOS15P4hMM9eo_M5q8stoIexY_s00_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/019d8fa87d.mp4?token=Qsg7Ngu8wwHhnypeypTFBL1zR8ZaSf6vIcp847NiBg0fDka93UyiVo7S-FBpWO9fLLNJgnc7AwZ2ceA6J9cLxNQwJbUNX-By-rEqXHbxKO733DSTvmyyoI2SWhnn-DbBy_jmAzjzXv_kwSbmfGNk6g6vIWeIDxcKtok6rNtKGLpzm4VqXbbBI_zenoInovcBA_o5tcaiubAu-L8CGJJzWV1H1mlpCcQiqvtauFNPir0j-mK3EAaDd-JPdT05JhIg7k5kMADlUdnMz_i5BYDh7Vni_ZWVuqLnvzKC62jjfF44lmnw944BsM3cOS15P4hMM9eo_M5q8stoIexY_s00_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویری از مراسم ختم خورخه‌مسی
🥸
😔
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/103127" target="_blank">📅 00:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103126">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-release.apk</div>
  <div class="tg-doc-extra">4.5 MB</div>
</div>
<a href="https://t.me/Futball180TV/103126" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎲
همین امشب با اولین شارژ
🤩
🤩
🤩
درصد شارژ بیشتر بگیر
همین الان شانست رو با موجودی اضافی امتحان کن حتما بزنده میشی
👌
👇🏻
👇🏻
🌐
Telegram
🎲
🌐
winro.io
🎲</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103126" target="_blank">📅 00:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103125">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1AKdJGc0pPAgxiHR3UlapDs2wtgzn0VnEG2K1oHNQ4d3SYt21wcBLUc_nLJJV0_4Th2l9yvaQHfg1_5zJi_-VYI7XMlWCS5pwuFjkopw5j2j3DV7OWiN3UQ5jupkAs6FPNLCdUNI5GkEm0gGQf982gd6fTdhcVv2yvE4s-uz7yqjgcEU60WrfOkFiVKo_ohTXu8HDclDrQyjdAv7AiDpoJdbFDHfckdaei1kU0EoSpF4kHvKo4sIGAOlfsRy8zt9XVa4EInnXXNW0nUx-sgWvAkAPWaFhATpiqlEH7ff-j08HPUoCzeo1agoAl4J2cM9iNgDuZ4fz3j8OsIO3YCPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
همین حالا موجودیتو
🤩
برابر کن
❌
☑️
۲/۵ میلیون شارژ کن ۱۰ میلیون شارژ شو
✅
برای اولین واریز تا 15 شهریور ،
0️⃣
0️⃣
3️⃣
درصد بیشتر در وینرو شارژ شو
🎁
✅
به ازای هر واریز در وینرو به ترتیب 300 ، 150 ، 75 درصد بیشتر شارژ شوید
.
🔊
با شارژ اضافی بدون ریسک بازی کن سرمایتو چند برابر کن
⚡️
🎲
ثبت نام آسان و سریع کلیک کنید
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا a17
🌟
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/103125" target="_blank">📅 00:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103123">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuujFo94t6cgMEjgR5xHUw_DBUcS6sa14d9M4hYEwRWvu_ViW9pMqMo89U8j_hA1sQ2xzSXvkoqVlAJlbvCgIcJFizd6LDWbsq4XqiSq0MbK6e1M8fLoJaeZRAn_I6v9KfLa09yDv8KCFQvJlGjKdrmVRoB6snWOuGYRvg-21AiTNwvaLtH4H_JsCQdSXkXQi8tS3SCZwmS20Tfq0ulnWFyaQhxB-cX-X_aFXZgOBRCdMDQQ208tzMLYlCS0dCw4ipyuAHkYf-oCGgCidlEhvQnL5_rn9qOh7v80af9UozkQBTP0V2Nd3xth96NfTapuH01dbaPE6rbXPLYEHk0KIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5e8a9ce1b.mp4?token=IA9lKw8vpZzB0F-b1wWMYPJOQlnqfJnDHsWhyJHtC-tSmlK7qQ0aiQtiMy5GdWg9WlHzGepjKQ4bImFcDUP52RZJTJI_jdBQ21710h2TQvOgbxFVSSLge5RUz__zAb6_Eo6rv8l1PuLXFzkfcwVPvC19Lu17yY4IJt-glnKr8YjdPj8fdUV7_6MqC8LUP9VvOF0I8CIESsqnv-ywxTpO-QocPpdKRbphpeu3lhikQFm6Tx2VibbpK1iy9zaAxmG-v2wP3pDReZ0v301sBqlha9_M6-BOQ3VNA3J3XUAnsRmWP7GcPQrfZQqkUlsRc5Ax3F2gaLv1VphMM13DvRqG5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5e8a9ce1b.mp4?token=IA9lKw8vpZzB0F-b1wWMYPJOQlnqfJnDHsWhyJHtC-tSmlK7qQ0aiQtiMy5GdWg9WlHzGepjKQ4bImFcDUP52RZJTJI_jdBQ21710h2TQvOgbxFVSSLge5RUz__zAb6_Eo6rv8l1PuLXFzkfcwVPvC19Lu17yY4IJt-glnKr8YjdPj8fdUV7_6MqC8LUP9VvOF0I8CIESsqnv-ywxTpO-QocPpdKRbphpeu3lhikQFm6Tx2VibbpK1iy9zaAxmG-v2wP3pDReZ0v301sBqlha9_M6-BOQ3VNA3J3XUAnsRmWP7GcPQrfZQqkUlsRc5Ax3F2gaLv1VphMM13DvRqG5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمیدرضا رجب زاده یکی از مداح های حکومتی بوده که چند هفته پیش به قتل می‌رسه، حالا یه کانال تلگرامی مدعی شده اونا این قتل رو انجام دادن دلیلشون هم اینه بوده که این مداح تو دی‌ماه جز نیرو های سرکوبگر بوده و به سمت مردم تیر می‌زده
ویدیوی قتل که قلبشو از سینش در میارن و رو صورتش خودارضایی می‌کنند رو هم منتشر کردند و بعد برای خونوادش فرستادن؛ چند ساعت پیش هم اعلام شد که قاتلین دستگیر شدند
🔞
مشاهده‌ی ویدیوی اول
⚠️
⚠️
مشاهده‌ی ویدیوی دوم
🔞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/103123" target="_blank">📅 00:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103122">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kt_Mitho2r0THUMulHSFsQOtp1Jic9U8FHcQ9L1kAX2cNAiwSjzgPXhR9fG5gUF9FapxAjT4CnG7EFuHvLwryCaHlual2eTW0XFNwrx6mYRs6_6v5a4-ugfTGQNS6X4gJYRqyNj_iG1uG_SyXCkt9rJDE9wrinZRgR-Jc_WyHZIBLpriGZ5Kl5K_Oanp8YQrj6Ju2meIseGODktBRLHcmMwljBbIOdeRX4d6QFveDg4YGu3ZvH3PAu03edLoPnAS8WWOW8kTpLopb4ug6iNnyHPP_JrHmd2IVx5XkDhEGKq-j8XZNfbHtbJ3vChYXVwEs9ZIExECoT8Sx6t_lyf0aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلات رشفورد که حسابی داره بهش خوش میگذره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/103122" target="_blank">📅 00:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103120">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J2YvYN_1p2-niMloYFXvlws16qSQHAoiCkn4-uthTwFuD6mUJw-wCDlFYm_vbsNnewgMhCCs5x18sMUMStg24AUNxZWRrj35d9IhD7rFEaB_46PWj0rsrWDyQrpMMfnvv89K7Dpx-79c-XJ6_jrUQ0gcaSqP7uhtopHGcYYPfXRKZtZDAxD3IGRi69NnaVrpwJycQugEFsMR362_gjk-b7ZtVON5IVgvjHJgcP1QxKTQuhtZYCepl-5JD_2oSWl1XniLs-Eh79Cet56WAt-ci9jl1_ZEMybpwILYvR_RGpdoJ2Nxf9EU89kwfYdSKjwbHcK6W6wGOPxqLOq9BwzAsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c-72relM17ZHmremCcAtNymIH3IVXJqjQSAJDSl7EconPnyTFoiJEHaIYVEAoUs8HcuAgAW_2ucUFWGUqkrY9OecP5wopHnEQ0UWNXyHXx32WpdzemxyasxWom2t_KS_zG69GI52_6ANwD2rOOAOfiHyEezFyUVNGpdaOglkx2nwZmEN3eYn5apBrGF4fuWTLacE38ENDOcyWqruvk4O_KAAzsmiRA64jZR9Hvg7vDRYZlLVbhdIh4t03EO0jnb0d0kI-gDaidxzMiaURPAxkEFoLyzs2pgDaJb_K89qX1RHV7RxHM-Nfn70G01NrqakqJBJHdWspe1xfW4g2c4X3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
گفته می‌شود فران تورس تحت فشار دوست‌دخترش برای پیوستن به پاری‌سن‌ژرمن متقاعد شده است. پاری‌سن‌ژرمن پیشنهاد رسمی خود را ارائه کرده و حالا همه‌چیز به پاسخ بارسلونا بستگی دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/103120" target="_blank">📅 23:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103119">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/feOIBCy8kwFzvyOd8ocYA9ILLjP3mxxKBN6rSfe4uZnd6AIDqc4pdfpVH1dsZ4wHKEm8KgkD4N4yWU5I7YsgK-nLEzZ_aYzfhvJImZz9URqoNIELcXrwjmSxb_PuSnthlXh8_ijxVTO_FbyRcdlQpq1V5VxWYmfMphCZYdes3SUJ6w8lo-KCGXWlai3PYQ_NvP-0VfIzt6Ai4rpUdHvYBcA36A0qfDcjx1QhGy9PWTu3bc7sJKaTW_gRLMk4DpiM6RsO2iYFtJcnXgRI1RxQyWbEwIcb5b_DSsNNx_SYrvFxQuoOnB9uqzMYD6_plCrL7p18jY1hkpilFitNkGpEAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🙂
جدول تورنمنت سه‌جانبه اودینزه، بارسلونا و ناتینگهام فارست؛ دیدار فینال لحظاتی دیگه بین بارسا و اودینزه آغاز میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/103119" target="_blank">📅 23:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103118">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAKjY-IUDpaOh-87XU-AuFdIrhWtchsx6v8NPiytERH1E0EvytbbSpydYqyTvbOrqXHhnf2J2jaaxGEeGPMENQLzZ1jiSGbRxyCR8Ik245OI_Un3Dce4yGoAdFe1WoNtQIJQpWwQf40B4BymoShuV2epkoNhrQF2I040lxi7-jrSdfQcch92RVz4oDB60PFvWpOUclFqClI-CJUZmmReArML-f_EiIyVSY8DkDng7IlUC9u1PzwxbmLktWZve1DFasRuTjZYsd5SebLM9w1H2b7tj5qbW7rSF9qf6m3xdZoCquax5YLRRz1ifJSitk9TD2W4hP86lsdy1FV74OYTKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری تسلیت مارادونا برای مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/103118" target="_blank">📅 23:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103117">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oq5XOoMwGkARI6ULhSgw04SSXGl92cUQNBTWVwWqSLIBna6wsUvHu5OdQs1Aaeb5JJK1si003rVAe518aFYkb9ORk0VPLwszlXrsZXGeG3tfHR6seAqTkrL6h8iNEQ_HTufy7x5TTGqeKwli7yew83rYOz9Qv-aEPKqWVUPOmSNvpfj751ukmphYn-WYgZVF1GxS2qdSy-b8e7VDak7_tyZalwzZdKO1_2MXEdXIbMGc5J0Dx0UfbyLLIkpV9G-hMDXNz732NeEUGUroJNorMZso0elBZiGTQZKSc2_3cBNrDNaS7pi8N-D4pT3_IYgDMvTVesCrm-_zwsZLVOPvhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🙂
پدری هم بالاخره بلوند کرد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/103117" target="_blank">📅 23:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103115">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fWmEyBZgK2TYe6SrCiWTqhFu-EP4_Z7yE37NnhVCthHyBS76zJ7tIeh1b-dtPhG7Ynp4EG2hcAMGzm1DzV8OPGKtsOAENFLdIMBdovhSgGGhyjaTyCLQpGV8ZYhkzVMT5aiS8UQu7Pk84YoK-3k3awLI3YzRODjaDHD2vWZKfU0oRnNSWx8NsQh4_G_0V11S_c-Abq3brozf4XT732fXjfA8tA6eMsHAvZpvaApU7Zw6CG_o10jQfz3ZkCQDngOg3bR2iGCMbU-Vv1OtZ9IVPye_HZmTRRuI_31PqeqW1dkMCSx3qIHuAPWRR5DJSX1t0ypnRpBwhdFvPRM2gDdr6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hE7YkY82rHHNhLAf2RFtcUaLVS6ZJmGZczMIBWtowFNje_B9tQ975bkiSFjXNa8PS1dPNu4n50LOSwPq8cOu5IpDx5qOSy5ZplLfXiLikmmtogOTp7R81wUVph12FSUrYh-w6-JGVFV4N8lzpXVN353_Jsf5sDdA9S7o8QzwgC258s8g3yP79QMVnxWVcsDLoeK6-U6a4n4OP7EjjKkuAWXxF9C7rL7x_Bw69o_Rf0slvysXWkASqYf-5iqkA43XRdOq5I7x-BKUwiJichMKUBfNYUJzDh2igGR_qNUi0lKLeYC7yznKAhesWZ48YPZZtYGsc5lggOEvyJz4Ar8fxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استوری جدید بانو جورجینا از کمالاتش
🍑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/103115" target="_blank">📅 23:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103114">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiNjDEiXCjI5m98rQ2MJLVge5Rl7ttEloXHTx4rGdzNa3s9KhbtHlZSfkPwbOfAYDQjs6ptUXKz7OmgwxzdPGV0FS3WNa8fCKGd-SwjT0N2IyV5gTewhD3rvNNd5xJVePVH_kQ9i198RcgCkrEhGaRumheByYfUAupve2qTT5imspGDpL1x2EmQub0v99QIqQ-VJP7X3J8CyPFT_8_w2gOrnN-oeLZJH0QmUdguI6r-2qhGe9UFzg4ImxWhARQWdwhqX6vPhQlSd5fQmEJrqEJ3VVu9c7WA_eEtP84ADGCZSZ6LhD56k5tb5_nx4fCjVP9OwJ27-epusKoL_C9d9aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
این کشورها به‌صورت رسمی حمایت خودشونو از جیانی اینفانتینو برای ادامه ریاست بر فیفا اعلام کردن:
🇦🇷
آرژانتین -
🇲🇦
مراکش -
🇶🇦
قطر
🇨🇩
جمهوری دموکراتیک کنگو -
🇲🇽
مکزیک
🇩🇯
جیبوتی -
🇦🇪
امارات متحده عربی
🇲🇷
موریتانی -
🇰🇼
کویت -
🇳🇪
نیجر
🇱🇰
سری‌لانکا -
🇮🇩
اندونزی -
🇱🇧
لبنان
🇧🇹
بوتان -
🇲🇳
مغولستان -
🇵🇭
فیلیپین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/103114" target="_blank">📅 22:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103112">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sOGDuUc4jDi9Y_hRF2EDBwF6uWWrIia351VzmXsfrjqkUH3SF-os7Pvg1F-MGkoK3_vBHJyWnSvleCWY_MmhJ2caYGrxTI-Iyu2bbZahX2Ds_AlBb5--pwGVM1RzrdrtTsKESEI_dt4ZL8J0YGYi8xcdiQ_zL5J2HDIo0-vSue3rLoFj1n1pe-P5AGb3EnxlCQwoP4xWIN7AAkowvoH74yxC-8bMJBwUEYMc-WZbZKhvfOZxP7YS9W5ZqCz6IvwWi8TtLUlCcCHbSLHsSfvyUIg6rMXPQ7F-Da7l1kI-UuzqurjnH6cLjWDAdSbjGjUxZsm5njGqYgiYJEN7BQD7QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cgfFN21WxGQTvUqO5tiyHwANZf54rpztwvU4qnQpcFWC0iSvUQELD52hFUYAs7DXs-E66IvhYuvw2SwSSgfxJMB1Zxjx-yEiMU1rqUl-irIxgL5qzsP1oCjWYVY1OiWkTawb61rMdC60GFTA7CN9C_wpQ71GJvvtTVdoPj-Zq7yCMZSb1Q3SM4mI5NNrcdXElXE61nagHp4t0Bsco3yWr1kmkCw8YUIVKSfYiU4oH4LxnvDWoGJW5OtRaDGJzqT6g9juPYpJbEJi06zFxT4RxfjyPP7W0jH2zqiSyCt3XYMMhEJnFzZw5qkRaKxhEfbAmfEPTNzmSFpPTuVdP_VJfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
مدافع وردربرمن، عبدو کریم کولیبالی، در آلمان با صحنه عجیبی روبه‌رو شد؛ سارقان هر چهار چرخ خودرواش را دزدیدند.
🎙
او با انتشار استوری در اسنپ‌چت نوشت: من فقط می‌خواستم برم تمرین.!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103112" target="_blank">📅 22:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103111">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjMH7-Lra4_-7dFE8-sGWhai9nyiF56Er8t01fJZCjyNHaWWt7a0Gj02Rl_cvqXqPvVQCDUtlF6wylZZmGodoVKdqCPLCCUEeID-prA3vbTsIqJuI61kxlysuJo07HJYFwWfkLbg6TxSyAwZFnR8FINzBOnyK_crSfxScwbYJ9lBF0VM0EeAG4Z87SrOztqvficN93paknQOQki90BAuskIDXevyv6pMmwDb0Bm-4YRw0rged0I7laXkRzHBuNs14Q5I89Rza3CpSVZvetyi7-ttcLu076be8NAaDSMkQsuLPjNzfThhVLwe_ApcReOPbEa1oTdengz5mlJSRS0-3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رودری در یک تورنمنت حذفی، تعدادی از بزرگ‌ترین ستاره‌های فوتبال را مقابل هم قرار داد و انتخاب‌هایش این بود:
رونی یا اوسیمن؟ رونی
بنزما یا کین؟ بنزما
کریستیانو یا لواندوفسکی؟ کریستیانو
زلاتان یا آنری؟ آنری
وینیسیوس یا هالند؟ هالند
امباپه یا اتوئو؟ امباپه
رشفورد یا لائوتارو؟ رشفورد
مسی یا صلاح؟ مسی
رونی یا بنزما؟ بنزما
کریستیانو یا آنری؟ کریستیانو
امباپه یا هالند؟ هالند
مسی یا رشفورد؟ مسی
کریستیانو یا بنزما؟ کریستیانو
مسی یا هالند؟ مسی
کریستیانو یا مسی؟ مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/103111" target="_blank">📅 21:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103110">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayF4SNIcVdPsCWvDOb8h2pUDZr0e1Q3dOPAePH4PD5MLDtGZiKqOxKKA8c-ldz8UHEOIR5XK5Gj0C0QIsvvKlfZrbBrMWBzEme0DUOgRmCgErsV3cfkVNQgJ09eGCk6gk2uD478ETrc9o7rybHS39Gzz4-MNE6z7R2rv0E-IA2ySPY8Zr3-4T0_OtFvFn13uEYyHJ_NtKdSwHb_O1pAiCxuHhRzbn6pGy5-YbJSoQObshfFw5gCqaN1iZ_QhkQz_Ec0MOAvvwbl9FzkP-or_JuqgyUZw0wxoazcbTAxOgP57azsZqj5peoJGtms0ne-rzmRI8cqv2gZ5SpDr0KOJgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔴
گری نویل :
🔻
من عاشق بازی در آنفیلد بودم، ۹۰ دقیقه شنیدن توهین بخاطر ظاهرم، عمدتاً از طرف پسرایی که شبیه سیاهی لشکر فیلم سیاره میمون‌ها بودند. یادم می‌آید یکبار یک پسربچه تپل فریاد زد "گری بابام میگه تو یه جقی هستی"
🔻
منم بهش گفتم "من ۸ تا مدال قهرمانی لیگ برتر دارم، تو غیر از دیابت چی داری بشکه مادرجنده؟". او غرق در اشک شد و سرش را پایین انداخت. رقابت یعنی همین کری‌های دوستانه و صمیمی
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/103110" target="_blank">📅 21:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103109">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mY9A3w33E6u_4C3WMt8N59sNNUbzmvtuoOHtbakwWr4ASeaAOuqpyCsIQaodeghJws60UaejMyGWku-LpdkmfB0qD_936t53YRzV5TpxRZ32uaH5KtYUNerbu3fjMtAnDYA4TdN7ZOyxOnESAtM8QNBHpijMu6P_05r-hsRl2WmzUVDCl3xFptZ6FgT9Rk0ajbEnNayvkYm7AKqJ9gNtd8Zlq7-kfpFNz72chLospvKvVQeQgCeNjBqtRM9p26bMiKLKa8yRKZjKYjgbqiqipBVyYu0ugUeVEhkiCpIf0lMpMGmXGtb8Mmci51CANn2gDuvZWAn-IlSiP7ZVpavvWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترکیب رسمی بارسلونا برای دیدار مقابل ناتینگهام فارست
این مسابقه فقط یک نیمه طول میکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/103109" target="_blank">📅 21:28 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103108">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfgKIai1XcIP-XV5s0rZj_P0GTOZGCfLcLQCKSqPRAOdTdJLwWUY8QBERAMSS_-7nyQWrdm_lRbizEt_vHyDlB3tNrH0txOVLSmoZLv_wZdqyE9ogjnn4xTZBCR1fSDDHkPCZbNC7bMkir03YN2_9o-z7fZqsy7ojjt174EM4T_JGJ-8ZTb67w3ovbj_Wq0QCXLkV6WkLp5sd-kbWVDFqvQEdsLuWQfwwsj0cEmk8uj7Sd8hsvYgKWIFzMpSBgGYl2P0VpbohdY80s3TZXQbaeWD3E2QI0RsZzvuodnVi17sR6QjyFwgx0n6ljVNq0BaSmjVzlk7spBFmjCKM_jfEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی کنیم از فصل اول حضور نیمار تو لوشامپیونه فرانسه؛ شاهزاده تو اون فصل تونست با نمره 8.90 با اختلاف زیاد بهترین بازیکن لیگ فرانسه بشه
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103108" target="_blank">📅 21:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103107">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeCe6DIdMPCCBH3tN2W3RmIL8SWN_FbPUnN4lY8z8dsXC4fWJMAmWA-c59wWXmWQoHK9piPs-38Tgys6LOKXP4Omq2ctgZq8Rq_3JfOfzXNY0ZdB6vkcWRb70ix8XjZl8lGTD9Fsuu3rRCsAPi1DKND3c6J5p8quRKGB4Qj6O7RkIObfyxkDqVhvVIr2qNvsIiTubKsnxGsff3TNVmi7iujlFssJMTjzTBQECd4Lqa7aOSdbFhaeA6PhkhzzELOulKxVFISWtHsZLUPb3c5Rw2An-7nEnY7h01FWV3phy3Jl6u73-mU3XSdyakXFJx_tKPosyiWcrOMlDi-T-DVHZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
بیانیه باشگاه رئال مادرید برای درگذشت پدر مسی
🔺
رئال مادرید ، رئیس آن و هیئت مدیره آن با تأسف عمیق درگذشت خورخه مسی، پدر لئو مسی را اعلام میکند، باشگاه ما میخواهد همدردی خود را با لئو، خانواده او و تمام عزیزانش ابراز کند، امیدواریم آرام در آرامش استراحت کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103107" target="_blank">📅 21:16 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103105">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bMmkNAkoukfEmcuAV1L07GoFWXl6JiY-aG5ySbU-IZu3d2wb5_2NXSVZ3wCY7PIv4DTiYcdCUgQGLwmzGoWEdHZrEIdrrSmv5_ogDjIRVQ42sIuBVHOSMlBcuUveljrgq5tNVNtjVA9WzcV259KfjEFb7s6qqsgu-RVW4A9ECcFUcXecohqV97VmTyFQS6th-FnXYNuwQBUyXCkd48m2o0NvYw88Zv9cxjz2JJU6dzWhqer4UNin2FhJsVIjnOBx4RN3UdQRcyyq4sYlpyB-e1NrLgmJLTDTLqsF8MoY-LSSWWVn5gl4AlmdLXMM9ODRZLRbjcs239FArt-fzUFV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bapgamg_t2ZWtUtDJWr7JRXzR-22pDL4-I2TXWo-XxX61X_lZLZN_y5Qgt8w9bJ37Sl2RFTpw0R75OUID8RupduMKNIVXgXAsSyc9E8CDu6vE3cwLlnYRS4UthRpvuDIqKOZwo7PPy2sAQgnRmOdvcnKq_fKrAz5wg1EYzRMzT-A4GpZxFESoCW-v2f4MrTzun7Pq_Rfv2Vjqr8mdxIitvClm8Fke0DzWqnZfC2uBi6hzH70U-XkyuWoNmbXGZxeR4ACWPRpwA-8kaO-_m_qynA6m1_wn1gqc5y5WPL9EOiLgMKR2DnY-E1n-JowCNwvMJbCl0XDg-9M6YwPSNlmCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آلپر ییلماز برای گل روی ایشون کل پیشنهادای خوب اروپاییشو رد کرده و میخواد تو گالاتاسرای بمونه
😛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103105" target="_blank">📅 21:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103104">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113b1e4e1a.mp4?token=ZZ06FwU7Unb5EUex_HgHXXT09NHA-XWUheULSuOn-txvIFVpgh-QXD1hTEFE4_ntra3BUzzCsh9mvleO4UbzS2PctgFGWilO13Vut0DRl0uwMcnfGlKsQU4s_fTH5UbaRvHLLJWZbCSitmfiYY-x0zpZZs9TD-CVbMOm3iAS5eyftx7sCPbpgX5-zEV6E5R-sb3XsRsrZ8cZvu8lCWoe0w_MF8MGbxIcbiMQX6jftnlhdsvNNiIMN7ZfTIFzP8r1ZqMkdyKh4eKkOZu2IPGmdd8t_dpbeoX6yRolkZaDNHTT-bm6S2okbqMS0GcZjAShtwl3vRVT6Xw7ufac8DHWbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113b1e4e1a.mp4?token=ZZ06FwU7Unb5EUex_HgHXXT09NHA-XWUheULSuOn-txvIFVpgh-QXD1hTEFE4_ntra3BUzzCsh9mvleO4UbzS2PctgFGWilO13Vut0DRl0uwMcnfGlKsQU4s_fTH5UbaRvHLLJWZbCSitmfiYY-x0zpZZs9TD-CVbMOm3iAS5eyftx7sCPbpgX5-zEV6E5R-sb3XsRsrZ8cZvu8lCWoe0w_MF8MGbxIcbiMQX6jftnlhdsvNNiIMN7ZfTIFzP8r1ZqMkdyKh4eKkOZu2IPGmdd8t_dpbeoX6yRolkZaDNHTT-bm6S2okbqMS0GcZjAShtwl3vRVT6Xw7ufac8DHWbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرایز نقل‌وانتقالات تابستانی
🔥
🔥
🔥
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103104" target="_blank">📅 20:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103102">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/molWLx52PgZozurBlOfDqWT5H6zB38EWxTM9H3amehrqRlguf65U0ByX8-sG8PXJ_NG3NhFKvL_OtBXoGfN5SegqmeH3oeF6x6w-pN2Ngxod2RDfsfjx8lj7K-V-2NCx-uxRQKUGGmuZ_zAz2HhzyIYbvWEnEkSfhOtTb1PJO4oIOW0S7PXabg3FTTeJtJ_CEsEUN7hcv6xjckXSNBGFuPhCnvEW_BZZ-MVV8GzJFlVVot9YI5La69qetQZuka9vnxS7_HGndutukSDpS22uZ2rxla8GXFRNaqQobC0K5PSufj6H6grCCofs2aRJX0_DzuADXqbnPazSBUZEEvGkLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fdd1aafd8.mp4?token=tul1g33QF8-9tk2Hk9jCuXq8nVrL59LlLt_FtrZ6RTRNnVKoK4nVoFdO_HstSyAaAhxsXJ7tOxcacT51_NTmjwYHJ_rYNeTTLJBDJKOPbgJZHQck9OtClj1buUngF7x-vl2aTJTBnA4JQU8NyOhikD9TKQsLZVsWfyZ1b1Cupsle9H7iyD3IgfRk_2j-1Ub2aU6-Z0gujE0ZQrpwJDwyQsVSXjRbGT7d-zv7SBE2RvYM0SdwYST_UYvCJomSp_DyEMyZZeXcaeSKGDQpyfvlJuWifefBAVmKpsNR2FmBhjzjYRnB4VotFIJy0WdBjUkk5hdhnY3Iq7VESrOxWyxmUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fdd1aafd8.mp4?token=tul1g33QF8-9tk2Hk9jCuXq8nVrL59LlLt_FtrZ6RTRNnVKoK4nVoFdO_HstSyAaAhxsXJ7tOxcacT51_NTmjwYHJ_rYNeTTLJBDJKOPbgJZHQck9OtClj1buUngF7x-vl2aTJTBnA4JQU8NyOhikD9TKQsLZVsWfyZ1b1Cupsle9H7iyD3IgfRk_2j-1Ub2aU6-Z0gujE0ZQrpwJDwyQsVSXjRbGT7d-zv7SBE2RvYM0SdwYST_UYvCJomSp_DyEMyZZeXcaeSKGDQpyfvlJuWifefBAVmKpsNR2FmBhjzjYRnB4VotFIJy0WdBjUkk5hdhnY3Iq7VESrOxWyxmUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز رسانه ها یه خبری دادن که کریس و جورجی قراره توی کلیسایی تو مجمع‌الجزایر مادیرای پرتغال مراسم عروسیشون رو برگزار کردن و سریع کلی آدم رفتن اونجا و جمع شدن؛ و کامنتی که رونالدو زیر اون پست گذاشته:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103102" target="_blank">📅 20:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103101">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QG8ndyzE_2N-sEiGQBDawNYPiy76Jwr4ZQHzfV-rZBFj9z6ySxcrwAIBZt_XDxiLXwy6GCdDbJKkVeiHEL24pa9rnDbLO5zbcz-Uvuw-fMyip_SBeYs09AFbEMbCJ38OYJoWPG6gpxa6V6Tg_uOYbfjnCxUCAV5RpC887eJN-1B6CUYSF1XTvnfEtXqVJLKukV1oMHFizfr6XsXbr1C1YB6oCmdhRpkurR1sqedOQwHrTux4SIxaCMJuGzEnZqeF_vg2VPj-SrgMIzLxlJHJRcIg6K790EHrp_QGTpy5gfOW4Z3ctLDAAE7zTSGHCJlH6Q670hqdKmB2pUIuHRNBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
کوروش اژدهاکش هافبک ۱۹ ساله آلومینیوم با قراردادی ۵ ساله به پرسپولیس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/103101" target="_blank">📅 20:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103100">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQmwyQaIWLe8QGK-GogX4tMjS3ZUanlVUi_s3abcifKqYB4epQNS5l5ElupCVki0xhlMkuS5DeOKCJTfYPvXStbPS0J1vxTN67Cow7vGW39ntN2ArsfZAKjhAchmKR8DuZ1dI_xJOqgUlfx1frNYOqmeZtoMmPqYOOfvaN8WoGO8p1WoINI_eY78AXyFNdDiuOCDGLmzG8jmgO5mFF0stsOdMIb7bq-FA8GzZiVQHVS-3_8-y1YfqMPQI5M_yW2eDklfXf9V57LPpx6j9p_DhkGeH3ZnrCJp3x4vsUpvEids0O9wYoYI1U1XKFQOR9hNXlzAsHd7Ah4kXGOSXh01sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوووووری
از رومانو: همه‌چیز طبق برنامه داره پیش‌میره و رودری بزودی بازیکن بارساست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103100" target="_blank">📅 20:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103099">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63a86fcf1a.mp4?token=F_zws_IZpu2lPO39xufIhuGvmgaGM07fqKcX_r6M5vvmHncFOXChiLYkJ3MsPA2diWqCqo1NeHkhRSynQT4Dlp4qiyJY7xMq_eVmePfdqHdFKnmo2T9zdjXnIRcEx-cpkmjZiA1ufbtSNiYDDCeFIfWm2XWu-PDzaNHNAl6ERpNG4WNV_YFCzacyDU5p0xmVUNpPKlcQEahUDdfmqCfakTbl0WorCWyW-7rrXHL_i8f4p0RYB_aWW1oUX3OZ94p8Dkbb_38xhMNa4HteGl77kvwIIVzXZtaT0-T4TzYOt4z6pxtKLQEJ7xsHgs61-m5CRBM7i7XW-B_DbRgxUipg2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63a86fcf1a.mp4?token=F_zws_IZpu2lPO39xufIhuGvmgaGM07fqKcX_r6M5vvmHncFOXChiLYkJ3MsPA2diWqCqo1NeHkhRSynQT4Dlp4qiyJY7xMq_eVmePfdqHdFKnmo2T9zdjXnIRcEx-cpkmjZiA1ufbtSNiYDDCeFIfWm2XWu-PDzaNHNAl6ERpNG4WNV_YFCzacyDU5p0xmVUNpPKlcQEahUDdfmqCfakTbl0WorCWyW-7rrXHL_i8f4p0RYB_aWW1oUX3OZ94p8Dkbb_38xhMNa4HteGl77kvwIIVzXZtaT0-T4TzYOt4z6pxtKLQEJ7xsHgs61-m5CRBM7i7XW-B_DbRgxUipg2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمیرم برا مظلومیت لیورپولیا که قراره این یار مستقیم هالند باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/103099" target="_blank">📅 20:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103098">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd45b921ef.mp4?token=abG85qj0pbKCga7t6sf_5ikdRNLoJl8rcrj81Cl7NJr94Faq_Od0bIM6HMKXcBug9-xNSqmxPhX61ZG9QvtmPWFyj4wClugEYQsbFuHwV-hZZEJYZX1JFMiR5vI9iiEuyHM5M6JcC3a11ebfijZa3_oLAO1MVY0iXAcD9LLTJFHf-IqWu7nphxoLjdS8-SwFYLmQC-B1puFKG6_VtIMoaynQ9hAqA8osimhIxeED0Mj6Isav2S8EQ1u3XUY2C7BrLlNnpHDdjmglvXcjAEforJPZHGyDoqe7_Beq20tzNGiw1Zx5fHziu7CjqWSEAZDp1ItKKTBqdQE6S-5WQcvnAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd45b921ef.mp4?token=abG85qj0pbKCga7t6sf_5ikdRNLoJl8rcrj81Cl7NJr94Faq_Od0bIM6HMKXcBug9-xNSqmxPhX61ZG9QvtmPWFyj4wClugEYQsbFuHwV-hZZEJYZX1JFMiR5vI9iiEuyHM5M6JcC3a11ebfijZa3_oLAO1MVY0iXAcD9LLTJFHf-IqWu7nphxoLjdS8-SwFYLmQC-B1puFKG6_VtIMoaynQ9hAqA8osimhIxeED0Mj6Isav2S8EQ1u3XUY2C7BrLlNnpHDdjmglvXcjAEforJPZHGyDoqe7_Beq20tzNGiw1Zx5fHziu7CjqWSEAZDp1ItKKTBqdQE6S-5WQcvnAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روحت در آرامش خورخه مسی.
🖤
🕊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103098" target="_blank">📅 20:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103097">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beec0f3cef.mp4?token=fysqqQ3VwXiDnFIU9pSSbIaz7YQyAGlkn8JMwKfhoTMKcE7jRr8oDVi2he8G2qM6Nvk-qqP4uVnTslOd5twvv5EDDH2Mwta5AZEoaBh3SOTfZFBQMBDZDs0JerhbYuVNht-__NXJO0Y1Wj3M42HIA10cdzImiMhQZnLtLpvsj9Gr0OcYwLWzV4ck745pL2l5oOT-yqJN50eMy6xZhDmGTiMLdLodUmROYOzKigiKgTS3hihzj9V5fHjFkv-umitkDeI40HlnmtRza-F9K6dIxvz0es3fXp5twkA7_r9mPny6FZ9z19bA879vsPiQvQYnB1gm01mu34Fw-h3jWNGGeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beec0f3cef.mp4?token=fysqqQ3VwXiDnFIU9pSSbIaz7YQyAGlkn8JMwKfhoTMKcE7jRr8oDVi2he8G2qM6Nvk-qqP4uVnTslOd5twvv5EDDH2Mwta5AZEoaBh3SOTfZFBQMBDZDs0JerhbYuVNht-__NXJO0Y1Wj3M42HIA10cdzImiMhQZnLtLpvsj9Gr0OcYwLWzV4ck745pL2l5oOT-yqJN50eMy6xZhDmGTiMLdLodUmROYOzKigiKgTS3hihzj9V5fHjFkv-umitkDeI40HlnmtRza-F9K6dIxvz0es3fXp5twkA7_r9mPny6FZ9z19bA879vsPiQvQYnB1gm01mu34Fw-h3jWNGGeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نیکی نیکول دوست دختر سابق یامال:
یامال ازم سو استفاده کرد با اینکه من دوسش داشتم بهم تکست داد و گفت هیچ وقت واقعا دوسم نداشته و فقط دنبال سرگرمی بوده، من کل شب رو بخاطر این پیام گریه کردم. اون خیلی دل منو شکوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103097" target="_blank">📅 19:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103096">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKqfVj4ANBaqfUKqinrXxWQLssw8T0mTGHIAcm7EnUy7GqnKS1Pv5daHurKODAfGCdXvRb_2BIF_-tSGK73A80mjGgN7zauOX-XaLUqkAu4kBMtJwfB1JzBhuxBoj2kC7oYy9TUJgeKyX6IIiMurv5B2XWDjTFb6I8Zxc87xtyoRS6fcMg0CkDTGITBSzDwJfQJir2YHE_j6iDjExiVgBOvEDvUcGx-V2mVqtVPR2S_Et7paCvKyGJJa8BWa_ONwuzDKVz0OHPc2Y-hAKNOgNwcCx3_PI4H0vp89uH_z2nmuGdgavr8J4WIGNTdHZ81aEDCTw5g2hlw0V4EXw8qtiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی جدی از اون نسل طلایی آژاکس که نیمه‌نهایی به تاتنهام باخت هیچ کدومشون بازیکن درست حسابی نشدن تقریباً
دلیخت، ون‌د‌بیک، زیاش، نرس، تادیچ و اونانا
دی یونگ یکم توشون خوب بود که همیشه مصدومه؛ جالبه همشون هم سود مالی خوبی دادن به آژاکس...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103096" target="_blank">📅 19:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103095">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa788f17f3.mp4?token=P8ILGAJlFC4hivnl5o2dCWNDj2kRTl2WOdrGEwChhcHUHt8fz04aWEoWS9CRTmiRKIxkSTVyOfMwi2Lorf8R0nRrMrwUsZE6Nd_3sFikzf06HEqhpR_RTqRC5aIxuhMYQnPcrUQK9D7dL6iP9-lfDfvxl45vWLySCvHwa0O9F9EguOrcXWmbR9U_DD2C4FW3qaTOzEg_nkl8ayUTVq4SDtdQmG3zSnBEIRnI7vp7Y181Q0ZmCF9khgDy2UAKu_Ftb_ZItGF-Bi89VuBlTojdeiQDiOlMNIHiBOSy6CPLzbhhf8Yy1rpkRX4B1GW6HJt76rRj7L-wdrhwTPBl6dupXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa788f17f3.mp4?token=P8ILGAJlFC4hivnl5o2dCWNDj2kRTl2WOdrGEwChhcHUHt8fz04aWEoWS9CRTmiRKIxkSTVyOfMwi2Lorf8R0nRrMrwUsZE6Nd_3sFikzf06HEqhpR_RTqRC5aIxuhMYQnPcrUQK9D7dL6iP9-lfDfvxl45vWLySCvHwa0O9F9EguOrcXWmbR9U_DD2C4FW3qaTOzEg_nkl8ayUTVq4SDtdQmG3zSnBEIRnI7vp7Y181Q0ZmCF9khgDy2UAKu_Ftb_ZItGF-Bi89VuBlTojdeiQDiOlMNIHiBOSy6CPLzbhhf8Yy1rpkRX4B1GW6HJt76rRj7L-wdrhwTPBl6dupXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتشر شده از عروسی رونالدو و خانمی
😃
😃
😃
😃
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/103095" target="_blank">📅 19:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103092">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vbzQxgEdB6TNZEOSspf51l86zSTDwnrM_PafFkGUOe4P9JneXXmmg-Gr4bZ8Yp4oxqYv4vttP9oC-VA12tw7NzewJVGpjAttoZ9qA3uf57nj_ttByj4v6Dw3dgBMqp3jBClU5uJe8ZJbZYcuNoGq5yyFVt-fR2WXfSC8_9GqoNm0NP0spZjahR5sX8VmMd_IheIkUHRKejbybNv5RcI9QuhX6U85FKzQpXFE8uQ3-lrnwyLXENZyUUO2mj8q109BlRIK1ON-deixPPtWkJUeoNt39rUHkpQigcm-sGlsCrJhWrMJHdmHiVzZBeRv40q2vOOcwWMymNBb22ZjKRZhgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQ4PYnNuuLJoIbm-5eL9QQN5MDi1Xzepvt6Rc-jnQZ76-ls6nM2cQT2KBQefe9GVHp2OLT9Lc3AaMs9toXydNmtc55ERdaDNxjVCsahXVtlGsByn7xR9175zppHIF417eL3VA-niQXG54H8LXuW7gI6cbhvPuzMT09KIf0B4hghYnEDxbC-iLdwhk_2LAfcwXcg6hde1rVUnT8KIu8E1NIvNPNBg3p5-TUcivXxJAH2nlXywhXPn8ogz5nNreFteRqYEDQM7KfcYBqWwPAEAarai3YLnRV7Hu3duBic4AnztXUOmD1bDYm-LtGC-a4b5osEHFpsBiAEV9pMGZUd5cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T_rlLTYsGLxuo73QtKBahFs41JkAG8ncLhssULu_8UdSPS6LvkVIV3qzwaGj3pDDDpbI_J31WexiLrQwxM5SdHNDZ94pAde1LqqpWFMSB78w670J3oVxdhYTA-ioiX8997J9kq7nzMyXNxEIRaLC-0zllKfnBj2U-Lpy_TPyeae3PSfiE1aG2Ns2nhec-LqK20lX2WkXFXUK5f3HGyuyMXEI2NG_qmNNWyL5qlegHaF40ZR-ojv3x2lB3Xqoyjaoq8gjyabO57uJZ_eQDENdBxQJkHVx4r4p2ynlwCRgKDuZx7_bTBnlgN3jXPYGVdgVLU4A8yjxHS2HXj55Rr9iXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
✅
👕
کیت سوم فصل جدید بارسلونا که قراره ۱۲ اگوست رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103092" target="_blank">📅 19:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103091">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mwo0f2i0hlVjf-JxMNMTL-JFhDeJFgFcl6lTome4wmuOBExRB4jzD7p1Qb26E1irrXKGBgf-C41nk4msTYL1e244Foqyxd0v1aQN021RtnddTM-qDb8GhKxNbHMOY47CqjWmkT9NM55enwhS8-tS_YuEG_41HUubqbFFEoWOx2CjDdzzj-7-Mf528euCLI-0aRWQsQfoS-43oUfbEPCugNDzwyeqh2aEoF697EHmVdXmbtGlmr-m9nIUVpIkj8mFOSBtDu4PJ1M67Hue8Ujh_a0Gb7ZeRVyvOTFxlOmoYnu7bAgceEiXk5N7e9WJx9N8CIZz7pfm7wZ16t6RsBJPrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🟩
پرسپولیس در دیداری تدارکاتی برابر آلومینیوم اراک به تساوی یک بر یک رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103091" target="_blank">📅 19:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103090">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUDQ2T_6W1jFY_9QR6KFwNwkefKwEmO4zcu1WLFB6yD-nG4yfzsOoKO2CDW0D5gm0oyOa6pQyrOFmlLcQEE0Vm-fjv41cPkC0uH0luwLUP7BONN08p7mMgFuddi1HhT8WUuG8wVf5Pp8sTEatwRT-Ji-OCPZrW5-cEkYbIXajzbwU9aVoSryun1rnWK8wAX6_NErWuGb6rOezBRS_v_4TRMouVh6sGsQCzvWXnVmk6xJJUOMZvDFkme5tcYKqAjGfJFBjPatn3FQNldEQIALSuTWLOBHJv1p54nbFzZQ7CUiN-YnLys_4pC9jYuOG1aa8qKIqoruuHwSkk5QkVxUBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب رئال‌مادرید مقابل واروش‌مجارستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103090" target="_blank">📅 19:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103089">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/103089" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
با این سایت به راحتی میتونی کل ضرر های جام جهانی رو جبران کنی
بونوس هاش واقعا عالیه
👌🏼
بدون قیدوشرط
❌
با هر 1 میلیون شارژ ،
🤩
🤩
🤩
هزارتومان شارژ اضافی بگیر
🅰️
❌
❌
طرح شارژ رایگان فقط تا پایان مرداد ماه</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/103089" target="_blank">📅 19:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103088">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3KI4oUhX_76qvd4L2ILFGJ5lukPfjI2TKMdlqfO730iy2rAQX4wYJxLLztw1JPmBUjupdr7NE_Ufi0e4abtxzIFfZg8cH9H0FuViRaydP-4ME-H4Dlct2Yhp9stNV3_-2ReKEmM47OgyUmd-JiCmz0htE6PJOlsSQ9mJSV9KwWU8BxyxGRVvtR0AzjtvDnzujLxG2YnHeFoPWICe3dx8tXRrHyS2RohsaiA3FPEl0B1_F5hYvHCD9J4mHLcp3iDNxsbmoGKX4Z-E_lxSfWWTvTuNvEWZqo_WswFhlcZ2L_7iO_cyfMn3D5xT_vqZg1XpYiZOaWuwEW2s73iHSumGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛍
#اتلتیکو
Vs
#منچستر_سیتی
💰
🛍
#لیورپول
Vs
#موناکو
💰
زمان: یکشنبه ساعت ۱۴
🚨
تجربه پیشبینی مطمئن با
🤩
🤩
🅰️
شارژ اضافی و ریسک خیلی پایین در
#بت_اینجا
رو از دست نده
❌
🤩
🤩
درصد برگشت وجه در  صورت باخت:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g17
@betinjabet</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/103088" target="_blank">📅 19:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103087">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUsEusdQpWm5QZi1INYneSRcTuT6V5Ck-55Fx6Uk_AE83oxwLu5nbNTx-LKJctpH7efYib-8dBDebpUEfx38vlElBy2guAbvubGHF4zpatLDm7zHmTXvHQyxyJQjJ82ryrlU8dgO-ioL9noi-d_9ZklvGwWAN7Jwa1iiDwQoMRwCaAeg048rsirRh6KxRkmP2cTZpvrS0SGD8RMpU3A9h_R6pBuUF5cNmBwdJg4CCDvAju8sZiTvgPyenNbX6xMEtC4nf2ZatoYuxg6Wrs2RzYs9eZvA8-GQmIYHQs9abtzzqxaYYiKqTm9b8ATRAA_Pb1iPgfksqH_JtcX0S2rBJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نتایج چلسی با ژابی آلونسو تو‌ پیش فصل:
- برد جلوی میلان
- باخت جلوی یوونتوس
- باخت جلوی تاتنهام
- برد جلوی سیدنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103087" target="_blank">📅 19:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103086">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47158534d6.mp4?token=l3uA4oTKrCpnM9Op3Dmn1FHgot7iapUKUdN-ZHtoYcOT597pZXC-GpcxYsxuDoso_Zhr9Cu6dm_aeke57Y87ynrQ3KoxjX6-9g3ZAFcsp_MSB-6syVecL8W0TjlY2lGNFpVzZ2uC2GZ9jatbFhqhuslzfUmmzMXR0zj-pzRArqkhY4h28z4SC-1AH0xAbJQGVxBk6Y7oazf7S34dpUoVDGhwq3RjCznqPGp7wzUShRM-gwcfgkhwQh1e3_bz5XtSmYloFxIKGDuVL9XTBKTjD8sYWFKdkL9enGBNhRCgxUXv6_Lxzg8OGPSbLtrmc9sAVaUeVCOl6HKH_SctY5JtNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47158534d6.mp4?token=l3uA4oTKrCpnM9Op3Dmn1FHgot7iapUKUdN-ZHtoYcOT597pZXC-GpcxYsxuDoso_Zhr9Cu6dm_aeke57Y87ynrQ3KoxjX6-9g3ZAFcsp_MSB-6syVecL8W0TjlY2lGNFpVzZ2uC2GZ9jatbFhqhuslzfUmmzMXR0zj-pzRArqkhY4h28z4SC-1AH0xAbJQGVxBk6Y7oazf7S34dpUoVDGhwq3RjCznqPGp7wzUShRM-gwcfgkhwQh1e3_bz5XtSmYloFxIKGDuVL9XTBKTjD8sYWFKdkL9enGBNhRCgxUXv6_Lxzg8OGPSbLtrmc9sAVaUeVCOl6HKH_SctY5JtNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادای احترام به مسعود ذات پرور تو مسابقات اورال کاسپین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/103086" target="_blank">📅 19:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103085">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpIZpGVITsZWTnCd_t_WxUHAZEl38ddjO0c-SXPjXxHZ-qCw2OHVEobMxDBNXU965cZW5rvC2DW9XaYYSfPHyGfchCkcvE86rf1g0TtrIauKO7ZwkCcDMBKF06E-JGQNxMjEi4kDoFWvg5DNy4TbVPk_kx0kVwKCFRUrUA9D2QxjokaOgwvGJWKmYdgt-0y4NGDdcDdMTUD2Hv1RMt9DtS49Qnnt_uct3WV7Y1LWlRA_TemEIf1uNJerzdeSWpwhPPODATQlDYiW8fPuPHR3WpXtgPMdbeY-bF05WPD5ZSMtyoKhcRdl15shi94PrW_Q1EKMedBH_0xbHSM7lRKLAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/103085" target="_blank">📅 19:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103084">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5956080028.mp4?token=I9V2O7naV7Z3IcFdYiFoysitsVqtKgsv2eEulG0m-q2J1jWzxTBAlEKUuhdA_hTikt_4obn9SvEg7Y7Q5KoZHNa88hWXXVkuk7CQ8B4QFrLVk03MrgeYg89rORezGzkcBVaz4B_0YOmvj9sB6TTNPsmsE_NkHGMoe7Y5A_fgXcbMU3vqvMpQwNX7z8AeYUNLjB5wa7-qvrm1-ub0_wLBf8Ugtjdey-UFYi9B38KAi7-p_yhnMT6CFU3Wspq0StqUJieCxsiR7Cui9r6JcVrtMeKatZt2q9HiR0VitVJS07QFQmxWBaXOQsig4GFJLAHubm9sRoF1DaZzzc1_uLcMBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5956080028.mp4?token=I9V2O7naV7Z3IcFdYiFoysitsVqtKgsv2eEulG0m-q2J1jWzxTBAlEKUuhdA_hTikt_4obn9SvEg7Y7Q5KoZHNa88hWXXVkuk7CQ8B4QFrLVk03MrgeYg89rORezGzkcBVaz4B_0YOmvj9sB6TTNPsmsE_NkHGMoe7Y5A_fgXcbMU3vqvMpQwNX7z8AeYUNLjB5wa7-qvrm1-ub0_wLBf8Ugtjdey-UFYi9B38KAi7-p_yhnMT6CFU3Wspq0StqUJieCxsiR7Cui9r6JcVrtMeKatZt2q9HiR0VitVJS07QFQmxWBaXOQsig4GFJLAHubm9sRoF1DaZzzc1_uLcMBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
رونالدو وقتی از سماور خودشو میبینه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103084" target="_blank">📅 19:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103083">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">▶️
داستان عجیب و غم انگیز از ناصر حجازی
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103083" target="_blank">📅 18:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103082">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_avQYh7CjdN9cnEMWZaDdimXTGLtFQebIBrLwJYG2iDyYXMOtugGeeWnH9xdPSsFVtsswWPRZsCXxRMs_Rqz7MOr41camV2AjCYGr1HBuw-Q88SEFv0izNcMeHvm1gRjTIklzaLbMiM9UUNdPAwG3xyPKlZsX_naBmlVof07ntY-_Dmwsr-c96FlHh-tmRANFo_iee4YqIPoURwr0h5hD9NOv_MLzQOvrqvCtpwEXYAYQrAVP-_tbTxsXeGHpzxK0sFsiAt2RbC1G28n9Dmic13kvkBRCu5onbdH9iLWoci_foEpzHUnR-vod5WCRY0EmeA13xN_BUHjTQsxs_MrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بالاخره موتور چلسی روشن شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103082" target="_blank">📅 18:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103081">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0Kv5iWBUJzDzuYxetbndrgpDBpR8YAxH2wJtZafHwDozaumzHAOk_7mZExJO8Xyn5YE8JDgxXtX3eAPPDbuafESEGwRbSnnGbBymE8HO4eDI1wkpLbYTXqq5nXCHGIsQ9P1Do6g6G-NgY2tVXO2RWdAxoXQz-1K7nFhqGFpRjjQ5wBBBZyh4TCOEkuVeb6Q0sDE3tZnLO9Q0eME7jarfpHPzGWvJnetkshcjC8ky_92JejiO6Ct4EXRyuNkgVwROi4BL-VPIYuEkidDG6h8vLTakPFPXuNE5GiGY_QAA8Gsr5TrWrw5Z6DeHjxNxd00TboKpNi02ne7Q8xl5D_CdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ایشون برایان ماجو مهاجم ۱۹۳ سانتی‌متری جدید استون‌ویلاست که لوکزامبورگیه و متولد لندن.
‏پشماتون بریزه که متولد ۱۲ ژانویه ۲۰۰۹ هستش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/103081" target="_blank">📅 18:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103079">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jG3F3QTHvITPuj3jT0m01CohNki6jArYywoE1_Qr8DrBdoGfjKmsNkGVaIQvrmbvThr1z925YbSHoUepenQURIZVhYhw1yRgfYErYIUw4ddBaGQv6QftYXRIiJwfymKwsoGcYPsU821A_ZeDZ7HTs4eLYd7l-fbt5RMRJX_3iuUjtZsq2mVrug4IJzo3IEIX_cRiz9bsAe1bUsl6BAcPoADNDAdwepVbKjEBbhy11zlzQGXHD0m4lFlEe1QZj9lp7UIgZT-dSR1PncPx4umUL5FvCVbBvAhAWAasJ48xepTCfjVjykQ_7jv5JYDr64P8IpT4Ee7ygAxZh4GULvEoWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y4sYYZhivTHo775TlxKXq9mHhJCIJXaRUAQxPchukGUsX10r6uvrhm4X06oHzHYZKUwyKDsvOwAc4Se7a3S48TqsUBmY8_dQSM4M0lLq8zSLC0wpDtKp7K4aP4I_yhKBsVcaleqgyMGcu54OmO6EHNN-f2GPLnL5l6xTiypM14F1_xTn_MB2zJAUArlwBuJG6ozNlFZhf4lz73bf1fPkY_PGpWyufKcMh5GVf7fD6MI-VzV3xQZ_hEKObqG9OamOro2CvGu4iIekqeHXw4JuwGampDt34yPbUvwx5U1IowCVBVpSxEA_L5ihYO03g7jwFTXpoOcae4doZ2AlJihA-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">8 آگوست تلخ ترین روز تقویمی لیونل مسی بوده..
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103079" target="_blank">📅 18:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103078">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
از ال‌موندو: زوبیمندی ستاره آرسنال یکی از گزینه‌های پیشنهاد شده به رئال‌مادرید پس از عدم‌موفقیت در جذب رودری است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103078" target="_blank">📅 18:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103077">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d44f31c73c.mp4?token=JqltQz-_Hbdc3gNNsXdSiPURqDccbOSGcwl3Y05I5IfmEuIU5RCVcMJDN3-wH89VZzJWMBk4kvC_lRwz3YLDPtTEou1PB2-QqYiZ6Ha45eYNXkjcBS0wE_YXZtcHHZPFtqjuZYGvzmy5ePuwKXJ4X4L92Pyzgt1vEPRE8WgKLQ-yDugyrPOpE9XPO-CQiTbvthS9xeAJKyhf5la0XXfQR8qfW2QNkhaIbikilGa--aj9XKn_UI2DsNJTsIuUQwf_KTjzrcbBcJ0XjSeoC8MyipZHP_EshDok_nqwml390lXCQl1C2-UeLyaPN8OXnNSWRRAbyC_OP8Re-AoszLxOyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d44f31c73c.mp4?token=JqltQz-_Hbdc3gNNsXdSiPURqDccbOSGcwl3Y05I5IfmEuIU5RCVcMJDN3-wH89VZzJWMBk4kvC_lRwz3YLDPtTEou1PB2-QqYiZ6Ha45eYNXkjcBS0wE_YXZtcHHZPFtqjuZYGvzmy5ePuwKXJ4X4L92Pyzgt1vEPRE8WgKLQ-yDugyrPOpE9XPO-CQiTbvthS9xeAJKyhf5la0XXfQR8qfW2QNkhaIbikilGa--aj9XKn_UI2DsNJTsIuUQwf_KTjzrcbBcJ0XjSeoC8MyipZHP_EshDok_nqwml390lXCQl1C2-UeLyaPN8OXnNSWRRAbyC_OP8Re-AoszLxOyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
ویدیو وایرال شده از مصاحبه چهار سال پیش رامین رضاییان در برنامه فوتبال‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103077" target="_blank">📅 17:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103076">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b851903a5.mp4?token=lIRIU9G0MWv83pj0MTT_AHJWpubDE3DIUJ5jbVTxgBjTVh9eh_5GWxqowWswqIXhClCZBeegVbLtPV5r-X_TGDMaQCLtn88bJFatfxc0mrbuvriKYecnNQbH7Q9_pJkDgJXfX96VAQ6YabH_xyop_-MGY3Syykns_CQdmA0U5VQwwJN57wz2OBtlrh87R1jw3b9wG245PgZVmsprSBdvzKxueC7hXJnJ6v6GrqAN4qO1jPJfgg4bMSMLpcIXNGmQiaRgBg2L7Am2EF9DR7LYQqRDiQzSePmbVHUAtSTrqJl9n14r_C3Atb4nrMgCdDLhBwQG4i2Yq5HLvDs9PsIPmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b851903a5.mp4?token=lIRIU9G0MWv83pj0MTT_AHJWpubDE3DIUJ5jbVTxgBjTVh9eh_5GWxqowWswqIXhClCZBeegVbLtPV5r-X_TGDMaQCLtn88bJFatfxc0mrbuvriKYecnNQbH7Q9_pJkDgJXfX96VAQ6YabH_xyop_-MGY3Syykns_CQdmA0U5VQwwJN57wz2OBtlrh87R1jw3b9wG245PgZVmsprSBdvzKxueC7hXJnJ6v6GrqAN4qO1jPJfgg4bMSMLpcIXNGmQiaRgBg2L7Am2EF9DR7LYQqRDiQzSePmbVHUAtSTrqJl9n14r_C3Atb4nrMgCdDLhBwQG4i2Yq5HLvDs9PsIPmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
🔥
آهنگ خاطره انگیز:
Savoir Adore - Dreamers / PES 2013
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103076" target="_blank">📅 17:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103075">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d1230c317.mp4?token=QhFI4tCRXlG9Esh8185-9bbThqG7w51qh8V3AP7kzCjNzDN0rIJmrwCEA0Lhr2rmcAPJ6Nv7tkyuRME0lSUYW4MXxc4G8J9_sLi3pyAyZQWF5wE-joOd3EHPRHJRHW9HPLWKPL1z_mq-VYdZ8bvqh8XuadRNrBhxMiVGSykK-rzCDvKsEJrLQPQLAzFcNGaLSQX_Di61DiuyU2Vy407cwK_sKhDiYvbHjClvkFbImgd9s5ndBJ7CdhOhSQXa8LtRpBRvrp39QIsPI9BdL7uGKgMxT7UfFzrqV2rt2u1Rtnbdl4nLFjqqFVVdOIh_ILMffFatm1A0eYVd9VWU2vsujxcDVPTxTJitO_gyZNhozT1bR6xNM0FfVI1J8EHbDa8isqT33EUrvn96YKhd_Oo7r05xnO_LokK28q7oGXpiBS_-Y3GfyU_PnDh_iCKtfVLR7_avKJmLQgTY5sFBmbtu8GgHwXnK_PQRvfv-MnLmXgFa7GUtmWShVqODH1xAxAGFrrSRAqPIhu-s8Dmzf_h-SHPkM7sa5WdSWiB64DvNZMvaSnr7CewYT0l9ZVIrNex16KT7UijPDEuCzVdu_nsJjnhJeNJnYwoDTm9HjNHsApwt-mvSL8MpQtzvaj0MibqcevDoVXU7owgk9SVdwfhaG6yDZMcjBhfJhIyuxdYvrZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d1230c317.mp4?token=QhFI4tCRXlG9Esh8185-9bbThqG7w51qh8V3AP7kzCjNzDN0rIJmrwCEA0Lhr2rmcAPJ6Nv7tkyuRME0lSUYW4MXxc4G8J9_sLi3pyAyZQWF5wE-joOd3EHPRHJRHW9HPLWKPL1z_mq-VYdZ8bvqh8XuadRNrBhxMiVGSykK-rzCDvKsEJrLQPQLAzFcNGaLSQX_Di61DiuyU2Vy407cwK_sKhDiYvbHjClvkFbImgd9s5ndBJ7CdhOhSQXa8LtRpBRvrp39QIsPI9BdL7uGKgMxT7UfFzrqV2rt2u1Rtnbdl4nLFjqqFVVdOIh_ILMffFatm1A0eYVd9VWU2vsujxcDVPTxTJitO_gyZNhozT1bR6xNM0FfVI1J8EHbDa8isqT33EUrvn96YKhd_Oo7r05xnO_LokK28q7oGXpiBS_-Y3GfyU_PnDh_iCKtfVLR7_avKJmLQgTY5sFBmbtu8GgHwXnK_PQRvfv-MnLmXgFa7GUtmWShVqODH1xAxAGFrrSRAqPIhu-s8Dmzf_h-SHPkM7sa5WdSWiB64DvNZMvaSnr7CewYT0l9ZVIrNex16KT7UijPDEuCzVdu_nsJjnhJeNJnYwoDTm9HjNHsApwt-mvSL8MpQtzvaj0MibqcevDoVXU7owgk9SVdwfhaG6yDZMcjBhfJhIyuxdYvrZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تمرینات میلان 2002/03
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103075" target="_blank">📅 16:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103074">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZllwytdSklYgq8wOovSJjMN52-iyStb_2HuWc_seEqeAvTyiJcSCtrg4_UIvrpeY6PU9J5Ov2XmwrMchUj61fzc7dSQxbdP9brCxaUy-XZayThCWfi19xuGr7Rcvg1q_ZOlKb3ntHi50bHPseaIZ7ciu42RPrKT8JYRRrX_FyAZmyAa1N3k9pdLzgJmC9s8hOGYuWvU6LwfPXDBOOq-Rn9A3IOpBs8g8P5gGYwdS5WwQ-T9tXwTbOOVXn1m3kwPTApLkbVFGsNaTEIU3Y4-quLGAHkUb0VQIGMMZE6VI3AgWD14OHQFipYPlM3QP50EoUspDeiru8kyzCrqWigwYcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فورییییییی از ویکتور ناوارو: بارسلونا در حال بررسی شرایط جذب لاپورت به جای آرائوخو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/103074" target="_blank">📅 16:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103073">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8cc1a076c.mp4?token=YS8jqRy2bnnTEVHnjhcTQ7hpGnNxuZQ4zYu5itYzx39t2YSSApxugFDIxBtnJnUg12d6_oqBDxJUuUsSWWjyg_f151itm7BROjkxUzEvBQo9UhyM4zgjmrDUMfZGKetZyP2cMpuqjxaTVdtV52a65aQYHLxVhYJRceNUfP8GlNblEjo6js9aXwEWELs3h7X9WdSJxIBJSsXcnxkkQiYykSfCLj6XD55rwKYhuFZ5UIMl0qT2xlWf4DG9tUHkw4tXAZflCLZRrbrk4w7Fz4URS0o6hIBDbsfPGngovTOiqzftW3uZadrW7qD9mN43EXJEcdo_jtnzwXuGlTS4Uk6h3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8cc1a076c.mp4?token=YS8jqRy2bnnTEVHnjhcTQ7hpGnNxuZQ4zYu5itYzx39t2YSSApxugFDIxBtnJnUg12d6_oqBDxJUuUsSWWjyg_f151itm7BROjkxUzEvBQo9UhyM4zgjmrDUMfZGKetZyP2cMpuqjxaTVdtV52a65aQYHLxVhYJRceNUfP8GlNblEjo6js9aXwEWELs3h7X9WdSJxIBJSsXcnxkkQiYykSfCLj6XD55rwKYhuFZ5UIMl0qT2xlWf4DG9tUHkw4tXAZflCLZRrbrk4w7Fz4URS0o6hIBDbsfPGngovTOiqzftW3uZadrW7qD9mN43EXJEcdo_jtnzwXuGlTS4Uk6h3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت عجیب بهروز رهبری‌فرد از قمه‌کشی دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103073" target="_blank">📅 16:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103072">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e632b28ac1.mp4?token=f7YerNMwPYSQCEbBWQrI4OB_WsQigYncdlBTcSo7Y9TFxzR_D-9NHtGaEzpg806B-ADfMf7fbY-vLVJiWiYRaKojhyZXC_1qF2ODy9RgFKBPv0dsztpvis-NtSI_TRZZpN2DVxBEn3nSSGusbqZpf7zd9NbwSKKDZDOeOHAou62LNURouAnwRB_W9h1-HQYFQUjjHL7pmQbc7e8bbICFxID8OMgUu4ZTYWSoJqTGt5Ej1GCtXjyBNARW9rQ1DlQDoio-AdBVhsClIoadgY2McGMyGllhObF0Rd7rKkSxE8gg8cH5pbO6roQTdkVtH0Fi9ODS3zP7OYD7INrs2r1qvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e632b28ac1.mp4?token=f7YerNMwPYSQCEbBWQrI4OB_WsQigYncdlBTcSo7Y9TFxzR_D-9NHtGaEzpg806B-ADfMf7fbY-vLVJiWiYRaKojhyZXC_1qF2ODy9RgFKBPv0dsztpvis-NtSI_TRZZpN2DVxBEn3nSSGusbqZpf7zd9NbwSKKDZDOeOHAou62LNURouAnwRB_W9h1-HQYFQUjjHL7pmQbc7e8bbICFxID8OMgUu4ZTYWSoJqTGt5Ej1GCtXjyBNARW9rQ1DlQDoio-AdBVhsClIoadgY2McGMyGllhObF0Rd7rKkSxE8gg8cH5pbO6roQTdkVtH0Fi9ODS3zP7OYD7INrs2r1qvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
این کلیپ رو چندبار ببینید و برای آدمایی که تو طبیعت همه چیز رو می‌کَنن و میخورن بفرستید تا بدونن یه قارچ چقدر راحت می‌تونه آدم بکشه! اونم مرگ با درد زیاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103072" target="_blank">📅 16:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103071">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf9b4001ac.mp4?token=bMBWdkeXz72neeiNwktEe7LdmLgXY29tSK5h7H7YGbOh0lXgkFDD7Dt6XGwJWBUgWLRVyTcyhPv4FQ0AQrse3iRLTMQy6Xus2QvQMpN5Ujyyu6whKjiC3NK3hohHJgFjJrW0QVj6GjT46TRA-FsRKj4fz_8GpO_qFUKi6BZaV6OJaNAJTV8wgVJGOkJb6f-MhmfcO34WsDZDm-NbV9OW6i1pBJ6OmYxwiaJ73qrb8C-Y0H-j1lWG8BEBmxgtnpYDQIku7pzV1gNfouZQCExr86FjnYly4KKYRM_29m08lJgz0ajcTVyWGiAOGWR8JQV7H6_0cLhO3TvvYmJ877M_gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf9b4001ac.mp4?token=bMBWdkeXz72neeiNwktEe7LdmLgXY29tSK5h7H7YGbOh0lXgkFDD7Dt6XGwJWBUgWLRVyTcyhPv4FQ0AQrse3iRLTMQy6Xus2QvQMpN5Ujyyu6whKjiC3NK3hohHJgFjJrW0QVj6GjT46TRA-FsRKj4fz_8GpO_qFUKi6BZaV6OJaNAJTV8wgVJGOkJb6f-MhmfcO34WsDZDm-NbV9OW6i1pBJ6OmYxwiaJ73qrb8C-Y0H-j1lWG8BEBmxgtnpYDQIku7pzV1gNfouZQCExr86FjnYly4KKYRM_29m08lJgz0ajcTVyWGiAOGWR8JQV7H6_0cLhO3TvvYmJ877M_gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
روایت‌جالب‌پپ‌از معرفی نیمار به بازیکنان بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/103071" target="_blank">📅 15:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103070">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be22201896.mp4?token=QQhBZFErOiWhzZ-dlvNl9Mz40In37PxmuIGQnm8o3Cs_Y4x6YLBlGiRMKysa9_CH4To0M5UP4F_CnnwKn_JKr5PeXQS6etugxehVJyDduNiVwg24vks10gjjfCroViZBj9h0miZYfmk4fA2lu9mxicIexEHIttbI_AUBi0v6EX1wugUZCK1r4lYlT6491zJdP5-96DDcwn1hXLNDAilNQLyAQO65k969d9E08sn7gZPijss4m75HArU8TQjKZa7bejKbUDBThDr0SOvaeotdpIuzbN_0EaCUY_x2TgFN9OZFFdzSIa3ecmxTBm9x8_O8qZ-8GcW7QD6FVrN3krXbeb-hVqi8V5jkF1AlIVnBL24pVCMEDXPJIGr6lnnl1vryZk5pEywmPzWPB91Bgjt1l2KoRoE1SNoBds5E6LZu9bs6xcf2Ih-ZWH0XPyqfo7Ff0Wqb37EieZ6UF1gHJvNQ2we4gEh6DEOmaq8Tl9KdOKlMkhxzNTIjsoLoWwZByi-RRzhiQwGcJYW_48IxBobVfvRKq98ejj0V54u565J1iT4NAEp_WIN3hqwU-tGRn6XtQJOY9d8K-oT3EidIdYP-bglEXG4L7tsrKanPKqVEoYkZNVg0Pj9qm0XxEE9SlC41FVUoxJGTWEyRY-3mYl4u9Mk3GeD-lWsRG8ALIh_KO7M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be22201896.mp4?token=QQhBZFErOiWhzZ-dlvNl9Mz40In37PxmuIGQnm8o3Cs_Y4x6YLBlGiRMKysa9_CH4To0M5UP4F_CnnwKn_JKr5PeXQS6etugxehVJyDduNiVwg24vks10gjjfCroViZBj9h0miZYfmk4fA2lu9mxicIexEHIttbI_AUBi0v6EX1wugUZCK1r4lYlT6491zJdP5-96DDcwn1hXLNDAilNQLyAQO65k969d9E08sn7gZPijss4m75HArU8TQjKZa7bejKbUDBThDr0SOvaeotdpIuzbN_0EaCUY_x2TgFN9OZFFdzSIa3ecmxTBm9x8_O8qZ-8GcW7QD6FVrN3krXbeb-hVqi8V5jkF1AlIVnBL24pVCMEDXPJIGr6lnnl1vryZk5pEywmPzWPB91Bgjt1l2KoRoE1SNoBds5E6LZu9bs6xcf2Ih-ZWH0XPyqfo7Ff0Wqb37EieZ6UF1gHJvNQ2we4gEh6DEOmaq8Tl9KdOKlMkhxzNTIjsoLoWwZByi-RRzhiQwGcJYW_48IxBobVfvRKq98ejj0V54u565J1iT4NAEp_WIN3hqwU-tGRn6XtQJOY9d8K-oT3EidIdYP-bglEXG4L7tsrKanPKqVEoYkZNVg0Pj9qm0XxEE9SlC41FVUoxJGTWEyRY-3mYl4u9Mk3GeD-lWsRG8ALIh_KO7M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
روایت احساسی خوزه از ساعات پس از فینال UCL و قهرمانی با اینتر و تصمیم برای سرمربیگری رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103070" target="_blank">📅 15:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103069">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/772fba48c6.mp4?token=ZJd8uSdBdhkSQju2mr7JJxS28sjcV9kV5wKMi-_jAbcOjcca0vtzvhf63puoTPefxxKlXXZnh9F-KPWtp0fOPmzVeoNnDDZUSdAwBkKuX13iY2mnbEZpU-I0BKwSNlHOgf4dqZsW06yPoFiNULt2zgcbdeM61ZtfN4g90E2bSllyk03dt1yzq9ZKMfjr2gmvunePzr1luyXLbapYANpy-6os39kqyx5lewVN7fhv0-c98AfRGVYuXKzzOEviLYmbg9j8jsIozVNbqE9YOe04J7HTBB5grX4iFRiZKN-riqE3vSrdVI2hl33m9OtEBBLhO_LGQA9whFpBOqQf0wZRag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/772fba48c6.mp4?token=ZJd8uSdBdhkSQju2mr7JJxS28sjcV9kV5wKMi-_jAbcOjcca0vtzvhf63puoTPefxxKlXXZnh9F-KPWtp0fOPmzVeoNnDDZUSdAwBkKuX13iY2mnbEZpU-I0BKwSNlHOgf4dqZsW06yPoFiNULt2zgcbdeM61ZtfN4g90E2bSllyk03dt1yzq9ZKMfjr2gmvunePzr1luyXLbapYANpy-6os39kqyx5lewVN7fhv0-c98AfRGVYuXKzzOEviLYmbg9j8jsIozVNbqE9YOe04J7HTBB5grX4iFRiZKN-riqE3vSrdVI2hl33m9OtEBBLhO_LGQA9whFpBOqQf0wZRag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید چقدرضربه محکم بود که یارو با این هیکل پهن شد کف زمین
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/103069" target="_blank">📅 14:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103068">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URt-caeqrpnhGSpRIDRRVrlH4-J2U5pPHeicui7bqJjELyaKd5nCty6z1lBe-l9EbYyn2rKEftNXl7-NsTQOCAyxbbfyVdDlbkLXrvHulub-OSUaCZgZGiekjdEU8_k6OTUGMXwfGD1yq9Ahnyx5Pm-p7v_AzL2f8Zxk54P-RaKRxGO5SQ1AhWvFDZKFstzWdfUb_XBL9pUSvLgAC666TbwaoT_TrMHyFdGVVSL1Fmd4jprcfK4D_g0e_yHtlNbUQ8kyl5xGYMZFMX_UbkkE9ScUv5auDIqpnY5qGIw7W5voSfEbIMfFi0iRhk9RxjwILw3rl8UlXiRNbuS-7J4bGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
نگاهی به آمار گلزنی لئو مسی در بارسا به مناسبت پنجمین سالروز خداحافظی او از جمع کاتالان‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103068" target="_blank">📅 14:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103067">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hi6LxbqHaAzcqdQ6iZfWaqM4i27dOrR9b6kdvgA2KNIKCeAyHQltWC5imBCgzQSZVWbdmEesAAcB57G61IhevuWbEVtjL0cJJ2S1zEYdw2YVpfSvj3XziPc9UNuObhuWlqyM90Mu3VAtWTqNmYvaRFD9H-SmZe2IdYe_aD7uqTTSIrb0wNnx_lWiRYhhm5HUFaEDLFVYmzVurigdhtEOTDuDN74KiwK8s369SIbHt7ntAEkoNfBcFOI70yihyNqAAuOhIe2-SVoxy7WumgCQjVLNJS3Td-ST4tVmVZ5gKx3njeC0umnMgpAoAu0V80iovQhkx_igWEsj-P8Vf4KK9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خورخه مسی، پدر لیونل مسی درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/103067" target="_blank">📅 14:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103066">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bc67d9626.mp4?token=uq96XRIpVfLtwe2sa-U9kopC_OcKWA15CxHqGr0cTHwTq6x20jVMqQPh7tWRCwLTsPbxX7S_8XPwG8LK9BF7o3ibCUWsJkS_95eosif958NlXQhl3-tF1Wgu9oFtV2GSFaprZyMF2PIn65Hin8pSKUxetpzrXcUxy6Ve_l9xoqFflN86wmYGNiJOgz5uqIs7EiljkaRNS3LRfuDsis6eRE-Pm9O7IkPmR8IGe9d9NawOBZNQWmHSczN_mBKtr1vAqaS2foCMqTAhJCk1KzDGaftmwH4YACMYXGMZajgQokFKsbwqbG2O6y97biIehWiiZja9tGXKiGHk8n_fkLOKsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bc67d9626.mp4?token=uq96XRIpVfLtwe2sa-U9kopC_OcKWA15CxHqGr0cTHwTq6x20jVMqQPh7tWRCwLTsPbxX7S_8XPwG8LK9BF7o3ibCUWsJkS_95eosif958NlXQhl3-tF1Wgu9oFtV2GSFaprZyMF2PIn65Hin8pSKUxetpzrXcUxy6Ve_l9xoqFflN86wmYGNiJOgz5uqIs7EiljkaRNS3LRfuDsis6eRE-Pm9O7IkPmR8IGe9d9NawOBZNQWmHSczN_mBKtr1vAqaS2foCMqTAhJCk1KzDGaftmwH4YACMYXGMZajgQokFKsbwqbG2O6y97biIehWiiZja9tGXKiGHk8n_fkLOKsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
سطح‌تمرینات تیم‌های باشگاهی آفریقا رو فقط
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/103066" target="_blank">📅 14:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103065">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8QroAxJljpO93OXIrlwCXyx3GmCux4a7OCu59KsJrJQgPfzZEZzN2UcGK6GwHznmg9zhcRfQ74caV4897bKUwiBrj-GKau3lkUFZTfdAEM5xFJKvwJOJLI0eFxWb5_cgS2T_sPjss2_xhDyoPqDXQ5s9V2uN9PtiFTUQa6iK_ZM2SpleNOu3x-1gZveSfZEbCHY3XfDPydnjqnO86pjTUbDm5YQk5vgXGdHf6OFffh3UTGTuiE7hN-IB8KJpai50sduiStZGBQbxW-IGNe6IIipQrP4T5LA_EZ1NUL5wUMFThXzU9xAwEZtyfpK-wfQigA5y07YPtKm2QeWHzo2sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇪🇸
🇹🇷
علی‌ناجی خبرنگار ترکیه‌ای: پیشنهاد ۱۲۰ میلیون یورویی اتلتیکومادرید برای جذب ویکتور اوسیمن توسط گالاتاسرای رد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/103065" target="_blank">📅 13:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103064">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🤯
🤯
🤯
🤯
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
#فوووووری و برگ ریزون از رومانو:
🔻
رونالد آرائوخو مدافع بارسلونا با عقد قراردادی به تیم فوتبال لیورپول پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103064" target="_blank">📅 13:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103063">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e15d33bd4.mp4?token=PN1hT7lblG6m8WjKFu5qAkYe9LBxNCL_P3wS8UIYizEylcEPvRDjTtb4ZuTpVn3NrDmwayFePvat6A0oBASNKAf3mFxZPlXa8FQxZjYVSJ3KowpSqVhyxClmw2hP-vYwBfdxyHJb7RGkBPom9rWELA9VV-Uy2bqAbAmU08jD_wW6zAxPENln-niC7-9IjOyFlzVLof1zIOWGK0DUEJ68ZhvgbR9_XMo2zj6aaFIE989ndWQZgVu5J9zqiBpX1IXA_wd0CUIy1POlCYxSeSIrcJJdC1alQ3JCJ250utj56R3K9DBSMfN_bLtZUTrS5zRJ3ueV4Y-x-QA1f_ifIpxoDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e15d33bd4.mp4?token=PN1hT7lblG6m8WjKFu5qAkYe9LBxNCL_P3wS8UIYizEylcEPvRDjTtb4ZuTpVn3NrDmwayFePvat6A0oBASNKAf3mFxZPlXa8FQxZjYVSJ3KowpSqVhyxClmw2hP-vYwBfdxyHJb7RGkBPom9rWELA9VV-Uy2bqAbAmU08jD_wW6zAxPENln-niC7-9IjOyFlzVLof1zIOWGK0DUEJ68ZhvgbR9_XMo2zj6aaFIE989ndWQZgVu5J9zqiBpX1IXA_wd0CUIy1POlCYxSeSIrcJJdC1alQ3JCJ250utj56R3K9DBSMfN_bLtZUTrS5zRJ3ueV4Y-x-QA1f_ifIpxoDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
یامال این‌روزها تو کلمبیا نقش دیجی‌ بازی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/103063" target="_blank">📅 13:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103062">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgbhzJqPrX74wrz2HPqIREggU6ZK_cQNkz9DW7IV_YRrx7FcmA7BiIJ796RdFTsXceQ8n9USxCQYE0mO7oVNIix_j6W1si2kRWQMTqf7ojLvZ4jANg9F1kMPSiX3tsc_OYFJzO7YYX74VV_UcnuNvRWaNi9kmmGwY0MQYuMZkxEVSUy8nxXJJTldC9FyzS0MWzXySZYshdbGovV17qXM0ItA5bDOd3oO4yWl5xn4H73sTFDUkQbEGCzQOINdnO1Uz3Z9_6nqETk7cs6evb6Q8eOX2kB4cwhKsWo2RSw2Wj9eJFtVVLiApu4ZmnDIfvYpAnRPQK_HADgB4_9M5Xke6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📰
افشاگری‌عجیب فرهیختگان: موسی جنپو فصل‌گذشته به ازای هرماه حدود ۱۴۰ هزار یورو از استقلال دستمزد می‌گرفته که در تیم جدیدش در یونان این رقم به ۲۰ هزار یورو در ماه میرسه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/103062" target="_blank">📅 13:06 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
