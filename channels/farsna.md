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
<img src="https://cdn4.telesco.pe/file/QDr5NkpDVMaxV0aCFNqd7KzpH4L5mCDxMY8-AhORPkov8-m7PtMVgkWuac0lFoY3GiHFV0UdPO9ZzGkfagExYjMuMSE520wyt5HOGP6aiSHSKNhVayfyroqFxYDPq_JTBtJaVDvccVmiXdOjWfmF5RrXY-0sJVsPcZlPXXsUysWmhxODcbh5qhzbYNv-ITWanoa_BkShLOX70KMqnXZXWMzbuLF1CBG2ev1g8OoEVrJRt7Gm9no3XVR2P4BD4tp9bgBDK6bqBJqOMNi9uGJOBBC6ufEMXfIyHm-_kx10ksAst8AGnVYKGzWDfe9q1LIQPT73yw_7CJ_JUAEmHSRjxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 02:35:17</div>
<hr>

<div class="tg-post" id="msg-437330">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/277fad787f.mp4?token=jYYkm92w9_MHewhpXsb_RXlAPaI5ClqFBaFFFHZezNaa-LBzBR_5i--egX_gRC4mAZeCc-NIe8NTX7C9W9BpsU-zTbTj1dqnCfGf7a36pqcsdIlDjdcGIPQio4Et2HyRrs5yF1hCAVX6sdN9GZAfnt6oJ4T0zDEEGB9_miUb8sPf7WC2uQE9gqnafZU5QdxNyNNOTsqbkepG9JBhAhm1pE1TaHGFrbgk27wJQt2-xka70cgA-QiAcxoSfXoa_IcJlqjLS3nIPPtvg2XUNgOIgFiDFaykCmUjRyp0p7s24xff4308rsDpsKD0aaMAQkOaFD9I_GykhCTaBnBxVeVHxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/277fad787f.mp4?token=jYYkm92w9_MHewhpXsb_RXlAPaI5ClqFBaFFFHZezNaa-LBzBR_5i--egX_gRC4mAZeCc-NIe8NTX7C9W9BpsU-zTbTj1dqnCfGf7a36pqcsdIlDjdcGIPQio4Et2HyRrs5yF1hCAVX6sdN9GZAfnt6oJ4T0zDEEGB9_miUb8sPf7WC2uQE9gqnafZU5QdxNyNNOTsqbkepG9JBhAhm1pE1TaHGFrbgk27wJQt2-xka70cgA-QiAcxoSfXoa_IcJlqjLS3nIPPtvg2XUNgOIgFiDFaykCmUjRyp0p7s24xff4308rsDpsKD0aaMAQkOaFD9I_GykhCTaBnBxVeVHxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت عکسی که به اصرار ماکان گرفته شد
🔸
ماکان نصیری دانش‌آموز کلاس اولی مدرسهٔ میناب است که در حملهٔ آمریکا جاویدالاثر شد.
@Farsna</div>
<div class="tg-footer">👁️ 828 · <a href="https://t.me/farsna/437330" target="_blank">📅 02:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437329">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/303b09821f.mp4?token=XV70Oks5yL5i0H-YNEvD3Nte-qiC-bO3wQAgbOj_P5tD6KOCZSJkfWaFV49BWzbIw5eCdIFk6cXwNrkm8iBCSDFxN8QQrmQ43-DlZ6eX8KiBsj6USbjYGCz87zpAPhSolfzsCBwK-hBTzmaEwH5E8_vehI6ex1-WYciwfRwPOeQIO5LIDQdaEhdE7sAc-xQjnXssZBpX-_RAQa_buuHFBvhXZW2QfUr712iit5GjB-rCOBn07qCzW6spNyrmY8uSzADCAo_cRg8OABcOdCk3dpPlU-Npok30aMeP3ROsYgU6srR0q1GZYrmj8_gOZoEjeNiTGYeA2yJCOfDucVM2Jov69IEhUFxSP5SS483Ey9OmAPlx3aWke7e2rN7f_c9KE4c0lpTpBd8IyfsgKSUMQfU_6mVj3JEGmkLduSejp736qOAQMnpAaYgSyDNMHqR_EmyplXeSOuwyGsdQZqsZQQWYgIy09zhWC12yDHgrI4knMEJTyMynVHroKlmCOuoCZ2Lk9t2dR4gZeubU9nM_ZTR6Q_4GPqeChVp3DNPM021Jg4Y9c88pJSMxAIKwTKX17riYaVkntY8Iy8kuH_DpfVJsmDiaeNkrbc-a9U1tT_N5uEHvXwPWZ4lQ097V4HFvIj2gf5YzFp4Tf3K0csnxG8tSoui96uNSsuD6OACEY8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/303b09821f.mp4?token=XV70Oks5yL5i0H-YNEvD3Nte-qiC-bO3wQAgbOj_P5tD6KOCZSJkfWaFV49BWzbIw5eCdIFk6cXwNrkm8iBCSDFxN8QQrmQ43-DlZ6eX8KiBsj6USbjYGCz87zpAPhSolfzsCBwK-hBTzmaEwH5E8_vehI6ex1-WYciwfRwPOeQIO5LIDQdaEhdE7sAc-xQjnXssZBpX-_RAQa_buuHFBvhXZW2QfUr712iit5GjB-rCOBn07qCzW6spNyrmY8uSzADCAo_cRg8OABcOdCk3dpPlU-Npok30aMeP3ROsYgU6srR0q1GZYrmj8_gOZoEjeNiTGYeA2yJCOfDucVM2Jov69IEhUFxSP5SS483Ey9OmAPlx3aWke7e2rN7f_c9KE4c0lpTpBd8IyfsgKSUMQfU_6mVj3JEGmkLduSejp736qOAQMnpAaYgSyDNMHqR_EmyplXeSOuwyGsdQZqsZQQWYgIy09zhWC12yDHgrI4knMEJTyMynVHroKlmCOuoCZ2Lk9t2dR4gZeubU9nM_ZTR6Q_4GPqeChVp3DNPM021Jg4Y9c88pJSMxAIKwTKX17riYaVkntY8Iy8kuH_DpfVJsmDiaeNkrbc-a9U1tT_N5uEHvXwPWZ4lQ097V4HFvIj2gf5YzFp4Tf3K0csnxG8tSoui96uNSsuD6OACEY8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان‌های میاندوآب آذربایجان‌غربی بار دیگر به صحنۀ حماسه‌سازی مردم تبدیل شد
@Farsna</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/farsna/437329" target="_blank">📅 02:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437328">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5Uxc8YpbWPhtOQuE1qO_ywlkfbQsN_vmpEelWgACok5QrEE6sIOpXLC2V8EihMR6iv34jv8dthgihkWrTLpQgclaKXCH5dTro9CE-vUfc4_XTT9BzHHfEzoOsjYBIWWm22fj599jeeEmL4jlc65znX2pdYzcfo2LNUkgnytkd5oOo5y_jU65wZuCT2ZzSzO-ek93Q2sstx9HaawGMp_y8T-pUKuBYaLmOdPOuR2earNRTFiYN5M0VSVIqYDB9aRb9CAo5LrJnMXoPzIFIYyJK_toorOB4tPxBeeQtw-ZsdF_e-DOMHqje_Tc_ZCO01gCRxMFwqJXqafT6ZS7zHk5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
آملی‌لاریجانی: دشمن در صف‌آرایی مستقیم به زانو درآمده است
🔹
رئیس مجمع تشخیص مصلحت نظام: ایستادگی ملت شریف و نستوه ایران، دشمن را در صف‌آرایی مستقیم به زانو درآورده و او را به سنگر تحریم و محاصره کشانده است.
@Farsna</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/farsna/437328" target="_blank">📅 01:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437327">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🎥
آمریکا آرزوی همراهی نسل زِد را به گور می‌برد
@Farsna</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/farsna/437327" target="_blank">📅 01:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437321">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MdH0LSmreodG7I6st36fQ22O0PnUlzskJL9ijTe_NgnnhaSAg9zlQkQeiXQAK4byKKjUWfCjLgKarIEe5iMBREUPFjOoKiClxgKAxretBairGfkg5LLgrQU9rDV3aZajFWgBGdipK_9hAihSsNianiguvzJcDngWLvfNBIKAZdacoTZwXx_T4WQvbk62_0SzVuo8L_R51kYV9xnUDnFFXFXP6uZMFa0INZ6xPx4xWWh2AG9ZO8Z3m3xpGwTyuYstU0twAL-TnrU_UZSGIDNduGNQdJ27DMicffibETacAO9EX3L7mO1NwLZFKiiJRiBmN6sMr6gK150L8G-qaB7HBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GyxUpSTR8Kesph_s82XdxsZj1C9B_8FjLPKBW8QPYrl8JDjOg7UP_LaTiDDf3UvQhPoyOkwFPquaWzlOMBu1wUpqiv81bTKwK256KCI4TuXnXulaQl99NvcPS1VNB34Z7LvoMKMjutco7jQz1XkQQ8ib5fIOWKvbLAxqc2c8Y456t6qYDT4DfzGhk5iHBZK_M-QG_CrRxlen-XdPDzIJH-AWFxgSL4UqXqaLV26dOqg6-fZtSnJny4J8wq5RMQhHAKrXCgh08M1xwHCWYaUSf4O0dBIx4pKlV1o3a_60HHdC1xRRbfPP7BkBoiTrs6rhQupWF75DDwcRK9zoGgnHfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ShOzSwOTnG8Woq399nS_DxpdKmZVmakGCauQUqfl7Gptw-PTHkSrZRnsJvg5WF4Rr4PrpGyiWUqW_l3noou7hyPn6AqhQnP7Cy4_-IcMyOL6IGV8zuX-HxrABpb5jZksXKNJ-R497IIXkVshog9nIXG2KV34E5-6z0dV2F1hTi70mV3u16wg4bI-Bek2_7aF7VFaJhLxb2LZHL1rhn79sn7GoR0AJ3A8puYLXZ6zv4VjUaeU1mxa_nw13JucA09Ydbk-p60TzT5Hms8D-lvF4STHVdlkbZIVTT9SQi0H88aT0veK4tDzrukUUzw-_aOOVPJEZo5rVCPt6gkH8-Rasw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P1bQiWrlmXl8fK-m7EZ_SeH4M6jTU1Evex2F_igcdL5-QX-GvGzp7wdrjrEw5lvCf-oimfPv28gI54BqjDfMUVgLf1HTKrhDIKlc14G_SNMFKa8GYKd17RWTAhDSbqNG2dQvQNd8Qv91tuKde10sglZorrJITE_UVT2rbqk9wRVScpE5nlAEf_a_0NHkCpfheb8ZrHCC1qv7NduZvLrmNTVDO9iZeZvCb98qgRyY3yC9SKZrab9Llr163s5Pqe1RISyW3CqIb3RmHuPfLQz8nxaR3ce-PL0Jyaa_k1zdXW04k_3jtcTWXcpJM7zhPygAuyVlmgmCypMKkcxUt_0yWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qGv4hGeUPjxrjfXXrA2J1b0zAV1llym6avZiHrSmxHsMKxEyISle257y9VxWaWQnJfXI6y-5m1mCbRdGk7guOFwMzgHbJfUV-VSEfb50M46oIS0slaT0WoQ_4znF7hPV3C9Tei7SS0uCSgIjJ5M8eFGy3SJIaLxxWTimq9Nf8f2fQyboZ5H4ZeRTmGeaE3SGiPodEl7iSQmTddQj_AXMVo7RI-_NeY0PVnKzYpS5iZluempKPoqIz1uWezbNIcOTHBEefcFvYgKJNdw3i1DqGeLxPufAaUd-vWRBIBLF4MBMMC3Dl7FfCA1zV6sXCHYN41az4bL4o281NJ2WWV5NEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n0Iy_MhK20HPhMhSmqeL_xoOqq8yLQ-m7nX9K_N5ScvjW5rbpwIdWFfpXvcpJRvkzMg1t6PcVmpNXF8VNc_Ccpvm7IFhu5OnTa8rOw3Zb7sYDchZsKu1wAgdFtyqyOIYrdECCZ6PqlqIO_OFuTVLfUjSosWJdOm-S4EGWmtMZshiwG9pOhT90kjKq8nk6xS3Gj94I_FJulEJ8b8UqxfffVnWKLDAdJv-juPkShsVXTjkoubKogsRHnuAPyxgB2ZRj24hbJMfs9ZDbflq5Kn12WNp9tRw1JGufP9TP0Wm5n2vPoKeq2QHKdlrKC-f-HxlqpT4dhP3NGPiEALcq8KoMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۲ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/farsna/437321" target="_blank">📅 01:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437311">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EX0DSMI_3XKHXq-0YjVELt3ihfVXP6jFIo6MIGjbVRQ6bOKo8pWKz9Mq08CWuhMtPD-3EiisWcQvYzOY18fx_yo4HLaxDpbPknlvuB-apX6lGZNSzh1pA06GYHaqqrs8V9t3RrotUA9iqpJbk6C0IQoLfiAWdpgseWDUifL42HQpIs3MLb75aAI58hqd-sNyJ4eufHPO3dxTIFjkXpbjh-uNlUbCudpE37xFKN4KX51ya0hG-FG75QrBegyIYt3xf_p96sRjQaJUTEj_CNMmOgirc6H3-RL1EDE_Qd3e0WpZBBgPPVeK0UN3Udvud8WZ55l1fv9nmL9OtkopR8VawQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uIfpRvq4eqduVQArzZJTjz0-qFtu_2pynI6tlhKRPZkJSUANzzC7lVzXTPipGz0YaB00SacabRre0H-gsZLKz_NdpglhWONhKpFv3VtaA3yufCHrL2P2fggyxPtb1PEa0MHgLdHqOAEUKXSKt3vu88SvFCkuVDqvgb0QwJ10gxonpUR8AcbN-6EIWPhz_I9w_DgbgcGGoNNZM1HgeZOJhke9E26qfe0crIx_2HAt7ScsJ_QDMbEglwPbCn90FQcifoNe6GSH0z39QjOqOh0e6LdzUN7K4GKq2MdivHdSnTMW0NOUN_MqSicgjGUydc0fX5FWxfxVNff_yLArcg3Kcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DjaNx1ULjK1CP491b5SsaTn91g8Iz-Cdp_JVEzEQpItIAmWu53AUkYEFi8UUZ-DKYW0s7PpwzgGXXlYjT6yM9fnS4gkC8al0XDYc_faxk_JDyKbmlhE0PMrD4O5Jn2AnCRTpiFXR7iWr5sIyq6OkEhoq8i10Hgck7Cr4J9OHrNepAmkr4HGk009EuXoK71wPnumvgeSmqRmmjOZ0OGEmEWapxtGYbb7w4wTK8eKqkCaXdt5VVPxSZooqRzWGDJcU-RRSW7KlYqKKjHxg-ZZUlSv_prksdX6Il7Yg6SDErxuVx9sPB-NHsmSztc8kgXqTg18LswY29AsgKrjnlxy_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QEjdSfG3bDWMwVBt3yE3kLL71DU16sryn0h1YksXXbkTk-SRGmOBahNqmL_PWKWxEYJoi7PD78AMHTJ7NBwBD_uO9YKFWVO9oekT0xVSIW0s3cLmV0sUFt2EJ1fPlFaQFENAkBpH0EhzXk4IsvlLc1OPxqgJGabUApbGodQl07PPYKmmhIITfK3ofJkAO89h2yjXbzRH3te6HRlr_DUoC1Wj17aARmfVAfkEcrkEXT24LrTB6nd9BCxO2D4k-4zKhOowTQSJwGT7rBOQUYSCB0gSZHzRZSt1y7k35A05ajVQ3Yqk2ZJJMBnKVY3UhvEhhF5JsIiX3ZJMkyzmPSD_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGl5l0CneT3WLfoN0krilrKaRKL32xmCXsE3I3sRlM_SI2BP-f01hh_bKbZqbKUZgWDWyr5nvRoUOBeV86-vBTBjXYYeQwXTeQyx4-L3gGC9v7LRnnFlF3tMEzMKxnr9BE9ikxkFG1EaHT940lDlpg7dtsrri2NG1Dn_CDE2wP1Abp0KF3pAnHvV3pgKpM7J6Lcip2V7RNibVF5t7f-g3wq_pBzkT8nGc0-8GQdXAeXlwdvgC4Kqbu8QmtpxBN9FWqyruOH6-P9-dfelOj7XFV-y9yP_BpIFP9IMYEQYyNSK0JYdq-oPHh3uUTH23KkSMbWMN59PLJZEpxlzM2Rqbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lUZX35auIVCpMuk4DDaISK-oGnYCCrzKEME2UorYXe-bNR47XA19z5_rEPm7jyiwlgAmoLEJqfXpQwGnscUEQKAHO3ZqkCr9GLCc3BBznAUPVWx4XaPOD1o2cH3nNJzpJjE3FjZybrTC2l4OV5lEP2AYDGISdbuU8MLIXMHJ7tuYRDErnHxL1c4Oo0ANJZm1MBOGeWbuefv7ZIGvMr-Bm3CcjD5ip15IIOpBEn0DNwJPAEhu44VOoIMGG-IUUoHHLTVy07XTuXG_saZTiR3RbOle2LQEi-2XrA565THFv65_oYdiqkMWhBCDCTeoNFLP-FWlzVsNAngIpUr7tXH8_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U2jdsRlYIGP4_2flID5mj2mfDMy6BWdk8mMSHuEhLEwQhiNKzfcoksnCxqX2tBe3L0yNYJfuH3qxDRIlNTygTptJDdcEx9S8y7PUYYHaeQm2ChxXmAKv8cX6vlbq1wywQqBfWSDfHU4DKMgrlnHq35GoYkFHHHWAtOP_SGITn2SlCo30vZ671cc9ejFoQTsue4dwUWFmQ38kam8NybVF0-iyeQmGotnjy1AquM6uoSJC12W0N_Sapyk_oBb2xT_7SbXEGYppVpy1xlNoVTmc0jzjfqn7wVSPLWyRklDyooHsbvgFbhAtFFC0Y1uPCG0IIjFNLg506mOQHBS5ghVhjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v59WRUC5fotuGFV3lrz7P8uaNdO6eQfTK5e7Iiiq8dBm631UinjtjRn9CO7L-kd0z-SaoCCIy7aCgiMEg5e5djLiAx_zgIFMbGTAYbwjmIAlJegxNXACTUTFNoapgj8cK2QIIbBz-mXC0xcYRTSlScBguhyns5Ai5eYD7uQduzYeSKXdasCezyjX3YA-VYSDBrCfYkoT-DhQQkm6B2a1284fH3-moDPqHcPAFXgg8f22aPyDPe-LClgmhS5z9w3SFdNsNfC75u9PxVFQs6DkcqXvMynQLFMoJJ33tVW07PzCZ_ZtCDPQy6w-TWmxTMLdIB_3vrWfupRmQUSdgqx43A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6ORN4-zeu-WRiUpQT5-ctbhhPpu8pa-Pcm0a9woTnFg5_Xh-kHLhSPsUpZCsb6y7gphzeQMcgSzgKG8f1olaR9TNwVhr-_Gt5h7JMM4xaB1Ss99YUdZgabNdWZy4ZWAzYvFz5QQTgUMZm0cPaoEszHh9T5xU_wxQEzKupFVxLOnrXx9jHw98Z-A-BxEWaCzhm5PgN6Is4b2HynR9Phf0HbUsRMmL7s99p_lwdhAwUzwsPrfwSthoAnapKJyTW7Z1bLZrDUS5vcr5CHL2IlQi5iCdEMwGvNf3TuvniQYJ20HWtyHiCBsHNaIa12LVzHf92EygrpN5Zm4qZbzyfArZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YbfUc2oGE6GIJr5tuSuVUBJf1JuiirsK2jkigb9obtc0T0smy-zYQbwYyz3KNv73lNXMFn0M7i7dw2Q-gnHDtIa24h4EcRhJMJMndf7cbCSeDQS0z4j0jc_VRg7N_BA-pB9smP-tC6sa3i2CN_xfD2pxRIy-2HmA7uy77DAkXAanh80GbU_aTOWkX--c0TxLPC2V1FTvXDb3-6AH2ZtLz8diIrw6S6AvwuZg8teX55g5YygANghSofWNIE8crdOINvCfPvCwjs9L-1HvxAO87TTidlLwmmwr4cH-7E8MMVjpUM0nnfBom66VrZ-aRCowrGmHUzvpUnHc4hN0w3iR4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/farsna/437311" target="_blank">📅 01:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437310">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzZaAvOruDYP5cPUeTumS5AVs9SLhhZU5uQ5y9hCLhUikJNcUltgc4oF4QTtwLD1qPBw64icZ9Z2waFe1h2uH4Heowkz97MdYT_w9vBYjt9191Sfs2AvQCsQGnLOKCTQkI-bDThYVuglYtmr9RUfjfdZtVpTFilMRKG98diqSKP9pnoKQ9w_TQA2JZMgGUSDAKXxinyHYebqA7MrjQa8vqeJDb0UBXOgp3oFk115Dfy-KffVo_Bmf-T4xW5ILyjP5AcvNpZ7JrGbBdG-unJEV-w9sGuLSR52YqpwTzdA4mPWd7GAcPIT-6JBcejkXRHO07NANEEueyaBVbCAM5c9nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفت‌وگوی تلفنی عراقچی با دبیرکل سازمان ملل متحد
🔹
در این گفت‌وگو راجع به تحولات منطقه‌ای و بین‌المللی، به‌ویژه وضعیت منطقۀ خلیج‌فارس و دریای عمان، تبادل نظر شد.
🔹
وزیر امور خارجۀ کشورمان ضمن تبیین آخرین وضعیت روند دیپلماتیک موجود برای خاتمۀ جنگ تحمیلی علیه جمهوری اسلامی ایران، سوابق بدعهدی آمریکا خصوصاً خیانت‌های مکرر به دیپلماسی و تجاوز نظامی علیه ایران به‌همراه موضع‌گیری‌های ضدونقیض و زیاده‌خواهی‌های مکرر را عامل اخلال در روند گفت‌وگوها به میانجی‌گری پاکستان دانست.
🔹
عراقچی تصریح کرد: جمهوری اسلامی ایران به رغم سوء ظن شدید به آمریکا، با رویکردی مسئولانه و با جدیت تمام وارد این روند دیپلماتیک شده و برای رسیدن به نتیجۀ معقول و عادلانه تلاش می‌کند.
🔹
در این تماس تلفنی همچنین راجع به مباحث کنفرانس بازنگری معاهدۀ عدم اشاعه که در نیویورک در حال برگزاری است، گفت‌وگو شد.
🔹
دبیر کل سازمان ملل متحد نیز با نفی توسل به زور علیه حاکمیت و تمامیت سرزمینی کشورها، بر ضرورت پایبندی به اصول منشور ملل متحد و استفاده از راه‌های دیپلماتیک به منظور برقراری صلح و ثبات در منطقه تاکید کرد.
@Farsna</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/farsna/437310" target="_blank">📅 01:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437309">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35821f22ec.mp4?token=Gyn_ZWpGml7_j7X3ctkyTcUCT9wm5L9twrtHPQbUSJzppB1lMQmySzJ9BG2oKQZtTJJ6hUl7HUMbdlWRy8ypMJ-yTY375029l_HIyKhljxED5qqwhXBIQ_SrNBk8fafaAh7wi3h-wPHQ1EVS81DXhlWLmH-2YM1JKOhPIiEPCFaHl7nIZt9UvVcd5oMGr5pLeNKqJF2FRvAJbpxQXtWbt-xQzBVxLYV8Q1HUbrQZajyiNKfsNzSkCjEHU4Td9iWaBfDEOyClMQ9J5VEeNCt5C_u-PGB9k77nFGy3nAgk9CzFviHhy5Yn6qgddlLfcnNcP0-bawjBMTT4wM80vz7Skg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35821f22ec.mp4?token=Gyn_ZWpGml7_j7X3ctkyTcUCT9wm5L9twrtHPQbUSJzppB1lMQmySzJ9BG2oKQZtTJJ6hUl7HUMbdlWRy8ypMJ-yTY375029l_HIyKhljxED5qqwhXBIQ_SrNBk8fafaAh7wi3h-wPHQ1EVS81DXhlWLmH-2YM1JKOhPIiEPCFaHl7nIZt9UvVcd5oMGr5pLeNKqJF2FRvAJbpxQXtWbt-xQzBVxLYV8Q1HUbrQZajyiNKfsNzSkCjEHU4Td9iWaBfDEOyClMQ9J5VEeNCt5C_u-PGB9k77nFGy3nAgk9CzFviHhy5Yn6qgddlLfcnNcP0-bawjBMTT4wM80vz7Skg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طرح جدید فدراسیون برای سهمیۀ آسیایی
🔹
سخنگوی فدراسیون فوتبال: طرحی وجود دارد تیم‌هایی که می‌توانند سهمیه بگیرند به کنفدراسیون معرفی شوند‌ و یک تورنمنت برگزار شود.
🔹
البته بحث قطعی نیست و فقط در حال مطرح‌کردن با کنفدراسیون هستیم‌. در صورت تأیید AFC مسابقات برگزار می‌شود و تیمی که در رتبه بالاتری قرار بگیرد، به AFC معرفی خواهد شد.
@Sportfars</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/farsna/437309" target="_blank">📅 00:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437308">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OifbfhBVvo3p-yJ5fwLeQMGFMPIDRTIX00EQlS2IkEpvzgWUukyG0Sw6fEjBAEUF2mc9RYPQd-pvzH1tc_UecXA7TTZJFasma_HXUXApJNMetAfZq7YCa4EjMBVSy_YGtyMcvpL5GuixeB200blbFQVfT8nDUJ8XmTo-fGsY38S4q7Bm1JC5Av7wuq1oA5oZnMTOKTGpgai5sjPM9qUOQjSu1gn578iPaKhGH4vJOADDxglbhE1I0z62NRHLr8IeWD9YoBVydpZCDubmmU_D15qblHWluBAjlBm7rqTfnpoG_tOrxZAXYWqLZAiWaaXB2Duzk6KvZS9Ogqlg7aHw9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخۀ فرزین برای هدایت اقتصاد ایران به مسیر رشد در پساجنگ
🔹
رئیس‌کل سابق بانک مرکزی نوشت: اسناد مهمی که محورهای اصلی برنامه اقتصادی کشور را تشکیل می‌دهد، اسناد برنامۀ هفتم توسعه‌وبودجه ۱۴۰۵ است که هر دو در فضای قبل از جنگ و با پیش‌فرض‌هایی تدوین شده‌اند که نیازمند بازنگری است.
🔗
یادداشت اختصاصی محمدرضا فرزین، رئیس‌کل سابق بانک مرکزی برای فارس را
اینجا بخوانید
.
@Farsna</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/farsna/437308" target="_blank">📅 00:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437307">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugMKcPTqrL6-1EgrvvHHmQiLGpaeCPhpxFVBaUrbef7bZ5QlHBfQ2PcwrU_1QCZqPnbwECRV0obomw5L89nj0Ngn_5cNu2byRSTnT-MoFHJsFKRutovjs5FDhQkC3_8PKXEQ1CTK2otwUhxF4WDhE6cLCem0pirE61w1fPZrue_0CZeHfwZZT4UhD19IKlI_v2j0jzxtjPWvepQninnSOm1371oj2D2nGDutIf4JeAiw25LLFlqVT8-4J3wL3zcej7rFz69wqZ7KPU8b08vwkQeHos293K-dRrbAMEMM8M0TUigeEJvf_m34cTZcwNnOT36xFAm5urnNGlKx7vPuLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موتور پروازهای داخلی و خارجی روشن شد
🔹
پس از جنگ تحمیلی سوم و بازگشایی آسمان کشور، از ۵ تا ۲۹ اردیبهشت ۱۴۰۵ در مسیرهای تهران-مشهد، استانبول و باکو بیش از ۱۱ هزار مسافر جابه‌جا شده و مسیرهای جدید شمالی و شرقی نیز درحال اضافه شدن هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/farsna/437307" target="_blank">📅 00:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437306">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48df89f74c.mp4?token=LmM9avg_qYzAkqSCHYY16H6pZI7QNtJx0jpWLWel7BFuqMsO93h2eAQlAi9fy7O9D43JaJ0l1IFEUl6qaEtARVFNaf2Bi88u6QPUbOeKQzs6ihKYNM-C6mSLYnsyjjoGeaNrG8QIz2UFV2gNTT81bIstOinvTjJbQx1G7rXOflo4Ir4hrGgWqGz5HrrC2ro4mlyzGqn3wuDAmCXl8lu5OE14S9ucCDEyQiwRTR3YfeAGp3spqPy7qEIIs4oIPt9p0352cUOBXs_S14xPuNntI71HT-OF6-ITHhJTzs3Aky2u0rIt7YpSSMGt8GtY4u0vcOR9OCoNbx693FzYCtInMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48df89f74c.mp4?token=LmM9avg_qYzAkqSCHYY16H6pZI7QNtJx0jpWLWel7BFuqMsO93h2eAQlAi9fy7O9D43JaJ0l1IFEUl6qaEtARVFNaf2Bi88u6QPUbOeKQzs6ihKYNM-C6mSLYnsyjjoGeaNrG8QIz2UFV2gNTT81bIstOinvTjJbQx1G7rXOflo4Ir4hrGgWqGz5HrrC2ro4mlyzGqn3wuDAmCXl8lu5OE14S9ucCDEyQiwRTR3YfeAGp3spqPy7qEIIs4oIPt9p0352cUOBXs_S14xPuNntI71HT-OF6-ITHhJTzs3Aky2u0rIt7YpSSMGt8GtY4u0vcOR9OCoNbx693FzYCtInMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسۀ حضور نطنزی‌ها به شب ۸۳ رسید
@Farsna</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/farsna/437306" target="_blank">📅 00:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437305">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad6eb8e738.mp4?token=DEYAoObrutaervUN4E1Etx32mrriOQn6tfEc7WkLs5KMPkXwiuacAXl7uKSBcZUAX24jL0WSZSaREQxivBGQ7k44CdA9UrdKB1FQigcSUcrZ4fOvLATnHvVkpJILSQpq0gHZCKthSMJs-5zpBbEZZqciTNCa4tHRUl5Bo_ySUIutYtYhnFEDgFvVKiQADKkh1-yL9PXfJX_Z_cj2cg5H9qI7CXlfc_4v8ykOchOhx23P2dfANZpOZmLo25Yu_mNrPHp7Z0VFxN1Aizu5fegIHFL7ZIX9aUoInvZo3RN0e7cM33OWcsQOEZYD0J_Z4RCZO-q3v-qFkzq8FNPAl8q0UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad6eb8e738.mp4?token=DEYAoObrutaervUN4E1Etx32mrriOQn6tfEc7WkLs5KMPkXwiuacAXl7uKSBcZUAX24jL0WSZSaREQxivBGQ7k44CdA9UrdKB1FQigcSUcrZ4fOvLATnHvVkpJILSQpq0gHZCKthSMJs-5zpBbEZZqciTNCa4tHRUl5Bo_ySUIutYtYhnFEDgFvVKiQADKkh1-yL9PXfJX_Z_cj2cg5H9qI7CXlfc_4v8ykOchOhx23P2dfANZpOZmLo25Yu_mNrPHp7Z0VFxN1Aizu5fegIHFL7ZIX9aUoInvZo3RN0e7cM33OWcsQOEZYD0J_Z4RCZO-q3v-qFkzq8FNPAl8q0UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: در تلاشیم پلیس‌هایی که به من رای ندادند را پیدا کنیم
🔹
من رای ۹۹ درصد نیروهای پلیس را به دست آوردم. باورتان می‌شود؟ هنوز داریم تلاش کنیم بفهمیم آن یک درصد چه کسانی هستند؟ @Farsna</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/farsna/437305" target="_blank">📅 00:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437303">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJQG_x5PMKeYdea02z7q2u4vOuSK6w8cjMlbsgXjBCNHhl-lKUFm7nb8ZzzwXWnwlIzrhKzYKweZlNxOOFMw6gVok5cKQW_5ctQTeCbeKTtMYV4_DlDimVm8gqRLBAvesj0FqC8QrwWdSRAAqLCos4KbWgl1G4dfzP2Etcm9T8ow3xGPQEY-ShiL8xjI8Q3pRuMmyPEx1x9P1f2Y6Y7vYu12bMqfhMwDPUEWlPb2G8uftKmIlMtlg0o1QHFuC4sKXFXUWxEk9Frkdlgai_2_vor1vbSOeL7lvimVlun9GWLazd23OLAzTcu0O93CgO59K9vpvHaO22SQEVcW8wdIMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسفر حج
🔹
مردی از سفر حج بازگشته بود و به دیدار امام صادق(ع) آمد. او شروع کرد به تعریف کردن از خاطرات سفر و تمجید فراوان از یکی از همسفرانش.
🔹
مرد با هیجان می‌گفت: «یابن رسول‌الله! در این سفر همسفری داشتم که نظیر نداشت. او مردی فوق‌العاده متقی، عابد و فرشته‌خو بود. هر جا که برای استراحت توقف می‌کردیم، او بلافاصله به گوشه‌ای می‌رفت، سجاده‌اش را پهن می‌کرد و مشغول نماز و عبادت خدا می‌شد.»
🔹
امام صادق(ع) با آرامش به حرف‌های او گوش دادند و سپس یک سوال ساده پرسیدند: «در این مدتی که او مشغول عبادت بود، کارهای او را چه کسی انجام می‌داد؟ مثلاً چه کسی حیوانش را تیمار می‌کرد و بارهای او را می‌بست یا غذا آماده می‌کرد؟»
🔹
مرد پاسخ داد: «افتخار این کارها با ما بود! ما با کمال میل کارهای او را انجام می‌دادیم تا او بتوا‌ند با خیال راحت و بدون دغدغه به عبادت و نمازش برسد.»
🔹
امام صادق(ع) نگاهی به او کردند و فرمودند: «بنابراین، همه شما از او عابدتر و بافضیلت‌تر بوده‌اید.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/farsna/437303" target="_blank">📅 00:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437302">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51ac83651c.mp4?token=RYJZFiTlwpJv-yO92EICP-1osUg9Dd43p8UCxSWDOASjFgHXTPS9z7GlfmzV8wB4CdkWlJ7rz238HrkFO7N0-o-UG27cHhgZ2Q59aCPWKSSjSvzz0kyxy5IY2wdFbEIer2JwsXSC2n8yRteHbRlpLdsn7f8AP8LzMc1yGaDdgHkgKqwxnejsbeY4eoUrffeEVfDoT7PRv_uZw-AGSTFOZctaVP4_kpouIaGK5xlxE7Qz-c4ChQsbHniDqekq5960e4sw64BHGwXl9aU5LNGqRsVJXtd9hRFhqVSKsiqxA3gBVE1-DTOaV-bhsHLuXB48fAqyQ28HsZqLc36jRq1b64WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51ac83651c.mp4?token=RYJZFiTlwpJv-yO92EICP-1osUg9Dd43p8UCxSWDOASjFgHXTPS9z7GlfmzV8wB4CdkWlJ7rz238HrkFO7N0-o-UG27cHhgZ2Q59aCPWKSSjSvzz0kyxy5IY2wdFbEIer2JwsXSC2n8yRteHbRlpLdsn7f8AP8LzMc1yGaDdgHkgKqwxnejsbeY4eoUrffeEVfDoT7PRv_uZw-AGSTFOZctaVP4_kpouIaGK5xlxE7Qz-c4ChQsbHniDqekq5960e4sw64BHGwXl9aU5LNGqRsVJXtd9hRFhqVSKsiqxA3gBVE1-DTOaV-bhsHLuXB48fAqyQ28HsZqLc36jRq1b64WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مردم گناباد علیه مفسدین اقتصادی در تجمع امشب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/farsna/437302" target="_blank">📅 23:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437301">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14c7bc1872.mp4?token=qmLMMmTDaKnOSVihINQw1SoGUpyx4LnS8RJOzzKcj02zX6_alw9a0yGFu4eLw4_Am7xhyRRsEMJ-AgNOFkxvYelhj99oX1XF4oee1jLmdmflKyeEfpV9fLCci3vDqguf6J0tpYkGv-C-WpMaVC4F4nR7O8qWeJlH9XkLFoKD66nnX1prlLq_okGGU-IewgZuLQhHu65D2GHD0RXlkJs0N2rmMo6C8go4R8Wdy4qvHvSFkS3q_CNxzOiw0QEGkV738JiEuAMWlt9ISb2eej7P2I9cwD1LdOwUSG4hiPQJYzYv9Qk3YFN4Y0-Fb8AzYhIfQ1fsboL8lZNNJH_8cPhAQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14c7bc1872.mp4?token=qmLMMmTDaKnOSVihINQw1SoGUpyx4LnS8RJOzzKcj02zX6_alw9a0yGFu4eLw4_Am7xhyRRsEMJ-AgNOFkxvYelhj99oX1XF4oee1jLmdmflKyeEfpV9fLCci3vDqguf6J0tpYkGv-C-WpMaVC4F4nR7O8qWeJlH9XkLFoKD66nnX1prlLq_okGGU-IewgZuLQhHu65D2GHD0RXlkJs0N2rmMo6C8go4R8Wdy4qvHvSFkS3q_CNxzOiw0QEGkV738JiEuAMWlt9ISb2eej7P2I9cwD1LdOwUSG4hiPQJYzYv9Qk3YFN4Y0-Fb8AzYhIfQ1fsboL8lZNNJH_8cPhAQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین هدیهٔ پدر آیت‌الله آل‌هاشم به فرزند شهیدش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/farsna/437301" target="_blank">📅 23:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437300">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daea970878.mp4?token=Vun1Y5Atef3EwWPStlM-B7BnLHpehxi2D6tqurJuj8UXI5wYVpx3ypKI0Efm9c0kAliYy3hV3bV6SPZZb1truz47OAwjvYRaa96xEkm9PMzbeBR9xbOW4PIs3JPQHdCfIcUWFwcjJNqbawUmsOimyjUNmA2IkQqE72R6dn7oIzrcZJwKGLtd13otqN7ea3v78uSo-_fnpdbwX57kpkVjMBf9JlqYvgz_G4W9M8jIzGV8thbJj-5Ar9BDV9GVlwbTEZTN2UhjdMJlhzMbhzky1-0Wkk4LMuzMJKPKgUFBDvprXnKUV_vlIHCsLg-5VLZ3sTrPJGWN2o72rArMcF7btw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daea970878.mp4?token=Vun1Y5Atef3EwWPStlM-B7BnLHpehxi2D6tqurJuj8UXI5wYVpx3ypKI0Efm9c0kAliYy3hV3bV6SPZZb1truz47OAwjvYRaa96xEkm9PMzbeBR9xbOW4PIs3JPQHdCfIcUWFwcjJNqbawUmsOimyjUNmA2IkQqE72R6dn7oIzrcZJwKGLtd13otqN7ea3v78uSo-_fnpdbwX57kpkVjMBf9JlqYvgz_G4W9M8jIzGV8thbJj-5Ar9BDV9GVlwbTEZTN2UhjdMJlhzMbhzky1-0Wkk4LMuzMJKPKgUFBDvprXnKUV_vlIHCsLg-5VLZ3sTrPJGWN2o72rArMcF7btw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: در تلاشیم پلیس‌هایی که به من رای ندادند را پیدا کنیم
🔹
من رای ۹۹ درصد نیروهای پلیس را به دست آوردم. باورتان می‌شود؟ هنوز داریم تلاش کنیم بفهمیم آن یک درصد چه کسانی هستند؟
@Farsna</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/farsna/437300" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437299">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ce61e2cae.mp4?token=V8HbKADPyS7QmdtQe410owpaAMjm04Pk5IVku5DZeEcYKqso5UKCCH8HJe4NqEpyUh-iMFm931fi9JEbJOqf-BpNTpH4k0f2LhOYRzRrhcjXfIuzCTKCtB8IQqt4473UDAH6o5hpsIeMYxXP79VQC756MAGxfpbJXOgWTZUJBshRlBBBseYWE58I089ueYNvDrFiJ7Pa-90ppiYhckucKIqpEgDa2_AE0kr8gTwZWIy-T0MWyHUSY734v4FR0itpZDqnmSd-8Yhd4WZ0eBu4MHmL0yJ1s3owyRw3_LiSdOqoZQNluu43vGIHah_WdIhrfRw-nQ_qNmt6qNn3atvVFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ce61e2cae.mp4?token=V8HbKADPyS7QmdtQe410owpaAMjm04Pk5IVku5DZeEcYKqso5UKCCH8HJe4NqEpyUh-iMFm931fi9JEbJOqf-BpNTpH4k0f2LhOYRzRrhcjXfIuzCTKCtB8IQqt4473UDAH6o5hpsIeMYxXP79VQC756MAGxfpbJXOgWTZUJBshRlBBBseYWE58I089ueYNvDrFiJ7Pa-90ppiYhckucKIqpEgDa2_AE0kr8gTwZWIy-T0MWyHUSY734v4FR0itpZDqnmSd-8Yhd4WZ0eBu4MHmL0yJ1s3owyRw3_LiSdOqoZQNluu43vGIHah_WdIhrfRw-nQ_qNmt6qNn3atvVFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحنه‌هایی از ایستادگی مردم آباده در خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/437299" target="_blank">📅 23:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437296">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LaZVPY9KIKS25fODp9sfhE5xGiNymBPzd0K0tCkFy7jRu9cRwqWiEatkVKi1dC28svfDx4tVVmgvWOgqlrUU16ZEVjAr-MwW0H90iTjYbBIDvZ-kxzFmajQPNYHo5wchgbyuzNOQ2dwswvC2Ou3qmD72ZJmRMzu_Ofi8IgU3WP0KOaY3WZS-peWop6Akzwyu3ZBxjam2_14zltJrmv1EDTHy-K8JktncI1yj9yvcOUU4cPNYBlFQNBuKEP24nrRxT3C1KacCY0j3-TeWP_fPmeYOHwUBW4YXDQQa6xOyySVOH5296Eo7ex8GvS-aL1hufzOD2rTyh0-7QQEhc_f2QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CCImNxKz9VPEPjOgctnS5M2VpUX2a5EfOTdiJbyHBmM_kEeOVkfs_Raw5VMzqvGgKavX4E09IXOIKwv-V0DlSzIFNAFbN17XgI7WYibbzsFzQe75V1oRASMI9HkEUhTv0p64qJ7hi8bRk0wFVxEEZ3Vw3IRbKfACrvljbkO5qCgHY8D_R9Gb9wrjY2SaVps_MWSwZ7POffMhbLTyMf0JvNmBXDywKcump1BiahEGwajPWnLGAaYvvJ9Sjtkbjc8g7D0IYSkEuJrQahmzAn4gYtasfRFKciiJyxL8r4XDhHckFfQgSOT1sgr8gmggohppVlWtw-D7A9xsE3HBcIKEQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/undh2KAFr0FmUipCsd21GVFfmr_d5Tk9pxxnWyYmU6pJJisAOPqWW50h3lZN0QvVtn_-DIcsDx06GGtJoFGf3NGOK0Su4Buk6H1wrFfOKqCVQwANF6XlIPJYqBWohjedLyv86Xotu6wkQkeHNZeFH5QAcJ24bikx6zatwktbCEsqOHLEp7btEt1ZZgjn5spYtVHeDGHG5VLwlTi7PfML1KkKHJXUdYav0L_PhKT3NoPMbE7b1zsR_cczfemswbASpyfwCIB5cm0PMB-sjz27p7YATBIhqjk02OYpxQbuhCco8w_YffmGEYZgHScfHW5NehzGZUiaN91NVnvQVhpNwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کشف لاشه پهپاد متجاوز به حریم کشور در هرمزگان
🔹
لاشه پهپاد اوربیتر دشمن که رزمندگان پدافند هوایی جنوب شرق کشور آن را در شب‌های گذشته مورد اصابت قرار داده بودند کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/farsna/437296" target="_blank">📅 23:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437295">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9DwlLHyUQj9PaGmHCZKR9SlKfFsbUwIZ8HTSZ3BTxbfZikAexIAYosGwhvOyXARQxywfP0RUnbK7TGKTEGNoUzAIzw4SyqQC7XZfhuBLxL9LFtKD1y_OrKnt4-QVG5hHW6y_8nOb0ofauqbBv-xYbLmjPhO_KAIMTKQRL7CEu-KuEfCDAY4YpPnG7df6GftDHWWxb6LAdbE4xARyCVvlDp7KtrpMqijGruQpkds63vQdoRXMc8qNYIZkedsylweBm3uU_FDXHYdEKfSKfsFoU8HyV9_7NZZJ67I3pk9uaos2HmWGzYpHfwoJWTpxljm3-sUTjlS-VTGdttuo3AMOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزیتا ترکاشوند: هنرمندان می‌توانند شاهنامه‌ای دیگر برای ایران بسازند
🔹
آزیتا ترکاشوند، بازیگر سینما و تلویزیون در گفت‌وگو با فارس: فردوسی درحقیقت یک شاعر حماسی بوده است و هر زمان که اشعار او را به یاد می‌آوریم، در کنار آن مفاهیمی چون حماسه، شکوه و غرور جریان دارد. در واقع یک روایت را در قالب شعر و به شکل حماسی خلق کرده است.
🔹
به نظرم هنرمندان در امتداد این موضوع می‌توانند روایتگر تاریخ روز باشند. حماسه‌هایی که مردم  در دو جنگ تحمیلی آفریدند، نشان دهنده آن است که پای آب و خاکمان با غرور ایستاده‌ایم. می‌توانیم از حماسه‌های این روزها، شاهنامه امروزمان را رقم بزنیم.
🔹
قالب‌هایی چون نمایش بسیار می‌تواند به این موضوع کمک کند. به نظرم این روزها می‌توانیم شاهنامه دیگری برای ایران رقم بزنیم.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/farsna/437295" target="_blank">📅 23:24 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437294">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🎥
شوروحال بروجردی‌‌ها در هشتادوسومین شب خروش مردمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/farsna/437294" target="_blank">📅 23:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437293">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انفجارهای کنترل‌شده، صبح فردا در کهریزک
🔹
سپاه حضرت سیدالشهدا(ع) طی اطلاعیه‌ای از احتمال شنیده‌شدن صدای انفجارهای کنترل‌شده در ساعت ۸ تا ۱۰  فردا در کهریزک خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/farsna/437293" target="_blank">📅 23:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437292">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f0bc381f8.mp4?token=pBdpJSNfN_4u6wmgV0PIwPDJQaQKeYmYDQfCMGalkylMi7Eke-SeU_aGSdgDOddyjeM6fzNS2HOw0Zy1NfYlKmZ48DE4VmbyaZoppDLzyly_jvsUZkfcorGyVOPMfYQmR0WREEJBrYE1dZqN1_UYgO2uV10xtFZraMRIbttOhHkMD_16-exvkhnHCbEoP0MNCa8QkLHpS4FPbi8fY6yu9U_yW-ylVLAouitG7i_pYPSdRYf4f29cPR0Z5pulTyH9UknRKr49YByOYqXf5knln0LvDKQeWtkcm5qi_nou4trPWN0qtcLwXIfliSIDk6R8ryyPT49rkgXRISPiWXHbZbXtlpTQmOVLOzyUoZxhKqLhWXhpX8cruCu6WtPCOMOrym2LRDI9l0TSRwCf38kJ0TXh7bCmDFOx9K6ClwhIgvqG8ZGLHcpP2gbljf4LyWo3B2AYwbuGh3vXxHfoki-JP2ZKagn1pnHC2AMcCYW9D-7wngsBuuv_MhxGj7s8t6oHH9nTyO4r3p_c6CiQZzC8OF-v3IQl1qDLbEL_xKWu6drS-cMM-YCvV-noGgG0i1bE9FB9AI-r3XseWQxAx4JAGUjelvQEFJEO3UDrdlEfmrGuF-AoN0KUVuQgAkaiG_RbSEbPnokkO4Mrt0cZv2OBHBoeveYTj_4UHVJ7USm_dis" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f0bc381f8.mp4?token=pBdpJSNfN_4u6wmgV0PIwPDJQaQKeYmYDQfCMGalkylMi7Eke-SeU_aGSdgDOddyjeM6fzNS2HOw0Zy1NfYlKmZ48DE4VmbyaZoppDLzyly_jvsUZkfcorGyVOPMfYQmR0WREEJBrYE1dZqN1_UYgO2uV10xtFZraMRIbttOhHkMD_16-exvkhnHCbEoP0MNCa8QkLHpS4FPbi8fY6yu9U_yW-ylVLAouitG7i_pYPSdRYf4f29cPR0Z5pulTyH9UknRKr49YByOYqXf5knln0LvDKQeWtkcm5qi_nou4trPWN0qtcLwXIfliSIDk6R8ryyPT49rkgXRISPiWXHbZbXtlpTQmOVLOzyUoZxhKqLhWXhpX8cruCu6WtPCOMOrym2LRDI9l0TSRwCf38kJ0TXh7bCmDFOx9K6ClwhIgvqG8ZGLHcpP2gbljf4LyWo3B2AYwbuGh3vXxHfoki-JP2ZKagn1pnHC2AMcCYW9D-7wngsBuuv_MhxGj7s8t6oHH9nTyO4r3p_c6CiQZzC8OF-v3IQl1qDLbEL_xKWu6drS-cMM-YCvV-noGgG0i1bE9FB9AI-r3XseWQxAx4JAGUjelvQEFJEO3UDrdlEfmrGuF-AoN0KUVuQgAkaiG_RbSEbPnokkO4Mrt0cZv2OBHBoeveYTj_4UHVJ7USm_dis" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری آمریکایی: ایران می‌تواند شریان ارتباطات جهان را مختل کند
🔹
لئون سانچز: ایران در تنگه هرمز فقط بر مسیر نفت تسلط ندارد، بلکه به یکی از حساس‌ترین شریان‌های اینترنت و ارتباطات مالی جهان نیز اشراف پیدا کرده است.
🔹
دست‌کم ۲ تا از این کابل‌های اصلی شبکه ارتباطات جهانی در آب‌های سرزمین ایران قرار دارند؛ آن ۲ کابل گالف و فالکون نام دارند.
🔹
ایران با گذشت هرروز بیشتر و بیشتر به اهرم قدرت خودش پی می‌برد که هیچ کشوری نمی‌تواند این اهرم تنگه هرمز را از ایران بگیرد.
🔹
اگر ایران تصمیم بگیرد این کابل‌های اینترنتی را قطع کند یا حتی تهدید به خرابکاری در آن‌ها کند، بخش بزرگی از اتصال جهانی تحت تاثیر قرار می‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/farsna/437292" target="_blank">📅 23:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437291">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مقام ایرانی: نیروهای مسلح ما برای بدترین سناریو برنامه‌ریزی می‌کنند
🔹
الجزیره: یک مقام مسئول ایرانی امروز به ما گفته که هنوز هیچ توافق نهایی بین ایران و آمریکا وجود ندارد و تلاش‌ها برای کاهش اختلافات بین تهران و واشنگتن ادامه دارد.
🔹
این مقام به الجزیره گفت تحرکات دیپلماتیک ادامه دارد اما فضا  برای یک توافق واقعی کافی نیست.
🔹
این مقام ایرانی هشدار داد که نیروهای مسلح ایران با نیت‌ها سروکار ندارند و اقدامات خود را بر اساس بدترین سناریو برنامه‌ریزی می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/437291" target="_blank">📅 22:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437290">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99c0b51c08.mp4?token=Mk326J7Cm-mpbWm2ogw7wyH6QvcWRx-coXbXUP9CXfqFStwjLA9e3Ho9QBKuAeDZaMrfWe-SgSYbHX8StghxWsn-xhjIzHBWTFIaguUknWA30d-nsiuuQwIZjLq1-RGirQDfkY8B8UWyVMZesEW8teGIsB19IVDCRAZUUxtTNqj9HSaLrphZHoykigRZjroyr856wiwG9UiOP4yTw3GjGf8Zw5vdBFjq3vtBDn7FSSqB4npb4ILE3nL59JMHaKywZZ9Umb2vxDIOxRjWO5ITmzGvWvFnrUQBpjQ3LDb_-XZcElm-e-_nXdU4SnbWb7lyGg4RJRPXq_ItGLEPNcMGfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99c0b51c08.mp4?token=Mk326J7Cm-mpbWm2ogw7wyH6QvcWRx-coXbXUP9CXfqFStwjLA9e3Ho9QBKuAeDZaMrfWe-SgSYbHX8StghxWsn-xhjIzHBWTFIaguUknWA30d-nsiuuQwIZjLq1-RGirQDfkY8B8UWyVMZesEW8teGIsB19IVDCRAZUUxtTNqj9HSaLrphZHoykigRZjroyr856wiwG9UiOP4yTw3GjGf8Zw5vdBFjq3vtBDn7FSSqB4npb4ILE3nL59JMHaKywZZ9Umb2vxDIOxRjWO5ITmzGvWvFnrUQBpjQ3LDb_-XZcElm-e-_nXdU4SnbWb7lyGg4RJRPXq_ItGLEPNcMGfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال کم‌نظیر مردم عراق از «محفل القائد المعظم»، یادبود رهبر شهید انقلاب در میدان التحریر بغداد  @Farsna</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/farsna/437290" target="_blank">📅 22:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437289">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e11689cc9c.mp4?token=V9ct6G8W9OgFOAHvz7HXrjO2YnTLQ9BgbZh7x3mcgtfDvlrv0Ebk2FZ2QHcplaCO2BLp5qlnbwNDvMMaTSNefpHPpBigGrnxQnXx80J41jBQEDriBzIy57cgI7ESVcRdElhqcZ0Fc9KHgHhUFu5CTF--nOeuYKDQh-dkUK3RMqfqHW2vIIb7cOje4Orf5sUQ8IfSl4IRgDvpyUkx1Xeys_arswoaGYQz46b_QAi88G_PbO3qpvosh4Qaj07R9EzhyT4_jeUMyl5aiZ_zuZ8kThS3Yc2E5dTQmzqzm9HXNloqU3EZSW3EXGylsDYRT158Jor2V_dqEhMVaIJL6iw7mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e11689cc9c.mp4?token=V9ct6G8W9OgFOAHvz7HXrjO2YnTLQ9BgbZh7x3mcgtfDvlrv0Ebk2FZ2QHcplaCO2BLp5qlnbwNDvMMaTSNefpHPpBigGrnxQnXx80J41jBQEDriBzIy57cgI7ESVcRdElhqcZ0Fc9KHgHhUFu5CTF--nOeuYKDQh-dkUK3RMqfqHW2vIIb7cOje4Orf5sUQ8IfSl4IRgDvpyUkx1Xeys_arswoaGYQz46b_QAi88G_PbO3qpvosh4Qaj07R9EzhyT4_jeUMyl5aiZ_zuZ8kThS3Yc2E5dTQmzqzm9HXNloqU3EZSW3EXGylsDYRT158Jor2V_dqEhMVaIJL6iw7mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی فدراسیون فوتبال: سفر ایران با هواپیمای اختصاصی ایران‌ایر به جام جهانی تقریباً قطعی شده است.
@Sportfars</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/farsna/437289" target="_blank">📅 22:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437288">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad727676c5.mp4?token=vtaq-eEPluewCVpyClx-K3IeRz6qBbsToUdArnlJZFgVewnURyxbc1h_FAUtxWrP_Idajq6Coj5woK8_zNoqn0-w__riXc0DzRVSaUeIRngqILuWcdhkrXvznBVTvXE3QLa-_UUlFPmxL534i9sR4ahUu-qZ9crslYHoJG7hUTB5ok345VRXGiNGZYbp7xZhpduBRDYnGaVVyMqfBamH4GvdZ5VFWbbES4KKvUrl8W6nmAHECTgE8bLkSUX2SHQU38geb4VhYz4e-Dbw2sp2Y_ore1mkFTLawgSmEhbUOAs3-ffulp8snJDGNAMBlAEQ0zw2BqOBeoF9QWiGcmYwbT-devD5tszLcosLIWlENb8pQ6QiPbJ7kb8nbBvegYWXcax2cqQopbHEEH124h3YKI7NoI7opKfbxU2F4vyhnLRHPZvyM2I41mNoDRzIsdDo7age4hn0b1FosbRmwwxdHjYrKkQejnBRx70IRSEGzurubsSK0F4PTFiH6m1vMMbnK5e7Lv2BBpuZ5WiescKycIwlxeFWX9tPHFC3KhlHbO-rr00uqfOx2D22nHL_NuEvaKAHfYrKSGSut24gIQ6Tz6BTAhHWADqEcVvDhBA7ZCDlfrysFb6ZEVDfdRJMszy-8duv38DPvYP2TzMQEKxupk4bKfYMK25oP_85W9KnbKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad727676c5.mp4?token=vtaq-eEPluewCVpyClx-K3IeRz6qBbsToUdArnlJZFgVewnURyxbc1h_FAUtxWrP_Idajq6Coj5woK8_zNoqn0-w__riXc0DzRVSaUeIRngqILuWcdhkrXvznBVTvXE3QLa-_UUlFPmxL534i9sR4ahUu-qZ9crslYHoJG7hUTB5ok345VRXGiNGZYbp7xZhpduBRDYnGaVVyMqfBamH4GvdZ5VFWbbES4KKvUrl8W6nmAHECTgE8bLkSUX2SHQU38geb4VhYz4e-Dbw2sp2Y_ore1mkFTLawgSmEhbUOAs3-ffulp8snJDGNAMBlAEQ0zw2BqOBeoF9QWiGcmYwbT-devD5tszLcosLIWlENb8pQ6QiPbJ7kb8nbBvegYWXcax2cqQopbHEEH124h3YKI7NoI7opKfbxU2F4vyhnLRHPZvyM2I41mNoDRzIsdDo7age4hn0b1FosbRmwwxdHjYrKkQejnBRx70IRSEGzurubsSK0F4PTFiH6m1vMMbnK5e7Lv2BBpuZ5WiescKycIwlxeFWX9tPHFC3KhlHbO-rr00uqfOx2D22nHL_NuEvaKAHfYrKSGSut24gIQ6Tz6BTAhHWADqEcVvDhBA7ZCDlfrysFb6ZEVDfdRJMszy-8duv38DPvYP2TzMQEKxupk4bKfYMK25oP_85W9KnbKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجرای متفاوت در تجمعات شبانه مشهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/437288" target="_blank">📅 22:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437287">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ab312ad2.mp4?token=g61ss13hi8KW0d9kFPoqYJGBoCECPYSsZO4NfSIqYwdagdPme0itvUYKjzZ6Ffn3ANFRBQUaClrx0V4rKs3shik6ccgVKQ5mqnZGi84bcyZ5YcpWd1LP7xox58_ejN9zgtRdc9rXiSwKGUYRmWQPxsGrCWzVRWHOHEfxQEFmV23IZYKaqentGW3yRf2bxrwtAtn7XUowgbnT_M5DCvFkbX050sePnN8E0DQqd5WzUdlTIyF4lJkkhELO6YEkfZX3oFgAI6GKB2UilzIYZpozpKWIn_gRxoJgx7hX549a3bkr473gsTpAgQMaHKiXePpok45uSNCskbAIR4p4GXe3JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ab312ad2.mp4?token=g61ss13hi8KW0d9kFPoqYJGBoCECPYSsZO4NfSIqYwdagdPme0itvUYKjzZ6Ffn3ANFRBQUaClrx0V4rKs3shik6ccgVKQ5mqnZGi84bcyZ5YcpWd1LP7xox58_ejN9zgtRdc9rXiSwKGUYRmWQPxsGrCWzVRWHOHEfxQEFmV23IZYKaqentGW3yRf2bxrwtAtn7XUowgbnT_M5DCvFkbX050sePnN8E0DQqd5WzUdlTIyF4lJkkhELO6YEkfZX3oFgAI6GKB2UilzIYZpozpKWIn_gRxoJgx7hX549a3bkr473gsTpAgQMaHKiXePpok45uSNCskbAIR4p4GXe3JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال کم‌نظیر مردم عراق از «محفل القائد المعظم»، یادبود رهبر شهید انقلاب در میدان التحریر بغداد
@Farsna</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/437287" target="_blank">📅 22:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437286">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791d9999f.mp4?token=JRamccXlN2ssVJn6SQAmMEuUVTsth5w7XeXP2pnYFlNPZeMA8V6SRQ45-mZB6irjjIVRPo-Nibj8NFxpvj_cvrwgYffObpcDk8FiY7HhupbzJS_BXBQ1TYTT-cQSGsffccmMkKzqu-C4WlaUGQWW3ui0s0psWb8xr5u2kvXM0V--NfPCzx1IMWNlJ6iASwbGAFLMT65KIp83vc2i_nUzfzekt-ygv0ZtXaHmVFhfyO6M3zmSgalXtIIezFus4z8ug7hUyhlEhAbQxhridML5AdgSnJ8dc8WBqCwjH6E_xU3rgXlwbjYWhUM2mvoMqSf4vkFqFLvfdjJinJIV233a4B6HO7I0wnTVNF5MehOObPAEiLdq_CXhxjZomQPSXp3YijiIxgRpirzkjUf1WtsG4-4J5JFJhPD9j08l793q18XURVG9u2WonlkJo0249FjZY0Jsm8xNN-1fW98BqETP2gFXlJ4qSkuZ6eM2E0LMuOSbvEyGjYKYAeGGGfHP9hUAO_fLhRul7FvvEjq2UB9-X-sZgVci0VArsqKqfsHh60GCihTEeR4yjj3SPVUk6uTeCqesCyB7Ne3MQfoTO9XqOeAlvWo6EcYnbHbgucCF_Bw--syCzj0kbecQAM2i1_5HiFDZmUi8hWQa5uU9FgXR6hzwwqb0CF7VFMUguXNrkBY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791d9999f.mp4?token=JRamccXlN2ssVJn6SQAmMEuUVTsth5w7XeXP2pnYFlNPZeMA8V6SRQ45-mZB6irjjIVRPo-Nibj8NFxpvj_cvrwgYffObpcDk8FiY7HhupbzJS_BXBQ1TYTT-cQSGsffccmMkKzqu-C4WlaUGQWW3ui0s0psWb8xr5u2kvXM0V--NfPCzx1IMWNlJ6iASwbGAFLMT65KIp83vc2i_nUzfzekt-ygv0ZtXaHmVFhfyO6M3zmSgalXtIIezFus4z8ug7hUyhlEhAbQxhridML5AdgSnJ8dc8WBqCwjH6E_xU3rgXlwbjYWhUM2mvoMqSf4vkFqFLvfdjJinJIV233a4B6HO7I0wnTVNF5MehOObPAEiLdq_CXhxjZomQPSXp3YijiIxgRpirzkjUf1WtsG4-4J5JFJhPD9j08l793q18XURVG9u2WonlkJo0249FjZY0Jsm8xNN-1fW98BqETP2gFXlJ4qSkuZ6eM2E0LMuOSbvEyGjYKYAeGGGfHP9hUAO_fLhRul7FvvEjq2UB9-X-sZgVci0VArsqKqfsHh60GCihTEeR4yjj3SPVUk6uTeCqesCyB7Ne3MQfoTO9XqOeAlvWo6EcYnbHbgucCF_Bw--syCzj0kbecQAM2i1_5HiFDZmUi8hWQa5uU9FgXR6hzwwqb0CF7VFMUguXNrkBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در ۸۰ روز اخیر پلیس بیش از ۴۰ هزار تخلف مربوط به مخدوش‌کردن پلاک خودرو را ثبت کرده است
@Farsna</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/437286" target="_blank">📅 22:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437285">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c32ab1459.mp4?token=IyAo10KVrzUioqnJvLb2fFT98LHb225iYgW7GwfrRxD2PL8DMp4jxT8-EWd_Qax433tqm8NSCknyz3g9VANaGs999M4klIMfaIVvzlaiAxbV02hlyqRqflmpVRLULfdONtNCywXxlVhpbtb2Km2GUt6R9vydtsXV8WWLU0nVpvnuShMnwjTF8PFj1h6RXWv2JMgtpHzR5Me6mj38qVkdZLRcij4s5mFi9S8VpY0MfgGdCd_8v-2i4FvWoyEzkEjNRz88pEmiXA7M44GX8QKjnFaCKWdHh4SlhwdpJTnH4y69wHHHVp3sCq3yGrllrixEge4VsC0_QxQpuiEcmY_v0b2B1ciK_iBxrpIj1BXjq61v4nnquyvtiPnJbmmPCSUUc46qhfkGfMEYQrtV7NKFIX2zYb1seYG8rdUOqMl2LeGp1JujHKUnPWrPqKjSQ3oPMq6ArIkHpCMdwWe7pjMT8BX_Zz9m-9daPtRW5OdHGDTrazI-H66VPzLnBdDSmhLPpB5R4izquTrmeFPwS1fMATyPfBq2DZu0bSq4sZS80Ugsu1SL2k59HCueLv0X-csMQMnxqyLwB67vm8dtJBo--_C4Fvjc0KaushvnkJtYbiqKsyGed2Ejzcroyjw7HpYuTMqS9C99TPwtlQjPEgLERpkZ-c8IPzDJP3UW7Z1wlZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c32ab1459.mp4?token=IyAo10KVrzUioqnJvLb2fFT98LHb225iYgW7GwfrRxD2PL8DMp4jxT8-EWd_Qax433tqm8NSCknyz3g9VANaGs999M4klIMfaIVvzlaiAxbV02hlyqRqflmpVRLULfdONtNCywXxlVhpbtb2Km2GUt6R9vydtsXV8WWLU0nVpvnuShMnwjTF8PFj1h6RXWv2JMgtpHzR5Me6mj38qVkdZLRcij4s5mFi9S8VpY0MfgGdCd_8v-2i4FvWoyEzkEjNRz88pEmiXA7M44GX8QKjnFaCKWdHh4SlhwdpJTnH4y69wHHHVp3sCq3yGrllrixEge4VsC0_QxQpuiEcmY_v0b2B1ciK_iBxrpIj1BXjq61v4nnquyvtiPnJbmmPCSUUc46qhfkGfMEYQrtV7NKFIX2zYb1seYG8rdUOqMl2LeGp1JujHKUnPWrPqKjSQ3oPMq6ArIkHpCMdwWe7pjMT8BX_Zz9m-9daPtRW5OdHGDTrazI-H66VPzLnBdDSmhLPpB5R4izquTrmeFPwS1fMATyPfBq2DZu0bSq4sZS80Ugsu1SL2k59HCueLv0X-csMQMnxqyLwB67vm8dtJBo--_C4Fvjc0KaushvnkJtYbiqKsyGed2Ejzcroyjw7HpYuTMqS9C99TPwtlQjPEgLERpkZ-c8IPzDJP3UW7Z1wlZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جاوید ایران
🔹
شعار هماهنگ نیشابوری‌ها در شب ۸۳ تجمعات مردمی.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/437285" target="_blank">📅 22:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437284">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d3480c7a.mp4?token=FfsHPRL-K6TDHGxWW-_iRUNe1Yk2VAoFULW1cbCVfJjVPr5ZahZqy3qYbQVqF0wGwQeev--P5DFRRdu2kfwooiedMUbe-trkdyRw2lg6Xrb1My6JySSg_jFbsi9eDWBoGHmx5PR2Q2j9Wb96RXm8sSDFqPeRk-eJQZl4V_5M3zNUKLUUHQOWkjW7VQO6czj8o47BYPSjfoSJoPBXHy5iDJmoQif2kB42iJC63xx6f-90pa6IbRDI2H80nVy6DzNXGZV8npNiZB7iIGax_PnP4wOofiPipBBhmt8jVloF5HWV_OGD0g5eb8glhKDHosTDukGhTFlJUtssO8CQvvM6H7cwmy7Q6v_kLYf_00Ys-TTvLz1NdmCFU3zGyqT9nI4o9p5YUHpYKcMesrWnQGUGLdrhe69r1ZptEXn8uKZ8CsHaezoHPF4PBNaLk3ztKakdGFgFPwRjnCcL_iqIQscu71Wul6mh88zJmADUU49jGQNnq7q5I_mVZ4vLISyENVQWoBMJaDcAIDIqr2zoPpBCPPJAb9r_KetYIN6c5Mr2rUmqLor5iBVO4r19uOgmE2u_J5Dl5E7w8KKoPK49cmRysDR7g4vTlpNBPJ-KuJK5gRMLL51nIDAwcANh44pNuyWqfUmy30jEGMqxMFGeGyKA_PK9_fajstQNOpKj04PazWU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d3480c7a.mp4?token=FfsHPRL-K6TDHGxWW-_iRUNe1Yk2VAoFULW1cbCVfJjVPr5ZahZqy3qYbQVqF0wGwQeev--P5DFRRdu2kfwooiedMUbe-trkdyRw2lg6Xrb1My6JySSg_jFbsi9eDWBoGHmx5PR2Q2j9Wb96RXm8sSDFqPeRk-eJQZl4V_5M3zNUKLUUHQOWkjW7VQO6czj8o47BYPSjfoSJoPBXHy5iDJmoQif2kB42iJC63xx6f-90pa6IbRDI2H80nVy6DzNXGZV8npNiZB7iIGax_PnP4wOofiPipBBhmt8jVloF5HWV_OGD0g5eb8glhKDHosTDukGhTFlJUtssO8CQvvM6H7cwmy7Q6v_kLYf_00Ys-TTvLz1NdmCFU3zGyqT9nI4o9p5YUHpYKcMesrWnQGUGLdrhe69r1ZptEXn8uKZ8CsHaezoHPF4PBNaLk3ztKakdGFgFPwRjnCcL_iqIQscu71Wul6mh88zJmADUU49jGQNnq7q5I_mVZ4vLISyENVQWoBMJaDcAIDIqr2zoPpBCPPJAb9r_KetYIN6c5Mr2rUmqLor5iBVO4r19uOgmE2u_J5Dl5E7w8KKoPK49cmRysDR7g4vTlpNBPJ-KuJK5gRMLL51nIDAwcANh44pNuyWqfUmy30jEGMqxMFGeGyKA_PK9_fajstQNOpKj04PazWU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه پاسداران: با تکرار تجاوز دشمن، جنگ را فرامنطقه‌ای می‌کنیم
🔹
بیانیه سپاه پاسداران: دشمن آمریکایی‌صهیونی که از شکست‌های بزرگ و راهبردی مکرر از انقلاب اسلامی درس نگرفته و بار دیگر زبان به تهدید گشوده بداند، اگرچه آنها با تمام توانایی‌های دو ارتش که پرهزینه‌ترین…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/437284" target="_blank">📅 22:12 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437283">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDBPRtaxVueS-QrGWW8WT8h9_CoAAuwIGO_hZnQs7ZK8AeeIbTzdrCGUG6547ESgTmnyXtT7jgf-fpqZlJrGnD8kZXTc0k_8RVLG6Z36FyyLbLFDqsFxd_hH1jKKixKLFONHL5D0_Tqs41mNrwKP8ZgWfOlAHqtluolyoHcK7dieFbWmTtulGKOMHEuz6Hogoz7KbbZlVWckYziNnY_72YHwbpi8PmSKDZSqqzPKdjUrDTIQIrPyh_ds12GcipS4mh-ESCoUpMiyF6C233ROrAUP-CZ-8mKqGUZObiihSaV3oeaJXDtW08Ays8lPknXMVun0is5udC7-TY36CZh1IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محاصره دریایی هم قفل ۲۰ ساله بنادر شمالی را باز نکرد
🔹
درحالی‌که ترانزیت از سواحل جنوبی زیر ذره‌بین محاصره دریایی ترامپ است، بنادر شمالی ایران ظرفیت واردات ۳۰ میلیون تن کالای اساسی را دارند.
🔹
بااین‌وجود اما پروژه اسکله رو-رو امیرآباد برای کاهش ۵۰ درصدی زمان ترانزیت، پس از ۲۰ سال همچنان در وعده‌ها گرفتار مانده است.
🔹
اسکله‌ای که اگر ساخته می‌شد، امروز کامیون‌ها و قطارهای حامل کالاهای اساسی می‌توانستند بدون تخلیه بار، مستقیم از روسیه یا قزاقستان وارد خاک ایران شوند.
🔹
کارشناسان تأکید دارند که اگر وعده ۲۰ ساله اسکله رو-رو باز هم در پیچ ادارات گم شود، نه تنها فرصت طلایی کریدور شمال-جنوب از دست می‌رود، بلکه ایران بار دیگر به مسیرهای محدود و وابسته به همسایگان شرقی و غربی خزر محکوم خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/437283" target="_blank">📅 22:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437282">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jw-HOgSwS4UTAAnTIiH3211GeM626cstTOYmyOVr7rIfwCgIGhGxkncI1GMXtOhp9g-txYpbkC4D_9XoUiD0Jz9L1vWg-Oa1RglqupFcblM49HD3NNL1ZLJKK2Rvj_AMpNiLAv9XrFKfH3qA717VW32Ilq9ByQx70kn4bjVIURqDIDYoM6xVePQMfkoWUPC6uKYWiNoEysLgaELaWpbVS2GGIKh3vvWkt17w1mrXUj5_Kxhw2BDCj9EfJIPz8P4kqOqLhCfs9c4Yj4RnBwojVvh9W2IkeBc4dgjNzDYrQno5dvWSnsE2J2Nx-isGnujjbYwYeMwNMg-RfURCvrbMBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیر اطلاعات ملی آمریکا استعفا داد
🔹
فاکس‌نیوز: تولسی گابارد، مدیر  اطلاعات ملی آمریکا از سمت خود استعفا کرد. @Farsna</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/437282" target="_blank">📅 21:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437281">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: یک هیئت قطری امروز به ایران آمد و مذاکراتی با وزیر خارجه داشت
🔹
کشورهای مختلف برای جلوگیری از تشدید تنش‌ها تلاش می‌کنند اما میانجی رسمی مذاکرات، همچنان پاکستان است. @Farsna</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/437281" target="_blank">📅 21:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437280">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: در مورد مباحث هسته‌ای تکلیف خیلی روشن است؛ ما عضو NPT هستیم و حق داریم از انرژی هسته‌ای برای مقاصد صلح‌آمیز استفاده کنیم. @Farsna</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/437280" target="_blank">📅 21:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437279">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: فعلا فقط تمرکز ما روی خاتمهٔ جنگ است
🔹
در شرایط کنونی ما باید ابتدا با مختصاتی نگرانی‌ها و منافع‌ ما را تامین می‌کند به خاتمهٔ جنگ برسیم؛ اینکه در مرحلهٔ بعد در مورد سایر موضوعات صحبت نکنیم یا نکنیم بحث دیگری است. @Farsna</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/farsna/437279" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437278">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: موضوعاتی مثل «خاتمهٔ جنگ در تمام جبهه‌ها، وضعیت تنگهٔ هرمز و خاتمهٔ راهزنی دریایی آمریکا» همچنان محل بحث است. @Farsna</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/437278" target="_blank">📅 21:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437277">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6HmGqlauDFXmEv5jxc2fa6B_t1znCz9CIHtqEJTvHTPTdg_6WITK2Ij0eQoqFVFyTKca35QBKKUhwyq_EdGIRDp0JPPsNCxP_yrCMPS_y9GQmfG4gTYTZVuNHELZmPPi3gf_VmAjp2gb7tXdPFaE9eH8vf_gk0PmJrGKIGe4L5sEZtBVzgazzXASmJZfgbglRSBfTAdoZbrYPNB_qv-zid6gk33NgxkDudhjNumgHxoeW2EO4uWWl_ZfdqaLlo72oEbYfDv_7Xb5vPiPonkaApC4JqQy3nTkLRAe4zLLhjbzr83jEornGNrfmOosBB7fcip3HVPKD3fZzr-aD3z7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیر اطلاعات ملی آمریکا استعفا داد
🔹
فاکس‌نیوز: تولسی گابارد، مدیر  اطلاعات ملی آمریکا از سمت خود استعفا کرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/farsna/437277" target="_blank">📅 21:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437276">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: تمرکز این مذاکرات بر خاتمهٔ جنگ است و در این مرحله قرار نیست راجع‌‌ به مباحث مرتبط با موضوعات هسته‌ای بحث شود. @Farsna</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/437276" target="_blank">📅 20:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437275">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم. @Farsna</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/437275" target="_blank">📅 20:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437274">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: نمی‌توانیم بگوییم که به‌جایی رسیده‌ایم که توافق نزدیک است؛ خیر این‌گونه نیست. @Farsna</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/437274" target="_blank">📅 20:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437273">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: سفر فرمانده ارتش پاکستان ادامهٔ روند دیپلماتیک است و نمی‌شود گفت که ضرورتا به این معناست که ما به یک نقطهٔ عطف یا وضعیت تعیین‌کننده رسیده‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/437273" target="_blank">📅 20:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437272">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فرمانده ارتش پاکستان وارد تهران شد
🔹
عاصم منیر، فرمانده ارتش پاکستان با استقبال اسکندر مومنی، وزیر کشور وارد تهران شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/farsna/437272" target="_blank">📅 20:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437265">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ci7usPDAwLjd7gEzpjzTcZOFu8uzTZEbPcTqudsjaD2b7TKvErQwUMq56mm5e7jcCp1eI_qXcqCBBFZGV-FtF2qvqbvTBrpMGEMksI4XSXVKZGKI_UsoiSTZ0C1l6Bgrozhm7xsYg614hbQvqBF18RrdHdp3OAfEBbttEcbZCmQ6EOP7JmxehJRY9HFEhTGeHenQRe2VntNjZH_RDHuFkOOFdkDCHyaEdPoUTBY6zm4ESDvWSRbtGDA1uFO72c8qiqWhUy7ad_D1fRkTbXu8VIMapLZcWCtY_MC6hkb-zdR-uYw1wQ21Ix_nH6kFUdlKtBZEM-KbPUcsMGiStW5eXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eeBetZzuyEuVZb4UBScjUyJh33uy5hN8djBIVa3wVAtXMhSpXyk2h0MuasRR3TdvDAZ95FY8kwuqJInuIwpWzisU7UlKcyZl0jYhc81VeY6ZgfTfFz_nGDZ1wh4w1E_KOpUC7hYpvTtSipxhIWt-edMoU-g2ekmmN6tsp8uM5E9DEs5d-YLV9buAUqdgbQp_mz3M2O7alvHpR5BjXgjkJTiufhyZrZhEa7oDxR-wEivRd6llGenjUTJZBVDuvYw-y2BK8_Ovp_397zo94CND-WCcl8Z1lANKJlsKKDbRLe2v4fZkFiPoTYJK4h9lJP6yfEA2E3zlQOMDiTQ58c8iOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZrgneKfDy2WdpOGG8ToOyR1UEjbr0LZNfFDi4BGYwqSCGV2AXcOlzi0X0zfxsFaCRTU4P5F9nWfjSnhtOx6XTMvTzGR_pzaPlL81TejVwtugLECm4GYYQLoh9gNHxmKZIdRbePh76cdz4rVFxmNcs5DH3iyaxGpvBDI2cpWNbGM91LWk3yrvKaNV2u83n89_ECMmYPewDRA1PHr9U3aSh82gwMYAjsSdqMKTr62zivdl3nA-M1nb9AmydXILTSO8Y10NA5Nf2OgTw1JVpTj0DXKpTXnBCgg2PS_l_wfd2VkWhmvL24x14P2522_LnnXUZ-OGpuirIjFe5J_dHGbFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vTjUTeLsXVUajY_z_feHE4LsYR2WEEN3aQyGgY8SsGpt2YD1PABrsljqZ84pAUd3qWQJO2KwPJ4J0mLbkOZfmUo__RzKGdFaJoxtfvbUJAvteULX5m9OvK3gkoaXw0TwW4GYfbsz98BNKuL0YLeGe4wO6-aGcBocksNFKsXYcr9cGQPd8H601aJ7cnCiCx_ZCBTx8XFbYdZhQ_CS_zfEu3Y_PkjSNs7V7t8zbnHEjKNTFLgyvWdKVvcAnClASwiYsSf--MOaAG3hFqram4IN5m0_VDtaWQyRKJ9X83zJyXkEtlriFj9sy0mft1Ky12Zg1R1-mqH193NQC6F2QjugDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SotXNwXsvJyFJGUcnZz5OMZWzC36svceF5kol8IqN0_1wL_9YvobRcK_K3ghtnuXgnWUmbSarg9L67LYuqUJBfL2-uYw8mjzD4CRhFPcmnG7H5z4Nt44F1NgGBgsPmYp7njNbPkQjkYGT4BA3mKPKx4pOo7dgvJUd3K3iH4U0LpxbqPDQGY2AQkYjuWqOkTHTblEjVwg9z5sDhzBqpB4J5Ek2ipg7Rrg0oFmdTmcXngf1CF0JisaXEnuVCQWJ9ByQ4Wph23A25cWQ351J3hg352m9EGb8C7aSGjqgUkKTWczosZrIU_Zo0he1FQVge6BnFjleVJBWDF2-F6NY-ljCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLG3ZR8s0QqM3oB4TejHJk4aqc_6nrb_JgVhudjpiZm0LTZrGMfXo1AIpIYNgsx9actT6uCKvEUhuOAZiN2SZ9XkgGz-YGzMmqKdvEiwB9vhp9qpNTzy-B03HVPjsTGA9J6Pr9X7zbs0MMdcF_2JLp-LJ78dj6QUufAtwyiJGxZ0COV5oNbFbioUjsczm5F9v6BfFbbk3CXPTNkvMhZcVucANSJvG1mqwcSJxpRm2ka791s_Ka2lJdfRhLEIHLjqG5CsZ3Adbb33ZR6u-mpeoMg8LfYdjINv0RrThUrv9d2xT53L9vrPKLT_5QgBQOSwXT9aHvOPjsKKEhv6hA_R2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xnh6b1zQ3Wd78ElwBNwEp5vANgYBOk0Q2_cIlauLn1X0v-I31T52uaYImzX_0XhggHIagEtiJgBwCfRUhjiEE0HHooZIH3JfvHyog0Bqejhgn-TWymLLbYYW7sdVItewmwH1yItMaHifN7o8ROt_P7KL5EzqS9_otxVDiwOZsda7QhWYACD5TDf6pe8ip2U29-WmVaLjK1s6F7SGlp-nnyjBWbnnCh0onOmFZNeZ9AdOK6xnzCf5kIxCd562hl6W0u3m5tx6IkUI4NGW130JOvLMudhWgwcgl-KIzqXJ1N02J8h7UsL-tjT_2jJRcYVS3vzr9I1H0A1i1r50WMHc0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سردار عباسعلی فرزندی به یاران شهیدش پیوست
🔹
سردار عباسعلی فرزندی، رئیس پیشین دانشگاه عالی دفاع ملی امروز به‌علت بیماری و جراحات ناشی از ۸ سال دفاع مقدس دعوت حق را لبیک گفت. @Farsna</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/437265" target="_blank">📅 20:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437264">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993985f526.mp4?token=NlRUJaD5GDd96o1PriZMzper5-d_TAvqPdLf2Z80ZR5_V5666CZY49YyfDBXH-kThFfX5LLO1NZGdYLd3QhwvgA5uGGLwAHIaikFDmMKEKRMdvebJFs3DSMw6tBJWHICyJBzpwmZjt8MbY9pzaiWELKOap0VreU2vWybYhGVpz2xcQwAezaTQ09G1CKD6aXWVMHa1J9B5n2eZ9SOuHUBxAy6o9q0Y0dtksqa61FUyIuuTPXTJlAbAjBQrAAAllazcRG7CAP8yzZ9LIVNh83w6x72nguiURP-DvfMWS1dE38lKWX6jbDtCD4t7Mbkx3nZVc8UNScQToE4rapkuEDw1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993985f526.mp4?token=NlRUJaD5GDd96o1PriZMzper5-d_TAvqPdLf2Z80ZR5_V5666CZY49YyfDBXH-kThFfX5LLO1NZGdYLd3QhwvgA5uGGLwAHIaikFDmMKEKRMdvebJFs3DSMw6tBJWHICyJBzpwmZjt8MbY9pzaiWELKOap0VreU2vWybYhGVpz2xcQwAezaTQ09G1CKD6aXWVMHa1J9B5n2eZ9SOuHUBxAy6o9q0Y0dtksqa61FUyIuuTPXTJlAbAjBQrAAAllazcRG7CAP8yzZ9LIVNh83w6x72nguiURP-DvfMWS1dE38lKWX6jbDtCD4t7Mbkx3nZVc8UNScQToE4rapkuEDw1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور گزارشگران و تصویربردار رسانه ITV در محل تمرین امروز تیم ملی
@Sportfars</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farsna/437264" target="_blank">📅 20:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437263">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2hlUxSudmBZjdTUQSETrgi-ev40z6O_TklVjg3BeXmHxZolwFHxZc7daqKUlG9TASS38MxGKiA9EZlJjyBbUU23gFFnWdPGiDMYyMHvnW1ThJphxb6VjAtsVLC-XdZtSkBNIv9sl67vOV2fXS0XxF6XXVcRhi4V64H40_H6J6PT8K0gm4DWSR1yd8TwjvmBON1__tVGuqzN2g54yCzDDmOstkYnTtWgBUs9L-kSBpLUewSQFH16ywojaoEufpPZ4qdNqGHnXYCqeZNxZsT4zwdQ0xI_8PeZNyuFVIAMoGmb8dYyG3-TNcZkxLzR5jPnc23mYZzDx84NHPUIJIvkWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده ارتش پاکستان وارد تهران شد
🔹
عاصم منیر، فرمانده ارتش پاکستان با استقبال اسکندر مومنی، وزیر کشور وارد تهران شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/437263" target="_blank">📅 20:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437256">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N23x3ULqtIF35A0l8WnBSKsG-C77XaSjOAbos8o3UA-9eQHaFpxhB7eZPoRLE7c8XGb47uubNwOeIBOZy0M4w_c8RvCU4tzo27U1GTfnk-j2BiOYFpFt8dIY7mtkaHQIv_e6hMYLmk3ROq-2zFoK3mBmzs9Bf0n2yfGScjMQsxjEap4tGrs0hrDA0xNM84ZiWdInCUSWASY8DpzQrTa7wHU9du2EHJ4qLdDrbW0ENI-me36Jq_Z9PyOAgq0vyW4ufHZjmd3p990AApDv-tg0zyLi9eWUm9tOUG8IJed8RocLdpQhDOqXUKzmnuXDjBjky_TXhB1f1mKQfSTXquzvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tsvr5KVGGn3Dx_3ggoAeMCQLSdZKjDENiJDwjsLhbJRjtwttmO5yVUs61J1i6NiAHPtsRacsCFv1xLzQ4QuueUtjLlmaGuMNY1h7v2ZXSwRV0PuJoS05dXlUk8Ox5OF--yaZdceyhR_UYjba233bmkDCE8vQjo-EaPDWyenCnBf_uYQGjTK5ujxmBC37EMLdOMI_RilYwYwdh0MXJa1gCahHY1lU7hivw1rmi5OtzX8Zw4h5ogRXewCUHzvQjPZgA7GC7TvltVDLyr3NDA9NS75fVuzzPYBKhdzYI3d-4E_IIWvLGfXUx1M4ZqU64JHRT1RHfzVyhe6XAj50bhk5Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G69j4Os5ejNAGQzA5YMl2X0_hHlTxQoZkXg0r6iyHZaF51S6Y02AyM3YAobkgdqaOymwd1ST_KXK-5LqnX2vnfAFSo4BOiCbbL867GIG40-s9QGvkZ1lc0qe53QKLtzZCdBVSEyYEeEC7FIRzX4CyDHzAMmlZCaKr1NDA8ILWanTRYrcLCZokVaNVpZF-BkHgUz6FvHu0whHIqeJdL0txbYlXosOhAO5f-deaSMU9uVARVm7nIAXuG4V3UivTWGPhbLiMMOCaF-ZKx_HLdsipyQsX93oeYkVjf3ybHvN6xJwGhYGPshtunn990VJFGBwn4q_29elM5805FUtiUTa4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TT6zNjg_rZakp1M4XGY8cLqGejOReb4GnFHyH4A_WVFlvud-aa21jkI4eOIMYrqEeTu07ACHFDSpfdaHkuSA2HT7ITTHFjR4okZkh1loyIXCjETAQzVqHMx52j6wV3_N5CRB5_e0nPdd6nngcUBYaqoWKt_midfKMEsGdCvjciBlUZoyETiRSgIsrXRxk85lULdQPmTP3g7eTX9KYTddbLxgMLkthI63zw6u1BtA2bj_RG-sVfIZgUjy8TCrpfiLwOSYWua3WxSidr4iqDq8-4DEV0az16WHVAK3uX2EXPRWuG43By4Q6QzGhOgsg8obH7nHn3vcPf_EiHTzSsp8nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J2kkyKrhaqlgZq6GCwrhBSw2Ym0Rui078BB-FHVHPJJNthJSgDgQzbvR7iy8OyE76Y07wU-rrWtskmGT1Ui4FU902xj_XeMpy_MdUz3xNwYha7DLiSfKtrT0f3vkZOqZgDNKjOflb--347PDRdvMi9vLwP87QWK7OUso_HcwRjCTbHIi2jNqLZ7tMyNFtDxnWuz7jz3URBwmyb5zGDMmxwnJ0vne3g62XdbIRyuPfF7ST5RZYwE5DnuExoQX8q0L1QhLscWytcRtjd97UWVnH6caKiuLEyA3PFdgQpTognL52XT_YsVrLmdr0tRsZ-6eD8ZEkKgXQaiHqFBUmVzszA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMtUAnGZTBrDK68EbWE9VGzWftjlXtxmFx_9oj7ESz_6l3y9hdRoX9gb4LN1jFIL0ocq8HP2x4mJ3qosavKTgG7OmYWlumfyOZpp08y2KbpU6Mn9porEVhptwWtbb2uurxnAI6X4XkAGW9_RD2vjs-PpLjRIspOZ_K59TWnlPgsGiL_uZKVTGyoJ63MNZW9DvrJYN3l9HF6IPJb71hJp_P2a378jjdRaX6HwIp0UbkQyZBwDWL7-4VfWniRR0kkLfX_bdo4ucYA8-z9mNLX6Qn5a_UBYI5unehat1YxhSP4tM14zER0dZSXZdr7xZgME_Xdqr1xYOmeh34NO6IviBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N23x3ULqtIF35A0l8WnBSKsG-C77XaSjOAbos8o3UA-9eQHaFpxhB7eZPoRLE7c8XGb47uubNwOeIBOZy0M4w_c8RvCU4tzo27U1GTfnk-j2BiOYFpFt8dIY7mtkaHQIv_e6hMYLmk3ROq-2zFoK3mBmzs9Bf0n2yfGScjMQsxjEap4tGrs0hrDA0xNM84ZiWdInCUSWASY8DpzQrTa7wHU9du2EHJ4qLdDrbW0ENI-me36Jq_Z9PyOAgq0vyW4ufHZjmd3p990AApDv-tg0zyLi9eWUm9tOUG8IJed8RocLdpQhDOqXUKzmnuXDjBjky_TXhB1f1mKQfSTXquzvsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گل‌های شقایق بهاری در همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/437256" target="_blank">📅 20:12 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437255">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW1fdOMZfiLY_JzazaVMf7Kb4bhYUsCxxIDgI6udheg0Rj5znbRUB5VnjS3h_iHJ72V5-0VEDnSd5plY9ra3PjQaKmDzBOuJ8kVC-nry95CRWDnBmDqR6_TExr3sAkIfb8s6KVOF2XXSFw21NIZQmntIFu15W76r3EwAe-mwQ0gm1uYhNdhp183hc5UlZhH6k-JAu_SbJo0TbM-GqqQ4aVW1MX-MjAg_KV0hl1Z6gHlGLeLPhzD_KPVu-ITNUuvT57rjEMczhzsRwwNVxfGElPNyGcvVuDanPLIYeZDNY3d43P-lw9FMK_xS8ysGBr7FgphHKkoj5V4tyg4t7LVuFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: امارات از جنگ‌‌طلبی علیه ایران منصرف شد
🔹
رسانۀ آمریکایی بلومبرگ: دولت امارات در روزهای اخیر تلاش‌های فشرده‌تری را برای پایان‌دادن به جنگ علیه ایران آغاز کرده و با پیوستن به عربستان و قطر، از ترامپ خواسته تا به مذاکرات دیپلماتیک فرصت دهد.
🔹
موضع ابوظبی نشان‌دهنده چرخش در موضع کشوری است که همواره رویکردی جنگ‌طلبانه‌تر نسبت به ایران داشته اما بیش از همسایگان خود از حملات ایران آسیب دیده.
🔹
اگرچه امارات، عربستان و قطر در خصوص نوع توافق با ایران با یک‌دیگر اختلاف‌نظر دارند، اما هراس همه‌جانبه آن‌ها از تکرار وضعیت بحرانی دوران جنگ مشترک است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/437255" target="_blank">📅 19:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437253">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTYKgk9xrz2MFszw4vrYFklcPZCOYhgTZUcWFgEgwqhRMDYaPmkorIJfCVKH4Xt7xPL-PnjbwQbmvK09hGQ1bsT6BLS8kXHnTXqJkbTRAh6Kt0l5kSGlX4ffj6ojVhSWpIykorSyfWuyu6YVqEBNjlegvhey-36KCH67dCl5nNZFfFXfVJUdQLePQllwxKJgcFfVIDkmSlHsAr3bdEKsqTPYFCie-AO3FQdhKumFruMwAz-Wjv43sjdILehS5AuRbrr_rLmHsqC8vSxtun9_YW8-PL9rfuSkTvnFzU9NxiMIhUV0K5XNfqrZjD4e4hAfHVsTIwHjcgm7MwfJu-gIhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تگزاس امنیت واتساپ را زیر سؤال برد
🔹
دادستان ایالت تگزاس آمریکا از پیام‌رسان واتساپ و مالک آن یعنی شرکت متا، به‌ اتهام نقض حریم خصوصی شکایت کرد.
🔹
دادستان تگزاس گفته: ه واتساپ به دروغ به کاربران اطمینان می‌دهد که پیام‌ها رمزگذاری‌شده و امن هستند اما مسئولین واتساپ به ارتباطات خصوصی کاربران دسترسی دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/437253" target="_blank">📅 19:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437250">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GUqFRp_6LmWfTOjbGgoW2Pq_N2AUZKFpgN6Sp6PpTzOpIW0YQ2FYG4Me3TzEB5wbZ0x2m-YG38t72Wv-T2xMvcRg02uHxx4Q0TpG1dVe3rEwRwfH63Lgq28r1VB8lV1GI4mb-U2PLatiGPF3UsH0kN9O-QvqgeishWGYwUGuIr1nK20CdJiDg9g4xKS3VNOXbtsDD6FsOFt3UBsORL_kqaDP1XY88J68oGnffiKy9GLpY62yiMwypL7elqRnjtT3cURAueroMiU7Khkex9ziBSzbSul4QkQtoR4aV_L8VtAGnJv0GNbbdzXKuFsmxeAFtdmsa6DXTs-pjvMK92jYRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qyFqMdelbEReuMgwyYr_oXbdyTKgF4shBmoPTVaW4HklO5SgvIhFzxtenM1WBjDZDLK8X3NTIUgc0SCEfSlN0yRe1UvSas-og9qiuwTbx9d2059T4D6tT8esxnQkM0UlBmS2BBDQtWLrECiv9Z3SZ0Up8mj602SsYmvHuHPXSPXAHYbd36nWQDRzbcZ8xKQxbLxI_TUIlMYW3W9597UIAXo1rora_VXmr8CiiU6Z5Vs_kqYjrD8hGAQdVO-VBDjhpN1VC9lCF1klLu50hW2NJUvHH1RkQoFz-nW81dOiCoVSCOtzBFqgmmxUfT-9uf8Zc7rzGUlzvO1FynFQNGm89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/erkHWQGutT7gJE7kCOkl0LFS9FIikeiMoPWkcc_BssFoK9x79sCaKH6-FQCTUa6ijj5XVtmuEtEfR46Q4sOr_RV9H0ZLIG0_lpj1Y068uHgTfMbMQsgrQK1l_BiwxCBVhCIbkbj7yAuzdWlLV9FIW7PEiUPsm8WSudDrSO9Qd9yYFC2KC2U4P3idAUmBgalEui7yUdjnV5UAE_YPclL0jLqq0VzpQv1uBkVcW9AG5fHLPNklLV32D98Cz1nV8Sx7jPsxWc3opfVogJK0nKzYW30OJ5yYp_dTmZTuB9vOLGx1_0X5s_3SLrp_1mNeFUpdxLSFsPw6nDnyaPIqT29hGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
حملهٔ وزیر امنیت داخلی رژیم صهیونیستی به اعضای دستگیرشدهٔ ناوگان صمود  @Farsna</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/437250" target="_blank">📅 19:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437249">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🎥
جنایت ترامپ به روایت کهنه‌سرباز آمریکایی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/437249" target="_blank">📅 19:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437248">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/878a398064.mp4?token=jiwM0uqEtbOiFofwiLeSUfvBWlAlPjRZyYrEtmmlHMvu5EF_dJhaGwSlU6S4kGbenUhyiiRIlGgfTkKmJT45yCKFf5RmJnemNY3OOiCwvIfqGymihAhjclaDuJ_LRihJqFAQyw0LDE5h7ccB9FITeFU-gwGrKZq7shVBtEbD58_7RFDULT_HjWamNkArZ2sPrtqe7hL0txDqdPVT5xsP8C89AS84aIdg4_ds3INikp0yWHG2A7zPEFE9l_wYg_ydC7soIJC74dh_UqKE--C8uLHyWp1-la1DTlzhb7xloy_SwuAR46VvnBpd9GxA4xC4txsGwKE7fYC1mSXPxdk7HnB-3asoU6Gts5SAxFBkMQgqGsOEzYP89apBru32IaKPWuGp9vzam9XeHiabe-AcT1NDiPtZvxZ55DZjPYFxH1VTZcHCYjJeM0JDnRf9C8DEljOeB_PCqfLI8PXXjZOvYKc-8U3nj3QWycoptBEv6dG0F0YL0upwtKCbF6smZ9JoEZjtlFytNazZM91BKl6XspS-198maXvm1MFuzWnon6qlCK2bsEoHDAlef72ziC9GJsZJtRFmNdRtLPsKb57TbfHmUdYOPZbL5QLrueHbAuBv06NfBwup9HSLPcXRefqhHyif5AhPgzYELdC2BmGsSSsQSo_gF8nsBCPTkzc1HPU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/878a398064.mp4?token=jiwM0uqEtbOiFofwiLeSUfvBWlAlPjRZyYrEtmmlHMvu5EF_dJhaGwSlU6S4kGbenUhyiiRIlGgfTkKmJT45yCKFf5RmJnemNY3OOiCwvIfqGymihAhjclaDuJ_LRihJqFAQyw0LDE5h7ccB9FITeFU-gwGrKZq7shVBtEbD58_7RFDULT_HjWamNkArZ2sPrtqe7hL0txDqdPVT5xsP8C89AS84aIdg4_ds3INikp0yWHG2A7zPEFE9l_wYg_ydC7soIJC74dh_UqKE--C8uLHyWp1-la1DTlzhb7xloy_SwuAR46VvnBpd9GxA4xC4txsGwKE7fYC1mSXPxdk7HnB-3asoU6Gts5SAxFBkMQgqGsOEzYP89apBru32IaKPWuGp9vzam9XeHiabe-AcT1NDiPtZvxZ55DZjPYFxH1VTZcHCYjJeM0JDnRf9C8DEljOeB_PCqfLI8PXXjZOvYKc-8U3nj3QWycoptBEv6dG0F0YL0upwtKCbF6smZ9JoEZjtlFytNazZM91BKl6XspS-198maXvm1MFuzWnon6qlCK2bsEoHDAlef72ziC9GJsZJtRFmNdRtLPsKb57TbfHmUdYOPZbL5QLrueHbAuBv06NfBwup9HSLPcXRefqhHyif5AhPgzYELdC2BmGsSSsQSo_gF8nsBCPTkzc1HPU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارندگی شدید باعث آب‌گرفتگی خیابان‌‌ها در گرمی اردبیل شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/437248" target="_blank">📅 18:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437247">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
انهدام یک سامانه گنبد آهنین توسط حزب‌الله
🔹
حزب‌الله: یک سامانه گنبد آهنین در پایگاه صهیونیستی برانیت در شمال سرزمین‌های اشغالی را با پهپادهای ابابیل هدف قرار دادیم. @Farsna</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/437247" target="_blank">📅 18:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437246">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎥
حملهٔ پهپادی اوکراین به خوابگاه دانش‌آموزان در لوهانسک
🔹
حملهٔ پهپادی شبانهٔ اوکراین به یک خوابگاه دانش‌آموزی در منطقهٔ لوهانسک دست‌کم ۴ کشته و ۳۵ مجروح برجا گذاشت.
🔹
کمیسر حقوق بشر روسیه، گفت که ۸۶ نوجوان ۱۴ تا ۱۸ ساله در کالج استاروبیلسک دانشگاه تربیت…</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/437246" target="_blank">📅 18:29 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437245">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-43.pdf</div>
  <div class="tg-doc-extra">3 MB</div>
</div>
<a href="https://t.me/farsna/437245" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-42.pdf</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/437245" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437243">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
انهدام یک سامانه گنبد آهنین توسط حزب‌الله
🔹
حزب‌الله: یک سامانه گنبد آهنین در پایگاه صهیونیستی برانیت در شمال سرزمین‌های اشغالی را با پهپادهای ابابیل هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/437243" target="_blank">📅 18:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437236">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mNSLl6U0E-bnvhKLriir0rGih-GFqfz18hhYJ-KWGEZidlAGoDnA9rM1zMttetBJT9Ve8rJ4Bf8MwBvs5dGjk5RqPKWLHVo34xVRfYI-yGoWyz5ZUUEHOWBsd952ZNq9QH9DHVzGtIXknnUbfbTQ6ZRb5SsFMabspINHI4I5Tcxt5etpLppXgU2T1Gu3CfUPIE3E6FR50o9TmGezak9KpEq9fm312-1_uvVKG4TPPZxsmO4h10Hy8cBmc57cNW1nXyfzPZnRSlNMVjFoEGRL4guehSSeTQ4KpkSW37SsWcE1NrE1sF6FZJ-ybEIpraVqQ2XK2nMwNfP4N-kdsK_gOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_EyMolbsJrD6PhooUmR2RgymD6zJ_jEhA193lRC6TZf8ny7HRd37oiTlvFTYc_U4tGRXXhIFfv8q_rO0H2so8OJahjrvCdA0yg4VIB5AcHWjAUg4MJLsg7Qn3ALkSuG3xpFg8ItYN6BrAaVEir9PgQE26IyscKdf5EvpCnmOXkXksBaPN3rZYhv7vK4lNN0nkHVKK8dM6WuiQ6eKKNYa66uOgip8KE89CP4nEemXpiIF0YTS3Bi00QpEFcDWhjuwlIL7Y6_TLlYyqGieYF7CMT9yln4d47XTD_hULoFpOkA6sWztglxyMTIScTqk-pdlyr03_DS2fON695dns-Swg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2_PrUQihw2azAWgUDVCQtuopxR1GGBi0oirLya-Sb_2p9OrMsMxqXx50Yk5MyBY0Y9L6h86s2CxhuvrHeWclIbZhJjr3GZkhlvdtilhfw6KfpSRPQtq10aIvuCVxY7tgt5NakphQuz9Gu4qR8-wuMaTUhlP6dTNMSrvWpTMfuXMOn_sErRJG-mjsugo-8lGzbSmfoWKCnxo-OMS1yqX0-eh9VSmqjAdXz2btVnlUMulUZUkmDUdlfmXKtCml_FuoRGe9ciNPMj88VyrAmDagWo2A1AxAfbjTgVgjdfQocdZJQCaiEYCQpwVhw2LnBWUuZw-ssoy3a3-R9jmhi5EhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XvjGsyfmckytDQokYkHQA7rrBA57BtRNUhv9Fosz6g-Db1qruxEJudsfuWeUiSLc02chB7iadMXMPVfhVKCE4KfJY-xYQTuodQYPoOSfuD9Vtr-CpATsoLCfQENAX8lbC4nozzHA1uHQtloQtPcQm4Pt2_426E6qfb2GEFXeKBKh3bHd_AKeQdRXb1LcXtV14rxmrWEnl4c-VzwAklMD5MRCYg1eqx28CFSd5geQPNn8EPZPSyzN-tw4SvVhpvc3kCQdqQ5lzW7OdErccysDx0iMB50QQ6zRKO6Vg9t4zp10sN6c1FhmttucdOxYc7LgVyXhjyLhh14epPIMruC4yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eVJaPukA675BaQ9BUUSTQc9bgz6eM-OUJVHkWZWcdppoaxOhNCNIiH_6dirQ0zU56EqEr4LDfs-C9RYKPq8r2gMlr9YvG2e4FYXCAzC7hhPtJh-fbjAmJW1PR_Nlo7PCzarnYrVSPqWYbr75-5lsxgnAD3k3UiAVCusLXsv3Uko9tGEZpjJTl-Gqzd4wye0wVCz6awMLD-YrZwM8IqRrzYlYzvMTpNseIyoBamJx2r5mmxG2nFCTNssvLyQtiH20YSfhsFxp3UndnEh74TlhSWui-gpi1BRObq-6lX7HWlZEH01_uJCMWc4WO2YmdcRuPh6eRhwmUtxQgIs7gyxDQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YyBlctc82e12RlRjgTrrdsjTFdpkaa2d-C1zpXSvvxdasnj6a8jav8a7yUey9O8isj7U1GnBQ79pG-BFEngxlV7iLJkzxynkjYS5fjhqSfpct5zTzRpZW0JjDss7fUkepM_ES6famrznkEFPZwf_K4bY9LH0jxvR-piO4eI2FrEOXZuLSse49Mcb8YVzi9xtJoou-5ExRvF-kg9Fg920-175U1acUDmAHpn0dSpiyO1_vESS8H2WJ22bkZPW866kfwBdR_OBcop-nF0C-BCGfknHfHQf9fxY5DaesAcI3WvGRwM_eJCIUkf7kNLDh7bmueB5pCQxbxAPPMPe5U-lIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g6v0xEpWUGlpZZApIe1kdpaEGZjzm7k_EzlVtJ6oHaVXemfbU3vOuPEjOi7qe3lgqF6fEYaxf7k7CBTVcSkzkJm_1ZJad2AA2LP4Ozmn1gJ_jhOMddE-SUMN2bgIm_5y2Vnf7CvyiyP3QNB4PkilXWISCqMIp8mzOcuLdtbEz1NzKYClb2Mh-1-_9_5O5I5NvzUVsfrwPto7ruu2vwk1N7rX80BsZDUJzP9cIkEyRxpaNOiZ4SdPwPW8O8AzelP5bFUNJ3QdDp0SgmWq5fKNFVeASYozWS0ARim1Yzovw56g43FXJMBI2qtk8tFxB6V_WPfghX8y1uMhxgyrRGRZjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امام جمعه موقت تهران: دشمنان در صورت خطا، موشک‌های جدیدی را تجربه خواهند کرد
🔹
علی‌اکبری در خطبهٔ نماز جمعه: نیروهای مسلح آماده‌تر از همیشه هستند؛ دشمنان در صورت خطا، موشک‌های جدیدی تجربه خواهند کرد.
🔹
آن‌ها در صورت خطا، جنگ فرامنطقه‌ای را تجربه خواهند کرد…</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/437236" target="_blank">📅 17:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437235">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzFGVgF8g3xTmwBCoAl0NKbIU5724ZUl2CxTJ-0K5KT7OKdDksfdh5xeMRU980qHhtQRILHcDmB22M0r9h_DkkefoJa9zwCNoIodD3HU_8iwZo4HbIzo8QflYqPZg3hxhGRGDrrk6Tueqlgr5DVqEa-F_EOB3GQkIw5A3_QY4SifUZjUOVMAo00KPKWDtpZQ1e6nNblDCna4kBo1RRJLTmCjJaHnQ12tG3tFputHH5BxYUmeMWNOiNFESiilh8-5R7oB2Zk_S7wL7_P2GYsEQzwZavMDcwN3Emwu1Gq1M8fqN1vYtybKe1o1ysuyISkHZySZ_3gL7H10pufX2R9-wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مقام ایرانی: خبری از پیش‌نویس توافق با آمریکا نیست
🔹
روزنامه «العربی الجدید» به نقل از یک منبع نزدیک به مذاکرات جمهوری اسلامی ایران و آمریکا گفت که سفر فرمانده ارتش پاکستان، «عاصم منیر» به تهران به این معنی نیست که توافق نزدیک است.
🔹
وی همچنین خبر داد گزارش‌هایی که اخیرا درباره پیش‌نویس احتمالی توافق ایران و آمریکا منتشر شده، صحت ندارد و صرفاً گمانه‌زنی رسانه‌ای است.
🔹
این مقام ایرانی گفت که «محسن نقوی» وزیر کشور پاکستان حامل پیام جدید آمریکا برای ایران نبوده است.
🔹
وی می‌گوید سفرهای مسئولین پاکستان به ایران، در راستای تقویت میانجیگری اسلام‌آباد و نقش آن و تمایل برای جلوگیری از تشدید تنش‌ها است.
🔹
این منبع تأکید کرد که تهران همچنان خواسته‌های آمریکا را افراطی و غیرمنطقی می‌داند و بر این باور است که مشکل اصلی مذاکرات در واشنگتن است نه در تهران.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/437235" target="_blank">📅 17:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437234">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9b283db6.mp4?token=pVGNMiF2WGoUTtk-wZj-nrpf6vDyrbHStiDv99Axh9Sw0g_od97yK8waTWfEHRoFW5hv7caXCOtXa4Qn8CIWrbh3HbF3ZyLzM3P92OJXhq8awJu_SOqLl8KYfNRFSBUZiOt2xC3aJmicimUXYOEAV6tsxZXdZGkgdz3bdfgYGGcfpW_NJhynW7K_Xh3TKa8DlYWgN_kxhYym-CV9QpmmHXgItZtTGVrZfqvX6Oy7FOLQXV1MPpD4nv3ZAbrfYPvlnzWAD_jhcX5qyPHncQXpfP-f_6Nrcogl9nNaijHbzDPCh7uGnpeJRKT0TcOLr-9w5PXvDQXSFweBR8CeyCTgG4NsIXwenxcwsrGrfmgxS-8xJpJxkMmIDw27AhzV61mOJqKrI8ajGmnQ7-_to5RRlIk3DwXBio-rJiAvnnNR1vHcvhututlSOAihkKN7hCz41Ojn18GPGbIuGgnYbgME1l1x93-206SraM3Qt1ZeCRw2f6YK-HxKcqHcSZ-Mcj2LX4o7Pnfa3ITU9ncN6ePOm6oDN05Djbgp4VgiikMnlTPfWa7Gk0V6tiy8MrwwwmTVtHodhNn9ceZfFf0o09BH1X154ZvqBfymIXXKxbdQBMnpCCV5bN4c4B5DakIZ3b0ZOr8PFxadZgFqOBQ-TweeGdFnr1noppK40MILOkP1H9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9b283db6.mp4?token=pVGNMiF2WGoUTtk-wZj-nrpf6vDyrbHStiDv99Axh9Sw0g_od97yK8waTWfEHRoFW5hv7caXCOtXa4Qn8CIWrbh3HbF3ZyLzM3P92OJXhq8awJu_SOqLl8KYfNRFSBUZiOt2xC3aJmicimUXYOEAV6tsxZXdZGkgdz3bdfgYGGcfpW_NJhynW7K_Xh3TKa8DlYWgN_kxhYym-CV9QpmmHXgItZtTGVrZfqvX6Oy7FOLQXV1MPpD4nv3ZAbrfYPvlnzWAD_jhcX5qyPHncQXpfP-f_6Nrcogl9nNaijHbzDPCh7uGnpeJRKT0TcOLr-9w5PXvDQXSFweBR8CeyCTgG4NsIXwenxcwsrGrfmgxS-8xJpJxkMmIDw27AhzV61mOJqKrI8ajGmnQ7-_to5RRlIk3DwXBio-rJiAvnnNR1vHcvhututlSOAihkKN7hCz41Ojn18GPGbIuGgnYbgME1l1x93-206SraM3Qt1ZeCRw2f6YK-HxKcqHcSZ-Mcj2LX4o7Pnfa3ITU9ncN6ePOm6oDN05Djbgp4VgiikMnlTPfWa7Gk0V6tiy8MrwwwmTVtHodhNn9ceZfFf0o09BH1X154ZvqBfymIXXKxbdQBMnpCCV5bN4c4B5DakIZ3b0ZOr8PFxadZgFqOBQ-TweeGdFnr1noppK40MILOkP1H9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار سی‌ان‌ان: ادعای فرمانده سنتکام در مورد به‌عقب‌رفتن چند ساله صنایع نظامی ایران درست نیست
🔹
به ما گفته‌شده که ایرانی‌ها توانسته‌اند پهپادهای جدید زیادی تولید کنند و برنامه پهپادی آن‌ها در واقع می‌تواند ظرف ۶ ماه کاملاً احیا شود.
🔹
پهپادهای ایران به‌شدت…</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farsna/437234" target="_blank">📅 16:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437233">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شمار شهدای لبنان از مرز ۳۱۰۰ نفر عبور کرد
🔹
وزارت بهداشت لبنان: در جریان حملات رژیم صهیونیستی، ۳ هزار و ۱۱۱ نفر شهید و ۹ هزار و ۴۳۲ نفر هم زخمی شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/437233" target="_blank">📅 16:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437232">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پیام قدردانی سپاه پاسداران خطاب به برگزارکنندگان حماسهٔ اجتماعات شبانهٔ مردمی
🔹
مداحان گرانقدر، خطیبان ارجمند، هنرمندان متعهد، ورزشکاران غیرتمند، مدیران و تمامی نقش‌آفرینان تجمعات شبانه مردمی سراسر ایران اسلامی؛ بیش از هشتاد شب پیاپی، خیابان‌ها و میدان‌های ایران اسلامی در شهر و روستا، به تماشای شکوهی نشست، که شما با سرمایه ایمان، غیرت و هنر خویش، به زیبایی خلق کرده و صحنه‌هایی رقم زدید که در محاسبات دشمنان این کشور، به‌ویژه آمریکای جنایتکار و رژیم پلید صهیونیستی، «معجزه‌ای غیرقابل باور» تلقی می‌شود.
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی، عمیق‌ترین سپاس و قدردانی خود را تقدیم می کند به  شما خطیبان که با روشنگری در تریبون‌ها و سخنرانی‌های آتشین، چراغ بصیرت را در شبستان‌های این مرز و بوم روشن نگه داشتید.
🔹
شما مداحان شورآفرین که با نوای حماسی و مرثیه‌های روشنگرانه خود، روح غیرت و شهادت‌طلبی را در رگ‌های اجتماعات دمیدید.
🔹
شما هنرمندان متعهد که با قلم، تصویر، سرود و نمایش، زبان گویای اعتراض به قلدری‌های استکبار و همدلی و حمایت از نیروهای مسلح و مدافعان وطن و همچنین غزه و مقاومت اسلامی را بلند کردید.
🔹
شما ورزشکاران غیرتمند، که با حضور مقتدرانه و نمادین نشان دادید که میدان ورزش، عرصه دیگری از جهاد تبیین و نمایش وحدت ملی است.
🔹
شما مدیران، میدان داران، مجریان و خادمان گمنام در فراهم آوری امکانات و زمینه‌سازی حضور میلیونی مردم مبعوث‌شده ایران اسلامی نقش‌آفرینی کردید.
🔹
شما حافظان امنیت در کسوت انتظامی، امنیتی و بسیج که حریم مقدس حضور یافتگان در تجمعات را، از گزند اهریمنان و خیانت‌کاران به ملت و کشور پاس داشتید.
🔹
شما خادمان فرهنگی که با قریحه و ذوق مثال‌زدنی با متون فاخر و تصاویر ارزنده خیابان‌آرایی و جایگاه‌سازی کردید.
🔹
و شما مردم مبعوث‌شده بصیر و آگاهی که این هشتاد و چند شب پرشور که طوفانی از «سرمایه اجتماعی» و «وحدت ملی» بود، در برابر چشمان حیرت‌زده جهانیان، ماهیت مستحکم و بازدارنده نظام اسلامی را به رخ دشمنان کشیدید و با پیوند قلبی و رفتاری با نیروهای نظامی میدان نبرد سخت، ثابت کردید که حماسه‌آفرینی در جمهوری اسلامی، نه تصادفی، که برآمده از یک اراده اعتقادی و ایمانی، باورمند به منافع ملی و میهنی، هماهنگ و عاشقانه است.
🔹
امروز، به برکت مجاهدت پرشور شما و ملت لبیک گو به فرمان مقام عظمای ولایت و رهبری و فرماندهی کل قوا حضرت آیت‌الله سیدمجتبی خامنه‌ای (دام ظله العالی)، قدرت نرم انقلاب چنان در تار و پود جامعه رسوخ کرده که هیچ تهدید نظامی یا روانی دشمن توان مقابله با آن را ندارد.
🔹
بی‌تردید همه شما وعده داده‌اید که تا پایان راه و تحقق اهداف عالیه انقلاب و مقاومت تاریخ ساز، در صحنه هستید؛ چه در زمان نبرد نظامی و چه در زمان نبرد مذاکره، چه اینکه می دانید مذاکره، صحنه دیگری از کارزار میدان نبرد است که نیازمند استمرار حضور مقتدرانه و پرشور در خیابان و پشتیبانی از افسران عرصه دیپلماسی تا کسب پیروزی نهایی است و این "وعده صادق"، بزرگ‌ترین سپر دفاعی کشور عزیزمان ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/437232" target="_blank">📅 16:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437229">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnEa5HrM0wgyxBtP5ofvSdv34z9Xys4Q3BzS1KAjCVKv8y3w8cvNCO_gmHO76prJU3iO3iRoeh1BKJXEPyj17daE8ioCd6gO1XQT09zrZkVOVGuR2WPODljT4iBAZENK-fVunyahnmo12eSlTRSYZy4eBCzedCtLrHdUoKbrSbBtWMq78B8vBbYUzXKHlp-G7IFOeG9MCZjxVDO6q5xpuZ7cD0oGOzVPHyuoQXekOqP9ZvehFb-n2B8fiDpctVHeV-NBzTPJkNrX2pg7A_ENLkRUN2LcMun6PyizgJcN3yMlhLcX278rv8gbSwcy4CErNMkWBeLj_5mnOT8ZxsRhOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کرکرهٔ من‌و‌تو باز هم پایین کشیده شد
🔹
تلویزیون من‌و‌تو، شبکهٔ تروریستی فارسی‌زبان مستقر در لندن، در اطلاعیه‌ای رسمی اعلام کرد که به‌دلیل محدودیت‌های مالی، ۳ خرداد به پخش برنامه‌های خود پایان می‌دهد.
📌
این شبکه تاکنون با دلایل مختلف ۳ بار اظهار تعطیلی کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/437229" target="_blank">📅 16:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437228">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130acd57d.mp4?token=K4HZD7-S5pywihhHeiYAAXw7wVyliDzTJeRvdkwcpHDiNQxiH2ATDpi0mvnXSQB7vSfQFbjR-OUS4z75k9_kDiwAVq1NN6jQULTNpSrl73Xxw53AJP4XuTBSYBn-Iz9R5iX2W3L-iJfhz0dsUb9BlCoq7iTcBmpdvRpQTyh8qI2uN-UI3grnlBGyIEADEiqDd1_cjnRxz4dI0_jyxqwDU8ifhLW4bhhsdGnJaa53qe1ccVaK8MvZ1DeLRLwY241TNRGav7wDdApw27VI9DCy9roVA4ZhiuB3LpXlQhwNozUfYP4kyhVelo3f5V2Pk9gpiOJ5T3IuXjGWIV7gjK_6oI3BqYeQcd-2vpCewikn9jIZ8l14e0FSrUzj50EYNT-Y3T3LynVrNX4z8y1idWDhq_XAp8TERWFhCX2F1nTUxm5gt7csYUdqKk-2iCcPkXgSphQ0bVPIQ6Bp71R5qpLJdkzyxlGackwqXVuJfGpO6qGk6ipZ7VFAAScfHx57H9uIrtxHRIbm0PomPdkA-ji5ziVDFhDIluy4e_ti5dDUd2qn0LxWiNagIDJHZm_4hbL7FtAhDOgN91j5nWqfuSUtnBhVxXJ7qsJe2Bham5ir-pXLGUVE0Z8UZTIepwCLbt5NXaixZfTxrXZ6-vNJhBvCR6LmNOAqix-jHC4i86b4wWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130acd57d.mp4?token=K4HZD7-S5pywihhHeiYAAXw7wVyliDzTJeRvdkwcpHDiNQxiH2ATDpi0mvnXSQB7vSfQFbjR-OUS4z75k9_kDiwAVq1NN6jQULTNpSrl73Xxw53AJP4XuTBSYBn-Iz9R5iX2W3L-iJfhz0dsUb9BlCoq7iTcBmpdvRpQTyh8qI2uN-UI3grnlBGyIEADEiqDd1_cjnRxz4dI0_jyxqwDU8ifhLW4bhhsdGnJaa53qe1ccVaK8MvZ1DeLRLwY241TNRGav7wDdApw27VI9DCy9roVA4ZhiuB3LpXlQhwNozUfYP4kyhVelo3f5V2Pk9gpiOJ5T3IuXjGWIV7gjK_6oI3BqYeQcd-2vpCewikn9jIZ8l14e0FSrUzj50EYNT-Y3T3LynVrNX4z8y1idWDhq_XAp8TERWFhCX2F1nTUxm5gt7csYUdqKk-2iCcPkXgSphQ0bVPIQ6Bp71R5qpLJdkzyxlGackwqXVuJfGpO6qGk6ipZ7VFAAScfHx57H9uIrtxHRIbm0PomPdkA-ji5ziVDFhDIluy4e_ti5dDUd2qn0LxWiNagIDJHZm_4hbL7FtAhDOgN91j5nWqfuSUtnBhVxXJ7qsJe2Bham5ir-pXLGUVE0Z8UZTIepwCLbt5NXaixZfTxrXZ6-vNJhBvCR6LmNOAqix-jHC4i86b4wWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم ایران ۴ هزار دقیقه در دستان مردم کرمانشاه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/437228" target="_blank">📅 16:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437227">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">زخمی‌شدن نظامیان صهیونیست در حملات حزب‌الله
🔹
برخی منابع صهیونیستی اذعان کردند در جریان حملهٔ پهپادی حزب‌الله به پادگان برانیت (مقر فرماندهی لشکر ۹۱)، چند نظامی صهیونیست زخمی شدند.  @Farsna</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/437227" target="_blank">📅 16:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437226">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اضافه‌کار بعد از ساعت ۱۳ ممنوع شد
🔹
سخنگوی سازمان اداری کشور: ساعت آغاز به کار و خاتمهٔ ادارات ۷ تا ۱۳ تعیین شده است؛ طبق بخشنامهٔ ابلاغی، تعیین حجم و درصد حضور کارکنان همچنان در اختیار استانداران است، اما ساعت آغاز به کار و خاتمه قابل‌تغییر نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/437226" target="_blank">📅 16:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437224">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AP9uZxW4LcRF-AWU9Fs5bB-ybb2QFY_u0A6QpjDSdW-C2OBngLmrFnraIL5r7atqKSO3QGlS_lJ7qL_He4g3F5xS7DxxPrlz2Mu1_xcYOduJ--j9K9bOVjZ92USvXMkJfzg-5zOR-DponNj2khQEsKWs6ig000K6fNeDiJf3iBRG0IB_hZ3MXVhzDyGfjGgHWm7HuAGCbPMDzKXr4mHuAvoweCooaxWiLfIzDb7Qz3r_nTO22BXGLn3LJ9WTO7nvsGlToiiDHQw_9xji0es9LT75c99R_eh_LuB_YoqUbXn69756TcRaLZyTLV3Z366UCN3ttTpD8MWOzy_bJhqFKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba3f4a10bd.mp4?token=sjXBaeo-P_Hnmrb8DVMfVppZ4VgPwUF8wnYAI7ZOeiJqJX0Z-FtyDKELZEDsbn8YSJmVSTP0NmIe2Wv7rtOG6n1f4N9ddsvYLG_wTsEZJqJiXfd_MZkkfSVl7L8Vk7XcVxwX7au7rOb5JpuJ5P3UZA85YmmZ7PKjE2LXMKV5mE_gFn4yXa9ZJSMWe1_EUTVlh2jhwFuqj914sBoQWBBWR-eCiKJUG3cl2LbwWigo0j4Xtdvfkc5T8zHQNomZyz8wL7wh0xnZRF4XNPkA0xfiyHnrs1TYIdfUxfFP_miD650l6yIG4GfqBod3lbl6wQQOyOblIdI-EvXF3AADX2touQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba3f4a10bd.mp4?token=sjXBaeo-P_Hnmrb8DVMfVppZ4VgPwUF8wnYAI7ZOeiJqJX0Z-FtyDKELZEDsbn8YSJmVSTP0NmIe2Wv7rtOG6n1f4N9ddsvYLG_wTsEZJqJiXfd_MZkkfSVl7L8Vk7XcVxwX7au7rOb5JpuJ5P3UZA85YmmZ7PKjE2LXMKV5mE_gFn4yXa9ZJSMWe1_EUTVlh2jhwFuqj914sBoQWBBWR-eCiKJUG3cl2LbwWigo0j4Xtdvfkc5T8zHQNomZyz8wL7wh0xnZRF4XNPkA0xfiyHnrs1TYIdfUxfFP_miD650l6yIG4GfqBod3lbl6wQQOyOblIdI-EvXF3AADX2touQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام اعضای مجمع شهرداران آسیایی به شهدای میناب
🔹
شرکت‌کنندگان نشست تخصصی مجمع شهرداران آسیایی در سیزدهمین اجلاس جهانی شهری به احترام شهدای میناب یک دقیقه سکوت کردند.
🔹
همچنین دبیرکل مجمع شهرداران آسیایی در این مراسم عضویت افتخاری این سازمان را به نمایندهٔ شهرداری میناب اهدا کرد.
🔹
دبیرکل سازمان متروپلیس، دبیرکل بخش خاورمیانه و غرب آسیای سازمان شهرها و دولت‌های محلی متحد از حاضرین این نشست بودند.
@Farsna</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/437224" target="_blank">📅 16:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437223">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5b1b1014c.mp4?token=akjJZ_PJh1zpBJyTNcyebC6kJVNQhFUAIgRHoYodQd_rwlrqGocCw7TTYWl--E5695U8KNwCvNbOu3yDG07Z9SE9okEp4gnBq4fu1AEYLSHgs_g9ss6GKzdNxQuYYFdBBr9erEvMZrwVqDaDSdeHNSFIQ9m0PEkgNchsJUpXLKQ5Q1rbJtpWvgPNcdr7nXRSfz5qcTFq06TdlY4gsZWHSlKUfk3mMHLrcIIJrdXQ44ZZhNgEu1H4Fj8D-WQ86cAtNrHqr-UTZOkNhf1wUS6TxH7bzNhwFd56392LEKH6tMrlyWN5J8VBYHeH4c_cU-E4XrLxpeOwIgFfTjxsoPUVgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5b1b1014c.mp4?token=akjJZ_PJh1zpBJyTNcyebC6kJVNQhFUAIgRHoYodQd_rwlrqGocCw7TTYWl--E5695U8KNwCvNbOu3yDG07Z9SE9okEp4gnBq4fu1AEYLSHgs_g9ss6GKzdNxQuYYFdBBr9erEvMZrwVqDaDSdeHNSFIQ9m0PEkgNchsJUpXLKQ5Q1rbJtpWvgPNcdr7nXRSfz5qcTFq06TdlY4gsZWHSlKUfk3mMHLrcIIJrdXQ44ZZhNgEu1H4Fj8D-WQ86cAtNrHqr-UTZOkNhf1wUS6TxH7bzNhwFd56392LEKH6tMrlyWN5J8VBYHeH4c_cU-E4XrLxpeOwIgFfTjxsoPUVgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تانک رژیم صهیونیستی در چنگ پهپاد حزب‌الله قرار گرفت
@Farsna</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farsna/437223" target="_blank">📅 16:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437222">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">زخمی‌شدن نظامیان صهیونیست در حملات حزب‌الله
🔹
برخی منابع صهیونیستی اذعان کردند در جریان حملهٔ پهپادی حزب‌الله به پادگان برانیت (مقر فرماندهی لشکر ۹۱)، چند نظامی صهیونیست زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/437222" target="_blank">📅 16:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437221">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735faee829.mp4?token=JAJTGeh9UMYpHEgM74JtFbk06AtoMLtkF2AnaDIVREhbwQhoUrWyT_9DRWrItBsh3uIpMYeUeNQtaP_-9fCTOw2I2CeZZGrLSTUK6k9fMIQosY9retL8jQ6GbISEFxH0OdxwoQHi0gJ9Wt-3tqfAY6SywLYrAO6EDGMOl2Bm-Y0O6MWKOpyXWOPA3YK9NxdT9ktvBRxvlf0PiGV58E6t9ONXzJWyXTpFLVsFGA9g8uBdWVLLnVmeTEEovt7QuThvjnm5ZgACiy3PN3snrdacmQJTH0XLNm2ry-b45offuNDi-9Sim14ju46S1ikxEiFxlYoITqbSYxZ9aGYke988xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735faee829.mp4?token=JAJTGeh9UMYpHEgM74JtFbk06AtoMLtkF2AnaDIVREhbwQhoUrWyT_9DRWrItBsh3uIpMYeUeNQtaP_-9fCTOw2I2CeZZGrLSTUK6k9fMIQosY9retL8jQ6GbISEFxH0OdxwoQHi0gJ9Wt-3tqfAY6SywLYrAO6EDGMOl2Bm-Y0O6MWKOpyXWOPA3YK9NxdT9ktvBRxvlf0PiGV58E6t9ONXzJWyXTpFLVsFGA9g8uBdWVLLnVmeTEEovt7QuThvjnm5ZgACiy3PN3snrdacmQJTH0XLNm2ry-b45offuNDi-9Sim14ju46S1ikxEiFxlYoITqbSYxZ9aGYke988xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درخواست رئیس‌جمهور برای بازنگری مصوبهٔ کنکوری شورای عالی انقلاب فرهنگی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/437221" target="_blank">📅 16:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437220">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eB1QoW22UwLBV0f6ivfN0JBe5FiYWjWgF6H5-FasqyjRNwl5Og9jMS3l-JMpPqxW5y6XSaTfD8AymljHmAIZ4s__GcO-jBCJhFABIhEldkVQ8Ri5VkXUGPicacQ8I8ol_vdLuboIqs5UUvkvy8fxKFb430xfu1rFmsVbmQpo00qrbBltaoFPtupjCUWueovWoLyufRCKuo6-udGLDSTKeG3KRUXmuZIrV1n1fxuX8yC_tFFXVcnIztgwN8ehKd2gWUYBhdhsZYQHuqN1qA9VdjXTHVkLLbS1W6VIH8ngvSUZJxJDmk2xYZ7EANrXI2825jjgTP9GmTwhjR5MPJJMxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه العربیه گزارش کرد که فرمانده ارتش پاکستان راهی تهران شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/437220" target="_blank">📅 15:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437219">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
حزب‌الله: موضع توپخانه‌اى ارتش دشمن اسرائيلى در شهر العديسه را هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/437219" target="_blank">📅 15:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437218">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/490dbb67c4.mp4?token=Md2hYr9r5jrtyg5XosBiQ0JppLjbXhELweifNYDHd4Y5UI-6JwmsTXRMEZA0fgJXw5VCJ6BlPs1iJsg12UTrjXIPuznnDo1UT3pGq_kLaollQ245oIalOMZ94G4iSc8bDz7XMC9FlLDpMdQtp0KP-3vbvQBF1A1z1y3qnxhMiNd5zGMrjudbUHa9fyHUkCr2GR8rjP1TAeMM-83NOKkeOyRQxN10gQj9z9dJvR5B9EVfoAMPaTRMnf312jd8jSVt1EUcoukPZEHaNOfuG5BERfPabuO9ma2ZMgKep9kUzY70Qm7m6HWgjigZiBylO7UAbZd16TKupYgTRc-9YD08sIKLlHKBx1oq-64qx4uGaasb65Kn_pO_MhCMWf3elVYpb0ODRfH1C-U-pfPyAOVM-gLBV8gxQidC-tKWH_4vSbpSo6a-WscDcTSEIGjMtmEGHh9nFh4wyFt1rfRtBNhHhN0iXzO60NoWxncowU_16u0zg7Tjb3_zjSIQbuzN3uLUZzI-2vRS6tNoZhPrVbVeZQs2ZwGSZSZEoZd-pbzMu8Fbuo8d9bTc8v-IkrvytNMqxEBCPyxV5FJWSlW2e1wfSql8YXjM3R0nYQ1nNWHnrSBnbJdVgYYY98EORAFweY_VMGWfZ1QI7lwf0BdKu-z8rEXvYV9q6OOAO4yurlxN2-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/490dbb67c4.mp4?token=Md2hYr9r5jrtyg5XosBiQ0JppLjbXhELweifNYDHd4Y5UI-6JwmsTXRMEZA0fgJXw5VCJ6BlPs1iJsg12UTrjXIPuznnDo1UT3pGq_kLaollQ245oIalOMZ94G4iSc8bDz7XMC9FlLDpMdQtp0KP-3vbvQBF1A1z1y3qnxhMiNd5zGMrjudbUHa9fyHUkCr2GR8rjP1TAeMM-83NOKkeOyRQxN10gQj9z9dJvR5B9EVfoAMPaTRMnf312jd8jSVt1EUcoukPZEHaNOfuG5BERfPabuO9ma2ZMgKep9kUzY70Qm7m6HWgjigZiBylO7UAbZd16TKupYgTRc-9YD08sIKLlHKBx1oq-64qx4uGaasb65Kn_pO_MhCMWf3elVYpb0ODRfH1C-U-pfPyAOVM-gLBV8gxQidC-tKWH_4vSbpSo6a-WscDcTSEIGjMtmEGHh9nFh4wyFt1rfRtBNhHhN0iXzO60NoWxncowU_16u0zg7Tjb3_zjSIQbuzN3uLUZzI-2vRS6tNoZhPrVbVeZQs2ZwGSZSZEoZd-pbzMu8Fbuo8d9bTc8v-IkrvytNMqxEBCPyxV5FJWSlW2e1wfSql8YXjM3R0nYQ1nNWHnrSBnbJdVgYYY98EORAFweY_VMGWfZ1QI7lwf0BdKu-z8rEXvYV9q6OOAO4yurlxN2-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت معاون اجرایی دولت شهید رئیسی از کار انقلابی شهید جمهور در صنعت نفت  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/437218" target="_blank">📅 15:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437217">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvtGM92SKLbi1vvP4SNme0PPZN70THYwGhEmtoL1_dC60IbgW2pUMHCUqSICq9RXuOsR77RcqpVrd-b2A1pGdLyGsolPvqKXb-_3ud8BsznWPdTBIJ6tX0qT14bYYwhsgX5OIge3tzXWCg5Hp83w66JoYr_GWlGZwDChce-NqE6ohAl-Xr7EukZ9rzEoztS2ZjSfYr7EmyL6ZNh7LNHiFdiBjoTsblJFQBPEtz1k-OgO4PHESdLusfLjsprZnoKNQRo1FQAwdBfj5Y6JSwRHZ5RDqtuKvLy3hdmu42Hzrs2bv7X96Ve4eECJMHj9zAZMtLiEX4XsFsABX-Y7Dbe21w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقایی سخنگوی هیئت مذاکره‌کننده شد
🔹
قالیباف، رئیس هیئت مذاکره‌کنندهٔ «میناب ۱۶۸»، اسماعیل بقایی را به‌عنوان سخنگوی این هیئت مذاکراتی منصوب کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/437217" target="_blank">📅 15:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437216">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🎥
دانشمند علوم سیاسی: عبور کشتی‌ها از تنگهٔ هرمز یعنی جامعهٔ بین‌المللی واقعیت تحمیلی ایران را پذیرفته است
🔹
بسبوس: ایران به همسایگانش ثابت کرد آمریکایی‌ها توان شکست‌دادن این کشور را ندارند؛ کشورهای حوزهٔ خلیج فارس با خود می‌گویند بهتر است با دشمنی که آمریکا نتوانسته شکستش دهد، تعامل کنیم.
🔹
ایران ۴۷ سال تحت تحریم بوده، اما انعطاف‌پذیری و هوشمندی بیشتری از آمریکایی‌ها نشان داده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/437216" target="_blank">📅 15:30 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437215">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kD7Ht0YvdoYqN9SVBbKKWnPr_UxjD7-ARsDzRL4AEqnu5U4fxFSdxrYFrKcTgzdBIk02fP2ZFHs19WYCyUjOEpHsZq1NWKWTzJm43a0IcLXr5ILeHnX5gAaf5ywaEgp2wuj3TkAc9LFDhJ1Pp--h-Uwn8y7Uaj2eYu-SLnHuYghcZjQgQZfcUD2J5mgByy7hryAixZxdAp6NRWrHRnNLDi3PZE7c9tA1NsLmW06F8qmPCy37zzENLnFPgUN5HzIKp34jODmqcqXCKHck_Eq5F2-9xJMAOzcOebgfJS4SBEll22CvsSM7vvX-INi4Dg342OxlhmeERI0nY2rH-1Zdog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار به کاهش قیمت مرغ چراغ سبز نشان داد
🔹
دبیر انجمن تولیدکنندگان جوجه یک‌روزه امروز از افزایش تولید مرغداری‌ها و کاهش قیمت مرغ در روزهای آتی خبر داد.
🔹
قیمت مرغ در روزهای اخیر با ۱۰۰ هزار تومان افزایش تا کیلویی ۴۶۰ هزارتومان بالا آمده اما اتحادیه‌های تولید از افزایش جوجه‌ریزی در ماه اردیبهشت و کاهش قیمت در روزهای آینده خبر می‌دهند.
🔹
درحالی‌که جوجه‌ریزی در اسفند زیر ۱۰۰ میلیون قطعه بوده، در فروردین ۱۰۶ میلیون قطعه و اردیبهشت ۱۲۰ میلیون قطعه شده و پیش‌بینی شده در خرداد ۱۳۰ میلیون قطعه برسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/437215" target="_blank">📅 15:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437214">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPv4TnBhvw0mh48S6kEEDHO8K8mFwQdZ8UqnGpQ46ep5QvQyW4bIJHNATogRXgPU3tfOcEjJbafNuUzPN_2jPWM7yJgfBF6_h2t2tiYpFHoYkUCeLClwNWAVLi3lfObJPcsviSedFX2zDMwyyU1ZIQHqIqZfH4qCvmlvphgmmiuSss0FPlIagIe3Avm1Why63rugXhDZojRQNBjWZgUYJlhr9_Rxax95ZQ9HwMCIZYTkeMFGiDOcfjVVDc1BepgTUs8JQiiaYSu05R1yX-HYB-Ic_yyXTWT9nS4q47C189fVaQ4vSItsg0mLdkN8gFdqx5zEYF15p62_kKaXksdcyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ علیه ایران میزبانی یک جام جهانی را از عربستان گرفت
🔹
میزبانی عربستان برای سومین سال متوالی در جام جهانی ورزش‌های الکترونیکی طبق گزارش امروز نشریهٔ اکیپ فرانسه به‌دلیل جنگ در خاورمیانه لغو شد و این میزبانی به فرانسه داده شد.
🔹
این مسابقات ورزشی الکترونیکی در ۲ سال گذشته به میزبانی ریاض برگزار شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/437214" target="_blank">📅 15:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437213">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJDD1HAGCPwpM2B4wJ7SW-h6ND5wWh35TxPotJDaKtPhetcXtA42ATyg6fD5z4VU4MmHYmkcLEbuFppGfZVFNBlGDlPzS4BOVYxPQ5NppydsT2m-lzzj7vsIIq-JygXgnfOV9bk318YAeV1Gusj800sKEMCrLOBgSPS9W16-R1yEH1H1P1dyLZDm45GKDMWJI4dCamshj-HJcDw-ohwzjF0fNTfOAWvGTRpnQPZ3nyNBC2UPgvn32z9Qyt-XOd_9Kp3MtiKw952EteQjgOByyqxbJjFaFeznyusznSsbcR1Ij9sVA6tvC2NbIRPutYmpgO0EQ40As_Uoe9__FaDj4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه: حمله به ایران تجاوز نظامی آشکار علیه یک دولت مستقل بود
🔹
بقائی در واکنش به اظهارنظر اخیر رئیس‌جمهور آلمان که در یک مصاحبه پادکستی، با انتقاد از آمریکا به دلیل خروج از برجام در سال ۲۰۱۸ و متعاقبا توسل به زور علیه ایران، تجاوز نظامی آنها را «جنگ غیرضروری» نام نهاده است: آقای رئیس‌جمهور، درست است که بحران کنونی که منطقه ما و جهان با آن مواجه است در اصل به خروج یکجانبه غیرقانونی و خودسرانه آمریکا از برجام برمی‌گردد.
🔹
درست است که این جنگ تحمیلی می‌بایست و می‌شد که شعله‌ور نشود؛ با وجود این، در منشور سازمان ملل متحد هیچ مفهومی با عنوان «جنگ ضروری» وجود ندارد که دولت‌ها را صرفا بر مبنای هوا و هوس متجاوزان مجاز به توسل به زور علیه یک کشور صاحب حاکمیت کند.
🔹
ماهیت مجرمانه حملات آمریکایی و اسرائیلی علیه ایران را نباید صرفا در حد «جنگ غیرضروری» تقلیل داد یا قاب‌بندی کرد.
🔹
حملات آمریکا و رژیم صهیونیستی علیه ایران، نقض فاحش بند ۴ ماده ۲ منشور سازمان ملل و یک تجاوز نظامی آشکار علیه یک دولت مستقل بود.
🔹
هر کشوری که برای حاکمیت قانون و اصول منشور ملل متحد ارزش قائل است باید این تجاوز نظامی را صراحتاً محکوم کند و خواستار مواخذه متجاوزان شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/437213" target="_blank">📅 14:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437212">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خنثی‌سازی مهمات عمل‌نکرده در بندرعباس
🔹
سپاه هرمزگان: عملیات خنثی‌سازی مهمات عمل‌نکردۀ جنگ رمضان فردا شنبه از صبح تا عصر در بندرعباس انجام می‌شود؛ مردم نگران صدای ناشی از این انفجارها نباشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/437212" target="_blank">📅 14:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437211">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a424005de3.mp4?token=lp4jVXSIxMWVii0Jqa1TgTepfp6EF3NK5gDJ5lenrYRO4MI3v38mJG8gRgcoGT_KRSHFhryTdM5SvgYGUYINZV16JZdqiabEG7kEn4mBNZFRqk78IowWjFRiZ_uBgP6S71YO1BPr_dT67JAdtLXvVIXC4h5dE96vbN0BjDFzDXgs9w4t6cB2eREMjcfBCTjJMF_WmMU16lhaIZNPAeT5tkVxIMo56opaT-hFc03lQbzmRR1xj61JWuK_fgFL07nMprfZVSaWWbuYhzpRbUzek012q08rS8gTX1cIM7PuFfWQLOrTufL_P-UPsoqXnaOl1v3EaMmp0Hj18eksY0BX4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a424005de3.mp4?token=lp4jVXSIxMWVii0Jqa1TgTepfp6EF3NK5gDJ5lenrYRO4MI3v38mJG8gRgcoGT_KRSHFhryTdM5SvgYGUYINZV16JZdqiabEG7kEn4mBNZFRqk78IowWjFRiZ_uBgP6S71YO1BPr_dT67JAdtLXvVIXC4h5dE96vbN0BjDFzDXgs9w4t6cB2eREMjcfBCTjJMF_WmMU16lhaIZNPAeT5tkVxIMo56opaT-hFc03lQbzmRR1xj61JWuK_fgFL07nMprfZVSaWWbuYhzpRbUzek012q08rS8gTX1cIM7PuFfWQLOrTufL_P-UPsoqXnaOl1v3EaMmp0Hj18eksY0BX4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تست شوکر برقی شهردار پرو روی مشاورش!
🔹
کارلوس بروس، شهردار یکی از مناطق پرو، ظاهراً تصمیم گرفته است شوکرهای جدید پلیس را شخصاً آزمایش کند و در جریان این نمایش، به‌طور اتفاقی مشاور خود را دچار برق‌گرفتگی کرده است.
🔹
شهردار مدعی شده است که این آزمایش «کاملاً داوطلبانه» بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/437211" target="_blank">📅 14:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437210">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8b42ad1d0.mp4?token=PkbcFrjlO52Nq4ihvXgxp8Turyg1ZQN0w8xkZ_rr1Bv-ULWvk2Zg2WTzroG2oQu8yOgn3Llkk441guvlxMirOl2yzlFdY4kfrkd5LVLZGjSCSBEL3YosJ6j56kO4yXYh2azkYP7XqhtNfWcOlMmDC-YEe4kIlCP9JJHvNXNcdfls77i6Vcxbj6kwpoNgJh2pOZyxAliM-gKxFnBNqZL4luBgyeKvC_9T7gYV7o7GQnPQZXVGtXyPBIxaZWYKFTuW-wwwMzX8zoI5rLrHDPySWk3hJzFNvIGEnUTHhQbSOVCw7mJLqLZ-Cn_HKlLUELCOLQtENxzJn-3HBq9fV9e9dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8b42ad1d0.mp4?token=PkbcFrjlO52Nq4ihvXgxp8Turyg1ZQN0w8xkZ_rr1Bv-ULWvk2Zg2WTzroG2oQu8yOgn3Llkk441guvlxMirOl2yzlFdY4kfrkd5LVLZGjSCSBEL3YosJ6j56kO4yXYh2azkYP7XqhtNfWcOlMmDC-YEe4kIlCP9JJHvNXNcdfls77i6Vcxbj6kwpoNgJh2pOZyxAliM-gKxFnBNqZL4luBgyeKvC_9T7gYV7o7GQnPQZXVGtXyPBIxaZWYKFTuW-wwwMzX8zoI5rLrHDPySWk3hJzFNvIGEnUTHhQbSOVCw7mJLqLZ-Cn_HKlLUELCOLQtENxzJn-3HBq9fV9e9dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاعات آمریکا: ایران به‌سرعت در حال بازسازی توان نظامی‌‌اش است
🔹
به گزارش سی‌ان‌ان،‌ ارزیابی‌های اطلاعاتی آمریکا نشان می‌دهد که ایران سریع‌تر از انتظارات در حال بازسازی پایگاه صنعتی نظامی خود است و تولید پهپادها را از سر گرفته است.
🔹
«ایران در طول آتش‌بس…</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/437210" target="_blank">📅 14:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437209">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHOh5LKtUtYIPWsJaWoMXWbhIZDzbgDZpuTz52CrtggSjTiBy4L7pJiBh8NcfVanFtuEzTyIUP7v79Y-4iuAxZmRjvBYdgeYYmgFyehstZnRk2io85cGIjHv43oKM_Uw_QC8_Xq-fSb7xXzJLTBIf1nFa6DJBWvbyuADzxYsK7_RLs2mItWM3dU-1AdB5y7-ba06C1msMu0zYWkj8pYd_8KTBnvTrNALKfP7tOKxEwsSbpc3GVs35d3FytQLB-ik9OhpVb_qZ6ZftgS8qteNQn-XrHbHXDSgaB768WSeEYDWr3YRdbTvHVeRK8Ny5iHlbN85ivlK59KSsYe9nZ5Iaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: پوتین در فکر پایان جنگ اوکراین تا انتهای سال است
🔹
پوتین می‌خواهد جنگ را تا انتهای ۲۰۲۶ پایان دهد؛ اما فقط با شرایطی که بتواند به‌عنوان پیروزی به مردم روسیه ارائه دهد.
🔹
بر این اساس، از جمله این شرایط می‌توان به تصرف کامل منطقهٔ «دونباس» و یک توافق امنیتی گسترده با اروپا اشاره کرد که عملاً «دستاوردهای ارضی» روسیه را به رسمیت می‌شناسد.
🔹
اوکراین و متحدانش به‌طور فزاینده‌ای مطمئن هستند که تهاجم روسیه درحال اتمام است؛ زیرا کی‌یف خط مقدم را تثبیت کرده و تهاجم بهاری مسکو را متوقف می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/437209" target="_blank">📅 14:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437208">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS4B6WCqmS8web5uxPbelqCpQddz4JtGP4wS5BhbGrCJA9do6kEL8w3kPACLsG5Xd4uBieAvaSX75Sx-im04-o8Fy5oKmx8PmsTCPKPSEaIFd8LWZI4lrlEKd-q3NK23qvFFk2aY_RP154Xdz_G4vS3YGeu80ZmoRFhrQ0RXF-NT4WILH0JDHqhWVL0cnkE-T_TudIFkWlLapWSqH7-R6gf2lQUZ2119S7yROGDWzR8hI6bQN8qdLD8-ioqcaK8L_I04mdaFNcclgGJuy3b4pJqp_3pG5aI0_Oifb_TPzzTSVkuUEokw9gk5uuXsldIqH5IqVBQgN-XXc4U7hK-bHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گواردیولا از سیتی رفت
🔸
باشگاه منچسترسیتی، پس از ۱۰ سال جدایی گواردیولا را از این تیم اعلام کرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/437208" target="_blank">📅 14:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437207">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029e0d7a1d.mp4?token=NGw-xxLoJaiQUtQCEu1BDz4ufcQm1CSEqL1oWaBYor1GcIKk_POOp3uRqY5nFLcWB8YcraPnFRgfCaaPE_V02RYhaTrvsaqLuiT96Gu43t-eTEUqqgos0ECROiw-bDfLvZOWeotfKnT2A0kyKXHh6VKbOl-R_hnefnDohuukO_Y66wDBNxtYiRQdSXWAJZ27P09Kn1Wm6KmUPE4qMJI5V2JVxx82C3R4AY9Jhei8O_FHAa8XuZl88ez681Vh0yGDQ6ySMGcsy7NSdvTFUjIdaiNM7IB8KPqBaNVHjqDfbjyx25PRUa6SIu1AelOr-ykrCmHZeAyHTnAUwkiK0EY0DYj9Ni6KCkNpMuI51AstNMm2nji45UakI1RG6-rBD6qmoLKEj2Uex_bzFrdZn535TUaysCscmAQyY1qx7TofEJhyL0eqViFP35dO3wQ_PUGf12AeYVm-S9DM48FUO2FrdPBVTHg0RbVmqSa3X3zDEw8tDxhAkqFhMibJjeZRRo9S6noLT6UH57ssJ39X5NwFWQntcBqag3LAN1dMJ6FmRW9n6tbUJOvuVWWIurXSU092n7aQbkre0aoOxETVYbM5GDUbSQGEXc65vQAZ_DQdfGSYSfQorrmh9bqFhyYGexq-X9dtgYyQk_kFPcia2gt9PstcOHBCinub3lQHYBCVDkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029e0d7a1d.mp4?token=NGw-xxLoJaiQUtQCEu1BDz4ufcQm1CSEqL1oWaBYor1GcIKk_POOp3uRqY5nFLcWB8YcraPnFRgfCaaPE_V02RYhaTrvsaqLuiT96Gu43t-eTEUqqgos0ECROiw-bDfLvZOWeotfKnT2A0kyKXHh6VKbOl-R_hnefnDohuukO_Y66wDBNxtYiRQdSXWAJZ27P09Kn1Wm6KmUPE4qMJI5V2JVxx82C3R4AY9Jhei8O_FHAa8XuZl88ez681Vh0yGDQ6ySMGcsy7NSdvTFUjIdaiNM7IB8KPqBaNVHjqDfbjyx25PRUa6SIu1AelOr-ykrCmHZeAyHTnAUwkiK0EY0DYj9Ni6KCkNpMuI51AstNMm2nji45UakI1RG6-rBD6qmoLKEj2Uex_bzFrdZn535TUaysCscmAQyY1qx7TofEJhyL0eqViFP35dO3wQ_PUGf12AeYVm-S9DM48FUO2FrdPBVTHg0RbVmqSa3X3zDEw8tDxhAkqFhMibJjeZRRo9S6noLT6UH57ssJ39X5NwFWQntcBqag3LAN1dMJ6FmRW9n6tbUJOvuVWWIurXSU092n7aQbkre0aoOxETVYbM5GDUbSQGEXc65vQAZ_DQdfGSYSfQorrmh9bqFhyYGexq-X9dtgYyQk_kFPcia2gt9PstcOHBCinub3lQHYBCVDkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از آخرین وضعیت تنگهٔ هرمز و کنترل آن توسط ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/437207" target="_blank">📅 14:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437206">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIRjB92-2Fp8RoDmm_QN0U9TumI01uVRSr1RHfe8TIj5UfrZy4aoTE1kLphPFlKhQxtFRztChOqRcVTvwFwlTx9EN10YIyMt9LdQGlmmiESt2hyWBDBrqrLLpOsPfie16YwgXSAHrGyoiyg5gF4l0rG7IuftiKs5qPZbyQqOMB9DmY_ZtuLsUkJTVZNuo0n_4nbRB_ImyRL5B026qttHLr3LEZSYGv21M_CVpJ3iyB97rFJcRZvVusrsABF2R3w6EPZ4kpDQvXiYEJZFMFaHUIGx_9M6U1nlsmlX5dQeYQxzB-9qDKNi-xeOHI4-VmORz-zRV2A82iBhiiOaDfQBAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امام جمعه موقت تهران: دشمنان در صورت خطا، موشک‌های جدیدی را تجربه خواهند کرد
🔹
علی‌اکبری در خطبهٔ نماز جمعه: نیروهای مسلح آماده‌تر از همیشه هستند؛ دشمنان در صورت خطا، موشک‌های جدیدی تجربه خواهند کرد.
🔹
آن‌ها در صورت خطا، جنگ فرامنطقه‌ای را تجربه خواهند کرد و به جای محدودکردن تنگهٔ هرمز، باب‌المندب نیز بسته خواهد شد.
🔹
اگر زیرساخت‌های ما را هدف قرار دهند، از تمام حامیان دشمن در منطقه زیرساخت‌زدایی خواهد شد.
🔹
پروندهٔ انتقام شهدا باز است و مطالبهٔ غرامت و شروط رهبری قاطعانه پیگیری می‌شود.
🔹
دستگاه حکمرانی کشور اولین مسئول در زمینهٔ صرفه‌جویی است و رفتار، شیوه‌ها و برنامه‌ها در تمام نهادها و دستگاه‌های دولتی باید اصلاح شود.
🔹
در شرایط فعلی هرگونه تفرقه‌افکنی خیانت به خون شهداست.
@Farsna
-
link</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/437206" target="_blank">📅 13:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437205">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdxOpQOIlzCkl7rpazGgEDBU9-I4-uf5OGn5qm23r363x2pTJLxlZQiE7BKeYxjr1gj4SOHY3YfRcKBtC1W0vAvDMicMHu52bOmfUTpK6fkI5tJomkVwypuC8w9sX0aGH6rjiipZaDgsQltvRsE_QllpqdOKmP67z_OYNsDAq1lfT7JfjSiqtz46dfMbim9raEx07Nv0klKaJHX3J2Y8jTwWtLZtdX_k3vGGqw8yyOiviie3l2QoacZcPeQTY4VEdLwLIq71gYY96uXxypHVFA4enLHzG0CHhUej0ojcny3_tq87mk3dvzbgbCxNnitLuvqu7_BMjjMuicPNOoZbrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسارت یک میلیارد دلاری ایران به ناوگان پهپادی MQ-9 آمریکا
🔹
درحالی‌که دونالد ترامپ مدعی است که توان نظامی ایران را «به صورت ۱۰۰ درصد» از بین برده است، رسانه‌های غربی از خسارت دست‌کم ۱ میلیارد دلاری ایران به آمریکا با نابودی شمار زیادی از پهپادهای MQ-9 ریپر خبر داده‌اند.
🔹
به گزارش بلومبرگ، ایران با ساقط کردن بیش از ۲۴ فروند پهپاد MQ-9 ریپر در طول درگیری‌ها با آمریکا، ۲۰ درصد از ذخایر این پهپادها را نابود کرده است؛ این درحالی‌ست که جایگزینی این تجهیزات نظامی کار دشوار است.
🔹
بلومبرگ همچنین به نقل از منابع آگاه گزارش داده که تعداد پهپادهای ساقط‌شده حتی تا ۳۰ فروند هم تخمین زده شده است.
🔹
تولید هر یک از پهپادهای ریپر حدود ۳۰ میلیون دلار هزینه روی دست آمریکا گذاشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/437205" target="_blank">📅 13:41 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437204">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJSdb3UQBMsthw4-0l4Qb_IjW1ZotvBtOVyL2tAFlYGOY20wRcZZp_kYdLwc6kuaLwnIojzB3zL9tW94m-Pn4_GaxomM9ob09lpc3j7vAQ1DEoU0L0c_CVbFrDYrOq5qSsoPuFvWZK45qT4NvlFl4PkKI62NIEIbRQTePawU1Lqo7uIaW7mVWxoEB16r9ZeRqaBwETBp-IfgKCnGx0lq6zKfO8Yo-5yMrWMK8_zXm-NT8U3gMQW7suujqpJvJrApW2tj7eC_RS1n0hZd_rp8Mm31pFk2rQLXZdn3XBSgT93d37uTwUHUtl6Ud3v2i0Dk917cw1R58zC4C0qaIN0D0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرین سلیمی: خوشحالم با مدال طلا لبخند روی لب مردم ایران آمد
🔹
سلیمی پس از کسب طلای قهرمانی تکواندوی آسیا در گفت‌وگو با فارس: خدا را شکر در قهرمانی آسیا با کسب مدال طلا توانستم در این شرایط، لبخندی روی لب‌های مردم کشورمان بیاورم.
🔹
در قهرمانی آسیا همیشه کشورهای صاحب‌ سبک با تمام قوا حاضر می‌شوند.
🔹
ما در شرایط سخت و جنگی تمرین کردیم و هنوز هم ایرادهای زیادی وجود دارد تا به سطحی که در المپیک داشتم نزدیک شوم و حتی از آن هم فراتر بروم.
🔹
خیلی از تکواندوکاران خارجی ما را دلداری می‌دهند و حمایت می‌کنند. مدام دربارهٔ شرایط جنگی در منطقه از ما سوال می‌پرسند و اکثرشان نگران مردم ایران هستند.
🔹
به هر حال با اتحاد می‌توانیم این مسیر را ادامه دهیم و این سختی‌ها را پشت سر بگذاریم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/437204" target="_blank">📅 13:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437201">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac353f693c.mp4?token=TZLysGzp1fMaSnMjlt0DuMJFgS5gD5Te0xcOXsTMxHMYSN6SYFtplFFhxsoW1jziZJUVPjUKfs4JWXV3-WSWF06uLytecJ3GdjAY6miC7i6M0axX8Y4ylYEQYdQoTd4NfTGL3oVPwRA3F3e4QU0YVeQK5zT9aSmqFB784Uj1ngEChKwQADTbcZbCX5eIAo1Mp1vmP4bwlNDN1tNjxhyo9F5syHOTpQ_uhXsfrFtyXJpOm_J8TTv1LCLq94ByTX4mEdeRt69-d3ZyL_35bVlhyoCfxacDmOUqBzhjuHmVenr114sUmDwrqTxEiSoB2CBCyhq6iGlr4G0TpCXxygHCIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac353f693c.mp4?token=TZLysGzp1fMaSnMjlt0DuMJFgS5gD5Te0xcOXsTMxHMYSN6SYFtplFFhxsoW1jziZJUVPjUKfs4JWXV3-WSWF06uLytecJ3GdjAY6miC7i6M0axX8Y4ylYEQYdQoTd4NfTGL3oVPwRA3F3e4QU0YVeQK5zT9aSmqFB784Uj1ngEChKwQADTbcZbCX5eIAo1Mp1vmP4bwlNDN1tNjxhyo9F5syHOTpQ_uhXsfrFtyXJpOm_J8TTv1LCLq94ByTX4mEdeRt69-d3ZyL_35bVlhyoCfxacDmOUqBzhjuHmVenr114sUmDwrqTxEiSoB2CBCyhq6iGlr4G0TpCXxygHCIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌‌ای خسارات به پایگاه‌های اسرائیلی در حملات ایران را فاش کرد
🔹
طبق یک گزارش منتشر شده، تصاویر ماهواره‌ای از وارد آمدن خسارت عمده به چندین پایگاه رژیم صهیونیستی در نتیجه حملات ایران حکایت دارد.
🔹
بر اساس تصاویر ماهواره «سنتینل-۲» که شرکت «Soar» منتشر کرده، پایگاه هوایی «رامات داوید» در جنوب‌شرق شهر حیفا، در هنگام جنگ در دو نقطه هدف قرار گرفته است.
🔹
همچنین تصاویر، تغییر ناگهانی در نقشه توپوگرافی را در ماه مارس، در کنار یک ساختمان داخل پایگاه «۸۲۰۰» نزدیک شهر صفد نشان می‌دهد. به‌گفته تحلیل شرکت، این تغییر در سطح زمین می‌تواند نشان‌دهنده وقوع حمله به پایگاه در تاریخ میان ۵ تا ۱۰ مارس باشد.
🔗
شرح کامل این خبر را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/437201" target="_blank">📅 13:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437200">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">عبور ۳۵ کشتی با هماهنگی سپاه از تنگهٔ هرمز
🔹
نیروی دریایی سپاه: در شبانه‌روز گذشته ۳۵ کشتی اعم از نفتکش، کانتینربر و سایر کشتی های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگهٔ هرمز عبور کردند.
@Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/437200" target="_blank">📅 12:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437199">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c96a6d7d38.mp4?token=ilhxxSOwXTRzvVa8NNF-_4NKxFe4jbFF8buiqe0ypRrNgYic73G_c7Q6XEtRLtCmeJ7ZFfBq-z7XoeD-jfItEukFB7HqVEC8bN7SMi3kYC7NjkW3kYe9PlPPhbYbZcli1q428_kqIzREbUIweJ5VF4l-gCaELWYKGR-2CC28S8h3ILs1xEN0hVFjYtI7frmIbVx1AdFoLHV03smY9SNrcRL_dFxv9HrgilNtLyGsMfbW99vufhMbOXRQa3PBIJsNR064ecHGVDdrmQ5LfhQWC7EWV08Ob7mPe-teJ4bPba714msshud07Dv9yP28MINUXVPLUzhIqwZmV-7Yf7JZHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c96a6d7d38.mp4?token=ilhxxSOwXTRzvVa8NNF-_4NKxFe4jbFF8buiqe0ypRrNgYic73G_c7Q6XEtRLtCmeJ7ZFfBq-z7XoeD-jfItEukFB7HqVEC8bN7SMi3kYC7NjkW3kYe9PlPPhbYbZcli1q428_kqIzREbUIweJ5VF4l-gCaELWYKGR-2CC28S8h3ILs1xEN0hVFjYtI7frmIbVx1AdFoLHV03smY9SNrcRL_dFxv9HrgilNtLyGsMfbW99vufhMbOXRQa3PBIJsNR064ecHGVDdrmQ5LfhQWC7EWV08Ob7mPe-teJ4bPba714msshud07Dv9yP28MINUXVPLUzhIqwZmV-7Yf7JZHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ پهپادی اوکراین به خوابگاه دانش‌آموزان در لوهانسک
🔹
حملهٔ پهپادی شبانهٔ اوکراین به یک خوابگاه دانش‌آموزی در منطقهٔ لوهانسک دست‌کم ۴ کشته و ۳۵ مجروح برجا گذاشت.
🔹
کمیسر حقوق بشر روسیه، گفت که ۸۶ نوجوان ۱۴ تا ۱۸ ساله در کالج استاروبیلسک دانشگاه تربیت معلم لوهانسک در خواب بودند که پهپادهای اوکراینی به آنجا حمله کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/437199" target="_blank">📅 12:44 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437198">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aec72b07f5.mp4?token=bSmoqXwvjBpGKlWwF9UWuHAsH55HFop8bbCYOYUS8AsgHJfwPiUs6yEBiduW249PtPM5dvH74AIMFLGID5riU_WsSdNdfJjbY-rbXq522f10It68OQu-cRsWS9yLoiKk7VMDiEHQqaBBQdqhEPiWR7ubOdZNU9J5gQFT06HOp4IoAiNVUIcp-c1Cww-uIbtjBMA2qq7hHbBRLJ0zKQXiAXwVYLlA-h-RhgxA93om4Xkaf1Jn_LWl8LOVdTdIcsH_SmVIO2HoEE3hK9GGOnUMGvVBXn5CVSiyhTCKVdf7vxKLH5wK9u-y5ixmCzvUiY-51-oQ59FznoYkZjg7Xqzj2nllYwePOYwyAxVKJZjfpmyhDEh-aHk-hDu3gN8n1XZ8LXjZeVLGdTU4KKwUoZuTcoI0ZKazi1VY33coF0hqbbJG04yuh8T6Z3NyC_20lN4YQ1SaCqJeS3Ch1JYQSfsMG2HPZVPhPqn1HFVUEyGE0cbV49IWkNYS1IpOFrPDoFh8ggRnJ5xYEUFCaIGrHvpkajGPDPsvSwLZR7UVmPhiPH9BG9aFUQokR_qQyv3e3Zy_aPXjB2mX1VtjLP5F78RFVPW0EQvyE6WpU-DSJcSYjkAFcyzonOBlqLUoWb8mEuhEpc0GH7fvJK3PNhKkUVSdJwxDVIXmudGQRUKQLcNDOlM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aec72b07f5.mp4?token=bSmoqXwvjBpGKlWwF9UWuHAsH55HFop8bbCYOYUS8AsgHJfwPiUs6yEBiduW249PtPM5dvH74AIMFLGID5riU_WsSdNdfJjbY-rbXq522f10It68OQu-cRsWS9yLoiKk7VMDiEHQqaBBQdqhEPiWR7ubOdZNU9J5gQFT06HOp4IoAiNVUIcp-c1Cww-uIbtjBMA2qq7hHbBRLJ0zKQXiAXwVYLlA-h-RhgxA93om4Xkaf1Jn_LWl8LOVdTdIcsH_SmVIO2HoEE3hK9GGOnUMGvVBXn5CVSiyhTCKVdf7vxKLH5wK9u-y5ixmCzvUiY-51-oQ59FznoYkZjg7Xqzj2nllYwePOYwyAxVKJZjfpmyhDEh-aHk-hDu3gN8n1XZ8LXjZeVLGdTU4KKwUoZuTcoI0ZKazi1VY33coF0hqbbJG04yuh8T6Z3NyC_20lN4YQ1SaCqJeS3Ch1JYQSfsMG2HPZVPhPqn1HFVUEyGE0cbV49IWkNYS1IpOFrPDoFh8ggRnJ5xYEUFCaIGrHvpkajGPDPsvSwLZR7UVmPhiPH9BG9aFUQokR_qQyv3e3Zy_aPXjB2mX1VtjLP5F78RFVPW0EQvyE6WpU-DSJcSYjkAFcyzonOBlqLUoWb8mEuhEpc0GH7fvJK3PNhKkUVSdJwxDVIXmudGQRUKQLcNDOlM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش ۱۰۰۰ موتورسوار جان‌فدا در تهران برگزار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/437198" target="_blank">📅 12:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437196">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6vaJeCXoGEkXzjOU-n9tv1itYtbs1VZIZG-cyYMynLoc50ubxe5cmNf4kG3HF6Q_7_BZK5uOe1n-zkmXj7Rs9ub3pPhtHT3gTFpx9smjPvkdQNNxVAngKjJiAg-1AcQi8X-eOig5GG1FovmdOFG-JMKqkj9y0HiOxPQQ_4hGzhYCuyKeTy6FHPjRRjlNx27VdBOZxSrZD6dKZeCiToKXn2DRPcEi7YBR8MBlEB2oQ8bic4DhTNB_D3egCsdbpcoCyjkFsY5p9GsuzQ6EvQmdRIn7ggkQM5uEtWEHuY14zxBAgX9raZVdz8x5rViVSBrWktdp4dhrsLJfYonbqefmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVQu71MJCPEOGWze0BSyv0DZJw_y7Lx_UYKqJdkYZhhzlh1QspwwboXp_Tha9yTuWNFDj2mH4Mk-9A15daNJyUBXSy_bmGB2QlJrTFyoX-ECjuz9CYHbS9a0_Xad2GudMk_f2LPEiS8cxXt26Y9mm0OeeCE_UoMDZ4sq9XGwcGV_iCKkx_ZlFId8yslO6Jq-VYpSaqsDOLXWbjro-U-HlkYNJwAy-AaOt8gv2Ks4ViXzJxUBTdv3dnJDU2tzAEu4BAFM8dWeDvkzK0RcCUza-Opn1JdKZ0V2ZrlNzn_4zH1hl1eqeQCxpd7-KX3z76b8EYRENlhVFE-iEsBi2P6g-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تعرفهٔ گوشی‌های بالای ۹۰۰ یورو به ۳۰ درصد رسید
🔹
براساس بخشنامهٔ ابلاغی گمرک، نرخ ارز مبنای محاسبهٔ ارزش گمرکی گوشی تلفن همراه برابر با متوسط نرخ ارز بهمن ۱۴۰۴ در مرکز مبادلهٔ تعیین شده و هر یورو ۱۵۵ هزار و ۱۹۶ تومان اعلام شده است.
🔹
همچنین نرخ جدید حقوق گمرکی واردات گوشی‌های ۶۰۰ تا ۹۰۰ یورویی ۱۵ درصد و گوشی‌های بالای ۹۰۰ یورو ۳۰ درصد تعیین شده است.
🔹
این بخشنامه تأکید می‌کند که واردات تلفن همراه از مسیر مسافری نیز تابع آیین‌نامهٔ اجرایی قانون گمرکی خواهد بود؛ همچنین واردات از مناطق آزاد تجاری-صنعتی نیز مشمول این مقررات است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/437196" target="_blank">📅 12:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437194">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nl-ERu1OpoBrNmjLgUatF2uOuScLqz0sKmQd5Q9R2AgfuDs-P3wTURftuwTuz0qba4VwD3lvRjflIysnxO3jv82RoHh5rkX8jDa4QTylrA3jtGL4Tl9q8C6-6hzSW-yt6nlfRUDi3mNBFv8WHO7dBTq-1EEoeoBP3ivKpcd6-2JQbDGreXyIQwA5J-TI3PEodiVDjwEwEMYPyrmxMM0jT_olDX-Q0ucYLoxG8FIOK8qNBYW6lMo5uBP0fgCW6-HzKKTXWuUX4RfBzryD-n_flzXbR-jp3v81yzZvhrxtWs4OlN_11DZ2QFAnvC0HVMo85ih1vJcVGYat7pw0ORNFCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SFDlrdduWakOEC1FCwjs-EJJMx2R-JkVu4ywJbKlzTXuKrYJ7gPd2OMP_yWuyoUPpAEkfaKqm2w0rGMw8OjpCT1ek3p-YmL1S0MSfXP5wNdh2_9Ji50omrbWJuamPjBdeGi7Nz7FxGgdm_X_xveJgknSVqw_7ODZFSxJM9VRhcnYnjR5phqTmryJT9VrwbJQXo0byyMag6_8tTLTWhAWJF2JYb9XQ-T1PKgCtni7cj7PKDkCu1MZXlFt3pySClH6Llazzug1pfYWfHihE6jfrVTkyZ_JXyqixhK4ctSbAalLJ_MVTZVlsLSQjE6fyeNW3sRY2s3pBNjNYlUa8EcTQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انفجار مهیب در بزرگترین مجتمع پتروشیمی مجارستان؛ دست‌کم یک کشته و چندین مجروح بدحال
🔹
وقوع یک انفجار بزرگ در پالایشگاه «الفین-۱» متعلق به گروه MOL در شهر تیسائویواروش، مجارستان را لرزاند. این حادثه حین راه‌اندازی مجدد تجهیزات پس از اتمام عملیات تعمیر و نگهداری رخ داد.
🔹
مقامات محلی اعلام کردند در این سانحه دست‌کم یک نفر جان خود را از دست داده و هفت نفر دیگر دچار سوختگی شدید شده‌اند. هم‌اکنون آتش‌سوزی گسترده‌ای همچنان در محل حادثه ادامه دارد و یک خط لوله آسیب‌دیده در حال شعله‌ور شدن است.
🔹
شرکت MOL از طریق خط لوله دروژبا به منابع نفت روسیه متصل است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/437194" target="_blank">📅 12:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437193">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">توقیف اموال ۷ نفر از خائنین به وطن در ایلام
🔹
رئیس‌کل دادگستری ایلام از شناسایی و توقیف اموال و دارایی‌های تعداد ۷ نفر از خائنین به وطن در یکی از شهرستان‌های استان به نفع حقوق عامه خبر داد.
🔹
اموال توقیف‌شده از متهمین شامل مسکن، خودرو، دارایی های بانکی و سایر اموال بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/437193" target="_blank">📅 12:16 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437191">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTcUefUUGIY0XWDWq1ajPfxg2C3bf1LSvTVyiAo8qSmPAST9kYEu-4PFrr1nuebZq5lI5nm6FM4WqrStmY8QSzk2uJq_BmTbSlpKCYoKkwIo-B7g16w6eJ936x-5WmeyDvX1Lt5LlU3-yoRUeo9iDgvb7eTYUlrGvAqj88VIcUZhQeaPiQgM3VvmIJgpOeixRTnMPKEMkZRod__g-hhP-TvAPkzk1NtcXzlrOgRbWfImceZep-z1hIITG_WIBXyldX5lujBx1LgYBz4mCGpbDSyTkwVprZWK8rn1hB1ZFYbrarmJf6dBF8UGXPABFe_chH3ylaNYwg3r9Dl1_vJVyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M07-e1UEy-eY6bhtok-x4lDYZuYf8YFxnrU4j_u9BGNl6XXMc52lXR8MQwoKVexirEXWJEiBNhyvP4RrB1h5NYqrH_K1LSydNBytdl5NITm6vdu0FGkM-LBaUbDGYIRf6jCqLAqfyY_hviXsRX4dfZ5E2rEvU1c-epfQDirXOS8PdVHdLtDYzIF2IN_km273TEgi4Ju3wn0smguUCG1sfmvk5VwgtK_Wbgg1j49vb7p-FyAaWlguSBnUfAHho210KtimS5vnz473KQMDTKABpqTs6w8NCmRbHszAR1GoiddDCqgM7sARnNHM4uw5v28r6Zd4RDai0lpdZzvyYQEKwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلیمی در ثانیه پایانی طلایی شد
🥇
آرین سلیمی در فینال وزن  ۸۴+ کیلوگرم تکواندوی قهرمانی آسیا مقابل رقیب ازبکستانی برنده شد و طلا گرفت.
📊
نتیجه: راند اول: ۷-۷ برنده ازبکستان راند دوم: ۶-۳ برنده سلیمی راند سوم: ۱۲-۱۰ برنده سلیمی  @Sportfars</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/437191" target="_blank">📅 12:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437190">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlUT7Go471RcsNK9YPqgKjU-lbGAD4YFRJnxEOUERra2XtYW7p-Lw-9cUGGThGjD_1tf_wwjiivmIKEg1_svvAHNvZDOIZfIQySyLbTllMaL-1396YxWc3BhfTgVbqzX4eHn7OmfrxIDEo2azKUvh4kvz2Yu9xsC1Om76BeMcWmHS3oHA9ZznliDAJKN4c-dnRitrPrUfPITPjA8Zm3ro94Jb0nTgH2Z19HOqeqnVWAyntWrVI2C9xMrKGyYL1aFc0e2nBlC40rK5sqB1jJXo-w8Hc4AWtHLSuMQEm2AB1WwxDHhsy63QHD1Wv-zN4U1B4F2LDLVbAzPUYSHYkQt5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن‌پست: بار اصلی دفاع از اسرائیل در جنگ بر دوش آمریکا بود
🔹
روزنامهٔ واشنگتن‌پست: طبق ارزیابی پنتاگون، آمریکا بخش زیادی از موجودی پیشرفته‌ترین رهگیرهای پدافند موشکی خود را در جریان جنگ ایران از دست داده و حتی بیشتر از اسرائیل برای دفاع از آن‌ها از این موشک‌های پدافندی استفاده کرده است.
🔹
به‌گفتهٔ ۳ مقام آمریکایی، این کاهش پدافند موشکی آمریکا در منطقه به خوبی نشان می‌دهد که آمریکا تا چه حدی بار دفاع از اسرائیل در برابر موشک‌های ایرانی را به دوش کشیده است.
🔸
آمریکا بیش از ۲۰۰ رهگیر سامانه تاد را در دفاع از رژیم صهیونیستی شلیک کرده که تقریباً نیمی از کل موجودی پنتاگون است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/437190" target="_blank">📅 11:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437189">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/083c1c9cb6.mp4?token=iyUk7DDqmG6UI7BqNzSbUVAwRwTUFtl72bt1iyLaUEUVEl6CZuMxomuowdcFrlvTw-yTLm6h4LbVNe5FTISnIufrB_Q3WdpdC5yBu8cOHh8l5oT_tiykOrVctlWx8mR1AaLFT_nb4r3Dq3TdBauZHRnYAqiM9-vFgLDO4tvbgXsB3fMv8ecLOZkkPgkon2QdyzFbqpcv06QITP9W09_awfgQWw_msCzkg4h5XmQ4QhfrUApp9Po_WyKLkzjiqHJ8D0-pvqNHMs-02vEuAGeMeD8D_6DR59RSlIeyvQuL2K2rq3J4uRCIU1P81-xZg-r_fAa5Uklzsxxbmcr6PEHbZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/083c1c9cb6.mp4?token=iyUk7DDqmG6UI7BqNzSbUVAwRwTUFtl72bt1iyLaUEUVEl6CZuMxomuowdcFrlvTw-yTLm6h4LbVNe5FTISnIufrB_Q3WdpdC5yBu8cOHh8l5oT_tiykOrVctlWx8mR1AaLFT_nb4r3Dq3TdBauZHRnYAqiM9-vFgLDO4tvbgXsB3fMv8ecLOZkkPgkon2QdyzFbqpcv06QITP9W09_awfgQWw_msCzkg4h5XmQ4QhfrUApp9Po_WyKLkzjiqHJ8D0-pvqNHMs-02vEuAGeMeD8D_6DR59RSlIeyvQuL2K2rq3J4uRCIU1P81-xZg-r_fAa5Uklzsxxbmcr6PEHbZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت معاون اجرایی دولت شهید رئیسی از کار انقلابی شهید جمهور در صنعت نفت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/437189" target="_blank">📅 11:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437182">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t0hfofSnZr-xPGW9R-1gx1sTpPLB3exTHP0LmyCDWAxEWjjBRCarJ-3XtWqtIOl7UyS0iLIEyXEq-ob63pn7bF9Rf0bcAmJP-5zklaOIERSrEez3q1UDzTt2J0lesq10A0KYOPfgNZEIR2xkb0nC2lm1vvRo_hY_UEkkIujlcPvdUbKAN5ocfL2JPGb01j8LXXiGS1vTbz1h9rq6eAFN4eQoNhw1NosnAyzprDBmy9dgpdYnbqtxHV8meSauEQR89upc1p57IACXQVAu0fOVr3MTDdbsnynhyp5QXPamR_k4yp0-fA7OO60xYycOObZjyYdSkLhxgUfE194V-qWXhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NdYMLzmec4mLnwdmCJk1t469Ruzc6vN9ZBuaF--5s7Pwk0tbyfaEzQEFPoGeCwVxASWkTmbgbZ9SYxSbr5cBlwFM99nyPvcNurtO9faw1uUhTZaJy_avXjzCs76_vI3ao7-fnwl_prQ8Vl05WyYik9xxZjK89WKomYsgjXtxRMRFEkdOm3Xnx1vc4j7NLWZ7pCLilsssLGGjxEXMzmcQxhu2hw8qnPDUxYiG1FZkCM_ElUeSrRrwHGX7leGhgX2uTeQRbqTWZhbnK9TcwWht9JqxYa4l4bRVw37KnZt3YTjgPJy1ZS18O2-c1mc22-pewnsGGdrR_GzQWN7c5IgvRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-85k1yXms3lPX0B9kgaZ4kHDcTqdB5Mdo1w8DP3HulWD7RojEBNK_O-nlP5ajuodu7Mc-Y4k3irBvZ4pz70OJMHS8Aen7356_SEetFfxUc9WQJ_-6efPseX5euR50-klBDMKv8JvDuTGy18s6rA99HgRvFGZMOJH6hedzM8cpy-cO30GQnXkqu7ax9EEx4sWRLB1zRzNM2yRNTkX7Pnbsy0nfa7SyplwIWpaVU_iUqzZutJhorap1C1ccXtWbLy0zKC7CNSujxQfwMSYOB65z3ePVXBt4ZQCpDqXV9GVa6TcAJcKx_owpwvEEEYSBr4s8OtLonAVSSQ5wSwLF30Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWuipNwza3Y2wXJwY6JXZIY5KJk-r3bXFJNjJcRYI0kx9RM3Ks3JRGuMXdSKD0la32ppLiozrfUATCWu9M8GczieEgmq0y_PX9-Q5B9RTUprAnhcEFKsac6W7T5E9CIRo37xJHvVLdDmD8cFt0xxjxNCjGw9kczKQnYPdirETCFIUUTFEXgxAxLM4E5QAWZeLTCdcLWj378AB9kabZ_bh8yZZSiyDBRCiMwP0AWcF36qG2mG5ChNK4CUc2HWYLsHg1UlcztRj2Yr_o_DaxcfM9hmeoNjmYP6fXe7nSHlbHh1TqK97WOC1ZMHRd3fKMAJFkdu7H1le79Cdv6bKGMr4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/diN8WdXwS2JiZbkJ8taFtxYz0oUmpLBjkn66om7jzpxr8LVZPJOKbYx5G68eYwXMDI2Tb4ZOFbOjU7d2q1PwsDCOLxEsQc8kFR8Lfwg7JOc_19kIP7Ojgta8y68Yg2Xuz7i03Oy6k3_GJgB1hJzYQ5ABNywRKCj4VXwT8KwcYp2xmayd-VXhZGOzsbvXwb9kFAstFlf6DOmtTE6Vffhpoz2oCg_6HmwtIUtmmqVoIuiThI9TXH0GRIKTIA6vO7X8fk0sq7ORh3bu-HC7Ixg4qF5IaLYfZPLbuJMO3hH5Jz6XN708s8kPsaP7Bzjz2YHMwYADJAq3OhDypKKg2cSnEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eVPvALvEV0xFG9iokO51YLgqjDxD2CVOlNrN7VZ291ss6A9LPqttcMp7aQhR1DGrzrUbop-65n4fEfDlCg_MSf9LS2PXBML9DMiBTPItnfXI8aT8CexlYBl7B5_E8MAZgxxOXUmxRwJ693_wqvyr1LmQU731uMFc85QJfHjCQz2HmGjuwbW-ObJKrlCAzV062QCAqUo7ePheeGJpzN-z9z855TzsNlYudPr6ZbdPd7DXa3UUOqQsWkdyA8AKEbDZjC7aUoBxD88YSY3mpYKTjluwR0i4yxTmkljFLU-gBTWuohDFIbF5FNE8wl-BhkiAX9kjfHRBbNa3BNg_-MJQFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YJw7Axk3QefKazMM9UTSRebeBYMgpARnFpsdpQ6Sjc4DBxummQIZPdxP85mRBYbafRbLW7pbBo42QYAB50u7qJ81N9B0cb6q0LoWiqMjptk5z-p6YyWA4dsaEJDqlnD4ONI_bBBinnmBVWehazQW6DZzBX_oU-AX-qvj9Y3rmtcxjBgRFK-n1z6yq8KyaFQr6nWaz6lWjRT8nkHolq6RbO5UgCDXnJnzmaDM6TvQSOJIy4WqRHlYniRLadE65LqYtYT3xW4KmkOuqQsjiTVKNN_S8ytbFsrSdF_RFqnGbaY9Fj5bbI4Lr8e99hqoPyic1DO3PdBCzHTZ4ypiJAc1Fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بدرقهٔ طولانی‌ترین کاروان پیادهٔ کربلا از مشهدالرضا
🔹
کاروان پیادهٔ انصارالحسین(ع) امروز حرکت معنوی خود را برای بیست‌وپنجمین سال متوالی از مشهد مقدس به‌سوی کربلای معلی آغاز کردند.
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/437182" target="_blank">📅 11:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437181">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یک‌طرفه‌شدن جاده‌های هراز و کندوان
🔹
پلیس‌راه مازندران: برای ساعت‌ ۱۴ مسیر جنوب به شمال کندوان برای اجرای محدودیت یک‌طرفه مسدود می‌شود.
🔹
حدود ساعت ۱۷ از پل‌زنگوله و حدود ساعت ۱۸ از مرزن‌آباد به‌سمت جنوب یک‌طرفه خواهد شد؛ جادهٔ هراز نیز از صبح امروز یک‌طرفه شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/437181" target="_blank">📅 11:28 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437180">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خنثی‌سازی مهمات عمل‌نکرده در خرم‌آباد
🔹
سپاه لرستان: عملیات خنثی‌سازی مهمات عمل‌نکردۀ جنگ رمضان فردا از ساعت ۸ صبح تا عصر در خرم‌آباد انجام می‌شود؛ مردم نگران صدای ناشی از این انفجارها نباشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/437180" target="_blank">📅 11:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437179">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace2e0f59f.mp4?token=iV-wB31Q0ZzWnzK14JwJjerXPzIQwo4vD-0NuY6d9MpQzijoRLHssMH9zMAzqOJSjKpOWq9iJmabofC9cr7R0j-hZCWQJwNorYuEkU8chs1misMcdB99ERgEB8llwu_iNCBYsp6ZYZrXwftT8micDxfOyY5DClITBmf3AR88101XJNWy1bLmpwm-xSgZlAk7waZ4lxK-d-7NGHPbqwc0zOiZSd2lPALqhYDWSETgpnKE0Zh2IgWh3I68s2JttYDpWIWwKz3JKM69XM4p3ufj6EWIfF3I7FPXpv6W34yzk-oRKzMr3cOym8h55pYcwuAslo_kaAu_9lPs8GbHDQJ7HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace2e0f59f.mp4?token=iV-wB31Q0ZzWnzK14JwJjerXPzIQwo4vD-0NuY6d9MpQzijoRLHssMH9zMAzqOJSjKpOWq9iJmabofC9cr7R0j-hZCWQJwNorYuEkU8chs1misMcdB99ERgEB8llwu_iNCBYsp6ZYZrXwftT8micDxfOyY5DClITBmf3AR88101XJNWy1bLmpwm-xSgZlAk7waZ4lxK-d-7NGHPbqwc0zOiZSd2lPALqhYDWSETgpnKE0Zh2IgWh3I68s2JttYDpWIWwKz3JKM69XM4p3ufj6EWIfF3I7FPXpv6W34yzk-oRKzMr3cOym8h55pYcwuAslo_kaAu_9lPs8GbHDQJ7HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گرینلندی‌ها علیه کنسولگری آمریکا به خیابان آمدند
🔹
همزمان با افتتاح رسمی کنسولگری جدید آمریکا در مرکز گرینلند، شهروندان این جزیره با تجمع در مقابل ساختمان این نمایندگی، مخالفت قاطع خود را با گسترش نفوذ واشنگتن فریاد زدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/437179" target="_blank">📅 11:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437178">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U40XGPQNInJE3SnSNdJ-uiv-kJaUZrdKunzo4Bql8_I7IS4ZhhTP7GOA6rPGeJ6wAZ_LjiPC7M1LO2dIpkelQFosVPYUr5AVqKxcERuyIRsnlYYBqEK5nBhK8A_Nub1HKU24dNZMqRE4QHbHCB6M5ywoGdnYlJPRlMQeobzEZhQODebsFJU7gmuBIVc0qye4kupjbqxZHfdvFDOJxEXUPKPTIsP-pcBLe7Nxqbrd5nQ1ZvEIUfhTPRwcPv5ewNihnBLZZItvC2tkQmvqbzVXnMBSUoAGdqqCT8q94V9x2CQMO9wTGLZ8vIhvlWkmo1kjOK4qzrfZA3qhDYQhq1ecYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثهٔ امنیتی برای یک نفتکش در نزدیکی یمن
🔹
سازمان عملیات دریایی انگلیس: یک نفتکش در ۱۸۱ کیلومتری شمال سقطری، تأیید می‌کند که یک قایق کوچک حامل ۵ نفر به آن نزدیک شده است.
🔹
تیم امنیتی مسلح نفتکش با شلیک گلوله‌های هشداردهنده، قایق را مجبور به تغییر مسیر کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/437178" target="_blank">📅 11:09 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
