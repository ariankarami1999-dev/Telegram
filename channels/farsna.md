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
<img src="https://cdn4.telesco.pe/file/l7Erw-q6wimGvP1dA2S-ePJr7vAz8glbswkiAN6XOwSK3WT3gLRsGoiI07bi1QfMwt4aqB6d-7naF5IWf1l9Ik5CKymrf2iHRDmEfmbyxG0gSGLg0jLdcwFVAEV5O-m8rmRYE5zRH41y1m6DjINjGD7l0j6_FTiqBNd-4UBI0dgd74E6sT_OfkPVCyWqMblWzR4kPYK2evlycpXYcnHiN8ZwdC2SlCmdNC7VjkjrOUAeBjyQwvt2ZQjq8sRED3ktn3Pvs1vaxUty6UCvgpNcbPxq7ZvqYjIpCOg8KHNp09ez1VcN9QI4u7bJhFWxhJycr80ZZXE9CzZzi2ujtcmCAA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 13:44:06</div>
<hr>

<div class="tg-post" id="msg-443179">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r7qd3RJB6Dy7rY-ud0zdHSfx4HnKTnBfNaKjv1LbeRcdAmXfcXD_uj-4Zslgaf4m5fUMrMXEygPj1Aye78vaPIgP_5UdeTqR_N8Zq7GaPKEjahKGHyKQ9HWPInt0xcK1Pg5X13Qw9lZ9ySbv0zW_13rk9dDNFUUs_j-GHdGVCtOAbHQYjlDPZCox71AL6IEyw7hUa9QE7UTtyDEcC2-mn3V0hVNy2OHfKfoKK8uX-tl5uII6J546e-dggoNXmvcoxKdcN-XVIEehHgtGSAoZuEM4CMWyl9gsXPSy6o8FjdRoT9g4fK11WKab_nJ8yuljSeQLh7MPGsg8cn1qjxB3Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uIwcNRadrOWc0kPENhHWo9gB1ypdZqzlCj_nXe2mWbNbIgOAzFh33UFEUw4GMhqCpOX59MBaNqInbUcmiUu58L6FRY-AEatdo7t4hxTn7RyQlgVDkX9gCsGEGF8OA5Fh-x3E1XM1EU3gjunS6oSEENFDMuzGUXyQAWzBMpqmvuE0To9N51OyKLGH3B8gq3PtUumexyusKIRZpJ7RauifGlJfDWTuvGsQVpt2iyJKC7oRy_f3g5_DWcPVG68y41Y54I43e36yLR40mlUgh7Snq7Tn0WRNwMV2BeepyA0MgRXPZyGlaCmtQ21oTP9PVw1Z3V4rJXnLRNqVYwNd-ps5dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nrVoS4ld5tt0B1p5VzAIrm1wfCM69UVZxr035at3rQxzkoVQ76IqZt-2ThNtgGiRzta3QZHj6GfEnBNNEKaiywxtFFqlosUng06USKckKpNGugZEx8rLfzidOuZ8gr_9_XWW0U01QaFcD8NoWaTSOrNL0CN_6r5gGg5NS7LlLoE-hasxv8mwiyfikOYQHE08MT0xM1DApBMa_kTMbn6Iwkmt4L6ROdZkiOTnRqsCBNF-IzHUHr14T-2PBTyWefZb0TieganiL9kwT4lXkBn4Fnkmys0cUdZAv8F-UdqAlreeuZgJms-0_IkexXgUjlyWCSEvARfm7j5sWQyDiXOjvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ESlEUA0RiNPeowhXzoRh-YZ_Dy2acHKt9xxJkmwSILWl0X2BwE36NT6-75S_yzvq4FKTxrY7DrTcuzGn2qIWAqGbBToWUXSEJp2cBW6piqSusf13d1I7YLpomtknt0l-xm1AjrRAEqGtrS4GQaQbEtrHJGmcg4N69z4o9WUACxhfmuH2h7FoElkldosKLTI3yT4gjS3hqNCeIshF-sYHwUPxXY5RIqkSDDC7GalUpcBClkTJhTUR_F-aZZJ7QEgy1zUGY5Dsbw20ZtIqJU8To4qiJP_femVVEu9ZWtmN-ZxxtNFmEG_S3rz3HyVu41Ny36hMIHuiA7ArEHdvOjXybw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnRhK-QDkiBlJRPMA0yuQDkH_f-igUkEoEHj5Jk_qBhnFXz4_9TrPndjwXwOZ0ppUXvoqYEIo1pwqBgOmCTevIAz2b31a-WKQcTOM-xDck_50U3wO2gS-w4Y77nYn1B-WIh94jgVOxKH24WkGxywWsntczQc4rZNYpZfB1PUkbuhar3JNsz9tyh9s4-HQr_mooFzM58I5wYAMelecYLa-V7kLzGQZCLsHyF1DlRuasAYFRy9w86IO3Fnof4HlLfoOFaWq_ZdxqdKoTQb1Xr90-KkltcBjUeqM0QVVPnM35z_F1wb2KOmH-s1PKQeLLwXgi9MbJTMCnxO_K6KeJ04tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VD8Tk9egkMXr68NNHmzEOlZqhHf9yVOdagcBlKuHcOh-LkoWObe8PNxh1hD34XI_gaHXChrKlYMWl42-Ne6FsM7eqb_3jZzeosYqkEL5-6R7RkX_lTpvRYwrSeVvtAoOz70YNDjGDxGq9qIs6nlvchfJXXg9E3W4Xda6qRy8ngbRI5Kt7uP4E0tdSCbbiF_BCOIzklXi-4cAgSMZukDg9MeY07WeL_LDk1RIR2xv3XLsvkPheimAGyYooEYnD9BZSHE28gqy7vhM8ON74p2DUMWVJ4wNtlRJMeKOXbaHKRHTmjIRzF93TUX82GWkcP_Ty_6FN4BU6zVVNXgFv0d9yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X_oi8bzSmO3w483hnNRx8gTtGQ3Nm-E6ThLW_869hBumL8CsLXtBWq6ASpTdB-mwSeVILF_D31NqOs42hM7DzSsp5IYjf2Rf7_jzsKLuX90ZUuhw0O0NSyvZqeZ9qQ_Gl3b1tSOswh14M14ZRAaC0Tvu0oAZnX2FTeQ2bKg4qlo5JCbQzl7Wz9P6FDgsbWk54R_amQ47jtdwp-xSENEBv88_vuVwNjHqkNZ9kcyqjK2_k7AVxR-8o5DguYgLOdGgKyYRFC6f4eNvuGyfnRIpNt_MRYlML_abOjVHZxqeVAr9H3GwdFdg812TCccJenu5SGhWQVzqXoSjSdhywHRT3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم شیرخوارگان حسینی در همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 358 · <a href="https://t.me/farsna/443179" target="_blank">📅 13:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443178">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/On3ltczWnQojw8MVqXtZ3wf1UkWQ63TqikcGQAyLmFuO6AZtM-RCRZiTJkJ1Z99NLU1T1NOvSiMHRzQx4GGXB3phAkO8_JCMNMbGpmzb-GzIytd330WA0pY6ughYzUXBmxD0UI4S2Jjh9STKscnrphJznUcy8vST9Cc6HdKmpCZjNUEe4saF9a9zGqXgeNxY_emn7sfIeaqq9rP-nV14dWFoIPKKWTTGmAUIYT019jutQxXehhb5tLTA33S-NI7DnxuoY21uyMLmlJAIGHu661Jmn4vbvGK475Q4AnlstAmK0v4gFVc_CuaZhgbcEY5o8Q57wY6GOl4FdJuZ0QqdbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسئول FATF در ایران خواستار اطلاعات همهٔ شرکت‌های ایرانی شد
🔹
مرکز اطلاعات مالی و مبارزه با پول‌شویی درخواست کرد، کلیهٔ اطلاعات صورت مالی شرکت‌ها از جمله کلیهٔ اقلام اطلاعاتی خرید مواد و کالا به تفکیک کالا و همچنین اطلاعات مرتبط با بیمهٔ عمر را در اختیار بگیرد.
🔹
بناست اطلاعات صورت مالی شرکت‌ها از مسیر وزارت اقتصاد و اطلاعات استعلام بیمهٔ عمر از مسیر بیمهٔ مرکز در اختیار مرکز اطلاعات مالی قرار بگیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/farsna/443178" target="_blank">📅 13:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443171">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CPaEiAsNMGaYY7DWsc6w3fjfBBVsmGpnD5MJAbb2FHotJeJxA65xje6UWCfrsH49nDIpJP-SRAFCBafXNqypFosWCuDFNC_FK0cudIaffD57Sza5nanpjrlu6F9dukCyrXA2VT5uiIZvxeK5c-9GhV00_I6wBPxTVvm_WOtUbImC4kSRWDADaOK-HyhgaP_blMetZqGSRz7Lm1bjN8ILMoUCijmbh2g8iIigdpfkcf6KRuw00PIUfQeNl2CsVboqGCr06VxoYUxKLExIq90e_RdSYTRtkw7u1s0KH1HiQAPtoYkP1zSLK7W508N8uAcY4xxB1rc-T3spYcoxO72yVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pdwCEAj_xGM2l50Nzhz1__ZN0WRl32uUexc4v3_YAmvR5tmKnTiTVRFL8i04feDTxdlP4BEq6OXNdf7-CDS6B-ixTRbWVHQpCuAKv1VlB3wo7Zn4gtIUnc_Up10sy2QL_ooHsFxg96PCwyB0hgUDJ7GoyoA612SWWpYw9kFLPR4Jw1VceunMVl1oXVrvKHXSQUaznAePCZwPDr2Erev9Dzu6OzXZZ_ltjQS96NHrDrkYQQFcOof-fFcr9WeywsJV6kyKJuvYb6zat-7a3gEQKOG7cshQ7pzbfxLopBqZYoYr0t-hA9B4JUY8LfDx-dLSB4lq8-ETyVlV4V-68J1yyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQNE0l08OZUR02PWeej4NRtO1KxqR9NoBdKFJxGS-hWq2y5UYyNNC1mZGpANacBIAP5SUKwrG_CYGxVb9ryFdReg5hmgTp-ttmbKBnLN3bYyS7IxltRHNsQiRnYej7RjY5UBDDlqPsUFCOTD0wODbRRG59cbLQjzvPsvDA2UTZVvnnmko2XYHyez_9EeV1c4z_rsXy8kcguKPUjqTYLw4EOamWlfUTrtlmuYnFut4KFiphd9TTCUwyEx-WItfec2UcRwAECx3MAD2KMbhS8I1ZlASsOXM9uOXqLzb4trEbTv6sV9onkSyEgUhzqJHU3basb56Dqsuuk4wzRNWQA-IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LIXyGzoSx4PQKeBzQelN-REIZQ9kDP38AI8OXrbsB9oPnEvvBMTXZ0I4d6iLCvTJWOhnozJ0QX_mKxdIOnOuRyQjgYLgmsBb_I4gKIeWB6csmCtDILW9MGuNmvxzT-VLJ6drMlbDzckGGZY8zHa71-IOHmXaTn11WWclvBfYLpl0Xmd59rH1_GaHJK9vlxKB1jNy8STmW9PMltnfljVtJzZpSG5BvWOJPSGzIYnrthsXRpdjTDS4Go8b14zo_mBhk75X_Xv-Vt2nkRlFfZMywSGzBvsq7Qh6js6Djiq_K332oMgRKm43cS4hTFQZBZHZ85aqqmQ8IatQoKNHkBtkVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WqAATnDIstllFWR97a7M7RNCHGATKfne-5hJk0CWMRadjXAso_v0WR_BDJAqVYt8Do1GQ8-QC4CgEC5btQLCW_fjoeDOinIAejGimIMpMGcQusc_9OLaMnjDlbsRI95b8lmF7eL23bNnTShTFKxaSIA4U4z0KgaX8KvZNXA21nd4tELK3kuZpK5j6v01cPObJ9zTNj0rSdcdL2Wu31LH6RNBCPSpCYA_KO9_70almDG2dFmA006ZGxwfAQ0C5SjGH99P0aHy919nnMYI1Zadz8GI5g29A3cFejmLBlMRODRFxQSimJUOhDPJ_sD7bhoqejf2JlXUkKIANtoQbRNGPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IypdC-keEJxKkzqUNrfVs7QxD4h_MtrO-Fjv633Nwg89BBxDXYRDR4F4lawf_I0VFwG7ang_C6QYhdm7n8tJY-UW_KdfOZEeLVyTnJ5j0ZNA-dXA51yt1hRqM4BP6bvhsmsO9kjBmacedkW8Axo7bkn_b9kubQ0IrmQHibWnq63w3VbUdY2Y1BuM5eV5aqrYVgdOhH_KCO0Y013kSMBk-DB7GOh7WAZySx3wRB02b4UUSlMn9Y37K-YYwmNfCBxSJBEXCmc-7PnJsbKT_C2r9KlxYKC_PUm27OTdgpHU_evv9iAaTPwWtzzkL9iQIKFByS_KlETrUDv4nYPApRbsRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/boZe2RjrVn1C7UMX8hUJkwA0mxFTfZePQRYO93Tpsgauskeeizzevwc41TXvs7UUmME97TAFITsIQ3SZSqAG5NwRh2eqhhzzM4DTXPMNMcZTuVREw0LnLEkpUQSmTePD63zystRn1XBa3bVHQZb9Ws_frc3IGekSur3VQKVnXgbd0KT_wHLgPzRzJR2_mS5t_dnjGXh7sqh85hEBaZJBfoB1jxjEXg4gRc-3AsG7z_V6K0rKC9XQ33_GoOMwAHgIaQpkAnMeUFWbTgCw_bDMCSC_C6Vb0MGSey7FZgIVns6FHwuaeyZq45DQ-7tP1UXRtfFzKMCt2_qLFHOvYkDRyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شیرخوارگان عاشورایی در مصلی تهران
عکس:
زهرا کابوسی
@Farsna</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/farsna/443171" target="_blank">📅 13:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443170">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فیروزپور صاحب وزن ۹۲ کیلوگرم تیم ملی شد
🔹
امیرحسین فیروزپور در مسابقات انتخابی تیم ملی کشتی در وزن ۹۲ کیلوگرم، عظیمی را شکست داد و صاحب دوبندۀ کشتی در مسابقات جهانی شد. @Farsna</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/443170" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443169">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noHIQOIjKZfKTOYfCXsR_c10c_-2qg-Z5Qk7XfJ15gClibtWYVGZrf9ZZwdVGSGnZV3KOFOZwBurX8S48E91Gxcv4Iqy9gaQUhf9aUQcWpXOFLCebLRuUbQN_brA_iHBw9ahcT1FXMNzv5INZUmUv2QQE4m9tWhefxuu-up7JP4wjxdAdr8XPhxXEwDLLWA1rbtOcXtygKo-mAt-Y-KQKJerrId8kAsoqI4o0L572retgOsDbYJK0qYxv_j6VK7Nl3QO4Y1zC6PanEyw6IW8jhZuIP7GF8vzFtBqsZJjmBWaykK4EeOl2wr4abwjdjv9RhEfvFETAsZWZiwjriYK7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت ۱۰۳ همت مطالبات معوق بانک‌ها به بیت‌المال
🔹
معاون‌اول قوه‌قضائیه: نزدیک به ۱۰۳ همت از مطالبات معوق بانک‌ها که عمدتاً در اختیار افراد خاص قرار داشت، وصول و به بیت‌المال بازگردانده شد.
عکس: احمد دهکردی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/443169" target="_blank">📅 12:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443168">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0hSMPXZcUhim2TIZOuDbnNoeVYrfjOpCIgSWl34Fp2NNepxnCDLIbTStqd7bdDAOePRFZKxQh-9fC-v6VWSCRj2gQVpDab-AYQgLa83LZTC7BsJtmdtlebZhABWwyG1Du27iGmwuurKHhX7vxXi39gr6WuUThEWeE1EEvb0V9UZnSRnJ0dcnmsIxhnvUj3zJamIwtRnmjVYe_pKgUYIbrGoXJ27hDYi-Kz2X0yq6fb9KTLkeuRzvlcwIsInvRtfEwtfqmfrwYieDZYDDbkmqSEFd5EySswwdeZmWLVPM85_wnto239D06CXeFPMt1tfPT-7GJJFEaqrUIPMByoaFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین واکنش‌ها و تبیین‌ها پیرامون پیام رهبر معظم انقلاب درباره تفاهم‌نامه را در فارس بخوانید
تازه‌ترین مطالب و یادداشت‌های:
🔸
شیخ اسماعیل رمضانی
🔸
محسن مقصودی
🔸
میثم مظفر
🔸
میلاد عرفان‌پور
🔸
علی خضریان
🔸
علی عبدی
🔸
میلاد حسن‌زاده
را می‌توانید در صفحۀ اختصاصی هر یک از این افراد در فارس تعاملی مطالعه کنید.
@Farsna</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/443168" target="_blank">📅 12:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443167">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5BfX_Lu8YMkSU-3VIxG2QL8_KuWFbud-jUj-bFUexcSRzvWq6tvwYYpt4jSmQb-OR6_LLXHfzI7FQOrxwlh1HVnVlMUHM9XzuNruuphW5jGoJ4EwBou8dQeM6p5mUYmv-QE2kh5Y47BDvkyls7PskAKEHZMgkUKcWvZ_GM3sz3gNm5SZdb3VYLPFRFiyf57PTwvKqH2H2AXZ-8aMZI5tWPFTPJ1wnilwlq8pZvKrQAKxYc1ldiDcm0E9rwlfGf5WxHA48SjGlymVQsldPzaQ_Pcbia6Ve2keyMPNVvlRs_AwIkfBTGnpkUb50twf9aQevqsE3kNnX_TDA72DNXt7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیروزپور صاحب وزن ۹۲ کیلوگرم تیم ملی شد
🔹
امیرحسین فیروزپور در مسابقات انتخابی تیم ملی کشتی در وزن ۹۲ کیلوگرم، عظیمی را شکست داد و صاحب دوبندۀ کشتی در مسابقات جهانی شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farsna/443167" target="_blank">📅 12:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443166">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWc8luT8IBXj56qEsfNsVw7a9DBMrhB4OxlqjqCPw0PmWYUSEjrQrxuKtCJGk9IJhC1g2MopHeD_Hvj3wM8Vm-XTiUKBQZw10dhUkgx7MQP-XxcLMQUdQhnlWv3jLGQktLvrv-x0olmo7V_TCn_j6Mt-fLaAvieqVNJpaTd88_scKKkIYv9dnOUZ8pr0TWFGzSfUVpL3OrleD1MQktrq_xjjUDMJclogF8OQKvMfr9JVhYVPnWiAMUd7lhF2uyJpvxM5ikzciG-C_GkfIeV4H1a02ZSbBF-qkNWhvRKWOGX8cmNG29aLWj1RlQZa75aOGiNn7cO3L6y-RqTa-6tJvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت هیأتی از پاکستان در مراسم تشییع رهبر شهید انقلاب
🔹
نخست‌وزیر پاکستان شهباز شریف در سخنرانی امروز خود در مجلس ملی این کشور گفت که رئیس‌جمهور ایران مسعود پزشکیان از پاکستان دعوت کرده تا در مراسم تشییع و تدفین پیکر رهبر شهید انقلاب حضرت آیت‌الله خامنه‌ای شرکت کند.
🔹
شریف گفت که هیأت این کشور طبق وظیفه در این مراسم حضور خواهد یافت.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/443166" target="_blank">📅 12:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443165">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پیروزی یزدانی مقابل آذرپیرا در دیدار نخست
🔹
در وزن ۹۷ گیلوگرم هر دو کشتی‌گیر برای رسیدن به دوبنده جهانی به دو برد نیاز داشتند در مبارزه اول یزدانی ۴ بر ۲ پیروز شد. کمیل قاسمی قهرمان المپیک یزدانی را در این مبارزه کوچ می‌کرد.  @Sportfars</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/443165" target="_blank">📅 12:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443164">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2V_mbOA64ORlrtR3rcJSV6KXmI7daHzIcUs6vvqn2Ia7efRC5zoDn_wkxf2iRptgXheKcCBWSJjIBAkqDu1xiPUd5QmDlnZcqIKkMBJh9MF6VxGtQcObSEGNj4hwkIJ8fqiE6Sv8lO5LbdnR4Aw7EOJyZD76wxXQxlrNWAZi1mTj7jCqi9nuEnsuZW0xB4g2436IinSjg3JWh31KIO5zDRbvQoVA-xcsYo10lXhNdZJbjgAuIucKLjv7ojW98z6zdaQn208KNG8i_4wWQMPdCfCCKDQRKPI3Np4tb_vwOIEIZGIHBlxAkdbZx67lkqNvQPunkeGqnOqUNu1t0mKeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
استفاده از ابزارهای نوین بانکی نقش مهمی در کنترل نقدینگی و کاهش تورم دارند
🔹️
مدیرعامل بانک رفاه کارگران گفت: ابزارهای نوین بانکی، تامین مالی واحدهای تولیدی را تسهیل و تسریع بخشیده و نقش مهمی در کنترل نقدینگی و کاهش نرخ تورم دارند.
🔹️
دکتر اسماعیل للـه‌گانی با بیان این مطلب در آیین افتتاح شعبه شهر فرش بانک رفاه کارگران که روز چهارشنبه ۲۷ خرداد ماه برگزار شد، افزود: سیاست بانک مرکزی در شرایط فعلی، کنترل نقدینگی عمومی کشور از مسیر استفاده از ابزارهای تامین مالی زنجیره‌ای (SCF) ازجمله اوراق گام و برات الکترونیک است.
🔹️
وی به موقیت فیزیکی شعبه شهر فرش اشاره کرد و گفت: بسترهای استفاده از ابزارهای نوین تامین مالی در این شعبه کاملا فراهم است و ضرورت دارد از این بسترها برای ارائه خدمات مناسب به مشتریان استفاده کنیم.
🔹️
حمید آزمون مدیرعامل شهر فرش نیز طی سخنانی در این مراسم گفت: بانک رفاه کارگران در سال‌های اخیر ابزارهای ارزشمندی برای حمایت از معیشت خانوار طراحی کرده است که از جمله مهم‎ترین آنها می‌توان به کارت رفاهی اشاره کرد.
🔗
متن کامل خبر...
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/443164" target="_blank">📅 12:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443163">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_av3rnQylXWy0ya2moEYHpI0obLQSJOKC7NVvGs_eqDv0mGp-xDuNU6lARKuW7zTSwzj5k7VnXydG35jxqWcNAJtnO-oPad1feIab64N68Kc0wjidaYLR-zodQhVwrd3Uk_euhlfZo03e6K2vNLmToka_ws3hyGekrMtcp81RnuRAKA_h2C3wfSjP83dg4VhlRqhur3ba8ER1gALwOxrxogJVVFt68SWNYuikcKhGhND5eWQa5USt8LfIWLmA2GIvUvnfc1GgRTg263AbO4R5xrgZ2Gmrp4XrtkQ-Jz90TJavf-BoIFtPcfDYpccsP1Pmphx8K8ctKos6yy22I7Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥀
لباس مشکی، پرچم عزاداران حسینی است.
🔅
سدن پوش برگزار می‌کند:
نمایشگاه تخصصی پوشاک محرم و اربعین
«عطر عاشورایی» در تهران
▪️
فروش مستقیم از تولیدکننده با بیش از ۲۵۰ مدل لباس مشکی
▪️
دوخت رایگان چادر از پارچه حجاب شهرکرد
▪️
چاپ تیشرت با برچسب‌های مفهومی
🛍
محصولات
: مانتوعبایی و چادر مشکی، روسری و شال، پوشاک اربعینی، پوشاک مردانه، کودک و نوجوان، کیف و ملزومات حجاب
📍
آدرس
: جنب مترو حقانی، باغ‌موزه ملی دفاع مقدس، جنب مسجد خرمشهر، سالن فکه
🗓
تاریخ
: ۲۵ خرداد تا ۹ تیر
⏰
ساعت: ۱۷ تا ۲۴
✅
ایران‌تن | رویدادهای پوشاک سدن‌پوش
🆔
@irantan_roydad</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/farsna/443163" target="_blank">📅 12:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443162">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/farsna/443162" target="_blank">📅 12:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443161">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8c45c1d0.mp4?token=bAEGPMQOC6ZQMlIrNBOiTaUtRgUkKpG8EdVlm9RfJ_XN5S_Th-VK8REViCpgxPEQycvD-bN8-vg6F19j0QFqvSHVw5adiufur8DoSVq1aVWvW5tlLOSKtU9xzarszbiWIGB0Tc5T6ACKnwfnDO-NAX2Z6bx2HFWquq8Y4R1CUObctvXSLWeTsrFiCxZb0hTcDA2L3aJPfwegrw0D3QQKrc556tM1u_OxlgZ6RnCjCb3j7TurepsyKV8UpMb6G3qTz05bG-CFABSzncsqa_dn0hwf818SseWuIknrV0B2qc3eQO52Z1LvLtzqEPLz5lrt08qh-iZKYN4W9wTRHm2flQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8c45c1d0.mp4?token=bAEGPMQOC6ZQMlIrNBOiTaUtRgUkKpG8EdVlm9RfJ_XN5S_Th-VK8REViCpgxPEQycvD-bN8-vg6F19j0QFqvSHVw5adiufur8DoSVq1aVWvW5tlLOSKtU9xzarszbiWIGB0Tc5T6ACKnwfnDO-NAX2Z6bx2HFWquq8Y4R1CUObctvXSLWeTsrFiCxZb0hTcDA2L3aJPfwegrw0D3QQKrc556tM1u_OxlgZ6RnCjCb3j7TurepsyKV8UpMb6G3qTz05bG-CFABSzncsqa_dn0hwf818SseWuIknrV0B2qc3eQO52Z1LvLtzqEPLz5lrt08qh-iZKYN4W9wTRHm2flQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳ شهید و ۳ زخمی درپی حملات اسرائیل به شرق لبنان
🔹
به‌گزارش خبرنگار المیادین، تلفات اولیهٔ ۲ حملهٔ هوایی اسرائیل به حومهٔ شهر بعلبک در شرق لبنان، ۳ شهید و ۳ زخمی اعلام شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/443161" target="_blank">📅 12:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443160">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0cQSlbAas-WN6q-wRHi5SEpoH4XkrfqVePSzS67aJSRRMJrUQxaigoE45khTIrtZ-gQtWy0soROhEIWMVkJXn6BvQJMwc7C1CGSfQZRI6peO79U8d2rLUCEhDu4iqc_-jFyZNI10HYJgrgo57M6SJfbWwPz5DpOgenw-FtYeV6Xqbv6E2WvL2iRspD8WgaFR9WE5pQpOVj3gsITcpy5EImPIkX_gAr_onbD931Uj6DEJoYDPw0p3VYCMSr-dS8KEPN3pkfMGYNpA0ecJnUlYNFCc63nYIcKilhRXim8efOaQp4XcY6xgjMXHmj25nG8NDgs7EFdFEqlRrJuxVyVjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیرمحمد یزدانی صاحب وزن ۷۴ کیلوگرم تیم ملی شد
🔹
امیرمحمد یزدانی در مسابقات انتخابی تیم ملی کشتی، با پیروزی مقابل یونس امامی دوبندۀ تیم ملی کشتی آزاد در مسابقات جهانی را به دست آورد.
@Farsna</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/443160" target="_blank">📅 12:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443159">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تبلیغ این ۱۹ کالا ممنوع‌ اعلام شد
🔹
دولت فهرست ۱۹ قلم کالا و خدمت در فهرست کالاها و خدمات آسیب‌رسان را اعلام عمومی کرد.
🔹
طبق قانون تولید و ورادات این کالاها مشمول پرداخت عوارض حداکثر ۱۰ درصدی می‌شوند اما هنوز میزان عوارض تعیین نشده است؛ همچنین هرگونه تبلیغ این کالاها در همه رسانه‌ها غیرقانونی است.
🔹
انواع سوسیس و کالباس، ژامبون، ساندویج و پیتزا، نوشابهٔ گازدار بدون قند، نوشابهٔ انرژی‌زا، ماءالشعیر فاقد استاندارد ملی، انواع نوشیدنی‌های میوه ای گازدار با و بدون گاز با محتوای آب میوه ۲۵ درصد و کمتر، شربت میوه‌ای و غیرمیوه‌ای، روغن مصرفی خانوار، مایونز و سس‌های سرد، فراورده‌های سرخ‌شده در روغن، انواع فراوردهٔ حجیم‌شده بر پایهٔ بلغور و آرد غلات، سیگار و محصولات دخانی، فرآورده‌های آرایشی تاتو، فرآورده‌های رنگ مو،‌ فرآورده‌های صاف‌کننده، فر‌کننده و کراتینه‌کننده‌های مو، فرآورده‌های کاشت ناخن، خدمات برنزه‌سازی پوست و خدمات تاتو و دتاتو در فهرست كالاها و خدمات آسیب‌رسان به سلامت در سال ۱۴۰۵ قرار گرفته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/443159" target="_blank">📅 12:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443158">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-text">پیروزی یزدانی مقابل آذرپیرا در دیدار نخست
🔹
در وزن ۹۷ گیلوگرم هر دو کشتی‌گیر برای رسیدن به دوبنده جهانی به دو برد نیاز داشتند در مبارزه اول یزدانی ۴ بر ۲ پیروز شد. کمیل قاسمی قهرمان المپیک یزدانی را در این مبارزه کوچ می‌کرد.
@Sportfars</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/443158" target="_blank">📅 12:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443157">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e5a99e11e.mp4?token=riI3D6hBV6bOVH9lToEpB3o_1nM3ColvxqoD79XaWwwDaqusTc3ehu_JE65tZdbTn2vxL6FpwBOMhEq6nQy3Q2skOlmF3FoQHJACxw-LvJ9zo-DfSWGKmMOlG3QdJsXnhrmfouPL0Ip3lf7dkVVWOl_Pa6kXSLR-gf4o09oP_cYzT6LvlNHj-E7e6twwcukrkZ_xUvYnCLPObk4WtyEiqvy8CSZ1b2JvxiNaLUr0XYwpBTvg5afauVoKIxbJ4zt7VzQq-4vrPlHQ24HNX8fDNvPb0530zqiEbHG2EyIJUFKGXmSmwNM06ul2uKY1yysNsxzLykRcsZ1jRod5VgzlSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e5a99e11e.mp4?token=riI3D6hBV6bOVH9lToEpB3o_1nM3ColvxqoD79XaWwwDaqusTc3ehu_JE65tZdbTn2vxL6FpwBOMhEq6nQy3Q2skOlmF3FoQHJACxw-LvJ9zo-DfSWGKmMOlG3QdJsXnhrmfouPL0Ip3lf7dkVVWOl_Pa6kXSLR-gf4o09oP_cYzT6LvlNHj-E7e6twwcukrkZ_xUvYnCLPObk4WtyEiqvy8CSZ1b2JvxiNaLUr0XYwpBTvg5afauVoKIxbJ4zt7VzQq-4vrPlHQ24HNX8fDNvPb0530zqiEbHG2EyIJUFKGXmSmwNM06ul2uKY1yysNsxzLykRcsZ1jRod5VgzlSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات مجدد رژیم صهیونی به شرق بیروت
🔹
خبرنگار المیادین در دره بقاع از حملهٔ مجدد رژیم صهیونیستی به منقطهٔ تل‌ابیض و بعلبک خبر داد.
🔸
دره بقاع در ۳۰ کیلومتری شرق بیروت قرار دارد. @Farsna</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/443157" target="_blank">📅 11:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443156">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwgY2IhejLXMNGM46G5KzM23_rjPSKnnM1hHvWDqIQxFNM5_ujxaGocVdxQoW1_TivtdwH6r3nQC-gAqIypqb7D5c4kQKiVNdjU6OxmbL8vSvvqTeioUBzexMQxiqsRj6caNlsD1QisjTUIEoMWuNOykhMeGoXuADmiDoJ9_PT8LZz4HQ3f_RveaZP_0S8FcjmRcpDAJuaA5lQ2PqaggUIHW5mF5y3CeNAJXFXY6RF6tCGYX3r9LwXvX_-bFHhz7sNkyGJ5FH3QAwbPO5qYTNHQxeWLm0KA1upA8x5eFL5sJNzfTr5zVfOzoAASKm1bxRrWY9KE1K_CEz47WX_wW4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس به منتقدان اسرائیلی: ترامپ تنها متحدی است که برایتان مانده است
🔹
معاون ترامپ خطاب به اعضای کابینه نتانیاهو که از توافق آمریکا با ایران انتقاد کرده‌اند، ضمن یادآوری کمک‌های هنگفت نظامی واشنگتن به تل‌آویو و وضعیت این رژیم در جهان، به آن‌ها توصیه کرد در مواضع خود تجدیدنظر کنند.
🔹
جی‌دی ونس خطاب به منتقدان اسرائیلی این توافق گفت «پیام من به آن‌ها دو بخش دارد. اول اینکه دونالد ترامپ در حال حاضر تنها رئیس دولت در کل جهان است که نسبت به اسرائیل همدلی دارد. اگر من در کابینه دولت اسرائیل بودم، شاید به تنها متحد قدرتمندی که در سراسر جهان برایم باقی مانده، حمله نمی‌کردم».
🔹
ونس در ادامه گفت که به اعضای منتقد کابینه اسرائیل یادآوری می‌کند که دو سوم از تسلیحاتی که از اسرائیل محافظت کرده‌، به دست آمریکایی‌ها ساخته شده و هزینه آن با پول مالیات‌دهندگان آمریکایی پرداخت شده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/443156" target="_blank">📅 11:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443155">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1370b55f66.mp4?token=Rv9Glioz5euxNQ_n8BDp5aUP27uKLsR8uuMrCosr6ao0-hwCzYXG6Qv-FGWRiW_bdtAAPyGarjVnjwCdG15QAhYHbGTd_LK8Agvxn0P6J4CB-O7ueLZoRQ9VZ_mJgXDBdRRpRivYE2fV8FfcxsrJmI1aiSr7XZlbyq9iRuiqW6SKKzax1X6OrxmpnDJgCBbtUO_ayMI5hfRhuRqKz86AkQD6pQDh4VZXg8MI-Z2vT7JgsIv18eQFPUMYY7sZGs5mkBztdjKRTeRO7tB-Q3tT_UQU86z0iO9phFTYu_SjCVSLGmHTdr5piyfgPzqsHlOigZKWLfwcZg5O35MdDx_EIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1370b55f66.mp4?token=Rv9Glioz5euxNQ_n8BDp5aUP27uKLsR8uuMrCosr6ao0-hwCzYXG6Qv-FGWRiW_bdtAAPyGarjVnjwCdG15QAhYHbGTd_LK8Agvxn0P6J4CB-O7ueLZoRQ9VZ_mJgXDBdRRpRivYE2fV8FfcxsrJmI1aiSr7XZlbyq9iRuiqW6SKKzax1X6OrxmpnDJgCBbtUO_ayMI5hfRhuRqKz86AkQD6pQDh4VZXg8MI-Z2vT7JgsIv18eQFPUMYY7sZGs5mkBztdjKRTeRO7tB-Q3tT_UQU86z0iO9phFTYu_SjCVSLGmHTdr5piyfgPzqsHlOigZKWLfwcZg5O35MdDx_EIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات مجدد رژیم صهیونی به شرق بیروت
🔹
خبرنگار المیادین در دره بقاع از حملهٔ مجدد رژیم صهیونیستی به منقطهٔ تل‌ابیض و بعلبک خبر داد.
🔸
دره بقاع در ۳۰ کیلومتری شرق بیروت قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/443155" target="_blank">📅 11:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443154">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/narglKMg-tyb3EB9zy9gA-4uzjJaNx21hPIhIoImCTu_wBNPU3rtj2VodPO7oiFyjh76AA24R80dQBNkleQDCtp7XDWjDPrI_bWApz3ltlZ12YFKGZozbSZQx3U5b96f9SomBLeabuVbn2oKbgJ0cZJDMtCzmXFZjp0rl3KVcvZNQN1JSa3Xl67nbhfZsQb4-8A88VSBiLWkVVEIulEPXSKEVjDGZSK_1sbnZMb7jAPnQbcvOv24y0Sc3sgdGetKeSY5ChV_-weTneir18P2VH35ygfCphOkoH2E3BtpC7fO4IEiJ0LBXFUd6scFtmRbHo39P1g6bHmSs8Oi8LLhHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ وزارت خارجه سوئیس: مذاکرات جمعهٔ ایران و آمریکا لغو شد
🔹
بعد از اعلام خبر لغو سفر معاون رئیس‌جمهور آمریکا به سوئیس، وزارت امور خارجه این کشور هم لغو مذاکرات امروز تهران و واشنگتن را تایید کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/443154" target="_blank">📅 11:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443147">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h0DjwjZakkd2fxfLOFgdNUIu0nvpZUryZ2VOMQxO_EcwbGaWSgc0I6Cu9zsOkfa7_cdHa63fMOVJUUoliYMTAokOuUF8Dl-cUSV0jccE1NmafueWGMez2mcpsAscMwRk7Tux79VgY8dojvPLbHQgcmTzWfkIualth9zkWLFFE0QOD8VrmvbhL51RWEWe1d7aFnUfADnWnQi0rkS4w8K2h47P66L8lTC9J37pYpTMCjgRHoeeVY3lSDVz6ctE52FNm3sJ2BYAE-Lagnma-XcqekRAZi21v3Bmck_xm1EC98hWJAcoKkAaW1ZNYLNwYVCwjEyByjNx_1LLvmkbs7WTcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dtR6ntLH3hp09ydOqhREtpX0paHUiRBWFI9RHVikyMqfHjE2ijiOxl7bnc4CE1rVwnhdmYYgTsfP_DD6angaHn7au_xYMA-7RezmscEkXHRLZCgNElbQRMzNcA8kjz7-9f_K21-e_o595u8EUOew1kH0EUuReosvs-lGx-wM02aSsGQYGbyeRamuJiDfMTpcNRdbOvZwKCt3SQ0GeZKcUBt9rHWGa9rmT38blgu5VtAwob6sWjPsKVp9KPlNxYa6wDAGJ3eHMOTkqP6UywJFDDkn-QyRN0yZYARdVNhfMsq58XNHHyBaLSuwcfuf7RAsGwfPiVd_xB_JxekMNB6A2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMeKnh3gT2szPTWSDMQ3vh9YHwwc6ImTW8WDONOwdbDymiezAZTWCUpL8N2Cyfj0TMcp9vRvBZfF2i1ndIwB58m5P2V_HQVnRs3i4jDOxg1b05Jp9z6VDkAdO2tLXgGTBLlafwDNhonFzwgC4RBK8ZFJqXQzheyn6Zo3aklzKF5zYbPoufTdQkWe40QwMjr0cPRGl1I4vvDhfH4smXz1kcv_7dvPAXqTuHJVoGX6FG4huFP2qG6Qaf0IOuAwoxVs_Ohc7V9uifyuDd52L1wrYiXFYjkIELJOosBg1mT8FG7U_y1wro3l-Fmq1vi0GlC8uHKarX8wh-iW28pKcvB_YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iPQmk1X6mX5pNnJdK0mMbBewNNILcEhRldxq3TI5-CMBYQvaqYKqs4qFo-0zVN549fZA7bhD_gFnoXJCQhJDCV-YStJvzjae-axAiIOZ3J447vehKHQul6IwOiMVHo8m_Os_27C_AQUoGPIA9pEEryClnqr7CZ-_zyPDT52huGLz3w4WmPoYIs61vmvoiqraxlef2xORfvr_biIuK_C5qp5CtROVwWttqLZNg0VWAuxdMwYn8f3vR-ApXZKeu398P19d73ffd2W5nrgNKWTZfHl7UJPrgUJAZEt7f_EVNb8bbYl8CSU_e0K0lo8Td4qVuYV5StEGr2XqjVlTbbjkMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lP2lGn2QIcioU_-MqTyTFNNQlsmaTWNBz9gmc9I1skmQDAa4nrRa8x8zAy2saorVd1Ksoq1snCkKJHrz6XHEJv4C28N3wsE52DVOflm6-FPRJykz9I6NeSXYoxb6ohfjZG6ss2-4Gr3aHWk8jjaUADOqY0JskQTDbLqBpO1BBPX-wVdkpz1ccoNF86TV9ul1PCXUZYxcNc0CBN4csCWWg18Pck44lloibOHJUUdG4EJE8HpIiC_iFNUIo4qCYeZE7JTVs3EdXsrbtBzP1_Y2Hlt2jwQxjOQR3bBAWMy2xmOJeYmJbsiXOX10AgoyK2KV3JmdVjIKj4eSOLDMllgUUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i2dDoZbzYYjQl1F-AHI59nsMhOzyBhTShdoHyx4IVIu6YCW4FgK-T7_vhWB5OvIVL8qHt3sNVuj83zNvkf6_lxJb1u5RKGtwpUq2MIWLASBNMt9nMdACObfH4JfSOxOaTMhtcxWOPyv_lMgEG96-w_Gm5jnozWo6ESFrL5r8zhu0MFONYvA0JCOyv7NTJpdPdF1Ypr7KML2542rfBhUO_XrQZ4kLlBa8SN2L0c9FzdLfWGa83iYLVqn5BecvwlO5xvqodFfr9i1IvSKLNmz0hK1FzvYFTvNTOcxa0ljdVfSl9aQYpX2rS2xguY9v1f_qjm2b32LshaB2erV3cxa_7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XET6e_6fH-F-Y1Ofys0q-6RGVGZlAyw2Fgt0OBfvkDlhl8bOxX1dmWSHdtP6TLx5hB4yQ5p_p_asPVM88G1ICea8_DesMOJPqS6Ml6bEXjoWGzPK_Rg3sTyQMONoGz54txTyH7HxG3jnxshiVhUKaTFtMp7icTW2j1F9hGDeTRAeWn-OuEFLfCOn5CFxaBVMuAGghH78wWfnBq8ATuOtGvhsTqSXlDDLEOgsPLIzbyY89W4uAI2ei5kPZmLLivEBLXKVyLW62hZfqTTszA9YtE2p5vu0TVEQhtCstG-_jNlSAeZf5eMVreHaL3SgQ-P8zUBT6w4A9FJ7Zd73St6eug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
محفل شیرخوارگان حسینی در حرم امام رضا(ع)  @Farsna ‌- Link</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/443147" target="_blank">📅 11:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443146">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‌ کشته‌شدن ۴ نظامی رژیم صهیونی توسط حزب‌الله
🔹
رسانه‌های اسرائیلی: ۴ نظامی صهیونیست از جمله یک فرماندهٔ گردان، بر اثر اصابت موشک‌های ضد زره که توسط حزب‌الله در طول شب شلیک شد، کشته شدند.  @Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/443146" target="_blank">📅 10:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443145">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66e0e7b317.mp4?token=L5LplEqpkZb1jFfof_NLBeFHcKVi2q5EIi5dFHF35gz7OMyX4LIBYDlEv1UAjd5YbDjvaARfHJpUeiAaJeXG8Ug0OvXoKPXkMm1JoB6qwVY1x3da38YJkJjwEf5yW2A8t4AmUZPU-9EmccjDqInNqmz-FvlummdeTcQGjw63VA7JxfBTK35wRWbIvvAnH4aZgab6BdnhlFM7np2tTyNz6PxkhFzPKckDOJ-pBn7q0DhuVDs2RlOvYEkuKl2D1J7DELowsnhsD3W7wDVH0UOMLw4XLQ_j5fFWBxWvca-Gv3NStHulTcNVctxVw5XShokBO4QaGbASRLpYccLCuUn1Fw9mZyru-c8aLwNIAHDjb630wqOLFFFpX8EJRYPdJWXir5aQOIs3qkEnBi5Lb6_F2S9Ne3GyzMLlqzCwmPVceBEsi7ROH3QokJCB33GaWC2bVoeUJIgveOIN5G21CsITP8oW652O70BWfLfdztJlXknfNj8pBvxmeoSse6EvKeRezWqGOT2f20O2ioJPElx1w4h0oFkUuDw4gkMtMIJIrNnDKPmqjvLOphbAAKdAlmiusuorWrAgZIlAkcbrnj3VG5YzO9TwM1ZZ87trMql1ajrKCkhf_y2KO040dhhCL7UhJ66HYubXttwPbAWsMPESY2X3XXHboZXTIttefyfcoiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66e0e7b317.mp4?token=L5LplEqpkZb1jFfof_NLBeFHcKVi2q5EIi5dFHF35gz7OMyX4LIBYDlEv1UAjd5YbDjvaARfHJpUeiAaJeXG8Ug0OvXoKPXkMm1JoB6qwVY1x3da38YJkJjwEf5yW2A8t4AmUZPU-9EmccjDqInNqmz-FvlummdeTcQGjw63VA7JxfBTK35wRWbIvvAnH4aZgab6BdnhlFM7np2tTyNz6PxkhFzPKckDOJ-pBn7q0DhuVDs2RlOvYEkuKl2D1J7DELowsnhsD3W7wDVH0UOMLw4XLQ_j5fFWBxWvca-Gv3NStHulTcNVctxVw5XShokBO4QaGbASRLpYccLCuUn1Fw9mZyru-c8aLwNIAHDjb630wqOLFFFpX8EJRYPdJWXir5aQOIs3qkEnBi5Lb6_F2S9Ne3GyzMLlqzCwmPVceBEsi7ROH3QokJCB33GaWC2bVoeUJIgveOIN5G21CsITP8oW652O70BWfLfdztJlXknfNj8pBvxmeoSse6EvKeRezWqGOT2f20O2ioJPElx1w4h0oFkUuDw4gkMtMIJIrNnDKPmqjvLOphbAAKdAlmiusuorWrAgZIlAkcbrnj3VG5YzO9TwM1ZZ87trMql1ajrKCkhf_y2KO040dhhCL7UhJ66HYubXttwPbAWsMPESY2X3XXHboZXTIttefyfcoiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از آخرین تمرین تیم ملی با حضور هنرمند شهداد روحانی
@Farsna</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/443145" target="_blank">📅 10:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443144">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7qnbEEeoS7VaCESci6tUj5Vqi0DKyc9qwHEsfT3-uwVae-lZv5ImGNh_scrTSf9vbxn3oIZEh3IGhnPTjOgSx-Q3Frq4o2KypwaXcmCFGWVas-oas657Of63guhjqFIliNO38yksxacpS4E7W-Biey_vQKRHdMzemvSHe3lHUMrPPoXVmHThKn5b4wzVZT9c_xNl7TWZXspCglWPQslDMklapjYLG8hxHraR4Jj6BareHY2ptdcn1GclEIMsYqGNBem5FpJ7qRaNvuhLtTdgvOyn9fwqu54K83T44DrKDJYhDQMkxnlb0an_bFjQSF35BRyBWDtRQLokpKUWRLH9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رسانه‌های عبری از هلاکت سرهنگ دوم «دور بن سمحون»، فرمانده گردان ۵۲، در حادثه امنیتی که روز گذشته در جنوب لبنان رخ داد، خبر دادند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/443144" target="_blank">📅 10:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443143">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سپاه: ملت عزیز و رزمندگان اسلام چون کوه استوار پشتوانهٔ دولتمردان خود هستند
🔹
بیانیهٔ سپاه پاسداران: محضر مبارک حضرت آیت‌الله سیدمجتبی خامنه‌ای( دام الله ظله) رهبر معظم انقلاب و فرمانده کل قوا؛ خدا را سپاس می‌گذاریم که یک بار دیگر ملت ما را از سرچشمه زلال ولایت سیراب و چشم‌هایمان را به پیام عزت‌مندانه و هدایت‌های نورانی‌تان روشن کرد. پیام حکیمانه‌ای که وحدت صفوف مردم را مستحکم‌تر، مردم بپاخاسته در میدان و رزمندگان جبهه‌های نبرد را به حفظ دستاوردهای پیروزمندانه‌شان امیدوارتر ساخت و سرمایه گرانسنگی برای سیاست مردان ما، در مسیر احقاق حقوق ملت شد.
🔹
اینک که دشمن متجاوز در مقابل بعثت تاریخ‌ساز ملت ایران و حماسه‌آفرینی‌های‌ درخشان رزمندگان اسلام در میدان جنگ شکست خورده است و از مواضع محو ایران از نقشه و برگرداندن آن به ماقبل تاریخ با استیصال به موضع درخواست و التماس برای تفاهم و مذاکره عقب نشسته و در مقابل عظمت ملت ما زانو زده است، انتظار همه ملت و رزمندگان این است، عرصه سیاست‌ورزی نیز امتداد آن میدان شکوهمند باشد و به احقاق حقوق ملت سربلند ایران بیانجامد.
🔹
ملت عزیز و رزمندگان اسلام چون کوه استوار پشتوانه دولتمردان خود هستند و اگر دشمن عهدشکن بخواهد چون گذشته به زیاده‌خواهی‌ها و تضییع حقوق ملت ایران روی آورد، پاسداران انقلاب اسلامی در زمین، دریا، هوا و تمام عرصه‌های جنگ ترکیبی قدرتمند‌تر از گذشته و با بهره‌گیری از تجارب چندین نبرد آماده‌اند تا با کوچکترین اشارهٔ آن فرماندهٔ شجاع و حکیم شکست تاریخی بسیار بزرگتری را به آنان تحمیل کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/443143" target="_blank">📅 10:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443142">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IP_fCHWp17aHkfzXKqJZF4X_BdFhhYiDuP39tJ2g4IRbACjj7sZcA_uyhqtfUzBGNnlQbXHDSeelgj_-Id3zRb3LNM0mxx3JEqm5b7UXCGuMj7YV9CiSCd7MVEHw55MPamtnFXlyBZwe0H4enerwcfSHHpKxUhBe6rkRJQ3f1vfpf4z22nu38KnzxqRmidDUjHnFJbMUhEHgfblKUS1-yS5Hr9-iFnSmV05dJngwlnHRhg1SKqj6K7xPLn4oafe8zEmT4tUXIdbO2ZwOoqnc2pRYrj9N6RjGNinde6c_I86EpzoTD7PBmZNAU6YlT5fsQ2lBifOX-LTjC_QkmJnibg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به بزرگی ۴ ریشتر در عمق ۸ کیلومتری زمین، صبح امروز اشتریان لرستان را لرزاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/443142" target="_blank">📅 10:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443141">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NY-YYo1HKwdQUrgnIKK7JtnmOZDt8hIqIXSk-fwjxIgoGIXU7j2wpaAnK6lNJm7Racv22HhZfn-pvy-VQjDGFNNtXZOrV9IzksLrnTTCe_Y_5i5oGJIB3D79Y1CS0G8b8UxvRdnB2hL4E6O9NdPa4GE_uHQHTcSb5Trr8B-rpFBNUYfj-OOPEwsFTHzHs60nYwmRTtSKljeRd6B6CQs22kdWgW8VvLJhbRXx9YqM1XCsDTDfzYWqPLUN16p9RRhus-XkjcLhcN_57lbRsRZlZ7NksYfPpfEUIlto6y86ol8KgOIBt9onuyWVMLCle5biHvchAER7kwsFXQeAyPlKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش فدراسیون فوتبال به تصاویر منتشرشده از محمد محبی
🔹
فدراسیون فوتبال: درپی انتشار تصاویری منتسب به محمد محبی در برخی شبکه‌های اجتماعی، به اطلاع می‌رساند تصاویر مذکور کاملاً جعلی بوده و با استفاده از ابزارهای هوش مصنوعی و تکنیک‌های دستکاری دیجیتال تولید شده‌اند.
🔹
همچنین تأکید می‌شود هیچ رسانهٔ رسمی و معتبری این تصاویر را منتشر یا تأیید نکرده و انتشار آن صرفاً در برخی صفحات و حساب‌های کاربری شبکه‌های اجتماعی صورت گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/443141" target="_blank">📅 10:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443140">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2227f35d62.mp4?token=DFkReGXrzb7hhWKG9n-L1Pw91MiPOnnjw6U-kCbtBT4n52d96sYgJ2UXRXJpUSTxLg9FUsQ4Kyi5nBSEhZMm6hOUTD7jRax1aun2XPs70-LciIqPpWFncW7GrFzwBCQ44pbkB15JnQ3tAI1D5tlKP3W7WpnotyaCy8hI04eoeHwfR5wJnuJp0NSE24T-SgLDaT_MUDxfP8o82rWgE_ubBi-kKDKd8H470UTla8-y_EF2sfRRnQxkHXFYrdd0nPlLR9cJRF0B_oEcQF42XYWSuX4diVqU4fwdxEnAepLaPRM4B1RLguciuSarG7RWgPcIKx3xNwpNY9GH9-Ce1pKzjbR_enjgJLBd_iCO_BGc-u0P5rcBrQg21E7ifB19lZ4om7mVaIRbSJHTqSHH8aNXShPma-4rg8Wt2k_-0HAAuP780PPewFl8FH23LvuwQQ6C9_MRJgsx0s8PPq4kcKKBYFhmML0XcewjfmFXaybFRUJkr5NXSOMGLztMJ0H37kSFWSQYdriUEcWckxVNLkqI1gRaFHeSyH6rX2dGaxihSCJ3keBctEK12QY3FuHo54e3AdP0uBDMLZEJ6FLi77hC4Eq_D9Kdl6ZqLSQMQnqQMDD4tuaUjQmMtUjrzLwK83hJyDnDN-Nxo2pz6vPI7PAZj2MXmttcaVGH4yiCKdA_97Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2227f35d62.mp4?token=DFkReGXrzb7hhWKG9n-L1Pw91MiPOnnjw6U-kCbtBT4n52d96sYgJ2UXRXJpUSTxLg9FUsQ4Kyi5nBSEhZMm6hOUTD7jRax1aun2XPs70-LciIqPpWFncW7GrFzwBCQ44pbkB15JnQ3tAI1D5tlKP3W7WpnotyaCy8hI04eoeHwfR5wJnuJp0NSE24T-SgLDaT_MUDxfP8o82rWgE_ubBi-kKDKd8H470UTla8-y_EF2sfRRnQxkHXFYrdd0nPlLR9cJRF0B_oEcQF42XYWSuX4diVqU4fwdxEnAepLaPRM4B1RLguciuSarG7RWgPcIKx3xNwpNY9GH9-Ce1pKzjbR_enjgJLBd_iCO_BGc-u0P5rcBrQg21E7ifB19lZ4om7mVaIRbSJHTqSHH8aNXShPma-4rg8Wt2k_-0HAAuP780PPewFl8FH23LvuwQQ6C9_MRJgsx0s8PPq4kcKKBYFhmML0XcewjfmFXaybFRUJkr5NXSOMGLztMJ0H37kSFWSQYdriUEcWckxVNLkqI1gRaFHeSyH6rX2dGaxihSCJ3keBctEK12QY3FuHo54e3AdP0uBDMLZEJ6FLi77hC4Eq_D9Kdl6ZqLSQMQnqQMDD4tuaUjQmMtUjrzLwK83hJyDnDN-Nxo2pz6vPI7PAZj2MXmttcaVGH4yiCKdA_97Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محفل شیرخوارگان حسینی در حرم امام رضا(ع)
@Farsna
‌-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/443140" target="_blank">📅 09:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443139">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حزب‌الله: یک سرباز و ۳ تانک مرکاوای رژیم صهیونیستی را در علی‌الطاهر هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/443139" target="_blank">📅 09:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443138">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌ المیادین: سفر هیئت مذاکره‌کنندۀ ایران به ژنو معلق شد
🔹
شبکه خبری المیادین: هیئت مذاکره‌کننده ایران، به‌دلیل ادامه حملات اسرائیل به جنوب لبنان، سفر خود به سوئیس را به حالت تعلیق درآورد.
🔹
هیئت ایرانی پیش از اینکه سفر خود را به حالت تعلیق درآورد، در حال آماده…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/443138" target="_blank">📅 09:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443137">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/333ee8bab0.mp4?token=khi8qyk0ChTWWJ2oOgfkAGyyne3aqL6vgdizUlj71VZ-0CeCoYj84iomPYn9UEnr40tLKG0ceSQzPUkOq4VFNXcR5f7LUvFUGHPMp60BRZb1PQ_LZ3tMR-6Q8WT03izaGi9QVRkhlslEbznUIWZ6AJ3wC0SfXc73UPnfg1QzciHL0uujFDi7trkLHcfQIz6OU_lPbb7F-rdhyynW82s4S5Gh7oVvQKMk2EhvevJY1wfazUZyaGpcTSNd9J-UgYGHbJG53fB6TXJCz5I1tQtCJlv9WzFKcROmfjbbXSl1iRbhJkFJ9vmyYQaV53S92Mz5lgxWj1mZ0LmxWFqfltgeMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/333ee8bab0.mp4?token=khi8qyk0ChTWWJ2oOgfkAGyyne3aqL6vgdizUlj71VZ-0CeCoYj84iomPYn9UEnr40tLKG0ceSQzPUkOq4VFNXcR5f7LUvFUGHPMp60BRZb1PQ_LZ3tMR-6Q8WT03izaGi9QVRkhlslEbznUIWZ6AJ3wC0SfXc73UPnfg1QzciHL0uujFDi7trkLHcfQIz6OU_lPbb7F-rdhyynW82s4S5Gh7oVvQKMk2EhvevJY1wfazUZyaGpcTSNd9J-UgYGHbJG53fB6TXJCz5I1tQtCJlv9WzFKcROmfjbbXSl1iRbhJkFJ9vmyYQaV53S92Mz5lgxWj1mZ0LmxWFqfltgeMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رامین رضائیان: خوشحالی من وقتی است که مردم ایران خوشحال شوند
🔹
همه تلاش خود را می‌کنیم که در جام‌جهانی اتفاقی را رقم بزنیم که دل مردم ایران شاد شود
.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/443137" target="_blank">📅 09:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443136">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06a69920e2.mp4?token=d5vDJAS5CXNBeD5tP9olhFECn-ruCwxSIb57tabxh2IIKmK5PRCrVCF5nk68xThr4iQKe17DzioYLEM1AvZqT9HT2N0wDk10UctCHp2p_3u3yz0vjpW0aQC6Prb9RR6U9eHBBZO3Zrq1wpdC_ybD5yEV3QZEy8wIX8vTzWfyLtSD4kQWC73bU5doq9zDLIlj0ezhwULJrlh1vohTRjMAeT7QkhsEr9crR2-gKPMzM9grX6PkPtpRZkWf5bFdQYXgflBwyDtHuYKzxgpOHV0qo_-_2KgupGBo1x3wT2hkVhy-NDPyPTMlUalosOutrLUPX2BO8SzEVnHL1w0kRJ2O8RosF1jKLBZOR9K72r5q9kYfNEbBQiKnDJobzQxwsRHUiPYmOnmWiVFaRJvROwDUxSFhQVxaQJA8yw9kY8VixY2JeX47BIJ79v8s7nV72S4N0DrMSB_YP0Hj2xA3o2Xv8Ukh815-EXgIahRCkSeonCdsxad4820I3prb8EuSM5CEwDcVJI8r7jFuEwkEG_Hv5R89ea65khmA-pKVbZdUjHEX9M4NpJylm16i6LGQC9fhFiKP6vMb9g6ErE4bg1LsDyp9RJt-AgnAOOh6iJT0llDp6HFu3Zkv6DSXFHPAzCJtSziSg6Trjz4J4bnc01TZPa7kQn4sUxzxB5qQvyLElxE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06a69920e2.mp4?token=d5vDJAS5CXNBeD5tP9olhFECn-ruCwxSIb57tabxh2IIKmK5PRCrVCF5nk68xThr4iQKe17DzioYLEM1AvZqT9HT2N0wDk10UctCHp2p_3u3yz0vjpW0aQC6Prb9RR6U9eHBBZO3Zrq1wpdC_ybD5yEV3QZEy8wIX8vTzWfyLtSD4kQWC73bU5doq9zDLIlj0ezhwULJrlh1vohTRjMAeT7QkhsEr9crR2-gKPMzM9grX6PkPtpRZkWf5bFdQYXgflBwyDtHuYKzxgpOHV0qo_-_2KgupGBo1x3wT2hkVhy-NDPyPTMlUalosOutrLUPX2BO8SzEVnHL1w0kRJ2O8RosF1jKLBZOR9K72r5q9kYfNEbBQiKnDJobzQxwsRHUiPYmOnmWiVFaRJvROwDUxSFhQVxaQJA8yw9kY8VixY2JeX47BIJ79v8s7nV72S4N0DrMSB_YP0Hj2xA3o2Xv8Ukh815-EXgIahRCkSeonCdsxad4820I3prb8EuSM5CEwDcVJI8r7jFuEwkEG_Hv5R89ea65khmA-pKVbZdUjHEX9M4NpJylm16i6LGQC9fhFiKP6vMb9g6ErE4bg1LsDyp9RJt-AgnAOOh6iJT0llDp6HFu3Zkv6DSXFHPAzCJtSziSg6Trjz4J4bnc01TZPa7kQn4sUxzxB5qQvyLElxE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مراسم شیرخوارگان حسینی در حرم حضرت معصومه(س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/443136" target="_blank">📅 08:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443135">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">شهادت یک مأمور انتظامی در حملهٔ مسلحانه
🔹
فرماندهی انتظامی سیستان‌وبلوچستان: ساعاتی قبل، ستوان‌سوم «عبدالسلام کرد» از کارکنان انتظامی خاش، درپی تیراندازی افراد مسلح ناشناس به درجهٔ رفیع شهادت نائل آمده است.
🔹
درحال‌حاضر عملیات‌هایی با هدف شناسایی و دستگیری عاملان این جنایت تروریستی در منطقه فعال شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/443135" target="_blank">📅 08:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443134">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حزب‌الله: یک سرباز و ۳ تانک مرکاوای رژیم صهیونیستی را در علی‌الطاهر هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/443134" target="_blank">📅 08:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443127">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A9m2Vp2mWX76DVbZKQ_5Ildv5i3eE_0CZmeIt3JylOuXrJIZcMpReCvvZLYXF4Exp6MYoENuo1ovH-pzsgUtoPd0U61ZjwRKjyWBe2UBrPynAp1bT52iYCTwqwYleHC8N-FlMIfeG88ysHI81JyeGsd1WmO1es4wj9bnTCHGUOXafvi_x-QRkzoJe70oQobQ6yAjZBs_Jzi2zYgdbvlUXKILfa3AvCkyolltru7Tj5S-qrXXZt8gVeuga1izqUwYM0yliw8hb081mytOkkJigWby-3QkdSipX3An7qew819KLvkA09ZXAoFU3GkSGPwTKwRpH7bhWZKVXnEejqf3Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WXzZT8P4k-hme6gQC-Z-iTod4EmeBYos6i1xuNDG_Fe7wrcLgKSfP92WXgNTW6dp6dlkuNPJTPXrdHl9GyFcBrpCHTT64oPQGUxn1kRBJpe4f0VXDaycu8Qa8PVBIHkSOn9RqGt_tMtYrsm7F58fNEietjIXqdc2FylmCP47SLU2dZfo2EN53ra7e0h2lzAv4R0cncMiPQUoT3UN7hOXSFBMH1JI-7H6cMgnxr0w3BYcFwD5jgWrjGLcIJblHtm3vmyuyWmPteggFNOE1UPoPy7UI2okGaGGKtBdCCGtH74_fD0B9qqZHYs-V8gjKnP9CZGdcn0oTJcLV1XyzAHWKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M_H3Lo-3-bQN1dkhaJcKhjDOr85Sb6b6E8exifWdZraxpsjc5LbBJ1ly45BvBr_Df1PyaVTPPxPJMVIsRi3TEAF84PdnR7wPzx0EL-TTOEa1I1zIca-_zQVmcwNq7ua9KL0P3TJcVJvxYMoWGNEyNi1ZWnmPl7oWUe04d_OIZjGoZHHzuJCBszeONZguVCoHSS9ViOoUGDF34LWtWYERjCtvL7Jt-d2DGEFrCOkMyXQTs-0bHPNnn0gi7NjYMPs4nafd7nqRUeEO3LUalT8Tic9AOeL1wMh6URYX9vJ9EI5ygxW0KmU_TgwMN3OLYcML0-5doJqhRMx6uQ1uhOlQbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B37k9EykvyCExrf6r07XizkqOpIwMKxCP8HPpjAjgzVsBvyVsfWilCIednt6-ntTQAE6ogfAoI74hb4GQiXL9u5pMRCbWEzuIRnSDnn8KmkvJV7RStUkQN7uc1Vxw7DslSMq8JzNNiF7AKd7uIPFwXv8s9MGLtAWqOJPRox3c7K3IAw6I0ApYxZS7X9TqRiy-2dOBYNFlLgmAin51dIDobm6viMiRdSckTah3EKUtaTBWl1TCFqL6h7n3tKCu1FFCol8liKROEnVMsVxWZfrmn2VkOYup3xtAcHKeZDubYniCWfiJugZiQhclW_sZZC043XAC_frpjQZkSuF7x1nCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/boyIhGkAW_pKMLa2qs_wJDgUG84cu0vAVevSSwhONJWpKjj6avMTLSko59HpA6Bwirj3Am8FINXC80G7TyenvYfXQcqTiifMe8vWN49bteVovFPY0aATqvviEsYIpnl2N3W_l4qiV9u8dn2HvGOU16KrLZyvVjsFm6fJ2EQe_d-4Gn41FPZV0iaoHeHMuhpJxFX1meLh4N9CcDL1wlVhTTx22lxvuAba_ip79ynnVGO5dqiQ4g-qYz_lEDkCa4O4h6iUs4-gYQNvnsMo1eHAnuDLW_j65vkp3wUF5AFFqg-ngwgG6JOJb5ikOxlJK9inBzhx5PD3v1nZcFuhY9uO-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/REo_9Innsfyvp7q_JmuBBZntZcV7_DSUWzB-zMteOjOpzZDhWXoQm60yYgpbKfWdOtaHOwFt4G0yvZ7SuyZAmwJjSeJIO2fsXmV1abDJNT2DT1P6OHvP_icjn5qhXJ56JqtCQ3Jsif8O9UQC2wQ31AhaQa2Xc54i8kM6z8kRUTVCygUo2mvnqDZVj1vtXQjeQRqQahM1-ytWOOqWgtzgVT7mFCqNZXq3CinI89PClieIWDQl3FUSeFcOPhR0USxbd50owzswgiOaXRsnB0AIxj1N_fy7SIqG31uHEzTmUiZ9h6XapyT5hyza5G60IOEHLt4cvGZYJfkKLpopGxqE3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h1di2BUM0X6cdPlcSrjDVQWb8UFDZ45G23CfMN4YgXK_4FoZqVKnp4U4XXgDetvdJvxWnwvditJxnLC7O024A3kOR81tGFs2v4oeo71W9qLt3ufEFJ2iYofy1vpgZUGNIMbD-2j8w5kWckG-tsDWrkx7BosTQC5fmrp8XtijHU4vdC-oHXVn7o6ZrmD4jFjzzALAtpG-OM2EIYpYWdIaXsZTKPOfAvclRlAh0-VSyXJCUACXCdzP_ojk68lrvMRAw_0vuoRbP6ALX8QiQ7o7cvDrL3-BbNS7-slw4_0fsDEEAd-MSCH0L8geuj_sBeQs3XHtBq7cIAtr9irT7_arog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین سنتی علامت‌کشی و زنجیرزنی در تهران
عکس:
محمد‌حسن اصلانی
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/443127" target="_blank">📅 08:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443126">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1025052ee.mp4?token=Bh9gDwGMAI_-WENLeRrgi0TVDaix9I8ie0VeEM-GMHNgWupiXbkaN42MlZkM80QEEDftG5U8aWJwo6L8KPwiKsOrZF6jghmRMvEeUi2uaYWWZ1j7u8YCq-xhn3hzZUG3B9t44h8_UDnqpzmz2yabgbpoieNhKkhc3-E_dkigYZYKcIXB8-aD_b8EsB19Y8R4gpXtHSvbQ_9TlYLBOCePBx-SFTLe27imFUwN3uuT97EHXP0h3eFsvPFRVyvNLyozWhzhEINzyezYSMGW1xMOKBzkf2t9C9q0-YphXmUbZvXtO3F3DMjw9BLIBbXVxaLjbFnXpJ5E_4sMBzCNvjFofw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1025052ee.mp4?token=Bh9gDwGMAI_-WENLeRrgi0TVDaix9I8ie0VeEM-GMHNgWupiXbkaN42MlZkM80QEEDftG5U8aWJwo6L8KPwiKsOrZF6jghmRMvEeUi2uaYWWZ1j7u8YCq-xhn3hzZUG3B9t44h8_UDnqpzmz2yabgbpoieNhKkhc3-E_dkigYZYKcIXB8-aD_b8EsB19Y8R4gpXtHSvbQ_9TlYLBOCePBx-SFTLe27imFUwN3uuT97EHXP0h3eFsvPFRVyvNLyozWhzhEINzyezYSMGW1xMOKBzkf2t9C9q0-YphXmUbZvXtO3F3DMjw9BLIBbXVxaLjbFnXpJ5E_4sMBzCNvjFofw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم
🔹
اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/443126" target="_blank">📅 08:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443125">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULghylFcxxeHDZQC4stp42-IrVydfROj0RL28XMA6ANvR7lr6s2Aqj8NooJzEp2wIGktEmIBvwW3HGPGDzYHwy3nYdzqVYdTNNi84ed_BlHbkGFdMP6GlkG7e5jWuYyOUopJFKQQRHNXSMoWCuM3qbohD_xkxwn9Wfj0zYSOeOoxXEBmG3jHXNAZ-NaOUwzniMQ9naI2IsHIMuvsVVTBCduula2bqQ02RSIxHghk7cl4LYAGOl2RvSgso4y1mElJNaCik2LAQWIEUH15xegA0CnQb_mt87FUVwjvyifQQIj9CRZ-LTUpb7QZJf2ntubA-7qEj861GRg0-TeUSnpT8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات شوراها تا قبل از شهریور برگزار می‌شود
🔹
احمد فاطمی، عضو کمیسیون اجتماعی مجلس‌: با اطلاع می‌گویم که انتخابات شوراها به تعویق نخواهد افتاد.
🔹
شایعاتی که این انتخابات همزمان با انتخابات مجلس یا ریاست‌جمهوری برگزار می‌گردد، تکذیب می‌شود و انتخابات همین امسال و تا قبل از شهریور برگزار خواهد شد و این مسئله قطعی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/443125" target="_blank">📅 07:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443124">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5Qm8TzafsaT_K_kSILhez6hsusYh7ttGArq5EvwVt5QTZPmrj_xHbkJV0x0mnGiqj_6AoDVcR8vh8dnrnB0Y5mpg13WAvzzqDwaAZUcICBAbvipFad079LKfMehIVJDfnc8u_GdLMqXLeXzGrFzs1bM19RyAbW_eFXiP6oBZXHqGLmbhviCwWqOQSz9N4V7RbkbFvwbxqQHQ8uQDzknYb3xvCDDJ9VuG0fbNxpksiJ2IJ3MlziDPWUSPU5AQPRrC89OJRtcgd4rTpl9i7xqSvEKvxd_BJ5Op8SPvgDNA3u65P4Vyeia54eCq5pd9vTQYcKwS3S0dy6nlZ7vkyk5xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرط پرسپولیس برای تمدید قرارداد با اوسمار
🔹
پیگیری‌ها نشان می‌دهد مهم‌ترین مانع بر سر راه امضای قرارداد جدید سرمربی برزیلی، مبلغ قرارداد اوست. مدیران باشگاه از اوسمار خواسته‌اند باتوجه به شرایط مالی باشگاه، در رقم پیشنهادی خود تخفیف قائل شود تا قرارداد فصل آینده نهایی شود.
🔹
اوسمار به مسئولان پرسپولیس اعلام کرده که حاضر است در مبلغ قرارداد خود تخفیف بدهد اما هنوز میزان این کاهش را مشخص نکرده و اعلام رقم نهایی را به روزهای آینده موکول کرده است.
🔹
به همین دلیل مدیران باشگاه در انتظار پاسخ نهایی این مربی هستند تا مشخص شود امکان ادامۀ همکاری وجود دارد یا خیر.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/443124" target="_blank">📅 07:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443122">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcZ2lQOGbsPlOhPv4optd4FSidl_c1r_CGjXphV6GvVj7Txrh1Ovvztip3TtyyA4FXpyTUdyY7Ss4lmdUjtH8fr2pR0CuTBVs3eviG0QAcsrV1fvPPiDOhAuZ8f7uRu-6jDNHRKb8lQkd4gcMTZ_2bu-7--11nu1Z47j4zypmT9GilewWHpae0YkBB7KzZBS3iKUpkEun3_3-IDgjMuL06yPiiJNWyeUDkYM0NVZPJfRIAj2OeOgkEzxYb2Ccspd8ZU0TlCOgMWcVUQPKqCWRqb_pzJbiQnaMMhUN1Cp2A0Bs8O3RXUfnVcBfpBOTYzVJks4X38eo69O08IZ7i020A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخستین لشکرها از کوفه می‌رسند؛ حلقه محاصره آغاز می‌شود
🔹
یک روز از استقرار کاروان امام حسین(ع) در کربلا گذشته بود. خیمه‌ها برپا شده بودند و دو اردوگاه در فاصله‌ای نه‌چندان دور از یکدیگر قرار داشتند؛ در یک سو خاندان و یاران امام و در سوی دیگر نیروهای حر بن…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/443122" target="_blank">📅 07:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443121">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پیام‌های جعلی ۳۵۰ قربانی گرفت؛ روی هر لینکی کلیک نکنید
🔹
معاون پلیس فتای فراجا: باند حرفه‌ای کلاهبرداری سایبری که ۳۵۰ فقره برداشت غیرمجاز از حساب شهروندان کرده بودند شناسایی و دستگیر شدند.
🔹
مجرمان با انتشار پیامک‌های جعلی حاوی بدافزار مانند «ابلاغیۀ قضایی» و «یارانۀ معیشتی» اقدام به ترغیب کاربران به باز کردن لینک‌های آلوده کرده و سپس حساب بانکی آن‌ها را خالی می‌نمودند.
🔹
علاوه‌برآن، با در اختیار گرفتن کنترل حساب‌های کاربری فرد در پیام‌رسان‌ها و شبکه‌های اجتماعی، اقدام به جعل هویت و ارسال پیام‌های درخواست وجه به مخاطبان فرد قربانی می‌کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/443121" target="_blank">📅 06:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443120">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
کمین و عملیات مرگبار حزب‌الله علیه صهیونیست‌ها
🔹
حزب‌الله: پس از کمین مرگبار مجاهدان مقاومت اسلامی علیه صهیونیست‌ها هنگام تلاش برای نفوذ به شمال ارتفاع علی‌الطاهر، نیروهای پشتیبان اسرائیلی تلاش کردند تا برای انتقال کشته‌ها و زخمی‌ها به سمت منطقه پیشروی کنند، که بازهم مجاهدان مقاومت اسلامی آن‌ها را با شلیک راکت و خمپاره هدف قرار دادند و اصابت‌های قطعی به دست آوردند.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/443120" target="_blank">📅 05:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443119">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvaRxzc718oPDwvs2mqwKzYF_g5MuWvkvfYocXSwXKSy1yzi22vaXJnP0iSvmIImdMOdKW6fSGqXuh0In8KysLCgft8DXXijw8eR_LUtxb80DNj3ZHkeGK5U8lnONXCQqIUgQRKWTD5qb_GRYqvMI-Ba3js1ZETLehgf6soPoTKOUXOSW6kGvkAqO0o4c0nRK_xEeuj_zYfx3tU5fu4XzStT01BPQ5zYvp2AGxFu2T3q-sAc1dIhbyhpslcqzBFsvV0ha8lXOKCtM2AlhqF60Zrd5sUhUf0PvVYHp9IuPCTlS1P3tlQ6FspdWGfd0PdWODclI3WNzbxvgfgYESWw8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بیانیۀ دبیرخانۀ شورای عالی امنیت ملی: با نظارت دقیق بر اجرای تفاهم، در صورت تخطی طرف آمریکایی اقدام متقابل تعیین‌شده صورت می‌گیرد
بسم الله الرحمن الرحیم
🔹
دبیرخانۀ شورایعالی امنیت ملی به رهبر معظم انقلاب و ملت بزرگوار و قهرمان ایران اطمینان می‌دهد در اجرای تدابیر و دستورات معظم له، به‌ویژه در نگهبانی از حقوق ملّت ایران و جبهۀ مقاومت، پاسداشت خون شهیدانمان و پیشبرد مذاکرات آینده بر مبنای منافع و مصالح جمهوری اسلامی ایران به هیچ وجه مسامحه نخواهد کرد و تا استیفای کامل حقوق ملت ایران و خونخواهی خون پاک و مطهر رهبر شهیدمان، از پای نخواهد نشست.
🔹
در این راستا، با بی اعتمادی کامل به دشمن بدعهد و پیمان‌شکن و با نظارت دقیق بر فرآیند مذاکرات و اجرای برنامه‌ها، چنانچه تخطی‌ و تخلفی از جانب طرف آمریکایی صورت گیرد، طبق برنامۀ از پیش تعیین شده، اقدام متقابل صورت خواهد گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/443119" target="_blank">📅 05:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443118">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ: بمباران ایران فایده‌ای نداشت؛ تنگۀ هرمز را باز نمی‌کرد
🔹
رئیس‌جمهور آمریکا در مصاحبه با آکسیوس خطاب به کسانی که می‌گوید او مقابل ایران مماشات کرده گفت: تنها راهی که می‌توانستم سخت‌گیرتر باشم این بود که دو یا سه هفته دیگر به آنجا بروم و همچنان آن‌ها را بمباران کنم، درست است؟ اما این چه چیزی عاید ما می‌کند؟ تنگه هرمز باز نخواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/443118" target="_blank">📅 05:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443115">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlOKbFQgX_vlNIiXekgMWvHbaDxtEFecUVVkc5mXjr-ffq0DaHfv3Mjjr9iskl_CJ4RsCZvdAzf5Q6t0vpa8bPBQ9uXsFMqQd-sjX2-PI8tCLg7z2Dpl07S9y2LzRMg0drG2J1p6EksR164xlxVwTubkA9v8AFR-TyIhLr7i3we32P69SMdzZr86ci2XLJ1q9RFcRXvoFGEgHb7lwwlrnv6uDzQKoIYaISMO3Rod3bd46zevyEDnu_KLlI993oceXB8BzqUo9AhgssIeVSBn1gzdNIGwfUGXiovnHUacuWapGF02MqmQaY3xfwbj0pW8HaIIpJkvNb9yBghXq9U71A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بامداد جمعه در جنوب لبنان چه گذشت؟
🔹
بامداد امروز، جمعه ۲۹ خرداد ۱۴۰۵ (۱۹ ژوئن ۲۰۲۶)، مناطق جنوبی لبنان شاهد یکی از شدیدترین درگیری‌های نظامی میان نیروهای حزب‌الله و ارتش رژیم صهیونیستی بود.
🔹
این نبرد محور «کفرتبنیت» و ارتفاعات «علی‌الطاهر» متمرکز شد و به اذعان رسانه‌های اسرائیلی، یکی از سخت‌ترین ضربات را به ارتش این رژیم وارد کرد.
🔹
شرح اتفاقات را
در اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/443115" target="_blank">📅 05:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443114">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
حزب‌الله: سه تانک مرکاوا را با موشک‌های هدایت شونده هدف قرار دادیم که منجر به نابودی آن‌ها شد.
@Farsna
‌</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/443114" target="_blank">📅 04:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443113">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zc_dyjPjerlEl8KfNLE_6cgwnoa9ENwF2HIyHHyl1e-XrGaTD-OlQj4jyH4Yu8jMdfbYeuINu5EVI9dX6TStdjkuI6B3chv_PbW88ElEmEAhl8PCrn7Y77hg2mkgRKN3ubSOFlOEAV5bubVsbgaeAA7XrIh5SQa924wszPrcZMKM-kV-ak2pSRQlgeGmSwTXVa3jDnc9knMqMGeYDhzi7H_ny1W1-q9sYL3RH_ZpGxbkzTqbURwvsbqAPXT6PanaGHyKxcQ7fgfzqK6_oXMP5WcmKMXkHBOrf4D0SJeca51jRJTPc7dDXd2QUdn6M1gp_ioYFx7xihbaFtEnURD6jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نجات ۴۵ ثانیه‌ای هزاران نفر در اعماق زمین
🔹
یک ابزار هوش مصنوعی که در شهر پرتوریا توسعه یافته، می‌تواند تنها در حدود ۴۵ ثانیه یک عکس رادیولوژی قفسه سینه را بررسی کرده و نشانه‌های بیماری‌های ریوی را تشخیص دهد.
🔹
این فناوری هم‌اکنون در یکی از عمیق‌ترین معادن طلای جهان در آفریقای جنوبی نیز مورد استفاده قرار می‌گیرد و به پزشکان کمک می‌کند بیماری‌ها را سریع‌تر شناسایی کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/443113" target="_blank">📅 04:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443112">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAbR7fDBBu_PcjDXF9GrRK3pP6QwCKgsqM919GFJtC2PDMC4NYUDWmVKCpFm_ZWvLRMri6MxXzgxIUlgsNso2Re57qhP2T-CFPCytWwHDx2jIXcwHwxIaS1t4foJjvDX80BV1vVk9JChJkxJFWh4lXWP_PTgK3NoFirFWz443UHfz3YQV-1cFhYgHbLKUNAy4QHvQQtlgjQqtCQTKAUiIGRuDArwtrODTr0JuabovRaxQAvAHKVGWYctEqjdnZol051vCQj09NowSAwsQrEGs33uH4Eai_G2CTPUjlfNMy1VF1Zy5-h70xenfh-UMBPRE_2m5igH6cDTxf-W-3VREQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاملۀ پنهان مالک اینستاگرام با کنگرۀ آمریکا
🔹
شرکت متا به‌صورت مخفیانه از اعضای کنگرۀ آمریکا خواسته بندی به لایحۀ قانون امنیت کودکان در فضای آنلاین الحاق شود که بر اساس آن، شرکت‌های آنلاین در برابر هرگونه دادخواهی یا مسئولیت قانونی در رابطه با امنیت و حریم خصوصی افراد زیر ۱۸ سال مصون بمانند.
🔸
این پیشنهاد درحالی مطرح می‌شود که متا و یوتیوب (متعلق به گوگل) امسال در نخستین پروندۀ مشابه، به پرداخت ۶ میلیون دلار غرامت محکوم شدند و با انبوهی از شکایت‌های دیگر از سوی خانواده‌ها روبرو هستند.
🔗
جزئیات پیشنهاد متا را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/443112" target="_blank">📅 04:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443111">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_-h2K1Uvm7uvJaJ0qx1uAvFNvIol2VngkOEIl5lw4EoqeiSEniJWhuylYuOThXX4FRyUB4MGIMkohHFXO4Nho1H62LExb5xaWpoAS5xihXYMJ2SdXSBlcQDTXHJrZY5uP9su7VI6kQCk8TGzHfToWm9mRtpXxhHpnW-w6AxA3sKGdLy3Xb_OCO__vbqpSBIIFct8sa55lxBbDQFTJ2mGpO__55df74ZjBtVt5g4zOpCvxN_ZQn0VRYrRmONBZK2pUWNtmBXUByFhMDZwerpymvKM93HcoGtRsF3sMvDWGTNN8fmevoq0Z5ddMpim2j0nyGlxuqNkAAgyih77TpvfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
برخورد شدید بازیکن ازبکستانی به فیلمبردار مسابقات، در بازی با کلمبیا @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/443111" target="_blank">📅 03:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443110">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb01ec959d.mp4?token=b_CihGPIfN2TCZbZzwXO0Gu2Y_FrXT3oQRrvkJESFXd9S5HGYRGEm134XkrfqfYIxjeaxYBlAzwd_LsQIWBXQuuJ1q-VxyKvDnKPApjIzLlrhAntNtjTwI8wI-SRDDs6S5D8pQBgd8lb-q8d_Ovcp0asHb31k0jQvfSTXeNX3a_mbBIItD0OPb7Ims3MCPHQ3mgiA8viGC-iFRp0i2Jc_AKFC353ZKyWnCSo3abMUg-IsPozVba3xARSgzbE8q2Fbq1pPzcuacL0ZCMBwJN88zMQJG67d_PAt08UCJSfIqT7xpHh2edHd3c7YcZ7z5a-MOCeP0sAfjDKzY7nvpACXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb01ec959d.mp4?token=b_CihGPIfN2TCZbZzwXO0Gu2Y_FrXT3oQRrvkJESFXd9S5HGYRGEm134XkrfqfYIxjeaxYBlAzwd_LsQIWBXQuuJ1q-VxyKvDnKPApjIzLlrhAntNtjTwI8wI-SRDDs6S5D8pQBgd8lb-q8d_Ovcp0asHb31k0jQvfSTXeNX3a_mbBIItD0OPb7Ims3MCPHQ3mgiA8viGC-iFRp0i2Jc_AKFC353ZKyWnCSo3abMUg-IsPozVba3xARSgzbE8q2Fbq1pPzcuacL0ZCMBwJN88zMQJG67d_PAt08UCJSfIqT7xpHh2edHd3c7YcZ7z5a-MOCeP0sAfjDKzY7nvpACXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاجعه قطری‌ها ادامه دارد خودشان هم به خودشان رحم نکردند  کانادا ۵ - ۰ قطر  @Sportfars</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/443110" target="_blank">📅 03:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443109">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf88283c8e.mp4?token=mr5iwOY5nK74GljmqQ0AlPdJTxBdHivLcFxhWkAK3MY4xc8E49TVakS311jOpTmNj1goJbUO3oJ7GCa9yRUj_2T55CwSC1n8wIbfG2pktaL7qLGXXaDWEczz26bhrLFDkTKlbsOFDNs7wa_pA8YrS5auHfzU2z5PO8pWyHMapEN32SkKq4CeLwVKUNBOVuG5f-FCVpHsAsChWcSooBK-9JMIXv1SyslKAfev4xVT9QRESBRkbQ1_isNpKAlDqGPOHys_jEdyVf1zTSM9eP5g9pyN6K9oAiLeNeCaabQltGLS1f2MRyr1il8SONKVxIuUG8yuYYRI4xhHUyMeXd7aMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf88283c8e.mp4?token=mr5iwOY5nK74GljmqQ0AlPdJTxBdHivLcFxhWkAK3MY4xc8E49TVakS311jOpTmNj1goJbUO3oJ7GCa9yRUj_2T55CwSC1n8wIbfG2pktaL7qLGXXaDWEczz26bhrLFDkTKlbsOFDNs7wa_pA8YrS5auHfzU2z5PO8pWyHMapEN32SkKq4CeLwVKUNBOVuG5f-FCVpHsAsChWcSooBK-9JMIXv1SyslKAfev4xVT9QRESBRkbQ1_isNpKAlDqGPOHys_jEdyVf1zTSM9eP5g9pyN6K9oAiLeNeCaabQltGLS1f2MRyr1il8SONKVxIuUG8yuYYRI4xhHUyMeXd7aMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاجعه قطری‌ها ادامه دارد
خودشان هم به خودشان رحم نکردند
کانادا ۵ - ۰ قطر
@Sportfars</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/443109" target="_blank">📅 03:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443108">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حقوق روزانۀ نتانیاهو به صهیونیست‌ها برای اجبار فلسطینیان به ترک خانه‌هایشان
🔹
دولت نتانیاهو به ۶۵۷ تروریست شهرک‌نشین در پنج منطقۀ کرانۀ باختری حقوق روزانه پرداخت می‌کند تا به عملیات غارت اراضی و کوچ اجباری فلسطینیان ادامه دهند.
🔹
بر اساس سندی که وزارت شهرک‌سازی رژیم صهیونیستی منتشر کرده، این طرح از ماه جاری تا پایان سال جاری میلادی (دسامبر ۲۰۲۶) اجرا می‌شود.
🔹
این افراد در مزارع و شهرک‌هایی که بر روی اراضی مصادره‌شده یا غصب‌شده از فلسطینیان احداث شده، سکونت دارند و عملاً با حضور خود، این اراضی را به تصرف خود درآورده و ساکنان فلسطینی را مجبور به ترک خانه‌هایشان می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/443108" target="_blank">📅 03:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443107">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e56ab972c.mp4?token=Ij5QWA3LdFuQyCd88-UCdVSbP03VqFHxFaGjhss6M5OqSuXOV5QCH1gm6Ph1Zxf0wAVdtR9k4AP5m_T9xb1LUP7U2ejXD7YLy3kB5AXDDzK_XPqjLihT4RcyoE49GKQO1j11sn7tLBkwUHEKyJSXf9K5QEApXTbPyUspFVE46lZTy4Xbvzww2hs4ndFvETaquC6Tnd7oLCWbCsHUMzFH4eAewN1TACrbeWdKVJ_JV9nKR4-xNZ1qL-QJO9_ETY3zVDrQn0KNWEEClG7TDTrwWWiA3dMU9rKtJ5njvIsxJMjjKaoHL-D-dftOLelREXV6BCuYsnGqprUgASvzL_aIFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e56ab972c.mp4?token=Ij5QWA3LdFuQyCd88-UCdVSbP03VqFHxFaGjhss6M5OqSuXOV5QCH1gm6Ph1Zxf0wAVdtR9k4AP5m_T9xb1LUP7U2ejXD7YLy3kB5AXDDzK_XPqjLihT4RcyoE49GKQO1j11sn7tLBkwUHEKyJSXf9K5QEApXTbPyUspFVE46lZTy4Xbvzww2hs4ndFvETaquC6Tnd7oLCWbCsHUMzFH4eAewN1TACrbeWdKVJ_JV9nKR4-xNZ1qL-QJO9_ETY3zVDrQn0KNWEEClG7TDTrwWWiA3dMU9rKtJ5njvIsxJMjjKaoHL-D-dftOLelREXV6BCuYsnGqprUgASvzL_aIFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قطر ۹ نفره شد
!
🔸
خطای شدید بازیکن قطر، باعث شکستگی پای حریف کانادایی شد.
🔸
یک بازیکن دیگر از قطر، دقیقۀ ۳۳ اخراج شده بود.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/443107" target="_blank">📅 02:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443106">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNKGBK4E-KPmkg9C5IySGjSBY5Uyna0U-u7gwWxtV7YDdToZAKY11SwcNggId_Uy4MoVhmw6jESDDpfDceTDtTAJtFSrUonjLjdKc0dH1Ak5Sl1AOGxDoE69iWnZVcD0ZulLrKWjR0SxAJfhbM5KqSIdAYXi0bv_JmMQqjwLxX5sSkxqqGvmQLoYgEkHYX3XPNecmnLXE2GNk8Y4YEPk6szj86br6pK4Le18wLyKn2YxKLYDJbEqCpvvSxReb2Ym8pBYutVXC_XGkeNSTrDK1vdgG_SfJ4iXw5EXSyiBBu9a8C2A8PVDcjHE3tLyDCYCQOuWO9hLAHESdijG3EYjIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هافبک هلند ضربه‌مغزی شد
🔹
کوئنتین‌تیمبر هافبک تیم ملی هلند در تمرین روز گذشتۀ این تیم دچار ضربۀ مغزی خفیف شد.
🔹
در نتیجۀ این اتفاق، کادر پزشکی تیم ملی هلند تصمیم گرفته برای جلوگیری از هرگونه ریسک، این بازیکن را از فهرست بازی آینده خارج کند.
🔹
بر همین اساس، فدراسیون فوتبال هلند اعلام کرد که او در دیدار دوم مرحلۀ گروهی جام‌جهانی مقابل سوئد بازی نخواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/443106" target="_blank">📅 02:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443105">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">چراغ سبز آمریکا به رژیم صهیونیستی با تحریم مرتبطان حزب‌الله
🔹
وزارت خزانه‌داری آمریکا اسامی ۳ فرد و ۵ نهاد را به فهرست تحریم‌های مرتبط با حزب‌الله لبنان اضافه کرد.
🔹
خزانه‌داری آمریکا در بیانیه‌ای مدعی شده که افراد تحریم‌شده از نفوذ خودشان برای «به تاخیر انداختن روند خلع سلاح حزب‌الله» استفاده کرده‌اند.
🔸
تحریم‌های جدید آمریکا در شرایطی اعمال شده که رژیم صهیونیستی با چراغ سبز آمریکا در حال بمباران مناطق مختلف جنوب لبنان است.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/443105" target="_blank">📅 02:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443104">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAIzbcZY31q0F2cJXuzaefGlZPfdsDvshucRUmBxU5gRvCycglsVEAQUGK6L5oBvz8L3d9XEbQuVyg04A9q5Own0v61OyDl-r37FHDT7hl-fUDVQxxcj8clJEmSN6mY5vrLaF5ZTrZdavwpZnqeXdKWiQfyvg6Noiq-atfdKdGQobxWAVc4AfhzVhrYLmsXBtE7-I2c5JLnhU8dejhlpHbyVEi4oDZsntuPBFJoJA-5-E7ddx93MKpVOytTvkXG1l4kGySTsdRxqE30zU4nkGxCjM3Jdt5Gj1YIyQWfCeFti1oGGlrCBQ7fO9Lq20h26rlrmMnBrMlN1HWVELUT-2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: در صورت حمله اسرائیل به ایران، از تل‌آویو دفاع می‌کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/443104" target="_blank">📅 02:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443103">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bdbeb5c90.mp4?token=Y2kYXeXME-QW_qn3R4djRT0p2rRighttV873A3YTGZdbnjwQ8Do_nvNoWJrU0UWQ46S4peWbZKjRbSmmAOpj7gSvn74TeN7PKQhJ_D0VHxAr1UCVmZ-VNTVLSB7D4_hjFlsGDknhif7t5THXsg21B5guELa2bGK-ibDv8vJXT0q-diPkW6fYC-NVLHSunOqJ1fMXk73CDsYy5wFK9sxH9r_GMA26y25yYv2yUaqnXuB9LDphxERBm286YT3WsMAPzlD20ox5oWvBR0LirVZ9TwTJTwUC6XHpTKMK8G7TwvFpJU08_pAMuQPYY2tSZom2ECHmt3iDhEYVPT4T2hk9Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bdbeb5c90.mp4?token=Y2kYXeXME-QW_qn3R4djRT0p2rRighttV873A3YTGZdbnjwQ8Do_nvNoWJrU0UWQ46S4peWbZKjRbSmmAOpj7gSvn74TeN7PKQhJ_D0VHxAr1UCVmZ-VNTVLSB7D4_hjFlsGDknhif7t5THXsg21B5guELa2bGK-ibDv8vJXT0q-diPkW6fYC-NVLHSunOqJ1fMXk73CDsYy5wFK9sxH9r_GMA26y25yYv2yUaqnXuB9LDphxERBm286YT3WsMAPzlD20ox5oWvBR0LirVZ9TwTJTwUC6XHpTKMK8G7TwvFpJU08_pAMuQPYY2tSZom2ECHmt3iDhEYVPT4T2hk9Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اشتباه و دفع ناقص دروازه‌بان قطر، گل اول کانادا را رقم زد
⚽️
کانادا ۱ - ۰ قطر
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/443103" target="_blank">📅 01:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443102">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تداوم تنش‌ها در جنوب لبنان
🔹
گزارش‌ها حاکی است نظامیان رژیم صهیونیستی منطقۀ نبطیه در جنوب لبنان را هدف حملات توپخانه‌ای قرار دادند.
🔹
همزمان، جنگنده‌های اسرائیلی بر فراز جنوب لبنان به پرواز درآمده و درگیری‌ها در منطقۀ علی‌التاهر شدت گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/443102" target="_blank">📅 01:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443101">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f306342bf9.mp4?token=K4XT3iKcw-LkWN6zXQlL8RspJPC3PDEW58RFJaTqUgVQJa0fHuVxIMhoTsxg_YkjmML1jH1A6Qv5VCk361n0yEynLYHei0C5Un0hBFFmCFaPXUjnzJtvVnd2RQTevHvZi8lkGRIlMwRJ5RUQqTAqtHYdbc7wYet8jlLHOaEsCYCuUhFIVHweImTjQ0og0Czn2vR2oUqZPgNw2hjfgy_zVKjO6f5qw3yVC2ZetZa6Gn2Gy37ljteSFtdTiUag50M5vn62MJF9fw0rQyWrvxIKcqNZE5gkeFiEUOc4x2i-RobEgPLMitbqBLW9PvojqoD9cww-GFfCxhNn4rruADQP_b2pfTaxAQdpAK7VEEc8kH6k7bIPIr22V0qI12xFJlHM2GE7mWJrgDOMHpH7oQzygeLUPu-mqN34OWnLcAvLaNlvRXC4CGUWKBC6tk4-49Ubw5fEHH1k7dJbigB_Zc4nV_OJSGG03MCBj-c_3MQENAgPAgi1JB7nmY_xDFA9BnYtCE7HRkQeYHVjG9HObIxxkkWERxWdFVvUansnG16oTDUoPxswU3HH9sVWFZD8mJ-_Mg5bjFYrne1ZeIWtf7TjfSl7FwgCSrBobPtmqNr4R8TsYwrNGOGoaeAF_I5-HekxiXynyMcp4YJk59phyYwQFxIYEKzpgKxkYDYf3n7XR08" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f306342bf9.mp4?token=K4XT3iKcw-LkWN6zXQlL8RspJPC3PDEW58RFJaTqUgVQJa0fHuVxIMhoTsxg_YkjmML1jH1A6Qv5VCk361n0yEynLYHei0C5Un0hBFFmCFaPXUjnzJtvVnd2RQTevHvZi8lkGRIlMwRJ5RUQqTAqtHYdbc7wYet8jlLHOaEsCYCuUhFIVHweImTjQ0og0Czn2vR2oUqZPgNw2hjfgy_zVKjO6f5qw3yVC2ZetZa6Gn2Gy37ljteSFtdTiUag50M5vn62MJF9fw0rQyWrvxIKcqNZE5gkeFiEUOc4x2i-RobEgPLMitbqBLW9PvojqoD9cww-GFfCxhNn4rruADQP_b2pfTaxAQdpAK7VEEc8kH6k7bIPIr22V0qI12xFJlHM2GE7mWJrgDOMHpH7oQzygeLUPu-mqN34OWnLcAvLaNlvRXC4CGUWKBC6tk4-49Ubw5fEHH1k7dJbigB_Zc4nV_OJSGG03MCBj-c_3MQENAgPAgi1JB7nmY_xDFA9BnYtCE7HRkQeYHVjG9HObIxxkkWERxWdFVvUansnG16oTDUoPxswU3HH9sVWFZD8mJ-_Mg5bjFYrne1ZeIWtf7TjfSl7FwgCSrBobPtmqNr4R8TsYwrNGOGoaeAF_I5-HekxiXynyMcp4YJk59phyYwQFxIYEKzpgKxkYDYf3n7XR08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت شهید حاج قاسم سلیمانی از ارادت شیعیان، اهل‌سنت و مسیحیان به حضرت اباعبدالله‌الحسین علیه‌السلام
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/443101" target="_blank">📅 01:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443100">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پیام قالیباف به رهبر معظم انقلاب: اوامر حضرتعالی را نصب العین خود قرار می‌دهیم
🔹
رئیس مجلس:  از پیام راه‌گشا و حکیمانه حضرتعالی سپاسگزاریم. این پیام نقشۀ راهی بود که بیش از گذشته روشن کرد با نهایی شدن این یادداشت تفاهم، تازه به آغاز راه سخت و پرپیچ و خمی رسیده‌ایم که باید حقوق ملت ایران و مقاومت را از دشمن بدعهد استیفا کنیم. این پیام و اعلام انتظار برای تحقق شروط تعیین شده در یادداشت تفاهم، دست ما را برای پیگیری تعهدات آمریکا پر تر کرد.
🔹
ما این اوامر حضرتعالی را نصب العین خود قرار می‌دهیم و اجازه نخواهیم داد طرف مقابل با بدعهدی و زورگویی حق مردم ایران و جبهه مقاومت را مخدوش کند. براساس آموزه‌های مکتب حسینی و سیرۀ امام شهیدمان، معتقدم جبهۀ توحیدی هرگز نمی‌تواند با جبهۀ باطل صلح کند و وظیفۀ همۀ ما این است که مقابل جبهۀ باطل بایستیم و در این مسیر، دیپلماسی را یکی از میدان‌های مبارزه برای  ایستادگی می‌دانیم.
🔹
تضمین ما برای تحقق این یاداشت تفاهم، نه بندهای آن، بلکه جان ماست که کف دست گرفته‌ایم و قدرت جمهوری اسلامی ایران که دشمن آمریکایی صهیونی در جنگ اخیر ضربات و قاطعیت آن را به‌عینه درک کرد. ما همان‌گونه که در مسیر گذشتۀ مذاکرات نشان دادیم اهل ایستادگی برای تحقق شروط و خطوط قرمز تعیین شده و کسب منافع ملت ایران هستیم. مذاکره برای ما مسیر مبارزه برای گرفتن حقوق مردم ایران است و در این مسیر اگر دشمن به دنبال زیاده‌خواهی باشد ثابت کرده‌ایم که دست‌مان روی ماشه است و هیچ تردیدی در پاسخ کوبنده به دشمن که در جنگ اخیر طعم آن را چشیده، نداریم.
🔹
درپایان از اینکه نحوۀ ادامه مسیر پرخطر و پیچیده مذاکرات را روشن فرمودید سپاسگزارم و امیدوارم این پیام همه آحاد جامعه را در مقابل دشمن برای تحقق شروط گفته شده در تفاهم، متحد و یکپارچه کند.
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/443100" target="_blank">📅 01:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443099">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">محدودیت برق برای ۳ هزار مشترک پرمصرف تهرانی
🔹
شرکت برق تهران: از ابتدای خردادماه امسال و با بهره‌گیری از سامانه‌های هوشمند پایش و مدیریت مصرف، محدودیت مصرف برق برای ۳۰۶۹ مشترک خانگی و تجاری در شهر تهران که در زمرۀ مشترکان بسیار پرمصرف قرار داشتند، اعمال شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/443099" target="_blank">📅 00:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443098">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIxQp1XUfxhX28Ce1YyYFA3KzbC-4SLfWsbpvbaoujxRS9kLz-N0ijIXEJerOjNLar8JO99X4GGpdntjCw8g0AkrVLBDwj0yt5EQyDsPccabHPHh8dDhCMQz4C_c7Dch3TaHnaQDdv_rcYOBkaU0cUo3avpOcvWltm6zs9Dhw4_CHgudKwNLxZrb92LsXvx0XfDhNuOo4jF-gYftcssFnIbVgvf_VUKDKysoy1vsDPRJ8hs706_mTBbt_Kh_-_f6f2ik6yvLjx-zYvbp3QxHjGbRoK73lpE6CqYU0Q4nPBOpXfpT9-cWxSZh8kj7v1IVfR7_0ZxjhX87o7Ya-f99Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوئیس، بوسنی را گل‌باران کرد!
⚽️
سوئیس ۴ - ۱ بوسنی
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/443098" target="_blank">📅 00:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443097">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNwJh2nOX6mevg-HAOz3oAvOulVPuktw7GMUeK9zbpxwcy9x5doYxu6UQx8LqC0hp1d70gHCJlFNA2bYh_DsYTO_MWS4oouIGVH-EH8g4XCRmD1rDFLGhAaxsh7F6Haf2Mrobom4e3k3E6HLY0uFHoRzTdC4JUPZfcD85kZFFZWLRtimm-pZv5mT5barTNVlZ99JiefXwLGSzitiYpRMBTrYwdpWVOhkbTVtA0EASG_-fcVGdq5b8kMGv2EoIfT5fSVL-bojF-IurHSVFmqneyvmZYI05ewEWMQcYjUjn6g5OhhJzs1LDzoA7RqiCiO3Q8OP53Mbg3ORrLl1uC7wGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمولۀ بزرگ اتوبوس‌های دوکابین به پایتخت رسید
🔹
سخنگوی شهرداری تهران: با ورود ۵۱ دستگاه اتوبوس دوکابین ۱۸ متری به تهران، تعداد این ناوگان به ۱۰۱ دستگاه رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/443097" target="_blank">📅 00:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443096">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۴</div>
</div>
<a href="https://t.me/farsna/443096" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۳ – کتاب آه</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/443096" target="_blank">📅 00:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443095">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پزشکیان: پیام رهبر انقلاب نقشۀ راه صیانت از منافع ملی در مسیر مذاکرات است؛ خود را متعهد به اجرای دغدغه‌ها و رهنمودهای ایشان می‌دانیم
🔹
پیام روشنگرانه و صریح مقام معظم رهبری خطاب به ملت پرشور و وفادار ایران مسئولیت هم اجزای مؤثر در فرآیند مذاکرۀ پیش‌رو را تبیین کرد. توجه مهرافزای معظم‌له مبنی.بر تلاش‌های دلسوزانه و حسن‌نظر مسئولین امر و صدور اجازه برای آغاز مذاکره در جهت تحصیل منفعت برای ملت ایران اسباب خرسندی و رضایت همه خدمتگزاران ملت ایران است.
🔹
بدیهی است اینجانب به‌عنوان رئیس‌جمهور و رئیس شورای امنیت‌ملی به‌همراه سایر اعضای این شورا خود را متعهد به توجه حداکثری نسبت به دغدغه‌های معظم‌له و حراست از حقوق ملت ایران و جبهه مقاومت می‌دانیم.
🔹
بی‌تردید خط قرمز مسئولین منافع ملی و پاسداشت عزت، شرافت و اقتدار ملت رشید ایران است و با توجه حداکثری تیم مذاکره‌کننده نسبت به جزئیات مذاکره و رجای واثق به فضل و عنایت پروردگار، پیروزی بزرگ حاصل خواهد شد. انشاالله
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/443095" target="_blank">📅 00:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443094">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آغاز واریز حقوق خرداد بازنشستگان کشوری
🔹
معاون صندوق بازنشستگی کشوری: حقوق خردادماه بازنشستگان کشوری آغاز شده و تمامی واریزی‌ها تا ظهر فردا واریز خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/443094" target="_blank">📅 23:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443093">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌
🔴
منبع آگاه: پیشنهاد امضای الکترونیکی تفاهم‌نامه ایران و آمریکا پیش از سفر به ژنو مطرح شده است
🔹
یک منبع آگاه نزدیک به تیم مذاکره‌کننده در گفت‌وگو با خبرنگار فارس، از مطرح شدن پیشنهاد امضای الکترونیکی متن تفاهم‌نامه میان ایران و آمریکا پیش از سفر هیئت‌ها…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/443093" target="_blank">📅 23:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443092">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎥
شريعتمداری: تنگۀ هرمز قابل مذاکره نیست و غرامت باید گرفته شود
🔹
مدیر مسئول روزنامه کیهان: در سند تفاهم ایران و آمریکا از ظرفیت راهبردی تنگۀ هرمز به‌طور کامل استفاده نشده و برخی ابزارهای مهم فشار علیه آمریکا و متحدانش مورد توجه قرار نگرفته است.
🔹
اگرچه دلسوزان نظام با تلاش صمیمانه و قلبی در تدوین این توافق نقش داشتند، اما با بررسی مفاد آن می‌توان دید که برخی موضوعات مهم در آن لحاظ نشده است.
🔹
موضوع ۳۰۰ میلیارد دلار که مطرح می‌شود، غرامت نیست بلکه سرمایه‌گذاری تحت نظر آمریکا و از طریق شرکاست و چیزی برای ما نیست و ۱۲ میلیارد دلار نیز پول خودمان است که پس می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/443092" target="_blank">📅 23:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443091">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: بنده علی‌الاصول دربارهٔ تفاهم‌نامۀ رئیس‌جمهور ایران و آمریکا نظر دیگری داشتم
🔹
بنده علی‌الاصول [دربارهٔ تفاهم‌نامه] نظر دیگری داشتم ولی از باب تعهّدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیّت ملّی از طرف خود و سایر اعضا در پاسداشت…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/443091" target="_blank">📅 23:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443090">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌
🔴
شورای‌عالی امنیت ملی: ترتیبات اجرایی و جزییات فنی عبور از تنگه هرمز از طریق مدیریت آبراه خلیج فارس اعلام می‌گردد.   @Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/443090" target="_blank">📅 22:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443089">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
شعام: کشتی‌های تجاری متقاضی عبور از تنگۀ هرمز به‌مدت ۶۰ روز، هزینه‌ای نمی‌دهند
🔹
بیانیۀ شورای‌عالی امنیت ملی: در اجرای بند ۵ یادداشت تفاهم اسلام‌آباد، کشتی‌های تجاری متقاضی عبور از تنگه هرمز باید درخواست خود را به مدیریت آبراه خلیج فارس (PGSA.ir) ارسال نمایند.…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/443089" target="_blank">📅 22:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443088">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
شعام: کشتی‌های تجاری متقاضی عبور از تنگۀ هرمز به‌مدت ۶۰ روز، هزینه‌ای نمی‌دهند
🔹
بیانیۀ شورای‌عالی امنیت ملی: در اجرای بند ۵ یادداشت تفاهم اسلام‌آباد، کشتی‌های تجاری متقاضی عبور از تنگه هرمز باید درخواست خود را به مدیریت آبراه خلیج فارس (
PGSA.ir
) ارسال نمایند.
🔹
به موجب یادداشت تفاهم اسلام‌آباد، به مدت
۶۰
روز، هیچ‌گونه هزینه‌ای از متقاضیان دریافت نخواهد شد و این هزینه‌ها توسط دولت جمهوری اسلامی ایران تأمین می‌گردد.
🔹
بر این اساس به مدیریت آبراه خلیج فارس دستور داده شده، در جهت تحقق اهداف تفاهم‌نامه درخواست‌ها را با سرعت و اولویت رسیدگی و پاسخ دهد.
🔹
با توجه به شرایط خاص و وجود برخی مخاطرات ایمنی در مسیر عبور و به دلیل لزوم حصول اطمینان از تردد ایمن و جلوگیری از حوادث دریایی، لازم است کشتی‌ها در مسیر و زمان اعلامی به آنها عبور نمایند تا به تدریج، امکان تردد افزایش یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/443088" target="_blank">📅 22:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443087">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5WZjONJ4XxqfzhF7kK0cll9avMdtbV3XsiNi1nkMox2kyuidoP0nUxCqVxS7hl7bISzdxgkJikiYj-w23eYs_ZToCKK0CqTGwloLd3FYaJF_kxLUMBBO5RxNBTtIMKoaEjedFwfozOgekqcXuI_XffzJq4oX9xUNMYRjRhcUmTx_DNvwPbb3RiJ47Njmh12xd92wdXjBxhenBdBU-v5PCgQYLmV5GaNAApocxuGfS7YURj3n08JprArzyumnQMt4OMlVBcMRkwDzT6YY6csHUT2FQajmM91-3CgGQQ79YfBbto8bXOzZMBzT5r61XImtTL6m7uF0T2t7YERUA0wCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رامین رضاییان به‌عنوان بهترین بازیکن زمین انتخاب شد. @Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/443087" target="_blank">📅 22:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443086">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f3f973b4e.mp4?token=v7KL2QYbkndfKrag5tiTviveGEnTl8J78pLcnNL3pbbww-CTnc2l9lpaqcFhiOjo8CPnrGFDlgEs4ZYqLsSqQ5nFUKgWpiwHsuXio87K8j6SridLHz6XLPzhhor9LMib9nloR9ysRgqxB7Qoet9gwDria7tX39agLqFQM4V3jst5tr-eWcUCHhImHej0l43URXqowejOPOI-IMUgaV54kkb1OvkUeCobVWCKqrDISnEGThhmANgNTzxFKb3wbp21NHO-bviCSx5PehdO8jLN2X8Qn0D3wuu7uQsLpvWj6bBiphMx3pQo8B57UzKYCcT-WPBA11K3VrmscQud38Ut1YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f3f973b4e.mp4?token=v7KL2QYbkndfKrag5tiTviveGEnTl8J78pLcnNL3pbbww-CTnc2l9lpaqcFhiOjo8CPnrGFDlgEs4ZYqLsSqQ5nFUKgWpiwHsuXio87K8j6SridLHz6XLPzhhor9LMib9nloR9ysRgqxB7Qoet9gwDria7tX39agLqFQM4V3jst5tr-eWcUCHhImHej0l43URXqowejOPOI-IMUgaV54kkb1OvkUeCobVWCKqrDISnEGThhmANgNTzxFKb3wbp21NHO-bviCSx5PehdO8jLN2X8Qn0D3wuu7uQsLpvWj6bBiphMx3pQo8B57UzKYCcT-WPBA11K3VrmscQud38Ut1YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مستند پاسدار پنجاه‌وهشت
🔹
روایتی مستند از زندگی سپهبد شهید علی شادمانی، فرمانده قرارگاه مرکزی خاتم الانبیاء
📺
فردا حوالی ساعت ۱۴ شبکه سه و ساعت ۲۱ شبکه مستند
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/443086" target="_blank">📅 22:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443085">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOYrhhMDQV8afm1FyNmKTEiPv-aHh9cKBFM_-6A2hBlAzZ9JYAP3TAawidEDv7R8ydTNbjRWhUmf_9vksAV6SYeYlgdhw7kifPyK1ZmSIQYYBIxJLwGR1uBH09c43GYglpln3sTXISoF1PLUz87FsjnKMRZhdVHyXK2MGExjJBKgCn7QY1Gteli7v2nAVEtUVV1umwHOSdpWI4-LkikRNgf-WHvEpXs0-5uc0LpmwspPhn_yHM8WMrVxilNNh71q5uXLZWvUilFA0RQe38YrQVgXhH0pXzU0fQnmUcofmh7F0HlhBTnT9tDYnr-48g-oMYF6B2o2x3IhsXAQt0IyFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ ژست حمایت از آتش‌بس در لبنان گرفت
🔹
ایالات متحده به صلح متعهد است و ما همۀ طرف‌ها در منطقه خاورمیانه را تشویق می‌کنیم تا به تعهد خود برای اجازه دادن به پیشرفتِ زیبای مذاکرات ما پایبند بمانند.
🔹
بازارها از آنچه در حال وقوع است بسیار خرسندند؛ قیمت نفت به شدت کاهش یافته و ارزش سهام به سرعت در حال افزایش است.
🔹
ما انتظار برقراری آتش‌بس کامل در تمامی جبهه‌ها، از جمله لبنان، حزب‌الله و اسرائیل را داریم.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/443085" target="_blank">📅 22:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443084">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ادامه حملات اسرائیل به جنوب لبنان
🔹
رژیم صهیونیستی در یک حمله پهپادی، منطقه «زوطر» در جنوب لبنان را هدف قرار داد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/443084" target="_blank">📅 22:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443083">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce3e38f31.mp4?token=aV6S7z9QScq2jV1imYZ9qM_2AQEW62LMU0zdcj5pM0t0Q14T5c61izTamfNFhZXZ7hXMMptfbDTZ9P2YI-gGsnA1v0E5ZkfwcgD7xrlHSEatC0JbUCpWK3xqyhKJsiP0whFUhpTUAbh75phZjLneXAGt3fS5_NFAUXRdqynCrn-tMc8vvCpxlJZfpIMV5YqY6-u7-B1oJvGtlFqva6TH2T5p7YTuMT-oRpMSTNWpAbWneh1uuIApT4SX1dG0vi7z42NEOt_aYoBVeuPZUSIJcs2TdPRC4BxYe9NAYGyLz5KcwU8fTyMLSLRBVkJSJPzF10wEnmxrlE1vFNNxG7K8hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce3e38f31.mp4?token=aV6S7z9QScq2jV1imYZ9qM_2AQEW62LMU0zdcj5pM0t0Q14T5c61izTamfNFhZXZ7hXMMptfbDTZ9P2YI-gGsnA1v0E5ZkfwcgD7xrlHSEatC0JbUCpWK3xqyhKJsiP0whFUhpTUAbh75phZjLneXAGt3fS5_NFAUXRdqynCrn-tMc8vvCpxlJZfpIMV5YqY6-u7-B1oJvGtlFqva6TH2T5p7YTuMT-oRpMSTNWpAbWneh1uuIApT4SX1dG0vi7z42NEOt_aYoBVeuPZUSIJcs2TdPRC4BxYe9NAYGyLz5KcwU8fTyMLSLRBVkJSJPzF10wEnmxrlE1vFNNxG7K8hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ تیم ترامپ تفاهم با ایران را به کنگره ارسال کرد
🔹
پایگاه پولیتیکو گزارش داد کاخ سفید «یادداشت تفاهم» مربوط به توقف خصومت‌ها با ایران را به کنگره ارسال کرده است.
🔹
این اقدام پس از چندین روز اعتراض نمایندگان هر دو حزب صورت گرفت که از عدم دسترسی زودهنگام به…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/443083" target="_blank">📅 22:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443082">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4545cba63.mp4?token=v256IhHFYWjj-vDX7aBUEO5yFSh0S-JqmPKVtgbdJwo5ma8LGqVaoDZSbSYosWiBN0gYypNLkUCj-TWddXSv3ovTI9nMaWn2lDX2crG_LmR5r-w1ZVcO9SibohZtsVYgJyndrdQtHgoL9nnjJELjzmHZufMI0Qw6LOQCuEprLBMqn-Kc95dk0UGw_4E5jC-5ZS-lrn0AARR95OcE30yd5dJ5My4ULUkY5adjiKR-byRrWC8aOR2YoH6GNGVpYSAZ40ikelvHnGhRKI_x-CXDJzomMM70z_decvrPObPZwkPf5bxPsmPtwa6CGVds6yF7bKwWLJ2MzsUQhwNqHo_D_YjIJWguPI6-xjY_PlEE6ofFJ9bksLTroer7GwiDGOIkO5FI3Y_YyVc9FqyufCllKvejsbDRJ7V9Nx_U8Xuxnvt8R8Z-SpSsrUE1_9yX984ObtFPT0yziJvWu61ZufsdjpBIQlpem-OnD-LexJquJ8XDjKqaxxh_9R2aOtY1yud3Hj0XkCiaZFUBALSGwRXouZZUS77TJBkjZK7K0Fa2IpljNN_yR73DqQRdDpdspmmohGCIO7vKLX1tZdvTYREvoMTdDQ9JJZ8MOKZmkC1tVeUTggO-aJNCTODV1ake9Ub_81wNO4WmouCJQYH6QTeQ-Uv6bG1KHVIGmlYXIC8LGhE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4545cba63.mp4?token=v256IhHFYWjj-vDX7aBUEO5yFSh0S-JqmPKVtgbdJwo5ma8LGqVaoDZSbSYosWiBN0gYypNLkUCj-TWddXSv3ovTI9nMaWn2lDX2crG_LmR5r-w1ZVcO9SibohZtsVYgJyndrdQtHgoL9nnjJELjzmHZufMI0Qw6LOQCuEprLBMqn-Kc95dk0UGw_4E5jC-5ZS-lrn0AARR95OcE30yd5dJ5My4ULUkY5adjiKR-byRrWC8aOR2YoH6GNGVpYSAZ40ikelvHnGhRKI_x-CXDJzomMM70z_decvrPObPZwkPf5bxPsmPtwa6CGVds6yF7bKwWLJ2MzsUQhwNqHo_D_YjIJWguPI6-xjY_PlEE6ofFJ9bksLTroer7GwiDGOIkO5FI3Y_YyVc9FqyufCllKvejsbDRJ7V9Nx_U8Xuxnvt8R8Z-SpSsrUE1_9yX984ObtFPT0yziJvWu61ZufsdjpBIQlpem-OnD-LexJquJ8XDjKqaxxh_9R2aOtY1yud3Hj0XkCiaZFUBALSGwRXouZZUS77TJBkjZK7K0Fa2IpljNN_yR73DqQRdDpdspmmohGCIO7vKLX1tZdvTYREvoMTdDQ9JJZ8MOKZmkC1tVeUTggO-aJNCTODV1ake9Ub_81wNO4WmouCJQYH6QTeQ-Uv6bG1KHVIGmlYXIC8LGhE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلتنگی مردم برای رهبر شهیدی که جایش محرم امسال خالی است
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/443082" target="_blank">📅 21:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443081">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دفاع ترامپ از تفاهم با ایران پس از سیل انتقادات
🔹
نفت در جریان است، ایران هرگز نمی‌تواند به سلاح هسته‌ای دست یابد (جهان در امان خواهد بود!)، بازارهای سهام در اوج رونق هستند، آمار اشتغال رکورد زده و قیمت‌ها در حال کاهش‌اند (قابل‌خرید شدن!).
🔹
کشور ما به گونه‌ای…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/443081" target="_blank">📅 21:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443079">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
رهبر انقلاب: از این لحظه، ما یعنی شما ملت سرافراز و این خادم ناچیز، منتظر تحقّق شروط گفته‌شده خواهیم بود.  @Farsna</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/443079" target="_blank">📅 21:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443078">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAo-13QOZROR-TWe2QwPEey-7uBmaJrJKfUA8MkKhfffq78EJfe7Ffn63XZJlRzbKHlR2p6qdebQEjtsjsAVgsMm0I1NiN_hlUWJyJEiykKb5Al-XhAtKg2sLnmrh-4I04CpZnw7Gmr6JsGVGNzSoBUsxzgY-m8gVjRSNWmhRUXdEPrtVK0qB0hrl0QpoFnNIr_z1fZHeS0FfG4WUlJ82MHrecu1mr3Oua4MRLIjdlUZWNW9V05i8eH8cGZvh9ZN9rxyHpTIUwToJwey0HoJwPMw_CPuDcLXJHuHYy8uRUxgK5wahCn7_jHnNQasR7S98taMVBx9V3yLch3Cpu4VcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رهبر انقلاب: بنده علی‌الاصول دربارهٔ تفاهم‌نامۀ رئیس‌جمهور ایران و آمریکا نظر دیگری داشتم
🔹
بنده علی‌الاصول [دربارهٔ تفاهم‌نامه] نظر دیگری داشتم ولی از باب تعهّدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیّت ملّی از طرف خود و سایر اعضا در پاسداشت…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/443078" target="_blank">📅 21:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443077">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">متن کامل پیام رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا
🔹
ملّت پرشور و باوفای ایران، همانگونه که مطلع شُدید، تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و امریکا امضا شد. در مسیر رسیدن به این مرحله، مسئولین امر، از سر دلسوزی…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/443077" target="_blank">📅 21:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443076">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMvoBOpEFTQ4RQbOMSoLDgNRPb43pLw3LzC-ul_i3955S7ISgb0BWCo0y4uLVLHmLYyJ_f78EHmvdNuv7D7hHBmWqdEL_ZXbMyW2AEfYNFcLRij45yW65H1ysDfruD_lYrEC7CcWAjrOeMu6cskVf7LJYQ0kbxv4aXj0drBDrNNac4QJQy_IS557ECzRXlDxUSImawOWKbJkyh8QMD1MFghuDpu8fMnTgHO4Upx1oJNHvWp32kSc6GN0rQt2sShkNdMTkzL2JKi77eKMlVhzOe348RR-T6uvJikpL1Jlazpab935Z1KHp3ubkK8yL06zQZ11bNs40Ixr1zju7uS9Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تا ساعتی دیگر، پیام رهبر انقلاب خطاب به ملت ایران دربارۀ تفاهم‌نامۀ رؤسای جمهوری ایران و آمریکا منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/443076" target="_blank">📅 21:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443075">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9cc72c133.mp4?token=p40nPOhuCTSecijWTlb1p_mB1gONXFeY9Akljg38_8b7doI1eRFCtnmEXeeO2Ycly7WDZJyJIIuWdVzPZrAP1PYomfmQLfQihVx3EgV5Vpx0fra2GES_FnXEcFBHNuvOgqnnePMxf6EBKDalYDax0vuhYd8bqea1QAoSBaaQGIpPShsaS9oPNjZG2ASbPeCEf1F_71fHajXdHrbY2y4FD2IqzhXxX61vHiN2Mavq6p5-XFyeKvH06e39stbKHnUjaaYN3X4h04FtkKHSYWTl8FsQ-VwYLhnoqVKcYS_rK850B-mErCJ3q77lMJTVOl_eQwuney8UOwpYpwJExg-BdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9cc72c133.mp4?token=p40nPOhuCTSecijWTlb1p_mB1gONXFeY9Akljg38_8b7doI1eRFCtnmEXeeO2Ycly7WDZJyJIIuWdVzPZrAP1PYomfmQLfQihVx3EgV5Vpx0fra2GES_FnXEcFBHNuvOgqnnePMxf6EBKDalYDax0vuhYd8bqea1QAoSBaaQGIpPShsaS9oPNjZG2ASbPeCEf1F_71fHajXdHrbY2y4FD2IqzhXxX61vHiN2Mavq6p5-XFyeKvH06e39stbKHnUjaaYN3X4h04FtkKHSYWTl8FsQ-VwYLhnoqVKcYS_rK850B-mErCJ3q77lMJTVOl_eQwuney8UOwpYpwJExg-BdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: کسانی در اسرائیل هستند که دوست دارند ایران را به لیبی تبدیل کنند
🔹
آیا فکر می‌کنم افرادی در درون جامعه اسرائیل وجود دارند که بخواهند ایران را به لیبی تبدیل کنند؛ یعنی اساساً یک دولت شکست‌خورده با ۹۰ میلیون جمعیت؟ احتمالاً بله.
🔹
تبدیل ایران به یک دولت شکست‌خورده برای آمریکا خوب نیست.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/443075" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443074">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXMzd_hibgBsEjgfnZEf_gkK6gyEIVsdfCOU5knfaGi_iNKABQivLwnUnZ1AhJ9jlCxHhsMkJlcsrxQcIF5pdm0k7w_xNQHunyWkdHb3NHvHih5f2kcTlyDS0aX50sSlgW5dfFNtSt80m52DknVfxCi5HmUpqxY83lYQZ0znoVVF9x54o1hSYj7K03vv7QZOo5n1gOyzSEzQ3K1g_gjCP9RufcCfAj9hBQLu8d40chyR3TiAQEJTRCA8hG0EBXUNI09iMymnhrpHUBvgygdoTLwr3Py3Xl3yGhD5g9mKPAsIVLQwDKX_O2rvUnJ3Atp3PjTm7FifxvFeCx1DgnTeiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ برنامه‌ها برای پرداخت ۳۰۰ میلیارد دلار به ایران را تکذیب کرد
🔹
رئیس‌جمهور آمریکا در تروث‌سوشال نوشت: «هیچ پرداخت ۳۰۰ میلیارد دلاری از سوی ایالات متحده به ایران وجود ندارد. این‌ها اخبار جعلی است!
🔹
آنچه برای ایالات متحده وجود دارد، تنها موفقیت، کاهش قیمت نفت و پیروزی است. نگاهی به بازار سهام بیندازید.
🔹
این‌ها تبلیغات داموکرات‌هاست، (داموکرات لقبی است که دونالد ترامپ برای تمسخر دموکرات‌ها ابداع کرده و می‌توان آن را به احمق‌سالارها ترجمه کرد.)
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/443074" target="_blank">📅 20:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443073">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">واشنگتن ۲۴ ساعت پس از تفاهم، در بوتۀ راستی‌آزمایی
🔹
کمتر از ۲۴ ساعت پس از امضای یادداشت تفاهم بین ایران و آمریکا، مقامات مسئول در تهران با اشاره به بندهای صریح این سند درباره تمامیت ارضی لبنان و توقف حملات به جبهۀ مقاومت، اعلام کردند که هرگونه گام بعدی در روند مذاکره، به اجرای کامل و بدون قید و شرط تعهدات آمریکا در این حوزه منوط خواهد بود.
🔹
متن تفاهم که روز گذشته به امضا رسیده، به صراحت بر لزوم احترام به حاکمیت لبنان و خودداری از هرگونه اقدام تجاوزکارانه علیه این کشور تأکید دارد. با این حال، حملات امروز رژیم صهیونیستی به مناطق جنوبی لبنان، سوالات جدی را درباره پایبندی واشنگتن به مفاد این توافق ایجاد کرده است.
🔹
مقامات مذاکره‌کننده به صراحت می‌گویند قرار نیست ایران به صورت یک‌طرفه تعهدات خود را عملی کند. چارچوب توافق به گونه‌ای تنظیم شده که اگر طرف مقابل در گام نخست خلف وعده کند، نه‌تنها مذاکره انجام نمی‌شود، بلکه اساساً اعتبار این سند زیر سوال خواهد رفت.
🔹
در همین رابطه تحلیل‌گران با اشاره به دو روایت متفاوت درباره حملات اخیر یکی مبنی‌بر نافرمانی اسرائیل از آمریکا و دیگری جنگ زرگری برای همراهی پنهان تلآویو و واشنگتن می‌گویند: «برای جمهوری اسلامی، تحلیل پشت پرده این اقدامات محل بحث نیست؛ آنچه ملاک عمل است، متن روشن تفاهمنامه و توقف عینی حملات است. تا زمانی که تعرض به خاک لبنان و جبهه مقاومت پایان نیابد، هیچ گامی در مسیر مذاکره نباید برداشته شود.»
🔹
کارشناسان سیاسی نیز معتقدند که اصرار ایران بر اجرای همزمان تعهدات، نشان‌دهنده رویکرد جدیدی در دیپلماسی کشور است که براساس آن، برخلاف تجارب قبلی، اعتماد به وعده‌های آمریکا جای خود را به راستی‌آزمایی میدانی داده است.
🔹
در همین حال، انتظار می‌رود که تیم مذاکره‌کننده ایران تا حصول اطمینان کامل از توقف حملات و پایبندی عملی آمریکا به مفاد توافق در خصوص لبنان، هرگونه گفت‌وگوی تکمیلی را به حالت تعلیق درآورد.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/443073" target="_blank">📅 20:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443072">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
‏با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله به ایران آماده شوند.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/443072" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443071">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
سنت‌کام رسما رفع محاصره علیه ایران را اعلام کرد
🔹
سنت‌کام در بیانیه‌ای اعلام کرد: امروز، نیروهای آمریکایی طبق دستور رئیس‌جمهور، محاصره دریایی تمامی ترددهای دریاییِ ورودی و خروجی از بنادر و مناطق ساحلی ایران را برداشتند.
🔹
نیروهای آمریکایی مانع تردد کشتی‌ها به مقصد یا از مبدأ بنادر ایران در [خلیج فارس] و دریای عمان نیستند.
🔹
تمامی تلاش‌های نظامی ایالات متحده برای اعمال محاصره دریایی متوقف شده است.
🔹
ناوهای جنگی بزرگ ما در منطقه عمومی باقی خواهند ماند تا اطمینان حاصل کنند که تمامی جنبه‌های توافق رعایت شده، اطاعت می‌شود و در کمال قدرت و اعتبار اجرا می‌گردد.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/443071" target="_blank">📅 20:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443070">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxeWn4SNduT69QQBCHX_SzWpGitq8XIc5jCdSFKmua3poRLK3Rl50EjJG2Q_c4uLaC57cwLIF8dLsnzxiRS8JwPXfOQxYYSkr3ie-if6Fed4CSR7PbcsgjWnHL-XQwbb409Prw1bnl7CAyPoVl6Y55sIKIgyniTHppVMYicARWemdQ3PkajVnr0ABuoizfmsKVFRCd5wrhbHkSmJvUc0cVrYxkh54rihpjUiIL2XDYVPHKWLSWyZa9xhy_rdw0X9t2_kyfqEmzeO-Hq-W5k5KODVfbFsY_oOgQGOkABKoPjuIQWoS7W_fcrc-HRXl4L2vxkzoKxnsJiqcFVImqQTGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین دیدگاه‌های موافقان و مخالفان مفاد تفاهم‌نامه و مذاکرات با آمریکا را در فارس تعاملی بخوانید  تازه‌ترین مطالب و یادداشت‌های:
🔸
عبدالله گنجی
🔸
محسن مهدیان
🔸
مسعود براتی
🔸
مهدی خانعلی‌زاده
🔸
کاظم انبارلویی
🔸
مهدی فضائلی
🔸
سید نظام‌الدین موسوی و... را می‌توانید…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/443070" target="_blank">📅 20:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443069">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3f5171b3.mp4?token=o0HtUETDRDBwKQD69Lqt9u4upZkKCBFWFaku74P22YXdGdqL-aEVN9xp6GXSPBjGNQdopnjZ7gEsqGUOEVHvp6MrQTp27Durl9CZqwSa7IvfsMWJUyTBK59W1LBZTqCz9MYkVaBQXcgt9qMk6pMLrMTqrm7bp3hpAU_eUPb9E-uQ4dHI2GHTNXMQV_mxn-eudtRAeRinZRyW6z-rUDp2GFGpCpVkNk6UJWSkmPCB2_lC3kl3gE-RmT2DicJuDI08Cd0NEYLNGS80C02fWkiK3Nl2kW18wjklN1EGqVMx-1-Kzdq3cA0chw6QigKIRjBCvbEauhebXqs46yg45lNIfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3f5171b3.mp4?token=o0HtUETDRDBwKQD69Lqt9u4upZkKCBFWFaku74P22YXdGdqL-aEVN9xp6GXSPBjGNQdopnjZ7gEsqGUOEVHvp6MrQTp27Durl9CZqwSa7IvfsMWJUyTBK59W1LBZTqCz9MYkVaBQXcgt9qMk6pMLrMTqrm7bp3hpAU_eUPb9E-uQ4dHI2GHTNXMQV_mxn-eudtRAeRinZRyW6z-rUDp2GFGpCpVkNk6UJWSkmPCB2_lC3kl3gE-RmT2DicJuDI08Cd0NEYLNGS80C02fWkiK3Nl2kW18wjklN1EGqVMx-1-Kzdq3cA0chw6QigKIRjBCvbEauhebXqs46yg45lNIfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ونس: مقدار دقیق دارایی‌های مسدودشدۀ ایران را نمی‌دانم
🔹
اعدادی بیش از ۱۰۰ میلیارد دلار شنیده‌ام. حتی اعدادی بیش از ۲۰۰ میلیارد دلار.
🔹
بخش عمدۀ این پول در حساب‌های ایالات متحده نیست؛ بیشتر آن یا در کشورهای حاشیه خلیج فارس است، یا در اروپا، یا در جاهای دیگر.…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/443069" target="_blank">📅 20:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443068">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b173f6692.mp4?token=k2iLJFqvt5V7panuF0JuVfUHFI7K1aof3fZ7FflcQE_rfI03BhqKvXcJiEUPD39HOVi2vh9kkUjjViWOojeuCcDbDsKnMcdTyEIuXU2AHReJPRX4kGctXxWZ0tpWi_hwWWNDM6hqeRsY7M9aMQC3KCbU7abZnv0wQZcRp5L4-NRa7e471VqjSzPRN7ZyAV0ZfbYv2iNaPUN1-iGTs7823h_XKRnZcKQNhtDiDBipo-JTV9R0h5UcfF7nQkEF0ToKXtOUTzs6_1vJ-Asdoy4Bl4_e4f34_L3H_eAg-xIf8qsJ61V4kkOhKdX-fdYmyqQj8l5Yb80od3aOk4aNjwHYVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b173f6692.mp4?token=k2iLJFqvt5V7panuF0JuVfUHFI7K1aof3fZ7FflcQE_rfI03BhqKvXcJiEUPD39HOVi2vh9kkUjjViWOojeuCcDbDsKnMcdTyEIuXU2AHReJPRX4kGctXxWZ0tpWi_hwWWNDM6hqeRsY7M9aMQC3KCbU7abZnv0wQZcRp5L4-NRa7e471VqjSzPRN7ZyAV0ZfbYv2iNaPUN1-iGTs7823h_XKRnZcKQNhtDiDBipo-JTV9R0h5UcfF7nQkEF0ToKXtOUTzs6_1vJ-Asdoy4Bl4_e4f34_L3H_eAg-xIf8qsJ61V4kkOhKdX-fdYmyqQj8l5Yb80od3aOk4aNjwHYVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برخورد جالب سیدمجید بنی‌فاطمه و مهدی رسولی با مداحی نوجوانی که در حسینیه معلی شروع به فالش‌خواندن کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/443068" target="_blank">📅 20:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443067">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
تا ساعتی دیگر، پیام رهبر انقلاب خطاب به ملت ایران دربارۀ تفاهم‌نامۀ رؤسای جمهوری ایران و آمریکا منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/443067" target="_blank">📅 19:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443066">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f54cbbb6fd.mp4?token=t2iIKhnWe9ruGklqIH9BrctKZ1ndpkDMB3rNbeKyiWmXznf4ZuhHOxvC8FzONm725hPyRAevVCCALzfaPvzNvaDWRZ1H8bhXNeCdIDKv7UqwSosJfxblcVcTPtj6Q5reoVYbUKM5GZveUcjFEVFHbY6ja1_47PyffWjQVWgCO-L7SwQFWca-VZm5Lv5j1hPxcUQ5TVvY9Hnvaqh7QR5gEt-8JaUzyz4nL1GBgJuuP1yax58g6NqjZdapsn0R7tEvkYbMqtMK4FwG2MxiKENhKMVsgrrz9k9ZEb3KZ72BeJY5L_6a1_64SNxsEsgncKd_BowEPiwBqtwmdey3aXikEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f54cbbb6fd.mp4?token=t2iIKhnWe9ruGklqIH9BrctKZ1ndpkDMB3rNbeKyiWmXznf4ZuhHOxvC8FzONm725hPyRAevVCCALzfaPvzNvaDWRZ1H8bhXNeCdIDKv7UqwSosJfxblcVcTPtj6Q5reoVYbUKM5GZveUcjFEVFHbY6ja1_47PyffWjQVWgCO-L7SwQFWca-VZm5Lv5j1hPxcUQ5TVvY9Hnvaqh7QR5gEt-8JaUzyz4nL1GBgJuuP1yax58g6NqjZdapsn0R7tEvkYbMqtMK4FwG2MxiKENhKMVsgrrz9k9ZEb3KZ72BeJY5L_6a1_64SNxsEsgncKd_BowEPiwBqtwmdey3aXikEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: به ایران اجازۀ غنی‌سازی اورانیوم نخواهیم داد
🔹
جی دی ونس تفاهم حاصل‌شده میان ایران و آمریکا را با توافق هسته‌ای سال ۲۰۱۵ در دوران رئیس‌جمهور وقت آمریکا باراک اوباما مقایسه کرد و گفت: «توافق هسته‌ای اوباما اجازه غنی‌سازی را می‌داد، اما توافق…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/443066" target="_blank">📅 19:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443065">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ff243d00.mp4?token=gu901bPm3Kb0ObQ7gcZTmpfQYXW5IpM8bc_OYjKO1z1Fhg5jA5ENblyir3xBV0XYfUXzddEvr_r0ZC4Mzy2WhpwCaxq4EOoAXrhSvsm2PeqUCWqQDNHh5C7wcDaVj3Ulau1yhfvzSEiTTswQMtHaIj8nYDst375YU9oEgi4B-DsuOzSNzY0vQveF6cCzEsnd0HWVBda3eaax1e8VWijLmguJ4xdNY-H2G-oeGtHJRDRcS5mfDHXhzuNUawqg8SGNuMFwPHDmNATTAuP7oqQcZ2Ghc4u4Zt2IwVSEIJXNbTX9SlXvMeEA4yGgOKkDXEIfTdKB9K7kWm5X3d_jHxCsqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ff243d00.mp4?token=gu901bPm3Kb0ObQ7gcZTmpfQYXW5IpM8bc_OYjKO1z1Fhg5jA5ENblyir3xBV0XYfUXzddEvr_r0ZC4Mzy2WhpwCaxq4EOoAXrhSvsm2PeqUCWqQDNHh5C7wcDaVj3Ulau1yhfvzSEiTTswQMtHaIj8nYDst375YU9oEgi4B-DsuOzSNzY0vQveF6cCzEsnd0HWVBda3eaax1e8VWijLmguJ4xdNY-H2G-oeGtHJRDRcS5mfDHXhzuNUawqg8SGNuMFwPHDmNATTAuP7oqQcZ2Ghc4u4Zt2IwVSEIJXNbTX9SlXvMeEA4yGgOKkDXEIfTdKB9K7kWm5X3d_jHxCsqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: اسرائیل باید به روند صلح احترام بگذارد
🔹
جی‌دی ونس: اسرائیل حق دارد از خودش دفاع کند. اما در نهایت آنها هم درست مثل هرکس دیگری، باید به این روند صلح احترام بگذارند؛ روندی که در اصل برای آن‌ها و برای کل منطقه، مثبت و سودمند است.  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/443065" target="_blank">📅 19:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443064">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاطلاع‌رسانی بانک سینا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etdnMgCt7hF5WoetYHnDwlZFxScuD9pl56Y6wN4GHwen52AMMFngOXLpGCgqQWhEf_wwHsDcBmoyUNALOQ6k57HUhgdgz3efSd4igAi-XVuppwbUHPm3Lj6PNmXV5RuNhwEcTkHUxJtbMpbG8IEYaIyIGETt04qEboLkzQ3IqTV56YxnmvFaed0w-CQGoex268L13F0EmH-mLGHT66xQuqvxeye-TX0AW6e42YSoTffRUq5-IshIMgzOMnuTuuwlw7LCL5uT3m0YwxExHX1TELR-BlHhqjt9cWzG8Mf0rcnZbVtGU5nSaBUXsWzuxwooYBzi_I9D76Fn6Dbd6kYaOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک سینا به رتبه دوم شبکه بانکی در ارزیابی سامانه آرش ارتقا یافت
🟨
بر اساس آخرین گزارش اعلام وضعیت بانک‌ها در سامانه آرش بانک مرکزی جمهوری اسلامی ایران، بانک سینا با بهبود عملکرد در شاخص‌های ارزیابی این سامانه، برای اولین بار به رتبه دوم بانک‌های کشور ارتقا یافت.
🟦
ارتقای جایگاه بانک سینا در این رتبه‌بندی، بیانگر توجه مستمر این بانک به بهبود فرآیندهای پاسخگویی، صیانت از حقوق مشتریان و ارتقای کیفیت خدمات به مشتریان بوده که نتایج مطلوبی به همراه داشته است.
🟨
گفتنی است این بانک، ماه گذشته نیز در ارزیابی و رتبه‌بندی بانک‌ها بر اساس مدل ارزیابی کملز (Camels) که توسط بانک مرکزی صورت گرفت، برای دومین سال پیاپی جزو پنج بانک برتر کشور شد.
▫️
@sinabank
| بانک سینا
▫️</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/443064" target="_blank">📅 19:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443063">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtRxmVoak8wVwc0tLQ0oxJeqg_zkI5vsP8-Gg4MpIM0PlQ7b3Vp-c0F1pEvb3CdzLzOOwJyFmYSve44tajbj6PsJYf0Rt8u06lZ-bnWExVirmWGQHiu3TniZO8llDOnYgj8G-OLiLdVNC3xdL0oL7dWAT8iBwYwCniqgX3YxNWGZ7MVR6U_xScChWlD8lV8t-KYtuwjjwz7V0xqf2BT_Mhj2bQJcsGzX73YYzk9vnMHw5UDg3tqxS1IS804N9bmNA_A06SNhwLC0xEhIFmkpvGEJS25m6j_hRdvt-Un52ItW53cLMayPlVIUsebsJKSSFxaRawaNqOK0ylARdD5g3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
در نشست همکاری پایدار اقتصادی ایران و چین مطرح شد
🔰
سه پیشنهاد مدیرعامل مس ایران برای توسعه همکاری‌های راهبردی با چین
🔻
مدیرعامل شرکت ملی صنایع مس ایران در نشست هم‌اندیشی فعالان اقتصادی با رئیس مجلس، با تأکید بر ضرورت ارتقای همکاری‌های ایران و چین از سطح تجارت به سرمایه‌گذاری مشترک و انتقال فناوری، سه پیشنهاد راهبردی برای توسعه همکاری‌های دو کشور در صنعت مس ارائه کرد.
🔹
نشست «همکاری پایدار اقتصادی ایران و چین» امروز چهارشنبه ۲۷خردادماه با حضور دکتر محمدباقر قالیباف، رئیس مجلس شورای اسلامی و نماینده ویژه در امور چین، سیدمحمد اتابک، وزیر صنعت، معدن و تجارت و جمعی از فعالان اقتصادی برگزار شد.
🔹
در این نشست، دکتر مصطفی فیض، مدیرعامل شرکت ملی صنایع مس ایران، با اشاره به جایگاه چین به‌عنوان بزرگ‌ترین مصرف‌کننده مس جهان و نقش این کشور در توسعه صنایع پیشرفته، بر ظرفیت‌های گسترده همکاری میان دو کشور در زنجیره ارزش مس تأکید کرد.
◀️
ادامه خبر در پایگاه خبری مس‌پرس:
https://mespress.ir/x6R9
@mespress_ir</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/443063" target="_blank">📅 19:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443062">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/443062" target="_blank">📅 19:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443061">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c774ae30.mp4?token=pPc61vnFiTEf_Ey-pwtDM8MNphC5kMVSShyaGPND3nDeei6aCq7Zl4s4SolrzMhLnehQdNUYoZauWb86jCSTrO49kranUQEMdBTqi1DimT4r6g81FlrKxYH6Fc55qXE8OUTSaklrhdelXY1OerGXFFx6xmwxpTL647Xnog24IlWhwmNDblzewqtbjpnJXko3G-Pvpj_uxSDO34LYGh3VWg2pHgitsBVUZokFwhIsoqs_coXY-tRokwXoIDe9Tn4DFQ9G3OqC3RU0FfSCmWxtswJWRrO2G-PjwF6Lv-01OpOMiH0E9VphtSEJVGzjvfYfE6Pjg9ZXwz2SCs47g_vqnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c774ae30.mp4?token=pPc61vnFiTEf_Ey-pwtDM8MNphC5kMVSShyaGPND3nDeei6aCq7Zl4s4SolrzMhLnehQdNUYoZauWb86jCSTrO49kranUQEMdBTqi1DimT4r6g81FlrKxYH6Fc55qXE8OUTSaklrhdelXY1OerGXFFx6xmwxpTL647Xnog24IlWhwmNDblzewqtbjpnJXko3G-Pvpj_uxSDO34LYGh3VWg2pHgitsBVUZokFwhIsoqs_coXY-tRokwXoIDe9Tn4DFQ9G3OqC3RU0FfSCmWxtswJWRrO2G-PjwF6Lv-01OpOMiH0E9VphtSEJVGzjvfYfE6Pjg9ZXwz2SCs47g_vqnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاش ونس برای عقب‌نشینی از اظهارات ترامپ دربارۀ برنامه موشکی ایران
🔹
معاون ترامپ: همه چیزی که رئیس‌جمهور ترامپ دیروز گفت این است که طبیعتاً کشورها حق دفاع از خود را کنار نمی‌گذارند.
🔹
اگر حزب‌الله به سمت اسرائیل موشک یا پهپاد شلیک کند، اسرائیل حق دفاع…</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/443061" target="_blank">📅 19:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443060">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ffa7c4fc.mp4?token=qr-J7siB-5HX5NxjiJWIjC-ud20O7IDu0biX-6xcotqbY9zkMorBB5R-gQy1PVNMCvcmtRHmLMO-9l0KYdgS3mMSQxClOFNuRz0s98vPQRJK651lQqI1DdLxx5-QB0a6yJEDxbgu7I8raxflAFrqF56Y1hDj9OLh7cR_1ltA0QI7J_ux3gukd-dbk1a0FeDGDHz6_hTNlzhn4-LlOAGCJKjSRGK2Q6Pi1gIdFsYchcud6fVIDkGs86tr3_SRYczA7I1nckNH81kbO2FAsdMYZVrPi9ra9rZDr__A1VU1QZMm2CnelldLHr-3Oav4la-7AAuFUa-XIBPFYRzU4SlqaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ffa7c4fc.mp4?token=qr-J7siB-5HX5NxjiJWIjC-ud20O7IDu0biX-6xcotqbY9zkMorBB5R-gQy1PVNMCvcmtRHmLMO-9l0KYdgS3mMSQxClOFNuRz0s98vPQRJK651lQqI1DdLxx5-QB0a6yJEDxbgu7I8raxflAFrqF56Y1hDj9OLh7cR_1ltA0QI7J_ux3gukd-dbk1a0FeDGDHz6_hTNlzhn4-LlOAGCJKjSRGK2Q6Pi1gIdFsYchcud6fVIDkGs86tr3_SRYczA7I1nckNH81kbO2FAsdMYZVrPi9ra9rZDr__A1VU1QZMm2CnelldLHr-3Oav4la-7AAuFUa-XIBPFYRzU4SlqaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ایرانی‌ها باید تعدادی موشک داشته باشند، چون دیگران هم دارند
🔹
ما روی یک تلاش موازی با کشورهای حوزه‌ی خلیج [فارس] کار خواهیم کرد تا به مسائل غیرهسته‌ای، مانند موشک‌های بالستیک متعارف که درباره‌شان صحبت خواهیم کرد، و حمایت‌ها بپردازیم.
🔹
کسی می‌گفت:…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/443060" target="_blank">📅 19:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443059">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🎥
عزاداری یزدی‌ها در حرم مطهر رضوی
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/443059" target="_blank">📅 19:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443058">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqkMY_7KGlq380uubxXUZHtHKMmZN2ygwkKXa1l2sUAYK6iPuqu2xnaPzldp6INuqqQpKtlMZA_Tr9saab-begQ9_wa98EBtC-Ged4NSCLBJ8SOzK7wyAvOHy4ttX9ER2W0hjqdjoQBkn780c59lWp2RVPGlH8OQK7lwV7jDRqJR9YYg_QGfBs-kGjEdbsNXTwIMcthfMU20CHt3ZTYj7eNF3whTXnyB7CaJXVRyjGmna7uNr_Sje_o9wUz8wOeTSdP6hhhyWhyybv1Ewd079qTI4HNuBSWIKACvakEIk3IaMpVdV9VU19mQHu7bPWxgWDFhs5jlA5QylUSop-WoPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: تلاش‌های پاکستان در مسیر دستیابی به توافق پایان جنگ در حافظه ملت ایران ماندگار خواهد شد
🔹
رئیس‌جمهور در گفت‌وگوی تلفنی با نخست‌وزیر پاکستان با قدردانی صمیمانه از تلاش‌های دلسوزانه، مسئولانه و دغدغه‌مندانه دولت پاکستان در مسیر کاهش تنش‌ها و پیشبرد…</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/443058" target="_blank">📅 18:56 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
