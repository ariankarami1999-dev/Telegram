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
<img src="https://cdn5.telesco.pe/file/Yg0vjgrv1Ox2Ty-ArkAxqB_5TKLeR3ZWGpdFSEFx6-OIZDkKfrwy_0R5jnVa_gzUpsOWUK1dVV-5JgBxsIHP_VTVbk73YU1FDTmCTbYpuWa3Wu83z46eCsORyolQ4irgm_pQlnFoPnG_4YpcFoSmzEtYJGq93aRc-nqxYFZMyVMCMtXFUBv3Ow1G8E9U-Q-3x09DqIX3WWNdcRdFZKnCvy76Yq0Xy92x3MeCVKzYrr6A3HpWAKHUkwk1cu2HM3Tf5YuRcUnAbQbbxhs-eXPx-Xo4j6IPSq7fHMJ_tZN5FOtJEs5HlSsliEI3Xexc0fEB_n-BMTxjqCNHAEIoXn_fhQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 657K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 20:14:51</div>
<hr>

<div class="tg-post" id="msg-97659">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a57b10cb97.mp4?token=ATfOgovPvivIfg7i2uSwo-En7tcLgNbbKCsNbZA1WhgmD-JFtxU1sTMd7JpwVVnCkLxi2ghJCBiv0Fg1xSUK3qDs-H-yUgb-xFQ-5QwQ-4oWDnExB2uWHk7HFKL1OZ-onVMAotFuKtLB8d6XNqKwzb99cfUsWKGUCvOhXw7JFXorLT8E2-gClRlR4C1aanLi5XSxauktrHSXryL6WXglQchjZutQ8ThzEucyZ-sKk-XwUPw4CbEBY5v_6eDCVp78OoMi-m8hDy5HXnFdJAHPZAEhOBFv-E_VlsyBcbg_H4iqaqivAvyMiRaRvv8iPeUAL7skItJQKIUgdQL4aAszSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a57b10cb97.mp4?token=ATfOgovPvivIfg7i2uSwo-En7tcLgNbbKCsNbZA1WhgmD-JFtxU1sTMd7JpwVVnCkLxi2ghJCBiv0Fg1xSUK3qDs-H-yUgb-xFQ-5QwQ-4oWDnExB2uWHk7HFKL1OZ-onVMAotFuKtLB8d6XNqKwzb99cfUsWKGUCvOhXw7JFXorLT8E2-gClRlR4C1aanLi5XSxauktrHSXryL6WXglQchjZutQ8ThzEucyZ-sKk-XwUPw4CbEBY5v_6eDCVp78OoMi-m8hDy5HXnFdJAHPZAEhOBFv-E_VlsyBcbg_H4iqaqivAvyMiRaRvv8iPeUAL7skItJQKIUgdQL4aAszSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🏆
ذوق‌زدگی مردم کانادا از دیدن کریستیانو رونالدو اطراف هتل محل اقامت پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/Futball180TV/97659" target="_blank">📅 20:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97658">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCPxK-8P0vssjx7pTv960FBKwg11sqv_l2f8OE1pUSAWgXWEZSzH9Cor53_x4AS-f4VbXW3tOxmduzzmFiIEyegSdObk_NU1WeWpRzDXYx7IP-wCThEkIUK5wHrS0cyoycSWKddw6RLo9gNEpek-HhFC44tA_SeN8ACMzR4PGRtea2QFbQTBQR_hA1gketG0ZvwnlN777e8xh_SiwsahzKl8Clo83lKUmuP8wsPyqGPNjKXuo-BuJ9ovhWv2R8QTGcceMuLNdaslo-3TKPKtHuWWXGhBOVccnwz64cejVTcEaYKxhDMW8qFEYX0rF2kyrP6If50O2lfBv0afs58lfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
— نیکولا شیرا:
🇪🇸
رئال‌مادرید به توافق نهایی با انزو فرناندز برای انعقاد قرارداد تا سال 2032 دست یافت و مذاکرات با چلسی برای تکمیل معامله آغاز شده
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/97658" target="_blank">📅 20:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97657">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYdtOeNFeeGo-5KMDVvA0T-8na749d4f9Opkp3J_B5a2aRePXFad9FjJ9VpuOt4pRr1hD-RmKh0b5alefwbnVa1E3Qp_msXA3yCtPZ4jusjisSkn3o3Og7e8NLCTf-Wbik6_Qp_75ki2tvBsKURmZn-LC6_FDVEXZKZzV6C7P_fsPQhrlihUzfFL7YSleKgn_1-qNkMeHlL7e4CV1P0qqYN3lnGrLuoJs7KxaNn3LFx7cjtCBvy1aXjlQlYgE80INEzQx_iptktfTf1u1jDUDnHg7_OoP0x8eUIkvAl8egH0Z3dyIakO8SvYergMF4c6G2jKKUwySIGQg4OjrhDOcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇦🇹
🎙️
رالف رانکینک سرمربی اتریش:
"لامین‌یامال امشب هیچ کاری انجام نخواهد داد، ما تمام فضاها را در مقابل او مسدود خواهیم کرد و خبری از گلزنی این بازیکن نیست."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/Futball180TV/97657" target="_blank">📅 19:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97656">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnsdS0y41F9BlpVZZJel4OgacvxiNKsfoxh40W5CUaiCMcMkKmEF-Fuvj-vWM69-l4-HquUAd-H9SzILb1YRwOKeR5Cz9lGwv17ihhGI-HwFL9Eb46vptkoW7rowfPkQjMxw2FoJHyv-vDNoGe_hViKJhtwm07lOGOdf68YU83DMjFu7048MKJKd7-R0oZPsjDafKfgFtdgzYFwDQuX3V0-cKmFKfEomndn3V9UkZDYqMu61klJaD3M2cj27SSZgmtcDbGxgyAOPTUyS36gEJ-3KyOWUA5vB9LjRcrVRPPDb4zsQcmc4M7GRuMKmNxMHyAQTbqUonJYJyzG_kuHr4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💸
🔴
#فوری
دی‌ماریزیو
:
باشگاه میلان، ارزش رافائل لیائو برای فروش را بین 60 تا 70 میلیون یورو تخمین زده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/Futball180TV/97656" target="_blank">📅 19:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97655">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0b8DArmR3pJN8gdwz6jGdyaMYMMwpPUTKnr2fj-w6dsoHdJDY3Jl1gYx9_xXwkbtUgCfmOdrw3zjeUH4RQt1mkilbJHhu35Z9gYHTqB6VcbDAHNE0mOlF_CaykkWTZDbiMV2-l-PBb8Qi1xYmWafKZ7J-7cn4JnELY_Cogr1FEo4fnsXk_r5DDco3GKd3glNivvGQPS0lUezwTbo_8-cCWwEqXhGAo490WUZ09vM-qEQ9dVumzDqpf5jOnhisO0S-IwTxyljcE0UW2WEzl9i5iL98D3nNOY-h18zrec7VqqIcy6bb5mL24B7-gy8dUUlpOVxmCOeBwDHwVrBraG0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🤯
📊
یامال بهترین رکورد گلزنی و پاس گل در مرحله حذفی مسابقات بزرگ تاریخ تیم ملی اسپانیا را دارد:
🔴
— یک پاس گل در مقابل گرجستان
🔴
— یک پاس گل در مقابل آلمان
⚽️
— یک گل در مقابل فرانسه
🔴
— یک پاس گل در مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/97655" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97654">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/Futball180TV/97654" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97653">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pzbX6kCcanh9ocPeP8W45t2rwI0qv63gQRm50DLpJ9rJ2gKLoMFTEtShVyAb-7f8AN1a0zsmbBBDJGZYlOEEBBQ29W-RXEW1vQclMm6xTjOWlukbbQr9g15ADmR1TgNbnPhE7F55AEiJN3zRtmCdCZ067dJjZeNYvqHBfvlkLmG9S4XIuoduZNho-QJJ5rbzO0G1A2zTa0ZW8mkvmvUzj4aqaURE3oD7QN_9-YjHzvfj5WYT0k_WyVxamCcSpl9BM1ME8XIgefvutCoKu3DdbLlvSs7VlrDQp031WcWNEf7iMKpRfQghxVDTSqFr6tvriC02UkXehHv4Q-0Y7BoxhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/Futball180TV/97653" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97652">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🔵
موندودپورتیو: بارسا به قانون 1:1 برگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/Futball180TV/97652" target="_blank">📅 19:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97651">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4659792849.mp4?token=bZDHp8wQt3UDTOrTM_pMyEcemeFa3b-r_zv8_Lplsh2WSDSkbka5Io4TA26BfJUZeDI1ux_Rqt5a2DEMPLzesLm4SJojwWzf4Da9I3beYp8XyfL0rX0YN2LqX8UsKUiwB4jz8wrB9E-oCbCEXFMFI2Rx1JlY5FDJSZdfomw2v2dUi7OS49JoJHD7SGuwpF3domzg7tTi8JTyfXEIyr9QbsE4oUEug0Rky6FQeQSBkoyq0sGNOAvMO_9-O020mBGCD3DAldPeqhVryD4MB3ICfSWx4hyOFz3ywDms4U-ZqwPMw-RQpxVozgq_XvVktnKLuGvwzdhS9gPiZ-Ncn8on8oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4659792849.mp4?token=bZDHp8wQt3UDTOrTM_pMyEcemeFa3b-r_zv8_Lplsh2WSDSkbka5Io4TA26BfJUZeDI1ux_Rqt5a2DEMPLzesLm4SJojwWzf4Da9I3beYp8XyfL0rX0YN2LqX8UsKUiwB4jz8wrB9E-oCbCEXFMFI2Rx1JlY5FDJSZdfomw2v2dUi7OS49JoJHD7SGuwpF3domzg7tTi8JTyfXEIyr9QbsE4oUEug0Rky6FQeQSBkoyq0sGNOAvMO_9-O020mBGCD3DAldPeqhVryD4MB3ICfSWx4hyOFz3ywDms4U-ZqwPMw-RQpxVozgq_XvVktnKLuGvwzdhS9gPiZ-Ncn8on8oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
متن خبر: خداداد عزیزی دقایقی‌پیش مدعی منتفی شدن حضور اسکوچیچ در پرسپولیس شد
✔️
❗️
🤩
واقعیت در پرسپولیس: جنگ قدرت شدیدا در باشگاه شدت گرفته و چند نفر اصلی بدنبال فرو کردن گزینه‌های خودشون به نیمکت سرخپوشان هستند. صحبت‌های خداداد عزیزی هم با دستور زنوزی رخ داده تا جو اطراف پرسپولیس متشنج بشه و به نوعی زنوزی از اسکوچیچ بابت نحوه جدایی‌ش قبل بازی حساس آسیایی فصل قبل، انتقام بگیره. اسکوچیچ همچنان نزدیک‌ترین به نیمکت پرسپولیس هست مگر اینکه زور برخی نفرات از پیمان حدادی بیشتر باشه...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/Futball180TV/97651" target="_blank">📅 19:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97650">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmz4V4dQmCsLtgBG8d8ZxW5esvwQs5inF7jdDTvpz7Kj5HytHGknpmh2iqlMIs5Q6DoZYZYZRmOAhNrLBaVOiS4gy0ogJWv-PNx80dAV9WsVClCUR0Fv19khXQNIvC8bZPlIV6uFLfoLMVAuDgD8JO5cUim1J24ByO712OPcUemBH3WFv1umvQ1WfAixlA7TamJXoWn7SRvblrnr8Z2N4h8YJE2CvzpAbGU3T5YXBqkn7990MGFit9RbCVlHRLkB8fhJX-PfNKQBHP92OUFrdsPluSwINxIN-ZEL6ZKkX0jYVQ3snjOJ5seBVXPAFA3xTacvEmuN3U063PQOkpKflw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
کدام حریف، سخت‌ترین حریفی بود که با او روبرو شده‌اید؟
🚨
🎙️
لامین یامال
🇪🇸
:
"نونو مندز، او خیلی خوب است، واقعاً عالی است، من از بازی کردن در برابرش لذت می‌برم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/97650" target="_blank">📅 19:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97649">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🔵
موندودپورتیو:
بارسا به قانون 1:1 برگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/97649" target="_blank">📅 19:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97648">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUygjnNANjNssIPJ4XcmmIM_fWGjWwthBE-vIQuPnLUC7QQ9p08A8HGrK6xX-jv5JzhQgEctlvryfk1yCR2idZYqG-4YGVSwg1G0jBkMAVX4tYd172PAZly9RSCGqBhA2nft-78EzLSreP7bUWbpok1SfJPoj23J0UZMoFeVAw0RYkYRTl19Jrtiv_cC-p1aRjdXisluhXHD9C75ecRHcoug_DurM2yfm-8kPEuF_E3CU0oUqdVF5BzitzZwm2cHHaRRO5byHqVYC8TkcZI1XYyOOX0Iq7XP4rboiyXnLISxh3eRmyhQhcQhBDkhyA-BUoyO4H2Z8_UXtbg5uXNB8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
🇧🇷
فوری از رامون آلوارز:
احتمال خروج وینیسیوس در این تابستان از رئال مادرید وجود داره! باشگاه رئال مادرید از قبل با نمایندگان وینیسیوس در مورد احتمال جدایی او صحبت کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/97648" target="_blank">📅 19:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97647">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUviXAexIHm4n3z2U8CWj3s3jKLwooufYtZkVo86vldGXjxyoUWX0rbGZzLueDJPc4D07Kr6Y7SnzFLhOYNrl54t2C8bFT9_3E-DpssN1iiVU7LIRvu1z4BGfzdGzaxN8R7es4b7f6OhqZuqB6avmwnnnYwVGJUSRqu4Sl3BoNK3v_EqB9dCx9FgJQq7qQ6ylLef6jOM22dHi7TJzneGY4mv1tXypNfDdZS6Vrwuqkthk9mgUXeUsb-YNn_RnHTl6SU-35Rf46esBEik5HD-8Pm6NAYrZBixKdTPjVvRl-ipKX6ppPA2dxG1RnvDzSqsNWjF3UfJB79osMKCH1q-fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
فوری از فلوریان پلتنبرگ:
فدراسیون فوتبال آلمان به ناگلزمن توصیه کرده امروز خودش استعفا بده؛ وگرنه خودشون مجبور میشن اخراجش کنن.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/97647" target="_blank">📅 18:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97646">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irUqvSOudRgPfcv18IbzzJ3gT4wtmNB74-fzC3bgTSyAVIBSptmnjBsBP9hFL1RU1aXGFHTiUGCB17jJlosNhbiC52fW7eI7L3oTLEeFwRLQCtvuqo3fHKDeujk0AFFfsNMHzPi_EOslL4p24IxwOheG5b3J2B_Oyj0A4KSoOuM5wtKgusmUHYzTI5u6umwY9pMb7MceHeuFFYXghpUaA0UoJ1NqTtV3BEJVjftx7tdL3_WJwhDF-H-AttIuSCu4cZdSepnyDCAuyqdm85BJgbKZuD8DMe41eesTEtwOWl5BoojLYsrdihCl5gIYPG3RGT5RfP5phbidE0tMwll48A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🚨
اسکای آلمان:
یولیان ناگلزمن در طول جام جهانی هیچ گفت‌وگوی خصوصی و رو‌در‌رویی با بازیکنان آلمان نداشته و ترجیح می‌داده پیام‌هایش را از طریق ویس در واتساپ برای آن‌ها ارسال کند.
📱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/97646" target="_blank">📅 18:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97645">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f55154a43.mp4?token=dGf0hS0SzslDND8waSRDpVwUDBi8xsC0Rx7pk8Hg4DAPPyFriM1T-eL8_xDCBnxin4CW69g_thjFlf7MUseS7v-GDuBMFSf1IsE6FxZMmvcTMN6pqIRjAssM9lPIKkoRFOgIC-IduMtGkcU_8iSiaHcauKVF0BIV8ua49I1vq-hGPZ3OtJsXI9znTUpNZYf6kW3eIbmjJaH2FKMqEwLgCt8pztkFiac3sCSqSyRDGv1uufq0-npedR1fOXDVQlE8_nBqC3Zm5hHsr5oe_fKLntaHm1p4L-jQkrzn60fijVIhQBgaVDRi_TVPmRwmdjsF_7UqyCe-zpl1jK1t7lPUew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f55154a43.mp4?token=dGf0hS0SzslDND8waSRDpVwUDBi8xsC0Rx7pk8Hg4DAPPyFriM1T-eL8_xDCBnxin4CW69g_thjFlf7MUseS7v-GDuBMFSf1IsE6FxZMmvcTMN6pqIRjAssM9lPIKkoRFOgIC-IduMtGkcU_8iSiaHcauKVF0BIV8ua49I1vq-hGPZ3OtJsXI9znTUpNZYf6kW3eIbmjJaH2FKMqEwLgCt8pztkFiac3sCSqSyRDGv1uufq0-npedR1fOXDVQlE8_nBqC3Zm5hHsr5oe_fKLntaHm1p4L-jQkrzn60fijVIhQBgaVDRi_TVPmRwmdjsF_7UqyCe-zpl1jK1t7lPUew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇾
عاشق پاراگوئه و کوهستان هاش هستم.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97645" target="_blank">📅 18:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97644">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUDpE5Z0gqi9CiItg_g0CtGt4JnyQ1pte6HLsChSX_UbgTpA-_eRQ3mG_kjPDTpUwGAuAqspySyBaHmtj9JdwveJd10ksa3C9wF-2oNi8R8T4vjtNoeLXdI-pajAL7plDqla84it9KR8LQBsilJXM5U9WvCiFbL31sV5fKNYWHGOrUfb-lzhERKk7P55t3hd9idEf8PIjxF78hmT6m5b9P36p84Y0mMNm6-q7GnigT2N_7UoGstElR2vn_pOFiMXzoU_du3kgHR1lNfbebo4P1u7kiQLIxHTqH8qFS8zynW4KzTT3-EcXTx_F3EjiaQQabhXehQqQwsDN-W64GCvpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
بازی فردای پرتغال مقابل کرواسی، دقیقا با سالروز درگذشت دیوگو ژوتا مصادف شده.
🤍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/97644" target="_blank">📅 18:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97643">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQaDtMrdCKZXwHsHbgYDBDBMg-Y62G7x4ngOMAtoOqorfa-gvcWWpf1KM4W-pLU5x7wyfm9dogTjdUTTC3dlK6DPDWPUBTjVc1lbgnOxT4KhS59gByQaipO5WrIBND-zvm05Ub_8ttI0-01O5T-ZCkXBkrKyz-mRxyvVt6x7ll9ofttS31xbtYulGBZR9sMGc1Bdt5esjbCYxE-ABAK1LCSH_TNmpH_PsQ96gHYApdN9Tuo3NnTVuNETN6KvXxACLjGG-GeZfLiDgynTmUCtg8Ynf8S4GYSZl5gXe7VzTdfawVWspvI4aiIiAlYlW1m5Gn7PyHPQn4fWns9uw2pnXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇩
سرمربی تیم ملی کنگو سباستین دیسابر قبل از شروع بازی مقابل انگلستان خبر فوت پدرش را دریافت کرد و با این حال تصمیم گرفت تیم را هدایت کند.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/97643" target="_blank">📅 18:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97642">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به مذاکرات دولت پزشکیان، قالیباف و عراقچی با کسانی که آنها را قاتلان رهبر و متجاوزان به میهن می‌دانید، آیا به نظر شما این آقایان حق شرکت در مراسم تشییع پیکر مطهر رهبر شهید را دارند؟</h4>
<ul>
<li>✓ بله، باید شرکت کنند</li>
<li>✓ خیر، نباید شرکت کنند</li>
<li>✓ نظری ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/97642" target="_blank">📅 18:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97641">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a4c734a62.mp4?token=oAqVYqFuSeVlb5LJmD5v8wYMlBrS0rSN_s_ImIP_7JVyB0qM1FS_FB5OrWwVclw9gwSlngfN97mBmL6dgFNfewUPIPlUbxLN90dIbxwPD_m2HtGhCFEae1G2-2FibBQ9izxULM5ALBC1BT1HBJDe2o6lGj4pPehzxhhTACZR8xBivnZePVJQyMtbxz5iOZayQc-A4KWhpO-Dw-5sHfVMg40K2wL9QZefKNe7zO9NDRyjGEVNWOTUXUHlhWT1Yklcvf1467JM2rdXi1o3q8lsH9OTY15o1qc0uZMmEtkoHy_JCTSO1qeffnkpGSZ2pSkE7CYDHQbVmnuf61b88kdo1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a4c734a62.mp4?token=oAqVYqFuSeVlb5LJmD5v8wYMlBrS0rSN_s_ImIP_7JVyB0qM1FS_FB5OrWwVclw9gwSlngfN97mBmL6dgFNfewUPIPlUbxLN90dIbxwPD_m2HtGhCFEae1G2-2FibBQ9izxULM5ALBC1BT1HBJDe2o6lGj4pPehzxhhTACZR8xBivnZePVJQyMtbxz5iOZayQc-A4KWhpO-Dw-5sHfVMg40K2wL9QZefKNe7zO9NDRyjGEVNWOTUXUHlhWT1Yklcvf1467JM2rdXi1o3q8lsH9OTY15o1qc0uZMmEtkoHy_JCTSO1qeffnkpGSZ2pSkE7CYDHQbVmnuf61b88kdo1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇲🇽
پلیس مکزیک: در جریان شادی مردم این کشور پس از صعود به ⅛نهایی، حدود ۱۰ نفر بدلیل ازدحام جمعیت کشته شدند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97641" target="_blank">📅 17:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97640">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2308c1db6.mp4?token=YT1GAEnsu-SJwiyUvgoD_jUL7cc7HBIWtZD2Mkf57DOsnB1z5qnA1U-5pqWs8hACF2uRlBALolm_a7tyc9pD9Naykr2uHm4Y-K5EhESk9n9GzkHU30WTxOktjHcF-uAMrCRItKieOfB7dNn_V931oI3I59J9vTuJsY2Tp9urBhTpYfxWbq_sE9fS3rByX2Cnu181WnLYDu3EGKV2D6ZN8xSSGfIOGpdKpFFSRhrj9pZ5r8HvhLi77Q6i75v4N2iLLCXHcEsy_F_BDNQhX35wVAbPzt9m2ZztCRUew6AcLMta8uCT6lgOL84X58hszg60lCREDHvPVNwhTlE6KmOAAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2308c1db6.mp4?token=YT1GAEnsu-SJwiyUvgoD_jUL7cc7HBIWtZD2Mkf57DOsnB1z5qnA1U-5pqWs8hACF2uRlBALolm_a7tyc9pD9Naykr2uHm4Y-K5EhESk9n9GzkHU30WTxOktjHcF-uAMrCRItKieOfB7dNn_V931oI3I59J9vTuJsY2Tp9urBhTpYfxWbq_sE9fS3rByX2Cnu181WnLYDu3EGKV2D6ZN8xSSGfIOGpdKpFFSRhrj9pZ5r8HvhLi77Q6i75v4N2iLLCXHcEsy_F_BDNQhX35wVAbPzt9m2ZztCRUew6AcLMta8uCT6lgOL84X58hszg60lCREDHvPVNwhTlE6KmOAAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طوری که باز کیپ‌ورد و‌ آرژانتین داره پیش میره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97640" target="_blank">📅 17:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97639">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f7799c99f.mp4?token=G69aiw649HGhf25pf8J_4udU32DGPksvqXZ04Iil_ji0zgqXBfLSnyXAS_EisnBHQVmbnspgHDswajDcuVSE3XzX4RCfy9bIT7otbE6ncvPGZ8GeSuK3FuPLWXbUOsrvP4ITbjF_5xYFPawCI8xbH8Ishmq04ubHuREJdRS4UrLzb0mF30Lh9CibR4FzGvzWNdLbB6I0ZkMjuApsjiScQ7sMAbjPn1lGcg1PcULJvqOeuoEP9lpNGnl9UnRnUa_GQ6cR2aqZ81WmfhOjQOxPmAbAc3fO8mkHLubfjFIhq1kT8Q5ATYMlecQQomOFWQvHnscRUEIDcGuTUQMt1ZH6gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f7799c99f.mp4?token=G69aiw649HGhf25pf8J_4udU32DGPksvqXZ04Iil_ji0zgqXBfLSnyXAS_EisnBHQVmbnspgHDswajDcuVSE3XzX4RCfy9bIT7otbE6ncvPGZ8GeSuK3FuPLWXbUOsrvP4ITbjF_5xYFPawCI8xbH8Ishmq04ubHuREJdRS4UrLzb0mF30Lh9CibR4FzGvzWNdLbB6I0ZkMjuApsjiScQ7sMAbjPn1lGcg1PcULJvqOeuoEP9lpNGnl9UnRnUa_GQ6cR2aqZ81WmfhOjQOxPmAbAc3fO8mkHLubfjFIhq1kT8Q5ATYMlecQQomOFWQvHnscRUEIDcGuTUQMt1ZH6gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
وضعیت آقای‌گل‌های جام‌جهانی ۲۰۲۶:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/97639" target="_blank">📅 17:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97638">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad14f6b1ec.mp4?token=XHrKulCgeKmwkddhvUopn-I_GAFkP82kv22FcUL4PDnzgLm-1QjcwbMfvGE11PbAS9eR9bAQ3CQz-ojDjbWVIdHxg1vGW57_dO-Nlls3w1FRY6K8i6UxFxM49AUTdMOm1h29Rwd0oCNX51WAEHRmqSupBc3lLVm7F0jY0FeC3ZdNNdkQDXTxbimtLuLVp2AOT_-5Xn0OCjH4V-3YFR7lMurJ1xJpQYLiHHQX_hCYr5CV-FixZK3rPYdRmE_lneWyrb81rV0S-OkD8bHI3Z6KAdfxU5D4KuA5uOWk0l_dLTCAqm9mELwpSY93tliiW7UZgmmpv9qZ9H9XfyxHHVo3gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad14f6b1ec.mp4?token=XHrKulCgeKmwkddhvUopn-I_GAFkP82kv22FcUL4PDnzgLm-1QjcwbMfvGE11PbAS9eR9bAQ3CQz-ojDjbWVIdHxg1vGW57_dO-Nlls3w1FRY6K8i6UxFxM49AUTdMOm1h29Rwd0oCNX51WAEHRmqSupBc3lLVm7F0jY0FeC3ZdNNdkQDXTxbimtLuLVp2AOT_-5Xn0OCjH4V-3YFR7lMurJ1xJpQYLiHHQX_hCYr5CV-FixZK3rPYdRmE_lneWyrb81rV0S-OkD8bHI3Z6KAdfxU5D4KuA5uOWk0l_dLTCAqm9mELwpSY93tliiW7UZgmmpv9qZ9H9XfyxHHVo3gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های ستاره تیم‌ملی فوتسال بانوان درباره رقم قرارداد‌های بازیکنان در لیگ‌برتر فوتسال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97638" target="_blank">📅 16:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97637">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZd7cYtE18rMev5kfEXWwVFA01d7X5kn98sh_zSEgnX624vptuTEAQprd-BdnezlxHt1lZCDS9R2qHM0_7zObf8rem2A9TW2vxA8ZhCqfXeHo--1MH3a2pIr7xMF-3Q9b2aIF0To4cfdzxxI00ENk1gX_WfA3cO9P17LW1bAz8N1XnfcdohPVOuBGIua1vfV74mNNzcC3M7J7DEDk3tsp3E0annCssXW9OpMRPgwWXsMFADHMzC3BQ6FAZmIvGw6MLLE_aDb-N5F6_8Xbuf5Yuo_nNjTlVQbsA5lUN8yOsAjn4LEYsG8xd1qG1A67yp37lVf6bAqA7L4mIjWpN4vAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
منچسترسیتی اعلام کرد الیوت اندرسون را به مبلغ 130 میلیون یورو با قراردادی 5 ساله با امکان تمدید یک سال دیگر به خدمت گرفته است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97637" target="_blank">📅 16:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97634">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sn9JzLg7BNB8D9cQPy6pynaKWttHUjtQldMbg5XG9SuQgo883f0KaDMGjc6KBvzr75I-kaTQrIAsOuYc482EU0-qNCAGZawMGToNdcQrhgCzdNALJ2IN3iRLDYDXVrGUrTwOMshzqjhAYum3d6Y6UWTKGYNscSzrgrhwytb3HfBKujSxofSbncFUTmmpFlM40cwi89dMHpsJTdu4sA5xUfx3qe6tdsWK04IKNVUvmv4rv82hmfphlIp8OWMfxAaZ4ymAFtX4JUVY4Z1BjWZ7r6CiVgOq2IePurygQKT4rjyIxA56xUM0tA-6EBRZit1P8YnAXIt85Etp_REqzYYuIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dCD__zBBbgpfc9AHRz2x4_abtsFUSll9a0rYjVNzFJ3nZLB-DLsMm9yR3He-DNPsXLDWxSDO3qLs1a83sldl3sQLSHSwHxOVC9IygWnEGie6nCxSvCIttX43THqgB63m73CqKuryrHfwNy8mjo_vTU2PKvHY9xTKlYRRubdvdigT5Ehtqzsns0rwg90MbD1FuOAngFYynx3HpMvN65eENsWJtjeqy9QVcKOZhVWZZ_oncxs3BEXidtVk1zs_JYnaYAGjC3ULaisNaeC_vmr5QuIU4d3YFsKN6VzicPgQFq-nY1D6EC6xVVJpjzRt6pbKuNx5bCnYxa6oRwKrauP-Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ociOgRYFHUYCTYNc8Ej_2FY5BQJGnAm3sdu9-tjLiTjtzPdk5HiCZs0LrnpSdcMInsPy4E8fv0_ke_gPA3CTKlmYpovw6sDZl_qhCIUxrKJs73MPStxjbazjrCKszU-qTY78_7HZ2kMbQ6ZoIap2ishtpBU1cgzeIuapTMfaNSDy6shR0leMQfwl7xBb9GmK2xmh1qyXMCw-DT8LoN3zraS8XEQ9BYku-pNm14f4yL2D1w3vuKZclNzAg7WOAvfKZLJSn-v34UEx1lLhJoTt2S11JXmMMSlSgq6XfyWHMIpiGne79i7Ux1dP0eZUicjMsZDoAY4ccYPehyAygUB6CA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🏆
فیل‌وفنجون سکوهای جام‌جهانی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/97634" target="_blank">📅 16:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97633">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuPEp7WngtHZPf0Cya1bnpxSrbRa1bj-nHjT13DlSlFNLA4tBQ2d8HFoVtBrDnQkdbkYH5tNhJgXnVPYHhvtF8ht1RXGVsdcJidwe_TeJS_1YsBfknvawn4eDfNTmK_-5Lcn9Br8ex8QGd7_mxwtpfOlL292AUos5N1zvjyKWradMwrtPKZEbf05bBdIXVn7XJnmKufUMaH7UtnD8jiyKdgNXWkNVs5rx4fc86S304Ca4C1hVUkqTxMcNHXlc-maKkCT68Ehih66wBWmfxCmwPJBtspdTP49cx8TBh8mx_mZ982-xUrYxAr6PyUYM6zhTOAGgUTJtWdRoEyKR86RCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
عملکرد مکزیک تو بازی های اخیرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/97633" target="_blank">📅 16:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97632">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RbjjBpspj5yrPWuo2HIjhtglB_gCYulAh91PI5UCZQ4fSFXyqIlYJE4ktiY9yU4vebsZgZwZUxjf-qAaSQkXFwxyv1zGGNZhPaVZqRPTS_HJ8hXFxYo5RMZyE2PRFskWJRWmN6QdadTx6hhH5FO8uWUsC5riuLXvpceACznHAemUbWYfImVxlZqIMboddcANX7bsoOTb8GL6U6TgSJ7g5AvyLdjT9vyXb-ntExbeRJ_G8QL02WTsqQsQkU_0IBMDsBId2F41ILdK_eTrHwtbEUqzdDwyd3Pt-QfMwFuDIty94a_eLLU8TF5DZTS_cgIXSci2MIZ7VzHsLDz8pIlaJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تام‌الاختیار مدیرعامل هلدینگ چادرملو در باشگاه با انتشار تصویر خبر «آسیایی شدن چادرملو» در سایت‌های رسمی فدراسیون فوتبال و سازمان لیگ ایران نوشت:
طبق اعلام این دو سایت، چادرملوی اردکان آسیایی شده. آیا کسی منبع معتبرتری سراغ دارد؟
با استناد به همین منابع، تیمی که در زمین حریفانش را شکست داده، به آسیا خواهد رفت.
ما به زودی تیم‌مان را مهیای این مسابقات خواهیم کرد.
مطمئن باشید از حقوق مردم اردکان و استان یزد، به هیچ وجه نخواهیم گذشت و به هر تصمیمی غیر از این هم واکنش محکم و قانونی نشان می‌دهیم.
مسئول جمع کردن این افتضاح هم فدراسیون فوتبال و شخص آقای تاج است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97632" target="_blank">📅 16:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97631">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1f0184f6.mp4?token=KH11pu8NrrvVAlExUWsurYJUfp-Jr_D0i_b7LBSEXRQjII9zFaty3V1VamYzC-1o_cMq5-lQ8Q3WkkBV53HtIHbxiGDlcDnCRpuXofKO2e-45wf7-vD3UEv1eYx5KfWpGvpk_xmTvtHHHJmGoiB83wcDk-5eQlFSI4QWb2VrWdoSzW8GhA55avpQastybXrLEnDqqn1Ie_a2HaUAv_Q2KR-h5RwiDLSBpRWZUwFLly5ZCpNKa5ePXwp5vjWhw-5rz51bu7ONhrFQ4UiuRGND5ZMsYG4BCHj5yLC5QwPSTNyCkUui2VgOv8lyo2IbHLVzbz2qLAs66HM3W6IYNVUJPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1f0184f6.mp4?token=KH11pu8NrrvVAlExUWsurYJUfp-Jr_D0i_b7LBSEXRQjII9zFaty3V1VamYzC-1o_cMq5-lQ8Q3WkkBV53HtIHbxiGDlcDnCRpuXofKO2e-45wf7-vD3UEv1eYx5KfWpGvpk_xmTvtHHHJmGoiB83wcDk-5eQlFSI4QWb2VrWdoSzW8GhA55avpQastybXrLEnDqqn1Ie_a2HaUAv_Q2KR-h5RwiDLSBpRWZUwFLly5ZCpNKa5ePXwp5vjWhw-5rz51bu7ONhrFQ4UiuRGND5ZMsYG4BCHj5yLC5QwPSTNyCkUui2VgOv8lyo2IbHLVzbz2qLAs66HM3W6IYNVUJPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇵🇹
تصوری که پرتغال از بازی کرواسی داره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97631" target="_blank">📅 16:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97630">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f836625f.mp4?token=mF37VE734kQTE5gfbVg3Gy3WpQ0Y-AW1NfZOIKc5VNMoJ9FBD9A8htnorp2yjiCZ2WGCMbnCjKf_I4gzfcbRox515bdo7XAJ_ZofVZwVe5w9dl2_qHJ23noV81vPJDOHn8n_qgyYBSZY4zCNAW6bJuPFjtwxWtw8dnNCsZLoi5XnuIBrdxfCceOWA63if2dQeMGAtvAHAfRh8UrkZApVpu0-_BGmm0z1qmSits3H4eEjwk6Obj-v_v6QWO4sgQrgSywErrgH1QLviqOmPBcrY1MGIpXDRim_iT_NpTgA50yNtTZ7EyDvlFglDf1V4CRBXP-RMBAfVwiTzS62WFkSYYcRkqgU8tHxXruhFtKdx5VB8TZgjGlIvAGk5Y_h-3cqlxFGik4aa7KpPsHTUnTa5vr9StRfXZZsX7suRm_GGSesm-8gcFmk951lbBk6j-fMiAfwET_mYOVYPcO99ir5JuSQpOaOdky1x2iDeFF3AKbaacHwwFQRUm9pig7h2aL0SQEMCBVLqiY9ceSdIFg43PUyp2tMJRTe3-29ii8Ui_Ej7k2uIPCM52DX8qt5HA_8mWWlRXcZ7iYiVt-gnmqtOe7JHeU71jRpawx8GVaATTNJHBlGvRhsOBku4RIaJWQAnmu6iJ7pLvK-9ubfjwTT83XJcbTb2dEUDO5SPfgWeyo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f836625f.mp4?token=mF37VE734kQTE5gfbVg3Gy3WpQ0Y-AW1NfZOIKc5VNMoJ9FBD9A8htnorp2yjiCZ2WGCMbnCjKf_I4gzfcbRox515bdo7XAJ_ZofVZwVe5w9dl2_qHJ23noV81vPJDOHn8n_qgyYBSZY4zCNAW6bJuPFjtwxWtw8dnNCsZLoi5XnuIBrdxfCceOWA63if2dQeMGAtvAHAfRh8UrkZApVpu0-_BGmm0z1qmSits3H4eEjwk6Obj-v_v6QWO4sgQrgSywErrgH1QLviqOmPBcrY1MGIpXDRim_iT_NpTgA50yNtTZ7EyDvlFglDf1V4CRBXP-RMBAfVwiTzS62WFkSYYcRkqgU8tHxXruhFtKdx5VB8TZgjGlIvAGk5Y_h-3cqlxFGik4aa7KpPsHTUnTa5vr9StRfXZZsX7suRm_GGSesm-8gcFmk951lbBk6j-fMiAfwET_mYOVYPcO99ir5JuSQpOaOdky1x2iDeFF3AKbaacHwwFQRUm9pig7h2aL0SQEMCBVLqiY9ceSdIFg43PUyp2tMJRTe3-29ii8Ui_Ej7k2uIPCM52DX8qt5HA_8mWWlRXcZ7iYiVt-gnmqtOe7JHeU71jRpawx8GVaATTNJHBlGvRhsOBku4RIaJWQAnmu6iJ7pLvK-9ubfjwTT83XJcbTb2dEUDO5SPfgWeyo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های بامزه نعیمه‌نظام‌دوست درباره خیانت پیکه به شکیرا
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97630" target="_blank">📅 15:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97629">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsDCMOyoxPQOv90uXppXtcoySJApt-LjpAyEVNMv30CSfUvtEqyY_8x6SlguVV6C83TVjURnm_laHG-uofAt0pMPCzd0fPfvaXPdm2T9dnzk0t9B_NXrLyENUPCFOY_ASVwnojNjAfeg8HFwqWkz792MiLxXq8hDdkMFO5SoRjJsT0W4j9kbTWtT84ATp4yFiYgzGpiTohwNDEGoGEt6X5_R-8lZddaF80t_5DIerPrfKor71GVhs25kppU7ofxIRpXL0UL8Np1I2xxoLI-3i9qymc_m6h5c1ioYVUQJr7-Ydmjmir3r70Tm0UPLmvf8egMNJ0naq87-O8f75oYKoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
تیم ملی آرژانتین برای کل مدت حضورش در جام جهانی، ۵۰۰ کیلوگرم گوشت با خودش به محل مسابقات برده
🥩
گوشت‌های انتخاب‌شده شامل این موارد بودن:
💥
فلنک استیک؛ فیله گوساله؛ اسکرت استیک؛ فلنک استیک شکم‌پر؛ پیکانیا؛ ران گوساله؛ دنده گوساله؛ ریب‌آی استیک؛ استریپ استیک؛  تری‌تیپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/97629" target="_blank">📅 15:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97628">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29cb7614f.mp4?token=cX_OjZNU6P-V9e06CFMSKpVinMEg2Wu7JxuXGi88ZZI-SdN432bodnToNaNfo_AdD9IHB9xxFHe7a2nSQlF4Deg6xkCK5lJKLhDP859WU9uVAdOUVjs05Hy0rVccvSoXyhTUooWIpS3FtIEPbyhI50AJzBRfDjbnpuoOW_r9apNygBcsu5mN8o0Oe8Bv55_V7-hGwTJNXR97WWJaGJSxlf8s9sT6MuGISOJJafjgQNZpkbR0POMEszIfu4v1xOnhUALj1HsM-_h-f3k6vTEa6VwYRfZcCVC4HMtj1qFDBYOTcBCPv7KFLSs7IsZYFysgs_90dcA4VZT8BNS0hB2VJSRMSb9NPvNeV9D6XfhZyaXAcfJHemJPBrN9DiNUnwEs3rLbuXmLhl4zfCgxaOeeSf1bnVaFMDahRsmHYlQ-Umi7tQu7lQYWVRsBMSVlRA9PHWFNA_LcRsl20H7AueGENZNdShMwjz3nfUT2bgLdbqLH4oAgg1h5oqI1-XIoAEEZoxzVP7GzteZMkUvtvZW7JG_tTsn-t8XOY9ivLtVVKfUmV490KRqggmOVb5kvPNgnw9TkWS6frVj2li6fx8wiag4JbM71ujxR4O2Z2mVGRpB5DOcwuuSUQiG_d7aHotkP3lyQwqblGAhGRjQg-PZnuKKbv3wpQpm1quZ6qyJO0vM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29cb7614f.mp4?token=cX_OjZNU6P-V9e06CFMSKpVinMEg2Wu7JxuXGi88ZZI-SdN432bodnToNaNfo_AdD9IHB9xxFHe7a2nSQlF4Deg6xkCK5lJKLhDP859WU9uVAdOUVjs05Hy0rVccvSoXyhTUooWIpS3FtIEPbyhI50AJzBRfDjbnpuoOW_r9apNygBcsu5mN8o0Oe8Bv55_V7-hGwTJNXR97WWJaGJSxlf8s9sT6MuGISOJJafjgQNZpkbR0POMEszIfu4v1xOnhUALj1HsM-_h-f3k6vTEa6VwYRfZcCVC4HMtj1qFDBYOTcBCPv7KFLSs7IsZYFysgs_90dcA4VZT8BNS0hB2VJSRMSb9NPvNeV9D6XfhZyaXAcfJHemJPBrN9DiNUnwEs3rLbuXmLhl4zfCgxaOeeSf1bnVaFMDahRsmHYlQ-Umi7tQu7lQYWVRsBMSVlRA9PHWFNA_LcRsl20H7AueGENZNdShMwjz3nfUT2bgLdbqLH4oAgg1h5oqI1-XIoAEEZoxzVP7GzteZMkUvtvZW7JG_tTsn-t8XOY9ivLtVVKfUmV490KRqggmOVb5kvPNgnw9TkWS6frVj2li6fx8wiag4JbM71ujxR4O2Z2mVGRpB5DOcwuuSUQiG_d7aHotkP3lyQwqblGAhGRjQg-PZnuKKbv3wpQpm1quZ6qyJO0vM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
جیمی‌جامپ‌های بازی دیشب از این‌زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97628" target="_blank">📅 15:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97627">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6859ad42ee.mp4?token=NI9tJynsSvfkNF3I8DcbbRNPYj3LAAogrJcWI8mZp37M1ZRHrR2E9COSv-9Xd9KNYVi91kbOn474vYpxdDJHx7lhR-OcYtHj-lfVSICRemmCDPjC0YCZJ-JM5Q6bZxQZ1LSV8Vd3KUHbgIm9FoPNTk69iMGC898_CWn2G4od6P-yM41Fv8tTreeogAItOLsmBl3UQYFVsanwoBerI9jKbFWyjArSJixZ2AtXF5bATRuWkGyIt6-brq4JchgYrGQeHtWL7jmfAU7IXInlA2kkT0Tl9kUh3xQ5d4akg2EyjflLd-YhHZq8BxiQWqIskHaFp9eXgUeO2xX_Kzm4K5Dgew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6859ad42ee.mp4?token=NI9tJynsSvfkNF3I8DcbbRNPYj3LAAogrJcWI8mZp37M1ZRHrR2E9COSv-9Xd9KNYVi91kbOn474vYpxdDJHx7lhR-OcYtHj-lfVSICRemmCDPjC0YCZJ-JM5Q6bZxQZ1LSV8Vd3KUHbgIm9FoPNTk69iMGC898_CWn2G4od6P-yM41Fv8tTreeogAItOLsmBl3UQYFVsanwoBerI9jKbFWyjArSJixZ2AtXF5bATRuWkGyIt6-brq4JchgYrGQeHtWL7jmfAU7IXInlA2kkT0Tl9kUh3xQ5d4akg2EyjflLd-YhHZq8BxiQWqIskHaFp9eXgUeO2xX_Kzm4K5Dgew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ژکو داشت مصاحبه میکرد که اونور زیادی سر و صدا میکردن یهو برگشت گفت هیس همه ساکت شدن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97627" target="_blank">📅 14:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97626">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAlTaJ_QN280UjpuRAXsezSmtHE8E1jTLa88PAu2zk1Cd4zJns_HeNjOy5dhpUHyCjDf8hH7RX_hrtg--SKM85zfevf3N_SBh-QVF1g__Liz7uW26l4RQoARI9dMMad9XhuYp_tJkJGmvnPOGqbBNLTBj6UM5UiB2mcpn-FgpR0cIqJe57T1xGVPvd4n0YMHSJgnxkQ_IxqUqkBahzk2hZZ07_Z2mBG50mDSrgJvxZdR1Rjewq3-u8qwSDqodF6tZJXLXy4RDuRBT1zvOe7TCHO6xP-qTDz8FnAOQd9bJ1Z3gVaYvFg2V5JRRCGRfJ3mF_V8NAr_X4TOhNpKiZ69_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97626" target="_blank">📅 14:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97625">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41d7e1df1.mp4?token=ebe_YJUEnHkatq6DQ7XQojUVhA9X-RuGlzWftiYwdyzINQygqb2Df12G2KvXELuQe8hyJ35_dQmkTFDUF27VMc0MpMMtG7Ac1ViWuWrpSLf9QKfXVCWlhdGYYYfGCZiE9oFBC92O6J8-tQUUBKn4GS_3qfTj1jbFPNluzF3unr9pQTKcupNPToXdl8DS01AMxHeapgNnYWFDcP1CfwLGfpd9d4L4AxURIVegvFgZoBq_ns5l3-lMsqNT8Aeh1BLEMATkwZ4Rbu3BIS7Qws4N1URjbKHRv0YDbhwTDfG6vriFN9R1OR7wMTeWYs6_EE9-tR6rPMDv0PmWpLa_0fo5cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41d7e1df1.mp4?token=ebe_YJUEnHkatq6DQ7XQojUVhA9X-RuGlzWftiYwdyzINQygqb2Df12G2KvXELuQe8hyJ35_dQmkTFDUF27VMc0MpMMtG7Ac1ViWuWrpSLf9QKfXVCWlhdGYYYfGCZiE9oFBC92O6J8-tQUUBKn4GS_3qfTj1jbFPNluzF3unr9pQTKcupNPToXdl8DS01AMxHeapgNnYWFDcP1CfwLGfpd9d4L4AxURIVegvFgZoBq_ns5l3-lMsqNT8Aeh1BLEMATkwZ4Rbu3BIS7Qws4N1URjbKHRv0YDbhwTDfG6vriFN9R1OR7wMTeWYs6_EE9-tR6rPMDv0PmWpLa_0fo5cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم ایران که نصف شب فوتبال میبینن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/97625" target="_blank">📅 14:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97624">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koQOvvvSqC6dSymvRgWPHvf4gOblUWOCVRzSvjsMZhacs80hWpV4s7emeZ48q4CUjp68XH_HNVaN6kAfRo2sXTfbLvtXA-uLfckpatbQr9pzxO8GzU0RPAp__2-aW0dZ1mhuG-KULblsAH-NMhELeeBo-9y3b30ATiietZXO2rkoF1PbknWaqntGdPYKt-bHSRdPfrWNLcVHBnzVic56SA1jmj6cN5kWwzx5vSpvWjlcAY195e2uzFilDeeCphSUphGBf5JLGGMj2DlwDN8gyHfkp9QpnMq4GVb5fTUA8QYZX269McnVegxkwKH_O3mIGZihaBaBd-P9gd-j2BreyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
علاقه رئال مادرید با انزو فرناندز:
👀
🎙
خاویر پاستوری (وکیل انزو فرناندز):
چه کسی رئال مادرید را دوست ندارد.. من حتی آنجا بازی نکردم اما الان در مادرید زندگی می‌کنم. انزو همچنین دوستش (جولیان آلوارز) را آنجا دارد و بیشتر اوقات فراغتشان را با هم می‌گذرانند. و جولیان هم برای انجام برخی امور کاری به دیدنم می‌آید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97624" target="_blank">📅 14:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97623">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6470fe1aae.mp4?token=TzLMrOi22wASZb_a0yBa8IY_zZjqLATcYy6056VTuLtYbOq71iHgW6p9Rd9Yq0aOz6FV65x5pq0Z2Z88Eu2sRQtAN5NG355dWWL7lEabC4q9HMtn003vcFcKguLriDqaEOlXfV6vg2vNscRmo1llYPYd8s3Tm5l21Tb72wyBap_B4UduWW32VUNMAPdt2FjAghYP1cTBc3V1vVdNw0PNBeKeKhCg_6nuC5DgpFgjaU62DHUmmiFXzO1DjOLnaVgYagdoSGUqLi58aPNMC3sXdat6I1SdITpaw9Qt87leFAYsYwLvcdD7bqjWsTx_qFqmiLbdsn2LJNzVamWkX8xjdlci-0IN7rdpv_yWUD5af8NuHC0eeTCgOxJ4YEi1nOWHChfr9OeVUZ6LePfAgIxRM_iZYkAqpVwdIG27V9q9CV-LLeMFTDAkjQOTGmXmrQxr7jxinH1wascxn9ANHMKzcZNSuooLRPOlCLUqZXpGklc4MQoW0afxzuyUC2uIFe325uhertJPCRzck4MDdAn2tcohPRW0U4nW-DIiJwNZoqfGslh57YfP6SIah7JqPUDtem3hmKosrhUK0vzg4UkF0lTry6brQ3UGGACYmq6Sau4uQg8kiQwKZk5G7AlEV9ca1RSj65qfZFOPrvuWDZS95mKQgEBLhYLG5WkM1dOFwP8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6470fe1aae.mp4?token=TzLMrOi22wASZb_a0yBa8IY_zZjqLATcYy6056VTuLtYbOq71iHgW6p9Rd9Yq0aOz6FV65x5pq0Z2Z88Eu2sRQtAN5NG355dWWL7lEabC4q9HMtn003vcFcKguLriDqaEOlXfV6vg2vNscRmo1llYPYd8s3Tm5l21Tb72wyBap_B4UduWW32VUNMAPdt2FjAghYP1cTBc3V1vVdNw0PNBeKeKhCg_6nuC5DgpFgjaU62DHUmmiFXzO1DjOLnaVgYagdoSGUqLi58aPNMC3sXdat6I1SdITpaw9Qt87leFAYsYwLvcdD7bqjWsTx_qFqmiLbdsn2LJNzVamWkX8xjdlci-0IN7rdpv_yWUD5af8NuHC0eeTCgOxJ4YEi1nOWHChfr9OeVUZ6LePfAgIxRM_iZYkAqpVwdIG27V9q9CV-LLeMFTDAkjQOTGmXmrQxr7jxinH1wascxn9ANHMKzcZNSuooLRPOlCLUqZXpGklc4MQoW0afxzuyUC2uIFe325uhertJPCRzck4MDdAn2tcohPRW0U4nW-DIiJwNZoqfGslh57YfP6SIah7JqPUDtem3hmKosrhUK0vzg4UkF0lTry6brQ3UGGACYmq6Sau4uQg8kiQwKZk5G7AlEV9ca1RSj65qfZFOPrvuWDZS95mKQgEBLhYLG5WkM1dOFwP8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمجیدهای زلاتان و مورینیو از ایران فیک بود؟
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97623" target="_blank">📅 14:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97622">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/un7ldE6mFKyG6hwiiYLLWs4twH3mnBh5zx1p3xWbl7HwHIbxaNOSDNc8r914DuRNNOFa8-PsFBTb018M043lQtYOfOC4eC546r5Nmak-stxz9Dx8TyA4dzgk5b-ThUx4AtGyr-srfeMpBss4b4kXf4TCf4KFJTD3INFi8fEAho7kt8SjyCP0ng8YN28q9_ees1rIZhfQEgwF67P158zl0I-fJvbWztWvej7yD0wAkPuOlrEG_vvWt2Ej-e020F1zo0bDmZ5l1dKj12ok0UuLUe29a7fQtoKL7S2DBabJyKRTR2vs_tDygF7THME2LFtCyApc8i1lkbQLdYj-3kkznQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇳🇱
#فوووووری
؛ ترشتگن با عقد قراردادی به تیم فوتبال آژاکس‌پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97622" target="_blank">📅 14:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97621">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fl0sQXYgrPaV71T2132nZeEhIiQv_l6lzpx2k3s3JZqzg3dQ81dnQ_pbyCn_h5OM9a5X4-Peoh29HVwozEgKkua0mR-8NBlIiL7NBZiRl9cpLujX97vCaJZ3VXDleqRA560RoyHP7Ysk-d0n8BIgDI-QEGrRxa7ta2901Hon1xoI4bK7Dn5SdNX9ID0ygRX5PXbsKbT78u6pPcQtA6tKRBQdub591pV-4x_RqWEwykQLRz4pBhM97TL3KtdFOSFK5tjbEsADUisidkZ4jANRATgpcT1rmxoS00pLTLsfq2wCWtXYEYHQ3orNG-Zvfhd16MwH_ps698hEaUZQ22zFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
#فوووووری #اختصاصی_فوتبال‌180
🔴
با تصمیم نهادهای امنیتی و توصیه به ارکان فدراسیون فوتبال، امیر قلعه‌نویی با توجه به فعالیت‌های اخیر در دو سه ماه گذشته، روی نیمکت تیم‌ملی برای جام ملت‌های آسیا خواهد بود و خبری از تغییر سرمربی نیست. این موضوع پس از حذف ایران…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97621" target="_blank">📅 14:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97620">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/97620" target="_blank">📅 14:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97619">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2f0deb63b.mp4?token=ThGgp30V5E64CIPfsizivfocgjRZiz1lUBeZ1HZuovVmSm3WpTrKsqRHls1P8kwIyBVqgGboVSUECuZCs6bfYpIXrH5rbiQJNoQsXEv2ABAyMEVMpnLjcXLaMEGuTXEiuc-41pVWACd3BOuboP9-KBYAVZqpjt-wA_4bqGG-2JqQQ3E6AIALM1U32ZhEw-_fosKrOKGJ_Ukmlf7g-zNw49ucUNVAXgo0pywYBV-m79svVkbc5SM3hT0prxm6txAXfqZ048ei_kZ55BtpXQAqUDmSpAMkLuyOAB1vkuLRDhwYH3ytiUKnELkeNLgJh36Dux4zNy-TbI-jzkcDBCqYvrX6GmM7jeU5wx1-eGCz4rVIZ3S3ChLLUvIYVeAKreldOv9QrrKUt46qXnE7SDohr_nH3zkjHWgBgq2I8k4AuvVEU2x0JrhxJjdPvuFblRj7vMGzI5hSchXFRXPTPrjAuYRErifMBWQCe_KdwQz3U2kOcfAjFTxjbk6Y7Tr_Gz1_PWYGGkvcHRJIEvnrbs2IfTnlnsz5fyASH65axAKetpkiKtSrya5B64ZqpP1b5FkdC_4rCCBA91GBP7DcV31sfhYUwtA7SWWzpEzt5AmeqOyYWrjO_cD00WrI6_FiOc6upgPtF2hQ7etZaH8JPYdPojFR0MfHJt3iLdTbqq8ADxE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2f0deb63b.mp4?token=ThGgp30V5E64CIPfsizivfocgjRZiz1lUBeZ1HZuovVmSm3WpTrKsqRHls1P8kwIyBVqgGboVSUECuZCs6bfYpIXrH5rbiQJNoQsXEv2ABAyMEVMpnLjcXLaMEGuTXEiuc-41pVWACd3BOuboP9-KBYAVZqpjt-wA_4bqGG-2JqQQ3E6AIALM1U32ZhEw-_fosKrOKGJ_Ukmlf7g-zNw49ucUNVAXgo0pywYBV-m79svVkbc5SM3hT0prxm6txAXfqZ048ei_kZ55BtpXQAqUDmSpAMkLuyOAB1vkuLRDhwYH3ytiUKnELkeNLgJh36Dux4zNy-TbI-jzkcDBCqYvrX6GmM7jeU5wx1-eGCz4rVIZ3S3ChLLUvIYVeAKreldOv9QrrKUt46qXnE7SDohr_nH3zkjHWgBgq2I8k4AuvVEU2x0JrhxJjdPvuFblRj7vMGzI5hSchXFRXPTPrjAuYRErifMBWQCe_KdwQz3U2kOcfAjFTxjbk6Y7Tr_Gz1_PWYGGkvcHRJIEvnrbs2IfTnlnsz5fyASH65axAKetpkiKtSrya5B64ZqpP1b5FkdC_4rCCBA91GBP7DcV31sfhYUwtA7SWWzpEzt5AmeqOyYWrjO_cD00WrI6_FiOc6upgPtF2hQ7etZaH8JPYdPojFR0MfHJt3iLdTbqq8ADxE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای مکزیک از فوتبال یهو سوئیچ میشن رو بوکس؛ لامصب چجوری همو میزنن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97619" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97618">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJ6pK0I_kW21hWcCjMnywzd7vEw7RL9E3WW_PT7SLHk0Dsv2cg-s3O7frpkLls5xfbAEd0tWy1Y4AqpwYpPJEd7lxdffhGkLrEnZEncME3Ya2_cvH-7sCBLeeKR8-rtaNTi9Lrx5qO5otXsZgWQNySemJdMmAI9YqP3xkftxHNQp18Sy-atT9UuhoWEMaWB2yVJnWqq6kOfFFsR37Lco87drBRP2xOAXxEx8pqW-Y4lQ16DX5dO2haEDKLI_OLWIwPfxyTdu80KLVICIGTY1d-FKUHSasIBP9Rv9LYpEThl1fkYctW1f_eYLCh_g3XMPt7a4yeN58Iz0O-5eRPWHIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سانتی کازورلا از فوتبال خداحافظی کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97618" target="_blank">📅 13:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97617">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afhn1ffJ9ZPn1w2JVvP3TcoSy2ieN8s7Gs0Y_PZSnQI742BciQsb6yZguEwHX3HMwFaCUB2GYWPNaKfrdE4yKmBtQHgMWcJLG-AzPA2cr4rIhmru69LEH3uAO3OdhaTtF9K4wpARDjFENl4pJB2_rO0PqrqF5BAt8FQEmGVsccgCuQUubFeMf2Y2SQsW4AfiKjLlYbfV4gFe7dVuZ1idX-QywDvwsc5ab25on0FPS3HkVGNKqDHQV98xJK5C1HaQXCQjjnMFTCA_36wd35Thsb8s8TSD9BYlQxXpF5VzvsMfRIXDVU-GfgfqU2UI8Wrl2hguoy3um9lShyry2bxiLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
🔥
مکزیکی‌های جذاب در حاشیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97617" target="_blank">📅 13:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97616">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e7dc94b5.mp4?token=jCuOzxmc43Szg-dXCwuUdVltI5EzOpUeAPp1J0Nh4q9tyTp5qBZuJn1krnV98sMhqdSqd2JzWd4d7HjGGsxpyri3gPoLMTm_J84UR-wK97CaIH30OG8E3MCAfRL9oHrU9AJoZSdnlXx5BPtNkq1gL8h7HneM-BEowAtHg_xJQrZDxLzrygKp6HgEqsyi4vFAkHWHsnD-KwgeVWEWKWyXLTpgbzGmYuzsWesKj6ESXuW6vbrF-ihvwqIW0VyKNOZ9XSYMYYF8XCPhTcM5_UsYwCwUHd7LrTWBYiqkQGKfNT36il-zh8L9Yn0McYWzYpDSmDzUgBqabqtB1NASPMMKCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e7dc94b5.mp4?token=jCuOzxmc43Szg-dXCwuUdVltI5EzOpUeAPp1J0Nh4q9tyTp5qBZuJn1krnV98sMhqdSqd2JzWd4d7HjGGsxpyri3gPoLMTm_J84UR-wK97CaIH30OG8E3MCAfRL9oHrU9AJoZSdnlXx5BPtNkq1gL8h7HneM-BEowAtHg_xJQrZDxLzrygKp6HgEqsyi4vFAkHWHsnD-KwgeVWEWKWyXLTpgbzGmYuzsWesKj6ESXuW6vbrF-ihvwqIW0VyKNOZ9XSYMYYF8XCPhTcM5_UsYwCwUHd7LrTWBYiqkQGKfNT36il-zh8L9Yn0McYWzYpDSmDzUgBqabqtB1NASPMMKCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
ما تو ایران چه کار خوبی کردیم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/97616" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97615">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjdUZEE24Nod2R8H3pI1GDE38MadHzn31SL5uhXarwmq02ZgKPR9Reb5_NdFu5Wg1WFs_Le8v3r0BHY2lYjOLyz9eTyRDIsYEKq4Jf-_bcG1hm5ADMGU1dKQqSGP6JmuHXd8LGYxCZAoknx13OYdAM410JJFJdCx1DZQc3nDfuvbgW1XT3Hlq0hvHoSlpky3dHdWZ4UzA0XU_SSahM8lrpM_2_W0NpdNTMXKl2EHyrBdkF_yQsJA3wUT5F8e-q8xgA4adjijqT3waNFCPgUQZsqD5J1OenWBD4TPeKsOKXX_WtkSrzBoPrPy97VCTgL3DhsXMhz4OmuSEtoX4RTusg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
از حواشی بازی مکزیک و اکوادور
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/97615" target="_blank">📅 13:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97614">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6oLOy9QlxQPwhyUOOIikkdfVlKSexav1BgRp8442eykpqq_mRxhkYiW3XkG-hF-T6sIUZ8hx7aNPyRu7PZmxa0UTUn31rAWeSTCdVm0wICDY3zv0uUEgpLOCn4_dM5SgZHZcJ9nrJ2Pr8cLJBTZoNujST6Kd7oDVL61wbOT1txCv7Oerm4OsZfZFJpepAjwlI6xirRxbWE-wOO76XOStFYtRdFkD3fzTD8T1pN27-3XABawnYULtD_TBe8Nwb9zT8TrAjbXBXBVV8eVB0xuYV0jQ6y694fKeaRHyql20gtrNi-pCvs0B85MNbvdCeHn25k6mVs6XQ7cb43-uuXK4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
فرناندز تو تاتنهام شماره 18 رو میپوشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97614" target="_blank">📅 12:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97613">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204ff9d4a4.mp4?token=Ap31tCk2btudSWKfC7Z9JsW0lZpE49nRDX8ApGPnDd4JihdR4JH-iG43Jt6UfN3NFhKKYDrhZWzgavqQ3Sbw7IhrjgLM_jX4ZAHgUFuLJP2PThs9Mhudo0TmkppaeiDbVSsL3LNOmCFCB6UTtK-EsIlKiadyCTvDd4uymodeWHv7x8Ezbw1w_WBGByLZ-3fILhCRmugA9AHSCMX9v6NHegkigGffg5yj0NIVHeRw54mVURWxd7nuVPNOsJJ8SPbJwxJeS70cCsgUyXuv1DmfKQ9JSkLrCAoSzLKzBsGPMLTVGyAw1AN1saXQBGN3I-kyKS256Q1GQjYG_nNICXy9Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204ff9d4a4.mp4?token=Ap31tCk2btudSWKfC7Z9JsW0lZpE49nRDX8ApGPnDd4JihdR4JH-iG43Jt6UfN3NFhKKYDrhZWzgavqQ3Sbw7IhrjgLM_jX4ZAHgUFuLJP2PThs9Mhudo0TmkppaeiDbVSsL3LNOmCFCB6UTtK-EsIlKiadyCTvDd4uymodeWHv7x8Ezbw1w_WBGByLZ-3fILhCRmugA9AHSCMX9v6NHegkigGffg5yj0NIVHeRw54mVURWxd7nuVPNOsJJ8SPbJwxJeS70cCsgUyXuv1DmfKQ9JSkLrCAoSzLKzBsGPMLTVGyAw1AN1saXQBGN3I-kyKS256Q1GQjYG_nNICXy9Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
خوبه کشور بنگلادش تو جام‌جهانی نیست وگرنه با این هواداراش سوژه رسانه‌ها میشدن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97613" target="_blank">📅 12:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97612">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAM_RKzIGYyaP4zTCthA06LCZ6QykEeulplMXykw_x-7lAI0Wd3HnItprs6KYuidwwfPAZ00v0PyTdPoidj7JYa3BtMsC1UwBrnUzsNGvDYIRPUq_V717akN6WlGWHBxkM6mLvwj8Z33crhALrbHfhxh3snt_K2lX_uBh_u-1uE_unukMmIya9DIMMaO2xPyg4MD39lNE-dld8Lh1PkAMwFteck_ldbPhlPXVASKS72V6wQ7stB0nRzBMXk_EM8f77TC-mV9JANoPGJlNR7Zn5HAAFEQYQXn0oI0kBl-16veDns8ZTDiu8luIpxeqN4vup7iGPBLBYxisygDLE5Y6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
🔥
🔴
میدونی هوش مصنوعی ترند دنیاست و اینده ی اقتصاده ولی بلد نیستی ازش استفاده کنی؟
🔴
تریدری ولی همش استرس اینو داری ضرر کنی؟
🔴
یا کلا ترید بلد نیستی ولی میخوای سود دلاری داشته باشی؟
هوش مصنوعی TimeTrade این مشکلاتو حل کرده
✅
هرکسی با هرمقدار علمو دانشی میتونه ازین هوش مصنوعی استفاده کنه و به صورت live و روزانه درامد دلاری داشته باشه
🔥
👇
https://t.me/+hcwmoHXpF6k5Y2Q0</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/97612" target="_blank">📅 12:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97611">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxhxRzSxeg_-ee65Xy3IhVuktsJFSCMe6psR7Y5Ou81dd4sf5CckOkamb5glRbn-zdYcY226Yl3NQG00EZt0Yn1J7Je8xXBm28tLQORfCSoENzbPQ8Cida929TR0ATskSia0P-2_Xie-pM3tkGYYD5gLzVFolOH2hd-YTpfOjesB-5ag6NWXq2qjohkQ2COyj8g1-Bq8rAxIrNbjt7XYvjkFRU8j2B-0Sva9KSCokXzrBvy7cXwibNwPZZB4uKtJRo2tFy_sJoLma62qz2lbL1dPMiipritDkTMlEQXRVS1MbXlRW1Odm2hZs8MN-RPiWvWwgfLJDNKiiMugs6Ct7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
#فووری فابریزیو رومانو: متئوس فرناندز به تاتنهام؛ !HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97611" target="_blank">📅 12:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97610">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EERB2GcefyKp6FlC3uZXb1fs50wdGy5MZOm8WvCWu5Rlpp_6Gwx0sLMoh2CcBZQpKdTo2FtFkHbgu_ayOx9Pyxf0_0BK0xgokuBGr6FcPHtD4z-uqFJDcPqNBwnU_GK9eeBbeDyyfC7CN8nQHsU20EqEtzdqssLJyby8mBrCtyh_x3aVgySXGbe3UJ9S7OVbRXAz2h9A88dO81ZPmNQaDpJwtMwCrzZiYuXSs_IodEnW57VQV5m0aKnQvxEBAxPx4CJEOAhdU3tgiLsrEoklHMlFRdMya4jJjb1uCee_f0evJtlLjHngjfNbJwL33jll3q9GJswJKeMCk7l8i1y0Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از باخت کنگو جلوی  انگلیس، سباستین دزابره، سرمربی تیم ملی کنگو متوجه شده که پدرش حین بازی با انگلیس فوت کرده و از دنیا رفته
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97610" target="_blank">📅 12:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97609">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Drl9zykZh_Pp4m_WQY2EeGvXBFjV-hemhE3QPi8uVs0DVa55o8bl7wuscrPTWZO5mpb36Ml_jvLhir9QZpOBTfOaVMFM8AUfhiX3m_ypSPonHrRggV3EQi5hm9e2Z7SQfRR2QqZIywksTv50SbeSakTpA5tKal-4GPQyI1AePi5Ofom_4J1U30xOQC1naT87BIDGoLj6B9FVtitedWBdxda0CBHHk-uLZC7y5bc3Kiimlr3KZFdaid2kL3Re8pi7Usz-8A-KWaynJXsXXXa9-82-3-KTXCme8Z8J5CG3YOyFKLOQQE_N4BB16-nJfJEFUYcU_h5Z6mY4F7ybmQoTGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🔥
کار درست مثل گاوی که بین خواهرش و زیدش رفاقت به راه انداخته تا زندگیش بگا نره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97609" target="_blank">📅 12:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97608">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbba94933c.mp4?token=B4_PDEcp5fyBuE4dTDIBiSB3aDllJxPoYRjIyYNtELNUAptrnq7clsc8gdnk60v8gKNlVGiHC0rVEJjKb-zJaHH_oHEc910LBBs8tJcjZv3SXA-rap4QOjhgGapd-USWHCjmlSEwgbcoj-3iOb-_ceQ3Nsmp63d2jY-4KbN5TfngxHClXp3dgpn4YgM_SbeXg_9LOcOrjcd4jNai4STENYW4o3d81dk3n0cgE9QixHf_fnprJOfQcaF4QDCNZBCMXNPlCaUcQnC57PTzMalBoHRUVMh0cG2GwHuZzL7MEkdGnu0fwDF2BkS3knvA3JZ6yNoxhEbLnP2MsMjQcAaQPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbba94933c.mp4?token=B4_PDEcp5fyBuE4dTDIBiSB3aDllJxPoYRjIyYNtELNUAptrnq7clsc8gdnk60v8gKNlVGiHC0rVEJjKb-zJaHH_oHEc910LBBs8tJcjZv3SXA-rap4QOjhgGapd-USWHCjmlSEwgbcoj-3iOb-_ceQ3Nsmp63d2jY-4KbN5TfngxHClXp3dgpn4YgM_SbeXg_9LOcOrjcd4jNai4STENYW4o3d81dk3n0cgE9QixHf_fnprJOfQcaF4QDCNZBCMXNPlCaUcQnC57PTzMalBoHRUVMh0cG2GwHuZzL7MEkdGnu0fwDF2BkS3knvA3JZ6yNoxhEbLnP2MsMjQcAaQPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✈️
🇺🇸
پرواز جنگنده‌های آمریکایی بر فراز استادیوم دیدار دیشب این‌کشور با بوسنی و هرزگوین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/97608" target="_blank">📅 11:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97607">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/97607" target="_blank">📅 11:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97606">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38ac3b752e.mp4?token=vgW5PF5V-ch9YaVAl8ZsV7YgGV5cGbgULlcMeOJdAPkPTUDiXIE1m-6TZuG7KEjJ-x2ciVAIKfY5eujHE4CtZ_jCuUc8jveK34jl6wkYQWrIS5MPwsDjBnbuHvn8Ypu9rTwnvQCOX6L-BESfMRAJvs2aX3QX3L0NSyCP6X0pHf9dYZp6E3NUHW4wU9NubKOPDuOBGPjpiztOuOERsKy2YXWJaJPbweTEeBYvfPo7J1fYSAok8oJmOkuMAqmJh280sbRrOB7W_zKhOMvoP_62ZUCE8Er8l5WHWB7o1GZRVI9nJ8f_3IzvRss-lzeno4GALyMZ-cME3ptVM6ZCdPwtFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38ac3b752e.mp4?token=vgW5PF5V-ch9YaVAl8ZsV7YgGV5cGbgULlcMeOJdAPkPTUDiXIE1m-6TZuG7KEjJ-x2ciVAIKfY5eujHE4CtZ_jCuUc8jveK34jl6wkYQWrIS5MPwsDjBnbuHvn8Ypu9rTwnvQCOX6L-BESfMRAJvs2aX3QX3L0NSyCP6X0pHf9dYZp6E3NUHW4wU9NubKOPDuOBGPjpiztOuOERsKy2YXWJaJPbweTEeBYvfPo7J1fYSAok8oJmOkuMAqmJh280sbRrOB7W_zKhOMvoP_62ZUCE8Er8l5WHWB7o1GZRVI9nJ8f_3IzvRss-lzeno4GALyMZ-cME3ptVM6ZCdPwtFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇵
ژاپن، غیرآسیایی‌ترین تیم آسیا...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/97606" target="_blank">📅 11:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97605">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDqJofLqEeUXS72OlGTk8PoDSmEQFXXTjnn9hrOZJ6WkIeGmmWEGj-JF706CxOk2f9Huu0nnrhPeFoXDV9la41I_uq7DeiEnp5g3iN6J4_fBcSIUQw_9cOBSLMHGHFCAYOeqhcRXT38SyTBW90X3gQ2V1e7a5AlM7470X0tCA1RRQRqTtzqU8DOBiDsQRAh-PE7KD57HZ3A2Hg5w-YWSuAcMy6r2MhephzOsa8m1HdLc6O6YCEoJfEchrR6ifDBu2g084KjSuutmvmOxnRNeIekpaOzUpB039hgJ6wxlP--_wKM2kvCTZ2zlTtzazQjvn1DmwHZ68L2fkdAhDPWlrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوری - فابریتزیو رومانو
📰
|
🇮🇹
— هیچ تماس، مذاکره یا پیشنهاد رسمی بین رئال مادرید و اینتر میلان درباره انتقال باستونی وجود ندارد.
❌
🤩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/97605" target="_blank">📅 11:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97604">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea402ec7ef.mp4?token=mGgE_vFifFYhMUif7WRV5i5_z2aJhDZW_qb8b6RZVnGKWF5mphRSBIq47IhBWAafrMud-FcGLq7_xNj8bNS8QT-sdDNq8FmGoKmJF4o2RGPAw2MfBAqImt9HI_meVoc7CV3KbXYfXsUi26VautPsdKrhoTTIrEG1Cvif6w3pzaxxRVBgU29LRW2sp2TVXEoxX-LjUEkPf1m-PDjzQcg-sugtdR9sBkGstcz4Ti4zd2eDFr9HLgWJFHBy6TWgwWJhoJAw-MiazmihTNgQYHk6EdkR3KZTNYNeF4tbkiJGB3MWvQ5uC29GsVZKEoHect5BMX-RNldZNkScO4cUvPrFEkYLkVKDKsQ4_aYDTkOoKeh37hieVdBAAoDZEjcwygqZLBszife9CUp3KRnhr6G6NKn_Ras5bdkz3nW1Cs6aOuCDqU3QHFDF47VK8DVqh6PdLP5plXb3hX7f8a2gpLA7g_ouz3MI8ik8pecborjoWNtOhBQ1S-rFOd05B4en7Bt5bMhp4UycTNYjc4nSyxZmokidukAl1n8M4M6pi15GDStwNg9iOC3rH1ygtxHafvvZHY0HGhZgVkL295dxWcgW8FgoiAPJqGD6pjJ3FzBpFx4LwAoSRdALRQyrTHbygqDxwsNg-HcXJW5czEDqIytOjV1vuG87ZIOy-Ry4luPzv74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea402ec7ef.mp4?token=mGgE_vFifFYhMUif7WRV5i5_z2aJhDZW_qb8b6RZVnGKWF5mphRSBIq47IhBWAafrMud-FcGLq7_xNj8bNS8QT-sdDNq8FmGoKmJF4o2RGPAw2MfBAqImt9HI_meVoc7CV3KbXYfXsUi26VautPsdKrhoTTIrEG1Cvif6w3pzaxxRVBgU29LRW2sp2TVXEoxX-LjUEkPf1m-PDjzQcg-sugtdR9sBkGstcz4Ti4zd2eDFr9HLgWJFHBy6TWgwWJhoJAw-MiazmihTNgQYHk6EdkR3KZTNYNeF4tbkiJGB3MWvQ5uC29GsVZKEoHect5BMX-RNldZNkScO4cUvPrFEkYLkVKDKsQ4_aYDTkOoKeh37hieVdBAAoDZEjcwygqZLBszife9CUp3KRnhr6G6NKn_Ras5bdkz3nW1Cs6aOuCDqU3QHFDF47VK8DVqh6PdLP5plXb3hX7f8a2gpLA7g_ouz3MI8ik8pecborjoWNtOhBQ1S-rFOd05B4en7Bt5bMhp4UycTNYjc4nSyxZmokidukAl1n8M4M6pi15GDStwNg9iOC3rH1ygtxHafvvZHY0HGhZgVkL295dxWcgW8FgoiAPJqGD6pjJ3FzBpFx4LwAoSRdALRQyrTHbygqDxwsNg-HcXJW5czEDqIytOjV1vuG87ZIOy-Ry4luPzv74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
آموزش رقص‌ توسط ایرانی‌ها به هواداران مصری قبل از بازی این‌تیم با استرالیا در آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/97604" target="_blank">📅 11:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97603">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgiG563rUtKuP9ZbZxnCWoBG44yQUSsowwOUsdmBjQ3kZD892II_qJWykw_b4SZbLeAvXjYeH6PORscrO2OT2ZW1av9VrH6j10YBqYuFPfQw6R3qQLuVPA5IE-Gib5RzRinWoksOZ_9go2Qymr4ybozoCv3t3TlGoT4dK04iQt21-vYoBGGT55w3LLHxkP-0s2CmE4pRz6gUZk6UXBSUU5UsQHPAgIzVSo1sqCNLIr_fy9FY0NnDrtkXqvV7vJaJjZk1Mjcf5G3dVbp_7nU2kzW9MvdzF4LZndoE1AXwWlltr_30cnUNflpY7CPuTwhds-2NKc5D-p3jYjN64h83-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
#فووووری
از آاس:
🇪🇸
سران رئال‌مادرید پس از نمایش درخشان اولیسه مقابل سوئد تصمیم گرفته‌اند که برای این بازیکن تا سقف ۲۵۰ میلیون یورو نیز هزینه کنند و رکورد تاریخ نقل‌وانتقالات فوتبال را عوض کنند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/97603" target="_blank">📅 11:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97602">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed83a057c.mp4?token=aVd_DP__H_K4Yopk_69ad60S6K2JmB4I4L8gG59Xt5N5jvmYqOLmkslf7AbQWKw1ob4w07IETQV7uxDbGJhAhUSvIjDUwHIZnKKPeGT9_4GnCQu4dPA8fYbeu7Gkbo2NZ67PS6HKio5oE-mRHntkneNB-No43qGIYlbqjdpixOmvMn7IpSztOQO6k7ryZ5oJU3vjEvH3pClO6C6_MSuMG2GkbLaOFyuTcyNm86bJUXBcGPQk-LqDmqzoMegLRbzOUaudlSWGIrDOD7HhrHuOXpX5j_zgli_59rKSG80y9JezQKwpALqCJEo7v0Fh0UJNwaAvYMqRY1mbScGBtENmew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed83a057c.mp4?token=aVd_DP__H_K4Yopk_69ad60S6K2JmB4I4L8gG59Xt5N5jvmYqOLmkslf7AbQWKw1ob4w07IETQV7uxDbGJhAhUSvIjDUwHIZnKKPeGT9_4GnCQu4dPA8fYbeu7Gkbo2NZ67PS6HKio5oE-mRHntkneNB-No43qGIYlbqjdpixOmvMn7IpSztOQO6k7ryZ5oJU3vjEvH3pClO6C6_MSuMG2GkbLaOFyuTcyNm86bJUXBcGPQk-LqDmqzoMegLRbzOUaudlSWGIrDOD7HhrHuOXpX5j_zgli_59rKSG80y9JezQKwpALqCJEo7v0Fh0UJNwaAvYMqRY1mbScGBtENmew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇧🇷
🇳🇴
اینبار تقابل دیدنی گابریل و هالند در سطح ملی و بازی حساس برزیل
🆚
نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/97602" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97601">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">لحظه ورود تیم ملی آرژانتین به میامی
تفتیش بدنی مسی و در ادامه خنده هاش
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97601" target="_blank">📅 11:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97600">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
رومانو: فلورنتینو پرز برای تکمیل معامله اولیسه دست به هرکاری خواهد زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/97600" target="_blank">📅 10:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97599">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9d1TmSCw5A0m0vRAuwNIft-3GcYsdCfuvhvKbKBZl5t87EtmNe8XbOREtbDeF91qC3xj-fKdJtBVKQ6V-zpQNL9kErr_9KTvgUsYVZc2BI2_zU2BgAMFKW5j5ihUEPE1FM4Y7VbGevIR2C2n-FeZvJA9cCre8VBI7qIzv3VOuNWhLNLBuMd-1XbAsPXcVGS-y6-Po5EWE7eLrIEZV8zHURyOXCE4ChB9l30sGcjCZLt5ZnJOoVwaa1ZFUnN66rLa572vROdwnmvTlHNW4DykV44iI6d8B8r--lveRZMpNo9dv7ZEOCmcpE6c9Kmw8xhsYlaX3dA42H1qVxVsuJ5GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⁉️
🔥
#فووووری خوزه فلیکس دیاز: رئال‌ مادرید و یک تیم دیگر با نمایندگان مایکل اولیسه درحال مذاکره هستند. کهکشانی‌ها با توافق نزدیک‌ترند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/97599" target="_blank">📅 10:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97598">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDKL5ufiwTN6Uzl5kP0hwY8UHrb5uQWUlx0esIpObsd0kyhxKPQtiEtyeEUM3MzeWz2Y5s5JMH4eOKynPBOLBgX_Da-FeK2308lKzYhmhItxwFReYXuFix9LcaBXnKonNk2JjClJwywTrHrE1G0D9T-a_GGVu4hTgFh-shQsqr_vszd1eZIjbvWNVmchN-Yuvc_Qia-y0dKLF5_c02V5zRL1KSgcZqVV8x_LXjXZx-gq3XqZjmPldKb2y9cF2ORQNDznnaqJ7LMqbwpE2evpsLabv2kzQP-SD3hGod1Jl3RZfJdSm6gBBhd7AFGo_vWAyYhtdWpYGcN-u1kmwvJzyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⁉️
🔥
#فووووری
خوزه فلیکس دیاز: رئال‌ مادرید و یک تیم دیگر با نمایندگان مایکل اولیسه درحال مذاکره هستند. کهکشانی‌ها با توافق نزدیک‌ترند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/97598" target="_blank">📅 10:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97597">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T82AG2U2yTtC39dfuj48n2C-OJuwoRZOH-17EHkFDYv8LU3slpW2mNwCehkP0MoG2iR61e9id4ya1LQUD8YbjlRUrhrMRq9oGLf5mVAG5WaE2Qn0lJOsODhGB4uaVaqEsNVBU4C9T9ZTKo8dYz1oFmwKJWimzJ2ZimKuwUKeYAVYG2etyQOiaRLB9FYW8a4M2dA2RHjeFVW7IMcVQLVrdexBH0ituCuEbhewQL3Zw7sWzzWKai3InDov3R0ChIoz3D0t1CFSs1tObJUICa_EJ5fDdp3HeqhsqCewUZ6EK_2be0b1coXz1AncE29wId3KAC21DDbCEt__PehGAvVbmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووری؛ ساندرو تونالی با رد پیشنهاد هنگفت منچسترسیتی در آستانه عقد قرارداد با تاتنهام قرار دارد و بزودی رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/97597" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97596">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aec355d42.mp4?token=SSunUuBr1c8yZFJ-U85GdNnMqMWSCvvuU82ucEc_5JpHM01kElpIhxOs6ttQ9r7Gw0XD82TpYiixYz6J0G3fngMlotVik-ufdZ1qajGJZqLgz8kxcA4Hk9Q_q9JDEyt_nWnHC4kaHQOF2g1yLWRf9_rohPg9WkzY62lrKXxV19aSvdUiYQBDbqw1-CcXBbOYbBVgFnwMeZAbP8tHkqUbL_0MtQw4Q8uLanPEM5IQD1bUcKKDOQ2Ao6xq1sa5lVV_fRYG-mJ7VSw2XjjttWEQdGsc-VbnXv4zv5xeJXoEduUhjtMqXC1-U4gThGbdgNY6A9b8M-x-Uj9cdTkbgyV7LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aec355d42.mp4?token=SSunUuBr1c8yZFJ-U85GdNnMqMWSCvvuU82ucEc_5JpHM01kElpIhxOs6ttQ9r7Gw0XD82TpYiixYz6J0G3fngMlotVik-ufdZ1qajGJZqLgz8kxcA4Hk9Q_q9JDEyt_nWnHC4kaHQOF2g1yLWRf9_rohPg9WkzY62lrKXxV19aSvdUiYQBDbqw1-CcXBbOYbBVgFnwMeZAbP8tHkqUbL_0MtQw4Q8uLanPEM5IQD1bUcKKDOQ2Ao6xq1sa5lVV_fRYG-mJ7VSw2XjjttWEQdGsc-VbnXv4zv5xeJXoEduUhjtMqXC1-U4gThGbdgNY6A9b8M-x-Uj9cdTkbgyV7LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
یه زوج روسی معروف که صخره نورد هستن، بدون داشتن تجهیزات ایمنی و در سکوت کامل دیروز به بالای برج Empire state رفتن و یه پرچم با شعار "وقتی قدرت عشق بر عشق به قدرت غلبه کند، دنیا صلح را می‌شناسد" به اهتزار در آوردن. پلیس آمریکا هم با هزارتا مشکل این زوج رو به پایین آورده و بازداشت کرده. حین انجام این کار، تو بالای برج پسر از دختر خواستگاری میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/97596" target="_blank">📅 10:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97595">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a9e27c8f.mp4?token=IuGy1R4KQGviwQz43FYWzApe_lvvoEbLSsjN4Y3PhxrS1sWH8PSwf61YqVbC1m6BpkPc7DSqw7n69O6jDHy4j-2HlWwxBqWox2cbVl_g8OEyzHsCS7pFYLWZ46nuZPJ8z2bPwecgrhHhdlCqWQ15ox9I8wW2PZqmMf6-wKZH6frX9t2wmrTPQHf7HyJlGDoIHLeV-ZZg39Los_XGs6VexkBZ-0xH1lyMXBg8EQXgFZhyOzaDwP_ccAVEREX13DIGLpiIifrhomOpuVnK_jPSo51FfdLe0zKNhZZYEbkCIlcZuvvr8XusH-_CJ5RAS8z_QveyVtSj86f1GtCkPhW0ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a9e27c8f.mp4?token=IuGy1R4KQGviwQz43FYWzApe_lvvoEbLSsjN4Y3PhxrS1sWH8PSwf61YqVbC1m6BpkPc7DSqw7n69O6jDHy4j-2HlWwxBqWox2cbVl_g8OEyzHsCS7pFYLWZ46nuZPJ8z2bPwecgrhHhdlCqWQ15ox9I8wW2PZqmMf6-wKZH6frX9t2wmrTPQHf7HyJlGDoIHLeV-ZZg39Los_XGs6VexkBZ-0xH1lyMXBg8EQXgFZhyOzaDwP_ccAVEREX13DIGLpiIifrhomOpuVnK_jPSo51FfdLe0zKNhZZYEbkCIlcZuvvr8XusH-_CJ5RAS8z_QveyVtSj86f1GtCkPhW0ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
اگه قرار بود با مربی ایرانی بریم جام‌جهانی بنظر این قاب برای عموم مردم دیدنی‌تر بود...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/97595" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97594">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRAN ANKER</strong></div>
<div class="tg-text">.
☀️
هوا گرمه ؟
🔥
ما قیمت‌هارو
💲
خنک
🧊
کردیم...
🥳
جشنواره‌ی تابستانه‌ی ایران انکر شروع شد
🤩
برای دریافت لینک جشنواره به لینک زیر مراجعه کنید
.
.
🛍️
تمامی محصولات انکر در این جشنواره انقدر تخفیف خوردن که این گرمای تابستون رو خنک کنن برای شما
❄️
.
.
📍
فرصت جشنواره محدودِ ،
دیر نکنید که این قیمت‌ها حالا حالاها تکرار نمیشه...
👇
لینک ورود به جشنواره
🌐
اینستاگرام
🌐
@iran_anker
#anker
#soundcore
#جشنواره‌ی‌تابستانی
#ایران‌انکر</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97594" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97592">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJkk1V9_xLs06P1hypH68_pnlqYyXeMY2s-HHU7Sm59VsKkX6anFF_WPO6K2o6l_gkOCiv_hPaJN9-oMUPoe-myLHGtKL56QFqANqtg7D-vG_Tilnafd1oTf2sreXGh6qJwLf8pwwcrIzKdqBhkKs7znzxMgQ96I7AneDZyJfeDmsx6cf7o91vVyrDlLkIFm_utKsPIbBeCyZKonXM-9yShoAAubwe-OsikzBczzr20_rz8Lbv0AjGowYE1mD74H9d2cxKQ_8j4iPSkgRTQyHeUjzQtRLCQOH1EIFvosGMtK93pwZO-GO4hWNf5t6iceUWF_-Rhl4gI-qwU1mlFnnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فابریزیو رومانو:
فلورنتینو پرز حسابی عاشق بازی مایکل اولیسه است و رئال مادرید هنوز هم دست از فکر کردن به جذبش برنداشته. توی باشگاه، خیلی‌ها اولیسه رو «خرید رؤیایی» می‌دونن. با این حال، فعلا بایرن مونیخ اصرار داره که نگهش داره و قراردادش رو تمدید کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/97592" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97589">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CRKBmGruQGt5A5yJ_h27ChuDrOqMrLrw3jBlamZhCZJwGcU5CCog6PbDRksHMPqaZ6LHvNBUMKPgJMXzj43CkhbaUWicWQM6BsIA16SMMCQNEsoMFXd6K-tJPI-zyD5xUCkz1q3kMSUCwIYQAj4LQR0M47hBqTJQa557Z8nIBddhQVuhSrWwPN3-hB3eBpzeL40QJTZq-89zNyhqMb5fgravM1aRSW5EpX_I5f09ZT-y4Ij4b1ngz409YEP1hQCDhKdyFttLuqb3iIHYo0ezDg4bjIrKTz_SyiD-2uD75fkLLFtlB2HkmpfGQ8xqi0hHC_ydMi0_fetiCA8GF2W0tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0hVbmYADjXeJTKaI_OhARVdBoXYlNNo46LlN4i_VXkKP_Anwtb6o_VEN842uEMFNSJutg1QHekrnwpO_nEzvcS6nhujSOE7lqHB1uwbTx5JdAhKKwCZ7od_1KrvUPydahVt7UhWrfV0QfS90l1W7eRlmIaMokNqavy8vrSIJ_yTQg9IWk81CFbD08lLEGphqQprRafWluK1943dKg_QBCZCUv7yyolwtsuFbWAYE58wokEymPCtk-KdOXT6lYQ-_4lwF18EhGFdRq0olWFydf0-XUDHibQcPWhb_1fJMQM_cEbDPpWyHh9V_5tWlY0cw4EBvVZQA8EFJDUboqtKdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgL81RsQKmhMGmcSZ60VAfGaHU0EfveM37-7lNQGPWYPIPQ7FZXqnCPrfGScloBmJnY4pXzRmuFbwCFGYqUa7Mm2TcIzV0SVvpiZpyyhK2RXcJN5uu-YCOZcirqNj2DQtUDemXz9AxDhn3D0k5yU047LU8zwE7UqakPXWtJEYyo8BavQPC1XwD7fxFdADFRzTCOY3fneSZI3OZLfSJuGsiechP0neKNS9Va8DWWrgqBiVtHOcIl-Hm2DCjnF2x2rPfxyr5ocAApJmF7pASNvdT4mlpWSEUEnM5wsdMgKscaP0e45tPkZhc2N_nHvF17Rl-UAjQi6IHK6BMgboQnu2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تفریحات تابستونی خانم آلیشا لمن ستاره تیم‌ملی بانوان فوتبال سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97589" target="_blank">📅 09:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97588">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uk1FfwdjttQGG0Np25VygIXRbxoNAsskUTcFVVak2WlKOsqiDcw93CP3kJummt_6TNHV1jE5Z9v9cCsJMK6LSzTKJKRsTRNvIlL7AUCG-ba1DwquOsd-N9DBix3ZCBk-c0vhf_X1bTlnVxhqSuo--VM_13DcBNX3KwEYdbBVJgzv8Xp4o98mhtl6vQR18B7ElB78SuTtfDe7AyGK0ZbPMvzLBGGad02OJ3xQ2bnPUr0Owr_-_cXLaIhyUDNsXQ_730ol-GOzzlmMcu6u5xWV1Nn3YKiNPS5Tmlpb1Uf-ASblFYK8lFdoOGThJ4dzJqsQ39dTEscVU2KG7C9qFdLScA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
چیزی که وینیسیوس از هالند میبینه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/97588" target="_blank">📅 09:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97587">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5cfa932c1.mp4?token=kTp_yKsY5h5zDTurx9d8iGBTQHe2IvKh5cefbFBJWpfu08tzn_yz_d1u7tTLF9w91SAjlAlzhSZu4QvYvXtf5imuJb-ooErI5eod1obDVPMumoNuROsxNTPY6gV2QumDrUiJbV3Y4JTCTwLO8kyFj1JQBmYfrOdBNi7GCmkSR5Bl55SaPIjpFgdkTmJQtf0Hh2kg5FJRq_cJceQPyw_w-JajUCiDdCGI6Xn-fQu6hkQXOLRNMaP7ahW7-f6l2_T5EdXqFJzQo5FNgFmSmRF5vg0_6ddSTSDmXN3Pg1xtx8sT5nuqwLqf1MiUSL_kjOPyd-BghuxzN_WbWuKE9ov_yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5cfa932c1.mp4?token=kTp_yKsY5h5zDTurx9d8iGBTQHe2IvKh5cefbFBJWpfu08tzn_yz_d1u7tTLF9w91SAjlAlzhSZu4QvYvXtf5imuJb-ooErI5eod1obDVPMumoNuROsxNTPY6gV2QumDrUiJbV3Y4JTCTwLO8kyFj1JQBmYfrOdBNi7GCmkSR5Bl55SaPIjpFgdkTmJQtf0Hh2kg5FJRq_cJceQPyw_w-JajUCiDdCGI6Xn-fQu6hkQXOLRNMaP7ahW7-f6l2_T5EdXqFJzQo5FNgFmSmRF5vg0_6ddSTSDmXN3Pg1xtx8sT5nuqwLqf1MiUSL_kjOPyd-BghuxzN_WbWuKE9ov_yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
یادی‌کنیم از مصاحبه سمی سوشا مکانی با خبرنگار برنامه نود که فوق‌العاده وایرال شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/97587" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97582">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3UftRtu6ZvRy043BoRt4o0bg5b1Y1wdFJZy2pJP4719auXKZu9T1Btr64qZlTeNV49ApaSLxpitlZ7aB4c_gqnNBEnBk1neLff3D17Ov-rwCpuw-xAADx-qP89_n2Nnr_jv8Dau2seDGMK2-l3szKMGScvQDPsS22_09NJfGngQlPoZvV-NwXaKTLdP-efOsdwq5rQVXh8F9sJ7TmNdXUY3_IvkP3fn2uNaUXi8vHW6uFCPh68d05PGsvqEprLgWw0txcpnC0cK9c4ZSsVyNPzPBwJ2asQi9avfzua0siUnuLd24_jrCwdNH8q5qUpdld_a2ChSSnBimKorgNSJgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YpfpvXl7eskzXs0oki0t_QMGE4C9abk0aZt9vLu_UN0dvqv6c4OG_nBNRU37W8cRJKK5Br-UFaoETpc8Efw3EIz41IwLEUVyiyWboBk6mQa3GwYBE-8vRQPoxW6OSt3vS2L45jAXsiz6p1QQkX-IMK0GJkgCplL7Pzgjwtr_qP0dHjysoa6XFpZgDAzAx-pFzo57XBnCO0sdHbf6GDPhg8zX6UfU8PnkqaI3YlDy7zK_ZmTTHZRBn5VUm7UbEB8dVEyhIm-uS6_6smtUkb1rkgeZq-uW-0k0Y1IYU94uT12bahZ2yClgaYd9tTczN1ZF8ITnjaADRzkjFBcoefjyLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HUJdo6EfWs1uPG3GrG41WYyZFIYQKjPlU2jY9j9112zw8z7hOAbX1BSuuXOXWFxCNpSZcTa3C2X40EanEHo85lASzSBkI8ABvxkGiUAZ7EKMoBoyfmFFGqgj54AUDfvn4yhzAU5ncEkGS8K3NJG8zmYOQsxzMizty0-k8pNXOD_IZriaESW4M6HtB-VxkYx1pUUS_H6cR5i13tXNrenhK780GH1yOYo8rW3j7W1ry6tAnkH869LFiY8Il9BEvtlzJ0ghY-IE2QMihYvfHpQysTpt_T7NfSeKC55YLq21-koApLnPYP0qCPVhyfjoWlJNT8R5mdIFl09iNje4fjKHIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rA_rQ8HqirnhnpgQlFebkfVjHcp8fqtUEJ_t5Ob1ngK6T3TfRWT2EvOuw1F1bgg13bS7pknXy0WltuKgtXo-hGQ4wTujZfA1Ndh71MsLdtdZjqJr054GbiWtqc3TxfjGgg_W3LWwIu-yREyHYR4TydZeVAouetzk74V36kJea3YwG_a9ZqFFejNWI8KXiiFyP6XC7t8naxn3tyksWiKbjRv5b8bUwVTV1OnBEBw3bslNXZAEIMc7LOWMtqfzLJZ6ONWbeLjMXAzCVnXrnCD6uxYaL8uyec33StAchMU_voU4aSs9OBxtqFSk3KLyPLvnJ8erQHh7iM_4gwIE3xZToA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PD7dEKA2P2mQkTiWfa-Gy9i7Heck0OkGgKwHxxNKAGYcOVnXcOnYSPtKCRZxYzsL3XSpg5Tfq_vutwMszdM0WcQChTYsRx6mOXMJzZS_ElM0-DADgfga5_JxBOPjtMLCYib9uW9QhhMAa47sq4Qd1hXaE7k6-iEgUxYNWQr2bbq6eCxYA7FQjOsZ-gNX4i91MduNvF0VdUYGdJUFDMXPiQs8jGZJtHWTV-AViFCiqINJ9VtvHrVxcW5OCjSjoPzGJ6V5VHZuMcgnbH1XD4E0deVtWabWfxDf60LSMnqfkgVw91_bCAn8neGE0o43iiYskRo2Gam-quWtKcwHNfFdYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیت‌ بازیکنای انگلیس با زیدیاشون بعد از حذف دکتر کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/97582" target="_blank">📅 08:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97581">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af6bf8f214.mp4?token=nGrUyJ1vdAnFdXm8WYkY9ewVKmrQn6utGWLV_q9p8bzZD0ugfTet3ukGUGMySqYRBkecIfca08NmUcWu2d-vNwyd1YWeKRKMy5Nkg2YNki1NOuiW0HeKPoJyyxHZg4_c7es8pM4eGsM7nQpWOs0KJyrieu8wZgtaE_-AUy4d3Y3mwzU_VvGcb3zsAx-p_1oa7SEQ8uwUf7bJEzEIOz-CkG8O5q7nAjyGsgAshI2Ix1T2BZ_cnqLhvfxDes95zpPZw8szx4zrT2VrB3S-zHLeJeKctZkDLljX-APMu3K70geUtz_Qc5nWuEz7mkwDP9fMPncOpkoa98aSOTxS3Mz_ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af6bf8f214.mp4?token=nGrUyJ1vdAnFdXm8WYkY9ewVKmrQn6utGWLV_q9p8bzZD0ugfTet3ukGUGMySqYRBkecIfca08NmUcWu2d-vNwyd1YWeKRKMy5Nkg2YNki1NOuiW0HeKPoJyyxHZg4_c7es8pM4eGsM7nQpWOs0KJyrieu8wZgtaE_-AUy4d3Y3mwzU_VvGcb3zsAx-p_1oa7SEQ8uwUf7bJEzEIOz-CkG8O5q7nAjyGsgAshI2Ix1T2BZ_cnqLhvfxDes95zpPZw8szx4zrT2VrB3S-zHLeJeKctZkDLljX-APMu3K70geUtz_Qc5nWuEz7mkwDP9fMPncOpkoa98aSOTxS3Mz_ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
نعیمه نظام‌دوست: روی عابدزاده کراش داشتم.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/97581" target="_blank">📅 08:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97580">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrFDvFB0RvhM-OcibrPlCvXVuhhzRT2S23o4K7e0eekOY2IgiKVRKQ-rtQAHD7_lyUqj_f8EJcsjPdMeqWp-hU1Gthhwq07N9RiIlD32obtwHggpezm5Ed-9bQXdqNaDbrZ_AGPGkOPpH5w1E8Fuq27idWTLOKt7-Y0K7HEkq_v39B6W3I8rFdrMFb_bUK6dMnP3ojU-_W5i_NhqgsMi8S_wST8hIbLnCtILmieNYWLH4a097wN6d6ODk4OEnRNhjFPefrrAlFdRJdJib_2t8CLjMHK2owrWrHazz9z4h4M1wSzYYX1oIgVVgbSJjIKUfM61WVqsvmBIXOCKkanJHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
ادینسون کاوانی 39 ساله پس از 3 سال حضور تو بوکاجونیورز به صورت توافقی از این تیم جدا شد.
🔺
کاوانی از اون مدل مهاجم‌هایی که وقتی توی زمین بود، حتی اگه گل هم نمی‌زد، جوری برای توپ می‌جنگید که انگار آخرین بازی زندگیشه. از اونایی که دیگه نسلشون داره منقرض می‌شه؛ با تعصب، جنگنده و تموم‌کننده حرفه‌ای
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/97580" target="_blank">📅 07:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97579">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda3b086b1.mp4?token=BKGPfgEvU0SqRHRXAVA4L-T3yxdE8wTamMBs1cfSiS5EPK8iOiHgTJthVUS737ZblK3W_ePKcrrWRAWclRw62Cvy544CUvZ77aJXkR9reNbBJj2NlXhtQlLWKIBDpGizIgZL89N78Ma4kh-2gGf2j7tl239UuEX8UpW5WJ-hOfb_lN0ByGcwr6nqVLmXYM6mWzEhUSg8rwTrV0DI_72F6x1Pune9SbBYo-Q6J0v3Qg0XycpGh8nnmBif4QUgKcKUZWg0LEIz-NG3SJHIz-6u28mRQFm5SnfdjagN_jv2yHMcVbtDyqIbw2x0gPDHAb28SZm4DQYEfmnCsTPKYTGJCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda3b086b1.mp4?token=BKGPfgEvU0SqRHRXAVA4L-T3yxdE8wTamMBs1cfSiS5EPK8iOiHgTJthVUS737ZblK3W_ePKcrrWRAWclRw62Cvy544CUvZ77aJXkR9reNbBJj2NlXhtQlLWKIBDpGizIgZL89N78Ma4kh-2gGf2j7tl239UuEX8UpW5WJ-hOfb_lN0ByGcwr6nqVLmXYM6mWzEhUSg8rwTrV0DI_72F6x1Pune9SbBYo-Q6J0v3Qg0XycpGh8nnmBif4QUgKcKUZWg0LEIz-NG3SJHIz-6u28mRQFm5SnfdjagN_jv2yHMcVbtDyqIbw2x0gPDHAb28SZm4DQYEfmnCsTPKYTGJCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این وسط فقط بدل رامین رضاییان رو کم داشتیم
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/97579" target="_blank">📅 07:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97578">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d15220e2e5.mp4?token=SG6kZHXlkX9ZyClkd3CKREeidLp21QLj12Np7dyqRTQQy5BMW_j6H0bistoKDzqH0oOvnMUWigzX1Vj1iUUr0mNvUpZoEBFFJd34CYjCIX_zliO-aO5O2l-DZiOmjwb5hp9TYI5YLOQLjpJFsC2SkyqL15RB7CoUUWAwhXxWBSMrzD__67VUK9C0JS3RUFUYkG9VixyDVLECPeoHomRkg7FrhSdDaBnY-n4YxBYn9lVq9pLgoxiQXhUbsRDd0pWTyHSWEp8Z2OaL6NssYtxDov7akGjyNVt1ioqIKz6xl3IjWmqrX1sZFSO9xaI5bVGWRtUJgJX51sWEY7nRcT4zzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d15220e2e5.mp4?token=SG6kZHXlkX9ZyClkd3CKREeidLp21QLj12Np7dyqRTQQy5BMW_j6H0bistoKDzqH0oOvnMUWigzX1Vj1iUUr0mNvUpZoEBFFJd34CYjCIX_zliO-aO5O2l-DZiOmjwb5hp9TYI5YLOQLjpJFsC2SkyqL15RB7CoUUWAwhXxWBSMrzD__67VUK9C0JS3RUFUYkG9VixyDVLECPeoHomRkg7FrhSdDaBnY-n4YxBYn9lVq9pLgoxiQXhUbsRDd0pWTyHSWEp8Z2OaL6NssYtxDov7akGjyNVt1ioqIKz6xl3IjWmqrX1sZFSO9xaI5bVGWRtUJgJX51sWEY7nRcT4zzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی میفهمی بعد این بازی باید اشک‌های رونالدو یا مودریچ رو برای خداحافظی از بازی‌های ملی ببینی
♟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/97578" target="_blank">📅 06:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97577">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veEtzsb6SRfNJVaVrWKS2hc7XgCt-GcNy2D_YfbO4ysOPJQBwDEcFUqiZbi72U9z3vSEzvbVBdCdsw1uHXSUtUj5ZpVgzuN4U0y0pKeaIB-mGZ6JsL667vMw1Jk72wbNc4wYajb76Pj6SXtswg96zxeEYYTce7nuIlKT_EmjkjIPVQQtzNi7gmgHEJJYiKIIC1Sjbrq9dIqCqFD3XLfy-QpJfzZuyYGyDzbNFvoiDx7ibHKppcSjftJccgaesOKIZ1WSBlchAFwpHfg2twcsquSFlSLgMhxF2kRx59wuHPcaXhwgBaqo-Ka2aQnw9_csxNsUgtFXpOrNarrgQzq_Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🌎
تنها ۴ بازیکن در تاریخ جام جهانی در مراحل حذفی هم گل زده‌اند و هم در همان بازی اخراج شده‌اند:
🇺🇸
بالوگان (۲۰۲۶)
🇫🇷
زین‌الدین زیدان (۲۰۰۶)
🇧🇷
رونالدینیو (۲۰۰۲)
🇧🇷
گارینشا (۱۹۶۲)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/97577" target="_blank">📅 06:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97575">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tnRcvtu1ZgNRvIProSHpJQXY7jbekQZkNOoL36Tg_a_oE4nLkeilakHGN393fSz30Nr_Zntyta4Zp6R1NrHogZJ3qHXec7w9CxWiuuETAtQUOqXV_FzIfQgNx6KjTXyS9IVyMI4lUT-eDKlKTBxlMs_o7wnKyaArf77hD-fMMFXUuyHhrACpHGC2XZVAA5_XtuPCd1Cr8MA9yGX_B7_nPZOcOXWhYeGBCswLUqJBsSc7flXTyTTgTByUPThgYaljzIVbmWXTLQD999TaVs5muDUtb_FPeqBE66sINrWklMQO3plH7JeSeh-tdFdfWwsC9ilc9hhd4EZwBhkOVsLKYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/McWixT1G37ugNY50QhtkhcCySdfvHCiDkeQvWCQEAOFIpYXRfMca_d4MTxlNSTWAkCOJXeBTX28jKbE-SoBH2vZaQxtVF-fuScAeM6isWfob5XkiuvuuTjEM949B7kv_h_u3Fv3_ppkBJogCjU_plBNJxGyInfvwkCTbcTBUFYDeExPsOUtyWRh3Q4Zoc16GUSFkB2TZZyDbSbLvA-SKfvllhrSVwGNckGhShYZPRC3dbb6T-my9KDhvxbaQ5LnbxEuuezaER_Hl4kwS0OjJeFQNRvHVcz7NyosikHUf8DGc9n33-t19JHZuD9E11qZOtuAmKEAnV0sAq-3DkFENEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔺
پاپه گی در اینستاگرام:
🟢
بعداً درباره دلایل حذف صحبت خواهم کرد. اما امروز اعلام می‌کنم تا زمانی که این کادر فنی در سنگال باشد دیگر در تیم ملی بازی نمیکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/97575" target="_blank">📅 06:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97574">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0RXQV57O4lyK48rJH3vUwyYqtUOpErxICz7E74MOGRq0zOLIC8tX4xAx8QsjQT5DwAeq8lxzFiWJGxxj-lbLI7eGGG7iESAkue637uqNSgWnnZwybW4ai3Af8Vz37dKQm1LRI9OCGP2v3eKMN5EPhpeGLkfygXOpVHPBAzTHsUB_yJqFaofFM7HiFg3m4qcktZnk7p6NzAAxoAF8vBpy1BHUTHBF64RYKE3QDhXtHYPR6Rus_BnRd248JIsWHRVTG7fcgzKLGF_e6A1P_SJzsLUdrjBwBtAl9RZ5KV88SIlsUU1Ye-kaWkaG8XpHfF8A92fr6Hh806T-sP_lSA_7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار درختی مراحل‌حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/97574" target="_blank">📅 05:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97573">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ajy1xzsAuqIQuPJ6vcO2PE2QLhR0wL__aA8ZdjtYxU7oWw_6Wfq1Bf0gP8Eneu4XbuFBiz7zE-UvL31xx2m4OAqo_P39R90nwJvQkBcTjdM6RX8mrb-aZfy1nbT9ySwpqozzXQ_C10BUA4ZUkau03I8bvmxHWAXbVMfbKOLazYsIzis0TORQ--OgT-h5R3fSff6P-KIvgnW_3EEhh2fm7bSXtfjHteJ11HwxH8OaFYjzp0gRMjN-P4UJlHF0ygb7jK9mvjhnbfzC1Fj6KIOtD3uQiE60NTiDM8FL8Nbrs0DF0lkBCSnv3nVVXBnUr7ElQFSyAuKIuYjMrQHFCN2HfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله‌ ⅛نهایی جام‌جهانی فوتبال:
🇧🇪
بلژیک
🆚
آمریکا
🇺🇸
🗓
سه‌شنبه 16 تیر ساعت 03:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/97573" target="_blank">📅 05:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97572">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N68DJR7dmbTCJKwajX1p8dyDBr4RDvbWYzr9Y7PbR6mEXsN52_RCQd9lonSKkx04LB2bbwPMnayysb6519AnulzKNs-jDfiJR0PXwNnbY4uubvgvrL9pvKkME1GxBa17CL74zNnDNPMPmGp4U0q9pE2kI2ja4JFmXIz4S_fsqQ5mafy_IxbPTPuXVTLuoD8-mVq9TmizB7Dek9-khiVeVLWrQbXyYDBjcU7rI-TQqD1JaFpf3mbv9D-N47cG7UBaTzkgqdBz5QKQfNO5hwjl-ub65kuTs6vSlgLtOrQbywk2ZWFceqCaYVq_oitabSyJmgILwCN7wQtTBPLA-QPF3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | پوچ بدون بالوگان در یک‌هشتم به بلژیک رسید؛ ژکو و یارانش به خانه برگشتند.
🇺🇸
آمریکا 2 -
🇧🇦
بوسنی 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97572" target="_blank">📅 05:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97571">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSusxyUtrJuB-easO_OU5Tc38HWhobfxKc_-rQYo6Zx2_kuqMRf-e4HsH3kOvRYE4_jOphHddku5akC-6-qh_HxeeHcOXlEYmbwW4mTfFTavZ_NSczXkto348DTHxEJDG4O7C-F3rpwJXMjhW-GEXzqEVEF0tn59kqn6WNagBOnr-BwzybsBPwmtbE5AupG6h4KOriJ0pAqZJ9tAHN2ypzTMTtp-UWqiggUxcUR1Yh7Y6SOpjsfmfY-Rtg4GPdDgqrq_PWtOj6SNfiiQFubHOAWi9VuQ8s-8WWdvgiLBB3vafshFtqhNJhE7UKN_7vaaUxUHxBBYTPR9tRPMjzCeQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#رسمیییییی
؛ آمریکا راهی مرحله یک‌هشتم نهایی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/97571" target="_blank">📅 05:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97570">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ده دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97570" target="_blank">📅 05:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97569">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ea16f99e.mp4?token=CP_6lpwZERtVRvutqk4PP4JrXY75xlebHiNmeXhNAyfY5WoFjwd6MEPXh8jSrOP7oCkP3yktLZ70b8yIEeGg0JZ6eN8PDR1mUVrLAW05-_qEdBqwlmK417IeZSPeWrJ4wmV3agv_BheEE6JuXbaL7brLXp_1JkNiYiD34qKNcWPRQ5_ynRHKdU9sSg4aqgY0-ULk0_7YtR2dUu6YS6-PKkmPQGmp2RhG0fzMqHPz86LRwXiARW9UhlpTWB_IfR4AfATRLpiwP7Px5xB4YXWuVnaMPtdPO8vL4PGqz5k3wNWEnjpC1aW169MfFAsc5KKwUmSHUtN_1mvLBgLHWCwaIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ea16f99e.mp4?token=CP_6lpwZERtVRvutqk4PP4JrXY75xlebHiNmeXhNAyfY5WoFjwd6MEPXh8jSrOP7oCkP3yktLZ70b8yIEeGg0JZ6eN8PDR1mUVrLAW05-_qEdBqwlmK417IeZSPeWrJ4wmV3agv_BheEE6JuXbaL7brLXp_1JkNiYiD34qKNcWPRQ5_ynRHKdU9sSg4aqgY0-ULk0_7YtR2dUu6YS6-PKkmPQGmp2RhG0fzMqHPz86LRwXiARW9UhlpTWB_IfR4AfATRLpiwP7Px5xB4YXWuVnaMPtdPO8vL4PGqz5k3wNWEnjpC1aW169MfFAsc5KKwUmSHUtN_1mvLBgLHWCwaIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل دوم آمریکا به بوسنی توسط تیلمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97569" target="_blank">📅 05:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97568">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">عجب تیمی ساخته پوچ
🔥
🔥</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97568" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97567">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ده نفره زدن</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/97567" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97566">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دومی آمریکااااااا</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97566" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97565">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گلللللللللللللللللللل</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/97565" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97564">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWFjXtokGRG33p7c3UOz6nWwWz9hxER8JgJM9gUC2x7VrH7Y9eteFbpIi5GK8jk8yxn-18tcgNsCNpOoWigjLbni7CxyIbuZX2uZHyPTU0YJfr7aGHwHp0JatILUG25QZzLGdL2_Y8ALcgdVMwSLwYUaEssup2sEno_fFC6gVOSuoltO2is88lSNocFqkyeICFsI7LbwJBSOtEPmei8X3iYhFvnXoeGW1yCdQ9PBKlPl3UyG8MoLk72On90UBySlHIVHZUH4sEX2iDQz0Dih1n45Amsc-a5TcYg0OFY0pkQRTu6ryvuOOnkDK9Qt4h4wrVbwQYCCDFncj61g3wqOgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97564" target="_blank">📅 05:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97563">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دومییی آمریکا که رد شد
❌</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97563" target="_blank">📅 05:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97562">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRIkvFbbz9p_8fexoJhl2RgqMWKnGVz0AfQ5x8qNDZarGr5SBdnL23fxItiZC-JJSsaK0-g9cdmb91nMtLXFb2v8JLfk5QLoFdYgyuLWZHPcjTNl9RebfRnGiribZMAcd7TQheGHccB2FidNvx9WuF5z5lquzWdy3BONvY1BCVD5zvJOZVfr12HvuSChYuQEvWSt4FPGQWndvB43ltby5FQ_vEa76UUDOBuJK9XHSIu5r2_kEvC2zdgRhA5L2t6QpcRIbz-o7AUwccZhtHnNAGZHKsJ2t8iXqV4omDtEJr8qavMH-U8fXADdLkq-okffEFxMnjRSBxBvBUftqGpSYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالوگان اخراججججججج شد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/97562" target="_blank">📅 05:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97561">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بالوگان اخراججججججج شد.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97561" target="_blank">📅 05:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97560">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دقیقه 62</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/97560" target="_blank">📅 04:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97559">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اوه اوه رفت کارت قرمز برای بازیکن آمریکا چک بشه</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97559" target="_blank">📅 04:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97556">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FFpRAjwkuap8_OBY6JJXlwhCd6BQyRrfQso8xh9RZok1fsa7qZRgdqQhElRt_mgkzqA67-QbhURssn_WNIS9R5Si6UTv2FnnP3PUJdcwICvhSHA45pWyiODOcJFeyt6drZf7_cCIqp15Xg15srb0Sdz1rZugd9-AFDpYESaV2Dv7xweoC-cv9r1ryCgCdPJyuCvOpuAKko3bZeK-lnfn5s8Dw0jQZTInYxqPZ9erIVkQxi6IF_YrraAMy9sDxvQyaOHN0MaMcH1aj1veoi8YHD-p2nb5C23qjdby1Eg_XmAh3ufJaruI6Wk1kUa_ySBdSI0rIW5HLOEveR2qaV1uzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N-3DWJek-9p9V9EbmTOHqBsiyxp4oHP-UQawRRPP9DCAkUwhykE3JbD8hXGUNoqMbZmtJ_Ndu1pV3ofuyOMA4v4QjBCGHA1CpojCACOW3mTqfsqbFbp7miKFTKNCprlAir9MkJepwHKNvJFiLOt46e9UBnR4tDhY4aVkO2ZxIG12rUydegtfTGgpUS8FsXwMZyADZ9Ydl-8qUeCZdL8dleQVTQOVJ2vZ7YYlohpujpe79rvZsLRMBzdz1UsxRjdFlQS3g-BLnBTjNRn3x-G02dTUMShXFowEu7zeD4ezJe-ew2P72mzeEolyisBbkbZE8DraKUdz0cG35KG2_2_BoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VSvv6GvlzLA9CWya6RPGOQUp_03irulPtve1uZGjj2Gbw-4_nfSHrfknh3XhsvY-OZ4q-aRkVew76lEQ2wBqhpnGdAnub0S9jybCLEkCBy_H1Z_U2LzPhsXuXIQk2qkcCYIWy1brCZrDrR36JQZBf1MOKvA4Ll4II9wreBzCYFQVPMxCAQUiCV_KxtVJmnNJyLgb0CWi2_IUyY_Xr83J-_fndrZaLF6cXKz4cvFgkV5MNQMF915oyZg5spn_BCUxCRuXlZ2onbWjeiqRaNogvmWliXg_ZiEAoSdIl66yAdSHOFRqUZAi8DRG9zRQN2c8zLuoQmAQZF7DZgZ0QBcH0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
بانو میروسلاوا مونته‌مایور مجری شبکه TNT اسپورت جام جهانی هستن
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97556" target="_blank">📅 04:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97555">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkHoYdVMDI7KyTQIEz9fw_RVU0NPaH3KlUxCJN19xNb5dnRNGnTO_-bsijyY_jnQmWw4IKl9_k3SUeipCgkH9vQm-A9STClD7BsiCa_sfjzZoBmxO_wkh5zHWpIQNJ4-AFrAUogjLlfpKmCIVwMlsJ0VDRLmXmpdNCME-35Kd-WMVsJMBh0Yfnu-IHTnzyxwMKRJIvkgaHXMSkgXdAZfMetgV38HXTZV1YGq98JavSkVUuIygzkPIrMfncablmss5WrRbbFnTtfs3zc3ufwCvpB1zvPBv3vXLNDbHH32PBOFnO11QcUwaKFExZVzoQiW8ExBbhyPwoyxrbG1RgiVXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تاریخچه دیدارهای تیم‌های اروپایی مقابل آفریقایی در مراحل حذفی جام جهانی:
🗺
اروپا: ۱۴ پیروزی
🤝
دو تساوی (که نتیجه در ضربات پنالتی مشخص شد).
🌍
آفریقا: 4 پیروزی که دو تای آن در ضربات پنالتی بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/97555" target="_blank">📅 04:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97554">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C38OJBGkoyO8jSViVVQJiWDSkx1LkCCcOA-5SmmZ703PFlLkBWPus0La2p7Hw2BHquqigrDRyZr0IJrjEnAbFI4q_tRDxI-eTMKSDzxEZOLSYi0eImyxrdNFMNROYuGd0Hn1g_65V3XxIqrgXoZyEiXDeETS8we5NcKDfaYGJ5-Tzo6R7bhnY6JmJeZbWoiWJ64oP6hCe-fOVQyBjuQFw8xYm9mCnKewtEjoPe8RWvkBztaPm1W3bhzvI-WKYJ6oFKCfxMIglebzUuV4f422rH_16JhC9Xc9gMG5pQ_q0_mfJVOrDryUm3Slij-bL5OXZ3dMBhoD7fUtODsHVkquXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخ داد پرز بخرش
😛
🎙
ویتینیا : لوکا مودریچ برای من یه الگوعه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/97554" target="_blank">📅 04:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97553">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/94e4656d07.mp4?token=jdy633_7N3_6kiSwKV95beyjapGm4hg9IUNWk9SMx6ToX0rjm1ICT1Erg5NOqfcHt2RK7wk0csTsvXbgnXUpOfZuqYFiibEhur9UU47WxI2VVfY23U0-ftCcSoF7PcAyU8P8HImEnyr8gj02MT1HjWTdy-8paduSG48uLwDq5kCLWRAIoN6JUuSmKcOgySEo-ctN-c8emfYC28FQheX8iBMXQA1tE1kKVUFvipBMyr1VMxoHP35ccTUL0uqGDnCPAdJvaS1N3oZUGumgosMfruMm1j1PfX-uuijw_UMV1TERo9so3nK4Dfiqed4pQnvzZ_D5Rc4qFCd5TwdHbWMCnw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/94e4656d07.mp4?token=jdy633_7N3_6kiSwKV95beyjapGm4hg9IUNWk9SMx6ToX0rjm1ICT1Erg5NOqfcHt2RK7wk0csTsvXbgnXUpOfZuqYFiibEhur9UU47WxI2VVfY23U0-ftCcSoF7PcAyU8P8HImEnyr8gj02MT1HjWTdy-8paduSG48uLwDq5kCLWRAIoN6JUuSmKcOgySEo-ctN-c8emfYC28FQheX8iBMXQA1tE1kKVUFvipBMyr1VMxoHP35ccTUL0uqGDnCPAdJvaS1N3oZUGumgosMfruMm1j1PfX-uuijw_UMV1TERo9so3nK4Dfiqed4pQnvzZ_D5Rc4qFCd5TwdHbWMCnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گللللللل اول آمریکا به بوسنی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/97553" target="_blank">📅 04:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97551">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rq2fALC65Mk1RCOBvc8j_tAaeZff4739UYqBsvSvBtd2kUct5cb6M7hWBZWnrmehu86J0X6z82Y7s29riMqkeGPmUMfBwmG-Z6r_i6WPb9IJjTK716vLI-PJLjaeAPUxv14i7-nijYwz5Z7YXa4EJhh31c3JYmULy79BZpoQSPZiEXVFtDC7PjUXiZKNA4SMlRmTAWX5jMchizb8vEWZ7I0bVE1d0VF_89jiVFDdDHcEcGONgyDpYA1NwAWiqsDGzbpNcUhiHpVeSEQ-rMzFioWjwJrWnMlW-G8NaMJxA5wzAQanT-LQf9GzfI1XReV_PINlbp1dFFsQiZsIl0QvZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇸🇳
| تیم ملی سنگال اولین تیم در تاریخ شد که پس از پیش افتادن با دو گل در دقیقه ۸۵، از مراحل حذفی جام جهانی حذف می‌شود.
❌
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/97551" target="_blank">📅 02:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97550">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYNyx1J6dQxVxYiW_XS9-OzCwOTGmiXNq9Hk0aJMMMXecKEVaMLgd9D4Xusu3OX_ZzpspsQ1a1f6xJ0Ct8BAH4d_ggtRyNHTRFHSojwJAzn4UX1OEU5wPssRv2sG3ZMbV1UQVyDLvWMnPkmuQbs8HE2J5i0lGwTF-irGywKduJqPOYj2d_9uAmQWEWDyJcObwddImBBINPqxWWoyXvgk-AFSPaKi8rhevFsRyWk_m1f_Oz4hiHuCAYUpn445CtfpDsKLWsGzzJlAkGtc6VnF423uyqqKIy-zU86m2dKyGJI1lKbdrbTFHdbgTDdyZIbppI_Q-avPwPZtIXfD3TX03Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇧🇪
بلژیک در ۱۷ بازی آخر خود در تمامی رقابت‌ها شکست نخورده است:
11 پیروزی
✅
6 تساوی
🤝
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97550" target="_blank">📅 02:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97549">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGQ9ugZLYr4RGmaDNY6u-4xTllEuNIBL6-6sPZNC27HwYESSpxFlR4Bb88a8Cb-3fosj1DdSPtgodEqnHiiB_KiTo6LIPQ1lXAzdwPrqyk2yNtbWP9EqLMGvMH8Z8Ejdq-EmhhZVUx-KBAEmI-QzW2EJD6-uAfA-SxGpTwa-RhVlHnFpGupo48vCqwlT-BPtBeV6itPggnm3hTVFTn1Td90jGgeXViMe7M4KgfM8ATd2cKb1EqJQfcBo-Ad36Bm7uE_YJydE6M9j7a2FdQRj608jKESL_uK3uKxc9RSge5y5CZOeMQzzDYy7OSGUfEG-1NUBwKPWYNB_EzQcFZ2SUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⁉️
🔥
🏆
بهترین بازی جام‌جهانی تاکنون
؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97549" target="_blank">📅 02:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97548">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoU2xFz0urOJU6yktkoTvNJktl9PJ8MdpA9gil_jMeo2eNZpYp_z6HadHwbX2WE4heglSdRw49B0RlZszMzS6HbLdBeC2HUSEGsx_3Tr1qUil6Lg27PaUsSvU4zuWEwpw1VBIQFTQQdTBDxZQFGlSNz5IBNNNOqCUkaz2w8LMR6PpKvc_0MYWziKzFe7x7lriVitFFEvE1sl_PlIOXlLGf81YSvKv2yQJpGCiqscbPx3kIbYFtDQ4SwU70q8uYhX5pgvO6fitlZDwxBizg1Eupy8poTCt5a8Dzs9yHc-AX_qBGGcbYj0cbnIvN_zZxkFrHnARNtxRa9CvttEpcrCAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🇧🇪
| بلژیک برای نهمین بار در تاریخ به مرحله یک‌هشتم نهایی جام جهانی صعود کرد:
‏— دوره ۲۰۲۶
‏— دوره ۲۰۱۸
‏— دوره ۲۰۱۴
‏— دوره ۲۰۰۲
‏— دوره ۱۹۹۴
‏— دوره ۱۹۹۰
‏— دوره ۱۹۸۶
‏— دوره ۱۹۳۸
‏— دوره ۱۹۳۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/97548" target="_blank">📅 02:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97547">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvRXfxTqTAR4_icgR2pjDl9KZZzWWBtqxMdDOcx00nWX4WxmL638y5cbGJRt2jyshXxOTzp5c6e2HjghYq4rer27THPkHMM3eSETChRfKWwP4iUlK8dUdIkrp10EFpNm7JXToO7i4YagspzgvgHw-ORgOJe6_qjq2Kh3mIobHbMwwldKcwmhAFVqR3ZT5PIu_oZhLT4ZG3AbhAFKZFtzkqAdveWCr4j73LxkJWfR0JQ5vUcSXrS8Z9DTPQJG1G2d63NFkiD1Shp2sFSvusmcHm8oXimdBaTB_BNFzYIzGgSHjjWaagKni7tPbpZbE3k1vWuvHkil1SPTFDC-tFP98g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
| سنگال چهارمین تیم آفریقایی است که از مرحله یک‌شانزدهم جام جهانی ۲۰۲۶ حذف می‌شود.
‏ــــ سنگال
🇸🇳
❌
‏ــــ ساحل عاج
🇨🇮
❌
‏ــــ کنگو دموکراتیک
🇨🇩
❌
‏ــــ آفریقای جنوبی
🇿🇦
❌
‏• تنها تیمی که صعود کرده، مراکش است!
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97547" target="_blank">📅 02:29 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
