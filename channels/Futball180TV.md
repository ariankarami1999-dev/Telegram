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
<img src="https://cdn5.telesco.pe/file/K5KdHhrqbYE3bN8Xqoz16yQipHvGbIU501F09ppmQ5BVP_FyjxoxjHVINnFfTkgOVd5LGo2qhKgDtpYbkTPV1lHdlKG_vUl5zKeR51IwQ8JLqOxRMRzDNkXbk822GMzPU9lq9zQhxd0XRybI50iUYnB3iXkyqxxyr-5A3n_OtngYmTJR2oJ5nJykqYO6hor6Lt5fIsGP4MzzuHlMdLnLJP7C_3Fwrrdk5aUmCrlsWoez7WDOfDbLsujT8zDiDkoUW9ev624_IV2qPCEAunnjQ2wMXfIIXZ0askuf_XPUNuggih5o4Irct_TAGrAJoTcnIYI73cFl16fAXSKsKWb1Fw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 694K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 20:29:22</div>
<hr>

<div class="tg-post" id="msg-96680">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTYsvJvfzH6hu4-j0V5ob6GgdE-iBGnZc60xMGQdjRKo8rzVXvEqSjPTmy_zWyY6vL9su5FobwA0r1tnR-5xP_ShUMSnz8XWb8qzITzQO96DESD6rmSPyi27ZAdsWXE6pZq1YeGYckV8y5n2NJmFidxxkL3USd_yVKpHthDTcBMoqUjPuKDeiIB_6r6HZ3dJ3EpDVVSsu0ek0jdL-7X4sdhLxnbiFlxRcWIxV4vBt4erO5DSk_OkuGHiG49oWe5GqiE6nFJvZYXjFhAPbYSnT-HLJUfDBQcY8hteZ65G9Mk_iWGq7hx9tNhfvPpQZ_Be7TI1Di8vuuNlDKT1cydkIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🇵🇹
وقتی‌بازیکنان پرتغال حرص این‌دوتا بانوی جذاب رو در میارن و سوژه رسانه‌ها میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/Futball180TV/96680" target="_blank">📅 20:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96671">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hoe7SEvRNFhldGRbdMoilkg1mL4Kc3tVK71cUgRmkPLENSJ1wRNoG4xMHwt-CuJjASbsw9rzlXElmdg0k4rmhwI_qXxRx34Cp17H0i2nBiIxIndDUDPWA8pZcsSwdx0sJmJUuMoU2_MtaekheyYKII_RYcWuW9IHw4LCdb9kTgy-rElgiIRVtawLwA-qIiZxxbEiGGn3c92OrwicIBVNM2nxY4_Njp-GXhio0fjAHP6MKshQ4qFRA7oyJyjRwDSK-BOpb3OrMZzFpYusN2sXpxj0apKxbAwSQwxEsh57crSiZBPu8XbF9251j6xP3RoPFDWBTqzG85AK30BANI_wUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJiGhs7i1RQlO2-veb6lGjIeG-Snx13AUITp-YPliEkhNE0PfldiqA1fcbqf0tdDakpdAQjt1VqK-LSac66gZwzbmq-ZEZJCokDQzQ-YY6oLXjeQf-74mtjCTdQTjfZXEG-f6b3xMBc_JhQ3fMRo_FkwrfWfCmbdFt0JCN76BhjdPzoRBXmZMnNxAUTEdpCM9xcDk9SOpFmuDKisXmNP9zz7VB3x2nyil0DwTeqZgbQwtjmXbRWvsCmNoedEXd4OnIgNh9ZP4lAyDbBaR4KR8S0A1SqAcinuSrlWlaKxZUMfNGEk6yW3MQlwI7GcOEUsqzX3i4X46lQwYGlsjnk6nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Seqz263jj7lsDNF8fSrDcZ2mzXN8SisGR2dppJ7n5nRYpAzJo-JxWj5JveJL0ZuOfIbKGr0aFnh_vHPBewvSySBcO2GM2DrEXU8StjW_j6_kg7K-52g9W4c_Q5YrW6__vH4Znh0y30xjgqcMG7KsLTjuzQVYAfnQXyRAmS8AGeiUGq8GL1e-g6FbcQUXqU1Og4GIJyHopg-6t5n6JleRisoz8nCpxfy_sFpdEIDvcEdJ4GUC9W7J-E4QpvavHrPNRsuWT2bN2QlXu6F3rdvJLZNB2E3u3PUNDYjOvTHY4H713voljKGyuhKtSDaRMTbv_2oMoxJeIj_P4cN8Wyrhgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJFSk7oZrDkQsgZE7k4BqmGgHLXFIKPx-LMvXAIgGYZQF9YWPw0hUysYKkFkg398cI8qKveWVP8uNnryOllnDZeLDgtiV7Hca0Ai_I4qp_xo-TwtIhmy41Mo8NOzdVJ0ytOZCxBMXYxBUGgtcQze-mNSF6iJwcWAPbKX261bx0SGSBOKgQE7mdCg9pdUXj4eB-jzoimB9ePj-rGPM-A0HQeq1weMzn1wVkiBYv-hq1gmK-PrUkhJM-PPn-z_zMpvCLQAq7T5MSwsGm0vyWpdIzh34swQ8I73SJS8Yxkb17q-zQ7_yN4PgAKuglUyj7p1wvQu9prkGXn7EzoBRSIUww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p52Cnc0e6z9njLp1kp_yqZRvDy9A8UubstRvT2_JabDXk8ScQGuzc5PL-PwBfj-VqQdXHpDJu4HaTYkmo_cnsHIo7nf5hxUWYPh4BBhze-39rpnYiCCyKHEP1YG-jHzDQW4xcGrjZhV-A5Ufr_Psk3iaX9igN3J2yzMgFgNxUBud7xFlyFIbs5UdI7DT9wGhPeMapTdVQsKcKY7RAn_ftD1ykjMRpBPX6Pj1oLCjNTHybMreE2lkM44nYzTDsgQaG8BzJiTVOznZHxwaYtKMnHdZ2JGcnjOQZx7-bdMRluDC3m3bGNFhh4UYmvZ4tWWxBD2glyXqwfOfjIC6VZI5OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/onkTsbrwcVWnG8tSmNy6mFAjMEkuqhAs5Uzq2tSyACJjxFP-LGAhaFku5b9m4qkxgbHeWqgUhEI_Gg6ACisiq-r8c7Hl8FGNOgXub_ql0kdGFpCwV2wznjEWHj6UHjA18BnwNGnPo7idJIGbINoBjzW2G2kLMdfAPeJmoQm0LLj80y6Rm_DmkT0hL1B5vnxP3u-cprBkgVXjUmta1rmERcbqej2Sl6U1TdyPZBvGDv7ME0KM0-dkE_vDnfOgds9_rDcghbRX_kgaM9JzE7f2ZQfEVV4ljdfyHNib4oRv7QhiKTcFBqegPMjqWvQilWCUi_rD1vGpy6Wlef2wLvjzgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ha42RFq3Ovcm-IinnnfkLw8xE48pd0cegPgFYkXADKG5Gnqc11ZmQtN_x6PlGLMGLBVlHF-DntA3VlAtECmMzbowr54qzuMtPwchnwKbf0ZKAc33HvHM8-tLicENbF-NnR96F92cpGyFH_k4CnLBYE2gkMoyOLTCxi3JkRctGEfHszQMyC06zzNL6Luqs5ZcSmFfjHJhISE9-xsawAjJvV430WUh6yg_Uo-U4baYSo8syxEdd_FaeZj5daIOwUlmcVZ5vR1cW_YKv5u1wC6uxyyYiORvWY96v7X6C5qGhAZYAkApuTogbvOFocfyJALjCiQiQT78WRom3IE4xdTWsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WNxoNYaDjBO14pKd0ofvjy_8nIuXEBBb-eMdl3V-C86il2eLjFHhb-7iTbc--eHVmpb1wcXMO08PJBRH_Bz_VRKCm7QssK6wKu3OWh3Verp6kDiDEdIe4eVBkvwsGWviG7MVeDNjCUL-3t7NAuJ1mvl1_MvsYbTN6b_r1cjVIebUnAJuGzKqyKGTB0rJELZF7Yp0fhaaSQJmD5MdjJFzeFWceUWtlW2eZ7VK03tAs_3icmqUJ6BjOJen-HNVTud-lV-w35j9U7ZqjJnTn4tAziAqo0e8be0gcy9fWti8qXv3t5FO9s0JyDM2wIwDkol5NKtRNWxon77jnY-Ff2vJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V3pQ0h1qCgIZQSqQCEpJuA1ahgns8Fb8zpoKnELxddtmwdXIW38lWj_efgVQW_yDpAfoMaE__twxlSgiRomlbEMN46-ysQ3cq1wdM6lRo3Gfjff3EX1xHbEQ5PXD6NvjmMXOnJLZ0E6zTlbeqNe9XgByaGV4-igR51YwXwYXG6jX4qc-8tAcmcL1alK-u4NiX9sNE52IaA9i9gz9_OmfQFtDKaBQYk115eJSCuZnV7A2jE_8TuX6wkz5QzkN1JyqbUcUxQAvVkP8JXWV-t2Z-nSCHLWL1SJVSeUuDwMm2sa83cTMXaXneXbVGlkqomGJTXyz0sUlvj_P-h7mp_oexA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😐
🇲🇽
تصاویر ازدواج نیکی‌هرناندز بازیکن تیم‌ملی بانوان مکزیک
💍
💍
💍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/Futball180TV/96671" target="_blank">📅 20:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96670">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e4bda6f8.mp4?token=GUCWLjEXfDwDXh3keW9yLG35PxKguKABgMx5uHVRJQRrt38sHL9EzYP6cP2IhT0i6114zH_sha8wjpbBlbj64iKR6cytLUD-3MvcyNq14AaV_Uzb2k1k-FADv8IQfQfdpHpsc1yN2OYBFRrzQs9xaoriMTeKwMc0-X4HjBBRw8ytka7go2bdICyQc8dpaIQ9Hrh9kTlW6s3qgYhB98RIfn9Hdbn3pQabyHTM7d0dN808WWHyg5p3hSlYYrwTNinabFc02f3VAY6EV8omNz0irZMuO53GNk-JcEAsbVtqkloDEY3FLm4XBuXjLObTPNleQwkMyCcozJ9lURa-8kTaxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e4bda6f8.mp4?token=GUCWLjEXfDwDXh3keW9yLG35PxKguKABgMx5uHVRJQRrt38sHL9EzYP6cP2IhT0i6114zH_sha8wjpbBlbj64iKR6cytLUD-3MvcyNq14AaV_Uzb2k1k-FADv8IQfQfdpHpsc1yN2OYBFRrzQs9xaoriMTeKwMc0-X4HjBBRw8ytka7go2bdICyQc8dpaIQ9Hrh9kTlW6s3qgYhB98RIfn9Hdbn3pQabyHTM7d0dN808WWHyg5p3hSlYYrwTNinabFc02f3VAY6EV8omNz0irZMuO53GNk-JcEAsbVtqkloDEY3FLm4XBuXjLObTPNleQwkMyCcozJ9lURa-8kTaxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✔️
🇰🇷
سرمربی کره‌جنوبی بدین‌شکل ضمن ابراز شرمساری و عذرخواهی فراوان از مردم کشورش، از هدایت این‌تیم بعد حذف از جام‌جهانی استعفا داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/Futball180TV/96670" target="_blank">📅 19:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96669">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWaiLvpD0zeTx_IuuPih9B4srXhBAy4sl50ViSTFNq4cUacuBS99TQL8b0s_UM7uSSqzyhIC97D6TFjrzus2mll1lSEP_VgVBVdsRpU3ZIPZQbaK-p9QrgZDoReb7DpmzAZgyWhXQGb9OpSU3K-1UChuCxa_F0197YN7orwCWzPqQUgjrRGyk1uNlZpNCztoNKd_7C2yrqaLcpCcVHANsn9d7AWrBVdPboA-xGJDpcor_gMpuDhzuBUpkQGA6WsVPVyxnclNdB6cR7sx7bFA5cS3ldUxwVx5Tv5UQ1uQpzNMZ9pD5myOvFchDm0FVdRbIx7SNn1vhmXNXLUwr7X4Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه منچستریونایتد اعلام کرد که مانوئل اوگارته، دچار پارگی رباط زانو شده و برای مدت طولانی غایب خواهد بود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/Futball180TV/96669" target="_blank">📅 19:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96668">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b44065a1.mp4?token=pa_IcLNrbo5UiA_KcCiCy7R_NWlCrvLQlWTWzrXBntbwAa_Rzr7UTqie144oRBBR5zcpM70vinAlc9GCre2bzGMXmCrIcwY6c3XYcS-r6YYPLuHM0DTbidiTQXE4BJDw5Wn5ZwsLc2e2V6wiJnB1OZ-ahbr5KWx6Y8Q99CvbMwwm_SaPcJSTpSLFRW1NEeP711t7nktobeCRKa9AfzSMcw6J3l3c7sDIyZ-c1DtX_0YQNqkvON1AbvUvPSIs0Ku39VE0FGWqZrki21qyGShQYZTUM9cUJCbYBUwXwBEVQQumH-IvbNIKShxHjVbTPuXyJ9O-Opjcnl7Q6QyKvmRKlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b44065a1.mp4?token=pa_IcLNrbo5UiA_KcCiCy7R_NWlCrvLQlWTWzrXBntbwAa_Rzr7UTqie144oRBBR5zcpM70vinAlc9GCre2bzGMXmCrIcwY6c3XYcS-r6YYPLuHM0DTbidiTQXE4BJDw5Wn5ZwsLc2e2V6wiJnB1OZ-ahbr5KWx6Y8Q99CvbMwwm_SaPcJSTpSLFRW1NEeP711t7nktobeCRKa9AfzSMcw6J3l3c7sDIyZ-c1DtX_0YQNqkvON1AbvUvPSIs0Ku39VE0FGWqZrki21qyGShQYZTUM9cUJCbYBUwXwBEVQQumH-IvbNIKShxHjVbTPuXyJ9O-Opjcnl7Q6QyKvmRKlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📊
🇩🇿
پاس‌های فراوان الجزایر پیش از گل در بازی مقابل اتریش که رکورد جالبی به ثبت رسونده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/Futball180TV/96668" target="_blank">📅 19:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96667">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRKFaa9t7MuiMcMN1QylkVdT65KfaTsfDenSq8YbshfBkYanGCVkxWis23GoooemuZH6dQj0TTfXnZ6DBbfHCtWqA1-uF91R75cOtUc-XBTyYQsP7kWAYVIkRk8xn7Wgp1MkA6QMHjQ5QalrIkNGvISKYFCxzl0x6mhrLJjvFh68D8StvytvvzHocEm1_xQjwEohP8_oLPE8d_CYXPWghtYLR-WXBP9CubkGUutkiUVXQBOXz439aOnHnDoueUuYA_sRkvanlZue2RaWjXnVuwyn0l0ZeLcfyU8ItWDDVT-vTfR7Ydd2uDodAT89K3kGfbRKXHEkT5fuz0KGs6c-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
😐
جاسم بازیکن کسخل اردن بعد بازی با آرژانتین برای تمسخر مسی این عکس رو پست کرده که جمعیت عظیم فوتبال دوستان زیر پستش از خجالتش در اومدن و مجبور شد کامنتاشو ببنده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/96667" target="_blank">📅 19:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96666">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94d5bf8566.mp4?token=Jis9mRTP45zq4ECdWnbamGp2Ah1fyCfQivu4bqp1UdqskVUcK4NbhH6njsr1uz8zYTkWxlwaQhtY_IJoVKLkdoz7jMo1OrAMhM3bzwpWL7RsoFKapG8ggfD5QkqqsUOZ4aUCJWePy0kGTpF2SyvcNaYAAxR3bND7XytyeaW8RP7wC2LmYhqhjgyW9LemqZt5IB3FsZPKF28pX6FptM9ZuoNVsNYPxW_PJkkSN5vUCAVGl6GvNF1ilvxvqb-duAg2YbTfBMbdjfMrh3JS5fnNQO84p3O1n6-JTiLPdvKcALIe-fNZofIPWH0-Ok5_hnJSntF3cfLqnoHSSLdY5LraBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94d5bf8566.mp4?token=Jis9mRTP45zq4ECdWnbamGp2Ah1fyCfQivu4bqp1UdqskVUcK4NbhH6njsr1uz8zYTkWxlwaQhtY_IJoVKLkdoz7jMo1OrAMhM3bzwpWL7RsoFKapG8ggfD5QkqqsUOZ4aUCJWePy0kGTpF2SyvcNaYAAxR3bND7XytyeaW8RP7wC2LmYhqhjgyW9LemqZt5IB3FsZPKF28pX6FptM9ZuoNVsNYPxW_PJkkSN5vUCAVGl6GvNF1ilvxvqb-duAg2YbTfBMbdjfMrh3JS5fnNQO84p3O1n6-JTiLPdvKcALIe-fNZofIPWH0-Ok5_hnJSntF3cfLqnoHSSLdY5LraBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
😢
🇩🇿
خوشحالی الجزایری‌ها از دریافت گل‌سوم مقابل اتریش و عدم برخورد با اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/96666" target="_blank">📅 19:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96665">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXePFfY5spNHuZ6WamMoSY-t5aCVPvdN6oMqHNwykNPQcALXRALyDmkSWXNDEzjIgU-mdYJhRckXr23J0S3f3duKwzbSQB5z6nRa_rQJiwj8d8Of03dYg7Tw-pEhwjYJ7kxJBdXLGlhNyypn6XzEifFS4kHb2Hw5rBrgXr_LxO0G2lxVdvGQkPiDVnScBGuJecQu82YXnpjvs_J-h49pCs6MIxHYpYUdmi-cx8dtglv7S6BKx4NnPLN8zVU2DCEGQaSiCDegJI_kMeMGGu_PEpRMhDLQNMpMsCtEnBu-O7CIJkDiVHtj6XTnjjSUH2F7WdvIQmuNpSYAb4PTZTiUiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🇵🇹
کریستیانو رونالدو  :
• ۲۰۰۶ مقام چهارم.
• ۲۰۱۰ مرحله یک هشتم نهایی.
• ۲۰۱۴ مرحله گروهی.
• ۲۰۱۸ مرحله یک هشتم نهایی.
• ۲۰۲۲ یک چهارم نهایی.
• ۲۰۲۶ صعود به مرحله ۳۲+.
🏆
- عدم کسب جام جهانی
❌
.
📊
🇦🇷
🤩
لیونل مسی  :
• ۲۰۰۶ یک چهارم نهایی.
• ۲۰۱۰ یک چهارم نهایی.
• ۲۰۱۴ نایب قهرمان.
• ۲۰۱۸ مرحله یک هشتم نهایی.
• ۲۰۲۲ قهرمان.
• ۲۰۲۶ صعود به مرحله ۳۲+.
🏆
- یک بار قهرمان جام جهانی شده است
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/96665" target="_blank">📅 18:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96664">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWY_Qpo4w3TuKLt7yPIr4QU7lNyAuRYCqfqknm-Qpv4yjUf6ozEs1q2ZqkGI0EoApa0A9_c_c91-UdgkzIPR3S-n_kgbuYvoe9h-aK4ekCnvh-zF6pCO7EcFemID6m3hZ5jN1DrhUpWRviscxb2x09SWX8ZmYRW6TInMdS9E0Ea876v_41a_SDgYngP_hIHW_lWNrE70kxxqJ2SbecZtpKb9E_p8mFNEq_NkhmmyKP8g4u39tBG8_AL4pcsvC9MnJs-mslSUf1hk84aaCfu8uQfiOw3kK10KrJB6xyz_jH59-ug6Wdic5uqQD91Mgva_lOLkCPyUUO5G3xS3qxkk5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇦
🏆
🇿🇦
پیش‌بینی اوپتا از اول بازی امشب مرحله حذفی بین کانادا و آفریقای‌جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/96664" target="_blank">📅 18:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96661">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZO7nFyMK7kurZlSf5Id_wTSbAw6TCmXiDYfyqJV496kImmDNmxRdzqiXbbEWWKm1ns4l2O4mt-5ut6y_9z5f03XSaQ3t9HDC8-3CGNHDIV4yZxTx1EfLt_HZJmVy-RzIwDsbLwHsgn7qVXS_2pzAQ2ZggOHlBzh_PeYVXCsJxEVDnU1por8Odiut60XjY6Sino6ZvjZ_iBAzpZ-LQQV36Bex0Tg79sH2UBS5Fo3gFzSlXpKpCIMRulDYHzB2m8hkWMlDfEZV5zZFfUByMYFbjDSdN1LKsU74h7vQ8P7wnpXNBcgPueiCAfSikX9gipKhlnyBCZ7N6Ob1HbVaiF-UTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oA0tiCQPiHpcX67DZGYZyLCKB06-nkg9u909E9EjaiLqHA35az7wi9zsApLOox9I1eRIRTsW1a9z2v-1JFasxbjrT7AbKBkF0Dal8hcGWcxok7ev4gnOkjvAFeqkG-A8ndkI-ltI18zEZ4KO243RF7J4Sl_JbJW89j8Ce1EUvn9Ijf03B_D5iTymI8CIgZvHsNlulyzen0Jr8dpv-znxygdBTgzdrGzb_vRQCyNYfCreRV2sTCvgTVVq6MW02TDUhLv5IdAPQ94IKV94BDfUM0DPl6_YYqRb0eO4rIYfdD9Lkgf7amIgaxG7AvRsQ4zkgLNmEfwAbp4a9ix3WUvHnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phMI55Co7H1ryIiHVR6-p__MSvuxLVjsD5ns3yFLifpQKK5lXD8iwqzX2xo12scgpNOZXAvOkJ2QB4gfQnQGaCknros1RQ1RFxBDT56dVLC4sr_G0HQdONm-Zywn-qd9REaZOF7pK6jLVyBkXcca0OMopiuNQBAoICAEZYUKYv88ISpuhaoLDTwvhliedIAY7UuNAuErCk6al13MBg-fCv8EEQc4Q431qTPPRGGCm63fGMpCbJLDyG8QlfSgcj9hcWyicCLtiubA7YNnKxiUWCRiW6iuCIX1Zld9gRfLWoj27S5m8i9mezc1PuTQIXGPYCaa8dw1rCHSXVxxvhS5ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
🥇
رئال مادرید مرحله گروهی جام جهانی را با بیشترین تعداد جوایز بهترین بازیکن بازی به پایان رساند، با ۸ جایزه، پیشتاز نسبت به لیورپول با ۴ جایزه، و پاری سن ژرمن و بایرن مونیخ با ۳ جایزه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/96661" target="_blank">📅 18:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96660">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2382f7a63a.mp4?token=AjFtGCtGpuNxpyOl8BzyPrIXrehtQ3nOZQxn2CoDoivjf1eSC5gfeWvxdGGp0gnpYCwL6v071wEnu6SmSd5jMkKQw7JCFoRY50jbrXaG5aiNGfuhnkbJ5GbCNJaZ4yE3X61nhUbnUsGGCpHkzN88sJiJNBz8VZtyB3xeMnrIO2XH-gnXxNrIpW_AntxZbwBGEWiefj8Bn_9cz3W_qYFUUt_OumxoZj2UuQbG-QbRiIfjSS0K0awkfLoLxNxiwCHHGuzZT7xTENTNcd-49urHtPSqRGiLMCmZNoOcQ2fiiS8nyBI_ZTyeS6bifBBAxSa3gvug7A_8UjvOxm4fhJhHQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2382f7a63a.mp4?token=AjFtGCtGpuNxpyOl8BzyPrIXrehtQ3nOZQxn2CoDoivjf1eSC5gfeWvxdGGp0gnpYCwL6v071wEnu6SmSd5jMkKQw7JCFoRY50jbrXaG5aiNGfuhnkbJ5GbCNJaZ4yE3X61nhUbnUsGGCpHkzN88sJiJNBz8VZtyB3xeMnrIO2XH-gnXxNrIpW_AntxZbwBGEWiefj8Bn_9cz3W_qYFUUt_OumxoZj2UuQbG-QbRiIfjSS0K0awkfLoLxNxiwCHHGuzZT7xTENTNcd-49urHtPSqRGiLMCmZNoOcQ2fiiS8nyBI_ZTyeS6bifBBAxSa3gvug7A_8UjvOxm4fhJhHQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلیپ کاربردی برای بازیکن های تیم ملی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/96660" target="_blank">📅 18:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96658">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vo4McMsm6DDst9ABZBvqIit5x268PPu5aVIMzs-Q-bihQ0MraujsuC5B25OsODvpCfwtsTOY206MwxXjdnhvKh218NgdlVI6J50ljeWn_G6KP1dk-KhltLtnH-2Q7dDcg_kXThxMlOrwGzI1ShgGKsW2Keb3gN74kU4R0Q5d3NPhbRu6f8ScQmgTDHKBTtSTCTnUFSFy83U8IFRWvi2Cg5MQMWvvPm471-ZT_w3rM_6Np1BITJWDGhON-E7arFNl73DrQ3Mv6yGSpBjBO7UJS5dEipyXB6bUE2hFT7BdOZdhCxj4cH_06TXt3l_ARBEJfmrrDXPkOFe10kZaIkUQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/myoxrrvRZLoG6WC0X2IW-dLRUZmd9tKQGmHIJvsGZaHTBp-rOyN_KY6a2BYPdQ7mAxMzyQa8_DfjweRDvg5LkNKQzCHPOLitWAUtPoKXGCSJRzej7-y0jOjltTgoO8QudILFdZ0f0bxpfx7GLfJ0RA7tEwAChlos0G-3A-aXBYua5dV1OarS75FMLHdbmXkYb-fgeMA0aqlz93bVqVNJbQe7M46mcwW3EhM2_SSBzMAvO1Q9WQRZqRSLE2ES5mue-ScHnZn-ZpjkYn-J7R4rRYpQVYGGAN0kTsv5BLVxQb47Qo3o3AzPj8le38BW5uAxWSYui4vd-_FXYfFbEMTVnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
یورگن کلوپ:
یه استوری از سادیو مانه دیدم که عکس تیم ملی مصر توش بود و براش قلب گذاشته بود. از اون پست اسکرین‌شات گرفتم و برای محمد صلاح فرستادم، فقط برای اینکه مطمئن بشم دیده! اینا همون خاطرات قشنگیه که همیشه بین ما سه نفر وجود داشته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/96658" target="_blank">📅 17:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96657">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gt456INXgWqIQnrZufnjZv_HQLpAE1F6Hpcdw5Pl4KlHvi3_VXvQu_bnbGBpit9vx3eodRVGbb2JxfvPH6YM8SQLnf1J0X6p80d29h3Jj-4quc69rGmJWvmkq53XbKomJiuUzPpssTpZZgfQj5arr5EtZ85XiOHgo80BfKEKYAEok7avPr_cFX7s792-_veXJdBJ1Uvau6nNHSdP8gO45gHUp98h5gUDg93dSeotaXjq2urMe6Cd7OlOAKiHt2oUugeBTky5zDaK5pPt0kPg-tn4yFB4bvy_FdrVan-aOB7dmbdLmQattG6-fORpHnC7Eqdj2yAYX4DHEFPO-vvd5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرشیووار:
در بازی کلمبیا و پرتغال یک فاجعه رخ داده و گل کلمبیا که 100% صحیح بود، مردود اعلام شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/96657" target="_blank">📅 17:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96656">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDpUqeTBeuLDPZwMhjgO059FR3hEchi4ZlgJPf9E5tIrbC5K3QdQ6n3HwA8BwQBwNZ3YcycqIhn-5XVjjlLMTvA2fUiJSxxM9Zkc9zqCfGu4ZG1dXxq0QkClGWwJ6fn554g8nr6k6dFj4JipAGkqDTnunjIQqx-avFEm8EutaxdkKT7Wbd7VesCedP9F3vmSRes5epqCaEqWfjLNod0iDq2vzyKisRY9oeBoGJa-omGtLv_u9b7aBRBdcq9O_DV1nX296e6rfEJMhZfve8vZoQqpvYzWfQ0u3kXQ-gRJGT4Pzm_9F6uV38nlnA-zplOdkEOD46VrawkKDAf7s2X_QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان والیبال ایران و کوبا با برتری شاگردان پیاتزا
🇮🇷
3 | 25 | 25 | 20 | 30
🇨🇺
1 | 22 | 21 | 25 | 28
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/96656" target="_blank">📅 17:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96655">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjUn_7ZOprzf36HeOK9M7rhXi8pDVBO_SwRzHjYxyH_K9pHCYB6C4PxlaVKt0pd3BhjAC_vuqg6Ib5iVt5F4z5vlweFmoOO4lrk-W6Z6z9AVC351xXwdfyzT2_IBbetwf4OAo9tmnK3TBA779qgxgKX2aJy4Vau5tghwx23s4jP8kkz1U_OR21DGgQafMVFh-4dAMUv6X2TkKgzpLyeOszmAOlIOnAzY16BaxLkCZRsHR5r3VhFlEiezOM6ahakiFinX9IWit2Ql4xc8UR2l5ipPBN_vKNZS5iYCzYVTFyiwzo0pCoaqN3P7Jel_KirIenLgni0SHM33MJG9cb66AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سراسر حق محمد خاکپور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/96655" target="_blank">📅 16:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96654">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNEM1RBZQtcPAcvBJf_YRVAMOrKCYjj_7X-7gHm7oWZZ9nr6wJQLyqrm0OzfEaQxbsMsqN5GZ4Z_u4tfz2-zQNH8OasOAYWSZnfh5Xxh2wKGIlWrF8uVwpW1W4Ethac5XtoF67KWpyX5e8zAOZQuf1T1pBqHlVzE5fj-nIgtcsgfuaJa6yDijG-O3Uhhgzh7dyyMmEPEagZbt0HA8fpfWM9N4MWHLniOqKtWcc2KL2hDCqvHFpCbTjhni93qnob2SvVJs1Jd-_8ppSGOZQqp_aHNYYuDKiSdOc2RR9r4y_zbmX8E4ybLiEYwAyUNEkph1Sorpy84cA79IhBPg5MTOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
ارلینگ هالند [
🇳🇴
]:
🇫🇷
فرانسه خیلی خوش‌شانس است که امباپه را دارد، کاش او برای نروژ بازی می‌کرد، او خیلی سریع و خیلی قوی است، او بازیکن شگفت‌انگیزی است
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/96654" target="_blank">📅 16:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96653">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8757cd458c.mp4?token=cu1PM37_TZ8D_FbEPFep6JDaTHA7SRhF1xWZc2yyjBbboGzAcz9CEbwx1O6D52OUTua_U-wKqHCNiKgPkH3HecZOVi7zm7cxLxCBy_jfafUHbI_Lt6fRPIjApNsWC6BFc-RP-cA0UUvQH_RSdjKKfnodjrGEcZ9LZzLzoyxMfkX-i5YJKyCIYxHLmPATPw7mjhqlI6fEWybUtjA2j1u4ivg4sBPHYFqA-B1AoibiNEHBQ0RTQoAJN0sN7aENnMW-LVV2CywsjuZ-xg6cDNvdSwlkQ0psxw0y1tiY1gZA8g4GXvuq_T1YF4dEbAkpWw_AqOTodEqBldcPnnbpspEqkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8757cd458c.mp4?token=cu1PM37_TZ8D_FbEPFep6JDaTHA7SRhF1xWZc2yyjBbboGzAcz9CEbwx1O6D52OUTua_U-wKqHCNiKgPkH3HecZOVi7zm7cxLxCBy_jfafUHbI_Lt6fRPIjApNsWC6BFc-RP-cA0UUvQH_RSdjKKfnodjrGEcZ9LZzLzoyxMfkX-i5YJKyCIYxHLmPATPw7mjhqlI6fEWybUtjA2j1u4ivg4sBPHYFqA-B1AoibiNEHBQ0RTQoAJN0sN7aENnMW-LVV2CywsjuZ-xg6cDNvdSwlkQ0psxw0y1tiY1gZA8g4GXvuq_T1YF4dEbAkpWw_AqOTodEqBldcPnnbpspEqkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
😂
صدف‌بیوتی و رفیقای‌شیرین عقلش وقتی صحنه آفساید شجاع خلیل‌زاده رو تحلیل میکردن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/96653" target="_blank">📅 16:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96652">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZxgULz0fmfE5dFU37i3WEYzsAtEl4phWgM7nz9XD-yFx0Zh4O-mlLuz0IBQMIMTWmv9tKe6v2lVuixOGZwcxI23A1bqSVpHJK_TKmPdTBQEwB5dVud7ipKKsomXl55RihmsmejIL-ONJE58PiavJzL0guJ1ctHGvN1xxhO_R37IxFtwcbHq5mAcbBBYqxVfXDDJhlxzWnH9XGS773-S-Fx68v3jS2kJTreoJWj_87HQUq-fTtKPYMOFX1MoJiKDNhuhruDbK7TKciZlVqQNaYM9FxsxdL2mom40dMj0EMGziI1-nv625XJ2m8cJUhjZ2o6DFQpXD-16iCqiwqqgPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌛
پست جدید اینفانتینو تو اینستاگرام:
تبریک مجدد به تو لیونل مسی؛ تو رکورد جدیدی شکستی و به اولین بازیکن تاریخ فوتبال تبدیل شدی که در هفت مسابقه متوالی در جام جهانی گلزنی کرده است. تو در دور گروهی عملکرد شگفت‌انگیزی داشتی و امیدوارم در دور حذفی هم بدرخشی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/96652" target="_blank">📅 16:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96651">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8146eb2115.mp4?token=mpY_uZ5qucNNnToYSiGyE3RW_Ia1Y4CofDx0hEO37FRvgRZFIiXBZ2y1QhGl0vUIjPGZxNtYBMO8kkQHCtHaeBGwReYT0Plc2ycFzHKtBNH4k_LiZkAKjkuITO6cnlfTAT0ICTnRdfp1YCeT1bvy87o2SU3wQxiGnjVgq4xN1hKqBXTIKgZN_sJq3GtIktSAP0fefwKdSj55tPTTCOeMV5Xedj3Jy8_dtXTOnmv7eIqj6vlBaWLtdoA8uQ1Z9dsPjXZjOfeBx75QLDnOgDEXqtdrRIjsMOvy2Yty_DYj2Z4hXDRQK814inYA7RwuKA_6sJ2vp9ESK76j_GagCmSRKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8146eb2115.mp4?token=mpY_uZ5qucNNnToYSiGyE3RW_Ia1Y4CofDx0hEO37FRvgRZFIiXBZ2y1QhGl0vUIjPGZxNtYBMO8kkQHCtHaeBGwReYT0Plc2ycFzHKtBNH4k_LiZkAKjkuITO6cnlfTAT0ICTnRdfp1YCeT1bvy87o2SU3wQxiGnjVgq4xN1hKqBXTIKgZN_sJq3GtIktSAP0fefwKdSj55tPTTCOeMV5Xedj3Jy8_dtXTOnmv7eIqj6vlBaWLtdoA8uQ1Z9dsPjXZjOfeBx75QLDnOgDEXqtdrRIjsMOvy2Yty_DYj2Z4hXDRQK814inYA7RwuKA_6sJ2vp9ESK76j_GagCmSRKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظه مصدومیت وحشتناک والیبالیست تیم ملی کوبا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/96651" target="_blank">📅 16:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96650">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4b9d9dec8.mp4?token=v2rVY7t9CByWlE0ZUZe91qFHMN-BcHxrlg5sgKW4xy23XOXH2Cle8m0ae_P6I5R_p2UUl9SZcKW7p7wAuy4d6AQ9hkIQwPLPVCOF95Ge54N3hg-yqcp5f4ck_7ufkLD8pAf66DX9OY3wza2sbqLfpTY_HOW-IhWoEi4YizWI939dA_05xIQVYKXKnxJJGQstANNXKkpTZJ3svem3Zwutj8mJbO-dLW5GErdsV0j0WTIV-S9YgVqRtzxocIt0t_P9rbuRb9ajbr3i0HnZGMN2bWhBbsdCApkjwapRvdzrTiC_awjmqiV3Jx8ffqqP5zfWOhxrLAWkl46rJ8XZnnMshw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4b9d9dec8.mp4?token=v2rVY7t9CByWlE0ZUZe91qFHMN-BcHxrlg5sgKW4xy23XOXH2Cle8m0ae_P6I5R_p2UUl9SZcKW7p7wAuy4d6AQ9hkIQwPLPVCOF95Ge54N3hg-yqcp5f4ck_7ufkLD8pAf66DX9OY3wza2sbqLfpTY_HOW-IhWoEi4YizWI939dA_05xIQVYKXKnxJJGQstANNXKkpTZJ3svem3Zwutj8mJbO-dLW5GErdsV0j0WTIV-S9YgVqRtzxocIt0t_P9rbuRb9ajbr3i0HnZGMN2bWhBbsdCApkjwapRvdzrTiC_awjmqiV3Jx8ffqqP5zfWOhxrLAWkl46rJ8XZnnMshw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗽
تو مرحله گروهی که واقعا میزبان شایسته ای بودن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/96650" target="_blank">📅 16:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96649">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxneN4wqOXnTwdqq_kRiJMYDwn2v4qcyLJpZBSnCyWHzJKwjiYQeGeM1Q4kBi3fhNcshPHKgkhxytjbDauauZQFavuUSo-nDNC55xSKE39Uyg5oLc0beiqSkoBDa6nItg4Ry0S7gCzKzQcLfEYpaXFQALTgKG6x4OlSixDd_98SXZf2RKxcXKwK4x-rNuzL9JMhS-WbDJkmWtDYp1szC8-G1-RNafTpaCLCsT7xovqgT7HyUllDPTA7yhA7XNOVqnCSe6SnAAKPgh7bNNq8e3Fyju4wx1BTe04H4DY73s1_YEOBICYa_lLv1vstVa4TR0oPuJR5uB8JEw56hxBXdzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب مرحله گروهی جام جهانی ۲۰۲۶ از نگاه هواسکورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/96649" target="_blank">📅 15:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96648">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQm2ksja9yh8liEaGAjxb1W0RfWYhniyhdyPkesGN-Rv8avDClk3g1UNAhiTGwC2K19eRevUfG2NCh7bkbH9fuMFMBSFeRjPMjEYhTDoNap02BFssG3cLU5z7K1O0GS6NkfK-gbDZkcr6PqjPEjh87UWbEBg5A4bylmn59OMZboi2HCB3LMTWXpBWT1YyltNRjDXsPZD91zAWF1R-KCB5_x6uBLJ_L0UeCvXx2nMJ7UrY536JY8TKirCjiemwTFZsMdKEL8RR5oScBCSR0WTPjb807RNDWMVhAREwVMogdgwMQV8ksFtRzwKhkQc8__v2vDv9d3p8mZ_mu_u0mxKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زلاتان ابراهیموویچ:
رونالدو بعد از بازی با ازبکستان گفت "من برگشتم"، اما کلمبیا تو بازی دیشب بهش گفت: "به دنیای واقعی خوش اومدی!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/96648" target="_blank">📅 15:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96647">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d23322c7e.mp4?token=ATZ9DKztYBfdbjfrl_ZT1i9iK_RBaqNgUmb4LUqPzOM70VgpdseJFP905WzQP12QaE8D6uj47I2sL1rvFn770V7h3KtY7XxRqVpmiy2rTCr-VH4370BSydFDaex06cGp7WCE5BkUWz99dml3ILGakfJCirHfr06L2LZ_p9HoSYzSnx77-VYxB7ExJtzKkNv2wBEuC6orTbL_ebr1SEd9Cxg3G8fjwAvtz0PC2VJd5cXYLmGyAnb4HYhV6Us1Ro2oBbiiYtSnwNJ9FKX-zGre_E_j8cUFBIqqD6LYsiJ3RIAfkL7dC0N4V0UGd974G8jOgBC5R3o6fioJhnAHywiG1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d23322c7e.mp4?token=ATZ9DKztYBfdbjfrl_ZT1i9iK_RBaqNgUmb4LUqPzOM70VgpdseJFP905WzQP12QaE8D6uj47I2sL1rvFn770V7h3KtY7XxRqVpmiy2rTCr-VH4370BSydFDaex06cGp7WCE5BkUWz99dml3ILGakfJCirHfr06L2LZ_p9HoSYzSnx77-VYxB7ExJtzKkNv2wBEuC6orTbL_ebr1SEd9Cxg3G8fjwAvtz0PC2VJd5cXYLmGyAnb4HYhV6Us1Ro2oBbiiYtSnwNJ9FKX-zGre_E_j8cUFBIqqD6LYsiJ3RIAfkL7dC0N4V0UGd974G8jOgBC5R3o6fioJhnAHywiG1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇬
🇮🇷
خلاصه‌دیگر از بازی ایران و مصر :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/96647" target="_blank">📅 15:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96646">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbgAXvV2Kc6BbywqXxn_ZUW1TGo7A5Qhs-Y6xSEyx7Jp7xX47jr5BtO4ml6GpcnFNqTfyXY7umGA3Y5QlWg7m_QDeJsdEL8Tys0-dx-gjmP6x8LHRGdYGbx7U_O8Cz02Oa49NJ3fUa_huxFOShwRoinBlIJMUxw8CHRhJ22PFGJd4U_ZM_Bp2qzk0-o1q0pqY2o7moL1EchqMRVwex9aVqb1pMWpd1Emabh15DWNg5miRRHiWTSv3bSpdM3ZMsLdwWCTIiRj_b8DjVDf12OClg8bJoz7tX_tgmMHaNGvK4UMo0EQN-3LS78AMv8GAQC6IGG04lz1Nxbe67zwDi-jsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر چند هوادار ولزی : ما اومدیم اینجا و به همسرامون گفتیم ولز صعود کرده به جام جهانی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/96646" target="_blank">📅 15:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96645">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dg4bOqmbqdzrpiX575JkTBGele2OrbBuuZi67aRofjXTjbtWlfe9mp8jYtsvgwoIwQcSMsdaSz0R1qEd9l7gzC64Cy-1bZq5qqDKxKkFk00WSSIOZenqpwFA0-aXT04sKCel1clbz_RB9Db-UrfyqOz4-Ac3Ym6wJs8bGcg9bWtRpbt_jcBCkZyBg_81-rveXFDMoxXdCK_wNoFPnIJB7BudDs8PObTYZI64zw0Y_8CWGiFQcjjXrAY89UfBTXloXHUNN0I0OodbuNgHgv0iqbuClxCKJFR7JgDIn1VY-vD-so6KlV-k1jBGyz9swl0aq-C7wKzfbcbGOmWoptdB2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇬
مصریا بیخیال کون شجاع نمیشن.
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/96645" target="_blank">📅 15:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96644">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‼️
🙂
علی‌نظر محمدی سرمربی شهرداری نوشهر رو مشاهده می‌کنید که درحال ماستمالی ریدمان تیمش تو لیگ‌یک هست. این برادر بزرگوار سابقه طولانی تو ریدن به تیم‌های شمالی کشور داره و داشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/96644" target="_blank">📅 15:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96643">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc66af2245.mp4?token=Dbuo_aAwWyhLYpt3B9xIMFXYnZ98f2c7TVcT56Iii73O_tAV-i9sqfQp57M-5l-tTaO3v-7giZ-410EZWGO_1VNmhT1a6UZbdLmZcavK-lG63vxYK5-UXIKKtkOEUjbpK3oxlEkS1bwB2Lh903e-Z3sgSgT8YdzdREtFxizdjlJCLh4phnK94gXvmMhEa5dP64Ly5V-TLlDonl2_veqPGnXCnSnWn6pV0O24Gl5wBznHIzuXop3tTIi0PZWXiN16GeAibAtOHCPWOjCGcAjm_TLuC2etS5NSh64vALKjJXYjJ7WHqHTSZECOqOM0UgM77yedFW39Z0Xv2MtGILY4jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc66af2245.mp4?token=Dbuo_aAwWyhLYpt3B9xIMFXYnZ98f2c7TVcT56Iii73O_tAV-i9sqfQp57M-5l-tTaO3v-7giZ-410EZWGO_1VNmhT1a6UZbdLmZcavK-lG63vxYK5-UXIKKtkOEUjbpK3oxlEkS1bwB2Lh903e-Z3sgSgT8YdzdREtFxizdjlJCLh4phnK94gXvmMhEa5dP64Ly5V-TLlDonl2_veqPGnXCnSnWn6pV0O24Gl5wBznHIzuXop3tTIi0PZWXiN16GeAibAtOHCPWOjCGcAjm_TLuC2etS5NSh64vALKjJXYjJ7WHqHTSZECOqOM0UgM77yedFW39Z0Xv2MtGILY4jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😏
اسپید از شدت ریدمان دیشب رونالدو کلش کیری شد و وسط بازی از ورزشگاه رفت
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/96643" target="_blank">📅 15:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96642">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVZAgKRBMaSdqAoQtGNIyPyijScRZRB45-5Do0sO_RoT-a31_HVB6-LxP3GnhP9l6VK_1XDrTG3br5X5GRDqyXJJnfT4S3x-uPU-seoy0-KrOad0REp5ZRDCaZEQuyVb17VbOY5VKLz9c1B4e64KO5qVQz_1GeYeglD-G2SVuH9u6KLmdUUZRX0HQFcDVkaqmCYPvQXS_g2D-TmSq95hdduRbDTWamFxwaxJrTHHQoHgyTeq3paZvaGgYY-XV3IpFtsKzr5M73QoI_PDCpK7cjk2Rpj3uPofcGmlz3laRne0Yrrxw6rp-CLDVYvKu34GfGRSv42YGlJ5EZPNEQhUpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇺
🏐
🇮🇷
اعلام ترکیب والیبال ایران مقابل کوبا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/96642" target="_blank">📅 14:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96641">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fd01d9791.mp4?token=HIIW148jcOJXU-uE6wDHOfw3whQyFZXFUX4X4r7orfFL7T_d8nKd1kqZnIEJKMDnmLevszKHrPjKpGCcP0DdJg8KfoOSLStkBUQ10HYOBwpST_l0yT05o55-_vX1p4ostmOTEdWfJj9qqm6RJvPJiAOxta38EGiNmBVtPVL9iVpfAJQyrohTyoSrjQxaKpBfc_iUzeKTdtqsrcZv6AsrrffJxQKOOPIC9qrVbuivmR-ttT5Bp76-0Hs36xi7JzU4QaY3wmjSDMxJWnx84e_ziim4uAf4UCoU9V8V0rqzGuxt2FsottV0KtGAPReNWf8CPhgdbDQNKzsbPFCfwlZSiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fd01d9791.mp4?token=HIIW148jcOJXU-uE6wDHOfw3whQyFZXFUX4X4r7orfFL7T_d8nKd1kqZnIEJKMDnmLevszKHrPjKpGCcP0DdJg8KfoOSLStkBUQ10HYOBwpST_l0yT05o55-_vX1p4ostmOTEdWfJj9qqm6RJvPJiAOxta38EGiNmBVtPVL9iVpfAJQyrohTyoSrjQxaKpBfc_iUzeKTdtqsrcZv6AsrrffJxQKOOPIC9qrVbuivmR-ttT5Bp76-0Hs36xi7JzU4QaY3wmjSDMxJWnx84e_ziim4uAf4UCoU9V8V0rqzGuxt2FsottV0KtGAPReNWf8CPhgdbDQNKzsbPFCfwlZSiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
وضعیت ایرانی‌جماعت بعد ریدمان اردشیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/96641" target="_blank">📅 14:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96640">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzFOC5usqJss6dW5JXW9T8ZZpexorEo6pQB5jFUnPs57ghjVpeMfKbXuUa2_fdxW20IG5S_AKMQebLxTtTSmT5KJsdXb5J4FM8J5WFBWRnkNjz0q5cf1g84Fq1nv1oM943GusOwj6PqK2NL9p1EJXTzv4mW6SpFI5xhawi6e8-mxLnoR9waEso3TVXKXw_0WBF2dwQpuCMzZr7P4nvdfbGgfQJE2m0f9xe52JP5f6-OR23S_vP5tTOXfv-JSuR4AaAuttqy-8A5en8WwYVlgsVbeqXSa9GRGSbNiNJb_O7Fk-I1UhPmDpQkJCJZPAhxZs0VHZrsVFPmUVGe1CdStag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
فکتی پشم‌ریزون از هالند که نمی‌دونستید
👀
مهاجم تیم ملی نروژ و همسرش، ایزابل هاوگسنگ یوهانسن، در سال ۲۰۲۴ صاحب یک پسر شدند، اما تا امروز نه اسم فرزندشان را رسانه‌ای کرده‌اند و نه عکسی منتشر کرده‌اند که چهره‌اش مشخص باشد
🇳🇴
در دورانی که تقریبا همه لحظه‌های زندگی در شبکه‌های اجتماعی به اشتراک گذاشته می‌شود، هالند مسیر متفاوتی را انتخاب کرده؛ او زندگی خانوادگی‌اش را دور از حاشیه نگه داشته و از حریم خصوصی فرزندش محافظت می‌کند
❤️
👶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/96640" target="_blank">📅 14:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96639">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/96639" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/96639" target="_blank">📅 14:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96638">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=iRyaHBJmJWGSFzvcPOSzIjaxBvn-gPbj-jqXnGsGcsnN_c_6CNHUg2MYzrzxhxhGIZGi8mio8FP3fFLF_XWn8J4ntxVA3pZcYupI-20_i0tf_5xInFEkQUpUWS7aO5O77FtPE2HNJrfWonkQ3GnBUGlN_jPdyC-6GI15-i57VM6mLt_z37wW_PjHCAFGDux2GKn54gOdv5V-ttJhlpdGqLWdpLlHBvJmPn3Zc6415z_C9zDlHyFEvba8ib3na976-taX5n9tCjpz8838vra7DrDwHl-jqF3HnpJU4HX9ePnpTZ2h4hfYoHW-waXD8VMfHQ_axy-XO9l6EjiEen4Ktl_bf9JIkvZqmqNcy7BTT0ePWq_1f1IRZ5YcPX2xFhndpN5Zoc208b7FVERMH5k4wIK-6BiLZpdwr9dOBtv0HdRpaCvclZDd_GHrYMfOQxjGT65Tl2UOvhdj30Us6eAeceOdsxLakhfodY_jL_9b7bT7bRmwkq-IyJDtZDSdpY9Xw21W-WEYMJQlYdiSykSgg4F5JFHDWEKfGFML6iBQiRaawllF7v_5eCej0K629-jwwSZYdzHDWjUMai5PqHVcKBSSEm30B1HdR7TpQlXzY6cDktCsdJsLxHDaSnr1tF_VB5GfXN0ogC8aZ_e_sD-e2WGOnNznjSZCisGG-phFZ90" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=iRyaHBJmJWGSFzvcPOSzIjaxBvn-gPbj-jqXnGsGcsnN_c_6CNHUg2MYzrzxhxhGIZGi8mio8FP3fFLF_XWn8J4ntxVA3pZcYupI-20_i0tf_5xInFEkQUpUWS7aO5O77FtPE2HNJrfWonkQ3GnBUGlN_jPdyC-6GI15-i57VM6mLt_z37wW_PjHCAFGDux2GKn54gOdv5V-ttJhlpdGqLWdpLlHBvJmPn3Zc6415z_C9zDlHyFEvba8ib3na976-taX5n9tCjpz8838vra7DrDwHl-jqF3HnpJU4HX9ePnpTZ2h4hfYoHW-waXD8VMfHQ_axy-XO9l6EjiEen4Ktl_bf9JIkvZqmqNcy7BTT0ePWq_1f1IRZ5YcPX2xFhndpN5Zoc208b7FVERMH5k4wIK-6BiLZpdwr9dOBtv0HdRpaCvclZDd_GHrYMfOQxjGT65Tl2UOvhdj30Us6eAeceOdsxLakhfodY_jL_9b7bT7bRmwkq-IyJDtZDSdpY9Xw21W-WEYMJQlYdiSykSgg4F5JFHDWEKfGFML6iBQiRaawllF7v_5eCej0K629-jwwSZYdzHDWjUMai5PqHVcKBSSEm30B1HdR7TpQlXzY6cDktCsdJsLxHDaSnr1tF_VB5GfXN0ogC8aZ_e_sD-e2WGOnNznjSZCisGG-phFZ90" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/96638" target="_blank">📅 14:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96637">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee3960474.mp4?token=g-1tPIywVuw9BnF7tGqU9RW5gl1xbAMtL_pwLhX_FfGr6q82-60aD2xRB6Rv5Gs88v6WT3tw9c7wfw0eTdqHAZgcpoDmVHKOVJDwkQGvU8Nh-Fpp5NM-PUkHCwqUPn40IQVbZsWeXSCsU0ouPySprI4K9TKo6Jyc4dFeuLKMZEFGmjmo6k0EovHsZ8KpyfRT7HKvxb8Fep-xYNh39NcH4sMU6WOwLy-UY6Q3nU0aLuyb22wNIK13NwwACJDiyyPnGyys99bz9wFVguRrwOPdP7amt2f9AiUPVF4UaHGfzw9KQOWMOYAFGLZA5riQXXP5q2rEkXIWqrDOGZ-88HprPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee3960474.mp4?token=g-1tPIywVuw9BnF7tGqU9RW5gl1xbAMtL_pwLhX_FfGr6q82-60aD2xRB6Rv5Gs88v6WT3tw9c7wfw0eTdqHAZgcpoDmVHKOVJDwkQGvU8Nh-Fpp5NM-PUkHCwqUPn40IQVbZsWeXSCsU0ouPySprI4K9TKo6Jyc4dFeuLKMZEFGmjmo6k0EovHsZ8KpyfRT7HKvxb8Fep-xYNh39NcH4sMU6WOwLy-UY6Q3nU0aLuyb22wNIK13NwwACJDiyyPnGyys99bz9wFVguRrwOPdP7amt2f9AiUPVF4UaHGfzw9KQOWMOYAFGLZA5riQXXP5q2rEkXIWqrDOGZ-88HprPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استعدادی که فیروز کریمی تو بازیگر شدن داره رو هیچوقت تو فوتبال نشون نداد
😁
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/96637" target="_blank">📅 14:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96633">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FhGFN7x3RiZsIo9GUYOzc4dDF5eWIcAfal1MaS34AIhm6VebtMmd7QUzJmm-snjpN6kC2HjlNncRCadvPCdlWNPU6xdO_G0Xo0I53xqPYpeBlOZSVLLVEWrLA9CnXphRV9krqyxedzMYoApWEzE18wuN5QgmdYSZiFVqloa8iyES-UAK8LqfzTJjlYATZaHOhrDI32MGBVKkBq4wiStxyDgyaM859f6TP0HQc7ssuDynJjcjYA_YsnJBV7a_3rN-joGrh6GwyLH4sCrcmM-mwHSlht9doAgRWLCENriHTurvbF3geQdogrNYCAiWMWO_SydVHC-ac8KYAgZB08oI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UL3zV9QE4KNG_tw-XnV-Z5ERfkeURLXmHNpqcE3tsWADnAC_dviMlA83MC-ZAUdlzH8iaqBhgZWZukE4ZJLlD9ROFrOuj_wMYlRuRqnGgCoLs9vNGUbZ6CJcSpVlA8WbbXuTDl4uTMJ35SfngLe0pXUTcBrKm-LgFHHE4skO1AyPnIAc-yKtLMoF5lH5YqaLZF3VMuEQCe3_kgKFXM91w-EeHMUb8b3Nz8w3fPk4uXqiKjUIYj3z6oA0Mu2kaI3AtKcvRXUOoV1iGPv5dusp_Eyh2riVlN-5JQedosdzBfavSx27kB8C5tdW3c77p4_Wv3qQXhfmXoCe2CvNYxiZnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ruS0srm9o8yB_PniWhMBm0gRNUvhpwE47GXObZncUbUmSmPzE5gBEP5Gn1LiiX1FLGPlq7UcUDVYcL6L2RhE4Ho4jl5DG2Ra-1U3v3xMkZkk42wuqfz91PhA-E0NBFW_Kk74168TAZ3OACgzuQ0bJG0GTtM9js8KzHFooI4Rg2GFp0n4bxohqJg29xOxMxY9fBX8TQQvJCFGTAGKxTz2xjKYYBSfYFCRIWVvU849e_43s4qyTE8zKbXDDiElhCxr5-FJ9g8_gCkcKnX7kwHSkW8kv7TQ2_sOxNHg5kZn1gl6erAYYQ1naaTdt725OI7y9yjVeGIyb9VplBW0OpKYsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NybKXU4kg-8rep4TgR4MD-u0ASz4GzaWJ26juyl_kWoSUqEzANPpetTC9yely0SDfliSVal3-r5SmGOP3bk_PLOcOUk5F1k1DW-OLTUeFydwUIGOgs7CEiy2VGnEPYbTtfyON3VGIzbXQiNl0fyiLw9slhFaQIXyyLe-4RVbz1QGSBx4oEKMjkfmfMsfw6QOrm27ySuQ8RzeZfREMb9OuX6KKUdqtcXWzwk1KP05gPwkPru2SnjC8sOtrrCn_JitWEeD0wWRdXRmae2GLzim7XYa3vO3MPqJBASBW4v20O_ElCTQAi4s7FdDvIbuOZhcP2epNv1kmJkT_9FL2GsjfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پس بگو چرا کلمبیا صعود کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/96633" target="_blank">📅 14:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96632">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6330122b85.mp4?token=U78NYvdWSBJnvXV8YcADaj9Oz3x9VfGqrZS_Sjm3qBH7a5Gwx6AL0tbP-WvWqilkOo3r8VcwcwrEOGqGS8gaiopQxkOz3BExbQBX73KMr_oU-yJ5pbpHLZhFTkJ_iswmGUEEsJxCm7SKFiJGTTOHp5Wrar93uWNgWhlyno6cAlgHL6ZtQ7NDGzzrTGqnqXJWAUjnDRndM9jrl5Toaht1bzUArE1jTnLGjREbeaWr4SCPw1mMWeApF-hqmxXhWWK5PpmeooldAvGZkXOiICFZZ_ACXI6ansK9lhHkkElQlduob-WLFUMxvE-T3VIk6Yyg9knCdRDz3MDg7mbtSoduMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6330122b85.mp4?token=U78NYvdWSBJnvXV8YcADaj9Oz3x9VfGqrZS_Sjm3qBH7a5Gwx6AL0tbP-WvWqilkOo3r8VcwcwrEOGqGS8gaiopQxkOz3BExbQBX73KMr_oU-yJ5pbpHLZhFTkJ_iswmGUEEsJxCm7SKFiJGTTOHp5Wrar93uWNgWhlyno6cAlgHL6ZtQ7NDGzzrTGqnqXJWAUjnDRndM9jrl5Toaht1bzUArE1jTnLGjREbeaWr4SCPw1mMWeApF-hqmxXhWWK5PpmeooldAvGZkXOiICFZZ_ACXI6ansK9lhHkkElQlduob-WLFUMxvE-T3VIk6Yyg9knCdRDz3MDg7mbtSoduMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
وقتی کله‌سحر تو ایران فوتبال میبینی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/96632" target="_blank">📅 14:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96631">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54816ed9d.mp4?token=WyQv9XgMpZQCd71SJyPmN-Ptk-giqNZJTl3-6QPkhRBALJYYytjSEpjyUi1TH5nqccN4thoLe9L74qLK56ep3HCcgdyRKdWOUAqw3DxirhtmkmkjBf14XPFmMchtlzz8o5l9sDFHU0jzEieHuDOg4lh_mo9XNpGpdZowDmmPSNdxRNbrWCm9Ctw7hDttaEQSvsPSiTSlrT0DD4rpf3XZXEB2IQ2tvlNSMJH2yff3jt884FRlmjIcF9rV-lWgpoWdYPxaXIS9ESERBHMFcDTDcwn-bTfoijhO15VT7nr8-1A3GrjvmZ8bieuNCQTxGdbyZrbqeNGee2bFalqgSZ_XIIqC9O8QuElyT6IEKlasZf267n_sDJeKHnmxHlLvsk0p3Pdj35FCjUYfDZ9lbH5qYxwSw1lCDsbS_b4MW-X1HF-xwdNLZLdFNJX4LyTb2n5SmW6jx0uXgnWzQh-81Z-NzE0tnHjeFrUY3RMMp5i7kXVNKd6PZrmbe95gGYkShpByHoCRBA2TiKJBqECblVMRtTfx1MLdrI36FxML6a1y8Lhf3xlEYi4mFVtWP_xzhQSneTF6AS_GgGD0ruN8LTLubhABNTPBFdV3tQ7cfUARsr_BvZ-iqhIEacqE7TWzjjlLzAB3_ihp9JjrphMc0AWmcUCupEn_RNm8tHSN63Z1KWs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54816ed9d.mp4?token=WyQv9XgMpZQCd71SJyPmN-Ptk-giqNZJTl3-6QPkhRBALJYYytjSEpjyUi1TH5nqccN4thoLe9L74qLK56ep3HCcgdyRKdWOUAqw3DxirhtmkmkjBf14XPFmMchtlzz8o5l9sDFHU0jzEieHuDOg4lh_mo9XNpGpdZowDmmPSNdxRNbrWCm9Ctw7hDttaEQSvsPSiTSlrT0DD4rpf3XZXEB2IQ2tvlNSMJH2yff3jt884FRlmjIcF9rV-lWgpoWdYPxaXIS9ESERBHMFcDTDcwn-bTfoijhO15VT7nr8-1A3GrjvmZ8bieuNCQTxGdbyZrbqeNGee2bFalqgSZ_XIIqC9O8QuElyT6IEKlasZf267n_sDJeKHnmxHlLvsk0p3Pdj35FCjUYfDZ9lbH5qYxwSw1lCDsbS_b4MW-X1HF-xwdNLZLdFNJX4LyTb2n5SmW6jx0uXgnWzQh-81Z-NzE0tnHjeFrUY3RMMp5i7kXVNKd6PZrmbe95gGYkShpByHoCRBA2TiKJBqECblVMRtTfx1MLdrI36FxML6a1y8Lhf3xlEYi4mFVtWP_xzhQSneTF6AS_GgGD0ruN8LTLubhABNTPBFdV3tQ7cfUARsr_BvZ-iqhIEacqE7TWzjjlLzAB3_ihp9JjrphMc0AWmcUCupEn_RNm8tHSN63Z1KWs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
کنایه‌شدید مجتبی پوربخش مجری ورزشی اسبق صداوسیما به افزایش قیمت‌نان...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/96631" target="_blank">📅 13:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96630">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOd9KRGmY96oYWOpgx-F8DfTo_ouHr1EHlwnKSsfTwPYzdYiw9-zPrdH7iz2YICXk6dmehl1wW-MqpdoT_H2OnVAz5VM7uw1VSHUqCAkMKK7mSD5A-8G-1gaHTqyZDLvDVSHOPijKnSs3ROz1zfPAu8ZmCJtaijXzXKjfffcKJJanGcf9HRDZ0xWIO5Srb_IKdvk6wOnrCVWRq4mIaueJtzhx7SnLLSKziJ7HGg8MfmbMiqOfCrIzOhqhkhVRxlV3i7MMwuorqSbh2pPD0Qk-G6xheiZDZ4URW8yh6uF6jsUFb0FKyQ6LFVyPrsIjzpS4ZUKQnREx5WySA7XgfxQ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بیشترین گل‌های ثبت شده از ضربات آزاد مستقیم در تاریخ:
۷۸ گل —
🇧🇷
مارسِلینیو کاریوکا
۷۴ گل —
🇧🇷
روبرتو دینامیت
۷۲ گل —
🇦🇷
لیونل مسی
🆕
۷۲ گل —
🇧🇷
جونینیو بیرنامبوکانو
۶۸ گل —
🇧🇷
مارکوس آسونسائو
۶۷ گل —
🇷🇸
سینیشا میهایلوویچ
۶۴ گل —
🇵🇹
کریستیانو رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/96630" target="_blank">📅 13:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96629">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f50e7c88e9.mp4?token=OgWmP5jaM3V1NhuZcaVgMcFD71p-pWc5POq35dSlUELkNz5qEpW06xBp1-AWGXdfUKM_l4qYf5bl0wBqCHHreTjm_QuhngAUxWCkPhKisDOIvAyle7b9V_bfu1L_Yzb-y81YrEDjNdGSJdfyiU8cpPgEy9rzT5EMUBx72bRUKk0x8lUvPH1FDAsCJ9_jbihhlplvPDmjOVQSY7X4wkzi_O_LRCwEqHVr0gY5P0aBGt8uX1s1Uo9D7QNhXKtryZIweFyqoM5Z8f3fjFCXxgrNyuy_NVxsfnI38AcpOPacTC9g4-caDq9cFrhZ6IXhoB5VskjXZopdGHWfQvnjhGJwbIvGls5fMMW_FuZfrTLG79IVS1SYeTzQNHMhzoVCf_E3lZk2PnhpvpvjaTIyxIxSTDHIMTYL-plwJlBphLMwNJCyb9fIgcFdKxhBxH3Tp3PW2aqbT4sLgt7PPCPzKGWS8OKoQeMASAIL-t827mFF65HryvRJiQ-lpE-7JbAhevzJIrFGAYfQMdmQLMoW5Oa6TyE3veMq53od_AsI-KNlk-Eb0-iOQ398XEreo8G9hssdAYCtWOKD-4hC2MoY8G_F5_Ia81ZEtmAsWErobr07YJfAwhEgLNlCDHl3-fihUwFbYVg0IercbjyS_32dUy4-FZ2v7iWX-D0pKjHt-nIQ0lM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f50e7c88e9.mp4?token=OgWmP5jaM3V1NhuZcaVgMcFD71p-pWc5POq35dSlUELkNz5qEpW06xBp1-AWGXdfUKM_l4qYf5bl0wBqCHHreTjm_QuhngAUxWCkPhKisDOIvAyle7b9V_bfu1L_Yzb-y81YrEDjNdGSJdfyiU8cpPgEy9rzT5EMUBx72bRUKk0x8lUvPH1FDAsCJ9_jbihhlplvPDmjOVQSY7X4wkzi_O_LRCwEqHVr0gY5P0aBGt8uX1s1Uo9D7QNhXKtryZIweFyqoM5Z8f3fjFCXxgrNyuy_NVxsfnI38AcpOPacTC9g4-caDq9cFrhZ6IXhoB5VskjXZopdGHWfQvnjhGJwbIvGls5fMMW_FuZfrTLG79IVS1SYeTzQNHMhzoVCf_E3lZk2PnhpvpvjaTIyxIxSTDHIMTYL-plwJlBphLMwNJCyb9fIgcFdKxhBxH3Tp3PW2aqbT4sLgt7PPCPzKGWS8OKoQeMASAIL-t827mFF65HryvRJiQ-lpE-7JbAhevzJIrFGAYfQMdmQLMoW5Oa6TyE3veMq53od_AsI-KNlk-Eb0-iOQ398XEreo8G9hssdAYCtWOKD-4hC2MoY8G_F5_Ia81ZEtmAsWErobr07YJfAwhEgLNlCDHl3-fihUwFbYVg0IercbjyS_32dUy4-FZ2v7iWX-D0pKjHt-nIQ0lM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
افشین قطبی: کارما در زندگی‌وجود دارد
یک دایره ای در زندگی است و هر اتفاقاتی که رخ می دهد بخاطر تصمیم های قبلی در زندگی خودمان است و سرنوشتمان به دست خودمان است. گاهی فردا بیشتر به خودمان فکر می کنیم شاید پنالتی طارمی میتوانست باعث جشن صعود شود و حیف که این بازی را نبردیم.⁩⁩
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/96629" target="_blank">📅 13:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96628">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad26229b05.mp4?token=UaCg0u4sbCtzihLN2HaXxuTVJubL-X9a2unwwlS_YbLAF-XqpGaH25NQx8nBYqrQsH77P2GJYWyq4Ah-rlHtYedNt4i3G9HjUAezrkJACoBEfT4jkyWUDSf7mBFeqddZalBzVg5jdA8JF7x8SPEIKPxTX8RqvRG6FANLayHcYVsr73pXzJyugzeNkOL8uai5loPiYGzOmg8J62ZxISwAk1YR5WmzqkbO-3AenY3dED4W79brncjTTokMiG-NO3xvbdhnpJG8UMJbow48PDYrxu6qtJd2aIrpONI7fcU9cwPejRx3SvR59zNDdge4UQeAsl0PAkZPfNIg5npfsKFJ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad26229b05.mp4?token=UaCg0u4sbCtzihLN2HaXxuTVJubL-X9a2unwwlS_YbLAF-XqpGaH25NQx8nBYqrQsH77P2GJYWyq4Ah-rlHtYedNt4i3G9HjUAezrkJACoBEfT4jkyWUDSf7mBFeqddZalBzVg5jdA8JF7x8SPEIKPxTX8RqvRG6FANLayHcYVsr73pXzJyugzeNkOL8uai5loPiYGzOmg8J62ZxISwAk1YR5WmzqkbO-3AenY3dED4W79brncjTTokMiG-NO3xvbdhnpJG8UMJbow48PDYrxu6qtJd2aIrpONI7fcU9cwPejRx3SvR59zNDdge4UQeAsl0PAkZPfNIg5npfsKFJ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🇪🇬
مصری‌های جذاب بعد از تساوی با ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/96628" target="_blank">📅 13:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96627">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/456a3c4775.mp4?token=R2vb9FDSmv3r8QWTdnDcPEt5RtBz_ehjHNaiKuwqBGEcLN3z3Vj0HPnh7PPljGkOotYOftMZJc0pssv8KHKkibGoJoa8yeiVTf_CqViPz43tNcEPfncGzpMMnIBVGgYLaS4kbBitt6xSqmOp8mmV6GbNhkrm3m7lguQ7Q0NgiVH69kMgFbTiMDrF2FXW5_hyptBEH7PBUHGCfSOakon_tB-l9zIoqUyDp8Rc4LMhcpil7T-oemtX1z-mHD_MoL8LpSxeAA9fOlMr352Rz4WwKFj7kLHf-h4PD6cgyNqOL6AaFDK2rxMnI1kI0xhol9n4v15PapQdMkGhMnkRl3lFKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/456a3c4775.mp4?token=R2vb9FDSmv3r8QWTdnDcPEt5RtBz_ehjHNaiKuwqBGEcLN3z3Vj0HPnh7PPljGkOotYOftMZJc0pssv8KHKkibGoJoa8yeiVTf_CqViPz43tNcEPfncGzpMMnIBVGgYLaS4kbBitt6xSqmOp8mmV6GbNhkrm3m7lguQ7Q0NgiVH69kMgFbTiMDrF2FXW5_hyptBEH7PBUHGCfSOakon_tB-l9zIoqUyDp8Rc4LMhcpil7T-oemtX1z-mHD_MoL8LpSxeAA9fOlMr352Rz4WwKFj7kLHf-h4PD6cgyNqOL6AaFDK2rxMnI1kI0xhol9n4v15PapQdMkGhMnkRl3lFKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🤩
حمله شدید وحید قلیچ به بازیکنان پرسپولیس بعد از تساوی شکست مقابل چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/Futball180TV/96627" target="_blank">📅 12:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96626">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1rO4nWOAP_zsnmFqrbyvwyL0aJPumoL2iCR-zbIoBsgqa9wUJ3-PDWYwWDWEzXy0y2CXPC5T0OeCeWg3yF1lE356pLlmiM-modiXEqVjkgu6-hgn-pufR_WbWvCLx1_xAt_bOuuFOp5Apig7o8wWGQSS3B7tRKRIv5t-sMjT-5La16UZkIIE1l_OUQCvfQyqfIxzLpOQuVZp7XWvh33vu6pUppo7FQa9hVjkTsRMGVjwItsMUdQ52T5odSU150rB12SbRpM7GjPwk2yq5EXONMJspUwKWsukfJpHjvK7kj0sLfwXnS7dTqfNlj31u2n5HFMRlGwUkdtpFA546oHUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ابرکامپیوتر اوپتا:
فرانسه قهرمان جام جهانی میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/96626" target="_blank">📅 12:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96625">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZ4q9Me3yt71Vmj7_FxbjVKVYSUrViBwWB5DQlJ2oRMnBmCZOvgZVx0HEW3LU9iDwc8FFvzfxCL-Pj6p48CIyGBj8Y2s_7M0MtqCpJjwzwHZWAXfIiSYqzeGfYG70M0y9_ijJCT9Qida-lg8ho49w0687OHJa85PoDIR8MfIwfAz_UVP6S7hEMTS4QVKXbcOn-SOpCFlz0mMT49wqkCMwoMOpgUjmG00UaeJyUBMU4YIX_JNDbRaNp29AZcF8g-Y3MwvgCN9FQelfx8DiN63UnFI0G5trmPlr2PlGmN9ff4xipVotmy8GQCnHHwGUET-0aZX3oe3aWaav0B1t6xNqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇦🇷
🇦🇷
مسی در مسابقات جام جهانی:
‏تا سن ۳۴ سالگی:
‏
۱۹ بازی
🏟️
‏۶ گل
⚽️
‏بعد از سن ۳۵ سالگی:
‏
۱۰ بازی
🏟️
‏۱۳ گل
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/Futball180TV/96625" target="_blank">📅 12:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96624">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b6ecbf93e.mp4?token=bk_g5iM9jjua4k1NcPBNzHP0YVA0i3VeJs72itwi77SuHJHXasW99LpGfHXQ2opsWz56IJ-p688FI8SRwNTAnv4DQKPOPiA89fVtHAKQDzL3oLdHhI9ayUAV5LpJ-bZvEY0z0qAwRv_nsnw_bNiWEcQN13VTQKXzInvMSGAlVNbbHe5rUNaY6DHxIuOMf-58nl7SI8XZBysdGg4ulM7ICrBHVd7ltzYEOgcqNyf1b4bm87mAlz-DY6R0Y_7bG2eV8pfvGOK_I1qK6JKYbhSB_hYYqqjQSY6CXo8p4u1VMS9L7w07RIyGBedDKFH7IP_A84IDW_r_XKDuoFENnWPQgAe1-eMqZ2exi_RisUDRpEdlNCPpDcbv8Umz5fYHAc-zX8MwRfeU2KSw5WD95f3Uxo8f00aOJdPpY1VrUWQABmYmCm7VTPnetUz2oJk1KVmGPmcrzhABNqt7nOEocKHEUJ7fqpVzBzLzg65yEOdJ_8A-wuwlLLbkIsd3WvgKxvNfeTSX1E9293-EPzMuwBWSwnw-W4V4N31D3TuyNSTKPvbdypzK_3Rl_jklOtLVxuknkCbI0NREslU3aYx1M4u9NNO0ESWHn3AlmJxuwxZmrrgYQTKaJ0200o3bMzSBAOpp5If_ml2Z6irAoklWZSMOLwmjgwNmOyQXELAazUk--VU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b6ecbf93e.mp4?token=bk_g5iM9jjua4k1NcPBNzHP0YVA0i3VeJs72itwi77SuHJHXasW99LpGfHXQ2opsWz56IJ-p688FI8SRwNTAnv4DQKPOPiA89fVtHAKQDzL3oLdHhI9ayUAV5LpJ-bZvEY0z0qAwRv_nsnw_bNiWEcQN13VTQKXzInvMSGAlVNbbHe5rUNaY6DHxIuOMf-58nl7SI8XZBysdGg4ulM7ICrBHVd7ltzYEOgcqNyf1b4bm87mAlz-DY6R0Y_7bG2eV8pfvGOK_I1qK6JKYbhSB_hYYqqjQSY6CXo8p4u1VMS9L7w07RIyGBedDKFH7IP_A84IDW_r_XKDuoFENnWPQgAe1-eMqZ2exi_RisUDRpEdlNCPpDcbv8Umz5fYHAc-zX8MwRfeU2KSw5WD95f3Uxo8f00aOJdPpY1VrUWQABmYmCm7VTPnetUz2oJk1KVmGPmcrzhABNqt7nOEocKHEUJ7fqpVzBzLzg65yEOdJ_8A-wuwlLLbkIsd3WvgKxvNfeTSX1E9293-EPzMuwBWSwnw-W4V4N31D3TuyNSTKPvbdypzK_3Rl_jklOtLVxuknkCbI0NREslU3aYx1M4u9NNO0ESWHn3AlmJxuwxZmrrgYQTKaJ0200o3bMzSBAOpp5If_ml2Z6irAoklWZSMOLwmjgwNmOyQXELAazUk--VU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😁
جلو جلو ذوق‌کنی کیرررر میشی(قسمت ۲)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/Futball180TV/96624" target="_blank">📅 12:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96623">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773c01efc8.mp4?token=AcKbdpZjEHf_U8elGyWy8yRZg1nZNNmZlKAgwQ4LVA3AP5ltah3BiGtd1IMyH-OXdhtdfKA1lKcKgdotAbCFobfBrdKU9TCK601lnuz0EMu27TxzFBgucWhyPZPtz3y12j6hOlLycDKQibTMxV4WgcNWgdTuF_dsEmkfwix9eOVfOX_QAyxNVD7n3aADedmUasn1QZlt56jpKPHO0gGNzmc4or525BNX6XWuupNDcw-facWZKLsBWGGByNN_rxrsKGtcqw7FOMejnqEaFRwmYnn0Up_P6KLfbMN7f3_zQN4uFeUBKtXflTz5KfqL01yQ6LMQK6nvJCcHXrArFQkmRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773c01efc8.mp4?token=AcKbdpZjEHf_U8elGyWy8yRZg1nZNNmZlKAgwQ4LVA3AP5ltah3BiGtd1IMyH-OXdhtdfKA1lKcKgdotAbCFobfBrdKU9TCK601lnuz0EMu27TxzFBgucWhyPZPtz3y12j6hOlLycDKQibTMxV4WgcNWgdTuF_dsEmkfwix9eOVfOX_QAyxNVD7n3aADedmUasn1QZlt56jpKPHO0gGNzmc4or525BNX6XWuupNDcw-facWZKLsBWGGByNN_rxrsKGtcqw7FOMejnqEaFRwmYnn0Up_P6KLfbMN7f3_zQN4uFeUBKtXflTz5KfqL01yQ6LMQK6nvJCcHXrArFQkmRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
👀
ایران رکورددار گل مردود در جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/96623" target="_blank">📅 12:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96622">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7L8UjumoLCTIKnr1cba4p4oJMzQDGSbO5Xb8tcMPXUbKWOq00T95iQ2wop6meMDBntLzbsE01YD1CX-pAYtj6mysTkS1NyAPDVeOoc98ciyaLlbY4op-8n8Vwy_nZEc0OI_HQuazB8LBMfNL3wN7PDyEPugnJdZ3e7oJmUn0G0kLXLbyRPWzaajC583xTznwcqhwMpEH5MsbJTnVAoucmDxL0ErrPdOAsxYQ5axDY_zJmjZTRox4RLy_q1gFdWOjO4YZUDEV1lnwNm5WGGR6wzAN_JDeJHlunhazOGhgJy_8pHNMmJlufgbtQH2hgxsyGd89x1nSXFl4hMSuGWktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تیری هانری:
قبلاً گفتم، مسی رکوردها را دنبال نمی کند، رکوردها او را تعقیب می کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/96622" target="_blank">📅 11:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96621">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPxQaIgA3V2gVkIbKJjqTBS5P_AwfrYhxHnmk-Mws2oYYiqG6EPp8AsrvxAslq7L3vyKKZ3ZGFm5KS5Zaqg7NR8khrE8e9abE5dDnUt53JsBQlZlz31Kx7YbKCFhW98tTomr4-46Gx2vS3qwM_D6WT2i7PF4gxtruCZaBf_oVjgVs4KF8P4RyLL-Ss0z-dZ-DoBvpNpwheWgj5EvDNRl2jrYAxnHUKAXoMLdC3LSK2UkBW86FMimrbwEwYhto8tEcMByiy0e3g47i9F-4QxzuAXN18kE2IqdrXpd3MZEnOfsrzRrLVNqjko9ExvwPk2WLMzcbpJTcOA6nlYjPtOY-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
مسیر تیم ملی پرتغال در جام جهانی ۲۰۲۶.
• مرحله یک‌شانزدهم: کرواسی
🇭🇷
.
• مرحله ⅛: اسپانیا
🇪🇸
یا اتریش
🇦🇹
.
• یک‌چهارم نهایی: بلژیک
🇧🇪
یا آمریکا
🇺🇸
یا سنگال
🇸🇳
.
• نیمه نهایی: فرانسه
🇫🇷
یا آلمان
🇩🇪
یا هلند
🇳🇱
یا مراکش
🇲🇦
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/96621" target="_blank">📅 11:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96620">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0juslNCHX45msKJT8G9XDNhwtwkDxhsxUba6c-fz36uql1-IOxRYFVxNMsPP-m7Uypi60LYjGQOT6oywVbGfPVKSwDPfXjzNnYSv28rwqJvoadXKiuEj-RiFjBT2B47d4otTFplVfpJMIvvAdfgk0yUbM-9sthwQAKyhjBlivsZ-qFSFt-Ncl2VnToc-SIM3phuUbrxNkRmenlmN91zwGVraLhV4S0Vitd5vcGaGlVmE4_bp_ZkkV08TxYXKDISPF6rx1WOsdtOULyn0XM81pmL2Zr9Axc-ye2KwOONj6uoprdhx36HBB2wVfPyLspFeGD_8MsunyhISDrOuCz2Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇺🇸
ترامپ: مسی دیدنی است. او تنها بازیکنی است که می‌توانی بگویی بهتر از پله است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/96620" target="_blank">📅 11:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96619">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/957600e824.mp4?token=iCfCfc3U4ZCgYgnd33zbRNAHfZxld7bf0JORZ0jGtYAwNajB8dTnfJv2Y3nBfl6RfaTCfw5lJVkPIG1m9vB9AFsIFnLEMPVKH31vi-3NvG1wX36u7oKLJy1n7PCF3NPI-p4B1I8kxsaJ_9wGXoDtK_08074VEftYahtUas9X2cKtiZzUVKfyGEOOFmVV4807GMjN_Ggv56Kw34vS9BNyvMDbWMk-gxFWWR-8P1sFrD-6JlEqOD4PexuRGmTN5mJzLyXJPDp3sbCl04vB5gaD9ZcYUelr86NstCCO4vyhZ8-IZhf6Egtrm7-aVKC7WxVL3revyP2GAr3vkreb4Kdn2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/957600e824.mp4?token=iCfCfc3U4ZCgYgnd33zbRNAHfZxld7bf0JORZ0jGtYAwNajB8dTnfJv2Y3nBfl6RfaTCfw5lJVkPIG1m9vB9AFsIFnLEMPVKH31vi-3NvG1wX36u7oKLJy1n7PCF3NPI-p4B1I8kxsaJ_9wGXoDtK_08074VEftYahtUas9X2cKtiZzUVKfyGEOOFmVV4807GMjN_Ggv56Kw34vS9BNyvMDbWMk-gxFWWR-8P1sFrD-6JlEqOD4PexuRGmTN5mJzLyXJPDp3sbCl04vB5gaD9ZcYUelr86NstCCO4vyhZ8-IZhf6Egtrm7-aVKC7WxVL3revyP2GAr3vkreb4Kdn2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
مصاحبه چندماه پیش استاد مهدی‌طارمی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/96619" target="_blank">📅 11:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96618">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29e12c0b7.mp4?token=eOoec5CwnEV8n8GGCKrKfirkG7A1YEERTGG9uxANHFh61Z2Vl-9TWUtSr4ZYSR7_Q_wBVHz5m9QYEwm_k6_zKYKz1zk_NCcl3xVLtcnTRty3lyqeio-ZW7OAm3DLkDo6jlBvWyt-nelQt3GSpf-zst6Fui7KsvBN48TC8Yy5j5HCxZVT8WkOGYAaednpVz1lC424FV5n84_TOc0LemULpVR045xxYuYb2_bi-jv0Vl-C7HYHlkhl3c_ezm0cSxHdbLmEISqZGsjaxs85AJAt2WsXtaLzP8YTaqljr2RNb3h7_-cZrDjgMcvfAdT-UTpOZXZgLejQ-gnJ1tTCDcR95Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29e12c0b7.mp4?token=eOoec5CwnEV8n8GGCKrKfirkG7A1YEERTGG9uxANHFh61Z2Vl-9TWUtSr4ZYSR7_Q_wBVHz5m9QYEwm_k6_zKYKz1zk_NCcl3xVLtcnTRty3lyqeio-ZW7OAm3DLkDo6jlBvWyt-nelQt3GSpf-zst6Fui7KsvBN48TC8Yy5j5HCxZVT8WkOGYAaednpVz1lC424FV5n84_TOc0LemULpVR045xxYuYb2_bi-jv0Vl-C7HYHlkhl3c_ezm0cSxHdbLmEISqZGsjaxs85AJAt2WsXtaLzP8YTaqljr2RNb3h7_-cZrDjgMcvfAdT-UTpOZXZgLejQ-gnJ1tTCDcR95Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تصاویر جنجالی در حاشیه بازی ایران و مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/Futball180TV/96618" target="_blank">📅 11:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96617">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
‼️
درگیری شدید هواداران ایرانی بعد بازی دیروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/Futball180TV/96617" target="_blank">📅 11:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96616">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🥲
🥲
شادی‌ عجیب اعضای تیم‌منتخب ایران در هتل تیخوانا پس از گل سوم الجزایر به اتریش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/Futball180TV/96616" target="_blank">📅 10:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96615">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiNS2I9yZQhyaFGXsmR5FZarvCCziVXh_-bwofTAclWuTRMRyCS3a45Z7J0dMoLC0fxIx7Rb7hG3yGEo6eamOEOrwPk1b4-Fbv0bY6i4PBEIxBwuPta5a_vIVmn2bGPJATEI9cICu6Gs5XX1_Zrz2puM80xr4MOLQv2cRiCNsVrgpBsX0Gk6Hvkqo9bmUdV6pQ4DU6Ve6vdlOwUkj_bDsF68xNll7TGrupU7gKAT_GlPyt68vosttE4Cx9WO_nr7N--PkH_KD9efoFg1cj187t4QG0BKePAQmH3PMD2OLGZU7_gQjtPTr1TWGJe-W3E3dPPVCIfAMffQeCQ15pb8BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇦🇷
اسکالونی سرمربی آرژانتین
:
🗣️
لیونل‌مسی امروز با من صحبت کرد و گفت میخواد نیمکت‌بشینه تا فرصت بازی به سایر نفرات برسه. این نشون دهنده شخصیت بزرگ این بازیکنه درحالی که میتونست به رکوردشکنی خودش ادامه بده اما تیم رو به خودش ترجیح داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/Futball180TV/96615" target="_blank">📅 10:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96614">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a4bb6889.mp4?token=fBdmhWB3bHSkp6W80parhojLiHeD3ISidu9UKLm2dKhwz-YlmTa0j7deEbpER2XXr41CCl3PcS_oCZ-d6_k0KcaFCBPVpUYegKK96X25ObJNP2mAYHSEO4rWzrFYFgh6anvTxDMgIvRMs9tZetUSH0D_jrFOxpaI4ORQP8O0DfZL6vnwxV1UO1og4I9G9q10iTOgTAhGDZH3psY_yFL7mpd-g3OxPn-0yprBjUAXZXzRc9Vp0BT-kdOo-O0aZ8OpGbKsklrQb9swBixGfYh8LoX_Dtpub4IYQKfApH3SEHC7NOrqK081vGd0-Jo2gOcBhcS0mgD7LXp344VFwzja9nDu7jSrbJCIr7TBvs0rp2YeK--cNNkdLKRWbuUR8AIO-1s-6ZU2F4RC0UTRCEY04UVMe-zUAGnidfB9E35GqLJ6Gdesquw84SfxK8cWsukIxyHprAtJTJ5mSO2N1hMEgZwxbwMKu-TDkLs_rrMHi9TuZfI74EqjsJdIXqR5cKb_mXWEWAMmlwZ3aWEDYbyfO3JValB2HUMo4vlPb1Tgre21UFv7xagIzLVsTgtx0MDP4AkWMbok2tBWVtYu6-EmLofF4A_ge4GrK_pD4U52JJTyZlyFdEejrrSc86O92-NcXB0t2-TgOkDsi_nfYRf_0HqxAeaH_ycpoWT9qO8-oyI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a4bb6889.mp4?token=fBdmhWB3bHSkp6W80parhojLiHeD3ISidu9UKLm2dKhwz-YlmTa0j7deEbpER2XXr41CCl3PcS_oCZ-d6_k0KcaFCBPVpUYegKK96X25ObJNP2mAYHSEO4rWzrFYFgh6anvTxDMgIvRMs9tZetUSH0D_jrFOxpaI4ORQP8O0DfZL6vnwxV1UO1og4I9G9q10iTOgTAhGDZH3psY_yFL7mpd-g3OxPn-0yprBjUAXZXzRc9Vp0BT-kdOo-O0aZ8OpGbKsklrQb9swBixGfYh8LoX_Dtpub4IYQKfApH3SEHC7NOrqK081vGd0-Jo2gOcBhcS0mgD7LXp344VFwzja9nDu7jSrbJCIr7TBvs0rp2YeK--cNNkdLKRWbuUR8AIO-1s-6ZU2F4RC0UTRCEY04UVMe-zUAGnidfB9E35GqLJ6Gdesquw84SfxK8cWsukIxyHprAtJTJ5mSO2N1hMEgZwxbwMKu-TDkLs_rrMHi9TuZfI74EqjsJdIXqR5cKb_mXWEWAMmlwZ3aWEDYbyfO3JValB2HUMo4vlPb1Tgre21UFv7xagIzLVsTgtx0MDP4AkWMbok2tBWVtYu6-EmLofF4A_ge4GrK_pD4U52JJTyZlyFdEejrrSc86O92-NcXB0t2-TgOkDsi_nfYRf_0HqxAeaH_ycpoWT9qO8-oyI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
این 3 دقیقه هم ببینید جالبه؛ گزارشگر داشت بعد گل سوم الجزایر خودشو پاره میکرد که یک کشور مسلمان به داد یک کشور مسلمان دیگه رسید. به دقیقه نکشید بعدش الجزایر گل مساوی رو خورد.
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/Futball180TV/96614" target="_blank">📅 10:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96613">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/949f56bccd.mp4?token=qMQZJhXgUmw9bfAHHz9UQTLabseHn3dIJhn9xltbB5AQ5b19-TsZsTVrFQrBdmBWVuvIDQNpbW21jHnbcKkmLJ0PpVhSsliUAkEEE1ldCGKNC8ysalMTfVOzv5Phvqtv95pBMBytUn8d5nS6ptihUrLrW1VMq5N3YPV7bwqJNTZkqx0aGpKpk0SSZGPZGkfy6kCeZY2J5i4GrjB-duZdxzXbYie-zubspDXkup-Gjs7jfJdaVyTxHPg_FScl4lVcxpBZsADJESc8O9xxBljFKoRlyXFBB2ItW2wWXCfp967WlGNFQrtxTuenbnqy1j8krTq0EYCouFihqC66Hi6X_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/949f56bccd.mp4?token=qMQZJhXgUmw9bfAHHz9UQTLabseHn3dIJhn9xltbB5AQ5b19-TsZsTVrFQrBdmBWVuvIDQNpbW21jHnbcKkmLJ0PpVhSsliUAkEEE1ldCGKNC8ysalMTfVOzv5Phvqtv95pBMBytUn8d5nS6ptihUrLrW1VMq5N3YPV7bwqJNTZkqx0aGpKpk0SSZGPZGkfy6kCeZY2J5i4GrjB-duZdxzXbYie-zubspDXkup-Gjs7jfJdaVyTxHPg_FScl4lVcxpBZsADJESc8O9xxBljFKoRlyXFBB2ItW2wWXCfp967WlGNFQrtxTuenbnqy1j8krTq0EYCouFihqC66Hi6X_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
آقای‌طارمی حقیقتا خاک‌تو سرت
😁
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/Futball180TV/96613" target="_blank">📅 10:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96608">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L1l23Zw2Nja9CjtoFEa19J6l5rIo5SuAerGC7KRTZOQsc_MbsFducxRmdlyxk9iO3VDFZIklD0gaGeeKvIaWpq7g2EDb4ztegHsOkX6sBx84tVd7t0KRd35uGlI1u3injpf4zbUOtBarvTY3YKVXkZIN9Lh96AEaqSGeLBUCwukaPptSg_TvQBWJhSDgYtgkKqXs8dId_ruuJTcY1d8Ogp8YIvjuGqNvTFtwm9AcCNfpZ8Uv58NAvOWHyhaMlwUC0QzNoncN8XVs3Y8x2Aj5Tfsij7fjT9xJLtK3gkD5qZ1lqYlkggXhE8t5akengWaauUKGb-2fFDybba9YUL3uWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9rcAOPSz0_ct4MSt-Sqc0mkPsWaaFs6KCO0MRuRXJwlmQduIDIUGbd6IH83uOzUi1E96k4TjTz7sKtC30zdO8ChAQkfQUSoLzf28kmFUDmMJl2y4ReOzZSavDuI7AbiyloIo_Xfy0tcx5lr-Zl2BxPUtm60M1fuiTtI-rkwgtECr_OlnGOkSrjaBja0w-0yZsTUbFsZhqwHRNzrOzdTzaq-iipTulXXnLW3LnO49c5n-3tF2ngnMTuSfDYWcb-R9KX1Z0ofW0bLSDXVbRQ872MOY5ESlKiAg-PG630ASMQA8M5AK_Ig3az0kvLKYaHIcPddbmq1lObc5rsdKMmsSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HdDeRHU_KiG3NkaZDvesO_gl3KNl20jUhxmTMUcquEZ_Tl8JIjcEHmo78vzjgV8rTWoW9mh5ZDIQt-tYJ0q7DHbjNnJpSR23dS1d3lCn2_gC4CsLgFOHH7O70OkKqf7rjA5647WNEkQmnJwAasDrRpz3U8xpco5I6Tm-RgQWNb7IUySBbBfEIT4_A-Cb3kvwreOuslSlosLHg7iubjzcoUBwX9X-9EDANcPqoIlm7NUnI2--iXFBy1Bsuaj8b2Yy0j00PZcJ0tNh-CRZhEl_Zt_3jj0ZtWFRsQE8KQfZYsNrZBPlUDRcwljLuRBOZeOv0dd9vVYKomR5TlaAV5G3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p2GWQw10QGZnEsjfdwnVrHJvt-jqKKh6CNLtX5tcCr0kuveLaW8fB-XD7KhbycZboqOs70wYgLqqEsfC7GwMv10KjrWk205-W_leZh29hvJF5qKI6qqjAL8Ea9vOyp3zTLNhGcb109aeVQzMwIkG-drlodBh69OGFTbUqBSzfJWS3UBG9ap2BYQguwJ-wwiqpCyeCh337Pio3k0iuXpvPk2ON6DlGbwLO9Sw7R9lXWZxZnx8YkdPUoXaWF-sFBilj2_twKk7VaDdcBdo-DC7fQENIR8RZ1nMmeKLLnCpjzfzSTL0_4hnoNnppcsG_veNBsPi6L5sqoDPWWvMyybAqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VM3MlzlVxaRvaVh9oi1Bv1iCB5CalGbw-okOqvg1ldkLbcAwXf-1FHCOl1bEogAIBFhqJgP63lufX5JcligMUUQUPEo7gh7-KhRDoPqvyqoIgq9t0ySJK3WQhXJIbF4bfGKD6ek21wEfz4McLUwKBMD6wS3usKrTQ4pbtvCOhIdCTUjz0bunQsCtgl4SzldujLEPUFiNKJKB1w1VXOoZQAXu0QrUVw6Pby-h1YaRbhSbaXHMdeeZJT8KeVw5F9j_PewroOZGgeGRJc00uFMtpX8Xtak58y7XnBjq7eBOqOcsMke1V_RaYC--lBILgoSLn0GQiLBT6s7-VuHRxFdBFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🇵🇹
دوست‌دختر زیبای آقای ژوائو نوس تو بازی بامداد امروز کلمبیا و پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/Futball180TV/96608" target="_blank">📅 09:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96607">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afef79198.mp4?token=Dqi7znXa60CRjp446pBcdJwRDYN7NO0mEF_Hd9cLzJIB5eTsrm8dmRyZG1gegt80CE8d2q2C5-iphroHcYzNI7jqRIGa7Esm4z0jy3XOrAFAeX25TvvpYbaliLKwkq9PL6LuAZKwO0Sz6-xNHlrucKdMQBG5DTABpHrzQHcK10UOW-EpN4_DCkp7zaDxFkuAS3wQdNbTitrIDuOJdEBh2a-nUVZQo4AlFKFQqrNlTQXsAzONeldbKCZy0A4I6JLIN8Dl980PJhKFz83xFcP2RSlzGEfA90OvMrR0n9XGDoFb8-cVI8-uJhD17-EN4bTxqFr4BSDMSN2RA0H8ketMMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afef79198.mp4?token=Dqi7znXa60CRjp446pBcdJwRDYN7NO0mEF_Hd9cLzJIB5eTsrm8dmRyZG1gegt80CE8d2q2C5-iphroHcYzNI7jqRIGa7Esm4z0jy3XOrAFAeX25TvvpYbaliLKwkq9PL6LuAZKwO0Sz6-xNHlrucKdMQBG5DTABpHrzQHcK10UOW-EpN4_DCkp7zaDxFkuAS3wQdNbTitrIDuOJdEBh2a-nUVZQo4AlFKFQqrNlTQXsAzONeldbKCZy0A4I6JLIN8Dl980PJhKFz83xFcP2RSlzGEfA90OvMrR0n9XGDoFb8-cVI8-uJhD17-EN4bTxqFr4BSDMSN2RA0H8ketMMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اثرات نبردن بازی با مصر که کله صبح باعث شده مردم اعصابشون کیری بشه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/Futball180TV/96607" target="_blank">📅 09:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96606">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4378d23f3.mp4?token=Po-zYqFkVswBelMrp8QkS4MD6Sp2wjeDPbGRTIqMaMWRhbQZAEtgFamUWfiucsBeO2cVEtUqlQLnTOsJaC6NwEO0zwhbIHayT_2SrlEZTnUnogEs1gH58ug1WRRiKEHppDI58nkvUcqJ2___IuUJJOiHQO4Gu_kKoEaLgwbuJL942cDPYe3fhYJNgvTGT3HhpFKals2-xUMfF_hvrTcZG5eBijnEI9mpJAtlw90ibEHUaKmI8m4b6kM9w67wuPwgtGLnNj5GI6x1tJtOY48LL_rTx2UZMcrB_4Du8rMz4oXOeJtbIvYF0JGNbb6Htn-2FsZFK_Ccl4p7ehO1zaJJOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4378d23f3.mp4?token=Po-zYqFkVswBelMrp8QkS4MD6Sp2wjeDPbGRTIqMaMWRhbQZAEtgFamUWfiucsBeO2cVEtUqlQLnTOsJaC6NwEO0zwhbIHayT_2SrlEZTnUnogEs1gH58ug1WRRiKEHppDI58nkvUcqJ2___IuUJJOiHQO4Gu_kKoEaLgwbuJL942cDPYe3fhYJNgvTGT3HhpFKals2-xUMfF_hvrTcZG5eBijnEI9mpJAtlw90ibEHUaKmI8m4b6kM9w67wuPwgtGLnNj5GI6x1tJtOY48LL_rTx2UZMcrB_4Du8rMz4oXOeJtbIvYF0JGNbb6Htn-2FsZFK_Ccl4p7ehO1zaJJOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
هوادار ایرانی ساکن آمریکا بعد بازی مصر خطاب به امیر قلعه‌نویی و بازیکناش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/Futball180TV/96606" target="_blank">📅 09:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96604">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XmOOvH_kab3F_2Ce5wibqLcpWQULajPgUe46D6HYlY0TXm9U7LoHwErkC3huEVlt9OIJNHj9jFPfC7zEOeS_8G88G3VKqTAt4LPWuqHXJf8LuWLxQFV2jaM-35hI6NmzBU5RzuoiVaFawYAUtJb7P4PUERLqXJeJS8q3XAuZoMV8Ah3ElLivWiJ7Vw2ehY6NTH4lo695ntlaAPZOV5Cnvk1Ki8nvy4LfquvgEv9LJF_LSkoG3gKZc4buIOnl47nMFyyO5eYA2OgFnhcOjdEQednG9uhtGXUhXgFX6ryPJ294RT_414R51dizzTiSF3yhVwpGBNeQBXbIMMqLsfyWJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bUScTUoVpSbDezrybew5rmnYobu-7KME77OxmdTsp1F0vKwJJNhw8S368ekmHKktZhvwBXM2GAEvm8zws0hlHIy4NphFnKUqDW_Wi4zYiFovlDoy_c39AVj2fSQRJPnYDw_jNtTdBgajaDBVTnUk6tLhQeDn5MSgACO4K4Lgq2kL1s3Ym1EbZDodOZwWnypy-IIAwSyeAQDZ5nsq19MPB0rZxQJ8v_OCD3U3s_nC836h9ZL8dyqVmgVU5M9epc0zXAifztuw18ENK1oVejnS5_H8p7uu8Lu4PtpgyBCXQwMmMPsOgLMY9LVVDLoiKU-VvOsFRcD9ROmCjKhSBRT94w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
📊
آمار از سایت StatMuse:
۷ بازی پیاپی با گلزنی در جام جهانی
😮‍💨
🇦🇷
🆚
۷ بازی پیاپی بدون دریبل موفق در جام جهانی
🧐
🇵🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/Futball180TV/96604" target="_blank">📅 08:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96602">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
😛
😛
میثاقی: بازیکنان الجزایر‌ و اتریش به شکل آشکاری درحال تبانی‌کردن بودند اما نمی‌توانیم به جایی شکایت یا اثبات کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/Futball180TV/96602" target="_blank">📅 07:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96601">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8kWqroMHQ-FQWcEeEwQ0fwpgMeYDO652ZvgvL_db9TnphD6vi_5rwFoIfjQcNatiUiWy3zAU9LygRm9rathKazjSivaxt-Q4h22KBuxuJmPHVr7dUE0Txllyc63BUiQvBTNJMOHOWO7KF32ZjuW36d1CntdKlI3eW3uF9JYIlu_czNj4-SFQcqajxtkFWdKJTSyk0YITiP3-82N0X8LrKKtP9ejRBrBgFDU6rqvsrTeEguASvKZSsZdLWnPy46XncHMzDXSCPLWh36gr2KxpfG02Ph2t7yMdE-Z5XZZ_zMDxNWgIBEyqlH1K6MBglPnZ2yKsv-i5Z69wqxK1lHdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
🏆
جدول بهترین گلزنان جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/Futball180TV/96601" target="_blank">📅 07:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96600">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWjT_vikeMvgwmSCG324Y3Kgqy6FyrjB5ICJKnGpiaYF1r2SRB2T5nE_sCPDxSh4TeJMeLWM_63rtCfqyslbYRlE0pb0d5-xyjoabVPzr8IDJRGA-jqUdeNnPBdO3bVqOvO57Jw2I5mGcH3BdBifQmH_FkMba2J_tfBfAN0SJeB_BRLoaZUkCswON6JXJ4danQs4XGRYCgmh-WG8e-f8_RwmKakKZq65y_LT73LZenyZsusvYuNdW3PYE9SC59rDATtnPVSi8sCQBJHZHMp8UbGg7jMDauzkCOv7_RCXBn2cU-RyBBK2EqSUqShxQ5aq16vTCDcfocfAeTVtIPzccQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس پیج تیم ملی مصر به شجاع
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/Futball180TV/96600" target="_blank">📅 07:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96599">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjtUeprLKcE_tdNUQ_K_tWp0BArpwx3BLHV3X7yw-IHLMCMRo06Vg1aeBwPC_Ux-SKLwF5ajmAq8AP2WDwc3uUwI4RyPzAhadNWSd-RtYao6FbnhaCtk-Mae_-AUv6oDTYtwZL6ZoHkeIXfUVQvbif9tpzO87iDYWpGe3z3VOlONU358DwZAnK8NwpdqTF8LzGqxywrXwuMGCGcyylM2-7viZGGHaK-tA2ZisdWGhojReg08v_qiZthc0Hi6xwc7QDkCAyx6Rqo3owEigf8uLdQm9JOm_ohjLzgGcIyn6MZC0NFyqatxwwytNznS_-0DMlnGGWbJzMl9WqUehaoatg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
لیونل مسی تبدیل به سومین تعویضی تاریخ جام جهانی شد که از روی ضربه ایستگاهی گل میزند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/Futball180TV/96599" target="_blank">📅 07:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96598">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXeKHqWsGmMLeKU7wtagOkXBiCJZjznS9Zpmw6uUs7ZD8vbARI3y2IzjwgU1WkAn3bCmP3HNPhdvE9sGvC2Xv_fF8R6OC0cNuoUSSA34zBGr0cekg6w1e9g-Yv3TKcypqLYuAGCLN0ielAPUsoQe2pC2y2e_Wt2p3T6BJfY350KPMiHtYsmCDmTLd2YFH0JLh0eDSDOZ_fvJ7_O-nRLIn7fp7Fjz7bO1FywFDkSsu9z95BuLkbQ0P7e0t5SWTWPs23YUoprFHsEoJErqPP852NKM2tg2bfOQ0yydTdfJ-w58GtDMGAajZBb2pC1eroqpjcec6INKKACmiciZvif8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
مسی در ۱۰ بازی آخرش در جام جهانی
🐐
🏟️
— ۱۰ بازی
؛
۱۳ گل
؛
۳ پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/Futball180TV/96598" target="_blank">📅 07:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96596">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🏆
نمودار درختی جام‌جهانی تکمیل شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/Futball180TV/96596" target="_blank">📅 07:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96595">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTPm4KVxjbJLfKTLE-m7qYABWXToHF5n472dm6WXve03gtydC8v4ZXuJYhY2gT4wAxquEkjc708hN3KID64oNH7OUiVgCTjGnTdlTgPTWB2Q9COSu0EOmW4DhjAUTQ-qClsd4vJfgrVVtDP7XJipB-cvbY5zhiUwK4yYnUjcYDq2Ia5Hs0M0I3wToQOKh-SJ0GdFsP3AWCmLerKzy1IvNnTB4kX7lSwg5GH3xGAhrGz3Kqk2MML7DqH5g9siUHMlBRgOh3Md_RdILEDgvWbFrxTks1KIsE3ExItwkW-icqJySdks7wGFG0V51x-E0ybB_NORs0at_KBmxpcRZD8big.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
نمودار درختی جام‌جهانی تکمیل شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/Futball180TV/96595" target="_blank">📅 07:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96594">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
ایران رسما از جام‌جهانی حذف شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/Futball180TV/96594" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96593">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">قشنگ قلعه رو سکته دادن</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/Futball180TV/96593" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96592">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پشمام عجب بازی ای شد</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/Futball180TV/96592" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96591">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اتریش مساوی رو زددد</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/Futball180TV/96591" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96590">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/Futball180TV/96590" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96589">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">چه دقیقه ای زد</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/Futball180TV/96589" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96588">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پشمام الجزایر سومی رو زددد</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/Futball180TV/96588" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96586">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pdd-gmU57I05Ic7MdEjlHVa8B4wu45QCenKtG7Ij1AYQRmkFc2CxihnJwmjk-vjdsUdNzya5TI9jTuhNXyR7oTrhUw4509PRosJz0k_9hqH_rwl5iE03VXFo7Co-2f3yhTEmjjbZv_hl2FsQyRUC3nll7UiySdPSgYj9etu2BejAA42BwYn9P6Ob_lN9LXNFnocaBRIyt8is8Srfy8OGL5_Zv_u3q-saORXvQ6LW8Syo5p38gp0QUIuQrmOxF5mj9lecUfubKmBDgH8dnQml2UyKR7B2TeLsHn9RQgx9_zuMn-HNmSCpgkRqQfgAzfbQ8AqYOyCy7ssuZkkmNG2i7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bMWBvPsxN5yALdvy-DzIWbiEy7RRs8Bd5aViwYjvYvVb-CharJAslFeFwqGpncoCs_EZR2tICP5-wH54-dFOSutcXe14F8ApeyT0zfStFGnX8c-b85evuG8b3iLe3GRVZOmM4DRTU1vKydLUZ4G72UFHMh3A8YpdGp5CRuozFXt_ACJcqgEP-ZNqYoNTTaC0np6J9_3bPQCj2wtiID5Cso6xCVfZOn6JOgYYXZadYW0AtkqiF9dsgGL352Vwp4tn4Vj1DHDOw_OU-WFdh9dr7hJSWTOOFxcraOr8FBBXupjf7h-3BLWi5c5aPdGQOHbdLBG3kOBle7r0x7740QdTgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شادی مسی و بانو تو ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/Futball180TV/96586" target="_blank">📅 07:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96585">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F25jvwKETGpkamisCXBIXOmBdDvgVHdLjHydJAbTFHLHnUWU33LrmKuWoHUB4B_F01JRhVRBvDWy_HzhKkXg_Gjhs-DPMe4py3MxI90iOtDL7Joy1oY__o27MfsPZDIstX9lky6WpQOqDumCVkDt5Vruyh-SDoQKRyalTQFjHkrQ4CH9RTNWwdCKsmVlfXVTemlvrPuQDREOzkz-tYA8V5bKzJ2xFkXDsaJAJGPKpjDUfWV22b-JMOhbZLy4FAZ6KPz3rS1z4gyX3_sNBK_05KikZLD_8RWaTxVtdPJNuW-1_P0qwKEubKTNv9JirVJwCidfGhW8oGKF-Xr3kvZtcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
1331 GOAL & ASSIST
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/Futball180TV/96585" target="_blank">📅 07:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96584">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ad9070b5.mp4?token=DEvRQ4ChoyIp_Koeb6W8VHD6Gr6awXAhybDLnjUoDY2o_ffd4Jjfe-zU5zRsz8mLS4gTcmYD0e0i7tAt9QLKT0nyczSkb0ld4K3cAscystTy3MGaaXoBW0ILBUlq4ZOHnZL9DPiYF_45eCBFcZyXtCmQr62M9zE3kaKb9LNaN7d4CA20DbPOD2zQPymsCN3B3iS2WJSi-1Db4pTfDewXVeI2iKzRLiCyEzupp7xwj2E5vG8FLcAcn6XA_PxIi9joUxKPhcdLB6iQRTWqcAA6VBZdVHlLwuQNz05NiPaxQVWauXxvWQw_aEuH4uFeUmioRn0baATDpyHFpNjhzfyt-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ad9070b5.mp4?token=DEvRQ4ChoyIp_Koeb6W8VHD6Gr6awXAhybDLnjUoDY2o_ffd4Jjfe-zU5zRsz8mLS4gTcmYD0e0i7tAt9QLKT0nyczSkb0ld4K3cAscystTy3MGaaXoBW0ILBUlq4ZOHnZL9DPiYF_45eCBFcZyXtCmQr62M9zE3kaKb9LNaN7d4CA20DbPOD2zQPymsCN3B3iS2WJSi-1Db4pTfDewXVeI2iKzRLiCyEzupp7xwj2E5vG8FLcAcn6XA_PxIi9joUxKPhcdLB6iQRTWqcAA6VBZdVHlLwuQNz05NiPaxQVWauXxvWQw_aEuH4uFeUmioRn0baATDpyHFpNjhzfyt-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
سوپرگل لیونل‌مسی از نمای تماشاگران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/96584" target="_blank">📅 07:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96583">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtuqvoWFFM_j8OT43ViTymNW9XKAiEJxX9ec7ZzTOmBwvk4rlV6hBkD0txHxCO0wp-BJArb2ZXv4gTKw0grIGMDywF-62hUk-BtfpKFlevjLnEaZ7LKa7YMGCzhftL87N6DEb-c4BeKWw1ELHec1FmSJFSS5g8Qe6TDNQ-9ropck-xST1w71nGAbi6JXXoBznbxVHPJT3UhC6zjJRjjMeIvvj8QpCzdvex6kDXf_9lKdff5miHud2KJE0g_UKmRggU7vk1E6useigZHtNYK-VyjGpczu52qqCQdbhUmho1OeIsRdlU8UD8bUBC0K7FBG_otzWr8NeFpYCnjZMb0NzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
لیونل مسی به اولین بازیکن تاریخ جام جهانی تبدیل شد که در هفت بازی متوالی گلزنی می کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/96583" target="_blank">📅 07:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96582">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/687290f3c6.mp4?token=uch-_kN2A0TlmkuF5IQ1Dfzrg0nRNysogzx-QLyEB7QWIZW-DRQroUfflvItPr5vyVKi81z9CN-5imWjz3cSbHPvn8l_6dLaxCfW9bGWpAQT2m9Zkcn094jNPPtaUub9zIFbtx7wkPXl7nQXKoYxgMsruf3t-iMP-6hhLSVRyLtTbGFYua9d_z2G0DrmzadT03ey6pKFdy45wcuIap7soGE1y0lfZ-LaA6178gZSTQ6WX2G7PFSVevnc1eYbEPEavYZ4MYqWGg2SU7vUJYr9yW9csxo4SG0zXKTnP2TEhmFVSVWQKmVASv6PpM_sxmQD-DyRGoCSM5M6EBaBnKmRoYpxt6mHftIeVoUoTqE8yyCaK1FNl6WGbCYxhIXvZK93xKBIfnQcsCbf8AQwHRFg9Z5NHSMwQZvs9QC693SV2zRXQPXv-GtEqGQyGBb5hGcWy9dIHpzv4i8eM3xbgb_jvg-Wet68DdR4HccGLEUqRq-1zlimUI5h5C3P1KR7chAds6kz6nylbC8J9AeVhqm5FR-eyCqrgaFwECMGcDVyPnWjkfsMHNt_IEEIhDgIwSFQHn_2M1ZyC9ufht1XdZpQKROajuKa_AzxgxmtGtlDZ58Rklv1Ow0UOCbywFVBZO4d79IWvTweiu8OeGTGN51y9uJO9cwsbaQy1hNtOlrBz5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/687290f3c6.mp4?token=uch-_kN2A0TlmkuF5IQ1Dfzrg0nRNysogzx-QLyEB7QWIZW-DRQroUfflvItPr5vyVKi81z9CN-5imWjz3cSbHPvn8l_6dLaxCfW9bGWpAQT2m9Zkcn094jNPPtaUub9zIFbtx7wkPXl7nQXKoYxgMsruf3t-iMP-6hhLSVRyLtTbGFYua9d_z2G0DrmzadT03ey6pKFdy45wcuIap7soGE1y0lfZ-LaA6178gZSTQ6WX2G7PFSVevnc1eYbEPEavYZ4MYqWGg2SU7vUJYr9yW9csxo4SG0zXKTnP2TEhmFVSVWQKmVASv6PpM_sxmQD-DyRGoCSM5M6EBaBnKmRoYpxt6mHftIeVoUoTqE8yyCaK1FNl6WGbCYxhIXvZK93xKBIfnQcsCbf8AQwHRFg9Z5NHSMwQZvs9QC693SV2zRXQPXv-GtEqGQyGBb5hGcWy9dIHpzv4i8eM3xbgb_jvg-Wet68DdR4HccGLEUqRq-1zlimUI5h5C3P1KR7chAds6kz6nylbC8J9AeVhqm5FR-eyCqrgaFwECMGcDVyPnWjkfsMHNt_IEEIhDgIwSFQHn_2M1ZyC9ufht1XdZpQKROajuKa_AzxgxmtGtlDZ58Rklv1Ow0UOCbywFVBZO4d79IWvTweiu8OeGTGN51y9uJO9cwsbaQy1hNtOlrBz5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم آرژانتین به اردن توسط مسی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/96582" target="_blank">📅 07:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96581">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مسی ایستگاهی زددد</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/96581" target="_blank">📅 07:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96580">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/96580" target="_blank">📅 07:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96579">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مسی هم به بازی اومد
🔥</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/96579" target="_blank">📅 06:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96578">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80fe6f9b5.mp4?token=BjTLPTiQp2oq0ZGDqln9Zo3zxIuHGnHxzxuO7QP5mJ7dWe7xVrH8cZXf0nsueFxWZHK6K7NXSMO-LqlrdfWrp1xB7hmHJIgYCQtwPwbf8Fi1QCwOe_Iuwvt61-2iQ-yDG6rqONNw24TQIhDxlwX21YV5j8UxfzN4y_7A1M2w5SaIDV744rSkFYv_dUSJflfK86wrvnsI11jCed367ZqqhfFCy3-NY1RzFtE_ZBF8VOlQovJuyVRZhvNO1YdDTTURfaAM52lj8hGP3xaZszFHoPcJjZ7NOjAuiNmwzSrpSFGIHaC19K_XEgIDc6BJHQgvr5Q8mUZeDfcO_fmOtEbaKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80fe6f9b5.mp4?token=BjTLPTiQp2oq0ZGDqln9Zo3zxIuHGnHxzxuO7QP5mJ7dWe7xVrH8cZXf0nsueFxWZHK6K7NXSMO-LqlrdfWrp1xB7hmHJIgYCQtwPwbf8Fi1QCwOe_Iuwvt61-2iQ-yDG6rqONNw24TQIhDxlwX21YV5j8UxfzN4y_7A1M2w5SaIDV744rSkFYv_dUSJflfK86wrvnsI11jCed367ZqqhfFCy3-NY1RzFtE_ZBF8VOlQovJuyVRZhvNO1YdDTTURfaAM52lj8hGP3xaZszFHoPcJjZ7NOjAuiNmwzSrpSFGIHaC19K_XEgIDc6BJHQgvr5Q8mUZeDfcO_fmOtEbaKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇴
گلللل اول اردن به آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/96578" target="_blank">📅 06:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96577">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">الجزایر گل مساوی رو زددددد</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/96577" target="_blank">📅 06:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96576">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/958bddc7c4.mp4?token=FjejZRRvPT321oB2NcbpeprdifI1PlhE3wMX0WR3q9Nsti7naGelACCl0joCL67FIUfXRGK0WQUk_fCW1ROFz6FwVk3eY8ToPZ2B9SF5RaxRRIoZEAcuml6u5Fn3M3v1Ht-zkI1ilySAXxcBg1TDlzIH-NXzR3SMyNcuqPJ9qmvxo0f4BgU2MDDw2AVcgL_4JoYmJx-bP-TJAV9aKQEUmegejziRXD6x_n6C3b9b-e0-dumSDTmgGrg8cSDDyFkD_LUg7YuPljTLXsfEe7KEcGc846VPzfaIzUspxdI7j8VAUuJ6Hrn51YMPhsRuVUHXkK_VnQD_dDwPEDwupOWuoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/958bddc7c4.mp4?token=FjejZRRvPT321oB2NcbpeprdifI1PlhE3wMX0WR3q9Nsti7naGelACCl0joCL67FIUfXRGK0WQUk_fCW1ROFz6FwVk3eY8ToPZ2B9SF5RaxRRIoZEAcuml6u5Fn3M3v1Ht-zkI1ilySAXxcBg1TDlzIH-NXzR3SMyNcuqPJ9qmvxo0f4BgU2MDDw2AVcgL_4JoYmJx-bP-TJAV9aKQEUmegejziRXD6x_n6C3b9b-e0-dumSDTmgGrg8cSDDyFkD_LUg7YuPljTLXsfEe7KEcGc846VPzfaIzUspxdI7j8VAUuJ6Hrn51YMPhsRuVUHXkK_VnQD_dDwPEDwupOWuoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇹
گل دوم اتریش به الجزایر توسط سابیتزر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/96576" target="_blank">📅 06:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96575">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/96575" target="_blank">📅 06:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96574">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سابیتزر</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/96574" target="_blank">📅 06:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96573">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اتریش زد
🤣
🤣</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/96573" target="_blank">📅 06:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96572">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پشماممممممممم</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/96572" target="_blank">📅 06:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96571">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اردنننننننن</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/96571" target="_blank">📅 06:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96570">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گلللللللل</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/96570" target="_blank">📅 06:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96569">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/96569" target="_blank">📅 06:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96568">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUk6vOZGhxl6sBcwuSu87U1VTKMvcU7nXnffSjAbHxP1OPzaJxkShC2473x-VRfoLVUcCMN63wq7pfGVLTUzP7WlIgg8DHvoJencjpUQ0YxzkEVRN1_NcnwKxSh4SiCByCiJTK5Ob_AaCXCsC2VRL8QEQu7KeL-Ky38gGJe81xyQwQlDe8hkGPrrcUowlf6Y5fu_hlPWHzKiNu0ScAqXP9t9wquRKCD8W9cD8ijbtj7-J3Pvx2nN5CyLqCxdJ_Zq8x9GKrwXlwNrNy7vF055bPUjjaUpWrrNupW46q-z3X0TyT8QXDeoVttpyVdmkkYCOeyF9UIeKz-ZkGp3lqzsDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی داره گرم میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/96568" target="_blank">📅 06:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96567">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سومی آرژانتینننن</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/96567" target="_blank">📅 06:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96566">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سومی آرژانتینننن</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/96566" target="_blank">📅 06:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96565">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گللللللللللل</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/96565" target="_blank">📅 06:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96564">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ia8uwTEKEbrzbPvXXZEKUxTDH7l1Jz5yRm3uPD4z7ntmXj25qQlJRuPICinX8bSLV8ZeD-KLIbHpzvzezkM9EEurjZgvH1FC4z9wI4tEaplUeD9EQXSs4S35Nj3W0p72c5o_0brc35gcF8Bax8SAKV4TDqWu2TP2HKnkd2O4iiAlxDLwSM8i1T3QRKNianHDE42jpXljELrnpw8ENq3W3FlTs1peES6JD4XRWSi9GUvrWYfqOk2MXu_UO2z36bY_V5pVWeV-y6RU7KXgno27ffrc2TkeG_rV7-xR-ieaGaEVrE0t_ALi_SzZXhPhx40NJAKDqCTMy2IJeMtIOdJPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
#فکت
؛
آرژانتین در ۱۰ بازی آخر خود در جام جهانی ۷ پنالتی کسب کرده است
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/96564" target="_blank">📅 06:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96563">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دوست دارین شاگردان قلعه‌نویی صعود کنند یا نه؟!
بله:
👍
خیر:
👎
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/96563" target="_blank">📅 06:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96562">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پایان نیمه اول بازیا
فعلا با این نتایج ایران حذفه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/96562" target="_blank">📅 06:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96561">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cc68fd1dc.mp4?token=TsIsWL7VdJqNhrbuBZABWXWuta5B_qd6FGE31InwI2fPSfdifafTgGIB8307qvA0pLux2GtcRox9PQt3uEqQYuQI9j5pnnavhdOxA7TngXD_uD7CYvMTNbbX_si49HmJnyh_HS29zQMVfhhTKp6FXXuj9ZUub3s0HZbKCl0TDBdSOwrk-wRKaUnhvfWqVw7Eb2HyfPS1CPntYZNTYj0dNqEv5yPIRnQMb0YBiwJQgi-W2FcYrvdI5RtIgZ_x4oa3b1wbNB09L_vqCU-Uv6sX9nYbqqTE3FR_bY6hfLmVRo0DXvJw-G-mbYC0BV-U58cA7FeBkp_7-QdzwZryW5PDyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cc68fd1dc.mp4?token=TsIsWL7VdJqNhrbuBZABWXWuta5B_qd6FGE31InwI2fPSfdifafTgGIB8307qvA0pLux2GtcRox9PQt3uEqQYuQI9j5pnnavhdOxA7TngXD_uD7CYvMTNbbX_si49HmJnyh_HS29zQMVfhhTKp6FXXuj9ZUub3s0HZbKCl0TDBdSOwrk-wRKaUnhvfWqVw7Eb2HyfPS1CPntYZNTYj0dNqEv5yPIRnQMb0YBiwJQgi-W2FcYrvdI5RtIgZ_x4oa3b1wbNB09L_vqCU-Uv6sX9nYbqqTE3FR_bY6hfLmVRo0DXvJw-G-mbYC0BV-U58cA7FeBkp_7-QdzwZryW5PDyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇹
گل اتریش به الجزایر توسط آرناتوویچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/96561" target="_blank">📅 06:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96560">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">توپ خورد به پرچم کرنر برگشت.
همون توپ رفت تو گل</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/96560" target="_blank">📅 06:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96559">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الجزایر گل مساویو زد</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/96559" target="_blank">📅 06:15 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
