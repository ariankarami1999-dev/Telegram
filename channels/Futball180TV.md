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
<img src="https://cdn5.telesco.pe/file/DPP5HhYYUGYjyVXrL_7I4Z3Ky7Ov59Ar0OL3a2X0GauUquZ4Kxdq7L7tp3IK-wJfxR0g3ZiHw2OL8Lyb2j646j65fJLOiKpDEFH9bX7BhmWV6lU72bGp03gHg0RZA-oUsv8ZT338Sjj9dhq2tRATaaeG30ym7oVsqvrWiPNdSL5YKq1SHMwkc37Ew7lSVXTgVMYZEOPIDhuhT82pSyHehlsiiTXSxSAYRQlUTg1AVlnn8RJtUJVRcHWrQteDbVuWT4ivknpxD9nnxqDpgWp8BAySCGDojkCsxRzaTrT7WGewZ_xS-Mlise-UGV7HKPQTZvYFQVJyEXoe_rsC6NbsCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 639K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 01:55:57</div>
<hr>

<div class="tg-post" id="msg-98244">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پشمام چی گرفت گلر پاراگوئه</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/98244" target="_blank">📅 01:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98243">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇫🇷
🏆
🇵🇾
بریم سراغ نیمه‌دوم بازی</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/Futball180TV/98243" target="_blank">📅 01:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98241">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MkX1Ug81x9d7PciDJ6BTNu_PuSvUZ3cC_Tr7yS_1e73JVOW4Wl3a0WjyNiEGhQp_e513MowkN2LeuvuqZbPZh6zX5UuFSyeBfIKWSCal75PgOarRCX69XiUD12L2Lsj0HeEy3ymeUHgvLm0ER7a_06oTJXB5Oe4pKXyXM1etkNd5WCAIdDH6JeSeXrgJF4Ue1E7F4bnzcN4GOsVtY_nLUb7Llib4i3wNvyubeE7QUkAuvg28m6_dtc51IaW25ZtP8JljIT_oDh_KVzjl2P3I62xR9ZTeGHhpkUyKgeyWNsvM3QTFealLkwXaQ0Jx3B6vFA-QXNEYd55d3GJfNbcylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YaE6mqdRcKdbre8wdidYib8SR_BrHIO492312UIp3TVU9Xb_C4_0vq_34JVUoNi6i0C3XiFuxwmuze_TZ-EEC5c89ZQS0GL9DP8lFFiqnBH3WiURKNFML0cWnjVOM7MpS22laGSmn-R6zZ1uCd-8REJqxTQGL-Cox8qNnS6XhzQR2bBeqcr2zItTEXg_ycdf36hYMQ-VO7jE6dpgGaKaLgi3LTa6zLpMIzXJ69kkV8TE_53zfOWrjAXegdKL9huHjfku899ze6r1D0XwJZ-VP468XGkj75cDn6kHJv_TPQjJlJuZc2kLN0OxkUtqRSS-pWIdp2pAsbVYYDRCTUOhsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
مراسم سالگرد استقلال کشور آمریکا که در بازی امشب پاراگوئه و فرانسه برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/Futball180TV/98241" target="_blank">📅 01:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98240">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auhXF4FkNPemVB10LZl3UH4rdsoZFFxX-cNtza2vq-VaHiC1lbS338qj5kHb_HOZctrXQDVAuQrPqA9xLkUBc-oBbTT9mcdkMIalZwVojYYerhokKSMAz5__YCJqgZ-jMBqkIWVu66OknI5Ke8Qro0e7N3ZhSZkQv9CmIFh_Nt-ZJRDwDLq_PX2UYoN4au2LAPb1tn2__Wslt5na2wf8u4REp88R4L0bvST5jEncqV3nj1PTqKM2MSp_B-cruAgKbOncnTFee8itquTfva4wvm95eFH2FODmChsCZOb4D1-OTONwLAzXVDqdVuXAWcKlyrzOv4-lzTlztCyqOZaiIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
حرام‌بال پاراگوئه از XG بازی مشخصه.
🇵🇾
: 0.05.
🇫🇷
: 0.15.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/Futball180TV/98240" target="_blank">📅 01:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98239">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پایان نیمه‌اول؛
🇫🇷
فرانسه
😏
😏
پاراگوئه
🇵🇾</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/Futball180TV/98239" target="_blank">📅 01:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98238">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پایان نیمه‌اول؛
🇫🇷
فرانسه
😏
😏
پاراگوئه
🇵🇾</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/Futball180TV/98238" target="_blank">📅 01:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98237">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBxZSg1gsSe7A62v4__tpWjeaRWGoYMgTA13wcuRGd8H4MoZRIM9qkA0hfrIS_b5JTMD4jCG5VPzy2jDOurOV_76lb4keYmcYb5SfbAJdOmDihTv4pBEBcBF3FNlXJsovvk2bz-wAN0Pe5iKN13vvhFoSZlPdgKxvtLPolwL-vrZo7sPYfAM7z8FBgVScXPuAxySVogiZmj1ESH8U0Wv462Geu-s-TVci1d8l-wgaMJbMLgh1LBP4kg4SodM8X40jNkBCjG9GR8yrGD9gRrlG07ZZQr5QiFMUn7IGrOKdLO7YD5lAnK8ltChbw0lDuDKGf2x6wIymYirZmPI-Fw4FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درگیری دیکتاتور با بازیکنای پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/98237" target="_blank">📅 01:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98236">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tbfzw4yk-h9SVyLfaOX759i8Zg6SPz2-frZq3AkP7TJ_xxInDszHnT7PsvqY77xySZ0FXrCq0RmXi7sWu3AYL-5sxQTDACiotPYeaEg3PgE4GINJ9TFfwN8SdI55RMNd9nb0PHprSJvdI8ON6qf5buE1p1ZfYOC1O9mQYTlycnViIZO700VNucE1c-Y6OBDg43HEww6k8Njs4EltiHIF98POAGrNEFwKXeD3RDOh0gwKUwET4nHsCw0-Gag3Y681uzpsNPPGB8rkgi21kYC22VNHNEehB98mLvFDioTN9gQHvPKsyGAwHTEUICbF65_oGbH2BUB4uy7Q7XSONvaDoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرامبال واقعی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/98236" target="_blank">📅 01:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98235">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پاراگوئه اتوبوس پارک کرده</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/98235" target="_blank">📅 00:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98234">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLV2WODLloKgns6GcmtV51s7OodlsbBGV-_cbOyZ2aZJCi75cRlf44cKGAVl55TYDDyAEh8etC8QYuF_8yC9EpVzrYZ8IrJZdhzQViDQx5zhDy16u-o7_gEWvNy3YnMBbyFFnu5Chp2qSCCABrmLLBlgymeLFGKcP916CunODHDw9knEy6mZbPElpqU8oEJ_nGnHHo3A-UYHYqcFQjfCYndqM1DbB61EQi8pJX302zsvz_W6dn6JLQr-tkKHypYaHQLxbf5uzQ6BuOcUXTqOJoKPItRyt2klZD4jc0hz6qaus9sP14J4uLmKRtzewmW6H4JWD5fgfxZo8X6RCif60w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراکش شایسته صعود بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/98234" target="_blank">📅 00:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98233">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/98233" target="_blank">📅 00:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98232">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dmM5vL40pfpXixOUJ3VBOLAhVo5yN-Oev6i1TFMYjEznR2T_d0Oib0MaSqP50OdtQeO2GXdbYKD2zaSEdGZMck-rlAyBJ3Lo5PoYZq3MdfjVkOgR9e1DWIFZMYfrDb4l8BqVEdvVHraldpTyKURhEOLbFb-NAJt8iqbZV64xq7PzFLmcp5c8MaHOnBgqCxk6p4O67gKVu-ktt6TJvirYMLOpZURDC8yKNYBBFg9ZKx7fm-vdryWvgbnwxSC6O7g1IJEhlv2JSRjqOQSoGK3EFHalpjETDEPWHKBbXoQDaRbxBlLnoQQnfLAuV6abHJ1eGJ9lj7eqKMfu_fnlFM5HfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/98232" target="_blank">📅 00:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98231">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بریم سراغ فرانسه و پاراگوئه</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/98231" target="_blank">📅 00:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98229">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/px-sNnHYNQOe7IgeedHFfY9dVvR4WX55yyjb-UwvmdLAGxUykjHLPlZvT1xdmykmuYoDMGJi0VYULSwZBbL4hxeE7uG3rp0uGGhJL_dR1YYJzP2H5Kly2HDWqDmGJWlHIUH62ZTZufCe-va8Pr8WD89qbWd3uPb-DXEwndxjUNcmsuOqK3XMX35L-NTHuyLU6eoVFxBiaTURC88QYtFUqygftOlPBv4dQ0CZuH24G_J2IZvdsmt8-_nMXlyq1YSJ-RkhwBnkbG7bBHeSE3AyBFKpGiZ-B6PWHAkPm6up8yXobWjc8IUel48ilSZBNKCppSncpiaPBc4xHLr5V_NODA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nCOw2NIcp7F4jiOAGjN_BwgylMo1edYhDtzeLOxkmsyKsU59xevZJcnbqCaLnpKmZxkSBFpIBYYXQRySRpnAoFmYx63N92dSEKkTP44PQWxsbEHA9-xx4OFwLiWWoSLlSkZFzSLORjnuoyXn63wEXZkaLDsscW5vESuVbj_qBC4EtglTZqZ1obu1X7DAl3bQb8Feh5K63waW2rh_2ZOUZZ_m-xiB4TBoM0_8auepEyT7TRjIzJRwt9sbXLvbsweezvnTQKOXMY_kCIt2pWGBNDuXSWn4inP4uAayE7l0raSymDndpVDPl6IxbPsct4RaOPs-cq6Zs8msAVhG7iJIFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مراسمی قبل از شروع مسابقه به مناسبت سالگرد استقلال آمریکا‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/98229" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98228">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGi_3QVkHeLiOLng1USQ47LhoZowRSfePKKyzu8vEcckbpBx0Lo6xOILk4tf3R-FFYDa3IJFJsrHzQhIoIWyCDEvKgG54NdISvHU_G8dCGIA9P2j1kh8-VkKJvcDeH0H7AR5boygucp-q2c4Qobmj4cozhRZORVHqJ_29hhuy8RYHlk4fy8qnqJemy51lvULiK_kTbeMz7IGE_-_YEUDHVU9phXde0cDqNueBEYlrOtLhrH5PmW52rMK8JU1SiK8h0FsyDuINAv0g8uRcB_Dv92Yc4FfugYVv2ukJ48WE0nMoSFUPz6nWLKYSMZWVYu__goK7BvBELnxoEAkvpU4Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلاتان امشب با این استایل رفته برنامه فاکس اسپورت؛ کارگردان لاشیم یه دیس قوی بهش داده و تو زیر‌نویس برنامه نوشته: زلاتان ابراهیموویچ - 0 گل زده در جام جهانی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/98228" target="_blank">📅 00:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98227">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTm7_jzuwx9uPZavbVSfYRPWlwsijsOW0sAflhoRig15xTM0H1u767UTOFzKATzRGUWolg-ZBQpkAkkYciskxX8oVnqk-O0NJwNr-QBAm5tO871BXcpJoOSus9GsXb8VGbcIWe9j9EnBJz2CTBNfTupxQHdtfYEcdhSxYMmlRwPW5iHN72fs1qlWSN6sb0pD_AF8W_KOaLK77fJYbRgDOtznwlt0ES0ymlLRUrTLA6TvebKg9d-g77_sB5xFvAsBsBhtTleqN5Ab-W43c3SfYPk9-v4tstdYakTNXJF9xohb0As8Qx0cNI2vEZIpfIU1rILmDY35dxGCShQI3QwGvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دماسنج‌های داخل استادیوم محل بازی فرانسه و پاراگوئه عدد 140 درجه فارنهایت رو نشون میدن که معادل 60 درجه سانتی‌گراده!
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/98227" target="_blank">📅 00:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98226">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYLIO2-8u_sPGiG9KarkZsHvVG0m9pv3V5-zav_qbVfNWLFsFLxVm4o5L3KCdLjGbr7fo2xeJY5vYEIf8BiaHXRbiPtabv2tuLXnCalUTLWhoeqTzHJVlm83uvU28-2_WFzUFSHTI4lK4axnCNqyrJRWsEGN2lgO8T9w2nrf2Xj2xi9nWGHSJzxXy9IdKq4c76ZdJW1djxIFCAY5ykrgf8NAgBy1nwaQ9xgeN2PZT70kyuwi5wH8H-HGTU4jT8mK7zFK6F-Z3WI-FEDBfL2D1mwbYwIulRdIVBIFThj2XXhND1wfxwyw09K1E0Br_AKB8PAiO1H2J-_Fo9ec4jDVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دماسنج‌های داخل استادیوم محل بازی فرانسه و پاراگوئه عدد 140 درجه فارنهایت رو نشون میدن که معادل 60 درجه سانتی‌گراده!
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/98226" target="_blank">📅 23:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98224">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAQK3u5HUxniqGJSw7HCmToLfP0W3bzPH64lL0ADVNSMoMS4gr8sqokHWXx3tdcRIt768Aepc3KvYnPgQS_7_fA8LZfeq9baXPxvoRosPeKEUI9-Pc0EDHzQNuuTqI46LU9PEKRk9WcdK2Fo8ls4Jpm4AhvEaUxxceW0miMuAYpxv5486II8eLXyoQJxeS-Bt-e4a_nUz3U7Akd9pFegsFbgowWkRO9d_uLucr7G1tHSjIEpCx5-TtG23DlqH_7SdyCMA5epqKmAswSNeGU8SqYT3E0GBVtM9VlKJLtP8yB3a1Xe4XIkta62w34BKbn_O0WWM6yGQpWGiW7QRUeRZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه به این شکل وارد استادیوم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98224" target="_blank">📅 23:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98222">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qdtnKQe6FL3oGEByMDJ3tRwClpJJIdfcL1Chy8YN68ICfRTloG70obCJOxvCq0KOO3aEr5xm855ymYzW7J5MtAx9ufhsnipvwmlDU0c_flcio3OYr2Z5otFhnrfLZomZAo5vlXBTuSyUe_J1_GB1nPNzh6wZaC_PxbiLOA4tcdslv0ri-Uo2hFt8YEKvoW_Zl7JVthk9CsRyMG65jHBWuai8RYRtpYOclv9v96maFr7s-ArCCufh7oj8skwPHBxyjp_GrRjIvhhcRdzmQrjraJHNso8coASU-VnSaWHc6bpuR2kQNzWCHcBCQrYlradrbe06UJ5YTKWX90IVrGlB5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AKiEVTVaZmGAqGfsRtcZj870iOU1uw6o5OIqj966hXD5BhNQoqwcguU9zWwL6P9isYN0qrCV5v6RgIaWUJ1-pmzUDY2FXL_uOhxx-8lQGSv1_stEKQ9mvP7vT_zNSRLMwCYWgWl7FtajBr4HYekhlIVpf49QvyIgQEofQJgVbKuS-YZ_SB9EyoHMHV4t_1gKnQE7QPVO2pg6wvzQhMQGEK6zDeajckt79GYWWFrrtP64-S3ceRjCdZv-RFRHCDIgjMgn4K3fHpDoQHA9q49a7TUe9MS-_b4j8Sqb0njTwL9zbowPzYu-CBdslcBp4boxaiY9bX59coC9cpqAorhlKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇵🇾
🇫🇷
ترکیب دو تیم فرانسه و پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/98222" target="_blank">📅 23:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98221">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvvTKNtPUQVtHfyPnG1XPcm3eBz9GMla3HEWl7u8WLfWpG8ytzsakjPDnZ3MzDHAl02Sj-mhbJcHOv5ZbmOTMqDPvjuufz1UXrbeonPI-Sipoegam_qkI7OcxNA9tqGuplbl8wP0kp51UBa0IuR4rS1FJL8d4a5VoSsrr4cJ5ejyJDdNCAE6zYayGie2wikkGQHx62L61-qaGVMHqnGdJUdEJXKAyHJM2UXib1FO-hVGKcVk3TmoCyxo0iYdDGW4H6YsRoNKd7SFExYUKabcTms1-jddZH55zM6ykV5Vo8haWmBHtNjcYx6e1PuX-sIgwo8GomoEkId_xBxCKkqHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🏆
اشرف حکیمی با ۳ پاس گل و ایجاد ۱۵ موقعیت، بیشترین تعداد پاس گل و موقعیت ایجاد شده را در بین تمام مدافعان در جام جهانی تا به امروز داشته است.
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/98221" target="_blank">📅 23:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98220">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwVlw3nzi9040asIQeOOJqXBNATIXBndOCHAmBPgRZBNfk6AAPrWIiTCOJLNxECpPJj5SoK8ZGb6BqJhIslWqhPjxvbsxcterPGuN2TNbxgE0vFGuLzcxzNjPJnO_AICQ2RUS1i-GxvIdATo92JrxrXkxFsVuiP0xyZY-6eNvK_WziUe2hdjrv6YwMkSS0EAXULla0wCS8DNvGb_JuYFfgX4smjEulKzWXU5_lt29Qz3CQIPIbCW6Jp8lQCJ9SC7k3qFWcCRd4N555fR1BlQIlx89bU_XMV5uT7OzI_X8t-n9-6jFuqnNuwPZl5bzNDKhZgHmEbIMnqME-5EHQSBTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بردن مراکش کار هر تیمی نیست.
😏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/98220" target="_blank">📅 22:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98219">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYjUdw-rTAieu-jA50wYl0D-jiltbAbkn8srEhdaZibN1VsR45mS9rV_aF3GeKreXr3U3khVpF5qoVrNhJMTI81cpKcjPnQrONu61MA1pien05KJ0TjBaKx5F-XP_2yyQW9q2OSnmo9Ai59YhCpoiudRGuebC0Da9pcUpTK8IbIQLZc6YN7eb2VTuJwSUWz3d6EjhTA8BMJzS5_tQSQ-TQf9ZGpI_oHNwj7r79E_NQgzxmQTFhxIc69ha7jShX_tw7o9RYa5Z6Rg3epQz8q7h_B0gIbn8VMVqJTzNqgJMnEQ8jy6t9banJejgKdmLvMsH5eS6anOAgQPYI1Cx-kAUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
یاسین بونو، نخستین دروازه‌بان عرب در تاریخ جام جهانی است که در 5 بازی متوالی دروازه‌اش را بسته نگه داشته است.
‏
🧤
بدون گل مقابل کرواسی
‏
🧤
بدون گل مقابل اسپانیا
‏
🧤
بدون گل مقابل پرتغال
‏
🧤
بدون گل مقابل اسکاتلند
‏
🧤
بدون گل مقابل کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/98219" target="_blank">📅 22:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98218">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
📊
|| بیشترین پاس‌گل در جام جهانی 2026:  ‏5 پاس گل -
🇫🇷
مایکل اولیسه ‏4 پاس گل -
🇧🇷
برونو گیمارش ‏4 پاس گل —
🇲🇦
براهیم دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/98218" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98217">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTcZAw9fWkrjgdjsjBGf2MhjYXy4vwVBXdaxTuZrLVWizmSM-GpnkKmuHetHwAuKYssBU98X5XuKGHgl4AgG4cLxHgIvFFPI9U0qbD_OoGHnjZ0pMOGQy-VEasISIByLk63-gNJ0wWBwkeC-42PiSnuME2p85h4KH2SG8_p9LFbSffZc5v51UkYg_7QRvY6TnmUJzQYvhjAQbet71q-ZMRRX-4kfrD7TSQr4cDmp3mcQxEsvNVDGb3WrcaHl96oQpVtBkwwFUaW3n8iRrRDXbsUXvOCGMG_4dFTEArQWQh7jrRvUbjTkDR2BehAMW8JbMBBnRxdILf6M7AIo6VEUeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
عزالدین اوناحی:
ما تمام تلاش خود را برای رسیدن به مرحله یک‌چهارم نهایی انجام دادیم. هواداران مراکشی در اینجا اقلیت بودند، اما به ما قدرت دادند. این پیروزی را به کشورم تقدیم میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/98217" target="_blank">📅 22:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98216">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVs5bR-uSZr8stoyTf2z5SSXqeOGvSn6kezZeRcOWcDfh2FR6kDBguBUZyerG1trWnuNQgHms0JB7wa6HzbvUdfGrO4OshuAYyPVw3mPuka_xxCqV-MntT9sVl0WzEuAZBMkl0XVfgfMu1sIVe_1l54j9m4Sw3CJkWGWEreOpfPx5T0lW8PcJwQcom4_JrAsEAhQ7_r0_onPJCNP6EEOntuDE7iiHGMtHvYJYHJlQV1KIQHulq6FtAYIvYBo7fCNp1uVI24QU_qoQ35hYAimHqd-SZhf3Nj7Jt8e2aOGF8Cs8sU94lTxMF5QIk6IDUtOdm4FwvwDenD1I_6WriOhoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
|
| بیشترین پاس‌گل در جام جهانی 2026:
‏5 پاس گل -
🇫🇷
مایکل اولیسه
‏4 پاس گل -
🇧🇷
برونو گیمارش
‏4 پاس گل —
🇲🇦
براهیم دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/98216" target="_blank">📅 22:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98215">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsTuVSSBMVRB7GolJtua6U7gfbc69gSjeOStOObPC9TBhNd2z9BvO_nUf_eUbABGRaH1CjXctKQihUHKbf5DnjvhPha3dDoq_zB_Dds_y632RFkV7APmULVVmwDTqc5wqAkRECW3dWEpDOMvgMyx8Hh5AujrGAmgNfZzx4z39o5o1A6Imb-2-pKSITvieaU8vHd3O_h1x9_v5drkIU2c2Q3QoNQvNSJFUOMpHBSRxtBwHb0fbjPnrZtl6-E-0EQR2VhU-3XUeY5CLILZ-ZOI6ee0QzhFRY1ohc1MPoQ_dG5Hx8O00uZ0b2dTPCEiPpp0yXNjwOwaP7twwA0VThJnIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بیشترین تعداد گل‌های زده توسط تیم‌های عربی در جام جهانی:
30 گل —
🇲🇦
مراکش
💎
18 گل —
🇩🇿
الجزایر
16 گل —
🇹🇳
تونس
16 گل —
🇸🇦
عربستان سعودی
11 گل —
🇪🇬
مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/98215" target="_blank">📅 22:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98214">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iG_nOxxOW1jXC76gyMClkuwOcBbvF5fH8_mkhzjFSTpDz3d-1TNQGSkq8TMo6zuzVwKwiNQQT4D842xbiQ0dLR_U0N4DIBjoSGlo0QN-8LgwWMipq5Q4Nqy2AcAWf3Rh46a9uIknWYNCS1kkmQaIFigmyFP-_ScARSny3tD46Qx_XvOjctX241pSKLqeMrduJG9ESkIYHkZLl9HWXZlUYE26JvkYjUfBp_QuneVxw7AXYNM4HOAaEookglDHbcfbENMVlIEKsUglKoqX8FkP2htxF82VVapLAcjHtjpsLlAX3vhtN451bVoPuf7dtsVpMHcOvUs8mpe3Dhc_SRB-qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
تیم ملی مراکش، نخستین تیم آفریقایی و عربی در تاریخ است که در دو دوره مختلف از جام جهانی، به مرحله یک‌چهارم نهایی صعود کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/98214" target="_blank">📅 22:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98213">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHjV4lWF3yym1aMZD_OCMGqI_O4xVS1W7LEzVvr9i2c0MQ_hi4WTrWzuamQXLxWckcZMTNPyNDd-JxvIttqcVM8VqCKgMAmvuZTLJepJj5jcHbUi7NW4xs0Nu6iGkx40sFZvqSFf24cAGnn-f9_ViSJwS9j4LaHSBXBqltPiDqw7gfVw3WD7Hlo1o2WUV3AI4h-Ssiw6Qfi2CUxlD28l7a8VmAcDooTl3DMwwa-KwtuLr8q5L-u45Wcz4Sp3brmcMTSyYlmM0Nb5frkHsRt1weu2xIGrOqDV66HD6TPGD52e0GYPdpISMwbjTAajpCvPdHBEs4VyWncVxptmee67uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
عزالدین اوناهی مقابل کانادا:
۲ گل
۱ موقعیت عالی ایجاد شده
۱ پاس کلیدی
۲ شوت
۲/۳ دریبل موفق
۳ مشارکت دفاعی
۳ دفع توپ
۶/۱۰ دوئل زمینی برنده شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/98213" target="_blank">📅 22:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98212">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود مقتدرانه مراکش؛ شیرهای اطلس همچنان در مسیر تاریخ‌سازی!
🇲🇦
مراکش
😆
-
😏
کانادا
🇨🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/98212" target="_blank">📅 22:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98211">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEvEXDMVh9vQCp8WyUhJ_-ECCYqE3AGRlAxNnFSVcXIOaOuv1SZpEz6S_NJN42N7j6P0BVJVl4BzO_0mWPjnGyzBOMsDgJRaLepz6BGT26GmNvk1pRv5jN5fENyaHfwonk-7HsWDkhV8Uc-GYsHlcr24RtXy8Zu33App5X0ynDplNg_C0GMZojJ0c_rZagJwKsZV5rXRABv6oIVEyZpHMZ_zqR_6gApn68AwUsi2YpRvIecOoe75L-4SyPEvX_hwHSM640BGJ3iZwbXgBukxktd1Uc4POmp271QcGI8sGHeWJMz1NM5bg71FcR4HOd22PM7D7c0vDk-Ig7tE6lTN4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود مقتدرانه مراکش؛ شیرهای اطلس همچنان در مسیر تاریخ‌سازی!
🇲🇦
مراکش
😆
-
😏
کانادا
🇨🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/98211" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98210">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d14181bcb.mp4?token=CQJf2EBjhezzLFePji_GOfRP4coU9xCWVK-kz_u2ytg92kCwKON7AFEnOv3OL17azAhe1ECw8ON5ChZQPajcu3AkAsLgQMoiWvc-FZQFols_CMLRv2WAqiAJeBwzuTlVUcgJ7cqc00QYLACKO5A5K-fp7ODQ1sQ1IN77yBru23eKlsPY7ypM2IyuOvhejbU8lYTJcNy77UnHWoCL8LTC-yKMfjHK2xB2xt9jqXbxyMgTZFyL0-5ZlcCSs6sfIo7IINTZmMOMSrjpq9AaIez-ZwXUzXxotkcSeLdpNCP89x0VSP8pZowQag-bG5GHUsBXKMrNIoqpw6O3_QGXoVrOVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d14181bcb.mp4?token=CQJf2EBjhezzLFePji_GOfRP4coU9xCWVK-kz_u2ytg92kCwKON7AFEnOv3OL17azAhe1ECw8ON5ChZQPajcu3AkAsLgQMoiWvc-FZQFols_CMLRv2WAqiAJeBwzuTlVUcgJ7cqc00QYLACKO5A5K-fp7ODQ1sQ1IN77yBru23eKlsPY7ypM2IyuOvhejbU8lYTJcNy77UnHWoCL8LTC-yKMfjHK2xB2xt9jqXbxyMgTZFyL0-5ZlcCSs6sfIo7IINTZmMOMSrjpq9AaIez-ZwXUzXxotkcSeLdpNCP89x0VSP8pZowQag-bG5GHUsBXKMrNIoqpw6O3_QGXoVrOVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
گل سوم مراکش توسط صوفیان رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/98210" target="_blank">📅 22:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98209">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گلللللللللللل سوم مراکشش صوفیان رحیمیی</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/98209" target="_blank">📅 22:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98208">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYYX4WM-zngWxgEC9hgbnMryHZ6OmcshBRRCS2yuDotjiUaufnXZATSfLnjs8_Jw5-gJWX0uEjwLiiefIOJttfRVo-hmo55C9mlEoTi9hjtFovR_rPtOwf9lCgSwBRv-nkfcDtDdwjJQjXzfb03yHJymmm69Vr-Behar3cymaeD--2cTHWCs_pgV7bqwnXHhaxYR6TFrmr6-hkmojcFn86B9Dj4Dgw8-eDXZL2IwcEII3C4DDGoQuqTGzXGyU8amxVsnty5ut59kLgELaHE4AvuZA6jIfd2a3fbq0tQnYFrPatbSRBjEZrxaghMm2CpRpjG9ekY7FH6wOfiKQCzqYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانوان عزیز مراکشی خوشحالن منم خوشحالم
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/98208" target="_blank">📅 22:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98207">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9a15c420ea.mp4?token=MpG2cjHjL1H0q8uApLXd4EXHMnUns4qX3Ai37ohDzDeiqzEuhOiS1UmRszAty-Ts4oabc16iyf2d61cp7PkJpY3mi1RC2p7RITkIikGURLRW58VYSbmP0dnsXJaTXzIIRiud11MvFEkeOTGDs4gyxtlcEILTWKSmBevkjOjm0mX9S6nSghT7dxTaZG5ebC3RScOyyhJZHTeKQDm0Y-nYjjEHWzQ-2XgfkV-VkpQ4W0Gldi-hWiWF-CN1VNv6m6zarLobTjtonTvk5UDjoa3840F94LiX9dVIfPT7mlXVFYp_hWI649SoLP-s-3dq7Ye04I-YHWbAPOyCB-Q7mQavLw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9a15c420ea.mp4?token=MpG2cjHjL1H0q8uApLXd4EXHMnUns4qX3Ai37ohDzDeiqzEuhOiS1UmRszAty-Ts4oabc16iyf2d61cp7PkJpY3mi1RC2p7RITkIikGURLRW58VYSbmP0dnsXJaTXzIIRiud11MvFEkeOTGDs4gyxtlcEILTWKSmBevkjOjm0mX9S6nSghT7dxTaZG5ebC3RScOyyhJZHTeKQDm0Y-nYjjEHWzQ-2XgfkV-VkpQ4W0Gldi-hWiWF-CN1VNv6m6zarLobTjtonTvk5UDjoa3840F94LiX9dVIfPT7mlXVFYp_hWI649SoLP-s-3dq7Ye04I-YHWbAPOyCB-Q7mQavLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
گل دوم مراکش دبل اوناحی با پاس دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/98207" target="_blank">📅 22:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98206">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گلللللللللللل دوم مراکش اوناحیییی</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/98206" target="_blank">📅 22:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98205">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ4uAk76Tbn-BHMRB_2a9WrIbFRMBJUdvChX8g7Cz381EVjGU90b3oDz5mGfcYbiGdcxbxQcqBDlHAgT1EHCTu_XPY4YTvQ7OBQNFwiloNYOGTX3mwtn0A5P1r6E3ItlRGqdQyv0ORRgdrbmg_LTac4qOzM5QcxWKSnQ8jJvPejhAAeee8k1yu7CpcCS_fk-Nd4EaisW3mTxz4yH-tG6XRg6IynKfNANZq8AtR6PBw6tD88hbbNGqh-EjwsYSBbyyvV5vpVrm2S1E5Ht01RR6kkuEEihfgrn89bXpVoEOdrptObZ2jw5g4DnILzjQGjR1xusE00AB3Z1m3Iu4W-ieg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل موی جدید رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/98205" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98204">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/98204" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98203">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mcNLItQIXTnII-_uSMClNruOA3V2w4U5L2Yr9hNK8PTZdCejnvJsm-oL9NzUSaRtJBvRePPMURr2A-Kc22T7ONT1fjjhAbmqyuh5uKAlMs-GZhRweHxB6RtOGCnh8N5elfhp9lhkbvuHjtMdLgEjJJQ4Lo4Ha3ncmiz2HDw_xqsMST1QLTwd2Hy7M4CiEa2eCbtXsktNui-SMOTzhigPUxm_vVcIVhgmmKkjUatWRW95ZLfh9MnRYLo-YcZE5_OLpr670yBMiiw8QHk4MgJU7Nb9aUGgyGFp5REzFVJRiRpE601_7VEDZcWXdz4NyjbqNzm1_cSJLZOViIwNws2jlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/98203" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98202">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79bed95c4a.mp4?token=ROxAJ8fOpehQb_EngRa_pWqLTGT8-RpCIOm8poQbTajIw0_qynaX9SRTTK93yjWfj318Ic-Nec9QLez1TcrWBlY1ltQWomFzAHvEF8FranIg7K9wQO_B6yxdcABao7idoF9GuT5EA4FONbLcoWsJBJzpbLRS2kkDymSylq-bh73IEjpe5MCdbq5SMV2XSHH20fwdHHejcB1vYYQ57AuXgMXVEaUy-YQhYFVE-fOO9lX-CMBGQQ2YkhY8qudLZd3LVwe-87_k-HZ-XCI_EyjY5fFkknSUrcr2fpuAHTJfMaTP3fNBDG305riPhYUqTdkfmz6YNeH6yo6jCRTj267qVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79bed95c4a.mp4?token=ROxAJ8fOpehQb_EngRa_pWqLTGT8-RpCIOm8poQbTajIw0_qynaX9SRTTK93yjWfj318Ic-Nec9QLez1TcrWBlY1ltQWomFzAHvEF8FranIg7K9wQO_B6yxdcABao7idoF9GuT5EA4FONbLcoWsJBJzpbLRS2kkDymSylq-bh73IEjpe5MCdbq5SMV2XSHH20fwdHHejcB1vYYQ57AuXgMXVEaUy-YQhYFVE-fOO9lX-CMBGQQ2YkhY8qudLZd3LVwe-87_k-HZ-XCI_EyjY5fFkknSUrcr2fpuAHTJfMaTP3fNBDG305riPhYUqTdkfmz6YNeH6yo6jCRTj267qVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول مراکش به کانادا توسط اوناحی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98202" target="_blank">📅 21:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98200">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مراکش اولی رو زددد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98200" target="_blank">📅 21:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98199">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/98199" target="_blank">📅 21:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98198">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بریم سراغ نیمه دوم</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/98198" target="_blank">📅 21:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98197">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rcsse4UfEKd-pUZunvQEGt8vS9Jv5JBqjVJbPW5nU1OTin3vwf6DKIqrh87LL-xWMMxZS0DwRj9xNME7-n2CTnjtsVEbE3Aiw39R5IoJ21jqCRUGzEYo12pVuUMW_odtwJe46BPLHPrXqdKydClGbCizVaa_FGlv2eL8RrQI2gsuBeFSykQlbyuZMb0MTPKJhu7SkK8HkPP-7SQ6_aqMFP5xmNhcfONghvGuKp-U-sfN0SZ4P9ptgK07ylACBPJOu4m-lrr0KD4K67mFOFrC3AaQxsjcuNkMnK-myZ5n_11KNr04Dsc_7tZd8SMRxXeskUZG0zD2jMZE5TLSOlwmxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول بازی مراکش-کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/98197" target="_blank">📅 21:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98196">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcsqZNZ3bQFbtLeCZTI6gowxFmgC6EhB6a0p57mdp6Z_Za6shwMVA99Aqjs3MDwj-72kVVaDiMyRBbfHB04WGMZIefKq0ocApOIUkFZqfFC8GU80Z1KkEfgFOEo3-u8b5Q8feJVj2xz9fpA-qc7FR91tVXUY6wO_7ZtmW7ryIvAFX2scbStk3lAbnBoO4hsqH--rboF1MttjLft3B5-not68ubj2TPReT932pApdiGXR8ezQFGTf16luI03gCxLMy-IuI0iuJBQP1CfFFL3ZTvcR_IOXVIizF_fVPL_k8kmydXYdxpuHvjoOyXpVO3bBDK7BClHRGNcYLUxu5DgHRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی اینفانتینو هم دیگه خسته شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/98196" target="_blank">📅 21:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98195">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پایان نیمه اول؛ کانادا 0 مراکش 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/98195" target="_blank">📅 21:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98194">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwvUM3VgqCp9ycaE8WbdgKBlufdVG7em6Wh8Cg3tsMA4NrNs47PVMuXfpyl7vSP9xOpufQgG9vYpDbdwriqX9vcm4h6psVbdzeBeaxEQdgBRQ3wmP5Q-4WODLFsfgKz08rtxOc0NvnftXhQbjEM-NZGUDg8-StBdpLgmrOyufu9wk2SwYa7IPK3hH8VD-UOuuZmSpknBIbAaPmV-ueNoD4URe4GsKMH5OTJDiWegQ1IMhw-BlYS1P7zBql9RURgBQKS-3kX9yTFcLbDPRVTfjDDGcz0418ggsZcr1kB4CnnRcZc0AKTlPF9rP4XgP4aa10O_xqrLWAIqm_-yQ1PtdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایباری مصدوم شد، صوفیان رحیمی جاش اومد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/98194" target="_blank">📅 20:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98193">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdqfekM_oL9fTvyNa6IP59g2obFJ0zuJJmPr7eSCh39muzuNCYT2uI1HMxWeopYm3VKUTTPm1Bq8melbDE7XiUm20A18pmJAxu-Mp7vEz6CZGZd_yp1UN6uR0Bccm7Beu8sGnRDKt1RKtdwZR05lR9C6mwES3uNV992BDfc3kUr-9N-MdN96GI9LKi0xB0Nd_e9YIu30lZGaajIWXJbJ7e3Aepm7HlejfMpgHdpmoxAnoX5p_MZP7LsvQrZLof95HA0-OEs10hxv6Ow9-aNIvfBHEYcudAL2nsJ7tVtV9_NpGa1pgGX9PHsp1MyJYL0xquo0ve2G5UaH3KIvMhp56g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98193" target="_blank">📅 20:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98192">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIvv1C_oYgbDAlQbK9_yxQgsnD8STju052XY366bYp1yRoVzs2VIvMmEM-jBh9kZOeH6kl1C-dlXWRFIu_AIwEz1QXU0TTbcZ5BOxJJgwjCZAgKlGf1hIFIgyL3jmxX8LHvJ4CYkPF2Tz4DLkLz7Q-umqcWFjuClmPAkWeMBeLmVFIyVbijW87Z3ezN09CWPUGPE_sMaJpIKCiH8sWcDmw7qXHCikwwb7Qswmyo2UbeD7EIqTxkFFLk_8UU69EOGv9eVJuKikGcS6a9yH4857HLOJKNfjeERRQ3RTOUkv4Yi35TuiHOeGPz2so1Z9JzchEiAe-hp29BgGHO3H4PHPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گلریه این یاسین بونو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/98192" target="_blank">📅 20:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98191">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سوپپپر سیو‌ بونو</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/98191" target="_blank">📅 20:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98190">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شروع بازی کانادا و مراکش</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/98190" target="_blank">📅 20:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98189">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🇹🇳
فدراسیون فوتبال تونس از انتصاب هروه رنار به عنوان سرمربی این کشور تا پایان جام جهانی خبر داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98189" target="_blank">📅 20:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98188">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OF5zJaNFeTTo-3w_ymFWvRhm2KDCeHjhSfggGi3UIBP7my_evtgFqcO7xZHh5mBolf_I6PJztBsBva5XNxYe4u5GODdTXJ8Yy58wsnNbNHmcSJdvrDgKrCvETqidS_HK2_IJJooiEw6_4bZF4QNRSf7NhZcgXzuR3MJVqdh28b4bKKjBSHz6Mjo7ufRTXFPwHgociQNFB9avkKAi9Y1gHT2QteJhmbfY-0RNNdzy2_WJKYVbIZFNqCz40pappc5Ic_lgaFn0iFP8fJvlxQApZji7pg4N8xHaLFIGG-j3fUJpbEk15Gx1p5oBbfUBAG3Ry8nrmB-lVD-2q4abIbOcTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
🇪🇸
آنتونی تیلور داور بازی اسپانیا و پرتغال شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98188" target="_blank">📅 20:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98187">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N38WORcAe2cCP9Ta_LjUYjRzrDsu-4UwERUdadfrhqLKX0e0unkblZ3vIAhPWQen_5u6Up499Tlwiu9Iq5RQHsN0XZqLAA_H_bYqV_1CLPjo1J4TKpi96njGF3u3pn4x6xtoSDDwLMsTypLdN6phnwSHl9ukSMTwQR_K0wp5Ig8F0LQUqOTKjbzj3AfUPdTTGh2FP0vTldlazOGdMVEDlqDM4V8vHrI-0GHgKydQ49V0O8MhL9opLAKjSOxiEm-5hlCE-0lix6qJe1aRCQv01RvdNswsR2jFt9uHuljPiTzteblCamNZFkUfOBj63R3AlY53FHw6n9m2Sh0XAZV2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
پدری، هافبک تیم ملی اسپانیا و زیدش، الکساندرا دورتا، عکس‌های جدیدی از کوه لی در لس‌آنجلس منتشر کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/98187" target="_blank">📅 20:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98186">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXMTQHjDdV2nl7PRYK-qDFKkwlPqf_DuDtEpZm-aZRp2CYrWC_MNH6dPWLT6enLUtmeXrTati_7VLO-mHTNeep4Zib_cipx9FA9SG_rC1w4ScIHFGX4mx2By2iJpU0CEEQ4IZnnudQIu09Oyohm739DycB6cmpBU9kU4WVm-Ztrg368UWZ4qMUYYF23b29inwRgU9kbxUKQhVoWF-EBIys3UAvKopT9CSCZ_Ur6NSeLKGnZLvfhFJ7xqMbDaXx__d_T0m5dLAo6LXgp7_VzedirB2pB4BewDMJfjli-mt7oeWKdcOztRBlVOB803RFlUF-nf7g9wMMILIznuWXHb0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#فوووووری
: بشیکتاش ترکیه با آرسنال برای جذب تروسارد به مبلغ ۱۸ میلیون پوند به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/98186" target="_blank">📅 19:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98185">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oL8chZRAukZ9rMygwq320cS4thPmXbSq_VIzlNZGbp1RrvLlhL8OOMC47JVZP4TLeTHd0uitZB0wgvw79JhdIQwyWcx5UnK5NHd_XouaSqn_E-Cg0weVtfJDmwEOpnYz4vRPFLoxjeAA5Dsmkr7wnigv5BNntF7H3i0NNkOAKjHIYMoVw8jo92K7IdvoEqg-qUYeyHWJEalkhRgoy8Ufgl-SQhk5zgzZG7C-Pm-J_MpSy0Ow2zYqR094PItHGZ0O-tIOq9qvmk7rshH0gJbbCwO5RLhRaheTU_FABSR5Swaqk5SpGo3UmNBEME7yA0RNZTr1jAl08oLGS_MV0TdgUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
— RMC |
🇫🇷
🇵🇾
فدراسیون جهانی فوتبال (فیفا) اعلام کرد که به دلیل شرایط آب و هوایی، احتمال به تعویق افتادن مسابقه بین فرانسه و پاراگوئه وجود دارد.
‏"ما وضعیت آب و هوا را در فیلادلفیا به دقت زیر نظر داریم و در حال حاضر احتمال زیادی وجود دارد که به دلیل شرایط آب و هوایی، این مسابقه به تعویق بیفتد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98185" target="_blank">📅 19:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98184">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4be21116.mp4?token=DtSDbTKZ-QC5VJSrlSH7PmYja75j7_m4rPXK6zvMKS_jLFm0JVbkfs4ETstBmG_sdCuwx9l5F11f3VT2vNddpPX-7TajlaBO9Dg6f6eoYTzbQ9Ke7yaO5dk3faHAOY6jlGVJCbhsADhYd1Xj2CqLD_JZbQHxTU_h9Vi6aT4koiBT7MTGiS_-I6MTpCP1M_itS-rEeqhqgFYmOZ2HokivfX4UOPleFOkE6hQqonvzsCY7ajtwTTUVu9VllzxIKglzw4hKrJrc2ahY-hTKFtUNFCmp4dBIQnItETMB2M1iKzpuKvHcD5Lox_ODqCnBXbZqOGIyASnmdl08UtX_nqeoCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4be21116.mp4?token=DtSDbTKZ-QC5VJSrlSH7PmYja75j7_m4rPXK6zvMKS_jLFm0JVbkfs4ETstBmG_sdCuwx9l5F11f3VT2vNddpPX-7TajlaBO9Dg6f6eoYTzbQ9Ke7yaO5dk3faHAOY6jlGVJCbhsADhYd1Xj2CqLD_JZbQHxTU_h9Vi6aT4koiBT7MTGiS_-I6MTpCP1M_itS-rEeqhqgFYmOZ2HokivfX4UOPleFOkE6hQqonvzsCY7ajtwTTUVu9VllzxIKglzw4hKrJrc2ahY-hTKFtUNFCmp4dBIQnItETMB2M1iKzpuKvHcD5Lox_ODqCnBXbZqOGIyASnmdl08UtX_nqeoCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
در کمال ناباوری و سرعت، به یک هشتم نهایی جام جهانی رسیدیم!
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98184" target="_blank">📅 19:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98183">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a342fb6d.mp4?token=KXhfFO8G7xlkhjqdkB47IQ_G0yW7Qc0P07AJf3RKgePsiAnSHkKbGkEpBU3dKTIGLEjt5xiH_Y98OvlhV6BggCNLbWFc-K85wZIYdFUXXP541lk4w8tMyUtJSCZBoUKGPQx28tEP1gOAjS2JkibCWN5hQIRXYHVvx7aznkcQttpUj9rCJXH_YFUtdalmc8KwUVKngU-IaXcxAhyB7-q74OXVfEBuoPgXWy_HALhTGR6ZavN4UrYewQLNrsqQ-2gZKeXJIswLmzGLGpzSRqKMP9a72bI4V1EiQp7rO2j9xKpQ_2iswTmdqQ7b38vClG_RNx4CjDTKaVaJbXAYiRYg5ZgJrsxrR7V-5253Y483ahhQJzF_sstGI4_jAf1tjpBtL-Em1QgkapCS7B7aiRqOderWq6BE2ArdNmbOmPXxurDA-cj7TKVRY_cI95IYLVYqaITDzOWxEJQVAzX2a2q8DqmsnpEe8BNRlgz6tEKWuxZUWr52mXK8HkJ_ZJcFz2eMowDC-2kP8ikxTRlRATWf4Ousi__CR6lREZ7cbn9uzDo277FtPSsWP5JCVcoxeKZaFkP2-B_U-S2R_xxc9fTx3Z9QG04sOgH_UfJUqKtcDs2EWSjDNBCDuDFhQ7vD2PZYokN6jhyuOatGKk9BRMeoSGAiV8h21wh3ryownjAWMpU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a342fb6d.mp4?token=KXhfFO8G7xlkhjqdkB47IQ_G0yW7Qc0P07AJf3RKgePsiAnSHkKbGkEpBU3dKTIGLEjt5xiH_Y98OvlhV6BggCNLbWFc-K85wZIYdFUXXP541lk4w8tMyUtJSCZBoUKGPQx28tEP1gOAjS2JkibCWN5hQIRXYHVvx7aznkcQttpUj9rCJXH_YFUtdalmc8KwUVKngU-IaXcxAhyB7-q74OXVfEBuoPgXWy_HALhTGR6ZavN4UrYewQLNrsqQ-2gZKeXJIswLmzGLGpzSRqKMP9a72bI4V1EiQp7rO2j9xKpQ_2iswTmdqQ7b38vClG_RNx4CjDTKaVaJbXAYiRYg5ZgJrsxrR7V-5253Y483ahhQJzF_sstGI4_jAf1tjpBtL-Em1QgkapCS7B7aiRqOderWq6BE2ArdNmbOmPXxurDA-cj7TKVRY_cI95IYLVYqaITDzOWxEJQVAzX2a2q8DqmsnpEe8BNRlgz6tEKWuxZUWr52mXK8HkJ_ZJcFz2eMowDC-2kP8ikxTRlRATWf4Ousi__CR6lREZ7cbn9uzDo277FtPSsWP5JCVcoxeKZaFkP2-B_U-S2R_xxc9fTx3Z9QG04sOgH_UfJUqKtcDs2EWSjDNBCDuDFhQ7vD2PZYokN6jhyuOatGKk9BRMeoSGAiV8h21wh3ryownjAWMpU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇲🇦
هواداران مراکش در آستانه بازی با کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98183" target="_blank">📅 19:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98182">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aj2PgvHuAOgFzVgbR-4lQfSXdrpXyEKZ2WDThQUCh_T0Q526lok6rQpo-HGzaQLiTYRObnVBJqtv1ZX3I53_OzBmdsMf3vX0Wc5SiV_a1S3P2pcFeu9-LOYxJM4ajcYdOei31CsSp5CF9AMe8OUS1UucwJerVSf4udvEqkwyjK49BZ-kJeVET9DgJ4dMwkbOBk0Jcaqpenrchx1irSP1yz-qrQDDCQQePJy5Re6zWGiUmiZeCvXpuCLfWDuPjn3m3-sSFaqbx0iu-g8ZMwbZ-OoUzP5sF1X5PITKINoM1aOnSI3KJKwaYTAtEKOuYVf4ie8F8WNNuOVptdnmTm6nGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
ترکیب مراکش مقابل کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/98182" target="_blank">📅 18:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98181">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKtpJ_KJGDqr5UYabpwHqDQJ1R3qTszwn7NJIyWgmHMm0Y1k8MsY2ULQcu7Fe1XEwvdnHBn2ItxxsX0NTZVqL7_NYBktVmDgIvhRi1tvmyta92a3RKOdIExiD4d2A0B-NHvux5OQLDHThBRFhi1tRADgvMQ6Jj3HZq6Vrmmi-uZMqZkIqsJrN4Wj0zVF9vD5rIbm3fL01X26dMAuVUa-9ARZtCxKxi6jdFbQMcFnHVB9TO2AB8yzcUOWDynB2FzENKymr48H-gRL_WZrttviTppHSR4IliWkZ5DNfeLCEMtZUC7Rhod8xBM7TvJo8NWf7F0mT8iNN7yAG0gsrlOBqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
🇨🇦
ورزشگاه NRG برای دیدار مراکش و کانادا آماده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/98181" target="_blank">📅 18:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98179">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZoLubezeLmDQ4DO54rJAahRT0fvtkvRMDTCY0WsPo96LGqtUy4nE3hQHtiYNiB31vkgpeIVaBCNTxjrPiTjZczMD2zBcBj-us8r0NUoKJJrjbynM86__Ye4fHnb2fCTSu0XxAcVmdh9fJ660wjlcyu3AasnptTjt2smMrfws4l3_G200rJ96WtaZFtCEdQnk0_67rM2sdXjUUhG4TZ0lk52roxqR2NNaYgnacqdfnD6MSMbEqrQsGvZVyO3C0y7MBkMVKS1Agg9jH6IXCiRhNpASSGBOI3eXdx0V3t0Xm5_f2yAuolI1MXnFjQG-nr_Dre-HuWEJU8II0IBgdw7qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NQyBLzKRdHU0OWvxXRHZ5mtj1VkeSnMpS7CtYCxM286fsVd35D7f78jVDFp7qXMIAeqb6WqhyuLOIGILoxTHfv0w825vnHwxZwR8tTupv6qiRGAMdPM_Xa2SKlVoat1zlUGNX6DNqonviDc_n9T7_B16IC4mHNEGm8R-SpT_R4kiUNiUNsPVHe1viQfWq-zPzfb9HJC2vlPsCTjgCK9ItsUq_P4Z88n2yEMtT2RH2lmzCteFYCJ3dmSRH3wswCkQoGjwum55fMZOvpWhxWbmuse2xJj9FaXfOzM-4dPlnW2z08Jf8bTclfPjeXnyXKug-vEb-3VSInmGIpxWTZItGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
📊
طبق گزارش سایت Score 90:
✅
احتمال پیروزی تیم‌های ملی در هشت بازی مرحله یک‌هشتم نهایی جام جهانی
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98179" target="_blank">📅 18:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98178">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af013992f8.mp4?token=qZyUhyzdicKgkSmTT9bbZP8faRqFBUYq62ILZF4l8hg7gzGOhmNSzAB1wtxa4mkjWp63OW3DN6jPIEJbKI2vdnP2roeZ-vW306eRIzoLVHfZNPk1YZS4h709Dr-Yi-MMSnInUI8DJXmDE4iADZ62N3m_3Rj1FQhxgt_-4CflHOlRyrbkcRvOzbWAiYSYoysbRLatmyHU01QT1W9y_BPkk1K_xFECsaDf77Y7hOnT6imKhXHLkZTDoBwvGapwQmSuowzhyS6277zpK9_ZdzB8WRw8ORcpkPBmQ4X0aSKkUo2cZe0h2PJ_UgtdgZ_hNgk9h7FkYRMnqJK7UtSrqkR8dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af013992f8.mp4?token=qZyUhyzdicKgkSmTT9bbZP8faRqFBUYq62ILZF4l8hg7gzGOhmNSzAB1wtxa4mkjWp63OW3DN6jPIEJbKI2vdnP2roeZ-vW306eRIzoLVHfZNPk1YZS4h709Dr-Yi-MMSnInUI8DJXmDE4iADZ62N3m_3Rj1FQhxgt_-4CflHOlRyrbkcRvOzbWAiYSYoysbRLatmyHU01QT1W9y_BPkk1K_xFECsaDf77Y7hOnT6imKhXHLkZTDoBwvGapwQmSuowzhyS6277zpK9_ZdzB8WRw8ORcpkPBmQ4X0aSKkUo2cZe0h2PJ_UgtdgZ_hNgk9h7FkYRMnqJK7UtSrqkR8dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهرداد صدیقیان: چون رو جورجینا کراش دارم دلم میخواد پرتغال قهرمان جهان بشه
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/98178" target="_blank">📅 18:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98177">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🙂
🏆
🇪🇬
شادی سم محمد صلاح بعد بازی دیشب و صعود به مرحله ⅛نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98177" target="_blank">📅 18:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98176">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwhfWmdVpQTSLmgSz1cuFVtFxQr-x_r-lfsVKa0sPNra5_sO5EpLaucBhBRC_Y3m3SeQKINRTK7aQ725OaZUkMglZkwbS7xR_9DW0FcLwHVSaKGRHOwT7TZ1QbuLXTUjLEr-9JxRdLfTnFhXsIPh0vnn-lG69z98FYHrhwD67UseLC0XGG-6oA66pMVFVIK21gm2ZrsjAzI58UOKBfKDtq8dv75dlLd_WCNaTYUIBPhNToQOO4HhEyZwmDMyS-TiDg1MLCVfGR7aMRNgBoefscTM29KNtXU4mB6PhC1WuBlwBYK0-JUamKpC5ah0C5T9KRG0Hxbp_KV0H6TmaLpduA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
میگل سرانو:
باشگاه رئال مادرید اعلام کرده که منابع مالی نامحدودی نداره و انزو فرناندز، هدف مورد نظر رئیس باشگاه نیست. فلورنتینو پِرز، قصد داره یک معامله بزرگ و مهم در سطح جهانی انجام بده و معتقده که اولیسه نامیه که باید به این تیم اضافه بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98176" target="_blank">📅 18:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98175">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
😐
مهرداد صدیقیان بازیگر سینما میگه تونستم مخ دختر مایکل اوون ستاره سابق فوتبال و برنده توپ‌طلا رو بزنم و حتی برام هدیه آورده
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98175" target="_blank">📅 18:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98174">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gudfLJ7XJyeEgfLhUAwMtnpX8EkxjI9FMfP4NMFdMgXT3FrNiinpUadxEOq07AQISRq7xHrrUIRLo9Z9MqIkmWBmGUrYX0OMyqpVcMoXvlQsH0Lplg39ixDVLONNBP6QvxhNYfhi69vI7U33LQxetWdpCWmcr3V8FMfCCXaYaVHzBSi6rYVAAXfmW1TwoMygQ9XOito8ZLJ0PIckNFsCaOXuA71sc6KRnWcpCo4BnW_Pfke6TaSxB5Ob3f2LWcF0VMS-KRwTQsb3KIxdv2WoSoaXlDL9GtecMdsYSuWkjsAW-xpEPIp2mkD0bLj3Acz3qseU4C7EuJTK-sP49dedKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇭🇷
اظهارات فوزینیا، دروازه‌بان تیم ملی کیپ‌ورد، درباره مسی:
‏" به او نزدیک شدم و حتی فرصت نکردم زیاد حرف بزنم، اما او بلافاصله به من دست داد و گفت:
‏' عالی بودی. تو یک دروازه‌بان فوق‌العاده هستی. حتماً مردم کشورت به داشتن تو خیلی افتخار می‌کنند.'
‏ شنیدن چنین حرف‌هایی از کسی مثل لئو برای من خیلی ارزشمند بود. از او تشکر کردم و گفتم: ' ممنونم، لئو، تو بهترین هستی.'
‏ سپس از او خواستم پیراهن بازی‌اش را به من بدهد، و او لبخند زد و گفت:
‏' حتماً، آن را به شما در راهرو اتاق‌های رخت می‌رسانم.'
‏ این لحظات را تا پایان عمرم به یاد خواهم داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98174" target="_blank">📅 17:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98173">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👀
▶️
🇨🇻
کشور زیبای کیپ‌ورد که علاوه بر فوتبال جذابش، این جاذبه‌های دیدنی رو هم داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98173" target="_blank">📅 17:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98172">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a6f3f631a.mp4?token=LgL8TG_B-DM_dIXDVt4g-8JCLxsJ8PGv4iHGAUaHGaazCSHmWu4TAohUR2ilTRXEYyR2FCHkgpzTUQTcjdyGsxuIiEaZD55v3YaOm4eX_buwpAoSujYJPJBiiTJLeod0o7ByqaqUfYaEOp7DF2Qt1V0dXnezRayofl6fOi2Y1wOsjHAaKjsNHlcZJPN469zKfi0MHuonhkbqBvQsLha8BlmqhJKy0gm1HDDlvx9qMD9FG6EMPL77paHbAIUTUWhA3WK7hiPwrjt97yb9SlK6RmTwgL4aIiwDMl2FiAtAJhpf1t_sniV5xQukXtMOgOFFpPQVtL_sD8ahI7i2h6H_Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a6f3f631a.mp4?token=LgL8TG_B-DM_dIXDVt4g-8JCLxsJ8PGv4iHGAUaHGaazCSHmWu4TAohUR2ilTRXEYyR2FCHkgpzTUQTcjdyGsxuIiEaZD55v3YaOm4eX_buwpAoSujYJPJBiiTJLeod0o7ByqaqUfYaEOp7DF2Qt1V0dXnezRayofl6fOi2Y1wOsjHAaKjsNHlcZJPN469zKfi0MHuonhkbqBvQsLha8BlmqhJKy0gm1HDDlvx9qMD9FG6EMPL77paHbAIUTUWhA3WK7hiPwrjt97yb9SlK6RmTwgL4aIiwDMl2FiAtAJhpf1t_sniV5xQukXtMOgOFFpPQVtL_sD8ahI7i2h6H_Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇲🇽
هوادارای خانم انگلیس در آستانه بازی با مکزیک که پسرای مکزیکی‌رو تو خماری گذاشتن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98172" target="_blank">📅 17:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98171">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPZoNPfkkWFkPnksXzK9IwkYDilCZM4Jp5NZwpZ-a1stOeSpp-ugqaqZQjrRqPhrDdOk9Rfi4P0kZW99pmqkuf3zZzx1shzU3kb1_745F912rI5OmgATx9S7UYXM1JB_RURZ8RAHk7VlUdMSyQoq_blzSIP5jI_h610gAXLqFA1goamksSisEUeiRJ9lvJG9XJ1HL3tiVDD63OcUxxcFeWQSI8ZnVTN_k6vuffkf8RaxCaNPRklrBcYv37vXXe0-ZTIWJ58Sc6lCw1qGEA15RQ1CBWqxElZjfMoD632635STuqnzG-Rx4lJ8fDPbY7yIvQQ66WBChb10wzoD5DrQ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⚪️
فوری از آاس:
باشگاه رئال مادرید در این تابستان با هیچ هافبک دیگری قرارداد نخواهد بست. این باشگاه با جذب برناردو سیلوا به عنوان تنها گزینه در این پست، رضایت خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98171" target="_blank">📅 17:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98170">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f0c663da9.mp4?token=iBDI3naX7ra-rZZTYSqDeMW0voQiW46POLDhB_DeXdj9U3C3JLah38pKrTyGAoD6knVdSq1emHpoqnYXBUVnr4G9evXtbPpSkRswHdBl8Y-z3fKys3auXytEsfKwn7gg1SKjPAvRP3B3KJ2JUOMH87Em4P862-LkZRD50u5DvDW72tAdDe07u5DJsyNDLAs9DimeMMdGp-prptz6YrfMXo0MhETEt1-zbuZYUMizOEVDfcl8kBzIefpeHMUmp1BFTW02JLAnc0LiHQXULOtTKXg4twNiJ8J4grErCEBpkVdMpEG8AAESdBFibVOxQ6SxTfLCEoh31kl3CeGm5mnXxIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f0c663da9.mp4?token=iBDI3naX7ra-rZZTYSqDeMW0voQiW46POLDhB_DeXdj9U3C3JLah38pKrTyGAoD6knVdSq1emHpoqnYXBUVnr4G9evXtbPpSkRswHdBl8Y-z3fKys3auXytEsfKwn7gg1SKjPAvRP3B3KJ2JUOMH87Em4P862-LkZRD50u5DvDW72tAdDe07u5DJsyNDLAs9DimeMMdGp-prptz6YrfMXo0MhETEt1-zbuZYUMizOEVDfcl8kBzIefpeHMUmp1BFTW02JLAnc0LiHQXULOtTKXg4twNiJ8J4grErCEBpkVdMpEG8AAESdBFibVOxQ6SxTfLCEoh31kl3CeGm5mnXxIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇦🇷
🇨🇻
امکانات سوئیت ۷۵ هزار دلاری ورزشگاه میامی در بازی دیشب آرژانتین و کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/98170" target="_blank">📅 17:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98169">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58ab6c152.mp4?token=CY2oqK7JvW0NSD0LxrK0ySMZO-VDEDNqJ3pILsvJuGprKWGdualW5tn7dHQyYrkC4D-kvOE3jzKfIP7BECL0u_4hPoyesTs1IQhKRHz73LuIHZjO8lb8f2Savn_mhv5yEYDymoC4DujDn0B5X1_DGA0U43iYelAWOvT82ptmbWH-_oxEf6xWoHHgy1x85WzUvHOBg6L0lDA4Nq8SWGovlWCjl32jK4MRDF5GQEyXFxOAL-kn7xPsTg4PXDOSm4kVjEAQVQt47qgXRtqsx5Xz2ujIxMuToMgpsj3ShCm44An4kAEAFmS4LgnfPB5b7LTCtBYb33FKScHZvnX4mAVHQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58ab6c152.mp4?token=CY2oqK7JvW0NSD0LxrK0ySMZO-VDEDNqJ3pILsvJuGprKWGdualW5tn7dHQyYrkC4D-kvOE3jzKfIP7BECL0u_4hPoyesTs1IQhKRHz73LuIHZjO8lb8f2Savn_mhv5yEYDymoC4DujDn0B5X1_DGA0U43iYelAWOvT82ptmbWH-_oxEf6xWoHHgy1x85WzUvHOBg6L0lDA4Nq8SWGovlWCjl32jK4MRDF5GQEyXFxOAL-kn7xPsTg4PXDOSm4kVjEAQVQt47qgXRtqsx5Xz2ujIxMuToMgpsj3ShCm44An4kAEAFmS4LgnfPB5b7LTCtBYb33FKScHZvnX4mAVHQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گریه های شدید یک خانم تو مراسم تشییع خامنه‌ای :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/98169" target="_blank">📅 16:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98168">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a2a62f27.mp4?token=NWgQ3ihfBwIQxQhc0wI_83xGSdTkaF5G20QSASYJ2QbgTKz8PvH2Ghimw0i0q7CmfNHtLc7gqVtFdai48NGRaWJFjQWYRt7PbTo35LrqIDkTaVUvxt8DVIO1HT_V-Np7iBCYekUK4YClOXm29Z_qy4ITt_QGRJv0hqaAhRUt1ZjluLB8KSKSu6aGxw6VJp6h1zRp0vuJKQpX7W55jUzm844cWZSm6hQxNgALvPcComP5IIeoisSTYRlekmYC5OMfhlGNO6GXmCq62RARCYoVHzVH3aDKbP_-s53Dt-FCAyzjYe9Bb9Mro1k73AaDv0OdSjnvWuNBQmNr6bIjlC85hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a2a62f27.mp4?token=NWgQ3ihfBwIQxQhc0wI_83xGSdTkaF5G20QSASYJ2QbgTKz8PvH2Ghimw0i0q7CmfNHtLc7gqVtFdai48NGRaWJFjQWYRt7PbTo35LrqIDkTaVUvxt8DVIO1HT_V-Np7iBCYekUK4YClOXm29Z_qy4ITt_QGRJv0hqaAhRUt1ZjluLB8KSKSu6aGxw6VJp6h1zRp0vuJKQpX7W55jUzm844cWZSm6hQxNgALvPcComP5IIeoisSTYRlekmYC5OMfhlGNO6GXmCq62RARCYoVHzVH3aDKbP_-s53Dt-FCAyzjYe9Bb9Mro1k73AaDv0OdSjnvWuNBQmNr6bIjlC85hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
برد دیشب آرژانتین احتمالا بخش مهمیش مدیون این سوپر سیو امی‌مارتینز هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98168" target="_blank">📅 16:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98167">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5efd98ee66.mp4?token=SWzTRplsLRgefH5Cwtk6eDNDDpTf7nOC8r1iJbqfj0f_HvuXna37lh7k-TVoOumogq6wk_9zFKmJQ7G31OO_PnPf0EzXAf6PmPlRGuvXZWVRoi-HuyspNqX1qC8TQIwR_-K3MkWHcvp3dpF9zg8DKsE2RuBlel3UMCJlUl00S-j2ELriFYnga94KkgiyMUjM25W9rgHVj4xnEwVwfsXu21i2OQ89lae7pNacvY28fAZ2SkubTkLPpp4enAKWWR_eDWWZJ6v-gh7fAYngtPZcjPcjR1StjklSo7m1I-3I-93NUoqOmjpdocRX1Madc0yXipXKX9jlxn2eYDaVbr3kLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5efd98ee66.mp4?token=SWzTRplsLRgefH5Cwtk6eDNDDpTf7nOC8r1iJbqfj0f_HvuXna37lh7k-TVoOumogq6wk_9zFKmJQ7G31OO_PnPf0EzXAf6PmPlRGuvXZWVRoi-HuyspNqX1qC8TQIwR_-K3MkWHcvp3dpF9zg8DKsE2RuBlel3UMCJlUl00S-j2ELriFYnga94KkgiyMUjM25W9rgHVj4xnEwVwfsXu21i2OQ89lae7pNacvY28fAZ2SkubTkLPpp4enAKWWR_eDWWZJ6v-gh7fAYngtPZcjPcjR1StjklSo7m1I-3I-93NUoqOmjpdocRX1Madc0yXipXKX9jlxn2eYDaVbr3kLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
😆
رفیقای من وقتی دختر میبینن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/98167" target="_blank">📅 16:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98166">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🔴
#فوری‌#اختصاصی_فوتبال‌180
🔴
تا این لحظه و با تصمیم اعضای مدیریتی سرخپوشان، سرمربی آینده باشگاه پرسپولیس به احتمال بسیار زیاد گزینه‌ای داخلی خواهد بود و خبری از سرمربی خارجی برای فصل‌آینده نیست.
🔴
در بین گزینه‌های اصلی همان نفرات همیشگی یعنی یحیی گل‌محمدی…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/98166" target="_blank">📅 16:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98165">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🔴
#فوری‌#اختصاصی_فوتبال‌180
🔴
تا این لحظه و با تصمیم اعضای مدیریتی سرخپوشان، سرمربی آینده باشگاه پرسپولیس به احتمال بسیار زیاد گزینه‌ای داخلی خواهد بود و خبری از سرمربی خارجی برای فصل‌آینده نیست.
🔴
در بین گزینه‌های اصلی همان نفرات همیشگی یعنی یحیی گل‌محمدی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/98165" target="_blank">📅 16:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98164">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🔴
#فوری‌#اختصاصی_فوتبال‌180
🔴
تا این لحظه و با تصمیم اعضای مدیریتی سرخپوشان، سرمربی آینده باشگاه پرسپولیس به احتمال بسیار زیاد گزینه‌ای داخلی خواهد بود و خبری از سرمربی خارجی برای فصل‌آینده نیست.
🔴
در بین گزینه‌های اصلی همان نفرات همیشگی یعنی یحیی گل‌محمدی و مهدی‌تارتار قرار دارند و چند گزینه عجیب نیز به گوش می‌رسند. از طرفی نیم‌نگاه برخی اعضا به بازگشت وحید هاشمیان نیز می‌باشد هرچند که بنظر با واکنش خوبی از سوی طرفداران پرسپولیس نخواهد بود
❌
در صورتی که با نفرات اصلی ایرانی توافقی صورت نگیرد، گزینه‌خارجی در مراحل بعدی مطرح خواهد شد که به اطلاع شما خواهیم رساند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/98164" target="_blank">📅 16:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98163">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b6f4aebb1.mp4?token=ZG5-n2W9tvWNElzQ-9eO_TnubWwH3Ci1aA9gNZ-pjeNRyL4wT29zNyqU0qBzP8kBN-dmdBiYj4NUW4dQJwtr0y__SfVOZ49SPmDYcwgSchT2orRBErLX_2b4ryocWR_LBCy1vaJUAuCSGls4z2s9get4hzMG7moKq17F3YWMXt_jmg5nFi9SgbBL_TqSiqYIhODUkr-wxdVgnz0Eucw67mO83M4YDVCS12GbfZxSDv8EonEqQje_RQxhiRlc4529jwpo06micFXr10FmixZAEYiNFPppUh6iFUNAa5KMuMWYYU5VrN6CJyE8VqZhd7CJx92YuxfhvyEQnCZ6Zji_IUasV5UepTeT294PEpaKVCOXv8awYDX9k7Otr_ZX0fz0Dyl7DGlyUIxnhWbCK82mdrv6V6YCBJVg62n6oKSLtqDBEbxwOYFIP0VtRMDmss42EWZgREOsanuOszBgdgRXpddetrGy16MYXhGKKRJ3_cg_KQqdjCWLLAS8BaEaPk57Waw_6O6cuzvVMZ4PLvHiP9Z6tVNhH8Tb-pE1YjM6_AzA-HRuFVSZpurkv_2CY0TZsrYS8l4mJN0SC_tAaSlqwFtd2Oo4CWLwLPDto4r3xUTgN5S9nwVR6ARFHfyUSz-JRpWYuStskekC06_RUIZgsEt3nu5TSo4yPtl4PEokE3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b6f4aebb1.mp4?token=ZG5-n2W9tvWNElzQ-9eO_TnubWwH3Ci1aA9gNZ-pjeNRyL4wT29zNyqU0qBzP8kBN-dmdBiYj4NUW4dQJwtr0y__SfVOZ49SPmDYcwgSchT2orRBErLX_2b4ryocWR_LBCy1vaJUAuCSGls4z2s9get4hzMG7moKq17F3YWMXt_jmg5nFi9SgbBL_TqSiqYIhODUkr-wxdVgnz0Eucw67mO83M4YDVCS12GbfZxSDv8EonEqQje_RQxhiRlc4529jwpo06micFXr10FmixZAEYiNFPppUh6iFUNAa5KMuMWYYU5VrN6CJyE8VqZhd7CJx92YuxfhvyEQnCZ6Zji_IUasV5UepTeT294PEpaKVCOXv8awYDX9k7Otr_ZX0fz0Dyl7DGlyUIxnhWbCK82mdrv6V6YCBJVg62n6oKSLtqDBEbxwOYFIP0VtRMDmss42EWZgREOsanuOszBgdgRXpddetrGy16MYXhGKKRJ3_cg_KQqdjCWLLAS8BaEaPk57Waw_6O6cuzvVMZ4PLvHiP9Z6tVNhH8Tb-pE1YjM6_AzA-HRuFVSZpurkv_2CY0TZsrYS8l4mJN0SC_tAaSlqwFtd2Oo4CWLwLPDto4r3xUTgN5S9nwVR6ARFHfyUSz-JRpWYuStskekC06_RUIZgsEt3nu5TSo4yPtl4PEokE3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
🇦🇷
گل‌سوم آرژانتین به کیپ‌ورد از این زاویه جالب و دیدنی تماشاگران رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/98163" target="_blank">📅 15:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98162">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-Vr9eTRDWiK3Dc2ewDfBlhfnnttWIsuhvI-YxciVORhH3M4pTCVAqYn93TqUGN2VYiYGFUiO2_-bxNMDyjVGkw2UFFoUwFeJo9hkTFvOZkR0SbZkgbbjvYtN4D9m52KnI-7UQUyYFoVJMTVQ0YnJXnb4J24hAj3e15bdWYtZmv2rdo7FfQZuaUCjtZ2gj2ohJHdLsn5Svq1NNNJ8aHcb9sj6_pBIJ7xwFo2uah8AcnNot1Y9erNRjqOAKGRe4EKonxsGy4oZFz2MMJxfs6_3h-Yc_0wGixrj7yIXWuSs3ePX_St_6wvf_f-yHXqBqV26LKN77WjMIWjBgqOlXrDew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریک فهمیده رو هرکی ببنده میبازه، 1 دلار بسته رو صعود مراکش
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/98162" target="_blank">📅 15:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98161">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/98161" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/98161" target="_blank">📅 15:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98160">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98160" target="_blank">📅 15:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98159">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/341bb1b1be.mp4?token=L73fiFyuP7eI3oifk7_nUdV-yXNMXsAhVk79hQ_T6_ZGgPcLK4Dv1Gh6J2_jFLC1I6poi4hkgESMMn-iaI8iV_5FHBVQzdTYK5kODqxgQiTrYLiYt7c8FhS5eF_l-6jIndzD5Mvsg0_fBI6CT_8G3L5GRUiPYwPUj-reuP6fzI73QW0GN63w65y2mDKXD95yfYRTVnw4ZH8w-ixXTaLLC5rQn-YFzXcK5JVKpvikHexGEas_YMo3TR_avJJHOUx_Wi2bbKRpJbUidC0ZoWgESyDvDezwNZkRgAkHGzPFmZ9ir868_wYnGoRNl155puTwnmZHhjVxCNhl6opSnhNCBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/341bb1b1be.mp4?token=L73fiFyuP7eI3oifk7_nUdV-yXNMXsAhVk79hQ_T6_ZGgPcLK4Dv1Gh6J2_jFLC1I6poi4hkgESMMn-iaI8iV_5FHBVQzdTYK5kODqxgQiTrYLiYt7c8FhS5eF_l-6jIndzD5Mvsg0_fBI6CT_8G3L5GRUiPYwPUj-reuP6fzI73QW0GN63w65y2mDKXD95yfYRTVnw4ZH8w-ixXTaLLC5rQn-YFzXcK5JVKpvikHexGEas_YMo3TR_avJJHOUx_Wi2bbKRpJbUidC0ZoWgESyDvDezwNZkRgAkHGzPFmZ9ir868_wYnGoRNl155puTwnmZHhjVxCNhl6opSnhNCBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
عادل فردوسی‌پور: اگه همین روند ادامه داشته باشه، علیرضا فغانی نیمه‌نهایی یا فینال رو سوت میزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98159" target="_blank">📅 15:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98158">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkqYqNbmrZIUbyeaMHzP7qNaUeGJd-iN5owsisWdfpaWrEs9aQmwIjidLgDEgC8jnRIZp19rEX-0lQoBIrYqwiq99SWefCwyfgmI_To793KtRtiGuYXwI0U_VyR4ZuUIqOMMNFgb8YEI5AZ2S1veRFunkEyHmeQkoJGBPfubLQN33EWns3O1AcY4AIE2x7tXqR0JNxciOuHvw9XW1qS5DxIQcCd9omrAIgifBxcQM7RFnF0eO5TGQUiMm6c-Dyu_d1HuH74RwN9fWIwk7dkAUGfu7vmioAl3ZbsHoY_zEz81bDUnXn_zVJm4dc0OhnJb0NwlRxUN1QWCM9ODHnyB8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
هوادار جذاب تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98158" target="_blank">📅 15:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98157">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1aaf3f086.mp4?token=paQLqk99jWa4NMI9yxXMdGn1nQybULc4D_t_GaufyNL9_4VqLkrqvtxAaz7dJfKcN_-2qR1d9hGyfhrV9Cj__EF4jJsUUIawYA9VXs2o1hrzGFM6nAe7soB7NIn0dZEfCT6JPcczTcHVXcWpIEORYCmeiaQ9rieZEkLDYA0BlxaK0FMj35pM3kLIzPGkLf2BApN-HwrpFpImRJoRDUfrNBatXrSyNVp2yw5Q5QMh1pULW-3D0-ImK6yf8C6bqYCeNGs2dmiYkdf3AmG_olVXxZUaAbGChl8c7Z9JttskkrwoXQLN4K_QmGy0OKkqGOPwvwYtqCgdR0fJpCxmYsh_4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1aaf3f086.mp4?token=paQLqk99jWa4NMI9yxXMdGn1nQybULc4D_t_GaufyNL9_4VqLkrqvtxAaz7dJfKcN_-2qR1d9hGyfhrV9Cj__EF4jJsUUIawYA9VXs2o1hrzGFM6nAe7soB7NIn0dZEfCT6JPcczTcHVXcWpIEORYCmeiaQ9rieZEkLDYA0BlxaK0FMj35pM3kLIzPGkLf2BApN-HwrpFpImRJoRDUfrNBatXrSyNVp2yw5Q5QMh1pULW-3D0-ImK6yf8C6bqYCeNGs2dmiYkdf3AmG_olVXxZUaAbGChl8c7Z9JttskkrwoXQLN4K_QmGy0OKkqGOPwvwYtqCgdR0fJpCxmYsh_4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فتح‌الله‌زاده اومده برنامه ابوطالب جلوش یه لیوان آب گذاشتن و بقیه ماجرا
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/98157" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98156">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kInOvKX5cOK_9UzaB6BoH1qiHOVCdYsGlU3oiU4GfziEnpb7mX1114BPHnvKvTTPpglN-_legGWAf37NIkWLquBXnTDSt-EWFSahu0h722LZif9latWcR86sLCYIjMRzyktYT9RSm_ObuhA_1wWaSOreH7P0kaIRwiqbezHUKvmpRwtG2S-Sk-ptsWnIL4x4JMBb7njimoadvw-vxbFuTmdSyZjI1TU6EfKCpLvG1v-eJoyyfCH2xV9WY6Lj0rRFEEPhALdYdHXSdIs7ISqQ-Bxw7O4U_ONXXsOJR15VG6inmzwbudb14gs-E4U-_E4vkseupamN5669EqLow4siPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
حمزه عبدالکریم بازیکن مصر در پاسخ به سوالی درباره تحقق رویای دیدار با مسی :
🔹
ما با آرژانتین بازی میکنیم، نه مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/98156" target="_blank">📅 14:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98155">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a433836c4.mp4?token=jO9WJDxQIAKlCDgXOBzZypbjIwSKq0HSW0ihMSmJc7qrCLWz5OmiibyrPmzNX7uOYkRMMucwwlce9_v4Wst2Coz6JFGQ-9NrgUUBBP4iLyInYWPWrztUgMUO1p_Q21r7uMCHdKcilSn0Tk_CwbswypAKHMTiCziqLCyQ9vjS2smCcBpPb0g4RVc7e0jkhfUvLtB3_e8sbF99DzuA14n1PPGhZBhFYQSpk_W-COy9dQ0fSrouIfuE3BSsIEVkysZvrMoWNDY0LSOp782JRWPVcGFIqGxd4DR9DiRss6njRv2L8XG-sn4uacNxSEsxnHfo5fiTaUWGOtqWk-7SOSDy-JelMwDhKSImU4qOd95sIzedNvpJbbG4md6e5ePIHNC05pxwQ6UEHcXmanoY7dzCVV2twvvTn0Vz29PUgYImg_w2fEYmcAFNTdohCvaqBOTT9hOlgZLCpA96qQkAiFPnI_QLHAfWnrxaWRkdEHAS6PiiJCSPDdODsKHF7L4MDQbwBdSBGyA5ni01ZxeGAHK4UFNV06sh8XUFjWU-Qvviu2BHjj7Q8ZdjgpVrENMiwg0G7U821jXLYqmKOPbKnzJwYMU8RTYlzOxR5MtmBE9MCETjttgLDWa3Uugd1pSlh5DYIGpTkHq2beavgSsp60JV0MGvZPcOGdbvbWJGL1LlTTs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a433836c4.mp4?token=jO9WJDxQIAKlCDgXOBzZypbjIwSKq0HSW0ihMSmJc7qrCLWz5OmiibyrPmzNX7uOYkRMMucwwlce9_v4Wst2Coz6JFGQ-9NrgUUBBP4iLyInYWPWrztUgMUO1p_Q21r7uMCHdKcilSn0Tk_CwbswypAKHMTiCziqLCyQ9vjS2smCcBpPb0g4RVc7e0jkhfUvLtB3_e8sbF99DzuA14n1PPGhZBhFYQSpk_W-COy9dQ0fSrouIfuE3BSsIEVkysZvrMoWNDY0LSOp782JRWPVcGFIqGxd4DR9DiRss6njRv2L8XG-sn4uacNxSEsxnHfo5fiTaUWGOtqWk-7SOSDy-JelMwDhKSImU4qOd95sIzedNvpJbbG4md6e5ePIHNC05pxwQ6UEHcXmanoY7dzCVV2twvvTn0Vz29PUgYImg_w2fEYmcAFNTdohCvaqBOTT9hOlgZLCpA96qQkAiFPnI_QLHAfWnrxaWRkdEHAS6PiiJCSPDdODsKHF7L4MDQbwBdSBGyA5ni01ZxeGAHK4UFNV06sh8XUFjWU-Qvviu2BHjj7Q8ZdjgpVrENMiwg0G7U821jXLYqmKOPbKnzJwYMU8RTYlzOxR5MtmBE9MCETjttgLDWa3Uugd1pSlh5DYIGpTkHq2beavgSsp60JV0MGvZPcOGdbvbWJGL1LlTTs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
دل‌هارو ببریم به سمت بازی Pes2013
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/98155" target="_blank">📅 14:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98154">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">💥
▶️
عملکرد لامین‌یامال مقابل اتریش که هرکاری دلش خواست انجام داد بجز گلزنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/98154" target="_blank">📅 14:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98153">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2xS7AU2rC2I0qRkgK0EgwozgV9PS4Ep220YucQ4Co0kfKuhqKLp1w3cJ0jhUF5kB8FjY11qw4-LxR09Xmvw96OoOQTitSXAg22ii6OalKa2Ll-LjkspZp3O1cB6Fs5F09ebDvdea3lyK1PVH87ehdAey6I8jXnnyOmR7zOW0-YD3WolTHBlhNXDheF24uX8uEeedMEsF1lmsYLPZth1vAvOl97em0OrKXBVZtiSBQiVEQWnJDAptAfXM7CjL-83rar-yDIFcwYyCseGbbaQANFJpXUe3YP03eOH_F0Syqtrlg8NWtBo4wOeTNRL5RAEvIPLLv6E4WcKsvwJ9K3y6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بازیکنانی که تا به امروز بیشترین موقعیت را در جام جهانی خلق کرده اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/98153" target="_blank">📅 14:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98152">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGu2_WJ99jG3CFJUpI4yMChKNGSEe8WjEoxmUgamVBZijSXbc8ZnkeFSwXHUbubDf2zzBEURI4VlKz0T3dPfgyuv7Aksw01PCoaS_3hbv6ycbrFj5LkQgdzDpCc9Isqdcbto3fWBB8JcTv2TLev564HiCYDtXevFMjrNOd6daWtJNGR50pyeb1dRddXJVWE1w9m8QS7a4akbSitqlvikSkY1oS8Cw4z0MI2xQF7y_dMJ-hgvX4ysREPjWEFlZBhnEpruutRj3iVJ2UWWkWAWlf_VsWs-USkfreGVlHE_0br9cpJ-DIEbQMckKtOi5wA01eJLCyiUbYesXWIxf7OsWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب مرحله یک شانزدهم نهایی جام‌جهانی از نگاه سوفا اسکور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/98152" target="_blank">📅 14:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98151">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc006f9bf2.mp4?token=VorenHKBl6hvjA5Jizet2wUaORqiiZ7LgXeptbK-0knyih7i0iDKC8WT-z4naJQv6pF9GdU7zBGbnwa6ynitmgmRPLUFT5sLIsehARraWFLOphmXlEH_0GvY5iUYR1MBFVbyBa8yii6o9MzEuxWpgwVan3-HiSOsJSw84YmzZk-VAs9yVQBfaXN6Q7oKVipGi0TT-1lLr-H-9-yc5OHLjbYhp0SnK9Q4m4ylQZTXZEFepWlF8HF5IcyfDfXzBH9FAJT1rCz4lXsC0r6Iqblwcnm77SOf34uHID_adEJNr0kJknZs-pMOf1C5Kh12Thxrmm0PnygIVZ4EkWA8mDKTRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc006f9bf2.mp4?token=VorenHKBl6hvjA5Jizet2wUaORqiiZ7LgXeptbK-0knyih7i0iDKC8WT-z4naJQv6pF9GdU7zBGbnwa6ynitmgmRPLUFT5sLIsehARraWFLOphmXlEH_0GvY5iUYR1MBFVbyBa8yii6o9MzEuxWpgwVan3-HiSOsJSw84YmzZk-VAs9yVQBfaXN6Q7oKVipGi0TT-1lLr-H-9-yc5OHLjbYhp0SnK9Q4m4ylQZTXZEFepWlF8HF5IcyfDfXzBH9FAJT1rCz4lXsC0r6Iqblwcnm77SOf34uHID_adEJNr0kJknZs-pMOf1C5Kh12Thxrmm0PnygIVZ4EkWA8mDKTRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهرداد صدیقیان از فوتبال دیدن فقط زن و دختر بازیکنارو دنبال میکنه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/98151" target="_blank">📅 14:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98150">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6NDc7beKzSKPLwPlXG3g7urGJb6iSz9KgXvCGWJJV_DiWOpMQ_r9hnWBMyJ0avxNNZ-C8VAKwukEfhIFsWEKCiuGBazPX0lu-sJ8NMSaSNAPVVPE34AL60IlcxvGGrGCGhOqFWdwmnkA66AQIqx2zzdWNftSKeq_pNHX5509iCo8j_a5hJidSGfT7_wW-XGwWFs43kP8k-XaFnjOy_rQcfC1zLbl-dIdmcfIZMIDq29FRFAAYcQN-xHIibcbg-7OlKt9TQ9Pr9pYp6U7LiwxkodyoPoXkX_71Of2pAkcKjWkGTZb3CHnIYk1XdBoQ3PrYCqTODsvLksvJI7t8ue8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
جیانی اینفانتینو:
‏"در این جام جهانی، مسی با یک سبک فوق‌العاده و شگفت‌انگیز بازی می‌کند. ما او را به خوبی می‌شناسیم، او یک بازیکن نابغه است و همیشه خوشحال می‌شویم که او و سایر ستارگان را در زمین مسابقه ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98150" target="_blank">📅 13:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98149">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618fa5af23.mp4?token=kFI203u6FgN1oXY8CqYuP42c1yhGhCKC1-uXMUwVGi0MkYBINwrPghzIuPfjivKzDTey-uPY0yJlg-xE11kq2OFpGgvLdlUe9dtnzOoIzoartbfAul3URzGW06vWFBnUc5tTdVVkS4pqSXmQRaWlxggnADF4TKQPeR_nemvohXUEi8ppLvqV8iyLo-v2bYCQkuJkVY585Kh9epeE-5xNqWswZJSxrOVQLLAiXJv9bkAuBFQx6JX428HnjEon833gxqlfqv62_HnAoaUC4sG_BXni2qT-hIWeMykcj8yJwZJvbokBsXNgFgETzGKlGx8EsxvVANOvq86UmqQRFRGP8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618fa5af23.mp4?token=kFI203u6FgN1oXY8CqYuP42c1yhGhCKC1-uXMUwVGi0MkYBINwrPghzIuPfjivKzDTey-uPY0yJlg-xE11kq2OFpGgvLdlUe9dtnzOoIzoartbfAul3URzGW06vWFBnUc5tTdVVkS4pqSXmQRaWlxggnADF4TKQPeR_nemvohXUEi8ppLvqV8iyLo-v2bYCQkuJkVY585Kh9epeE-5xNqWswZJSxrOVQLLAiXJv9bkAuBFQx6JX428HnjEon833gxqlfqv62_HnAoaUC4sG_BXni2qT-hIWeMykcj8yJwZJvbokBsXNgFgETzGKlGx8EsxvVANOvq86UmqQRFRGP8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇨🇻
ووزینیا دروازبان کیپ ورد پس از درخشش مجدد برای کشورش مقابل آرژانتین:
"تقابل تک‌به‌تک با هر بازیکنی همیشه سخته، به‌خصوص با بازیکنی مثل مسی که فوق‌العاده خونسرده و قشنگ می‌دونه چطور فضاهای خالی رو پیدا کنه. برای همین مجبور بودم خودم رو آروم نگه دارم و تا آخرین ثانیه ممکن مقاومت کنم؛ خوشبختانه موفق شدم توپش رو مهار کنم.
بازی کردن مقابل مسی یا هر کدوم از بازیکنای آرژانتین همیشه خیلی سخته چون اونا بازیکنای تراز اول جهانی هستن. اما این رو هم دلم می‌خواد بگم که هم‌تیمی‌های من هم لیاقت این رو دارن که توی بزرگ‌ترین و بهترین لیگ‌های دنیا بازی کنن."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/98149" target="_blank">📅 13:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98148">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f3e951975.mp4?token=Y1VyQEDAT7rteTVk0sA9p1NoEEI0_MC4gqhE3v9PPQ0E4_ywBQmTvxZT4T3NgMMnPjjMlC079nXQDSn0ZpcdNLRM-Nyzs1wZaIUbqZuqGAxA2JZT2m5TyCvn-0J7aBaUZ0ZXRP0oc5x0tg2yKi1-T8234oMZFOqMb_PPlpsCcyrc0ygqp0PXFOC7FgsQDUthckz4NzW0oKGbKsl55ns_10CFcsn80wYsuF2BF34XnDJ4d_f8HPekn62e0EvIDC2B1PvR-zW5nnkb9cQky5t0vGv4Rl-ikzrxa0y1315QeD-m0s3y4GuhsQDuxw7TjEju793GnqUM-mQ98k39spPvFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f3e951975.mp4?token=Y1VyQEDAT7rteTVk0sA9p1NoEEI0_MC4gqhE3v9PPQ0E4_ywBQmTvxZT4T3NgMMnPjjMlC079nXQDSn0ZpcdNLRM-Nyzs1wZaIUbqZuqGAxA2JZT2m5TyCvn-0J7aBaUZ0ZXRP0oc5x0tg2yKi1-T8234oMZFOqMb_PPlpsCcyrc0ygqp0PXFOC7FgsQDUthckz4NzW0oKGbKsl55ns_10CFcsn80wYsuF2BF34XnDJ4d_f8HPekn62e0EvIDC2B1PvR-zW5nnkb9cQky5t0vGv4Rl-ikzrxa0y1315QeD-m0s3y4GuhsQDuxw7TjEju793GnqUM-mQ98k39spPvFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی
🇵🇹
پرتغال
🆚
اسپانیا
🇪🇸
از این نما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98148" target="_blank">📅 13:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98147">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FO-E7-GcD0T7tlYX-Wm5OwaffCjpLrzfOU4p3gBouJp9McJvMdjdkRpeTgM7n7gcNEaRJhUT24cDMnPuryYMDEgY6mHursIa4jaODUnCtj6IcYpgihHDLgVJE3J4C4bvM8I6p-GuzOHRlmoVxsLrRQOh7dQ9vOhP1HHDIBmZlMKOpqS3cxYiRl6TRk49pUclcKJAvo0y56JMPmuTjjRVxmqHbxZiP8MFqLH42kl5VmUnMiyy7fZ5vLRGkbi_GLuYYs81BQLo1yrEsqWlmIgTOLst1nMHsPpPNAwZSe6YlExw6Utu5YWWYS-aQswa3oChO3ptHdQ25DU2XufpSWoN8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
متن خبر: خداداد عزیزی دقایقی‌پیش مدعی منتفی شدن حضور اسکوچیچ در پرسپولیس شد
✔️
❗️
🤩
واقعیت در پرسپولیس: جنگ قدرت شدیدا در باشگاه شدت گرفته و چند نفر اصلی بدنبال فرو کردن گزینه‌های خودشون به نیمکت سرخپوشان هستند. صحبت‌های خداداد عزیزی هم با دستور زنوزی رخ…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/98147" target="_blank">📅 13:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98146">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f532fa68ef.mp4?token=Zl4ARoa66CiCXEpqh0n8J-3tlsnCA0eIvkdmhFuYC5KiBeoAia6wJEHPdz8jrBgmvUGIzGQUl0m-Ztp0KUvXIe_uDxmyeTEHtWCR13R-jYkhAPBURWVbNKsuhHMeWBJ3LhfQWl8YLR0x182rbjykdazIMdptTfRaNZIrdK-xj7OZFSJkCyrM-xZfjE6TMbtp2orgzKuxv8wc0Q8ZlS0ei4gHfXIW3k2OoJ11ef5zR8oS5mR2_1SVW1CWkvAyyVrXvewNpXPu4SmwfyOH2NqU-yR01anweV6Ugl8hw4rfgNUxsZFvjDr31aireJXA--Xy1_IxSPSvWfoQNOBp-veKXKVPKC2ElX3gxqFAgcQvTaktvwKFHEVoIGIgmlp0m-_1N1TFx1HZnWTB242b5qVKKiW9Yr6vJmCrtgkvsBRaYwTSUvbZJlS3SKq6shD97oGAOx9LYRWYeuA30dhYSG25djm_kWwBitD1m_KiELjR5JHNbS2B_P77eHr3m1viLeZXNsf8Viwa2hyiCjbMUzI8qyH_qN32HtmuQoDJGWV1LcM0Kgs4MXJYw2KmCGbTUKVvvSBZ_Eu5Ku-po4fbNSVZdT9LN49gKovs2pkxxmNkxUBoJHFAdLSpG556e-Sa4vqjxQb5xMwDmmf_NUb82YpsbBLnPQhRharSNWsHIjO582M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f532fa68ef.mp4?token=Zl4ARoa66CiCXEpqh0n8J-3tlsnCA0eIvkdmhFuYC5KiBeoAia6wJEHPdz8jrBgmvUGIzGQUl0m-Ztp0KUvXIe_uDxmyeTEHtWCR13R-jYkhAPBURWVbNKsuhHMeWBJ3LhfQWl8YLR0x182rbjykdazIMdptTfRaNZIrdK-xj7OZFSJkCyrM-xZfjE6TMbtp2orgzKuxv8wc0Q8ZlS0ei4gHfXIW3k2OoJ11ef5zR8oS5mR2_1SVW1CWkvAyyVrXvewNpXPu4SmwfyOH2NqU-yR01anweV6Ugl8hw4rfgNUxsZFvjDr31aireJXA--Xy1_IxSPSvWfoQNOBp-veKXKVPKC2ElX3gxqFAgcQvTaktvwKFHEVoIGIgmlp0m-_1N1TFx1HZnWTB242b5qVKKiW9Yr6vJmCrtgkvsBRaYwTSUvbZJlS3SKq6shD97oGAOx9LYRWYeuA30dhYSG25djm_kWwBitD1m_KiELjR5JHNbS2B_P77eHr3m1viLeZXNsf8Viwa2hyiCjbMUzI8qyH_qN32HtmuQoDJGWV1LcM0Kgs4MXJYw2KmCGbTUKVvvSBZ_Eu5Ku-po4fbNSVZdT9LN49gKovs2pkxxmNkxUBoJHFAdLSpG556e-Sa4vqjxQb5xMwDmmf_NUb82YpsbBLnPQhRharSNWsHIjO582M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇹
فرنوش جعفری گزارشگر دختر ایرانی: رونالدو قبل پنالتی گفت بسم‌الله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/98146" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98145">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilmGcWHbnkRLMeiWBowuuCE5jlQCMc4GRvqRZHsuIJOnnTAwds9NAJ2f4aIWZlFZzZvV9PJUA9-1Y1a6zirU-YffK65m3l-xNl9UUdISSMhFE3v0Nzu87lM_qNf1TTBJTrAPXSof4VhUe8MYpij7OkMd0x8XKqt13ndWR1sLuc0YySdTxoO_LIgnVL-69oOu9yL-ifQrbfpnU-1TSejiFigO1S6nFP7U6par71e3yUjP9s2woXtFLuRrDpM623xjRoUNuCBocvW3QPbY2PhgScjBhPO2jfX78pPbVk7NZL9N430xodBIzhr5rbNEN8pNZC7Ve2gUtMx7HX9iSa8S5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇫🇷
#
فوووووری
؛ شوامنی بدلیل مشکلات عضلانی در بازی امشب با پاراگوئه غایب خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/98145" target="_blank">📅 12:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98144">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1560d3443.mp4?token=ZGxiEXI40W_OZec3QHYSUBenVfGe0t8XvFke-V5EN1En-NRb0_HKgoomRcQjsywpIynkh5ngEgn-8r4kfLSSvBHM3TdEzqI57PNxjs9uZ4ZQV10yHxqGKtiO-0mVKcjQMriWYnlpD7QdEUPYa2mqKyUD20mXxNfJPsvyk1zWs4lg6vZDNYmUyWS3BQs3j_aVKKDeQLR_k2dz4xKGLe73s4fhM05nYSdUjlCsh2PkZBgPP4-ApqNGxcZ47yJFK2f_uEvO30Rr4IFJOofq-PPBzKaXXSlSmOyQKyHuBcJKIGrn5Ks4PTPPfZofhALV3zVj_AhmHX46WfX8g9afOIL7iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1560d3443.mp4?token=ZGxiEXI40W_OZec3QHYSUBenVfGe0t8XvFke-V5EN1En-NRb0_HKgoomRcQjsywpIynkh5ngEgn-8r4kfLSSvBHM3TdEzqI57PNxjs9uZ4ZQV10yHxqGKtiO-0mVKcjQMriWYnlpD7QdEUPYa2mqKyUD20mXxNfJPsvyk1zWs4lg6vZDNYmUyWS3BQs3j_aVKKDeQLR_k2dz4xKGLe73s4fhM05nYSdUjlCsh2PkZBgPP4-ApqNGxcZ47yJFK2f_uEvO30Rr4IFJOofq-PPBzKaXXSlSmOyQKyHuBcJKIGrn5Ks4PTPPfZofhALV3zVj_AhmHX46WfX8g9afOIL7iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
👀
دیس هادی حجازی‌فر به حسین‌میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/98144" target="_blank">📅 12:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98143">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e644ac1b7.mp4?token=chKQJ2LsLY83BsNfbSVwS8nhvLywd__REWLVQ8Q4Rqrw3XfBv4CQWjv5fOBS1eAZYh7uigLB6IMjyrTM-veZXiIzLMkggTfwiV1_Pig2flm980oH8jgVscFFbV9uh_zOXd1t5X3rupgvpHhMHRAzl40bW3MvZQmheApEo8f9tUSbVT29gXX_QVG4-MEd-yVDPyyfCnME8mF5zP6VaWtrf4JiodJ4550bNEM9U--uACUUt_EoNPdGCpBCYQciFWNejk6jGnBprQr5Y_8bzX_qvSqkrcMeMp9EV_PRcaqMY18BNfNRy4rQnE1T_vOaj4Ql3ipp4xrldvos0WnBJAVgEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e644ac1b7.mp4?token=chKQJ2LsLY83BsNfbSVwS8nhvLywd__REWLVQ8Q4Rqrw3XfBv4CQWjv5fOBS1eAZYh7uigLB6IMjyrTM-veZXiIzLMkggTfwiV1_Pig2flm980oH8jgVscFFbV9uh_zOXd1t5X3rupgvpHhMHRAzl40bW3MvZQmheApEo8f9tUSbVT29gXX_QVG4-MEd-yVDPyyfCnME8mF5zP6VaWtrf4JiodJ4550bNEM9U--uACUUt_EoNPdGCpBCYQciFWNejk6jGnBprQr5Y_8bzX_qvSqkrcMeMp9EV_PRcaqMY18BNfNRy4rQnE1T_vOaj4Ql3ipp4xrldvos0WnBJAVgEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇲🇽
رییس جمهور مکزیک: از مردم میخوام اگه جلو انگلیس بردیم، زیاد مشروبات الکلی نخورن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/98143" target="_blank">📅 12:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98141">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32c0e1238c.mp4?token=qXIkrrqHRhLBPdLAQh5hcKBnMUw2sKDWq3FdVU7uZn5tgkncItMh9_8WkD9NgUMLzTmn8L0_WQWJxEDXZAyB_Poh1XRw6HV4hOvbtMIfFczBmC8DfgJI-sYHLmjdLUAczqga0_0_p6apGC9QOwpqbLUZgCcq8jt_NKDaCz2b2v9U2gWe7rShDuJ9QIZxK5jupsHM3h1_r8gtjJF29yCeC94wOWXBZc_UCnH-H7zVrM_gLXYCeqZs48scjEW4L8d0qWKJaindtc0yrtVtzaI8t1b6KJYUKifiRcuHoJkH512bzMMJCll8tW6JMQQkrj9N_aTIzcw6jS6BHFRWCFrBEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32c0e1238c.mp4?token=qXIkrrqHRhLBPdLAQh5hcKBnMUw2sKDWq3FdVU7uZn5tgkncItMh9_8WkD9NgUMLzTmn8L0_WQWJxEDXZAyB_Poh1XRw6HV4hOvbtMIfFczBmC8DfgJI-sYHLmjdLUAczqga0_0_p6apGC9QOwpqbLUZgCcq8jt_NKDaCz2b2v9U2gWe7rShDuJ9QIZxK5jupsHM3h1_r8gtjJF29yCeC94wOWXBZc_UCnH-H7zVrM_gLXYCeqZs48scjEW4L8d0qWKJaindtc0yrtVtzaI8t1b6KJYUKifiRcuHoJkH512bzMMJCll8tW6JMQQkrj9N_aTIzcw6jS6BHFRWCFrBEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇵🇹
رونالدو با ارسال ویدیویی به پسر بچه‌ی ونزوئلایی که از زلزله جان سالم بدر برد ولی تمام خانوادش بعلاوه یه پاشو از دست داد، از اون دعوت کرد که یکی از بازیاشو از نزدیک ببینه اون پسر هم توی بیمارستان این کلیپ رو دید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/98141" target="_blank">📅 12:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98140">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe8d2196b.mp4?token=kwICqYeusKM_CA3ZBi_wAzt_Se9QsWDAUnLC6thf1Xy-OyRi23p1_PvRyVG-R7v6ScjT8tVuiuOZKLrglSsWxHnwdXjwzQKpQ5-SCk1SxT-sEYOB8YIDq6Vb41IpfSx_vUbFNiAa0lsqREoZr7ik5-1Jp_5U5mUClvPnxdVzZgVTQA7ddoI74C-MBBe7ijlLlUTBuCiI9vj17W5e3BmIjMCIa7jmWBNH1gHbhHk35PS7YIBJjPNS1pDhPGV7kME3R9SuHOpolEP-ITlhYn3MihJpANIeJfde70899Qyk8u6SKlqKOU9TQd_5fSqlX4dnCPvdymUXPk4fh4Os6njDuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe8d2196b.mp4?token=kwICqYeusKM_CA3ZBi_wAzt_Se9QsWDAUnLC6thf1Xy-OyRi23p1_PvRyVG-R7v6ScjT8tVuiuOZKLrglSsWxHnwdXjwzQKpQ5-SCk1SxT-sEYOB8YIDq6Vb41IpfSx_vUbFNiAa0lsqREoZr7ik5-1Jp_5U5mUClvPnxdVzZgVTQA7ddoI74C-MBBe7ijlLlUTBuCiI9vj17W5e3BmIjMCIa7jmWBNH1gHbhHk35PS7YIBJjPNS1pDhPGV7kME3R9SuHOpolEP-ITlhYn3MihJpANIeJfde70899Qyk8u6SKlqKOU9TQd_5fSqlX4dnCPvdymUXPk4fh4Os6njDuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
تکرار ادعاهای کسشر فتح الله زاده در گفتگو گو با ابوطالب حسینی: اگر مدیرعامل بودم مسی را می‌آوردم…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98140" target="_blank">📅 12:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98138">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iznUpdTCaT4nHhXsh17hWDAINUJnZNDKYWeV2CfdpyxpJltEn5j3jUkDnWLntFRqirgXC2UN4zMeEBSoZQ8k_HykObqGyx05K_bE9y72i8l2fy8WeghjAZEI9Ne8CFaKdxqglYxkoNNCLaKcASGWHtIKFiwt4zog-ThDNy9Oa76wbNPILvnpvcd7M8-8L_p-zDRWOYKE_fnoY7MVlQ6CHk5tQDOdrj0SjNHr4Tf-XPlsa8SU8ZMrqJU6hyHFyHLrztL4Cjj-muLfOsla01y1yu88mq84vRzNqzuqik9c9eNPyfFlIsBC0gamTT8s22Xt-_YiZUiQEXGcQ69Fl2jsAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OU8Rrd7PpygMjnRFNKHbrp3A_fC4pt03WmKOLd5uuqf3k4ICyICozpZXc7FvfphhnRWxPoyb4vkrBs4UIfeVmVa0-D_-fOirpwUP0rbPfQDtIi5L5bjcDMX7e4nAc11pot8m-gIfryDw2hGcwcDK-GmY_QwIY-QxaScvJ-xRmPXtxL1B9rmP-h86RjnjT6ycLd3dQKzEN_e_wS0ntDg4Sh436x6Iso8xgRUiTOBGEVFB6gkkVEV8rQINbWYIBNvYOWk0BTOABSXYap9R_gIkjRtHrRBJ6d5l4aaXCeMWIIzCJ9pc3_nbJS8AHQhE8C0FeN79Hqmv1rNdgk2g3ciIQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هتل "انگلیس" در مکزیکو سیتی، به دلیل نگرانی از احتمال ایجاد مزاحمت و اخلال در کار تیم توسط هواداران مکزیکی قبل از بازی، با تدابیر امنیتی شدید و یک "حلقه فولادی" محافظت می‌شود. نیروهای پلیس، واحدهای ضد شورش، موانع ترافیکی و گشت‌های یگان‌های ویژه ارتش در اطراف هتل مستقر شده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/98138" target="_blank">📅 11:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98137">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7c8cb22e4.mp4?token=KxsWOd53E1AZcadomeSoE9M4soUn5EEWCXwdyIRP_NF1JU167LZHiPYnkyUdUCQ9aboH6-HMN9miRk2OsGyzY0M1T0RopnvedK_HH41KCXFiQsTEC9S7eZWvHt7MpYvdkg2uu-JH7bSu9KQC83FA-qWcjTpg--q_hmuzxYXgn2s9l7Aor71JMctO_8-uCkBTQ6jDCe037ipU56F5-G3e0rlZjXcOYyMOkeGRVuIdXbcM6bvhKTfb3X7A45eLkFcZh3QD4c-iN6OT_SDiqwWnd1ty9YuGX_GkbTvpmc-TiKIkC07PBOFehSNR_fEljhZjoo4ruu6ze_xGmIPGCPt-uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7c8cb22e4.mp4?token=KxsWOd53E1AZcadomeSoE9M4soUn5EEWCXwdyIRP_NF1JU167LZHiPYnkyUdUCQ9aboH6-HMN9miRk2OsGyzY0M1T0RopnvedK_HH41KCXFiQsTEC9S7eZWvHt7MpYvdkg2uu-JH7bSu9KQC83FA-qWcjTpg--q_hmuzxYXgn2s9l7Aor71JMctO_8-uCkBTQ6jDCe037ipU56F5-G3e0rlZjXcOYyMOkeGRVuIdXbcM6bvhKTfb3X7A45eLkFcZh3QD4c-iN6OT_SDiqwWnd1ty9YuGX_GkbTvpmc-TiKIkC07PBOFehSNR_fEljhZjoo4ruu6ze_xGmIPGCPt-uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
😎
بهترین گل‌ فعلی جام‌جهانی از این زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/98137" target="_blank">📅 11:20 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
