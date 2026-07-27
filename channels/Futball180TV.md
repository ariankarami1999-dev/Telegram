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
<img src="https://cdn5.telesco.pe/file/lKncEe7zBz7hl2UtJeuPpgnKfuCPXOwvPTzoD0p5IjFq_XCbCXF3ItbfU-zhpyNq1VYevMMacTHrKPV-IBEasGUU9c7oPmmEN5c8vlECoEuB6Xi59ViWFUrTMnXAb7RdruTqKGleeFoMlIHUSOyjv4MO_ffBvFJtxmsUq_yZXD9SoTs3kqLxi9mYM1VK15cd3GMddzAx0yG_B35h0QgFOd0zcucmXMJlfBF81guHVdob8vnnbZL-mGNV6HTpXe2LkXo0zdp-MbJpkc3SkCcCJ8mdu-hKTAob4OZGjS_OfiL4IEiVZNx3lpPJvl1azLkBEWAaSG2pefYKXa6n3EP-aQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 523K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 15:42:25</div>
<hr>

<div class="tg-post" id="msg-102067">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/orUoyUrhagI10YDYWkyYeyQMy0kGQj3JrY7QTNQcyFVnEdRXezLAoe-Qlxr3KNqhjG4OBO9U5jl80Q0arc3_7CB06Eswpr0FZqeGRnjdcw_avDn1p_a1TEQoio0yq0yVeed068kW4oZYmJKj7Um4U2Oq0hBmMSmTWjkAgckyCsLpvm0RLZ8zXY5GgkmSjPkywXSnQ3QlcdZEihnYq0H_tDuwaSmnAA7-F5Ry1rprmFu0Ro6IHkQLz7lM0_p-Dxo1q0qVHPkwtYUxpLbtK1DFMspu44SSZNvL1eNS_Cm3xQBBZ124VLWsyHYWILx9qTmUB2SXrSys3X0i_pDiV2QsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hz0DKsiVEbL-yb0JqYu3W4rWGK5xEjTRd5cyhUGbvHDXivqXiaFYxgZ3BXDKE_WKWZd_44ugE-aHwK3kpt9IlI2JuvexxCpnBFhz9NpQsFFci__hn1pSLcHtbvLqndhS_tWumEigkJM785xzz7eZni0uFB36vihBTPs8Mjq8p_NPN8M2q-_5lLy1ttjeZ2LJ1AOJRccTrQi0TrY90Uq5XhLFIi1QK00Z0vTxAyCq3aWlgLn_hLHhqbp3lg42_CHA6V3AgkQw7JD0L95qOMgiJR2QMa3bErIW_DgTBNts4vQqORYVFVBfd36deefieQkf6cUgCtVyl33fyw6XScEyhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A4D4XFOCDkFaGoVzJOqYAKtBUsi4pFNlCASqCmqlUqtZvFOngq5M33H7ZWE-Uu6wGnBtJB8aevnQYIcbYPzYKXDTghTMccZkEEuo9SZBKoaEazaVvEwE1pt-5afNaLGwIRdQnytryqka0WJFidRF21qZQrGYgp6_-JJjOR6YMyj18e-1uFBCo4sbKrbmuIetiG9s4TFpPDdv_eYJrBYb5JTesIheLMmv41cZEAgICGrxJes6OI9dDpKmPk_tfeRhKXmLSVG5qNj88kcVpKi5eUa2w8j7IOvuqyxmtU3aavJjHQRen5Kav049cV_E5n4Y7Kh5irTiPNVzJL5IIOYIRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایشون که تو تصویر میبینید مارتینا گونزالس دفاع 18 ساله بارسلونا هستن؛ حالا هی برید پیگیر یامال و رافینیا باشید درحالیکه اصل داستان جای دیگست..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/102067" target="_blank">📅 15:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102066">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
‼️
انتقاد شدید امیرحسین صادقی از مجری خانم شبکه دو سیما بابت انتقاد از قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/Futball180TV/102066" target="_blank">📅 15:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102065">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f32263398.mp4?token=H2_Q_-EuvdZbJwsLT8pf8Ag-5pgq3jNQs3stmOK0Bb9iYsJ8x6gRzyukvbOrakh3fyYll7SDZGpUwqVYPX_S6nJDPM-CSDiEAmu6XT_8HDhLC86AOcLeLGk_ZB1evlFoYFTbFWEINsMw6fOpaoBsfm0KIRBJHl59mbidcMLjLCxx5lIgJ0JEEAj4Lceqki1NT-qdrdOeu6OojUp9vVsg1Mu4C5iKMJGGgToSl84dGBNBgmKl-hCPqHlI12SMUyGzgFqWizYzJ6e6DdeRvu1or1L6DT3Y4tgCr4Ya9Y9qHltE7ahhNf4Lx8v2xHh6NMM3qZfg6khB2NymEKkZiIbFJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f32263398.mp4?token=H2_Q_-EuvdZbJwsLT8pf8Ag-5pgq3jNQs3stmOK0Bb9iYsJ8x6gRzyukvbOrakh3fyYll7SDZGpUwqVYPX_S6nJDPM-CSDiEAmu6XT_8HDhLC86AOcLeLGk_ZB1evlFoYFTbFWEINsMw6fOpaoBsfm0KIRBJHl59mbidcMLjLCxx5lIgJ0JEEAj4Lceqki1NT-qdrdOeu6OojUp9vVsg1Mu4C5iKMJGGgToSl84dGBNBgmKl-hCPqHlI12SMUyGzgFqWizYzJ6e6DdeRvu1or1L6DT3Y4tgCr4Ya9Y9qHltE7ahhNf4Lx8v2xHh6NMM3qZfg6khB2NymEKkZiIbFJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزاله اکرمی بازیگر: رضا عنایتی کراش دوران نوجوانی‌ام بود
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/Futball180TV/102065" target="_blank">📅 14:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102064">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lwl5GwU2_WPSyeLM1apW0RGYIAmjIzoaG4Y9cZECh5E8YhcZu2p_QJAwTHIefPEpGo93op2Y7ttC3Hjm7PJvTlo8PTEFT6fa7XkTXkBYkROryu5e7EHHSnrHA2G0XykKfv5iqQv-5_5s9rZ56B-aU7xvHiTWfU1vUte6m3ODBacuijZlYY1raeMXkU_Xy3kUcJ5GjEimO7KwJXH0Yzfh3Xqm62odUxpbX1GAhniR385L6ngj6a_KZpqEfOzthSCSzjoh5PvtUpzxoLM2FFt4vWL1l8nUA67zsgjgST0XmoCq3liUepDph3WatTu6QqW5qYxmPEqAmhHaBXioEP0i-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری از رودرا (ESPN): رئال مادرید نسبت به احتمال جذب رودری خوش‌بین‌تر شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/Futball180TV/102064" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102063">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQUrjA11MZubmEyqcAn4iqMlwLNQvajPRbX9M_V7uKDvWYXrwECak709F4RRs0vntqirshjMv3V2OcMjQa2cvJGxJeKipBYXEdNA6dJSkmy0RP6-iIYJXmV2uCzrNEKCB189WM7_-FcS5w0NeUeo9tQ8zQebRmlq90c4KcvkdzVCnT5CgiGp15Uryn3uhGJMhbs76AJA4tw4FvJwCicuZCzjiwyEYO3H7aF034MWpsT8vdfdNR7UAuhSLXl2qutA96yT5SgUe_lXxo9ZOW2KzgglrDMrtZ_TmMw9VtdZCe9_MQsn1VDQQR5Ougj6OrBi-S55pM4nQYcmEjruynG2jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
اسم کوکوریا تو لیست رئال  برای لالیگا ثبت شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/Futball180TV/102063" target="_blank">📅 14:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102062">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sChJWF5oIqWhzwWNzfmoEAPh0zNCaca8H2dbM9QBESmABJVxkZlWLKFD-FtaWuTvmUeoNUG4zRx4oOlVMmUpX49nhFcTk3DqAR0SvAnJxmdZUCWb20-rhQTf-V8oft7SFWCL2_AZjGjqLp-_XZAkEQj6iGdg7A8v_-mmyCoIJsbKM2_IjZSTBRQm_yNpRMus1qnrlIjCX6FfdYatryUaWDSWwyxvMV9rIfftolJKGtke87OvNdR7CE54OlPNmizb76Pz5SnSK9G5A1SCyNqnPOSeGEhVX29zcZM5UMXXr39km8oSvZ0IPIbVjEaZfCSXoqByPKu19NKUdBV1qaxpYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
مقایسه عملکرد نیمار و امباپه و هری‌کین در بازی‌های ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/102062" target="_blank">📅 14:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102061">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2084d796e5.mp4?token=Ppuw877SF89XUEkTsp5yrY81aPaMBifrt8rHcuxvTZp3r0UXwvxpiMfSZ6GMHhKGbM-95C1ekuse2FkHvBSbLe-NmQg8zV15Q1dgPtzIMvDDETN1zKhRPSBoWu9MePSRSbA8LmP2ciIe_H8BWEPql_PHNcj9jrc5tolXgHoeoDCmdY6st-TDGaOabJ8CcbSk-ubkecZhkLbBKCKMn0IRCdwmL8R8QXSFSWuyQyW2n8go1wu4IX6nV2Ux2oJZ8QMQKG0jsh5tD5ODYKvqaSInrELeEUdzKYYSCZTAuhX4PLuTyigECPVRsY5kSA0yBzR9LCuloNgDotolULFo3_RIzr1iVg1LCexEeKwlQx75jeezp0PgLPyVJDchwNJpR1sxYPmBe1_ZXTMZL9MRx9UH2D_AyLD4zYYrBDZTkNH2-b2MO6hJmngRZfMBL-9NIMHmqJ9mk08VaUoO0Opr5JkJE0fBxrnWYfgw-_NRTQqxC_gDHxV4a2-Afzlo6RAOjAyP0vKa21rdQRtZVmhk1O7ZvT7kf6DZqNGVbUQf6kta0nBlIUzlCN7luIX1ZB0I0aS-3T_dvHaTfGhxDtWLz56MpMhg65_77SOayEK8tYK7kBnRT0FWpary8MBBqjv1XdI5hIffOZXdnmSTUNRQQ0BL-_M11XHMkEttMYyqPsfMEYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2084d796e5.mp4?token=Ppuw877SF89XUEkTsp5yrY81aPaMBifrt8rHcuxvTZp3r0UXwvxpiMfSZ6GMHhKGbM-95C1ekuse2FkHvBSbLe-NmQg8zV15Q1dgPtzIMvDDETN1zKhRPSBoWu9MePSRSbA8LmP2ciIe_H8BWEPql_PHNcj9jrc5tolXgHoeoDCmdY6st-TDGaOabJ8CcbSk-ubkecZhkLbBKCKMn0IRCdwmL8R8QXSFSWuyQyW2n8go1wu4IX6nV2Ux2oJZ8QMQKG0jsh5tD5ODYKvqaSInrELeEUdzKYYSCZTAuhX4PLuTyigECPVRsY5kSA0yBzR9LCuloNgDotolULFo3_RIzr1iVg1LCexEeKwlQx75jeezp0PgLPyVJDchwNJpR1sxYPmBe1_ZXTMZL9MRx9UH2D_AyLD4zYYrBDZTkNH2-b2MO6hJmngRZfMBL-9NIMHmqJ9mk08VaUoO0Opr5JkJE0fBxrnWYfgw-_NRTQqxC_gDHxV4a2-Afzlo6RAOjAyP0vKa21rdQRtZVmhk1O7ZvT7kf6DZqNGVbUQf6kta0nBlIUzlCN7luIX1ZB0I0aS-3T_dvHaTfGhxDtWLz56MpMhg65_77SOayEK8tYK7kBnRT0FWpary8MBBqjv1XdI5hIffOZXdnmSTUNRQQ0BL-_M11XHMkEttMYyqPsfMEYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
درخشش‌های فصل‌گذشته لامین‌یامال در بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/Futball180TV/102061" target="_blank">📅 14:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102060">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap50rvTiVleX_PK6zusjXmdq49VexkkU5OWO2dnuv22MO0cBJ3Ka8ylrKSOytsrgmyxFTAIp12qZmQZMB9An6q5Ul9Dh2TV6F151hmdgHOIhTZuqR-EvcJ6SxiT4LKPDv3iPFwhz5GV9LZIBpcXrmTXwXAviJN6At4KBmv0hZocs9zHZg6kr68JislmNj_j8hsk545cLGuCu8bnUwvJILihN5oDddnW57UkThFIs1BCLsdVMwlzGPAY-01i2dz8wwPWa5MMVJo08mAmWgwlbtmKAUy5zhF8Ybel3gtYFoolnRG7WFJLQzF8AGSm1KTN-f7nZth_fw5TsS5Is4SJyIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽
لیست بارسلونا برای سفر به انگلیس برای پیش فصل با حضور ترشتگن و دیونگ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/102060" target="_blank">📅 13:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102058">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLipo37XpQRJjMrnscnAYXoqEfri71pujDL5k7G6bl76kaqnvqlgACOqEYvfRbwBVHteqZirmXB053r1AaW2MPROLO9F60BSBzP677rU1X2kdbqyfqswCMFSSjDmLTjE3ONt4kQQIe_fWsBqNZ7XIoBLe9pqV2ld_i9ULo12ECr7lOGT3WgmY66ntFrxJ5glanmx3z1tebaAK4srROS9HRc060ropQRHNUQm2nPkseHBq5cWIA5T_P6kNCTrbewPlrwZ3fBrhXw30H4H9TccqgNyZnxW5DBrZRfrK04AYCnaXYy45pp01qDYwCSH-HhQ6EubzqrGhtWa3CwUgzcu3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/olfgU8RdiVcLsHfeiGMsAO7ClXoANC8-2Xranav4Wgk18KM5UfNlFBHX7Habs8zabT2ETZpab2eQIwVWKO2W1YOwl9-LJslyRgpp3PCUB5wINz0S4WirdASasMNUWnxBr-BmQ4raXwgxlerM_mrUsnFC2ZaKcJhYWBMgqBgG6RGtnxeHnwMCfIzYI_xxmkTlAkoaPLwLLLz8CksXCGEgfWEnnjTXnVyLN8tt_V8EueOCJxdbFt5xj6wMzbKs6f2at1jcUszFw1cfB9053c1LXatw3tz4kEslnAIxyPzxhptFQ9BnwPtfw9HBC_CxOWUcMGRK4ocYZ6EcTITxlavl9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
نیمار:
وقتی در پاری‌سن‌ژرمن بودیم، از مسی خواستم پنالتی‌ها را بزند، اما او گفت: "نه، من برای این کار اینجا نیستم. یا خودت بزن یا بده به امباپه." او حتی برای هیچ‌چیز هم بحث و جدل نمی‌کند. آدمی فوق‌العاده آرام و صلح‌طلب است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/102058" target="_blank">📅 13:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102057">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/772e430691.mp4?token=oMz0AeB5Iq5BtLiMfpuZ20Lf4WlKK3QxdsYL2PNQ0tbSpT_eqwibMuq43uySvg9LZHLCfwtFmpWYSzZVrge-e39OhKdEy0Xj3eczbe6AcW1mPTZoeFiMrxeIc0NnpRH6rJ0_GBHJ8L9cJTduzNJWLXuIB-t28yR9dtHFaGfcX3RRTZ7I1eGAEm0geZrBl11MVNa1sc-wQPOxQuwN8NAfZYWitvoNDBV53BWsS1EECr0KdA7fM69kx7EVCTip1D0rU6izSI4dTw6K513qODtlKcOQ2QfzKTjzs--oE9-zkNEk_MBIjRAI2KM9dpkqR4y5ghRKWDet54sfUFmckOXu-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/772e430691.mp4?token=oMz0AeB5Iq5BtLiMfpuZ20Lf4WlKK3QxdsYL2PNQ0tbSpT_eqwibMuq43uySvg9LZHLCfwtFmpWYSzZVrge-e39OhKdEy0Xj3eczbe6AcW1mPTZoeFiMrxeIc0NnpRH6rJ0_GBHJ8L9cJTduzNJWLXuIB-t28yR9dtHFaGfcX3RRTZ7I1eGAEm0geZrBl11MVNa1sc-wQPOxQuwN8NAfZYWitvoNDBV53BWsS1EECr0KdA7fM69kx7EVCTip1D0rU6izSI4dTw6K513qODtlKcOQ2QfzKTjzs--oE9-zkNEk_MBIjRAI2KM9dpkqR4y5ghRKWDet54sfUFmckOXu-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این جامی که داری میرینی توش آرزوی خیلیاس پسر جان نکن
🌟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102057" target="_blank">📅 12:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102056">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwtbYgdT2wmo10EvZmvSzTFc5VYiGOa-4uS6QONHfn8upRb8smCIJRVWXFQJdcB1XfaF16rUOTKsF4zm994BxmKveuORph0AjRGikt2nJOI87Q63k4S3axcSX_LeOFcoAWUHpAKvbfinCA9ENUwhqXafkYTrARVGfhYu8qbfSgzOeamoXnZcZN4nuTLNyva3uhOqHNe2NvPxlsZRJZ0Me7YGInLvWqThKMsuERAEk0XUktx5tdP6SC_Du1dzmSHKKxKlyvCDXH1Ju9mgW9SnISlnCZe5jFe51Sgl2EXTLX2fottxBtRnocnIdlDeDDk5p0n7F4yIoKJkQMf1J3vI8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇦🇷
بنر هوادارای بوکاجونیورز برای تیم ملی آرژانتین:
ممنون بابت تمام این شادی‌ ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/102056" target="_blank">📅 12:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102055">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
🇮🇹
✅
پائولو مالدینی، به عنوان مدیر فنی جدید تیم ملی ایتالیا انتخاب شد.  HEREEE WEEE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/102055" target="_blank">📅 12:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102054">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebffP0JjbQ747RbG-W2N4qx4aM0NvdWinoQ9a73MUpQrrkYp-F26pbxoL4SDUJcm0zY69_-qjm4dlhodKuADiW5M99KatHxU_Nl6Ags-bj1_UE3YFosDU8ytZcOk_rzj2OLeGjRZMPktl-xYnvWSvk0FTfh6DZAtPYVx66D3dBDu6ZA5vbCQ4QxBd50stJB3EhNH2xVLy9QUXjPbKBL-5LpjnE1gM6kOUgK7i39hdohPdCibVCM1N2gvgnQ47rNv5Z6X3N4SlZIzcF2QsmC6C_k-JrCElmU1dF_52x6Cpzq3u03u5F7nn0gtScnkFwXSOZy5U1WC00oNCO_5b9q5EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
الهلال به کریم بنزما پیشنهاد داده بود که به هر باشگاهی در لیگ عربستان که میخواهد برود. اما بنزما این پیشنهاد را رد کرد. این مهاجم کاملا روشن کرده که هیچ قصدی برای ترک باشگاه ندارد و این خود الهلال است که می‌خواهد او را کنار بگذارد. در واکنش به این شرایط، بنزما خواستار نامه فسخ قراردادش و همچنین پرداخت کامل ۱۰۰٪ حقوق باقی‌مانده‌اش طبق قرارداد شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102054" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102053">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChWiwSNlUgBsASpCasJpnNAivaqFAflA6zuiz-x7oZGxmXGn8Hf3mzDtZH5B8qZMnN_ysCGgPWD-IMdpLYIcIrWt9YCA8VeiW6TMGR4pmN7Bki_QPeEGp1wD99WfoeUB4784yl2cvm4wTp0JPe4Y9E4RgR0OHIu4JAUkd-Q95GhoCxlNWa1-fpXFtDV_HLKKkmOHCSUa0NC_DhrNaEEAtwzg2ewNO97BCjUf99d6jrBHSfGk1IO_iHbU5ZCOwBhGbhkHwjGf2Y8YVUUW6ET9MuRS9pG6C6q_cT_7MjmhWHsZ7zvVivSg4Kd4WG_ydzLaC02lP_tANHKeu2TNr59X9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا رودریگز درباره اولین دیدارش با کریستیانو رونالدو:
قد بلندش، بدنش و زیبایی‌اش توجه من را جلب کرد. جلوی او می‌لرزیدم، اما یک جرقه بین ما شکل گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102053" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102052">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCE4XnxmTAfNmJ5hRr6W3ajuo-_PnjnLMuEFzwhnqAE7HlLSdxcLYYAh2kQDHRLhTwO5NglIBF6_irEhvU4zzxFmyIbWt9L6MCB9S985e2Di5VTLUhgtxQLPQHXvhnNcWRA78RVWNb-VayM0GKQt9p5eCfJwtElfLfsjFErWa512ticBcJvaVhZTzVV2eQM678eJ-O-CsxWw_TAsRWkXMJRSMW_A-ftVPKSMgoQjO1oV9ns-5ndHXKKQu1kAWEZoKJxNm0vwF7Rh5TLFsnh8ZLl3FSjU-DgLLUwy2sNi1k540PhWGGfJXaTidFWmJp3VXiyOvtq_S8ioTo9WD7Tadw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برناردو سیلوا و ژائو نوس به همراه زیدیاشون تو مراسم عروسی گونزالو راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102052" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102051">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/809e9f523f.mp4?token=VouvFJkG23N0HP8tXpaFKUxovjucc050dS3Ddoy7Xri8O4Og9PduEjRwzRrmRIQOQWtF2tuNXkm0km5Qfpu5gJfcayO2jOzsHjp899Sy_jYxLgUyrdLcUfjMEIInQFEKWIf6GKKy6f-IQ5YN2Lk5qknaaQBTSsFndN5HN7fMassbxDdf2X2IeBmnCyiQNnZP0tBziDaPiiltG4rSCzQBoYtVpdn-7d2C5x-WLdyBuU5gvgUWUVBNWA9hGWkT7wq-zX-HQ29toHb3xEJu-id9UaIvjkjaNss9sH21Lfh0uBw1gUWobFM8upBbbXpB_RyALX9D_44zRLgOP7MRPjwipQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/809e9f523f.mp4?token=VouvFJkG23N0HP8tXpaFKUxovjucc050dS3Ddoy7Xri8O4Og9PduEjRwzRrmRIQOQWtF2tuNXkm0km5Qfpu5gJfcayO2jOzsHjp899Sy_jYxLgUyrdLcUfjMEIInQFEKWIf6GKKy6f-IQ5YN2Lk5qknaaQBTSsFndN5HN7fMassbxDdf2X2IeBmnCyiQNnZP0tBziDaPiiltG4rSCzQBoYtVpdn-7d2C5x-WLdyBuU5gvgUWUVBNWA9hGWkT7wq-zX-HQ29toHb3xEJu-id9UaIvjkjaNss9sH21Lfh0uBw1gUWobFM8upBbbXpB_RyALX9D_44zRLgOP7MRPjwipQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📆
🇧🇷
۱۵ سال از روزی که نیمار این گلو زد و پوشکاش گرفت گذشت:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102051" target="_blank">📅 11:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102050">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfPw_DakiWIuYvgkhOksj-Eu4GrKo0CO1SaCccJc-PMsWUeRcnYHBKlL7vCWJRycWgTBj_HENipSrXXBVd143vflM0Lsqbfr6k1h12TJJ9jE-B2CvzEwgqbfdmvp_CkPjSYVzvMAIJBkUulkQ7OqbSE52s4TBDM8ou4TzhUGUNgatP8PdyzFLl_GD3tclTPzZJpsE1gO65O_D3qiNgq4wqzQLdvBWGq4Z0kB2nrpnkKIQ3YlGotOzYq7aC0QHFDWgc783ez7MKMxq-7CObBVeKGz28J0fr0F-ITSaGUpuRZMyMQr9SXkYSUwIlXjZ2K_RcFPd8zgEOHbXN1OjLwOlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
منچسترسیتی مذاکراتشو با باشگاه لیل برای جذب ایوب بوعدی ادامه میده. مذاکرات با باشگاه و بازیکن همچنان ادامه داره و تصمیم‌گیری در مورد انتقال او، یا در حال حاضر یا در تابستان سال 2027 انجام میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102050" target="_blank">📅 10:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102048">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ie5Uc4jlmGlSqTlO8QPQ2aCpq9qzLSDENCQjm57D5-B1FjT8hxiNl6LRNPoOxMRDOrxMm0gjynQ1ySGYioupVhXhLFohmD8H-OkYGwphfWGUPmtIzai5Sa9XizlIrhplULpAUsn-PqFKB9luL9eMtWGOpkmbZWkbRmG8JFmyJ3lCISIeYFB8wTtqH7b7kcfd9gZ1y9dnCAUaNmobLJIc_hX1kJT0Bcip7YZhIeNM2UohRsFTol4ECRJ12kxELcP9uMblqOx2MnqB0nllEUYC9fJX0eYzi54pI5qwQP8KHMNBx7vesL1Qhc4CNKbyJhtLisZodzXXlBThReafjmNk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5K9UsvBOEJm_xOFDpseRXn35KjlBbJYm0xq3a9dDPyFr3xmIqjzHbIwiHnWFbVA5hEANki65U1E28ywVRVju9VytZGhKnuVpzQxLiov9niHwoOaborVfVhSadf-iwCSWXUc1FLVki5xTRWnQsb9Hthn3s9AuuQJf5vwjE6KGw4nDgWwyuDtWGRbjlwfF3_D8kDo_IcB_sfxsS0FwLn67YeU6vURPjLmQsFy-xZdqgou7ORDtrFm-Alngk70d_K8LZ_TNZHKMJLSeJiKAM5maDuIo84oTKK9dX1kcR2ydzgn_DXTcmKv_YkB2L4ThQtEoExavQpkl-bza6lIYuDLuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جورجینا و پسرخونده‌ش که حسابی باهم گلف بازی میکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102048" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102047">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZq4GPifQ83R8SDEnhmqHe7hV3WNVwnqn286fZ1rZoEUOmqEckNJWZ3zPSSDCc_RoJdM7HdoNZmYV3pluFZazIlGAWXQqcwxsg1s0RQC5PeQG66yGHqpm9NejS9hAsHO_8kHd_FwO_xhF5C1dHEq7cr3AQLNo19UVardKnqkPfOFf3XLcOQvhwOmdPwj1Mgcak9G71AT0cYEDQqHPSTs2815IQW8Qt_oYIQJr79SxPJjEB2VBWUHkBe-N-BsfDJjq-aawJPjecWl70WIOBk-_kLQ4h8fFfEIhRYxX1A7J-KK0k-ptoVE1bxsqECIzWHrh2Osex95sl6ELnMW_QgMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
الیور کان در مورد کلوپ و تیم ملی آلمان:
شخصا فکر نمیکنم کار در تیم ملی به آن سادگی که خیلی‌ها تصور می‌کنند باشد. من معتقدم مشکلات خیلی عمیق‌تر هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102047" target="_blank">📅 10:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102046">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MV50iwe06tVwV_Y3wtKxEd9oSEqCh21VediSr16G8WLyXw4XERdh2f-bow2e5b7uwMD20g-pe7g4BWPXmoq2xshYGJuJG0_FMdlAO30STRz3-5cBwYTagu6muo8x6rG8qMVnWFXBwxfLFTgd9WVXxqDr7fnp0MgkA3vgHM0uApE2R4QHwXML3kUMycH48HNbbBVbKwvx3jg66_96XQQbjmoP-M8ojRLmNEF7DTxI2LXyf5DyNMgqvH457f19LNxtNGbgwCzTF9BWdKNMMZ8cKEyiN8K04oa7C-Fj1udGlpLF63YQ59-pOx5NDrJYesriyZS8shPo0hGfd6Tz5AapAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
وینیسیوس جونیور فصل گذشته ۱۴ گل و پاس گل بیشتر از هر مهاجم آرسنال ثبت کرد. او می‌تواند خط حمله قهرمان پریمیرلیگ را فورا یک سطح بالاتر ببرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102046" target="_blank">📅 10:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102045">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQ19ttLEK6pG9hIvCKqn4agJrRNORHih7x0Rvc6f8Mcg7PGSl3uO8NjBdZTzeoc_Hdddg-7JuEO23zWJj0IiEvL6e3nv9o3sfWPaWYs-lYk1crfh8Stg3xI1EmXE95eJz0ZKu_DCkZ2w09W8DI7si_I80FANAQgfkUa5vRdaM8S9Hg4IRXbNcsQo85bwAcKgIfaweQPaLr8-CrMcE6ed73sAnkxY3lazFWP_MjesO02WU4tXCdOJYyc-e0FKIvmern4QzZQy_ZUFQgjtDTQuhh2e9TMLylA19X-4a8mPRcboKjeKfmI_X68tnp3hGLth3SfShoXBID6zncUlDrx4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو: پاریسن ژرمن تلاش میکنه بین رودری و رئال مادرید مشکل به وجود بیاره
‼️
🔺
🔻
پاریس از هایجک شدن دیومانده بسیار عصبانیه برا همین با رودری تماس گرفته تا اوضاع رو برای رئال مادرید سخت تر کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102045" target="_blank">📅 09:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102043">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eRsfEI6O9yr7Y_IGOXQ_Va0UZGLd_3QWt_aims24GuYVqHLiARnMLRmXeNE2gzdSl3qxqgjUSYrBnUDtch2GdAV8BwhkFhmRfGmhb7yqDHHUgD9_UHfMb4lb2JMqgzItUSs_eDI5Li_OiJKw_iUb-85_gpcTEdbGZ_czKaQ-HzYvXcrpOamov-aP4QfEVSTQz1auGZdrL_v3FqzcQkrtF1MjxL4NcO7ELMrKPCopADa2J7y-nKd_Xfz_LsN3UL44ks5m2eunrC4Y6UJ-hYJlYPKv-k06pv79knxnZ5neDmyJFcNoQXkdVLl1vuD3yJ2mYu8UmiEthNSsKJXgED9vhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d3eF6WFMF5xi0w_zhtXcUp5TZLps2j76hX_Ab8Mw-HI5llfFe3WE7qr5Nck6OSQ3ltqlcsQk2_qwsDpSsRpq7RUI3pyi_sas24BoW2zFVBEEuTOXxLJBtt0Tf2oYKhg4rBIUJnRGKcwjvis2bgmWWd-TWnAgxP1Tkxnt6HoJ4OaN5zmWK1epZNyA65GO0TMcwII2vS00aizyvEd892nOwTtHb7Qn59pq3dmxx-tRhDQJ3BfQTvl-vJRB1kHLZ_b6k3XfYXN4q308JSKa8-5OfknDoRHavrxJqRfTCeC4jhEyOeXJxNmbjGOk1rnVIC7IDoyTr90CCUYv7qGxOuzLKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
طبق گزارش رسانه‌های برزیلی؛ نیمار بدون اجازه، کمپ تمرینی سانتوس را ترک کرد و بعد از برگشت هم در تمرینات تیم شرکت نکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102043" target="_blank">📅 09:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102042">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTt9dokoU-A02FqQrxqvVgDT9QXIggcdmC4zGnXQ9v6BvTjbG9AD4ZokiPz7MFHsKtczKYDHnb0fGv7SXXHX-9nTXtQRMw914RBbwv4yGXBKBprxY9-t1qoq10S7-G01BI5zmVmtXk0q2E3aW9vAzPF0tyeJHcKTW-3p_QJkCL8DhUU_fhr-D1vF6eyKLfOviSmp6wUgoaGeKbTLY1M1J-nfBSXRH6mrQ4-FQBNmpsz3S0Wj5Wm-rz2JQ1oihU0gPzFh4mEtumQpqcS_B9ATRFD1Y7US3VKIhY1Iyj0Cw8hBWcdKnZ7RGaRPR4r5CpirXT0nSRCgSJKQZXfo3npz1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیکولا شیرا:
رئال مادرید آماده ارائه اولین پیشنهاد به منچسترسیتی برای جذب رودری است.  ارزش اولیه پیشنهاد بین ۵۰ تا ۶۰ میلیون یورو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102042" target="_blank">📅 09:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102041">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uw_kpRbBKVGlHZ43A167w5nNuZuPJ3liCnIKFIEAp9_CEB4X8_aNP8AKJY0ztQX4fZ0Dn0yqAPsqmW-J7JV2n54EPdCSt_gvnP_J74CDQ7tnxC0r9Jxm4vASD7lPg0VoN9M_vA4QXJ-Kp2nN7NGQPapaDlxHQWVB9evnzTIBA7D61jypuhpGFGehhvAjXZVkei05QSZ2wlAUJ_59zJ6POub0g3K9adeQbz36OtNZPmhbd8BgKYd5eGkPivXEyWAlIZaWn7X0E9APEXeVz_Q61vNcdllBZGeWIPLHVkVcvTLfNe6czXoTedF3vMECgSyIdcViCRh7PiuaSGy7xIz2Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
اوه‌اوه یکی جلو فلوریان پلتنبرگ رو بگیره که ریده به سر تا پای رومانو:  حالا که ما را "دروغگو" نامیدید، شما خط قرمز را رد کردید. شما فقط یک روز پس از آن، انتقال رسمی لوزانو به آینتراخت فرانکفورت را اعلام کردید، و با این فرض که هواداران شما احمق هستند،…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102041" target="_blank">📅 04:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102040">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSAFQWso-oJMXq8oMVg9FNn7KaGfJEtgcOxMPgPCz7JBFwmyrJsR62vFVawaaBdbF8Ntsws_1X85zWh7N8agHySWtnHaQhs74Yi-NSSDyBax8fEMCsIkPRNseb-a1I5fT3Bgvk_Gzo0-wuQoCNj5ySVZESxAhwTpTgeRt-rGD77CmwLV1aN5PBCpD0mElEF4rl2q04JQYV4VQgLPZpSSZLWLmOQx6PzFqmD5w3bbjWD4BX0dpjtZc0hJ1zibxL9ZULpfP8EygouIfBPH1rp91h-jkdRtcGq6ZA7ve2zGPE8SDRk5ZKuAqw9knLvHfwqJONN1h8arvcFc6QKx1-GPLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇮🇹
#فوووووری؛ حضور پیرلو به عنوان سرمربی تیم‌ملی ایتالیا بدلیل فعالیت‌های شرط‌بندی وی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102040" target="_blank">📅 02:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102039">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qu08iTHJZz1El56D8k09wyRltM_fjKi1AdDMhAQULcfwq_ycYcdL9pSrERwG-Hl5BmOXayD1i1Pcc9HOfB3XtyZvzTcJFjEP_rKAXPlQzhcNsq4FNKGzK1Vl80d3aRTx7Gh5wdeoGsv7HbEX2xmsBfpckHm0w5KHlWUlpaTEfNAXwWlPTVQIAsZcFPFe7WDfOU8_8EcuJlUTKiutT2mIs0Vimzj9o-vstVJURIB1V7pJJWjLwEYz3l_il-zzW4OPlkPsQ-C5jkHhDkoSL8MpQe6V_AWBlpH36v_gTWM6vmVPi2KBZEvjJojpqhWj_83Fj3qNKVdu4md1Ovx5R1snsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇮🇹
#فوووووری
؛ حضور پیرلو به عنوان سرمربی تیم‌ملی ایتالیا بدلیل فعالیت‌های شرط‌بندی وی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/102039" target="_blank">📅 02:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102038">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWrrbqIYE468t1YJSj3UJjIkHjAGt6cc4J-wcAZqLBCpI6FiTXHn0-nh2_PTRlCpvzAUNSi_B5bBYR85zXKeK-EctyWcrcevL5g_5UV5bm-Ki1F8Vx1cCuM-EKUEo4hjdvsB_MgTrpwNevQ6AQ9B1uJN-i-d1MOw_evAHPNwtPJu4JPHDQf6ypVN1h3CHCCo56syXvBXH8fkaFlBv541rTp-F_yzfFnql9z72--mS2deWDrw9VVv8FtJz2B0mFMqIJi3fo1XhSccQWqoHy3Zsv4dIpsYHVM5Cw5RkWhzcuGCeDiRU0Qa7Ukl4WWIdmq1NkbJWfI3o6xOsqbcyhjXEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ماستانتاتو بازیکن آرژانتینی رئال‌مادرید قراره به صورت قرضی راهی بنفیکا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102038" target="_blank">📅 02:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102037">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQlqmGfuHZHZ8LIzW_Uw4en1ZUm42PU2MLV358vrvIO_3fS_C90LZw22pTJTgqy4Kls5afpyZe9xfxvuCz2QTVgU4MVBLhNeU_3xSTgwtGXexcTI9PxHP5iiQqHPGyJDHHfYh1gckydT_SKQ5tnpc4tFHgxoqU6pTy2AtcpDfAijX2-UDezubaudHNO5mi4omRBOIWxPz2Uybq1b21vVpAtPm24HZGXWH31AUT1IRyC8wSTJrmmqD8284T9VAyl74JL_EszQNxM1OiWo4yYjyNtJm5_zKReKc52FUjxLB084xrfEy_Kj9Whphz-RMM-yd96EFUBRY3uFxhDHVLOl7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
جنگ بین خبرنگاران مطرح فوتبال اروپا بالا گرفته به طوری که دیوید اورنشتین گفته پیشنهاد رئال‌مادرید هنوز مورد موافقت لایپزیگ قرار نگرفته و نیاز به زمان داره و به نوعی گفته رومانو فعلا زر مفت زده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/102037" target="_blank">📅 01:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102036">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Alb4TVjmNjrpg-KGfs-XuYlQFrMPxRESbVu-4tdCBXUBDahSPItBuD8VFXGVVcTLy60P8VOr0E_T5tx2_04bDNlc8DD4hooC4FVAkXwYZADCQPZxIdXLVCAacPVE02GYIiG8QQMryKDbGAnby19osRE_s_iINRZ_FsX5dUGPpWqZ2061ssfxkIchkoZZC_NddV8UW29QNcfNzFTifiZpF8q6snC1d2VKZq0np-qYAa_kYlljkS05jq71_7CcN0Pvj39s5hPIHg6B5oRopJKqGocVZM9d_r5w4ou_QZMCSH2QU15ZDJNNoiocSxXSqw-9DS_jeH3n1tmasRcB7Hiq2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرخیو والنتین خبرنگار فوتبال اروپا: ژوزه مورینیو به کاماوینگا گفته که فرصت بازی زیادی در فصل‌آینده نداره و بهتره به فکر تیم دیگه‌ای باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102036" target="_blank">📅 01:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102035">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Huz5GJJLSV8Ax8Hzqo-0NWAEdYPo3x0A0ecxDZUVqMDLqQyhhkQ1vtOHFukXkikf1CkeHmD2eaMQKJzyoenjrduOMFePFwQW97ccrpAWtHVRjZuD9jxRHq2lhDndvPxh6YiCmaaDs3pA38Hq95kT4iMVZoVrd1f16cODH6s5IdDjUZGEqo53n4Dy_had-8Q1fKRGaa8DnpuLzJLjUrCVW4X4fbfcjoA_Uo6uw6_bc4updS9bYVw-7a8vyDcAgUMAnThIZqsHPQKAuzpXusvuHCbNosavJ37tEC1EHUADrqh7w0U20Sbfg4f94sBUQ9YphLRlwiYnQMKgVveG5SpT5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/102035" target="_blank">📅 01:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102034">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fa8UvnkUF_f01vHrldLAh4E4VdD3JzARKGXGz3RFKzsPpcM1eX2eUfoKVH8VljRLfWZ4tSQbj1YIJiEH4F__W9PC-gKkJz7qWc7rPP2EFV-iZyk9ihqLHvI8AsJtS5GUKpDCg8yMRHxgAwPHtyoJcn8O-WtdbzdMpLA9_TK4MTkQMX7kcne9Xma0iL8cetXtNFyiXqHbjX5y1y5oDfqSXn3J0rVcVw17afAQetE2rlK3W_Dbh1eJARXGuuV3QtS_nXCTHFuripIW-qmwDz5dKcO0b8zoELd09PlpYZnAZo23J1Hm7FH9UjvUwcySP-fBDdNf7OUlR9d5AACi6ekJ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
تلگراف:
مدیرای آرسنال معتقدن وینیسیوس جونیور همون بازیکنیه که میتونن باهاش چمپیونزلیگ بگیرن و هرچی واسش خرج کنن ارزش داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/102034" target="_blank">📅 00:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102033">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=EtXiPOLft1nrldRd2vwmqejQ7dGMuSUShujyNG1y2cOH6sQFxtht0Q8OAnnruVwTAUDk9GhdmH87iSgo1aZNzAqgqIxadZ5-_9yt4b6vdqywh2LdO4k8Snhgmc7lycWYoODZGGCbSmPzM74nY6iv4VSgGtbqd3Eyj_trNh87xjZpApkiiqTEJpftT1g-djtUJKyLje2ta2RnXHkoAq7NBRvasAc3FyUaw2C23AEqP2WcPBa0y6OWZQ3PxezKiv5nlNl5vLx7x8gz-F3DQzFQuk5yvEUhUJayZmlCk2HwmjE8GJ0yhn27znOJcffl9me_-QljtJ0E88sj3JR8_XHFRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=EtXiPOLft1nrldRd2vwmqejQ7dGMuSUShujyNG1y2cOH6sQFxtht0Q8OAnnruVwTAUDk9GhdmH87iSgo1aZNzAqgqIxadZ5-_9yt4b6vdqywh2LdO4k8Snhgmc7lycWYoODZGGCbSmPzM74nY6iv4VSgGtbqd3Eyj_trNh87xjZpApkiiqTEJpftT1g-djtUJKyLje2ta2RnXHkoAq7NBRvasAc3FyUaw2C23AEqP2WcPBa0y6OWZQ3PxezKiv5nlNl5vLx7x8gz-F3DQzFQuk5yvEUhUJayZmlCk2HwmjE8GJ0yhn27znOJcffl9me_-QljtJ0E88sj3JR8_XHFRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
وضعیت این‌روزهای لیونل‌مسی در تعطیلات:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102033" target="_blank">📅 23:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102032">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsxSCbDGDoskxmMlPAA0qbm6GCmsP9l9pbPe6AskIGOgNdB0ZQZzFZ2ZlcKeg9sxg95QeDZC49RKcoUDKF26FqsWfEwT8j35-4VrZuxBt5Xdg2sYvFxQcKOpMu_8V8XgR9ka9Cxiuh4PLCT0vTLhbq-MzQ3p_cDSrUJ21K-ZrCgF6zfGQRZuPmViOm48flAN7FLFfdy3v7ZuPolt8KVFa_ljlyC0bN3q-o9KKAgBl_90kzNB0mW315qI1SIT-rl01CT89qKmJddERHwUxoo3Z3TjeLI5FDXMfq3_XAI0Z-nL0gfuVpOHgrUCb90kulTSmK7Sj9dX98wBtt3cZqiWkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📮
🇮🇹
دیس فلوریان پلتنبرگ به رومانو: بعضیا همیشه میخوان اول باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102032" target="_blank">📅 23:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102031">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pg6834j19-onTZyksz_TLGfUfB3KwP4Qe1TahPuOJcGEH2PmNQGgw4IivhCxLodImPkpzXS9US0CueVpsQpemcT9ig4iN0onPdURtxbxWz6nyKDKLGD2vA10xp4qdY23A2WtqrGE1G1Ly2wSWkAKpDeb_PnOdqrl8G9MtvHc9Kqo_09m26C1rU6H_vaMJ069Rp9L6uFbjlOtQ8zvsvu5f-AeBMeva4tLFM8715B6NEOyL7QTTaEeckNt5QST0o7jr8k2GEL7gfYjfw7FoCmar2PIqLhUAk0XjVNaXewBB-gR1vwVOMbF7xsVW72qbANiCsCCA4ZOLdA-fOhztU5CwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
فلوریان پلتنبرگ اصرار داره که هنوز هیچ توافقی (حتی توافقی اولیه) بین لایپزیگ و رئال مادرید حاصل نشده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102031" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102030">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102030" target="_blank">📅 23:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102029">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=dEMdWHUTzPVrAitDx5eMqMu_DsZFbn6YzvlwSg6PYBD2yQj7gyCFziTQOlkSYThPn51NCnIx_FxmPDUsGk1BLQ3EgALDUqGntTE6sWu14xkYhwlUqpAL8aev6NXGSjXFY7d3lylypGSROgqGTaodfvz8v3f_h6tlc6GVgAGLJvM5TIsQBIhT5rn5xuKJ9qn2dXJbXidqY1iH8YQI4eQcA-ru2gJQSG0-TBMV9R_4arOaIygGqmF3RRcbospymVavh8KdlOaUad2OjG-uH5AkPa7VsoFpMurj9r6cxTu8MZCt0iKneoEzfNPOKx-UESPeCFuNocxicIcsZJVnGPoKMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=dEMdWHUTzPVrAitDx5eMqMu_DsZFbn6YzvlwSg6PYBD2yQj7gyCFziTQOlkSYThPn51NCnIx_FxmPDUsGk1BLQ3EgALDUqGntTE6sWu14xkYhwlUqpAL8aev6NXGSjXFY7d3lylypGSROgqGTaodfvz8v3f_h6tlc6GVgAGLJvM5TIsQBIhT5rn5xuKJ9qn2dXJbXidqY1iH8YQI4eQcA-ru2gJQSG0-TBMV9R_4arOaIygGqmF3RRcbospymVavh8KdlOaUad2OjG-uH5AkPa7VsoFpMurj9r6cxTu8MZCt0iKneoEzfNPOKx-UESPeCFuNocxicIcsZJVnGPoKMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره فوتبال مملکت علی‌آقا دایی
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102029" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102028">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-Jf-JDFYT5hmzFjQoKs4JmLlmoPVu4ar7P8xJCR4KckGrpHNOWgX_G_SzdWzabmwMBGHLBDFvjmlTf_9rLStKBzL86wLdDH9bH3bbIAcH2O9lNMO3iZ9JGYoPTvSfxEeKMynx6rjPkOYpnhhb-K9i9hf8ykdwLEZorzGLvgbWz3yewPdGjfYlI5jLxixaKNZKRYD4X72Ru2fKNgYvtreJTAzaQTIruILOXCnhoWR39XllTCLE7FJx745MlvsbK_agBM0eQPeFCaV8NstUc4viHOirwnlVvuFQ2-d5CoAl5B6nXip13iCf7qHRL-NHjY-fSY3N3bP5eVXkTPXrM5Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
👀
رومانو:
🔺
خرید دیومانده بیش از 100 میلیون یورو برای رئال مادرید آب خورد.
🔺
مدت قراردادش هم تا سال 2031 هست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102028" target="_blank">📅 22:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102027">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7akM1nsPOQPdQq40UThZrzimtRHiV5G2c2jjLfuaMUYR68CktDIGCI7bSdYWCBydryz-PhCemq2c04aXuumGL5xY6otk_0Her-HiaE7nicGREDEHUKmgxsjcR3LqMJoSQi1wPxRA9HcgC2jvlJgJc_DFtSyoJFyg4i8BnZXggH-JZGne0VvmLtwgfflSlRS0JQ7I996kdeV9XHbz-SdA73GkxxCxNB7LdzAtH0X8_57Op5wrUnJYNaxDJtMEnmKxYdO4Nu6kMlVP_rk9FMvM8gTmnvMgXwosEaCYjyr8b1jlgiWEx72EXFNXGiQT6pajE1-ICqPzEW3uWsNhaxFPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار پرز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102027" target="_blank">📅 22:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102026">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102026" target="_blank">📅 22:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102025">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3FoT2IcQaQfdDpg0riZpW-BtKr8o4ToHw14lClyoKbswHRD1ciyDrmfdJJoEIgeu4W_m80aQ8q8vYJMS45t6fG9NsjnvYlRvs7z30bFR4ukIt7HvZusRh0pg3lMFfvGGVX-_gTx9fDZJNBd36b068uevnBOUk3utMor-xNIpI__sTxDoiqpr4ZfQgIPnsvP1qjRQRU3m_e5NS_aWAylNeEvtH0ugmmx5tdParQa16x2fF1nG5z1JKt2NkBQ7_sa6B4XyB_uvs09PoVzKX3c8feP25iByIk1UtpoEtBcB0b3Fuq0VdNBWTnUNmNVUdEeIanYYnAZx8V18f_g1xiSwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
اسپورت: خولیان الوارز گفته میخواد یه قدم دیگه برای پیوستن به بارسا برداره و بزودی انجامش میده . نهایت تا ۱۰ روز اینده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102025" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102024">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsoxNlju29xs5yhDxU3V7X_k0Ye9pVSVP2Bg0MxQ1eBmRD9TOq_cfFskYMQ7sZ6rQwqvzxd7tsng57mpYfIbytTe_6krCyIs2aPqkJCTi62PI4MLZzE5623Y7DWAN-nI0yv-85uUxdfo3TX3Dthu3TBLZheaB4ZHY49cqrcCm4h-_vq9YC_DINDLTEHjUaKScLA9ZrNUCdiQimr80Oxmq7iOlVx63oo4I-SbzW_29NYs4mwgeiM6Lzm-QSmRVi586Tu8UZ8kC2Pj-cMjNRy7sscp3qvcS9NRkY6HT7qu34VD5ik51OsA1FrubFTPMZ25D9dqpLjrIZdlamPo3367ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی
از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست.
𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102024" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102023">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9274ecf947.mp4?token=BbDyRDe2uaPqO9h_XTou3bFQrZ4JUgHDPZdBDaTVkPAxalp9waXzT0xoB3CacwpV2XNSQZ9UJqS_azxz7pVDSw7z6R7PjF8EzwuJ7nFK2dUVvsaHbw0SJ7fUA62T08kmED4XHITlmySChw9bx4dVGtWbW_rn6i_jXeq0K91NQhAf6giXZrj9OJ5v-EOqJY4MSyvuqWoWYWcYm3lnE5I3S1I8hLTMqX1Z413MZhqfmSvDpLYWcsr8TBKFMHr6A3fGsWEHppFmFUnMl0FHsjjg0yDCMPyKnr--Mt8aEVVaUBRl44kdYUmoBF-tJtOlUMlQ1wtcw__jh1vk_LgnKWoWYylSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9274ecf947.mp4?token=BbDyRDe2uaPqO9h_XTou3bFQrZ4JUgHDPZdBDaTVkPAxalp9waXzT0xoB3CacwpV2XNSQZ9UJqS_azxz7pVDSw7z6R7PjF8EzwuJ7nFK2dUVvsaHbw0SJ7fUA62T08kmED4XHITlmySChw9bx4dVGtWbW_rn6i_jXeq0K91NQhAf6giXZrj9OJ5v-EOqJY4MSyvuqWoWYWcYm3lnE5I3S1I8hLTMqX1Z413MZhqfmSvDpLYWcsr8TBKFMHr6A3fGsWEHppFmFUnMl0FHsjjg0yDCMPyKnr--Mt8aEVVaUBRl44kdYUmoBF-tJtOlUMlQ1wtcw__jh1vk_LgnKWoWYylSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
آنخل دی‌ماریا: مسی نشون داد که یکی از بهترین‌های تاریخه و تا وقتی که خودش بخواد میتونه همچنان ادامه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102022">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNtM0RqHP3dW_GfaYJ2r_0Prw2B80aAR16G66xL-glT3ZVN6DOV1L1SoT196vFCGGkUP1-Grof_1kDSQEyOYnCZEjqV_wKEehM8zyWyr514u3FTMgvDMDPuAQOsYID7LPkWwQkVnuwaR5mqUgLvhXRO81t6UzZy8uy95pNP5epkp1iDS-BocQhxcSnwxoUoLfS79HmOZR5YZfj4fp8SpXLCb0LgoaueXBwuO6KeRJrJDkXI9bTrQh7ZMheR-sB1o28BISzKItJkt3g6JcTK7LIxe09uRtRH4rIGdGSoUb8wjQYn136OcCquwd_GAl-rXwAsqbZduuRzgo2uWMAYqeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⚪️
عمق اسکواد رئال مادرید برای فصل آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102022" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102021">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=XIEWabVqC07DbUYaEQxPZC0bxF-k_CTlKac6aYNzvddNe430gVjjuoZqewmx63DwVERv5QhbI_Nj13hwo2KWPJrvOHUzZniaSWSz2OMqSNB3uODdIIla7p3SHJeUhmE-ptxWvpgQECuNnHwSzQCLrL8RlLlDhJcxhc74-2wcOnSdBudCnSyWcs9EowzjVU_wMTHt3JuIYK-Er69ciZdWOQRshAp6udMc6hZkvj6y-JbH_8ICHogSIjysDx014702h9RTBb4HdWUF77A3wzztluy09dZr0FjzrnJPnzNMAnLS_-p-kkvMN3UQ4CtJhfhdWv4bLxiASKk7159S6EoEJqnT6WqRpq2isM687MEscGWRzbs3F-mbPLxtmfeFIsuC_Os_hXiuE_kUGJo2kyvre9otmSUPj_Ibv_XWOnoAydldJBOkczTdOINYX1U9n4wMGv8hJKNrJbPdWNnvSkl8WbQs1uMw72dFtyuXSiurZZp0BMxIlj4BAjwutmyw9ntZ-mGS3_EwhqyfIjkLbQoz6NUivDq1G7tbk5-wfVEd60LntZH36ft-PTsBa9KOH8j5eXatWyC80G7FeffNT0jXqn60W0VYmKXkqa5TpvFCSreJjBQHxyJzYuevP81C7T63-EvE9tLRMJim3CZqWwCfJ7Ekksp093wvrJAc7BwRkg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=XIEWabVqC07DbUYaEQxPZC0bxF-k_CTlKac6aYNzvddNe430gVjjuoZqewmx63DwVERv5QhbI_Nj13hwo2KWPJrvOHUzZniaSWSz2OMqSNB3uODdIIla7p3SHJeUhmE-ptxWvpgQECuNnHwSzQCLrL8RlLlDhJcxhc74-2wcOnSdBudCnSyWcs9EowzjVU_wMTHt3JuIYK-Er69ciZdWOQRshAp6udMc6hZkvj6y-JbH_8ICHogSIjysDx014702h9RTBb4HdWUF77A3wzztluy09dZr0FjzrnJPnzNMAnLS_-p-kkvMN3UQ4CtJhfhdWv4bLxiASKk7159S6EoEJqnT6WqRpq2isM687MEscGWRzbs3F-mbPLxtmfeFIsuC_Os_hXiuE_kUGJo2kyvre9otmSUPj_Ibv_XWOnoAydldJBOkczTdOINYX1U9n4wMGv8hJKNrJbPdWNnvSkl8WbQs1uMw72dFtyuXSiurZZp0BMxIlj4BAjwutmyw9ntZ-mGS3_EwhqyfIjkLbQoz6NUivDq1G7tbk5-wfVEd60LntZH36ft-PTsBa9KOH8j5eXatWyC80G7FeffNT0jXqn60W0VYmKXkqa5TpvFCSreJjBQHxyJzYuevP81C7T63-EvE9tLRMJim3CZqWwCfJ7Ekksp093wvrJAc7BwRkg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
امیرحسین صادقی: وحید مرادی من و فرزاد را در هتل المپیک آشتی داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102021" target="_blank">📅 21:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102020">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yt_ROmmhbo_7jnQgP9o2S3GRJ73SPHeZCuuGx6cp1HNbVdklaOaLNoVWL_ULhW6QK_LWmk8XNjTWjM9B8X4iKBLyPJQNZlV4_tCY9sadAjYDQRwRE6Rhv81WPlHRWPmirSo0bsa758so_yS2f3ef0o-Xejdmg1ULI2tI2A61wg7Nt58DT-YHQt93pZPiyq7N0bZiB-otYLocSBkownaEeJFRnjnqGxPYrSywAhYEGONOq9bPYdrMTPT7ykIhhsrmOmhAWvwTakM4pga8hrlfmzzywxpll9ICHg5oLBqQUtxF14uwYHXLdEGTi_4rvOiwLdWlxUh4x70i4wAHHx2Rzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🚨
پژمان جمشیدی که به تجاوز متهم شده بود، در رای نهایی دادگاه از این اتهام تبرئه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102020" target="_blank">📅 20:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102019">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5zzliCY3XhrOr2MesfXcMSwTkDEmBEKk7hTR25U_BJZOilYk9IZZQfv2hQZEIPOBznr1i_IvAi7po9C_X4D9pwMmV-D6DO83LQLOjISwP7TaR9j2LDeT6xOwRckW1EKHAkhaIAv3xAYPRcHt0laCvZzZ2SADfkt6RIA1zmeZ6IVDV4VplJYY-gGnbtJ_l4RUaCLIsxhAz3NhFaKc1d0C85LdtDMYDlTWA__ZUMyUeUrfqESPjA2v-DDMuzUbpEEgmb-ddfh64-r_7Z8ax-FhQzNZe-GFg7cK2a8L5urkZej3VKNBjYoWX605c76umlnGy0NfelYf5-J_m6qEcsc6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
آرانچا رودریگز: انتظار میرود که یان دیوماندی این هفته به تمرینات رئال مادرید بپیوندد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102019" target="_blank">📅 20:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102018">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=O72gAn2RjfWYhG2M3dj7t2ecKmlz7nBypTsvLfzPmyB7-wZLda1x-_zjJksLc5otzl8FLbXLYV5vZ-1eslf6Xb7Egw-yI1aFOjg4YmZE5EBiyR2v1momHunw4ZsTMiVvcLcufZexvrnWM_hzo_KJIz-46F97INcUBn5QVeOLiMRblr_fGAD0M0OoArlDPNj2Ufd9pLAEOac2TOhOgNXZ054mI-MnjqFamXNz96ORCp78U09ONnCyWk3nCblpeDhtrNhuHizNn1r1hco1gm2LpOYIxg7ZK_WbFNDNSM4NkGI-CJkoEjj7Gchr5jyFn-cb9SOgizJcQ3Ab4CewacaHbzxP3PyEfw00dGaBnWBUvb5V3hBIKx0pDKMZuBwUwbNeKBiJNBFqQ9jUsn6yMpiYlFvsFR-2SpczG8UVyLRs_MlHCzP4ULVN9lGFp0juFhDzhI3wsymepoqA0ilkiYKKGJ0kEiw0rZWNQ7n32JVm_AE6Ay8fAx7MNqEw7ZY9_c7ZLR4qeMQvn50UUDVY63yC-4SldaXy6d-1I2F_L2v0Aot-FYmYfdQY_5PkbiSxLODsJIutqx-Z4M4Ibj2hzTeB88tM3ruzncdpttulVODbm-kVcTr0y9Srqsnq_9oqPnYc15FZRJncTmqDbzdeT71xu1I6cy13wRQNx6OglCYRu1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=O72gAn2RjfWYhG2M3dj7t2ecKmlz7nBypTsvLfzPmyB7-wZLda1x-_zjJksLc5otzl8FLbXLYV5vZ-1eslf6Xb7Egw-yI1aFOjg4YmZE5EBiyR2v1momHunw4ZsTMiVvcLcufZexvrnWM_hzo_KJIz-46F97INcUBn5QVeOLiMRblr_fGAD0M0OoArlDPNj2Ufd9pLAEOac2TOhOgNXZ054mI-MnjqFamXNz96ORCp78U09ONnCyWk3nCblpeDhtrNhuHizNn1r1hco1gm2LpOYIxg7ZK_WbFNDNSM4NkGI-CJkoEjj7Gchr5jyFn-cb9SOgizJcQ3Ab4CewacaHbzxP3PyEfw00dGaBnWBUvb5V3hBIKx0pDKMZuBwUwbNeKBiJNBFqQ9jUsn6yMpiYlFvsFR-2SpczG8UVyLRs_MlHCzP4ULVN9lGFp0juFhDzhI3wsymepoqA0ilkiYKKGJ0kEiw0rZWNQ7n32JVm_AE6Ay8fAx7MNqEw7ZY9_c7ZLR4qeMQvn50UUDVY63yC-4SldaXy6d-1I2F_L2v0Aot-FYmYfdQY_5PkbiSxLODsJIutqx-Z4M4Ibj2hzTeB88tM3ruzncdpttulVODbm-kVcTr0y9Srqsnq_9oqPnYc15FZRJncTmqDbzdeT71xu1I6cy13wRQNx6OglCYRu1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چنتا سوپرگل قیچی‌برگردون ببینیم تا روحمون ارضا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102018" target="_blank">📅 20:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102016">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1Z5RJYqU0itqrAylG3Pn7gwGkwJ13vjs4CzPCCq3W7SUJ1WH9XwDcdwAVkdWbMzrctbz0IFFLkp5aVdzrN02P4ISI3ff7B4vWs5r6shyXlRIlASuK4jGbAt0PfuIsp2VeM56MM7n9nOuOdk-JAX45HU8Kj_XLza_1NJ0y3eanc9b9PIOGI2stbRtsf76EcOYv2x_-ioikDWz44Q2S0rOOZKelCQcQtAKfaJ9EuafwKI8IIcpTlL3Idd4V_DGQ3F7dFzkqbybboxBwtM4A8RFRWxcsAdLVi2EVmbniCjrk0HFKB1Q3cBDFBKG6tHUHIZFIX_BqxyT4QRMzdSNEtghw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VCT9zj2eo7fvKACWgr1Xi6kCzJZFm1H5cOtOBOZ4cgxsn2jMhYO7Ckf009Q0ccStHnla49EpQzMODLI4pdE8rtqw0Bi9JN6V_8nx1fstKwO22b9EhWxpd8Q5NB9VeLRtTe4KhYbhhwihGCUAg2sGo5cW8np1c_c-XTas-z6VbUdmB8LeCOoWdTzMxqkxXzN4eTG1DqiWNVU0_DJsb69iUjx11Nxc04u2KJD_fO3pInNb9F9hH75f3tICaM2UnmDkNtiAscr3Oo4kZmttGHCpF5Xem5JUt5gNt4QvYoyB8TYpg14zaJZ7_yOKHxvFzwrVgMah7bRqFRM2H9SsLQG2Sw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
لواندوفسکی:
شاید مجبور باشیم ۱۰۰ یا ۲۰۰ سال دیگه صبر کنیم و منتظر بمونیم تا دوباره بازیکنی مثل مسی ببینیم.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102016" target="_blank">📅 19:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102015">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9CRI4FJM2qZrFbvcK-fVOetUkwrfhGFJHMXWD2CZMJSZZflwfxj9eaBbWhVPfoaWbfpEAYUCrRpRSqxrU_QpuGK97DofnNZvz5mE9pgHgfwtc9qab0iTPq6sUV-4gwmpue8Par9RqS9pmiFragNJC4J4iPwGyPDp3-CYltsIDNCOk3esFIIE1JcG2c5Hctxv-4WwgpaB2x5UAMiFjHEBaDf_0s-pOQaBqKK3awPyvDOZXX3uPQ24LOYrq1UMluNjD3bGWZbtaQ6QBiW-YeJg05W3bV8JcDn71FRV5-ad5OqUWDnNuFonEN2IaBlYoA-vQNyxFIH6ud_Yi1KqTmyrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
گران‌ترین انتقال‌های تاریخ فوتبال با در نظر گرفتن تورم:
🥇
رونالدو: ۸۰ میلیون پوند → ۲۹۲ میلیون پوند
🥈
ادن هازارد: ۱۵۰ میلیون پوند → ۲۴۵ میلیون پوند
🥉
آلن شیرر: ۱۵ میلیون پوند → ۲۳۸ میلیون پوند
نیکولا آنلکا: ۲۳.۵ میلیون پوند → ۲۲۶ میلیون پوند
فیلیپه کوتینیو: ۱۴۲ میلیون پوند → ۲۱۷ میلیون پوند
پل گاسکوئین: ۵.۵ میلیون پوند → ۱۹۷ میلیون پوند
مارک اوورمارس: ۲۵ میلیون پوند → ۱۹۶ میلیون پوند
گرت بیل: ۸۶ میلیون پوند → ۱۹۲ میلیون پوند
استن کولیمور: ۸.۵ میلیون پوند → ۱۷۹ میلیون پوند
ریو فردیناند: ۳۰ میلیون پوند → ۱۷۵ میلیون پوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102015" target="_blank">📅 19:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102014">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=YbE19qF2guyuy30AKGJTIRuJwdE7V13qWJ4sVtO79m9iBIQYP-n4FTp64MTDbfASXcDzbFp4v8R8iANckixgHKhyJYhr9BXs-VsUfcYkOvn56ohtddtFbJrEl4c0mNVIXnMz5wMjw82IWf1eAl0u3vvxEgyFPf_gnNHmfTdpwNa0JbEFzqYQod6RtzWu5Q418dRTrkITNPLPu_IdF5Ct_fPtc0cr_4gowaiU7ZifSHShkobMEiAq9celxQhceQwix9wCWFa_CpzdKxH4sKggI26QfsvQ6wfCrHncqIsvEcOeeGUg_SWio-921OBADSOb51dngvJUV3KY_A2bXr-8VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=YbE19qF2guyuy30AKGJTIRuJwdE7V13qWJ4sVtO79m9iBIQYP-n4FTp64MTDbfASXcDzbFp4v8R8iANckixgHKhyJYhr9BXs-VsUfcYkOvn56ohtddtFbJrEl4c0mNVIXnMz5wMjw82IWf1eAl0u3vvxEgyFPf_gnNHmfTdpwNa0JbEFzqYQod6RtzWu5Q418dRTrkITNPLPu_IdF5Ct_fPtc0cr_4gowaiU7ZifSHShkobMEiAq9celxQhceQwix9wCWFa_CpzdKxH4sKggI26QfsvQ6wfCrHncqIsvEcOeeGUg_SWio-921OBADSOb51dngvJUV3KY_A2bXr-8VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الگوت کیه؟
دیومانده: رونالدو
رونالدو یا مسی؟ مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102014" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102013">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=cwlLXjAkdYKSiYK6srFXgqSfGzvj6pWm7gSuze9YfioOwpn-gKKwZ7Dx_9_rBR_QIc4rnnBytkWxf4zn8fMTTP7LKZhjqFnFCj2VyzTM7fr6KFS0k1E16nL1ibalYHIUSYFzMsLT3mm6BKIQky2NZ0R5PAuzq1IWqFj1NQIpg-1plhkLU_SZL3WIdxqwcgsvyhbiC_zfweEQj8fKM3Bb0kp6NJPtbkGsxcpVVLETg-joXA06N-7odxG-bIsLKRz-MC_-1glj7nl1-hIQjVXrhRAsdUWmyf2iI2vtuZ4l5T7xeSdhkx8A29ERHOMs84P0eo-07nvs8DtIjtIek8ctsgNPyst0g9xY9F3V3dNcSI3CX5UeG-WEvvOv1kdl_NY2aQr27iDGWSlAB9Z1VXeZFBYvSKIxRzkJ5gq7N1vbwMNzY2Nv1f6udgRFWXDIvPxWdaue7UI310zPtutDUCVgnQXzQOQTppSGOWqQJpsMU2yl3yp22uBVu1Ow71T0SI4obsZcC4NTvxvNAVk3I4KY_PR4YRs6dZ8FqiKXAqYB8Ueg6GPHQIQ7C4mqfBAKmqWslkyZUntwAKdK0mLLpxireOZ5fpyTHQmhkoHRCu6jtI8Mxm07oJZ-aw0kQActw4qQ2DpDNgbCQ3yx6moA0FE2St7NxbUvIKOw9mPeJI74Zrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=cwlLXjAkdYKSiYK6srFXgqSfGzvj6pWm7gSuze9YfioOwpn-gKKwZ7Dx_9_rBR_QIc4rnnBytkWxf4zn8fMTTP7LKZhjqFnFCj2VyzTM7fr6KFS0k1E16nL1ibalYHIUSYFzMsLT3mm6BKIQky2NZ0R5PAuzq1IWqFj1NQIpg-1plhkLU_SZL3WIdxqwcgsvyhbiC_zfweEQj8fKM3Bb0kp6NJPtbkGsxcpVVLETg-joXA06N-7odxG-bIsLKRz-MC_-1glj7nl1-hIQjVXrhRAsdUWmyf2iI2vtuZ4l5T7xeSdhkx8A29ERHOMs84P0eo-07nvs8DtIjtIek8ctsgNPyst0g9xY9F3V3dNcSI3CX5UeG-WEvvOv1kdl_NY2aQr27iDGWSlAB9Z1VXeZFBYvSKIxRzkJ5gq7N1vbwMNzY2Nv1f6udgRFWXDIvPxWdaue7UI310zPtutDUCVgnQXzQOQTppSGOWqQJpsMU2yl3yp22uBVu1Ow71T0SI4obsZcC4NTvxvNAVk3I4KY_PR4YRs6dZ8FqiKXAqYB8Ueg6GPHQIQ7C4mqfBAKmqWslkyZUntwAKdK0mLLpxireOZ5fpyTHQmhkoHRCu6jtI8Mxm07oJZ-aw0kQActw4qQ2DpDNgbCQ3yx6moA0FE2St7NxbUvIKOw9mPeJI74Zrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اگر قصد دارید سفر اربعین را با اتوبوس راهی مرز شوید، پیدا کردن بلیت را به سپاس بسپارید
🔹
سامانه پایش آنلاین سفر (سپاس) با اتصال به همه درگاه‌های رسمی فروش اینترنتی بلیت اتوبوس امکان مشاهده و مقایسه ظرفیت‌ها را در یک سامانه فراهم کرده است تا سریع‌تر و آسان‌تر بلیت مناسب سفر خود را پیدا کنید.
🔹
از ۲۷ تیر پیش‌فروش بلیت سفرهای اربعین آغاز شده است. برای برنامه‌ریزی آسان‌تر سفر به سامانه سپاس مراجعه کنید:
🔗
sepas.rmto.ir
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102013" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102012">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102012" target="_blank">📅 19:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102011">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaR_FlWhowmLHDJ85Avkckrm8klindGULpqGo9_MGnrLnIg5kT-IQCmVUWKXKjv41Ji_Agi7ENNdzKbFwiu2o1OZlH9TKm07EONNd1LCS2uwJZYPAsZuGcqTQbMN9KYFVomkIVnZmuWU4cGjW44ni9zx1i-FBFyjPQ2avVOTpPXTogV60R5osbcTrNyzwF1r_eozJMEIamwrub9gptoEMHZRhQL0sMuQdwLZ0n0pxUdNPz3zvWizCfnvV63hfl0zaZS6XzJPHTZoLY3eb04yuwqwN9t6FXHMN4946uc5f6pnZrYbt-YQjnBeBAWtrSjCx3y-40UbN1JKimc8-CJzxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102011" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102010">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/746abba13b.mp4?token=tuXTS2HqiKMKKB3SW0Lxu0NvCED-s6H9VcuRfKXsQB8yT1jlJrFRXCXrYLZE1Qd8HzXGfa9rXwYIaWxD7SEa9Amp0ybXscsjxFINcHASTf4wceS9WXivOCK7qxOu4OxdO5LwUugy67vdy6fyH2eQgwBrPCFqZYSsxhmlqeSWlt5UnVCXS_fcuxj3kX26Ag7pt9G-IcaMkootOvRZioAWdHIHDCYI7eaXfpeXtzVGunv4LbBCfJCin9K8SMM7hs5YgaIfG5lONIAso_jyv-sc7pmIS9uFCtXVRuA6DFkr1HO5BiQoBQiAO9VM2G63ilgj2AjER11kXDEZ0-vuQfm21LhWCKToqEqnHXnvhuxk8d2Yvn6jSvni5FkMFdtv4kN0qrEtulgR5BTRi1AUf-ln92fkORZrRrAjMGFfQdEtPh9RsksSSiV8wcgRs3MmD5FkxP2v_HjoqjH66c8xlgvITi5xsqX9Txg1GRx-XOA5Gi4csuZXBZhfgwBegeXTop1SQXeO5dbFAn2I5NMF6G0PvB4AsdcM6-aGSDl7SJ-h4ASmgxwRqpRgS42aKtUyRJXuleLBgpU4I5LFWJ6RcQx709GXmBbMaxr88_xQIuFxsMDsoWLPRt8Tz4Pyru3XlC3I4iRtS6Q4mVs2Ys5JBZ4bXynQcp5YsgHFhiQWFVMGB-k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/746abba13b.mp4?token=tuXTS2HqiKMKKB3SW0Lxu0NvCED-s6H9VcuRfKXsQB8yT1jlJrFRXCXrYLZE1Qd8HzXGfa9rXwYIaWxD7SEa9Amp0ybXscsjxFINcHASTf4wceS9WXivOCK7qxOu4OxdO5LwUugy67vdy6fyH2eQgwBrPCFqZYSsxhmlqeSWlt5UnVCXS_fcuxj3kX26Ag7pt9G-IcaMkootOvRZioAWdHIHDCYI7eaXfpeXtzVGunv4LbBCfJCin9K8SMM7hs5YgaIfG5lONIAso_jyv-sc7pmIS9uFCtXVRuA6DFkr1HO5BiQoBQiAO9VM2G63ilgj2AjER11kXDEZ0-vuQfm21LhWCKToqEqnHXnvhuxk8d2Yvn6jSvni5FkMFdtv4kN0qrEtulgR5BTRi1AUf-ln92fkORZrRrAjMGFfQdEtPh9RsksSSiV8wcgRs3MmD5FkxP2v_HjoqjH66c8xlgvITi5xsqX9Txg1GRx-XOA5Gi4csuZXBZhfgwBegeXTop1SQXeO5dbFAn2I5NMF6G0PvB4AsdcM6-aGSDl7SJ-h4ASmgxwRqpRgS42aKtUyRJXuleLBgpU4I5LFWJ6RcQx709GXmBbMaxr88_xQIuFxsMDsoWLPRt8Tz4Pyru3XlC3I4iRtS6Q4mVs2Ys5JBZ4bXynQcp5YsgHFhiQWFVMGB-k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی فوتبال تبدیل به یک فیلم و اثر هنری میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102010" target="_blank">📅 19:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102009">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VB8ZrIL6xwx_sPkLNbD2SgRbEkBHAJ8pyfAL8qcMnhmi4aTfOT2RL5L-xsf51jtULZL6TP0C61wbfH4gvm8btoCbk9xnOgw9CfG4yYCz-FXaIiJZ6EntIrRfU3vHchNtMJ0Wgx3Ybs4DmL2g0CkAVwzEId6nQPPQgxQV0CwePBafhwgMNARa0IPmBM9BmzYK7cv6Lx7fJvdNdr3NjiF9BDY8WvFrWK_MJfdfLynZGr05mIQsmYDvy1-nUmGBmDNukh1MgARvP1CaSVjNlzP_mbiEEZJ9zmAafT-AdxDq0ZFMO63b26KXu6nQXJaNqLRmGJOUb0RkDQNbUVCXdkcTxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
اشرف بن عیاد:
کار تمامه، مدیرای بارسا متوجه شدن که موضع اتلتیکو برای فروش آلوارز تغییر نمیکنه و نمیفروشنش، حالا بارسا منتظر واکنش آلوارزه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102009" target="_blank">📅 18:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102007">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vEFZb5cdZ9LcW0VJ46lseWy7T5rFL6N4aPIS9v9z8eyzgY0L06i-sALmrUOqNL8ScOcnvRd8rkFV83VSZw_FURNMGFIIMf0vPpEtfkb38MIv7dG1i1ibpYb47FT5pBS93SUd7RSEAxl8vJjAC1SwNVVweP6f87cCvJRb0Mr46HwfMHuNuAqoe188HCQs489rSZyMIFFPoK8-vNK5J0atv7SUUM9sQ1M-uxR4xgFiO6x30xQ44sb9EZoOUOWKIJxDiXJeq77EBmKNyRug0unY0TtEhiEVUnOD6_ovqmexc8fXt5GbrjAmV8-hUDoGYQF5mfMoL_oxhJsO0H78MHrRhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NROWnWDGMRF4n-U2FYJ70mP8hDEblKNQTvqDPTZMEsDZv5e4fO5UTGtNHLBbAmEM6Vi5h6Qtlmog1tRXw76qy7vQIcmdM2w_5vmLCI-iW-Eps2hjZE7NW-8MsdKoYSWE7_9Z6lUH3UuW66kZ9up81Q7DcF9Ll6oRnm10bZ9jwH67d5yJTqEsxH8rPEyrQMpGDYbEGNLqRb445EquuF83moN2qdj0rwWbLIoHKR6dimZldoTd7vFMuZsFTGPpgKunzqxrRrVmweWcr1veySyuBcIrueT2X2mHtcGxSsWFmgtlGW5S2AKvINO0IsCJsZLG46XheEIrlzf-EuKAeA2Y1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تاریخچه رابطه‌‌های وینیسیوس جونیور:
• 2021 —
🇧🇷
ماریا جولیا مازالی
• 2022 —
🇪🇸
اِستر اکسپوزیتو
• 2023 —
🇧🇷
لورنا ماریا
• 2024 —
🇧🇷
جولیا رودریگز
• 2025 —
🇧🇷
ویرجینیا فونسکا
• 2026 —
🇧🇷
ویرجینیا فونسکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102007" target="_blank">📅 18:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102006">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=crMGgTFmLWCCf30bsoE84zILwwD8NLiiwgOByNZikVQiTeSkBQMUN9xAdpP4r7Tld3XFd6XAJU4p3w1LGABAbTTE3ZJt_4H16d5P1INKDzH60JNBdIWekp6v28Ooe_-ci8o5xFjpQG6X4GbdQWiCLSog39A_MuyhENoekUrtmcnnShR5pW1trLnUb7A0_QKrowuJTBhf1QjvHRwczOWOOFVngaBGMLOuigb-gRpGs_tM4t_mCYky62gNYUjuT68oCEHVfvIavEx-WtugffVSVF9spXrSHUpc_Eu3c6cb7bn7ZS1Y0vmBhAppKabzsHSXT9Rdez3-vG7viqW_peFCVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=crMGgTFmLWCCf30bsoE84zILwwD8NLiiwgOByNZikVQiTeSkBQMUN9xAdpP4r7Tld3XFd6XAJU4p3w1LGABAbTTE3ZJt_4H16d5P1INKDzH60JNBdIWekp6v28Ooe_-ci8o5xFjpQG6X4GbdQWiCLSog39A_MuyhENoekUrtmcnnShR5pW1trLnUb7A0_QKrowuJTBhf1QjvHRwczOWOOFVngaBGMLOuigb-gRpGs_tM4t_mCYky62gNYUjuT68oCEHVfvIavEx-WtugffVSVF9spXrSHUpc_Eu3c6cb7bn7ZS1Y0vmBhAppKabzsHSXT9Rdez3-vG7viqW_peFCVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خشونت بی‌سابقه در لیگ‌فوتسال بانوان برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102006" target="_blank">📅 18:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102005">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdO5qb8VwBuBTXy1XyFNWwo-ouKnLFHLo40IBluQZfQO2VzXPXXdVnKYtfrwplmW7JF1XeC7rC3V1OQyI5pipX1LbHzCRnrMDemJejcvPM9GBGOp5HgosgZYhwKaBxthqZRddKcz_73Fnx_jyLMDqVSTi0b2rSriX6mjSHoGDDxZr0vqkeTg0deb_AMh2RU4Z-XCaNUgtLLade_udamTju8xB2HonwLCw-s83R-RUfeobFBr7rwPmjdWbJuGtC9L4lzuibXHkmc4bkPvlIcmB9U4Ju5LrkklHnSqd102JKdfdL8NgG6WslXk_QRhnHtN867vCdvr1Le_vM3S4wyGtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🇪🇸
رقبای احتمالی رئال‌مادرید در سید یک UCL که با دو تیم از این تیم‌های در تصویر بازی میکنه
🇮🇹
اینتر
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🇩🇪
بایرن‌مونیخ
🇫🇷
پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102005" target="_blank">📅 17:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102004">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfeUbvs-0P_eubpA5IVt6nz6IOki-OohPfXPWXjPtxcGn_Nf9Yf-r5o4TvabIrTAX0GgpKNuQPryFrNyVCsGB5NSEKWuu-3Kfq80IzhbV1uvnvWpwnktmBiWy-PfmdFMMk8o8sY6jujKZ6aIUWuGCyOCcXvZ--r3_gr8lSTbXg6Ipsvr2x1Vh-MpKitbddPQ64O0SMxkv45JzHcHP0C-GhrXN6KHUwbTPpADCvrB8JEZX65uJuRAr-LAw9ddOGR7w_xhTHzuqF7jr96x48iVPZPnVcY5oPHqxXxHsP-qsKFNo1J-eQnmbGrTPqZK1UAwsig2U57rQPKiCG3rPe0DyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
متئو مورتو:
فولام قصد دارد یک پیشنهاد بزرگ به رئال مادرید برای جذب گونزالو گارسیا ارائه دهد. آربلوا می‌خواهد او را به تیم خود بیاورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102004" target="_blank">📅 17:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102003">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/botmedUF1HoTewWFtbN47Sra8X_Sv01o6ZUnB3_l8fJbun8f7hYxnHCrTJvxOoUs7aYTMie9EJdYoaDg93yQ2v5P50mQR-2QJdyVpKOeuNxssSFwCqacYQae2t0u4Mru0v2_HA9slhQbySvhhZGyPa2UQeMJ5xFSetCDjrb37fB1nQZIgrEEMzaHyOz-giWijtGAhSjEXOwMQX85hW90MquLMK4jCmCPMS6ysjluDprvZuz2LIHWsysLxreD7Wz0fYhTcGddP5DAjWpNqYaAfmZv6yyBrm4RwKi7O3JxFkR0Bz4DYHxbjNdEeUonT0L0PPcvg6_jriKTpgKid7yO5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سانتی اونا:
باشگاه الریان قطر پیشنهاد خود برای جذب جیدون سانچو ارائه کرد
باشگاه قطری در تلاش است تا وینگر انگلیسی را متقاعد کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102003" target="_blank">📅 17:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102001">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🏅
فوری؛ لینک پخش زنده بازی پرسپولیس و پیرامیدز مصر گذاشته شد
💬
@squadify_ir</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102001" target="_blank">📅 17:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102000">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=GEIlE5Uq2UV9J7YYSEcrii0G7LOMBFqvYoJBI21wzRAH1FsrcgU1QWVcsOB7jOwyvgJUxB2IGypWwNqUCN0t6ks0vV-O5Gte-uerkYqcA-FhnzHyAIJL1LAvBx4AOxwx8RAcwBUK3ltGOkkaEA-vgfBAYcZkDMSRGilvqWfxdTlSbrQ8x6xo6jQccLwmbZFLCpo6jHneMo40dFIiU3fggFmqzdIUB3pXgUo6PNd7ukdht6Eb7_-HexWdPYTY3fm6jOU24zGUod8B5Zt29Qjkp9TfhrM9F3PPRvfNHSuu84RI6SKZsmm74Hx3seWaVoe2B3UgGlxgweMBZP0OL8JBvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=GEIlE5Uq2UV9J7YYSEcrii0G7LOMBFqvYoJBI21wzRAH1FsrcgU1QWVcsOB7jOwyvgJUxB2IGypWwNqUCN0t6ks0vV-O5Gte-uerkYqcA-FhnzHyAIJL1LAvBx4AOxwx8RAcwBUK3ltGOkkaEA-vgfBAYcZkDMSRGilvqWfxdTlSbrQ8x6xo6jQccLwmbZFLCpo6jHneMo40dFIiU3fggFmqzdIUB3pXgUo6PNd7ukdht6Eb7_-HexWdPYTY3fm6jOU24zGUod8B5Zt29Qjkp9TfhrM9F3PPRvfNHSuu84RI6SKZsmm74Hx3seWaVoe2B3UgGlxgweMBZP0OL8JBvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
آنتونی جاشوا، قهرمان سابق بوکس سنگین وزن جهان، از آهنگ سیاوش قمیشی برای آهنگ ورود خودش استفاده کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102000" target="_blank">📅 17:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101999">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=Z_qkpxnmC7PQ3wKWX03COiiNBzUU2RRUhKiTDyi6f4QABDEYongR7yDDQdwRzNZKPdXYeZCQkBktp_jUmD6PuuK9C0FtSq4g-A0eDzEQjvZf_Zbv3foKP9jzg7JQEyQHeojsutdKAm1eIcmENxZ-YY2scdlWOWxg4K5q2i2wYmPZXvCHhK-MJ6UbF2AStQL2bqS3zyunl3OqAbwYq26JBij17WWc1TNKS8a1MgF0BOv8qoh4I9BbeOdPLJVZaVik4lA6im7bja1JhYIFsDVuNaVMoUqA3ZyhC69ILBstxOkLhFm3LGwR4cdfpD9Ax8wlaLio4GOWe6bPgkj32i2uRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=Z_qkpxnmC7PQ3wKWX03COiiNBzUU2RRUhKiTDyi6f4QABDEYongR7yDDQdwRzNZKPdXYeZCQkBktp_jUmD6PuuK9C0FtSq4g-A0eDzEQjvZf_Zbv3foKP9jzg7JQEyQHeojsutdKAm1eIcmENxZ-YY2scdlWOWxg4K5q2i2wYmPZXvCHhK-MJ6UbF2AStQL2bqS3zyunl3OqAbwYq26JBij17WWc1TNKS8a1MgF0BOv8qoh4I9BbeOdPLJVZaVik4lA6im7bja1JhYIFsDVuNaVMoUqA3ZyhC69ILBstxOkLhFm3LGwR4cdfpD9Ax8wlaLio4GOWe6bPgkj32i2uRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
قلنج‌گیر معروف ایرانی که با درودافای مملکت ویدیو میگرفت توسط پلیس بازداشت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101999" target="_blank">📅 16:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101998">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=oirfx1_Q3ZfSuohPH7rSEk4AUi9w0N1p8EUa0IT413p_PKz0Fy1akdI13mFzn9UxPe3kHURAYRbrjsPqwxXEnsFlt9Ta28RE-9jeRBRY1XQ_NiyzMTluRDDfmLp1AxdDmRQXTE4FL1IjOLy89NJNNkLO7siw6QPIQ8ZEue5y8Tah28QvL8DzZ5Z6N7JMAg48SqyAjaFgWIEOvRhyux_n-urDYsSPSibUzXV4AQRjFPr2MREz71lqyERy8COAr1M_wuoysDGD8jMT4A-QE5abo6bK4wLe76STAXmwCxqdlHlSa4HNSNap-dkd4ZluyV0e-0Ptu8y_-AsVOfA__hao-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=oirfx1_Q3ZfSuohPH7rSEk4AUi9w0N1p8EUa0IT413p_PKz0Fy1akdI13mFzn9UxPe3kHURAYRbrjsPqwxXEnsFlt9Ta28RE-9jeRBRY1XQ_NiyzMTluRDDfmLp1AxdDmRQXTE4FL1IjOLy89NJNNkLO7siw6QPIQ8ZEue5y8Tah28QvL8DzZ5Z6N7JMAg48SqyAjaFgWIEOvRhyux_n-urDYsSPSibUzXV4AQRjFPr2MREz71lqyERy8COAr1M_wuoysDGD8jMT4A-QE5abo6bK4wLe76STAXmwCxqdlHlSa4HNSNap-dkd4ZluyV0e-0Ptu8y_-AsVOfA__hao-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
اسلحه به دست منتظر آمریکایی‌ها
صداوسیما: مردم بندر جاسک به صورت خودش با اسلحه در ساحل قدم میزنند و در انتظار ورود نیروهای آمریکایی هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101998" target="_blank">📅 16:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101997">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfhJ8AWfjDk3lgT5s88j2s_nxXugrl8mQKPwibu2l-yucTI1eGfGja3wCml7C0TFurqOI7gu3vCrQ5k4i0bI12bMj1VpIvl3Zct6reRRLBJes3IuRCJ0FQ_l_yUIFNV-aIQZIJb7fE6MCRfT7x_A36WfKN4TvTLBONYbiB-CXQyEy8vC_yMybCibZAA1vejCILHhELbNs96GECpBKLpe-Cn9M7o9UXaffLZPL0hH8DSyR9FPd-EONoZs03Q2gvfrtNbBsHY-0nkcdSqrnlb7KP_QE-0iLEKpxKdZCCFNYfa_JTawdTXnT3GM6tQagHgua3BUiZdZ3Nq_wQ0LE6Dk6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنانی که با همسر یا پارتنر هم‌تیمی‌هاشون وارد رابطه شدن:
🇦🇷
مائورو ایکاردی و همسر مکسی لوپز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان تری و دوست‌دختر وین بریج
🇩🇪
مسوت اوزیل و دوست‌دختر کریستیان لِل
😀
تیبو کورتوا و دوست‌دختر کوین دی‌بروینه
👀
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101997" target="_blank">📅 16:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101996">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=URzCDDoYDMcYjo5jK4foOSHKXT232AkWHS4NTxN1xzUpkqYbf2e8b0yEAhKprae5NOe3FOG9ZXQ1LoTVA7IUdLCl0fS2kWU0CDs3NcjaGfPWIwalm12vG-ii8a2yDJP6m025DJEqRGFYI9BjyMKIzCmiV1ayVvmG6544QaZsXpjWEkqqXcqsKhy5MMsSwgocQTqWVp0oL9CpuKf_7R1hNBRnQtlA2vkn0DRb8QUCtq5g-jew5P6mdU2-FMgGnoDOnMASe93CPcBkegCpEhxAHhKoA9VEPDn6yVDEW9ZS2D4bDz6lev7DCakJy7VdYzFQ6U98VcDGSqwyEvn4aRgmbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=URzCDDoYDMcYjo5jK4foOSHKXT232AkWHS4NTxN1xzUpkqYbf2e8b0yEAhKprae5NOe3FOG9ZXQ1LoTVA7IUdLCl0fS2kWU0CDs3NcjaGfPWIwalm12vG-ii8a2yDJP6m025DJEqRGFYI9BjyMKIzCmiV1ayVvmG6544QaZsXpjWEkqqXcqsKhy5MMsSwgocQTqWVp0oL9CpuKf_7R1hNBRnQtlA2vkn0DRb8QUCtq5g-jew5P6mdU2-FMgGnoDOnMASe93CPcBkegCpEhxAHhKoA9VEPDn6yVDEW9ZS2D4bDz6lev7DCakJy7VdYzFQ6U98VcDGSqwyEvn4aRgmbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
علی علیپور: حتی خود پرتغالی‌ها هم کیروش رو گردن نمی‌گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101996" target="_blank">📅 15:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101995">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpnOF2v0ul-CWzqwltb3Invt7xhsUyRMqmTJtjLlNJxc3jaUe7fW5AVI2Hb2ENUDvOiMq8Qa3-dyA-l_ZAw-jDR8PTjUNibcEI7JfzVlvkmB2YTdGy3smLA72vA6YKJUX7wcNtXdl-LHHmFelzewu9v89GAspOE0GDdLK8NHQ7YsbDLpQniGNDRmHsdZJZE_CyNdrZkcRFbEewCVO2N9hs_qNWYP5q-sFWJtXbjGc1MetRk0ce9RvPME0MLHFJiYrRn0ZGVkAVShqc1W9ttfhLoL8IbiIT1Oed7RmgBB3cU31bFKO_vH_lwQZIvu8BKkJGqXmHm2xQuU_U50eGHjKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📉
می‌دونستید؟ فقط چند هفته قبل از جام جهانی، اینس گارسیا، دوست‌دختر لامین یامال، حدود
۲۵ هزار
فالوور در اینستاگرام داشت. از زمانی که با لامین وارد رابطه شده، تعداد دنبال‌کننده‌هایش به
۴ میلیون نفر
رسیده است. فقط در روز فینال جام جهانی هم حدود
۱.۵ میلیون
فالوور به دست آورد. همین رشد انفجاری باعث شده چندین برند بزرگ برای همکاری تبلیغاتی سراغش بروند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101995" target="_blank">📅 15:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101994">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🔴
فوری از رومانو: لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101994" target="_blank">📅 15:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101993">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqnyxJizCFhPSqsiEz04MRtoaVkF4fV-rTdPvstNb1ggTFTEDi_dK-B0OOzu17CPFy-F23OIVmUN4wCB7SAewnNVl_iJKgiwyOtEuzAlYusFXRei1z0yPZMMPZrjtuwWZjNJTbBm4GC3xD2UBMHAtLGuBdqOJmkClU_uVaDdQRflx2i7EJJDUgWHu4T2rRqTyQfvVULIrlFOM6VM1vbCWkcN0rcGNNPS-Yyuz-iYyDTbDmnDhozDwXhvU4Oxvyy4z80QlGtCy9bGiZSnByzHPbnKMiIVHISv-6354r1N1ZCjbVXQJNmCJc_oGQAXHQk2uuDy_HosThtSpigde-2a1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فوری از رومانو:
لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101993" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101992">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=Mf6dnREtmV8gX1L1_Mb_YkXQzpZ_NvJg2bdpcbGH2JOTndBb3MUA2PsJ99joXVQSrQPTC8QfCt1iMWHA_keOyVBnAJFPYKEsqicykXFXWLtu83Lsm2Fwz-J-WFqzYu5fuKbrFTHewRizkdAaO_P2ahBOD5zlmW9YKRfcLng9mET-_x2pZvtu8AcHpcVGGe4OCrX4Q_uCMwcRojGVxR570OMS1aB8wZdLf8S8c6DzDy2jfQD4IUariMiEKraheujqnk2l5K1IGxXV4f4jyT-GJFhYhtB8UIzy_XWR5OAkaOFatXz-k0NS8P9H9_OyuPhhQszMpwXPKnB-2o_VguOTPpodZw6MLBWtPgywxExgyOanmmd83qMeWWuNYe2qXz0KY3n5DvIjwSI5FG67ygkpoNpka6-lZ1Mx2GJ_OoW559YkKLe89coOWQ9BEyiXpwaN5RtNkfxlY390NStGCjz3GN6GILOqt_umeL6ImTSBvJL5zPhMhZsjw5Pq893hMODpa6XkPU_xGUyQ45Hz6RUf89gM7p9uK-_zIy0c6DRjDPkr7hi0MGi29wL5JUpchLt1LBP_tCP9zIYSRWMRefpP25P6TW_pcLiPDNEpNPx8CbWQ3glpZrO2frAhn8BRCK2_1EcvVPtsZd2Y8Ow81ytgig3sinhGXau1KbMAPcM5L6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=Mf6dnREtmV8gX1L1_Mb_YkXQzpZ_NvJg2bdpcbGH2JOTndBb3MUA2PsJ99joXVQSrQPTC8QfCt1iMWHA_keOyVBnAJFPYKEsqicykXFXWLtu83Lsm2Fwz-J-WFqzYu5fuKbrFTHewRizkdAaO_P2ahBOD5zlmW9YKRfcLng9mET-_x2pZvtu8AcHpcVGGe4OCrX4Q_uCMwcRojGVxR570OMS1aB8wZdLf8S8c6DzDy2jfQD4IUariMiEKraheujqnk2l5K1IGxXV4f4jyT-GJFhYhtB8UIzy_XWR5OAkaOFatXz-k0NS8P9H9_OyuPhhQszMpwXPKnB-2o_VguOTPpodZw6MLBWtPgywxExgyOanmmd83qMeWWuNYe2qXz0KY3n5DvIjwSI5FG67ygkpoNpka6-lZ1Mx2GJ_OoW559YkKLe89coOWQ9BEyiXpwaN5RtNkfxlY390NStGCjz3GN6GILOqt_umeL6ImTSBvJL5zPhMhZsjw5Pq893hMODpa6XkPU_xGUyQ45Hz6RUf89gM7p9uK-_zIy0c6DRjDPkr7hi0MGi29wL5JUpchLt1LBP_tCP9zIYSRWMRefpP25P6TW_pcLiPDNEpNPx8CbWQ3glpZrO2frAhn8BRCK2_1EcvVPtsZd2Y8Ow81ytgig3sinhGXau1KbMAPcM5L6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظات خنده‌دار از زنده‌یاد اکبر عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101992" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101991">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=SvuvFqXXiTkSqOY1HIWkq8VoFvBuze1ll9FkDDebepaDQFV669JUL6JIHYqpIfljwLKHbxXggKWw-oQK_34FTmf9M0OUNQW_7z7eqhk0HbpJbbsJa76IuJrXPXXUxwP8G-QiZ51rlRTWLgDkn0VOsU91XnUHd3UDg_yoZBu344CEs9eV_2yJblH0bxM6_y9xJX_1i5OyAW6ZdtWOzKvUA7-_-kNOsZxLl9coP5Ay5wY-927tZ22zN_KDl6jk8leoArehszkrMibiEAf_EXBw8CBERDUt6C-sxpAMnEq5mS8XkS5pChtg7ytSDgxd1IsPygUHqh83nTt9kKhyn4d6Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=SvuvFqXXiTkSqOY1HIWkq8VoFvBuze1ll9FkDDebepaDQFV669JUL6JIHYqpIfljwLKHbxXggKWw-oQK_34FTmf9M0OUNQW_7z7eqhk0HbpJbbsJa76IuJrXPXXUxwP8G-QiZ51rlRTWLgDkn0VOsU91XnUHd3UDg_yoZBu344CEs9eV_2yJblH0bxM6_y9xJX_1i5OyAW6ZdtWOzKvUA7-_-kNOsZxLl9coP5Ay5wY-927tZ22zN_KDl6jk8leoArehszkrMibiEAf_EXBw8CBERDUt6C-sxpAMnEq5mS8XkS5pChtg7ytSDgxd1IsPygUHqh83nTt9kKhyn4d6Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
دستاورد دیگه تیم‌ملی در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101991" target="_blank">📅 14:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101989">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZOH7tGkMHQwcGc08Do0Nk7HVtW70FkSJOXZMZ7tDcKFnc_DXpYYJxXduHqeRSY0JK7RWD8bAZgwLVjtLa61I6ISDD2dDx8N9mhFyDLC1z5cIp6L7KLxfoUqti9uBB4wQysB6qLYhuFRLcNEVorm6PHiBM4QKKDMyhVy1Ga7eBW9Ss-U7k2k06lffNN2C85lUDjq5GtFVPxxVMEeA-uHB8mNghyRdWASIvPs6tCdsS7RWlWERHzCmk3qNWS6hLT1wZEkAtAmE3tXAiZrFTFnFg4Uo4xN00bsXLWmUA15LYOSiEbpL1x-4ZFFPncL9Z-6yAm1WaJt1Df7BzP3IKUsiWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MPsibcGW50eLcCXUZu_Th5You8Pq-Bj_EUwPpRA50hvGssJn9ainofxpnpZENNhknumv1_q_piHiaWvHTgQf5sKbOCPSR-bd1wVE873ylv6ScTwxjp3zwUG6BBVgorX-Whipy4zObsMzdBvzeMyF4f7fYhX9OshLDVzJCJR84UKoQJsnGSxde_I6FsW8CGKwf4138DzRxUITg_xrfBeSJRuO3H2Oa7Cn1eFiCmo6k_IBIB8A8NnaqvaUpKMiua7WUlEffbNSBlllZkUm8PBmK991RX-PLmglZXlwZEtzLeyEgYd5ZT761s_d245W-_4r7vikiHugJ-apfEC1RCDpIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اینس گارسیا، دوست‌دختر جدید لامین یامال به این موضوع که گفته میشد باعث جدایی او و نیکی نیکول شده، واکنش نشون داد:
من به کسی آسیب نمیزنم، چیزی رو از دست کسی نگرفته‌ام؛ فقط دارم زندگی خودمو میکنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101989" target="_blank">📅 14:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101988">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=tg8Xt94kQQw-STvYkHHdqIM4gj3Hx1nQyGTu2e3Jy365ZnFRqUfSqq9UmvP-O_Ymf2f5ml4gxqF020JZxIu8Il9iCt4pGaaM4QYViivv8MoHONz50BpIu3AKlD6B0OSCZiaddX4VOfz5NI_SWG8C1xxgavg0Wg_bxdy9kS-m8OTxZzhkckV3wTChHe5yF3eVznNRw2Z_SAxhUiIcsa78VJDbvbvnliwdlfQQsGuGEuNqBUEEDYaCu_qHNFzzrO1fc0dOzg9MnFwVcQUl94xVhzsmsuPGEzggtks5l497H3bmwwq2qhA67S3Zd24jGDev1VYUh3blZGIu26RKeATXNixFPfmt9AS9wFS5W0VqMbY_wsvK12ah6q7iUDSXowU9IsF4KN20CXRJLCUDIh_HylB3K7AqxptP5c3ugNggUyD3S20-7bgYrT6fljfOHnrHNVmzEYHsHYWsbNu4A1tRx-_92ohZCwdK5NXKYbV-G9zjC-DfY0AsOEjEXzOIMMAOteOyBibd8EMnQfs61sSDtT0wcFis-IcnxH0kQxKPUIgYXFMBk-Qe2ycrKqjUYvsBfaczUD6CBvsUOIc2aQMQ-dt50tIBM55vqZ34HUYwLFAbFkY4GC4NyvKULyn2l6cogB5r_l07lfn9MJvcPa_O9mB3Rzxx_vsNXj-dlF6PbfU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=tg8Xt94kQQw-STvYkHHdqIM4gj3Hx1nQyGTu2e3Jy365ZnFRqUfSqq9UmvP-O_Ymf2f5ml4gxqF020JZxIu8Il9iCt4pGaaM4QYViivv8MoHONz50BpIu3AKlD6B0OSCZiaddX4VOfz5NI_SWG8C1xxgavg0Wg_bxdy9kS-m8OTxZzhkckV3wTChHe5yF3eVznNRw2Z_SAxhUiIcsa78VJDbvbvnliwdlfQQsGuGEuNqBUEEDYaCu_qHNFzzrO1fc0dOzg9MnFwVcQUl94xVhzsmsuPGEzggtks5l497H3bmwwq2qhA67S3Zd24jGDev1VYUh3blZGIu26RKeATXNixFPfmt9AS9wFS5W0VqMbY_wsvK12ah6q7iUDSXowU9IsF4KN20CXRJLCUDIh_HylB3K7AqxptP5c3ugNggUyD3S20-7bgYrT6fljfOHnrHNVmzEYHsHYWsbNu4A1tRx-_92ohZCwdK5NXKYbV-G9zjC-DfY0AsOEjEXzOIMMAOteOyBibd8EMnQfs61sSDtT0wcFis-IcnxH0kQxKPUIgYXFMBk-Qe2ycrKqjUYvsBfaczUD6CBvsUOIc2aQMQ-dt50tIBM55vqZ34HUYwLFAbFkY4GC4NyvKULyn2l6cogB5r_l07lfn9MJvcPa_O9mB3Rzxx_vsNXj-dlF6PbfU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
چنتا سوپرگل نامزد پوشکاش ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101988" target="_blank">📅 14:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101986">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eYJz_6k-SR7qV29WUrNBfbz2uTVVf0mJATNeH9dBXNr4aJKqH5YerzIlrb6jab-iidUPmzOwRKak2FiZtPOZlKcZIYUjOe0fRNkpdfzq7tlQFoafXrqxxe61x6TsY2tz1fzjnMqGvYKYfuQsWU3etp6nUS4ZsqQGq7seDLJW5EftPjD-sghczU5jO-dFmltpFJLhU8H1XgD-hpLtap0pfcbqE9y0ky4llv0hBWU-dAPyx4pc5iU9beQHfllkugf2vGWmPsx8t7FX-tI1S6l5J2Btr25ZNYRhkrhU8TB4EfuQ9V2dPjMow27hFtYv_x710lWaw_yi3O6qN8DVyb3oDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0cdPr2fFo9WDR6yWEtg7UBak-5_2AL7Ofb8oNpKsMwsqE-6TjvxNmgFs7QF643AVZMd5eUUEQ6nH_uKmrcbek4TysSAVPPGMfUYuNcHyA8n-JPCDpc1K1t7Sv3uuhMJDlnzcbGegp_2-GBGNnh4p3ARcABFFz2QndP0qTEGu-Fjj7PAMZRGcoLon-Bwdd1HrheCy7uZmEwfq7v7ii47TP5bk7DEn8j_CgwjSseXPbc89Ofee9GmNtpp2gg4BIcme2CWDdY5o2C2OLocPxkaaW1usyqNEEJe9zMy6XfV6skUqsUkTXInv-cHBDi53PkeurNhboYshC0ir_bAQPbHZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تاریخچه رابطه‌‌های لامین یامال:
• 2022 — سینگل
• 2023 — آلیسا
🇷🇺
• 2024 — الکس پادیلا
🇪🇸
• 2025 — فاطی واسکز
🇪🇸
• 2025 — کلاودیا باول
🇪🇸
• 2025 — نیکی نیکول
🇦🇷
• 2026 — اینس گارسیا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101986" target="_blank">📅 13:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101984">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JTR9qCEm57Z6S4kDJrPUB0i2IAevhVEwIPG-kCOIO7VPdxAECQSrgmz58O3F1X6zjLJFKeOpUFltkwn0kjdsu-RCegwozvexRo4tGqptoexTPrT4kW0SLcan0XcQ2wwldXa8advuBggKIBGzyqQ3BO-eO5kc-HEFJe-iXPNx7Wpjyr64vwN1P48wdb5XpHEA4xWgo0CVKAS7tK1-ayK7iS2IrzeUfr6mP4RjJAEQH3ZZwn6ZNaVLzGZrSjhjJd9VPEKaA01ZyI6vMmw8nwFgNmm4w_lAnBmfyZs6I7jay3z7ytt1WelHDM7820UCwZBVrHwTSwfZiLV2BgdX3RMu4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7u9SPbtNMl3Y1VxajwPZ6f6kb_BxpK7bIelH992Zxm33xNbbmMFvBBZev7Y62nHKbzct5H_YXy6NP_QNCDHA5lpxVLwLxTY1dSxK-m0xG7RFx4fb8GLuA9zpOY1hUQ_p8ctAmyesQ7lJSUf6XGuvxPdp-2TeHH0sBi38iF_YnIwFvjToKbZ-5ztB9vBT3Y1laepG7259r-536pd2gTiTyNBsCQo_6pXL6sQeVde8PEyzZNyhxMyODK0vBI1wxAKOfaPNG-fyIcB0_E1qGamG-MJI-V57kzIpg1Dt4BdjtogxgzBHcBuFo46jgls822F8ef3qeucUTOhsA5YOw9yFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
جسیکا توگا دوست‌دختر سابق وینیسیوس جونیور:
این فوتبالیست‌های سیاه‌پوست فقط از نژادپرستی شکایت میکنن ولی همیشه با زنان سفیدپوست و بلوند وارد رابطه میشن. اونا هیچ‌وقت با یک زن سیاه‌پوست وارد رابطه نمیشن یا چنین رابطه‌ای رو علنی نمیکنن دلیلش چیه؟ جوابش واضح و مشخصه! خواهشا این سیاه‌پوستا فاز آدمای اخلاق‌مدار رو برندارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101984" target="_blank">📅 13:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101983">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101983" target="_blank">📅 13:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101982">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_rOnUYqcvghJbp15q4gKScujPjNObXs6fMpDvQisPglmwz291r0-XlumMxr9fNToFvOukr1covnFgx17jBF6MXlPFvizWUWKqss5JbYizIp2a4TeBqAwV7j8Z1xgn5x_ulr-EqOx-caa4zvAcET3HZQKq5LbddSvyRUlz_XKJNLnBEMu_Le8kOecOnImLgQiRHpVWhmAvyIyhWLCEZM24whN7jC044ZR-JRLGy5AmUQ0LhgiOPpPVz7uY3xqeFJUgvyfIKnrDhTS64kL8EKgtljxk9j0XcBvIsP1CtrCX5hf2aPPnFRf5yhQuMX5N5pHUoc-SZmahJFCaGVKgVJQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101982" target="_blank">📅 13:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101980">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FcgvJRUNdG_tXHiG0RIPt8LiZ2mnUW1ukgPP51kGO0xtrnnbDNXAJUwbYxnt-Htq6XvAs-3UbOXXOIAc_eY_TGMtCyz3WXKc4AO5vxbTZTWE796fxNh96VCzLAgt3DtWwRvefDalZVSvAjzX7Icwc2TDn9e_aAV13Kz7xYE-W4HuQtlN090gCB35Ohl3psX-22NH935UVyf7tsekf4V5Ge_prCjxnpyUEcklChUVST89vIFCLsc3kdRyGKqy2TR5neks0zZyX-QhYe-K9EKOZaKAez-9Ly7fy6s9Gy8bqYSxi1SELXCJdUO7xujpDWpXhX7tTSypb2QcHxrCDLRp6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dNbY7l3Wf_Gs6i_z1kVulDRgw2KXc7diJK0hf8DqDOva3e27I2-uJvrThLydo41WiJKTUBVXJtWaAX5wIP30Zy-jfVbxcYpze2aZA3Sc-IMAw8V87rsqLSJr0V-SOzZau-tR-3zC1SryklVszguqvS-GgSzkI11aNXvgBC3vPxs2bm_kxedVvf7pLaVVxiKoj7R_ED9ecFueGUUToSpg2yJxdviFk15iJPmRVkrwuRvqpssS3cA3GEMnyaH88wqrgVeX0gJajXhURYIUHQ25D8FQX0M86y9iG4Ont3kDS0TJ5GeH83cQF9D_pv9aqrBPe1Nd1AP3eEpGiJ9gWxGgtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📅
🔵
17 سال پیش توی همچین روزی بارسلونا 46 میلیون یورو + اتوئو رو به اینتر داد تا زلاتان رو از اینتر جذب کنه.
🔵
🔺
فصل بعد اینتر تونست با حضور اتوئو یکی از موفق ترین فصلای فوتبالی تاریخشو رقم بزنه:
🏆
سری‌آ
🏆
لیگ قهرمانان اروپا
🏆
کوپا ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101980" target="_blank">📅 13:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101978">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rn8khMJyVCHuB8lKchqMMU2w2VckZi-SGutzgCealwM1ChBuuPhMKSYDk5pQLNzS_2pMTqjARGGMndHGMDGZVOlPGexs6fNngIIHf2vGFuSeBP7ysG4vZZGhOPz4dTsLVx3GQZq2T70kXX5TPYOJ6kWeBElGOL8lRGOpBZFbShpIbYpaqUTQ5QqelAMJlZvfVbvggrKzQ4mv0arjpIqHnlYommJBYiQaseM3-Jd_gcTeByihBCwRjRlvmuxs_92IFEJ5N5Zl1ZzsLxhB6-SN6jA6FHoPRtFIPGIei4FJJ5nR8MxhkgH5d8_B8t_hIhr_UEM_eAoCuWVGqBSYoMYdBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KaXYSTrfUHnt15rb5JyZdm-C3O9KClgI0dLTLNPbSEXVCJPh9wAmd2oFlNOJbm93bj9Y1miQLNe48VQt1Be1tgdBpCWmSKEtVjNcfP6oxoEh6j39db8_Jt_uUUFW-eAF9H5knbHcyOAJJRRzJzjUR7YFvzGfznD4501NuSN0cLr8-hQXGp-XEC_RssZloTn6SYrp1cx34MzbMmg7r-0AYYi1AKZxyxqpzYJ15GYdcZr1kCTDQ0X4f42qZWIKtenF1SfX1xAkxK4rBoN4JcX-OuGItLRa2jDeadV-TezcV5zZLEO0DDHbyYypLodOK327UI0it3mDu2mWG9O8-2dybA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
الساندرو نستا درباره غیبت ایتالیا در سه جام جهانی متوالی:
باورنکردنیه! پسرم تقریبا ۱۸ سالشه و هیچ‌وقت ندیده ایتالیا توی جام جهانی بازی کنه. وقتی بهش میگم ما واقعا جام جهانی رو بردیم، تقریبا باورش نمیشه. میگه: واقعا؟ برای نسل بچه‌های امروز، دیدن ایتالیا در جام جهانی انگار داستانی از یک دوران خیلی دور و گذشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101978" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101977">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syfdKn1kiACQubCX5gUd012k_TWMQZL3bfwxHxzrs_9Lbp7eHPBUQIxwVfuDeOQltpddgMPGSDIRNVSJ3kniyM_ax5AWrZCGJr9HGbUX7OGvDLoc1n0Gwts8rGESCsvJiArjfiGzkdX3sqIGpBaT4BOCgbbFrHzpAhtTVNQLJSci1yl69IlOkjeF6zdtwS70-M9d-b2vtLmOjhir_jP9U2xuB6ld0x8wfY2-loN7mLxYrtEpzPaDG78EpoJy-rsPlLn3Os4_ZJEPGZ6hP8cxTMZNsVrCEOxTgS5CwkrMkWH3FGRX3b6-VtpJ2wUp3FQu2735V9UWLWYmnc94jiDt_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
ترکیب آرسنال اگه همه شایعات نقل و انتقالاتی به واقعیت تبدیل بشن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101977" target="_blank">📅 12:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101976">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otXjVNrs_OhlFgjyiZL_JXm81ms2ZXAaZYh3mrUBGLZZuIgMLZQi70jxKprT_QJslmHebZFLbd2dlHvfMCTIHezN4kdtpiwEyhseTYhWYpRewvtulBs7ePRylCwuR3gaZ_gEn0k61kpw1lUDmF_OEoAgPexa9p-HLL0k_NeXwtUBKJahdam-2Y67VS9yIU4ptxc6r1VG9dUyVWYKUOjoaL5Rii_0ksiIiV55kXh9ApuiqQXbTeWbZK00GokrVwRIzrxKCCdRv7iXy50indJ3vZV99ZFlbufFHJLdQHT4TP8hINbjSEypjWAUx74QQ_QZFrarCkIVaVKsyB3mK4NKyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
طبق گزارش‌ها، بدهی‌های النصر عربستان به حدود ۱ میلیارد دلار نزدیک شده و همین موضوع توانایی این باشگاه برای جذب بازیکنان جدید را محدود کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101976" target="_blank">📅 12:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101975">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ddfc2f853.mp4?token=CHXMpASvC5LNn1fa8O8V5IpkUNotvl69jJ_YtrjZQzGa3_RMh_Q0UPTNXfcrM2YPWkUZfSVNXEKResnoeHmWn-EJdWnYfPk-hhUeIWEHrOVNpP0J3LQOQkXA0i1lgjBc2-N7z4NMF0CoWWior0el_OeQE_9VfypXb7EMq4SvNEGos848doCrgEKzLh5C-dRSlwHpIdibzZ4Bu_L4TXI1Mdd6Hm7E6LlAWZGXKP-yjQjf3KGZUeeOrONK-xi9VDg54z9G_KmaZHPaZonLSjXJdGj0w2WQiEbPjac5-bt7r8q1ysbimC3Zl1o0btV_Jd_OOvB260jSd7i9e6fyu1dkOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ddfc2f853.mp4?token=CHXMpASvC5LNn1fa8O8V5IpkUNotvl69jJ_YtrjZQzGa3_RMh_Q0UPTNXfcrM2YPWkUZfSVNXEKResnoeHmWn-EJdWnYfPk-hhUeIWEHrOVNpP0J3LQOQkXA0i1lgjBc2-N7z4NMF0CoWWior0el_OeQE_9VfypXb7EMq4SvNEGos848doCrgEKzLh5C-dRSlwHpIdibzZ4Bu_L4TXI1Mdd6Hm7E6LlAWZGXKP-yjQjf3KGZUeeOrONK-xi9VDg54z9G_KmaZHPaZonLSjXJdGj0w2WQiEbPjac5-bt7r8q1ysbimC3Zl1o0btV_Jd_OOvB260jSd7i9e6fyu1dkOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خارکسده جزیره برا ایرانه
✔️
خارک و سه‌جزیره برا ایرانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/101975" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101974">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIE-5AJ08u_4utc5RZx0JJ9pI0i0X9Fda4AL3B9Fw6zpDd0MGo7tuDnf4fMQTvdQb3gAtRtSZCT2roYG51wHdXTBda50C16QyIXl-h-6eLPd1sYg5ucT1yAVj2azhXjHDLWZydUAXChNoTbUYxDA-oUPvOOLHPeCkrxbE7Zg2RJZE9hKQNtTXPrxJCjnmaEeATWajOjlY4fUqJIOmXPqCschW-bJJzTtKISbuEl_RBCHQ87-khM9ABt-9igk8fqWbHv7LENoYXTaitf_P4bENqfn0u123mQbfzUxFnxafbDX4S_8ZxlWVVXp-7LbdaEJbcjE0nEFwS_3ICQv8I29jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انزو و خانواده تو تعطیلات
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101974" target="_blank">📅 11:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101973">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeX4oMzTKaIOKHc9MmuqGQ3M60hwEh8DgqxWd2yaVfSc5c5CAIq1DDRnJanBy3XCMae0VVs7Rvhs6kY3FaT3ygoaP-xKK7Fq1EzzHFSEhC0Xx3DTws2xbRsrqpRpxhnyJhbtnwNjF6vtIK_LiSyFaZWTCr-UQsqeg9SsVSEs_ZeFbmAaEJjcIQiglcsll6ek2Qzu0SRM30GlqMXziB1IVSe7IyH4nCXHdGF0mvVEnXHsy0RL6RzN2-fyl7FWrgijm45E1myOztHFWV9rZGS4B5Sh_mi6WOP9uFMST-1an17eu3nwaCPoA3Xyq7uQkQbN0BhrWjq3GlHeM757TKJymQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
‼️
مانوئل نویر:
🔺
هرگز آن لحظه را فراموش نمی‌کنم. مسی بواتنگ رو رد کرد و درست جلوی من گل زد.
🔺
بعد از مسابقه، بواتنگ شوکه شده بود و گواردیولا به او گفت: «احساس گناه نکن، این کاری است که مسی با همه می‌کند.» سپس به ما گفت: «حتی اگر صد سال هم مربیگری کنم، دیگر هرگز مربی بازیکنی مثل او نخواهم شد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101973" target="_blank">📅 11:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101972">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c941f7e49.mp4?token=m88ZWdWuO7SIz89-1bDtUvWSjSpNtPhv8YezbP4wAKqbFi2ErqJU4UhGu7W27Gc_XpyZlPX8GGYkdSzXdDCxdLaErcJ0XIEypt5kLBBRmVhuRjCFL1Ha_rV6JFu7FLKeBgg0CAODBMPIT_3iplI7F057cdYvgJNN8_V1tiP9K8hDi9CamoEuo33-8vfTvrmCeo3pWPsKXCQWTmvtVsOUpdCC1HIKklunWcW9OqDlrNXG46-D9u5FJmeqPuoYkwq3sZfSwMgfLXDyIhEXgolqp5aklhhQ3bNS8_OXS3bEorgAM_pbIw37aL7vInikB7JoQmo_JIk-VRIG8o42jW-jqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c941f7e49.mp4?token=m88ZWdWuO7SIz89-1bDtUvWSjSpNtPhv8YezbP4wAKqbFi2ErqJU4UhGu7W27Gc_XpyZlPX8GGYkdSzXdDCxdLaErcJ0XIEypt5kLBBRmVhuRjCFL1Ha_rV6JFu7FLKeBgg0CAODBMPIT_3iplI7F057cdYvgJNN8_V1tiP9K8hDi9CamoEuo33-8vfTvrmCeo3pWPsKXCQWTmvtVsOUpdCC1HIKklunWcW9OqDlrNXG46-D9u5FJmeqPuoYkwq3sZfSwMgfLXDyIhEXgolqp5aklhhQ3bNS8_OXS3bEorgAM_pbIw37aL7vInikB7JoQmo_JIk-VRIG8o42jW-jqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیوزلندیا اینطوری از بازیکنای تاتنهام استقبال کردن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101972" target="_blank">📅 10:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101970">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uUFOqRG08kbH6Ab-i5iU7tq_Y8UTM6cneo0HjeskpZFdkPgpFMFvBp670ifGoBxXLP6rurbpZYKZh3dvuJA6tB-oP7D0-N62GQJh5ZzM-2PoYaEb-8NH4_7S1n34s2Gu-u4Nb2YUNa23_sLgxpFpmKgtv1qrA-LWyVoHhvrBrA5ur2f94-yj7-ElfJkTDRrMroqMDI5JONxeldAqJBDWgWjwx9R0TtIw2pRPk8ZdcOW-QavR8qWk9nvwX3xB1-71OomiIcLMkY3tjlc2QDDRFfvZuseAyCVEc2SJKNxepbJpK_i6vA7JArRcfot_UJXGxog91Lb2yHnsduMa2P7GPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T6pC9y90jOEKZzcpywvKu-jJMA0SChqLlT3KEcMvz-_C1nyNi5X_08p80LEMV8RSgwwRoKXXPANrQJ6y01IVJMG0dR72YteqDQ8yExr9RPVYNrXbKxQgfxg6tSKr8NIzKs6VidBXDRHsCeKVCBVu2vuOGM-3HY9V0xhS7bkLsctRH5VBTB7mXV6nqKGyg1tHuxIbjqSASFjd3OdVc24ImE7FPzBlanyTb0V3wMmItc76FvGsGWcNdFQyjJzUdCBLkjC6zG1uu2fzqf0nfQdm_s3zCXHVsNFxVP7vric1SVQtgcwAKnVGjF_s0z1xQO_b8PIzdt3g1cfJAz9-uHmmyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پدری داره تعطیلاتش رو اینجوری تو اسنپ چت میگذرونه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101970" target="_blank">📅 10:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101968">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G4Gve4fxMrarwrKcXLVHff9HPURhhhGbM88CBUorgie7wC1daRBcW0-gW6AVtYLWY3EdXgBrRnQ3xSdauhBbFrXIlbS1fEYVt3MUL9cTgxMfHYk2pOQ0friKQ9nfYExwrVW7C400gTIbIrCV4Op4OSeDielGfHEHNxFL5IuhHAIevWpW7rxE5jjiOtPsZHqplIci1TA3aV-B3ziIIwJ6kHRPppw0-b9Qha7HiLIPh_iUZs3UDGDODM2vjYrdimZd9Lo3Bk3din_DXHBKIczJJmSDA8jTELzqIpoXJlu1OJiEJvB0uq4-lAWOpY6NYps35WX48vJcNPCACG_9wtZKog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ihUZ1gjcwTDt1peEOIoQrt4jo016Yh3zdy3DC6oJlVeuxcFnii1CsjVGQXrCAoVnczDv6lcJZ9UCTXhsyndB2WwvksvwandtOYFSHDtQJ6gGVeyD1FFeH7l-mjCrzltUzm2HIAyG2J8ZHH1NpJN25kpuv1mJXBKmy52WWmmtNK4ZkAgO7gf84usR2fZahAELT9RIt5FLz2k1uRVNy8qKWYmyfyoPe1uIk9BHUmm0YWFrtnN7zIm_1pCsRwTIxITL7B79THQbbvlwqxooitWc4enmvXNwlQlqXHtgNK89u8Q-qegtzdqM4de4qzpWCjrku6FQeHEnv2XDpYluImQ6cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
😞
میگن نیکولاس پپه بعد کات کردن با اکسش تیانا ترامپ ( پ.ورن استار ) الانم داره با لانا رودز وارد رابطه میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/101968" target="_blank">📅 10:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101967">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tpv2QvJzBSbkWy4lQDGlAu14sHRk4E29z0C5A4SJykvRTFqP-QotoqQD64nJfPxVjHzOFcIGNDvvs_mIMjfqO3_n9PXqKFl9fCbI3Tl69frJ0PsZQChADkbX-ryewq9xwqu83QD3Gqe-uH9EE03Ij3yEFWg7ZpIVSbKm6xTKj6FDYGyHfAatjV__GBaV8bNu_10_tJws4Zf0TRQeeulJHmtEDOI96WSwMJHvfKTA_NkQewQPKK1d2DOHtxwrWAE7l0kIPE3kuGgNnVc4fWzAzV-0qzoK8g0-cjYvbC52U_HvOJi0iBDb4c3dAitCy40oDZvfPQwLpOm0CRVXxj01sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
موندودپورتیوو:
اگر بارسلونا نتواند خولیان آلوارز را جذب کند، دیگر هیچ مهاجم نوکی هم نخواهد خرید. بعد از جذب آنتونی گوردون و کریم آدیمی، مدیران باشگاه احساس نمیکنند نیازی فوری به خرید مهاجم داشته باشند و معتقدند فصل آینده فران تورس، دنی اولمو و رافینیا هم می‌توانند در نوک خط حمله بازی کنند.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101967" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101966">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArCtMrrte9OnpRNn9qa-sm50j4YI4pJCdZLwn132AVg8Xm6UmhrF4o7vwBVmXA2hJQk9w_FfCp88vkz_L97b1tIIifENFRZB3QRD3BA8gPM5ay1RfB2Xlk7dNBVjWyiaBseJrwd09yPHqze7zA5SYA1sjSD_gxPEBj6UR0r46Nuo4JzooOevkO3qBiZpeWP-lQj2t9RFDU74BCS3jpnLHG7V5ntYM_XMI46r19JVwp3GJsGLicfAPT32cA7jVu212dvERMgVvwZV5vp1WKiVc7qsG9SEdEgDcaMzOt9qZUApWbKT6UidhLxi_2lTTHkEByG2ro_Sikbkx_9vJ-Odmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
–
فابریزو رومانو:
⚪️
در ساعات آینده، باشگاه رئال مادرید یک پیشنهاد جدید به باشگاه لایپزیگ برای جذب دیومانده ارسال خواهد کرد.
🔻
این پیشنهاد از 100 میلیون یورو بیشتر خواهد بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101966" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101964">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vpmaw_IHUAFsJmVB4N-Ns0lyK1k3AJjGQnW0MLcd7mvcbFIpyEvKynrmJbYiddkgJ3Lsgn0fFK-pFCe3rxSijcrtwBLJa4p_6e32SUtFgC3z7d9OabY-aelQWefL6F80YReoOfwsxJOGcdybPq_CHIjMoiTAxrDUg1-nHOSHuO-GTG193hEu57naGB4oKKVL44O7drbd2CFdIKLxPHk-q26UDaUfx2BS4znIzW8VQV4T1G8G8R-uPytZJqb3kNBOHvYEXBI8fsuCvEmwpk0nuffO_-Omab9bEhpM--hHw18YUx6SSydgqTJuX2LlzcDAuil9pki8UJx-7hpErlYifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sUYWjxwNLPhO5QmqLQS-9Xbo4wWPQLCbHLWDa1mu5Y-fRnxmwmlqegddVQSBhe4Fu6Dq-uNmCOFSHvUmlpqbJO2W4TSeHincA7KMiTwTn15TyGuaaNAPLxxd89MMbYmz-Pob5AzpFfqWy09yd9e-Tg6sbU9UnTeabM5l0DyyU8JS0E1dCoksGZcOPiKyusC6btPss2FX0plf1jaerjEcuS5NnV_9iXXAE1vWtOkqBWrx-V4ngOaP4madIDR9B3b_PMMtXRrfrfOfggDmXOhN4BrkHL_OZTOyancgQgeUfpoGxS__Sg8sE0Lxeg9nf6PW2dJt7wIVWDJdLG5uKfO9Ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
سوفیا رین شایعه‌ای مبنی بر اینکه حاضره شبی رو با کیلیان امباپه، آقای گل جام جهانی، بگذرونه رد کرد: من هیچ‌وقت با امباپه شب رو نمی‌گذرونم. هنوز باکره‌ام و خودم رو برای همسر آینده‌ام نگه داشته‌ام!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101964" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101963">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksUUOMOJW5RTFZzP0f4pYwxaVtlLnpL5-vSJSa4pQuq6lL9xUJjHJkxptoIUqCjT9NCNiHeLhZibLivnOAQjKE2lK7k-IENqFqY53cYrg0NRRP-dcr2wJaSLNUXpRvvBgrw5oLTme5K8ECr3nrcx2LqQxBkUX2DEa9huofACERHzf_nrTKBfT9FmHorv5qRu6e-L46PouRZOQFuWIMPL6J53AaP29m6XfNF3ue7ikEMyFJr3YlphpDGvFw4vsHzrfFE8awcjUnCmU4kugxMfY42-S3opMM9B_lJ4k1jHzn7rxF0MJY0X6a1VIz3V1-oMdKTS4HpSwbVXptQr3i9aXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رونالدوی برزیلی درباره کریستیانو رونالدو:
فکر میکنم بازیکن‌های خیلی کمی مثل او از بدنشان مراقبت می‌کنند و این‌قدر اشتیاق پیشرفت دارند. من تمرین میکردم چون مجبور بودم، اما او تمرین میکند چون عاشقش است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101963" target="_blank">📅 09:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101962">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0d0985c7.mp4?token=pxfNPFhiL2HmCWa5APLMTkDvIbZfEx5vFMxi9mtpBK-PLMCCx9wVTSkDRuoW3aMegguhehezZx1vURsx1K5UpEGZvSB0_ssv3r2xMlDpT_2i1xsgWwgrTRO-iivRZvk4aCoysex85J_qToGWd2IxPThfpCoQbEOElSlRsXSsTIu8uAbaHJFG-qaIarqScoq6RXmnggCuTuLFwCRLFFIDWGca1dqTDqJmSamvH6cZhYKh3XXlfFLUL-yqfWqCBY-6wkNftqCZz_vbpGc4VgKnlkow5x1mzQllJ4iOqgAf73Wkbkcg-wt33OIWqpu7m3csHAHRHlgU0341JLWKNg7zSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0d0985c7.mp4?token=pxfNPFhiL2HmCWa5APLMTkDvIbZfEx5vFMxi9mtpBK-PLMCCx9wVTSkDRuoW3aMegguhehezZx1vURsx1K5UpEGZvSB0_ssv3r2xMlDpT_2i1xsgWwgrTRO-iivRZvk4aCoysex85J_qToGWd2IxPThfpCoQbEOElSlRsXSsTIu8uAbaHJFG-qaIarqScoq6RXmnggCuTuLFwCRLFFIDWGca1dqTDqJmSamvH6cZhYKh3XXlfFLUL-yqfWqCBY-6wkNftqCZz_vbpGc4VgKnlkow5x1mzQllJ4iOqgAf73Wkbkcg-wt33OIWqpu7m3csHAHRHlgU0341JLWKNg7zSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚡️
بخشی از گفتگوی جذاب بکهام، زیدان و زلاتان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101962" target="_blank">📅 09:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101960">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fIpWjyo7dRdmN6TUkh63jLsewBSimDaOfcuMYohb71615jq57iSJIVJpYUNe27l3nUwzlj3xicJrrCTfg9vm4Wgc3KNuc-sgtakqZUgyzQlb9Q3xf7xxl32u4jbMvxxCdtOvt1GYpThCgLBZ2MFldwxYE6YU75CrAYBqu34s3gWiN7yAURh-3mo2kNscwsuXlD1scLiBSgd9aV9pXtLdOeqC2MDedx7fOVb_jaEaYAIGo4FAC8wr3AiE3vBlh2mV_zicCjaYSFo8-KDAzDcGGuzGnjcEpeO6dvIt1SWwnOEtmH12joaDeB5MxbmGvAtxHWn0pPzKEWNtEjLp7L5Stg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lz4l-H5NmLqiOBeEgan8F4IJJdLmLI_KOeawCmfz-kNvXBqxGyY3HKtODvkKFDgpI9XPj415V_XsttJgqMSHzzBlNpYkDTIwpJTN8C50vQs795A3cNm55AKXFZ89roYFoMXTSHkodaTDLI4G9oZhdHA--wYVh6d3lbe33mJEPP7YIyNj5z7Njsa9Kzuq2iXlM-3bJThikM9ZBmNWizYi3jwHQC31vRt5ygUkY2y8-VRN82uCl0B26mr0lpLU7ZYPjptqvOW6S8Igie7B2FdLE5YpQSUJrTj4wdvkpqcEZlw5n529CCb7fuvRD9s_73qHyqHbN1rZ_UIFUXKkRTOBAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریستیانو و جورجینا قراره ۱ آگوست با هم ازدواج کنن بالاخره. تبریک به این دو نوگل دیرشکفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101960" target="_blank">📅 07:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101959">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsVtfZrI5dooqwVubSp4sIODVynrC1zxjwsHSLi2Wvc167aIyYhv45jjOxXZVkBGtIJW7GwbyK1x-OmeCXx-goismxjarMtGvDq2gzYTP6Bdb_oSwpyYBM7E1bWzxtTruz49_vEjkXbmDFD0I1G6GmXdIwl-qS5PY-eEIzvXHNtQN4_H0JzxpGjYL-PqSUAeC65YWRoJLAIk3wQHXmSYE8wANDj6aEtTniQqnZqMKoB2WXCSXQ55xILTHUl7kb21DL6jU9HnM33q7uNDs-_4qWpIsiwyebipLRZfueD_xGEQA4KRIJMzYDMbu5bsZ5cK7k2Oo6atU8MmJJzK6HeojQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👑
موندو:
تعجب نکنید ولی احتمالش زیاده که لاپورتا پرونده نقل و انتقالات بارسلونا رو بدون جذب مهاجم ببنده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101959" target="_blank">📅 06:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101958">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85d2fa751b.mp4?token=g3MyyN_xx9ULX_W-ml7LxYsbVUK9IOJUG382jxjI8JHjbuIYqlT91m8U4j4os9eVgzvwkaMX8ZxzlrrC9a9l6NIELi2_jmQH0bSs1sZSuCrI7mBE1Qb91wE2buhOmngL-qKvrQ1-sKTKaHyf4uKH2uHp90z80pHqC-dAU6hBykI1vi2hR9rciA3VvDpgS3Lw6zts6SSZRpgiMy3y7QnFa3lBVq9HQIWAGqsvOzU7p8_W_zLHIiYCr6OMaeLliN2vsaqrSYcTS2ITsmT5DDRiwNCh79iNtd6M5_GNkBsQOSJofcHZDTBCMtdl2KYZAiPNJX-FggGZg5eF64c2BPXPaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85d2fa751b.mp4?token=g3MyyN_xx9ULX_W-ml7LxYsbVUK9IOJUG382jxjI8JHjbuIYqlT91m8U4j4os9eVgzvwkaMX8ZxzlrrC9a9l6NIELi2_jmQH0bSs1sZSuCrI7mBE1Qb91wE2buhOmngL-qKvrQ1-sKTKaHyf4uKH2uHp90z80pHqC-dAU6hBykI1vi2hR9rciA3VvDpgS3Lw6zts6SSZRpgiMy3y7QnFa3lBVq9HQIWAGqsvOzU7p8_W_zLHIiYCr6OMaeLliN2vsaqrSYcTS2ITsmT5DDRiwNCh79iNtd6M5_GNkBsQOSJofcHZDTBCMtdl2KYZAiPNJX-FggGZg5eF64c2BPXPaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
نیمار تو اولین بازیش بعد از جام‌جهانی با دبلش کون سانتوس رو مجددا نجات داد و با نمره 9.4 بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/101958" target="_blank">📅 06:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101955">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HYxFrRAeX0M_Xtzdsvy1dkufLoWLGgx8X1ijIDmbdX71x2ZX7HWneoyDHqbm4p1hBtt0SXca-i7s43AcFdNCF4SQL2P_Hy118rWPFl4oBPMYSK7e_gXS17gZJjeadkpOVvNVGsBRkzN8Tgdkgcl9BPiDAbDtIkArzyzA9F4Z09LEoiqCuOno-3vqW4U383Us9MRviFyDE_lZPIwAwlto3CLzVHwVEiiGayMHwRMbDuz_9IFaWLA642jpsqd1ZCuOEtwsGPgaxrvGke7DSxxXZLxU9seBqE6G6yhdBH9ioJPr8Ird3odG856Nu2OjDPXXkM4y2tGtGoZxIRc7wy1aEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FLCEiRMLP_kG_b--Ig1anjQAGvIKlDNePd4O6JJlxxvwk5BMJ3kNrCp75mzEWDx9o3HtSRxGKnInJYorQFaJbJt0WB91PFYVMdq7Bv_EJKutT1cWaHjHmm5LW4g0q-vXl5iaXFL58Q0jpsMoP_An8UUoYjI563-FUG25XcfIM7MxJEFuVDCjJizXzfYMZaSpYI1JXvjDVvoC1Bfx7mDknRbm2VPvbL9nq_UNDhHIfVLkYN0c3JwmVU31oBE_3Hq_YfhBn8zHU8pz38Xnd-29hg2lN3r_8RBJ3x1OG3le5svZdLhFiMjVOwkQdWdyG21k4YmxGFlobKyE1qyHV8CU6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953a60dfac.mp4?token=sVszyVV3_WBJ0xygVHWe26UHZTf648mD5h8q0VnO_eCF8p9P0P_RjWlu1fGMjMYJrXpauAx4gRvplDVwjeAl3yMZKMHdUKEtuI5IDCuXZRTL0V-f_oXSjYW4g2uyFAU7bnq6AVAkG873bL_ZXkiZsjgRYtP3py07j7lddoX6zUskil0ZIQlAsWF3ElQCF4INXOQlnqKTUwUJnaXkIZq9wUVpBObckVQ_R392VftdfKZyYxA_ySOr0giAYR9FKIpi2VCun5B5QtYpuc8kz56djw4bEoYT6DvfK_S_iShH7zRoWSBCh6HXg4N8XiiC18xGKSbZtLF64VvXJbIZujkXfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953a60dfac.mp4?token=sVszyVV3_WBJ0xygVHWe26UHZTf648mD5h8q0VnO_eCF8p9P0P_RjWlu1fGMjMYJrXpauAx4gRvplDVwjeAl3yMZKMHdUKEtuI5IDCuXZRTL0V-f_oXSjYW4g2uyFAU7bnq6AVAkG873bL_ZXkiZsjgRYtP3py07j7lddoX6zUskil0ZIQlAsWF3ElQCF4INXOQlnqKTUwUJnaXkIZq9wUVpBObckVQ_R392VftdfKZyYxA_ySOr0giAYR9FKIpi2VCun5B5QtYpuc8kz56djw4bEoYT6DvfK_S_iShH7zRoWSBCh6HXg4N8XiiC18xGKSbZtLF64VvXJbIZujkXfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
نیمار تو اولین بازیش بعد از جام‌جهانی با دبلش کون سانتوس رو مجددا نجات داد و با نمره 9.4 بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/101955" target="_blank">📅 06:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101954">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzFo1M7MFwMR-_ed8kbGbPzIoo6b41JJui5Q6A1EgoHOexDRxYYM0lm1jwio-v3ZCZ-XylaDCC4V-d_isdA536Xffo9fyBzO182o-a5A_wEUfV-xdnQg5wiZpVDd21FQOl4Gp87tT6KeyLCO2epGd9mn_M0a1sLFgyJdeF09dBVkiqmv_XRQkMDlMU9LnOobfIvKzpt7SGprBLUUaTB-2gNbIeirf1Dczcf117QxJydMbWUJzGQTMaR8mpo6hwk4W_P14peUCkToUszmu2yzm6u9E9TCQJEhOTzTNZLhwscWElvlv1Py4SAyfMnC1S7DknA0Yn_gzHZc5VLB7MDQXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
مسی امروز اینجوری تو روزاریو شکار شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/101954" target="_blank">📅 01:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101953">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44643cb150.mp4?token=rPSk2LDyZU7yUXjQlSJRAvgx2Y2QwM4fcjW9heVjYj9_MIFvQsoLy8bQftYoitglN2-XdZMqtIng5ey7aQWTuDr5HYv8QjjbOp0d3YygxZ5B_sA-6JedxQ-mpT22x1HSMtBOawHgEwViLzfp15hvnkLRJkDHb6zjp-soUxwCoSEuM2YYRMs5kQ0kv3IgxcXjYVStu7crbVt5Z6xagFvPEIywb3Sm4Q89_0mXLRR4psu24R_M1avBet4IhHNqY5anyjdZXTOt1c5Q2_QMPvlkrMEqbWeSuNKZxUc1inA5RUN7hRMP_7IXU1bZ3PQbv0Tu1Q29eVQpgRxaNlAJ7VAN9LfSxmLgJdf1OwfUxihpX87HqXUiilQj4JxFHnbgyrWDt8qYukHJNgZTy-u2PYDqJgRnZcM2j2TEy27sr3F6MxdElrq9rd7-DHj2VIx0UjHFH5uRLqj9MbNItbCzRED8XAwJm-eMrRyIhFp9-rpSAYEEEPosTpQCggAkvw9uSTgixCu7-3_As1qVuDWW8dASZpaQ6JYPygY1pHKPcikEls7fHx2ltXOv0e1qhKfxaSFnVKWEVRR22MEcn11no0yzaEf1Fy-jNH6m3st3f7_5q1kZ_tkhv2cPSDsF75RXkYBfzVr0gingi3xTB8RvX2g0SEAvhOlZkvXPhUMTdd16tVk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44643cb150.mp4?token=rPSk2LDyZU7yUXjQlSJRAvgx2Y2QwM4fcjW9heVjYj9_MIFvQsoLy8bQftYoitglN2-XdZMqtIng5ey7aQWTuDr5HYv8QjjbOp0d3YygxZ5B_sA-6JedxQ-mpT22x1HSMtBOawHgEwViLzfp15hvnkLRJkDHb6zjp-soUxwCoSEuM2YYRMs5kQ0kv3IgxcXjYVStu7crbVt5Z6xagFvPEIywb3Sm4Q89_0mXLRR4psu24R_M1avBet4IhHNqY5anyjdZXTOt1c5Q2_QMPvlkrMEqbWeSuNKZxUc1inA5RUN7hRMP_7IXU1bZ3PQbv0Tu1Q29eVQpgRxaNlAJ7VAN9LfSxmLgJdf1OwfUxihpX87HqXUiilQj4JxFHnbgyrWDt8qYukHJNgZTy-u2PYDqJgRnZcM2j2TEy27sr3F6MxdElrq9rd7-DHj2VIx0UjHFH5uRLqj9MbNItbCzRED8XAwJm-eMrRyIhFp9-rpSAYEEEPosTpQCggAkvw9uSTgixCu7-3_As1qVuDWW8dASZpaQ6JYPygY1pHKPcikEls7fHx2ltXOv0e1qhKfxaSFnVKWEVRR22MEcn11no0yzaEf1Fy-jNH6m3st3f7_5q1kZ_tkhv2cPSDsF75RXkYBfzVr0gingi3xTB8RvX2g0SEAvhOlZkvXPhUMTdd16tVk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لوکاس هرناندز: «کیلیان، اگه قرار بود یه تتو بزنی، چی انتخاب می‌کردی؟
🔺
کیلیان امباپه:
فکر نمیکنم هیچ‌وقت تتو بزنم. دوست دارم مردم من رو به خاطر کاری که توی زمین انجام دادم به یاد بیارن، نه به خاطر تتوهایی که روی بدنم دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/101953" target="_blank">📅 01:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101952">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ih5tq-GBDlswHd74Ryt9-w682fWdJw6ixvt26cENIlxcKqVdY3P-2IV-ISogKZpxCJ2JUJjsnqtwndO_uE_hHjEgvSfzQes-zE_B3cWNTPCKKCaIBhsn10jJilWkdC40SnrrlDu5MvMtQyyc1xA1d89fJ2IdTKOgq7X6O2f4aeUIOFK4-1YlenTZGV10JIaMkTv1ROLnczy-PQkoUWyZrE3ZSML4wT0AXT58A0Ab-h9Q4QUSk3wj78xl52_6KSLAKZtAtpoZtm-icGjY6rzhY_gKDA064MhpJ5w4EedmnRZL6nkGRBzca7m7vg_hcdIe-PPKAZkVPSAvOzGB1eekTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
امباپه و پارتنرش بانو اکسپوزیتو‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/101952" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101951">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTB7nO-HzLDuXzpRT6Sd0DP0aZ7YlmFrMc-yW2SmI0Bthg2_pZ2wHmF_eG6VzBxznK11WNXif8hfRT1tvFteqXWTTOUW6kxT9ZvbdEdv3kfKLedh-OFpOxFI60VVyZeipZcggt6n4qNinQrj9RzJX3cR4gKTMzGVz1np58M7p6RBa1TElOfWqjh5Tiosj_55PJhDFHqOQxrAqESPHbiJiEDwz54atDC9FqmLApTQfuKLwY4WCG2s4m8b_Cansyd2ruHOJt_GotM2BtN1DE-rz5HkFmQh8Lt_jOoCikQCEm70XlA1G99qmkvWJR3s6s8b-QIWHpZ1r84Lf6TZOKfs3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینی خوشتیپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/101951" target="_blank">📅 00:51 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
