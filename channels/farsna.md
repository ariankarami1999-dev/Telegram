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
<img src="https://cdn4.telesco.pe/file/QB2CxLwPBFIUgX9LU8AuAHjfVE4ZUugFVRPKJ2lLpZz0PWdrsbC9_fBaYuIB6cXXTAsaZRIoh271hOhyqzeiyZAPymb-v4FKLVdxF630qou_-apPfZuTFTesCccIfSnpSBwtFvLQeFsW6pkHfjPnKz2d7VQoaBpwutT83YBnjssCDUjjWlC0uVgvQSRnAVU4WxC_SIvVJlHtiPQa2qAq-flMU-NJHgei2BDnxzHaEebjwWb2BE-Qs9ka-ZNcORnDdDwDW7N9RhXa8vVSDPMad-HijIqBx8rim5rWgh5_JC45YSiRj8V_tYSsqNXD8RKVTHoTVA1n6tDHOEfIYccbTw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 07:13:44</div>
<hr>

<div class="tg-post" id="msg-447353">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d381a31e.mp4?token=ePdcasfi_VoRevNSrpW0DFcfbdDpzxNIKWPucb-aMwxAxQGhbDYlHQiSo3_XThGMnBwhiRfU8WkMSKdvxMY7pzG1tE-edCacth_RYP759H6x-FsjXNPX11F6E5S_pqO_8l2K5607sSVE2coxAgg16HOf3lQAFBIhaKldOuqg3xqodheeMjgqr60fSjMvEBKmE9JDovQgk_Vw8q-nCCf82fXXnFBWqcmaqieUESKUOI3g9N9WMhNI3Pz5s-uu-iSr17VLuqhjnIBHlKEBYa8z5H-iLkNEFOqn13BF22nOUuKfVHPSOVEYSkyZd6xZieyfcdepFH_nMM6TG_wMhSosFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d381a31e.mp4?token=ePdcasfi_VoRevNSrpW0DFcfbdDpzxNIKWPucb-aMwxAxQGhbDYlHQiSo3_XThGMnBwhiRfU8WkMSKdvxMY7pzG1tE-edCacth_RYP759H6x-FsjXNPX11F6E5S_pqO_8l2K5607sSVE2coxAgg16HOf3lQAFBIhaKldOuqg3xqodheeMjgqr60fSjMvEBKmE9JDovQgk_Vw8q-nCCf82fXXnFBWqcmaqieUESKUOI3g9N9WMhNI3Pz5s-uu-iSr17VLuqhjnIBHlKEBYa8z5H-iLkNEFOqn13BF22nOUuKfVHPSOVEYSkyZd6xZieyfcdepFH_nMM6TG_wMhSosFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با توجه به حضور گسترده و پرشور مردم در محدودۀ مترو دروازه‌دولت، سیستم‌های مه‌پاش جهت رفاه حال مردم فعال هستند.
🔹
هم‌اکنون، دمای نسبتاً مطلوب و هوای مطبوعی در این محدوده جریان دارد و تردد برای زائران تسهیل شده است.
@Farsna</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/447353" target="_blank">📅 07:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447351">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e601d07abd.mp4?token=dalISB_0vdaeANKFUr_CnJ_KlY09nNMK0PCo_UYx2Z0LgO1NovxjDzn7RGrxBIR3PiCWrXpOtyzcQO1U8wIs0_tecc5tLz4N_e9E4mFZH1Mqm9jxG6tXyoAyqmkmy0LUmspw2tG4feMcKCKwDjYR_rvQKIK9BSv-2VxUXbXSKa75DCsQyvLtEgdHoGW2smbtRbc7DKiBe7oREmN4WmVS2AMPnwNTVUVPS6NFh7Cv1MCvK5urQ1WWbpy5v8X3kLWNatC9AM3tamY7arrnXXu-dDTA1MAyT52lDWD0ChknEbdO7GgTvQzPhTjgZfLX1_AQh_lfchnJBbZO_0ApZBCLBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e601d07abd.mp4?token=dalISB_0vdaeANKFUr_CnJ_KlY09nNMK0PCo_UYx2Z0LgO1NovxjDzn7RGrxBIR3PiCWrXpOtyzcQO1U8wIs0_tecc5tLz4N_e9E4mFZH1Mqm9jxG6tXyoAyqmkmy0LUmspw2tG4feMcKCKwDjYR_rvQKIK9BSv-2VxUXbXSKa75DCsQyvLtEgdHoGW2smbtRbc7DKiBe7oREmN4WmVS2AMPnwNTVUVPS6NFh7Cv1MCvK5urQ1WWbpy5v8X3kLWNatC9AM3tamY7arrnXXu-dDTA1MAyT52lDWD0ChknEbdO7GgTvQzPhTjgZfLX1_AQh_lfchnJBbZO_0ApZBCLBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یزله و هوسۀ عشایر عرب خوزستان در سوگ امام شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 711 · <a href="https://t.me/farsna/447351" target="_blank">📅 07:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447350">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3a8c2c68a.mp4?token=AWNMAWEoMYCdvRYaofnturYw-q_eKvVHvmHGVtDvVLCCbJPoBltKMoEScqA5gaQHnuaFo1w530ycwaw4meJDHFiT2xIbRrYmn4MeVPtIKJ5TFgczCxkpRBecpy2DcOpn0_NZnJcqGHXT8TcGE1Gmn7Ex76Si_GNwaJKVqP99jF4Q2mO6g6g4QvmDL86SiSkbV9-qJAisMK6n98SWtVcUJOAwCN58zGhEYkO7Hz5sDCp9SFIYmeOFJ8qzLaUZfjNcjyEEYz6yHriTPtw2A4Gnv6NAfD1ExZ4JWrVpjG6aaRKEUYqGR5cxu5CRQjHMIXEioH75foT1QsM-JdsOW2hgHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3a8c2c68a.mp4?token=AWNMAWEoMYCdvRYaofnturYw-q_eKvVHvmHGVtDvVLCCbJPoBltKMoEScqA5gaQHnuaFo1w530ycwaw4meJDHFiT2xIbRrYmn4MeVPtIKJ5TFgczCxkpRBecpy2DcOpn0_NZnJcqGHXT8TcGE1Gmn7Ex76Si_GNwaJKVqP99jF4Q2mO6g6g4QvmDL86SiSkbV9-qJAisMK6n98SWtVcUJOAwCN58zGhEYkO7Hz5sDCp9SFIYmeOFJ8qzLaUZfjNcjyEEYz6yHriTPtw2A4Gnv6NAfD1ExZ4JWrVpjG6aaRKEUYqGR5cxu5CRQjHMIXEioH75foT1QsM-JdsOW2hgHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل عظیم مردم در ساعات اولیه بدرقۀ رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/farsna/447350" target="_blank">📅 07:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447349">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/367cf4053d.mp4?token=n5EDZceBZAhBlA6Jj7XurJ_5_7gqux5tP-zN7mAnh1hcjkjoIbhpyt5DEzAhgQnsiggK_PJV6ZgFRMXVAnC40gW3oJlZqbMWNrliyFTxDr0tirg5jXLxadtOQgspfgVJbbYe7CvQZ18zP0i02UUcXESdcGDR3SIrsU-gQ9K24vZlk0Wevr3_HvNA8BxoOnpoqv6PojzCKCfanzYEFjSF07qVwOBIZW3U3Yvwp44ubfA42X9BsLVPHwmcaIZEQigoe9R-S5K1FJgjxRhWikXVmh6dPAZXOsYmAo2pK7EWmovnXxZjjjCDYcq3Kyi5TT3WJIE3oVzeJrZELFaQ4PVwog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/367cf4053d.mp4?token=n5EDZceBZAhBlA6Jj7XurJ_5_7gqux5tP-zN7mAnh1hcjkjoIbhpyt5DEzAhgQnsiggK_PJV6ZgFRMXVAnC40gW3oJlZqbMWNrliyFTxDr0tirg5jXLxadtOQgspfgVJbbYe7CvQZ18zP0i02UUcXESdcGDR3SIrsU-gQ9K24vZlk0Wevr3_HvNA8BxoOnpoqv6PojzCKCfanzYEFjSF07qVwOBIZW3U3Yvwp44ubfA42X9BsLVPHwmcaIZEQigoe9R-S5K1FJgjxRhWikXVmh6dPAZXOsYmAo2pK7EWmovnXxZjjjCDYcq3Kyi5TT3WJIE3oVzeJrZELFaQ4PVwog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی از خیل جمعیت با پرچم‌های سرخ یالثارات الحسین در میدان انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/farsna/447349" target="_blank">📅 07:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447339">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZHjS7hc59M7_VPoHw6zRFtmHA-RGMTo_TEcp6maGtrCpuFNY4MfGp686ZsFXfXIyPS33zDtV_Jo7AkoJ3vi9fsA9BT7a6-ytDzwfc4pna90YhybhAD8m4fxQ5gxXDDBAUECWFSy6vYuSJ7Dm2cbfudL4LoeUR4NLahESyrHCiyfeiOgtYAoe1URthaMdFEQ8bb_cnAiwlmqDM1w8OnY11FcEFg4dt2TXaHj8fY-aUVIo4MpIZ7Ku79qyjvWzny3RFX3QbumITwtPg5Gwghgn7q8h9ef98Fa1d_IB72E07RnmsrcU2BLA-thHr1HvqlQWqEXYoHAFLavDmL8k8wgvOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DE7QScq8VuVyOkWenIca3ynfe8SqvtBxZtvDXsIsvSLpebEW1zpv0YKNZOHGqNVjgMQMvcmXPujuxon736llhjfHsaFHAJ2ipCOQ3O2CZEZQ_795X2Y6K41g9vL1NAKOTzOXJwZh6vTepwUy_lUSQuQHU3kcx1OXxGAZJpyvsF9FLAj6kH3uOCk7tb2wEbB5vKTMs5xeEQFX4pjIbbUGk5zrbNyUgogTVDbuFjmJuIIAIWt-2SC4O2W2I2ccuIbHASbjnKIwcM4a1yrYo16O3ZRYyh1AmK_CQuUTMRKFEy99KDvwpBxBLL6blR6n3z7Z70xIsbOWrTDdTt8TzqWa4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-VqoQAIMPKt9DVcRdntZR2E3jljgZ746_jlnWKAlFCx2TG8QXsdwL_udRiVbFiloZO9c00-oXQzVWDAxxGS3XfadyTDMnnAmjdVKpxgca1lA3v0GWMRiu41gHwvg8wIP-aQt2ROrz_BThkFQSvdQ8y7JqWBQe1PXrpwk9FTx-4hy3zKu3VwKJRTOmGShYgcndZ3pNk0SF1X6o0UkS2eLK79Xyb0IeAn_YsFV2lgkgQiBlM5XLY8c-wvclT-9KcYcgkyLQrVsMQrTbH_pVOuHXDXNii1QYtzgjdn4S6lZ0z8uCvpNKh9Tf-BfTbqCjCmbaDfnCELmh90cuRN-yR2ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EbHywZhCs8O071ouvTA_jdHWfrUzjH78jpU57yXnEZUHp7bqN5M6UUQ_zfFIgreo4A3aaby6itLbLkIcjBI9a7Cl8hgBMZf88QLoD3r3ruSyi4lI7nTTy-BFjBuduGDaFXhn1cCEbn1SkzRUxrD4zaVnpnYTUkZYktEevBdFqEauKs3fTzcF15Fepr2BWoLXRxh5PBn-Mwd64pMcwHjBjaU0_lEMDo63yyt41TZaltx7tTi3M-JqtBx6Jb2-lTguuxCaCPnpra3V1hO0CKxt50BHOx8IcD6WwY9uPBhaS9yWB2o_xmYf40l9aGZD_Ij4sgYyHfcW_Yk2dyU9KaPJ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IUCY0ADw-Aajmxfq1jr3qWKqeBxX0stmn_cLrYq-O5K_ek9sAeWstwaYSlF4IwVIMR1fZShJBMNC5HO3tOshCH5NxVcnWsgvN0FBHepF7p8Fdwi4nPchPzMi1FT13m6e038yVj5OEeHCN_lx8aRIJZVXFZNwL7lrtp1Iu4svIAo7lwLvN-kGLUi0YT3XHTSc3LlBg4RCBHTG0dn7jXD466Db2hyi3UUAaVRcKrhy4CvaIqH5mEO1htmgvH_iId66Xkjt-xb74EZs7uuxm-_ZA9D6wCMNG6TYxiYld1K3Kdq6F-xLMtm7m4WyGHqs7IuXQk70CcpZym7x6GP_o6FZFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rY-xJYgXRbyIFqIDPS2doM07M3ZbZtW2vfGRwuOKgle3sUoXOoTv0160UndFul1dPs5Gv9v4xgONgIl_Zfh0fEmLYNtTRDvp7IggdJMODlU2vOSQyIIvZ1BSk2OrQjMOBde_7elpN_S_na8jr95RH_9k3GWPNxbJDZJ9k90pk78wJmuFjbJU1T4GhF2Ci_-0ReHcHsF82Oq7_umSdZr1slARyGoqEUP6ynWvTD8mrtD1GKvkTLuEXKsZzBSgxNNSXHds0PHOaaynBWXP9aF7dAJnmmxW_bB7kWhOnoMVsuG2QKtz-BgCh_fH_I_JYfmuyf9IkM41TI-USOAbXMtqEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ooqpOIXTo_M8Ta4vuwf7zlkGV4O90Www-XO-oR_4GO1vtfxpFH3b31tdhERKw8pfGT-RaEtQU200nPHJj7EMyl-qNjcQyipnXh-130qU-iFf4WY0ba3GwC9mfMyJRS_EabWXEnInqilYZLiFmm1SHK-JbQsZBpllvuro1MQnBUOLdqlWJ35bUQxMLf2EawoXQkZF2NzMjrRsg4TCisKiYm6huJ24Jy-WgEPaP9Tn3DQI0hwjLYXaAfb_6k5OUWl3-96hTkjOf6Xi3vIrWuau-JHjoSE4uvEVsEv-1uREajUUa3150hk24nnGUkGRGe6BrYcaUZoE0-re65IF9h9Uxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJBr3q6nlbnrPH0wvkvwkF3X9D_DYaIq0UJF4Re1vkyqs1WNay_--sntz1u0ZBEY3bq5qSQChMs8Y56nJAY3Ow1o6YaFSYI03iCXf9_lnYpfPqYcDvBZW5lCZKXukElI8c-4bXXHzkni_Hg-KCF_RZ3va2EECFZHUhUCTGC-5HcpFRE993rBABgwjvTxsVdLsdyK-csD9mkuG4bRevIWVvWo0QYt6vQG_ngsrpbriqXSGWfm1c4s3Ix-ZYcIu2lqukIpYc6MBdkklr8uVfHSr7oqD6iXuLVonboYKIhhYahv-jgSlt0bx8KrYLBcblTVtliHImf5HHv9Ur1GaYWhWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JjSe3xwoJWF6Wjo58T_ubSTNLFMcEIpi4ie9KYi23K4pdBGg03K2DrPMaKx1cgDWF30b1voIMkajv6c0pB_NT2QSmL0yGZnIlJXj70KsefPGl13qHlNvKj_yCoa1-3ozSz7sud_LvnTgk-LQG9zftUTETolYFuUbkkcOr5e5dbLzJJVAxq9A7x0LMgLj3ofAopsjSaIVkVZuF6yDqOr65rj94P7-TDcncnjdmpxkY_HflgA44VrlwI4nFoQqmAl5VRbaJ5nOt56NlTRxmVO77EGjW8QurenzFZw_FYP9JlPVXj1PQ4UgbAE8I190V5m-D03kVxMTO2IH5eC5vrf74A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FfGeVLvhRce3TymsCN1kCpsq07XYOsgG5ZfpoEjJsjYSQJBamqXDbtL4Up0cz9yMT1qnz4lKFgDvvpMFjueG0YobfSouKic0x-Qwmich-uK2ogp5f4jyaj2OvhxlkssjCykLTlZoqKqEs4gwJrhdWgwsxhIuZehOIoy6EiyIjx8oY9c_w68ztNDcT76c6vviV6-BIKc83lzMwqpre8Egr9Za6U-CrsJZfzl1Y5LqK7MmWE9j8ZqIG99vMtVAyYwp4cdKXZNf4CF_FSk6aCpGTylqXxomQbZfRBQaMs_mVSipH-0p6pEpKtLn-TFGuQ3T1PW8Vxro36L1jC3cY24b5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ما خون‌خواه امام شهیدان هستیم
◾️
ساعات اولیۀ مراسم بدرقۀ رهبر شهید انقلاب
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/farsna/447339" target="_blank">📅 07:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447338">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d2ac4fc5d.mp4?token=LpGUd5UDiFtZekBCsdJmY0jkQMfNVQcsWGKI3ynWeg3-eIo9weXZ507aE7FOSn9AEPiKZt6jnSW7eqIR_xOfAx8Rk-GbB7rRKI144I7_41-K5ePILwQ_H4tW62fPGu2ro27CJJPg0QNkqGmGUYwizPzIvWUH4R-ZTbr1sYAusMR0QvFpENa9-yHjL0bzAwnleGOTyFLAz8qy5noPAKElE4C9TD8chB9QvvZdp1lGhyQ89cHYMQgrtUtb_3loayN_F-nJl4NJmKdHTgeNXqP5aRgZUNERpXCJoNXtgf62ZXxAqbXEB7_D6ZeRN-M07eLh1qL6brYyuSwKgZRASYF57A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d2ac4fc5d.mp4?token=LpGUd5UDiFtZekBCsdJmY0jkQMfNVQcsWGKI3ynWeg3-eIo9weXZ507aE7FOSn9AEPiKZt6jnSW7eqIR_xOfAx8Rk-GbB7rRKI144I7_41-K5ePILwQ_H4tW62fPGu2ro27CJJPg0QNkqGmGUYwizPzIvWUH4R-ZTbr1sYAusMR0QvFpENa9-yHjL0bzAwnleGOTyFLAz8qy5noPAKElE4C9TD8chB9QvvZdp1lGhyQ89cHYMQgrtUtb_3loayN_F-nJl4NJmKdHTgeNXqP5aRgZUNERpXCJoNXtgf62ZXxAqbXEB7_D6ZeRN-M07eLh1qL6brYyuSwKgZRASYF57A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روحانی اهل سنت: حرف و عمل رهبر شهید یکی بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/farsna/447338" target="_blank">📅 06:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447337">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/farsna/447337" target="_blank">📅 06:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447335">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1P3FWSymMAZvVIGEYfnHKRuqdsTl27NhtiNXaZKBsoQn978wCT9QASrCedHCbupVC7ig7DiF7roqRmlgqexgM5swkIoZr0oXn1-4vQYl_4pZFkMmln-o5kTHKq2JKFm0mMoff7gtQdkcn9M3dQwTEhiDgv9qHIBCXDf81c8KlL-Xuucab3RAYMtpz3dak-w11nNvDho1pVO948Fjylw8GUR-L_MVKhhDyia3NKWrEk0z0cvrQ_M8i-sl23FeZtTcGEDsm1J-nyAv1AfbSHWa8aLqBJ1UEVN3iq_VUw2w9xW7fhboxyyjdLDnm4xbDqoDLq0RiclvisuzY-rLhrlEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
مردم غیور ترکمن هم خود را با پرچم سرخ انتقام به تشییع آقای شهیدشان رسانده‌اند
@Farsna</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/farsna/447335" target="_blank">📅 06:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447334">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎥
خیل انبوه عزاداران و خون‌خواهان قائد شهید امت در چهارراه ولیعصر(عج)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/farsna/447334" target="_blank">📅 06:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447333">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac5c64b1a1.mp4?token=ZCa2IBqEFUOZknu2dBgHBEengKDAiAB6qE_RY44NsWi326bRY63chngI2KjKcCPWQyZ2Yq9Q6unCKjL-A_pCT2LYwTQ3e7PjMbr_kXx0oL9MNgGJw_ort1NbmSrI3ps2ic6CEgoee27FLOCEkg1IofwRKhqHI7Gn0mD0NEqzhoS_2AbZZKNaHeaxJLmCiIucdngXRk-xDbr3qRIZgCy-b9KRtxFbV-F-x3TkUjNX5Luih_Nz7lw3ZnHDQRRtE4XnQ0fe-qfslRMeEDKFD2neVH_cD7RxJg1OBbjzrtKDTgDERtX22VAbPEU63Tc6dklsE_XvfEgVYtGKbnbu77W9Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac5c64b1a1.mp4?token=ZCa2IBqEFUOZknu2dBgHBEengKDAiAB6qE_RY44NsWi326bRY63chngI2KjKcCPWQyZ2Yq9Q6unCKjL-A_pCT2LYwTQ3e7PjMbr_kXx0oL9MNgGJw_ort1NbmSrI3ps2ic6CEgoee27FLOCEkg1IofwRKhqHI7Gn0mD0NEqzhoS_2AbZZKNaHeaxJLmCiIucdngXRk-xDbr3qRIZgCy-b9KRtxFbV-F-x3TkUjNX5Luih_Nz7lw3ZnHDQRRtE4XnQ0fe-qfslRMeEDKFD2neVH_cD7RxJg1OBbjzrtKDTgDERtX22VAbPEU63Tc6dklsE_XvfEgVYtGKbnbu77W9Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور باشکوه مردم در دروازه‌دولت در بدرقۀ شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/farsna/447333" target="_blank">📅 06:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447332">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80f48c054e.mp4?token=E1O99ZzOfcHA05XyuT2UJo8UBg1UkuqixBvhIFo9hGgyn5C7aIH7wS-LXfwsvoxFDV-1PEs4AEN6jdkZrXe0OOTOXKtAHbvLb53BwsSughsKyK1I7m-SW8fMBhBCbfbX64onhGNRjBi0WOCQpC25mrZrgvFtr5p9AnfC9Ubffb2Xpdo1zSrLo-BbeqhNgU-fWquebF2WhSvzE-IShpqFdUQx7EBwtFZuV7nIn_gXOekxGNi2iHdw2Jv4VENa1JXUK7dGaT-l_GpBE35LNI7bnwonJAlptgiG-Sui8uC-xnUGFYN9OghTf0JTy4WmJq_PgICu7d3jhunlDeJ4PE-7-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80f48c054e.mp4?token=E1O99ZzOfcHA05XyuT2UJo8UBg1UkuqixBvhIFo9hGgyn5C7aIH7wS-LXfwsvoxFDV-1PEs4AEN6jdkZrXe0OOTOXKtAHbvLb53BwsSughsKyK1I7m-SW8fMBhBCbfbX64onhGNRjBi0WOCQpC25mrZrgvFtr5p9AnfC9Ubffb2Xpdo1zSrLo-BbeqhNgU-fWquebF2WhSvzE-IShpqFdUQx7EBwtFZuV7nIn_gXOekxGNi2iHdw2Jv4VENa1JXUK7dGaT-l_GpBE35LNI7bnwonJAlptgiG-Sui8uC-xnUGFYN9OghTf0JTy4WmJq_PgICu7d3jhunlDeJ4PE-7-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همه آمده‌اند، با پرچم‌های سرخ انتقام
◾️
قابی از حضور مردم در مراسم تشییع رهبر شهید انقلاب در میدان امام حسین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/farsna/447332" target="_blank">📅 06:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447331">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28907d739d.mp4?token=W176tCe6Qf-fcYFrgG-nCNSxDT5ApyABMhvObAJ8dEVvFnTtGq4BZYf9DE4zwN7B8b0hNMJYV5MNYjxJ3nEb7pWQb9AIySJhr8tESSlW9uX8yGfikcdwP7JWtoAgExJOFb5hJEF9l-2zmr8YFBgC9zkjD_siY1HjdzPxu16L6j_Wn6XKF3OQUlZobYgaezOOsXbBt_1buZBqYUSggHBeIqaG81FKDImbnqB2kpOd6tkSL8MU_uch9PASHOjkHpeyLRWt_kJdPeBVD_QNg7szKsnIMK_shsoTr5AG18ArtqMxhopQBv5OwOx-iX9SIYBFOQ5UA8M6Rd7C8rE0yIfdkIKBy3y6u_LHicO0jn_q7yu7-V3No_IkokGp8eN3UpytiSL2W5iRe_JOCZOuIiBQa_wAPF6kGlHUcky7Z3W3iyOwesf78KjZvaAA9ryezlP_ttaL7gQG-vB9QtLD2nEAeB3dCLGMN0AzCLGj-a0ZtQ4u-DpwCxJqAuLP1PKNqKvd6JvD2SwDFCCEqpy9_Dm81emUzhdayNlCM2v9QZyFjtU6q0U6nj2uJx7uGdYlwOdxO5UjfIKY8W5Hjco7p5PWSnV2tOkkPtEPhnYMS1AVOYMFC6ms2NbYWh0QYEAzHZeGj6H2vFfCKI3UtTOMlrxieEAf-AdrKtzCqb2EZ9xhC4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28907d739d.mp4?token=W176tCe6Qf-fcYFrgG-nCNSxDT5ApyABMhvObAJ8dEVvFnTtGq4BZYf9DE4zwN7B8b0hNMJYV5MNYjxJ3nEb7pWQb9AIySJhr8tESSlW9uX8yGfikcdwP7JWtoAgExJOFb5hJEF9l-2zmr8YFBgC9zkjD_siY1HjdzPxu16L6j_Wn6XKF3OQUlZobYgaezOOsXbBt_1buZBqYUSggHBeIqaG81FKDImbnqB2kpOd6tkSL8MU_uch9PASHOjkHpeyLRWt_kJdPeBVD_QNg7szKsnIMK_shsoTr5AG18ArtqMxhopQBv5OwOx-iX9SIYBFOQ5UA8M6Rd7C8rE0yIfdkIKBy3y6u_LHicO0jn_q7yu7-V3No_IkokGp8eN3UpytiSL2W5iRe_JOCZOuIiBQa_wAPF6kGlHUcky7Z3W3iyOwesf78KjZvaAA9ryezlP_ttaL7gQG-vB9QtLD2nEAeB3dCLGMN0AzCLGj-a0ZtQ4u-DpwCxJqAuLP1PKNqKvd6JvD2SwDFCCEqpy9_Dm81emUzhdayNlCM2v9QZyFjtU6q0U6nj2uJx7uGdYlwOdxO5UjfIKY8W5Hjco7p5PWSnV2tOkkPtEPhnYMS1AVOYMFC6ms2NbYWh0QYEAzHZeGj6H2vFfCKI3UtTOMlrxieEAf-AdrKtzCqb2EZ9xhC4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عهدی که تمام نمی‌شود...
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/farsna/447331" target="_blank">📅 06:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447330">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c1499fca.mp4?token=VYuW3qt4n_-FR4SIY8319KX-lNCfgsbcCDxUUaHMJExdrTCoEwfp-Cz5JK6Kyy7oqaCuq07XVOMakzMyGjI9q7cJCA4_AG4bkJMKrafbzUFdBPnTccMTFZYSKHxqUml3nS6l9cyGMZeCdKEGXEqDVWotkGrW6eATzh6m1ieHWwYyF3yjhwFIDW0jGYjGed6ZyNgDSrunyX1ZdU8SwKZvxUyqrmeek2VL6_jjI8-rTt3hijJwIf6b2L2PUGffBQtx61PF8KBalvirZ-M9zP8DNw-Bs3LpAaEYwfWXSitrdiK0iExQVII7tW1liKUsSaRtDdP-ca43vthdPSIKFueHxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c1499fca.mp4?token=VYuW3qt4n_-FR4SIY8319KX-lNCfgsbcCDxUUaHMJExdrTCoEwfp-Cz5JK6Kyy7oqaCuq07XVOMakzMyGjI9q7cJCA4_AG4bkJMKrafbzUFdBPnTccMTFZYSKHxqUml3nS6l9cyGMZeCdKEGXEqDVWotkGrW6eATzh6m1ieHWwYyF3yjhwFIDW0jGYjGed6ZyNgDSrunyX1ZdU8SwKZvxUyqrmeek2VL6_jjI8-rTt3hijJwIf6b2L2PUGffBQtx61PF8KBalvirZ-M9zP8DNw-Bs3LpAaEYwfWXSitrdiK0iExQVII7tW1liKUsSaRtDdP-ca43vthdPSIKFueHxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مرگ‌بر آمریکا و مرگ‌بر اسرائیل عزاداران رهبر شهید انقلاب در ایستگاه متروی تئاتر شهر
@Farsna</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/farsna/447330" target="_blank">📅 06:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447329">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🎥
مردم عزادار با پرچم‌های انتقام یالثارات الحسین به مراسم تشییع رهبر شهیدشان آمدند
@Farsna</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/farsna/447329" target="_blank">📅 06:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447328">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تمام ایستگاه‌های متروی در مسیر تشییع باز هستند
🔹
شرکت بهره‌برداری متروی تهران: تمامی ایستگاه‌های واقع در مسیر مراسم باز هستند، اما در صورت افزایش حجم مسافران، ممکن است برخی ایستگاه‌ها به‌صورت موقت بسته شوند.
@Farsna</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/farsna/447328" target="_blank">📅 06:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447327">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/365c1f58ce.mp4?token=JMB5WCEnRk69-2SYR0J9jaqomTlCNJTKN4MuXsU6YgsGoWikXOh_Gv7wfUJvvDr-BGglDji8YwT01mTPMdds6AZRe1LR6vdgUT0WJy2HbQTTJdXEYLwWHKfr3H3DeaAIHqVnq6z79i0fCxeMglxFBNgdl_icz8i0sE4-Ty9zLXFC-71uF5bcmIzVcS0Ht5kez0cEC39LaWmujv0Xoyo48RDoaW7if2Oz0fLbtg1MvSr-SF8uP0PSitGouhfBUyRhsEovY6kzJCyscdIb1TgAD0tiN-d3dxh26vOMNgEcSWTx1IX0u9elvGA5OdIpwlCYH5E9wMNHSTGFAD7y_5WWlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/365c1f58ce.mp4?token=JMB5WCEnRk69-2SYR0J9jaqomTlCNJTKN4MuXsU6YgsGoWikXOh_Gv7wfUJvvDr-BGglDji8YwT01mTPMdds6AZRe1LR6vdgUT0WJy2HbQTTJdXEYLwWHKfr3H3DeaAIHqVnq6z79i0fCxeMglxFBNgdl_icz8i0sE4-Ty9zLXFC-71uF5bcmIzVcS0Ht5kez0cEC39LaWmujv0Xoyo48RDoaW7if2Oz0fLbtg1MvSr-SF8uP0PSitGouhfBUyRhsEovY6kzJCyscdIb1TgAD0tiN-d3dxh26vOMNgEcSWTx1IX0u9elvGA5OdIpwlCYH5E9wMNHSTGFAD7y_5WWlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری محلی جمعی از بانوان در متروی تهران، در مسیر رسیدن به مراسم تشییع پیکر آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/farsna/447327" target="_blank">📅 06:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447326">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a088ef3c7.mp4?token=cNErqk5G4o2oOuiGtVkinFNHOns5rnJIof1wsh2EYFJ-77N-4gnHZ839gQwkm0n4yvRarZvDHN0B0H-71wqp9GfXZbpWYeAzKXDF63ymVp_d9j4L8Np5Jvgb_cOPwvAOGJPd3UHeymzNxiDTVsIKXc_urL0qonem4Q2LUvRbm1gg7TJoXSzRV8ZenINjnokKBfwVZqIGhOXBnSwjV-nJtABtn8NM5_-INiji9WDY8vocfs5ICEZ0m3ZfJsfHssn1yLCDrNGTPiyAyB99hitDT0UI9UZBNTMX8UQhSomG1SjDdrPqb1weeFqmx9naDghgKAs13soOhBDSKDzBBtj_ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a088ef3c7.mp4?token=cNErqk5G4o2oOuiGtVkinFNHOns5rnJIof1wsh2EYFJ-77N-4gnHZ839gQwkm0n4yvRarZvDHN0B0H-71wqp9GfXZbpWYeAzKXDF63ymVp_d9j4L8Np5Jvgb_cOPwvAOGJPd3UHeymzNxiDTVsIKXc_urL0qonem4Q2LUvRbm1gg7TJoXSzRV8ZenINjnokKBfwVZqIGhOXBnSwjV-nJtABtn8NM5_-INiji9WDY8vocfs5ICEZ0m3ZfJsfHssn1yLCDrNGTPiyAyB99hitDT0UI9UZBNTMX8UQhSomG1SjDdrPqb1weeFqmx9naDghgKAs13soOhBDSKDzBBtj_ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای متروی دروازه‌دولت در آستانه آغاز مراسم تشییع پیکر رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/farsna/447326" target="_blank">📅 06:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447325">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33401348d1.mp4?token=RNkHuTaw5J_x_BMTjN91bLJ2CXyyGTgTblCvQPh-sjQNDQ6iY8Fecgvx8OqjWM3ifks4V8MDhH4UmTOCjFLVl6rzzF9kGtopUzLC5l198OwcjAa_eygsrrpS43kyYfhDEw9mYEccMss7fqQBbMgY2nESuT02jO1pRkYqsgUokbNZ7tJi3yMl6USTmxQifa6UCGnOm8RMhP87-FKi64B8ToCD-o4_bCSZFmpbtBEpuMM4yXUWyrLuuv7DrJiTmK2OTB9ESxcfTFICQLVKqoa0Tr8x10cW8NBAQodR_wIjrhsjlXOzsxITDDA6kF4wOHJ3mVmJkd4e8m-EMdRIElTPNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33401348d1.mp4?token=RNkHuTaw5J_x_BMTjN91bLJ2CXyyGTgTblCvQPh-sjQNDQ6iY8Fecgvx8OqjWM3ifks4V8MDhH4UmTOCjFLVl6rzzF9kGtopUzLC5l198OwcjAa_eygsrrpS43kyYfhDEw9mYEccMss7fqQBbMgY2nESuT02jO1pRkYqsgUokbNZ7tJi3yMl6USTmxQifa6UCGnOm8RMhP87-FKi64B8ToCD-o4_bCSZFmpbtBEpuMM4yXUWyrLuuv7DrJiTmK2OTB9ESxcfTFICQLVKqoa0Tr8x10cW8NBAQodR_wIjrhsjlXOzsxITDDA6kF4wOHJ3mVmJkd4e8m-EMdRIElTPNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم‌های سرخ انتقام در دستان مردم حاضر در چهارراه ولیعصر(عج) تهران  @Farsna</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/farsna/447325" target="_blank">📅 06:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447324">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01380449bd.mp4?token=JjGv2GhyTa_OQF13c6hv6_nUhPYjwyXcNFwwGgwbOpu-aSdN14MlRBDlABfV0b0Y3oWihtiOIWoYn64gRlSqz_M8_LyuKBT_3cl6fj4ahcC42FuOttk2byrbzIXeGdr3lJ1orbd_0vt0N23YhhrNlt4-LRvcuwey9u3D92t_sY0Lz32BaUxW0GhpeldUBpvX6VRebBuazko_kWXlDhnK78m9Th_6nte-MOVBXNrE-Ijj3vrJbRRDeqNUC_Gf24GMtDMjaE_HhiAsVp_8TSucY5ZHD7uz_FKqldKh7rfUB4oaNF8SItLv2mwC-40y2RUUAIH1RVB9OiHrOsHEwXbUXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01380449bd.mp4?token=JjGv2GhyTa_OQF13c6hv6_nUhPYjwyXcNFwwGgwbOpu-aSdN14MlRBDlABfV0b0Y3oWihtiOIWoYn64gRlSqz_M8_LyuKBT_3cl6fj4ahcC42FuOttk2byrbzIXeGdr3lJ1orbd_0vt0N23YhhrNlt4-LRvcuwey9u3D92t_sY0Lz32BaUxW0GhpeldUBpvX6VRebBuazko_kWXlDhnK78m9Th_6nte-MOVBXNrE-Ijj3vrJbRRDeqNUC_Gf24GMtDMjaE_HhiAsVp_8TSucY5ZHD7uz_FKqldKh7rfUB4oaNF8SItLv2mwC-40y2RUUAIH1RVB9OiHrOsHEwXbUXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای چهارراه ولیعصر تهران  @Farsna</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/farsna/447324" target="_blank">📅 06:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447323">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fed9d9e34.mp4?token=ScGMC3pwOYwe3zTPFkPrbnCMVpjKZNneAjVA2BJD0dA6bqxTL1JCRj_PoSHque03KihUV4mWUIjolAuRYPk2d2v0EaJTbT4Wm3OrGJd--pbwhrHTftZyNGn15eKD-fRzSzeCpJs3Tq6BkVND1RK67Myp0PxGirZ6P5yxahvlOfs54w_c9sE-vfZILRa-rZKGjiHpeAtQ_HKs77vvrfreCt2chKgPo5H4B7e1kibowP4jmLlOOTeGy5K_IHp7sQI6RMb6xzx2VIb4yMwsbRTJrTw-D3hq8OZfGoBVOV5-4h-TnyD9Ib7METp7jz20KXqTC8kbSbkSOa_fHrHQ2oxYEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fed9d9e34.mp4?token=ScGMC3pwOYwe3zTPFkPrbnCMVpjKZNneAjVA2BJD0dA6bqxTL1JCRj_PoSHque03KihUV4mWUIjolAuRYPk2d2v0EaJTbT4Wm3OrGJd--pbwhrHTftZyNGn15eKD-fRzSzeCpJs3Tq6BkVND1RK67Myp0PxGirZ6P5yxahvlOfs54w_c9sE-vfZILRa-rZKGjiHpeAtQ_HKs77vvrfreCt2chKgPo5H4B7e1kibowP4jmLlOOTeGy5K_IHp7sQI6RMb6xzx2VIb4yMwsbRTJrTw-D3hq8OZfGoBVOV5-4h-TnyD9Ib7METp7jz20KXqTC8kbSbkSOa_fHrHQ2oxYEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان انقلاب تهران؛ اندک اندک جمع مستان می‌رسد...  @Farsna</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/farsna/447323" target="_blank">📅 05:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447322">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d420a8f2a4.mp4?token=d28-BECWagsDatXOF90iQyNf5EDuk4ThqUqCQ2W36XbiZ2aHltl69XRYTdvS1QHeuf-ZroHOgr9qZvFykO2hn92ZxJ7HxI1iSMaBSE6F2QWpBZRLLwoTm_w5AfV8H_pqGMchiyAKJMGgtClwSDc9wjyBvniWBr_c-XhZq2xpmN2_W2ed7l4FD4fuRSn8eFMzz1R_fJNjqp1jqESHX3NtJ4SqMWAMY_q7zKQoJAPtm5J--mdtGwOU5NvFK8tGJkZvrrNCBZaAWhIBIk05335nVHE2B798D6atymRN_OpOO2_JkaaLVGopbyXicaDXqMPyMhoYLlSGmBYWX3OkE3eQOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d420a8f2a4.mp4?token=d28-BECWagsDatXOF90iQyNf5EDuk4ThqUqCQ2W36XbiZ2aHltl69XRYTdvS1QHeuf-ZroHOgr9qZvFykO2hn92ZxJ7HxI1iSMaBSE6F2QWpBZRLLwoTm_w5AfV8H_pqGMchiyAKJMGgtClwSDc9wjyBvniWBr_c-XhZq2xpmN2_W2ed7l4FD4fuRSn8eFMzz1R_fJNjqp1jqESHX3NtJ4SqMWAMY_q7zKQoJAPtm5J--mdtGwOU5NvFK8tGJkZvrrNCBZaAWhIBIk05335nVHE2B798D6atymRN_OpOO2_JkaaLVGopbyXicaDXqMPyMhoYLlSGmBYWX3OkE3eQOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سه‌راه تهرانپارس، و مردم منتظر برای آغاز تشییع پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/farsna/447322" target="_blank">📅 05:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447321">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57253c680e.mp4?token=Bk4d6yXACeb6c8NzYN0EP0XG_fCRhLEskAwOfGdFjTpCRho0TSISCSEdd7Mog1aA9PXpq6ui3MSbvx1lFcewx2m5Vl_tQ4yI0Y5J5fGD0OM7P_FTJDWS3G_vJGzUnrjvD76Wh6TPTpg8ct3YV5Bzr3d3DPCj8dgLC08S9gkXh2Yv76lExo7uGxUgTTTJ5eHU8WEc3DYixudQ1sodNB2WwxmOCdqn_fNY2_mQd4efxXqllZIGXuUJ0yQTSgFMRASzm-aCO5fBPVxmfeCMMGCmHA7EqwPHNvqGXuKeJvl8xNxZpEv31k2Df83sIIfPoupXCHqEzuYl5fotLrx7cF63Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57253c680e.mp4?token=Bk4d6yXACeb6c8NzYN0EP0XG_fCRhLEskAwOfGdFjTpCRho0TSISCSEdd7Mog1aA9PXpq6ui3MSbvx1lFcewx2m5Vl_tQ4yI0Y5J5fGD0OM7P_FTJDWS3G_vJGzUnrjvD76Wh6TPTpg8ct3YV5Bzr3d3DPCj8dgLC08S9gkXh2Yv76lExo7uGxUgTTTJ5eHU8WEc3DYixudQ1sodNB2WwxmOCdqn_fNY2_mQd4efxXqllZIGXuUJ0yQTSgFMRASzm-aCO5fBPVxmfeCMMGCmHA7EqwPHNvqGXuKeJvl8xNxZpEv31k2Df83sIIfPoupXCHqEzuYl5fotLrx7cF63Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
متروی صادقیه و مردمی که همچنان در حال عزیمت به مراسم تشییع پدر امت هستند
@Farsna</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/farsna/447321" target="_blank">📅 05:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447320">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-text">📹
#فیلم
| مصطفی راغب قطعه «وداع» را برای رهبر شهید خواند
@rahbari_plus</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/farsna/447320" target="_blank">📅 05:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447319">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/359fef61fe.mp4?token=uwehuVab_laqbY2DGdFyTEiF9px_4turFK8_qhxnxv10WsgcqKvvmHaiUeoW0JWxiT2Vo7JsPxlPQNOANi8AXeQ9GpPSIjt3xxnRkfSYaBVjo18IdNzgS8YGYnz1eF7k625lyLl2pAXv1xu37_jlyYCYvpN3h-UQ_p4IqkhERqNntrki2tnQfgZYB0R5megVeLTqvnu7g_qAPklUkPD5NznAX-7KU5mWE-QMtvF81ozgvNk7IdKQ5nVDSKFqsx9jYNn5ujaZL4qfo0sfaI1aENs0GLzQjp90l8RJLpkL2s76OSUoO0bFEuo_wjSGfQR_uPBGzhwV6YwcEd1AeNYpkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/359fef61fe.mp4?token=uwehuVab_laqbY2DGdFyTEiF9px_4turFK8_qhxnxv10WsgcqKvvmHaiUeoW0JWxiT2Vo7JsPxlPQNOANi8AXeQ9GpPSIjt3xxnRkfSYaBVjo18IdNzgS8YGYnz1eF7k625lyLl2pAXv1xu37_jlyYCYvpN3h-UQ_p4IqkhERqNntrki2tnQfgZYB0R5megVeLTqvnu7g_qAPklUkPD5NznAX-7KU5mWE-QMtvF81ozgvNk7IdKQ5nVDSKFqsx9jYNn5ujaZL4qfo0sfaI1aENs0GLzQjp90l8RJLpkL2s76OSUoO0bFEuo_wjSGfQR_uPBGzhwV6YwcEd1AeNYpkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای چهارراه ولیعصر تهران
@Farsna</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/farsna/447319" target="_blank">📅 05:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447318">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d4b48290.mp4?token=tD6UyKJa0D5QAO27pOlNi9eiv_SSpNlbVmNWBnSr-SdqGKS0dUSWOeDalJwAVvPuWBQQYVPwCYYpbt8WmxKt0eEQNQvSPFDEPqxKVhrlTHL2qA3fbaKLNP-8pIwzOEJTokK0h4sHmcx4HBpMRw8v69V5AafkKSlE3oeCwUfdLGSitTaD07Gat5QAwlWezJjfpXRaQ7mTyjSrA_apD_tXJOt12UOYZ7elzT8a8ZR0vp3gG7-xTgKODMuqUipHa6TW5VMdYS2y_x-gKlyftOw_lhzL-u0sXf9MppxRTSgKa-TYMP9mHLlKXbplsjOtPf5Jzkc0fmfm45-Un3RrEGY8XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d4b48290.mp4?token=tD6UyKJa0D5QAO27pOlNi9eiv_SSpNlbVmNWBnSr-SdqGKS0dUSWOeDalJwAVvPuWBQQYVPwCYYpbt8WmxKt0eEQNQvSPFDEPqxKVhrlTHL2qA3fbaKLNP-8pIwzOEJTokK0h4sHmcx4HBpMRw8v69V5AafkKSlE3oeCwUfdLGSitTaD07Gat5QAwlWezJjfpXRaQ7mTyjSrA_apD_tXJOt12UOYZ7elzT8a8ZR0vp3gG7-xTgKODMuqUipHa6TW5VMdYS2y_x-gKlyftOw_lhzL-u0sXf9MppxRTSgKa-TYMP9mHLlKXbplsjOtPf5Jzkc0fmfm45-Un3RrEGY8XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تهران مهیای بدرقۀ آقای شهید ایران   @Farsna</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/farsna/447318" target="_blank">📅 05:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447317">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3340c6ef33.mp4?token=XJLeSExK23wZj_n7c4d35AQIsz0ROJ7IWz8jA32c8V_DNqidyJLS_JRWa1_kY2v2qJVdqufe2qWpyxIg0E_4n6dnyMDMckNh0W0gJsknqOexCnKBF2SHDSs4rdTMWqX-0nnov6Fcz0xr-MbiYLJdyJ6NTYSThDy05Bx7IdPkQBXwB_LY-4v-xLRcqXShcs6myUoj1igKmxiat1F0jWnSCAbQ1o7ZzTHkDAZ8qzj6V6ERmk19Av_RTjq3OtzuVpoFIGXYjxPSh3bguwqtkJTxuTfHmoD6Z05CZRYI9IFM0a9omTC47d0Di46BDXjJInnc5LkX00UP7uvZl0SlJxkKEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3340c6ef33.mp4?token=XJLeSExK23wZj_n7c4d35AQIsz0ROJ7IWz8jA32c8V_DNqidyJLS_JRWa1_kY2v2qJVdqufe2qWpyxIg0E_4n6dnyMDMckNh0W0gJsknqOexCnKBF2SHDSs4rdTMWqX-0nnov6Fcz0xr-MbiYLJdyJ6NTYSThDy05Bx7IdPkQBXwB_LY-4v-xLRcqXShcs6myUoj1igKmxiat1F0jWnSCAbQ1o7ZzTHkDAZ8qzj6V6ERmk19Av_RTjq3OtzuVpoFIGXYjxPSh3bguwqtkJTxuTfHmoD6Z05CZRYI9IFM0a9omTC47d0Di46BDXjJInnc5LkX00UP7uvZl0SlJxkKEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تهران مهیای بدرقۀ آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/farsna/447317" target="_blank">📅 05:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447307">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OOrpGpDsCCwk6mY3-0HOVeGDl1k2orve4Wqyr-5Io2lpYJN3K9OxVJ07oRUynvJDWgEAksjZL7QloreVDNUlmYJEsWzWy1UiiycVy1Mxk61amz2B-zfHae82D9XE06eguEZFBTBo1RSuMw5neBSnJ2bLAph_r8d7m7j7JTgFJlYGpOIN5qJQmDgaHTuU7JD_sc4CR95q7ZrPinOe8tpDnTB54Lob6P6raE1L5UONmKESuuT_weIogcira6NFfWIc76CArzPKV41uIcMl_hLzDzP7ON-sMQPoy5aPB6MLRH1S4UYLQjrw4lhnP8T8VYSDgSufNUCwQq00sgk1zRxVFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDINY4LXibireQysU6wjE2c2vYPd5rAUKECIgA0viLviMN7oZubR2nrfzCq6G7Gb7_g_cWMp5mGzYIssVXuZ0C4YbwRSGWfaueqOtH4QBSku0r505T2c5uqUHJQXHuTB9NZYdFW6lcPGiJfL7X8VNntqvxCgG0FIqN6zoq7HuhGNM0I0ACzW1hFOjZqWB1GqqKmeVdz6Wod7KAz2BEBTpDWpeT0IJtsh0OvNteUJ1bGy9wPuIJzqv1E9famXbRv5H-jl-7AANnbDXODvrRJZI5_AzuhNRG6loW-Apx8uF2JWsqdEvSU-vD7iFKQN2eN8lQ55j5KBAznt-IdfPSBOHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/plZLe4B4ahlgticse0tVrY-BgfkGas5jVip2XvDy2JVcQO_TuBEoFv7eRP9bzQlvQ1pNo04bp_FgAbKcGfh0gPlbDtC8nZqMwep4OwaY_v_yCpyGS6HlBaAbuGqt89YPoGhDzjHhZQvY3m-U-I2f4rCAB6jpkD9_n-eF_b446apf8BOK0NQedn5TB5jY83bODKGcL27V1B7knrFrVKW4CY2VsCdLkdcHGRpU4ZMLvne0SU3NFaj2uaUw5RLyCdw5PsC8HfDo7xPEirTAABFehgAjUI3semuFb7Hfmxm3bLfs663ERpKsnXfNreD3lym2DMn72W4qXatV5LjkL1fE6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6DuSHgC24TI7uFWM2LIV8XDDACbdYnBfePOgrPkEvH5Vyi9GhsdtQHFAkTM7rBxCNtkp5KC5tov5xIL35An7-auyvvrvMTA_fST6q9SE-L4d9YDg4VHc4bSkv-21lWcFoKxBVCvrOpykimsyk7AzsB0kwVeIeqR7M5hYrTsFW-FqCfa0C8NLONvOImK77QxlEN32t8Ra7knKkmYEB4f_YoTgMqwxSqGA-vmk4V3KxEZjG_d-1UWYELXfZUNaSa5wh_CWRpE2nKFfbq3b33xbALvPAiGvSrhYl5tmpnjzWK4bOev3-be4mYm_whtIoVwcvP4MUiP5JTfCcwIoJel2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2OzHxZLFNEbGXiqxYQTMwlMuLOe5t82bKgmapErWIgHKP2ynVtIZUczRSgamy7v5oxTe-jH4xE2n780WgZbP83X4oKW0CICoUqi3bePnxsjniobix4q4zB76l71nNHbRk-qRXKD5F1Zr4-EBIkJoFLUnYRZnwk4XbnThuLhlG4zw4paPYeYN-AWU0mluM7vsOS3b7MGefajLheFJx5DhDlLOt5jPaeig0Y5l3hObUWxSh5VRcryWxXwqInD2iEUMCle3mwOmvmg3AIQJHfMJtR4qiFqAniyjcelthbgvgRdM6EeWgOcEOlRUSvH4rKk_LU7qElfYHVATU49HwCaUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h-FCK1sguJMTjEjLoG4oe39_KeX0el_85H44_x3URoEOMBEusUo6j-echcoOfQF--tNWBSkIIRItViL0_SurRFCLQHo7c4QQnn3cXMEUwfxJzQWUeWotaTPxF1_AS4mvrcSlkRctGu5hS3tbh-2owraFXC_C2XqQ-yPKHzR519OTSERpNZqRPTGzADxnE4ZqjWpaXhyW7fGj4-4U2Os-845aoNRrg1EFKXH8tF_QON9MvLCFqe1BU59LwscUN6Ier9zdVYLAtx1I5tIFpXWdR7AynGKmPyRPN8xKshcALY2-VA5JUmYJt5SlpAv1F6HElWS2VbcrfYDG81T2VSvdcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b2YJ7PzfRdPK9HbsqgD-jpW1xVLQnFBLO0yAKSIGNTmUi3HlBsBCOBG4NqWtFy7y3mb-6tYU6Ab0Rwx5XQX3fJJ9kR4P28saB-x2JOx0VE5Bdir4mR9iyrHyq7R0ZQWO5dfXx8DRmEcL_JoHCfFwDpDHiuZCvmyx7cntgDDvKJnEnKk8ZAmmpShrnLcy2OqtVG4DjG5kNs-LIAyZqN6CMwyJiA8CSeuYnexrmwoGaitGkIrao0Ctfa-kmam-yq2jodaR5_WB3CHG14GfKkdaaCftsu5qskznHOUXoeLJiqaYYOo4242rYzJxUp-tIs9NbsCnX8fFAIKauoouNgsd_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NPLLpBqKFaYOPey6Hw0reXBio12p4YBVbR9qrrDxRE0n-tImBxtsXJMDxBZn_h15UzHRfvR-eNrO_kDJN-BmMB6NL1aI7969BLoZFqh9jRcBHGmDnldVmQFid9Tn7Pbz1ffyWzfMvE88fCyAmkoThraPdS2xovrTvPJHsRLYwGsMR4LbpO4nd57AgGcvJ9wOIFs7m1SDhVOIX9ZF_uibsV9j8m5Y5OM89rCrs6y04uHxpMkxz6dD7sy-0vawraYpOt5huPze7JCh--5CbjoIOpSlhm3b0T3tW9fv53RhbKafalNT6do6iVUqmUkrqaDkr-QAj9qEuQCEZ-01aq7GHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W9lrg7D0RxL_r_TxW4lTe7qlXURUSSxxhVjf14vS-KR4SpT6jgYxDtTRKwjMMSqsctyPnzkpCqFSg-j7eeQVUY8t60wdT7iNnvAvIVp6jwY1GqFstXWNDWg_knCurTXnJbDWu4Bf7QaL2mg_20p0NI2pIJWLTNlryNnqmcUPxuLAntdG6mIp6ayQMVqArLCqSN_6i8zJPBTvSqQhN8o14QuNNFH8v9jVTOn7ir_AfXWsAFNZKVRfTArT9W7DqC3mLhB7qnYBVXnTNltUaYMGQc3FXNcwC0pnD5a4koBrCGHvzNT6E7tNflFgE5BLpTVmUxfVe-FBRL7mU1b_I8_B3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0XGpx24jiDdd0mOwNtk5hy3uAYMzilhX9XF8Mo-Uq_pdcSAxhR4rz8R19-FXM2oBDPyL_oOykyo37gEy4c95Fdkro9LNf_j_33K0ubdbdcl0LkW3DtG3xjIpEqftyDoMHcZbBwAtI7iZt4UZEE-HD63AgkroWKp0APAK5E5A_NaYRT2pLD4jz7wSS9D5frR-l_1iy_zWFgqUz0vmoT2difQycQm85Mv97Grc8lZkyBZYEt2pClG4i4qwNOHjfnJU-y7YCQrF0FzQL3EXXD4EwlDuJO6SIwiUnkQLJm4xGwBYYYYm44tea26rcull6djd5fXtNfTEHvXYW43i0Ic6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آماده‌سازی مسیر تشییع رهبر شهید انقلاب در قم
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/447307" target="_blank">📅 05:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447306">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14a6b8059.mp4?token=iygmKg5vjEMl4tOBfKoTqbVXUqePWu8rK2d11tSvpbAvLVMqYoIgalDVvim7uOF8-Goi-fWZkGmFYVNAsAucddTH6REV5rpMlvk3JBZUvV9k7y6vFpGViQcLdO2dvO8KryerRVQkeQN2cfWlWfK5CdqcaBKOyr5CdIoytd5i09A-MFgtJB2exdOEktfteIPVm6QYn5uz-xqDFkVXnhmJ5f1PW1E5ABdKq6SaUh0CL6inYHfEPVKWVjy3Ii0osIpwscuAd4sa30YQl-GengtWfi4LNjXL-eynapXbNbAu-lIHqH7EFfVjckxxloChhhYiZhGTKu38p9v71Pk8gD2EUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14a6b8059.mp4?token=iygmKg5vjEMl4tOBfKoTqbVXUqePWu8rK2d11tSvpbAvLVMqYoIgalDVvim7uOF8-Goi-fWZkGmFYVNAsAucddTH6REV5rpMlvk3JBZUvV9k7y6vFpGViQcLdO2dvO8KryerRVQkeQN2cfWlWfK5CdqcaBKOyr5CdIoytd5i09A-MFgtJB2exdOEktfteIPVm6QYn5uz-xqDFkVXnhmJ5f1PW1E5ABdKq6SaUh0CL6inYHfEPVKWVjy3Ii0osIpwscuAd4sa30YQl-GengtWfi4LNjXL-eynapXbNbAu-lIHqH7EFfVjckxxloChhhYiZhGTKu38p9v71Pk8gD2EUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
متروی تهران، و مردمی که درحال عزیمت به مسیرهای تشییع رهبر شهید انقلاب هستند  @Farsna</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/farsna/447306" target="_blank">📅 05:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447305">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2415cf5901.mp4?token=S7uov_ImEDguszyD7Fl5MwkFII1ZBbuQAUlEp1ILUXBI2qIARfZkDgQD9DV7hO0_msuaaE7BnFOySHRbhtV87rmYFE4qaA1dJNiA_5hAY3TeetBcYkyRI3o5tlmboQPISwepLZSnxFRPE9PHyZhbUfHKzZzStMUocS0KkR1FTPcafJpkRGFdhOSgxq7RJShT3Gmt9IBJwR4G1uHQ-XZFZrTYkJDr1zZofmIVkGhHPSKa408YlpPNHDb2komRAoOlXR9HROubYm-KV8vApAE6jFdCjmUSqGmOkxTJS8cDl78HJ79ECyArhqsqGkZsXUxTSVhdWEKMXhiDNxF4KvuW1WqX678dblRHh1WY_mW-wI6mswdkytNh5rw68j9PT5Y7725s6yJOFSjNzp0YXLCfkvWYjNL61MuFaPlNdPJZ0RY_0zh_QCnEOjMlV2vmuNiK2eIW6LHOlYrGfeoLeoCAidaNVfJ0tANPNXDpmTEcH1DUWgSMDBhXOIRNhpUEccMfEfQ6YfwK3YEOaPvKGF2UNcH5QauMrGfUer57_GEU1N8hPMMoA4C0N643KvewN3ocYOVf_yiM1DYHC8wVx7BZQ4QyXUjVS26JqcHWLtPv3jjh8kkjC77gCKbnA_XSc9hsu7gT62fUYR9STlOS2Z0-52nC9I5oKWdrzzcDiTo7fg4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2415cf5901.mp4?token=S7uov_ImEDguszyD7Fl5MwkFII1ZBbuQAUlEp1ILUXBI2qIARfZkDgQD9DV7hO0_msuaaE7BnFOySHRbhtV87rmYFE4qaA1dJNiA_5hAY3TeetBcYkyRI3o5tlmboQPISwepLZSnxFRPE9PHyZhbUfHKzZzStMUocS0KkR1FTPcafJpkRGFdhOSgxq7RJShT3Gmt9IBJwR4G1uHQ-XZFZrTYkJDr1zZofmIVkGhHPSKa408YlpPNHDb2komRAoOlXR9HROubYm-KV8vApAE6jFdCjmUSqGmOkxTJS8cDl78HJ79ECyArhqsqGkZsXUxTSVhdWEKMXhiDNxF4KvuW1WqX678dblRHh1WY_mW-wI6mswdkytNh5rw68j9PT5Y7725s6yJOFSjNzp0YXLCfkvWYjNL61MuFaPlNdPJZ0RY_0zh_QCnEOjMlV2vmuNiK2eIW6LHOlYrGfeoLeoCAidaNVfJ0tANPNXDpmTEcH1DUWgSMDBhXOIRNhpUEccMfEfQ6YfwK3YEOaPvKGF2UNcH5QauMrGfUer57_GEU1N8hPMMoA4C0N643KvewN3ocYOVf_yiM1DYHC8wVx7BZQ4QyXUjVS26JqcHWLtPv3jjh8kkjC77gCKbnA_XSc9hsu7gT62fUYR9STlOS2Z0-52nC9I5oKWdrzzcDiTo7fg4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع آقای شهید ایران «خبر اول» رسانه‌های جهان شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/farsna/447305" target="_blank">📅 05:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447303">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a903d21c.mp4?token=HFmurLbnhSZsmfHFefy8kWs3VuOYxpdSiUc7uq2Xhd86eHcVwA6QVvzgIzfE-Dr9De60NrFywLyjNndJmLU0lj4PEc3ncSIU1PAm8AL95d1uwrWekZq83v8AyLi4e5YNK6k3iBr1-bs1lLFUEvvg7sp7eSoRFKRoaahKvT8PTHBc6FSgXtIfXePSQeXyFCVnOQrsQ8Lk95AGtk40HEOR-F3yj0dA4mHnRKgE5xzqXAH8xl0tr8NwEqNq9Ki8i1SepYEMJtqTSnosNqPWQgKpgAgwrjAk3uEEmllWTuKoXG3jKl3GtY2f_XeoYtTwVH9bgayutlhOE2PkiUYKmLw_CqSyBZhlMfQH5dYEDlArfLjRHl4KCSDGDQ10LY-FvHutW8z0hxlLql7SgGvGfQ80Fs1m5TPBFBWiZ9QoczHFP1PFggBiIGn5Cp495XeOYl7Tf8Epr85Vbud_9jTXRC-VD_TQk1QQtJssO-1Qynbmh1BEWtjaFnR_FJzRxkmou5v-piJ_y1BaS6VKMW6s6x704XXsGjaf-6LU4GCeyaOWRMPWHNjFMeF1LiN5bjrI7T6paHbMaSGQAvQ1TwTGOcT3BO01Dy8ZbPEklznjalZswX_KmVUDWQeP1K4X_HmebetaqQrp6dlTiZ0XyiY48GCt61c63Ss63sALi5wy-GOl5PM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a903d21c.mp4?token=HFmurLbnhSZsmfHFefy8kWs3VuOYxpdSiUc7uq2Xhd86eHcVwA6QVvzgIzfE-Dr9De60NrFywLyjNndJmLU0lj4PEc3ncSIU1PAm8AL95d1uwrWekZq83v8AyLi4e5YNK6k3iBr1-bs1lLFUEvvg7sp7eSoRFKRoaahKvT8PTHBc6FSgXtIfXePSQeXyFCVnOQrsQ8Lk95AGtk40HEOR-F3yj0dA4mHnRKgE5xzqXAH8xl0tr8NwEqNq9Ki8i1SepYEMJtqTSnosNqPWQgKpgAgwrjAk3uEEmllWTuKoXG3jKl3GtY2f_XeoYtTwVH9bgayutlhOE2PkiUYKmLw_CqSyBZhlMfQH5dYEDlArfLjRHl4KCSDGDQ10LY-FvHutW8z0hxlLql7SgGvGfQ80Fs1m5TPBFBWiZ9QoczHFP1PFggBiIGn5Cp495XeOYl7Tf8Epr85Vbud_9jTXRC-VD_TQk1QQtJssO-1Qynbmh1BEWtjaFnR_FJzRxkmou5v-piJ_y1BaS6VKMW6s6x704XXsGjaf-6LU4GCeyaOWRMPWHNjFMeF1LiN5bjrI7T6paHbMaSGQAvQ1TwTGOcT3BO01Dy8ZbPEklznjalZswX_KmVUDWQeP1K4X_HmebetaqQrp6dlTiZ0XyiY48GCt61c63Ss63sALi5wy-GOl5PM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
متروی تهران، و مردمی که درحال عزیمت به مسیرهای تشییع رهبر شهید انقلاب هستند
@Farsna</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/farsna/447303" target="_blank">📅 04:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447302">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d332d41043.mp4?token=EVDduzgPyiaFQdlYF63sseGdrPt8ITKble6gHT_LZ83gfsePDamPQPEudgOEA55w21yyL7ftK8ZK1k1Y6vzvpN5R-vcV4stiZPNd5rwki8-CR0wscf3SLSspAov0Me2XA91PHYocEtHkr_LLA4SDpD-AuSqMfE4YSUcgHYy7H7ufQyPRNYXkfEz4w7fv68XQ5JuMUIebdLpnRNbkA-HihxbTL6rBrHPdr5iG5b7ZWbCD5hhKAm_Ltm4CHTd_Ri5z7VmKrnSPThcYiigHuOTgXERLBlXy01fiYe-RSCDNs71NrD3UWUTLCvPzt-JfCC4_X692CrdyMar58C8Xl016Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d332d41043.mp4?token=EVDduzgPyiaFQdlYF63sseGdrPt8ITKble6gHT_LZ83gfsePDamPQPEudgOEA55w21yyL7ftK8ZK1k1Y6vzvpN5R-vcV4stiZPNd5rwki8-CR0wscf3SLSspAov0Me2XA91PHYocEtHkr_LLA4SDpD-AuSqMfE4YSUcgHYy7H7ufQyPRNYXkfEz4w7fv68XQ5JuMUIebdLpnRNbkA-HihxbTL6rBrHPdr5iG5b7ZWbCD5hhKAm_Ltm4CHTd_Ri5z7VmKrnSPThcYiigHuOTgXERLBlXy01fiYe-RSCDNs71NrD3UWUTLCvPzt-JfCC4_X692CrdyMar58C8Xl016Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معجزۀ خون در روزهای بعد از شهادت آقا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/farsna/447302" target="_blank">📅 04:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447301">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حملۀ اسرائیل به جنوب غزه؛ ۲ نفر به شهادت رسیدند
🔹
بیمارستان الشفاء غزه اعلام کرد در پی حملۀ هوایی ارتش رژیم صهیونیستی به یک واحد مسکونی در جنوب شهر غزه، دست‌کم دو فلسطینی به شهادت رسیدند و چند نفر دیگر زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/447301" target="_blank">📅 04:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447300">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/503afd9156.mp4?token=JG9qNOw0Zs3-vSylI87o-VE372fEW3jbaLJgw1Y9Ki8Oz24C_H-7-ffzwdelwsWxxqMKxcxo12aOHPjD_-jlrrBagVZJGxmINwXna6ODtj16J9i8ipZpCgSL1i0pLXnJ1Le40NW3TVzs3X7rBNRYhLILwuv3n1aPtJhewlseu6Si2kpMVsUUA5QSCSi36GstboogDWB8BVXHMNcFpnlUUP-ivqsS7kuojFpsPM4PR5xwWVr18E5DJSlEp_cFSlyNExspAP6dE7NE26AWzHQiA6-CWoikYvG6HbFx0PLoROpKG8ILOKdoxpyJXr62sQo_gRP3nfCYyALTI5q6_q8sc6Hk58HoOvymfPPbIBmVWgkg0oN2g25Kb2ZAxVbqT4NomUE6jdVa5wVpnRxRYoaNTd_gc_Z3IEfc15h5aJKieT_Qk9zviLhvqhKsVKs6Ue3c54gn_DjyVk3UZSHCHJ_TZdYCVzmqTQZn2kWsLsEl-Mh4PezgasKuQUYcym7AqpPc8bwKVzIlUAT5y45ods4dtkawFuEmgXuxnVV_gS4RdS8MTrzzUUv2SLu2wl1iY3QOf3cJcCHN_iXlhysRlEgiqCDbsXAcqclbketPjsOWqBKBLTaMu6Ih6NFCctq3procQWfaaZXaN5i5urJzyl1Y5Xk-S4c9NcA77ZXNWNdJE2I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/503afd9156.mp4?token=JG9qNOw0Zs3-vSylI87o-VE372fEW3jbaLJgw1Y9Ki8Oz24C_H-7-ffzwdelwsWxxqMKxcxo12aOHPjD_-jlrrBagVZJGxmINwXna6ODtj16J9i8ipZpCgSL1i0pLXnJ1Le40NW3TVzs3X7rBNRYhLILwuv3n1aPtJhewlseu6Si2kpMVsUUA5QSCSi36GstboogDWB8BVXHMNcFpnlUUP-ivqsS7kuojFpsPM4PR5xwWVr18E5DJSlEp_cFSlyNExspAP6dE7NE26AWzHQiA6-CWoikYvG6HbFx0PLoROpKG8ILOKdoxpyJXr62sQo_gRP3nfCYyALTI5q6_q8sc6Hk58HoOvymfPPbIBmVWgkg0oN2g25Kb2ZAxVbqT4NomUE6jdVa5wVpnRxRYoaNTd_gc_Z3IEfc15h5aJKieT_Qk9zviLhvqhKsVKs6Ue3c54gn_DjyVk3UZSHCHJ_TZdYCVzmqTQZn2kWsLsEl-Mh4PezgasKuQUYcym7AqpPc8bwKVzIlUAT5y45ods4dtkawFuEmgXuxnVV_gS4RdS8MTrzzUUv2SLu2wl1iY3QOf3cJcCHN_iXlhysRlEgiqCDbsXAcqclbketPjsOWqBKBLTaMu6Ih6NFCctq3procQWfaaZXaN5i5urJzyl1Y5Xk-S4c9NcA77ZXNWNdJE2I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حقیقت حضور مردم ایران در روز تشییع این است: عاملان و آمران شهادت امام ما باید به اشد مجازات قصاص شوند
.
@Farsna</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/447300" target="_blank">📅 04:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447299">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎥
پیش‌‎کشی جالب به آقای شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/farsna/447299" target="_blank">📅 04:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447298">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a390a1978f.mp4?token=UgtFPvyDjqVzXhXeNQCE2H640TUzNa3BNNupYjC5BNPTBUtFNUQKn4uI7FBuPyvo748M6Skxo1Mi2mUXXH_wUtxXggt2-71sNKfREig-lMjBO23BlIIQ0nk8lcdGmsXo2PtHlPnYTCwsjBIjr30qFmEU1Y9mUwP13lI8g_XrK-LPvCxYB8i6LMKcS3fnE0RKcJY_qI7w49ydREDIjF8Y6-gYjqFmcQK5a5Pl_fhtIM1SjIqnAWVBmJSFa0zhYFW2hlWDU8hL_dy83l98Aq5KGRwvlODIxZQQKn1zivlk0H5xujdoQYtjedg0YAaP2URWW1GT39mELwLJSy1zwsuZdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a390a1978f.mp4?token=UgtFPvyDjqVzXhXeNQCE2H640TUzNa3BNNupYjC5BNPTBUtFNUQKn4uI7FBuPyvo748M6Skxo1Mi2mUXXH_wUtxXggt2-71sNKfREig-lMjBO23BlIIQ0nk8lcdGmsXo2PtHlPnYTCwsjBIjr30qFmEU1Y9mUwP13lI8g_XrK-LPvCxYB8i6LMKcS3fnE0RKcJY_qI7w49ydREDIjF8Y6-gYjqFmcQK5a5Pl_fhtIM1SjIqnAWVBmJSFa0zhYFW2hlWDU8hL_dy83l98Aq5KGRwvlODIxZQQKn1zivlk0H5xujdoQYtjedg0YAaP2URWW1GT39mELwLJSy1zwsuZdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهید طهرانی‌مقدم، پدر موشکی ایران از سید مجید نقطه‌زن می‌گوید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/447298" target="_blank">📅 03:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447297">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46aeca7a65.mp4?token=tps8Rab6IVbZQO4Pi_x9CMhfDGgb4FGY1Rr8AVuL70JOmfNPiA3FP0S1iHVooKbBGGk9OZJ0Y7mZrSDLEDvDkzrUknBvR_HtnZSOOVPBjznIWkQPUWEb5KfoCHREV9FYRxV07lXj6NPMbPrqnx_ShyJJYhjSh7z2gXLLT5CbdRp8YNQWefVbhzp35wq9dIwDPtJiKpzco4kJE0vEAwB6IyIrBRJBmB9ypRh0CH-mm3j5zCGeduGHbLE9prGC03cZBPCgv5lkVQh9R8-7Ec-TzIH1VJVkBn2ExrqXbL_h7ZcieiGxXm46XjoVldvztWWnQDKy_9B1LdmkPO9wcuOtgTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46aeca7a65.mp4?token=tps8Rab6IVbZQO4Pi_x9CMhfDGgb4FGY1Rr8AVuL70JOmfNPiA3FP0S1iHVooKbBGGk9OZJ0Y7mZrSDLEDvDkzrUknBvR_HtnZSOOVPBjznIWkQPUWEb5KfoCHREV9FYRxV07lXj6NPMbPrqnx_ShyJJYhjSh7z2gXLLT5CbdRp8YNQWefVbhzp35wq9dIwDPtJiKpzco4kJE0vEAwB6IyIrBRJBmB9ypRh0CH-mm3j5zCGeduGHbLE9prGC03cZBPCgv5lkVQh9R8-7Ec-TzIH1VJVkBn2ExrqXbL_h7ZcieiGxXm46XjoVldvztWWnQDKy_9B1LdmkPO9wcuOtgTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام دانشجوی آفریقایی به مردم ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/447297" target="_blank">📅 03:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447296">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/860521e59e.mp4?token=pW4izN3R668-jpXrH86ffslQUojgiuyVio6vIML5M5Fp7GRZJpObWmQXnOyTLzFnrA31BBH5AAU0_2CCCGmaBMJiiA8wuBXOtorWacRdoNLnYQDfCNRfXdkY9ynVSjecQfuEKFwF_mS3pU0SpOPVpo-Emnrb8gjzEU4okn_t2KL1waNYvbJrhiUPBhVgcy4mcQFRHcDNeLW8vdJjOkCYQTFZX0QS1iXzLvN5b5TWeQ1SwBnRavDfvlD1CwozZskhzIJsiUsjJjH7XKSxzbwEr0J8ylYHBhkDSKzV7GXMtf0SDonfir37kjMIlO_9a3mXir_rHwdSopZFv46zTwP2oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/860521e59e.mp4?token=pW4izN3R668-jpXrH86ffslQUojgiuyVio6vIML5M5Fp7GRZJpObWmQXnOyTLzFnrA31BBH5AAU0_2CCCGmaBMJiiA8wuBXOtorWacRdoNLnYQDfCNRfXdkY9ynVSjecQfuEKFwF_mS3pU0SpOPVpo-Emnrb8gjzEU4okn_t2KL1waNYvbJrhiUPBhVgcy4mcQFRHcDNeLW8vdJjOkCYQTFZX0QS1iXzLvN5b5TWeQ1SwBnRavDfvlD1CwozZskhzIJsiUsjJjH7XKSxzbwEr0J8ylYHBhkDSKzV7GXMtf0SDonfir37kjMIlO_9a3mXir_rHwdSopZFv46zTwP2oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این جمهوری قائم به مردم است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/447296" target="_blank">📅 03:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447295">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnfQI-kJNWrXGwv_A1NS3ROVsBYepJBauLGYNDkTSUL9QxSRpmb4RdqcGcuQ5NtFyk6_z8H1twKwxkV5xHUFQXj93rJ4BOqxmcBhfTxeV3AcS_rD7dUvCzNpHLXIWs9BgQ2xUyRkYG0sGxyssUjxGjHWeH6nXNZDV31Glf0hkWcCj-NBLOcKbh5Qnox7NqV-iRmFnJtn0opyvjgXZ95w3zjAds7pO6aFqj_1EoGjHl8YToax9_MpSYYVFlyTQwhK3R5tdwlN2bzSVpR8KuhHVnJV3HeoTF-ObklMZwvSjR8VCw5kvctPxLDe7zIaSpqDXJE9uShyXqD9iwjVIJwPjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
لیست پارکینگ‌های مراسم تشییع رهبر شهید در قم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/447295" target="_blank">📅 02:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447294">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_PhIPbkQ7R97ceNODcWnO6UIQyAXsOj5K_4Dp0ei_549Cs82T0aqN6ZV93oZo_StK-b2kSZD-jY_IpG5w4LUg7OmKbSh7NiSKKALXTU4MKyMe84jDqeCb_JY1I6AeVuOaeTvJQz9dVEyR1ZP3c2ItdN61FPCJA7RMQJ9JUbsE8A_ifWSIDUsd3sbYmwqX_xR_Dk1gnkulz4OfgRa4HyDlL5qn-_2tT3zWozd_nQf4NjLmqAFGYBOHfCheX_RZYYHoT-bJdPjXA0HQjnEtIL4Nen_c1OAZtOlJZ1SxnRcfHfagDRSyc6czC1ulXsxOPJWBUZoRf9n7v8whddUfR6MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
دیدار مکزیک و انگلیس به‌علت شرایط آب‌وهوا با یک ساعت تأخیر، در ساعت ۴:۳۰ بامداد برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/447294" target="_blank">📅 02:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447293">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">صدای انفجار و آژیر خطر حملۀ موشکی در پایتخت اوکراین
🔹
خبرگزاری فرانسه از شنیده‌شدن صدای انفجار در کی‌یف پایتخت اوکراین همزمان با به صدا درآمدن آژیرهای حملۀ موشکی خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/447293" target="_blank">📅 02:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447292">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKi0H4BiBehMM3Fcu150amyv8YqHdfFaI6yEMTyTNg-_8bgH89Zev6a8VUlU6cmeWMPmOvGYgqzaB5SEYIbz_XgDpK1KsVcmeBS1u-IGLrJQBlfFwzvVXzDZ20Lh21iGMiIJXFftgWNZ8kyIQNEb-qwkDPZBpCeNfaEC-m1vNmz_ywaNn-QRbv3YkDc5KaYQNh0w21ingnL91vYLZ3rs4iCRPh0mKSndvyXH9DxGJaDA4_Zkml9xEnmbrhNpRNwXQ5Q7p24htCaP1M3aV6Jh4TN19slVXzV1Ha1HzRDeTUxWlzyWnkbw9VnUjXcP_1u3NCacw20HBq7j-exncLHBtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تلفات ونزوئلا به ۱۷۱۹ کشته رسید
🔹
با گذشت پنج روز از دو زمین‌لرزه پیاپی ۷.۲ و ۷.۵ ریشتری در ونزوئلا، آمار رسمی تلفات به ۱۷۱۹ کشته و ۵۰۳۴ زخمی افزایش یافته است.
🔹
به گفتۀ رئیس مجلس ملی ونزوئلا، ۶۱۱ پس‌لرزه در این کشور به ثبت رسیده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/447292" target="_blank">📅 02:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447291">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbRiWOxKzFnrj6kt86mJzZYG__-0Ysgd7Lofj_ejS8BhDrRUYcInAj5meehUZ_fefXpYGLzt1mdsD1FfYVVHhWJTalV6HA4HMFw77NLJ6QUcFdJwxoP7XdQ6u3qdJhEG0SUQno6gUL-RndSXg8TMqNsimW4f2qDnGNrpzBIpLAX4QmULIvur-SIOXY7sMV2lpXJrSkcKmzGtEh6_eeN0rroWdewf3ropwOYsb3y3TrsQLq6B9d2UM9inaMamjOw7jlrmi5Zj07mcMG1iomuOUVbVnqSkYIYbioAPml3cReIjPM5liI-sxE3AR-XHzS6rkNOdAFtuYem0c-4IvGw4mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریم باقری اولین بحران تارتار در پرسپولیس
🔹
مهدی تارتار پس از معرفی به‌عنوان سرمربی جدید پرسپولیس، اسامی دستیاران و همکاران موردنظر خود را که در سال‌های اخیر نیز با او همکاری داشته‌اند، به مدیران باشگاه ارائه کرده تا کادرفنی جدید سرخپوشان هرچه زودتر شکل بگیرد.
🔹
پیگیری‌ها نشان می‌دهد مهدی تارتار تمایل دارد کریم باقری همچنان در کادر فنی پرسپولیس باقی بماند، اما شنیده‌ها حاکی از آن است که باقری تاکنون تمایل چندانی برای حضور در کادرفنی تارتار نشان نداده و همین موضوع آیندۀ همکاری دو طرف را در هاله‌ای از ابهام قرار داده است.
🔹
حالا باید منتظر ماند و دید در روزهای آینده مذاکرات میان باشگاه، مهدی تارتار و کریم باقری به چه نتیجه‌ای خواهد رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/447291" target="_blank">📅 02:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447290">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfdv7Lq8SG2L2AV3XAosz4vydJb0ytMR5pgKe-0_d20rxQ9aMG2Z1tBhNovHTSrdN-EHeCAObhYgrIN8R-cDp50BIeXIZuyZDqcgoBrZxcPjqgMNeeSqP7sovY9KR9GA2L-DON9_Qg9EhdHZnIkPGRy2w3bbn9Y1aeTMbG5bsWPflKhSAEUkfcQrgjsOw5d1xpl3Rb_zpTEzt1-bniii90VXSxzY-D8orFWjNaNvhSj6f83pyXxipzpgQZMF0rO01caWWrn9EJfrQVF0xZ_2f4ISFV4MZjYxtUcmD24mOtdIOjl1PYnOXaVr4J2q2WR_hhs2Q0iZTZJYQIHPRYmlHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلوک‌های سیمانی «کشوردوست»، سیاهپوش به مصلی رسید
🔹
پسر جوان با ثبت حرف دلش روی دیوار سیاهپوش مصلی می گوید: «آقا جان! مثل دیدارهای بیت که حواستان به دستنوشته‌ها و چفیه‌نوشته‌های مهمانان بود، یادتان نرود قبل از اینکه ما و مصلی و تهران را یتیم بگذارید و بروید، سری هم به دل‌نوشته‌های این بلوک‌های سیاهپوش بزنید...».
📎
اما مگر این بلوک های سیمانی چه پیام هایی برای رهبر شهید دارند؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/447290" target="_blank">📅 02:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447289">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8a5d084a.mp4?token=XDQNMqZfkfyxDQrxeb5QTiRIZEeiGk6lEjxYOirf9IDDBiVNHYWGg4wgdWuPqqvxXzUGviJ9hMGFzWOxrFjzV3KgvnP-0DGFIME2P8gwWUU4ePv81JATRq_xIrVT4YyjLoU_sfkKz6UQGttUvgHq57kCg1EGMj4NN_3Fv3IHyKyKKINm7uuC1u6ip1ABSOKsEtQGG0F3mznNl-Xt0kgeP2DPDVak67gmjxROhM8bAnD8sErJm3eOHqXuRgi05KfmkNTM36yFGsH9xz9CZMJAqYM3IBbVehzLrrvoLrl5wvgC7VAIkhb-794yENXfu4A1TCNUe9JudS0wSMkQ1mG_EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8a5d084a.mp4?token=XDQNMqZfkfyxDQrxeb5QTiRIZEeiGk6lEjxYOirf9IDDBiVNHYWGg4wgdWuPqqvxXzUGviJ9hMGFzWOxrFjzV3KgvnP-0DGFIME2P8gwWUU4ePv81JATRq_xIrVT4YyjLoU_sfkKz6UQGttUvgHq57kCg1EGMj4NN_3Fv3IHyKyKKINm7uuC1u6ip1ABSOKsEtQGG0F3mznNl-Xt0kgeP2DPDVak67gmjxROhM8bAnD8sErJm3eOHqXuRgi05KfmkNTM36yFGsH9xz9CZMJAqYM3IBbVehzLrrvoLrl5wvgC7VAIkhb-794yENXfu4A1TCNUe9JudS0wSMkQ1mG_EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
️
به رسم همیشه در دیدارها، حرفمان را کف دست‌مان نوشتیم که شاید ببینی و بخوانی
@Farsna</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/447289" target="_blank">📅 02:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447288">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91581c02ef.mp4?token=TZ1sjSjNz0lRsdyHuSF8yYOd60eTTognQ2jSISWbRDC4em6EyXQzCyoxWQdy0_k-o3TNHQNJQXmkt6FnH7WCyDzp4Gh7a3c2w9bxh8cmYu6OFg4XeN_F1aAN9m5gzOIzytSm9fLahKaxdhdpxfpO573AP6tPsxE_rHxHqnpI_57kERhyduztABDM6CNMxVyqs54A2O9cdQBIkX-Vm-1tNdjeGUPVhroR8-wVFdqV5Eh5JFJBg6AMRgfiFoo4RXd6zwnpDI8P_7cjp-ANTaJf_TIgUqVVNiqncV054N6BuFB1tHFktgmh8gpBhzfmZuM-L3NSwucVkJbm_WkZ6sNDogFBFTcoIQzDPDiBjvvlpxMIQEdVnCTtB21fSXarNnRY5kh-PlofPwJpV_RiJCo3ADFjHfA0r_KvFIK6-68M6U2EagmX3YFOqeJEsWtdDWcukNUIVTCAzx8vATmy7W1oOQPmbKqTfzQ6S4G-Ogisqh9xip2FjLXsIB-MVZwuiNBcKYkTnGfQzicObMkCr4T5ZLTKmYZiBF-dWXZl2A7lQQfjeXtpPzc7NsyGDDCircVQqo4Vb3TDO2h7rfCuUX1VauSV0qin8dk1dRkOFIwgVtz0lUVuF-tMS_y7eOy3XjAut30Izm3PgDe0Ao4nYMDex5aDBpR9K5Pt5o9puQ2EX38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91581c02ef.mp4?token=TZ1sjSjNz0lRsdyHuSF8yYOd60eTTognQ2jSISWbRDC4em6EyXQzCyoxWQdy0_k-o3TNHQNJQXmkt6FnH7WCyDzp4Gh7a3c2w9bxh8cmYu6OFg4XeN_F1aAN9m5gzOIzytSm9fLahKaxdhdpxfpO573AP6tPsxE_rHxHqnpI_57kERhyduztABDM6CNMxVyqs54A2O9cdQBIkX-Vm-1tNdjeGUPVhroR8-wVFdqV5Eh5JFJBg6AMRgfiFoo4RXd6zwnpDI8P_7cjp-ANTaJf_TIgUqVVNiqncV054N6BuFB1tHFktgmh8gpBhzfmZuM-L3NSwucVkJbm_WkZ6sNDogFBFTcoIQzDPDiBjvvlpxMIQEdVnCTtB21fSXarNnRY5kh-PlofPwJpV_RiJCo3ADFjHfA0r_KvFIK6-68M6U2EagmX3YFOqeJEsWtdDWcukNUIVTCAzx8vATmy7W1oOQPmbKqTfzQ6S4G-Ogisqh9xip2FjLXsIB-MVZwuiNBcKYkTnGfQzicObMkCr4T5ZLTKmYZiBF-dWXZl2A7lQQfjeXtpPzc7NsyGDDCircVQqo4Vb3TDO2h7rfCuUX1VauSV0qin8dk1dRkOFIwgVtz0lUVuF-tMS_y7eOy3XjAut30Izm3PgDe0Ao4nYMDex5aDBpR9K5Pt5o9puQ2EX38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این خصلت آقا زندگی‌ام را تغییر داد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/447288" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447287">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvoVtIlkBosISU9ZEsxJw83d3Y_NH87uHKTIyZ6kjhTCcXtBQm-VQoRZJW64vFAvVCx8KrKu9VY6mlWoNVxRLe1PTHdvePKI04mAhEv05cZrj10SdeZ5naeWGkIcIvWdg7Fri2mF8URkbfqStHK_fpQC2OV1LWMmgOnu2DQnbm9NHDCIRR3lC3e6VTWvEKm4bPJhe9ZkdY-wiPsjQUPEboirgNir2lPDfQKgyeWaZyU-tikGeuiKXLvH3T2VllwD8dWeRjnWJn9VUXx63eVWdFAaj1EBMJz-oYFdxouXMR64bN9hU_FLssf1p2anrMKU4WioZueLHVTqy9MDsGgyvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نمودار حذفی جام‌جهانی ۲۰۲۶ پس از حذف برزیل
@Sportfars</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/447287" target="_blank">📅 01:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447286">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4f7a9b09c.mp4?token=Ctptx3EHUPbmkR-MJ-cIWpQIxp4jAfZ5g86dzvMJ7LCSIMXJQy8pHt7DBxN83J14rHyG0h2TEBW35rubNk9YNfa4I2NHr7Mr7QyBks3F3e1MpAgfS9vpSfy3y2YLPzuu1FYJcDPP5sRiUauv2r_cFYGVNk6LtclVQu8h9Er8xqEiyHeKTxtTSK7IPGGGmOGGh4ZxX7MR9mJFBrH54S8ryEOqszF7o7UnipBGmhCh7ofKdceOEQTh3arVtR11JS127lMagBceurxKN2h5FOVUqGTp3tPWkw8yaJO0FKCO7hI7i3Jr0OHR2YljvVaN1b0n2Y8HVVpe1iB0zt-nHilD6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4f7a9b09c.mp4?token=Ctptx3EHUPbmkR-MJ-cIWpQIxp4jAfZ5g86dzvMJ7LCSIMXJQy8pHt7DBxN83J14rHyG0h2TEBW35rubNk9YNfa4I2NHr7Mr7QyBks3F3e1MpAgfS9vpSfy3y2YLPzuu1FYJcDPP5sRiUauv2r_cFYGVNk6LtclVQu8h9Er8xqEiyHeKTxtTSK7IPGGGmOGGh4ZxX7MR9mJFBrH54S8ryEOqszF7o7UnipBGmhCh7ofKdceOEQTh3arVtR11JS127lMagBceurxKN2h5FOVUqGTp3tPWkw8yaJO0FKCO7hI7i3Jr0OHR2YljvVaN1b0n2Y8HVVpe1iB0zt-nHilD6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین دیدار، آخرین نماز
@Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/447286" target="_blank">📅 01:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447285">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvOPa5SWRcDKSvoaPaB7FOxV7C8BEIEekEBHfoS7jNa_lVfvWhwLqlE8MRXs5qi1zU3XH8yiglGdIFJCI33jgcdSNADhLbYP2yCaKuiQkRnRQ8tmhbt6cqL01TfsGq_hrCUUkD1BQO_U3GWQlqHo_d1Gm8RxqT23ewmmMYl_gmcvzJnsxyWyFDwIs4AgrKjYauc8Emrn8XdOUhBJhai70cwt8elCcaayfUwnO71aVdpBCxAhzL9jHdSoznAz8C_YTGiD_pw6BpOpwdE_DHwK5FZ8FlZmHeTDgaL3OEDku65ZTprWk6OFRVRHsaZj1e96d0xWVegKwrz-QdE26n02pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برزیل از جام‌جهانی حذف شد؛ نروژ به یک‌چهارم صعود کرد
⚽️
نروژ ۲ - ۱ برزیل
@Farsna</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/447285" target="_blank">📅 01:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447283">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdbff5919.mp4?token=CehbuxGO63wHmb-ZxY29K-WZj0VJ9KuGeb2uu2DzxELKn8MjwwtKIAoXjkgrkc7FHQniYORAVtIwBKQn6SFpO5RMfrEO4uMIEH7d7FB1CHXHsOMTxaRUS4Vlv3wIIJWK1SjYjt9rINJFIc_eiuaT368EMgBffs6rSay-bGazsax-r-Xw5yOdA7Hkxi9VOQ-m0ATWGJu6MiTKinwmUw8sW2renhXGABNCdZlbZp0W6g6aJ3TIy60M8fzNHgPsEBUT3Wd65zeSAf-vpNCj7rHu0SrOgsIrUwlzzFX8JAk5UWNazzpB9Evmmt5177EkKOkSTwhrBnqa1sdKD-MhMqTQLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdbff5919.mp4?token=CehbuxGO63wHmb-ZxY29K-WZj0VJ9KuGeb2uu2DzxELKn8MjwwtKIAoXjkgrkc7FHQniYORAVtIwBKQn6SFpO5RMfrEO4uMIEH7d7FB1CHXHsOMTxaRUS4Vlv3wIIJWK1SjYjt9rINJFIc_eiuaT368EMgBffs6rSay-bGazsax-r-Xw5yOdA7Hkxi9VOQ-m0ATWGJu6MiTKinwmUw8sW2renhXGABNCdZlbZp0W6g6aJ3TIy60M8fzNHgPsEBUT3Wd65zeSAf-vpNCj7rHu0SrOgsIrUwlzzFX8JAk5UWNazzpB9Evmmt5177EkKOkSTwhrBnqa1sdKD-MhMqTQLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این دیدار با سال‌های دیگر فرق دارد...
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/447283" target="_blank">📅 01:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447282">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d884ee2d3a.mp4?token=rRgi6Ne42_ZolDQ5R8ju7YPELNgCG4nI6RUmUn7b2zPTartnRG3dsUgnYj_Q7v2uU7MHkw9W56MIN8aIqWZX_oqEBOmOdtDb5dhNO8gVFEsXPzsHfMCcMRlqZM8Nbkp8wqkh4u1WPXjIfwTvg2_XwmdOQl3dt1l74Ser5qYpeuuvNo1E1U6XBM6DDxuqSoKbolqRN5Ob_MKtHA0B5Oir0sRaKhteE2hvhUfR8AnSmxpLDB8v2oZ6SKH_miIsh93MEo5CM8tB_r9fAdlkwzPg4U0tB9XdPb6nycvZ2g7ytiqEFmiVEs7pOVz3PwMTOSTbbpxmvoit9XnCWRCpAqSSHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d884ee2d3a.mp4?token=rRgi6Ne42_ZolDQ5R8ju7YPELNgCG4nI6RUmUn7b2zPTartnRG3dsUgnYj_Q7v2uU7MHkw9W56MIN8aIqWZX_oqEBOmOdtDb5dhNO8gVFEsXPzsHfMCcMRlqZM8Nbkp8wqkh4u1WPXjIfwTvg2_XwmdOQl3dt1l74Ser5qYpeuuvNo1E1U6XBM6DDxuqSoKbolqRN5Ob_MKtHA0B5Oir0sRaKhteE2hvhUfR8AnSmxpLDB8v2oZ6SKH_miIsh93MEo5CM8tB_r9fAdlkwzPg4U0tB9XdPb6nycvZ2g7ytiqEFmiVEs7pOVz3PwMTOSTbbpxmvoit9XnCWRCpAqSSHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا دزفول، و دلتنگی مردمی که جا ماندند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/447282" target="_blank">📅 01:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447281">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eup1D8eWgefAHMsToVuCBx86YnDGNydIk-q9CrSIOFbmQIBHe1pkONwQhy7OUXrLIevRgaEq2pn9g9URR21ro35aqaXP-3LAcVbIXvILXy9pRKUCP6IURF3zc-oZ-ckORu_7ci3Runy3hnHdhn-9cL8dKVGLqoRlax-4kx0VxMHrreM530ksGJKs3US8Y5WiVFEh26hGNsmU-edijFiqJqYdr7t1M760KbdlE1cR9dRGH-4ZOSICXwUK43Z6D69vvteouCl67lgSk4uRq-oDnBkr-eTmU49cYQiv-FvD-S1UCHfH2sMKYnY78YWul1SujYWJsQgbkzBt2d08WI7W8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌سوزی‌های گسترده در پرتغال، یونان و اسپانیا؛ هشدار دربارۀ انتشار دود سمی
🔹
روز یکشنبه، صدها آتش‌نشان در پرتغال، یونان و اسپانیا به نبرد با آتش‌سوزی‌های جنگلی پرداختند. در همین راستا، اسپانیا و ایتالیا برای کمک به مهار آتش‌سوزی عظیمی که بیش از سه روز است در پرتغال ادامه دارد، نیروهای کمکی اعزام کردند.
🔹
مقامات یونان از ساکنان بخش‌هایی از «تسالونیکی» (دومین شهر بزرگ یونان) خواستند به دلیل انتشار دود سمی ناشی از آتش‌سوزی در یک کارخانه بازیافت که در میان شعله‌های آتش گرفتار شده، در خانه بمانند و درها و پنجره‌ها را ببندند.
🔹
همچنین عصر یکشنبه، یک آتش‌سوزی بزرگ دیگر در غرب «آتن»، پایتخت یونان رخ داد.
🔹
سازمان آتش‌نشانی اعلام کرد ۲۱۰ آتش‌نشان با پشتیبانی نیروهای داوطلب، تیم‌های تخصصی و ۲۹ هواگرد (شامل هواپیماهای آب‌پاش و بالگرد)، برای مهار آتش در جنگل‌های کاج منطقه «ماندرا» اعزام شده‌اند. مقامات در تلاش بودند تا قبل از تاریک شدن هوا و توقف عملیات هوایی، آتش را مهار کنند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/447281" target="_blank">📅 01:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447271">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/resW1B9Je4r-MU3hBUxpCBOunWlDqRFuyKxby3p-vn8xkS-fmWbs45ADQ6iqbrH7hAGmknynTeCzkd5D_Tuuwem19_L3zvBlwDP0XW0pttCAChkZpD0Aj39y-gnznXGZReLuZUUZKdfc4N0zCiV5ivNDQsqm8du3pgwnIPA5y3ZIIRUWoSsTctQLNrvkTJS09vWp0Cm96doAQS5WmAfZaDjMjhnMWhRh9UaNkKeHBFEAShJUSoCHDAIITLJRdHLd4tJozitrZFyjKyB_7Zy8xa_PZeBA7h7y_rtZ7GIv9kq3EI7w67UlCzBWfIQShfZ6aarvgvTgm-IoGYR6kwXquw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TzCtdsqpbzhKHMZEeP86ZSNtjq0GdnaTF9S4bSVv0MOj9O0bC8GfBzQJMskN64_EiJ959AV4aQM3pzX-HA-BLDdc-a7yZ9_NGcYGeRK9FIADvSZfpWOYU4nBkubDT88TH-QT-getLoZ8jNjGcAGgg4_cZLU292_UF4QBqdt1A-rJIhgSnIWh2p4teQj8_EkVHly39CJ9ARk8QOoJyNtHI9ok3_8NxpL5BQPb_7GkRziWagPoS2B0TsaeXg1LcWJdqcwJMUOMdm85n48qcUGz55uMuENAjTDuWAzohliwcvLZ7sgF-T4LfbuFXdF7EbUCXyp9MKy-hsjqdyLvo7PGYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jaBHlbgZ9K_8l_RlB5SV6ilX2SDj9Hbee4Xhw1nn53aNjJWXAn6_7KoRy0hYYNwLRoK7dwCFzY2SoUx3G5A6cLpGD0HUiZRhTswyizTtRHabSfF3i1oykePjJkbs1upNWzeoaon5I7iS1lPIL7l7v46VpdMmkTA9uQ6DCs-1O4vRHpljpKshcp8mSXPARbFqtDNuj4Y6dsLpwf35-NMdMxCnuuZcZt3wA0jUWA09SX83wP28puWy9CdQgDB2xFZBgumk7fAvCaJkcUkkj39iOfYsg6IGOgZ1ogFZxwwCgncocV4nteUmbfvtu7N19JOV0Z3-sBbQCMi7kekpYJPBgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oLBgJi35kdxcbwXWkl7qrUAi-8W12NGU8DSVlhkD3AOpZ4Ov0VXasbDsPKJjCmxWBSJhCtjBHqLCzCa7YV-cMNaxR9Y1mDDyln7abM5cw_M-PA-Qd8YQJLPQiqvc7_UMPjWu61QC4q_5U3ZvpEbOMkEdbUKdB1I88OEIg5XCLcsRiy0uW05b6ZhJFPXp2fkkW1Ee8gPX5wKyUk8QCKnwWICm74cx7Io7tBANsstWOGwhxnseChe2lYShoiBKn861W623D3PwfqeKzNq1ZO0JfSVIPtHk8KsKkNJd00zOLBJQIXjvesMgqZfwY5f-EC2L7Aba0SfgORGB2qLIQv9_bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stDKNHbfRCXsOrpOhrccevjQmSvwNb364fUgxhFUnpDEAkuhHiUTJPf-zbZocPu-2zhsi1-nIjVrXhNzl2zwDHdkhthtGE002KyXiOwuRzcOSmQd2gNAzwxLS5pk4kp0X0HcvJC1dXps4nOx-7k15HOhV-iO1FLPoTAkeL0wwCUUXehAbOv88nH_40aMkcCAOjScSKLm294g40O6o18EvAMkTsACy-cSgCAtWeYVp53vOwQq9qm6-EOp3Ye6iBMX2T6FjXrptbfcoMfdJMsEg4hTpuO2o9XXkB7_U-16q-PWG9qKuQH3Wdf0sF2DdwHMXaStMrz2g3RLmXpTwEpILw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/py_7znmnn1OxajbyXei2blzTp-D-nV3ySGDXnv54ASiT-qpn2gKbYSFiNUoajrpnn9kBcqghaK3kbe6lqh5y_hjIewcG_jMkKXFYQr4ZonM-G-JmuDmGWBagsSWp0qSVPzrNr-Qm63G-Y1LLSnmFNWXv-oLxDqXY_QBzVij1uVgFDB-_NMVcg_-Cg6Axwp2GMDfnnVwxctCIGy2gbOtaXI-_NQDyRm931qQy2FD6QTQEkIuJ70LUnA5kjGbVofmyUIjygwREhmrnmCODFpndDb20ktO76qB13wQr-Wqoty1fQmZHH00pDauYBdk0sKAx74C_wkdyPlPIPdxd19Ii8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W0RA2NrDPUhluQwCnQH6lPBDIpr9yWBhFIYaQutvajQx4FKUchKR97HUYJV0x6SXUUOhKnMChdJKnLYTofXZva_3otKOzO5ibPRVDVzNvTNXP7G-79aAVKeXvLS3LJkSuNWsT7MQbhx_11eod9e0Y-X4CdnB4IX6P5FxGL5QAFiOAGxC5kA8_SA16uYVTpjrRsEeF8KQiusnhfsD71KDqRPyloICE8NTEZZFiZV4BKpdRXvaNJqwjjkaFRAtqR8p1BE5dl7mDK5uauqUuFVG88u1ojJgeexTmKjcO199NvovPwtQtt4LVfdvMbl42MunWNiEU7E5ArhamJNacZB30g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eOipbfjlSh-LHE4aKG4i8iUrhmSCSvxEY49Rpn12f7DCwqaO_7gNS6IoozmGrU_TCXhsRn_Zrmmuif7hr1WENTo2zb5sT7_E3T0BWh_I6a3vBSl7LcKT3BHoxosz-xKbHmq0ORt1tKsOtnr4T6Qm2QzuG_6aP4-hjfCBpSFRNVVb1U_ArPI5qsunFN-oDrmJ4u9yF6ABP0rMwSwknjVRP0zenpempDctEIn0Do7I_82UpF9GG2qDwda4NPyrjsBuGaen3lCXMP4kXV_OK1Mnfv_hA4p4bXcVy2meAhmemeO74hetT5cTSW5J-ZOwFQhzu-DqoGxFDNlHK17Em5SncQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkoN6SZSkYScLKIurTQBRvVxmQID41fY9XILCrVP4Dh6pwFO9cpku-BKbhhe3AJRu-2JzjdTtNo2xyZIvmVWlE7rOY9pJFj113U4MlbggGMUzUKikERfgw9yts6L9ugiIm8KCBhkc6Z7cjqdKEzb-G-N6t4aaSmeWrZ8OMWIFbCjcHERgph1KGZjJZSP8pFDIaHhEvYgiDLQAiMr1BOIkknpldh4rwlGuKw7jG4X2O8BOHqADwRy4U922x2vV3o2g5zCGG5aM89qROs9YrKIEia9riRbBk67ESKvoFrYVRSOa7jQrbOc59sph6Ju08x5c7lpelZsyiQZkfjpSr6zaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uoPZp38SZHNiBi_OdNlO2Pschm2TqAW2CsRfKiaMo1lQIOxv3WrMtN6t-MrgwIf0a6ix0KrF7J_FhCiZzeyHUY59IIhHKX2gGbdgH6312jxDADQeXSH0XJj9IbPb5MLoKmqssOgMfPJ45VCUeKtZDA1ICkEeEJ4r3N_bu-A5yEiME6Z0kJcRFHB96NiRQoBM3Qszl0XCAl8lgWK3hFShCRa349b2RPABFRC-q3plAXSfQd7ui8pAM0U1MCZmPtjtvGStcsZTeStBzQCrw2OK6msvqdJjd1zDWNIpEcy6BbZUHi6CuMkH3pIhsf20B5X7GjuyACNq18UPox_z45DcrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۱۵ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/447271" target="_blank">📅 01:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447270">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c11ebc07.mp4?token=WIl1GHqKZJxiUiUe6jjIA43NJ9veUX519vSjmTkOlQP8PG7L2HfCe5uwwZiWXfPBiVnhGpUMJM_zOqEUnstngoOtTJ3dTNXJhm4DDVVBpn6twUe4WtYJPM26q0gYLwdxHSGXV0uEzuRl901tMMCUTTXiNDfvOCY4bfoIjubSJiA0m4ow7V-FD-az5bw4zRM1X9FzXQe0InNE6N9jxm5rsOURCdKBBiTNIZR0hIffS-lCCLq722_ohT1ywmZEnD6ZN0aV6f0Gv58sKPB5PLR8vO9hsImzQVw__YEpHLRtWlN7OyoTdjihRFPJm8C4JF2pQBmMgxsgUNp18etHz6uISA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c11ebc07.mp4?token=WIl1GHqKZJxiUiUe6jjIA43NJ9veUX519vSjmTkOlQP8PG7L2HfCe5uwwZiWXfPBiVnhGpUMJM_zOqEUnstngoOtTJ3dTNXJhm4DDVVBpn6twUe4WtYJPM26q0gYLwdxHSGXV0uEzuRl901tMMCUTTXiNDfvOCY4bfoIjubSJiA0m4ow7V-FD-az5bw4zRM1X9FzXQe0InNE6N9jxm5rsOURCdKBBiTNIZR0hIffS-lCCLq722_ohT1ywmZEnD6ZN0aV6f0Gv58sKPB5PLR8vO9hsImzQVw__YEpHLRtWlN7OyoTdjihRFPJm8C4JF2pQBmMgxsgUNp18etHz6uISA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تهران آمادۀ برگزاری بدرقۀ تاریخی آقای شهید ایران
🔹
بر اساس مشاهدات خبرنگار فارس، مسیرهای منتهی به محل برگزاری مراسم از ساعات گذشته آماده‌سازی شده و موکب‌های خدمت‌رسانی در نقاط مختلف مسیر مستقر شده‌اند تا با ارائۀ خدمات پذیرایی، امدادی و رفاهی، از شرکت‌کنندگان در این بدرقه تاریخی میزبانی کنند.
🔹
همزمان، تمهیدات گستردۀ امنیتی و انتظامی در طول مسیر پیش‌بینی شده و نیروهای مسئول با آمادگی کامل، شرایط لازم را برای برگزاری منظم، ایمن و روان مراسم فراهم کرده‌اند. همچنین برنامه‌ریزی‌های لازم برای هدایت جمعیت، مدیریت تردد و ارائۀ خدمات موردنیاز مردم انجام شده است.
◾️
آیین تشییع و بدرقۀ پیکر آقای شهید ایران و خانوادۀ شهیدشان از ساعت ۶ صبح یکشنبه آغاز می‌شود و کاروان حامل پیکرها از
مسیرهای مشخص شده
حرکت خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/447270" target="_blank">📅 01:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447269">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDnxHknm8AT6SrPVlAAwaYnXgWlbj7tswB-36yZS2QX9yW1nAcsebS7JfwtHNEPbU-xEPdgZGs_OfCyAACIr9wwGIZN3DVl-5f5wpa11ukRBkS8SH8NTwi2iKKauV7DihVpJER5H6DzrquGAPscmzBGyjAoAX4CcVeSQy-FDuvV1iwQ1LjrWAwBk7B3e4LEySPjMgK2VDbbj_qxgF2VBwSPEFbCxuGS23yAa7IBXcMOwo_opm55WBqA4TrqEU5jBj7TLp5vztubF3VSa3qNdCvTllHU07yLeBkGso3mtG_2LDYUJmTP-KRTSmUfUAmwQgwKLnVZyskexlXfyIhy5fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راز دعایی که رهبر شهید پای عکس ۲ نفره با محمدرضا نوشت
🔹
خانه پر از عکس‌های خانوادگی است، اما نگاهش همیشه روی همین یکی می‌ایستد؛ عکسی که هیچ‌کس در این خانه نمی‌داند کجا و چه زمانی گرفته شده است. شهید فرشاد(محمدرضا) پورمقدم کنار آیت‌الله سیدعلی خامنه‌ای که لباس سبز سپاه بر تن دارد، ایستاده است.
🔹
«عکس که به دستمان رسید، حال مادرم عجیب بود. عکس را به سینه چسباند و زیر لب زمزمه می‌کرد چه عکس قشنگی. دستخط رهبر تبرک خانه ماست...»
📎
ماجرای عکس یادگاری و دست‌خط رهبر شهید در خانه شهید پورمقدم را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/447269" target="_blank">📅 00:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447268">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شایعه‌پراکنی ابلهانۀ ضدانقلاب دربارۀ سیدحسن خمینی؛ از خروج زودهنگام تا غیبت در نماز
🔹
در مراسم وداع با پیکر رهبر شهید انقلاب، برخی رسانه‌های معاند نظیر اینترنشنال، با سوءاستفاده از خروج زودهنگام حجت‌الاسلام سیدحسن خمینی (که از نخستین ادای احترام‌کنندگان بود)، شایعۀ ناراحتی ایشان از تلاوت آیۀ ۹۵ سوره نساء را مطرح کردند.
🔹
بررسی تصاویر نشان می‌دهد این خروج، پیش از پایان قرائت و به‌دلیل عدم اطلاع از پروتکل مربوطه رخ داده و ربطی به محتوای آیه ندارد.
🔗
متن کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/447268" target="_blank">📅 00:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447267">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آماده‌سازی اسکان شبانه برای ۲میلیون زائر در حرم مطهر رضوی
🔹
ستاد تشییع رهبر شهید در خراسان‌رضوی: برای بیش از ۲ میلیون زائر در حرم مطهر رضوی، اسکان شبانه آماده‌سازی شده است.
🔹
بیش از ۷۰۰ گروه واکنش سریع جهت حفظ سلامت زائران در مراسم تشییع رهبر شهید برنامه‌ریزی شده و هلال احمر نیز برنامۀ گسترده‌ای برای امدادرسانی در جاده‌ها دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/447267" target="_blank">📅 00:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447266">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e61b3912.mp4?token=uKc2HkIFgiCZYvNq1rvw3FbEdz-8dkTVlRukjgSzIogZNRZGCgcB0meacbJBEdnKsSWznLpnz0vFfZrBLtVzdkZL2ExgSZNq3Ee4892IsFhTvsj8uun2VP-lRqykM3CEfjcn7_ItiqdN0hA6fEl80wCIpTeIabiyyDfVxCnJ_EIBsawdMgXJCeOPXtp44A7FXVMjDFELUO9CiQUqcG7cYSasULeyMjVHieLY9cuQNEL6GLdKdUU1UklW2-doV4hTLkP-ye7L-K8HXR-4kUsE6bMMAi5IR4lGVTp0_O1Y-hn-ZpMRcONrw9BZirTAQkrPkU_DzEDp4rH6vUYbZe-ZoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e61b3912.mp4?token=uKc2HkIFgiCZYvNq1rvw3FbEdz-8dkTVlRukjgSzIogZNRZGCgcB0meacbJBEdnKsSWznLpnz0vFfZrBLtVzdkZL2ExgSZNq3Ee4892IsFhTvsj8uun2VP-lRqykM3CEfjcn7_ItiqdN0hA6fEl80wCIpTeIabiyyDfVxCnJ_EIBsawdMgXJCeOPXtp44A7FXVMjDFELUO9CiQUqcG7cYSasULeyMjVHieLY9cuQNEL6GLdKdUU1UklW2-doV4hTLkP-ye7L-K8HXR-4kUsE6bMMAi5IR4lGVTp0_O1Y-hn-ZpMRcONrw9BZirTAQkrPkU_DzEDp4rH6vUYbZe-ZoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود ده‌ها صهیونیست به خاک سوریه در میانۀ سکوت الجولانی
🔹
ده‌ها نفر از شهرک‌نشینان صهیونیست در میانۀ سکوت و انفعال حکومت شورشیان سوری به سرکردگی الجولانی، آزادانه وارد خاک سوریه شدند.
🔹
در همین رابطه شبکۀ عبری «کان» گزارش داد در پی تلاش حدود ۷۰ تن از فعالان جنبش صهیونیستی «پاشان» برای نفوذ به خاک سوریه در منطقۀ جبل‌‌الشیخ، وضعیت در این منطقه به آشوب کشیده شد.
🔹
ارتش رژیم صهیونیستی نیز با صدور بیانیه‌ای مدعی شد ده‌ها صهیونیست که ساعاتی پیش قصد عبور از مرز و ورود به خاک سوریه را داشتند، بازداشت و برای تکمیل روند قانونی به پلیس اسرائیل تحویل داده شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/447266" target="_blank">📅 00:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447265">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ورودی‌های تهران شلوغ شد؛ ۱۴ ورودی تهران بدون محدودیت باز است
🔹
رئیس پلیس‌راه راهور فراجا: بار ورودی ترافیک به تهران از تمام ورودی‌ها پرحجم و شلوغ است.
🔹
با این‌حال هیچ‌گونه محدودیتی برای ورود به شهر تهران وجود ندارد و تمامی ۱۴ مبادی ورودی تهران برای تردد زائران باز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/447265" target="_blank">📅 00:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447264">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a18b4fe3d2.mp4?token=CEtxtklf5ff4RuzEVeKLMxWT1-nyTI5AliLBRbFHGme4xHGUk3UdqMOBUR1F2jWi-L3nDtimk_ymnYVOhaD-7Rm9884PjIoLiLgfJV_P3jnjA5SvQ0JVD6ad7-1A62UM6XNNIguWHIkr1z0KUT4g456ViMD_33k_jIbp4vJawLmx7JrV651PuZ-Dp_7apuJAaIex4-KtGLju9BT9hGov5hiNPwLrkIlpdjIDdyHhG1z-YqvtsPU6ajOT5Z8L_D8-q4bTgcTYA373JkSDaQPVEGGn1QH_nW00kdXrluaoY2aUTGM3j5FnukUzXOu7HwMW-vXmyTmLmcsPWFFKTWBSQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a18b4fe3d2.mp4?token=CEtxtklf5ff4RuzEVeKLMxWT1-nyTI5AliLBRbFHGme4xHGUk3UdqMOBUR1F2jWi-L3nDtimk_ymnYVOhaD-7Rm9884PjIoLiLgfJV_P3jnjA5SvQ0JVD6ad7-1A62UM6XNNIguWHIkr1z0KUT4g456ViMD_33k_jIbp4vJawLmx7JrV651PuZ-Dp_7apuJAaIex4-KtGLju9BT9hGov5hiNPwLrkIlpdjIDdyHhG1z-YqvtsPU6ajOT5Z8L_D8-q4bTgcTYA373JkSDaQPVEGGn1QH_nW00kdXrluaoY2aUTGM3j5FnukUzXOu7HwMW-vXmyTmLmcsPWFFKTWBSQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تهران آمادۀ بدرقه تاریخی «آقای شهید ایران»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/447264" target="_blank">📅 00:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447263">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc2918bd10.mp4?token=FQQvXhFYl5xV6_qEgKyO3lE12-K_mghzd6dtNdIenubREjC-GPykOTqilwh12sOE2sZo_YjAn5eN2YuMi8Rs22_sspqoJi766MolF15IxFCvNiAOfLgZTKTmMi4iZkpYCmGGYJjTGsMUeNgb5ZvuvMbagMcBmfHcrAgiqAmaFMAFfzdYTN1qOidFprQMn3Kr4aY5C0LMtrHQoKWvrL_4s7LolzNO3DlCJrDgwN7Z7rxUqC6RpPcAWvkeXj6w5H9T3zCKQ_ZnDWdbjbFCLLQ0W1U4ul45VKYp4-gOlk3xfss0yWe3nMmT2YwaRryfSWl7lDReJBLcUua2SIvPTmNzxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc2918bd10.mp4?token=FQQvXhFYl5xV6_qEgKyO3lE12-K_mghzd6dtNdIenubREjC-GPykOTqilwh12sOE2sZo_YjAn5eN2YuMi8Rs22_sspqoJi766MolF15IxFCvNiAOfLgZTKTmMi4iZkpYCmGGYJjTGsMUeNgb5ZvuvMbagMcBmfHcrAgiqAmaFMAFfzdYTN1qOidFprQMn3Kr4aY5C0LMtrHQoKWvrL_4s7LolzNO3DlCJrDgwN7Z7rxUqC6RpPcAWvkeXj6w5H9T3zCKQ_ZnDWdbjbFCLLQ0W1U4ul45VKYp4-gOlk3xfss0yWe3nMmT2YwaRryfSWl7lDReJBLcUua2SIvPTmNzxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرودۀ جدید افشین علا به مناسبت وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447263" target="_blank">📅 00:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447262">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e2779e53.mp4?token=lox4zIcQ-FHDBYcYPuZTB1-rXb-NnR6k5YD7YDLTZSmZTh0uuGpA1rF5RTsPVIrRrKy8XlGWVclAi8zphsTIvL79o8fv6UIffgtwpuAKcQ_jIhPy2Rs0Zljjfh3rOJz6qvXPqzWkQjrva7VbirGq4Y2_odQuber66-WkzK8fQZdWoXJf4E_F3znbDYR8grLb-8hroQBQbsLZuJ5liTFwb4_8eFgIwk11YF5Wpb5XyX3_zEhrrw1DIrNHcN1F8MvRMbTPSKjZ9PR9qrICfy2CaJQTtC8zcPjPbvmGPSsUnTgMvy3aZb5FIT24LBlageuSJWRFjNNb641wjFR8IOr9VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e2779e53.mp4?token=lox4zIcQ-FHDBYcYPuZTB1-rXb-NnR6k5YD7YDLTZSmZTh0uuGpA1rF5RTsPVIrRrKy8XlGWVclAi8zphsTIvL79o8fv6UIffgtwpuAKcQ_jIhPy2Rs0Zljjfh3rOJz6qvXPqzWkQjrva7VbirGq4Y2_odQuber66-WkzK8fQZdWoXJf4E_F3znbDYR8grLb-8hroQBQbsLZuJ5liTFwb4_8eFgIwk11YF5Wpb5XyX3_zEhrrw1DIrNHcN1F8MvRMbTPSKjZ9PR9qrICfy2CaJQTtC8zcPjPbvmGPSsUnTgMvy3aZb5FIT24LBlageuSJWRFjNNb641wjFR8IOr9VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهدی تارتار به‌عنوان سرمربی جدید پرسپولیس انتخاب شد  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/447262" target="_blank">📅 00:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447261">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqsEvr0TrbfUwN9g8NXcnhwxCMo-fwbAyxXhx5yjBoqz1kEoTUmtnXQ1E3ztFerKusl1gNinFzlJqqjwZ-VkmNAwyi0fJyGnOeL2dQTpzf6ozZfA2yNEdDIUp496ytmGkcMd1uhEsgyDemkmXWnAgrqGrnei8q7iOy6y3RRuBnb7PYgSBjKwkbSnnKDYyE3BQ5RH-yrZ4xqyPJxKMEq6RGa9Pa9rEubAjusKc1kF-AJL4yWUXVNiHPRquKMKD4W0yM0UsbZha9D2v0ASa7PCwbsEJHSa0TOMT-5tG1J0CgbziOwkzo-TKB3nLpTt4hmsGxjCCeTJRRkg-oDn2-WQNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوب‌تر از خوب، بدتر از بد
🔹
«شقرانی» مردی بود که پدرانش آزادشده‌ی پیامبر اسلام(ص) بودند و به همین دلیل او خود را وابسته به خاندان پیامبر می‌دانست.
🔹
در زمان منصور دوانیقی، تقسیم بیت‌المال برقرار بود، اما شقرانی به‌دلیل اینکه کسی را در دستگاه حکومت نداشت، از دریافت سهم خود محروم مانده و بسیار گرفتار و درمانده شده بود.
🔹
او روزی سرگردان کنار خانه خلیفه ایستاده بود که ناگهان چشمش به امام صادق(ع) افتاد. شقرانی جلو رفت، مشکلش را گفت و از امام خواست که به واسطه ابهت و احترامی که نزد خلیفه دارند، سهم او را از مأموران بگیرند.
🔹
امام صادق(ع) با کمال مهربانی و بزرگواری وساطت کردند، داخل شدند و طولی نکشید که سهمیه شقرانی را تمام و کمال گرفتند و با دست خود به او تحویل دادند.
🔹
شقرانی غرق در شادی و سپاسگزاری بود که امام(ع) در همان لحظه، بدون اینکه کسی در جمع متوجه شود، در محیطی خلوت جمله‌ای به او فرمودند.
🔹
امام که می‌دانستند شقرانی شراب‌خواری می‌کند، با لحنی بسیار نرم و مشفقانه فرمودند: «ای شقرانی! کارهای خوب از هر کسی سر بزند، خوب و پسندیده است، اما از تو به‌خاطر نسبتی که با ما داری و انتسابت به خاندان پیامبر، خوب‌تر و زیباتر است؛ و کارهای بد از هر کسی سر بزند، بد و ناپسند است، اما از تو به خاطر این انتساب، بدتر و زشت‌تر است.»
🔹
امام(ع) به او فهماندند که رفتارش مایه سرافکندگی خاندان پیامبر است. شقرانی با شنیدن این سخن، به.شدت تحت تأثیر قرار گرفت و شراب‌خواری را کنار گذاشت.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/447261" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447260">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P45BsHDbqIjmaBjVVTGI6-A0ZNY9-RBrHP-xD6pFKkr0NkuiRop41BoL9NgOWsCXRABeSq3FX31Eb56VUwbk0ZeFa2HMu4oqWVIv_oqWp23C7kTJCV_ZK0oAHS4t4n0UzpbSNaEGoMIRgZm3GSPWitFDZWFfJQLgxOlsvrn4J9PtnjnT_CyFVGhj8IOGHMJSq3KNTr5voTtHofgpogQxdn_SYK8vOTZorGPbgIucxi9zTAtV7JAzMkSJDqrS7yev453Yo6OynhXnf1Pd0ZWpWNpttMeGfTqYN4lAgQyjbnVchJlvPes7RZHmojYmMnQleqdDScLHqQfD2mNzbTvT9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
| دوشنبه ۱۵ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/447260" target="_blank">📅 00:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447259">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9w2somzkrc7DkX-4JvK3iFPYBtkoIYpSSFnLDx4aHm9G8vTk0IEBScgIovAzCaR-qW-LSFOEWh9SQ5ieaXHcNE0ph7eaEeR4579_LWAVbTX6f6UluKXfI-PSi-AiUAex7pcUcfJpAENFWfSzFShJRgDMEd7vUu-WW9HB1dLdHRSYgRyHfLjzcjUTr4Mb34K9oH4BUHI2tUPK_EeLosqKfVavXiWUyfBtmlCk94YsQ2_5Bzl-wQQSRRtt-n275vpKfXJTMxD1ZD3PgQEXuL5Xt4vozhXnYoGxJaK7mtLjftSdY7PlosfjEVHre2EBNy0dx4We5H4B0F632ElOMlY2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به عشق رهبر شهید به بچه‌هایتان تاریخ یاد بدهید
🔹
زنی تنها روی پله‌ای نشسته، چوب پرچمش را به زمین تکیه داده و دارد رجز می‌خواند. نه به رسم ۱۲۰ و چند روز گذشته برای دشمن بلکه این بار برای مخاطبان داخلی.
🔹
برای مخاطبانی از جنس خودش می‌گوید: «آی مادر! آی پدر! بچه‌ها را دریابید؛ بچه‌هایی که امروز، اسیر رسانه‌های خارجی‌اند؛ به کودکانتان از مردی بگویید که ترور شد اما خودش هزینه درمانش را داد».
📎
صحبت‌های پرشور این مادر ایرانی را
اینجا
ببنید.
@Farsna</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/447259" target="_blank">📅 23:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447258">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf1c51221a.mp4?token=WJ-eelKuIXav6ip_DaJD1qdg0BjjOHqMWIUMW2JJslk94TLLx3KuBr_yHYgW0xMdE1e7t-tFihf827sLzlsNDLccCpUIx-K4o_w7lnQOZkE9LmRw8b-iMYMBvlAjyF6HGEUKc267LlsBWQy8ec2bNPNskR-d5e3FS_8LTycHxtd7dCfA0EXc-oZDryvYsZvmjXNHab4pjAxX3Y_T7tBAzRp56FKj8cbYIOAvZ4gF43G6HWfzyRd8e-xZ4ahi5M1iDoMaqKfaDFxDpN_5VMvpP5C9vLBS0s4kEq5ZIs3yEQTD4GRn6mbB7-DDcDBW7xdhtylsBC0gA7ZyEJ7UdvrZ-RZw8Ib8-TqaY2TNszZo-ksIzkiXyG0Z70tGMzYogqRca05IanbwJfuzDdLzeXi63oNQFcxq5ToiyQzWWK1QxJ1DDLsunDJ2oAC3DDjFY0-VfXn_Y3XVVrw_SGMsNj3nUC8Ng5Ce_aABbElT7ug6mHWoD7PSpLK9PB3HLhx29ohH09aSdMV2ZBQ6K1uhrKKuijVP0f4H9pi1xwzzSC6ClaSFZevNUl4vNFy0woXdpekFGea3MnaTnXNtgxTWIs7iSvIvOnXYfMHynvt5tv2bWQkeGXeyeds-Z-WmXaAwo1-JaiFyxU3BDnOFA5ENMg2tANcPIM9rEUQXXk67gsfkdSk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf1c51221a.mp4?token=WJ-eelKuIXav6ip_DaJD1qdg0BjjOHqMWIUMW2JJslk94TLLx3KuBr_yHYgW0xMdE1e7t-tFihf827sLzlsNDLccCpUIx-K4o_w7lnQOZkE9LmRw8b-iMYMBvlAjyF6HGEUKc267LlsBWQy8ec2bNPNskR-d5e3FS_8LTycHxtd7dCfA0EXc-oZDryvYsZvmjXNHab4pjAxX3Y_T7tBAzRp56FKj8cbYIOAvZ4gF43G6HWfzyRd8e-xZ4ahi5M1iDoMaqKfaDFxDpN_5VMvpP5C9vLBS0s4kEq5ZIs3yEQTD4GRn6mbB7-DDcDBW7xdhtylsBC0gA7ZyEJ7UdvrZ-RZw8Ib8-TqaY2TNszZo-ksIzkiXyG0Z70tGMzYogqRca05IanbwJfuzDdLzeXi63oNQFcxq5ToiyQzWWK1QxJ1DDLsunDJ2oAC3DDjFY0-VfXn_Y3XVVrw_SGMsNj3nUC8Ng5Ce_aABbElT7ug6mHWoD7PSpLK9PB3HLhx29ohH09aSdMV2ZBQ6K1uhrKKuijVP0f4H9pi1xwzzSC6ClaSFZevNUl4vNFy0woXdpekFGea3MnaTnXNtgxTWIs7iSvIvOnXYfMHynvt5tv2bWQkeGXeyeds-Z-WmXaAwo1-JaiFyxU3BDnOFA5ENMg2tANcPIM9rEUQXXk67gsfkdSk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وعده دختر دهه هشتادی به «آقای شهید ایران»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/447258" target="_blank">📅 23:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447257">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e97073945.mp4?token=tM6H09siUtLDBHb88qphxpEzn0HEHIujvlj570fmFu65J4HdLVbuCx4d0rRMpxysgO1B4o2q-3nSzRq5iUfw22msJbPuVd1pdPnXlet_lMafD7EIyPRVNiuUP_TwmZEWTRPEZ7BssCgNJv553xeLBA7dGwTFrXk0rjB4XInRh89SPzwovDVzrOgIWRQ8HCgRJBnWQp5azX8xRfAUHEXY6-7jwJSWMuYtuO8xsU5Hw3cmoHgKzpgHP6wbDQzwD5DAEP4007lcogzrENeKv5lWTuVvhiNpmO8j_ID78t2AoEa_14tNEe8XfTvvnQUBLSZPHpLJrz95-yHIOCSEQUU07g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e97073945.mp4?token=tM6H09siUtLDBHb88qphxpEzn0HEHIujvlj570fmFu65J4HdLVbuCx4d0rRMpxysgO1B4o2q-3nSzRq5iUfw22msJbPuVd1pdPnXlet_lMafD7EIyPRVNiuUP_TwmZEWTRPEZ7BssCgNJv553xeLBA7dGwTFrXk0rjB4XInRh89SPzwovDVzrOgIWRQ8HCgRJBnWQp5azX8xRfAUHEXY6-7jwJSWMuYtuO8xsU5Hw3cmoHgKzpgHP6wbDQzwD5DAEP4007lcogzrENeKv5lWTuVvhiNpmO8j_ID78t2AoEa_14tNEe8XfTvvnQUBLSZPHpLJrz95-yHIOCSEQUU07g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آماده سازی جایگاه پیکر رهبر شهید در مسجد جمکران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/447257" target="_blank">📅 23:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447256">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eefcd0c2b.mp4?token=C2FpHrdj7ON_ngKBX6YIEnYUE517nj8e0L5bQGWd6c9j8tiXdpczoaYwB5rY2HECqrs_dRzyqKGeHc7q06Zd6Vxb0XKN1VpwTQvrLliehXuC-93HTLhFAFjwEd_6EsbNkBP334fX9W4va_ojDinR83q8YoImhzQieQjB5RD7zVkXrZcdCicVlfOSfCQr_Goncb2Vwo33vug0GIo8y6rx0HzILX9Z8x8Sfj8Slf9aB7tGnMRjWdWHKpGBp2rk1fzpp1UUfzolZXWmD_YEza-e9nTmEmuBl7LJa1E-V7OkSHhSwsaeaFNi1X12qLqyaTzVLMdCqaOCGlkB5HkzSzoAjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eefcd0c2b.mp4?token=C2FpHrdj7ON_ngKBX6YIEnYUE517nj8e0L5bQGWd6c9j8tiXdpczoaYwB5rY2HECqrs_dRzyqKGeHc7q06Zd6Vxb0XKN1VpwTQvrLliehXuC-93HTLhFAFjwEd_6EsbNkBP334fX9W4va_ojDinR83q8YoImhzQieQjB5RD7zVkXrZcdCicVlfOSfCQr_Goncb2Vwo33vug0GIo8y6rx0HzILX9Z8x8Sfj8Slf9aB7tGnMRjWdWHKpGBp2rk1fzpp1UUfzolZXWmD_YEza-e9nTmEmuBl7LJa1E-V7OkSHhSwsaeaFNi1X12qLqyaTzVLMdCqaOCGlkB5HkzSzoAjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگر بخواهید یک کار خیر به نیت رهبر شهید انجام دهید، چه می‌کنید؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/447256" target="_blank">📅 23:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447255">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02f93d2ec3.mp4?token=Cc4ukc6ZJ9jtUHwSMhrhPKLtKmR2BeLS8k6AjgadlHsmHwrgFU7GYhRNeyJjvVij4Wmkms_GSQvDbEAo049QmznY-HJQ9GyNR2ZDMM5_RYOBdBCmU3TGBdKWyodDG4fvVcWgAklCMjxc_1gIBjXMJDdN72tIhLbpvt4QrhSdKFweqFRly2Wrn8W2VHS9cJ1Td-cqwFxXeo514or-kwvspovs_x5txRMo3TfLXP8JsVr5vkj5NxFVMMgDmat2Jbez7OjRbv6AmGopKw_xhwWlFX_YLtRPSY48KYrBzFeEBBmewEt5lwhLahAg2VdiLPm5t0jGc5TCcEcv2O95w2JlFimFWeB0iiay3vfQHgngV6HWDKlLlsDzvS8ILpK5I6Xt3kxeETJ5If7ao65mmoMxF0xpFqb0qbUs0-DtqdzjcUivjtcQRluCkmkXce4wglGBOqNym4G606XX8BQCos-t8aiC3265MRToGroeM7gFhVaNi62gaUo6ek_uYAOwzA4EiTLLW1E3a0TYQdcRw0U6T2SRJrMpfOo-nnUQe8PRH2cYCNc3U6rOaMWiZL7IuueWuk7ZrA52sWjI77ERdydzJptYpeqfh_wHIMiQcZp8lW_dQQdU0UaC9AoDC-35cl27MiX4YWMKWJseE57RunhXOydvRRAG5-Q1pfCl70yc4OI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02f93d2ec3.mp4?token=Cc4ukc6ZJ9jtUHwSMhrhPKLtKmR2BeLS8k6AjgadlHsmHwrgFU7GYhRNeyJjvVij4Wmkms_GSQvDbEAo049QmznY-HJQ9GyNR2ZDMM5_RYOBdBCmU3TGBdKWyodDG4fvVcWgAklCMjxc_1gIBjXMJDdN72tIhLbpvt4QrhSdKFweqFRly2Wrn8W2VHS9cJ1Td-cqwFxXeo514or-kwvspovs_x5txRMo3TfLXP8JsVr5vkj5NxFVMMgDmat2Jbez7OjRbv6AmGopKw_xhwWlFX_YLtRPSY48KYrBzFeEBBmewEt5lwhLahAg2VdiLPm5t0jGc5TCcEcv2O95w2JlFimFWeB0iiay3vfQHgngV6HWDKlLlsDzvS8ILpK5I6Xt3kxeETJ5If7ao65mmoMxF0xpFqb0qbUs0-DtqdzjcUivjtcQRluCkmkXce4wglGBOqNym4G606XX8BQCos-t8aiC3265MRToGroeM7gFhVaNi62gaUo6ek_uYAOwzA4EiTLLW1E3a0TYQdcRw0U6T2SRJrMpfOo-nnUQe8PRH2cYCNc3U6rOaMWiZL7IuueWuk7ZrA52sWjI77ERdydzJptYpeqfh_wHIMiQcZp8lW_dQQdU0UaC9AoDC-35cl27MiX4YWMKWJseE57RunhXOydvRRAG5-Q1pfCl70yc4OI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدوبیست‌وهفتمین شب سنگرنشینی کاشمری‌ها پای عهد انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/447255" target="_blank">📅 23:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447254">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2407c70c00.mp4?token=jB2x7YUoyBiBpJBNK0k9VuZFnxFsP_fhKaEsPQdfg8Xygk9nuWmf89q8jdc1oI6y87rWh4CA9PlYelGmYhweE9IcYmFSUh9QlnLnPFd5glQR1L2R5_RhUxKGGNbuVFRTrkwQOwxU3YnzpOyjwku_pK73RpSWdqkO5ci8YVi8NAvsn4KE52nv-7n0dOeSRhTrcQSJ8zHF0IAfn6BsO9A38oLVVCOckrwkS2aMRD-eQLsIyM3fXoTuSiT0qAqivkiqrDb1bX9thmfFBhJ1trwm8anf6ZraOBm9YnoDe2MG0b5o1dDime-YEZm-VSoKNDw6BCqKEpfHShOUno8Pa7X9gjUxLMkMpMtaIXBVsF1_PqWkz3jPgAgfFTlC1utsr-BwBl9UnfTgYMQmzBuD_LmfRR4x-LVURBtdqLJ9Hr8nTuhxD_EVHEQ6FXmVjl3EmbdoltSeimMU_Kw6rF-jfIXIpVu_IOrV77K11hDqqxMLTFR14ip4JuYYrEJPgzMfX4pVMR81pT53kJ0uy4qIigjBRMTthFjqi6p1igg93QGhV0UU0pacrFSHbF7k-imECcwV5S7_OykfWUSuTPbIyQrwXBEmOpSRPrBr9iCYlC4GAAlm4k8aTFzcOsF8GrCdJgV0_dAzJhdYl8u3c8dP9BR4YlFD0UJwJA34DzCr17Ewq-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2407c70c00.mp4?token=jB2x7YUoyBiBpJBNK0k9VuZFnxFsP_fhKaEsPQdfg8Xygk9nuWmf89q8jdc1oI6y87rWh4CA9PlYelGmYhweE9IcYmFSUh9QlnLnPFd5glQR1L2R5_RhUxKGGNbuVFRTrkwQOwxU3YnzpOyjwku_pK73RpSWdqkO5ci8YVi8NAvsn4KE52nv-7n0dOeSRhTrcQSJ8zHF0IAfn6BsO9A38oLVVCOckrwkS2aMRD-eQLsIyM3fXoTuSiT0qAqivkiqrDb1bX9thmfFBhJ1trwm8anf6ZraOBm9YnoDe2MG0b5o1dDime-YEZm-VSoKNDw6BCqKEpfHShOUno8Pa7X9gjUxLMkMpMtaIXBVsF1_PqWkz3jPgAgfFTlC1utsr-BwBl9UnfTgYMQmzBuD_LmfRR4x-LVURBtdqLJ9Hr8nTuhxD_EVHEQ6FXmVjl3EmbdoltSeimMU_Kw6rF-jfIXIpVu_IOrV77K11hDqqxMLTFR14ip4JuYYrEJPgzMfX4pVMR81pT53kJ0uy4qIigjBRMTthFjqi6p1igg93QGhV0UU0pacrFSHbF7k-imECcwV5S7_OykfWUSuTPbIyQrwXBEmOpSRPrBr9iCYlC4GAAlm4k8aTFzcOsF8GrCdJgV0_dAzJhdYl8u3c8dP9BR4YlFD0UJwJA34DzCr17Ewq-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری مردم تربت‌حیدریه در فراق آقای شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/447254" target="_blank">📅 23:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447253">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712f858aea.mp4?token=LbDug6xGy5hW5DookPuGacZNWIfOXmx_w8N5RfiJWvl26x6PFb7PF8rQu7UDjBzDOlT2DOIxiarXCefBZ7MU_P47QYnwc4rE4ksOTrrv_mII7qFbfj7XyNtNrhBKnVbqDVbk3zDhp-sa7GdjPgNbSgHNAHcYwDoQm9ZsLqx8SdrSTYTWHuNLLQSmy3glYeGZxYWn9o8xgKAm8TEb_RX326sP8zh9GKjp_ILXkh8AQXhzLyVqCMwBITJTcptOalJnRsL8cr16WdgBARcYH_XQJdEAxlEcW_6GRZdSSAigKH7cU6CTDxAwKVeOCYgmJCS9dO5qOpERDZd_HdmXI0mYPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712f858aea.mp4?token=LbDug6xGy5hW5DookPuGacZNWIfOXmx_w8N5RfiJWvl26x6PFb7PF8rQu7UDjBzDOlT2DOIxiarXCefBZ7MU_P47QYnwc4rE4ksOTrrv_mII7qFbfj7XyNtNrhBKnVbqDVbk3zDhp-sa7GdjPgNbSgHNAHcYwDoQm9ZsLqx8SdrSTYTWHuNLLQSmy3glYeGZxYWn9o8xgKAm8TEb_RX326sP8zh9GKjp_ILXkh8AQXhzLyVqCMwBITJTcptOalJnRsL8cr16WdgBARcYH_XQJdEAxlEcW_6GRZdSSAigKH7cU6CTDxAwKVeOCYgmJCS9dO5qOpERDZd_HdmXI0mYPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت شنیدنی کمیل خجسته، برادرزاده همسر رهبر شهید از اهمیت دادن رهبر شهید انقلاب به نماز اول وقت
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/447253" target="_blank">📅 23:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447252">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/486ac6fc3f.mp4?token=XzAeiavoJVUhoRZYn1sT1RPyW-Q-YAWggiFeHU79S3zsZLbfBOx7mvoLvDmFACjEVneOuX4Adg8OOj97LTzJPqTh5d3iP8BvT9hfpEJ0kXzENMwOPOJFFMDZ5pCzM-gtAZrbh1Xshi-Pnq3vwROY-2SiX9lL-uhTI6oHRZg4rwVTqUpw8y6qr-8FOAFFRz8EbyEOKWV3etH-lBNTUdxJFjXZctNY-ISGHwbyADcUjBsoiJDpnpjH12MGS7R0eJT7cg4CL_YxtvpnB9FnRkiffdN4TUsdktEaQQZ4ZPcGWVkpzrYIyAkdNPONQQiAQbSm2E-6Cx8EFgTy0kKJj4oC0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/486ac6fc3f.mp4?token=XzAeiavoJVUhoRZYn1sT1RPyW-Q-YAWggiFeHU79S3zsZLbfBOx7mvoLvDmFACjEVneOuX4Adg8OOj97LTzJPqTh5d3iP8BvT9hfpEJ0kXzENMwOPOJFFMDZ5pCzM-gtAZrbh1Xshi-Pnq3vwROY-2SiX9lL-uhTI6oHRZg4rwVTqUpw8y6qr-8FOAFFRz8EbyEOKWV3etH-lBNTUdxJFjXZctNY-ISGHwbyADcUjBsoiJDpnpjH12MGS7R0eJT7cg4CL_YxtvpnB9FnRkiffdN4TUsdktEaQQZ4ZPcGWVkpzrYIyAkdNPONQQiAQbSm2E-6Cx8EFgTy0kKJj4oC0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
|
به پایان آمد این دفتر؛ خاموش‌شدن چراغ‌های مصلای تهران و آخرین لحظات وداع امشب، با روضه حضرت سیدالشهدا (ع)
#باید_برخاست
@rahbari_plus</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/447252" target="_blank">📅 23:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447251">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15ccb9daef.mp4?token=X-wKnJVs_5VdAv8GToJSf-byOHLQ8ubAa0XxeqwSG71ygwzxHixRIv996uU8DTG5_l7ttCs5bCCjHrrDgY8gGsCWNlJbs2f_9euEj8L_5oTB-j1xb7krlgtM1plp6M03YNgtlGKqxmSb7bGt7Vr9pHDulGGXB1eUTzPRtbe_D4vJrIYePlwwvVv3tA_B9SwQ-xBp0Fn8dl-OPuwznqtznJOnj-zRUc2uU-oIjzhywqgnI3UJvyzzkbSzMWyh0insMpLq9Qr3kxUNnInSjGMHhWysbtLvws16dILl-VOxxw0ezP3p9UnMSjrZ4-_m7u1AS45LTHpzBclypBcFJ_SQag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15ccb9daef.mp4?token=X-wKnJVs_5VdAv8GToJSf-byOHLQ8ubAa0XxeqwSG71ygwzxHixRIv996uU8DTG5_l7ttCs5bCCjHrrDgY8gGsCWNlJbs2f_9euEj8L_5oTB-j1xb7krlgtM1plp6M03YNgtlGKqxmSb7bGt7Vr9pHDulGGXB1eUTzPRtbe_D4vJrIYePlwwvVv3tA_B9SwQ-xBp0Fn8dl-OPuwznqtznJOnj-zRUc2uU-oIjzhywqgnI3UJvyzzkbSzMWyh0insMpLq9Qr3kxUNnInSjGMHhWysbtLvws16dILl-VOxxw0ezP3p9UnMSjrZ4-_m7u1AS45LTHpzBclypBcFJ_SQag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خدا صبور کند در غمت ما را
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/447251" target="_blank">📅 23:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447250">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e141fcec4.mp4?token=H9X_zFLfNdcadA2CJSOw8NOMy_tbDMsVqQGRz_LsHO_ZQemhc5n5PHQwdlmtnZXl6-YzJiJI_RXqjNLhzsLJ5ffFZ9r95oTuy_1oEhQYHCwgR8znRgW0uI3Dhbe-Jo4GeF8VHGiCIg4TxY9bA6lOYdDrLqrBIIMqGaWcU41Wf4PlHguSBuHk0oJKwLibFFH1cDuo-u9KZhGIZ8ONZ7MY-O4OwX8EObUsmK_BAF2Uq5d4nmM6S2-pU5uJrJzxhi2GZ10bLzERCzulZJrj_7OF_pSRg3mX-0i7acARJlUwPWGn5ZPiV43_K8xulehy834tyTXZZeBUY01W83WKDGrGSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e141fcec4.mp4?token=H9X_zFLfNdcadA2CJSOw8NOMy_tbDMsVqQGRz_LsHO_ZQemhc5n5PHQwdlmtnZXl6-YzJiJI_RXqjNLhzsLJ5ffFZ9r95oTuy_1oEhQYHCwgR8znRgW0uI3Dhbe-Jo4GeF8VHGiCIg4TxY9bA6lOYdDrLqrBIIMqGaWcU41Wf4PlHguSBuHk0oJKwLibFFH1cDuo-u9KZhGIZ8ONZ7MY-O4OwX8EObUsmK_BAF2Uq5d4nmM6S2-pU5uJrJzxhi2GZ10bLzERCzulZJrj_7OF_pSRg3mX-0i7acARJlUwPWGn5ZPiV43_K8xulehy834tyTXZZeBUY01W83WKDGrGSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین سلام به رهبر شهید از زبان امام رضا علیه‌السلام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/447250" target="_blank">📅 22:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447249">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d300c6813.mp4?token=IGbagwxgL08zpEbLUbCRVAReqACG5p2Mk9cDO4TmW1vCzonpmlIEqVV5bzNktyUORLaES9BKSbHQzCq_hg8fjNCiWnOaqMGs6ptIWDIF1jrnZfMNMm94jfLZrcoO58r20fi-VxSjCrj9ZbeYqKAd6bixVDMuUrek43jphAfHaAI4PRzsJK1-sYeoV2tKO0rQ6dQIW0nZhdDNv5gAnDXP1l5382PP-v35r5zW4f8NdOB2OnOdK_HP9zL_9lJinwbqnJ5suo_2H5PGyQcn8n9cwK1NXnJwtUunX6MQ1YS5Cj7XNpL8woTnbR0CeyWu8T73c6qzJjBrBDIsj6KZQp5irA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d300c6813.mp4?token=IGbagwxgL08zpEbLUbCRVAReqACG5p2Mk9cDO4TmW1vCzonpmlIEqVV5bzNktyUORLaES9BKSbHQzCq_hg8fjNCiWnOaqMGs6ptIWDIF1jrnZfMNMm94jfLZrcoO58r20fi-VxSjCrj9ZbeYqKAd6bixVDMuUrek43jphAfHaAI4PRzsJK1-sYeoV2tKO0rQ6dQIW0nZhdDNv5gAnDXP1l5382PP-v35r5zW4f8NdOB2OnOdK_HP9zL_9lJinwbqnJ5suo_2H5PGyQcn8n9cwK1NXnJwtUunX6MQ1YS5Cj7XNpL8woTnbR0CeyWu8T73c6qzJjBrBDIsj6KZQp5irA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گوشه‌هایی از مراسم تشییع پیکر شهید مصباح‌الهدی باقری، داماد رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/447249" target="_blank">📅 22:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447248">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64e84926e3.mp4?token=dEBZKTOvF_m-d4AncW_iKmWHQpM9FQOFsFrbvb3euap20wLGtmTpTg3Pbn2R8Jrbw5ixz5ZZH3KUEk_WsLkRrDmL2fAt8-LxLWdrshgB8MTyykyP8jTL94LGORbDT_MV8WhM_73zPsif5QULDZucnQ2-P4JWAtx8qF3M9aDpPfWP-cAG67gFzLtMW_9ejC1JUKqwGcH0RdrkVWgvYIUZ4jIK9lLqWr3G8enKSnnXe69w9ZE5JySkbm_A_a606t5hSnGB3hxRweWzfXqRoB589juLxwHQFLKNHwNNuyREhtVGZiWGMOJ5BLJTu0BCwMCUWmB5Buc6uV1xiF_zxkw7BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64e84926e3.mp4?token=dEBZKTOvF_m-d4AncW_iKmWHQpM9FQOFsFrbvb3euap20wLGtmTpTg3Pbn2R8Jrbw5ixz5ZZH3KUEk_WsLkRrDmL2fAt8-LxLWdrshgB8MTyykyP8jTL94LGORbDT_MV8WhM_73zPsif5QULDZucnQ2-P4JWAtx8qF3M9aDpPfWP-cAG67gFzLtMW_9ejC1JUKqwGcH0RdrkVWgvYIUZ4jIK9lLqWr3G8enKSnnXe69w9ZE5JySkbm_A_a606t5hSnGB3hxRweWzfXqRoB589juLxwHQFLKNHwNNuyREhtVGZiWGMOJ5BLJTu0BCwMCUWmB5Buc6uV1xiF_zxkw7BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رانندهٔ این تاکسی، زائرانِ رهبر شهید را رایگان به مصلی می‌رساند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/447248" target="_blank">📅 22:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447247">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuxDWacRIMTHsbblHQ988pMZn2gxTCdRO39Of3OU40lA1wbL6Noi2N_DUOwpst0a9c797kiWo3a9n74BrxtU_fgVe7YCBbBz5qEYdY3x-GXorLkgWru4Yq4bbGguIx7mA8IhfcGgAB1XsaGoh0QyPuuI-njs7-8ZrSeJGB-ghUPl_w093BCHOMKnVgFvZEIgriCL63-Qz4hytYB0H5BBNF_iL6EkIx_M3nDqkeXlcayRZGkZoDnDMs8Z863jK3qkDjwxMC-49x289nSo9L-pCaLEJl5YrcKPsWGRcwvl0RAqZnlUSpa1-8-YppHZuV5cUx6cmzJBx0QVi4TdCYW6yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: دیپلماسی به دنبال تثبیت دستاوردهای میدان است
🔹
رئیس مجلس در گفت‌وگو با‌ محمد درویش، رئیس شورای رهبری دفترسیاسی حماس: دیپلماسی و مذاکره باید بتواند گره نظامی را باز کند و دستاوردهای رزمندگان را حفظ و تثبیت نماید و این مهم زمانی محقق می شود که کشور…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/447247" target="_blank">📅 22:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447246">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
مردم در وداع آخر چه عهدی با رهبرشان بستند
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/447246" target="_blank">📅 22:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447245">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7df973e0e.mp4?token=rOZs9mQmJhHpWJQvqFXj_JcJM10kVljaZN2ccWXEN6fjkarU7i5f9CVgpxjRnltwfZrz847623D97-Ic7IXy0n3lqqENpuh9_SGyJA4vvTSwYcFGsFMBalPRbLU0XHp3sOLNwb9PG-_0WYnkDA3dSya_7NOaRZLodjgimM3uA77i2vhe537uTjdN6pzzNK02gge9XunOGiO4_EVscu3jvwO4Mcmup_TcRTl-kckGDKL_Srxs5lJsdDkh-VEWqe2vgff_9SPfjTFTgjd2S2MJf6frd1xuxzyHuMdQkYllRSwvfi61UeVTklLyuGLxcaq4ADNZPQKvb49uEpGQ-0jU6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7df973e0e.mp4?token=rOZs9mQmJhHpWJQvqFXj_JcJM10kVljaZN2ccWXEN6fjkarU7i5f9CVgpxjRnltwfZrz847623D97-Ic7IXy0n3lqqENpuh9_SGyJA4vvTSwYcFGsFMBalPRbLU0XHp3sOLNwb9PG-_0WYnkDA3dSya_7NOaRZLodjgimM3uA77i2vhe537uTjdN6pzzNK02gge9XunOGiO4_EVscu3jvwO4Mcmup_TcRTl-kckGDKL_Srxs5lJsdDkh-VEWqe2vgff_9SPfjTFTgjd2S2MJf6frd1xuxzyHuMdQkYllRSwvfi61UeVTklLyuGLxcaq4ADNZPQKvb49uEpGQ-0jU6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دردی که حتی کوه‌ها را می‌شکند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/447245" target="_blank">📅 22:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447243">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفالس نیوز</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YYgOIwfrDsfO-tn4xqrRSQu_SuG3J9K1EM_9YovpQFMUFApvctAOrngm-AaOP2YEY0R6QGWjeTjaSNbZ6CY-UqAu8sYrmcKQSqtPn3BeRiTs-NW3__TTeLlht6xPO4fE3rXlCsYcx1Y2Tajcd17-K9Rp1WN0Lcq97_MQo48c_BgEbNYhzDMKSE0bRKHAE-NDnGqSID5ciONg8WFdRL3f0NlTpaqrjHN8AM5_wrInTEFZTeJsNx10DieMkHaBbIItXc1T9al9US1aljHvIBw9yrqlST2Ki-vyutp2RF1RYr1f3smYL-T_LXrfLOvXPwLm4BD4zeM7QnH6r8cmJKJw2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LKujN3EWMiHbT4iVvR4ttIxrfRq_PhzKm_XccGCQaI3CZLkPl8nUmfc-MPKjjIMYxs-ekYtlBn6cXMsj1dfVUMEjkXWjC7i5C2b5QC9Metc2bsMT2J2FRwxKOdJ26SvQlBrUhEQBrKMUe29ckBTLgz95I8SqPQMS-SoBgRRWr41m7HjvFm2LsklMidOtRP2J5K6Ci6FFZzLdp9tgC4gYPfPZ3ldtL6H9E3vte6MenOxddgTrmbq5Vh2UMVoS8HEwH5zVggvL6Ft9i5ErYzfBVXrzDhwwfzz-a1c3rhTr0p_A1mYiqRjh_FsQ3vdWQP4K9mxOTG_rQ5SWmSNx_hHcwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبر اختصاصی اینترنشنال درباره رئیس قوه قضاییه هم دروغ از آب در آمد
!
❌
در ادامه تحرکات رسانه‌ای اینترنشنال و فضاسازی‌های ضدانقلاب برای هموارسازی سیاست‌های آمریکا و اسرائیل، این رسانه چندی پیش مدعی تغییر ریاست قوه قضائیه شد.
❌
اینترنشنال در راستای اختلاف افکنی در خبری اختصاصی مدعی شده بود: [آیت‌الله]مجتبی خامنه‌ای اژه‌ای را پس از پایان دوره پنج ساله ریاست قوه قضائیه کنار می‌گذارد.
✅
این درحالی است که آیت‌الله سیدمجتبی خامنه‌ای  رهبر انقلاب اسلامی با صدور حکمی حجت‌الاسلام محسنی اژه‌ای را بار دیگر در سمت ریاست قوه قضاییه منصوب کرد.
@Fals_News
-
Link</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/447243" target="_blank">📅 22:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447242">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🎥
ویدیوی حشدالشعبی برای دعوت به مراسم تشییع رهبر انقلاب در عراق
@Farsna</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/447242" target="_blank">📅 22:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447241">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef0be33eb3.mp4?token=pG1P9tNkGet-dW69w0hbBNIL77iJdLafVyR_2A2syJ7GbRunb0sdKqWeBzYzPGEB7DDdW46xD3nGu90xue_joLXO1f91c1EJ1rf2i3es2arHYg3mHiplzcO2SYQtrRAD0PhjlGGMfDCWrDTPVr2gFvm8jkbjxuvf4do-WrEEOpY4GSjOLsnFIbT6kT8RmnEnWVO5-cNkc3zS_VjdHR-SHKsQB8Grd0EmuJU0bLoBIKp_mYWLUiDDoiofcVEZ5x56ef4SpqZ5CYGrmZpV-8uH6XJkQCYLtuWtYIv54RqX2UDZdAAW0K0lRYohN48jJbZ6nnJ_npEOak2I2QSQtKzMsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef0be33eb3.mp4?token=pG1P9tNkGet-dW69w0hbBNIL77iJdLafVyR_2A2syJ7GbRunb0sdKqWeBzYzPGEB7DDdW46xD3nGu90xue_joLXO1f91c1EJ1rf2i3es2arHYg3mHiplzcO2SYQtrRAD0PhjlGGMfDCWrDTPVr2gFvm8jkbjxuvf4do-WrEEOpY4GSjOLsnFIbT6kT8RmnEnWVO5-cNkc3zS_VjdHR-SHKsQB8Grd0EmuJU0bLoBIKp_mYWLUiDDoiofcVEZ5x56ef4SpqZ5CYGrmZpV-8uH6XJkQCYLtuWtYIv54RqX2UDZdAAW0K0lRYohN48jJbZ6nnJ_npEOak2I2QSQtKzMsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان: اگر حال‌وهوای امروز و دیروز عاطفی‌تر بود، فردا حماسی‌تر خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/447241" target="_blank">📅 22:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447239">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f921ab159e.mp4?token=rh31q-SjbaA4Q3LYUE012kU7R7DP01gsOaEWZyRLdKn18ogj2ac0cdusKjmcnrWQhavr_QkyEnHwoKkFSxInpMQ8uT36YnwYkGJqjK74ib-AnB7iGJ3st0jEVG_FuTMsKQNMVp8Jg0pa5lgKGBdKPcwVtRzfLHwmZ6aIkcVFI94H1jJCnCbqcqyg6W11b8NKRGkwn609anjj_0dTrb2XI6rnOS9H0zA6B92yLWYLW5O4WlimkRD_Ux3PFFHyueH16QwUmA6qgVmoz3-5eHlb0bB7hUQZfK9StiVHLdzSMJlJZvcfyPxP32ZOSVnjMNkdTkheReNqJYkqQ-bziK2Tig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f921ab159e.mp4?token=rh31q-SjbaA4Q3LYUE012kU7R7DP01gsOaEWZyRLdKn18ogj2ac0cdusKjmcnrWQhavr_QkyEnHwoKkFSxInpMQ8uT36YnwYkGJqjK74ib-AnB7iGJ3st0jEVG_FuTMsKQNMVp8Jg0pa5lgKGBdKPcwVtRzfLHwmZ6aIkcVFI94H1jJCnCbqcqyg6W11b8NKRGkwn609anjj_0dTrb2XI6rnOS9H0zA6B92yLWYLW5O4WlimkRD_Ux3PFFHyueH16QwUmA6qgVmoz3-5eHlb0bB7hUQZfK9StiVHLdzSMJlJZvcfyPxP32ZOSVnjMNkdTkheReNqJYkqQ-bziK2Tig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ وداع آخر با رهبر شهید در مصلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/447239" target="_blank">📅 22:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447238">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3203834f.mp4?token=N-qV0Grk75vp_V2X1-1_PE3YAz4_yquCyNiU8P703u60wAy9BmNBCMs9rhK2NVsrQfAmy5OGhqhA2RklrL48J_5xBQamc0L5IQoCkZJcPgTCeK9ffD43FEOR0t5TPWWQ2wRVgY5tZqWn3_2I21AIJBxWULoZz8xMb0kqTPmRZoRye8V1oV6_BC0v_AVHIK-fpaf3JNBvPKqOHVSWS0e9IPpZVAyW1yvROXVxzx8BDuLZjFqompgUhxEB8H7iYLoCSCV28I7KJAwGlxTIaJHPdLgBhy4z89ljvLO_rDuk_hyT6_PnG5X1z-scsybzxcw39ZMU4rw1QlHGusmoj-BqfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3203834f.mp4?token=N-qV0Grk75vp_V2X1-1_PE3YAz4_yquCyNiU8P703u60wAy9BmNBCMs9rhK2NVsrQfAmy5OGhqhA2RklrL48J_5xBQamc0L5IQoCkZJcPgTCeK9ffD43FEOR0t5TPWWQ2wRVgY5tZqWn3_2I21AIJBxWULoZz8xMb0kqTPmRZoRye8V1oV6_BC0v_AVHIK-fpaf3JNBvPKqOHVSWS0e9IPpZVAyW1yvROXVxzx8BDuLZjFqompgUhxEB8H7iYLoCSCV28I7KJAwGlxTIaJHPdLgBhy4z89ljvLO_rDuk_hyT6_PnG5X1z-scsybzxcw39ZMU4rw1QlHGusmoj-BqfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اللَّهُمَّ إِنَّا لَا نَعْلَمُ مِنْهُ إِلَّا خَیْرا..
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/447238" target="_blank">📅 22:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447237">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d2881a783.mp4?token=O7hcREtrkQHgipkYXBhXDk9jBTU9LCPzR3v3sWuBoCzMNu-YtXMz55xaFzpvjZamJK21bYxPaqdimS4sJ-kPe361HQeugOfNmorGXhpN47YSefTSHSAY4n7CxLSkHkV7SG3cKlYXX69sO5x2iZqLbLsJD8pthf5fLxNIwYlp3tyhCR8N27-daroTDTC9PYQmGTHtMxvKzzWlDRfEj6FMbJZvvEQwxXvpkiufyKuMsiPSBSVhK8vmkULLl0x2kzNRSMREuGLA0h-3d2TJQrJvXu0k7AzRf9FzsKGxV9ncRa_MGNWBZbXVO7n12-r2EtHkULIuQ62sj2vMRIOTu7kQmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d2881a783.mp4?token=O7hcREtrkQHgipkYXBhXDk9jBTU9LCPzR3v3sWuBoCzMNu-YtXMz55xaFzpvjZamJK21bYxPaqdimS4sJ-kPe361HQeugOfNmorGXhpN47YSefTSHSAY4n7CxLSkHkV7SG3cKlYXX69sO5x2iZqLbLsJD8pthf5fLxNIwYlp3tyhCR8N27-daroTDTC9PYQmGTHtMxvKzzWlDRfEj6FMbJZvvEQwxXvpkiufyKuMsiPSBSVhK8vmkULLl0x2kzNRSMREuGLA0h-3d2TJQrJvXu0k7AzRf9FzsKGxV9ncRa_MGNWBZbXVO7n12-r2EtHkULIuQ62sj2vMRIOTu7kQmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت علیرضا دبیر از دیدار با رهبر شهید انقلاب پس از کسب قهرمانی در مسابقات المپیک
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/447237" target="_blank">📅 22:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447236">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/789d4d5328.mp4?token=oNgz5XIo-Vk0WL-Be7gIvltwnJnAy-PKzYBk__OXHYoqkiJWi6_1uVUTyD-mG6rZtQ-WPOYi5xuka6cWGCUDyUVtlrQO7tfA_7P3Y5xlhCONlMyZfNrssYZRL-WnZ3Y2yYQQFXli5-4QyaA2Qe7sR-vd9lcQ04vj_fYHgWm--6niUIC8cJ1dly8TmakJCCadM3HcIgdkXDDC8EIQZHAH_f5W5hcPLpR4LYFzFRN10UTw0Fyoy6EyI3ovyml28YNbqt4rECj63t3_9fnbZuEZsJAF14exgCUmQHiFkXKhd7l0_hXGieNevSzg9Onm81rJMud2Efv66uTEk7idyCUcor2j9C6XBWk0u3TUCh3Ik_81Yb-ihsPI8t8I5QU7KP8rsD-Bh5vgZMioFSTzEogpdkFZgKKFsOtLoerbxIPwHrC0bynGC-yvH6FCD8bFXYvbnHW6KdLhbyiFxAlG_hV480FCkARE35f5f395LXAE2-oRt2BrCGda3BAU2VeQ94pIMO6Ke5VIUHmnN21jyV3KoBqR1JZZ7c-GLVK1msiamU_tmAYvmAl0aQx5Y24DxjqeBYmLCh03eOBqLMctSugrcIXKJuSNbz3HQfv0PGQO3rF9FzeG9CIYVtIg217AUvn5JR3I4ggOWcibvi_-Tsksra926hf3OZgM9qaLHfbUDGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/789d4d5328.mp4?token=oNgz5XIo-Vk0WL-Be7gIvltwnJnAy-PKzYBk__OXHYoqkiJWi6_1uVUTyD-mG6rZtQ-WPOYi5xuka6cWGCUDyUVtlrQO7tfA_7P3Y5xlhCONlMyZfNrssYZRL-WnZ3Y2yYQQFXli5-4QyaA2Qe7sR-vd9lcQ04vj_fYHgWm--6niUIC8cJ1dly8TmakJCCadM3HcIgdkXDDC8EIQZHAH_f5W5hcPLpR4LYFzFRN10UTw0Fyoy6EyI3ovyml28YNbqt4rECj63t3_9fnbZuEZsJAF14exgCUmQHiFkXKhd7l0_hXGieNevSzg9Onm81rJMud2Efv66uTEk7idyCUcor2j9C6XBWk0u3TUCh3Ik_81Yb-ihsPI8t8I5QU7KP8rsD-Bh5vgZMioFSTzEogpdkFZgKKFsOtLoerbxIPwHrC0bynGC-yvH6FCD8bFXYvbnHW6KdLhbyiFxAlG_hV480FCkARE35f5f395LXAE2-oRt2BrCGda3BAU2VeQ94pIMO6Ke5VIUHmnN21jyV3KoBqR1JZZ7c-GLVK1msiamU_tmAYvmAl0aQx5Y24DxjqeBYmLCh03eOBqLMctSugrcIXKJuSNbz3HQfv0PGQO3rF9FzeG9CIYVtIg217AUvn5JR3I4ggOWcibvi_-Tsksra926hf3OZgM9qaLHfbUDGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیعت مردم با رهبر شهید در لحظات آخر مراسم وداع
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447236" target="_blank">📅 21:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447230">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dGY8WuhipwrZpacT-9WPuFLxbPiJzYm8qMtvC9pMWTURZajgNrVFxr4aAvR3cptYZsYwMghwFy-3bbbBf3iFukikqKxys7kDoxAqXW9VL_eoXZID3EHBM1uX4L7IkGlnO275hNk0A24x6u0HnAj-hBwZv2MrNpXsa-JQb3HtE7CDZ0we_O7pHzJ87kEj4-Q_p73VSKnDwiafP9qWuxJZpmr8knktYWD18f7CFgKHAatHa2_CQ2uTYCb0jp8WrJF3QETE5HEnQb88XFIKW3SZV_NRXkYrW9-15ablz3WuXWS60IcYYq25cE7-O25gcoYIGoML7zZ-B5VF07P5UIpWBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QfFVhOY64TSXTF3gC0gUvw1XemXXs7tgahV9JoZ0gUYN2pnuUl9W32tRgH7W3wwH6laxLlpnokE0V64c2z9a8Wz6AJJdICEBCU88SbdaWbVw7h3iEdhQoEXFm-KKxzk2UftVUDXY_YD0aHrBYBPJ7HcswEJBXTMcHnIuuC_jo_njvZxmpq9E7873LXyJGjdOtc5HVM9NuJTt9Lt1Exu8xUP2DnFix1dOvlY6I9ggK2KNEyHVtZdwjdF3Hg1ZERVaF82oKowgd1u0e8NiMWdefJBg3XMiRzbXmAnVT3zqRQejVAhHeuKIk_XEei1EGec7Bo4546xq3HH1fnyx2MvlOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sdvCPeuN5Pu9qxZajcTJNQur1vCNCdIaP4tjEaVBGs29TltqNeK4ihtwSgJMIr1coaaDB7VRNk0VO66kFlBf6-pX92p5bKeDAE_i0JFa21K5kjtV494bpndYbvXkG-qsUemd79DMng2fvf1YmQ7g9YwyILLRTj0hSMg5bxNqmvisJoQcqtV3NVj7mdI29IEm5fHw-yU3qU5WhxGnQMuK4Npkg2mL5UnKJbM_YnR2SFVIuiPTXk0TeudnobaD1iVZgvihgkNFG59NZMaJjemTHQhwp8InhKXBcruV3AwZiRm3LBX_kAh-1ya1K6PF2rN_p7aJ8U-XULNW_fInhGvtrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kodiRcjcKW0102kJCuDjq2uzJ1Jwb1eAkBS6y8kApVZ3H8Dfpt_tRPvL2SDJTi_35uuWV7gXE9kD5-6joGelW4-GKuGMB-W1RLpt1VQ9xrxAbmdIl8PSBxt_cOXN16i_at8b8nM_1MJF8D7CoaWuRWpk3iEQ2rm9qfu_k8zuTNPs9pPUrik5Qj1UO_RkfnXRPYBaGxpucXMySrxWq_kBpb3qZZO1ghPBPmF0KoI8vUf7S2NMLpkLBMcmHwnuXPTIYAozh-MenLTczR3iNVSRaMxAaIWfG9skfK9vRRgWTA549Ach0R9W2DPQYNwQDe2-4He1InA7TV54QPCRtP4ICw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bZ1_GHvqbFzbdSf8zd8JaTgfargCnJLpBXjwPfnAtVN-SFXeih14ahDCmRzXjdHA0Y7OPMWl-rv4CS4W8NqEyhvkrXmKYxYddy83TWdpRDlgO4Hrghlh-h9V2fy8-hEGgPsSnZYg2TmJlHQ0U1eclXl8TjH-kg2hzuVFN6ATriiIxsQdzZA20ojz1ruV_QeIXs8ETcYTKaHiL2Q4qt5oKI1AajZToc4oCsFeVfVJ-llmHUB5fGFl5SGFPUcy25JQC-vz9L-XS5bZ8pMBPEnzQIYLl0iyYfnQSMrwd-pC_PtFJZZ8ZJ-aXQ9Kn7Rxh02G6nkqncVO5v-87EZ12HOvEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SvN6ZpJcKTUIOwEQMKvA__pBwrtfXhuDzPZeAikRTFF345HkMvaGF5g6ayIJYAQxTPJEDVvgj7Q-P6YvusMECB_MC11LEjHlno5r9Ia3M7M-n2dlUadZmuMTnA49bJFPU3Fs14amk-PHHJSGRsjkBvdvCd595z5nV7I2p8eQYq3vhMdEMEt33O5IGvntnfSHipo7h-XEHSV4gEjeQCQ7GgPVxXet9s_V5OLnZX75sNRL3liwiCLYTuq9sNeZvj9czrIe3b5BP2_yW21ZpPJKwvdAGeMwgU36jwPbUyN08Jogk5sgggKuuA1kVbsCpSUEVQZM-C0X-a8JxzrP8s-NXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نگاه‌های بارانی به شهید قائد امت
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/447230" target="_blank">📅 21:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447229">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ba4e6e6d.mp4?token=EOSE_jncZILTbi4Kc6gv9MBYAraRDwWl060C87hhqijCD6yvV_F62VUCESBY7fgYSMt8-jwgu1P_tt7pKZbW1_do5PscsJ9fPGUSDMSze8VgC155ReU132IlS4CwM_LSVZWtzkXY54f08iNeMS23ohnfT6okxHFXjRjrrmdCubBori0xhAvTYq39yf1KEwK3uEmaPUf0KRWGovrvkWmr6nhYmu_4xq-cddKo8IKdnptEMJvobgngCo7jja26Urs7yl1kPLR_2xWLf0-Jl1g1Xe8k40qXtBGjSi0oHZIYxFrxU4Ni2gjf8SmM9N0I-UN7O9nGfiFO3UAKV9XpLTixrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ba4e6e6d.mp4?token=EOSE_jncZILTbi4Kc6gv9MBYAraRDwWl060C87hhqijCD6yvV_F62VUCESBY7fgYSMt8-jwgu1P_tt7pKZbW1_do5PscsJ9fPGUSDMSze8VgC155ReU132IlS4CwM_LSVZWtzkXY54f08iNeMS23ohnfT6okxHFXjRjrrmdCubBori0xhAvTYq39yf1KEwK3uEmaPUf0KRWGovrvkWmr6nhYmu_4xq-cddKo8IKdnptEMJvobgngCo7jja26Urs7yl1kPLR_2xWLf0-Jl1g1Xe8k40qXtBGjSi0oHZIYxFrxU4Ni2gjf8SmM9N0I-UN7O9nGfiFO3UAKV9XpLTixrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام میرهاشم حسینی: مسئولان در صورت تکرار تهدیدهای دشمن، پاسخی محکم به آن‌ها بدهند.
@Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/447229" target="_blank">📅 21:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447228">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1bc4a7fe9.mp4?token=HlKh4yxTBO4TtCgTUyWmZ224wQuCKdgcCbg9R4aHvJkffgMClgGOyNKBZxv9WE0x380fBPpuycy0eBYEqmNx19CYIUonYP1H1IS3GJcZOigit-VLyXQmSzhKn52bEXlU9ZLpsKsMLb5vZmqUGAVgMr9KhcPVy9nDuNyUX9MEqvX9N4bdDQXdG9ho3GBQ4QF3xSLSvP2T78wlCq21iE02rMMo0oe0_vM3AFti-TCXUyfTa-Sgf3Eme5vk80pUFWVd6T0Hq7PZqlcJ6kytN1ysqg40Sf45qH27J9eotI74gUBbaKjNySiacCDXBY_cabet5mlzDwg8PAfYi9lCiN54yTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1bc4a7fe9.mp4?token=HlKh4yxTBO4TtCgTUyWmZ224wQuCKdgcCbg9R4aHvJkffgMClgGOyNKBZxv9WE0x380fBPpuycy0eBYEqmNx19CYIUonYP1H1IS3GJcZOigit-VLyXQmSzhKn52bEXlU9ZLpsKsMLb5vZmqUGAVgMr9KhcPVy9nDuNyUX9MEqvX9N4bdDQXdG9ho3GBQ4QF3xSLSvP2T78wlCq21iE02rMMo0oe0_vM3AFti-TCXUyfTa-Sgf3Eme5vk80pUFWVd6T0Hq7PZqlcJ6kytN1ysqg40Sf45qH27J9eotI74gUBbaKjNySiacCDXBY_cabet5mlzDwg8PAfYi9lCiN54yTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی عبدالرضا هلالی در ساعات پایانی وداع با امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/447228" target="_blank">📅 21:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447226">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
برنامۀ وداع در مصلای تهران به‌دلیل ازدحام جمعیت تا ساعت ۲۲ تمدید شد.  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/447226" target="_blank">📅 21:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447225">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f38f101ed.mp4?token=b4KJT0TgxRJf7y_IkAJBJJKm24L_CquY4OsS0D5-ItWpZVfHdzSFMJuNunvqJm7Thdk3RBC-QfEVZOc7B7wOy8in67Mhu3ngTP2oOr9bGI_pN099LqnlSCPeOb_GBv5dp7UjjY3XChUQPBCSmVhYeuapXbELEArgNFYBWgdCM54srgh6_A2hLwk8aWuLFS1HafZbQBTmcUhGtX5mRP3EELhblc0FhdmzPryOS_zFlVDcjuQShVJ_aK_JoK3SimYbonIYGpDecmzPdkt_e7GYxVcar381XIHOLOkxgOjJDBeiTwhPZqP4jS2mJHemKrYpcRwBD22GPD58DQo0aNaFBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f38f101ed.mp4?token=b4KJT0TgxRJf7y_IkAJBJJKm24L_CquY4OsS0D5-ItWpZVfHdzSFMJuNunvqJm7Thdk3RBC-QfEVZOc7B7wOy8in67Mhu3ngTP2oOr9bGI_pN099LqnlSCPeOb_GBv5dp7UjjY3XChUQPBCSmVhYeuapXbELEArgNFYBWgdCM54srgh6_A2hLwk8aWuLFS1HafZbQBTmcUhGtX5mRP3EELhblc0FhdmzPryOS_zFlVDcjuQShVJ_aK_JoK3SimYbonIYGpDecmzPdkt_e7GYxVcar381XIHOLOkxgOjJDBeiTwhPZqP4jS2mJHemKrYpcRwBD22GPD58DQo0aNaFBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار تهران: خدمات ۲۴ ساعته مترو و حدود ۴ هزار اتوبوس جهت تسهیل رفت‌وآمد مردم در مراسم تشییع رهبر شهید فراهم شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/447225" target="_blank">📅 21:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447224">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34db08e600.mp4?token=umLT4Q1BSmo2HdCkpYBUyHlet4julww-iPbBm-vdnMgRhDNuD928s2_Jp8PwHDrcoiCEIWbkV-bwK-WS4sLMY_3unRX9u9v_HdowQ3AoMU4JpSPtqTH1P4kJ28Xt0D_FzolmtFtv7hc9EWcrVuXlVF82860BX8BKGXofaNHFBTDpdjti3-w8nHho-N5QEBUuB-2Xv_ideBxs5VJQ_4qRdt4d0-AAc25qsMHORb69a43b_MDRD0tsdhB9DkEf-awp2ilLBM7iWrk3I96gdxVGu3YPmzhbRVXC4lxPyqR1DhcEFVcUJRp3IEA0-VCnN-l5SEa60tguAN6SucjGpu_Ynw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34db08e600.mp4?token=umLT4Q1BSmo2HdCkpYBUyHlet4julww-iPbBm-vdnMgRhDNuD928s2_Jp8PwHDrcoiCEIWbkV-bwK-WS4sLMY_3unRX9u9v_HdowQ3AoMU4JpSPtqTH1P4kJ28Xt0D_FzolmtFtv7hc9EWcrVuXlVF82860BX8BKGXofaNHFBTDpdjti3-w8nHho-N5QEBUuB-2Xv_ideBxs5VJQ_4qRdt4d0-AAc25qsMHORb69a43b_MDRD0tsdhB9DkEf-awp2ilLBM7iWrk3I96gdxVGu3YPmzhbRVXC4lxPyqR1DhcEFVcUJRp3IEA0-VCnN-l5SEa60tguAN6SucjGpu_Ynw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«جنگ رسانه‌ای» علیه مراسم تشییع رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/447224" target="_blank">📅 21:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447223">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎥
قم آمادهٔ میزبانی از پسر فاطمه است
@Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/447223" target="_blank">📅 21:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447222">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114792c204.mp4?token=UorjZspbJ-vosn8PQ24v9lRW6u1oB8Vp_mmsy2lyweuPRQO7L0Ee_d9DAI4kqZPo4ODQ_ZxTtqpbcl40CFRPgE4JMhNQe6ycu6B5-UMzaxaxA4_aoJ9nZ-vwH8oR9DLuqU2SIrz7gcW_nFSLF6fpFs8smc5tBK3W11emfOJqotLwvySoY68smfPH_sWusTGdciwbv38TTDKy8GDgaOoxh4EtzVFkPb3Bf1YlDAc3vDZHQGihnswonXatQsC85Ln1xyzofPc5ONGj3JC_gDEixnCapxZwQbQHVriDpkebsJIw3b1JgaZhbkCqqDogxxxtFxyAFgv0aPUviQWsIBRRSYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114792c204.mp4?token=UorjZspbJ-vosn8PQ24v9lRW6u1oB8Vp_mmsy2lyweuPRQO7L0Ee_d9DAI4kqZPo4ODQ_ZxTtqpbcl40CFRPgE4JMhNQe6ycu6B5-UMzaxaxA4_aoJ9nZ-vwH8oR9DLuqU2SIrz7gcW_nFSLF6fpFs8smc5tBK3W11emfOJqotLwvySoY68smfPH_sWusTGdciwbv38TTDKy8GDgaOoxh4EtzVFkPb3Bf1YlDAc3vDZHQGihnswonXatQsC85Ln1xyzofPc5ONGj3JC_gDEixnCapxZwQbQHVriDpkebsJIw3b1JgaZhbkCqqDogxxxtFxyAFgv0aPUviQWsIBRRSYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این وداع ابدی است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/447222" target="_blank">📅 21:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447221">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e437001e1.mp4?token=jKhhP8bv_9NnsP8-y9etrvNYB4ELXxRDNWH8q8joC_vZua9w55lbDofRpmaDLaXA5WgpouOR125mRx1S5C_tOvj3KnZUumJ-SMEqraY9XB5zl7QQyGqWHfs9_EwUwYWjxOyyWZfGb04sxZwEAh7au5AMKhwUdF0IpaRgVKkMUxyORIyEmgLsplLh42CV-b0-SVVtJuMOY9KHSS837N-T5zMk2N4OqwT5K2R56X61L55rEGNhpCb3IMv9_mTT5RSkYaS8gMkLzIaLJSCptXsJzN_i_9EmMvEljLyxP-N2uZzs56CMYYqmpzYOf6XfKsRoPkZEh8ocJTcKqVlMoUEIfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e437001e1.mp4?token=jKhhP8bv_9NnsP8-y9etrvNYB4ELXxRDNWH8q8joC_vZua9w55lbDofRpmaDLaXA5WgpouOR125mRx1S5C_tOvj3KnZUumJ-SMEqraY9XB5zl7QQyGqWHfs9_EwUwYWjxOyyWZfGb04sxZwEAh7au5AMKhwUdF0IpaRgVKkMUxyORIyEmgLsplLh42CV-b0-SVVtJuMOY9KHSS837N-T5zMk2N4OqwT5K2R56X61L55rEGNhpCb3IMv9_mTT5RSkYaS8gMkLzIaLJSCptXsJzN_i_9EmMvEljLyxP-N2uZzs56CMYYqmpzYOf6XfKsRoPkZEh8ocJTcKqVlMoUEIfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطرهٔ دختر شهید مدافع حرم از آغوش رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/447221" target="_blank">📅 21:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447220">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3ab0fca99.mp4?token=NT17Q5hEziTKf8Q2s1_FLhn94QOg0cZeNLQfMICgXSNDQBABxHXbwUWZT2HPTKbrWDFyUzXR_QtOkUQCIjY3YLI1upMO7hE20KNeWN6mCPjSGJ1FhkFLpLqbx_ahWcHYQXagFobyDsnGNgtpgbp5ArDAdtJROXnJqbcA9BAzLCdLsVEne5gyLQL2cmaThSkjzlf-rz_NucRX8_Tzuc3KvBndv-YtA9kkUX-EUahDiGQFLE6Pnwb-dIojZlBKDa-zcWFTq1S0JiQJDNS_beIuotZxlyvh5FTL_AJKITXHwWwHQ5lK3bcsV_kWbpAwDPh1vdU-9-sZqnsTn5jWsyBL_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3ab0fca99.mp4?token=NT17Q5hEziTKf8Q2s1_FLhn94QOg0cZeNLQfMICgXSNDQBABxHXbwUWZT2HPTKbrWDFyUzXR_QtOkUQCIjY3YLI1upMO7hE20KNeWN6mCPjSGJ1FhkFLpLqbx_ahWcHYQXagFobyDsnGNgtpgbp5ArDAdtJROXnJqbcA9BAzLCdLsVEne5gyLQL2cmaThSkjzlf-rz_NucRX8_Tzuc3KvBndv-YtA9kkUX-EUahDiGQFLE6Pnwb-dIojZlBKDa-zcWFTq1S0JiQJDNS_beIuotZxlyvh5FTL_AJKITXHwWwHQ5lK3bcsV_kWbpAwDPh1vdU-9-sZqnsTn5jWsyBL_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
متروی مصلی مملو از جمعیت است  @Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/447220" target="_blank">📅 21:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447219">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1d0c68399.mp4?token=HX2ZJ-mA0JXCw2NcZb63uxhfgiIaean6veDUAYptKyo7Xh_4pCSp4AhAp4KcusWMtGn8DCDrIgkXN6F2YU7E6u3xk6tVe_6H2eOHgzPeSBeNRDnbws-dqmf_yuoMQ0m61VRJJ2HMmyXXtecAfjkqpjENJrNX4CVOscPDhNfjl2Tnj0bgKaeQPmRuInIPdN50ZPhYPD1qbw8aFWJNJm1_9h6SH4DaPnIcYe6-2kdqLi0JH4UMuw_fixWgZz3GY5GV6WAnfdMr3c5UrFUVWQiQsT5OZgrEoyS6E5Q2XDJE-HlkdQfx9Rkd32RWd-So2JUAf5qZ4si3hUGepBJjrFJJEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1d0c68399.mp4?token=HX2ZJ-mA0JXCw2NcZb63uxhfgiIaean6veDUAYptKyo7Xh_4pCSp4AhAp4KcusWMtGn8DCDrIgkXN6F2YU7E6u3xk6tVe_6H2eOHgzPeSBeNRDnbws-dqmf_yuoMQ0m61VRJJ2HMmyXXtecAfjkqpjENJrNX4CVOscPDhNfjl2Tnj0bgKaeQPmRuInIPdN50ZPhYPD1qbw8aFWJNJm1_9h6SH4DaPnIcYe6-2kdqLi0JH4UMuw_fixWgZz3GY5GV6WAnfdMr3c5UrFUVWQiQsT5OZgrEoyS6E5Q2XDJE-HlkdQfx9Rkd32RWd-So2JUAf5qZ4si3hUGepBJjrFJJEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار تهران: حضور میلیونی مردم در روزهای اخیر، نشان‌دهنده دو پیام روشن است؛ نخست، وحدت و انسجام ملی و دوم، تجدید بیعت ملت ایران با آیت‌الله سید مجتبی خامنه‌ای.
@Farsna</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/447219" target="_blank">📅 21:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447218">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f9b9fcd0.mp4?token=u4BqyXlNmEDsB4B14BV6AwMeQ8C2lhhlNcH-7pPAQtutzkSXrmQYQuaobaeFw9vQpZ5Cl2V53irvJM9OuIEutAonz6tFJ3q8MGsDwFiGXh0jrKQWTwtH4SMsy5EU0c1Ee3odrhxLARIoxAavJZ5K2KE1woctN2W7LJOjxxLqZnUiDkfjVSHWmmZSRpvg3QfbXBjeDGFUir1yTl8NKmaG2EjQhFh1vrEC4J8axT-OtDsdtX6iUpcEeabTaRizOHmlXJVu9LowQhBDVm_XkafEMWmyuyYNtO5wLqxXH5gfl2hKsy6csPrX6mO41ujmZBPZCcUfjLZQUdYBA2h8haPedg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f9b9fcd0.mp4?token=u4BqyXlNmEDsB4B14BV6AwMeQ8C2lhhlNcH-7pPAQtutzkSXrmQYQuaobaeFw9vQpZ5Cl2V53irvJM9OuIEutAonz6tFJ3q8MGsDwFiGXh0jrKQWTwtH4SMsy5EU0c1Ee3odrhxLARIoxAavJZ5K2KE1woctN2W7LJOjxxLqZnUiDkfjVSHWmmZSRpvg3QfbXBjeDGFUir1yTl8NKmaG2EjQhFh1vrEC4J8axT-OtDsdtX6iUpcEeabTaRizOHmlXJVu9LowQhBDVm_XkafEMWmyuyYNtO5wLqxXH5gfl2hKsy6csPrX6mO41ujmZBPZCcUfjLZQUdYBA2h8haPedg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقت سحر بود که رفتنت رو شنیدیم؛ چقدر گریه کردیم چه غصه‌ای کشیدیم
◾️
مداحی سیدرضا نریمانی برای آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/447218" target="_blank">📅 21:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447217">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4a22b97c6.mp4?token=NXZFXDYORH4bsV_eL1Ef4sgTGxCmvsS0smLdKp39_T-J-ZUi4_9JXfOfxSDg2Ro52EanFYore-TLoZJzvuNPE4KLhFq36ifEVNOQQou9b3L5-MCbx5BGC3wlXXSA8UxF14nWQ7ppSiJiv6-reBE4qKtysT2dpyqEfY1UoFOcMlWn4FFdISbAM8nPQUvkdO2J4BXTpsvZJ8VPL0iQzPQE8TpaGeHDfB6zUiQKNaHDbA_vPc5fUr7vHzPJue1C4ovcdVaTdMJhWKw-QaMFy_XZzH0_iR_ki3yEMXrhMby-qZoXetim53AErauO7lf_OF4x8J29WRVI_NNcScNNomtARA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4a22b97c6.mp4?token=NXZFXDYORH4bsV_eL1Ef4sgTGxCmvsS0smLdKp39_T-J-ZUi4_9JXfOfxSDg2Ro52EanFYore-TLoZJzvuNPE4KLhFq36ifEVNOQQou9b3L5-MCbx5BGC3wlXXSA8UxF14nWQ7ppSiJiv6-reBE4qKtysT2dpyqEfY1UoFOcMlWn4FFdISbAM8nPQUvkdO2J4BXTpsvZJ8VPL0iQzPQE8TpaGeHDfB6zUiQKNaHDbA_vPc5fUr7vHzPJue1C4ovcdVaTdMJhWKw-QaMFy_XZzH0_iR_ki3yEMXrhMby-qZoXetim53AErauO7lf_OF4x8J29WRVI_NNcScNNomtARA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قوم ما قومِ شهادت طلبِ پیروز است
🔹
نوحه‌خوانی امیر کرمانشاهی در شب دوم وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/447217" target="_blank">📅 21:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447216">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68e4e84657.mp4?token=TjBu5ovchEN8V8Lfr_IJPv3WAGreVkjp-OJXrhSjyCJLB7xnpqogkQVFkYPU8MF1aACVhdmlNmB6AbTlxFTFig9jhors4Bg3eqJY1ZZ08FVC2px-2nauv6xZzeEbQDNTBUvm8lvbOov0B5mvbzBAhADKpfES3MXz6OQkAAEs0_MTIfVPgEj-gNXJWhESPXKRkMzwDAjOsclEPROGjD5sIl2IpITe55wCgPmPmQeSOXxi83wATtkdqSRJLn4VyLMNqujionuzYWjd-ZTVB9YB7uGUUkMvrTRC4dX49WSfve-PouMhWuMmWKmnjuo4JIF69t4Pb0OJFOyatYaocn9ENw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68e4e84657.mp4?token=TjBu5ovchEN8V8Lfr_IJPv3WAGreVkjp-OJXrhSjyCJLB7xnpqogkQVFkYPU8MF1aACVhdmlNmB6AbTlxFTFig9jhors4Bg3eqJY1ZZ08FVC2px-2nauv6xZzeEbQDNTBUvm8lvbOov0B5mvbzBAhADKpfES3MXz6OQkAAEs0_MTIfVPgEj-gNXJWhESPXKRkMzwDAjOsclEPROGjD5sIl2IpITe55wCgPmPmQeSOXxi83wATtkdqSRJLn4VyLMNqujionuzYWjd-ZTVB9YB7uGUUkMvrTRC4dX49WSfve-PouMhWuMmWKmnjuo4JIF69t4Pb0OJFOyatYaocn9ENw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایمان قیاسی، مجری تلویزیون: درود بر غیرت خواهری که وسط برلین حرفی را زد و حجت را تمام کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/447216" target="_blank">📅 20:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447215">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9295861970.mp4?token=HBaw_rjGpJp3phkNwmqp3ib8UbNeEZIFkWA-ungtQSDCd4sw1f6LSroqJHUQhtCv9pNMLdisN6wU2KCINkNhRvyqnGYhkn7Mlk-rEQXtvuETAMpPdGGIw4Su_RfySyhgxmE9GGBgpTUowc002TuXV03xyjatGvXe0AvCNgoBRprikS8dvJ88hhKX22jWeDNemi7oE-j7PIOEgH4QFxSAIvHLFFye6zqdKxjV-y_AvPefP2MjeP3jlL2gCtwr6gzTMKiWI2RH8ocZhYP5_bs9pLShzEmRHxmOpO7Mob-TQ63hWPpoT5k_kKjGCU3S5j8MbAFXu-hSFaRxEKa7HAghTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9295861970.mp4?token=HBaw_rjGpJp3phkNwmqp3ib8UbNeEZIFkWA-ungtQSDCd4sw1f6LSroqJHUQhtCv9pNMLdisN6wU2KCINkNhRvyqnGYhkn7Mlk-rEQXtvuETAMpPdGGIw4Su_RfySyhgxmE9GGBgpTUowc002TuXV03xyjatGvXe0AvCNgoBRprikS8dvJ88hhKX22jWeDNemi7oE-j7PIOEgH4QFxSAIvHLFFye6zqdKxjV-y_AvPefP2MjeP3jlL2gCtwr6gzTMKiWI2RH8ocZhYP5_bs9pLShzEmRHxmOpO7Mob-TQ63hWPpoT5k_kKjGCU3S5j8MbAFXu-hSFaRxEKa7HAghTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام رحیمیان: تنها مسئولی که بدون وقت قبلی می‌توانستند خدمت امام راحل بیایند، رهبر شهید بودند.
@Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/447215" target="_blank">📅 20:55 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
