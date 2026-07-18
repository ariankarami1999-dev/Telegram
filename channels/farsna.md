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
<img src="https://cdn4.telesco.pe/file/MMiBcX7SbWP4nLRHFmLrq9qswXnoneZZhpvw8kfiwCd5jiBhwP2m_lyXnuPZeBBA-aYPtMpdcw4JaiiVLdvCO17bdBRZVLDJ1X1eV2h7EruB7aXrHqHc-RHYGaJLjBx7VQKk12W8jLbSW4A1OchjzjK-t9VB8Bwgxf_onNWexUypb4ZStaZR1OgLA69xlOiYG9m8ds8O6e1-9zo3kRMUhQmJurGlNoScaUNts7p0w6TySmf9Mpi5gGlgE0I4drUvBepwK7cQf9IpNIM26SfD6p7WUxQxRj5PNkJGCxwqV0pEBjWlxCJRElNAumsB0JcdvWI5AqXnUGAMd9I7V_NOKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 01:11:19</div>
<hr>

<div class="tg-post" id="msg-450990">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31f8764ea6.mp4?token=TH6nMAdbYyFN4hpN30SB2uFCqabWfehQWbAKOI3vLVgevo6ASEiaSoB0CWZSS20AfhHPKL9x_CTRJL8ooZM_yedMPkLcPHP66qRwr3_9LECH0lhyM03_jLUjI7GMaiSiWIa422I_LIaHaBFL-7TpiFGJGvpG3XzZ7S1OathFHF5jqI_NPpr7dOUPPkQWLv1JrLTE5bDVSvvPAWzdfCMXTvQMaXCbTQJrlQg1F0q3EVmhJzvoejiZ2RIen3iMjwVbuTdoYSEoWux_1n5X7zOzLqfG_8TsaJs5x08eckyud2_0wN8jzRacm4wG588FC4JKvMjRUuI9lyo-3nCvhXrumw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31f8764ea6.mp4?token=TH6nMAdbYyFN4hpN30SB2uFCqabWfehQWbAKOI3vLVgevo6ASEiaSoB0CWZSS20AfhHPKL9x_CTRJL8ooZM_yedMPkLcPHP66qRwr3_9LECH0lhyM03_jLUjI7GMaiSiWIa422I_LIaHaBFL-7TpiFGJGvpG3XzZ7S1OathFHF5jqI_NPpr7dOUPPkQWLv1JrLTE5bDVSvvPAWzdfCMXTvQMaXCbTQJrlQg1F0q3EVmhJzvoejiZ2RIen3iMjwVbuTdoYSEoWux_1n5X7zOzLqfG_8TsaJs5x08eckyud2_0wN8jzRacm4wG588FC4JKvMjRUuI9lyo-3nCvhXrumw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انگلیس گل دوم را هم زد
⚽️
انگلیس ۲ - ۰ فرانسه @Farsna</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/farsna/450990" target="_blank">📅 01:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450984">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CYBfhUP2yGq9oLIucrAJd9VB5ABWK3j1IuzmgI3ERUlaQTwaYj9uid0-ewEYYgm5VNMqTP0a55T4huBQQXuPIlj4iQtRYUd7MlFXhZSgLd8uILWu-XCKgrGmGmTW8kqmc7mn85JfmZrPMm1HD_hg93pVdjXHxB7ab6Eyc7dZ6X38gJC2wMzRHLzY_2fTAhdv-Oc893-8bB6Ep-QE724R_tGDUBPS7ap_OBNS-7VbfNt1yL2yQjPxdzgXdTtOmfNx9vBgFF-xIx3LKm1kAszrgmMzH5_DyWPvKB7rKDbfy4HeXD3POPkpwsdlGQGa96nFqzRG05D3gZgrLRy4ebnrLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sbii6J8WfaWhCcW-fV1TJOF7KLCVz7kWrTarv4Ch2vmQO2iT33UjPaELCSznHSIK8VcOfsDWdEZfzUS91BF5mGnzFhzEMHqCt5S0An4_5_GaFnSTnbjofqRIge6mu1LH8Sh0yclgcr4upCu8dpXa6kBjelgOro5s-To9819qle90rTIB9NIIhq_66NUhyawEv5kcWnS-QDtt2HMYzHCwE1TNFLQ-Fr5hTmS7jx1pFV31_XQHxXdl-eIpS-0U3if8h046cUfejRE4v6Z_Yfh3wM684UiMm__LXg77huWS0De2vbpkrK7LJ5vHRICK9Wz_-yl4zrps-QNu3NFRwTo10g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TO7N782eZ3Uj5_0wiP9p6olp0cWwc4vS5mUHNg2Jhjp0roHem9s_VZF9K1hcBZqHVipCHtQArC0Tbj0-VHGJRevs8_Dz8D-aQYZzLFJ3Axe96b6ifpY8zGYngiYkn3aLDftrQ7YvefdUoeUtte43gaMZq8ITHMdxd_AbHZRRFgjF-S0aAithTvivpfdje5kX5xVehcLuYqG8srVd_U0U5rdYfyxWhovfRg06NgIpXmDWF85mO5QgtZwdMlKt2i0hXvMMBaaVkNHxwr2FEWn7KR0h23JzDLnO2NpGSzJv-_0ZsbxCcFcpmOJ0G8W8ImcFNjPnUPZMKm8bsr14Ar1UtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZwyDQk9xLu5D877u39zWqz05UuDFZZJ0s43F0gmf9WYAnlFgHHLEdjIFtmw6MLCsVOYEOhUjBg0zohf1TXfdP0PT1sXd74EuKTr1FKVx_8eI15XnpXFbU7KOPfFJUFFcWn70POnbru7HeV3T5X20su1_1KLDGKZda_4Q3-fo2bXlrZZ1owNIbRULru-e2jNVu4zlS0v-U6K4imrutwfn1HyAaSQrlyf-I2oJHjzQUMMp2GPqtYHX7gJhVvyzY-K0K8we07V1fF-NY4MLxGqI4lepkCWZJsTSEKu8Lx3QpmjS6pkKz6GMwazs3Arp9FnFji5k3hYKINR_x5IesJ-kUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/slUFXitHS4K6RxWOM1PHcW9MxjRNujCY5pBNkk5IYQYDQowpJj1pnVm6Uksp_Lo9IIW6lAMSvKvtxeWZB4-kKW6NMCfLg4evjN2TaH3WjFEEmDtv_QBc-rv0tDfnR-_0CQRjN7IOE76H_646dnnsduov8WfFlaWVXb7aJA4hjtp2aaNrbgdNGGb6ieFW9kL5qHT8f8p1cEX9Wnc6ClCGeznbea0--4puPzn_XeHWseJhop5LUktOAeacdnbMXG4uTHwEtxp-Ju_rXD4yl5TK3XaVQ2fyvorLERO9l55IOV_m7FcBW_PuMR5U3Vf4iGKX2c_bcoCiZzr45if1M5eZIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/anoMxaCaxuYMSTpg9AVg2j22IPwkl-XD-aS3WmNu7451a-YjZVaPIcmeLEkDi3z0rEbUsn9zk6XQP1FSqvFYqZ9GRv8Nm8UPWX_dV08hmWwcM02RFwBu5mBhhFRWNL-V5eEj66dGQqZHgmKeymZf6cWHow_t_3cyS4KuVOWUSSf8U2snocbKts37WxdVxQIinXyA5oxqD4sfK1TkfZIPcqBiefJIgb_lm5xEjgU-5rJG5in_CT1oyBnPpDrMDp-zQPMnMblf6vGg51qdpoAiph80lGVcJkyuIf72lXnHpoqOkPXVKfs68BNRUvsOObVASpNsTprXxj2_lacxq5SM6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یک‌شنبه ۲۸ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/farsna/450984" target="_blank">📅 01:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450974">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PqVIRwfcU2VDyYe4Vq3EqU1e6PyHEpB0EQBBhRHZ3g3WJQO_O2JhRzFvseygvMuxbh75_GnHMScEdRSpL7ZJ301wEsxsf_j-pDtyiod87iUZ87MZsI3rsyLiOGmvCYHFKr7jlmXq38H8KkyNt1smGswTrFvRdJDBisON0BaqMN4PkBwFBMZH0OX_vZhGiw6NWQSnNBffYmgEDZ50FXh2wse3Rh5sphW72vySAjl2wl8Bt3MIq3DoTOj0-sBoWgis68lcQdGf4lVXiAPZtIzkLBvx-QSS1Pz06fKSk3lqS6wBcrbyZ8mYzSZzXfGpR7NRj_9FzBsCBrZH0jk93qxmwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2l-p8Ta-OJUu6kEWlnnNHTCFHnjTFNS5nAj07r6rVVXxvfxxQiSeP6VU0iGzSyzQrGRsUkjn18EXVzLuDVdx-OdVwFjl0Ix4rH7AlePtVmexBX3pO2Cck7CGX6y8u4zXezrqLApunOOXQZ1ReFTTfw7mRQgplXRZ3R-T5VWmy2cMUkQT_UZR245FyUSxkL5p70nJzOw4y-9HoKq3Rm-IscluvJmgYTyTYcwG1Yr48K9ylKNZ6HaKYoy7ObkkxG5zK62xAZe0EwehEd-m-8jp0s7biHMZewNUgf1GtE-LHn4EGUmi58SgebziL3TPqZWyWyGJQjZJ_GNwQTJDbefFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v81gZaj2aQuRlGM4QwqEbx8EGUZEvr7KuRI-W3WZn_TGtNq2rY8IJOwyLRhpe1VgATHyeiTjcp1E2cVzZ7MWjKi3OLhTGtjiHhXWCf5silqKiyGbf16AxGyESSC5TalzY8NLnBPEhhvlpuC3ksVwqci28Rt8peS5W5QuIyeCvtxvf-fbB5G12OvHiI7Kmuk8Hmwm4gyWAoaqCX6432BdsEVmmMIaI3MZRNLbz0rkRGWkaPZzT_5_YvvX8w-Zu4ZBCNVehYGdI4dZDI_uMuy5K4nczqS8Fp1AEhwj1dJza7ACg5rsbsDl81InlTJ0HmMbwvDQB4UTPh3tbmCHrjenuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egQJO_gdHSUaHyjT75sdBSRn-4HmFcrSJdDK3ZZgn-SxzyaB5sw-N28m3Y3EIHl3FeQPf3XCXO6Zm5qdsu-4oUeBEsVfyErWx3ysgRbHZ1LtdVMaUgCQXtM0S6OKrbwBDKOq09OUq-ZENEr7huwv7MM3qQH0T6DHWJQ0VNzzjmkm963-IG9hvC1LH6yXYdFa-5cRG8e-kLUGVLmeVNYi2gtioOz_iZtaXMwi6HBpE6w2yVllqMhuwPMs3XNhARQVTLsa3i3s3bLoheSkZollAWOgCr3hcOZeXDm1IsPpgCUdCGbaTNDnEF76NJ6V0u6DzSO_WqJMh0BTRqDdwCU3VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E255wLxMiqioI2l0hVUBhZcZ255tYtUZ2gpcqT-QiKZQLj31RwFlYDT02Av4ZFGikMPdYS5G-FfbOWg0BMIHxVCpu6RGMPnLdxxEUdnAM_NzXeZklq5aLWCtLNwlmBYWv_x69S4WHJsoCek9ruc8YBp3I0foe4Ia8930Jl4oMV-1fpClwqXjrbXzWK2sxVjAQ2lqb7f_UZpf_1DEdbX4hFbIDhBrBVoXyy6tAANiNw61vUPJ5rBNW6bBVVIFOjpWmy5cmimrA5Zhn6XxzvOOu1kYTOsMLn2eMHsxm_w1bP11Gkel814NPfChd5N-AcuevcisFQZoosmWBrBHryyEjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jVS5VBSFglgQ2qPZsRhCNVv0cP-4b2SpHH1TwUOHWDXAhDYxTzFdff0BpNBvJHgGQDycuHlYZu98ROiSdEeZaJFq4CINyM0zdVwJ7-Yr4VzfdXiOJfs16nem4DhIsla-NcEEijOi_qDBSS94gCemSjWpLHeKLlhpnGZXmFtxpjfMu0AsAs1H9FqFtileiF-_VfrEGoyHXRRRo_48gBe0FOLiTF96TZZ5BWlxZXHfAaPiFnxbrmJHN2xcY28BPMDogqpMBKomHi10axdRz2OQRF_ecS87_L9l6gLOplKqV0tjUsHpMWc84KFM3vzLTxWji0ffb7I4K1-6-0GlvSvL0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cCVI0Kf1L7ovuQP3KcIwyYgrZRw7jzgCnspSfs7-znWsQ0rUfTM6O-qPeMiRcVmKDkzvCvjnQd4v97BrhUEvkAYSd4PndYOhKkyp-rs27z2hT2pfv-yTXWWRWB08bYwpsuVasgRR3AjheEecEW-_dzZ1rBePD7J7SKZE4jFYkHM4fckI7j_i7vdPjI9CnI_NznVkGkwRXjxciBW0_u0rWF1DsWoPrLQPyDgKKFbLElTx912vK2z7iQVEpDZygF6ENDTHgasmvTB1gIKZeXnVQNT3QTZ5wGGAry80EDAg2ngGk1QuYHQeK5hmHy7fGAzbj0hrL33ifzsmcxXIf5N64g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xtmiubv5XHKuZSw5fPSNzuD-oSJ0HnE35llTSTiiHiDVg-n7bivH_B3KJ35rZZEBxlwk8t-m2Te1uBwrVqXbpc9-xDzR2ps9A_G0-BnoX5Ch09zSANaEa6e8wjQb_1XXOa00X6HPEUKKIha7iH8C5R1xnz8HCkwB9iOnlw203wewjlgE2LBZAEWkHxqYO19toproEjwD3HoGSnjDwm0ieYrTiar-8BlMKpP6pyAxct2ZvtEdGipFmGCxga-38Fj42eAywnl9RRVzHeJ2P93-mD6qzDdTY2a77FKdE9NbdoBj3ll3qBS-DxnUNZe3LjjQ8pj6OP3JwyqkIntlEezD8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vheqp6KWLro8-AylXXURcD9WrCA48NzwVqqb9FCB5c_vmRuTtTwdYz0_sm8dLCL64DI3XYqpG_82jqljk_1H-wBFaizkPP9D2HEo8L_WSqRx6f2rjI2k7_3r2SksQfHv_1j8tDVLQK2lTtbUOPSCk6VosbFC9keNj4I2-7ymaq9E-8yP_aNZj8Ds4fi-d7DlBQFt-AB4ifXHEoxA10yu8LKKnJhg68WlKm4zh3RV6CrbRFx7OOZP6BE_fQ-SKlsbnhupclXSIKAtmv21Gm9P_zazd0876LeiMmBxtaVzFmYCf45SBGQmagbi1kjdrCTk_JM8Itv8t1pUnsAB14f5yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Klp1ji2vHBw1Z9MkghTQ7KcxCaPgKoURvYdvA5LAwvNhVxE3h-NMpX40_7FKI_25HlK3qH4OlZscgGcxNFt99VIym3Mqxu2vt_FYi23E00EMJiMcZ7z05LJubE3fut8DbAIwqEYSfJR0sWSSunxzPffvKM1_PTf5Og75wfV9sG-KFscbm1eSbqI-Vd9V9c6fu5okrNv7OU7Rk75qGFRUW9EO0_iMZO-o1oY9ojzBEuQS9p8Ihdpw0rVeVHNad97aiqpRXhzoJW1QDS-nfbUHVPk03cO3VwnPWZ66F8bdS7djQO9k9C3z9OnsinByLn6rrXI6YCArIvzsq-KFFT82lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/farsna/450974" target="_blank">📅 01:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450973">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f62fe2e92.mp4?token=vpIs2_OAjmjUo2S2NMo6djpgpxWEDyHRm48tGa14rFIKJjlHOzNaEOr8VO_cdhyehU0tEKDa6KPr_lh4n-L3rXh_xX9MRrRotIo6xh1IeaWJ6nkjt3fezuNRs9mIs7hrVlBmcb9elswvZKOFFWyXEh6siRZUqrHwvNazb_cg5MwlWcnkc2_HrdyTnZ4lrXRcRo6pGmRtTz-CXmZZwlW8eaP8VxEp4eDNWs_M6ytuh6-8dNn7ujk6nggTq27CamyNbhm9Du3OHa4G2FaN7gOM1G57DOg6t5jybeKUnKzEi041acP0oZScgbYlvNlOTswzyRa2gMROVUBJBWk39yxu8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f62fe2e92.mp4?token=vpIs2_OAjmjUo2S2NMo6djpgpxWEDyHRm48tGa14rFIKJjlHOzNaEOr8VO_cdhyehU0tEKDa6KPr_lh4n-L3rXh_xX9MRrRotIo6xh1IeaWJ6nkjt3fezuNRs9mIs7hrVlBmcb9elswvZKOFFWyXEh6siRZUqrHwvNazb_cg5MwlWcnkc2_HrdyTnZ4lrXRcRo6pGmRtTz-CXmZZwlW8eaP8VxEp4eDNWs_M6ytuh6-8dNn7ujk6nggTq27CamyNbhm9Du3OHa4G2FaN7gOM1G57DOg6t5jybeKUnKzEi041acP0oZScgbYlvNlOTswzyRa2gMROVUBJBWk39yxu8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انگلیس در دقیقهٔ ۳ به فرانسه گل زد
⚽️
انگلیس ۱ - ۰ فرانسه @Farsna</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/450973" target="_blank">📅 00:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450972">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMDXUOn-xlEb-xrCzwaJeI_xVF3mpfZgV8E87gvSS9owQmaWJmDZ_aqsGFdYlD15fFsliA_IMFlQ8Tpb6-XuBHGWR9Iky--PMiv9JqyND8I-0RTxF3sZawvhVrj87rvZNv2FW_fHZlkTIIK5vXFzzGrJA35EsFwQ906Yt-fTD22kpKSHZQrHQjZKMGQJvTxj9iUL5cwaxluH12hro9VeCRbX1X-nVfjmHiGy6fPSVI0fWEsAzuBQbXNW2IxnAwdSyYR_U9S91k9J8NsPWL1-p7OJlc98H_mw9LDhrbm-tSIKKYnWChP76c4kNUW2MxLswEviC4dXafBWVB0KCucLvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزلۀ ۳.۷ ریشتری سرگز در استان هرمزگان را لرزاند
🔹
ساعت ۳۰ دقیقۀ بامداد یکشنبه، زمین‌لرزه‌ای به بزرگی ۳.۷ ریشتر حوالی سرگز در استان هرمزگان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/450972" target="_blank">📅 00:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450971">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎥
الیوم یوم‌الانتقام
🔹
فریاد خون‌خواهی مردم بندر دیر در صدوچهلمین شب میدان‌داری خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/450971" target="_blank">📅 00:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450970">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b1a55d0ee.mp4?token=nJpWm95tWVSh1OmDJvOy8nX8cNZDQ2DoE9UoI8Uh0M7JpmLV8ObMYQw0ziTW0NziY-GTM16cym0CnXHby9y5CMx-T1mqyAgZT82iVtIox3ZskRlW9ecmhBiy6f4nsGAD1rNJ0xaR3hmTxptEI4k61ODpYxbnqKqzJnNcFbY-DF5DTxxAJpmNx3cgx00zMfyHX6i2eJ50mYl7qjR0OszYOL8F22ESUEfrgpuF6hj1iHzidev8UFrQQzCAr4y1rjdd-Bi6tZJ9eGPQnN0ZUKz3GTWmYdx5ZFihYp1atp1SGw5orhuINvRyrobpQS2JERqvW0Y9tmQPYu7E4Bz2ysXlRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b1a55d0ee.mp4?token=nJpWm95tWVSh1OmDJvOy8nX8cNZDQ2DoE9UoI8Uh0M7JpmLV8ObMYQw0ziTW0NziY-GTM16cym0CnXHby9y5CMx-T1mqyAgZT82iVtIox3ZskRlW9ecmhBiy6f4nsGAD1rNJ0xaR3hmTxptEI4k61ODpYxbnqKqzJnNcFbY-DF5DTxxAJpmNx3cgx00zMfyHX6i2eJ50mYl7qjR0OszYOL8F22ESUEfrgpuF6hj1iHzidev8UFrQQzCAr4y1rjdd-Bi6tZJ9eGPQnN0ZUKz3GTWmYdx5ZFihYp1atp1SGw5orhuINvRyrobpQS2JERqvW0Y9tmQPYu7E4Bz2ysXlRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انگلیس در دقیقهٔ ۳ به فرانسه گل زد
⚽️
انگلیس ۱ - ۰ فرانسه
@Farsna</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/450970" target="_blank">📅 00:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450968">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiVVGtboj2yV-sgjjIwKwfKaJkKvC7AMKfTW1-k8_jqifwmK34PRTTLxYugwWVrL_mngQeMj38Gbv-1uOdJe8DcBFA3dg2ZWXRqFaehp6Cg5Q0ywA8-DmJKWTd8pux3vPRXaUvGsRGO6x38tjmiCRgNCavvcVn_tUvtrZKMVayo-_89UbLURayl8WMR2zYSOL3B5Vf4KM8AjR2If7r-nTkGpy_M0tmnVC9SDuJlltWZYHdvVZkwa3qWlGA7DSvGj35BXuVPYYp9gCQoG78-v5GPrKf_Y16UGcDk81I84db1XF1M5DTkw2-EcFz6ugi7_AJ2nsbTjkdDQAz9yUIzp-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربه به شریان نفتی جایگزینِ هرمز در عربستان
🔹
در حالی که عربستان برای فرار از بحران تنگۀ هرمز، صادرات نفت خود را به بندر ینبع در دریای سرخ هدایت کرده بود، گزارش‌های غیررسمی از خسارت به تأسیسات نفتی این منطقه حکایت دارد.
🔹
هرچند ایران یا یمن یا طرف دیگری مسئولیت این حملات را رسماً تأیید نکرده و مقامات سعودی نیز جزئیات روشنی دربارۀ ماهیت حادثه ارائه نداده‌اند، اما منابع غیررسمی از خسارت به تأسیسات نفتی در این منطقه سخن می‌گویند که می‌تواند زنجیرۀ صادرات نفت این کشور را با اختلال مواجه سازد.
🔹
بنا به تایید تحلیلگران هرگونه خسارت به تأسیسات ینبع که اکنون به‌عنوان شریان اصلی صادرات نفت عربستان عمل می‌کند، می‌تواند قیمت‌ها را بیش از پیش افزایش دهد و ثبات بازار جهانی انرژی را با چالش جدی مواجه کند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/450968" target="_blank">📅 00:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450967">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‌
🔴
نیویورک‌تایمز: حملات چند روز اخیر ایران به پایگاه‌ آمریکا در اردن باعث مجروح‌شدن ده‌ها نظامی آمریکایی و آسیب‌دیدن تعدادی از بالگردها شده است. @Farsna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/450967" target="_blank">📅 00:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450966">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌ وال‌استریت‌ژورنال: مقامات آمریکایی می‌گویند ایران خود را با سیستم‌های دفاعی آمریکا وفق داده و موشک‌هایی را شلیک می‌کند که با سرعت بسیار بالا حرکت می‌کنند و هنگام شیرجه به سمت زمین، قابلیت مانور دارند. @Farsna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/450966" target="_blank">📅 00:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450965">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🎥
پنجرهٔ متفاوتی به تشییع باشکوه پیکر رهبر شهید انقلاب بر دستان مردم عراق در کربلا
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/450965" target="_blank">📅 23:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450964">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آغاز دور جدید عملیات روانی دشمن با ۳ محور هم‌زمان
🔸
ارزیابی دستگاه‌های اطلاعاتی حکایت از هم‌زمانی ۳ جریان در روزهای اخیر دارد: تشدید القای فشار اقتصادی، تحرک رسانه‌ای هماهنگ برخی سلبریتی‌ها و افزایش مواضع انتقادی چهره‌های سیاسی.
🔹
آنچه ناظران را نگران کرده، شباهت توالی این رویدادها با روزهای منتهی به وقایع ۱۸ و ۱۹ دی‌ماه ۱۴۰۴ است؛ الگویی که در آن زمان نیز به اغتشاشات انجامید.
🔹
در این میان، آنچه بیش از پیش قابل تأمل است، هماهنگی زمانی و محتوایی این سه محور با یکدیگر و با تحولات میدانی منطقه است؛ هماهنگی که به‌سادگی نمی‌توان آن را برآیند طبیعی فضای نارضایتی دانست.
🔹
تجربهٔ گذشته نشان داده که شبکه‌های معاند و سرویس‌های اطلاعاتی بیگانه، همواره با طراحی سناریوهای چندوجهی، از بسترهای معیشتی و مطالبات به‌حق مردم برای پیشبرد اهداف تخریبی خود بهره‌برداری کرده‌اند.
🔹
بازخوانی وقایع دی‌ماه ۱۴۰۴ نیز مؤید آن است که آنچه در نگاه نخست، اعتراضات خودجوش به‌نظر می‌رسید، در پشت‌صحنه از هدایت و پشتیبانی فرامرزی برخوردار بود.
🔹
شباهت‌های ساختاری این روزها با آن مقطع، ضرورت هوشیاری مضاعف را پیش‌روی نهادهای امنیتی و افکار عمومی قرار می‌دهد تا اجازهٔ تکرار سناریوی تلخ گذشته داده نشود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/450964" target="_blank">📅 23:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450963">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">📷
نمایی دیگر از حملهٔ موشکی دیشب ایران به پایگاه آمریکا در اردن  @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/450963" target="_blank">📅 23:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450962">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPpRPJM6nZVc5_AUVeIIk4gFllQHfU0yYKutcbBeEc1f-4ABlVvUkRmmmcq5My6lutAP5JsL-6upL_J9RNu698cDFkF2iMLKGQ1Lm_B8xUDDCI9xIuOgP3vOvlLmHfK_LSGtKzRblAUlI8krhtenrDgqBluiVzu6tfizk1TIuLDR1LL1ahfC6EM5xoC63gZHTEXkkOXVPUG4oI0d-KZsIn1see-xAcUxLIHYiWU82Lbad-MR276-lxjtfFaCaMJrwKs0ioNGNSGfXLN4F5YGjMAldFWY2s-683E7kNzJFJ4H64fkiBhXHKqjd6N5rB4zkUrfn7QT1UDcKVEck7IpGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصاویری از حملات سنگین موشکی ایران به پایگاه هوایی آمریکا در اردن  @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/450962" target="_blank">📅 23:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450961">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
هشدار یک مقام امنیتی در گفت‌وگو با فارس: در صورت حمله آمریکا به زیرساخت‌های ایران، فرودگاه‌ها و بنادر امارات باید فوراً تخلیه شوند
🔹
یک مقام آگاه در نیروهای مسلح در گفت‌وگو با خبرگزاری فارس ضمن هشدار نسبت به پیامدهای هرگونه اقدام نظامی آمریکا علیه ایران…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/450961" target="_blank">📅 23:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450960">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgUe_fIfevEXpYDhsLNutS2p9cmOX1Vf9BV6WeWUmKZUwbcO21fGRikzCznYnSAQFsbP3yScll5ldb-4Ucl7XUhwu8eC91zWHXNDqj0SfS4yXzMo09myzwlKVgLTaLrRbsq28D4rpniTNXlc_kAficUyRHBbQuVcXV_6iPoXwi925n8waUQHF_dcBxSrY4En_5ElWHTBY2VzThZkzElp1DbKXQANyJ13gj_PVjj9MChpu7SDrDkSOczIesYQ-fh24G73IsNl3jT8hksG6n3fv5F1Qa3t_z45ptNxez6SxfLggAATkOqjw-6LWfyzESTIut_t3yJZ1vJO4DkNPzRNrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انقلاب: مردم مؤمن عراق در استقبال از قائد عظیم‌الشّأن شهید حماسه‌ای عظیم و پرمعنا آفریدند
🔹
به محضر شریف مراجع عظام، علمای معزّز و اساتید و فضلای حوزات علمیّه و دانشگاه‌ها، اندیشمندان و نخبگان گرانقدر، اُمرا و سران قبائل و شیوخ عشایر و سران طوائف و مردم…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/450960" target="_blank">📅 23:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450959">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_XNZvFbm8YiB3SQ7leq1cAp_H-N3OdcB3zPaCYaddLEqSq__Hlo_J8-c9a0RvmXp6-4VuWPwcBVQ63uF14JriWNmyKWcuOnfpSKRoj7V2EDnd7YVuP7qrfeLTljIEeW52_qvZpeX1VuJ7a93_zfAID939XBOIcrQyPkKi7wauoZ4F0iHlXT1T7Z11sUK3aIBP7c2O1O-xZFvnNWvC4ppy_MnhV8Zi_HIomjVcIb5WA5OP311ukSvdhSxt1aSDNO-WHvHkpiKFP9xPdqBbePagnFbY7sQAVEzFohih42htV6xYC1b8DNlnZib2ujavZQuItpdrm0wXyHsSt37Xjumg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر معظم انقلاب: تشییع میلیونی و بی‌نظیر علمدار مقاومت، فصل جدید تغییر معادلات مستکبران را رقم زد
🔹
بی‌تردید سران استکبار با دلهایی هراسان، تصاویر صحنه‌های باشکوه این اجتماع عظیم در عراق را مشاهده کردند و دیدند که چگونه سرمایه‌گذاریهای کلانی که برای تخریب…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/450959" target="_blank">📅 23:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450958">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrAZZQ952VgU2fcVHAuLj3h9zVZt2h1w3uFdCamWsS0RABQ2JRhlZHwfEUoEzDxI5LXQfS1QnmRVvXW6gmNXUne-oSTUl6T8fLZJQmxJgEoHyxYsouiHlfazgz71-713ZbgYGdebLTdcqPmPshM1gkcvdtIzLFBlwJqd0zLkMkV75JqhRiEPBFy4vn3S4dPR4qnybIR4eYpWSWqUcM_pa28-aZV7irsgkX_-A8He8X6v503OpnwUcTOqZk-fThYyxlIVDXjorw5-c9glTDVBWTXowyXxdR7gz2goO7EbPFBztH03PcsBhIbu0pTNTsbMWpBYUVrG8NajZfYvC-5oDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تا دقایقی دیگر پیام قدردانی رهبر انقلاب اسلامی از ملت عراق به‌پاس حماسه تشییع امام مجاهد شهید منتشر خواهد شد.   @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/450958" target="_blank">📅 23:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450957">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-text">🔰
#یادداشت
| هرچه فریاد دارید، بر سر آمریکا بکشید
📝
تبیین مضامین و نکات مهم پیام راهبردی رهبر معظم انقلاب
🔸
پیام امروز رهبر معظم انقلاب در شرایطی صادر شد که ملت ایران هنوز در فضای حماسه‌آفرین
#تشییع_میلیونی
امام شهید قرار دارد و از سوی دیگر، بار دیگر با نقض تفاهم‌نامه امضاشده میان رؤسای جمهور ایران و آمریکا از سوی ایالات متحده مواجه شده است؛ نقض تعهدی که با اجرای دوباره محاصره دریایی، تجاوز به خاک ایران و حمله به مراکز غیرنظامی از جمله بیمارستان کودکان سرطانی و زیرساخت‌های حیاتی کشور همراه بود. در چنین فضایی،
#پیام
رهبر معظم انقلاب صرفاً واکنشی به یک رخداد سیاسی نیست، بلکه ترسیم‌کننده نقشه راه ملت ایران و مسئولان برای عبور از این مقطع حساس است. این پیام را می‌توان در دو محور اصلی خلاصه کرد: حفظ انسجام داخلی و
#ایستادگی
قاطع در برابر دشمن متجاوز.
* حفظ وحدت، وظیفه همگانی
🔹
نخستین و مهم‌ترین محور پیام، تأکید بر حفظ وحدت کلمه و
#اتحاد_مقدس
ملت ایران است. رهبر معظم انقلاب، صیانت از انسجام ملی را مهم‌ترین سرمایه کشور در این مقطع دانسته و آن را مسئولیتی همگانی معرفی کردند:
«صیانت از
#وحدت
و پرهیز از تفرقه و تنازع، اختلافات سیاسی و برجسته کردن تفاوت‌های اجتماعی وظیفه‌ی همگانی است» ۱۴۰۵/۰۴/۲۶
🔸
این تعبیر نشان می‌دهد که وحدت، صرفاً یک توصیه اخلاقی یا سیاسی نیست؛ بلکه یک
#ضرورت
راهبردی برای حفظ عزت، امنیت و استقلال ایران است. تجربه روزهای اخیر نیز این واقعیت را به‌خوبی آشکار کرد. حضور تاریخی و میلیونی مردم شریف ایران در تشییع امام شهید، جلوه‌ای از همین
#سرمایه_اجتماعی
بود که نشان داد ملت ایران در بزنگاه‌های تاریخی، اختلافات را کنار گذاشته و حول منافع ملی و آرمان‌های مشترک به میدان می‌آید.
🔹
رهبر معظم انقلاب در ادامه، نخستین لازمه حفظ این وحدت را
#اعتماد
به مسئولان دلسوز و حضور آگاهانه و فعال مردم در صحنه دانستند:
«ملّت عزیز، با تداوم بر اعتماد به مسئولان دلسوز در هر سه قوّه، همچنان برای تضمین صیانت از منافع ایران اسلامی،
#هوشیار
و فعّال در میدان خواهد بود.» ۱۴۰۵/۰۴/۲۶
🔸
در کنار این توصیه، پیام به یک مرزبندی مهم نیز اشاره می‌کند؛ مرز میان
#نقد
مسئولانه و تخریب وحدت ملی. رهبر معظم انقلاب ضمن ارزشمند دانستن نقد، نسبت به دو آفت بزرگ هشدار می‌دهند:
«باید [منتقدین] مراقب باشند تا این رویکرد، اوّلاً ظلمی را بر بی‌گناهی روا ندارد که آن خود منشأ محرومیّت از برکات و عنایات می‌گردد؛ و ثانیاً موجب شکست در وحدت و
#انسجام_اجتماعی
نگردد... دشمن نباید هیچ علامت ضعفی و از جمله این ضعف را از ما دریافت کند.» ۱۴۰۵/۰۴/۲۶
* درس فراموش‌نشدنی برای متجاوز
🔹
دومین محور پیام، ناظر به تجربه دوباره
#عهدشکنی
آمریکاست؛ تجربه‌ای که به تعبیر رهبر معظم انقلاب، بار دیگر نشان داد امضای رئیس‌جمهور آمریکا هیچ اعتبار و ارزشی ندارد و ذات آمریکا همچنان بر پایه زورگویی،
#وحشی‌گری
و فریب استوار است:
«امروز شیطان بزرگ بار دیگر چهره‌ی واقعی و بدون نقاب خود را آشکار کرده تا این تجربه‌ی تاریک از جنایت و بدعهدی، سند محکم دیگری بر
#دروغگویی
، غیرمنطقی و غیر قابل اعتماد و پلید بودن آمریکا باشد.» ۱۴۰۵/۰۴/۲۶
🔸
اما پیام در این نقطه متوقف نمی‌شود. در کنار افشای ماهیت
#دشمن
، راهبرد مقابله با او نیز ترسیم می‌شود؛ راهبردی که بر تحمیل هزینه به متجاوز و تبدیل تجاوز به شکستی پرهزینه برای آمریکا استوار است. رهبر معظم انقلاب تأکید می‌کنند:
«ملّت عزیز ایران و جبهه‌ی مقاومت،
#درس‌های_فراموش‌نشدنی
برای او دارد که رشادت‌های رزمندگان اسلام و غیرت مردمان شجاع خطّه‌ی جنوب در این روز‌ها نمونه‌هایی از آن را نشان داده است.» ۱۴۰۵/۰۴/۲۶
* فریاد واحد ملت ایران
🔹
این پیام، در امتداد همان واقعیتی است که امروز در
#میدان
دیده می‌شود؛ از یک سو، ملت ایران با حضور میلیونی خود، انسجام و ایستادگی را به نمایش گذاشت و از سوی دیگر، فرزندان ملت ایران در نیروهای مسلح با وارد کردن
#ضربات_سخت
به پایگاه‌های دشمن، نشان داده‌اند که تجاوز بی‌پاسخ نخواهد ماند. از همین رو، روح حاکم بر این پیام جمع میان وحدت در داخل و اقتدار در برابر دشمن است؛ پرهیز از تفرقه در درون و افزایش هزینه‌های تجاوز در بیرون.
🔸
در حقیقت، پیام امروز رهبر معظم انقلاب را می‌توان بازتولید همان
#منطق_تاریخی
امام خمینی(ره) دانست؛ منطقی که در برابر دشمن متجاوز، جامعه را به اتحاد، حضور هوشمندانه و مقاومت فرا می‌خواند و اجازه نمی‌دهد اختلافات داخلی، سپر دفاعی ملت را تضعیف کند. خلاصه این پیام در یک جمله تاریخی
#امام_خمینی
(ره) متبلور شده است:
«هرچه فریاد دارید، بر سر آمریکا بکشید.»
@rahbari_plus</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/450957" target="_blank">📅 23:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450956">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/678ff98030.mp4?token=AuyRBFs84sFDzdbf_K374YYZ33d92d6FSBlJvG04OlNvzBKvICF5NAiPuGl1iSVhrizwT7CKOj18TfZe6ZnL8lTv38l-Mb6r0lu7Rrj2C6PdHhQry8yyKor-KSMR2VGkiENv9Zw-KrwaXrlZZVskRAXlFb2qyi2EwBZt1CwWmbgawfLLLi-uy21Xsny53tf-dU0xLTBLxMOXEU-qfIYhcpys-393rbfOwS32aeUYG-mbifi9H_fs8WMmwW5bSIaLBROeyWrRdJ317EaT_G5p5NchvLULf6FbtKpYrkykwtMKUEkIXkdTGQhUFHxw_4l0P_ON18pzudyaGG75TeFsjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/678ff98030.mp4?token=AuyRBFs84sFDzdbf_K374YYZ33d92d6FSBlJvG04OlNvzBKvICF5NAiPuGl1iSVhrizwT7CKOj18TfZe6ZnL8lTv38l-Mb6r0lu7Rrj2C6PdHhQry8yyKor-KSMR2VGkiENv9Zw-KrwaXrlZZVskRAXlFb2qyi2EwBZt1CwWmbgawfLLLi-uy21Xsny53tf-dU0xLTBLxMOXEU-qfIYhcpys-393rbfOwS32aeUYG-mbifi9H_fs8WMmwW5bSIaLBROeyWrRdJ317EaT_G5p5NchvLULf6FbtKpYrkykwtMKUEkIXkdTGQhUFHxw_4l0P_ON18pzudyaGG75TeFsjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری که گفته می‌شود مربوط به شلیک موشک‌های بالستیک اتکمز توسط نیروهای آمریکایی از کویت به‌سمت ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/450956" target="_blank">📅 22:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450955">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97eb2b198c.mp4?token=H6kcV7Ya8Khe5nHoOLd5gNJY13u0CSbzPbwEcybHaMPb4REh6NDA2TLQ4-p1Xyqe42MXE0A4_ep-BZu7467vWeqi1LkIfp-LT3O3i_tfKr2Bhr7ApI2mpcqngJQYl_mT_6JvpifQEirBd19yFeHFSGK7PP9-w4G16RtpNvwrcjN8NqtEPQ_mgC0-1gvPJimgOTLpC8yd5k-MinAeHm4KMCsqd82juYpUte7mtlti_HXX2tgW1de7tzBq9m3O64_23FiRjaKD7w_hWPFzp1u_ZMZOhcnRHD2Np0_FIOvSJicckRuAxwbQNrLzNwGCvI-RJOc2fB51GhZhosRrClyvmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97eb2b198c.mp4?token=H6kcV7Ya8Khe5nHoOLd5gNJY13u0CSbzPbwEcybHaMPb4REh6NDA2TLQ4-p1Xyqe42MXE0A4_ep-BZu7467vWeqi1LkIfp-LT3O3i_tfKr2Bhr7ApI2mpcqngJQYl_mT_6JvpifQEirBd19yFeHFSGK7PP9-w4G16RtpNvwrcjN8NqtEPQ_mgC0-1gvPJimgOTLpC8yd5k-MinAeHm4KMCsqd82juYpUte7mtlti_HXX2tgW1de7tzBq9m3O64_23FiRjaKD7w_hWPFzp1u_ZMZOhcnRHD2Np0_FIOvSJicckRuAxwbQNrLzNwGCvI-RJOc2fB51GhZhosRrClyvmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جمعیت شگفت انگیز مردم هشتبندی هرمزگان در ۱۴۰ شب ایستادگی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/450955" target="_blank">📅 22:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450954">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/804e907130.mp4?token=GgR2wGYzsr47yw9GfpA9l0uDP_EXcsyH0M1_DKZuxG4c0HA2SAj0I4dy2RmbCr6eBAQFckNfRzQdOx77CzeclDS7crJCclR1lvVQLukA_RFtnun6v4gOnJbKXhs7ApqB3SkXOFDEJQ2HiagZr_NYowqf7OSY7GhL_sPyksV6iMs3Sb-ICnGWrZez6YGV2-n1CUpwf2wxGMh9hnguSsTZKqCX50_tSh-XBV7QhMg93Co0tR4WivhKfsKiPA12Y17JLtv68vw5f_tve4zLPXW6Hey95IGkyaZFN2U3s9n1EwGKIgq-j7A17UYF0Qmbs2BEXMQGoH6hqNyLZg2A3ZuiQo-bgneDGwn-Skz7_F5wTIabyN5Fufyj53g4GUt0wsZSdOif71BdQcT2HtWIT8KYJV5zWMaK6L3A2YDqVs-oejiGjWRTnq7aWwiVctaAv0kUN4e-IeqepBXFAFmPKzJC0e3Etz2OdUMd1Qhuz7CtjziMqcjY-nyg81rwQ9G7piZWLdheGclUYyTE7HpNWhrvaBAa7V0f6vO-iUG42AuX8Z6YBLrD8NdhH5KhUqm8bk-0qI-wuUvP3B48mfuVU3rZfnWjnTLtRI1sVWQzfciY2LDkhnjeCi1OOmyCQqSz6LrhmOW1yWhi9t_hZ0iDDhCTNZhlEnjA-5zVfHybngp6Pv4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/804e907130.mp4?token=GgR2wGYzsr47yw9GfpA9l0uDP_EXcsyH0M1_DKZuxG4c0HA2SAj0I4dy2RmbCr6eBAQFckNfRzQdOx77CzeclDS7crJCclR1lvVQLukA_RFtnun6v4gOnJbKXhs7ApqB3SkXOFDEJQ2HiagZr_NYowqf7OSY7GhL_sPyksV6iMs3Sb-ICnGWrZez6YGV2-n1CUpwf2wxGMh9hnguSsTZKqCX50_tSh-XBV7QhMg93Co0tR4WivhKfsKiPA12Y17JLtv68vw5f_tve4zLPXW6Hey95IGkyaZFN2U3s9n1EwGKIgq-j7A17UYF0Qmbs2BEXMQGoH6hqNyLZg2A3ZuiQo-bgneDGwn-Skz7_F5wTIabyN5Fufyj53g4GUt0wsZSdOif71BdQcT2HtWIT8KYJV5zWMaK6L3A2YDqVs-oejiGjWRTnq7aWwiVctaAv0kUN4e-IeqepBXFAFmPKzJC0e3Etz2OdUMd1Qhuz7CtjziMqcjY-nyg81rwQ9G7piZWLdheGclUYyTE7HpNWhrvaBAa7V0f6vO-iUG42AuX8Z6YBLrD8NdhH5KhUqm8bk-0qI-wuUvP3B48mfuVU3rZfnWjnTLtRI1sVWQzfciY2LDkhnjeCi1OOmyCQqSz6LrhmOW1yWhi9t_hZ0iDDhCTNZhlEnjA-5zVfHybngp6Pv4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قزوینی‌ها به فرمان رهبر انقلاب همچنان حافظ سنگر خیابان هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/450954" target="_blank">📅 22:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450953">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🎥
تشییع باشکوه شهید سیدفرشاد علوی از شهدای پادگان ارتش در بمپور در چاروسای کهگیلویه‌وبویراحمد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/450953" target="_blank">📅 22:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450952">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
تا دقایقی دیگر پیام قدردانی رهبر انقلاب اسلامی از ملت عراق به‌پاس حماسه تشییع امام مجاهد شهید منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/450952" target="_blank">📅 22:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450951">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‌
🔴
اعتراف سازمان تروریستی سنتکام: ۲ نظامی آمریکایی در حملات ایران به اردن کشته و ۴ نظامی مجروح شدند. @Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/450951" target="_blank">📅 22:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450950">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36c0d531ea.mp4?token=OZfoKl5DM2_dMtdXW2HXOOqr1Ve-ZkxDjUYDJ9ZJ1PxGEMC7VmV64Cb9Dl6xlLjwUMtg0kXav9pFveE0EVSB4vDvudbUVrkrThEsg2MGpwzTriiCEI56pac_uDFVdBlq9TQZGNkuc_PD5wXQ99wwWtihE5w0y360pjObudaqPbcq5CZeB20o4ZNMrckg0_KAMBNJn7XoPuBlsVO3OK8U-0EpflcdVISV0gWi0bYESkBIo6w2w-X7ylYeLhdjaoKFuoRSR6gSrcq47kb6lltW3USYdoqv8PBDU8r7xz21ReGO5s72-fYqFBJC6_AdsMbPcNnzUvkY1AyYxwDh2O2pOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36c0d531ea.mp4?token=OZfoKl5DM2_dMtdXW2HXOOqr1Ve-ZkxDjUYDJ9ZJ1PxGEMC7VmV64Cb9Dl6xlLjwUMtg0kXav9pFveE0EVSB4vDvudbUVrkrThEsg2MGpwzTriiCEI56pac_uDFVdBlq9TQZGNkuc_PD5wXQ99wwWtihE5w0y360pjObudaqPbcq5CZeB20o4ZNMrckg0_KAMBNJn7XoPuBlsVO3OK8U-0EpflcdVISV0gWi0bYESkBIo6w2w-X7ylYeLhdjaoKFuoRSR6gSrcq47kb6lltW3USYdoqv8PBDU8r7xz21ReGO5s72-fYqFBJC6_AdsMbPcNnzUvkY1AyYxwDh2O2pOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۵ مکان در مشهد که رهبر شهید در آن خاطره دارند
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450950" target="_blank">📅 22:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450949">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فرماندار بوشهر: دستور تخلیه خارگ کذب است
🔹
تاکنون نه درخواست و نه دستوری برای تخلیه ساکنان جزیره خارگ صادر نشده است و مردم بومی در کنار کارکنان صنعت نفت به زندگی روز مره خود مشغول هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/450949" target="_blank">📅 22:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450948">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjASiaf49mGFcgagVUcvxiFziLBp8f8bZWx2cfbkDWi5AWCHjXGIWr7ZuL8d66eDmUeXmKclHj8UCKXN7gQgt2F0ZChcM8FbX5rGH2uEczg_jjGfez3mlB-_HRiB00PIwCA_AyZzlGHe0IA3YaC1TS899S6B6P1s502iFeyjNnMkXE29uh8EKlTm77GP5fCXkHuqbvK1ILccLIlFQz1djV68JendK3sOgDOenk9PqBeYJ4cd04ANRfKzoZlz8kaKXn8EhTwwQcqTtZpJFkaxH-kC3J4cJv4MPZHoB_6AZZFytzVWD6Veucacjm0_c7Tc7VQVBumzl4_Z_cJ8Q-J6ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: پیام رهبر انقلاب، سرمایۀ بزرگ کشور برای حفظ منافع ملی است
🔹
پیام حکیمانه و وحدت آفرین رهبر عالی‌قدر انقلاب اسلامی و حمایت ایشان از سران سه قوه و مسئولان کشور مهم‌ترین پشتوانه و سرمایه در جهت صیانت از منافع ملی و سربلندی ایران اسلامی است.
🔹
پایبندی به لوازم اتحاد مقدس و پرهیز از اختلاف و تفرقه رمز پیروزی در این بزنگاه تاریخی است.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/450948" target="_blank">📅 21:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450947">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f7289ee98.mp4?token=DXw3aAbcLspfoX5vmMLlSnS3ZaW7rtYPinT6iMdyKftNMfXhapJNK2NL8OD5dqz8FU5qEGRz80OJ4exmY5Pk4kGlcnRSdx0OkqFnBdi-D7BVsWveN-crG3dyxQm-ViAFOmvKnyg4dyfNd-jruCKFenmQaUOL25Yb1ZcltvtSP5BhASdeg7lLnvWUY6NDy5CSB6kLbEPKFLvsLwznKNb6jgAn__1GiLaNd_uSjCV-wo-6Fylv5H3MKEcRWvSXbwqb_mwM-ghYv1RHOfORzSxeBQFS5jQXKS1A5k7znnmWKXVwTydWUFkS1zj2p4PAhoApdVU1-MAuIxw1QzLrYPlvAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f7289ee98.mp4?token=DXw3aAbcLspfoX5vmMLlSnS3ZaW7rtYPinT6iMdyKftNMfXhapJNK2NL8OD5dqz8FU5qEGRz80OJ4exmY5Pk4kGlcnRSdx0OkqFnBdi-D7BVsWveN-crG3dyxQm-ViAFOmvKnyg4dyfNd-jruCKFenmQaUOL25Yb1ZcltvtSP5BhASdeg7lLnvWUY6NDy5CSB6kLbEPKFLvsLwznKNb6jgAn__1GiLaNd_uSjCV-wo-6Fylv5H3MKEcRWvSXbwqb_mwM-ghYv1RHOfORzSxeBQFS5jQXKS1A5k7znnmWKXVwTydWUFkS1zj2p4PAhoApdVU1-MAuIxw1QzLrYPlvAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربان یک ملت برای جنوب کشور
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/450947" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450946">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afdebd4732.mp4?token=WQlHaY9ZYftXtR37HMHSmR9fSlHbDa40gFJvgK1S6TWIKI2MeKz102lZRt2HrRQUV1Yauk_mJ_aRCUxiKds_PyQ_Dan-j1dxeT1FbuazLI8iAw4njevhCg18GpOqMFHvEyGu6ZzLotgfqZvY9_SHYl5tvJC4jRoX7RGjhYag9a-Fp94JLrGLcTSlydZ9BqlhqyV1JsK-v-IWAYnTQQxanAE182XYFNkF-EAbEsU3GhccFu6KVy3ELNuPIWxSMjoZk7UIWku4w8b1xRIWLU-h4S4TaAJqEMKYF8-Slt2ByqNrQ-fx-3O4RudZe5F6eAEuDnA5gZ7iFO47l8NAz6rcHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afdebd4732.mp4?token=WQlHaY9ZYftXtR37HMHSmR9fSlHbDa40gFJvgK1S6TWIKI2MeKz102lZRt2HrRQUV1Yauk_mJ_aRCUxiKds_PyQ_Dan-j1dxeT1FbuazLI8iAw4njevhCg18GpOqMFHvEyGu6ZzLotgfqZvY9_SHYl5tvJC4jRoX7RGjhYag9a-Fp94JLrGLcTSlydZ9BqlhqyV1JsK-v-IWAYnTQQxanAE182XYFNkF-EAbEsU3GhccFu6KVy3ELNuPIWxSMjoZk7UIWku4w8b1xRIWLU-h4S4TaAJqEMKYF8-Slt2ByqNrQ-fx-3O4RudZe5F6eAEuDnA5gZ7iFO47l8NAz6rcHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سازمان تروریستی سنتکام: یک نظامی آمریکایی در حملات ایران به اردن مفقود شده است. @Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/450946" target="_blank">📅 21:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450945">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c744b2d6.mp4?token=m7V290G-gkRAnuF1Y_rO3K5JnA8s01kHa61as_aEeAuDr5vv6smAXhe7QyM0QRfmvhy8lTlTwU-EJlN9IKHWFa_YQBu8DPGKJIooLINmct_zWUCxnYk3WUQLJXW910SmG7dupA-sEY6pfRiJV06mi82cbjUK35Q0LOkPpzoEKyz6eG-Sbz7oN0rMNviOdcOJ5Qa5JwoNjEPAahiUepX-EQVkByN2UA2S-qGhufgiSMUEBjHZ0E4uW-cyNMnlIeMRe48kSgRa1-MfpffMu1CI5qRuGQbiedKin_g0GrE60j2wvfjGjXSLzFxWwy0MHzZJjMWOY48QX0QwoMh5vBEwREQBJJnHQoalxf9kE7-uKsJBxiCW6sZFWt5NlWelGAZqgwZX_Q596g8MHiBOQIf1RGEbh4rbi_TmaGgSVf5U8NOXS5sjPyPUVQLyOBQDyNqSJOklkvDon_iOBP6QE_fSAiOTRAxTHxzpMAN-jnxgUqnCq0Sy5FIER7f65ihKBhlYmMDGeltSmaeJ-ZNKNB7q3aCHEy88SKmbjp6M-ZeFiQFhK_Yb4Ge9HX9Wl5sJlCJDdaYuxd7Ihvdgu93c08MO-CRM1WRve_ROnoGzQEfnyeWUTRAv-5NTuILPRpOjCYgUwPDREGUQxqN3qtRi17dj3dSrG72dvmfGU7YRGMaxm9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c744b2d6.mp4?token=m7V290G-gkRAnuF1Y_rO3K5JnA8s01kHa61as_aEeAuDr5vv6smAXhe7QyM0QRfmvhy8lTlTwU-EJlN9IKHWFa_YQBu8DPGKJIooLINmct_zWUCxnYk3WUQLJXW910SmG7dupA-sEY6pfRiJV06mi82cbjUK35Q0LOkPpzoEKyz6eG-Sbz7oN0rMNviOdcOJ5Qa5JwoNjEPAahiUepX-EQVkByN2UA2S-qGhufgiSMUEBjHZ0E4uW-cyNMnlIeMRe48kSgRa1-MfpffMu1CI5qRuGQbiedKin_g0GrE60j2wvfjGjXSLzFxWwy0MHzZJjMWOY48QX0QwoMh5vBEwREQBJJnHQoalxf9kE7-uKsJBxiCW6sZFWt5NlWelGAZqgwZX_Q596g8MHiBOQIf1RGEbh4rbi_TmaGgSVf5U8NOXS5sjPyPUVQLyOBQDyNqSJOklkvDon_iOBP6QE_fSAiOTRAxTHxzpMAN-jnxgUqnCq0Sy5FIER7f65ihKBhlYmMDGeltSmaeJ-ZNKNB7q3aCHEy88SKmbjp6M-ZeFiQFhK_Yb4Ge9HX9Wl5sJlCJDdaYuxd7Ihvdgu93c08MO-CRM1WRve_ROnoGzQEfnyeWUTRAv-5NTuILPRpOjCYgUwPDREGUQxqN3qtRi17dj3dSrG72dvmfGU7YRGMaxm9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری سنتی بوشهری‌ها برای رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/450945" target="_blank">📅 21:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450944">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56628759b1.mp4?token=jtlnTmlvPdyEQll3i0jBTKxAdMNbhRBjKOYk4y0v6sdkioBwdY_9oZ9fwLO7rHUyzBzvtior-9KLTu0liw05ivKeltIOZnaaZhLK_ie94KYqYt1BkY564RUUkSdA49jHaXuuEkG_fDW5ZZpp0i2c6b-Y8xyX48u2ELzvtwPslohOf9tHsdYw_dSt90PFTrQ_tYekYDIMUypRjMwhapFPqD2BxHstYUqQBYVLc3kDhdZbRtie1PZSZWPn9GAjBpLPMvfNkJF7-f6BGIr4gSwVziNUnc_VnBgWFXpTb5lJplThphRIJ7p9qusB5-N7DAVi6H3XDFjKbNf-PrYOlMIILA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56628759b1.mp4?token=jtlnTmlvPdyEQll3i0jBTKxAdMNbhRBjKOYk4y0v6sdkioBwdY_9oZ9fwLO7rHUyzBzvtior-9KLTu0liw05ivKeltIOZnaaZhLK_ie94KYqYt1BkY564RUUkSdA49jHaXuuEkG_fDW5ZZpp0i2c6b-Y8xyX48u2ELzvtwPslohOf9tHsdYw_dSt90PFTrQ_tYekYDIMUypRjMwhapFPqD2BxHstYUqQBYVLc3kDhdZbRtie1PZSZWPn9GAjBpLPMvfNkJF7-f6BGIr4gSwVziNUnc_VnBgWFXpTb5lJplThphRIJ7p9qusB5-N7DAVi6H3XDFjKbNf-PrYOlMIILA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام نظافت: اگر انتقام گرفته نشود، دشمن ادامه خواهد داد؛ اگر سراغ دشمن نرویم او سراغ ما می‌آید.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/450944" target="_blank">📅 21:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450943">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda32cfcd9.mp4?token=JWKio0a2FFTGv4kcJMEapGNGTPSL7W-yTqu99iv1V5Kjtn5z8UprQvbHDg8EmELJiBZRyjKwW-VtEAbbQ8DjsNRi8tsqQlWkS809nSGymbUTLgSwwSFyDZzu8K8TA9yhM3LxYY6bvg8UIeE5pUYzpRJugbx-eU6WPjI2qRVg8ePju6eZ4dyud1q9LH32C6WPOYeZdtzmY1FdpP8GwOH4JGmlpUX89JQQ4puj42Hk7IhtRiv08FV6pkIpsmQlxeBHNDjZdsgzS4Bh5ifjTCmA37uMK1JR8ewu5uOZIbdgIq1908ApCzG8Tyt7bJQTv5lvkkbhXgpX6d-CSDnNl1rNlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda32cfcd9.mp4?token=JWKio0a2FFTGv4kcJMEapGNGTPSL7W-yTqu99iv1V5Kjtn5z8UprQvbHDg8EmELJiBZRyjKwW-VtEAbbQ8DjsNRi8tsqQlWkS809nSGymbUTLgSwwSFyDZzu8K8TA9yhM3LxYY6bvg8UIeE5pUYzpRJugbx-eU6WPjI2qRVg8ePju6eZ4dyud1q9LH32C6WPOYeZdtzmY1FdpP8GwOH4JGmlpUX89JQQ4puj42Hk7IhtRiv08FV6pkIpsmQlxeBHNDjZdsgzS4Bh5ifjTCmA37uMK1JR8ewu5uOZIbdgIq1908ApCzG8Tyt7bJQTv5lvkkbhXgpX6d-CSDnNl1rNlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چه کسی در تیررس ایران قرار می‌گیرد؟
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/450943" target="_blank">📅 21:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450942">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f7c00ffec.mp4?token=SVBvRkUFf0PNUhEXWkF6NSdePCnpU-R7HNKy9b2bDMD6V1UHg5VoBAFgB8ej5xflCHEb4W8_2c6ZpV1CcaNfQpeTRsYou87iFICvGoI53y5VpL0zTAxVZK1jsExxzF9Ym6_GraXSLVnk4SIrzq1nWQd3QzzLLsugIjP0HryjsZ_iCU-bYIrj6z0ZsIwyhZTJDt2VX9-F58QD8V2WMJtmvj1A2hW9Tp9AkZKJf9zf9kYtgJG3JML-Hxs_1i2ebFthCddlZVH67R9MZ5aVGmQd0Rz3pc8h0maqEGJ7oNW8TCyZ0hmCUVbx4wv3D4sHO0bsNP3Gd3bKhhvDbLNfa--FBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f7c00ffec.mp4?token=SVBvRkUFf0PNUhEXWkF6NSdePCnpU-R7HNKy9b2bDMD6V1UHg5VoBAFgB8ej5xflCHEb4W8_2c6ZpV1CcaNfQpeTRsYou87iFICvGoI53y5VpL0zTAxVZK1jsExxzF9Ym6_GraXSLVnk4SIrzq1nWQd3QzzLLsugIjP0HryjsZ_iCU-bYIrj6z0ZsIwyhZTJDt2VX9-F58QD8V2WMJtmvj1A2hW9Tp9AkZKJf9zf9kYtgJG3JML-Hxs_1i2ebFthCddlZVH67R9MZ5aVGmQd0Rz3pc8h0maqEGJ7oNW8TCyZ0hmCUVbx4wv3D4sHO0bsNP3Gd3bKhhvDbLNfa--FBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌گرفتن تانکر حامل گاز در زاهدان
🔹
سازمان آتش‌نشانی زاهدان: آتش‌سوزی در ورودی شهر زاهدان به علت آتش گرفتن تانکر گاز بوده که هم‌اکنون آتش مهار شده است
🔸
این حادثه هیچ‌گونه تلفات جانی نداشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/450942" target="_blank">📅 21:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450941">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRSh1EJtTp6RiZV10XVZ9q7AieZkkbP33_YCeydg7Wp4nhryk0j3z4agaeimfyN3x7h4UEZdjdtyv139ReMn5wEsMKv1FhqvaUrppo2gAZcUZUoZTXRyZ_OncjbQZjb19cKudSzjNzH8VYckSKUBK-YJck-c280dKyySPv81cgKAqeEUXErRptMVgXbSLxTglpduNrVApEhvVNqOChJgUYcXFfmwB89ZRTnIrivGoJJFAAiBp9hZ1W6gf2ZQBozECok7cmKZlcKjCs_ewzRVmUt8Fa5EfdkH5DLPfULklNHsVjXJQMA-kfF-1IOByIV8FAWsk53yTpJFc1ZEvqYLEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: آمریکا پیش از خشک‌شدن مرکب تفاهم‌نامه به ایران حمله کرد
🔹
معاون اول رئیس‌جمهور: هنوز مرکب تفاهم‌نامه ایران و آمریکا خشک نشده بود که آمریکا بار دیگر تعهدات خود را نقض و به کشورمان حمله کرد.
🔹
این حملات در شرایطی انجام شد که بر اساس مادۀ ۵ تفاهم‌نامه، مدیریت تنگۀ هرمز در ۶۰ روز پس از امضای آن بر عهدۀ ایران قرار می‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/450941" target="_blank">📅 21:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450939">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/000716b3f2.mp4?token=d_1Wv8_7RLqZHN7RpJfLUrtm4y1TzfSPLVgA2mlazbju8FVc5p89tI7X74HdKyINnz9Id59g_5GZRNDEke8ELC5cz8-_KMn1GQ_gSihB3rj4s9YIihGYYNKpqEnMT1oNBWz_YhO05IH35KOasuDp11FTXqQfDj6VI3BIMD4Z4y0TIOAX2S9Q9LMwOOpRY-nhFQXtBDpn7KbCjaH9cIKOz2UsGMd0ojUdtSoPm27Ydg86CN4VeIpeelRFkoH6n5kHR5rab2MjCuGAGXx8e5biFHICCjNKiufvqOPEZ71-H8yIyrhq5a5lfcrE_FJAlbVQjgmirbwalR-rwColpDoXEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/000716b3f2.mp4?token=d_1Wv8_7RLqZHN7RpJfLUrtm4y1TzfSPLVgA2mlazbju8FVc5p89tI7X74HdKyINnz9Id59g_5GZRNDEke8ELC5cz8-_KMn1GQ_gSihB3rj4s9YIihGYYNKpqEnMT1oNBWz_YhO05IH35KOasuDp11FTXqQfDj6VI3BIMD4Z4y0TIOAX2S9Q9LMwOOpRY-nhFQXtBDpn7KbCjaH9cIKOz2UsGMd0ojUdtSoPm27Ydg86CN4VeIpeelRFkoH6n5kHR5rab2MjCuGAGXx8e5biFHICCjNKiufvqOPEZ71-H8yIyrhq5a5lfcrE_FJAlbVQjgmirbwalR-rwColpDoXEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه
:
مردم عملکرد دستگاه قضایی را در ۵ سال اخیر، بهتر از ۲ قوه دیگر ارزیابی کردند.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/450939" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450938">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ed02AlMZWAW4C1Ee9wejHROFg7wYZh8vNwA7wPGOBwgKXETwkYHNewxBwhBKUr7sjDGX5hITzxBqTM_DcI9dpV8yQcRMon0eAN9sHZikc64q9-EC6HTIFgUYFeSSGgVBgFibHWVdIfwZ-rTRUIHYRvhqps0Ms8Aze_R2xAy_lvV5O25JMqJRlmPWxON5fjRvXcdQENziECMbfHV_LTHFkdjs2i2zGVzXTQAyYdMDn61D3ZTin-vOe5_yvcSFyN7I1vJRFz7EDDIM2WPgH2JX7t2tI1dKJSkQ--L5-jvw8ZxV8xj9a3iz_Q3bFOqOKEkYqhA1QWAoVoFaYVoGf5C4aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسکاری‌ها برای پرداخت پول کالابرگ شروع شد
🔹
بیش از ۲ هفته است که برخی فروشگاه‌های طرف قرارداد کالابرگ مطالبات خود را از دولت دریافت نکرده‌اند؛ در حالی که طبق قانون، تسویه باید حداکثر ظرف ۷۲ ساعت انجام شود.
🔹
بانک مرکزی می‌گوید از ابتدای سال ۱۴۰۵ دیگر مسئول تأمین منابع کالابرگ نیست و این وظیفه طبق قانون بودجه بر عهده سازمان برنامه و بودجه قرار گرفته است.
🔹
اما سازمان برنامه تأکید می‌کند این نهاد نیز مسئول تأمین منابع نیست و منابع کالابرگ با وصول درآمدهای دولت به‌تدریج تأمین و سپس از سوی وزارت تعاون پرداخت می‌شود.
🔹
در حالی که فروشگاه‌ها از کمبود نقدینگی گلایه دارند، سازمان برنامه می‌گوید درآمدهای دولت به‌صورت تدریجی وصول می‌شود و مطالبات فروشگاه‌ها پس از نقد شدن این منابع پرداخت خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/450938" target="_blank">📅 21:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450937">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/008837f665.mp4?token=ZjUvo2IlfptC75gkML-FIQE-JGAK6zpXJNmkvid-UEqDCWoeYYDHfUMWcm9KQMmh9K50XQblT9H89cLkUQsrX-C54asIHmFymeKEAVMUtADBm4cfnpi23XUNu0XgwtB2xNukEMl8f6EoHQfNKE9wnCZX0LvB5px-ppcIqtTqkAv0YRnKxZWiHehN5puygTdqOjGBxIBtEcQBWVVULAWXMvSFrhMPX5B7HhHbMky6gpu-f1xvrIp-vwnI3aFbiE57OcOxEgms83GR6hcSsFqwiGunpA7SJc9K9S2LXwfh5kNjW38Dh52HSxO7qm027GFe_0xjPL6294iPKKQGZ8iB6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/008837f665.mp4?token=ZjUvo2IlfptC75gkML-FIQE-JGAK6zpXJNmkvid-UEqDCWoeYYDHfUMWcm9KQMmh9K50XQblT9H89cLkUQsrX-C54asIHmFymeKEAVMUtADBm4cfnpi23XUNu0XgwtB2xNukEMl8f6EoHQfNKE9wnCZX0LvB5px-ppcIqtTqkAv0YRnKxZWiHehN5puygTdqOjGBxIBtEcQBWVVULAWXMvSFrhMPX5B7HhHbMky6gpu-f1xvrIp-vwnI3aFbiE57OcOxEgms83GR6hcSsFqwiGunpA7SJc9K9S2LXwfh5kNjW38Dh52HSxO7qm027GFe_0xjPL6294iPKKQGZ8iB6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس ستاد اربعین: هیچ مشکلی برای تردد زائرین در مرز خسروی وجود ندارد
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/450937" target="_blank">📅 21:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450936">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad26fa7899.mp4?token=auedItVgw8q2kK19s6j945b4FdFm8xqJlpfrEfXlrjxdhJyrZXkHKDwZXY8MowmGXABpmWqRoMVH6PC_6l43t0n0yZH9TLWblQ4U_3QyHKUChcpfpI6Qv3byir_gyG7UKgcEwq3zDpkBF0ArzrxSHfRlFtRxFsQS6KyrAxkKoh4yoxKhL9MhD_apLPnq-Gk0D5y2MuvAjsjLqz9xJr9eQZzncQf3GXdT0wzDAhI75dErnCqP2AXNF0gUT2AYeLuWMxIH9BOWwoZmM1tbK3XrGIMEWNLnCZCaZsxpX2LK5bboRDg9B5NUUeATYiWOydPAC2CDlgny6e9d0wwIcGIKNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad26fa7899.mp4?token=auedItVgw8q2kK19s6j945b4FdFm8xqJlpfrEfXlrjxdhJyrZXkHKDwZXY8MowmGXABpmWqRoMVH6PC_6l43t0n0yZH9TLWblQ4U_3QyHKUChcpfpI6Qv3byir_gyG7UKgcEwq3zDpkBF0ArzrxSHfRlFtRxFsQS6KyrAxkKoh4yoxKhL9MhD_apLPnq-Gk0D5y2MuvAjsjLqz9xJr9eQZzncQf3GXdT0wzDAhI75dErnCqP2AXNF0gUT2AYeLuWMxIH9BOWwoZmM1tbK3XrGIMEWNLnCZCaZsxpX2LK5bboRDg9B5NUUeATYiWOydPAC2CDlgny6e9d0wwIcGIKNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازگشایی مسیرهای آسیب‌دیده در مناطق جنوبی کشور با همت نیروهای جهادی
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/450936" target="_blank">📅 21:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450935">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۹۷.pdf</div>
  <div class="tg-doc-extra">3 MB</div>
</div>
<a href="https://t.me/farsna/450935" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📎
دستِ پُر به میدان بروید
🔸
اگر برای اجتماعات انقلابی به‌دنبال شعر، شعار یا تک‌بیت‌های روز هستید، ویژه‌نامهٔ «خط» پاسخگوی نیاز شماست.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/450935" target="_blank">📅 21:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450934">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/446f1163d1.mp4?token=aG879b0mL8TE2uwe6KHDSKZc-9ZM4VDTp7mVLRRuprhVZknVmgHC8PSADIZRzx3nRoJz2RWatwn7j0b3E4llLXkKHNZEM_Muv4c1cVZFSJ3GRucksHmtRnwL9xX1LnBLLNQQ-a3fZUznNoYbQj9q_S26eGo4UIfXyZCpHA3ExLSyFwemFJqyIZzVjGgQEUUJvpubY5eEwWDoZSPuBctOQ10vV0lg0oij2nHbWPSLpru-nt8e8GhBL0Q3NAHx-3TkVD64xixRR1uerg6A4OAYhUERRXNrYn8_UJdShSXnt_wz8bwypmbFxv2LFCerWrnpa0lJ1pZRFVvifSOzNkVuBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/446f1163d1.mp4?token=aG879b0mL8TE2uwe6KHDSKZc-9ZM4VDTp7mVLRRuprhVZknVmgHC8PSADIZRzx3nRoJz2RWatwn7j0b3E4llLXkKHNZEM_Muv4c1cVZFSJ3GRucksHmtRnwL9xX1LnBLLNQQ-a3fZUznNoYbQj9q_S26eGo4UIfXyZCpHA3ExLSyFwemFJqyIZzVjGgQEUUJvpubY5eEwWDoZSPuBctOQ10vV0lg0oij2nHbWPSLpru-nt8e8GhBL0Q3NAHx-3TkVD64xixRR1uerg6A4OAYhUERRXNrYn8_UJdShSXnt_wz8bwypmbFxv2LFCerWrnpa0lJ1pZRFVvifSOzNkVuBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁨ ⁨
💫
ارز اربعین؛ خدمتی از بانک شهر برای سفری آسوده‌تر
📱
سفر اربعین، سفری از جنس عشق و دلدادگی است. بانک شهر با همکاری اپلیکیشن آپ، امکان ثبت آنلاین درخواست ارز اربعین را فراهم کرده تا زائران بدون مراجعه حضوری برای ثبت درخواست، تنها با چند گام ساده، شعبه منتخب بانک شهر و زمان دریافت ارز را انتخاب کنند و با خیالی آسوده راهی کربلا شوند.
✔️
ثبت درخواست برای خود و افراد تحت تکفل در اپلیکیشن آپ
✔️
دریافت ارز از شعب منتخب بانک شهر
✔️
تا سقف ۲۰۰ هزار دینار
⏳
لطفاً پیش از ثبت درخواست، ثبت‌نام خود را در سامانه سماح نهایی کنید.
بانک شهر؛ در کنار زائران، در هر قدم از این مسیر معنوی.
#آپ
#اربعین
#سفر
#بانک_شهر
⁩⁩</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/450934" target="_blank">📅 21:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450933">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه معلم | MIC Insurance</strong></div>
<div class="tg-text">🔸
«کام»، خریدی هوشمندانه؛ آینده‌ای مطمئن
🔹
با طرح ملی «کام»، خریدهای روزمره شما فقط یک پرداخت ساده نیست؛ بلکه فرصتی است برای ساختن آینده‌ای بهتر.
🔹
در این طرح، بدون آن‌که مبلغ بیشتری پرداخت کنید، با خرید از پذیرندگان منتخب، بخشی از مبلغ‌ خریدهای شما به‌صورت خودکار به اندوخته‌ای ارزشمند تبدیل می‌شود.
🔹
مزیت مهم طرح «کام» این است که این اندوخته در قالب بیمه‌نامه سرمایه‌گذاری رایگان نزد بیمه معلم برای شما تشکیل می‌شود؛ یعنی بدون پرداخت هزینه اضافی، هم از خرید خود لذت می‌برید و هم برای آینده‌تان سرمایه‌گذاری می‌کنید.
🔹
گام‌های پیوستن به طرح «کام»:
▫️
ثبت درخواست در وب‌سایت بیمه معلم
▫️
ثبت کارت‌های بانکی از طریق اپلیکیشن سکه به‌پرداخت ملت
▫️
خرید از پذیرندگان منتخب و شروع خودکار فرایند اندوخته‌سازی.
#بیمه_معلم_همراه_هم_وطن
سایت
|
بله
|
اینستاگرام
|
تلگرام</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/450933" target="_blank">📅 21:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450932">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/450932" target="_blank">📅 21:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450931">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">استانداری هرمزگان: شنبه تمام اداره‌ها، سازمان‌ها و بانک‌های استان با حضور ۵۰ درصدی کارکنان، فعال خواهند بود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/450931" target="_blank">📅 21:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450930">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26d005a4bd.mp4?token=tPaIH5CFYD9bwv7eJTMqaWjmsmrQLSg3TYuyxRs-tuO7plcoANk_I4juaWpbo72SdhZSsPlWYnnCd5WUJTwstVHWtWhuJTtm41fy_jNaDQaOs6zhGtc0NXAivXPnuXpgi3DpY4EJsIUErZj5DoTTrM2RxstNH6o_yDWUwxDKt3rIDlnfTBBFD-0eNdLGKAJ0ckU1fTabNF9Ngl5EIbgwqlED3E7g22eoM-2doftZFVEHYd4Zxm7-GZjLjfXpx_GAe-Lje6bCPlVE47foCoBYdU4cywt0RXR5k7SxnppOvpWgDKPoHdXvTh3PE2xM7SWpBahTwindRAOazEEzw2LO6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26d005a4bd.mp4?token=tPaIH5CFYD9bwv7eJTMqaWjmsmrQLSg3TYuyxRs-tuO7plcoANk_I4juaWpbo72SdhZSsPlWYnnCd5WUJTwstVHWtWhuJTtm41fy_jNaDQaOs6zhGtc0NXAivXPnuXpgi3DpY4EJsIUErZj5DoTTrM2RxstNH6o_yDWUwxDKt3rIDlnfTBBFD-0eNdLGKAJ0ckU1fTabNF9Ngl5EIbgwqlED3E7g22eoM-2doftZFVEHYd4Zxm7-GZjLjfXpx_GAe-Lje6bCPlVE47foCoBYdU4cywt0RXR5k7SxnppOvpWgDKPoHdXvTh3PE2xM7SWpBahTwindRAOazEEzw2LO6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قدرت‌نمایی موشک‌های ایرانی با اصابت به اهدافی در اردن
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/450930" target="_blank">📅 20:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450929">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌
🔴
اعتراف سازمان تروریستی سنتکام: ۲ نظامی آمریکایی در حملات ایران به اردن کشته و ۴ نظامی مجروح شدند. @Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/450929" target="_blank">📅 20:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450928">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‌ اعتراف آمریکا به زخمی‌شدن ۱۳ نظامی در حملات ایران
🔹
فاکس‌نیوز به‌نقل از مقامات آمریکایی گزارش داد که از آغاز حملات ایران به پایگاه‌های آمریکا در کویت، بحرین و اردن، تاکنون دست‌کم ۱۳ نظامی آمریکایی مجروح شده‌اند.
🔹
با وجود گذشت چند روز از این حملات، مقام‌های…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/450928" target="_blank">📅 20:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450927">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">حادثه امنیتی در نزدیکی سواحل عمان
🔹
سازمان عملیات دریایی بریتانیا اعلام کرد که گزارشی از حادثه‌ای بین یک کشتی تجاری و نیروهای نظامی در فاصله تقریباً ۱۰۰ مایلی در شرق شهر دقم در سلطنت عمان دریافت کرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/450927" target="_blank">📅 20:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450926">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6849fcb1a4.mp4?token=olAHsh3V4Lhl9TIAEyc3M0bIx2k5Wq7B8QxqVWEBQQFQWdt0CsvVp3pMwU9OmY4GY2FBMfsMAuBkD7wUZ9uvZ9K8nCS25E58-2gbgVVvl46PuOMsOSeD_QzRgUKtoFc1Kri9l3LqlLAUP4Y9NpV35vKT_axgl3MhymBBaEta1yZFiOtNAFlYs_dyBantc7qsPsC-yml-qOy1BAF7VNJwUHHtDRBKlvkPaKsMKd9o9yJjjUmCFmznZyQ7_K6eFLaa0haJNQpA61B2FcYxILO425eE3HpOfnwvw7__Q94syB9-mPbTEiX3s-p9Red6qXQIwrW6I3aJCfV6sdw_zjeesQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6849fcb1a4.mp4?token=olAHsh3V4Lhl9TIAEyc3M0bIx2k5Wq7B8QxqVWEBQQFQWdt0CsvVp3pMwU9OmY4GY2FBMfsMAuBkD7wUZ9uvZ9K8nCS25E58-2gbgVVvl46PuOMsOSeD_QzRgUKtoFc1Kri9l3LqlLAUP4Y9NpV35vKT_axgl3MhymBBaEta1yZFiOtNAFlYs_dyBantc7qsPsC-yml-qOy1BAF7VNJwUHHtDRBKlvkPaKsMKd9o9yJjjUmCFmznZyQ7_K6eFLaa0haJNQpA61B2FcYxILO425eE3HpOfnwvw7__Q94syB9-mPbTEiX3s-p9Red6qXQIwrW6I3aJCfV6sdw_zjeesQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از پارک ممنوع تا پارک ایمن؛ آنچه زائران اربعین باید بدانند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/450926" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450925">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">متن کامل پیام رهبر انقلاب.pdf</div>
  <div class="tg-doc-extra">144.6 KB</div>
</div>
<a href="https://t.me/farsna/450925" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">‌
🔴
رهبر معظم انقلاب: نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد
🔹
هم‌زمان با این حماسه [بدرقه‌ٔ آقای شهید ایران]، نقض عهد‌های مکرّر شیطان بزرگ نسبت به تفاهم‌نامه امضا شده بین رئیس‌جمهوران ایران و امریکا بار دیگر این…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/450925" target="_blank">📅 20:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450924">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
پیام رهبر معظم انقلاب دربارۀ حماسۀ عظیم بدرقه آقای شهید ایران و تبیین مسائل مهم کشور تا دقایقی دیگر منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/450924" target="_blank">📅 20:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450923">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‌
🔴
رهبر معظم انقلاب: بدرقۀ آقای شهید ایران حماسه‌ای تاریخی و رستاخیزی بی‌سابقه بود
🔹
ملّت عظیم‌الشّأن و شگفتی‌ساز ایران! سلام و درود و سپاس بر شما که با حماسه‌ی بی‌نظیر و تاریخی خود در رستاخیز بی‌سابقهِ‌ی بدرقه‌ی آقای شهید ایران، نِصاب تازه‌ای از جلوه‌ی بعثت…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/450923" target="_blank">📅 20:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450922">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‌ رهبر معظم انقلاب: انتقاد به عملکرد مسئولان نباید موجب ظلم به بیگناهان و شکست وحدت و انسجام اجتماعی شود
🔹
ملّت عزیز، با تداوم بر اعتماد به مسئولان دلسوز در هر سه قوّه که تلاش ایشان برای رفاه و سعادت ملّت، مشهود می‌باشد، همچنان برای تضمین صیانت از منافع ایران…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/450922" target="_blank">📅 20:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450921">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AF6rmG4Ir_jNOn2MhxQp5gpy9b4Span9ximhHM2nyadsb3PF7ADZ1w12GRtBw83QvpIkfeRE5B9lenv7Y8EjFpk9GN4kBCVecoubkGcqQyas5Q9qSrSRjEv-RXHGnbe56gajWkHLOlu9ILzD904tEz7a0uPORsqVFfkKOUaG9er51MbWrb-VoCoUI5gh57DUi0S-pV4R787yDXN7iXl77YwwlnRvqsImB4-uq76Po8ZAhA1-0nnBgSuH6Z0gkjl1kuxiQIZLh1myqIAgOJmCQf8hpNoshxCxQnj1HS-TBbTCLhZG_6HM3OhELHqm-eU9BZebs_TtKkc2yka2xAItEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رهبر معظم انقلاب: از اصولی‌ترین امور، اصرار بر اتحاد مقدّس در همه‌ی سطوح است؛ پرهیز از تفرقه و تنازع وظیفۀ همگانی است
🔹
لازم است به شما مردم باوفا و سرافراز ایران عرض شود که از جمله اصولی‌ترین امور در این برهه، اصرار بر وحدت کلمه و اتحاد مقدّس در همه‌ی…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/450921" target="_blank">📅 20:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450920">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‌
🔴
رهبر معظم انقلاب: نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد
🔹
هم‌زمان با این حماسه [بدرقه‌ٔ آقای شهید ایران]، نقض عهد‌های مکرّر شیطان بزرگ نسبت به تفاهم‌نامه امضا شده بین رئیس‌جمهوران ایران و امریکا بار دیگر این…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/450920" target="_blank">📅 20:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450919">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aK_XVl0_KUUqAuGyyiFgiOgcTNG2w3cQ0E7eYY9mKB81qYGcQyG5LtybT9KNTdNHVPBlGfPnMOOT7SdbRZo9zCScDZByuwrqHrfzwi2gkRHBxGBCMDePBe6NGY26IeuOrlLWjS1J4T4I6u1or5aRM-rGyHP8VSovWblO0PvX47epx2IpWGCmGd6QEmSAaGdfoiQ8pqiFFDwLdjYJDIyRDW43MTFW6YsQesJbROspUmTck2D6vLmYteIkd7L3STiAaYBZ-rZXCznwXqh8ZJu3z7yH7cs02KDEiXHTwnnOr4i4OxYTYKUzXimlrvI-iF2ZQ5lELXKfGl8D1IV980sc3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیام رهبر معظم انقلاب دربارۀ حماسۀ عظیم بدرقه آقای شهید ایران و تبیین مسائل مهم کشور تا دقایقی دیگر منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/450919" target="_blank">📅 20:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450918">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ادارات خوزستان دوشنبه دورکار شدند
🔹
استانداری خوزستان: با توجه به پیش‌بینی تداوم گرمای شدید، ساعت کاری ادارات استان در روز یکشنبه تا ساعت ۱۱ خواهد بود و فعالیت ادارات در روز دوشنبه به‌صورت دورکاری انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/450918" target="_blank">📅 19:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450917">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114af211a3.mp4?token=txpBXlb9a4zdZ9X3g0ngiy-3pJb4yCBTYKacYF7iTVVbltbPrRn5gkuMevZkCqi2aKM0VBTeH8ArQfaCZ0Heyl4yr8ushWQThQP-idNYhpD7kevy3076olr4UsGqulAiD89K2Yn5RYV0GWoSl3hwTcmEI952M--diUeaTAvWrwULzBdQHodtBbiDfRcGXERuD9HrKTL9EumAFnUjgL0_JBWHWfnykwfWF1zRwhNZFvt_h1rIQYLtpxn_wiT4BINy4mcmgBK9aYn42R2TJbVCYp6ZyMdIsAFpiWmaiYwUwx_sgNV_zlhyqrrc7MsbXaJ2me9bd-_f7qCit17E81VPlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114af211a3.mp4?token=txpBXlb9a4zdZ9X3g0ngiy-3pJb4yCBTYKacYF7iTVVbltbPrRn5gkuMevZkCqi2aKM0VBTeH8ArQfaCZ0Heyl4yr8ushWQThQP-idNYhpD7kevy3076olr4UsGqulAiD89K2Yn5RYV0GWoSl3hwTcmEI952M--diUeaTAvWrwULzBdQHodtBbiDfRcGXERuD9HrKTL9EumAFnUjgL0_JBWHWfnykwfWF1zRwhNZFvt_h1rIQYLtpxn_wiT4BINy4mcmgBK9aYn42R2TJbVCYp6ZyMdIsAFpiWmaiYwUwx_sgNV_zlhyqrrc7MsbXaJ2me9bd-_f7qCit17E81VPlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایتخت سوئد امروز شاهد راهپیمایی در حمایت از غزه و اعتراض به جنایات نتانیاهو بود
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450917" target="_blank">📅 19:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450916">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
پیام رهبر معظم انقلاب دربارۀ حماسۀ عظیم بدرقه آقای شهید ایران و تبیین مسائل مهم کشور تا دقایقی دیگر منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/450916" target="_blank">📅 19:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450915">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635337e268.mp4?token=lTIevtUv4LKdIg9iD4ZCJBbZsQ5PY5b0PBbiWhw0sEDZee4kDPege_neutaBqhLGQ0ivMjsXEkRQQ-LsKFfL_mWyCH77qSC4syEOTIETZQEG6rLOv8oSC48leAaIr5-pek3CFj6lKtbQfH4y3j23zlDvn87FMO3E_TInRs8wBtU4BPii6mucoikcbU6WzzywuQY-0MWYsYcnXSTpeiHUyWPv9U4cNZZBxwFW1Gb7SZJzz7Ft-58w8Ay4EZdUPaRITq7fPx8Oo3m2A-CCxrVPuyXaqyth8BkDaAyZ0dm99m1YGHaSKeGiS2iiIlmjEPMntqYXE_AsFLhO8kZGBl3Sjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635337e268.mp4?token=lTIevtUv4LKdIg9iD4ZCJBbZsQ5PY5b0PBbiWhw0sEDZee4kDPege_neutaBqhLGQ0ivMjsXEkRQQ-LsKFfL_mWyCH77qSC4syEOTIETZQEG6rLOv8oSC48leAaIr5-pek3CFj6lKtbQfH4y3j23zlDvn87FMO3E_TInRs8wBtU4BPii6mucoikcbU6WzzywuQY-0MWYsYcnXSTpeiHUyWPv9U4cNZZBxwFW1Gb7SZJzz7Ft-58w8Ay4EZdUPaRITq7fPx8Oo3m2A-CCxrVPuyXaqyth8BkDaAyZ0dm99m1YGHaSKeGiS2iiIlmjEPMntqYXE_AsFLhO8kZGBl3Sjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت پردۀ کاسبان جنگ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/450915" target="_blank">📅 19:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450914">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌  بقایی: براساس یادداشت تفاهم، هیچ نکته‌ای وجود ندارد که به آمریکا اجازه دهد مسیر موازی مستقلی در تنگه هرمز ایجاد کند
🔹
آنچه آنها انجام دادند، نقض تعهداتشان بود. آنها کشتی‌ها را مجبور کردند از مسیر دیگری عبور کنند و عملاً مسیر هماهنگ‌ شده با ایران ــ که مسیر…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450914" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450913">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بقائی: تک‌تک بخش‌های یادداشت تفاهم از سوی آمریکا نقض شده است
🔹
سخنگوی وزارت خارجه: تک‌تک بخش‌های یادداشت تفاهم اسلام‌آباد طی یک هفته یا ۱۰ روز گذشته از سوی آمریکا نقض شده است.
🔹
ایرانیان هرگز خواهان جنگ با هیچ کشوری، چه در منطقه و چه خارج از آن، نبوده‌اند؛…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450913" target="_blank">📅 19:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450912">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiDDuc12pIqq5Y1vjc_qAmlGoSg2_BpMl5sHht6pHV8lxvBMEo_-ubV18LApAcG0bEA8Bf6QNNQeMweNAcZW8Fh9tSO7o9THYhgrL2R7Xy8c6MmnHMScgmhhMkqmBjizv9fx2nLvuf0jp-BjQIEuURcJSFN6wlPamR7puyoF2YbXFSxJbmUpC4tSomqZXoTyHtyshJ95W3tl4slts0x-ZS8e_FUxGIou2Qvi5GadAINofsobp4qQekGtrn9zWK4CQO_lLXT90z1k938f8NJ3464xLHa7lAfo4ZwpbBMFXBf8Nx9xoYnDPFgEjeLLJc0eHbcto5vvUgctUBcs8YqKDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: تک‌تک بخش‌های یادداشت تفاهم از سوی آمریکا نقض شده است
🔹
سخنگوی وزارت خارجه: تک‌تک بخش‌های یادداشت تفاهم اسلام‌آباد طی یک هفته یا ۱۰ روز گذشته از سوی آمریکا نقض شده است.
🔹
ایرانیان هرگز خواهان جنگ با هیچ کشوری، چه در منطقه و چه خارج از آن، نبوده‌اند؛ ما صرفاً از خود دفاع کرده‌ایم و این جنگ بر مردم ایران تحمیل شده است.
🔹
تعهد آنها این بود که در طول دوره اجرای این یادداشت تفاهم، ایران به تمام دارایی‌های مسدودشده خود دسترسی آزاد داشته باشد. قرار نبود آنها پولی به ایران پرداخت کنند. این پول، دارایی خود ایران است که سال‌ها به‌صورت غیرقانونی مسدود شده است.
🔹
هیچ هدفی را جز پایگاه‌های نظامی و تجهیزات نظامی آمریکا مورد حمله قرار نداد‌ه‌ایم، ایران و جمهوری اسلامی از یکدیگر جدا نیستند و ملت ایران هیچ دشمنی با مردم آمریکا ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450912" target="_blank">📅 19:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450911">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HajlgaHtbWiCsLbv-thT8MgzoHPUYRtf0i4T0Zl3YsaHYg4B9F8Qt0yQXwB1O_hUtgtmGixsbYLnhvdK_acKXZZbkqoz6qZFJQPF9kw-laMtyQJ4CG9gJoD-txkwGoW-hsYdsRNsIgdljhQCa1GUGwVHtkYuQUHAaxfPCfU5CSd7yOK1SbRd-TQQmTIvKQB26G5tuZuu61IiO9rm0utalv5WsyuGPKyHAIsoeXEc9N9oKAKRvbw84GU4vh7rAlUaYJOEvSMga15HTJt3qOvtFI9ifI6-yDa26Xu5d5sBvVw0hXnjHLWo63FqVYVY50UID9t73m65z5TojA7sI0m-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چت‌جی‌پی‌تی تخلفات نوجوانان را به والدین گزارش می‌دهد
🔹
انگجت: اپن‌ای‌آی از گسترش قابلیت‌های نظارت والدین در چت‌جی‌پی‌تی خبر داد. بر اساس این تغییر، در صورت غیرفعال شدن حساب یک کاربر نوجوان به‌دلیل نقض سیاست‌های مربوط به تهدیدها یا اقدامات خشونت‌آمیز، والدین متصل به حساب فرزندشان یک اعلان دریافت خواهند کرد.
🔹
اعلان جدید فقط از غیرفعال شدن حساب به‌دلیل نقض قوانین خبر می‌دهد و دسترسی والدین به محتوای گفت‌وگوهای نوجوان را فراهم نمی‌کند. این قابلیت برای کمک به مداخله زودهنگام خانواده‌ها در صورت بروز نشانه‌های نگران‌کننده توسعه یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/450911" target="_blank">📅 18:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450910">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
حملات متعدد موشکی دشمن آمریکایی به حوالی سیریک
🔹
استانداری هرمزگان اعلام کرد: در ساعت ۱۲:۳۰ و ۱۶:۳۰ و ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله نظامی دشمن آمریکایی قرار گرفت.
🔹
در حملات جدید آمریکا به سیریک هیچ مصدوم غیرنظامی گزارش نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/450910" target="_blank">📅 18:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450909">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba8a32ee92.mp4?token=nPy_aMEkID7ctkpJ-TieX4OE_rMP-xwMW43kk1RMD850xbZxJLN0jzTuap3dvImMWkb2eV_eMdQW2WYFDzqz0BucpQJaLJLkRb1Xp2GXp9USjExyXYO-f9rpUvjDwQ-Z2cbPjAR1_-TBsM2Wkb-BYFk4V_nBj54m9W6fBAnI0Yf9yQoN-gFm-hXkCxYzs1UkJCjaHcFOb7wAS0znsg6Xz0ONJnhKRTGgDjZ2cb-4qAAyrElOgGwzjgx7txuwpsXXcikQIcIFswpHL7OTMoIYu1G_jYtVPGghUAz9Pp2Y1fxXZgieKTGRP1c1fqYih0QzirMJhE4Qe-ejK5eq0Aw4-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba8a32ee92.mp4?token=nPy_aMEkID7ctkpJ-TieX4OE_rMP-xwMW43kk1RMD850xbZxJLN0jzTuap3dvImMWkb2eV_eMdQW2WYFDzqz0BucpQJaLJLkRb1Xp2GXp9USjExyXYO-f9rpUvjDwQ-Z2cbPjAR1_-TBsM2Wkb-BYFk4V_nBj54m9W6fBAnI0Yf9yQoN-gFm-hXkCxYzs1UkJCjaHcFOb7wAS0znsg6Xz0ONJnhKRTGgDjZ2cb-4qAAyrElOgGwzjgx7txuwpsXXcikQIcIFswpHL7OTMoIYu1G_jYtVPGghUAz9Pp2Y1fxXZgieKTGRP1c1fqYih0QzirMJhE4Qe-ejK5eq0Aw4-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احساساتی‌شدن داوران برنامۀ محفل ستاره‌ها با تلاوت فوق‌العادۀ خلبان کوچولو
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/450909" target="_blank">📅 18:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450908">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d76f189634.mp4?token=ZeFsdsdS6WWrJfZm5N_Gky5-7h7crt_kNEJ5yYKsM9HzmlZfrmmUeEGEwhFLzP58kvO9zok5FmMO6Bv3W5eEoQwoQD3in03ISwwRoF6yzUsI1xcvnPGJzsztgYR2VuyB1jNgkSX9e46UKeu8w4gOlX3DMts09SM_IB8s-eupkgvFOR4aK_sLPPRZ97fwCg6VxH0wM88k04xHOR5vUWnXeqyLyTOQxnh2q5rpzVW2mp4xho-I48uX2YUcfeBT68TBviwtoJ_OlX8zolknI2Afuv6s-zKa5-tOn1umRJrVso30B6BumudOHGIhg6E09TlV7B0gPZm7zOpFw764CowRBJM-PZHudfmbXkgDyxSfQkjE3uEZ9GIqksA77RAk3kiV2LTKmRl_QC94a2R-yinWIFKwRL7qHG3g4xq4HJfXQpsxa7RqfkoyQJUMCIidJPfr2c1kycenPpytOZno4qIabBzQhP1dKDUL1baITxnVqOzo-Ttb6fZPxZqLnw1TOkOSyf5Cd1jls8ntxpYb_lXpb8B2v93BMldls3oAZuceGjZLYfzXshXs9YtgPR4fdhctN1_oezIj7-gO-LA4tblLNC06oqxH2QsDWE07b6lqKr1uBVorNd6bJmOoJTpa4qKJCnIVgs-bo_jDIYQdGb9gQJ9da36beovlsShRTA0kxFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d76f189634.mp4?token=ZeFsdsdS6WWrJfZm5N_Gky5-7h7crt_kNEJ5yYKsM9HzmlZfrmmUeEGEwhFLzP58kvO9zok5FmMO6Bv3W5eEoQwoQD3in03ISwwRoF6yzUsI1xcvnPGJzsztgYR2VuyB1jNgkSX9e46UKeu8w4gOlX3DMts09SM_IB8s-eupkgvFOR4aK_sLPPRZ97fwCg6VxH0wM88k04xHOR5vUWnXeqyLyTOQxnh2q5rpzVW2mp4xho-I48uX2YUcfeBT68TBviwtoJ_OlX8zolknI2Afuv6s-zKa5-tOn1umRJrVso30B6BumudOHGIhg6E09TlV7B0gPZm7zOpFw764CowRBJM-PZHudfmbXkgDyxSfQkjE3uEZ9GIqksA77RAk3kiV2LTKmRl_QC94a2R-yinWIFKwRL7qHG3g4xq4HJfXQpsxa7RqfkoyQJUMCIidJPfr2c1kycenPpytOZno4qIabBzQhP1dKDUL1baITxnVqOzo-Ttb6fZPxZqLnw1TOkOSyf5Cd1jls8ntxpYb_lXpb8B2v93BMldls3oAZuceGjZLYfzXshXs9YtgPR4fdhctN1_oezIj7-gO-LA4tblLNC06oqxH2QsDWE07b6lqKr1uBVorNd6bJmOoJTpa4qKJCnIVgs-bo_jDIYQdGb9gQJ9da36beovlsShRTA0kxFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انتقام رهبر شهید، مطالبه‌ای که خاموش نمی‌شود
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/450908" target="_blank">📅 18:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450907">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bc6b40448.mp4?token=rh5ntSt41DtlwZHTm7DvBCiZgDPFWxM6eCWSUihnQLI1s15SDbm1C3tD1Q6KPOaIFagbgRcZ9IPob1qlefIfd7lW0EgMkLhByWvPxyh1V0fFgvA6FvMhILSOeTZU5WCHFm6dfh_m_CuRO_D1AM4p_HcCSXTSVz_p6c6yWa0wekhpMt4tbm2xW5dCJlkkjt0yIB_ziPDvSkh4erclAHVKI6v5nCZia9faLH26oozByoXPXvCcuCUQfXskYnmpjAf2vcJNIYURvPcjTOsc9VYCwS-7r8LxT7j1yfqrCvI4bX60u1luG1nZiJgnA3S5Ja1QwlJHG6oBcUJjHmAqBVcFkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bc6b40448.mp4?token=rh5ntSt41DtlwZHTm7DvBCiZgDPFWxM6eCWSUihnQLI1s15SDbm1C3tD1Q6KPOaIFagbgRcZ9IPob1qlefIfd7lW0EgMkLhByWvPxyh1V0fFgvA6FvMhILSOeTZU5WCHFm6dfh_m_CuRO_D1AM4p_HcCSXTSVz_p6c6yWa0wekhpMt4tbm2xW5dCJlkkjt0yIB_ziPDvSkh4erclAHVKI6v5nCZia9faLH26oozByoXPXvCcuCUQfXskYnmpjAf2vcJNIYURvPcjTOsc9VYCwS-7r8LxT7j1yfqrCvI4bX60u1luG1nZiJgnA3S5Ja1QwlJHG6oBcUJjHmAqBVcFkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چه روشی جلوی ترامپ جواب می‌دهد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/450907" target="_blank">📅 18:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450906">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360c979e00.mp4?token=b2OMU17quBWfH7jIUdgAatjpjQlQ24bh0pCXzUTVet1PJrZk4Cuh7XxsoyU4n6gKLSvxlev01ZZPGT_SeMdAZON9t_pBhod6xeyS1bd_qN4HGpy9YjyYd9-MD9iu4V3iLNNMj8_y1gm-bDhmdcsTpXC2GqVCOaCLvTSbVdYJnruFK6y_ZXv-CrZ8mQPEufYnM-wmsPAecT0lXyFSWhUypRyubPuBP1uAA9nDO6NqveoZAdvM4oICF-r319ITdbrQPpbLrZTDiW5oCKoOxv_USNlhnXrWTTFe9frb-_vqStdH-PUCFsGzpI9BmDCGLr_oA-9pN9hgsigrkUr5s9P58Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360c979e00.mp4?token=b2OMU17quBWfH7jIUdgAatjpjQlQ24bh0pCXzUTVet1PJrZk4Cuh7XxsoyU4n6gKLSvxlev01ZZPGT_SeMdAZON9t_pBhod6xeyS1bd_qN4HGpy9YjyYd9-MD9iu4V3iLNNMj8_y1gm-bDhmdcsTpXC2GqVCOaCLvTSbVdYJnruFK6y_ZXv-CrZ8mQPEufYnM-wmsPAecT0lXyFSWhUypRyubPuBP1uAA9nDO6NqveoZAdvM4oICF-r319ITdbrQPpbLrZTDiW5oCKoOxv_USNlhnXrWTTFe9frb-_vqStdH-PUCFsGzpI9BmDCGLr_oA-9pN9hgsigrkUr5s9P58Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش ۲.۵ متری برف در شیلی
🔹
در ۲۴ ساعت گذشته، ۲۵۰ سانتی‌متر برف در بخش‌هایی از شیلی بارید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/450906" target="_blank">📅 18:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450905">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6ee473e85.mp4?token=bsOQOoMA5io-8sKzWXyNgXqeIdGhtNwTZ-kJr33sxVRQINxVVT_QKolaBWblWvkfd5FZcmhmAwuLMAZINj6_fqMjCAtAHAMlDH9cNIwogcHIMJeqK9tPNXUh3kxxamO6lE_QC3WA7dG7zyaaBkLyceTSAwZYWLKUaDUUa_Z9sc0FQHi47iuKQEndJs76XMhFvp6rSSHyIqEWXchDQPJuCzzzTQF4jvZ5Pqej_EsQhfK5LVO8jSxiarpjJbhF-Ya8IAJmeYovOVffG2iHEN0ygA_d3r0WhLojUIiDBdsiI_9A5j35pVw5U71ytrHIVyofGEYq2tiYoT7E1VDO0WEYVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6ee473e85.mp4?token=bsOQOoMA5io-8sKzWXyNgXqeIdGhtNwTZ-kJr33sxVRQINxVVT_QKolaBWblWvkfd5FZcmhmAwuLMAZINj6_fqMjCAtAHAMlDH9cNIwogcHIMJeqK9tPNXUh3kxxamO6lE_QC3WA7dG7zyaaBkLyceTSAwZYWLKUaDUUa_Z9sc0FQHi47iuKQEndJs76XMhFvp6rSSHyIqEWXchDQPJuCzzzTQF4jvZ5Pqej_EsQhfK5LVO8jSxiarpjJbhF-Ya8IAJmeYovOVffG2iHEN0ygA_d3r0WhLojUIiDBdsiI_9A5j35pVw5U71ytrHIVyofGEYq2tiYoT7E1VDO0WEYVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، کارشناس حوزۀ مقاومت: پایگاه‌های آمریکا در اردن پاسبان اصلی رژیم صهیونیستی هستند
🔹
تمرکز ما بر اردن باید به اندازۀ سرزمین‌‌های اشغالی باشد. @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/450905" target="_blank">📅 18:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450900">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t7FtsllaODEdVFrH4B6OkF0cjC34S6FR-O_zoKACie0pwQRDDKlHfst7NJBglLYqsJb13ZtckON_nA26cMDb6EtBJO5aern6Cp2kO2lvAZ3JCBDDih32w0Nsfa0W2hyxBmSg_Hzma7hjqfKk6G9_cQzB3hgENS1_3fy4P3J-bR1he37yHaTlb7yRPIDbOcyL4pg2tDRW0mdKskrKMJDP6XN6vn0H4bvlCO3NAxYcddOAizxL_rfwYsiS2YZodL5z1RFHBZkV5G_AJM2DuM6iM7MHdUbrFZpE5fVN6xnbIsXke6BV7HOy-clEVsucp6QwQtRshffxXkhfoheXlkL0pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k8Ive0Ovq7u31tfockwvqiyRonxpWIb53he3b_SrllMilodr30l6ojeMqKYoz87Ixmf7KJL93jFFQ1U_qMw1MFZQ2PIhnKDBu14w_GdwfyYNWhXAVoa47FkW91ToCBkcEKKF8ChwF4yaxxEBsqj4kpfux5s9VedcWeIDUhP0PJleNTUhusdY5Jb7BGgQfNK92L2z0K_qqBnzxADIYGC0cEVzhpYbosXFxtPgUx0x6Sgg6OReMQ28hUlTCUh0NshE8_LF1rG6kOJ4C2cXf6pCEdOjcOjrdzN_MpUQtUfbCZnSGPY0Pyh1dfaSxPp4pK_e-arv-nuC2E_6wPJ36nOBhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n4iF_Bfwwsedb4lcJIpQ80H5u3ZBep6kUSuG0NhktP_0_b5wgFvDKWflOP1ojGYW2_xWn4U4EcuLP0ozWr1cwt4wRz_6qhhj1c4SDMxLp-k7hibHT3B3cuoeNToAjJKgu8xRAUgsuzfgJ_GzskArA3YPY_YDYOLnC-Nv92ACEqY5pvzlBjiMF95H6LyaSru6e0xiXXLFCtXJdhxK6iDxzgdvmG7u1DAo5t5BnoPd4Gyd69sT2cIjuO6Km2ZwBQJ2vQvWcdzSZsRClfgd7BkhQ6VBasDsDsv8gmbZlza6SxZeQeQr4qKunaC5aLihWSgYXuWeGhK8cX15gzRMv1eFZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a1x6-hWGBCNXceQ3-OLlTgZdFKhphXWGGl-Q-TUfgZr_VyLi2kbBCZoQaYC3HG7LNVDmuuTE_uIdTRNJ9cSFR5xqQO1VQrTRdR3UGtUQzadpLYeyxAr3kMWS8500nV500wlXxqq1I79OR_ErvFpWo2zWdrjIvp9cJUjZG6yu6j2WXCg0gOqqszrKYGdWUM85gsHJLI4tEXqGoAD__glSkWeCdq9lYMxYTFY8UgYv65m8X0jr83S_yvoDJXlATFYjlNA71m77AYAgNnRV9Z2EQB3FpCwGOCh7wXKqwpzk_7OpGCyk6D7J98j-HLszSInA2FC-G-YjC53-pdxjUn-Gpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pfidtyx8fnYEzF3rxYGJ5kI7Ej089cCsUtk6PS9kGu9kAm0LyIS6cLMXqHsnhWkMZonL3xjOVs2RfkdQzYsOxjyOcxybyy0DAtT1aZpjYPCKEuevxmbCdT7wWomKuYQ56Kc0NPQ4MggUlfzm4IMg4wy3StvY888MMhxGbgUjBmn6lU7EMCUfnSSaCergzA2Gik6QN4otzO73e75rLIGBcnAU9x0ShME4nzTviTz6xr_w_mq6VjDdDI1pe3gIvLR6UAvvVrXQaBIYZpbTL17NTUL2rItyHkkRkCjhqHtDSP1O5XAFYpQZlsjBO2pTysUHeF98cJS4c68y12VllxHuKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم بزرگداشت رهبر شهید انقلاب‌ از سوی آیت‌الله سبحانی
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/450900" target="_blank">📅 18:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450899">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BC9haJ_DQr1mrrdJEKv7mzaxxA_rpEk-JxnVw31sazSl6MVp9t9CcdTpsrnCS9L_G0P4DpuBB2mqsAxw6XBR81ucgKcsNQb0zq6YeDCbiROUoZ2cTKU-KSIIz2W4rGBdHlKAT0DwilWMpZhnJ2KveQsuD4O3Omttpne4eS1iPpo9FnYHzGKFDRWI9YyOQn208BosgyNWSWIL_hwDOwyDthDWnD5QJn1B8B7IDpI-A1FCO6Twn7fI6YsphO1dcsiHf5QT1oPxyRIOkBk2JceCgI7QRd5bbu-ZIKJyIG4B2iJ8srReuJqmuv9WDpyDJ9cQrZnIpjeyKyqM1TxRoecXWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واریز بخشی از مطالبات گندم‌کاران
🔹
بنیاد ملی گندم‌کاران: ۳۰.۸ هزار میلیارد تومان جدید به حساب گندم‌کاران واریز شده است. با این پرداخت، مجموع واریزی‌ها به ۹۳.۱ هزار میلیارد تومان رسید.
🔹
از زمان آغاز خرید تضمینی در فروردین ماه، ۶ میلیون تن گندم به ارزش  ۳۰۰ هزار میلیارد تومان از کشاورزان خریداری شده و حدود سی و پنج درصد مطالبات پرداخت شده است.
🔹
بر این اساس، حدود ۲۰۷ هزار میلیارد تومان از مطالبات گندم‌کاران همچنان باقی مانده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/450899" target="_blank">📅 18:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450898">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🎥
می‌خواهم در پایگاه‌های آمریکا شربت پخش کنم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/450898" target="_blank">📅 17:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450897">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f462e38c0.mp4?token=lNOmKKClD6COBUOQ6tofRd0heAqP6lIdHjzperME__B64nRG0QUsg8C_foa-f752dGZz1HfsE21q1Ooc2ryO4CFiYr5GuJ4srdKZPppSgrXhwKUbflc4IW_a8CsAgbbQORI_D2aomvv_FaxflBrCAResLRRcbPJj_RgmotrYcbqmOFskFD7JAICLZ5_wkVuI27eROdRhZe_FsKLBEyrUqhvpUwrpYVMmMWRcrGZ4CIqdOgxWkuOxIgz5UcbRtft0lfiV5zBRuTUGYAxtvIq6Z1FUOiPA2XzWkDCLq4shZ8htDVA4AZZY7s6mOG7sV7L_KjsAAqQEdy2CKzdiC6N01w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f462e38c0.mp4?token=lNOmKKClD6COBUOQ6tofRd0heAqP6lIdHjzperME__B64nRG0QUsg8C_foa-f752dGZz1HfsE21q1Ooc2ryO4CFiYr5GuJ4srdKZPppSgrXhwKUbflc4IW_a8CsAgbbQORI_D2aomvv_FaxflBrCAResLRRcbPJj_RgmotrYcbqmOFskFD7JAICLZ5_wkVuI27eROdRhZe_FsKLBEyrUqhvpUwrpYVMmMWRcrGZ4CIqdOgxWkuOxIgz5UcbRtft0lfiV5zBRuTUGYAxtvIq6Z1FUOiPA2XzWkDCLq4shZ8htDVA4AZZY7s6mOG7sV7L_KjsAAqQEdy2CKzdiC6N01w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پنجمین تلاش آمریکا برای توقف خبرگزاری فارس!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/450897" target="_blank">📅 17:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450896">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌‌
🔴
سی‌بی‌اس: مقامات آمریکایی اعلام کردند که ایران در این هفته دست‌کم ۲ پایگاه در اردن را هدف قرار داده و چندین نفر از نیروهای نظامی آمریکا مجروح شده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/450896" target="_blank">📅 17:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450895">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKlJ0-CA3EiEQTxPVymFkMSTzArkLloTj1Vh1PzATGgnx1VAqsFxMRGl9jPWXJkiZUtrOIKSAfX3VCvSZY7dfu-lxZq0VOKDT_bOubcL3VQaideE0CZ4bTB7uSwjYFkaAhuoitfgZZdjWZ7S-U_qB9GeHfylQrzB7aBjsV4Eg93M8jOE_5r4e4wh9PhBLJ7VPyB9mPy9-zPMMUt8AQWFRAtOIbfcAL5d95nA47eMud4TMZRW2KdLPITVR0Scfj8WSc1DAGrO-h4QKV7UWXVknFiWMHWJx__zLsNFiPpxnLKBB3FASZzMTaQtqDfpK_cmfwhDknfAxwMQuaNUUJQjlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسران والیبال ایران بر بام آسیا ایستادند
🔹
تیم ملی نوجوانان والیبال ایران در فینال قهرمانی آسیا، ۳-۱ ژاپن را شکست داد و بدون شکست قهرمان شد.
🔸
ایران در ۱۳ دوره‌ای که در مسابقات شرکت کرده موفق به کسب ۸ عنوان قهرمانی، ۳ نایب قهرمانی و ۱ مدال برنز شده و پرافتخارترین کشور این رقابت‌ها محسوب می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/450895" target="_blank">📅 17:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450893">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1dd38297f.mp4?token=PVbWfsuMfNdf4J4T8f4UJr7rfFsj3LtC_7XWZopxVNQjEecV_e39KtB282J8FbeHhkMc7KyNU_q-fFKHkZqHIs8IBWgIJfa06IUOHKbEUkeubSruG--5OMr3JigvjgAyKr8IfhNygnGMgFreI9M6TcsAfffJ1OrlaGHREyxenjo1WlhsilxUmZ9UbO9yPRcJvQ6CHAJbPm6U2aFXvUDlBx-t_hqZo-jQTRwNIfoYPVOBjd5_rNkew60oBbROn8a2dUtJ-JHMvywlfHPMwRkW21QpzIc3RV3YP3Xy4DF7HHm2UeM-DQyEFAImxgsSbyaKjTUzLiH6yOduhM4hBFVfpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1dd38297f.mp4?token=PVbWfsuMfNdf4J4T8f4UJr7rfFsj3LtC_7XWZopxVNQjEecV_e39KtB282J8FbeHhkMc7KyNU_q-fFKHkZqHIs8IBWgIJfa06IUOHKbEUkeubSruG--5OMr3JigvjgAyKr8IfhNygnGMgFreI9M6TcsAfffJ1OrlaGHREyxenjo1WlhsilxUmZ9UbO9yPRcJvQ6CHAJbPm6U2aFXvUDlBx-t_hqZo-jQTRwNIfoYPVOBjd5_rNkew60oBbROn8a2dUtJ-JHMvywlfHPMwRkW21QpzIc3RV3YP3Xy4DF7HHm2UeM-DQyEFAImxgsSbyaKjTUzLiH6yOduhM4hBFVfpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هجوم مسافران برای خروج از کویت
🔹
بعد از هدف‌قرارگرفتن اهداف آمریکایی در کویت، فرودگاه کویت روزهای شلوغی را سپری می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/450893" target="_blank">📅 17:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450891">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Aq0_QvuEcIe8F_6OgxVwjhkeVqmFVLCG85VoSEfYU52UtfKv2GcrmDG9D5ce2j6Ir73Gk8A2LlTnN8u-z0PIQBBD9V8RpIl5JHYwZ5ahhwCgYhtkUL3e55MRPhQkZMgo5eoZXKACTZmx0S2Zqc0txWVlXl1uXck7XnEL0cZUmUGIzF84hoywobEwC78_VkgarhNjK-ro_Qh7yDSvk0hmC1E6I74EbGHOjW8haYXtSMrDTVT3XybHL6_07B-ve8VYRctKHPtQuYJSZZZfvtgml7lTQmen1kQUXkuUiumhTLWpkvfxov-HLQVduheq1G8QnhFL00n4pIhvMYJLWwxjlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZ6jczelrnpINpPOFrA7srhZv5V2ho0uOjPibHn9DIIvKQxlUCPAaW7inrnJqSkceQn9SdW53p4UgEoJ-WFaUEK1u1Jcwc8-zJB2z9wK8uEdF9FYhQUef5D1SLvEtuK6-1Lj487cR3yDSa1YpXjYrYjY2s8oHNeib5ECnk6r7V4xex8728LKfvljomG8aFGSZ3xZoYut5UYVdeK1yta0z5phRhenwffOBBoXn4EhqDMAdy_-29kSPAy-tf-L96OJtUL5ntioF3IEqA5wqcA8HniiIlkjztOAUTV9IhCfrb_vvi9HRJPuvGYGYCiPvEE_Cvjm_QrpxXpKUqbVqkGsuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
حمله به تروریست‌ها در سلیمانیه عراق
🔹
به گزارش منابع خبری، در این حملات، مقرهای تروریست‌های تجزیه‌طلب ضد ایرانی هدف قرار گرفت.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/450891" target="_blank">📅 17:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450890">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/behevu-dKwY4OmN7dDb3Spk7TM4znK2FakOInoEPyJATzmBv3vYyM3-vORG6Nzxi3ExFwKHdMmx4Ix8J37uhOIGGgqNWYhCAphgy_OUOvwI6EfV0GzVIqVSTDpHczsFmGYiJIOg6LdTloiN8l1XWN0F4r59a3z23PfQfM4Mfc4aOgs6oRm4WxFjBbG-f1MBgTfCwTGIsMJ3kJ5EPMH_BWjw5iKt-WdJBS5nm20gEF_FOZe5NeS785FnTYZdHP3Z8gxu7PCB4U3UOIXTFQw3q8adxI2NmzB90MRcCAoGm_IFdrb9ZWnfKyBpicyI9nvgC5woz5Y7lKEJ0mqxFEirZZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع برق بیش از ۵۰۰ ادارۀ بدمصرف در تهران
🔹
شرکت برق تهران: تاکنون محدودکنندۀ مصرف برق در بیش از ۵۰۰ اداره که از سقف مجاز مصرف فراتر رفته بودند، عمل کرده و برق این ادارات قطع شده است. این رویه تا زمانی که ادارات مصرف برق خود را کنترل کنند، ادامه خواهد یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/450890" target="_blank">📅 17:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450889">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
هشدار یک مقام امنیتی در گفت‌وگو با فارس: در صورت حمله آمریکا به زیرساخت‌های ایران، فرودگاه‌ها و بنادر امارات باید فوراً تخلیه شوند
🔹
یک مقام آگاه در نیروهای مسلح در گفت‌وگو با خبرگزاری فارس ضمن هشدار نسبت به پیامدهای هرگونه اقدام نظامی آمریکا علیه ایران اعلام کرد: اگر امشب آمریکا به زیرساخت‌های غیرنظامی کشور حمله کند، برای حفظ جان شهروندان از حملات متقابل ایران، فرودگاه‌های دبی و ابوظبی و همچنین بنادر فجیره و جبل‌علی باید فوراً تخلیه شوند.
@Farsna</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farsna/450889" target="_blank">📅 17:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450888">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c448a578a.mp4?token=o2Y7uX7Y0uafeEPTYsvvkrSqnVe79LXOhDsdieuXVHwtRXcDv6plHvewLMVBdQuaMVjJgFXvk9W0bJRWrusINAD-8ReQC8XrSIjV1AND6uM-dfMg1MbJ0I5mp2p3Ce8eBatlzj24P6YGjuYoq7lJXtBeIyJwxigUodF7nN2E9ULaTc5KkuNFLCpB7enoOsAyR7yv7duewDQ_-s4-Zc72iuMFhkK43nQ76Fo5stnLmG-tviv_hduUCfA6H6It5tburoqWMNs6pLARAUzP27ThhHtWVOUrc2e-UU9b1-K7tdQC9gvpdgYaLaWjPnOt99qk1Czej4vNTeOMzWLrB3mfOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c448a578a.mp4?token=o2Y7uX7Y0uafeEPTYsvvkrSqnVe79LXOhDsdieuXVHwtRXcDv6plHvewLMVBdQuaMVjJgFXvk9W0bJRWrusINAD-8ReQC8XrSIjV1AND6uM-dfMg1MbJ0I5mp2p3Ce8eBatlzj24P6YGjuYoq7lJXtBeIyJwxigUodF7nN2E9ULaTc5KkuNFLCpB7enoOsAyR7yv7duewDQ_-s4-Zc72iuMFhkK43nQ76Fo5stnLmG-tviv_hduUCfA6H6It5tburoqWMNs6pLARAUzP27ThhHtWVOUrc2e-UU9b1-K7tdQC9gvpdgYaLaWjPnOt99qk1Czej4vNTeOMzWLrB3mfOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هجوم مسافران برای خروج از کویت
🔹
بعد از هدف‌قرارگرفتن اهداف آمریکایی در کویت، فرودگاه کویت روزهای شلوغی را سپری می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/450888" target="_blank">📅 17:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450887">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6hsXUnDEbiIPfL7M14V7QmdmS9I1jz5nBtYB3VkzoOzfcTcuDCCaj519RVwPX-NXURiCly33aObrMR8CF6SwEYoB5Oadsiv2MRtpgInW2eXLWXNvNB2YL1a4GXM00WSMPOlsibtwR5yqhTC6QnkGY1qijVKs4v4fHRNycSxjYTbHiD2MNknD8WSCR79rVtLNZpw4o89i5hNJ1gwVq1lIi6-WUF-UM4bfux2oNszIMYaprAiZrVjTYGQ7BxJ8jClQ8WU0RT1TXUJTIBb9CalfgODmShNBVQNK10YJPNXsBGm-Js0lXp-voGZ3HA6Sn9t48mDs2pVNVKGjV0FcGhsPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل تصاویر ویرانی مراکز حساس کویت در حملات ایران را محو کرد!
🔹
براساس بررسی تصاویر ماهواره‌ای گوگل، مشخص شد که این شرکت تصاویر با وضوح بالای چندین تأسیسات حیاتی در منطقه «الشعیبه» کویت را به‌طور عمدی محو کرده؛ این تأسیسات شامل نیروگاه برق، تأسیسات آب‌شیرین‌کن،…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/450887" target="_blank">📅 16:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450886">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2109385f6f.mp4?token=ShsMJmLLdthz701kDl67Gykw6FnonQcYW1uVzfUwgm8y-5-2K1rOUDx1XCq3CT_J2ytiA3rR1xOc2Sq12_XndDQCLLDbrqYAimvQC-C4lZ4iJ4pjrjDk2UDDuLdeeW43J8sx54XgwuN7EyaeSwIRb8-_CKnpZfENfYtnYGfP9eczUuUvyZVva1Tqkyi6BsYZpfjp_VxVqGOvhYDGezbT6cEhuup9ig-FrdnXxBraY7F6aVceCd2LHgBwio9ackOdfMThZGVAn9fbOsZpp75g5SqrMH_q-RO_Qz2tDgDdv5ssS7h_O4j6FT2-1EYa18N1qeH4WevXS4R9GXqGbPePxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2109385f6f.mp4?token=ShsMJmLLdthz701kDl67Gykw6FnonQcYW1uVzfUwgm8y-5-2K1rOUDx1XCq3CT_J2ytiA3rR1xOc2Sq12_XndDQCLLDbrqYAimvQC-C4lZ4iJ4pjrjDk2UDDuLdeeW43J8sx54XgwuN7EyaeSwIRb8-_CKnpZfENfYtnYGfP9eczUuUvyZVva1Tqkyi6BsYZpfjp_VxVqGOvhYDGezbT6cEhuup9ig-FrdnXxBraY7F6aVceCd2LHgBwio9ackOdfMThZGVAn9fbOsZpp75g5SqrMH_q-RO_Qz2tDgDdv5ssS7h_O4j6FT2-1EYa18N1qeH4WevXS4R9GXqGbPePxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، کارشناس حوزۀ مقاومت: پایگاه‌های آمریکا در اردن پاسبان اصلی رژیم صهیونیستی هستند
🔹
تمرکز ما بر اردن باید به اندازۀ سرزمین‌‌های اشغالی باشد.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/450886" target="_blank">📅 16:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450885">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اطلاعیه دولت: مراسم بزرگداشت امام شهید انقلاب که مقرر بود روز چهارشنبه از سوی دولت جمهوری اسلامی ایران برگزار شود، به روز یکشنبه ۲۸ تیرماه، ساعت ۱۰ صبح موکول شد.
🔹
این مراسم به میزبانی قوای سه‌گانه کشور در مصلای بزرگ امام خمینی (ره) تهران برگزار خواهد شد.…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/450885" target="_blank">📅 16:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450884">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45191fb108.mp4?token=CqkdLCMwplOkUWJbhWKx69BmrReipQqXnBIqDo9SUIKe8gXUsx4EabE4pK0RMbMqyFsJRcY5hsYd6VsJ3orrZH3gpiAnIuSqRw-raQJSPnrj8Gh1r8OtwDzHvMbnXZxkFxmLLUVAUodQSG1Rr0VD_l0I0666x8lef6iwzvRyuexq53RTzbsuVHUoqfh7XtCUni6haWTQ-nTbSzueAz4_8tZe1aGyUO65ENeGpop0srt0vkQ1fJjaSxkWEnkOQZ8QGPb005rFupsU0oaE6-JPrjfgkUhSS-DgCzVZ5LyPzgOes5-jWRolWbR6M6BwQXrZ9gL4KxQ1J9EA6ocl640csQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45191fb108.mp4?token=CqkdLCMwplOkUWJbhWKx69BmrReipQqXnBIqDo9SUIKe8gXUsx4EabE4pK0RMbMqyFsJRcY5hsYd6VsJ3orrZH3gpiAnIuSqRw-raQJSPnrj8Gh1r8OtwDzHvMbnXZxkFxmLLUVAUodQSG1Rr0VD_l0I0666x8lef6iwzvRyuexq53RTzbsuVHUoqfh7XtCUni6haWTQ-nTbSzueAz4_8tZe1aGyUO65ENeGpop0srt0vkQ1fJjaSxkWEnkOQZ8QGPb005rFupsU0oaE6-JPrjfgkUhSS-DgCzVZ5LyPzgOes5-jWRolWbR6M6BwQXrZ9gL4KxQ1J9EA6ocl640csQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاکر کارلسون: ادعاهای آمریکا درباره قدرت نظامی‌اش، پوشالی از آب درآمده است؛ تحقیر مداوم ایالات متحده، چشم جهانیان را به واقعیت باز کرده؛ ارتش ما با بودجه ۱.۵ تریلیون دلاری حتی نمی‌تواند یک تنگه را باز نگه دارد
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/450884" target="_blank">📅 16:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450883">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">۱۱۶ دکل مخابراتی هرمزگان از مدار خارج شد
🔹
اداره‌کل ارتباطات هرمزگان: در حملهٔ دیشب آمریکا به‌خطوط انتقال ترافیک و پهنای باند در بندرعباس و حاجی‌آباد، ۱۱۶ دکل مخابراتی از مدار خارج شد.
🔹
درحال‌حاضر تلفن ثابت، تلفن همراه و اینترنت در برخی مناطق شمال استان…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/450883" target="_blank">📅 16:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450882">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رئیس کمیسیون اصل ۹۰ مجلس: ادعای تبرئۀ زنگنه کذب محض است
🔹
حجت‌الاسلام پژمانفر: ادعای تبرئۀ بیژن نامدار زنگنه در پروندۀ کرسنت، کاملاً کذب است. اگرچه رأی صادره در اردیبهشت‌ ۱۴۰۵ مبتنی‌بر «تبانی در معاملات دولتی» را از حیث میزان مجازات ناکافی می‌دانیم، اما واقعیت این است که در مرحلۀ بدوی، زنگنه و مهدی هاشمی رفسنجانی به یک سال حبس و انفصال دائم از خدمات دولتی محکوم شده‌اند.
🔹
البته مهدی هاشمی پرونده‌های دیگری نیز دارد و ۶ نفر دیگر که مرتبط با این پرونده هستند، هر کدام به ۳ سال حبس و یک سال انفصال از خدمات دولتی محکوم شده‌اند.
🔹
ما این اخبار کذب را بخشی از یک جریان سازمان‌یافته می‌دانیم که در برابر این فساد بزرگ شکل‌گرفته در کشور، تلاش می‌کند به مردم القا کند دستگاه قضایی در برخورد با مجرمان هیچ اقدامی انجام نداده است.
🔹
این احکام هنوز قطعی نشده و پرونده در نوبت رسیدگی تجدیدنظر قرار دارد و در ماه‌های آینده بررسی خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/450882" target="_blank">📅 16:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450879">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4286e833.mp4?token=hUXGZTjYO_s9ZSfFsyyIMpYy_cAIrYe695mMNvr0TymNx8dxkmH2_4kxgXTDXX_vYDdTqDJ15K4UVdgHRyL7NWhbvY3G-MEO-0yFehaK_Xnemp0QcH1YigM9FBASOc4nTSAtfsmSr47u4GrkdfixiFRpMA18CUc5pXEgixlDAyYnMmDLTQwy8G6DJejDE1a3nycsJ2bvgOSmhbxFO0Boz0OTS9uot-8sfGG3uUGyy2VkStXYEK80V6CAI2hbVcodLxML1LQscNcQYz-Woto8glStaI5Vdk5K8DyQ1A3Gle2JrOe6YIl9J1o4Lr2MM3OS4Z6eKhHumzknffKUTMFciw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4286e833.mp4?token=hUXGZTjYO_s9ZSfFsyyIMpYy_cAIrYe695mMNvr0TymNx8dxkmH2_4kxgXTDXX_vYDdTqDJ15K4UVdgHRyL7NWhbvY3G-MEO-0yFehaK_Xnemp0QcH1YigM9FBASOc4nTSAtfsmSr47u4GrkdfixiFRpMA18CUc5pXEgixlDAyYnMmDLTQwy8G6DJejDE1a3nycsJ2bvgOSmhbxFO0Boz0OTS9uot-8sfGG3uUGyy2VkStXYEK80V6CAI2hbVcodLxML1LQscNcQYz-Woto8glStaI5Vdk5K8DyQ1A3Gle2JrOe6YIl9J1o4Lr2MM3OS4Z6eKhHumzknffKUTMFciw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
ارتش کویت از تداوم حملات پهپادی و موشکی به خاک خود خبر داد
🔹
ارتش کویت با بیان اینکه چند موشک و پهپاد را در حریم هوایی خود رهگیری کرده است، گفت که ترکش این موشک‌ها باعث وقوع خسارات مادی شده است.  @Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450879" target="_blank">📅 16:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450878">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای خطر به صدا درآمده و از شهروندان می‌خواهیم که به نزدیکترین مکان امن بروند.  @Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450878" target="_blank">📅 16:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450877">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bac2171a2.mp4?token=XbzWxcouTPiDY4WnP9xgshuTlmh7_tSgCiFoOGpBtoBVL5E5KRcDK26IA3GS_86FVQPaJLsz-qeqGHzOt4EH7SzHa3UCcpi32Qj9QFp7_CoEun6i1bzXODAsVZHl_8847yqLJg-us1JbSS-XiccszSMVubbVIwVHOZfumkXsU9WNbinMLqt4mPss0qXUNoI7Yd3X_YUIMzhOS-yhmeiowoig9ZI5QyFBRPAeyjeJ2S92fLaCrESjHCLzypSvUhQ77qVBgbmwtA0zund9jpO38N45MplgysOTkh4GgBd0G2TrG5y4VzoGusBgjRNZA7sNu9LO2r65TzBRvV40xmHO7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bac2171a2.mp4?token=XbzWxcouTPiDY4WnP9xgshuTlmh7_tSgCiFoOGpBtoBVL5E5KRcDK26IA3GS_86FVQPaJLsz-qeqGHzOt4EH7SzHa3UCcpi32Qj9QFp7_CoEun6i1bzXODAsVZHl_8847yqLJg-us1JbSS-XiccszSMVubbVIwVHOZfumkXsU9WNbinMLqt4mPss0qXUNoI7Yd3X_YUIMzhOS-yhmeiowoig9ZI5QyFBRPAeyjeJ2S92fLaCrESjHCLzypSvUhQ77qVBgbmwtA0zund9jpO38N45MplgysOTkh4GgBd0G2TrG5y4VzoGusBgjRNZA7sNu9LO2r65TzBRvV40xmHO7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بغض‌های سفارشی برای جنوب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/450877" target="_blank">📅 15:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450876">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ba45eebb.mp4?token=lgK9yY6MkMmyfFCIUOduBI0GWzHiD32lL7CKhtt57XiJ7OWmXATGL0oavPYawG3Zf_C_LOqwDNFE-_Rh8ZOKfK0qvSJ8OnY66VkWJk5nBnjBRVa9W38YH8NRrsrifhbuIlPUIvoCoXCQpCzqrguss3tTH9LkDV0W_8xw_k26eo8veECclIaOK1g5qbDLbOaZ_zv_7nR6fz5JShwewjpbm8waLj2mmXVbDaVh3QePNgW8YEAWCNpb56ceY1kd0T6gzJ1JwbH1iFotuuPT0bTaF5YwWdbt9fjhrX_e7NQRu84gHQyeJyJgX_uDlkRKjrtwITYM1VOIoFS8C5ckMwDCkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ba45eebb.mp4?token=lgK9yY6MkMmyfFCIUOduBI0GWzHiD32lL7CKhtt57XiJ7OWmXATGL0oavPYawG3Zf_C_LOqwDNFE-_Rh8ZOKfK0qvSJ8OnY66VkWJk5nBnjBRVa9W38YH8NRrsrifhbuIlPUIvoCoXCQpCzqrguss3tTH9LkDV0W_8xw_k26eo8veECclIaOK1g5qbDLbOaZ_zv_7nR6fz5JShwewjpbm8waLj2mmXVbDaVh3QePNgW8YEAWCNpb56ceY1kd0T6gzJ1JwbH1iFotuuPT0bTaF5YwWdbt9fjhrX_e7NQRu84gHQyeJyJgX_uDlkRKjrtwITYM1VOIoFS8C5ckMwDCkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: تعهداتمان در تفاهمنامه اسلام‌آباد را متوقف کرده‌ایم
🔹
معاون حقوقی وزارت خارجه: آمریکا تمام تعهداتش در چهارچوب یادداشت تفاهم اسلام‌آباد را زیر پا گذاشته و متوقف کرده است.
🔹
ما هم تعهدات خود را متوقف کرده‌ایم، در حال اجرای آن‌ها نیستیم و مشغول دفاع از کشوریم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/450876" target="_blank">📅 15:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450875">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سخنگوی قوهٔ‌قضائیه: دادگاه رسیدگی به پروندهٔ شهید امیراحمدی آذر برگزار می‌شود
🔹
پروندهٔ شهید سلمان‌ امیراحمدی که در اغتشاشات سال ۱۴۰۱ به شهادت رسید در دادسرا تکمیل شده و دادگاه در آذرماه برگزار می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/450875" target="_blank">📅 15:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450874">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای خطر به صدا درآمده و از شهروندان می‌خواهیم که به نزدیکترین مکان امن بروند.
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/450874" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450872">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd7c7e6a3e.mp4?token=fDPNv6KUB9HoRR0uDbszN-NdKFwE0LKjJF3upaeFospejXN6TV5Zmh_NPpqvYkJ45Cxh_OwsHwSSaLGNqYkagZdhKaeDRuq0Q6kHxMWL7u0XWoM-Ohi9mahbthXnGSrbgVAWH06Gl8ruSUrNtHBvosPEo_XtaG8qEdyR8z9EOvpaaDiCox4r0lAfiunupDU-G9KbyRJ4diRZjyJXbFu439__5u8lPuYFLAdbC3v2BTObXHKUGcP1wnAqMdrH9Tlt7WBr0l45ZqflNacm7gBg44CzNlpt0MOnRYgA9P9zSX_IQ99BIR0UNHDSH0wfbyfB6HudYucfjiTbPp3rkMrVt7XFoKpdjUrFnsW9qAvJ7h7Ouj64FYkEthgqFcnGDZD5SxBsTPTy-Cy3EpgRDBWraSmjlLb9-HNmwn1P2OTo8o2h29fNub7ee5q04nUD4HRZPSPE6JedTkuSh7WfFqHXgs6fAZY8k4q4MyOJIXhO9aHppVs6OCohkXDbPj-s6w0AZsklfc2hScOiXvBEc1BaeasKxV9X65r_OrHkl2Mij5VwrBUQdlyBFXVJugdI9ydA4ds8_k5znfL4INpQTk26uJe9EBr2fAlPDaMpr7SD1ZdUjuF_pAG66RD6pGqCAsBNdMzaZoiIjpRcskuX5AZ_Xf8U31OrVDsHW4UYE5FVlN8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd7c7e6a3e.mp4?token=fDPNv6KUB9HoRR0uDbszN-NdKFwE0LKjJF3upaeFospejXN6TV5Zmh_NPpqvYkJ45Cxh_OwsHwSSaLGNqYkagZdhKaeDRuq0Q6kHxMWL7u0XWoM-Ohi9mahbthXnGSrbgVAWH06Gl8ruSUrNtHBvosPEo_XtaG8qEdyR8z9EOvpaaDiCox4r0lAfiunupDU-G9KbyRJ4diRZjyJXbFu439__5u8lPuYFLAdbC3v2BTObXHKUGcP1wnAqMdrH9Tlt7WBr0l45ZqflNacm7gBg44CzNlpt0MOnRYgA9P9zSX_IQ99BIR0UNHDSH0wfbyfB6HudYucfjiTbPp3rkMrVt7XFoKpdjUrFnsW9qAvJ7h7Ouj64FYkEthgqFcnGDZD5SxBsTPTy-Cy3EpgRDBWraSmjlLb9-HNmwn1P2OTo8o2h29fNub7ee5q04nUD4HRZPSPE6JedTkuSh7WfFqHXgs6fAZY8k4q4MyOJIXhO9aHppVs6OCohkXDbPj-s6w0AZsklfc2hScOiXvBEc1BaeasKxV9X65r_OrHkl2Mij5VwrBUQdlyBFXVJugdI9ydA4ds8_k5znfL4INpQTk26uJe9EBr2fAlPDaMpr7SD1ZdUjuF_pAG66RD6pGqCAsBNdMzaZoiIjpRcskuX5AZ_Xf8U31OrVDsHW4UYE5FVlN8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آن شب، آن بیمارستان
🔹
با اینکه خدمت‌رسانی دوباره در بیمارستان شهید بقایی اهواز پس از تهاجم هواییِ آمریکا به محدودۀ آن از سر گرفته شد؛ اما آنچه در آن شب رقم خورد، از خاطرات مردم خوزستان پاک نمی‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/450872" target="_blank">📅 15:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450871">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">۱۱۶ دکل مخابراتی هرمزگان از مدار خارج شد
🔹
اداره‌کل ارتباطات هرمزگان: در حملهٔ دیشب آمریکا به‌خطوط انتقال ترافیک و پهنای باند در بندرعباس و حاجی‌آباد، ۱۱۶ دکل مخابراتی از مدار خارج شد.
🔹
درحال‌حاضر تلفن ثابت، تلفن همراه و اینترنت در برخی مناطق شمال استان با قطعی مواجه است که تلاش برای وصل‌کردن آنها در جریان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/450871" target="_blank">📅 15:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450870">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cckDhqideT2AYneSjyre6Igp5BsXAhlAq8eBWHIDnDt_tKusUCot7ELNUWo5fV4YA--8wvCLjwPSkS5Db-VNy635jKCie-BOc6duUHswffB94QXPAhwitgAyq9IIi72naA0_aH9oSZG6VJDNNmbsStNyf3LmSIkRz-mD-0PN__As7vfNIP7UFSQDuC56lo2KMw_Yi2YD8OC0KR61qf-Co1X85dLXbmRZlHmRdKHmFfqFNev4oUualBQAgnQ8PAvz796E60KjQ-xG0Z6HYGR51Qo-UPTExudGRdZVDxhHrTSU6pys0nYKPNr6BC4mWaC1AA6IDYBSz9oQW5H_oZO8hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
حملات پهپادی به مواضع آمریکا در اردن
🔹
درحالی‌که منابع خبری از شنیده‌شدن صدای چندین انفجار در اردن خبر دادند، ارتش این کشور مدعی رهگیری ۳ پهپاد شده است.
🔹
منابع خبری می‌گویند در این حملات که با چندین پهپاد انجام شده، پایگاه‌های آمریکا هدف قرار گرفته…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/450870" target="_blank">📅 15:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450869">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3238bd6396.mp4?token=OJC3ygIWudXbbf7kbVAUA6AQmN4gSvWAVDMw-AtCdrscY7DEtwxvhiIiF-REmLpE4-ns7V2GPYzu4wnykJXwIyqzrxAJ--QzsoakOr_01Y_xsp4pcXqzX4-jjCTBsmCsPnGciRcYqov-hNlLivO99y5-UNqobFEwSKs5-9Wx9mIL3BI-kCAfhnjZlu0UPaVDp9YQo62_7rsmqQs2zllHp6yJ96AGtz313LpAXJ6mobGfryXnuANOisQW5ESR_eISS_r5GbHWba8-pjgOPCkIfhQITfiK4_H-i2iCsDJIYNIkX3hiUqkDmDCGBjgPfNfBFR1kRXZHm21Gpdk2U5wo7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3238bd6396.mp4?token=OJC3ygIWudXbbf7kbVAUA6AQmN4gSvWAVDMw-AtCdrscY7DEtwxvhiIiF-REmLpE4-ns7V2GPYzu4wnykJXwIyqzrxAJ--QzsoakOr_01Y_xsp4pcXqzX4-jjCTBsmCsPnGciRcYqov-hNlLivO99y5-UNqobFEwSKs5-9Wx9mIL3BI-kCAfhnjZlu0UPaVDp9YQo62_7rsmqQs2zllHp6yJ96AGtz313LpAXJ6mobGfryXnuANOisQW5ESR_eISS_r5GbHWba8-pjgOPCkIfhQITfiK4_H-i2iCsDJIYNIkX3hiUqkDmDCGBjgPfNfBFR1kRXZHm21Gpdk2U5wo7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار هرمزگان: با وجود تهاجم به آب‌شیرین‌کن‌ها در ۲۰ روستای شهرستان جاسک، اختلالی در روند آب‌رسانی به مردم وجود ندارد
🔹
در روزهای آینده آب‌شیرین‌کن‌ها وارد مدار می‌شوند.
🔹
دشمن فکر کرده با زدن چند پل و تونل می‌تواند در روند ارتباطات استراتژیک بندرعباس…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/450869" target="_blank">📅 15:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450868">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5afb3ddfbf.mp4?token=hQ-GVjjwfRdEDx8zhZ06pZRZBaV00wPwhOqdRREIQIvJ7FYXo_-9-b5msYoCahRNytoB07TXTMahnqJJRskR6dNPxGs2Rpkb71FN5S4q7F0o4wQF7rhA4FqmVooixe2R6U-umW7Fmva-hy3Jx4hpDO6Gga_My2GuLaqinC7twq5R-8VgD33e5gBeBBduRNRaAqg2FDqYxOToB7dOrhRpgbyRu72orZN9QMRQ1iC33B2trbfXO6chBPgea_b-2rVQL64DUOd0zeTKogsqny-fX-5rygst3TJns4yZ4eyfjtn_yJfPF6j6WeCvUcPWAlfeO6S4Egwh4iX2TTOmN1gStQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5afb3ddfbf.mp4?token=hQ-GVjjwfRdEDx8zhZ06pZRZBaV00wPwhOqdRREIQIvJ7FYXo_-9-b5msYoCahRNytoB07TXTMahnqJJRskR6dNPxGs2Rpkb71FN5S4q7F0o4wQF7rhA4FqmVooixe2R6U-umW7Fmva-hy3Jx4hpDO6Gga_My2GuLaqinC7twq5R-8VgD33e5gBeBBduRNRaAqg2FDqYxOToB7dOrhRpgbyRu72orZN9QMRQ1iC33B2trbfXO6chBPgea_b-2rVQL64DUOd0zeTKogsqny-fX-5rygst3TJns4yZ4eyfjtn_yJfPF6j6WeCvUcPWAlfeO6S4Egwh4iX2TTOmN1gStQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازگشایی یکی از تونل‌های آسیب‌دیده محور بندرعباس-سیرجان
🔹
مدیرکل راه و شهرسازی هرمزگان: یکی از دو تونل گلوگاه شهید میرزایی در جادۀ بندرعباس-سیرجان بازگشایی شد.
🔹
تردد خودروها از ساعتی پیش در این تونل آغاز شده و عملیات تخلیۀ ترافیک این مسیر درحال انجام است.…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450868" target="_blank">📅 14:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450867">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‌
🔴
شرکت نفت کویت: صبح امروز یک مرکز نفتی مهم توسط ایران هدف حمله قرار گرفت و خسارت‌های زیادی به آن وارد شد. @Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/450867" target="_blank">📅 14:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450866">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d8390497.mp4?token=oFZIZS2kttlzOCwrdGVJxvRT_9PoccSw2ceGQQc3kpHYE1Nu_ItvCAFFNk3QTvUHJxrapeWz6QPpoB3YYacHvjbdXrIh42MC8lBsMp4ykSmsBtWrzAaOF_b6Z1gO8r-Aye3osl24bYCQ8ORRgPH-LJ0CijRNXVSrvmqjEl-99reX_c5Q1L1Vb0Eh-fi4_gHQqkhzax5YtZkl7q3YFfDfVuOicyIHzddI_vIulqZKSrA15TxuwRGvly_SAfvOVTqQ6TXWeQmj9DwtzN1OyyqahfwpbG48GfXznN_w4YfHV2gz-1EKz8LbenNoFou0Un2V5KMqzYt698wSmGHLKMR8qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d8390497.mp4?token=oFZIZS2kttlzOCwrdGVJxvRT_9PoccSw2ceGQQc3kpHYE1Nu_ItvCAFFNk3QTvUHJxrapeWz6QPpoB3YYacHvjbdXrIh42MC8lBsMp4ykSmsBtWrzAaOF_b6Z1gO8r-Aye3osl24bYCQ8ORRgPH-LJ0CijRNXVSrvmqjEl-99reX_c5Q1L1Vb0Eh-fi4_gHQqkhzax5YtZkl7q3YFfDfVuOicyIHzddI_vIulqZKSrA15TxuwRGvly_SAfvOVTqQ6TXWeQmj9DwtzN1OyyqahfwpbG48GfXznN_w4YfHV2gz-1EKz8LbenNoFou0Un2V5KMqzYt698wSmGHLKMR8qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ شهرسازی هرمزگان: یکی از ۲ تونل گلوگاه شهید میرزایی در جادهٔ بندرعباس-سیرجان بازگشایی شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/450866" target="_blank">📅 14:41 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
