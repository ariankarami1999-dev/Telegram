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
<img src="https://cdn5.telesco.pe/file/XWdUxjxwYKIg4RFVkyYlUj3sCnNrEcsn58GmpP-kbe8jqG5snBCmsJHIHLsK9c3i8c4EPYE_a_aJpwzOU-MkdAkYoxCy-jWwa98Gj62waDPXNZwUJ_xhhSlLTgSEQoIRYjfIUEvCaokvMVUZ8w83gFqgpXiBBFZ865sY88d7CA0dL9c_jctT9y0n_bHRWn4j9iruK_ib3gnZxMXYha8BNEbZacwDo1IwcS4fG20gBWo5ZFWSpYHgRzPYifEsV41R6xWKBkHmxAQ1yw8ueMQ01dQjk3N_zTiNq266KgjtFSpoAc33vHeAZeJeDG1tzv9_e7ZBIpB2VOge9spQTdXANw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 511K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 19:02:01</div>
<hr>

<div class="tg-post" id="msg-102362">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_YAfeGmFo-Ud2AAQ3fVICA7t3ZMSNxLyPDBvlWrOvZKUcukQ9KGgSWnAOv9x9tieQpf6eR41uIaAHOCzoHrFQXdK6Yh7g5WqmtmolRyIuolMQzweZX00IG28MxzFeJJLGgqADPCn83Of48-nFDlyDWwxoRlLEtT8gyceAAVcTS075cPWuULycrcYlpCJOdVoEYmw7_n251t1lEXoA8ohM1_eL7Rl9OR_BKcvXix2qUiDLwNmEoxgIDbLb7ezVHsg86fsLoRVtFTcQ5lY0haG2larEb3eB3Rczyc3L3_a94GNO6aWDJ6el8Sl_FzbQlwt_Qz3UL5kmYyFa3_XOC85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3645ae0183.mp4?token=fIxgOOl64xp-yCY0rRGnKPeCePBiL6udxAkqpk1Knqm699srdqBnRO9EzAlGeFa9rbejmRFkuqrzMfFS11yxjhrIPmgc_A97GGlG8J1Lu-N8kE_yuH7ED65NcQax3766Fz-KrqXcs-_DyazlsAS5rWY5TqDu6IdUgY9SNMHZWrKljEIqjBu80W8qKXgDMdsgXRdaFdYLsGlhBB_Fki8JY43HhPFm2Sa2145SOkTZsAG-XgB4JV_u0odCC9vjICc3Urf3pOmDa7i0BPO-epeGWODOkhePHFnOFn4rLjGi282LqGOKgyD8h-L03iSsI8loIxfFZzPI6D9-k9QWmPB-Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3645ae0183.mp4?token=fIxgOOl64xp-yCY0rRGnKPeCePBiL6udxAkqpk1Knqm699srdqBnRO9EzAlGeFa9rbejmRFkuqrzMfFS11yxjhrIPmgc_A97GGlG8J1Lu-N8kE_yuH7ED65NcQax3766Fz-KrqXcs-_DyazlsAS5rWY5TqDu6IdUgY9SNMHZWrKljEIqjBu80W8qKXgDMdsgXRdaFdYLsGlhBB_Fki8JY43HhPFm2Sa2145SOkTZsAG-XgB4JV_u0odCC9vjICc3Urf3pOmDa7i0BPO-epeGWODOkhePHFnOFn4rLjGi282LqGOKgyD8h-L03iSsI8loIxfFZzPI6D9-k9QWmPB-Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نیکی نیکول، رپر آرژانتینی و دوست‌دختر سابق لامین یامال، در مصاحبه‌ای مدعی شد که رابطه‌اش با ستاره بارسلونا فقط برای بیشتر دیده شدن بوده:
راستش باید اینو اعتراف کنم. مهم نیست وایرال بشه یا با واکنش منفی روبه‌رو بشم؛ من سال گذشته فقط با لامین وارد رابطه شدم چون می‌خواستم اسمم بیشتر دیده بشه و به کار موسیقی‌ام کمک کنه. با این حال برای اون خوشحالم و امیدوارم اینس مثل من ازش استفاده نکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 618 · <a href="https://t.me/Futball180TV/102362" target="_blank">📅 19:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102360">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Os49vwLRtkfODRLUuPaXnDiMMc4U3FR5mFfMGDbS-YI5Imo8uDO9C3AkTMxRXZ2vBUuClRZaWA6b1aqIRNtqO-jr-GvUbfRDsfct67FFUWg4Z12WvnNaSYdA16ZSo6cDRK2gSc63vyasmH7wkJF4efADRQrPVXoXdMFM5nIIc2dxTW-P9pXDmZxbsE868Lq9YwWK5xxSMAhloHxzPz8AYmgbp4tOGloCxJH73vOw0mAdk6UvIx1rZVEa5bt3XCZKtUFrpf641Jy-dWtPJYmTxRXtauXbtm6GE2MYuSPX4L_-cgaSo5zBiWYJs5iOO1yDBHpOynT34NjenMmjgVcDRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TC7Fmi9l_0VNRcm88mwN99u-NDqWmQ65vjp7t2I2xQr3tuxaMXxQEpqQsuiu1nUyJtospw94Vq6-zD3p_EEOTuDn2AzhaBpkEolDltgrsEc_wP9EMTAM4fSngvSGyxcAnShbQZjR-ZSVnryrK4MNgSGaT1G2eId2wRdhBj8nQGPfs_Rr035S6Fb0mUmxuIgVg_zyQ203wVK3H9JKg01qNVe_qshB8fJSXaZV8sT0cgNbUjaP1vijGB-N-wgeW2tnENKrZdNwEXe5X5X0TUZ_AMsYU2QnHoJRmaiGFyW4tW6oOrq2OZCrZ2UopfRTv9lvCi2Fto_xvrhtfTY0C7ZWTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇦🇷
طبق گزارش‌ها، لیساندرو مارتینز و الکسیس مک‌آلیستر بعد از پیروزی آرژانتین مقابل انگلیس در جام جهانی، برای خانه‌هایشان در انگلیس نیروی امنیتی خصوصی گرفتن. گفته میشه بعد از حواشی جشن پیروزی و نمایش یک بنر جنجالی درباره جزایر فالکلند، به خاطر بالا بودن احساسات و احتمال واکنش هواداران انگلیسی، برای چند روز مراقبت امنیتی در نظر گرفتند. البته گزارشی از حمله یا خرابکاری علیه خانه‌های آنها منتشر نشده و این فقط یک اقدام احتیاطی بوده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/102360" target="_blank">📅 18:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102358">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qioeAFGCmr43hIjwkAAYpo4e0QRN1qnr8saIZchHOG3hGf0tbanzGW6suGQF81XcfCcNMrIor9skYcy3J-dOvqiyOKf9zllt2iR_s_EIRvaJCzOfOeKT9dUK65rWUOI2mzpwez3Pox_psOyy_OYJvmf5qLOwFBKbaJNxq2TVgdU5LxeCFOh5PfMFFk_CcUCn5PByenH-y7-QkJd-Zp56CGxWhYjZXEsxuXuzHUZGydDB5yRE60lX_k0drVAbD8kU7cIRjIJ9lIArmyffaAlU0swBjIl_R3Lru68RUCzaB7kctTISS32pB63YEbppcQNMc2JLJIRCELYuU877assmqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KVOySIM7dSpifNFGY4NgutTpUsSD5f7wcSgZofOkalcdHTjzzBLOpDskAT-gBzImq6cH57H0SuBWsKG9Wk1kW0ZzCEh0LTLyccwGf_3_73tEx3BwVhO-pAAJXdAqan1oV_VBvT-fSiuT6sWv0SokUvEzlUOd_8VqpR1w70BQwTnifVmexmmJ8RZ-9xksJw5rwKNWs3aQZwgXExCEBtKizIMNn24Mv1YWd_hiWHlaWqgHfE2sxKm68J7qbd22kBX-SRpSqyDZEwCpRbUvnRem0zP62VsSZNDNcxjsyYnhEqJ8DZ7t8EBMHUPcdHvNQxNSWwRHyUb_GYd1TEXxtR8Yxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
نیکو ویلیامز و دوست‌دخترش آینهی گارسیا جدایی‌شون رو اعلام کردن. طبق ادعاهای منتشرشده، گفته میشه آینهی نیکو رو در ایبیزا و روی یک قایق در حالی دیده که مست بوده و کنار سه دختر دیگه حضور داشته. بعد از این اتفاق هم وسایلش رو جمع کرده و جزیره رو ترک کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/Futball180TV/102358" target="_blank">📅 18:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102357">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e33cfddb.mp4?token=r846RRxNOJ2n9NnaWpQd7LqS1n61mIs4SvRn4Ur9KLFcP_I3IL0AOsbZQr-dS_wRsBtl4ksJvbAD1-QblxiRvrQcKwMgEqOCSllyfVzUx2ZGh2UQuERsUWKpXghVqLrgKNL8RXP8pFJsrsx-e3SNE0g-E4QtPDRl54EhGDUhbLVf8LEPRqe5dU-aAGF95kLdYp1ePEMlxNCto2pGSZa0X-NnSmrXSXHa4KQWSGDNNMPY-t8T8z_XwOGZxAwjs1PFYVcSXqhoyw-AW2sNsZxJXmzB6MEqsz0FFG32yJZwKs3HjjUYQcpZDXe8cDBGTaQ4K4amSSChn6a3gaDLOGeMwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e33cfddb.mp4?token=r846RRxNOJ2n9NnaWpQd7LqS1n61mIs4SvRn4Ur9KLFcP_I3IL0AOsbZQr-dS_wRsBtl4ksJvbAD1-QblxiRvrQcKwMgEqOCSllyfVzUx2ZGh2UQuERsUWKpXghVqLrgKNL8RXP8pFJsrsx-e3SNE0g-E4QtPDRl54EhGDUhbLVf8LEPRqe5dU-aAGF95kLdYp1ePEMlxNCto2pGSZa0X-NnSmrXSXHa4KQWSGDNNMPY-t8T8z_XwOGZxAwjs1PFYVcSXqhoyw-AW2sNsZxJXmzB6MEqsz0FFG32yJZwKs3HjjUYQcpZDXe8cDBGTaQ4K4amSSChn6a3gaDLOGeMwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی ترامپ‌نادان با بازیکن غول‌پیگر فوتبال آمریکایی؛ بعدش که مزه میریزه از اتاقش بیرونشون میکنه
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/Futball180TV/102357" target="_blank">📅 18:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102356">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5a8032cf.mp4?token=cxc2Y7IZVKD1K96uH_t8cAjyhb7laM_kH24CuBalgVmw4US8CEb7wkjZAg1iMQ22_cU9FfseT92eGqFSiCsoC5SHaQprq_smxqtvbo99C4hccM80O5X8XLzDJoUZOtGTVXkuPvX6Ke8dstJppD7_PXl2iL763xo1q1FaisD-Qsm4dDtBCXh-a6WhOed_7QtA9jfnSlnPUttPOwfEjaRMueWrLfGCfhwfEgvHrLl0o9biw8fdvO8IGiLddDM85ISBSvXGyXd1M-l5YsHZ-3IJBXkPnUb5A3eVlxpDyPqaP4YTnnHC3NBxU25s2QmhKfqzHoOvkC9yMyGTfhcs8JxhVlERt0wexE-D7n0JTpWBATsL5uHVZu4ia6cpdAa7IJnKpGW4VdBxKm13ObM8lqV_mMfPU7ZtGZkD2h7rQ85ZTR8jey4IuSd7QgJDooUqiBAxrdOhywxrPDD76tt3r0TJBcjUmRDENO8ZAu_cH-Fav0QSMeV2u61SO8Y3lwjak2_0WjkLZpSinYxaDKmjzXEHC92NHoW8rcR2mpzz6A2qHWXwU0nHlZeHTRVqxBnsUGOsTFN6WAgiYJ5k4KIOy9YeQ2mlrWc267YsmycV4shYB8ZeDeOU5BmwFVSCwx9Vd7YuQ3ck878jccXT692AfOtXMvxvp2Q3831R4tIsKG0WeYc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5a8032cf.mp4?token=cxc2Y7IZVKD1K96uH_t8cAjyhb7laM_kH24CuBalgVmw4US8CEb7wkjZAg1iMQ22_cU9FfseT92eGqFSiCsoC5SHaQprq_smxqtvbo99C4hccM80O5X8XLzDJoUZOtGTVXkuPvX6Ke8dstJppD7_PXl2iL763xo1q1FaisD-Qsm4dDtBCXh-a6WhOed_7QtA9jfnSlnPUttPOwfEjaRMueWrLfGCfhwfEgvHrLl0o9biw8fdvO8IGiLddDM85ISBSvXGyXd1M-l5YsHZ-3IJBXkPnUb5A3eVlxpDyPqaP4YTnnHC3NBxU25s2QmhKfqzHoOvkC9yMyGTfhcs8JxhVlERt0wexE-D7n0JTpWBATsL5uHVZu4ia6cpdAa7IJnKpGW4VdBxKm13ObM8lqV_mMfPU7ZtGZkD2h7rQ85ZTR8jey4IuSd7QgJDooUqiBAxrdOhywxrPDD76tt3r0TJBcjUmRDENO8ZAu_cH-Fav0QSMeV2u61SO8Y3lwjak2_0WjkLZpSinYxaDKmjzXEHC92NHoW8rcR2mpzz6A2qHWXwU0nHlZeHTRVqxBnsUGOsTFN6WAgiYJ5k4KIOy9YeQ2mlrWc267YsmycV4shYB8ZeDeOU5BmwFVSCwx9Vd7YuQ3ck878jccXT692AfOtXMvxvp2Q3831R4tIsKG0WeYc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
یادی‌کنیم از کینگ‌کمالی از اساطیر بدنسازی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/Futball180TV/102356" target="_blank">📅 17:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102355">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a15854e8.mp4?token=LbItQK7bb4HW9rw31vp-Fo_4h_YlPPCYE2UUXUTVNLH2WAIH-5e1s1GlwTRNnIkZF-3lOe6horXImT4I_MGNyk-qHLG6i1n-skJeyLzPaZLcYkEn1_2YbodRBQB-zp5stc6WcLoSUkA3yZt98CM9FqbR4tI1zJlvX7AUZvNjW2e0IDfd5W_g5c3GznPF8FsH2K8XcnoaK0YtFx28fP3HLD5eRueNLcovI5VVrLYUiFz6tm-_PTSBYIXMXcR-E01F_S0HvHTOKM3CDPGe6R89lORZGluAG9TFG_y03ssd2r4gXjfu5xXxKll3JyvmBRqWF9Apcp_8JlF7U5cJqeVW9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a15854e8.mp4?token=LbItQK7bb4HW9rw31vp-Fo_4h_YlPPCYE2UUXUTVNLH2WAIH-5e1s1GlwTRNnIkZF-3lOe6horXImT4I_MGNyk-qHLG6i1n-skJeyLzPaZLcYkEn1_2YbodRBQB-zp5stc6WcLoSUkA3yZt98CM9FqbR4tI1zJlvX7AUZvNjW2e0IDfd5W_g5c3GznPF8FsH2K8XcnoaK0YtFx28fP3HLD5eRueNLcovI5VVrLYUiFz6tm-_PTSBYIXMXcR-E01F_S0HvHTOKM3CDPGe6R89lORZGluAG9TFG_y03ssd2r4gXjfu5xXxKll3JyvmBRqWF9Apcp_8JlF7U5cJqeVW9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
وضعیت این‌روزهای هانسی‌فلیک در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/Futball180TV/102355" target="_blank">📅 17:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102354">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=dxevt1ZukvxseBOwuYWb4jwnEwKMNDVaLrIWeCXevlvzsNCfmRfojWgYohAd-mOueDriLo8I0J9nM97Vzh30GMtDBpzzOUFloMVZFkuCiIonmstxQ9Le3dd7N57CymdgEv7wyhxW-J0vKkajv48IuCv-XSrtVf1Q9CrxOoiYf70vQc8T-il9nsI9ipsgtO9NzUGISl3jFi9MW5HiaWynWDKROSZnWgqMsJdDIcWOyF_5kJnBfp-XwdwUboOCc-xxmawlZfIgbkGmQdQHCKX_IODpXpSt467bn0-VNqfjILxQ8PpMfiDIB8xFBAzNmMDiz0Hxbt_v4jbWvUXs49wvNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=dxevt1ZukvxseBOwuYWb4jwnEwKMNDVaLrIWeCXevlvzsNCfmRfojWgYohAd-mOueDriLo8I0J9nM97Vzh30GMtDBpzzOUFloMVZFkuCiIonmstxQ9Le3dd7N57CymdgEv7wyhxW-J0vKkajv48IuCv-XSrtVf1Q9CrxOoiYf70vQc8T-il9nsI9ipsgtO9NzUGISl3jFi9MW5HiaWynWDKROSZnWgqMsJdDIcWOyF_5kJnBfp-XwdwUboOCc-xxmawlZfIgbkGmQdQHCKX_IODpXpSt467bn0-VNqfjILxQ8PpMfiDIB8xFBAzNmMDiz0Hxbt_v4jbWvUXs49wvNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
‌‌ ‌ ‌ یه ویدیوی وحشتناک ۱۰ دقیقه‌ای از
این حرومزاده منتشر شده
🔗
🔞
مشاهده ویدیوی کامل</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/Futball180TV/102354" target="_blank">📅 17:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102353">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-o5CHhYbX86xGweWLc5_XPwJLDzWf80wYqf_nDu-2wk9tzdIrdiF2Mb2IUnAfQudD6KaNsH8QQisUkmBhoqKLoLqxPmWD0Rb-Lg0sr9-bNvSQjhFKzLeUL7hmnhUsdunBpp6_l67K9Fd1pY6MOhcuofY5uf9TUkQhXwpwejVHCoKVSqWJ7LKB-DMcmqPfl5JCJQGRxvPZIpU0js7M7xhGO-szB43SEXaqWncOTqadCNr2i1v0blNzHtDY4OCbQNrsHWf19FfKwP4rXfUmM2JmrUrX6NKdaf5uneTOry7OM7NKydOpw6Dm4XTV_XJlSgAj2-1f2UOKG6wBrO4tErKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🗞
رئال مادرید، پیشنهاد رسمی ۵۱ میلیون پوند برای جذب رودری از منچسترسیتی ارائه کرده است.
❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی قصد فروش او را ندارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/102353" target="_blank">📅 16:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102352">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f25fd06c.mp4?token=q5p3FiAVMmCOzxCiwwP8Z4aTw5ouBR0IXV14IRMcN8h0gaBUfRcosZMteVBs6X50db4CeHJe8gdAbFTLeW3jTkWdXVWMY6KMG4QPxh_1tf3r-JastFqNvvjL0T15UCGGS5LOYXDsxvkZ31eINA_3iTjiMtI7JZAIW-5ATXptS2ZZU3tXLWVW9yZGKz22M4iElZdGs_L7JQgVPAJN9Aedc6-hNpB0khAKsGePIpDX3j_sfOfrqL_CH8NoNrhnnajtZAb1d2DVguEBMqbmLp8MZkZ6Xwm72Mye1js5RAUxv-Y5vz55uU4yJX7iR0oxDrj5t53DrTh7hcnQtVfwNmlQV07ztEMWgYs9LuCW-Uh_bJn_RR7TrGbuUPPQji4Ci-2QvemPrMXBN3b4m_aZjY_n-NTlGhvd_BI3_UIzLUaVpftCcwjBVW_bW4dsbUX1DEKD733autYBxbIi4PUzE-etg7ZDCuXgy3HmQM9QR3ujvt5qs-5j1gMxHRbzTvAgavbuaVEl-Stp1-jq7txPYxERbbVtyiOEgy4ctiKq5HR5GxO5UJPg-sxmAENOAydc0GtDcwMyX-Gs7m7vcaO8dEtABKFLMLvIKBmPBnQl_mShCCssG3o_nkId-JoCYKBq9d76v3LwRvHU2i97eODbl3ea_l-pepMqZ4LafdHLBbKtScc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f25fd06c.mp4?token=q5p3FiAVMmCOzxCiwwP8Z4aTw5ouBR0IXV14IRMcN8h0gaBUfRcosZMteVBs6X50db4CeHJe8gdAbFTLeW3jTkWdXVWMY6KMG4QPxh_1tf3r-JastFqNvvjL0T15UCGGS5LOYXDsxvkZ31eINA_3iTjiMtI7JZAIW-5ATXptS2ZZU3tXLWVW9yZGKz22M4iElZdGs_L7JQgVPAJN9Aedc6-hNpB0khAKsGePIpDX3j_sfOfrqL_CH8NoNrhnnajtZAb1d2DVguEBMqbmLp8MZkZ6Xwm72Mye1js5RAUxv-Y5vz55uU4yJX7iR0oxDrj5t53DrTh7hcnQtVfwNmlQV07ztEMWgYs9LuCW-Uh_bJn_RR7TrGbuUPPQji4Ci-2QvemPrMXBN3b4m_aZjY_n-NTlGhvd_BI3_UIzLUaVpftCcwjBVW_bW4dsbUX1DEKD733autYBxbIi4PUzE-etg7ZDCuXgy3HmQM9QR3ujvt5qs-5j1gMxHRbzTvAgavbuaVEl-Stp1-jq7txPYxERbbVtyiOEgy4ctiKq5HR5GxO5UJPg-sxmAENOAydc0GtDcwMyX-Gs7m7vcaO8dEtABKFLMLvIKBmPBnQl_mShCCssG3o_nkId-JoCYKBq9d76v3LwRvHU2i97eODbl3ea_l-pepMqZ4LafdHLBbKtScc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مملکت به شدت عجیب و غریبی داریم
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/102352" target="_blank">📅 16:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102351">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/138f735fee.mp4?token=YVATD0qsXa0hmheDqFYmB1fNlV8VaHW4WkHxXLBiYBO6D7EYnciE8MV56kJdo-Q5QFcf3YbYJBWnh0CxmBJihII8RwFSR1CIYqUdKE5hvbMfboCeSHR4yLXcVCISnk-iLeEcpmx-VxG8SKUnS9vPSCxWIvmqcYvya4IksLx-fjbkymYnyfdA3GiXf9eTPW2V50bqkKT2E29hVhhA3ibpDGx3NYNH86hWV44-ESD3usr0Hgr-rxm8RKEnR6Mv1xxwPNr6R_-Z5OLy1mCGSZh5bjKKSs6CWHR7FlbsR0nyWxwy_ST-RPzJnIZ-MBNVMUFQfVn6dHkLIVUiEi8asA6MoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/138f735fee.mp4?token=YVATD0qsXa0hmheDqFYmB1fNlV8VaHW4WkHxXLBiYBO6D7EYnciE8MV56kJdo-Q5QFcf3YbYJBWnh0CxmBJihII8RwFSR1CIYqUdKE5hvbMfboCeSHR4yLXcVCISnk-iLeEcpmx-VxG8SKUnS9vPSCxWIvmqcYvya4IksLx-fjbkymYnyfdA3GiXf9eTPW2V50bqkKT2E29hVhhA3ibpDGx3NYNH86hWV44-ESD3usr0Hgr-rxm8RKEnR6Mv1xxwPNr6R_-Z5OLy1mCGSZh5bjKKSs6CWHR7FlbsR0nyWxwy_ST-RPzJnIZ-MBNVMUFQfVn6dHkLIVUiEi8asA6MoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
برترین‌های تاریخ از زبان رودری ستاره اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102351" target="_blank">📅 16:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102350">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇪🇺
🇪🇸
یادی‌کنیم از آخرین قهرمانی بارسلونا در اروپا با مثلث تاریخی کاتالان‌ها در خط‌حمله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102350" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102349">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNkBcnpsFMIWA8M8sxuxU-sDFMIxL8K1pqZx-qj5wSNNIeEVG--aLzvtSbVWk3SFOHjmbF2Sm_KJP8gp0Ed0SNEtMcg3HO54Lgew67ZPfuQG_QrQQtSBu0M2kFrjtzTlY47_sxt6f9XpFQywg7Se7UfdRiFDe53S62OxL7qkg-93KCuPgFOdxVTOxDdFmas2dwpIXSAWSaXSMF09lI8xvO57yUJPyGoaAhz-ktv76xjLwozHpeqJsrIUkI80g2lbqGg_XeBj_J4wnqm0O3IXRafDchrhylvMfE59NtB2867yWC2TtiWipcvL8ARZm_6Gse2NneWymnM34WMWGNAj4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گونزالو گارسیا به فولام پیوست
۴۰ میلیون یورو
۲ میلیون بند پاداشی
۳۰٪ از فروش بعدی به رئال مادرید میرسد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102349" target="_blank">📅 15:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102348">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d88e7b9804.mp4?token=Cdv6_kGuapdAjf9Co-I74z5T5UG_9guMcBmF4Ph9bc7HCMHxtdSr2FotNaKaPuki0IVeWJekTeWKuXI7zD-dTt6toPOXL4qSMD9Z-jbIbZPfvKZUdF9Qa-A6GroW1TIPgxeOzGi0EiK1RTjEjouFTs4-DpMKjNUyA1lc5FBLataS4K2T-tycZ_VFuuggWrnmBOVm-RZHT9nOEZgpZkiLH-8k0HqEkP9NECGHmpK5yKSYJW2SPK_4ogaKDP385SCjWzAphwEwl373qkOYUmamLpxuNYqF7Q_s3LW4yYc1Tpq-XcyG-bEuDPuiq4MG4m1pCHja3s9SvmbXm8FOC-n7AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d88e7b9804.mp4?token=Cdv6_kGuapdAjf9Co-I74z5T5UG_9guMcBmF4Ph9bc7HCMHxtdSr2FotNaKaPuki0IVeWJekTeWKuXI7zD-dTt6toPOXL4qSMD9Z-jbIbZPfvKZUdF9Qa-A6GroW1TIPgxeOzGi0EiK1RTjEjouFTs4-DpMKjNUyA1lc5FBLataS4K2T-tycZ_VFuuggWrnmBOVm-RZHT9nOEZgpZkiLH-8k0HqEkP9NECGHmpK5yKSYJW2SPK_4ogaKDP385SCjWzAphwEwl373qkOYUmamLpxuNYqF7Q_s3LW4yYc1Tpq-XcyG-bEuDPuiq4MG4m1pCHja3s9SvmbXm8FOC-n7AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
💥
حالا که بحث تیم‌ملی داغ شده، این تیم‌ملی و بازیکنانش بنظر از همه سر تر بودن :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102348" target="_blank">📅 15:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102347">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0063915b2d.mp4?token=htdxodQ7Ond_EhzaDNJef6_MXNhT5Ckk-5z7lGtmuL1rSrLnHD2pnIjAw67nXPPpA0bTkQrTPDrhZEaRlmp3PK-T7MBJY59MY3tH1ef9mATYFUGuUxib3byzvFaGB5eWPL8sHAnfaDweC8tvTbz-YHf81ronh8c03iA0u5O3yXzd4M1hAf1DLm5I98d6Ub3ti7g9MoZMn-9QbgI7MFiZcgIloFiXx-gYJDMeMQPGKtMYsU7ya7n5_D5niviKbxUkHqoYNaYBImwM-6IFymXqasfyo00RxWUyUzJIaM_AY5WXL_JTd3eGevYiIL65sXvTy_boucEfobxW1XTXpCYC_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0063915b2d.mp4?token=htdxodQ7Ond_EhzaDNJef6_MXNhT5Ckk-5z7lGtmuL1rSrLnHD2pnIjAw67nXPPpA0bTkQrTPDrhZEaRlmp3PK-T7MBJY59MY3tH1ef9mATYFUGuUxib3byzvFaGB5eWPL8sHAnfaDweC8tvTbz-YHf81ronh8c03iA0u5O3yXzd4M1hAf1DLm5I98d6Ub3ti7g9MoZMn-9QbgI7MFiZcgIloFiXx-gYJDMeMQPGKtMYsU7ya7n5_D5niviKbxUkHqoYNaYBImwM-6IFymXqasfyo00RxWUyUzJIaM_AY5WXL_JTd3eGevYiIL65sXvTy_boucEfobxW1XTXpCYC_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره‌بامزه از زبان فیروز کریمی
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/102347" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102346">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2314f18179.mp4?token=Y0l1LHU_5B-KrqgK-krqoohGFbjINvSw9c1PW7LXoLfZNv_ahe0gdQIhBOrBbldMXxmXngQ_fje7xb1NATKhLe8HgeM4vO2PeknmFI-NShqj2Kz8-s30ftZa8-2QMwFb80raV2bgXmmp1g6gFlSl_kqN5v9otrs6ZJv4D0cBNwZQYKVavrG9cLnGFuNDLusz_o-Cf4jXwAmbOJeQLmnq5X3f9cyYcapvqC93wkZ-VLjrIF6WWedRc9YbiaQFvmed2O8sydZHmm1G2ue1iTCFb2aROwLGBNUbM8N98KY94_J047_08ByGPUu2AtIOdzZJUA2FC7d-J16LcS7OvfQkdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2314f18179.mp4?token=Y0l1LHU_5B-KrqgK-krqoohGFbjINvSw9c1PW7LXoLfZNv_ahe0gdQIhBOrBbldMXxmXngQ_fje7xb1NATKhLe8HgeM4vO2PeknmFI-NShqj2Kz8-s30ftZa8-2QMwFb80raV2bgXmmp1g6gFlSl_kqN5v9otrs6ZJv4D0cBNwZQYKVavrG9cLnGFuNDLusz_o-Cf4jXwAmbOJeQLmnq5X3f9cyYcapvqC93wkZ-VLjrIF6WWedRc9YbiaQFvmed2O8sydZHmm1G2ue1iTCFb2aROwLGBNUbM8N98KY94_J047_08ByGPUu2AtIOdzZJUA2FC7d-J16LcS7OvfQkdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
تمرینات پیش‌فصل بادیگارد لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/102346" target="_blank">📅 15:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102345">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇪🇸
🔥
۵ گل زیبا در تاریخ باشگاه بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/102345" target="_blank">📅 14:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102344">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e80cceff6.mp4?token=VXdTNGR-QbuOIeXwd_XjfpTSNSFtTzBN-ardi1DLLY_TeTa4a4b2kDcEPt15dzm4bb0ARvfMAiye4ygHtFUpnXkARCyunlCcSf0k84uEuXqPY3eZbdbHrC-CI6mGacZ5IJAXLWUCCXlZI73J55P1oyvzSdErry-ProPNou5D9BnKt3E5m0mIw4ycsGR57d70vPnp18hKO4WGeqQXf0cojas1iPmFJWk9jvcHdtGcK-VL2pJyY-tB4dxmnv92VAKeDlmAPvi8ALY0l92ZuU5yYfL02cXq88DddENSQakNvj2vlYZIqPqsCclEjgH_6QDoFiCEHiPjcPk8yartDcFueW8-vG9kPhogkeElvU-wQp0kbmYdiNYthPwYxFp1gq9NhNbQ-OvxRdAOgUMvnvWvDsL2WHOglmi-br-HTixXxvF4NMqEQU5Xbc17fA58mcsv7KKm75oL7DCwt-9CH-SXimip94koWIWlHe95tREPqbYO4IAzMbbEEsYP_GwLNUSAOop_wPv6v_6PFLLuVUPxG5wTIIz6vLwRFKERT32Y-JTTexQiZP5Rm1xmtnXvTT77CHiAI9FdAXGEL38E18uGB4Y5UGOfuYevmUqMBLi0JA_XsFSKfoLsGasHgQU-TGXHPKiZeoYiBHuMnRdrm9X6iAW2yomG7NOSG_KAVI0JNPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e80cceff6.mp4?token=VXdTNGR-QbuOIeXwd_XjfpTSNSFtTzBN-ardi1DLLY_TeTa4a4b2kDcEPt15dzm4bb0ARvfMAiye4ygHtFUpnXkARCyunlCcSf0k84uEuXqPY3eZbdbHrC-CI6mGacZ5IJAXLWUCCXlZI73J55P1oyvzSdErry-ProPNou5D9BnKt3E5m0mIw4ycsGR57d70vPnp18hKO4WGeqQXf0cojas1iPmFJWk9jvcHdtGcK-VL2pJyY-tB4dxmnv92VAKeDlmAPvi8ALY0l92ZuU5yYfL02cXq88DddENSQakNvj2vlYZIqPqsCclEjgH_6QDoFiCEHiPjcPk8yartDcFueW8-vG9kPhogkeElvU-wQp0kbmYdiNYthPwYxFp1gq9NhNbQ-OvxRdAOgUMvnvWvDsL2WHOglmi-br-HTixXxvF4NMqEQU5Xbc17fA58mcsv7KKm75oL7DCwt-9CH-SXimip94koWIWlHe95tREPqbYO4IAzMbbEEsYP_GwLNUSAOop_wPv6v_6PFLLuVUPxG5wTIIz6vLwRFKERT32Y-JTTexQiZP5Rm1xmtnXvTT77CHiAI9FdAXGEL38E18uGB4Y5UGOfuYevmUqMBLi0JA_XsFSKfoLsGasHgQU-TGXHPKiZeoYiBHuMnRdrm9X6iAW2yomG7NOSG_KAVI0JNPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فرشاد محمدی‌مرام درتست گزارشگری سال ۱۳۹۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102344" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102343">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufPyxDRehTWkskIZi-vuvgp_uVzAK04wEKPnR2E_L1GsjmXvLly894zm22CLFJkCcIgCjrTaZ-EIF-vaEFi_Y6QWS_QcRFthw7nVc4dYYpaorBIHYDs-7X3jbv7lLpp-o5VPvN98WDcgIlAwnDJHdtDEK6DmzB0LRZxiEjR7QE3MQ9uyxpTWnfYXRz7H5FvzDrhRJbS1FBV3rIebEpGGcQTZL_tuXaQPM0MDprDYV2WW7EM8YEisb8f5gvtnPICc2lTp7tG6O_5mpCk-jLy6eJLPrtIhz9nwTe2plYGlfN5IFLaL8teoPZnyxMBPhhixTSHZ_iERR2UXDNq8TCXDTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔹
رسمی؛ نیو راموس مصدوم شد و حدودا یه ماه و نیم از میادین دوره‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102343" target="_blank">📅 14:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102342">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3336c43202.mp4?token=tedZgQiw5LaANkpOd3dMX2fDv2seWXHOZMq_Uf6-K82M1NeIKXdjXlSxsEmBOCY-V89okzBLgNrHJlKyIs_zz4MRNaBiLMKpP7WEf0jVlmtNeyb1dRSh7CoDeAmRHW-ZNVoWAvMXp-79LXHvNLdO_fptQrvjy2e0lMWevolWFKSqQTdRSI31sHK8hpLb33qfC61U-wEC-gRJ5vrtACJQCD0_aMt-WWZiqPOnThMV4HNDSbCNJaHSfN5oO-tE5HzYtFGioMRb2Yby_6vaf62phGe0TChjH0OzE8Wbg9eig9RfgKsKriSibo94B2h_PKduisdoUPQh95E4knheMZV-uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3336c43202.mp4?token=tedZgQiw5LaANkpOd3dMX2fDv2seWXHOZMq_Uf6-K82M1NeIKXdjXlSxsEmBOCY-V89okzBLgNrHJlKyIs_zz4MRNaBiLMKpP7WEf0jVlmtNeyb1dRSh7CoDeAmRHW-ZNVoWAvMXp-79LXHvNLdO_fptQrvjy2e0lMWevolWFKSqQTdRSI31sHK8hpLb33qfC61U-wEC-gRJ5vrtACJQCD0_aMt-WWZiqPOnThMV4HNDSbCNJaHSfN5oO-tE5HzYtFGioMRb2Yby_6vaf62phGe0TChjH0OzE8Wbg9eig9RfgKsKriSibo94B2h_PKduisdoUPQh95E4knheMZV-uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
رتبه بندی سوپر گل های فرناندو تورس ستاره سابق باشگاه لیورپول و تیم ملی اسپانیا، توسط خودش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102342" target="_blank">📅 14:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102341">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyKRIwdr2sShXhBdRDTwUtEig1VQ-vzN73ARztTpI7g7Rv3o_nTiMuSF-RTCmnSKqmi88yev-NQ_VtgSTHL15grsrzvqXCsJNmiGbUGFaVOg2CcnRxlDgM5PMUZ80y7ufSblaYBujeV1dfsyF2kYtKIxUZkACI29TpSZPFHjOjKorWKkrf3l55cKUyfcq5tgJaHSJXVYp5nVe9Zo1Xu3BA9z7iGHFAeA2zsTXDY3x24pIzqz2LnV4U5AyfA-zaMC2maJ36gY05LbCutwtw52Kp9b9-gvilNIV7vbFVCfEEkcGIlUPSeLRzir07RlQmqkdQOec6QnAhO4sD2qzhZVGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از کوپه: رئال‌مادرید و فولام بر سر انتقال گونزالو گارسیا به مبلغ ۷۰ میلیون یورو به توافق نهایی دست‌یافتند تا این بازیکن شاگرد آربلوآ شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102341" target="_blank">📅 13:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102336">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-qqbeyNqxg_HIIYyvcpzlL0_n1QRp4Iom2arBvqgTgwnNkk8gIsapvq-FOAHrDV0I4rxcqfuVaH34kF-6XNijyhJuZ4MCnkG4KklV0_M_HtkmqNxxTWJOf61ym_Dbn99NH3588PrtZHUmJ0wTk8NY_POzYr4dcGnHAYviSEVn_zXXMP0V4b4GVNa48KJRrhkhVZ0YF0kzjva0bpmWgwQY6ekZebHI7NPema7PrPaoh55QzSfm-nDhbCHgs7CxYq6ILtnB3xLPPTbvVNGsjTObJP1AVjgEBbnQPhDirVqo0nTge5H_njcLO7fzzExgx39LDi6Ux4vchVD17NMYXHAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dppjneVktDDpR2cyxdSJAFFkrzOekl0N-xq4izvS6FF9Ig0RNCIeE_D-CoTNjtIpIkn5PmV95qv3u87ziLuJ9g2JsxGfsbxUk9HDgTOkPsrU1C6YfYpgESShapqz3FM2wLu5BcOOkh6CzkzYSs84d_Ykp4huctvtLGXAaoKj6hfoHYT5h1QRbgL33LQ1L9HAAyw2m5rtbeFvnSSZ2LMktSO2PlOI7N4z91qaJ1FS1oJ_5etCkOtwLshIR7vD9jibiE9qeGsrfiz8oznGu_NFSRpHBAKk-tRePaup498Mc3iUBEOPeNhzOag9jF5niOTm0D19UeqEs4IuD102VGtrSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4XcB-5eGsEJrW23Zvi22eQ_cp66mWxIuxPoxRkv9e-3d8DPWfCZRXSUgIkW86dN44ZhF_shxMzlNaU3voyh8o7x32Z_tsOrP1wk9Qem5C-ZgsR9vNVoKy5ZroBrxGLycZra8OyUJhPUTctbx_q3xUJdSsA40BOSfgwEfDhVIXgUqYQQyRKA7key6BihngzTaEn9XfebcG9SlTkvNEXnEVhsb02ObK3x9cOInlAvEoPpLXKcJhGnuMkTVkMKgN6HmgXpnBVNCFmkRQ3rqfAR71pL-Bii6vK4-gytX9yu57bSw-1Sk95mjsHerQwdaQhBFJXYh26rQv1Xx69Ui4SVkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nrtKuxGYc_m7Z4xEmisPLY-dFWsHjhPkSZ5zOJBgkafv3BbHAbD1_GZfTsVroPmGyMxGFHA1-Ok23mAF59vKHRFXm-OJjMFUQnFfBFsfJPkKrA3I2DYSf-TMeNLyyH6YXcYEoMP6Xg1w9ct5ViNQOALRHFFcyFpdxR-xCXHwoIok-clEWXEGLo4oQeQQRJcp-IR8L7jdUJlEOL6TD-zpEPKPBLikfKNbdJrFuH_cWxYTWOHSRsNgmVrlhmdC_MMG1qCqLvuoAUJAhr1y22Xam1SLphqthWN81ikbVvuA4wBxqg8FpAhfUXM0UOopHPer3T5JRdhIo9HhvTfy-QWOAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CjK3baZWCnURaRnm-1HDGWhkptyamps7k-evjrBPQgHduqjmbgHB1Szgd5Nl8msEh-tzfYxCtS2q8EvvXSAbBpYVnoQFFCq_fNFUfIQmOLx0De6_wqO2TtaZNyb6l6GzVwTR5nfhAVnwWJxxYNz7nc9YoSMAa0V4M6S2zb9mTTFoBnhdkHcjJ_GnI8sNosIuTahlGKzhlgOu8iNebFzmyjpd2wm4eH66uYLu7Yi1reUhLEvyBlAXkUf6F6-VFEbK0gGuwXILEN98JzdYOaWFRf1Bz943NIWis4l7dx78WJDUQEykjsA7mqVxU55iHSDvO47lFEpxae8DSGnKW9YC8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">+ قدرت تورم :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102336" target="_blank">📅 13:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102335">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efgdUFLb99sJDYMT-ESXqw4MRH6PDfJeZeYhQ90rQuURg-U9F43XQc3edOvVpH5Euwp-27kgWVjQIe3S2YjASIFcHO7ObR1d_hsGMd2vcpCfz5GlRrSSPpCwldT1AofRZeOVCW80MWVMUAj1G9fBshGG5Ltq1LzZrgdWZovjqb1qF8BqYVI0BO5MjJuw1NMPDHBeLjb2RDi6z4culoxJXXmA-uS2_D0TEK2yxveMYV2008y5OtxyxU_VEly0Mw_9dTfM5p-3-KIN3rvd2TFAETMnXppStjuHVPF8m7gHq8zWQIWczgw5LpT-gYz1x5J0J8HBPGR9pjCjkqIi0Mbehw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
💙
#رسمیییییی
؛ روزبه چشمی قراردادش را برای یک فصل دیگر با استقلال تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102335" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102334">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYYg47D9f_gWTOscWY922tkYnOoEiuoqY-ld3mJIUFytfsTx53J3FgAanX8rfKsi5JxcKbZWOZ2bbPkhwC6LpaiKFl-A89davgrdzrY_jFZDT2JTBMJ7YvGvVhEWw9FrbkNIlx8_zOsB0VfrIz7ERv6Qq95dgqWvA6KgVjqaG0cyqGSe68AG-F4tey57EmWcz6AtqRkOJJTGsf1WCClenn3pcUSB7aNuwdlSc0oBIK-HJStdoyuOY5dN2WmI2vL5wVZ4PvbEnqKNs2cqc1VkL46ZN83guhd2Igilsd3TMeIgAstN-w-kGauyaDmrdPPaaN5IDslAAbVozbJffzP9gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
⭐
فوری از فابریزیو رومانو:
⚽️
ماکسین لاکرو از کریستال پالاس به چلسی پیوست. 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/102334" target="_blank">📅 13:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102331">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dW8CLmSKKrU2PzwE1vr7WY7vGT_tscPxVb2xtDGnva_x9sgHPCY7VhARio_EZ7crgvDjTwe4kkX1p2v4R2q3bVpRG0YlcCBg7D9fj1azETpEle-iXscFS9EuA-9lVJX_Emes_l-CBTyiIJfDudS_D1Z8Tjk-tcR26jmEsdirL9BLeFXOJexRmLH-iK9bRqFrMnk3rfz0u9drefLdQngGk2as50oGg6T6mTGDi1C0gdyE-tfFTcrWP9_7JznISp4n11Rpoa2iRA1rUbHrrL4thfug-T_Mbq5kYVyGvQ4MIryN4gLsw7EPtVhcioqSZjldPY3FAUHNrw-XydTFqfUd2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VDccYwmzMB_hdgdtGkUYJmXUY4zvL1p_x6P25bz1wsBgq97zHRMbuRwxJMC3fboVEHyoT4q68UwEK_rgkGRGcxLAlgZM1k2S94Onho5k2HFdB4dLcJaOX8rctxZUj0Kx6zUlBxNZi3-YJ44oOPwKjTEE6_ClmhwathlFwCfD-N-S1TOhdjIZs1UZ6dZLde_iszvo4q2AKwnR2gP5Gpim7qG3h0cJOlRhDdIgvQ_z6fGVffxi64tsRN0v4dLlza1JPB4g8iT60Zv-dYUi5e-ijgHNxoeAlq9FhWF6bg3oPCEy5LzIwQYQ-1aT1IDPWaSUrWO_jjiFhquoJhj26f-0_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uO9wWl8mU180nOAQQDqmJiuwg8shpKpq8dVV2RPW_Z_2E2-DUEzxf0on-FdUKZ4Ba4_pW2Y1W6BHM8jVgPs5pV0fc0lcJaz4It9TQRHCbDP9tdQEYNZCAYjkaWPkoByO-6Dj-kcfxSOsjWhExZ-HI6JwVk4_M_pebP9hFH56RKL4xfzYJRE_gIbN6zD2l3JuzGdomj5O-Uf9VpCBHFRArjNuzaEIw1OtkxdDI2ANKU1CAFagbt4xrP4vZ2WgZ775H6CbQwTGzS2qs0Wc-S0bkJW7i3ashfr6IMysJq-XhBOwWX8JAyE_ScKYq68elv-C7aWbCZbdKqIojYc6HXA2jQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🗓
🔹
اعلام برنامه مسابقات سه هفته ابتدایی پریمیر لیگ ایران
⚪️
هفته‌اول لیگ‌برتر
🔵
استقلال - مس‌شهربابک جمعه ۲۳ مرداد
🔴
شمس‌آذر - پرسپولیس شنبه ۲۴ مرداد
⚪️
هفته‌دوم لیگ‌برتر
🔵
استقلال - نساجی سه‌شنبه ۲۷ مرداد
🔴
پرسپولیس - اس‌خوزستان چهارشنبه ۲۸ مرداد
⚪️
هفته‌سوم لیگ‌برتر
🔵
استقلال - سپاهان یکشنبه ۱ شهریور
🔴
پرسپولیس - تراکتور دوشنبه ۲ شهریور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102331" target="_blank">📅 13:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102330">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAEn909jin1xduxJ_8gLY_Z5cP6ez5UZTiIpxBMsp7V69bKmVj1cFmoZfhelBFg2Zx41ScWxGgGIF1TMFStq76MB3a_pBwy_zXX1CM0wJT6ap8nR6h10H4ro5cpwEZuVf5tSx9IOVYLPrOXutJgJDGnaUwPdmylKY3ri9USZWleEk3YGa69ogyaBCsPwKFxr0sthuQvtv4h3orGDFDx6jXpW51HlyIGf5efi0IXm87jkdtAVGtXRLWFh1NttT1ZflHOHXt7h-Iev6TuquZMEdkX_67A0QbsgjCjynJzDXpThzFCn-pNkX9sSd-tqQbwKqJIRmJbfJDFgOvawe-Dqzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از کوپه: رئال‌مادرید و فولام بر سر انتقال گونزالو گارسیا به مبلغ ۷۰ میلیون یورو به توافق نهایی دست‌یافتند تا این بازیکن شاگرد آربلوآ شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102330" target="_blank">📅 13:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102329">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AO9rfLsecNDs1bF2pI9YNg3DjGyWdfodgK4EMJrjZOt1X1AHva2fmVZxfoXonNLxRG5JsgoxpvQ_vZw7twtVr_5LHviAWZiINEh4NlxgJYOM91FtJNnJz0r18Lu0Ho0zI3bZ6q8K5rsXdN1GjfuWfG4nv7lNaI1wwnmFWZYpS-o_kLEwxsWr_PEWXtWjrYZteoElQD5ZwMATGEVaHTs41YpeaQZrs4g1DdL6eAYOYWLYz7mtK2ncdB8v7eS7XZwra27MkoZoKuRAabMOTOr02Om2PLXJpTRgiI05aI7nuOSBLjWWxwZMW6rwXd4uZeaS97xxuHTOcFE_3TKGAaUFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
✅
توییت مجتبی پوربخش مجری سابق صداوسیما علیه عادل فردوسی‌پور.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102329" target="_blank">📅 13:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102328">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee8b739e27.mp4?token=FcdU_PPMQEug4FGYwnUu61LGtKG-0n86drr9wnmeHKBFeeQQPJ5vGpDqzK_gPz0SCL9lik8J7BDnb4u0Tfpe1HDGbalaAB-V6Lj9F_aEr16hcNzmr8HbOqKJFpKm7IcO7GA6PknOqPNBWmqnKgIy42-hz78uOgLOm4s52-zGQe4cjWaRe4WQ_vgY3L6VH0dbbSaflTqvEg4veUbvBQvaZZKlQAB8olpvXL0ey6e89fpkn7uF8bXHw9wNktmW62xzIkjeJaxvxXmfJbf3wRFN0Qbp2XVag3GZJ3JSXQZ_VD4U2Ox49lGU9lP0C7Rzl3Q3Tk3CryJ21BzGvOG0qPgjVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee8b739e27.mp4?token=FcdU_PPMQEug4FGYwnUu61LGtKG-0n86drr9wnmeHKBFeeQQPJ5vGpDqzK_gPz0SCL9lik8J7BDnb4u0Tfpe1HDGbalaAB-V6Lj9F_aEr16hcNzmr8HbOqKJFpKm7IcO7GA6PknOqPNBWmqnKgIy42-hz78uOgLOm4s52-zGQe4cjWaRe4WQ_vgY3L6VH0dbbSaflTqvEg4veUbvBQvaZZKlQAB8olpvXL0ey6e89fpkn7uF8bXHw9wNktmW62xzIkjeJaxvxXmfJbf3wRFN0Qbp2XVag3GZJ3JSXQZ_VD4U2Ox49lGU9lP0C7Rzl3Q3Tk3CryJ21BzGvOG0qPgjVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
روزی که مسی به برونو فرناندز درس فوتبال داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102328" target="_blank">📅 13:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102327">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRZodgNJULNP-7Qdfjgzz9-2eiZqO4p6x3H8KIu1xiwOjjBXMobLeqhSh23E6t7sF8zudf4zm1vYgd--raDTA5M4Rhozdn1OatCwIQdkE04KPMDmoUwvttsYHZOU3wNzFQeGpUE3ceK1PzVXv-mCaVpHgsIj1PkkLzFiq8sfqU4uHYIkeent6_S2z8ELLoMF02uNBRPnu7Sq9n7N2oUbnnkxUOjNl3y5fhBuTjKugAt8uV-_SFpMkABvCOrXYXr9SbqnZu4SphXO_TLtIlHlS3hOs8EtfSXVwrFwiYsSfoZ5SM9s6wExgOlF6JNPryJAXn1-s3qxB_ZPHdizcyBHYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🟢
صندوق سرمایه‌گذاری عربستان سعودی ضمن تقدیر از یاسیله پس از کسب دو عنوان قهرمانی متوالی در آسیا برای الاهلی، با جدایی این سرمربی به مقصد نیوکاسل موافقت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102327" target="_blank">📅 12:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102326">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa8a1ce74f.mp4?token=G-73f51DmccXCW77AUTfXo8pQDDNZuz3xJ32oRpcvlb_Kdy3H76241yApZLINwe08GC7r9oUES6wsLOGIXEBtRqwB7A0vPS5HWB2kiMigEvzdJaRWkuT79p8mSdaP51uoCG2M33gzW1ZYZSmnetZ1BAv6Clkd9YuXoPfhh6PrhM0A1-GZfa0APVlokt9uwMIi92OINVr-31YyramgQxdIC2bqox346Wy-sWAbvIRDE5JI20_avYcEz0ceo68j2T_X4oqq7NmzdYnpYttCI5AVgF2k2HmE4qrL96dhxKPHtJNS4eqM3Ffphp2cUnqRCr5G-vc3L5OLG4ezAPykxoVWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa8a1ce74f.mp4?token=G-73f51DmccXCW77AUTfXo8pQDDNZuz3xJ32oRpcvlb_Kdy3H76241yApZLINwe08GC7r9oUES6wsLOGIXEBtRqwB7A0vPS5HWB2kiMigEvzdJaRWkuT79p8mSdaP51uoCG2M33gzW1ZYZSmnetZ1BAv6Clkd9YuXoPfhh6PrhM0A1-GZfa0APVlokt9uwMIi92OINVr-31YyramgQxdIC2bqox346Wy-sWAbvIRDE5JI20_avYcEz0ceo68j2T_X4oqq7NmzdYnpYttCI5AVgF2k2HmE4qrL96dhxKPHtJNS4eqM3Ffphp2cUnqRCr5G-vc3L5OLG4ezAPykxoVWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
یه فلش بک بزنیم به زمانیکه داور زن بازی رو متوقف کرد تا به کاکا کارت زرد بده و باهاش سلفی بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102326" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102325">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49420aa7fc.mp4?token=D5c7yeXENS-SGTrkdmU5oabRcoCKUtjRvyjixnbBW1KIBy9Edex01q1gSyBNiwvafL68H1Nmov95JjnR1DzhVU3VLdxuebJ-bZ8Gj46JA_3DJOlAr4IhGTjtR_JF-twyQ2GH3Owv3M24AtH-CkzuYrQ3RodHRehwXSyv6BYuiiesfs8msiRZUeXWtLwD6FA5rGSXLbxOyYgOI4F3FQtP9woxLkaxxG-JgZ5hgakZxUJru9s75YHuQngjMs9GkETN9FrhDygOsBvgN2qGUShoQX72d1AkslYHhVGciU9Y0-ShLSdeticG-q3kIc8_LkvECRDhlgWCHHD-7CGZaNvmxIHVziSre9dX6Jqy-rTMVbYndZeCCu45ITtj6lTgAbmM-tAqwJpGquEZfYtYDgIBnQPtCZfvlCyLipEYvFIeEXZARuJAi7FpNdA1rtPzzf6uAWr1RK-ca60INU5n4ATbeI6OcOxQlWg2Ya-HvKKRoZ2fXOKMpGDw-ccwVPoH7VT0jrBtrGrL489-r2o0mQ4IouS8YYbT2ih4srJbKMokvZI2fxQykrs63-1ULiT5IR2PPkb-QXA5m__BZNpRDliyrD5_dkEQ5OL3hLtFqBsKVyJtScayPGLYX7ra5t0QLB2gl8HfXUAX_cePFEEATLEGkJn2mzCSiE5cOwm8XuvRrfk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49420aa7fc.mp4?token=D5c7yeXENS-SGTrkdmU5oabRcoCKUtjRvyjixnbBW1KIBy9Edex01q1gSyBNiwvafL68H1Nmov95JjnR1DzhVU3VLdxuebJ-bZ8Gj46JA_3DJOlAr4IhGTjtR_JF-twyQ2GH3Owv3M24AtH-CkzuYrQ3RodHRehwXSyv6BYuiiesfs8msiRZUeXWtLwD6FA5rGSXLbxOyYgOI4F3FQtP9woxLkaxxG-JgZ5hgakZxUJru9s75YHuQngjMs9GkETN9FrhDygOsBvgN2qGUShoQX72d1AkslYHhVGciU9Y0-ShLSdeticG-q3kIc8_LkvECRDhlgWCHHD-7CGZaNvmxIHVziSre9dX6Jqy-rTMVbYndZeCCu45ITtj6lTgAbmM-tAqwJpGquEZfYtYDgIBnQPtCZfvlCyLipEYvFIeEXZARuJAi7FpNdA1rtPzzf6uAWr1RK-ca60INU5n4ATbeI6OcOxQlWg2Ya-HvKKRoZ2fXOKMpGDw-ccwVPoH7VT0jrBtrGrL489-r2o0mQ4IouS8YYbT2ih4srJbKMokvZI2fxQykrs63-1ULiT5IR2PPkb-QXA5m__BZNpRDliyrD5_dkEQ5OL3hLtFqBsKVyJtScayPGLYX7ra5t0QLB2gl8HfXUAX_cePFEEATLEGkJn2mzCSiE5cOwm8XuvRrfk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در هرجای دنیا همواره فوتبال آبستن حوادث است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102325" target="_blank">📅 12:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102324">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xp52jHaL-tItnLiudaspfSI0RLn81FyHidO6YRvxewx9GYdzQpnWrlNck3vRg6PDcFibzL3QXoAtf6IArTY1b4D_TiLCSa5e3BpCVamdowlSWuJlLCQBgQEliaXFyXHeRL4jpT6xxawAV7LUWLEBj5TxDckWWgM-pjQhhoW69GfeP4TL6vCiWFmf7kAIV53QonSLA1XTDaZqAH6-FPotOscL-DyzoYrv0_4m4SfXSEbLJm5_tYAnWsnQskShaJegn1WIgjpC4jeVsAQdjRWSKY1qvCvvPxQ_rlYqOjrbqu_-Mbmwxuqtxvz6_fYZzOcbbsSwY4JbyeP37HC37bKfkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتیاس‌یاسیله سرمربی الاهلی عربستان در آستانه هدایت نیوکاسل قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102324" target="_blank">📅 12:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102323">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9305c345ee.mp4?token=LEJhivmdzV6DJtOikt2ClMb2vxYJ3qRN8-gsmeWC2dYOfn6c9C6-g98LdUWzA0hNDWSB8GaHH8ZnsrizCoD32esVIs406EpDGbY_GRrHBW6SgunaTIhRdCV7N4FYCOCvu9yUf9S155Q3EPOKvpVpmw2kczs4V7pU5KRThn7ypZZ5I-Gpxs2eNV5kJDSLS9e6emSowDGtklZ6VB2oqr-uTNNA5cQcAN_A1RJQFXcuD6AWLKhQLgMMQ1EkECYvNhdJWWYlqOMxveEMMv-TmpNl4QJyWsVLyZzqQHfqxF61xvbUXMQggSyKGrcaym7chfCAsbafkYfPkj4KydSGlA_LaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9305c345ee.mp4?token=LEJhivmdzV6DJtOikt2ClMb2vxYJ3qRN8-gsmeWC2dYOfn6c9C6-g98LdUWzA0hNDWSB8GaHH8ZnsrizCoD32esVIs406EpDGbY_GRrHBW6SgunaTIhRdCV7N4FYCOCvu9yUf9S155Q3EPOKvpVpmw2kczs4V7pU5KRThn7ypZZ5I-Gpxs2eNV5kJDSLS9e6emSowDGtklZ6VB2oqr-uTNNA5cQcAN_A1RJQFXcuD6AWLKhQLgMMQ1EkECYvNhdJWWYlqOMxveEMMv-TmpNl4QJyWsVLyZzqQHfqxF61xvbUXMQggSyKGrcaym7chfCAsbafkYfPkj4KydSGlA_LaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇧🇷
فالکائو برزیلی بهترین فوتسالیست تاریخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102323" target="_blank">📅 12:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102322">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1c528fcb.mp4?token=eudO8BNZiT8wHCmGAOOoBNC2-AjVjBZtkHAHlPLgGuovWVjd51nQXRrDUFFPciX-sY1uUiQ3mIbNRzWaSES7RkTfn6ROGYEpyvDwstN4xFXVJGjY45WtHTzjOEhqz_Nl3G0v8SsT7t3bdkjVPNjG0DM-HIrEWhpHFpGHG-7rLXKSEq2plMHLufddzqYEhzmvmU6qWolvCYhH3lrAhgWwPnTaRudLxl5NPhqb87yLlDKEaUUuErmbkOmlgUfPMj9FfJkx8vxQzrDmHjTfApaSbduvfp0EN3usnFAHSTHPIhdqcJecUJ2nmTiLTFIgqzUKMaVhsc-kSqNH068rhb03Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1c528fcb.mp4?token=eudO8BNZiT8wHCmGAOOoBNC2-AjVjBZtkHAHlPLgGuovWVjd51nQXRrDUFFPciX-sY1uUiQ3mIbNRzWaSES7RkTfn6ROGYEpyvDwstN4xFXVJGjY45WtHTzjOEhqz_Nl3G0v8SsT7t3bdkjVPNjG0DM-HIrEWhpHFpGHG-7rLXKSEq2plMHLufddzqYEhzmvmU6qWolvCYhH3lrAhgWwPnTaRudLxl5NPhqb87yLlDKEaUUuErmbkOmlgUfPMj9FfJkx8vxQzrDmHjTfApaSbduvfp0EN3usnFAHSTHPIhdqcJecUJ2nmTiLTFIgqzUKMaVhsc-kSqNH068rhb03Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
❌
الکساندر پاتو؛ ستاره‌ای که قدر خودشو ندونست و خیلی زود از فوتبال محو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102322" target="_blank">📅 11:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102321">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfUZUV4WD3eypy4er16uF9FukTFMnxT0fODnLF-gcLsxkbegS4ndj0DmzBMHd8jjVGyoGjOqR38gCUDxYtdxUj3Y6PgbwUa811PQIDiOepzuvM-fGRB-4GDv-veDhL-lXU0RsDV1itlRMmXcDOARbRDv0pFFM4g9R3ZPOm0EABs86pEtMesF4MvXxBeHEQFJ_biOW-IIoHTEXB03JwrLNZP64jQXaY2gNjc1N8xt5P07nzIlQ8UEFNY_KVm_AET22ZwxkaojBMX1ag-aLbvYGMYXqOYxF_wCViVWF6npu6oHl0BPSG7IP8um-opdtzX7uc2oQtRJbltx3pRLZ_RVXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
⚽️
رونمایی از کیت اصلی النصر برای فصل بعد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102321" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102320">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
🔹
بازیکنان خارجی ، 4 مدعی لیگ برتر
:
🔵
استقلال:
🔵
آشورماتوف، ماشاریپوف، آسانی
🔴
تراکتور:
🟠
خامروبکوف، هلیلوویچ، ایگور پوستونسکی، اشترکالی
🟡
سپاهان:
🟡
ریکاردو آلوز
🔴
پرسپولیس:
🔴
دنیل گرا، اوستون اورونوف، مارکو باکیچ، ایگور سرگیف، تیوی بیفوما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102320" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102319">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQcDfqLVoH_HwKLZtXFo_8PbAGmFE2TghnHCnJfUCSQdCKzfftaMSGi1CXQmBdUtWtYaZ9UDwnV0-zb0ehrKf7u2c6Jz1GzGP_kaSk9icpBou25fWpXwrV5xv3UudA0ZhlJBOD2Xp6FnoXs6aVaR6qsvUnstp7e7A4zpFtJeSHlDgmXn8r9EPxox0tTMDiAtGZMpJAWfanQL7uU5bkhpgIHfXB2NdedbvOdxQxRb57UEIuA737mpeSaduCZ1VaiGpngWUPIhK4-CbsuIhu1CWSE96rnMlp8MEoqgyo3xScchyucFePRcO86M_KnVYBhB5ajkxp8ql_KCjud9gzwEjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتیاس‌یاسیله سرمربی الاهلی عربستان در آستانه هدایت نیوکاسل قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102319" target="_blank">📅 11:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102318">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=qSXQSJO89G-05cziXmYc1uEtzoM1t-Y-GFjuJk7SWm4u3SJLhjVIng5f2Aw5zBPYE-yDb78GtfwH3kDcokeJGMQk5OxwnTvrlN3dZoYNdzwxgHUShWx2wZLaUxyr32bboWOZXqVuVButyMH0l2R_iTxfmloAh7adlsGM5aLyNnxZnzmfHxvRN-E8AIH3Vg6T054xvoFy8D2ZNMA1EE-B9E4A--NM6yBSJg_CtJzWEWBxVUlTYj35h03CiVUgY5pgt3qEMKzuDul-U4V6S_17KE07aZvkQgX1mJxTSqmaU8buIHtQFTDOvCwLPHuocaSJ_Fn_DsSGtJMO56IfKbpViQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=qSXQSJO89G-05cziXmYc1uEtzoM1t-Y-GFjuJk7SWm4u3SJLhjVIng5f2Aw5zBPYE-yDb78GtfwH3kDcokeJGMQk5OxwnTvrlN3dZoYNdzwxgHUShWx2wZLaUxyr32bboWOZXqVuVButyMH0l2R_iTxfmloAh7adlsGM5aLyNnxZnzmfHxvRN-E8AIH3Vg6T054xvoFy8D2ZNMA1EE-B9E4A--NM6yBSJg_CtJzWEWBxVUlTYj35h03CiVUgY5pgt3qEMKzuDul-U4V6S_17KE07aZvkQgX1mJxTSqmaU8buIHtQFTDOvCwLPHuocaSJ_Fn_DsSGtJMO56IfKbpViQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
با اعلام خبرگزاری رکنا، نوید زیادخان قره‌داغی همون حیوون کثیفی که دخترارو تو خونش کتک می‌زد و لایو می‌ذاشت، بازداشت شده
⚠️
‌‌ ‌ ‌
یه ویدیوی وحشتناک ۱۰ دقیقه‌ای از
این حرومزاده منتشر شده
🔗
🔞
مشاهده ویدیوی کامل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102318" target="_blank">📅 11:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102317">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
‼️
🗞
🇪🇸
رومانو: رئال‌مادرید و لایپزیگ بر سر انتقال دیومانده به توافق نهایی رسیدن اما دلیل اعلام نشدن خبر اینه که لایپزیگ ابتدا باید بازیکن جایگزین جذب کنه و سپس خبر رسمی اعلام میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102317" target="_blank">📅 11:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102316">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a432ebcf02.mp4?token=gLFiVhlKzG7FJ0YQi4dqbYp8j0FXmmDpndzcSL5oQDoKa8N4UXSVD-mIVRZAC7_FGHYdl3P5WVw18461NJzqPhz84Sj5ojL6CgpECmFZ4OF7yDEueum7hj8XQ1_OkZ_A_IrFl-6raPUKIdYkmrRasKQWs2ZZHwmxiQOL3al9W4I-xAeEQO5iCCEP2pyLlQDpkU5LC_1cnidbjX1v_oF4ZzewIKRg69WJoK8_xR9KwdS40gIa3j2D1vSOqSDeWFUx8Ko9RpxKRK7A9-4yR7IuOmFLpqRB2K5AwhLBTD733sZcbiCT8u8uXQ4ZFo2LJxNz5T6aonaa8ggamxlsqfbXIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a432ebcf02.mp4?token=gLFiVhlKzG7FJ0YQi4dqbYp8j0FXmmDpndzcSL5oQDoKa8N4UXSVD-mIVRZAC7_FGHYdl3P5WVw18461NJzqPhz84Sj5ojL6CgpECmFZ4OF7yDEueum7hj8XQ1_OkZ_A_IrFl-6raPUKIdYkmrRasKQWs2ZZHwmxiQOL3al9W4I-xAeEQO5iCCEP2pyLlQDpkU5LC_1cnidbjX1v_oF4ZzewIKRg69WJoK8_xR9KwdS40gIa3j2D1vSOqSDeWFUx8Ko9RpxKRK7A9-4yR7IuOmFLpqRB2K5AwhLBTD733sZcbiCT8u8uXQ4ZFo2LJxNz5T6aonaa8ggamxlsqfbXIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
از دعا کردن تا بزرگ کردن لامین؛ چند کلمه درباره یامال از زبون مادربزرگش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102316" target="_blank">📅 11:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102315">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEJWuDtemdI1MmV-arsWxdozGKeT7mLFcGUzvGA_Cfi04wvRd6NB2H2-r5jwcgrVttMFdSzICR2Crxfv6A2ileQ8NU-1lLZsbIRerUV4kDJB7m_UB0JtNrdqTWVCnaqCIF9MCwTDqPM0tFRwnmsIvmlnxGGHR5DIMyx7X0hzVJrZJY6TbjMtHpOUgeN5HWfthkR_YlpcGRWNKr5miSU919CP2NMmU42BaqXO0MgVLbEqovfcYQ92GqvZ1B8aM0DUV_sHbfI1AJ51JX9Am1k9i7BExl4Z3jBK9q2ifEqfmo3pj5ujCDoJYxeS-8TT_7Fqr_nhY7rB7mzCjalCP6ar_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇦
🔵
با اعلام رسمی AFC، مراحل حذفی سه فصل‌آینده لیگ‌نخبگان آسیا به صورت متمرکز در کشور عربستان‌سعودی برگزار میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102315" target="_blank">📅 10:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102313">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB8VFnNrszajPacXstSh9A8UjUVhBQMMvodOfpFvsY9cBOhLDWn5ASKGkqIImmd-sixWcYzcaKoZANgKW7EXhMmU8OcsnXRwH8qn_HLZp-f_dk4WtFNGpCZiO6IPqd1ENcvUbKbqGIAmg_GoVeUwmJTxitZY1h_NGHfq4fXLo4P9jVffm6mb1xM_3B1olF6xP18KVs_zH2SAGkDdh7e1n4Xh0H7N7w-3mT3GYLhnuZacoGmgTxRliKeV5srPgHM-3iR7gHAlzNzfaEjTXsQKFUUv5U0lauayWiJgiJFrTbE8j1s70RtW7FrR9yjuXdEFgClSeBTtgHNgsVkvuPd6ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ایوب‌بوعدی ستاره جوان و مراکشی باشگاه لیل در آستانه عقد قرارداد با منچسترسیتی قرار داره و بزودی جانشین رودری میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102313" target="_blank">📅 10:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102312">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac4341594.mp4?token=qBVBxdS3BWZ-5yNFsrCw7AB9GA2hyRnzsknf20OwLusZpmtI2ReEjM2kFmzrA7IVykJSguJmtg4c0ygMbQVMf1rzO3ULNBwdxf-JAqoSczuBdQNH5s-bZZZO9iipZnIuPslANDiDx1HUE3xdWOIF2R01-yVKpoNVuGOLMkAPVuWmKBxNHJd3NXtIFAlG5bt1RL81P6qd9ouMQTYvwgFbKQCN0JgE5oHtDWFthV07MeuoWgOGb1qhyLyH9Y_gkNefYU5sVi9lo42gK9uw3q4URZJVnCD1IlUMooUmCinn4n5o1ZhpNQa0tVWe0oyHo9KIjlugkYNG8IjWbv6cJKSQVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac4341594.mp4?token=qBVBxdS3BWZ-5yNFsrCw7AB9GA2hyRnzsknf20OwLusZpmtI2ReEjM2kFmzrA7IVykJSguJmtg4c0ygMbQVMf1rzO3ULNBwdxf-JAqoSczuBdQNH5s-bZZZO9iipZnIuPslANDiDx1HUE3xdWOIF2R01-yVKpoNVuGOLMkAPVuWmKBxNHJd3NXtIFAlG5bt1RL81P6qd9ouMQTYvwgFbKQCN0JgE5oHtDWFthV07MeuoWgOGb1qhyLyH9Y_gkNefYU5sVi9lo42gK9uw3q4URZJVnCD1IlUMooUmCinn4n5o1ZhpNQa0tVWe0oyHo9KIjlugkYNG8IjWbv6cJKSQVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Auraboat kids
💀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102312" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102311">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZX-t7F1mfiTFNx5cIufMXR5g5DQQbw0J0oDVARzJmaKuoSU4vHBDEUCcy8jxyA4c8h2OkkEqZp1W6TKTusPauRJPkiCV5RJwQwO_ee168Efi8I2uk_3bmXy4_c6ycQcnZfkakiwpBfoOw3gj5_vkRz4MTCC82l84eRxaTdlJc6KmG3R6y7x60rCV3HiM3Pbl2c6Rcp5fZXBBOWV66zLs7TmizSCUonTKeY83BnGYqIJQ7dGIpq9r9626OQOtkU64ggNpSn6fyZJblRSLYBAbGpEm7MS8_6GEMmmED5_DVtc921yICGAvU4b0So6QePnw6WXjOa4-mp4LizWLBM2dCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
تمام‌نیازمندی پسران فوتبالی سرزمینم :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102311" target="_blank">📅 10:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102310">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gY18BWVibkRFkbMHplkbnpKPAbNP4RnKIOPFK66vDlYUXoEpWUM80y2U5oyJ-ssMxjlEucI1E7rDsbwgtuqke5Ovr32uXiYVqufUVRxHX4L5T3I0mVGD035o5lOi6m4lW6PlswKPPP8T_ZgTsd65qsd8KqQEwcgYOr-90VTUFGumJ9aBEozbHpiduMAgQFf07KK4U66cG8QXp03yt4FDnzRmQGmvHUseK_QA-sGuUCV0CkjZStHJLkP8CEeFF2JCAQpH22L3wrniqhv_QFmaDU38hNbG6xbaQ9L9Fnz_IndDQwb4FtbCtrXGHyUrxCCSqcVgDYf7fG8EVv6TcgdOzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🔵
فابریزیو رومانو:
پاریسن ژرمن و موناکو برای انتقال مگنس آکلیوش پیشرفت زیادی داشتن و معامله در قسنت نهایی خودش قرار داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102310" target="_blank">📅 09:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102309">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kf5sSrQpzFjq6s7rJJegEMwBk7UEIFxeCSWjFHV1fDh6bzF0YGmSeTORcQtqWsKgZ8ZywzW0kdKJG_nB6jLnr1cckMnQ1ZZBTdHBmdWLxYg0pM21D_sT7w86mUs04yvMeeLFH-IRDheHDf7HwcwPpS6wzWeFbmsbKppoEwMFbCY1-yASdcP9UGOo7lLQFHIaIBqYGVMznIS_F30V78gMmwj4wRtiH3hG6rZDHEgq832PStL6MLpRrPDN6iWXYjQDlD9pGP9dSePGjxC9v9nFpu3xHEYTXeGrJ2LMyOqF_5oJkSNKVBeLGMwOSxiO2zpmAijjkqGh66FVLPdP3QKJng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بلینگهام برا زیدش تو تعطیلات عجب پایی میخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102309" target="_blank">📅 09:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102308">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl1aXHvTWqQoecVsnLSjxuFBn2JHvAVubUcWpRL8sIYy-2fLxw3rQwuNO0mX1ni9TpptFYs3nfq8vtrTOjAacWAuDe6OCoeU3Vp_kelfsfGqHRDaZLrUDHPTJ41ZFiK9J2SJGx_pRRyWi0T4pzpWqOjD-M6zbvToPcY8cA6BuV4S3Oa23dCIrC748N2x2392cHm-A7yExHxyuiNlTJzWSketWLelZgHu8udvUgnxxXkoDfEocXmdzQRgB7NsI4r26uagqmuWot9Cu7wUgmtzhlN1yaxc-XOYHFXHdT7Htv-Ut3qIkmsnt9tpe3mAMytUstNucHnUXbzjm9s71Do8hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
عکس پروفایل فرمین لوپز، در حالی که تمام هم‌تیمی‌هایش در تیم ملی اسپانیا عکس‌هایی با جام جهانی دارند.
😭
🇪🇸
لوپز در بازی آخر بارسلونا قبل از مسابقات جام‌جهانی، دچار آسیب‌دیدگی در پا شد، که عملاً شانس او را برای حضور در جام جهانی از بین برد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102308" target="_blank">📅 09:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102307">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31f0971b6a.mp4?token=VjZ6NR1Af3b97GzeCK6x2v7_y1sniMynCeDB7kclXiCgURvjwswJC4ZKVQQegyslBTj--hyFVqF8GebuGR5BXczD7ZeSWQYJ_uLDy8gvRYbDEsn_ldZR0xYz5VvFsivWTct1eZZH4LW14DBAEumk7NIBLlVGBuTBaxA-oKczgrIkZrthIPTO7Rw-X77njmGWtTK8g5xipez_-Rr1wgRF9ZRlIfOSu0_TK_8t2LFokyqxSVdVWxKx-qlIwlSx_yJpeP0AAao_OgkchWMTCGe4TwG8PahUmo8ewdKSeH0VeRlm1ZctSWi-9i97H41QH3I5XtgRK2u_QD3931CbqEqw1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31f0971b6a.mp4?token=VjZ6NR1Af3b97GzeCK6x2v7_y1sniMynCeDB7kclXiCgURvjwswJC4ZKVQQegyslBTj--hyFVqF8GebuGR5BXczD7ZeSWQYJ_uLDy8gvRYbDEsn_ldZR0xYz5VvFsivWTct1eZZH4LW14DBAEumk7NIBLlVGBuTBaxA-oKczgrIkZrthIPTO7Rw-X77njmGWtTK8g5xipez_-Rr1wgRF9ZRlIfOSu0_TK_8t2LFokyqxSVdVWxKx-qlIwlSx_yJpeP0AAao_OgkchWMTCGe4TwG8PahUmo8ewdKSeH0VeRlm1ZctSWi-9i97H41QH3I5XtgRK2u_QD3931CbqEqw1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیوی سنتکام از حملات بامداد به ایران
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102307" target="_blank">📅 08:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102306">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‼️
👀
اسطوره‌علی‌دایی امروز رفته بود مراسم ختم اکبر عبدی که مردم این‌شکلی ولش نمیدادن و دنبال سلفی گرفتن بودن!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/102306" target="_blank">📅 02:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102305">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiGRLnGkH-vYsSQstItgbbnMIRJoQ7CFVGTKYotSWtUiz9wRma-4drwdSS0FsPShE5HSRm2oa_3zNQP2AJTKAdRMpwpetixjMR-99YuNHYnOzGpLAFIBn8QTBMYQbhoI-qFZBNW3K2O_n50QbFhTzhtzEewK33d7WgaOkvQ1k-F2IGYUGyoSAgkCaCAUudX5Z4zgEiAizrm3eTPBfLH7rnyYN69CNATC-BxojAuNSZhaC3IvrBqWKA8NE8-669koQv4A-sRoTFNTZHbEMWeuBvKog_KoqkWEzwwFGtni8hou3jgaY1Tz3_IOsz9O2lDrVPU2MRf8m4H0Y3W0R5gG4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از Cope: اولین پیشنهاد رئال‌مادرید برای جذب رودری به ارزش ۵۰ میلیون یورو تقدیم منچسترسیتی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102305" target="_blank">📅 02:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102304">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7Ci0H5CSDKe19Oym76Al9nSEOoAmSdK6A-8bG3sLTqAIMF_2jEsJ8cHpBnaitUQPEOqcNRUOoc_4i8IPiFbiT_CfNZkx6TLBuQ2TXRJeSiYnqiuP58frmzG39L7YYiNhfO5QBNwxOd-6AGMMU6GIZ2KSqnHD6B_fPkLZW898PDhOgNkyOz-j-z31qJqB3HOkbQaeygNn8XoXeypPbSVTj2YDmEWIhdmws3VMFpgdWQrabX2oy8xK0wxorYcDHf75bcXCnPvLx6_UQorg44PsubdYlJMEoMQd_lCTPhEkuZIHdQOB_aVf7E-KD9NJn_5EH-4bC4BM7rnp8dIF7KisA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
🇮🇷
وال استریت ژورنال گزارش می‌دهد که دریاسالار برد کوپر، فرمانده سنتکام، طرح‌هایی را برای یک کمپین هوایی ۱۰ تا ۱۴ روزه با هدف قرار دادن زرادخانه موشکی ایران به ترامپ ارائه کرده است. ترامپ هنوز تصمیم نگرفته است که آیا مجوز عملیات کامل را صادر کند یا حمله محدودتری را انتخاب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/102304" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102303">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6afbb43876.mp4?token=vr3bwRc7pr8eFyda_3gtk40QUW_zlOMCMpMC7k35xQI1CYKEDGawNJtP6g5HQBxu5CX7E341XH2IL9zXQghXiXTAWUhA8WWOEpLBLs2MvmWsjfQuOvsgsswZztI-IWq-KJesAmBgnoNc8ws8EHgWgi_JIF0vxKXDsQOpk-cOtrxhG62MXmw36qXB-A7zZwfKV74IPlojHt5qWYuaMsLoqA1m3WuwLzTyFJYwJuZiQiJ2MatRb7QUXeqTVyS1R31ieMEkz0NaV_JrpVE9RKDa6iVQ-G7UAnNpTshLriSbr0mP9vNBs7zMclECFhn2Ltnt1G6h1JzwYHMH7Zq-R34owg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6afbb43876.mp4?token=vr3bwRc7pr8eFyda_3gtk40QUW_zlOMCMpMC7k35xQI1CYKEDGawNJtP6g5HQBxu5CX7E341XH2IL9zXQghXiXTAWUhA8WWOEpLBLs2MvmWsjfQuOvsgsswZztI-IWq-KJesAmBgnoNc8ws8EHgWgi_JIF0vxKXDsQOpk-cOtrxhG62MXmw36qXB-A7zZwfKV74IPlojHt5qWYuaMsLoqA1m3WuwLzTyFJYwJuZiQiJ2MatRb7QUXeqTVyS1R31ieMEkz0NaV_JrpVE9RKDa6iVQ-G7UAnNpTshLriSbr0mP9vNBs7zMclECFhn2Ltnt1G6h1JzwYHMH7Zq-R34owg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
عصبانیت شدید آزیتا حاجیان خطاب به مردم در حاشیه مراسم ختم اکبر عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/102303" target="_blank">📅 01:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102302">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIK0t6jW3W_MFNzwa602Fj8JRpdziqDQ2xCIPXNzyJN7LU_Ey91kAHxdR3F8sdSoic1sJymGLPiAbx5p5LtmtdOdjPHmK5eI5IdVRww9o7YVYq1sVCXMDFUJQN-T6e6W3TOmkIM3Eq4Ramh5ooF02bRtP5TuCscpffY9eKizFD0FG0kLphYNuZGpqBvdXLISu2sXHAwMTf7boDk9X6V_sWCvkQemChtWtTSKzEWN40O5WguJMIhwErXq4rxLP8CWMVOyxHvcV9UBtUgXL97-H9T0DKdcHDON_WXZr8zKYfhgQvcSf6J9NZFupPpx0n48n4ZJcSqY9Rx3K9J6A9kaTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🟣
بازگشت لیونل‌مسی به تمرینات اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102302" target="_blank">📅 01:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102301">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4e2122bef.mp4?token=ukx8VS9GOt3xb1TV1rz0lj-EgTRzrw8JYe-aCO6xGzYzGuywCJ6zYeUZcApZhHROyU0uzDrIPSQdAko3y-6WNrCBVBzYfvNNGMLo8nXevflXixDc3dMdpoQUIp4olOlL0OIjsaoc42s514j5M3eWvsOtlHbw9ZaDj6JQPvU513S4ureazb1lATha9ppRBL4sR1XLQRkOohfomQrpSZjd3efy_4jcne4Oi_WxWrxCDYvnwELWhXddBE6puDDBbrlQjkwb-5rYlWzU6KUYXs2ohyVUcxqZN1MFLeFip1VFFNLM50t880VNAhSGw6N2KGIQtdkSVrJ1Xtd3QMwitv3n7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4e2122bef.mp4?token=ukx8VS9GOt3xb1TV1rz0lj-EgTRzrw8JYe-aCO6xGzYzGuywCJ6zYeUZcApZhHROyU0uzDrIPSQdAko3y-6WNrCBVBzYfvNNGMLo8nXevflXixDc3dMdpoQUIp4olOlL0OIjsaoc42s514j5M3eWvsOtlHbw9ZaDj6JQPvU513S4ureazb1lATha9ppRBL4sR1XLQRkOohfomQrpSZjd3efy_4jcne4Oi_WxWrxCDYvnwELWhXddBE6puDDBbrlQjkwb-5rYlWzU6KUYXs2ohyVUcxqZN1MFLeFip1VFFNLM50t880VNAhSGw6N2KGIQtdkSVrJ1Xtd3QMwitv3n7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🟡
افشاگری مدیرعامل کارخانه فولاد مبارکه: دشمن با بیش از ۵۰ موشک مارا هدف قرار دارد و بزرگترین دستاوردش در جنگ همین بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102301" target="_blank">📅 01:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102300">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IU2PDdhiSQZbEZLg76BffyiE70Nn9AG7RqNDSxQIsGbrE0F-XNi77WyRb1ofAqYELkOqLnSTC3kmIsJp5OEUUCN5wc5NsOOTHQktXfriD0W-KSS_liFMW43_9RlbdjieXJhqhW9Z601uu_FFdgJ7ma2J6n6PGL-HTEDLJqLQdRwWK4jjT9CQIbwt5in4pfnXw5iV3B3H7LQZlMJDptA_af4deG9BxnJ1et6cFTlS-YE_p0o8BaAGoTOnrbLNagBZ5VDND3BZTRatyJeBy_J8srNGODlPpRyQNrdm89LBFdpjQr_yUSerBADMaYiLkqkpMxo_Hf4Mr0cxPa2uzbxJnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
📰
به دستور ایلان‌ماسک، صفحه خبرگزاری تسنیم در اپلیکیشن ایکس(توییتر) مسدود شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/102300" target="_blank">📅 00:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102299">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fe21feda.mp4?token=NAO9XDgka1mZFOhm_aaxQhlj8JdFetXmOyWbugApozpx3In-vgOxPRr90GlKSOEzaP_up-f5AcTuEgRiLPtbsJYPb75tEz5w7hjb6P-zdgTousNGhKOTiEYjdPRbZ4PL-N7OfDNuDKYMlJHOSPMtlNS10rNgZUea3UYMXyZxicV_1fkLxumeR40bvBQCK5EmbzEXc2bwnd10ygDg1_OWe0nvsP7IaARaYO3y2xpFYncVR0FZjIwar246nq6-4OS75LgCCjbsyTskE9W7JLgNdVJLmk4yk5_f3LVc2xOkSoG_vqdrIKJCfGrZXs7BZatj6nFOjW5KbbwThlhrgkQrjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fe21feda.mp4?token=NAO9XDgka1mZFOhm_aaxQhlj8JdFetXmOyWbugApozpx3In-vgOxPRr90GlKSOEzaP_up-f5AcTuEgRiLPtbsJYPb75tEz5w7hjb6P-zdgTousNGhKOTiEYjdPRbZ4PL-N7OfDNuDKYMlJHOSPMtlNS10rNgZUea3UYMXyZxicV_1fkLxumeR40bvBQCK5EmbzEXc2bwnd10ygDg1_OWe0nvsP7IaARaYO3y2xpFYncVR0FZjIwar246nq6-4OS75LgCCjbsyTskE9W7JLgNdVJLmk4yk5_f3LVc2xOkSoG_vqdrIKJCfGrZXs7BZatj6nFOjW5KbbwThlhrgkQrjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
پلن آخر بارسا استفاده از ترشتگن تو خط حمله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102299" target="_blank">📅 00:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102298">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ip1MbEl5mY6RyFcK-CCCZAIm79qapz5mmj2u9Qjl43js0cRRUPhz_Uz9zc1c9fBqUDBhqnPOpg6nyV1MNnxnmbr2Ty7xLarcvjAmKdzNDqFXUxgAnGf7NAyZn2j6ZJ3NXQh7VCit8FHPNmXZTyLI21FxVSdbQBOZ-enzutEPHWW1cfTrcY_ce_Fnktohg11lTJncIX-jmBqy-ZB4t8byKtJPRrsx-ysDnqGpnDPiqj52ehiA-G9ynuPWK5eVySvdgaGvkUsCu7dE75_U89SlBk8JY5VOAGOMQsoC9UVE2rBCKdOKXjX6YpjgOLxgcGRT7MDmN_X2r4oj_ZeXFWnoVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
په‌په‌آلوارز
:
🔻
مورینیو، وینیسیوس را به عنوان یک عنصر ضروری در رئال مادرید نمی‌داند.
🔻
باشگاه، این بازیکن را مجبور به ترک نخواهد کرد، اما در عین حال، درهای خود را به روی یک پیشنهاد "مناسب" بسته نخواهد کرد.
🔻
همچنین، باشگاه قادر به پرداخت پاداش قرارداد به مبلغ 80 میلیون یورو یا اعطای 80 درصد از حقوق تصویر (حقوق بهره‌برداری تجاری از تصویر) به او نیست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
از طرفی نمایندگان آرسنال پیشنهاد خود را به‌وکیل وینیسیوس ارائه کرده‌اند و حالا همه‌چیز تحت نظر وینیسیوس برای پذیرش یا رد قرارداد با تیم لندنی است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102298" target="_blank">📅 00:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102297">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-5qslWY88Q8QyNqf8Fr6L8btnEMKvciGCR-wfB4nz39FrmY6RetdyJuSgLquwepBusy55B46o0wkuPiVMfdBEa-BuMmvw6NnPOJjZJDw4sCiihcbiV4q9dcpddqs0BtmXCtEJTsOx_yxX597VCPttHXs9qEW669zLVXvmJAt7-BQzElPDl-12NK7V6r9bPxxFzquBfZhEGQthGNGpURe27YMKq9akGTBxVlbOmndmHeO0uCORrffO_FEp0vyvdDdQ-BCIsUKxnp9PaE-bYbuPdS-hj_b2R72ZNDLmY82ll4eG2f9Q3SDAw8fiD7wMJ8F_vuUHWa9LZ0smiilgDsug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇪🇸
🇩🇪
فلوریان پلتنبرگ: امروز هم توافق میان رئال‌مادرید و لایپزیگ بر سر دیومانده حاصل نشد و مذاکرات به فردا موکول شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102297" target="_blank">📅 00:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102296">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a93d51cbc.mp4?token=Eu9JbRLYU5F1GvrFGeG4yoa_37YCN6PYC_m5BBzrLdzFUnC4MkY4ovINRpxU7UuCzoa8vmMR8YSFcnFq8HzRTwN646ryRxNQU8giqcEMLGL54kfGKIDeCI6amMi1KpkdB6CJSAiTXncusS9c-PrtOJ9DjN-nkwgvQIrTwvk_J5ch1VhlwlYpUU-K-l2kbp5idVNO8HfK_anLUhZhxwi-5sHCCL3G0GTRzqpChNmHfOYzeSDlae4lTatn2XQGxn7ubwvdlKBdO1WGUGr4Mg_jzNx5YXaBK0yO3E3Q3TYAEktiZzSV62Tfl_VjuLOfaVXp6ab48O_S7-WW8K4Ybxbj2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a93d51cbc.mp4?token=Eu9JbRLYU5F1GvrFGeG4yoa_37YCN6PYC_m5BBzrLdzFUnC4MkY4ovINRpxU7UuCzoa8vmMR8YSFcnFq8HzRTwN646ryRxNQU8giqcEMLGL54kfGKIDeCI6amMi1KpkdB6CJSAiTXncusS9c-PrtOJ9DjN-nkwgvQIrTwvk_J5ch1VhlwlYpUU-K-l2kbp5idVNO8HfK_anLUhZhxwi-5sHCCL3G0GTRzqpChNmHfOYzeSDlae4lTatn2XQGxn7ubwvdlKBdO1WGUGr4Mg_jzNx5YXaBK0yO3E3Q3TYAEktiZzSV62Tfl_VjuLOfaVXp6ab48O_S7-WW8K4Ybxbj2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمای اورانگوتان از بدن کوارشما ریخته
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102296" target="_blank">📅 00:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102295">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4b353d1e.mp4?token=pKNrxYQTPahMWPtRg-q0HoUGsejsjuU4BIifvxYNl3RjEWqBA_Hvz1YtzDcDAYBGI_OmygD6o8d5OjHYpLBdOThlgyC-JaFRLceoHATFrEPMc-6G2731xqAcc2pDprM_gsHHi-J0JBEC15UknZUPh7KdNvry8KfCHogV224nfcdOxXLfSBbJbyPhX--ajJ1PyGWM9HX1xsBOWkVKRz8Ghp1xOUjEFhvYtiVY1UOOfmywCj20ke67Wr-DD9qtLPcpSkHQj3wdC62jynqJYTKdYtTq8ie_4eY8CkGCmK3ywNy3Yoo-TOPdxFs-uPXiy_kVlmFEMm95l78HS1njK7O_eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4b353d1e.mp4?token=pKNrxYQTPahMWPtRg-q0HoUGsejsjuU4BIifvxYNl3RjEWqBA_Hvz1YtzDcDAYBGI_OmygD6o8d5OjHYpLBdOThlgyC-JaFRLceoHATFrEPMc-6G2731xqAcc2pDprM_gsHHi-J0JBEC15UknZUPh7KdNvry8KfCHogV224nfcdOxXLfSBbJbyPhX--ajJ1PyGWM9HX1xsBOWkVKRz8Ghp1xOUjEFhvYtiVY1UOOfmywCj20ke67Wr-DD9qtLPcpSkHQj3wdC62jynqJYTKdYtTq8ie_4eY8CkGCmK3ywNy3Yoo-TOPdxFs-uPXiy_kVlmFEMm95l78HS1njK7O_eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال تو تیک تاک : دوست دخترم خوشگل ترین دختر دنیا با من آماده میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102295" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102294">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102294" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102293">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=Py9a9i-OYHSENGAi0xtdvSUAgbEtgbiQ-55VYpzZMlwDsjErXAn0amtE9vifItMLw5gtvmHdoZo28f2vKua5Qs_cTpfhRcOg7G5aeh50hrKBlXxPv7Hrko9SPoW6BQSvafyCLWbzv076iOwJ6J-iLqsjMXrNUEfPWu6oVV7KNWHtomoP2tR1EX5-YRr-N-rxse_BiPvEUzxR3cC7kQ3jjUXkWm-TXTjr_IsAGOfy0krojiHGenSB85qi7_-0fDt3J-vrfS1eEHsBNzCXkYdiPO1nctBbDwAMbl50iqIiHFR4VQWU4zqpl7IDLZ8bOsVQbMK1AFSRVFx-HC64Ifdm6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=Py9a9i-OYHSENGAi0xtdvSUAgbEtgbiQ-55VYpzZMlwDsjErXAn0amtE9vifItMLw5gtvmHdoZo28f2vKua5Qs_cTpfhRcOg7G5aeh50hrKBlXxPv7Hrko9SPoW6BQSvafyCLWbzv076iOwJ6J-iLqsjMXrNUEfPWu6oVV7KNWHtomoP2tR1EX5-YRr-N-rxse_BiPvEUzxR3cC7kQ3jjUXkWm-TXTjr_IsAGOfy0krojiHGenSB85qi7_-0fDt3J-vrfS1eEHsBNzCXkYdiPO1nctBbDwAMbl50iqIiHFR4VQWU4zqpl7IDLZ8bOsVQbMK1AFSRVFx-HC64Ifdm6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102293" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102292">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYC4G0pmDltwfnQ7cPvdSwm_0uAj9z0mHL2OXsDjrDl4jHtQ6zv_kH6mmfo7s8yoDtDcXACQvKAhiUycTklYwsS6z1VId0Wom2DTpJY5lIV4ks9uJ5elgEKBBGDbWE4ChOJkMrib4Cn1WJq5eLSs-RzkjncR1ObXbVp14ysUtKQr7cKs7IQe2g8mJhaVjWopXnuEpyAOajcKr2QSWzdyMCzeSv6ZYl_agiD4kmposn2h8hopIVIHeKraIAG5DgIN8PoveCoApfFcWV-o7s9VZtMUd0fyWSzOU7AEgaoulND9dXee5NgimX_ETvEqKJYA5nG_K7U38twn3C7sjGOOIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری از پپه آلوارز: مارک بلینگهام (پدر جود بلینگهام) در پایان فصل گذشته با باشگاه رئال مادرید در مورد جدایی پسرش صحبت کرد او دلیل این صحبت رو اختلاف نظر در مسائل ورزشی اعلام کرده بود.
باشگاه اعلام کرده است که جدایی او امکان‌پذیر نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102292" target="_blank">📅 00:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102291">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXjzNkI97Ag_9zvF9CMZkKpXsRFYCSWK96UQapNv9sK4Ns-eKKvIEXRHZgdUj70GJycUm2-sYhJ4dIJPTF8uGO31NgMOtnR8RKRLFwc69HRruz57eNgPLJg8GSHA5qj_X2ZdIZzDiULWmAHGGjuigi9gPqps1fcmG2qz9SZOdd0Y8q9PBZKXxKiUfcaLuVe1TEuAaI1-6CS4V5PxqWGJfUGlgWVrUF9Y8LHstmZZiziGl1xfCmfidXJL99LPWwP5qIMrAJLzzDw2Om7Kq_uDzJ6vCFXwFO7hVYdJ84Co8g3uOQFRoXjAaWK-4XYOyzd8zVdTfyEq8jbsiJ92YbNF2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇹
فوری از شبکه DAZN ایتالیا:
استراماچونی از ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی ۲۰۳۰ پیشنهاد رسمی دریافت کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/102291" target="_blank">📅 23:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102290">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGf7u4dV_12AoEKpZnW3AEDidMuvUsJPt4bCLs6hs0P_CfyLxzM7-lE41jc-ONnUTO9EcNxgBd5vbtfUdEJCsei121aYT0o3LehEMrJoBDM0vz5hyPNzmW9lNTMiqtfyxpgwgpqEljQY_g16nrowYvTIZ_-aWWI0RAadvMf03-qMEJL74Flo2HXnE1FtvDN3OO66NPx1URWS297oa2o3aCb9MLBgadr2DI0pJEt79-xKCkVWSTsLp3VNT-loDpNTQ1rFtVr7cW9nPFuMcmFaw1DMqcYhg3MQtbTXrDxr-TzZX7GpLz6JYKLJEGfjCogqsuOqy4PL449hNFkvoksLkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فرمین:
این بدترین تابستون زندگیم بود! همه چیز داشت خوب پیش میرفت که مصدوم شدم، اوایل جام جهانی نمیتونستم بازی هارو ببینم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102290" target="_blank">📅 23:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102289">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4mmsHnyDNbJ4g-wEbZa5_MrstDUWHHEf4nUmkFqac4cprfXJS3ti3ZijDUoqmS7K66NUFW4kxV2z_H2nX5kGFmyuEPSrxh8s16UWvaqs-82a3gWZrEKmw7zPj18sXXJhDjAwvs8V2Yvtaa6hnHIfXN9DLiaY7SUa4Ps6QeCudOXbQQ_5iuQFoP9a1eusW_j0XwNl_fAEkw8bg6dLORvCNcyVoEJc9SYCZSn67BwaVUW6Eg0G1M8kMGrEYesjTjFEcGkt4kvmCEFh9UpoMnL5R2dgSe5xvRd0n3DYeQMN4HvGSC309drjufvVoVwsur03fqA1Zp_VIx10_gz7Ii-sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
کیت سوم دورتموند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102289" target="_blank">📅 22:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102288">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osJ70eJR3k9-4RoDRsyzkpAqBpATF46PIVLmLCmGZXmgOOyuRkcuInOSGz6Djvf6rZNu0iL3XNkAzMqsp0ojifRS4KV4nMGcPSdqLE_8RcSc59ta--S4BVPEe-ablazo_jPovuGetHpHpZqjPuiHK8rzNchOcHe-pwB5CBsSWQMfQkuntExCiNeiv27lgVTBy8XrnXqEiXfJ7OFxhZhGLyWMFU-DNPjLnNF25sf0X-FXezCdGukAqq83OMaSsYVliw_M9qjoHfrtuzYzfMCBF9d7EttNzi2zTLkB7GnjmEfFIUZV5iFhAWPqbJaK7MIoqyi5HGEDtByeeMwaOxsYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید رونالدو چه سیسی گرفته
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102288" target="_blank">📅 22:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102287">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b210f5e9.mp4?token=jUzqETA-C5NyecJVwQqtB8S1hPYh4F0R3r-6ojrjTchXKjj2NqlmVfRWqIbHKfpZnY2_4GngDflSyR9oHu_59mmRw7zHpqN5afmnPmF1XnXSd42FFZp45R6Q8saz8LGJBfv1LTGEEYXmzc4WpmnO9pz9nbxFPtKa7JOwnjvLT4oX1nnLFB2BLMfhKdTZNJOEqazk7G_gi-WeInDTU7StqJ6DjFNejxKOv9a3NYaSuTP2qayt2QGlkILIWITilGt6FbS5c4EuA4UDpUj51v7_Qe7wVXQooo0VcOycPFHhB5E8oSg5Sba6iDuuEtSDUpcGvZ6GGK9TF0PJ5wyOvgHKng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b210f5e9.mp4?token=jUzqETA-C5NyecJVwQqtB8S1hPYh4F0R3r-6ojrjTchXKjj2NqlmVfRWqIbHKfpZnY2_4GngDflSyR9oHu_59mmRw7zHpqN5afmnPmF1XnXSd42FFZp45R6Q8saz8LGJBfv1LTGEEYXmzc4WpmnO9pz9nbxFPtKa7JOwnjvLT4oX1nnLFB2BLMfhKdTZNJOEqazk7G_gi-WeInDTU7StqJ6DjFNejxKOv9a3NYaSuTP2qayt2QGlkILIWITilGt6FbS5c4EuA4UDpUj51v7_Qe7wVXQooo0VcOycPFHhB5E8oSg5Sba6iDuuEtSDUpcGvZ6GGK9TF0PJ5wyOvgHKng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ادعای نادر فریادشیران درباره بیرانوند:
اگر بیرانوند همان متنی را که علیه علی دایی نوشته بود، جلوی من نوشت. نامرد باشم، یک ماشین به او ندهم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102287" target="_blank">📅 22:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102286">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQA5fxNkcKWLCF-jhCyn1V-Bt-blPF7b-Om-JwIEQiIV1hUaoLUKSSw7Ve-8W-56RxJqC7or2bzEKg24mhqUX6_z6KmFhO1MejtTYPJM5NcvYjl_mJsU4HYo0W3xgUUWitWLeXYqBmd06igSxLjjh4tVPlpPxtKGQHLDIa9DxoZEtyNB8abPP0qcIl59v54X9oWFAwL5-D1YpivJHjVGrhf2TRkeraz879pRjgRF-ShGTEO0vh-cfkzePhtFCY3zd6ZNEYLvBfK0mpb5tbnrw5SjSursxt57WhG9K3s6_9WqimKwmm4LwaayE2UiKpU14IoDZx4MBqx0sQYC-q0iEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
فیفا بدلیل نمایش بنر فالکلند در جام جهانی 2026، پرونده انضباطی علیه آرژانتین باز کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102286" target="_blank">📅 21:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102285">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb35f99ea4.mp4?token=ky2kEc7hKJ03qHqU8QXABzq2oOHhiyxXuYX_4CMwRz14gy54WFIYDgKcVrQ2eiPdWulrQoGsMKhG_3xZSahAUSBo_MIsVqc0sV4vgMhEZUjeu9votopIGiJXcB7AEBDVuzD_7SgQpHAGMqnpb1B6GbY2wC6JfYxfL1E54cXbPEI_VLdqZ3EBa_qF3v85IwzRiEL03ydW2Bc-EalwPnVDGEseOxfdwUOOk6cql_yqukgcJplPeeDCH8tZIztSiOzOhYABSqotLSHhK1GPXTBcQxevhv5uj_aPhENJEWJCDkgaEDeu5jIHkGq7qcKYbgeM_AuiadYjJp2Siftxninusg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb35f99ea4.mp4?token=ky2kEc7hKJ03qHqU8QXABzq2oOHhiyxXuYX_4CMwRz14gy54WFIYDgKcVrQ2eiPdWulrQoGsMKhG_3xZSahAUSBo_MIsVqc0sV4vgMhEZUjeu9votopIGiJXcB7AEBDVuzD_7SgQpHAGMqnpb1B6GbY2wC6JfYxfL1E54cXbPEI_VLdqZ3EBa_qF3v85IwzRiEL03ydW2Bc-EalwPnVDGEseOxfdwUOOk6cql_yqukgcJplPeeDCH8tZIztSiOzOhYABSqotLSHhK1GPXTBcQxevhv5uj_aPhENJEWJCDkgaEDeu5jIHkGq7qcKYbgeM_AuiadYjJp2Siftxninusg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از روزی که نیمار باعث شد کرک و پر امباپه بریزه:) خودش هم اصلا براش مهم نبود ضربه رو زد بیخیال رفت. امباپه اون پشت داشت جون میداد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102285" target="_blank">📅 21:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102284">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8732bd386a.mp4?token=uMehRA3Yuo07YJxdle-nVehH3pmPpBeKMtNE_8SLpqquTfZ3FjS0cC4m_HmECDzB85Yv_VlIYpzqAE21v1gfnWiLuyyz7av0YqbTGRoJFdOtLQfiPDyw71r3ZINapUFF3vUQ17IR6rmrnesPeGVebRplELJpAjWYAr3bobMHKANMUb8xfhHmFK8xLZZkW2ZpDN8VQFeOqp7ek5n5-8kDOt3RwvHOpqh21DYCyLfrJWk2ohYu_aNsM_vtX2Ms_UQw2AnlI_KLbvIqhsGISyrB7Qkac8vHCQIp3FD2BuhMLuxLfeAhzcIRpngNWsOLDhqsRgfIAvzRWVXmRPn_3KUmCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8732bd386a.mp4?token=uMehRA3Yuo07YJxdle-nVehH3pmPpBeKMtNE_8SLpqquTfZ3FjS0cC4m_HmECDzB85Yv_VlIYpzqAE21v1gfnWiLuyyz7av0YqbTGRoJFdOtLQfiPDyw71r3ZINapUFF3vUQ17IR6rmrnesPeGVebRplELJpAjWYAr3bobMHKANMUb8xfhHmFK8xLZZkW2ZpDN8VQFeOqp7ek5n5-8kDOt3RwvHOpqh21DYCyLfrJWk2ohYu_aNsM_vtX2Ms_UQw2AnlI_KLbvIqhsGISyrB7Qkac8vHCQIp3FD2BuhMLuxLfeAhzcIRpngNWsOLDhqsRgfIAvzRWVXmRPn_3KUmCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
نذر سفر؛ سهمی کوچک، اثری بزرگ
🔹
در سفر اربعین، اگر صندلی خالی در خودروی شما هست، آن را نذر یک همسفر کنید.
🔹
هم‌سفر شدن با خانواده، دوستان یا هم‌مسیرها، علاوه بر کاهش هزینه‌ها، به روان‌تر شدن تردد و کاهش تعداد خودروها در جاده‌ها کمک می‌کند.
🔹
اربعین، سفر همدلی است؛ و همدلی از همین انتخاب‌های ساده آغاز می‌شود.
#چشم_به_راهیم
#اربعین
#نذر_سفر
#هم_سفری
#سفر_ایمن
#فرهنگ_رانندگی
#سازمان_راهداری_و_حمل_ونقل_جاده_ای
#حمل_ونقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102284" target="_blank">📅 21:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102283">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poMGl0vDTcBVx2g4sZdiL-yF7u7bxi-JjXXc1GXdRw3hqTKfzzNB0yYpE7SNEeZI7abQM2pn53QcgZ715KRYx3cgmIf5r2nfc37j_nK5KSWbs7YUd1nEcbzwXN0IDs3GPBr4t8QPRkTVDM9Y6rlyLXZJDrElpkunIjmuChIDjzATV5mqh-PDzksS8JC78JxtGk1k5ORkxfclPyNudby1N2heJLB-utaRpKRuYT27-bz_M_yaIQ88CT2AlRrMkPobvvcpbqcQJligQxP7NFmDZ9PbdELC4PbwhrL6-FSbiMYkhbJXDWPcqqqKb3mrveuPfEL9xJCLeS8TZhFDdGQ9GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید جورجینا که بسیار هم پرمحتواست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102283" target="_blank">📅 21:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102282">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkW7nuDtIcm4lsJ478T4JAOwUN67n4BPI9wERkSU1iqBk0a29-AO7z5r9SRlbEmPSNvsl-hqYunTMCYniYSLSAtqL5J-_75U0UC3BQIfte5GbVvLaW4pJXyB2Ryg2zfS0t2HojvcySTYaXdxAZ6Nfrvx2F0QmKIxpMef9eOHn_C_nlcib4jghS_uiGCO2-ekvTc3JioMXUFddvJZq0VigBLz4MTN3TjRHyadjTMoMTn5FQ6nR9P0sUrNTwkOyA3U1DsQ3lmI2NmQA3NZ2FGi7tt9oQ5MhRj6-_1D1T2C0P7UHaCVMojACdJXOFxmZdo7NUruTIQoVf5fTEwhvTkjKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔹
کریستیانو رونالدو از زمان پیوستن به النصر تا الان حدود ۶۲۵ میلیون یورو دستمزد و پاداش گرفته!
❗️
در کمتر از ۴ سال، قرارداد رونالدو به یکی از بزرگ‌ترین قراردادهای تاریخ فوتبال تبدیل شده:
✅
حقوق پایه (۳.۵ سال): ۵۹۵ میلیون یورو
✅
پاداش ۱۲۹ گل: ۱۱ میلیون یورو
✅
پاداش ۲۳ پاس گل: ۱ میلیون یورو
✅
دو کفش طلا: ۸.۵ میلیون یورو
✅
پاداش قهرمانی لیگ عربستان: ۸.۵ میلیون یورو
💰
مجموع درآمد:
حدود ۶۲۵ میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102282" target="_blank">📅 21:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102281">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1795b5f8ad.mp4?token=BfTAIO__1o4fXsH0I9N3FI7Zh1zxwYlkRcG5DS3u9aUGHbrCIRlVsqbUSu4Sps7t72F4zGoD8NtBNrMU4d8QDXYoa0Q9y6MeToQxuQDjC8-ry36Xu5JOph_-OjlNxYGMc7f6ynKjmUf_ojPE1nb4cnEJhnJ0PQzScNiyLH7JAQoWmkEmll-w8_OStJbDGQ0LO3kbQH9NtZOF3Z1iD7hLYnaCBUwBMVI4ST08c5IX431d0Yx7Sn8_5OLpK-nyKbOiApubfxXV6XEv6LTcdEgTWEEegmGFiY05cwA5EOySy1plB_JUo7KhYVvShLfcMa5gCil3QWcnztM_H0HIC2DrUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1795b5f8ad.mp4?token=BfTAIO__1o4fXsH0I9N3FI7Zh1zxwYlkRcG5DS3u9aUGHbrCIRlVsqbUSu4Sps7t72F4zGoD8NtBNrMU4d8QDXYoa0Q9y6MeToQxuQDjC8-ry36Xu5JOph_-OjlNxYGMc7f6ynKjmUf_ojPE1nb4cnEJhnJ0PQzScNiyLH7JAQoWmkEmll-w8_OStJbDGQ0LO3kbQH9NtZOF3Z1iD7hLYnaCBUwBMVI4ST08c5IX431d0Yx7Sn8_5OLpK-nyKbOiApubfxXV6XEv6LTcdEgTWEEegmGFiY05cwA5EOySy1plB_JUo7KhYVvShLfcMa5gCil3QWcnztM_H0HIC2DrUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریوالدو، نابغه‌ی تمام‌عیار
🇧🇷
🔺
پای چپش چوب جادو بود
• هت‌تریک تاریخی به والنسیا؛ قیچی از بیرون محوطه
🔺
جام‌جهانی ۲۰۰۲: معمار خاموشِ قهرمانی برزیل
🔺
وقتی رونالدو و رونالدینیو تیتر می‌شدن، اون بازی رو می‌چرخوند
🔺
توپ طلا، قهرمان اروپا و جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102281" target="_blank">📅 21:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102280">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RImcj2Bqm1eWAC0JXOShx2RYmxPB7xZereJWHLKrB18vgy9_Q7S_5D69mKmGOd7otSL6HLnV76TrHmFaYZMCvYDOCgpWY4IpIy7X9lVWmKDrhmSLWSqWNMO_haQH4YQUesVzqGEf-Z5Po2MDcUUdTULux0DstXYkjnAunzoLj8-59sk_Ei_0xooudjFeAvWCGNeXmOKUz65jcZ-a-cecdXq_l7EmxSpKkxF_frX-qKWqlKZ_FzZvlV5fNWrTr_G8Lbir12j7nfAMTd3TfDjU3TMcgkeUiRnp9DulO1PbE4e8gUsthQGQq94LFGYWN4uf1twuz1yk4tE326fTxvDmPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اووووووف کیت‌جدید منچسترسیتی رو ببینید که قراره دو سه روز دیگه رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102280" target="_blank">📅 21:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102279">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFsllu_aWaGfJraiY1YePoj9hwiC1ujNRmx7Aqv9MUoXcnhNWXgyrtwTT3B0LQ02F-GGNSFejqz5RDXLN0Aj3cxoppHtNROLavtUOUr_A6FVlXwtvWsG-M3zFUvI_w_qLZiaiEbzg_WwEFEXC3i5158xFKjJTjqN0BVCrXHmcgdj6NElsjvpaj1_8UbmWfTz8k5G3P4DbMOQSgijRjQ4R9ZE_AGwMg6CpFQehj9FlqQxvdTIg9rLRucq4RdutRHq_TFpeOr0d9W0xFzbxk2FTEl8GBg2wwdSL25Nc7yg2DwEiu3l9DBOGJGTG-vXkpfdJsEMQyypwKy5yWlY9RIWXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚠️
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#
فوووری
: رسمی: الی جونیور کروپی گزینه خط حمله بارسا پس از شکستگی استخوان متاتارس پنجم پا تحت عمل جراحی قرار گرفت. مهاجم بورنموث طبق برنامه زمان‌بندی ریکاوری، انتظار میره ۳ تا ۴ ماه از میادین دور باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102279" target="_blank">📅 20:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102277">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s61wj9Z3Izy8_9OBx7vcXKq7MRzI2ebGG6zV_jJf5XRsW0Mpv_Rt9QEPJlsxJGjtlchB29wRSGr8mUwJUikkbINsKoe11ExNLNM-LjkBm0kWJ6yacgrsXe_9Mr8HM0T526TsaYbjOrlJrn26w2k6lHg0wPu_vEW4Cx8bqbnR6PH1KBKQMr0iVzsDDZjA2HO11sJIhtPiNOH_8b8xxJD_TafY_44FFrgY27hWW-YJop6JH_gI_RqcecQfNrnttYTKV48V9vL4vo1LtnNi9dvqUdI-dMFVHCJ6HbcuWPpN1TxBEfppOHj4nIKjMkyolGsiDEwzdwdE2j0S8a8NwGfqnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PmK6NO3azIP2YRzeJnzh3LvKDqSfo8_Oe3USlS9W-puhXbITrwZYLq-v1D_sjD_suV9vqqob3-WNKXo3wFnYxA06qcyYgUshnulTpA1vaD-0YQjvdDBrfxwfb4KfhSHvfojTpNIPRLG1vo9d7e9JBWkRvNuhSOKSDf5qBavlNMLLCUyLa_xxybPfYfAGqFCuLxmY96IVhugQKyUz53CNU_e-xImCLzj5TnAVeTIHP4Ytz9zzA5e49622s4k2rmiyOsjC4Er1zc_i6s4dbE85ZUxwIcZtGsBD2k-BWhSLcUwFPQrTD6lxIPDC5JStwrezbzy7OidkjpLRo3DlKSJgvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
طبق گزارش‌ها، ویکتور گیوکرش، مهاجم آرسنال، ظاهرا سر یک ماجرای ۳۰ هزار دلاری گول خورده؛ گفته میشه به یه مدل اینستاگرامی پول داده بود تا برای دیدنش به لندن بیاد، اما اون به‌جای انگلیس با پول رفته یونان و حتی یه عکس فیک فرستاده تا نشون بده تو راهه. گیوکرش میخواسته این قضیه بی‌سروصدا بمونه، ولی ظاهرا اون مدل برای دوستاش تعریف کرده و ماجرا لو رفته. این اولین بار نیست که زندگی شخصی گیوکرش حاشیه‌ساز میشه؛ قبل‌تر هم شایعاتی درباره ارتباطش با اینفلوئنسر سوفی رین مطرح شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102277" target="_blank">📅 20:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102275">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3bplRnH8Gk3Bb-Vagrky6iFLOMNiVqTd12LkyjOQK5lnCPRf-ya1zp-tRDJXkw5SUaPf0EexFyvFPfdURvKeYp4y01ilmeqlIJy_icwrLfHIm-hxTDwCYg26aFr1TF0y9-qmZ8MeQ-ZpGMlFe12YrKKbSBRjqFUwo3itaMTgpgzDXNW6OlPcJN3fuBnh8a3sib9mZy_ngTyF2U7U3VaG7N-iqGS05a8kErVGyUlcLXcOfiVQT_jvGS_atouXLZfr_7xW00I-vdRPkhtTWgkkR3E9Hnx6V4I7vgE7YkFp6XgJ6J55t-MYp126jyiCqrNeCwvjU_Fu9jEWa4b-tbBiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rtTuNOUnRROhx48hu9CREQUMxufDgCE64leS-Vh2t3TLdoIpmKNsCQLPOgfLddTMKoytqhxWkZIveZrgX-IvlUpqlFy8hilZ_RRCRvp6TDxvPaw4ZI2yAjbbePPWcSCUPGI9RwvJDFNcC7eiOzVRrunppb9t0Gi4pm0bjZG5QBn813ZsfbH7oiX6WmyjNd_JzgD5NtYwyODMAtwVTw6jXExWp_vMY4kWPCKwZjvBFz60OenPR2Sw_wN1G5LO1vmYAui5ftT3D9aYiatqqGAA5sKmFgDdlljDq03O_RgkAPcfYmY9P-63rDQX9k30qFeQpGMKUr3BbkFiF3IpXjc26g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
پپ گواردیولا درباره لیونل مسی:
من جام‌ها، رکوردها و جوایز زیادی بردم، اما شگفت‌انگیزترین چیزی که تا حالا در زمین فوتبال دیدم، لیونل مسی با توپ زیر پاش بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102275" target="_blank">📅 20:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102274">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfaTKOKYE1KT6iQSQm4RRJZDQizDT-3jGnqzdPLyGhnVXyW4xcVx-87GCGlJOuClhiNtEHTKHFplJLAO3DIhz8ew2kD8ewfUjojcl8JRn8zcB8SJNWftpecdREHhjV-_nEAziK700s_KuSG2LOpKsQlOEQRuRFM-f-ZB8O9GgVbCnAOdOIkKzhxhXwoUdg1Kg3i54o_4m8NwfGOHsufw-OvDCt4ABHBCKclwNmLucuLV8NF-dtV5KOZVZpoNxtg85Uwm7Q0DPbsBx-RCxN7jRCBtZbEnMhfYG2ZwSnVnGLzVkDEAuq1Eow5qNgwcsxsKYHv3US1AUWeo-2Ya2g2xzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
#فوووووری
از رومانو: بارسلونا به طور قطع نظرش راجب فران‌تورس تغییر کرده و هرجور شده میخوان نگهش دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102274" target="_blank">📅 20:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102273">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hg-EnSST8Uv5bNbBm4k2baeCCzaQLApDI430NKaA9Ztvj8YTqi8OoxE8TTN65IKwBSFu097jVLMrJkqbCXymyc0pXnxfmWXn8yiHZ8l44ecEb00yfsdOSVFGIhcQyxcDJygima34AFlmIxPt1DT5xqOx_vibxzRWAYtWaqPWmCLBpUODpWzH-CaP5q-VzylzPUS3n5lLZdtVt-7_Ju4hFTFCEsOm_RCSVRl2KQAcq0WlpQT4yrYJNwhCbhybHtJ8oLuid1yYfIK5musWZBdquB7gAj7KbfxqQfF00F0ldKY3gv9Zm-ozTMLeN1joQDgtUZ-5QeOV0EqhBwd5nR5GZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس کوکوریا مدافع رئال‌مادرید
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102273" target="_blank">📅 20:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102272">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84ff90fced.mp4?token=p1q3wxaBkZj5ANJwDCDntWMQVIGzhGu2yO6MvkF2nAOnrwqpLLigJopIEh-ULkPYxud4-sAQfbVPXqncpHLWlK5S5COd9a5iQp_gDsn2XZXX0XE8-T-GIIHbVC40mGkidyDWnD6UytMfJslPE0d_AnGcQsP5gou3G9Xxr_P2_SmBEq-r2G2z_T-3ZQmxxuRVsD6v7Y4j9chmPXuZZmvhcOamho_LnieUdUTN-FmxRMVHxUmvDZ1tN3wxQ9XgltUaIanyOnWuzhROlCNVqjKCzi13Sk86QwMWyokJ5F6nK1NbVUa-B1S84jkHC5HsVd9Fl-Gsh4khCEuI_7Mhd4dfhKNuq-yoMoZ48MviWuP3PlVLMgXW1nXhGoDivBO9sZ12nQlrDm1Nu8G0NvQKiJFt_xqslTB6K3d3wbN0Z21UTBTzpGBCPJhIVOsrOrtvD6RAqzMFiJxrfVbnOiEbAn_Xaubwx9-QDSeE0RwIgAMltrUsEV2Xjg2r-AkXyZner3SazJZYyJBikh1fYUY5-0iWR-wPKcF740ezmW_0MGX7ak9CpWYBKFPjRyHTrwMMQzY9tEniQ7BEf0wgIqwF9yhydfEG9JpbsSHfbWiSgLhVbNuUa9fH1Nwe4X7zpoTBB4r6GRw_jkjC-zUKECFy0tL3Cv73rb8XXFvPv-kB2nEO6oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84ff90fced.mp4?token=p1q3wxaBkZj5ANJwDCDntWMQVIGzhGu2yO6MvkF2nAOnrwqpLLigJopIEh-ULkPYxud4-sAQfbVPXqncpHLWlK5S5COd9a5iQp_gDsn2XZXX0XE8-T-GIIHbVC40mGkidyDWnD6UytMfJslPE0d_AnGcQsP5gou3G9Xxr_P2_SmBEq-r2G2z_T-3ZQmxxuRVsD6v7Y4j9chmPXuZZmvhcOamho_LnieUdUTN-FmxRMVHxUmvDZ1tN3wxQ9XgltUaIanyOnWuzhROlCNVqjKCzi13Sk86QwMWyokJ5F6nK1NbVUa-B1S84jkHC5HsVd9Fl-Gsh4khCEuI_7Mhd4dfhKNuq-yoMoZ48MviWuP3PlVLMgXW1nXhGoDivBO9sZ12nQlrDm1Nu8G0NvQKiJFt_xqslTB6K3d3wbN0Z21UTBTzpGBCPJhIVOsrOrtvD6RAqzMFiJxrfVbnOiEbAn_Xaubwx9-QDSeE0RwIgAMltrUsEV2Xjg2r-AkXyZner3SazJZYyJBikh1fYUY5-0iWR-wPKcF740ezmW_0MGX7ak9CpWYBKFPjRyHTrwMMQzY9tEniQ7BEf0wgIqwF9yhydfEG9JpbsSHfbWiSgLhVbNuUa9fH1Nwe4X7zpoTBB4r6GRw_jkjC-zUKECFy0tL3Cv73rb8XXFvPv-kB2nEO6oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لیونل مسی:
آنتونلا اجازه نمیده داخل خونه با پسرام با توپ بازی کنم. تناقض‌های زندگی همینه دیگه! من از فوتبال پول درمیارم، ولی حتی نمیتونم داخل خونه فوتبال بازی کنم.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102272" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102271">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRZ6SacYWp-hXoO-xDyDGRiDhoECYu13V3GBAlC4fczEiYGJIR0k3IHxnpzz_LQ0DkOLXcexyrihgsoIPVkUp_QNYJSg7wfo3t5XzaQK--aczqaGGoTYJKjChaEA-D-GAFm036l3OCJxDAd4SgPrrWz7rbV_nmeXKIRPjvW1wSFkc7ExsWFD0d6GOtgA8u3qowlm8av8qDjwNK_Tb8Av1pvR5pZlZhf3bh0yx2dwu6rl6um_nEeKJW1lc3ilSVHo3bLQBB_k7EUjz9GVfPt-AcKd5U0BPmMwPtJgR_TfM3ZHUEzcAR80-gqaAwTM2Mp1CHEae4TeCJMHOMq7-soLFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✔️
⚽️
نگاهی به اسکوربوردها
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102271" target="_blank">📅 19:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102270">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f57a7d2d3f.mp4?token=p98_wDVzPV254LtaE1efvERhrJiw10Mcd1HCqLNvfIR2WkIS5EoWGyfluIkeuA1EMLQjbH6I88A2xFCt2boCcMU5KYOcLXXK8OCcdFyaxSMFb5HrmxTLv8YNPjo7Pux2-zuFWy6AJzys-4lH8zdpYFgR1OrH1LIA9N6vLYGofDHO5TtXXcGEaTnDLYCbcl3TmG8gUDzau2OJt5UkZiF8z3uBqRjg4-pJHBLzvDb7L6uuIXahVJEkzx_D06mK2bpDbMmwcvoBG-tNFmlRpiOrLjhxUo5K6OmgnTfwDIWe9tKKv5DgJckN-A2Td3PTnQdoWMuY9TxK_FHV458LnGo0Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f57a7d2d3f.mp4?token=p98_wDVzPV254LtaE1efvERhrJiw10Mcd1HCqLNvfIR2WkIS5EoWGyfluIkeuA1EMLQjbH6I88A2xFCt2boCcMU5KYOcLXXK8OCcdFyaxSMFb5HrmxTLv8YNPjo7Pux2-zuFWy6AJzys-4lH8zdpYFgR1OrH1LIA9N6vLYGofDHO5TtXXcGEaTnDLYCbcl3TmG8gUDzau2OJt5UkZiF8z3uBqRjg4-pJHBLzvDb7L6uuIXahVJEkzx_D06mK2bpDbMmwcvoBG-tNFmlRpiOrLjhxUo5K6OmgnTfwDIWe9tKKv5DgJckN-A2Td3PTnQdoWMuY9TxK_FHV458LnGo0Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚽️
دریبل‌زنی در حالت عدم تعادل (Off-Balance Dribbling) در FC 27
.
این ویژگی آن‌قدر اعصاب‌خردکن خواهد بود که ممکن است وادارتان کند بازی را وسط مسابقه ترک کنید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102270" target="_blank">📅 19:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102269">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7495121486.mp4?token=cc5Q7QoXUNhu52NcSyCyAlvKoD8GjIIOXLYCsxXaedhEhlrnhIz_dDToFOgNXn21DjP1kygMMUkrwINhMOtccR9-idfw_XpwbKdZlSySxtvZJJlBg_ktPpJTdEAYFVBdNT3EGIXeMmORtA-A-P7acqrJUI1JTCn9fWdnHNhuWjSvRmzIxkmki3RjYo7xrsTvF0uOuvo0Cyyt-KgBxHZ9tG9R1PKyjuuLMi9GnYq3IWA0yEpbAdrB56AtOSYAKEpitcijIloZkqzhw1BHegUzTnBDHdwV18yJh3R2XHyYZfgSDPH3HnjlnKEKu2T_-kjh6bWb2up2u4x_T17pah9CGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7495121486.mp4?token=cc5Q7QoXUNhu52NcSyCyAlvKoD8GjIIOXLYCsxXaedhEhlrnhIz_dDToFOgNXn21DjP1kygMMUkrwINhMOtccR9-idfw_XpwbKdZlSySxtvZJJlBg_ktPpJTdEAYFVBdNT3EGIXeMmORtA-A-P7acqrJUI1JTCn9fWdnHNhuWjSvRmzIxkmki3RjYo7xrsTvF0uOuvo0Cyyt-KgBxHZ9tG9R1PKyjuuLMi9GnYq3IWA0yEpbAdrB56AtOSYAKEpitcijIloZkqzhw1BHegUzTnBDHdwV18yJh3R2XHyYZfgSDPH3HnjlnKEKu2T_-kjh6bWb2up2u4x_T17pah9CGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚽️
کرنر ها در FC 27
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102269" target="_blank">📅 19:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102268">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a87aed54.mp4?token=N0oY5SC-gESTC_OW01xoaferUNdP8fscExyyD6CDBPSijCfzEJhGg1Uu59AKahp3JRGv9-S_hdpgNRPhKvevKI8ZxSUCyw6eULP8YLrB5q7vRhONUQInWCSPHEPVxXJIwpg_O7Cnuyp2RO3dISfKZSQzqjmSdoVPsd9RFdEJTtstXP3CNHVmkLxxUyHj8gtxSgkTEM9M6AFL10KJIFSSQ12UI2VzYIHa6Br9AgztMrf6cvMpUdhOvPe-q9uWjKdsZT30LOsz1tfouXZYojaE5Fe_n66zJ-UW_pq4uWsqeIDHN6D0k_86qkVbvbwJw_6p2o_xPRmaGiQyYassN-IneA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a87aed54.mp4?token=N0oY5SC-gESTC_OW01xoaferUNdP8fscExyyD6CDBPSijCfzEJhGg1Uu59AKahp3JRGv9-S_hdpgNRPhKvevKI8ZxSUCyw6eULP8YLrB5q7vRhONUQInWCSPHEPVxXJIwpg_O7Cnuyp2RO3dISfKZSQzqjmSdoVPsd9RFdEJTtstXP3CNHVmkLxxUyHj8gtxSgkTEM9M6AFL10KJIFSSQ12UI2VzYIHa6Br9AgztMrf6cvMpUdhOvPe-q9uWjKdsZT30LOsz1tfouXZYojaE5Fe_n66zJ-UW_pq4uWsqeIDHN6D0k_86qkVbvbwJw_6p2o_xPRmaGiQyYassN-IneA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚽️
دفاع دستی در FC 27 دوباره به اوج برگشته است!
✅
‌   رهگیری‌های دستی (Manual Interceptions) بهبود یافته‌اند.
✅
‌   دفاع سایه‌ای دستی (Manual Jockey) بهبود یافته است.
✅
‌ در مقابل، قدرت تکل‌های خودکار (Auto Tackles) کاهش یافته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102268" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102267">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5128380014.mp4?token=qHQZEPGJKdNKQWOef0WD68wyw90OTOggIml614yIXUOJa5qLJi4vinGEdCGHpYp7_UqsnVTc74oTavO0eUq9yt-dQ0VTpAVNGPgkbWiQYO-2ivafLIYX3H7YPpBgC-Jw0zFKaCt4CojG4_vRLn1g-079HI_3rKily0BSa4PQeL1K3GWXytIpMeb8JV5i88LpPf9foTcWxZ53VVH75-_SYwqZBVfMaNxc80zL_c4dWLzC50D39yVBHSGyvmi5iqrXY9RmqYhzirfbpDGm14dL1peFaofFXFOILS10RRuQ4WceXfwZDn1dAr9GE_83HItKoOqoKAGGY3EdCGQps-XoMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5128380014.mp4?token=qHQZEPGJKdNKQWOef0WD68wyw90OTOggIml614yIXUOJa5qLJi4vinGEdCGHpYp7_UqsnVTc74oTavO0eUq9yt-dQ0VTpAVNGPgkbWiQYO-2ivafLIYX3H7YPpBgC-Jw0zFKaCt4CojG4_vRLn1g-079HI_3rKily0BSa4PQeL1K3GWXytIpMeb8JV5i88LpPf9foTcWxZ53VVH75-_SYwqZBVfMaNxc80zL_c4dWLzC50D39yVBHSGyvmi5iqrXY9RmqYhzirfbpDGm14dL1peFaofFXFOILS10RRuQ4WceXfwZDn1dAr9GE_83HItKoOqoKAGGY3EdCGQps-XoMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🔥
⚽️
#
فوووووووووری
و
#رسسسسسمی
: تررریلرررر گیم پلی FC 27 منتششششر شدددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102267" target="_blank">📅 19:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102266">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a8d0459b3.mp4?token=B6PGgilPWAJVXQGD-M1R8BsiwO6NaBUJ9F2NnM2REZJURIb5yynMML9Yapo6JjAr0DA6CUnIf0b3f-nSYJQVy5wfS_dYgCZPBTNvtQjVY6RRCXAALFIUkP1opVlH3eCMlZE7-AqdXGajy3mJIlM_AoPDstRizQxyWXoqPXgsF-tMFnO8NNL2wqYOzhd0lXig9fxKL_8dlr_wGAmvwxZbPyPjtzU9HhBQ749LSh_Dg0Sjn-GwqIicRivK8jl6EjoDG8wgA4Gi2r16JclaRtN4J__sYq2VI94AZjs-8_Qgae2grHnZzqTxw0n5BFTly6y9KyUOShuyfyT9oxpSi9hQBIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a8d0459b3.mp4?token=B6PGgilPWAJVXQGD-M1R8BsiwO6NaBUJ9F2NnM2REZJURIb5yynMML9Yapo6JjAr0DA6CUnIf0b3f-nSYJQVy5wfS_dYgCZPBTNvtQjVY6RRCXAALFIUkP1opVlH3eCMlZE7-AqdXGajy3mJIlM_AoPDstRizQxyWXoqPXgsF-tMFnO8NNL2wqYOzhd0lXig9fxKL_8dlr_wGAmvwxZbPyPjtzU9HhBQ749LSh_Dg0Sjn-GwqIicRivK8jl6EjoDG8wgA4Gi2r16JclaRtN4J__sYq2VI94AZjs-8_Qgae2grHnZzqTxw0n5BFTly6y9KyUOShuyfyT9oxpSi9hQBIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روایت جالب مجید «قصه‌های مجید»:
وقتی ۱۵ ساله که بودم، تنها از اصفهان به تهران می‌رفتم تا بازی‌های آسیایی تنها تیم دو ستاره فوتبال ایران (استقلال) را ببینم. در ورزشگاه یک سرود می‌خواندیم که آن زمان غیرمجاز بود و البته خیلی کیف می‌داد؛ آهنگ تنگ غروب سیاوش قمیشی…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102266" target="_blank">📅 19:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102265">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BODeRDPqm62jYDhmHgIbVbmvhn8Vb7pv78lwFFHiaQnHb8MVp2pRnAtANI78kqUaa0EY8V_pm7al96WQ_xwVrMH2Cq5mj1WInDkSkEJ3H72ByR_pT0iwExdUDC6igMmZnAKFYZqcAFNyyVpCrnmMx4PV2fmgOcY-VBloXBmRXQmDHE1c9dMwoqQQjKgAdA7LG0WRCZ0lPBhVCFNnSqZwKA5l9w-Ui0MABijmioSyh3uMxDpsXxEJp9l-3I5Lz5gs383gi51M2Q616NKrY_BzTeyZresKmVtvwXouhTd0S3aIH0Tlxxsaq_GeWPDPgeYyzrhs8ExneFvhFONrQZxDgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🟢
تلاش‌های علیرضا دبیر برای حضور نکونام در پیکان هم جواب نداد و ساکت‌الهامی سرمربی این تیم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102265" target="_blank">📅 19:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102264">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bcb41b861.mp4?token=m96Az0FnsRk54D4Og2X4dLwrpXk5aIyKKyrOKo3NlGBIX99bRWHqb_dtC8M1jlv2aGX4SRZb8MNhDVS8V5rT0hcya3Dyr-6RnvfANs67aGoitVUUEJrozovN7C1F-hMe9iCNtGpIMfj3Cn0BMHbEwxze9S2z2GaGDcy_Z1IOGtEyoURNwByT7YLQrj2NfdL92ECRvVUmZ9DsclWO2C_w62uKcdX0i3JBUTYv2Lv2LeK0gF3_2PR3QQtoZo-2roGEOBUNKpokEyqwi4WbrEKHz6PjYZQgLYR5U5VDry_AtHAm1G-EStBgo3FxdlDPHvmmGCL8wttceA_ynwcfs1S7pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bcb41b861.mp4?token=m96Az0FnsRk54D4Og2X4dLwrpXk5aIyKKyrOKo3NlGBIX99bRWHqb_dtC8M1jlv2aGX4SRZb8MNhDVS8V5rT0hcya3Dyr-6RnvfANs67aGoitVUUEJrozovN7C1F-hMe9iCNtGpIMfj3Cn0BMHbEwxze9S2z2GaGDcy_Z1IOGtEyoURNwByT7YLQrj2NfdL92ECRvVUmZ9DsclWO2C_w62uKcdX0i3JBUTYv2Lv2LeK0gF3_2PR3QQtoZo-2roGEOBUNKpokEyqwi4WbrEKHz6PjYZQgLYR5U5VDry_AtHAm1G-EStBgo3FxdlDPHvmmGCL8wttceA_ynwcfs1S7pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔻
داستان پسری که دنیا او را به حال خود رها کرد، تراژدی تلخ زندگی ماریو بالوتلی
🔺
ماریو بالوتلی در ۳ سالگی به دلیل مشکلات مالی از خانواده بیولوژیکی‌اش جدا شد و توسط یک خانواده ایتالیایی بزرگ شد. اما کودکی سختی داشت و به خاطر رنگ پوستش در مدرسه مورد تمسخر قرار می‌گرفت؛ حتی مدتی فکر می‌کرد با شستن دست‌هایش می‌تواند رنگ پوستش را تغییر دهد.
🔺
سال‌ها بعد همان کودک تبدیل به ستاره‌ای بزرگ شد و به اینتر میلان رسید. اما وقتی مشهور شد، خانواده بیولوژیکی‌اش دوباره سراغش آمدند و ادعا کردند می‌خواهند رابطه‌شان را شروع کنند.
🔺
بالوتلی با ناراحتی گفت: «وقتی هیچ‌کس نبودم، کجا بودید؟ حالا که معروف شده‌ام، همه یادشان افتاده من پسرشان هستم.» داستان او، روایت پسری است که با طرد شدن و تبعیض جنگید و دردهایش را به انگیزه‌ای برای موفقیت تبدیل کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102264" target="_blank">📅 19:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102259">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smizAtDP3iBPe9ERfeae74zh_RXTS2dqUvm1Kzry4jOP4VzFz2TjuNm8HIoYdp0kEJjz9Era7dMdGHZ_30MmN31R6mTU38gB8b0cf1gSG2PYaR4IdfUbasSezi05gxL69_AvEUYPYqg7ned8ozINDxI3FwvqvJakCRxlqagUJiAbfKAMqrCy3lpg100nk-0buf7br3ErwsxPP-mK4P-dJGn-A5LLGsZq9NLZBEKjj_RdQLW4NAVKOFzLiNiszFBBchUv-H_GX8mH5GeiMmxKG0RBrwB9_KS7dwG27LwXV1Ehq5Z6FL0G2UGjMAhRlT-OPNNLMoD7VwPejRHh26JqOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
می‌دونستید؟
چلسی در سال ۲۰۱۴ با ژوزه مورینیو به جذب لیونل مسی نزدیک شده بود. گفته میشه آبی‌ها آماده پرداخت ۲۵۰ میلیون یورو بودن و حتی با اطرافیان و وکلای مسی مذاکره کردن تا او رو به لیگ برتر بیارن.
اما مسی و خانواده‌اش تصمیم گرفتن در بارسلونا بمونن، چون این باشگاه برای او چیزی فراتر از فوتبال بود. تلاش رومن آبراموویچ هم در نهایت بی‌نتیجه موند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102259" target="_blank">📅 18:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102258">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b74b82c7.mp4?token=S3hECrXXrVo21L5IAiv2TLeb8Up23GZv_kHlHeSQKquziFVNxIxcG4rd3vUTz3m22LADzIjptucwo963NqSDSnZD5FAhcDvDPiPzxF42HzCb18Y6Kp6UfUroxPGo2_J-qFs_hPIp5Yg31yteMOG9R8B_ay6nBjPd2GmOYZFJFtx-vNNDQMkBQit0Z86kwU6ZV9jIBkCklS6pYbUsPS8MLv_jfixVB1U41cviqeOhUQM3l9i50ahkRQXLCRpzj1cXQGTaMzKvkbi8BKm321b0HRCfBVU6cQyWZRLLuE-czbx3FCpKq4T2H5K9pQji04Q6nioAIx3dst17KkKY30JgSBwp9sX4wMjqsomMm_57_eLwWXjOsb4g_Rz-cyV412guKzOvE73nRrf3sO3PDMMzuK1afdFo4N8jx4hv6Hz3v9NWa_0yZhO1hhQF2PaZpvNoyfaNax-oj_ErT9HGWujHaR5I19YaP4QOQRly4nxprNbuAUVifrAorjzN0hJFWoPhJyCaLfccpRtyLyAF4sAus_C0Oufg2_ZptaUYrWSLRzd4nllSfojj166lCf57LBTaxd6wUPGjBKNX4Efso1eFhZ19IaApbBK2uRymZQS_gTQni8LXYTehx2Tqlf8kUWy4PrsYj8uzRTluyD2FwdCiQIHPkdXCuBQBKK24sFYky-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b74b82c7.mp4?token=S3hECrXXrVo21L5IAiv2TLeb8Up23GZv_kHlHeSQKquziFVNxIxcG4rd3vUTz3m22LADzIjptucwo963NqSDSnZD5FAhcDvDPiPzxF42HzCb18Y6Kp6UfUroxPGo2_J-qFs_hPIp5Yg31yteMOG9R8B_ay6nBjPd2GmOYZFJFtx-vNNDQMkBQit0Z86kwU6ZV9jIBkCklS6pYbUsPS8MLv_jfixVB1U41cviqeOhUQM3l9i50ahkRQXLCRpzj1cXQGTaMzKvkbi8BKm321b0HRCfBVU6cQyWZRLLuE-czbx3FCpKq4T2H5K9pQji04Q6nioAIx3dst17KkKY30JgSBwp9sX4wMjqsomMm_57_eLwWXjOsb4g_Rz-cyV412guKzOvE73nRrf3sO3PDMMzuK1afdFo4N8jx4hv6Hz3v9NWa_0yZhO1hhQF2PaZpvNoyfaNax-oj_ErT9HGWujHaR5I19YaP4QOQRly4nxprNbuAUVifrAorjzN0hJFWoPhJyCaLfccpRtyLyAF4sAus_C0Oufg2_ZptaUYrWSLRzd4nllSfojj166lCf57LBTaxd6wUPGjBKNX4Efso1eFhZ19IaApbBK2uRymZQS_gTQni8LXYTehx2Tqlf8kUWy4PrsYj8uzRTluyD2FwdCiQIHPkdXCuBQBKK24sFYky-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔴
۱۰ گل منتخب تاریخ تیم منچستریونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102258" target="_blank">📅 18:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102257">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6xRZrrsu3LXNvx4bL8hZPqtb4TO2pvMUKZInN4SFHRamFso-1H10gztGZrWI6NfT6OEnk4AJBc5hUTdCghtaO0D-vfL2e8naqcc7tz-rEe1SbbIG1N1B5ciQ1Q6UjvKARY9NkzIRsYKkLl7GjbnYNBv_mnHPaQTkd0u--L1EoUnfHyuBcXAFd8fOFtuzRpauKGlJwLrX2gImD3JPalnGLulNltEWc2S1-Kb8giT5BkGIld19k5Sd0xwRYZ5O08JgMwjh0dvvZcanpNeCm9hEoGkZvtVoP7l5RKy3bLiyAqn_1GAL0Yc1hJMBt3FPNoGQmssdLlnOKgW0qkNtH9-2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⚫️
#فوووووری
؛ فلوریان پلتنبرگ: کریم آلبگوویچ ستاره تیم بایرلورکوزن با عقد قراردادی به ارزش ۳۳ میلیون یورو راهی یوونتوس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102257" target="_blank">📅 17:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102256">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxhoWR0WWf0pptR70czbIoPCo2wITRXDXEl7G_LkyyJYFAe8kSpbtdhczJUm8VpFeNWAdmwX21iTaMRu7_0uTse3h6HEUqJziSHCgQ7P9pGsoIZSDWFVq7JZlzAeblZ6xDsCeMZEHB6WW-iTt_7dlswECBM_KHdxbVOrIHfa2Y76QJuiIV6J3WYltMWO7dy3bw_mHNk86BN_2jF7JHL9KSbHyFC9_r1rYXZP5ZRLDbs7DPcRBznMOeX62SIbbeQZH3btLO_0SKxdUZ_ovlJzwnZoTM8cxhHGF5Cy0aT648HyN9dlDS8iUYLG-IgL5E9hun-lAnhgHc1rkV56sQllcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
رونمایی‌رسمی از لوگوی جدید فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102256" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102255">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IihtgBgTpFXRve_h8VvcwSj76pvXFdvoPhBsCc5xnmBXYHnSZ1eA7QU39UtVABsHsiUU85Hiv7h4dTkBOExW5rXdi83WV1UHhfTj8wijvC8A6ZIeXNVDZhaf93L0433OMrkzG0lPTjCgIJVEma4fm8tu-pYPagVsAMY21NAWpKPajmZsw5-H3zgItWx5O6KBbaH6lDK-wJPS8TCBlwnq5SpI5Dje9PMpOhXUsoeVZdZFyYnpmwuPuTCTmv5JTq7QWJLukjDQytZFT7HT9apnXTp-vuwg3VQnLIW1Eof_2yHe5QexkibgX40vbPzETqAj9mxz7Cgf7qcomi3pnPwusw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚽️
مارتن زیگلر - تایمز اسپورت
🔻
جیانی اینفانتینو، رئیس فدراسیون بین‌المللی فوتبال (فیفا)، قصد دارد بخشی از حقوق مسابقات جام جهانی را به سرمایه‌گذاران بخش خصوصی بفروشد.
🔻
مذاکرات با سرمایه‌گذاران و چهره‌های نزدیک به دولت رئیس‌جمهور آمریکا، دونالد ترامپ،…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102255" target="_blank">📅 17:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102254">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d715de39.mp4?token=u09rJruljSEHI2rsRrUPsCfLxHW-59mhrG9nLL4dwhBSs47fx9X0Z3sil2QhjFoq6TwipJjgJdlDSbQ993fzoQQtQuvgaDtOyqVx1KSjzWZZ5Ay8ZErwLosYruLb1iR7Detdl0oz7pWDMDcyHvRaGt88eXpO-HOl4Im4b1A2iZap2XYcxCoN3l-8B24mb7sf9VmySHQIzKnpAVFZub5fP4s7FrIvLMoOtMpTzmG51Y04gY0CeXDFOe_u-Y8x3CkuOB44kKJ-ZfKrFqc4bMDNBr24uC6hceDjVQ6KoBfqbnM-rzS-itjKva2xIUwZ3P4oVqZqWwQKVMHjSDfFvKStkhl2ATtS3x0-phSqtrvWVMuOCjshARRYBslvEBBdj3gkW72fPVieuUa3WsacYqOGGBlc4-tFZLqbohyPsmH14ffj-V5uNynDvxS__8jfrlXJLai95649hy0wo-TltQd_N2mKDyhx_6BpBMw3IfNhe-PZpzzUOcWtpvnJQPGtQ9x0hM4tC1pMFd0Ww4Lt5gsy7KKMntHb70yaCCHAPTrRsWaRFtcqSwZSQaRv-Z9MTMD0wcyBJQD5NNspO8pLViyF_0jWa9S_GHgXvWYzx64QkBSN41aIyOhJwXCDihnp38DljQJPBTwmQPLGipumr47rDE3zVazgOMN7y2RkUeLJLdE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d715de39.mp4?token=u09rJruljSEHI2rsRrUPsCfLxHW-59mhrG9nLL4dwhBSs47fx9X0Z3sil2QhjFoq6TwipJjgJdlDSbQ993fzoQQtQuvgaDtOyqVx1KSjzWZZ5Ay8ZErwLosYruLb1iR7Detdl0oz7pWDMDcyHvRaGt88eXpO-HOl4Im4b1A2iZap2XYcxCoN3l-8B24mb7sf9VmySHQIzKnpAVFZub5fP4s7FrIvLMoOtMpTzmG51Y04gY0CeXDFOe_u-Y8x3CkuOB44kKJ-ZfKrFqc4bMDNBr24uC6hceDjVQ6KoBfqbnM-rzS-itjKva2xIUwZ3P4oVqZqWwQKVMHjSDfFvKStkhl2ATtS3x0-phSqtrvWVMuOCjshARRYBslvEBBdj3gkW72fPVieuUa3WsacYqOGGBlc4-tFZLqbohyPsmH14ffj-V5uNynDvxS__8jfrlXJLai95649hy0wo-TltQd_N2mKDyhx_6BpBMw3IfNhe-PZpzzUOcWtpvnJQPGtQ9x0hM4tC1pMFd0Ww4Lt5gsy7KKMntHb70yaCCHAPTrRsWaRFtcqSwZSQaRv-Z9MTMD0wcyBJQD5NNspO8pLViyF_0jWa9S_GHgXvWYzx64QkBSN41aIyOhJwXCDihnp38DljQJPBTwmQPLGipumr47rDE3zVazgOMN7y2RkUeLJLdE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
تعریف ژیلا صادقی مجری صداوسیما از بازی پژمان در عشق ابدی !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102254" target="_blank">📅 17:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102253">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dtfvu8Bj58-fgg2XCsQxxVFRT84UJuaWn6GoVSU2JHNpPH1ebUFjVvWQgtHa4OD4HT8RlngJdLhJBcoM-gN-M116FyghdEyBCmQdP7FF4BKJ1V3Ot4s28hgzw4LHIY5t2c-kyeWBF9dw5H5l8nD-s0KvOScRb0mQXkc0y8LYjzQkHxOrBbZvlGZIGrug0japv_wsDrkULY3m74dYP75zV3sNDO6-lpuQ8PZTj6kpWZVHhhMK89KGo6ANnaL6tv49tyfqBMtFGYS-t59gXLeezd2K8uG_OQKTxsKu5eHXnR7hiJm6PKZFNCp6Ulb30EQq8h3n6k_LNomwgB7y2NERCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
از فلیکس‌دیاز: رئال‌مادرید به احتمال فراوان معامله رودری رو فردا نهایی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102253" target="_blank">📅 17:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102252">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6KiVeQ3w0XB9uLxTp6ZtS5e8QkNIfexyZ51XEWx4ap--vicxz-JofuKjnxydCGx1K1hmo8WsXh6n292HwCKIEMM0yfy7p5Qf2-tPUWkibWNAT2MLDNnfOX76sJKuq26CMI3G_bRa8CrDd4q84udvWl-PlMcYybheFaja0MinK9l4oCPTXktIy3DEaYK_vmSRhXEddd8_HpABbpTmd4MFMbAQ1S6kaP1hl-RB_L40rFqM6ngFSfhrjSCk1DOSyZhtwRLeBQHXNDAb5KIyucbNksBz2mzOzUhvFufvmnHMAHgQibhVbWAlKmzc1usdetAR3reH_0vpd5xj0ro1eqm7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
ساسا تافولیری:
بوعدی با منچستر سیتی به توافق رسیده است و قراردادی تا سال 2031 امضا خواهد کرد.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
🇫🇷
لیل امیدوار است که 100 میلیون یورو از این انتقال به دست آورد، در حالی که منچستر سیتی می‌خواهد این انتقال را با 90 میلیون یورو به پایان برساند.
💰
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102252" target="_blank">📅 17:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102251">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXt_2dl_c77N_eN1ec5lc6-yS-LFL16SVsUZPjQ0p6DGnjnuSQXL8osnuRb-TB_ghIjsk_tyemERhOoNUdvpsDo_C1xVrw1e39GXPRzApB2AHyp-yGqB_52vFY_1VmBAAZbmxErBOAAJz3cgwPyXOCJeWLF8luhJnPLFn6ROP66X2NauhPg_pDMa9YJ266P2y4gZPzcqJeksz_Mx1Ic5VGAQMcS6AUuaB65OE728Lb8F1fENguydK9HuOxVSE_psmqFSsbNKorY4KHsQ8vh-Kqa2EYyf91LThqe--Isvi9lhVxl_Cvo-_uPc9UUBDk7S8n6BUWJx5FaSbyoFp9k0jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: جردن هندرسون با عقد قراردادی به مدت دو فصل راهی چلسی میشه
HERE WE GO
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102251" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102250">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb71ce498.mp4?token=NpZKKrO2IsSnchcGyPZ1yQMeneNTqYOYYfBY-E31R4F3W-9OcofFAdReUAEhnOEdDVax3q9vB-Nc1bJGKM6PPLpUbs2B_akpqB7yKdDdxj_WQrTDg5vG-m-q5DM3lwN_aAIThu0kZI0DSqdnRggjBHzazEdxqw8zn_ReHWgPVi4C7PsjkcLFdgIWtphYDCz5CKdVV7-1128VqtTndPctN7Ayja049cCJjFG3QUXFRa-Bdi-NEu3vf608TKOGkL9h1QaCXaW6xRHIA_v_o0gELTQcNyBMvxX6kcAJc-9scXLclu_ZkgdpXUkUEu4AbGHV8bkijSd0IxqzHHvFpB6Dyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb71ce498.mp4?token=NpZKKrO2IsSnchcGyPZ1yQMeneNTqYOYYfBY-E31R4F3W-9OcofFAdReUAEhnOEdDVax3q9vB-Nc1bJGKM6PPLpUbs2B_akpqB7yKdDdxj_WQrTDg5vG-m-q5DM3lwN_aAIThu0kZI0DSqdnRggjBHzazEdxqw8zn_ReHWgPVi4C7PsjkcLFdgIWtphYDCz5CKdVV7-1128VqtTndPctN7Ayja049cCJjFG3QUXFRa-Bdi-NEu3vf608TKOGkL9h1QaCXaW6xRHIA_v_o0gELTQcNyBMvxX6kcAJc-9scXLclu_ZkgdpXUkUEu4AbGHV8bkijSd0IxqzHHvFpB6Dyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
لامین‌یامال و زیدش در تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102250" target="_blank">📅 16:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102249">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ebe18939.mp4?token=Aer8UUGyyUsGkzTOu5wTf4yIAlhviyYOBF1DyCsjd06oMXIYVEGKMQvjZ2wQPXUlD4zjd58kdnM-kBeWxQbHVscPQwHLSSOyAJVyAiDVsf9nBrzbWmDLK0WCRSeZ2Wi0HISJdZSByaInNbG7vVlfCKID2RlhBubEyTYUMgUgxdHMGVuaiqH326ig88Lbs36c_wwqzchuJMgRMhqV459KTO8nQCjpD2jHCXQVxuBg8qlYwWWLolg230W0awzR1rguWbsPeI18BqxD36aE9S63_Te_vCxAUAMy7NrOG7cnELUCNlotDlVdCPKtE3RmoyhSzAgplS-7eM5vYkEU4t84xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ebe18939.mp4?token=Aer8UUGyyUsGkzTOu5wTf4yIAlhviyYOBF1DyCsjd06oMXIYVEGKMQvjZ2wQPXUlD4zjd58kdnM-kBeWxQbHVscPQwHLSSOyAJVyAiDVsf9nBrzbWmDLK0WCRSeZ2Wi0HISJdZSByaInNbG7vVlfCKID2RlhBubEyTYUMgUgxdHMGVuaiqH326ig88Lbs36c_wwqzchuJMgRMhqV459KTO8nQCjpD2jHCXQVxuBg8qlYwWWLolg230W0awzR1rguWbsPeI18BqxD36aE9S63_Te_vCxAUAMy7NrOG7cnELUCNlotDlVdCPKtE3RmoyhSzAgplS-7eM5vYkEU4t84xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ نادان وسط مراسم ختم گراهام آدامس در میاره به بغل دستیاش تعارف میزنه
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102249" target="_blank">📅 16:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102248">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvnH8fFLcztsZh3jKjC4IjAgrh8GyCag2hO-6PnIcwxw2yZFBu1jY6FhQnlx84OOCesLkER_ML16gQsqonIdq2cCDGg2PLmSl6pc0BcjexMB00QIWVPj5hYrxe1xZ8hltSBYu0wB4PMWwHForgliHkJiI3RDbIuoM2JMWH3kA3Qx7vfzlXPQUI6hVcOPTJsY2k8YMgw_vm4jKkH_zlrUbu_L5RC5qh2uo0dUYHlNzwrDvnKLT4V8ttLo5UMi86c-LLa8rIKDPUn-lQCz1K0aicWKkrsn5sUgnzHL5lJyBMT2qKNyqfdTqqqh04wWBf0rDuaZsIM2h-1jJZghEhK5bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔹
رئیس باشگاه الاتحاد فاش کرد که بعد از جدایی لیونل مسی از پاری‌سن‌ژرمن، این باشگاه یک پیشنهاد تاریخی به او داده بود:
ما ۱.۵ میلیارد یورو به مسی پیشنهاد دادیم، اما او این پیشنهاد را رد کرد چون خانواده‌اش می‌خواستند در میامی زندگی کنند.
چیزی که بیشتر از همه ما را غافلگیر کرد این بود که حتی یک لحظه هم برای تصمیمش تردید نکرد. میتوانست خانواده‌اش را راضی کند، اما خانواده‌اش را به پول ترجیح داد. ما کاملا به تصمیمش احترام می‌گذاریم. خانواده همیشه از هر مبلغی مهم‌تر است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102248" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
