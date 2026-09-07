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
<img src="https://cdn5.telesco.pe/file/VS9ycGDwkyM_LDGem8vnhrOOE_jlRKoWlSvqrL5s9crBUtc3-N1H-8ySSq4148fhEGpNwbvHMVLnC_1szn2mA1JbssfugsO3mb2CPgqS_plD4h6oSqDVO-klBkDNRey1aXTvw5yuANzyF_B0HDPYU825v4W9jnSkSLpYzBQYGJQvIVYas2oMig9nyFIe08Q5nS46tJExidY7wJtlb3nbRkSjRW9X-FwoSpk0FkeQi7UygY3t22kaMe-7XP0ZyjjdM9AAWkYXVbPbTVkRzKifefZUmYEXV50atURcd48OhDXcTlAna_SA5ANxVBmDUULS2GseMjcOHjxRyykyIg2j8w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 424K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 14:07:21</div>
<hr>

<div class="tg-post" id="msg-105790">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7j1rB590KW0zz2ODRRTCdLfEjrpL1un8u_d7NcHsX0Fm5HrANGHqBQz13vZaLK0tGwY5YVNKpJLAYC0ct_e3vo2RXw5MbRHOtdV5ZT71-XaYVEnc6k-kxjKNENtyMiQ2sawZ46BTEvuLnB00wkoF5Qs6dnr-7t5iYuSLVpud5YqLMUkpUD122Mx57e6ZxPQnqNU2DIfO2Uf36T-BQRakhZOseHeUyz6g3ZtXH3zLqBLrk38sZjQaWHHYoZddS0gP6ayxE479QwHSZmFWrt-mRrQGixOScLPWi0vCgbJBfeB9nm-Jn9wDIqbWVOlLvhQnwS7-MHR2-yK-NFdHqJk0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇭🇷
🎼
لیست تیم‌ملی کرواسی برای فیفادی با حضور لوکا مودریچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/Futball180TV/105790" target="_blank">📅 14:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105789">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iY4WNgi4sIDFAE9O4OEJLneMFN7s0UIie-FHjcXa5nAngaZc3twKDM4H7aYvKvJC-2rrcC6m1SsAFNHlCi6nPAhSsvWe22PwautemaeRH-QVdbqiqVEAPWVwXIYpS3whtdJOsTBtz8XwamJ-vJ6LHt9hWGYupITe24fqzfk_pWi9kFj8PLx1g85L_Ix4w2XFljv2FpN2kS3y4YZT505Mbx0Ay0hH9ecS_3fz516GwamHTjEEjCXCpqeG1xmzC3jDdpcYe7ox2z1yzE2EGS3FuTKQHd_WUl2l3H8fzcXAz9jD_02dQbKQmhtr7A328I3F8srCfLlni31S25GjFVUlpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇪🇸
این تنها سومین بار در دوران حرفه‌ای امباپه است که این بازیکن هم موفق‌به گلزنی نمی‌شود  و هم چهار موقعیت گلزنی بزرگ را در یک بازی از دست می‌دهد.
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/Futball180TV/105789" target="_blank">📅 13:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105788">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51d2063588.mp4?token=DAPl5WeuE6O5TlXkOQAgopDsSgyBzpPonUecw12TqYt5eAjnTZn40coDi304q_6kCJl8HpwGueJjbSHZQLYv0CnqP8bCFg9ieKN8rq-3YxZc-lKvBCApt3BXHJ8UqEWOdULKfHa3xCUI4vdq3mwONMwtELY2vre7XNAehDPGdyr8kW7sBSF4TztgY_-v_dHGACVM--QxTLOKevQl478ruJcpp_o3GC2PgH2oikP2_-4G8FlO6jkXlJx0BxK55LvM9zuTTog6-sa_SaNATc2MrzlitirvfLa9sULBWe9ko6YmBQPCboED_fx5EjMhR5ZWzfdCBsQkv2ao7GppfpM6TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51d2063588.mp4?token=DAPl5WeuE6O5TlXkOQAgopDsSgyBzpPonUecw12TqYt5eAjnTZn40coDi304q_6kCJl8HpwGueJjbSHZQLYv0CnqP8bCFg9ieKN8rq-3YxZc-lKvBCApt3BXHJ8UqEWOdULKfHa3xCUI4vdq3mwONMwtELY2vre7XNAehDPGdyr8kW7sBSF4TztgY_-v_dHGACVM--QxTLOKevQl478ruJcpp_o3GC2PgH2oikP2_-4G8FlO6jkXlJx0BxK55LvM9zuTTog6-sa_SaNATc2MrzlitirvfLa9sULBWe9ko6YmBQPCboED_fx5EjMhR5ZWzfdCBsQkv2ao7GppfpM6TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
امین‌رضایی یکی از اساطیر سندروم‌داون در دیدار با علیرضا منصوریان در بغداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/Futball180TV/105788" target="_blank">📅 13:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105787">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/737dc646bf.mp4?token=PLnzUcmKhMWBMwMiAXYrtckTzJp-Qr1kgOL3uJCXbzPKZshE58_qty4MLxONLgRFGaR2sWgHABa2L3VZmElfBVj8surjMrBzOoXCnbjYJ5L2ee0iF_3V79bu2nCZDo8wQ28Ga3pZ99U_Vhn5klvEn6YJZTq5VJxG-2T-ll5ZTSl0lSftkIw50290EHHzJSS4UDqpN29UWTBOn50C_yNbnhuE5NXnNAmV1euwDD_4uSRDOcz8ab6XFAjoHvVUFCpMHn-EDqV4bch6WVMvzuePj_njpwJkrGiLlyTDeTysVaLA9dGjGthao8qsN9xYChROVyvv0-omwWyl15fdggmUQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/737dc646bf.mp4?token=PLnzUcmKhMWBMwMiAXYrtckTzJp-Qr1kgOL3uJCXbzPKZshE58_qty4MLxONLgRFGaR2sWgHABa2L3VZmElfBVj8surjMrBzOoXCnbjYJ5L2ee0iF_3V79bu2nCZDo8wQ28Ga3pZ99U_Vhn5klvEn6YJZTq5VJxG-2T-ll5ZTSl0lSftkIw50290EHHzJSS4UDqpN29UWTBOn50C_yNbnhuE5NXnNAmV1euwDD_4uSRDOcz8ab6XFAjoHvVUFCpMHn-EDqV4bch6WVMvzuePj_njpwJkrGiLlyTDeTysVaLA9dGjGthao8qsN9xYChROVyvv0-omwWyl15fdggmUQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🇮🇷
حمایت جالب هوادار استقلال از امید عالیشاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/Futball180TV/105787" target="_blank">📅 13:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105786">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ca5c3fb8.mp4?token=gbekEcge7Dk7k3WkhaA7srWnjM9Iyg3HI4V4PSxAAAi-6a0b0OgjIS8rKEtyH47ANQG9yxsUO2Da6XDDjv1qWpezXtqOO5Oc1UXNxln6-RhhFGqWdZ3OEBxkUbu6VVYdrjaYZz8mPXa-P6yvm4nKtDkOdrSUFOAXWAB9-D91qtm5067E6ZWXek_BWPyHyjxmL3VkKShOvHHxQjToIB-DQs0ZATCcD1P28OdbjHFzVEtFPXrtE73HOpsnClYGmkx9MzHlgycX_B_B_H3ZRDPNyBe8VOOh-Jt7HyaeWn689-AlXOPIAQmdmwLobk7BXPeG68CJtaM7QYs5y2VwpD5goA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ca5c3fb8.mp4?token=gbekEcge7Dk7k3WkhaA7srWnjM9Iyg3HI4V4PSxAAAi-6a0b0OgjIS8rKEtyH47ANQG9yxsUO2Da6XDDjv1qWpezXtqOO5Oc1UXNxln6-RhhFGqWdZ3OEBxkUbu6VVYdrjaYZz8mPXa-P6yvm4nKtDkOdrSUFOAXWAB9-D91qtm5067E6ZWXek_BWPyHyjxmL3VkKShOvHHxQjToIB-DQs0ZATCcD1P28OdbjHFzVEtFPXrtE73HOpsnClYGmkx9MzHlgycX_B_B_H3ZRDPNyBe8VOOh-Jt7HyaeWn689-AlXOPIAQmdmwLobk7BXPeG68CJtaM7QYs5y2VwpD5goA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوخی سمی همسر دیوید بکام با ظاهر عجیب محصول کشاورزی شوهرش
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/Futball180TV/105786" target="_blank">📅 13:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105785">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4072bbde8.mp4?token=vUf93SBCNoh5c4MkDWPI8skDLwwsPcOChsY-lAbSlZvNzdnGt2fCtVGyRo1mUdhhCN4pC8bWCb79a6Iqkuf8Ubj_TzWl6V9A5eGq1bw_jPm7y4PN_bjk69XfRXknv8U6ET6MGsk-E2ad3UBK-iDgFlm5wn5_s24X0JdFhRgZZfLHDSoMXM1hfaorNVJw6DKggk-NtXLkZMKbHm8ADjSUfbPiqJpGdFvg55yPIieY9HIB-NH5V-4S3NTRCOid9Kh6Kq_Spa8M0oOlUQeWMH3G-tw6f9v38HY2tanXNPyzh1B58-1K-a_tC-QidEtdGiCvN29TsBOG5FdAAiAL8UeKeahcx8a1D-gytwELJMjEir1eU8s09D4dWm6WRNoF8AbgqGIkQY_GAnskQ43qZtaUbr8VhxHuYREUwSh2ClgFoQGS6BBS8dRRlcQLMS8-7Dkt0AMCvisfKRE4AHNwmIQrAFTk5tDv7CctB1N6y1QSUy05mZ_GxZUeVuysjWPdsHNnhwkpPhpGbCzdPv9thsfNkH9X_uFEfR6JvDOjStlJRga4XP9G-xSIfUFRZc2upUsl7Em7lnz-hoK6qZoVpeLrj4i01-Q4XjzkIZOG5CLFpH-o9fO8ar46wzEfLID0ap0P7EPD4WLo2TIdeKwGQjr-AO4wC5J-iXRGvtCynYoyszo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4072bbde8.mp4?token=vUf93SBCNoh5c4MkDWPI8skDLwwsPcOChsY-lAbSlZvNzdnGt2fCtVGyRo1mUdhhCN4pC8bWCb79a6Iqkuf8Ubj_TzWl6V9A5eGq1bw_jPm7y4PN_bjk69XfRXknv8U6ET6MGsk-E2ad3UBK-iDgFlm5wn5_s24X0JdFhRgZZfLHDSoMXM1hfaorNVJw6DKggk-NtXLkZMKbHm8ADjSUfbPiqJpGdFvg55yPIieY9HIB-NH5V-4S3NTRCOid9Kh6Kq_Spa8M0oOlUQeWMH3G-tw6f9v38HY2tanXNPyzh1B58-1K-a_tC-QidEtdGiCvN29TsBOG5FdAAiAL8UeKeahcx8a1D-gytwELJMjEir1eU8s09D4dWm6WRNoF8AbgqGIkQY_GAnskQ43qZtaUbr8VhxHuYREUwSh2ClgFoQGS6BBS8dRRlcQLMS8-7Dkt0AMCvisfKRE4AHNwmIQrAFTk5tDv7CctB1N6y1QSUy05mZ_GxZUeVuysjWPdsHNnhwkpPhpGbCzdPv9thsfNkH9X_uFEfR6JvDOjStlJRga4XP9G-xSIfUFRZc2upUsl7Em7lnz-hoK6qZoVpeLrj4i01-Q4XjzkIZOG5CLFpH-o9fO8ar46wzEfLID0ap0P7EPD4WLo2TIdeKwGQjr-AO4wC5J-iXRGvtCynYoyszo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
فرشید باقری، بازیکن پیکان: خوشحالم در پرسپولیس شاگرد گل‌محمدی و مطهری نشدم. اینکه بعد از جدایی به همه جا زنگ بزنند و من را خراب کنند، حرکت درستی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/Futball180TV/105785" target="_blank">📅 12:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105784">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZataCB-NXxPzs080VhekdxbfOFkR1aT6vQcGGjMSza2KdeB8eeUrMB7FbNdMmZXMhqfWSGKajRGIYiHYWdKdss4xs-8pw1RdHKYzFrMs2hOfuv5WaI7brt688MASbjCpOnz1XPGZUOYiw8pr-hapXCKYCCdx1wKXQ0xdO8YkTFUoiXaVbyBaxMeBnAjYmG1ZoaYOqz3VTaAMB2RcwotU7s5WsPLj9ci5_hoA3iJUJnLCGoT8ihpL8JTqU8j62Qn2de4duQlR69-8egonQQctEYxePXuE6-3SxAywWpGY-R7mW5l1RpYcBbXHeQEJm1dakM04jknS76WQNRkMenHcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
👩‍💻
💡
یه راهنمای فوق‌العاده کاربردی برای دوستانی که با برنامه‌های آفیس سروکار دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/Futball180TV/105784" target="_blank">📅 12:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105783">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4331728b0.mp4?token=dA0KMcRWufHOWHGTYDVYr4B1O8Byeov50Wvj8CugmH9Mukolz061fd9rSgT1epo0_LH0CK_ElLVm0UmYkp1qfJOXnz3r_3XxeqvJCaIQHb2MrQjwbRJBy4UlsLE1u0KijFxhrr7aVWGo_-X1gqVZxBtIvHVjwciqLcf9xzm2OsBzkeNxnROvbj6z4H50FGij99n1EybR4HQ3fft53xuBpAHsv9x2DXg5Lfe6wYi3WN2SRQao6sWLZo9Vl3aDEky2JjRhQv9Nb09ttZjyiGXMlKsCicKKeOL-iB3Uyaz9pKvx2NMA7joP2doofmthma5N5AXnKoWSW_w3zQLx2yqWmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4331728b0.mp4?token=dA0KMcRWufHOWHGTYDVYr4B1O8Byeov50Wvj8CugmH9Mukolz061fd9rSgT1epo0_LH0CK_ElLVm0UmYkp1qfJOXnz3r_3XxeqvJCaIQHb2MrQjwbRJBy4UlsLE1u0KijFxhrr7aVWGo_-X1gqVZxBtIvHVjwciqLcf9xzm2OsBzkeNxnROvbj6z4H50FGij99n1EybR4HQ3fft53xuBpAHsv9x2DXg5Lfe6wYi3WN2SRQao6sWLZo9Vl3aDEky2JjRhQv9Nb09ttZjyiGXMlKsCicKKeOL-iB3Uyaz9pKvx2NMA7joP2doofmthma5N5AXnKoWSW_w3zQLx2yqWmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد آلمانی بعد از شروع فوق‌العاده در لالیگا و ۴ برد متوالی و ۱۷ گل زده: تقرببا بی‌نقص بود، چون هیچی بی‌نقص نیست و همیشه جا برای بهبود هست!
بارسای تقریبا بی‌نقص هانسی فلیک در صدر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/Futball180TV/105783" target="_blank">📅 12:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105782">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105782" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/Futball180TV/105782" target="_blank">📅 12:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105781">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncLzYKXSELUGDffKfePQ7uS-9gglwHsr6K27_SGmIAihJLpwwzrLLjhQfvQUU8cHZyMAn-GF3zNz8OEepQbzfxG3zedK2zB8TygRFXSO6JXZL4KLfMD-j8cs887RTFNKPEIQnhr7Uzq05zhjNCD6CX9VaYYoPzuFQx0owDOiidsgPc0c2Ni2lvcOIe30yzYVRRhrZm-9gVdIb4uR6Wm8z-G2PPJLBj0sDdv5AplC7_WnXbT6joLXgzefc7qlppK2VYkDl0dO_kIzIlpekPkmnOaQH8MwyqqbLMa6qPXJQcXqdc1K_XW4kr0L0lXs_0bPdB8X24lh-aTgdQDa_AxhYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
ذوب‌آهن
🆚
پرسپولیس
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی
به آمار ۲ تیم در در این فصل
ذوب‌آهن: ۵ بازی ۱ برد, ۳ تساوی، ۱ شکست
پرسپولیس: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/Futball180TV/105781" target="_blank">📅 12:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105780">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1732fa7bfa.mp4?token=jH22a_UhXhBYICG4mzaS3WNiFAsXM_H4pITRyQ8mcXlDrvvw4A5RK5xpm6ZtFosTt7_fwFOQv0cG-oZJGnMdp8COV9mFT_bInMw0xgGvwqm-ekHrPqwwUVGpAO9ThCksY-Oob4jIDP3jMcSCNX98fuh3OhP73gHCOg0L7Fok1tXRlONKzLMRIkIunEGR3NTi2MboHFqCLD6KYpJqqEzdW1h0ZCDraGyPbqb8DpFiHUE6eXzTxHSXa136p3fCOIGgTgve3B-K93du9jYvvxtvlyMdl-ugqSsJXPoOrelxKDrJKvGKZF_QbmxnpGZ3S5Gg6WczMrvRTXYMpKOxMnSE2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1732fa7bfa.mp4?token=jH22a_UhXhBYICG4mzaS3WNiFAsXM_H4pITRyQ8mcXlDrvvw4A5RK5xpm6ZtFosTt7_fwFOQv0cG-oZJGnMdp8COV9mFT_bInMw0xgGvwqm-ekHrPqwwUVGpAO9ThCksY-Oob4jIDP3jMcSCNX98fuh3OhP73gHCOg0L7Fok1tXRlONKzLMRIkIunEGR3NTi2MboHFqCLD6KYpJqqEzdW1h0ZCDraGyPbqb8DpFiHUE6eXzTxHSXa136p3fCOIGgTgve3B-K93du9jYvvxtvlyMdl-ugqSsJXPoOrelxKDrJKvGKZF_QbmxnpGZ3S5Gg6WczMrvRTXYMpKOxMnSE2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لندن مطابق سالیان اخیر قرمزه
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/Futball180TV/105780" target="_blank">📅 11:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105779">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be20a40432.mp4?token=VUhdI5ds0ShRbl21JPSRahTtjQqW_y8u6_IYHani-7Q947oYHsUXIdQDuONjLuoZMzC4hfZc1Lq1koYUjB2npoL2BypLJzB1mTljfOIUo2fLynn23N1IjcIg3eevfx40k7vytNkLlw8Pd-J_0L_aWUROk5ED3Xw4Q83Te8ebA3JH4nTorUOjU-ox8oTEkaTT4AozgUlZ82M6EBwafmtuN6yqZ1FN3j15pjFCkRaAKlYaJocHxeWQCWyEjIlsYjH_39xE6oqoaFCWcjPoRxO02HVyov2-JSXUonF0zMaWz-AF3WasepUUOW2fDsKYgcea_4myEbp42is69CV0cTt4mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be20a40432.mp4?token=VUhdI5ds0ShRbl21JPSRahTtjQqW_y8u6_IYHani-7Q947oYHsUXIdQDuONjLuoZMzC4hfZc1Lq1koYUjB2npoL2BypLJzB1mTljfOIUo2fLynn23N1IjcIg3eevfx40k7vytNkLlw8Pd-J_0L_aWUROk5ED3Xw4Q83Te8ebA3JH4nTorUOjU-ox8oTEkaTT4AozgUlZ82M6EBwafmtuN6yqZ1FN3j15pjFCkRaAKlYaJocHxeWQCWyEjIlsYjH_39xE6oqoaFCWcjPoRxO02HVyov2-JSXUonF0zMaWz-AF3WasepUUOW2fDsKYgcea_4myEbp42is69CV0cTt4mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
⚡️
ویدیو بسیار‌کاربردی از بات‌های جذاب تلگرام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/Futball180TV/105779" target="_blank">📅 11:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105778">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/872be66f89.mp4?token=Ygk8AtFl5mEZT1F2TwB9IP31dQlIATQQ7iB0fv9njX_KFkHr9Tr7A0VWPKr0HitpSLOSXoMzNZmoNLyoOJycPQurjzsVy-HjDUd_DuumMS4RyhcqnfWNYzVlqgGMltdP2n7PxHLkjNQANnv8h2fZ-wgixhCe5tLJlkC6C5VIjy4WKXIoJquEo8zUHYmaTkm6DpBPojHPVlNwIR2aYLQ98fWGakdZx0gjiNJng4HVGx18nXdl0-bUivLk8Y1Nbwf0j4DkvcmTETs7QHgoQQeo7cMIML2TuP5Z6x7L553KLCWIXu7jtsOBvQAp3tnKxSwRd1amOqhvZtUUwhaQo7XzNoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/872be66f89.mp4?token=Ygk8AtFl5mEZT1F2TwB9IP31dQlIATQQ7iB0fv9njX_KFkHr9Tr7A0VWPKr0HitpSLOSXoMzNZmoNLyoOJycPQurjzsVy-HjDUd_DuumMS4RyhcqnfWNYzVlqgGMltdP2n7PxHLkjNQANnv8h2fZ-wgixhCe5tLJlkC6C5VIjy4WKXIoJquEo8zUHYmaTkm6DpBPojHPVlNwIR2aYLQ98fWGakdZx0gjiNJng4HVGx18nXdl0-bUivLk8Y1Nbwf0j4DkvcmTETs7QHgoQQeo7cMIML2TuP5Z6x7L553KLCWIXu7jtsOBvQAp3tnKxSwRd1amOqhvZtUUwhaQo7XzNoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
هایلایت‌درخشش دیشب لامین‌یامال برای بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/105778" target="_blank">📅 11:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105777">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQw368piiEKlYeEqlpodWoA46zsH8sJXkAu0p-Lxl-lWn6y62JXl9Cnte5MDc7xs8jC25JzuGDmSnzA1RTSn3i1TejJnOK63n2zOGVBJY-zsUsxTY__MkG8EgwbtCorudKeYCgE8TfT0fmcROnoO5CffQoxTmBkzaKPShw5ywshTVmPiIfux8FmJpEWJRoAZe_oewOMj6QYhKhA282FHGmuzq3vdvnHwGo7V183HcCwXa6VG1pkIEW65RVyw5CxCRo0PdxZEMSUR2O_ZJWKi77utcI1oOu_VhDy84KCPpmvPxNHJCpLj5cneE_pqTzDmi_mZYZqaD1Tf8Am_VMcjpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💸
بالاترین میزان حقوق در بین سرمربیان جهان؛ هانسی‌فلیک بهترین سرمربی فعلی جهان در بین ۱۵ مربی اول لیست قرار نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/105777" target="_blank">📅 10:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105776">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
⭕️
با اعلام سازمان‌لیگ ایران، فصل‌گذشته لیگ‌برتر بدون معرفی قهرمان به پایان رسیده و جامی به استقلال تعلق نمی‌گیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/105776" target="_blank">📅 10:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105775">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e60f25ffc.mp4?token=EiOn1qHGKe7gDZF-E33RPqegWoSVmZwfu0gMxRt-xe45mZLx1R6J1c845yw4-xEEAxjqViHRj990mxjEfnAqdvzSKgbNQHzkArgVyfsDnqDw7-eJanSe-REmlLCnZ0md4dLe34Y3vf2XlBahJIVyMiJm2qufX2p8O65UKZImJW8jiPONvOOmY3DI0jKjvmJ3EU50fjZjMhWlTRHw5WRJc1GcjZT_xuSuVLGGEuZGj3ukGpLWajp98EPQv8CB0JcE9mBkwGKhikkLwRoQc3OUPka_w0z7gWjOtF48wcZ47s5gXYPEgaElnFpC_ClOGgz6oBm9VHSxd3qtPeBc1euRTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e60f25ffc.mp4?token=EiOn1qHGKe7gDZF-E33RPqegWoSVmZwfu0gMxRt-xe45mZLx1R6J1c845yw4-xEEAxjqViHRj990mxjEfnAqdvzSKgbNQHzkArgVyfsDnqDw7-eJanSe-REmlLCnZ0md4dLe34Y3vf2XlBahJIVyMiJm2qufX2p8O65UKZImJW8jiPONvOOmY3DI0jKjvmJ3EU50fjZjMhWlTRHw5WRJc1GcjZT_xuSuVLGGEuZGj3ukGpLWajp98EPQv8CB0JcE9mBkwGKhikkLwRoQc3OUPka_w0z7gWjOtF48wcZ47s5gXYPEgaElnFpC_ClOGgz6oBm9VHSxd3qtPeBc1euRTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😢
🇮🇷
هوادار روشن‌دل تراکتور خطاب به شجاع خلیل‌زاده: به قرآن خیلی جدی میگم راموس ناخن پاته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/105775" target="_blank">📅 10:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105774">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ab9d20b35.mp4?token=TFKbOfpC2Gylnyy9_hkMRPVVhsjh_75SkC_KTybPBzXXWPXSCPDVoOkFFILAbxnHu8jr5mh_Ipe1U2SPnYnsErvIjkwpFA8DbSR-Oo1QzeTW2ekSybxdv22xJc0cNvhApjBRPn2Zh4GC-ZfMTIjztBzZu102BP3gumMsE7Al25NbaJhfBlkYBA4aL_OkAXb2A4rNeDY7mFQrL3beOiEKZpcprcZ0wddglWv-socJkNnNAPCUaKbRHZ8f9_-6F3JaV_R_84Bh4n_yTPBqW3tJ5R-PlcTu6ldZl2X-O8RAZNbZE2A3ZJx6_3zqCrwL6_0rKF36pARw4IzVqh7pZWdTDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ab9d20b35.mp4?token=TFKbOfpC2Gylnyy9_hkMRPVVhsjh_75SkC_KTybPBzXXWPXSCPDVoOkFFILAbxnHu8jr5mh_Ipe1U2SPnYnsErvIjkwpFA8DbSR-Oo1QzeTW2ekSybxdv22xJc0cNvhApjBRPn2Zh4GC-ZfMTIjztBzZu102BP3gumMsE7Al25NbaJhfBlkYBA4aL_OkAXb2A4rNeDY7mFQrL3beOiEKZpcprcZ0wddglWv-socJkNnNAPCUaKbRHZ8f9_-6F3JaV_R_84Bh4n_yTPBqW3tJ5R-PlcTu6ldZl2X-O8RAZNbZE2A3ZJx6_3zqCrwL6_0rKF36pARw4IzVqh7pZWdTDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
کنایه تند رسول مجیدی به فحاشی خداداد عزیزی: والله اینطوریا هم نیست که همه جامعه فحاشی کنن
…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105774" target="_blank">📅 09:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105773">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfbdf6e4f5.mp4?token=D80knjKSa_Wtso7RibQjukHChCz0JXL1OHnPoa2ZlaI-64eq_W4tlxIz20i934hT9iJLfQwDb7btghwp-q19t9pSeC02cOGOMGtUYC9uNURoOFEEGCBPZOzvqU9GzTHiP7bEvlOpag-u5i84KZ7HPNdmu2zfpAC86_tOvSOgTw71wAxBDvXBdt1-75e2GGPPUC4ls9-483M8PJYob5NsJMpR5dHh7NsiV0TXJJnZfiVyOBSMzdys3y_wCtEEW12vT2XPk2UrjegYSxODeZYmNkrK6gR-HlVGCltou_zq9sYco5uu_g2eTWvlAUlQv_y2XOk0O6rTVWPWVcaCAl5sCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfbdf6e4f5.mp4?token=D80knjKSa_Wtso7RibQjukHChCz0JXL1OHnPoa2ZlaI-64eq_W4tlxIz20i934hT9iJLfQwDb7btghwp-q19t9pSeC02cOGOMGtUYC9uNURoOFEEGCBPZOzvqU9GzTHiP7bEvlOpag-u5i84KZ7HPNdmu2zfpAC86_tOvSOgTw71wAxBDvXBdt1-75e2GGPPUC4ls9-483M8PJYob5NsJMpR5dHh7NsiV0TXJJnZfiVyOBSMzdys3y_wCtEEW12vT2XPk2UrjegYSxODeZYmNkrK6gR-HlVGCltou_zq9sYco5uu_g2eTWvlAUlQv_y2XOk0O6rTVWPWVcaCAl5sCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت تماشایی دیشب رودری در بازی بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105773" target="_blank">📅 09:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105772">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6-eLitZcRDaQtlulGUXmcPM2bcn_y7lR2WLmN3TW-h8YVj624jN0hYVl2O4RpfPShOxKFFQeIEu6vDRd2NglHeiRv6iDGbvp0v7QNQlWCwil6Ja9eBZAI5pYniyOj4nyv3raocWyWvBdEhd6-F2Ky7vOezALlHvv3kRuC4XTeh0i4tdtykY2Fx_XaFvgRTwRzLeu0wkTXNR9vo_4MP5yxiscv_DH5RAeFgNM4I1DoUwIvMVBhmGyvaoac0pUjob1GAG87J8uaW5RIvCP0WYR-nx1EF3peHwbQDh8NdTOiS8t3aYZbjejifgFr8vK07YXWqwKK_nCfr0Mk_rvtoeIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/105772" target="_blank">📅 09:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105771">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf5650c1b3.mp4?token=Puyu1tXgmaXrRXJh0VVKaPAj3SV4mrsOlqvdwQgk3hdiOota2X29PO4mCdRESmdAAJAwvbD0PoCGtWKa_DFREgCQa7ofxsMuqfQfcZkqn8OtP8DZ6Xt6TSQDuZOB0EvedVDZ00qrtcdfJwNBTll3KsyjYv_detP_pAlrf8ahL7piP_89T9E3fWKGLq38o90nfqseDx4GHpAUevifP6181zQ1uSU_Gasz2MCYLbsUsK1Yr-QkqeFQaxJrdFaFBS5mI1GA591NXdtDalRxL9zPlEZGk6LZ8DCnJadf8MJMl4yKUxUdIkzpaNqz7IQ5UwAT8n1XgkK301c_E_llN7EV9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf5650c1b3.mp4?token=Puyu1tXgmaXrRXJh0VVKaPAj3SV4mrsOlqvdwQgk3hdiOota2X29PO4mCdRESmdAAJAwvbD0PoCGtWKa_DFREgCQa7ofxsMuqfQfcZkqn8OtP8DZ6Xt6TSQDuZOB0EvedVDZ00qrtcdfJwNBTll3KsyjYv_detP_pAlrf8ahL7piP_89T9E3fWKGLq38o90nfqseDx4GHpAUevifP6181zQ1uSU_Gasz2MCYLbsUsK1Yr-QkqeFQaxJrdFaFBS5mI1GA591NXdtDalRxL9zPlEZGk6LZ8DCnJadf8MJMl4yKUxUdIkzpaNqz7IQ5UwAT8n1XgkK301c_E_llN7EV9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هواداران آرسنال دیشب حسابی از خجالت مورگان راجرز بابت عقد قرارداد با چلسی بجای آرسنال دراومدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105771" target="_blank">📅 09:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105770">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e6028a7c.mp4?token=Ybny9rFkpzWH64EU23fxpPFhG6RmCxmclCkNXcO2xCuahuMSqP0lR_9tStXtr5X8Y9mgVX6p_UlCuWkDkuZe6xJReLmQRlZumxp8X-n7JZZ0XCEvtpgGBgORuZU0az-nq8gjCK8hJgMLGDkOo6bF7e8nC5Y_uolBKgtMBhOwd1rkSVS2cMjHpI-JQncABgyOs3ihzqGm2SXfKAoaqWAtUiZU_8eh3UQxV1A15J_hj3c4agp37F5EkVRgTZfFDC-u5oAu6aE2IoZEWsYhrK4sT7JfJYOhGny80Mk8w8HAg7Bg0rpXALSlmXaCjgZuo1oc_4cS_udhdepiU67Rvy_k3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e6028a7c.mp4?token=Ybny9rFkpzWH64EU23fxpPFhG6RmCxmclCkNXcO2xCuahuMSqP0lR_9tStXtr5X8Y9mgVX6p_UlCuWkDkuZe6xJReLmQRlZumxp8X-n7JZZ0XCEvtpgGBgORuZU0az-nq8gjCK8hJgMLGDkOo6bF7e8nC5Y_uolBKgtMBhOwd1rkSVS2cMjHpI-JQncABgyOs3ihzqGm2SXfKAoaqWAtUiZU_8eh3UQxV1A15J_hj3c4agp37F5EkVRgTZfFDC-u5oAu6aE2IoZEWsYhrK4sT7JfJYOhGny80Mk8w8HAg7Bg0rpXALSlmXaCjgZuo1oc_4cS_udhdepiU67Rvy_k3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمله شدید وحید قلیچ به خداداد عزیزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105770" target="_blank">📅 08:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105769">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105769" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105769" target="_blank">📅 00:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105768">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjJcXfc7PBbsulDmJrr6LLhAPqdV3RDdptwEfT7fkswwWmgINi_H91LezdbQXLt8L_WtrIkoFSY_yzlbzYv2rZ4Lcnz56Zva1Sccuk-uPRIzBXaXSQZMDD-52sRPckGBAStSRxLe2bCkHCfPTfUg3GcLdjlXL_rlXnLH4ZyXhe0n1XxFl7OinNzdpPur9wUhxJR-hv3P5AGbY9UiD76i4mEis3rtJysGPrj9XW9ETputT2sjSr0gPQo-qGwAbAvI7Hw40VFyldfONFFELGBz1mYWZktCj3I-46ej_Lb3eX1zmveopQzt77TI86dX_iDNh53G5ey3br9uUxCWzq3ojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105768" target="_blank">📅 00:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105767">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105767" target="_blank">📅 00:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105766">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e26f7c6c2.mp4?token=rB8-ARWLaKEzQ9KEQY3wm4uKzQ95cspBJennnTLUfPH7N6lL7byZNnH428l9_Ob9xDYcdOXUvpdjg30Nx_trks44SPPma9YRwo6STpQWpVlaARD_u1SVXBc_a0sSc71lFQMBlGOul6ohI8zWsd4_oHMk0p2Xes62QICzFestfRy6rTwO4mqmvrgK87klMfuknJHBXjdlMh34yZPEm3L2f0aDtErVGruBAGHhIP6Nypi6WclLsn7dQrkGfdsB8Iv_m-2n0FnVBvdAwub_MJMq4uGfLw01-pkCxz4SBUrZ8CA9bczJQoVpph2vqjrd6RHyrn4yENa5u1xuamCijC3CqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e26f7c6c2.mp4?token=rB8-ARWLaKEzQ9KEQY3wm4uKzQ95cspBJennnTLUfPH7N6lL7byZNnH428l9_Ob9xDYcdOXUvpdjg30Nx_trks44SPPma9YRwo6STpQWpVlaARD_u1SVXBc_a0sSc71lFQMBlGOul6ohI8zWsd4_oHMk0p2Xes62QICzFestfRy6rTwO4mqmvrgK87klMfuknJHBXjdlMh34yZPEm3L2f0aDtErVGruBAGHhIP6Nypi6WclLsn7dQrkGfdsB8Iv_m-2n0FnVBvdAwub_MJMq4uGfLw01-pkCxz4SBUrZ8CA9bczJQoVpph2vqjrd6RHyrn4yENa5u1xuamCijC3CqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
🇮🇷
🇮🇷
سجده جیمی‌جامپ امشب نقش‌جهان با پرچم استقلال مقابل سیدحسین‌حسینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105766" target="_blank">📅 00:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105765">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Euv0MaNobX4O2MI4wNMG496ZI7d8FsU4eFRfQCdnpd_EauZoQTAl391hRO7Jo8JORCR0oK6n6HA2K1mMOFu3erk75zRdBNhSCk4YzSQDiY1fsBKocfIhpLYyuKePGBohGQGZt7Uc-Fpv3UJX1HZH0GfsHtm7sMpLXwEzDfetrMtrBrbsjNb_kUenxpPu2hTNp5HATIUWw9zpKrRxxkFtq1yaNMJOK_VzCFqtAV0iLD4g_lsXY9I5mBE-7q9CKzdC_Mrhfv-VYF4zd_FALPvCHH7QnDdw5nw-tYmAXUbIvWsun8o3QkOZcyVcJrNj-WRh-PMezRVxt6C8BbSJadI1Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یووه لحظات آخر مساویو زدددد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105765" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105764">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇹
گل‌اول میلان به یوونتوس توسط سیسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105764" target="_blank">📅 00:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105763">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a702f2c4b3.mp4?token=MSaYAnQd4MMZM1GppG_Y8kBRBi3WQQ3OV6vH1Xal_O1t7SwiluPBhJ4Znx-7Q6UrfTE29r9_9CGIubr7x2x4KVJtq_yVqJYi6P3NyWJErPlI4XP7KXF-hmy-xd-nRI4QJ3GOF4jkEQHDKUO69dT6m_a7YRLAvhlkfb1vMFmET9lllmpxtRRMdAV-eYOAqECQVIQyMfPk429PY8k3JsW0-evhPQjKHBr0I0Ujb_Lq6rio5_68Lwf-5qb11k-XO7LIWE3v5qjAu8nY2kVBBo8cLaDzAtVc78aN3ASBQpWBDCPY3MMZ6HobFqnTZshEHEfBBWUMxKtP7vj3lIw3s3GylA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a702f2c4b3.mp4?token=MSaYAnQd4MMZM1GppG_Y8kBRBi3WQQ3OV6vH1Xal_O1t7SwiluPBhJ4Znx-7Q6UrfTE29r9_9CGIubr7x2x4KVJtq_yVqJYi6P3NyWJErPlI4XP7KXF-hmy-xd-nRI4QJ3GOF4jkEQHDKUO69dT6m_a7YRLAvhlkfb1vMFmET9lllmpxtRRMdAV-eYOAqECQVIQyMfPk429PY8k3JsW0-evhPQjKHBr0I0Ujb_Lq6rio5_68Lwf-5qb11k-XO7LIWE3v5qjAu8nY2kVBBo8cLaDzAtVc78aN3ASBQpWBDCPY3MMZ6HobFqnTZshEHEfBBWUMxKtP7vj3lIw3s3GylA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
گل‌اول میلان به یوونتوس توسط سیسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105763" target="_blank">📅 23:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105762">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
پیروز قربانی: من به توافقات قبلی کاری ندارم، خلیفه و گودرزی رو نیم فصل به استقلال نمی‌دم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105762" target="_blank">📅 23:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105761">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02ce7af3d1.mp4?token=uEQ1UDYvyW1ccS5RysolhJrF2IwUd92w81KPtL-X_shVHibgza_iaXK7S2nzEmtLpmox_t6E7berzkmHNheObqG6wPywc57e9k6Y8N7kdK1XR6atRiwHhmN4SnNaWHPfbcvoktAd2kqj8RLZr9sRi4OAlWgqaOVnk2vH6r-tEvyLMnuwoCTwKCa5XnerVFLydqrgEeCqqTndMUVM_1GxMnvVm0obJ_q6bk85Tnq4etYjoZAXNTjy_ud_QnJCBXda0loYCWOz2MHGymFHAuqSHnw3Y6QFyhZVNpysyksHBR5l5PCjIQOkrhSPUtbOe2kxEE5Dt0xGgbvbHkGlfrFmQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02ce7af3d1.mp4?token=uEQ1UDYvyW1ccS5RysolhJrF2IwUd92w81KPtL-X_shVHibgza_iaXK7S2nzEmtLpmox_t6E7berzkmHNheObqG6wPywc57e9k6Y8N7kdK1XR6atRiwHhmN4SnNaWHPfbcvoktAd2kqj8RLZr9sRi4OAlWgqaOVnk2vH6r-tEvyLMnuwoCTwKCa5XnerVFLydqrgEeCqqTndMUVM_1GxMnvVm0obJ_q6bk85Tnq4etYjoZAXNTjy_ud_QnJCBXda0loYCWOz2MHGymFHAuqSHnw3Y6QFyhZVNpysyksHBR5l5PCjIQOkrhSPUtbOe2kxEE5Dt0xGgbvbHkGlfrFmQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
واکنش عارف حاجی‌عیدی به جنجال در بازی با استقلال: والا یه ۱۰ نفر بهم فوش ناموسی دادن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105761" target="_blank">📅 23:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105760">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1098753ac8.mp4?token=nwioSKSdolqezthpb55UEr7iVkUVQH7C2h6wxBnMxazYG_06nPFtRrrfLLQhKzJalci1bSOL-iHBGNUUjLUNxTlDUgVWp1DxGqHPBGy1B9h0BArIGx6f2Q2xSVyDEIWkkNCFqqQU0pGB80SmPq0YaOPTWz_1A1c-OqZHIbHpUk5XIf9IH879_gcQsDPqyM5QFS7YATbIdsDltGcBDjUXApmqVWe3FMxv3KdxsQhxaR4bErc1w2Bf0ez-MChRFA6bjS2sHcfJ5isGAW28xiP5A9VLST2f-6KcXcM_NLyDG9zHhjEQPbYfrTDxQdI6LqyXN3jZft7XlSqRsu4ys-XttA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1098753ac8.mp4?token=nwioSKSdolqezthpb55UEr7iVkUVQH7C2h6wxBnMxazYG_06nPFtRrrfLLQhKzJalci1bSOL-iHBGNUUjLUNxTlDUgVWp1DxGqHPBGy1B9h0BArIGx6f2Q2xSVyDEIWkkNCFqqQU0pGB80SmPq0YaOPTWz_1A1c-OqZHIbHpUk5XIf9IH879_gcQsDPqyM5QFS7YATbIdsDltGcBDjUXApmqVWe3FMxv3KdxsQhxaR4bErc1w2Bf0ez-MChRFA6bjS2sHcfJ5isGAW28xiP5A9VLST2f-6KcXcM_NLyDG9zHhjEQPbYfrTDxQdI6LqyXN3jZft7XlSqRsu4ys-XttA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
واکنش پیروز قربانی به پخش آهنگ "نصرالله معین" در نشست خبری بعد از بازی با استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105760" target="_blank">📅 23:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105759">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‼️
🚨
🇮🇷
🇮🇷
محمد خلیفه: تفاهم‌نامه بین استقلال و آلومینیوم خیلی صددرصد نیست چون ممکن است استقلال مرا نخواهد یا یکسری اتفاقات بیفتد. حتی اگر قرار شد بیرانوند به استقلال بیاید، با او رقابت می‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/105759" target="_blank">📅 22:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105758">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b9ee8002.mp4?token=KhUMfLY8bKZHZ1n-ZD8IuxWKGDos0ZPg5GloZZK0SwTuqkj0mhdS7SkNig2gQCz7ONvo2yHWaPGNLGTMxYORYf9mZ99nAEwtWCr9lqjb8g2nLIxl8Y_qtjA3Tg-hbYgX-xLCpsbws2QMPKdjIePO_C5qsfv-ySyz4W50V9sXMGZPNiQJEfejrV3YN3xAFc8plj3P-qPrSc7NDT28QYsGhd18j5gKTx6A3GFfnrEduMbU2cTQ5dAi-bMuSPL1wcUhp3n2HpJ87GPgr8ltZzlGEpHnlc2j6UOBUMVQ6MoN52H0Te3QVAfX97oHqSjCMOHakEw5tDhgw09BRQJoYUa7VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b9ee8002.mp4?token=KhUMfLY8bKZHZ1n-ZD8IuxWKGDos0ZPg5GloZZK0SwTuqkj0mhdS7SkNig2gQCz7ONvo2yHWaPGNLGTMxYORYf9mZ99nAEwtWCr9lqjb8g2nLIxl8Y_qtjA3Tg-hbYgX-xLCpsbws2QMPKdjIePO_C5qsfv-ySyz4W50V9sXMGZPNiQJEfejrV3YN3xAFc8plj3P-qPrSc7NDT28QYsGhd18j5gKTx6A3GFfnrEduMbU2cTQ5dAi-bMuSPL1wcUhp3n2HpJ87GPgr8ltZzlGEpHnlc2j6UOBUMVQ6MoN52H0Te3QVAfX97oHqSjCMOHakEw5tDhgw09BRQJoYUa7VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
پیروز قربانی: من به توافقات قبلی کاری ندارم، خلیفه و گودرزی رو نیم فصل به استقلال نمی‌دم
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/105758" target="_blank">📅 21:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105757">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNXO46NsH5CMx1xOrEczfxmqmOL73RGARs0y27uXkN9CqUlBtpNU9iNeSMLDIkv8x_nGVUmd2XuthPOvWqz6F2ybD_0HpDs1rMRpfM8Q2EUKxSvEwzEUB3v-UopNHCR2682YGOws3_Kn9801_YIjXwhr8lMXroV3LZajICwfaCRRja2Y7c4uUGADzb5WUktJynsAOMabhDHuXf3u9agSLyeUaITEjDRZzZHfWIVfBJsFBjbGIBr5Z8x0LFDz_tAzJvPnv1cGA7nmUsSAwPFrlWRCtDhZy9yWyFwMT8nZCnPq-A_DVP7QU4A9OR9kVFL0tSBiUtsTDayBshAoazjuUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فکت
؛ آرسنال در ده بازی متوالی لیگ‌برتر مقابل چلسی شکست‌ناپذیر بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/105757" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105756">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
🚨
💙
بیزاتی مربی استقلال: ما هم از نتیجه خوشحال نیستیم. قطعا مشکل گلزنی را حل می‌کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/105756" target="_blank">📅 21:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105754">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d4a38935.mp4?token=L8GlpZ2kW-duBpQsdTprfVM3FFHs9buGOvP0gpC_MAbLAoFFjdya8rlNWoT2SAUlpm9W2myDnoKsj-AQKnUx7AVA7FdaMzY9gB4UK62QFAEpmZfruBrePdY3wdxQ47sPVDwDz4otXOPNi06xFPUm6r-8z55wkgV0zD8Wyu0r4fKZd7Tig61SA45u-MHNu_XmhGkbokyEOYEP3npFMrexUEG-Ss-LHC-_EDVyQOGjEd8-gQAJdErlK_o1ZiHndSQXsWi0CdsUn8VYLJ8mcDPsbgwCrxSqPdxmfMkrcNnM7WCxJJAUOphZ3TIECTzR8ZMBLd2h57sIQiIeJ6F6AIE10g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d4a38935.mp4?token=L8GlpZ2kW-duBpQsdTprfVM3FFHs9buGOvP0gpC_MAbLAoFFjdya8rlNWoT2SAUlpm9W2myDnoKsj-AQKnUx7AVA7FdaMzY9gB4UK62QFAEpmZfruBrePdY3wdxQ47sPVDwDz4otXOPNi06xFPUm6r-8z55wkgV0zD8Wyu0r4fKZd7Tig61SA45u-MHNu_XmhGkbokyEOYEP3npFMrexUEG-Ss-LHC-_EDVyQOGjEd8-gQAJdErlK_o1ZiHndSQXsWi0CdsUn8VYLJ8mcDPsbgwCrxSqPdxmfMkrcNnM7WCxJJAUOphZ3TIECTzR8ZMBLd2h57sIQiIeJ6F6AIE10g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
⭕️
نرخ سوم بنزین به مبلغ 10 هزار تومان تغییر کرد؛ سهمیه اول و دوم بدون تغییر
سخنگوی دولت جمهوری اسلامی: نرخ کارت جایگاه سوخت از بامداد ۱۷ شهریور به ۱۰ هزار تومان افزایش خواهد یافت.
در جلسات کارشناسی اعداد متفاوتی گفته می‌شد اما چون رئیس‌جمهور به مردم قول داده بود همان ۱۰ هزار تومان تعیین شد.
۶۰ لیتر بنزین ۱۵۰۰ تومان و ۵۰ لیتر بنزین ۳۰۰۰ تومان همچنان بدون تغییر ماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/105754" target="_blank">📅 21:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105753">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDB7L1An7lCNMD4kyPhtvF6UpUhArhE7HxO4rlc980HSs54hS7z9wWlCwLTBiclg5_fgLjnF25FITKCjq5otQmMUUNIKRVMyD3IPat5RObl3a5rEms8CekjqrpURYkpoHGGktRVIWGN4wHwZ0A4NM-b3RS93QNCXvIaeK4RrUr1Uc-UCbHzbpEuDnXpFth3yfYS6CzzvsR-HciUcl_Y1YmeojC1oCOGkia-4BwMo5iFDaEpYwTxcKH-rShAweS9-ovH_QBkoC9yqmoPNm_xr4i71tUlRr4mbg4NyCldHu5ldfXmGp2HwthSw-7l0E06w-uTdYiqMU_K2vT5S4RrOGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌ششم‌لیگ‌برتر فوتبال؛ به یاد دوران مساوی‌های متوالی با فرهاد مجیدی؛ استقلال و سهراب در آستانه به صدا در آمدن زنگ خطر قرار گرفتند!
🇮🇷
استقلال
😏
-
😏
آلومینیوم
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/105753" target="_blank">📅 20:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105752">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW08QMxxV-xjOaFcJIHvy7WN6kBE-9L1hscQ-IBdPoeFQcJK0wmp1rBfs2iqXUp2ZwFUGbQBcGLzp6UcQV7_5pLFzWUwD8-kpNyALwiPlH-_SEI6Tzhj5lLpIsR1mwlOzuBfIG8h-XJReOEz-xVmX3rRZPOAKRCit1cYjsVZkYdgF9UivZisLef8dTx9B4XyhrMmuIjF80ef6IZHik1TDwQrB8819IactIGhw85JGp-S48UcLx9nEPMyAUTDJtjFDcG6FriXt2LkwS4Sx2rkv_qSyqsDabpjOwpdwjE6THkwqCHIY4N7b_j_HiiNcVQs2cODwZZctMnZBKYZwxbkLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌ششم‌لیگ‌برتر فوتبال؛ به یاد دوران مساوی‌های متوالی با فرهاد مجیدی؛ استقلال و سهراب در آستانه به صدا در آمدن زنگ خطر قرار گرفتند!
🇮🇷
استقلال
😏
-
😏
آلومینیوم
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105752" target="_blank">📅 20:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105751">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مرحوم ماشاریپوف برای استقلال به زمین اومد</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105751" target="_blank">📅 20:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105750">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مرحوم ماشاریپوف برای استقلال به زمین اومد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105750" target="_blank">📅 20:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105749">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5e1fcdc1.mp4?token=hRcS6gAiyz-2gMSZbEciu8zi0Psq9Yz5cNz0CPkeFOa8MGA4Yffbpz_630p66qEhXKnMPDvbWygrDzfU0yyYnI21bhIO9mmbpSXJtKdjuJP8IfOtilbI2OaHW50_E7zONROAZRkp9ik8EYuxT-EQiZ94sQiKvoLRSlv4I1Wd4UWK77dm6j759DZGHtMyMDHNB6kxQZicAViy3IvLhOow_4cai-73Co03RJOV0W0l4msnn7lSOMZ2LpURNgueN1EMQb30KWt6Syj9A8qHIpxQq8KRQKCAfK_R1iGjbVgG-wCkuP146SSDvcdhTvaP_36v9lPUusUUrZpvOqiSbvPASA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5e1fcdc1.mp4?token=hRcS6gAiyz-2gMSZbEciu8zi0Psq9Yz5cNz0CPkeFOa8MGA4Yffbpz_630p66qEhXKnMPDvbWygrDzfU0yyYnI21bhIO9mmbpSXJtKdjuJP8IfOtilbI2OaHW50_E7zONROAZRkp9ik8EYuxT-EQiZ94sQiKvoLRSlv4I1Wd4UWK77dm6j759DZGHtMyMDHNB6kxQZicAViy3IvLhOow_4cai-73Co03RJOV0W0l4msnn7lSOMZ2LpURNgueN1EMQb30KWt6Syj9A8qHIpxQq8KRQKCAfK_R1iGjbVgG-wCkuP146SSDvcdhTvaP_36v9lPUusUUrZpvOqiSbvPASA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
😆
گزارشگر اراک: محمد خلیفه ما رو یاد جوانی‌های مانوئل نویر میندازه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105749" target="_blank">📅 20:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105748">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d287258445.mp4?token=fClqUjKGRTMdnBiDASaTZZJ14w1tQG3OWVUUwBSB80jTIuvrm9CwcrNtfuWl6fdw9valzdANujYyytDI1I5C048src_99LkgFVmgnd4KGq-Rmn3LT7p1o2zaVzJ_6F1ns0BbA6diBu0GP7NhT25ddh5ZKXzHUgJfCyTD9fK_3kjD_aRncSLlsa_dCo5ZSoSTmcG4jiPfekf1G_DVdhWxLRCfKTy2JAmdyHgALutqFXlQLa5tQW796VcXIHd4PQGmLHnz03RoYdXwgYYLU3MGttZM3ysFhrJYPNLOPkhoCqToEGn7BBcifvSozfaglT1zxX5p68WG95Vypr4SO_PbxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d287258445.mp4?token=fClqUjKGRTMdnBiDASaTZZJ14w1tQG3OWVUUwBSB80jTIuvrm9CwcrNtfuWl6fdw9valzdANujYyytDI1I5C048src_99LkgFVmgnd4KGq-Rmn3LT7p1o2zaVzJ_6F1ns0BbA6diBu0GP7NhT25ddh5ZKXzHUgJfCyTD9fK_3kjD_aRncSLlsa_dCo5ZSoSTmcG4jiPfekf1G_DVdhWxLRCfKTy2JAmdyHgALutqFXlQLa5tQW796VcXIHd4PQGmLHnz03RoYdXwgYYLU3MGttZM3ysFhrJYPNLOPkhoCqToEGn7BBcifvSozfaglT1zxX5p68WG95Vypr4SO_PbxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
استقلال از کوووووون آورد
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105748" target="_blank">📅 20:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105747">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">استقلال داشت سوپرگل میخورد
😐
😐
😐</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105747" target="_blank">📅 20:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105746">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105746" target="_blank">📅 20:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105745">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da0209e41e.mp4?token=sllSOAdWdGdgIYui2qNcyVSnb2WCPLGyKiG51sJbjkLp0_bmhAPK5Kdc2A77BqYo-_3fKdUghPHA8lFoY4AkOg-iR6pH6RfWCZ8kzvxpYm6CnMNPPr0wl-Wqp_J8vT7N1ggUHo9xK-MVmRmZ4w8cgeX4MDkAuxU_tV_X8JDtgg3KgQxU6LQpZCF07t3zbOcNCwoJUGvTKQP9AgFa1tegRPyybEm7HcGhsHNyle9p1rKBh3gh95cO41bA-fxj5BjssYNIBPqCrlb1fYfBPhsjIJcpFNcMojKNVugOY4AXHDJbmKLyXr5ynK98jx5WtUARa8TT6rh6a0SUlWv5ei01Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da0209e41e.mp4?token=sllSOAdWdGdgIYui2qNcyVSnb2WCPLGyKiG51sJbjkLp0_bmhAPK5Kdc2A77BqYo-_3fKdUghPHA8lFoY4AkOg-iR6pH6RfWCZ8kzvxpYm6CnMNPPr0wl-Wqp_J8vT7N1ggUHo9xK-MVmRmZ4w8cgeX4MDkAuxU_tV_X8JDtgg3KgQxU6LQpZCF07t3zbOcNCwoJUGvTKQP9AgFa1tegRPyybEm7HcGhsHNyle9p1rKBh3gh95cO41bA-fxj5BjssYNIBPqCrlb1fYfBPhsjIJcpFNcMojKNVugOY4AXHDJbmKLyXr5ynK98jx5WtUARa8TT6rh6a0SUlWv5ei01Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل‌اول سپاهان به استقلال خوزستان توسط لیموچی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105745" target="_blank">📅 20:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105744">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cb815a8901.mp4?token=Gy6qlOIsf7pbGqib2KwapZpFleulqt3qyRyjU507V0cF0IZ07a575WaZm4nboRX5IqRuaonOm9l110MbB8Sue4JUXQiA59lsQZdhSZTqoudgNOGxwutB1e8WjSKgBLavJEkjCF4YhQzyZiehXf_IFwQJ7tklFTJBA6G_LUWevBkwigONN604XDlXuwVreYQ0XCdSlrqUHNb0GFlhl7yW-uNOH4qqwJYmIXWpvXVrxVkNXMyDjs9QvaVkKcNVHRxzgRumY_mnmJMYytLcBY7CtSOiyuR-Vvz7NftmUMm4NWmC45RfMphdDrIPDGhPDX1q4fU0CQ4nl1-W0wTIw8kfGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cb815a8901.mp4?token=Gy6qlOIsf7pbGqib2KwapZpFleulqt3qyRyjU507V0cF0IZ07a575WaZm4nboRX5IqRuaonOm9l110MbB8Sue4JUXQiA59lsQZdhSZTqoudgNOGxwutB1e8WjSKgBLavJEkjCF4YhQzyZiehXf_IFwQJ7tklFTJBA6G_LUWevBkwigONN604XDlXuwVreYQ0XCdSlrqUHNb0GFlhl7yW-uNOH4qqwJYmIXWpvXVrxVkNXMyDjs9QvaVkKcNVHRxzgRumY_mnmJMYytLcBY7CtSOiyuR-Vvz7NftmUMm4NWmC45RfMphdDrIPDGhPDX1q4fU0CQ4nl1-W0wTIw8kfGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم آرسنال به چلسی توسط مارتین اودگارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105744" target="_blank">📅 20:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105743">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اودگارد گل دوم آرسنال رو زدددددد</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105743" target="_blank">📅 20:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105742">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQF6NiBxa01yP4FgX97lU0CrTx_ITlTOQlkjkrHhRGteE6nRXYhiBiTK1wX8KrHQVUObaxLds6RlanlMDX9lLTwRNXTk0GTa_HvKP4tl4nUElWiwHXm4UvxxaT7N9-_ZslLb-WhL-TMomoXS4kZpe0gvMw9F27Iy3rp_3fbRkzj39Y6TTbldXPibWJ2imoveALJqkGITd7Cggk_GN6PlkUSWFFGwMmksLfTW3wTne2JvLNHwEmNg0OwKZ5_4xDiEtdA3S_88NC3C51hlTamBrX2VAG_80x6psyUC44XqFjbwHzYRckgzhtycCpoBO2oP19KudN6rkk34hEd7deQisw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🌟
مربیانی که بیشترین تعداد پیروزی را در بارسلونا کسب کرده‌اند، پس از انجام 80 بازی در لیگ:
🥇
1- فلیک (63)
🥈
2- انریکه (62)
🥉
3- گواردیولا (61)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105742" target="_blank">📅 20:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105741">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAYGKhLVkgXWaK5qySRmn7UApOiBmBEGAcay7kB3En7Shjtm7Q9jxFBM84_aMXIJAs-R0KMR5WAiZSdcoZZpZcIPThV8HjTSqUrMTaayzcev27iFz2p0i2OJSi7QMCQudyJEiXA1lz2me8b8i72y-RLTvdzo2jBq5171XDd6HnJPkdmxFmlAlKiM-ZW4nrjtkoReLyPkx5qizmuZejQHc9TXlrmvn5vQtNx9IilK2XPh-qy8q2oRx8pM_lv3y867FJxbgjWdHXLUcqHBJxnSD_jpSOFl7lmiKQLnEfy_Pv3bigcSM7tPtABCGtnuG2ydZiPHzHDpjC8bpvC-MCYEUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
هفته‌چهارم
لالیگا| خفاش‌ها اسیر درخشش فرمین و یامال شدند؛ نمایش فوق‌العاده شاگردان فلیک در مستایا
🇪🇸
والنسیا صفر - بارسلونا پنج
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105741" target="_blank">📅 19:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105740">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e47c1a3826.mp4?token=QdmHmIvfUsfmBkfYYTe18_gzr4llyf-e8YtQp2Tx0ALpQVfmVwCFe41jHu5A4zsSn9CfM4UA_EphHVx4w5z91vBfslwnZL9Joax5f9nNG-h3SkKyrbEzHk2tOkEk8PYZ5TGGjZeKVFXc-KUpRhWAt4ZwWJII0IW1n_PLHGv4KTm1pn3jbwyDrDZ1VWiuNuXVs8IhHJn-56ZQYlrGEt3sdDmou_Cz2fLb0xacBRaTV-Ahq2lsm0--w_pd27f1YhiPu-ujuiJTXyn9iQmudWabOfG8iwnNZHpCitLayuSjcIwXjAjk-ZxMqeMlA4AkgKaGnU4WLrvgmHd8if48UkG34QiywPs4lswzChsuh3sFEP68i7OCXbM6anENeY_npyvX8UphwD340ChtMolCxj6yAJJRKnGuHAnJ3EvKrvSFcQEHl2wAbdcUSNnJZJ4SsQUXYmZ_vTJKlpzB5bgoamf02vOp5PWpHrDmLd0iGc6fmb1W5t9hNFpcveD7tKt8-QF2JlgpPPmYjVrNjr_5w_xEOsye3Hie92BZ4Ch0JwADqIvG8D9Lzc0M9ezrgm6itB3S8MmfgbhjWx3BZJ9W04KymLILofsFJnkJnUFkn6-dIedH_OTgzxWW_8Bx5s3uhDKFsUwi1dvgSOXUhCtrI07tAWdtLbJpqkVeUb2k1XGRsiY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e47c1a3826.mp4?token=QdmHmIvfUsfmBkfYYTe18_gzr4llyf-e8YtQp2Tx0ALpQVfmVwCFe41jHu5A4zsSn9CfM4UA_EphHVx4w5z91vBfslwnZL9Joax5f9nNG-h3SkKyrbEzHk2tOkEk8PYZ5TGGjZeKVFXc-KUpRhWAt4ZwWJII0IW1n_PLHGv4KTm1pn3jbwyDrDZ1VWiuNuXVs8IhHJn-56ZQYlrGEt3sdDmou_Cz2fLb0xacBRaTV-Ahq2lsm0--w_pd27f1YhiPu-ujuiJTXyn9iQmudWabOfG8iwnNZHpCitLayuSjcIwXjAjk-ZxMqeMlA4AkgKaGnU4WLrvgmHd8if48UkG34QiywPs4lswzChsuh3sFEP68i7OCXbM6anENeY_npyvX8UphwD340ChtMolCxj6yAJJRKnGuHAnJ3EvKrvSFcQEHl2wAbdcUSNnJZJ4SsQUXYmZ_vTJKlpzB5bgoamf02vOp5PWpHrDmLd0iGc6fmb1W5t9hNFpcveD7tKt8-QF2JlgpPPmYjVrNjr_5w_xEOsye3Hie92BZ4Ch0JwADqIvG8D9Lzc0M9ezrgm6itB3S8MmfgbhjWx3BZJ9W04KymLILofsFJnkJnUFkn6-dIedH_OTgzxWW_8Bx5s3uhDKFsUwi1dvgSOXUhCtrI07tAWdtLbJpqkVeUb2k1XGRsiY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌پنجم بارسلونا به والنسیا توسط لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105740" target="_blank">📅 19:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105739">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBaEvmKnOjt8TazL1hm7ydUoZEMC1uAORIMxuEa6Z7Fh1vCBR8pVu3GeWG7h075tAPToPx4vqJDIapjslP1CZ2cR4XMlH_CrlSAtt6NCSr8tYEBTCVq6qu3Scoq6qtFtzS4bAkWf-K4SMH-PI8tfxbMdGRdc4fHd2VeVg_EPYMAmg4SjikO-sq9Yu1sZ33RteUmRPVOAAiqVIS75oBOtusK_G_rtxfCrtflxLFVbJPsWIhyhzffTFoOMvtA0e6jmVCz1UYeoSXP34_jQDipahE23SpLjyzCoVCYTWFNexogWQBPfuhcKaR0SjknmPoPil7bRM2h3mJ-WIM1bGwkWcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚽️
لامین یامال به صدمین گل یا پاس گل خود با پیراهن باشگاه بارسلونا رسید.
فقط در 19 سالگی!
🤯
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105739" target="_blank">📅 19:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105738">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">لامین‌یامال زدددد</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105738" target="_blank">📅 19:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105737">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بارساااا ۵۵۵۵۵</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105737" target="_blank">📅 19:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105736">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105736" target="_blank">📅 19:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105735">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/db8af8559a.mp4?token=dzltKCYOi7AA-a_Q0RBu2nc5FGAthN59qXCi6d2M_O0bEae-BahtAY7VqZLfDIPxYsV3JL74OH9f1rwebpAas5ExsdExMC2A_jYacOvatrfcI7Y9t0_N8GtMRrNkF0PH9CpTjtd8oK5VSwCxEaeA9LxpfuZM_tVN65YsebJcWJy1bct4SFfyfydRm8rRBtZWxtDSzROhk68Pi9rD09CftMRVRhNENn_BIUyld50YSYt0UCDwEEk-YAoI9MaRv_FEh_5tB14khbciNfRwYcjcIeiQ3tUW048yQF1D5ktaiV3c1mip8-GLJawWgz_qeBoj7SIUTSiCvWyKfOmN0nXIJEQCaU9ZUhO8_COU0W2fAwHCUyJNqmsqVR1d-VX0LvvllCN4gzNVFrQcDGiQGAYEiEgroqmXBE7ZExWc_ypSYz4NOSq1p8Jnu-SrB7iqV4dODe9p9RMRNHcZTLW8E8cp7eQOwrt3lCuxDQeaXjXedXJvwxBx6tjdqmiYkiZu0URPu5OTYrgI0TbPrfhppGlqAAZQ8n_Gy6aoZa9aTJM5NOheaKHn_a9m362qs6a2CBOaVbKEKB6cS7xAgrjXXJpOz0ulNLIqcTCGc-gTtic8VL52OPhEOsjkM6R_EJjlCZ7zFZBSx6kSZxsRYJA0zbJNAgVwJjQ7itgpoyUy_NhlZeY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/db8af8559a.mp4?token=dzltKCYOi7AA-a_Q0RBu2nc5FGAthN59qXCi6d2M_O0bEae-BahtAY7VqZLfDIPxYsV3JL74OH9f1rwebpAas5ExsdExMC2A_jYacOvatrfcI7Y9t0_N8GtMRrNkF0PH9CpTjtd8oK5VSwCxEaeA9LxpfuZM_tVN65YsebJcWJy1bct4SFfyfydRm8rRBtZWxtDSzROhk68Pi9rD09CftMRVRhNENn_BIUyld50YSYt0UCDwEEk-YAoI9MaRv_FEh_5tB14khbciNfRwYcjcIeiQ3tUW048yQF1D5ktaiV3c1mip8-GLJawWgz_qeBoj7SIUTSiCvWyKfOmN0nXIJEQCaU9ZUhO8_COU0W2fAwHCUyJNqmsqVR1d-VX0LvvllCN4gzNVFrQcDGiQGAYEiEgroqmXBE7ZExWc_ypSYz4NOSq1p8Jnu-SrB7iqV4dODe9p9RMRNHcZTLW8E8cp7eQOwrt3lCuxDQeaXjXedXJvwxBx6tjdqmiYkiZu0URPu5OTYrgI0TbPrfhppGlqAAZQ8n_Gy6aoZa9aTJM5NOheaKHn_a9m362qs6a2CBOaVbKEKB6cS7xAgrjXXJpOz0ulNLIqcTCGc-gTtic8VL52OPhEOsjkM6R_EJjlCZ7zFZBSx6kSZxsRYJA0zbJNAgVwJjQ7itgpoyUy_NhlZeY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
گل‌چهارم بارسلونا توسط پدری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105735" target="_blank">📅 19:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105734">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a50ec1141f.mp4?token=YW3mVz_DXBD19EvhUZhG0lApWLxm2maP7EdtnaX-ZfEG2PAKD8PRb-2NttToDYavaEDtGmFZNI0LQ7-TXFz6JEO1cY1R_6dY8PTIsHuPH5VfFwF627LbXj97kqHoZVmXPUux3uviRa2Oud2r6jFl53Knu8PIRqqiyxVLJwqd9uv-o8SG_lMOwRpByFGAnXdrs5_oNzmlDI25PvsyUMFxQQG1HTKo0SyzcN-3p0MhViJCSJx9nFnSqVof1NNCJKldAO2lcwIDQsbrgF-QwIzOz9FKTR83YvQkOGpMJXPZGcSaAIXqLEM-Ux_234AKy7PJLpHYZJrGUyGxbdAdeW0Lgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a50ec1141f.mp4?token=YW3mVz_DXBD19EvhUZhG0lApWLxm2maP7EdtnaX-ZfEG2PAKD8PRb-2NttToDYavaEDtGmFZNI0LQ7-TXFz6JEO1cY1R_6dY8PTIsHuPH5VfFwF627LbXj97kqHoZVmXPUux3uviRa2Oud2r6jFl53Knu8PIRqqiyxVLJwqd9uv-o8SG_lMOwRpByFGAnXdrs5_oNzmlDI25PvsyUMFxQQG1HTKo0SyzcN-3p0MhViJCSJx9nFnSqVof1NNCJKldAO2lcwIDQsbrgF-QwIzOz9FKTR83YvQkOGpMJXPZGcSaAIXqLEM-Ux_234AKy7PJLpHYZJrGUyGxbdAdeW0Lgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا حضرت محمد خلیفه
😐
😐
😐
😐
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105734" target="_blank">📅 19:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105733">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یا حضرت عباس پشمامممم ریختتتتت
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105733" target="_blank">📅 19:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105732">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">محمد خلیفه چه توپی گرفتتتتتت
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105732" target="_blank">📅 19:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105731">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پشمامممممممم
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105731" target="_blank">📅 19:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105730">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89f570dcbd.mp4?token=U9xmNVFzb3gslgwufpzbjP131UVzQhoTWeCsCWkW2xsjR2gvnVXs-BQ6YQSYox8yI5vcMyfBOXVSCeluvxRcaNhsyDwEAVCuijJA8Vv8Vo-stDvW0lvgdXgSTtoOyR2TA_JI7ZaKqrPsJDvXEcijQCjr8USZJQLDjGaGDrTCswVPyyE-6FUwpxjTloxBQf1IF4_e8_9rRDM1s6V9tw-wXm--sLzrWQ7kv1ObgQXlzd2GfBiWi5wwBwlac9Ey8F1-wjbpq7v84dpxfHe29pSRMwkYdmUztSBP1aLZxHbx9kBvYA89KWscWvShNil8iwyAPu5SxmcX2kjc9-32YfB8XbtOlb_ggSYFaQr3adnqLS5theSn9rAEuX4L1JCRofACVPskM6WkdYXR8_1U7Q65Rf4Xgz8QFkNp2H0qXUADemyAs3obTkXphngSLRH3T7dVdEqT22EU-gFiwoxd04fBlfv5X1MJcS6OCf-XIC5YlC9nxG7KkyYLWRA8i3Lufpy3AfvF4UjzmaaRv0j6DjNvj7hcj4UCSp_ovD6C3durMCKMt7xCt8TPNL1HbaIEavoscqANs6pHj8pPAZgLvWQkui1ZwpsKklJY41L9PkjgsfBN2FIfwmE6wkiyki-ENtKyTAI9RLK62SGfx17FXWXRfLTwRZ8015tOcu7yDdtun-o" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89f570dcbd.mp4?token=U9xmNVFzb3gslgwufpzbjP131UVzQhoTWeCsCWkW2xsjR2gvnVXs-BQ6YQSYox8yI5vcMyfBOXVSCeluvxRcaNhsyDwEAVCuijJA8Vv8Vo-stDvW0lvgdXgSTtoOyR2TA_JI7ZaKqrPsJDvXEcijQCjr8USZJQLDjGaGDrTCswVPyyE-6FUwpxjTloxBQf1IF4_e8_9rRDM1s6V9tw-wXm--sLzrWQ7kv1ObgQXlzd2GfBiWi5wwBwlac9Ey8F1-wjbpq7v84dpxfHe29pSRMwkYdmUztSBP1aLZxHbx9kBvYA89KWscWvShNil8iwyAPu5SxmcX2kjc9-32YfB8XbtOlb_ggSYFaQr3adnqLS5theSn9rAEuX4L1JCRofACVPskM6WkdYXR8_1U7Q65Rf4Xgz8QFkNp2H0qXUADemyAs3obTkXphngSLRH3T7dVdEqT22EU-gFiwoxd04fBlfv5X1MJcS6OCf-XIC5YlC9nxG7KkyYLWRA8i3Lufpy3AfvF4UjzmaaRv0j6DjNvj7hcj4UCSp_ovD6C3durMCKMt7xCt8TPNL1HbaIEavoscqANs6pHj8pPAZgLvWQkui1ZwpsKklJY41L9PkjgsfBN2FIfwmE6wkiyki-ENtKyTAI9RLK62SGfx17FXWXRfLTwRZ8015tOcu7yDdtun-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی آرسنال به چلسی توسط هاورتز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105730" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105729">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گل چهارم بارسلونا توسط پدری</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105729" target="_blank">📅 19:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105728">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">هاورتز زددددد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105728" target="_blank">📅 19:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105727">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آرسنال مساویووووو زدددددد</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105727" target="_blank">📅 19:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105726">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/581a696d28.mp4?token=r3Kw9DuVTZGkrjAQfayhmmWQH-ZPkDcl9X4XfWovzJJ2fJEMqEaD3r2y_E39-3jIieg7xG51Z09EhxWVi4FuawK9e11uhd5XRmozgJ9OJuItiV8FGG6Z0_ffodFXMLPSz0QBzyaus903g9XQfX6iBL5ixqMh674PV0DFCNnSJ3sRCe55REbhgMaRDiQfIZWr7sCAt61tcxfyf1NsA86iUoK9C4fMjayMkvLfaL6j_c_Md06vBOLKd6XgyaKZhM_yHdSaYY_-7QTeC-AJQSLav79xuKpY6D87TNdWt7Bp99RjVjsmC1govzpYJsu1xpbggjBd58rjjNfpGxVQz86ixw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/581a696d28.mp4?token=r3Kw9DuVTZGkrjAQfayhmmWQH-ZPkDcl9X4XfWovzJJ2fJEMqEaD3r2y_E39-3jIieg7xG51Z09EhxWVi4FuawK9e11uhd5XRmozgJ9OJuItiV8FGG6Z0_ffodFXMLPSz0QBzyaus903g9XQfX6iBL5ixqMh674PV0DFCNnSJ3sRCe55REbhgMaRDiQfIZWr7sCAt61tcxfyf1NsA86iUoK9C4fMjayMkvLfaL6j_c_Md06vBOLKd6XgyaKZhM_yHdSaYY_-7QTeC-AJQSLav79xuKpY6D87TNdWt7Bp99RjVjsmC1govzpYJsu1xpbggjBd58rjjNfpGxVQz86ixw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول چلسی به آرسنال توسط مورگان راجرز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105726" target="_blank">📅 19:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105725">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31943b0e62.mp4?token=P4rxwHER4xEhi-un2FoznbJuOCpj44w9iEvJyLio6d5aXgjDK00d7PW_kqyepF6v9a7DUo2aCTG9puoVlOvokPoaBT47k2mEi_ED1dfw4HzMiMOmPAa6B0-AqJRgwmygCQ_zzmbJMxc1J2XBT5HR0bbO0SBcuSRkWavcO_ByklUGV1EvYXBDeyANUg5Rmgq0Yic5AeM2PAbkJ1SkdHuGcga8pI09NVtiGLXrV1apnfXeIiAybJaj6TILKolOJ3lOn-gDGcgtwz31bgLdmiH0uSjW2INwdigGjyxnHGuZTghI8Aib5sHebH47X-4M_Alm_nh0Nh542D0q-TRnJyqJCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31943b0e62.mp4?token=P4rxwHER4xEhi-un2FoznbJuOCpj44w9iEvJyLio6d5aXgjDK00d7PW_kqyepF6v9a7DUo2aCTG9puoVlOvokPoaBT47k2mEi_ED1dfw4HzMiMOmPAa6B0-AqJRgwmygCQ_zzmbJMxc1J2XBT5HR0bbO0SBcuSRkWavcO_ByklUGV1EvYXBDeyANUg5Rmgq0Yic5AeM2PAbkJ1SkdHuGcga8pI09NVtiGLXrV1apnfXeIiAybJaj6TILKolOJ3lOn-gDGcgtwz31bgLdmiH0uSjW2INwdigGjyxnHGuZTghI8Aib5sHebH47X-4M_Alm_nh0Nh542D0q-TRnJyqJCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌سوم بارسلونا به والنسیا توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105725" target="_blank">📅 19:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105724">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بارسا هم سومیو زد رافینیا</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105724" target="_blank">📅 19:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105723">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">چلسییییی یکی به آرسنال زدددددد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105723" target="_blank">📅 19:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105722">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXSOUBrSXSNto62txAMnVomM6R_QiLy3SKcLn1W5_f9wRcv5Ti9l7thUIwJFzPdzdi7NUSrtS9r4Z2Re-G-9AFUuD_3FtEycKmETAc59mbt9pMe0cwV4PLlDyS3uP9TlxJtbLnRttC4ESz-dZYC6FfVigC5RDT1NlD4LKg4P-nt-ICkCYrLKb8OhvVzQ0Y1Ii6EnkaYXdowzZ3JL2AwxrkThQu0jUV6viAaNMCi8pat0MI5mhELvbuorK0qN1_3W81ZEnzkhRvsvbbMSET2brchGthZgwIQBl5TW1VZIvpdcJ4HhAU3qYQ5Nz2zWtklzIAdEMjCxxejkqN5cFCpwoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رد ناخن حسین کنعانی‌زادگان روی گردن و گلوی عارف‌آقاسی؛ لامصب چه جوری چنگ انداخته
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105722" target="_blank">📅 18:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105721">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaR-6giyeSEixw78Q2WmenfqReFppO0HQqert961P3Pg_HmPa7oPuX_05qvCO5XKBA7_J523sLOi1OvpEHuB68F3I6N_f55VNC4NtB0OywC5oFfB3izJG_7scnldU1MW5KEkw8GE8EMY0O-Rv7HBqDYDpFfHux78AOu8m5brDWhofk6HPvOmz-xJ0qeY3KgmRVPUN8MO4CuywsS1O7SFQCJzJCHkeYuC-kqgdvsfH0s6CMkgLyMCqXQxwkJIiBaoZfSZoCl52MlWi8hUsUFTYc5nM-GrwIyKVFDNvZ95b4hs4I5LlT_Y1J2pLzzdRm-IcJzo4vgin5XG_rybQw_gBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
اریک‌گارسیا در بازی امروز بارسا بدلیل سر به سر شدن با رودری دچار شکستگی بینی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105721" target="_blank">📅 18:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105720">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LV-uAxUd2uXsrr5Tznu9QjD0UeD6bMkRTTpsEmL-TZxoeeTTCEg2rdnePNGOL2qHWuPQ6zwR8avbHDFJUhCdsuN_8_w2sHg_jKepk_9RHx1XAf7NiuPOVRhdSC8yOp_K571kedhYir8LxJsHbfxzE-sTens3SWWxijdgXQofxL9-YrOufRUMHXI2w76DdoNoKJKbH4tNlUD8UYfVLtkKoFIzTq8Jcd8Ox72SUIP5FQC1DYZ1FKlWVn5ZAcXwWVetwMnJ9LTzfVvvwS7Ua8UCyd-lmsjhbcDXY3BeOeNllj0-YPNqWzVVhHoXYfgBow2GB855W499-ZCSomoDSZNe1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
گل‌اول بارسلونا به والنسیا توسط لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105720" target="_blank">📅 18:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105719">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90fe998947.mp4?token=sbAJ-Dskx7XDXbF-lqBjb6pTPg1zLA119osyGJCD4vHJYky2hFfSuswwZgUaJKmgq4MZ141R6ySjdJCcFS9XBvLpYz7bDc_z0tKJgF2EGPHeUMWLJOOUYqzdpvtInEQ99UuYGDTHxP7sWDSUA6HKuQzt-Mbkwe_M5hCuJ4YFEDId82CZ6_CjBANIoow6mUi41eiuDz58LNV_yvDx1rz6xYmoFnUuuVdTNhCecGPAWIt2LeS4d-1cpIvxnl80TTvtc9eHDdMtoAiV5F99nCf4I2AuF03bhSqvKupC0tA74oeiMmRwRGuj23OtVRiCKQglqgwhQCDPZI_z8lO6rEgnYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90fe998947.mp4?token=sbAJ-Dskx7XDXbF-lqBjb6pTPg1zLA119osyGJCD4vHJYky2hFfSuswwZgUaJKmgq4MZ141R6ySjdJCcFS9XBvLpYz7bDc_z0tKJgF2EGPHeUMWLJOOUYqzdpvtInEQ99UuYGDTHxP7sWDSUA6HKuQzt-Mbkwe_M5hCuJ4YFEDId82CZ6_CjBANIoow6mUi41eiuDz58LNV_yvDx1rz6xYmoFnUuuVdTNhCecGPAWIt2LeS4d-1cpIvxnl80TTvtc9eHDdMtoAiV5F99nCf4I2AuF03bhSqvKupC0tA74oeiMmRwRGuj23OtVRiCKQglqgwhQCDPZI_z8lO6rEgnYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
سوپرگل دیدنی در ثانیه های پایانی؛ گل دوم اورتون به منچستر یونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105719" target="_blank">📅 18:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105718">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e19464327.mp4?token=F0cxblussiwoVjCmBiM5y8SwD-DRwVvx0F3Leflp_sDF_cI9mWl6WZ8P17cqVMr9hn1wc9qC0ZWtvwZmzySU0EIQBX8bAOWdaZIILCejIvigh1xojEMqGGFxJ1pvtupKoQ8OFHFD0M36nGOui91UmX91h7d_jdjEJh_mPbB2gq1fkNOZiEe-sENDlCoeLDCrJ3-k-ZdgFKN0GGFc7tKBHWjBN8t67higN9RSv9gKnRFz_lnknN309DjMKZhP48h_iUShtLpD6xtAxWYgYLgja-QNxIRb9J4JiUFuUvW_TFwkADijkB0MC7ULjUvHtrfCzXJcAvaf-3_MEM8jaOrgkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e19464327.mp4?token=F0cxblussiwoVjCmBiM5y8SwD-DRwVvx0F3Leflp_sDF_cI9mWl6WZ8P17cqVMr9hn1wc9qC0ZWtvwZmzySU0EIQBX8bAOWdaZIILCejIvigh1xojEMqGGFxJ1pvtupKoQ8OFHFD0M36nGOui91UmX91h7d_jdjEJh_mPbB2gq1fkNOZiEe-sENDlCoeLDCrJ3-k-ZdgFKN0GGFc7tKBHWjBN8t67higN9RSv9gKnRFz_lnknN309DjMKZhP48h_iUShtLpD6xtAxWYgYLgja-QNxIRb9J4JiUFuUvW_TFwkADijkB0MC7ULjUvHtrfCzXJcAvaf-3_MEM8jaOrgkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم منچستر یونایتد به اورتون توسط بنجامین ششکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105718" target="_blank">📅 18:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105717">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گل دوم هم یونایتد زدددد</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105717" target="_blank">📅 18:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105716">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4032557f9.mp4?token=PMzAKg0yFlGF2KAl_bCDepZIL2mIUeyaw7suXAAfL3zWrryOeZpURzxCo31VlNGAu-le8oNaidqMa438QwsGKgEtD0-cCSmSv2KPkJGg0nGWGWo2dtBAl1uYNe0Jt2JUyuSGmWW-wjTda7KgRAB9CGGXriSIEaAsUrptKotWBGK2GOY1naJQ0EK8qQZOGr92ac5BCTW3Uopf_JgAm1F_Cb3wmVPiVK6F4rb61Q0LOj9SNCcKxxXOelXyq_KkJ87OYh4orOcr0hZP1nkI8PCPUV8-fV4NgNif75ck6XWnVEIPXtevG4VvF4pdOaBSSRqEFp2PJ0-CBvFu2rgweu1HTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4032557f9.mp4?token=PMzAKg0yFlGF2KAl_bCDepZIL2mIUeyaw7suXAAfL3zWrryOeZpURzxCo31VlNGAu-le8oNaidqMa438QwsGKgEtD0-cCSmSv2KPkJGg0nGWGWo2dtBAl1uYNe0Jt2JUyuSGmWW-wjTda7KgRAB9CGGXriSIEaAsUrptKotWBGK2GOY1naJQ0EK8qQZOGr92ac5BCTW3Uopf_JgAm1F_Cb3wmVPiVK6F4rb61Q0LOj9SNCcKxxXOelXyq_KkJ87OYh4orOcr0hZP1nkI8PCPUV8-fV4NgNif75ck6XWnVEIPXtevG4VvF4pdOaBSSRqEFp2PJ0-CBvFu2rgweu1HTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شلیک به زاویه موافق لامنس؛
گل اول اورتون به منچستر یونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105716" target="_blank">📅 18:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105715">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گلگلگلگلگلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/105715" target="_blank">📅 18:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105714">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گلگلگلگلگلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105714" target="_blank">📅 18:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105713">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پاس گل از آنتونی گوردون
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105713" target="_blank">📅 18:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105712">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بارسااااااا ۲۲۲۲۲۲۲۲۲۲۲</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105712" target="_blank">📅 18:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105711">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">چه گلییییییی زددددددددددد</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105711" target="_blank">📅 18:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105710">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">فرمینننننننن لوپززززززززز</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105710" target="_blank">📅 18:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105709">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105709" target="_blank">📅 18:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105708">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6zWpAndKNw_Ek5vRCUxv9pGSXuVKGvewuplL_6eq4N7TalA8EJFiiYcOaqcDfExGjYlm2SmZn_klnqSWwW4ZnUkGoECvVGyoY8nDlSyXL0avdeBxcCP19QrJdaPrCwiJwmILwg9-TFSpJQQYl8jZFcIMANbm0-FbUDLmSwXUTpwYW8L9cRKHLkJE-eeC2Dl4zWVhMXMCe0S1mOypLXMv_fgaKLKODEVnLaoaQesSiKFlaq_OaYTtzDXeNaXKzB_I77qeGFlbHv9kkK5_ibqFruXq9V3HWAdFJw6i7EY30qDlbPs1KW9bJc4GWYK--pgR9DIIsy62L-q2gkE9wIzjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
گلگلگلگگللگ یامال آفساید شددددد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105708" target="_blank">📅 18:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105707">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgJ-ltggE4N0IrMgAKjxVeUzZzsPQ_76WtXbgxnTbctny8CxQ1FuMCWm0w2N5Q0bB6PCpNx8AcCqVZ-sXC82OsK9Gk-tN89eKIbl4Hw__gb8xO-bk9G31eZYXo-cBA_BldQhBAQZ7h-qX_OMgDO7y5z0eyE7SsX7B9trr49CRnC8Key4joJHG8VjeiajucRgCbhoT48UBHdjU05thl5OD4KA3MLtwKVQpiIwjDzwEzYsuk8o2r1q25N55qqEL6xBn0J2FyTQFWSn2_7lbxPqht0d-AinSIV1rqf4dkbzfURu-9pb_VAUwgoNQud7tuJCki0vHY0nRmUgASuZgIYbyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیب سپاهان مقابل استقلال خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/105707" target="_blank">📅 18:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105706">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/10c1daa423.mp4?token=qbKoNlLSz5_tsLXZYEBvWKGWFTcNpTDaTTxBRw4OQHumaLwC8onoQALhIyvKnXZEv-TwSVRPvD93fYl75-fR2TtpntEK9m0s5NmAfnFUXTatjxjmZbrEuMjIV87ydbARJb-wlbS2bCr0N7cQmqMGHUSo624xGvsa80Nci33o-Qn_PHc6m0rpo9bHs04X6Y_NgNrRjwCqi65dhFsySvyH2MnOqBN0d85dXDBbU0sG1luQKs0EIOq8f4aHOIvtPRl6qTqjqpSpaN8JFgIQpoxcNtiwu3QW_ths-HyQXz-Lwm_q4CTPQAgr-s2_4hF3L_ZycvEs3JC4UYaNd4eNk98zrlfhQkkgWM1L0dYm7Hd-yPTUlsCAS34pO_cHHBi1wBJpCNDqcy_uv_F5BN7yCPBKZM-ds2SYcUfQqbxsOkaFxKK2Z8NeV60tc9XPXffpufYul440mzY_F9Ct177PSgQc-yCadPxsBf3Xt2Ui1sksrlTB92t9Y2c0XJ9jHCAl36c3xiLXugjnYTLv3AENO90c7qfde8YuNsYqUV9mSlPZRxFc06pGys31ahzXY0qxYBXyie_hJxgXrSBZF9tbyqoBPwrSARNRMz9Ru51AanaE0Qg6H2upTcfWrizaf77zAKu153B7pEN2gVjtYcBhQB46fMqN67SQFjubcbr0XXKcJJI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/10c1daa423.mp4?token=qbKoNlLSz5_tsLXZYEBvWKGWFTcNpTDaTTxBRw4OQHumaLwC8onoQALhIyvKnXZEv-TwSVRPvD93fYl75-fR2TtpntEK9m0s5NmAfnFUXTatjxjmZbrEuMjIV87ydbARJb-wlbS2bCr0N7cQmqMGHUSo624xGvsa80Nci33o-Qn_PHc6m0rpo9bHs04X6Y_NgNrRjwCqi65dhFsySvyH2MnOqBN0d85dXDBbU0sG1luQKs0EIOq8f4aHOIvtPRl6qTqjqpSpaN8JFgIQpoxcNtiwu3QW_ths-HyQXz-Lwm_q4CTPQAgr-s2_4hF3L_ZycvEs3JC4UYaNd4eNk98zrlfhQkkgWM1L0dYm7Hd-yPTUlsCAS34pO_cHHBi1wBJpCNDqcy_uv_F5BN7yCPBKZM-ds2SYcUfQqbxsOkaFxKK2Z8NeV60tc9XPXffpufYul440mzY_F9Ct177PSgQc-yCadPxsBf3Xt2Ui1sksrlTB92t9Y2c0XJ9jHCAl36c3xiLXugjnYTLv3AENO90c7qfde8YuNsYqUV9mSlPZRxFc06pGys31ahzXY0qxYBXyie_hJxgXrSBZF9tbyqoBPwrSARNRMz9Ru51AanaE0Qg6H2upTcfWrizaf77zAKu153B7pEN2gVjtYcBhQB46fMqN67SQFjubcbr0XXKcJJI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول بارسلونا به والنسیا توسط لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/105706" target="_blank">📅 18:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105705">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA3knATZqS0xwgdbQhfniHWw7CPPcQTQ7N-NYIFYOl9TKwW7XdMK9WWEfIvfCLgMSVPg7IKPJtiMBl2uAdQFs3-faOxbU87_x5BpFuIUJE-WPPv0gVAFlN7TX-cn_QMS5VxUJGQi12zRos8PYqY1aE62_HIQdQKrwAR6javWo1tffGTiHOcpafgRb4MKhs3p9dy-7F62TXWQdjPUjzMF9EsNAza8kNBjHeL0_WDIJyt1axvjMQKVPaJC5jwfJk8ovvKXGknMhdbaG3BoOIlewncBJP4f_c-b-6lVhIXinbYemnexltgp_Wj1Jwo51F87t-9TschXyLy4TPis-KRc7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اووووووف بارسا چه سوپریههههه
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/105705" target="_blank">📅 17:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105703">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J-Mpm_Np9VLxKyPhaRAg9DQzCOhrfwot8ZPrcG-mEEGJ6YQQD2cpzLE1I5tFM9612lxoj0jZgzb5XdAtx0IFORX5ZhqKtMgDZTrd-4lbIcikrSM7S6gNF-kQVj4W4ns3JGeuzo1Ne4nsvqC6TDB0fyvMeJsDImmcloYUC2bV6EF9UE2MnA-rk2fUpfszEv-4x4TplXTOQVG7NvN_67nQqJa-gT8IJJEmYzP27jALwnCWL12IeIIhebnVMu-DBWf8SSAthVUoBHS3m5M7hmDVLmF54ZEeqc3mlAiQhZwAoB2Hjb-v6lIOglMt5ILiVU6MnoxEKWG1SSUK340ej0YRPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A-BbP90az-alDbvieUbLQXVOnJymrIPf0iegyVbqWVpzIWmzYKmnCQ0SZB6GnSMudMeK3a_kBm4cMSb_b59AGq-nGasL0nN2DyzgfCAlTgmSr4-OCVKz7T8RqNFjhQYQ0ADIzi4g5ERxAPtrqzRGOrShovJJ2F3hfukjOWcjF8Ym9pKmPpEr1I8aaXKX3yWMCqap5T765WnQ-3P92lSoQskr_KlI8z-jBYPUlmw6WNXMfJe8pj8qYaVG5W1eKWlW6fZouIieuWpfeijRA8nLRjOtW8jWpmZ0rdF7llZDALyz7eoiLcQVwnlNPXQrrQYIHh2m_nBPiG7SAlby9G0R9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکییب دو تیم آرسنال x چلسی
ساعت 19:00
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/105703" target="_blank">📅 17:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105702">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اووووووف بارسا چه سوپریههههه
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/105702" target="_blank">📅 17:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105701">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دبلللللللل لامین یاماااااااال
😂
😂
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/105701" target="_blank">📅 17:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105700">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گلگلگلگلگگلگلگلگگل</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/105700" target="_blank">📅 17:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105699">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">چه گلی زد ناموسا
😐
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/105699" target="_blank">📅 17:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105698">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بارساااااااااا دقیقه ۶ اولیوووووو زدددددددد</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105698" target="_blank">📅 17:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105697">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">لامین یاماااااااااللللللللل</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105697" target="_blank">📅 17:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105696">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گلگلگلگلگلگلگگلگلگلگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/105696" target="_blank">📅 17:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105695">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d3e81743b.mp4?token=Ztav_eBUoRg3MmRyUcFpq4LOA6iyDBO6PETee6Hpf91n40AgUeT1jQSYYCYKyUTXFiTqTXykHEVdNbNvTO2IGW-AAQKzWcgpW6ZvP6vqkfNIOpaETi5OX0nFID00iI3ZqBwJGR1tIXiYPjqRbYiRERUrIkvnUNRRb3Fvs_c8uckchnP7Z1wDShPIL3xD4rLq8ku2IgJgVDPjmdFCU_GrCPZZtZzoVlYWOwjXFMW7AfsWN5-Z1Kwcsg_-NrkfBhfr4lj9SN0_9jgycJXfgl78lk0ugOOXdhiRHpePFOZrey5SZhp89tRBjFSvO05VJASL39LRi6NhRLpfFgoggsuDOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d3e81743b.mp4?token=Ztav_eBUoRg3MmRyUcFpq4LOA6iyDBO6PETee6Hpf91n40AgUeT1jQSYYCYKyUTXFiTqTXykHEVdNbNvTO2IGW-AAQKzWcgpW6ZvP6vqkfNIOpaETi5OX0nFID00iI3ZqBwJGR1tIXiYPjqRbYiRERUrIkvnUNRRb3Fvs_c8uckchnP7Z1wDShPIL3xD4rLq8ku2IgJgVDPjmdFCU_GrCPZZtZzoVlYWOwjXFMW7AfsWN5-Z1Kwcsg_-NrkfBhfr4lj9SN0_9jgycJXfgl78lk0ugOOXdhiRHpePFOZrey5SZhp89tRBjFSvO05VJASL39LRi6NhRLpfFgoggsuDOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول منچستر یونایتد به اورتون توسط برایان امبومو با گزارش ابوالفضل عامری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105695" target="_blank">📅 17:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105694">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJL8sg0zZLrN5aTpWuJ6QQqf8hGg1fN6EeEk0BcRfIKlG35EUtrbPo7TWuNaYSm-n-E-rDKuQZnBIQhmXICxYlYe0ZnC_hIeG09wXKtPSpaKmzFl2kl0tdJ74_RbjIFcb0_pWDRBy9gO0k154m1ZEWxuBIks_QvISxBnbkp0HFViJrvYs998iW8zmA-rvJTQmoxkx6SDJHQjf8e8kBqpBZO_3XkJlrsRaZeIP_n_tXYBf_rdvCE6wzDzJDTXsbXv4F84ivduybjPtyDyxngYVcMInPd7LDaOY7VrpeuPs4aGFm1V9E3a58UZA5DMCRGgW-uHeNLh6oecT9YG7Bw0Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
ترکیب استقلال مقابل آلومینیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105694" target="_blank">📅 17:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105693">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">صداوسیما راحت با ۳ دقیقه تاخیر داره بازیو پخش میکنه
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/105693" target="_blank">📅 17:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105692">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">امبومبووووووووو</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/105692" target="_blank">📅 17:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105691">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">منچستریونایتد یکی به اورتون زدددددد</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105691" target="_blank">📅 17:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105690">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گلگلگلگگلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105690" target="_blank">📅 17:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105689">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5PsAStwv0ze-EU8H4ewXIL_AIk2Acizyzf2CRPckbfvwqHZnARnsuDGw8hWhJOgvKHWzJ4UeBlp3Xvuaqanb5Ow7UDm6UUPEEjxSbp3XR3B-KRronLLocDpjajeUFPUMMxawyBDpXzd_vabnrsJDmSguxn8vsXqDHJ98idac1FzT1iXDQH55ErjuIn7qO9GOnZlnd1Y424SjAFqmJA0cV0eN0gM2rasFm-pvCA3ft762ghbGOSlUaoeBeRAIVFf7BAATN05xE9P179htoiS0I05elxB1ep_LsLcTwGLhlD9DZdDE09TGRqNIl5YG6HnK9lvop-gM6mNjXVyMJNnkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
ترکیب آلومینیوم برابر استقلال
محمد خلیفه، امیرمحمد هوشمند، امیر نوری، ابوالفضل قنبری، شروین بزرگ، سیدمهدی مهدوی، سیدمهران موسوی، سعید صادقی، ساسان جعفری‌کیا، عباس کهریزی و امیرحسین امانی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105689" target="_blank">📅 17:31 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
