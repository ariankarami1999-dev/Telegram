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
<img src="https://cdn5.telesco.pe/file/n4rxAIpbi3a270GR_k1zoKXdIz3ujaV0dzUoEYW-anVbR6QjJl65uVGEdk6LbzkoLfEbYRdxKFxHUa_IcuhfNVflWoLbLu2rUNyfabDQMPaPRAOI6ej8tNVELaZe7s24YyMwkzUvFBxooNWFCsFQwI4JjhZHYJWlo9G1VnT1HRVDh-G-nLg7xjsizSY_cu7tMcdOpNCE9TropFn59btkKN69_L7eu0HeeXBQOTx3PDlDru8ke-wlr0QfJQh593kYGt_L0LqStJ_mJulKQipr7zTzpkmgIDRAsZo8h8gQ1cSWS8P5ypM9SkSZhhsDWlE0GCu3dgX4tVj4ACtnIaFALw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 389K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 02:39:50</div>
<hr>

<div class="tg-post" id="msg-107981">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JIfzUVShNmXMOQr899369nPXpYDEUvo_0Dq3WOFQmk0xCfKK6h401QMG0vPuyE-KdnziG_OmTETRsAk6q9YyqpHbxLCClhUbc2P9MhUtV1sqXIke-RnX34V0eIw3ByVVK3B6NoshjKDgyVXp0mGNg2I8G-Hz1s_gxkciqX-sWdcZZgB2XfU5u3KsEnit3R5O09bIKhevGhXjMKmF57pkKh3rdADQIEQz4gavdM2zmZFSkX6QjEl42V7VEfl8ITkrFllPaYP7aGj6F2a2b4elH46LTP8FG5CFSbMLvoY4PGQ1aWsO9s4sL6LLm_wbqfsRAbCU513DQJde9gdpbW1CQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OeyBH-g9Osr3rbjOZB5AWY8XcU9t3mxXhCkvAPu5dasDFujmPHno-9QKmowgpUT1i79v6JDVVBH5GG1E9hsjMWKLBNPptQyBWyyVr2qU-ej3SyFieofcWvCqQxvRnQ4wj3ezHJoIyyYuLfmvWOIphnyvN0iLvaDLSPFJNbECv0_H7W9pkxoIs-lyobDip3IBaR4ghtHLi62X0EYTAq0GkvEkatF7iP-Gw_60TKHY02wpmPYh2NbS00gXrJJZcTBhuCtzL0KVc0ImsaVol17hFdrnLeeGMyxY6nl77lFgSwa3oXTcqPSKUf4VMLy4PLDu4bNbpD2PKH0vpr0Za72_kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😭
😭
😭
اشک‌های دی‌پائول بادیگارد مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/Futball180TV/107981" target="_blank">📅 01:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107980">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abf74e1898.mp4?token=e7hsy4ERrCL9RHGH0MiFCdU5LF5I_H2RFAT2vVSzZzssuDiZWBsgghGMlxnOvxE1tcGe-sA6ChX1Hg6KxcNB4Jo1F6r1Zo9yPpe0mq7jaJ0uC5dwUgXSwtHOCKlFp6RZXQ_jWg5HAunqGaJogOftVQ5HTR1CHVMDs3paGI1PkVlLFbXEW1bnq27894X-azOM3FwVPlOp243vmyImiNaaZy1zTPWfLXwib7HjPloPTqpuLCAoUFZ4MbdDsjIz2T-ir5PrH5mvOmv-Iqa02N0TeNkJ6I4YUY2kLFBQR1vP1FLCfnV4jIoGGn3DTJ9i4PdX5TMigicqsh6acybE5swqwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abf74e1898.mp4?token=e7hsy4ERrCL9RHGH0MiFCdU5LF5I_H2RFAT2vVSzZzssuDiZWBsgghGMlxnOvxE1tcGe-sA6ChX1Hg6KxcNB4Jo1F6r1Zo9yPpe0mq7jaJ0uC5dwUgXSwtHOCKlFp6RZXQ_jWg5HAunqGaJogOftVQ5HTR1CHVMDs3paGI1PkVlLFbXEW1bnq27894X-azOM3FwVPlOp243vmyImiNaaZy1zTPWfLXwib7HjPloPTqpuLCAoUFZ4MbdDsjIz2T-ir5PrH5mvOmv-Iqa02N0TeNkJ6I4YUY2kLFBQR1vP1FLCfnV4jIoGGn3DTJ9i4PdX5TMigicqsh6acybE5swqwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
آرامش‌خاص و لبخند‌های لئو در حین ورود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/Futball180TV/107980" target="_blank">📅 01:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107979">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uL89O6aZGuytaMldxL3nS_cc73r43jkHqmd5KJCwo7sI2rRHWmbdorrJN2wQ3QF7xRFEUOIpK-OjC5ZjyOTquP-SXDE3Y9y-bDRkG9VCxXh__MAlpkACcBU6_7A11U1PkXsgz1vVZYUGd80-cipV5mYX-_0Z_kDHz4XJFrxztKcg1-xhJfD2EqKqwtgGvi95SwgRfVf6zPaLuft69PHIEpJ5UwnUTLN3porQQx6bkNyTxIkk4UkXE3rIbPVTaxcjenppA_HNhg_ObTeZPe95oM7RD7KM2u1HlgnLfFzP-7N852CvV8mtbuMk7CImIe5ztCMpQtiUNyPOu5IV_3ImhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لبخند زدن هاشو ببینیم
🐸
🐸
🐸
🐸
🐸
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/Futball180TV/107979" target="_blank">📅 01:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107978">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvGNSJ5RvHSZF1jupKTDiUjQh0Jma_3k7Ufk8QT8DK6n-6eogJLwoeYu7arBaj_RgD5nf5R8sNdDZyVEhATjLPc_Bp0VcTMEw4GYhOjm8IIHhHNwwWEgtO4bK8U0IT_SSePGun_kZRg0IR7Gw8zlln34_ZPHNRX8ESF2QsU9Ly3WXvwJshEjqPp4NXuGOZyry-2B8lvHsl7ee5Cx3-MCJkz-LFIZnpxIyzRoFbCa0JOZLatUqNesfiXOdab8qg-LB7WVE2n38N2fl6yYzEDCk9Tiun1i_epeww-uLBzNCqXRclfWSKIcaRPj98l6AUGliIrEK7xoWWJyofylEqxMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🐸
لحظه رسیدن لیونل‌مسی به استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/Futball180TV/107978" target="_blank">📅 01:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107977">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0rzl4DMct1_KEgmT8sugGU3GmlNYmHTBZ9t-IVs4eMisE-O5NBpjlRycX4R07A9Up-j_QizRsL990xU94bDob9fnTJ015AEQyRO2L6fCFqOejiNqIILwlykKevOSsCfcfQOeEII63bp4LiKQbfjHblilmCdmIKYj1yFMq1N3s_cGxKKBGbAwQf6ZPOr5EgZFFJhF7ra-BI1cdpghfwx92ycOjHn13lscoioceWA71ioRwKhIaA2POOTbgvFSBMxqIZcR88-DOwU8F48X8DhanjqmbcCtgTl1rGoGzrrpcgd74FCiCSWyG9MaPMe2_To_jZyiZ8G6esDj7xfimGdMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
نمایی از استادیوم مونومنتال آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/Futball180TV/107977" target="_blank">📅 01:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107976">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64dbdaf83b.mp4?token=gp9BiivM69e6AWyQNDUz9uJw041QTIk2zl-Hz79Uo6dvS2po_tBlmkQkR7RLxhGwECFvsVdroAWVcOhvUhoPqra3yjix6vyG5O7atOSWqbVxytbYmk01UBRfiL5jJb_DtC-ec3LnpEPZiWs5z58KnPNZaK_bGwaRxqsPKC8OMv6FPrOaSOhdO0Crc0QU34QcIIEtw1dLy3h0dF-oq3zxswBcnKVblG3nsOqszszk_NWrfc5_j-xweXxVdIhQCVH6iT3bbH920IbaWagzrCt9sPGhM9N2MTUF5auXOVK8LseweJVyGC1vKg3wOaiXD8JhmVMMZ0vYJ6KHfwcuRXhwcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64dbdaf83b.mp4?token=gp9BiivM69e6AWyQNDUz9uJw041QTIk2zl-Hz79Uo6dvS2po_tBlmkQkR7RLxhGwECFvsVdroAWVcOhvUhoPqra3yjix6vyG5O7atOSWqbVxytbYmk01UBRfiL5jJb_DtC-ec3LnpEPZiWs5z58KnPNZaK_bGwaRxqsPKC8OMv6FPrOaSOhdO0Crc0QU34QcIIEtw1dLy3h0dF-oq3zxswBcnKVblG3nsOqszszk_NWrfc5_j-xweXxVdIhQCVH6iT3bbH920IbaWagzrCt9sPGhM9N2MTUF5auXOVK8LseweJVyGC1vKg3wOaiXD8JhmVMMZ0vYJ6KHfwcuRXhwcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
😭
استوری امی‌مارتینز از سیل‌جمعیت اطراف ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/107976" target="_blank">📅 01:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107975">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbdff94ee.mp4?token=Og7Nl_6B5rsJt-0hIjsN8MoDibiwQVElWCjBfDHC2_goNNaUbE1fgcQNnUbydyI7saW5ZXXbolmt8H_pD5_1lw4tt4MG7Tj3mjpMRR0vWoB6DxD2bHOMK2pGFSEvP6PkKekfx0maBnlsVsCkKSxxko7FQ2rru6LiPFhBHtcPj5rk-WyZzK8C8TF9nHtDxEBMnOpGYvTo0oPA1H0GLbUxxWjVNJSAepQS5NYviW5wPZodFH8ESDAQetIuDfcI7u6278dU49fz9u4a4lv_LXtTlTrJu8Zdo_82eclXkswF9G9ygR7_AFBwolL5cGfl9bJlMp994Q4lDQCkk90yRkR9kIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbdff94ee.mp4?token=Og7Nl_6B5rsJt-0hIjsN8MoDibiwQVElWCjBfDHC2_goNNaUbE1fgcQNnUbydyI7saW5ZXXbolmt8H_pD5_1lw4tt4MG7Tj3mjpMRR0vWoB6DxD2bHOMK2pGFSEvP6PkKekfx0maBnlsVsCkKSxxko7FQ2rru6LiPFhBHtcPj5rk-WyZzK8C8TF9nHtDxEBMnOpGYvTo0oPA1H0GLbUxxWjVNJSAepQS5NYviW5wPZodFH8ESDAQetIuDfcI7u6278dU49fz9u4a4lv_LXtTlTrJu8Zdo_82eclXkswF9G9ygR7_AFBwolL5cGfl9bJlMp994Q4lDQCkk90yRkR9kIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
جو فوق‌العاده استادیوم یکساعت مونده به بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/Futball180TV/107975" target="_blank">📅 01:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107973">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZN5Twh459Q9e_3m1cHhtyHt_VlEMVtGQmk-QV9JUO7A3rIsHKJV2KaD1wB74FoXbl5XN_NQYutvGlFJnP-ptkgF5icn7sJ6iR0N-TOSlplMBSLUHUzhTJyNPvXHkhRG5_LwQAAf_R0nCCZZMRpNcuGF5hZ0FzPhQP-ET2ChvCK_bnwEyOxsCRc4tWIM8O0My9E0PSCNFYGsvdFJmhSwkzQ73aableMRMmwW5rfE7UWy5upzSRDT0EzXNJclAXEuDboLKmQQ7128g5R253hz7ugvzRZbeK-JY96QHgwmuEgMZRJGytf-Pueenu5UK8dK2HpyTRtNDGYRMiNcPUIzcZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URIIadWTPZrdXt02PCP39SGDR86XEYisZsPNnROo9-Z5PPI_gFZe9_qT_-PRWfSj_CsFdWi3wYACtRhQi3cUO5bM6e7Fd19EAyShtjNPhLncOAefQnPmwLfL-vtPxM6WMBPVA8NY4RBI5SZj8UsLFb5jllcFn2v5X3lyaHUpQhu5rgAmAFeLcQRDKNMvcaV3msgKD-agqQ8Ym9P93jacgRQ-PSn1Wvy_PcoNJ1ldERuIovFYonJoNJ5Mi9i5krbXsIpo7YzssxfX06wmAfPrmDfY0U2YpYNdqHyTA0sIPNBbtALEO1AjkNv4IZ91icCU1gJR9e7yU718Oymlbe4aHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تغییر عکس پروفایل آدیداس به شماره ۱۰ آرژانتین
همه اکانت‌های آدیداس در کشورهای مختلف، عکس پروفایل خود را به عکسی از تشکر از لیونل مسی تغییر داده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/107973" target="_blank">📅 01:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107972">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اینقدر غم امشب زیاده که آدم رمق پست زدن نداره
😭
😭
😭
😭
😭
😭
😭
😭</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/Futball180TV/107972" target="_blank">📅 01:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107971">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qVihbgWdk_nkwjvtffm6TuyfXePwfM-8apmMuLTSEmHhkDvRhcLsSo47oFLh-Xdg8QAHqYtCgMeatDE5TxKuco_2XWKta7HVu-5Bp92Qi3rFRKPQLPseO4004DkEtHqs3dB1dtAnAWKY1h0yN6Ok2E-536QDOUsA67dkYMasLyhlXfxTpThlgfkTBJoTuZ_ltb5pO0wjjM_zhna4ajfdSvIa5-TogG1BKd-GBJJA13qgG8z6fgTWPNtAO8b2i8sVyAX4mneK8pEqusGTKgYMTYix_BwcQFDZoEDx93-_YJxWohaSAaQl7tNLSXk3fgXe3q-5y2YDigTNFFs3vWrClA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
⚽️
The Last One...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/Futball180TV/107971" target="_blank">📅 01:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107970">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDkKAXrit-ypZHBNoUqWmlODqInA_neFdwy8v2Rkedv3a9WHkXHuNHzxluKQEHQ6-xqHjPKHmpSDsIThsbHd6zpVliZY6513AFIMlIDcupxKYodsUMd7fwUmQDpKbmqSQ0srlYt1NaLRBVPk428C-tXpH54hXix6ZdlbknCmcyPe46WYCaTcczCj3L_qbEHBLthtcIaxE9Dd_LYRwZXyi9SlDTmu4sHLZ3K-_PlTBfWBe1Payoj9-1PSkVsn_NPqt0wTi30CGKEZiqiO16v_qWsbP0aryEuaQXCfRmZlPynDPy1LJ5cz94A9EBjGYXwIB_x2WvpzlM84a90ZWIqzjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😭
گریه‌های لیونل‌مسی در بدو ورود به استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/Futball180TV/107970" target="_blank">📅 01:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107969">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wge84qMM5ODe6M2_CXuccHKkdEgRn3f6YhdyYk0ZSiW_bUEPJBOnEbEGC6VoxDN2rQZcN47Xq6oCVgNnN7NTQbLXpJPb_CF8IN1hBbwCskYYHChlEkrWvx9-njp1QB9HdWLs8dbxl10yKwTJGbZzoHmeRwDCip8XmkM5p-MzQgqS17TkCl1Oe5vXt4GDgKFIS2jDSAFZF1hYYUrN59VjqYAu_B9rfeEaMc-nxxippKDSIlcjkPCn2It8Nv6cvDbi9H-u6aGHlosHV80vP5akveSVnnI_pFN2y-zr0PjnDptmbDYjPX6HDmpeKqMuZ6sHElbq06hep6_E-Ad_VbxYsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😭
گریه‌های لیونل‌مسی در بدو ورود به استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/Futball180TV/107969" target="_blank">📅 01:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107968">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRXD8qyjH5M61bml4J7QBa7W8tZiOw1LgQ1e-qDd3dxz7GlcQISvmy_qPRK0tgZ5hm7C6AMZKshlfvrZ29H_4cQtNgzGFfvMa_rjxA-fZqrYk3t7seKW29xBenPU4EFSdy8eaDo6EHyb8LdaMESVC36RBW7VOlGzqGqyTmUK3U_hLs_23Evsdl_rWaskZGfZuKjuUDPnQ8y_UhIp4-sLam0aO02BNdfBfUNFK3lDIhPXN31W7ihw8R9FTHHuDUQzzQ1S0wCxwiFPXr3o0qZk9mwH0eG2f_AYCBvEPoo_C-DRIHBxtJsqR8GxRk2wtC6VcgB5MYh-MDVG4tigy6_qLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🐐
آمار فوق‌العاده مسی در ورزشگاه مونومنتال:
29 بازی
⚪️
19 گل
⚽️
11 پاس گل
🅰️
30 مشارکت در گلزنی
⚽️
🅰️
✅
هیچ‌وقت مسی در یک بازی در ورزشگاه مونومنتال شکست نخورده است.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/Futball180TV/107968" target="_blank">📅 01:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107967">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577bffe68.mp4?token=LJejC8ImA9-OQI_A0lqFr5e0ubiNCkfwP14PRMEBa0CVRB_h8Pp3q82Rg4aRcicPISAFMiFsZ48BmAUzXyCGw3fL-EgQ_P0FLnycu5Q_raQamwmUGWWD63vJOmsbhSVLcyUL1AdW6xYAGJq2J_BVxpbWxK04rIwjhE2A0-Am1qVB2K1Ez-obnyy1t4Nj5hBri-2plC4SbVXei7mfqsH4PyTlyA0MsijUodleDRcv-e_pSCbbVKD9j9EuS4jjtDqHrJRAp3FP1aU3U1dOSZCOXOrOD3Ywn6hUK46Tp9Q-TtqCz-waCFe1OscdQwVtEAz5-WAOTMVn8GLEOwn_VrFfGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577bffe68.mp4?token=LJejC8ImA9-OQI_A0lqFr5e0ubiNCkfwP14PRMEBa0CVRB_h8Pp3q82Rg4aRcicPISAFMiFsZ48BmAUzXyCGw3fL-EgQ_P0FLnycu5Q_raQamwmUGWWD63vJOmsbhSVLcyUL1AdW6xYAGJq2J_BVxpbWxK04rIwjhE2A0-Am1qVB2K1Ez-obnyy1t4Nj5hBri-2plC4SbVXei7mfqsH4PyTlyA0MsijUodleDRcv-e_pSCbbVKD9j9EuS4jjtDqHrJRAp3FP1aU3U1dOSZCOXOrOD3Ywn6hUK46Tp9Q-TtqCz-waCFe1OscdQwVtEAz5-WAOTMVn8GLEOwn_VrFfGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
زلاتان ابراهیموویچ برای تماشای بازی وداع با لیونل‌مسی در کشور آرژانتین حاضر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/Futball180TV/107967" target="_blank">📅 00:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107966">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b38517c17.mp4?token=VFg6ZO0LacrbYVfgYV5q1duEj84Lfb-eFqDDNYWyd7AYv9QiVPKc6vEz7jq4FRMOaQ7Ltn1e0qr3Q2bbR4MAvUkevUS7zAtwcqe1IpY1IlHzqyAtENvpKNqGBGkgWNvniCdrYSxMLi4ENnIeEwW_da5ssbyPcZk1_TWjTe3nOT8A7yPb3iOcZl5xlMzpxnZJ0WfV9tIuuAOsPR0cQ5Iu1cgUMXQ8pk578b_GCxqkkdpdd11ScDoDYCsB4HenzcSZFyB7zvNqRdwY-9DcaiTZYDLh69qZ8es1f1TgwmEdv4CfvUpTOmN4y9C_Mr26uPoZ3EZ9OYn-Ony2VaPL0reGog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b38517c17.mp4?token=VFg6ZO0LacrbYVfgYV5q1duEj84Lfb-eFqDDNYWyd7AYv9QiVPKc6vEz7jq4FRMOaQ7Ltn1e0qr3Q2bbR4MAvUkevUS7zAtwcqe1IpY1IlHzqyAtENvpKNqGBGkgWNvniCdrYSxMLi4ENnIeEwW_da5ssbyPcZk1_TWjTe3nOT8A7yPb3iOcZl5xlMzpxnZJ0WfV9tIuuAOsPR0cQ5Iu1cgUMXQ8pk578b_GCxqkkdpdd11ScDoDYCsB4HenzcSZFyB7zvNqRdwY-9DcaiTZYDLh69qZ8es1f1TgwmEdv4CfvUpTOmN4y9C_Mr26uPoZ3EZ9OYn-Ony2VaPL0reGog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دویدن مردم آرژانتین همراه با اتوبوس لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/Futball180TV/107966" target="_blank">📅 00:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107965">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L47K0D12YSCG7qtnzxkYd4e_rACli6UxacxTDFZDySAtokBizDHC8IOzGwu3aajcQdaK6jihwEbMXOjE7wJiHCZnBKlQa6s9ThA19tJBrLtZ4hWAT90a8luhp92Je7PW4XmrHo3aX_WAc8HLvEbVzWFK5dDrZrly8BdDxx9J4F4LGL7hx75fOw4afA9pXcpldnsDBBDbRiBBk20EQ1jyEWp1svBd5opiFIwBHKJYZ9OXi3i8aOIJDv865sadNUwAGgoJ8SuY2PkeqUFaqW2LxDhdx3dnkSv8Pz6phQiWd3dJ0WzzWVbHuWQdGE0v-Ju-ZrA-6YAV_0cbJwyfmEcD-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
⚽
رتبه‌بندی گلزنان لیگ ملت‌های اروپا پس از پایان هفته چهارم:
🥇
هری‌کین — 6گل
🇫🇷
مایکل اولیسه— 4 گل
🇪🇸
لامین یامال — 4 گل
🇫🇮
لیو والتا — 4 گل
🇮🇪
تروی باروت — 4 گل
🇸🇪
ویکتور گیوکرش — 4 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/Futball180TV/107965" target="_blank">📅 00:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107964">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oyKnvRIVLHxB9X8jxHter2-QSkhicOO2CKfJj6XgY2tac7ANbAadZ8FW5UZldHdnJCNXiHvlD5gLYunUtKJncRRUlHqakdQyGkkklZM5n4tjuHu8HnMAuwKZw9WJ98ElqDQJDVQmYbnUZcB4hhzdrCCNxIzgJ0aOB1u6qDc3lHRIelwUdZA6ccYWf-u7s_u9EY4i51nIApbooyQ2GHKwFkuVWST_qKt5mV6qdcOP-1hZoq1IS5cWWhiag21cAckHiP-dkxsfxWAKqGXa2rqyYFHBY0d1hE6XfUrzy6cLnEFG5rdeXeLgmErnFRPNx9YE1ntY4H2lhJYOeY_m_xKBcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسطوره در راه ورزشگاه
😍
😍
😍
😍
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/Futball180TV/107964" target="_blank">📅 00:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107963">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=cKO9bfp4rKdUNzEhEHrgwUovYlmVhImKfh2Zili-3OgtNAZ7NrICooKiniAZnmoCgRajRwHmeQ2ISmDyGP5NmG5BeHRmC5XUZTt6Poxnuc5nSgHx3SlB2DeAcbrIBcpgkANO1-QUsziqspHhTykXoDUjViiGSaM9L1raiqy1DFOzNCosZHFTrW0Fcv6jw46djAwkFWsD452jHnFpS3dqPJOXrlgn3orthXXUIxQ6DWyMkWqgw8i1WwfM-gKtrjqoHxek0kYSRNRjydQCgjBgZCvvcjsMLOHLymS14SKlbfzvTIWo9jVayNQeKAEmTEj6-Qz-pXJlAMAQi_LqeO1pxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=cKO9bfp4rKdUNzEhEHrgwUovYlmVhImKfh2Zili-3OgtNAZ7NrICooKiniAZnmoCgRajRwHmeQ2ISmDyGP5NmG5BeHRmC5XUZTt6Poxnuc5nSgHx3SlB2DeAcbrIBcpgkANO1-QUsziqspHhTykXoDUjViiGSaM9L1raiqy1DFOzNCosZHFTrW0Fcv6jw46djAwkFWsD452jHnFpS3dqPJOXrlgn3orthXXUIxQ6DWyMkWqgw8i1WwfM-gKtrjqoHxek0kYSRNRjydQCgjBgZCvvcjsMLOHLymS14SKlbfzvTIWo9jVayNQeKAEmTEj6-Qz-pXJlAMAQi_LqeO1pxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلاصه‌ای از دستاوردهای همتی در بانک مرکزی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/Futball180TV/107963" target="_blank">📅 00:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107962">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUxhDj4DiQfLQ-1cnF5zfRnKgrv_7aOSDY3ApHS91HVwpdpPhXK-sByxno58sXzjWtJf8c40_4NWmq21XrRsSUQkCsCOq7kAlYa2yYthRO_9e7bpM39aRhE7xFqcCzSZg-woU8KHDCKpqwvtqxCw6IkxDETNVYuhBF89-HKYgGT1fIsp_HoJTft00SCQM091UV401UuS3p3jNIhsWIohEpt5OY5rjjDahvbs3GNB5cbVIyXOzZtfCgGm4YgFnIv71R62Jp5UtJoMfJXZKoznCHQwaRFUF7cTBJeOHJ2_UVaO-MpW4lLorQ9zf76ud8zPWPpmWsBZYslmijI_u-XQmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
ترکیب تیم‌ملی آرژانتین مقابل بنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/Futball180TV/107962" target="_blank">📅 00:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107961">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcTg66lKWGQQ5nICipBIeMKb_sMEYbDwEtcG65hEXI72z0_2dhq3Q7r3f_2BB8_DxrzJBXpeUxYLj_5W-n67_ou28ontX0Cc7M56HIovhn5jwRTTyg4VmyPdmHwrmzFyy1YK90CL4bxf33wpwvunh5BHH6TMTtzHq92W8hIUNf_79VRopIMH_laEOZyabYNCzVeMk6Jd_u0tAaFRiCZxgHAv3snN91m5QM8Q_5lQ1_nWIcVmRv42XA8NOL_ERjB_2hRSUwRmQUvwRolm2BdSn1gGTX-8w4_YP7vT8HN8u1U-oo5wY7lcjfaFcznYUIFnX0fWpgTPeTs2P1dlqaWpEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی اسپانیا به مرحله یک‌چهارم نهایی لیگ ملت‌های اروپا راه یافت.
🇪🇸
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/Futball180TV/107961" target="_blank">📅 00:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107960">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Shatel-VPN.apk</div>
  <div class="tg-doc-extra">58.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107960" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فیلترشکن شاتل
🔥
✅️
تازه نفس
✅️
تست شده رو همه‌ی نت ها
نصب از گوگل پلی</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/Futball180TV/107960" target="_blank">📅 00:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107959">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
فیفادی کسشر و طولانی سپتامبر و اکتبر رسما به پایان رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/Futball180TV/107959" target="_blank">📅 00:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107958">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/580bfb3d91.mp4?token=vl22bQSU85YOZn3LZ-KF6PMv69C8UH1LGPXAjInsbizwoaCn4jr9KuNPLSi66ofJCvZirgHpPN61XcOmjvEfcse8YSujvtDPijcpc9g3SxmKse8TlnpFurZOFAuSZnlei-3r_MycOKT220a0K1_XV32iH3XolkizTksHdQPtfBplDmraTdfESrNgLvK5jvl9oIHf5355UdUbP3ofplayzoKBQRtxEFqXgn2jbfDgg48JhDt2y6zM8VLYJhM813vJLGe2502qSs4cWR4XSRsdWcKzP6ty3i-i35332netB5N6OIoJfpB9x6SRY6Am9NA3CMte6U8kRTXiW0UTsOlWNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/580bfb3d91.mp4?token=vl22bQSU85YOZn3LZ-KF6PMv69C8UH1LGPXAjInsbizwoaCn4jr9KuNPLSi66ofJCvZirgHpPN61XcOmjvEfcse8YSujvtDPijcpc9g3SxmKse8TlnpFurZOFAuSZnlei-3r_MycOKT220a0K1_XV32iH3XolkizTksHdQPtfBplDmraTdfESrNgLvK5jvl9oIHf5355UdUbP3ofplayzoKBQRtxEFqXgn2jbfDgg48JhDt2y6zM8VLYJhM813vJLGe2502qSs4cWR4XSRsdWcKzP6ty3i-i35332netB5N6OIoJfpB9x6SRY6Am9NA3CMte6U8kRTXiW0UTsOlWNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم اسپانیا به کرواسی توسط میکل مرینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/Futball180TV/107958" target="_blank">📅 00:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107957">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb0272b88.mp4?token=mDfNepFM9nUOG2nTTfSG8todFEHDVwAz1HDVT5oiIvvU8dakQ0tm6RyA8oaHZLun34db-CR_DFozffsPko72OPWKOQWsVDrGW9BqPjhgPwsPjjzPforIXVg0PIsGusqqeF-xglJUURxrxNR0vsGRcSVAb4pgB5bpkEV9Svm16bv9bn6pZsFaJ2JW7_P0KPc4KhNxR1eW2ipy9A9Hhdm7nL4-UAa3v5CUkfB-M3Gw7u-K1FbaMOqmIbUf_pYVpLqWdJymommIxVOSOdM2UI1S51r8D5vKejoKJd4YXYQCzUoQLi9yNe03SYDe3_LrckleBzBw0XmqZxQ74t-w8L31vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb0272b88.mp4?token=mDfNepFM9nUOG2nTTfSG8todFEHDVwAz1HDVT5oiIvvU8dakQ0tm6RyA8oaHZLun34db-CR_DFozffsPko72OPWKOQWsVDrGW9BqPjhgPwsPjjzPforIXVg0PIsGusqqeF-xglJUURxrxNR0vsGRcSVAb4pgB5bpkEV9Svm16bv9bn6pZsFaJ2JW7_P0KPc4KhNxR1eW2ipy9A9Hhdm7nL4-UAa3v5CUkfB-M3Gw7u-K1FbaMOqmIbUf_pYVpLqWdJymommIxVOSOdM2UI1S51r8D5vKejoKJd4YXYQCzUoQLi9yNe03SYDe3_LrckleBzBw0XmqZxQ74t-w8L31vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول اسپانیا به کرواسی توسط میکل مرینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/Futball180TV/107957" target="_blank">📅 00:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107956">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa7164783.mp4?token=vlrDvZrIaRXlddNCgx8SSXedBnYzpQpenAoOGoeOSiM_v-MBw2WaHqd1vljw2eArydEdatn0hi_1hPGkhvcxVI8g2QMO5PxU8yKsaYrjM9j_poOfUvzmaqrIXs4-_1_ziRjss4BDbCjC6P2kU-89iTAkQXOp6SJynToTeKO2XGHAy_YdDy3FNAPhB9QcXkrxTW8Rxmh_OE6deohnRdB0PmZ1m5UuH_rS4U9I9cQlaVaMIjShZ9AVbTaLZcAyC4pXSAj2UH4GdnOewe2dqJjX5qwvlTcGKJFQeO-cCJlUOXR-KUINnwl8p2_DEiWv5hxRONXgbf-KToh1aGTPYwMVDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa7164783.mp4?token=vlrDvZrIaRXlddNCgx8SSXedBnYzpQpenAoOGoeOSiM_v-MBw2WaHqd1vljw2eArydEdatn0hi_1hPGkhvcxVI8g2QMO5PxU8yKsaYrjM9j_poOfUvzmaqrIXs4-_1_ziRjss4BDbCjC6P2kU-89iTAkQXOp6SJynToTeKO2XGHAy_YdDy3FNAPhB9QcXkrxTW8Rxmh_OE6deohnRdB0PmZ1m5UuH_rS4U9I9cQlaVaMIjShZ9AVbTaLZcAyC4pXSAj2UH4GdnOewe2dqJjX5qwvlTcGKJFQeO-cCJlUOXR-KUINnwl8p2_DEiWv5hxRONXgbf-KToh1aGTPYwMVDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
تنها سه‌ساعت تا پایان افسانه لیونل‌مسی در آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/Futball180TV/107956" target="_blank">📅 23:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107955">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d0fbc6d16.mp4?token=fz9VXWu80-XAJb8Y3ENWWtK6dBaM45Prc7LVA8E82_VyjA7BTNHwIgRb_jEYIJ23zDmSEwDmBXHWflVOil63CQfelLyaqPLcgHbrTrJgR43UH6yG7bfnCgZqs9vdIw1_y_zQmGN-Rw_tI9U-R-nfJnFnYAJ6Gf9y763Ta02S7ef86-jkmUxbtHwAZMz539_Tdo40D2n3YTYiVt9ouw5l6ladZq0Uf7c5wg9kI722nlkL-qI3Rh4Q8gRPU-CGWx-NFws7P7q30MQp26BxoBIckCJFJ0-0D28f7XkWUmbUQZM7GQDkN1zuB-2CuFLNcMz7SfosUlldwTn86eHNiZOZuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d0fbc6d16.mp4?token=fz9VXWu80-XAJb8Y3ENWWtK6dBaM45Prc7LVA8E82_VyjA7BTNHwIgRb_jEYIJ23zDmSEwDmBXHWflVOil63CQfelLyaqPLcgHbrTrJgR43UH6yG7bfnCgZqs9vdIw1_y_zQmGN-Rw_tI9U-R-nfJnFnYAJ6Gf9y763Ta02S7ef86-jkmUxbtHwAZMz539_Tdo40D2n3YTYiVt9ouw5l6ladZq0Uf7c5wg9kI722nlkL-qI3Rh4Q8gRPU-CGWx-NFws7P7q30MQp26BxoBIckCJFJ0-0D28f7XkWUmbUQZM7GQDkN1zuB-2CuFLNcMz7SfosUlldwTn86eHNiZOZuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
💋
پرواز لباس غول‌پیکر لیونل مسی
به کمک هلیکوپتر بر فراز شهر زادگاه وی ، روساریو ، قبل از شروع بازی خداحافظی لباس غول‌پیکر مسی به پرواز درآمد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/107955" target="_blank">📅 23:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107954">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c2d316bd4.mp4?token=iHQP0d2n72p9yVBDpuNooDDqot5JGs2gpwEPZNjpUON97kHATHlMxY8vukoEfavnesVa6OohelFIOMnsqyOi8ezBdF9tDxH1qYBxa8z6AkJB0PojTEZhD2B-RcPvF2Xwsn9huViwLPA7AzGZaCIEHjNwAUTg7c4CyYQtwe8MdkuD9DEYZ8t9tYiIeptBhOuXm4ukAfboqP96Xs6KvRG3FrW1lGqc0cLhq8iJmbb1a6yfseIc6yGxJn3s6X8UjyzlH_WyykxsqK1UImlfwNSA2GM6tFpbk5kDLEjb7ETOFIkZRjHT7VkiYJCF6hi4ApQd0jvSIsMUDoOayLKMKBI-bD18vmui9IORFb91Q4iR-ie7CmXe3zqT_oEqnRHOYJuxZ9kynhWieqiVO6t-NvYmU1KIVeQLNdvHjFRcYS9Lg25fQE1kOJVQrfRJzUbvcBMrUitOIzCxXIsvwgtxrh_WKGeTj5E2-KY3mmrnbcqZLYJZqodx61b0Z2ujq1Tf3KMYgs6NlAOR8S0uW5cgKjJO0BDqD3HeeJ2VilzksVB2VlxtD3OAj2QQ8-1r0s38scoD-yqxebltSsyjES9XqgSBcN4Datlxwp3AK3suOoNj1vuqg9MyzXVXJP66y2LQztULWp0Q88DhVZXbY5Kkiugrt-kIIF5TmgE3P5ygVvQhRUg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c2d316bd4.mp4?token=iHQP0d2n72p9yVBDpuNooDDqot5JGs2gpwEPZNjpUON97kHATHlMxY8vukoEfavnesVa6OohelFIOMnsqyOi8ezBdF9tDxH1qYBxa8z6AkJB0PojTEZhD2B-RcPvF2Xwsn9huViwLPA7AzGZaCIEHjNwAUTg7c4CyYQtwe8MdkuD9DEYZ8t9tYiIeptBhOuXm4ukAfboqP96Xs6KvRG3FrW1lGqc0cLhq8iJmbb1a6yfseIc6yGxJn3s6X8UjyzlH_WyykxsqK1UImlfwNSA2GM6tFpbk5kDLEjb7ETOFIkZRjHT7VkiYJCF6hi4ApQd0jvSIsMUDoOayLKMKBI-bD18vmui9IORFb91Q4iR-ie7CmXe3zqT_oEqnRHOYJuxZ9kynhWieqiVO6t-NvYmU1KIVeQLNdvHjFRcYS9Lg25fQE1kOJVQrfRJzUbvcBMrUitOIzCxXIsvwgtxrh_WKGeTj5E2-KY3mmrnbcqZLYJZqodx61b0Z2ujq1Tf3KMYgs6NlAOR8S0uW5cgKjJO0BDqD3HeeJ2VilzksVB2VlxtD3OAj2QQ8-1r0s38scoD-yqxebltSsyjES9XqgSBcN4Datlxwp3AK3suOoNj1vuqg9MyzXVXJP66y2LQztULWp0Q88DhVZXbY5Kkiugrt-kIIF5TmgE3P5ygVvQhRUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم انگلیس به جمهوری چک توسط هری‌کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/107954" target="_blank">📅 22:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107953">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f36f54f3.mp4?token=hCaym4kXLqT69D6CPfJ2EoanJhaRmuzydC5uTEQdgSYTW5QW2zySxNmvBZvrRfDhz7c0vNFSdyHqexNn5s2_TzD7PYdDAKdwBG6J-gPIFnC56Ch4UfFngN0068Jbw8FlOxNexBcHSqJNTzk13p01qkArNTayzR6e76meDkuJpbZoswafenBMNPIByVFty75bCnDPc6Ul9ou14_XV8NBBBLX0X3E9t0Jmhg6mZp2rjpqEJAkhE6_n_IT6bo9UJZMITlmSjQnhVpnISiBrupbLmWQ6kKxw9T5F6FlGfc2kNLBba2WWpeegtN1rW870ddlL6Ap1dvh5M5d_0R7ha2Op1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f36f54f3.mp4?token=hCaym4kXLqT69D6CPfJ2EoanJhaRmuzydC5uTEQdgSYTW5QW2zySxNmvBZvrRfDhz7c0vNFSdyHqexNn5s2_TzD7PYdDAKdwBG6J-gPIFnC56Ch4UfFngN0068Jbw8FlOxNexBcHSqJNTzk13p01qkArNTayzR6e76meDkuJpbZoswafenBMNPIByVFty75bCnDPc6Ul9ou14_XV8NBBBLX0X3E9t0Jmhg6mZp2rjpqEJAkhE6_n_IT6bo9UJZMITlmSjQnhVpnISiBrupbLmWQ6kKxw9T5F6FlGfc2kNLBba2WWpeegtN1rW870ddlL6Ap1dvh5M5d_0R7ha2Op1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
مدل‌موی مارتینز به احترام مسی در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/107953" target="_blank">📅 22:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107952">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7217759036.mp4?token=MBl8W_3COwstYGUHVLs3B4uSJ4_SCXW4B1hntfo2UDHMi8P01VtcJ3rVXIq2qMh9u6uwzTZ1Fw7JXkYq0owItEfJdt-DEKj5ELJCsFxePoGB-_Scb6T-T0F1OPKQweWL-TqMjZMOZZwHYiG17H-e6MZVrn4ORmDYYwRBGzdFYq6NYWYPzNnP4mnxrbddcBhqnhfsUOcsyL1DYIL02BaB3rrYWbcPyHKqbTmj_LfrblfdH5X6nVwcGRScbhLw33mbQIWyiNh8bkmsttleWZBGqg56aXD0vsMQO8SVe5fbx0pQpuXZXnWWzsmFpKfwB9BS79hB0KdqxVnuAxPAfpKu02gDUE8pmP2ttjBJXGmkuULqYAALFLY8F35TuW0KTPXWZh_g1tr_MMx-6tZUNQ2gc0Qd7JC95tQvFM3hbjjvBbxiuyU7n-VxlW09lmzw58uGfHfIbFUr5gx_2dLfOGzS3Kbffda8f-eXu8gnf4-iHSnz-zQ_QWZfSEZwFfpPBX8t-Tis_Ca3giiA3L3k0TNFuBb9kaXgl9opLetErX0nyBveJRywDqGI0CgLLMSObguX3qiSpSybuIQE4hIrk_6TpzB4xV59adjfs4lbFn_PiWCC00OELweuIOmDlfr8HgY1ir1bwzZvzlfTR6WE4ZOOsNMurl0ZF_kCtwdxLWni6us" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7217759036.mp4?token=MBl8W_3COwstYGUHVLs3B4uSJ4_SCXW4B1hntfo2UDHMi8P01VtcJ3rVXIq2qMh9u6uwzTZ1Fw7JXkYq0owItEfJdt-DEKj5ELJCsFxePoGB-_Scb6T-T0F1OPKQweWL-TqMjZMOZZwHYiG17H-e6MZVrn4ORmDYYwRBGzdFYq6NYWYPzNnP4mnxrbddcBhqnhfsUOcsyL1DYIL02BaB3rrYWbcPyHKqbTmj_LfrblfdH5X6nVwcGRScbhLw33mbQIWyiNh8bkmsttleWZBGqg56aXD0vsMQO8SVe5fbx0pQpuXZXnWWzsmFpKfwB9BS79hB0KdqxVnuAxPAfpKu02gDUE8pmP2ttjBJXGmkuULqYAALFLY8F35TuW0KTPXWZh_g1tr_MMx-6tZUNQ2gc0Qd7JC95tQvFM3hbjjvBbxiuyU7n-VxlW09lmzw58uGfHfIbFUr5gx_2dLfOGzS3Kbffda8f-eXu8gnf4-iHSnz-zQ_QWZfSEZwFfpPBX8t-Tis_Ca3giiA3L3k0TNFuBb9kaXgl9opLetErX0nyBveJRywDqGI0CgLLMSObguX3qiSpSybuIQE4hIrk_6TpzB4xV59adjfs4lbFn_PiWCC00OELweuIOmDlfr8HgY1ir1bwzZvzlfTR6WE4ZOOsNMurl0ZF_kCtwdxLWni6us" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول انگلیس به جمهوری چک با گل‌بخودی عجیب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/107952" target="_blank">📅 22:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107951">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb203d7cdb.mp4?token=uu8FTzYe4WAY8zv0tJeXsCnOUCx9E759S4tc30FKh6s7N1OaMU3aoO3WTl6uGJqefKTaJf7nCCou7DRO-AyF6zNAndBsWlXZF3Qvora805Wiyls420YfLu1mXil03cQh1fE4SkYOHb08sj6myiipSnLLHzKxiYiLil9Ki4cjrgqDPFi3EArC-V7KIizOG_UnzUrc4pvWq-AIvvs7OyKSwPfbmZbhpsMBRA0yu3kadHf7OgHLrhiM8kcaZIu8onSWFdv_fYvr8n00loHDNvvp2h-UHCn6ZmQmqW7ahJ2fbICB5iXhVOvrDPmn5KmUTm2yN8cu81dP2aNMCLMJ5iKGQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb203d7cdb.mp4?token=uu8FTzYe4WAY8zv0tJeXsCnOUCx9E759S4tc30FKh6s7N1OaMU3aoO3WTl6uGJqefKTaJf7nCCou7DRO-AyF6zNAndBsWlXZF3Qvora805Wiyls420YfLu1mXil03cQh1fE4SkYOHb08sj6myiipSnLLHzKxiYiLil9Ki4cjrgqDPFi3EArC-V7KIizOG_UnzUrc4pvWq-AIvvs7OyKSwPfbmZbhpsMBRA0yu3kadHf7OgHLrhiM8kcaZIu8onSWFdv_fYvr8n00loHDNvvp2h-UHCn6ZmQmqW7ahJ2fbICB5iXhVOvrDPmn5KmUTm2yN8cu81dP2aNMCLMJ5iKGQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤯
سیل هوادارای مسی برای خداحافظی در آستانه آخرین بازی مسی برای تیم ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/107951" target="_blank">📅 22:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107950">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d806496fdb.mp4?token=KFwvggMLKxJIR6X1AOKpptiKVrHkmE7OFGgAH3zcDnk90Wp2JnBHalVSQsFRNlNOvZxQXbk4WmvhICrXzDaHBpBEDhij3csJaNgDwD4YSE83m-8T5IkcZISignNQ1Kd2BNoD3K4PXlGn_dWc36O7bB47xxQwpUz6jMUUDcjNw133ys0-lnDzfy0bj8Jn4dk_aNU7YqZXoS61zHB0nCVltc2fmUOtavRyeMbxFUMAsH-FbBLDNaPnqON7-Mcbi-pBxLOpIrAOQP1OqPxxSTmU1A3UxnQXGdO8i5p4cZPXeWcE-4lNzRMVmLfBO5xRGWSSuCoCtx2Q2H6y1G16g8BrNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d806496fdb.mp4?token=KFwvggMLKxJIR6X1AOKpptiKVrHkmE7OFGgAH3zcDnk90Wp2JnBHalVSQsFRNlNOvZxQXbk4WmvhICrXzDaHBpBEDhij3csJaNgDwD4YSE83m-8T5IkcZISignNQ1Kd2BNoD3K4PXlGn_dWc36O7bB47xxQwpUz6jMUUDcjNw133ys0-lnDzfy0bj8Jn4dk_aNU7YqZXoS61zHB0nCVltc2fmUOtavRyeMbxFUMAsH-FbBLDNaPnqON7-Mcbi-pBxLOpIrAOQP1OqPxxSTmU1A3UxnQXGdO8i5p4cZPXeWcE-4lNzRMVmLfBO5xRGWSSuCoCtx2Q2H6y1G16g8BrNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول کرواسی به اسپانیا توسط ایوان پریشیچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/107950" target="_blank">📅 22:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107949">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گگگگل کرواسی یکی به اسپانیا زد</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/107949" target="_blank">📅 22:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107948">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfAQ39ziWxC5H3R_BRMLwlSLtEPrI4y1OyzbUHUTfISDmVp3Q-H8XkVV_wyv5nSiyfjSgLVlC37Kibi5PcKEsyDDEYyziRV8V-fsY5Z8jbHZyyWs4yMKEEqNtKPny5BOjLS2o1_lbffzx_GAOIsFWp13aIU7x9c2jArI8VUQaOroPg18OAH0RBtxzG0wS4V2SiUwGwSpjQhWxdClviflpdw1gaKdCkrsy509kdcqapIOnglrK6lxFDyLTz2XnTwViQgewzPjjEybuTvGKRlqwcMEzWZo6_xG5IyMdbBZ_Trh8bbkCfhh12X51F1mmucg89n2hLVsl3SKDReO6-u1Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔻
خلاصه‌ای از بیانیه کریس رونالدو:
🔻
رونالدو تأکید کرد که مربی قبلاً با او توافق کرده بود که در یک برنامه مشخصی برای بازی‌ها شرکت کند، و بازی با نروژ در این برنامه نبود. سپس، به طور ناگهانی از او خواسته شد که برای بازی 30 دقیقه آماده شود، و در نهایت، با وجود…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107948" target="_blank">📅 22:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107947">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
⚽️
🇵🇹
اسطوره رونالدو:
🔻
بابت ترک‌ناگهانی اردوی تیم‌ملی از تمام بازیکنان و مردم پرتغال عذرخواهی میکنم. من به عنوان کاپیتان تیم مستحق جریمه و مجازات بدون هیچ تخفیفی هستم
🔻
همچنین به مردم می‌گویم که اگر شرایط ادامه حضور داشته باشم قطعا دوست دارم برای کشورم بازی…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/107947" target="_blank">📅 22:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107946">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxCnr_P2f3BE6dKCbxI9bninHvhRmPNF4pZLFMdkVAVAm2f4gaebv9WqZf0sGHGcACyTaec0iN0sE_SBo3CEG2Gws_LVDpx4hFR8nTKDqNzXZGxS-S2H3RzwxIbxQtdMIOeGNYiTahZQXsXbynZqYod_t4gz1OHbRuLb9lF_fSiAwfW91u9R8lfBgxnrcezB_z9Q_q9xPEqS4QCVJEz0XiQPj8CifjXyM719bfahxlA-H6MKjUAmQ1NCmQiR6_CAPAv793FIQjL1aIfcBZRShVD6O5gH77YPoPROhTuiMJHrAyX6V3H-JiDXhQrcNrv3l23TcAYndyuq8N58Y47CFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره کریستیانو رونالدو:
🔻
جورجی ژسوس برای اولین بار با من تماس گرفت و گفت که مایل است به صورت حضوری با من ملاقات کند. من موافقت کردم و قرار گذاشتیم در پایان تعطیلاتم با هم ملاقات کنیم.
🔻
آن روز، مربی به من گفت که به من اعتماد دارد و حضور من برای…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/107946" target="_blank">📅 22:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107945">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
🚨
بیانیه‌ کریستیانو رونالدو:
🔻
بعد از جام جهانی 2026، من پیامی برای مردم پرتغال آماده کرده بودم که آن را تا امروز نگه داشته‌ام و آن را زمانی که به طور نهایی از تیم ملی خداحافظی کنم، برای آن‌ها ارسال خواهم کرد.
🔻
بعد از مسابقات، رئیس فدراسیون فوتبال پرتغال…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107945" target="_blank">📅 22:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107944">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🚨
بیانیه‌ کریستیانو رونالدو:
🔻
بعد از جام جهانی 2026، من پیامی برای مردم پرتغال آماده کرده بودم که آن را تا امروز نگه داشته‌ام و آن را زمانی که به طور نهایی از تیم ملی خداحافظی کنم، برای آن‌ها ارسال خواهم کرد.
🔻
بعد از مسابقات، رئیس فدراسیون فوتبال پرتغال از من خواست که با تیم ملی به همکاری خود ادامه دهم، و همچنین از من در مورد انتخاب مربی فعلی نظر خواست. من به او گفتم که این انتخاب، گزینه درستی است. بنابراین، از انتصاب او خوشحال بودم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/107944" target="_blank">📅 21:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107943">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9MBj0Xg8l15bIPDsRj22l1CYySp-RSpjsOMw3y-6gk3GlNe0_36xOvNU117W-TLJ8kz6F0n0kI-5qpxlCUmmaVjgcek-FJ-VWVz_FCpWaEWNwPm-Q6KXrRataR9Rxj96-wju9WtlkdvL9G8bRq_CpkVDzyaYSqP-KRbHesqMS3VtOsFM_okTLDO8lEX-LpO1IehVvIa2aGeZhR1yymbv5E5FM468SQttr1UdlK3mfvBvlEP8dzoHwv1esLUYd20p8dSpXqiZvKNGOs-olgCM5Xp8wcpgs-C5gVicANV4CvZBXnKgBrfrDTymwCNEPJPVFD0d4NRW3PFvPcoI7fZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
مصدومیت حبیب فرعباسی سنگربان استقلال جدی نیست و این بازیکن به دیدار روز ۱۶ مهر مقابل تراکتور تبریز خواهد رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107943" target="_blank">📅 21:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107942">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8036043b2b.mp4?token=ZuZLjGA2SphOnmm8srMWzM2vcpZPqT-QCIsHMx_xnCE6sJPxNl-U0z8kz7OWm75N9cuS1QFhwIW4AmbZIghkfe8aQ8Wz7ljFJ3W3L-M5tNWKiLSHs82nDxC4BFRikeq2SnQwhKS8ZAtYyWyu_6T9pqvaXz6LiXUoN0RY3r3nKYQQUGjntUeZHnHFleuJwCxrFFeuyI-iRrIKyh74As3fDBRg6O9mtlyM0XZK-Uv9B-z6o2rHjNmT5UNmbhEissQn-HymnNpQpPWUOXWVkwWlBB0abz7hSjz8oEaHYl30NE2-7NlHoiVBzIe-ZMFvEuE1pnukZx_O8muQgRc4ROHgTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8036043b2b.mp4?token=ZuZLjGA2SphOnmm8srMWzM2vcpZPqT-QCIsHMx_xnCE6sJPxNl-U0z8kz7OWm75N9cuS1QFhwIW4AmbZIghkfe8aQ8Wz7ljFJ3W3L-M5tNWKiLSHs82nDxC4BFRikeq2SnQwhKS8ZAtYyWyu_6T9pqvaXz6LiXUoN0RY3r3nKYQQUGjntUeZHnHFleuJwCxrFFeuyI-iRrIKyh74As3fDBRg6O9mtlyM0XZK-Uv9B-z6o2rHjNmT5UNmbhEissQn-HymnNpQpPWUOXWVkwWlBB0abz7hSjz8oEaHYl30NE2-7NlHoiVBzIe-ZMFvEuE1pnukZx_O8muQgRc4ROHgTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
حمله تند خداداد عزیزی به مدیرعامل تراکتور حجت‌کریمی بابت مصاحبه دیشب در فوتبال برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107942" target="_blank">📅 21:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107941">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a98f55b4.mp4?token=SNTpbP1lMwXGLjxhtAO7Nmc3Z8BohGlKw0Z8guwIOD-MIfGV9YHBSdd4SPdzeUDXwuthXQWaO-UChQOrWIfQEvdYmoD_tXstCMe2FtM5TuEsqhPuXtUQxMJSs3H1YUY0jil0TyT1EDI8RtDUPkfGMXrd0kO9bGq3Wbrd1hbd6SfVJrpAFUKEYIgFp5FZWM-GkCo5pQsvPqHyBPI8wUoCIpiGyUdcRpw48RSv_ruYz8u2MefM_WTHHVM2mXCdf5Up6an5xndq5lyZrf3Qw5LoLy62phmqy9UmNItDUHhjQWXavryO7Xp1_AJeElke7B0PTV3t5VstydwsJWmwMDoWnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a98f55b4.mp4?token=SNTpbP1lMwXGLjxhtAO7Nmc3Z8BohGlKw0Z8guwIOD-MIfGV9YHBSdd4SPdzeUDXwuthXQWaO-UChQOrWIfQEvdYmoD_tXstCMe2FtM5TuEsqhPuXtUQxMJSs3H1YUY0jil0TyT1EDI8RtDUPkfGMXrd0kO9bGq3Wbrd1hbd6SfVJrpAFUKEYIgFp5FZWM-GkCo5pQsvPqHyBPI8wUoCIpiGyUdcRpw48RSv_ruYz8u2MefM_WTHHVM2mXCdf5Up6an5xndq5lyZrf3Qw5LoLy62phmqy9UmNItDUHhjQWXavryO7Xp1_AJeElke7B0PTV3t5VstydwsJWmwMDoWnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
افشاگری بهداد سلیمی از ناداوری در المپیک ریو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107941" target="_blank">📅 21:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107940">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8dd97c34d.mp4?token=JBhacZ9SUJ2a41p6V7nAprn6IpaJY8zd5xZPLQGC153LP_0gHbsSimTyj0CCAHwX2b_2b8bo4eqeuLvqY_ybZewK5Kz4NPNtQmSt8-uSseXuQzSGOix3G61G9hPauqYa2Y52FS6jG6YwHKUd_cnA-DD6VozjQHQ5dXkeOnGXpE2Iu9PJawnGmIKAg5ZExqKUY19x2djmPw1DbgFLIxicgeKaE7FskzZEstspcVPU7G4jiXFljG1FTMyju2IFlteOSpkK7bfUu0RgwG3hmV4bNCaqs4jS-eH9ZVMD3vggL1Q7YhQwnFrUcKXqTc9RuFx_eVg9tcJdOI8DBsj0hTn01Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8dd97c34d.mp4?token=JBhacZ9SUJ2a41p6V7nAprn6IpaJY8zd5xZPLQGC153LP_0gHbsSimTyj0CCAHwX2b_2b8bo4eqeuLvqY_ybZewK5Kz4NPNtQmSt8-uSseXuQzSGOix3G61G9hPauqYa2Y52FS6jG6YwHKUd_cnA-DD6VozjQHQ5dXkeOnGXpE2Iu9PJawnGmIKAg5ZExqKUY19x2djmPw1DbgFLIxicgeKaE7FskzZEstspcVPU7G4jiXFljG1FTMyju2IFlteOSpkK7bfUu0RgwG3hmV4bNCaqs4jS-eH9ZVMD3vggL1Q7YhQwnFrUcKXqTc9RuFx_eVg9tcJdOI8DBsj0hTn01Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
علاقه‌خیابانی به گزارش بازی آخر لیونل‌مسی در تیم‌ملی آرژانتین که بامداد فردا برگزار میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107940" target="_blank">📅 20:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107939">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e0f6c80a.mp4?token=RSGxZO9f4UhvXq95V8_lGEwMA7x5pvU2hupdpTE4lNbDUC5MO-qR-jJh7lTHPLFvuWJK37YniIVcQrVNqY3i54m--9GN4o0I_hr_aurqqdtS8oXYPOQkETyD37uL28Mx2i9eAgjcsoh3IMlsy89o3D_ylLUF_GqtdljDn51OIDoqG2BfDtYejVpgqKxbg-2-b2K6jG5e2qpfqTRtamXzKP0O7dZjawfgb-rlj0RHYJwRD20EyhkmSQEZ9FdfaaUelmgORJXpDhnJs_yC9Eoy05ujt2Hzsq8olELUSWR0L4AF8JonUciauKkwNOl_dpQSyfeVtGj8OxzFoYYTC_AWNCNn6jZbdXpfgi9YtQYI7voVh3pxZCbev7ijFHCYdjzBY8B_r6zVnc-dHpLu1dkmB6f43UeEk8inPmUa6dU5sl85fRqpTNRQErVJWXkrXF7SM05FcioBBp-7PbCfOg9AzVr74lo-mHDpw4ZG8BXxHI6o7qCJyS19nO06co_7icgai9uz3iZqY2ZMzReZTWzZ9rGN0rbEZr02dVsnWgpr-qF01-SKpYftr1sb1qTK1SWlYCh-IaiqfxlrQDqd6es8VgoZmpamN85pZjgNwR6L4AKRsFFv5SeJZQgtFsHSIcTOBSVPuaeQGVL-N6e69r8nPE8EaUuWd3ZPNqfN0ruQsKs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e0f6c80a.mp4?token=RSGxZO9f4UhvXq95V8_lGEwMA7x5pvU2hupdpTE4lNbDUC5MO-qR-jJh7lTHPLFvuWJK37YniIVcQrVNqY3i54m--9GN4o0I_hr_aurqqdtS8oXYPOQkETyD37uL28Mx2i9eAgjcsoh3IMlsy89o3D_ylLUF_GqtdljDn51OIDoqG2BfDtYejVpgqKxbg-2-b2K6jG5e2qpfqTRtamXzKP0O7dZjawfgb-rlj0RHYJwRD20EyhkmSQEZ9FdfaaUelmgORJXpDhnJs_yC9Eoy05ujt2Hzsq8olELUSWR0L4AF8JonUciauKkwNOl_dpQSyfeVtGj8OxzFoYYTC_AWNCNn6jZbdXpfgi9YtQYI7voVh3pxZCbev7ijFHCYdjzBY8B_r6zVnc-dHpLu1dkmB6f43UeEk8inPmUa6dU5sl85fRqpTNRQErVJWXkrXF7SM05FcioBBp-7PbCfOg9AzVr74lo-mHDpw4ZG8BXxHI6o7qCJyS19nO06co_7icgai9uz3iZqY2ZMzReZTWzZ9rGN0rbEZr02dVsnWgpr-qF01-SKpYftr1sb1qTK1SWlYCh-IaiqfxlrQDqd6es8VgoZmpamN85pZjgNwR6L4AKRsFFv5SeJZQgtFsHSIcTOBSVPuaeQGVL-N6e69r8nPE8EaUuWd3ZPNqfN0ruQsKs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ترویج دروغگویی به دستور فدراسیون و کادرفنی؛ لو رفتن ماجرای تعویض زودهنگام محبی مقابل روسیه در مصاحبه احسان حاج‌صفی؛ ناراضی بود، گفت بخواب زمین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107939" target="_blank">📅 20:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107938">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc57e60057.mp4?token=r8OSTaxAKFNP1iKlz4Dx0A4ozULUZM1rfruvEopc7YO9THreKrQ_gINyrSKu3WEM-GS-_4JfGEJUn82JtHl1Q7Po7N-M0UeshlmdXMH8jok3E8KTdzpx96KMAN3BKeuGnnRIMEPwYvfbocA3oiK3g-oE_tFx9X0xofsj_1DswLEg991jg3YcmT9h1I_xrMwrn3HmQ99EsSj2DWiMzSFZqfHzpZHFxWl2ktmCYeui2MOAyebU4UMYdvyBG8fznHAFtWL37YTudOsp-mMnpEylcJJOOzrMRnfkmSFW_AMeKfOktYSit-o03-TlndPrHIQvwY5ZbR6Y3-8VrxJ63q94jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc57e60057.mp4?token=r8OSTaxAKFNP1iKlz4Dx0A4ozULUZM1rfruvEopc7YO9THreKrQ_gINyrSKu3WEM-GS-_4JfGEJUn82JtHl1Q7Po7N-M0UeshlmdXMH8jok3E8KTdzpx96KMAN3BKeuGnnRIMEPwYvfbocA3oiK3g-oE_tFx9X0xofsj_1DswLEg991jg3YcmT9h1I_xrMwrn3HmQ99EsSj2DWiMzSFZqfHzpZHFxWl2ktmCYeui2MOAyebU4UMYdvyBG8fznHAFtWL37YTudOsp-mMnpEylcJJOOzrMRnfkmSFW_AMeKfOktYSit-o03-TlndPrHIQvwY5ZbR6Y3-8VrxJ63q94jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
😱
بدون شک این عجیب‌ترین پرونده فساد توی تاریخ ورزش کشوره!
یه خانم با تیمای بزرگ فوتبال مملکت قرارداد می‌بسته و می‌گفته بهم پول بدین، منم در ازاش با داور سکس میکنم تا نتیجه رو به نفع شما بگیره!
بعد از دستگیری، این خانم اعتراف کرده که با بیش از ۴۰ داور سکس داشته و باعث صعود خیلی از تیما شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107938" target="_blank">📅 19:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107937">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
⭕️
طاعون روسی دومین کشته خودشو ثبت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107937" target="_blank">📅 19:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107936">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZiEIv3R4a1TYeN-RpVLEH629MJ6aHSm--tBlRHaUErvAwgA8hnQE-mH-I_DgCu8vgsgehc31lrJhv8TTu1Tzd__9F2XNLVFY0GiRFPnsA3-dYWyHwG2k0Xx2Uh2inbLY9ZSMGvf3sYyWuzV1-nmbPdRnbtGMPgkjz5XJ5w7iLnEIFOPvzKobQYKyKvnokMI7ZNEPdjWJmoWZiiSAPTKFdl4DfqWatCVIm_yUAmfXHICDGIRj5FbBaUzfIMnjGWKzGlY6xTniVkIe94x1Wbwm5A77YXnwOeN97wPclko6dbvalwc5mK3APTd6mbuGug5KcidqtR2bSbrWIM6AvuOTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
طاعون روسی دومین کشته خودشو ثبت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107936" target="_blank">📅 19:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107935">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e5d14acd5.mp4?token=Q7fTXpXBJ8UxMwUYW4DmDlWuSF5c11Xx9soy10-i9qKeUsIr682bt2Uul_L3nasPktt3G8IqJNGw9cBim0QkCZM3P2Y5u6Iu9CXdxxNJ-JFZSxzA9Z3PnASJjvZPM182Ejza21ZCr77dE3ikmIbQK26H1IMRjK3H5nG0KT4yeM20fPDLqyATjEBWYrReMsrwKLCQdRCkVLsro-Uo4m2E9Z69pANOtEQtWCS7aA5HiaY9ymW3_lKVv43ynknp-ES4kJBJKd_M1kWdaDLViLN2fdkOHj31UOF1B4F6fqvVYjJZshNiuc1HqR21IIrfPwxI7bckSOmFtVZsk1RAnxw7Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e5d14acd5.mp4?token=Q7fTXpXBJ8UxMwUYW4DmDlWuSF5c11Xx9soy10-i9qKeUsIr682bt2Uul_L3nasPktt3G8IqJNGw9cBim0QkCZM3P2Y5u6Iu9CXdxxNJ-JFZSxzA9Z3PnASJjvZPM182Ejza21ZCr77dE3ikmIbQK26H1IMRjK3H5nG0KT4yeM20fPDLqyATjEBWYrReMsrwKLCQdRCkVLsro-Uo4m2E9Z69pANOtEQtWCS7aA5HiaY9ymW3_lKVv43ynknp-ES4kJBJKd_M1kWdaDLViLN2fdkOHj31UOF1B4F6fqvVYjJZshNiuc1HqR21IIrfPwxI7bckSOmFtVZsk1RAnxw7Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚫
کنایه‌های ژوله به مصاحبه‌ اخیر قلعه‌نویی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107935" target="_blank">📅 19:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107934">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a828a3618.mp4?token=UFnHro4OOn5kKFHdp43sMNc36Acexo3hEXmqaTSY2VyCvN1jf33Fr81DGD44LoD017sCfNycIO5dmOn4VCSAat7YrCTY5V1yVkJpqEvW8H65H2smU37Kpi5H5q8bXBrQagU2OM2SlcFUIiOex7k_7f5FPqkl6TPhXmI0XTsYap_z2zMjkrvwpU3Gg5xr-KjDldyKRmqm-99qRutFqnwkwbrxyC2E7Qm2cWxnRQqK34KtqbQM4G3_eba3zusbfck0-DSXwJVbkhaKkeHGPZY1iUAJk1y9ZGMGgh4jMlP2TAlFQTGQOPewXyTBTWBu8V0ZqN1_F79bdfBzVThjHu3dCYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a828a3618.mp4?token=UFnHro4OOn5kKFHdp43sMNc36Acexo3hEXmqaTSY2VyCvN1jf33Fr81DGD44LoD017sCfNycIO5dmOn4VCSAat7YrCTY5V1yVkJpqEvW8H65H2smU37Kpi5H5q8bXBrQagU2OM2SlcFUIiOex7k_7f5FPqkl6TPhXmI0XTsYap_z2zMjkrvwpU3Gg5xr-KjDldyKRmqm-99qRutFqnwkwbrxyC2E7Qm2cWxnRQqK34KtqbQM4G3_eba3zusbfck0-DSXwJVbkhaKkeHGPZY1iUAJk1y9ZGMGgh4jMlP2TAlFQTGQOPewXyTBTWBu8V0ZqN1_F79bdfBzVThjHu3dCYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پادشاه مسی:
🔻
لحظه‌ای که منتظرش بودم بالاخره رسید، با خیال راحت میرم چون هر کاری از دستم برمیومد انجام دادم، این پیراهن برای من فقط یه لباس نبود، رویایی بود که بهش افتخار می‌کردم و تمام زندگی من بود. ممنونم که این‌قدر دوستم داشتید، همیشه شما رو با خودم خواهم داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107934" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107933">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxBoewIqYkv6nZ5EuWYejEPKYTXuyGPwy0BIFpR1trY1gMaWvIu_WK4kOTO3T52OHZDs7LkG5D-0v9U8PrEE7PuFe8sGs6Pacfqnh15Q40VfEG6EZpfIhjRbBDYqhDYzecLn5bpUrG9aEmAzwZRUOE-1HCpivdmd8iBwGbR8vpF6EwRxEnk0nESY5yky3VV3753cinb8teoZcjmSEZNMQoHUapfm25xwah9pEkojFaTfzF0hGjgtdol3fftRA7JOtIVtatT5B_4tYbzeCb-gSkUqAGjPnkbA3nco_qll9BtIgqysDnpiy6ZLhXC0dsG4xlrCUipPi9tDjh7bMZ-uTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دنی‌کارواخال مدافع سابق رئال‌مادرید به ختافه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107933" target="_blank">📅 18:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107932">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3341518f56.mp4?token=CqjUFYGHWPINev6mG8-b0YBF_5bwyawhk-QmnmnKcNSkA7oxiq3E68Ft8vd97yAboNOougOv76Vd4g_8dXit13Ha88B-Oe_kLRAK7I3rkKTdP6Um0MWUhy7y1sYimt-o8znhtWXghekG1DOSJ3QV86kdCX6YgGGFGAQvOmJdjpWnf8sBVL2olnZEoFqeDfclzHz6lmQkGnaw0l7XQpP54VTwuHm25byTVNR4zkrI6nA0dXtCCX_ELRCGoXMvHTANDQ2qHqJrpoIfv5h4Q3NKMahB5xr0rucuyO7_cuUA2NfmJs2Q-BF-W0PbN_u85tLmEj9Ri1hj6BJrEQANzhMyTqS3wAUCiZPPDk6CIuVlunlWLVQDyrCSBHhnry7ICngGLF9efVEsSRBQsdd_G4Ya4AOCm7ICWyd35qD4K7bRarr_NXlor5fMmTvOaNsQmLyZ5fREg-0OcWHua8RFYUgKhyExWSGSzs807wXlrV7jpiFbzRLVY2eWXAm8yvHitpCJlqmvcICrYjNvCZspdiXpT1JTlg3Lp0NiG-pQ05ct1pvE9M02t3ZQMg1w1UOyT2IAhjqqWYkVNPohVZvg34flN0HiedtvFj4gxfr28pQQSe1QqmTyDNrjZfQ1bt_JL8f1W1G-BwDpd629ss7mKILqMEVaNCLVCGITujwgiRxTp68" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3341518f56.mp4?token=CqjUFYGHWPINev6mG8-b0YBF_5bwyawhk-QmnmnKcNSkA7oxiq3E68Ft8vd97yAboNOougOv76Vd4g_8dXit13Ha88B-Oe_kLRAK7I3rkKTdP6Um0MWUhy7y1sYimt-o8znhtWXghekG1DOSJ3QV86kdCX6YgGGFGAQvOmJdjpWnf8sBVL2olnZEoFqeDfclzHz6lmQkGnaw0l7XQpP54VTwuHm25byTVNR4zkrI6nA0dXtCCX_ELRCGoXMvHTANDQ2qHqJrpoIfv5h4Q3NKMahB5xr0rucuyO7_cuUA2NfmJs2Q-BF-W0PbN_u85tLmEj9Ri1hj6BJrEQANzhMyTqS3wAUCiZPPDk6CIuVlunlWLVQDyrCSBHhnry7ICngGLF9efVEsSRBQsdd_G4Ya4AOCm7ICWyd35qD4K7bRarr_NXlor5fMmTvOaNsQmLyZ5fREg-0OcWHua8RFYUgKhyExWSGSzs807wXlrV7jpiFbzRLVY2eWXAm8yvHitpCJlqmvcICrYjNvCZspdiXpT1JTlg3Lp0NiG-pQ05ct1pvE9M02t3ZQMg1w1UOyT2IAhjqqWYkVNPohVZvg34flN0HiedtvFj4gxfr28pQQSe1QqmTyDNrjZfQ1bt_JL8f1W1G-BwDpd629ss7mKILqMEVaNCLVCGITujwgiRxTp68" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👀
شور عقاب‌های سبز؛⁣ هفته دوم لیگ مراکش و تشویق بی‌نظیر هواداران رجا کازابلانکا در اولین میزبانی فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107932" target="_blank">📅 18:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107931">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7y4peZzrS5rYe2ByRGKaFBp8sj3yDBGZWSwnSTu5adY24n-VvaiIP24I4JWAtrdjWtFeIERMQsqLyrAGn5giyzaYa0fvYybyz2ZhmqUybZOiVv9JuqtoXXdSEm6NNj7Vp8d3rXKuKES2WySxMs4tDP0tG2r9xafFsyuZxA9zp8TGIj87D48Id1ZkvhpW9qGHbvbBdSqdh43JHWlLlZRXBGfqfqYsgURKFvg5xL9YY6JJuHLs1qg0ywaUN5sfsuAdXAp9m_PsAWGb5J4w1NWxxdscujtuQJ-aziP7XMaFo81xFhLeGjD7Un04cuGHJVGt_PNjBa4PP_FkF-ryX_T8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری اسطوره لیونل‌مسی
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107931" target="_blank">📅 18:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107930">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ad3a54680.mp4?token=KWB2ApkcqH3toUV9QDnlOc7t4YdNG3izk4i7Tya4wvu103pZD6glZ6LMQo-KGuptVDTxB7OMFW2LuAU9ObsCteYXoFRhilM8OMLGHf5gcSzWreN6nV57DZr7FdPaw2NA3YDuWeDDkeWwvaum7nV-uO0YgJ-KR57q6ht547AuGSwtfZfDoQ7NRTLAOww658FjIKVlthq-pEuJlyBONw05JqAWQ8o57U7Zv3aF2tgx_oTotfc3cQk62jomCsvk6vvyVL2nDpKsho_KRl1RtxzK5XIBUBXT3OyBZ6h1acqycFVkbIADj6yh5xu3nfpJPSWgF6VSR3BAI-Pu9ieFea1_qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ad3a54680.mp4?token=KWB2ApkcqH3toUV9QDnlOc7t4YdNG3izk4i7Tya4wvu103pZD6glZ6LMQo-KGuptVDTxB7OMFW2LuAU9ObsCteYXoFRhilM8OMLGHf5gcSzWreN6nV57DZr7FdPaw2NA3YDuWeDDkeWwvaum7nV-uO0YgJ-KR57q6ht547AuGSwtfZfDoQ7NRTLAOww658FjIKVlthq-pEuJlyBONw05JqAWQ8o57U7Zv3aF2tgx_oTotfc3cQk62jomCsvk6vvyVL2nDpKsho_KRl1RtxzK5XIBUBXT3OyBZ6h1acqycFVkbIADj6yh5xu3nfpJPSWgF6VSR3BAI-Pu9ieFea1_qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
در شهر روساریو، یک پیراهن غول‌پیکر به عنوان ادای احترام به آخرین بازی مسی رونمایی شد.
😲
🇦🇷
این پیراهن در مقابل بنای یادبود پرچم ملی قرار داده شده و روی آن نوشته شده "Gracias" (متشکریم)، که نشان‌دهنده قدردانی از مسی به خاطر تمام تلاش‌هایی است که برای کشورش انجام داده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107930" target="_blank">📅 17:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107929">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107929" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107929" target="_blank">📅 17:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107928">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGmh8w9ByuPF7plyIOyppzSjm15meLKk2nP4pZ5Ar9PCCX_cYrLP6sPMlw2o4PQfivGrOhGGJymdWEg65kTADro8z677WkWAlE52kZK8zX7uUSOxC5DBybO4IYehlW8G6iX7NpLHyzbXitu-7Tq1Wl5V_w6sSQyr6B6jXVBsKjIO6qeMRj0VLa9aTRyNintJTq6c-Cl6JaNK332LB5A98H1KxUar7K8dgh9MUkee9i0N3lCeMO5yxBRPuwvD8vhO-TvdU3WfWHRw-jQiu7FX-uypZ65M6fXPTFF2FjPeGq-YxiQefsSJ36f7A1Z-blk5S0rVg9UGO0ACJQfeTuqFfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107928" target="_blank">📅 17:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107927">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c936aa92.mp4?token=pN0exFE3ePgWM8L_BovSlIu5RE5hBmlWwLq580WPFRNUfxjmNPbFYjO9oDtVUBwa4xTTwMrA3YaGLvmH4QsxlfZTIPSd0IoY4vZ_HRHSr3jGXXpuzym_DwNBuDBav_XWhkzmfrAGQroUGeU1gGnFhaXZRT5dsrxBPnWDPxy5m6adVpuI5Z2LiNNvC4_P_TbNT4cST5a7NxNLP9Oph7PAXDAKaZ8Uliqx0elsXvOTzPyN7IUgUI_Y4RHxUrr55cch3ph1M3LMXzx6Cdcnd0PtZwvqLjkpkKHvnkLdE-IeyyHiAI7s9wHRJNKINdnVH6d_XBozym9RmZ3DPidozjAMJ4kU2EJeC-bHBNxIZXzymtmVDBaaH7l_NQ2nUpwdipRIFfZAy6eqnFJRUzNTM9uPnC3yjfZnagrl3AtnOJjw7B5MaP2KkLr8ZZ0nU0xkhwZu9IGbeQafK3c0O-WL8tJJJ1L8hYBaZieNE0bkzFL77Jly89sIOQVbpa1bSbyniGMae1xpmE5zspw7Bah4STegsHIVdsgckC_JSRSyC5uVZ06G3TNvOTa-AN6qiuAbFEGmSa9q2X1EyBytgx5dBKTG7wlThMjlj6WkpIKzSSiddaZ4BxWCUhGo8XV3zSkO4brHk8alnGIh6Tc4vmN8P6GW6AyJi0v2RmY6UviqVB7xGw8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c936aa92.mp4?token=pN0exFE3ePgWM8L_BovSlIu5RE5hBmlWwLq580WPFRNUfxjmNPbFYjO9oDtVUBwa4xTTwMrA3YaGLvmH4QsxlfZTIPSd0IoY4vZ_HRHSr3jGXXpuzym_DwNBuDBav_XWhkzmfrAGQroUGeU1gGnFhaXZRT5dsrxBPnWDPxy5m6adVpuI5Z2LiNNvC4_P_TbNT4cST5a7NxNLP9Oph7PAXDAKaZ8Uliqx0elsXvOTzPyN7IUgUI_Y4RHxUrr55cch3ph1M3LMXzx6Cdcnd0PtZwvqLjkpkKHvnkLdE-IeyyHiAI7s9wHRJNKINdnVH6d_XBozym9RmZ3DPidozjAMJ4kU2EJeC-bHBNxIZXzymtmVDBaaH7l_NQ2nUpwdipRIFfZAy6eqnFJRUzNTM9uPnC3yjfZnagrl3AtnOJjw7B5MaP2KkLr8ZZ0nU0xkhwZu9IGbeQafK3c0O-WL8tJJJ1L8hYBaZieNE0bkzFL77Jly89sIOQVbpa1bSbyniGMae1xpmE5zspw7Bah4STegsHIVdsgckC_JSRSyC5uVZ06G3TNvOTa-AN6qiuAbFEGmSa9q2X1EyBytgx5dBKTG7wlThMjlj6WkpIKzSSiddaZ4BxWCUhGo8XV3zSkO4brHk8alnGIh6Tc4vmN8P6GW6AyJi0v2RmY6UviqVB7xGw8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
آنالیز فوق‌العاده سوپر تیم فردوسی‌پور از مصاحبه‌های قلعه‌نویی که واقعا عالیه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107927" target="_blank">📅 17:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107926">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9410553bb0.mp4?token=QfKwJXC5DS-msRF97We9-IyBIDtw4pnVW8F3_3tsPjyFB39aHP_XVnMQeJXnjt0gs1CiOVg8eEXxnKYzFjdi_qtwn4ct7WYRTtPzQnVyW-0yqXdKAy-jH_i5ALgegjxxWXoAzfPUB3zxv3gGWw1Kii11P9m1VydLfLuiuGbaQHgPMIJIhEG13AgGIdR4MZbBiHfr5sMBH3U8s_jBhD-x5PHT7KGp0xZ8u847qhWALtj3pOpm_vYvnu0axlRETKfvWrQ_LGn_wq5FjRDSA8iKrk55rk_aIzO0HlymdTsKT48dJLLaQD_e8_no9GG_JrIGL1fM6whEe-X1BKUlwB4L4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9410553bb0.mp4?token=QfKwJXC5DS-msRF97We9-IyBIDtw4pnVW8F3_3tsPjyFB39aHP_XVnMQeJXnjt0gs1CiOVg8eEXxnKYzFjdi_qtwn4ct7WYRTtPzQnVyW-0yqXdKAy-jH_i5ALgegjxxWXoAzfPUB3zxv3gGWw1Kii11P9m1VydLfLuiuGbaQHgPMIJIhEG13AgGIdR4MZbBiHfr5sMBH3U8s_jBhD-x5PHT7KGp0xZ8u847qhWALtj3pOpm_vYvnu0axlRETKfvWrQ_LGn_wq5FjRDSA8iKrk55rk_aIzO0HlymdTsKT48dJLLaQD_e8_no9GG_JrIGL1fM6whEe-X1BKUlwB4L4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
👤
👤
حمله عادل فردوسی پور به میثاقی :
تو که‌ حامی قلعه نویی بودی ؛ آفای محترم لطفا رنگ عوض نکن... الان دیگه حق انتقاد ازش رو نداری...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107926" target="_blank">📅 17:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107925">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2cHJtsOZeYz1cTsBytC4GTRmC-Z0ioPjWdL9wTvWZOm9bMfsux3JJ4o5NRtEyE_VWLHxSdbuG-YAhcGUvlofRRxOOL9jRVd8vp4gcRQAFoEoYsgbsSnj0b4nSAlXmLSDX1jrjZc_ACF7AorKrRt56Uh3kHWJmy43cHjqtrVopxCWzF0DMDOyImXZJpuda06BwhYE9JKTn4p4MfK3CQzTIR-HastPTibfeSDRk1cdp8PF2I86QgiyjfcA7qt6_OsZMEhHkV0EIV4XHF3_L1hyLE5CHezcFsZNAoqNVXTeBIYyvb3slPRHoZ4dQu_uqsmaMDkL-vzqyEBMVDWd9D9bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎤
آندره ویلاش-بواش، رئیس پورتو:
🔻
برای مورینیو واقعا حیفه که بارسلونا تا این حد قدرتمند باشه. درست مثل زمانی که اینتر را ترک کرد ، بارسلونا در بهترین دوران خودش به سر میبره.
🔻
اما این دقیقا همان چالش‌هایه که مورینیو بیشتر از هر چیز دیگری از آن‌ها لذت می‌برد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107925" target="_blank">📅 16:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107924">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مهدوی‌کیا: وقتی شکست می‌خورید باید پاسخگو باشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107924" target="_blank">📅 16:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107923">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf4e21ea3.mp4?token=rUzSTvASbqA5FdiKVYO8frpcDJmSATsCcb36eUtmYVF6LZB85Bdq_Gh3ebeHYShv3sT_augZ0dJL2TzSGUGC7uYKVQItXknsxOHggsvXSLn3cOzWZ7xDXKvTKwLg2T-iOfjvK7t5z7DhoTReh9b4n2aUJOc4k0wAVZJ6IOrBGIilhj6iEhCAmuzP-_d0IafFtDhuhAbZZhG9drt9aDPzajOQxZIhxneUI7GXHLB6MIT-HTRiXsDqmIlDwangnpJxpPjjQE-PzErvsgyAQDSwjZJ2cnSXB8_UIQIMSKvvMdAEBVy6kDk6VLZEMcr1fFF4sDcAVhqcym7QBPWg4s5BlBdJcFaAnz7H5sOQacP4B8HGim3LXqsm6I-I3My2B2O4tF9vWhpVH37-TpMeZS-l8DPkIlGoz1_QENCZGOWnt9Dpy7RSMxvZJoqs0pUUBZMM4eChfn16VCeTbivdP-O9qIXdXjg-VsQwXjgbTIP3n5alKDkR5AGKiOVwKYYQsYkXZWDTdMV4INIYz2B9891CCJe-gnJJejpefWevO__IvC0-EegnPdqQdFZYxWfXxRoUZ3KNLhAR5x3UzYk6tncfDK-sGM8Z29MJMjpAsoGDpQH4ZSZbEb-vRmJwIhSbg9zHgYklUnje08VzFpjuLxUGeXqpfeTrzZhNWJYc-jH50jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf4e21ea3.mp4?token=rUzSTvASbqA5FdiKVYO8frpcDJmSATsCcb36eUtmYVF6LZB85Bdq_Gh3ebeHYShv3sT_augZ0dJL2TzSGUGC7uYKVQItXknsxOHggsvXSLn3cOzWZ7xDXKvTKwLg2T-iOfjvK7t5z7DhoTReh9b4n2aUJOc4k0wAVZJ6IOrBGIilhj6iEhCAmuzP-_d0IafFtDhuhAbZZhG9drt9aDPzajOQxZIhxneUI7GXHLB6MIT-HTRiXsDqmIlDwangnpJxpPjjQE-PzErvsgyAQDSwjZJ2cnSXB8_UIQIMSKvvMdAEBVy6kDk6VLZEMcr1fFF4sDcAVhqcym7QBPWg4s5BlBdJcFaAnz7H5sOQacP4B8HGim3LXqsm6I-I3My2B2O4tF9vWhpVH37-TpMeZS-l8DPkIlGoz1_QENCZGOWnt9Dpy7RSMxvZJoqs0pUUBZMM4eChfn16VCeTbivdP-O9qIXdXjg-VsQwXjgbTIP3n5alKDkR5AGKiOVwKYYQsYkXZWDTdMV4INIYz2B9891CCJe-gnJJejpefWevO__IvC0-EegnPdqQdFZYxWfXxRoUZ3KNLhAR5x3UzYk6tncfDK-sGM8Z29MJMjpAsoGDpQH4ZSZbEb-vRmJwIhSbg9zHgYklUnje08VzFpjuLxUGeXqpfeTrzZhNWJYc-jH50jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پروژه‌ای که هر روز یک شاهکار تازه رو می‌کند!
قرار بود با عایق‌بندی سکوها مشکل نفوذ رطوبت و آب برطرف شود، اما هنوز هم آب از سقف ورزشگاه آزادی چکه می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107923" target="_blank">📅 16:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107922">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4700a47c7a.mp4?token=eFxdkk8H7zmDdzyEwKvuSUXamXG2llG5j67i11GhELcC7EaMqqSSpvXzXJynt-lJx_1VMB_3vupL9GfHhlR5mjxnhuQwoDbBTHPJYm6rFmcJeneB22CFA_pdKE8q77VnK_qxPZNA9I4rxKD6ahHDFSi2JZYp6jWre2HGpRN5o-7EEESEEkYenw_vbnpGRmlP-ROaqx5YfW1i68xjlOgclqoP-uZpSv-wW6urx44Fv7yIpFfpWYBef-kTDWf-GSeS-xo1zPKckv5PS5ziH4iS29HHqkx7abhA4EOiI09Ql6sBXXIPCxJ8SJrhhUnau0yNKuykvkREDa_kqf1_onxEnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4700a47c7a.mp4?token=eFxdkk8H7zmDdzyEwKvuSUXamXG2llG5j67i11GhELcC7EaMqqSSpvXzXJynt-lJx_1VMB_3vupL9GfHhlR5mjxnhuQwoDbBTHPJYm6rFmcJeneB22CFA_pdKE8q77VnK_qxPZNA9I4rxKD6ahHDFSi2JZYp6jWre2HGpRN5o-7EEESEEkYenw_vbnpGRmlP-ROaqx5YfW1i68xjlOgclqoP-uZpSv-wW6urx44Fv7yIpFfpWYBef-kTDWf-GSeS-xo1zPKckv5PS5ziH4iS29HHqkx7abhA4EOiI09Ql6sBXXIPCxJ8SJrhhUnau0yNKuykvkREDa_kqf1_onxEnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🎙
✔️
صحبت‌های جالب یاسر‌آسانی پیرامون فرهاد مجیدی اسطوره باشگاه‌استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107922" target="_blank">📅 15:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107921">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27cad11c0b.mp4?token=q1FptjrgZVUsoEcQJdbmLru3qHIAIFHv2-_7gFy_ElrGEP6Bp3eNmYD-iSTEIQ2tx_jxeWbLXc7LsSSxJ5KHfrAS14GglhzxxJq3trc6QP6S7_TSXfgthUmq10CxcVwuwdMOcnrzO_eQlMpTk-t0fiOnfTtrtV14sY0SndJ5P20uoYBt3ICrM2wNAJ_TbVAD5ByjlHuskUk8ycZkhDw97AhtvJmeepPL8PW1PR2DLdeDly9i5IsqRFFEw8oRnnXwDbo549PJUMtd7dBEbn9V8Y8TRaiWicBAjNhuJmYw6CpPwIess8GMgj_jaMwUe6i3I4Vz3oMHIakI1XYsB6ZFXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27cad11c0b.mp4?token=q1FptjrgZVUsoEcQJdbmLru3qHIAIFHv2-_7gFy_ElrGEP6Bp3eNmYD-iSTEIQ2tx_jxeWbLXc7LsSSxJ5KHfrAS14GglhzxxJq3trc6QP6S7_TSXfgthUmq10CxcVwuwdMOcnrzO_eQlMpTk-t0fiOnfTtrtV14sY0SndJ5P20uoYBt3ICrM2wNAJ_TbVAD5ByjlHuskUk8ycZkhDw97AhtvJmeepPL8PW1PR2DLdeDly9i5IsqRFFEw8oRnnXwDbo549PJUMtd7dBEbn9V8Y8TRaiWicBAjNhuJmYw6CpPwIess8GMgj_jaMwUe6i3I4Vz3oMHIakI1XYsB6ZFXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
پشیمانی بزرگ رجب‌زاده؛ باید به پرسپولیس یا استقلال می‌رفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107921" target="_blank">📅 15:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107920">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f6fed1c3.mp4?token=WJ6Fp5yKa9w6MbDrEWOrYEEy3PrQ1zzQO-ndtXt8ATOvK4zm-SfHbSIGG3AGk5tuk42eezl5TI2As4GV0oVCdiURPBh_ws_C-pN2Ksa638y3upBhFMX7p9LQ-i3v3rKTlnJoHZMU198iUXNGqNXJJZA6M04RI_RSEa6tSOMtL326iu33zIh4DR1fICXFfkCiNr1CVkqZE7sm1DPRoZDTXifOMUSq3PwgfwnXIZ45iNgvhdxvHk7RlwWTUnwVGFpu5QVT_AxE4UEuubCBxWu3Nv7E0xaPbpzw4JxStif0jzX5DhKjuMwklSwiBI3YbpHbzMnUKRDhAUTh5GnB36knYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f6fed1c3.mp4?token=WJ6Fp5yKa9w6MbDrEWOrYEEy3PrQ1zzQO-ndtXt8ATOvK4zm-SfHbSIGG3AGk5tuk42eezl5TI2As4GV0oVCdiURPBh_ws_C-pN2Ksa638y3upBhFMX7p9LQ-i3v3rKTlnJoHZMU198iUXNGqNXJJZA6M04RI_RSEa6tSOMtL326iu33zIh4DR1fICXFfkCiNr1CVkqZE7sm1DPRoZDTXifOMUSq3PwgfwnXIZ45iNgvhdxvHk7RlwWTUnwVGFpu5QVT_AxE4UEuubCBxWu3Nv7E0xaPbpzw4JxStif0jzX5DhKjuMwklSwiBI3YbpHbzMnUKRDhAUTh5GnB36knYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قلعه‌نویی سال ۱۴۰۰ در برابر قلعه‌نویی سال ۱۴۰۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107920" target="_blank">📅 14:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107919">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw_Ng7pqnLLpmQMJIlyqtYlX6L9ujJj26cAVjeEaMkDS7AsUJrS11MAa0JRiz6GY-2AKRykHa_4uBdFmlMazU6aKp14xbRm8n-WYH9UIjQFTG3pbedzhiQo4nRfNuSNSyD5Bdu1ROdw2vdJHx3rB4wvAVGS1wqUheSgokYzdy-lP4ZFN-9sbiKeDrCo8bxuF2yFfJ2oSdLypACCsiLB2LUtPX2xQ9mDrd_VsvmXX4Wswtok-b7PHNo4jck8rrrijs8Rea0A6wq2albp1w2BdjqSNUasSHamTut26RUX31tlheL3UcZ6TF31bZ2HZ1tCHG8OjhtDtwLBFNyzhKlzMHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🙂
رسانه‌های برزیلی با انتشار این تصویر معتقدن که وینیسیوس به قتل رسیده و بدلش داره برای رئال‌مادرید و برزیل بازی میکنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107919" target="_blank">📅 14:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107918">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0504ebd98.mp4?token=T1E8yikv0ey1vs-kCdBab5OtltsteXFdwD76mcQci_S7cRqedazIumf0elakMzgaoPmP6usT1Fa4krs5R5-VfSQLGD11lNYPsnbUHbJELnUuGF7r085_mywvCckZztn34f-Tiag9DMt7hM7GgjLFKHsVp25eYStRTspGsjNln0S3VULExQdb0LpYAqPGeTTm8lVVUg9EGj9Sgtq46nd4OiULB7UM09p6-rrjJswss2m8WLXwIO3Px7n72YYyVmB7XEJD8anV0yob9hFD1abHMzNdyLif8n-mLuUfEDsc_9H8NzGZ-8m3bqczcDOq3QnTxLA85Mlby2wOCddVjpvyTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0504ebd98.mp4?token=T1E8yikv0ey1vs-kCdBab5OtltsteXFdwD76mcQci_S7cRqedazIumf0elakMzgaoPmP6usT1Fa4krs5R5-VfSQLGD11lNYPsnbUHbJELnUuGF7r085_mywvCckZztn34f-Tiag9DMt7hM7GgjLFKHsVp25eYStRTspGsjNln0S3VULExQdb0LpYAqPGeTTm8lVVUg9EGj9Sgtq46nd4OiULB7UM09p6-rrjJswss2m8WLXwIO3Px7n72YYyVmB7XEJD8anV0yob9hFD1abHMzNdyLif8n-mLuUfEDsc_9H8NzGZ-8m3bqczcDOq3QnTxLA85Mlby2wOCddVjpvyTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
فتح‌الله‌زاده: از استقلال که بیرون آمدم برای مدیریت پرسپولیس هم پیشنهاد داشتم/ تاجرنیا نه مدیرعامل میشه نه میذاره کس دیگه‌ای بیاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107918" target="_blank">📅 14:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107917">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8beb00264c.mp4?token=pnwKxvS8WDX17znnM5-YIeSdQaCu_4bs26BTPNz5aPHv2-Yn3BEVdJv_H8qFMfyeG3c8wCI2-jDbCdFCtlqyk63-bRYIGPlMvtcLo7jBHvqtIpZ_DOW3zEPRGzd33NP3ZBH2TQOBOpXJp1FnDjtrkge8qFyqgDRbHirAtUk-3oKDRNrAGMWbO9zHGbdRqHVKdx7QOdw5EdGQ9xgpIQ-Pjcyr5-PDSuefk-8xUj9Fj29s1fYgKVLQfvTCV4YTVcqfyidmrWXoqMxZVwnC59ndOV4WUV8ZXk6ycIAg1BqAuD25_yyMbHhItbqjisbYE9M9nq6bC8Qz3Io_WmTeqLePlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8beb00264c.mp4?token=pnwKxvS8WDX17znnM5-YIeSdQaCu_4bs26BTPNz5aPHv2-Yn3BEVdJv_H8qFMfyeG3c8wCI2-jDbCdFCtlqyk63-bRYIGPlMvtcLo7jBHvqtIpZ_DOW3zEPRGzd33NP3ZBH2TQOBOpXJp1FnDjtrkge8qFyqgDRbHirAtUk-3oKDRNrAGMWbO9zHGbdRqHVKdx7QOdw5EdGQ9xgpIQ-Pjcyr5-PDSuefk-8xUj9Fj29s1fYgKVLQfvTCV4YTVcqfyidmrWXoqMxZVwnC59ndOV4WUV8ZXk6ycIAg1BqAuD25_yyMbHhItbqjisbYE9M9nq6bC8Qz3Io_WmTeqLePlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
▶️
👍
تسسترون خالص!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107917" target="_blank">📅 13:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107916">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اعتراف جدید کلثوم: آمار دقیق افرادی که به قتل رسوندم، ۱۱ نفره. یک نفر هم پیش‌از کشته شدن متوجه میشه و نمیذاره اینکارو انجام بدم
😐
⚽️
Channel: @futball180tv</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107916" target="_blank">📅 13:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107915">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8324686f63.mp4?token=f8wtvCuk7qTwkKKacPe0R2leQ1DSxO-VA9y51mtOMs0nsHJSR7LAnVmP7I3fPLIHwNK2LUp-o_r4dFwJYD7vBSVVRcsvDm1etRJH2Tm_9qhf-h9um4SEOab5MIEb4rxZxGNREfyCb_06GVqdo4gCRFCCKo_cpcPRil-KnrI6qpde7DzOzUO3nVjg7GdWsr89Kb1A-wk_ZX_9oJZ-opfhErYuzOv25Z6yE6fbbEhh3foriNWkmy7aTiOlGygsEeZwTzu2EmE6in7oU3EVH5I-alNZEDB67clvJOdYkrO8aCwGo6R5Ucvj9aoF0rFqB_fUIAF1WtmWJk53Qr1-4u-bVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8324686f63.mp4?token=f8wtvCuk7qTwkKKacPe0R2leQ1DSxO-VA9y51mtOMs0nsHJSR7LAnVmP7I3fPLIHwNK2LUp-o_r4dFwJYD7vBSVVRcsvDm1etRJH2Tm_9qhf-h9um4SEOab5MIEb4rxZxGNREfyCb_06GVqdo4gCRFCCKo_cpcPRil-KnrI6qpde7DzOzUO3nVjg7GdWsr89Kb1A-wk_ZX_9oJZ-opfhErYuzOv25Z6yE6fbbEhh3foriNWkmy7aTiOlGygsEeZwTzu2EmE6in7oU3EVH5I-alNZEDB67clvJOdYkrO8aCwGo6R5Ucvj9aoF0rFqB_fUIAF1WtmWJk53Qr1-4u-bVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
دیس سنگین ابوطالب به هادی چوپان!
هانی رامبد بهت برنامه نمیده؟ خب تو نیازی نداری به برنامه بزرگ‌تر از این نمیشی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107915" target="_blank">📅 13:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107914">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05980d89a2.mp4?token=n_EZCrFOLaETF6qRgeixXOEnTu5WYyMEoq1i7hZ8r8pbr4PN4X4rF8CWHIMZlnCW0uyRHcyFbQt4d7tcjHtnjqCiuTQj1kQJZaEY3uIyve0CjYvOXXxZv0I3wEf9Z7pW3yFDx4HswQxCq3und72qudmmSdRBtPG1os4Ojbgv8gWabNxyNFzT9PNsUhfC0_RYgohe7lrKqYnJCj2lqxDX9L-jETVjvjPXEI7FaVhL3Zvonk4s0uSKHT3sSqqq7TcY5TIUS1edyDuD-H2z0CDkGYKOnUgTBTZvPUoS_-Er1EVnJ5P3HJD0J3IwqH1kvkMz_m4a_Vzp_KbacOezRyPsjKohLYmwPT3UfvodUwFIutlWf1CVgi1SkqwMDgOUSJ4y2Ar2qgKDPYPkNna2vYAjDH6nNriuj-a6SvjNvqh9dlld2_teuVrpwE3BvY352zbmkjglOLeXvdK1KnVgyl-7niOkejT4-vZjCT2w9OzoXbfMgVZZgHRr5X2ttGSP7qguo-_kc9Cv2NQGeHuS_ABMBWz1T1c6xZi_p44B0qn8Va3tsASzj5iSwZzXIIev_uE8hI8NV7agVOpryd9I2ogQDLmQ4B5s4p3gU6aXpebMk3eqP6mfloVKlgU51oHPn1PbcFrfeg0eqV0vsV3xOaTzdEkqXYy93X527iIlYPvaJ28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05980d89a2.mp4?token=n_EZCrFOLaETF6qRgeixXOEnTu5WYyMEoq1i7hZ8r8pbr4PN4X4rF8CWHIMZlnCW0uyRHcyFbQt4d7tcjHtnjqCiuTQj1kQJZaEY3uIyve0CjYvOXXxZv0I3wEf9Z7pW3yFDx4HswQxCq3und72qudmmSdRBtPG1os4Ojbgv8gWabNxyNFzT9PNsUhfC0_RYgohe7lrKqYnJCj2lqxDX9L-jETVjvjPXEI7FaVhL3Zvonk4s0uSKHT3sSqqq7TcY5TIUS1edyDuD-H2z0CDkGYKOnUgTBTZvPUoS_-Er1EVnJ5P3HJD0J3IwqH1kvkMz_m4a_Vzp_KbacOezRyPsjKohLYmwPT3UfvodUwFIutlWf1CVgi1SkqwMDgOUSJ4y2Ar2qgKDPYPkNna2vYAjDH6nNriuj-a6SvjNvqh9dlld2_teuVrpwE3BvY352zbmkjglOLeXvdK1KnVgyl-7niOkejT4-vZjCT2w9OzoXbfMgVZZgHRr5X2ttGSP7qguo-_kc9Cv2NQGeHuS_ABMBWz1T1c6xZi_p44B0qn8Va3tsASzj5iSwZzXIIev_uE8hI8NV7agVOpryd9I2ogQDLmQ4B5s4p3gU6aXpebMk3eqP6mfloVKlgU51oHPn1PbcFrfeg0eqV0vsV3xOaTzdEkqXYy93X527iIlYPvaJ28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🐐
حالا محکم بشینید؛ این دور آخره …
چهارشنبه؛ ۲:۳۰ صبح - پایان ۲۱ سال سرمستی در لباس آرژانتین؛ رقص آخر، قدم‌های آخر، قرار آخر
🎬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107914" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107913">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-Tf39QShKdgvZB7QbIEfDJGgvwDk-UwVbQP1RmJWdHhYUqmqOqeC60ekl_XbS-ppJFFNn7QS6513mCh--tVDv_wcnRdG6r7lJxo18ZHxhu6HaLYtTKeXJRY7exoS9dytOFRKaREaH3PJzYzk-wr2Lqu9EXZxmxHprcSUN40-39P9AYHs9J8ltqwKDc4l1eccU01P-9mEWK0Iq58AsZLSI4PcIZYEC2tIufScS8PrPXx2tnpOyY488p5XPEe3ll5sWINXyRbzyI5Cn8C9t4fQSwjzTqiDSZ99Ex8iQY0KfPVykQDoUkxGc8Rifv8MdtdMH1ZYfdRNmXOFFv2DHFVuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
👤
۱۰ رکورد اسطوره مسی، با تیم ملی آرژانتین:
1️⃣
بیشترین حضور در فینال‌ها: ۱۱ فینال در رقابت‌های قاره‌ای و جام جهانی.
2️⃣
پرافتخارترین بازیکن آرژانتین: ۴ عنوان قهرمانی با تیم ملی بزرگسالان.
3️⃣
طولانی‌ترین حضور متوالی در تیم ملی: ۲۱ سال.
4️⃣
بیشترین بازی ملی: ۲۰۷ بازی.
5️⃣
بیشترین پیروزی با پیراهن آرژانتین: ۱۳۴ برد.
6️⃣
بیشترین بازی با بازوبند کاپیتانی: ۱۴۷ بازی.
7️⃣
بهترین گلزن تاریخ تیم ملی: ۱۲۵ گل ملی
8️⃣
حضور در ۶ دوره جام جهانی و گلزنی در ۵ دوره از آن‌ها.
9️⃣
حضور در ۶ دوره جام جهانی و ۳ فینال؛ تنها بازیکن تاریخ که به این رکورد رسیده.
🔟
اسطوره جام جهانی: رکورد بیشترین بازی (۳۴) و بیشترین پاس گل (۱۳) و بیشترین تاثیر مستقیم روی گل در تاریخ جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107913" target="_blank">📅 12:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107912">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e79f527d7d.mp4?token=fo7OGBEhZBJDrCyVAqAVFl7wzsteRkNfqn8ByowohI_G51AI5S0u-Xih2LE_QdlZNqCAmF2rxzqDIOinXFrjmDDbGRtWXND4UqMykjJdmqMUYUs5Dzf7GTrociyQLjn_bEY6fjq3iZtUz7MhOu9S3PfsMyT1p6kYop85GyplGLWOqXG2IaL7LEFmcTVIS5boAeaZQgRPjNQJ8EAAJ1q4NZQg5fertMtlvbeLf4KUwtJKfgQmK4omjIz25AHTtsWMWmpCGNm3iJ3pdSC2mkghcHt_tdgZVKCZLo28CkxT7Er8JcudtNwZ9wrcUhC5SznyFF6rKKaXgAQeAFQgERq3cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e79f527d7d.mp4?token=fo7OGBEhZBJDrCyVAqAVFl7wzsteRkNfqn8ByowohI_G51AI5S0u-Xih2LE_QdlZNqCAmF2rxzqDIOinXFrjmDDbGRtWXND4UqMykjJdmqMUYUs5Dzf7GTrociyQLjn_bEY6fjq3iZtUz7MhOu9S3PfsMyT1p6kYop85GyplGLWOqXG2IaL7LEFmcTVIS5boAeaZQgRPjNQJ8EAAJ1q4NZQg5fertMtlvbeLf4KUwtJKfgQmK4omjIz25AHTtsWMWmpCGNm3iJ3pdSC2mkghcHt_tdgZVKCZLo28CkxT7Er8JcudtNwZ9wrcUhC5SznyFF6rKKaXgAQeAFQgERq3cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇹
ولی این رسمش نبود ...
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107912" target="_blank">📅 12:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107911">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f83cf644f9.mp4?token=XEMKC03WzXWGe1aPhJEbnasv8tRw2dxSYuYcyng_8uz1lBY3yjuX_nZQgIUBZYG2Zi3f3QurHduDII8JpSQy28aIai0bCFTptTKYlWiikfqGn7i-rVywLw4zpzvF1IE92hzcgV3S-1zm2Msn2pIVH3ZUbVFU_VesRz1WaYsP5rh3E_UMS8hpR41fGuGLv3hVJ4OBq3JvTi6B-MHKuAYAQV7xCdx52RMu8BuD3XYts1yWywems1L3ueWaAiuuwvkHn5qhUzqNE6rvK2NfRec-RCYDIEIJLqQJEPq9zNM30bEeXoOF_RCKPBHYUlYtyu06QIeoisZm_-LuelVK-fFK4Xl-ZFTHSvzUQc_3avIOmbevViZk-oPoLc-H2MwXZtITqg0TbeTVxW88QdOYde9oVGjoem4JNoVioUWYb8xRzDRhG9WDAJKBQYundEaNMK0KnbcbsRI_tFr-uq2u0zG3ROb2vgpdlXGB-aApXLBRa8nFP4BLqkQuB-QsygKyIMwlnj3tVypJesZSZYxLmS2eukULTlLy8bTbDtdt7JtMhv09PFxf_iKqWLomnpxmZLnPM-2cDMBNxXyuc-4fMr1YoiQX5uYnjOqZjNpr_ADrW7o2ZIC2hzod2WxA9jP52AMYyBdWndE5qcikPOISMFfnRj3tNA0_TxB1FxMs_AlUHBI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f83cf644f9.mp4?token=XEMKC03WzXWGe1aPhJEbnasv8tRw2dxSYuYcyng_8uz1lBY3yjuX_nZQgIUBZYG2Zi3f3QurHduDII8JpSQy28aIai0bCFTptTKYlWiikfqGn7i-rVywLw4zpzvF1IE92hzcgV3S-1zm2Msn2pIVH3ZUbVFU_VesRz1WaYsP5rh3E_UMS8hpR41fGuGLv3hVJ4OBq3JvTi6B-MHKuAYAQV7xCdx52RMu8BuD3XYts1yWywems1L3ueWaAiuuwvkHn5qhUzqNE6rvK2NfRec-RCYDIEIJLqQJEPq9zNM30bEeXoOF_RCKPBHYUlYtyu06QIeoisZm_-LuelVK-fFK4Xl-ZFTHSvzUQc_3avIOmbevViZk-oPoLc-H2MwXZtITqg0TbeTVxW88QdOYde9oVGjoem4JNoVioUWYb8xRzDRhG9WDAJKBQYundEaNMK0KnbcbsRI_tFr-uq2u0zG3ROb2vgpdlXGB-aApXLBRa8nFP4BLqkQuB-QsygKyIMwlnj3tVypJesZSZYxLmS2eukULTlLy8bTbDtdt7JtMhv09PFxf_iKqWLomnpxmZLnPM-2cDMBNxXyuc-4fMr1YoiQX5uYnjOqZjNpr_ADrW7o2ZIC2hzod2WxA9jP52AMYyBdWndE5qcikPOISMFfnRj3tNA0_TxB1FxMs_AlUHBI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
آخرین پیش‌بینی خوش‌چشم، کارشناس صداوسیما، از تاریخ وقوع جنگ بعدی ایران و آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107911" target="_blank">📅 11:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107910">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pM9UVWhD63VyGhP5bi49aiD4MOL7NhgGnI5cpyWz03RjXKH33rk1TUHxkoZOpUiQ3uhdPwTd63PgZ-cBR67NmbsoU7nWEffPbZLIFgDMJfv0bDMq1_FlM_gakcAjddcDxvcpDzefmn_YINQjsyCDWPBwGPbSgWaiWYT0FUxoE-pq5FK7NHWKYk-tbHufUd0xSJwEA8JW6RXL6HRDLAK-2XZRMJDRAH0WqaTa3HN2XK54k1sxibZEaWSbkJoBSi64Q2nEw3_zijT6arrImTUkCpuVu9cQ8XuEWIsb55McPbukWkRkQHRe2IE2Zd5rJLxDsyGFRuveMScLyaPCCP0-BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
مصدومیت حبیب فرعباسی سنگربان استقلال جدی نیست و این بازیکن به دیدار روز ۱۶ مهر مقابل تراکتور تبریز خواهد رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107910" target="_blank">📅 11:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107909">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477e1b7cf7.mp4?token=Pzl6l3sYKPq9Qjvz4kRnxkP_mkkaBdIwLx33NsCsTqzrwVEnDmGgkit3r0z_dpr9xm1XGI4hftahIAAMDh5d4frBp_FTIbU50ZLTiZ8jGQlCCLzmhi_noCOywR0EsKr8dZvOY7v67Gu_sNoiD1IhjhGMErjipn5tfEnB-LL4HlryAVxWlz7unnjNZMvMqVJpVDcmDuuEOhFXZXfKo4TugBWNfQhSADm58qfTXCYC0A3etAcJ_g6B8ryaoO3P4McvgW6GqnugRwpdznMkZRy8D9QIJt7xErfdh9tVwoTXHiUcKO7XjQWWepA32dkYcVIUsLrqNdD2o5sRJoDOQVmq1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477e1b7cf7.mp4?token=Pzl6l3sYKPq9Qjvz4kRnxkP_mkkaBdIwLx33NsCsTqzrwVEnDmGgkit3r0z_dpr9xm1XGI4hftahIAAMDh5d4frBp_FTIbU50ZLTiZ8jGQlCCLzmhi_noCOywR0EsKr8dZvOY7v67Gu_sNoiD1IhjhGMErjipn5tfEnB-LL4HlryAVxWlz7unnjNZMvMqVJpVDcmDuuEOhFXZXfKo4TugBWNfQhSADm58qfTXCYC0A3etAcJ_g6B8ryaoO3P4McvgW6GqnugRwpdznMkZRy8D9QIJt7xErfdh9tVwoTXHiUcKO7XjQWWepA32dkYcVIUsLrqNdD2o5sRJoDOQVmq1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
ادامه‌دهنده مطمئن برای راه پدر؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107909" target="_blank">📅 11:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107908">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eeed962e7.mp4?token=VGS3XCtTIDq4QLKgBF89xjXu7gSH1vWv82_nqs7aF9t8vvdACNR9Npvy_eKMXyezyE3PqhBijqSZRbb-fX9MeoT1NqVGo-6nkM69bYdUyPL1G1e0x5GqaXC_QoZOYvoaU8Tv25SkBRQAOXvMFJTdq2iuMhr1DrHa_nHnsywVdOpzHHUvhakXDygqJfuDB6Oym6KvpMWDgrXSww-Z0HlcKUa3wOUnJ73VCQN87Mx52inU3U_4ixIw7rE4HgMwgPsB4o4wc427sTykGcpkFKhPaZ8ig2fJhFZiWUuUoISgvO63zcrQfH4AWGHfxk9cFRE6s-2ZtHnW3iG8EjUdspn-9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eeed962e7.mp4?token=VGS3XCtTIDq4QLKgBF89xjXu7gSH1vWv82_nqs7aF9t8vvdACNR9Npvy_eKMXyezyE3PqhBijqSZRbb-fX9MeoT1NqVGo-6nkM69bYdUyPL1G1e0x5GqaXC_QoZOYvoaU8Tv25SkBRQAOXvMFJTdq2iuMhr1DrHa_nHnsywVdOpzHHUvhakXDygqJfuDB6Oym6KvpMWDgrXSww-Z0HlcKUa3wOUnJ73VCQN87Mx52inU3U_4ixIw7rE4HgMwgPsB4o4wc427sTykGcpkFKhPaZ8ig2fJhFZiWUuUoISgvO63zcrQfH4AWGHfxk9cFRE6s-2ZtHnW3iG8EjUdspn-9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
تعجب علی‌ضیا از تغییرات باورنکردنی دختر بهداد سلیمی؛ تو ده سالگی هم قد خودش شده!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107908" target="_blank">📅 11:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107907">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107907" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107907" target="_blank">📅 11:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107906">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PG7jLc8YqFmTSYbp-KEMfTrNHA6nl5DOBYv5AdmX-AfUVDuN-ecQ7wXJ3WG4pyQAhVnqf10XWHLUSO3hU0af5P3kY4WqrfcoAuBfliC_MfSAt2eP9m8GmZKb-YcSglh7_nfMzlUO_rQcfN8aHUvvVO5HXzTGWEdZv0JrnElAZamIpJFkVyq6DGKFy9dDU-FvJFkIs-rkycSlvZvdRDNhooPn3MbRN1vD4Go2vHwcjy0yFYAZOHqkVP8qqmgbzrzxqgJZH9kB-HY0FZi4n46hP0jhE4UR3M3CxM1k-yFJ4yofrgVrih9vTVjmtks4nmalM685CMs084jsoM2f-kxJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
اسپانیا
🆚
کرواسی
چک
🆚
انگلیس
اسلوونی
🆚
اسکاتلند
مقدونیه شمالی
🆚
سوئیس
ازبکستان
🆚
کره‌ جنوبی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107906" target="_blank">📅 11:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107905">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906a8b3b0f.mp4?token=ohNuh3ncDCaA-qQHv6B_gAiN8xIdeFcpxOgq21GX9VvKc0Wf4PQA9b1GVHffUKIQgGMGFPBGhSLg8gNq2YEQmVATp18nAVrhUVZbxkBNO3CcZYyFB9b8EUeH7GgGRBVFw1q8-COSol0wYj0LwT3dZWAO_nkMFrJjV65laKN91xbe2Aq3Qwkp7KPe1yY_i5hFI5evcr68vTW2mtxzI6c5vUIA7PVcqZia0ylKqYjkjcdHfsJBaxMqbr_9WxuBIp_flTbnryqlBa5PvEJQctRPd8CyapZN_mKXlfypsfD4orO5TaGg05eCbWeydribEsNWGWJcy1nVeikdUCC1CVP4dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906a8b3b0f.mp4?token=ohNuh3ncDCaA-qQHv6B_gAiN8xIdeFcpxOgq21GX9VvKc0Wf4PQA9b1GVHffUKIQgGMGFPBGhSLg8gNq2YEQmVATp18nAVrhUVZbxkBNO3CcZYyFB9b8EUeH7GgGRBVFw1q8-COSol0wYj0LwT3dZWAO_nkMFrJjV65laKN91xbe2Aq3Qwkp7KPe1yY_i5hFI5evcr68vTW2mtxzI6c5vUIA7PVcqZia0ylKqYjkjcdHfsJBaxMqbr_9WxuBIp_flTbnryqlBa5PvEJQctRPd8CyapZN_mKXlfypsfD4orO5TaGg05eCbWeydribEsNWGWJcy1nVeikdUCC1CVP4dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
محاسبه افت قیمت خودرو :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107905" target="_blank">📅 11:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107904">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0ELwcZ2slPaML9HGErkc3wpYydldzf9z1EPABzKck2ZMHTQK8Afl4yCwrPhblZQ31-_XPTYhV9t4OClgYUmFIehNxFl3oZvblKynHYdOk9QdAr4_N0o7h1InqyHjawNKGeVUVEOZ8uWEEjU3hCQ-U_R86CU4yb5SfDU-ZsMxffI6alTjMLs_4QyDQ_g31D_E0zjFbkIG9EkRTsjZTn171fpv_Ounj2lCf3zrtjtIhE32JSIJI83KNyPahdT8XJGilCoa4BcaIVeIGgywVXqsXoHRUmPukyao69xYvbZJKL_S344Z_7HhwdZoy_tWRdmmt2ROVowDd81vJoaNzky8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
بیشترین تاثیر‌گذاری روی گل‌ها در این‌فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107904" target="_blank">📅 10:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107903">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KF6C0l5xhEASsbTbBca9u5ZRlTRayxQIKW6VEhHbSjwXVpmEawfFwUsk91x4xxgj10VINwBEHDpPl9caz3AejTae0OvJ_uuOIzfVTmLuKCcbZT5WON2TUVyiUBnvUTxF07fLqfrDhMHEmRcmE8uU3irHS9mjx20tPvAs_8bGyPisMHsmw62uRfSv4JJHa3_g39ZUaW84Wj39kl7JFQJm2S1NpW_buHmqsfvTZrIC64uoN9VTZ5zdpd0cN0JYPTyHijUWpqFt7ZGJagc0kTfvezqk5QEfBqsYiAIJtFjfpshkIEpUgaK_hsKO39uJKb8fdF8nlYuPhkvrk5ymnYn7og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوری
؛ رومانو: قرارداد رافینیا با بارسلونا تا ژوئن سال 2030 تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107903" target="_blank">📅 10:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107902">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sslu7IOQ0bEZv-D5dZ5vpMRqK9sth1OFmy5uRE89uNfMwwzx-iQwkkS0VThqd_Jj94jcQzfzFLnNt2CMMWNxFodtFbIdIsjCTEO1uOYMGOj4CtWymKpRiOTMrxfD0NbxT0BoRzObzBjugvbKTn7yjcS6339zoklMtwyglTSt2RRIBn5xCuH4qAFTvoKgj2I5bsp888CkEAnfSUefG7n_d51NzJHGdKjYc0JXnooP-uv-n9_Bu8Kx0nBYxRKnLMx3AOctUUCA4s85uAAwh9Vh6AXNWJnWzLKVaWsEEIs5DUbSwBNiyjOCE4WgKcoF4OKj8kv209PZMEnzUfhDgXeDkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
معرفی داوران دیدارهای هفته ۸ لیگ برتر
🔸
🔸
تراکتور - استقلال؛ داور وسط: سیدوحید کاظمی، داور VAR: امیر عرب‌براقی
🔸
🔸
پرسپولیس - صنعت‌نفت آبادان؛ داور وسط: احمد محمدی، داور VAR: میثم حیدری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107902" target="_blank">📅 10:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107901">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff702b8d86.mp4?token=h6IyTZyFCpBtFndmbiH3mOBc4kcVmU_FfDUw7q430DpNkvVh0dITl8LjdTcLdxu9wzHTzhhplfeIPKJLjOquAP80GpkW0l7lJoM1h_1PxqPnOiVS1MgmY4N9_O0nON-3oZ8KAc38rR9Pnkg7Edr_8l_fyXC2SF4I1-FstfkJwEh_UWmvKYvJD8TKWrmbUJUmjeLgJp3xWJzip6YXRlEwvG5XM_QeeHIbnP8F_C8gmofXm8ce7X-D_Tk01wp_Zq7TsnithB_7bTG4Sx7W_BeNobAZEmyoHNEArG0K52Al6VdpTs9QFmIi046QP6bf7SRpcgseXWxoEKasRGwcRrmejX_yfXDdp-TND5JogzibVpEwfhMO9Me4O0X-lqRIbbvCEaZC7xsZIaDHPmQSqMZm5I8uG_BoTPPkI7S2M7OvPb4_vOmNzIO2CqraMd-b1mXbPrZXmncSk9TEXvAuKZ095HAPpAyYWI87cErl_U7SMoENOSt2GRnaMCIAxDteHsAZuNyYZIoP3pvFaSDD0FJgismNwa9WXmLBnSjcWvECG4m-4p0H4apaE9MdgjhHbyW9oDvejENXJOrwFn9ibAluUnd-B-53NyMogmuTR6plVVYMw_787ZVhKHWuuI9OuFe5HCwz4LsHAiQBefHvH8Hkl_tzm-LBKOaaIopIwH6v6pk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff702b8d86.mp4?token=h6IyTZyFCpBtFndmbiH3mOBc4kcVmU_FfDUw7q430DpNkvVh0dITl8LjdTcLdxu9wzHTzhhplfeIPKJLjOquAP80GpkW0l7lJoM1h_1PxqPnOiVS1MgmY4N9_O0nON-3oZ8KAc38rR9Pnkg7Edr_8l_fyXC2SF4I1-FstfkJwEh_UWmvKYvJD8TKWrmbUJUmjeLgJp3xWJzip6YXRlEwvG5XM_QeeHIbnP8F_C8gmofXm8ce7X-D_Tk01wp_Zq7TsnithB_7bTG4Sx7W_BeNobAZEmyoHNEArG0K52Al6VdpTs9QFmIi046QP6bf7SRpcgseXWxoEKasRGwcRrmejX_yfXDdp-TND5JogzibVpEwfhMO9Me4O0X-lqRIbbvCEaZC7xsZIaDHPmQSqMZm5I8uG_BoTPPkI7S2M7OvPb4_vOmNzIO2CqraMd-b1mXbPrZXmncSk9TEXvAuKZ095HAPpAyYWI87cErl_U7SMoENOSt2GRnaMCIAxDteHsAZuNyYZIoP3pvFaSDD0FJgismNwa9WXmLBnSjcWvECG4m-4p0H4apaE9MdgjhHbyW9oDvejENXJOrwFn9ibAluUnd-B-53NyMogmuTR6plVVYMw_787ZVhKHWuuI9OuFe5HCwz4LsHAiQBefHvH8Hkl_tzm-LBKOaaIopIwH6v6pk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇮🇹
آنالیز بسیار جذاب از تقابل تاکتیکی ایتالیا و فرانسه در فیفادی اخیر با هدایت زیدان و مانچینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107901" target="_blank">📅 10:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107900">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02c435695d.mp4?token=PMlvyyTPtyHZurgcR8uYC4yeqiudOs91pP0nxZuziqU0Oa7zTz4OFBpbp11ww-cjWW4Q2KgbBCbGVB0kEUXAxyzXIOnCoSbRkAFV4TA-b6y8lbejyoTlIEQYcSgEooTCLUzyyiqCmGSuH53HeIA2miV57lrAXE5qTzCGwpEKy1vjVuDDiKYBVA-qXkMZrlP-Ce6jS0QN5ByiWTaSh25NV68X8zcfskJTMjqTfNSnVP4aErF9oH6JTc2tfCOw-JfYQUgJkPFzPJtiBUvhmf5GqjdZ7_rsl0YME-K9tQSrzuTIcnsC8qiwSqxOLoerlFMPEufwYvR0qKNMDBD6RVK3dLNObOrVlMXYlHz615kquDK0BwCpKYAUEihi4muxevO8HnkGt8tjDdGspPA-hEXc1VoOTPYvHnJb5AKm0z8RkdmsAVDJe-p8CfRnsWFvjBNgoGIrXtIDPwLk3JaclewURtROoJWnWNt-eVygg99a4yIMVjidl9Vy0BCKBN87GdQQxSXKI6unr2Tjc6ET-T4GQPpj_88MykFKe2jCQsyplvAOTdV6JuwW-ZrE0DGw2NZLpPRHjl68hDFMmsJJKRX_14hhPMDTGGFoQVhlPmPM9TzISVd5EEaxTO7WoTrv0NuhRRL0XgtrRaacx7n19IQJVmp0QqnEEVKrLTa09VPBKeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02c435695d.mp4?token=PMlvyyTPtyHZurgcR8uYC4yeqiudOs91pP0nxZuziqU0Oa7zTz4OFBpbp11ww-cjWW4Q2KgbBCbGVB0kEUXAxyzXIOnCoSbRkAFV4TA-b6y8lbejyoTlIEQYcSgEooTCLUzyyiqCmGSuH53HeIA2miV57lrAXE5qTzCGwpEKy1vjVuDDiKYBVA-qXkMZrlP-Ce6jS0QN5ByiWTaSh25NV68X8zcfskJTMjqTfNSnVP4aErF9oH6JTc2tfCOw-JfYQUgJkPFzPJtiBUvhmf5GqjdZ7_rsl0YME-K9tQSrzuTIcnsC8qiwSqxOLoerlFMPEufwYvR0qKNMDBD6RVK3dLNObOrVlMXYlHz615kquDK0BwCpKYAUEihi4muxevO8HnkGt8tjDdGspPA-hEXc1VoOTPYvHnJb5AKm0z8RkdmsAVDJe-p8CfRnsWFvjBNgoGIrXtIDPwLk3JaclewURtROoJWnWNt-eVygg99a4yIMVjidl9Vy0BCKBN87GdQQxSXKI6unr2Tjc6ET-T4GQPpj_88MykFKe2jCQsyplvAOTdV6JuwW-ZrE0DGw2NZLpPRHjl68hDFMmsJJKRX_14hhPMDTGGFoQVhlPmPM9TzISVd5EEaxTO7WoTrv0NuhRRL0XgtrRaacx7n19IQJVmp0QqnEEVKrLTa09VPBKeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تضاد قابل توجه صحبت‌های مورینیو در مصاحبه اخیر خود با رفتار دیروز کیلیان امباپه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107900" target="_blank">📅 09:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107899">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6256aac96.mp4?token=CgEmKc-gt3MGVGe-EmkN9TWYHT1xga1TFfV-Akgv87CQK2y9Zr3abTTD-PkJhkPSJYQe3Ik8gVfmToWNY0-L-1awIFeyO1FwugivfJ5_Ok7IkMsRl_WP88B2cOhk4Sd0kJtEhc9QrSXxwknoUDCEpUuqIvVkrjF1TCdV3spmoYosos3-Y3jmoGHbtYD00PNKq8z6O1OzWfR_brLt176pGJCdhJ8FFPxRFzHBvK1zYW3rk7W4tHPgfMSnUwo6MPVp6EdslfrooiRke-G0Oass6-IpMMmjV9ZwkgmGhqCWjLwDKdS92ZDRZb-Smm-5g2xMMjSd-py9e-bnVb1Qbz0PqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6256aac96.mp4?token=CgEmKc-gt3MGVGe-EmkN9TWYHT1xga1TFfV-Akgv87CQK2y9Zr3abTTD-PkJhkPSJYQe3Ik8gVfmToWNY0-L-1awIFeyO1FwugivfJ5_Ok7IkMsRl_WP88B2cOhk4Sd0kJtEhc9QrSXxwknoUDCEpUuqIvVkrjF1TCdV3spmoYosos3-Y3jmoGHbtYD00PNKq8z6O1OzWfR_brLt176pGJCdhJ8FFPxRFzHBvK1zYW3rk7W4tHPgfMSnUwo6MPVp6EdslfrooiRke-G0Oass6-IpMMmjV9ZwkgmGhqCWjLwDKdS92ZDRZb-Smm-5g2xMMjSd-py9e-bnVb1Qbz0PqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
پرتغال بدون حضور رونالدو همچنان می‌برد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107899" target="_blank">📅 09:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107898">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522303d3e9.mp4?token=ujeTc3m7zZa4wqUGmQEhQrfg5GCSjSRoZ8_r4G_ZAj9AW3sbEN8qzfVxe0iafCxLixiN-6Q1m2sAo4lYs-rh4j_2pLMZ5X07ciygS3nXj0dnPvQ0vCvJ7kblZXWTs8vq_zz_lpSDaDGntVcXyjsu537-FV05yZS6o_oXLiwmctWRdRv5aAzIjjD04ZrGZBLNsA7e1_cvn_HF-m0nHk8MIng2Kb8ESQVwHS__Jmt8YkFXbQ2gIPGPSWDCMF-iZB7Mpft5ANjF5K3vCIU0N6XtEIHGuNciVoCiNdKVQY9cc_mRk_YnRY2yBdKpDZ001PR3uU33Q7_mIN8uN2lMcOHOXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522303d3e9.mp4?token=ujeTc3m7zZa4wqUGmQEhQrfg5GCSjSRoZ8_r4G_ZAj9AW3sbEN8qzfVxe0iafCxLixiN-6Q1m2sAo4lYs-rh4j_2pLMZ5X07ciygS3nXj0dnPvQ0vCvJ7kblZXWTs8vq_zz_lpSDaDGntVcXyjsu537-FV05yZS6o_oXLiwmctWRdRv5aAzIjjD04ZrGZBLNsA7e1_cvn_HF-m0nHk8MIng2Kb8ESQVwHS__Jmt8YkFXbQ2gIPGPSWDCMF-iZB7Mpft5ANjF5K3vCIU0N6XtEIHGuNciVoCiNdKVQY9cc_mRk_YnRY2yBdKpDZ001PR3uU33Q7_mIN8uN2lMcOHOXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تماس‌ژوله با آناهیتا درگاهی عمه مهاجم تیم‌ملی وسط برنامش؛ بهش میگه فوتبال ما عمه‌ای شده
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107898" target="_blank">📅 09:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107897">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25bf4f2e86.mp4?token=fmXsY8YB0eIot5CTrUymtCzJuOhjbC73axEzxa2l4ltzuxDMezgfrxtvudP8bdJjdL0gGVuC3racmcKg8bcneVgXpr8tXoCexpbR70TD5bEZUvf9K5T_tj3PWDjPmBe_sGU1XOgXYDXQ_uBMzk8-Fg_Mg-8BdbWJFVkyEWXefWPaPnGDmMe-2HpMmGSN200W6e46r_nBV8X0TzZamqNpPxuKnc2caZuZP76GAXnK4onyhDawzwi9X_2lzhbCgL84wkBy_qjWA03NKO_-d80MRY7VQ5Nz5gRY_ZDZG4btEwA--CAwQswAH1QsAxWMNhi7DwqRmUO2iIGvREjVeRcRlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25bf4f2e86.mp4?token=fmXsY8YB0eIot5CTrUymtCzJuOhjbC73axEzxa2l4ltzuxDMezgfrxtvudP8bdJjdL0gGVuC3racmcKg8bcneVgXpr8tXoCexpbR70TD5bEZUvf9K5T_tj3PWDjPmBe_sGU1XOgXYDXQ_uBMzk8-Fg_Mg-8BdbWJFVkyEWXefWPaPnGDmMe-2HpMmGSN200W6e46r_nBV8X0TzZamqNpPxuKnc2caZuZP76GAXnK4onyhDawzwi9X_2lzhbCgL84wkBy_qjWA03NKO_-d80MRY7VQ5Nz5gRY_ZDZG4btEwA--CAwQswAH1QsAxWMNhi7DwqRmUO2iIGvREjVeRcRlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
حجت کریمی توهین کرد، علی خطیر تهدید؛ کریمی: تو دلالی، خطیر: دادگاه می بینمت!
❌
درگیری شدید دو عضو هیات رییسه پیش چشم سخنگوی فدراسیون فوتبال در برنامه زنده تلویزیونی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107897" target="_blank">📅 08:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107896">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4798a06f34.mp4?token=ZdIddWiToV0XEmxlO3YIC3immjCl-2WzZm0ftXJLipnfxwqtgFzeLbxmxACc-IWn3wRHkYzRLcqqV0DeehCAyUjC6-xKrHOH1roWhOEpfFkcXQ91NZUEJUMPIbkoUTm1yZMyHhBvMfqsp67eAttrwL0kWPaKpZlf-fDtuQFV_xGlF-jTGP3G9n8wWV9mQlWi0TiJ5pOR2ZpJ09Nz1O1cWSc1dKUxT4FY72nivIG8wv1LgxJVVfxEn-JGfDXVziK_OTgSyTKh4Zg6ma-9AEyG2M8jo9D1mEVSMs-R3PstWUpapAlexNGl0SbC4kyIU07BFtvfQQv8c3VYNNV4Bz4l5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4798a06f34.mp4?token=ZdIddWiToV0XEmxlO3YIC3immjCl-2WzZm0ftXJLipnfxwqtgFzeLbxmxACc-IWn3wRHkYzRLcqqV0DeehCAyUjC6-xKrHOH1roWhOEpfFkcXQ91NZUEJUMPIbkoUTm1yZMyHhBvMfqsp67eAttrwL0kWPaKpZlf-fDtuQFV_xGlF-jTGP3G9n8wWV9mQlWi0TiJ5pOR2ZpJ09Nz1O1cWSc1dKUxT4FY72nivIG8wv1LgxJVVfxEn-JGfDXVziK_OTgSyTKh4Zg6ma-9AEyG2M8jo9D1mEVSMs-R3PstWUpapAlexNGl0SbC4kyIU07BFtvfQQv8c3VYNNV4Bz4l5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
خطیر: اگر آقای گل‌محمدی قبول کنند من همین فردا کل هیئت رئیسه را متقاعد خواهم کرد
خطیر: هیچ مربی ایرانی با ماهی 500 میلیون تومان سرمربی تیم ملی امید نمی شود! کمترین دستمزد مربی در ایران 70 میلیار است کدام مربی سرمربیگری تیم امید را قبول می کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107896" target="_blank">📅 08:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107892">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3867ed322d.mp4?token=lFU2svwo1JU9iTZeRkQqnm6McfQaSviRNQryppiWCXdQRWSCBVoMdajmaq2dm4ynSJTH5GdG-x3qsWr5m73nc2D6yhkOrTirMsRrWzPQMVA7t6GsWmWQXKQIWREDH4yrZNHDj2l1_Si6jmD2M_BICn5-jzL7UWVI1S1Q73Cke5VBB9NaIzffh1d5MhvvpnVRk-5GU1I-CmG71Q0uoRo4a_mvhntUgscCqQ9iddHNI9aud3EF1x0wXvnxtlyBXiYMqLhpuoUElVkjHPAhxnvVT44BO6kSRAOZm5zZTMdH_3ndkaUHgIagqh7aRNtmEUfccAnBtlx7jw_7Lp83eqbZOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3867ed322d.mp4?token=lFU2svwo1JU9iTZeRkQqnm6McfQaSviRNQryppiWCXdQRWSCBVoMdajmaq2dm4ynSJTH5GdG-x3qsWr5m73nc2D6yhkOrTirMsRrWzPQMVA7t6GsWmWQXKQIWREDH4yrZNHDj2l1_Si6jmD2M_BICn5-jzL7UWVI1S1Q73Cke5VBB9NaIzffh1d5MhvvpnVRk-5GU1I-CmG71Q0uoRo4a_mvhntUgscCqQ9iddHNI9aud3EF1x0wXvnxtlyBXiYMqLhpuoUElVkjHPAhxnvVT44BO6kSRAOZm5zZTMdH_3ndkaUHgIagqh7aRNtmEUfccAnBtlx7jw_7Lp83eqbZOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
لحظاتی رمانتیک و شبه هندی در شبکه سه
روبوسی های واعظ آشتیانی و علی خطیر در پخش زنده
😂
پی نوشت: گفتنی‌ست در لحظاتی از این برنامه واعظ آشتیانی و علی خطیر با یکدیگر درگیری های لفظی داشتند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107892" target="_blank">📅 00:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107890">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4ZHWzS-PkmxUT7DKRBlrsLNAea3HNwWgtaGyvbDWR90z8pW1Ps-dw7UNWsOe6B7ooCcV05acghwUdynye6CLQuj70sChRCb-msR3-7j2SWVqMm6eDXAp1NQmgHqmjLDr40TDgyCe18JFePEiA875vMDxlJuQGk1qLV1uMVPEm9SfSkxk9ACeZu_QMsDb6YM6S8exa_qMLivHTGcuTkhqUiVmF2in4_C8l9zUeSN-EDmovqF614Ylsm94p7JP-NxFn1K5EPMLjNvW0IEDKlYz3Z-3ztmZ8k2ysHhsB4SMdCZ9hr8Ey21tA3M6fHvr-YUTx4tbTCuJ73TRiIGSapUBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m_4ecsuWp31n_LmMShtGykU4t8N77VhmlegXCUbgyTtR1VH6Oq0NIIbtjxKVOKJbi8RFQrLbAFEDZvYiNyzoksD8maIVU3zA5BDrTJ2IjidOGHBpJjxf-rIusg-vEZXp4raDKWAGR4Xvk9ZVN4MHTWcKWbk-vBiPgkBq8hH1ysVtS_VGnRQQSOqNQxFj-cPEx1qACmD9cvnjr0BH61QIFU1kTGiaVG4cToE0FoUR0OclDzLR_aTUO5e4BynPMGz-4lLQ_8XuiIQU8jTDP_gV3NAMwI5xK0prcSd9i7iUf7SciWSJkF2C1-AkHEtU-aSgITRubXq3b1UDQ0-FdfNYcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
ترامپ: نمی‌تونیم جلوی شیوع طاعون از روسیه رو بگیریم!  این ویروس بسیار کشنده و خطرناک‌تر از قبل شده و مثل یه ارتش شدن! حتی با پیشرفت چشمگیر پزشکی هم نمیشه جلوشو گرفت، با این حال ما به روسیه کمک میکنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107890" target="_blank">📅 00:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107889">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIriAz9WVQFq-Jt0-tYS0cfl6DwjiegSce8M0ID-sBWbdgW9jm8N-PiqdIDidfXyEPdhbpcVhhcjU2l1RwWb1GTG78PSmuignB454zqK42SzURUlyfMUcn6Aj6wQuQDxEXRwyHRC6zt0O5CvS604QYufeeALutLJABE_iCuZJS3FbpTCuWa-GHpL9hAdbRWYJRKtqKlyxzCczUqjiC5d3eXbbhWMhIekqN7WN1ng4_wWLC938wWhSV_Uo79AC3Kgk2U7r6z9UZI5LkcgTXtJoBt7nEYfbK0O_YC4DzRGdQ9WCXExJG29psWDFCtHn07Vg92rUkeMwJ89H3dID62HcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
✔️
لیگ‌ملت‌های اروپا؛ ایتالیا رفت و برگشت مقابل ترکیه پیروز شد؛ تیم مانچینی سرحال نشان می‌دهد!
🇮🇹
ایتالیا
3️⃣
-
1️⃣
ترکیه
🇹🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107889" target="_blank">📅 00:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107888">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3c5cdf08.mp4?token=vFf6UKTXxPlfkdc_so0IROFXLOxxaWeo0QiRwm6aaeaD5lo6bXrKCbSN1W1IFCSjznjB-Y4rvyD4hdSxayL8eIoqYEKeNfvPk0pEL5efs862PYWt1AGSuh2dMrvftygJfkYI_5ABnsQeBiywVqLncKFWc9tdoxZuNrCPAiA-o86n-mZ6O003jk83XefkOU0lOcnVQMRFhfGPRtzxoFDzi1kuA9OYmyb0-0OHsYY-IhJMitcGwE5TwYI7lzrbrb2F8RgqVUS_DX-jinnq0LNgslCRibrVqvl60z9TWrty4hfYl1KZY_Ri07mwSlJ8OJeyqvnYBiFX0UxgeTQig53w7TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3c5cdf08.mp4?token=vFf6UKTXxPlfkdc_so0IROFXLOxxaWeo0QiRwm6aaeaD5lo6bXrKCbSN1W1IFCSjznjB-Y4rvyD4hdSxayL8eIoqYEKeNfvPk0pEL5efs862PYWt1AGSuh2dMrvftygJfkYI_5ABnsQeBiywVqLncKFWc9tdoxZuNrCPAiA-o86n-mZ6O003jk83XefkOU0lOcnVQMRFhfGPRtzxoFDzi1kuA9OYmyb0-0OHsYY-IhJMitcGwE5TwYI7lzrbrb2F8RgqVUS_DX-jinnq0LNgslCRibrVqvl60z9TWrty4hfYl1KZY_Ri07mwSlJ8OJeyqvnYBiFX0UxgeTQig53w7TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
درگیری لفظی واعظ آشتیانی و علی خطیر روی آنتن زنده
🔹
آشتیانی: من فکر می کردم نفرات اول و دوم فدراسیون برای پاسخگویی حضور دارند
🔻
خطیر: من هم انتظار داشتم با نفری صحبت کنم به مسائل روز فوتبال دنیا آگاه باشد
🔹
آشتیانی: همه آقای خطیر را به عنوان ایجنت می شناسند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107888" target="_blank">📅 00:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107887">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff62591c17.mp4?token=cET2CFEXaZ00CynDaAx7MGgWn0rLjaqvqZC24tnpSwBSefDz8F-Z7-_mnLLRLM9QQ9f6xpowN4y-Vr6FME33p73zKYTNlNdE-SgJ7rX_7evo4CXH00Y-G3r6-4Dj5eKHKBu_wsYq07LkuwkkeQMdUZQf843XLQfPpK4X8tpkeYX2DW3lh-37UKJGE9pvN8LXBHsNYb0mWxHmzSqpLdT_LBexxW3Zlk6gg3zf5ojHkEWlagSySzSEmLYopvgAhPP6O1chT-ghWsoetK-dNpVCHGuYc8lr-SmO4Jql8uezuVgleP8u90H9te67cK6LkiPbvMDhdSh88GNpxidKqFGQsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff62591c17.mp4?token=cET2CFEXaZ00CynDaAx7MGgWn0rLjaqvqZC24tnpSwBSefDz8F-Z7-_mnLLRLM9QQ9f6xpowN4y-Vr6FME33p73zKYTNlNdE-SgJ7rX_7evo4CXH00Y-G3r6-4Dj5eKHKBu_wsYq07LkuwkkeQMdUZQf843XLQfPpK4X8tpkeYX2DW3lh-37UKJGE9pvN8LXBHsNYb0mWxHmzSqpLdT_LBexxW3Zlk6gg3zf5ojHkEWlagSySzSEmLYopvgAhPP6O1chT-ghWsoetK-dNpVCHGuYc8lr-SmO4Jql8uezuVgleP8u90H9te67cK6LkiPbvMDhdSh88GNpxidKqFGQsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚨
‼️
میثاقی
: فیفادی واسه تیم ملی ایران بعد از بازی دوم تموم شد، درحالیکه ژاپن همین امروز بازی داشت و خیلی از تیمای جهان 4 تا بازی انجام دادن. قرار بود تیم ملی با گینه بیسائو بازی کنه، دیدن تیمه 3 تا به نیجریه زده، بازی رو کنسل کردن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107887" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107886">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/berpiyvf4eDb7wvZwsJdlXuljPkhv3RTfkuZcqLYcYmCrhmTfw_39WHcYm8tu893SZxELCndUyrg3vAw8xhGZhCDC0cYMUt5t4YjdxFZFas8bCt93ajFUWXFy52tuBee7pyaxWXddmsl3JITH2zJAPPjBVxeSKK86TynNpsK_HeeWPGSk_bjJCkUT6kcWDFi_LLX5Emm9FX0iLMy34mmtYX-nAdVRa1aOorck5D4SFXyzy94RX31toN9dkJNf6S3_Z7uGvChZRzDKaEe5x7Y2x-p8SyD3ZMwFH2vahSEh7OAtQORN3Y7LxKMMo1r_XfbgfWI5wfU3vrQn9oBbdWppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇺
لیگ‌ملت‌های اروپا؛ زیدان نیازی به امباپه نداشت؛ اولیسه و چرکی ستاره‌های خروس‌ها شدند
🇫🇷
فرانسه
4️⃣
-
1️⃣
بلژیک
🇧🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107886" target="_blank">📅 00:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107885">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jh-7wDzern-1jha0KLsX_iHAayZLBznJy_GRXAxPv694A0H1_ws5-DK2OA8HlsNPmoC1JdqxJ2pyUiaxokoqHAh-7RXeU2ztBrO0YO31sxEDST9G3B1PAJ0luN7QqOT3zxj3MOGlhbRoWAVG0d1FcFzEaSRUmrqbAMPC6ZQZMw6VmR6pqpXX04pmmoA1xAawM9EAt78iWPZsYrjqPyKaTifXs7tlCfdj9qHgspLKU6yTKGUlqwVNw19Ox91JO8Ea8Th2LHBcYhrD7Ya5khWuEnYhifXYH98eohFfIgkOzl9wKgJXKOzP7ubkdHd8SU97CZyijKaaF8tW4FmgLL1GTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇺
لیگ‌ملت‌های اروپا؛ زیدان نیازی به امباپه نداشت؛ اولیسه و چرکی ستاره‌های خروس‌ها شدند
🇫🇷
فرانسه
4️⃣
-
1️⃣
بلژیک
🇧🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107885" target="_blank">📅 00:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107884">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_AyNaX-vmW9aX2PJwsSvpmBsBme6Wzwtst54BKLn-M6TOyk8wAMNztCGpQdq84o2JZP8pHDUmWyk8vGGynhyZutRww2mfcE1rg-KMs7248mE7A0-4qAi95qL6FO6ESy0WiKAGaKD-lSI4Od_vsLfr0oWwK9RGhc1S0zJg4_YWpfdxi4uARqUcd2mQ6djbWTtVPb7xBZuk5lHl7dcpyLF5AAavMv2Ws1MMoKC9OhLoOk9xiyUEMS013KJJtxao1c1nvc2_1f7E_ctBW52JiuswK9C0LTPPu-cO9vPJe3Yluyd4mlDyvWIcTIJ57_Ke-R2HWVl31c8ytY1k0_XBTTZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
✔️
لیگ‌ملت‌های اروپا؛ ایتالیا رفت و برگشت مقابل ترکیه پیروز شد؛ تیم مانچینی سرحال نشان می‌دهد!
🇮🇹
ایتالیا
3️⃣
-
1️⃣
ترکیه
🇹🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107884" target="_blank">📅 00:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107883">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25f8a10c9e.mp4?token=qxXrM8WCjtQWZSOLaaJhzjsrEh9lU2PNSzGD94X2lpNwTExgU0Ola21NSJ_jRJXtpj8GWR0KqtEkcPXSRjUZvHPabUB4nHyKPDrtsdyCCXCczlQLG33Al5K3Xluv3e7YTFxBOxgRZF1T8Zjy7YQJD11lv88a0BM0W6NULbH8ALnJa8DgcT8Dxvmb_Th0D98PRjYHIpDsg43OwEN3aTaEocSeznBnZQrMoyG2Vk3VfOpX522EKe9EOAMLyhzzNOaMa-Z2hNZcJNomElokivXJp18JXFOM0gfdbXbwS3G6hGh6OU4nxd53w83dsPZEJOUn-rUmMEe3CC5eYDjrpK1pwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25f8a10c9e.mp4?token=qxXrM8WCjtQWZSOLaaJhzjsrEh9lU2PNSzGD94X2lpNwTExgU0Ola21NSJ_jRJXtpj8GWR0KqtEkcPXSRjUZvHPabUB4nHyKPDrtsdyCCXCczlQLG33Al5K3Xluv3e7YTFxBOxgRZF1T8Zjy7YQJD11lv88a0BM0W6NULbH8ALnJa8DgcT8Dxvmb_Th0D98PRjYHIpDsg43OwEN3aTaEocSeznBnZQrMoyG2Vk3VfOpX522EKe9EOAMLyhzzNOaMa-Z2hNZcJNomElokivXJp18JXFOM0gfdbXbwS3G6hGh6OU4nxd53w83dsPZEJOUn-rUmMEe3CC5eYDjrpK1pwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ترامپ: نمی‌تونیم جلوی شیوع طاعون از روسیه رو بگیریم!
این ویروس بسیار کشنده و خطرناک‌تر از قبل شده و مثل یه ارتش شدن!
حتی با پیشرفت چشمگیر پزشکی هم نمیشه جلوشو گرفت، با این حال ما به روسیه کمک میکنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/107883" target="_blank">📅 00:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107882">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bb309807.mp4?token=eJmlk0ZVpxZqgYP_-bszexPw_gFkzH5OkpXMIpGCekbpHckf1-QOPzfxxxMxUzh9xtW5xxt5n2cjAj61wCJwt1mDcTbP9CcrMYvhTk-1RVeAoP2o8CWG_0JkSteMA7DEgBphVlSBVRzAFErEui7S0_R3orlNl0BoPI-iAgsDYLvjU73mEziG1xOJFjbkoKUhLOH2_fzHIMUnZyFMwHfl4AI62TPJTQGniAnmE5IomSqKWtHlLeLpl8VT-0amgwX8y9gD1m11huWprTy2pe371g9pEiwNM8NWuY7unjaCXXoCl4IY9P866x8Xt5QIJ0qGDKysbx4jgfdD0haqRa6Rlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bb309807.mp4?token=eJmlk0ZVpxZqgYP_-bszexPw_gFkzH5OkpXMIpGCekbpHckf1-QOPzfxxxMxUzh9xtW5xxt5n2cjAj61wCJwt1mDcTbP9CcrMYvhTk-1RVeAoP2o8CWG_0JkSteMA7DEgBphVlSBVRzAFErEui7S0_R3orlNl0BoPI-iAgsDYLvjU73mEziG1xOJFjbkoKUhLOH2_fzHIMUnZyFMwHfl4AI62TPJTQGniAnmE5IomSqKWtHlLeLpl8VT-0amgwX8y9gD1m11huWprTy2pe371g9pEiwNM8NWuY7unjaCXXoCl4IY9P866x8Xt5QIJ0qGDKysbx4jgfdD0haqRa6Rlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
خاطره امیرمحمد رزاقی‌نیا از هم‌اتاقی بودن با رامین رضاییان: سنش را بگویم ناراحت می‌شود ولی مثل یک جوان 24 ساله تمرین می‌کند و در دویدن باهم کل‌کل داشتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107882" target="_blank">📅 23:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107881">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d63f949c.mp4?token=KsCIuSGDLRjhoS_pcW0naASrZAFyX-PcOYcmwjxsfZ5CNaDQ_i6KhegJrDuHcIq3G-LV6wGSCvVEoalZdkE4P32H4NOQ9JfFrxtwvCGcqKBGHd8Sv6Tm40KzAMo7ubDPqnRQNQoTd-Pj_tRjVscBGHnDT6tk3_2-hyQsjfM9dBPPDX7s0GvWDG6SQ8dUm1hxujIGH4jIR8cGvthxPBaTnJevzdrMKNwGDesmEjWETS60N_9Nas0s86VJYY1iQ19ZKhxTJI-ywHRpMwVgSUeKjIK3DOkp0b6r2LVDg-M4uPdijbMSuhnUstLudgUs-eplhAE_SNusR9oWD1USd_KeTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d63f949c.mp4?token=KsCIuSGDLRjhoS_pcW0naASrZAFyX-PcOYcmwjxsfZ5CNaDQ_i6KhegJrDuHcIq3G-LV6wGSCvVEoalZdkE4P32H4NOQ9JfFrxtwvCGcqKBGHd8Sv6Tm40KzAMo7ubDPqnRQNQoTd-Pj_tRjVscBGHnDT6tk3_2-hyQsjfM9dBPPDX7s0GvWDG6SQ8dUm1hxujIGH4jIR8cGvthxPBaTnJevzdrMKNwGDesmEjWETS60N_9Nas0s86VJYY1iQ19ZKhxTJI-ywHRpMwVgSUeKjIK3DOkp0b6r2LVDg-M4uPdijbMSuhnUstLudgUs-eplhAE_SNusR9oWD1USd_KeTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
سنگین ترین پرونده مهریه ایران اعلام شد:
اقای جراح ۶۳۶۰ سکه مهریه برای خانم با وفاش زده بوده و الانم تو زندانه
+ تا چند نسل قبل و بعدش هم جمع بشن نمیتونن اینو پرداخت کنن
😕
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/107881" target="_blank">📅 22:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107880">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
‼️
🇮🇷
بعد از پیمان حدادی، موبایل همراه مهدی تارتار سرمربی پرسپولیس پس از تمرین امروز سرخپوشان به سرقت رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/107880" target="_blank">📅 22:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107879">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1743ee1f5a.mp4?token=u3dpUspVbI-rkwm9xt_ZgEChNo-N27RxqDW8wbAUZ4OyVoCtUjmMNU8phqm8kSdJ5hWGSACkYpkHq2654_aHiE5F3xF6Q27u2lWJhAGfgOBM4yDiNfuYSxTMQ4XUjGQxEvzEHV3jZh7QH-Tr7VRuBDIqoEBe21P4zT0dxu1gnUA12MLNc9fO4Gxs4bZtqMPrFPnHxtt9PND3_lJVuh8OYXs4p-dHYldGbEIGdmOBXYifH01pdo_w0j4wi8PctgyDreQKnx-68k3g6TwHF1dLtxtFyBhC11oVFstKKlbi1pzlsCpfqWAHDIGiovHM933rFSXaMs9ZOJZnogTzqbxP_gwmkt--IvLGg9vmQn8tx4_aUWO2HLbVlweTTCXL7ldJKgLNQHZ2GspsoO67VrpWtYhm7hJN61uvlgKF2_8dAVmCjXbcvdrd0SlHWn-OegDQk-TUv50OUXBPjG01U6pI5CTkSP9qxPE4U5vBh_1egST_agq_Dma_WIr4dkOdt3IR7q2zlKUMZucgG9pSjBpU4zjk06zN-_BctQJVFm1al1rQvH5j1UuBxi87R7L0sZrjNiIUPGQ8Ndb7BXOfEcZWwmRtAwVaPIYrN2VFiAoqQcFN3TbnD2XtaigQErD775P3rYtRJM6pYZabAk89r6-ht6BfNFmzmDhFA63BofFi7SE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1743ee1f5a.mp4?token=u3dpUspVbI-rkwm9xt_ZgEChNo-N27RxqDW8wbAUZ4OyVoCtUjmMNU8phqm8kSdJ5hWGSACkYpkHq2654_aHiE5F3xF6Q27u2lWJhAGfgOBM4yDiNfuYSxTMQ4XUjGQxEvzEHV3jZh7QH-Tr7VRuBDIqoEBe21P4zT0dxu1gnUA12MLNc9fO4Gxs4bZtqMPrFPnHxtt9PND3_lJVuh8OYXs4p-dHYldGbEIGdmOBXYifH01pdo_w0j4wi8PctgyDreQKnx-68k3g6TwHF1dLtxtFyBhC11oVFstKKlbi1pzlsCpfqWAHDIGiovHM933rFSXaMs9ZOJZnogTzqbxP_gwmkt--IvLGg9vmQn8tx4_aUWO2HLbVlweTTCXL7ldJKgLNQHZ2GspsoO67VrpWtYhm7hJN61uvlgKF2_8dAVmCjXbcvdrd0SlHWn-OegDQk-TUv50OUXBPjG01U6pI5CTkSP9qxPE4U5vBh_1egST_agq_Dma_WIr4dkOdt3IR7q2zlKUMZucgG9pSjBpU4zjk06zN-_BctQJVFm1al1rQvH5j1UuBxi87R7L0sZrjNiIUPGQ8Ndb7BXOfEcZWwmRtAwVaPIYrN2VFiAoqQcFN3TbnD2XtaigQErD775P3rYtRJM6pYZabAk89r6-ht6BfNFmzmDhFA63BofFi7SE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
کلید واژه‌های تکراری قلعه‌نویی؛
همه مقصرند جز ژنرال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/107879" target="_blank">📅 21:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107878">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
‼️
💵
عادل فردوسی‌پور: دیگر حوصله شوخی‌کردن با قیمت دلار را هم نداریم
روزگار سخت و تلخی که سپری می‌کنیم/ شروع فصل لیگ برتر، با دلار ۱۸۷ هزار تومانی، بازگشتش از فیفادی، با دلار ۲۷۰ هزار تومانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/107878" target="_blank">📅 21:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107877">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc2122fb81.mp4?token=PeEtMwlJEkxV7VShKphuOSG9-IB7ahcbu9fmvN7KL6Ss_e-fNFaNzpPiNn9aYQnldcnb1yn9AH8X0aE4cwHhjVS2-_Hs3njJqaYDonDj9MmCE2Q_C1DbA0X8cbzM8eYJa3dA24-DzP5xmv53iF33z-o01HOqXi2AsvmA4E0ifk2711ggMAyhU5WM_RK7145kT4cUHhOB66OrO9vpHi84NywdR6GJGH9H_kuyMittPEdAwmXK7oWJJSXDJJL5yhfPokeLTiUyE8e4MyhgUi5FlDLx_WapMht9uyEhYgU400hu31Tcrt0ysYeE2uAo4-cwj6vrUBh2fh9Gg8Msxzw45yCYXrJFAmO4XAeQOJ1yEk6V48rXZW730im0FsK8wyWB8Gk_f5LBIjo5F6LIxUJXsaXzBXhGkGz5I1L9UxNtfJ6OFqdzsYB0BlJU0OXuC7Q6-TJ-pbBQ1TDEH62eslk3PlUfLs3e_pvTgrAE2rkzfSm_UnwtX4G4n983fUgYberfywrCF-pnRzTah8qVRtdA9DCrWA0gFB_q4TSCkODtNJ1qgrjcD_aBMliViSdWYsby5UAfRwivQvSAv1-OEDJFFRUa1p46P0qhJEe-4DmUhlwEgX0Y1Jl5sB4DJhVuN3iRYTxotxgm2BTfHvCmV97_gcziDNFDHnZDIqrRrgMBxgY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc2122fb81.mp4?token=PeEtMwlJEkxV7VShKphuOSG9-IB7ahcbu9fmvN7KL6Ss_e-fNFaNzpPiNn9aYQnldcnb1yn9AH8X0aE4cwHhjVS2-_Hs3njJqaYDonDj9MmCE2Q_C1DbA0X8cbzM8eYJa3dA24-DzP5xmv53iF33z-o01HOqXi2AsvmA4E0ifk2711ggMAyhU5WM_RK7145kT4cUHhOB66OrO9vpHi84NywdR6GJGH9H_kuyMittPEdAwmXK7oWJJSXDJJL5yhfPokeLTiUyE8e4MyhgUi5FlDLx_WapMht9uyEhYgU400hu31Tcrt0ysYeE2uAo4-cwj6vrUBh2fh9Gg8Msxzw45yCYXrJFAmO4XAeQOJ1yEk6V48rXZW730im0FsK8wyWB8Gk_f5LBIjo5F6LIxUJXsaXzBXhGkGz5I1L9UxNtfJ6OFqdzsYB0BlJU0OXuC7Q6-TJ-pbBQ1TDEH62eslk3PlUfLs3e_pvTgrAE2rkzfSm_UnwtX4G4n983fUgYberfywrCF-pnRzTah8qVRtdA9DCrWA0gFB_q4TSCkODtNJ1qgrjcD_aBMliViSdWYsby5UAfRwivQvSAv1-OEDJFFRUa1p46P0qhJEe-4DmUhlwEgX0Y1Jl5sB4DJhVuN3iRYTxotxgm2BTfHvCmV97_gcziDNFDHnZDIqrRrgMBxgY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
تصویر تکراری تیم ملی
بازنده اما طلبکار و با اعتماد به نفس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/107877" target="_blank">📅 21:22 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
