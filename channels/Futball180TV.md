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
<img src="https://cdn5.telesco.pe/file/Uo1KV1i3JQ99jogJx65kuC8P7tIK5U3iCG10r0xX-QB0oaC7QHtPQ6zw6THi-ra7gZIlEKFDK7DsbD1YJGzlcd64BZPVzNqNuzZkO44OdYSyZyKn-cbC0bBjUb4tUIBRiob9r411c-AsYJ_bQpQ5dbEr0ygtLULoAYPAz7EHxCKqCqc-mkQmRLx-h0A9Aa4EoQoTYnZsKnXU71WiygkawXfwTpFF5tZJ6zc9GRk42XJWpuFSkrGrYBnVaLU6w566eGPKZpi3KcFsuWa0XkTJULeAZF55dUU5fcFakpdlU8cgdV-8GvzDy-kxo1JdMadfCduQJgXvGoLvd7CrFPctOA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 679K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 13:56:39</div>
<hr>

<div class="tg-post" id="msg-97113">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ef2e2b2ce.mp4?token=bI_jrMv4c-7MiV5X1Hv8sRqIv4Kn-bBcJ29h2iGw25QguvFrHQqSNhdxyO8GM_a1zILEjHWLRhdkhIR6X7sDToAxklm0KJgyuGICS_nz_uuTR9j5Ht975sdF8mocuyJaFBA6gEEEOsFLg7W9hlzgAAsfQFhDyRV_9lbt7ki17_f6EXIm3fkri0Dr3rZjXu0TZqcEsjrpssat9J82ObJ04d3PyswjIuwR5Rt-DqJJcMwSPR8p2cbGPFk9ICZUMyOhQIXKOJN4D39D1WDz71W1tUgdBimMyEA9lpdJswTicSscYjt9SiASorOiuTR2Pr8_JetUCXphR_XA44lQGmI5eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ef2e2b2ce.mp4?token=bI_jrMv4c-7MiV5X1Hv8sRqIv4Kn-bBcJ29h2iGw25QguvFrHQqSNhdxyO8GM_a1zILEjHWLRhdkhIR6X7sDToAxklm0KJgyuGICS_nz_uuTR9j5Ht975sdF8mocuyJaFBA6gEEEOsFLg7W9hlzgAAsfQFhDyRV_9lbt7ki17_f6EXIm3fkri0Dr3rZjXu0TZqcEsjrpssat9J82ObJ04d3PyswjIuwR5Rt-DqJJcMwSPR8p2cbGPFk9ICZUMyOhQIXKOJN4D39D1WDz71W1tUgdBimMyEA9lpdJswTicSscYjt9SiASorOiuTR2Pr8_JetUCXphR_XA44lQGmI5eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🌏
پست‌سمی پیج‌چادرملو بعد کسب سهمیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/Futball180TV/97113" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97112">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_2MgLXZOh5kfxPkHGWi4GhtWw-f30Sp-RLBQDzM2rTC_DBTB8UAjGShm5M5KT5zsRoYDm2VPKErVRkC7-I37_wpv4Z0KdnvKbw5RJDchoI04oGW90V6SAruQMKDGkGIGf0fj8Fj_TAiu94XHeyOQ-_zcgT6yU4IZYlcA1PRjdI0AOi8DREliyfH-tYxKJsowcNS5mYnVfmLO4teiDdQxj5XGkL5LU83Un0-hAQPbdU7MaaFNghpyawzT4eHX4DXUyXbQ1nFCv4YnaQJHHtAsqd9Cv7wg4ZdmW41xviVcT8_psHwrESMjv5lJXSP5w9jmriQtSPUJl5ze-xyaNN0sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
#فوووووری
از رومانو: قرارداد کاسمیرو با اینتر میامی سه‌ساله هست و بزودی رسمی میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/Futball180TV/97112" target="_blank">📅 13:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97111">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oowxpQFzkdN0UVdHSdTYwT_T7CgelnwDk93BvdVMWElrbiGYrDLvFdxw2Xn6XN62UTILokqfdYn5MxuB75ZZlWEVWJIU0Cq_5syMvM-hbbhO66KNA1bkf9d_2c1iAOl5wWwl2G0Q8V9OMyOZmq5Nli6_kYzK_MSa7VppZLETBfX91qCkjYWsZQWVppmRsKJkI1qD6in3DU9aHhrNCRO9IMp_iXbGoGSk7i8R7yv_hLJA0PlhSm7vNUrKDEdQy7X_av-tIcP43lYmT9pi2dPKsduEGlm6Dg-MOeVbfyMfmQZ3ebu8PfQv28CrV7MySsU2fqkbabxq9YMMGRWCA7uYKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متئو دارمیان هم از اینتر جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/Futball180TV/97111" target="_blank">📅 13:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97107">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pDt7PILPWDS71ZbcQ2RXmIeOuEU7UgazyJEuWZvEvFBUfkpfQ0ITgDzGL4PI_98UNkoB1kn5spPwVhJn94_xUn_AbGbn5KUeeDMKxrd3CkRmOZf7E0tX3VW4C1vashFMeMsLccU1GA56-QhmtmbCKNiz_JpXzsT8Snnq9psblSuAWjBOXCIYHpXasGB-aihu-rrNc5FvcxwAvu2MS3XmBilM1_HUvKN5qsBfmKAvcIrguppyzjni8Z-PzngNIOCP_gNlb2osPUMBsrbOWVi8qJcXHLRS9qAdcBhLizmh9bpC8Sb6CE6uC7qKThfMYnkeBq_fyejvWtS6MmS4xrRn5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KXtDyA9_fWJJipoK9l0pU3-x9xScrRvOh6DjphGAwJjcNhlcleXR5m6VQ9lZKOx7qLkhT2wZF5C5pposyluqT1covy3ePLJvTI7sXCrkD9EbK2ShD28i7tNjwAXzkhTovzEPahawnm9_iy9926v60FET72zjHf2lW1KtwYBWgV7nZ7b6eQQ62MN3LdC4K9_YyNz3OEnN_Lmhz22UPZXFFYD01SLztmHxh_fMHCpOli2s1iYs_1GdgpAHNQ3hC3AtqwsFAnZonNww7BKotfcsg_dmkgjU3tQHu53jKJCxdx0yhP_ibeQzLzdeo7Fg40chj6dW5WQHarEExBMifimTvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7tzDjr46ptABTY4s6WFkFKSXQGatA4Llh9U42Z9RJ_6xvyyOICIylPGy1Co-YTHIhU6qqvBercTKuNOXc0hfO7DOaBXeooK9gE9ClaniG661EgBjeNvjfsNU_iM0rgS_sa2-EXkF9kFQl6BJreuwYMeMSghmDal0btpfCpmExXmdmyhqNplyl6Or1WxOtg6snjaZ3kqUmDX09ODM2PqE5cQ2BXb7BvrION8ZCprrAoKfbcvZmdmD4hWTXAkjMDfvC_FJip79yQnX7L6uATIE_7dVY4i1F7eDx6exkP6VDEzQ4mGM46xQwIaHJRkG_6fCpb1EWmp00coJjFWi2Qbww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VwGsXzD6YC8eR2RWjZxIY_k9yD80Gx8rD4mWiND9YW49Hu-qV2owimqL-Q1KpzutHYefdLGOQ2u0aMSo70wi4G2APLRYNk4H43uIag1o_iGfC4djMroaHyO5KmGdc2i0Ao-WPJ8cmq3jDU8RdqSW_RfhbZn1npwtL_hNRUNEic68veu2Eo0C8TD_b2O80P8FTB21Bqu8HngdEajLPKgv9zGqbrPzWWJJCkDGdsk1aSVsBwWBDNrKOIfJWuu5LLbBR0vTILjRDueNS7_SNdz5u8_ASEciLpTe9Kl80BmwCoiinbVj5ZRkSfLvHWynTR-U-hn9C0X7f5cKEwJxKNdGhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
تصاویر جدید اللهیار صیادمنش و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/Futball180TV/97107" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97103">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcOdKCMD3rjjcYbKXHXEbbkj29WQKZaiaoMNSRMcUQQUdEUYILFsnc_PsFMbjaY9rG9c0xc2ijiwPnczmk32AmE0XHoq-2nSwC8x6z0JuRO8Esc8MvxBhWR9CuP0xpJPXCEU-s2Ckj0yhsqXUFQlQNIvfiVAbb_m82pePFbePBJtw2iTvw6gJhJmmBgpP4OJ6Ce_kQvZwYLnKYohg4As4iu4pmd0KSL8JQhpLM34Op03SdP2l5Qq0NsdrNVuEl1-rkaw2bFEd1ZerrvMtcLzpdOMz38QI2ZeZDZblLdzuqZgqNdOS5IAOTMEVe-4gLgIZdyvWdKsP5akXKFpFxzU1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KcC7SaNCeUEijoNnsK3LfyGIMkMDLixpfixCZXdtoQ7NC2Pt51QrIK125sDdczb5xm9syTvGVcI0LN-ktazaNCUMABaIp_zpnu7BUbZruMGszqE8Wl0ZJHmddf7n_1rgxwiyB4Qkd7ubjmRT3vUqI3mhKv30BGGlIlaM9Sy_R8y6DOnAhUSUAdApFyvcENIbyb_uESKi5C_16S_syeryij1FgUy3DUpw6RGYj4B2LKGClE7s9JW4NBh4FnKpQY1XAGGMrs59H9srWLkeVqj01mQu-Rl5jfu4IvDJ9KnIXgn8Aeyrh7Jsj55PbT23iagcrjFJ2i4wZhnl8ysAA7gtfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qCZcHAoy-9wC3EQQi9zMb-4SIpD5befDbT0qxvpowF9LjRdUt1Gob5r1owQOm_VKH47e6TgwNZe-wTRkaiNjsRfalszAcAwCmoATBHZUX5gUBrxnGjQ9jOXUh7Xo-zBHjbxgmFWfxxnKqfEy8AFuQ95NfEltKB8aPNBc7LaCZfhS5iEdovWU_jd155fcRG4QqzWX5h-LpxJti4f5iJg3WYEEnFK8bpkN02vxMeqIWX57nk4LYRcvwiBT-VinHUm-DpEGbnJVuWnN_Iksu8ewzq7FGF1cSMoq5ROK8K0T3Vn5MBPjczJE03D8dNzwmtmHmz2tICxdST9yMaGxrGsbgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qze_jRWZ6NUWE-HLFAQyQPlS9zG13X0XCZaoMjBHzNlRkia4McGG49ZjfpKGjnViTQJblkF7kLy3dxG9NEWM5q-B-mJfk7TGpCRx5UBaIok8G_WzlL1j0RQkds7S_WBPqSLejODImgVP3kM2yjQyFS15AX-ELJJLUJllULo816OmbDvQRWc87qEnWv1tYaAAafX3sa9B9z9oxwKuuMqKzcHU5o730QbCACw7lPhThAuqRO7Mb4NbHkGTOyelQr4nhoqTaKMuRNAyvWW_nGUnidKudNdRYqPV4lbvZKfBp-HKtBl6Z3nqg9_2q-_50rMV_RmzsxRH6xTobCrl2b2Kig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
هوادار پرتغالی در بازی اخیر با کلمبیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/97103" target="_blank">📅 13:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97102">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThlxQKcw-xhQiw11YvOC1ZKOP-jkbhZ5wGSwS4LZMRKg5zpL9Hd_3ic-LAcJ-InpLuQHgyBuK9xh_nPElvB3OAlztu0_jcVw7CY1CqK8lQSvkRjVWshxes79-iUoGnJ_XIgNgRHi3Ovqpxf4-yzhIaBwu7qlmsd89pgUra-3c8dYlFz39CBU9wa0eL4G-ar3f-DCi4-c5U_KtnKnpzla1hZF3JPb31taHrCpQ0LuZaSqCEAvPCWhtI-cLSYEfbi0W2SDI_dExDQj9PcuEQf4b4elGW44bw_WsQd4joC2NV4Vd2lGIXsta6P2DjYloPk1TyWRLxkn4L8c78uPNp7CKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
باشگاه اینتر اعلام کرد که آچربی مدافع این تیم و کابوس بارسایی‌ها از تیمشان جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/97102" target="_blank">📅 12:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97101">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b3d094a9.mp4?token=XLrYEkHfPKiHx6Isu2l0AvBnsnX5OXv7IR-keF1f7iVMvTrIOw90HDfpda4z3DXHTFC7RveL_JKyUjI_0lO62ozruAUge4lLqhp1oM0mqKFiwgxXoiSJhQp0AXdpD0AdfVAqb5ryldI69nnNJLxlA8i1hQfX8c56idOLBwvuRaNolPdhgnNZB6XfbPRta32apfnLgf_jy3USWQQUIHg3-vI5jBlOUbggsqaGWq_qVjVuCLYRPEoyZ_zQTeKX0OGfQ43nx523O2f-mp1Lgy42cfDTlHZs4dzfTN7XdhxMLNqsAaSUL-j9uDco8p6aLiXH0cXNW6PTEfrSneA2Fwo8OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b3d094a9.mp4?token=XLrYEkHfPKiHx6Isu2l0AvBnsnX5OXv7IR-keF1f7iVMvTrIOw90HDfpda4z3DXHTFC7RveL_JKyUjI_0lO62ozruAUge4lLqhp1oM0mqKFiwgxXoiSJhQp0AXdpD0AdfVAqb5ryldI69nnNJLxlA8i1hQfX8c56idOLBwvuRaNolPdhgnNZB6XfbPRta32apfnLgf_jy3USWQQUIHg3-vI5jBlOUbggsqaGWq_qVjVuCLYRPEoyZ_zQTeKX0OGfQ43nx523O2f-mp1Lgy42cfDTlHZs4dzfTN7XdhxMLNqsAaSUL-j9uDco8p6aLiXH0cXNW6PTEfrSneA2Fwo8OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
وقتی شجاع خلیل‌زاده سوژه ابوطالب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/97101" target="_blank">📅 12:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97100">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAzKXdhgggNMhW9_gtnaXXQ-pXE9pes0sCexohoyGbqW4f2AnRo9WbAvwliq_rHjoP0a7h9Z0MSKoqSWWNuc89b7X_lgWtvhfDxgtJApLXRiGrssLXbZ862yLHDiwWcWuDItUv5Y5AQt4_J1I7xhcBDU29prYT-hwWiK0bNnG9v5G4nnNjRJvYHq8EGBdK071zilp_xjQ03NWrHVfi-K-LR2r9-MpUB6GthXWe2tW7uDYTC9h93saRT_Bk4mWqwb8Z8Bs2pPaShPcpgEAW_wDmoRH-bbYPgAkECcGyLsYYJhNd-Frst0FDWtgYthgPhf01SFQ840FUPsrUnT72VMpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🗓
🏆
در چنین روزی ۲۴ سال پیش، برزیل برای پنجمین بار تاج پادشاهی جهان را بر سر گذاشت و فصل جدیدی از افتخارات سامبا رقم خورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/97100" target="_blank">📅 12:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97099">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/197441ec59.mp4?token=eITAWPeWDOGfl5sc1zsCWTZDJ_eOM-Sj8dgtg9LXsQuGzIp9A5K64aWYNqCEmMDRV0JWVBIZXN1vYZg97teWidTAv-xEwUEu04MqIWDq5s1QQv0po4AfY8z1h4iECH-wy0rb_AmoJZr6WaIxUubq7Znl0-pt-0YxKR7c8TkXgp8DtK5pqrBaWpwXvXv96MQRNzoin6YN9qD2V9tTNNocBoHvxpE5LVesfxJLROIY9JtDzBAaBhs4kwm9OfuQ4VwcStIe_fDjmY3AnQXYhDt9AcbSgqHU8j8DF_SqlOGeZFu4uR2nNUdnJBKm430nWOvMlP5X1JLC39xl496Kb00Lhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/197441ec59.mp4?token=eITAWPeWDOGfl5sc1zsCWTZDJ_eOM-Sj8dgtg9LXsQuGzIp9A5K64aWYNqCEmMDRV0JWVBIZXN1vYZg97teWidTAv-xEwUEu04MqIWDq5s1QQv0po4AfY8z1h4iECH-wy0rb_AmoJZr6WaIxUubq7Znl0-pt-0YxKR7c8TkXgp8DtK5pqrBaWpwXvXv96MQRNzoin6YN9qD2V9tTNNocBoHvxpE5LVesfxJLROIY9JtDzBAaBhs4kwm9OfuQ4VwcStIe_fDjmY3AnQXYhDt9AcbSgqHU8j8DF_SqlOGeZFu4uR2nNUdnJBKm430nWOvMlP5X1JLC39xl496Kb00Lhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
💥
شادی هواداران ایرانی طرفدار برزیل از صعود به مرحله یک‌هشتم نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/97099" target="_blank">📅 12:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97098">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c36135326.mp4?token=tYEC8mDCJHBzaurDZRcJ54Fwj3amgTf-2X-9IPE7BoG719qfga4OHMymj0o6jImhbbjnuZtntEVWkOx_A5_4Z6Yx7iRK18ftFN_mOxKmtLs3fwsMyu1gq3ckAxrXRrdGeexAMaq2xGJ8aG83exy67_aaXfbWjfp7iruc4hVasqZQnxc_nQwXVXp_FousHowW_R-zH6SvXlSvljFEt-Luc10cyF7QbTcmc8N0ebB2Lkm0ad4D4MmqkoLNHHRTYN9AXdpD6XYFNLnUzKLgViOttDilnOtSrlxjFuVQByRKxgoyWgk0vrSbS0_UyyQ91z6DRGmZcd3PIaFXp5ankP4lXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c36135326.mp4?token=tYEC8mDCJHBzaurDZRcJ54Fwj3amgTf-2X-9IPE7BoG719qfga4OHMymj0o6jImhbbjnuZtntEVWkOx_A5_4Z6Yx7iRK18ftFN_mOxKmtLs3fwsMyu1gq3ckAxrXRrdGeexAMaq2xGJ8aG83exy67_aaXfbWjfp7iruc4hVasqZQnxc_nQwXVXp_FousHowW_R-zH6SvXlSvljFEt-Luc10cyF7QbTcmc8N0ebB2Lkm0ad4D4MmqkoLNHHRTYN9AXdpD6XYFNLnUzKLgViOttDilnOtSrlxjFuVQByRKxgoyWgk0vrSbS0_UyyQ91z6DRGmZcd3PIaFXp5ankP4lXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
کسخل ‌بازی هوادار ژاپنی تو بازی دیشب
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/97098" target="_blank">📅 12:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97097">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnZRbm0oipLQabHXJ52KK01ySWVuqZaJWXd5ZHNwqetfV4FbVfi51JuXuGhhFPLnQwK_VGHlBm4AWtzmmJ_yClbjNfETyDFHTwCSlMWX7YMIjqWRm2I-1OxpyQAFeAusuGXoAzgaYhZWD9nrTYB3FJS5BKTPr7HpzVrECdMT72U1yDivLO8_JYM0q7KJpU7Tc7B9-mw_Aw-ZiAgPwLYbEQccfJ4GsVegkcCJOlPitA1wjFc4Lyg4hozFg9lZnAktHD_0xQRK17UVAkuxk8tTMUN6goxNP3L1z-b7Rc87mq34cOa4EYQsoMxsuoXZ1WdYbqzNDO8ZBj2JZaLVYfESJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اینترمیلان از جدایی یان سومر دروازه بان خود از این تیم خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/97097" target="_blank">📅 12:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97096">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnSz0VWb2qXm4b0s5F3JZEBlgPzHZrMg_gA2uoNH9CV31uK-_l26We9cPIXa18XT1pO-IT810RLWZ_CLqrRTqu0MIEeISBLLZy0Ap2e3NVb4T832T9dGqcNciuDF1kBH_7JMeY0Kb_GW1bb_el7_cSM1GtidRRrsZRhiwoaZ97KYL68BOy-_9duHUDnz5I3-h8_78bOqcFwlD3iDgS4LHFBGKimF_R5rUBUVzgGSPHSLY5DRvGOrOmC9LOzmeTR4lUQ-lBr1TGf--BVAc0I4lTtEcpKAwaWlBZSkEM9N4O251Wj-CpYDSwmAPawjDnM1BowpIm6JNuxfuDHQZ-FYNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇳🇱
رونالد کومان سرمربی هلند درباره ضربات پنالتی دیدار با مراکش
:
"
من سعی می‌کردم تیم را بر اساس تفکر درباره اینکه چه کسی می‌تواند پنالتی بزند تغییر دهم. دی یونگ را از دست دادم، خاکپو را از دست دادم و سپس سعی کردم بازیکنان واجد شرایط را قرار دهم. موفق نشدند، به من چه ربطی دارد و چه کار میتوانم انجام دهم؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/97096" target="_blank">📅 12:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97093">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bWZJRqeT6-zprKinpTR2QWrsJJqy8lySCGy61pfVfNPOZniK3a-U8JYo4wdRl9x0h_d2sCPeCkuvcKAsk5kN9z8cGaM5l6GLRDVDb1KUJWmSkzEqUaBiYdi510jeXj3ULj31hVSfMUZIo0t2GfD-Fwuy-tIfQHhiLGViU46uYmiF0PikZAVCP4BPcUlzSqWhTpXmRlsTQatKQl7LU8uUXf_ggf-sojge2Ycegnbs3kITVyEy3YaDqtuZTI-iicHywsAWqyJQ2dae5qaCPE4eM_aFkzmRwbrtyFL2djkGOVtoYSKMm8iTbTFTvRzvIZp8Mnof7mBe6AXZB5rYqTRoPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H3pWsciNY8FutrMQ0Vehu3q8K5jf3Bfwpj8cauMi1Og1bredAoqXhlZC6OH_fGM0emxA58eYsmVIelVQz-JbbmxcqMI4OGMEyDgcdLa4ZjWxuTO_HHgJswGNE-3sBpiNpQsxv_2wAzKBj20fCNL5EOopdDWfRH7vfhdkCaHPZDzVYThvwBqzWcZu7ooDA1hYEHPy4f9O6Vrs9ulpLIrWSn5KE5Ub2b0gqulzX3L0uW3X-ukTXUsg67klH3omr9CnIYVp84Zrxm7cRBApZoX6Pl_-anlL2Wd50LljaWSxAgE_0VyHh0KEjRrUajS1rKTHqxfPkPt79u03RaopqO24Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tKUUgoUkr1TrjIkJrUinjdv9GnaG7Zspa9xdtB4P3NYPu0a1mfa_UQMA0MqHRWd3nBdrHFTGatIbZw-Yu7NaT48h-3zt7wZ_36Wspiv0r842t43OVZB6mQyFsUEJr61Fzg33NJZY01aCiDK0ca5mnSQh-0KrbysIMJj7-MKB_hGcAXu3q3sUu_aF1w492h6gnm9QEiqZy0MTgMJwhyqdd4H9b8sIoATafdS_VHkx0bKszd-VeDafubgPiSXM9x1MD5xMqcAZPf05-Nz9beClKy471IqnqHjLCXLhuQJWJOTjdCHAEfEVm21te9-NOgylwHMtzJPV51a7-dBz0S7RMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🇧🇷
همسر اندریک در بازی دیشب با ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/97093" target="_blank">📅 11:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97092">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">▶️
🤩
حس‌‌وحال دیدنی رختکن تیم‌فوتبال چادرملو اردکان بعد از صعود به آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/97092" target="_blank">📅 11:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97091">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_B-BiRZR5wfsFMD0IMo9CasS3D4GLnJiTEkExzFb7yF84DYs0TaenszUGlNWtTy9qlCMi5H2VSDj8n56v8CODsOi0YTlutfz_W8WlQdHR_KsxC1uZ0b-Qs9CenIWfxITazFfmj6mxbBqOXRJSzaTI-vf8ob7i_tsSOFQfwFdCHnkcXi8WfP4jwdpQ_KsMpdnH1DVkxS1MfeJvqb8xAug81g9X-9TrbagD1FOMzjaxfMAk70dcG54t-hei5DNuucr0WDuGfMy3TdDRBdLU7sDJr0lYQs9r28byKCrkMoPj9Um07inM3YMZ7vtPK09Oio_mK51Hppi5kaMDXiAwGuFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اینترمیلان از جدایی یان سومر دروازه بان خود از این تیم خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97091" target="_blank">📅 11:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97086">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QjuSvJabqL4ZNGLs1-UdpnYPlYJ862OG4YNMDjGTNzPGF_e13eZ18t01ZvG_Uv7c7_fkmyut-FwSJQQQT-Wu5wQiiOHNIE2uVwZUd6SG6Vdk3ziDzuAfzOfphoxagiYPoTjsS1G878n-1TZaljSAvC5rGHXbU5ivYQaOm8VByMl3Cc59_BK2h-xtCeN9zOuFmsuDOe3ZsNGHOnPYn_l-OHqWdaGUlgT5Zdvu7L6kkl8-pi8SmICqfJNUUfwIGkh1xmBUNnq3Ub_06QOTIy0_FGh0s2PTjs2e9qP7y0KatleikfAWUN6fvHcyDbFYzX_pcpXe7Q5ZbNPwmWmGxomCHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0tpJNvJi78OP5zNQRHWGdT9HxdnROH5RY-wn5Wxn7Q0Mh-F0OjknGm1RwdQbbGS3G1O6VX8nxA9ewt6dsLK6GlNBxjeBbS-xRzLu4shr8L1SDIsZoFMom1aTX5TrYfhcuSyDoOjUZwNZ4Fv3QAfd8xdpO3dobLIYtYZLvAsGdPPpASeD32Ct4IVq2SQYRQAky8_LDUw6LWuoeYkHJ1d43aBKdEtLpq4T6-UjWZgKp9uuoIvcTTUcprVblhMWyUucJhYl1fj5pnhZIRDFjVx7ild5DOt6JLALy3NbSL_0SCJWM6jLIgNYS_oRtg3PD7-WkKMITU46xvse0h-svXJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nyd9d8x3978Oa7shNzyyHhToIDEgjJlCwq41_dKAfhk7gjyMu3DuGpP0ip6JHka1hmq2sZZWm1guPgLxsjfH1qt1Bv0ssuF5cigLvToLNRKJfVYadE8A37nhMoO6sAoSfRKM9-DBRCOVfymKBNCr-vDO-L8KDOwlyNUPhFHNdY-7AuSCxI7xGuNvJ2AMAGCfVhjF5nF6Zeyo4Q79LRw2ik1Wr2M76a9tgT2L68ytrDpGlDqt6mQJmET01CZlRx1_8_COKqz5zLyLelZbJmBvRzo11zaoVcb0LeOpqHCDL9iOzNx0x3jxRkhdAiMS3t6vq28T_DYC30T5HY7o3sx-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_B2vODfagr7_DuQ3-tlw24giusNarhGulyY3VwLJnb0VF5_Y4vjZwSGVbdeVyCFUAkQnKsBucwr_de6kwv0CuosevsWqW3DXANbrLF0QYxs2f-oW19qeYX1tj7gveWPkF2viXC1EHmPb7882iv28d71zIiJ-ryXNCI_syuAjEOaoEHYICxWOC-54rp3ZIKQS4oFPz064F_66BpzD-sKV5xqKb0dc3trzbAD0YolP78aZaK2SJBj21FsrVx1gALSTEJgC9vw6yuF2RUK-rb3c8k0wKypaFm45q3nuWUtUsi_9pXkPyQiDjpYTWZm0ERXhe9Ox4HqAg5G82aF0vt0-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3twTBG2ye8zQZOEzvvjWzbpkJuGYNF4lKUGKBkm-_1BDwBe-va8v2burVM322raJAZLd3egKsEsPupgd-En_b0G7QrBPW2lsVFBYHM5OCqtIbJBMyM0QFowvGOKn7Cca5zXMUX1F3GKrc980lBjLRWsGF99TBI1nHWpi0E3rg5BYHuR0pF6V4c5Aiudh7ej8UEa5iMxRDZcAt64wc-WbCipzob_ayRrv5mpuXh-ERvv82TxRYbRVhsmx6DzCuRql2AAIZQyCaMYCfvXSvHBqcRHRKXjpEsUcTjBU79Ux07aEc3oCz-1Fl_u_ImTNncTEjTaVPPYk0j-5Ig0z6jHgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
همسر رونالدو نازاریو در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/97086" target="_blank">📅 11:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97085">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdbeb523d8.mp4?token=I1I6XzFKRDSjf8-kcyOXHOkAatwvzrvsN8laCcpjZT2iAsjX5np5_rHhKJozu9xCtAdSa18no8pNTSR2QwknJQ6rsFrgKV-u0ChP-tzHnyqMasknO01gt2MMLvPyBhiM4ZWUk3Mji3Y6WVzHLB9TOXSZuTTvVAuevHewmGfWbL9HNJYIAHiD3ia8KROykSJ4ymyAzLkNDycQlCVZPzdEbKZIX8HGOin-q4H-v3lKAhqIOrAQD7Rgj5npu5K210HcqIXpGgpXY_BOpwNREVCNzvPYeuZ2bwYP7HIJ_m4KI2hQ5S6bSTgt42y3xK6-rNz8bidTtnkEy7UNbM2x98R4zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdbeb523d8.mp4?token=I1I6XzFKRDSjf8-kcyOXHOkAatwvzrvsN8laCcpjZT2iAsjX5np5_rHhKJozu9xCtAdSa18no8pNTSR2QwknJQ6rsFrgKV-u0ChP-tzHnyqMasknO01gt2MMLvPyBhiM4ZWUk3Mji3Y6WVzHLB9TOXSZuTTvVAuevHewmGfWbL9HNJYIAHiD3ia8KROykSJ4ymyAzLkNDycQlCVZPzdEbKZIX8HGOin-q4H-v3lKAhqIOrAQD7Rgj5npu5K210HcqIXpGgpXY_BOpwNREVCNzvPYeuZ2bwYP7HIJ_m4KI2hQ5S6bSTgt42y3xK6-rNz8bidTtnkEy7UNbM2x98R4zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
هالند تو اردوی نروژ داشت غذا می‌خورد یهو‌ تو آینه خودشو دید رید به خودش
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/97085" target="_blank">📅 11:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97084">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d2830ba3.mp4?token=g8zfCwPMtU2i9NrgNO-2b5C_D3kOG-6eAtktIpOB8NYCPNJO2TP72S9APkFrcfO2-_SX_JuYn4F933BVpZQ-MKniONfS8wVSx9Chc9PVaq5oQ2_XGoDk12gT82zDWllQbWNDsYuV1vmBzjILkCUQTXgM2v5XN5ZT_GoIP-0_3GQjuU-zK_V-cmL8emEpHQzfJROHT_BWRu5lzPuNvxd15RDV_XIR5nzYDnE4C77gik5fs8oDVL0OLXfT4w_3drWHQvn_1qLJ8KCgQR4X1hqSfnxtRAX8B4ZcnJAhUL_015YZB_TwxQI4BC8KXW2BqozZWOkUs3ZOXqK2u0u8H60muQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d2830ba3.mp4?token=g8zfCwPMtU2i9NrgNO-2b5C_D3kOG-6eAtktIpOB8NYCPNJO2TP72S9APkFrcfO2-_SX_JuYn4F933BVpZQ-MKniONfS8wVSx9Chc9PVaq5oQ2_XGoDk12gT82zDWllQbWNDsYuV1vmBzjILkCUQTXgM2v5XN5ZT_GoIP-0_3GQjuU-zK_V-cmL8emEpHQzfJROHT_BWRu5lzPuNvxd15RDV_XIR5nzYDnE4C77gik5fs8oDVL0OLXfT4w_3drWHQvn_1qLJ8KCgQR4X1hqSfnxtRAX8B4ZcnJAhUL_015YZB_TwxQI4BC8KXW2BqozZWOkUs3ZOXqK2u0u8H60muQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
🇲🇦
خوشحالی سرمربی مراکش و خانواده‌ش بعد بازی و شکست دادن هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/97084" target="_blank">📅 11:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97083">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd2ed3762.mp4?token=ikWdOlNDvJ3Vf9eNCnRRROxrqMbqX8QfbJ-BrlmTTlSEvPTBRwDyRTcLnHrwiackUlFtRGFED-0blqYRy3fzsBGRvcnRoVRoI1dc8zmYewOHTDkIwUIj9Cq5UGWmzAu0uoLasjCsDNhMeFMmJUaVbLTg2o93X8cTuzOAy_DXc-gyMf6kbKLHQc9Xm03GBGB_dpthEYd8-npjosoryaHjeymRDMNCysGtASBYcKMgPFhqlP0f7A-kgiipwYSvHMZ4xUznVsaC_dwCMA7qnxRhc_8PNkgz39YX7ELTBuVnZrajdfCOVDWFKYsM26I6X1OOJo1FrIKPCAJ2plNJkEakIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd2ed3762.mp4?token=ikWdOlNDvJ3Vf9eNCnRRROxrqMbqX8QfbJ-BrlmTTlSEvPTBRwDyRTcLnHrwiackUlFtRGFED-0blqYRy3fzsBGRvcnRoVRoI1dc8zmYewOHTDkIwUIj9Cq5UGWmzAu0uoLasjCsDNhMeFMmJUaVbLTg2o93X8cTuzOAy_DXc-gyMf6kbKLHQc9Xm03GBGB_dpthEYd8-npjosoryaHjeymRDMNCysGtASBYcKMgPFhqlP0f7A-kgiipwYSvHMZ4xUznVsaC_dwCMA7qnxRhc_8PNkgz39YX7ELTBuVnZrajdfCOVDWFKYsM26I6X1OOJo1FrIKPCAJ2plNJkEakIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇩🇪
🇵🇾
خلاصه‌بازی دیشب پاراگوئه و آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/97083" target="_blank">📅 11:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97082">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIBwfCe1e0wgqPmlHt3Es9ZjwytfSgyhPLnrCckJ6Q2_YaM7VYrt2m3410_nZLxiSz7mMyeY8--IamQy1wTP8ELlnZDGXsf7UzdyRgo8YoBxi23eYPcHxtu-RRyvVNONQPcZOcRthRAuT3R7bHQujqUVZwAzEYVArr9Q4MqDD3sU_kgMKGgl_XFMuKWEr0Fe8ovPSijcJRWBZbpt6elTsJuHP9iKHeP-UqZk7CQSixbc4xCTSeudSpTYM8_cNghqwYrjNSxqG4gZsfgRD9kZizwrOeL2u3gAiXGLMAZFtCuZo7R0Vi3OI5gcAKdcVE79pa_pgk6S9u1OWlRGR-PCKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
عملکرد تیم‌های آمریکای جنوبی در مقابل اروپا تا این لحظه در جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/97082" target="_blank">📅 11:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97081">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-text">ریا و دورویی برخی مرزها را درنوردیده و حد و مرزی نمیشناسد.
واقعا با چه رویی میخواهند در مراسم تشییع پیکر رهبر معظم انقلاب شرکت کنند و در چشم ملت بنگرند؟!
https://t.me/hashiyeh_news24</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/97081" target="_blank">📅 11:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97080">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c92c81a09.mp4?token=smzUVxDqZVXdp8Ha0ThYXQhASDlkcOl9SBDC18iiLI464g6KLG5USqzp-aTCkjBXRirxsHjZVB37gq-DYwnljt2a7PpdSaIB1B7jOYqOQJU0Ujg_JKJjJ3pwO_eCEXop-_zOVEz7hul5g-8TPM5w_Z6yAlI2WOCPaQmkHzzt56nHMuMXIsto3skegMFL6Gr94UPPDLZ1oqquPDy74fbYnoSRbzMvzB76PovlzGZG97rhJ0zffSix7ROvF1M5DJ_OdYT-BZePB2WQnXnHOfXLf1WoZiNYkjqkxBt4Hcawo5V4StazzULzd0-T7uvEly6N4s_OJec8v8-wPWeSjowojkCDlRYdJ-Nyv6sgfV0-6JrhzvHEMTid3KbZxyx_USstbD1Iajdi6Z3FhbKvLoaxHbf0ruIoqnAIxtkNjGPH3B9Vcu05yeLz8xd2fRlvwEOcB7zeDUK2ShTSp5I1BUQ1BhULp6eDDn59kqmP_aN3Sb9TMrgsg8ysaS9aVKYo0-o_ZyB_Jqs4MjF1NR_JPta28D4eH-f4_lNkzOdMTmRM8KYzpmZgX1yp8QFfCUV9B5vaFuK9aPY1xkb81xLt2jVHyql67RKL9c-UNfxDaBq1ilBk3llzy2SmUN15pkoV6Q5CBKcquqVmW3hv9xUcW_8RlZymvF1feHjBZ_TlUFLL4x4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c92c81a09.mp4?token=smzUVxDqZVXdp8Ha0ThYXQhASDlkcOl9SBDC18iiLI464g6KLG5USqzp-aTCkjBXRirxsHjZVB37gq-DYwnljt2a7PpdSaIB1B7jOYqOQJU0Ujg_JKJjJ3pwO_eCEXop-_zOVEz7hul5g-8TPM5w_Z6yAlI2WOCPaQmkHzzt56nHMuMXIsto3skegMFL6Gr94UPPDLZ1oqquPDy74fbYnoSRbzMvzB76PovlzGZG97rhJ0zffSix7ROvF1M5DJ_OdYT-BZePB2WQnXnHOfXLf1WoZiNYkjqkxBt4Hcawo5V4StazzULzd0-T7uvEly6N4s_OJec8v8-wPWeSjowojkCDlRYdJ-Nyv6sgfV0-6JrhzvHEMTid3KbZxyx_USstbD1Iajdi6Z3FhbKvLoaxHbf0ruIoqnAIxtkNjGPH3B9Vcu05yeLz8xd2fRlvwEOcB7zeDUK2ShTSp5I1BUQ1BhULp6eDDn59kqmP_aN3Sb9TMrgsg8ysaS9aVKYo0-o_ZyB_Jqs4MjF1NR_JPta28D4eH-f4_lNkzOdMTmRM8KYzpmZgX1yp8QFfCUV9B5vaFuK9aPY1xkb81xLt2jVHyql67RKL9c-UNfxDaBq1ilBk3llzy2SmUN15pkoV6Q5CBKcquqVmW3hv9xUcW_8RlZymvF1feHjBZ_TlUFLL4x4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
وقتی سجاد غریبی کسخل با ابوطالب‌حسینی فیس تو فیس میشه؛ سطح برنامه رو فقط
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/97080" target="_blank">📅 11:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97079">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5R5tY35KzobAKutazsPdBq98HkWQ61_PrB7tjyrhSPoLgg_J8eD-Fof7LzBHQdrpQn0QKkCyCIshGDeun3O67YrRqqwQnAyxYtaSTXY46r4vAE2c_ZiyMjXgZuZXsst9mvtPhqw8xnP-450f-9wlcpuEs4VGhYxwJSzUN3NB1G7PNbJIYz7Plxm6o3rXDzHceN4O-LxlKYwCc16Add0Tuy7IlebrJLa9e5KEVewy0bkY4n5QkiaoDY4q7FIAHDrgeL0Kug16Phjns8CT9trBffBKhyJ_qrbhnpugo5nSrgVxYzW909WgEksiO2Ir1yLbJdcsB5q3oY34aB7G5Sjrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
#فوووووری
#اختصاصی_فوتبال‌180
🔴
با تصمیم نهادهای امنیتی و توصیه به ارکان فدراسیون فوتبال، امیر قلعه‌نویی با توجه به فعالیت‌های اخیر در دو سه ماه گذشته، روی نیمکت تیم‌ملی برای جام ملت‌های آسیا خواهد بود و خبری از تغییر سرمربی نیست. این موضوع پس از حذف ایران از جام‌جهانی از طریق مهدی‌تاج به قلعه‌نویی اعلام شده تا خیال این سرمربی از محکم بودن جایگاهش راحت شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97079" target="_blank">📅 10:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97078">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22b45db9c9.mp4?token=vbXUzmsYmQ9pNRmortQTp-UHH9fK3TwgqeSAOODyR0_Y0EYgnI0Togc9yKISUhY6WUUBgd9HMJr__Bxgw5aYucBwUTrdjm3vFNM_t7i8MCr03Qg-e8KjD8Yl1YYyEj_PWMRgwiJFucdLI896U9ZPPw4u9x2ba7ESd4gqsmWi9f1IKlQ60h6ZbCvYE7TtZ4V2LcNCiPVf0Oq-nJ2Ptq0ossXzlQCSJ6N_6n301pN0CggakqvPjPTivKwdyHIHexIkGDQCyFc99gjZedGVtk9DpBhoWPZEdfTmVIXIg8HZkon8VhpEprEUeaEvb_q9MafLc70I9ynBqPgwv8l9yuk4Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22b45db9c9.mp4?token=vbXUzmsYmQ9pNRmortQTp-UHH9fK3TwgqeSAOODyR0_Y0EYgnI0Togc9yKISUhY6WUUBgd9HMJr__Bxgw5aYucBwUTrdjm3vFNM_t7i8MCr03Qg-e8KjD8Yl1YYyEj_PWMRgwiJFucdLI896U9ZPPw4u9x2ba7ESd4gqsmWi9f1IKlQ60h6ZbCvYE7TtZ4V2LcNCiPVf0Oq-nJ2Ptq0ossXzlQCSJ6N_6n301pN0CggakqvPjPTivKwdyHIHexIkGDQCyFc99gjZedGVtk9DpBhoWPZEdfTmVIXIg8HZkon8VhpEprEUeaEvb_q9MafLc70I9ynBqPgwv8l9yuk4Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
💥
🇧🇷
گزارش فوق‌العاده گزارشگر برزیلی روی صحنه گل مارتینلی مقابل ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97078" target="_blank">📅 10:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97077">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKZ4PTn3GDM5-Jg9VBokuaANXztFGgCuKqZAwoB7KesFKNImA05I73iGei2oPtL0VQ9wZYJmubvuhgWCL5qdHS5-DPBw1D_J2qX3cm8CgvQBGXwwv7NL45qwTqJAzIlOIiO4G8_uHsIEImP_qItfgXYPlmvvKlwvIUsZsPuKHNDd6ywQ66zvwMiOFvZPNawJFWnHCSONZBK6835HG8acbts_P8oYt_DJd6NeuV0EX-DsTnt7_prGac6LAcq3ELr7Q-Du4QKf9I3wEqz8tutq5tVVKIxHQZsRpOJsl3ORUe9XAHOCQqTSnScveOdzhZEK0afwuPrRBmz24qLF3iEpHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
📊
🇦🇷
جزئیات عملکرد لیونل‌مسی در ده بازی اخیر مسابقات جام‌جهانی قطر و ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/97077" target="_blank">📅 10:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97076">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhYRZ9OPuIFEgkGsBMph7sqQ6JLy_wXPceSFp75R6ymsNxNZpuIhrwqZFIu404vt_liqbhm1NX-fNI7OG4KTyJsBMFSxL9039mB-1DBfRHnCWBCJDLR-5D5IaTdFsWiuv8fq7F3LlgiVytCkafpHsPqFz2XGTDn_IuVxVEwOPiz_p6Qh4AVL6nI7EQSiacAACDud6RCLSkfldOXqz8Gud7r_nkU9KOzABLoTQKi8Jb8PmkroPYSFINduzrd5G5nFnWF2WBUBUQpWuv8-tZbppQLPVMQW63G-1-rPi50c7TJoH9D66Qqq5a_8j7lrz_BSHaxi-CziqW2hP3-sfV9GSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیوید اورنشتاین:
پاریسن ژرمن معتقد است بردلی بارکولا را باید با قیمتی بالاتر از 116 میلیون پوند بفروشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97076" target="_blank">📅 10:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97075">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead284c858.mp4?token=I5wya9HNcEoI5x4XUzacxT7kNIrPKKzHXi0_pnXatrCnIaf4qqbDhV5Cle43i2gaZqgMOlV4cZHgsCzu4ZFV-wKh911ovSt1Iw2DHr3yHQJ2Ty1UxLq_S9-1YGikrWSGPJbkDhW9mJrtDvYJJBoYEqUjzjLwua6IKIKJrTR23Vwzh0sufPLkM_yQ6aYr3HVipTNsWAt05ufCv9K2nJw2A4cRW96rWKxLfWTz4qKizR3cuIxKig8Rn4Nlk_dx318l71DwywBQwjJ8odoPsZL8gtm82pzca8bwTCV8jf2M111gQUJy_ZpEhNCnzEg9kdMZXZEHwu-YDoXB3CB9tpj1SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead284c858.mp4?token=I5wya9HNcEoI5x4XUzacxT7kNIrPKKzHXi0_pnXatrCnIaf4qqbDhV5Cle43i2gaZqgMOlV4cZHgsCzu4ZFV-wKh911ovSt1Iw2DHr3yHQJ2Ty1UxLq_S9-1YGikrWSGPJbkDhW9mJrtDvYJJBoYEqUjzjLwua6IKIKJrTR23Vwzh0sufPLkM_yQ6aYr3HVipTNsWAt05ufCv9K2nJw2A4cRW96rWKxLfWTz4qKizR3cuIxKig8Rn4Nlk_dx318l71DwywBQwjJ8odoPsZL8gtm82pzca8bwTCV8jf2M111gQUJy_ZpEhNCnzEg9kdMZXZEHwu-YDoXB3CB9tpj1SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
وقتی میری میوه بخری فروشنده قلعه‌نویی هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97075" target="_blank">📅 10:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97074">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‼️
▶️
🇺🇾
روایتی از مارچلو بیلسا سرمربی عجیب و خاص تیم‌ملی فوتبال اروگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/97074" target="_blank">📅 10:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97073">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77d79899dc.mp4?token=TH4G-mZrD6KlD5dQulHipu6D1UKWB3QMcYfeDCkKG907cqBJJGqh5F67-wD8OI9exeRsBlCixjpO1O6a1GA5v3v4MHYXQeGW4bzrETl5s5ftKiY7EEutyrP2Rz85_fx7V2wSbPOMeo8WaeSkSyLnhTTV4No36bOMAQ0nm-9N5-GkFHSR29Wn8kTgB6QkS7GfOzMYzoSCJm1uCTtnj4y-3AzoVDt81Mv-QXFREny-TsThvbKovJ3sRARWJ6RwR0WB6PGbHXj2qTZ1fG-yXeJVJotvr6kHPoRT4ZX7N5HVlpldvwBhJ6-3TG1jjxBrNRZ6lioI5uPTqLhVlguixdvV9zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77d79899dc.mp4?token=TH4G-mZrD6KlD5dQulHipu6D1UKWB3QMcYfeDCkKG907cqBJJGqh5F67-wD8OI9exeRsBlCixjpO1O6a1GA5v3v4MHYXQeGW4bzrETl5s5ftKiY7EEutyrP2Rz85_fx7V2wSbPOMeo8WaeSkSyLnhTTV4No36bOMAQ0nm-9N5-GkFHSR29Wn8kTgB6QkS7GfOzMYzoSCJm1uCTtnj4y-3AzoVDt81Mv-QXFREny-TsThvbKovJ3sRARWJ6RwR0WB6PGbHXj2qTZ1fG-yXeJVJotvr6kHPoRT4ZX7N5HVlpldvwBhJ6-3TG1jjxBrNRZ6lioI5uPTqLhVlguixdvV9zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عصبانیت عجیب وحید قلیچ از خداداد عزیزی؛ حسابی کلش کیریه سر صبحی
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/97073" target="_blank">📅 09:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97072">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80d90dfc72.mp4?token=A86j66xnbJSpNo-drofYXypo9b-EfyykSCTa2o6uKghn4Kk0qng7RuufAt53wKc7jv_QXVMBfNFfaWJmW-W89fa6sn6lv2N1lKG6espuaRZ7ilKWivj80JZ2XlyWdYf0mv_uBDhiyOVr_EnEk4_EOeWH_D5UodEczmEYpKK6lbwTzC12CAUvW_L8_VOiXe9K4i-59BVTYoaZoUfbYKS98mCtYM8KWED0KT0u7s5ySoDN4rfL9v37wGvRrRj24sWYjPL6x-MzOP6QJyTMuct1aEECTPRj-eF5YoKdIxqgOlAZ4czxaYepDV7fzWNAdkDf8Vs0HxmrlUMXkVtftZzbHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80d90dfc72.mp4?token=A86j66xnbJSpNo-drofYXypo9b-EfyykSCTa2o6uKghn4Kk0qng7RuufAt53wKc7jv_QXVMBfNFfaWJmW-W89fa6sn6lv2N1lKG6espuaRZ7ilKWivj80JZ2XlyWdYf0mv_uBDhiyOVr_EnEk4_EOeWH_D5UodEczmEYpKK6lbwTzC12CAUvW_L8_VOiXe9K4i-59BVTYoaZoUfbYKS98mCtYM8KWED0KT0u7s5ySoDN4rfL9v37wGvRrRj24sWYjPL6x-MzOP6QJyTMuct1aEECTPRj-eF5YoKdIxqgOlAZ4czxaYepDV7fzWNAdkDf8Vs0HxmrlUMXkVtftZzbHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
سید حمید حسینی سخنگوی اتحادیه صادرکنندگان نفت، گاز و پتروشیمی:
با توجه به شرایط فعلی، احتمال دارد مدارس و دانشگاه‌ها امسال نیز بخشی از هفته را به‌صورت مجازی برگزار شوند و فقط یک یا دو روز برای رفع اشکال و حضور دانش‌آموزان و دانشجویان به‌صورت حضوری باشد. هدف از این سیاست، کاهش ترافیک، مدیریت مصرف و کنترل شرایط موجود است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97072" target="_blank">📅 09:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97071">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b23fa1a74.mp4?token=aUgviIsBdWt2xXMaxgsUNWdfr0bx_Yi_FhT07TuaIvZFlDYYWB0VU3VAQTbqiyeATmIPnia4SyYFJ7DR6vrAI5xpQmrGeRaysWFQAOCl8YnZu8-lZUNitX0OPB0gsjjQRlIx59Sl5oC5hKY1UuLUy2Q8hc61q9rMaoFCsvhC7RBPV8IXBNpi0p1FpuWqnAgxEtQ0NtmPnkL71bq4VmEGgvRm8RwfoPDCgfpqp96x5ON42_URkeI9MxN74N4sFz2x0zveBRorNAi_AFep82UAQsxNHeyVLmHXYBQh95LVod8A7JdJ_1xILhaBJDHEXr1aQj8of3cqwVELaSktSUswFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b23fa1a74.mp4?token=aUgviIsBdWt2xXMaxgsUNWdfr0bx_Yi_FhT07TuaIvZFlDYYWB0VU3VAQTbqiyeATmIPnia4SyYFJ7DR6vrAI5xpQmrGeRaysWFQAOCl8YnZu8-lZUNitX0OPB0gsjjQRlIx59Sl5oC5hKY1UuLUy2Q8hc61q9rMaoFCsvhC7RBPV8IXBNpi0p1FpuWqnAgxEtQ0NtmPnkL71bq4VmEGgvRm8RwfoPDCgfpqp96x5ON42_URkeI9MxN74N4sFz2x0zveBRorNAi_AFep82UAQsxNHeyVLmHXYBQh95LVod8A7JdJ_1xILhaBJDHEXr1aQj8of3cqwVELaSktSUswFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🤣
وقتی زودتر از تلویزیون نوتفیکیشن گل دریافت میکنی ولی کونت میخاره نمیتونی سکوت کنی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97071" target="_blank">📅 09:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97070">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUtghhRg19OwztJmTulUyuNchQcuE0NHPE06uGHnQokpaV2nZpLucfrbumvuqHZ-qJqNr7e4rFAFa99nXQoNtakZAFQ8nr9Dn8efiLNewGZLyreCkGwUBBrA21fUwp4V1ZPXlf5ZKhZIR-h02IOzeNl7sM6Hso5P1G4fsGFfLF2cOzQyhuId6IR4lQQFbQ8DnfIRJ9WCprmIWnwuO8MFWAg1_d3-kKfYrqV8pmjFSpYy8f8Wvh0NnO9TehCjpwnqZ80mVnxDf6Z2CYpmpMU8zFLA0L4Z8hCXhlSKFtakqVoO0QnuX6PdojaBdU7d8AUlFhWFXWrOId2Q70eEiPh4ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بوسه‌نیمار و همسرش در بازی دیشب
😘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/97070" target="_blank">📅 09:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97069">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de3e24176e.mp4?token=TLicEd7Y3rqZugVeeFbgr6iNt1rNX-PFF2bogMAMB-hz3DZD1rWEm11OIjHR3GaDvJVkPWaxjHyl_taNCDESrA9PUcgtelO4aXkTmFEZ5MEvSINjTuzQ5KpeGUHN6TLpAr2ATB3xXjPQK2Y_CjdnXdfYuF1GVe-wsMe1OPYPfBz2Vjc56w1hlR9Zfk3RtE8IPhbyI05jSSNC1hZuh2gBWXxnICe0V3M12hutXQiKocpOBhBw4UlO6xDjV828qzlnDHjUcisvLha_Fhc36upjl2uEDCQ62m5Ksb78SFMDydNXrJ7317_zVsD59NtuCpvXhr_htPW83pU5qwazuUBopQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de3e24176e.mp4?token=TLicEd7Y3rqZugVeeFbgr6iNt1rNX-PFF2bogMAMB-hz3DZD1rWEm11OIjHR3GaDvJVkPWaxjHyl_taNCDESrA9PUcgtelO4aXkTmFEZ5MEvSINjTuzQ5KpeGUHN6TLpAr2ATB3xXjPQK2Y_CjdnXdfYuF1GVe-wsMe1OPYPfBz2Vjc56w1hlR9Zfk3RtE8IPhbyI05jSSNC1hZuh2gBWXxnICe0V3M12hutXQiKocpOBhBw4UlO6xDjV828qzlnDHjUcisvLha_Fhc36upjl2uEDCQ62m5Ksb78SFMDydNXrJ7317_zVsD59NtuCpvXhr_htPW83pU5qwazuUBopQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇳🇴
ماموران امنیتی فرودگاه دالاس این‌شکلی به  استقبال تیم‌ملی نروژ رفتند
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/97069" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97068">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8YJ_OQcuFRki2xiPqzyAGC3WF8MOPhhR2rxTUcOhCiJt92nM0AZepqHJQSNiUPAj4gqX6w1iSHmGX3yzCCQBYg6jYECJIUCAs8Kt1gnDxtQOLzSYKqlW8LAmRy4MBE65h65qHOldDFMjIsOgNw1qhMTC_Pcig5Iz5vqGDY242nWpip9zbCWXBI5_uvdv7CmmqiDtpuoWBnSNNNP0OYYbFqmCgffMBx6wsSnc9skJ8GtG6WG4uSUoe25VVdMJzg-BJeUSj2pCK2A39TWRxXzKQdidzP5NZ6tkAMVK9KKCvHvP58njR-h3mbcfEVY3K3EX6Q9RP3cG2R_Ac4DKrYAtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
یواخیم کلمنت، ریاضی‌دانی که سه قهرمان آخر جام جهانی رو درست پیش‌بینی کرده بود، معتقده که هلند قهرمان جام جهانی ۲۰۲۶ می‌شه
⁉️
⏮️
مدل پیش‌بینی اون همه‌چیز رو در نظر می‌گیره؛ از جمعیت و تولید ناخالص داخلی (GDP) گرفته تا رنکینگ فیفا و فرهنگ فوتبالی کشورها.…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/97068" target="_blank">📅 08:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97067">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AG28k-zRurAQdzbmE605Srknusg86CGCpqVggPV39BcpEAEeN4xuKl6XV3lJqqA4EvDPfjpBhFOm27dOC0wc3OSRzzBSXcRcuKMoxHajdUmRJPc3iNJHRwOYyG_SYkpIEPjskq87iNUK0ZSU7fK_qiw1vSmiEFz_CCXPvIJUeSgXy3rtEseXMgaTfNbIDIBR95hVQ9QXOF1hcb64WUI1-WVzMQuIHtpV_-1CEaoe-4hGWP0B_jxpgnJ74F4Cxu4KJuesapGzmL0raxUBxPhEVGyoPz1cRlO8N-xdxt5j_w5CHkHqsgJwT4qEaSZGNcUD3BUnY_o5_e0m_w-M3cwp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇲🇦
اشرف حکیمی [
🇲🇦
] :" بسیاری فکر می‌کردند که این فقط خوش‌شانس در سال ۲۰۲۲ بود ولی ما نشان دادیم که قدرت جدید  فوتبال جهان هستیم"
🤯
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/97067" target="_blank">📅 08:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97066">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTLTIUdn4evmWWjCo55t8nvN5-NEuyzOuVwq30TLGf7jWOtqUAMcWgH0CBsMQVe-G07k6ShmBasEHDDc74g7MCkwBveFJ7sPTGDGye7w7fHVu2kiDflq0qSFPKhSrQkBFF7TW1D1URF3BeCua36gnqGNJyU26XDpPtvYNDP1GNfluSYo70QMLA3hqfHERoAjbDxZelyyA0BYuGvtTSw3Nt4hsr1iXRcMO3KCe0fP1iFXLOEq6iUZ_MwPuBKsXV0XqkJO0yp4Zuks1DYcTHMtG5BljR_gW_EK3NGGWyjuC3FSV_EWI0rtDXqgY0nPJsNlcl7RdKTvRQSitEMXYK74pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇳🇱
🇲🇦
آمار بازی حذفی هلند و مراکش
🤯
🤯
از 878 تا پاس مراکش 800 تا صحیح بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/97066" target="_blank">📅 07:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97065">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCwSZKGcyMsr-klrfDvflVwZnQeCRZ4mjZaCIaMJIR72eBwjFGUu5wp1SHc3wrukckq2d3t-wdJpz1cKNWHkW92QBpq5bXoCAMcoSvzEPOnEYLp1QhsLPPUd69w-TW8bhyiMQua0pRPwfiS93TmxexUL7Lx6lPUFLytiUH4pTQGqX-4ZxUI8F91fsbzJ-3K6Jcgs5gXrayt_rQX_DBc66QwfOYIJkACn7RhGxwTW1GnAwB_IzsxZccEOGsMY057mkH4Hykx3WBXGi2nx_Oc3z1txWHULLHunExtkhGKDp-s4qlIOs4j1LnQyCX2XWCje2D1DuK4JDvD7cuSMF7GGbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
🇪🇸
🏆
بازیکنان حذف‌شده رئال‌مادرید از جام بعد نفرین‌کردن توسط ژوزه‌مورینیو
❌
🇹🇷
گولر
❌
🇺🇾
والورده
❌
🇩🇪
رودیگر
❌
🇳🇱
دومفريس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/97065" target="_blank">📅 07:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97064">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvwXEOV_U6ne0ig9bo24jRfwWRdvqSUjoZCw2hqe63KoCHWJiKDIHClbqKrwqKJbPX2kfXLBSn9IEa1uDIFWF4NsUB57dtaehGjTNSkrN1hAaBkovTDRkKEHBf9y-M4FdQMtsQSr004NIoi0qTScO9qcb66MDVMTwnnQM4wjFs3CxDqWzlgGubXa64owC7bkXwFv8GWYPgo9fm3SPfy5Xeke_XecffwDME18U7SCR_pAgPscrcEYzB67ckGy9eASTUY-v1wSylke9scu20lymrIpSUZ1dpaRBHPcw0trEWzVaHnkpK30cABemYAVdItA4ojtXSLQOPi5jx-8OTkj0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📊
تیم ملی هلند از جام جهانی ۲۰۰۶ تاکنون هیچ مسابقه‌ای را در زمان قانونی (۹۰ دقیقه) نبرده است!
• از آن زمان تاکنون ۲۳ بازی انجام داده و در زمان قانونی هیچ باختی نداشته است و یک رشته ۲۳ بازی بدون شکست را ثبت کرده است.
🇳🇱
🤯
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/97064" target="_blank">📅 07:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97063">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGzxqSm-3MHJORDFGSStvNW-SwWRxBt27WhPSw8q7wFEjU-0jGUHlp-qNzAUH6a3eDl5H98QTF8hZEMIJN7Rg5R79j3rwYTqWBb7MuSXq0HiE6bV1dob7EZNKIUd7OrbDrBXPsLFIG356FFB0xA_qrQPott3g-x3eJUwrGr4LbzoNapruWHGPicXyikPJXAkbzJ-80tF3tmMvmQZ3pjRJFMqXXBQUCBsOUcapvS78U8xMtKBb55ydIEs3iBDZv3VNC76qUv-99EXLJPszqSPlKEcb1hxgow91FYpXudz9oEqBEm0AxIomv3iw8_2Tp8QjTGT31q5AZz3jjM2dB2qqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله‌ ⅛نهایی جام‌جهانی فوتبال:
🇨🇦
کانادا
🆚
مراکش
🇲🇦
🗓
شنبه ۱۳ تیر ساعت 20:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/97063" target="_blank">📅 07:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97062">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ACEJyTq8D2fpI0dTV8BH2FNzZhjDZplNCugr1ZvawoCgiVIwLG2JPZlQnIw5cbR6o5wdidpKKl9_A6DMFt5FRzjeom6hTWB8JFHgivE0ZWWjN7lkBveCkqoKJvKv7OVt-059uldOoRf8dKvPzwu6XsIVgYMOxpW87SxXPFA_r8B5M1fsjPM9P36xLWyKrYrNi0NiEvzSTI4T3pKnykeHQHqGwR3lWa2hMtl2kaqhBlvvZJRDu6UTkW1Xhb-WEfg5akuV9hvTlsWefjim0834QyX3V-OinOHd-R6nf3MhtrpuWcKNfx8sTtgQNJi0NOZRGxdykBH8qvhMrzkND4cxjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
👀
یاسین بونو، دروازه‌بان تاریخی مراکش، اولین دروازه‌بان عرب است که در تاریخ جام جهانی به سه ضربه پنالتی پاسخ داده است
🧤
🇪🇸
در سال ۲۰۲۲ دو ضربه پنالتی مقابل اسپانیا را مهار کرد
✅
.
🧤
🇳🇱
در سال ۲۰۲۶ یک ضربه پنالتی مقابل هلند را مهار کرد
✅
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97062" target="_blank">📅 07:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97061">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOY1cC_gXaFBhXGwCL1Th4yI4Cn7uBMNZ7r9uwJQetEhP1gOviYqviCvPT7bpNC1HcKzRwhYm50JO6H2dgfJzB74-P0nTLWYZ5HNgKsZttdHkmXcGsYfczrKtFXFQDPXlfgT-ZLy49JXdtuUkUXhM6C4_Zmh46taeGAg0t0iwsRRQAMguSGvdhhGmHgzHGLZ-AS7dbsmjJgsTnk5H-5RCRurd6HU072Ic-jJUD80lS3Xb-a-3rPjZMAoROpqWiMeLvWkuX1pT_dOiIbKZKp4_9UgHTAtM3GWIY5lMqDV6TZ5pkXThI43QYXLYnyVAe8nsPKw_csvd9lHil86zjOjlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇲🇦
تیم ملی مراکش به شکست‌ناپذیری‌های متوالی خود تا ۳۳ بازی ادامه می‌دهد
✅
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97061" target="_blank">📅 07:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97060">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdWA8AAf_kb3vY9RzhlaXtKq8Vi8iQ17SLa5k6dhb6X4wWDE_QbdTLRB1bkTlCK9ZXcCG4DVu3SH8dcc339EFFbJ_rTtTbbZ38gibtK-7J13DT9rJoAi7kgPsWG0uYlzIEFIU_gYtiTlStAy3yAC90OJe2LHMCnXbt4wQccwpveRWZtiyU2LAz31t-2sH2Eq9hauC0GDXeo-t9Dg3YoY9Eo_qfgkrcxfnWClpfcrc5yeKYh5K_t45VTElfwHzDu_1eFPpy5fCZrdt8ZZ7FIZLIbegN6eFfrb2KxztOVDH8xsBBuN-Zz8Sk3aNWeSq8MczuRqLweKdRb0-0Cu4tnsjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مراکشی که تو جام جهانی 2018 از ایران شکست خورده بود تو جام‌جهانی 2022 و 2026 تونسته اسپانیا، هلند و پرتغال رو حذف کنه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97060" target="_blank">📅 07:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97059">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Os5Z_jtWMtt7TDCVeYPlhgRItwY3vo_8zbD6CZurO3fu252y2Hw1i_iXfOcBsaqU0pcd7RMrhuhIAiaQLaKCYPvNmfAEVEWYCZ4HCQFVVkWZBKSZ5YS98t_q_ikNXxY_csL6hPU1RpQ6faZ5qm5g3JzMo3__SanRpJXAiS4EchJ_E2LvME9UwDmnZdHzkimfP0d8-Y3P4W82BTDshsUWHf6itQAAAk0SVYXksDAEkTaY-NTGjDT7_vs8MvCR9pyUlvBAk1CjhZ6DKmKJUhU9jzYNoWYMOdVt9DhClqbCogTdGPgcWZKtyKUpnuYM0HgBM6tklGnvlgk4LBpQDASokg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار حذفی جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97059" target="_blank">📅 07:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97058">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/si5Vz0j3rlLa6GX9rF2gKOxjy15kmGsnrl0tfZtQ6qmrbKBQti3mNo5PYCQxPy10uQKwLc3VIpxTp8YqiFPiIJzYpuEnVVJnZPEC63YFkM9VRymhCPl6m-hwpW6rvD2MuG1heAVFbu8AzvtgzZFTnWUer2De1lGhV-YPrdKwD51iinoW9inB0Bl9fRPRJmg5tendPjXnnxm2xO1tb_u-v38SQEtMgHegWYbhqfnSrM2gTdJrroMd7TOSQNcU4DZROFksiQ7HWDWur7qnBRWGqEMcj3Tn8XnDJov-F-W8TPLPufex3fEs4NkRbFUOR5SejjAvGggL0Uiym1ZWReTrHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#رسمیییییی
؛ مراکش با حذف هلند راهی مرحله یک‌هشتم نهایی جام‌جهانی شد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/97058" target="_blank">📅 07:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97057">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گللللللللللل و تمام</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97057" target="_blank">📅 07:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97056">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مراکش بزنه تمومه</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97056" target="_blank">📅 07:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97055">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بونو اینم گرفتتتتتتت</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/97055" target="_blank">📅 07:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97054">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پنالتی پنجم هلند</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97054" target="_blank">📅 07:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97053">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">چه خبره امروز</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97053" target="_blank">📅 07:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97052">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اشرف حکیمیم خراب کرد
😐</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/97052" target="_blank">📅 07:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97051">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آقای کومان ریدی با تعویضات</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97051" target="_blank">📅 07:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97050">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">تیمبر پنالتی هلندو ریددددد</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/97050" target="_blank">📅 07:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97049">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">همه چیز مساویه</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/97049" target="_blank">📅 07:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97048">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مراکش هم گل کرد</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97048" target="_blank">📅 07:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97047">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شمس الدین پنالتی بعدیو میزنه</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97047" target="_blank">📅 07:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97046">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">هلند گللللللل</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97046" target="_blank">📅 07:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97045">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">عجب گل کصشری
😂
😂
😂</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97045" target="_blank">📅 07:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97044">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مراکش دومیو رفت که بزنه</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97044" target="_blank">📅 07:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97043">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کلایورتم تیرک زد</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97043" target="_blank">📅 07:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97042">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پشمامممم هلندم رید بعدیو</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97042" target="_blank">📅 07:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97041">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کجا زد
😂</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97041" target="_blank">📅 07:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97040">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خرابببببببب کرد</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/97040" target="_blank">📅 07:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97039">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">العیناوی برای مراکش پشت توپ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97039" target="_blank">📅 07:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97038">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
زنده از ضربات پنالتی(آپدیت خواهد شد)
◀️
🇳🇱
هلند
✔️
❌
✔️
❌
❌
◀️
🇲🇦
مراکش
❌
✔️
✔️
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97038" target="_blank">📅 07:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97037">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گللللللللل</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97037" target="_blank">📅 07:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97036">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پنالتی اولو هلند میزنه</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/97036" target="_blank">📅 07:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97035">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بریم برا پنالتیا</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97035" target="_blank">📅 07:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97034">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🏆
پایان‌بازی در وقت‌های اضافی؛ ضربات پنالتی تعیین کننده تیم صعود کننده خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97034" target="_blank">📅 07:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97033">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دقیقه 119</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/97033" target="_blank">📅 07:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97032">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اوه اوه این چی بود گلر هلند در آورد
😐
🔥</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97032" target="_blank">📅 06:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97030">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56fcfd81e7.mp4?token=Bt6e1UqAWWZjTbUjCVFNX3R7I4oD2JQGCHGCT7wEDbDvEClGvkpSQiJzjAAp0Pu0DZKJnZ8JQyYv0DZURpB9WZfFq0Kg-5IqWgJXC-l404znF1wO9wlsFP7vnJt_CoMtlXhe_jLQ-IOE8iAm7adXGKqyiHfcnH2GgIQzH6Xq_TB1rVnp_F04freo4_E8H_tYxO1N-K9NsTABOCnLA-lSM8M14FDjU57NsGx4Hlcq0_9UEO0uLgtKnbmbucv1DLw8gww0-Q6QVoRrWUQZ5NljPF1f83pcm7fU6EDUNgYnXfZVN2HshVsAt6FRf3LmZcVvoVA66PLrLbPKmrr1CXFVag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56fcfd81e7.mp4?token=Bt6e1UqAWWZjTbUjCVFNX3R7I4oD2JQGCHGCT7wEDbDvEClGvkpSQiJzjAAp0Pu0DZKJnZ8JQyYv0DZURpB9WZfFq0Kg-5IqWgJXC-l404znF1wO9wlsFP7vnJt_CoMtlXhe_jLQ-IOE8iAm7adXGKqyiHfcnH2GgIQzH6Xq_TB1rVnp_F04freo4_E8H_tYxO1N-K9NsTABOCnLA-lSM8M14FDjU57NsGx4Hlcq0_9UEO0uLgtKnbmbucv1DLw8gww0-Q6QVoRrWUQZ5NljPF1f83pcm7fU6EDUNgYnXfZVN2HshVsAt6FRf3LmZcVvoVA66PLrLbPKmrr1CXFVag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گللللللللل مساوی مراکش به هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97030" target="_blank">📅 06:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97029">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🏆
پایان بازی در وقت قانونی
🇲🇦
مراکش
😃
-
😃
هلند
🇳🇱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/97029" target="_blank">📅 06:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97028">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhy02WB2qpuMHumdheVQIppqqsn1_POT2tNqSrFGXobvIep1C3LxfaIo-ymn7cIzilxgT1mfsgK7njA0EjEvliJX8_dq0gTUioCIs8DIFwWMRQASgoFIfgCjqaLKQg9QYQGBhr78DX00Oh1YwN3Pf-Od42PcWXi8EpgkCQLr51YRvkooR0ka-2TtY8iWDTSRcJVtif6oNl8jKRd2qrIaEXHqKqhh07TxbUibYUhilm-ALGzw8LucEIwpnARAtKRkB4lE1-iomoOA3NqIW-JW3XQZrZGAxS2VmtsM17rZjeYvV4JJJiByzUlP_9wrV5Gx_I_q_eavPtBUuAtaYw981g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فن‌دایک رو خدا وکیلی
🌟
🌟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/97028" target="_blank">📅 06:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97027">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پشمام چه بازی ای
چه دقیقه ای گل زد مراکش</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/97027" target="_blank">📅 06:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97026">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دقیقه 90</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/97026" target="_blank">📅 06:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97025">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گللللللللللللللللل مساویییییی</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/97025" target="_blank">📅 06:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97023">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pObdAZIIBmCfSy8CkycwqnB-DGxrQBGpgvpKQb5RK_7DaSwXmPvuVBSbABj3zTYGxGTIF7Sfm35iWhqPhrji5Ob6STDdqqL_p61oQ9L7cnvRWaLJ2K_n5mMRzkYhtmppdHd34kk-uVIpGrhEvLn1k-ixhFuOH1KDNJL6mVeRmysK2zhxHpLQtYgcFRCEgjQy46fV3y18kwKt16Gyr1DZ41WHIf0J4GzLTY-x2MvegihV5mPNBXeXs4cyEdBGznk5YaKNpqzgXk3UZd2eKwmX9Pt8SvHUXEueOZRrnvUMazNvCa3MvZ_MC5ki5mtGvuskjmG9xt6EPLmsFE_C9vDn0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/maxdmtzsmTf7Myz5fWlvvDPjlNul9Da6rjpzHDyKu05OmVuqsmqgDlOIxRvz735qLdNKpi-lQhrz_CizI2oPFvYePbWR2279ijdmgW4kk-FL5yQTxrcC2Uw9KbDQUk9Jwj6brykQon5i48Rt_SFlTXQLNbM7rVbcjB9uNM5e4Lm7DaQywi8wO5SO-fAqd8vJ6gZKD1nL7pgl6weIensmftvqJU0bT5q5GbfMWWtnXmGXQciyiXhjfGoaAMNaFT9ySTgdFn8LMY29Q5OBog3bFKHf6B7sRFf9tGEx-B354hJa_0wseq0q2Z6g3Vuhb8kmQ_3qjhO1igV9kPW041MLfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کودی گاکپو بعد از گلزنی به مراکش به دلیل از دست دادن فرزندش نتونست جلوی اشکاشو بگیره..
♟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/97023" target="_blank">📅 06:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97022">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eec21bdcc.mp4?token=eEHfksuXsRPFtrabehTQ8g5xm4lk3iODn9jPDgX7ojBo7uyYO_JyqbxGGKF_qD7r0ubf3rZ7A_2DyPwF6oS5XIMjbHIo-JMH0228JvdvxkKxCWPqA2a4utNXZvyTg7nXiGTcbZUq0YpJDDvyAZdKCkc2LH7RwRFqHRmQAAznc87YoX8L6XFFZp5p9z-vGDmP33TmqcTNMI8ghg449GShtw-SBzDkAF2bvt1YZ4-W03uevNWnk5HvNRidVGXhoYWLgPozxy3je-Jh7hqYIl5hi-FztiQjYKir_B76JawDw8SGdIL1_jz0Y-95cwGeFEAhNY1n1Mv-lmLgEh4g47YrHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eec21bdcc.mp4?token=eEHfksuXsRPFtrabehTQ8g5xm4lk3iODn9jPDgX7ojBo7uyYO_JyqbxGGKF_qD7r0ubf3rZ7A_2DyPwF6oS5XIMjbHIo-JMH0228JvdvxkKxCWPqA2a4utNXZvyTg7nXiGTcbZUq0YpJDDvyAZdKCkc2LH7RwRFqHRmQAAznc87YoX8L6XFFZp5p9z-vGDmP33TmqcTNMI8ghg449GShtw-SBzDkAF2bvt1YZ4-W03uevNWnk5HvNRidVGXhoYWLgPozxy3je-Jh7hqYIl5hi-FztiQjYKir_B76JawDw8SGdIL1_jz0Y-95cwGeFEAhNY1n1Mv-lmLgEh4g47YrHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل هلند به مراکش توسط خاکپو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97022" target="_blank">📅 06:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97020">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خاکپو
🔥
بر خلاف جریان بازی</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/97020" target="_blank">📅 06:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97019">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هلند زدددد</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/97019" target="_blank">📅 06:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97018">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گللللللللللللللل</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/97018" target="_blank">📅 06:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97017">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee6fb4d140.mp4?token=ePc98CSPbAEB-ygI2tWJGEZOIOY3hJClJI6j3TPOc28kedFjm0UI8UQOXBA6kHc7uPpdBNilzzsBTsfVcOUKjFOKtwmtndFj7-6TFVteDY_LeCKV--iLOnUyO-0s6Oo42XNIEWSLmYgattTmtwx4B33nGMerY34cBQzs0r7EYTIkL7AlWGxXWXD8d53rl1EnS_tMoVCPqnuvjqcmXQ1Xacc9Lk_oe_HYxuZ3mmMSvbmfYVNWH-jHX-9-TCv8IxMgXPN-pHpK5q9oXuH98ziqGS-lr4GXcG_R04aDKFmizvw3jowxoKL-kS2s3ojKM5BdnnA7jG1fls58C7zQ7myKTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee6fb4d140.mp4?token=ePc98CSPbAEB-ygI2tWJGEZOIOY3hJClJI6j3TPOc28kedFjm0UI8UQOXBA6kHc7uPpdBNilzzsBTsfVcOUKjFOKtwmtndFj7-6TFVteDY_LeCKV--iLOnUyO-0s6Oo42XNIEWSLmYgattTmtwx4B33nGMerY34cBQzs0r7EYTIkL7AlWGxXWXD8d53rl1EnS_tMoVCPqnuvjqcmXQ1Xacc9Lk_oe_HYxuZ3mmMSvbmfYVNWH-jHX-9-TCv8IxMgXPN-pHpK5q9oXuH98ziqGS-lr4GXcG_R04aDKFmizvw3jowxoKL-kS2s3ojKM5BdnnA7jG1fls58C7zQ7myKTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🔺
ولی پسر عجب اندریتدیه این فن د فن دفاع هلند؛ رسما تو این بازی کون لاله‌های نارنجی رو خریده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97017" target="_blank">📅 06:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97016">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgECt16FjL8TyRhohTOk-5npjMqa292hNLusTaZ-aXqYGYe7wekwYl_gKVPA3kI4ubI4XuLK73Dw--fThOp0mssJKuKsXgY8cg0VUXD_P8qCt1FfIITojLlo_np16HFiKiiX_GOPiNwPPdwDtV_MkQb-p30h2Q5yy2LZ9XvA0wRZMC-osd5W9WfscI8LC4gO0zcW8R8h3OIAXWPTbLk03KVAtRL7sIpGGFBWGmDuu2iv-4TLM7YrLt0scxnnEwct3GUSWx23PdGeWO6UZs37S5CzZxaLhqGgLa0LmAlJiypld8ljl6DnrKQEG_Ip6FDlaeRwQBtqd9itc3hAhXFq-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
آمار دیدار‌های تیم‌های آمریکای جنوبی در برابر اروپا:
🇵🇾
پاراگوئه ۱-۰ ترکیه
🇹🇷
🇦🇷
آرژانتین ۲-۰ اتریش
🇦🇹
🇧🇷
برزیل ۳-۰ اسکاتلند
🏴󠁧󠁢󠁳󠁣󠁴󠁿
🇪🇨
اکوادور ۲-۱ آلمان
🇩🇪
🇺🇾
اروگوئه ۰-۱ اسپانیا
🇪🇸
🇨🇴
کلمبیا ۰-۰ پرتغال
🇵🇹
🇵🇾
پاراگوئه ۱(۴)-(۳)۱ آلمان
🇩🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97016" target="_blank">📅 05:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97015">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بریم برا نیمه دوم بازی</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/97015" target="_blank">📅 05:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97014">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پایان نیمه اول بازی</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/97014" target="_blank">📅 05:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97013">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🎙
یورگن کلوپ: «اگر این صحنه خطا باشه پس آرسنال هم نباید قهرمان لیگ برتر می‌شد. اونا ۶۰ درصد از گل‌هاشون رو همینجوری زدن
⁉️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/97013" target="_blank">📅 05:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97012">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQiAF_ZaJnvHXoWw9wT2jLRSKpmRiHbcwwTrkvLdR4Hpn6TM7LvK3awKOSlV9oVl-lJZbkuF9s5WdnpLRV2Rie2arQgfiC45u73mEeznLpby6YOwPGr1jJHB17j6zPAScyPtQ6Xvp9yLE5nlnh6zNuMcbeqKeyU34btpy7R85rc-vIU-7_6fjouNLA9co0YiFBuFpDgPkaOAnpMoqR50281pFh82pGYFKxAAY1kLMtDz2SI3rsLThscSSvREH7iSA0qwnRpe1qy7knTY0uRENzRw108yl-r3o4bkve_5fwbbEXhTdGhKmY5iKe7y4TKJuEWY2uWILqZwF6ivgqzdeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه چه خونریزی ای کرد سر فن هکه</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/97012" target="_blank">📅 05:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97011">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اوه اوه چه خونریزی ای کرد سر فن هکه</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/97011" target="_blank">📅 05:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97010">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCBHsfwMbXLRXiMRkwV96cDU78cJXnt9EG4QoVuSz32SUX3_4NX2Wq_YEam8KQ04jJZ0Cn6DlzTPjeNeVZw9rI6Mixoc4EWQxNZrtm73jolJbitw0M49zn59ms_vvvg40paVQBlLzH94TJkBwcfrcv-VMfolb8ZdJ5EmV5dPi4xH4xH55tQ6k-CFJ2jlCFCSHPl5l6t4shLl3Dv6aOSCGPiFwaszaxBKRgIHr9-E0IYLmDRCl1BxmMe7PrFZVok-EGxK54yNV2qYni-Mu8wzXaoRLNFaUvPtydrY7Vl9MuJewO8BYY7Ek5MfnGR---Skb4Tm62Ld_zKDxWH37AQDKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه خوشگل مونتری مکزیک در جریان بازی هلند و مراکش
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/97010" target="_blank">📅 04:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97009">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تموم شو دیگه مشتی
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/97009" target="_blank">📅 04:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97008">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کم کم بریم برا شروع بازی فوق‌العاده حساس مراکش - هلند
🔥
🔥</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/97008" target="_blank">📅 04:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97007">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqVJgua2pxF_mjNwOHpZILCuvGq1q4oQ8cCjV_zeFaZdta1j_MWqs5uyZNpxjiJDzScSZ9FSwjntuYTyBDY-VAidxleYojh2X0XZarjNnRCCGv2XsvryM69-tikHNhpW3TV0aq1MrPsKmDK0p4QyfgzbBa5mSdRpfhx8nruf_kRUM3MRAvXvvbIu1cmpAXm028CHAlil5gctuiV-FmH4_essMSvsuQSMuw4sIYfP2nQadtgFHwDm2NJVSiRgPDbiw4hRbS2Q0o48MlfNumzAU2UzH6FUxwf_b2B7WTbhRuTitMRqxE9k3yJryipmFPUxMn7wiggkW-Xuuy9rdc5_TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
مارك كوكوريا: ترجیح میدم کچل باشم تا اینکه لوگوی بارسلونا رو روی بدنم تتو کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/97007" target="_blank">📅 04:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97006">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7675e39d8c.mp4?token=e623nt8kwmKPI6aB1EYAkYGPhoqJ-T41QRi_lMlNiZ1J0wGDoPvyI6sFWJ9rr9GKAXvLW8-ioSCtTQP7s_8x62dMisHhI0ItQz2UUK7hHIsMonOWYUQksI1lsueW9-XnEp-yTqzK_Iuh6G8TMlhi-ZJn6lhw3yQKqtpwxRApUoH8ZiuTFoXO6zbLFfL2xDujvXNYYP3E1E60hRxx8LxMx8kxdsPaLFLXkQLVTbiunBTUzDTpRRiIspu-ES_2byjjDqyG6NYQjBzC5GE4McIom1ZW58_L9felAM9Q5ABZ2-E9i_0SjYV4QR6jL5fqNcPSEfjf-8Vo94yiaK0b3Efeag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7675e39d8c.mp4?token=e623nt8kwmKPI6aB1EYAkYGPhoqJ-T41QRi_lMlNiZ1J0wGDoPvyI6sFWJ9rr9GKAXvLW8-ioSCtTQP7s_8x62dMisHhI0ItQz2UUK7hHIsMonOWYUQksI1lsueW9-XnEp-yTqzK_Iuh6G8TMlhi-ZJn6lhw3yQKqtpwxRApUoH8ZiuTFoXO6zbLFfL2xDujvXNYYP3E1E60hRxx8LxMx8kxdsPaLFLXkQLVTbiunBTUzDTpRRiIspu-ES_2byjjDqyG6NYQjBzC5GE4McIom1ZW58_L9felAM9Q5ABZ2-E9i_0SjYV4QR6jL5fqNcPSEfjf-8Vo94yiaK0b3Efeag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک ماه پیش: هاورتز قهرمانی چمپیونز لیگ رو در ضربات پنالتی از دست داد
❌
امشب: هاورتز با پنالتی که از دست داد باعث حذف آلمان از جام جهانی شد
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/97006" target="_blank">📅 04:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97005">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6JJkW4wGBQdoapItUKnmQBg84La8aScA6HmCuACXKRZIE8PEuGzzQDa_W5PwpqDhJFfPJ8DAeoU3lCU19I7rfITKqRioFarKN8nEmz2_av5K_JtMtBxQFc_xUVPZ6R8Lm9CMwdXcMfHf7mECKWeuLjJJmKXQZYKazbYtW1ZGrRGtsST2iq7CXRC3i6rgMbJOdqUGXRU6MVyyOhvL3S4stOtaHxp8XRt-Y4d3sKTvQd2oeIvrI_ArtMIcAU8sf5hoflyJX22RjFyrkC9CNqyJ4g72BqXUh5BeF55pfUO5inCNkMk91WuUR_ft-xOuXqODBJJJuhSX9-yZx-RVItPvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مود ناگلزمن تو بازی امشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/97005" target="_blank">📅 04:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97004">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-pU9KvbpF8XkAzEnBgrJkByOvy7POQKUt_LwPqpR3CmchFrKP3qSr24Si32dDJJnf8j1sWIx_KhQDGUdasmgbE4gYADkm39b-wKYlQo3Sv6riiUfaGp-nn-Om0cFzxHgjpBnQLgOMFlg154YefhLg1K68ChcZSC_P_SULtgLvIaSmYLlvGFTsscLaegB4F4lrtSNqWWAzLMY6AbJgQKqlmFTN4amXqUy1ltaoIfB_qZKHLsg3kExQ7mR2uwXAJ9nl-G3HoKn80lrVPfW8y8VSjEZ10X0LO5NMv8mIfmi-vs0o9zta_gGIozB9-tSRP9kWcPBgQnZY5_ccr3veh7iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشاپیش طرفداری خودم رو از لاله‌های نارنجی اعلام میکنم
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97004" target="_blank">📅 04:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97003">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔥
🇳🇱
ارتش‌هواداران هلندی پیش از آغاز بازی حساس و دیدنی امشب مقابل مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/97003" target="_blank">📅 03:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97002">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5899cc42f3.mp4?token=N4Xkmx9ugjuMv_QP1TDGNIeS9B2p0BElpY6kEUujKJtZPqt7UpUzH65rINrUV_e9X8UlAVqkrpXvKZS0Xe4vac6l_ALeaLMTxTwAWcXwXyrV6PBJmsul1hxdfrigrX-4HrKq-0mdjsyj5pOgR4pnYNMmXe7bKDkGvvpyPdWaIZESdBqjquCg69D5C6M8LWvieZvHpzB9pg2VuWjFpgzsj7MSEp90CmBz6N8oFMc44JIl4EP8vko0sEX5EWsj6YoE_UyeG5JX_TKiOS8aTvHwpFLU6mE2i7GRH_m0kRZ9Y-83EVt5s10aWvyJebgWcoNz6Cj5oRxQbXQhK-vbEkSurQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5899cc42f3.mp4?token=N4Xkmx9ugjuMv_QP1TDGNIeS9B2p0BElpY6kEUujKJtZPqt7UpUzH65rINrUV_e9X8UlAVqkrpXvKZS0Xe4vac6l_ALeaLMTxTwAWcXwXyrV6PBJmsul1hxdfrigrX-4HrKq-0mdjsyj5pOgR4pnYNMmXe7bKDkGvvpyPdWaIZESdBqjquCg69D5C6M8LWvieZvHpzB9pg2VuWjFpgzsj7MSEp90CmBz6N8oFMc44JIl4EP8vko0sEX5EWsj6YoE_UyeG5JX_TKiOS8aTvHwpFLU6mE2i7GRH_m0kRZ9Y-83EVt5s10aWvyJebgWcoNz6Cj5oRxQbXQhK-vbEkSurQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇻🇪
👍
در‌پی زلزله وحشتناک ونزوئلا، نیمار مبلغ ۲۵۰ هزار دلار و خانواده لیونل‌مسی مبلغ ۵.۵ میلیون دلار کمک بشر دوستانه به این کشور اهدا کردند
منبع: ال‌ناسیونال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/97002" target="_blank">📅 03:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97001">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuawPOpySeb-EjNFdhZsZxQisaO1F1wO_zUCuJTGFG1P0X2gm7t3RHRNZ1Bim38CyNgInYHQdZv0SpqFlrQRAHOTyqqBuktpHZczaNY8sd0oCkl3t21vawHkuAIbSFX6BG-Kgx9kN93yDv69JZVRo9jMmr9wXBApLP63SEvepFZjVrcaNx5NtmukKi8QuYHstmexR1aSgrfcorb_afnWAd1NtypINSw975VlY5okja6grUn3QX1qUsLPkqGRnuF03Ldfa4VoV4-Ir8KyYY-OEj3EItmK6i_2qwhrRAvtelmEoIONDqqo9hh1qn1kYfF1WoMFj1JMaKk-zjpG9B9L0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
#فوووووری
و
#رسمیییییی
؛ مانوئل نویر رسما بازنشستگی خود از بازی‌های ملی‌رو اعلام کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97001" target="_blank">📅 03:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97000">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یکی بود میگفت یورو از جام جهانی بهتره
🤣
میدونید کیو میگم دیگه؟
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97000" target="_blank">📅 03:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96999">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwRahTltoMLi5KVygEnE-NNWzjWUbptuw7gKvg-yQlXx-kJ84uj4lK-f867XJyJK8vxjduVlE9XsneVYs-pu_HZKQOvYtZBlwakcaLuGi1HnqVoXsSTkljKSbvNk_V1LZwPlymkqnMZs_zRDSqiz7iBmxSEB1SQs0mUia2SCzQRwC72MfcyKv_UoDgKK_DPlVyGCW8tvvp_cbLfQPlGhFC51tN-pp4NFpOhDCfzU2gZ2jGjAvitkdZcnO9FaG_64Tksr3nE67kGoc5gfu9lSdYFwqsDoRmZF9quHM05DWKhc6XM3ez3RRJHSQRBM_EpH9uV0Ak_n58V16KlKFU_rHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنامه مسابقات مرحله‌یک‌شانزدهم
🇨🇦
کانادا
😃
-
😏
آفریقای جنوبی
🇿🇦
🇧🇷
برزیل
😀
-
😃
ژاپن
🇯🇵
🇩🇪
آلمان
😃
(
😆
)-
😃
(
😀
) پاراگوئه
🇵🇾
🇲🇦
مراکش
😃
(
😆
) -
😃
(
😀
)هلند
🇳🇱
🇳🇴
نروژ
🆚
ساحل‌عاج
🇨🇮
سه‌شنبه ۹ تیر ساعت 20:30
🇫🇷
فرانسه
🆚
سوئد
🇸🇪
چهارشنبه ۱۰ تیر ساعت 00:30
🇲🇽
مکزیک
🆚
اکوادور
🇪🇨
چهارشنبه…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/96999" target="_blank">📅 03:15 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
