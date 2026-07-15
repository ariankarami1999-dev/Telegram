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
<img src="https://cdn4.telesco.pe/file/t__wUD5960hfXh1yJzC1VboECe33bVVc130ScU6CzuLMnVPSJ1z8_IElWBps-Ya-jwkz3N-gF55iFyySrQSHJFl4XnWK8TUP-4TV9B1FXWUozqNLN0UW1BiXlXh5PvDY5i5FzPrCUgGUkInFiGcjmwSpJAMMfu5mkyOl3ixhfmbnYSOQxh77fdbFeexTdvgRUGl-n94PUl_BwykOCNRB1jqTfl7Po8aY7OU6oXwjej0mMqQdliB4KoojOuPbKyuq9gSEQM0kJd76mINUPOWVbehrU3VzpVl3nqFsi43_t1IPketbQsb3eea_J0a-UjZT_avp9lx1MddaDI4GNRWb-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 474K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 00:57:43</div>
<hr>

<div class="tg-post" id="msg-25813">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcEFqQhZ0DllI0yiTumTYgOkTUiCeXYtkbix7Z78b8x-eYXkesKG9tXZWD-1AYtQ2jfHpfK1wpj3mw0zqvW7hlsto4Qy4D3zMzdK5CA-vzgZB6xcreujEM2pOAxzf_fKgUl0vesQZnvAngOyNWg-vVaOte6zdnrnKim8KplGN5A-mIDxrvzDoOTOh3d6I5ll7saXcEjufqYOLPQ8UhXpwY6UIr1U2sWvlIBn5-SWZ2ylS90GX2B66MBxZwMmi3ZR0TvHmjjL3QoCRfEriM8cJXq9p5696-wn-CLyofKqmrY-YFSiUGjXAnhmtZ_Wyhz6xS8v_8DwwVXk6lP9vbK5Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/persiana_Soccer/25813" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25812">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsnydyTGNgktuQxkJT71dQZy8p6wpvuRo4y4zSLaVQlyyQmUj-lHyR6K_DbcMuNg5_nt_8wDQdRh7JL-DAn4y6eFqbYt1_2-p2lVXXeAz2JJEQxjM-kK-xAkkOmIzXCfupLqLytlCqArNB26M0BdUu2ooUZJRbwYWk17CkpjJmSmxsSAlfvofuLQKYWyzYiQVklw9tRJ5J_-6VLqUDtlN3fMUQMM07cX-RnGlioN6fzSgpHi88UdQ-WD9PlkssLaaHUkEl7clf_HOlDAe_7qtfVCOCvArKG001aAB-fU0q-zAjfAKC59UppbP8X5G60emkvoA5IfAn0p1YBnXr0wBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال‌جام‌جهانی2026؛ روز یکشنبه بین دو تیم ملی اسپانیا
🆚
آرژانتین برگزارخواهدشد. امیدوارم قاضی این دیدارحساس علیرضا فغانی عزیز باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/25812" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25811">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOCYWebnztwqiXGijjhcwocz_s9UUNfysrJuw89OiLiztK7wDN0_33SMA_MzRaOcx5ApA1wGl3D2GCNvRQpdxW_3_cUvIAFNryUGQH6UwRIroVpDmAMABA9PYWRDDZmWVHxtyFVQ9QXwbapHSD0iQMKSMkrINbvBNibanUV4qEgldZCMwV_UtApiG_uOMMFvXg4nErV3biLinxbsCrWNsLMCmk6178lJD9puLacQ2UffAeHNdJVhii2sbc7sYBhv_lfIyPqsa2FpBK1QyYuP1Y4Wji5PjzFOx6_nqPMhTzJnQHF-7BQT_BOOVRuIPTa4g04k_5Ry0i23sNkbaWHwig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/25811" target="_blank">📅 00:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25810">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lf5WluhlqDQyN3MxbTm6rl7L-HLX8NDbWsrxJTSrtmwuk4vuY-_ymfEE28tCHTfGcExAfm0O247rBnS5xOU2gK6vtH-kqN5Vg7X5AGOR9mRL4HzlvQJVLGULYRcGK8zzvwbDAG71RsvJj3EXd7RTf7vtUjGzVmeb2oTEXOH1LO_iutg_rAyFKVPCz8oGvueZrGe5AuTyNVRFrvMOiMxGV7y6gI4K0njNFj64JySlR7ZWhxDXb4LMj7EaRmSiOfx8cOuo5E4pcnU1qx6BTWrV0gzj_sdk-7EnHo4A8bL2G6C9J3oozbZmsMuM5Svh1lqHpRN7uZNU3AXMaRybhKZ4gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی 39 ساله با دریافت نمره فوق العاده 8.9 بعنوان بهترین بازیکن زمین انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/persiana_Soccer/25810" target="_blank">📅 00:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25809">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZZaIPU2bizYWIGbHu56bqYygynfYgJhPKevcgg-gYWLdekVT_kS8zdYG3Y3gt-shLvalyD6djtIsiL0dynGuPeAhJp1-l51Qt14GKdBRd80DOJ9s1YN0PdtTGAybUSBo45BPgUbDRdRxZyePudO3_0lRnpwo0WPGg_2lyZwoGqRF2ftfoMaggOJeVSKz7muNyr2CWavlLLXo09Kdd2AFypFCzEpe0Dd5a1R6kh9w0HEHDwN_T3OMu-5UhfZpe7M7XQkDLKgthBDwvrxmg-nAAKbo_rK85uAB8ILzuF8rqQu3UBx5mgILZWRB_ZzxVpysPMxc66ZfAsBFv3Rbjn-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی 39 ساله با دریافت نمره فوق العاده 8.9 بعنوان بهترین بازیکن زمین انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/25809" target="_blank">📅 00:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25808">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovZy_yrznIlZvq2ncejJtQtc33ctt8ch3zSMZf0hiCn-duWoGpERp2JhptA4WZ3LDTKB3uPMre5yfIy3k9izsUbIGXF_0Rxj7uzDBH2ByCStFQPyzeSnKAYTpKgV1gArTTGgMRg6oDhl95ZIjyCh-44pVEBzNlG4jRi9SP-0MbSZBw41BJCPh7p5QmbBNKoppZ3UvqpGRkJHmLiv6POt_XHXpei41plLiEp5qfcxE_A8Lq_Ldi-Acy6-Jf9e1kEbZ_T-XmXSS7ZlU7e1VFpHi2WkDfkfnUfP8Ymw3Gky-9gfgQnMv3a-l40mC7juXDfpSS641vELy5g-xBxPk345Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/persiana_Soccer/25808" target="_blank">📅 00:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25807">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oj0Wa3xfTQSBBpeA4cKcP1zkwzxSbWaBxh0nDd1kW3qAJKAMjnqjxFfqidLzN0dKc_rvhxBFJhsURhUYjjGyO4FwgwPlyRchufNwCfpJKb-z8zsxXFiAKIQMxiy2NclZRv25VxoFvkic89RwH02wSsEyUvY_Vh9rIPZJh1dRtisdX79gDvmFH6-gcuAbr0FFAi9S9vHDuLjUuBHlhjOnOC-YMtED7Qd-XuAKGmcG0qRxZQLjYVUswV2a3o7LpffA9Cj58k_Q3FqcnmqUQVOMkmJxZTAOeNeg79qQpGO04oaofiReE5qIh-Cz3bFDx1f-hM3KRXI9SUDDoLYyGfgV9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
گل دوم آرژانتین به انگلیس توسط لائوتارو مارتینز روی سانتر فوق‌العاده دیدنی لیونل مسی؛ این یازدهمین پاس‌گل لئو مسی در تاریخ جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/25807" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25806">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d89d4e5750.mp4?token=AK5MefpCNRmrwJV6cxBsWVKOpaEl6PQkHmhl7mQJLqURUs33xBSlnKUigyhIG3Zz5VjPZcPrOtFZmbPmJbNoagLmu5WgZAyrblIT5Wz_3KuDrKRylZwUaRtEJ_amFl0z4ZHQFmRRpANQ5x2-hlfyzJ7UCx7F813O5Q-itguOLPuwa9YVeTxZpXsiyXs4pQIvyziR1fX2RROuhkTymG3Yh4UP0SjQ9sbWNM9HU3dIcDq7VmkALyZynVzJDxjFR7RE97VRTYHbmK30-NGjdEe_DVF5HUk4Ur832u81Kih2rOp-vP6naAmLC7obHp_y825s7s4bKlnWrvvjXJYyWV_tng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d89d4e5750.mp4?token=AK5MefpCNRmrwJV6cxBsWVKOpaEl6PQkHmhl7mQJLqURUs33xBSlnKUigyhIG3Zz5VjPZcPrOtFZmbPmJbNoagLmu5WgZAyrblIT5Wz_3KuDrKRylZwUaRtEJ_amFl0z4ZHQFmRRpANQ5x2-hlfyzJ7UCx7F813O5Q-itguOLPuwa9YVeTxZpXsiyXs4pQIvyziR1fX2RROuhkTymG3Yh4UP0SjQ9sbWNM9HU3dIcDq7VmkALyZynVzJDxjFR7RE97VRTYHbmK30-NGjdEe_DVF5HUk4Ur832u81Kih2rOp-vP6naAmLC7obHp_y825s7s4bKlnWrvvjXJYyWV_tng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
انزو فرناندز ستاره آینده رئال مادرید با این شلیک دیدنی مانع حذف آرژانتین از جام جهانی شد؛ دقایقی قبل هم گل دوم رو به انگلیسی‌ها زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/25806" target="_blank">📅 00:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25805">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0c717972.mp4?token=fsaddars4hUrHUiqz2RRNOyv8SPPXo7blEj_geXikWXfhduTCvvEA9Hwzs4pySSTB1PWs6sdfB_TFi-hafqdhT_Qu7yWcsVYipRjfrnzXNVOsOc8H5BRNuwtTPQK0uw5v51VP9z5JUbL2rsj8CAyufdEfHIYZXClZ-Jn4UvZ9FifpMh04jeavHGIX5qQgtLaFo7vTjxETkS40O5AgBLaEPM6QYN8b59unee2x0cFCYWfSqtbQaTBYQhOqmV5oSQuoKyBEEOeVLrr0QOwayC3ifaQAWGFVPZYCgzyM44WhxL1xJHwYLbhrKsx5x_Fz_rquH63HxzsJP9mqHmyJHTFoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0c717972.mp4?token=fsaddars4hUrHUiqz2RRNOyv8SPPXo7blEj_geXikWXfhduTCvvEA9Hwzs4pySSTB1PWs6sdfB_TFi-hafqdhT_Qu7yWcsVYipRjfrnzXNVOsOc8H5BRNuwtTPQK0uw5v51VP9z5JUbL2rsj8CAyufdEfHIYZXClZ-Jn4UvZ9FifpMh04jeavHGIX5qQgtLaFo7vTjxETkS40O5AgBLaEPM6QYN8b59unee2x0cFCYWfSqtbQaTBYQhOqmV5oSQuoKyBEEOeVLrr0QOwayC3ifaQAWGFVPZYCgzyM44WhxL1xJHwYLbhrKsx5x_Fz_rquH63HxzsJP9mqHmyJHTFoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نیمه نهایی جام‌ جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/25805" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25803">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db22288ce.mp4?token=nBXRtdhQpMLsmfJR3CfPniXzOSEuuez1-xcGea2pNkFMVp6Er0sgsVFM9NWRjlTtxqE9wWIs6thcI2zohbie10MCuaBv9VIYpFEE4zcMmQA2T_UMb6v0nyk6SjNLPcb6U1GW-8CdcHBZHqSqxShtuzbRIBWSbWdL7b42iHUdQkqHsr1-f1E8nU9EJ6GplXi1g8sTxnInKuRyzjxErFVicVA_BGOLuCSGdA_-BhAYIyPCTUkvpT6qCEPYIpEXLwZ5ZaylSxyBIstkcNV6QDauEO3bYR4hlW5a4IB2CaDVwgvoYX5nKlRqeAuAYGCFcyNF9_jiWwE_nvNKefa8gM-T0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db22288ce.mp4?token=nBXRtdhQpMLsmfJR3CfPniXzOSEuuez1-xcGea2pNkFMVp6Er0sgsVFM9NWRjlTtxqE9wWIs6thcI2zohbie10MCuaBv9VIYpFEE4zcMmQA2T_UMb6v0nyk6SjNLPcb6U1GW-8CdcHBZHqSqxShtuzbRIBWSbWdL7b42iHUdQkqHsr1-f1E8nU9EJ6GplXi1g8sTxnInKuRyzjxErFVicVA_BGOLuCSGdA_-BhAYIyPCTUkvpT6qCEPYIpEXLwZ5ZaylSxyBIstkcNV6QDauEO3bYR4hlW5a4IB2CaDVwgvoYX5nKlRqeAuAYGCFcyNF9_jiWwE_nvNKefa8gM-T0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیرانوند: چرابعضی‌رسانه‌هااومدن‌گفتن مصاحبه‌ های مورینیو درباره من فیکه؟ اصلا فیک باشه وقتی می‌بینی همون‌مصاحبه فیک داره به من روحیه میده چرا توهم نمیای همون مصاحبه فیک رو پخش کنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/25803" target="_blank">📅 00:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25802">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsLsHrOWAEEVhVUDrG1UIogHpSuv9FIBzdqI0u2rrYY5bp6Y9ETH67JBrX4znLNN17d3VsFqFMMeFizkxl9BmVXtNzAUJlULXm0R-i4Gnq2ahHSApfDwcdOJpXSwDy8ikcDiJoqIdEQ05Onmm9Ka0k0BsHBvkPPOntAwNxWko_g0CP0i3k7SK0fT6yMDKhJOWmO3q1j3RFxcuktaHFKmQTKgQpGhRtLYcuNBQIlIt2XYr49-HrMHsZ8FyVTVSF3FO1m8VcOB69ENjaMdzXksGo42o3MKkO6EEAirB-FS8ULvRtlVXHxVlhCuCgMcoFW32nEIKYoLrh27OsQJqsZI6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/25802" target="_blank">📅 23:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25801">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsO6lWmlYZx4vdwgs8XOQVhfchS6Wiic4AgtgsZ6NWvuCRKcdOy0S6koCXrb42IRQB1H82WjrZBtmLIis9QMXUr-aZ6vYKpjJ9SbFijK8nCLfkkF3tG3n5GQQz6Xzxbul7nrGdopeWQK950XqSGghN8sXnB_L_uuSLqEdb-Q1_d4b-BM-5x8b22evPSwGbzEGQB45pp2_MjWnNeDEksXUve5ei6BPTVMb3POFfDUii8C1XzJKp8lIdxsdFsuS9gTlLWgUQ368MrIvwJMXBW5Ekpgl6muz0_4_CfznRXi_FwnIRCsHoI7lteWG5f5-VkFBDE0xrk40QsQycJ0j1jEtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/25801" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25800">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8axSPAWzmwnKQsPI8bjgwlz7mRCIBI8h1AahwzB4TgQqMFA0J7X0HPlefynVvM0MO7Dp4AG1S24QZnNT1chsIwk0zmm4OKGOZWWINraGp7lO22A32TjO9qfIOoNGr3tckeaS3uG__bBYw_hYpn_SIqzI9TL2zS6BPc1S27pCMKLYIKeVw2sRme9zyu5Qib8ICh9F-DPVjobFAo3vA-zNxf04aQqSajM_DaJVrtD6E3B-3T1Or08t1mDILhAkX2ZC36i79OTz5wT2b3OVEfaNoNSAgYjEj-3SSqTgzseQPffPCr0uh8a-k_mcS1z0BPoeJ5fMolOQqJfs8OoYZOmOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/25800" target="_blank">📅 23:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25799">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30d2d3139d.mp4?token=uXY9WxJ8pgG93CTLJ8KturRkXM2ciqaRwYIcIuFeYb2BCIM1XKirXL4xT56-ij2GOH49jB0bhKXzIHLgI5r-uhp2cdSVjoJNXeP-WS1boWZT_lXgmIb6DyuSArQh3SBuyEa0abQdnUUeenm-1zMQln-IWexMXWQdZ8X5l4IjqgnmXz_g8jZ5knKA6X20kFkTy-V3PAL9ZWqo7M6B89UcrHiqbleGsR3GHN_1Ul2RnWqP2NniDtsRureg9dRV3cMR354_0XkYIaqHLK_e945p4LZGbxJfU0AdDO94MwGU6UVP--dULRsWzCl6jeF7ewY5aEHy_F-Jt3B6FIgadYo15w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30d2d3139d.mp4?token=uXY9WxJ8pgG93CTLJ8KturRkXM2ciqaRwYIcIuFeYb2BCIM1XKirXL4xT56-ij2GOH49jB0bhKXzIHLgI5r-uhp2cdSVjoJNXeP-WS1boWZT_lXgmIb6DyuSArQh3SBuyEa0abQdnUUeenm-1zMQln-IWexMXWQdZ8X5l4IjqgnmXz_g8jZ5knKA6X20kFkTy-V3PAL9ZWqo7M6B89UcrHiqbleGsR3GHN_1Ul2RnWqP2NniDtsRureg9dRV3cMR354_0XkYIaqHLK_e945p4LZGbxJfU0AdDO94MwGU6UVP--dULRsWzCl6jeF7ewY5aEHy_F-Jt3B6FIgadYo15w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/25799" target="_blank">📅 22:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25798">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_yKkza6KYFUfJ1rYTlitJQbmASfdIkQo509TR7drT48e45x-DjibM38TsbW1nX989xXOwLMEhOFWJ2yy5g8bfoqCIKtiN2-MqteOquVC_-FHkNfj8Bnj4oGjp_7fEoDXuO4jrUfxPBLg2WiU0sjjnYes75ejmRhkHt8RjhrXjs_l7zlBzyBPrpBSnQlVRzItiRVtaJSAWgM2fqbMqiGDFrzchJjh3myGTzwlUouTJBjJKi7b1GqHUP9uqgOJc5yfIQWM5q1oSAzL-KOGc8S8g2vLq492ZFKhWfeXF0ZG7rCyTXcetmJSrYZC19xLFGk-6HVSKvSsxB2wGPtEMkQdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معرفی زیبای عادل خان فردوسی پور از مهمون‌های ویژه‌ برنامه‌ امشب؛ علی دایی: تیم ملی ما وقتی‌حذف‌شد که سردار رو خط زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/25798" target="_blank">📅 22:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25797">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c436909609.mp4?token=eG_B0Avi9111S5aQo-sHxtYdxgcr9t1m52FwqRhMwh_m8q0UpuEyZzKKQU4G0Dtwjn3fiLkmZXFSLRNSZLxxXw5atnEkeK5rCN7QdQ_n7jonKZEs7qN7LqDkGoYMdx_3Bx8gZcqxdvvCjun9J6i5rv9XxLf1E-4-eswdsdwg8ptNhnM2RYPtBHCNvEBNmssgcs3NUeC2axg2Z5NsKQ1-O1FOr-8jU53OH8Bej75buzchBekstHDbnTtIMS4jeGQqHbjr2qt5iDK4Z2j2BQYQbdD2rM3s72XRQk9rPwGghHcbcGs8XA359oUNuBx6S-JeOvPt0ATJhwscJ0JAZ16vMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c436909609.mp4?token=eG_B0Avi9111S5aQo-sHxtYdxgcr9t1m52FwqRhMwh_m8q0UpuEyZzKKQU4G0Dtwjn3fiLkmZXFSLRNSZLxxXw5atnEkeK5rCN7QdQ_n7jonKZEs7qN7LqDkGoYMdx_3Bx8gZcqxdvvCjun9J6i5rv9XxLf1E-4-eswdsdwg8ptNhnM2RYPtBHCNvEBNmssgcs3NUeC2axg2Z5NsKQ1-O1FOr-8jU53OH8Bej75buzchBekstHDbnTtIMS4jeGQqHbjr2qt5iDK4Z2j2BQYQbdD2rM3s72XRQk9rPwGghHcbcGs8XA359oUNuBx6S-JeOvPt0ATJhwscJ0JAZ16vMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق دستور علیرضا بیرانوند مجسمه امیر قلعه نویی درمیدون‌ازادی‌ساخته‌شد. بیرو دیشب گفت هر مربی دیگه‌ای بجزقلعه‌نویی این نتایج درخشان "سه مساوی در ضعیف‌ترین گروه ممکن" رو گرفته بود تا حالا مجسمه اش در میدون آزادی زده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/25797" target="_blank">📅 22:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25796">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mx2MTsnyryxDtBHHMBRTM_DAOTwiUTDL92YSPvXoQxb61rQFArBD43j6BB6aoPyZF1SyScSREXCzMTQw_fo_hzd1OYYUriwG-KMCACyUm90wkXZLAsvZp2p0BQXhy5taNbTxyU2DMJ4IpXnmUE1lOiGxg3xo4ku6zLDWlqEXjV7mVnNC1hWHiEVdlZcowFmksA3IqRbrgrNgv0oRkE6qkfLya91RTd76rr5VD3Zf2ZXT1Nf2ALPVY86Bk9zq5XF4jXKN04m3lKeZR-eNv-Zc9s6Go_QOsgKXwrJtuLVxGArKgESgRw_6h0ysXKsPD_E_6xWqkH1s5gT9_N3jqjsf2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هفته اینده هلدینگ خلیج فارس؛ تغییراتی مدیریتی گسترده‌ای درباشگاه استقلال ایجاد میکنه و بچه بالاخره از هیات مدیره رفتنی میشه. شخصی که تاثیر زیادی در جدایی ستاره‌های این تیم داشت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/25796" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25794">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113eaa3d5a.mp4?token=IPxthAn9epxc_wXkbgSZMBKA48LXyS9fat0I9j7bFYE0pcc20o1VceKaEpFaNdRsT3xkvnhjx6Yt1khg32cVqMT4hXs7fKbNYonamAK1TNjvISd9HygOJOF39MuOatXOcVxOsYoNhxPdNlnNC_D8Wkn-lb6Bm6qUw1qcQ_616ay3FvpGAKZigaVdmr1V5dMEPbdRtwCFlz_AcSYpD1dGE5MZ-DuPNORjR2YE_bcqdvAGoF96ZITGbXcUrcc814ybijHhnTXmxpzARQcq4elHD4KjdHDr4Y4t6YbkB907syMPpMMn3lx4g8A9fGiLu4uQ4RCOR82sanm6GSuMQI-CdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113eaa3d5a.mp4?token=IPxthAn9epxc_wXkbgSZMBKA48LXyS9fat0I9j7bFYE0pcc20o1VceKaEpFaNdRsT3xkvnhjx6Yt1khg32cVqMT4hXs7fKbNYonamAK1TNjvISd9HygOJOF39MuOatXOcVxOsYoNhxPdNlnNC_D8Wkn-lb6Bm6qUw1qcQ_616ay3FvpGAKZigaVdmr1V5dMEPbdRtwCFlz_AcSYpD1dGE5MZ-DuPNORjR2YE_bcqdvAGoF96ZITGbXcUrcc814ybijHhnTXmxpzARQcq4elHD4KjdHDr4Y4t6YbkB907syMPpMMn3lx4g8A9fGiLu4uQ4RCOR82sanm6GSuMQI-CdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قابی بسیار زیبا از سه مرد شریف و عزیز ایران در آستانه دیدار امشب دو تیم آرژانتین
🆚
انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/25794" target="_blank">📅 21:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25793">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/558fc696a6.mp4?token=ISyZOCKv0RWZr0VNa2Dayxus6rEyDz4eVwTW3YzCMyMwLuMckOoXPNEYbC8SAzEwv9hYr1ypWGLOyly28G6s3StH-UuXVNk4e9BXT75WoU4dxjmogYKXp6CbAnr1pRhLASLJZjjYB6Fnzvk03TDplkicn-_SGlnu3U2-F3VJP5o_tHSKQOKZHUPZlk6vPAbAmeNzyseQrjqqZARfxZ0C4T37PNOehVEJ3hqEiGpVYAyebINljnuu4VqQm3rEBz0iDeQwIGk7aF6UnRfa8IQyZNGK7piBj0KD70sPG-qnga68orjheE95sEPt19ldeBeYFoPfRG2zCmRwpV48hfAGmoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/558fc696a6.mp4?token=ISyZOCKv0RWZr0VNa2Dayxus6rEyDz4eVwTW3YzCMyMwLuMckOoXPNEYbC8SAzEwv9hYr1ypWGLOyly28G6s3StH-UuXVNk4e9BXT75WoU4dxjmogYKXp6CbAnr1pRhLASLJZjjYB6Fnzvk03TDplkicn-_SGlnu3U2-F3VJP5o_tHSKQOKZHUPZlk6vPAbAmeNzyseQrjqqZARfxZ0C4T37PNOehVEJ3hqEiGpVYAyebINljnuu4VqQm3rEBz0iDeQwIGk7aF6UnRfa8IQyZNGK7piBj0KD70sPG-qnga68orjheE95sEPt19ldeBeYFoPfRG2zCmRwpV48hfAGmoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
#فکت؛ ‏بیژن مرتضوی تو فینال‌جام‌جهانی حضور داره، اولیسه و امباپه نه؛ تعز من تشا و تذل من تشا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/25793" target="_blank">📅 21:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25792">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNFO3j7cliQT8lVASY8LkjeLi6isZRsakB_ogDe5NvqD46zhwteD3mzvp7WL8lY_HNmmlHCmDaHWXzyhxlGJUB3fuKcREnl5Woi8o_lQ7siU4_gpfgsMz18ZynDmIciqi--AB2b1Orhb8KpREQm0KC4wGrEbuoKKdj0QXunVQolRNmHyxrQ50ElanFloN3gD-qNZnmpL3tllOlvL9ufZe0heiMNNKL9yAuu_bLzaaoEEQt-KV4BCohn02yJsoXArbKHDoKt69lJxSsClu-MUVrWe8abeE1ajZtokEhQWADWEhbzWLWm9mVlfu_3NIxtXo9QnuvKAR8a4xTRXoCoG9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
🇬🇦
#فکت؛ با دبل‌دربازی‌امشب مارسی؛ پیر امریک‌ اوبامیانگ برکورد 400 گل‌زده در دوران حرفه ای خود رسید. امار فوق‌العاده اوبامیانگ در این فصل درمارسی: 18 مسابقه، 10 گل زده و 8 پاس گل.  گرینوود هم که در منچستر سرنخواستنش دعوا بود آمار خیره‌کننده داشته: 15 بازی،…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/25792" target="_blank">📅 21:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25790">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GX99Y_HuA4cO-xdaIKvjb9H26NnT54BJtfCd5AMwNrPTp1SlEqNlFUDU77UNJNd14hj5wC6-roCA-UZUONlr9lh4UmRuqxHR2vHtUek3EtT4UXefOk7iex-egi-dNU4o3SEu07WSE1UGXzHdw3M6c-Oy_XyKMgNfNAIfKaZ-riuUu9R0B_DeAzS58Gq-lpzjp15doMb2QguBHbqZq70c2FduWKBPP9reWV6wLDsWMTelVpfepYGBtlsg_ledm-HKG1uiOLusVL3SOgS3Ps3NdbiBM7_nVvUvvpH7wdc0Zl7inK5d9P3eZPEMpYCUwexV6pnla1r5Be-LOoVUjBfBhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UciGm-K7cCiVReEYyecFcTGG3G0neNxpOihPJUw8bnfMULB9aN5H5Uf7OYWwNYiRtZtdst0SFhiRqfJO4HZGllzInUhetO23iizYW7xQhZNH-Lvn2_wOjxNlqER4lcgZ3dT5pt2yOG8hzgMhfNcudBFihfRq03lHNSQqpkcgU-_nx1Srb_locf3ZjgQm77VHyeTpAqTAw_ejSMZ-B9k1oLk-r0xxav_G3oslgKybmnJn3O0qFepo4ZgBUdNKs1Hj5sDuzM5HAsrBKVlIe6iCWtwPN2uZaA9h6_nibYlk6YjLc0kqrCmiAVtRrHW74G3AibSWPyBNo_H1t550Irb8lA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام‌ جهانی
؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/25790" target="_blank">📅 21:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25789">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BB-F3OfstbJwU9bsLg5qqqGRXX5FDUxj8zOci0e2wPtT35yTFv3NWev5jxIGxxfJyYM1A_d8QJUyrowp0ZCKQ4b5Buta7qhzPNWMAmef8bie2KaEjClD47h1-eqfzi4nEIBHe5Vhg2WI0UqSFX7jKbKoTtVxeLBnIDujEIYqGRy64jvqSA5tICw4kFxAgxc5wZeqo_14oI4EAm1ml7AzubcS8zZfXdK-d8dYaBIcKAjs2yJu8Lg0pIJkx21U_r1UWJNrxgS9ACvhNGUQAfnfAqfUvkmeTqfen09uj7n9ispQ2jo9BtEUZNXBX93tv_LXx96UU3MRi-vdWmVnPfs1KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/25789" target="_blank">📅 20:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25788">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSJVe8IUBdBNdawenDOcRf0Heh9krbxA2Kacs0jtV9VSZ0iOFMgUmKZHXG5I0gnNvAB7WgAcDo0tckKFDE2nUp1-2_t3SfJZ3VY-3QWb3VA8fRt67EaST1ZFsoFc9ii431D6lwk1WjaV75elybDlwnZpSE_Wn1XghQ63i4W5rOWN29sUWTJUn-7xguQCGNd9nAtFVEovCNAJMQJRxp83mXKXJHkH9PUTWPK5yDfScEE4HyTemRQaXtxlAMnXYnDT_z9lw_sy5ZHQBuRe4eQqzXnbRzfLWnQ5slTlBluRy5hpPaq-yOMpb6J061mFozMYPOSCGZ9qIAsGyodJh7HdsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لئو مسی در نیمه‌نهایی‌های جام جهانی:
دو بازی، یک‌گل،یک‌پاس‌گل،یک‌برد، یک تساوی؛ هر بار که‌ مسی به‌نیمه‌نهایی‌جام‌جهانی رسیده موفق‌شده راهی فینال شود؛ این اتفاق تاکنون دو بار براش رخ داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/25788" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25787">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b4c95cb5f.mp4?token=gRFpzwIzZM4RxPRl4UdhMG-Y5SnPPgd5zJJguyx7cIFG8duIemGdPoVsxpbutHw7UATqag4He-gOvRDsNt5XyqTabaJUKnc4FHUOO0rtQkHPE_kTTpYJYpTg8a_fEu0TWueujmx4D6AnH7B8nhJv3d1Al4n8s0_g7yKmpFYwB9G5GhPHA9_ZhfXHLeANufZj-T1WAazWjp--vwJWJHG-3X0rXjrt1azhC5QU7R8xOME-R5UG1HRBvUfitumdPIrTgDP9Z9tfKutOK2aIGhdKR2KIDsN4-Gk2AvNy0QsabcP_OQrck-x8MLdjUm1nGZAtYf47ipZOJiNnYapvzTo2xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b4c95cb5f.mp4?token=gRFpzwIzZM4RxPRl4UdhMG-Y5SnPPgd5zJJguyx7cIFG8duIemGdPoVsxpbutHw7UATqag4He-gOvRDsNt5XyqTabaJUKnc4FHUOO0rtQkHPE_kTTpYJYpTg8a_fEu0TWueujmx4D6AnH7B8nhJv3d1Al4n8s0_g7yKmpFYwB9G5GhPHA9_ZhfXHLeANufZj-T1WAazWjp--vwJWJHG-3X0rXjrt1azhC5QU7R8xOME-R5UG1HRBvUfitumdPIrTgDP9Z9tfKutOK2aIGhdKR2KIDsN4-Gk2AvNy0QsabcP_OQrck-x8MLdjUm1nGZAtYf47ipZOJiNnYapvzTo2xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇭🇷
چالش ترند این روز های اینستاگرام این بار با آنا ماریا مارکوویچ ستاره تیم‌ملی‌کرواسی با خواهرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/25787" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25786">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUNo-ttyVjLvGfVYFn1e0camMucDES_qLgOndyUqAfMCKJgl4aQEM2F68YjT0GAUoBqcqWRAj3ntkwK4lrV4UfUiDVn9wgWn9KR02DSydRXrujdgLmIIepC7Mqqgu4Zrh2AG4QPxSFQlL3OA94Si8feEHXXKYhCWaCni4NI4jktYxTDl2Jdqmn32tMLCmCp6UvRX1NKx0iYaXgzBMMJtX_pgJ6WT5sl6zAGd3zwiXb-mJxcYYYelE-XGd03gEF8RyfDNL2dXos0EkbcoCAA4TyBfB3lq_v8g_-inUymMCwEimyAd5lq_UjCCVZVpARDnxxlwoJ6tj_b2d6gQ-oOX5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
— آرژانتین
🇦🇷
🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت یک‌ماهه برای همه پیش‌بینی‌های صحیح
نتیجه بازی را تا قبل از شروع مسابقه ثبت کن.
🏆
مبلغ ۵۰۰ دلار بین برندگان تقسیم می‌شود.
📶
هر برنده یک گیگ اینترنت یک‌ماهه هم دریافت می‌کند.
🎁
جوایز به‌صورت
FreeBet
پرداخت می‌شود.
👇
ثبت پیش‌بینی:
https://t.me/betegram_bot?start=p8_r4EF37DCE</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/25786" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25785">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgzhJJ8U6P0klz_QtszAjNu_IF_p2I4q4UeZBj57u4gHRAGkSpywXgGKDBFmAOVpDVLO2zo5UpTC7SOzQksp4uJTj3WfQueAvStDSnXm_O7PmXcjrxE5mvlLEEhWixO9JLgFl50DNtx8bXRPKRTLPfn_qDTKq445r4uL4SfW1zeteJNVDsL0ErqS3Lc8DI-boxPQL6wkGPKk0dMYSjdw84vh5gbTXgH-xJzCRguaJY-IjeosPRaUn8FGU3h0sd-AnQ6Mop0tZaq7cKzCwDURjjfQyYJw7yy2zODrsN-_fFj0elWzA-Ln1QgU-rboWab-KQ8hEmFc7X5VAfLj4csTsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌دایی‌ و کریم‌ باقری دوتااز اسطوره‌های بزرگ فوتبال ایران مهمون ویژه‌برنامه امشب عادل هستند. ویدیو کامل برنامه رو در پایان این گفتگو میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/25785" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25784">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz1VgjnzTYZlBd9ZVrWgWVShn7_w4gkTlXrpdCO-jYOhlvcGwRXLS9iIwLB2zP11jyihWbPINdATn7SX2PZ3cVRlMm7Cxmi2ABrTRUHmwAwi6yH0uCa2NAXkLgWQ9vVB7GJ_wkFd0SR0sfZox6R2AK4zW5V_WTizSV-5lt6mmyZm4QHCJXv4m30zOaKMPq2v0nFLRK9TRGpTsQT2tnZHBPfqxN4zpPHeg06og7QxGE7q9_hpdQt71yj7LXe-smMnTUNe50z85LhfLQ78IfANTXc3eN7LUpUZcPC6Vm7cHzBrIjvRnaYyExpxu2uU54ZyY5ldPOdDHFl9Czf4_tbBhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرویس برگ‌ریزون بازیکن جوان تیم ملی والیبال در بازی امروز مقابل تیم ملی اوکراین؛ خودشم فهمید خرابکاری کرده زد زیرخنده؛ اشکال نداره این همشون 17 18 سالشونه جوونن. اونیکه تو 33 سالگی و اوج فوتبالش مفت پنالتی خراب میکنه اون درد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/25784" target="_blank">📅 20:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25783">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_YEOQW4R6G8zz00w1FNI_ErnKY38hTodgz-Yji5g-ep3eIa6oerSlUSS4MYpa0PydOPrrlRTnrmoK8iqhVHo-P8aCStnf5d4kRXzzIFU_nLu3kryWFBRF97-URaGBcXUSR2bCaa6UgkU_wQ7Kso9m-L4Xp6BOWLKBxaCnt45o-BoMPEp4kyiasChPTJ2-DSaLM6b3GnEM5rSz-pT8k50VCKLhApt-tZIMamgzcMNjMhU8dZyeL7yrAHy7mG4PhEHGXiLweKyvSjD2akyrLSed0fHqYwKyMGy_Ys46uoupEmFwypyxhuxM0sv0xoWL33TnH8mOxBVVstHU3KHAKN8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
واکنش جالب ابوطالب به انتخاب بیژن مرتضوی بعنوان خواننده بین دو نیمه بازی فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/25783" target="_blank">📅 20:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25782">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87ed733fb0.mp4?token=rZ8c5QieMUm0HBt-DK0VwPDh_WhDkuxP_VaQjHD3U0PF7L7GIFnJfkXUTr_bS4zcSWqkQS3K0A8X3BBQJrL9p6jiAAeXn_ua5MJwNu96BKqH4Pdnr6nDnqzfJ6aMV6WpFNMPfIM11Zne61dhlebPfS-45_W_SX52nQAdIU1M9DNNKxnChInLGZWGz83RiIvzg_TjfgqB6PutziWUOl94IU-CSegj-Pha6k-0Imx-IcxIiSW8I8UcMvHBpXhNYWu94Ee8z8K6ymVv9javgtg9Dn12FQRq5lC2NMGjtmqT4j2QGOoI0CsjnVTN7D4uwABTDqLRlQIpCvRwGZ--yMIV_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87ed733fb0.mp4?token=rZ8c5QieMUm0HBt-DK0VwPDh_WhDkuxP_VaQjHD3U0PF7L7GIFnJfkXUTr_bS4zcSWqkQS3K0A8X3BBQJrL9p6jiAAeXn_ua5MJwNu96BKqH4Pdnr6nDnqzfJ6aMV6WpFNMPfIM11Zne61dhlebPfS-45_W_SX52nQAdIU1M9DNNKxnChInLGZWGz83RiIvzg_TjfgqB6PutziWUOl94IU-CSegj-Pha6k-0Imx-IcxIiSW8I8UcMvHBpXhNYWu94Ee8z8K6ymVv9javgtg9Dn12FQRq5lC2NMGjtmqT4j2QGOoI0CsjnVTN7D4uwABTDqLRlQIpCvRwGZ--yMIV_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه بازی‌های تیم‌ملی‌والیبال+جدول رده بندی لیگ ملت‌های والیبال قبل از شروع هفته سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/25782" target="_blank">📅 19:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25781">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5e427ee9.mp4?token=nxePHNwwlJQXYsVuU8HWp3klrMFIhQh18b1cZtu8eYAYkEjbfipHhBp--bSz0eA2GjQPw-wdeBDTGfFu5HXJcvj1FjR6PA46m-JehS9dFKq0iArYZvWqxiSZOKYKGOh9d-XJG0k1WrNL2ab7AFglATbOPBRtAvH6YDZhfCY07JPkOlVPxTvmZdSRWoIgoV94UMyZF7jR3LSKypzch9tg5Hh2C5s5lTFGAvwEpCVIbl53aHRTnfvB1ZqD6Ca4RVr5mQG6GgLMdnqWWhw54kxBkX31cnfQ2h1HJ0ki67CpqFKyWKaXolOEoJVifd6t7Jg6AeJKilUba8BwjuwsfwfCnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5e427ee9.mp4?token=nxePHNwwlJQXYsVuU8HWp3klrMFIhQh18b1cZtu8eYAYkEjbfipHhBp--bSz0eA2GjQPw-wdeBDTGfFu5HXJcvj1FjR6PA46m-JehS9dFKq0iArYZvWqxiSZOKYKGOh9d-XJG0k1WrNL2ab7AFglATbOPBRtAvH6YDZhfCY07JPkOlVPxTvmZdSRWoIgoV94UMyZF7jR3LSKypzch9tg5Hh2C5s5lTFGAvwEpCVIbl53aHRTnfvB1ZqD6Ca4RVr5mQG6GgLMdnqWWhw54kxBkX31cnfQ2h1HJ0ki67CpqFKyWKaXolOEoJVifd6t7Jg6AeJKilUba8BwjuwsfwfCnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوزیبا از حضوراسطوره‌های تاریخ اسپانیا در حاشیه دیدار شب گذشته دوتیم اسپانیا
🆚
فرانسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/25781" target="_blank">📅 19:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25780">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f78ae3e4c.mp4?token=cLlk2bKYJdQs8jbw8q-LHWviHmxe_n-D1m2uO6c2klyGBUk1bpPP9tyyNqMfDlmihFmd4UFYa9GVNxo6ra7Qhckl9SmQYsZvAP9J4lCbajfA5snn8PWYcIAtXh-HjK-y_5KSG9oa4ChzYE49HTT0GLzMXHsrbs9pIcWMUQEhBDoK6aEEi3UZxzxseJTUYs9wnc1LuXor9xZTFU5mWYE-9iSafy4C-ogVX-I2HIb9FVeRb2M3ojynmLPwYehhWzjsEISIrq0qrRJvUgWg5w4Nd-82yP_HowVld1ZgYt_89WM66lLB-nG2vdS5fWmGQjaGSNDyYWPioFN7TU-xHMMQ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f78ae3e4c.mp4?token=cLlk2bKYJdQs8jbw8q-LHWviHmxe_n-D1m2uO6c2klyGBUk1bpPP9tyyNqMfDlmihFmd4UFYa9GVNxo6ra7Qhckl9SmQYsZvAP9J4lCbajfA5snn8PWYcIAtXh-HjK-y_5KSG9oa4ChzYE49HTT0GLzMXHsrbs9pIcWMUQEhBDoK6aEEi3UZxzxseJTUYs9wnc1LuXor9xZTFU5mWYE-9iSafy4C-ogVX-I2HIb9FVeRb2M3ojynmLPwYehhWzjsEISIrq0qrRJvUgWg5w4Nd-82yP_HowVld1ZgYt_89WM66lLB-nG2vdS5fWmGQjaGSNDyYWPioFN7TU-xHMMQ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
#نوستالژی
؛ یک زمانی میلان تیم نبود مجموعه از سوپر استارهایی بود که همه جام ها رو میبردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/25780" target="_blank">📅 19:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25778">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RoX4Jh0IkGo6VKuVOI3FHFMtPLR-gjH7MvU5o-Ts9ekHY0uDEH1GBWwP-ctxCxDUu8bJ2_MCSj2xqEe5lCLmgp9zw9dbNLBrYNn661sl-JzPzYgHN9Ufr-NxxB6jVTkaplvVOeLzOd2Q-T7OZnytri1g4zdIa6ptr7HAB1s8t-RayMlA4UlwOMvRoHWsWRkxZ-fqJVb6F0aTLrsRKstwyEZldRz0mINQTCxkdy9l_u__P17752-xazBGJsa94QHZaPXgGHM_sieAtyMbtIrBAFHxQUYtWkt7LGVI3CvP56aYp400HcA1tQCokzZIWe407u4j9MvRoKeq53Dvwyt78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-f8BESUnPFVEorN_FGGR_JzEtM9jIrVF75IQ8ewrlxnT5en8zo4Y_Xl0WSWxapDVNy_fNQ_kQdkUgPnk54fjygMCor9Q6ExDlC-sGuuLV84km7-EkVGDBdcokbCk-UES9Xe6oycdO3UHPVxNJ6yWGU53a0vEl3n7_S_3trsaBx7-HOVKmPkCtlB-aXsxrfymH6H2DAn9ODQ2srBl25topB0PHw4PjRNtdnYYWJpwdi3O3GJ-AtrYXSbf4nCBAJ9_U_J6jxC8_Cwgl3g1xljDFmiFAzKdcbwYcWXF9XDMAuiSy_Lj0wlDrJ9YdwOl-HLqpRz4IKy3OYLfLDagQ3c-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
👤
مدل موهای جدید مهدی قایدی ستاره ملی پوش النصر امارات؛ اماراتی‌ها رقم فروش ستاره ایرانی‌اش را 3 میلیون‌دلار اعلام کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/25778" target="_blank">📅 19:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25777">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cS5-wcs8Lib8dOEBIp4ggO4swlfMcWtMqQe8-pZA0xtTxFb-6-T7ykJQFoulY-_i9s9ARXy3xY728aNqfCAFDzOps8NQrs-3UvALDq9zaXCLL7K2hg6WdXZv_KSmPapDhWLJv7acXHEtYjsr73RNFEMyN7U1GsDe93MDzP7xdOYq5JmmV_Ph77Oit_a1gJ3xWJ4P1T4cb8GdHcqbNwvKIv7RoBIt4bRAD9LPl0dLQXyg2-DLUCCq42wajmILawZypvWvwJ4dEicIQwkPmA4ChhpnTKcC5g9fypDr7u-mJYKp6EwqLQFZdxKRUruJ4jCm62shr43jr8Vd54bTxCznSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛ جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/25777" target="_blank">📅 19:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25776">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsRkYQjdCm0RQsQjDb5vBBAYixARnoeQSfThGdseyDddwwWoyRPsd6bumQpRXb0aU4ZR-ldTClOI3qI8Ba68Ni_xU5oSayEpHfFhS2h6IvHYRvOllOL0sXJYC6fedhR8-OfFXhfzgwoFZ1PRiej65G8kkxJLIuqXYL6cfYT9VeaiA6PDKqPaz3A_CRlatA6DT_TqQ7i3JAfYP1iaK2f7mdoUNiEcG2xj6Fk7SVQLppXI1nM1960OD13S5OAAwZE4LlTPDMNQ_-EYR0ZdfZ2uScJ2mNmk-UjPzlttXzWmcZ5tl5wjcsmh6wBBRYP576nfqFqCH-kjud-3gEUe8N4G9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سانتی‌آئونا: باشگاه رئال مادرید اماده است هزینه بسیار هنگفتی برای جذب مایکل اولیسه بکنه. بایرنی‌ها به‌احتمال‌فراوان با 220 میلیون یورو موافقت خود را با فروس اولیسه خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/25776" target="_blank">📅 18:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25775">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isACpuYeNbFIh0kK1qIA9gvDWehlCkP-WZjE0XgRZEzDyDW4s_WtVjHgoAm9hq-a_5v347hIbnKSIjbkLsJhgCp20UTORSpWfMQU9b-N_rUeuKgTxvZY74SOrMStg2Z48OGlAO_pMH5taMLguN-Qb4ZaKqvPwarSoYaFTwxjvWY2I8v_xmK2IbJOJqrqBYfE2jxYU1KzPnJmCM44I5blTnjjIdAU507WTLdyGBxo-LxTvwl0ydcZQ2vNQmTyhxkw5WkABHf2HKgVlx480EzG74IaibfEXJgdSCK_2D8lBVAvLQx-ovO2kJYoKY4Blxok97kc6yvUOHd6vDjem7oo4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخبار دریافتی‌‌پرشیانا؛ احسان حاج‌ صفی قراردادش‌روبه‌مدت 1+1 فصل دیگر با سپاهان تمدید کرد و تا 38 سالگی در این تیم خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/25775" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25774">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urlZd5TZMgYSGIGTUmd_VCqwha8rxEf58HMVc0PXcMp0DlRLQMTCk2hB2E-sAoFVt9WdAn1-Io07Q-qyiQ23hW_gOWeCHWljft-Dn4ArVvt2rxYRqnLATHbZFYRjvFEh7LjmyiMwKO6_w2ZRT9k-yj7zOvOczoxsQ_15wgSKfIcjptI-bdZgYr0ZbfL4qWvaAHf8zDiLllmGqCsSR7tnmnp_xZyv6aLwxpNycEAh4LMxLxpaHFb8KLQGc4Pm-GmqofWG5_XMNAKWoF1RwVfaZnauwg7OkiCOa3WIrU60abYCjY59rF5RC4RyVnCs-cXDpXYTaXPAIDnGKt27r9wzGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#فوری؛ سانتی آئونا: مایکل اولیسه می‌خواد درهمین تابستان به رئال مادرید بره و این موضوع رو نماینده او به مدیران‌باشگاه بایرن مونیخ اطلاع داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/25774" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25773">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lvIlWO5eB03H3KzkqBZCS5fEaZLaJPcSYSguABjoz_gMPPsWSpmgbA0T-U0oHFPzOR2RRRBfm6r6C5vplxHIyWUhMa5xCSO4g5rlNYluEix84oefenBk0rhxXkQjWWQzWFUtcv_RT6AoBf5ipDF1Ex-4taWrRMqaiBMV1yx7AWSDrgTf0YazFOdb0Z8uA-qunfK2twYqPJYbBtZnzotfSUDRz90gbR0__4hDgXIlJHXX_21VpOzTjtNwd3g9KHQ49JvKTfdwX9cV6Xre6H0Jb6Dmr4sdCQ3SbHl8p0AIsYQfPYxmRWuy5C-zcCTlCYp_nYx-Rk_qssg5v0cKTXDqmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوووق جذاااااب
انگلیس
و
آرژانتین
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🌐
دانلود مستقیم اپلیکیشن اندروید
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای، مطمئن و درکلاس‌جهانی پیشبینی کنید!
برای ورود بسایت‌فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25773" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25772">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvZsLVeSkpxrnPe4168BmNhxlIFksHreVTxvTWdRTWXOI_nEehNYZu07GDKGlTQIYOeY01NRMLCE70A3Kd6LWN8qeG8x91-OHkViM9k31VL7b_jxnvlebGbnq52v_AZNxfmOQvNzZUv0qNygbpRcB6gdfED-2P2E0P-miUtTeaygUMlLNSU7w_3oP1Ga7rZTiODJDWpHXBjTM-FytBjL2EbCQ8z-5DFui1W0iIA1XvtcMCRNrSc-vArZiwdYHJTUihrKCdoafq6uSZvlrIXYyUok94XcimmZsdngzVzdRDzUgHSUlVMy5KrupVu3BJwprJttF4pVgS1Vxx1jOpgHKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
فابریس هاوکینز: مایکل اولیسه پس از جام جهانی دربارهٔ آینده‌اش بابایرن‌مونیخ گفت‌وگو خواهد کرد. اگر آفری‌بالای ۲۰۰ میلیون یورو برای اولیسه ارائه شود ردکردن آن برای بایرنی‌ها سخت خواهد بود. پرز رویای حضور اولیسه در رئال مادرید را در سر دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25772" target="_blank">📅 18:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25771">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ayabq7mACFTNWoXuw-ia_Rv7QgIA_bbOBf3iRRy3n65EvnDC2OPdt46LBpqwu_gLjjVbdW9jv9qHN9gvuQ3HBb_Xh2gXKtEm1vVfJ4OkqwUYLUCx5re3b2wdabV696-nKyPSg4wYvtpOj8S8d5HlieJbPkbT6F84PSLYo4agX-IDyfafSgHw8SYhqAExe0GlZXCkaQSMwuG47iFL4qRbZbpNOT0UfXto5t-8n_WXNgRLn69tuaSKVnSk-c9ph55HniKggQtzSL976IiWU7GsAzNbzJgEhsjzF2RhdhKzkawOMAZLc_QryJEKfdZ9_r8BOW-5PtwhbbUiWSPfmWDDHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالی استقلال پنجره‌اش بسته و دوفوق ستاره فصل قبل‌خود یعنی یاسرآسانی و منیر الحدادی رو از دست داد که فصل آینده نماینده ایران در لیگ نخبگان آسیا خواهد بود. کار بختیاری زاده سخت بود سخت تر هم شد. ممکنه حتی بختیاری زاده استعفا بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25771" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25770">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qM9YqYLXkaElqMTmpsqVh_cka2oGjO9Snwew6Pl8y5HVpyfYcR7L82J01YryHVKQvBmffjYacXgXpA_VJXb3UZH8Nn6O9Zc5V3rUQ4_SVRN-Uxzn6uSnIrd1dcy76cJQOhNL3jlFrP7FYlgDiQDNK7cjpkFUEBUOE52TDloNNKSkjV2_B01P343ffOFsLdNLN4rZzKnXm_xkiCcWmAAw9R5KwiQDE7kqiFhuFCirbKoToZBzEXirX02d6Yu6US9UrrKxMtvLCZXkn8GmKMfMUemEFlf_u3usdzHD_4PsLE1-ThqMch53zvDxGPSgbYFEBnhFFxgHHNJxzwqipa4TKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب‌بعداز بازی فرانسه و اسپانیا درنیمه نهایی جام جهانی؛ خونه یامال تو بارسلون مورد حمله قرار گرفته. دزدهاداشتن‌از دیوار بالا میرفتن که نیروهای امنیتی بارسلون متوجه‌شدن‌وجلو دزدی‌رو گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25770" target="_blank">📅 17:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25769">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtVxvLonZIV1GrpWAetpdY59LI8F_hV7Zg3NQl_ALolPTggS2R-S_kQSOmJFi_6VuN2Gi2Z_jmx6zM4hWyksR3BFfF72L7qitRl1y5lysj-fFXL77autWfiavHlqk2oLTs4Vk2byeK_P_CYiQucVnYRwoY29WI0lWXFMyYucO8YHt14MAYmU2MiQfyxjp3kVvZmPqTm8jHqQAp7RsHnnMZSi9jWtlfYt8uKdgPmL71y3WSmxe-9aiizWB7KXB3WGHnnKGDCM3p8TCXQJoILmf3vCxlIxnksHiPRKRv-UGYYH2XQa7d2aIfHGT3E8XexZPmmYXCFfPc77MV36B2F28Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25769" target="_blank">📅 17:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25768">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEK6Zkbd32dcADu4f2S3R0POHpIcgTu2aHiv0O02Sc9jFtFfG8kSRKNMy7OxxHeRBQJ4uT3-qmf_I9eVZ6oreESiWJB5ahmYeE-uoQ4QY04QbWwxPM2vVuFYVk1cDsSuydvUA2U485XFWqanXGdvER83G4cq8jzTOvzN4XB_JX-EbRyhlQs-5Dfyn9M3RrbH1vMiS4wgnqkj29Bb1QA3Cp7hWLLpgTEvPNsFrjrOQsGGvSs2X9gmQ6BZiV2_IM9ECkGwdCcjI9khGm1bp7q8-vRRVdWZ11v3B1KWYfuEbTgociaUXKbP-4-H2rrLYhIQiE3njl7f5rIdLph59QpfZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های بلژیکی مدعی شدند که جرمی دوکو ستاره تیم ملی این کشور دیدار فرداشب مقابل تیم ایران در هفته دوم جام جهانی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/25768" target="_blank">📅 16:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25767">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dq_Ta0GdY-X7eXcci6-kFo7h88w_eAXREQnjODnp9P-3POIcCHQj1yd3qRme5y9oOy9h48GgQb3MSnrtkBf6LMHRuO5vjuuyBjs9yS9-lYMUCXLRQOzGtg-nvRI7jiH3PbeO2_EB5kheppA1dLc_fHmQxTbvI9LVQtlOdy47Li_UwGVywn_Avwj4anyHeUS2Cy23FjGWEmrjWuAAz0mKKIsgH-c3VbfSws80RbZ2VqbrFgaN5djvnk_HrC_ACYiWYr_pXK-1Eq5sdxE6dS7PCFEXTgrC2yfrQUUCNnlmpyyfTNzCiCfIhU0YUYC5SrxudccgCUz4zeCHBvbaw_xyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری:
باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25767" target="_blank">📅 16:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25765">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb986dc0f7.mp4?token=U87LHwnNizeuU5hNCWaP9GyTi5Qme0xVb3mmeDMVei2YtGSfRY1HUaMbFwtSOcveBJEzqHBPBCcMg8RL_hGcE37tYAiTy2uDCUeNXBmqHCLEcfKZ-IKsL9L6xl9m3CGO7E7llDMJMLhR5p5RupsaLMa6-DnJsuwcLxma3y295B-FHBNIEP9a5TbtTZNR4MT2v1I5ecao-mxdzdr1JQCk67MZXc6MM9DwzUrwSlkGek6_Y3lShQFpqO8vaxOckCRqmiSvO9llRKyH76M-ssmFVBK6Ujg-vynwYUCmOAqTFaIdcGERddUKEJIV_KqBkGMnpXhNqSIXUxG3sxhAbvEFAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb986dc0f7.mp4?token=U87LHwnNizeuU5hNCWaP9GyTi5Qme0xVb3mmeDMVei2YtGSfRY1HUaMbFwtSOcveBJEzqHBPBCcMg8RL_hGcE37tYAiTy2uDCUeNXBmqHCLEcfKZ-IKsL9L6xl9m3CGO7E7llDMJMLhR5p5RupsaLMa6-DnJsuwcLxma3y295B-FHBNIEP9a5TbtTZNR4MT2v1I5ecao-mxdzdr1JQCk67MZXc6MM9DwzUrwSlkGek6_Y3lShQFpqO8vaxOckCRqmiSvO9llRKyH76M-ssmFVBK6Ujg-vynwYUCmOAqTFaIdcGERddUKEJIV_KqBkGMnpXhNqSIXUxG3sxhAbvEFAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25765" target="_blank">📅 16:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25764">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K51F02mwc8Z_xeej-_UgelMRlRZqDQSDGjsNE_lrYoLEW_wa1asZ_INk_HgGtUE7ucN78hvWyTpgugfZrOOkNF4artP338Eaveiu-fqbTkp9YR81T8a6njjN1RjrjEQkQcVDxJE1-Rvz-bh0Lc0uAzhudD7UPKOuJTJf9h07RRGy88vwBsKFWiB-YXOd5NSRh_vGJ2Bsu_F9Ik-X_7K9PYsht8KSVSDkmCgYqmympGV6SsSfJsuk9HCe8JArU2soAXAiIobPvA_o-u2e6QipiiT4KhFc2cU4xKdnqKVG-UbQFARB2jcA5tNK-ChXZirw9E7yFzf-K7iruq1NuRYIOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛ فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25764" target="_blank">📅 16:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25763">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2oDBZNv1u87a75hTpkYRxbKGkllMAgNPNmusctW4syyysF4jvIdgjshlr1XLTJx1Sm_3x9hYrLpu_IRIxN1NPqLJZGu5kR671VfEpP8LFLFM2zixWqscPWfbjWCcea5B5XkDWw37Ds35mkTighA2wSwlL-JK4BlgWaTVWd9do1oI-wyj89bRVf9gUCSVFOu7FoU8m95ry4rIVi-hWjfJNAjD_SlrGgmJGb9PKy4T4F1bhKOoiUs7beHp5MiMaozN_g-VHA6QcIH9dWsgowwgkaTVeTsNZs_V1U4XyHPZOae8KJzC4fG5xhulpnXYEuxI8N0bCgkISAFnkyLeMrgbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/persiana_Soccer/25763" target="_blank">📅 15:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25762">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgLiFfxNPsvDFwqpU1em7GKwgWKmcVkFDcPTZh0itGsOTs11UQfTnCqxgcQPgMigCQ6Lx7EPYnqyX9Pir4aBh6tbELDimjYJucxspOe6WnVCL_PJhsdGSnElfEmblCyNfF9UodTOR49Hz87Q6J0Ai2fZZcNQ62MEXoHjeDKZPTDthIl04k33o_0I_xgbXN_1vJaoJ3pGG2cvcqFFBvXTV9ui3AfECeHvZLskowDE3J-3MlRWJE2AKTinCLgy8y08Xzdi4lrSNMF4OatZfdZEqvBV0GwgAqG1-1JFZrYDy2zc20cmw-m6aEsRuTqty9u8dJMHhcvfoQTemb8anB2-aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/persiana_Soccer/25762" target="_blank">📅 15:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25761">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=qC6M1S5EXV98JNhuK878Rx9t1OBkY0kp4Tovfm4fCkDkNs4bB4LHYa0rPzmaP26anEyFt-fMYcIvJsCmSNKZCMUAvbTMWj4ELeS6OnTQdp02SB-och_5XVYK2-6ZkEHPiDyJy8LBD8z-cj-fPb7ZiSaGKFCvarTmLNHyr1ZW89jgCJlpnQMhgtOL8d1oDGZLT_e-_VT59Ded2Yxbc49FofPzEc_XCtPtM93CJkDWTRWA-0-wS0-dNknRspjs19JDp8j8JyQcW2clBwzVjiu5gkOIyrsPZMLrHJp58BQsJ4sbyaByabXiT4YQ2c1iNSVqgHtPNFwRfS86Y0UlmkzxLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=qC6M1S5EXV98JNhuK878Rx9t1OBkY0kp4Tovfm4fCkDkNs4bB4LHYa0rPzmaP26anEyFt-fMYcIvJsCmSNKZCMUAvbTMWj4ELeS6OnTQdp02SB-och_5XVYK2-6ZkEHPiDyJy8LBD8z-cj-fPb7ZiSaGKFCvarTmLNHyr1ZW89jgCJlpnQMhgtOL8d1oDGZLT_e-_VT59Ded2Yxbc49FofPzEc_XCtPtM93CJkDWTRWA-0-wS0-dNknRspjs19JDp8j8JyQcW2clBwzVjiu5gkOIyrsPZMLrHJp58BQsJ4sbyaByabXiT4YQ2c1iNSVqgHtPNFwRfS86Y0UlmkzxLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
حماسه‌ای دیگر از جواد خیابانی در ویژه برنامه دیشب جام‌جهانی؛ از خداداد سوال میپرسه نمیزاره حرفش تموم بشه دوباره یه سوال دیگه میپرسه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/persiana_Soccer/25761" target="_blank">📅 15:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25760">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMmek5x1ahWyLjnmHYz6zYDGlz_h1eCw8Sh59NWBqeXqXxf1O1ouYY8IkroLHHqMNbraJ4aDhaBNSQ2ObscDiGdtTsW7xP4i9I4Ge7Qrcp0SwM1J0SrMg_rMhSg3aXcfcVKDRfpLmIO7C4lz1UVm2XgH5vgHMCZJEJHk-yViZdm4Mml2Y3gAKyhhzZUZnKFWiXCWtWTDkfraLXjFhW0g_RzYm77CZmS8kvr-izY37EQceSrqz3Mes8V3Lz-a7HhhrSAGlPyS0HRdJRS8Y4PI0VsmFsZZH1Qpk-huKhFj0f-NzSd8GP_UGQIlsLPhSP8YWStaS1Aue8f2a5JO7-xyNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#نقل‌انتقالات
|اسپورت:
سران اتلتیکو بدنبال جذب رونالد آرائوخو مدافع 27 ساله بارسلونا هستند. مذاکرات باشگاه با نماینده آرائوخو آغاز شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25760" target="_blank">📅 15:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25759">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSISFbQpxyYkarBuhJ9k_gK0Y9xA-trOgdhAQMROS3x5_lzxiAWPPHuzGgbv_aAvookmmDUvlWhchdpIzTl8OKPaLi-zNf670EhjfqNwuNUWJr-A9HWogu76Zfm2G98UzWj7X7D3_2tLhNPW7TTkYgAS_WFInsXUmFF1qL6J5e7i8sH5cb97FcQrzmTa1Q4YIxn_6AyRMevaePR7Fs9AD_HS-IBKy0G4fKjc5BhiFYve7Fwt_rhIj6sI56uzENEDHNzC0uJPuPVNyJ3l8UEMcK7Uejo8Fk-0pLGSlGnu9w0QtfwyqqCHtMu6370Dv6fTT6G9Xcgg9BijF32d0u0KPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25759" target="_blank">📅 15:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25757">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfRuLGO0JeZnLBQxkHU2DBhHn7U4HM5CjctDenbT-HQJ_4t3NaUle7OHYoYY14QEGsHPg8lKKTzbje9g9RtaK1TnhJLIyWwnn4WktU3uVLo49hUoy_8Bf5eKv873uqPQQ3Xdu8sHLhJvDIJY_xT3aOR9wUMyH5MxrKu6qZCRUQvjdSbIxvMDi5HQfRCbmdp7ytQCiKvhwciap1qXhPeCrlDtiZfq4fR3uUeuQg36cPz7zo3gjIxZRo7lTvsa8wMBpYuA_9WGPYqMZwiLI24kN9wqKqt9v5iMZoO7UzFaEDIx-dAb0FFVtRrKV17j9oHJVKSgEzSUT0PSj_XQmqUn1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق‌ پیگیری‌ های‌ ما از ایجنت ستاره‌ سابق استقلال؛ قرارداد فصل‌ آینده یاسر آسانی 1.2 میلیون‌‌دلاربوده که فوق‌ستاره آبی‌پوشان برای تمدید قراردادش1.5میلیون‌دلار درخواست‌کرده که مدیران استقلال با این درخواست مخالفت کردند و به مدیر برنامه‌ های او اعلام…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25757" target="_blank">📅 15:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25756">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYCCDeCYFyYFSdXBIuZJJq6iNjHNI6c_SPU0uBITIVIJmAv4wyngsrHsP_bJcJAlwI5DomkqYORiOc2W6SawKeCJvvOdcoqO_wTsR--bKfYOiSJf1_pEgggzBqeR_SnpGUu9KeI9RiG21bXt2ljw3dPDJ6I1t9O78c3N6ZxrmuPxydUxQfUXd1X2v3y7KCF-X2U7TWvtq9PPfAL0sixy4FMfIRQRwW1p4MlI2z90AytTXhWHQykdvTPwP12EWqrq0vZW_sWn4ZpSlMlfG20OogO5MJMMt9lX_m8tfn6e5n3AvJnyOXE8Q_WsU_alXTbi-7jtS2HOXIrD2vzFOs-xvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نیمکت‌های جام‌جهانی 2026
؛ چه کسی ماند و چه کسی‌رفت؟ از 48تیم‌حاضر درجام جهانی 2026 برخی سرمربیان همچنان هدایت تیم‌های خود را بر عهده دارند و برخی هم از سمت خود کنار رفته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25756" target="_blank">📅 14:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25755">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QebI9MWA_hCAdH2KuJaSm-HNGwafsSM_gjnAxN3nsE19jR67XlJItMi1skvQQ7wLAzDNgtB7enxSqq8OxMB1_Qb72Oj4Tg-Z4yHf8fK5Dsmwd-bff21XxFQayfYPDkZa-OyKvpI4kXoNAy409AdbcxugsjjTB7vrF13FP9oB_gw5_NSgk2gcqZDcqpsglbiCU1Pg6TBQzehRrLP3gEKC64a0Cyx1IhHFY-ablNsiMKxXF3UQik2evl5p5htgzHhu_wW5Z8WhUCrKGR4419S79Vh7FHz8aolJKpKfpK1yjkKGA-II2TRbSxAgPCw8nnN-J7tennRo91GzF8-l4wrBaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
همانطور که دیشبم گفتیم؛ سهراب بختیاری زاده قصد داره درصورتیکه تا یک‌هفته اینده وضعیت استقلال سر و سامان نکند از هدایت این تیم استعفا بدهد و این موضوع رو به علی تاجرنیا اعلام کرده. سهراب بختیاری زاده به تاجرنیا گفته با این وضعیت اسفناک آبی‌ها از آسیا استعفا…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25755" target="_blank">📅 14:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25754">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOqFy1edCgLykBW3voRn9QXrLSqr2Ul7HhS7zaBZIb2k8QRdgmd6m8sYcJVtpIWu99uXEhI3Ccjawvl7dBt4JKSJD19oiaFxX-Bev7JqTgsYi8cA3SXf97M1klxoQF2_kXNxvhXHGFpSWRH2nEZxMW7BIdm1_XRj1QhVLsmhv9VKh_HQoyyne7a33DPuTm-bQF7a7VKeTTmIF4Vv5zkUut-B7BoTfmde5lzpvAohYxcpZH9k6dOmV3ytu_bFF2X1GuvHZKpWb4wgMIOKZsJwXrAtPv3sypty4ZLLCat-fssOu8IklE2tL7CY1G0kkrzp7cSgsdDY0N5ZMv_DZ6wXIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خبرنگارمطرح‌باشگاه شاختار دونتسک پیش بینی کرده آرژانتین میره فینال و اسپانیا قهرمان میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25754" target="_blank">📅 13:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25753">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lriwMMxgoY1zTbKzjgloLrtVUMLO4q8JNsMw-mDjoKPi3f0hP53uuBLkeo1flqDGvkDbIKDe9aw80Fkk-5Glb0nmtallgFh6GN_bXbuLcUu7m3zbyCWiNKkGO2-jCI3r8WkObwwKS3A4olRU1WBH4pIJO9x-KT598GmdcXXO_G95eMgjBIQm5HuKRImpZ6QexqCPOhXcCNxmuPMy8xkxIEJnJQKxKmaBZRaSMXEfLsf1I4YpMWA96MrE4Mt_PVLH8pY99Al3ZR5VbXhLFKKclxm7nBCb4tS6JgAuGolITkkvE1ReUFFBe088c6_RJYL_TUhG9MXr9T77gSLWtZZugQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممکنه حتی بختیاری زاده استعفا بدهد.</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25753" target="_blank">📅 13:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25751">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgfEoj_R7JpJ9_3s-kVmZI2ewJRZ4u6t2rj-pG6CScoUXVzpGtb08Ii1WqOrPvj7D44EcmtUwSwifl71Ei8PRNS_XgRvzRYae3k1qm-JmOnzZHpJlbM_rOKtVLBMwNB90Tc2VSMQMwo5zaYwVpIy7JVubqpF3TfqTaPYuLLlyhnUFI9raovmc7OVKwDVQ0TMJjmkMKfwrWvCgoufb26IfUmJstgorPhK00aNQTMvD2b7qNRfSzn9YgmBVBgXu-_a3DvqAo9zoROA_M5nhHBiVIoEHpcB0U4jrTet0RbcoKeSPG2-sLV8egTVjmtEjRXAh6nKwlHHTNPXc2t9zL5W6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
کمیته استیناف حکم خود را درباره پرونده باشگاه پرسپولیس و علیرضا بیرانوند اعلام کرده که باشگاه‌پرسپولیس موظف‌شد که مبلغ یک میلیارد و دویست میلیون به گلر سابق خود پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25751" target="_blank">📅 13:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25750">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K064-hpG3XgZ1IUNnfcfh-t6U4UGpHfOOf9Llpm003OalciA8tWkxaw1MyhAQ9U_zJrsrPAl3b_7F-BfcFSYS32GCr_jP2EqRMVOv8ahk7a6jdVKSh_A5vf7hd8TEuH5vueIG3HgLpuMAeuynvDZVuj_CBBmywWHQ1tFiVoxF0sJXVmI0Dr3Gd8Mr3ay4eYoULCUCYHl6fgfBCs_-otrB4h3D0a7swhhhknI3bjq-Je41XVxmOm2vNd2RYH6NkyLx4heBrKxtUap0q27ta4WsXkD5aH_D1Z_10OfSCRB1pzv5pQoLfJeu9JBQD568Ps3vmW2Q8Hs_7FlWjMBvlB0fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25750" target="_blank">📅 12:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25749">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=MDO19MFwpmEWE0oa4LcEF6-p8O8hJm3qWlbZq6CQsYI-ouc4Gspi61uUyjk58QKAwEsSaNYX5jqTlh-OI2T5meZuPXDt-HHMoX8hRpnxEpxYVIBam1Abz8bBsOjTUq0Le5m0EPAaG4eYl8Zmx4FhHA79emg0ZzbghzBhFAhZ3IJtzUA3V68U-miJ8cM9RO2f62zwT4Kbx5sHGnW1bwsnadnQesdOlC2320WSu1yV1ZJgb0tg8J3CFtmeadsw4kj-nyq5nyXVSbisPqDj3IQ0pe48-cGnXbnI5y0sK9HoZUnZXWceY8QW0dpnf7gegWcl7vqKeYRXhaBBLEouHmacpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=MDO19MFwpmEWE0oa4LcEF6-p8O8hJm3qWlbZq6CQsYI-ouc4Gspi61uUyjk58QKAwEsSaNYX5jqTlh-OI2T5meZuPXDt-HHMoX8hRpnxEpxYVIBam1Abz8bBsOjTUq0Le5m0EPAaG4eYl8Zmx4FhHA79emg0ZzbghzBhFAhZ3IJtzUA3V68U-miJ8cM9RO2f62zwT4Kbx5sHGnW1bwsnadnQesdOlC2320WSu1yV1ZJgb0tg8J3CFtmeadsw4kj-nyq5nyXVSbisPqDj3IQ0pe48-cGnXbnI5y0sK9HoZUnZXWceY8QW0dpnf7gegWcl7vqKeYRXhaBBLEouHmacpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25749" target="_blank">📅 12:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25748">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlwqncwfG1UJrky0_WFoJN96cGTTCWbedZMoii9XNpsXUwLqymwItGvnMf4kUInBTWiC767FufJBTEdnDv8cV6vchS1qjpcNajtyb_XrkTbcIWrU0AOzLRqIiEcwW4Dpsb74k-jggZtNu6k8maKUTxhS9DXbaGKKFDBS2N9S-ZEu9PpeykXsIp3tteYhS2qLFhVLaw4X7TzefKFNMIPOstXsFqQXO0wNkcoLf_y3IDCLPHVnYkr-Vu9kYTAdSVdFYK1U4LBKCVLZn7A42f1K7WAhYygfS5HH2fmSPdiK-THz_NfQ0ONvwfY3dBVRfS-JsXAB8CxKm3Ngre_FLL5Yzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران استقلال: آسانی برای ماندن مبلغ جدیدی میخواست که مابااین‌موضوع مخالفت کردیم و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25748" target="_blank">📅 12:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25747">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/funk4VwP_hP7b53Yodu9s7kLpPQgZano6BBRbO4N0AedgtQUBLehpBB2ug9j1T0uokXNGrMNJxSY5L63UIkZehaJB-th6mq1kMNmYIRS5AsC0a3dHwHZSdCbcFIzoFuvaGN0_1SVxH3zKS6VwvQb5-pZEkIyi69pVGA5n-nldhLI8BE_TniPxiOrWVa_4KrxHSRAIaVi0UUNREg3X4R9PvuqGHJesEkNDkOstMqKguc_N5PWmETty4wcsPIGF-yqwHDeKIuNFNw2F45Hic-nrapFbaRcL9hB7m7TJxIR-YN1w68EkQWFCa_5zHIYjgiupfotOZoD5iCghRY1ZwR_HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25747" target="_blank">📅 11:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25746">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtMuiqbPndku9qTspn71lBv3KYFuLBDwCc72XCg0t-njDFL7Wksgne74hsgVrhmNOboL8876NbUF9OeyOhmH49WKdrgBuRorBjX1pr6nuds9xjf7WTJcuh3Lppsug7WlExt_jErBDFWV-2zWl3Fz69Ed9O0tTf6z7eWNOh2Q88gFPek_cpCiAGLS5YBQCqNuv0nbf_5x9tZLfESykb7rzDj2qWd09dlz4H8HEwprJWCm9BlM28RcNqb0fJvMFBv8flL0cpQz3AtreyocMLUNKTNzr2sHeLKnhUcqO-293tAF7jFY1MjIIstdYnb5aqFu9m6Ct3Ryjp16bSnc9zTyMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دیدار جذاب و تماشایی شب گذشته دوتیم فرانسه
🆚
اسپانیا در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25746" target="_blank">📅 11:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25745">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3HwIHiBM6_4BhtbpSRxrmuc3_XiCQJHo9c1XeXEhjiJsrK44-HD0ILqOu6UksXrJpX2kEEIQYeEFBKk0wrA-vru1YjMPwMeUiYsFwsh5Gxb3LHU_ekSZxU_tDzMGd6twDE-Xj5nlwRPDfdYEqRIccIEsxlywJjajFGFUn-pG9TB84UBdhdG84QvhsRUHrXLn85Xdf4tbKaL6LMbhI4BC81xZvvqASwzrU2x3GKbPb0ObmfdZ6Bme78ZJksyaDLxgFadOIPJY46wPtZylNM3-rIaVJ2V69WwXesti3aUTs8tyx5UwzH5BVmLoAdvRraniY9N-DmUBLpr6omoINFZLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیشب‌مدیربرنامه‌های آسانی به ما گفت که‌باشگاه استقلال ریالی به آسانی نداده و به او گفته که‌میتونه بره قراردادش روفسخ کنه ولی اگه بعنوان اولین‌رسانه این‌خبر رومیزدیم قطعا هجمه‌های زیادی به‌ما وارد میشد پس صبر کردیم همه بزنند بعد ما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25745" target="_blank">📅 11:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25744">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqDM8uOkuz1AsamMzkeT0vG1iTg9Rt9nZArRU1G9gw5scxZdjJbd8i05Pxq0HgnagSJvuNWuU6oUyuvypqQ6d7rMsgVzQ5gIi4szJcsecUJlaH5M2aGeZhij3gFJGzFwwhuQ7JzBG97nk74OEQrbDJZOI3D6_uBXJMN3z-SHkFVm5DZb_L3s2MS69P2_lQoCpxrUyl9EDwd208cX3YX1Ip8UTPXemPplME3mE1dCwzKHBq709AaBpk-L3AKGwg9n0LICKRZP3KMqONC3T4Ic7H12Ea04JoAcbJvUzBOMfTyr2RhUcW-E8-0ysZJ5YGbtKu1z8iBH5T-Ee_Ej5XaQZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ پیشنهادباشگاه‌سپاهان به امید عالیشاه دو ساله به ارزش95میلیاردتومان است که به احتمال زیاد به آن پاسخ مثبت خواهد داد و بزودی با حضور در باشگاه سپاهان قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25744" target="_blank">📅 11:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25743">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=rR4aSzWwls031XVUyRZCtMzW-Y5j5wuoIUDkKqNyAy9BsSOcUJruP8G8uSz24ini55Ilho2D-_Z8uI4fu5MHDDfCNJlKgJACyVcwRhJThiy2LBTs3FCegeRNcI64oOKH_giTUQpPjhK5xAXDK3Y5qnQwYorLhC2CX2kYDIV2L6tFyNeJL-WQJIQ9HcUO_dLLf3Coi46lfHI7t1rgyhwoMUTyEo_Lm19_DaCaoSvGfXEM1IFvvuXY5_Ve2bKsic91karI4LpGYprDnEoVYmGuqwMrHTHaGXWk3ugOfG8xBLvnjnLDeVqcAxl0YWeCUZnudSO5ZuMwBqFl8wA79JUcRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=rR4aSzWwls031XVUyRZCtMzW-Y5j5wuoIUDkKqNyAy9BsSOcUJruP8G8uSz24ini55Ilho2D-_Z8uI4fu5MHDDfCNJlKgJACyVcwRhJThiy2LBTs3FCegeRNcI64oOKH_giTUQpPjhK5xAXDK3Y5qnQwYorLhC2CX2kYDIV2L6tFyNeJL-WQJIQ9HcUO_dLLf3Coi46lfHI7t1rgyhwoMUTyEo_Lm19_DaCaoSvGfXEM1IFvvuXY5_Ve2bKsic91karI4LpGYprDnEoVYmGuqwMrHTHaGXWk3ugOfG8xBLvnjnLDeVqcAxl0YWeCUZnudSO5ZuMwBqFl8wA79JUcRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25743" target="_blank">📅 10:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25742">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25742" target="_blank">📅 10:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25741">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILZ_FZIN0S3t8jmHorEpz2wJoxWFVKuHyNwVylYTLGmoS6XW9cfW33pBHzIXqYleMsAdt3sKCMSvfy9A3_6kSK1aES71tkstPRuDE9U07GhvG5wM3HVzWvs43lNYliWEePA81IEFPJX1JF9AkNfPeenoPYnqH9RjuUVYxvptlUzL7Dz82LtsP-rqzBXE1O0yFonBSjkHiu2MOKe5KNkUd-R7xSXtLssNBzyCfTIvilQ6J0vPKngO66SSJn1BssqoAsgP2PAa8WI9aViauWXGS8EIvxPo-OQAe48jIF0dFc87aGjjXd9Lelw8scjnPvoOhfrne7Hho0Ym1lzYBjdi7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25741" target="_blank">📅 10:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25739">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCpCo2cFpoEV8sIn1dklRsqelPNsL65o_q86z8AItig12LfzKcpFUzUbm72NhLhnt3md3jiKxtqI2MNHR7eb81q5YhYR6W8lgP5JM9jduN1SkI8Doe9-BjWm1rOkUPYbAgpngMw1cX61ZD5XeGxoQdOCTjd6_1O1hzRzQBRrTeySQbyIYeZM256cZ6qlD11EcWZpVjEbDGjMnQIZEP31UcBxO9382bkJLJN_zu846xDGPxb2Njk62rHbeOu2HtxISKifqL4BR_7bblfzIYM-IzcudmMIK2NyGehKW-HqES5XipkrCzWmky9cKnTM5h7ajtVdsb2SRYx96iajcvI2KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم؛ سال 2016 دقیقا در چنین روزی؛ باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25739" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25738">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=Ln14kOA27L8q1Teki-4nqlggdbKr5opwS_mvr9K4g_5Fh3oREm7P5VwybBeQU8nfYIvJFjubnT3sEK6_a3XRGr-9-29fdO9tdznvrvmLxAzZnBKeZYNDZ_O60iy88Kq1QDx2NRFLdfuLHDCnSeACZ4QbcTmiOlncAULwEqtb-L3mqOBfrEY37sGXHF3l5NaJdvTPZIS9WZ_ZPXLwFh6v0wlvwuzHxGW2JePuUAgGh7i-A2tvpJWHlSPT-VbDJPlWfaRDUMt72A8EOHd2xA0HDd8RlrkyPGovCcqz31MHr_ps53Q8UnaFO_mzmGmbFwk6hv3Nhfpivxixc5rxdCW8LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=Ln14kOA27L8q1Teki-4nqlggdbKr5opwS_mvr9K4g_5Fh3oREm7P5VwybBeQU8nfYIvJFjubnT3sEK6_a3XRGr-9-29fdO9tdznvrvmLxAzZnBKeZYNDZ_O60iy88Kq1QDx2NRFLdfuLHDCnSeACZ4QbcTmiOlncAULwEqtb-L3mqOBfrEY37sGXHF3l5NaJdvTPZIS9WZ_ZPXLwFh6v0wlvwuzHxGW2JePuUAgGh7i-A2tvpJWHlSPT-VbDJPlWfaRDUMt72A8EOHd2xA0HDd8RlrkyPGovCcqz31MHr_ps53Q8UnaFO_mzmGmbFwk6hv3Nhfpivxixc5rxdCW8LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو لو رفته‌از اعصبانیت‌شدیددیکتاتور کیلیان امباپه در رختکن فرانسه بعد از دیدار برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25738" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25737">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bNGzo4x27ErOjxB5_9HE7J5YbFf48KszLx6KEKRj6J99wf0M9uac5DuDTaw-i5SPTUX9knVRRRYbiOahTOpdrvDlw8k-VqRLfdmx9Wen7wgYQ_i0q6bLr2kdRiRsxWOYL8A7P6E-LcgQAloZoATyjZge2MDhwuVyfBGQ-wj-4a6EVPxHjsUFFjpReBP80eua6GMdGMcYcekVaAFLjwdofdkBYbiDZ2bXpSgvyyCU1wyZaJQYDkAJaDRMUVY2vZ__7bxrIpYXaNdG2DFFYEEaxdy_D2XTWbRHC2wdIYG8BgeA_IezP5QPiWpCulaV4S-PF5N4dxd0KN93yy6JHV1qZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک‌کنم‌اگه‌هرشب‌با ۱۰۰ هزار تومن میومدین چنل بت ماشبی بالای ۲ میلیون‌سودکرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25737" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25736">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=JDM2fDvzj9nuYRDYXrLB34Wmk_MElWfeCn1GcrkQvDzLiPBHqxvpTLm35rGgc7kV2ef_ujsEIRK7MyfLQIj0O9VGp4zdCNM-sdsWbPUQbwMUM8ud9inLzx8d5yUGEIimbvxzsm866m1dzeQvtKRtvfFcnyty3MiOoTQi030ufHIrStlzpo1-i0btvnLBEmBEljmNZzm5ZIGtUudLv341moUvTwsEqBqo9P_GFauUmRx4Y5zPZ8kho0ZMiyfGcvBjMq5P1Ef6YWfvGZwWUdzaLjdOoE1v_47Ncl6pZTwZaNzY7crwugd_b6CgM9YhssIgjCKp3qQaKIiSB7xa6YQaXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=JDM2fDvzj9nuYRDYXrLB34Wmk_MElWfeCn1GcrkQvDzLiPBHqxvpTLm35rGgc7kV2ef_ujsEIRK7MyfLQIj0O9VGp4zdCNM-sdsWbPUQbwMUM8ud9inLzx8d5yUGEIimbvxzsm866m1dzeQvtKRtvfFcnyty3MiOoTQi030ufHIrStlzpo1-i0btvnLBEmBEljmNZzm5ZIGtUudLv341moUvTwsEqBqo9P_GFauUmRx4Y5zPZ8kho0ZMiyfGcvBjMq5P1Ef6YWfvGZwWUdzaLjdOoE1v_47Ncl6pZTwZaNzY7crwugd_b6CgM9YhssIgjCKp3qQaKIiSB7xa6YQaXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25736" target="_blank">📅 09:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25735">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJf-3rTM1-eBBd3HQZpBcvrV0x3FCjVXUMCq_EWMZaZii62HS1e5kIRPeBLE9HnYAHE2EZkgQfkuiQfvujC9DZHqd0nXjlKjjh-pFz9HQVM7xoIbjWdkfEzzFWoYuAq2zYBhJUjZebJT6QbsdxeAfoI6zk5c_kZy_RgklGKloaTBib4NBgifdFsz46IcYnS0wudL1Zwz4zuh6hL4XKD3Bk1Ajrd5Zucw-5gvnGGALQbVHSjXTA2ugUut2WFHXItWLZDh3GBW2Bxz-Gr-pmq5XigDxA-BeVWstzs4-A9NvR32Az4xcSKHtqxq4E4LwM_GXTOfl00euIYYAt9imO2JkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25735" target="_blank">📅 09:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25734">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPpazo1cQeMYskiHcM-e3iYswZDff5v5WlCzyNZGbp-z3CDznBSjgiri97m8VOLo_0VP-wQc4TWFYlsFLdOvMXLIwZOHwlFOxEZCdJzA9skTOf592G6PD5tuG2uQ8AOP4XD7ZhBoHVSqMJi32a-5xZmPcAp2yySd6a0gchSyiVPKud8ktTj5e37cXxYzagZfbnQK1z5Qn-AEeyp8g4hk5ZPGVnD6euBi7FjM0KyiKyHJTaNnud_Xs6wrhsG2BKpLiRtVZgGVjtJMNcIBAmbvFc57UNgGQ6HMdjCe35fj6LJj6bgC3-qnIsmD_OQCTkW6GzW4y2pWDiFPv9CEKmzTZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گویا فوق‌ستاره‌انگلیسی‌ها شارژشده؛ دوس دختر جود بلینگهام: فردا یک‌ورژن‌جدید و فوق العاده ازبلینگهام مقابل آرژانتین خواهید دید. مطمئن هستم جود میتونه انگلیس رو به فینال جام جهانی ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25734" target="_blank">📅 09:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25733">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=RkBstdNbhKU2TQMbEXQ4PaN8WnzUG2ANEPHZ4NOpITLb2h0emWNqQF54n_itAi47bzlS7PP1AanyatyWM1UMU0bdqv0KkRrYrfo4RQiOzQMqKIvwxO_Ix1eGksgzmdXzh72J3C8ZilFBacEeDvBZP7S8f7stmLj5G13nM5XLLqavZVJqJrH14_tZPEZCl4ZGT4unauKJhbWq3M1dnH_CI4Gd1lJRFj5Axzo1d5t1OnfAYf7vX_Orb6ulFQ3EYPmZGTPAyapIFIh5ijK9kaA4HovuvtGdSLQsTe8LSBMBFHF1U6jfvGKJC0asb4-oo66-p9UMGSaclsBP6upJhgWGrJi2ek8TW4xFGvi0weyL8ZtjbkVGJ2EU_J2s2kRNs1GGv8jM-n91iuWHj6C7YcfCj7WGlz7NYWXsRSoj41dxWtxR1F3-KEdH1QMbYkBIj7I8FuAbcFNqshZ30k6oZJT2HL9Y0NUqjs7rfCl-jLhgaATsITRd6U1PxGZUivuZaSLlOJ0wRL3HTsatx-aJooTVpaTfWPe4T9_pxYCwdAJNy2ZPnZRcaJxi3Utx5fB2XuvNk74e5XjcHVNfGWMdi_uRJc2rPeoDZGt_dVbIsQIczfiKo2EiECrVRvzBayqdfFd8aY5NVfcNUpvxEvZ00u19mKsZEMgfS9D5pj2J5QXYRIU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=RkBstdNbhKU2TQMbEXQ4PaN8WnzUG2ANEPHZ4NOpITLb2h0emWNqQF54n_itAi47bzlS7PP1AanyatyWM1UMU0bdqv0KkRrYrfo4RQiOzQMqKIvwxO_Ix1eGksgzmdXzh72J3C8ZilFBacEeDvBZP7S8f7stmLj5G13nM5XLLqavZVJqJrH14_tZPEZCl4ZGT4unauKJhbWq3M1dnH_CI4Gd1lJRFj5Axzo1d5t1OnfAYf7vX_Orb6ulFQ3EYPmZGTPAyapIFIh5ijK9kaA4HovuvtGdSLQsTe8LSBMBFHF1U6jfvGKJC0asb4-oo66-p9UMGSaclsBP6upJhgWGrJi2ek8TW4xFGvi0weyL8ZtjbkVGJ2EU_J2s2kRNs1GGv8jM-n91iuWHj6C7YcfCj7WGlz7NYWXsRSoj41dxWtxR1F3-KEdH1QMbYkBIj7I8FuAbcFNqshZ30k6oZJT2HL9Y0NUqjs7rfCl-jLhgaATsITRd6U1PxGZUivuZaSLlOJ0wRL3HTsatx-aJooTVpaTfWPe4T9_pxYCwdAJNy2ZPnZRcaJxi3Utx5fB2XuvNk74e5XjcHVNfGWMdi_uRJc2rPeoDZGt_dVbIsQIczfiKo2EiECrVRvzBayqdfFd8aY5NVfcNUpvxEvZ00u19mKsZEMgfS9D5pj2J5QXYRIU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25733" target="_blank">📅 09:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25731">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DE00ZIKJ_B7VV7JLLEX7I_qJCXVr2xAmTl4CsjnVpg2eLOxSB5tbS1It1QPxd4qrCslFhzGVWm6zEe4oyqIPIYz5IJO0t1r6MEOizvawSrJH8bbN3fkTPPXsyMf-hfgVPSiHK4b0fXb3b8XHKfuQvbPKk4rFxLcSRPEGi7gagRnJMmqm9xkBJKGoKiI_ZhiGGS7NUNL8Ea-Ulcf-V8XLXy8SO9NJpZcO0wkkXM8FWMAXvG56p_eg9mrsw2vO1NtxwtdCu8VSnfQIn9OdHKHtaeerm1Pumw_NYZxgqgmK33oFSDNoCiHJfihDN4JaZiHNPXyDzExQRxR0VVflgtx4kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25731" target="_blank">📅 02:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25730">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4pYwdMsyTbAZv3nd4Nsbbt2GsA6BtdC1lmyPOl6xBEVKl6XhwCnDp2yCuYAb-cDwo20JYJlJKBpcwHlvpJhUfLnr0iubQMRx89CHEcJKji5-TwhbLkWesq2LBrRIao_IGosjN-81Qdzh8OhXfW6l9cR63PoSHDoo1JHxrLh12SWLDsm7YwGTXd5JBY5vk3RJzru4XR7y__ndnyqIv64htH5D4wktEM-jh4ohxTgCiLbvjqXpqjfZHLnJ6-6mcceAMew-hh3wq1R2qQ-CmKigaBo9QqeTQlaFH0zr8Wa5quwTEeU1nUieZl70Tnk2AiYZY5HzQTP3BGMSgDN9Ci2eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درسته که کیلیان امباپه امشب تو زمین نتونست گل بزنه؛ دقایقی دیگه گل رو توی تخت خواب میزنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25730" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25729">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vG9EqWMq2ymlnQA4rUgPJfLO7-rw69J6bgsljNaa-WDDkdaT0zhagJVxu2ZzeCITO5Y_tsf39fwkRCJqMUq_AKdNlBtfpT0yJ-pU6D1tzuT6DTMcGSvexKcL0wF3MUR7JrJ5wfHmX3NdouSTEIMjXrv8pellSQiOkhgE32VUGwiuxbOel4CglNb72x5UwXwn6gTILUOqsG2-JsnqTiAWur_JG6mZSxUq1js339Jps7iOqgGoVHTJxT2pNetEuqNyO_c60cV2SQ8btsZoAnZf4wG9s-p8BFJTwZUiWp5rmp1fRC0uUG1Z7zdMocrTXjiPZKnss9_49wWXpx_J3KR-dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام ستاره‌انگلیسی‌هاگل‌هایش در جام جهانی رو به دوست دخترش که قبل هر بازی به او روحیه میدهد و او رو شاداب میکنه تقدیم میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25729" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25728">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJdOZtAbaKmTQv1GI4Y6QKxvf7uGMs3Xo1CErgVlMkHNLI-yi882stcEZXahBv4yCP1110Zni9G15asytthJZG0FFYk7xZsln5OL3-D2TaROkJbYtcvnla_xV4YV3ZKv48AVE64GYrZLAKabiVR8Iw4Kp9IGV1sBlRl_17FS-q7dj3qD_Ev7P4-M2YoD5V03kZQRcteI9AxTc0YBUBi_AZIpRZZTVNUR-8sZw0WmSI08VbUdWemXkA-4cxHLOL22fXJzaGxsJXcenNrzH4l1PyEZwK2h2On7wxs6q1WKp7YjjDeEnxZW5NWW128_csyyXzuKG2kWmZYrTT2aD6dmcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25728" target="_blank">📅 01:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25727">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=Rm9ShuzgYkCIzmrOge1KfvtmUhA8QQzyky7rQ2WfVipYET_16RyQubydqCMbcT87kBjnZ1Z4no7GRfqN6d6mAgj4rl5ANohHPzlsZlxKLBDN0SANQFJFb8pGBWebazHCEmKcF7Pe9kA8Y0ORNBECB0c_b-w-3qsFqrpYa0r85EVmrgyaU-hFvRFGkFHBOlJMtxOnn9KvbkWrpaBrBrz9OCyyqGsnYXjEKPxwatQ6uG4-NywWjfdK8P5utuj_EjvhjpAmVbjx43EXSc5S64N4UDlF4om_Mb2k4bCdg18u6O0hXhGLlLQbM46nIq0YOaAQIeHrugX6YSzVRUGTG-YF_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=Rm9ShuzgYkCIzmrOge1KfvtmUhA8QQzyky7rQ2WfVipYET_16RyQubydqCMbcT87kBjnZ1Z4no7GRfqN6d6mAgj4rl5ANohHPzlsZlxKLBDN0SANQFJFb8pGBWebazHCEmKcF7Pe9kA8Y0ORNBECB0c_b-w-3qsFqrpYa0r85EVmrgyaU-hFvRFGkFHBOlJMtxOnn9KvbkWrpaBrBrz9OCyyqGsnYXjEKPxwatQ6uG4-NywWjfdK8P5utuj_EjvhjpAmVbjx43EXSc5S64N4UDlF4om_Mb2k4bCdg18u6O0hXhGLlLQbM46nIq0YOaAQIeHrugX6YSzVRUGTG-YF_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25727" target="_blank">📅 01:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25726">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctN-a8vPf2gKwGSKcyBDMNsQEFviAEjCFqdV602pX_QEM2mEUXavBMj1fhO05iwooJcyQEAMvyN_fSUxCMg5RWSNgyhB3_iHmUBRzH1iRyNbCnj2dQ1HLRt2vpzx8h_W1xNTYTwRtKBl5hVS5WYvKVBPyJRews8XFmm6Uhvgkg8VPSlmcgHo1jzce9TPCr-y5f8B_8DlDDlt_zENnJWBpELBZBc14B2pLP0WbQ4SIF1sFkz-mPNcgm-b-WeaW2CwCGght4VHWD75yNNeFZKNKdBCMDDHKgqM2QUSkQNTBds9mTBZ9TiUUgUWIO-0TpuaxHf8ngTfjn3UXXASccvu2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇫🇷
استر اکسپوزیتو دوست دختر اسپانیایی کیلیان امباپه امشب تو تخت: آخه من چکاره‌ام؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25726" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25725">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAPsFwaiqtMrft1tPqiNSh47C33aHJoJBCJWiZ7__pnVtlFu9QmtGAbqdXWzdHbrOVj7Bqmhv5Rwz7o2cW2cbbVqeC8SXteUooJoH4e1gTmOu9DRfRG25rkYzavWJLs8Q-Cjuy_nOPIZiulei3hXchS1IIR0ZwgzuMah2tFtntCg8x3mYa4PLvQYA-uEJFeS5x-aCUam1mAsYm8G-bJvQD-hTRJbXmqp-KzO30I3W1-cJrywzGyWccPj7gVt2U9xVOdg_cdWrf7a0VuDT6RmiMPxlCeH42EmEeXFPrRpAEzR8lgb_3caMXWR9bI-_2TD9b9sW2ubruknpFx4CLdzaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25725" target="_blank">📅 01:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25723">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L2VCvnfcMJM2Nb7c9MIHf68aQroAbMwvCsJfA7AWXVIaD5PPzKAX49DDjMBPN260VkSx2w7jIf2zfUk3QwpZ8uITA7bC-xw1EIpN4dBkz6XTqt903jvGQXqTC5Y9_Z70HpvxzlQOpBM-lJuFdSvurQXg1F2En1EtM-cNq3Xn4lqBfvVfYmSDxOeaGMFEFolOnSxSe3TJ_m48KjpRmUwEf7ncJMWq7SMlsezziIxV3YdGWMDm6ifqBI_TY0lXCMSL0PvDTXw0n8VKbSRRr-uOJFb-Is_-qQN2i28rLpQXPhs1E9gOvlYeVY-lMDjNKD02MLc9XyU5pO0wAaKMg56A0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I7ANth6CgC2WtUcEAf9G7crL9wCF0kyI1HH-kKuVAbR6W6v08fFla0XVK0nUZRcH4NiOCLZIwS8tiNaDNMr5ODgTyzx_eSKpRjJPHoB6ygO9SZ1VztZ8IPmhZR1lbJr3hz_Aar0zkRtNvlnapgeQUWopBoDzlYP_tPYP85O1dfttJGE2k57FH4dLIm8_ZB7kFAlfQNig4OI7h0c_d-EK-haMvrIhwhTjZnCoV1z9BkKPmR7C4jIwzr0lNHPjHBNpXxYdfMrevNrkuo823AnFsYEz7TsdutVZ5RBZpsahlJVMavY7X-GLxR5i41CbQmP_xXm10pgMX-4ktJOuU3HqMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25723" target="_blank">📅 01:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25722">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2zXL0l5ss27mn29EnEv5mITf2KdwXU8Yr9ZkJyGh0YmLJVn5ACM2L_3kSdxfrNYcEy1vyHN3l3T0F_167NQHZyCq3p7ONJmXUSCxb8wrckp-I99jEB75bh4zAzZBhHGDvxTAAMc-u2_ef5t8vm08NR6F_xTbM7tk7RzFPrg8gpFSxrcDO5Pkz6IBMebDSLjQn4CweP4mpRCM6HFUSbLMTYwIJMFt_KbvlLe1aHaK4Mf1I_dnofixWYi-SHjKd1KZzk5MUSPu9suI81SR6DN5ZyoxfdlnzUhS8gjlGUxJ0je3v7V_1fr2xUrTZCVqqljBlVnnU0Y7UTIH3su4Ji9kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛
جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25722" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25721">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcNhJ_-j8rIYcGqthz22O_W24EslrO13-b7uCErtFZCHIpmPYvPCYfp17KJVqbHw2WZgmw-M35ZTDfPNruZx9DAM8RjH7v2A7XGDAHUGqt9NLqL9RNY4WkDuwISfkRM-Kdz8yo2jitdgbcIVzuTqZwxZQR-p_7Kh0c2fx2MQV3ZQWJEgyZ8ZUAmJUhs7-xcvZ_oNqsVawbKQpGZEh_R5H5nvWzlHbNSevaumrEsqzB-kD7WebNRtgNtOJ5Nm3VcLDzxgy1E9RiO7-5ot4xoexMggOirH8metgC0L4R_npr8LNaYns5V2M5_ozxHMtLFtO4J1JEf3EHTNM2wV6NdZWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدار‌ دیروز؛
راهیابی اسپانیا به فینال جام‌جهانی با نمایشی منظم مقابل شاگردان دشان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25721" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25720">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/st4HoZD-x93CN0wePpB0SfQBgO-_LB8_gTkfTnCjKlFJZKHzXICXXLyG4jwerg1_sx3Xr9eut3a20Arq0X_rqAJjjpEdljkeAV0ZGLbszb5dwjXTsoSRN_W5fsdO8uHKoSW49kun8F1cXChqkMxQuyXYpAGrAcD6PapaOMjYL8TTuzzj5uhVju-UH2bjvhqc4EISeL4aiIxlvOkI_GHmLyWNXse2PHnxiO682oWGw3p8Fh5c-hRuWplNJerAlVY3YsIg_TaKARRMV6UFF4tYPfOcfnhDCCG4-l_Qg-z5Z8dwv5bcwRMr_N7hht-1v7bm7VFi5FD8-AKZGP1vCA2ZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ زین الدین زیدان برای قرار داد 4 ساله بافدراسیون‌فوتبال‌فرانسه به توافق کامل رسید و در پایان جام جهانی 2026 جانشین دشان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25720" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25718">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AQFSK-8xEBROhXhykuuJ9fX0j8iHzjrmJE5PaOjpVbx3jajNlEalZkNy_74hghcQf49Mf9nQuBBL_yu_IdOt6XrqISbp5PWBGsCUsOhbxsrdIgETrf6bMrt07wVsb3pRicQvQPBUn7aZQAccCHaCRgMQYMzTKczDKTlNrOt0njhEI2t4gIvpDqZpMB3BtJ2AmUtqImY2QggIrfV0QgOo5biWLOrFZRLFeWzcQvXPWNnvzOcA9mk93xW9OfOdAXX6o07Q1r41Ozj05uFdyTJyMJCuyrs1zJdEsN85b3HIyw3lpCdVWN0OUtWh_FYBRzXuB_oMbtLLWa16w-r_wlY_sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLqqVrKdwzhTVy3NibvXYJ-kOAVHkFESzT7nPGw1DrPHJPWisCaBitoTdaz3ZRpF-z0XlHyQFoPg5kFER0hxhTcJ01ufFSRwQ8IFzovNTqIscOljDXyn_deLpmU-COW_uUgSe3wzj3YCuX7dcHFJgleJjZCOQSkx8oOfd_LoLF_qVBpHR1sazh3n-_pIbnSxujiQzUoHg0XlJbVmKfiJeMZO6_yC3uR46siEBnRmnyManEZwql9uwZUMeHhJL_OcVTD5ULZceM-bJmOycXJ-nFIaaXQm_KRdonhadX3OOBTGwy7pXHLC1Uu2vTHSMhD_EHw49k0bNhMlFP80Nuy6nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25718" target="_blank">📅 00:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25717">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-8xBDi0PjFQ9XWNEEk6iGY1t12FqaoImb654P9kBidlViASOonxhD_U5GYdAfltPYRkmsY5kBfkSJNYl2chvnQC9UaQIuV7STwXvha3iJ7KTwq1cr18uER0VgI8R6b7QxYS0ic4X98wxS2hBA1Qk0SuDU2GabFkXGKPFd_YKbbLT3S11GCf-6eMla72eW2Tk7s6LG91zCOBjGPjW7NgYz7_7CvC2QnaIuc9F9waJtclvXZfgpRfm8XsngZ5ooDlI8k8XxO1JdzLi2ifDJZfyZ0FOilNoKfaUbhR-WvBhv9_3ng67yZqU70z4lHdN8Wm0HapZ8pnVdXtt6HeAzwLFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25717" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25716">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmiGRwqh9IOBG2Cx8r_CbjqPt9OAlOtgasKjF7Z__V2Twa768COusiZeq38IerltFwHZjQVKk0kPO7Wfr2KgVixBPgfNDHKkORcHfxXAHUNAV4JksBqyxFSDJi201mhHwCLxBvFN1uZdzEHLsmnWQmzU0h46zu3cI4hQcKmKpAVVx6lR8GYabfHjBmkX-SY7BEJZn5Ppzu5vtuSCEPFvc8Y_EwPcMEFjR8rU0s9wWtcj8HWIphWWdBSecWp5n_Ltja1tWnyrkXgRYAbziMUwiDGkrAPq10g6YsP67kLg89d8mL4pNr1VQgtNNDzJcH6Y3xj2utMseKIrFtvSirPUuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25716" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25715">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSl_uxfm48CZpOphkVAlnru35Eo79xTuLNuyYgGMgpwDsuYUDSk90Nb4c8UBjbgfGbwR_zZ6G6W-lm-_09M3fejaMnXsKiZf7c8oPiECo-Ad74JStO06le6Gh2UG-7xb_mQUzlKdBwev1pHNnte4H-6Lg1490scDEMPkcPz3AGW-EOpJimSQddTIG290gyT_ylQLEGr-W9uOJ4Mry20wu2sNJAprfCihty-ptUulQlxXq2NqmUbubqhJpDuRmNwaf1-5wQsXjdro6rBeUpvgKx9Xve0zeRxnOhh63SNzbyU3d1Zp00gDteu7m_GfKk38sMuhe9wK7ygUJiCukgH3Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25715" target="_blank">📅 00:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25714">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NI7Gacw6mNbFhZZY4iZycYkK3CZSBXl1wpSI8YkHVveZ7ZN-bG_PMH2TiWWQcsSALxRAWlnQI6rvA_bJwoMGgbAgpAZeNS5cKojrpUEfee8SKyAo1dZWSEcUHod4CSAmzhXN_JkloYEFceugPYzqJzSpBn5q3rMonAtEYynGLNprOvoS8etYJ-WzSJOaFiyc_VbFKbpp5PVWFSOX0QC6oUcltwBYj8SnxNFezMVwG2z8a9W7ZeN87TxRktGy0MXVDbijuP0A-WhYrh52RzW-7xXZu1j3d2bRX_iH0pTVwu5lqrzAmam-WSE1Edr446olYH7qUrN6Txflp8Ec9xGjqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
وریا غفوری کاپیتان‌سابق‌استقلال درگفتگو با عادل اعلام‌ کرد دیگر نمیخواد بعنوان دستیار فعالیت کنه و به همین خاطر پیشنهاد کادر فنی آبی‌ها رو رد کرده. وریا میخواهد سرمربی تیم لیگ برتری شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25714" target="_blank">📅 23:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25713">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAl3QW0-rFchCZxCs5fqnPDKtfasYZB_p1FhLihtqwAAhB1kUIqVIkbTqOQkCE0JlshIg1zZgOWRf02GNzNrz45f_9Lx1hRCjewAcMRUXz52R4pBhwXD-7GO9gZF3TIC6At7_nLIydYCA-shhGTBmajgXPbaXVCaPDPZD7CgxbVRRwOsAD3-JbcGb_ajiuLEMPbn3Gs4GzAG2Sik-MJlJEJ2rlBpIvtznZReF92L51uibxZdE6mzzVTIwSbuDOpluYrRrTXlFYmejcmbrb228CxhSwp46OhMEU5ldGf-HboKh6ZFD_mc619TyJdMfXSPlCGjj3lN4CppsCR8Huhf_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25713" target="_blank">📅 23:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25712">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvgavLKh_P96CiZlHk-3R3an9YJydfaTI_GE7BOixY_EZ0Sz_a4gks033NFYxE9mrXaCkOBR3pQqHmPTH-69Sqk0OqC-XKfKTmc4N1BI3IdhBXXD8VXK_0CAWq4mNkjDpp4v1xxFAjaflYG4-NuJbRzz75RLw7qbW-3eXeX6XLcU6IzvqmR2Mr_a_M_xqSqKBJzMR05KxAK06FpmelWDjQM-uxcmwX3vZP0MZGLDKZVS2_RGjMuGMJKxX-S5-lPTm2lXdfN0zUDCUpmTR2xkkoYgDzB96PI_kyXZroGyn2wmoOOXucm1eX3CGN3kuUf2RAH0l8Bv78VJzUGqeXelAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25712" target="_blank">📅 23:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25711">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILwtnaWBSK2KV0OchXRO7jJtxwzHInRuMdHtro_9UYwVZ1JC04Zw8Xzw4uQN66TwIKDNeyP8D4HPH3o2J74J7os2b4eLCgMexi8THwkLAfA9AwAcO6kRlp3SDnHh0rdTqBFcGv6C24njGjGMC6ggr8ccYSzPj_rqQx1j-aW9V-YB8peIHHZD-r2Yn2TVfuds0K0Cpkwo9JJZzjj3pNBC2Cz-Jd9ufixAYfPxekcfL94UX3NQgq4HekgNak5bzlBvWc8UtfkGN5qU-Dq_mGU3ZUEqoWc_IWEaUCZApLKHlHtHn3-IsylALHGoJGId9UrkfQ6se_eIhYkotPIOXIMA3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛
فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25711" target="_blank">📅 23:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25710">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=M3vrlandLTnbBZ2g6iAFAXFyAHKPY1BNvC3bqcH3WOi6CnhvPs9O_yQjHPJTUcP1_kVxWfjNq4LOBQks0MrUl_qeZskU0J0xlWEfjmnu4dU273a-TqWdckZ7Px04Ixvzze3uPxn6f40sKfXCLuNlMU56HG8SNtFq4UrlYswC9GoKWOzCfDKBQ7200IcmiOtDKK0VHsli-hFNxrTcVxTvZm0tuWGEj52xTql0apzW6KVRMa9uXVIVwgoFxphc6D5f9_WgUtOUjKf436fY5nt_70q9SQQBUantJeoximv1Pt6T6irdgogyL_FrsJgEHwrC6rRj15b_sHTYsGQNEO25AEf06tnycUeWmRrVtJLi3AoN1IvEOSwHIIiHuyC4NH6IHtTLsSRCjrzb8eN7PCEcB0Xo_vCXy8MxsqjW01iyO6PdQZWyHJX3GxPaZWWd3kG_8quJFl09AYAwpUAFgfHxLu1yzO_A7b3fPb-XmTEFL-gp7qrE9GnVH4DYdVJv3uBFl7pOK75U1aGSBTj4hsWRc5sVLQhHb5oF1qaazgYIWuNXi2Nao0PL8631W3BduUn3Fr7afUOAQvhW1jEcLP40txbWkaB5tvnT_M-aNMMbkEIgQWjjc0cAxsvAfWu4xl-WuKQ-_7t3zqVcUVM-YrGyduFNgsoL_CVVX-vZy7juCIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=M3vrlandLTnbBZ2g6iAFAXFyAHKPY1BNvC3bqcH3WOi6CnhvPs9O_yQjHPJTUcP1_kVxWfjNq4LOBQks0MrUl_qeZskU0J0xlWEfjmnu4dU273a-TqWdckZ7Px04Ixvzze3uPxn6f40sKfXCLuNlMU56HG8SNtFq4UrlYswC9GoKWOzCfDKBQ7200IcmiOtDKK0VHsli-hFNxrTcVxTvZm0tuWGEj52xTql0apzW6KVRMa9uXVIVwgoFxphc6D5f9_WgUtOUjKf436fY5nt_70q9SQQBUantJeoximv1Pt6T6irdgogyL_FrsJgEHwrC6rRj15b_sHTYsGQNEO25AEf06tnycUeWmRrVtJLi3AoN1IvEOSwHIIiHuyC4NH6IHtTLsSRCjrzb8eN7PCEcB0Xo_vCXy8MxsqjW01iyO6PdQZWyHJX3GxPaZWWd3kG_8quJFl09AYAwpUAFgfHxLu1yzO_A7b3fPb-XmTEFL-gp7qrE9GnVH4DYdVJv3uBFl7pOK75U1aGSBTj4hsWRc5sVLQhHb5oF1qaazgYIWuNXi2Nao0PL8631W3BduUn3Fr7afUOAQvhW1jEcLP40txbWkaB5tvnT_M-aNMMbkEIgQWjjc0cAxsvAfWu4xl-WuKQ-_7t3zqVcUVM-YrGyduFNgsoL_CVVX-vZy7juCIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌جذاب‌وشنیدنی‌فیروزکریمی‌کارشناس‌بازی اسپانیا
🆚
فرانسه از تسلطش روی زبان انگلیسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25710" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25709">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=q8O9eb8qmkPJzC3T-hLzB-TaLttbH5TJaKHd4qCl098lrmvxQap1fsmVRsTMjrvevIHxlBjmguQCElkRoPw9sCR9nu11behPfbZguc_kuvYTP6oGctWQn7XY9FEC01n3m30mLXxwr78f9C5LHw5vx4bMNdgrqn1ufmX29tWZ7_ihwoI904oZMkDGG1jKBlOoTPL-yZ2mp9W_1ZTfSIxb9Ukpt_Jsh5fmz5ygzKzV1b2RNFjpbyE7M017V0kl0FOSDA1PB4WqLaClSj0zYSBCuXAMsOnnAOzkXfgnchyUuD8TC9d7xqDMZwmZ8EGl_93DY4A2Req-KEtFwvvAbpw_zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=q8O9eb8qmkPJzC3T-hLzB-TaLttbH5TJaKHd4qCl098lrmvxQap1fsmVRsTMjrvevIHxlBjmguQCElkRoPw9sCR9nu11behPfbZguc_kuvYTP6oGctWQn7XY9FEC01n3m30mLXxwr78f9C5LHw5vx4bMNdgrqn1ufmX29tWZ7_ihwoI904oZMkDGG1jKBlOoTPL-yZ2mp9W_1ZTfSIxb9Ukpt_Jsh5fmz5ygzKzV1b2RNFjpbyE7M017V0kl0FOSDA1PB4WqLaClSj0zYSBCuXAMsOnnAOzkXfgnchyUuD8TC9d7xqDMZwmZ8EGl_93DY4A2Req-KEtFwvvAbpw_zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس اینیستا اسطوره اسپانیا خطاب به عادل فردوسی‌پور: باعث‌افتخارمه‌که باشما حرف میزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25709" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25708">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seFmus0QaGjvRnN_l1x0MwIlBI0hDzdxBjh8U9YLo6IO1hjpEna0uilJ3wl7_ZRBEu34pfea0Nj5u8yNSuaJ4qCFLTUyzIhaUw5Zd13ui2RaAECV1-hTB_m7vIIc1dRAMcLPBHQudptH5hgLTzEqYPp-3XBVDOJCPqojEgAe4zdCXNBj27VII6wL0fRwUoFoaZvchHKYRWrF26jI92IIelIyW0NiPi_J3Fbw8weBnVRAfJvkPySYjqNn1vpSpqF_expe2Hp_wTXWzGkqpW9zVTNzol8nBcPciUKXJC0H5uOi2lwdxpfzqF9m5fpHDUnZu_2ufei-2OxAZiiqG671zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25708" target="_blank">📅 22:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25707">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMbD2Vw_k7ZQ-ToU2UkYKscSKMHRKhAMVwlDXanb9p2lIEXFRCGoEDSa4kX0l5K4wCpHbd328ua_xvpJxOZOqNM-P3tTPUU_kfxtIL_NQjcxKWf-1LuM-l8XQeWCeiL6afAdya3WrY0mXp88oglU9ysZYOsdxcF-kvNyTjVPoBbbd1D33xPwziAlTcxnQYHA4AEUqPBj38w7S90A_JT0_NNLSEm9Km97pIUxAXMIcyI8qYUgQDYHrC89QLXHdqDb99AQKAJSPzzqnEST8vaOITZdyYdMkj_VPRUZ8OJccqzsp_2ruCdye2Sont4N7wk-qFLApo2T9xdYeKZgTyGIpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25707" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25705">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K3GLzu-y_C8c30UQx25tw_UrJrk7-HjH_wyBJAAsnwqTyySLQQczjJb0ytccdmh8Hh8A9qc5NOtr4PORWp-hmUPsJLShBFpaoUyWFq49xVnPo3gFD4dsKP-dD3-JIDze8J-8SytT0Jjqy-3lRYq1ugTSDKrr-88NhIJ5O2Dii0yOlid7PAuu_7-Sy8vdZte_Uimf276a8k8KA-s4ah-zStA6juqkoUgwsQw-nGK-6Lg4qXEQnKwEHzJwXglpOmlwM97KPNjN96MK8PMorzlX8WbO93DQeJ-YNNhdcSLyq5weO-m3ciiG28H4Pwpzd_LT1HjMN_vHwhtKQC4j-9YwNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DcOzQT6imRwqP-uVIqCp4s1Ie-AZixHken3gGMVMfY36iZpQvsa_l_J-2USrdad2B6aVjQUeeglAOWTXR-riVA5zuimzHcYxYMFikpdt7RXZm9akSsCyLf_xnNkyhVkUn_2AlEA0z0d5ot3SrM9yV_JISRFy5lVR0hA62rcU28IF35Sj8egx0s5eLhhb9Gg_3wLwk_U4jMRUzVkdHYKcCdJEvFN0wqzbyZSiC2_B2TE9hhqcrQnTX_ZXN5pKh9Uvr6EEPXZTp1Gte0lx74wqlnAGhnToKJnOBMe7tZEsrbm51zKA1BXBhal0ZprN0g8R3Wqo74W6Co-UZrILXgBQww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
خبرنگار معروف‌ شبکه ایتالیایی DAZN که معتقده تیم‌ انگلیس قهرمان جام‌ جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25705" target="_blank">📅 22:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25704">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBWX-1WXANDRYyeZR-1x0P4G2-Hr9eAHwY973enys_uy8v5UaZYJRYVzl0_nlb9sczXt-XMXzz5zQOb4C1uzQitpFG1VDxEzZZJi0eDqbKS5LeE0miy80YUVdtZAWStwlkwQZRZm-XeG-4ZkI1h_OD6ku-lkdaRnFLWU10z7z_DtBmdy7VKQ4UrVfI1gn3sr7-qoSB9rhDCeI2nW6uUNIgf9SicpfC05eKnz2fqig2NwWopMo9FwOMu1eW-1EJR65Sf36ieqYVUCPJJKSo3nItLr3Nwqun49DO7N1RRWYbGYzG5dsPx1Ar0-6rTqSeElvcIiCmvFT6IvJJGNNutyBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهاب‌زندی‌‌مدیرعامل‌‌تیم‌نساجی: برای خرید یک بازیکن‌دیگر از روسیه باباشگاهش‌به‌توافق رسیدیم که روی 1.8 میلیون‌دلار این‌بازیکن تهاجمی روبخریم اما خودِ بازیکن حاضر به امضای قرارداد نشد. پدر کسری طاهری به نماینده از خودِ او امضازد و به تیم‌ما اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25704" target="_blank">📅 21:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25703">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doNmM7BruzFCmYs1CS42h3_StW8UGsWcxxh6RGUvGqbO7bF1YZuzdd8fgrUSU5WIB3gCY3UK_-lbUYQ3rHHI-yoWblXkqhEEqVpjmsf9iHkwKawOb2dwcK9NtzYqv5eh-VODbjVJ83H4B27XoPbTRGT8YHKYkDrCPuXqx8CSVNAwl70UbLkALgkFDQEvaVHlC7RdXaJ5opWh6NnyaT7iOloynjLbA8708Mmrhy-noNKkY4EFu7kOsQWkcqKOjfc-JST1LwG-PdHv7-jKWt6pvRxNdwT88Jj7mBJlkF1pynJ0hzZNypoZ3MkR93pcdzCXda348BbzourM4PpXP-dadw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
طبق‌نتایج‌یک‌نظرسنجی‌درکشور پرتغال، اکثر مردان حذف‌شدن رونالدو ازجام‌جهانی را سخت‌تر از جدایی‌خودشان‌ازپارتنر و کاپلشون توصیف کرده‌اند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25703" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25702">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0ckF2v6DPrjpRLByR6zJfZFRjQerhbm9cdAr68k36gisnQK6b5cXjcPi1VWtmtDkNb0dhQnbjkxpuAk33h0MSj8jeJF4NcW3OWmtGXBSosptWQweq1ufo4ZVLmraFSEF-5UgI445z1AdCHRZoygJsnxg3JPdKJIpDiz6VsMI5c4K9fLiDUvy7p9oxiIP25SGUf6Qf1rXF-eOxooAUgXcG7cSIvt8Cfmq8Bt6_XYLKV72K4mlHqGOmAZMyfU2JtDWDH2aKBLFf7cKwHCROMAqRoK5SR_PVtUd3zpI-nIhUizsRKKpc7x-6lpKU26NI1pFCPLkR23Ydm-sBEdBUb12w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
۵۰۰ دلار جایزه نقدی + ۱ گیگ اینترنت رایگان!
🎁
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
🔥
نیمه‌نهایی جام جهانی ۲۰۲۶
فقط کافیه نتیجه بازی رو
قبل از شروع مسابقه
درست پیش‌بینی کنی.
🏆
۵۰۰ دلار بین تمام پیش‌بینی‌های صحیح بصورت FreeBet تقسیم میشه.
🎁
علاوه بر اون، همه برنده‌ها
۱ گیگ اینترنت یک‌ماهه رایگان
دریافت می‌کنن.
⏳
فرصت ثبت پیش‌بینی محدوده؛ بعد از شروع بازی دیگه امکان شرکت وجود نداره.
👇
همین حالا وارد شو:
https://t.me/betegram_bot?start=p7_r4EF37DCE</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/25702" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
