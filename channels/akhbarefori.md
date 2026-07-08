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
<img src="https://cdn4.telesco.pe/file/eBh4UXPQ2xY0-9vmDHzCdL7TwRWkS5iQfxG5VoVWK3n2Y7ziC0gol_IP-PB9mXyZ6NbdUuwKVOuVhExU6PcnbkvKXSrnqrrUvWgAFE6LycpjUwSu3lc9JYKswvW4etKcH5my_meNJ6AynkIbJGK5EVxWYZYD0-A2Kz2FurihEgcAKNlbMu_5B-uBELPQshtKVXxdcMDAumEsM58_DZ2bnwxqBgxUfXYOFJr2R5W8QJ70TWKD9YU_p7-OO93x_ifiMa-JeJfTelwMAgX6KwgmJUn2m8ACT4YJMLtoU3pIrzA8de3ocm3BbMulq6BfU5Dk116plUpcit6ajCmCGZp8JA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.48M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 05:22:29</div>
<hr>

<div class="tg-post" id="msg-668206">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای انفجار در بحرین خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/akhbarefori/668206" target="_blank">📅 05:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668205">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای انفجار در بحرین خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/akhbarefori/668205" target="_blank">📅 05:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668197">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KwwYa9jZZV3ZOqBjtOecq97NqG7xCxwNkPgwAmEqqCI-I0UeiUvZC_9qmeJv0QQ_S3yWPVc351x7e1zp6J9xfTpMG-N1qL4IkJ2HglhCmGGl41DTGnOYB7KZBUWnJu6B7KrEbkVppxDHBcxsseI_qF_hq65lRj7cN3L5TtUtGwq1oDQqH4eyh58-CJPWlKt07DsgSxhQEWqzgFBzR8iD6eQZiGWvJ1r_qfikddM7vWYzw2lzaiXUPfnkUgnW73Quff10kqNiKLCu77Jf0dZ5xZqI6IDqyOE86zjNhpAVJo3UdTebEs-i4KjammCDs7rQ2vSVTL8pVz0EBDWNQ96KRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pem-k4Vp72bpCUTSXCMon9-rCeql-APXeKVxO40Ffr347cMjgTFmk1UtoY28KZv97a0rU-k99l0NdL81jw66ZQS0FbuQFrdePZX5NpMMSTsVP5-yKbpsY7LsWrlqgMVXC29yNtaDdlw87xJoV1VwGzgGh6RlC1IWzh8oVFKl7QJD21s5PMSXufKU7DwT0OAnHbRuAqx6O270R9BNsF4bfPYwTaXj6Ulj5wNtcl68izh5NYOdBKAgtMTMWWpq7EKbDcR2NGltCHLDKSTX6JCWC7If0FSI-qHit9hpa4z8fKcFdbU6iQB-NhvNKT9GXo65ERB8_k-0ELP2TtVKnnyZXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tBfdvkdpQHLixpdXsMd7mDpHM50wemhg5G71cKa7CXSTsf0z8lqZqEF0Sf1VOibusN29taCrIfjmIfGoKrDqOyed85DwkJbJxXZRBVR5RBx4TURDe7vPcz7BQAOp2cFUdS8486rWyoDr3HB1uPyq2ab_BlgE_jS1RMXjVSfTAxh0J7AcxGesx90ryAeWlHZF_rxlw86PjYV5SppVh8WmcPU9JIi5Rk-Ws-_zz4UUMocRaecDlqyuFcdIU9VNxXescXIwIlo7-gzTKQeZ1DbPmnJL80spg21MHm4i1kaX44EPMwYydUsxiJ8c1SrbxxqPXlWwWcy_5LTCMmMtnmzs8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FgGnZyNJRtSrxUCUlABUJrz5fQTu0e5ymVSlT5p7uS7SmhR0CHm_bQBeW4wOMJtmgHSTQZa8x2VX7MPb2piUBFpxWVCr3UhOD8Bs-JpRvb1oAVHAZYpB0wcDFsHiKjEiNX1_BmNtGEQff8E_yfkZRYyUDi29KV3bYyNomGx_jm4doN9CQP__gJ_ayvZTEXXPyfRie34uvcaX4SFsyZGehccPh1cU2lnhMNd5Xspev5b0ZLc2AV69RLpJAG-dSDDBweCzO81_vs_qR0oYHiRS5rmI43-TFx-FagimOsL3cHKjUQkCOSmiNSxDgUmlDDYUIOyf1r1bRjFMuVIvPVA36g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WP9Tn9qjBiVNQ1cy1JkvS5cBCME-mQkNspwpg4J3V8oFkbu3uOaBSrl10KUAQJcyXL4o1yNJQHpWGq7Ra8LQOysPfR-1JDf1S51iWusC7LI-BhYYvO-9rBrDiUOlopQBstBvVftnGmeuU2q_gLB7z3hk2ZIbPVPseue9lLd6mRKIHpvj0RLypHTJZPwUCnCsIzUvMvlyjYxYssvF-kkCkiXA32HkisJg9u_Cp_ZhfhjYchH1VPY-2_mowbQYtqSVdJNGcTEK3XFlm2s-InkKYRODEmO5mw-RFAUO9ypOdA9-Q9DkocAAZPK1V_4aruumggf2_K7iPIGR3F3lSKhQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d2OcCKGBFQZwjbzJyO7W7n5tSPP1UacpYPn1iKzJFElEkgjCe6xpEYXXEIc8Ihl0qu4NXKHIv3lKxK1N3svSqFVQeLwB_Hrw4jTilsuJ5Ybc8RjPtg-05-RXyPxodlZe4TmjZS8tTn1ByX94Yr2V7488T91rsYThPXWKiugrrPmGusO-iNSwAn1bDQP_ULnX3blQYAm-z7zM7mvDq189apuyl3mVnhV1-PXE5-Qeop6vazgW6zpTNWbfN_W7F9zYFidE_K9hEj6oEgT1YRgSbISoIBnCzwiawpDiPiJqmy23pplQ4ptGTbxulAnbTQy_Mzm2kklYrL-8DeT4RYM7zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbasVtMeTchH8TwIYD1vUokvuKtx8qopj-iZitew68CotDP1j4dR750R60whngeM1XKb7weAC-oDFaigJddbSA0Qvf_GY-CEQRcscGUUgDFW5cdAIs5xyx8dHkLX7Lr6XMvJu-wgdcDxTIxhUj0gdh4Om81W2fhnylHF2RmSySzyWejogEjEZHIoUvtjulVeF1mmzUoUMR_kA87q7jGabXUp0ASZcKwxaB40rfHFc3yVnlJGGEgHl9prLGjYLS__YxGAHlL4mnxVR8fz4lEFA80hX6mvne4lUVn9fTF3gneg6BOEqK-Jf7jtyWfJzBR0oaVk8oi6Rpy6YkNpXtC5uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TXuX0RwdBcBFGqWbKvC4i3wp_raomCHcX0sXJ_r1OT_hUsV3Gn-V9QD2u9lPEOgnrsrevfm5m6Z8VEw3owlvm4LrXCmI_STJOVzMzqCFeSO1wm3l1KmxaVcFHrO-4Q8YZi7EUiqzzH9kL6OdS9l9TN860yaQwcks_A8iEghw3NA1whHJJh5F3MDKfKoZdlrMaCqQUOIja30q8BbmBjDR8nZhwiSJVjCJ7tupB4ab-T7mIzJA5UyUQTDc9ptDwNTI1Yt8efv6R9lVAIKSUOlTU-VasefoQlf5O8OtcxAf4tEyT9CMgrYdbt47w1kmePeEA1Slva7fegtqcBy_YZgprQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از حال و شور مردم عراق در حرم امیرالمؤمنین
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/akhbarefori/668197" target="_blank">📅 04:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668196">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac39b4df86.mp4?token=HAsE12gv4zZS9biAA3NhqoVaTfau30OQS53tNu9ZSztoj1XQgJ1_kc1Ios4KpxOck8nPpLxo1nldJ1Pl5vrQuVtxdzL3fdOP6LRzpwgPDttNRiySDiFnvmoy8yj7wJggnypMEBdeUPcyYU9QRgtzB2Ns2yswuuHtXIXqrUiTK9JyDg8VdMWXfnP8WclVbZ1VpMFZaCi4VovhjsU6Ks-boyy48OBQcIYT1IP4ji-xFhL2YpkggDXRrRQ8lIFsdcwR1nWY_wqQggM-IpyBr2dC_y8A2CxakOW7sZMlPQjYiVnJAqHp036RrywO-ONLHarXLDd1UjTkwR1fOlXPHH85JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac39b4df86.mp4?token=HAsE12gv4zZS9biAA3NhqoVaTfau30OQS53tNu9ZSztoj1XQgJ1_kc1Ios4KpxOck8nPpLxo1nldJ1Pl5vrQuVtxdzL3fdOP6LRzpwgPDttNRiySDiFnvmoy8yj7wJggnypMEBdeUPcyYU9QRgtzB2Ns2yswuuHtXIXqrUiTK9JyDg8VdMWXfnP8WclVbZ1VpMFZaCi4VovhjsU6Ks-boyy48OBQcIYT1IP4ji-xFhL2YpkggDXRrRQ8lIFsdcwR1nWY_wqQggM-IpyBr2dC_y8A2CxakOW7sZMlPQjYiVnJAqHp036RrywO-ONLHarXLDd1UjTkwR1fOlXPHH85JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای اربعینی مسیر ورود عراقی‌ها به شهر نجف برای تشییع رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/akhbarefori/668196" target="_blank">📅 04:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668195">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6519ae9688.mp4?token=CBjyj47QfIQdI6Q7Ia1g4oC6mzCgn3WTE6batEsnYk7MY2ArmXYnqDznV7xCPaTBfwZ_y64z-eySzIeTkJDI6qnWAgXCxRfy_-ydYgg5_HRnVw9S7-PbZ4i3zkDgVqembDssELpvGgzV94Rj3aKK2I95Xai6r_htDGncyjmIL6FcsKPibuGSqmzBJ_4WUDOkM2ax8BWHG5xfkM3zbnqbtH2pTUcuR3nIuWav_vGEVm9aHfrmg7rB8nI4kpRF50KMbRGOaNFzEcIqLdmBRRMK5db-SC0TwWSYZsOvGZTeq_pNze7jwQXnobrPNbu2Acf2tG3W_h6Fek5T5EAOUUUNLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6519ae9688.mp4?token=CBjyj47QfIQdI6Q7Ia1g4oC6mzCgn3WTE6batEsnYk7MY2ArmXYnqDznV7xCPaTBfwZ_y64z-eySzIeTkJDI6qnWAgXCxRfy_-ydYgg5_HRnVw9S7-PbZ4i3zkDgVqembDssELpvGgzV94Rj3aKK2I95Xai6r_htDGncyjmIL6FcsKPibuGSqmzBJ_4WUDOkM2ax8BWHG5xfkM3zbnqbtH2pTUcuR3nIuWav_vGEVm9aHfrmg7rB8nI4kpRF50KMbRGOaNFzEcIqLdmBRRMK5db-SC0TwWSYZsOvGZTeq_pNze7jwQXnobrPNbu2Acf2tG3W_h6Fek5T5EAOUUUNLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وداع عراقی‌ها با پیکر مطهر رهبر شهید انقلاب در حرم امیرالمومنین(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/akhbarefori/668195" target="_blank">📅 04:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668194">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/283cfe7718.mp4?token=rbINENQ0Wg4TWbODqNa9RuPMw24Z1A4CKqFdr1rlA4WZRwgaHxmRN_WMVKyUVebi0pAV5OShUOcjzRZJJT9oqHNSDk2Xg2n6uVH-1HkTZZqVvDjP2892dzovB1B_GxNmxb7ZZM16Ziyj8iTT8g4YV8cMjgAD7oLUU8LuA4TaaMfA0hg9v1yUW8y8QUdCSlkp3gLWokpSlFzLrc6qNA49UbzFElbQ6Ne8JKKU4XAONrTo2X4cf4Uk-hm8QBbor8knXTgmGmsnNcSHd4lr5dlPsaJBS3iFirZAh5_f81GItf5XhWKLNpky6s3ggIg7zklkJ1gyotHVIS6YWYubuIZ2iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/283cfe7718.mp4?token=rbINENQ0Wg4TWbODqNa9RuPMw24Z1A4CKqFdr1rlA4WZRwgaHxmRN_WMVKyUVebi0pAV5OShUOcjzRZJJT9oqHNSDk2Xg2n6uVH-1HkTZZqVvDjP2892dzovB1B_GxNmxb7ZZM16Ziyj8iTT8g4YV8cMjgAD7oLUU8LuA4TaaMfA0hg9v1yUW8y8QUdCSlkp3gLWokpSlFzLrc6qNA49UbzFElbQ6Ne8JKKU4XAONrTo2X4cf4Uk-hm8QBbor8knXTgmGmsnNcSHd4lr5dlPsaJBS3iFirZAh5_f81GItf5XhWKLNpky6s3ggIg7zklkJ1gyotHVIS6YWYubuIZ2iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقامه
نماز بر پیکر آقای شهید ایران در حرم مطهر حضرت علی علیه السلام
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/akhbarefori/668194" target="_blank">📅 04:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668193">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4164e246.mp4?token=HtPSohcRTxL8ferwTyHDta5ILhv7aLikmnjiqW8Be_hFHeJrGrOw67TGyFUmfMUfYbHfKMuchnoSrFVPTSEr4qpjwaOXS3k5RR21AEF8FKUKyDuwEmc3e74qeiqoVaunBIvtvnHQMGurn1mNuyPx-PhmB7BEZJSJY6eWnLCIdDw8oPMDg9kD32AcQiYRNd0KSHlaSpmvAj2Nu_COZA_T9PKna8GGu2h5iRu8Vd7RNVeNKZKgAsJEOzs8f-6jQxUEhZIdtgfde0PBdup0FC_DQGMNdaNyoHd08BcuD8EQfBj8SUz71VJqGxBwOfb4fHpY8qSzJMZ7_M4gxTgZiMoLGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4164e246.mp4?token=HtPSohcRTxL8ferwTyHDta5ILhv7aLikmnjiqW8Be_hFHeJrGrOw67TGyFUmfMUfYbHfKMuchnoSrFVPTSEr4qpjwaOXS3k5RR21AEF8FKUKyDuwEmc3e74qeiqoVaunBIvtvnHQMGurn1mNuyPx-PhmB7BEZJSJY6eWnLCIdDw8oPMDg9kD32AcQiYRNd0KSHlaSpmvAj2Nu_COZA_T9PKna8GGu2h5iRu8Vd7RNVeNKZKgAsJEOzs8f-6jQxUEhZIdtgfde0PBdup0FC_DQGMNdaNyoHd08BcuD8EQfBj8SUz71VJqGxBwOfb4fHpY8qSzJMZ7_M4gxTgZiMoLGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طواف پیکر مطهر رهبر شهید انقلاب بر ضریح امیرالمومنین(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/akhbarefori/668193" target="_blank">📅 04:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668192">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfbc9752c8.mp4?token=RvB0x6oM7Ml6QEIDr30-tHUTjk3iKggry92ha_D-dwf5sPdydyqml6vILZEs4_dKGwel79ks7K28IoF5f6jgL6dIA4nvpQ-rKWu3hibVjmXH8723C6goaXAM27j-eoEqS27zI5BDrMlfZJCGdFD5aaNphCwplO1VOjnJiZYLX6_txOAcZ1Dxp-1GIfUHcXydVDK1vySCrA701Df1ZTZyyXudlKJGJvRbZRoHjpiJv8gUzgSMwNzKB3nop9A-ON6gBu0EsTR0SC2YHhSGFxTDLMMDYsuZz-NHiSeKCR_FMItVBdGH65UV_21M1ffSjAp-M-TzkMMZJigtRe_PEvhWYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfbc9752c8.mp4?token=RvB0x6oM7Ml6QEIDr30-tHUTjk3iKggry92ha_D-dwf5sPdydyqml6vILZEs4_dKGwel79ks7K28IoF5f6jgL6dIA4nvpQ-rKWu3hibVjmXH8723C6goaXAM27j-eoEqS27zI5BDrMlfZJCGdFD5aaNphCwplO1VOjnJiZYLX6_txOAcZ1Dxp-1GIfUHcXydVDK1vySCrA701Df1ZTZyyXudlKJGJvRbZRoHjpiJv8gUzgSMwNzKB3nop9A-ON6gBu0EsTR0SC2YHhSGFxTDLMMDYsuZz-NHiSeKCR_FMItVBdGH65UV_21M1ffSjAp-M-TzkMMZJigtRe_PEvhWYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر امام شهید در صحن حیدری شریف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/akhbarefori/668192" target="_blank">📅 04:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668191">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
شلیک موشک از ایران به سمت ناوهای آمریکایی
🔹
رسانه «میدل ایست اسپکتیتور» بامداد چهارشنبه مدعی شد که ایران چندین موشک ضدکشتی به سمت شناورهای جنگی نیروی دریایی آمریکا در خلیج فارس شلیک کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/akhbarefori/668191" target="_blank">📅 04:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668190">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293c50bc2a.mp4?token=tVJDpHqBo_hMlrZhyjQsYLTTEXnGlTV_IymlMEHa08Q27NspZZn8kuY96GXVdDECkxRFIEOuG_G1OjaH4i_a4z-aADTxElhRHnuQggvZgJ1tNrVt_Qzdf7JATYGuzjA-zbMm7WwmODDlN9T51aTfwuL6sMfajVgfrTf71xNgmdH2dD9sEC-G5mXm4myWBdu8w7QxrAGm6jTF88bxwAr71Y6gPa3KuFNRaGBBDEe3dZX2GExWjSHKixMz6E5Nn6khN2WU-X1CozyUfHfK09YI2tLMcURM2f-GyL6ufnMP0DxYj8GK12CXWOcGve74gw2_ercwnRRddTxwCoK22HG2VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293c50bc2a.mp4?token=tVJDpHqBo_hMlrZhyjQsYLTTEXnGlTV_IymlMEHa08Q27NspZZn8kuY96GXVdDECkxRFIEOuG_G1OjaH4i_a4z-aADTxElhRHnuQggvZgJ1tNrVt_Qzdf7JATYGuzjA-zbMm7WwmODDlN9T51aTfwuL6sMfajVgfrTf71xNgmdH2dD9sEC-G5mXm4myWBdu8w7QxrAGm6jTF88bxwAr71Y6gPa3KuFNRaGBBDEe3dZX2GExWjSHKixMz6E5Nn6khN2WU-X1CozyUfHfK09YI2tLMcURM2f-GyL6ufnMP0DxYj8GK12CXWOcGve74gw2_ercwnRRddTxwCoK22HG2VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعیت انبوه در حرم امام علی علیه السلام در انتظار تشییع پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/akhbarefori/668190" target="_blank">📅 04:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668189">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkcXN3Kzsqc-_6cvIoqpacId8cn2MhBYmVgeDrcrRik2MHXaXXKnno-2wDMeZd2ZxKq4uZww2LarrxEt0b6dbEHp675G39zWx-jFMKrvJEGRduKxDSIKtIp82Bwpv71iLKh5usJHErwTSesnWoRevVdDPD-K_4zGuH3j5GE7ZDCA1dXcE1Gxy_1_KT0_phP6iofIHJ8GNsz-kXjnez-kExZqIrSXGqo0eUeqGvzQU0cejxQJHh2zxv5kvwJJjFYWoh0Nl4H1mgnQ8wW6qvXaudyrDA3zO_7VkkFmGQzdINLvmc0qPqsQcaxAtFascAIkGfGOPWgWCS4Tsuar2TSsAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آرژانتین و فرانسه در صدر تیم‌های با بیبشترین گل زده تا به اینجای مسابقات جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/akhbarefori/668189" target="_blank">📅 04:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668188">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
پزشکیان عراق را به مقصد ایران ترک کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/668188" target="_blank">📅 03:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668187">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b564605731.mp4?token=DsjU6aP2Xzz_7MA14x6Bs6tcNaUQGYIWgP76tSRimrY8oeFUVee7KNTfsS8vZmpgyEBa80qgzyS0A-v_Vv9-ovMPPxOIGu311PUPnOcNQwdUn5z7xs6v6x-iqCu_YQB5wuNs6z6QG0Ul5GzvtHT9Wzq6O9Et0NkJRTbEdmm9A9dv0hCAWIHsWakmP6AyIjIbRjOYEuHax04htz5qiXweMbkjrjlBqvFlgtS25MYpyA5kpyZusgFBB2CfioHwztOAeuC2DFPze4xQhNlT9XQlKYeNcCpsXVxBZB5N2pU2r3ZZzNzKMQa7dLQb4jt_8pBrqcjhSTHdB0wXMZ8HqCqjGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b564605731.mp4?token=DsjU6aP2Xzz_7MA14x6Bs6tcNaUQGYIWgP76tSRimrY8oeFUVee7KNTfsS8vZmpgyEBa80qgzyS0A-v_Vv9-ovMPPxOIGu311PUPnOcNQwdUn5z7xs6v6x-iqCu_YQB5wuNs6z6QG0Ul5GzvtHT9Wzq6O9Et0NkJRTbEdmm9A9dv0hCAWIHsWakmP6AyIjIbRjOYEuHax04htz5qiXweMbkjrjlBqvFlgtS25MYpyA5kpyZusgFBB2CfioHwztOAeuC2DFPze4xQhNlT9XQlKYeNcCpsXVxBZB5N2pU2r3ZZzNzKMQa7dLQb4jt_8pBrqcjhSTHdB0wXMZ8HqCqjGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور اقشار مختلف جامعه عراق در مراسم تشییع پیکر رهبر شهید امت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/668187" target="_blank">📅 03:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668186">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2567d64ec2.mp4?token=XGaLwORlVOsujhgGO04qQinr93YV30ZcydiOl6cqnTfhw36SO_dtKBb308vSy95nEHdyH92mCpCjcjR4HdMK6aXZg3WEGWp_sipmyO_SpaohsD7d95aYmQl8J6jn5QHI9DQCAIpQklu1qRjE3Qpzvpl4CZXL_PTvQI7krDkC84uSaDQaXYFusM4oLGVkDT6lGwDw5WUlrsHki4egx-vXVMMelhFdhW2Ytc1snC7hWO1XvOb_1d0kS9-pt88qFlB8MV9UtN69NPscFJ3LVKxXFtXPbXWTQ8RsRFYCH1PPvjTFl-wnNQzj5-ye5881nr7XlV0bggcjiKCS57HtzJ8wEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2567d64ec2.mp4?token=XGaLwORlVOsujhgGO04qQinr93YV30ZcydiOl6cqnTfhw36SO_dtKBb308vSy95nEHdyH92mCpCjcjR4HdMK6aXZg3WEGWp_sipmyO_SpaohsD7d95aYmQl8J6jn5QHI9DQCAIpQklu1qRjE3Qpzvpl4CZXL_PTvQI7krDkC84uSaDQaXYFusM4oLGVkDT6lGwDw5WUlrsHki4egx-vXVMMelhFdhW2Ytc1snC7hWO1XvOb_1d0kS9-pt88qFlB8MV9UtN69NPscFJ3LVKxXFtXPbXWTQ8RsRFYCH1PPvjTFl-wnNQzj5-ye5881nr7XlV0bggcjiKCS57HtzJ8wEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهیدان سید محمدباقر صدر و سید محمدباقر حکیم، حالا میزبان آقای شهید ما هستند...
🔹
تصویر نصب شده در نجف اشرف به مناسبت ورود پیکر مطهر رهبر شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/668186" target="_blank">📅 03:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668185">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bce9bc8fdb.mp4?token=UWm1VlE9_1_MipI3pyH-AAoibxk6bfsK5MnYhGNY5hef31xnCaUtdV1Pl-hKj-F_dkcn6W1XANg2SArbOxsv6l6RlD7LAL2pxix_yIYSlU2xPwAm07wX1_vKeby7ZZnr23fCND8UJzpNes3eJHEreF2uTB4pmZUXeLb0VjEtGJSMP8c93GMnd2OXdFHmO6jmUeszBbcw_4WtyRiMaEweNgGJTytP8hEi5yi97N7UAaRoptupLwuzPQSECnbePy43hk7dujhNDrFOv8qXGZfzNeZvFZtEV12LP_DDMVdF0Knr60LaJLFltZcIX6m3-gT_NLb67uKlxkJ9CcfGj3w0vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bce9bc8fdb.mp4?token=UWm1VlE9_1_MipI3pyH-AAoibxk6bfsK5MnYhGNY5hef31xnCaUtdV1Pl-hKj-F_dkcn6W1XANg2SArbOxsv6l6RlD7LAL2pxix_yIYSlU2xPwAm07wX1_vKeby7ZZnr23fCND8UJzpNes3eJHEreF2uTB4pmZUXeLb0VjEtGJSMP8c93GMnd2OXdFHmO6jmUeszBbcw_4WtyRiMaEweNgGJTytP8hEi5yi97N7UAaRoptupLwuzPQSECnbePy43hk7dujhNDrFOv8qXGZfzNeZvFZtEV12LP_DDMVdF0Knr60LaJLFltZcIX6m3-gT_NLb67uKlxkJ9CcfGj3w0vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزاداری عراقی‌ها در کربلا و دعا بر آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/668185" target="_blank">📅 03:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668184">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52d30bf222.mp4?token=KIlyXA6LiJYCsl0odDa6PkhNsA0a91edkol3m3T9TdWz_qlx1C10XkdQWo4UPwsdtnV_dIdGXZS72GmxdlO8yqS0HOyqIafxvUiruQBnq1urwUkeQ07U0t9wfSmBHDndWuosN7Cgo_WDYPmD0W_84Qp-jg7rxZqcdm4qJL7L6U5kmAZSKLs3Yu0FMFlb6GiFG87vRd3L65AvlBQHSBwzsUaLmDm-cMW7VoVGAZuoVSsie11gcU7IAk55nD6av8LMsSvZb1ttUTCofioLPs72nzOnkOEIFjsJNtu98Mrp2WwlZ_TxJz4EIJgstm9CEBATdv-sBKaJiIKjfXm7iSqbDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52d30bf222.mp4?token=KIlyXA6LiJYCsl0odDa6PkhNsA0a91edkol3m3T9TdWz_qlx1C10XkdQWo4UPwsdtnV_dIdGXZS72GmxdlO8yqS0HOyqIafxvUiruQBnq1urwUkeQ07U0t9wfSmBHDndWuosN7Cgo_WDYPmD0W_84Qp-jg7rxZqcdm4qJL7L6U5kmAZSKLs3Yu0FMFlb6GiFG87vRd3L65AvlBQHSBwzsUaLmDm-cMW7VoVGAZuoVSsie11gcU7IAk55nD6av8LMsSvZb1ttUTCofioLPs72nzOnkOEIFjsJNtu98Mrp2WwlZ_TxJz4EIJgstm9CEBATdv-sBKaJiIKjfXm7iSqbDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار هیهات مناالذله عراقی‌ها در حرم حضرت امیرالمومنین(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/668184" target="_blank">📅 03:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668182">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe2e701a0.mp4?token=S52PmKkU07mEPqBjXqwsCelmB7k9-orMnqU7po8bDRetftRxBhob5j5K-JDknHH9sEwgpirV7_8NxII3rBPB2Suk-66_kKeaDURKVtPqWG7Qb1U-rMsFJjjV-vnpLwsvSCghxmG9nHo4CYdPxDABbojnnEM2CuTOtcomAkV_a3uU1jiqI2CVIzSvarRGg3l-2sk0LbOJ9V8tGdJFLW115Ftv90soTUHhYvg5LY9jaKjmQlnZmc8GLWnV4uQ25huEGFfTWx6fWRreloBgXfT0HBpp0XkMCh3hFRWJhCHoZzusLVoyEJzvlBccaSb21d8WFRVkVHkts74Ylvg_7wPBAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe2e701a0.mp4?token=S52PmKkU07mEPqBjXqwsCelmB7k9-orMnqU7po8bDRetftRxBhob5j5K-JDknHH9sEwgpirV7_8NxII3rBPB2Suk-66_kKeaDURKVtPqWG7Qb1U-rMsFJjjV-vnpLwsvSCghxmG9nHo4CYdPxDABbojnnEM2CuTOtcomAkV_a3uU1jiqI2CVIzSvarRGg3l-2sk0LbOJ9V8tGdJFLW115Ftv90soTUHhYvg5LY9jaKjmQlnZmc8GLWnV4uQ25huEGFfTWx6fWRreloBgXfT0HBpp0XkMCh3hFRWJhCHoZzusLVoyEJzvlBccaSb21d8WFRVkVHkts74Ylvg_7wPBAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودروی حامل پیکر مطهر رهبر شهید انقلاب به صحن حضرت زهرا(س) در حرم امیرالمومنین(ع) رسید.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/668182" target="_blank">📅 03:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668181">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ادعای اکسیوس: یک مقام آمریکایی گفت ترامپ طرح حمله به ایران را تأیید کرده و
امروز، در حالی که برای نشست ناتو در ترکیه حضور داشت، دستور اجرای آن را صادر کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/668181" target="_blank">📅 03:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668180">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
جدیدترین جزئیات مناطق مورد حمله در جنوب ایرا
ن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/668180" target="_blank">📅 03:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668179">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6976fab17.mp4?token=F4Dfj3Q0DxD-LkgoGtaK_K99jYgbaVEtQ20SrW8dVHdmv2DHflj_Qz9tnDLk3TX79xM6Ncon7o5Bfyd7gbHphkV5k1Ns1mB1TISlgraPM1szYFuJzQ6TDqYnchXvFLKVHl0KMSPVzhnOGRu-9sovGX9NLi7YEnDGC-FcveZYs3BfHlRgU-nrmmb8Pdf0Egma48-HDNDMj2uaVRZaJz9OYPnDeWBCjToSuWnP2scj1GhjJvYSu4GTc_INVu_LLcOjmlHipiXDj8qw8Mv7gfRapDUjMjIb3nnYsJvRUH2CYXRKBknRQl3puA-ppVdZKkWZXeFnogw6FIERnJtQfWKVcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6976fab17.mp4?token=F4Dfj3Q0DxD-LkgoGtaK_K99jYgbaVEtQ20SrW8dVHdmv2DHflj_Qz9tnDLk3TX79xM6Ncon7o5Bfyd7gbHphkV5k1Ns1mB1TISlgraPM1szYFuJzQ6TDqYnchXvFLKVHl0KMSPVzhnOGRu-9sovGX9NLi7YEnDGC-FcveZYs3BfHlRgU-nrmmb8Pdf0Egma48-HDNDMj2uaVRZaJz9OYPnDeWBCjToSuWnP2scj1GhjJvYSu4GTc_INVu_LLcOjmlHipiXDj8qw8Mv7gfRapDUjMjIb3nnYsJvRUH2CYXRKBknRQl3puA-ppVdZKkWZXeFnogw6FIERnJtQfWKVcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی حیدرکرار انتقام انتقام
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/668179" target="_blank">📅 03:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668178">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62c1a1ba88.mp4?token=i8O3uk6UR5nJ21gskMFb-WVVKGzDZ9bTa_s7Ts1UyI9y11UgJb3i_SsWd-AX4pTJLMDfe60hkW3S4iARFOWPFD1bdBddHSxOiDPqjaIUmelI0Uez0U6DpvozwVvWW5OzaLWeEq0-WpXLnDPPTro4PzyoZti4Sr-txGQOXZInTnBt5glg-afG5CawbdKyAWJShT7NnAclagwjUcPtCYYB-v_Lap7dEstXXUMVjet0pGSiuk5cgx_Rze0sULUvtoiTXfXUhYGtQepUlQ3tPsVBQI52PpuuQN8Qp9n0E2K5Enm6ybsLJWy_Fqf9qaYvFJFe3fCpZCto671a5CYZnXgoOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62c1a1ba88.mp4?token=i8O3uk6UR5nJ21gskMFb-WVVKGzDZ9bTa_s7Ts1UyI9y11UgJb3i_SsWd-AX4pTJLMDfe60hkW3S4iARFOWPFD1bdBddHSxOiDPqjaIUmelI0Uez0U6DpvozwVvWW5OzaLWeEq0-WpXLnDPPTro4PzyoZti4Sr-txGQOXZInTnBt5glg-afG5CawbdKyAWJShT7NnAclagwjUcPtCYYB-v_Lap7dEstXXUMVjet0pGSiuk5cgx_Rze0sULUvtoiTXfXUhYGtQepUlQ3tPsVBQI52PpuuQN8Qp9n0E2K5Enm6ybsLJWy_Fqf9qaYvFJFe3fCpZCto671a5CYZnXgoOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیابان‌های نجف اشرف قبل از وداع با رهبر شهید امت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/668178" target="_blank">📅 03:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668177">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4d8e44b3.mp4?token=t4W84x7yWNpSK_OEnpyLq8dDAqcBTQil1wXnnvWxZXY_TXTp5n9lazrSrxiGzM09yaO26og3YTTQruEkEAGT3214wYSSfezFpZpxYgktWT09fWYaHPGy12yU1sZxLiw_xjqnHCjVgm9wK36txDYYHgKm8GXl6Mq9afduMVJsEdFadKPD9rCiZ-PjZIUlua5NYZgzBokh_RBBgoUDOyE5yMqxxzHidj0SWGSYcuOv2p9NGgdQS_BQTbQCkLBMgVIHeod9M6FOWAHdUyV_I4JcQugkAIvu3X3jKoEc6FrPZLE84Km4lp4BHpdd910DKKJq_EJJhLwBiHOUVCOmMUMoXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4d8e44b3.mp4?token=t4W84x7yWNpSK_OEnpyLq8dDAqcBTQil1wXnnvWxZXY_TXTp5n9lazrSrxiGzM09yaO26og3YTTQruEkEAGT3214wYSSfezFpZpxYgktWT09fWYaHPGy12yU1sZxLiw_xjqnHCjVgm9wK36txDYYHgKm8GXl6Mq9afduMVJsEdFadKPD9rCiZ-PjZIUlua5NYZgzBokh_RBBgoUDOyE5yMqxxzHidj0SWGSYcuOv2p9NGgdQS_BQTbQCkLBMgVIHeod9M6FOWAHdUyV_I4JcQugkAIvu3X3jKoEc6FrPZLE84Km4lp4BHpdd910DKKJq_EJJhLwBiHOUVCOmMUMoXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درهای حرم مطهر امیرالمومنین(ع) به‌منظور آماده‌سازی برای استقبال از امام شهید بسته شد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/668177" target="_blank">📅 03:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668176">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ffdade163.mp4?token=l0XagTPd4p2KO2NelmH_UWMcjzGERP7BZd-NCDIO-0bHOg2D-4_iaKj3Knz2-A050jhqzLDEZo_2fbE_JG6wLTnAGgIfE_-4DAJYKsmlIkieRCZ2fTBAYvO9RFropwpFIhadF6drTdP0G59ymuRgplMujarz8EFtVU2GCMhkD_YgWIET8q2BSMXOjRHMqBM6inlg6MdTvfyKSnhQ2jlTu6D4Uc-ddB-IorM3fweQLUJDZ46jZFaqi-Z8IdlyLuAdJZ46lI_pwt2g3EapNHgJtRfYRgK106GITkHEnRiz5XfsFnCyxc3qO2LoqvXeML7bRDu99YxTVEawqWraNvB7iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ffdade163.mp4?token=l0XagTPd4p2KO2NelmH_UWMcjzGERP7BZd-NCDIO-0bHOg2D-4_iaKj3Knz2-A050jhqzLDEZo_2fbE_JG6wLTnAGgIfE_-4DAJYKsmlIkieRCZ2fTBAYvO9RFropwpFIhadF6drTdP0G59ymuRgplMujarz8EFtVU2GCMhkD_YgWIET8q2BSMXOjRHMqBM6inlg6MdTvfyKSnhQ2jlTu6D4Uc-ddB-IorM3fweQLUJDZ46jZFaqi-Z8IdlyLuAdJZ46lI_pwt2g3EapNHgJtRfYRgK106GITkHEnRiz5XfsFnCyxc3qO2LoqvXeML7bRDu99YxTVEawqWraNvB7iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یزلۀ جوانان عراقی در سوگ رهبر شهید انقلاب در بین‌الحرمین
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/668176" target="_blank">📅 03:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668175">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2c0b2f180.mp4?token=syZarHVUVsoWtcw9ikMyLtqUVEqowwQJYAE_kjYeQk-GF4p6o49biogbqZDe3Qu755H56k1aVNV6pTmxlAAgdoD5zXljnixhaTbO7jV7ywmGtMHbGcr8fLeYhi2kYswsaYml4N2wLU1FnwK6aNL_OUdbrJ20y9uxiKmhNtpyq5d0k4XgOGUOy7GojLF88iklPRXkL8as3Tjm_BvUPlJtrVDzMJX3kfUOPGlkST8x2Uoo4fUZN0ooAwxxDn5WT5QWE0GHNltcIf8aLTI1lXsF_2cgOyMJWeBQYj9X_RETnvJ2WRKOlJ2Pk1_iJ_Qn3nT6PXZaZpOdZXupL9_Z4Bdtuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2c0b2f180.mp4?token=syZarHVUVsoWtcw9ikMyLtqUVEqowwQJYAE_kjYeQk-GF4p6o49biogbqZDe3Qu755H56k1aVNV6pTmxlAAgdoD5zXljnixhaTbO7jV7ywmGtMHbGcr8fLeYhi2kYswsaYml4N2wLU1FnwK6aNL_OUdbrJ20y9uxiKmhNtpyq5d0k4XgOGUOy7GojLF88iklPRXkL8as3Tjm_BvUPlJtrVDzMJX3kfUOPGlkST8x2Uoo4fUZN0ooAwxxDn5WT5QWE0GHNltcIf8aLTI1lXsF_2cgOyMJWeBQYj9X_RETnvJ2WRKOlJ2Pk1_iJ_Qn3nT6PXZaZpOdZXupL9_Z4Bdtuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای خیابان‌های منتهی به حرم امیرالمومنین(ع)، ساعاتی پیش از آغاز مراسم تشییع رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/668175" target="_blank">📅 02:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668174">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
سی‌ان‌ان: وزیر جنگ آمریکا روز چهارشنبه به اسرائیل سفر می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/668174" target="_blank">📅 02:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668173">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
صابرین‌نیوز: هزاران نفر از عزاداران عراقی در پارکینگ‌ها منتظر هستند تا وسایل نقلیه برای انتقال آن‌ها به کربلا فراهم شود تا در مراسم تشییع پیکر امام شهید شرکت کنند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/668173" target="_blank">📅 02:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668172">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66cc907b68.mp4?token=LsES1L1pX0KUKOowCmHrqy_dWnkKpGThTZrIwMbs3m3g7HQxgtm931FUqHiTJI3yEfOjRxRJCwJDG-WhImeyCHzQAD54t2gj3J88n4kybxJ6GTxD1jXTkaMW6jpTz9A-n1e_D2Zmt-_iiOaDvZhnP7UWAMGERMMTDyhjKSvQhV03mpNAIVwHv_4BLYiHteU1Hgx_XBdCIzuFfR1RJ-k5xcNVjQXEvxqT8CvdB2SSSjXjUVfyQPfjE7TFsUh_3fERYX81KOdyvSNfYyHW2a7vZVpz7FLjHwyrz8DtQFo73G38ciyiEF0KLnqAuisHIMKRb2qX1x9sAw2RsAAMFhEgGoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66cc907b68.mp4?token=LsES1L1pX0KUKOowCmHrqy_dWnkKpGThTZrIwMbs3m3g7HQxgtm931FUqHiTJI3yEfOjRxRJCwJDG-WhImeyCHzQAD54t2gj3J88n4kybxJ6GTxD1jXTkaMW6jpTz9A-n1e_D2Zmt-_iiOaDvZhnP7UWAMGERMMTDyhjKSvQhV03mpNAIVwHv_4BLYiHteU1Hgx_XBdCIzuFfR1RJ-k5xcNVjQXEvxqT8CvdB2SSSjXjUVfyQPfjE7TFsUh_3fERYX81KOdyvSNfYyHW2a7vZVpz7FLjHwyrz8DtQFo73G38ciyiEF0KLnqAuisHIMKRb2qX1x9sAw2RsAAMFhEgGoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم اکنون «میدان الصدرین» نجف اشرف با شعار: یا سید فراموشت نمی‌کنیم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/668172" target="_blank">📅 02:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668171">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3Tj3eKVcohBoRKZ-u3Zb0kKl3Wv9D4Up-DGwyyF6H1-t6Ysmj29nokJA6OHunZDDruGcBxg_82eCC_aswTkV27ZSeaTQMoX5pcE666jPkkaXQaJQ76QDB8-dXzjKt7s49R6VZ88RIXhlsnxtu-Zy4-QYAwIKX8uYgKq3yZkv5UB4aujvgA67PCSPBflBle7vQUULhsnJwTzvbQVtUHVtmYFFFejKrNDyF6v-3EF1EAFCW8x3oMdDIujr1L-4HdXrvjWu4GnXH4H_yBs1w_kMC3nHszeBTNayfWAlATNYSUw4xOHiOWtxapU4L0k91m1dkbKptv_M_Rn8gbLhjYvRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
خوشامدگویی متفاوت عراق به قائد شهید: «خوارکننده آمریکا خوش‌آمدی»
🔹
«هلا بجیتك، مذل امریکا و التطبیع: خوش آمدی ای خوارکننده آمریکا و سازش.»
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/668171" target="_blank">📅 02:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668170">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80c67bdf1.mp4?token=Z7cecCQ84c_SGB1uY-wSLfXXRF_w7BekbDl-3EN5supAdF_rU97BrvoqRZf1C8c5KgmH_36dJm32onuiQMODCQi2MAH6B1lvOgTTcoi6ANYRrf_fAj-NgwbD6InoiNgQEvUZ9no4JNlTg-D78IImEIkM_zq5ARkSr1WBO5OZ7yHuZ2n6zw3b2s_VYUXwkEV9MXb4I41OLiPfyqEYSOo7Zqb6Nn3pJzmYV-OqXxQtoicwXFFop3RwagNvV6LJccihHhN5vvyRAyJ18D7XC51es1RUnBhX35N7r94kaj-REGGTWMiAvJ-YVW1hAUYBQx-9_oP1upfE62hvcDlPguebyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80c67bdf1.mp4?token=Z7cecCQ84c_SGB1uY-wSLfXXRF_w7BekbDl-3EN5supAdF_rU97BrvoqRZf1C8c5KgmH_36dJm32onuiQMODCQi2MAH6B1lvOgTTcoi6ANYRrf_fAj-NgwbD6InoiNgQEvUZ9no4JNlTg-D78IImEIkM_zq5ARkSr1WBO5OZ7yHuZ2n6zw3b2s_VYUXwkEV9MXb4I41OLiPfyqEYSOo7Zqb6Nn3pJzmYV-OqXxQtoicwXFFop3RwagNvV6LJccihHhN5vvyRAyJ18D7XC51es1RUnBhX35N7r94kaj-REGGTWMiAvJ-YVW1hAUYBQx-9_oP1upfE62hvcDlPguebyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از رهبر شهید انقلاب در خیابان‌های عراق
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/668170" target="_blank">📅 02:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668168">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XCGz2_-Lu3xF5iE5GpWqObpLnihmT8x0UXEPdLKVtU3hhh2u33sfCzZYlsbvhRv584_vtHPjSZoQajilOWo04yz8dDfScY_SbOfthIX8WifgKuZszREZUb4IgrXYoFdtsVk5YPtrJRQ3C6XpDu73vMD_lXxuMuXfQ-c42DSC5r3snf8_pGIoNgdoC9C1wYfy4TKuf7qEIM7YHELSQE3I_wp1sX79O7GqTuawlAUWo6dhWQi0Zu_jn72yNwNDFmCnQUbGOYO_ajKkD1G3U1_r28KiP-eta5LaqOIX53dzJW9XoXUIOiOq7UT6u7Wz1dKjVNBz6ccJnJ0X-SA2VeXXuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xr_8qt1j8vaPIlrygMfP-EeyvrLJQ6upQ_OZ0WdIlp_0xOS9Gnv6yIS_YUaQL8pXi5IZt_65lcnaJraVdBuTDWd8X8y358nB02RNtASTa_zXiUhVdmT0UYnUUI2yGMWWB5P6_qmxrzMmr8lDQA0gdnvD3Ih3u3rqZkT64Hl1XthbsVBSVBcxcCZ7rKUpw7FWIprBvbMAb9CwZMf4Z93LHGBgItEvP16rm-0p0tALD35z8O1k3ZnnkyzV2zswPUjq5Dp8bxfed9aYdzypFlO0i7u0w5HFtaoq7BHDOmqN1QobChV9j1igtW3GVb7SGXYAAMQ0ftlfPjocnrKHD9OjbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر منتسب به آثار حمله جنایتکارانه دشمن آمریکایی به جنوب کشور
🔹
اصابت بمب رژیم تروریستی آمریکا به یک خودروی حمل و نقل عمومی در بندرعباس
🔹
ستون دود بندرعباس ناشی از حملۀ دشمن به شناورهای صیادی مردم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/668168" target="_blank">📅 02:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668166">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDQpbhGXQFP_oNJJU0GMFkS5HEq-LJuyCRO7Tds93eM8lrBTeK6sl_EIz6zOZzWjsLlfPDFy8OpO2T7nEIU2n1gYr3_-1h-O7jzKPyqb3kAarO3s4cfEzEt_cI8lcttCWCBTfCrgJzV9vfGXAw1-9rnH51N1nXQGU-YyUNqCr4WuGl6la2QJDNF2lSrDGYplgnwVwViAb_rdW6eG95nUQSkQlY0kFotajjZ2wsp1QBp72cI9jhJAIvNdri7pEEsbFWkYP81cSh7rrUS_f-uMpkA2kecW5qmVIj4rTUtNlfZbkFsRdUsbiXmFQtif0Fj_jB9MD7KeBNL-adKN_YGYvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z0sstLduzFHLiefsrSaVcV-R6qyrdGP7QbnZgdrEk9jlBkFwRl1muKvmxAsfrlvBz93CjR7in-DRrB7mejcETx-BAcgVPHp1VNcFRhqBZA8am6ThbHAXP0EW3uylZSr70UKNnCYlw7D0Vc_310nGkh3a9SWvhZ6QYHhiACjmfDxKMlcCZYGz5OiTSM7NJfopFAItQJPtJmkI1ZDVgp_5utOFArGLjIwelvEQuDSRkTAAtXmXkAyArGLD6SF3ZprVMxyL-YbaJ1mHd28EaPRJWgvuN8zQwZ3R24L3_P8s0cu1H3UhRZF3JmI6SnIT6nZEtnSydE5s8LE5N6mbTLSgRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
استوری محمدرضا شریفی‌نیا و هادی چوپان به مناسبت تشییع رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/668166" target="_blank">📅 02:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668165">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f11883d2.mp4?token=BUGfFhNsQLlWqI0RTcmw6NfXw91yaC0IC62YVhXe93C8KtnrKljC2jFZn-QShdx6nttzo9KyBUPFBu7e7LAt3aLStEnKZbyPT61VOvW45k6xlwfVtvvn8554Jmac_ssDUCU2veTj2v7XDQ-TrwXlI4uyc7SN7RiE-1-DMsh1A0phViGlwJBqtkvTMWcebk837PPATpLXcRdYoseTNaIkiGB3cB6ny7eUqJEgE0MtVKi4G7Ofv0qm3V5j6KIdUmuSSfnYsgIYgZ9klfEbgsukDf5TjrUTUG1xXF7UFkMXpbwFMHaSGJUJxkxDFpfVAv2R3GRI-lU6M3QVN_7Qa-7e4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f11883d2.mp4?token=BUGfFhNsQLlWqI0RTcmw6NfXw91yaC0IC62YVhXe93C8KtnrKljC2jFZn-QShdx6nttzo9KyBUPFBu7e7LAt3aLStEnKZbyPT61VOvW45k6xlwfVtvvn8554Jmac_ssDUCU2veTj2v7XDQ-TrwXlI4uyc7SN7RiE-1-DMsh1A0phViGlwJBqtkvTMWcebk837PPATpLXcRdYoseTNaIkiGB3cB6ny7eUqJEgE0MtVKi4G7Ofv0qm3V5j6KIdUmuSSfnYsgIYgZ9klfEbgsukDf5TjrUTUG1xXF7UFkMXpbwFMHaSGJUJxkxDFpfVAv2R3GRI-lU6M3QVN_7Qa-7e4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزارت برق کویت از قطعی ناگهانی برق در نقاط مختلف این کشور خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/668165" target="_blank">📅 02:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668164">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOLGEJhK8-ImQA1tUOnNhimNtfffSqXbJEF305WlsJ1-8TcE0Lj5HAoAbKdSuDWD_KirjefGvwQvPGXuQ_SgmjBNrPjoNlN2N32DgDHJAvTk3Bu-yb-637hyQXG2-sYQkWXsog3UONbrVLY4EAzVylOtm2cKJRW6CsWEvFjUweE3ONzEBnvefatxLxuSQBDk9Xe1mCJa9d0hKUGRUFebhekEzYdhrM2w99p5MB2ATO-y83Muc2jYbFfLobwZ21in8zFG2R2dPcZcEiZmdUa7Yocakm3fvlr5c_aJ5pNPQ0eS1Nhj9PS7m1yS1CnWJGj7bpHlYwqA2TR7k-sp8TLgaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمودار مرحله حذفی و یک‌چهارم نهایی جام
جهانی ۲۰۲۶
🔹
شش تیم از اروپا، یک تیم از آفریقا و یک تیم از آمریکای جنوبی
🔹
بازی‌های مرحله بعدی، پس از یک روز استراحت آغاز می‌شود.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/668164" target="_blank">📅 02:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668163">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
چند نفر  بر اثر اصابت ترکش پرتابه دشمن در اسکله تجاری شهرستان سیریک مصدوم و به بیمارستان میناب منتقل شدند
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/668163" target="_blank">📅 02:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668162">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a1db4c83.mp4?token=eeXrSyuYdwFoF8pZ_G9OyXBNvYUnAyB1m_pvrXYRIvAnM_PdB08Cs5KQwH0_bVZUEFZIXP-jtymQzS4v3gL1CSTBEu7t9Do4s-1vVls5WOE7pri3EE0fwxoyjoDfz6-XPXLy7obc048LbEYVwmZFiYnPTzDlN1z0tw-K1D05k8LrBNADTFUMTP25xi908JEOCWt-GDYGwIZg7Hp03xHU3iZU7bkZQdyNmsKrj0pDbvmuhz9nZI-PR1wJ7Qqq7-uxLLL16y3rpy3DQmwtvlGuL4Sw2WeJIwXZPWWxLhedarbqu4QGowjlHbS-JwQ3QCZg7UJWYUY3HDXQy8G0-cncIQ3ZthjRX3Va6yIOv4jtXew9Ny87Tyyr1u4zJZb2bQDGiHLCZasaokn4-9t_6LrJT2yu6WmUJU8HhlqvLPEtR4J0QfccGXRaoQcVFkteBwBpKDCITZzMHrZj02uaSh6XzYPRH67O-z1Fclnr1mbnKACYLeDQyETRSY50OJ4dMn2mybnPud6eC_f5Ml53ubfG6WAh4bo8On01b5OsSy0-dCf037T_uWKNvIlx92UOHNoN4GlQ2QTo2MffL381EIzl_-cTXCb0V_6FuydUQhnNDX7WbXYEaSWCOwKk8k3LWogrZRsX7i20YFc66PZbw3yVITBtDj_GxLFz5M4ioMhjyXo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a1db4c83.mp4?token=eeXrSyuYdwFoF8pZ_G9OyXBNvYUnAyB1m_pvrXYRIvAnM_PdB08Cs5KQwH0_bVZUEFZIXP-jtymQzS4v3gL1CSTBEu7t9Do4s-1vVls5WOE7pri3EE0fwxoyjoDfz6-XPXLy7obc048LbEYVwmZFiYnPTzDlN1z0tw-K1D05k8LrBNADTFUMTP25xi908JEOCWt-GDYGwIZg7Hp03xHU3iZU7bkZQdyNmsKrj0pDbvmuhz9nZI-PR1wJ7Qqq7-uxLLL16y3rpy3DQmwtvlGuL4Sw2WeJIwXZPWWxLhedarbqu4QGowjlHbS-JwQ3QCZg7UJWYUY3HDXQy8G0-cncIQ3ZthjRX3Va6yIOv4jtXew9Ny87Tyyr1u4zJZb2bQDGiHLCZasaokn4-9t_6LrJT2yu6WmUJU8HhlqvLPEtR4J0QfccGXRaoQcVFkteBwBpKDCITZzMHrZj02uaSh6XzYPRH67O-z1Fclnr1mbnKACYLeDQyETRSY50OJ4dMn2mybnPud6eC_f5Ml53ubfG6WAh4bo8On01b5OsSy0-dCf037T_uWKNvIlx92UOHNoN4GlQ2QTo2MffL381EIzl_-cTXCb0V_6FuydUQhnNDX7WbXYEaSWCOwKk8k3LWogrZRsX7i20YFc66PZbw3yVITBtDj_GxLFz5M4ioMhjyXo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین جزئیات حملات به جنوب ایران؛ وضعیت در شهرهای بندرعباس، سیریک و قشم عادی است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/668162" target="_blank">📅 02:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668161">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
پزشکیان عراق را به مقصد ایران ترک کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/668161" target="_blank">📅 02:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668160">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJ1z7ostftUERTJZH46gVdaUSYCzV9NIpo_jN2fnkBg_Wxv70COmwrtn8QogDyQ418W8S1TcYBVc7AbXLfjfqPrnprzKYDqfbMN8kVxccijddQd7vUwALrrEUn9MdAqkK2qgIkpK0xn3LoMEcKxwZoXTgmeGxksMUPN-2mzX7Y_k74-OMzT25TSfd-akYYQTtN9sXkrX3WacDbAWwtwD9qa-h42PZbkXf-xj9oK3mrSonjtoK4_w4vDKB_tZiLJsKyq7rjZ06xOEgQx_VXnvHn6jVD8kdQ31vQMJ7qw25q49RLmhYN2j9EDDUzBESsr8ra1CG3chgDZxgIb4T-SLUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جام ۲۰۲۶/سوئیس در پنالتی‌ها بلیتِ دوئل با آرژانتین را گرفت
🔹
سوئیس ۰ (۴) - (۳) ۰ کلمبیا
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/668160" target="_blank">📅 02:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668159">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eec577fb73.mp4?token=Nz19eEfCTnQ3jUFcXfSFC22v6kY_95_oaP-XAx-adCnnXTlw6ZPi1zb1YwW8XHHBjGcA-0Z-6bRhBlDsK9p6Td8gKQEcfssBkLpCrjZCuyN-X4hBCHVRuRkI8Zkh1iOKYbXTB8MOHsDGuz7sXNLX1Gw_VQjmOCxbngwX8gQWcNX5qduFm8x24b8ell29_VKJVVNlSATOsDN8TzWeVip8FxYfOsxgYMmGpYwfpU6ZmYSWSRlHCqLg8-PSgUB8713_QAvcRwRrynsTOO5oGLFclCL0cJ5oBF4XE7CNe0qvfbACFodn6SmtNE5lAMDK8jKP01f9W8qkVuAjaRqU15Aw5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eec577fb73.mp4?token=Nz19eEfCTnQ3jUFcXfSFC22v6kY_95_oaP-XAx-adCnnXTlw6ZPi1zb1YwW8XHHBjGcA-0Z-6bRhBlDsK9p6Td8gKQEcfssBkLpCrjZCuyN-X4hBCHVRuRkI8Zkh1iOKYbXTB8MOHsDGuz7sXNLX1Gw_VQjmOCxbngwX8gQWcNX5qduFm8x24b8ell29_VKJVVNlSATOsDN8TzWeVip8FxYfOsxgYMmGpYwfpU6ZmYSWSRlHCqLg8-PSgUB8713_QAvcRwRrynsTOO5oGLFclCL0cJ5oBF4XE7CNe0qvfbACFodn6SmtNE5lAMDK8jKP01f9W8qkVuAjaRqU15Aw5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برق برخی مناطق در کویت و بحرین قطع شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/668159" target="_blank">📅 02:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668158">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
بر اساس گزارش‌‌های اولیه، حمله امشب رژیم تروریستی آمریکا در استان هرمزگان عمدتاً تأسیسات و موقعیت‌ هایی را هدف قرار داده که غیرنظامی‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/668158" target="_blank">📅 02:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668157">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca00dc6e4.mp4?token=d6fMQoHIl-am9nS5Aw9QWfvU80LOlvlaY4MMIgEEqEwg5D8__yohrYOebOEfRAXSG1ps7-AKfBDH98POElGSPT7bKLl4tEbYtS6gbo4sDgr3yhVpLoUp2q2GLz1KFXCI0nG87BUchS7It0CLrtGrP2xNjzo02rONlnj59KjfZ4PFs4TTPChDYC7cKRL3CzVOsaEcZRXgz9U5fNfLIJUajcqFsraffG0bmCxHt7jfTXDXVPrI-FfceecUroCrzZRZIn0DB8i32pSy28LZ2RCRLQs_H2kaL0gwwLKSPOYrxVHKGR3lrGjY0--daeNl3zJPKg_ANAEMk8iw6mLypCKoSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca00dc6e4.mp4?token=d6fMQoHIl-am9nS5Aw9QWfvU80LOlvlaY4MMIgEEqEwg5D8__yohrYOebOEfRAXSG1ps7-AKfBDH98POElGSPT7bKLl4tEbYtS6gbo4sDgr3yhVpLoUp2q2GLz1KFXCI0nG87BUchS7It0CLrtGrP2xNjzo02rONlnj59KjfZ4PFs4TTPChDYC7cKRL3CzVOsaEcZRXgz9U5fNfLIJUajcqFsraffG0bmCxHt7jfTXDXVPrI-FfceecUroCrzZRZIn0DB8i32pSy28LZ2RCRLQs_H2kaL0gwwLKSPOYrxVHKGR3lrGjY0--daeNl3zJPKg_ANAEMk8iw6mLypCKoSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرتاب منور توسط ارتش رژیم صهیونیستی بر فراز ارتفاعات «علی الطاهر» در جنوب لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/668157" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668156">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
المیادین: توپخانه مستمر اسرائیل حومه نبطیه الفوقه و مفدون در جنوب لبنان را هدف قرار می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/668156" target="_blank">📅 02:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668155">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
ستون دود بندرعباس ناشی از حملۀ دشمن به شناورهای صیادی مردم است
مدیر بنادر و دریانوردی شهید باهنر و شرق هرمزگان:
🔹
دود سیاه در پشت بازار ماهی فروشان بندرعباس ناشی از اصابت پرتابه های دشمن به اسکله صیادی بندرعباس و آتش گرفتن تعدادی از قایق های صیادی مردمی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/668155" target="_blank">📅 02:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668154">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce85279956.mp4?token=NUsd_auz03zc2OoEfUyaZrz6hE8QbRxQ8omQyz74RFgAKbVB8UauZkj9byW5l0fFwMLQyaSxIahyqNA5U0mV9MyLFlDVI0drTM1yQFBn0crXwBZa_7BiIbF59Dxub2NzJ96osM8M5XcXRZhQtdTYz2vGl7fEAHwAa_1uAuSMkHB-17n50H662ceRtZ4ebWe86Sf6nfcpKKCcXMDR11BnWw5FitoQ-yTr5IGxoEVc8lZy6_dYhgWYbkcofHmmJ4aUSIHw16r0P6yVsvatmb8TrZ-FBxRUPrx_avyYXJuL1uquaBLSdNLjEdeJzGVAIAdW4fJBT0Iv6GMfZB-FojbIFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce85279956.mp4?token=NUsd_auz03zc2OoEfUyaZrz6hE8QbRxQ8omQyz74RFgAKbVB8UauZkj9byW5l0fFwMLQyaSxIahyqNA5U0mV9MyLFlDVI0drTM1yQFBn0crXwBZa_7BiIbF59Dxub2NzJ96osM8M5XcXRZhQtdTYz2vGl7fEAHwAa_1uAuSMkHB-17n50H662ceRtZ4ebWe86Sf6nfcpKKCcXMDR11BnWw5FitoQ-yTr5IGxoEVc8lZy6_dYhgWYbkcofHmmJ4aUSIHw16r0P6yVsvatmb8TrZ-FBxRUPrx_avyYXJuL1uquaBLSdNLjEdeJzGVAIAdW4fJBT0Iv6GMfZB-FojbIFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای اطراف حرم مطهر امیرالمومنین(ع) ساعاتی پیش از آغاز تشییع پیکر رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/668154" target="_blank">📅 02:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668153">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
روزنامه صهیونیستی اسرائیل هیوم:
ایالات متحده به کشورهای خلیج فارس اطلاع داده است که باید برای پاسخ احتمالی ایران در ساعات آینده آماده باشند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/668153" target="_blank">📅 02:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668151">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
خبرنگار صداو سیما در سیریک: دقایقی پیش، شنیده شدن دو انفجار دیگر در اسکله روستای زیارت شهرستان سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/668151" target="_blank">📅 01:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668150">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99baa6d07b.mp4?token=hnctG77R-th4bJU00Bvu4y16IIagFOOvEjE4Lkj98lRnVECwV5mKPIwaSe1D2olvrbVF7T5A-9i0VGQRxi0bhFglyB8YksN-XgyRpcqwBYoXPtxem3JAF-T_61CUrAP0d2CILJ5f2SV1ajJLkWKbuxC_cucIoKmil_qc6fDtYWWi0hjvzFBU2r4RnvTT8PXLhOMWPzq7TfIh9ZFzmHlds9doGc8HpFMqBoSINVBycBla5wj0p0vRLiaQeta48vhBPdoSG_76z32QeCjVCoyeNcAINV1WgWMVwOjJ0HX3rPX_JsAD8aTruhYQHnybD-Gv1Dkt_qp6Ve3yELRkwYkn_2Qb2n2wtTgLeIvDTSHW38VgEymquLdWUmOWLzpbKlrBxpu04UBIWwU6Hk2SPphKmw4_Hb1s0s8GYoA505IJ_QfqtSAjcM7nk54EmhR7RUUy3BlB6S8T7HWu0AWFoaDVC8Yn0sWIXq-EHTZInk0ooyOOOHJaJjvFrbAQkc3l1BSTbaPa0e-WKzvrCfzoGiynmTmxVMNxWhLnAHrQr_6Kknqa8QdHjcEGykNvz52u5J3naZnelbeHYZNAM1uk3_X5kOk0WTtXfM4LXIRgP7HRhamV6Do-w2DKOONAAEq_dDiEG1JEOaLt1gQ3OvlS3XghqN5Lg8ARkKhi1JN4iH7srZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99baa6d07b.mp4?token=hnctG77R-th4bJU00Bvu4y16IIagFOOvEjE4Lkj98lRnVECwV5mKPIwaSe1D2olvrbVF7T5A-9i0VGQRxi0bhFglyB8YksN-XgyRpcqwBYoXPtxem3JAF-T_61CUrAP0d2CILJ5f2SV1ajJLkWKbuxC_cucIoKmil_qc6fDtYWWi0hjvzFBU2r4RnvTT8PXLhOMWPzq7TfIh9ZFzmHlds9doGc8HpFMqBoSINVBycBla5wj0p0vRLiaQeta48vhBPdoSG_76z32QeCjVCoyeNcAINV1WgWMVwOjJ0HX3rPX_JsAD8aTruhYQHnybD-Gv1Dkt_qp6Ve3yELRkwYkn_2Qb2n2wtTgLeIvDTSHW38VgEymquLdWUmOWLzpbKlrBxpu04UBIWwU6Hk2SPphKmw4_Hb1s0s8GYoA505IJ_QfqtSAjcM7nk54EmhR7RUUy3BlB6S8T7HWu0AWFoaDVC8Yn0sWIXq-EHTZInk0ooyOOOHJaJjvFrbAQkc3l1BSTbaPa0e-WKzvrCfzoGiynmTmxVMNxWhLnAHrQr_6Kknqa8QdHjcEGykNvz52u5J3naZnelbeHYZNAM1uk3_X5kOk0WTtXfM4LXIRgP7HRhamV6Do-w2DKOONAAEq_dDiEG1JEOaLt1gQ3OvlS3XghqN5Lg8ARkKhi1JN4iH7srZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت عراقی‌ها به سمت حرم‌ امیرالمومنین چندساعت مانده به اقامه نماز بر پیکر رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668150" target="_blank">📅 01:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668149">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
ادعای رسانه صهیونیستی اسرائیل هیوم به نقل از یک مقام ارشد آمریکایی: اگر ایران تلاش برای جلوگیری از عبور نفتکش‌ها از تنگه هرمز را متوقف نکند، آتش‌بس در خطر فروپاشی قرار خواهد گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/668149" target="_blank">📅 01:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668148">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
نیکلاس کریستوف ستون‌نویس نیویورک‌تایمز: به نظر می‌رسد جنگ ترامپ با ایران دوباره در حال ازسرگیری است
🔹
علاوه بر حملات هوایی، آمریکا لغو تحریم‌های نفتی علیه ایران را نیز پس گرفته است.
این موضوع صرفاً یک نوسان یا اتفاق گذرا نیست
، اما دست‌کم برای من هنوز مشخص نیست که
آیا ما به سمت یک جنگ تمام‌عیار بازمی‌گردیم یا وارد سایه‌ای تیره‌تر از منطقه خاکستریِ میان جنگ و صلح
خواهیم شد./انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/668148" target="_blank">📅 01:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668147">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/782ab0c59a.mp4?token=bfcTiurzzmi-cxym5z7-PojDowBUEB568u6__Q8zw_mtGOgQd9mKAnx7kaT0lnIzrP7aVFYYe3DuyOQQpg55YLlwVRo3zkHy_EUrAqJEs3i3SNwYel1xkX1RnPZp38W-pifFWCU3DorjIcDHJUm1dX3Vb_dDKHKIC2vTvsGug6Rgdl2uDrTt5ei04oFdGMDSxxDaEY9nPr41DnpTIciCgganXWIdl4p7iob3908sm4dmhBoRgxsMHNZAI7xMfdqeVlLcGsav9rXT8OLwi0P2pEW5bN8KzM-VLKLCfFELgiyGQAz7Wn3RyE03yLbvq17dYr3Upe6eG6LwVdnvFxQ3Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/782ab0c59a.mp4?token=bfcTiurzzmi-cxym5z7-PojDowBUEB568u6__Q8zw_mtGOgQd9mKAnx7kaT0lnIzrP7aVFYYe3DuyOQQpg55YLlwVRo3zkHy_EUrAqJEs3i3SNwYel1xkX1RnPZp38W-pifFWCU3DorjIcDHJUm1dX3Vb_dDKHKIC2vTvsGug6Rgdl2uDrTt5ei04oFdGMDSxxDaEY9nPr41DnpTIciCgganXWIdl4p7iob3908sm4dmhBoRgxsMHNZAI7xMfdqeVlLcGsav9rXT8OLwi0P2pEW5bN8KzM-VLKLCfFELgiyGQAz7Wn3RyE03yLbvq17dYr3Upe6eG6LwVdnvFxQ3Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای حرم مطهر امیرالمومنین(ع) ساعاتی پیش از آغاز تشییع پیکر رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/668147" target="_blank">📅 01:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668146">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
برق برخی مناطق در کویت و بحرین قطع شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/668146" target="_blank">📅 01:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668145">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
رسانه عبری کان‌نیوز: در آمریکا برای احتمال چندروز نبرد با جمهوری اسلامی آماده می‌شوند و این موضوع با کشورهای عربی خلیج‌فارس نیز درمیان گذاشته شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/668145" target="_blank">📅 01:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668144">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
استانداری هرمزگان: هیچ گزارش مصدوم غیرنظامی در حملات امشب دشمن آمریکایی تا این لحظه نداشتیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/668144" target="_blank">📅 01:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668143">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ادعای مقام آمریکایی به سی‌ان‌ان: این حملات «تنبیهی‌اند، نه متناسب» و فعلاً هم تا مدتی تمام نمی‌شود/انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/668143" target="_blank">📅 01:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668142">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHeRdzUX4dwAJ-ZZYarhyZjRbh7WjjGtdK-vkIX00oHKWea3FsQ3L9DBuORuaBZ1J-lkrQcYHWRJw7dNFw-ikBbHzTI1WhVst1wnI6w5dbl1UvJ57s8QtN7wZcqmrbz-mNWa7aR3tTqFnwYn1kBFFXv6PD5NXDV9uPwTua-hcnHR-VChTxuS0InhA4-ex8Jf7oQnjhta7VJn_KXa_nIVuRcESmh_UqhRV6hVuqI2s-pxyfs9A9fxSJA2avX7tKrsoU0irzxe2LO_98imUxzcUMwG6dJW6KZ9eid8lxbSB1KLqBEtKFOGYFMM3hNI7Bee35cJQ-VNdjqQKpiReMc4Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دشمن را به زانو در می‌آوریم
🔹
تصویر قابل توجه از آقای شهید ایران که بر تن جوانان عراقی نقش بسته است.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/668142" target="_blank">📅 01:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668141">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a56dc51f77.mp4?token=bQhR0rnNsCBtOlRMSw_wldO0Ycw7d1wnwiUg4nLt3H00alqhMZcJtllrBnzvG-RotBsTTXoxuRDWBymGZ6DRaRoAv1DsB-MI49Dcvk3e55wpIu8FF04hfK2usWAXpdggB1jVB4IzLd8eNl2S17N4eAFHHPhCDRerdSbJsnO5gGAGP_iWfCyaAmU97LhMWSUjTzUQjW-rBvkqbEqHk_VkvGJ1SODM4iC73iGUeqIN-k-fnTxCy0X21LrN2AJEKMwnind6M3W8wQqF1BN43K8zdhPmhaF7fZCpQAyZPFv07Qs6IFNFWuqxP_JSFc5ESJzic7RFYyw3gBP7LIs6q6getLVkcL0bPiU7tizppQOLRrZ830mjIaQh7CeYxfPaEkbFEvqD98uC18h0A854o1DLEccgMi2Ae4cZrJGTzL-b6MvjjZY0wjdqFm3AcI2smZrl5xlcE4az2ER17hg2PvfbqCVleLWDFNy8JWFIuFyyclqzsQ4bKtzAe9lTxN7W3SMlTuz5RAHmijpH8n_gfQg1VBj9VNvgrd5zP2Xo0TAmPeSJbnkmsDb0pfkhpf7tsqrFAeMUezQElmRizrVYuqHu1RTQwMdjirn8_-7oMvmp0-bK9pcn_f66A_9Z0j8fDwVNFvSIY1iHFHWorMg9nOXmSVHPMNRk1SlH_Lv5WUlDwjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a56dc51f77.mp4?token=bQhR0rnNsCBtOlRMSw_wldO0Ycw7d1wnwiUg4nLt3H00alqhMZcJtllrBnzvG-RotBsTTXoxuRDWBymGZ6DRaRoAv1DsB-MI49Dcvk3e55wpIu8FF04hfK2usWAXpdggB1jVB4IzLd8eNl2S17N4eAFHHPhCDRerdSbJsnO5gGAGP_iWfCyaAmU97LhMWSUjTzUQjW-rBvkqbEqHk_VkvGJ1SODM4iC73iGUeqIN-k-fnTxCy0X21LrN2AJEKMwnind6M3W8wQqF1BN43K8zdhPmhaF7fZCpQAyZPFv07Qs6IFNFWuqxP_JSFc5ESJzic7RFYyw3gBP7LIs6q6getLVkcL0bPiU7tizppQOLRrZ830mjIaQh7CeYxfPaEkbFEvqD98uC18h0A854o1DLEccgMi2Ae4cZrJGTzL-b6MvjjZY0wjdqFm3AcI2smZrl5xlcE4az2ER17hg2PvfbqCVleLWDFNy8JWFIuFyyclqzsQ4bKtzAe9lTxN7W3SMlTuz5RAHmijpH8n_gfQg1VBj9VNvgrd5zP2Xo0TAmPeSJbnkmsDb0pfkhpf7tsqrFAeMUezQElmRizrVYuqHu1RTQwMdjirn8_-7oMvmp0-bK9pcn_f66A_9Z0j8fDwVNFvSIY1iHFHWorMg9nOXmSVHPMNRk1SlH_Lv5WUlDwjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش زندۀ خبرنگار صداوسیما از آخرین جزئیات حمله به جنوب ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/668141" target="_blank">📅 01:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668140">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
دن لاموت خبرنگار واشنگتن‌پست گفت که حملات آمریکا علیه ایران احتمالاً برای چندین ساعت ادامه خواهد داشت./انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/668140" target="_blank">📅 01:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668139">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
حملات مجدد رژیم تروریستی آمریکا به استان هرمزگان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/668139" target="_blank">📅 01:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668137">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f3f14c10.mp4?token=FRrCtYdsJnNEWyrINo03PyFfMYpXw1bk-eCD86lXnVPKfjQB42-ZaSG_B72M0Soty_mvarYVL3jxvrrJeKHjj4rK7mGdJJddhR6AzgkKWA-CsUkFyLHTn4O8GrG1qdzwIt7SwTrVWbUYtJHjvuN6zYkDXvABTETPVjvKhwb5MQkSA1TUUIgd-sOqoVnJvOuLeaTiAf_DGj8Q85BjmVnUcBFsT6h0UAHui4h-bfrUBlcnJN2O7ZkwNPI2ryvX64Q3qNaKTgp2Qi6x6zx9-GUBBo-mZz2WMT3ktcfV_ocTFLFEJC5XXBKvwRtK_GuCX6b_HUG27gR3Ookqc2LSYE9-_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f3f14c10.mp4?token=FRrCtYdsJnNEWyrINo03PyFfMYpXw1bk-eCD86lXnVPKfjQB42-ZaSG_B72M0Soty_mvarYVL3jxvrrJeKHjj4rK7mGdJJddhR6AzgkKWA-CsUkFyLHTn4O8GrG1qdzwIt7SwTrVWbUYtJHjvuN6zYkDXvABTETPVjvKhwb5MQkSA1TUUIgd-sOqoVnJvOuLeaTiAf_DGj8Q85BjmVnUcBFsT6h0UAHui4h-bfrUBlcnJN2O7ZkwNPI2ryvX64Q3qNaKTgp2Qi6x6zx9-GUBBo-mZz2WMT3ktcfV_ocTFLFEJC5XXBKvwRtK_GuCX6b_HUG27gR3Ookqc2LSYE9-_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور پزشکیان و عراقچی در حرم امام علی(ع)
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/668137" target="_blank">📅 01:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668136">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: ستونی از آتش و دود دقایقی پیش در پشت بازار ماهی‌فروشان بندرعباس دیده شد
🔹
یکی از فرماندهان نظامی گفت محل دکل‌های مخابراتی شرق استان هرمزگان مجدد مورد اصابت قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/668136" target="_blank">📅 01:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668135">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
سی‌ان‌ان: شدیدترین حملات به ایران از زمان امضای توافق آتش‌بس در فروردین تاکنون در حال وقوع است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/668135" target="_blank">📅 01:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668134">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d312260b09.mp4?token=sCs9cRk2gIt-CyDvMnk6L-p0WZ_wujvhaHRBIqctfPf2LZgicQl2vy1_ETZMlslihcEo--N6Pxjw9_ha8-swlQ3zlIs9UoL8kLtLtnXDS9sKuI5cy1B2rxCCJmkBq0zV1oUZEnAzK3VEqv1cI8YuajEcpDIYwqxniLJbqMNDFWGfnfcCf84v7UNnVP_iWoCDlKgeTciGhlnEO8vsVH3PUxjaJBr8uvQU7BxdeXSsy_EYQiJeGthzjNvLBeIUUCPI7UnKtN8AvLqFoE6ZqAkfiFdsHdhwcsCLjAtWMpsRDKwQ8hFgci83fPP25B3Y_wlLgozZxCyzuFQfRkyRhTRF7UR2Y3AqzR_keBBsXSp0B9WYoAx73Nn60RdacfSnWxJq955HoZiE_jHdsiXznHdTzRqjfi64ezAwwLqbMAnhn_6Ycyu0jOYAtNsDSs2eFQfM-LW-7-uodTrxND_C2hW5V9U2eqjoz1aqWSST5aSLOymAfK6M3zbkWDtp_v0I1GGMMGuy0x6XBJEeLNwLWw9eftpE6KV6xir3cg2mHyGuZukeYTetRv0s6WmKRYORkWhUcRqkp5qMeCevKzMRYa4HbE1XtOgUAaJDM2BjLCmrQ-phOEKrM5fx8Y38-cwxrzi_6Wz7RkMF4SqRrRxIJ4nSlWrCcyBAd3rob3nvQ8qKafg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d312260b09.mp4?token=sCs9cRk2gIt-CyDvMnk6L-p0WZ_wujvhaHRBIqctfPf2LZgicQl2vy1_ETZMlslihcEo--N6Pxjw9_ha8-swlQ3zlIs9UoL8kLtLtnXDS9sKuI5cy1B2rxCCJmkBq0zV1oUZEnAzK3VEqv1cI8YuajEcpDIYwqxniLJbqMNDFWGfnfcCf84v7UNnVP_iWoCDlKgeTciGhlnEO8vsVH3PUxjaJBr8uvQU7BxdeXSsy_EYQiJeGthzjNvLBeIUUCPI7UnKtN8AvLqFoE6ZqAkfiFdsHdhwcsCLjAtWMpsRDKwQ8hFgci83fPP25B3Y_wlLgozZxCyzuFQfRkyRhTRF7UR2Y3AqzR_keBBsXSp0B9WYoAx73Nn60RdacfSnWxJq955HoZiE_jHdsiXznHdTzRqjfi64ezAwwLqbMAnhn_6Ycyu0jOYAtNsDSs2eFQfM-LW-7-uodTrxND_C2hW5V9U2eqjoz1aqWSST5aSLOymAfK6M3zbkWDtp_v0I1GGMMGuy0x6XBJEeLNwLWw9eftpE6KV6xir3cg2mHyGuZukeYTetRv0s6WmKRYORkWhUcRqkp5qMeCevKzMRYa4HbE1XtOgUAaJDM2BjLCmrQ-phOEKrM5fx8Y38-cwxrzi_6Wz7RkMF4SqRrRxIJ4nSlWrCcyBAd3rob3nvQ8qKafg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چه اندوهِ سنگینی بر دل‌هایمان نشسته است!
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/668134" target="_blank">📅 01:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668133">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc98386b9.mp4?token=XP0z4zo-5PnQJj3upPXw_at6gz26Qv9-Ube0I-_PaaGUuZQRVXt77j-KzvJRJ2Oj2QBHHkfjyv9HyfYa-6jcwEF-pM-_K34Z2sH-Ml0xAGsn6xduBEI-5puQ953YYws_7qcAzyEAOczq8Nv5WSwZzS2r2MJwAhemQ95o61egAYhBJ3Rnls-ne5IURG17Fkws0Wp7jE0mNGCzbrHSEqOza6rZzHhHhvKxca9QwZ7voU7ew8qfhfLprKzlA0SNCeOPRuA2_xSVN0O_0iJ_TrnA0k6Mljfhr7LPw2rrhVZK0nzWpY60E4D2OZOlOq2_IgnoRNliwplgdlJLoJmOem11Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc98386b9.mp4?token=XP0z4zo-5PnQJj3upPXw_at6gz26Qv9-Ube0I-_PaaGUuZQRVXt77j-KzvJRJ2Oj2QBHHkfjyv9HyfYa-6jcwEF-pM-_K34Z2sH-Ml0xAGsn6xduBEI-5puQ953YYws_7qcAzyEAOczq8Nv5WSwZzS2r2MJwAhemQ95o61egAYhBJ3Rnls-ne5IURG17Fkws0Wp7jE0mNGCzbrHSEqOza6rZzHhHhvKxca9QwZ7voU7ew8qfhfLprKzlA0SNCeOPRuA2_xSVN0O_0iJ_TrnA0k6Mljfhr7LPw2rrhVZK0nzWpY60E4D2OZOlOq2_IgnoRNliwplgdlJLoJmOem11Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودرو حامل پیکر مطهر رهبر شهید انقلاب به محوطه حرم مطهر امیرالمؤمنین امام علی (ع) رسید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/668133" target="_blank">📅 01:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668132">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
‏نیویورک تایمز: در پی اعلام آغاز حملات ایالات متحده به ایران، قیمت نفت با افزایش ۶ درصدی به حدود ۷۶.۵ دلار در هر بشکه رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/668132" target="_blank">📅 01:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668131">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
خبرنگار صداوسیما در سیریک: دقایقی پیش ۷ انفجار در بندر سیریک شنیده شد
🔹
این انفجارها مربوط به اصابت پرتابه به اسکله تجاری سیریک و اسکله صیادی روستای زیارت بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/668131" target="_blank">📅 01:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668130">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
خبرنگار صداوسیما در سیریک: دقایقی پیش ۷ انفجار در بندر سیریک شنیده شد
🔹
این انفجارها مربوط به اصابت پرتابه به اسکله تجاری سیریک و اسکله صیادی روستای زیارت بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/668130" target="_blank">📅 01:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668129">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68492ed60a.mp4?token=arfmLfFxWtiK1MovS6z8KNtIPDD-Xc0HBNY4jIQUg3WtOda3JRJD07uktEf9KaJmZEcK2E99zZdqgcnZFn9QPy9-tk4PTKe1OyZtCkbyZ5viw3QN-6Gbi0AC6WNA1H_ENRwc5IgWSzAfAK064eEMn_5SiasQkOHf4P4CRdSroCX1D7_ZPJ1GrZ4sxHptG5xaK_h57E4Rx5RCMb4XOzDbHIaKhaXxa9M4am_ziaJHukcbAEAlu4v76Pit8Z7F_WAF4bYTpzO3j9IXOUqPkxjkk4Ib0KanhPlacAqzb5NAmfUyN6mGYRQ8J_ym6SV2XwpEogPz3ohsAZUsIt9BMphDMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68492ed60a.mp4?token=arfmLfFxWtiK1MovS6z8KNtIPDD-Xc0HBNY4jIQUg3WtOda3JRJD07uktEf9KaJmZEcK2E99zZdqgcnZFn9QPy9-tk4PTKe1OyZtCkbyZ5viw3QN-6Gbi0AC6WNA1H_ENRwc5IgWSzAfAK064eEMn_5SiasQkOHf4P4CRdSroCX1D7_ZPJ1GrZ4sxHptG5xaK_h57E4Rx5RCMb4XOzDbHIaKhaXxa9M4am_ziaJHukcbAEAlu4v76Pit8Z7F_WAF4bYTpzO3j9IXOUqPkxjkk4Ib0KanhPlacAqzb5NAmfUyN6mGYRQ8J_ym6SV2XwpEogPz3ohsAZUsIt9BMphDMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری از حملات بامدادی دشمن در بندرعباس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/668129" target="_blank">📅 01:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668128">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: حملات سنتکام به ایران ادامه خواهد یافت
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/668128" target="_blank">📅 01:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668127">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ادعای آکسیوس: اهداف حمله امشب در ایران شامل سایت‌های موشک کروز ضد کشتی، سایت‌های پرتاب پهپاد، تأسیسات بندری و دیده‌بانی دریایی بوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/668127" target="_blank">📅 01:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668126">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Po-zI0OMUfmBBRGu6Y0n_7o1Tc2O-xqPmYenjnpXsu9yLCKh33IGppS_W4hRTWeS7YtHHN2VlwT4-xrJLOTA9Qb2H7q149PQ4Rjnzj8R1nAliEf62WVXYYW7_1DCVOsppbZOUcBifGIYsUWr6Sk7OAMRdLSeW8f8JtQZhnn2dwQd7n3QlTEAXIRMjNY8kUSc4LZElZ6DU4ELO8KASaBnciqL0UoAHhjjGobIjIYXpvrcu1la-IndgtJX6BlvoFn8Z9GasPLxr5ux8An7xUSB_szItVTqjMxtFTfXwGouBgKotr_eDU0-XX7r9eqQXI_ib0sB11DrOBIeN0Gw3WnLVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: حملات سنتکام به ایران ادامه خواهد یافت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668126" target="_blank">📅 01:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668125">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای مجدد در حوالی قشم و سیریک
🔹
بامداد امروز (چهارشنبه)، منابع محلی از شنیده شدن صدای مجدد چند انفجار در حوالی شهرستان سیریک (۵ انفجار) و مناطقی از حوالی جزیره قشم خبر داده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/668125" target="_blank">📅 01:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668124">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ادعای وال‌استریت ژورنال به نقل از مقام‌های آمریکایی: ناوهای جنگی ایالات متحده همچنان در حالت آماده‌باش باقی مانده‌اند تا اگر دونالد ترامپ تصمیم بگیرد، محاصرهٔ بنادر ایران را دوباره برقرار کنند
/انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/668124" target="_blank">📅 01:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668120">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe18353a92.mp4?token=swolmDp0hTXQnMe1pRwkkfChADcD2FjuMgMoLNi_1x0V0bhS-cNkh9PWCoIurHhYOJXP6spTlk_KPymI0G5cpFYBPTZcoUGyiMmV5JOWtYBepdkVT4qz_IVCb3R_sh1ud57o7BrPeCNh4mKYaIcdLRJkrdwaUyR82lO0xj2Lj50AOOhnDGyGp6ugMiecwB0g3K37mJbt0megrBQJ5wCBZjiew-fNnUDg9uussJcjzJg0mcDch2olhXnkynpg9zj__2idX-XB3R3xZq8OhIyBJsR53BoXneXxOOSc5pElSRNb9HvkwdDlmQ5o077UA3D-PaWC1xgTbyMpKGMqIscuAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe18353a92.mp4?token=swolmDp0hTXQnMe1pRwkkfChADcD2FjuMgMoLNi_1x0V0bhS-cNkh9PWCoIurHhYOJXP6spTlk_KPymI0G5cpFYBPTZcoUGyiMmV5JOWtYBepdkVT4qz_IVCb3R_sh1ud57o7BrPeCNh4mKYaIcdLRJkrdwaUyR82lO0xj2Lj50AOOhnDGyGp6ugMiecwB0g3K37mJbt0megrBQJ5wCBZjiew-fNnUDg9uussJcjzJg0mcDch2olhXnkynpg9zj__2idX-XB3R3xZq8OhIyBJsR53BoXneXxOOSc5pElSRNb9HvkwdDlmQ5o077UA3D-PaWC1xgTbyMpKGMqIscuAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نظر مردم، قبایل و نظامیان عراقی راجع به شهادت و تشییع پیکر رهبر شهید در گفتگو با خبرفوری
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/668120" target="_blank">📅 01:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668119">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
۶ پرتابه به محدوده اسکله طاهرویی و ۲ پرتابه به محدوده لنج ساری طاهرویی سیریک اصابت کرده است  بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3228642</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/668119" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668118">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqaTQWpg_s2LBcDenOMIFIUMmk72sF7siSnu5BptcZ1-h6y1jH8gpEi0UD20EI0zlOjNhP5XDm8r8bqoJQ6Ou_SdUN-QGZ9SJW5tzw-hdLbXoxVy9p1_JYKyio3vHPODwVidYjdZmZIAEy8XSNc2Shgir9D4z2GcrfdDm4igEcXgZdekADtVFls5Bg6RnTDv05V6nOv2dRmc-7noHsTsLq0UKHazWhQ0z3WmeGzKBX97mGAwgZrN6P44sDr6A-0Wm_lbXDU8zMHBUmkQqLi8KqQ-Ifs_sAy0qFfQxPVDnxmI1AGI1vGHS0514SVy9UJyHxvoQLXAaV92fY8n4uhTWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه درباره نقض صریح بند ۱۰ یادداشت تفاهم اسلام‌آباد توسط آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/668118" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668117">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
تجاوز رژيم صهیونیستی به جنوب لبنان
🔹
منابع خبری از تجاوز هوایی رژیم صهیونیستی به شهرک بیت یاحون و منطقه واقع بین دو شهرک برعشیت و بیت یاحون خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/668117" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668116">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
خبرنگار صداوسیما در سیریک: دقایقی پیش صدای ۷ انفجار در محدوده روستای طاهرویی شهرستان سیریک شنیده شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/668116" target="_blank">📅 00:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668115">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqJGi3fSfjPQLd9QtK4xeV5-ZxPI58h9fwtoZgebTG0NGkl_MWkHK51ARDSMXPmojxceLs1alY39yD6ZNZXt3aa2VV89S_YN6cauVuf5nOfv-_G9R-UreJhpukdGcFWFhj10KTH4pgbtaj9Hvj_J9ZFpb3Kewc2nEB2IgA0OfftvdtB2qS6RKHE_zx8759Fo57POwerybPTH_0liTgOWnRi4LsZ-QV0bgTe6ohhtzLiPADliKD15SXRcCC_F-LCOEi-7yG2iB-3MU3cL-hIu7fbpx345mqz9fywhbrMk3LoOhZa1QEhQjgWHxnlOjKQWAbyLl_jabOsnCD2blrrihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند
🔹
حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/668115" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668114">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
خبرنگار صداوسیما در قشم: شنیده شدن ۶ انفجار در روستایی حوالی شهرستان قشم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/668114" target="_blank">📅 00:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668113">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
در اولین ساعات بامداد چهارشنبه صدای انفجارهایی در  سیریک شنیده شده است
🔹
تا این لحظه هیچ مقام رسمی یا نهادهای نظامی و انتظامی منطقه ماهیت این صداها را تأیید یا تکذیب نکرده است./ مهر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/668113" target="_blank">📅 00:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668112">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
دقایقی پیش مردم در حوالی سیریک و قشم صدای چند انفجار شنیدند
🔹
هنوز محل دقیق و منشأ این انفجارها مشخص نیست. اخبار تکمیلی متعاقبا اعلام می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/668112" target="_blank">📅 00:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668111">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
آغاز حملات ارتش ایالات متحده به سیریک/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/668111" target="_blank">📅 00:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668110">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مهر: صدای انفجار در قشم و بندرعباس هم شنیده شد @AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/668110" target="_blank">📅 00:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668109">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f82e9adf0.mp4?token=uremnGeC5c93lUPWzKdke2hu8hBTE7xPleyvl3DM8m694blJzJyUFwWuTjZXSENqIc94eouixbWA0q69xfD7pG2QQK8Ls_MCNuU1ZPvgdODmb6Q4QznV6Yv1mj_-wjA6jlpW0v4LMG93eGHQYflWsXdo9MXwkh5uCFLmb1S6BPdpPlaUnilKMLCn7rW09cw4_RZfWV_udaWqINppLwM6XWvO_hzbaneJz1lHivZqpJK3REd0JVbpnWQi-Top28JLVxVvJNDxV90P5POJmnyKQ9sOxaZ2YS4nBc-29xD1L3jJIbNy28hu7mVoix7t4Fj70ayjRLm_2fPfQ0Wm79YAPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f82e9adf0.mp4?token=uremnGeC5c93lUPWzKdke2hu8hBTE7xPleyvl3DM8m694blJzJyUFwWuTjZXSENqIc94eouixbWA0q69xfD7pG2QQK8Ls_MCNuU1ZPvgdODmb6Q4QznV6Yv1mj_-wjA6jlpW0v4LMG93eGHQYflWsXdo9MXwkh5uCFLmb1S6BPdpPlaUnilKMLCn7rW09cw4_RZfWV_udaWqINppLwM6XWvO_hzbaneJz1lHivZqpJK3REd0JVbpnWQi-Top28JLVxVvJNDxV90P5POJmnyKQ9sOxaZ2YS4nBc-29xD1L3jJIbNy28hu7mVoix7t4Fj70ayjRLm_2fPfQ0Wm79YAPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرفوری از یزله کربلایی‌ها در بین‌الحرمین حسینی به یاد رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/668109" target="_blank">📅 00:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668108">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
گزارش‌ها از شنیده شدن صدای بیش ۸ انفجار در سیریک خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/668108" target="_blank">📅 00:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668107">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
گزارش‌ها از شنیده شدن صدای بیش ۸ انفجار در سیریک خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/668107" target="_blank">📅 00:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668106">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dac22428e7.mp4?token=Y1OuAHFemQuoSoqLRVWtF9FuD_P8CRsTbulvU5y3psrGSZCmsba3sBlSO3CN8ooXRBko3gfO1M885XBqSAnmAFwIdlrn5ROIBnCXLF_tcdAHlg5SlAgIIDv9MiXmkFN3r-6EE-qxgfbMUOXJxN17POCHe73_bZTFi6gGUHZk9NTfGOQgvNeDcVoGH3Nv5700YkZj3GMqj65UWxhIcdfmAeoiReNIM054HXO91Z7CRa7F5hmmmEHBz7kuIVqp1ju4Z3o8FEP2cHhHnzlVS34BU5Z1O8-9W8_nzgla3YQfRlCqLUCe6avlSv60MArocv80BQx8llYcfnwQreY8hNVpnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dac22428e7.mp4?token=Y1OuAHFemQuoSoqLRVWtF9FuD_P8CRsTbulvU5y3psrGSZCmsba3sBlSO3CN8ooXRBko3gfO1M885XBqSAnmAFwIdlrn5ROIBnCXLF_tcdAHlg5SlAgIIDv9MiXmkFN3r-6EE-qxgfbMUOXJxN17POCHe73_bZTFi6gGUHZk9NTfGOQgvNeDcVoGH3Nv5700YkZj3GMqj65UWxhIcdfmAeoiReNIM054HXO91Z7CRa7F5hmmmEHBz7kuIVqp1ju4Z3o8FEP2cHhHnzlVS34BU5Z1O8-9W8_nzgla3YQfRlCqLUCe6avlSv60MArocv80BQx8llYcfnwQreY8hNVpnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون حضور مسعود پزشکیان رئیس جمهور کشورمان در حرم حضرت علی(ع)
🔹
بهنام توفیقی
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/668106" target="_blank">📅 00:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668105">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef12cc8100.mp4?token=oG2e9NC7MvSSn6V8xezji5j5Bk8nlN78QfjkwDS1_83o5kNpGdOzjS9vNVghHZBBJWGatbT-cNXLUs0bSHvYzufnkB3us4pn5Lno36w9bdt3sKGhcOFgz3Rl_LdGiLFFQnxxBRCNETa3VpbWAwEcdg8CL_7XLfJ_KWivwybSVr-U1M6t489cNreNqnGU3odvPS-ya1MFynHlTXeYRAKYTj7J5TV4UuREkF8JYqV3NCMkJeLOXrUGPKD6cXg6auPWLn0ZYRqYRBRU2Zs84qgIyo8MT5Al_4YBa2w8vd6skEGdXL0W__ToXYv1N7fE2SbaNmFuYhLZvP0krGzyLLaLFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef12cc8100.mp4?token=oG2e9NC7MvSSn6V8xezji5j5Bk8nlN78QfjkwDS1_83o5kNpGdOzjS9vNVghHZBBJWGatbT-cNXLUs0bSHvYzufnkB3us4pn5Lno36w9bdt3sKGhcOFgz3Rl_LdGiLFFQnxxBRCNETa3VpbWAwEcdg8CL_7XLfJ_KWivwybSVr-U1M6t489cNreNqnGU3odvPS-ya1MFynHlTXeYRAKYTj7J5TV4UuREkF8JYqV3NCMkJeLOXrUGPKD6cXg6auPWLn0ZYRqYRBRU2Zs84qgIyo8MT5Al_4YBa2w8vd6skEGdXL0W__ToXYv1N7fE2SbaNmFuYhLZvP0krGzyLLaLFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ندای خونخواهی عراقی‌ها در بین‌الحرمین
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/668105" target="_blank">📅 00:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668102">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9ade6e58e.mp4?token=UXQYrxrjLGYPwSd7Z1eYBbS-Bfvo_SFNeKgRfegAsv3xrcm-VthQ_uka1uA-Vf6W3Qq6CbVReqoxcckuNtBwxeIJqx9Co7UlFySHhRFlyAqAVRgZHexZpWXtmMSw7TaYXaK1M1fGuZLhaon74CF0E77Cduj3I7IOLTygFXrJwW2Qm_z49MwrLeg6dch2IUmUrq6SsKhQQplCzoJgRfpUoE-3SkXKxywwzhntQNL7c_nf0MuIy5D5IwM9u6P2IaPchimCbgTTkzKKI0gQEZOJgHSyPdoasktohl4S1cnTTpBNn0BH6u3dLLhOhqXaumRr3A_mr9l5A6vmYMXd-Ca6yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9ade6e58e.mp4?token=UXQYrxrjLGYPwSd7Z1eYBbS-Bfvo_SFNeKgRfegAsv3xrcm-VthQ_uka1uA-Vf6W3Qq6CbVReqoxcckuNtBwxeIJqx9Co7UlFySHhRFlyAqAVRgZHexZpWXtmMSw7TaYXaK1M1fGuZLhaon74CF0E77Cduj3I7IOLTygFXrJwW2Qm_z49MwrLeg6dch2IUmUrq6SsKhQQplCzoJgRfpUoE-3SkXKxywwzhntQNL7c_nf0MuIy5D5IwM9u6P2IaPchimCbgTTkzKKI0gQEZOJgHSyPdoasktohl4S1cnTTpBNn0BH6u3dLLhOhqXaumRr3A_mr9l5A6vmYMXd-Ca6yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عرض ارادت شهروندان ایرانی و عراقی در کربلای معلی به رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/668102" target="_blank">📅 00:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668099">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
یک هواپیمای ترابری در مسیر کراچی پاکستان ناپدید شد  سازمان هوانوردی پاکستان:
🔹
یک فروند هواپیمای ترابری بوئینگ ۷۳۸ متعلق به یک شرکت خصوصی که از شارجه عازم پاکستان بود در مسیر بندر کراچی ناپدید شده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/668099" target="_blank">📅 00:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668098">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bce9bc8fdb.mp4?token=QI-VWENplK90K280_d6JJGE2DH4YjWZbS6kvBDhy-oKqAzR8FQWd_yASYQ_ZH9wh5aJpPazIr-U-T7mt26lDuuHCIVeyiZsSDU-5ctbjTqbxs6mCeizahFpr2SDO04F3X4w9ZoLg61szYdriGB1HRKk6yev0fBtM-VO_0oAwqXdFJ9clzr_GDdkYmsNoNlogUt4Mqugf8N06gI-fwKkaRLDKCebvU_ijmvFrtwFtcxWyv0hoF_hxTNwqfMXh0Tpkguzdzy2IOXeDlwHCuHq1xNuCWQDzC_XxSd9FPiBTADuvrPdmFCpdVXh1PfLj_DOeo1ObAps6rtXJeF5oWnL8Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bce9bc8fdb.mp4?token=QI-VWENplK90K280_d6JJGE2DH4YjWZbS6kvBDhy-oKqAzR8FQWd_yASYQ_ZH9wh5aJpPazIr-U-T7mt26lDuuHCIVeyiZsSDU-5ctbjTqbxs6mCeizahFpr2SDO04F3X4w9ZoLg61szYdriGB1HRKk6yev0fBtM-VO_0oAwqXdFJ9clzr_GDdkYmsNoNlogUt4Mqugf8N06gI-fwKkaRLDKCebvU_ijmvFrtwFtcxWyv0hoF_hxTNwqfMXh0Tpkguzdzy2IOXeDlwHCuHq1xNuCWQDzC_XxSd9FPiBTADuvrPdmFCpdVXh1PfLj_DOeo1ObAps6rtXJeF5oWnL8Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزاداری عراقی‌ها در عتبات عالیات و دعا بر آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/668098" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668097">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec12a3d841.mp4?token=jOjKtr-RmxkTmRyWTYSj3THIVx6MuSJRb9SyPkH-zVYWBh9n3yo8zeRqgOQP3LSxCw_gJXjiJoKNnUvHFfm6HvIM-K79EHIkHLTB8I8ZAjjU3lihX_Ac8aQVx0Gv5KTgyNe3XOQsbN7SN3iq6xCiqk7oh1KRc19ujZb3j5tnLnAjGcbQnemxj_qrDEse8cJWDM7OvOnEa9fRPBw4IedurWqLbl8RVXHI0__WHJY_ZcJDVy8hpQIlKLSR9cm1IGxjk1-b0sGNMeB0IYTaaHCqTVTsLfUQZycDYSdmIiNTY_fnwF1-C1t3wWbnim3C2ztSZox6bA3sx2ykvknve-5lPkT28sQNX_3X8G5RvpwJbDLCl97qLiXNSNzK7kI9h8wf5K-I6havVZENkr7KLwgJHgQdxwcrglaiy1QHvYUsVdr1AtJRYYY_b7VpjIScV2hDg2lXWznAYzC1qJgIjNwLBuqfmRmnDfLP8T4u4UUePwtp7qt0VyYtwVNvxkTNe8JnG8NdK3hDWVhsCb2tYQigS6OQnRC9ZlaCcTkVnoiyGf07jRRrXt3HslcXsCVI0XWfJ-x1IrEuEIGNoxiEX5BU2eNzb_Rz_S9I78bb4L18Rl59sKPdhXT16mcuNHEIUMd4EE2WJbpkgaGcJUcTpLRwS1V2zRXiP4JEc7vd0tgVrGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec12a3d841.mp4?token=jOjKtr-RmxkTmRyWTYSj3THIVx6MuSJRb9SyPkH-zVYWBh9n3yo8zeRqgOQP3LSxCw_gJXjiJoKNnUvHFfm6HvIM-K79EHIkHLTB8I8ZAjjU3lihX_Ac8aQVx0Gv5KTgyNe3XOQsbN7SN3iq6xCiqk7oh1KRc19ujZb3j5tnLnAjGcbQnemxj_qrDEse8cJWDM7OvOnEa9fRPBw4IedurWqLbl8RVXHI0__WHJY_ZcJDVy8hpQIlKLSR9cm1IGxjk1-b0sGNMeB0IYTaaHCqTVTsLfUQZycDYSdmIiNTY_fnwF1-C1t3wWbnim3C2ztSZox6bA3sx2ykvknve-5lPkT28sQNX_3X8G5RvpwJbDLCl97qLiXNSNzK7kI9h8wf5K-I6havVZENkr7KLwgJHgQdxwcrglaiy1QHvYUsVdr1AtJRYYY_b7VpjIScV2hDg2lXWznAYzC1qJgIjNwLBuqfmRmnDfLP8T4u4UUePwtp7qt0VyYtwVNvxkTNe8JnG8NdK3hDWVhsCb2tYQigS6OQnRC9ZlaCcTkVnoiyGf07jRRrXt3HslcXsCVI0XWfJ-x1IrEuEIGNoxiEX5BU2eNzb_Rz_S9I78bb4L18Rl59sKPdhXT16mcuNHEIUMd4EE2WJbpkgaGcJUcTpLRwS1V2zRXiP4JEc7vd0tgVrGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعارهای لبیک سیّد مجتبی، الموت لامریکا و کلّا کلّا آمریکا در حرم امیرالمؤمنین طنین‌انداز شد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/668097" target="_blank">📅 00:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668096">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H07cuglbveEfeyI3AaG6eLNhTMS7S1aa2gHg4ualCmlxMUngmvhLhuu9HX-iU5w43-jKyqO-63xu8SjtP58ly7jQDzw833GhWMIie1mEahAFX2Ncu4_YXAxIfYIqtm_0yCr_ue6P7J93xmR57iPMNCOBI5WSnsMFsIYBsrbTT-__zPOlpPVMsT--Ey5Pkpwbfo1L7z-qA93tfOTx_S0Ljwm094W8xmOATM6SW0UVVyjIWRAAGAT_tsQOpguFLg0lRPkhD0Lb1nSGKlWQd0PFxoQQK4bmkYHGCdP74CiNIxYYXVVFV_VfOCoYbCFEHIPTqjmI-hWcW7YMsmmg3FZcLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت
بقائی به مناسبت ورود پیکر آقای شهید ایران به عراق
🔹
ای زائر حسین، این سفر بر تو مبارک باد؛که عمر فانی است، اما درِ حسین همواره به روی مشتاقان گشوده و چشم‌انتظار است. خوشا به حال قدم‌هایی که به سوی بارگاه او شتافتند؛ چرا که این گام‌ها، گام‌هایی هستند که تقدیر، خود آن‌ها را ثبت و ماندگار می‌کند.
🔹
سپاس از عراق، به پاس کرم و بزرگواری‌اش در میزبانی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/668096" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668095">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBnRRLql0QGeGiS60K0W4qS1R12dJ6dKanWPQFtG2MMAfFKYmPT6FLvPox-JPZqdTvGDfKBptMOPNyHvQlgL5aBPFSbeZkWms13G3hthMA0LyHOp2WKYqtQw3huT6s8WdyHZnhI-f7f59wX8_eLqndcwe6avea0sggep9UWWCLek8csIoCJ3UMkFITn1nbqrqoBYEtnddmyxziCYouJfGQucJ_Ay1Hw04PhxyAUC48Ncel76SvQ1BOtZZmmN-jlgBp8oEjcGJTSIEW1TsebaESFVK2GsYlAZsYqVHAduDnA11mHw68UlewtrY1a97s2n0bxtzS7B-QkmlzVRV3Uq3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور مسیحیان عراق برای استقبال از پیکر پاک رهبر شهید انقلاب  #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/668095" target="_blank">📅 00:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668094">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
یک هواپیمای ترابری در مسیر کراچی پاکستان ناپدید شد
سازمان هوانوردی پاکستان:
🔹
یک فروند هواپیمای ترابری بوئینگ ۷۳۸ متعلق به یک شرکت خصوصی که از شارجه عازم پاکستان بود در مسیر بندر کراچی ناپدید شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/668094" target="_blank">📅 00:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668093">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e1fa65d60.mp4?token=Ybtv4qF8YWO9H_AVMKnTbBxS7iHVePoeTGkQwxdhG8vjJUS29IuQOzIK3yD-KsClQsLztjc1B39irsL5u9LoP0SvEDvlawhfnwwGlYpc4RYZDrZ2r8Eaoz7o1BdLfXUfQ9-r3P_hvu7J6SRxo9wg2Rnr03y9fvlwONR1m7L378MysuqoaSg6Y5gK9umxOkZN8RjKsHx30U0AfDoOOKeVFyDN5KfnJ9_99TRf7x9MoXqKTCY25SLLyS9tzJPji_8u8t7tTldlJx--vgEzso5gMb1KIZBV4rDX6V1zg74Se773TL2855D2BEPN9WileklhjsuYJ1saQ95dOU76bmrL_UtVFlDiVixQOOzwwUcbOaREFP8_QqCeMCKukhB_w_05iqvNFCa5KfPWiUJi29sLDv-OX-IzQlfpKNEAkEMaG6T8gi7pdFTi3Op1YqZuEFxjesZ4ZopMWZGstF9Ld5M5h53jw6myIPt0LPsGYRHG_cO-ip5peps6EXQZlI8YVwTOP87TNo3wodV96FLVDUxys7e2SgNrfhHhKYspzCZ51goeWNizxq0ggG3UP_4myzU-8ivw2-UYKIjxW_KSu9lS86Pp-zAid5MRN8LXcUYS8MlLm9cdgaxP52WAxcSTSUCVnA7QGVxpuFYxKGoFZTztA0gLU28l2TAm51CDlgOFQpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e1fa65d60.mp4?token=Ybtv4qF8YWO9H_AVMKnTbBxS7iHVePoeTGkQwxdhG8vjJUS29IuQOzIK3yD-KsClQsLztjc1B39irsL5u9LoP0SvEDvlawhfnwwGlYpc4RYZDrZ2r8Eaoz7o1BdLfXUfQ9-r3P_hvu7J6SRxo9wg2Rnr03y9fvlwONR1m7L378MysuqoaSg6Y5gK9umxOkZN8RjKsHx30U0AfDoOOKeVFyDN5KfnJ9_99TRf7x9MoXqKTCY25SLLyS9tzJPji_8u8t7tTldlJx--vgEzso5gMb1KIZBV4rDX6V1zg74Se773TL2855D2BEPN9WileklhjsuYJ1saQ95dOU76bmrL_UtVFlDiVixQOOzwwUcbOaREFP8_QqCeMCKukhB_w_05iqvNFCa5KfPWiUJi29sLDv-OX-IzQlfpKNEAkEMaG6T8gi7pdFTi3Op1YqZuEFxjesZ4ZopMWZGstF9Ld5M5h53jw6myIPt0LPsGYRHG_cO-ip5peps6EXQZlI8YVwTOP87TNo3wodV96FLVDUxys7e2SgNrfhHhKYspzCZ51goeWNizxq0ggG3UP_4myzU-8ivw2-UYKIjxW_KSu9lS86Pp-zAid5MRN8LXcUYS8MlLm9cdgaxP52WAxcSTSUCVnA7QGVxpuFYxKGoFZTztA0gLU28l2TAm51CDlgOFQpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کودکان پاکستانی با عکس رهبر شهید در نجف سرود می‌خوانند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/668093" target="_blank">📅 00:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668092">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2U13gS85zEVhg2eGvXo5-kSBTodAzka8xB2n8mWbk_EC2ovOw6gg-jnOKHZh0juFg2q85S7YlqsTpbBc2R_fNHKzKKT0PUpViw6V1pzw_10iBpBHYvYS8jVTRmu4UwLpLf3Q1G-CPDRv6VOMqr21pCVwxcEAA5IEL3lnACQF8sgZh27Nr2qTt89_2BJ4BoK-VayPf-3t6UwE18Tol1ybm1UXfwe26Px_txdk83NmtzdXvvYzJoCyQSDuILZfCD9kL10DlO6DV93Vprw7cUpKLJXLDLD6zXfEgAarvL619l6RDHCVHb5yloY8YejuGayM50C52StKT8IjHS7CxDAdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/668092" target="_blank">📅 00:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668091">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54d15ba9f7.mp4?token=QolvRSUmMWJ5AJEkdmHqs_XlR9v90rJ42v0rRdTYN5KvhhO-7GyXLQeW3Sv3d97hxK9imcDWyv6uKhuX_V8rrH6nvWXZpYItsmUsjXpwPIwDfaenKo9C7LwiJdiIxoQJimiRPZRo01kNzwJ1bYgFq9dYq3xV1mq5TFrD3XDuBoqFz5lSi3sMsoTjtF978P3uQ0QRrbMakOfU24gWK7t-Kr44S_w_NqpCXPJDZozygq0wD6Jui5VYxLdwdF8yNqLfaNfCjQF7w7IraPJXUkkIgwaT495tqLaSPOyoflhC75tS8iIwYQw9HREEUbsoGT144pzc8dksp8XX3uDA0Mtsbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54d15ba9f7.mp4?token=QolvRSUmMWJ5AJEkdmHqs_XlR9v90rJ42v0rRdTYN5KvhhO-7GyXLQeW3Sv3d97hxK9imcDWyv6uKhuX_V8rrH6nvWXZpYItsmUsjXpwPIwDfaenKo9C7LwiJdiIxoQJimiRPZRo01kNzwJ1bYgFq9dYq3xV1mq5TFrD3XDuBoqFz5lSi3sMsoTjtF978P3uQ0QRrbMakOfU24gWK7t-Kr44S_w_NqpCXPJDZozygq0wD6Jui5VYxLdwdF8yNqLfaNfCjQF7w7IraPJXUkkIgwaT495tqLaSPOyoflhC75tS8iIwYQw9HREEUbsoGT144pzc8dksp8XX3uDA0Mtsbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر رضایی: هم انتقام مصداقی و هم انتقام از اشخاص باید صورت بگیرد
🔹
انتقام مصداقی به معنای خروج آمریکا از منطقه حتما باید صورت بپذیرد تا مسیر پیشرفت ما باز باشد.
🔹
اما به غیر از آن، ۲ قاتل رهبر شهید نباید از انتقام در بروند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/668091" target="_blank">📅 23:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668090">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8lHotYaUVnT4vAuQ_y8l7BzkxHW1kEdhnGVAHeHO3usLbsRjUcVpNx0R_8vxwhUCzZVpgiMbYeWElH3yPPE1LsJ8_bi1-OSAGKQ5dHpRsfeIUlHprJIs52_dhDPVxItPOniRJdBSlY0E_fpKbaW2RCMCY-FuI_ABcCFYG7qPLiLAuOfSyW6WtENWshhOb_fBVQ4QyXHYSEL_MZtkJ0saA304-JJf1utuGnr_gzqd911hqdRN5Vi6HxdWtDSEdyTlGzPbwU4L9glUWdiViVGx3XcIdVYHFUd3s-qVPGBXd4oUCFl3IYWAL-z56gAAVdIIq8_rPYyZ09Vm7v-hdBCag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شایعه رابطه لیونل مسی با گزارشگر زن بالا گرفت | همسر مسی وارد شد!
🔹
در حالی که طی ماه‌های اخیر شایعاتی درباره ارتباط احساسی لیونل مسی و خبرنگار مشهور آرژانتینی، سوفی مارتینز، در شبکه‌های اجتماعی منتشر شده بود، کاپیتان تیم ملی آرژانتین سرانجام با لحنی طنزآمیز به این گمانه‌زنی‌ها واکنش نشان داد و به آنها پایان داد.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3228554</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/668090" target="_blank">📅 23:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668089">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvKqZga4ajlYf2omcyvbAUuWVLw8ZPb1Zu7gkKznRaEpFpb8OJUkafzzpK-hDXVtuAqSipR9nT0aCH78064rcjyKN3-C1WbdQeWfiQom0M2xMkQFegSwgktxq8CzS4gRnUrcTBQbXEVd3TdG46au58_MwCx6_gbGu4ndKY4hmUxJSIk8s6SKrEg1hGD5xemEnw7_MMsrFZlCRLWet_PssnR0IqZEk5nGMsd7Mp0bpc8f0R2trTuOJuO7J9N25Djh6z3nJBJWS1EhcP7Y0ov490k212CYD0zQ7gsuOfFCDrqRdwETtdLeU2_iEfpX_aR6gpKdb8wf3zQ3462CJM46BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بی‌قراری عراقی‌ها در لحظه ورود پیکر مطهر رهبر شهید انقلاب اسلامی به فرودگاه نجف اشرف عراق #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668089" target="_blank">📅 23:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668088">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
خبرفوری| ادعای مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند
🔹
یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
🔹
به گزارش خبرگزاری رویترز، این مقام…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/668088" target="_blank">📅 23:49 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
