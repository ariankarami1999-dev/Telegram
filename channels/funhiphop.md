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
<img src="https://cdn4.telesco.pe/file/k1ZK-KXDRipi8sWQmzXa8XxorNQYEaCNYx8dsH2qpFg4F0iQebO0xPzW35ZqghGNzA2iN5mZxej1U49W4ZiehDwvavC_CVVPLPrbLwNXf9uMprZL2ePFWffAd7rM2CQUaYOVKq3PQcACTO8gnWrI382lJBsc-cYMXmiqE3Et_DU0yai5o4_5I4WATwBRf9_cueXKpeyb6Sz9kGegYmHGcKvVkGYn48Ea21vpVzPBUCfG2E8jyvo1FhfW64owmJq6BfBICNLbZFLZPs8MVVo3SC3w1jFZ-NPSV15niQQDfOte1CeJNY8FphE5dVN4VsNRZGljquIeOKXAGU_7GSz2Yw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 152K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 14:16:55</div>
<hr>

<div class="tg-post" id="msg-75345">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سعی کنید تا حد امکان از نوبیتکس استفاده نکنید فعلا، آمریکا بدجور سیخ کرده روش هر لحظه ممکنه همچیشو فریز کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 393 · <a href="https://t.me/funhiphop/75345" target="_blank">📅 14:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75344">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اهواز امروز  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/funhiphop/75344" target="_blank">📅 13:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75342">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c99MVQUhtvgYooQRrEhIf2KWXYG6KdGdFjFImsNZ5gdpDwVMmNo14RiHtJBwT9kML9wTTVPLYjnJEfInxtTM9KQOEGHHk7TSVXukXcr-hirAZxorIFBpvMBzT1Cao0AxQHWH4A11hAWZArQgkpSFZmqk3Jk-ZHu9pWaSBLdnkGXS7S-E8tmrcTeGJl9wv6vbgVa-3Viyxq8JsDaTECn7y92FAsjoERk1bl71IfLZ_rDJH6Dz7PBpR_HxS7GI_EczAoAM0drqj6Nmqvt4FxqvOIVJFKsLUayBEjVIIYaX5I_lTOb2GmZyslyUihQL-GrL3cMrz1paDLSQdnT4UVbnLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اهواز امروز
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/funhiphop/75342" target="_blank">📅 13:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75341">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90d827a7ab.mp4?token=MZRLdgrvmHmpGgPIQg1rusB88IdyB3OoVQecbe8105BGj42IdXgemrIwwL5zBNoix8a6waGGEdmDdFPoyDHVgJBU-PV7UyATPHHivuJwf-sRDnJBcOXSiB6m1_dJwiqygJsRUv_UHAfgdWIiTVKfPdWlo-JWArBwFomstG9Ik7flVaeZ-PAOz26GjXN-2mhO_qrp6ProGolDtQM1M7XT3qgjGnBM39wft2ywrqXnsXinlkCSCCx8V8TIiiq84TEoUQKU-850XxK4Quosj_BVQ-Ux9iehY6uM-q6OcDU_ZFpjnfjC004mNa8e0u1SKSF_EFvieWHqFKBQmV88A7taXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90d827a7ab.mp4?token=MZRLdgrvmHmpGgPIQg1rusB88IdyB3OoVQecbe8105BGj42IdXgemrIwwL5zBNoix8a6waGGEdmDdFPoyDHVgJBU-PV7UyATPHHivuJwf-sRDnJBcOXSiB6m1_dJwiqygJsRUv_UHAfgdWIiTVKfPdWlo-JWArBwFomstG9Ik7flVaeZ-PAOz26GjXN-2mhO_qrp6ProGolDtQM1M7XT3qgjGnBM39wft2ywrqXnsXinlkCSCCx8V8TIiiq84TEoUQKU-850XxK4Quosj_BVQ-Ux9iehY6uM-q6OcDU_ZFpjnfjC004mNa8e0u1SKSF_EFvieWHqFKBQmV88A7taXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بصورت خیلی عجیبی امروز به لبنان اتک نزدن  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/funhiphop/75341" target="_blank">📅 13:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75340">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بصورت خیلی عجیبی امروز به لبنان اتک نزدن
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/funhiphop/75340" target="_blank">📅 13:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75339">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">He said she was Persian   میشه  پسره گفت ایرانیه یادگرفتم ممنون
❤️</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/funhiphop/75339" target="_blank">📅 13:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75338">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">Diddy:
He said she was Persian and started speakin' Farsi
پسره گفت ایرانیه و شروع کرد به فارسی حرف زدن
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/funhiphop/75338" target="_blank">📅 13:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75337">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مدیرعامل جهاددانشگاهی
:
به دانشجوهایی که ازدواج کنند ۳۰ میلیون وام تعلق می‌گیرد
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/funhiphop/75337" target="_blank">📅 13:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75336">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تسنیم:
رسانه‌های اسرائیلی اعلام کردند یک هواپیمای مقامات دولتی اسرائیل لحظاتی پیش به سمت امارات پرواز کرده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/funhiphop/75336" target="_blank">📅 12:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75335">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6TawOfPEbWKHpqe--oLyeZQXAvc4HhjiA8KaABkeSIrVLvaoZrDGMN_dc3KuJ12-RUiUl-uFyTRZdy5rwinQRnz3EO0Y_4LyLW51GwwNTCvAC7u6543wp-z91LtftRFE4NsJuooa35up-ZL3gV3InpSauaoyC_Jt06AaPCaFgzDTNjC5LRxoM5ZXzt1FxRX8l3381gcBiCWV4llie6aGOb5Ey3FPOgaO_402xd_bqIXdtDazaRKrsckKF3xof0q7SDCG1xSuvn74LPWoRPqhaoPG2AZ4IjOgGh5vY1ixLczc3kBjyLSpJ9uf4V6CvtD-RtjhowuaPO5VkzLXWjByg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادر فکر میکند شخصیت اصلی داستان است
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/funhiphop/75335" target="_blank">📅 11:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75334">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یعنی ترامپ ریسک حمله قبل جام جهانی رو میکنه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/funhiphop/75334" target="_blank">📅 11:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75330">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rVPBw4sQwdZAhY6992IffUy2PK5Z_XQYdILhhsh50wKHqlohPajd3ZgGR8hznQ5XQO7sVpItHjB_AxoV0XUClSr6iug5B3VhkL8PKM7cEx4hlrezkbBQVBeCpKhHhVoEtGPJDJi702QeBkGFITzZrSpuutU1fhNBYAfymjDxtryMU6ZqWfGsg4WFyM_R4ob3KHdzYVEIDYPojbXz6LqDrdTNPRI-exH0mUZTwHYZ7ZDqqPcDBOBaQhuma5lo82NpOG1QxOavQ-iZMx45ktQGcwQOnD7X-_l04D-MShl0-6V9IL1E1GY4rm61d6rkaDVpRtBzSnMoxy_OqPxvLfEkrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mxKY79YHVN35FpbQ9YmIM_loxQM6MWqHO2K-vUp3p9ibclGD3tRJ3pQQJuFacsemPwFU7YC4LrWGLG_D759krd67JB4pXJQwQZ3Vh12JqTPvtmqflBzRGeo2Z0pKxBcWr0Frw889IKySPAhRWgq5eKk7uSN5sa766oE090lkHNDKHZ6WPGnHIJRdDe7vZCDq8Bcg-bLdGOakxEafaFuYcMiq4_KO7J0YKTB0Op37W5EwZbFW19S1lgaJDfalRp3OM-CjaWhOK5o544itSJ9gCOfvYm7kBcOie5jWi-TAyZaf1h3RzCMR6wicAgeswDzfYGtN_6NRV_1CvmjNQetdYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Erl6-EZHI96DgjIhyWRIKFybBkv5AOZoKgc7M3M5EfyEfllG3610dDMhEaQCKyZ-3JoeHPy1vlndTpUHmCBK15ZlSnyzBSXqDZrJ1OdxWqb10FcgSs5iDZPsYRJRM_WYeoPb3UmuXEM5KySo9r-JQiRWXPvimpaVffSNVhLbaif3hLXiQlQIrQxW2cFtyk2jLZKIimxYXh0t7p3yCOP8A-IKEgJkJ1e8PMWQSiGMZUx-pqNTiBzoHgQORuC7lNirTyUh6AjboPvIenkU9dZo2KZLmc42fP_RFeZGZX5cj29dSsvCqcLPf8NvfkojcM-lGWIZ1DnBMgc43WqAcReiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2QYAfytN7ulqjTRUNbSbzNAR9HjzglILABZPEYyFY6l543_K7DHvsUrLtwGoPaWC1geZeuStttcwAYvDGJ7i1aDOLeipfNPwDDU0tWFqY9Lvi-3VzePyNpDTxdxP0AvWNURpGC5qbkO4nKgOz84CuQHYd5XkG4jrieYeV5mDDO5Jz6hWimCQfvcPoNqkWZmybBV0hHyy3dhJyDUz_8hCFPz3EYoPZ72Zp1MnIBEbTye3NebekBv01gIRCqRfVYqXK9SpWnnEOsmdrwgfNCt97l_0dRcVWIsaG1NCv0sRj9arsSEGATseHykYqcYGWQHgGDWcvb_zzZfb4NRV6Rtjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راک‌استار رسما اعلام کرد جی‌تی‌ای ۶، ۲۸ آبان امسال منتشر میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/funhiphop/75330" target="_blank">📅 11:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75329">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فرمین لوپز جام جهانی رو از دست داد بخاطر مصدومیت</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/funhiphop/75329" target="_blank">📅 11:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75328">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بورس ایران بلاخره باز شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/funhiphop/75328" target="_blank">📅 10:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75327">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIF4O-gBi48yS3gC47XXpSlxdPTWK0JLt_jSdAp_lM_qm8XZAMOeWe925tKvXUZ5nmTp1adiDHhN37sPfhLX-TfVDIlZrMvx8ohisw7KjmLYdfeNzGNFwNVvwzaHsLbeRhNqQtS3p6kBc4EfNY0j9rkW-TOpyCa_LZOT1Nxpz0UFLseFxch_j1__cWFAlRCbT3c-VXA7Xqx4dQBAOwplDiVNYha5zVSOPogB1ySyymN1lqHIyGoXvRO5PAw_IqiBKO3-yubVQvHu5LKREJrDg-n-rzIwJDzjEoouYuL8cgqVEodPzWTZt8mJmDnlIgc6uRZhQe3EmU3rnm-jy8r0Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس ایران بلاخره باز شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/funhiphop/75327" target="_blank">📅 10:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75326">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔮
اینترنت آزاد با «ملوان زبل»
📦
تخفیف 24 ساعته
📦
50,000 تومان تخفیف روی اولین خرید مثلا 1 گیگ میشه 140,000 تومان
😐
🔥
پلن ویژه:
✨
1G = 190,000 تومان
✨
2G = 380,000 تومان
✨
3G = 540,000 تومان
✨
5G = 850,000 تومان
✨
10G = 1,600,000 تومان
☄️
تمام سرویس ها با ساب تقدیمتون…</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/funhiphop/75326" target="_blank">📅 10:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75324">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdMRSNoikq-ZAR-enq3FZJz6aZndC58oOqnRfWYcp1zLISYxS6cM1AYaXgIcd6pxFZBazKe6P8YfbegwhL8mI3hF_3AbPQK0ULlSBkPWE64O92ukr1GIYSiEpCWTQ5zUQ_gjeS1xGK-fucz0piABzZaNeNLK993RJX8QCuYp5PV9ATEh5cTTxaojzKk7tpgUIS4rw3TT1oF3OOLbJIgWygFVWCsuAAKr7UQTPYU__-yG7KbOqtF-6oRpzGiWAA-FzNSglzcSq-Q2lbJwegNU8Otg8bRE-wgvS36AkXHXm1tK4vser9ZvIGeJ56C6AuIfuywtbP-lis5YRmN9p_y5hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔮
اینترنت آزاد با «ملوان زبل»
📦
تخفیف 24 ساعته
📦
50,000 تومان تخفیف روی اولین خرید مثلا 1 گیگ میشه 140,000 تومان
😐
🔥
پلن ویژه:
✨
1G = 190,000 تومان
✨
2G = 380,000 تومان
✨
3G = 540,000 تومان
✨
5G = 850,000 تومان
✨
10G = 1,600,000 تومان
☄️
تمام سرویس ها با ساب تقدیمتون میشه
☄️
⭐️
‌تا 100G هم موجوده
⭐️
کاربر و زمان نامحدود است
🌕
✅
تحویل سریع
✅
پشتیبانی
✅
مناسب آیفون و اندروید
✍️
برای خرید پیام بده
🚀
«ملوان زبل»؛
@MalavanZ_SUPPORT
چنل
🦠
@MalavanVpn</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/funhiphop/75324" target="_blank">📅 09:54 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75323">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی مجلس:
ما در حال کار بر روی چارچوب قانونی هستیم که توسط مجلس شورای اسلامی برای مدیریت تنگه هرمز تصویب خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/funhiphop/75323" target="_blank">📅 08:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75322">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88a0f52793.mp4?token=kdsEbxMzDVCkppYg4G2BEj5htMfZdFH4xBd_S7wobwDN4WUor73MgV048iRTSWhITMTdHoC1KvuCo3fZPQty-no3GPUGMTEcYXNS4ew3GnC41yvbN7prI6t3DeZDY3Q89HS_SG-waIK_3i00t3pcHKcX30Dzmq_dD5gItbC-A4Q5b7joFnZRlyBKwHbp8l5fAWpsuHjw7jIm1l-HRi0DApIXVGQCt1XyB7rygwELsXHe6GiR8BTm2BOK8ctCm5K-e_51jIZliOqTKT7_sEmug3J5pSWMI9K8LMp-4rSSukGJ9vq9cbMLmtWTxHEI6RUL5smqzI_Mt5U2mdP2TQIcJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88a0f52793.mp4?token=kdsEbxMzDVCkppYg4G2BEj5htMfZdFH4xBd_S7wobwDN4WUor73MgV048iRTSWhITMTdHoC1KvuCo3fZPQty-no3GPUGMTEcYXNS4ew3GnC41yvbN7prI6t3DeZDY3Q89HS_SG-waIK_3i00t3pcHKcX30Dzmq_dD5gItbC-A4Q5b7joFnZRlyBKwHbp8l5fAWpsuHjw7jIm1l-HRi0DApIXVGQCt1XyB7rygwELsXHe6GiR8BTm2BOK8ctCm5K-e_51jIZliOqTKT7_sEmug3J5pSWMI9K8LMp-4rSSukGJ9vq9cbMLmtWTxHEI6RUL5smqzI_Mt5U2mdP2TQIcJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و محمد بن زاید آل نهیان، رئیس جمهور امارات متحده عربی از من خواسته اند تا حمله نظامی برنامه ریزی شده خود به جمهوری اسلامی ایران را که برای فردا برنامه ریزی شده بود، متوقف کنم.…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/funhiphop/75322" target="_blank">📅 03:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75321">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ:
ما حمله‌مان به ایران را ۲ تا ۳ روز به تعویق انداختیم چون عربستان سعودی، قطر و امارات فکر می‌کنند که به توافق بسیار نزدیکی رسیده‌اند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/funhiphop/75321" target="_blank">📅 01:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75317">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GS4MxhwzIJ6gDMfxPLjcF_0N0d9zMIlcsSxGZqlK55j3Y0s5QSwtndZwb6PNWTYWjTa07nWfPKztwc0C9GCB3YCn1f-ON-aQiWjd1yGht0ajoFiw2F4Bd4QAoXOSVyRgNeh22uSr-yX8_jlyZ1qvLQiL-sIenwIGw6TxmPWKn41feNymt6-6B-Tqms-opTpAkXc754MlDtcKEbz40yII52S22q4NM-5L2X74MpG6vsFZKA-_P3WjF4YRXoWCxjnn0xsyRsU_tKJp1YN2Ozr1XKBi4RIWIjHte_CbxbWw_Bag3Z8JSak7nO-6p-sIzAWrZ36QZdJ3BmH0GQvEKeUFRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/funhiphop/75317" target="_blank">📅 00:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75316">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کارلو آنچلوتی تو یه حرکت انتحاری ژائو پدرو رو از لیست برزیل برا جام جهانی خط زد.  پ‌ن: نیمار دعوت شده  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/funhiphop/75316" target="_blank">📅 00:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75315">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnxpQkzg5bh_g86YoySF-gL2mbvuZCcBfarlDZRrdHHxpWDcz8Ewp3mS8k5-zUDDqgCpsHGjGIVGQyLKY93lhRWupiWgMqIRAc9dLtueBdxm44c4_RsRsa8PIiNDC5WlsKwCjdOYljkX_hI0Pjevr3RuA-oUsUtz9E-p2KDT7bpA02-6mR1cR2sA6bF1fotZ3xXHPhJeCGtKVSGDWKDnyY6HGufW4QA-dmrHkpDOvqKA7kLGPgeZqs79I3vH_Cw8Qx9VqiDw-uEKdsyeFWQQ29Xl8ffhtlVwigBNv3hNu9xOMnDIRjDZDqBrmjxLe0pf4310J84mpoFRzvHbYKzmtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارلو آنچلوتی تو یه حرکت انتحاری ژائو پدرو رو از لیست برزیل برا جام جهانی خط زد.
پ‌ن: نیمار دعوت شده
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/funhiphop/75315" target="_blank">📅 00:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75314">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کل تلگرام دارن با کانفیگا رایگان سونیک وصل میشن شماهم وصل شید:
@SonicVPNRBot</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/funhiphop/75314" target="_blank">📅 00:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75313">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پدافند هوایی اصفهان درحال فعالیت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/funhiphop/75313" target="_blank">📅 00:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75312">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBGIwVxQojR2xmHQQndKF7p1P03pteC3U-Kwc0Q-menOg3fHMCoJpVm2Wlo47zBfb1ziohT4qiDXJG7XczTeZIAHCTtKIh2SIJeyra5CzYXZTef8s-k_G-1LjIGjqifrNITKzDf0JHRUeE40z-2o2FiegBuvIWXjo3PTI6ALJ3VBz4fJZNzYtTNjpV4woU1UMWJ1xXkV3yXU_lhLrPhw_HqWry0iVRev2OpW4vV_O5yHQpFmlYEDl_EBaVj_hD0QSLUmJMcCzKWPBjD4boeeLRvXKOGEhrRXhmADzvaQHlwcbi7bTxnwm2eDUgDjpOdT8HdQfAiqWvfXkRXsVg_i7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😮
فیلد مارشال رضایی
برای حمله نظامی ضرب‌الاجل تعیین می‌کند و سپس خودش آن را لغو می‌کند!
با این امید واهی که ملت و مسئولان ایرانی را تسلیم کند!
مشت آهنین نیروهای مسلح قدرتمند و ملت بزرگ ایران آنها را مجبور به
عقب‌نشینی و تسلیم
خواهد کرد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/funhiphop/75312" target="_blank">📅 23:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75311">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فوری: پپ گواردیولا در آخر فصل منچسترسیتی رو ترک میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/funhiphop/75311" target="_blank">📅 23:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75310">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">با رفتن پپ از لیگ انگلیس، دوران پادشاهی آرسنال با رهبری آرتتا رسما شروع میشه و تا سالها هیچکس نمیتونه جلوی این تیم رو بگیره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/funhiphop/75310" target="_blank">📅 23:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75309">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فوری:
پپ گواردیولا در آخر فصل منچسترسیتی رو ترک میکنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/funhiphop/75309" target="_blank">📅 23:17 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75308">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">باز حداقل الان ۱۰۰٪ سهام کمپانی های خودرو سازی داخلی دست خودمونه
نه که ۲۰ درصد بنز دست ما باشه نصفیش دست اجنبی‌ها
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/funhiphop/75308" target="_blank">📅 23:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75307">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZyKskRAtu8gZRAVy8QkIUxhu1LLjQsvEOme97L__x0OO4UGJcpPyh0MpXZXb7RfZLcVAfz6XFuxa6xmPxHEMRf7S8xkGGFxhhSL5z-6byhGYfTUS-xlYHtWAA-Gf84K1wonenRZQrY7T1KfvH0An7GXUWHeJpA6u6dT6YQCfAZu_ligw3PpmQXr8NRb6yEjYkU7LjtLZ7Iw3kX7L84cXCucrbXwQQjOPiCG0QUwE-qqheHqTgKH0gc_mYchH20UU-lZ99m0YirmNT4kNIc7K7mLpxCnhFEsuPkSdlvU9jSPIp_4JeV7w0_dNPQkXyOg4FjZChVg3DAjMYpeiGlo_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و محمد بن زاید آل نهیان، رئیس جمهور امارات متحده عربی از من خواسته اند تا حمله نظامی برنامه ریزی شده خود به جمهوری اسلامی ایران را که برای فردا برنامه ریزی شده بود، متوقف کنم.…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/funhiphop/75307" target="_blank">📅 23:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75306">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUZxRsLae9hIW2cItF-8WNr65PQa614O8MmKNSRkQqcab-cV6-y13eBOeZ4rvB_SvvOeEsVoYHnP0nnBuToE0IFTjjABpsATV4brIzRKI_p2N-sf3Jo7OYxz7ewB7qgxuWPjH-DYvLXixggPwrAcfHq2nSNyuu3Ox-EqA0r6ULE3YE8tzvxTJo6T265DhmskOSMThsYeranx_x0g_mKnd5aeTwB8dMW1TZwlPdmsKqcyqtHngclyaybg1RB94afhXh01X4L1-8dXqEEpv6z6Pg44qmeRr23xsQCQsX8M67mqxaW1xxPDb1L7pI0QRvIFySwpiHjBGRisYqH1pGu08w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و محمد بن زاید آل نهیان، رئیس جمهور امارات متحده عربی از من خواسته اند تا حمله نظامی برنامه ریزی شده خود به جمهوری اسلامی ایران را که برای فردا برنامه ریزی شده بود، متوقف کنم. به امید توافقی که خواهد شد که برای ایالات متحده آمریکا و همچنین تمامی کشورهای خاورمیانه و فراتر از آن بسیار قابل قبول خواهد بود.
مهمتر از همه، این توافق شامل عدم وجود سلاح هسته ای برای ایران خواهد بود! با توجه به احترامی که به رهبران فوق الذکر دارم، به وزیر جنگ، پیت هگزث، رئیس ستاد مشترک ارتش، ژنرال دنیل کین و ارتش ایالات متحده دستور داده ام که فردا حمله برنامه ریزی شده به ایران را انجام نخواهیم داد، بلکه به آنها دستور داده ام که  در صورت به توافق نرسیدن آماده باشند تا با یک حمله قابل قبول و در مقیاس بزرگ و کامل علیه ایران آماده باشند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/funhiphop/75306" target="_blank">📅 22:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75305">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خبرگزاری مهر:
فعالیت پدافند قشم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/funhiphop/75305" target="_blank">📅 22:28 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75304">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بچه ها اگه کانفیگ میخوایید تهیه کنید میتونید از ایشون تهیه کنید، ۲۰ روزی هست باهاشون کار میکنیم کارشون درسته
قیمت: گیگی ۱۹۹
@TornadoAdmin
| خرید
@Tornado_Ping
| فروشگاه</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/funhiphop/75304" target="_blank">📅 22:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75303">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">الان یادم اومد ک تتلو راجب ممه های گلشیفته آهنگ خونده بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/funhiphop/75303" target="_blank">📅 22:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75302">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZChh6MAUkC7aeRs3lR4eN5mbxPoXmrjsYkFfSGtd2_Vem_xRCzV0JVk8SYsupqHTya2jc_Q2USkbctnrIinhRqjqX1eXpue19Z54rs1mtE99S6AN6ZnfrA6FMLPEyE0c8Uflx0ZBFQjLWxtZQ_tUhPBe3O-euuSXUvugTIf0cHZEf6iUTVZKDPdugdw7htS5pdsV2_f7wnJkjH6UhUtAytQDtGjxd-WqTPFWIn9-2kRFYDNpy2d5-tHeL_YB638nO-oR2wc8IhaTghaKq7uEEHt1-gnx9PM7TvxyF8WdazcujXvAZn6rmTC3QjqpeOgVSyTtXT3GGVguQeNKjlSeKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/funhiphop/75302" target="_blank">📅 21:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75301">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✈️
واشنگتن پست
اسرائیل برای آغاز دوباره عملیات علیه ایران آمادگی کامل دارد و اکنون منتظر تایید و چراغ سبز نهایی از سوی آمریکا است.
😶
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/funhiphop/75301" target="_blank">📅 20:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75299">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ: از آنها کاملا ناامید نشده‌ام و می‌توانم به شما بگویم که آنها بیش از هر زمان دیگری می‌خواهند معامله‌ای انجام دهند، چون می‌دانند که به زودی چه اتفاقی خواهد افتاد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/funhiphop/75299" target="_blank">📅 20:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75298">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وقتی نیویورک پست درباره اظهارات قبلی ترامپ که می‌گفت ممکن است یک توقف ۲۰ ساله در غنی‌سازی اورانیوم ایران را بپذیرد، از ترامپ سوال کرد، ترامپ گفت:  الان به هیچ چیزی تمایل ندارم. در حالی که از ارائه جزئیات بیشتر خودداری کرد. ترامپ در ادامه: واقعاً نمی‌توانم…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/funhiphop/75298" target="_blank">📅 20:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75297">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ به نیویورک پست:  من پیشنهاد ایران را قبول نمی‌کنم. ایران باید بداند که در این مذاکرات من حاضر به دادن امتیاز به ایران نیستم. ایران خواهد دانست که «به زودی چه اتفاقی خواهد افتاد» پس از دیدار من با تیم امنیت ملی.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/funhiphop/75297" target="_blank">📅 20:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75296">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ به نیویورک پست:
من پیشنهاد ایران را قبول نمی‌کنم.
ایران باید بداند که در این مذاکرات من حاضر به دادن امتیاز به ایران نیستم.
ایران خواهد دانست که «به زودی چه اتفاقی خواهد افتاد» پس از دیدار من با تیم امنیت ملی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/funhiphop/75296" target="_blank">📅 20:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75295">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الان وقتشه مکرون از گلشیفته به شیما کاتوزیان مووآن کنه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/funhiphop/75295" target="_blank">📅 20:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75294">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ به العربیه:  ما کار بزرگی انجام میدیم و نصرمن‌الله و فتح الغریب
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/funhiphop/75294" target="_blank">📅 20:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75293">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdHSINLq42Ik7nfoC_nq_pT9oJ-e_4FMsbZvwyzcmdwjIVbWLUwDGAkMP_vHLdWu9BBMmppv4SYjC3DHXBrpciyv4Hl-UYvT4Za5hE790HbxZHzlQGR3cJ0IpWZ6-huBDTs1jn-bvJEfygU1UmopA5Iu4Ss8WQOUUOiKM_Bqdxikc6Is0mi2GeDOxQ6PFWhIeiFBKdurjM7oMTKNh4wI-2xkVqXiYHZ0zTKhVL6lJUnp2D-QC_GuTTDSzgRIJdPDETqOt1REmOxTYDJRUxkth-TyzQ7dwvfy5itXgMRfRLaYJaGmYWkaKu90gmQbR3SZZCCRGxRkBahf5MQ0lcKBVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعا ارزش خرید داره، هر بازی بیشتر از پنج گل میبینی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/funhiphop/75293" target="_blank">📅 19:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75292">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">——• 4KNET •——
🔥
تخفیف ویژه سرویس V2ray
🔥
10GB 2500 —> 1900  •پایداری تا بیشترین حدممکن
⚡️
•متصل برای تمامی اپراتور ها
💯
•مدت زمان 30روزه
⏳
•بدون محدودیت کاربر
♾️
•لینک ساب برای مدیریت حجم
🧮
–کمترین مقدار حجم 1GB  برای دیدن لیست قیمت ها و خرید به چنل مراجعه کنید:…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/funhiphop/75292" target="_blank">📅 19:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75291">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1G98u6IniXNBV4AcxDy9Da2jLUJoSu7D_odGU43vCQhIPux9Ba2i5Y3y8h79nqsgQ2IBbaYOUJCcnWi_rF_HlQz6wVDTj06YYC3lP5Zx7x-tmN1hCo3AoTCq7JXKbMuAtMfq3aQY6gd1ExXdAfXasfMdcOrhoXol2CzpnQMo4eruzFij-n1a7VrzJ9YA4bOIiE6lOYYzhEA-ffy1OMzmfhZUAd83aas46c6poezH07UbTWr35XpRRoiKmzCom1QjEadZmPZo4iE7GWhJtskq2VH_b6KHKC4ZZjGRBnWxDWbw0OU-_OuTGkLvpMQyEPXEvGBMirfY7puVr0dOUolNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">——•
4KNET
•——
🔥
تخفیف ویژه سرویس V2ray
🔥
10GB
2500
—>
1900
•پایداری
تا بیشترین حدممکن
⚡️
•
متصل برای
تمامی
اپراتور ها
💯
•
مدت زمان
30روزه
⏳
•بدون محدودیت
کاربر
♾️
•
لینک
ساب
برای مدیریت حجم
🧮
–کمترین مقدار حجم 1GB
برای دیدن لیست قیمت ها و خرید به چنل مراجعه کنید:
——•
4KNET
•——
پشتیبانی :
@SUP4KNET</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/funhiphop/75291" target="_blank">📅 19:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75290">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آکسیوس: یک مقام ارشد آمریکایی گفت پیشنهاد اخیر ایران برای توافق ناکافی است و هشدار داد در صورت عدم پیشرفت در مذاکرات، احتمال از سرگیری اقدامات نظامی وجود دارد. انتظار می‌رود ترامپ روز سه‌شنبه با مقامات ارشد امنیت ملی دیدار کند تا گزینه‌های نظامی ممکن را بررسی…</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/funhiphop/75290" target="_blank">📅 18:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75289">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✈️
آکسیوس
👾
کاخ سفید پیشنهاد به‌روزشده ایران را بسیار کمتر از آنچه برای توافق لازم است می‌داند.
🔜
یک مقام ارشد آمریکایی آن را تنها شامل بهبودهای نمادین توصیف کرد، با زبان قوی‌تر درباره تعهد ایران به دنبال نکردن سلاح‌های هسته‌ای اما بدون تعهدات دقیق درباره…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/funhiphop/75289" target="_blank">📅 18:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75288">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✈️
آ
کسیوس
👾
کاخ سفید پیشنهاد به‌روزشده ایران را بسیار کمتر از آنچه برای توافق لازم است می‌داند.
🔜
یک مقام ارشد آمریکایی آن را تنها شامل بهبودهای نمادین توصیف کرد، با زبان قوی‌تر درباره تعهد ایران به دنبال نکردن سلاح‌های هسته‌ای اما بدون تعهدات دقیق درباره تعلیق غنی‌سازی اورانیوم یا انتقال ذخیره موجود اورانیوم بسیار غنی‌شده خود.
🔜
این مقام هشدار داد که اگر ایران از موضع خود کوتاه نیاید، آمریکا مجبور خواهد بود مذاکرات را «
از طریق بمب‌ها
» ادامه دهد و افزود: «
ما امروز در موقعیت بسیار جدی هستیم. فشار بر آنهاست که به شیوه درست پاسخگو باشند.
»
🔜
هیچ تسهیلات تحریمی بدون اقدام متقابل از سوی ایران اعطا نخواهد شد، این مقام افزود و گزارش‌های رسانه‌های دولتی ایران مبنی بر موافقت آمریکا با لغو تحریم‌های نفتی را رد کرد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/funhiphop/75288" target="_blank">📅 18:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75287">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بمب پشت بمب: آمریکایی‌ها باید دریابند که ایران به هیچ وجه با اینکه پایان جنگ در گرو تعهدات هسته‌ای باشد، موافقت نخواهد کرد. ایران درباره ضرورت پرداخت غرامت توسط آمریکاییها به دلیل تجاوز نظامی به ایران، بسیار جدی است.  اما آمریکایی‌ها با وجود سخن از چیزی به…</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/funhiphop/75287" target="_blank">📅 18:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75286">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ
اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌شان از بین رفته و در ته دریا است، و نیروی هوایی‌شان دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم» در حالی که پرچم سفید نماینده را به شدت تکان می‌دهند، و اگر تمام رهبران باقی‌مانده‌شان همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی عظیم و باشکوه ایالات متحده آمریکا بپذیرند، روزنامه‌های در حال سقوط نیویورک تایمز، وال استریت ژورنال چین (WSJ!)، سی‌ان‌ان فاسد و اکنون بی‌اهمیت، و همه اعضای دیگر رسانه‌های خبری جعلی، تیتر خواهند زد که ایران پیروزی استادانه و درخشانی بر ایالات متحده آمریکا داشته است، حتی نزدیک هم نبود.
دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند.
آنها کاملاً دیوانه شده‌اند!!!
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/funhiphop/75286" target="_blank">📅 18:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75282">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کان نیوز:
نتانیاهو امروز جلسه امنیتی محدودی با مقامات ارشد دفاعی و چند وزیر درباره ایران برگزار خواهد کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/funhiphop/75282" target="_blank">📅 18:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75280">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بمب جدید تسنیم: اختلافات اصلی ایران و آمریکا همچنان حل نشده باقی مانده است؛ منابع می‌گویند آمریکا هنوز خواسته‌های غیرواقعی دارد. یک منبع نزدیک به مذاکرات به تسنیم گفت ایران در پایان دادن به درگیری، بازگرداندن کامل دارایی‌های مسدود شده ایرانی و درخواست غرامت…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/funhiphop/75280" target="_blank">📅 18:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75279">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">العربیه: ایران در این پیشنهاد جدید خود خواستار آتش‌بس چندمرحله‌ای و بلندمدت است و همزمان بر بازگشایی تدریجی و ایمن تنگه هرمز تأکید دارد.  در این طرح همچنین از پذیرش توقف بلندمدت برنامه هسته‌ای به‌جای برچیدن کامل آن، انتقال مشروط اورانیوم غنی‌شده به روسیه به‌جای…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/funhiphop/75279" target="_blank">📅 17:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75277">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">العربیه: ایران در این پیشنهاد جدید خود خواستار آتش‌بس چندمرحله‌ای و بلندمدت است و همزمان بر بازگشایی تدریجی و ایمن تنگه هرمز تأکید دارد.  در این طرح همچنین از پذیرش توقف بلندمدت برنامه هسته‌ای به‌جای برچیدن کامل آن، انتقال مشروط اورانیوم غنی‌شده به روسیه به‌جای…</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/funhiphop/75277" target="_blank">📅 17:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75276">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یک مقام ارشد ایرانی به رویترز:  آمریکا در مذاکرات نشان داده است که در برخی موارد انعطاف‌پذیری دارد، از جمله در محدودیت‌های مربوط به برنامه هسته‌ای ایران. با این حال، آمریکا تنها موافقت کرده است که ۲۵٪ از دارایی‌های مسدود شده ایران را در یک بازه زمانی مشخص…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/funhiphop/75276" target="_blank">📅 17:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75275">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDon Quixotet</strong></div>
<div class="tg-text">رویترز فیکه بخدا</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/funhiphop/75275" target="_blank">📅 17:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75274">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یک منبع آمریکایی به الجزیره:  صبر رئیس‌جمهور ترامپ به دلیل عدم پیشرفت در رابطه با ایران در حال تمام شدن است. رئیس‌جمهور ترامپ تمایل دارد اقدام نظامی انجام دهد مگر اینکه ظرف چند روز چیزی از ایران دریافت کند.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/funhiphop/75274" target="_blank">📅 17:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75273">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یک منبع آمریکایی به الجزیره:
صبر رئیس‌جمهور ترامپ به دلیل عدم پیشرفت در رابطه با ایران در حال تمام شدن است.
رئیس‌جمهور ترامپ تمایل دارد اقدام نظامی انجام دهد مگر اینکه ظرف چند روز چیزی از ایران دریافت کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/funhiphop/75273" target="_blank">📅 17:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75272">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAKkHq843aQMXdK3h0kDBLVV2E8Ua8znym0v5_ilJRoAgsif8E3Qxy2BE0Lo2fpD9it0y_SgmV75qwBsPrJjisj46IrV4PsrE18GAY2tZaK3hzedFvkIw5sin7gErSGDFm0w6gadwA3Nw_m_cc4qAniUSokZ2rGbGIs6cSREApF-CLNd-rpprZEZ1n9lXNJEC0u9ZfW_6EB9hY_y-oulvoa6Gi9ClyKEDqYTfzgmNvGM0Dnv2LcOKRTN7Ev3c-kBOdQoOWHqWoziAjRUEcKHfC9TO6snUA51eXfpGrCPZ6BquGF3rS5hxCYoECjr7zFOeT2tkCOAYufdi099EV0mzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/funhiphop/75272" target="_blank">📅 16:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75271">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lw--TwXPesRp4lvJiB2k0MwiP7tfP7L986isaR0GQSF4-Y2dE3h0uVTRBzD2UAUZnnRs0obnKP6UqTyKD6cVC0_FmHIJ38sE8lm-BoxVbp5wd8x-0AGvCCTwC7hcQdWLtH7GgjsjHC8trhe6agewLUWg7ReFFY24KkSvYJRN2MaTBXPhfS0gFwrwT4JvEyn2YJyL-NPCkjOMX4pSyUJWDUFZ1btG2NlBMnOmBXubDPtxLysIMEhGMa-tiwD55K741OE5c0GVQfBeAJUlqnmgz3r6V49KScWejUim1cc-dc9CE_iALkaSD3gy58FJZ6CwSaewb6Y8mYvabW8eGK7osg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر بد واس رئالی ها فعلا قرار نیست جام ببرید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/funhiphop/75271" target="_blank">📅 16:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75270">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الحمدالله اقا سالم هست
توضیحات مدیر روابط عمومی وزارت بهداشت راجب زخمی شدن مجتبی خامنه‌ای تو روز اول جنگ:
۱۰ صبح روز ۹ اسفندماه در وزارت بهداشت بودیم که تماس گرفتند و به ما گفتند که حوالی پاستور بمباران شده و جنگ رسما شروع شده است.
دکتر ظفرقندی، وزیر بهداشت همان لحظه تماس گرفتند و جویا شدند که آیا مجروحی یا مصدومی را آورده‌اند و بنده گفتم که تا این لحظه خیر.
آقای ظفرقندی با موتور راه افتادند و به سمت بیمارستان سینا رفتند.
حدود ساعت ۱۲ بود گفتند که آقای سیدمجتبی خامنه‌ای را به بیمارستان سینا می‌آورند.
خوشبختانه اتفاق خاصی برای رهبر انقلاب نیفتاده بود. فردی که در محل چنین حادثه‌ای باشد، طبیعتا چندین زخم بر روی بدن خود خواهد داشت.
این زخم‌ها نیز زخم‌هایی نبود که بخواهد چهره رهبر انقلاب را مخدوش کند یا اینکه همانند امام شهید ما جانبازی بگیرند یا قطع عضو داشته باشند. اصلا اینگونه نیست.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/funhiphop/75270" target="_blank">📅 16:06 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75269">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kI9s-aXNIdBcYq17H6C4qP7tcJaSOthOFC0b4uAEbybxCWZCRH3AIawsOG1yKdXAl9c72dAn6WbLoCE_HPSR8FZ27p99EbZomHvNq5xdquzPGE2m4L9RZtMw_A5J5vSBGZcBWiMKf-9TI8PWKLpCYuBAlxasD-8Gwj7ajk7o45WMOQslfvQiMyOMHvrSluUDuDw6149EyHeXjxf4uobvN83qQakpdyWHzOXLz2NUyPT90Rn-elCpKPmcSheB4yF2cUp3kGg2yhiDnHUsRVGG48gWadvE4OCPipGm7IwKXn8G_z5HL60VRcO2aG0H_uZt6Kph3M9kXgObeefiyt10Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات کی برگزار میشه؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/funhiphop/75269" target="_blank">📅 15:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75268">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNCQLlOdlUd-MdjB9sAXwdauW85LlTYmyn0xNiy1JhZXZYiORtMO5i-gDeIf-7DmmKaRZZfPJKzH1ubI6IqRiibKQ-Dj-w9tp6CJBELdAl-7-LrubxUYTFDv-dgErExnBqhc6t7eXq-v6dE8wkc7WkkLNl87H4W90lBHq1DquQN0V427NmDFLYbtkr_WcoT3kuSIPylynVnBfEwexTwIpAyyOQdjN4O5lg0Z0chyPiqwLi2D2HktG3o_06pgSmk_qRA0k4GnVwddVBZWWK35i9I1hHKWU4y07dauqI9az2jIdKP3v7hfTC12MDluEVn7BOxeOww7NzIvtf_gBf_yjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان عزیز در خدمتتون هستم با یک برنامه جذاب دیگه از سیاست با فرید   این چند وقت بدلیل اینکه خبر زیادی نبود برنامه نداشتیم خب همونطور ک میدونید آرایش نظامی آمریکا در خلیج فارس و دریای عمان کامل شده و هر لحظه امکان حمله هست  بنظرم این شرایط باعث میشه که جمهوری…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/funhiphop/75268" target="_blank">📅 15:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75266">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دوستان عزیز در خدمتتون هستم با یک برنامه جذاب دیگه از سیاست با فرید
این چند وقت بدلیل اینکه خبر زیادی نبود برنامه نداشتیم
خب همونطور ک میدونید آرایش نظامی آمریکا در خلیج فارس و دریای عمان کامل شده و هر لحظه امکان حمله هست
بنظرم این شرایط باعث میشه که جمهوری اسلامی قبل از شروع حمله دوباره یک پیشنهاد طولانی به آمریکا بده و باز از برخی از مواضع خودش کوتاه بیاد تا ترامپ رو متقاعد کنه که دستور حمله رو صادر نکنه
ولی این پیشنهاد هم مثل همیشه توسط ترامپ رد خواهد شد و دور بعدی حملات شروع میشه
هدف اصلی حملات حذف یک لایه دیگر از مقامات جمهوری اسلامی هست که به شدت مخالف توافق هستند
تنها چیزی که مشخص هست اینه که ترامپ خیلی زود تصمیم نهایی رو میگیره چون باید قبل از انتخابات کنگره کار رو تموم کنه وگرنه انتخابات رو میبازه و منافع زیادی رو از دست میده
تا برنامه های مفید و جذاب دیگر خدانگهدار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/funhiphop/75266" target="_blank">📅 14:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75265">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBUaMjqPSYl_QwlxFasAHepTsd4IKYEiqXizg4T50fozeNF1IT75SIihNnsmwBz-uxGqKm0bBt7I4KcbGL6_05LIOA0AY_aNyRKsSMoedWfX1ofz2erMcW4oqsXRGUuVtUyzHyOkNULE4tb1eoe_pmzX03jVFgLPUoSuLKluvOaH-ZMnI9r9NzOcvkKPtHNZWqDF2VjDZTWmjrNGlKBgaQcVvMKO6VlmNiMTOZCDqSlzlio5o8vCt0k3plw4DxvXLm1mzZzTIz0Kp6IIuaTGd__TJUnX948dyC5uzu9AFGyC5sITZhNTa7d7Uhf5xr8sjdXYO-KDnIEvAJDRXkMjcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی قلهکی فعال رسانه ای :
علت اصلی آموزش‌های نظامی این چند روزه در رسانه‌ها و تجمعاتِ میادین، توصیه‌ی یکی از «مقاماتِ مهم» برای آمادگی بابتت فازهایِ جدید جنگ بوده
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/funhiphop/75265" target="_blank">📅 13:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75260">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وضعیت شغلاتون چطوره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/funhiphop/75260" target="_blank">📅 13:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75259">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دوستان من شوخی میکنم با رضا پهلوی چون فامیلیم پ داره نزدیکم بهش
شماها بی جا میکنید</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/funhiphop/75259" target="_blank">📅 12:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75258">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مهدی قائدی پیج رضا پهلوی رو فالو کرد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/funhiphop/75258" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75256">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ON-8deW_UY2TlhHvm8wLuXGIfB9GK3UGuR-6ktq7xh7WSuog1V3lZLprAlST-HLy7dGsCPKrjrWd8PyXIeWTH08uuI8ccTk7Uew_jneZYeQxz-jD_sYDpTBPwOW85wUdtYK4lcXU6syOrPtcL6xcCNP8RaJVh7EfP_Mj72y_g4x61rf781NqBYn1Hku6egkBWjjU4WmZLOWpEAfdYvFwphHD2ePQp8yd-_MG11AQCsYBq6G66zpghtoSzfz8gsOBNMNqNiMA0r8W1KcIdS7QX8zLD8XdFBvjJ_Wu20e0mK7EUCrnv2K9GK0el0JmilsvCR9oRynvkiCsevkMFcRkQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش سردار  به خط خوردن از تیم ملی:
پاک کردن پروفایل با لباس تیم ملی ایران و آنفالوی پیج های تیم ملی
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/funhiphop/75256" target="_blank">📅 12:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75255">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انتخاب مورینیو هوشمندانه ترین تصمیم پرز در ۵ سال اخیر بود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/funhiphop/75255" target="_blank">📅 12:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75254">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فوری از فرید رومانو: مورینیو سرمربی رئال شد  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/funhiphop/75254" target="_blank">📅 12:28 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75252">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کوروش با آهنگ علی سورنا پست حمایتی از جاوید شاه گذاشته.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/funhiphop/75252" target="_blank">📅 11:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75251">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✈️
وزیر امور خارجه کوبا
دولت آمریکا بدون هیچ بهانه مشروعی، روز به روز پرونده‌ای ساختگی برای توجیه جنگ اقتصادی بی‌رحمانه خود علیه مردم کوبا و در نهایت تجاوز نظامی می‌سازد.
برخی رسانه‌ها در دستان آن‌ها بازی می‌کنند، تهمت می‌پراکنند و اتهاماتی را که خود دولت آمریکا مطرح کرده، منتشر می‌کنند.
کوبا نه تهدید می‌کند و نه خواهان جنگ است.
کوبا از صلح دفاع می‌کند و آماده و مهیا برای مقابله با تجاوز خارجی در چارچوب حق دفاع مشروع است که توسط منشور سازمان ملل به رسمیت شناخته شده است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/funhiphop/75251" target="_blank">📅 06:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75250">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROQI7Nlb9VNoQALiZwqoE6xrZYiWlKIDwBcbwJZCkfqL8ZXxdaT51imqSSQ_u8PMGNK04CP8NhI2Xe4u13il_-AQkOii2PtnrGQ2MeYxapy4gVETICev3RUb3ZfBLXWRV2wDixQ8J8W0Ska1rMR3I755eKlj4wiQ6PZgQWo0V98pCrAE8gURnk4kxAKoDXmX15A5y4Z0c9faSP3C1EQ4D8Lz_6M2IpRHkSdTs5_O9Y-Z7W7K2HYDb4xjyeVqxm_Mho4jzBDLpuRiev6OhZpudZ4ICy_Ix9DJfm-SbOEykdVbYgqgaXTDk_OcVXz0p24x02lujnOXYljklM529f0gwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
تا یادم نرفته اینو بگم؛ مارکت حدود یک ساعت پیش باز شد و تا الان بیش از 500 میلیون دلار پوزیشن لانگ لیکویید شد و قیمت کوین ها دارن به سمت پایین حرکت می‌کنن.
🤩
ترس توی بازارهای ریسکی داره بیشتر میشه و از اون طرف قیمت نفت هم روند صعودی گرفته.
🥵
مجموع این اتفاقات نشون میده بازار فعلاً داره احتمال تنش و خبرهای مرتبط با جنگ رو قیمت‌گذاری می‌کنه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/funhiphop/75250" target="_blank">📅 04:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75218">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YU-DKFVuAHcT7DrEb0CprTHP7hzz1LMuK2GfAc7IkYWauyyatZUSnmpGfMHbFYOW1Kyc0w3W-zs5Ae6oWpQsczPrdFCZXEn_XiXVzG7CElSMIMSB-4zQEJzMdrV7htJsAHQVxtxDwvDRIkIN8dHQHH2ge98lfzY0p024zmpaINfqZjGIftBOiY_B1giq82OtncWLbJWnTQB-1IDwc1yAKFpzemAZDvB_FouhV7GPEMKSmGM9cnvH9NRtxethsKpv_RB9LbenHncWHjWX3uBZMDJEq0wOr2TwhvBedfolCY6ntPye1Da-380tD44L-0a5ePLx8RauGpu7hK4xBYM8xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک راه اتصال رایگان که این روزا جوابگو بوده کلاینت (فاطمیون) هست و فقط برای اندروید هست
آموزش اتصال داخل اندروید
لیست ای پی های جدید</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/funhiphop/75218" target="_blank">📅 02:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75217">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FD5Dn8j6bbUcyGSI9SSV_uDtmbvrOMlnixDLhqFSg2NguyA1qLhg14NG5tmB23UhVujW3OulJPnIqy1Aepjpms--9biRTHXMyTemq-0susl0fg9UDS4h5mXabYgkJhJkKF6AgR4LkKSHpQCARWVnYS1XgreEcEtgmx7DW4SLHQOx58c9lQmasyykZSzTZao1xEcLW0lbYF4VdSAYUy2DePBvrXvDDVL5ngaJF8_HYXcyS19eqFGCywSttv_lo2ksPG79UMtIbrvuNVQPXpODyi8FnvFJRkAexqa8KaPQXQ-5BcY3W9RJxEKtfKPMABZPUsDdbsJ0kdWw24VjCAQ9tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری اشخاص دارن توی چنلای خارجی خبری ریکشن فیک میزنن, بعد ادمینای اون چنل هم برا دیسبک اسکرین شات همون مسیج و با اموجی هاش میزارن بهش میگن دمت گرم که ریکشن زدی.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/funhiphop/75217" target="_blank">📅 02:06 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75216">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یه سری اشخاص دارن توی چنلای خارجی خبری ریکشن فیک میزنن, بعد ادمینای اون چنل هم برا دیسبک اسکرین شات همون مسیج و با اموجی هاش میزارن بهش میگن دمت گرم که ریکشن زدی.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/funhiphop/75216" target="_blank">📅 01:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75215">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">لبنان MTV
مسئول جهاد فلسطین، وائل عبدالحلیم به همراه دختر ۱۷ ساله‌اش در دوریس در دره بقاع، شرق لبنان توسط ارتش دفاعی اسرائیل ترور شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/funhiphop/75215" target="_blank">📅 01:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75213">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ree5ebvfSsD0Sl2ATDopR25EoBRhXcpKPrj-pbIOwS1ioYw02k7nPr9RQskIpeMfdri8WMGnuK40ZSIo3maqkrj1zlgAhtYaSH8C7kup2A1D5zj8uKVMYB9IVeQGJYV8jzUyQLJyNelL4rp0RvMSVNw8RAoTgouZ17-wg-_yEepe1jlebZn2p9TaaRodg2Y2cfk7Rv-J6gpPqJyo7isyy4oIC0UbGTb5IDyvG117Z18epwn11y8h3XFS0wqUxecLxz0JwQLO62hi5fkCrwAERcM3tyqcOntEhqtZ97EclyuBH3XzWporrWCZchO47uGkXOLn4hi-OqWsffs91ggFbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه ترامپ این عکس و توییت کرد  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/funhiphop/75213" target="_blank">📅 01:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75212">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjJWHYSi45yZG8yoJKjAgAf_TvqghKTyuvH5bIKLHJPOiQAfTCW_2Tvaoxs9jYnqlv8BFhJIAyI94WmyVW5MZ_m60EfuOCatUReQar7W2C7OE_fP1Lkv8bdKg3-v0wQv9d7sq32QyM1T3e9bbtQ18WiCIB93rxda0v569nTewOBhtJl--cJ7ITjbSuiP_gpuOEQPcCKbVNhjg_YdOaq3s55xgUkTzRA0iKymsWHGN2HxFEWkp5ysHWzZMGoErrUQUZDbaWZ-7eX23xmX0O3Ugwfh9MoHhuTHAallnoLDpF-ibDYGSCCaz1PFbAaeBsOxeI8NRY54m2tYoHPD-EwxlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکرشو بکن تو 2026 پست های خیلی مفهومی املاکی و مشاهده میکنیم.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/funhiphop/75212" target="_blank">📅 00:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75211">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">جدی پستایی که راجب ترامپ پوشش میدیم بدجور ریکشن خورش کم شده
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/funhiphop/75211" target="_blank">📅 00:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75210">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کانال 13 اسرائیل
ترامپ در مصاحبه با کانال 13 اسرائیل گفت فکر میکنم ایرانی ها باید از آنچه الان درجریان است بترسند.
آنها باید مراقب باشند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/funhiphop/75210" target="_blank">📅 00:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75208">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6MXtOyW8vvXOK3DuHJ1wzQTVs6BOMaglJqcWYUXayCcer8H7JxNryYqEbj_9UPR2dYIAkpTcIxdXX2uP8WmKF1Lw4hkNXb46skw4C_saAkJDhm444PU1iP8ZAxYI7zAVB7zHScJYWjNbxgYENiON9kmrp1hXvTyRw1ihc7r0a-JPnH-QDMx-TJzEfZc5g4YyUZYetGMB-ZV_KHCd6VgOpUf4zfc0-hdjfTsbwlbZiQE8TITwW1QZVM0VpLVQIzJymvAmIwHZ384ExK2pvpUi_nw0CGsrjBQ7B1cWaFOwFz16mLzdZwZPUl8GprZVgVXfVSivJXI3k_a2ye5hGEPbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوبه خودتم می‌دونی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/funhiphop/75208" target="_blank">📅 00:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75204">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tcSBlHtPKPq6kE6GAQJq6qCZUw-kagLGvA2YrS3aW6AyIkLqTcd6E2wpvnEyy5Fe5qEeW3RnEEAs7q5tC8NA1Eyd-P8zXUNHBKFZ_aUC6xTbbSvg1E70_B-WMI97ImOubsrVQi84zwYipOW-iCLVMVaultsl1_9jouQV3JVGNH-dUjwWjRPbDI5TM42RiQuqi-wEHgmNjZK67xjs0yUwFgXn42sGXXdBEMfllTygboI_yHuwA0C-TkzHCJLjWDfFCYtuEgPRoHcFSIpqJaoMN4hHmuJ97a79W0lu34bnVlQWpJTbEHULYuY7BjDY8G_kHaUN94tdK0FgaU3vTCHn-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_gjT4AkLW69pv-Vzp1-sKONEutEWTgHghv4qGMsIqv7PvkC7-BZ-KDRU-HBmHF451-Cpe5bnthprWtd8cTG2l8S7HkhkkiPFUlPGy7AWqJnvL45fQstnlLXTyomMq2XblQS_IbazWHY0fvcxFVpuOUucDNVKNVTbME4x707IR7P35gUL_-w-XHIyiRrbWjSZtPMNm0K19-pDc0ngdVlZK21HNyqRTYcX8zlJZowztjTgR-hFjPVoDxsLfXBP3FH5ajeCw0-7y1ngrCZjMXAOreLNu-jpuHCFCFrXFx5zxddVsW9o0tqHSkEuH8i4QASOxdRnmLrZE-7_V9M2VVQhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHkn8kkToftjVquFDkJkTqVSa13_5Pf1ZjOJTUAjFzYFbLvt2ep6iZ4AWcmjjmQZSaMlQsuasTMzrmmA5RHEsWM01QCV4vtPzF-H8Q2Di5VAvWBzA7G7RMKmveb6rqKYyHrzWIfbiv-UD6OfwoY3cLaP4-cWzaVSksHkZto0cIy1oNhB9bmZvhNAgVCvYkG1BUNnxK4QD5j1Xb6rm9UH0hRjEDpqhJXwpyjJ67v-0YcanBNKBWWCO1w5Ii03OmCLh9VOOw7wHFAjbzzMtF8RLotehrckwKeDIPAd7wNrcFF8yZN9x10OFtj3tKm5X9mkuWif77kTWaPjFhJNySt6ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nAaRMXUcFiTnO8QNFup47ldwimHQtlxXXbrBu04t7VJ2LtOV42wk6O6_gSx4lF5MCBL69B2-zNUQKk2fbabsnbxZGHi4-LEyhHzHzUe0S_-eMngX5fix1d6gA9h9PLyXUXG3ccMhc0EQOxuC65lRpQgPkGSA4A_onZfSR-DF_akunHBz7CiTVEZe-B4-iWFxDv3eX8FkghzGSuaotk_ZVkfTgnz8U2Q0lLGuocK0WRFAaKav_VwNBmsqal9k56QwWXL7HKEaD7TnmZqqKbRDlgF9MivHqtay_B8_GeXG_Zlwgfp8e5sMAJIWxw-fMpp8TEKjRAIQNlMF358EiKbIiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکرشو بکن تو 2026
پست های خیلی مفهومی املاکی و مشاهده میکنیم.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/funhiphop/75204" target="_blank">📅 00:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75203">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-ygd4zacKuiR4jtBJSQn_l33GNIgnHcBsJPAU2MLk_OZQlWl3ronAQ6_-aVSMY-p75r2JI-cWYqcmRojt2DdXMkWZqpDPAylDK599-Ivz3PHSY_4oVqLzv-UgjAok_HHXyfSkpEWuZaWeue_9gagE5jejOtRD1J28rVrlKztvznHtb9AlP1zQUlzfo-0ToVfSlMq3ZBbuMocy9lowViVeRA0eMjHkAAV98vDDQGzOKZu1isaRjtG5z26FsrjfdcelkRskRp-vBdLBnekxmSjoMVe8OuwYZDcR4ghllChglQnL-fyGTBg8e1YzLmlpfMpyxdqV-Bj3eTKo7H1rBY6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/funhiphop/75203" target="_blank">📅 00:28 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75202">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👻
ویتالیک بوترین
ببین آقا یا خانم باهوش هیتلر حتی کسایی که معلولیت ذهنی و جسمی داشتنو هم اعدام میکرد و میگفت برای جامعه مضر هستن.
🤬
خوب حالا یه چیز جالب میخوام بهت بگم
بعد ساتوشی (سازنده بیتکوین) یک شخص هست بنام
ویتالیک بوترین که سازنده اتریوم هست و ویتالیک داستان ما اوتیسم داره.
🤩
عملا فنای هیتلر مخالف زنده موندن چنین اشخاصی هستن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/funhiphop/75202" target="_blank">📅 00:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75201">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5adfd6fc37.mp4?token=YUEiJtIW7XxFxSC3z6ckdJa8eNpbR0Ruq7v2dS1CpYiwfcpGKp2svthAPglr3YHOu9QS9e4n17uv6OI21HjXlYa02K3ra00HcOBV5xhywBcryKnYCIwHBTUlcdj_nng2ftgawTqlqEkGyAK5TDSXZbR50mGEbH0ugac4N6ER0NedLXqU0_Vc29r0N67krgys9bdCJnQ2UGSiy8ZKvyq2cGGgdwegMlKkly74tYCzjDWu8FUhNQc5eYrUAZKvg31pf-KOTAfKRYqL1AnDinoBEwduu3eT2kKyKomMhAgUrghfcIZ3Bhn2VNL2UR8B4926A2SwSTTK910z_xqyn1zXzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5adfd6fc37.mp4?token=YUEiJtIW7XxFxSC3z6ckdJa8eNpbR0Ruq7v2dS1CpYiwfcpGKp2svthAPglr3YHOu9QS9e4n17uv6OI21HjXlYa02K3ra00HcOBV5xhywBcryKnYCIwHBTUlcdj_nng2ftgawTqlqEkGyAK5TDSXZbR50mGEbH0ugac4N6ER0NedLXqU0_Vc29r0N67krgys9bdCJnQ2UGSiy8ZKvyq2cGGgdwegMlKkly74tYCzjDWu8FUhNQc5eYrUAZKvg31pf-KOTAfKRYqL1AnDinoBEwduu3eT2kKyKomMhAgUrghfcIZ3Bhn2VNL2UR8B4926A2SwSTTK910z_xqyn1zXzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/funhiphop/75201" target="_blank">📅 00:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75199">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فعالیت پدافند در اهواز
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/funhiphop/75199" target="_blank">📅 23:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75193">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">محسن رضایی:
ابوظبی به عربستان تعلق دارد؛ امارات ابوظبی را به عربستان تحویل دهد!
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/funhiphop/75193" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75191">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کی بود میگفت اروپا اینترنت وصله؟ اونم بزودی قطع میکنیم
خبر مهم شبکه CNN درمورد ایران
:
تهران قصد دارد شرکت‌های بزرگ فناوری مانند «گوگل»، «مایکروسافت»، «متا» و «آمازون» را مجبور کند از قوانینش پیروی کنند و از شرکت‌های کابل‌های زیردریایی حق‌الامتیاز دریافت کند.
همچنین، اپراتورهای بین‌المللی به دلیل نگرانی‌های امنیتی تلاش کرده‌اند کابل‌های اینترنتی را در بخش عمانی تنگه هرمز متمرکز کنند، اما مؤسسه تحقیقاتی «تیلی‌جئوگرافی» تأکید می‌کند که دو کابل اصلی دقیقاً از آب‌های سرزمینی ایران عبور می‌کنند.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/funhiphop/75191" target="_blank">📅 22:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75189">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🤡
د فیلد مارشال ماحسن رضایی
آمریکا یا شرایط مارا میپذیرد یا با موشک مورد استقبال قرار خواهد گرفت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/funhiphop/75189" target="_blank">📅 22:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75185">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ گفت من یه پیشنهاد دیگه دوست دارم از ایران دریافت کنم که حمله رو انجام ندم.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/funhiphop/75185" target="_blank">📅 21:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75184">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">زیر این پست زمان شروع جنگ رو دقیق پیشبینی کنید  هرکی درست بگه یه جایزه پیش من داره  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/funhiphop/75184" target="_blank">📅 21:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75183">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">زیر این پست زمان شروع جنگ رو دقیق پیشبینی کنید
هرکی درست بگه یه جایزه پیش من داره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/funhiphop/75183" target="_blank">📅 21:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75182">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یک فروند هواپیمای ترابری VIP C-37A نیروی هوایی ایالات متحده که حامل مقامات ارشد نظامی/دولتی ناشناس بود، حدود ۴۵ دقیقه پیش در پایگاه نیروی هوایی مک‌دیل، مقر فرماندهی مرکزی آمریکا فرود آمد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/funhiphop/75182" target="_blank">📅 21:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75181">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=aApkdjPVr3wC7COZPcTgQ8RMkWQCByuABqIbHyOIc5ILiaTEBvEqJDo9edIMYEiM_FdmHmALpjt0ny8MhL19M5biVPdyP8VXNQt2tXz5zISzVJILSSMhXtQYD4z-n6PUuLjM-ITPmYAzlFk5qPmW6xqqfuMI9H4b-g0q2eP6xyBQyWmdEN5b1eADR0dTbRZom4N5xKxT01ygSm1PC5Ryt3LFkaHdnxV8ivM1Oz0FrDswM85Ovj3izPSJMhvgE-Fk-LBCBl1NpAsbD_016c6u8HnIdfblzCrJUqEG3F5GWXDMfyrkNM5ODXrm-P5zXYCfbq_HzbwUzSZbPjY7djtyzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=aApkdjPVr3wC7COZPcTgQ8RMkWQCByuABqIbHyOIc5ILiaTEBvEqJDo9edIMYEiM_FdmHmALpjt0ny8MhL19M5biVPdyP8VXNQt2tXz5zISzVJILSSMhXtQYD4z-n6PUuLjM-ITPmYAzlFk5qPmW6xqqfuMI9H4b-g0q2eP6xyBQyWmdEN5b1eADR0dTbRZom4N5xKxT01ygSm1PC5Ryt3LFkaHdnxV8ivM1Oz0FrDswM85Ovj3izPSJMhvgE-Fk-LBCBl1NpAsbD_016c6u8HnIdfblzCrJUqEG3F5GWXDMfyrkNM5ODXrm-P5zXYCfbq_HzbwUzSZbPjY7djtyzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله بعدی امریکا کوتاه هست و میان یه لایه دیگ رو حذف میکنن و دوباره مذاکره میکنن و فشار میارن که تسلیم بشن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/funhiphop/75181" target="_blank">📅 21:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75180">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آکسیوس به نقل از منابع خبری در دولت آمریکا:
نشست روز گذشته تیم امنیت ملی آمریکا با حضور ونس، ویتکاف، روبیو و رئیس سازمان سیا برگزار شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/funhiphop/75180" target="_blank">📅 21:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75178">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnZRBhhQWQxeziI-OI1sHY3K0hZpkoLiuvpq4SaTTkj2tw-VMXrroqTM6V0dthnNCmnzixNNvltEub0xVCLMsMsYGtHU9AJR0FHAMigVyNyN_Ne9Pvo-u4xWNj0vzdUL4EOYdSUWIH6MNOfy5VOp_8l1dNcQMIkM3orVv2_ZutQl-17dAd-kVM7X2oy0Mthyb3tCZFlT22Kx686tPz4hWuicm9lEPfVA4Ay11q_BUduDyGqYABdNvZxPWXBw2cmQ_p--brN4ecz2mqbTXOpua66fWl5qnpYw1R_GH5SBLYGjNlNeSrVPzV1Ps_guXF84p0DDt1HV2m0--_y4cpfv3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پریشب: آموزش کار با ak47 دیشب : آموزش کار با pkm امشب به حول و قوه الهی: آموزش لانچ موشک  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/funhiphop/75178" target="_blank">📅 21:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75176">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qx4hMZRb8134X_vdLsEl4b3u4P4j4KNX4QwRJNm4LIgHIw3xuLCzF2vYkImGj_BANtAmPDk4Gh6Qr3D085MQpE2QYz9UVEysuAOUzdaLv_A41O8ca_BIrmEFwK4QTZ2G23H4iYwC8upxKsNoqEhdzFPTEokQfVooA5p6G2LId2ajGsS1PpZ9LNHbqviXb1GamHjzRI23jCNtfj1Sv7u2KKzUICtPR9wiSH_MyKauHMuYJMEiEZJokETir6nuaEdBYFoLTOCXJfEFOK8mJn0AL9jgq6qhXQM6l2gj0m108OJP1Gdga3K2loAwsgpSyyNas1BRxNj2VTxNJj9oLGxUDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/funhiphop/75176" target="_blank">📅 21:09 · 27 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
