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
<img src="https://cdn4.telesco.pe/file/eVw7Ido8aogrHNgn8Av5g1WwFbg4MUAtsWcUsdFWfoDvvfKmm1SE20uPVp_x4Hb73CBJ3QeZ9lugl4_ryMySa2zC2Y1VXxq8yIqRS6xJbE91gE_RC366k8ChW0HdcN0MBd8MwabV4Dfl1CalJaaTJYkhDfCrnOKLv_iAgHQVQYhEwUBRRbLNT3CaqZu8FFTcWIbPCM-pyP8AlnlAzViC7FryDU2Dy9fCUcYbMBzk0JihOUCKxCb8mbazWQU3rhkY1cKpYCvXsRUU-wzGEiEyOfIgFR_ueUU-ZCNYHlCaRcZf8kWFoC4w352MbsXfzMwRjNBt5SxXoqPNAK_3VRB3YA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 09:34:16</div>
<hr>

<div class="tg-post" id="msg-6804">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o3dAVzKDx7hBWM_1zhbpJNryBsq9LlpbCZJJrbk1w3e5VHwA7v5pDJeJkm_BeLbasHP48iuQKajuzWRs21f1ylJxuERVjyvb52RIiZMARQU3dfC33SxkXh5QDdl8baDL_eaQyddf6xN5coHTlHM9DJ02KTYD0NKM3LYcI57uzJps0toxvpVur5bTQWJg9SFit8PrMwHDmqny0Cmcerm4bgrMHfdj5SBEwQVMXtHXRuLG8heSTD7Bhp9Bum2D4F3rtQ0yDgcJ_MfaQY7JdCSlIR_DwxvdIuPmly70VGeh8kAo-lKUnyqJGDd5kSae_3JcVKRBJLZRwqqibdC25ZgMSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zc2bwJfKBd-cXRtYUK4lVRoyL7yz1m2jflGfjFkOJB1k2A6VuQ_oJBJBRd9sG5oEVEUJ7IrttsGWwkdofcKxpzDVYYG-VEfuWajU72_occb_ITKF5WnMwzEd9dtCRNADb5bQZtJRr9cvrXjcEsCmTDFKXzGSK2zPk5JLHHARY28q2C91IDKHjekGd8DDRlPKihJSkD6xLYLkuoiFf5IwG8uvCNVskOdi3YCY3OK3IkLIR7c14P1osWinIoXk-b7OHFxoV05fnPcssoy_LBwx5bYm9TdeIArc2cuUVlTn2b8ArlvNpDCG8ukb6qucmkWP4keaM0q1N525cOWoMdcCHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca5f42c66.mp4?token=NctiGj2uhYb3el30Q7Wy_IEAFgo_27izNzOHmgmlW2dx9qLryak1C7CsJPzGwvcX-MEJ7sR0Sfc9bOxwUNyCcTUb2ozva79VpcSbcbyn4DxcBpbl5nPqqJU7T31KE2HVU09xZm0YOL5Ef6ZAfBCsaKJhmi737BQ6npq31JDgO2ZPMZpsr78gqSFEZ9Ea7_X2BVbEBw8PdVFXeBd3lvb4zqOvWtNv5wrCiEOYNGhwlyPIpkRuRR1Gzw3tmRZDa0H5q-NGZI39G-RVrMsV1zehfR78Z6AaPfPmQHd1Jf3EyAKzXH8iGtTuttVsNJD65KmR7PKQk9KFZC9Iptz6k_ENIjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca5f42c66.mp4?token=NctiGj2uhYb3el30Q7Wy_IEAFgo_27izNzOHmgmlW2dx9qLryak1C7CsJPzGwvcX-MEJ7sR0Sfc9bOxwUNyCcTUb2ozva79VpcSbcbyn4DxcBpbl5nPqqJU7T31KE2HVU09xZm0YOL5Ef6ZAfBCsaKJhmi737BQ6npq31JDgO2ZPMZpsr78gqSFEZ9Ea7_X2BVbEBw8PdVFXeBd3lvb4zqOvWtNv5wrCiEOYNGhwlyPIpkRuRR1Gzw3tmRZDa0H5q-NGZI39G-RVrMsV1zehfR78Z6AaPfPmQHd1Jf3EyAKzXH8iGtTuttVsNJD65KmR7PKQk9KFZC9Iptz6k_ENIjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهره اصلی اعتراضات دانش‌آموزی فرانسه
با چفیه فلسطینی که در یک ویدئو
رهبر جناح چپ افراطی فرانسه را می‌بوسد.
ائتلاف ارتجاع سرخ (چپ) و سیاه (اسلامگرایی)
همان دو گروهی که عامل انقلاب ۵۷
در ایران بودند و سیاست خارجه و داخله
و جنگ و بحران و تنفر و انزوا
و عقب افتادگی  رو برای ایران آوردند.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6803">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=M-vVWDWPMpJivFZZuZTORBlAn-bTq9TVe-Vp5DSpOHoyuS4G9pi3FIZycXMb0Raxuzhkf_bNWBdw_842bXeSP2M5ubJFsRu63lAhlXm9UKXCx3EdSAgH97KKyJ_SQ9Qb9YUdZE402RewgEmilvsRuRNFHhCKF9QhmSeJNWNtzGhvHmFhFt4YwsGpn0vdQg6yHx7niYLF0yCpKmGW1UYEaDexYQcHhw1u1YDMvzHBa1q-QfmSbthG4qH980sC_2yB80RfUP-nI0phoX4W7KKPhSO80Uouu__F4H1PyBK5iFnzdVyhRLbFOOepkzztX1nA0ioBMLfspsM4o9E51VFGQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=M-vVWDWPMpJivFZZuZTORBlAn-bTq9TVe-Vp5DSpOHoyuS4G9pi3FIZycXMb0Raxuzhkf_bNWBdw_842bXeSP2M5ubJFsRu63lAhlXm9UKXCx3EdSAgH97KKyJ_SQ9Qb9YUdZE402RewgEmilvsRuRNFHhCKF9QhmSeJNWNtzGhvHmFhFt4YwsGpn0vdQg6yHx7niYLF0yCpKmGW1UYEaDexYQcHhw1u1YDMvzHBa1q-QfmSbthG4qH980sC_2yB80RfUP-nI0phoX4W7KKPhSO80Uouu__F4H1PyBK5iFnzdVyhRLbFOOepkzztX1nA0ioBMLfspsM4o9E51VFGQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGOey_jBLBxLdpyqfgjQ6yjG5SXM9Y_BC1Eo5u_9ziTd6Ab5PkydFXpZzms3lAZB_iZdgrzXGZKHQRgFhZlmJS0jhYIvn2r4ycW6xwUW_0P9eoijkIqy2OZjJimxkyHSiozJ9TDjd6yLoKb2ImlGI7t0PohtRx39at9KRyV0B5HzsaOv1oY-ljON9b2-nsRWHKTBIyBol7VSalGopyUbArXtwPX__KIND5nyLA-SampYzI8g1nbGfBZQix2VlT2UheRd8wHJDbCgHSnc_M73t6eF5kLetBzD2mhkqG_bi1eUxbiqhHOewnjflG_96sPseWlvP88SFuAk4UdM9m8KLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6801">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVSSSoBFcueDN7cZPuL9S2uU8g79KviGtO2fanbA9v9_NGYmgtKUIl5_D9Y_UlOdqHRZ-Rm0n4b_jv06gpuKXgPv7mtqWrS8lIS3uXihzEtgr5iln4J_Z970PcSDcSDhP8EoIAqHyOAeXhzIUuycP0-40FC12VbHY0W4bWl_ShOgZXi0hAKjIYCjMQakEzkWx56Jl0rdPQ7C1YEOXyHYJdGhzvT4AR3Vxe57xbyPPzu5WUQ8oyxexFTUqcpJv5dNBUdVDtkLOxHU6eD0VyC62J9R3pMiz3HL4-APYPFfpwMUJzPkjg1qOGcUSxUyR9mpC2yLo5BAdotGGWY84VGcQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن
که آخوندها دائم به نفع خودشون و شیعه و…..
استفاده می‌کنن
آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟
یعنی قرآن وسط تعریف یک داستانه،
و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل
و فرعون صحبت میکنه و
اینکه خدا اراده کرد امت بنی‌اسرائیل
رو  پیشوا قرار بده و البته «وارث»!
این آیه مکی است و این نکته مهمیه!
چون آیات قرآن در مکه همه در مدح و ستایش یهودیان و مسیحیان بود، تا زمانی که اسلام در مدینه قدرتمند شد و شمشیر و سرباز هم به دست آورد!
اون موقع آیات متفاوتی نازل شد سراسر سرزنش یهودیان و مسیحیانی که مسلمون‌ها  رو تحویل نمی‌گرفتن!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6799">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=OqiPacSLiV-543iADiGO_l_rqHorI5n9q4lsQqPIwLiJssmCknCjfqr86LbzvPbORXPicUUdKS7nylB-4oCfdMvZ19bAzNeR22-4sK5k4jPCYDNs28crux6t8ulqdhtIDv7oq5v86N8stmRgnIZJfpWqob08fxeHJ1CWbsRpJzrToFp3Ad2IodSPtHBjP4X91xXtK7lrxalJGHfKsTViiP77V8hCwj6vbcPne1CvOC0j_zd070cSGmsIpRptm4qvfmRP0uM-dxvNHgPK0ZTLi-rKdQhlf4RmV3rFwOsvmUPjaxz5duI0IjcOyb9BXSS71IyRzI5hRVIIHrnV3uhoa13JWCEvlmqPn1lMpBsSmaVRdEWrzVmT24UnmQVU7EIBsBSqcnPT0QQ4PblStEBseKMG_d-3mz8GVq9dotcqmXDw8_pJVCxnIJYCSMFIb3TXYPdWmg1MrZrjMdqb1yMV3izAmHGDeeAPDmr-6eUdPOMksL-hzmO7-lk2scH6PRP4GZCBRiAcPiyTynLBr5l5o7ocHsThmbNcqX6H0i2CmUac_MJapiMPT82Sd9Rf3M857oC0CmagDW5EKQQEscLRiVldJgX64YKFPc-76mCnTG-DBIawjAILCvusNy4ijoVe8ORpOE2Ib-3Hiz5z1ZVfinEGXcC2iaJnuFJsKSkhngc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=OqiPacSLiV-543iADiGO_l_rqHorI5n9q4lsQqPIwLiJssmCknCjfqr86LbzvPbORXPicUUdKS7nylB-4oCfdMvZ19bAzNeR22-4sK5k4jPCYDNs28crux6t8ulqdhtIDv7oq5v86N8stmRgnIZJfpWqob08fxeHJ1CWbsRpJzrToFp3Ad2IodSPtHBjP4X91xXtK7lrxalJGHfKsTViiP77V8hCwj6vbcPne1CvOC0j_zd070cSGmsIpRptm4qvfmRP0uM-dxvNHgPK0ZTLi-rKdQhlf4RmV3rFwOsvmUPjaxz5duI0IjcOyb9BXSS71IyRzI5hRVIIHrnV3uhoa13JWCEvlmqPn1lMpBsSmaVRdEWrzVmT24UnmQVU7EIBsBSqcnPT0QQ4PblStEBseKMG_d-3mz8GVq9dotcqmXDw8_pJVCxnIJYCSMFIb3TXYPdWmg1MrZrjMdqb1yMV3izAmHGDeeAPDmr-6eUdPOMksL-hzmO7-lk2scH6PRP4GZCBRiAcPiyTynLBr5l5o7ocHsThmbNcqX6H0i2CmUac_MJapiMPT82Sd9Rf3M857oC0CmagDW5EKQQEscLRiVldJgX64YKFPc-76mCnTG-DBIawjAILCvusNy4ijoVe8ORpOE2Ib-3Hiz5z1ZVfinEGXcC2iaJnuFJsKSkhngc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو روز پیش به فراخوان یک اینفلونسر مسلمان
و هجوم جوانان عمدتا مسلمان در شهر «وینچنزا» در شمال ایتالیا، شهر  به آشوب کشیده شد.
در این ویدئو یکی از دیگر از اینفلونسر‌های مسلمان رو به دوربین به صراحت میگه :« باید اصول کشور مبدا خودمون رو به اینجا بیاریم. باید به کشور مبدا خودمون احترام بگذاریم.
دیدید دیروز در فرانسه چه کار کردیم؟
همین کار رو در این «فاکینگ» کشور [ایتالیا] ، این کشور گوه، انجام میدیم! تغییرش میدیم ، مگه نه؟ تغییرش میدیم!»</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZyMKTdo9tWXDm3IqRKfNsXOxqzuQMJD6G6ykThT6dv-2ySnIhM4CKMENeOZIDBV-Uo03aOSUw6Hma64vVk2AQycakTqlgS5P4AjEOgEcNVF03q9FY2ZJU0p4IgWAXmSy_UFwdmS3-gM9-tMIO949M7VMmg89GAtchbctA5bchSBat6yhElC3zpF_E2OeDXKIIfMHNIm7MKz-eDch7RwC7P1bPLUrkwdw-J7XLO7A9j_4BtWfNeckGE62fg0ZdM1DQ9-7U6e-HRbYmQubQ3PPvgu1Yp0uTvKB8m4V3i6pognp0WnoV4k2bbKvsjIFrn-6ZpYsMYuyDfilgH3U4M4hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6796">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CuU_5cFBShMrvn57Ih5hrOHsJpMdyIjnbaRw4iR7zkp-5v1daKeeYqBpau1V7b2T_ugDLug8rfXajC80-h3BM2OAjCBvZMdhPUBvgJkrsHJULu4RhiGuOwSIzIC_V3507TTMga9ZGcs6DjCbIht-wYx6NTod2uRqaG_n-c8tF3rk-ooLVFgv8l2TBNl0yBJzq84EoTDeWvREsdPEBK3BeO1qzOcBy9lDypM-_BTiyoWOTW92RQxTQJjHKCfLiFMafqCmUrkHJWxaITKAEBHvMEUMWPa25Zm5BIh-XX4yI0U6XJ9V23bVja8RKflmnVxvDjJrlTpMW2AxOkJhIOR0uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NVq3mZsFqs0CVPqRmqvcuHjWpix8wwbUZrRHr6t34dwA8mYUVISm7TO9D2_HQPRY-i-5M-EbKzs7QBNfKJT_27i4Q6f-wuICk_VMszmonBtI1DVI1fMO-fn3fEEc_dFmNgstTOLUJephE3gVgoN0bBML6PCqmpO58fQOaVX3kj1-VzGi923zLeYHi6B4fsang5qP-rUoH8L1M1TzStLhiCX665u6P2euZ7pfbZVEgRqRoZpusDiDdXgIf4v8IBx4ncXdtRH8mUZPKYHvBdMbSjjxzm9r_57icCmANL2rDZP5xObk4CYUJaGeJfXYm2AaOlARqrY_FLXFU2Ees9Jrqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»
در تخریب‌های اخیر خبر میده.
دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.
در حالی که اعتراضات دانش‌آموزان فرانسوی
کاملا مشروعه و دولت بهشون مجوز میده،
عده زیادی با پرچم فلسطین، الجزایر و مراکش،
در تجمعات حضور دارند و دست به تخریب میزنند. دقیقا مثل هر بار که بازی فوتبال هست
و همین جماعت شهر رو به آشوب میکشن.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6795">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">می‌د‌ونید چرا جریان چپ اینقدر خودش رو
هم داستان و همراستا با آخوندِ جنایتکار دیده؟ می‌دونید چرا اینقدر چپ از جامعه ایران
متنفر و خشمگینه؟
چون همه هویت و هستی اینها مبارزه با آمریکاست!
ایران اگه یک پایگاه ضد آمریکایی و یک کوبا
و یک ویتنام بشه براشون ارزش داره!
ج‌ا، چپ‌ها رو قت@ل عام هم کنه براشون مهم نیست!
چون هدف و نقطه مرکزی آمریکاست.
همه هستی‌شون در این تعریف شده که جایی آمریکا
حمله کنه و اینها سریعا بیان وسط میدون
و ضد آمریکا شعار بدن،
در قضیه ایران ناراحتن که چرا آمریکا حمله کرد
و اکثر مردم ضد آمریکا نشدن؟
البته به جز اقلیت مزدور اسلامگرا و اقلیت بی‌آبروی چپ که هر دو اساس انقلاب ۵۷ رو داشتند.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6781">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید
که حامیان حکومت،
در دفاع از خودشون میگن :
بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل
شعار میدیم، ولی کدوم کشور به خاطر
شعار دادن و پرچم آتش زدن و حرف،
حمله کرده به یک کشور دیگه؟
البته که همین جا هم صادق نیستند،
چون اونها فقط شعار ندادند!
خامنه‌ای رسما در برنامه «گام دوم»
که سیاست‌ها و اولویت‌های جمهوری اسلامی
رو برای ۴۰ سال بعدی تعیین می‌کرد،
اخراج آمریکا از منطقه خاورمیانه
و مبارزه با اسرائیل رو رسما جزو برنامه‌های نظام قرار داد، بگذریم به اینکه در عمل و با افتخار و صدای بلند می‌گفتند ما به گروه‌های تروریستی حزب‌الله لبنان، حماس، جهاد اسلامی و….. موشک، سلاح و پول میدیم برای مبارزه با اسراییل و….!
هر گروه دیگه هم بخواد مبارزه کنه،
بهش پول و سلاح میدیم! اینو خامنه‌ای هم علنا گفت.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEUHTaWoZffg2e7agg6jPOuts1SS4jVWKZoS7_ewaLzuw4qAWlrB6WWaACNC1Pw4sHjp2G1mcKcHJlG2E9nzsbmUTqcWw1p11YIfagDD7_QLuJBAKDCBsdmgeDFuhbOXR_Rvi3i8mEG02uJOsEF6gA_tIP3hC8YaMJwkXDlPH5irenpKh2CWqpTcxuZEkla9hvCABB0C1lqu_5HAggyh2qXzcrSqkxI92MHUyTV4OKHj__mhMhyPfP-MqG3cx0DIy1fD3bQCbJ03382tvsQU8IVVA3yKargpK5GDISW9htT7GAwgJ4G2rCIUuWaHYwJWNXr1axv9Q2w6PYeM-YLUrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یورو شده ۳۰۰ هزار تومن!
و دلار تقریبا به ۲۷۰ هزار تومن رسیده.
ولی یادمون باشه که بزرگ‌ترین
فروشنده و عرضه کننده ارز در بازارهای ایران
خود حکومت و عوامل حکومت هستند!
ارز دست اونهاست!
صادرات دست اونهاست!
حکومت و عواملش خودشون دارند قیمت رو بالا
می‌برن، تا ارزهاشون رو به قیمتی بالاتر بفروشند
و سود بیشتری به جیب بزنند!
اساسا برخی از دامن زدن به جو جنگ و التهاب،
کار خود حکومته و مافیای حکومتیه، برای افزایش
قیمت‌ها و افزایش قیمت ارز
و افزایش درآمدهای خودش!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oB_U1s-8rMcNPdT5zV9y5kEKia_q2Bc97ApiWpVVt5myPtU6tS4sMg3BvKJpET7aVmveGPgHVotolIVMaqws0RdAF1ILB6-3Hm2_BW-6I2ZM4KMVNbm-r2s2nN2Ofl2Nq74_AuF-809EUDatdD9azf9uKyZ_Ay96oOMN2PyrHYDU1slMV_22Zzt8ZJ61x6HmmjGyKbosIdV7RpnIprzgiTV7emP4MYnU8wkHpQBh5SBo-eROv9yXV-ex7ui1a2xja_VOVossrFsz3NDhKyeJa06EihH96t0vvNcpFAmM0pb0gHIeaBHdtpC1mBmhiRKjSHAytS0VDeazt_cYdXN-JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SD3vDeAlBVOxSRcsNlN3fWsbmWSUXueXishoJNc9kh4ZIgzCK1n2ug0Kq5gYo_Tlb0Tg4j0liQLApET6aDrMCwdRD4kSdPKNPbuos7n0DO1Sj_ewgeMDeTHYrxXxy3vNHfgYDVSN2aw4A1JPW3Rud0UL_CTeiBnG8yNmW214z9S1fybQbd97r3Iv9x7NdFj851rzYj5t5kfLgQOC5Cy_pDy5H1G9uW-uyQWE_nW9S03rox5q49r4XRpxdi_Lsg34yWU15FGIBfBYngTlXC0mr3h9V6ZnRmJFqL_44LGAjLalmrsUDlTrw5pG-M-ex_dC6O8yr8anT6OZpWxzSvheFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=OXOTUPutJCgVbE1YgOY92yJzKeg6yTa_1l91xreuTx-SZpHWKacwBsnOR2jF6uEVfUkrYgdpercOLan8UY88ZR94AdA0QTbbFwNwU1Jh-sUb6UIqt2EIRb9fs2XYD2KnejVAqKhrE4Jb_coQxWJxSKF0rSmTW0wexz7YnXLrEfDsMBnBdCGpyS_D-d1Y1dAyxkBTQtU2q255TjJPM03B1NEjmTfR74hYJU92WdJ-ZqM06DCQ_0IySU1Nxl3qaRklqKWQxVjrpledSkk5flECuqNc3W8w6BfG-NimNa5N4N0X5vtzR_6CD_6UHQqt0lxw_YwPZYaSQMpl5OKLu9rSOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=OXOTUPutJCgVbE1YgOY92yJzKeg6yTa_1l91xreuTx-SZpHWKacwBsnOR2jF6uEVfUkrYgdpercOLan8UY88ZR94AdA0QTbbFwNwU1Jh-sUb6UIqt2EIRb9fs2XYD2KnejVAqKhrE4Jb_coQxWJxSKF0rSmTW0wexz7YnXLrEfDsMBnBdCGpyS_D-d1Y1dAyxkBTQtU2q255TjJPM03B1NEjmTfR74hYJU92WdJ-ZqM06DCQ_0IySU1Nxl3qaRklqKWQxVjrpledSkk5flECuqNc3W8w6BfG-NimNa5N4N0X5vtzR_6CD_6UHQqt0lxw_YwPZYaSQMpl5OKLu9rSOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=Pdbni0ZOvMnnsgO4mwPRBR8t_SBxMNyBqzZLkIPfsSiSorLpk3mm-D2sx8xvLddRnAXFapdJjuO3Xa7GvxC3ZeqBtAR6UA-vb_fZ3DryYHwH2p1rVOnKBtRTPtu4q3usHOH9Zp_K48AaZBJb-z9I-iYuVp4C8oxkOR1X0oXstdrVNHmrhWvrjb3TIXuSkfuooi6QTE75hrpoAvug-5or3X8wcXoKH9UY5JQifFcxoj7r3yWRhERQDFD3WITsld3dqibi1OYIuYPhoH8pKH9usXiXUII2pP7qvrA3c5r2ll-krcizcCHXRbEnLy2vyoM73iLB1H78XPKL-2YlE7pJtrPCTlrf5XBj-QEEacfEKxWrg06xmfZwkzzpP9OabzsTREM0DntyVjbuPrqEdeXwmY9IrAu5zHX7rf10KItfMnjKnLm2zm2Yz5LzSeAIjpSmZkIpbHfRg-SIsEcJWXwfHlE4Izu1E-agvzGvklCE2Lur5R9XbxWNxDQPFq8FYqggV9e4IVQ9y0WHjkNHZdC1REFs3k-kXJO2uBwkUkAFqrRmTVp0CS_DTGcfdtQZ9DrSaf_J8pAMoUmdMCDTJUrD2IMO_p0HndhhEW-1tBZD5DZJbR52b-jDuWletq4CVta6U2mxP95B_2TKJKGTZVS1_AOJ_6QM32AlTyBD2iS9Wds" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=Pdbni0ZOvMnnsgO4mwPRBR8t_SBxMNyBqzZLkIPfsSiSorLpk3mm-D2sx8xvLddRnAXFapdJjuO3Xa7GvxC3ZeqBtAR6UA-vb_fZ3DryYHwH2p1rVOnKBtRTPtu4q3usHOH9Zp_K48AaZBJb-z9I-iYuVp4C8oxkOR1X0oXstdrVNHmrhWvrjb3TIXuSkfuooi6QTE75hrpoAvug-5or3X8wcXoKH9UY5JQifFcxoj7r3yWRhERQDFD3WITsld3dqibi1OYIuYPhoH8pKH9usXiXUII2pP7qvrA3c5r2ll-krcizcCHXRbEnLy2vyoM73iLB1H78XPKL-2YlE7pJtrPCTlrf5XBj-QEEacfEKxWrg06xmfZwkzzpP9OabzsTREM0DntyVjbuPrqEdeXwmY9IrAu5zHX7rf10KItfMnjKnLm2zm2Yz5LzSeAIjpSmZkIpbHfRg-SIsEcJWXwfHlE4Izu1E-agvzGvklCE2Lur5R9XbxWNxDQPFq8FYqggV9e4IVQ9y0WHjkNHZdC1REFs3k-kXJO2uBwkUkAFqrRmTVp0CS_DTGcfdtQZ9DrSaf_J8pAMoUmdMCDTJUrD2IMO_p0HndhhEW-1tBZD5DZJbR52b-jDuWletq4CVta6U2mxP95B_2TKJKGTZVS1_AOJ_6QM32AlTyBD2iS9Wds" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXL2c7yIabxRiB07U1qwWGe-PdjapHmX1Lmlj6_PhFfqBH4Fe4hENhq3FMLuXuxaRgceFJC_th7gM4J1ZXoheOOtnoHmsGwOfzn71Qi3y1z8CXhiVX1PGqNOqaxszjl8589deGJt_h5TJ0FaPFK5RxeOaYXHKb6Fd988MiEk6OCBKT41tEDsqXVd6WMnXjRRlbBaRtmvUI_gJ9Pqt6LEmPIOAjcYWOJno6CsWCteCdM6PzWFMrGdUZpavuOpoc-aWTApIDbgcUMCtouUamSod279b5ekcENg_X0IG95e7ajPQ7ypnWysTMeAWma407Lp7yFV6SmIkpXfJMGleiNrkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lvsYWnNKrPYXgRuzfkfhCGjVJQPanDS3Y9vKoQU2D3PMfFqEGMzRU4hsjhta0Rdrg8XTKfxBmNX1_goB60987DBxkMSsbyrgL9fgIGz9yrUICMb_qn0VtbzLIj-R6JcTijnXu1p5Cn4Wh18-yBJn-CmFwtIeF_h5A7xMArSlImIguLUzuuIE-KCOOViT0XVtcrtG9I37O9oVyVrpfNb8kDKQh_c3NJ_PG9yejRoZhbLMxDkzFSiZG6H7MqWUBnVZ_Yz3sN3C8zBM5P7WdZ7v9aNL9tYbc7iweGhp12OO7nL7LXs7tkH8b5VdEKkJi3DUktdU68GVjTqyBgZZ7iUl6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h1edOF9OKV9QEnOaRvmNAOl4R730AYl6AdrxUcmaoX51cofBKhZf7A0ew1fimBRk5WWdR3N7-vURm-8B3t5FIqEJcBhUsu2Twz2DTluESZLLJnv972tnhU3FBPbm7HSOnfZSqwXf7uG8dnW5G9V5zWNIR91Lpxte38PTvYa7hP6de410KiBAsMu9eHNScWs53hrARVa8CozeH6JeQzxgRcYJGbC8EuzLKVzlts07aFD7UaZz3CJKlyzor07_Udwm2rO5xa-c30GNKDNyIb4NHj0kT19VqxIcXn8DyVo80F0BjK2KMXCuYo9lvacER7QiAuKvaSDQkDWw06cs6HMynQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=DMZLPmXc0AEnaMEKK91FvbqXmncHr5hrLsself6SSIZfLpfC_sNw8xuNby1hA-DOzabQxeuCTUMi2BqEWKc-b5TfjsC2PYohlqu-J4UZDEJn2pULBFYBsY0HfARRHD-QQouxIAmUG0sMTBCh25iTubPAnzyrhoOAsSQQZlbEijMQxC1myO_gSEtbZkUzTBpEhp4vYjg16woamlfN87A_2PONc3pbfu4f_aK3MSrEXKcmMaGrcorBMEuCirlX-XYfQKWKgXG-AVpl-HW1-5t6qFOtffk5jJL8Ust0sfraU65-Kpo_WXWDjrxHSE-vZ4W3xG-kEyE6502uAEG81S-Png" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=DMZLPmXc0AEnaMEKK91FvbqXmncHr5hrLsself6SSIZfLpfC_sNw8xuNby1hA-DOzabQxeuCTUMi2BqEWKc-b5TfjsC2PYohlqu-J4UZDEJn2pULBFYBsY0HfARRHD-QQouxIAmUG0sMTBCh25iTubPAnzyrhoOAsSQQZlbEijMQxC1myO_gSEtbZkUzTBpEhp4vYjg16woamlfN87A_2PONc3pbfu4f_aK3MSrEXKcmMaGrcorBMEuCirlX-XYfQKWKgXG-AVpl-HW1-5t6qFOtffk5jJL8Ust0sfraU65-Kpo_WXWDjrxHSE-vZ4W3xG-kEyE6502uAEG81S-Png" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش
حسن نصرالله، رهبر گروه تروریستی
حزب الله لبنان، برای چند هفته،
ویدئوهای تهدید آمیز می‌ساخت!
کج نگاه میکنه! انگشت میزنه روی میز!
رد میشه و…!
رسانه‌های جمهوری اسلامی هم جشن گرفته بودن که آقا اسرائیل «با یک ویدئو!!» بهم ریخت!
تا اینکه در روزی چون امروز
(۲۷ سپتامبر)  ارتش اسرائیل با احداث یک گودال ۳۰ متری (به اندازه یک ساختمان ۹ طبقه) در بیروت، به تهدیدها و ویدئوها  و گنده گویی‌ها پایان داد!
به همین سادگی! فقط چند ثانیه زمان برد!</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=HG7dayS-Q73uapEvR5IwT-i-TvXAxdc3VHLZuIU2urmV8hh-13QJEz3MrIUvcKknxWnOTapdrappwtCh2Z3r2vp1r6NCRqZzGsLi216gmHE5EbK1YbIUsEd_fMWDkbL16AwrBtY0vkekEPFCutcv9G2d3XmD5KTfFJc4biIGWp7K9lHsuk6WogbwooppBcTFFZ1pcDlKtyyjp6FWZEWQHg_6DNF1HMFh_tC3aI17KvO8oawB6AhCxFctt7RDnSXPS9L1RLJpviM6MmzTZh7AsJ4WZD89Z-bJP3SO6i_GFaOIHAiFVMkrLvpbe-LTaMg6R7QWQB3KLhTZMEW65RmTDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=HG7dayS-Q73uapEvR5IwT-i-TvXAxdc3VHLZuIU2urmV8hh-13QJEz3MrIUvcKknxWnOTapdrappwtCh2Z3r2vp1r6NCRqZzGsLi216gmHE5EbK1YbIUsEd_fMWDkbL16AwrBtY0vkekEPFCutcv9G2d3XmD5KTfFJc4biIGWp7K9lHsuk6WogbwooppBcTFFZ1pcDlKtyyjp6FWZEWQHg_6DNF1HMFh_tC3aI17KvO8oawB6AhCxFctt7RDnSXPS9L1RLJpviM6MmzTZh7AsJ4WZD89Z-bJP3SO6i_GFaOIHAiFVMkrLvpbe-LTaMg6R7QWQB3KLhTZMEW65RmTDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vz65eKqzCwzbiiiufOzSz8UaBpkWBOUx_K3y_IZzsYZUtLTN_B19lIzZZ1rvdhP6icuK5Tq3es8qqGLrZ4yaI3wmrweO9b5Q-lFpSxR2Y8GPFbn9855I6L0EHvigvqJWudGMwVgWj3lJYaiRK6glmsmrJdAX1l3-mGdzHKQVOHJD5VTXljVugOiidrXH0T7YBJp0TuC1WQoDIKtWj_JTcokZqerbQpuUF-O_XZqdJ4n8A0K9zf64pEbfVJah_2K0L_TqYnXXizZIEVXosdPMqcUlIns1SZrh9iXtiIixFq7thBRRXfpSgzUeZzUS4irhrYx2fUyH27usTvaKeMbf-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=ch8lGKSgRS9UgZeFWofBZraB4kNCSOe5DTdbNf9ngrIYOppgm9k7fAZp7RfInUjj2O3Zhs74BCAQIjLSr_9AS1cWYlMFgOtv4MUJ1t3djJ3VZV8Y1_spdSIJCSonBjfLieLHz2MxQGzIv-CX1DmcpDO85eBkdAkTk7vIUcfaqvcCvg-Cc4m0vnfq9Rr91GkJxdAKVONeXVT553tnsfmHmg-eWMCcehYRt5A2zAFCnzBD6bETm44yPB8rm0YftZXGz7ZZ9EAvQyU_5JDBI8ce-d1qfCOrqdKsk6UXc9YOkkL15dpSzxvE2vl2gT8e5yCfzttCdsl4xULOYKxie2gBMwyslcvhcbwOoUlzU8O9-T0Y5FqM3WTpAw0rrxeBcjJz1xEccqsgNa78QyaxqU0T9EN5qSsx9sC6CETN-IT02qz_MoR6KhMBENnfgRvIsF0LweDQ2S06NOy5llnT_4CFX8qhKs5ZdMd7aT08aMVyAPtNdyfE7kTU9qQv3KNuXF2GfnDevaPN-orNx8PQvdWWQ3ZJXJKBs3Jj64RkGg6_HtJPKDojqb69yInyQ7RnJwgeIuKG7PUR6y3bd-70ulLclRtkTuMya8jG2ILUIMKjNXHtdTKsRocs1S-d-PN5EjLbyuDIfr8Hf-rNfZmUYyk5fCZp8nNRCRhukRZuv4b9gF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=ch8lGKSgRS9UgZeFWofBZraB4kNCSOe5DTdbNf9ngrIYOppgm9k7fAZp7RfInUjj2O3Zhs74BCAQIjLSr_9AS1cWYlMFgOtv4MUJ1t3djJ3VZV8Y1_spdSIJCSonBjfLieLHz2MxQGzIv-CX1DmcpDO85eBkdAkTk7vIUcfaqvcCvg-Cc4m0vnfq9Rr91GkJxdAKVONeXVT553tnsfmHmg-eWMCcehYRt5A2zAFCnzBD6bETm44yPB8rm0YftZXGz7ZZ9EAvQyU_5JDBI8ce-d1qfCOrqdKsk6UXc9YOkkL15dpSzxvE2vl2gT8e5yCfzttCdsl4xULOYKxie2gBMwyslcvhcbwOoUlzU8O9-T0Y5FqM3WTpAw0rrxeBcjJz1xEccqsgNa78QyaxqU0T9EN5qSsx9sC6CETN-IT02qz_MoR6KhMBENnfgRvIsF0LweDQ2S06NOy5llnT_4CFX8qhKs5ZdMd7aT08aMVyAPtNdyfE7kTU9qQv3KNuXF2GfnDevaPN-orNx8PQvdWWQ3ZJXJKBs3Jj64RkGg6_HtJPKDojqb69yInyQ7RnJwgeIuKG7PUR6y3bd-70ulLclRtkTuMya8jG2ILUIMKjNXHtdTKsRocs1S-d-PN5EjLbyuDIfr8Hf-rNfZmUYyk5fCZp8nNRCRhukRZuv4b9gF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=sGZdnTIs-_r-7jFe-fzLGHLJR1ljFrgFzSm_Zmhcwe-hm18NgSNW5QfvjteoGCNGDee_GaINgo8owIkfPAUGOmHVR5UZ19jjtUzOQGOCshevQScklKOFTjgyoD2uE944KvzBgy0BrcknC8CAic_nCm36kulMsT8yUANl7utY8pqy3jGiHtWWREjEOdOkZWZXwcuLiEf04tKqtJZdGwuqq_q1pLjnDzGXT7Kv3kRgx3gSfAphOmiENpJXjOTdzHxCFnbAGympy1m7ge-db3ZHcEoQ_EQmd2lhD_ccBrgpugCoyWAL3s1kux9v7Yp4S_M1VqKFOq2Z7uOPCsbRVWI7ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=sGZdnTIs-_r-7jFe-fzLGHLJR1ljFrgFzSm_Zmhcwe-hm18NgSNW5QfvjteoGCNGDee_GaINgo8owIkfPAUGOmHVR5UZ19jjtUzOQGOCshevQScklKOFTjgyoD2uE944KvzBgy0BrcknC8CAic_nCm36kulMsT8yUANl7utY8pqy3jGiHtWWREjEOdOkZWZXwcuLiEf04tKqtJZdGwuqq_q1pLjnDzGXT7Kv3kRgx3gSfAphOmiENpJXjOTdzHxCFnbAGympy1m7ge-db3ZHcEoQ_EQmd2lhD_ccBrgpugCoyWAL3s1kux9v7Yp4S_M1VqKFOq2Z7uOPCsbRVWI7ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrg0UupR2NgInOIaFyeym9FwVpGeDANPSggVUOignRzOnPS9TMwz1-f47ykQcX1Fnku0gkRhjnvWOu6DVb2tO9PoYE51zffuHcGp3UKuYsvOsWeVCJ6hwVaHO6im5nbAgR4Rdc4cS84wlfIiKPSTTkz9QKn7bRL4tyGmo3GOfcvMKlAAj4fGWPvfY6u03T3mM1eK4_5G-tVZ3yvoB09rHoI_o4v4YOfhebim_KTMetMx-F0vc9_U5dcDLkxOUcBho6jXzQbFMujkJqLBLEsGl7ehCq2zaYJ7QIWt-onRy1oE_S38bRh99iyCxmhR94qBCA0kfOnAoQV5FjIYA2s6SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=FynZ7GcqTU0PtqB-hs8d7tLcWW-C-JedVnN8sUAYOknGd7jVliQR6gCKG9rx649M-52tS-fTbWbbpXtwKw6RRIcQvLoa1F_ZLtvuzfEF6fJ3YDJVHZWvaBd87x8U7IxhmCK8uUPXw8yOrq-EOMxx_XE3NRRXsx3lAA0o7hejbd81ORNq8IXBdPoUeRBYPjNRjrS7PRgp56t_0vXWL-L0tg3JwKfcrfK986fgk1SIQcnYhkqeaiwuekkQ9SQoOtombgkNWOhFuQgFO8ezk4bGKZ7MUctmcqTIc7P_FGf8rdWm4i3jjR6wu1XLwb-DijFjqN-l2RZOt8UUD1xu_D-w1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=FynZ7GcqTU0PtqB-hs8d7tLcWW-C-JedVnN8sUAYOknGd7jVliQR6gCKG9rx649M-52tS-fTbWbbpXtwKw6RRIcQvLoa1F_ZLtvuzfEF6fJ3YDJVHZWvaBd87x8U7IxhmCK8uUPXw8yOrq-EOMxx_XE3NRRXsx3lAA0o7hejbd81ORNq8IXBdPoUeRBYPjNRjrS7PRgp56t_0vXWL-L0tg3JwKfcrfK986fgk1SIQcnYhkqeaiwuekkQ9SQoOtombgkNWOhFuQgFO8ezk4bGKZ7MUctmcqTIc7P_FGf8rdWm4i3jjR6wu1XLwb-DijFjqN-l2RZOt8UUD1xu_D-w1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو و این حرکت
یادآور داستان‌های عهد عتیق است!
شجاعت و جسارت فرزندان داوود!
که در عین جوانی و نحیف و خرد بودن،
مصمم و بی‌هراس،
مستقیم به چهره دشمنان خود می‌نگرند!
مثل داوود، نوجوانی ظریف و آواز خوان!
خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه زده بود، اما اسرائیلِ ۸۰ ساله، از این نهراسید!
یا از اینکه جمعیت ایران ۱۰ برابر اسرائیل است!
یا اینکه مساحت ایران ۷۵ برابر اسرائیل است!
در قطع سر حکومت جمهوری اسلامی تردید نکرد!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taI_IbnFpoqLKUYVfTbTpHYrvpZTHTaJeiWAq7ERolmzekPD5RBrOqP0XwkeeAZkBk3fRLiJCg_JjRrNrFmtym252Z0WyoEUHXWqzKQDf_pKdl6N3TupvwazQ4ikF6GSs5Uf3TwPfO1cuu90TpxH-iwLtsT21hjKqPdqWbYOk6VPzDlDmYgPx_jqDL5wFQ2eanZSdgu4bAAZMfeauKxYem0GVVwmeJ_HButkHpXkh2-Tf8mchDO3xQwizi-L_2UZ0wgV4GOR3RhnUyDU7XSPXHcAs8SS3rTfCfNu-o4mQkmXl_Hj_ibY3Y6jcmEKwYDUfhzR97jDh-1_UqEc6eKxow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QpxhcnZU0_48Fuqjja5Mh0c8MeyBy2vaiChHFPj-uKAlwsef8ZUN6wfmKx_2RSv3RtM1N9lwMPqftmYXkbbxidRxG52IFL5PuWwpOeJjYG89rrR-sIXsnyD6nl_JEI_n3NZg55otpegdms27fh57ff0Xmai4dkykU6WoIg7wAHmJFVRatzaORtOJztU4fciEtE9qyDiS501XkoBVSPTlJhByGKOHFRCe5fnpsYv-AkDO6vqGNnT2zkk9lRjpehSR9o1GMQoDkbTe-nfpiyb5ec-14clQXvXfpxWPYYMwR66zdneSMp_e8mrm6gYOjH-wDx9Cj54hZnquUt-8BU9eGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود
که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.
.
این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،
و نقش میانجی‌گری این کشور.
(وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،
باز هم ترکیه این مسیر رو باز نگه داشت و گرچه  از انتقادها هم مصون نماند، اما کار خودش رو ادامه داد و سود بالایی هم برد)
🔴
با توجه به وضعیت افغانستان، پروازهای ایرانی به سمت شرق (چین و..) هم احتمالا ادامه داشته باشه
🔴
و از روی خزر پروازها به روسیه ادامه خواهد یافت.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=BMZz8fyDXwCpxn6dYWjGZMDXraZyRMMDMq2Tu46b_P35_QQTITak4DIfUn06vcBu_u-hEvECMZT53ohb0aoyERxb0dYQRKYEvu8ak_A3BiVbyv_PVuW9Ug6qDB-fqoNxamwror_piBA8_WahZrWvmmTEGR1-GtN0JYo4KFTdh3SqC6ZCHMgjyQ-PzakWMF2KRVXpKcwgE1-acr0tDQ0yuT1er1O2XCKCHUwXyu3gnVdOu1x404TjPHFI7E9Up4htx8f1GLkpIdK7dU8U72in7EufPAQkpb6iZ7EaiMUTsQqbU2AKyjYcxJIJqXZN1wNFXkdqrPjooy8GYlPSC5HMv1_T1Il2OS8ZzvHtXJgDbRhygrsD0mfZ1dQfJaVHihEC5aGpCUrXkigmKRGs8GURUe9GK4f8tg32kRu28dMe0GFvj77VIr6FeNQS6tgn7T1XktNFaJyJBM3hll_q2RtN9S2usJvZY6Y5oG0V_Wvtey4ljAio_qdfUYU6wvOJZZNBHyLNUNxtpMeuvZBaWzJRtm0QGanmuFmt7PHsH8xEEFudyUwXI5iPtsSY6Evc-K9fYLoaD8VMUnoLMRP622Zbp_AKz0LEO0m6CEmaFX0o9r2FaMKbxfnVwe7plykm9YBHNAnoUuyg_9RBT55xOmvHi0Br2IjyevyWuwnnZH31Wtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=BMZz8fyDXwCpxn6dYWjGZMDXraZyRMMDMq2Tu46b_P35_QQTITak4DIfUn06vcBu_u-hEvECMZT53ohb0aoyERxb0dYQRKYEvu8ak_A3BiVbyv_PVuW9Ug6qDB-fqoNxamwror_piBA8_WahZrWvmmTEGR1-GtN0JYo4KFTdh3SqC6ZCHMgjyQ-PzakWMF2KRVXpKcwgE1-acr0tDQ0yuT1er1O2XCKCHUwXyu3gnVdOu1x404TjPHFI7E9Up4htx8f1GLkpIdK7dU8U72in7EufPAQkpb6iZ7EaiMUTsQqbU2AKyjYcxJIJqXZN1wNFXkdqrPjooy8GYlPSC5HMv1_T1Il2OS8ZzvHtXJgDbRhygrsD0mfZ1dQfJaVHihEC5aGpCUrXkigmKRGs8GURUe9GK4f8tg32kRu28dMe0GFvj77VIr6FeNQS6tgn7T1XktNFaJyJBM3hll_q2RtN9S2usJvZY6Y5oG0V_Wvtey4ljAio_qdfUYU6wvOJZZNBHyLNUNxtpMeuvZBaWzJRtm0QGanmuFmt7PHsH8xEEFudyUwXI5iPtsSY6Evc-K9fYLoaD8VMUnoLMRP622Zbp_AKz0LEO0m6CEmaFX0o9r2FaMKbxfnVwe7plykm9YBHNAnoUuyg_9RBT55xOmvHi0Br2IjyevyWuwnnZH31Wtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4leZNCNgqRbNF13ukbTMmmmW1uETYIzRKpAxpPPsefbSakN7k35wqP6mlNxI6Y9JAMdi_dWJV9PcEWyJ2b0M8Eo8Phd5Tx7hRlCSgbOT8QM54jxARfAVu07cSwC04C6HiNsGXqzorqIlh-tWv5FUZ-FJymMDWDDLhV6yB6FURDRyfB0yRgZ-pLM7PlBl0LF7fGwjFgRAYftG5Ak8iKy690MDPKDLWfzZQcbADMT4JQxumogvTUoG5vWNsHpnB60ONm2EXgZh7LYaTH6b3kHMM4XX0lIDLGxDyAyL0geGjxHYX42xr8uJl3iQacNg790gnPCgF-R33KftqYhknTNCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXkER1JbH2-FJ7BeavRLUvITU0zULBMaZBaNhJ2n1SV0SEc1xvdxH8hjBr5T8f7T9toAHjpevG4NH7qBSmGXmZZhXTJjxyI5iC0AiWKuFnziCrkuNfPVY0BlVnClAYSqlhGsz9HmvwOMYgEPBJZJhI4-14tIAfcASXGq-go-ZNy1ZSbOSSYwbNj5MEsqjQRH3ZIWUE1fLfLcYfR0QpgOl1ZgMrE6Dj_8YnJ2SPIE8qMowHSl6rjk5O6lFaYwcIvFuuOWMhfINZSN6BtsZCx0FL8YGKc6unpLxfUrsmDUgbjBDFn3jBhOIF1DAvyILZMm5ICvp_zR9WuA5V6swvfYQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=T05F6sJ0imLZTdSwma5KdGvTeucN6JRC1UQjvmJiGv6QvAhBfTOD97HBgckzNUklm_erC3hu7rVk3OVoLcAlOOxcPcwxLrHBu-FwPuMibE8tjPZjXOn0YLtDso1IeyifvvV2R4nrJiPWMDbBGGNTZTZNBH773T5mKQN_EZEv-VbGvd8ykHyK5YpFwf1OFEbmaQXh6Sgoy0LTlNSZT0S5BlRUjDxh_M3kW0vHMRbVq6Jwn_TLGbmWP0M5mZ3xb9v6I2GOKU9megwKuvT_OLuyG1WXW-KKI5R1Qa5V3CkBGLooU1EK0zTYG0r9N73KHMPGnP48LvKPzhtnGr7V2wICEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=T05F6sJ0imLZTdSwma5KdGvTeucN6JRC1UQjvmJiGv6QvAhBfTOD97HBgckzNUklm_erC3hu7rVk3OVoLcAlOOxcPcwxLrHBu-FwPuMibE8tjPZjXOn0YLtDso1IeyifvvV2R4nrJiPWMDbBGGNTZTZNBH773T5mKQN_EZEv-VbGvd8ykHyK5YpFwf1OFEbmaQXh6Sgoy0LTlNSZT0S5BlRUjDxh_M3kW0vHMRbVq6Jwn_TLGbmWP0M5mZ3xb9v6I2GOKU9megwKuvT_OLuyG1WXW-KKI5R1Qa5V3CkBGLooU1EK0zTYG0r9N73KHMPGnP48LvKPzhtnGr7V2wICEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=aA20b1-kZmFApNKnV39OH8cP5CFBmX7BKAsVkDkStym25zS3I0voOEVdac2qC47vwnU0vH3JiZ3luRnjcE3_SIlWogXYhEPmoh_a5ja-3MxEqzjN664Nsyb1nAhq4GdeooOi02R-nra2zvtcb0GlFfXcJCk9d1do9fJKHgwvJGczVKqF0dt91xf2i9SWATdGoyzGC68yy3MKkSRVEY9UNSMdLwclEnsWUlULtWKfDIXY0LTtfy-2AnFTF8a8ld_AAn0dX56_zoFNUnw-gBJ62ThYRYq_FBXVR7SBHizqE5WYY-fnnrTICN4ZjoLVA880B9eTFpz4kCA4gKjWZbyDkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=aA20b1-kZmFApNKnV39OH8cP5CFBmX7BKAsVkDkStym25zS3I0voOEVdac2qC47vwnU0vH3JiZ3luRnjcE3_SIlWogXYhEPmoh_a5ja-3MxEqzjN664Nsyb1nAhq4GdeooOi02R-nra2zvtcb0GlFfXcJCk9d1do9fJKHgwvJGczVKqF0dt91xf2i9SWATdGoyzGC68yy3MKkSRVEY9UNSMdLwclEnsWUlULtWKfDIXY0LTtfy-2AnFTF8a8ld_AAn0dX56_zoFNUnw-gBJ62ThYRYq_FBXVR7SBHizqE5WYY-fnnrTICN4ZjoLVA880B9eTFpz4kCA4gKjWZbyDkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=Q9tO59AsuvLBUh1yQmPCioCD89kiwL84jLIGb6xV9LewyaRegT-R1GEZgs1Wd5PNVCSTatZmpMNBKemEzRe53g7RHyTuRD0q6PNZQQDjbcVhc-fewgwS6d4ZHeXyzoMiJAY4A56gankpunpYdaxOWV8Aex6pRWtlBT0ptSbEMNaN9ydwBL6B2wx1-7oZGNL4mQR3BKCqCKtCrfvDwlfyW_eq3nAOAzim0dWxTkpkIKAgkclop_Mq6BuZfHR4yUykA0sw43pcXO357IkYzuWgqB4zGjnIbvEkuSDOEm5s6AYLkn_h_3Kfq1kX0fIyh8hj3B3cxrHbAkDBzRMYxFEB8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=Q9tO59AsuvLBUh1yQmPCioCD89kiwL84jLIGb6xV9LewyaRegT-R1GEZgs1Wd5PNVCSTatZmpMNBKemEzRe53g7RHyTuRD0q6PNZQQDjbcVhc-fewgwS6d4ZHeXyzoMiJAY4A56gankpunpYdaxOWV8Aex6pRWtlBT0ptSbEMNaN9ydwBL6B2wx1-7oZGNL4mQR3BKCqCKtCrfvDwlfyW_eq3nAOAzim0dWxTkpkIKAgkclop_Mq6BuZfHR4yUykA0sw43pcXO357IkYzuWgqB4zGjnIbvEkuSDOEm5s6AYLkn_h_3Kfq1kX0fIyh8hj3B3cxrHbAkDBzRMYxFEB8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lf7QGOrac9GPHtZRYj0tB-mIXiT9X88k1DdU-VuEDpdeXzKUKrI5Nd6qybiEeGhi63gpKZf-ONDcuL5LyaDjbnTi2MwKiRciQGeREzk7a7PVOE9z-jqRMIpi9ym9xJ6TBLeHhttpyfSGt4-I3JyJ4xszVvomFUfbnWBHsrIiERh6nU1lha-yl4mOWe7VPA7uBk0vg2HsbCaV8dBfXOR5N6NL-5-TCqPuvSCGXRkK98DqgBgQi395HCriAIlchOyFElhLI4Br5waYuxmYnDpntAGPHFDAhDz1D_5OFw8ldol_gN6oWKVGysC_SJBvfkM29wmjPHSimNv7iCsbEQXuPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBroyqmpXKe0W3YV_sXYO74QqBCyQj7afDs4LD_FsTvURDX6-J6FFEYEtp3YtrWma84-NO3dWyIc325VCat3W0xPfKojK9PC0Vda9b8hitChaEkgQWBQQHbEQQ1LBMfB0LU7mkkstcEJL-ET5aJC9cuksg8wX4i7W3pvYJoRXm3xZTUxPcajGNQnk3xyVULl3fS4E5vHnuG8YEvduzOta0Wafy400KELoNpkwt-o3DACfvwWKd4W3HkenUYd6cnZnnb9ItR1wjb0bslEGKzMKs9iRRrVJAu1WbzIpNs3Wc4j6Q_NKFqKTbCW0SOff0kAfhLRimpxOGbiA0piH21SoDV6sY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBroyqmpXKe0W3YV_sXYO74QqBCyQj7afDs4LD_FsTvURDX6-J6FFEYEtp3YtrWma84-NO3dWyIc325VCat3W0xPfKojK9PC0Vda9b8hitChaEkgQWBQQHbEQQ1LBMfB0LU7mkkstcEJL-ET5aJC9cuksg8wX4i7W3pvYJoRXm3xZTUxPcajGNQnk3xyVULl3fS4E5vHnuG8YEvduzOta0Wafy400KELoNpkwt-o3DACfvwWKd4W3HkenUYd6cnZnnb9ItR1wjb0bslEGKzMKs9iRRrVJAu1WbzIpNs3Wc4j6Q_NKFqKTbCW0SOff0kAfhLRimpxOGbiA0piH21SoDV6sY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=i9a1t_ghqHjNnL_q4VknLsC8-piN1xulkWC2OJWH7zkqX9cvhWdoJlA5URogjHTonHcpUoRev499McALowtlLOdfO1TPDHPG4Kacl1Bu9KuykdjhNDvuQ15f-j5O6MN1utb3kqORQstANTYA2hRTR7derz7O8eNxxW5tmsnodk-wazH4etPbLMRZBGvVuMZadhoV4aNmNTWALzR6rzmbJG3xQPtH99_0aDWncaxy2Q8LXXl3xWpBRI9qsyEyAxbbqyGgO3Ywam_dK9WK0Opvz1cn7fZwjlL7KGgZRWY4IBJhA8e_aJMgUdTLcrY-TNcib2hOi705K2m6V0Nv8C_85g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=i9a1t_ghqHjNnL_q4VknLsC8-piN1xulkWC2OJWH7zkqX9cvhWdoJlA5URogjHTonHcpUoRev499McALowtlLOdfO1TPDHPG4Kacl1Bu9KuykdjhNDvuQ15f-j5O6MN1utb3kqORQstANTYA2hRTR7derz7O8eNxxW5tmsnodk-wazH4etPbLMRZBGvVuMZadhoV4aNmNTWALzR6rzmbJG3xQPtH99_0aDWncaxy2Q8LXXl3xWpBRI9qsyEyAxbbqyGgO3Ywam_dK9WK0Opvz1cn7fZwjlL7KGgZRWY4IBJhA8e_aJMgUdTLcrY-TNcib2hOi705K2m6V0Nv8C_85g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZFY9wDnMfkEk8KfktGYBI_SXthJYI7FdSMyJlNDSnxBj1mdy6OfdP4yJNXH8loifyJl5-J8_ZODjC_xbyx4Aj3hmdT3Vi6u-ovRlLqI7oMkl9rl1U0CJK30KrWk-WJjNikWgsllN96jE39L8smlKONtNXZAcqczYnWC4EIAXEMZuhQ5FewcISQojiCtBiaOETwWR0Mit8MB8HL45ARts1IrF2RcDSEFhZabrXnCfKWd5LphfZ9gqmcTqar_zIN46gqRDmn14pSuZBCy4k2bWENua11gDA-BylXeWjGpG3jCtWIA7vjmzj8KgtJZZhmHdJmrzOKQWTPT413XUvmAnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=G2HzJmxMt4I7iTe05bf2fH6VWwzSVhMxjuu4VUvZ7hZnqnIKvqI-ZA0AhpDun7JAtc9xZQbRvm-UCp7OsJC5NkQ5QtRiy3Mniqbs_eWRVkLQ2YugJG_24TNG0XmlqUXJsHYk2Tj9cfNCScWKPMIJXoUe3kyaVipiQEPALuwGROnuBmpjIDuTgifUXlzpyFMOmCn4FqPFteGY4MlieuBEOnWUcBqsp9GaB52CifiWiZrs47IW5IqwLguIAnrl7uQwXcWhyHMhf7gwswvlDHmg4BjzE7AIwNbUSZb7IljL1IDboUpo0vriSZxca-vJlxbtNppddSYECVf2_K0qzBBhznfXvQBi7_jqHjaajP0R2VTTwFklty-0ro5PQPNR566-sD2wGO_bUC0YLMlMg4qdLHy_OVik13E_4Q1NlgjB04vMDWTZGj87_bWdR8jicV9sVz-CKxJ51EoRY4wLYCL0h05kOQLusshvH5qjxhqZ2jRNE5b-coYnyZbUJlj7q_A8tn8S6ps24nUQwup99_nSOH9O_sRcFsnBANOVHo02QtdQgHUX9ScREabnjUiPUil7tyE0OB4A04ShEbWcg_oVSWr77PLUzJpvYx0giDnU0RXFoQjaepSQtIL3k79aaThCVyFPaVaceVObbjw7ot8Vv7BaK33MZSInliz6vEruiVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=G2HzJmxMt4I7iTe05bf2fH6VWwzSVhMxjuu4VUvZ7hZnqnIKvqI-ZA0AhpDun7JAtc9xZQbRvm-UCp7OsJC5NkQ5QtRiy3Mniqbs_eWRVkLQ2YugJG_24TNG0XmlqUXJsHYk2Tj9cfNCScWKPMIJXoUe3kyaVipiQEPALuwGROnuBmpjIDuTgifUXlzpyFMOmCn4FqPFteGY4MlieuBEOnWUcBqsp9GaB52CifiWiZrs47IW5IqwLguIAnrl7uQwXcWhyHMhf7gwswvlDHmg4BjzE7AIwNbUSZb7IljL1IDboUpo0vriSZxca-vJlxbtNppddSYECVf2_K0qzBBhznfXvQBi7_jqHjaajP0R2VTTwFklty-0ro5PQPNR566-sD2wGO_bUC0YLMlMg4qdLHy_OVik13E_4Q1NlgjB04vMDWTZGj87_bWdR8jicV9sVz-CKxJ51EoRY4wLYCL0h05kOQLusshvH5qjxhqZ2jRNE5b-coYnyZbUJlj7q_A8tn8S6ps24nUQwup99_nSOH9O_sRcFsnBANOVHo02QtdQgHUX9ScREabnjUiPUil7tyE0OB4A04ShEbWcg_oVSWr77PLUzJpvYx0giDnU0RXFoQjaepSQtIL3k79aaThCVyFPaVaceVObbjw7ot8Vv7BaK33MZSInliz6vEruiVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEnU-gM6it8NsPh7AOIf_GobRxJAQs9bST7TtZCtAfMephD7ZSI_URMcZfzwB9dDabeb6nrC0CtGuCfSz6tQfnTaBCo84Jvdw2aBbOQZynU7sfdgqBAWsu78cAnjdTaWPLkZrlmHgy-cjEtVQOqdZt1gqTJMETmB9p7wVvhkJ8FTtPaSEKPD4vPnmvEOX-hdk12Cg46_PfVBnXKLdEREmKBiSx-ypreAZlAMVF5nhIp877x1u0ea4dXxuzGisM5ApbwqTO4MHnYPTynlYTqZJdf_2ClkHRnYiLSEqf--QW8gr3MOjPVuD05ObWViMOYuYK2kdlGA_gqghq2I8K2-HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=lOjHEFOr_Hq8aDV1obAlUZf6f9AATNV3_H4Sxi1wdi_ukgTSTm97TUF2_uYWpcgkh7RPeNRknyYmhVCUtSN5upHUjZAAWtq477RVF77DCYxVT1C63eIRLaqu_tAtv6Q-WdOv_78Egv-zieTdBLU20d6Z-jp_Q1TsiNqTVSw9lknBnG9uTjJDZI-Pi_w6inoRKPnlHavL4EeiJgYXXXRYWwCjFHmJOlhzxI3OiOMHDgEtlUPV6gquxvfMCZq459-i4MIy1kqsb-fLj3QnfW2srbnFCTMD_Ve5tDwTvJV7AYmdrflgd5zENXCHqVhI3afj02OZGXl7oTBv9mQlqP1PbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=lOjHEFOr_Hq8aDV1obAlUZf6f9AATNV3_H4Sxi1wdi_ukgTSTm97TUF2_uYWpcgkh7RPeNRknyYmhVCUtSN5upHUjZAAWtq477RVF77DCYxVT1C63eIRLaqu_tAtv6Q-WdOv_78Egv-zieTdBLU20d6Z-jp_Q1TsiNqTVSw9lknBnG9uTjJDZI-Pi_w6inoRKPnlHavL4EeiJgYXXXRYWwCjFHmJOlhzxI3OiOMHDgEtlUPV6gquxvfMCZq459-i4MIy1kqsb-fLj3QnfW2srbnFCTMD_Ve5tDwTvJV7AYmdrflgd5zENXCHqVhI3afj02OZGXl7oTBv9mQlqP1PbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swJkIL6voO0ueOyo32r7zf2T-5kdtNeRA_WeJ8uWHJZwZAgch3I-Z0Z3YnPHS3jE8b5xllLoYYE2Mc18eEQr1ntzDCLECe2rHvhBPINeQhXPYwfJEFOggarXwiiYrLBG2vHSgOsiG1dBDqDe7pXBlPlUCJPcc9OpHc2FsjtmbdNwRrvWT8Hy9XqnYZs1I8LJ1Ph2vx7XdTPiQcowvNORgP3FBbdSdp2tFTJJvifKNSuhmvT_jm-_rkdhqPSUgckQ_tOZlT137susaDxCKhWVmb2cgaxA78MTAVkuYtZSPk_yaxbvWnFYgTqFfv9ni7vdudS4DdsEPtUC2qwHEVnVnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIENtiHPAXD2i28m9T6Z0EFJNCZOwsOS6Gfqwal2EtVIr9jlSYvB4wConZnMrSqkqGclnkusaYmdK8RL1xJ1E07D0VFisgQZKggFMDWdbtkm6tNuSTkC3_34EHUobHaljO3nJLt7ZK8_UukIXWWvP1mRZcqoOpHCK4zyqlHXK7fTMaKD_Z_R1JbkEWPbBywmwK8AcTu8mEfp1kcXAmF8ODbV8MwhIqhqjzMZq8YF1WsCJrHI-M5Rzuue414X4m-BbO3AuJoKdgvZvT_Ad9XPA7_S7qhsoH11OB8lW6ZHhvIaOTvkbdlIu4RLMSBa0iViDmuq2M65Dh4HmuXVyCVdeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtcMH9NZzAbS7MvXVqqcH9UHsTQFoP4bjmrkz6SFWYb9WxRPA6to_8bBqXu5mClhzE4dbdbTNSXeIeKbuRlGRbuBdquXcmCfUjJkqD7p_5jCx9xs_0J_lti2viRG_y3O8J6w4I2e0DwOW0SucHCh-_h250VV1jn0TERD78yO7X7l4kaOWWRe23Q0YZodTBdT21qytGRFsFsqhBL7XlIcIHjkJ9NbgIk8rpfsZ_im5_Qjxn2LkHFneQA-bmJ0_6pGcWm0CjPU8RJHzJDpqWQPvAuyzWyWwFs8ByEc1lO-7xD2idS75uWfKIM7qpM70fjc-YiXa6fnyyIP8JfuYIEq2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=nyWU8tVvXsMYoc5yjQfRk5wg2t9IQ1SHVKHvqvhSod333GSVG9Un0rj9HYFxo6zoXrzwT8e_xCt0tyNhx7rEfI6bQwCznl7erAfPWpG80cc2DoLf5HRNuia2TJqCuxK99L9SbhEbC15CyRVTKjs8m1m326CGU_9o4UCHh74-4cUfPNV6zsQrSauWsBRtUxn4LsxL831tdNYr1oM4_y7pyCoth_WhKI9FAJFHEIcmyZtRIcfEzezmomOIyuBT1ckMv4hGuTj41ZvUNoFKqhVMkxG2p9zr0VjVHCSGHgcI6DwyexitDoLpFKOPCmeUQbQIMibkKMjtEh_ssThbsdtjhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=nyWU8tVvXsMYoc5yjQfRk5wg2t9IQ1SHVKHvqvhSod333GSVG9Un0rj9HYFxo6zoXrzwT8e_xCt0tyNhx7rEfI6bQwCznl7erAfPWpG80cc2DoLf5HRNuia2TJqCuxK99L9SbhEbC15CyRVTKjs8m1m326CGU_9o4UCHh74-4cUfPNV6zsQrSauWsBRtUxn4LsxL831tdNYr1oM4_y7pyCoth_WhKI9FAJFHEIcmyZtRIcfEzezmomOIyuBT1ckMv4hGuTj41ZvUNoFKqhVMkxG2p9zr0VjVHCSGHgcI6DwyexitDoLpFKOPCmeUQbQIMibkKMjtEh_ssThbsdtjhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_XmD3papI82w1NfEbv--UXd14aGHemWtGe8MMGgBZ6iiAZLE2_EEx9tTo59P8fl_VLZz_ILGZbTIMgBDF9Eh9Epp_zTliBEQcxRGPXYov_O9vIQ2cde6p8xo8eHM4CW1d5UYcwr08w3xuFIBWjPLJCYYkTwqw8M5YoIfsmIK-sMTcDzgNlRjbtmmBadHexyMwCdtDPhIl2wHXV13tclvrIpCIJgYqiNBV8NN2CLw5JbP8vgOzG8bU6QEFVUMPARNBIDqqUARf7DHMq0s7K9f1YY5K9_KYOfah5B_E8l5U1QXN8oyA9uPUmgjoiWTMq2JKzBBGFureGj1E17QkEJKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFHfYoUdjtIAl3PUjMQr9PFgHZ68ipz8nODbODJLHGzDzMGlBfu4B5uWXsGksqymo9DBGcbWsXbn_A-WE6zgg1FBxPlhMa0xzrD16sWhRECrEfq1Wi1ugOvLLBWmed3QPqs2Y9RDRDcHUAos1pFXZhJWAO5OSVRQsaR-VJ_14EiCq152wUPYdsm69UBqYrIHa0I2DDuxceriFhYJdNjqBsPchkJOzcUTQJs1k0hplHAVyG-4tdjMv-KuwP2LvISioyS92_Z_bisp6M8txJ4afe2VYEaTT42ALG2umPKoZKazcCjuWpcGIHallcccNo4r0bAoO5sUvMopINJ6HhM8IRZ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFHfYoUdjtIAl3PUjMQr9PFgHZ68ipz8nODbODJLHGzDzMGlBfu4B5uWXsGksqymo9DBGcbWsXbn_A-WE6zgg1FBxPlhMa0xzrD16sWhRECrEfq1Wi1ugOvLLBWmed3QPqs2Y9RDRDcHUAos1pFXZhJWAO5OSVRQsaR-VJ_14EiCq152wUPYdsm69UBqYrIHa0I2DDuxceriFhYJdNjqBsPchkJOzcUTQJs1k0hplHAVyG-4tdjMv-KuwP2LvISioyS92_Z_bisp6M8txJ4afe2VYEaTT42ALG2umPKoZKazcCjuWpcGIHallcccNo4r0bAoO5sUvMopINJ6HhM8IRZ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=mRMd1fOoSxazyWAu8TxJm65pb4I3nMA5jdeXx37Q_fUlME-SsXd3OM3mkc7sPsxTlJBkYeqkIWovISWuTZZskU_eihxbdinO2ynX5BSWkN1fS-uOKan33Yi9wJ_FvBtCxSccM5MJE-7bZAoZmNhKNulUjG4ikEburNnSkPTMXVZcInsmskPCQOhHEjuDO-xNfPypoSA39IemJ45aKH63OVooWTJJMUInSbM1Rp3oApmyNWG0hFP0JDPeV5amderYMW8Jop3jFLlLdbW_Q12bITb9Gb084IaQmbu6xAKos7JzG0loTWMu7QzdhvtqUIbBZkchTeHnu2F5_ApwcUyh_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=mRMd1fOoSxazyWAu8TxJm65pb4I3nMA5jdeXx37Q_fUlME-SsXd3OM3mkc7sPsxTlJBkYeqkIWovISWuTZZskU_eihxbdinO2ynX5BSWkN1fS-uOKan33Yi9wJ_FvBtCxSccM5MJE-7bZAoZmNhKNulUjG4ikEburNnSkPTMXVZcInsmskPCQOhHEjuDO-xNfPypoSA39IemJ45aKH63OVooWTJJMUInSbM1Rp3oApmyNWG0hFP0JDPeV5amderYMW8Jop3jFLlLdbW_Q12bITb9Gb084IaQmbu6xAKos7JzG0loTWMu7QzdhvtqUIbBZkchTeHnu2F5_ApwcUyh_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=FMi6LzsLAmPbE9fanMNl3615DVG56bzl4p_TMyxE0QXOT_6n9c4qj81xiM78SLKoz43xQ8tzgpkJiTC_nYC6LHDPHjiwcLTQ4ncmAZaEHnaLYTenq9IPn6QJLRIvltX9I5eDmgDInFLWkg-2VIv0iZeJalJf85eMj3hlzdhw1PMCaMo0fMn92atLus6eg_Ks6CXeiJAi89e-2CYoWKo6vaNdFxjV_W2uMK9QR7x_cUnSCDOFl1WZdoAfzUxOnxIE0aPTHji2E9013AZRqaj6UoQ-P6N-ydSIzmJzKMbmcrnX67e9xSPe5QGmV-FmzyTDwqOcCkQFrtMdbLxStMA9-gVng6j_VhwIfB1Azi2jse7FACliW81HM8wIq3e8sOqd6i0LMFQl3rqdFAi40O69eKHD2nA-qi5xB5-2itk9jpMh1z-Xd8MczGMWeSxB5JAT5r2B47g7PWEoLVzxOyh-xEVPsSJGA8OotXgcB1f7G1O8ESl2qUR6LjNNIpcY7yW1dG5-32yyBPgQEoNOV3KILXV0x76OeJTFiausj7z1KnIbzXnNeujzY44yalgIU6K_ZQCG9D4gnnLshDE9n9FRCNskLQHAIewaSxPh-r94mC6imhlALhkZIW0X1TaXVXcrN7JGlf0MKPxH9HgaWuIjy4RNgqUy_J6C3dqnCmr3Fak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=FMi6LzsLAmPbE9fanMNl3615DVG56bzl4p_TMyxE0QXOT_6n9c4qj81xiM78SLKoz43xQ8tzgpkJiTC_nYC6LHDPHjiwcLTQ4ncmAZaEHnaLYTenq9IPn6QJLRIvltX9I5eDmgDInFLWkg-2VIv0iZeJalJf85eMj3hlzdhw1PMCaMo0fMn92atLus6eg_Ks6CXeiJAi89e-2CYoWKo6vaNdFxjV_W2uMK9QR7x_cUnSCDOFl1WZdoAfzUxOnxIE0aPTHji2E9013AZRqaj6UoQ-P6N-ydSIzmJzKMbmcrnX67e9xSPe5QGmV-FmzyTDwqOcCkQFrtMdbLxStMA9-gVng6j_VhwIfB1Azi2jse7FACliW81HM8wIq3e8sOqd6i0LMFQl3rqdFAi40O69eKHD2nA-qi5xB5-2itk9jpMh1z-Xd8MczGMWeSxB5JAT5r2B47g7PWEoLVzxOyh-xEVPsSJGA8OotXgcB1f7G1O8ESl2qUR6LjNNIpcY7yW1dG5-32yyBPgQEoNOV3KILXV0x76OeJTFiausj7z1KnIbzXnNeujzY44yalgIU6K_ZQCG9D4gnnLshDE9n9FRCNskLQHAIewaSxPh-r94mC6imhlALhkZIW0X1TaXVXcrN7JGlf0MKPxH9HgaWuIjy4RNgqUy_J6C3dqnCmr3Fak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=nbnScNx5xXANBTeZlDeGM0T_5EGG9BT3GBiCwW03P_wxxqz2-bQLiB1MOXOZ5jgXsGLTZiV5QH5lxf_sPgW5tVYzIoPfzX-ivt2IkvMAOa1hmWQze5IJIih2yGGl_FH978TUo7-dfFvrmuAXPAhaS14OrJE6HzKaPhSNKuomOgf4Elrzy4HqGjMiyGtmL-ECT_4y7SUgYupK1aX22mivJcDwm2ibx3ZfWX2UCcmTKZqa52wunJtpm35-SIWvzBQzgY8tj0eVvPk_9_Bsi4XbluD5w3dsjPN-kep-oCskxzGNumW71IbBSErw4jFMj3T8Xugx2s7IHa0qZAbo7A_bPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=nbnScNx5xXANBTeZlDeGM0T_5EGG9BT3GBiCwW03P_wxxqz2-bQLiB1MOXOZ5jgXsGLTZiV5QH5lxf_sPgW5tVYzIoPfzX-ivt2IkvMAOa1hmWQze5IJIih2yGGl_FH978TUo7-dfFvrmuAXPAhaS14OrJE6HzKaPhSNKuomOgf4Elrzy4HqGjMiyGtmL-ECT_4y7SUgYupK1aX22mivJcDwm2ibx3ZfWX2UCcmTKZqa52wunJtpm35-SIWvzBQzgY8tj0eVvPk_9_Bsi4XbluD5w3dsjPN-kep-oCskxzGNumW71IbBSErw4jFMj3T8Xugx2s7IHa0qZAbo7A_bPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LowMGDng-eU9tnYkXEoMoE5rPNYu_L3CcGRcTXysTiRv0jl2U4DPAclXLisw6cmt5zWz6WeFoK-RAGKgU2A-ZdhyQM50gGmGpSmLkF3aM5wyhD9OO0w7mgHIRtGf9NYjsWQsRUt15Urx90LBLHGfieflC3zDfCjrIHqHxVw3xZ7GTXY6cAFg0w30txoA1PSweZokIIjhw-0e25rDv2hSFjYO75vB-Wjwk4u_WpXZVGYAFsXV0Uouvh8JmsL2CdMJi4j8gTUXTTHcc8qZvAYFsS0eLCNNrcAm1bvrke82DCnsVavN146oReW7iwuWLKY_U8rvg2HdyoOi74FBldwsRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=Q0i8k64TUH462OBIKmfbsCtFC0gy9vOCHvid7htGlB1qLeZTeIUIFc8RV-_hJjGLqKY1NMkFJ60fdBDdngfMZxJrm9wA6VZzoA2RNg0oXjRMVJXY6sUezMnVP1nYDzqnv_3CoCDCh360zREVedWbaS0MpoV34-iZkjayTarQ3wwNy_KP9pn9mSI-NPlz5EvzjP4UGdmc5BigJoJnnj0D8l-x8VcLGKDj2-RltpGXtvcNwOzLzNOKwx3Br7Bk35T2n-rO6VocTzh9zjOaRf4SM4UaxQHGhLThoV6chj1xroezjaIOxL4B9veNHgVr0CDWCGObEAy5KA-cv5VFJWcDww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=Q0i8k64TUH462OBIKmfbsCtFC0gy9vOCHvid7htGlB1qLeZTeIUIFc8RV-_hJjGLqKY1NMkFJ60fdBDdngfMZxJrm9wA6VZzoA2RNg0oXjRMVJXY6sUezMnVP1nYDzqnv_3CoCDCh360zREVedWbaS0MpoV34-iZkjayTarQ3wwNy_KP9pn9mSI-NPlz5EvzjP4UGdmc5BigJoJnnj0D8l-x8VcLGKDj2-RltpGXtvcNwOzLzNOKwx3Br7Bk35T2n-rO6VocTzh9zjOaRf4SM4UaxQHGhLThoV6chj1xroezjaIOxL4B9veNHgVr0CDWCGObEAy5KA-cv5VFJWcDww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=a4a4WTWDZJgExyqTPhDyZPegsMBoXh6BQvpdWy8E7Kg_SPNEAd8G7xMxIrDcwk7sWM7TRP7xggJYIEH26osvT1pYyetDXKy9F5PKS1pr8AQkE4zvxJLVIWtaZH_QFs0BOgRnTZwJ3FBCXTIQYTmQ-g8OW6rdodN6fTFST_BJi2OWp9X0UQidhzakGJZoQebLTzIX8rj5XMcW8YQXvS_-xbemttPRjxZBdPVAPHx63qvdwhzm9WJ8yCMaq1iiqCJJml-oDkA-2arunjvaFZ4Gx4HKVf_p5uns11pwQkIu3DwWMMPjdcmMTpaW7sUz5Hf0_SJCfojxdBNex41HorPPiHgn0UsviLNPCnAblB3HOCfv17Mu5ac9TY31zUlg64AKwQq-P0946X6xdPhi9gy38TlYb-1XGnjVgBKkAF_hyw5yLtDXXnTIivFobpvNtxjTsNnSdzPVlpp8BGGnkbpg-WQPP_kBsBeFGoP8bU98cmQlmR88Fqeu3jCnzHcKBelIQULoAdgW5ESSdYZWKU49jpIAF-IH4Wv0v23nZ_5dR97aWrrmVMEq2bNhOQmLHD9OYuRZUFoWQ5qC241EAesqh9SbEF0YmJfLmNYPNubFNdQKU5OIhKkutgDyTfwQPcfzyidRN3t6Oc_g0d_EZgDkQICd7SWU35AZFm8f4aHEzoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=a4a4WTWDZJgExyqTPhDyZPegsMBoXh6BQvpdWy8E7Kg_SPNEAd8G7xMxIrDcwk7sWM7TRP7xggJYIEH26osvT1pYyetDXKy9F5PKS1pr8AQkE4zvxJLVIWtaZH_QFs0BOgRnTZwJ3FBCXTIQYTmQ-g8OW6rdodN6fTFST_BJi2OWp9X0UQidhzakGJZoQebLTzIX8rj5XMcW8YQXvS_-xbemttPRjxZBdPVAPHx63qvdwhzm9WJ8yCMaq1iiqCJJml-oDkA-2arunjvaFZ4Gx4HKVf_p5uns11pwQkIu3DwWMMPjdcmMTpaW7sUz5Hf0_SJCfojxdBNex41HorPPiHgn0UsviLNPCnAblB3HOCfv17Mu5ac9TY31zUlg64AKwQq-P0946X6xdPhi9gy38TlYb-1XGnjVgBKkAF_hyw5yLtDXXnTIivFobpvNtxjTsNnSdzPVlpp8BGGnkbpg-WQPP_kBsBeFGoP8bU98cmQlmR88Fqeu3jCnzHcKBelIQULoAdgW5ESSdYZWKU49jpIAF-IH4Wv0v23nZ_5dR97aWrrmVMEq2bNhOQmLHD9OYuRZUFoWQ5qC241EAesqh9SbEF0YmJfLmNYPNubFNdQKU5OIhKkutgDyTfwQPcfzyidRN3t6Oc_g0d_EZgDkQICd7SWU35AZFm8f4aHEzoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXAVfkVLEs6nOeRoqa7hBQbo-33zOnqo3Iypv20zbbioTte7hccAd4ZQ9tEFcP6MfgLjh_01LYTkogf7e8MEuah33P9FSOMC99vuM0qGX_TfZg53_4RPsNhlrEiwl2AdtvyJb1OthSb-ddrJ42C_7Q-qex8bbw4067kgfgzXty0ijox59Pg80lP7m09WeTSbFs303gOrbsCxbGg40mcIDNPpxluKYU2rNL8kMhf5IaSMe4eNZfpMY6k-x8YHeCK118dwWECgXEvovNOxGtctv6oxJPh1FBKUbw2HmKmjQhjRbeOXMYEqCth9k-d1ge2sQ4g1dLDMF079SyI4rYMA3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=iO26lAu1Nz52EltCKfqv0j28t_xjMuBSCF-TxGa1D9havFmpJUPI-K6__XAGsmWVfE90fb1EqbW5Jkapd0NxOzLUbIlvIGPNznxd5HzCMPgjoc_ScdhEoqU6nbDD7mcB8PiMV-Dfi6f9cBcw-KkjyIk8GJ6BbsJwNCFKWafmMMat6m12qtLhVlqNMJ69mrnyvNxjRe_BIxj60k1Irz7DleMq9KfOOw4B-hg9NdwFNSl-sXatwdP91bqWW-1essbMWYXnEHnhY8ywl05dR2xZMch6OjRn2K2RQDubWMM5v6jS7r0R8bt2f2HzZysLhy-DY1qp76QweLRwAXwOJtbWxZ9JZ1pvswYjV7LEr3iAHH8BxFgQmwDfvqY8RbLFs4T98BFOyzW0dCS2f6nBHixp9ZzTwb76ZEllFn4elNBxwhrvrEvSJgYIIXC_QeVc7PWFBtQnEVjycZLtvLVAEZUD2F0lJ1FMB3yoPqadqbsID3BPji8Le06vhp0vCrrcGYMkoaxqxBZaGYzaQSvpIZBTEMlG3z1DoJXMqF-MPQIou71lELy0TlnKqIV8qU-fx3rzoXuNb7JatG8Fudz-IO-_R2rbQA2iNbuLiM4P0H8HAp4o6Q_8xSC_z-fWKN7pWfAwKuGDRzteP3RTMH6z2yglDU22gmt6ce9Yk8YGiEddZQU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=iO26lAu1Nz52EltCKfqv0j28t_xjMuBSCF-TxGa1D9havFmpJUPI-K6__XAGsmWVfE90fb1EqbW5Jkapd0NxOzLUbIlvIGPNznxd5HzCMPgjoc_ScdhEoqU6nbDD7mcB8PiMV-Dfi6f9cBcw-KkjyIk8GJ6BbsJwNCFKWafmMMat6m12qtLhVlqNMJ69mrnyvNxjRe_BIxj60k1Irz7DleMq9KfOOw4B-hg9NdwFNSl-sXatwdP91bqWW-1essbMWYXnEHnhY8ywl05dR2xZMch6OjRn2K2RQDubWMM5v6jS7r0R8bt2f2HzZysLhy-DY1qp76QweLRwAXwOJtbWxZ9JZ1pvswYjV7LEr3iAHH8BxFgQmwDfvqY8RbLFs4T98BFOyzW0dCS2f6nBHixp9ZzTwb76ZEllFn4elNBxwhrvrEvSJgYIIXC_QeVc7PWFBtQnEVjycZLtvLVAEZUD2F0lJ1FMB3yoPqadqbsID3BPji8Le06vhp0vCrrcGYMkoaxqxBZaGYzaQSvpIZBTEMlG3z1DoJXMqF-MPQIou71lELy0TlnKqIV8qU-fx3rzoXuNb7JatG8Fudz-IO-_R2rbQA2iNbuLiM4P0H8HAp4o6Q_8xSC_z-fWKN7pWfAwKuGDRzteP3RTMH6z2yglDU22gmt6ce9Yk8YGiEddZQU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=Gcje3D_Ynyl-dY1xb25kfV4oQc01HKr65fhpgMpJS_jsstixptK9MkQppqLJTRPHafEkBH17dGHL1TVM1mRMkV_AfL8HAs-uZlt6DH3HKdRdBLgqONU6CV53P_oxcscIrhJTgu8CAzgA81hwHRtv7PBGkQteMnDy3BLMbFg_6bx5dfHh271733AjF8ahiGVjq43-1vdXEwgnLYzGNjK0Aur4H-dZ5A46wMu9GlfjViELD2dNLgYWGv4qBfxbiZ3k_Mi4op2akppjtXSctc-gcXdBXxppZbOpuxAdcsNowza5Dqp-hTPCO10WbWzWa8xUQdT57gPrYtLd_uKNyEF1IGq_k_wRDlNuyyUQF3UAqGO56W9qCYUv-cD7OF_rjM_ue8FeEm2CvTh_GCv-tLabJNc_Rcv0FC673Zp5irPfIPw3G1ewGWXVFjm0xuPoJ3dldfWa4Ke5jZuU3kl7R92F76eJIy4bOrHp0B8TXcvcWS2qf1G9kJFhCrsV0ifX2CS7LZvN-HVTNloEUXr9BlzHdKesNqtYHJYrUXR-6TKhmipHXZBmOCyNrHzZUiABdSt9at-wbUBreHRPncDw_lRo48uOTCbRh4L_WJl9ZO4Wxv0a7qQQizZAQwVL3zxO27ulqIFmKCqlyn3m0aeGjMbNOF0U6Zsz3gHY6US9xF1nGI0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=Gcje3D_Ynyl-dY1xb25kfV4oQc01HKr65fhpgMpJS_jsstixptK9MkQppqLJTRPHafEkBH17dGHL1TVM1mRMkV_AfL8HAs-uZlt6DH3HKdRdBLgqONU6CV53P_oxcscIrhJTgu8CAzgA81hwHRtv7PBGkQteMnDy3BLMbFg_6bx5dfHh271733AjF8ahiGVjq43-1vdXEwgnLYzGNjK0Aur4H-dZ5A46wMu9GlfjViELD2dNLgYWGv4qBfxbiZ3k_Mi4op2akppjtXSctc-gcXdBXxppZbOpuxAdcsNowza5Dqp-hTPCO10WbWzWa8xUQdT57gPrYtLd_uKNyEF1IGq_k_wRDlNuyyUQF3UAqGO56W9qCYUv-cD7OF_rjM_ue8FeEm2CvTh_GCv-tLabJNc_Rcv0FC673Zp5irPfIPw3G1ewGWXVFjm0xuPoJ3dldfWa4Ke5jZuU3kl7R92F76eJIy4bOrHp0B8TXcvcWS2qf1G9kJFhCrsV0ifX2CS7LZvN-HVTNloEUXr9BlzHdKesNqtYHJYrUXR-6TKhmipHXZBmOCyNrHzZUiABdSt9at-wbUBreHRPncDw_lRo48uOTCbRh4L_WJl9ZO4Wxv0a7qQQizZAQwVL3zxO27ulqIFmKCqlyn3m0aeGjMbNOF0U6Zsz3gHY6US9xF1nGI0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=PG8jyIyEP0H96t6fc2Mw512QPqxYdnZ2d3Lipu6xl1qNDEfAsTS9mObEq2IB_wICMU48y2pFXInAupdVDB6nAg0_nrIuaeC0rAlgemrO75TgHk3D_epNNKA-Yd4YBBTls3XQliX2MUvX_q0zy5SpyK3pcmhWUeHUPNO4tzhxPCWY54KwrhsOQUwXLIPRdPUwIKNRaiouvwkDiJymExz2ol64zkRscTwFNziEGF1M1Hm27Tg1SERM25SY6yJHOmv8kh1PyftoRac4Yddu9_Qo1XdKorpMZKLJmJOdiSm2LJH1tAYSD3G0O1wbaaUjmTId60Xy8ZHBCm97BjXlwQlIpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=PG8jyIyEP0H96t6fc2Mw512QPqxYdnZ2d3Lipu6xl1qNDEfAsTS9mObEq2IB_wICMU48y2pFXInAupdVDB6nAg0_nrIuaeC0rAlgemrO75TgHk3D_epNNKA-Yd4YBBTls3XQliX2MUvX_q0zy5SpyK3pcmhWUeHUPNO4tzhxPCWY54KwrhsOQUwXLIPRdPUwIKNRaiouvwkDiJymExz2ol64zkRscTwFNziEGF1M1Hm27Tg1SERM25SY6yJHOmv8kh1PyftoRac4Yddu9_Qo1XdKorpMZKLJmJOdiSm2LJH1tAYSD3G0O1wbaaUjmTId60Xy8ZHBCm97BjXlwQlIpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=RpSEcqyJHBn-6czGLU-U8cSLQ6ZCyFfVhTi90e6wkwj63lBD-X83ZcZXgnSHiILJjRu8-exp1NVJZHf8IZovQmZeNXclaP1-NUMeERzNbIy9Vi2-UnIY3CnvoJ2YVRWQWz_Wyy2qvtZqorBbiDn2DQV5739AzuiboassdUHDgNhf-qvYyz9VmA4h3KJP2MHu6bp6d48Vxhzasig4G0Z1XQvROCi2skB-krDrPZHCixGAMRZACDaFC4KxcySGZC2Gud84Vgo9qHvNQViyItq1_Id5CzEHqYfGHWsdvMQpSalMS7t1Tsw5wURNGOiPvuWGkFj0BIsAUNEvQCQa8JT6yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=RpSEcqyJHBn-6czGLU-U8cSLQ6ZCyFfVhTi90e6wkwj63lBD-X83ZcZXgnSHiILJjRu8-exp1NVJZHf8IZovQmZeNXclaP1-NUMeERzNbIy9Vi2-UnIY3CnvoJ2YVRWQWz_Wyy2qvtZqorBbiDn2DQV5739AzuiboassdUHDgNhf-qvYyz9VmA4h3KJP2MHu6bp6d48Vxhzasig4G0Z1XQvROCi2skB-krDrPZHCixGAMRZACDaFC4KxcySGZC2Gud84Vgo9qHvNQViyItq1_Id5CzEHqYfGHWsdvMQpSalMS7t1Tsw5wURNGOiPvuWGkFj0BIsAUNEvQCQa8JT6yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=q8_fH7-2KOG-0oLv7Cm1ZwdRBXMsmprpinI-O-SQmL1eJhFKpJO28jEOW-xxwvZhbgp7gD_ioQC-8Xy_HUr7x_KtVh4WX7zRfOuyjC37wdUPBIuj5oNECZAPdAcTqeJddD_RvHZru9m2YB8tgLeuLKAOzV7hzY8SWfQhUYKLsCkeXVdxGKF25PRKXVcrJRNrV_b0BH58Bxs8DgTmnIw6PhC3FqaT_7xtlFB9diqRlMRsi4B0o8GAA6zwhtcwAxvyFfzAVdmlBpKRczUafa-9ypGXNB78KIEClIo0Q9GoS12r1IWKmLHKnW7VnRTU_7UhrP_hzRkJwk38Wcgo8rB4iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=q8_fH7-2KOG-0oLv7Cm1ZwdRBXMsmprpinI-O-SQmL1eJhFKpJO28jEOW-xxwvZhbgp7gD_ioQC-8Xy_HUr7x_KtVh4WX7zRfOuyjC37wdUPBIuj5oNECZAPdAcTqeJddD_RvHZru9m2YB8tgLeuLKAOzV7hzY8SWfQhUYKLsCkeXVdxGKF25PRKXVcrJRNrV_b0BH58Bxs8DgTmnIw6PhC3FqaT_7xtlFB9diqRlMRsi4B0o8GAA6zwhtcwAxvyFfzAVdmlBpKRczUafa-9ypGXNB78KIEClIo0Q9GoS12r1IWKmLHKnW7VnRTU_7UhrP_hzRkJwk38Wcgo8rB4iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=EG_ZEbEBbtUiy3OvgW4v700xKnyxrMlFrKqDpQvKA5EcC6mCTmVAr_3nj6A4dbiicIxdFPcO_hyVe58tTL3xLPbUl6ZSaaga3zhg99Wor3l5W_frXoXuMbMkwp-JwRLlxVr8nwbw9mxX7hifWVCCabp2tbYOF_uwNhdRgm0AYw8T1cYxDt97dd-BoKoIWCtXazNor_FQzX1Yz3fvzDxhL_Va46jsOb0LSylH2Al1QiLXWJ4ZXZ1c1MCoIbDgG7ovILs82PE0IVUGkhTx3cb894rpfRWEOq-_MpoXY__S6ujvhTkddIT07vXXof7Pi0scHlZyeGLMzTU3ewIZw8xSig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=EG_ZEbEBbtUiy3OvgW4v700xKnyxrMlFrKqDpQvKA5EcC6mCTmVAr_3nj6A4dbiicIxdFPcO_hyVe58tTL3xLPbUl6ZSaaga3zhg99Wor3l5W_frXoXuMbMkwp-JwRLlxVr8nwbw9mxX7hifWVCCabp2tbYOF_uwNhdRgm0AYw8T1cYxDt97dd-BoKoIWCtXazNor_FQzX1Yz3fvzDxhL_Va46jsOb0LSylH2Al1QiLXWJ4ZXZ1c1MCoIbDgG7ovILs82PE0IVUGkhTx3cb894rpfRWEOq-_MpoXY__S6ujvhTkddIT07vXXof7Pi0scHlZyeGLMzTU3ewIZw8xSig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=K68LeSxz1Z5-uG0CScArBCFRMKynA6EHl-LpgHaTmh_sYc2NYaQS1o-V6MCOc04y0dMZSjouX92JxmVEygHNKYeW016eSJxpudTrxMrz6817lvv-GZU-MRO_omyN7sSkp7Oh_d-o3RK8jTOulNa9jmWPvBPij6f5KGBV8pgYFaFXaFSWxgz0PPDkZwZ46xujp6zftBbjqRnfgFQH2ZKspMixSTatvN6W9EHqCIHv0E8U5TKo6oajW1Ptl_4Fc50TsGdIscvIFIYwKJ8ZNkeCLvSpuE2rxwUKgJNavsTYwuS0MbtBcoZzrAwF33q_1nM0ja-MUVU2xbpD4I0gHmNyAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=K68LeSxz1Z5-uG0CScArBCFRMKynA6EHl-LpgHaTmh_sYc2NYaQS1o-V6MCOc04y0dMZSjouX92JxmVEygHNKYeW016eSJxpudTrxMrz6817lvv-GZU-MRO_omyN7sSkp7Oh_d-o3RK8jTOulNa9jmWPvBPij6f5KGBV8pgYFaFXaFSWxgz0PPDkZwZ46xujp6zftBbjqRnfgFQH2ZKspMixSTatvN6W9EHqCIHv0E8U5TKo6oajW1Ptl_4Fc50TsGdIscvIFIYwKJ8ZNkeCLvSpuE2rxwUKgJNavsTYwuS0MbtBcoZzrAwF33q_1nM0ja-MUVU2xbpD4I0gHmNyAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=gMsVK20tReZ_dtFhFvQqUCqddMnlk20T4xto5EVgwk0vjwSWFD0fkU1at7XCyEazsS08o1mdeKkI2XXDDP1cE4IDWsNJaE4ihw4X10Ldzzp868OtFixYDoRTFbDW_b6zVQGtwBgg2a_g9F4h-zXPJTWiTvwNXV8ow5fC9GxLbYJ_j8RchOtZc2ukHyJXj3XY2BbpZmN3jP4LijlM1hS00mgTzynwVAf_IVe4AIHiJ_aoIotSP0xlm_I1AKEuCgJuNkbr4zCj6WfDo0LOHguSJaBQbJeAQ649PiZ2bgL2na5By0E8xOXwVIRhTh-hWj9MCnWdMzAMgOaqpMZuUURxAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=gMsVK20tReZ_dtFhFvQqUCqddMnlk20T4xto5EVgwk0vjwSWFD0fkU1at7XCyEazsS08o1mdeKkI2XXDDP1cE4IDWsNJaE4ihw4X10Ldzzp868OtFixYDoRTFbDW_b6zVQGtwBgg2a_g9F4h-zXPJTWiTvwNXV8ow5fC9GxLbYJ_j8RchOtZc2ukHyJXj3XY2BbpZmN3jP4LijlM1hS00mgTzynwVAf_IVe4AIHiJ_aoIotSP0xlm_I1AKEuCgJuNkbr4zCj6WfDo0LOHguSJaBQbJeAQ649PiZ2bgL2na5By0E8xOXwVIRhTh-hWj9MCnWdMzAMgOaqpMZuUURxAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=j4MTdKYdGnj4tOoRsr-ErI5C6dcLxLyTQw46__JjOOF2VvUMTAtRACrKqtneifqId1a14BfTp7HERNywq0TzgBcSZC5k47xL5in-0-wE_Y9VvQNeb0j-nqgvZ7Wby0mMFSRyBOUqn8fGxSg47FYJsSiNFASnDrP-CGpBccjxTkUk3Faesvz4gEQqyxZBsTPhG9Nb9J7v6pEhhHMuqGKxZt5nIGuMd_pfue8e_gfx-qv0sDnGyu0QOmQvFOf84sRQgopT5Jj0QCn2osNoIhQahnywjkXaROC7md32KkelA8Vvg_b1gcPSP5RYei7DL9YBdb547b8XAJ-wyYgFKzBWHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=j4MTdKYdGnj4tOoRsr-ErI5C6dcLxLyTQw46__JjOOF2VvUMTAtRACrKqtneifqId1a14BfTp7HERNywq0TzgBcSZC5k47xL5in-0-wE_Y9VvQNeb0j-nqgvZ7Wby0mMFSRyBOUqn8fGxSg47FYJsSiNFASnDrP-CGpBccjxTkUk3Faesvz4gEQqyxZBsTPhG9Nb9J7v6pEhhHMuqGKxZt5nIGuMd_pfue8e_gfx-qv0sDnGyu0QOmQvFOf84sRQgopT5Jj0QCn2osNoIhQahnywjkXaROC7md32KkelA8Vvg_b1gcPSP5RYei7DL9YBdb547b8XAJ-wyYgFKzBWHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOjg26AFuXcCns94jOPISM3mfejrzVMwxT4aGEdBgt0S8DmQSlGx5Yf5kSUx-E5rV7LehKDZVuvQzo9E5_DswBHroJYaSe87KZplrMKMypwGDZEMIvVQiTMMr0uU75LZgF2UY-8jK7Vfmah07vmWQ_MC0X-fxiceVsR0nd5zfVbeHeoGfypy8Hlaf6Bwh4fOSG9QfYdGOzxL7PIEHMsZw3nlMV2G854I5NB0MTm6mhhp2FuJP4bjYO4tkl0pujwTedUJvsiKaRfoiXIC7uvVPxIQORilfxIXVeEq9a8WWVYCW7umhBdLQzhRfslIWBdfVu89f-Hjhr-dCEAI93RTfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Cz7oxI9T9FB-AfrGtn5UjonkhSet-pDTjFoQ3rVV7uCR3zNvGfNXWaz8ggB0qdVjLpbuDFuSPcUuKdA36cV7AhXOxjxDnJxGIbCqJPf_ZHIyYflhairYNkNNz5wDF03MG9K_9R2jKuBWHHKdWXOYUsyWjJ8wOUZtGC7K9Z_ak7wqx1b1eTVJ7-a8X1RgUije9lSZFZudwZ4RXPV7dypFOT9fbJUeGZ19EpP-ChSVLLhST6qDIPMYDGsEht3-Qxi4U0YdYP19uJ4Diu9BtzPmvSdZRthCp_aeKSzdjqRmfA2nZfKSF-zXgeiHK1GGk-HuMfgv83orN7oi-vs_4AY__w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Cz7oxI9T9FB-AfrGtn5UjonkhSet-pDTjFoQ3rVV7uCR3zNvGfNXWaz8ggB0qdVjLpbuDFuSPcUuKdA36cV7AhXOxjxDnJxGIbCqJPf_ZHIyYflhairYNkNNz5wDF03MG9K_9R2jKuBWHHKdWXOYUsyWjJ8wOUZtGC7K9Z_ak7wqx1b1eTVJ7-a8X1RgUije9lSZFZudwZ4RXPV7dypFOT9fbJUeGZ19EpP-ChSVLLhST6qDIPMYDGsEht3-Qxi4U0YdYP19uJ4Diu9BtzPmvSdZRthCp_aeKSzdjqRmfA2nZfKSF-zXgeiHK1GGk-HuMfgv83orN7oi-vs_4AY__w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=K_AMYSVN_Rs3cYGl8W6-gYO4jpavcWZZ60ucapOB_bHHuzxNQ_rwcQ3-iYdjPFI-8g4zOAsYdIHTajgxmdBckNC1kkyFx8AEoUgujg4ewtgblRKJ0t8tGukelQ6WS0QTD2YXtajqY3ooxL6qaKeWuvKAWlLt9KzPXOUld6dY4BJw5ZT0bfhLBJfHmVbVF7D9gvohzQTVqqcmuREXCJsvKDp72xDVZuP6MpJj78WXH6jQMi0ixDDd8w_eavJDtUl-mgdSjLf2TM0cSbcsdCPnA9dF8J-xqPrTaLjiNbx1tAhp-_TUoTonptXURnhe9ZqLP5s_pwm1HjjaV2OyqO0qFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=K_AMYSVN_Rs3cYGl8W6-gYO4jpavcWZZ60ucapOB_bHHuzxNQ_rwcQ3-iYdjPFI-8g4zOAsYdIHTajgxmdBckNC1kkyFx8AEoUgujg4ewtgblRKJ0t8tGukelQ6WS0QTD2YXtajqY3ooxL6qaKeWuvKAWlLt9KzPXOUld6dY4BJw5ZT0bfhLBJfHmVbVF7D9gvohzQTVqqcmuREXCJsvKDp72xDVZuP6MpJj78WXH6jQMi0ixDDd8w_eavJDtUl-mgdSjLf2TM0cSbcsdCPnA9dF8J-xqPrTaLjiNbx1tAhp-_TUoTonptXURnhe9ZqLP5s_pwm1HjjaV2OyqO0qFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=HTwj52pfbTQkCtNNQ_r8_BxsA1p_zADUKz6XZ7c-t8nV8cUqngFaz_wVOn75C-l6uYDojzSM5vdcFowVaAECJw5qKxYPmK9JVv0F_RVe0UXW9peaGg9VaUIKv4fgBJwA97KoSzEC1jrMkeKfzWLk1rAJo3mRWoqfPrkkN0WlmcFyFmFFfqG4q6JK6UsEWp-l74n29Zpv5vHccAzFN8-4Bjlv3zRsMghmGNblLmTD_jmYGMGK5KUtj_x7I8aKZVCDScyQTPtxrpWKxqD6dNPEJ52Q6iVv2TzD4sibZiJEsOzKW6wtfh-oiOQpFvOwOsh9lMtRWNOk491ltYlaClnnyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=HTwj52pfbTQkCtNNQ_r8_BxsA1p_zADUKz6XZ7c-t8nV8cUqngFaz_wVOn75C-l6uYDojzSM5vdcFowVaAECJw5qKxYPmK9JVv0F_RVe0UXW9peaGg9VaUIKv4fgBJwA97KoSzEC1jrMkeKfzWLk1rAJo3mRWoqfPrkkN0WlmcFyFmFFfqG4q6JK6UsEWp-l74n29Zpv5vHccAzFN8-4Bjlv3zRsMghmGNblLmTD_jmYGMGK5KUtj_x7I8aKZVCDScyQTPtxrpWKxqD6dNPEJ52Q6iVv2TzD4sibZiJEsOzKW6wtfh-oiOQpFvOwOsh9lMtRWNOk491ltYlaClnnyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=kv2Gz04UmWgfr94rEhNF4rOt_WQhiZB3hWmdcxltAP5Mnl40M-4tg4d-EAOKZOh_Y_Fr4ByGiSZVVg-4TvLDbHJbdBACBMuEFf2giPPlk1loiRJFP1ynI1x_abEQUDoJM63kza8PikQXs18xnAgxMDFAYkPnYAB-c8Ak28f5jnveI_N4FulQq4ddlKWMKllcTzHZHPfYH4AFVqFXwuphcs_I4b3NoRufGNzwSLf6ZZFTvPrf-kYHGOUDGGcQSqFl_FgBHnSQi_nGz1Cfkz8Rxm9ETbA8805dkUeTI9o4uxQt9mNnM6QSpFbzNjlA-16B7Iu73U-UUUw-Wh2SakzAGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=kv2Gz04UmWgfr94rEhNF4rOt_WQhiZB3hWmdcxltAP5Mnl40M-4tg4d-EAOKZOh_Y_Fr4ByGiSZVVg-4TvLDbHJbdBACBMuEFf2giPPlk1loiRJFP1ynI1x_abEQUDoJM63kza8PikQXs18xnAgxMDFAYkPnYAB-c8Ak28f5jnveI_N4FulQq4ddlKWMKllcTzHZHPfYH4AFVqFXwuphcs_I4b3NoRufGNzwSLf6ZZFTvPrf-kYHGOUDGGcQSqFl_FgBHnSQi_nGz1Cfkz8Rxm9ETbA8805dkUeTI9o4uxQt9mNnM6QSpFbzNjlA-16B7Iu73U-UUUw-Wh2SakzAGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQX6fNsC-nAbXda0xjtGOvdA88UPcfx-tguiBNmTjnwwBaQLCWz5L_TK2zSwpEy9g1zPlvtIME8ehno5mFAQlGlrR3vC67fsLGM6st8kAmojbE9T-J-LsSmiR2ZU27jow5FM8WS-rCPlJNy_wcN_EsqzfJqNAu6BRTvabt9bbYkgF6FQTfg6B4altKKEofOIGqBUibQxBbsc9TjhXwGugcsvW8ioXaXpw7ak7g6w3PaWLjdKUYKLKjWrv1x3KicltSuR3yWHu5aow5rOd50mUUmB_k0wR5LFrEvumUGsjxQldDGlFz35h_OZYt5cpDcWwOhn5cySJGIjXDsg9MeAQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=c0DHC3hfa7MpUu81CQGnk2COR74qrbn_LPVfbO1qcWVu2ig0aFoyisDUokzF5DHWWg3yK_4Wn1B1FH3q2vdH2BMcprAM_LBaRTyugfF9893rwqdxaDrtRcaveBXwCAexbwM9YJrnYyLOtOXRpqNznnJVwg-GBOsZuo4JTC1rVNvlIxq1trVTgdNuTX3bSpFumbiXLJ20feDCSh0lf6E_XEJa5pEjYxhrknUrablDOiaBuyr6thbAxrLh6x16Py4Ae3gQjFbNETnJ1Wy2MUJA8VDgrf_ft-XmOPfxVTwxzMfv5q71XPdcc1pyo1r5Ihq384qfd7GSi48GVxh-FlYN3jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=c0DHC3hfa7MpUu81CQGnk2COR74qrbn_LPVfbO1qcWVu2ig0aFoyisDUokzF5DHWWg3yK_4Wn1B1FH3q2vdH2BMcprAM_LBaRTyugfF9893rwqdxaDrtRcaveBXwCAexbwM9YJrnYyLOtOXRpqNznnJVwg-GBOsZuo4JTC1rVNvlIxq1trVTgdNuTX3bSpFumbiXLJ20feDCSh0lf6E_XEJa5pEjYxhrknUrablDOiaBuyr6thbAxrLh6x16Py4Ae3gQjFbNETnJ1Wy2MUJA8VDgrf_ft-XmOPfxVTwxzMfv5q71XPdcc1pyo1r5Ihq384qfd7GSi48GVxh-FlYN3jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=drxteBsVP_AWZ7pE7P2OpW-b4MsHMRy5g1fbLYCDJXKjVIQFS_rcmfWLNkNFksrcz7WOCqhBv83z21uNZIiMRql2hYULE21pZvbwjv5qk2wZQF6E1l5ZKScsTTIvmIsUgKO0yFLTz1sO0QyJQ-eGnK4pLpved0xj1vQCuhaqtzAIoMct_UFRlhflebCIuhdWk7rWmVTB-cAb0LLo4kX-hLTeynVB28cFRfPTy4xVHAv2-VaZw_SYbjYIoEsESQcQKwkzC64AEPp1l0g94QPXNAHzAGfSKPxgxyBUQzDcbhzj6tP3Bk1LVU04YMclujq5eqJn4mw47rZLrv-c2e_2zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=drxteBsVP_AWZ7pE7P2OpW-b4MsHMRy5g1fbLYCDJXKjVIQFS_rcmfWLNkNFksrcz7WOCqhBv83z21uNZIiMRql2hYULE21pZvbwjv5qk2wZQF6E1l5ZKScsTTIvmIsUgKO0yFLTz1sO0QyJQ-eGnK4pLpved0xj1vQCuhaqtzAIoMct_UFRlhflebCIuhdWk7rWmVTB-cAb0LLo4kX-hLTeynVB28cFRfPTy4xVHAv2-VaZw_SYbjYIoEsESQcQKwkzC64AEPp1l0g94QPXNAHzAGfSKPxgxyBUQzDcbhzj6tP3Bk1LVU04YMclujq5eqJn4mw47rZLrv-c2e_2zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/azW9MsRrT3DpTQq1sOxvaUSnCXHXemUn2OnzhTlPEVvKqeo8V7i5umxUyQDWUXQWq5LRn6hHw_l-FaEJWWDSBQit_mdaLhzw32DexE6SiE2o4hACiB71YAkF3RcRMbye4hP7Gs4Z9tQtlvMqGjhGrGyPeLSrWnwTWfoOfeEi9gUukLILtPethm-CooLu8fUJCGUdeqnEZO4SebMf3cCx0NAUWf76u4MD-bt57h_-EM_pn9En3u2Bi-LUGiLEWCZDdZpRv6b1WpoqUsar1IVHeAdvFz0r41_s3OwrOsOpr_ZvXzNsvLLjalIVHCHdNCpvURVRdaJK1BYGbQi4R-C4hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VHvz28UyaeQSseX9zYNGrl1fXv0JD31QA37RHwEyZ0mfobIcMABnV-MMFmwmhja3pWJQnSkz_hy8ElmUnv5HDpUzklSHaXBLXpcTb3gcuYu6XbeXRJe36F3zHO2Qiszjt9rsMfOk1a3ShJfsD5BP87O1q4yGOG8Smh_1suxRdJrjlmygLx_OGo37bWiA-0M_c-lKG6HgQWHGMFDcK3m1JLo7hLbWy25qFXwerE8pGOeHLE-HM0_bJZ5JKSooSs_FmslYnnP0mwcn_41Cw9Rd5sqm75ewLQ9Big1ZY6vsc9tzgOER4ZdIsg2kvb-MCfVHu1DvxwqUMRVrl5HrzVxvHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Ub4PoADvQdutFb37wsGhi656e7hLs4AQp38cMmLxS8yfjnDi8sV1V0Ayuu0tz-gyTssG9aaWcy5DhOr6rmR49XGBVxVfs7Nqw1CA_dmqZvEjDfpURPkXK5IYyhc1JnTKRzxPsz_s_KXaapIZdNqr6ToSVOKh5RSU-L1sjeUrudrykKd5TqcPFVT2hQOIdirxT2AlONpTYuXSZnaiGjjapANQ1AXfmFpvcvnWcbS1KPyL_ZImM5GmwHcbUKlD_7tSDSyStOT-UnEBlCtQOlNCQhgCMY-dzhgAepQYzmoWE_ZLwgeDZlOHQv8Bq_8qFk8mv2bOGw2KCMP9elztSEuykw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Ub4PoADvQdutFb37wsGhi656e7hLs4AQp38cMmLxS8yfjnDi8sV1V0Ayuu0tz-gyTssG9aaWcy5DhOr6rmR49XGBVxVfs7Nqw1CA_dmqZvEjDfpURPkXK5IYyhc1JnTKRzxPsz_s_KXaapIZdNqr6ToSVOKh5RSU-L1sjeUrudrykKd5TqcPFVT2hQOIdirxT2AlONpTYuXSZnaiGjjapANQ1AXfmFpvcvnWcbS1KPyL_ZImM5GmwHcbUKlD_7tSDSyStOT-UnEBlCtQOlNCQhgCMY-dzhgAepQYzmoWE_ZLwgeDZlOHQv8Bq_8qFk8mv2bOGw2KCMP9elztSEuykw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVOzpEqPlxdoWaJGOLMO9kHbFOw6JosPSP-EpgLCyQjsL2K1efIePeBom8B8z5bmBx4fTr3J9SdRksoy_7SX6oNp7rSgtZBvbchV6fp8g4apUL1CEw4NPJMzniaac2StTpv7CJaaPPwo6CjORzD5ts4UujVvyxEIPGxAP3mfC8stf449kXiZCIWdkvrXbo7_VIWEloTyJLnDbozH2loGujo_XGV83iYwD8E9C_9YpzebECL2izLXj-sHIbM6mLu7XJ4XF_RpSLiY_IgrCncqhHHFvqNRG17YjmAElqgTz_pJAFDteP6lMIqlHvSAjvrRmhhluKa3rbmdEMO5BTAptg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
