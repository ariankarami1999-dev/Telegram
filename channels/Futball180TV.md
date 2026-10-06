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
<img src="https://cdn5.telesco.pe/file/GQGCdiZ2bZEoy6VL64pwvv3z5mhHDoYb87pC8Uh0NL1-_qY3F7yv_mTe4VM7BCRkn4VdZxly7ISchRKtj8u_4t5uZWN10rJq1q1Pt0qVFD-ZpJFHLy6-ZK4nsJ98gQh0oqQgAF0F8CK2QCC5BTucryJ2wKVKm0caDZ4c917yVj1SA4NZ4b-p6RgRObTf5eQeGABfDDcP8zvE_IMWP-QXMY68gSSuDw03ZMUc-7z7fExPGXAz7MKNnVjPZbZx2FVTQNqcdRCeSqun0NRNB9uqDQZ3t8jqLlwGFZ3lTMZNZzgk07c0yvsvoniyv7UlD8rQiZTleTIVt_SBPWmD_PExmg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 390K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 10:14:23</div>
<hr>

<div class="tg-post" id="msg-107901">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 124 · <a href="https://t.me/Futball180TV/107901" target="_blank">📅 10:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107900">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/107900" target="_blank">📅 09:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107899">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/Futball180TV/107899" target="_blank">📅 09:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107898">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/Futball180TV/107898" target="_blank">📅 09:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107897">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25bf4f2e86.mp4?token=BM27WSmj_iyI7yybEg88Q0Y2iJELs6Tj0HDDoGqpI5tTNsMHigUcjRz_m6O7_P3gKjagoYcSBTQP0_xkMHayPXt9XOq0pFu7p7S2EGJbyONB4iOOQwBGplpEaukuXw9SkPLubuAULdWT_5Rv7CX0C30weMrIDAdNKdEUUkCAXlEIr4JDljpZcCSaTO89n0FNFgh-ytE_9WGKfv6Vjk8memJz8lNB6yNzmH5drIiFvetEUwR94DE5fzO7xT-Z3kvt1W96o8GVRSzu74zld1KJUctyX8wX_wWyikFglAq6tlA2qjTTOtb3gnkQcGjdNIsR7hnT4PKunBez17lod12_5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25bf4f2e86.mp4?token=BM27WSmj_iyI7yybEg88Q0Y2iJELs6Tj0HDDoGqpI5tTNsMHigUcjRz_m6O7_P3gKjagoYcSBTQP0_xkMHayPXt9XOq0pFu7p7S2EGJbyONB4iOOQwBGplpEaukuXw9SkPLubuAULdWT_5Rv7CX0C30weMrIDAdNKdEUUkCAXlEIr4JDljpZcCSaTO89n0FNFgh-ytE_9WGKfv6Vjk8memJz8lNB6yNzmH5drIiFvetEUwR94DE5fzO7xT-Z3kvt1W96o8GVRSzu74zld1KJUctyX8wX_wWyikFglAq6tlA2qjTTOtb3gnkQcGjdNIsR7hnT4PKunBez17lod12_5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
حجت کریمی توهین کرد، علی خطیر تهدید؛ کریمی: تو دلالی، خطیر: دادگاه می بینمت!
❌
درگیری شدید دو عضو هیات رییسه پیش چشم سخنگوی فدراسیون فوتبال در برنامه زنده تلویزیونی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/Futball180TV/107897" target="_blank">📅 08:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107896">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4798a06f34.mp4?token=vu9dNXQiVmfqZv5jroLotiAiwzhEzpACwcVTb-0k-fpjUHWOjM3t2lXAb_q27kRshZo0eeR33N4gXXBAEXhq7t9QrJAVbSMJZViuxUtT6k4G_7qOanxBM4B5KMqt-3KQHX2OvzEgB8s-89ahdPjmxL2gOo4rTbGNuCiE0dQRsZz5JmkZDPf4SOKAvXPRMPSpYx-PUCVKdhDEsBXmYShiJkMkLlOxiTcWQEuWmzv8-gOCjFwUMGINka42yEZsEiQSPkT3DxlRDLrqzbb6CmdrYdlM-mvMGmGiw00DulAbVZ5v9ja9oQSvWW-RYZmK3eOueAqlYvBL3Iw7a580hlTFMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4798a06f34.mp4?token=vu9dNXQiVmfqZv5jroLotiAiwzhEzpACwcVTb-0k-fpjUHWOjM3t2lXAb_q27kRshZo0eeR33N4gXXBAEXhq7t9QrJAVbSMJZViuxUtT6k4G_7qOanxBM4B5KMqt-3KQHX2OvzEgB8s-89ahdPjmxL2gOo4rTbGNuCiE0dQRsZz5JmkZDPf4SOKAvXPRMPSpYx-PUCVKdhDEsBXmYShiJkMkLlOxiTcWQEuWmzv8-gOCjFwUMGINka42yEZsEiQSPkT3DxlRDLrqzbb6CmdrYdlM-mvMGmGiw00DulAbVZ5v9ja9oQSvWW-RYZmK3eOueAqlYvBL3Iw7a580hlTFMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
خطیر: اگر آقای گل‌محمدی قبول کنند من همین فردا کل هیئت رئیسه را متقاعد خواهم کرد
خطیر: هیچ مربی ایرانی با ماهی 500 میلیون تومان سرمربی تیم ملی امید نمی شود! کمترین دستمزد مربی در ایران 70 میلیار است کدام مربی سرمربیگری تیم امید را قبول می کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/Futball180TV/107896" target="_blank">📅 08:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107895">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107895" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/107895" target="_blank">📅 01:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107894">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwX-JNmSqlWItURMzCM03reFTp8zdM-Z3RMZm3JuRGCCZzg1I_n0WV98EDE9XUM45LSTiPealPd_2uHM_fx3-rCYH47V6ATlo1K-F7X8C_r-1RKoY1WMHCWnLx49R2Dr8NEb8P3HDojXFAIegoxde3Xdi2JH9sgldaCBrmhd1UUGezB26tdKznAc_8rO58Up4MRXTdHDcm4mpoTLedJ1Gegby3z3E5duTgGrtcH7JtTwk9xgYUj1gpBF7XJ7mj5V03t8OZIB7roojdWDJ6il1c81GLGp76HkShGyFcRSK6R-Bq-d4ZzmvWjtpwGKHKX13YANiJthrK4i_2UAEistQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/107894" target="_blank">📅 01:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107893">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/107893" target="_blank">📅 01:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107892">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3867ed322d.mp4?token=rTS-PA0lAbZtxj_1CNlkUt3fxMxO-uXOxXEQWnDFmzRJ-9C-Nkl7qvaZgnJ87AqQAYOEPUHnJVGRTLuyh1jFy1_Hcm6a3p9jQrbSDZIrpcfJDEjguET41s0fdoHd5AxphosYzZlJI_NQ87Kt_eUJJyNMmuUVOW2G4rFUlwOtWLx8wLvvg39CDFS8OhWOnsdmKZvac-C9vRVPbyxU5t7S9H1KhBexp8RAEbUI4cOI7DJoA7dIXrVJc7_v4oBys5sIy8LDa6RDgILC6hjO4iaChM4SbdjmnhAPrZPiZbzo1t1IpkumhkqADkTxhGXV4eDyTP_5uNuIsG5i5vseK6fJ7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3867ed322d.mp4?token=rTS-PA0lAbZtxj_1CNlkUt3fxMxO-uXOxXEQWnDFmzRJ-9C-Nkl7qvaZgnJ87AqQAYOEPUHnJVGRTLuyh1jFy1_Hcm6a3p9jQrbSDZIrpcfJDEjguET41s0fdoHd5AxphosYzZlJI_NQ87Kt_eUJJyNMmuUVOW2G4rFUlwOtWLx8wLvvg39CDFS8OhWOnsdmKZvac-C9vRVPbyxU5t7S9H1KhBexp8RAEbUI4cOI7DJoA7dIXrVJc7_v4oBys5sIy8LDa6RDgILC6hjO4iaChM4SbdjmnhAPrZPiZbzo1t1IpkumhkqADkTxhGXV4eDyTP_5uNuIsG5i5vseK6fJ7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
لحظاتی رمانتیک و شبه هندی در شبکه سه
روبوسی های واعظ آشتیانی و علی خطیر در پخش زنده
😂
پی نوشت: گفتنی‌ست در لحظاتی از این برنامه واعظ آشتیانی و علی خطیر با یکدیگر درگیری های لفظی داشتند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/107892" target="_blank">📅 00:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107890">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DA2_TcVh-61UP4cIUWpTIAC-keAgFJ_TBbRdbayX1XHGGa0k94spVT9WDl3UDdU-OOnb5KvBYY2N_23HQRn0FF8060hmwrg4tg35vdkVUYix9YfHyIKnrqE2r6usohuWIwtdSKtR0q2Ntaj5T08y60u2h0MykDg-57N_ADwrUgNWClf4kaeGekWqX-QTU_cDbcS07QtgAvwGpjZwtAQbELj_MHRLzOzHjThWSqnsaforuRFpN6ZYyUhZRiLsi1iMHup5GxwAiOuKuW41Q2uBxbLKB6IQ5XRRIjSrzusmaS3oFzQP3rSBLLInPR_2uES8vYfXAiOJT0qTslJWkdxOgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ttXQv15h1wEUqB_yG5ZK0bnkIb3HiYU7pWqDMhZljg9uT8rjUJi5QtJc672ntWnV3YG8JEoWmKsTiOZJsFuqCIKYjL2iyLjNYySDQNV0NC3ZhJjK3rYk9dNSUMlRQ5cFQBKvSzVWTF_jz0EaR5qEuxYBnX9CGLWd8ONu_7DDsV7xAUSA8jhcVRJLgHoPC17nYLEq-fm4_pgiTorRv-9zToGgETRdECtgyx27B4JKhikN0SElFe5nqag0RsQWfKimUQxHBOJLKlILORJJJ32tBQ-qwHsIVfBYlRK0bAUh4UhTMLFhDrQ5F05L--QxEhIGuphUxhUCHvx0HMtWIHt00Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
ترامپ: نمی‌تونیم جلوی شیوع طاعون از روسیه رو بگیریم!  این ویروس بسیار کشنده و خطرناک‌تر از قبل شده و مثل یه ارتش شدن! حتی با پیشرفت چشمگیر پزشکی هم نمیشه جلوشو گرفت، با این حال ما به روسیه کمک میکنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107890" target="_blank">📅 00:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107889">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7gjzl6XiwoHfqx4yWaaLnvltGBzQBE9zieu6EqSXNFRkZJedtLGnY5LKwFO3DmHCpSyzoMVs1Mril9R8DPOoqE4b5mJSM_TJ0DlgKDHNIUfddKXynjkwWu5oej8gz7hvLh-P21NdlCwQBAPXcbzGIMDVVQdvNeN-aUr38c_DbAtB9DbAryy-OFKL8Dzb_X2MFw4v4CkT4pHObfZ-D3UwKP0ayAUAo_KsoZl875k_A22xJ4lIDTNuDOZBWzkvWUGBSU_p1wRb-HjP15MPnyk7g4ekdimJhd56R6Z089LIQ06R61Gxc4gsHqnD_an1fsxgkknQBUN-BVcrowZIs9akg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107889" target="_blank">📅 00:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107888">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3c5cdf08.mp4?token=UaVnv1t33bObEJ2Emdk7oyzaXOOMg7F533hfb9iOiolQ4zpyUBcs-mqtYJ3Pr8e9zuPfI-1DwZsJ6LjeZbJQP0QvTx4Wc_6CLRRqJMPxb4GwaQGE6xHYEYBtpo7gEpQhpt9ftpmX_5GQO_QSO5TBoT_tFGJt8U0z9stZa1kGZLwKieGTId1SOsQI6ZlzW4Yj8PvlX7Dy938nrnZjw2VZvPIAYhAoyCjNBIEhi4weyxIbLmXpvk_PeCSXXXvEBVR2ofldBSoSKNOplJNFrQp_EowfqQPASKdGeZqFqDzbv7-V6TCahA-XiuFHrTeFKRDQwhGZxqeYEEgTkS3IWfqxD4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3c5cdf08.mp4?token=UaVnv1t33bObEJ2Emdk7oyzaXOOMg7F533hfb9iOiolQ4zpyUBcs-mqtYJ3Pr8e9zuPfI-1DwZsJ6LjeZbJQP0QvTx4Wc_6CLRRqJMPxb4GwaQGE6xHYEYBtpo7gEpQhpt9ftpmX_5GQO_QSO5TBoT_tFGJt8U0z9stZa1kGZLwKieGTId1SOsQI6ZlzW4Yj8PvlX7Dy938nrnZjw2VZvPIAYhAoyCjNBIEhi4weyxIbLmXpvk_PeCSXXXvEBVR2ofldBSoSKNOplJNFrQp_EowfqQPASKdGeZqFqDzbv7-V6TCahA-XiuFHrTeFKRDQwhGZxqeYEEgTkS3IWfqxD4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/107888" target="_blank">📅 00:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107887">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff62591c17.mp4?token=aGN4iEz8qESQi_ZgpH6tki6PJFTXxCb6JP8UX3IYO8n8eQndxFZ50eGoPUY69pxPV_8OQjMrL0yiOlmElC6ADaW0bK6LbWGjzFUgqU58Lxgaz2xWcw8w3zkyMUZqKQjGozdP-VKZlES0bATVmZzOtWD93El3zwPRGZ31yqSkgmaKxjVb1vhJacwfvpKVInjOV_NsIEOHVs6LgKjnHnwI2dqNkuP81tfH6w0VryNeX8yuQi8-v703ol9XMtduLiuUEXxKcLm-Tzv7B7AWG5zgx6MwEULdwzty6NJ9E65R8Zl62WyZjNiNkkkM0jvTpFTFhVXyOaOV_a0ReY4CCVYuKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff62591c17.mp4?token=aGN4iEz8qESQi_ZgpH6tki6PJFTXxCb6JP8UX3IYO8n8eQndxFZ50eGoPUY69pxPV_8OQjMrL0yiOlmElC6ADaW0bK6LbWGjzFUgqU58Lxgaz2xWcw8w3zkyMUZqKQjGozdP-VKZlES0bATVmZzOtWD93El3zwPRGZ31yqSkgmaKxjVb1vhJacwfvpKVInjOV_NsIEOHVs6LgKjnHnwI2dqNkuP81tfH6w0VryNeX8yuQi8-v703ol9XMtduLiuUEXxKcLm-Tzv7B7AWG5zgx6MwEULdwzty6NJ9E65R8Zl62WyZjNiNkkkM0jvTpFTFhVXyOaOV_a0ReY4CCVYuKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚨
‼️
میثاقی
: فیفادی واسه تیم ملی ایران بعد از بازی دوم تموم شد، درحالیکه ژاپن همین امروز بازی داشت و خیلی از تیمای جهان 4 تا بازی انجام دادن. قرار بود تیم ملی با گینه بیسائو بازی کنه، دیدن تیمه 3 تا به نیجریه زده، بازی رو کنسل کردن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107887" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107886">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WywV-WEJW33r2J3F6xhtmRWz8NCT_EK16fAb8KFTPH_H5Qg1HaD2JycHjI89p-tiw4zt6bZD7-NSIt30USCealOJDYAPJWa9Kh2XBNiVZf1n6G6g-oPPSyOHcb1ev0SXbumqyGa8mytZ35AZtqBbDBqsewr2p-unnU-2Qxr5700Psijou-GiIH2-QySD305toutBsE2vamFKtkEyndN1CzqsViTKlHYia4d9ukxXMdypyBGizHrAy7qRw1IWqEiyUTBI03HP_Vu1-APmXsr6NtLGQwf_u52su9e0Wl5YSCd0xEqfL-VHdZi4zWhy8mBBDEYQJxC9CdPLHLTM-M81wg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107886" target="_blank">📅 00:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107885">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZJwGVq8OvyqlHJUStYuDL-DpREOmAjF4XGQIquzhaL-hXh5hVHqSEi25CJQvC7I5Y-g-xK6KD4ZIX6XWjhO7CfoHxiCmkjRqc2noJ86oNSTzDy9tG-NkmnqgBtENe2ce1NpPW6xvzV3kc7s7wuOp7jvxPYRjcoiA9k12xNsW0bwhtj-1NiJnhUqFclTvmiXQMpCmgiK1KjPiMTKb-J3S8RfR_4ToMRjVVKRTMmYU_nIyJjK4aDJ4K29NqlORpQqhXMnitGmJ10mF_jUfeYydvB1swyvW0q1wSzfuE9rHf4Ff1TBHAuavPDDZx0_ue6Ga6w-apo-UYGrdIrYIaibcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107885" target="_blank">📅 00:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107884">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tra_vJ-vL2E9EF2hsgdPznU9rSE640xrSVMya9s0es0Lcl9ssof5VivFbQJxu67CVidbdYmFe0CE1VtSIdDfBGLVTmdBHG9Og-buUEe-IOTceRDhwQq1uSIaFv0Q5IvW839E8rS-FOS5hMp8TkfK-XjXVh83gN9M4L2YZijs-VxFQO3rfL3NBdDRBznGPhsESabAUxg0_8LYsST_GDRjsEPEMoelWyPhO_y1ndg7cybbECPnCLKNlfC8rrLj90778cc8n_WME9l3XHbVLCKp9kC2H2Xm15N2gY6Z3LsHlifCcr7NJThQcza_QqZ2O7UD0xNsJrT5sWXJRHQIuLqcew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107884" target="_blank">📅 00:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107883">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25f8a10c9e.mp4?token=B11xSgLavZXr4Y1RrL6SEXDKfziAtbzPKNaKlHyjOCoKyZt_tZ2LvoeAnYLEiNdYQjSMRtYuWEaX34iseXbp_yPDZq3aNG_yOC97lBy833wyuae6E5wJ4A2005zJkdrBj5YPfNawGNe9bwnYWqxrQpvyJRBP5Y5DD8ALAwLm2-DUfbOkUIfunMIvzN7I8Lk4D7r0JtTjQf9JcjUEu5WIWgzR0_xrDCscO6miD6zmG7dT7n-TtC5ACSaqssk5LfxuLG9Lz6TLKmxCTeA0UjPwJ1Em_kl1nVXoSX65jTVCGnyBc7QhdK5l2YJ8XzMXye8WJm58Jc3UH8-iKxH6Y5yS7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25f8a10c9e.mp4?token=B11xSgLavZXr4Y1RrL6SEXDKfziAtbzPKNaKlHyjOCoKyZt_tZ2LvoeAnYLEiNdYQjSMRtYuWEaX34iseXbp_yPDZq3aNG_yOC97lBy833wyuae6E5wJ4A2005zJkdrBj5YPfNawGNe9bwnYWqxrQpvyJRBP5Y5DD8ALAwLm2-DUfbOkUIfunMIvzN7I8Lk4D7r0JtTjQf9JcjUEu5WIWgzR0_xrDCscO6miD6zmG7dT7n-TtC5ACSaqssk5LfxuLG9Lz6TLKmxCTeA0UjPwJ1Em_kl1nVXoSX65jTVCGnyBc7QhdK5l2YJ8XzMXye8WJm58Jc3UH8-iKxH6Y5yS7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ترامپ: نمی‌تونیم جلوی شیوع طاعون از روسیه رو بگیریم!
این ویروس بسیار کشنده و خطرناک‌تر از قبل شده و مثل یه ارتش شدن!
حتی با پیشرفت چشمگیر پزشکی هم نمیشه جلوشو گرفت، با این حال ما به روسیه کمک میکنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107883" target="_blank">📅 00:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107882">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bb309807.mp4?token=RRllumQrhebaAjfWapq2Dk6TUAcVnVQgj9cRrhSdxBczp8qv6oIct4ggoBMa2-6aNJ4O1kkGgjiYhfu7i7Ugch3ybQEE_bhG4Im4b1oa8qJpzobUwjsAyx-tSVcMXLbAomhaPt4ijgT22sKaq9eBE3ilLz08fjP3Q8suF70XR_ZcbN5EkOMg-XmJUCl--jRQubJMIOt5yZ-vgQIIBc67D1EWTmiR0Ze4doqDKCMKZiVeK-WiE1rbDWyJ8pUntVTdCGLuSirtIXv0_F8UrTJewJgb38PQrz_iwkgbvfZ6Xoc02GDWt-RrlaaQTXPr-122rlo3-P2tf8Y_s3VRSoHSog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bb309807.mp4?token=RRllumQrhebaAjfWapq2Dk6TUAcVnVQgj9cRrhSdxBczp8qv6oIct4ggoBMa2-6aNJ4O1kkGgjiYhfu7i7Ugch3ybQEE_bhG4Im4b1oa8qJpzobUwjsAyx-tSVcMXLbAomhaPt4ijgT22sKaq9eBE3ilLz08fjP3Q8suF70XR_ZcbN5EkOMg-XmJUCl--jRQubJMIOt5yZ-vgQIIBc67D1EWTmiR0Ze4doqDKCMKZiVeK-WiE1rbDWyJ8pUntVTdCGLuSirtIXv0_F8UrTJewJgb38PQrz_iwkgbvfZ6Xoc02GDWt-RrlaaQTXPr-122rlo3-P2tf8Y_s3VRSoHSog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
خاطره امیرمحمد رزاقی‌نیا از هم‌اتاقی بودن با رامین رضاییان: سنش را بگویم ناراحت می‌شود ولی مثل یک جوان 24 ساله تمرین می‌کند و در دویدن باهم کل‌کل داشتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107882" target="_blank">📅 23:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107881">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d63f949c.mp4?token=NazhgcjfXkvU5cLHJ9gJaGAb-1Ff7EF9XiDHHvqmjExxiExM_H3PidTzZVLy4PVITS8kvMOIpSiAQo70kMGjcOmo3auRm_qf4mJPhWdPpxOD6O0WifCr0oUPNAGiuOw3D48n0wImXJu7kunG9KxpAMoDCJUgArE03kCnnVV-Vq1vkYB3iNlbVLhuzfTL1_0A3T2-9mdaYuFxJ2GUvxfpNmjztQu4tnQ1Senyo6a_IDnXhb8P4x8zA0eoZ8AuHpqqg2-6g3VfIhGAcDttAhlQMVNqNCADILvmlLjqt6cBrdKRUPK-lz4JzDG7L0miYssLpL3r72RXSulZJNlV06av8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d63f949c.mp4?token=NazhgcjfXkvU5cLHJ9gJaGAb-1Ff7EF9XiDHHvqmjExxiExM_H3PidTzZVLy4PVITS8kvMOIpSiAQo70kMGjcOmo3auRm_qf4mJPhWdPpxOD6O0WifCr0oUPNAGiuOw3D48n0wImXJu7kunG9KxpAMoDCJUgArE03kCnnVV-Vq1vkYB3iNlbVLhuzfTL1_0A3T2-9mdaYuFxJ2GUvxfpNmjztQu4tnQ1Senyo6a_IDnXhb8P4x8zA0eoZ8AuHpqqg2-6g3VfIhGAcDttAhlQMVNqNCADILvmlLjqt6cBrdKRUPK-lz4JzDG7L0miYssLpL3r72RXSulZJNlV06av8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
سنگین ترین پرونده مهریه ایران اعلام شد:
اقای جراح ۶۳۶۰ سکه مهریه برای خانم با وفاش زده بوده و الانم تو زندانه
+ تا چند نسل قبل و بعدش هم جمع بشن نمیتونن اینو پرداخت کنن
😕
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107881" target="_blank">📅 22:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107880">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
‼️
🇮🇷
بعد از پیمان حدادی، موبایل همراه مهدی تارتار سرمربی پرسپولیس پس از تمرین امروز سرخپوشان به سرقت رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107880" target="_blank">📅 22:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107879">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1743ee1f5a.mp4?token=O2E3tnn701r5kInk7SA7OBrPBdBaoFnSeJHMa5dYsJ2IV1aGxpQK8zJiOgLYNbl9WCHLFzqQ0j8q6gvM8OYgf149wz6MSOtuW_saSRLBPeUTqYgIVla8okrRK2fYMUNipGDIumvYbV1nGzYlDvU_wCgtY2TyujYks5vR6cTk3-g5bhETdjdHWg5yEkLRcXT4BSerH1mYWktjS2sNkW6n4kwdGOn7SoLz-CvCWfdLLJ_EQNrFvYBSf2CUgHZDx8nKo-IlK0eRwd42fnauGtcAwvG9JdGem1b4MnYFPsQNiNQVaVI_8-iq6LOv4xyhb0UEShZJjU-yRfjaKhUJ8-hmkFUmAhOS9FPUVaFTnxMKOJu28gI_yHtoVlHS-lf35S8uel_0Eo6-YknEZUlv5HbRIHvbIVtHDbaC9fwpW20-q7flCG99qNQqC9HNTNnoaGApBAGjePzScijyWutMxTjJN2geXhupv_8S8swStnLzx3CK1Hvr85IgKhlhR54UluBCgyZdULoB79vNsP_HXGeGoG0EmOqGVg-dTkgKvplcfoaSFYOELwnUyWI1ZCahDNF1O1BfgzUzWdAjM8bP2EAogfNEZDDXUhaMTwcwgP2h0pFQurXZg77_J0cGOOVfBylXBxL8GhJtUUgKj-NdbVzfMpMmE_zENOzqHh0ZxLXXprU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1743ee1f5a.mp4?token=O2E3tnn701r5kInk7SA7OBrPBdBaoFnSeJHMa5dYsJ2IV1aGxpQK8zJiOgLYNbl9WCHLFzqQ0j8q6gvM8OYgf149wz6MSOtuW_saSRLBPeUTqYgIVla8okrRK2fYMUNipGDIumvYbV1nGzYlDvU_wCgtY2TyujYks5vR6cTk3-g5bhETdjdHWg5yEkLRcXT4BSerH1mYWktjS2sNkW6n4kwdGOn7SoLz-CvCWfdLLJ_EQNrFvYBSf2CUgHZDx8nKo-IlK0eRwd42fnauGtcAwvG9JdGem1b4MnYFPsQNiNQVaVI_8-iq6LOv4xyhb0UEShZJjU-yRfjaKhUJ8-hmkFUmAhOS9FPUVaFTnxMKOJu28gI_yHtoVlHS-lf35S8uel_0Eo6-YknEZUlv5HbRIHvbIVtHDbaC9fwpW20-q7flCG99qNQqC9HNTNnoaGApBAGjePzScijyWutMxTjJN2geXhupv_8S8swStnLzx3CK1Hvr85IgKhlhR54UluBCgyZdULoB79vNsP_HXGeGoG0EmOqGVg-dTkgKvplcfoaSFYOELwnUyWI1ZCahDNF1O1BfgzUzWdAjM8bP2EAogfNEZDDXUhaMTwcwgP2h0pFQurXZg77_J0cGOOVfBylXBxL8GhJtUUgKj-NdbVzfMpMmE_zENOzqHh0ZxLXXprU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
کلید واژه‌های تکراری قلعه‌نویی؛
همه مقصرند جز ژنرال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107879" target="_blank">📅 21:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107878">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
‼️
💵
عادل فردوسی‌پور: دیگر حوصله شوخی‌کردن با قیمت دلار را هم نداریم
روزگار سخت و تلخی که سپری می‌کنیم/ شروع فصل لیگ برتر، با دلار ۱۸۷ هزار تومانی، بازگشتش از فیفادی، با دلار ۲۷۰ هزار تومانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107878" target="_blank">📅 21:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107877">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc2122fb81.mp4?token=p4-FFx9fVmqKCzR1jrtHNX2RDsaHyXIA5RROlHip97Hr3qJ5IFew65wDCt0qoAU2lfwl46RdF_O3kAj1_ZsiwsxdRpe499eZEvbR4Xl0x8XODp57TMMbV1NpRqL-dwHrdWDE7Zde3Cl5K8wrdOLkyeTJE_s3EQvnsLlxnXaHyDab6iU6kMneoZKjNg7yGpH-543QS7t-0sg5oDqD_HzcRwmgc4OPrigJ3TgwFwJFm4IAcpUFLNQrldPdiMRj04mzg2IEBDkGTm2boSFlP2CIc61Rr-c3-CUrck1fb-V7qJsnUkcH-UvEIEQjhfHa2QOwVFtDxlM8WGMN_QOy-i694gUyJWgBEtSNqmO1_Ur9BrUMjAwp9U0tidEt_8IzyrcONhm8wUkWgYZALTGCS34Rj_NXjGZlVpwg6C-cIX0NDq8pDoQk9lD97ECf4Lec-7ygeTPMsCODRIHA32_bKD_Aa9VtjzVx7aixxK1V9YOHt-XT3_DTVDGTooAbgDKs3A1SGI_gOG7KoLqeXeOhqGhGNEKemrotkabKDlN76CBigMwcFXZooEwCjUZmSNZPpg9wRXZ9GnHeburDsNR-GLbhxXc9-JSRYP2T9eUwxaSMEZVmXaku3xu88-jHGBHqMaWDSTtlKSnmWIRBN1w7UBgoZMViUXXnIkRbso4bEt1vHiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc2122fb81.mp4?token=p4-FFx9fVmqKCzR1jrtHNX2RDsaHyXIA5RROlHip97Hr3qJ5IFew65wDCt0qoAU2lfwl46RdF_O3kAj1_ZsiwsxdRpe499eZEvbR4Xl0x8XODp57TMMbV1NpRqL-dwHrdWDE7Zde3Cl5K8wrdOLkyeTJE_s3EQvnsLlxnXaHyDab6iU6kMneoZKjNg7yGpH-543QS7t-0sg5oDqD_HzcRwmgc4OPrigJ3TgwFwJFm4IAcpUFLNQrldPdiMRj04mzg2IEBDkGTm2boSFlP2CIc61Rr-c3-CUrck1fb-V7qJsnUkcH-UvEIEQjhfHa2QOwVFtDxlM8WGMN_QOy-i694gUyJWgBEtSNqmO1_Ur9BrUMjAwp9U0tidEt_8IzyrcONhm8wUkWgYZALTGCS34Rj_NXjGZlVpwg6C-cIX0NDq8pDoQk9lD97ECf4Lec-7ygeTPMsCODRIHA32_bKD_Aa9VtjzVx7aixxK1V9YOHt-XT3_DTVDGTooAbgDKs3A1SGI_gOG7KoLqeXeOhqGhGNEKemrotkabKDlN76CBigMwcFXZooEwCjUZmSNZPpg9wRXZ9GnHeburDsNR-GLbhxXc9-JSRYP2T9eUwxaSMEZVmXaku3xu88-jHGBHqMaWDSTtlKSnmWIRBN1w7UBgoZMViUXXnIkRbso4bEt1vHiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
تصویر تکراری تیم ملی
بازنده اما طلبکار و با اعتماد به نفس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107877" target="_blank">📅 21:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107876">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFGbATYHCo-_k-JoTzkc-F9ZtG0wjyvcOiPR5X9gFv_wqcZDbqMeDFAzKvlr6wFALT73Y79fGk7BemrQtjhfCs2KL0yM9pCfBTtdN_UvqrpFiVtYwlLqMJ6ZY_2z6WSakxzQOIBRZjekVphteOVuhL4bw8vlYeJzcwzW8mPIBBz0-zMwTqmauL8Q14eMAiZRsMC6ilwBZqgt9kWigWpo2fUILF-Bpx8HX_x8ZcyI3Ewpk3B_xkuzxGpmw7-oiXEJj-DIQAxhXpXA6eFb0m_9CEnfjxthsJwOP2JhuO5Ry86HtLBP70UYGlrHHKw3fCBISZljEFADvJ-jF6fi84yMRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇫🇷
ترکیب تیم‌ملی فرانسه مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107876" target="_blank">📅 20:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107875">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f2c09e35.mp4?token=Ewi7vtPdVU23cNtEPIYv-mdKzjKxlRkFsbtTmkZNpRUwtvmXEBxW2kOmRs99PbR4jNpwBq3vZExbOZRckhRSZlsRAfvnEaWVPsBT0nKkQz4I_X06Zl6QZU3dh5hhXML8Z8I4aaEP8k7kbYtctGk7IwpP9zjTcXZLtClKmj7BOC6VjeKpLJQFOS5WxVzuCCfzBnxIpVYjUP3ijrKtOrZ_VHGN9Ka3rzgsTSKZpBEa6OLRYVkWOnXe5xyLNAZ-DZ38RBt_5FLH2a51pMd8d6ej3SdGevxmFv-cgmHytxttqVFHTMu2YJl3F2AXxPioAbxV97ksoHy0SMEw0MIGLwl1pUEWLDd6VTC_b_7qlA91FySbVmL4U_q29J-tUOCw0xx1bmLnWdVSdriZEkANDhsz2xGPUf_GomtAZaruuliIOTsZoGjdw_a_jf3rhv7OIHrZ1m2tjdLOraMf2eNihANN2id5bg2vYG-FEyvcdhN3lAYaFvc6EcRf8wUSQm1VbCFYSXwfKnAlVY12OyeL3wZcSW3c5mHCdepXzvU5c4djEskqHaIX8XwqHjZsNh0Re9QBjtp-mg3eqewchs5A1RgaR2a7nE8BRfuzF5A-urHiCzZ6I4dCDIqIHInubMWEbRDK7JtSQXolb_cC9FewCb9K3fp1Qh4fdjx9Lcw_bOKxQHY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f2c09e35.mp4?token=Ewi7vtPdVU23cNtEPIYv-mdKzjKxlRkFsbtTmkZNpRUwtvmXEBxW2kOmRs99PbR4jNpwBq3vZExbOZRckhRSZlsRAfvnEaWVPsBT0nKkQz4I_X06Zl6QZU3dh5hhXML8Z8I4aaEP8k7kbYtctGk7IwpP9zjTcXZLtClKmj7BOC6VjeKpLJQFOS5WxVzuCCfzBnxIpVYjUP3ijrKtOrZ_VHGN9Ka3rzgsTSKZpBEa6OLRYVkWOnXe5xyLNAZ-DZ38RBt_5FLH2a51pMd8d6ej3SdGevxmFv-cgmHytxttqVFHTMu2YJl3F2AXxPioAbxV97ksoHy0SMEw0MIGLwl1pUEWLDd6VTC_b_7qlA91FySbVmL4U_q29J-tUOCw0xx1bmLnWdVSdriZEkANDhsz2xGPUf_GomtAZaruuliIOTsZoGjdw_a_jf3rhv7OIHrZ1m2tjdLOraMf2eNihANN2id5bg2vYG-FEyvcdhN3lAYaFvc6EcRf8wUSQm1VbCFYSXwfKnAlVY12OyeL3wZcSW3c5mHCdepXzvU5c4djEskqHaIX8XwqHjZsNh0Re9QBjtp-mg3eqewchs5A1RgaR2a7nE8BRfuzF5A-urHiCzZ6I4dCDIqIHInubMWEbRDK7JtSQXolb_cC9FewCb9K3fp1Qh4fdjx9Lcw_bOKxQHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
بررسی ۵ نکته مهم در جدیدترین نسل‌آیفون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107875" target="_blank">📅 20:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107874">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dce1470830.mp4?token=d4siQusuQYbSkYkAbrr3i6lKEOx_J3f7KloYjJaYc49WR3Mclm4CIwBBDU2bbS2Rf_-uPwYpT83exbhpwSj7dlbxQdI24oLANqm_RIz5cu5cpyhOQYpm5xLMcL9iDF8GNVDSYGFhK_9OLIfyVgceX8n2hrV4X1PdVuT6L5miKGYXHZfI3fUr7vW4B_ZFmjRB_jJYFhAJ0xJPrVS52wjjfBSDd_WTDb6OqFHR6rT7XVmtpGLg1LKKIkVOTCGTHHCLrczaOMQihgiIHeJ7Wbvkbh5q8dgo_g-OyQspzC4GXx9hVxhT5BQQSW4nwhNov1LWbOOGgtErVo5uPRwSkewwMSKC7MrdttHiDQB7boi42ydJLHVgfE7m2eFQaQlmFTiKZOT-_7jaV_8OqJFvIeYR9gN4tAQicw7B_YBxlp3zu0qY1oJoFThAGOP9o0aiI4TLVKbxL-VadesvfjN72z8VPpIrkFmdH4eVoi9Wwpop0s6B916219QwtLiB_DnkFilmGYmRw1SGC84n6vU3oOil31qH6bS_uyxuzx-_jLs98FP9rPAdvwn1KL_A8JvjptVfOR3DueyPMFRVjW8oVJ-ylBIwsgAvBNIBrhRSuxEwCEQj2Brl9Rwvl7vmDo4lLMEtEL4w2-szoq2d2NoysglxWasenFKNY9NmzAOB7WWAi2E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dce1470830.mp4?token=d4siQusuQYbSkYkAbrr3i6lKEOx_J3f7KloYjJaYc49WR3Mclm4CIwBBDU2bbS2Rf_-uPwYpT83exbhpwSj7dlbxQdI24oLANqm_RIz5cu5cpyhOQYpm5xLMcL9iDF8GNVDSYGFhK_9OLIfyVgceX8n2hrV4X1PdVuT6L5miKGYXHZfI3fUr7vW4B_ZFmjRB_jJYFhAJ0xJPrVS52wjjfBSDd_WTDb6OqFHR6rT7XVmtpGLg1LKKIkVOTCGTHHCLrczaOMQihgiIHeJ7Wbvkbh5q8dgo_g-OyQspzC4GXx9hVxhT5BQQSW4nwhNov1LWbOOGgtErVo5uPRwSkewwMSKC7MrdttHiDQB7boi42ydJLHVgfE7m2eFQaQlmFTiKZOT-_7jaV_8OqJFvIeYR9gN4tAQicw7B_YBxlp3zu0qY1oJoFThAGOP9o0aiI4TLVKbxL-VadesvfjN72z8VPpIrkFmdH4eVoi9Wwpop0s6B916219QwtLiB_DnkFilmGYmRw1SGC84n6vU3oOil31qH6bS_uyxuzx-_jLs98FP9rPAdvwn1KL_A8JvjptVfOR3DueyPMFRVjW8oVJ-ylBIwsgAvBNIBrhRSuxEwCEQj2Brl9Rwvl7vmDo4lLMEtEL4w2-szoq2d2NoysglxWasenFKNY9NmzAOB7WWAi2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
کنایه‌های ژوله به داستان سربازی دکتر بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107874" target="_blank">📅 19:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107873">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d2ddbc7f1.mp4?token=YL6SmoPT_gdrl-eNn-eV742zZ6-A2zipMyKrEiPvbGaEFVaRToUl58eaFB5DNcgTb1V5HiBCtSyTP4Q1qJwwA-7JQ7hYAhKbWVY4aWNLQcl-9n2rldjUGv_7jWlTGA-GqrlaESTtVl9QZPsz_3b3wFo_5e0YpeRPQoVGOjAYN2FBFBaPCxKPe4FKf0S3rsj9IWUhZ5H4Y6P38YEvn8Z-rp9ZQ7lX24I7TGv09sjI5efU1yNsi_Z7NbMhIOGfan4DFALUia8AYHy_kshp-rwRNFoCTuleE1rvCFB0LicfeO77Mo5SNFmoZmShpU6gea3cTCE1oJJIVwTwZqoAKniSTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d2ddbc7f1.mp4?token=YL6SmoPT_gdrl-eNn-eV742zZ6-A2zipMyKrEiPvbGaEFVaRToUl58eaFB5DNcgTb1V5HiBCtSyTP4Q1qJwwA-7JQ7hYAhKbWVY4aWNLQcl-9n2rldjUGv_7jWlTGA-GqrlaESTtVl9QZPsz_3b3wFo_5e0YpeRPQoVGOjAYN2FBFBaPCxKPe4FKf0S3rsj9IWUhZ5H4Y6P38YEvn8Z-rp9ZQ7lX24I7TGv09sjI5efU1yNsi_Z7NbMhIOGfan4DFALUia8AYHy_kshp-rwRNFoCTuleE1rvCFB0LicfeO77Mo5SNFmoZmShpU6gea3cTCE1oJJIVwTwZqoAKniSTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ممکنه دفتر نُت موسیقی دیده باشید ولی ندونید چیه
این ویدیو کمک میکنه تا کشش زمانی نُت‌ها یا مدت زمانی که یک صدا یا نت ادامه می‌ یابد رو راحت متوجه شید
و به هر کدوم از این نت ها چنگ، دولاچنگ، سه‌لاچنگ و ... میگن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107873" target="_blank">📅 19:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107872">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd348ccf0b.mp4?token=WEq0wvdyMP1-e7PM6MvG30t_wQRHca5z-k4y8JwNONP1SvsBdr2TERP0YwplXpSu4FymoEYdrOJIIHgvNifhKveEz9Dk3nALd1KitcHiEbc3XCJ_Z1YHqNuUN8rOwyqFOYS1r0u2EnXOR4t7J9_KU9VzEy0CxYgTgaDWlNrbj_IBu-WWMEl4iV4epN8TU4AZBS34wrefCGtMrb8E4XktmX3EbW2DiGtb5ABVEKX4RrnqHnfAUQykld-gPQk2v_9FEILTNroGgcROThe-J3Am_IdvQVxHTtUBlYK7jETG37tmy4twruZw-eZPMqaNJAu8gDgHr33Bbp-xI8E8wBYYKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd348ccf0b.mp4?token=WEq0wvdyMP1-e7PM6MvG30t_wQRHca5z-k4y8JwNONP1SvsBdr2TERP0YwplXpSu4FymoEYdrOJIIHgvNifhKveEz9Dk3nALd1KitcHiEbc3XCJ_Z1YHqNuUN8rOwyqFOYS1r0u2EnXOR4t7J9_KU9VzEy0CxYgTgaDWlNrbj_IBu-WWMEl4iV4epN8TU4AZBS34wrefCGtMrb8E4XktmX3EbW2DiGtb5ABVEKX4RrnqHnfAUQykld-gPQk2v_9FEILTNroGgcROThe-J3Am_IdvQVxHTtUBlYK7jETG37tmy4twruZw-eZPMqaNJAu8gDgHr33Bbp-xI8E8wBYYKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت پسران و دختران پس از نتایج کنکور:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107872" target="_blank">📅 18:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107871">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B38BX241Oz-6BJns7LSAEMW62d4S_WcGuzuxf8eXdLJIQfm2kJPQs5CSj7ApthJAatmGM9LaU-PbTnxcBicWzMW2rPwa_c08u6Dx19ksHWmOdBq59RmtZ3yWvATE0TcvBUvHe6hg6UYY9_32pHfQsEn4_Crg4vr3VFm_7Fu415Nve4hvdnesvgB3VMZYopjQG-DGPZlAz-gc3_dTCB843X55Zky-5GVLwFUlU3nYObmh3DlPpGFzB7Amhh5X0FeelJoh4bZ_DNk5l942N46kSD7CZtxk_mB3DbGAb86SlwdPoG6J4nN3i5E8NMChxAE_G1_3F1IOsFjgEUgIJE63tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
فهرست نامزدهای جایزه گلدن بوی بعد از کاهش از ۱۰۰ به ۲۵ نامزد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107871" target="_blank">📅 18:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107870">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6601bb6094.mp4?token=Bv7691GmSFVMmjdjzzH3OjqB5yb4Qo7AqLb2sp-oGeV5NBq0v5lrDLG_BOnWG58bG_A1JCnI4kTZKskdA_3aMkHeHi3Zmobwe3KwJUJhRgb7iFF4-v2J6Mk9d8FYFNnMaB7V-owCDIQADBYtiPnJeMo2pzVmXD5c5OABDqaw6kwMbrh7-YFaHurk2O-6VHflEeM6oflosdJLkhLDXkbg7sspMFkM9bjIXdiBhuYIAKB4JFAFvF_BYXQYMw6MCuA2D1q7lvxuooGPvaaXGKchUH3F2BtbCdyCan_7h0Yd5D--suTZHD8lkSW5CqsYTuk5DlUYNiQr-zkqqkHjUzCa3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6601bb6094.mp4?token=Bv7691GmSFVMmjdjzzH3OjqB5yb4Qo7AqLb2sp-oGeV5NBq0v5lrDLG_BOnWG58bG_A1JCnI4kTZKskdA_3aMkHeHi3Zmobwe3KwJUJhRgb7iFF4-v2J6Mk9d8FYFNnMaB7V-owCDIQADBYtiPnJeMo2pzVmXD5c5OABDqaw6kwMbrh7-YFaHurk2O-6VHflEeM6oflosdJLkhLDXkbg7sspMFkM9bjIXdiBhuYIAKB4JFAFvF_BYXQYMw6MCuA2D1q7lvxuooGPvaaXGKchUH3F2BtbCdyCan_7h0Yd5D--suTZHD8lkSW5CqsYTuk5DlUYNiQr-zkqqkHjUzCa3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
میگل آلبوکرکه، رئیس دولت منطقه‌ای مادیرا، زادگاه کریستیانو رونالدو:⁣ ۳۰ سال دیگه کسی یادش نمیاد کی سرمربی بوده، کی رئیس فدراسیون بوده یا کی کارشناس بازی‌های فوتبال بوده؛ اما همه می‌دونن رونالدو کیه.⁣ این تفاوت بزرگی و معمولی بودنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107870" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107869">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107869" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107869" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107868">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhkOob-Gfl3J-uxL1edo_smTU_-BfclnDyHvQEtWVGTYF_Vvx9x81AjrtunrA-JLI1Vqtf154082NsXBOhWtdIn8yY6_2Zlpo1jvFGFXVTWHeEn9VFJcrvDlfXDCytEUCRESl1PG0mUmUsuTn5VNATO5S9ru4CfDrWt0LDnHLDPSebCh0PgVLpxn112qI-hql5sC3Hd00hA5-6HO8BT5Jb3bv9upfBRx4HUtoh6bg9M7tpI5m67iPeNJj9ePOkdMfu0_IlvlvF9lxCVuCgK3HTmHxywuHGKPgmpCXs1KTYXbQBzWPYJiM3ugXRcBLsShEXwWtG4p9XCmWYEm6VzjVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز بلژیک
🆚
فرانسه را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
بلژیک: ۳ برد، ۲ شکست و ۱۰ گل زده
فرانسه: ۲ برد، ۱ تساوی، ۲ شکست و ۷ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107868" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107867">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUloX3k-WGb-NkZUTKE7gz42Pqud-iRS3ge1tD4oC_WT4UaeqThOZtdYPjjlXnuOAj2bhDxlZaH_Agrz0m9A66UwhEk3LXMBd30sBupYJdlLd647wCVsq7V1lPjZjXLC18dR_CbWic7V5esdSOtHWqnytyyqe94YGGT2AzHOOzXE9ySX1E37eYpO-_-iH10iFppaFowLMN1V9yif8su1QlFOC978NQApAfZEZS1nuuR8-MChEepws3u0RGf8gwqSyE6LNq3XevRrORy9AUFN6VQ7cnRW6Qkh6Zk-jDe59tRjxareGxyUue_56DaWzLMT8Qoaamag44Ye_fnqgOyM5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
گونزالو راموس در هر سه بازی اخیر خود با تیم ملی پرتغال که به عنوان بازیکن اصلی در آن حضور داشته، گلزنی کرده است.
🇵🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107867" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107866">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1c39a914.mp4?token=sseranLArIQVB4swkBMgC34SFsXToFIYleHiYiZRXZ9aXswQOY51qfFLzXRr9QtgXwwiq-tXCx-FnD-lWoa8BtZ-oY8GAHL16SAecO5HljXHbGDrtMxSUmaOallI9swps6BSfszh6DZ3pCVk9R_dt6Hty_eSW5jjI3S0NZKHgwQx8xlZprECfMq-x3QKxtzJIDmDn7-0vA8BCbn0er-goJomuK3ffVObX2NkmqB61bfHUPC6abVnoWxJGIobX-wVBCRDt_ik_PBlNeGvrEE2Q0d-uzMAZjt91hDkeYLkcNhMOt1TwqQ_Lh2cptAGv8ny50sVEvLRpyTnZDp4IwrA1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1c39a914.mp4?token=sseranLArIQVB4swkBMgC34SFsXToFIYleHiYiZRXZ9aXswQOY51qfFLzXRr9QtgXwwiq-tXCx-FnD-lWoa8BtZ-oY8GAHL16SAecO5HljXHbGDrtMxSUmaOallI9swps6BSfszh6DZ3pCVk9R_dt6Hty_eSW5jjI3S0NZKHgwQx8xlZprECfMq-x3QKxtzJIDmDn7-0vA8BCbn0er-goJomuK3ffVObX2NkmqB61bfHUPC6abVnoWxJGIobX-wVBCRDt_ik_PBlNeGvrEE2Q0d-uzMAZjt91hDkeYLkcNhMOt1TwqQ_Lh2cptAGv8ny50sVEvLRpyTnZDp4IwrA1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
آخرشم نفهمیدیم بارسا چجوری تونست 8 تا بخوره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107866" target="_blank">📅 17:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107865">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kI27Bbfeamg6YyRaYRuQgGtEK_DBTGp519vFvo6UGsdKcq8iUcigR3ShtREQgO0rpfJQI-lT3OtMQ7-JNdv0essbtslBg2pjmEO0LCwPL5adtUpJvyqtsrtamrHnpDiptk6shgPAhkKWWtgNK7L_JAbX21KGkzD1Ef_kO_o8zyPLwA-rnNMJ9b4uekGlBIafpgd4pXBdGty3JreOTZkrSjtlj_LipqjTIqr68ezAvU1yt_c4tZNjmKGsG1KvR4rdNlzYnuVuKW_hj7L07CUB7GDE1rKyRKJyP3UUYPYkIfuap8DgKDp4iKRG5BFDutds21bzmqiOJ9sBox2mPRv35Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عکس جدید نیکی کریمی در 54 سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107865" target="_blank">📅 16:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107864">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d579a3c3bc.mp4?token=jBiQ4EO9BAj2bAKG4qpN0bJByRRTpobwSxU5dA4hKzYAbkxHSYIGmA5e4K1k6tsL02beBoIADPdMkBNjzYA9azxCjvJjPYmowlUOfz-Ui8bjledfo7-vtaOmETsl9HjZMAwfTJtVAUdUb9BvLo8LSHRpJ07VfqoIW_vdcJyI2W0nBjKEXuy5j9GULrhVUv3zFJNeMsCkYGgQk9XOWLRV2iOPmGHlimQffMmIgChO_Ppy2TSBb3GEWB_aMeziFlcorJmblMAo49tS8o9gu4pMWgYVyhDPc1CR3Nct0np6Gy0uOOFpIIouNzgwr2aLqmC-WphSNpQZQtocwjZ3pqW08g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d579a3c3bc.mp4?token=jBiQ4EO9BAj2bAKG4qpN0bJByRRTpobwSxU5dA4hKzYAbkxHSYIGmA5e4K1k6tsL02beBoIADPdMkBNjzYA9azxCjvJjPYmowlUOfz-Ui8bjledfo7-vtaOmETsl9HjZMAwfTJtVAUdUb9BvLo8LSHRpJ07VfqoIW_vdcJyI2W0nBjKEXuy5j9GULrhVUv3zFJNeMsCkYGgQk9XOWLRV2iOPmGHlimQffMmIgChO_Ppy2TSBb3GEWB_aMeziFlcorJmblMAo49tS8o9gu4pMWgYVyhDPc1CR3Nct0np6Gy0uOOFpIIouNzgwr2aLqmC-WphSNpQZQtocwjZ3pqW08g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
صحبت‌های رسول‌مجیدی درباره سختی مربیان تیم‌های ملی بدلیل زمان کم آماده‌سازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107864" target="_blank">📅 16:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107863">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ea1e2bc4.mp4?token=v9KiplPNl903XrT9SvjOGWSGf1hLjzJDu1f46YGgOWnvVIYCDBc2as4pSW9e8wRTvmBUwEHR3V0KD5NZRVMeZRxzigiL5XgfZNRDEjL7OLmXfpmkxpgtS0MAPAlLnUaj_RNUqfA57ABXYIzUVpbAnhV2LtzBRsTCQX3axXah-PCwV0qOP4Bz_0p1WRvlXvQL67fYKkB_bEL6P0GzOAgMJBy2Ax3mT4vxlCRTGksaY97jPoNlyYaBG-MagMLUoYhfsOuEP2JlnrKbfQktxjWtSbizZogqCL41XZvyFIDUjY7VsIq0oxGaomz1JfZc4mH8_C1V_R38ZhPTkV8eRGO6rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ea1e2bc4.mp4?token=v9KiplPNl903XrT9SvjOGWSGf1hLjzJDu1f46YGgOWnvVIYCDBc2as4pSW9e8wRTvmBUwEHR3V0KD5NZRVMeZRxzigiL5XgfZNRDEjL7OLmXfpmkxpgtS0MAPAlLnUaj_RNUqfA57ABXYIzUVpbAnhV2LtzBRsTCQX3axXah-PCwV0qOP4Bz_0p1WRvlXvQL67fYKkB_bEL6P0GzOAgMJBy2Ax3mT4vxlCRTGksaY97jPoNlyYaBG-MagMLUoYhfsOuEP2JlnrKbfQktxjWtSbizZogqCL41XZvyFIDUjY7VsIq0oxGaomz1JfZc4mH8_C1V_R38ZhPTkV8eRGO6rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
بیرانوند تو سربازی اسلحه بازو بست کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107863" target="_blank">📅 16:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107862">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/367af750e7.mp4?token=E6VwkWaVV5VIEzhgBMntEJ1M-AIQdJvEuP47Q_Dd2CxAxkzKFr7bgP7WABr66MavfsGY4gCl8GinO5lz4gBlw72MU1ZI52q3Qlaw-9iLHN3wUvPG8dyV0SEoFYLzVSDSC2iXDczOvzr9zuF7bknx8pDcJ7SdA5Nln9FgjMXtAehsfM6m_ixZsIWfZnUq8G5SfAre_G63lrS0VkLnP4IfPfAH8aGTZugSstMVB4-SudiPbaaTasBoGWrgLGv9135fjGtASd-ZV0KsEp7dxGXX_oJfFK40hl7FNdFCrgwtU5yAIu__507nqLfOofNc82bff4FYkg1Io57s-HFyhmkx7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/367af750e7.mp4?token=E6VwkWaVV5VIEzhgBMntEJ1M-AIQdJvEuP47Q_Dd2CxAxkzKFr7bgP7WABr66MavfsGY4gCl8GinO5lz4gBlw72MU1ZI52q3Qlaw-9iLHN3wUvPG8dyV0SEoFYLzVSDSC2iXDczOvzr9zuF7bknx8pDcJ7SdA5Nln9FgjMXtAehsfM6m_ixZsIWfZnUq8G5SfAre_G63lrS0VkLnP4IfPfAH8aGTZugSstMVB4-SudiPbaaTasBoGWrgLGv9135fjGtASd-ZV0KsEp7dxGXX_oJfFK40hl7FNdFCrgwtU5yAIu__507nqLfOofNc82bff4FYkg1Io57s-HFyhmkx7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
▶️
با توصیه‌های هانی‌رامبد، اینجوری شانه های پهن تری میسازی؛ ذخیره کن و بفرست برای دوستت
❤️
👌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107862" target="_blank">📅 15:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107861">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anIwa143B0VGe1_tZVmNxcsAY1HMcio8XSMUbdrUg6-dEvFptsvTSklWJbHDUlqCTVs_TTEAU5_4sHd3EHhneXpcZXs-36EhLnk8ZxoFCgt_WBA1xF4HvYpkLomsQJtresBH7qTy_XuxMEVCWQctjla41NI2jdBxE8DLiftMC5eFLscir8LuSnEqIQB86a8nCHhNr4N0N4T8MFMdpiv9MwQ3oaieh3In9I1iYC6kRgjN9RDv7TrDPTaiP6gJK2ONIuoOnY9YRFKpVGRWIkx3fW56Z0EsZam8RkSXrSGWEjmlaVt52lg4DcqNjwwoRDv4PUUvmLF0rAL_1s-sP7SRHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
اسپانیا اولین تیم ملی مردان در تاریخ فوتبال است که 41 بازی متوالی را بدون شکست به پایان رسانده است.
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107861" target="_blank">📅 15:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107860">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c6f99cc68.mp4?token=hDbncCkwPMRQAvhdpvIeEu7zzQLxeYuvpDEsWJCowjBl-fNb6EH1eO6QMvVtGxmsAGZU0rauDY-kcO4lT2HYaU1dhrcG2akS1QKUZf3IjbNUYYHpJcqbysaAD5eJ-9tykNFWrZBaWkQQ6z-s9CPDO9KTDnPeFWoiJYXs92znxgvaD50YC_GIm71-BPf183To9j3i43fFrUanX1fIaOZ751_-OFjx8Lh4v5N7cJiGIuiXKVU5t4vgxvvGqdcdUJyZiGW9m93wFAFUhhVLTApwepKEYPQzNEIFQuHu3_j8ta-397Q3SlAA5Pr-rZPImDeNCcYJJrEo5apB4jw_q4wuMwsQ3EIz7REpxFkuomzRq5OVlUH10hIHZ09G8A2_COMHFvdJk02RnvDajwCTv9cFV9Zx5QSQf-X1n4Rc64mKGr2IfDJaOHF2cEyNw1YgQdFZ6pSxLRmww2EqVfpuawCKYuuL5RWJ_Gq6N9cv7LUyDlLUjKavFBx_oq_uHAiV-xKuESeyEkRZ7FmNm2apJfdBbIE8hFJuBbKtrL01ZLZrNAbn4X3C18k7PaMXncMHtbAE24-EPIrR4DiEA3Ubg9PNZrovmknBO8B5yXmqJ-AFt64zKljvOAkOjnRrUoPLUNxS9nqVVLxgrtIZBB0EsT_qm_7GrCyF_LUhMrFzdqjXgTc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c6f99cc68.mp4?token=hDbncCkwPMRQAvhdpvIeEu7zzQLxeYuvpDEsWJCowjBl-fNb6EH1eO6QMvVtGxmsAGZU0rauDY-kcO4lT2HYaU1dhrcG2akS1QKUZf3IjbNUYYHpJcqbysaAD5eJ-9tykNFWrZBaWkQQ6z-s9CPDO9KTDnPeFWoiJYXs92znxgvaD50YC_GIm71-BPf183To9j3i43fFrUanX1fIaOZ751_-OFjx8Lh4v5N7cJiGIuiXKVU5t4vgxvvGqdcdUJyZiGW9m93wFAFUhhVLTApwepKEYPQzNEIFQuHu3_j8ta-397Q3SlAA5Pr-rZPImDeNCcYJJrEo5apB4jw_q4wuMwsQ3EIz7REpxFkuomzRq5OVlUH10hIHZ09G8A2_COMHFvdJk02RnvDajwCTv9cFV9Zx5QSQf-X1n4Rc64mKGr2IfDJaOHF2cEyNw1YgQdFZ6pSxLRmww2EqVfpuawCKYuuL5RWJ_Gq6N9cv7LUyDlLUjKavFBx_oq_uHAiV-xKuESeyEkRZ7FmNm2apJfdBbIE8hFJuBbKtrL01ZLZrNAbn4X3C18k7PaMXncMHtbAE24-EPIrR4DiEA3Ubg9PNZrovmknBO8B5yXmqJ-AFt64zKljvOAkOjnRrUoPLUNxS9nqVVLxgrtIZBB0EsT_qm_7GrCyF_LUhMrFzdqjXgTc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💥
پیت هگست در سالن «کلون آرنا» در آکادمی نیروی هوایی آمریکا، در یک نوبت ۹ شوت از ۱۰ شوت سه‌امتیازی خود را به ثمر رسانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107860" target="_blank">📅 14:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107859">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/969710a175.mp4?token=EMl9a3iNCaZgedLMei2goxbQeEfR1K0MCcZd-wT0nHk51bt_CcqBCw1qHoxpHKpQ4P8Tf5KEnvPeKfv3iHkGUIsfU6VP4p0--B8gSzSJWDCZ2fIb2R57BmOzhJU1cRF_xSpvJJ2wImXRl5aAbbTeL8MB1CibK_nH9j1E_UGr8PEWrhVqIVc8iLHzaHZBCpyjQJVRpyR2VrQ_EEScZXPban1RkxZKRDaBh4nkjOqq-YbgsjrUBojhJJNyO3ffIqriAYm6gUpQWwVPard9CXYv9NVW-OQb9Xl6gMEeo59zrafoiVrlilFwHuRo0zF7cyeeVO2smIXUDPDxRitRSQP60JdNyeMpS1qeelva0pxOtMao28oxtqvtO0k7U7xF6hYO5jSDk1aR9XQsXhhI4sVZrEXjgSyLZqhysVr31Dqe5GSinCMPFXTx_ZdF95w5G2gMerdpgxi04bveY9Mf6vc403qLZBznwGxpR2LnVRc5ApTKdRBYFaqSPAWU9Ad78LRuX4ijcu9Sr1OEiTmoSzvs4LiZowEG9YmRn32TdvBd-nc0Zv3ay76ksasgETYqNDl-EZ2N2ZjlD03725V5usafi_2ISnQ36L8wnkdVgXC1NFrfY2JQnVviv3kXYm2yRX4bnL-jP8SuohVQJSfmVpiks22NACVz78rGE10M8jT38tI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/969710a175.mp4?token=EMl9a3iNCaZgedLMei2goxbQeEfR1K0MCcZd-wT0nHk51bt_CcqBCw1qHoxpHKpQ4P8Tf5KEnvPeKfv3iHkGUIsfU6VP4p0--B8gSzSJWDCZ2fIb2R57BmOzhJU1cRF_xSpvJJ2wImXRl5aAbbTeL8MB1CibK_nH9j1E_UGr8PEWrhVqIVc8iLHzaHZBCpyjQJVRpyR2VrQ_EEScZXPban1RkxZKRDaBh4nkjOqq-YbgsjrUBojhJJNyO3ffIqriAYm6gUpQWwVPard9CXYv9NVW-OQb9Xl6gMEeo59zrafoiVrlilFwHuRo0zF7cyeeVO2smIXUDPDxRitRSQP60JdNyeMpS1qeelva0pxOtMao28oxtqvtO0k7U7xF6hYO5jSDk1aR9XQsXhhI4sVZrEXjgSyLZqhysVr31Dqe5GSinCMPFXTx_ZdF95w5G2gMerdpgxi04bveY9Mf6vc403qLZBznwGxpR2LnVRc5ApTKdRBYFaqSPAWU9Ad78LRuX4ijcu9Sr1OEiTmoSzvs4LiZowEG9YmRn32TdvBd-nc0Zv3ay76ksasgETYqNDl-EZ2N2ZjlD03725V5usafi_2ISnQ36L8wnkdVgXC1NFrfY2JQnVviv3kXYm2yRX4bnL-jP8SuohVQJSfmVpiks22NACVz78rGE10M8jT38tI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فوتبال معلولان عجب صحنه‌های فوق‌العاده‌ای داره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107859" target="_blank">📅 14:25 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107858">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81e41c5067.mp4?token=g11Kxrto7YoMZUijxrs1rV0yzZYIVA_8fFtE4Ky6yqjOmQt9yBXQfjUNweSeMiR_aEWwo1ZNsmUdEo9FXAmxJq9WYRkYoaYhsCPBefKDgQBAHOANfhKcn819ZUtw1T_5AV0PYahTCb4T_p-xdB77V5fpO3fSiUbdAX4m_fEC0r8vkZQvcU0RqDgFeuba1Ua6DrfZ3veOg_EhZRA7o2qK1jxQnxA02hO0StVhSIPfwWMVFmb2np3QTlBFczeRcbLEEZuUuLWrf9VxEtvv0Rjlq9mJJ-YqNHaR3Iv0uHf_eYBRoOxJkwoLAmbVBEBzkivO-0c2yueny3oOAZ6RGGKDIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81e41c5067.mp4?token=g11Kxrto7YoMZUijxrs1rV0yzZYIVA_8fFtE4Ky6yqjOmQt9yBXQfjUNweSeMiR_aEWwo1ZNsmUdEo9FXAmxJq9WYRkYoaYhsCPBefKDgQBAHOANfhKcn819ZUtw1T_5AV0PYahTCb4T_p-xdB77V5fpO3fSiUbdAX4m_fEC0r8vkZQvcU0RqDgFeuba1Ua6DrfZ3veOg_EhZRA7o2qK1jxQnxA02hO0StVhSIPfwWMVFmb2np3QTlBFczeRcbLEEZuUuLWrf9VxEtvv0Rjlq9mJJ-YqNHaR3Iv0uHf_eYBRoOxJkwoLAmbVBEBzkivO-0c2yueny3oOAZ6RGGKDIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سمفونی خیابانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107858" target="_blank">📅 14:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107857">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5554fbfbba.mp4?token=sFqT6b8aHNbWPhUBY7d5gAX4dhnK7tuB1N_vz1-3Lys3_ACUUnIHcWoOFN1eH-ebACxG2AGT7rITHRGie7Vd8Be9JLadWjaRksF9lXvOnIywAdJplc7UHM1EDT-O11nfHlpLtDihZ-E9bZqeI688zV_VpDUxTgSpe1LtQuD3uCIl_qvafQVR5HQBBRxO6pLoZMbXSATkfVAfhbJrszNrY8GOsqXfebHXGAGz5xkpDXBCVJP_byLq7ClB8mpGLkBxFsZVxhI1kzwRE3BSS1zfisLgke9FMMXOSwG1UXJ3G5_O_OAjqhJ8EPbpUjw7W2EmvgeL6ZZPqPkyNI_kYXrGwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5554fbfbba.mp4?token=sFqT6b8aHNbWPhUBY7d5gAX4dhnK7tuB1N_vz1-3Lys3_ACUUnIHcWoOFN1eH-ebACxG2AGT7rITHRGie7Vd8Be9JLadWjaRksF9lXvOnIywAdJplc7UHM1EDT-O11nfHlpLtDihZ-E9bZqeI688zV_VpDUxTgSpe1LtQuD3uCIl_qvafQVR5HQBBRxO6pLoZMbXSATkfVAfhbJrszNrY8GOsqXfebHXGAGz5xkpDXBCVJP_byLq7ClB8mpGLkBxFsZVxhI1kzwRE3BSS1zfisLgke9FMMXOSwG1UXJ3G5_O_OAjqhJ8EPbpUjw7W2EmvgeL6ZZPqPkyNI_kYXrGwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
👍
ویدیو جالب دو بانوی کاروان ایران در ناگویا و خوشحالی بابت کسب مدال در آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107857" target="_blank">📅 13:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107856">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cedf090cb4.mp4?token=e7-kDBHed1--bi8e4GFcrp7uhpQ17kTqdsS4up80RPUCSJAiNwIlImEpy7vdipr26I5u6qO9MA8Vn5soR-58995H073nhClGzk-LPVj_2FhFYZvyrpF4VKDJWra_0Sf_vG2xTUwOMcMll9Eo1YVXv7AYe2WCCDwDjjVwyuGs4dtBp9Pr9Bmdx_Z74ElOAzlOMIjwFWABtB1ajRuobVN1tw5NzaIjLWdgB4TFdv2s0km5teePDXRUpk2a-SqrEm7zMW-Ojbu65kQRQAFGADlSORdKQnC4UbBWX_MWvHDvdFY2v04cirpJhVNKTSqyztLWAG-aoL9JRfhI8KF0YS-Fzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cedf090cb4.mp4?token=e7-kDBHed1--bi8e4GFcrp7uhpQ17kTqdsS4up80RPUCSJAiNwIlImEpy7vdipr26I5u6qO9MA8Vn5soR-58995H073nhClGzk-LPVj_2FhFYZvyrpF4VKDJWra_0Sf_vG2xTUwOMcMll9Eo1YVXv7AYe2WCCDwDjjVwyuGs4dtBp9Pr9Bmdx_Z74ElOAzlOMIjwFWABtB1ajRuobVN1tw5NzaIjLWdgB4TFdv2s0km5teePDXRUpk2a-SqrEm7zMW-Ojbu65kQRQAFGADlSORdKQnC4UbBWX_MWvHDvdFY2v04cirpJhVNKTSqyztLWAG-aoL9JRfhI8KF0YS-Fzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های متواضعانه اسطوره مهدی‌ مهدی‌کیا درباره اختلافات بهترین نسل فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107856" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107855">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54734be7bf.mp4?token=SUOrWlfaD20m6KtJG-rCWVz7lqwNHoePsRDg8Cesui2cP4Y5dVvImJkbuLRqmDOQBoWsEhBOUI9E8DZKuKI3IbfoU3wI1Fs1BJymKOwvEu4KV6_u9iHxBv0O0GZM7eeOFG7_Zhk1w_BR7r53NMbG12GUniyVV8iR9l6qhmvo67cBZn17nIUTyiIoargddAYZtlZ9dYmiIBGsAf3LeAoJMgyUjyQpbtC32tmNKYcQGj9ffDboduMVmTUm8oMabB1-POJ8jou7rj5FMe0OlcI2oQRy09eDx5XZ-sPBZ3TY3qNt_wbPVsN5nVh3JyNzL9fQYsqqF6kr070fqATq41fOxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54734be7bf.mp4?token=SUOrWlfaD20m6KtJG-rCWVz7lqwNHoePsRDg8Cesui2cP4Y5dVvImJkbuLRqmDOQBoWsEhBOUI9E8DZKuKI3IbfoU3wI1Fs1BJymKOwvEu4KV6_u9iHxBv0O0GZM7eeOFG7_Zhk1w_BR7r53NMbG12GUniyVV8iR9l6qhmvo67cBZn17nIUTyiIoargddAYZtlZ9dYmiIBGsAf3LeAoJMgyUjyQpbtC32tmNKYcQGj9ffDboduMVmTUm8oMabB1-POJ8jou7rj5FMe0OlcI2oQRy09eDx5XZ-sPBZ3TY3qNt_wbPVsN5nVh3JyNzL9fQYsqqF6kr070fqATq41fOxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
خاطره بامزه علیرضا بیرانوند از شب پیروزی دراماتیک مقابل پرسپولیس در ضربات پنالتی …
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107855" target="_blank">📅 12:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107854">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-nnFjcVNBWoDL05djS7sQ2VXNJ6ppY-bw4cCFUQinQLty0juMwpwI0dBnZHSXXwRbNWLRYZkj1-aCmJMFS8OtJ6XQsFDMHe7sBSLfNR1uAFHgSSraUDOXgWYAQ0oCCZsylHjCPoiTxqMtugKP-Wbeetx-VMSe4S4QxDu2lwmg0ZrmsbAz1o9WNOjyYHOY9zqP1wvxwr98KFEfRQ76fkNFw9yDLCphVtK7AHrXC8MezhgHPF00JVcw0cYhRnqL_UTF0bWMJrNlMJsWYyOsJ_CiEB-AiJfCoIWbUu9q6eFp2Kt_R-t9sQluVE1vinivPNA71vFydZMbZtDuWgujqQRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
استوری مدیررسانه‌ای استقلال در واکنش به مصاحبه شب‌گذشته مدیرعامل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107854" target="_blank">📅 12:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107853">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmxJx3QYJ1uxn-i1UYilQj6eKL2eWAQIAhCN_z_ffZwP8nwBSLlnuFDg1PgfGa7faCy9Xu5af_cEHxg2letHU3iqnsK0_xu468b77GxtAPHvvv0R9zcPuGBmF9zylqDe_fdJsIJd_5W5j5oCNMEKKThV-qCiL-sgtVQ0EHenqrSoh2cqMjMB9wGxa8_7kd84sSc2zRbwK2RoDQ2iZJFXuIrL7GETH1gOBErpLGvgY0DVT7tPE80tvzr2ZRXt5o6Gba52jOLPmtKAE3mvI881c53KmL-CB1Nqlznfk53AMnAPgTdO2RAHB1TnhtlZnKWAiwwVdjMLaN1_FipN-gfeCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
هیئت‌رئیسه فدراسیون فوتبال اعلام کرد که جام‌قهرمانی فصل‌گذشته به استقلال داده نخواهد شد و پرونده این موضوع رسما مختومه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107853" target="_blank">📅 12:25 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107852">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f754e7f64f.mp4?token=aJyo7BOPIahDdsJUAv6NTGt65n80gxqZbTPxgs9I-tvm-V7ZY0pbJXHl1YIxpzZR8Hu5ocO4uKJOgNTApHW1Qx6cl9vBcih_AQsx2ai7AcxPj66GkHiQzg0p-_-iQ5dIlB3Mktkz37H7Exg5_Mx7cFA22tcjHs2aCBEXXJP1LbM3nt70X0E_jZ_pz2DBybY2Ubk3wHMbphle3KzgGPA_ukMvkXsHJMYt4WKXM8ffxDfPyVw86Qd1P_YqHivEgnE-IOXybz54RZPpTbuxub-gqTLG7VOGrS1hM0QAbbf3nqSV18SgPXajpNfTo9gr1sLMPWaX-FkjxDXLPg5sGUoxcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f754e7f64f.mp4?token=aJyo7BOPIahDdsJUAv6NTGt65n80gxqZbTPxgs9I-tvm-V7ZY0pbJXHl1YIxpzZR8Hu5ocO4uKJOgNTApHW1Qx6cl9vBcih_AQsx2ai7AcxPj66GkHiQzg0p-_-iQ5dIlB3Mktkz37H7Exg5_Mx7cFA22tcjHs2aCBEXXJP1LbM3nt70X0E_jZ_pz2DBybY2Ubk3wHMbphle3KzgGPA_ukMvkXsHJMYt4WKXM8ffxDfPyVw86Qd1P_YqHivEgnE-IOXybz54RZPpTbuxub-gqTLG7VOGrS1hM0QAbbf3nqSV18SgPXajpNfTo9gr1sLMPWaX-FkjxDXLPg5sGUoxcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
چالش فوتبالی با چهار اسطوره محبوب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107852" target="_blank">📅 12:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107851">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atmqeKrhVYIu2bCckIZEtkNACAZOkXbzuqYvn_wV72n6YJNEYsme6eoX9gZWkpL4cU8CJnI6Y_y_TTqea8oi3R1H4fmSOOkCub7wXVGiz2vNcpcseSIpsiA-XuRTIamNdDSZe3yfcQI2LyPcmy-KJHH6PsKimeMnrahJo0rMOmsWEg3k_NDW5YdwlnBBdYnU1q79zYtvNL4m96NoTamFeEkdLYAr2MmeHDdto4eTHAiKwXNbXz594UAhNgEY2bpx7K8E2e3QwD2TgagyhDv5UBLjJNJzjfvU1NzFW4aL0uGJIgDyDtkGSGZItqUuoVzdbC-Lx9Q62VBnaBi1eRTnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
عملکرد مهاجمان بارسلونا در این‌فصل چه در بازی‌های باشگاهی و چه بازی‌های‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107851" target="_blank">📅 11:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107850">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fd2204c7.mp4?token=JPE-f16qXeogq2iynClAcluTQBc0gib6HPFrgh130Jh1KliG01fMNvPIk30YqCka0ylpC_HB1kkPeSzD5aM7N-tXmZqjdLRSW7XnuJVhnoMNUZ4oZI16oQOz1S9xNIlD5UZFwbK20JXzLDFYnf27Ar7GhQX4tgrLJFkktyMeMIVUBwx-A1eFHwDyBH789c8pBtKx0HNZn5bPzIwdBz0LbKor2-oIajQJoG5kFI67yyOrlY6L-Oyhkw5WydvNKNPqMX0noOm6Y3afkw5sVdeqG9gZcJwi8IbzvVpDlVOFeH9i3KCOgLslbJ9xgySWT_GycChladrNCvC7UFf60GQkzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fd2204c7.mp4?token=JPE-f16qXeogq2iynClAcluTQBc0gib6HPFrgh130Jh1KliG01fMNvPIk30YqCka0ylpC_HB1kkPeSzD5aM7N-tXmZqjdLRSW7XnuJVhnoMNUZ4oZI16oQOz1S9xNIlD5UZFwbK20JXzLDFYnf27Ar7GhQX4tgrLJFkktyMeMIVUBwx-A1eFHwDyBH789c8pBtKx0HNZn5bPzIwdBz0LbKor2-oIajQJoG5kFI67yyOrlY6L-Oyhkw5WydvNKNPqMX0noOm6Y3afkw5sVdeqG9gZcJwi8IbzvVpDlVOFeH9i3KCOgLslbJ9xgySWT_GycChladrNCvC7UFf60GQkzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
خاطره عجیب حنیف عمران‌زاده از وسواس‌های فتح‌الله‌زاده: حاجی توی عربستان چمدونش رو زیر شیرآب شست می‌گفت با دستمال کاغذی کنترل تلویزیون را بردار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107850" target="_blank">📅 11:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107849">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8daf57827.mp4?token=HzCgT57ZTnCJ_xraI9aqCqwkgk8brtRf3RJ2STJcH5SNtZXgKc0yZSUJoAlturYTLhb9F6HcTA6OFMf5ZspSVPIjUtIz54dF58uZVNe8pTQmz4jF35zXoYZVJC0BkPoyDdW3GyIc2s_aUr7XKJuR0HpupCW_mZX4DiLL8nIVOl6Vo-jV81GFG9F9zomyoymbnQZWsWoUryhYtjbWbBK65K8WdS9NzxL-uYPp6g_b8YweWIBl--tWaNr_79g9oc0xpXGWqePE5MurZBigqLgyP1bPoTRKAoGrRcogZMT1OIc_9PmDuPxuFC1MhHi5oJdgRF1Js2mqH0GW2VcNwd7elQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8daf57827.mp4?token=HzCgT57ZTnCJ_xraI9aqCqwkgk8brtRf3RJ2STJcH5SNtZXgKc0yZSUJoAlturYTLhb9F6HcTA6OFMf5ZspSVPIjUtIz54dF58uZVNe8pTQmz4jF35zXoYZVJC0BkPoyDdW3GyIc2s_aUr7XKJuR0HpupCW_mZX4DiLL8nIVOl6Vo-jV81GFG9F9zomyoymbnQZWsWoUryhYtjbWbBK65K8WdS9NzxL-uYPp6g_b8YweWIBl--tWaNr_79g9oc0xpXGWqePE5MurZBigqLgyP1bPoTRKAoGrRcogZMT1OIc_9PmDuPxuFC1MhHi5oJdgRF1Js2mqH0GW2VcNwd7elQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
‼️
سردار آزمون به دو بانوی تکواندوکار ایران یعنی ساغر مرادی و فاطمه احمدی که در مسابقات آسیایی مدال کسب کرده بودند،‌ نفری یک میلیارد تومان پاداش هدیه داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107849" target="_blank">📅 11:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107848">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👀
‼️
🇮🇷
صحبت‌های شروین‌بزرگ درباره پیشنهادی که در فصول اخیر از پرسپولیس دریافت کرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107848" target="_blank">📅 11:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107847">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107847" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107847" target="_blank">📅 11:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107846">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VklWgiLfGasu5smtoTGvZCPVE97Ux6ao5MeYrtrp9qbfyavp33J4GlrzpwYgfN22sMoKizHGNBcX8W0v97mhjR0SH7apVFi54ifbtnHTpfBXDMS1m200V6ocCw7j2873OO0uhlgg-ILf8WQys-rmNWfriYtEb8SOcCLdsJfshCfGxx8mjEp2gGE6Xf8O90ynUdYlEfS4gzgN0BkSe4M-Np3CTlGPZKQuWAFlc6PrJDIlbcB_71ahZgpgwlhlTXnkpep2BQFq8tsDXKuKfhKMo7nGcpVa6BP2cVJc9vovjUluwFjNz1naqo7fGZRsn8ux25eTlNYt3QUK7tje0gN9dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
بلژیک
🆚
فرانسه
ترکیه
🆚
ایتالیا
لهستان
🆚
بوسنی
سوئد
🆚
رومانی
نیوزیلند
🆚
ژاپن
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
https://TrexBet.com
http://T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107846" target="_blank">📅 11:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107845">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/294e1e1160.mp4?token=XXLMkEgDfQR7b_FxvJxWHdbCznT-JNS8rtEe7iLpbTl2I9ygV8ScJCYUTSQfr0mtUeztRDv6Gs2NykxkBSO11v-Qy8xCg6esZ_GcJygAgTW8VtMLD6oBdbOEwijyxWyY80r622Fuehl3Vk1td091dHbCPdFu4jnYxghuGQNk0k-gA2dtlbHWnw3HHVeh9i7MEgzKuDp9TdPeo-eYOYO82j2irNx_YDrZw5zCubHFk1rFZpdBqdZLWQfp18D2-4p84Dl1ZcL918PWSQtildPeJ1WNzGW1i4toa-TKd-mp_F1U7MWVKPg4OFpxeCJM7wv2oqLXf5y3nDV12y7650imlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/294e1e1160.mp4?token=XXLMkEgDfQR7b_FxvJxWHdbCznT-JNS8rtEe7iLpbTl2I9ygV8ScJCYUTSQfr0mtUeztRDv6Gs2NykxkBSO11v-Qy8xCg6esZ_GcJygAgTW8VtMLD6oBdbOEwijyxWyY80r622Fuehl3Vk1td091dHbCPdFu4jnYxghuGQNk0k-gA2dtlbHWnw3HHVeh9i7MEgzKuDp9TdPeo-eYOYO82j2irNx_YDrZw5zCubHFk1rFZpdBqdZLWQfp18D2-4p84Dl1ZcL918PWSQtildPeJ1WNzGW1i4toa-TKd-mp_F1U7MWVKPg4OFpxeCJM7wv2oqLXf5y3nDV12y7650imlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚪️
حاج‌صفی کاپیتان تیم قلعه‌نویی: امیدوارم در‌ جام ملت‌ها باشم اما قلعه‌نویی‌ دنبال تغییر نسله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107845" target="_blank">📅 11:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107844">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‼️
🎙
🇮🇷
🇮🇷
بی دلیل از استقلال تعریف نکردم؛حمید مطهری سرمربی فولاد خوزستان: کاش سهراب بختیاری‌زاده خارجی بود!
🔺
حمید مطهری می گوید اگر نتایج سهراب بختیاری زاده را یک مربی خارجی می گرفت، همه کار برایش می کردند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107844" target="_blank">📅 10:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107843">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFyC2uJpEiZyIDN11tFJkPOTF9D5kSyzYAF---nkBojEnx_LkcowftilbfvxgXk1SQd0NAWwUaE1eGkAFi4c46BdyRVptBJYeYzzCtZyUJZGJnXwaPgLIK7_fhHlxpxzS6ufd6opA2dnyv-kWRgWZtMGSAZaVZ7MLZtTrvu-PJrPi_kDDLbdDV9wejCzVBBzweIHLe19P0qxZ9MKPotxii2PnK03TWL855CGUgnnb2NPYO3EDRM0_jlCfPxzI_Er3CB8zLlpGGLLKhZc8cuRyi89NaZ9XvKa6FGWfmMJctfpExnka86Nr9L-0ntCqZiy9pxXRwEv0TXFLapBGdHW-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💸
گران قیمت ترین بازیکنان اروپا
⚡
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107843" target="_blank">📅 10:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107842">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75399136b6.mp4?token=pT2rs5EVjz5q0VHHFKtSu-Z30CFO08QPiQBYswDuKQAMJ4rpLqVzRpNI7DufYxsPCvNw7d8b-AIizLBeMyzOj_t7_UH6RNPbaHUNTjyE3bHaTnJzVX8UAE51Ez2WfU1pIbBKJEFU_mLkGG7KFMKGtwhOyYY-XbPgFUdGgtCkWi8lRu3aPQjAEUmeXSeBMtsD9po1vlUilKjF0KCblu1Ux8j4hNAAo1juZVGZkCkteDQIOWrtzGq5pBVVI8CWbteFATwF4BVQRTWZ0_0wVoPf2sL6wrT-EsCNaMg46THZ2y02XvQKj2ThC1uowBRH24MQrO-vGByRdrrOsmOhB99gyKTj3v_4j26qnNSSdf4gwShSXqGXiLuaYw1AUh82aK6lHHQFeJdjXfxbjqIxxRR_0ieVR--EEWmUL3-0NztwTsFW_FuMkO4mNjwAiK59QZ8Fgzhbugn7XqO8xDRvfYJSJ7ka7nEvUDmdrR1n90WcTmaKTO1RezsOGGKaeCV5Hgs7uCEZpxATg4xomlZ7gRDRxXCR2DuHJQU59pKWSAmGdPDN40_vTLxmhFJMpoBzpF0bSagCyKii9goFk2nZOfV9YzjncTqbEbVJ7_fi5NqBz-j04XwaAlb8sGfmFcbWCILZ1fHU70O9aY36xgDYZLQWbe5JFqEVmOxOu8iV6SJe5pM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75399136b6.mp4?token=pT2rs5EVjz5q0VHHFKtSu-Z30CFO08QPiQBYswDuKQAMJ4rpLqVzRpNI7DufYxsPCvNw7d8b-AIizLBeMyzOj_t7_UH6RNPbaHUNTjyE3bHaTnJzVX8UAE51Ez2WfU1pIbBKJEFU_mLkGG7KFMKGtwhOyYY-XbPgFUdGgtCkWi8lRu3aPQjAEUmeXSeBMtsD9po1vlUilKjF0KCblu1Ux8j4hNAAo1juZVGZkCkteDQIOWrtzGq5pBVVI8CWbteFATwF4BVQRTWZ0_0wVoPf2sL6wrT-EsCNaMg46THZ2y02XvQKj2ThC1uowBRH24MQrO-vGByRdrrOsmOhB99gyKTj3v_4j26qnNSSdf4gwShSXqGXiLuaYw1AUh82aK6lHHQFeJdjXfxbjqIxxRR_0ieVR--EEWmUL3-0NztwTsFW_FuMkO4mNjwAiK59QZ8Fgzhbugn7XqO8xDRvfYJSJ7ka7nEvUDmdrR1n90WcTmaKTO1RezsOGGKaeCV5Hgs7uCEZpxATg4xomlZ7gRDRxXCR2DuHJQU59pKWSAmGdPDN40_vTLxmhFJMpoBzpF0bSagCyKii9goFk2nZOfV9YzjncTqbEbVJ7_fi5NqBz-j04XwaAlb8sGfmFcbWCILZ1fHU70O9aY36xgDYZLQWbe5JFqEVmOxOu8iV6SJe5pM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇹
آنالیز انقلاب تاکتیکی گاسپرینی در این فصل با تیم آاس‌رم که حریف سختی در اروپا خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107842" target="_blank">📅 09:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107841">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‼️
🎙
محمود فکری: باید به قلعه‌نویی حق بدهیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107841" target="_blank">📅 09:25 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107840">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75fb30e6b0.mp4?token=Mj2SvkfvM8iVO8rBJgVJB-aYTB0gPS5vLst2Ob9khv3odhy2NfqgqiRD7XCiogV2G1CfZJZJwfvaEKkzgopINy_7hX1dCDofAaPDcKbE_JAjhSFNQC1Bxx4npl6a7gjb930QoDMKM6Gbqxj-Yj4oAXoiccQoOcI__MmYme_NXKceiLy56kaKgAhpNLf38Bj9456YRq8fYaBPAFJGVFbLEHLdbJGMsBqiLvXf7_Ml7s-f6DKO1wAn-q-h9QdaHiEWa7DkSD2_NLEfQ1C2fQMu70QfwGT6gJQwfxAyROHB8Tfylgzy3gyxNiAxhZeZfyovbiHNavNnIZf8PSLHn-6XpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75fb30e6b0.mp4?token=Mj2SvkfvM8iVO8rBJgVJB-aYTB0gPS5vLst2Ob9khv3odhy2NfqgqiRD7XCiogV2G1CfZJZJwfvaEKkzgopINy_7hX1dCDofAaPDcKbE_JAjhSFNQC1Bxx4npl6a7gjb930QoDMKM6Gbqxj-Yj4oAXoiccQoOcI__MmYme_NXKceiLy56kaKgAhpNLf38Bj9456YRq8fYaBPAFJGVFbLEHLdbJGMsBqiLvXf7_Ml7s-f6DKO1wAn-q-h9QdaHiEWa7DkSD2_NLEfQ1C2fQMu70QfwGT6gJQwfxAyROHB8Tfylgzy3gyxNiAxhZeZfyovbiHNavNnIZf8PSLHn-6XpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
فوتبال جا مانده ایران از امارات، از زبان شهریار مغانلو؛ دانیال اسماعیلی‌فر و برشمردن مصائب هواداری در کشور ما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107840" target="_blank">📅 09:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107839">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e551facae3.mp4?token=qynhh461FJvHXbBaw3OBAMsSOfMdOa4QjHzNPE6vH0SCjn79PqogZ0uXndCodaIXy14_I6vocyFGEswLRjMw_PuDjiAoPxbgh1XX9jMO2GaZfkJPziz9opuW-3V6_vCCN7wkxLi1GRkFAoaf5EpTXemJwwsNxPFj7V_uFUbJh-Pou1ld9MOi47TlCiIWKbt_da7oaIcBadUJqF-PcAzHOvuZfaVTBWFFC9oO2q5T1kfwRDDAP4OJ5iI32ddqbrju87WDyK_brJ1vfnumz3pB3A18N-JooxKyNzDu_KxuH2MLtWGX0pLbFv6W3nyU4aYnc-vbRKrbQS2aucuuyeyNLTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e551facae3.mp4?token=qynhh461FJvHXbBaw3OBAMsSOfMdOa4QjHzNPE6vH0SCjn79PqogZ0uXndCodaIXy14_I6vocyFGEswLRjMw_PuDjiAoPxbgh1XX9jMO2GaZfkJPziz9opuW-3V6_vCCN7wkxLi1GRkFAoaf5EpTXemJwwsNxPFj7V_uFUbJh-Pou1ld9MOi47TlCiIWKbt_da7oaIcBadUJqF-PcAzHOvuZfaVTBWFFC9oO2q5T1kfwRDDAP4OJ5iI32ddqbrju87WDyK_brJ1vfnumz3pB3A18N-JooxKyNzDu_KxuH2MLtWGX0pLbFv6W3nyU4aYnc-vbRKrbQS2aucuuyeyNLTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥶
🇪🇸
جدیدترین پدیده آکادمی لاماسیا بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107839" target="_blank">📅 08:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107835">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ra8z2BPdmUf0mYtPkEO51MlRHv3fd8M8mCgReO7xH6mOshbVle5-XGQn8Oy8Wrkw5MVhFWC9_PHztALIb8ORcinZ-Z_cIeYw7oVQOCNaChD_g9SsyPmIiXE5vMc1Zhcc9XZ6aN0uR9w-nx9AYdqKroWEnliwqsVigxs807zCpxe-7wOT10T8CkVNksNLPPjyVxExJPq3crF83eAB-k_zQn4LyCgn-d371eNB4qxc564VJGjYLMJqQk5M-YLftNt_FeggIknPjXhu8_JhXVNwDXSNt4WF45igMY6p5D3BIUe_HIF_yeL1DXGPWotobMHsaN2aqeUD60wynFcNG-4Hwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
🇵🇹
ژرژ ژسوس سرمربی پرتغال: آنچه بین من و رونالدو رخ داده یک سو تفاهم است که به آسانی حل می‌شود. البته این بستگی به تصمیم خود رونالدو دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107835" target="_blank">📅 00:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107834">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fb2_KYn_JjlbenLln87LReFE1SCxJlquRzBOwqilRzSpKgbyjWrTkvfzA7-o3x2GEwm18_A3nGzg3ZWwps7c93OpCMOPcPkg8ZIkw9izfFSnSMxBLZHVAsT9oIzUK4w1ClBVGkqiHDnMMqReCmnletyyEKx1HZgE773BsYjEl-WOMBl0kmTITNyJD52E3UqgTQbCcM3D5zjz2HgvS4oVMaRH0K3zUwk9yyv_cQQhhOMRY5Wt0jWy0SeTgONMLbylNdf1ooc6kH-amKnguPrInST9njg52S9aZ9SdRqdp9_080KMRzm7P5QOGSVwGSN8g-VhqJZfDrfNUXJDMPCKAMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
تیم‌ملی پرتغال به مرحله ¼نهایی لیگ‌ ملت‌های اروپا صعود کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107834" target="_blank">📅 00:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107833">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e30d963cb6.mp4?token=eRJ7MFvuzqM8cFBbjnqFvqpDjemxi6JK-mDtQYC2_CEZvl_2XFIoG_-kmhoRrX9Ed2QwMtW2sxtywf-6kdR93eTq-uPHv7tzD0Rzoo_Y3CugCIB7RAJ9atTQzfqbotoL2FrIe-BFMxqUu2NGvs9mW2N3ZNZUyYSvT_dPSSm4X10bPL45xBznXPySorSxFDpYaxK_VC9XRtdyL7P3h3v59pCWzfv8KntxJijBU-MbrcewzB2YoqcXV6ZvJ9zcr7u91TkIoEWrtL6rlK_d08-NVzqg7f1V7iAJyDtSZ5KBKOBdTIA9w0f2104XVs40bcBY6qbQnhse4Vs_cqLkQ1I30SVnoWv3GuEKjjOGE47YBkJMZjeuuZJsJhRSE_AlyRv1RNh8GugkxI6t58TZ3Oq5tADGy-i-K7MHvSQoadFAot_jAwIYJOpEuxGJBu_QjmOiNhQVNC4yiNJl88X7UMjIY7EnuzbdUJSTVZrNnj-O9AFfp3NqRfG7Q_8AnMTw26K5R0yIa-4pRLX8L-yU4LnmuF5NHDpuEOhb2b4tEIXfA9EYtmCu4Q7CS7iH_0DEWy4-ilYr57UfsY3nl5UkMoyFV2Wor7nHOSYySW9KhLOwXqqRksQiHzh6JyrZQ-zw_YgEJxi0cN-hxkXT2HgN8X1UNje6Kse0PRcRRcv6SP8jt0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e30d963cb6.mp4?token=eRJ7MFvuzqM8cFBbjnqFvqpDjemxi6JK-mDtQYC2_CEZvl_2XFIoG_-kmhoRrX9Ed2QwMtW2sxtywf-6kdR93eTq-uPHv7tzD0Rzoo_Y3CugCIB7RAJ9atTQzfqbotoL2FrIe-BFMxqUu2NGvs9mW2N3ZNZUyYSvT_dPSSm4X10bPL45xBznXPySorSxFDpYaxK_VC9XRtdyL7P3h3v59pCWzfv8KntxJijBU-MbrcewzB2YoqcXV6ZvJ9zcr7u91TkIoEWrtL6rlK_d08-NVzqg7f1V7iAJyDtSZ5KBKOBdTIA9w0f2104XVs40bcBY6qbQnhse4Vs_cqLkQ1I30SVnoWv3GuEKjjOGE47YBkJMZjeuuZJsJhRSE_AlyRv1RNh8GugkxI6t58TZ3Oq5tADGy-i-K7MHvSQoadFAot_jAwIYJOpEuxGJBu_QjmOiNhQVNC4yiNJl88X7UMjIY7EnuzbdUJSTVZrNnj-O9AFfp3NqRfG7Q_8AnMTw26K5R0yIa-4pRLX8L-yU4LnmuF5NHDpuEOhb2b4tEIXfA9EYtmCu4Q7CS7iH_0DEWy4-ilYr57UfsY3nl5UkMoyFV2Wor7nHOSYySW9KhLOwXqqRksQiHzh6JyrZQ-zw_YgEJxi0cN-hxkXT2HgN8X1UNje6Kse0PRcRRcv6SP8jt0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
گل‌دوم پرتغال به نروژ توسط گونزالو راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107833" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107832">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e974e0edb0.mp4?token=YkuZI81ffqzKuQPE76Yu5Ba5c2HHygRVLDVUfeo0H59qJouSu-NaPpp69X60cSh2beFMcGIthbv7-VAZZHCKant81zpb4UT2-L_qv2A2RVo2-obg2lqVGgoHSkZ3mwg0D9_q0ynLygSahMe1r2LR7U4nfEEd3gC3YQyiRIj2XkdNG8q52s4N7TkQE9oXJpjyJNUfijDlZfYuAaDzVxEHiE8CNkn6ePkQp8G_1-l28NK2EHh059fd54umU-V-Yx-RPbVS61Xrby6Xi7_JCufWeIxi_nebe4D0kLa5BBEyoMjgZSk3prqADh2xXSg1iyDLXrNgcWUWHVWWv--NbsGIAoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e974e0edb0.mp4?token=YkuZI81ffqzKuQPE76Yu5Ba5c2HHygRVLDVUfeo0H59qJouSu-NaPpp69X60cSh2beFMcGIthbv7-VAZZHCKant81zpb4UT2-L_qv2A2RVo2-obg2lqVGgoHSkZ3mwg0D9_q0ynLygSahMe1r2LR7U4nfEEd3gC3YQyiRIj2XkdNG8q52s4N7TkQE9oXJpjyJNUfijDlZfYuAaDzVxEHiE8CNkn6ePkQp8G_1-l28NK2EHh059fd54umU-V-Yx-RPbVS61Xrby6Xi7_JCufWeIxi_nebe4D0kLa5BBEyoMjgZSk3prqADh2xXSg1iyDLXrNgcWUWHVWWv--NbsGIAoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپرگل‌تساوی پرتغال به نروژ توسط ژائو کانسلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/107832" target="_blank">📅 23:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107831">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2872cf61d0.mp4?token=eeHX492SNFWPSVaX1INBULcWdy1HJOuz1tMhTegxqM8NSTB3bMhzhATG-ZuNWmEXiBd5vETE_hyCUrNW4F7Hk7X2eSeg-wmy2NHE31E9P_BnI0PkvuFWfciz5Xf3DSOXQQNiOOup9JjROV0sNzQlX_SSsc9dg_r048bWgJtuFpDmVD7_-9jCQmUlS3ma13NUGabE1SKevrl9UihAWJBWhRPQq2RNh2-M1YyfAkJI5URltpo7Vk1vnkkFqBqMiJQz5I1kCC3qvU275fpN1HsohRdNg37DRhgR3aSH_11-cvwKzSRKcjg1Dp54plWLbnx6VdAZfbvx23lslWhW7-cp2BZ9V9GRGkHU635IlWOR8pGpnNeMc0nRQ_FUbaBQwYeTQvteeFCiCTOmrGz4iJKiH9zBnijXqE0P_nZN-AGrqhd4ffu9jAvzbMMdN_4ti0iY7x19Ys3bzXNt5AAJ8rAKyqUkYvYaVnVEyTScX3ZO2zRY_AjtNzzq_r545FHHh8EgSVR_nYG8cKlMxkTxZ1QYBF0qzsAzOEhc3D31AlQPCXx1HtLZHMvdfuwvnNEn1Bi79kvGrcQ7rDUrBqT7nKzlth052k9vF-Zu9lsFHhqA1MzSQyWVUWv2ZCrdAu3GMjyJ4XoYD653Z7HJRgS6XDBSTWrlfj8FMjRsDUCWZD3qwEM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2872cf61d0.mp4?token=eeHX492SNFWPSVaX1INBULcWdy1HJOuz1tMhTegxqM8NSTB3bMhzhATG-ZuNWmEXiBd5vETE_hyCUrNW4F7Hk7X2eSeg-wmy2NHE31E9P_BnI0PkvuFWfciz5Xf3DSOXQQNiOOup9JjROV0sNzQlX_SSsc9dg_r048bWgJtuFpDmVD7_-9jCQmUlS3ma13NUGabE1SKevrl9UihAWJBWhRPQq2RNh2-M1YyfAkJI5URltpo7Vk1vnkkFqBqMiJQz5I1kCC3qvU275fpN1HsohRdNg37DRhgR3aSH_11-cvwKzSRKcjg1Dp54plWLbnx6VdAZfbvx23lslWhW7-cp2BZ9V9GRGkHU635IlWOR8pGpnNeMc0nRQ_FUbaBQwYeTQvteeFCiCTOmrGz4iJKiH9zBnijXqE0P_nZN-AGrqhd4ffu9jAvzbMMdN_4ti0iY7x19Ys3bzXNt5AAJ8rAKyqUkYvYaVnVEyTScX3ZO2zRY_AjtNzzq_r545FHHh8EgSVR_nYG8cKlMxkTxZ1QYBF0qzsAzOEhc3D31AlQPCXx1HtLZHMvdfuwvnNEn1Bi79kvGrcQ7rDUrBqT7nKzlth052k9vF-Zu9lsFHhqA1MzSQyWVUWv2ZCrdAu3GMjyJ4XoYD653Z7HJRgS6XDBSTWrlfj8FMjRsDUCWZD3qwEM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل‌اول نروژ به پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107831" target="_blank">📅 23:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107830">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d1f2465c.mp4?token=kDvMHCrIr5PG4CBoCAW29ge5mH4sHoXYW49y6lkzqAXM6LJgueRxZQ2WjJpCoIj8RaB3A9GEZIntdjQVdby-Uu0uUZwOru0BkgxgHuLo8PzEMlQzbj-VfprPcnv4_VU-U4ZOMBxgN32y03SeIylYUxbuLELu8lT8MmjZPSegcuXSgTGacmS0w8tnBhT91m3bf5Q1eZ92-ZCYvrEmormWVDirvSyM1uje5IytMNkA-NSGc-N12b3erbZJzriIvGAGcmnugsm2EqqHI3X5h5Y-rMN3Xhf2xYsjvvbovYxZTMnpBJO7phFvD4m59A2Z7Tnr1HTNzKdioal6aqmGcx70rwwUKLGyGKWpUaGvb2CrIwBeLOwJlTtjU_xT8yAk1FSvr2LfA9pFbzxOPxTx3TXPNBXswu2F9iF3cAZbsTMEsCLnDMk0r0ad1izr6-8qAqACh8G9EUVgSBJbLwihWjDSCrdQQ1PMdWzPTuaDSyvI17fL92T0U8d-7kRSruiEsRT0f4UzBfpVkfTicqfAxeDPm196VrrTVw2rFVaR38lsIYE9dpE3WY7q85-ZXclPPI3VLE0gk0keweIHJDbelMJZqxOr7gtO9Ss5bFckkc5HUnfTdlWgJScjxlC2aVQzNd20We1bouJUOLZnFUcWn_8riheGt7zOuwfQJOMF3iDbgUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d1f2465c.mp4?token=kDvMHCrIr5PG4CBoCAW29ge5mH4sHoXYW49y6lkzqAXM6LJgueRxZQ2WjJpCoIj8RaB3A9GEZIntdjQVdby-Uu0uUZwOru0BkgxgHuLo8PzEMlQzbj-VfprPcnv4_VU-U4ZOMBxgN32y03SeIylYUxbuLELu8lT8MmjZPSegcuXSgTGacmS0w8tnBhT91m3bf5Q1eZ92-ZCYvrEmormWVDirvSyM1uje5IytMNkA-NSGc-N12b3erbZJzriIvGAGcmnugsm2EqqHI3X5h5Y-rMN3Xhf2xYsjvvbovYxZTMnpBJO7phFvD4m59A2Z7Tnr1HTNzKdioal6aqmGcx70rwwUKLGyGKWpUaGvb2CrIwBeLOwJlTtjU_xT8yAk1FSvr2LfA9pFbzxOPxTx3TXPNBXswu2F9iF3cAZbsTMEsCLnDMk0r0ad1izr6-8qAqACh8G9EUVgSBJbLwihWjDSCrdQQ1PMdWzPTuaDSyvI17fL92T0U8d-7kRSruiEsRT0f4UzBfpVkfTicqfAxeDPm196VrrTVw2rFVaR38lsIYE9dpE3WY7q85-ZXclPPI3VLE0gk0keweIHJDbelMJZqxOr7gtO9Ss5bFckkc5HUnfTdlWgJScjxlC2aVQzNd20We1bouJUOLZnFUcWn_8riheGt7zOuwfQJOMF3iDbgUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
در مورد شکایت از یاسر آسانی؛
🎙
حدادی: چیزی که عوض داره گله نداره!
🟢
نامه فیفا به استقلال را خواستار شدیم
🟢
مدارکی داریم که بقیه باشگاه‌ها ندارند
🟢
آن سال هم هواداران استقلال قهرمانی آسیا را از ما گرفتند
🟢
رفتن کامنت گذاشتند عیسی محروم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/107830" target="_blank">📅 21:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107829">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2aee117f1.mp4?token=JgocnCvNVoKeJ1FVlk3i3Pk9nSM-XmK0aikZWt41GAP1Q6g8HW-kKZDeWGzu2HwLY3WgUNGrNCZ79WsqC7I1tBNx8Gmf8s-QMwz6XLZXkAe9l6wefM2mEJ4L-PttPIArFDwxme47rFdJ2Ur31RPoavuwVXa0UqoAZYen1vSFm344aLy-kRT3qLN1ao2mYOwOQyLQGBn-LBN8r8ngjAGFJml5gz4AckojW6dW7FfjCwxXaHpmcEllBXNoo33tcrqlx79BtjzjR8VtmLICHTfwV3rfZR-6j0c_0Bi_UuKO4ZYXM5Y665A5ahFDHSlKFii_Wu-t7QCCPn8RZMGuSu4WPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2aee117f1.mp4?token=JgocnCvNVoKeJ1FVlk3i3Pk9nSM-XmK0aikZWt41GAP1Q6g8HW-kKZDeWGzu2HwLY3WgUNGrNCZ79WsqC7I1tBNx8Gmf8s-QMwz6XLZXkAe9l6wefM2mEJ4L-PttPIArFDwxme47rFdJ2Ur31RPoavuwVXa0UqoAZYen1vSFm344aLy-kRT3qLN1ao2mYOwOQyLQGBn-LBN8r8ngjAGFJml5gz4AckojW6dW7FfjCwxXaHpmcEllBXNoo33tcrqlx79BtjzjR8VtmLICHTfwV3rfZR-6j0c_0Bi_UuKO4ZYXM5Y665A5ahFDHSlKFii_Wu-t7QCCPn8RZMGuSu4WPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👍
🎙
تمجید و حمایت زیدان از رونالدو:
"فکر می‌کنم اتفاقاً باید از کارنامه فوق‌العاده‌اش و کارای استثنایی که انجام داده تقدیر کنیم. اون باعث شد ما جام‌های بی‌نظیری رو ببریم، پس به احترامش کلاهم رو برمی‌دارم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107829" target="_blank">📅 21:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107828">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af8a71f26.mp4?token=K3yj69QzkArxQy-Wnls9TVEFXcFMEP56YepcCyeTatSDBVJVu1if_snsLW59z56l6EyXPq93z5Cq9JnEfuz1E5k0DJm0QLI27KcaaAYxAWpEIo2nt1v9PPzzVVwxfKKDRIbbwvCL2cyuj1Q6dZx3ktgAgqIU6LRd-mIu59znQH7h4FB0fOm5IKEfXknH-sQ55h0QcCJxlUTXBa81EAi_nNOXGvggyxMBZabOxgmckXXTIj2Q5PRkzIvQ3MjYahROmSbMuTeDFCjRf59BA1wGh7nyje8eoik9tFuARHvHQjA6nRn2UKkxFKjbPXiXfzsP780NKmGGC9y6bwY71cuhqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af8a71f26.mp4?token=K3yj69QzkArxQy-Wnls9TVEFXcFMEP56YepcCyeTatSDBVJVu1if_snsLW59z56l6EyXPq93z5Cq9JnEfuz1E5k0DJm0QLI27KcaaAYxAWpEIo2nt1v9PPzzVVwxfKKDRIbbwvCL2cyuj1Q6dZx3ktgAgqIU6LRd-mIu59znQH7h4FB0fOm5IKEfXknH-sQ55h0QcCJxlUTXBa81EAi_nNOXGvggyxMBZabOxgmckXXTIj2Q5PRkzIvQ3MjYahROmSbMuTeDFCjRf59BA1wGh7nyje8eoik9tFuARHvHQjA6nRn2UKkxFKjbPXiXfzsP780NKmGGC9y6bwY71cuhqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
پاسخ علی چینی پیشکسوت استقلال به مالک تراکتور: ما از منیریه جام بخریم؟ بیا تهران از نزدیک جام‌ها را لمس کن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107828" target="_blank">📅 21:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107827">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56554104cf.mp4?token=QGtKdQo4EZVdGBlgEvqNUxm0cyJude_EwuC3h1RJAQ2SNunKmEXARZdQj0qDJYcKehLrc9qMFdkAUW5j_JNJW1B6k7kJhpH2VVxPrpCs2ugyOLY6_t8YXRyG3ADfN8OZT10wrC0FA_ZWNn2zwF8nHnX1zfi5SgmCzN4hKKR7zwMswZPIDAc1WuWcqI2zWdYYR-5QgKZOfKF5HAkMCvssIQRHDqu8aW7sOouUaCHCi3IRrUF_SUKjusvwNSxx1h1GQ0nmEiTRLcd6_VKl_ayzq0g_Rk5MqXEgoj1f5dYz7d-XuCpjiooByEh_28MprmO40-tVx_maVQnnuUZb7d9yAaE46cgMRZyYl631xsq6lwqQEWaNex9YF99eUiTS0y05oYD14swHWUy6xi_tTLi3N9u33Xy6MSyfzSx7DTbQ5lRffO9dzeH2Tt7c8IbvZ7M2_X_er1axZ8Ep6IHhd2jkZMV_nEFnAjdqx3G7mpfvPxkyVnnMMLF0y03aqEndbcTxK3ZaMPxk4SrTcDmis2bqYfKqkHWTalhCBt-m64zUVcSdMmfxrEnliMcGFmVJWEiyAO5pFw19TmwKlD_Ats8MzTq6UXjDzZIIYg8m_Sl79R6BGEEzz8cgrud_pTnIBOJ-oDyYrLcdh2754tScEp-oaWYh4-3djOAcdZRMQzkrfCk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56554104cf.mp4?token=QGtKdQo4EZVdGBlgEvqNUxm0cyJude_EwuC3h1RJAQ2SNunKmEXARZdQj0qDJYcKehLrc9qMFdkAUW5j_JNJW1B6k7kJhpH2VVxPrpCs2ugyOLY6_t8YXRyG3ADfN8OZT10wrC0FA_ZWNn2zwF8nHnX1zfi5SgmCzN4hKKR7zwMswZPIDAc1WuWcqI2zWdYYR-5QgKZOfKF5HAkMCvssIQRHDqu8aW7sOouUaCHCi3IRrUF_SUKjusvwNSxx1h1GQ0nmEiTRLcd6_VKl_ayzq0g_Rk5MqXEgoj1f5dYz7d-XuCpjiooByEh_28MprmO40-tVx_maVQnnuUZb7d9yAaE46cgMRZyYl631xsq6lwqQEWaNex9YF99eUiTS0y05oYD14swHWUy6xi_tTLi3N9u33Xy6MSyfzSx7DTbQ5lRffO9dzeH2Tt7c8IbvZ7M2_X_er1axZ8Ep6IHhd2jkZMV_nEFnAjdqx3G7mpfvPxkyVnnMMLF0y03aqEndbcTxK3ZaMPxk4SrTcDmis2bqYfKqkHWTalhCBt-m64zUVcSdMmfxrEnliMcGFmVJWEiyAO5pFw19TmwKlD_Ats8MzTq6UXjDzZIIYg8m_Sl79R6BGEEzz8cgrud_pTnIBOJ-oDyYrLcdh2754tScEp-oaWYh4-3djOAcdZRMQzkrfCk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
پیمان حدادی مدیرعامل پرسپولیس: ما زور داشتیم و تورنمنت سه‌جانبه برگزار کردیم. اینکه قهرمان فصل‌گذشته معرفی نشد کاملا منطقی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107827" target="_blank">📅 20:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107826">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇷
۸۱ سال گذشت؛ کلیپ ویژه سالروز تاسیس باشگاه استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107826" target="_blank">📅 20:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107825">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZECAUj_2QJ8Na4kUI5uolS9NRcxDLAm544Bdv7-EJ7-gYg_OUG9ncX1AWdVL2BL9BuubwIs5Xf6DWkkDl7wnHvfr8Tr6rlKwEWZb74mtBd_-nLOXuyts3UmeyNnYF9dPEVw7iEGIg4T_s208djdTGj_Myrh2hXr74atuVcbWYNTzq2yuRz3HSvGuDNCMiGzXGd9TV2WmxJLt2ZpzUCGiqF3KTvZoIQe3FdVgcKsyLaCJdNnynp1eVSVAepgtvpbtj9TUtEzmZypuXM9Ix6lxPKkm0uPxwFIf9yM1ScrlFp8bo7isqQgoJL5d9cZ9WeIkLTyoff5To706PHywSfCMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
‼️
پیمان‌حدادی: قرارداد اورونوف را تمدید کرده بودیم که بتوانیم بعد از درخشش احتمالی این بازیکن در جام‌جهانی این بازیکن را بفروشیم ولی برنامه‌ریزی موفقی نداشتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107825" target="_blank">📅 20:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107824">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‼️
حمید مریخ مدیر برنامه یاسر آسانی و نزدیک به باشگاه استقلال قصد داره که شیرزاد آسانوف هافبک میانی 23 ساله تیم ملی ازبکستان رونیم‌فصل به تیم استقلال بیاره و منتظر تاییدیه بختیاری زاده‌ست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107824" target="_blank">📅 20:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107823">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50712b5d4b.mp4?token=lUTE04jSwkiCwxpwQZu-vctJbG6Brc_Qk2zN3O7R1sjUDdSu9A0OeM-bcA1B3tE9-7MrE1LC7U6-Qa0srx-RvwheDttavEPSPVZLjpsq83f43Y59o6rtjz5LRZTMynYV_07RAtlKhEHr3ThstEwBUSWzN-TcZkAgQmGkGMSF1QNXACmk1uU0ZRnOlMs84iteumC59m6mDVlikhBAJOeMcfvM3PRkObsYjYkd8hTNYjF6r0wtuyGQ8eG-ooote0RT5PxbCzlcesgqq2ptXjJw-HbHoSTJCg7v5nOd2H1jVTeEEvFY1Mk9T0EGnp9OPcnrS7ucPgwHcnaesBsWWM_kRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50712b5d4b.mp4?token=lUTE04jSwkiCwxpwQZu-vctJbG6Brc_Qk2zN3O7R1sjUDdSu9A0OeM-bcA1B3tE9-7MrE1LC7U6-Qa0srx-RvwheDttavEPSPVZLjpsq83f43Y59o6rtjz5LRZTMynYV_07RAtlKhEHr3ThstEwBUSWzN-TcZkAgQmGkGMSF1QNXACmk1uU0ZRnOlMs84iteumC59m6mDVlikhBAJOeMcfvM3PRkObsYjYkd8hTNYjF6r0wtuyGQ8eG-ooote0RT5PxbCzlcesgqq2ptXjJw-HbHoSTJCg7v5nOd2H1jVTeEEvFY1Mk9T0EGnp9OPcnrS7ucPgwHcnaesBsWWM_kRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پیمان
حدادی مدیرعامل پرسپولیس: قرارداد 5 بازیکن خارجی ما 4 میلیون و 80 هزار دلار است
🔴
در نیم فصل و تابستان بعدی بازیکن خارجی نخواهیم گرفت. ابتدای فصل بخاطر همین کادر ایرانی گرفتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107823" target="_blank">📅 20:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107822">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65b6b0e4ee.mp4?token=HngObQ9tHtuzZGJYO5HasH9yIiPyxbTRUN8FMuPhILUuuRCp8vv0w8qv5fUbuJX_JSh4yPWh0LyBcFlMPDlv_CiiwIwQByiCtMXE7CvhNFkZ_NERdBISBqLLa_wYqZylbpHf8v7DwexniDMUUsn_Ptr_bKUlTm3jOlcE3SALPHGZLGbGS-D6k_pNK4UecVjblIDjaMeF6MPLSlVzQxgtdYCyLFngOtX0MLvH-yO8O89Vm1qeLp9Ou3vD6tyDfgp1Ec0RzOtIt4BxRj-2FTn23SzUFJsS1lDJGwO-5Qh7Eoyr5Q7ZAKUH5EgovAI64kEHngMSSmeLKDRUvSfkxNNjGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65b6b0e4ee.mp4?token=HngObQ9tHtuzZGJYO5HasH9yIiPyxbTRUN8FMuPhILUuuRCp8vv0w8qv5fUbuJX_JSh4yPWh0LyBcFlMPDlv_CiiwIwQByiCtMXE7CvhNFkZ_NERdBISBqLLa_wYqZylbpHf8v7DwexniDMUUsn_Ptr_bKUlTm3jOlcE3SALPHGZLGbGS-D6k_pNK4UecVjblIDjaMeF6MPLSlVzQxgtdYCyLFngOtX0MLvH-yO8O89Vm1qeLp9Ou3vD6tyDfgp1Ec0RzOtIt4BxRj-2FTn23SzUFJsS1lDJGwO-5Qh7Eoyr5Q7ZAKUH5EgovAI64kEHngMSSmeLKDRUvSfkxNNjGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
‏همسر
بیژن مرتضوی: تو مجازی به آقا بیژن فحش میدید ولی تو واقعیت دنبال عکس و امضا هستید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107822" target="_blank">📅 20:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107821">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe589a60ed.mp4?token=PyrAH-JTqZq18jEvQKaBw80uiJ6Uk7_YX3ZgK8nFCFpeiT2MQu6CnkzIGClwO0omLlMNqAIIRMFrvf_DADYmqKYfEzrcd7Rf1XYiMLlFDwZgbk54bLRLB2p7q91lmVxYbQAXpwhJ7mf1E4xkDR1pOE4drc1pkjwP1NbCzcfg5VPGmTqC2G_vOiECDEWKEbCw_tY3GHlcNzbYR87ANFhDxFEigThhHtYRFpPx746DIBkafzbz2umxY8oh7pePymkJFvllpWk-jsLrqapXZ4r4oi-f1EGWIFWa0JBtIVGbg4y0fcfV1wCarifO3RLnUY_oNd7rdGQXu3tvEi2CET82lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe589a60ed.mp4?token=PyrAH-JTqZq18jEvQKaBw80uiJ6Uk7_YX3ZgK8nFCFpeiT2MQu6CnkzIGClwO0omLlMNqAIIRMFrvf_DADYmqKYfEzrcd7Rf1XYiMLlFDwZgbk54bLRLB2p7q91lmVxYbQAXpwhJ7mf1E4xkDR1pOE4drc1pkjwP1NbCzcfg5VPGmTqC2G_vOiECDEWKEbCw_tY3GHlcNzbYR87ANFhDxFEigThhHtYRFpPx746DIBkafzbz2umxY8oh7pePymkJFvllpWk-jsLrqapXZ4r4oi-f1EGWIFWa0JBtIVGbg4y0fcfV1wCarifO3RLnUY_oNd7rdGQXu3tvEi2CET82lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
اقدام تلافی‌جویانه امید عالیشاه برابر خداداد
😆
😆
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107821" target="_blank">📅 19:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107820">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6340210c7d.mp4?token=qAxx7mpeWkA_hxQ695TV_N9cBoEj36b7pxKDLdmG9Bn8rtL0ox_IICQJDbqmyjDu05JlcDvD8rBEuydrpN9Yik6KkDlbe5PJnl_tPdmH77DG5GMtsulDDuKwLOPzgN0a9CPCrNd_ehkVUM9wq9_ZJsqTYNXL0IYMTpBldu0joy_kK8FvgMvdr85TcHdCpE2wKrcVfhsAG0-g2PQGo6riE4_teRAUGwHhdmJnUCTiLO7hsD4jUJg_IYLa39CkOJdLrOLw2mhVZdUpG_CzMHa446SzQ8lN9JCB-dFNa4i-VzoSp62PpMmQFguUuCniQB3PkxU2WbOYvSYQCs7s0eY67w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6340210c7d.mp4?token=qAxx7mpeWkA_hxQ695TV_N9cBoEj36b7pxKDLdmG9Bn8rtL0ox_IICQJDbqmyjDu05JlcDvD8rBEuydrpN9Yik6KkDlbe5PJnl_tPdmH77DG5GMtsulDDuKwLOPzgN0a9CPCrNd_ehkVUM9wq9_ZJsqTYNXL0IYMTpBldu0joy_kK8FvgMvdr85TcHdCpE2wKrcVfhsAG0-g2PQGo6riE4_teRAUGwHhdmJnUCTiLO7hsD4jUJg_IYLa39CkOJdLrOLw2mhVZdUpG_CzMHa446SzQ8lN9JCB-dFNa4i-VzoSp62PpMmQFguUuCniQB3PkxU2WbOYvSYQCs7s0eY67w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
مهدی مهدوی‌کیا در واکنش به اتفاقی که برای کریستیانو رونالدو در تیم ملی پرتغال افتاد گفت:
🔹
«وقتی این خبر رو خوندم واقعاً ناراحت شدم؛ یک ابرستاره مثل رونالدو شایسته چنین رفتاری نیست. کسی که سال‌ها برای تیم ملی پرتغال همه‌چیزش رو گذاشت و یکی از مهم‌ترین چهره‌های تاریخ این تیم بود، حالا به جایی رسیده که اردو رو ترک می‌کنه. به نظرم باید احترام بیشتری برای بازیکنی با این سابقه و جایگاه قائل بود.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107820" target="_blank">📅 19:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107819">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae14913e57.mp4?token=GGb-E33evMjekm79k38DXkfJNHfWJJ9nm69M6dQGLH7w5XhSwFfRHiFvGn7cNo9GzFnd-FaqlvULggJnB3vQACAs2qmNxhxSeLn3cRcrmbebIVOku-dvVDV2kJF9q4QR4U0RCmKf14aioVSr-0km6xbcVcC_mXjik0Tdk9J5J-H46QEwrB0i0Pci1u-4Po362XMT-eQdL98SNdJD2EVQbCw8yArhtqTkepl39KU2g9PDtk0ZIEgJ08kl5owsv1m8YMTW64rN-GqQSLMaUksJjIVWPFWeJdGMmmyyxeKSTnhNa5BTqKe04v6gM_NYgC8dRG-N861-3HzVp0BKge3LsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae14913e57.mp4?token=GGb-E33evMjekm79k38DXkfJNHfWJJ9nm69M6dQGLH7w5XhSwFfRHiFvGn7cNo9GzFnd-FaqlvULggJnB3vQACAs2qmNxhxSeLn3cRcrmbebIVOku-dvVDV2kJF9q4QR4U0RCmKf14aioVSr-0km6xbcVcC_mXjik0Tdk9J5J-H46QEwrB0i0Pci1u-4Po362XMT-eQdL98SNdJD2EVQbCw8yArhtqTkepl39KU2g9PDtk0ZIEgJ08kl5owsv1m8YMTW64rN-GqQSLMaUksJjIVWPFWeJdGMmmyyxeKSTnhNa5BTqKe04v6gM_NYgC8dRG-N861-3HzVp0BKge3LsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
💙
فتاحی رئیس سازمان فوتبال باشگاه استقلال: نمی دانم پرسپولیسی‌ها علیه یاسر آسانی چه مستندانی دارند/ وقتی باشگاه السد قطر با آن تیم حقوقی قوی که دارد از باشگاه استقلال شکایت نمی کند یعنی حضور یاسر آسانی هیچ مشکلی نداشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107819" target="_blank">📅 19:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107818">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70613f964d.mp4?token=IKiwEo1B-Gy5CYLjaZvIOg5dq_43arm7Qj17SHRzhds8TmPfIhluJBMS8PXVzrI9QtVOpxlaQQyHs9bu9hDthF0lnu03EI05E4P-DIX_Mq-BooyTzQIFs87z52J7zdozJ5FYxsy2EPUKg8yVR1fWj3eNyDNi00wmeAlArmBihcfTUOplORoro11Ey38E2faB6e2lYmCavJv1H7JNpKA99Ft0NArrD9s_eivGbqg4lMtmza_TAEZ_85CUM0rrRHXW4cHA89tkNlcUc-OoDi-fsqhDFnjqRCEDx03fpYAW4npGDHzGpkWj-cSPE9zOoh00_BZAukOR0_9ME3dC2cdt2oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70613f964d.mp4?token=IKiwEo1B-Gy5CYLjaZvIOg5dq_43arm7Qj17SHRzhds8TmPfIhluJBMS8PXVzrI9QtVOpxlaQQyHs9bu9hDthF0lnu03EI05E4P-DIX_Mq-BooyTzQIFs87z52J7zdozJ5FYxsy2EPUKg8yVR1fWj3eNyDNi00wmeAlArmBihcfTUOplORoro11Ey38E2faB6e2lYmCavJv1H7JNpKA99Ft0NArrD9s_eivGbqg4lMtmza_TAEZ_85CUM0rrRHXW4cHA89tkNlcUc-OoDi-fsqhDFnjqRCEDx03fpYAW4npGDHzGpkWj-cSPE9zOoh00_BZAukOR0_9ME3dC2cdt2oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های امیرحسین صادقی بازیکن اسبق استقلال و تیم‌ملی درباره وضعیت وخیم اقتصادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107818" target="_blank">📅 18:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107817">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf836fb3bd.mp4?token=m6AZY8iIWD1QPBJSODSkKf9aX8z7HV3PVBNEVummAWmC-3CE8e8LGq4jz1_ubJ2cKDN_wAiCbbsx-SBmWNk0UgTty3pXpGBqRSnAOBUwtwOi38yMXOshyDu_FMWN1Xj41zSM5T4hOtHRC2_f_G8FX1P-byi1nSjUsv3D1-AQzYG_XCAsPUEoXzEg7W7oGMBbkDK4HuZ5-y38vQD50xH46S8L4EXOiS5nM30VEqEfol_GAY1GDe0F203FyBYLhW3vi4MH_XZUwSGvYRjDtrEQTFpksufTPJYmcuWm-eKfM7fYl0jgJ0yzaQ3mBP7ienTs2bCwfrbW4z2AK3Qz9CiM9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf836fb3bd.mp4?token=m6AZY8iIWD1QPBJSODSkKf9aX8z7HV3PVBNEVummAWmC-3CE8e8LGq4jz1_ubJ2cKDN_wAiCbbsx-SBmWNk0UgTty3pXpGBqRSnAOBUwtwOi38yMXOshyDu_FMWN1Xj41zSM5T4hOtHRC2_f_G8FX1P-byi1nSjUsv3D1-AQzYG_XCAsPUEoXzEg7W7oGMBbkDK4HuZ5-y38vQD50xH46S8L4EXOiS5nM30VEqEfol_GAY1GDe0F203FyBYLhW3vi4MH_XZUwSGvYRjDtrEQTFpksufTPJYmcuWm-eKfM7fYl0jgJ0yzaQ3mBP7ienTs2bCwfrbW4z2AK3Qz9CiM9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
فریادهای عجیب یه نماینده مجلس جلو قالیباف به همتی رئیس بانک‌مرکزی: به والله میرم خودمو جلو بانک مرکزی آتیش میزنم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107817" target="_blank">📅 18:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107816">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZxfMZaykNWyzMqd_FUfy-T2Krb2QpV53UGlFad-TgVF_bRH72hKuixcnoDSJyEsp5UKMrB3I0Bc1tdJdQ_bjPMIYk_iUeJEnKSVG-ZuUV2VCOijqL1Dy1z50_OXz4-fDjhtYnNUodEXfUDI8-ZN6ggBQ4tzsyvIwIxJCSgc-CSyRpPpHYujyktxKQjwyF5ok0tkFXfvuai5RyAJcNubqRLLTOewSgN4CQVzT-LnKbVLMr_v8-BI-fPUvQAkZhh8_Y0VDTeUDhq1LvwZUFNs8r4t9PFAFzH6LILvqRAwtfCUMYk0ppu_sn0pf20v-sHOwPgeMAgexT0LyIzKdjAU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
فدراسیون فوتبال پرتغال قصد داره برای فیفادی بعدی یک بازی ویژه خداحافظی با اسطوره کریس‌رونالدو مشابه اقدام آرژانتین برای لیونل‌مسی تدارک ببینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107816" target="_blank">📅 18:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107815">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0576436f6.mp4?token=SviMOvnfht2ZFvwcMOex3AbyF0f9YXuf95AYS5q4ycf8BqcG3HKIMfplyfHV0ZfJLbdYa4thLLNRyrsFqxoG5vHwfgIi7zMIVaFHCsSaL1Y4Jti9QGRjrvc3W6g9fNdnfl-mYkB_lKELGzc1Phhhw4zXi-roZLFD5jmqGvLAXHYqcNjwSldQW-QzhhFfYFBHWf2_uEQPZHwGu1RSgLiVi8kOQNZ1b2Itf1itqQX-y-8s60n1Ti3NhhRqiihEeAsLiR224xXud8D2b0ucBes5AibzG6NJDGcO-BVgQE4PF5NCB2kXHHahv1Vpc1BIwHP_ZJmg09OZfzpoE1a5SyXdZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0576436f6.mp4?token=SviMOvnfht2ZFvwcMOex3AbyF0f9YXuf95AYS5q4ycf8BqcG3HKIMfplyfHV0ZfJLbdYa4thLLNRyrsFqxoG5vHwfgIi7zMIVaFHCsSaL1Y4Jti9QGRjrvc3W6g9fNdnfl-mYkB_lKELGzc1Phhhw4zXi-roZLFD5jmqGvLAXHYqcNjwSldQW-QzhhFfYFBHWf2_uEQPZHwGu1RSgLiVi8kOQNZ1b2Itf1itqQX-y-8s60n1Ti3NhhRqiihEeAsLiR224xXud8D2b0ucBes5AibzG6NJDGcO-BVgQE4PF5NCB2kXHHahv1Vpc1BIwHP_ZJmg09OZfzpoE1a5SyXdZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚽️
مهدی مهدوی‌کیا اسطوره فوتبال ایران در حمایت از مهدی قایدی گفت:
🔹
هر بازیکنی حق داره بگه بهترین مربی‌ای که باهاش کار کرده چه کسی بوده. اینکه به خاطر چنین مسئله‌ای یک بازیکن رو به تیم ملی دعوت نکنیم، واقعاً نمی‌دونم چی بگم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107815" target="_blank">📅 17:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107812">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoYm9cciw4i34eromTVjBtphGqk8H904MnjXRDxdnXXr6lN3-6ucE1aM7EWYiIgNRUyHKxH5IxQR0l7LnhQyj-l22TumU1yCHnQediMuQtEDAfuKPFKa3mTQJKfelOBV7Urea7KhPVbK-IyutwKhazAX325HYFQ0dHT9XBmdpgVbVim73u0yLrBns6tbGwhM0ckJRfnvO0wy2aIBUlkDUdZeL9qimHq8SBGUUckcpqULkiLFo6UkMD2XYC3JD1DWKfdKMYnOhJkAs_i9A-4hpns4u96iO_HojeXUGPWcuywP73BGUcWRhRhJh_MLyxf_2itGyhGo_leYEpOIjBpqrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
⚽️
براساس گزارش منابع خبری، یحیی گل‌محمدی سرمربی فعلی دهوک عراق قرارداد خود را با این تیم فسخ کرده و در آستانه حضور روی نيمکت تیم‌ملی امید قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107812" target="_blank">📅 17:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107811">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_DJnXKGf_-Nx3KcHIXApwh3JwoL1yS49GYoT35IarKOYhYo5nrN_vQGJISfZBeD_F6T4k4tlxjBxLvhHnShn8W-XUA3UI2jB5n1xbNlITL218OH-3fbW2WbBvf2GBCNuPvEiiy02T_HKTtGSosgWaRHQ0Uq9LhVylb2Aox3VrrA034CPl5Kggzv5uVX2igpyAiDDRLofNDqOat19uO-ygXn0qbeBLyh5Szp2VHq7UbDCIpHDaEGmwxiNM-oeuehZjnoU-_5VVQNLRr1qL9oTMnBEo0jOl1oR21z0KeX0W3xRNN23S-FCoWvohdm2L_2d-DxRxkCrcGrk8uouJAGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
مارکا: اندریک از نیمکت‌نشینی‌های مداوم توسط مورینیو ناراحته و میخواد ژانویه مجددا به صورت قرضی از رئال‌مادرید جدا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107811" target="_blank">📅 17:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107810">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‼️
⚽️
لحظات تلخ احسان حاج‌صفی در تیم ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107810" target="_blank">📅 17:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107809">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0177fa0248.mp4?token=qJlo0sXk4XCWPybvzGnQ5VurLT_BrAb71-fxstpbeI2BWIpUKs0ZM7WrpK7cIDqutaxSmY6kiTbmsWYw0DOVLhy325HHugtJ5nDn52SyqEZgcgsy6C5fk6UT2pOTFmUOayD1n-qvaTb2y0oAnAFPRWbsUGjHV1uvzAKsvDNPuQijWGXsIBvfzIvqnG4z2QxB4-qhZKPe2Qrj5pXRhY5AoCSwhw8-bKlLfpY5Qn0_-UXe18qhgDJ4iQw0mqrveydMajyDV3ptdyCNi40OMtMtjKfg73X_6ZNBjE36F99QBvbBIwbZHeAu5C2s8nAfkwvfcWIUYtbkhgdQCTfW3VtAiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0177fa0248.mp4?token=qJlo0sXk4XCWPybvzGnQ5VurLT_BrAb71-fxstpbeI2BWIpUKs0ZM7WrpK7cIDqutaxSmY6kiTbmsWYw0DOVLhy325HHugtJ5nDn52SyqEZgcgsy6C5fk6UT2pOTFmUOayD1n-qvaTb2y0oAnAFPRWbsUGjHV1uvzAKsvDNPuQijWGXsIBvfzIvqnG4z2QxB4-qhZKPe2Qrj5pXRhY5AoCSwhw8-bKlLfpY5Qn0_-UXe18qhgDJ4iQw0mqrveydMajyDV3ptdyCNi40OMtMtjKfg73X_6ZNBjE36F99QBvbBIwbZHeAu5C2s8nAfkwvfcWIUYtbkhgdQCTfW3VtAiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
⚽️
علی‌فتح‌الله‌زاده مدیرعامل سابق استقلال: قلعه‌نویی نتیجه نمی‌گیره؛ من بودم عوضش می‌کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107809" target="_blank">📅 16:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107808">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e1845ed89.mp4?token=EYFprEFkoM1ghiHoDznBvHsLyHQNjZ_EsKN0rVSUhDwfzs8e-m_jf6UTdrjMLFumUmY4L_1ktOBEyZCz3kl3wwRzCCtvKf5TrBL8q1V2qWtPwV2E7kjY8M6o2KLR8JAqfe-r4dsRoXRB8WacOLSBtzoqOmN4eNxiX446DMHTdpU562luns3UO3T9BS7EqHU2XgMiYUQ3IxuHp3w1ryLA0HkXqOLnmh2mwCsP-pP6L1y6rP6EGxekNatrL4Ws46lAM7tK0RpDw4fbCjs2svurAirhY6aqQJUj_-PVuIzG-869YbRGhes0WBR9rcRnvGli1fjg3mYUAeePKi33Q3FD6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e1845ed89.mp4?token=EYFprEFkoM1ghiHoDznBvHsLyHQNjZ_EsKN0rVSUhDwfzs8e-m_jf6UTdrjMLFumUmY4L_1ktOBEyZCz3kl3wwRzCCtvKf5TrBL8q1V2qWtPwV2E7kjY8M6o2KLR8JAqfe-r4dsRoXRB8WacOLSBtzoqOmN4eNxiX446DMHTdpU562luns3UO3T9BS7EqHU2XgMiYUQ3IxuHp3w1ryLA0HkXqOLnmh2mwCsP-pP6L1y6rP6EGxekNatrL4Ws46lAM7tK0RpDw4fbCjs2svurAirhY6aqQJUj_-PVuIzG-869YbRGhes0WBR9rcRnvGli1fjg3mYUAeePKi33Q3FD6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
میثاقی: فیفا دی سوم چیشد؟ اگر قرار نبود بازی کنید حداقل لیگ را برگزار می کردید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107808" target="_blank">📅 16:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107807">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63df69c40a.mp4?token=VDmZRICmmq2o_A_o7fdyQAyj_lVnnyR72-ioUtimF5vLoKxM_Aouzcv2744TRO_rqF-O4S292TiK3-1-JtvlyN4gOY7pKzlQ6KvxD6H21aRdTgFu2s2r1lW9VbLKuJfjriEXukyenpas4Cp6W8BbAAcTg2y1JR_fDxG0ArhFsFL22qn5L1lRVTMfwo4PF1WjzdIqketFuzdF0aZxaB8dspoq15srr2jEi3sxqs3PSMw9C1wjeJy_oMD7CnlYwdtQVe8Dkt1BEJKE2EhLCFmRSJa_b6SbrVtMRnETS3Xdqph4qpojwXSNCT0anM4-2Ir-lapy3i6fxYdNWBXm0r6M4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63df69c40a.mp4?token=VDmZRICmmq2o_A_o7fdyQAyj_lVnnyR72-ioUtimF5vLoKxM_Aouzcv2744TRO_rqF-O4S292TiK3-1-JtvlyN4gOY7pKzlQ6KvxD6H21aRdTgFu2s2r1lW9VbLKuJfjriEXukyenpas4Cp6W8BbAAcTg2y1JR_fDxG0ArhFsFL22qn5L1lRVTMfwo4PF1WjzdIqketFuzdF0aZxaB8dspoq15srr2jEi3sxqs3PSMw9C1wjeJy_oMD7CnlYwdtQVe8Dkt1BEJKE2EhLCFmRSJa_b6SbrVtMRnETS3Xdqph4qpojwXSNCT0anM4-2Ir-lapy3i6fxYdNWBXm0r6M4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
رسول‌مهربانی مجری دلقک و گزارشگر صداوسیما که با این الفاظ دیروز جنجالی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107807" target="_blank">📅 16:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107806">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dc22c75d3.mp4?token=fBTy5QEFkC0H8v6EhUmD9WO9XMEKhvHY6W8x8IhW8qWX-rFC2282W0neFnWizhljazMKEwKB_nHqWlUp2Gpmi5VvL77S8qGZrYmyOLqesLw0NsXFi6Y9qEtlSG0seO9P6isSMVS5q8IIhCKOHkcH7iZ3Q-ZUJ6sMhPACO7ZwPmUcn3B0znkD1STYrpW8Gh0mj6Or3VXdv0EtTyJB36TWNo-vGhV37DxcADqbdW9RzV-578r3bHR28Kdw4c1VFGXJtoCDpx8k89_sxt6JPzoM9ihSBEO8jY4lNFZ4iBmMCHFTcXwLvI_EuQ-r8VIhaWVeOTAYa_kn8mnchhVKugx8mhSRPZ7FHy_oZCllxEZ39WodPwmHS0S5sPyB5qbzrdip1jARvroX_Ciu-zFwYz8WmGNp1sVLOtyYUIxDhoe_-FwCXcXip4L5GkPKMmlOtTiMcg7YoASXMGexO5_qFzxwg7lQz2sD0DgeV6caRWdDPSpEAtjjb3q_ENB39vS_iXN76sYGG6E11J7yAlYlIyw1BPFTL--8Cs8utjOLiRzbZCjSX5FJyGvyRyvRYglmAIZhS1X4l9qsnyQz2AhJnW5mM3i1vPm0LnAwbaS_mdBo_x3dhJHfyYShB_6u9byvvqpglBjCAsRJ-H5TKERu6BNrhkzd-6WyNupJIAiWZK4BjwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dc22c75d3.mp4?token=fBTy5QEFkC0H8v6EhUmD9WO9XMEKhvHY6W8x8IhW8qWX-rFC2282W0neFnWizhljazMKEwKB_nHqWlUp2Gpmi5VvL77S8qGZrYmyOLqesLw0NsXFi6Y9qEtlSG0seO9P6isSMVS5q8IIhCKOHkcH7iZ3Q-ZUJ6sMhPACO7ZwPmUcn3B0znkD1STYrpW8Gh0mj6Or3VXdv0EtTyJB36TWNo-vGhV37DxcADqbdW9RzV-578r3bHR28Kdw4c1VFGXJtoCDpx8k89_sxt6JPzoM9ihSBEO8jY4lNFZ4iBmMCHFTcXwLvI_EuQ-r8VIhaWVeOTAYa_kn8mnchhVKugx8mhSRPZ7FHy_oZCllxEZ39WodPwmHS0S5sPyB5qbzrdip1jARvroX_Ciu-zFwYz8WmGNp1sVLOtyYUIxDhoe_-FwCXcXip4L5GkPKMmlOtTiMcg7YoASXMGexO5_qFzxwg7lQz2sD0DgeV6caRWdDPSpEAtjjb3q_ENB39vS_iXN76sYGG6E11J7yAlYlIyw1BPFTL--8Cs8utjOLiRzbZCjSX5FJyGvyRyvRYglmAIZhS1X4l9qsnyQz2AhJnW5mM3i1vPm0LnAwbaS_mdBo_x3dhJHfyYShB_6u9byvvqpglBjCAsRJ-H5TKERu6BNrhkzd-6WyNupJIAiWZK4BjwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🙂
بازگشت سردار آزمون به تیم ملی بعد از مدت‌ها با کمک متن هوش‌مصنوعی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107806" target="_blank">📅 15:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107805">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ab5019276.mp4?token=JVK16wbqE5LYcxlfK-Brk9uFS7FDQqqV-ss_p0NEmz3TDCqZoLHm35sx0Cq_lberZVd1TfXVqGXxMpQTjv4lnIdTZFEU-5yCfpvkd8QYFQpi5ZK99m7IQsTUphdD9bdrjJOskYCo8q4GKa0m84ejX5oKSutxHYgk8gFnuIE9OKamBSlYOMYG7JD2UOK-eE9LlimEGZSFn-EswMf6dpx0Onehat_4HCeNWkFxpTQkds6Pg5VYGLv3VBLYAQ3UOc7B1lTPSFX6jxRTbsITz3MimwZ0L4IxwKbReXmvHO76-zEyAye19B0vE5OxIAQAwP2pQjklUqoYnQwVTTS3vGr9sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ab5019276.mp4?token=JVK16wbqE5LYcxlfK-Brk9uFS7FDQqqV-ss_p0NEmz3TDCqZoLHm35sx0Cq_lberZVd1TfXVqGXxMpQTjv4lnIdTZFEU-5yCfpvkd8QYFQpi5ZK99m7IQsTUphdD9bdrjJOskYCo8q4GKa0m84ejX5oKSutxHYgk8gFnuIE9OKamBSlYOMYG7JD2UOK-eE9LlimEGZSFn-EswMf6dpx0Onehat_4HCeNWkFxpTQkds6Pg5VYGLv3VBLYAQ3UOc7B1lTPSFX6jxRTbsITz3MimwZ0L4IxwKbReXmvHO76-zEyAye19B0vE5OxIAQAwP2pQjklUqoYnQwVTTS3vGr9sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
ویدیو وایرال شده از شادی رتبه ۲ و ۶ کنکور در حین اعلام نتایج کنکور سراسری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107805" target="_blank">📅 15:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107804">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49b154fa09.mp4?token=SbZF-sOb7Yjy6j0e1Nvvuy-MyL3LC8FmR5VYeiqei1W7Df7Sk6mxyqZhB8Px46elhQbqtMt_dFNaMaESW_Uiz23iNqsy7MRiC5W3dAFCqF8EpYIbNth5uBuEt1gP_T9XiSKxfh8lrVZJ59VxB4DbEZbyogJRf84hzO2AFgDiOHLfDTFpbKAi2N83o2NdlA7U3903pF0adhue-wPkAEI6nIjg6A8NfgqKrq6A7VngwHVz_3ZPWoF2WAo0XoAqvbqHrfSS-Ih2-4O8rrrdm3zAEqAsNKjPbKqzwZoGm36m-F_-3c-l2EDrEt7232YZp4mboxk0AoK5oJnKI9TZRECVqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49b154fa09.mp4?token=SbZF-sOb7Yjy6j0e1Nvvuy-MyL3LC8FmR5VYeiqei1W7Df7Sk6mxyqZhB8Px46elhQbqtMt_dFNaMaESW_Uiz23iNqsy7MRiC5W3dAFCqF8EpYIbNth5uBuEt1gP_T9XiSKxfh8lrVZJ59VxB4DbEZbyogJRf84hzO2AFgDiOHLfDTFpbKAi2N83o2NdlA7U3903pF0adhue-wPkAEI6nIjg6A8NfgqKrq6A7VngwHVz_3ZPWoF2WAo0XoAqvbqHrfSS-Ih2-4O8rrrdm3zAEqAsNKjPbKqzwZoGm36m-F_-3c-l2EDrEt7232YZp4mboxk0AoK5oJnKI9TZRECVqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
👤
👤
مشاور قالیباف رئیس مجلس:‌ تا به عادل فردوسی‌پور تذکر دادم، مطلب حمایت از علی کریمی را حذف کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107804" target="_blank">📅 14:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107803">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezkSYJPNoSRQrfdM9wiF3IrB1KIttNvACSryzUUnTVkSKmkE54GkXCeYeF4-WzHnUDNbsqTaTBS-lgcF2N7DJeslrmkfYGyBaidwdCaDLaIbyhVzj4m_18RVEKUeFIsiEcAnqYgch1UGP02xSS4NTT9kBgz92VxVotx_29UJK4PTVO-jJNronDJpAfEXZu_D9DzIS3RG_QSe8iFCiQxx3f8_5QiocdXQw4JxEepD98Wl92sOgW0AFY_TWrAqN1vRcWagT9pghjkkdFM_rnR0vbgcoIkdn14dQZqVbZ_ldiks377I_5sCDgwa54pxd0jOu4_RDWZNP62rqjP3JUBHEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇹🇷
وضعیت وخیم ترکیه در لیگ‌ملت‌های اروپا؛ بازی بعدیشون جلو ایتالیا هست که آردا گولر بدلیل دریافت اخطار محرومه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107803" target="_blank">📅 14:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107802">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e464e1d963.mp4?token=PMlj_bm2cp8A97jfhJeDsKs66Bd0nf3HPtaVERL7g-ZKjUzmQNYQ3QheNbAQxCPh8u41L2fO7B4tSwaBGwczQRYO2bq07DRgp73jhDaMc39aFurtf8tVCPPsNF9rWPu8_-X4iatQYFqYtdGmPjNCCFhDH2GKXf5WMZ8O118bZbMT561s6_v_eVB7pKCaR6_8pQIWnqrCRc0IgKktnUpWprOrsrWFa1dEfW_RCWS9bhm9eydU27r8jcOwQ5tK842zWP7hakFEeT6chZV-bczDYtPWRjWKGEoi7VRwrPYSKm9PfzcWfRJaP_29VHy8x35wMWTX7HDeMmziF4Osqal7t26-bUPtC5qp3JT-8BR5fn3Gvm_99uit06VeFRRlEZNfFQ_q3dX2ofbG0qEG-6eBnS-e3NSuPS-jicVd22rElXDj9oTqYD6pgUZOj1F4ulkIvZRMjki5rO6YMhwi7rX5NWbaWl7GDTSvs60Tidjciq_y_4KvJvg7dcokWJYoZgF5N5VqdLyF5CprR66Sj116vpLouWQk550kNhHV_47ljY3-CJh8dEUPyglKmmmqXK7I9eAu-ZYMZQxrlkojoAUi25shqVEjnz176z8E3727SY1PZ6pZu6AAhg3mq4e3cv8F02YqtPL6zzE77820BjI_OjEswcg7DrIYolXNEAY3cjc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e464e1d963.mp4?token=PMlj_bm2cp8A97jfhJeDsKs66Bd0nf3HPtaVERL7g-ZKjUzmQNYQ3QheNbAQxCPh8u41L2fO7B4tSwaBGwczQRYO2bq07DRgp73jhDaMc39aFurtf8tVCPPsNF9rWPu8_-X4iatQYFqYtdGmPjNCCFhDH2GKXf5WMZ8O118bZbMT561s6_v_eVB7pKCaR6_8pQIWnqrCRc0IgKktnUpWprOrsrWFa1dEfW_RCWS9bhm9eydU27r8jcOwQ5tK842zWP7hakFEeT6chZV-bczDYtPWRjWKGEoi7VRwrPYSKm9PfzcWfRJaP_29VHy8x35wMWTX7HDeMmziF4Osqal7t26-bUPtC5qp3JT-8BR5fn3Gvm_99uit06VeFRRlEZNfFQ_q3dX2ofbG0qEG-6eBnS-e3NSuPS-jicVd22rElXDj9oTqYD6pgUZOj1F4ulkIvZRMjki5rO6YMhwi7rX5NWbaWl7GDTSvs60Tidjciq_y_4KvJvg7dcokWJYoZgF5N5VqdLyF5CprR66Sj116vpLouWQk550kNhHV_47ljY3-CJh8dEUPyglKmmmqXK7I9eAu-ZYMZQxrlkojoAUi25shqVEjnz176z8E3727SY1PZ6pZu6AAhg3mq4e3cv8F02YqtPL6zzE77820BjI_OjEswcg7DrIYolXNEAY3cjc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حضور بیژن مرتضوی و همسرش در دربند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107802" target="_blank">📅 14:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107801">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82e592cb76.mp4?token=qM1PHrco89ixWHvfQ-J0SS73eZnX1_QStGe6Q7K8bLPQwxW_TlblaxqPuFW17C7VDwL6SeREDVvOQwn4geDfI05Hf0nomQ7elukKBV1qvm7NcAuS1iEiDlGi-kXUGMt7ElxfGBD0PSSuCO0FEeNqj9xpJTsMHVdJnLdrXuRkQlH3VVd8aV9Y5LNvbtHiHfVgoI3e55ex4nOgQTdE2Nwbx8PaM4T7YTtFNLZeBguu_hZVjslRYhEFrnpcPxN_RY_CP6yPG8Sv4wQuRDUXq88wj8wdkEUVSL9KfoGAdPGVmeBQIZ6lQ_-efjbknkWAo_GyVH_Ciyt4i0r9Toj75RusGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82e592cb76.mp4?token=qM1PHrco89ixWHvfQ-J0SS73eZnX1_QStGe6Q7K8bLPQwxW_TlblaxqPuFW17C7VDwL6SeREDVvOQwn4geDfI05Hf0nomQ7elukKBV1qvm7NcAuS1iEiDlGi-kXUGMt7ElxfGBD0PSSuCO0FEeNqj9xpJTsMHVdJnLdrXuRkQlH3VVd8aV9Y5LNvbtHiHfVgoI3e55ex4nOgQTdE2Nwbx8PaM4T7YTtFNLZeBguu_hZVjslRYhEFrnpcPxN_RY_CP6yPG8Sv4wQuRDUXq88wj8wdkEUVSL9KfoGAdPGVmeBQIZ6lQ_-efjbknkWAo_GyVH_Ciyt4i0r9Toj75RusGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇮🇹
یک‌دقیقه با درخشش دوناروما مقابل فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107801" target="_blank">📅 14:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107800">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5581b57d8f.mp4?token=Q8XfrjLgDaew550fwikBYRKRXwZ2dhaW1xrdOu-KxALQIdlQOMp4cei4S7P6ZIFsuoH1_luYntsyyZADAL9Ab-P32yRHYK17ywIIKUBj0nJK8KoKmmXQg47SO33x3VoE8y6s_mNjae_LV8jA8xJaM4yTcA-SbAI-S3OPj9jac3QeshYEgxP3-pvphOvFyHfoHMNvgw5_47wj7LYPWor_WHcn2Ch2L_UPhXJpSJTVenW7glRUnnRCgrSHyXwA8aZmDBXwg1hazXPO4Hw1HuDYY8YGo3M7tgeAX5arxs1Ju5SxwAsHvIwHyIcXhfuzZGbA-hsZCuprPXypis2-eC1OBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5581b57d8f.mp4?token=Q8XfrjLgDaew550fwikBYRKRXwZ2dhaW1xrdOu-KxALQIdlQOMp4cei4S7P6ZIFsuoH1_luYntsyyZADAL9Ab-P32yRHYK17ywIIKUBj0nJK8KoKmmXQg47SO33x3VoE8y6s_mNjae_LV8jA8xJaM4yTcA-SbAI-S3OPj9jac3QeshYEgxP3-pvphOvFyHfoHMNvgw5_47wj7LYPWor_WHcn2Ch2L_UPhXJpSJTVenW7glRUnnRCgrSHyXwA8aZmDBXwg1hazXPO4Hw1HuDYY8YGo3M7tgeAX5arxs1Ju5SxwAsHvIwHyIcXhfuzZGbA-hsZCuprPXypis2-eC1OBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
دزدی مسئولین از بانک‌ها سوژه جالب و وایرال شده مهران مدیری در مرد سه‌هزارچهره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107800" target="_blank">📅 13:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107799">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
‼️
⚠️
درگیری‌شدید و خونین در مسابقه‌ای از لیگ زیر ۱۸ سال کشور که در مشهد برگزار شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107799" target="_blank">📅 13:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107798">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46755fa2d0.mp4?token=DEznA4RgjwCf8mM_3WNoyWrK5piW4yreqFO1jxbKJIvm3oZo3v9dMbAYPfdtVqelVYBvqXYYuQVZGH5_jaYBnEK_9wCpa-3h-zIWxrJvev4wA5PNPs76abLQpTsCKTXDEH064CtdxeCoY88XbbvzjxMkA6KWRPntx0eQbfOaQLP_vFouYB-3ruo4IjQnsj7rLinQpOg9F-oqpAUeKlQp1RNY0vv86wt6QusYhDaBrhSZOinw7j9q5qJ9PsL2EVhYx33Gz5wH1GOGnCnfbXpibKe4Vlkk43iYK0rqROxykBLdRDJRqSUz-y29ivBXrLWzQ7prGW6ILrp-K9H_mURtiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46755fa2d0.mp4?token=DEznA4RgjwCf8mM_3WNoyWrK5piW4yreqFO1jxbKJIvm3oZo3v9dMbAYPfdtVqelVYBvqXYYuQVZGH5_jaYBnEK_9wCpa-3h-zIWxrJvev4wA5PNPs76abLQpTsCKTXDEH064CtdxeCoY88XbbvzjxMkA6KWRPntx0eQbfOaQLP_vFouYB-3ruo4IjQnsj7rLinQpOg9F-oqpAUeKlQp1RNY0vv86wt6QusYhDaBrhSZOinw7j9q5qJ9PsL2EVhYx33Gz5wH1GOGnCnfbXpibKe4Vlkk43iYK0rqROxykBLdRDJRqSUz-y29ivBXrLWzQ7prGW6ILrp-K9H_mURtiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🐐
از توماس مولر پرسیدن: «مسی یا رونالدو؛ بهترین فوتبالیست تاریخ کیه؟»
جوابش؟
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107798" target="_blank">📅 12:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107797">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad1675b1b.mp4?token=j5M5EMoqfDv_FMWbpJXxQn41qUIIw6Ufi_XwwJclH9L-ZLWXvj8jNASQ0bsa7jIJzZN5EoCn3u0hqi_46GjI1vsBku6MoyIfzOXkRiBzDZRv-0kJ3BaHrw1Gg3O4j7OdBYTAW7zrdmXRAigr8EptYawprbBzlEXrciuPKdsn351Zp4uUhWuB84ULjMVTUDEVcejst7V2SL5Z0WY2CLBxEJi5C8be5ioa6FD0Se4G_kUxh-OGtjgp3b1iKi-jFkw0VITakAXLuBSZjmsASoJ2uyfAspk_z_HtuYIeYVtsUh-5aTDTbT1CcWgYq6FQWVXp7PDnLM6LNEynlObsVUu-5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad1675b1b.mp4?token=j5M5EMoqfDv_FMWbpJXxQn41qUIIw6Ufi_XwwJclH9L-ZLWXvj8jNASQ0bsa7jIJzZN5EoCn3u0hqi_46GjI1vsBku6MoyIfzOXkRiBzDZRv-0kJ3BaHrw1Gg3O4j7OdBYTAW7zrdmXRAigr8EptYawprbBzlEXrciuPKdsn351Zp4uUhWuB84ULjMVTUDEVcejst7V2SL5Z0WY2CLBxEJi5C8be5ioa6FD0Se4G_kUxh-OGtjgp3b1iKi-jFkw0VITakAXLuBSZjmsASoJ2uyfAspk_z_HtuYIeYVtsUh-5aTDTbT1CcWgYq6FQWVXp7PDnLM6LNEynlObsVUu-5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇹
عدم‌پاسخگویی سرمربی پرتغال درباره رونالدو در نشست‌خبری پیش از بازی با نروژ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107797" target="_blank">📅 12:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107796">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a683578dd.mp4?token=f18YwemsowKZBJYLviFQKBTyHxkOzGWECTP6raOv0sO4OAWR_3cW5J_BhErGlE152l3Z1dzH-pd-eaLLmXZDfT5OhKcrzhsAZ8h7sQ6C9SmE1Ti-sqMmtM8G5HPAdH1nEZA0mdOVZlURUNb-X8Uo5GPsJI5d6-d0g6vH6ZDEnU801g9QodfTcwcl6I6qr5uonduSCti26LmIGfWEfNqcx5Bjv-ET1Yn9qtGYTo_e_EM3O7NX34dlkpAwZ_VWnUawdv0L4K3GDFm4e8SeakLf43XN0WJXUTTI33wm05VMaeLyJiYxd4_fXJOxxSNQC9-WE72RVe3RAVjd8UJAv0rGFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a683578dd.mp4?token=f18YwemsowKZBJYLviFQKBTyHxkOzGWECTP6raOv0sO4OAWR_3cW5J_BhErGlE152l3Z1dzH-pd-eaLLmXZDfT5OhKcrzhsAZ8h7sQ6C9SmE1Ti-sqMmtM8G5HPAdH1nEZA0mdOVZlURUNb-X8Uo5GPsJI5d6-d0g6vH6ZDEnU801g9QodfTcwcl6I6qr5uonduSCti26LmIGfWEfNqcx5Bjv-ET1Yn9qtGYTo_e_EM3O7NX34dlkpAwZ_VWnUawdv0L4K3GDFm4e8SeakLf43XN0WJXUTTI33wm05VMaeLyJiYxd4_fXJOxxSNQC9-WE72RVe3RAVjd8UJAv0rGFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
دهقانی، مسوول مسابقات بین‌المللی فدراسیون فوتبال: باید ورزشگاه آزادی را همانند نیوکمپ بارسلون مسقف کنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107796" target="_blank">📅 12:07 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
