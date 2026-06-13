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
<img src="https://cdn5.telesco.pe/file/gNNVh2833jllNBAAH0LtGceiQcALpzka1QtHFEjyV2-vEJydTmamlHEyCM4cWvCzGzfPZROuz29eXgqDhzrBDAt_EeGVWUFJ8Za8-uBiExI8_oaAaS-DnjZaOIzumN-DCI8oi03mS2fymuFA_itAzKqDNGDXc_gqKbPNJ97heZ03tq4NhSQeSIbiTVDDfY5zFnA0rCiu1rxZWfvx4R58G-ntJbB02j5ev6sxDuG4UWiOAGa14KOcQ_U6cd5ywP5eugl11OuUwU-1Gou5u1SU1lMuids4XdZz5x1tlNWe9XIVGe72ueAJz3MotP7TDt1YyIjtK3o6D3hrIgu5Mr0OiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 510K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 00:15:23</div>
<hr>

<div class="tg-post" id="msg-92683">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3a1d64a3.mp4?token=v7MpeVm7YiM5SNhfLABSWJqJ6iyQANhHxuXTxCetmQO-fe7StpTRaHkxLhGtNFuCugTVNPKrXvyAntly0C6_4ymSfMcS3W-NBiBPy8vheKVirfG7GQ18sDsg33YVGjgeDav9wWVvOSRcxsg9mKUVKfiQW4F1xabsHhM3hJqjvGLZXvdqRYl3WZTtiWBLATN14YYH3cMpfuH8DDnDHNV9QpNijDdXPSoMaQsUFyq_rsJoBnSr37Z2fmkUSD_gNJ__CHmTu5t6Gi2OWRHSTj8dLNUlGOiLgHlYtQ1lYJJu28j4fiIsvFXjUPqH45VQ-8tk_sriz0bCbezG1NhTGxDHqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3a1d64a3.mp4?token=v7MpeVm7YiM5SNhfLABSWJqJ6iyQANhHxuXTxCetmQO-fe7StpTRaHkxLhGtNFuCugTVNPKrXvyAntly0C6_4ymSfMcS3W-NBiBPy8vheKVirfG7GQ18sDsg33YVGjgeDav9wWVvOSRcxsg9mKUVKfiQW4F1xabsHhM3hJqjvGLZXvdqRYl3WZTtiWBLATN14YYH3cMpfuH8DDnDHNV9QpNijDdXPSoMaQsUFyq_rsJoBnSr37Z2fmkUSD_gNJ__CHmTu5t6Gi2OWRHSTj8dLNUlGOiLgHlYtQ1lYJJu28j4fiIsvFXjUPqH45VQ-8tk_sriz0bCbezG1NhTGxDHqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
آفتاب‌گیری رونالدو و رفقاش در سواحل آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/92683" target="_blank">📅 00:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92682">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi0_ozdJwqZszQBnV4EZu4azFYV9dlsfX628fngZiN-uV-wr9ygBnZCCKVToYG_tRVeTTNBl25pCUVD4SbwUCIPluuPbBUaAJChYFxMf_8oAG2iOsLFDTCwe5ijYIuwqytndPXzStWOelmDyEcrpSpNEWmouXMbmqvBaiXfOKWdvZvzfv1sYgOVrUjZpNFXuXVLXN4fFmQdFYByCn6rmYMAWiUnsOpuCdTffKfOrWX73-84sog6FdoMtHOVva_hkyEeO7ysViUdS3TSU1V2GKlgFiR6x7DilvVvTOC119AoNf2WEoecmreHCCWYTeZW9Y7ijyUKD0RWz7cXYPPBozg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇧🇷
ترکیب تیم‌ملی برزیل مقابل مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/92682" target="_blank">📅 00:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92681">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8gOGKal05fJi6eiPU7MpY2WBQLUJD2lzywYQPTEMU0IiYLbV9yNcidrD8z4H6EdRPgdHrdrJYANHWR1EibkVt8bsmekqhoXtA2NIZ7Te4BXvRk_FFUGUoiH1XLL16Kbu_R5386t8T9y1sqDKmJDZD2hkY9SHGtMG5PtSR1C3s9UqjnshigYV85De4hD_XNNHDAV9ezDCmhN75thNFHIk1iNDIZ3kd8VQjClsz477lJO8LJQfHuT_QosoVW5pAGsiX7RPFJh6hUnmolDEoeNhCP-U0JLZbuyD1W6HWk22SnlmobKd-xW043gE7tqijNL_sXuBdaIKeJGLnKP26gpXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیگو سیمئونه: «من بازی خولیان آلوارز رو دوست دارم و اونو به همه بازیکنان ترجیح میدم مگر اینکه حرفی از مسی وسط باشه.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/92681" target="_blank">📅 23:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92680">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">قطر تا اینجا کون اورده ۴ ۵ تایی نشده</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/92680" target="_blank">📅 23:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92679">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نیمه دوم بازی شروع شد</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92679" target="_blank">📅 23:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92676">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U89P75MdcfrogNGyOCVU4k9LbcECqMc6rvKfG3gwzDYaf1zd_NdF49PJlrHL-626o2T4JXsp4llxaCfpdTGmirx4N2ibfL8UK1_WtpWptH7Z0PrUE7jm7jvmHSL6wDamlW0-nStLxcxdkoZdurTc7XG1qvPZRg61E86CTMuH2kx__ulNHN6icE4VUJBUbDOoFROl0lNRxk7OFyr657_W0ilpUCYCsr6jeg18ERaPEEhkS8OfwmlaPKV_7HWxDN-oiLfXtZQ-jUSe30jEC7UqOGANEXtj1e4znB2kTfVVyJ2L1O7L7dT1AMLnRMXH1Heu2MGvXQjiRZRt4h4akYpsEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OKPjN3jh1YMiod3YXi_30x0v9o1pLTH8pZb1az3RfDbzWap9HQwUY2gVtVzMA7aVoPSwgGzaKStS5hkMrCtdf8NsRn2p6jfWdRCPlyWfnTLV8U7UPJuDB9zR1IXePOd370y6hg4BZWmHsRLsqp-pSvBLLn9359nbcY-FIP7zVbESm2zSqLtgsNENzqoB4fLDtaZszPZy85p9LN1eqIIVGeGIJ26g4hhigo_6H5GOaHdxuLN_OQvb28PRMPXGkkL-cd0hXdzdpCN8h5GCYQxN-34aDcBZNXOudzm6KH6s_dVgfVh4q7qK0xqIRw4pG3CvR7-ScYWv7Nq3GqbrzIoa-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VjH-DTR6yUIy2EZlEXq9ZwisrCMLAcRUONAgBV_PbrnKq-5njVkJvllEYnfmMhWu7HdcR2D7Qa0PKi5lhgsBR_43kkz8mwdf4L36QmEOTzLTCNh8bJ3YAkRwvEBtwo1GQ0VfEKRewAv4LMwKqrqlHp499HSkBEvBbZ9v-b2PK29876VUtCe7rppyE_hGmDoiLHesspYtgkrFtjW2CKFpEd06o6ZfKLApPMp5WGT67ViWnY2iKXQL_Uy9WV69x4R4ms_obByiy84UJhRfry3YDikc_ZPk4eh_VWehJLdZSulhFS4fLHmJpRsKPBLsmP3adtQtwlkmhbLw2XWwfnPpYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇩🇪
بازیکنای آلمان از بازرسی ها پشماشون ریخته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92676" target="_blank">📅 23:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92675">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qtDVKGiXO5T9nLLmhbPEPKk6Pk9nJuxf7KsGVSmxYMAUESYkLGf5WcOUoP1up5mTTKgGVvj3bSFXFa5TkYDnWm5ZrgURKj3YAo3r_Xtn2rFCyb12Yl2SAnIoXYhuTu4oeMJt_OvH3RtgjlzXVoYdcujwFS61kXJfswjBs34gc0IjrdSCKK2k3LdnY8Qh8rv2uBy0MQz-W29OnU9WqtDyxS_nSCUyIEZluKNLW1DfALj1nNLu226CDga2I3bPFYgHQ1WhVImnzrw-gLFaRIP6pp8WqDhUtQCQnSHZ9rpmEql6pAeZF9IL1ZUBExJU6JH1Udi6A0PqXyShuqL5gV_7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وطن بالاتره یا شوهر؟🫩
وطن
👍🏻
شوهر
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/92675" target="_blank">📅 23:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92673">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WZoI1cfwlycI53kH0WoDiKrQkVmZICp_wCO16rbDMHIfpm6LArgf_ZyD7QfrqBzZW4NIcns4K4b0em86v5Q7BQ85nVpb6luNI8idsErwITCVQYiVIMJafr5l7XRGL9G2BL6biFb2Qk0sAVfzfy8JZ7BkgTzZe1tYK4ZMvOi9Dhm-FjAiDitTY-xuYo238K0RVbfjiySiYw8jtfh-9aW8nF88sbfHEgNIXCjs1IigeUXyR6MpFrVk_6batsydaMQ_63oscAFDrmKANLc5O9-foCa1Ow512Gq39H8Z0wUeVFNaQ5gFUMTgul84nCsdH8pV-DC18uBaQW_SaZ8hUkzprw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XtiVtaRL3CuqZdGxPpdawmz3Sbj_bPGXp7QBlBZsnq0ZgqDGzzdXx1DAJa80mS8AgsFIfUSPBrb54NvwSGp8EQESt_F2GSJHsMDnp84pu0feoqM3yfRxdNCxWGEgqfbDHCepjctL9xCDp5xmrBD_lMQ9aNmQgBBGeli0WHE9m2ufKhXzG6iEYeRTANqcdS4kqwbMARHGSrWL4bU36iy2BDN-KzfiGT7Gl5uGE9chNEKPljalSZirtsiyCfv-FBy3TytpZm09EPtgwQFn43OiXcnwTMuBIODzHMkZBWN_pN3mH7Jq4S5DvpBtGMPAx2_c3zBsl2cHKReVRgxmjpxKJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریس رونالدو لباسا رو کنده تا سواحل آمریکا رو جلا بده
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/92673" target="_blank">📅 23:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92672">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcVr-CdEdYAyfrwfNZ2wvF57ylzKFY_1gBkgL5aqtVeoKiFpnB1RC74pxQYta0Ok-SHyDEBOkG7rTKyHYUIBOtx13eADD5C9Ttwof70z89WQUA-bEvT8fSpyUye99UlSju-n4pGwABEuT_I_I3aDiB4mrGSXCe51fhsylHoSezQkKTWC6VBCE0EE9qlppOn-w2MorEBtIl1v6M7JACxQt8anhImvi8tDW6v7Kl16Q44iVQyOnVXTjoQz__h7EMB_cYa9rlNnJ4gvfBiWHp56IxicNuognQqViiouW-e0LPGGFRfiSPgrXT_nuI3kxbf8w7XwK5LFs8nZVqNOb5uJ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ماتئو مورتو: آلوارو آربلوا در حال مذاکره با فولام برای سرمربیگری این تیم است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/92672" target="_blank">📅 23:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92671">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvuK2f3VBWTGGsl63eR-PKpqb7Nx_8eWY5hgEHKb2jI234HUop6QkQmnVHAJYnTB2o2j90na5pTyEU6Jgt07vGVHrV_iSNgDkCop5Yy25ZqvZqMZc4Yus33ap3lpZGJ0bGF-3X5Uf2YwqrT5mT88arJGSserHCs8-2QZQinzsfFHj6v3nYao1Biz_XlT3F4uyyCHx-iWEBx7OXRfZQsxaNC30VNdBPMuRC2gNvjsCZ-LVU9fz4ogilz6RUFmOzryBAjysxPk7ICj_Sdf7QnmW769h3h3So8mPvXyXDhY7nbABtr-2zGG4hr4ghAVLynoA_eHa_v1lTGAUDlF4gBabw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
این توپو بازیکنای سوئیس گل نکردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/92671" target="_blank">📅 23:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92670">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNVrW3BzcwWYKcXrFOSlzsYqD_xlwF5u2ltQFJ0heBJHlEDrH7EsOdjnY6dFv__JYA1ImjILeuCQZcG4xfVdXl8lvbFft8G7eppTMNucTqaB6GhCIvcxXe-Dkokxrbd3eeorZg9lVDUGbyYw4BK4uzc0rC594dKIOsVmkgtxCp8OMM8DUYNnWWUIoHFVnhIGBthdk56KZfQz5E9PamKvHGwnXn8mJsVseJqXqhKEnV-ODJGlyTcQMKy1uuaUsk73mJS3KQreAO5bogN2I3iNrro-0ocDJ09m3kRFlU6_23WJYHidZ3je5q2Lg870QQZDcf4IKD1iG4CWW7Ws8a3n7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماتون بریزه
دروازبان قطر ۵ تا توپ رو سیو کرد و تو ۴۵ دقیقه نمره ۷.۷ گرفت
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/92670" target="_blank">📅 23:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92669">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پایان نیمه اول
⬛️
🇶🇦
0️⃣
🏆
1️⃣
🇨🇭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/92669" target="_blank">📅 23:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92668">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">واااااای چیووو نزدددد سوئیس</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/92668" target="_blank">📅 23:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92666">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">چه سوپر سیوی داشت گلر سوئیس</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/92666" target="_blank">📅 23:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92665">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gueaukzKjw9CHlF7AD2fTXzkD9BqrnuaGMIqn_OV0znYaf6_Jh9O-qF_OoqMBxm2DoBXPrjSFrgfhPUhRQrcTUkax39xakcWg_6D7QscjyhDW8bJB2z59Yfe8p-XKrFDLkRxlVKRgKrWUkk-CQmRgesAXVGfZZYP12LVNTV-mp8jUc0g_1AiObnQP5k1SQZVim8n80-q6_HE3J8wS4WHWi5Rknqi0e4NMq9yxi1ocXvWDgmkbIRlkDv7gENt55jfDU_n1wOCGWjgCmkNOQFAcg_8XM_LOkwXwHgbaGj1cJScrx6y6itAeU3Puqy6zp7JlpFH0MSbhh0YmHfamoEi9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گل‌های امبولو در چهار تورنمنت بزرگ اخیر:
⚽️
یورو 2020
⚽️
⚽️
جام جهانی 2022
⚽️
⚽️
یورو 2024
⚽️
جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/92665" target="_blank">📅 23:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92664">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04f957d097.mp4?token=mJ8Uks_yHUfaQvI-CSwai69xV3JCSB5-9guu1CJFtD5LkO280mRH2bo6g_wa_w69x4M6i9nLiVblOuQW-gF3X4R_epQ4Eo2n6laoM_8HVpgxpCmJLfIKFkKwuA9EV4NV4Rrq-hhHlHCkYzdPmnDM7rcLZ6rlmNu8B_2zn7OHX8HYhqieSUi0kl2OaGvy8lLYbzoLfunVSAKUYhhD19bwY6ytND__K95ivX9QFf2xOvVZ_cnnEQd4y4QdxvOcHEiko6ll7I4AYc_OPZSoU0opVUlrzCWpcLzJpiVuf1lC2t7yeYlyLoxcIAgfgZOBjF921NDSEewD1Otd9BVSBK5Y3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04f957d097.mp4?token=mJ8Uks_yHUfaQvI-CSwai69xV3JCSB5-9guu1CJFtD5LkO280mRH2bo6g_wa_w69x4M6i9nLiVblOuQW-gF3X4R_epQ4Eo2n6laoM_8HVpgxpCmJLfIKFkKwuA9EV4NV4Rrq-hhHlHCkYzdPmnDM7rcLZ6rlmNu8B_2zn7OHX8HYhqieSUi0kl2OaGvy8lLYbzoLfunVSAKUYhhD19bwY6ytND__K95ivX9QFf2xOvVZ_cnnEQd4y4QdxvOcHEiko6ll7I4AYc_OPZSoU0opVUlrzCWpcLzJpiVuf1lC2t7yeYlyLoxcIAgfgZOBjF921NDSEewD1Otd9BVSBK5Y3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇨🇭
گل‌اول سوئیس به قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/92664" target="_blank">📅 23:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92662">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پنالتی برای سوئیس</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/92662" target="_blank">📅 22:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92661">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پنالتی برای سوئیس</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/92661" target="_blank">📅 22:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92660">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سوئیس نزدیک بود بزنه که گلر قطر واکنش نشون داد</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/92660" target="_blank">📅 22:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92659">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بازی قطر و سوئیس شروع شد</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/92659" target="_blank">📅 22:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92658">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tvq5HV-glAO4KWocW0R65d7aPBsRBN-S8gTO4Cbg7D84pcGaHfCe4z606LruRdzhLcTQfU2zbpoiHpXQt3OIjEJcEsGA7OKybFeOan7374XVNxJvNi4T7GGn7Z--nU3_FL7ZdPiWcatXu4DGXyRLP-25h3SQyddAdluuxOYMgXC0XCiFiVhfZEkJKzm-ax1XW-yM1t1zYHjXrQjEic5k2dUnOr8GuFUzX2ZpYz1LQmX_189cXcM6bmJjhPfpzuuOWDjAREU-Qqvgsw38o45OomCfkuG5jrCIoGHncvkY0__j_24fKEyAdf6AJs2MENC5qXHWxa7xA5fFkOUOks8kNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🔺
توییت جدید نیمار در توییتر؛ امشب قراره بازی کنه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/92658" target="_blank">📅 22:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92657">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnKjRNIfyvcwx93wEr0z0mSKjpKjAJb-e-6PjcBEUO_p4p6iIGEMQN0VuLUhlc0cnmRqJ7xOHQHB6uNrhN3YWHUtcozM37sjQ1j9g-QqBUp_tkBD6Jd3adIQHImrshsArAgDRZo3DAMl1A9rDt7FGoQjIh9droq91_rW5EIPiMDlGSV0mJ5V4CyK0E6fnUP164jNGAB951Bb9RS5gY_vOj5RH8CdoKLUifwy-00HDlq5u0lTYz-v8NJp_DrnAg7RUvDfosNAIQPUFi3Z-dC5jrC1hKTtUaI_hhnf_jhqDJqrm94qd0VkEhtUjb6Rgk_yRsPQFAirSBmHuJ-ePWefUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
📊
🏆
براساس نظرسنجی‌ها از تماشاگران، رضایت مردم از میزبانی آمریکا به نسبت کانادا و مکزیک در مقام بالاتری قرار داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/92657" target="_blank">📅 22:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92656">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90512a635.mp4?token=KkYYcfo9ORkjSk8duxlVuhM7CizLXE2g3YiEqj9fGRKITgj-z5-tIjqrM6RGKOQHuPHSB5UJOtA1ABLqBsquA03r4zIO7_swvRJtlJFOUlij4oEyoYH1ocNYmgy4rdv_-Jhu6JWi0GYMD9RPXSQoVO_OdzkrbivwPHKjAVf3x3QiNC8tLrltnaXcR4DGweFSI7-HXa4INjMJPZJHwL_7MaAN9siLyE-s8YTEmfhHu11r3EAZT6X3jiBnx7wSPibH7FTaz9IKOuphwghGmJTwtLBz_5HZNOI6lkOELprjhgSaoUp6wYj9I6WpQhy-OmV8UW61yc0JIyi3r8ycAziesw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90512a635.mp4?token=KkYYcfo9ORkjSk8duxlVuhM7CizLXE2g3YiEqj9fGRKITgj-z5-tIjqrM6RGKOQHuPHSB5UJOtA1ABLqBsquA03r4zIO7_swvRJtlJFOUlij4oEyoYH1ocNYmgy4rdv_-Jhu6JWi0GYMD9RPXSQoVO_OdzkrbivwPHKjAVf3x3QiNC8tLrltnaXcR4DGweFSI7-HXa4INjMJPZJHwL_7MaAN9siLyE-s8YTEmfhHu11r3EAZT6X3jiBnx7wSPibH7FTaz9IKOuphwghGmJTwtLBz_5HZNOI6lkOELprjhgSaoUp6wYj9I6WpQhy-OmV8UW61yc0JIyi3r8ycAziesw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
🏆
مراکشی‌ها در آستانه بازی امشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/92656" target="_blank">📅 22:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92655">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pN00bfxvSb9hMqZors80Ldlgh9VCZdwu3l4EsD7DZTSdlviqvb6FijxwNlsj1Y8UHeptf0t8J8x49Lb2bLOLcAgPlWmLYl1nh7kUGkQhRtqAnj7-Idduc0prJrFqLkc8499NhTaRQBLWCioXqdn3Iggmi0h0-i1tk31tnW54sasFWgGdOVAk2MPtfJWFfjrNYmmIgNssoNA5acFr4KhiW1iHgMbQ2nSuRJaokV4Fn6DPvCCiMGa6RK6zB2kD1FYnKySdA4jslNTSrA8RdxD_7zhwHVzHM3cViIJpyWDhXD7wphu_pvuc0encgXU5aRflNoq0vKhDY4VCjEufiBw1kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوووووووری
؛ رومانو: روبن‌آموریم گزینه اصلی هدایت فصل‌بعدی میلانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/92655" target="_blank">📅 21:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92654">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1__dzuJaOgAridJqcSCLe36Dic4F9ZKNmazUXQVrlAdrh3Sq48rqKgn51Q4RbAdhpBzLAUHMk9yQkC0JcsY2pIOpHcZ5ixyc6D6P8E65QnRXohG7YWi8JHd9TZzO-EvwTPFk8AuaZapHeR8ioV-e36teK5FGtNNTKBYcRiZxoE7DBIare7H-7LKysp6YVEil39BSTziSwVC-gMlDeTiRk7LF_qdYuvq9hhn4IQpCZ09J-I3oSJsij9SwR3j9eKJebkrPaa4m80-xCLJhOmg5dt3f4N6y5T5aAX9YZHI-1xoK3MpbouxSUQqSgB8grtW4pLdKVULtq6jXCiLYoZCfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇲🇦
اعلام‌ترکیب‌مراکش‌مقابل‌برزیل
؛ ساعت 01:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/92654" target="_blank">📅 21:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92653">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhtGtpXGPoJRkIx7zKeTPndQhneRTCDTpEFDVseL4JS-x4gdGXpH8i8pwQ1dlqRcgT3AeqoPUP6jWLCE30Z-OcgQZ6hfE6-VCphlqvfrWc-H2Hj505X5cdLUH5I9TESyCKQZAlXhL8790kvuG9KxcnT87RubpcjQAmqZbDFHvRCvIAuIAeJGfqUkZP-0oA7jM5g1WdYeNEXmTcLu8gclMkKBEFWmbnymZ6hRodl5BVmLG_yG2yJ_9kIjA_IdmQFcbi2fmg1F6l7dhl_vcaP2Q3MnnjTyxu-VYvWGuxlu6P2hcD6pDGY-1oN7tqEZc9X-rQCDkPecVyPUpNV-zDrbTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👀
🇳🇱
فرنکی‌دی‌یونگ
: ‏
🗣️
هیچ تیمی از بازی مقابل تیم هلند در جام جهانی لذت نخواهد برد. ‏ما سرعت‌های بالا، توان بدنی و قد بلندی داریم و همچنین در مالکیت توپ و حملات سریع و خطرناک تخصص داریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/92653" target="_blank">📅 21:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92652">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/028f0149ec.mp4?token=hWUxM84eHgfNJxIkQSVIYtDAXirsAqHgy6rjaRmnpDql-FZ8TRsClKOxDDbaNp6yvQFob1jgkz2Uu5pqA0vlu0mSiENFVjM1YVgiUiYojG8OmCZtP0DhN9PYmd8gL_--JTrpLCSWt90HjkHkTCzGfR43XRVItDjxg2BU8bnBVTeFJqEtZ2SMV9WYDdQeXnu3UjlKjL4oJ5_3LazZLQ0zM4O0hrLR6Qff1viww0J4bfOJCzgWDY5_dUpyK2v0rEPNyJmv8oeRyeTj3fcsN2LIS3MhBKzq7s3ufTrWlOyiSjg3OyS2EqXPDJgIcB-mahBt2nqWhI_rULBaKIgtOJCScw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/028f0149ec.mp4?token=hWUxM84eHgfNJxIkQSVIYtDAXirsAqHgy6rjaRmnpDql-FZ8TRsClKOxDDbaNp6yvQFob1jgkz2Uu5pqA0vlu0mSiENFVjM1YVgiUiYojG8OmCZtP0DhN9PYmd8gL_--JTrpLCSWt90HjkHkTCzGfR43XRVItDjxg2BU8bnBVTeFJqEtZ2SMV9WYDdQeXnu3UjlKjL4oJ5_3LazZLQ0zM4O0hrLR6Qff1viww0J4bfOJCzgWDY5_dUpyK2v0rEPNyJmv8oeRyeTj3fcsN2LIS3MhBKzq7s3ufTrWlOyiSjg3OyS2EqXPDJgIcB-mahBt2nqWhI_rULBaKIgtOJCScw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نظر پیروز قربانی برای برخورد مجدد احتمالی ایران و آمریکا تو جام جهانی به همدیگه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/92652" target="_blank">📅 21:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92650">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0i1bk1tu7cAnAKLeDUtwoECwf_A5CRXWcJhnCh-JYFIE1AIYiaVs2akDbLxIfdEqFHOlRv6zHKneufS7vjdMHjcXz-FZLi4P9O38pd9_KD69rjhF44P84iJC4_qalsQEIQtwgCkEIqNIOi_vLj-2rF0sZoHO6nA1sUDhI9o66k0-VDeLvwAAw3jSOuH9EX00Yd2Ayr-2STNJmyN4pBoCFQF_mPJOXJuRrqPnCrZK_PhK4E7n5ncE82PHepmJU7C9IJA-Aud5cJXeifBWTi5RgPVCrJJRLMtWZSp-Ct5ylEQeLLVnvRHIM7bQAEe8eo6KQuEKp9_mo9ISana_Z9HgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
پست جدید ترامپ کنار رهبر کره شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/92650" target="_blank">📅 21:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92649">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VifODHDDDC0gpE5JkqaV0C462vobRtfVogMZT_B3VjM4njoAht261eF1HnbswYGGMJOSnrRgpz20WSJOPCX2kOxy4Iq-S1thFvtC3TQCOGTgCl8NB_m9aPW1RN6DXUqxsNweqeuDo-JnG7drC713KYqL9mHd_AL3VwUCn2jcfqmkAohUrLIAZdCM8FV8w1Qvke0xsI2042_3C29fNmo2M8xzbVxPHCwKrVZPCiDky2z1U1rPTiJ7sAUwfSmtWSb-cse0VA3r9Typ4X1GqdstBf-M43pp-cKe7sEvHjRCVcXY7e1-4cToleK8f_MXygOBnYaNUNIvd5Q_iJZymn0K2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هر پیش‌بینی دقیق = شارژ کیف پول
در لیگ پیش‌بینی «همراه من»، برنده فقط خوش‌شانس‌ها نیستند؛ هر پیش‌بینی دقیق، بدون قرعه‌کشی جایزه دارد.
«پیش‌بینی دقیق» یعنی درست نتیجه بازی (برد، باخت یا مساوی) به همراه تعداد گل‌های هر دو تیم ثبت شده باشد.
۳۴ روز هیجان، ۳۴ میلیارد تومان جایزه! هر روز یک میلیارد تومان جایزه نقدی بین برندگان پیش‌بینی‌های درست همان روز تقسیم می‌شود.
💳
سهم هر مسابقه نیز مستقیما به کیف پول همراه اول پیش‌بینی‌کنندگان دقیق آن بازی واریز خواهد شد.
@mcinews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/92649" target="_blank">📅 21:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92648">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIICFmv1acV5St677KtpiFTKdcr2jmU9BbjxbwWRtnTpYNuHLXs7DtTP6ThUsfAAacyNatH5msOjsaVUcldC0zGmvgM_8oFf1Ex3QtgRlzGGopSvxAu5O_7lbfPuNGGcbJJ2W1NsSiKBKub4ojENZP4W76GV0aetuLRnO8WcI7w896S9LAm-cSpZfGdP2GHV6Me5Jim7GliTqiheqA3bTJ_I7k9B5MsVghlwG048gbB2qZEeknAiU7KJMzEUlcENVVCdIalQvsgAd90FxlEf7_L87_Md1a0LZ7Udhd0Pz2T450_8B5csT9c3yop7LdbOQbKgQxoCN_kk_HCc4CAW-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکیپ : دولت آرژانتین فهرستی از 13000 پدر آرژانتینی که نفقه بچه هاشون رو پرداخت نکردن رو به ایالات متحده ارائه داده تا اجازه حضور در ورزشگاه رو به اون‌ها ندن و فقط در صورت تسویه میتونن به آمریکا سفر کنن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/92648" target="_blank">📅 21:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92647">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwylTuYgLru0PYIrS9mFA8Ua3_SfuJePi3mVpusLvUXoWt-s7u554WasuN00iYXS01wzKBB9EpVV2icGjvWTrnbJv6AtuP5flph8oEsh-vYfezKUpwzRoO7pMPzeQgTloB-0kcIakSxuRf5qYXwTexTvaIgkL-3yxOPgPPt8EXk-vYw-DIydNML18U1-RTgVrXM7P14OssczJO2BPh8-i1QpMAB5JEwYcGGYrkYVmtK3kPqD115D3lqVaXV6TviQqr640bbTcNiX_Xd-Ul0NA4RNms0uh5u27UXadpDzNUSx1gnLPBQDBG9bcsBaRH9hOLXKEjSQq1f2WAgskPGKxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇧🇷
🇲🇦
نمایی زیبا و دیدنی از استادیوم مت‌لایف محل بازی امشب برزیل و مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/92647" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92646">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uP1SbAhbHd6WpQfXB5yRyNVDO4WfhOJGV4TFZflmGM8c9jJdbL0umUzIJ1VkJrJ3Sa0qltXBbRZH7Ywbh9TDg3k8DQ9A53wEEoHVmMzG79HFWXmWuS9WRzt98sdj9HXCKxFtSf8HCDGMKOJd7zhOZSuQEu-tiLP9OPaYywgQoTHhT3s3nNtfUjB05S46kaxcui7bdCDKJV5iMgaxW4p2V4ec2JgmI13fOx4CrOB-G8Q1eEXv-uXtdj-_cPjhz31VAojrI6NlJiAHV0zAqDcS55loFkELosmqIviq_wwAXHnSwSq7_UlF5JhpLcOrdoEYxNNI2WYTqVSvWNgAEBfrgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت طلا، دلار و سکه پس از توییت ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/92646" target="_blank">📅 21:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92644">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mrTwKFF4cLXVBD8VXkXVlSv1buvjRgvJIulKTrGZDJjKYzCexeGLXU3MxbAN_coERvHQN9Ox16iT0-3o251-Dhv1nhoDJ2xWKKFd-TxwK79oyIH1US_O_m8ELD2_DqNcaR_dXR_jrKIsbqrlSLKuZvouSFct49XGhjTpdhMpf8Agp8eH58i0g4W0pieMP-UYIJ9Wz5KkTInQ0EVdRigdAaEhL8A0qVoqPwx94UiBcfZJfSEl5PkNKC-9WOn48PK2tc6PKjy1kn-pIPCBv_oiK59dhRDQLgbnwnF033ekWdChYfKiV1qMBrjFIK9u2y6mBOvlsap4CwKMOmFLR5BVaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sim3wS4O6VN4VYjWEBejLd5EmDwK58aFcmaFq39Xsv3ZTOci2iU6LFS7I3_zMoqF3nvtdEWpu-PgeazkHu-VMK4viFmrEDsC81p9pmemzqxk5nahYKO87q5M6kY-rADnbKnbNQz_vxTkmkszXbK-3O4Qgy4HDJIXbU1JstV79xi5F8Ream30H1ks5Wjl4lDFwCozrm7m4MqB9q2Gv46oreXWKbzjNpTerhqdI7y5Oy3BhxhqImlcl4Fw2ABFB9_KRmDLzKiE3UlesUbSXElE6ogn0zCyBGMWRzkQ9WBEb_MnuaWaoXTgSCDcQzIQpQ2E87eJm0n4A4L0OcHdYAgwIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🏆
🇶🇦
🇨🇭
ترکیب قطر و سوئیس مقابل هم؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/92644" target="_blank">📅 21:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92643">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKIUqxQwiwudx-1-SU89wpnB1TMMIl60Sf4H-CKbwfAh4lwH96_kIYL0awjI6_t4TrrC9Ikg0g2pQ1quSuhU3M8WaWg2ULVG5krIWpU8bJt74GtxsVtDZU7ugP9xpOHdVhUgL9Cw98FA2K_ZZccFegRY17-CM1otsFWtcWuZ78VYvzJPnNp6VPuDb8ggOOJO1M92QPlyKY9mNFZXY1Cm5Wv7O9Dn8uEPHL-vVVxbAwTC4FN3LfZGEefbE0bPFOMOvuV0bd9pPbnHhyT0GtdiO6KFv-7xb2sJPi6jGxHU9Ub-qAHrc4BXEhLtAxnYU_gM8exiGTmSPxKDi_bFdIZztg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
به گفته‌منابع برزیلی، نیمار در بازی بامداد فردا مقابل مراکش برای حفظ روحیه هم تیم‌های خودش روی نیمکت قرار میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/92643" target="_blank">📅 21:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92642">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLMGQi7JIGqyv85EaVmDZpxCedgCKbquXMWn2mIy2qDth7kcaz0JLDuaOOzs10Yu1qLpPmEFbPivpFh7JU1CVjwtJuPe1YY6Wxj_rIsN433zJ2N9WVh_rEdZHgVnc8QF6Eky_G4fdJsH8MTif2WzN76Z56p2FTWKzrq9cvnuwQ9fWIfSNp_Ox488wZxYAD-UxlBqLqqG5JMra3-3-SZBdPr3OGxuXVNlpbK3rb_9NMBhYap0pIwEbUWUxVDCeM1vFQL1JneYjfmvTlbu-D1LOD0IVAd2mC6dZUYfy4io8sFFQGIAx7rBvm_PMAiZSuR9WJwfA0UzGKchizZVGkqgRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هلند
🇳🇱
-
🇯🇵
ژاپن
🏆
جام جهانی ۲۰۲۶ - گروه F
⏰
یکشنبه ساعت ۲۳:۳۰
🏟
ورزشگاه دالاس (ای تی اند تی)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
🚑
بازیکنان مصدوم:
یورین تیمبر
از هلند و
واتارو اندو
از ژاپن به علت مصدومیت در این دیدار غایب هستند.
👨‍⚖️
حقایق داور:
🟨
میانگین کارت زرد:
۳.۸۵
کارت در هر بازی
🟥
میانگین کارت قرمز:
۰.۲۶
کارت در هر بازی
🧠
نه گفتن بخش مهمی از استراتژی است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/92642" target="_blank">📅 21:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92639">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtdAEgO4nSM_JSBgj-BpJDQDBgJcgUJuQFzyfMiI6Jjt-8qry7hOO7wbU-2ilDU2RSA0IxhKaHX0n0vqNKO2gJsp2EreSOG4E54pBi7G2mq4NaBMvmDgoH7cz4QdXVk57Agp9oEHtIC_ftcOwoZEDxdxDYu0Is0HzEdY5icVIXRpjVW2fdLnaZwXjLgPZ5RICNXtmOJzb3AEPXqGtq_9CPhxvN6sYi8khlME29mciCqzS9oivi-RlO_MCGs-aXuyTtY6Z1QMj6EhEh3SJEum0q920KX2LTiXVgNXofN2VxreGZn49RIsv6QoTPkJzmvXu84Ol9yYeWVBPDWQ_SfDjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخت‌ترین روز زندگی بارسایی ها اگه این اتفاق بیفته
😊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/92639" target="_blank">📅 20:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92638">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jh9x9mb9zfuHhlLNOqqBAtMuhI5gbYfrwcLVaAVZqWcqLM2tV-0Lo4HaXwKEOtuGzOnsTZNP-tEWhWExretTQj9OWcnPI_Zw5pXy5JWhXVywEHzf5yuxuxMeodZabMr3_ZMcnqt_Z1so475JSdOF7m6hLqX1JClqbIU6S2_nmuJMvej2HiQLK0c9eIfFNxEkbgQrra-jLZ1Mwt-z54JAeSrCSpK0Hio98cQNZeW2kDhty50QU1yTPqf7iD-0xD4UhEg2bOQ2V9m9MRXJcBgRW0GLfwc9GJGbhj48BFGk2quYBW-mk4pRoQZhVyz6chhvolEHUBf9fhvPyM3n3JSU9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر قلعه نویی برای صعود به جام جهانی ۱۳۶ فاکینگ میلیارد پاداش گرفته از فدراسیون
😳
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/92638" target="_blank">📅 20:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92637">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XX6AuztlkQ5XqluwUstg25SKijUwvKc3yEARndSHEaf8wx7qYZRCaXO_B8pIebDqoAhfHjtUvac8EyRlbtm9hBsPeLWnYzvU8RBMj4fP22c6c8jv7H5vmUIf0iX8r4Xb0iVMPwphRHtiqf2_EsfysMyavkV-YxIA0RsOI8J4SrwPpx8xQoYM_Nm3laO39o-2JL5hDdOgBWr8LZsNJCmpt6RboP-v-MPfRy9cwQoO00Xn-otKyq0CFvKZnIBcz0eBbz8TYPWg8wrLVOc6s29ABjAXQ0oBmi9jMcU1EOXa0UsbAJj8zH8O-ToXPnjk0ASgyjuKDTxAmD6O4DR8qcMubA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇶🇦
🇨🇭
نمایی از ورزشگاه سان‌فرانسیسکو ساعاتی‌قبل از برگزاری دیدار قطر و سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/92637" target="_blank">📅 20:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92636">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
🚨
♨️
با اعلام ترامپ، توافق جمهوری اسلامی و آمریکا فردا در پاکستان امضا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/92636" target="_blank">📅 20:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92635">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H1Ga7N2ELdEovr9-_q-K1djhegLfBqvOYDzVzh3Cid7DXuphr1dV01GK8GqM72dgn91MMVE2LiALVM-swr-GdCwBXnFM1FhHQwbsQBLjWKQoukW9EuZn-xZ3BAWrPOd6AKcRzkOpNgzJenPlAiYm4VeQ8f-qUYZ6-8NdlOaU9fs5z7LOsI6DDGIlSNef7gtDdlnpTTBmdOeWdQb0rJ7H3kN-jxdFvPKlKCoy6FGJgO6G2m4Mk7n_VkQvMAhQu8XGs9VcvmtZSakdohcQizmp_DanZkSYFEmUsYHLRXGMxi-_bT9dRBC4Buil_IY6-aYF72vRRgeLpnmLKrYuYdcGwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
به گفته‌منابع برزیلی، نیمار در بازی بامداد فردا مقابل مراکش برای حفظ روحیه هم تیم‌های خودش روی نیمکت قرار میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/92635" target="_blank">📅 20:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92634">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🚨
♨️
با اعلام ترامپ، توافق جمهوری اسلامی و آمریکا فردا در پاکستان امضا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/92634" target="_blank">📅 20:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92633">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14d347ca72.mp4?token=STguFEELq-KbH7sqRkmzv8ZyqZWaRWtLrMOa2m2mYMxAYdZ1VVodaLeZc8j8cWz2UQ3vCiNty_3dQ-n6NdRw3jd6rXpWPJw_xunOr2rG5CWlJ5yHI_ainsUKi0cq_F2M3q6M-_VyIOMa8RrLrtgRx5607ImlNIlgtKxSeoAUrvcJq0Fkot5KFgHNXnZ6JQ2iOSxII51kaJtqjYdXKwFFliX7zHUJNP2UTZOitnLpSRNm9wjLSOakaJlP1UwM2IbxFkUhUAI9LpJT3_negixyef6hBVVjJbxdN-ny1e16CXyJvzELVQUbq2XdiGmuDIllzU-W16Fatvm5RyZEiUEaGjWrwFjFe02PBA1RPlXwShjMX8ONLAc8QaVuy-9OM1fhPHJmXw5b5oFq9a9Kkt5FmZsAkXgz5hNwY4PGPE_6bl0hIO_ix5KVQrkGvc6IvBOfzbKImG_BMjkO9isQKm5iBewDGdGn-doO5o5Sa92HChPq3RHTMdOfWEQeIkQKn9bCAVzTOP2ZSOWCEcLEtcYDwBWLZlIXfFeIjdWmFzsEYC9HibQPL4aA301a1e387EhF90lY_WAnlQah4sXoIi99sNjF4FPMs8yBcOTShlbrZ_eI2V_o4_5eL1mA--TE3WhxJuhKRt9J1iEkPFDfSkLkHqMx-W8Dt7rM9-k47pcUgTs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14d347ca72.mp4?token=STguFEELq-KbH7sqRkmzv8ZyqZWaRWtLrMOa2m2mYMxAYdZ1VVodaLeZc8j8cWz2UQ3vCiNty_3dQ-n6NdRw3jd6rXpWPJw_xunOr2rG5CWlJ5yHI_ainsUKi0cq_F2M3q6M-_VyIOMa8RrLrtgRx5607ImlNIlgtKxSeoAUrvcJq0Fkot5KFgHNXnZ6JQ2iOSxII51kaJtqjYdXKwFFliX7zHUJNP2UTZOitnLpSRNm9wjLSOakaJlP1UwM2IbxFkUhUAI9LpJT3_negixyef6hBVVjJbxdN-ny1e16CXyJvzELVQUbq2XdiGmuDIllzU-W16Fatvm5RyZEiUEaGjWrwFjFe02PBA1RPlXwShjMX8ONLAc8QaVuy-9OM1fhPHJmXw5b5oFq9a9Kkt5FmZsAkXgz5hNwY4PGPE_6bl0hIO_ix5KVQrkGvc6IvBOfzbKImG_BMjkO9isQKm5iBewDGdGn-doO5o5Sa92HChPq3RHTMdOfWEQeIkQKn9bCAVzTOP2ZSOWCEcLEtcYDwBWLZlIXfFeIjdWmFzsEYC9HibQPL4aA301a1e387EhF90lY_WAnlQah4sXoIi99sNjF4FPMs8yBcOTShlbrZ_eI2V_o4_5eL1mA--TE3WhxJuhKRt9J1iEkPFDfSkLkHqMx-W8Dt7rM9-k47pcUgTs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇲🇽
هوادار مکزیکی که برا ورود به ورزشگاه رو سینه‌هاش پرچم کشورشو میکشه
😈
😈
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/92633" target="_blank">📅 20:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92632">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkEasbVF_xpMT8-MrBRsU6BEyQacmU8P6D-UD4-4y9lk2ZfXEQCHI2i7r3_-Vp7uRyoMSEndARlDzh-T1knizRhS89i231xgbVW95vPt5l3142oSDrb40DD6hw9cdZAkhA4QticdKnd3YlJJMHWqLgdNcH65cd4LAgyi5Sg0gEEli6IyVNmmmJ_Y2rbNJsucj7zTNu6GXEWtUcOgDn0Ks0LOK8vJ8-E2y_R6v6Jh12k2xFzuWhLX64SMNZN0vESn5Uj83EeZJz5JU9MjkPWObO3UL1aj0-WRaJztF-K0EwUd1SZBS29zx7-DAwKGHzZliky2tSXOSETk5CX3KCWQtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇩🇪
🇪🇸
🌪️
شرکت آدیداس برای بازیکنان تیم ملی آلمان و اسپانیا جلیقه‌های خنک‌کننده ویژه‌ای مجهز به فن‌هایی که مه آب سرد پخش می‌کنند، فراهم کرده است. همچنین کادر پزشکی و امدادگران در زمین تمرین به طور کامل آماده‌باش هستند تا در صورت بروز هرگونه وضعیت اضطراری ناشی از گرمای شدید، اقدام کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/92632" target="_blank">📅 20:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92630">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eX6sgEEaywc7KqxTuJMPK62uTfIgGvFcQQkGI2bMep5X_Tt7IwMMNHOup_e8hRcvDNpM8uKgN5ICTWM1bYGTo6kK6CfWyL6nxbap0dgUa8EI6eedSsb5Zb_totL8cC2EjUcgNHXLG44OpaXEfhR4vxy76lytQT516g5SGAkk_IHSL84NRA0LWxlDA2osAU_AbEeX7iStDTB7mpacCeiEM4yNZUE285HM6kRfB-0AOmflMDIyRZ6B4envlncbjcCmq_qr6CRBC3eyszwPmfoepgvtXdEcIezWz8q29typl4CRw5Q_FuHnnq3qkguwpsnD8DRuFVh3brSNHkYvo2bavg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووری
؛ رومانو: لوکا مودریچ از تصمیم بازنشستگی صرف نظر کرده و اگر شرایط مناسب باشه دوست داره به فصل دیگه در میلان ادامه بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/92630" target="_blank">📅 20:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92629">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2a7ddedc51.mp4?token=fVZntnMWdbAlU9xnlLz2ZIIf3GHS-IY3PftvTU5_veHmG5KYjv0riJJM7QEvFv8qnokv7CBeiNI2pyanS0R2dzQYL28lwMhbEkdDzW_vqRdMNT4eviosGWP4_AJYeXylK9E4x1PBl0TVjESn7zCoU4qiuVvCfSiSo8yPUcdr3eQpt8K-i2nt9p07jQlXQwLQ__aG4r3TmjGPmZnIPqX-XX91LN1SKc8AqsJdsYans_oFAW5b0dj3iC8qM7KnPC2AJiSSI0Q7in3X7h5M1XCXeE3wPN_aAVi4TrYp6DwegLNKeQmZu5oeRhU_PiOUQTlXciaFEHss7mUo7HezsROI9AQgyhQ78fc7SJKXAPRB8_yGJxacNLZbJvzP4R0TyAftnnqv3lnr21upJrOc6SZqOJy7Thwt28Wvu9IxLPmp_qUDyym8S-jRFtD-xKIzVDXYqAxXguPP3GB65vSU9N37ywCBYRJsHbt7FRctsIUR8ONbeP-reVCH9e4EkKcfrviHpNO26mm7w2cpc0JDr75fAwbGoXKfzGXBZLgbdDp1vYUsmFc4qXjelGafrnBToAt0KseIZVSJi5DHIMnNLGeNTFsLRdP2tKnj6z-iA6Zkz0RbHOGjdzqB1UvNx8FjISli-XONK-K6zFJ2fh-kHCt7eKdriyaG3RGO5QvhAKGLOM8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2a7ddedc51.mp4?token=fVZntnMWdbAlU9xnlLz2ZIIf3GHS-IY3PftvTU5_veHmG5KYjv0riJJM7QEvFv8qnokv7CBeiNI2pyanS0R2dzQYL28lwMhbEkdDzW_vqRdMNT4eviosGWP4_AJYeXylK9E4x1PBl0TVjESn7zCoU4qiuVvCfSiSo8yPUcdr3eQpt8K-i2nt9p07jQlXQwLQ__aG4r3TmjGPmZnIPqX-XX91LN1SKc8AqsJdsYans_oFAW5b0dj3iC8qM7KnPC2AJiSSI0Q7in3X7h5M1XCXeE3wPN_aAVi4TrYp6DwegLNKeQmZu5oeRhU_PiOUQTlXciaFEHss7mUo7HezsROI9AQgyhQ78fc7SJKXAPRB8_yGJxacNLZbJvzP4R0TyAftnnqv3lnr21upJrOc6SZqOJy7Thwt28Wvu9IxLPmp_qUDyym8S-jRFtD-xKIzVDXYqAxXguPP3GB65vSU9N37ywCBYRJsHbt7FRctsIUR8ONbeP-reVCH9e4EkKcfrviHpNO26mm7w2cpc0JDr75fAwbGoXKfzGXBZLgbdDp1vYUsmFc4qXjelGafrnBToAt0KseIZVSJi5DHIMnNLGeNTFsLRdP2tKnj6z-iA6Zkz0RbHOGjdzqB1UvNx8FjISli-XONK-K6zFJ2fh-kHCt7eKdriyaG3RGO5QvhAKGLOM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
انتقاد شدید و عجیب
نبویان
: من خیلی ناراحتم این چیزی نبود که رهبر پیشین گفت. پیش‌نویس توافق بازتاب خواسته‌های آمریکا است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/92629" target="_blank">📅 20:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92628">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhTH6Y2xzHmx9tm20QfhmVeInZL_K8Nc2KSByNiiqINsewmEGqtVi_w0Q9Hy-iFNCXlYSRC8r_prKn6t_Y8faLTQoqMZvfgS-pCN0S5gDoMSiGAU6-fnvn1giHp_SFlNY2_fsC2HBEczk-R16shnIIomkB_cLUf-iAvhWIAasPAuqzueU2KUYKwePrcwIK_dkpnjeI-f3jDvkkGDdqaihW705_SwYlMnKWTlypWJa-DNi7BrhZCyq_Ju0pBGFruviYPreHxWnrRSiu6d8gQuxtKGoLzsl2RzL1ygdE5NPFh6-uZQ9XYe7ePoQHj8XL4Ocl5V9TAIYgD3ARtcFuJvSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
ویژه جام جهانی ۲۰۲۶
هیجان بزرگ‌ترین تورنمنت فوتبال دنیا فقط داخل زمین نیست… بیرون زمین هم جریان داره
⚽
به مناسبت جام جهانی ۲۰۲۶، یک پیشنهاد ویژه برای همراهان فعال در نظر گرفته شده:
📌
از ۲۱ خرداد تا ۲۸ تیر
📌
هر روز ۲۶٪ بونوس روی بالاترین واریزی روزانه
یعنی در تمام مدت جام جهانی، هر روز می‌تونی با یک شرط کاملا رایگان  وارد فضای پیش‌بینی و هیجان مسابقات بشی
🔥
🌍
از روز شروع بازی ها  تا فینال
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/92628" target="_blank">📅 20:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92623">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DIsrwLPMntSMhY5MxRMHDMLB_JdSUb-_KLv5gaq3-G8VOMYcyVaDZKHrH6Koh2JKB-2hCYR7cADETCbPvCeW3-r_lisB6ybELU2NykMa54OPHpsDmZUzgDt4BfURrhKXHzFcXwkXbRCUrkqpI_XgP9UkF1W8oqVw557ghZj8xaZhzlaM09yDdCTX4NAJUQYzihvgfdI1TI6RPSYKI--AdkEga71y4b-7dohA17chdkJdefDI4OF6Iw0T5C9DfGEc7K1YbyBEF61-ZsDLFgg0_WyVhKPzHx9kbGumw8hejiZ7f4kN4G87VKWuxD5zV3GiK1DfizdoXpykMeCYkg9JVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oJaai3hPt68LQVt6n6tSO853yWfyko4hg3oJ45TIqBptIePocOyVOsUp-31A-I9GSNAQh_iJKBtq3pi-Jb9ZtYTteMmibZJLfgJ-0qzUTQkBqBPcXXmmUvSXlRNmpeB0rFcy3AvQ62mF3vheeoZJ1nJY548qqNXi56ZnaJSzjokGhpH-qXzcCdrK7So2TAKuNftudppU7Uw3lV_6n0GlkdKTvqy9R1WW9ErWMlj3xxZ5ymBVzyv1aj5FqAOOVN4vQ19WIi5eQzEK_EUrKI4RmFJhXbb4A8GlSnVBBncXhJiLClVDlUB9CPsvozkgAGT5ualqmvsKgx3XRWEmktu7pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇲🇦
ورزشگاه مت‌لایف در آمریکا با ظرفیت 82500 نفر که بازی برزیل و مراکش داخلش برگزار خواهد شد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/92623" target="_blank">📅 19:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92622">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbT-eki8aGzlDWBL4Mrx_KShuMQxg1yL2vyVQvkMkMXUiHE8RwRec2Zsii2E8talsMQbQdtaFX6UjPi_MqKTZ3TYgQ4V7vAD0PzdM4DrTWvAe82XSfe_QCx0MUwhqju84Oz0igRQ8sxVZCnkUFymIzeHXTw-55y5-4MkYH1ZQfzy3Cnnvgijp6K80Y9lgPvjrg6jRsUSLe4EbEguvXiWehFx6H3VOBGguHwWbqNfUDx347H9mraFmaEt1rYTlOHzEm4SUXrB3d1s3l2IjUIbi_J4qiau8Z5oDifeSStyAbDh_tGZvahXJETNh0P2sO0s_H949jP9NXkoweoxYf5hkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
الکس کروک:
برادلی بارکولا درخواست جدایی از پاری سن ژرمن رو داده، لیورپول و آرسنال به جذب او علاقه‌مند هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/92622" target="_blank">📅 19:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92620">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a5c97851.mp4?token=MFQ9SMEUXLxOyTbePsB_bXIaOqBcWKj41wNL0l0IsCLCgLdVZNHMiP5Ta0eI6BGCb3HrGSZClZUczFZ3Oa4TLS6Hfco3IzU7xxKUq1XUMzt43HzH7pScXXBNLfX32MeTiAWv-SDS2lch_kmepx6V6TdsYVsbA56s4RdiBBWJdMrOIrCyklQUo0Ui6jKDjK1_iRCgGKfuR2PkQkEyzE_oQvscn_KijYRR6-JT2fwhkFLd4tf0NnHdWJlxeWY7GUn5qbKg9w5dOzGl8gKeYoSL89YHTbnpqFqcorNzvCx73Qo_w8lV7M88R786hHYZBuZsZ8OnUSMg--oEB1o5w1lXig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a5c97851.mp4?token=MFQ9SMEUXLxOyTbePsB_bXIaOqBcWKj41wNL0l0IsCLCgLdVZNHMiP5Ta0eI6BGCb3HrGSZClZUczFZ3Oa4TLS6Hfco3IzU7xxKUq1XUMzt43HzH7pScXXBNLfX32MeTiAWv-SDS2lch_kmepx6V6TdsYVsbA56s4RdiBBWJdMrOIrCyklQUo0Ui6jKDjK1_iRCgGKfuR2PkQkEyzE_oQvscn_KijYRR6-JT2fwhkFLd4tf0NnHdWJlxeWY7GUn5qbKg9w5dOzGl8gKeYoSL89YHTbnpqFqcorNzvCx73Qo_w8lV7M88R786hHYZBuZsZ8OnUSMg--oEB1o5w1lXig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇲🇦
یه هوادار برزیلی اومد برا مراکشیا کری بخونه که اینجوری طرف مقابل بهش ریددددد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/92620" target="_blank">📅 19:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92619">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P44aR6Wtp3DgS_2c3IXb15YEL8Hp6LhIwQzyCd7b7JCYnjE45G8VyPgbOsrMYDtwWw88B2zuAd6Ys8bqEV6bwYqO0l26qpVl7-9KfxGpWp6Iza3I6kBYPcBo6rm9fPY1DQDgf1QH4AdTWbeAEnL5ct0pPlDCPf-xSEBxrFgqkN4JS65OI96tlppgO0ICaZfnfQpW4OV3bf1LQAH-aR-n97TaDmoJNTLE-apWjdtfXoaJtjLmZU68Ti8KlpviUIZ_fpUvudcWeB6ZhYzm0CCjl3fyb5F91OUOLoLtIjFYmF8YpvacL6nxGjO_wzRttet-eSTbdA3p2k4sJPTERtYq0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلو آنچلوتی: «احساس فشار و ترس خوب است. اگر بدون ترس بروی، با شیر روبرو می‌شوی و فکر می‌کنی که گربه است!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/92619" target="_blank">📅 19:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92618">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdef04be15.mp4?token=PLC2kwTa00oANP3qqIqRAR-arViQJEW7dYeqPV9YUohWCtJ6L97qDf1k9RtQ8z2D5vrT87m6zMU8uD8MnhF8jxHJfj0ejt2kmOMPAl6uhvclObWCpODAXuEfLyPoTjBDTJWvTrFSPlXaBlcSQ2CEKZJesNjHlXJQOIQUU3KWqtNI6huzDtJVeng2makpAZdURt_qhJzSqg2pz280FWkFBOAF-kP-fJbuumQHSGGLQuN7A26s634Vd43f3VTfBcc8rxqWEOTZO5CteJhhymZEUFUhm_3wdnciq5mUMnmaOyBHp9gFE0FwP10MlJqSBYNvOcN1l6VD2F52JksuqMXOvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdef04be15.mp4?token=PLC2kwTa00oANP3qqIqRAR-arViQJEW7dYeqPV9YUohWCtJ6L97qDf1k9RtQ8z2D5vrT87m6zMU8uD8MnhF8jxHJfj0ejt2kmOMPAl6uhvclObWCpODAXuEfLyPoTjBDTJWvTrFSPlXaBlcSQ2CEKZJesNjHlXJQOIQUU3KWqtNI6huzDtJVeng2makpAZdURt_qhJzSqg2pz280FWkFBOAF-kP-fJbuumQHSGGLQuN7A26s634Vd43f3VTfBcc8rxqWEOTZO5CteJhhymZEUFUhm_3wdnciq5mUMnmaOyBHp9gFE0FwP10MlJqSBYNvOcN1l6VD2F52JksuqMXOvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمامممم طرف عرق ریخته توی محفظه شبیه گوشی
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/92618" target="_blank">📅 19:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92617">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxl2oANwc02-qlm1MuEBXPrljQYgmJM9oo1hx7o14-e0tBWXV6fpP18aetdvK28spsgLiCthTLUltbAhmFPfDtnCx52ElmId9y9xOuUIgpWDXLfmNcurchTFVm8qR3qCxDxlV0OrLByBAuB4Cva9coOjBZ8nGN3UbfJsuzonHekKLtYZnj2ORVB-he3A3Ro3ewbBh3gKS6nLZPZxgsu-4ij-WNa0KwVOTXPv5i-1xwBJYVK-XZNQb1vsg9CIu33mipAVu33hA15z7qxzMFxfLjNzqsBstIFJgkcVRx3BhNcLWxHjR1cR9PbPmTzjNBkZL0Zhiy4eFS82Lkpw-fhiJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید بکهام : انگلیس‌ قهرمان جام جهانی میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/92617" target="_blank">📅 19:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92616">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
🔴
#فوری
🇮🇷
🇺🇸
🇮🇱
وزارت خارجه پاکستان رسما اعلام کرد توافقنامه فردا به امضا خواهد رسید
🔴
@Perspolis @RedStarFc</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/92616" target="_blank">📅 19:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92615">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q55bsOc8WIv9xNcZzcj-9SvHaak752S8fbjlUBD_31M0Cmd5cHol0PP3sLSTnIiByEeKGGk8ulyefPmqA6MDB11zNiGhVwCTkZg_tGYZDAGa7cWwl3D3qhTpQ2D7t8qULGUKH5UVAiELwIwJhQvs_TKk0sWhJ83f4D7JfWhs-j4n8s0kQGamU4us-ShA2GEu3pWUUFcI1vCuu00SWQnYyBNABNTG0JN738oBWd41IiUkMoJebMTpDYb5oQVgUKv2WZRy9RzkPa09IwMvyHeKX9IPaoYl-R0CTfUPxqQP0fjJOR2qTkRpHPPl1ibe1BLDXiBt1YqwQnbxi5HsY00WYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
‏تو پلی مارکت مردم شرط بستن که رونالدو تو جام جهانی گریه می‌کنه یا نه
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/92615" target="_blank">📅 19:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92613">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWbXgb8Yrnl5XA-MYeELi_-sXrZkfh5-VYVRIsiH9tOQSJmJbOg7_Eem-lcOidqo7gH4TFrvajhcb9gGZ_4sUwyuFNnsr7Xq69nsNOnurIDfl0T9pADIfFIzvrI-MG89cKvTaOW-mxd5TSqOp7Rp638V10Pu28kpnLfYNk-lj1izS1OLuoTLA0S8hKt5ckt7Gx99sZG_E-XLw_Ntx0_LvBm_ibjKygmMuWkkG-bKig44pfoQMFRwFxqq6h4M0CN-r5T3mI_-k4f3anL35Mx0ZDkZYkJ4gsueYZy1bFWTt34UkKhg21SqwtJDz-9Vc64ShhwvuXJUeczvbAz6f30djA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
فابریتزیو رومانو:
🔻
آرسنال بزودی قرارداد آرتتا رو تمدید خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/92613" target="_blank">📅 19:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92612">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXH4WuUFATfvpEumxGpvO80XZTzO3ElvJXhdveC1vaBy3r6-NneITGtwq4UETDXefJ2t-tSU6QoNp8PeyAUZY7iKfjJHcILK9hs_TLufEECDfsQgPocSLmbl-JhVifqKjXj2GZK9xFVcMvDJOYLKaY-JS9X4eSIePBy52veOz__Fgwh7mfQPOn8OBVWW47deIftSl4m5XmFjEcoH5HuZSx23pYic7scpRNZ46RKvB5oyVNzn-9FgF_LnW1WNpYXKMrNHNWEHtON3j9wxPSBk3xQrDnjJHIm9GstDUjlCxa0i7XuMw0IEBiPcuXf9NGZS0LnJyBJm_gSTexS0D2p6bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ماتئو مورتو: آلوارو آربلوا در حال مذاکره با فولام برای سرمربیگری این تیم است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/92612" target="_blank">📅 18:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92611">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8848bc0e2e.mp4?token=V9-V8Vca67aWLrcwXk8wqPnaJHTb4Bos639W-QhsELtHGrOTQkbZ9lX7sjNZsPd9UbvOTmTPDE9d3Pg4w21bU_zCL2sEDjRWIBDleZFxrC6Jo6aE-HVgKom60JrJfjgEf3fAFoaWNpPYj0vx1nL4fdzxPsb0HknO3o6lu-BeVh1KM-gsQi7YMcYzkkYinFRmuC27mhHlUJ3yp-awiMazdfwWFgLGD-rVlbx5gUw3yYQ41mWV8PpCG50hfjoj2ZTZ5d6j-13EWUMLvAUdIGt27GuLE37ZqwUSx_ORKm7N3U98BB1UNkhJqAUcfehNPFI-lWERvpMbgqjzIq36oZXd-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8848bc0e2e.mp4?token=V9-V8Vca67aWLrcwXk8wqPnaJHTb4Bos639W-QhsELtHGrOTQkbZ9lX7sjNZsPd9UbvOTmTPDE9d3Pg4w21bU_zCL2sEDjRWIBDleZFxrC6Jo6aE-HVgKom60JrJfjgEf3fAFoaWNpPYj0vx1nL4fdzxPsb0HknO3o6lu-BeVh1KM-gsQi7YMcYzkkYinFRmuC27mhHlUJ3yp-awiMazdfwWFgLGD-rVlbx5gUw3yYQ41mWV8PpCG50hfjoj2ZTZ5d6j-13EWUMLvAUdIGt27GuLE37ZqwUSx_ORKm7N3U98BB1UNkhJqAUcfehNPFI-lWERvpMbgqjzIq36oZXd-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پوچ بال ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/92611" target="_blank">📅 18:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92610">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ac29a7f7.mp4?token=BHwSURqjBC9ayDwjmXRdVvQU0EBGDPK9CrjK5lgzEP1NHB98boqzT62Lzd8frPdBPx0oh0_OgOptnXff7Hl-6X5t9iM-bD4s_edTTBUdNQdOtkz41FdwKu0qC73hW4_gfldGfyQnxtw7s9TgF5-Enee6uW2HdxMi93OcFlS87UIwItEtxIEmztD_Xej4t5MOyyH6R1cUYveeGqawSn53sYNdAG2E2tmq7kltfWufNyUJaUdg1YqK2rHL4hvArEx1KCKhpXgoqypd5rg8xaGVTmpsqGu6ziRRZSbqShdc_Fi5nO03xg86vUe3z5ooo3ybmdjzgHGtL-oHdQAdl1t_PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ac29a7f7.mp4?token=BHwSURqjBC9ayDwjmXRdVvQU0EBGDPK9CrjK5lgzEP1NHB98boqzT62Lzd8frPdBPx0oh0_OgOptnXff7Hl-6X5t9iM-bD4s_edTTBUdNQdOtkz41FdwKu0qC73hW4_gfldGfyQnxtw7s9TgF5-Enee6uW2HdxMi93OcFlS87UIwItEtxIEmztD_Xej4t5MOyyH6R1cUYveeGqawSn53sYNdAG2E2tmq7kltfWufNyUJaUdg1YqK2rHL4hvArEx1KCKhpXgoqypd5rg8xaGVTmpsqGu6ziRRZSbqShdc_Fi5nO03xg86vUe3z5ooo3ybmdjzgHGtL-oHdQAdl1t_PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏆
ابوطالب‌حسینی و کنایه به امیر‌ قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/92610" target="_blank">📅 18:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92609">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
فوری؛ وزارت خارجه پاکستان رسما اعلام کرد توافقنامه ایران و آمریکا فردا به امضا خواهد رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/92609" target="_blank">📅 18:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92608">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CltuzjB0pBDkfzp_Vz0E8Ajv6_Mx-oxiX5uyv8xvIOSwGRn0KjFcwk-sjh2sI0kvzlyKV3xMbwIac2zp860oWiZOXjWZEUvcRCUHNyhOi2XFkYpPiP1M9sgpzIid4dMWzqYWj9SWgIi2L20dy5Twoof0YQFs8mCXDRWb7Kul6ZUUnBh8GWINgauMT35tIJiN4RLTX5GYlwGlTZK-jrRRQVfOrXjvnZEt4vGnY0bU2fszNb1EcaGtryaZVzHAjftUHyJxaMi2F8ebkF2SUM9VUgIU4IMw20OVmSMI--UL_6TcwdrgMcXXrwyahmPgHEdCd5YKEiql5FDoanV3eth_Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
بیشترین تاثیرگذاری روی گل‌های تیم ملی بین بازیکنان حاضر در جام جهانی ۲۰۲۶.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/92608" target="_blank">📅 18:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92607">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_t4jQ4vI8I6ZBEESgi-ZhDhWPf0bzP_9eS3Km7P5MX7NIj4pT-v2OhuOHDZq-vVBIxMyGO2vdbNfVgX4-RubG0ylejS-l7GfpgfkVyR3wwfL0ND-6W9tzsIUvDgWHlcsB6RVB0mz1RD6hUsCIwXWK7ttDGIVScC0gnrYO_PQTkVlKU3DctWMAvqho8WDsiWeAKxeMH0pTzZHqjsVXMjd17nar29gkpEK2Vwt16DuECq3yMlxd5KzrAraV5LVZ1Abcabyg0vJ33qVvBm-vzHAVVvj3w1FjSo982wsvKJzUCS9mKmZJfIAoPLOe1wijnTWGidlrKO5R1kxJ4Faq6ZLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوستر باشگاه دهوک عراق برای یحیی گل‌محمدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/92607" target="_blank">📅 18:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92606">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mF4uamuUmClaPie4lYgycoCZmu05fBHImCOR7dsfksXvYnfqIDLvsrcEqUgPQOtLz9IwMkHn34jcixnDCbsk6q7Sp3eUksfzMv88WkZRGlDpjpZlY1Ed5V1Dgc6Ni5mvn3bPlZ02QSvQa6qrQnRuRX7YvVZAVT83jyoXBLHA-zbb62aFM_h-4KdGqxiYUgw5OPZEeOd-wSmv_hZtYh0uSchRp4BToYmiQ9yXPkENb2KLBPc9KmXdx_wkFF1SktUsaB4kgo-GiDTYbf4i5EG9NraILTHXXUck-bATQrZFYVERDg3H_oW1gQ4WgLtnuc3bxlL8DTPNPqEasWuXhNegDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
مائوریسیو پوچتینو:
رئیس‌جمهور ترامپ ازم پرسید پوچ به نظرت میتونیم قهرمان جام جهانی بشیم؟ منم بهش گفتم: چرا که نشه؟آره قطعا میتونیم آقای رئیس‌جمهور.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/92606" target="_blank">📅 18:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92605">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMyUeMatdtworXhoo7mHEDzyt-AFoUsIj-Sj9rFbtQcAUdhAkuc4enPQwIPz9uhBprBY5qQeQWTymgO-S7njOBTBaDYkVNhkF8AmzLbo07m1gnLIXu_vQAvsd7SDzHkhBZe99fjbvTw-euqwE-4hg0ini-7bfIrwOgoK7o2tCCoQeL-qh8_e6ufCwJx67Bb_4FD0QZ9UaEia3_MqeA-0IOXDVfmT3KU95VVZEmJznCyYNghatIkC75SLqF6vDiXhJisOnr85X96uhq0w31_4rqd7Xx8gW2wVUh3-sHGgoUuCXMac1t_3aVChh7ECpsLRwgFf8ni1FGI9QdV6cxOofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسر زننده اولین گل جام جهانی
🏆
هستند
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/92605" target="_blank">📅 18:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92604">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_JNdyjM8D_QO6vSbKHqpxtx61TSGBbgxcsvxEH23Hx_y9ecVYyYmWkEk7l-fUytADwyHjGVftbHtLjDt7rcf0Y2w_BpQpGIHLFeAmHVLTZ5-tZC6FCcBzmp9u7CiyCb1mdJzbMJw2kaySs7xVEcC7paRzyJIHB4p3kSavR2A3ILk5dAmoDsVkrkmgXlFZE2l5D7e8F0GkmpAy4juNzWMDeqE0r6cKSBMdrj7OjRhvzDPGzs5KgLmJu32czRqBsr8BNtaR5Qyvj3_J33gH58h5HIA00OkEsnLXPI9rEqGfS8hthv4QhiRHNz0U4mljVN30hCWqVER5NMJSYREDm0mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گری نویل:
همه درباره استعدادهای انگلیس حرف می‌زنن، اما ما فقط یک بازیکن واقعا در سطح جهانی داریم و اون هری کینه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/92604" target="_blank">📅 18:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92603">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IisWXp45ncgP77ZI3QkUlSsBXRTNnx2pxf3p-jbnbVfecZep589rR4lE0taR2ucUIl3oo0znWKv332VJ6tZ-KKqyn89gpupEspCJ6yeru-KFFCNIKa3r2W-TdG_YlDVDXQ6ZTaBCwcQZl4lxqZZ-kao5jIfR5jjmgDETa_s_qSi4uSddzn7gyD4IQAFOXgnLTg8G0914e8n93TXv_V79oARvorOl1Ksa-zCi2TocH-AK_5848UOYNWjWutBd7H6wmQpgS0n0BpOf5E3J5d1x0upe5_NhQ3zwxTAUITVIiaPL8TT1MFCoJSNGQk7RgTv7E-zPjrFDPnIdwhA8sUfQHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🇧🇦
درسته‌بوسنی نتونست مقابل کانادا برنده بشه ولی این هوادارش عجیب چشم کارگردان رو گرفته بود
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/92603" target="_blank">📅 17:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92602">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb924a92cb.mp4?token=DuMdLLlR7uJX0OJ7GPiQVmimGMtXeZpSomsDXMAd0H1g7RFqbkylKYTtznPtNbEOgRU2JFs4Q8DAkW88AkWpW7jLvomx0tz5sJXmrltRDfEfu5NZeHn7bU6Pq7yfJwCkHVFd1EisA1727CXBhN7bYmiF-tta_m3bQcbXV3xAsMvxPZpgvIEGcxhhFuX8-CSzzhXYPONzjfeF3sMIvHWj6udKd9dlohoWGhzLKhdHee41yxoWtQ1nvL2XqhmpC1IXg3rlCIUVFEbiJvI55tID-sKUj0Ti9vQJqDKb_tYkBCCCioGgPkelA0H52spzLjNepuJji9u5HtBP-urwbUSYRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb924a92cb.mp4?token=DuMdLLlR7uJX0OJ7GPiQVmimGMtXeZpSomsDXMAd0H1g7RFqbkylKYTtznPtNbEOgRU2JFs4Q8DAkW88AkWpW7jLvomx0tz5sJXmrltRDfEfu5NZeHn7bU6Pq7yfJwCkHVFd1EisA1727CXBhN7bYmiF-tta_m3bQcbXV3xAsMvxPZpgvIEGcxhhFuX8-CSzzhXYPONzjfeF3sMIvHWj6udKd9dlohoWGhzLKhdHee41yxoWtQ1nvL2XqhmpC1IXg3rlCIUVFEbiJvI55tID-sKUj0Ti9vQJqDKb_tYkBCCCioGgPkelA0H52spzLjNepuJji9u5HtBP-urwbUSYRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🏆
کل‌کل برزیلی‌ها و مراکشی‌ها‌ در خیابونای آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/92602" target="_blank">📅 17:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92601">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">از جام جهانی تا لیگ ملت های والیبال ! هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در بت ویژن در نمیره ! فقط کافیه یه شب از گلچین فرم های بت ویژن تا استفاده کنی تا ببینی چرا سایتا دنبال ترور ادمین این چنلن بیا اینجا تا ببینی فرق ما با بقیه چیه
💸
💸
💸
💸
…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/92601" target="_blank">📅 17:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92600">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMZAWVzoVCjZnXMLToUUGY4Z1LlwE6JdDIOq6n3m0fy4DKb-thaxxZYwwhzYayeDX_TqP4PcijOgv_0KkqSiiq61WngG9p3eWzmAXYmk-y7NtGyTPlRYMXgi4csb0pVTx3MrkYNJH5Av9inlDlLb7342-eqBKNsVXWZjyy_7so1UR4CN4h-cxzwOuF_NCICKvkduZt53tnSeQ693zuJd1d1egXYOFCaqteW-QvEqet7WBvqU2gORU72WOYfZFHByJfmJ3SLEze__DYugqkSK6bjQHdidk_qhWdXpxFvqp2jAZHC8Lv8Bd1D-mqe-8jYEURi0xLKp9J1O0fEaY8laNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از
جام جهانی
تا لیگ ملت های والیبال !
هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در بت ویژن در نمیره !
فقط کافیه یه شب از گلچین فرم های بت ویژن تا استفاده کنی تا ببینی چرا سایتا دنبال ترور ادمین این چنلن
بیا اینجا تا ببینی فرق ما با بقیه چیه
💸
💸
💸
💸
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/92600" target="_blank">📅 17:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92599">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e9b6fd3dd.mp4?token=geWhnwfutrthoudnHYC3a76rXOW4VQSYM8PJdz-23V1l-hRJCH-rRkak-HiABVmMeMz1xptTbjSZA6bv71qztX5JANaEsHIU49P1LzNKuuxB-l0dISyDWiEUcrzjjE1X5RKqypAAHwOPs8nM7jqHEbWHxhSea0bEytF8xTr7kk4eobfoHfdYGc-A50c3sN3hueHR6vAZdMn6sVGglYsf94Z-pE-L1YajG77m0HC_4QsdfuWs4ByuuGgv82xqr3RVsPs2B-JEJaPqoswyERtCAMmRa1Qa6cAIj49wMRMrb8LXB2rkVortjOEwY0zKG2ruKDh5VCgWo__ORrpLEIEqSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e9b6fd3dd.mp4?token=geWhnwfutrthoudnHYC3a76rXOW4VQSYM8PJdz-23V1l-hRJCH-rRkak-HiABVmMeMz1xptTbjSZA6bv71qztX5JANaEsHIU49P1LzNKuuxB-l0dISyDWiEUcrzjjE1X5RKqypAAHwOPs8nM7jqHEbWHxhSea0bEytF8xTr7kk4eobfoHfdYGc-A50c3sN3hueHR6vAZdMn6sVGglYsf94Z-pE-L1YajG77m0HC_4QsdfuWs4ByuuGgv82xqr3RVsPs2B-JEJaPqoswyERtCAMmRa1Qa6cAIj49wMRMrb8LXB2rkVortjOEwY0zKG2ruKDh5VCgWo__ORrpLEIEqSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
همچنان از حواشی جالب‌جام‌جهانی در‌مکزیک:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/92599" target="_blank">📅 17:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92598">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiCkoXUgN9Tih2Jc3hw15POVIroOs7AYq_t-tjOcOvf1emf_OlDE2MAloFvdViupfMZ6k47k-YLSiKWtPOPMUFFPh9xhRqWP0R3-mg7FYCPbhoMtMgWhTuFv33e6jo31IfUUERBw8ns-G1uMtwZMQo_TxRzwPTBn8mLC6BoxlvR7rqfbdPSRSdMJgXP9hNiKtyJNMD5Bo1Fc5UGj7LaT-L9jr22uotrP0tlTkPmguZTdnYtsjDAAE96lZ5cD6A-FdPy-zAXtnoehJU6n0GZWjr01ww7P53LFt3_fXa9F84a9HLOMNCzzimA6slaWSWBKl9O3o054jzanGGohTS7NTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
بیشترین کارت‌قرمز در ادوار مختلف جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/92598" target="_blank">📅 17:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92597">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/f8a434df64.mp4?token=avbI_t3c1tjaQI1FHXABGamWwOnk-JLgOsFAp6Tyg-PeMN6xuj3DESQQprgrpKfUNzPBirvKkC7sHthYJmbIa3S7VlRRJIndaVVCrL25E3chGW1xdKYl0V9alJQnzQEjuaJPR00ivvOGCsRzeQwt_3bKMFfdESmXrSJ54jb_YR2kWYlmV7Mz1ZgSv2Oq4SaY26BJbKnq1x_iBu7yuBmhAkRG1ZqYvmSpeW4gt70SaNrZC1wH0cXAqgsHyjNt4spxInSiyCYem1oXlFj9LOp7iKAzDHzHlBz3y9JJarPxXmxK0AwPY7BbGQapmKv3587DDoi1T84NuZxZub6hwdqFRg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/f8a434df64.mp4?token=avbI_t3c1tjaQI1FHXABGamWwOnk-JLgOsFAp6Tyg-PeMN6xuj3DESQQprgrpKfUNzPBirvKkC7sHthYJmbIa3S7VlRRJIndaVVCrL25E3chGW1xdKYl0V9alJQnzQEjuaJPR00ivvOGCsRzeQwt_3bKMFfdESmXrSJ54jb_YR2kWYlmV7Mz1ZgSv2Oq4SaY26BJbKnq1x_iBu7yuBmhAkRG1ZqYvmSpeW4gt70SaNrZC1wH0cXAqgsHyjNt4spxInSiyCYem1oXlFj9LOp7iKAzDHzHlBz3y9JJarPxXmxK0AwPY7BbGQapmKv3587DDoi1T84NuZxZub6hwdqFRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
یه بلاگر عراقی از مراحل آماده شدنش برای سفر به آمریکا واسه جام‌جهانی براتون ویدیو گرفته. واقعا داف‌ای حقی دارن
😂
😊
😎
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/92597" target="_blank">📅 17:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92595">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b37621fcc7.mp4?token=f91EjAWqxiaezbdugfyb1GowPWh7BGLNChn98-TZpOAp9Pa20YL2iSVj4PC1eELBXyuErDzE7WWrxzoP8hTZk4fZXncgt0u-lnwRrR6JnpREcqqXDynS1nriYICMX9NTgAjP_AE_7q_HjClT7cV4kzqGvcmqFjUcNBLSBbNRbb32AI46eCfX0PCi-hNVrZDGsvEmVZxCzpREFQFi9TGOqwkl96GLgZxbp32Ag1wAbiZuKxDgWVwqmH1b3JT_59MycC8Z4kr--n0qNIxzyS6KnilbZ0nt4iOHO7YZi7o0u1XbjKj9yTZWRc210w1GY4YVZMJMNfe-oIYmoKkmj_DO1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b37621fcc7.mp4?token=f91EjAWqxiaezbdugfyb1GowPWh7BGLNChn98-TZpOAp9Pa20YL2iSVj4PC1eELBXyuErDzE7WWrxzoP8hTZk4fZXncgt0u-lnwRrR6JnpREcqqXDynS1nriYICMX9NTgAjP_AE_7q_HjClT7cV4kzqGvcmqFjUcNBLSBbNRbb32AI46eCfX0PCi-hNVrZDGsvEmVZxCzpREFQFi9TGOqwkl96GLgZxbp32Ag1wAbiZuKxDgWVwqmH1b3JT_59MycC8Z4kr--n0qNIxzyS6KnilbZ0nt4iOHO7YZi7o0u1XbjKj9yTZWRc210w1GY4YVZMJMNfe-oIYmoKkmj_DO1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
بخشی از اجرای نورا خانم در مراسم افتتاحیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/92595" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92594">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpghueVzIkZjEZzMpU_dU7Evc0jXenDw3uQYyCLstGxlGDEmWomhnZmjQcMOZ-0Dj0L11zpUQ01AwlDrLwhgWJbnE3sWFyufCSARyMHJoS0k39AOBuKh1uziutCNT23PK64mse_Zklu2KkAUHMaut18QsmFTFeqxv89jfzg1xSUys--x46ESTOWISAU6_yU6EBderbcz3kOs0rn0mpgRRZbdLshJ-27wA4nQsTwv5kgajLDQ0SMXSDQ9CUAB3bkQMA6Sn6eTvwsIippV2r5QWllna6c1XFKUSm9dG2tOaNiLMa_mT74ORcMZ2nsTg_d7AL4EaGGcLJB6dPLOHlOjWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
🇸🇳
علیرضا فغانی به عنوان داور بازی فرانسه - سنگال انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/92594" target="_blank">📅 16:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92593">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWjTrl5IO4mNeNmF6MhJHFtkWelzq_SYLQiV64Gh-gs7dfBQgFuas-rbXQw7nKP6smyBMwmJp-3uJ_lCrwP6z6MpVqBFNAEmxYCT_kzTMdOC_r1-nP20k3DJ5iMAObTHbnP639T2Agxa3NwYB1ZXPTkMaJ7fxoGQyLewYDDn7FXgVDq29wmtsieR1BX7RUNiu7RrnFW0_Ky6BRWFhAbo0usphFRqyPm34sUeyVFalo8ckNCl0QovQF7Q9bSt4Qm5aRI1zAoa8v-tYaI6myP54aeWgF-5dYS3wyWU8gYYNDczB4LZ_QU6U3_C25l4iEkGBrxRHg5n_Sbd0mgwB4Wbfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید بپرسید این آمریکاییا که فوتبال نمیفهمن چطور میشینن پای تلویزیون؟ جوابش اینه که تلویزیون آمریکا برای تک تک صحنه ها میشینه واسشون توضیح میده تا بفهمن! مثلا تو این صحنه گفته: در مسابقه یک گل زده شده و بوسنی و هرزگوین 1 - 0 پیش است. ضمنا کلمه BIH مخفف بوسنی و هرزگوین است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/92593" target="_blank">📅 16:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92592">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuhRySDgeHhWPzH8q6-LvcdJQOo8nacaBvcdOzQxYpfOkeponzTAIaffet62Lq-b4u8IYwnNGqGwmnLWniNY_KWKevVlDXudYdus9ewkXKuFHxtGdN7qXvGujQmbHNQNmZKhkDCHHVx47YfguM1xL8hBNMRoF3pU-29ihpxaqu9Lb5ppg90g-n2IxbrorgmnMpOxgCMzEWoECcjCLOZ3e5tFQdOocFZL999tG6vD7m2vHmWcjlw4KGf71FjtMXhqmmHRXv_a-OR42RF8jt6TWBwJrBTcnuMd5pE2n4o2z4tYNqqmlurwWjWN5xCyRbtmBEmuDn0CAGC4YQDX8yY5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇩🇿
مارسینیاک به عنوان داور بازی آرژانتین و الجزایر انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/92592" target="_blank">📅 16:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92591">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20cc98b7b9.mp4?token=AfvH2_u_CItTLGdAQ9vcHnUQwW1ivB82WoPUB30dYsfnSLwQdfxGysERO5dDl4fuTXqbGQdE42RjJkWBTfmtFlIR2i5Ig09mUvmfbc3EbAnOTpcdI2FWsXgGTR0erTfwQm1ijxXHtmp1M3nUTTGdOE4X0ChsMuqaY_2Nsd9R8_JAWn7Bed_-9113dHuykaVFqCVIK3TNKrbQgcz4nQwHmlWfBjOIauRj-3VCFsg2GWS-ioJGP3FA5gPgSiCkNtmV__r-KZhxisjk0kKtHlOHqV2WqqwMXQlfRgkHQZ3kwxFKYva2fepMi52PVSnEyC5bZIHBwbvU4pGaBSuzffZJjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20cc98b7b9.mp4?token=AfvH2_u_CItTLGdAQ9vcHnUQwW1ivB82WoPUB30dYsfnSLwQdfxGysERO5dDl4fuTXqbGQdE42RjJkWBTfmtFlIR2i5Ig09mUvmfbc3EbAnOTpcdI2FWsXgGTR0erTfwQm1ijxXHtmp1M3nUTTGdOE4X0ChsMuqaY_2Nsd9R8_JAWn7Bed_-9113dHuykaVFqCVIK3TNKrbQgcz4nQwHmlWfBjOIauRj-3VCFsg2GWS-ioJGP3FA5gPgSiCkNtmV__r-KZhxisjk0kKtHlOHqV2WqqwMXQlfRgkHQZ3kwxFKYva2fepMi52PVSnEyC5bZIHBwbvU4pGaBSuzffZJjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇺🇸
هوادار آمریکایی که دیشب سعی داشت بپره وسط زمین و اینجوری گیر افتاد
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/92591" target="_blank">📅 16:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92590">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
از فصل‌بعدی لیگ‌برتر انگلیس، کشیدن مو توسط بازیکنان با کارت زرد جریمه میشه و کارت قرمز نداره. ینی از الان امثال هالند و کوکوریا و سایر دوستان باید یه وقت سلمونی بگیرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/92590" target="_blank">📅 16:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92589">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🏆
🇮🇷
🇳🇿
طارمی مصدوم شده و احتمالا بازی با نیوزیلند از دست میده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/92589" target="_blank">📅 16:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92588">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc29fa385.mp4?token=IGZMayZxry3Ul_ZDKE8bf6Ip9dxyku_TxecbdU-V1Z6zbF5WD02gqlOwSEOVvAV9_WJR1HrkE49_DGDHk5aqGa-3pd7E8p_n2Y8yzMwnKg7x0FEzkFYBuAYETaQffnsCNCz91RJEIRfpP63DRBsPjmvOTAdjbzhrb1vjfbv8-uYLRYMIbaQFl2YYATEN_8HekC-MJYDKv_D4I-8t3XTZ8ULvBZGzdCZd_XZabec8Vge9gNobznoKM6OKsxXdGZ5jNbRLQIQv490yYbcc8WX-nd6Q2qr4SdgKdbIdYodHETYRAT-kpfRT0p9xIEuscspx-x0_6ot28j7EueAxX0s1Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc29fa385.mp4?token=IGZMayZxry3Ul_ZDKE8bf6Ip9dxyku_TxecbdU-V1Z6zbF5WD02gqlOwSEOVvAV9_WJR1HrkE49_DGDHk5aqGa-3pd7E8p_n2Y8yzMwnKg7x0FEzkFYBuAYETaQffnsCNCz91RJEIRfpP63DRBsPjmvOTAdjbzhrb1vjfbv8-uYLRYMIbaQFl2YYATEN_8HekC-MJYDKv_D4I-8t3XTZ8ULvBZGzdCZd_XZabec8Vge9gNobznoKM6OKsxXdGZ5jNbRLQIQv490yYbcc8WX-nd6Q2qr4SdgKdbIdYodHETYRAT-kpfRT0p9xIEuscspx-x0_6ot28j7EueAxX0s1Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇴
👀
💥
هوادار اردنی در انتظار آغاز جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/92588" target="_blank">📅 16:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92587">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQNFmJvzJe2LFKDruVWlRo1Nv7YpcioTWRyahn8ugVGdCWnjUjiQ9BKyPr_hkHL7dVXlYiZoacyKZuSbWd939IY4R8ON3a0arQXiBX3VGZcZQmRevV2mf6OjCtbj9deOTTdiKCySM1Vjpv14Ybp57XhCdQidI_XXKxwqEND3eGHlXwVwxW7dBDjrwYApeCYeHm06_NavuIm0F7wLqM9rQ5pNZ98c21sd7N7NE7g6pcwkEckTWOXKFEy0wvaJxGMJUAFKDFhOSC6KL-0muCwNtKk5ltLrEsLh61zp-WqgjLmndcDVMdwMG4DHmBP-glgaGyXjMUMyLc31dbpn040mPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان امباپه در اردوی تیم ملی فرانسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/92587" target="_blank">📅 16:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92586">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔥
🏆
🇧🇷
خیابون‌های آمریکا در تسخیر برزیلی‌ها برای بازی با مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/92586" target="_blank">📅 16:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92585">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yft4bMc6STlF1-2t4xlIZF9HYAiuLcD43aIGhzj00PifU0QxM2S_M1encYFDOwBAWREd7asLhuiGC75XAwT8tF2oQbocx2XjrYg9st5TkuhATyIMWWLEiLvgHE2oonfczGQlyT9k4Sz2XV11H0brp9cClNWbVZzl4-B_2Fj9gYtgwoeBumLUPenbFlLwp0k_Thv2GkdL4FSxlOvSAcAtLRZiWkrhAD3tmI9oSsz5gpUmwtfd6rV7UwX-9gxkrNjGWRcX_g5PTdwRqiwlgAgCoz6l1s_HVYyp8xXZT7wuMjUDjG50zEUkwygcyVbdxwj3Jq8StVDK2bbUPaXZzE3LgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇲🇦
تمام ۸۰ هزار بلیت بازی برزیل و مراکش فروخته شد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/92585" target="_blank">📅 15:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92584">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea0232ce3.mp4?token=RZhBvDNsUuqBchmbkwD0BesxR6nH9BPGpyM6LnjrBQMxWaSQ6Iontgua15iBKQ8JBWj-rm33mKF10eDQGVIrPu_fIRbYmKzf8dIzCGtPKfsToB_k0YSnWa35Rk-BNUSEn9niq3lLHAHz6AVo0o4B4r92piZwRPUP8j_FHBWqAQ-Ab12yAtp_OizF-_DMxJ9a7RinepbyTWNyJCT4jADoYlv4lg4FRi5OBIhCXdrnuhzgk4MFdUkXL3upAeoyD4K3tg1EMHjKafd6s0lZjkCWEJodANP2p5c0Jaz8pEUZcSy6UEc89hizF4V8nxbhlGzdA-N-KXDd2tD4f13LiHUNow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea0232ce3.mp4?token=RZhBvDNsUuqBchmbkwD0BesxR6nH9BPGpyM6LnjrBQMxWaSQ6Iontgua15iBKQ8JBWj-rm33mKF10eDQGVIrPu_fIRbYmKzf8dIzCGtPKfsToB_k0YSnWa35Rk-BNUSEn9niq3lLHAHz6AVo0o4B4r92piZwRPUP8j_FHBWqAQ-Ab12yAtp_OizF-_DMxJ9a7RinepbyTWNyJCT4jADoYlv4lg4FRi5OBIhCXdrnuhzgk4MFdUkXL3upAeoyD4K3tg1EMHjKafd6s0lZjkCWEJodANP2p5c0Jaz8pEUZcSy6UEc89hizF4V8nxbhlGzdA-N-KXDd2tD4f13LiHUNow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇲🇽
مراحل آماده‌شدن بانوی مکزیکی برای رفتن به استادیوم برای دیدار افتتاحیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/92584" target="_blank">📅 15:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92583">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
فوری؛ نخست وزیر پاکستان: ایالات متحده و ایران به متن نهایی توافقنامه صلح دست یافته‌اند. پاکستان در حال آماده‌سازی برای امضای الکترونیکی توافق صلح بلافاصله پس از تایید آن است، و پس از آن مذاکرات در سطح فنی در هفته آینده برگزار خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/92583" target="_blank">📅 15:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92582">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30d3a7229c.mp4?token=IDkgoYJ8wD85X6O3-9gMSb2944-rMVkgUEu6FgEd3yEMgLXWesg1rQkhUkMZnZQWmesauBsxehQ7kvAp9xMj7iApMxusMydveNEbyarrrOxaZGsQy-N6HyFoM2ky7_-qh0MdKupWUSqpQwwZxMlvcC5_3DmiasuqI2ZwfjrkdE4KoEpHnYg31s9eCSa2nbyNUp1l8SjlPl9hiCaudmvyB76A54igevwuRGv7IiESkju_E91cXlktmg53-hdOpHyFGC6WuuUvm-PwOJcngLSAQDvCqr7QERtVDHs0QYrXR4iEpT5A4kyJhtmW4TKMPca6wdVsQfl4fFH2UhQy5rwmfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30d3a7229c.mp4?token=IDkgoYJ8wD85X6O3-9gMSb2944-rMVkgUEu6FgEd3yEMgLXWesg1rQkhUkMZnZQWmesauBsxehQ7kvAp9xMj7iApMxusMydveNEbyarrrOxaZGsQy-N6HyFoM2ky7_-qh0MdKupWUSqpQwwZxMlvcC5_3DmiasuqI2ZwfjrkdE4KoEpHnYg31s9eCSa2nbyNUp1l8SjlPl9hiCaudmvyB76A54igevwuRGv7IiESkju_E91cXlktmg53-hdOpHyFGC6WuuUvm-PwOJcngLSAQDvCqr7QERtVDHs0QYrXR4iEpT5A4kyJhtmW4TKMPca6wdVsQfl4fFH2UhQy5rwmfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
🇹🇷
هوادار ترکیه‌ای حاضر در مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/Futball180TV/92582" target="_blank">📅 15:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92581">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzLBXTU0Dt0MVfRLUjnnDZUnVNZ9lsCupnqsBdB3gaNCVF5mo_BQ3GkltAFfamtMPCCRad9RMkyJyg8mDwqXQWDyX0Lou5n4BoM00y0zeH9_cpy26tW86TSvOdNRgEBLvbDk0KcrGuUBIAQH8SkcAyTu5UObNe9_kQp5HZuP3wETOoxkHd-PqIs3WEVABrbqHn7bJ_Vgarc_FTDvtZZRiZ_a3iyhlU4DHJZlV8UrNlJxTXNegh0vcL-0bGRKjo_SJvzw8njSvw0DRM2sqVMYLExnsQAfUKyEWW35woJknkN_qFaFD_MGfC0BEg4RYoc0ygeTMrVKmsAEzaysQftRow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
#فکت
؛
پاراگوئه که دیشب آمریکا به راحتی شکستش داد در مقدماتی جام جهانی آرژانتین، برزیل و اروگوئه رو برده بود
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/Futball180TV/92581" target="_blank">📅 14:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92580">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb8e1d2890.mp4?token=UNzB4QIV6dif_Xi9kcfS8N28WgsvCvTEmmn7pci0EEp-p10idAtsaNjqFSmA9ih1WcOvqzGiD_GPiZTQrwNoKQcryijns2ga95eSK2xaa4U2-ctWiiUBAFgRpk5P0ppYLtV9Jk5oRA5dhVdy-OIkUs6aYyOqbFyN5YPmJwFmKAzBLLM9LFKzebC2c1XHX3miRkLrkZu2LlPPPcWE3dnamF_3KFbmZlZjkjlpDblp7QWtyyYc4qP6zIb3SCSgmMJCfovRyW0JyPK8YzUYvGBOFCuwqvafsXonvMR7zZskS5rahTVlcCtIpbcYEj9zjqGZfqCh2lW8MQs57JT4R1VkcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb8e1d2890.mp4?token=UNzB4QIV6dif_Xi9kcfS8N28WgsvCvTEmmn7pci0EEp-p10idAtsaNjqFSmA9ih1WcOvqzGiD_GPiZTQrwNoKQcryijns2ga95eSK2xaa4U2-ctWiiUBAFgRpk5P0ppYLtV9Jk5oRA5dhVdy-OIkUs6aYyOqbFyN5YPmJwFmKAzBLLM9LFKzebC2c1XHX3miRkLrkZu2LlPPPcWE3dnamF_3KFbmZlZjkjlpDblp7QWtyyYc4qP6zIb3SCSgmMJCfovRyW0JyPK8YzUYvGBOFCuwqvafsXonvMR7zZskS5rahTVlcCtIpbcYEj9zjqGZfqCh2lW8MQs57JT4R1VkcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
یه بلاگر عراقی از مراحل آماده شدنش برای سفر به آمریکا واسه جام‌جهانی براتون ویدیو گرفته. واقعا داف‌ای حقی دارن
😂
😊
😎
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/92580" target="_blank">📅 14:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92579">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlXLP8mlpbXol3dbT1AUPxkGQOuCPlPdI49FC5cA-p_DvtemzD6UzX4GN5IKqgZGZf7JDA6HKzA7z2Oa9iqa_sm1R2cfCe479_MOnuQQTVlDQndyDqbBHiOvBJdOoHbq8-3jr20GWxB0UYruP6L1NL2DZTndTkZXCBrsLA9LABDNx9dNn7LstLe4_XIYi9tNbvgDR3wy31ueSvUV4o4JpvVbC9_gu8aNZQ9rjO7IN7-IRgjwLT0d_yKFR7iS5Cg7994h_AX-s-sb9eeJiNqbKbBfi-gcCbtIt_SHMFqMKFftVmj8aVPVkcJEjEnEne-r2pfmDCSiedpbHSBt4z4N6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وضعیت هری کین بعد از سرقت ون تیم ملی انگلستان که حاوی لباس‌های مسابقه، کفش‌های فوتبال و تجهیزات تمرینی بود:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/92579" target="_blank">📅 14:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92578">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLmGBRzkngNH3HhU0KwkgwHuzkvVUokDdZUKfHUbwVzZL4VzC9LZ5IQH8S7EzKMSPvNRFOs0xplmg_qokf8ow2Z3QWNOvJEQ-CMMjJisb-YkuSyksfzygebH4oFqCFRRjTH_of3_SW-0mbYRrQJ-B3mbRVQ15Ia2qUPNMWlHPufYDNSEqCf8wdvZ5AjEjaRtn57RnZ-ma6L0VJXhsYN5R6YMk2fQxfAAeJkAvnUmvIdOk1K7S7Fjf1EPd4ZHFZKs3_3mmSnKsx8dZ_74mZkGNfeTBi7glpQ6vAmnYj7v7iA5SOTcGcipDTsDbdritaVOP6B1zZM7WqTm2Vcqw1MpeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
فابين رويز:
حاضرم همه قهرمانی‌هایم را فدا کنم تا قهرمان جام جهانی شوم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/92578" target="_blank">📅 14:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92577">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9988c82bbb.mp4?token=u-WO-vDX9CQuwIgzaCmzAv8DfacQF4p4akTJ26CvlkULHhKfUFojnszLZm7oIvFsXnPAMn9wVn-7wuMLGvDyA15HZneE9q_AgOWC9d-BupPwFAGnaFBsI2dijouLSmkboPtIuM4VtSQPH7_DgfWLdH9TSfrp-8FjjpGhiJ2p__LInCU7kPOlgtYfwaOvT7SgGu-o8JRa0v-2-vecYYnIqnAy9mvbYe5jWoWeqZZW76PSP4PQXpNLV6J7JcYseNokTVIWrV7xQ8dS6FCX0bSE1HzWBklpAnNlLX2T5yOl2_f_KehdGgnO7oefHll_IsUOGK9HJgpWrQLatoM3NbgrUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9988c82bbb.mp4?token=u-WO-vDX9CQuwIgzaCmzAv8DfacQF4p4akTJ26CvlkULHhKfUFojnszLZm7oIvFsXnPAMn9wVn-7wuMLGvDyA15HZneE9q_AgOWC9d-BupPwFAGnaFBsI2dijouLSmkboPtIuM4VtSQPH7_DgfWLdH9TSfrp-8FjjpGhiJ2p__LInCU7kPOlgtYfwaOvT7SgGu-o8JRa0v-2-vecYYnIqnAy9mvbYe5jWoWeqZZW76PSP4PQXpNLV6J7JcYseNokTVIWrV7xQ8dS6FCX0bSE1HzWBklpAnNlLX2T5yOl2_f_KehdGgnO7oefHll_IsUOGK9HJgpWrQLatoM3NbgrUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تاثیر گرمای شدید مکزیک روی هواداران!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/92577" target="_blank">📅 14:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92576">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c68dc271bd.mp4?token=iaHI7oxLrox9i9VepqR82HRQKG_bcXqJhnXlBMZG1a5zJwkQXbgJO3U0GSyTYgOxKsVlA31x6LsIsHosVLM4VNori_Ls-hrC1zV68G_PSTfx6tS2ExiKbObVVNNlldSMqaKCnmiwwkxE26aM2wCJ2yrTWC4r-cqeXqEOk4k__YaCZgZw14ZG-XCWkm9iTI1MhF3NY-5vbtOu4E9AuuIk2lgJZ80QpaqHgLnIrO3U6nm8RiIgTOc321erYy5qNhK551-AeMhr0iWSQJxDdh5x5K15gr-Prbd1hbJeIvFwToHqkc6S8wwt6QRE_ooFPiFAiAyqD_NvvzUdKdzQeL9mPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c68dc271bd.mp4?token=iaHI7oxLrox9i9VepqR82HRQKG_bcXqJhnXlBMZG1a5zJwkQXbgJO3U0GSyTYgOxKsVlA31x6LsIsHosVLM4VNori_Ls-hrC1zV68G_PSTfx6tS2ExiKbObVVNNlldSMqaKCnmiwwkxE26aM2wCJ2yrTWC4r-cqeXqEOk4k__YaCZgZw14ZG-XCWkm9iTI1MhF3NY-5vbtOu4E9AuuIk2lgJZ80QpaqHgLnIrO3U6nm8RiIgTOc321erYy5qNhK551-AeMhr0iWSQJxDdh5x5K15gr-Prbd1hbJeIvFwToHqkc6S8wwt6QRE_ooFPiFAiAyqD_NvvzUdKdzQeL9mPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چندسالته؟
- هشت
اسمت چیه؟
- پابلو
تو افتتاحیه از چه چیزی خوشت اومد؟
- رقص شکیرا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/92576" target="_blank">📅 14:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92575">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">💥
دو هوادار مکزیکی که ویدیو خوشحالی‌شون در فضای‌مجازی حسابی وایرال شده
🍑
🍑
🍑
🍑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/Futball180TV/92575" target="_blank">📅 14:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92574">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/92574" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/Futball180TV/92574" target="_blank">📅 14:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92573">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfXJYgXshFUfr8t0glZlOicJZWbCyq1DmkoeEasElgMaGfyYj52EFzQNNmN3v01WBetaNV2DBiRaQhagg3yydXzV8Z4SCf71qotXUoX9jbCd_DeoJpEIlyts44CaEvE-BnRPZmAu917_4a0wRbVkN1g2mLd5RamnZ6tNQ6GGj5Hqcj2O04ksUODJjsKqnWM6f0jYMNZaRcFyb7uHvmmfNezl5r6EMHG5hRoGGgK7Y9ElnkPRrqg1y5DPqXnOxieYw8UQxUiUJvluluNGvTJ5YhvqT8rFNBR2Z6savH4LjIkoCpnwphppdOoIN0Ka4HwwQW_bmizzBhv9w0X6mIWwww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/Futball180TV/92573" target="_blank">📅 14:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92572">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myHCqERqgCjYEetdcsvzac-xtHmdJtz0JUjfa0ei2Vc698tO2lwceTt58U-8xbl8jN_oj0BlwQJEyA98wZ6qlhztZ9F8h-xZiKJOxGz5gFc7RifOVn9QOQ484kYV8GuvTWFEf_G06G0C-3j_O7oocZtw4mlROhFxsEspKnB6aHi3IiCCImMoekokxLdXC3kv8j-yGyGvTjZmDoVu-xmJLbk0FjlrJksCGsgI8OCy9ZR4b_hTdm4p__OJVJy6iFeF3BNgTvpvQtD2_ZK0VFAjzpZ_Lf4OR21ux6LKKa3aa0WnvVym5odoiqsNard61lFfyhV2PdO8-nUdVpz9gZS3OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📅
در چنین روزی در سال 2022 منچستر سیتی با مبلغ 60 میلیون یورو، ارلینگ هالند را از دورتموند به خدمت گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/92572" target="_blank">📅 14:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92571">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/066401b152.mp4?token=LzPZAE6Q0H5NCJTgOfBvDyRWl3UJ3L6tjiUkl5CvXsrulYsYs0eVK001gGrOZuMyzClH0YZcp8X5MkpFrnundpUP9ukipNeJry7vjPkHxWrShSoEDVK4RgaOETLPcVjgdcvP_nKTaUS5rszQKP8sYVVlyDNckwBTdesULaaGjg2_LsPScloL09ZFUM6mPXJ-FN6VkxecPxSF3dm4-_di8Pt287xYji6MEoLPGarFlGB8eYdkjPhyHkzHo1zvtTMe2sUo-n40gdC4VY9Of93OYM7HZ3yskLKBsywpclceqLxJqHo8710uyPkLykAeNU587iZfOt-D0GUdWQNKPYzJxjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/066401b152.mp4?token=LzPZAE6Q0H5NCJTgOfBvDyRWl3UJ3L6tjiUkl5CvXsrulYsYs0eVK001gGrOZuMyzClH0YZcp8X5MkpFrnundpUP9ukipNeJry7vjPkHxWrShSoEDVK4RgaOETLPcVjgdcvP_nKTaUS5rszQKP8sYVVlyDNckwBTdesULaaGjg2_LsPScloL09ZFUM6mPXJ-FN6VkxecPxSF3dm4-_di8Pt287xYji6MEoLPGarFlGB8eYdkjPhyHkzHo1zvtTMe2sUo-n40gdC4VY9Of93OYM7HZ3yskLKBsywpclceqLxJqHo8710uyPkLykAeNU587iZfOt-D0GUdWQNKPYzJxjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
عراقی‌های شنگول منگول درحال سفر به آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/92571" target="_blank">📅 14:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92570">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgDT3cGVC5NaIlbZk-UK4wd_5qEiBEJLHdQAhihxaNqzeb0OEkBu4O3Og0c0ke-60sTR9JzcVuQPnlIaD3Pb-ehrqLw9Da3Zt7nauxJK033Yc84fAFTtfN-7Yr_4mlNxxnz8VitKSgQAWxLMnm8m5ESbSZVKPfJwp70Lc9LNYJa5SiPC3OJV5u936x9rAQXvwFadbXsOkr5mP41goCGqHxF_4iGyBgUOhSONK1I-BQK_z2Ut7VVnHY5PKCh50zKZBThlfd3KWyvZYlpcWXUNhpuC9UiOZNhE6B7ixrulc73w62bAhB8j9yVDcO_Lc26oC7v1aqf776jU73ae3WhvHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تو سال 2026 ایرانی‌ها با میانگین IQ (104.8) رتبه چهارم جهان شدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/92570" target="_blank">📅 13:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92569">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09d9becd6.mp4?token=INwvpuDaxEJZuQLV5Eq4AikbgCY4lYTS_GsQg2iHMyEN6t_n6WRbA3c5nesthlX6wmN01-QMdEd3HhnQeT07oKRZRcAaLBzNKEpBqx7zOTWyuonmAl6s_RpAnkBUGaLtFf4SnkslBmVyIM5qkG0hVFKdcKsOIJFO6Eoh6Z0ebU1a7ZR-UEPzuia4f4DkEkP1aKGf07FAZKn0r4v9v7D10tEDf4Ny78yM89kwlaPckfZqIu4w172lh-O3cZjG9BEHZAi8owHp-urywzwssgrqDTjzZH3gbUoAaCVp02QestVLbnkHonKSn4--JMkGmNPE7m0LWyAHq69mImw6A57lfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09d9becd6.mp4?token=INwvpuDaxEJZuQLV5Eq4AikbgCY4lYTS_GsQg2iHMyEN6t_n6WRbA3c5nesthlX6wmN01-QMdEd3HhnQeT07oKRZRcAaLBzNKEpBqx7zOTWyuonmAl6s_RpAnkBUGaLtFf4SnkslBmVyIM5qkG0hVFKdcKsOIJFO6Eoh6Z0ebU1a7ZR-UEPzuia4f4DkEkP1aKGf07FAZKn0r4v9v7D10tEDf4Ny78yM89kwlaPckfZqIu4w172lh-O3cZjG9BEHZAi8owHp-urywzwssgrqDTjzZH3gbUoAaCVp02QestVLbnkHonKSn4--JMkGmNPE7m0LWyAHq69mImw6A57lfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه هوادار کره‌ای بلند شده رفته استادیوم بعد مکزیکی‌ها اینجوری پشت سرش حرکت نژاد پرستانه میرن که طرف پشماش ریخته
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/92569" target="_blank">📅 13:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92568">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🏆
🇯🇵
#فوووووری
؛ اتوبوس اعضای تیم‌ملی ژاپن دیروز تو آمریکا تصادف کرده که البته خسارت جانی به کسی وارد نشده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/92568" target="_blank">📅 13:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92567">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">جام‌جهانی که نیست لامصب تهش میبینی ازش فیلم سوپر در میاد
🤡
🤡
🤡
🤡
🤡
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/92567" target="_blank">📅 13:18 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
